---
description: >-
  Return the current time. This function outputs the current time of day as a
  value in 'HH:MM:SS' or HHMMSS format.
---

# CURTIME

## Syntax

```sql
CURTIME([precision])
```

## Description

Returns the current time as a value in `HH:MM:SS` or `HHMMSS.uuuuuu` format, depending on whether the function is used in a string or numeric context. The value is expressed in the current [time zone](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md).

The optional _precision_ determines the microsecond precision. See [Microseconds in MariaDB](microseconds-in-mariadb.md).

## Examples

```sql
SELECT CURTIME();
+-----------+
| CURTIME() |
+-----------+
| 12:45:39  |
+-----------+

SELECT CURTIME() + 0;
+---------------+
| CURTIME() + 0 |
+---------------+
| 124545.000000 |
+---------------+
```

With precision:

```sql
SELECT CURTIME(2);
+-------------+
| CURTIME(2)  |
+-------------+
| 09:49:08.09 |
+-------------+
```

## See Also

* [Microseconds in MariaDB](microseconds-in-mariadb.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
