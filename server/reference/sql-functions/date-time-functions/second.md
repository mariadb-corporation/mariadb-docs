---
description: >-
  Extract the second. This function returns the second portion of a time or
  datetime value as a number from 0 to 59.
---

# SECOND

## Syntax

```sql
SECOND(time)
```

## Description

Returns the second for a given `time` (which can include [microseconds](microseconds-in-mariadb.md)), in the range 0 to 59, or `NULL` if not given a valid time value.

## Examples

```sql
SELECT SECOND('10:05:03');
+--------------------+
| SECOND('10:05:03') |
+--------------------+
|                  3 |
+--------------------+

SELECT SECOND('10:05:01.999999');
+---------------------------+
| SECOND('10:05:01.999999') |
+---------------------------+
|                         1 |
+---------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
