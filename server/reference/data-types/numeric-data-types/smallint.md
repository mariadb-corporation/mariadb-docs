---
description: >-
  Small integer type. A SMALLINT column uses 2 bytes and stores values from
  -32768 to 32767 (signed) or 0 to 65535 (unsigned).
---

# SMALLINT

## Syntax

```sql
SMALLINT[(M)] [SIGNED | UNSIGNED | ZEROFILL]
```

## Description

A small [integer](int.md). The signed range is -32768 to 32767. The unsigned range is 0 to 65535.

If a column has been set to `ZEROFILL`, all values will be prepended by zeros so that the `SMALLINT` value contains a number of M digits.

#### Note:

If the `ZEROFILL` attribute has been specified, the column will automatically become `UNSIGNED`.

`INT2` is a synonym for `SMALLINT`.

For more details on the attributes, see [Numeric Data Type Overview](numeric-data-type-overview.md).

## Examples

### With [strict\_mode](../../../server-management/variables-and-modes/sql_mode.md#strict-mode) set

```sql
CREATE TABLE smallints (a SMALLINT,b SMALLINT UNSIGNED,c SMALLINT ZEROFILL);
```

```sql
INSERT INTO smallints VALUES (-10,-10,-10);
ERROR 1264 (22003): Out of range value for column 'b' at row 1

INSERT INTO smallints VALUES (-10,10,-10);
ERROR 1264 (22003): Out of range value for column 'c' at row 1

INSERT INTO smallints VALUES (-10,10,10);

INSERT INTO smallints VALUES (32768,32768,32768);
ERROR 1264 (22003): Out of range value for column 'a' at row 1

INSERT INTO smallints VALUES (32767,32768,32768);

SELECT * FROM smallints;
+-------+-------+-------+
| a     | b     | c     |
+-------+-------+-------+
|   -10 |    10 | 00010 |
| 32767 | 32768 | 32768 |
+-------+-------+-------+
```

### SIGNED and UNSIGNED

The `SMALLINT` data type may be `SIGNED` (allowing negative values) or `UNSIGNED` (not allowing negative values).

Example of `SMALLINT SIGNED` (the default):

```sql
CREATE TABLE smallint_signed_example (
   description VARCHAR(20),
   example SMALLINT SIGNED
);
```

```sql
INSERT INTO smallint_signed_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', -32768),
   ('Maximum', 32767);
```

Example of SMALLINT UNSIGNED:

```sql
CREATE TABLE smallint_unsigned_example (
   description VARCHAR(20),
   example SMALLINT UNSIGNED
);
```

```sql
INSERT INTO smallint_unsigned_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', 0),
   ('Maximum', 65535);
```

### Out of Range

A value is considered "out of range" when it is too small or too large to be stored in a data type. When `sql_mode=STRICT_TRANS_TABLES` (the default) is set, an out-of-range value generates an error. If strict mode is not in effect, the value is rounded to the nearest valid value and a warning is generated (which might be hidden, depending on your warning settings).

An example of non-strict out-of-range behavior:

```sql
TRUNCATE smallint_signed_example;

-- Disable strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO smallint_signed_example VALUES
   ('Underflow', -32769),
   ('Overflow', 32768);
```

```sql
Warning (Code 1264): Out of range value for column 'example' at row 1
Warning (Code 1264): Out of range value for column 'example' at row 2
```

```sql
SELECT * FROM smallint_signed_example;

+-------------+---------+
| description | example |
+-------------+---------+
| Underflow   |  -32768 |
| Overflow    |   32767 |
+-------------+---------+
```

```sql
TRUNCATE smallint_unsigned_example;

-- Disable strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO smallint_unsigned_example VALUES
   ('Underflow', -1),
   ('Overflow', 65536);
```

```sql
Warning (Code 1264): Out of range value for column 'example' at row 1
Warning (Code 1264): Out of range value for column 'example' at row 2
```

```sql
SELECT * FROM smallint_unsigned_example;
```

```sql
+-------------+---------+
| description | example |
+-------------+---------+
| Underflow   |       0 |
| Overflow    |   65535 |
+-------------+---------+
```

### SMALLINT ZEROFILL

A special type of `SMALLINT UNSIGNED` is `SMALLINT ZEROFILL`, which pads out the values with leading zeros in `SELECT` results. The number of leading zeros are just enough to pad the field out to the length of the type's maximum unsigned value, but the zeros are not included in an expression result or in a `UNION SELECT` column.

Using `SMALLINT ZEROFILL` works the same way as `SMALLINT UNSIGNED` for most operations except a simple `SELECT`. For example, with the following test table setup:

```sql
CREATE TABLE smallint_zerofill_example (
   description VARCHAR(20),
   example SMALLINT ZEROFILL
);
```

```sql
INSERT INTO smallint_zerofill_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', 0),
   ('Maximum', 65535);

-- Turn off strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO smallint_zerofill_example VALUES
   ('Underflow', -1),
   ('Overflow', 65536);
```

```sql
Warning (Code 1264): Out of range value for column 'example' at row 1
Warning (Code 1264): Out of range value for column 'example' at row 2
```

The resulting data would look like this:

```sql
SELECT *, example + 0 FROM smallint_zerofill_example;
```

```sql
+-------------+---------+-------------+
| description | example | example + 0 |
+-------------+---------+-------------+
| Zero        |   00000 |           0 |
| Forty-Two   |   00042 |          42 |
| Minimum     |   00000 |           0 |
| Maximum     |   65535 |       65535 |
| Underflow   |   00000 |           0 |
| Overflow    |   65535 |       65535 |
+-------------+---------+-------------+
```

## See Also

* [Numeric Data Type Overview](numeric-data-type-overview.md)
* [TINYINT](tinyint.md)
* [MEDIUMINT](mediumint.md)
* [INTEGER](int.md)
* [BIGINT](bigint.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
