---
description: >-
  Single precision floating-point number. A FLOAT column uses 4 bytes and stores
  approximate values with less precision than DOUBLE.
---

# FLOAT

## Syntax

```sql
FLOAT[(M,D)] [SIGNED | UNSIGNED | ZEROFILL]
```

## Description

A small (single-precision) floating-point number (see [DOUBLE](double.md) for a regular-size floating point number). Allowable values are:

* -3.402823466E+38 to -1.175494351E-38
* 0
* 1.175494351E-38 to 3.402823466E+38.

These are the theoretical limits, based on the IEEE standard. The actual range might be slightly smaller depending on your hardware or operating system.

M is the total number of digits and D is the number of digits following the decimal point. If M and D are omitted, values are stored to the limits allowed by the hardware. A single-precision floating-point number is accurate to approximately 7 decimal places.

`UNSIGNED`, if specified, disallows negative values.

Using `FLOAT` might give you some unexpected problems because all calculations in MariaDB are done with double precision. See [Floating Point Accuracy](floating-point-accuracy.md).

For more details on the attributes, see [Numeric Data Type Overview](numeric-data-type-overview.md).

## EXAMPLES

### SIGNED and UNSIGNED

The `FLOAT` data type may be `SIGNED` (allowing negative values) or `UNSIGNED` (not allowing negative values).

Example of `FLOAT SIGNED` (`SIGNED` is the default):

```sql
CREATE TABLE float_signed_example (
  description VARCHAR(20),
  example FLOAT,
  sz6_2 FLOAT(6,2),
  sz20_19 FLOAT(20,19) SIGNED
);
```

```sql
SET @pi = 3.1415926535897932384626433832795;

INSERT INTO float_signed_example VALUES
  ('Pi', @pi, @pi, @pi),
  ('Series', 1234.567890123, 1234.567890123, 1.234567890123),
  ('Negative', -1234.567890123, -1234.567890123, -1.234567890123),
  ('Various', 1234567890, 9999.99, 9.9999999999999999999);
```

```sql
SELECT * FROM float_signed_example;

+-------------+------------+----------+------------------------+
| description | example    | sz6_2    | sz20_19                |
+-------------+------------+----------+------------------------+
| Pi          |    3.14159 |     3.14 |  3.1415927410125732000 |
| Series      |    1234.57 |  1234.57 |  1.2345678806304932000 |
| Negative    |   -1234.57 | -1234.57 | -1.2345678806304932000 |
| Various     | 1234570000 |  9999.99 | 10.0000000000000000000 |
+-------------+------------+----------+------------------------+
```

Example of `FLOAT UNSIGNED`:

```sql
CREATE TABLE float_unsigned_example (
  description VARCHAR(20),
  example FLOAT UNSIGNED,
  sz6_2 FLOAT(6,2) UNSIGNED,
  sz20_19 FLOAT(20,19) UNSIGNED
);
```

```sql
SET @pi = 3.1415926535897932384626433832795;
```

```sql
INSERT INTO float_unsigned_example VALUES
  ('Pi', @pi, @pi, @pi),
  ('Series', 1234.567890123, 1234.567890123, 1.234567890123),
  ('Various', 1234567890, 9999.99, 9.9999999999999999999);
```

```sql
SELECT * FROM float_unsigned_example;

+-------------+------------+---------+------------------------+
| description | example    | sz6_2   | sz20_19                |
+-------------+------------+---------+------------------------+
| Pi          |    3.14159 |    3.14 |  3.1415927410125732000 |
| Series      |    1234.57 | 1234.57 |  1.2345678806304932000 |
| Various     | 1234570000 | 9999.99 | 10.0000000000000000000 |
+-------------+------------+---------+------------------------+
```

### Out of Range

A value is considered "out of range" when it is too small or too large to be stored in a data type. The size specified when creating the column is the limit for what values can be represented. The limits can also vary based on your hardware and operating system. When `SQL_MODE` is strict (the default) an out-of-range value generates an error and the operation fails. If strict mode is not in effect, the value is rounded to the nearest valid value and a warning is generated (which might be hidden, depending on your warning settings).

A value whose significant digits must be rounded to fit only generates a warning note about data truncation, since it is only an out-of-range value if the rounding causes the value to overflow. A somewhat strange exception happens when the decimal places are 16 digits or larger: at that point the value can round up to be one digit larger than you would expect to be accepted, but only for the next larger power of 10. For instance, a `FLOAT(17,16)` should max out at 9.9999999999999999, but that value rounds up to being equivalent to 10 (and 11 overflows).

