---
description: >-
  The VALUES table value constructor, which produces a set of rows.
---

# Table Value Constructors

## Syntax

```bnf
VALUES ( row_value[, row_value...]), (...)...
```

## Description

A Table Value Constructor (TVC) produces a set of rows from values you list, without reading from a table. You can use it:

* On its own, as a statement.
* In [UNION](../../sql-statements/data-manipulation/selecting-data/set-operations/union.md) operations, [views](../../../server-usage/views/create-view.md), and subqueries, to inject arbitrary values into the result set.
* As a derived table, in the `FROM` clause.
* In an `IN` predicate.

All rows must have the same number of values. When a TVC is combined with other queries, as in a `UNION`, it must have the same number of columns as the result set, otherwise it returns [Error 1222](../../error-codes/mariadb-error-codes-1200-to-1299/e1222.md). The columns are named after the values in the first row.

Table value constructors are available from MariaDB 10.3.3. A TVC differs from the [VALUES()](../../sql-functions/secondary-functions/miscellaneous-functions/values-value.md) function, which only has a meaning in `INSERT ... ON DUPLICATE KEY UPDATE` statements.

## Examples

As a statement on its own:

```sql
VALUES (1);
+---+
| 1 |
+---+
| 1 |
+---+

VALUES (1,'a'),(2,'b') ORDER BY 1 DESC LIMIT 1;
+---+---+
| 1 | a |
+---+---+
| 2 | b |
+---+---+
```

As a derived table:

```sql
SELECT * FROM (VALUES (1),(2)) AS v;
+---+
| 1 |
+---+
| 1 |
| 2 |
+---+
```

In an `IN` predicate:

```sql
SELECT 2 IN (VALUES (1),(2)) AS in_list;
+---------+
| in_list |
+---------+
|       1 |
+---------+
```

Using TVC's with [UNION](../../sql-statements/data-manipulation/selecting-data/set-operations/union.md) operations:

```sql
CREATE TABLE test.t1 (val1 INT, val2 INT);
INSERT INTO test.t1 VALUES(5, 8), (3, 4), (1, 2);

SELECT * FROM test.t1
UNION
VALUES (70, 90), (100, 110);

+------+------+
| val1 | val2 |
+------+------+
|    5 |    8 | 
|    3 |    4 |
|    1 |    2 |
|   70 |   90 |
|  100 |  110 |
+------+------+
```

Using TVCs with a [CREATE VIEW](../../../server-usage/views/create-view.md) statement:

```sql
CREATE VIEW v1 AS VALUES (7, 9), (9, 10);

SELECT * FROM v1;
+---+----+
| 7 |  9 |
+---+----+
| 7 |  9 |
| 9 | 10 |
+---+----+
```

Using TVC with an [ORDER BY](../../sql-statements/data-manipulation/selecting-data/order-by.md) clause:

```sql
SELECT * FROM test.t1
UNION
VALUES (10, 20), (30, 40), (50, 60), (70, 80)
ORDER BY val1 DESC;
```

Using TVC with [LIMIT](../../sql-statements/data-manipulation/selecting-data/limit.md) clause:

```sql
SELECT * FROM test.t1
UNION
VALUES (10, 20), (30, 40), (50, 60), (70, 80)
LIMIT 2 OFFSET 4;

+------+------+
| val1 | val2 |
+------+------+
|   30 |   40 | 
|   50 |   60 |
+------+------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
