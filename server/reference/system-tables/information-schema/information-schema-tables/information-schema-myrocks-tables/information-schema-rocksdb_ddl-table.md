---
description: >-
  The Information Schema ROCKSDB_DDL table contains information about Data
  Definition Language (DDL) operations in MyRocks, including table and index
  names.
---

# Information Schema ROCKSDB\_DDL Table

The [Information Schema](../../) `ROCKSDB_DDL` table is included as part of the [MyRocks](../../../../../server-usage/storage-engines/myrocks/) storage engine.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It contains the following columns:

| Column              | Description |
| ------------------- | ----------- |
| TABLE\_SCHEMA       |             |
| TABLE\_NAME         |             |
| PARTITION\_NAME     |             |
| INDEX\_NAME         |             |
| COLUMN\_FAMILY      |             |
| INDEX\_NUMBER       |             |
| INDEX\_TYPE         |             |
| KV\_FORMAT\_VERSION |             |
| TTL\_DURATION       |             |
| INDEX\_FLAGS        |             |
| CF                  |             |
| AUTO\_INCREMENT     |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
