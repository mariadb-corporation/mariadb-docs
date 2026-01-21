---
description: >-
  The status_by_thread table lists session status variables for each active
  thread, effectively providing a "SHOW SESSION STATUS" for every connection.
---

# Performance Schema status\_by\_thread Table

{% hint style="info" %}
The `session_status` table is available from MariaDB 10.5.2.
{% endhint %}

The `status_by_thread` table contains status variable information about active foreground threads. The table does not collect statistics for `Com_xxx` variables.

The table contains the following columns:

| Column          | Description                                                                   |
| --------------- | ----------------------------------------------------------------------------- |
| THREAD\_ID      | The thread identifier of the session in which the status variable is defined. |
| VARIABLE\_NAME  | Status variable name.                                                         |
| VARIABLE\_VALUE | Aggregated status variable value.                                             |

If [TRUNCATE TABLE](../../../sql-statements/table-statements/truncate-table.md) is run, will aggregate the status for all threads to the global status and account status, then reset the thread status. If account statistics are not collected but host and user status are, the session status is added to host and user status.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
