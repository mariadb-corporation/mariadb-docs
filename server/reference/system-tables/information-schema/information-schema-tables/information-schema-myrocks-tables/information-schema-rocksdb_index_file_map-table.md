---
description: >-
  The Information Schema ROCKSDB_INDEX_FILE_MAP table maps MyRocks indexes to
  their corresponding SST files, useful for understanding data storage.
---

# Information Schema ROCKSDB\_INDEX\_FILE\_MAP Table

The [Information Schema](../../) `ROCKSDB_INDEX_FILE_MAP` table is included as part of the [MyRocks](../../../../../server-usage/storage-engines/myrocks/) storage engine.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It contains the following columns:

| Column                 | Description |
| ---------------------- | ----------- |
| COLUMN\_FAMILY         |             |
| INDEX\_NUMBER          |             |
| SST\_NAME              |             |
| NUM\_ROWS              |             |
| DATA\_SIZE             |             |
| ENTRY\_DELETES         |             |
| ENTRY\_SINGLEDELETES   |             |
| ENTRY\_MERGES          |             |
| ENTRY\_OTHERS          |             |
| DISTINCT\_KEYS\_PREFIX |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
