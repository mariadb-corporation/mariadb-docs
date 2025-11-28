---
description: >-
  Calculate MD5 checksum. This function returns the MD5 hash of a string as a
  32-character hexadecimal number.
---

# MD5

## Syntax

```sql
MD5(str)
```

## Description

Calculates an MD5 128-bit checksum for the string.

The return value is a 32-hex digit string, and a nonbinary string in the connection [character set and collation](../../../data-types/string-data-types/character-sets/), determined by the values of the [character\_set\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) and [collation\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variables.

`NULL` is returned if the argument was `NULL`.

## Examples

```sql
SELECT MD5('testing');
+----------------------------------+
| MD5('testing')                   |
+----------------------------------+
| ae2b1fca515949e5d54fb22b8ed95575 |
+----------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
