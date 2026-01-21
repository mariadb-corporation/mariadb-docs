---
description: >-
  This table summarizes I/O wait events by table, detailing the frequency and
  latency of fetch, insert, update, and delete operations.
---

# Performance Schema table\_io\_waits\_summary\_by\_table Table

The `table_io_waits_summary_by_table` table records table I/O waits by table.

| Column             | Description                                                                                               |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| OBJECT\_TYPE       | Since this table records waits by table, always set to TABLE.                                             |
| OBJECT\_SCHEMA     | Schema name.                                                                                              |
| OBJECT\_NAME       | Table name.                                                                                               |
| COUNT\_STAR        | Number of summarized events and the sum of the x\_READ and x\_WRITE columns.                              |
| SUM\_TIMER\_WAIT   | Total wait time of the summarized events that are timed.                                                  |
| MIN\_TIMER\_WAIT   | Minimum wait time of the summarized events that are timed.                                                |
| AVG\_TIMER\_WAIT   | Average wait time of the summarized events that are timed.                                                |
| MAX\_TIMER\_WAIT   | Maximum wait time of the summarized events that are timed.                                                |
| COUNT\_READ        | Number of all read operations, and the sum of the equivalent x\_FETCH columns.                            |
| SUM\_TIMER\_READ   | Total wait time of all read operations that are timed.                                                    |
| MIN\_TIMER\_READ   | Minimum wait time of all read operations that are timed.                                                  |
| AVG\_TIMER\_READ   | Average wait time of all read operations that are timed.                                                  |
| MAX\_TIMER\_READ   | Maximum wait time of all read operations that are timed.                                                  |
| COUNT\_WRITE       | Number of all write operations, and the sum of the equivalent x\_INSERT, x\_UPDATE and x\_DELETE columns. |
| SUM\_TIMER\_WRITE  | Total wait time of all write operations that are timed.                                                   |
| MIN\_TIMER\_WRITE  | Minimum wait time of all write operations that are timed.                                                 |
| AVG\_TIMER\_WRITE  | Average wait time of all write operations that are timed.                                                 |
| MAX\_TIMER\_WRITE  | Maximum wait time of all write operations that are timed.                                                 |
| COUNT\_FETCH       | Number of all fetch operations.                                                                           |
| SUM\_TIMER\_FETCH  | Total wait time of all fetch operations that are timed.                                                   |
| MIN\_TIMER\_FETCH  | Minimum wait time of all fetch operations that are timed.                                                 |
| AVG\_TIMER\_FETCH  | Average wait time of all fetch operations that are timed.                                                 |
| MAX\_TIMER\_FETCH  | Maximum wait time of all fetch operations that are timed.                                                 |
| COUNT\_INSERT      | Number of all insert operations.                                                                          |
| SUM\_TIMER\_INSERT | Total wait time of all insert operations that are timed.                                                  |
| MIN\_TIMER\_INSERT | Minimum wait time of all insert operations that are timed.                                                |
| AVG\_TIMER\_INSERT | Average wait time of all insert operations that are timed.                                                |
| MAX\_TIMER\_INSERT | Maximum wait time of all insert operations that are timed.                                                |
| COUNT\_UPDATE      | Number of all update operations.                                                                          |
| SUM\_TIMER\_UPDATE | Total wait time of all update operations that are timed.                                                  |
| MIN\_TIMER\_UPDATE | Minimum wait time of all update operations that are timed.                                                |
| AVG\_TIMER\_UPDATE | Average wait time of all update operations that are timed.                                                |
| MAX\_TIMER\_UPDATE | Maximum wait time of all update operations that are timed.                                                |
| COUNT\_DELETE      | Number of all delete operations.                                                                          |
| SUM\_TIMER\_DELETE | Total wait time of all delete operations that are timed.                                                  |
| MIN\_TIMER\_DELETE | Minimum wait time of all delete operations that are timed.                                                |
| AVG\_TIMER\_DELETE | Average wait time of all delete operations that are timed.                                                |
| MAX\_TIMER\_DELETE | Maximum wait time of all delete operations that are timed.                                                |

You can [TRUNCATE](../../../sql-statements/table-statements/truncate-table.md) the table, which will reset all counters to zero. Truncating this table will also truncate the [table\_io\_waits\_summary\_by\_index\_usage](performance-schema-table_io_waits_summary_by_index_usage-table.md) table.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
