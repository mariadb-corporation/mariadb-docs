---
description: >-
  These views summarize global I/O consumers by event name, sorted by total
  latency, helping to pinpoint slow I/O event types.
---

# io\_global\_by\_wait\_by\_latency and x$io\_global\_by\_wait\_by\_latency Sys Schema Views

{% include "../../../../.gitbook/includes/sys-schema-views-are-availa....md" %}

## Description

The `io_global_by_wait_by_latency` and `x$io_global_by_wait_by_latency` views summarize global I/O consumers, displaying I/O and time waiting for I/O, grouped by event. Rows are sorted by descending total latency by default.

The `io_global_by_wait_by_latency` view is intended to be easier for human reading, while the `x$io_global_by_wait_by_latency` view provides the data in raw form, intended for tools that process the data.

They contain the following columns:

| Column           | Description                                                     |
| ---------------- | --------------------------------------------------------------- |
| event\_name      | I/O event name. The wait/io/file prefix is stripped.            |
| total            | Total number of occurrences of the I/O event.                   |
| total\_latency   | Total wait time of timed occurrences of the I/O event.          |
| min\_latency     | Minimum single wait time of timed occurrences of the I/O event. |
| avg\_latency     | Average wait time per timed occurrence of the I/O event.        |
| max\_latency     | Maximum single wait time of timed occurrences of the I/O event. |
| count\_read      | Total number of read request for the I/O event.                 |
| total\_read      | Total number of bytes read for the I/O event.                   |
| avg\_read        | Average number of bytes per read for the I/O event.             |
| count\_write     | Total number of write requests for the I/O event.               |
| total\_written   | Number of bytes written for the I/O event.                      |
| avg\_written     | Average number of bytes per write for the I/O event.            |
| total\_requested | Total number of bytes (read and write) for the I/O event.       |

## Example

```sql
SELECT * FROM sys.io_global_by_wait_by_latency\G
*************************** 1. row ***************************
   event_name: sql/global_ddl_log
        total: 223
total_latency: 288.66 ms
  avg_latency: 1.29 ms
  max_latency: 26.07 ms
 read_latency: 0 ps
write_latency: 2.59 ms
 misc_latency: 286.07 ms
   count_read: 0
   total_read: 0 bytes
     avg_read: 0 bytes
  count_write: 114
total_written: 220.17 KiB
  avg_written: 1.93 KiB
*************************** 2. row ***************************
   event_name: innodb/innodb_log_file
        total: 95
total_latency: 165.29 ms
  avg_latency: 1.74 ms
  max_latency: 26.48 ms
 read_latency: 61.04 us
write_latency: 1.31 ms
 misc_latency: 163.92 ms
   count_read: 6
   total_read: 66.50 KiB
     avg_read: 11.08 KiB
  count_write: 43
total_written: 81.00 KiB
  avg_written: 1.88 KiB
...

SELECT * FROM sys.x$io_global_by_wait_by_latency\G
*************************** 1. row ***************************
   event_name: sql/global_ddl_log
        total: 223
total_latency: 288663966666
  avg_latency: 1294456930
  max_latency: 26072142152
 read_latency: 0
write_latency: 2594925264
 misc_latency: 286069041402
   count_read: 0
   total_read: 0
     avg_read: 0.0000
  count_write: 114
total_written: 225459
  avg_written: 1977.7105
*************************** 2. row ***************************
   event_name: innodb/innodb_log_file
        total: 95
total_latency: 165291020006
  avg_latency: 1739905288
  max_latency: 26478157582
 read_latency: 61040974
write_latency: 1310187820
 misc_latency: 163919791212
   count_read: 6
   total_read: 68096
     avg_read: 11349.3333
  count_write: 43
total_written: 82944
  avg_written: 1928.9302
...
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
