---
description: >-
  These views provide a breakdown of file I/O events by event type (e.g., read,
  write) for each host, helping to characterize the I/O workload.
---

# host\_summary\_by\_file\_io\_type and x$host\_summary\_by\_file\_io\_type Sys Schema Views

{% include "../../../../.gitbook/includes/sys-schema-views-are-availa....md" %}

## Description

The `host_summary_by_file_io_type` and `x$host_summary_by_file_io_type` views summarize file I/O, grouped by host and event type. Rows are sorted by host and descending total I/O latency by default. The `host_summary_by_file_io_type` view is intended to be easier for human reading, while the `x$host_summary_by_file_io_type` view provides the data in raw form, intended for tools that process the data.

They contain the following columns:

| Column         | Description                                                                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| host           | Host that the client connected from, or background for background threads (where the HOST column in the underlying Performance Schema table is NULL). |
| event\_name    | File I/O event name.                                                                                                                                  |
| total          | Total number of occurrences of the file I/O event for the host.                                                                                       |
| total\_latency | Total wait time of timed occurrences of the file I/O event for the host.                                                                              |
| max\_latency   | Maximum single wait time of timed occurrences of the file I/O event for the host.                                                                     |

## Example

```sql
SELECT * FROM sys.host_summary_by_file_io_type;
+------------+----------------------------------------------+-------+---------------+-------------+
| host       | event_name                                   | total | total_latency | max_latency |
+------------+----------------------------------------------+-------+---------------+-------------+
| background | wait/io/file/innodb/innodb_log_file          |    45 | 109.80 ms     | 26.48 ms    |
| background | wait/io/file/innodb/innodb_data_file         |   195 | 29.47 ms      | 1.23 ms     |
| background | wait/io/file/sql/global_ddl_log              |     4 | 4.45 ms       | 4.33 ms     |
...
| localhost  | wait/io/file/csv/data                        |     4 | 25.98 us      | 9.60 us     |
| localhost  | wait/io/file/partition/ha_partition::parfile |     1 | 14.19 us      | 14.19 us    |
| localhost  | wait/io/file/myisam/kfile                    |     1 | 11.95 us      | 11.95 us    |
+------------+----------------------------------------------+-------+---------------+-------------+

SELECT * FROM sys.x$host_summary_by_file_io_type;
+------------+----------------------------------------------+-------+---------------+-------------+
| host       | event_name                                   | total | total_latency | max_latency |
+------------+----------------------------------------------+-------+---------------+-------------+
| background | wait/io/file/innodb/innodb_log_file          |    45 |  109804643160 | 26478157582 |
| background | wait/io/file/innodb/innodb_data_file         |   195 |   29469738630 |  1226986584 |
| background | wait/io/file/sql/global_ddl_log              |     4 |    4447263252 |  4327780456 |
| localhost  | wait/io/file/csv/data                        |     4 |      25978718 |     9603922 |
| localhost  | wait/io/file/partition/ha_partition::parfile |     1 |      14191190 |    14191190 |
| localhost  | wait/io/file/myisam/kfile                    |     1 |      11954300 |    11954300 |
+------------+----------------------------------------------+-------+---------------+-------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
