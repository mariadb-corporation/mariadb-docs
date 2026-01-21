---
description: >-
  Extract the minute. This function returns the minute portion of a time or
  datetime value as a number from 0 to 59.
---

# MINUTE

## Syntax

```sql
MINUTE(time)
```

## Description

Returns the minute for _time_, in the range 0 to 59.

## Examples

```sql
SELECT MINUTE('2013-08-03 11:04:03');
+-------------------------------+
| MINUTE('2013-08-03 11:04:03') |
+-------------------------------+
|                             4 |
+-------------------------------+

 SELECT MINUTE ('23:12:50');
+---------------------+
| MINUTE ('23:12:50') |
+---------------------+
|                  12 |
+---------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
