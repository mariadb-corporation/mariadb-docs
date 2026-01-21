---
description: >-
  Subtract a time interval from a date. This function calculates a past date by
  subtracting a specified unit, such as days, from a starting value.
---

# DATE\_SUB

## Syntax

```sql
DATE_SUB(date,INTERVAL expr unit)
```

## Description

Performs date arithmetic. The _date_ argument specifies the starting date or datetime value. _expr_ is an expression specifying the interval value to be subtracted from the starting date. _expr_ is a string; it may start with a "`-`" for negative intervals. _unit_ is a keyword indicating the units in which the expression should be interpreted. See [Date and Time Units](date-and-time-units.md) for a complete list of permitted units.

See also [DATE\_ADD()](date_add.md).

## Examples

```sql
SELECT DATE_SUB('1998-01-02', INTERVAL 31 DAY);
+-----------------------------------------+
| DATE_SUB('1998-01-02', INTERVAL 31 DAY) |
+-----------------------------------------+
| 1997-12-02                              |
+-----------------------------------------+
```

```sql
SELECT DATE_SUB('2005-01-01 00:00:00', INTERVAL '1 1:1:1' DAY_SECOND);
+----------------------------------------------------------------+
| DATE_SUB('2005-01-01 00:00:00', INTERVAL '1 1:1:1' DAY_SECOND) |
+----------------------------------------------------------------+
| 2004-12-30 22:58:59                                            |
+----------------------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
