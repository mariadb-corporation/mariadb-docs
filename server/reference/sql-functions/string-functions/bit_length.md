---
description: >-
  Return the length of a string in bits. This function calculates the size of
  the string in bits (length in bytes multiplied by 8).
---

# BIT\_LENGTH

## Syntax

```sql
BIT_LENGTH(str)
```

## Description

Returns the length of the given string argument in bits. If the argument is not a string, it will be converted to string. If the argument is `NULL`, it returns `NULL`.

## Examples

```sql
SELECT BIT_LENGTH('text');
+--------------------+
| BIT_LENGTH('text') |
+--------------------+
|                 32 |
+--------------------+
```

```sql
SELECT BIT_LENGTH('');
+----------------+
| BIT_LENGTH('') |
+----------------+
|              0 |
+----------------+
```

## Compatibility

PostgreSQL and Sybase support `BIT_LENGTH()`.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
