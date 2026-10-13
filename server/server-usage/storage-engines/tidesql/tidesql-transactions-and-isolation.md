---
description: >-
  The optimistic MVCC model, how MariaDB isolation levels map to the TidesDB
  library, consistent snapshots, savepoints, and how write conflicts surface.
---

# TideSQL Transactions and Isolation

TidesDB uses the library's multi-version concurrency control. Each statement runs inside a library transaction, and the engine keeps a per-connection transaction context through MariaDB's handlerton interface, the same shape InnoDB uses. The transaction object is created when the first statement locks a TidesDB table and is registered with the transaction coordinator. After commit or rollback it is kept and reused with `tidesdb_txn_reset()` on the next statement, which takes a fresh MVCC snapshot while preserving the internal buffers, so an autocommit statement does not pay a malloc and free each time.

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

This is the architectural difference from InnoDB, and it is worth stating plainly. TideSQL does not take pessimistic row locks. Concurrency is optimistic MVCC in the library. Readers never block writers and writers never block readers. When two transactions at `SNAPSHOT` or higher modify the same row, both proceed, and the second one to commit fails with a conflict rather than waiting.

Write-write conflict detection is a property of the higher isolation levels. At `SNAPSHOT` a commit claims each key it writes on a first-committer-wins basis rather than validating what it read, so two transactions that modify the same row cannot both commit. `SERIALIZABLE` keeps that check and adds the one the library's own `REPEATABLE_READ` level runs, validating at commit that every key the transaction read still holds the version it read and that no key appeared inside a range it scanned. At `READ_COMMITTED` the library does no write-write checking, which is why every autocommit statement, having no concurrent modification of its own, runs there.

The check runs inside `tidesdb_txn_commit()`, so a detected conflict fails the losing transaction's `COMMIT`. The engine maps `TDB_ERR_CONFLICT` to `HA_ERR_LOCK_DEADLOCK` (handler error 149), but because MariaDB reports any error raised from the commit callback as `ER_ERROR_DURING_COMMIT` (ERROR 1180) rather than `ER_LOCK_DEADLOCK` (1213), a commit-time conflict reaches the application as 1180 wrapping 149, as in `Got error 149 "Lock deadlock; Retry transaction" during COMMIT`. Transient contention or memory backpressure that fails a commit maps instead to `HA_ERR_LOCK_WAIT_TIMEOUT`, so it arrives as 1180 wrapping 146. The engine does not retry a failed commit. The transaction is rolled back and should be retried by the application.

{% hint style="warning" %}
MariaDB does not re-run an explicit `BEGIN ... COMMIT` block, so an application that uses explicit transactions at `REPEATABLE READ` or higher needs retry logic for error 1180.
{% endhint %}

An error the library reports inside a statement, before `COMMIT`, reaches the client as the plain server error, `ER_LOCK_DEADLOCK` (1213) for a conflict and `ER_LOCK_WAIT_TIMEOUT` (1205) for transient contention or memory backpressure. The engine first retries a transient contention error from a read, iterator open or seek, or write call a bounded number of times with a short backoff, about sixty milliseconds in all, so 1205 only surfaces when that retry runs out. A scan that fails partway reports the error rather than returning the rows it had read as the whole result. A cross-node conflict in a Galera cluster is described in [Replication and High Availability](tidesql-replication-and-ha.md).

Plain reads never take a lock at any isolation level, matching InnoDB's non-locking reads. `SELECT ... FOR UPDATE` and `LOCK IN SHARE MODE` take no lock either, and the engine treats them as ordinary reads. Whether a read is recorded for the commit-time check depends on the isolation level alone. At the default level, which maps to the library's snapshot isolation, reads are not tracked and only write-write conflicts are caught. At `SERIALIZABLE` the library also validates the read set, so a concurrent commit that changed a row this transaction only read makes its `COMMIT` fail. A transaction that wrote nothing never conflicts, because the engine ends it with a rollback rather than a commit. There is no lock wait and no wait-for-graph deadlock, only the commit-time conflict.

