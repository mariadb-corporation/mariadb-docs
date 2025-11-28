---
description: >-
  Return the current UTC date. This function returns the current Coordinated
  Universal Time date in 'YYYY-MM-DD' or YYYYMMDD format.
---

# UTC\_DATE

## Syntax

```sql
UTC_DATE, UTC_DATE()
```

## Description

Returns the current [UTC date](../../data-types/string-data-types/character-sets/internationalization-and-localization/coordinated-universal-time.md) as a value in `YYYY-MM-DD` or `YYYYMMDD` format, depending on whether the function is used in a string or numeric context.

## Examples

```sql
SELECT UTC_DATE(), UTC_DATE() + 0;
+------------+----------------+
| UTC_DATE() | UTC_DATE() + 0 |
+------------+----------------+
| 2010-03-27 |       20100327 |
+------------+----------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
