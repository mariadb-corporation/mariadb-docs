---
description: >-
  How TideSQL keeps delete-heavy and write-heavy workloads from degrading:
  single-delete, the tombstone-density trigger, range deletes, batched bulk
  statements, and backpressure.
---

# TideSQL Write-Path Optimizations

This page describes how the engine keeps delete-heavy and write-heavy workloads from slowing down as tombstones and unflushed writes build up. Most of these optimizations are automatic. The ones that change semantics are opt-in through session variables.

## Single-Delete

A `DELETE` writes a tombstone into every column family the row touches: the primary row column family plus one column family per secondary, full-text, or spatial index. A regular tombstone must be carried through every compaction until it reaches the largest active level, because a lower level could still hold an older put of the same key that the tombstone masks. Insert-then-delete workloads pile these up at the low end of the key space, where `DELETE` range scans start, and scan cost climbs with the backlog until compaction catches up.

The library's single-delete primitive lets compaction drop a put and its matching tombstone together at whatever level the merge writes, instead of carrying the tombstone down to the largest level. It drops the pair only when the put lies directly beneath the single-delete, no reader can still see that put, and no SSTable outside the merge holds the key, and a single-delete it keeps is written back still a single-delete so a later merge can drop it. Its contract is at most one put between single-deletes on the same key. For reads, a single-delete behaves like a regular tombstone.

The engine applies single-delete in two ways.

### Secondary-Index Single-Delete (Automatic)

Every secondary index entry, `(col_values, pk)` for a regular index, `(term, pk)` for `FULLTEXT`, and `(hilbert, pk)` for `SPATIAL`, is written exactly once per row lifetime and deleted exactly once, across `INSERT`, `UPDATE`, `DELETE`, `REPLACE INTO`, and `INSERT ... ON DUPLICATE KEY UPDATE`. Two `UPDATE` paths write an entry again in place, one that refreshes the expiry of a row in a table with a TTL and one that rewrites a `FULLTEXT` term whose frequency or document length changed. A later single-delete of such an entry still leaves it gone, because the library keeps a single-delete while any SSTable outside the merge holds the key, and a merge that drops it drops every older version of the key with it. The engine therefore uses single-delete for every secondary-index delete with no configuration. On a table with three secondary indexes, that covers three of the four tombstones per deleted row.

The uniqueness sentinel that a `UNIQUE` secondary index keeps in the shared `__tidesdb_uniq` column family is the exception. The same value can be written and removed any number of times over a sentinel's life, so its delete is a regular tombstone.

### Primary Column Family Single-Delete (Opt-In)

The primary row column family is different. `UPDATE ... SET non_pk_col` writes a fresh row at the same key, a put over a put, and `REPLACE INTO` on a table without secondary indexes overwrites silently for the same reason. Either pattern leaves more than one put under a later single-delete, outside the library's contract, and the engine cannot tell from outside which rows those are. Primary single-delete is therefore behind the session variable [tidesdb\_single\_delete\_primary](tidesql-system-variables.md), which defaults to `OFF`.

```sql
SET SESSION tidesdb_single_delete_primary = 1;
INSERT INTO events (...) VALUES ...;   -- monotonic PK
DELETE FROM events WHERE ts < NOW() - INTERVAL 1 HOUR;
```

{% hint style="warning" %}
Enabling `tidesdb_single_delete_primary` is a promise that the session performs no `UPDATE` on non-primary-key columns, no `REPLACE INTO` or `INSERT ... ON DUPLICATE KEY UPDATE` on the silent-overwrite path, and that a new row for a given primary key is always preceded by a `DELETE` of that key. Leave it `OFF` for any session that may issue those statements, because they break the at-most-one-put promise the library asks of every single-delete caller.
{% endhint %}

## Tombstone-Density Trigger

Single-delete handles the insert-then-delete shape where its contract holds. For everything else, such as updates of indexed columns, `REPLACE INTO` on tables without secondary indexes, and mixed OLTP, tombstones accumulate inside SSTables until a compaction at the largest level reclaims them, and a read over a deleted region pays for every tombstone the merge iterator skips.