Neither model is strictly better. Optimistic MVCC removes all lock waits and lock-manager overhead, and a low-contention workload where most rows are touched by at most one writer at a time sees almost no conflicts. A workload with many transactions contending on a few hot rows, such as a single counter row, will see conflicts and depends on efficient retry.

## Consistent Snapshots

`START TRANSACTION WITH CONSISTENT SNAPSHOT` is supported. It eagerly creates the transaction and captures the snapshot sequence immediately rather than when the first statement locks a table, and it forces the isolation to at least `SNAPSHOT`, since a lower level would refresh the snapshot on each read and break the consistent-snapshot contract. Rows committed by other connections after the snapshot are invisible. This is useful for cross-engine consistency when TidesDB and InnoDB tables share a transaction:

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

Statements that touch many rows, such as `LOAD DATA INFILE`, multi-row `INSERT`, `INSERT ... SELECT`, and range `DELETE`, keep the transaction from growing without bound by committing mid-statement in fixed-size batches, but only when the statement is its own transaction, under autocommit or as the copy step of DDL such as `ALTER TABLE`. Inside `BEGIN`, or with `autocommit=0`, every write stays in the transaction, so `COMMIT` or `ROLLBACK` covers all of it. The engine hooks `start_bulk_insert` and `start_bulk_delete`, counts row operations (the data write plus secondary-index maintenance) against a batch size of 500 operations, and at each threshold commits the current transaction and carries on in a fresh transaction at `READ_COMMITTED` for the next batch. Statement memory stays bounded regardless of statement size, a failure rolls back only the current batch, and the statement reports the first error it hit. Rows committed by an earlier batch stay committed, so a later failure in the same statement cannot roll them back. An `UPDATE` does not batch, because the engine does not advertise `HA_CAN_FORCE_BULK_UPDATE`. One exception is a range `DELETE` on a table with an explicit primary key, no triggers, and no Galera. The engine defers its primary-row tombstones so the whole range can become one range tombstone, holds back the mid-statement commits while it buffers, and bounds memory with a key cap instead. See [TideSQL Write-Path Optimizations](tidesql-write-path-optimizations.md).

A `DELETE` with no `WHERE` clause runs row by row inside its transaction like any other `DELETE`, since the engine declines `delete_all_rows`. Only `TRUNCATE TABLE`, which commits implicitly and holds an exclusive lock, drops and recreates the table's column families.

## Group Commit

The engine participates in binlog group commit. When a batch of transactions commits together, the durable commit runs in binlog order through the `commit_ordered` hook, which lets the server run the rest of commit outside the commit-order lock. Each commit's durable write is issued in that order, and since the ordered phase runs one transaction at a time, each commit of a binlog group waits for its own log write. Commits whose log writes reach the library's WAL at the same time, such as concurrent prepares with the binlog enabled, are written out by the WAL flush thread together and wait on the same flush. For what `FULL` sync costs, see [Durability and Sync Modes](tidesql-durability-and-sync-modes.md).

## Crash Recovery and Two-Phase Commit

TideSQL is a full two-phase commit participant, so it recovers to a consistent point after a crash and coordinates with the binlog and with external XA. In the prepare phase the engine logs the transaction's write batch under its XID, durably under the default `FULL` sync mode (see `tidesdb_memtable_sync_mode`), so a crash after prepare but before commit leaves an in-doubt transaction that recovery resolves rather than loses.

When the server restarts it asks the engine to recover, and the engine reports every in-doubt prepared transaction the library recovered and holds each one in a process-wide registry, so the coordinator can commit or roll it back to match the binlog. An external `XA PREPARE` keeps the transaction attached to its connection and also registers it in the same registry, which takes ownership if the client disconnects, so a distributed transaction survives the client disconnecting between `XA PREPARE` and `XA COMMIT`:

```sql
XA START 'txn1';
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
XA END 'txn1';
XA PREPARE 'txn1';
-- the prepared transaction can be committed from any connection (durable under FULL sync)
XA COMMIT 'txn1';
```

<sub>_This page is licensed: GPLv2_</sub>
