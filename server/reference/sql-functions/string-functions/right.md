---
description: >-
  Return the rightmost characters. This function returns the specified number of
  characters from the end (right) of a string.
---

# RIGHT

## Syntax

```sql
RIGHT(str,len)
```

## Description

Returns the rightmost _`len`_ characters from the string _`str`_, or `NULL` if any argument is `NULL`.

## Examples

```sql
SELECT RIGHT('MariaDB', 2);
+---------------------+
| RIGHT('MariaDB', 2) |
+---------------------+
| DB                  |
+---------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
