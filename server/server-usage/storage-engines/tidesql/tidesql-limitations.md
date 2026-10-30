---
description: >-
  What the TideSQL storage engine does not do, and the behaviors to plan around,
  including foreign-key shapes, copy-only DDL, stats caching, and commit-time conflicts.
---

# TideSQL Limitations

**Foreign keys carry a few shape restrictions.** TideSQL enforces foreign keys inside the engine, including `ON DELETE` and `ON UPDATE` with `CASCADE`, `SET NULL`, and `RESTRICT`, references to a primary key or to a non-nullable unique key, and self-references. The referenced columns must be every column of the parent's primary key or of a `NOT NULL` unique key. A reference to parent columns that carry only a plain index, or to the leading columns of a composite key, is rejected at `CREATE TABLE` and `ALTER TABLE`, where InnoDB accepts it, and so is a reference to a nullable unique key, because the value-only child probe cannot reproduce that key's null indicator. A foreign key column declared with descending order is rejected too, because the engine matches child rows against a forward sort key. One difference goes the other way, since a self-referencing `ON UPDATE CASCADE` is applied, where InnoDB treats it as `RESTRICT`. Cascades nest at most 15 levels deep, as in InnoDB. See [TideSQL Foreign Keys](tidesql-foreign-keys.md) for the full description.

**Only appending a column is instant.** Rows store their fields by position, so `DROP COLUMN`, `ADD COLUMN ... FIRST` or `AFTER`, and any column reorder rebuild the table by copy, as do a change to the primary key or to a column type such as `INT` to `BIGINT`. Appending a `BIT` column or a stored generated column copies too, and so does an append that changes the row's null layout, such as the first `VARCHAR` added to a table of only fixed-length columns. Turning encryption on or off, or changing `ENCRYPTION_KEY_ID` on an encrypted table, also copies, because every row is rewritten under the new key. Adding a regular secondary index runs inplace but blocks writes until the build finishes, so `LOCK=NONE` is refused, and a `FULLTEXT` or `SPATIAL` index is added by copy. See [TideSQL Online DDL](tidesql-online-ddl.md).

**Statistics are cached for up to two seconds.** Right after a bulk load the optimizer may briefly see stale row counts. `ANALYZE TABLE` forces an immediate refresh.

**Write conflicts surface at commit and are the application's to retry.** Concurrency is optimistic MVCC, so a multi-statement transaction at `REPEATABLE READ` or higher can fail at commit with a first-committer-wins conflict, which reaches the client as `ER_ERROR_DURING_COMMIT` (ERROR 1180) wrapping handler error 149, or 146 for transient contention. An error raised inside a statement instead arrives as `ER_LOCK_DEADLOCK` (1213) or `ER_LOCK_WAIT_TIMEOUT` (1205). An application that uses explicit `BEGIN ... COMMIT` blocks at those levels should retry on these errors. Autocommit statements run at `READ COMMITTED`, where the library does no write-write checking, and a transaction that wrote nothing never conflicts. There are no pessimistic row locks, and `SELECT ... FOR UPDATE` takes none, so there are no lock waits and no lock-wait deadlocks to tune. See [TideSQL Transactions and Isolation](tidesql-transactions-and-isolation.md).

<sub>_This page is licensed: GPLv2_</sub>
