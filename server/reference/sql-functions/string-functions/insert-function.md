---
description: >-
  Insert a substring into a string. This function inserts a string within
  another string at a specified position and length, replacing existing
  characters.
---

# INSERT Function

## Syntax

```bnf
INSERT(str,pos,len,newstr)
```

## Description

Returns the string `str`, with the substring beginning at position `pos` and `len` characters long replaced by the string `newstr`. Returns the original string if `pos` is not within the length of the string.\
Replaces the rest of the string from position `pos` if `len` is not within the length of the rest of the string. Returns `NULL` if any argument is `NULL`.

A `len` of `0` inserts `newstr` without replacing any characters. Because a `pos` past the last character returns the original string, `INSERT()` can't append to a string; use [CONCAT()](concat.md) instead.

## Examples

```sql
SELECT INSERT('Quadratic', 3, 4, 'What');
+-----------------------------------+
| INSERT('Quadratic', 3, 4, 'What') |
+-----------------------------------+
| QuWhattic                         |
+-----------------------------------+

SELECT INSERT('Quadratic', -1, 4, 'What');
+------------------------------------+
| INSERT('Quadratic', -1, 4, 'What') |
+------------------------------------+
| Quadratic                          |
+------------------------------------+

SELECT INSERT('Quadratic', 3, 100, 'What');
+-------------------------------------+
| INSERT('Quadratic', 3, 100, 'What') |
+-------------------------------------+
| QuWhat                              |
+-------------------------------------+

SELECT INSERT('Quadratic', 3, 0, 'What');
+-----------------------------------+
| INSERT('Quadratic', 3, 0, 'What') |
+-----------------------------------+
| QuWhatadratic                     |
+-----------------------------------+

SELECT INSERT('Quadratic', 10, 0, 'What');
+------------------------------------+
| INSERT('Quadratic', 10, 0, 'What') |
+------------------------------------+
| Quadratic                          |
+------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
