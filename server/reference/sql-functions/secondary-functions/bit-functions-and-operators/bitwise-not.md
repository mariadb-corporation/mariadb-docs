---
description: >-
  Invert all bits. This unary operator flips every bit in the operand, changing
  1s to 0s and 0s to 1s.
---

# \~

## Syntax

```bnf
~
```

## Description

Bitwise NOT. Converts the value to a 64-bit unsigned integer and inverts all 64 bits.

## Examples

```sql
SELECT 3 & ~1;
+--------+
| 3 & ~1 |
+--------+
|      2 |
+--------+

SELECT 5 & ~1;
+--------+
| 5 & ~1 |
+--------+
|      4 |
+--------+

SELECT ~0, HEX(~0);
+----------------------+------------------+
| ~0                   | HEX(~0)          |
+----------------------+------------------+
| 18446744073709551615 | FFFFFFFFFFFFFFFF |
+----------------------+------------------+
```

## See Also

* [Operator Precedence](../../../sql-structure/operators/operator-precedence.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
