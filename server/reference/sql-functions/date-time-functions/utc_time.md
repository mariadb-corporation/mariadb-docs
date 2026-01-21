---
description: >-
  Return the current UTC time. This function returns the current Coordinated
  Universal Time in 'HH:MM:SS' or HHMMSS format.
---

# UTC\_TIME

## Syntax

```sql
UTC_TIME
UTC_TIME([precision])
```

## Description

Returns the current [UTC time](../../data-types/string-data-types/character-sets/internationalization-and-localization/coordinated-universal-time.md) as a value in `HH:MM:SS` or `HHMMSS.uuuuuu` format, depending on whether the function is used in a string or numeric context.

The optional _precision_ determines the microsecond precision. See [Microseconds in MariaDB](microseconds-in-mariadb.md).

## Examples

```sql
SELECT UTC_TIME(), UTC_TIME() + 0;
+------------+----------------+
| UTC_TIME() | UTC_TIME() + 0 |
+------------+----------------+
| 17:32:34   |  173234.000000 |
+------------+----------------+
```

With precision:

```sql
SELECT UTC_TIME(5);
+----------------+
| UTC_TIME(5)    |
+----------------+
| 07:52:50.78369 |
+----------------+
```

## See Also

* [Microseconds in MariaDB](microseconds-in-mariadb.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
