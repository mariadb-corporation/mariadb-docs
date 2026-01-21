---
description: >-
  Calculate absolute value. This function returns the non-negative value of a
  number, removing any negative sign.
---

# ABS

## Syntax

```sql
ABS(X)
```

## Description

Returns the absolute (non-negative) value of `X`. If `X` is not a number, it is converted to a numeric type.

## Examples

```sql
SELECT ABS(42);
+---------+
| ABS(42) |
+---------+
|      42 |
+---------+

SELECT ABS(-42);
+----------+
| ABS(-42) |
+----------+
|       42 |
+----------+

SELECT ABS(DATE '1994-01-01');
+------------------------+
| ABS(DATE '1994-01-01') |
+------------------------+
|               19940101 |
+------------------------+
```

## See Also

* [SIGN()](sign.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
