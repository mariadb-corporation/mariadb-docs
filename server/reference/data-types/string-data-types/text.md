# TEXT

## Syntax

```sql
TEXT[(M)] [CHARACTER SET charset_name] [COLLATE collation_name]
```

## Description

A `TEXT` column with a maximum length of `65,535` (`2^16 - 1`) characters. The effective maximum length is less if the value contains multi-byte characters. Each `TEXT` value is stored using a two-byte length prefix that indicates the number of bytes in the value. If you need a bigger storage, consider using [MEDIUMTEXT](mediumtext.md) instead.

An optional length `M` can be given for this type. If this is done, MariaDB creates the column as the smallest `TEXT` type large enough to hold values`M` characters long.

`BLOB` and `TEXT` columns can be assigned a [DEFAULT](../../sql-statements/data-definition/create/create-table.md#default) value.

## Examples

### Trailing spaces:

```sql
CREATE TABLE strtest (d TEXT(10));
INSERT INTO strtest VALUES('Maria   ');

SELECT d='Maria',d='Maria   ' FROM strtest;
+-----------+--------------+
| d='Maria' | d='Maria   ' |
+-----------+--------------+
|         1 |            1 |
+-----------+--------------+

SELECT d LIKE 'Maria',d LIKE 'Maria   ' FROM strtest;
+----------------+-------------------+
| d LIKE 'Maria' | d LIKE 'Maria   ' |
+----------------+-------------------+
|              0 |                 1 |
+----------------+-------------------+
```

### Example of TEXT

```sql
CREATE TABLE text_example (
   description VARCHAR(20),
   example TEXT
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer
```

```sql
INSERT INTO text_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 65535, 'x'));
```

```sql
SELECT description, LENGTH(example) AS length
   FROM text_example;
```

```sql
+---------------------+--------+
| description         | length |
+---------------------+--------+
| Normal foo          |      3 |
| Trailing spaces foo |      9 |
| NULLed              |   NULL |
| Empty               |      0 |
| Maximum             |  65535 |
+---------------------+--------+
```

### Data too Long

When `SQL_MODE` is strict (the default) a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.

Example of data too long behavior for `TEXT`:

```sql
TRUNCATE text_example;

INSERT INTO text_example VALUES
   ('Overflow', RPAD('', 65536, 'x'));
```

```sql
ERROR 1406 (22001): Data too long for column 'example' at row 1
```

## Indexing

A [unique index](../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#unique-index) can be created on a `TEXT` column.

Internally, this uses hash indexing to quickly check the values and if a hash collision is found, the actual stored values are compared in order to retain the uniqueness.

## Difference between VARCHAR and TEXT

* [VARCHAR](varchar.md) columns can be fully indexed. `TEXT` columns can only be indexed over a specified length.
* Using `TEXT` or [BLOB](blob.md) in a [SELECT](../../sql-statements/data-manipulation/selecting-data/select.md) query that uses temporary tables for storing intermediate results will force the temporary table to be disk based (using the [Aria storage engine](../../../server-usage/storage-engines/aria/aria-storage-engine.md) instead of the [memory storage engine](../../../server-usage/storage-engines/memory-storage-engine.md), which is a bit slower. This is not that bad as the [Aria storage engine](../../../server-usage/storage-engines/aria/aria-storage-engine.md) caches the rows in memory. To get the benefit of this, one should ensure that the [aria\_pagecache\_buffer\_size](../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_pagecache_buffer_size) variable is big enough to hold most of the row and index data for temporary tables.

### For Storage Engine Developers

* Internally the full length of the [VARCHAR](varchar.md) column is allocated inside each TABLE objects record\[] structure. As there are three such buffers, each open table will allocate 3 times max-length-to-store-varchar bytes of memory.
* `TEXT` and `BLOB` columns are stored with a pointer (4 or 8 bytes) + a 1-4 bytes length. The `TEXT` data is only stored once. This means that internally `TEXT` uses less memory for each open table but instead has the additional overhead that each `TEXT` object needs to be allocated and freed for each row access (with some caching in between).

## See Also

* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [MEDIUMTEXT](mediumtext.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
