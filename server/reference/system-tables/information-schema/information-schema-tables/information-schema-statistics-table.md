---
description: >-
  The Information Schema STATISTICS table provides information about table
  indexes, serving as a standard-compliant alternative to SHOW INDEX.
---

# Information Schema STATISTICS Table

The [Information Schema](../) `STATISTICS` table provides information about table indexes.

It contains the following columns:

| Column         | Description                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TABLE\_CATALOG | Always def.                                                                                                                                                                                                                                                                                                                                                                                   |
| TABLE\_SCHEMA  | Database name.                                                                                                                                                                                                                                                                                                                                                                                |
| TABLE\_NAME    | Table name.                                                                                                                                                                                                                                                                                                                                                                                   |
| NON\_UNIQUE    | 1 if the index can have duplicates, 0 if not.                                                                                                                                                                                                                                                                                                                                                 |
| INDEX\_SCHEMA  | Database name.                                                                                                                                                                                                                                                                                                                                                                                |
| INDEX\_NAME    | Index name. The primary key is always named PRIMARY.                                                                                                                                                                                                                                                                                                                                          |
| SEQ\_IN\_INDEX | The column sequence number, starting at 1.                                                                                                                                                                                                                                                                                                                                                    |
| COLUMN\_NAME   | Column name.                                                                                                                                                                                                                                                                                                                                                                                  |
| COLLATION      | A for sorted in ascending order, or NULL for unsorted.                                                                                                                                                                                                                                                                                                                                        |
| CARDINALITY    | Estimate of the number of unique values stored in the index based on statistics stored as integers. Higher cardinalities usually mean a greater chance of the index being used in a join. Updated by the [ANALYZE TABLE](../../../sql-statements/table-statements/analyze-table.md) statement or [myisamchk -a](../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md). |
| SUB\_PART      | NULL if the whole column is indexed, or the number of indexed characters if partly indexed.                                                                                                                                                                                                                                                                                                   |
| PACKED         | NULL if not packed, otherwise how the index is packed.                                                                                                                                                                                                                                                                                                                                        |
| NULLABLE       | YES if the column may contain NULLs, empty string if not.                                                                                                                                                                                                                                                                                                                                     |
| INDEX\_TYPE    | Index type, one of BTREE, RTREE, HASH or FULLTEXT. See [Storage Engine Index Types](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/storage-engine-index-types.md).                                                                                                                                                                                           |
| COMMENT        | Index comments from the [CREATE INDEX](../../../sql-statements/data-definition/create/create-index.md) statement.                                                                                                                                                                                                                                                                             |
| IGNORED        | Whether or not an index will be ignored by the optimizer. See [Ignored Indexes](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/ignored-indexes.md). From [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes).                                                                   |

The [SHOW INDEX](../../../sql-statements/administrative-sql-statements/show/show-index.md) statement produces similar output.

## Example

```sql
SELECT * FROM INFORMATION_SCHEMA.STATISTICS\G
...
*************************** 85. row ***************************
TABLE_CATALOG: def
 TABLE_SCHEMA: test
   TABLE_NAME: table1
   NON_UNIQUE: 1
 INDEX_SCHEMA: test
   INDEX_NAME: col2
 SEQ_IN_INDEX: 1
  COLUMN_NAME: col2
    COLLATION: A
  CARDINALITY: 6
     SUB_PART: NULL
       PACKED: NULL
     NULLABLE: 
   INDEX_TYPE: BTREE
      COMMENT: 
INDEX_COMMENT:
...
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
