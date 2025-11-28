---
description: >-
  Test for the existence of rows. The EXISTS operator returns TRUE if the
  subquery returns at least one row, often used for correlated subqueries.
---

# Subqueries and EXISTS

## Syntax

```sql
SELECT ... WHERE EXISTS <Table subquery>
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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
