---
description: >-
  Shift bits to the right. This operator shifts the binary representation of a
  number to the right by a specified number of positions.
---

# >>

## Syntax

```sql
value1 >> value2
```

## Description

Converts a longlong ([BIGINT](../../../data-types/numeric-data-types/bigint.md)) number (_value1_) to binary and shifts _value2_ units to the right.

## Examples

```sql
SELECT 4 >> 2;
+--------+
| 4 >> 2 |
+--------+
|      1 |
+--------+
```

## See Also

* [Operator Precedence](../../../sql-structure/operators/operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
