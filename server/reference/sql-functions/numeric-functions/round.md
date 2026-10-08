---
description: >-
  Round a number. This function rounds a number to a specified number of decimal
  places.
---

# ROUND

## Syntax

```
ROUND(X), ROUND(X,D)
```

## Description

Rounds the argument `X` to `D` decimal places. `D` defaults to `0` if not specified.`D` can be negative to cause `D` digits left of the decimal point of the value `X` to become zero.

The rounding algorithm depends on the data type of `X`:

* For floating-point types ([FLOAT](../../data-types/numeric-data-types/float.md), [DOUBLE](../../data-types/numeric-data-types/double.md)) the C libraries rounding function is used, so the behavior _may_ differ between operating systems.
* For fixed-point types ([DECIMAL](../../data-types/numeric-data-types/decimal.md), [DEC/NUMBER/FIXED](../../data-types/numeric-data-types/dec-numeric-fixed.md)) the "round half up" rule is used, meaning that e.g. a value ending in exactly .5 is always rounded up.

## Examples

```sql
SELECT ROUND(-1.23);
+--------------+
| ROUND(-1.23) |
+--------------+
|           -1 |
+--------------+

SELECT ROUND(-1.58);
+--------------+
| ROUND(-1.58) |
+--------------+
|           -2 |
+--------------+

SELECT ROUND(1.58); 
+-------------+
| ROUND(1.58) |
+-------------+
|           2 |
+-------------+

SELECT ROUND(1.298, 1);
+-----------------+
| ROUND(1.298, 1) |
+-----------------+
|             1.3 |
+-----------------+

SELECT ROUND(1.298, 0);
+-----------------+
| ROUND(1.298, 0) |
+-----------------+
|               1 |
+-----------------+

SELECT ROUND(23.298, -1);
+-------------------+
| ROUND(23.298, -1) |
+-------------------+
|                20 |
+-------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
