---
description: >-
  The ps_trace_thread procedure captures a trace of Performance Schema
  instrumentation for a specific thread and dumps it to a .dot formatted graph
  file.
---

# ps\_trace\_thread

## Syntax

```
ps_trace_thread(thread_id, outfile, max_runtime, interval, start_fresh, auto_setup, debug)
```

## Description

`ps_trace_thread` is a [stored procedure](../../../../server-usage/stored-routines/stored-procedures/) available with the [Sys Schema](../).

Parameters:

* thread\_id `INT`: The thread to trace.
* outfile `VARCHAR(255)`: Name of the .dot file to be create.
* max\_runtime `DECIMAL(20,2)`: Maximum time in seconds to collect data. Fractional seconds can be used, and `NULL` results in data being collected for the default sixty seconds.
* interval `DECIMAL(20,2)`: Time in seconds to sleep between data collection. Fractional seconds can be used, and `NULL` results in the sleep being the default one second.
* start\_fresh `BOOLEAN`: Whether to reset all Performance Schema data before tracing.
* auto\_setup `BOOLEAN`: Whether to disable all other threads, enable all instruments and consumers, and reset the settings at the end of the run.
* debug `BOOLEAN`: Whether to include `file:lineno` information in the graph.

Dumps all Performance Schema data for an instrumented thread to a .dot formatted graph file (for use with the [DOT graph description language](https://en.wikipedia.org/wiki/DOT_\(graph_description_language\))). All returned result sets should be used for a complete graph.

Session [binary logging](../../../../server-management/server-monitoring-logs/binary-log/) is disabled during execution, by adjusting the [sql\_log\_bin](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sql_log_bin) session value (note the permissions required).

## Examples

```sql
CALL sys.ps_trace_thread(25, CONCAT('/tmp/stack-', REPLACE(NOW(), ' ', '-'), '.dot'), 
  NULL, NULL, TRUE, TRUE, TRUE);

--------------------+
| summary            |
+--------------------+
| Disabled 0 threads |
+--------------------+

+---------------------------------------------+
| Info                                        |
+---------------------------------------------+
| Data collection starting for THREAD_ID = 25 |
+---------------------------------------------+

+-----------------------------------------------------------+
| Info                                                      |
+-----------------------------------------------------------+
| Stack trace written to /tmp/stack-2023-04-05-19:06:29.dot |
+-----------------------------------------------------------+

+-------------------------------------------------------------------+
| Convert to PDF                                                    |
+-------------------------------------------------------------------+
| dot -Tpdf -o /tmp/stack_25.pdf /tmp/stack-2023-04-05-19:06:29.dot |
+-------------------------------------------------------------------+

+-------------------------------------------------------------------+
| Convert to PNG                                                    |
+-------------------------------------------------------------------+
| dot -Tpng -o /tmp/stack_25.png /tmp/stack-2023-04-05-19:06:29.dot |
+-------------------------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
