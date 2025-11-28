---
description: >-
  Define isolation levels and access modes for transactions. Learn to configure
  the behavior of the next transaction or the entire session for data
  consistency.
---

# SET TRANSACTION

## Syntax

```sql
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

## Description

This statement sets the transaction isolation level or the transaction access mode globally, for the current session, or for the next transaction:

* With the `GLOBAL` keyword, the statement sets the default transaction level globally for all subsequent sessions. Existing sessions are unaffected.
* With the `SESSION` keyword, the statement sets the default transaction level for all subsequent transactions performed within the current session.
* Without any `SESSION` or `GLOBAL` keyword, the statement sets the isolation level for only the next (not started) transaction performed within the current session. After that it reverts to using the session value.

A change to the global default isolation level requires the [SUPER](../account-management-sql-statements/grant.md#super) privilege. Any session is free to change its session isolation level (even in the middle of a transaction), or the isolation level for its next transaction.

### Isolation Level

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

### Isolation Levels

The following sections describe how MariaDB supports the different transaction levels.

{% include "../../../.gitbook/includes/with-both-read-uncommitted-....md" %}

#### READ UNCOMMITTED

`SELECT` statements are performed in a non-locking fashion, but a possible earlier version of a row might be used. Thus, using this isolation level, such reads are not consistent. This is also called a "dirty\
read". Otherwise, this isolation level works like`READ COMMITTED`.

{% include "../../../.gitbook/includes/with-both-read-uncommitted-....md" %}

#### READ COMMITTED

A somewhat Oracle-like isolation level with respect to consistent (non-locking) reads: Each consistent read, even within the same transaction, sets and reads its own fresh snapshot. See [innodb-consistent-read.html](https://dev.mysql.com/doc/refman/en/innodb-consistent-read.html).

For locking reads (`SELECT` with `FOR UPDATE` or `LOCK IN SHARE MODE`), InnoDB locks only index records, not the gaps before them, and thus allows the free insertion of new records next to locked records. For `UPDATE` and `DELETE` statements, locking depends on whether the statement uses a unique index with a unique search condition (such as `WHERE id = 100`), or a range-type search condition (such as `WHERE id > 100`). For a unique index with a unique search condition, InnoDB locks only the index record found, not the gap before it. For range-type searches, InnoDB locks the index\
range scanned, using gap locks or next-key (gap plus index-record) locks to block insertions by other sessions into the gaps covered by the range. This is necessary because "phantom rows" must be blocked for MariaDB replication and recovery to work.

**Note:** If the `READ COMMITTED` isolation level is used or the [innodb\_locks\_unsafe\_for\_binlog](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_locks_unsafe_for_binlog) system variable is enabled, there is no InnoDB gap locking except for [foreign-key](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) constraint checking and\
duplicate-key checking. Also, record locks for non-matching rows are released after MariaDB has evaluated the `WHERE` condition.If you use `READ COMMITTED` or enable `innodb_locks_unsafe_for_binlog`, you must use row-based binary logging.

#### REPEATABLE READ

This is the default isolation level for InnoDB. For consistent reads, there is an important difference from the `READ COMMITTED` isolation level: All consistent reads within the same transaction read the\
snapshot established by the first read. This convention means that if you issue several plain (non-locking) `SELECT` statements within the same transaction, these `SELECT` statements are consistent\
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

#### SERIALIZABLE

This level is like REPEATABLE READ, but InnoDB implicitly converts all plain SELECT statements to [SELECT ... LOCK IN SHARE MODE](../data-manipulation/selecting-data/select.md#lock-in-share-mode-and-for-update-clauses) if [autocommit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) is disabled. If autocommit is enabled, the SELECT is its own transaction. It therefore is known to be read only and can be serialized if performed as a consistent (non-locking) read and need not block for other transactions. (This means that to force a plain SELECT to block if other transactions have modified the selected rows, you should disable autocommit.)

Distributed [XA transactions](xa-transactions.md) should always use this isolation level.

#### innodb\_snapshop\_isolation

{% tabs %}
{% tab title="Current" %}
If the [innodb\_snapshot\_isolation](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_snapshot_isolation) system variable is not set to `ON`, strictly-speaking anything other than `READ UNCOMMITTED` is not clearly defined. [innodb\_snapshot\_isolation](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_snapshot_isolation) defaults to `OFF` for backwards compatibility. Setting to `ON` will result in attempts to acquire a lock on a record that does not exist in the current read view raising an error, and the transaction being rolled back.
{% endtab %}

{% tab title="< 11.4.2 / 11.2.4 / 11.1.15 / 11.0.6 / 10.11.8 / 10.6.18" %}
If the [innodb\_snapshot\_isolation](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_snapshot_isolation) system variable is not set to `ON`, strictly-speaking anything other than `READ UNCOMMITTED` is not clearly defined.
{% endtab %}
{% endtabs %}

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