```sql
TRUNCATE float_signed_example;

-- Disable strict mode
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO float_signed_example VALUES
  ('OK', 3.402823466e38, NULL, NULL),
  ('Overflow', 4.0e38, NULL, NULL),
  ('OK', -3.402823466e38, NULL, NULL),
  ('Underflow', -4.0e38, NULL, NULL),
  ('OK', NULL, 9999.99, NULL),
  ('Rounded overflow', NULL, 9999.995, NULL),
  ('Overflow', NULL, 10000, NULL),
  ('OK', NULL, -9999.99, NULL),
  ('Rounded underflow', NULL, -9999.995, NULL),
  ('Underflow', NULL, -10000, NULL),
  ('OK', NULL, NULL, 9.9999999999999999),
  ('Rounded OK', NULL, NULL, 9.99999999999999995),
  ('Overflow', NULL, NULL, 11),
  ('OK', NULL, NULL, -9.9999999999999999),
  ('Rounded OK', NULL, NULL, -9.99999999999999995),
  ('Underflow', NULL, NULL, -11);
```

```sql
Warning (sql 1264): Out of range value for column 'example' at row 2
Warning (sql 1264): Out of range value for column 'example' at row 4
Warning (sql 1264): Out of range value for column 'sz6_2' at row 6
Warning (sql 1264): Out of range value for column 'sz6_2' at row 7
Warning (sql 1264): Out of range value for column 'sz6_2' at row 9
Warning (sql 1264): Out of range value for column 'sz6_2' at row 10
Warning (sql 1264): Out of range value for column 'sz20_19' at row 13
Warning (sql 1264): Out of range value for column 'sz20_19' at row 16
```

```sql
SELECT * FROM float_signed_example;

+-------------------+-------------+----------+-------------------------+
| description       | example     | sz6_2    | sz20_19                 |
+-------------------+-------------+----------+-------------------------+
| OK                |  3.40282e38 |     NULL |                    NULL |
| Overflow          |  3.40282e38 |     NULL |                    NULL |
| OK                | -3.40282e38 |     NULL |                    NULL |
| Underflow         | -3.40282e38 |     NULL |                    NULL |
| OK                |        NULL |  9999.99 |                    NULL |
| Rounded overflow  |        NULL |  9999.99 |                    NULL |
| Overflow          |        NULL |  9999.99 |                    NULL |
| OK                |        NULL | -9999.99 |                    NULL |
| Rounded underflow |        NULL | -9999.99 |                    NULL |
| Underflow         |        NULL | -9999.99 |                    NULL |
| OK                |        NULL |     NULL |  10.0000000000000000000 |
| Rounded OK        |        NULL |     NULL |  10.0000000000000000000 |
| Overflow          |        NULL |     NULL |  10.0000000000000000000 |
| OK                |        NULL |     NULL | -10.0000000000000000000 |
| Rounded OK        |        NULL |     NULL | -10.0000000000000000000 |
| Underflow         |        NULL |     NULL | -10.0000000000000000000 |
+-------------------+-------------+----------+-------------------------+
```

```sql
TRUNCATE float_unsigned_example;

-- Disable strict mode
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO float_unsigned_example VALUES
  ('OK', 3.402823466e38, NULL, NULL),
  ('Overflow', 4.0e38, NULL, NULL),
  ('Underflow', -1, NULL, NULL);
```

```sql
Warning (sql 1264): Out of range value for column 'example' at row 2
Warning (sql 1264): Out of range value for column 'example' at row 3
```

```sql
SELECT * FROM float_unsigned_example;

+-------------+------------+-------+---------+
| description | example    | sz6_2 | sz20_19 |
+-------------+------------+-------+---------+
| OK          | 3.40282e38 |  NULL |    NULL |
| Overflow    | 3.40282e38 |  NULL |    NULL |
| Underflow   |          0 |  NULL |    NULL |
+-------------+------------+-------+---------+
```

### FLOAT ZEROFILL

A special type of `FLOAT UNSIGNED` is `FLOAT ZEROFILL`, which pads out the values with leading zeros in `SELECT` results. The number of leading zeros are just enough to pad the field out to the length of the type's field size (counting the decimal point), but the zeros are not included in an expression result or in a `UNION SELECT` column.

Using `FLOAT ZEROFILL` works the same way as `FLOAT UNSIGNED` for most operations except a simple `SELECT`. For example, with the following test table setup:

```sql
CREATE TABLE float_zerofill_example (
  description VARCHAR(20),
  example FLOAT ZEROFILL,
  sz6_2 FLOAT(6,2) ZEROFILL,
  sz20_19 FLOAT(20,19) ZEROFILL
);
```

```sql
SET @pi = 3.1415926535897932384626433832795;
```

```sql
INSERT INTO float_zerofill_example VALUES
  ('Pi', @pi, @pi, @pi),
  ('Series', 1234.567890123, 1234.567890123, 1.234567890123),
  ('Various', 1234567890, 9999.99, 9.9999999999999999999);
```

```sql
SELECT * FROM float_zerofill_example;

+-------------+--------------+---------+------------------------+
| description | example      | sz6_2   | sz20_19                |
+-------------+--------------+---------+------------------------+
| Pi          | 000003.14159 |  003.14 |  3.1415927410125732000 |
| Series      | 000001234.57 | 1234.57 |  1.2345678806304932000 |
| Various     | 001234570000 | 9999.99 | 10.0000000000000000000 |
+-------------+--------------+---------+------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
