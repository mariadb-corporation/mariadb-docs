---
description: >-
  These views summarize file I/O events grouped by client host, detailing total
  I/O counts and latency to identify hosts generating heavy disk traffic.
---

# host\_summary\_by\_file\_io and x$host\_summary\_by\_file\_io Sys Schema Views

{% include "../../../../.gitbook/includes/sys-schema-views-are-availa....md" %}

## Description

The `host_summary_by_file_io` and `x$host_summary_by_file_io` views summarize file I/O, grouped by host. Rows are sorted by descending total file I/O latency by default.

The `host_summary_by_file_io` view is intended to be easier for human reading, while the `and`x$host\_summary\_by\_file\_io`view provides the data in raw form, intended for tools that process the data.`

They contain the following columns:

| Column       | Description                                                                                                                                           |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| host         | Host that the client connected from, or background for background threads (where the HOST column in the underlying Performance Schema table is NULL). |
| ios          | Total file I/O events for the host.                                                                                                                   |
| ios\_latency | Total wait time of timed file I/O events for the host.                                                                                                |

## Example

```sql
SELECT * FROM sys.host_summary_by_file_io\G
*************************** 1. row ***************************
      host: localhost
       ios: 6526
io_latency: 490.28 ms
*************************** 2. row ***************************
      host: background
       ios: 457
io_latency: 151.39 ms

SELECT * FROM sys.x$host_summary_by_file_io\G
*************************** 1. row ***************************
      host: localhost
       ios: 6532
io_latency: 490447878974
*************************** 2. row ***************************
      host: background
       ios: 457
io_latency: 151388125856
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
