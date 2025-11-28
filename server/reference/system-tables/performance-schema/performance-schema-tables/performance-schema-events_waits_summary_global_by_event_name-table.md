---
description: >-
  This table provides a global summary of wait events aggregated by event name,
  showing total server-wide wait statistics.
---

# Performance Schema events\_waits\_summary\_global\_by\_event\_name Table

The [Performance Schema](../) `events_waits_summary_global_by_event_name` table contains wait events summarized by event name. It contains the following columns:

| Column           | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| EVENT\_NAME      | Event name.                                                |
| COUNT\_STAR      | Number of summarized events                                |
| SUM\_TIMER\_WAIT | Total wait time of the summarized events that are timed.   |
| MIN\_TIMER\_WAIT | Minimum wait time of the summarized events that are timed. |
| AVG\_TIMER\_WAIT | Average wait time of the summarized events that are timed. |
| MAX\_TIMER\_WAIT | Maximum wait time of the summarized events that are timed. |

The `*_TIMER_WAIT` columns only calculate results for timed events, as non-timed events have a `NULL` wait time.

## Example

```sql
SELECT * FROM events_waits_summary_global_by_event_name\G
...
*************************** 303. row ***************************
    EVENT_NAME: wait/io/socket/sql/server_tcpip_socket
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 304. row ***************************
    EVENT_NAME: wait/io/socket/sql/server_unix_socket
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 305. row ***************************
    EVENT_NAME: wait/io/socket/sql/client_connection
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 306. row ***************************
    EVENT_NAME: idle
    COUNT_STAR: 265
SUM_TIMER_WAIT: 46861125181000000
MIN_TIMER_WAIT: 1000000
AVG_TIMER_WAIT: 176834434000000
MAX_TIMER_WAIT: 4912417573000000
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
