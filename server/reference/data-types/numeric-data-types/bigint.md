---
description: >-
  Large integer type. A BIGINT uses 8 bytes and can store values from
  -9223372036854775808 to 9223372036854775807 (signed) or 0 to
  18446744073709551615 (unsigned).
---

# BIGINT

## Syntax

```sql
BIGINT[(M)] [SIGNED | UNSIGNED | ZEROFILL]
```

## Description

A large integer that uses 8 bytes of storage. The signed range is `-9223372036854775808` to`9223372036854775807`. The unsigned range is `0` to`18446744073709551615`.

If a column has been set to `ZEROFILL`, all values will be prepended by zeros so that the `BIGINT` value contains a number of M digits.

**Note:** If the `ZEROFILL` attribute has been specified, the column will automatically become `UNSIGNED`.

For more details on the attributes, see [Numeric Data Type Overview](numeric-data-type-overview.md).

`SERIAL` is an alias for:

```sql
BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
```

`INT8` is a synonym for `BIGINT`.

## EXAMPLES

### With [strict\_mode](../../../server-management/variables-and-modes/sql_mode.md#strict-mode) set

```sql
CREATE TABLE bigints (a BIGINT,b BIGINT UNSIGNED,c BIGINT ZEROFILL);


INSERT INTO bigints VALUES (-10,-10,-10);
ERROR 1264 (22003): Out of range value for column 'b' at row 1

INSERT INTO bigints VALUES (-10,10,-10);
ERROR 1264 (22003): Out of range value for column 'c' at row 1

INSERT INTO bigints VALUES (-10,10,10);

INSERT INTO bigints VALUES (9223372036854775808,9223372036854775808,9223372036854775808);
ERROR 1264 (22003): Out of range value for column 'a' at row 1

INSERT INTO bigints VALUES (9223372036854775807,9223372036854775808,9223372036854775808);

SELECT * FROM bigints;
+---------------------+---------------------+----------------------+
| a                   | b                   | c                    |
+---------------------+---------------------+----------------------+
|                 -10 |                  10 | 00000000000000000010 |
| 9223372036854775807 | 9223372036854775808 | 09223372036854775808 |
+---------------------+---------------------+----------------------+
```

### SIGNED and UNSIGNED

The `BIGINT` data type may be `SIGNED` (allowing negative values) or `UNSIGNED` (not allowing negative values).

Example of `BIGINT SIGNED` (the default):

```sql
CREATE TABLE bigint_signed_example (
   description VARCHAR(20),
   example BIGINT SIGNED
);
```

```sql
INSERT INTO bigint_signed_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', -9223372036854775808),
   ('Maximum', 9223372036854775807);
```

Example of BIGINT UNSIGNED:

```sql
CREATE TABLE bigint_unsigned_example (
   description VARCHAR(20),
   example BIGINT UNSIGNED
);
```

```sql
INSERT INTO bigint_unsigned_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', 0),
   ('Maximum', 18446744073709551615);
```

### Out of Range

A value is considered "out of range" when it is too small or too large to be stored in a data type. When `sql_mode=STRICT_TRANS_TABLES` (the default) is set, an out-of-range value generates an error. If strict mode is not in effect, the value is rounded to the nearest valid value and a warning is generated (which might be hidden, depending on your warning settings).

An example of non-strict out-of-range behavior:

```sql
TRUNCATE bigint_signed_example;

-- Disable strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO bigint_signed_example VALUES
   ('Underflow', -9223372036854775809),
   ('Overflow', 9223372036854775808);

Warning (Code 1264): Out of range value for column 'example' at row 1
Warning (Code 1264): Out of range value for column 'example' at row 2

SELECT * FROM bigint_signed_example;

+-------------+----------------------+
| description | example              |
+-------------+----------------------+
| Underflow   | -9223372036854775808 |
| Overflow    |  9223372036854775807 |
+-------------+----------------------+

TRUNCATE bigint_unsigned_example;

-- Disable strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO bigint_unsigned_example VALUES
   ('Underflow', -1),
   ('Overflow', 18446744073709551616);

Warning (Code 1264): Out of range value for column 'example' at row 1
Warning (Code 1264): Out of range value for column 'example' at row 2

SELECT * FROM bigint_unsigned_example;

+-------------+----------------------+
| description | example              |
+-------------+----------------------+
| Underflow   |                    0 |
| Overflow    | 18446744073709551615 |
+-------------+----------------------+
```

### BIGINT ZEROFILL

A special type of `BIGINT UNSIGNED is BIGINT ZEROFILL`, which pads out the values with leading zeros in `SELECT` results. The number of leading zeros are just enough to pad the field out to the length of the type's maximum unsigned value, but the zeros are not included in an expression result or in a `UNION SELECT` column.

Using `BIGINT ZEROFILL` works the same way as `BIGINT UNSIGNED` for most operations except a simple `SELECT`. For example, with the following test table setup:

```sql
CREATE TABLE bigint_zerofill_example (
   description VARCHAR(20),
   example BIGINT ZEROFILL
);

INSERT INTO bigint_zerofill_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', 0),
   ('Maximum', 18446744073709551615);

-- Turn off strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO bigint_zerofill_example VALUES
   ('Underflow', -1),
   ('Overflow', 18446744073709551616);

Warning (Code 1264): Out of range value for column 'example' at row 1
Warning (Code 1264): Out of range value for column 'example' at row 2
```

The resulting data would look like this:

```sql
SELECT *, example + 0 FROM bigint_zerofill_example;

+-------------+----------------------+----------------------+
| description | example              | example + 0          |
+-------------+----------------------+----------------------+
| Zero        | 00000000000000000000 |                    0 |
| Forty-Two   | 00000000000000000042 |                   42 |
| Minimum     | 00000000000000000000 |                    0 |
| Maximum     | 18446744073709551615 | 18446744073709551615 |
| Underflow   | 00000000000000000000 |                    0 |
| Overflow    | 18446744073709551615 | 18446744073709551615 |
+-------------+----------------------+----------------------+
```

## See Also

* [Numeric Data Type Overview](numeric-data-type-overview.md)
* [TINYINT](tinyint.md)
* [SMALLINT](smallint.md)
* [MEDIUMINT](mediumint.md)
* [INTEGER](int.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
