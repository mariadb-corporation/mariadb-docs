---
description: >-
  Install a user-defined function from a shared library. This command loads an
  external compiled function into the server for extended capabilities.
---

# CREATE FUNCTION UDF

## Syntax

```sql
CREATE [OR REPLACE] [AGGREGATE] FUNCTION [IF NOT EXISTS] function_name
    RETURNS {STRING|INTEGER|REAL|DECIMAL}
    SONAME shared_library_name
```

## Description

A user-defined function (UDF) is a way to extend MariaDB with a new function\
that works like a native (built-in) MariaDB function such as [ABS()](../../reference/sql-functions/numeric-functions/abs.md) or [CONCAT()](../../reference/sql-functions/string-functions/concat.md).

`function_name` is the name that should be used in SQL statements to invoke\
the function.

To create a function, you must have the [INSERT privilege](../../reference/sql-statements/account-management-sql-statements/grant.md) for the\
mysql database. This is necessary because`CREATE FUNCTION` adds a row to the [mysql.func system table](../../reference/system-tables/the-mysql-database-tables/mysql-func-table.md) that records the function's name,\
type, and shared library name. If you do not have this table, you should run\
the [mariadb-upgrade](../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) command to create it.

UDFs need to be written in C, C++ or another language that uses C calling\
conventions, MariaDB needs to have been dynamically compiled, and your\
operating system must support dynamic loading.

For an example, see `sql/udf_example.cc` in the source tree. For a collection of existing UDFs see [sql-udf](https://github.com/pluots/sql-udf).

Statements making use of user-defined functions are not [safe for replication](../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

For creating a stored function as opposed to a user-defined function, see [CREATE FUNCTION](../../reference/sql-statements/data-definition/create/create-function.md).

For valid identifiers to use as function names, see [Identifier Names](../../reference/sql-structure/sql-language-structure/identifier-names.md).

#### RETURNS

The `RETURNS` clause indicates the type of the function's\
return value, and can be one of [string](../../reference/data-types/string-data-types/), [INTEGER](../../reference/data-types/numeric-data-types/integer.md), [REAL](../../reference/data-types/numeric-data-types/real.md) or [DECIMAL](../../reference/data-types/numeric-data-types/decimal.md). `DECIMAL` functions currently return string values and should be written like [STRING](../../reference/data-types/string-data-types/) functions.

#### shared\_library\_name

`shared_library_name` is the basename of the shared object file that contains\
the code that implements the function. The file must be located in the plugin\
directory. This directory is given by the value of the [plugin\_dir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir) system variable. Note that\
before MariaDB/MySQL 5.1, the shared object could be located in any directory\
that was searched by your system's dynamic linker.

#### AGGREGATE

Aggregate functions are summary functions such as [SUM()](../../reference/sql-functions/aggregate-functions/sum.md) and [AVG()](../../reference/sql-functions/aggregate-functions/avg.md).\
Aggregate UDF functions can be used as [window functions](../../reference/sql-functions/special-functions/window-functions/).

#### OR REPLACE

If the optional `OR REPLACE` clause is used, it acts as a shortcut for:

```sql
DROP FUNCTION IF EXISTS function_name;
CREATE FUNCTION name ...;
```

#### IF NOT EXISTS

When the IF NOT EXISTS clause is used, MariaDB will return a warning instead of an error if the specified function already exists. Cannot be used together with OR REPLACE.

### Upgrading a UDF

To upgrade the UDF's shared library, first run a [DROP FUNCTION](../stored-routines/stored-functions/drop-function.md) statement, then upgrade the shared library and\
finally run the CREATE FUNCTION statement. If you upgrade without following\
this process, you may crash the server.

### Examples

```sql
CREATE FUNCTION jsoncontains_path RETURNS INTEGER SONAME 'ha_connect.so';
Query OK, 0 rows affected (0.00 sec)
```

OR REPLACE and IF NOT EXISTS:

```sql
CREATE FUNCTION jsoncontains_path RETURNS INTEGER SONAME 'ha_connect.so';
ERROR 1125 (HY000): Function 'jsoncontains_path' already exists

CREATE OR REPLACE FUNCTION jsoncontains_path RETURNS INTEGER SONAME 'ha_connect.so';
Query OK, 0 rows affected (0.00 sec)

CREATE FUNCTION IF NOT EXISTS jsoncontains_path RETURNS INTEGER SONAME 'ha_connect.so';
Query OK, 0 rows affected, 1 warning (0.00 sec)

SHOW WARNINGS;
+-------+------+---------------------------------------------+
| Level | Code | Message                                     |
+-------+------+---------------------------------------------+
| Note  | 1125 | Function 'jsoncontains_path' already exists |
+-------+------+---------------------------------------------+
```

## See Also

* [Identifier Names](../../reference/sql-structure/sql-language-structure/identifier-names.md)
* [DROP FUNCTION](../stored-routines/stored-functions/drop-function.md)
* [CREATE FUNCTION](../../reference/sql-statements/data-definition/create/create-function.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
