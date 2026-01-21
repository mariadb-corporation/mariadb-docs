---
description: >-
  Extract the hour. This function returns the hour portion of a time or datetime
  value as a number from 0 to 23.
---

# HOUR

## Syntax

```
HOUR(time)
```

## Description

Returns the hour for time. The range of the return value is 0 to 23 for time-of-day values. However, the range of `TIME` values actually is much larger, so HOUR can return values greater than 23.

The return value is always positive, even if a negative `TIME` value is provided.

## Examples

```sql
SELECT HOUR('10:05:03');
+------------------+
| HOUR('10:05:03') |
+------------------+
|               10 |
+------------------+

SELECT HOUR('272:59:59');
+-------------------+
| HOUR('272:59:59') |
+-------------------+
|               272 |
+-------------------+
```

## See Also

* [Date and Time Units](date-and-time-units.md)
* [Date and Time Literals](../../sql-structure/sql-language-structure/date-and-time-literals.md)
* [EXTRACT()](extract.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
