---
description: >-
  The Information Schema ROCKSDB_DEADLOCK table provides information about
  deadlocks that have occurred within the MyRocks storage engine.
---

# Information Schema ROCKSDB\_DEADLOCK Table

The [Information Schema](../../) `ROCKSDB_DEADLOCK` table is included as part of the [MyRocks](../../../../../server-usage/storage-engines/myrocks/) storage engine.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It contains the following columns:

| Column          | Description |
| --------------- | ----------- |
| DEADLOCK\_ID    |             |
| TIMESTAMP       |             |
| TRANSACTION\_ID |             |
| CF\_NAME        |             |
| WAITING\_KEY    |             |
| LOCK\_TYPE      |             |
| INDEX\_NAME     |             |
| TABLE\_NAME     |             |
| ROLLED\_BACK    |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
