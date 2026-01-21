---
description: >-
  The Information Schema ROCKSDB_CF_OPTIONS table contains information about
  MyRocks column families, such as the column family name and option type.
---

# Information Schema ROCKSDB\_CF\_OPTIONS Table

The [Information Schema](../../) `ROCKSDB_CF_OPTIONS` table is included as part of the [MyRocks](../../../../../server-usage/storage-engines/myrocks/) storage engine, and contains infomation about MyRocks [column families](../../../../../server-usage/storage-engines/myrocks/myrocks-column-families.md).

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It contains the following columns:

| Column       | Description                                                                                           |
| ------------ | ----------------------------------------------------------------------------------------------------- |
| CF\_NAME     | [Column family](../../../../../server-usage/storage-engines/myrocks/myrocks-column-families.md) name. |
| OPTION\_TYPE |                                                                                                       |
| VALUE        |                                                                                                       |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
