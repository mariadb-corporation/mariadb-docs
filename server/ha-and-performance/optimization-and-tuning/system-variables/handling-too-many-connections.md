---
description: >-
  How to handle and avoid the 'too many connections' error on busy servers.
---


# Handling Too Many Connections

Systems that get too busy can return the `too_many_connections` error.


When the number of [threads_connected](server-status-variables.md#threads_connected) exceeds the [max_connections](server-system-variables.md#max_connections) server variable, it's time to make a change. Viewing the [threads_connected](server-status-variables.md#threads_connected) status variable shows only the current number of connections, but it's more useful to see what the value has peaked at, and this is shown by the [max_used_connections](server-status-variables.md#max_used_connections) status variable.


This error may be a symptom of slow queries and other bottlenecks, but if the system is running smoothly this can be addressed by increasing the value of max_connections.


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
