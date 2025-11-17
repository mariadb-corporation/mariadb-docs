# TINYBLOB

## Syntax

```sql
TINYBLOB
```

## Description

A [BLOB](blob.md) column with a maximum length of 255 (2⁸ - 1) bytes. Each `TINYBLOB` value is stored using a one-byte length prefix that indicates the number of bytes in the value.

## EXAMPLES

### TINYBLOB

Example of TINYBLOB:

```sql
CREATE TABLE tinyblob_example (
   description VARCHAR(20),
   example TINYBLOB
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer
```

```sql
INSERT INTO tinyblob_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 255, CHAR(7)));
```

```sql
SELECT description, LENGTH(example) AS length
   FROM tinyblob_example;
```

```sql
+---------------------+--------+
| description         | length |
+---------------------+--------+
| Normal foo          |      3 |
| Trailing spaces foo |      9 |
| NULLed              |   NULL |
| Empty               |      0 |
| Maximum             |    255 |
+---------------------+--------+
```

### Data too Long

When `SQL_MODE` is strict (the default), a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.

Example of data too long behavior for `TINYBLOB`:

```sql
TRUNCATE tinyblob_example;

INSERT INTO tinyblob_example VALUES
   ('Overflow', RPAD('', 256, CHAR(7)));
```

```sql
ERROR 1406 (22001): Data too long for column 'example' at row 1
```

## See Also

* [BLOB](blob.md)
* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
