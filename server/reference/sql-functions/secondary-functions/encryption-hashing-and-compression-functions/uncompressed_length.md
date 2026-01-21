---
description: >-
  Return length of uncompressed string. This function returns the length of a
  compressed string before it was compressed.
---

# UNCOMPRESSED\_LENGTH

## Syntax

```sql
UNCOMPRESSED_LENGTH(compressed_string)
```

## Description

Returns the length that the compressed string had before being compressed with [COMPRESS()](compress.md).

`UNCOMPRESSED_LENGTH()` returns `NULL` or an incorrect result if the string is not compressed.

Returns `MYSQL_TYPE_LONG`, or [int(10)](../../../data-types/numeric-data-types/int.md), if the result fits within 32-bits.

## Examples

```sql
SELECT UNCOMPRESSED_LENGTH(COMPRESS(REPEAT('a',30)));
+-----------------------------------------------+
| UNCOMPRESSED_LENGTH(COMPRESS(REPEAT('a',30))) |
+-----------------------------------------------+
|                                            30 |
+-----------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
