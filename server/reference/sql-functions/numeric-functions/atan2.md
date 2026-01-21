---
description: >-
  Calculate arc tangent of two variables. This function returns the angle in
  radians between the positive x-axis and the point (X, Y).
---

# ATAN2

## Syntax

```sql
ATAN(Y,X), ATAN2(Y,X)
```

## Description

Returns the arc tangent of the two variables X and Y. It is similar to calculating the arc tangent of Y / X, except that the signs of both arguments are used to determine the quadrant of the result.

## Examples

```sql
SELECT ATAN(-2,2);
+---------------------+
| ATAN(-2,2)          |
+---------------------+
| -0.7853981633974483 |
+---------------------+

SELECT ATAN2(PI(),0);
+--------------------+
| ATAN2(PI(),0)      |
+--------------------+
| 1.5707963267948966 |
+--------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
