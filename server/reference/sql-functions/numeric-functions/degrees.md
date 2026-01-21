---
description: >-
  Convert radians to degrees. This function transforms an angle measured in
  radians to its equivalent in degrees.
---

# DEGREES

## Syntax

```sql
DEGREES(X)
```

## Description

Returns the argument _`X`_, converted from radians to degrees.

This is the converse of the [RADIANS()](radians.md) function.

## Examples

```sql
SELECT DEGREES(PI());
+---------------+
| DEGREES(PI()) |
+---------------+
|           180 |
+---------------+

SELECT DEGREES(PI() / 2);
+-------------------+
| DEGREES(PI() / 2) |
+-------------------+
|                90 |
+-------------------+

SELECT DEGREES(45);
+-----------------+
| DEGREES(45)     |
+-----------------+
| 2578.3100780887 |
+-----------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
