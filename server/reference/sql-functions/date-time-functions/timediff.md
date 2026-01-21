---
description: >-
  Subtract two time values. This function calculates the difference between two
  time or datetime expressions.
---

# TIMEDIFF

## Syntax

```sql
TIMEDIFF(expr1,expr2)
```

## Description

TIMEDIFF() returns `expr1` - `expr2` expressed as a time value. `expr1` and`expr2` are time or date-and-time expressions, but both must be of the\
same type.

## Examples

```sql
SELECT TIMEDIFF('2000:01:01 00:00:00', '2000:01:01 00:00:00.000001');
+---------------------------------------------------------------+
| TIMEDIFF('2000:01:01 00:00:00', '2000:01:01 00:00:00.000001') |
+---------------------------------------------------------------+
| -00:00:00.000001                                              |
+---------------------------------------------------------------+

SELECT TIMEDIFF('2008-12-31 23:59:59.000001', '2008-12-30 01:01:01.000002');
+----------------------------------------------------------------------+
| TIMEDIFF('2008-12-31 23:59:59.000001', '2008-12-30 01:01:01.000002') |
+----------------------------------------------------------------------+
| 46:58:57.999999                                                      |
+----------------------------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
