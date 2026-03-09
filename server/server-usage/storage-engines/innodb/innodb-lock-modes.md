---
description: >-
  InnoDB employs Row-Level Locking with Shared (S) and Exclusive (X) locks,
  along with Intention locks, to manage concurrent transaction access.
---

# InnoDB Lock Modes

Locks are acquired by a transaction to prevent concurrent transactions from modifying, or even reading, some rows or ranges of rows. This is done to make sure that concurrent write operations never collide.

[InnoDB](./) supports a number of lock modes.

## Shared and Exclusive Locks

The two standard row-level locks are _share locks_(S) and _exclusive locks_(X).

A shared lock is obtained to read a row, and allows other transactions to read the locked row, but not to write to the locked row. Other transactions may also acquire their own shared locks.

An exclusive lock is obtained to write to a row, and stops other transactions from locking the same row. It's specific behavior depends on the [isolation level](../../../reference/sql-statements/transactions/set-transaction.md); the default (REPEATABLE READ), allows other transactions to read from the exclusively locked row.

## Locks Apply to Index Records, Not Logical Table Rows

In InnoDB, when using `LOCK IN SHARE MODE` under the `READ COMMITTED` isolation level, it is critical to understand that locking reads are based on index records and not on abstract table rows. This difference is important, when using locking reads like these:

```
SELECT ... LOCK IN SHARE MODE;
SELECT ... FOR UPDATE;
```

InnoDB's locking engine works at the index record level, but a query logically focuses on a row. Therefore, based on the isolation level and data creation order, lock conflicts can be avoided if two simultaneous transactions access the same row through different indexes.

### Index Reads and Lock Behavior

When a secondary index matches a transaction, InnoDB:

* Reads only the secondary index
* locks the secondary index records
* Avoids accessing the primary index record

If another transaction alters a column that is not included in the secondary index, only the primary index record can be locked. In that case, the two transactions lock different index records without blocking each other.

### Example

The following scenario illustrates a case where `SELECT ... LOCK IN SHARE MODE` does not prevent a concurrent update, even though both statements refer to the same logical rows:

```
CREATE TABLE tbl_1 (
  col_1_1 TIMESTAMP,
  col_1_2 VARCHAR(100),
  col_1_3 MEDIUMINT,
  col_1_4 INT,
  col_1_5 DOUBLE,
  col_1_6 NUMERIC,
  pkid_1 INT,
  INDEX idx_1_1 (col_1_4, col_1_2, col_1_3, col_1_5),
  PRIMARY KEY (col_1_4, pkid_1)
) ENGINE=InnoDB;
```

Here:

* `PRIMARY KEY (col_1_4, pkid_1)` -> Clustered Index (Primary Index Record)
* `INDEX idx_1_1 (col_1_4, col_1_2, col_1_3, col_1_5)` -> Secondary Index (Secondary Index Record)

**Sample Data**

```
INSERT INTO tbl_1 VALUES
('2025-12-19 16:46:56','str_002',2,3,1,1,0),
('2025-12-19 16:46:56','str_002',2,3,2,1,1),
('2025-12-19 16:46:57','str_002',1,3,2,1,2),
('2025-12-19 16:46:56','str_002',1,3,2,1,3),
('2025-12-19 16:46:57','str_002',1,3,2,1,4),
('2025-12-19 16:46:56','str_002',1,1,2,1,5),
('2025-12-19 16:46:56','str_002',1,2,2,1,6);
```

**Connection 1**

```
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN;
 
SELECT col_1_4, col_1_2, pkid_1 FROM tbl_1 WHERE col_1_3 > 1 LOCK IN SHARE MODE;
```

**What happens**

* The query makes use of the secondary index `idx_1_1`.
* The query reads `col_1_4`, `col_1_2`, and `pkid_1`, which are part of `idx_1_1`.
* This is a covering or secondary index read.
* InnoDB skips the primary index and only applies shared locks to records in `idx_1_1`.

