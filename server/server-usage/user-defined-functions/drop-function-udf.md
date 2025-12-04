# DROP FUNCTION UDF

## Syntax

```sql
DROP FUNCTION [IF EXISTS] function_name
```

## Description

This statement drops the [user-defined function](./) (UDF) named `function_name`.

To drop a function, you must have the [DELETE privilege](../../reference/sql-statements/account-management-sql-statements/grant.md) for the mysql database. This is because `DROP FUNCTION` removes the row from the [mysql.func](../../reference/system-tables/the-mysql-database-tables/mysql-func-table.md) system table that records the function's name, type and shared library name.

For dropping a stored function, see [DROP FUNCTION](../stored-routines/stored-functions/drop-function.md).

### Upgrading a UDF

To upgrade the UDF's shared library, first run a [DROP FUNCTION](../stored-routines/stored-functions/drop-function.md) statement, then upgrade the shared library and finally run the CREATE FUNCTION statement. If you upgrade without following this process, you may crash the server.

## Examples

```sql
DROP FUNCTION jsoncontains_path;
```

IF EXISTS:

```sql
DROP FUNCTION jsoncontains_path;
ERROR 1305 (42000): FUNCTION test.jsoncontains_path does not exist

DROP FUNCTION IF EXISTS jsoncontains_path;
Query OK, 0 rows affected, 1 warning (0.00 sec)

SHOW WARNINGS;
+-------+------+------------------------------------------------+
| Level | Code | Message                                        |
+-------+------+------------------------------------------------+
| Note  | 1305 | FUNCTION test.jsoncontains_path does not exist |
+-------+------+------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
