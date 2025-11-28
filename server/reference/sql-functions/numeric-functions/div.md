---
description: >-
  Perform integer division. This operator divides one number by another and
  returns the integer result, discarding any remainder.
---

# DIV

## Syntax

```sql
DIV
```

## Description

Integer division. Similar to [FLOOR()](floor.md), but is safe with [BIGINT](../../data-types/numeric-data-types/bigint.md) values. Incorrect results may occur for non-integer operands that exceed the `BIGINT` range.

If the `ERROR_ON_DIVISION_BY_ZERO` [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) is used, a division by zero produces an error. Otherwise, it returns `NULL`.

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
