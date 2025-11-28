---
description: >-
  Retrieve data from the database. This fundamental statement selects columns
  and rows from tables, supporting filtering, joining, and aggregation.
---

# SELECT

## Syntax

```sql
SELECT
    [/*+ hints */]
    [/*+ JOIN_PREFIX(argument_list) */]
    [/*+ JOIN_ORDER(argument_list) */]
    [/*+ JOIN_FIXED_ORDER(argument_list) */]
    [/*+ JOIN_SUFFIX(argument_list) */]
    [/*+ MAX_EXECUTION_TIME(milliseconds) */]
    [ALL | DISTINCT | DISTINCTROW]
    [HIGH_PRIORITY]
    [STRAIGHT_JOIN]
    [SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT]
    [SQL_CACHE | SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
    select_expr [, select_expr ...]
    [ FROM table_references
      [WHERE where_condition]
      [GROUP BY {col_name | expr | position} [ASC | DESC], ... [WITH ROLLUP]]
      [HAVING where_condition]
      [ORDER BY {col_name | expr | position} [ASC | DESC], ...]
      [LIMIT {[offset,] row_count | row_count OFFSET offset  
      [ROWS EXAMINED rows_limit] } |
        [OFFSET start { ROW | ROWS }]
        [FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } { ONLY | WITH TIES }] ]
      procedure|[PROCEDURE procedure_name(argument_list)]
      [INTO OUTFILE 'file_name' [CHARACTER SET charset_name] [export_options] |
        INTO DUMPFILE 'file_name' | INTO var_name [, var_name] ]
      [FOR UPDATE lock_option | LOCK IN SHARE MODE lock_option]
export_options:
    [{FIELDS | COLUMNS}
        [TERMINATED BY 'string']
        [[OPTIONALLY] ENCLOSED BY 'char']
        [ESCAPED BY 'char']
    ]
    [LINES
        [STARTING BY 'string']
        [TERMINATED BY 'string']
    ]
lock_option:
    [WAIT n | NOWAIT | SKIP LOCKED]
```

{% tabs %}
{% tab title="Current" %}
`[/*+ hints */]` syntax is available.
{% endtab %}

