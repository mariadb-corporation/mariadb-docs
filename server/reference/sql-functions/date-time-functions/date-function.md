---
description: >-
  Extract the date part from a datetime expression. This function returns the
  year, month, and day portions, discarding the time component.
---

# DATE FUNCTION

## Syntax

```sql
DATE(expr)
```

## Description

Extracts the date part of the [date](../../data-types/date-and-time-data-types/date.md) or [datetime](../../data-types/date-and-time-data-types/datetime.md) expression _expr_. Returns NULL and throws a warning when passed an invalid date.

## Examples

```sql
SELECT DATE('2013-07-18 12:21:32');
+-----------------------------+
| DATE('2013-07-18 12:21:32') |
+-----------------------------+
| 2013-07-18                  |
+-----------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
