---
description: >-
  Review the full syntax for SQL joins in MariaDB. This guide details the
  structure of table references, index hints, and various join types supported
  in SELECT, UPDATE, and DELETE statements.
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

When [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) is active, the Oracle-style `+` syntax can be used. For example, the following two queries are identical:

```sql
SELECT * FROM t1 LEFT JOIN t2 ON t1.a = t2.b;
```

and

```sql
SELECT * FROM t1, t2 WHERE t1.a = t2.b(+);
```

Similarly, the following two queries are identical:

```sql
SELECT * FROM t1 RIGHT JOIN t2 ON t1.a = t2.b;
```

and

```sql
SELECT * FROM t1, t2 WHERE t1.a(+) = t2.b;
```

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
