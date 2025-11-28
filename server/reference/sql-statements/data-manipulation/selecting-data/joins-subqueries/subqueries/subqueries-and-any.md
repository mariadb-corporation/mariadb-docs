---
description: >-
  Compare a value against any result from a subquery. The ANY (or SOME) operator
  returns TRUE if the comparison holds for at least one row.
---

# Subqueries and ANY

[Subqueries](./) using the ANY keyword will return `true` if the comparison returns `true` for at least one row returned by the subquery.

## Syntax

The required syntax for an `ANY` or `SOME` quantified comparison is:

```sql
scalar_expression comparison_operator ANY <Table subquery>
```

Or:

```sql
scalar_expression comparison_operator SOME <Table subquery>
```

* `scalar_expression` may be any expression that evaluates to a single value.
* `comparison_operator` may be any one of `=`, `>`, `<`, `>=`, `<=`, `<>` or `!=`.

`ANY` returns:

* `TRUE` if the comparison operator returns `TRUE` for at least one row returned by the Table subquery.
* `FALSE` if the comparison operator returns `FALSE` for all rows returned by the Table subquery, or Table subquery has zero rows.
* `NULL` if the comparison operator returns `NULL` for at least one row returned by the Table subquery and doesn't returns `TRUE` for any of them, or if scalar\_expression returns `NULL`.

`SOME` is a synonym for `ANY`, and `IN` is a synonym for `= ANY` .

## Examples

```sql
CREATE TABLE sq1 (num TINYINT);

CREATE TABLE sq2 (num2 TINYINT);

INSERT INTO sq1 VALUES(100);

INSERT INTO sq2 VALUES(40),(50),(120);

SELECT * FROM sq1 WHERE num > ANY (SELECT * FROM sq2);
+------+
| num  |
+------+
|  100 |
+------+
```

`100` is greater than two of the three values, and so the expression evaluates as true.

SOME is a synonym for ANY:

```sql
SELECT * FROM sq1 WHERE num < SOME (SELECT * FROM sq2);
+------+
| num  |
+------+
|  100 |
+------+
```

`IN` is a synonym for `= ANY`, and here there are no matches, so no results are returned:

```sql
SELECT * FROM sq1 WHERE num IN (SELECT * FROM sq2);
Empty set (0.00 sec)
```

```sql
INSERT INTO sq2 VALUES(100);
Query OK, 1 row affected (0.05 sec)

SELECT * FROM sq1 WHERE num <> ANY (SELECT * FROM sq2);
+------+
| num  |
+------+
|  100 |
+------+
```

Reading this query, the results may be counter-intuitive. It may seem to read as `SELECT * FROM` sq1 `WHERE` num does not match any results in sq2. Since it does match 100, it could seem that the results are incorrect. However, the query returns a result if the match does not match any _of_ sq2. Since `100` already does not match `40`, the expression evaluates to true immediately, regardless of the 100's matching. It may be more easily readable to use `SOME` in a case such as this:

```sql
SELECT * FROM sq1 WHERE num <> SOME (SELECT * FROM sq2);
+------+
| num  |
+------+
|  100 |
+------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
