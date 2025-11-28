# Subtraction Operator (-)

## Syntax

```sql
-
```

## Description

Subtraction. The operator is also used as the unary minus for changing sign.

If both operands are integers, the result is calculated with [BIGINT](../../../data-types/numeric-data-types/bigint.md) precision. If either integer is unsigned, the result is also an unsigned integer, unless the `NO_UNSIGNED_SUBTRACTION` [SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md) is enabled, in which case the result is always signed.

For real or string operands, the operand with the highest precision determines the result precision.

## Examples

```sql
SELECT 96-9;
+------+
| 96-9 |
+------+
|   87 |
+------+

SELECT 15-17;
+-------+
| 15-17 |
+-------+
|    -2 |
+-------+

SELECT 3.66 + 1.333;
+--------------+
| 3.66 + 1.333 |
+--------------+
|        4.993 |
+--------------+
```

Unary minus:

```sql
SELECT - (3+5);
+---------+
| - (3+5) |
+---------+
|      -8 |
+---------+
```

## See Also

* [Type Conversion](../../../sql-functions/string-functions/type-conversion.md)
* [Addition Operator (+)](addition-operator.md)
* [Multiplication Operator (\*)](multiplication-operator.md)
* [Division Operator (/)](division-operator.md)
* [Operator Precedence](../operator-precedence.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
