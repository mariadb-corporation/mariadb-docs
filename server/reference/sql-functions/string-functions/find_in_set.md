---
description: >-
  Return the index of a string in a comma-separated list. This function finds
  the position of a string within a list of strings separated by commas.
---

# FIND\_IN\_SET

## Syntax

```sql
FIND_IN_SET(pattern, strlist)
```

## Description

Returns the index position where the given pattern occurs in a string list. The first argument is the pattern you want to search for. The second argument is a string containing comma-separated variables. If the second argument is of the [SET](../../data-types/string-data-types/set-data-type.md) data-type, the function is optimized to use bit arithmetic.

If the pattern does not occur in the string list or if the string list is an empty string, the function returns `0`. If either argument is `NULL`, the function returns `NULL`. The function does not return the correct result if the pattern contains a comma ("`,`") character.

## Examples

```sql
SELECT FIND_IN_SET('b','a,b,c,d') AS "Found Results";
+---------------+
| Found Results |
+---------------+
|             2 |
+---------------+
```

## See Also

* [ELT()](elt.md) function. Returns the N'th element from a set of strings.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
