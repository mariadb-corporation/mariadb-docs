---
description: >-
  The events_stages_current table shows the current stage event for each thread,
  including timer information and nesting details.
---

# Performance Schema events\_stages\_current Table

The `events_stages_current` table contains current stage events, with each row being a record of a thread and its most recent stage event.

The table contains the following columns:

| Column               | Description                                                                                                                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| THREAD\_ID           | Thread associated with the event. Together with EVENT\_ID uniquely identifies the row.                                                                                                                           |
| EVENT\_ID            | Thread's current event number at the start of the event. Together with THREAD\_ID uniquely identifies the row.                                                                                                   |
| END\_EVENT\_ID       | NULL when the event starts, set to the thread's current event number at the end of the event.                                                                                                                    |
| EVENT\_NAME          | Event instrument name and a NAME from the setup\_instruments table                                                                                                                                               |
| SOURCE               | Name and line number of the source file containing the instrumented code that produced the event.                                                                                                                |
| TIMER\_START         | Value in picoseconds when the event timing started or NULL if timing is not collected. Relative to the server start, not to the epoch, so cannot directly be converted to a timestamp.                           |
| TIMER\_END           | Value in picoseconds when the event timing ended, or NULL if the event has not ended or timing is not collected. Relative to the server start, not to the epoch, so cannot directly be converted to a timestamp. |
| TIMER\_WAIT          | Value in picoseconds of the event's duration or NULL if the event has not ended or timing is not collected.                                                                                                      |
| NESTING\_EVENT\_ID   | EVENT\_ID of event within which this event nests.                                                                                                                                                                |
| NESTING\_EVENT\_TYPE | Nesting event type. One of transaction, statement, stage or wait.                                                                                                                                                |

It is possible to empty this table with a `TRUNCATE TABLE` statement.

The related tables, [events\_stages\_history](performance-schema-events_stages_history-table.md) and [events\_stages\_history\_long](performance-schema-events_stages_history_long-table.md) derive their values from the current events.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
