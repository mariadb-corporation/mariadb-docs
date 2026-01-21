---
description: >-
  Calculate arc tangent. This function returns the angle in radians whose
  tangent is the given number.
---

# ATAN

## Syntax

```sql
ATAN(X)
```

## Description

Returns the arc tangent of X, that is, the value whose tangent is X.

## Examples

```sql
SELECT ATAN(2);
+--------------------+
| ATAN(2)            |
+--------------------+
| 1.1071487177940904 |
+--------------------+

SELECT ATAN(-2);
+---------------------+
| ATAN(-2)            |
+---------------------+
| -1.1071487177940904 |
+---------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
