# Division Operator (/)

## Syntax

```sql
/
```

## Description

Division operator. Dividing by zero will return `NULL`. By default, returns four digits after the decimal. This is determined by the server system variable [div\_precision\_increment](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#div_precision_increment) which by default is four. It can be set from 0 to 30.

Dividing by zero returns `NULL`. If the default `ERROR_ON_DIVISION_BY_ZERO` [SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md) is used, a division by zero also produces a warning.

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
