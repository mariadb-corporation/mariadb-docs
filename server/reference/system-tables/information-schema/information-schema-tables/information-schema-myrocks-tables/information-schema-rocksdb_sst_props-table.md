---
description: >-
  The Information Schema ROCKSDB_SST_PROPS table displays properties of SST
  files, such as data size and compression ratios, for MyRocks tables.
---

# Information Schema ROCKSDB\_SST\_PROPS Table

The [Information Schema](../../) `ROCKSDB_SST_PROPS` table is included as part of the [MyRocks](../../../../../server-usage/storage-engines/myrocks/) storage engine.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It contains the following columns:

| Column                  | Description |
| ----------------------- | ----------- |
| SST\_NAME               |             |
| COLUMN\_FAMILY          |             |
| DATA\_BLOCKS            |             |
| ENTRIES                 |             |
| RAW\_KEY\_SIZE          |             |
| RAW\_VALUE\_SIZE        |             |
| DATA\_BLOCK\_SIZE       |             |
| INDEX\_BLOCK\_SIZE      |             |
| INDEX\_PARTITIONS       |             |
| TOP\_LEVEL\_INDEX\_SIZE |             |
| FILTER\_BLOCK\_SIZE     |             |
| COMPRESSION\_ALGO       |             |
| CREATION\_TIME          |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
