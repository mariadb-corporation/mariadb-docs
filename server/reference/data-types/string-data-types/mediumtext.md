# MEDIUMTEXT

## Syntax

```sql
MEDIUMTEXT [CHARACTER SET charset_name] [COLLATE collation_name]
```

## Description

A [TEXT](text.md) column with a maximum length of 16,777,215 (2²⁴ - 1) characters. The effective maximum length is less if the value contains multi-byte characters. Each `MEDIUMTEXT` value is stored using\
a three-byte length prefix that indicates the number of bytes in the value.

### SYNONYMS

The following are synonyms for `MEDIUMTEXT`:

* LONG
* LONG CHAR VARYING
* LONG CHARACTER VARYING
* LONG VARCHAR
* LONG VARCHARACTER

## EXAMPLES

### MEDIUMTEXT

Example of `MEDIUMTEXT`:

```sql
CREATE TABLE mediumtext_example (
   description VARCHAR(20),
   example MEDIUMTEXT
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer
```

```sql
INSERT INTO mediumtext_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 16777215, 'x'));
```

```sql
SELECT description, LENGTH(example) AS length
   FROM mediumtext_example;
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

When `SQL_MODE` is strict (the default) a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.

Example of data too long behavior for `MEDIUMTEXT`:

```sql
TRUNCATE mediumtext_example;

INSERT INTO mediumtext_example VALUES
   ('Overflow', RPAD('', 16777216, 'x'));
```

```sql
ERROR 1406 (22001): Data too long for column 'example' at row 1
```

## See Also

* [TEXT](text.md)
* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
