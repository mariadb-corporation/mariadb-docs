---
description: >-
  Return a string representation of bits. This function generates a string based
  on the bits set in a number, using specified 'on' and 'off' strings.
---

# EXPORT\_SET

## Syntax

```sql
EXPORT_SET(bits, on, off[, separator[, number_of_bits]])
```

## Description

Takes a minimum of three arguments. Returns a string where each bit in the given `bits` argument is returned, with the string values given for `on` and `off`.

Bits are examined from right to left, (from low-order to high-order bits). Strings are added to the result from left to right, separated by a separator string (defaults as '`,`'). You can optionally limit the number of bits the `EXPORT_SET()` function examines using the `number_of_bits` option.

If any of the arguments are set as `NULL`, the function returns `NULL`.

## Examples

```sql
SELECT EXPORT_SET(5,'Y','N',',',4);
+-----------------------------+
| EXPORT_SET(5,'Y','N',',',4) |
+-----------------------------+
| Y,N,Y,N                     |
+-----------------------------+

SELECT EXPORT_SET(6,'1','0',',',10);
+------------------------------+
| EXPORT_SET(6,'1','0',',',10) |
+------------------------------+
| 0,1,1,0,0,0,0,0,0,0          |
+------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
