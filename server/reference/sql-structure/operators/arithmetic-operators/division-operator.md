---
description: >-
  Divide one number by another. The result keeps extra decimal places set by
  div_precision_increment, and dividing by zero returns NULL.
---

# Division Operator (/)

## Syntax

```bnf
/
```

## Description

Division operator. For exact-value operands, the scale of the result is the scale of the dividend plus the value of the [div\_precision\_increment](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#div_precision_increment) system variable, up to a maximum of 38. `div_precision_increment` is four by default, and can be set from 0 to 38. For example, `7/2` returns `3.5000`, and `1.00/3` returns `0.333333`.

Dividing by zero returns `NULL`. When the [ERROR\_FOR\_DIVISION\_BY\_ZERO](../../../../server-management/variables-and-modes/sql_mode.md#error_for_division_by_zero) SQL mode is enabled, as it is by default, a division by zero also produces a warning. If [strict mode](../../../../server-management/variables-and-modes/sql_mode.md#strict_trans_tables) is also enabled, an `INSERT` or `UPDATE` that divides by zero fails with an error instead.

## Examples

```sql
SELECT 4/5;
+--------+
| 4/5    |
+--------+
| 0.8000 |
+--------+

SELECT 300/(2-2);
+-----------+
| 300/(2-2) |
+-----------+
|      NULL |
+-----------+

SELECT 300/7;
+---------+
| 300/7   |
+---------+
| 42.8571 |
+---------+
```

Changing [div\_precision\_increment](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#div_precision_increment) for the session from the default of four to six:

```sql
SET div_precision_increment = 6;

SELECT 300/7;
+-----------+
| 300/7     |
+-----------+
| 42.857143 |
+-----------+
```

## See Also

* [Type Conversion](../../../sql-functions/string-functions/type-conversion.md)
* [Module operator (%)](modulo-operator.md)
* [Addition Operator (+)](addition-operator.md)
* [Subtraction Operator (-)](subtraction-operator.md)
* [Multiplication Operator (\*)](multiplication-operator.md)
* [truncate()](../../../sql-functions/numeric-functions/truncate.md)
* [Operator Precedence](../operator-precedence.md)
* [DIV function](../../../sql-functions/numeric-functions/div.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
