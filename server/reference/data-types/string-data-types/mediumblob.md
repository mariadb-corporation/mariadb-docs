# MEDIUMBLOB

## Syntax

```sql
MEDIUMBLOB
```

## Description

A [BLOB](blob.md) column with a maximum length of 16,777,215 (2²⁴ - 1) bytes. Each `MEDIUMBLOB` value is stored using a three-byte length prefix that indicates the number of bytes in the value.

`LONG VARBINARY` is a synonym for `MEDIUMBLOB` .

## EXAMPLES

### MEDIUMBLOB

Example of `MEDIUMBLOB`:

```sql
CREATE TABLE mediumblob_example (
   description VARCHAR(20),
   example MEDIUMBLOB
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer
```

```sql
INSERT INTO mediumblob_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 16777215, CHAR(7)));
```

```sql
SELECT description, LENGTH(example) AS length
   FROM mediumblob_example;
```

```sql
+---------------------+----------+
| description         | length   |
+---------------------+----------+
| Normal foo          |        3 |
| Trailing spaces foo |        9 |
| NULLed              |     NULL |
| Empty               |        0 |
| Maximum             | 16777215 |
+---------------------+----------+
```

### Data Too Long

When `SQL_MODE` is strict (the default), a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.

Example of data too long behavior for `MEDIUMBLOB`:

```sql
TRUNCATE mediumblob_example;
```

```sql
INSERT INTO mediumblob_example VALUES
   ('Overflow', RPAD('', 16777216, CHAR(7)));
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
