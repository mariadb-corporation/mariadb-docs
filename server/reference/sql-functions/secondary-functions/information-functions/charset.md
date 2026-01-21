---
description: >-
  Return the character set of a string. This function identifies the character
  set encoding used by the argument.
---

# CHARSET

## Syntax

```sql
CHARSET(str)
```

## Description

Returns the [character set](../../../data-types/string-data-types/character-sets/) of the string argument. If `str` is not a string, it is considered as a binary string (so the function returns 'binary'). This applies to `NULL`, too. The return value is a string in the utf8 [character set](../../../data-types/string-data-types/character-sets/).

## Examples

```sql
SELECT CHARSET('abc');
+----------------+
| CHARSET('abc') |
+----------------+
| latin1         |
+----------------+

SELECT CHARSET(CONVERT('abc' USING utf8));
+------------------------------------+
| CHARSET(CONVERT('abc' USING utf8)) |
+------------------------------------+
| utf8                               |
+------------------------------------+

SELECT CHARSET(USER());
+-----------------+
| CHARSET(USER()) |
+-----------------+
| utf8            |
+-----------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
