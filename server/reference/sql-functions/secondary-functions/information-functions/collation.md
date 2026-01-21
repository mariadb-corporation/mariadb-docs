---
description: >-
  Return the collation of a string. This function outputs the name of the
  collation rule used for sorting and comparing the string argument.
---

# COLLATION

## Syntax

```sql
COLLATION(str)
```

## Description

Returns the collation of the string argument. If `str` is not a string, it is considered as a binary string (so the function returns 'binary'). This applies to `NULL`, too. The return value is a string in the utf8 [character set](../../../data-types/string-data-types/character-sets/).

See [Character Sets and Collations](../../../data-types/string-data-types/character-sets/).

## Examples

```sql
SELECT COLLATION('abc');
+-------------------+
| COLLATION('abc')  |
+-------------------+
| latin1_swedish_ci |
+-------------------+

SELECT COLLATION(_utf8'abc');
+-----------------------+
| COLLATION(_utf8'abc') |
+-----------------------+
| utf8_general_ci       |
+-----------------------+
```

## See Also

* [String literals](../../../sql-structure/sql-language-structure/string-literals.md)
* [CAST()](../../string-functions/cast.md)
* [CONVERT()](../../string-functions/convert.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
