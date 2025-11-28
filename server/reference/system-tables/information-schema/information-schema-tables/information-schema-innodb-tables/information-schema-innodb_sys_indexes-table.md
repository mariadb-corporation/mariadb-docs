---
description: >-
  The INNODB_SYS_INDEXES table provides metadata about InnoDB indexes, including
  the table they belong to, unique IDs, and type.
---

# Information Schema INNODB\_SYS\_INDEXES Table

The [Information Schema](../../) `INNODB_SYS_INDEXES` table contains information about InnoDB indexes.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Field            | Type                | Null | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------- | ------------------- | ---- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| INDEX\_ID        | bigint(21) unsigned | NO   | 0       | A unique index identifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| NAME             | varchar(64)         | NO   |         | Index name, lowercase for all user-created indexes, or uppercase for implicitly-created indexes; PRIMARY (primary key), GEN\_CLUST\_INDEX (index representing primary key where there isn't one), ID\_IND, FOR\_IND (validating foreign key constraint) , REF\_IND.                                                                                                                                                                                                           |
| TABLE\_ID        | bigint(21) unsigned | NO   | 0       | Table identifier, matching the value from [INNODB\_SYS\_TABLES.TABLE\_ID](information-schema-innodb_sys_tables-table.md).                                                                                                                                                                                                                                                                                                                                                     |
| TYPE             | int(11)             | NO   | 0       | Numeric type identifier; one of 0 (secondary index), 1 (clustered index), 2 (unique index), 3 (primary index), 32 ([full-text index](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/)).                                                                                                                                                                                                                                 |
| N\_FIELDS        | int(11)             | NO   | 0       | Number of columns in the index. GEN\_CLUST\_INDEX's have a value of 0 as the index is not based on an actual column in the table.                                                                                                                                                                                                                                                                                                                                             |
| PAGE\_NO         | int(11)             | NO   | 0       | Index B-tree's root page number. -1 (unused) for full-text indexes, as they are laid out over several auxiliary tables.                                                                                                                                                                                                                                                                                                                                                       |
| SPACE            | int(11)             | NO   | 0       | Tablespace identifier where the index resides. 0 represents the InnoDB system tablespace, while any other value represents a table created in file-per-table mode (see the [innodb\_file\_per\_table](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) system variable). Remains unchanged after a [TRUNCATE TABLE](../../../../sql-statements/table-statements/truncate-table.md) statement, and not necessarily unique. |
| MERGE\_THRESHOLD | int(11)             | NO   | 0       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Example

```sql
SELECT * FROM information_schema.INNODB_SYS_INDEXES LIMIT 3\G
*************************** 1. row ***************************
       INDEX_ID: 11
           NAME: ID_IND
       TABLE_ID: 11
           TYPE: 3
       N_FIELDS: 1
        PAGE_NO: 302
          SPACE: 0
MERGE_THRESHOLD: 50
*************************** 2. row ***************************
       INDEX_ID: 12
           NAME: FOR_IND
       TABLE_ID: 11
           TYPE: 0
       N_FIELDS: 1
        PAGE_NO: 303
          SPACE: 0
MERGE_THRESHOLD: 50
*************************** 3. row ***************************
       INDEX_ID: 13
           NAME: REF_IND
       TABLE_ID: 11
           TYPE: 3
       N_FIELDS: 1
        PAGE_NO: 304
          SPACE: 0
MERGE_THRESHOLD: 50
3 rows in set (0.00 sec)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
