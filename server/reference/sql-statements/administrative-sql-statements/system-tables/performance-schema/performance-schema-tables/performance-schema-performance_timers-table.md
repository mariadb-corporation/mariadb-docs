
# Performance Schema performance_timers Table

## Description


The `performance_timers` table lists available event timers.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| TIMER_NAME | Time name, used in the [setup_timers](performance-schema-setup_timers-table.md) table. |
| TIMER_FREQUENCY | Number of timer units per second. Dependent on the processor speed. |
| TIMER_RESOLUTION | Number of timer units by which timed values increase each time. |
| TIMER_OVERHEAD | Minimum timer overhead, determined during initialization by calling the timer 20 times and selecting the smallest value. Total overhead will be at least double this, as the timer is called at the beginning and end of each timed event. |



Any `NULL` values indicate that particular timer is not available on your platform, Any timer names with a non-NULL value can be used in the [setup_timers](performance-schema-setup_timers-table.md) table.


## Example


```
SELECT * FROM performance_timers;
+-------------+-----------------+------------------+---------------------+
| TIMER_NAME  | TIMER_FREQUENCY | TIMER_RESOLUTION | TIMER_OVERHEAD      |
+-------------+-----------------+------------------+---------------------+
| CYCLE       |      2293651741 |                1 |                  28 |
| NANOSECOND  |      1000000000 |                1 |                  48 |
| MICROSECOND |         1000000 |                1 |                  52 |
| MILLISECOND |            1000 |             1000 | 9223372036854775807 |
| TICK        |             106 |                1 |                 496 |
+-------------+-----------------+------------------+---------------------+
```


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
