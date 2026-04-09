---
description: >-
  Understand window function concepts. These functions operate on a set of rows
  (window) defined by an OVER clause, returning a value for each row without
  collapsing results.
---

# Window Functions Overview

## Window Functions

Window functions calculate across related rows without collapsing them. Unlike `GROUP BY`, they return one result for each input row.

## When to Use Window Functions

Use window functions when you need to:

* Rank rows inside a group.
* Calculate running totals or moving averages.
* Compare a row with earlier or later rows.
* Return the top _N_ rows per group.

## Basic Syntax

```sql
window_function(expr) OVER (
  [PARTITION BY expr [, ...]]
  [ORDER BY expr [ASC | DESC] [, ...]]
  [{ROWS | RANGE} frame_clause]
)

frame_clause:
  {frame_border | BETWEEN frame_border AND frame_border}

frame_border:
  UNBOUNDED PRECEDING
  | UNBOUNDED FOLLOWING
  | CURRENT ROW
  | expr PRECEDING
  | expr FOLLOWING
```

You can also define a named window and reuse it:

```sql
SELECT
  SUM(score) OVER w AS running_total,
  AVG(score) OVER w AS running_avg
FROM student
WINDOW w AS (
  ORDER BY score
  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
);
```

## Window Functions vs `GROUP BY`

Use `GROUP BY` when you want one output row per group.

Use a window function when you want to keep the original rows and add per-group or per-sequence calculations beside them.

```sql
SELECT test, AVG(score)
FROM student
GROUP BY test;
```

This returns one row per `test`.

```sql
SELECT
  name,
  test,
  score,
  AVG(score) OVER (PARTITION BY test) AS avg_by_test
FROM student;
```

This returns every row, plus the average for that row's `test`.

## How `OVER` Works

### `PARTITION BY`

`PARTITION BY` starts a new calculation for each group.

### `ORDER BY`

`ORDER BY` defines the row sequence inside each partition.

### Frame

The frame controls which rows contribute to the current result. Aggregate window functions use frames. Ranking functions such as `ROW_NUMBER()` and `RANK()` do not.

{% hint style="warning" %}
`OVER ()` uses the whole result set.

For aggregate window functions, `OVER (ORDER BY ...)` uses a running frame by default. In MariaDB, that default is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.
{% endhint %}

## `ROWS` vs `RANGE`

`ROWS` counts physical rows. `RANGE` groups peer rows that share the same `ORDER BY` value.

Use `ROWS` when you need strict row-by-row stepping. Use `RANGE` when ties should be treated as one peer group.

```sql
CREATE TABLE t (score INT);
INSERT INTO t VALUES (10), (10), (20);

SELECT
  score,
  SUM(score) OVER (
    ORDER BY score
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS rows_sum,
  SUM(score) OVER (
    ORDER BY score
    RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS range_sum
FROM t;
```

This produces different results for the duplicate `10` values:

```
+-------+----------+-----------+
| score | rows_sum | range_sum |
+-------+----------+-----------+
|    10 |       10 |        20 |
|    10 |       20 |        20 |
|    20 |       40 |        40 |
+-------+----------+-----------+
```

## Supported Functions

Dedicated window functions include [CUME\_DIST](cume_dist.md), [DENSE\_RANK](dense_rank.md), [FIRST\_VALUE](first_value.md), [LAG](lag.md), [LAST\_VALUE](../../secondary-functions/information-functions/last_value.md), [LEAD](lead.md), [MEDIAN](median.md), [NTH\_VALUE](nth_value.md), [NTILE](ntile.md), [PERCENTILE\_CONT](percentile_cont.md), [PERCENTILE\_DISC](percentile_disc.md), [PERCENT\_RANK](percent_rank.md), [RANK](rank.md), and [ROW\_NUMBER](row_number.md).

Aggregate functions that also work with `OVER (...)` include [AVG](../../aggregate-functions/avg.md), [BIT\_AND](../../aggregate-functions/bit_and.md), [BIT\_OR](../../aggregate-functions/bit_or.md), [BIT\_XOR](../../aggregate-functions/bit_xor.md), [COUNT](../../aggregate-functions/count.md), [MAX](../../aggregate-functions/max.md), [MIN](../../aggregate-functions/min.md), [STD](../../aggregate-functions/std.md), [STDDEV](../../aggregate-functions/stddev.md), [STDDEV\_POP](../../aggregate-functions/stddev_pop.md), [STDDEV\_SAMP](../../aggregate-functions/stddev_samp.md), [SUM](../../aggregate-functions/sum.md), [VAR\_POP](../../aggregate-functions/var_pop.md), [VAR\_SAMP](../../aggregate-functions/var_samp.md), and [VARIANCE](../../aggregate-functions/variance.md).

