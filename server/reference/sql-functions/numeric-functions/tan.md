---
description: >-
  Calculate tangent. This function returns the tangent of an angle given in
  radians.
---

# TAN

## Syntax

```sql
TAN(X)
```

## Description

Returns the tangent of X, where X is given in radians.

## Examples

```sql
SELECT TAN(0.7853981633974483);
+-------------------------+
| TAN(0.7853981633974483) |
+-------------------------+
|      0.9999999999999999 |
+-------------------------+

SELECT TAN(PI());
+-----------------------+
| TAN(PI())             |
+-----------------------+
| -1.22460635382238e-16 |
+-----------------------+

SELECT TAN(PI()+1);
+-----------------+
| TAN(PI()+1)     |
+-----------------+
| 1.5574077246549 |
+-----------------+

SELECT TAN(RADIANS(PI()));
+--------------------+
| TAN(RADIANS(PI())) |
+--------------------+
| 0.0548861508080033 |
+--------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
