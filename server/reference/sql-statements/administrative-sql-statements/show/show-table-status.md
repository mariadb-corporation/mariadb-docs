---
description: >-
  Get metadata for tables. View details like engine type, row count, data
  length, and create time for tables in a database.
---

# SHOW TABLE STATUS

## Syntax

```sql
SHOW TABLE STATUS [{FROM | IN} db_name]
    [LIKE 'pattern' | WHERE expr]
```

## Description

{% tabs %}
{% tab title="Current" %}
`SHOW TABLE STATUS` works like [SHOW TABLES](show-tables.md), but provides more extensive information about each table.
{% endtab %}

{% tab title="< 11.2.0" %}
`SHOW TABLE STATUS` works like [SHOW TABLES](show-tables.md), but provides more extensive information about each table. Only non-TEMPORARY tables are shown.
{% endtab %}
{% endtabs %}

The `LIKE` clause, if present on its own, indicates which table names to match. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

The following information is returned:

| Column             | Description                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name               | Table name.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Engine             | Table [storage engine](../../../../server-usage/storage-engines/).                                                                                                                                                                                                                                                                                                                                                                     |
| Version            | Version number from the table's .frm file.                                                                                                                                                                                                                                                                                                                                                                                             |
| Row\_format        | Row format (see [InnoDB](../../../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md), [Aria](../../../../server-usage/storage-engines/aria/aria-storage-formats.md) and [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/myisam-storage-formats.md) row formats).                                                                                                        |
| Rows               | Number of rows in the table. Some engines, such as [InnoDB](../../../../server-usage/storage-engines/innodb/) may store an estimate.                                                                                                                                                                                                                                                                                                   |
| Avg\_row\_length   | Average row length in the table.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Data\_length       | For [InnoDB](../../../../server-usage/storage-engines/innodb/), the index size, in pages, multiplied by the page size. For [Aria](../../../../server-usage/storage-engines/aria/) and [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/), length of the data file, in bytes. For [MEMORY](../../../../server-usage/storage-engines/memory-storage-engine.md), the approximate allocated memory.                 |
| Max\_data\_length  | Maximum length of the data file, ie the total number of bytes that could be stored in the table. Not used in [InnoDB](../../../../server-usage/storage-engines/innodb/).                                                                                                                                                                                                                                                               |
| Index\_length      | Length of the index file.                                                                                                                                                                                                                                                                                                                                                                                                              |
| Data\_free         | Bytes allocated but unused. For InnoDB tables in a shared tablespace, the free space of the shared tablespace with small safety margin. An estimate in the case of partitioned tables - see the [PARTITIONS](../../../system-tables/information-schema/information-schema-tables/information-schema-partitions-table.md) table.                                                                                                        |
| Auto\_increment    | Next [AUTO\_INCREMENT](../../../data-types/auto_increment.md) value.                                                                                                                                                                                                                                                                                                                                                                   |
| Create\_time       | Time the table was created. Some engines just return the ctime information from the file system layer here, in that case the value is not necessarily the table creation time but rather the time the file system metadata for it had last changed.                                                                                                                                                                                    |
| Update\_time       | Time the table was last updated. On Windows, the timestamp is not updated on update, so MyISAM values will be inaccurate. In [InnoDB](../../../../server-usage/storage-engines/innodb/), if shared tablespaces are used, will be NULL, while buffering can also delay the update, so the value will differ from the actual time of the last UPDATE, INSERT or DELETE.                                                                  |
| Check\_time        | Time the table was last checked. Not kept by all storage engines, in which case will be NULL.                                                                                                                                                                                                                                                                                                                                          |
| Collation          | [Character set and collation](../../../data-types/string-data-types/character-sets/).                                                                                                                                                                                                                                                                                                                                                  |
| Checksum           | Live checksum value, if any.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Create\_options    | Extra [CREATE TABLE](../../data-definition/create/create-table.md) options.                                                                                                                                                                                                                                                                                                                                                            |
| Comment            | Table comment provided when MariaDB created the table.                                                                                                                                                                                                                                                                                                                                                                                 |
| Max\_index\_length | Maximum index length (supported by MyISAM and Aria tables).                                                                                                                                                                                                                                                                                                                                                                            |
| Temporary          | Until [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.0), placeholder to signal that a table is a temporary table and always "N", except "Y" for generated information\_schema tables and NULL for views. From [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.0), will also be set to "Y" for local temporary tables. |

Similar information can be found in the [information\_schema.TABLES](../../../system-tables/information-schema/information-schema-tables/information-schema-tables-table.md) table as well as by using [mariadb-show](../../../../clients-and-utilities/administrative-tools/mariadb-show.md):

```bash
mariadb-show --status db_name
```

## Views

For views, all columns in `SHOW TABLE STATUS` are `NULL` except 'Name' and 'Comment'

## Example

```sql
SHOW TABLE STATUS\G
*************************** 1. row ***************************
           Name: bus_routes
         Engine: InnoDB
        Version: 10
     Row_format: Dynamic
           Rows: 5
 Avg_row_length: 3276
    Data_length: 16384
Max_data_length: 0
   Index_length: 0
      Data_free: 0
 Auto_increment: NULL
    Create_time: 2017-05-24 11:17:46
    Update_time: NULL
     Check_time: NULL
      Collation: latin1_swedish_ci
       Checksum: NULL
 Create_options: 
        Comment:
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
