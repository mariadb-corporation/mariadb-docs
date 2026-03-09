---
description: >-
  Complete reference for JOIN Syntax in MariaDB. Complete syntax guide with all
  options, clauses, and practical examples with comprehensive examples and best.
---

# JOIN Syntax

{% hint style="info" %}
For an introduction to joins, see [Joining Tables with JOIN Clauses Guide](../../../../../mariadb-quickstart-guides/mariadb-join-guide.md).
{% endhint %}

## Description

MariaDB supports the following `JOIN` syntaxes for the `table_references` part of [SELECT](../select.md) statements and multiple-table [DELETE](../../changing-deleting-data/delete.md) and [UPDATE](../../changing-deleting-data/update.md) statements:

```sql
table_references:
    table_reference [, table_reference] ...

table_reference:
    table_factor
  | join_table

table_factor (<= MariaDB 11.6):
    tbl_name [PARTITION (partition_list)]
        [query_system_time_period_specification] [[AS] alias] [index_hint_list]
  | table_subquery [query_system_time_period_specification] [AS] alias
  | ( table_references )
  | { ON table_reference LEFT OUTER JOIN table_reference
        ON conditional_expr }

table_factor (>= MariaDB 11.7):
    tbl_name [PARTITION (partition_list)]
        [query_system_time_period_specification] [[AS] alias] [index_hint_list]
  | table_subquery [query_system_time_period_specification] [AS] alias [(column_name_list)] 
  | ( table_references )
  | { ON table_reference LEFT OUTER JOIN table_reference
        ON conditional_expr }

join_table:
    table_reference [INNER | CROSS] JOIN table_factor [join_condition]
  | table_reference STRAIGHT_JOIN table_factor
  | table_reference STRAIGHT_JOIN table_factor ON conditional_expr
  | table_reference {LEFT|RIGHT} [OUTER] JOIN table_reference join_condition
  | table_reference NATURAL [{LEFT|RIGHT} [OUTER]] JOIN table_factor

join_condition:
    ON conditional_expr
  | USING (column_list)

query_system_time_period_specification:
    FOR SYSTEM_TIME AS OF point_in_time
  | FOR SYSTEM_TIME BETWEEN point_in_time AND point_in_time
  | FOR SYSTEM_TIME FROM point_in_time TO point_in_time
  | FOR SYSTEM_TIME ALL

point_in_time:
    [TIMESTAMP] expression
  | TRANSACTION expression

index_hint_list:
    index_hint [, index_hint] ...

index_hint:
    USE {INDEX|KEY}
      [{FOR {JOIN|ORDER BY|GROUP BY}] ([index_list])
  | IGNORE {INDEX|KEY}
      [{FOR {JOIN|ORDER BY|GROUP BY}] (index_list)
  | FORCE {INDEX|KEY}
      [{FOR {JOIN|ORDER BY|GROUP BY}] (index_list)

index_list:
    index_name [, index_name] ...
```

A _table reference_ is also known as a _join expression_.

Each table can also be specified as `db_name`.`tabl_name`. This allows to write queries which involve multiple databases. See [Identifier Qualifiers](../../../../sql-structure/sql-language-structure/identifier-qualifiers.md) for syntax details.

The syntax of `table_factor` is an extension to the SQL Standard. The latter accepts only `table_reference`, not a list of them inside a pair of parentheses.

This is a conservative extension if we consider each comma in a list of table\_reference items as equivalent to an inner join. Consider this query:

```sql
SELECT * FROM t1 LEFT JOIN (t2, t3, t4)
                 ON (t2.a=t1.a AND t3.b=t1.b AND t4.c=t1.c)
```

It is equivalent to this query:

```sql
SELECT * FROM t1 LEFT JOIN (t2 CROSS JOIN t3 CROSS JOIN t4)
                 ON (t2.a=t1.a AND t3.b=t1.b AND t4.c=t1.c)
```

{% hint style="info" %}
In MariaDB, `CROSS JOIN` is a syntactic equivalent to`INNER JOIN` (they can replace each other). In standard SQL, they are not equivalent. `INNER JOIN` is used with an`ON` clause, `CROSS JOIN` is used otherwise.
{% endhint %}

