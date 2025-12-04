---
description: >-
  Detailed information on the COMPACT row format, which reduces storage space by
  roughly 20% compared to REDUNDANT, handling NULLs and variable-length columns
  efficiently.
---

# InnoDB COMPACT Row Format

**Note**`COMPACT` was the default row format in prior versions of MariaDB. MariaDB has since transitioned to `DYNAMIC` as the default row format.

The `COMPACT` row format is similar to the `REDUNDANT` row format, but it stores data in a more compact manner that requires about 20% less storage.

## Using the `COMPACT` Row Format

* If you performed a physical upgrade from older version of MariaDB Server or MySQL to a newer MariaDB Server version, then some of your tables may still use COMPACT row format.
* Compact row format does not store large columns as efficiently as the Dynamic row format.
* Compact row format limits indexing column values to 767 bytes, which is significant smaller than the Dynamic row format.

The easiest way to create an InnoDB table that uses the `COMPACT` row format is by setting the [ROW\_FORMAT](../../../../reference/sql-statements/data-definition/create/create-table.md#row_format) table option to `COMPACT` in a [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement.

It is recommended to set the [innodb\_strict\_mode](../innodb-system-variables.md#innodb_strict_mode) system variable to `ON` when using this row format.

The `COMPACT` row format is supported by both the `Antelope` and the `Barracuda` [file formats](../innodb-file-format.md), so tables with this row format can be created regardless of the value of the [innodb\_file\_format](../innodb-system-variables.md#innodb_file_format) system variable.

For example:

```sql
SET SESSION innodb_strict_mode=ON;

CREATE TABLE tab (
   id INT,
   str VARCHAR(50)
) ENGINE=InnoDB ROW_FORMAT=COMPACT;
```

## Index Prefixes with the `COMPACT` Row Format

The `COMPACT` row format supports index prefixes up to 767 bytes.

## Overflow Pages with the `COMPACT` Row Format

All InnoDB row formats can store certain kinds of data in overflow pages. This allows for the maximum row size of an InnoDB table to be larger than the maximum amount of data that can be stored in the row's main data page. See [Maximum Row Size](innodb-compact-row-format.md#maximum-row-size) for more information about the other factors that can contribute to the maximum row size for InnoDB tables.

In the `COMPACT` row format variable-length columns, such as columns using the [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) data types, can be partially stored in overflow pages.

InnoDB only considers using overflow pages if the table's row size is greater than half of [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size). If the row size is greater than this, then InnoDB chooses variable-length columns to be stored on overflow pages until the row size is less than half of [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size).

For [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) columns, only values longer than 767 bytes are considered for storage on overflow pages. Bytes that are stored to track a value's length do not count towards this limit. This limit is only based on the length of the actual column's data.

Fixed-length columns greater than 767 bytes are encoded as variable-length columns, so they can also be stored in overflow pages if the table's row size is greater than half of [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size). Even though a column using the [CHAR](../../../../reference/data-types/string-data-types/char.md) data type can hold at most 255 characters, a [CHAR](../../../../reference/data-types/string-data-types/char.md) column can still exceed 767 bytes in some cases. For example, a `char(255)` column can exceed 767 bytes if the [character set](../../../../reference/data-types/string-data-types/character-sets/) is `utf8mb4`.

If a column is chosen to be stored on overflow pages, then the first 767 bytes of the column's value and a 20-byte pointer to the column's first overflow page are stored on the main page. Each overflow page is the size of [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size). If a column is too large to be stored on a single overflow page, then it is stored on multiple overflow pages. Each overflow page contains part of the data and a 20-byte pointer to the next overflow page, if a next page exists.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
