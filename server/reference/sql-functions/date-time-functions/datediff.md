---
description: >-
  Complete DATEDIFF() reference: DATEDIFF(expr1,expr2) syntax, date vs datetime
  expression handling, time component ignore, and positive/negative results.
---

# DATEDIFF

## Syntax

```sql
DATEDIFF(expr1,expr2)
```

## Description

`DATEDIFF()` returns (_expr1_ – _expr2_) expressed as a value in days from one date to the other. _expr1_ and _expr2_ are date or date-and-time expressions. Only the date parts of the values are used in the calculation.

## Examples

```sql
SELECT DATEDIFF('2007-12-31 23:59:59','2007-12-30');
+----------------------------------------------+
| DATEDIFF('2007-12-31 23:59:59','2007-12-30') |
+----------------------------------------------+
|                                            1 |
+----------------------------------------------+

SELECT DATEDIFF('2010-11-30 23:59:59','2010-12-31');
+----------------------------------------------+
| DATEDIFF('2010-11-30 23:59:59','2010-12-31') |
+----------------------------------------------+
|                                          -31 |
+----------------------------------------------+
```

```sql
CREATE TABLE t1 (d DATETIME);
INSERT INTO t1 VALUES
    ("2007-01-30 21:31:07"),
    ("1983-10-15 06:42:51"),
    ("2011-04-21 12:34:56"),
    ("2011-10-30 06:31:41"),
    ("2011-01-30 14:03:25"),
    ("2004-10-07 11:19:34");
```

```sql
SELECT NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2011-05-23 10:56:05 |
+---------------------+

SELECT d, DATEDIFF(NOW(),d) FROM t1;
+---------------------+-------------------+
| d                   | DATEDIFF(NOW(),d) |
+---------------------+-------------------+
| 2007-01-30 21:31:07 |              1574 |
| 1983-10-15 06:42:51 |             10082 |
| 2011-04-21 12:34:56 |                32 |
| 2011-10-30 06:31:41 |              -160 |
| 2011-01-30 14:03:25 |               113 |
| 2004-10-07 11:19:34 |              2419 |
+---------------------+-------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
