---
description: >-
  Create a date from a year and day of year. This function constructs a DATE
  value given a year and the day number within that year.
---

# MAKEDATE

## Syntax

```sql
MAKEDATE(year,dayofyear)
```

## Description

Returns a date, given `year` and `day-of-year values`. `dayofyear` must be greater than 0 or the result is `NULL`.

## Examples

```sql
SELECT MAKEDATE(2011,31), MAKEDATE(2011,32);
+-------------------+-------------------+
| MAKEDATE(2011,31) | MAKEDATE(2011,32) |
+-------------------+-------------------+
| 2011-01-31        | 2011-02-01        |
+-------------------+-------------------+
```

2012 is a leap year:

```sql
SELECT MAKEDATE(2011,365), MAKEDATE(2012,365);
+--------------------+--------------------+
| MAKEDATE(2011,365) | MAKEDATE(2012,365) |
+--------------------+--------------------+
| 2011-12-31         | 2012-12-30         |
+--------------------+--------------------+

SELECT MAKEDATE(2011,366), MAKEDATE(2012,366);
+--------------------+--------------------+
| MAKEDATE(2011,366) | MAKEDATE(2012,366) |
+--------------------+--------------------+
| 2012-01-01         | 2012-12-31         |
+--------------------+--------------------+

SELECT MAKEDATE(2011,0);
+------------------+
| MAKEDATE(2011,0) |
+------------------+
| NULL             |
+------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
