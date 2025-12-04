---
description: >-
  A list of constraints and limits within the InnoDB engine, including maximum
  table size, column counts, and index key lengths.
---

# InnoDB Limitations

The [InnoDB storage engine](./) has the following limitations.

## Limitations on Schema

* InnoDB tables can have a maximum of 1,017 columns. This includes [virtual generated columns](../../../reference/sql-statements/data-definition/create/generated-columns.md).
* InnoDB tables can have a maximum of 64 secondary indexes.
* A multicolumn index on InnoDB can use a maximum of 32 columns. If you attempt to create a multicolumn index that uses more than 32 columns, MariaDB returns an Error 1070.

## Limitations on Size

* With the exception of variable-length columns (that is, [VARBINARY](../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../reference/data-types/string-data-types/text.md)), rows in InnoDB have a maximum length of roughly half the page size for 4KB, 8KB, 16KB and 32KB page sizes.
* The maximum size for [BLOB](../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../reference/data-types/string-data-types/text.md) columns is 4GB. This also applies to [LONGBLOB](../../../reference/data-types/string-data-types/longblob.md) and [LONGTEXT](../../../reference/data-types/string-data-types/longtext.md).
* MariaDB imposes a row-size limit of 65,535 bytes for the combined sizes of all columns. If the table contains [BLOB](../../../reference/data-types/string-data-types/blob.md) or [TEXT](../../../reference/data-types/string-data-types/text.md) columns, these only count for 9 - 12 bytes in this calculation, given that their content is stored separately.
* 32-bit operating systems have a maximum file size limit of 2GB. When working with large tables using this architecture, configure InnoDB to use smaller data files.
* The maximum size for the combined InnoDB log files is 512GB.
* With tablespaces, the minimum size is 10MB, the maximum varies depending on the InnoDB Page Size.

| InnoDB Page Size | Maximum Tablespace Size |
| ---------------- | ----------------------- |
| 4KB              | 16TB                    |
| 8KB              | 32TB                    |
| 16KB             | 64TB                    |
| 32KB             | 128TB                   |
| 64KB             | 256TB                   |

### Page Sizes

Using the [innodb\_page\_size](innodb-system-variables.md#innodb_page_size) system variable, you can configure the size in bytes for InnoDB pages. Pages default to 16KB. There are certain limitations on how you use this variable.

* MariaDB instances using one page size cannot use data files or log files from an instance using a different page size.
* When using a Page Size of 4KB or 8KB, the maximum index key length is lowered proportionately.

| InnoDB Page Size | Index Key Length |
| ---------------- | ---------------- |
| 4KB              | 768B             |
| 8KB              | 1536B            |
| 16KB             | 3072B            |

## Limitations on Tables

InnoDB has the following table-specific limitations.

* When you issue a [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) statement, InnoDB doesn't regenerate the table, rather it deletes each row from the table one by one.
* When running MariaDB on Windows, InnoDB stores databases and tables in lowercase. When moving databases and tables in a binary format from Windows to a Unix-like system or from a Unix system to Windows, you need to rename these to use lowercase.
* When using cascading [foreign keys](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md), operations in the cascade don't activate triggers.

### Table Analysis

When running [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md) twice on a table in which statements or transactions are running, MariaDB blocks the second [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md) until the statement or transaction is complete. This occurs because the statement or transaction blocks the second [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md) statement from reloading the table definition, which it must do since the old one was marked as obsolete after the first statement.

### Table Status

[SHOW TABLE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-table-status.md) statements do not provide accurate statistics for InnoDB, except for the physical table size.

The InnoDB storage engine does not maintain internal row counts. Transactions isolate writes, which means that concurrent transactions will not have the same row counts.

### Auto-incrementing Columns

* When defining an index on an auto-incrementing column, it must be defined in a way that allows the equivalent of `SELECT MAX(col)` lookups on the table.
* Restarting MariaDB may cause InnoDB to reuse old auto-increment values, such as in the case of a transaction that was rolled back.
* When auto-incrementing columns run out of values, [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statements generate duplicate-key errors.

## Transactions and Locks

* You can modify data on a maximum of 96 \* 1023 concurrent transactions that generate undo records.
* Of the 128 rollback segments, InnoDB assigns 32 to non-redo logs for transactions that modify temporary tables and related objects, reducing the maximum number of concurrent data-modifying transactions to 96,000, from 128.000.
* The limit is 32,000 concurrent transactions when all data-modifying transactions also modify temporary tables.
* Issuing a [LOCK TABLES](../../../reference/sql-statements/transactions/lock-tables.md) statement sets two locks on each table when the [innodb\_table\_locks](innodb-system-variables.md#innodb_table_locks) system variable is enabled (the default).
* When you commit or roll back a transaction, any locks set in the transaction are released. You don't need to issue [LOCK TABLES](../../../reference/sql-statements/transactions/lock-tables.md) statements when the [autocommit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) variable is enabled, as InnoDB would immediately release the table locks.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
