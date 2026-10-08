---
description: >-
  The Information Schema ROCKSDB_LOCKS table displays information about locks
  currently held or requested by MyRocks transactions.
---

# Information Schema ROCKSDB\_LOCKS Table

The [Information Schema](../../) `ROCKSDB_LOCKS` table is included as part of the [MyRocks](../../../../../server-usage/storage-engines/myrocks/) storage engine.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It contains the following columns:

| Column             | Description |
| ------------------ | ----------- |
| COLUMN\_FAMILY\_ID |             |
| TRANSACTION\_ID    |             |
| KEY                |             |
| MODE               |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
