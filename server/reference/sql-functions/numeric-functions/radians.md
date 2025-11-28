---
description: >-
  Convert degrees to radians. This function transforms an angle measured in
  degrees to its equivalent in radians.
---

# RADIANS

## Syntax

```sql
RADIANS(X)
```

## Description

Returns the argument _`X`_, converted from degrees to radians. Note that π radians equals 180 degrees.

This is the converse of the [DEGREES()](degrees.md) function.

## Examples

```sql
SELECT RADIANS(45);
+-------------------+
| RADIANS(45)       |
+-------------------+
| 0.785398163397448 |
+-------------------+

SELECT RADIANS(90);
+-----------------+
| RADIANS(90)     |
+-----------------+
| 1.5707963267949 |
+-----------------+

SELECT RADIANS(PI());
+--------------------+
| RADIANS(PI())      |
+--------------------+
| 0.0548311355616075 |
+--------------------+

SELECT RADIANS(180);
+------------------+
| RADIANS(180)     |
+------------------+
| 3.14159265358979 |
+------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
