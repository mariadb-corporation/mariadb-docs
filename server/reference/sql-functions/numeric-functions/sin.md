---
description: Calculate sine. This function returns the sine of an angle given in radians.
---

# SIN

## Syntax

```sql
SIN(X)
```

## Description

Returns the sine of X, where X is given in radians.

## Examples

```sql
SELECT SIN(1.5707963267948966);
+-------------------------+
| SIN(1.5707963267948966) |
+-------------------------+
|                       1 |
+-------------------------+

SELECT SIN(PI());
+----------------------+
| SIN(PI())            |
+----------------------+
| 1.22460635382238e-16 |
+----------------------+

SELECT ROUND(SIN(PI()));
+------------------+
| ROUND(SIN(PI())) |
+------------------+
|                0 |
+------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
