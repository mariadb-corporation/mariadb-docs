---
description: >-
  Calculate exponential value. This function returns the value of e (the base of
  natural logarithms) raised to the power of the argument.
---

# EXP

## Syntax

```sql
EXP(X)
```

## Description

Returns the value of e (the base of natural logarithms) raised to the power of X. The inverse of this function is [LOG()](log.md) (using a single argument only) or [LN()](ln.md).

If `X` is `NULL`, this function returns `NULL`.

## Examples

```sql
SELECT EXP(2);
+------------------+
| EXP(2)           |
+------------------+
| 7.38905609893065 |
+------------------+

SELECT EXP(-2);
+--------------------+
| EXP(-2)            |
+--------------------+
| 0.1353352832366127 |
+--------------------+

SELECT EXP(0);
+--------+
| EXP(0) |
+--------+
|      1 |
+--------+

SELECT EXP(NULL);
+-----------+
| EXP(NULL) |
+-----------+
|      NULL |
+-----------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
