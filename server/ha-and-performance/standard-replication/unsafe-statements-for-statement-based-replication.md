---
description: >-
  Identify unsafe statements for statement-based replication in MariaDB Server.
  This section details SQL commands that can cause inconsistencies, guiding you
  toward safer replication practices.
---

# Unsafe Statements for Statement-Based Replication

A safe statement is generally deterministic; in other words the statement will always produce the same result. For example, an INSERT statement producing a random number will most likely produce a different result on the primary than on the replica, and so cannot be replicated safely.

When an unsafe statement is run, the current binary logging format determines how the server responds.

* If the binary logging format is [statement-based](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging), unsafe statements generate a warning and are logged normally.
* If the binary logging format is [mixed](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#mixed-logging), unsafe statements are logged using the row-based format, while safe statements use the statement-based format.
* If the binary logging format is [row-based](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#row-based-logging), all statements are logged normally, and the distinction between safe and unsafe is not made.

MariaDB tries to detect unsafe statements. When an unsafe statement is issued, a warning similar to the following is produced:

```sql
Note (Code 1592): Unsafe statement written to the binary log using statement format since 
  BINLOG_FORMAT = STATEMENT. The statement is unsafe because it uses a LIMIT clause. This 
  is unsafe because the set of rows included cannot be predicted.
```

MariaDB also issues this warning for some classes of statements that are safe.

## Unsafe Statements

The following statements are regarded as unsafe:

* [INSERT ... ON DUPLICATE KEY UPDATE](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-on-duplicate-key-update.md) statements using tables with multiple primary or unique keys, as the order that the keys are checked in, and which affect the rows chosen to update, is not deterministic. The warning about this was removed, because we always check keys in the same order on the primary and replica if the primary and replica are using the same storage engine.
* [INSERT-DELAYED](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md). These statements are inserted in an indeterminate order.
* [INSERT ... SELECT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-select.md) for a table that has an [AUTO\_INCREMENT](../../reference/data-types/auto_increment.md) column.
* [INSERTs](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) on tables with a composite primary key that has an [AUTO\_INCREMENT](../../reference/data-types/auto_increment.md) column that isn't the first column of the composite key.
* When a table has an [AUTO\_INCREMENT](../../reference/data-types/auto_increment.md) column and a [trigger](../../server-usage/triggers-events/triggers/) or [stored procedure](../../server-usage/stored-routines/) executes an [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) statement against the table.
* [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) statements that use [LIMIT](../../reference/sql-statements/data-manipulation/selecting-data/select.md#limit), since the order of the returned rows is unspecified. This applies even to statements using an ORDER BY clause, which are deterministic (a known bug). However, `LIMIT 0` is an exception to this rule (see [MDEV-6170](https://jira.mariadb.org/browse/MDEV-6170)), and these statements are safe for replication.
* When using a [user-defined function](../../server-usage/user-defined-functions/).
* Statements using any of the following functions, which can return different results on the replica:
  * [CURRENT\_ROLE()](../../reference/sql-functions/secondary-functions/information-functions/current_role.md)
  * [CURRENT\_USER()](../../reference/sql-functions/secondary-functions/information-functions/current_user.md)
  * [FOUND\_ROWS()](../../reference/sql-functions/secondary-functions/information-functions/found_rows.md)
  * [GET\_LOCK()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/get_lock.md)
  * [IS\_FREE\_LOCK()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/is_free_lock.md)
  * [IS\_USED\_LOCK()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/is_used_lock.md)
  * [JSON\_TABLE()](../../reference/sql-functions/special-functions/json-functions/json_table.md)
  * [LOAD\_FILE()](../../reference/sql-functions/string-functions/load_file.md)
  * [MASTER\_POS\_WAIT()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/master_pos_wait.md)
  * [RAND()](../../reference/sql-functions/numeric-functions/rand.md)
  * [RANDOM\_BYTES()](../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/random_bytes.md)
  * [RELEASE\_ALL\_LOCKS()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/release_all_locks.md)
  * [RELEASE\_LOCK()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/release_lock.md)
  * [ROW\_COUNT()](../../reference/sql-functions/secondary-functions/information-functions/row_count.md)
  * [SESSION\_USER()](../../reference/sql-functions/secondary-functions/information-functions/session_user.md)
  * [SLEEP()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/sleep.md)
  * [SYSDATE()](../../reference/sql-functions/date-time-functions/sysdate.md)
  * [SYSTEM\_USER()](../../reference/sql-functions/secondary-functions/information-functions/system_user.md)
  * [USER()](../../reference/sql-functions/secondary-functions/information-functions/user.md)
  * [UUID()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/uuid.md)
  * [UUID\_SHORT()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/uuid_short.md).
* Statements which refer to log tables, since these may differ across servers.
* Statements which refer to self-logging tables. Statements following a read or write to a self-logging table within a transaction are also considered unsafe.
* Statements which refer to [system variables](../optimization-and-tuning/system-variables/server-system-variables.md) (there are a few exceptions).
* [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statements.
* Non-transactional reads or writes that execute after transactional reads within a transaction.
* If row-based logging is used for a statement, and the session executing the statement has any temporary tables, row-based logging is used for the remaining statements until the temporary table is dropped. This is because temporary tables can't use row-based logging, so if it is used due to one of the above conditions, all subsequent statements using that table are unsafe. The server deals with this situation by treating all statements in the session as unsafe for statement-based logging until the temporary table is dropped.

## Safe Statements

The following statements are not deterministic, but are considered safe for binary logging and replication:

* [CONNECTION\_ID()](../../reference/sql-functions/secondary-functions/information-functions/connection_id.md)
* [CURDATE()](../../reference/sql-functions/date-time-functions/curdate.md)
* [CURRENT\_DATE()](../../reference/sql-functions/date-time-functions/current_date.md)
* [CURRENT\_TIME()](../../reference/sql-functions/date-time-functions/current_time.md)
* [CURRENT\_TIMESTAMP()](../../reference/sql-functions/date-time-functions/current_timestamp.md)
* [CURTIME()](../../reference/sql-functions/date-time-functions/curtime.md)
* [LAST\_INSERT\_ID()](../../reference/sql-functions/secondary-functions/information-functions/last_insert_id.md)
* [LOCALTIME()](../../reference/sql-functions/date-time-functions/localtime.md)
* [LOCALTIMESTAMP()](../../reference/sql-functions/date-time-functions/localtimestamp.md)
* [NOW()](../../reference/sql-functions/date-time-functions/now.md)
* [UNIX\_TIMESTAMP()](../../reference/sql-functions/date-time-functions/unix_timestamp.md)
* [UTC\_DATE()](../../reference/sql-functions/date-time-functions/utc_date.md)
* [UTC\_TIME()](../../reference/sql-functions/date-time-functions/utc_time.md)
* [UTC\_TIMESTAMP()](../../reference/sql-functions/date-time-functions/utc_timestamp.md)

## Isolation Levels

Even when using safe statements, not all [transaction isolation levels](../../reference/sql-statements/transactions/set-transaction.md#isolation-levels) are safe with statement-based or mixed binary logging. The REPEATABLE READ and SERIALIZABLE isolation levels can only be used with the row-based format.

This restriction does not apply if only non-transactional storage engines are used.

## See Also

* [Replication and Foreign Keys](replication-and-foreign-keys.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
