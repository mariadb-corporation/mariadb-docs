---
description: >-
  Cast a string to a binary string. This operator converts a character string to
  a binary string, often used for case-sensitive comparisons.
---

# BINARY Operator

This page describes the BINARY operator. For details about the data type, see [Binary Data Type](../../data-types/string-data-types/binary.md).

## Syntax

```sql
BINARY
```

## Description

The `BINARY` operator casts the string following it to a binary string. This is an easy way to force a column comparison to be done byte by byte rather than character by character. This causes the comparison to be case sensitive even if the column isn't defined as [BINARY](../../data-types/string-data-types/binary.md) or [BLOB](../../data-types/string-data-types/blob.md).

`BINARY` also causes trailing spaces to be significant.

## Examples

```sql
SELECT 'a' = 'A';
+-----------+
| 'a' = 'A' |
+-----------+
|         1 |
+-----------+

SELECT BINARY 'a' = 'A';
+------------------+
| BINARY 'a' = 'A' |
+------------------+
|                0 |
+------------------+

SELECT 'a' = 'a ';
+------------+
| 'a' = 'a ' |
+------------+
|          1 |
+------------+

SELECT BINARY 'a' = 'a ';
+-------------------+
| BINARY 'a' = 'a ' |
+-------------------+
|                 0 |
+-------------------+
```

## See Also

* [Operator Precedence](../../sql-structure/operators/operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
