---
description: >-
  The optimistic MVCC model, how MariaDB isolation levels map to the TidesDB
  library, consistent snapshots, savepoints, and how write conflicts surface.
---

# TideSQL Transactions and Isolation

TidesDB uses the library's multi-version concurrency control. Each statement runs inside a library transaction, and the engine keeps a per-connection transaction context through MariaDB's handlerton interface, the same shape InnoDB uses. The transaction object is allocated lazily on the first data access and registered with the transaction coordinator. After commit or rollback it is kept and reused with `tidesdb_txn_reset()` on the next statement, which takes a fresh MVCC snapshot while preserving the internal buffers, so an autocommit statement does not pay a malloc and free each time.

Autocommit single-statement DML runs at `READ_COMMITTED`, because a single statement has no concurrent modification of its own to track and conflict tracking would be wasted work. Multi-statement transactions inside `BEGIN ... COMMIT` use the session isolation level.

## Isolation Levels

The engine honors the session isolation level from `SET TRANSACTION ISOLATION LEVEL`. The mapping to the library is:

| MariaDB | TidesDB |
|---------|---------|
| `READ UNCOMMITTED` | `TDB_ISOLATION_READ_UNCOMMITTED` |
| `READ COMMITTED` | `TDB_ISOLATION_READ_COMMITTED` |
| `REPEATABLE READ` | `TDB_ISOLATION_SNAPSHOT` |
| `SERIALIZABLE` | `TDB_ISOLATION_SERIALIZABLE` |

`REPEATABLE READ` resolves through the per-table `ISOLATION_LEVEL` option. A table that leaves the option at its default `REPEATABLE_READ` maps to the library's `SNAPSHOT`, which is the semantic match for InnoDB's repeatable-read, a consistent-read snapshot with write-write conflict detection and no read-set tracking. The library's own `REPEATABLE_READ` level is stricter, it tracks the read set and detects read-write conflicts at commit, which produces excessive conflicts under normal OLTP, so it is not the default. A table that sets `ISOLATION_LEVEL` to `SNAPSHOT`, `SERIALIZABLE`, `READ_COMMITTED`, or `READ_UNCOMMITTED` is honored as written, so a workload can pin a tighter or looser level per table without moving the session default. A session that explicitly requests `READ UNCOMMITTED`, `READ COMMITTED`, or `SERIALIZABLE` bypasses the table option and uses the session level.

The available per-table levels are `READ_UNCOMMITTED`, `READ_COMMITTED`, `REPEATABLE_READ`, `SNAPSHOT`, and `SERIALIZABLE`, set at `CREATE TABLE`:

```sql
CREATE TABLE ledger (
  id INT PRIMARY KEY, amt DECIMAL(10,2)
) ENGINE=TIDESDB ISOLATION_LEVEL='SERIALIZABLE';
```

DDL such as `ALTER TABLE`, `CREATE INDEX`, `DROP INDEX`, `TRUNCATE`, and `OPTIMIZE`, along with autocommit single-statement DML, always runs at `READ_COMMITTED` regardless of the session, to keep a large scan from accumulating an unbounded read set.

## Optimistic Concurrency, Not Locks

This is the architectural difference from InnoDB, and it is worth stating plainly. TideSQL does not take pessimistic row locks. Concurrency is optimistic MVCC in the library. Readers never block writers and writers never block readers. When two transactions modify the same row, both proceed, and the second one to commit fails with a conflict rather than waiting.

Write-write conflict detection is a property of the higher isolation levels. At `SNAPSHOT` and `SERIALIZABLE` the library validates each write against the version the transaction actually read, recorded in its conflict footprint, and runs a first-committer-wins check before the write log, so two transactions that modify the same row cannot both commit. At `READ_COMMITTED` the library does no write-write checking, which is why every autocommit statement, having no concurrent modification of its own, runs there.

The check runs inside `tidesdb_txn_commit()`, so a detected conflict fails the losing transaction's `COMMIT`. The engine maps `TDB_ERR_CONFLICT` to `HA_ERR_LOCK_DEADLOCK`, but because MariaDB reports any error raised from the commit callback as `ER_ERROR_DURING_COMMIT` (ERROR 1180) rather than `ER_LOCK_DEADLOCK` (1213), a commit-time conflict reaches the application as 1180. The transaction is rolled back cleanly and should be retried.

