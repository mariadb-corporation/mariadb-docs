---
description: >-
  This function returns a JSON-formatted stack trace of all statements, stages,
  and events for a given thread, useful for deep diagnostics.
---

# ps\_thread\_stack

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.ps_thread_stack(thread_id, verbose)
```

## Description

`ps_thread_stack` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../) that, for a given _thread\_id_, returns all statements, stages, and events within the Performance Schema, as a JSON formatted stack.

The boolean _verbose_ argument specifies whether or not to include `file:lineno` information in the events.

## Examples

```sql
SELECT sys.ps_thread_stack(13, FALSE) AS thread_stack\G
*************************** 1. row ***************************
thread_stack: {"rankdir": "LR","nodesep": "0.10",
  "stack_created": "2022-03-28 16:01:06",
  "mysql_version": "10.8.2-MariaDB",
  "mysql_user": "msandbox@localhost",
  "events": []}
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
