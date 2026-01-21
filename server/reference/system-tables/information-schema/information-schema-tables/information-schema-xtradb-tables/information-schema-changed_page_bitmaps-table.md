---
description: >-
  The XTRADB_INTERNAL_HASH_TABLES table provides memory usage statistics for
  internal hash tables used by the XtraDB/InnoDB storage engine.
---

# Information Schema CHANGED\_PAGE\_BITMAPS Table

The [Information Schema](../../) `CHANGED_PAGE_BITMAPS` table is a dummy table added to [XtraDB](../../../../../server-usage/storage-engines/innodb/) with reset\_table callback to allow `FLUSH NO_WRITE_TO_BINLOG CHANGED_PAGE_BITMAPS` to be called from `innobackupex`. It contains only one column, _dummy_.

For more information, see [MDEV-7472](https://jira.mariadb.org/browse/MDEV-7472).

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