{% hint style="warning" %}
MariaDB retries autocommit statements automatically but does not re-run an explicit `BEGIN ... COMMIT` block, so an application that uses explicit transactions at `REPEATABLE READ` or higher needs retry logic for error 1180. A cross-node conflict in a Galera cluster is surfaced differently, as a clean `ER_LOCK_DEADLOCK` (1213), described in [Replication and High Availability](tidesql-replication-and-ha.md).
{% endhint %}

Plain reads never take a lock at any isolation level, matching InnoDB's non-locking reads. Whether a read is recorded into the conflict footprint depends on the isolation level, not on `FOR UPDATE` or `LOCK IN SHARE MODE`, which the engine treats as ordinary reads. At the default level, which maps to the library's snapshot isolation, reads are not tracked and only write-write conflicts are caught. At `SERIALIZABLE` the engine also tracks the read set, so a concurrent write to a row this transaction only read makes it lose the first-committer-wins check at commit. There is no lock wait and no wait-for-graph deadlock, only the commit-time conflict.

Neither model is strictly better. Optimistic MVCC removes all lock waits and lock-manager overhead, and a low-contention workload where most rows are touched by at most one writer at a time sees almost no conflicts. A workload with many transactions contending on a few hot rows, such as a single counter row, will see conflicts and depends on efficient retry.

## Consistent Snapshots

`START TRANSACTION WITH CONSISTENT SNAPSHOT` is supported. It eagerly creates the transaction and captures the snapshot sequence immediately rather than at the first data access, and it forces the isolation to at least `SNAPSHOT`, since a lower level would refresh the snapshot on each read and break the consistent-snapshot contract. Rows committed by other connections after the snapshot are invisible. This is useful for cross-engine consistency when TidesDB and InnoDB tables share a transaction:

```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION WITH CONSISTENT SNAPSHOT;
SELECT * FROM tidesdb_table;   -- sees data as of snapshot time
SELECT * FROM innodb_table;    -- InnoDB snapshotted at the same point
COMMIT;
```

## Savepoints

SQL savepoints (`SAVEPOINT`, `ROLLBACK TO SAVEPOINT`, `RELEASE SAVEPOINT`) are supported inside explicit multi-statement transactions. They are only meaningful within a `BEGIN ... COMMIT` block.

## Bulk DML Batching

Statements that touch many rows, such as `LOAD DATA INFILE`, multi-row `INSERT`, `INSERT ... SELECT`, and range `UPDATE` or `DELETE`, keep the transaction from growing without bound by committing mid-statement in fixed-size batches. The engine hooks `start_bulk_insert`, `start_bulk_update`, and `start_bulk_delete`, counts row operations (the data write plus secondary-index maintenance) against a batch size of 500 operations, and at each threshold commits the current transaction and resets it at `READ_COMMITTED` for the next batch. Statement memory stays bounded regardless of statement size, autocommit semantics are preserved so a failure rolls back only the current batch, and the statement reports the first error it hit. The mid-statement commit is shared across insert, update, and delete through one helper, so the threshold and the iterator and dup-cache invalidation are identical on all three paths.

## Group Commit

The engine participates in binlog group commit. When a batch of transactions commits together, the durable commit runs in binlog order through the `commit_ordered` hook, which lets the server run the rest of commit outside the commit-order lock. The transactions in one commit round share the cost of a single durability barrier, so on a busy server throughput scales with the size of the group rather than paying a separate barrier per commit. This is what keeps `FULL` sync affordable under load, as covered in [Durability and Sync Modes](tidesql-durability-and-sync-modes.md).

## Crash Recovery and Two-Phase Commit

TideSQL is a full two-phase commit participant, so it recovers to a consistent point after a crash and coordinates with the binlog and with external XA. In the prepare phase the engine durably logs the transaction's write batch under its XID, so a crash after prepare but before commit leaves an in-doubt transaction that recovery resolves rather than loses. A prepared transaction is held in a process-wide registry, so its commit or rollback decision can arrive from another connection or after a restart.

When the server restarts it asks the engine to recover, and the engine replays every in-doubt prepared transaction so the coordinator can commit or roll each one back to match the binlog. An external `XA PREPARE` detaches the transaction to the same registry, so a distributed transaction survives the client disconnecting between `XA PREPARE` and `XA COMMIT`:

```sql
XA START 'txn1';
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
XA END 'txn1';
XA PREPARE 'txn1';
-- the prepared transaction is durable and can be committed from any connection
XA COMMIT 'txn1';
```

<sub>_This page is licensed: GPLv2_</sub>
