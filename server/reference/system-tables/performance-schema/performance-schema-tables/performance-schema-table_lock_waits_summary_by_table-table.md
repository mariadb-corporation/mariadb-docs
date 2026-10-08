---
description: >-
  This table aggregates table lock wait events, allowing administrators to
  identify tables experiencing high contention due to locking.
---

# Performance Schema table\_lock\_waits\_summary\_by\_table Table

The `table_lock_waits_summary_by_table` table records table lock waits by table.

| Column                                | Description                                                                                                                                                                                  |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OBJECT\_TYPE                          | Since this table records waits by table, always set to TABLE.                                                                                                                                |
| OBJECT\_SCHEMA                        | Schema name.                                                                                                                                                                                 |
| OBJECT\_NAME                          | Table name.                                                                                                                                                                                  |
| COUNT\_STAR                           | Number of summarized events and the sum of the x\_READ and x\_WRITE columns.                                                                                                                 |
| SUM\_TIMER\_WAIT                      | Total wait time of the summarized events that are timed.                                                                                                                                     |
| MIN\_TIMER\_WAIT                      | Minimum wait time of the summarized events that are timed.                                                                                                                                   |
| AVG\_TIMER\_WAIT                      | Average wait time of the summarized events that are timed.                                                                                                                                   |
| MAX\_TIMER\_WAIT                      | Maximum wait time of the summarized events that are timed.                                                                                                                                   |
| COUNT\_READ                           | Number of all read operations, and the sum of the equivalent x\_READ\_NORMAL, x\_READ\_WITH\_SHARED\_LOCKS, x\_READ\_HIGH\_PRIORITY and x\_READ\_NO\_INSERT columns.                         |
| SUM\_TIMER\_READ                      | Total wait time of all read operations that are timed.                                                                                                                                       |
| MIN\_TIMER\_READ                      | Minimum wait time of all read operations that are timed.                                                                                                                                     |
| AVG\_TIMER\_READ                      | Average wait time of all read operations that are timed.                                                                                                                                     |
| MAX\_TIMER\_READ                      | Maximum wait time of all read operations that are timed.                                                                                                                                     |
| COUNT\_WRITE                          | Number of all write operations, and the sum of the equivalent x\_WRITE\_ALLOW\_WRITE, x\_WRITE\_CONCURRENT\_INSERT, x\_WRITE\_DELAYED, x\_WRITE\_LOW\_PRIORITY and x\_WRITE\_NORMAL columns. |
| SUM\_TIMER\_WRITE                     | Total wait time of all write operations that are timed.                                                                                                                                      |
| MIN\_TIMER\_WRITE                     | Minimum wait time of all write operations that are timed.                                                                                                                                    |
| AVG\_TIMER\_WRITE                     | Average wait time of all write operations that are timed.                                                                                                                                    |
| MAX\_TIMER\_WRITE                     | Maximum wait time of all write operations that are timed.                                                                                                                                    |
| COUNT\_READ\_NORMAL                   | Number of all internal read normal locks.                                                                                                                                                    |
| SUM\_TIMER\_READ\_NORMAL              | Total wait time of all internal read normal locks that are timed.                                                                                                                            |
| MIN\_TIMER\_READ\_NORMAL              | Minimum wait time of all internal read normal locks that are timed.                                                                                                                          |
| AVG\_TIMER\_READ\_NORMAL              | Average wait time of all internal read normal locks that are timed.                                                                                                                          |
| MAX\_TIMER\_READ\_NORMAL              | Maximum wait time of all internal read normal locks that are timed.                                                                                                                          |
| COUNT\_READ\_WITH\_SHARED\_LOCKS      | Number of all internal read with shared locks.                                                                                                                                               |
| SUM\_TIMER\_READ\_WITH\_SHARED\_LOCKS | Total wait time of all internal read with shared locks that are timed.                                                                                                                       |
| MIN\_TIMER\_READ\_WITH\_SHARED\_LOCKS | Minimum wait time of all internal read with shared locks that are timed.                                                                                                                     |
| AVG\_TIMER\_READ\_WITH\_SHARED\_LOCKS | Average wait time of all internal read with shared locks that are timed.                                                                                                                     |
| MAX\_TIMER\_READ\_WITH\_SHARED\_LOCKS | Maximum wait time of all internal read with shared locks that are timed.                                                                                                                     |
| COUNT\_READ\_HIGH\_PRIORITY           | Number of all internal read high priority locks.                                                                                                                                             |
| SUM\_TIMER\_READ\_HIGH\_PRIORITY      | Total wait time of all internal read high priority locks that are timed.                                                                                                                     |
| MIN\_TIMER\_READ\_HIGH\_PRIORITY      | Minimum wait time of all internal read high priority locks that are timed.                                                                                                                   |
| AVG\_TIMER\_READ\_HIGH\_PRIORITY      | Average wait time of all internal read high priority locks that are timed.                                                                                                                   |
| MAX\_TIMER\_READ\_HIGH\_PRIORITY      | Maximum wait time of all internal read high priority locks that are timed.                                                                                                                   |
| COUNT\_READ\_NO\_INSERT               | Number of all internal read no insert locks.                                                                                                                                                 |
| SUM\_TIMER\_READ\_NO\_INSERT          | Total wait time of all internal read no insert locks that are timed.                                                                                                                         |
| MIN\_TIMER\_READ\_NO\_INSERT          | Minimum wait time of all internal read no insert locks that are timed.                                                                                                                       |
| AVG\_TIMER\_READ\_NO\_INSERT          | Average wait time of all internal read no insert locks that are timed.                                                                                                                       |
| MAX\_TIMER\_READ\_NO\_INSERT          | Maximum wait time of all internal read no insert locks that are timed.                                                                                                                       |
| COUNT\_READ\_EXTERNAL                 | Number of all external read locks.                                                                                                                                                           |
| SUM\_TIMER\_READ\_EXTERNAL            | Total wait time of all external read locks that are timed.                                                                                                                                   |
| MIN\_TIMER\_READ\_EXTERNAL            | Minimum wait time of all external read locks that are timed.                                                                                                                                 |
| AVG\_TIMER\_READ\_EXTERNAL            | Average wait time of all external read locks that are timed.                                                                                                                                 |
| MAX\_TIMER\_READ\_EXTERNAL            | Maximum wait time of all external read locks that are timed.                                                                                                                                 |
| COUNT\_WRITE\_ALLOW\_WRITE            | Number of all internal read normal locks.                                                                                                                                                    |
| SUM\_TIMER\_WRITE\_ALLOW\_WRITE       | Total wait time of all internal write allow write locks that are timed.                                                                                                                      |
| MIN\_TIMER\_WRITE\_ALLOW\_WRITE       | Minimum wait time of all internal write allow write locks that are timed.                                                                                                                    |
| AVG\_TIMER\_WRITE\_ALLOW\_WRITE       | Average wait time of all internal write allow write locks that are timed.                                                                                                                    |
| MAX\_TIMER\_WRITE\_ALLOW\_WRITE       | Maximum wait time of all internal write allow write locks that are timed.                                                                                                                    |
| COUNT\_WRITE\_CONCURRENT\_INSERT      | Number of all internal concurrent insert write locks.                                                                                                                                        |
| SUM\_TIMER\_WRITE\_CONCURRENT\_INSERT | Total wait time of all internal concurrent insert write locks that are timed.                                                                                                                |
| MIN\_TIMER\_WRITE\_CONCURRENT\_INSERT | Minimum wait time of all internal concurrent insert write locks that are timed.                                                                                                              |
| AVG\_TIMER\_WRITE\_CONCURRENT\_INSERT | Average wait time of all internal concurrent insert write locks that are timed.                                                                                                              |
| MAX\_TIMER\_WRITE\_CONCURRENT\_INSERT | Maximum wait time of all internal concurrent insert write locks that are timed.                                                                                                              |
| COUNT\_WRITE\_DELAYED                 | Number of all internal write delayed locks.                                                                                                                                                  |
| SUM\_TIMER\_WRITE\_DELAYED            | Total wait time of all internal write delayed locks that are timed.                                                                                                                          |
| MIN\_TIMER\_WRITE\_DELAYED            | Minimum wait time of all internal write delayed locks that are timed.                                                                                                                        |
| AVG\_TIMER\_WRITE\_DELAYED            | Average wait time of all internal write delayed locks that are timed.                                                                                                                        |
| MAX\_TIMER\_WRITE\_DELAYED            | Maximum wait time of all internal write delayed locks that are timed.                                                                                                                        |
| COUNT\_WRITE\_LOW\_PRIORITY           | Number of all internal write low priority locks.                                                                                                                                             |
| SUM\_TIMER\_WRITE\_LOW\_PRIORITY      | Total wait time of all internal write low priority locks that are timed.                                                                                                                     |
| MIN\_TIMER\_WRITE\_LOW\_PRIORITY      | Minimum wait time of all internal write low priority locks that are timed.                                                                                                                   |
| AVG\_TIMER\_WRITE\_LOW\_PRIORITY      | Average wait time of all internal write low priority locks that are timed.                                                                                                                   |
| MAX\_TIMER\_WRITE\_LOW\_PRIORITY      | Maximum wait time of all internal write low priority locks that are timed.                                                                                                                   |
| COUNT\_WRITE\_NORMAL                  | Number of all internal write normal locks.                                                                                                                                                   |
| SUM\_TIMER\_WRITE\_NORMAL             | Total wait time of all internal write normal locks that are timed.                                                                                                                           |
| MIN\_TIMER\_WRITE\_NORMAL             | Minimum wait time of all internal write normal locks that are timed.                                                                                                                         |
| AVG\_TIMER\_WRITE\_NORMAL             | Average wait time of all internal write normal locks that are timed.                                                                                                                         |
| MAX\_TIMER\_WRITE\_NORMAL             | Maximum wait time of all internal write normal locks that are timed.                                                                                                                         |
| COUNT\_WRITE\_EXTERNAL                | Number of all external write locks.                                                                                                                                                          |
| SUM\_TIMER\_WRITE\_EXTERNAL           | Total wait time of all external write locks that are timed.                                                                                                                                  |
| MIN\_TIMER\_WRITE\_EXTERNAL           | Minimum wait time of all external write locks that are timed.                                                                                                                                |
| AVG\_TIMER\_WRITE\_EXTERNAL           | Average wait time of all external write locks that are timed.                                                                                                                                |
| MAX\_TIMER\_WRITE\_EXTERNAL           | Maximum wait time of all external write locks that are timed.                                                                                                                                |

You can [TRUNCATE](../../../sql-statements/table-statements/truncate-table.md) the table, which will reset all counters to zero.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
