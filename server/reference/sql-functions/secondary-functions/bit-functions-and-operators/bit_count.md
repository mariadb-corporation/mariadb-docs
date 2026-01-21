---
description: >-
  Count the set bits. This function returns the number of bits that are set to 1
  in the binary representation of a number.
---

# BIT\_COUNT

## Syntax

```sql
BIT_COUNT(N)
```

## Description

Returns the number of bits that are set in the argument N.

## Examples

```sql
SELECT BIT_COUNT(29), BIT_COUNT(b'101010');
+---------------+----------------------+
| BIT_COUNT(29) | BIT_COUNT(b'101010') |
+---------------+----------------------+
|             4 |                    3 |
+---------------+----------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
