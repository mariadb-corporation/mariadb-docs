# Performance Schema events\_waits\_summary\_by\_host\_by\_event\_name Table

The [Performance Schema](../) `events_waits_summary_by_host_by_event_name` table contains wait events summarized by host and event name. It contains the following columns:

| Column           | Description                                                       |
| ---------------- | ----------------------------------------------------------------- |
| HOST             | Host. Used together with EVENT\_NAME for grouping events.         |
| EVENT\_NAME      | Event name. Used together with USER and HOST for grouping events. |
| COUNT\_STAR      | Number of summarized events                                       |
| SUM\_TIMER\_WAIT | Total wait time of the summarized events that are timed.          |
| MIN\_TIMER\_WAIT | Minimum wait time of the summarized events that are timed.        |
| AVG\_TIMER\_WAIT | Average wait time of the summarized events that are timed.        |
| MAX\_TIMER\_WAIT | Maximum wait time of the summarized events that are timed.        |

The `*_TIMER_WAIT` columns only calculate results for timed events, as non-timed events have a `NULL` wait time.

## Example

```sql
SELECT * FROM events_waits_summary_by_host_by_event_name\G
...
*************************** 610. row ***************************
          HOST: NULL
    EVENT_NAME: wait/io/socket/sql/server_unix_socket
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 611. row ***************************
          HOST: NULL
    EVENT_NAME: wait/io/socket/sql/client_connection
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 612. row ***************************
          HOST: NULL
    EVENT_NAME: idle
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
