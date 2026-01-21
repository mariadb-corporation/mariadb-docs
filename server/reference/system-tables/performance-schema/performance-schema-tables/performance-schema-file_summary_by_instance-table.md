---
description: >-
  This table summarizes file I/O events aggregated by file instance, providing
  granular I/O statistics for individual files.
---

# Performance Schema file\_summary\_by\_instance Table

The [Performance Schema](../) `file_summary_by_instance` table contains file events summarized by instance. It contains the following columns:

| Column                        | Description                                                                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FILE\_NAME                    | File name.                                                                                                                                                                              |
| EVENT\_NAME                   | Event name.                                                                                                                                                                             |
| OBJECT\_INSTANCE\_BEGIN       | Address in memory. Together with FILE\_NAME and EVENT\_NAME uniquely identifies a row.                                                                                                  |
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
SELECT * FROM file_summary_by_instance\G
...
*************************** 204. row ***************************
                FILE_NAME: /var/lib/mysql/test/db.opt
               EVENT_NAME: wait/io/file/sql/dbopt
    OBJECT_INSTANCE_BEGIN: 140578961971264
               COUNT_STAR: 6
           SUM_TIMER_WAIT: 39902495024
           MIN_TIMER_WAIT: 177888
           AVG_TIMER_WAIT: 6650415692
           MAX_TIMER_WAIT: 21026400404
               COUNT_READ: 1
           SUM_TIMER_READ: 21026400404
           MIN_TIMER_READ: 21026400404
           AVG_TIMER_READ: 21026400404
           MAX_TIMER_READ: 21026400404
 SUM_NUMBER_OF_BYTES_READ: 65
              COUNT_WRITE: 0
          SUM_TIMER_WRITE: 0
          MIN_TIMER_WRITE: 0
          AVG_TIMER_WRITE: 0
          MAX_TIMER_WRITE: 0
SUM_NUMBER_OF_BYTES_WRITE: 0
               COUNT_MISC: 5
           SUM_TIMER_MISC: 18876094620
           MIN_TIMER_MISC: 177888
           AVG_TIMER_MISC: 3775218924
           MAX_TIMER_MISC: 18864558060
*************************** 205. row ***************************
                FILE_NAME: /var/log/mysql/mariadb-bin.000157
               EVENT_NAME: wait/io/file/sql/binlog
    OBJECT_INSTANCE_BEGIN: 140578961971968
               COUNT_STAR: 6
           SUM_TIMER_WAIT: 73985877680
           MIN_TIMER_WAIT: 251136
           AVG_TIMER_WAIT: 12330979468
           MAX_TIMER_WAIT: 73846656340
               COUNT_READ: 0
           SUM_TIMER_READ: 0
           MIN_TIMER_READ: 0
           AVG_TIMER_READ: 0
           MAX_TIMER_READ: 0
 SUM_NUMBER_OF_BYTES_READ: 0
              COUNT_WRITE: 2
          SUM_TIMER_WRITE: 62583004
          MIN_TIMER_WRITE: 27630192
          AVG_TIMER_WRITE: 31291284
          MAX_TIMER_WRITE: 34952812
SUM_NUMBER_OF_BYTES_WRITE: 369
               COUNT_MISC: 4
           SUM_TIMER_MISC: 73923294676
           MIN_TIMER_MISC: 251136
           AVG_TIMER_MISC: 18480823560
           MAX_TIMER_MISC: 73846656340
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
