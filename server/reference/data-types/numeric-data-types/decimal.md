---
description: >-
  Exact fixed-point number. DECIMAL(M,D) stores values with M total digits and D
  decimal places, preventing rounding errors common with floating-point types.
---

# DECIMAL

## Syntax

```sql
DECIMAL[(M[,D])] [SIGNED | UNSIGNED | ZEROFILL]
```

## Description

A packed "exact" fixed-point number. `M` is the total number of digits (the precision), and `D` is the number of digits after the decimal point (the scale).

* The decimal point and (for negative numbers) the "-" sign are not counted in `M`.
* If `D` is `0`, values have no decimal point or fractional part, and on [INSERT](../../sql-statements/data-manipulation/inserting-loading-data/insert.md), the value will be rounded to the nearest `DECIMAL`.
* The maximum number of digits (`M`) for `DECIMAL` is 65.
* The maximum number of supported decimals (`D`) is `30` before [MariadB 10.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1021-release-notes) and `38` afterwards.
* If `D` is omitted, the default is `0`. If `M` is omitted, the default is `10`.

`UNSIGNED`, if specified, disallows negative values.

`ZEROFILL`, if specified, pads the number with zeros, up to the total number of digits specified by `M`.

All basic calculations (+, -, \*, /) with `DECIMAL` columns are done with a precision of 65 digits.

For more details on the attributes, see [Numeric Data Type Overview](numeric-data-type-overview.md).

`DEC`, `NUMERIC`, and `FIXED` are synonyms, as well as `NUMBER` in [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle).

## Examples

```sql
CREATE TABLE t1 (d DECIMAL UNSIGNED ZEROFILL);

INSERT INTO t1 VALUES (1),(2),(3),(4.0),(5.2),(5.7);
Query OK, 6 rows affected, 2 warnings (0.16 sec)
Records: 6  Duplicates: 0  Warnings: 2

Note (sql 1265): Data truncated for column 'd' at row 5
Note (sql 1265): Data truncated for column 'd' at row 6

SELECT * FROM t1;
+------------+
| d          |
+------------+
| 0000000001 |
| 0000000002 |
| 0000000003 |
| 0000000004 |
| 0000000005 |
| 0000000006 |
+------------+
```

### With [strict\_mode](../../../server-management/variables-and-modes/sql_mode.md#strict-mode) set

```sql
INSERT INTO t1 VALUES (-7);
ERROR 1264 (22003): Out of range value for column 'd' at row 1
```

### SIGNED and UNSIGNED

The `DECIMAL` data type may be `SIGNED` (allowing negative values) or `UNSIGNED` (not allowing negative values).

Example of `DECIMAL SIGNED` (`SIGNED` is the default):

```sql
CREATE TABLE decimal_signed_example (
  description VARCHAR(20),
  sz10_0 DECIMAL,
  sz6_2 DECIMAL(6,2),
  sz20_19 DECIMAL(20,19) SIGNED
);
```

```sql
SET @pi = 3.1415926535897932384626433832795;
```

```sql
INSERT INTO decimal_signed_example VALUES
  ('Pi', @pi, @pi, @pi),
  ('Series', 1234.567890123, 1234.567890123, 1.234567890123),
  ('Negative', -1234.567890123, -1234.567890123, -1.234567890123),
  ('Various', 1234567890, 9999.99, 9.9999999999999999999);
```

```sql
SELECT * FROM decimal_signed_example;

+-------------+------------+----------+------------------------+
| description | sz10_0     | sz6_2    | sz20_19                |
+-------------+------------+----------+------------------------+
| Pi          |          3 |     3.14 |  3.1415926535897932385 |
| Series      |       1235 |  1234.57 |  1.2345678901230000000 |
| Negative    |      -1235 | -1234.57 | -1.2345678901230000000 |
| Various     | 1234567890 |  9999.99 |  9.9999999999999999999 |
+-------------+------------+----------+------------------------+
```

Example of `DECIMAL UNSIGNED`:

```sql
CREATE TABLE decimal_unsigned_example (
  description VARCHAR(20),
  sz10_0 DECIMAL UNSIGNED,
  sz6_2 DECIMAL(6,2) UNSIGNED,
  sz20_19 DECIMAL(20,19) UNSIGNED
);
```

```sql
SET @pi = 3.1415926535897932384626433832795;
```

```sql
INSERT INTO decimal_unsigned_example VALUES
  ('Pi', @pi, @pi, @pi),
  ('Series', 1234.567890123, 1234.567890123, 1.234567890123),
  ('Various', 1234567890, 9999.99, 9.9999999999999999999);
```

```sql
SELECT * FROM decimal_unsigned_example;

+-------------+------------+---------+-----------------------+
| description | sz10_0     | sz6_2   | sz20_19               |
+-------------+------------+---------+-----------------------+
| Pi          |          3 |    3.14 | 3.1415926535897932385 |
| Series      |       1235 | 1234.57 | 1.2345678901230000000 |
| Various     | 1234567890 | 9999.99 | 9.9999999999999999999 |
+-------------+------------+---------+-----------------------+
```

### Out of Range

A value is considered "out of range" when it is too small or too large to be stored in a data type. The size specified when creating the column is the strict limit for what values can be represented. When `SQL_MODE` is strict (the default), an out-of-range value generates an error, and the operation fails. If strict mode is not in effect, the value is rounded to the nearest valid value, and a warning is generated (which might be hidden, depending on your warning settings).

A value whose significant digits must be rounded to fit only generates a warning note about data truncation, since it is only an out-of-range value if the rounding causes the value to overflow.

