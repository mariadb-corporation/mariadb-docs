---
description: >-
  This table summarizes socket I/O events aggregated by event name, showing
  execution counts and wait times for operations like send and receive.
---

# Performance Schema socket\_summary\_by\_event\_name Table

It aggregates timer and byte count statistics for all socket I/O operations by socket instrument.

| Column                        | Description                                                                                                       |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| EVENT\_NAME                   | Socket instrument.                                                                                                |
| COUNT\_STAR                   | Number of summarized events                                                                                       |
| SUM\_TIMER\_WAIT              | Total wait time of the summarized events that are timed.                                                          |
| MIN\_TIMER\_WAIT              | Minimum wait time of the summarized events that are timed.                                                        |
| AVG\_TIMER\_WAIT              | Average wait time of the summarized events that are timed.                                                        |
| MAX\_TIMER\_WAIT              | Maximum wait time of the summarized events that are timed.                                                        |
| COUNT\_READ                   | Number of all read operations, including RECV, RECVFROM, and RECVMSG.                                             |
| SUM\_TIMER\_READ              | Total wait time of all read operations that are timed.                                                            |
| MIN\_TIMER\_READ              | Minimum wait time of all read operations that are timed.                                                          |
| AVG\_TIMER\_READ              | Average wait time of all read operations that are timed.                                                          |
| MAX\_TIMER\_READ              | Maximum wait time of all read operations that are timed.                                                          |
| SUM\_NUMBER\_OF\_BYTES\_READ  | Bytes read by read operations.                                                                                    |
| COUNT\_WRITE                  | Number of all write operations, including SEND, SENDTO, and SENDMSG.                                              |
| SUM\_TIMER\_WRITE             | Total wait time of all write operations that are timed.                                                           |
| MIN\_TIMER\_WRITE             | Minimum wait time of all write operations that are timed.                                                         |
| AVG\_TIMER\_WRITE             | Average wait time of all write operations that are timed.                                                         |
| MAX\_TIMER\_WRITE             | Maximum wait time of all write operations that are timed.                                                         |
| SUM\_NUMBER\_OF\_BYTES\_WRITE | Bytes written by write operations.                                                                                |
| COUNT\_MISC                   | Number of all miscellaneous operations not counted above, including CONNECT, LISTEN, ACCEPT, CLOSE, and SHUTDOWN. |
| SUM\_TIMER\_MISC              | Total wait time of all miscellaneous operations that are timed.                                                   |
| MIN\_TIMER\_MISC              | Minimum wait time of all miscellaneous operations that are timed.                                                 |
| AVG\_TIMER\_MISC              | Average wait time of all miscellaneous operations that are timed.                                                 |
| MAX\_TIMER\_MISC              | Maximum wait time of all miscellaneous operations that are timed.                                                 |

You can [TRUNCATE](../../../sql-statements/table-statements/truncate-table.md) the table, which will reset all counters to zero.

## Example

```sql
SELECT * FROM socket_summary_by_event_name\G
*************************** 1. row ***************************
               EVENT_NAME: wait/io/socket/sql/server_tcpip_socket
               COUNT_STAR: 0
           SUM_TIMER_WAIT: 0
           MIN_TIMER_WAIT: 0
           AVG_TIMER_WAIT: 0
           MAX_TIMER_WAIT: 0
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
               COUNT_MISC: 0
           SUM_TIMER_MISC: 0
           MIN_TIMER_MISC: 0
           AVG_TIMER_MISC: 0
           MAX_TIMER_MISC: 0
*************************** 2. row ***************************
               EVENT_NAME: wait/io/socket/sql/server_unix_socket
               COUNT_STAR: 0
           SUM_TIMER_WAIT: 0
           MIN_TIMER_WAIT: 0
           AVG_TIMER_WAIT: 0
           MAX_TIMER_WAIT: 0
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
               COUNT_MISC: 0
           SUM_TIMER_MISC: 0
           MIN_TIMER_MISC: 0
           AVG_TIMER_MISC: 0
           MAX_TIMER_MISC: 0
...
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
