---
description: >-
  The Information Schema TABLES table provides metadata about tables in
  databases, including row counts, storage engines, and creation times.
---

# Information Schema TABLES Table

{% tabs %}
{% tab title="Current" %}
The [Information Schema](../) table shows information about the various tables and [views](../../../../server-usage/views/) on the server.
{% endtab %}

{% tab title="< 11.2.0" %}
The [Information Schema](../) table shows information about the various tables, excluding`TEMPORARY` tables, except for tables from the `Information Schema` database) and [views](../../../../server-usage/views/) on the server.
{% endtab %}
{% endtabs %}

It contains the following columns:

| Column             | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TABLE\_CATALOG     | Always def.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| TABLE\_SCHEMA      | Database name.                                                                                                                                                                                                                                                                                                                                                                                                                |
| TABLE\_NAME        | Table name.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| TABLE\_TYPE        | One of `BASE TABLE` for a regular table, VIEW for a [view](../../../../server-usage/views/), `SYSTEM VIEW` for [Information Schema](../) tables, `SYSTEM VERSIONED` for [system-versioned tables](../../../sql-structure/temporal-tables/system-versioned-tables.md), `SEQUENCE` for [sequences](../../../sql-structure/sequences/) or `TEMPORARY` for local temporary tables.                                                |
| ENGINE             | [Storage Engine](../../../../server-usage/storage-engines/).                                                                                                                                                                                                                                                                                                                                                                  |
| VERSION            | Version number from the table's .frm file                                                                                                                                                                                                                                                                                                                                                                                     |
| ROW\_FORMAT        | Row format (see [InnoDB](../../../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md), [Aria](../../../../server-usage/storage-engines/aria/aria-storage-formats.md) and [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/myisam-storage-formats.md) row formats).                                                                                               |
| TABLE\_ROWS        | Number of rows in the table. Some engines, such as [XtraDB and InnoDB](../../../../server-usage/storage-engines/innodb/) may store an estimate.                                                                                                                                                                                                                                                                               |
| AVG\_ROW\_LENGTH   | Average row length in the table.                                                                                                                                                                                                                                                                                                                                                                                              |
| DATA\_LENGTH       | For [InnoDB/XtraDB](../../../../server-usage/storage-engines/innodb/), the index size, in pages, multiplied by the page size. For [Aria](../../../../server-usage/storage-engines/aria/) and [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/), length of the data file, in bytes. For [MEMORY](../../../../server-usage/storage-engines/memory-storage-engine.md), the approximate allocated memory. |
| MAX\_DATA\_LENGTH  | Maximum length of the data file, ie the total number of bytes that could be stored in the table. Not used in [XtraDB and InnoDB](../../../../server-usage/storage-engines/innodb/).                                                                                                                                                                                                                                           |
| INDEX\_LENGTH      | Length of the index file.                                                                                                                                                                                                                                                                                                                                                                                                     |
| DATA\_FREE         | Bytes allocated but unused. For [InnoDB](../../../../server-usage/storage-engines/innodb/) tables in a shared tablespace, the free space of the shared tablespace with small safety margin. An estimate in the case of partitioned tables - see the [PARTITIONS](information-schema-partitions-table.md) table.                                                                                                               |
| AUTO\_INCREMENT    | Next [AUTO\_INCREMENT](../../../data-types/auto_increment.md) value.                                                                                                                                                                                                                                                                                                                                                          |
| CREATE\_TIME       | Time the table was created. Some engines just return the ctime information from the file system layer here, in that case the value is not necessarily the table creation time but rather the time the file system metadata for it had last changed.                                                                                                                                                                           |
| UPDATE\_TIME       | Time the table was last updated. On Windows, the timestamp is not updated on update, so MyISAM values will be inaccurate. In [InnoDB](../../../../server-usage/storage-engines/innodb/), if shared tablespaces are used, will be NULL, while buffering can also delay the update, so the value will differ from the actual time of the last UPDATE, INSERT or DELETE.                                                         |
| CHECK\_TIME        | Time the table was last checked. Not kept by all storage engines, in which case will be NULL.                                                                                                                                                                                                                                                                                                                                 |
| TABLE\_COLLATION   | [Character set and collation](../../../data-types/string-data-types/character-sets/).                                                                                                                                                                                                                                                                                                                                         |
| CHECKSUM           | Live checksum value, if any.                                                                                                                                                                                                                                                                                                                                                                                                  |
| CREATE\_OPTIONS    | Extra [CREATE TABLE](../../../sql-statements/data-definition/create/create-table.md) options.                                                                                                                                                                                                                                                                                                                                 |
| TABLE\_COMMENT     | Table comment provided when MariaDB created the table.                                                                                                                                                                                                                                                                                                                                                                        |
| MAX\_INDEX\_LENGTH | Maximum index length (supported by MyISAM and Aria tables).                                                                                                                                                                                                                                                                                                                                                                   |
| TEMPORARY          | Is set to "Y" for local temporary tables.                                                                                                                                                                                                                                                                                                                                                                                     |

