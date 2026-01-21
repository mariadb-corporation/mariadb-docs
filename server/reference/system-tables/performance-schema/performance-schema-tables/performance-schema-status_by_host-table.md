---
description: >-
  The status_by_host table aggregates session status variables by client host,
  useful for tracking activity levels from specific application servers.
---

# Performance Schema status\_by\_host Table

{% hint style="info" %}
The `status_by_host` table is available from MariaDB 10.5.2.
{% endhint %}

The `status_by_host` table contains status variable information by host. The table does not collect statistics for `Com_xxx` variables.

The table contains the following columns:

| Column          | Description                                     |
| --------------- | ----------------------------------------------- |
| HOST            | Host for which the status variable is reported. |
| VARIABLE\_NAME  | Status variable name.                           |
| VARIABLE\_VALUE | Aggregated status variable value                |

If [TRUNCATE TABLE](../../../sql-statements/table-statements/truncate-table.md) is run, will reset the aggregated host status from terminated sessions.

If [FLUSH STATUS](../../../sql-statements/administrative-sql-statements/flush-commands/flush.md) is run, session status from all active sessions are added to the global status variables, the status of all active sessions are reset, and values aggregated from disconnected sessions are reset.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