**Default Connection (Concurrent)**

```
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN;
 
UPDATE tbl_1
SET col_1_1 = '2025-12-19 16:46:56'
WHERE col_1_4 = 3;
```

**What happens**

* The `UPDATE` changes `col_1_1`, which is not present in `idx_1_1`.
* The PRIMARY KEY record must be locked in InnoDB.
* No changes to `idx_1_1` are required.

### Why No Blocking Occurs

1. Connection 1's `SELECT` performs a "covering read" on the secondary index `idx_1_1`. Since the index contains all required data, InnoDB only uses shared locks on secondary index records.
2. Default Connection's `UPDATE` modifies column `col_1_1`, which is not part of that secondary index. Therefore, an exclusive lock is acquired on the Primary Index record (Clustered Index).
3. The Result: Since these are two different index records, there is no conflict between the shared and exclusive locks.

### How to Ensure Blocking

To cause a lock conflict, the locking read must access the primary key record (Clustered Index). This ensures that the _shared lock_ (S) is applied to the location where the update operation (exclusive lock, X) will later be required. This happens when:

* The SELECT contains a column that the secondary index does not cover (e.g., using `SELECT *` or selecting a non‑indexed column), or
* If the secondary index itself is insufficient to satisfy the query, InnoDB must access the full row in the primary index, thereby placing the necessary locks to ensure blocking.

Example:

```
-- The UPDATE is blocked since col_1_1 is not included in the secondary index idx_1_1.
SELECT col_1_1, col_1_4, pkid_1 
FROM tbl_1 
WHERE col_1_3 > 1 
LOCK IN SHARE MODE;
```

The UPDATE will now wait while the clustered index is accessed.

## Intention Locks

InnoDB also permits table locking, and to allow locking at both table and row level to co-exist gracefully, a series of locks called _intention locks_ exist.

An _intention shared lock_(IS) indicates that a transaction intends to set a shared lock.

An _intention exclusive lock_(IX) indicates that a transaction intends to set an exclusive lock.

Whether a lock is granted or not can be summarised as follows:

* An X lock is not granted if any other lock (X, S, IX, IS) is held.
* An S lock is not granted if an X or IX lock is held. It is granted if an S or IS lock is held.
* An IX lock is not granted if in X or S lock is held. It is granted if an IX or IS lock is held.
* An IS lock is not granted if an X lock is held. It is granted if an S, IX or IS lock is held.

## AUTO\_INCREMENT Locks

Locks are also required for auto-increments - see [AUTO\_INCREMENT handling in InnoDB](auto_increment-handling-in-innodb.md).

## Gap Locks

With the default [isolation level](../../../reference/sql-statements/transactions/set-transaction.md), `REPEATABLE READ`, and, until [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), the default setting of the [innodb\_locks\_unsafe\_for\_binlog](innodb-system-variables.md#innodb_locks_unsafe_for_binlog) variable, a method called gap locking is used. When InnoDB sets a shared or exclusive lock on a record, it's actually on the index record. Records will have an internal InnoDB index even if they don't have a unique index defined. At the same time, a lock is held on the gap before the index record, so that another transaction cannot insert a new index record in the gap between the record and the preceding record.

The gap can be a single index value, multiple index values, or not exist at all depending on the contents of the index.

If a statement uses all the columns of a unique index to search for unique row, gap locking is not used.

Similar to the shared and exclusive intention locks described above, there can be a number of types of gap locks. These include the shared gap lock, exclusive gap lock, intention shared gap lock and intention exclusive gap lock.

Gap locks are disabled if the [innodb\_locks\_unsafe\_for\_binlog](innodb-system-variables.md#innodb_locks_unsafe_for_binlog) system variable is set (until [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104)), or the [isolation level](../../../reference/sql-statements/transactions/set-transaction.md) is set to `READ COMMITTED`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
