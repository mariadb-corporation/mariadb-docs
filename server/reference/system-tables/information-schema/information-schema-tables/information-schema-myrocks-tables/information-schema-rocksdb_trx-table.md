---
description: >-
  The Information Schema ROCKSDB_TRX table provides information about active
  transactions in MyRocks, including transaction IDs and states.
---

# Information Schema ROCKSDB\_TRX Table

The [Information Schema](../../) `ROCKSDB_TRX` table is included as part of the [MyRocks](../../../../../server-usage/storage-engines/myrocks/) storage engine.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It contains the following columns:

| Column                      | Description |
| --------------------------- | ----------- |
| TRANSACTION\_ID             |             |
| STATE                       |             |
| NAME                        |             |
| WRITE\_COUNT                |             |
| LOCK\_COUNT                 |             |
| TIMEOUT\_SEC                |             |
| WAITING\_KEY                |             |
| WAITING\_COLUMN\_FAMILY\_ID |             |
| IS\_REPLICATION             |             |
| SKIP\_TRX\_API              |             |
| READ\_ONLY                  |             |
| HAS\_DEADLOCK\_DETECTION    |             |
| NUM\_ONGOING\_BULKLOAD      |             |
| THREAD\_ID                  |             |
| QUERY                       |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
