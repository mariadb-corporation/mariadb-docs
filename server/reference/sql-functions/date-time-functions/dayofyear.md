---
description: >-
  Return the day of the year. This function returns a number from 1 to 366
  indicating the day's position within the year.
---

# DAYOFYEAR

## Syntax

```sql
DAYOFYEAR(date)
```

## Description

Returns the day of the year for date, in the range 1 to 366.

## Examples

```sql
SELECT DAYOFYEAR('2018-02-16');
+-------------------------+
| DAYOFYEAR('2018-02-16') |
+-------------------------+
|                      47 |
+-------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
