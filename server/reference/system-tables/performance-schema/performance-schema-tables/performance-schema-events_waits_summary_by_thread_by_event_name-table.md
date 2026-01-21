---
description: >-
  This table summarizes wait events aggregated by thread and event name, useful
  for pinpointing threads experiencing high wait times.
---

# Performance Schema events\_waits\_summary\_by\_thread\_by\_event\_name Table

The [Performance Schema](../) `events_waits_summary_by_thread_by_event_name` table contains wait events summarized by thread and event name. It contains the following columns:

| Column           | Description                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------- |
| THREAD\_ID       | Thread associated with the event. Together with EVENT\_NAME uniquely identifies the row. |
| EVENT\_NAME      | Event name. Used together with THREAD\_ID for grouping events.                           |
| COUNT\_STAR      | Number of summarized events                                                              |
| SUM\_TIMER\_WAIT | Total wait time of the summarized events that are timed.                                 |
| MIN\_TIMER\_WAIT | Minimum wait time of the summarized events that are timed.                               |
| AVG\_TIMER\_WAIT | Average wait time of the summarized events that are timed.                               |
| MAX\_TIMER\_WAIT | Maximum wait time of the summarized events that are timed.                               |

The `*_TIMER_WAIT` columns only calculate results for timed events, as non-timed events have a `NULL` wait time.

## Example

```sql
SELECT * FROM events_waits_summary_by_thread_by_event_name\G
...
*************************** 6424. row ***************************
     THREAD_ID: 64
    EVENT_NAME: wait/io/socket/sql/server_unix_socket
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 6425. row ***************************
     THREAD_ID: 64
    EVENT_NAME: wait/io/socket/sql/client_connection
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 6426. row ***************************
     THREAD_ID: 64
    EVENT_NAME: idle
    COUNT_STAR: 73
SUM_TIMER_WAIT: 22005252162000000
MIN_TIMER_WAIT: 3000000
AVG_TIMER_WAIT: 301441810000000
MAX_TIMER_WAIT: 4912417573000000
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
