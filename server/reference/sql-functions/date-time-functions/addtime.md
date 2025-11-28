---
description: >-
  Add a time value to a date or time expression. This function sums two time
  arguments, returning a new time or datetime result.
---

# ADDTIME

## Syntax

```sql
ADDTIME(expr1,expr2)
```

## Description

`ADDTIME()` adds _expr2_ to _expr1_ and returns the result. _expr1_ is a time or datetime expression, and _expr2_ is a time expression.

## Examples

```sql
SELECT ADDTIME('2007-12-31 23:59:59.999999', '1 1:1:1.000002');
+---------------------------------------------------------+
| ADDTIME('2007-12-31 23:59:59.999999', '1 1:1:1.000002') |
+---------------------------------------------------------+
| 2008-01-02 01:01:01.000001                              |
+---------------------------------------------------------+

SELECT ADDTIME('01:00:00.999999', '02:00:00.999998');
+-----------------------------------------------+
| ADDTIME('01:00:00.999999', '02:00:00.999998') |
+-----------------------------------------------+
| 03:00:01.999997                               |
+-----------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
