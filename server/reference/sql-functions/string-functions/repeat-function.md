---
description: >-
  Repeat a string. This function returns a string consisting of the input string
  repeated a specified number of times.
---

# REPEAT Function

## Syntax

```sql
REPEAT(str,count)
```

## Description

Returns a string consisting of the string `str` repeated `count` times. If`count` is less than 1, returns an empty string. Returns NULL if `str` or`count` are `NULL`.

## Examples

```sql
SELECT QUOTE(REPEAT('MariaDB ',4));
+------------------------------------+
| QUOTE(REPEAT('MariaDB ',4))        |
+------------------------------------+
| 'MariaDB MariaDB MariaDB MariaDB ' |
+------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
