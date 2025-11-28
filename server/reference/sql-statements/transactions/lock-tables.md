---
description: >-
  Explicitly lock one or more tables. This statement acquires read or write
  locks on tables, preventing other sessions from accessing them.
---

# LOCK TABLES

## Syntax

```sql
LOCK TABLE[S]
    tbl_name [[AS] alias] lock_type
    [, tbl_name [[AS] alias] lock_type] ...
    [WAIT n|NOWAIT]

lock_type:
    READ [LOCAL]
  | [LOW_PRIORITY] WRITE
  | WRITE CONCURRENT

UNLOCK TABLES
```

## Description

The _lock\_type_ can be one of:

| Option              | Description                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------ |
| READ                | Read lock, no writes allowed                                                                                 |
| READ LOCAL          | Read lock, but allow [concurrent inserts](../data-manipulation/inserting-loading-data/concurrent-inserts.md) |
| WRITE               | Exclusive write lock. No other connections can read or write to this table                                   |
| LOW\_PRIORITY WRITE | Exclusive write lock, but allow new read locks on the table until we get the write lock.                     |
| WRITE CONCURRENT    | Exclusive write lock, but allow READ LOCAL locks to the table.                                               |

MariaDB enables client sessions to acquire table locks explicitly for the purpose of cooperating with other sessions for access to tables, or to prevent other sessions from modifying tables during periods when a session requires exclusive access to them. A session can acquire or release locks only for itself. One session cannot acquire locks for another session or release locks held by another session.

Locks may be used to emulate transactions or to get more speed when updating tables.

`LOCK TABLES` explicitly acquires table locks for the current client session. Table locks can be acquired for base tables or views. To use `LOCK TABLES`, you must have the `LOCK TABLES` privilege, and the `SELECT` privilege for each object to be locked. See [GRANT](../account-management-sql-statements/grant.md).

For view locking, `LOCK TABLES` adds all base tables used in the view to the set of tables to be locked and locks them automatically. If you lock a table explicitly with `LOCK TABLES`, any tables used in triggers are also locked implicitly, as described in [Triggers and Implicit Locks](../../../server-usage/triggers-events/triggers/triggers-and-implicit-locks.md).

[UNLOCK TABLES](transactions-unlock-tables.md) explicitly releases any table locks held by the current session.

### Aliases

Aliases need to correspond to the aliases used in prior SQL statements in the session. For example:

```sql
LOCK TABLE t1 AS t1_alias1 READ;

SELECT * FROM t1;
ERROR 1100 (HY000): Table 't1' was not locked with LOCK TABLES

SELECT * FROM t1 AS t1_alias2;
ERROR 1100 (HY000): Table 't1_alias2' was not locked with LOCK TABLES

SELECT * FROM t1 AS t1_alias1;
```

### WAIT/NOWAIT

Set the lock wait timeout. See [WAIT and NOWAIT](wait-and-nowait.md).

## Limitations

* `LOCK TABLES` [doesn't work when using Galera cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations). You may experience crashes or locks when used with Galera.
* `LOCK TABLES` works on XtraDB/InnoDB tables only if the [innodb\_table\_locks](../../../server-usage/storage-engines/innodb/innodb-system-variables.md) system variable is set to 1 (the default) and [autocommit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) is set to 0 (1 is default). Please note that no error message will be returned on LOCK TABLES with innodb\_table\_locks = 0.
* `LOCK TABLES` [implicitly commits](sql-statements-that-cause-an-implicit-commit.md) the active transaction, if any. Also, starting a transaction always releases all table locks acquired with LOCK TABLES. This means that there is no way to have table locks and an active transaction at the same time. The only exceptions are the transactions in [autocommit](start-transaction.md#autocommit) mode. To preserve the data integrity between transactional and non-transactional tables, the [GET\_LOCK()](../../sql-functions/secondary-functions/miscellaneous-functions/get_lock.md) function can be used.
* When using `LOCK TABLES` on a `TEMPORARY` table, it will always be locked with a `WRITE` lock.
* While a connection holds an explicit read lock on a table, it cannot modify it. If you try, the following error will be produced:

```sql
ERROR 1099 (HY000): Table 'tab_name' was locked with a READ lock and can't be updated
```

* While a connection holds an explicit lock on a table, it cannot access a non-locked table. If you try, the following error will be produced:

```sql
ERROR 1100 (HY000): Table 'tab_name' was not locked with LOCK TABLES
```

* While a connection holds an explicit lock on a table, it cannot issue the following: INSERT DELAYED, CREATE TABLE, CREATE TABLE ... LIKE, and DDL statements involving stored programs and views (except for triggers). If you try, the following error will be produced:

```sql
ERROR 1192 (HY000): Can't execute the given command because you have active locked tables or an active transaction
```

* `LOCK TABLES` can not be used in stored routines - if you try, the following error will be produced on creation:

```sql
ERROR 1314 (0A000): LOCK is not allowed in stored procedures
```

## See Also

* [UNLOCK TABLES](transactions-unlock-tables.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
