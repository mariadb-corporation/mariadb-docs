---
description: >-
  Extract the month. This function returns the month portion of a date as a
  number from 1 (January) to 12 (December).
---

# MONTH

## Syntax

```sql
MONTH(date)
```

## Description

Returns the month for `date` in the range 1 to 12 for January to December, or 0 for dates such as `0000-00-00` or `2008-00-00` that have a zero month part.

## Examples

```sql
SELECT MONTH('2019-01-03');
+---------------------+
| MONTH('2019-01-03') |
+---------------------+
|                   1 |
+---------------------+

SELECT MONTH('2019-00-03');
+---------------------+
| MONTH('2019-00-03') |
+---------------------+
|                   0 |
+---------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
