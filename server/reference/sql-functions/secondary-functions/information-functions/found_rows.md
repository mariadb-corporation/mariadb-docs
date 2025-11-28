---
description: >-
  Count rows found by the last SELECT statement. This function returns the total
  number of rows matching the query, disregarding any LIMIT clause.
---

# FOUND\_ROWS

## Syntax

```sql
FOUND_ROWS()
```

## Description

A [SELECT](../../../sql-statements/data-manipulation/selecting-data/select.md) statement may include a [LIMIT](../../../sql-statements/data-manipulation/selecting-data/select.md#limit) clause to restrict the number of rows the server returns to the client. In some cases, it is desirable to know how many rows the statement would have returned without the LIMIT, but without running the statement again. To obtain this row count, include an [SQL\_CALC\_FOUND\_ROWS](../../../../ha-and-performance/optimization-and-tuning/optimizer-hints/#sql_calc_found_rows) option in the `SELECT` statement, and then invoke `FOUND_ROWS()` afterwards.

You can also use `FOUND_ROWS()` to obtain the number of rows returned by a `SELECT` which does not contain a `LIMIT` clause. In this case you don't need to use the `SQL_CALC_FOUND_ROWS` option. This can be useful for example in a [stored procedure](../../../../server-usage/stored-routines/stored-procedures/).

Also, this function works with some other statements which return a result set, including [SHOW](../../../sql-statements/administrative-sql-statements/show/), [DESC](../../../sql-statements/administrative-sql-statements/describe.md) and [HELP](../../../sql-statements/administrative-sql-statements/help-command.md). For [DELETE ... RETURNING](../../../sql-statements/data-manipulation/changing-deleting-data/delete.md) you should use [ROW\_COUNT()](row_count.md). It also works as a [prepared statement](../../../sql-statements/prepared-statements/), or after executing a prepared statement.

Statements which don't return any results don't affect `FOUND_ROWS()` - the previous value will still be returned.

**Warning:** When used after a [CALL](../../../sql-statements/stored-routine-statements/call.md) statement, this function returns the number of rows selected by the last query in the procedure, not by the whole procedure.

Statements using the `FOUND_ROWS()` function are not [safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

## Examples

```sql
SHOW ENGINES\G
*************************** 1. row ***************************
      Engine: CSV
     Support: YES
     Comment: Stores tables as CSV files
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 2. row ***************************
      Engine: MRG_MyISAM
     Support: YES
     Comment: Collection of identical MyISAM tables
Transactions: NO
          XA: NO
  Savepoints: NO

...

*************************** 8. row ***************************
      Engine: PERFORMANCE_SCHEMA
     Support: YES
     Comment: Performance Schema
Transactions: NO
          XA: NO
  Savepoints: NO
8 rows in set (0.000 sec)

SELECT FOUND_ROWS();
+--------------+
| FOUND_ROWS() |
+--------------+
|           8 |
+--------------+
```

```sql
SELECT SQL_CALC_FOUND_ROWS * FROM tbl_name WHERE id > 100 LIMIT 10;
...
SELECT FOUND_ROWS();
+--------------+
| FOUND_ROWS() |
+--------------+
|           23 |
+--------------+
```

## See Also

* [ROW\_COUNT()](row_count.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
