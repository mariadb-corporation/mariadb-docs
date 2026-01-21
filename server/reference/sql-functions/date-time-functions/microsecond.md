---
description: >-
  Extract microseconds. This function returns the microsecond part of a time or
  datetime expression as a number from 0 to 999999.
---

# MICROSECOND

## Syntax

```sql
MICROSECOND(expr)
```

## Description

Returns the microseconds from the time or datetime expression _expr_ as a number in the range from 0 to 999999.

If _expr_ is a time with no microseconds, zero is returned, while if _expr_ is a date with no time, zero with a warning is returned.

## Examples

```sql
SELECT MICROSECOND('12:00:00.123456');
+--------------------------------+
| MICROSECOND('12:00:00.123456') |
+--------------------------------+
|                         123456 |
+--------------------------------+

SELECT MICROSECOND('2009-12-31 23:59:59.000010');
+-------------------------------------------+
| MICROSECOND('2009-12-31 23:59:59.000010') |
+-------------------------------------------+
|                                        10 |
+-------------------------------------------+

SELECT MICROSECOND('2013-08-07 12:13:14');
+------------------------------------+
| MICROSECOND('2013-08-07 12:13:14') |
+------------------------------------+
|                                  0 |
+------------------------------------+

SELECT MICROSECOND('2013-08-07');
+---------------------------+
| MICROSECOND('2013-08-07') |
+---------------------------+
|                         0 |
+---------------------------+
1 row in set, 1 warning (0.00 sec)

SHOW WARNINGS;
+---------+------+----------------------------------------------+
| Level   | Code | Message                                      |
+---------+------+----------------------------------------------+
| Warning | 1292 | Truncated incorrect time value: '2013-08-07' |
+---------+------+----------------------------------------------+
```

## See Also

* [Microseconds in MariaDB](microseconds-in-mariadb.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
