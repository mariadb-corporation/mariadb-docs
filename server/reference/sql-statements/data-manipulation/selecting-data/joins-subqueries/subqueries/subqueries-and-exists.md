---
description: >-
  Test for the existence of rows. The EXISTS operator returns TRUE if the
  subquery returns at least one row, often used for correlated subqueries.
---

# Subqueries and EXISTS

## Syntax

```bnf
SELECT ... WHERE [NOT] EXISTS <Table subquery>
SELECT [NOT] EXISTS <Table subquery>, ...
```

## Description

[Subqueries](./) using the `EXISTS` keyword will return `true` if the subquery returns any rows. Conversely, subqueries using `NOT EXISTS` will return `true` only if the subquery returns no rows from the table.

EXISTS subqueries ignore the columns specified by the [SELECT](../../select.md) of the subquery, since they're not relevant. For example,

```sql
SELECT col1 FROM t1 WHERE EXISTS (SELECT * FROM t2);
```

and

```sql
SELECT col1 FROM t1 WHERE EXISTS (SELECT col2 FROM t2);
```

produce identical results.

`EXISTS` is an expression that returns `1` or `0`, never `NULL`, so it can also be used in the select list. A subquery row that contains only `NULL` values still counts as a row, so `EXISTS (SELECT NULL)` returns `1`.

`EXISTS` is most often used with a correlated subquery, which refers to a column of the outer query and is evaluated for each outer row.

## Examples

```sql
CREATE TABLE sq1 (num TINYINT);

CREATE TABLE sq2 (num2 TINYINT);

INSERT INTO sq1 VALUES(100);

INSERT INTO sq2 VALUES(40),(50),(60);

SELECT * FROM sq1 WHERE EXISTS (SELECT * FROM sq2 WHERE num2>50);
+------+
| num  |
+------+
|  100 |
+------+

SELECT * FROM sq1 WHERE NOT EXISTS (SELECT * FROM sq2 GROUP BY num2 HAVING MIN(num2)=40);
Empty set (0.00 sec)
```

A correlated subquery, where the inner `WHERE` refers to `num` from the outer row. After adding a second row to `sq1`, only `30` is smaller than some value in `sq2`:

```sql
INSERT INTO sq1 VALUES(30);

SELECT * FROM sq1 WHERE EXISTS (SELECT * FROM sq2 WHERE num2 > num);
+------+
| num  |
+------+
|   30 |
+------+

SELECT * FROM sq1 WHERE NOT EXISTS (SELECT * FROM sq2 WHERE num2 > num);
+------+
| num  |
+------+
|  100 |
+------+
```

`EXISTS` in the select list returns `1` or `0` for each row:

```sql
SELECT num, EXISTS (SELECT * FROM sq2 WHERE num2 > num) AS smaller_than_some FROM sq1;
+------+-------------------+
| num  | smaller_than_some |
+------+-------------------+
|  100 |                 0 |
|   30 |                 1 |
+------+-------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
