---
description: >-
  Calculate SHA-1 checksum. This function computes the SHA-1 160-bit checksum
  for a string, returning a 40-character hexadecimal string.
---

# SHA1

## Syntax

```sql
SHA1(str), SHA(str)
```

## Description

Calculates an SHA-1 160-bit checksum for the string _`str`_, as described in RFC 3174 (Secure Hash Algorithm).

The value is returned as a string of 40 hex digits, or `NULL` if the argument was NULL. The return value is a nonbinary string in the connection [character set and collation](../../../data-types/string-data-types/character-sets/), determined by the values of the [character\_set\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) and [collation\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variables.

## Examples

```sql
SELECT SHA1('some boring text');
+------------------------------------------+
| SHA1('some boring text')                 |
+------------------------------------------+
| af969fc2085b1bb6d31e517d5c456def5cdd7093 |
+------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
