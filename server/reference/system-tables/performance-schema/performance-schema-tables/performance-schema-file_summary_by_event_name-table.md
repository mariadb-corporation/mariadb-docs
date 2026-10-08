---
description: >-
  This table summarizes file I/O events aggregated by event name, detailing
  read/write counts and bytes transferred for each file type.
---

# Performance Schema file\_summary\_by\_event\_name Table

The [Performance Schema](../) `file_summary_by_event_name` table contains file events summarized by event name. It contains the following columns:

| Column                        | Description                                                                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EVENT\_NAME                   | Event name.                                                                                                                                                                             |
| COUNT\_STAR                   | Number of summarized events                                                                                                                                                             |
| SUM\_TIMER\_WAIT              | Total wait time of the summarized events that are timed.                                                                                                                                |
| MIN\_TIMER\_WAIT              | Minimum wait time of the summarized events that are timed.                                                                                                                              |
| AVG\_TIMER\_WAIT              | Average wait time of the summarized events that are timed.                                                                                                                              |
| MAX\_TIMER\_WAIT              | Maximum wait time of the summarized events that are timed.                                                                                                                              |
| COUNT\_READ                   | Number of all read operations, including FGETS, FGETC, FREAD, and READ.                                                                                                                 |
| SUM\_TIMER\_READ              | Total wait time of all read operations that are timed.                                                                                                                                  |
| MIN\_TIMER\_READ              | Minimum wait time of all read operations that are timed.                                                                                                                                |
| AVG\_TIMER\_READ              | Average wait time of all read operations that are timed.                                                                                                                                |
| MAX\_TIMER\_READ              | Maximum wait time of all read operations that are timed.                                                                                                                                |
| SUM\_NUMBER\_OF\_BYTES\_READ  | Bytes read by read operations.                                                                                                                                                          |
| COUNT\_WRITE                  | Number of all write operations, including FPUTS, FPUTC, FPRINTF, VFPRINTF, FWRITE, and PWRITE.                                                                                          |
| SUM\_TIMER\_WRITE             | Total wait time of all write operations that are timed.                                                                                                                                 |
| MIN\_TIMER\_WRITE             | Minimum wait time of all write operations that are timed.                                                                                                                               |
| AVG\_TIMER\_WRITE             | Average wait time of all write operations that are timed.                                                                                                                               |
| MAX\_TIMER\_WRITE             | Maximum wait time of all write operations that are timed.                                                                                                                               |
| SUM\_NUMBER\_OF\_BYTES\_WRITE | Bytes written by write operations.                                                                                                                                                      |
| COUNT\_MISC                   | Number of all miscellaneous operations not counted above, including CREATE, DELETE, OPEN, CLOSE, STREAM\_OPEN, STREAM\_CLOSE, SEEK, TELL, FLUSH, STAT, FSTAT, CHSIZE, RENAME, and SYNC. |
| SUM\_TIMER\_MISC              | Total wait time of all miscellaneous operations that are timed.                                                                                                                         |
| MIN\_TIMER\_MISC              | Minimum wait time of all miscellaneous operations that are timed.                                                                                                                       |
| AVG\_TIMER\_MISC              | Average wait time of all miscellaneous operations that are timed.                                                                                                                       |
| MAX\_TIMER\_MISC              | Maximum wait time of all miscellaneous operations that are timed.                                                                                                                       |

I/O operations can be avoided by caching, in which case they will not be recorded in this table.

You can [TRUNCATE](../../../sql-statements/table-statements/truncate-table.md) the table, which will reset all counters to zero.

## Example

```sql
SELECT * FROM file_summary_by_event_name\G
...
*************************** 49. row ***************************
               EVENT_NAME: wait/io/file/aria/MAD
               COUNT_STAR: 60
           SUM_TIMER_WAIT: 397234368
           MIN_TIMER_WAIT: 0
           AVG_TIMER_WAIT: 6620224
           MAX_TIMER_WAIT: 16808672
               COUNT_READ: 0
           SUM_TIMER_READ: 0
           MIN_TIMER_READ: 0
           AVG_TIMER_READ: 0
           MAX_TIMER_READ: 0
 SUM_NUMBER_OF_BYTES_READ: 0
              COUNT_WRITE: 0
          SUM_TIMER_WRITE: 0
          MIN_TIMER_WRITE: 0
          AVG_TIMER_WRITE: 0
          MAX_TIMER_WRITE: 0
SUM_NUMBER_OF_BYTES_WRITE: 0
               COUNT_MISC: 60
           SUM_TIMER_MISC: 397234368
           MIN_TIMER_MISC: 0
           AVG_TIMER_MISC: 6620224
           MAX_TIMER_MISC: 16808672
*************************** 50. row ***************************
               EVENT_NAME: wait/io/file/aria/control
               COUNT_STAR: 3
           SUM_TIMER_WAIT: 24055778544
           MIN_TIMER_WAIT: 0
           AVG_TIMER_WAIT: 8018592848
           MAX_TIMER_WAIT: 24027262400
               COUNT_READ: 1
           SUM_TIMER_READ: 24027262400
           MIN_TIMER_READ: 0
           AVG_TIMER_READ: 24027262400
           MAX_TIMER_READ: 24027262400
 SUM_NUMBER_OF_BYTES_READ: 52
              COUNT_WRITE: 0
          SUM_TIMER_WRITE: 0
          MIN_TIMER_WRITE: 0
          AVG_TIMER_WRITE: 0
          MAX_TIMER_WRITE: 0
SUM_NUMBER_OF_BYTES_WRITE: 0
               COUNT_MISC: 2
           SUM_TIMER_MISC: 28516144
           MIN_TIMER_MISC: 0
           AVG_TIMER_MISC: 14258072
           MAX_TIMER_MISC: 27262208
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
