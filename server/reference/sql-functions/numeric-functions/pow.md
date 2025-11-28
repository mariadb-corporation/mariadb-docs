---
description: >-
  Synonym for POWER(). Returns the value of a number raised to the power of
  another number.
---

# POW

## Syntax

```sql
POW(X,Y)
```

## Description

Returns the value of X raised to the power of Y.

`POWER()` is a synonym.

## Examples

```sql
SELECT POW(2,3);
+----------+
| POW(2,3) |
+----------+
|        8 |
+----------+

SELECT POW(2,-2);
+-----------+
| POW(2,-2) |
+-----------+
|      0.25 |
+-----------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
