---
description: >-
  Return the numeric value of the first character. This function returns the
  code for the leftmost character, supporting multi-byte characters.
---

# ORD

## Syntax

```sql
ORD(str)
```

## Description

If the leftmost character of the string `str` is a multi-byte character, returns the code for that character, calculated from the numeric values of its constituent bytes using this formula:

```sql
(1st byte code)
+ (2nd byte code x 256)
+ (3rd byte code x 256 x 256) ...
```

If the leftmost character is not a multi-byte character, `ORD()` returns the same value as the [ASCII()](ascii.md) function.

## Examples

```sql
SELECT ORD('2');
+----------+
| ORD('2') |
+----------+
|       50 |
+----------+
```

## See Also

* [ASCII()](ascii.md) - Return ASCII value of first character
* [CHAR()](char-function.md) - Create a character from an integer value

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
