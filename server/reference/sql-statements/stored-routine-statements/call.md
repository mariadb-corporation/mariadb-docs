---
description: >-
  Invoke a stored procedure. This statement executes a previously created stored
  procedure, optionally passing parameters and returning results.
---

# CALL

## Syntax

```sql
CALL sp_name([parameter[,...]])
CALL sp_name[()]
```

## Description

The `CALL` statement invokes a [stored procedure](../../../server-usage/stored-routines/stored-procedures/) that was defined previously with [CREATE PROCEDURE](../../../server-usage/stored-routines/stored-procedures/create-procedure.md).

Stored procedure names can be specified as `database_name.procedure_name`. Procedure names and database names can be quoted with backticks (). This is necessary if they are reserved words, or contain special characters. See [identifier qualifiers](../../sql-structure/sql-language-structure/identifier-qualifiers.md) for details.

`CALL p()` and `CALL p` are equivalent.

If parentheses are used, any number of spaces, tab characters and newline characters are allowed between the procedure's name and the open parenthesis.

`CALL` can pass back values to its caller using parameters that are declared as `OUT` or `INOUT`\
parameters. If no value is assigned to an `OUT` parameter, `NULL` is assigned (and its former value is lost). To pass such values from another stored program you can use [user-defined variables](../../sql-structure/sql-language-structure/user-defined-variables.md), [local variables](../programmatic-compound-statements/declare-variable.md) or routine's parameters; in other contexts, you can only use user-defined variables.

`CALL` can also be executed as a prepared statement. Placeholders can be used for `IN` parameters in all versions of MariaDB; for `OUT` and `INOUT` parameters, placeholders can be used since [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5).

When the procedure returns, a client program can also obtain the number of rows affected for the final statement executed within the routine: At the SQL level, call the [ROW\_COUNT()](../built-in-functions/secondary-functions/information-functions/row_count.md) function; from the C\
API, call the `mysql_affected_rows()` function.

If the `CLIENT_MULTI_RESULTS` API flag is set, `CALL` can return any number of result sets and the called stored procedure can execute prepared statements. If it is not set, at most one result set can be returned and prepared statements cannot be used within procedures.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
