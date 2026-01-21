---
description: >-
  Convert a Unix timestamp to a datetime. This function formats a Unix timestamp
  as a date string or number in the current time zone.
---

# FROM\_UNIXTIME

## Syntax

```sql
FROM_UNIXTIME(unix_timestamp)
FROM_UNIXTIME(unix_timestamp,format)
```

## Description

Converts the number of seconds from the epoch (1970-01-01 00:00:00 UTC) to a`TIMESTAMP` value, the opposite of what [UNIX\_TIMESTAMP()](unix_timestamp.md) is doing. Returns NULL if the result would be outside of the valid range of `TIMESTAMP` values.

If format is given, the result is exactly equivalent to

```sql
DATE_FORMAT(FROM_UNIXTIME(unix_timestamp), format)
```

{% tabs %}
{% tab title="Current" %}
Timestamps in MariaDB have a maximum value of 4294967295, equivalent to `2106-02-07 06:28:15`. This is due to the underlying 32-bit limitation. Using the function on a timestamp beyond this will result in NULL being returned. Use [DATETIME](../../data-types/date-and-time-data-types/datetime.md) as a storage type if you require dates beyond this.
{% endtab %}

{% tab title="< 11.7" %}
The one-argument form of `FROM_UNIXTIME()` returns a`DATETIME`. This means that it can return values outside of valid `TIMESTAMP` range, in particular `1970-01-01 00:00:00`. And it can return the same result for different values of unix\_timestamp (around DST changes).

Timestamps in MariaDB have a maximum value of 4294967295, equivalent to `2106-02-07 06:28:15`. This is due to the underlying 32-bit limitation. Using the function on a timestamp beyond this will result in NULL being returned. Use [DATETIME](../../data-types/date-and-time-data-types/datetime.md) as a storage type if you require dates beyond this.
{% endtab %}

{% tab title="< 11.5" %}
The one-argument form of `FROM_UNIXTIME()` returns a`DATETIME`. This means that it can return values outside of valid `TIMESTAMP` range, in particular `1970-01-01 00:00:00`. And it can return the same result for different values of unix\_timestamp (around DST changes).

The maximum value is 2147483647, equivalent to `2038-01-19 05:14:07`.
{% endtab %}
{% endtabs %}

The following options can be used by `FROM_UNIXTIME()`, as well as [DATE\_FORMAT()](date_format.md) and [STR\_TO\_DATE()](str_to_date.md):

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
| %x     | Year with 4 digits when first day of the week is Sunday. Used with %v.                                                                                                            |
| %Y     | Year with 4 digits.                                                                                                                                                               |
| %y     | Year with 2 digits.                                                                                                                                                               |
| %#     | For [str\_to\_date](str_to_date.md)(), skip all numbers.                                                                                                                          |
| %.     | For [str\_to\_date](str_to_date.md)(), skip all punctation characters.                                                                                                            |
| %@     | For [str\_to\_date](str_to_date.md)(), skip all alpha characters.                                                                                                                 |
| %%     | A literal % character.                                                                                                                                                            |

## Performance Considerations

If your [session time zone](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#time_zone) is set to `SYSTEM` (the default), `FROM_UNIXTIME()` will call the OS function to convert the data using the system time zone. At least on Linux, the corresponding function (`localtime_r`) uses a global mutex inside glibc that can cause contention under high concurrent load.

Set your time zone to a named time zone to avoid this issue. See [mysql time zone tables](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md#mysql-time-zone-tables) for details on how to do this.

## Examples

```sql
SELECT FROM_UNIXTIME(1196440219);
+---------------------------+
| FROM_UNIXTIME(1196440219) |
+---------------------------+
| 2007-11-30 11:30:19       |
+---------------------------+

SELECT FROM_UNIXTIME(1196440219) + 0;
+-------------------------------+
| FROM_UNIXTIME(1196440219) + 0 |
+-------------------------------+
|         20071130113019.000000 |
+-------------------------------+

SELECT FROM_UNIXTIME(UNIX_TIMESTAMP(), '%Y %D %M %h:%i:%s %x');
+---------------------------------------------------------+
| FROM_UNIXTIME(UNIX_TIMESTAMP(), '%Y %D %M %h:%i:%s %x') |
+---------------------------------------------------------+
| 2010 27th March 01:03:47 2010                           |
+---------------------------------------------------------+
```

## See Also

* [UNIX\_TIMESTAMP()](unix_timestamp.md)
* [DATE\_FORMAT()](date_format.md)
* [STR\_TO\_DATE()](str_to_date.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
