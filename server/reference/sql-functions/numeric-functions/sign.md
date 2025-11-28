---
description: >-
  Return the sign of a number. This function returns -1, 0, or 1 depending on
  whether the argument is negative, zero, or positive.
---

# SIGN

## Syntax

```sql
SIGN(X)
```

## Description

Returns the sign of the argument as -1, 0, or 1, depending on whether X is negative, zero, or positive.

## Examples

```sql
SELECT SIGN(-32);
+-----------+
| SIGN(-32) |
+-----------+
|        -1 |
+-----------+

SELECT SIGN(0);
+---------+
| SIGN(0) |
+---------+
|       0 |
+---------+

SELECT SIGN(234);
+-----------+
| SIGN(234) |
+-----------+
|         1 |
+-----------+
```

## See Also

* [ABS()](abs.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
