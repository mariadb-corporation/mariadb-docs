---
description: >-
  Convert a string to uppercase. This function returns the string with all
  characters converted to uppercase.
---

# UPPER

## Syntax

```sql
UPPER(str)
UCASE(str)
```

## Description

Returns the string `str` with all characters changed to uppercase according to the current character set mapping. The default is latin1 (cp1252 West European).

`UCASE` is a synonym.

```sql
SELECT UPPER(surname), givenname FROM users ORDER BY surname;
+----------------+------------+
| UPPER(surname) | givenname  |
+----------------+------------+
| ABEL           | Jacinto    |
| CASTRO         | Robert     |
| COSTA          | Phestos    |
| MOSCHELLA      | Hippolytos |
+----------------+------------+
```

`UPPER()` is ineffective when applied to binary strings ([BINARY](../../data-types/string-data-types/binary.md), [VARBINARY](../../data-types/string-data-types/varbinary.md), [BLOB](../../data-types/string-data-types/blob.md)). The description of [LOWER](lower.md)() shows how to perform lettercase conversion of binary strings.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
