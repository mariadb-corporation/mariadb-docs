---
description: >-
  The session_status table displays status variable values for the current
  session, providing data equivalent to the SHOW SESSION STATUS statement.
---

# Performance Schema session\_status Table

{% hint style="info" %}
The `session_status` table is available from MariaDB 10.5.2.
{% endhint %}

The `session_status` table contains a list of status variables for the current session. The table only stores status variable statistics for threads which are instrumented, and does not collect statistics for `Com_xxx` variables.

The table contains the following columns:

| Column          | Description                        |
| --------------- | ---------------------------------- |
| VARIABLE\_NAME  | The session status variable name.  |
| VARIABLE\_VALUE | The session status variable value. |

It is not possible to empty this table with a `TRUNCATE TABLE` statement.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
