---
description: >-
  The XTRADB_RSEG table contains detailed information about the rollback
  segments used by XtraDB for undo logging and MVCC.
---

# Information Schema XTRADB\_RSEG Table

The [Information Schema](../../) `XTRADB_RSEG` table contains information about the XtraDB rollback segments.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column     | Description                                                         |
| ---------- | ------------------------------------------------------------------- |
| rseg\_id   | Rollback segment id.                                                |
| space\_id  | Space where the segment is placed.                                  |
| zip\_size  | Size in bytes of the compressed page size, or zero if uncompressed. |
| page\_no   | Page number of the segment header.                                  |
| max\_size  | Maximum size in pages.                                              |
| curr\_size | Current size in pages.                                              |

The number of records will match the value set in the [innodb\_undo\_logs](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_undo_logs) variable (by default 128).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
