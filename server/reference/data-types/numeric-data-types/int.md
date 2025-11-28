---
description: >-
  Standard integer type. An INT column uses 4 bytes and stores values from
  -2147483648 to 2147483647 (signed) or 0 to 4294967295 (unsigned).
---

# INT

## Syntax

```sql
INT[(M)] [SIGNED | UNSIGNED | ZEROFILL]
INTEGER[(M)] [SIGNED | UNSIGNED | ZEROFILL]
```

## Description

A normal-size integer. When marked `UNSIGNED`, it ranges from 0 to 4294967295, otherwise its range is -2147483648 to 2147483647 (`SIGNED` is the default). If a column has been set to `ZEROFILL`, all values will be prepended by zeros so that the `INT` value contains a number of M digits. `INTEGER` is a synonym for `INT`.

{% hint style="info" %}
**Note:** If the `ZEROFILL` attribute has been specified, the column will automatically become `UNSIGNED`.
{% endhint %}

`INT4` is a synonym for `INT`.

For details on the attributes, see [Numeric Data Type Overview](numeric-data-type-overview.md).

## Examples

### With [strict\_mode](../../../server-management/variables-and-modes/sql_mode.md#strict-mode) set

```sql
CREATE TABLE ints (a INT,b INT UNSIGNED,c INT ZEROFILL);
```

```sql
INSERT INTO ints VALUES (-10,-10,-10);
ERROR 1264 (22003): Out of range value for column 'b' at row 1

INSERT INTO ints VALUES (-10,10,-10);
ERROR 1264 (22003): Out of range value for column 'c' at row 1

INSERT INTO ints VALUES (-10,10,10);

INSERT INTO ints VALUES (2147483648,2147483648,2147483648);
ERROR 1264 (22003): Out of range value for column 'a' at row 1

INSERT INTO ints VALUES (2147483647,2147483648,2147483648);

SELECT * FROM ints;
+------------+------------+------------+
| a          | b          | c          |
+------------+------------+------------+
|        -10 |         10 | 0000000010 |
| 2147483647 | 2147483648 | 2147483648 |
+------------+------------+------------+
```

### SIGNED and UNSIGNED

The `INT` data type may be `SIGNED` (allowing negative values) or `UNSIGNED` (not allowing negative values).

Example of `INT SIGNED` (the default):

```sql
CREATE TABLE int_signed_example (
   description VARCHAR(20),
   example INT SIGNED
);
```

```sql
INSERT INTO int_signed_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', -2147483648),
   ('Maximum', 2147483647);
```

Example of INT UNSIGNED:

```sql
CREATE TABLE int_unsigned_example (
   description VARCHAR(20),
   example INT UNSIGNED
);
```

```sql
INSERT INTO int_unsigned_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', 0),
   ('Maximum', 4294967295);
```

### Out-of-Range

A value is considered "out-of-range" when it is too small or too large to be stored in a data type. When sql\_mode=`STRICT_TRANS_TABLES` (the default) is set, an out-of-range value generates an error. If strict mode is not in effect, the value is rounded to the nearest valid value and a warning is generated (which might be hidden, depending on your warning settings).

An example of non-strict out-of-range behavior:

```sql
TRUNCATE int_signed_example;

-- Disable strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO int_signed_example VALUES
   ('Underflow', -2147483649),
   ('Overflow', 2147483648);
```

```sql
Warning (sql 1264): Out of range value for column 'example' at row 1
Warning (sql 1264): Out of range value for column 'example' at row 2
```

```sql
SELECT * FROM int_signed_example;

+-------------+-------------+
| description | example     |
+-------------+-------------+
| Underflow   | -2147483648 |
| Overflow    |  2147483647 |
+-------------+-------------+
```

```sql
TRUNCATE int_unsigned_example;

-- Disable strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO int_unsigned_example VALUES
   ('Underflow', -1),
   ('Overflow', 4294967296);
```

```sql
Warning (sql 1264): Out of range value for column 'example' at row 1
Warning (sql 1264): Out of range value for column 'example' at row 2
```

```sql
SELECT * FROM int_unsigned_example;

+-------------+------------+
| description | example    |
+-------------+------------+
| Underflow   |          0 |
| Overflow    | 4294967295 |
+-------------+------------+
```

### INT ZEROFILL

A special type of `INT UNSIGNED` is `INT ZEROFILL`, which pads out the values with leading zeros in `SELECT` results. The number of leading zeros are just enough to pad the field out to the length of the type's maximum unsigned value, but the zeros are not included in an expression result or in a `UNION SELECT` column.

Using `INT ZEROFILL` works the same way as `INT UNSIGNED` for most operations except a simple `SELECT`. For example, with the following test table setup:

```sql
CREATE TABLE int_zerofill_example (
   description VARCHAR(20),
   example INT ZEROFILL
);
```

```sql
INSERT INTO int_zerofill_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', 0),
   ('Maximum', 4294967295);


-- Turn off strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO int_zerofill_example VALUES
   ('Underflow', -1),
   ('Overflow', 4294967296);
```

```sql
Warning (sql 1264): Out of range value for column 'example' at row 1
Warning (sql 1264): Out of range value for column 'example' at row 2
```

The resulting data would look like this:

```sql
SELECT *, example + 0 FROM int_zerofill_example;

+-------------+------------+-------------+
| description | example    | example + 0 |
+-------------+------------+-------------+
| Zero        | 0000000000 |           0 |
| Forty-Two   | 0000000042 |          42 |
| Minimum     | 0000000000 |           0 |
| Maximum     | 4294967295 |  4294967295 |
| Underflow   | 0000000000 |           0 |
| Overflow    | 4294967295 |  4294967295 |
+-------------+------------+-------------+
```

## See Also

* [Numeric Data Type Overview](numeric-data-type-overview.md)
* [TINYINT](tinyint.md)
* [SMALLINT](smallint.md)
* [MEDIUMINT](mediumint.md)
* [BIGINT](bigint.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
