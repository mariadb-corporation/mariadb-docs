---
description: >-
  The INNODB_SYS_TABLESPACES table provides metadata about the tablespaces used
  by InnoDB, including space ID, page size, and filename.
---

# Information Schema INNODB\_SYS\_TABLESPACES Table

The [Information Schema](../../) `INNODB_SYS_TABLESPACES` table contains information about InnoDB tablespaces. Until [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105) it was based on the internal `SYS_TABLESPACES` table. This internal table was removed in [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes), so this Information Schema table has been repurposed\
to directly reflect the filesystem (fil\_system.space\_list).

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SPACE           | Unique InnoDB tablespace identifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| NAME            | Database and table name separated by a backslash, or the uppercase InnoDB system table name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| FLAG            | 1 if a DATA DIRECTORY option has been specified in [CREATE TABLE](../../../../sql-statements/data-definition/create/create-table.md), otherwise 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| FILE\_FORMAT    | [InnoDB file format](../../../../../server-usage/storage-engines/innodb/innodb-file-format.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ROW\_FORMAT     | [InnoDB storage format](../../../../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md) used for this tablespace. If the [Antelope](../../../../../server-usage/storage-engines/innodb/innodb-file-format.md#antelope) file format is used, this value is always Compact or Redundant. When a table's [checksum algorithm](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm) is full\_crc32 (the default from [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105)), the value can only be Compressed or NULL. |
| PAGE\_SIZE      | Page size in bytes for this tablespace. Until [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0), this was the value of the [innodb\_page\_size](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_page_size) variable. From [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes), contains the physical page size of a page (previously ZIP\_PAGE\_SIZE).                                                                                                                                            |
| ZIP\_PAGE\_SIZE | Zip page size for this tablespace. Removed in [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SPACE\_TYPE     | Tablespace type. Can be General for general tablespaces or Single for file-per-table tablespaces. Removed [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0).                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| FS\_BLOCK\_SIZE | File system block size.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| FILE\_SIZE      | Maximum size of the file, uncompressed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ALLOCATED\_SIZE | Actual size of the file as per space allocated on disk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| FILENAME        | Tablespace datafile path, previously part of the [INNODB\_SYS\_DATAFILES table](information-schema-innodb_sys_datafiles-table.md). Added in [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes).                                                                                                                                                                                                                                                                                                                                                                                                |

## Examples

```sql
DESC information_schema.innodb_sys_tablespaces;
+----------------+---------------------+------+-----+---------+-------+
| Field          | Type                | Null | Key | Default | Extra |
+----------------+---------------------+------+-----+---------+-------+
| SPACE          | int(11) unsigned    | NO   |     | 0       |       |
| NAME           | varchar(655)        | NO   |     |         |       |
| FLAG           | int(11) unsigned    | NO   |     | 0       |       |
| ROW_FORMAT     | varchar(22)         | YES  |     | NULL    |       |
| PAGE_SIZE      | int(11) unsigned    | NO   |     | 0       |       |
| ZIP_PAGE_SIZE  | int(11) unsigned    | NO   |     | 0       |       |
| SPACE_TYPE     | varchar(10)         | YES  |     | NULL    |       |
| FS_BLOCK_SIZE  | int(11) unsigned    | NO   |     | 0       |       |
| FILE_SIZE      | bigint(21) unsigned | NO   |     | 0       |       |
| ALLOCATED_SIZE | bigint(21) unsigned | NO   |     | 0       |       |
+----------------+---------------------+------+-----+---------+-------+
```

```sql
SELECT * FROM information_schema.INNODB_SYS_TABLESPACES LIMIT 2\G
*************************** 1. row ***************************
         SPACE: 2
          NAME: mysql/innodb_table_stats
          FLAG: 33
    ROW_FORMAT: Dynamic
     PAGE_SIZE: 16384
 ZIP_PAGE_SIZE: 0
    SPACE_TYPE: Single
 FS_BLOCK_SIZE: 4096
     FILE_SIZE: 98304
ALLOCATED_SIZE: 98304
*************************** 2. row ***************************
         SPACE: 3
          NAME: mysql/innodb_index_stats
          FLAG: 33
    ROW_FORMAT: Dynamic
     PAGE_SIZE: 16384
 ZIP_PAGE_SIZE: 0
    SPACE_TYPE: Single
 FS_BLOCK_SIZE: 4096
     FILE_SIZE: 98304
ALLOCATED_SIZE: 98304
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
