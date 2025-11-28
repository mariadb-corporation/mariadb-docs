---
description: >-
  The status_by_account table aggregates session status variables by client
  account, showing cumulative counters for specific user-host combinations.
---

# Performance Schema status\_by\_account Table

{% hint style="info" %}
The `status_by_account` table is available from MariaDB 10.5.2.
{% endhint %}

The `status_by_account` table contains status variable information by user/host account. The table does not collect statistics for `Com_xxx` variables.

The table contains the following columns:

| Column          | Description                                     |
| --------------- | ----------------------------------------------- |
| USER            | User for which the status variable is reported. |
| HOST            | Host for which the status variable is reported. |
| VARIABLE\_NAME  | Status variable name.                           |
| VARIABLE\_VALUE | Aggregated status variable value                |

If [TRUNCATE TABLE](../../../sql-statements/table-statements/truncate-table.md) is run, will aggregate the status from terminated sessions to user and host status, then reset the account status.

If [FLUSH STATUS](../../../sql-statements/administrative-sql-statements/flush-commands/) is run, session status from all active sessions are added to the global status variables, the status of all active sessions are reset, and values aggregated from disconnected sessions are reset.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
