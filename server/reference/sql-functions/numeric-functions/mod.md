---
description: >-
  Calculate modulo. This function returns the remainder of a number divided by
  another number.
---

# MOD

## Syntax

```bnf
MOD(N,M), N % M, N MOD M
```

## Description

Modulo operation. Returns the remainder of N divided by M. See also [Modulo Operator](../../sql-structure/operators/arithmetic-operators/modulo-operator.md).

Any number modulo zero returns `NULL`. When the [ERROR\_FOR\_DIVISION\_BY\_ZERO](../../../server-management/variables-and-modes/sql_mode.md#error_for_division_by_zero) SQL mode is enabled, as it is by default, it also produces a warning. If [strict mode](../../../server-management/variables-and-modes/sql_mode.md#strict_trans_tables) is also enabled, an `INSERT` or `UPDATE` that takes a modulo by zero fails with an error instead.

The integer part of a division can be obtained using [DIV](div.md).

## Examples

```sql
SELECT 1042 % 50;
+-----------+
| 1042 % 50 |
+-----------+
|        42 |
+-----------+

SELECT MOD(234, 10);
+--------------+
| MOD(234, 10) |
+--------------+
|            4 |
+--------------+

SELECT 253 % 7;
+---------+
| 253 % 7 |
+---------+
|       1 |
+---------+

SELECT MOD(29,9);
+-----------+
| MOD(29,9) |
+-----------+
|         2 |
+-----------+

SELECT 29 MOD 9;
+----------+
| 29 MOD 9 |
+----------+
|        2 |
+----------+
```

## See Also

* [Operator Precedence](../../sql-structure/operators/operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
