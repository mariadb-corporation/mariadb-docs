---
description: >-
  Replace occurrences of a substring. This function replaces all instances of a
  specified search string within a string with a replacement string.
---

# REPLACE Function

## Syntax

```sql
REPLACE(str,from_str,to_str)
```

## Description

Returns the string `str` with all occurrences of the string `from_str` replaced by the string `to_str`. `REPLACE()` performs a case-sensitive match when searching for `from_str`.

## Examples

```sql
SELECT REPLACE('www.mariadb.org', 'w', 'Ww');
+---------------------------------------+
| REPLACE('www.mariadb.org', 'w', 'Ww') |
+---------------------------------------+
| WwWwWw.mariadb.org                    |
+---------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
