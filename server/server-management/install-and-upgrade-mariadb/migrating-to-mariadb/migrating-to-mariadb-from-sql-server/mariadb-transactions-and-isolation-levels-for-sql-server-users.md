# MariaDB Transactions and Isolation Levels for SQL Server Users

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/UQS8KgfG8jtpHBvT83fL/" %}

This page explains how transactions work in MariaDB, and highlights the main differences between MariaDB and SQL Server transactions.

Note that XA transactions are handled in a completely different way and are not covered in this page. See [XA Transactions](../../../../reference/sql-statements/transactions/xa-transactions.md).

## Missing Features

These SQL Server features are not available in MariaDB:

* Autonomous transactions;
* Distributed transactions.

## Transactions, Storage Engines and the Binary Log

In MariaDB, transactions are optionally implemented by [storage engines](../../../../server-usage/storage-engines/). The default storage engine, [InnoDB](../../../../server-usage/storage-engines/innodb/), fully supports transactions. Other transactional storage engines include [MyRocks](../../../../server-usage/storage-engines/myrocks/) and [TokuDB](../../../../server-usage/storage-engines/tokudb/). Most storage engines are not transactional, therefore they should not considered general purpose engines.

Most of the information in this page refers to generic MariaDB server behaviors or InnoDB. For [MyRocks](../../../../server-usage/storage-engines/myrocks/) and [TokuDB](../../../../server-usage/storage-engines/tokudb/) please check the proper KnowledgeBase sections.

Writing into a non-transactional table in a transaction can still be useful. The reason is that a [metadata lock](../../../../reference/sql-statements/transactions/metadata-locking.md) is acquired on the table for the duration of the transaction, so that [ALTER TABLEs](../../../../reference/sql-statements/data-definition/alter/alter-table.md) are queued.

It is possible to write into transactional and non-transactional tables within a single transaction. It is important to remember that non-transactional engines will have the following limitations:

* In case of rollback, changes to non-transactional engines won't be undone. We will receive a warning `1196` which reminds us of this.
* Data in transactional tables cannot be changed by other connections in the middle of a transaction, but data in non-transactional tables can.
* In case of a crash, committed data written into a transactional table can always be recovered, but this is not necessarily true for non-transactional tables.

If the [binary log](../../../server-monitoring-logs/binary-log/) is enabled, writing into different transactional storage engines in a single transaction, or writing into transactional and non-transactional engines inside the same transaction, implies some extra work for MariaDB. It needs to perform a two-phase commit to be sure that changes to different tables are logged in the correct order. This affects the performance.

## Transaction Syntax

The first read or write to an InnoDB table starts a transaction. No data access is possible outside a transaction.

By default [autocommit](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) is on, which means that the transaction is committed automatically after each SQL statement. We can disable it, and manually commit transactions:

```
SET SESSION autocommit = 0;
SELECT ... ;
DELETE ... ;
COMMIT;
```

Whether autocommit is enabled or not, we can start transactions explicitly, and they will not be automatically committed:

```
START TRANSACTION;
SELECT ... ;
DELETE ... ;
COMMIT;
```

`BEGIN` can also be used to start a transaction, but does not work in stored procedures.

Read-only transactions are also available using `START TRANSACTION READ ONLY`. This is a small performance optimization. MariaDB will issue an error when trying to write data in the middle of a read-only transaction.