Although the table is standard in the Information Schema, all but `TABLE_CATALOG`, `TABLE_SCHEMA`, `TABLE_NAME`, `TABLE_TYPE`, `ENGINE` and `VERSION` are MySQL and MariaDB extensions.

[SHOW TABLES](../../../sql-statements/administrative-sql-statements/show/show-tables.md) lists all tables in a database.

## Examples

```sql
SELECT * FROM information_schema.tables WHERE table_schema='test'\G
*************************** 1. row ***************************
   TABLE_CATALOG: def
    TABLE_SCHEMA: test
      TABLE_NAME: xx5
      TABLE_TYPE: BASE TABLE
          ENGINE: InnoDB
         VERSION: 10
      ROW_FORMAT: Dynamic
      TABLE_ROWS: 0
  AVG_ROW_LENGTH: 0
     DATA_LENGTH: 16384
 MAX_DATA_LENGTH: 0
    INDEX_LENGTH: 0
       DATA_FREE: 0
  AUTO_INCREMENT: NULL
     CREATE_TIME: 2020-11-18 15:57:10
     UPDATE_TIME: NULL
      CHECK_TIME: NULL
 TABLE_COLLATION: latin1_swedish_ci
        CHECKSUM: NULL
  CREATE_OPTIONS: 
   TABLE_COMMENT: 
MAX_INDEX_LENGTH: 0
       TEMPORARY: N
*************************** 2. row ***************************
   TABLE_CATALOG: def
    TABLE_SCHEMA: test
      TABLE_NAME: xx4
      TABLE_TYPE: BASE TABLE
          ENGINE: MyISAM
         VERSION: 10
      ROW_FORMAT: Fixed
      TABLE_ROWS: 0
  AVG_ROW_LENGTH: 0
     DATA_LENGTH: 0
 MAX_DATA_LENGTH: 1970324836974591
    INDEX_LENGTH: 1024
       DATA_FREE: 0
  AUTO_INCREMENT: NULL
     CREATE_TIME: 2020-11-18 15:56:57
     UPDATE_TIME: 2020-11-18 15:56:57
      CHECK_TIME: NULL
 TABLE_COLLATION: latin1_swedish_ci
        CHECKSUM: NULL
  CREATE_OPTIONS: 
   TABLE_COMMENT: 
MAX_INDEX_LENGTH: 17179868160
       TEMPORARY: N
...
```

Example with temporary = 'y':

```sql
SELECT * FROM information_schema.tables WHERE temporary='y'\G
 *************************** 1. row ***************************
   TABLE_CATALOG: def
    TABLE_SCHEMA: information_schema
      TABLE_NAME: INNODB_FT_DELETED
      TABLE_TYPE: SYSTEM VIEW
          ENGINE: MEMORY
         VERSION: 11
      ROW_FORMAT: Fixed
      TABLE_ROWS: NULL
  AVG_ROW_LENGTH: 9
     DATA_LENGTH: 0
 MAX_DATA_LENGTH: 9437184
    INDEX_LENGTH: 0
       DATA_FREE: 0
  AUTO_INCREMENT: NULL
     CREATE_TIME: 2020-11-17 21:54:02
     UPDATE_TIME: NULL
      CHECK_TIME: NULL
 TABLE_COLLATION: utf8_general_ci
        CHECKSUM: NULL
  CREATE_OPTIONS: max_rows=1864135
   TABLE_COMMENT: 
MAX_INDEX_LENGTH: 0
       TEMPORARY: Y
...
```

### View Tables in Order of Size

Returns a list of all tables in the database, ordered by size:

```sql
SELECT table_schema AS `DB`, table_name AS `TABLE`, 
  ROUND(((data_length + index_length) / 1024 / 1024), 2) `Size (MB)` 
  FROM information_schema.TABLES 
  ORDER BY (data_length + index_length) DESC;

+--------------------+---------------------------------------+-----------+
| DB                 | Table                                 | Size (MB) |
+--------------------+---------------------------------------+-----------+
| wordpress          | wp_simple_history_contexts            |      7.05 |
| wordpress          | wp_posts                              |      6.59 |
| wordpress          | wp_simple_history                     |      3.05 |
| wordpress          | wp_comments                           |      2.73 |
| wordpress          | wp_commentmeta                        |      2.47 |
| wordpress          | wp_simple_login_log                   |      2.03 |
...
```

Returns information about a temporary table:

```sql
CREATE TEMPORARY TABLE foo.t1 (a INT);

SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='foo' AND TEMPORARY='y'\G
*************************** 1. row ***************************
   TABLE_CATALOG: def
    TABLE_SCHEMA: foo
      TABLE_NAME: t1
      TABLE_TYPE: TEMPORARY
...
       TEMPORARY: Y
```

## See Also

* [mysqlshow](../../../../clients-and-utilities/legacy-clients-and-utilities/mysqlshow.md)
* [SHOW TABLE STATUS](../../../sql-statements/administrative-sql-statements/show/show-table-status.md)
* [Finding Tables Without Primary Keys](../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#finding-tables-without-primary-keys)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
