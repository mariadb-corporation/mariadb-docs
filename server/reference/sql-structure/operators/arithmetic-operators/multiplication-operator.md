---
description: >-
  Multiply two numbers. If integer multiplication overflows the BIGINT range,
  an error is returned.
---

# Multiplication Operator (\*)

## Syntax

```bnf
*
```

## Description

Multiplication operator.

If both operands are integers and the product is outside the [BIGINT](../../../data-types/numeric-data-types/bigint.md) range, the multiplication fails with an error. To get the exact product, make one of the operands a [DECIMAL](../../../data-types/numeric-data-types/decimal.md), for example by adding `.0` to it.

## Examples

```sql
SELECT 7*6;
+-----+
| 7*6 |
+-----+
|  42 |
+-----+

SELECT 1234567890*9876543210;
ERROR 1690 (22003): BIGINT value is out of range in '1234567890 * 9876543210'

SELECT 1234567890*9876543210.0;
+-------------------------+
| 1234567890*9876543210.0 |
+-------------------------+
|  12193263111263526900.0 |
+-------------------------+

SELECT 18014398509481984*18014398509481984.0;
+---------------------------------------+
| 18014398509481984*18014398509481984.0 |
+---------------------------------------+
|   324518553658426726783156020576256.0 |
+---------------------------------------+

SELECT 18014398509481984*18014398509481984;
ERROR 1690 (22003): BIGINT value is out of range in '18014398509481984 * 18014398509481984'
```

## See Also

* [Type Conversion](../../../sql-functions/string-functions/type-conversion.md)
* [Addition Operator (+)](addition-operator.md)
* [Subtraction Operator (-)](subtraction-operator.md)
* [Division Operator (/)](division-operator.md)
* [Operator Precedence](../operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
