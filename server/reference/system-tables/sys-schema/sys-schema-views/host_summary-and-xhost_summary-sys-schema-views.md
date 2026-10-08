---
description: >-
  The host_summary views provide a high-level overview of activity per client
  host, including statement counts, file I/O, and connection statistics.
---

# host\_summary and x$host\_summary Sys Schema Views

{% include "../../../../.gitbook/includes/sys-schema-views-are-availa....md" %}

## Description

The `host_summary` and `x$host_summary` views contain host activity information, grouped by host. The `host_summary` view is intended to be easier for human reading, while the `x$host_summary` view provides the data in raw form, intended for tools that process the data.

They contain the following columns:

| Column                   | Description                                                                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| host                     | Host that the client connected from, or background for background threads (where the HOST column in the underlying Performance Schema table is NULL). |
| statements               | Total number of statements for the host.                                                                                                              |
| statement\_latency       | Total wait time of timed statements for the host.                                                                                                     |
| statement\_avg\_latency  | Average wait time per timed statement for the host.                                                                                                   |
| table\_scans             | Total table scans for the host.                                                                                                                       |
| file\_ios                | Total file I/O events for the host.                                                                                                                   |
| file\_io\_latency        | Total wait time of timed file I/O events for the host.                                                                                                |
| current\_connections     | Current connections for the host.                                                                                                                     |
| total\_connections       | Total connections for the host.                                                                                                                       |
| unique\_users            | Number of distinct users for the host.                                                                                                                |
| current\_memory          | Current allocated memory for the host.                                                                                                                |
| total\_memory\_allocated | Total allocated memory for the host.                                                                                                                  |

## Example

```sql
SELECT * FROM sys.host_summary\G
*************************** 1. row ***************************
                  host: localhost
            statements: 59
     statement_latency: 148.11 ms
 statement_avg_latency: 2.51 ms
           table_scans: 11
              file_ios: 2065
       file_io_latency: 79.57 ms
   current_connections: 1
     total_connections: 3
          unique_users: 1
        current_memory: -2672 bytes
total_memory_allocated: 0 bytes

SELECT * FROM sys.x$host_summary\G
*************************** 1. row ***************************
                  host: localhost
            statements: 98
     statement_latency: 160926285000
 statement_avg_latency: 1642104948.9796
           table_scans: 12
              file_ios: 2071
       file_io_latency: 79742533755
   current_connections: 1
     total_connections: 3
          unique_users: 1
        current_memory: -2672
total_memory_allocated: 0
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
