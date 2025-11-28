---
description: >-
  Identify statements that force a commit. Certain commands, like DDL
  statements, implicitly commit the current transaction before executing.
---

# SQL statements Causing an Implicit Commit

Some SQL statements cause an implicit commit. As a rule of thumb, such statements are DDL statements. The same statements (except for [SHUTDOWN](../administrative-sql-statements/shutdown.md)) produce a 1400 error ([SQLSTATE](../programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) 'XAE09') if a XA transaction is in effect.

Here is the list:

```sql
ALTER DATABASE ... UPGRADE DATA DIRECTORY NAME
ALTER EVENT
ALTER FUNCTION
ALTER PROCEDURE
ALTER SEQUENCE
ALTER SERVER
ALTER TABLE
ALTER VIEW
ANALYZE TABLE
BEGIN
CACHE INDEX
CHANGE MASTER TO
CHECK TABLE
CREATE DATABASE
CREATE EVENT
CREATE FUNCTION
CREATE INDEX
CREATE PROCEDURE
CREATE ROLE
CREATE SEQUENCE
CREATE SERVER
CREATE TABLE
CREATE TRIGGER
CREATE USER
CREATE VIEW
DROP DATABASE
DROP EVENT
DROP FUNCTION
DROP INDEX
DROP PROCEDURE
DROP ROLE
DROP SEQUENCE
DROP SERVER
DROP TABLE
DROP TRIGGER
DROP USER
DROP VIEW
FLUSH
GRANT
LOAD INDEX INTO CACHE
LOCK TABLES
OPTIMIZE TABLE
RENAME TABLE
RENAME USER
REPAIR TABLE
RESET
REVOKE
SET PASSWORD
SHUTDOWN
START SLAVE
START TRANSACTION
STOP SLAVE
TRUNCATE TABLE
```

`SET autocommit = 1` causes an implicit commit if the value was 0.

All these statements cause an implicit commit before execution. This means that, even if the statement fails with an error, the transaction is committed. Some of them, like `CREATE TABLE ... SELECT`, also cause a commit immediatly after execution. Such statements couldn't be rollbacked in any case.

If you are not sure whether a statement has implicitly committed the current transaction, you can query the [in\_transaction](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#in_transaction) server system variable.

Note that when a transaction starts (not in autocommit mode), all locks acquired with [LOCK TABLES](lock-tables.md) are released. And acquiring such locks always commits the current transaction. To preserve the data integrity between transactional and non-transactional tables, the [GET\_LOCK()](../../sql-functions/secondary-functions/miscellaneous-functions/get_lock.md) function can be used.

## Exceptions

These statements do not cause an implicit commit in the following cases:

* [CREATE TABLE](../data-definition/create/create-table.md) and [DROP TABLE](../data-definition/drop/drop-table.md), when the `TEMPORARY` keyword is used.
  * However, [TRUNCATE TABLE](../table-statements/truncate-table.md) causes an implicit commit even when used on a temporary table.
* [CREATE FUNCTION](../data-definition/create/create-function.md) and [DROP FUNCTION](../../../server-usage/stored-routines/stored-functions/drop-function.md), when used to create a UDF (instead of a stored function). However, [CREATE INDEX](../data-definition/create/create-index.md) and [DROP INDEX](../data-definition/drop/drop-index.md) cause commits even when used with temporary tables.
* [UNLOCK TABLES](lock-tables.md) causes a commit only if a [LOCK TABLES](lock-tables.md) was used on non-transactional tables.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
