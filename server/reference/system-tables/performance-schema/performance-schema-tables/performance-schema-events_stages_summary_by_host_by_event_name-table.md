# Performance Schema events\_stages\_summary\_by\_host\_by\_event\_name Table

The table lists stage events, summarized by host and event name.

It contains the following columns:

| Column           | Description                                                               |
| ---------------- | ------------------------------------------------------------------------- |
| HOST             | Host. Used together with EVENT\_NAME for grouping events.                 |
| EVENT\_NAME      | Event name. Used together with HOST for grouping events.                  |
| COUNT\_STAR      | Number of summarized events, which includes all timed and untimed events. |
| SUM\_TIMER\_WAIT | Total wait time of the timed summarized events.                           |
| MIN\_TIMER\_WAIT | Minimum wait time of the timed summarized events.                         |
| AVG\_TIMER\_WAIT | Average wait time of the timed summarized events.                         |
| MAX\_TIMER\_WAIT | Maximum wait time of the timed summarized events.                         |

## Example

```sql
SELECT * FROM events_stages_summary_by_host_by_event_name\G
...
*************************** 216. row ***************************
          HOST: NULL
    EVENT_NAME: stage/sql/Waiting for event metadata lock
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 217. row ***************************
          HOST: NULL
    EVENT_NAME: stage/sql/Waiting for commit lock
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 218. row ***************************
          HOST: NULL
    EVENT_NAME: stage/aria/Waiting for a resource
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
