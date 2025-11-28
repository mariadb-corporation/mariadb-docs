---
description: >-
  Return a string of spaces. This function returns a string consisting of a
  specified number of space characters.
---

# SPACE

## Syntax

```sql
SPACE(N)
```

## Description

Returns a string consisting of _`N`_ space characters. If `N` is `NULL`, returns `NULL`.

## Examples

```sql
SELECT QUOTE(SPACE(6));
+-----------------+
| QUOTE(SPACE(6)) |
+-----------------+
| '      '        |
+-----------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
