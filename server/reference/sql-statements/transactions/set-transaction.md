---
description: >-
  Define isolation levels and access modes for transactions. Learn to configure
  the behavior of the next transaction or the entire session for data
  consistency.
---

# SET TRANSACTION

## Syntax

```bnf
SET [GLOBAL | SESSION] TRANSACTION
    transaction_property [, transaction_property] ...

transaction_property:
    ISOLATION LEVEL level
  | READ WRITE
  | READ ONLY

level:
     REPEATABLE READ
   | READ COMMITTED
   | READ UNCOMMITTED
   | SERIALIZABLE
```

## Overview

This statement sets the transaction isolation level or the transaction access mode globally, for the current session, or for the next transaction:

* With the `GLOBAL` keyword, the statement sets the default transaction level globally for all subsequent sessions. Existing sessions are unaffected.
* With the `SESSION` keyword, the statement sets the default transaction level for all subsequent transactions performed within the current session.
* Without any `SESSION` or `GLOBAL` keyword, the statement sets the isolation level for only the next (not started) transaction performed within the current session. After that it reverts to using the session value.

A change to the global default isolation level requires the [SUPER](../account-management-sql-statements/grant.md#super) privilege. Any session is free to change its session isolation level (even in the middle of a transaction), or the isolation level for its next transaction.

## Isolation Level

To set the global default isolation level at server startup, use the [--transaction-isolation=level](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tx_isolation) option on the command line or in an option file. Values of level for this option use dashes rather than spaces, so the allowable values are [READ\_UNCOMMITTED](set-transaction.md#read-uncommitted),[READ-COMMITTED](set-transaction.md#read-committed), [REPEATABLE-READ](set-transaction.md#repeatable-read), or [SERIALIZABLE](set-transaction.md#serializable). For example, to set the default isolation level to `REPEATABLE READ`, use these lines in the `[mariadb]` section of an option file:

```ini
[mariadb]
transaction-isolation = REPEATABLE-READ
```

{% tabs %}
{% tab title="Current" %}
To determine the global and session transaction isolation levels at runtime, check the value of the [transaction\_isolation](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#transaction_isolation) variable.
{% endtab %}

{% tab title="< 11.1.1" %}
To determine the global and session transaction isolation levels at runtime, check the value of the [tx\_isolation](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tx_isolation) system variable.
{% endtab %}
{% endtabs %}

```sql
SELECT @@GLOBAL.transaction_isolation, @@tx_isolation;
```

InnoDB supports each of the translation isolation levels described here using different locking strategies. The default level is`REPEATABLE READ`. For additional information about InnoDB record-level locks and how it uses them to execute various types of statements, see [InnoDB Lock Modes](../../../server-usage/storage-engines/innodb/innodb-lock-modes.md), and [innodb-locks-set.html](https://dev.mysql.com/doc/refman/en/innodb-locks-set.html).

## Isolation Levels

The following sections describe how MariaDB supports the different transaction levels.

{% include "../../../.gitbook/includes/with-both-read-uncommitted-....md" %}

### READ UNCOMMITTED

`SELECT` statements are performed in a non-locking fashion, but a possible earlier version of a row might be used. Thus, using this isolation level, such reads are not consistent. This is also called a "dirty read". Otherwise, this isolation level works like`READ COMMITTED`.

{% include "../../../.gitbook/includes/with-both-read-uncommitted-....md" %}

### READ COMMITTED

A somewhat Oracle-like isolation level with respect to consistent (non-locking) reads: Each consistent read, even within the same transaction, sets and reads its own fresh snapshot. See [innodb-consistent-read.html](https://dev.mysql.com/doc/refman/en/innodb-consistent-read.html).

#### Gap Locking at READ COMMITTED

InnoDB takes no [gap locks](../../../server-usage/storage-engines/innodb/innodb-lock-modes.md#gap-locks) at this isolation level. For locking reads (`SELECT` with `FOR UPDATE` or `LOCK IN SHARE MODE`), and for `UPDATE` and `DELETE` statements, InnoDB locks only the index records it examines, not the gaps before them, and thus allows the free insertion of new records next to locked records. This applies to range-type search conditions (such as `WHERE id > 100`) as well as to unique searches (such as `WHERE id = 100`).

Duplicate-key checking is the exception: when InnoDB checks a unique index for a duplicate value, it takes a next-key (gap plus index-record) lock regardless of the isolation level. [Foreign key](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) constraint checks, by contrast, do not take gap locks at `READ COMMITTED`.

Gap locks are what block phantom rows, so without them InnoDB cannot be logged safely one statement at a time. With [binary logging](../../../server-management/server-monitoring-logs/binary-log/) enabled and [binlog\_format](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) set to `STATEMENT`, InnoDB rejects any statement that would write rows:

```sql
SET SESSION binlog_format = STATEMENT;
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
UPDATE t SET v = 9 WHERE id = 1;
ERROR 1665 (HY000): Cannot execute statement: impossible to write to binary log
since BINLOG_FORMAT = STATEMENT and at least one table uses a storage engine
limited to row-based logging. InnoDB is limited to row-logging when transaction
isolation level is READ COMMITTED or READ UNCOMMITTED.
```

The default `binlog_format` of `MIXED` is unaffected, as is `ROW`.

#### Semi-Consistent Reads

In a semi-consistent read, an `UPDATE` statement skips a row that another transaction has locked, provided the latest committed version of that row does not match the `WHERE` condition. The statement proceeds instead of waiting for the lock, which means you might see only a partially consistent read.

Semi-consistent reads are limited to `UPDATE`; a `DELETE` waits for the lock. They also require the statement to scan the clustered index with a non-unique search condition. An `UPDATE` that matches every column of a unique index exactly, such as `WHERE id = 100`, waits for the lock, as does one that scans a secondary index.

{% hint style="info" %}
At `READ COMMITTED`, semi-consistent reads apply only when [innodb\_snapshot\_isolation](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_snapshot_isolation) is disabled. That variable is enabled by default from MariaDB 11.6.2, and while it is enabled, `READ COMMITTED` performs an ordinary locking read and waits for the lock. Semi-consistent reads then apply to `READ UNCOMMITTED` only.
{% endhint %}

Releasing a lock on a non-matching row is separate, and is not restricted in either of those ways. For a `DELETE` as much as an `UPDATE`, and regardless of `innodb_snapshot_isolation`, if InnoDB locks a record at `READ COMMITTED` or `READ UNCOMMITTED` and then finds that the record does not match the `WHERE` condition, it releases that record lock — unless the transaction has itself modified the row.

### REPEATABLE READ

**This is the default isolation level for InnoDB.** For consistent reads, there is an important difference from the `READ COMMITTED` isolation level: All consistent reads within the same transaction read the
snapshot established by the first read. This convention means that if you issue several plain (non-locking) `SELECT` statements within the same transaction, these `SELECT` statements are consistent
also with respect to each other. See [innodb-consistent-read.html](https://dev.mysql.com/doc/refman/en/innodb-consistent-read.html).

{% tabs %}
{% tab title="Current" %}
For locking reads (`SELECT` with `FOR UPDATE` or `LOCK IN SHARE MODE`), `UPDATE`, and `DELETE` statements, locking depends on whether the statement uses a unique index with a unique search condition, or a range-type search condition. MariaDB does not relax the gap locking for unique indexes.
{% endtab %}

{% tab title="< 11.0 / 10.11.2 / 10.10.3 / 10.9.5 / 10.8.7 / 10.7.8 / 10.6.12 / 10.5.19 / 10.4.28 / 10.3.38" %}
For locking reads (`SELECT` with `FOR UPDATE` or `LOCK IN SHARE MODE`), `UPDATE`, and `DELETE` statements, locking depends on whether the statement uses a unique index with a unique search condition, or a range-type search condition. For a unique index with a unique search condition, InnoDB locks only the index record found, not the gap before it.
{% endtab %}
{% endtabs %}

For other search conditions, InnoDB locks the index range scanned, using gap locks or next-key (gap plus index-record) locks to block insertions by other sessions into the gaps covered by the range.

This is the minimum isolation level for non-distributed [XA transactions](xa-transactions.md).

#### Snapshot Isolation and DML Operations

{% hint style="info" %}
[innodb\_snapshot\_isolation](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_snapshot_isolation) is enabled by default from MariaDB 11.6.2. It was added, defaulting to `OFF`, in MariaDB 10.6.18, 10.11.8, 11.0.6, 11.1.5, 11.2.4, and 11.4.2.
{% endhint %}

While `innodb_snapshot_isolation` is enabled, MariaDB enforces `REPEATABLE READ` more strictly for `UPDATE` and `DELETE` statements:

* **Conflict Detection:** If an `UPDATE` or `DELETE` attempts to modify a row that has been changed by a concurrent transaction since your snapshot was established, the operation is rejected.
* [**ER\_CHECKREAD**](../../error-codes/mariadb-error-codes-1000-to-1099/e1020.md) **(1020):** This rejection triggers error `ER_CHECKREAD`. The revised error message suggests that the user should try restarting the transaction.
* **Automatic Rollback:** Unlike a simple statement error, `ER_CHECKREAD` is treated similarly to a deadlock: **the entire transaction is rolled back**.
* **Purpose:** This prevents the transaction from switching to "current-read" mode for that row, which would otherwise allow the transaction to observe concurrent changes it did not make, violating the pure repeatable read invariant.

#### Traditional Locking Behavior

If `innodb_snapshot_isolation` is disabled (set to `OFF`), InnoDB follows traditional behavior where locking reads (`SELECT ... FOR UPDATE`), `UPDATE`, and `DELETE` statements read the latest committed version of rows. In this mode, subsequent non-locking `SELECT` statements for those same rows also return the current version rather than the snapshot version, which can lead to non-repeatable read anomalies.

### SERIALIZABLE

This level is like `REPEATABLE READ`, but InnoDB implicitly converts all plain `SELECT` statements to [SELECT ... LOCK IN SHARE MODE](../data-manipulation/selecting-data/select.md#lock-in-share-mode-for-update) if [autocommit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) is disabled. If autocommit is enabled, the `SELECT` is its own transaction. It therefore is known to be read only and can be serialized if performed as a consistent (non-locking) read and need not block for other transactions. (This means that to force a plain `SELECT` to block if other transactions have modified the selected rows, you should disable autocommit.)

Distributed [XA transactions](xa-transactions.md) should always use this isolation level.

### innodb\_snapshot\_isolation

If the [innodb\_snapshot\_isolation](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_snapshot_isolation) system variable is not set to `ON`, strictly speaking anything other than `READ UNCOMMITTED` is not clearly defined. While it is `ON`, an attempt to acquire a lock on a record that does not exist in the current read view raises an error and rolls the transaction back.

### Access Mode

{% tabs %}
{% tab title="Current" %}
The access mode specifies whether the transaction is allowed to write data or not. By default, transactions are in `READ WRITE` mode (see the [tx\_read\_only](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tx_read_only) system variable). `READ ONLY` mode allows the storage engine to apply optimizations that cannot be used for transactions which write data. Note that, unlike the global [read\_only](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_only) mode, the [READ\_ONLY ADMIN](../account-management-sql-statements/grant.md#read_only-admin) privilege doesn't allow writes, and DDL statements on temporary tables are not allowed either.
{% endtab %}

{% tab title="< 10.11.0" %}
The access mode specifies whether the transaction is allowed to write data or not. By default, transactions are in `READ WRITE` mode (see the [tx\_read\_only](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tx_read_only) system variable). `READ ONLY` mode allows the storage engine to apply optimizations that cannot be used for transactions which write data. Note that, unlike the global [read\_only](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_only) mode, the [SUPER](../account-management-sql-statements/grant.md#super) privilege doesn't allow writes, and DDL statements on temporary tables are not allowed either.
{% endtab %}
{% endtabs %}

It is not permitted to specify both `READ WRITE` and `READ ONLY` in the same statement.

`READ WRITE` and `READ ONLY` can also be specified in the [START TRANSACTION](start-transaction.md) statement, in which case the specified mode is only valid for one transaction.

## Examples

```sql
SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

Attempting to set the isolation level within an existing transaction without specifying `GLOBAL` or `SESSION`.

```sql
START TRANSACTION;

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
ERROR 1568 (25001): Transaction characteristics can't be changed while a transaction is in progress
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
