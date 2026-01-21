---
description: >-
  The Information Schema INNODB_CHANGED_PAGES table lists pages that have been
  modified since a specific checkpoint.
---

# Information Schema INNODB\_CHANGED\_PAGES Table

The [Information Schema](../../) `INNODB_CHANGED_PAGES` Table contains data about modified pages from the bitmap file. It is updated at checkpoints by the log tracking thread parsing the log, so does not contain real-time data.

The number of records is limited by the value of the [innodb\_max\_changed\_pages](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) system variable.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column     | Description                                                           |
| ---------- | --------------------------------------------------------------------- |
| SPACE\_ID  | Modified page space id                                                |
| PAGE\_ID   | Modified page id                                                      |
| START\_LSN | Interval start after which page was changed (equal to checkpoint LSN) |
| END\_LSN   | Interval end before which page was changed (equal to checkpoint LSN)  |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
