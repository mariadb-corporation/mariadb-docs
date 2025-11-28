---
description: >-
  Format a time. This function formats a time value according to a format
  string, similar to DATE_FORMAT but for time values.
---

# TIME\_FORMAT

## Syntax

```sql
TIME_FORMAT(time,format)
```

## Description

This is used like the [DATE\_FORMAT()](date_format.md) function, but the format string may contain format specifiers only for hours, minutes, and seconds. Other specifiers produce a NULL value or 0.

## Examples

```sql
SELECT TIME_FORMAT('100:00:00', '%H %k %h %I %l');
+--------------------------------------------+
| TIME_FORMAT('100:00:00', '%H %k %h %I %l') |
+--------------------------------------------+
| 100 100 04 04 4                            |
+--------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
