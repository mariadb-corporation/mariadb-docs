# Multiplication Operator (\*)

## Syntax

```bnf
*
```

## Description

Multiplication operator.

## Examples

```sql
SELECT 7*6;
+-----+
| 7*6 |
+-----+
|  42 |
+-----+

SELECT 1234567890*9876543210;
+-----------------------+
| 1234567890*9876543210 |
+-----------------------+
|  -6253480962446024716 |
+-----------------------+

SELECT 18014398509481984*18014398509481984.0;
+---------------------------------------+
| 18014398509481984*18014398509481984.0 |
+---------------------------------------+
|   324518553658426726783156020576256.0 |
+---------------------------------------+

SELECT 18014398509481984*18014398509481984;
+-------------------------------------+
| 18014398509481984*18014398509481984 |
+-------------------------------------+
|                                   0 |
+-------------------------------------+
```

## See Also

* [Type Conversion](../../../sql-functions/string-functions/type-conversion.md)
* [Addition Operator (+)](addition-operator.md)
* [Subtraction Operator (-)](subtraction-operator.md)
* [Division Operator (/)](division-operator.md)
* [Operator Precedence](../operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
