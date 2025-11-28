---
description: >-
  Fixed-length character string type. CHAR columns store strings of a specified
  length (0 to 255), padding with spaces if necessary.
---

# CHAR

{% hint style="info" %}
This page covers the `CHAR` data type. See [CHAR Function](../../sql-functions/string-functions/char-function.md) for the function.
{% endhint %}

## Syntax

```sql
[NATIONAL] CHAR[(M)] [CHARACTER SET charset_name] [COLLATE collation_name]
```

## Description

A fixed-length string that is always right-padded with spaces to the specified length when stored. `M` represents the column length in characters. The range of `M` is `0` to `255`. If `M` is omitted, the length is `1`.

`CHAR(0)` columns can contain 2 values: an empty string or `NULL`. Such columns cannot be part of an index. The [CONNECT](../../../server-usage/storage-engines/connect/) storage engine does not support `CHAR(0)`.

**Note:** Trailing spaces are removed when `CHAR` values are retrieved unless the `PAD_CHAR_TO_FULL_LENGTH` [SQL mode](../../../server-management/variables-and-modes/sql_mode.md) is enabled.

If a unique index consists of a column where trailing pad characters are stripped or ignored, inserts into that column where values differ only by the number of trailing pad characters will result in a duplicate-key error.

## Examples

Trailing spaces:

```sql
CREATE TABLE strtest (c CHAR(10));
INSERT INTO strtest VALUES('Maria   ');

SELECT c='Maria',c='Maria   ' FROM strtest;
+-----------+--------------+
| c='Maria' | c='Maria   ' |
+-----------+--------------+
|         1 |            1 |
+-----------+--------------+

SELECT c LIKE 'Maria',c LIKE 'Maria   ' FROM strtest;
+----------------+-------------------+
| c LIKE 'Maria' | c LIKE 'Maria   ' |
+----------------+-------------------+
|              1 |                 0 |
+----------------+-------------------+
```

Example of `CHAR`:

```sql
CREATE TABLE char_example (
   description VARCHAR(20),
   example CHAR(255)
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer
```

```sql
INSERT INTO char_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 255, 'x'));
```

```sql
SELECT description, LENGTH(example) AS length FROM char_example;

+---------------------+--------+
| description         | length |
+---------------------+--------+
| Normal foo          |      3 |
| Trailing spaces foo |      3 |
| NULLed              |   NULL |
| Empty               |      0 |
| Maximum             |    255 |
+---------------------+--------+
```

### Data Too Long

When `SQL_MODE` is strict (the default), a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.

Example of data too long behavior for `CHAR`:

```sql
TRUNCATE char_example;

INSERT INTO char_example VALUES
   ('Overflow', RPAD('', 256, 'x'));

ERROR 1406 (22001): Data too long for column 'example' at row 1
```

### NO PAD Collations

`NO PAD` collations regard trailing spaces as normal characters. You can get a list of all `NO PAD` collations by querying the [Information Schema Collations table](../../system-tables/information-schema/information-schema-tables/information-schema-collations-table.md), for example:

```sql
SELECT collation_name FROM information_schema.collations 
  WHERE collation_name LIKE "%nopad%";  
+------------------------------+
| collation_name               |
+------------------------------+
| big5_chinese_nopad_ci        |
| big5_nopad_bin               |
...
```

## See Also

* [CHAR Function](../../sql-functions/string-functions/char-function.md)
* [VARCHAR](varchar.md)
* [BINARY](binary.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