The tombstone-density trigger lets the engine act on this without waiting for a capacity or file-count trigger. When the library's compaction planner evaluates a column family, it checks whether any one SSTable, at any level, has a tombstone count divided by entry count at or above a ratio while holding at least a minimum entry count. A single such SSTable escalates compaction.

The `TOMBSTONE_DENSITY_TRIGGER` and `TOMBSTONE_DENSITY_MIN_ENTRIES` [table options](tidesql-table-options.md) turn it on. The aggregates show up in the `Tidesdb_total_tombstones`, `Tidesdb_tombstone_ratio`, `Tidesdb_max_sst_tombstone_density`, and `Tidesdb_max_sst_tombstone_density_level` [status variables](tidesql-status-variables.md), and in the Tombstones block of `SHOW ENGINE TIDESDB STATUS`.

## Compacting After a Range Delete

Sliding-window expiry, tenant eviction, and time-bucketed log rotation share a shape: a multi-row `DELETE` over a known primary-key range, followed by a wait for compaction to reclaim the space. A session that knows it runs such deletes can skip the wait with [tidesdb\_compact\_after\_range\_delete\_min\_rows](tidesql-system-variables.md):

```sql
SET SESSION tidesdb_compact_after_range_delete_min_rows = 100000;
DELETE FROM events WHERE ts < NOW() - INTERVAL 30 DAY;
```

The default `0` disables it. A non-zero value is both an opt-in and a row-count threshold, so only a `DELETE` touching at least that many rows triggers the compaction, and a one-row `DELETE` never pays for it.

The engine tracks the smallest and largest primary key seen during the statement, with no extra scan or locking, and at the end of the statement queues that range on the transaction, with an end bound just past the largest deleted key. Secondary-index tombstones are not compacted this way, because a primary-key range does not bound a secondary-index range. They are left to the tombstone-density trigger.

After the transaction commits, the engine flushes the memtable once so the tombstones reach SSTables, then compacts each queued range on the primary column family synchronously on the committing thread, so the commit returns only after it finishes. Under autocommit that is the `DELETE` itself. Set the threshold high enough that the compaction time is small relative to the `DELETE` that triggered it. A transaction that rolls back compacts nothing. If another compaction already holds the column family, the request is skipped, since that compaction absorbs the work. Any other flush or compaction failure is logged as a warning in the error log and does not fail the commit.

## Range Tombstone for a Whole-Range Delete

When a multi-row `DELETE` removes every row across a contiguous primary-key span, the engine writes one range tombstone over the span instead of a tombstone for each key. One interval in the WAL and in the memtable replaces thousands, and compaction drops the whole span in a single step rather than carrying each tombstone through the levels.

The engine cannot know in advance that a `DELETE` covers a clean range, so it works it out as it goes. During the statement, it buffers each deleted primary-row key and holds its tombstone back. With the tombstones deferred, every row the statement deleted is still live, so at the end of the statement the number of live rows between the smallest and largest buffered key equals the number of buffered keys exactly when the statement removed the whole span. In that case one range delete replaces the run.

A surviving row leaves more live rows than buffered keys, and the buffer falls back to per-row tombstones with no change in the result. A survivor can come from a residual `WHERE` condition, a gap in an `IN` list, a row rejected by index condition pushdown, or an `ORDER BY ... LIMIT` that picks scattered rows. Everything happens inside the transaction, so a `ROLLBACK` restores the rows like any other write.

The following rules apply:

