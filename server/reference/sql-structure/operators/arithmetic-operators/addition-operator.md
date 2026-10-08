# Addition Operator (+)

## Syntax

```bnf
+
```

## Description

Addition.

If both operands are integers, the result is calculated with [BIGINT](../../../data-types/numeric-data-types/bigint.md) precision. If either integer is unsigned, the result is also an unsigned integer.

For real or string operands, the operand with the highest precision determines the result precision.

## Examples

```sql
SELECT 3+5;
+-----+
| 3+5 |
+-----+
|   8 |
+-----+
```

## See Also

* [Type Conversion](../../../sql-functions/string-functions/type-conversion.md)
* [Subtraction Operator (-)](subtraction-operator.md)
* [Multiplication Operator (\*)](multiplication-operator.md)
* [Division Operator (/)](division-operator.md)
* [Operator Precedence](../operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
