---
description: >-
  Return the character for a specific ASCII value. This function is similar to
  CHAR() but accepts a single integer argument.
---

# CHR

## Syntax

```sql
CHR(N)
```

## Description

`CHR()` interprets each argument N as an integer and returns a [VARCHAR(1)](../../data-types/string-data-types/varchar.md) string consisting of the character given by the code values of the integer. The character set and collation of the string are set according to the values of the [character\_set\_database](../../system-tables/information-schema/information-schema-tables/information-schema-character_sets-table.md) and [collation\_database](../../system-tables/information-schema/information-schema-tables/information-schema-collations-table.md) system variables.

`CHR()` is similar to the [CHAR()](char-function.md) function, but only accepts a single argument.

`CHR()` is available in all [sql\_modes](../../../server-management/variables-and-modes/sql_mode.md).

## Examples

```sql
SELECT CHR(67);
+---------+
| CHR(67) |
+---------+
| C       |
+---------+

SELECT CHR('67');
+-----------+
| CHR('67') |
+-----------+
| C         |
+-----------+

SELECT CHR('C');
+----------+
| CHR('C') |
+----------+
|          |
+----------+
1 row in set, 1 warning (0.000 sec)

SHOW WARNINGS;
+---------+------+----------------------------------------+
| Level   | Code | Message                                |
+---------+------+----------------------------------------+
| Warning | 1292 | Truncated incorrect INTEGER value: 'C' |
+---------+------+----------------------------------------+
```

## See Also

* [Character Sets and Collations](../../data-types/string-data-types/character-sets/)
* [ASCII()](ascii.md) - Return ASCII value of first character
* [ORD()](ord.md) - Return value for character in single or multi-byte character sets
* [CHAR()](char-function.md) - Similar function which accepts multiple integers

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