* Deferral applies only to a table with an explicit primary key.
* It is skipped for a table with triggers, since a deferred tombstone must never hide a row from a trigger that reads the table mid-statement.
* It is skipped under Galera, where a deferred range tombstone would not line up with the per-row certification the write path already issues.
* Secondary-index entries are still deleted per row, so the range tombstone covers the primary row column family alone.
* A run of fewer than 64 buffered rows is written as per-row tombstones without the completeness check, which would cost more than it saves.
* While it defers, the `DELETE` also holds off the batch commits described in the next section.
* A delete larger than an internal cap of 262,144 keys flushes its buffer to per-row tombstones and finishes on the ordinary path, which keeps the buffered keys to a few megabytes.
* When the range tombstone is written, it already reclaims the span, so the compact-after-range-delete pass is skipped for that statement.

## Batched Bulk Statements

A multi-row `INSERT` or `DELETE` that MariaDB runs as a bulk operation commits its writes in batches, rather than holding the whole write set in one transaction, but only when the statement is its own transaction, under autocommit or as the copy step of DDL such as `ALTER TABLE`. Inside `BEGIN`, or with `autocommit=0`, every write stays in the transaction, so its `COMMIT` or `ROLLBACK` covers all of it. An `UPDATE` does not batch, because the engine does not advertise `HA_CAN_FORCE_BULK_UPDATE`. The engine counts one operation per row plus one per secondary index. When the count reaches 500, it commits mid-statement.

It does not reset the committed transaction. It begins a fresh `READ COMMITTED` transaction for the rest of the statement and parks the committed one until the transaction ends. This is because the source table of an `INSERT ... SELECT`, the scan of a batched `DELETE`, or an `ALTER TABLE` copy can still be iterating under the committed transaction, and a reset would end that scan early. Rows committed by a batch are durable, so a later failure in the same statement cannot roll them back. Under Galera a statement other than DDL commits as a whole instead, since a batch committed before the statement's write set was certified would stay on this node alone if the statement then failed. DDL runs on every node in total order and replicates no rows, so its copy still batches.

Because only autocommit and DDL statements batch, and the engine already runs both at `READ COMMITTED`, the first batch commits at `READ COMMITTED` like every later one. A statement inside `BEGIN` keeps the session's isolation level and its snapshot, since it never batches. For how this interacts with isolation, see [Transactions and Isolation](tidesql-transactions-and-isolation.md).

A `DELETE` with no `WHERE` clause takes this same row-by-row path inside its transaction, because the engine declines `delete_all_rows`, and on a table with an explicit primary key the range tombstone above can collapse it into one interval. Only `TRUNCATE TABLE` drops and recreates the table's column families.

## Backpressure

When ingest outruns flush, the library applies backpressure at its L0 admission policy, making a commit dwell or wait for the flush queue to drain before it is admitted. This happens inside the library, so a writer is slowed rather than failed. The effect is visible in the write-stall [status variables](tidesql-status-variables.md): `Tidesdb_writes_throttled`, `Tidesdb_writes_blocked`, `Tidesdb_write_stall_us`, and `Tidesdb_write_stall_ceiling_hits`. A sustained rise in `Tidesdb_write_stall_ceiling_hits` is the sign that flush is not keeping up with ingest.

Only when the library's own no-progress budget is spent, with the memtable, flush queue, or L0 backlog still at its cap, does the library report a memory-limit error to the engine. The engine maps it to `HA_ERR_LOCK_WAIT_TIMEOUT`, which reaches the client as error 1205 inside a statement, and counts it in `Tidesdb_stmt_memory_limit`. The statement can be retried once flush has caught up.

The engine also absorbs transient contention that the library reports as locked, typically a memtable rotation that outran a single call's own retries. The engine's read, write, delete, iterator-open, and iterator-seek calls retry up to 16 times with a short, growing backoff, about 60 milliseconds in total, and stop early if the session is killed. Only then does the statement fail with a lock wait timeout. A commit is never retried, because a failed commit leaves the transaction aborted, and neither is a step to the next or previous entry, because a failed step does not say where it left the iterator. In a query or a write, an iterator call that still fails ends the statement with an error rather than as the end of the data, so a scan does not hand back part of its rows as the whole result.

<sub>_This page is licensed: GPLv2_</sub>