Aggregate window functions do not support `DISTINCT`.

### Aggregate Functions as Window Functions

It is possible to use [aggregate functions](../../aggregate-functions/) as window functions. An aggregate function used as a window function must have the `OVER` clause. For example, here's [COUNT()](../../aggregate-functions/count.md) used as a window function:

```sql
SELECT COUNT(*) OVER (ORDER BY column) FROM table;
```

## Common Pitfalls

* You cannot reference a window function in `WHERE`.
* Compute the window result in a subquery or CTE first.
* MariaDB does not support `GROUPS` frames.
* MariaDB does not support frame exclusion.
* MariaDB does not support explicit `NULLS FIRST` or `NULLS LAST`.
* `RANGE` frames do not support `DATE` or `DATETIME` arithmetic.

{% hint style="info" %}
Window functions are evaluated after `WHERE`, `GROUP BY`, and `HAVING`. Filter the computed result in an outer query or CTE.
{% endhint %}

## Examples

Given the following data:

```sql
CREATE TABLE student (
  name CHAR(10),
  test CHAR(10),
  score TINYINT
);

INSERT INTO student VALUES
  ('Chun', 'SQL', 75), ('Chun', 'Tuning', 73),
  ('Esben', 'SQL', 43), ('Esben', 'Tuning', 31),
  ('Kaolin', 'SQL', 56), ('Kaolin', 'Tuning', 88),
  ('Tatiana', 'SQL', 87), ('Tatiana', 'Tuning', 83);
```

### Average by Test

```sql
SELECT
  name,
  test,
  score,
  AVG(score) OVER (PARTITION BY test) AS avg_by_test
FROM student
ORDER BY test, name;
```

```
+---------+--------+-------+-------------+
| name    | test   | score | avg_by_test |
+---------+--------+-------+-------------+
| Chun    | SQL    |    75 |     65.2500 |
| Esben   | SQL    |    43 |     65.2500 |
| Kaolin  | SQL    |    56 |     65.2500 |
| Tatiana | SQL    |    87 |     65.2500 |
| Chun    | Tuning |    73 |     68.7500 |
| Esben   | Tuning |    31 |     68.7500 |
| Kaolin  | Tuning |    88 |     68.7500 |
| Tatiana | Tuning |    83 |     68.7500 |
+---------+--------+-------+-------------+
```

### Running Total by Score

```sql
SELECT
  name,
  score,
  SUM(score) OVER (
    ORDER BY score
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_total
FROM student
ORDER BY score;
```

```
+---------+-------+---------------+
| name    | score | running_total |
+---------+-------+---------------+
| Esben   |    31 |            31 |
| Esben   |    43 |            74 |
| Kaolin  |    56 |           130 |
| Chun    |    73 |           203 |
| Chun    |    75 |           278 |
| Tatiana |    83 |           361 |
| Tatiana |    87 |           448 |
| Kaolin  |    88 |           536 |
+---------+-------+---------------+
```

### Top 2 Scores per Test

```sql
WITH ranked AS (
  SELECT
    name,
    test,
    score,
    RANK() OVER (PARTITION BY test ORDER BY score DESC) AS rnk
  FROM student
)
SELECT
  name,
  test,
  score,
  rnk
FROM ranked
WHERE rnk <= 2
ORDER BY test, rnk, name;
```

```
+---------+--------+-------+-----+
| name    | test   | score | rnk |
+---------+--------+-------+-----+
| Tatiana | SQL    |    87 |   1 |
| Chun    | SQL    |    75 |   2 |
| Kaolin  | Tuning |    88 |   1 |
| Tatiana | Tuning |    83 |   2 |
+---------+--------+-------+-----+
```

## MariaDB Support and Limitations

MariaDB:

* Supports `ROWS` and `RANGE` frames.
* Supports all frame bounds, including `RANGE n PRECEDING` and `RANGE n FOLLOWING`.
* Does not support `GROUPS` frames.
* Does not support frame exclusion.
* Does not support explicit `NULLS FIRST` or `NULLS LAST`.
* Does not support `DATE` or `DATETIME` arithmetic for `RANGE` frames.
* Does not support `DISTINCT` for aggregate window functions.

## See Also

* [Window Frames](window-frames.md)
* [Aggregate Functions as Window Functions](/broken/spaces/SsmexDFPv2xG2OTyO5yV/pages/T8uOYfwo7PbEMtMvwoDd)
* [ROW\_NUMBER](row_number.md)
* [RANK](rank.md)
* [AVG](../../aggregate-functions/avg.md)
* [SUM](../../aggregate-functions/sum.md)
* [Introduction to Window Functions in MariaDB Server 10.2](https://mariadb.com/resources/blog/introduction-window-functions-mariadb-server-102)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