{% tab title="< 11.8" %}
`[/*+ hints */]` syntax is **not** available.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
Available join order hints [can be found here](../../../../ha-and-performance/optimization-and-tuning/optimizer-hints/#join-order-hints).
{% endtab %}

{% tab title="< 12.0" %}
Join order hints are **not** available.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
`[/*+ MAX_EXECUTION_TIME(`_`milliseconds`_`) */]` syntax is available.

The hint limits the time of statement execution to the number of milliseconds given in the hint argument.
{% endtab %}

{% tab title="< 12.0" %}
`[/*+ MAX_EXECUTION_TIME(`_`milliseconds`_`) */]` syntax is **not** available.
{% endtab %}
{% endtabs %}

## Description

`SELECT` is used to retrieve rows selected from one or more tables, and can include [UNION](joins-subqueries/union.md) statements and [subqueries](joins-subqueries/subqueries/).

* Each `select_expr` expression indicates a column or data that you want to retrieve. You must have at least one select expression. See [Select Expressions](select.md#select-expressions) below.
* The `FROM` clause indicates the table or tables from which to retrieve rows. Use either a single table name or a `JOIN` expression. See [JOIN](joins-subqueries/joins/join-syntax.md) for details. If no table is involved, [FROM DUAL](dual.md) can be specified.
* Each table can also be specified as `db_name`.`tabl_name`. Each column can also be specified as `tbl_name`.`col_name` or even `db_name`.`tbl_name`.`col_name`. This allows one to write queries which involve multiple databases. See [Identifier Qualifiers](../../../sql-structure/sql-language-structure/identifier-qualifiers.md) for syntax details.
* The `WHERE` clause, if given, indicates the condition or conditions that rows must satisfy to be selected. The `where_condition` is an expression that evaluates to true for each row to be selected. The statement selects all rows if there is no WHERE clause.
  * In the `WHERE` clause, you can use any of the functions and operators that MariaDB supports, except for aggregate (summary) functions. See [Functions and Operators](../../../sql-functions/) and [Functions and Modifiers for use with GROUP BY](../../../sql-functions/aggregate-functions/) (aggregate).
* Use the [ORDER BY](order-by.md) clause to order the results.
* Use the [LIMIT](limit.md) clause to restrict the results to only a certain number of rows, optionally with an offset.
* Use the [GROUP BY](group-by.md) and `HAVING` clauses to group rows together when they have columns or computed values in common.

`SELECT` can also be used to retrieve rows computed without reference to any table.

### Select Expressions

A `SELECT` statement must contain one or more select expressions, separated by commas. Each select expression can be one of the following:

* The name of a column.
* Any expression using [functions and operators](../../../sql-functions/).
* `*` to select all columns from all tables in the `FROM` clause.
* `tbl_name.*` to select all columns from just the table `tbl_name`.

When specifying a column, you can either use just the column name or qualify the column name with the name of the table using `tbl_name.col_name`. The qualified form is useful if you are joining multiple tables in the `FROM` clause. If you do not qualify the column names when selecting from multiple tables, MariaDB will try to find the column in each table. It is an error if that column name exists in multiple tables.

You can quote column names using backticks. If you are qualifying column names with table names, quote each part separately as ``tbl_name`.`col_name``.

If you use any [grouping functions](../../../sql-functions/aggregate-functions/) in any of the select expressions, all rows in your results will be implicitly grouped, as if you had used `GROUP BY NULL`. `GROUP BY NULL` being an expression behaves specially such that the entire result set is treated as a group.

### DISTINCT

A query may produce some identical rows. By default, all rows are retrieved, even when their values are the same. To explicitly specify that you want to retrieve identical rows, use the `ALL` option. If you want duplicates to be removed from the result set, use the `DISTINCT` option. `DISTINCTROW` is a synonym for `DISTINCT`. See also [COUNT DISTINCT](../../../sql-functions/aggregate-functions/count-distinct.md) and [SELECT UNIQUE in Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle#simple-syntax-compatibility).

### INTO

The `INTO` clause is used to specify that the query results should be written to a file or variable.

* [SELECT INTO OUTFILE](select-into-outfile.md) - formatting and writing the result to an external file.
* [SELECT INTO DUMPFILE](select-into-dumpfile.md) - binary-safe writing of the unformatted results to an external file.
* [SELECT INTO Variable](../../programmatic-compound-statements/selectinto.md) - selecting and setting variables.

The reverse of `SELECT INTO OUTFILE` is [LOAD DATA](../inserting-loading-data/load-data-into-tables-or-index/).

### LIMIT

Restricts the number of returned rows. See [LIMIT](limit.md) and [LIMIT ROWS EXAMINED](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/limit-rows-examined.md) for details.

### LOCK IN SHARE MODE/FOR UPDATE

See [LOCK IN SHARE MODE](lock-in-share-mode.md) and [FOR UPDATE](for-update.md) for details on the respective locking clauses.

### OFFSET ... FETCH

{% tabs %}
{% tab title="Current" %}
See [SELECT ... OFFSET ... FETCH](select-offset-fetch.md).
{% endtab %}

{% tab title="< 10.6" %}
The clause doesn't exist.
{% endtab %}
{% endtabs %}

### ORDER BY

Order a result set. See [ORDER BY](order-by.md) for details.

### PARTITION

Specifies to the optimizer which partitions are relevant for the query. Other partitions will not be read. See [Partition Pruning and Selection](../../../../server-usage/partitioning-tables/partition-pruning-and-selection.md) for details.

### PROCEDURE

Passes the whole result set to a C Procedure. See [PROCEDURE](procedure.md) and [PROCEDURE ANALYSE](../../../sql-functions/secondary-functions/information-functions/procedure-analyse.md) (the only built-in procedure not requiring the server to be recompiled).

### SKIP LOCKED

{% tabs %}
{% tab title="Current" %}
This causes rows that couldn't be locked ([LOCK IN SHARE MODE](lock-in-share-mode.md) or [FOR UPDATE](for-update.md)) to be excluded from the result set. An explicit `NOWAIT` is implied here. This is only implemented on [InnoDB](../../../../server-usage/storage-engines/innodb/) tables and ignored otherwise.
{% endtab %}

{% tab title="< 10.6" %}
The clause doesn't exist.
{% endtab %}
{% endtabs %}

### Optimizer Hints

These include [HIGH\_PRIORITY](../../../../ha-and-performance/optimization-and-tuning/optimizer-hints/#high-priority), [STRAIGHT\_JOIN](../../../../ha-and-performance/optimization-and-tuning/optimizer-hints/#straight_join), [SQL\_SMALL\_RESULT | SQL\_BIG\_RESULT](../../../../ha-and-performance/optimization-and-tuning/optimizer-hints/#sql_small_result-sql_big_result), [SQL\_BUFFER\_RESULT](../../../../ha-and-performance/optimization-and-tuning/optimizer-hints/#sql_buffer_result), [SQL\_CACHE | SQL\_NO\_CACHE](../../../../ha-and-performance/optimization-and-tuning/optimizer-hints/#sql_cache-sql_no_cache), and [SQL\_CALC\_FOUND\_ROWS](../../../../ha-and-performance/optimization-and-tuning/optimizer-hints/#sql_calc_found_rows).

See [Optimizer Hints](../../../../ha-and-performance/optimization-and-tuning/optimizer-hints/) for details.

### max\_statement\_time clause

By using [max\_statement\_time](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_statement_time) in conjunction with [SET STATEMENT](../../administrative-sql-statements/set-commands/set-statement.md), it is possible to limit the execution time of individual queries. For example:

```sql
SET STATEMENT max_statement_time=100 FOR 
  SELECT field1 FROM table_name ORDER BY field1;
```

### WAIT/NOWAIT

Set the lock wait timeout. See [WAIT and NOWAIT](../../transactions/wait-and-nowait.md).

## Examples

```sql
SELECT f1,f2 FROM t1 WHERE (f3<=10) AND (f4='y');
```

See [Getting Data from MariaDB](../../../../server-usage/data-handling/mariadb-selecting-data-guide-1.md) (Beginner tutorial), or the various sub-articles, for more examples.

## See Also

* [Getting Data from MariaDB](../../../../server-usage/data-handling/mariadb-selecting-data-guide-1.md) (Beginner tutorial)
* [Joins and Subqueries](joins-subqueries/)
* [LIMIT](limit.md)
* [ORDER BY](order-by.md)
* [GROUP BY](group-by.md)
* [Common Table Expressions](common-table-expressions/)
* [SELECT WITH ROLLUP](select-with-rollup.md)
* [SELECT INTO OUTFILE](select-into-outfile.md)
* [SELECT INTO DUMPFILE](select-into-dumpfile.md)
* [FOR UPDATE](for-update.md)
* [LOCK IN SHARE MODE](lock-in-share-mode.md)
* [Optimizer Hints](../../../../ha-and-performance/optimization-and-tuning/optimizer-hints/)
* [Oracle mode from MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
