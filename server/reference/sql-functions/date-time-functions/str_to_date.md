---
description: >-
  Complete STR_TO_DATE() reference: parse strings to DATE/TIME/DATETIME, format
  specifiers (%Y %m %d %H %i %s), invalid input handling, and SQL_MODE errors.
---

# STR\_TO\_DATE

## Syntax

```sql
STR_TO_DATE(str,format)
```

## Description

This is the inverse of the [DATE\_FORMAT](date_format.md)() function. It takes a string `str` and a format string `format`. `STR_TO_DATE()` returns a`DATETIME` value if the format string contains both date and time parts, or a`DATE` or `TIME` value if the string contains only date or time parts.

The date, time, or datetime values contained in `str` should be given in the format indicated by format. If str contains an illegal date, time, or datetime value, `STR_TO_DATE()` returns `NULL`. An illegal value also produces a warning.

Under specific [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) settings an error may also be generated if the `str` isn't a valid date:

* [ALLOW\_INVALID\_DATES](../../../server-management/variables-and-modes/sql_mode.md#allow_invalid_dates)
* [NO\_ZERO\_DATE](../../../server-management/variables-and-modes/sql_mode.md#no_zero_date)
* [NO\_ZERO\_IN\_DATE](../../../server-management/variables-and-modes/sql_mode.md#no_zero_in_date)

The options that can be used by STR\_TO\_DATE(), as well as its inverse [DATE\_FORMAT()](date_format.md) and the [FROM\_UNIXTIME()](from_unixtime.md) function, are:

| Option | Description                                                                                                                                                                       |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| %a     | Short weekday name in current locale (Variable [lc\_time\_names](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names)). |
| %b     | Short form month name in current locale. For locale en\_US this is one of: Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov or Dec.                                                    |
| %c     | Month with 1 or 2 digits.                                                                                                                                                         |
| %D     | Day with English suffix 'th', 'nd', 'st' or 'rd''. (1st, 2nd, 3rd...).                                                                                                            |
| %d     | Day with 2 digits.                                                                                                                                                                |
| %e     | Day with 1 or 2 digits.                                                                                                                                                           |
| %f     | [Microseconds](microseconds-in-mariadb.md) 6 digits.                                                                                                                              |
| %H     | Hour with 2 digits between 00-23.                                                                                                                                                 |
| %h     | Hour with 2 digits between 01-12.                                                                                                                                                 |
| %I     | Hour with 2 digits between 01-12.                                                                                                                                                 |
| %i     | Minute with 2 digits.                                                                                                                                                             |
| %j     | Day of the year (001-366)                                                                                                                                                         |
| %k     | Hour with 1 digits between 0-23.                                                                                                                                                  |
| %l     | Hour with 1 digits between 1-12.                                                                                                                                                  |
| %M     | Full month name in current locale (Variable [lc\_time\_names](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names)).    |
| %m     | Month with 2 digits.                                                                                                                                                              |
| %p     | AM/PM according to current locale (Variable [lc\_time\_names](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names)).    |
| %r     | Time in 12 hour format, followed by AM/PM. Short for '%I:%i:%S %p'.                                                                                                               |
| %S     | Seconds with 2 digits.                                                                                                                                                            |
| %s     | Seconds with 2 digits.                                                                                                                                                            |
| %T     | Time in 24 hour format. Short for '%H:%i:%S'.                                                                                                                                     |
| %U     | Week number (00-53), when first day of the week is Sunday.                                                                                                                        |
| %u     | Week number (00-53), when first day of the week is Monday.                                                                                                                        |
| %V     | Week number (01-53), when first day of the week is Sunday. Used with %X.                                                                                                          |
| %v     | Week number (01-53), when first day of the week is Monday. Used with %x.                                                                                                          |
| %W     | Full weekday name in current locale (Variable [lc\_time\_names](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names)).  |
| %w     | Day of the week. 0 = Sunday, 6 = Saturday.                                                                                                                                        |
| %X     | Year with 4 digits when first day of the week is Sunday. Used with %V.                                                                                                            |
| %x     | Year with 4 digits when first day of the week is Monday. Used with %v.                                                                                                            |
| %Y     | Year with 4 digits.                                                                                                                                                               |
| %y     | Year with 2 digits.                                                                                                                                                               |
| %#     | For [str\_to\_date](str_to_date.md)(), skip all numbers.                                                                                                                          |
| %.     | For [str\_to\_date](str_to_date.md)(), skip all punctation characters.                                                                                                            |
| %@     | For [str\_to\_date](str_to_date.md)(), skip all alpha characters.                                                                                                                 |
| %%     | A literal % character.                                                                                                                                                            |

## Examples

```sql
SELECT STR_TO_DATE('Wednesday, June 2, 2014', '%W, %M %e, %Y');
+---------------------------------------------------------+
| STR_TO_DATE('Wednesday, June 2, 2014', '%W, %M %e, %Y') |
+---------------------------------------------------------+
| 2014-06-02                                              |
+---------------------------------------------------------+


SELECT STR_TO_DATE('Wednesday23423, June 2, 2014', '%W, %M %e, %Y');
+--------------------------------------------------------------+
| STR_TO_DATE('Wednesday23423, June 2, 2014', '%W, %M %e, %Y') |
+--------------------------------------------------------------+
| NULL                                                         |
+--------------------------------------------------------------+
1 row in set, 1 warning (0.00 sec)

SHOW WARNINGS;
+---------+------+-----------------------------------------------------------------------------------+
| Level   | Code | Message                                                                           |
+---------+------+-----------------------------------------------------------------------------------+
| Warning | 1411 | Incorrect datetime value: 'Wednesday23423, June 2, 2014' for function str_to_date |
+---------+------+-----------------------------------------------------------------------------------+

SELECT STR_TO_DATE('Wednesday23423, June 2, 2014', '%W%#, %M %e, %Y');
+----------------------------------------------------------------+
| STR_TO_DATE('Wednesday23423, June 2, 2014', '%W%#, %M %e, %Y') |
+----------------------------------------------------------------+
| 2014-06-02                                                     |
+----------------------------------------------------------------+
```

## See Also

* [DATE\_FORMAT()](date_format.md)
* [FROM\_UNIXTIME()](from_unixtime.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}

