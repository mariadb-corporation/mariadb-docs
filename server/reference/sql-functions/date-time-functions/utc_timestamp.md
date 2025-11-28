---
description: >-
  Return the current UTC timestamp. This function returns the current
  Coordinated Universal Time date and time.
---

# UTC\_TIMESTAMP

## Syntax

```sql
UTC_TIMESTAMP
UTC_TIMESTAMP([precision])
```

## Description

Returns the current [UTC](../../data-types/string-data-types/character-sets/internationalization-and-localization/coordinated-universal-time.md) date and time as a value in `YYYY-MM-DD HH:MM:SS` or `YYYYMMDDHHMMSS.uuuuuu` format, depending on whether the function is used in a string or numeric context.

The optional _precision_ determines the microsecond precision. See [Microseconds in MariaDB](microseconds-in-mariadb.md).

## Examples

```sql
SELECT UTC_TIMESTAMP(), UTC_TIMESTAMP() + 0;
+---------------------+-----------------------+
| UTC_TIMESTAMP()     | UTC_TIMESTAMP() + 0   |
+---------------------+-----------------------+
| 2010-03-27 17:33:16 | 20100327173316.000000 |
+---------------------+-----------------------+
```

With precision:

```sql
SELECT UTC_TIMESTAMP(4);
+--------------------------+
| UTC_TIMESTAMP(4)         |
+--------------------------+
| 2018-07-10 07:51:09.1019 |
+--------------------------+
```

## See Also

* [Time Zones](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md)
* [Microseconds in MariaDB](microseconds-in-mariadb.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
