---
description: >-
  Convert a string to lowercase. This function returns the string with all
  characters converted to lowercase.
---

# LOWER

## Syntax

```sql
LOWER(str)
LCASE(str)
```

## Description

Returns the string `str` with all characters changed to lowercase according to the current character set mapping. The default is latin1 (cp1252 West European).

`LCASE` is a synonym for `LOWER` .

## Examples

```sql
SELECT LOWER('QUADRATICALLY');
+------------------------+
| LOWER('QUADRATICALLY') |
+------------------------+
| quadratically          |
+------------------------+
```

`LOWER()` (and [UPPER](upper.md)()) are ineffective when applied to binary strings ([BINARY](../../data-types/string-data-types/binary.md), [VARBINARY](../../data-types/string-data-types/varbinary.md), [BLOB](../../data-types/string-data-types/blob.md)).\
To perform letter case conversion, [CONVERT](convert.md) the string to a non-binary string:

```sql
SET @str = BINARY 'North Carolina';

SELECT LOWER(@str), LOWER(CONVERT(@str USING latin1));
+----------------+-----------------------------------+
| LOWER(@str)    | LOWER(CONVERT(@str USING latin1)) |
+----------------+-----------------------------------+
| North Carolina | north carolina                    |
+----------------+-----------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
