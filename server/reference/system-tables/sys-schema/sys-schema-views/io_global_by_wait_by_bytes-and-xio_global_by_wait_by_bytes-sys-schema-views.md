---
description: >-
  These views summarize global I/O consumers by event name, displaying total
  bytes read and written to identify high-throughput events.
---

# io\_global\_by\_wait\_by\_bytes and x$io\_global\_by\_wait\_by\_bytes Sys Schema Views

{% include "../../../../.gitbook/includes/sys-schema-views-are-availa....md" %}

## Description

The `io_global_by_wait_by_bytes` and `x$io_global_by_wait_by_bytes` views summarize global I/O consumers, displaying amount of I/O and time waiting for I/O, grouped by event. Rows are sorted by descending total I/O (bytes read and written) by default.

The `io_global_by_wait_by_bytes` view is intended to be easier for human reading, while the `x$io_global_by_wait_by_bytes` view provides the data in raw form, intended for tools that process the data.

They contain the following columns:

| Column           | Description                                                     |
| ---------------- | --------------------------------------------------------------- |
| event\_name      | I/O event name. The wait/io/file prefix is stripped.            |
| total            | Total number of occurrences of the I/O event.                   |
| total\_latency   | Total wait time of timed occurrences of the I/O event           |
| min\_latency     | Minimum single wait time of timed occurrences of the I/O event. |
| avg\_latency     | Average wait time per timed occurrence of the I/O event.        |
| max\_latency     | Maximum single wait time of timed occurrences of the I/O event. |
| count\_read      | Total number of read I/O events for the file.                   |
| total\_read      | Total number of bytes read for the I/O event.                   |
| avg\_read        | Average number of bytes per read for the I/O event.             |
| count\_write     | Total number of write requests for the I/O event.               |
| total\_written   | Number of bytes written for the I/O event.                      |
| avg\_written     | Average number of bytes per write for the I/O event.            |
| total\_requested | Total number of bytes (read and write) for the I/O event.       |

## Example

```sql
SELECT * FROM sys.io_global_by_wait_by_bytes\G
*************************** 1. row ***************************
     event_name: innodb/innodb_data_file
          total: 220
  total_latency: 38.96 ms
    min_latency: 0 ps
    avg_latency: 177.09 us
    max_latency: 4.07 ms
     count_read: 174
     total_read: 4.73 MiB
       avg_read: 27.86 KiB
    count_write: 0
  total_written: 0 bytes
    avg_written: 0 bytes
total_requested: 4.73 MiB
*************************** 2. row ***************************
     event_name: aria/MAD
          total: 1107
  total_latency: 18.27 ms
    min_latency: 0 ps
    avg_latency: 16.50 us
    max_latency: 204.97 us
     count_read: 105
     total_read: 840.00 KiB
       avg_read: 8.00 KiB
    count_write: 0
  total_written: 0 bytes
    avg_written: 0 bytes
total_requested: 840.00 KiB

...

SELECT * FROM sys.x$io_global_by_wait_by_bytes\G
*************************** 1. row ***************************
     event_name: innodb/innodb_data_file
          total: 220
  total_latency: 38959722138
    min_latency: 0
    avg_latency: 177089374
    max_latency: 4065566778
     count_read: 174
     total_read: 4964352
       avg_read: 28530.7586
    count_write: 0
  total_written: 0
    avg_written: 0.0000
total_requested: 4964352
*************************** 2. row ***************************
     event_name: aria/MAD
          total: 1107
  total_latency: 18270683624
    min_latency: 0
    avg_latency: 16504546
    max_latency: 204973168
     count_read: 105
     total_read: 860160
       avg_read: 8192.0000
    count_write: 0
  total_written: 0
    avg_written: 0.0000
total_requested: 860160

...
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
