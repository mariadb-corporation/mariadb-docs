---
description: >-
  Return the weight string. This function returns the binary string that
  represents the sorting and comparison value of the input string.
---

# WEIGHT\_STRING

## Syntax

```sql
WEIGHT_STRING(str [AS {CHAR|BINARY}(N)] [LEVEL levels] [flags])
  levels: N [ASC|DESC|REVERSE] [, N [ASC|DESC|REVERSE]] ...
```

## Description

Returns a binary string representing the string's sorting and comparison value. A string with a lower result means that for sorting purposes the string appears before a string with a higher result.

`WEIGHT_STRING()` is particularly useful when adding new collations, for testing purposes.

If `str` is a non-binary string ([CHAR](../../data-types/string-data-types/char.md), [VARCHAR](../../data-types/string-data-types/varchar.md) or [TEXT](../../data-types/string-data-types/text.md)), WEIGHT\_STRING returns the string's collation weight. If `str` is a binary string ([BINARY](../../data-types/string-data-types/binary.md), [VARBINARY](../../data-types/string-data-types/varbinary.md) or [BLOB](../../data-types/string-data-types/blob.md)), the return value is simply the input value, since the weight for each byte in a binary string is the byte value.

`WEIGHT_STRING()` returns `NULL` if given a `NULL` input.

The optional AS clause permits casting the input string to a binary or non-binary string, as well as to a particular length.

`AS BINARY(N)` measures the length in bytes rather than characters, and right pads with 0x00 bytes to the desired length.

`AS CHAR(N)` measures the length in characters, and right pads with spaces to the desired length.

N has a minimum value of 1, and if it is less than the length of the input string, the string is truncated without warning.

The optional `LEVEL` clause specifies that the return value should contain weights for specific collation levels. The `levels` specifier can either be a single integer, a comma-separated list of integers, or a range of integers separated by a dash (whitespace is ignored). Integers can range from 1 to a maximum of 6, dependent on the collation, and need to be listed in ascending order.

If the `LEVEL` clause is no provided, a default of 1 to the maximum for the collation is assumed.

If the `q` is specified without using a range, an optional modifier is permitted.

`ASC`, the default, returns the weights without any modification.

`DESC` returns bitwise-inverted weights.

`REVERSE` returns the weights in reverse order.

## Examples

The examples below use the [HEX()](hex.md) function to represent non-printable results in hexadecimal format.

```sql
SELECT HEX(WEIGHT_STRING('x'));
+-------------------------+
| HEX(WEIGHT_STRING('x')) |
+-------------------------+
| 0058                    |
+-------------------------+

SELECT HEX(WEIGHT_STRING('x' AS BINARY(4)));
+--------------------------------------+
| HEX(WEIGHT_STRING('x' AS BINARY(4))) |
+--------------------------------------+
| 78000000                             |
+--------------------------------------+

SELECT HEX(WEIGHT_STRING('x' AS CHAR(4)));
+------------------------------------+
| HEX(WEIGHT_STRING('x' AS CHAR(4))) |
+------------------------------------+
| 0058002000200020                   |
+------------------------------------+

SELECT HEX(WEIGHT_STRING(0xaa22ee LEVEL 1));
+--------------------------------------+
| HEX(WEIGHT_STRING(0xaa22ee LEVEL 1)) |
+--------------------------------------+
| AA22EE                               |
+--------------------------------------+

SELECT HEX(WEIGHT_STRING(0xaa22ee LEVEL 1 DESC));
+-------------------------------------------+
| HEX(WEIGHT_STRING(0xaa22ee LEVEL 1 DESC)) |
+-------------------------------------------+
| 55DD11                                    |
+-------------------------------------------+

SELECT HEX(WEIGHT_STRING(0xaa22ee LEVEL 1 REVERSE));
+----------------------------------------------+
| HEX(WEIGHT_STRING(0xaa22ee LEVEL 1 REVERSE)) |
+----------------------------------------------+
| EE22AA                                       |
+----------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