Only DML statements are transactional and can be rolled back. This may change in a future version, see [MDEV-17567](https://jira.mariadb.org/browse/MDEV-17567) - Atomic DDL and [MDEV-4259](https://jira.mariadb.org/browse/MDEV-4259) - transactional DDL.

Changing autocommit and explicitly starting a transaction will implicitly commit the active transaction, if any. DDL statements, and several other statements, implicitly commit the active transaction. See [SQL statements That Cause an Implicit Commit](../../../../reference/sql-statements/transactions/sql-statements-that-cause-an-implicit-commit.md) for the complete list of these statements.

A rollback can also be triggered implicitly, when certain errors occur.

You can experiment with transactions to check in which cases they implicitly commit or rollback. The [in\_transaction](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#in_transaction) system variable can help: it is set to 1 when a transaction is in progress, or 0 when no transaction is in progress.

This section only covers the basic syntax for transactions. Much more options are available. For more information, see [Transactions](../../../../reference/sql-statements/transactions/).

## Constraint Checking

MariaDB supports the following [constraints](../../../../reference/sql-statements/data-definition/constraint.md):

* [Primary keys](../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#primary-key)
* [UNIQUE](../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#unique-index)
* [CHECK](../../../../reference/sql-statements/data-definition/constraint.md#check-constraints)
* [Foreign keys](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md)

In some databases, constraints can temporarily be violated during a transaction, and their enforcement can be deferred to the commit time. SQL Server does not support this, and always validates data against constraints at the end of each statement.

MariaDB does something different: it always checks constraints after each row change. There are cases this policy makes some statements fail with an error, even if those statements would work on SQL Server.

For example, suppose you have an `id` column that is the primary key, and you need to increase its value for some reason:

```
SELECT id FROM customer;
+----+
| id |
+----+
|  1 |
|  2 |
|  3 |
|  4 |
|  5 |
+----+

UPDATE customer SET id = id + 1;
ERROR 1062 (23000): Duplicate entry '2' for key 'PRIMARY'
```

The reason why this happens is that, as the first thing, MariaDB tries to change 1 to 2, but a value of 2 is already present in the primary key.

A solution is to use this non-standard syntax:

```
UPDATE customer SET id = id + 1 ORDER BY id DESC;
Query OK, 5 rows affected (0.00 sec)
Rows matched: 5  Changed: 5  Warnings: 0
```

Changing the ids in reversed order won't duplicate any value.

Similar problems can happen with `CHECK` constraints and foreign keys. To solve them, we can use a different approach:

```
SET SESSION check_constraint_checks = 0;
-- run some queries
-- that temporarily violate a CHECK clause
SET SESSION check_constraint_checks = 1;

SET SESSION foreign_key_checks = 0;
-- run some queries
-- that temporarily violate a foreign key
SET SESSION foreign_key_checks = 1;
```

The last solutions temporarily disable `CHECK` constraints and foreign keys. Note that, while this may solve practical problems, it is dangerous because:

* This doesn't disable a single `CHECK` or foreign key, but also others, that you don't expect to violate.
* This doesn't defer the constraint checks, but it simply disables them for a while. This means that, if you insert some invalid values, they will not be detected.

See [check\_constraint\_checks](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#check_constraint_checks) and [foreign\_key\_checks](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#foreign_key_checks) system variables.

## Isolation Levels and Locks

For more information about MariaDB isolation levels see [SET TRANSACTION](../../../../reference/sql-statements/transactions/set-transaction.md).

### Locking Reads

In MariaDB, the locks acquired by a read do not depend on the isolation level (with one exception noted below).

As a general rule:

* Plain [SELECTs](../../../../reference/sql-statements/data-manipulation/selecting-data/select.md) are not locking, they acquire snapshots instead.
* To force a read to acquire a shared lock, use [SELECT ... LOCK IN SHARED MODE](../../../../reference/sql-statements/data-manipulation/selecting-data/lock-in-share-mode.md).
* To force a read to acquire an exclusive lock, use [SELECT ... FOR UPDATE](../../../../reference/sql-statements/data-manipulation/selecting-data/for-update.md).

### Changing the Isolation Level

The default, the isolation level in MariaDB is `REPEATABLE READ`. This can be changed with the [tx\_isolation](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tx_isolation) system variable.

Applications developed for SQL Server and later ported to MariaDB may run with `READ COMMITTED` without problems. Using a stricter level would reduce scalability. To use `READ COMMITTED` by default, add the following line to the MariaDB configuration file:

```
tx_isolation = 'READ COMMITTED'
```

It is also possible to change the default isolation level for the current session:

```
SET SESSION tx_isolation = 'read-committed';
```

Or just for one transaction, by issuing the following statement before starting a transaction:

```
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

### How Isolation Levels are Implemented in MariaDB

MariaDB supports the following isolation levels:

* `READ UNCOMMITTED`
* `READ COMMITTED`
* `REPEATABLE READ`
* `SERIALIZABLE`

MariaDB isolation levels differ from SQL Server in the following ways:

* `REPEATABLE READ` does not acquire share locks on all read rows, nor a range lock on the missing values that match a `WHERE` clause.
* It is not possible to change the isolation level in the middle of a transaction.
* `SNAPSHOT` isolation level is not supported. Instead, you can use `START TRANSACTION WITH CONSISTENT SNAPSHOT` to acquire a snapshot at the beginning of the transaction. This is compatible with all isolation levels.

Here is an example of `WITH CONSISTENT SNAPSHOT` usage:

```
-- session 1
SELECT * FROM t1;
+----+
| id |
+----+
|  1 |
+----+

SELECT * FROM t2;
+----+
| id |
+----+
|  1 |
+----+

START TRANSACTION WITH CONSISTENT SNAPSHOT;

-- session 2
INSERT INTO t1 VALUES (2);

-- session 1
SELECT * FROM t1;
+----+
| id |
+----+
|  1 |
+----+

-- session 2
INSERT INTO t2 VALUES (2);

-- session 1
SELECT * FROM t2;
+----+
| id |
+----+
|  1 |
+----+
```

As you can see, session 1 uses `WITH CONSISTENT SNAPSHOT`, thus it sees all tables as they were when the transaction begun.

### Avoiding Lock Waits

When we try to read or modify a row that is exclusive-locked by another transaction, our transaction is queued until that lock is released. There could be more queued transactions waiting to acquire the same lock, in which case we will wait even more.

There is a timeout for such waits, defined by the [innodb\_lock\_wait\_timeout](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_lock_wait_timeout) variable. If it is set to 0, statements that encounter a row lock will fail immediately. When the timeout is exceeded, MariaDB produces the following error:

```
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
```

It is important to note that this variable has two limitations (by design):

* It only affects transactional statements, not statements like `ALTER TABLE` or `TRUNCATE TABLE`.
* It only concerns row locks. It does not put a timeout on metadata locks, or table locks acquired - for example - with the [LOCK TABLES](../../../../reference/sql-statements/transactions/lock-tables.md) statement.

Note however that [lock\_wait\_timeout](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lock_wait_timeout) can be used for metadata locks.

There is a special syntax that can be used with `SELECT` and some non-transactional statements including `ALTER TABLE`: the [WAIT and NOWAIT](../../../../reference/sql-statements/transactions/wait-and-nowait.md) clauses. This syntax puts a timeout in seconds for all lock types, including row locks, table locks, and metadata locks. For example:

```
Session 1:
START TRANSACTION;
-- let's acquire a metadata lock
SELECT id FROM t WHERE 0;

Session 2:
DROP TABLE t WAIT 0;
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
```

## InnoDB Transactions

### InnoDB Lock Types

InnoDB locks are classified based on what exactly they lock, and which operations they lock.

The first classification is the following:

* Record Locks lock a row or, more precisely, an index entry.
* Gap Locks lock an interval between two index entries. Note that indexes have virtual values of -Infinum and Infinum, so a gap lock can cover the gap before the first or after the last index entry.
* Next-Key Locks lock an index entry and the gap between it and the next entry. They're a combination of record locks and gap locks.
* Insert Intention Locks are gap locks acquired before inserting a new row.

Lock modes are the following:

* Exclusive Locks (X) are generally acquired on writes, e.g. immediately before deleting a row. Only one exclusive lock can be acquired on a resource simultaneously.
* Shared Locks (S) can be acquired on reads. Multiple shared locks can be acquired at the same time (because the rows are not supposed to change when shared-locked) but are incompatible with exclusive locks.
* Intention locks (IS, XS) are acquired when it is not possible to acquire an exclusive lock or a shared lock. When a lock on a row or gap is released, the oldest intention lock on that resource (if any) is converted to an X or S lock.

For more information see [InnoDB Lock Modes](../../../../server-usage/storage-engines/innodb/innodb-lock-modes.md).

### Information Schema

Querying the [information\_schema](../../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/) is the best way to see which transactions have acquired some locks and which transactions are waiting for some locks to be released.

In particular, check the following tables:

* [INNODB\_LOCKS](../../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_locks-table.md): requests for locks not yet fulfilled, or that are blocking another transaction.
* [INNODB\_LOCK\_WAITS](../../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_lock_waits-table.md): queued requests to acquire a lock.
* [INNODB\_TRX](../../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_trx-table.md): information about all currently executing InnoDB transactions, including SQL queries that are running.

Here is an example of their usage.

```
-- session 1
START TRANSACTION;
UPDATE t SET id = 15 WHERE id = 10;

-- session 2
DELETE FROM t WHERE id = 10;

-- session 1
USE information_schema;
SELECT l.*, t.*
    FROM information_schema.INNODB_LOCKS l
    JOIN information_schema.INNODB_TRX t
        ON l.lock_trx_id = t.trx_id
    WHERE trx_state = 'LOCK WAIT' \G
*************************** 1. row ***************************
                   lock_id: 840:40:3:2
               lock_trx_id: 840
                 lock_mode: X
                 lock_type: RECORD
                lock_table: `test`.`t`
                lock_index: PRIMARY
                lock_space: 40
                 lock_page: 3
                  lock_rec: 2
                 lock_data: 10
                    trx_id: 840
                 trx_state: LOCK WAIT
               trx_started: 2019-12-23 18:43:46
     trx_requested_lock_id: 840:40:3:2
          trx_wait_started: 2019-12-23 18:43:46
                trx_weight: 2
       trx_mysql_thread_id: 46
                 trx_query: DELETE FROM t WHERE id = 10
       trx_operation_state: starting index read
         trx_tables_in_use: 1
         trx_tables_locked: 1
          trx_lock_structs: 2
     trx_lock_memory_bytes: 1136
           trx_rows_locked: 1
         trx_rows_modified: 0
   trx_concurrency_tickets: 0
       trx_isolation_level: REPEATABLE READ
         trx_unique_checks: 1
    trx_foreign_key_checks: 1
trx_last_foreign_key_error: NULL
          trx_is_read_only: 0
trx_autocommit_non_locking: 0
```

### Deadlocks

InnoDB detects deadlocks automatically. Since this consumes CPU time, some users prefer to disable this feature by setting the [innodb\_deadlock\_detect](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_deadlock_detect) variable to 0. If this is done, locked transactions will wait until the they exceed the [innodb\_lock\_wait\_timeout](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_lock_wait_timeout). Therefore it is important to set innodb\_lock\_wait\_timeout to a very low value, like 1.

When InnoDB detects a deadlock, it kills the transaction that modified the least amount of data. The client will receive the following error:

```
ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction
```

The latest detected deadlock, and the killed transaction, can be viewed in the output of [SHOW ENGINE InnoDB STATUS](../../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md). Here's an example:

```
------------------------
LATEST DETECTED DEADLOCK
------------------------
2019-12-23 18:55:18 0x7f51045e3700
*** (1) TRANSACTION:
TRANSACTION 847, ACTIVE 10 sec starting index read
mysql tables in use 1, locked 1
LOCK WAIT 4 lock struct(s), heap size 1136, 3 row lock(s), undo log entries 1
MySQL thread id 46, OS thread handle 139985942054656, query id 839 localhost root Updating
delete from t where id = 10
*** (1) WAITING FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 40 page no 3 n bits 80 index PRIMARY of table `test`.`t` trx id 847 lock_mode X locks rec but not gap waiting
Record lock, heap no 2 PHYSICAL RECORD: n_fields 3; compact format; info bits 32
 0: len 4; hex 8000000a; asc     ;;
 1: len 6; hex 00000000034e; asc      N;;
 2: len 7; hex 760000019c0495; asc v      ;;

*** (2) TRANSACTION:
TRANSACTION 846, ACTIVE 25 sec starting index read
mysql tables in use 1, locked 1
3 lock struct(s), heap size 1136, 2 row lock(s), undo log entries 1
MySQL thread id 39, OS thread handle 139985942361856, query id 840 localhost root Updating
delete from t where id = 11
*** (2) HOLDS THE LOCK(S):
RECORD LOCKS space id 40 page no 3 n bits 80 index PRIMARY of table `test`.`t` trx id 846 lock_mode X locks rec but not gap
Record lock, heap no 2 PHYSICAL RECORD: n_fields 3; compact format; info bits 32
 0: len 4; hex 8000000a; asc     ;;
 1: len 6; hex 00000000034e; asc      N;;
 2: len 7; hex 760000019c0495; asc v      ;;

*** (2) WAITING FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 40 page no 3 n bits 80 index PRIMARY of table `test`.`t` trx id 846 lock_mode X locks rec but not gap waiting
Record lock, heap no 3 PHYSICAL RECORD: n_fields 3; compact format; info bits 32
 0: len 4; hex 8000000b; asc     ;;
 1: len 6; hex 00000000034f; asc      O;;
 2: len 7; hex 770000019d031d; asc w      ;;

*** WE ROLL BACK TRANSACTION (2)
```

The latest detected deadlock never disappears from the output of `SHOW ENGINE InnoDB STATUS`. If you cannot see any, MariaDB hasn't detected any InnoDB deadlocks since the last restart.

Another way to monitor deadlocks is to set [innodb\_print\_all\_deadlocks](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_print_all_deadlocks) to 1 (0 is the default). InnoDB will log all detected deadlocks into the [error log](../../../server-monitoring-logs/error-log.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
