---
description: >-
  The Information Schema ROCKSDB_PERF_CONTEXT table contains performance
  counters for the current session, providing granular metrics on RocksDB
  operations.
---

# Information Schema ROCKSDB\_PERF\_CONTEXT Table

The [Information Schema](../../) `ROCKSDB_PERF_CONTEXT` table is included as part of the [MyRocks](../../../../../server-usage/storage-engines/myrocks/) storage engine and includes per-table/partition counters .

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It contains the following columns:

| Column          | Description |
| --------------- | ----------- |
| TABLE\_SCHEMA   |             |
| TABLE\_NAME     |             |
| PARTITION\_NAME |             |
| STAT\_TYPE      |             |
| VALUE           |             |

Note: for multi-table queries, all counter increments are "billed" to the first table in the query:[1018](https://github.com/facebook/mysql-5.6/issues/1018)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
