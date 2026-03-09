---
description: >-
  Convert a date to a day number. This function returns the number of days
  between year 0 and the given date.
---

# TO\_DAYS

## Syntax

```sql
TO_DAYS(date)
```

## Description

Given a date `date`, returns the number of days since the start of the current calendar (`0000-00-00`).

The function is not designed for use with dates before the advent of the Gregorian calendar in October 1582. Results are not reliable since it doesn't account for the lost days when the calendar changed from the Julian calendar.

This is the converse of the [FROM\_DAYS()](from_days.md) function.

## Examples

```sql
SELECT TO_DAYS('2007-10-07');
+-----------------------+
| TO_DAYS('2007-10-07') |
+-----------------------+
|                733321 |
+-----------------------+

SELECT TO_DAYS('0000-01-01');
+-----------------------+
| TO_DAYS('0000-01-01') |
+-----------------------+
|                     1 |
+-----------------------+

SELECT TO_DAYS(950501);
+-----------------+
| TO_DAYS(950501) |
+-----------------+
|          728779 |
+-----------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
