---
description: >-
  The ps_is_thread_instrumented function checks whether a specific thread ID is
  currently instrumented by the Performance Schema.
---

# ps\_is\_thread\_instrumented

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.ps_is_thread_instrumented(connection_id)
```

## Description

`ps_is_thread_instrumented` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../) that returns whether or not Performance Schema instrumentation for the given _connection\_id_ is enabled.

* `YES` - instrumentation is enabled
* `NO` - instrumentation is not enabled
* `UNKNOWN` - the connection ID is unknown
* `NULL` - `NULL` value

## Examples

```sql
SELECT sys.ps_is_thread_instrumented(CONNECTION_ID());
+------------------------------------------------+
| sys.ps_is_thread_instrumented(CONNECTION_ID()) |
+------------------------------------------------+
| YES                                            |
+------------------------------------------------+

SELECT sys.ps_is_thread_instrumented(2042);
+-------------------------------------+
| sys.ps_is_thread_instrumented(2042) |
+-------------------------------------+
| UNKNOWN                             |
+-------------------------------------+

SELECT sys.ps_is_thread_instrumented(NULL);
+-------------------------------------+
| sys.ps_is_thread_instrumented(NULL) |
+-------------------------------------+
| NULL                                |
+-------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
