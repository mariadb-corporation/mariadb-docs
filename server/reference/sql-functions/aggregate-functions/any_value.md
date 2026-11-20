---
description: >-
  Return a value from any row of a group. Use ANY_VALUE to select a column that
  isn't in the GROUP BY clause when ONLY_FULL_GROUP_BY is set.
---

# ANY\_VALUE

{% hint style="info" %}
`ANY_VALUE()` is available from MariaDB 13.2.
{% endhint %}

## Syntax

```bnf
ANY_VALUE([DISTINCT] expr)
```

## Description

Returns the value of _`expr`_ from one of the rows in the group. Which row the value comes from isn't defined, and it can change with the execution plan. In particular, `ANY_VALUE()` can return `NULL` for a group that also contains non-`NULL` values. Use it when every row of the group has the same value, or when any of the values will do.

It is an [aggregate function](./), and so can be used with the [GROUP BY](../../sql-statements/data-manipulation/selecting-data/group-by.md) clause. Without `GROUP BY`, it returns one value for the whole result set. Like other aggregate functions, it can't be used in a `WHERE` clause.

The main use of `ANY_VALUE()` is with the [ONLY\_FULL\_GROUP\_BY](../../../server-management/variables-and-modes/sql_mode.md#only_full_group_by) SQL mode, which rejects queries that select a column that isn't in the `GROUP BY` clause and isn't passed to an aggregate function. Wrapping such a column in `ANY_VALUE()` satisfies that rule, and documents in the query that you don't care which row's value is returned.

The `DISTINCT` keyword is accepted, but it doesn't change the result.

`ANY_VALUE()` can be used as a [window function](../special-functions/window-functions/), and it supports the `FILTER (WHERE ...)` clause, which limits the rows the function considers.

The result has the same data type, character set, and collation as _`expr`_.

`ANY_VALUE()` is unsafe for statement-based replication, because the replica might pick a different row. With [binlog\_format=STATEMENT](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format), a statement that uses it in a write, such as `INSERT ... SELECT`, logs a 1592 note. With `MIXED`, such a statement is logged in row format.

`ANY_VALUE` isn't a reserved word, so you can still use it as a column name or alias.

## Examples

```sql
CREATE TABLE t (a INT, b INT);
INSERT INTO t VALUES (1,10),(2,10),(NULL,20),(3,20),(NULL,30),(4,40);

SET SESSION sql_mode='ONLY_FULL_GROUP_BY';
```

Selecting a column that isn't grouped fails with `ONLY_FULL_GROUP_BY`:

```sql
SELECT b, a FROM t GROUP BY b;
ERROR 1055 (42000): 'test.t.a' isn't in GROUP BY
```

With `ANY_VALUE()`, the query succeeds. For `b=20`, the group contains both `NULL` and `3`, and `ANY_VALUE()` returned `NULL`:

```sql
SELECT b, ANY_VALUE(a) FROM t GROUP BY b;
+----+--------------+
| b  | ANY_VALUE(a) |
+----+--------------+
| 10 |            1 |
| 20 |         NULL |
| 30 |         NULL |
| 40 |            4 |
+----+--------------+
```

Without `GROUP BY`, `ANY_VALUE()` aggregates the whole table into one row, so it can be combined with other aggregate functions:

```sql
SELECT COUNT(*), ANY_VALUE(b) FROM t;
+----------+--------------+
| COUNT(*) | ANY_VALUE(b) |
+----------+--------------+
|        6 |           10 |
+----------+--------------+
```

With `FILTER`, only rows that match the condition are considered:

```sql
CREATE TABLE t2 (a INT, b INT);
INSERT INTO t2 VALUES (10,1),(20,1),(15,2),(30,2),(NULL,2),(40,2);

SELECT b, ANY_VALUE(a) FILTER (WHERE a > 15) FROM t2 GROUP BY b;
+---+------------------------------------+
| b | ANY_VALUE(a) FILTER (WHERE a > 15) |
+---+------------------------------------+
| 1 |                                 20 |
| 2 |                                 30 |
+---+------------------------------------+
```

## See Also

* [GROUP BY](../../sql-statements/data-manipulation/selecting-data/group-by.md)
* [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md)
* [MIN](min.md)
* [MAX](max.md)
* [Aggregate Functions as Window Functions](../special-functions/window-functions/window-functions-overview.md#aggregate-functions-as-window-functions)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
