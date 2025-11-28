---
description: >-
  The events_waits_history_long table stores the most recent 10,000 completed
  wait events globally, autosized at startup.
---

# Performance Schema events\_waits\_history\_long Table

The `events_waits_history_long` table by default contains the ten thousand most recent completed wait events. This number can be adjusted by setting the [performance\_schema\_events\_waits\_history\_long\_size](../performance-schema-system-variables.md#performance_schema_events_waits_history_long_size) system variable when the server starts up.

The table structure is identical to the [events\_waits\_current](performance-schema-events_waits_current-table.md) table structure, and contains the following columns:

| Column                  | Description                                                                                                                                            |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| THREAD\_ID              | Thread associated with the event. Together with EVENT\_ID uniquely identifies the row.                                                                 |
| EVENT\_ID               | Thread's current event number at the start of the event. Together withTHREAD\_IDuniquely identifies the row.                                           |
| END\_EVENT\_ID          | NULL when the event starts, set to the thread's current event number at the end of the event.                                                          |
| EVENT\_NAME             | Event instrument name and a NAME from the setup\_instruments table                                                                                     |
| SOURCE                  | Name and line number of the source file containing the instrumented code that produced the event.                                                      |
| TIMER\_START            | Value in picoseconds when the event timing started or NULL if timing is not collected.                                                                 |
| TIMER\_END              | Value in picoseconds when the event timing ended, or NULL if timing is not collected.                                                                  |
| TIMER\_WAIT             | Value in picoseconds of the event's duration or NULL if timing is not collected.                                                                       |
| SPINS                   | Number of spin rounds for a mutex, or NULL if spin rounds are not used, or spinning is not instrumented.                                               |
| OBJECT\_SCHEMA          | Name of the schema that contains the table for table I/O objects, otherwise NULL for file I/O and synchronization objects.                             |
| OBJECT\_NAME            | File name for file I/O objects, table name for table I/O objects, the socket's IP:PORT value for a socket object or NULL for a synchronization object. |
| INDEX\_NAME             | Name of the index, PRIMARY for the primary key, or NULL for no index used.                                                                             |
| OBJECT\_TYPE            | FILE for a file object, TABLE or TEMPORARY TABLE for a table object, or NULL for a synchronization object.                                             |
| OBJECT\_INSTANCE\_BEGIN | Address in memory of the object.                                                                                                                       |
| NESTING\_EVENT\_ID      | EVENT\_ID of event within which this event nests.                                                                                                      |
| NESTING\_EVENT\_TYPE    | Nesting event type. Either statement, stage or wait.                                                                                                   |
| OPERATION               | Operation type, for example read, write or lock                                                                                                        |
| NUMBER\_OF\_BYTES       | Number of bytes that the operation read or wrote, or NULL for table I/O waits.                                                                         |
| FLAGS                   | Reserved for use in the future.                                                                                                                        |

It is possible to empty this table with a `TRUNCATE TABLE` statement.

events\_waits\_current and events\_waits\_history are related tables.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
