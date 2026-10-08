---
description: >-
  These views display the most recent file I/O events, providing a real-time
  look at which files are being accessed by the server.
---

# latest\_file\_io and x$latest\_file\_io Sys Schema Views

{% include "../../../../.gitbook/includes/sys-schema-views-are-availa....md" %}

## Description

The `latest_file_io` and `x$latest_file_io` views summarize file I/O activity, grouped by file and thread. Rows are sorted by most recent I/O by default.

The `latest_file_io` view is intended to be easier for human reading, while the `x$latest_file_io` view provides the data in raw form, intended for tools that process the data.

They contain the following columns:

| Column | Description                                                                                                                                          |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| thread | Account associated with the thread for foreground threads (port number for TCP/IP connections), or thread name and thread ID for background threads. |

|           |                                                   |
| --------- | ------------------------------------------------- |
| total     | Total number of occurrences of the I/O event.     |
| file      | File path name.                                   |
| latency   | Wait time of the file I/O event.                  |
| operation | Type of operation                                 |
| requested | Number of bytes requested for the file I/O event. |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
