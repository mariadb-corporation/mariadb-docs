---
description: >-
  Fixed-length binary string type. This type stores a fixed number of bytes,
  padding with zero bytes if the data is shorter.
---

# BINARY

This page describes the BINARY data type. For details about the operator, see [Binary Operator](../../sql-functions/string-functions/binary-operator.md).

## Syntax

```
BINARY(M)
```

## Description

The `BINARY` type is similar to the [CHAR](char.md) type, but stores binary byte strings rather than non-binary character strings. `M` represents the column length in bytes.

It contains no character set, and comparison and sorting are based on the numeric value of the bytes.

If the maximum length is exceeded, and [SQL strict mode](../../../server-management/variables-and-modes/sql_mode.md) is not enabled , the extra characters will be dropped with a warning. If strict mode is enabled, an error will occur.

`BINARY` values are right-padded with `0x00` (the zero byte) to the specified length when inserted. The padding is _not_ removed on select, so this needs to be taken into account when sorting and comparing, where all bytes are significant. The zero byte, `0x00` is less than a space for comparison purposes.

## Examples

Inserting too many characters, first with strict mode off, then with it on:

```sql
CREATE TABLE bins (a BINARY(10));

INSERT INTO bins VALUES('12345678901');
Query OK, 1 row affected, 1 warning (0.04 sec)

SELECT * FROM bins;
+------------+
| a          |
+------------+
| 1234567890 |
+------------+

SET sql_mode='STRICT_ALL_TABLES';

INSERT INTO bins VALUES('12345678901');
ERROR 1406 (22001): Data too long for column 'a' at row 1
```

Sorting is performed with the byte value:

```sql
TRUNCATE bins;

INSERT INTO bins VALUES('A'),('B'),('a'),('b');

SELECT * FROM bins ORDER BY a;
+------+
| a    |
+------+
| A    |
| B    |
| a    |
| b    |
+------+
```

Using [CAST](../../sql-functions/string-functions/cast.md) to sort as a [CHAR](char.md) instead:

```sql
SELECT * FROM bins ORDER BY CAST(a AS CHAR);
+------+
| a    |
+------+
| a    |
| A    |
| b    |
| B    |
+------+
```

The field is a `BINARY(10)`, so padding of two '\0's are inserted, causing comparisons that don't take this into account to fail:

```sql
TRUNCATE bins;

INSERT INTO bins VALUES('12345678');

SELECT a = '12345678', a = '12345678\0\0' from bins;
+----------------+--------------------+
| a = '12345678' | a = '12345678\0\0' |
+----------------+--------------------+
|              0 |                  1 |
+----------------+--------------------+
```

Example of `BINARY`:

```sql
CREATE TABLE binary_example (
   description VARCHAR(20),
   example BINARY(255)
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer

INSERT INTO binary_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 255, CHAR(7)));

SELECT description, LENGTH(example) AS length
   FROM binary_example;

+---------------------+--------+
| description         | length |
+---------------------+--------+
| Normal foo          |    255 |
| Trailing spaces foo |    255 |
| NULLed              |   NULL |
| Empty               |    255 |
| Maximum             |    255 |
+---------------------+--------+
```

### Data Too Long

When `SQL_MODE` is strict (the default), a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.

Example of data too long behavior for `BINARY`:

```sql
TRUNCATE binary_example;

INSERT INTO binary_example VALUES
   ('Overflow', RPAD('', 256, CHAR(7)));

ERROR 1406 (22001): Data too long for column 'example' at row 1
```

## See Also

* [CHAR](char.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
