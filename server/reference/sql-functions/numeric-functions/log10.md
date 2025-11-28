---
description: >-
  Calculate base-10 logarithm. This function returns the logarithm of a number
  to the base 10.
---

# LOG10

## Syntax

```sql
LOG10(X)
```

## Description

Returns the base-10 logarithm of X.

## Examples

```sql
SELECT LOG10(2);
+-------------------+
| LOG10(2)          |
+-------------------+
| 0.301029995663981 |
+-------------------+

SELECT LOG10(100);
+------------+
| LOG10(100) |
+------------+
|          2 |
+------------+

SELECT LOG10(-100);
+-------------+
| LOG10(-100) |
+-------------+
|        NULL |
+-------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
