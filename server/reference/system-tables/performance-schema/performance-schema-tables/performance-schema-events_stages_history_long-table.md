---
description: >-
  The events_stages_history_long table stores the most recent 10,000 completed
  stage events globally, providing a deeper history than per-thread tables.
---

# Performance Schema events\_stages\_history\_long Table

The `events_stages_history_long` table by default contains the ten thousand most recent completed stage events. This number can be adjusted by setting the [performance\_schema\_events\_stages\_history\_long\_size](../performance-schema-system-variables.md#performance_schema_events_stages_history_long_size) system variable when the server starts up.

The table structure is identical to the `events_stage_current` table structure, and contains the following columns:

| Column               | Description                                                                                                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| THREAD\_ID           | Thread associated with the event. Together with EVENT\_ID uniquely identifies the row.                                                                                                 |
| EVENT\_ID            | Thread's current event number at the start of the event. Together with THREAD\_ID uniquely identifies the row.                                                                         |
| END\_EVENT\_ID       | NULL when the event starts, set to the thread's current event number at the end of the event.                                                                                          |
| EVENT\_NAME          | Event instrument name and a NAME from the setup\_instruments table                                                                                                                     |
| SOURCE               | Name and line number of the source file containing the instrumented code that produced the event.                                                                                      |
| TIMER\_START         | Value in picoseconds when the event timing started or NULL if timing is not collected. Relative to the server start, not to the epoch, so cannot directly be converted to a timestamp. |
| TIMER\_END           | Value in picoseconds when the event timing ended, or NULL if timing is not collected. Relative to the server start, not to the epoch, so cannot directly be converted to a timestamp.  |
| TIMER\_WAIT          | Value in picoseconds of the event's duration or NULL if timing is not collected.                                                                                                       |
| NESTING\_EVENT\_ID   | EVENT\_ID of event within which this event nests.                                                                                                                                      |
| NESTING\_EVENT\_TYPE | Nesting event type. One of transaction, statement, stage or wait.                                                                                                                      |

It is possible to empty this table with a `TRUNCATE TABLE` statement.

[events\_stages\_current](performance-schema-events_stages_current-table.md) and [events\_stages\_history](performance-schema-events_stages_history-table.md) are related tables.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