In general, parentheses can be ignored in join expressions containing only inner join operations. MariaDB also supports nested joins (see [Nested Join Optimization](https://dev.mysql.com/doc/refman/5.1/en/nested-join-optimization.html)).

### Subqueries

A table subquery is specified as a parenthesized query and must contain a following derived table name (specified as _alias_ in the above syntax specification).

{% tabs %}
{% tab title="Current" %}
You can optionally specify a list of column names in parenthesis.

```sql
SELECT ic1, ic2, ic3 FROM
      (
        SELECT c1, c2, c3 FROM t1 GROUP BY c1
      ) dt2 (ic1, ic2, ic3)
    JOIN t2 ON t2.c1 = dt2.ic1
    WHERE c2 > 0
    GROUP BY ic1
```

Here, the table subquery for t1 will be materialized and named dt2, with column names ic1, ic2, ic3. These column names are used outside the subquery.
{% endtab %}

{% tab title="< 11.7" %}
You **cannot** optionally specify a list of column names in parenthesis.
{% endtab %}
{% endtabs %}

See also [Correlation Column List](../joins-subqueries/subqueries/subqueries-in-a-from-clause-derived-tables.md#correlation-column-list).

### System-Versioned Tabled

See [System-versioned tables](../../../../sql-structure/temporal-tables/system-versioned-tables.md) for more information about the `FOR SYSTEM_TIME` syntax.

### Index Hints

Index hints can be specified to affect how the MariaDB optimizer makes use of indexes. For more information, see [How to force query plans](../../../../../ha-and-performance/optimization-and-tuning/query-optimizations/index-hints-how-to-force-query-plans.md).

### Oracle Mode

{% hint style="info" %}
This feature is available from MariaDB 12.1.
{% endhint %}

#### Overview

When [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) is active, the Oracle-style `(+)`  syntax can be used. For example, the following two queries are identical:

```sql
SELECT * FROM t1 LEFT JOIN t2 ON t1.a = t2.b;
```

```sql
SELECT * FROM t1, t2 WHERE t1.a = t2.b(+);
```

Similarly, the following two queries are identical:

```sql
SELECT * FROM t1 RIGHT JOIN t2 ON t1.a = t2.b;
```

```sql
SELECT * FROM t1, t2 WHERE t1.a(+) = t2.b;
```

With more than two tables, these two queries are identical:

```sql
SELECT * FROM t1 LEFT JOIN t2 ON t1.a = t2.a LEFT JOIN t3 ON t2.a = t3.a
```

```sql
SELECT * FROM t1, t2, t3 WHERE t1.a = t2.a(+) AND t2.a = t3.a(+)
```

To "rewrite" a join query using the `(+)` syntax, use [EXPLAIN EXTENDED](../../../administrative-sql-statements/analyze-and-explain-statements/explain.md#explain-extended) (the last line is an approximation at using the "regular" `LEFT JOIN` syntax):

{% code overflow="wrap" %}
```sql
EXPLAIN EXTENDED
    SELECT * FROM t1, t2, t3 WHERE t1.a = t2.a(+) AND t2.a = t3.a(+);
id	select_type	table	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	t1	ALL	NULL	NULL	NULL	NULL	3	100.00	
1	SIMPLE	t2	ALL	NULL	NULL	NULL	NULL	3	100.00	Using where; Using join buffer (flat, BNL join)
1	SIMPLE	t3	ALL	NULL	NULL	NULL	NULL	3	100.00	Using where; Using join buffer (incremental, BNL join)
Warnings:
Note	1003	select "test"."t1"."a" AS "a","test"."t2"."a" AS "a","test"."t3"."a" AS "a" from "test"."t1" left join "test"."t2" on("test"."t2"."a" = "test"."t1"."a") left join "test"."t3" on("test"."t3"."a" = "test"."t2"."a") where 1
```
{% endcode %}

#### Limitations

The table whose columns are marked with the `(+)` operator in a subexpression (a part of the `WHERE` clause divided by `AND`) are the **inner part** of the expression. A table whose columns are not marked with the operator belong to the **outer part**.

Example of a single subexpression within a `WHERE` clause:

```sql
... WHERE t1.a = t2.a(+)
```

Example of two subexpressions within a `WHERE` clause – here, both `t1.a = t2.a(+)`  and `t2.a = t3.a(+)` are inner parts, because both contain a `(+)` operator:

```sql
... WHERE t1.a = t2.a(+) AND t2.a = t3.a(+)
```

Example of two subexpressions within a `WHERE` clause – here, `t1.a = t2.a(+)` is the inner part (because of the `(+)` operator), and `t2.a = 42` is the outer part (it doesn't have a `(+)` operator:

```sql
... WHERE t1.a = t2.a(+) AND t2.a = 42
```

"Rewritten" as a "regular" join, that clause looks like this:

```sql
... FROM t1 LEFT JOIN t2 ON (t1.a = t2.a) WHERE t2.a = 42
```

The following limitations apply:

* The `(+)` operator can only be used in a `WHERE` clause.
* The `(+)` operator can only be applied to a table column, and the column should be from the local `SELECT`, not from an outer `SELECT`.
* The `(+)` operator cannot be used with other `JOIN` methods – it must be a comma-separated list in the `FROM` clause.
* When the `WHERE` clause is split into subexpressions by `AND`, `(+)` cannot be used.
* The `(+)` operator cannot be used on the right side of an `IN` function.
* The `(+)` operator cannot be used in row operations.
* The `(+)` operator cannot be used when two or more tables are on one side of and marked with the `(+)` operator and some are not.
* The `(+)` operator cannot create loops (or cycles) of dependence, where the same table appears on both sides of the operator in one expression, or through a chain of expressions.

#### Error Codes

The following errors may occur when not adhering to the `(+)` operator limitations or for other reasons:

* `ER_INVALID_USE_OF_ORA_JOIN`
* `ER_INVALID_USE_OF_ORA_JOIN_OUTER_REF`
* `ER_INVALID_USE_OF_ORA_JOIN_WRONG_FUNC`
* `ER_INVALID_USE_OF_ORA_JOIN_ONE_TABLE`
* `ER_INVALID_USE_OF_ORA_JOIN_CYCLE`

You can find examples of the errors by error code in these files (which are [available on GitHub](https://github.com/MariaDB/server/tree/main/mysql-test/suite/compat/oracle/t)):

* `mysql-test/suite/compat/oracle/t/ora_outer_join.test`
* `mysql-test/suite/compat/oracle/t/ora_outer_join_err.test`

## Examples

```sql
SELECT left_tbl.*
  FROM left_tbl LEFT JOIN right_tbl ON left_tbl.id = right_tbl.id
  WHERE right_tbl.id IS NULL;
```

## See Also

* [Joining Tables with JOIN Clauses Guide](../../../../../mariadb-quickstart-guides/mariadb-join-guide.md)
* [More Advanced Joins](../joins-subqueries/joins/more-advanced-joins.md)
* [Comma vs JOIN](comma-vs-join.md)
* [Joins, Subqueries and SET](../../../../sql-structure/joins-subqueries-set.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
