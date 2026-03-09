---
description: >-
  Complete START TRANSACTION reference: BEGIN/COMMIT/ROLLBACK syntax, WITH
  CONSISTENT SNAPSHOT option, READ ONLY/WRITE modes, AND [NO] CHAIN/RELEASE
  modifiers.
---

# START TRANSACTION

## Syntax

```sql
START TRANSACTION [transaction_property [, transaction_property] ...] | BEGIN [WORK]
COMMIT [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
ROLLBACK [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
SET autocommit = {0 | 1}

transaction_property:
    WITH CONSISTENT SNAPSHOT
  | READ WRITE
  | READ ONLY
```

## Description

The `START TRANSACTION` or `BEGIN` statement begins a new transaction. [COMMIT](commit.md) commits the current transaction, making its changes permanent. [ROLLBACK](rollback.md) rolls back the current transaction, canceling its changes. The [SET](../programmatic-compound-statements/set-variable.md) [autocommit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) statement disables or enables the default autocommit mode for the current session.

`START TRANSACTION` and `SET` autocommit = 1 implicitly commit the current transaction, if there is one.

The optional `WORK` keyword is supported for`COMMIT` and `ROLLBACK`, as are the`CHAIN` and `RELEASE` clauses.`CHAIN` and `RELEASE` can be used for additional control over transaction completion. The value of the [completion\_type](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#completion_type) system variable determines the default completion behavior.

The `AND CHAIN` clause causes a new transaction to begin as soon as the current one ends, and the new transaction has the same isolation level as the just-terminated transaction. The `RELEASE` clause causes the server to disconnect the current client session after terminating the current transaction. Including the `NO` keyword suppresses`CHAIN` or `RELEASE` completion, which can be useful if the [completion\_type](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#completion_type) system variable is set to cause chaining or release completion by default.

### Access Mode

{% tabs %}
{% tab title="Current" %}
The access mode specifies whether the transaction is allowed to write data or not. By default, transactions are in `READ WRITE` mode (see the [tx\_read\_only](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tx_read_only) system variable). `READ ONLY` mode allows the storage engine to apply optimizations that cannot be used for transactions which write data. Note that, unlike the global [read\_only](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#read_only) mode, the [READ\_ONLY ADMIN](../account-management-sql-commands/grant.md#read_only-admin) privilege doesn't allow writes and DDL statements on temporary tables are not allowed either.
{% endtab %}

{% tab title="< 10.11" %}
The access mode specifies whether the transaction is allowed to write data or not. By default, transactions are in `READ WRITE` mode (see the [tx\_read\_only](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tx_read_only) system variable). `READ ONLY` mode allows the storage engine to apply optimizations that cannot be used for transactions which write data. Note that, unlike the global [read\_only](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#read_only) mode, the [SUPER](../account-management-sql-commands/grant.md#super) privilege doesn't allow writes and DDL statements on temporary tables are not allowed either.
{% endtab %}
{% endtabs %}

It is not permitted to specify both `READ WRITE` and `READ ONLY` in the same statement.

`READ WRITE` and `READ ONLY` can also be specified in the [SET TRANSACTION](set-transaction.md) statement, in which case the specified mode is valid for all sessions, or for all subsequent transaction used by the current session.

### autocommit

By default, MariaDB runs with [autocommit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) mode enabled. This means that as soon as you execute a statement that updates (modifies) a table, MariaDB stores the update on disk to make it permanent. To disable autocommit mode, use the following statement:

```sql
SET autocommit=0;
```

After disabling autocommit mode by setting the autocommit variable to zero, changes to transaction-safe tables (such as those for InnoDB or`NDBCLUSTER`) are not made permanent immediately. You must use `COMMIT` to store your changes to disk or `ROLLBACK` to ignore the changes.

To disable autocommit mode for a single series of statements, use the `START TRANSACTION` statement.

### DDL Statements

DDL statements (`CREATE`, `ALTER`, `DROP`) and administrative statements (`FLUSH`, `RESET`, `OPTIMIZE`, `ANALYZE`, `CHECK`, `REPAIR`, `CACHE INDEX`), transaction management statements (`BEGIN`, `START TRANSACTION`) and `LOAD DATA INFILE`, cause an implicit `COMMIT` and start a new transaction. An exception to this rule are the DDL that operate on temporary tables: you can `CREATE`, `ALTER` and `DROP` them without causing any `COMMIT`, but those actions cannot be rolled back. This means that if you call `ROLLBACK`, the temporary tables you created in the transaction will remain, while the rest of the transaction will be rolled back.

Transactions cannot be used in Stored Functions or Triggers. In Stored Procedures and Events `BEGIN` is not allowed, so you should use `START TRANSACTION` instead.

A transaction acquires a [metadata lock](metadata-locking.md) on every table it accesses to prevent other connections from altering their structure. The lock is released at the end of the transaction. This happens even with non-transactional storage engines (like [MEMORY](../../../server-usage/storage-engines/memory-storage-engine.md) or [CONNECT](../../../server-usage/storage-engines/connect/)), so it makes sense to use transactions with non-transactional tables.

### in\_transaction

The [in\_transaction](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#in_transaction) system variable is a session-only, read-only variable that returns `1` inside a transaction, and `0` if not in a transaction.

### WITH CONSISTENT SNAPSHOT

The `WITH CONSISTENT SNAPSHOT` option starts a consistent read for storage engines such as [InnoDB](../../../server-usage/storage-engines/innodb/) that can do so, the same as if a `START TRANSACTION` followed by a `SELECT` from any InnoDB table was issued.

See [Enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT](../../../ha-and-performance/standard-replication/enhancements-for-start-transaction-with-consistent-snapshot.md).

## Examples

```sql
START TRANSACTION;
SELECT @A:=SUM(salary) FROM table1 WHERE type=1;
UPDATE table2 SET summary=@A WHERE type=1;
COMMIT;
```

## See Also

* [Enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT](../../../ha-and-performance/standard-replication/enhancements-for-start-transaction-with-consistent-snapshot.md)
* [MyRocks and START TRANSACTION WITH CONSISTENT SNAPSHOT](../../../server-usage/storage-engines/myrocks/myrocks-and-start-transaction-with-consistent-snapshot.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
