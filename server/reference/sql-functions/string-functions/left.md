---
description: >-
  Return the leftmost characters. This function returns the specified number of
  characters from the beginning (left) of a string.
---

# LEFT

## Syntax

```sql
LEFT(str,len)
```

## Description

Returns the leftmost `len` characters from the string `str`, or `NULL` if any argument is `NULL`.

## Examples

```sql
SELECT LEFT('MariaDB', 5);
+--------------------+
| LEFT('MariaDB', 5) |
+--------------------+
| Maria              |
+--------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
