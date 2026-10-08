---
description: >-
  The ps_thread_trx_info function returns a JSON object detailing the current
  transaction and executed statements for a specific thread.
---

# ps\_thread\_trx\_info

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.ps_thread_trx_info(thread_id)
```

## Description

`ps_thread_trx_info` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

It returns a JSON object with information about the thread specified by the given _thread\_id_. This information includes:

* the current transaction;
* executed statements (derived from the [Performance Schema events\_transactions\_current Table](../../performance-schema/performance-schema-tables/performance-schema-events_transactions_current-table.md) and the [Performance Schema events\_statements\_history Table](../../performance-schema/performance-schema-tables/performance-schema-events_statements_history-table.md) (full data will only returned if the consumers for those tables are enabled).

The maximum length of the returned JSON object is determined by the value of the [ps\_thread\_trx\_info.max\_length sys\_config option](../sys-schema-sys_config-table.md) (by default 65535). If the returned value exceeds this length, a JSON object error is returned.

## See Also

* [Sys Schema sys\_config Table](../sys-schema-sys_config-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
