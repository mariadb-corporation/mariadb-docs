---
description: >-
  Return the binary representation of a number. This function converts a number
  to its binary string equivalent.
---

# BIN

## Syntax

```sql
BIN(N)
```

## Description

Returns a string representation of the binary value of the given longlong (that is, [BIGINT](../../data-types/numeric-data-types/bigint.md)) number. This is equivalent to [CONV(N,10,2)](../numeric-functions/conv.md). The argument should be positive. If it is a `FLOAT`, it will be truncated. Returns `NULL` if the argument is `NULL`.

## Examples

```sql
SELECT BIN(12);
+---------+
| BIN(12) |
+---------+
| 1100    |
+---------+
```

## See Also

* [Binary literals](../../sql-structure/sql-language-structure/binary-literals.md)
* [CONV()](../numeric-functions/conv.md)
* [OCT()](../numeric-functions/oct.md)
* [HEX()](hex.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
