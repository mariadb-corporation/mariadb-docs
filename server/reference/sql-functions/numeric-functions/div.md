---
description: >-
  Perform integer division. This operator divides one number by another and
  returns the integer result, discarding any remainder.
---

# DIV

## Syntax

```bnf
DIV
```

## Description

Integer division. The fractional part of the result is discarded, so the result is truncated toward zero. This differs from [FLOOR()](floor.md) for negative results: `-22 DIV 7` returns `-3`, while `FLOOR(-22/7)` returns `-4`. `DIV` is safe with [BIGINT](../../data-types/numeric-data-types/bigint.md) values. Incorrect results may occur for non-integer operands that exceed the `BIGINT` range.

Dividing by zero returns `NULL`. When the [ERROR\_FOR\_DIVISION\_BY\_ZERO](../../../server-management/variables-and-modes/sql_mode.md#error_for_division_by_zero) SQL mode is enabled, as it is by default, a division by zero also produces a warning. If [strict mode](../../../server-management/variables-and-modes/sql_mode.md#strict_trans_tables) is also enabled, an `INSERT` or `UPDATE` that divides by zero fails with an error instead.

The remainder of a division can be obtained using the [MOD](mod.md) operator.

## Examples

```sql
SELECT 300 DIV 7;
+-----------+
| 300 DIV 7 |
+-----------+
|        42 |
+-----------+

SELECT 300 DIV 0;
+-----------+
| 300 DIV 0 |
+-----------+
|      NULL |
+-----------+
```

## See Also

* [Division operator](../../sql-structure/operators/arithmetic-operators/division-operator.md)
* [Operator Precedence](../../sql-structure/operators/operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
