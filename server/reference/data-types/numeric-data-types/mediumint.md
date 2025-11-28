---
description: >-
  Medium-sized integer. A MEDIUMINT column uses 3 bytes and stores values from
  -8388608 to 8388607 (signed) or 0 to 16777215 (unsigned).
---

# MEDIUMINT

## Syntax

```sql
MEDIUMINT[(M)] [SIGNED | UNSIGNED | ZEROFILL]
```

## Description

A medium-sized integer. The signed range is -8388608 to 8388607. The unsigned range is 0 to 16777215.

`ZEROFILL` pads the integer with zeroes and assumes `UNSIGNED` (even if `UNSIGNED` is not specified).

`INT3` is a synonym for `MEDIUMINT`.

For details on the attributes, see [Numeric Data Type Overview](numeric-data-type-overview.md).

## Examples

### With [strict\_mode](../../../server-management/variables-and-modes/sql_mode.md#strict-mode) set

```sql
CREATE TABLE mediumints (a MEDIUMINT,b MEDIUMINT UNSIGNED,c MEDIUMINT ZEROFILL);

DESCRIBE mediumints;
+-------+--------------------------------+------+-----+---------+-------+
| Field | Type                           | Null | Key | Default | Extra |
+-------+--------------------------------+------+-----+---------+-------+
| a     | mediumint(9)                   | YES  |     | NULL    |       |
| b     | mediumint(8) unsigned          | YES  |     | NULL    |       |
| c     | mediumint(8) unsigned zerofill | YES  |     | NULL    |       |
+-------+--------------------------------+------+-----+---------+-------+
```

```sql
INSERT INTO mediumints VALUES (-10,-10,-10);
ERROR 1264 (22003): Out of range value for column 'b' at row 1

INSERT INTO mediumints VALUES (-10,10,-10);
ERROR 1264 (22003): Out of range value for column 'c' at row 1

INSERT INTO mediumints VALUES (-10,10,10);

INSERT INTO mediumints VALUES (8388608,8388608,8388608);
ERROR 1264 (22003): Out of range value for column 'a' at row 1

INSERT INTO mediumints VALUES (8388607,8388608,8388608);

SELECT * FROM mediumints;
+---------+---------+----------+
| a       | b       | c        |
+---------+---------+----------+
|     -10 |      10 | 00000010 |
| 8388607 | 8388608 | 08388608 |
+---------+---------+----------+
```

### SIGNED and UNSIGNED

The `MEDIUMINT` data type may be `SIGNED` (allowing negative values) or `UNSIGNED` (not allowing negative values).

Example of `MEDIUMINT` `SIGNED` (the default):

```sql
CREATE TABLE mediumint_signed_example (
   description VARCHAR(20),
   example MEDIUMINT SIGNED
);
```

```sql
INSERT INTO mediumint_signed_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', -8388608),
   ('Maximum', 8388607);
```

Example of `MEDIUMINT` `UNSIGNED`:

```sql
CREATE TABLE mediumint_unsigned_example (
   description VARCHAR(20),
   example MEDIUMINT UNSIGNED
);
```

```sql
INSERT INTO mediumint_unsigned_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', 0),
   ('Maximum', 16777215);
```

### Out of Range

A value is considered "out of range" when it is too small or too large to be stored in a data type. When `sql_mode=STRICT_TRANS_TABLES` (the default) is set, an out-of-range value generates an error. If strict mode is not in effect, the value is rounded to the nearest valid value and a warning is generated (which might be hidden, depending on your warning settings).

An example of non-strict out-of-range behavior:

```sql
TRUNCATE mediumint_signed_example;
```

```sql
-- Disable strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));
```

```sql
INSERT INTO mediumint_signed_example VALUES
   ('Underflow', -8388609),
   ('Overflow', 8388608);
```

```sql
Warning (sql 1264): Out of range value for column 'example' at row 1
Warning (sql 1264): Out of range value for column 'example' at row 2
```

```sql
SELECT * FROM mediumint_signed_example;
```

```sql
+-------------+----------+
| description | example  |
+-------------+----------+
| Underflow   | -8388608 |
| Overflow    |  8388607 |
+-------------+----------+
```

```sql
TRUNCATE mediumint_unsigned_example;
```

```sql
-- Disable strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));
```

```sql
INSERT INTO mediumint_unsigned_example VALUES
   ('Underflow', -1),
   ('Overflow', 16777216);
```

```sql
Warning (sql 1264): Out of range value for column 'example' at row 1
Warning (sql 1264): Out of range value for column 'example' at row 2
```

```sql
SELECT * FROM mediumint_unsigned_example;
```

```sql
+-------------+----------+
| description | example  |
+-------------+----------+
| Underflow   |        0 |
| Overflow    | 16777215 |
+-------------+----------+
```

### MEDIUMINT ZEROFILL

A special type of `MEDIUMINT UNSIGNED` is `MEDIUMINT ZEROFILL`, which pads out the values with leading zeros in `SELECT` results. The number of leading zeros are just enough to pad the field out to the length of the type's maximum unsigned value, but the zeros are not included in an expression result or in a `UNION SELECT` column.

Using `MEDIUMINT ZEROFILL` works the same way as `MEDIUMINT UNSIGNED` for most operations except a simple `SELECT`. For example, with the following test table setup:

```sql
CREATE TABLE mediumint_zerofill_example (
   description VARCHAR(20),
   example MEDIUMINT ZEROFILL
);
```

```sql
INSERT INTO mediumint_zerofill_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', 0),
   ('Maximum', 16777215);
```

```sql
-- Turn off strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));
```

```sql
INSERT INTO mediumint_zerofill_example VALUES
   ('Underflow', -1),
   ('Overflow', 16777216);
```

```sql
Warning (sql 1264): Out of range value for column 'example' at row 1
Warning (sql 1264): Out of range value for column 'example' at row 2
```

The resulting data would look like this:

```sql
SELECT *, example + 0 FROM mediumint_zerofill_example;
```

```sql
+-------------+----------+-------------+
| description | example  | example + 0 |
+-------------+----------+-------------+
| Zero        | 00000000 |           0 |
| Forty-Two   | 00000042 |          42 |
| Minimum     | 00000000 |           0 |
| Maximum     | 16777215 |    16777215 |
| Underflow   | 00000000 |           0 |
| Overflow    | 16777215 |    16777215 |
+-------------+----------+-------------+
```

## See Also

* [Numeric Data Type Overview](numeric-data-type-overview.md)
* [TINYINT](tinyint.md)
* [SMALLINT](smallint.md)
* [INTEGER](int.md)
* [BIGINT](bigint.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
