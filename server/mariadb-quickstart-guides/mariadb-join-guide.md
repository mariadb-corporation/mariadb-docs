---
description: >-
  This guide introduces the different types of JOINs (INNER, LEFT, RIGHT, CROSS)
  and demonstrates how to combine data from multiple tables.
---

# Joining Tables with JOIN Clauses

This guide offers a simple, hands-on introduction to three basic `JOIN` types in MariaDB: `INNER JOIN`, `CROSS JOIN`, and `LEFT JOIN`. Use these examples to understand how different joins combine data from multiple tables based on specified conditions.

### Setup: Example Tables and Data

First, create and populate two simple tables, `t1` and `t2`, to use in the `JOIN` examples:

```sql
CREATE TABLE t1 ( a INT );
CREATE TABLE t2 ( b INT );

INSERT INTO t1 VALUES (1), (2), (3);
INSERT INTO t2 VALUES (2), (4);
```

### JOIN Examples and Output

Below are examples of different `JOIN` types using the tables `t1` and `t2`.

#### INNER JOIN

An `INNER JOIN` produces a result set containing only rows that have a match in both tables for the specified join condition(s).

```sql
SELECT * FROM t1 INNER JOIN t2 ON t1.a = t2.b;
```

**Output:**

```
+------+------+
| a    | b    |
+------+------+
|    2 |    2 |
+------+------+
1 row in set (0.00 sec)
```

_Explanation:_ Only the row where `t1.a` (value 2) matches `t2.b` (value 2) is returned.

#### CROSS JOIN

A `CROSS JOIN` produces a result set in which every row from the first table is joined to every row in the second table. This is also known as a Cartesian product.

```sql
SELECT * FROM t1 CROSS JOIN t2;
```

**Output:**

```
+------+------+
| a    | b    |
+------+------+
|    1 |    2 |
|    2 |    2 |
|    3 |    2 |
|    1 |    4 |
|    2 |    4 |
|    3 |    4 |
+------+------+
6 rows in set (0.00 sec)
```

_Explanation:_ Each of the 3 rows in `t1` is combined with each of the 2 rows in `t2`, resulting in 3 \* 2 = 6 rows. _Note:_ In MariaDB, the `CROSS` keyword can often be omitted if no `ON` clause is present (e.g., `SELECT * FROM t1 JOIN t2;` or `SELECT * FROM t1, t2;` would also produce a Cartesian product).

#### LEFT JOIN (t1 LEFT JOIN t2)

A `LEFT JOIN` (or `LEFT OUTER JOIN`) produces a result set with all rows from the "left" table (`t1` in this case). If a match is found in the "right" table (`t2`), the corresponding columns from the right table are included. If no match is found, these columns are filled with `NULL`.

```sql
SELECT * FROM t1 LEFT JOIN t2 ON t1.a = t2.b;
```

**Output:**

```
+------+------+
| a    | b    |
+------+------+
|    1 | NULL |
|    2 |    2 |
|    3 | NULL |
+------+------+
3 rows in set (0.00 sec)
```

_Explanation:_ All rows from `t1` are present. For `t1.a = 1` and `t1.a = 3`, there are no matching `t2.b` values, so `b` is `NULL`. For `t1.a = 2`, a match is found (`t2.b = 2`), so `b` is `2`.

#### RIGHT JOIN (t1 RIGHT JOIN t2)

A `RIGHT JOIN` (or `RIGHT OUTER JOIN`) produces a result set with all rows from the "right" table (`t2` in this case). If a match is found in the "left" table (`t1`), the corresponding columns from the left table are included. If no match is found, these columns are filled with `NULL`.

```sql
SELECT * FROM t1 RIGHT JOIN t2 ON t1.a = t2.b;
```

**Output:**

```
+------+------+
| a    | b    |
+------+------+
|    2 |    2 |
| NULL |    4 |
+------+------+
2 rows in set (0.00 sec)
```

#### LEFT JOIN (t2 LEFT JOIN t1) - Simulating a RIGHT JOIN

This example uses a `LEFT JOIN` but with `t2` as the left table. This effectively demonstrates how a `RIGHT JOIN` would behave if `t1` were the left table and `t2` the right. A `RIGHT JOIN` includes all rows from the "right" table and `NULL`s for non-matching "left" table columns.

```sql
SELECT * FROM t2 LEFT JOIN t1 ON t1.a = t2.b;
```

**Output:**

```
+------+------+
| b    | a    |
+------+------+
|    2 |    2 |
|    4 | NULL |
+------+------+
2 rows in set (0.00 sec)
```

_Explanation:_ All rows from `t2` are present. For `t2.b = 2`, a match is found (`t1.a = 2`), so `a` is `2`. For `t2.b = 4`, there is no matching `t1.a` value, so `a` is `NULL`.

### Older (Implicit) JOIN Syntax

The first two `SELECT` statements (`INNER JOIN` and `CROSS JOIN`) are sometimes written using an older, implicit join syntax:

*   **Implicit INNER JOIN:**

    ```sql
    SELECT * FROM t1, t2 WHERE t1.a = t2.b;
    ```

    This is equivalent to `SELECT * FROM t1 INNER JOIN t2 ON t1.a = t2.b;`.
*   **Implicit CROSS JOIN (Cartesian Product):**

    ```sql
    SELECT * FROM t1, t2;
    ```

    This is equivalent to `SELECT * FROM t1 CROSS JOIN t2;`.

While this syntax works, the explicit `JOIN` syntax (`INNER JOIN`, `LEFT JOIN`, etc.) with an `ON` clause is generally preferred for clarity and to better distinguish join conditions from filtering conditions (`WHERE` clause).

### Understanding JOIN Types Summary

* **`INNER JOIN`**: Returns rows only when there is a match in both tables based on the join condition.
* **`CROSS JOIN`**: Returns the Cartesian product of the two tables (all possible combinations of rows).
* **`LEFT JOIN` (Outer Join)**: Returns all rows from the left table, and the matched rows from the right table. If there is no match, `NULL` is returned for columns from the right table.
* **`RIGHT JOIN` (Outer Join)**: Returns all rows from the right table, and the matched rows from the left table. If there is no match, `NULL` is returned for columns from the left table. (The example `SELECT * FROM t2 LEFT JOIN t1 ...` shows this behavior from `t1`'s perspective).

### Joining Multiple Tables

`JOIN` clauses can be concatenated (chained) to retrieve results from three or more tables by progressively joining them.

### See Also

* [More Advanced Joins](../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/more-advanced-joins.md)
* [JOIN Syntax](../reference/sql-statements/data-manipulation/selecting-data/joins/join-syntax.md)
* [Comma vs JOIN](../reference/sql-statements/data-manipulation/selecting-data/joins/comma-vs-join.md)
* [Joins, Subqueries and SET](../reference/sql-structure/joins-subqueries-set.md)

_The initial version of this article was copied, with permission, from_ [_Introduction\_to\_Joins_](https://hashmysql.org/wiki/Introduction_to_Joins) _on 2012-10-05._

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
