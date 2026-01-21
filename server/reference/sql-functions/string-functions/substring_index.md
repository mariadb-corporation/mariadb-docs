---
description: >-
  Return a substring before a delimiter. This function returns the substring
  from a string before a specified number of occurrences of a delimiter.
---

# SUBSTRING\_INDEX

## Syntax

```sql
SUBSTRING_INDEX(str,delim,count)
```

## Description

Returns the substring from string _`str`_ before count occurrences of the delimiter _`delim`_. If _`count`_ is positive, everything to the left of the final delimiter (counting from the left) is returned. If _`count`_ is negative, everything to the right of the final delimiter (counting from the right) is returned. `SUBSTRING_INDEX()` performs a case-sensitive match when searching for _`delim`_.

If any argument is `NULL`, returns `NULL`.

For example:

```sql
SUBSTRING_INDEX('www.mariadb.org', '.', 2)
```

It means "Return all of the characters up to the 2nd occurrence of ."

## Examples

```sql
SELECT SUBSTRING_INDEX('www.mariadb.org', '.', 2);
+--------------------------------------------+
| SUBSTRING_INDEX('www.mariadb.org', '.', 2) |
+--------------------------------------------+
| www.mariadb                                |
+--------------------------------------------+

SELECT SUBSTRING_INDEX('www.mariadb.org', '.', -2);
+---------------------------------------------+
| SUBSTRING_INDEX('www.mariadb.org', '.', -2) |
+---------------------------------------------+
| mariadb.org                                 |
+---------------------------------------------+
```

## See Also

* [INSTR()](instr.md) - Returns the position of a string within a string
* [LOCATE()](locate.md) - Returns the position of a string within a string
* [SUBSTRING()](substring.md) - Returns a string based on position

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
