---
description: >-
  How MariaDB compares row constructors such as (a, b) = (1, 2), and which
  row comparisons the optimizer can use an index for.
---

# Row Constructor Optimization

A row constructor groups several values into one tuple, written `(expr1, expr2, ...)` or `ROW(expr1, expr2, ...)`. You can compare two rows of the same size, or test a row against a list of rows with `IN`:

```sql
SELECT * FROM t1 WHERE (a, b) = (1, 2);
SELECT * FROM t1 WHERE (a, b) IN ((1, 2), (3, 4));
SELECT * FROM t1 WHERE (a, b) > (98, 30);
```

Whether the optimizer can use an index for such a condition depends on the operator. Equality and `IN` work as well as their single-column forms. The other comparisons don't use an index, so rewrite them if the query needs one.

## How Rows Are Compared

Both rows must have the same number of elements. Otherwise the statement fails with `ERROR 1241 (21000): Operand should contain 2 column(s)`.

* `=` is true when every pair of elements is equal. `(a, b) = (1, 2)` means `a = 1 AND b = 2`.
* `<>` and `!=` are true when at least one pair differs.
* `<`, `<=`, `>` and `>=` compare the elements from left to right and decide at the first pair that differs, the way words are sorted in a dictionary. `(a, b) > (98, 30)` means `a > 98 OR (a = 98 AND b > 30)`.
* `<=>` is the NULL-safe version of `=`.
* `IN` is true when the row equals one of the rows in the list.

A `NULL` element makes the result `NULL` only when the outcome depends on it:

```sql
SELECT (1, NULL) = (1, 2), (1, NULL) = (2, 2), (1, NULL) < (2, 0), (1, 2) < (1, NULL);
```

```
+--------------------+--------------------+--------------------+--------------------+
| (1, NULL) = (1, 2) | (1, NULL) = (2, 2) | (1, NULL) < (2, 0) | (1, 2) < (1, NULL) |
+--------------------+--------------------+--------------------+--------------------+
|               NULL |                  0 |                  1 |               NULL |
+--------------------+--------------------+--------------------+--------------------+
```

`(1, NULL) = (2, 2)` is false because the first elements already differ, and `(1, NULL) < (2, 0)` is true for the same reason.

A row constructor can't be a column of a result set: `SELECT (1, 2)` fails with error 1241. To compare a row with the result of a query, use a [row subquery](../../../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-row-subqueries.md).

## What the Optimizer Does

The examples use this table:

```sql
CREATE TABLE t1 (a INT, b INT, c INT, KEY ab (a, b));
INSERT INTO t1 SELECT seq % 100, seq % 37, seq FROM seq_1_to_20000;
ANALYZE TABLE t1 PERSISTENT FOR ALL;
```

### Equality

The optimizer splits a row equality into one equality per element before it plans the query, so `(a, b) = (1, 2)` is planned exactly like `a = 1 AND b = 2`, and nested rows are split the same way:

```sql
EXPLAIN SELECT * FROM t1 WHERE (a, b) = (1, 2);
```

```
+------+-------------+-------+------+---------------+------+---------+-------------+------+-------+
| id   | select_type | table | type | possible_keys | key  | key_len | ref         | rows | Extra |
+------+-------------+-------+------+---------------+------+---------+-------------+------+-------+
|    1 | SIMPLE      | t1    | ref  | ab            | ab   | 10      | const,const | 6    |       |
+------+-------------+-------+------+---------------+------+---------+-------------+------+-------+
```

### IN

For `(a, b) IN ((1, 2), (3, 4))`, the optimizer builds a range scan from `(a = 1 AND b = 2) OR (a = 3 AND b = 4)`:

```sql
EXPLAIN SELECT * FROM t1 WHERE (a, b) IN ((1, 2), (3, 4));
```

```
+------+-------------+-------+-------+---------------+------+---------+------+------+-------------+
| id   | select_type | table | type  | possible_keys | key  | key_len | ref  | rows | Extra       |
+------+-------------+-------+-------+---------------+------+---------+------+------+-------------+
|    1 | SIMPLE      | t1    | range | ab            | ab   | 10      | NULL | 12   | Using where |
+------+-------------+-------+-------+---------------+------+---------+------+------+-------------+
```

The row doesn't need to match the index exactly. For `(a, c) IN ((1, 2), (3, 4))`, the range scan uses the `a` part of the `ab` index, and the server checks `c` for each row it reads.

`NOT IN` with a row never uses a range scan.

A long `IN` list is converted into a subquery instead of a range scan once it holds [`in_predicate_conversion_threshold`](../system-variables/server-system-variables.md#in_predicate_conversion_threshold) values (1000 by default). Each element of each row counts as a value, so a list of 500 two-column rows reaches the default threshold. See [Conversion of Big IN Predicates Into Subqueries](subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md).

### Other Comparisons

The optimizer can't build a range scan from `<`, `<=`, `>`, `>=`, `<>`, or `<=>` when the operands are rows. The condition is checked for every row the server reads, which is usually a full table scan:

```sql
EXPLAIN SELECT * FROM t1 WHERE (a, b) > (98, 30);
```

```
+------+-------------+-------+------+---------------+------+---------+------+-------+-------------+
| id   | select_type | table | type | possible_keys | key  | key_len | ref  | rows  | Extra       |
+------+-------------+-------+------+---------------+------+---------+------+-------+-------------+
|    1 | SIMPLE      | t1    | ALL  | NULL          | NULL | NULL    | NULL | 20000 | Using where |
+------+-------------+-------+------+---------------+------+---------+------+-------+-------------+
```

Write the comparison out element by element, and the optimizer can use the index:

```sql
EXPLAIN SELECT * FROM t1 WHERE a > 98 OR (a = 98 AND b > 30);
```

```
+------+-------------+-------+-------+---------------+------+---------+------+------+-----------------------+
| id   | select_type | table | type  | possible_keys | key  | key_len | ref  | rows | Extra                 |
+------+-------------+-------+-------+---------------+------+---------+------+------+-----------------------+
|    1 | SIMPLE      | t1    | range | ab            | ab   | 10      | NULL | 232  | Using index condition |
+------+-------------+-------+-------+---------------+------+---------+------+------+-----------------------+
```

This pattern is common in [pagination](pagination-optimization.md) that continues from the last row of the previous page.

## See Also

* [Row Subqueries](../../../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-row-subqueries.md)
* [IN](../../../reference/sql-structure/operators/comparison-operators/in.md)
* [Conversion of Big IN Predicates Into Subqueries](subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
