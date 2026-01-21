---
description: >-
  Convert hexadecimal to string. This function interprets pairs of hexadecimal
  digits as numbers and converts them to the characters they represent.
---

# UNHEX

## Syntax

```sql
UNHEX(str)
```

## Description

Performs the inverse operation of [HEX](hex.md)(str). That is, it interprets each pair of hexadecimal digits in the argument as a number and converts it to the character represented by the number. The resulting\
characters are returned as a binary string.

If `str` is `NULL`, `UNHEX()` returns `NULL`.

## Examples

```sql
SELECT HEX('MariaDB');
+----------------+
| HEX('MariaDB') |
+----------------+
| 4D617269614442 |
+----------------+

SELECT UNHEX('4D617269614442');
+-------------------------+
| UNHEX('4D617269614442') |
+-------------------------+
| MariaDB                 |
+-------------------------+

SELECT 0x4D617269614442;
+------------------+
| 0x4D617269614442 |
+------------------+
| MariaDB          |
+------------------+

SELECT UNHEX(HEX('string'));
+----------------------+
| UNHEX(HEX('string')) |
+----------------------+
| string               |
+----------------------+

SELECT HEX(UNHEX('1267'));
+--------------------+
| HEX(UNHEX('1267')) |
+--------------------+
| 1267               |
+--------------------+
```

## See Also

* [Hexadecimal literals](../../sql-structure/sql-language-structure/hexadecimal-literals.md)
* [HEX()](hex.md)
* [CONV()](../numeric-functions/conv.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
