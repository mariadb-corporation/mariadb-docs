---
description: >-
  Assign query results to variables. This statement retrieves column values from
  a single row and stores them in local variables or user-defined variables.
---

# SELECT INTO

## Syntax

```sql
SELECT col_name [, col_name] ...
    INTO var_name [, var_name] ...
    table_expr
```

## Description

`SELECT ... INTO` enables selected columns to be stored directly into variables. No resultset is produced. The query should return a single row. If the query returns no rows, a warning with error code 1329 occurs (`No data`), and the variable values remain unchanged. If the query returns multiple rows, error 1172 occurs (Result consisted of more than one row). If it is possible that the statement may retrieve multiple rows, you can use`LIMIT 1` to limit the result set to a single row.

The `INTO` clause can also be specified at the end of the statement.

In the context of such statements that occur as part of events executed by the Event Scheduler, diagnostics messages (not only errors, but also warnings) are written to the error log, and, on\
Windows, to the application event log.

This statement can be used with both [local variables](declare-variable.md) and [user-defined variables](../../sql-structure/sql-language-structure/user-defined-variables.md).

For the complete syntax, see [SELECT](../data-manipulation/selecting-data/select.md).

Another way to set a variable's value is the [SET](set-variable.md) statement.

`SELECT ... INTO` results are not stored in the [query cache](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) even if `SQL_CACHE` is specified.

## Examples

```sql
SELECT id, data INTO @x,@y 
FROM test.t1 LIMIT 1;
SELECT * FROM t1 WHERE t1.a=@x AND t1.b=@y
```

If you want to use this construct with `UNION` you have to use the syntax:

```sql
SELECT  * INTO @x FROM (SELECT t1.a FROM t1 UNION SELECT t2.a FROM t2) dt;
```

## See Also

* [SELECT](../data-manipulation/selecting-data/select.md) - full SELECT syntax.
* [SELECT INTO OUTFILE](../data-manipulation/selecting-data/select-into-outfile.md) - formatting and writing the result to an external file.
* [SELECT INTO DUMPFILE](../data-manipulation/selecting-data/select-into-dumpfile.md) - binary-safe writing of the unformatted results to an external file.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
