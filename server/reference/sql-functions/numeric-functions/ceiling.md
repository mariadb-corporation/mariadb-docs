---
description: >-
  Round up to the nearest integer. This function returns the smallest integer
  value that is greater than or equal to the argument.
---

# CEILING

## Syntax

```sql
CEILING(X)
```

## Description

Returns the smallest integer value not less than X.

## Examples

```sql
SELECT CEILING(1.23);
+---------------+
| CEILING(1.23) |
+---------------+
|             2 |
+---------------+

SELECT CEILING(-1.23);
+----------------+
| CEILING(-1.23) |
+----------------+
|             -1 |
+----------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
