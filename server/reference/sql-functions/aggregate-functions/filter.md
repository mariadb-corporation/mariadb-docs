---
description: >-
  Limit the rows an aggregate function processes with FILTER (WHERE ...), so one
  query can compute several differently filtered aggregates without CASE
  expressions.
---

# FILTER Clause

## Syntax

```bnf
aggregate_function(...) FILTER (WHERE condition)
  [OVER (window_definition)]
```

## Description

The `FILTER` clause limits the rows that an [aggregate function](README.md) processes. The function sees only the rows for which `condition` is true. Rows for which it is false or `NULL` are skipped. This is the SQL standard way to write several aggregates over different subsets of the same rows in one query.

`FILTER` is available from MariaDB 13.2.

You can use `FILTER` with:

* The built-in aggregate functions, such as [AVG](avg.md), [COUNT](count.md), [GROUP\_CONCAT](group_concat.md), [MAX](max.md), [MIN](min.md), [SUM](sum.md), the [BIT\_AND](bit_and.md), [BIT\_OR](bit_or.md), and [BIT\_XOR](bit_xor.md) functions, the standard deviation and variance functions, [JSON\_ARRAYAGG](../special-functions/json-functions/json_arrayagg.md), and [JSON\_OBJECTAGG](../special-functions/json-functions/json_objectagg.md). The `DISTINCT` option works as usual, for example `COUNT(DISTINCT category) FILTER (WHERE ...)`.
* [Stored aggregate functions](../../../server-usage/stored-routines/stored-functions/stored-aggregate-functions.md) and aggregate function plugins.
* Aggregate functions used as [window functions](../special-functions/window-functions/README.md). Write `FILTER` before `OVER`. The filter applies to the rows of each window.

The `condition` is evaluated for each input row. It can be any expression allowed in a `WHERE` clause, including a subquery, with these exceptions:

* It cannot contain an aggregate function, including another `FILTER`.
* It cannot contain a window function.
* It cannot use a column alias from the `SELECT` list.

If no rows pass the filter, the result is the same as for an empty set of rows. For example, `COUNT(*)` returns `0` and `SUM()` returns `NULL`.

These uses return an error:

* A function that is not an aggregate function, such as `UPPER(name) FILTER (WHERE ...)`, fails with `Incorrect usage of FILTER and non-aggregate function`.
* A function that is only a window function, such as `RANK()` or `LAG()`, fails with a syntax error, as does putting `OVER` before `FILTER`.

{% hint style="warning" %}
`FILTER` is not a reserved word, but `SELECT SUM(x) filter FROM t` fails with a syntax error, because the server reads `filter` as the start of a `FILTER` clause. Write `AS filter` if you need a column alias with that name.
{% endhint %}

## Examples

```sql
CREATE TABLE sales (
  id INT PRIMARY KEY,
  category VARCHAR(20),
  status VARCHAR(20),
  value INT
);

INSERT INTO sales VALUES
  (1, 'Electronics', 'active', 100),
  (2, 'Electronics', 'active', 150),
  (3, 'Books', 'inactive', NULL),
  (4, 'Books', 'active', 200),
  (5, 'Electronics', 'active', 100),
  (6, 'Clothing', NULL, 50),
  (7, 'Clothing', 'active', 75),
  (8, 'Books', 'active', 200);
```

Count all rows, and the active rows, in the same query:

```sql
SELECT COUNT(*) AS total,
       COUNT(*) FILTER (WHERE status = 'active') AS active_count,
       SUM(value) FILTER (WHERE status = 'active') AS active_total
FROM sales;
+-------+--------------+--------------+
| total | active_count | active_total |
+-------+--------------+--------------+
|     8 |            6 |          825 |
+-------+--------------+--------------+
```

The row with a `NULL` status is not counted as active. Without `FILTER`, you would write the same query with `CASE` expressions:

```sql
SELECT COUNT(*) AS total,
       COUNT(CASE WHEN status = 'active' THEN 1 END) AS active_count,
       SUM(CASE WHEN status = 'active' THEN value END) AS active_total
FROM sales;
```

Use `FILTER` with `GROUP BY`:

```sql
SELECT category,
       COUNT(*) AS total,
       COUNT(*) FILTER (WHERE status = 'active') AS active_count,
       AVG(value) FILTER (WHERE status = 'active') AS active_avg
FROM sales
GROUP BY category;
+-------------+-------+--------------+------------+
| category    | total | active_count | active_avg |
+-------------+-------+--------------+------------+
| Books       |     3 |            2 |   200.0000 |
| Clothing    |     2 |            1 |    75.0000 |
| Electronics |     3 |            3 |   116.6667 |
+-------------+-------+--------------+------------+
```

Use `FILTER` with a window function. The filter applies within each partition:

```sql
SELECT id, category,
       SUM(value) FILTER (WHERE status = 'active')
         OVER (PARTITION BY category) AS category_active_total
FROM sales
ORDER BY id;
+----+-------------+-----------------------+
| id | category    | category_active_total |
+----+-------------+-----------------------+
|  1 | Electronics |                   350 |
|  2 | Electronics |                   350 |
|  3 | Books       |                   400 |
|  4 | Books       |                   400 |
|  5 | Electronics |                   350 |
|  6 | Clothing    |                    75 |
|  7 | Clothing    |                    75 |
|  8 | Books       |                   400 |
+----+-------------+-----------------------+
```

## See Also

* [Aggregate Functions](README.md)
* [GROUP BY](../../sql-statements/data-manipulation/selecting-data/group-by.md)
* [Window Functions](../special-functions/window-functions/README.md)
* [Stored Aggregate Functions](../../../server-usage/stored-routines/stored-functions/stored-aggregate-functions.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
