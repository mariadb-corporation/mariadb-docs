---
description: >-
  This table summarizes socket I/O events per socket instance, allowing for
  traffic analysis and latency monitoring of individual connections.
---

# Performance Schema socket\_summary\_by\_instance Table

It aggregates timer and byte count statistics for all socket I/O operations by socket instance.

| Column                        | Description                                                                                                       |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| EVENT\_NAME                   | Socket instrument.                                                                                                |
| OBJECT\_INSTANCE\_BEGIN       | Address in memory.                                                                                                |
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

The corresponding row in the table is deleted when a connection terminates.

You can [TRUNCATE](../../../sql-statements/table-statements/truncate-table.md) the table, which will reset all counters to zero.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
