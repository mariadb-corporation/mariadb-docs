---
description: >-
  The global_status table provides a persistent view of global server status
  variables, aggregating statistics across all threads.
---

# Performance Schema global\_status Table

{% hint style="info" %}
The `global_status` table is available from MariaDB 10.5.2.
{% endhint %}

The `global_status` table contains a list of status variables and their global values. The table only stores status variable statistics for threads which are instrumented, and does not collect statistics for `Com_xxx` variables.

The table contains the following columns:

| Column          | Description                       |
| --------------- | --------------------------------- |
| VARIABLE\_NAME  | The global status variable name.  |
| VARIABLE\_VALUE | The global status variable value. |

[TRUNCATE TABLE](../../../sql-statements/table-statements/truncate-table.md) resets global status variables, including thread, account, host, and user status, but not those that are never reset by the server.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
