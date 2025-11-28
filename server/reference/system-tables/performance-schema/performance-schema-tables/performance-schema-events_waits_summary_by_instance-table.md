---
description: >-
  This table summarizes wait events per instrument instance, allowing detailed
  analysis of specific locks, mutexes, or conditions.
---

# Performance Schema events\_waits\_summary\_by\_instance Table

The [Performance Schema](../) `events_waits_summary_by_instance` table contains wait events summarized by instance. It contains the following columns:

| Column                  | Description                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| EVENT\_NAME             | Event name. Used together with OBJECT\_INSTANCE\_BEGIN for grouping events.                                                              |
| OBJECT\_INSTANCE\_BEGIN | If an instrument creates multiple instances, each instance has a unique OBJECT\_INSTANCE\_BEGIN value to allow for grouping by instance. |
| COUNT\_STAR             | Number of summarized events                                                                                                              |
| SUM\_TIMER\_WAIT        | Total wait time of the summarized events that are timed.                                                                                 |
| MIN\_TIMER\_WAIT        | Minimum wait time of the summarized events that are timed.                                                                               |
| AVG\_TIMER\_WAIT        | Average wait time of the summarized events that are timed.                                                                               |
| MAX\_TIMER\_WAIT        | Maximum wait time of the summarized events that are timed.                                                                               |

The `*_TIMER_WAIT` columns only calculate results for timed events, as non-timed events have a `NULL` wait time.

## Example

```sql
SELECT * FROM events_waits_summary_by_instance\G
...
*************************** 202. row ***************************
           EVENT_NAME: wait/io/file/sql/binlog
OBJECT_INSTANCE_BEGIN: 140578961969856
           COUNT_STAR: 6
       SUM_TIMER_WAIT: 90478331960
       MIN_TIMER_WAIT: 263344
       AVG_TIMER_WAIT: 15079721848
       MAX_TIMER_WAIT: 67760576376
*************************** 203. row ***************************
           EVENT_NAME: wait/io/file/sql/dbopt
OBJECT_INSTANCE_BEGIN: 140578961970560
           COUNT_STAR: 6
       SUM_TIMER_WAIT: 39891428472
       MIN_TIMER_WAIT: 387168
       AVG_TIMER_WAIT: 6648571412
       MAX_TIMER_WAIT: 24503293304
*************************** 204. row ***************************
           EVENT_NAME: wait/io/file/sql/dbopt
OBJECT_INSTANCE_BEGIN: 140578961971264
           COUNT_STAR: 6
       SUM_TIMER_WAIT: 39902495024
       MIN_TIMER_WAIT: 177888
       AVG_TIMER_WAIT: 6650415692
       MAX_TIMER_WAIT: 21026400404
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
