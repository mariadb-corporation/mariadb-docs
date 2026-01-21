---
description: >-
  The INNODB_SYS_TABLES table exposes the internal InnoDB data dictionary
  metadata for tables, including row formats and space IDs.
---

# Information Schema INNODB\_SYS\_TABLES Table

The [Information Schema](../../) `INNODB_SYS_TABLES` table contains information about InnoDB tables.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Field           | Type                                                                                                 | Null | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TABLE\_ID       | bigint(21) unsigned                                                                                  | NO   | 0       | Unique InnoDB table identifier.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| NAME            | varchar(655)                                                                                         | NO   |         | Database and table name, or the uppercase InnoDB system table name.                                                                                                                                                                                                                                                                                                                                                                               |
| FLAG            | int(11)                                                                                              | NO   | 0       | See [Flag](information-schema-innodb_sys_tables-table.md#flag) below                                                                                                                                                                                                                                                                                                                                                                              |
| N\_COLS         | int(11) unsigned (>= MariaDB 10.5) int(11) (<= MariaDB 10.4)                                         | NO   | 0       | Number of columns in the table. The count includes two or three hidden InnoDB system columns, appended to the end of the column list: DB\_ROW\_ID (if there is no primary key or unique index on NOT NULL columns), DB\_TRX\_ID, DB\_ROLL\_PTR.                                                                                                                                                                                                   |
| SPACE           | int(11) unsigned (>= MariaDB 10.5) int(11) (<= MariaDB 10.4)                                         | NO   | 0       | Tablespace identifier where the index resides. 0 represents the InnoDB system tablespace, while any other value represents a table created in file-per-table mode (see the [innodb\_file\_per\_table](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) system variable). Remains unchanged after a [TRUNCATE TABLE](../../../../sql-statements/table-statements/truncate-table.md) statement. |
| FILE\_FORMAT    | varchar(10)                                                                                          | YES  | NULL    | [InnoDB file format](../../../../../server-usage/storage-engines/innodb/innodb-file-format.md) (Antelope or Barracuda).                                                                                                                                                                                                                                                                                                                           |
| ROW\_FORMAT     | enum('Redundant', 'Compact', 'Compressed', 'Dynamic') (>= MariaDB 10.5)varchar(12) (<= MariaDB 10.4) | YES  | NULL    | [InnoDB storage format](../../../../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md) (Compact, Redundant, Dynamic, or Compressed).                                                                                                                                                                                                                                                                       |
| ZIP\_PAGE\_SIZE | int(11) unsigned                                                                                     | NO   | 0       | For Compressed tables, the zipped page size.                                                                                                                                                                                                                                                                                                                                                                                                      |
| SPACE\_TYPE     | enum('Single','System') (>= MariaDB 10.5)varchar(10) (<= MariaDB 10.4)                               | YES  | NULL    |                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Flag

The flag field returns the dict\_table\_t::flags that correspond to the data dictionary record.

| Bit     | Description                                                                                                      |
| ------- | ---------------------------------------------------------------------------------------------------------------- |
| 0       | Set if ROW\_FORMAT is not REDUNDANT.                                                                             |
| 1 to 4  | 0, except for ROW\_FORMAT=COMPRESSED, where they will determine the KEY\_BLOCK\_SIZE (the compressed page size). |
| 5       | Set for ROW\_FORMAT=DYNAMIC or ROW\_FORMAT=COMPRESSED.                                                           |
| 6       | Set if the DATA DIRECTORY attribute was present when the table was originally created.                           |
| 7       | Set if the page\_compressed attribute is present.                                                                |
| 8 to 11 | Determine the page\_compression\_level.                                                                          |
| 12 13   | Normally `00`, but `11` for "no-rollback tables".                                                                |

Note that the table flags returned here are not the same as tablespace flags (FSP\_SPACE\_FLAGS).

## Example

```sql
SELECT * FROM information_schema.INNODB_SYS_TABLES LIMIT 2\G
*************************** 1. row ***************************
     TABLE_ID: 14
         NAME: SYS_DATAFILES
         FLAG: 0
       N_COLS: 5
        SPACE: 0
   ROW_FORMAT: Redundant
ZIP_PAGE_SIZE: 0
   SPACE_TYPE: System
*************************** 2. row ***************************
     TABLE_ID: 11
         NAME: SYS_FOREIGN
         FLAG: 0
       N_COLS: 7
        SPACE: 0
   ROW_FORMAT: Redundant
ZIP_PAGE_SIZE: 0
   SPACE_TYPE: System
2 rows in set (0.00 sec)
```

## See Also

* [InnoDB Data Dictionary Troubleshooting](../../../../../server-usage/storage-engines/innodb/innodb-troubleshooting/innodb-data-dictionary-troubleshooting.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
