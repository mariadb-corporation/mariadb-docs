---
description: >-
  What the TideSQL storage engine does not do, and the behaviors to plan around,
  including foreign-key shapes, copy-only DDL, stats caching, and commit-time conflicts.
---

# TideSQL Limitations

**Foreign keys carry two shape restrictions.** TideSQL enforces foreign keys inside the engine, including `ON DELETE` and `ON UPDATE` with `CASCADE`, `SET NULL`, and `RESTRICT`, references to a primary key or to a non-nullable unique key, and self-references. Two constraint shapes are rejected at `CREATE TABLE` and `ALTER TABLE`. A foreign key column declared with descending order is not allowed, because the engine matches child rows against a forward sort key. A foreign key that references a nullable unique key is not allowed either, because the value-only child probe cannot reproduce that key's null indicator. Everything else behaves as in InnoDB. See [TideSQL Foreign Keys](tidesql-foreign-keys.md) for the full description.

**Changing the primary key or a column type needs a full copy.** The engine does not support an inplace primary-key change, and changing a column type such as `INT` to `BIGINT` also rebuilds the table by copy. See [TideSQL Online DDL](tidesql-online-ddl.md).

**Statistics are cached for up to two seconds.** Right after a bulk load the optimizer may briefly see stale row counts. `ANALYZE TABLE` forces an immediate refresh.

**Write conflicts surface at commit and are the application's to retry.** Concurrency is optimistic MVCC, so a multi-statement transaction at `REPEATABLE READ` or higher can fail at commit with a first-committer-wins conflict, which reaches the client as `ER_ERROR_DURING_COMMIT` (ERROR 1180). An application that uses explicit `BEGIN ... COMMIT` blocks at those levels should retry on that error. MariaDB retries autocommit statements automatically. There are no pessimistic row locks, so there are no lock waits and no lock-wait deadlocks to tune. See [TideSQL Transactions and Isolation](tidesql-transactions-and-isolation.md).

<sub>_This page is licensed: GPLv2_</sub>
