---
description: >-
  Subtract a time value. This function subtracts one time or datetime expression
  from another and returns the result.
---

# SUBTIME

## Syntax

```sql
SUBTIME(expr1,expr2)
```

## Description

`SUBTIME()` returns `expr1` - `expr2` expressed as a value in the same format as `expr1`. `expr1` is a time or datetime expression, and expr2 is a time expression.

## Examples

```sql
SELECT SUBTIME('2007-12-31 23:59:59.999999','1 1:1:1.000002');
+--------------------------------------------------------+
| SUBTIME('2007-12-31 23:59:59.999999','1 1:1:1.000002') |
+--------------------------------------------------------+
| 2007-12-30 22:58:58.999997                             |
+--------------------------------------------------------+

SELECT SUBTIME('01:00:00.999999', '02:00:00.999998');
+-----------------------------------------------+
| SUBTIME('01:00:00.999999', '02:00:00.999998') |
+-----------------------------------------------+
| -00:59:59.999999                              |
+-----------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
