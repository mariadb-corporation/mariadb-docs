---
description: >-
  This table summarizes wait events aggregated by user name and event name,
  helping to identify users triggering significant wait events.
---

# Performance Schema events\_waits\_summary\_by\_user\_by\_event\_name Table

The [Performance Schema](../) `events_waits_summary_by_user_by_event_name` table contains wait events summarized by user and event name. It contains the following columns:

| Column           | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| USER             | User. Used together with EVENT\_NAME for grouping events.  |
| EVENT\_NAME      | Event name. Used together with USER for grouping events.   |
| COUNT\_STAR      | Number of summarized events                                |
| SUM\_TIMER\_WAIT | Total wait time of the summarized events that are timed.   |
| MIN\_TIMER\_WAIT | Minimum wait time of the summarized events that are timed. |
| AVG\_TIMER\_WAIT | Average wait time of the summarized events that are timed. |
| MAX\_TIMER\_WAIT | Maximum wait time of the summarized events that are timed. |

The `*_TIMER_WAIT` columns only calculate results for timed events, as non-timed events have a `NULL` wait time.

## Example

```sql
SELECT * FROM events_waits_summary_by_user_by_event_name\G
...
*************************** 916. row ***************************
          USER: NULL
    EVENT_NAME: wait/io/socket/sql/server_unix_socket
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 917. row ***************************
          USER: NULL
    EVENT_NAME: wait/io/socket/sql/client_connection
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 918. row ***************************
          USER: NULL
    EVENT_NAME: idle
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
