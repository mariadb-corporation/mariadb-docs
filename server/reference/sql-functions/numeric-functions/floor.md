---
description: >-
  Round down to the nearest integer. This function returns the largest integer
  value that is less than or equal to the argument.
---

# FLOOR

## Syntax

```sql
FLOOR(X)
```

## Description

Returns the largest integer value not greater than X.

## Examples

```sql
SELECT FLOOR(1.23);
+-------------+
| FLOOR(1.23) |
+-------------+
|           1 |
+-------------+

SELECT FLOOR(-1.23);
+--------------+
| FLOOR(-1.23) |
+--------------+
|           -2 |
+--------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
