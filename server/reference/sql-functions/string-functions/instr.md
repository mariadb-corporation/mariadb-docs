---
description: >-
  Return the position of the first occurrence of a substring. This function
  locates a substring within a string and returns its index.
---

# INSTR

## Syntax

```sql
INSTR(str,substr)
```

## Description

Returns the position of the first occurrence of substring _substr_ in string _str_. This is the same as the two-argument form of [LOCATE()](locate.md), except that the order of the arguments is reversed.

`INSTR()` performs a case-insensitive search.

If any argument is `NULL`, returns `NULL`.

## Examples

```sql
SELECT INSTR('foobarbar', 'bar');
+---------------------------+
| INSTR('foobarbar', 'bar') |
+---------------------------+
|                         4 |
+---------------------------+

SELECT INSTR('My', 'Maria');
+----------------------+
| INSTR('My', 'Maria') |
+----------------------+
|                    0 |
+----------------------+
```

## See Also

* [LOCATE()](locate.md) ; Returns the position of a string within a string
* [SUBSTRING\_INDEX()](substring_index.md) ; Returns the substring from string before count occurrences of a delimiter

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