```sql
TRUNCATE decimal_signed_example;

-- Disable strict mode
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO decimal_signed_example VALUES
  ('OK', 9999999999.4, NULL, NULL),
  ('Rounded overflow', 9999999999.5, NULL, NULL),
  ('Overflow', 10000000000, NULL, NULL),
  ('OK', -9999999999.4, NULL, NULL),
  ('Rounded underflow', -9999999999.5, NULL, NULL),
  ('Underflow', -10000000000, NULL, NULL),
  ('OK', NULL, 9999.994, NULL),
  ('Rounded overflow', NULL, 9999.995, NULL),
  ('Overflow', NULL, 10000, NULL),
  ('OK', NULL, -9999.994, NULL),
  ('Rounded underflow', NULL, -9999.995, NULL),
  ('Underflow', NULL, -10000, NULL),
  ('OK', NULL, NULL, 9.99999999999999999994),
  ('Rounded overflow', NULL, NULL, 9.99999999999999999995),
  ('Overflow', NULL, NULL, 10),
  ('OK', NULL, NULL, -9.99999999999999999994),
  ('Rounded underflow', NULL, NULL, -9.99999999999999999995),
  ('Underflow', NULL, NULL, -10);
```

```sql
Note (sql 1265): Data truncated for column 'sz10_0' at row 1
Warning (sql 1264): Out of range value for column 'sz10_0' at row 2
Warning (sql 1264): Out of range value for column 'sz10_0' at row 3
Note (sql 1265): Data truncated for column 'sz10_0' at row 4
Warning (sql 1264): Out of range value for column 'sz10_0' at row 5
Warning (sql 1264): Out of range value for column 'sz10_0' at row 6
Note (sql 1265): Data truncated for column 'sz6_2' at row 7
Warning (sql 1264): Out of range value for column 'sz6_2' at row 8
Warning (sql 1264): Out of range value for column 'sz6_2' at row 9
Note (sql 1265): Data truncated for column 'sz6_2' at row 10
Warning (sql 1264): Out of range value for column 'sz6_2' at row 11
Warning (sql 1264): Out of range value for column 'sz6_2' at row 12
Note (sql 1265): Data truncated for column 'sz20_19' at row 13
Warning (sql 1264): Out of range value for column 'sz20_19' at row 14
Warning (sql 1264): Out of range value for column 'sz20_19' at row 15
Note (sql 1265): Data truncated for column 'sz20_19' at row 16
Warning (sql 1264): Out of range value for column 'sz20_19' at row 17
Warning (sql 1264): Out of range value for column 'sz20_19' at row 18
```

```sql
SELECT * FROM decimal_signed_example;
```

```sql
+-------------------+-------------+----------+------------------------+
| description       | sz10_0      | sz6_2    | sz20_19                |
+-------------------+-------------+----------+------------------------+
| OK                |  9999999999 |     NULL |                   NULL |
| Rounded overflow  |  9999999999 |     NULL |                   NULL |
| Overflow          |  9999999999 |     NULL |                   NULL |
| OK                | -9999999999 |     NULL |                   NULL |
| Rounded underflow | -9999999999 |     NULL |                   NULL |
| Underflow         | -9999999999 |     NULL |                   NULL |
| OK                |        NULL |  9999.99 |                   NULL |
| Rounded overflow  |        NULL |  9999.99 |                   NULL |
| Overflow          |        NULL |  9999.99 |                   NULL |
| OK                |        NULL | -9999.99 |                   NULL |
| Rounded underflow |        NULL | -9999.99 |                   NULL |
| Underflow         |        NULL | -9999.99 |                   NULL |
| OK                |        NULL |     NULL |  9.9999999999999999999 |
| Rounded overflow  |        NULL |     NULL |  9.9999999999999999999 |
| Overflow          |        NULL |     NULL |  9.9999999999999999999 |
| OK                |        NULL |     NULL | -9.9999999999999999999 |
| Rounded underflow |        NULL |     NULL | -9.9999999999999999999 |
| Underflow         |        NULL |     NULL | -9.9999999999999999999 |
+-------------------+-------------+----------+------------------------+
```

### DECIMAL ZEROFILL

A special type of `DECIMAL UNSIGNED` is `DECIMAL ZEROFILL`, which pads out the values with leading zeros in `SELECT` results. The number of leading zeros is just enough to pad the field out to the length of the type's field size (not counting the decimal place), but the zeros are not included in an expression result or in a `UNION SELECT` column.

Using `DECIMAL ZEROFILL` works the same way as `DECIMAL UNSIGNED` for most operations except a simple `SELECT`. For example, with the following test table setup:

```sql
CREATE TABLE decimal_zerofill_example (
  description VARCHAR(20),
  sz10_0 DECIMAL ZEROFILL,
  sz6_2 DECIMAL(6,2) ZEROFILL,
  sz20_19 DECIMAL(20,19) ZEROFILL
);
```

```sql
SET @pi = 3.1415926535897932384626433832795;
```

```sql
INSERT INTO decimal_zerofill_example VALUES
  ('Pi', @pi, @pi, @pi),
  ('Series', 1234.567890123, 1234.567890123, 1.234567890123),
  ('Various', 1234567890, 9999.99, 9.9999999999999999999);
```

```sql
SELECT * FROM decimal_zerofill_example;

+-------------+------------+---------+-----------------------+
| description | sz10_0     | sz6_2   | sz20_19               |
+-------------+------------+---------+-----------------------+
| Pi          | 0000000003 | 0003.14 | 3.1415926535897932385 |
| Series      | 0000001235 | 1234.57 | 1.2345678901230000000 |
| Various     | 1234567890 | 9999.99 | 9.9999999999999999999 |
+-------------+------------+---------+-----------------------+
```

## See Also

* [Numeric Data Type Overview](numeric-data-type-overview.md)
* [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
