---
description: >-
  These views provide a granular breakdown of InnoDB buffer pool usage by
  individual tables, sorted by buffer allocation size.
---

# innodb\_buffer\_stats\_by\_table and x$innodb\_buffer\_stats\_by\_table Sys Schema Views

{% include "../../../../.gitbook/includes/sys-schema-views-are-availa....md" %}

Querying these views can have a noticeable performance impact on a production server.

## Description

The `innodb_buffer_stats_by_table` and `x$innodb_buffer_stats_by_table` views summarize information from the [Information Schema INNODB\_BUFFER\_PAGE table](../../information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_buffer_page-table.md), grouped by schema and table. Rows are sorted by descending buffer size by default.

The `innodb_buffer_stats_by_table` view is intended to be easier for human reading, while the `x$innodb_buffer_stats_by_table` view provides the data in raw form, intended for tools that process the data.

They contain the following columns:

| Column         | Description                                                                                                                                 |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| object\_schema | Object schema name, or InnoDB System if the table belongs to the [InnoDB storage engine](../../../../server-usage/storage-engines/innodb/). |
| object\_name   | Table name.                                                                                                                                 |
| allocated      | Total number of bytes allocated for the table.                                                                                              |
| data           | Number of data bytes allocated for the table.                                                                                               |
| pages          | Total number of pages allocated for the table.                                                                                              |
| pages\_hashed  | Total number of hashed pages allocated for the table.                                                                                       |
| pages\_old     | Total number of old pages allocated for the table.                                                                                          |
| rows\_cached   | Total number of cached rows for the table.                                                                                                  |

## Example

```sql
SELECT * FROM sys.innodb_buffer_stats_by_table\G
*************************** 1. row ***************************
object_schema: mysql
  object_name: transaction_registry
    allocated: 64.00 KiB
         data: 0 bytes
        pages: 4
 pages_hashed: 4
    pages_old: 4
  rows_cached: 0
*************************** 2. row ***************************
object_schema: InnoDB System
  object_name: SYS_FOREIGN
    allocated: 48.00 KiB
         data: 0 bytes
        pages: 3
 pages_hashed: 3
    pages_old: 3
  rows_cached: 0
*************************** 3. row ***************************
object_schema: InnoDB System
  object_name: SYS_TABLES
    allocated: 32.00 KiB
         data: 1.07 KiB
        pages: 2
 pages_hashed: 2
    pages_old: 2
  rows_cached: 10

...

 SELECT * FROM sys.x$innodb_buffer_stats_by_table\G
*************************** 1. row ***************************
object_schema: mysql
  object_name: transaction_registry
    allocated: 65536
         data: 0
        pages: 4
 pages_hashed: 0
    pages_old: 0
  rows_cached: 0
*************************** 2. row ***************************
object_schema: InnoDB System
  object_name: SYS_FOREIGN
    allocated: 49152
         data: 0
        pages: 3
 pages_hashed: 0
    pages_old: 0
  rows_cached: 0
*************************** 3. row ***************************
object_schema: InnoDB System
  object_name: SYS_TABLES
    allocated: 32768
         data: 1100
        pages: 2
 pages_hashed: 0
    pages_old: 0
  rows_cached: 10
....
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
