---
description: >-
  General introduction to numeric data types. This page summarizes the available
  integer, fixed-point, and floating-point types and their storage
  characteristics.
---

# Numeric Data Type Overview

There are a number of numeric data types:

* [BOOLEAN](boolean.md) - Synonym for TINYINT(1)
* [INT1](int1.md) - Synonym for TINYINT
* [INT2](int2.md) - Synonym for SMALLINT
* [INT3](int3.md) - Synonym for MEDIUMINT
* [INT](int.md), INTEGER
* [INT4](int4.md) - Synonym for INT
* [INT8](int8.md) - Synonym for BIGINT
* [TINYINT](tinyint.md)
* [SMALLINT](smallint.md)
* [MEDIUMINT](mediumint.md)
* [BIGINT](bigint.md)
* [DECIMAL](decimal.md), DEC, NUMERIC, FIXED
* [FLOAT](float.md)
* [DOUBLE](double.md), DOUBLE PRECISION, REAL
* [BIT](bit.md)
* [VECTOR](vector.md)

See the specific articles for detailed information on each.

## SIGNED, UNSIGNED and ZEROFILL

Most numeric types can be defined as `SIGNED`, `UNSIGNED` or `ZEROFILL`, for example:

```sql
TINYINT[(M)] [SIGNED | UNSIGNED | ZEROFILL]
```

If `SIGNED`, or no attribute, is specified, a portion of the numeric type will be reserved for the sign (plus or minus). For example, a `TINYINT SIGNED` can range from -128 to 127.

If `UNSIGNED` is specified, no portion of the numeric type is reserved for the sign, so for integer types range can be larger. For example, a `TINYINT UNSIGNED` can range from 0 to 255. Floating point and fixed-point types also can be `UNSIGNED`, but this only prevents negative values from being stored and doesn't alter the range.

If `ZEROFILL` is specified, the column will be set to `UNSIGNED` and the spaces used by default to pad the field are replaced with zeros. `ZEROFILL` is ignored in expressions or as part of a [UNION](../../sql-statements/data-manipulation/selecting-data/set-operations/union.md). `ZEROFILL` is a non-standard MySQL and MariaDB enhancement.

Note that although the preferred syntax indicates that the attributes are exclusive, more than one attribute can be specified.

Only the following combinations are supported:

* `SIGNED`
* `UNSIGNED`
* `ZEROFILL`
* `UNSIGNED ZEROFILL`
* `ZEROFILL UNSIGNED`

The latter two should be replaced with simply `ZEROFILL`, but are still accepted by the parser.

### Examples

```sql
CREATE TABLE zf (
  i1 TINYINT SIGNED,
  i2 TINYINT UNSIGNED,
  i3 TINYINT ZEROFILL
);

INSERT INTO zf VALUES (2,2,2);

SELECT * FROM zf;
+------+------+------+
| i1   | i2   | i3   |
+------+------+------+
|    2 |    2 |  002 |
+------+------+------+
```

## Range

When attempting to add a value that is out of the valid range for the numeric type, MariaDB will react depending on the [strict SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md#strict-mode) setting.

If [strict\_mode](../../../server-management/variables-and-modes/sql_mode.md#strict-mode) has been set (the default), MariaDB will return an error.

If [strict\_mode](../../../server-management/variables-and-modes/sql_mode.md#strict-mode) has not been set, MariaDB will adjust the number to fit in the field, returning a warning.

### Examples

With `strict_mode` set:

```sql
SHOW VARIABLES LIKE 'sql_mode';
+---------------+-------------------------------------------------------------------------------------------+
| Variable_name | Value                                                                                     |
+---------------+-------------------------------------------------------------------------------------------+
| sql_mode      | STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+---------------+-------------------------------------------------------------------------------------------+

CREATE TABLE ranges (i1 TINYINT, i2 SMALLINT, i3 TINYINT UNSIGNED);

INSERT INTO ranges VALUES (257,257,257);
ERROR 1264 (22003): Out of range value for column 'i1' at row 1

SELECT * FROM ranges;
Empty set (0.10 sec)
```

With `strict_mode` unset:

```sql
SHOW VARIABLES LIKE 'sql_mode%';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| sql_mode      |       |
+---------------+-------+

CREATE TABLE ranges (i1 TINYINT, i2 SMALLINT, i3 TINYINT UNSIGNED);

INSERT INTO ranges VALUES (257,257,257);
Query OK, 1 row affected, 2 warnings (0.00 sec)

SHOW WARNINGS;
+---------+------+---------------------------------------------+
| Level   | Code | Message                                     |
+---------+------+---------------------------------------------+
| Warning | 1264 | Out of range value for column 'i1' at row 1 |
| Warning | 1264 | Out of range value for column 'i3' at row 1 |
+---------+------+---------------------------------------------+
2 rows in set (0.00 sec)

SELECT * FROM ranges;
+------+------+------+
| i1   | i2   | i3   |
+------+------+------+
|  127 |  257 |  255 |
+------+------+------+
```

## AUTO\_INCREMENT

The `AUTO_INCREMENT` attribute can be used to generate a unique identity for new rows. For more details, see [auto\_increment](../auto_increment.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
