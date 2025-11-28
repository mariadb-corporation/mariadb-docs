---
description: >-
  This table aggregates I/O wait statistics by index, helping to identify which
  indexes handle the most traffic or are causing latency.
---

# Performance Schema table\_io\_waits\_summary\_by\_index\_usage Table

The `table_io_waits_summary_by_index_usage` table records table I/O waits by index.

| Column             | Description                                                                                               |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| OBJECT\_TYPE       | TABLE in the case of all indexes.                                                                         |
| OBJECT\_SCHEMA     | Schema name.                                                                                              |
| OBJECT\_NAME       | Table name.                                                                                               |
| INDEX\_NAME        | Index name, or PRIMARY for the primary index, NULL for no index (inserts are counted in this case).       |
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

You can [TRUNCATE](../../../sql-statements/table-statements/truncate-table.md) the table, which will reset all counters to zero. The table is also truncated if the [table\_io\_waits\_summary\_by\_table](performance-schema-table_io_waits_summary_by_table-table.md) table is truncated.

If a table's index structure is changed, index statistics recorded in this table may also be reset.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
