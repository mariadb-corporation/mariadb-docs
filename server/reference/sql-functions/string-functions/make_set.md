---
description: >-
  Return a set of comma-separated strings. This function returns a string
  consisting of substrings corresponding to the set bits in a given number.
---

# MAKE\_SET

## Syntax

```sql
MAKE_SET(bits,str1,str2,...)
```

## Description

Returns a set value (a string containing substrings separated by "," characters) consisting of the strings that have the corresponding bit in bits set. _`str1`_ corresponds to bit 0, _`str2`_ to bit 1, and so on. `NULL`\
values in _`str1`_, _`str2`_, ... are not appended to the result.

## Examples

```sql
SELECT MAKE_SET(1,'a','b','c');
+-------------------------+
| MAKE_SET(1,'a','b','c') |
+-------------------------+
| a                       |
+-------------------------+

SELECT MAKE_SET(1 | 4,'hello','nice','world');
+----------------------------------------+
| MAKE_SET(1 | 4,'hello','nice','world') |
+----------------------------------------+
| hello,world                            |
+----------------------------------------+

SELECT MAKE_SET(1 | 4,'hello','nice',NULL,'world');
+---------------------------------------------+
| MAKE_SET(1 | 4,'hello','nice',NULL,'world') |
+---------------------------------------------+
| hello                                       |
+---------------------------------------------+

SELECT QUOTE(MAKE_SET(0,'a','b','c'));
+--------------------------------+
| QUOTE(MAKE_SET(0,'a','b','c')) |
+--------------------------------+
| ''                             |
+--------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
