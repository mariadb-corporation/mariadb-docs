---
description: >-
  Compare a value against any result from a subquery. The ANY (or SOME) operator
  returns TRUE if the comparison holds for at least one row.
---

# Subqueries With ANY and SOME

## Syntax

`SOME` is a synonym for `ANY`.&#x20;

```sql
scalar_expression comparison_operator ANY <Table subquery>
scalar_expression comparison_operator SOME <Table subquery>
```

* `scalar_expression` may be any expression that evaluates to a single value.
* `comparison_operator` may be any one of `=`, `>`, `<`, `>=`, `<=`, `<>` or `!=`.

{% hint style="info" %}
#### About IN

Although `IN` functions similarly to `= ANY`, it is documented separately due to unique optimization characteristics. Refer to [Subqueries with IN and NOT IN](../../subqueries/subqueries-with-in-and-not-in.md) for more details.
{% endhint %}

`ANY` or `SOME` returns:

* `TRUE` if the comparison operator returns `TRUE` for at least one row returned by the table subquery.
* `FALSE` if the comparison operator returns `FALSE` for all rows returned by the table subquery, or if the table subquery has no rows.
* `NULL` if the comparison operator returns `NULL` for at least one row returned by the table subquery and doesn't returns `TRUE` for any of them, or if `scalar_expression` returns `NULL`.

## Examples

The subsequent examples use these tables:

```sql
CREATE TABLE sq1 (num1 TINYINT);
CREATE TABLE sq2 (num2 TINYINT);
INSERT INTO sq1 VALUES(100);
INSERT INTO sq2 VALUES(40),(50),(120);
```

### Subquery With `ANY`

```sql
SELECT * FROM sq1 WHERE num1 > ANY (SELECT * FROM sq2);
+------+
| num1 |
+------+
|  100 |
+------+
```

`100` is greater than two of the three values, and so the expression evaluates to `true`.

### Subquery With `SOME`

`SOME` is a synonym for `ANY`.

```sql
SELECT * FROM sq1 WHERE num1 > SOME (SELECT * FROM sq2);
+------+
| num1 |
+------+
|  100 |
+------+
```

`100` is greater than two of the three values, and so the expression evaluates to `true`.

### See Also

* [Subqueries with IN](../../subqueries/subqueries-with-in-and-not-in.md)
* [Subqueries with ALL](subqueries-and-all.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
