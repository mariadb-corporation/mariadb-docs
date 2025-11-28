---
description: >-
  Calculate logarithm. This function returns the natural logarithm of a number,
  or the logarithm to a specified base if two arguments are provided.
---

# LOG

## Syntax

```sql
LOG(X), LOG(B,X)
```

## Description

If called with one parameter, this function returns the natural logarithm of X. If X is less than or equal to 0, then `NULL` is returned.

If called with two parameters, it returns the logarithm of X to the base B. If B is <= 1 or X <= 0, the function returns `NULL`.

If any argument is `NULL`, the function returns `NULL`.

The inverse of this function (when called with a single argument) is the [EXP()](exp.md) function.

## Examples

LOG(X):

```sql
SELECT LOG(2);
+-------------------+
| LOG(2)            |
+-------------------+
| 0.693147180559945 |
+-------------------+

SELECT LOG(-2);
+---------+
| LOG(-2) |
+---------+
|    NULL |
+---------+
```

LOG(B,X)

```sql
SELECT LOG(2,16);
+-----------+
| LOG(2,16) |
+-----------+
|         4 |
+-----------+

SELECT LOG(3,27);
+-----------+
| LOG(3,27) |
+-----------+
|         3 |
+-----------+

SELECT LOG(3,1);
+----------+
| LOG(3,1) |
+----------+
|        0 |
+----------+

SELECT LOG(3,0);
+----------+
| LOG(3,0) |
+----------+
|     NULL |
+----------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
