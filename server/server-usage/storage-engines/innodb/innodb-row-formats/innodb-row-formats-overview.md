---
description: >-
  An overview of the four InnoDB row formats (REDUNDANT, COMPACT, DYNAMIC,
  COMPRESSED), comparing their storage efficiency and feature support.
---

# InnoDB Row Formats Overview

The [InnoDB](../) storage engine supports four different row formats:

* [REDUNDANT](innodb-row-formats-overview.md#redundant-row-format)
* [COMPACT](innodb-row-formats-overview.md#compact-row-format)
* [DYNAMIC](innodb-row-formats-overview.md#dynamic-row-format)
* [COMPRESSED](innodb-row-formats-overview.md#compressed-row-format)

## Default Row Format

The [innodb\_default\_row\_format](../innodb-system-variables.md#innodb_default_row_format) system variable can be used to set the default row format for InnoDB tables. The possible values are:

* `redundant`
* `compact`
* `dynamic`

This system variable's default value is `dynamic`, which means that the default row format is `DYNAMIC`.

This system variable cannot be set to `compressed`, which means that the default row format cannot be `COMPRESSED`.

For example, the following statements would create a table with the `DYNAMIC` row format:

```sql
SET SESSION innodb_strict_mode=ON;

SET GLOBAL innodb_default_row_format='dynamic';

CREATE TABLE tab (
   id INT,
   str VARCHAR(50)
) ENGINE=InnoDB;
```

## Setting a Table's Row Format

One way to specify an InnoDB table's row format is by setting the [ROW\_FORMAT](../../../../reference/sql-statements/data-definition/create/create-table.md#row_format) table option to the relevant row format in a [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement:

```sql
SET SESSION innodb_strict_mode=ON;

SET GLOBAL innodb_file_per_table=ON;

SET GLOBAL innodb_file_format='Barracuda';

CREATE TABLE tab (
   id INT,
   str VARCHAR(50)
) ENGINE=InnoDB ROW_FORMAT=DYNAMIC;
```

## Checking a Table's Row Format

The [SHOW TABLE STATUS](../../../../reference/sql-statements/administrative-sql-statements/show/show-table-status.md) statement can be used to see the row format used by a table:

```sql
SHOW TABLE STATUS FROM db1 WHERE Name='tab'\G
*************************** 1. row ***************************
           Name: tab
         Engine: InnoDB
        Version: 10
     Row_format: Dynamic
           Rows: 0
 Avg_row_length: 0
    Data_length: 16384
Max_data_length: 0
   Index_length: 0
      Data_free: 0
 Auto_increment: NULL
    Create_time: 2019-04-18 20:24:04
    Update_time: NULL
     Check_time: NULL
      Collation: latin1_swedish_ci
       Checksum: NULL
 Create_options: row_format=DYNAMIC
        Comment:
```

The [information\_schema.INNODB\_SYS\_TABLES](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table can also be queried to see the row format used by a table:

```sql
SELECT * FROM information_schema.INNODB_SYS_TABLES WHERE name='db1/tab'\G
*************************** 1. row ***************************
     TABLE_ID: 42
         NAME: db1/tab
         FLAG: 33
       N_COLS: 4
        SPACE: 27
  FILE_FORMAT: Barracuda
   ROW_FORMAT: Dynamic
ZIP_PAGE_SIZE: 0
   SPACE_TYPE: Single
```

A table's tablespace is tagged with the lowest InnoDB file format that supports the table's row format. So, even if the `Barracuda` file format is enabled, tables that use the `COMPACT` or `REDUNDANT` row formats are tagged with the `Antelope` file format in the [information\_schema.INNODB\_SYS\_TABLES](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table.

## Row Formats

### REDUNDANT Row Format

The `REDUNDANT` row format is the original non-compacted row format.

The `REDUNDANT` row format was the only available row format before MySQL 5.0.3. In that release, this row format was retroactively named the `REDUNDANT` row format. In the same release, the `COMPACT` row format was introduced as the new default row format.

See [InnoDB REDUNDANT Row Format](innodb-redundant-row-format.md) for more information.

### COMPACT Row Format

Default row format in earlier versions `COMPACT`.

The `COMPACT` row format is similar to the `REDUNDANT` row format, but it stores data in a more compact manner that requires about 20% less storage.

See [InnoDB COMPACT Row Format](innodb-compact-row-format.md) for more information.

### DYNAMIC Row Format

`DYNAMIC` is the default row format.

The `DYNAMIC` row format is similar to the `COMPACT` row format, but tables using the `DYNAMIC` row format can store even more data on overflow pages than tables using the `COMPACT` row format. This results in more efficient data storage than tables using the `COMPACT` row format, especially for tables containing columns using the [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) data types. However, InnoDB tables using the `COMPRESSED` row format are more efficient.

See [InnoDB DYNAMIC Row Format](innodb-dynamic-row-format.md) for more information.

### COMPRESSED Row Format

An alternative way to compress InnoDB tables is by using [InnoDB Page Compression](../innodb-page-compression.md).

The `COMPRESSED` row format is similar to the `COMPACT` row format, but tables using the `COMPRESSED` row format can store even more data on overflow pages than tables using the `COMPACT` row format. This results in more efficient data storage than tables using the `COMPACT` row format, especially for tables containing columns using the [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) data types.

The `COMPRESSED` row format also supports compression of all data and index pages.

See [InnoDB COMPRESSED Row Format](innodb-compressed-row-format.md) for more information.

## Maximum Row Size

Several factors help determine the maximum row size of an InnoDB table.

First, MariaDB enforces a 65,535 byte limit on a table's maximum row size. The total size of a table's [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) columns do not count towards this limit. Only the pointers for a table's [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) columns count towards this limit. MariaDB enforces this limit for all storage engines, so this limit also applies to InnoDB tables. Therefore, this limit is the absolute maximum row size for an InnoDB table.

If you try to create a table that exceeds MariaDB's global limit on a table's maximum row size, then you will see an error like this:

```
ERROR 1118 (42000): Row size too large. The maximum row size for the used table type, 
not counting BLOBs, is 65535. This includes storage overhead, check the manual. You 
have to change some columns to TEXT or BLOBs
```

However, InnoDB also has its own limits on the maximum row size, so an InnoDB table's maximum row size could be smaller than MariaDB's global limit.

Second, the maximum amount of data that an InnoDB table can store in a row's main data page depends on the value of the [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size) system variable. At most, the data that a single row can consume on the row's main data page is half of the value of the [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size) system variable. With the default value of `16k`, that would mean that a single row can consume at most around 8 KB on the row's main data page. However, the limit on the row's main data page is not the absolute limit on the row's size.

Third, all InnoDB row formats can store certain kinds of data in overflow pages, so the maximum row size of an InnoDB table can be larger than the maximum amount of data that can be stored in the row's main data page.

Some row formats can store more data in overflow pages than others. For example, the `DYNAMIC` and `COMPRESSED` row formats can store the most data in overflow pages. To see how to determine the how the various InnoDB row formats can use overflow pages, see the following sections:

* [InnoDB REDUNDANT Row Format: Overflow Pages with the REDUNDANT Row Format](innodb-redundant-row-format.md#overflow-pages-with-the-redundant-row-format)
* [InnoDB COMPACT Row Format: Overflow Pages with the COMPACT Row Format](innodb-compact-row-format.md#overflow-pages-with-the-compact-row-format)
* [InnoDB DYNAMIC Row Format: Overflow Pages with the DYNAMIC Row Format](innodb-dynamic-row-format.md#overflow-pages-with-the-dynamic-row-format)
* [InnoDB COMPRESSED Row Format: Overflow Pages with the COMPRESSED Row Format](innodb-compressed-row-format.md#overflow-pages-with-the-compressed-row-format)

If a table's definition can allow rows that the table's InnoDB row format can't actually store, then InnoDB will raise errors or warnings in certain scenarios.

If the table were using the `REDUNDANT` or `COMPACT` row formats, then the error or warning would be the following:

```sql
ERROR 1118 (42000): Row size too large (> 8126). Changing some columns to 
TEXT or BLOB or using ROW_FORMAT=DYNAMIC or ROW_FORMAT=COMPRESSED 
may help. In current row format, BLOB prefix of 768 bytes is stored inline.
```

And if the table were using the `DYNAMIC` or `COMPRESSED` row formats, then the error or warning would be the following:

```sql
ERROR 1118 (42000): Row size too large (> 8126). Changing some columns to 
TEXT or BLOB may help. In current row format, BLOB prefix of 0 bytes is stored inline.
```

These messages are raised in the following cases:

* If [InnoDB strict mode](../innodb-strict-mode.md) is enabled and if a [DDL](../../../../reference/sql-statements/data-definition/) statement is executed that touches the table, such as [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/), then InnoDB will raise an error with this message
* If [InnoDB strict mode](../innodb-strict-mode.md) is disabled and if a [DDL](../../../../reference/sql-statements/data-definition/) statement is executed that touches the table, such as [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md)`or [ALTER TABLE](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md)`, then InnoDB will raise a warning with this message.
* Regardless of whether [InnoDB strict mode](../innodb-strict-mode.md) is enabled, if a [DML](../../../../reference/sql-statements/data-manipulation/) statement is executed that attempts to write a row that the table's InnoDB row format can't store, then InnoDB will raise an error with this message.

For information on how to solve the problem, see [Troubleshooting Row Size Too Large Errors with InnoDB](troubleshooting-row-size-too-large-errors-with-innodb.md).

## Feature Summary

| Feature                                         | [Dynamic](innodb-dynamic-row-format.md)                                                                                 | [Compressed](innodb-compressed-row-format.md)                                                                           | [Compact](innodb-compact-row-format.md) | [Redundant](innodb-redundant-row-format.md) |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------- |
| Default                                         | Yes                                                                                                                     | No                                                                                                                      | No                                      | No                                          |
| Recommended                                     | Yes                                                                                                                     | No                                                                                                                      | No                                      | No                                          |
| Efficiently stores large columns                | Yes                                                                                                                     | Yes                                                                                                                     | No                                      | No                                          |
| Efficiently utilizes buffer pool                | Yes                                                                                                                     | No                                                                                                                      | Yes                                     | Yes                                         |
| Supported Page Sizes                            | • 64k • 32k • 16k • 8k • 4k                                                                                             | • 16k • 8k • 4k                                                                                                         | • 64k • 32k • 16k • 8k • 4k             | • 64k • 32k • 16k • 8k • 4k                 |
| Maximum size of indexed column values           | • 3072 bytes (innodb\_page\_size >= 16k) • 1536 bytes (innodb\_page\_size == 8k) • 768 bytes (innodb\_page\_size == 4k) | • 3072 bytes (innodb\_page\_size >= 16k) • 1536 bytes (innodb\_page\_size == 8k) • 768 bytes (innodb\_page\_size == 4k) | 767 bytes                               | 767 bytes                                   |
| Supports ADD/DROP column with INSTANT Algorithm | Yes                                                                                                                     | No                                                                                                                      | Yes                                     | Yes                                         |

## Known Issues

### Upgrading Causes Row Size Too Large Errors

In earlier versions, MariaDB doesn't properly calculate the row sizes while executing DDL. In these versions, _unsafe_ tables can be created, even if [InnoDB strict mode](../innodb-strict-mode.md) is enabled. The calculations were fixed by [MDEV-19292](https://jira.mariadb.org/browse/MDEV-19292).

As a side effect, some tables that could be created or altered in previous versions may get rejected with the following error in these releases and any later releases.

```
ERROR 1118 (42000): Row size too large (> 8126). Changing some columns to 
TEXT or BLOB may help. In current row format, BLOB prefix of 0 bytes is stored inline.
```

And users could also see the following message as an error or warning in the [error log](../../../../server-management/server-monitoring-logs/error-log.md):

```
[Warning] InnoDB: Cannot add field col in table db1.tab because after adding it, the row size is 8478 which is greater than maximum allowed size (8126) for a record on index leaf page.
```

InnoDB used the wrong calculations to determine row sizes for quite a long time, so a lot of users may unknowingly have _unsafe_ tables that the InnoDB row format can't actually store.

InnoDB does not currently have an easy way to check which existing tables have this problem. See [MDEV-20400](https://jira.mariadb.org/browse/MDEV-20400) for more information.

For information on how to solve the problem, see [Troubleshooting Row Size Too Large Errors with InnoDB](troubleshooting-row-size-too-large-errors-with-innodb.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
