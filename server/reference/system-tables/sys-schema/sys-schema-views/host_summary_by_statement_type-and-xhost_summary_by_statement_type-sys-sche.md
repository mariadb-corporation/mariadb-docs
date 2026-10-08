---
description: >-
  These views aggregate executed statements by type (e.g., SELECT, INSERT) and
  host, providing statistics on frequency and latency.
---

# host\_summary\_by\_statement\_type and x$host\_summary\_by\_statement\_type Sys Schema Views

{% include "../../../../.gitbook/includes/sys-schema-views-are-availa....md" %}

## Description

The `host_summary_by_statement_type` and `x$host_summary_by_statement_type` views summarize information about executed statements, grouped by host and statement type. Rows are sorted by host and descending total latency by default.

The `host_summary_by_statement_type` view is intended to be easier for human reading, while the `x$host_summary_by_statement_type` view provides the data in raw form, intended for tools that process the data.

They contain the following columns:

| Column         | Description                                                                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| host           | Host that the client connected from, or background for background threads (where the HOST column in the underlying Performance Schema table is NULL). |
| statement      | Final component of the statement event name, for example create\_table or select.                                                                     |
| total          | Total number of statement occurrences for the host.                                                                                                   |
| total\_latency | Total wait time of timed statements of the statement event for the host.                                                                              |
| max\_latency   | Maximum single wait time of timed occurrences of the statement event for the host.                                                                    |
| lock\_latency  | Total time spent by timed occurrences of the statement event for the host waiting for locks.                                                          |
| rows\_sent     | Total number of rows returned by occurrences of the statement event for the host.                                                                     |
| rows\_examined | Total number of rows read from storage engines by occurrences of the statement event for the host.                                                    |
| rows\_affected | Total number of rows affected by occurrences of the statement event for the host.                                                                     |
| full\_scans    | Total number of full table scans by occurrences of the statement event for the host.                                                                  |

## Example

```sql
SELECT * FROM sys.host_summary_by_statement_type\G
*************************** 1. row ***************************
         host: localhost
    statement: create_table
        total: 18
total_latency: 366.93 ms
  max_latency: 48.02 ms
 lock_latency: 3.16 ms
    rows_sent: 0
rows_examined: 0
rows_affected: 0
   full_scans: 0
*************************** 2. row ***************************
         host: localhost
    statement: select
        total: 27
total_latency: 339.16 ms
  max_latency: 64.51 ms
 lock_latency: 205.61 ms
    rows_sent: 750599937895926
rows_examined: 13925
rows_affected: 0
   full_scans: 21

...

SELECT * FROM sys.x$host_summary_by_statement_type\G
*************************** 1. row ***************************
         host: localhost
    statement: create_table
        total: 18
total_latency: 366927804000
  max_latency: 48023563000
 lock_latency: 3156000000
    rows_sent: 0
rows_examined: 0
rows_affected: 0
   full_scans: 0
*************************** 2. row ***************************
         host: localhost
    statement: select
        total: 28
total_latency: 343873182000
  max_latency: 64507216000
 lock_latency: 205984000000
    rows_sent: 750678474440767
rows_examined: 14370
rows_affected: 0
   full_scans: 22
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
