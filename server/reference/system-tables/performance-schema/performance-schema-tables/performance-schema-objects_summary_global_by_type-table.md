---
description: >-
  This table aggregates usage statistics for objects (tables, events, etc.) by
  type, schema, and name, showing global access counts and timers.
---

# Performance Schema objects\_summary\_global\_by\_type Table

It aggregates object wait events, and contains the following columns:

| Column           | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| OBJECT\_TYPE     | Groups records together with OBJECT\_SCHEMA and OBJECT\_NAME. |
| OBJECT\_SCHEMA   | Groups records together with OBJECT\_TYPE and OBJECT\_NAME.   |
| OBJECT\_NAME     | Groups records together with OBJECT\_SCHEMA and OBJECT\_TYPE. |
| COUNT\_STAR      | Number of summarized events                                   |
| SUM\_TIMER\_WAIT | Total wait time of the summarized events that are timed.      |
| MIN\_TIMER\_WAIT | Minimum wait time of the summarized events that are timed.    |
| AVG\_TIMER\_WAIT | Average wait time of the summarized events that are timed.    |
| MAX\_TIMER\_WAIT | Maximum wait time of the summarized events that are timed.    |

You can [TRUNCATE](../../../sql-statements/table-statements/truncate-table.md) the table, which will reset all counters to zero.

## Example

```sql
SELECT * FROM objects_summary_global_by_type\G
...
*************************** 101. row ***************************
   OBJECT_TYPE: TABLE
 OBJECT_SCHEMA: test
   OBJECT_NAME: v
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 102. row ***************************
   OBJECT_TYPE: TABLE
 OBJECT_SCHEMA: test
   OBJECT_NAME: xx2
    COUNT_STAR: 2
SUM_TIMER_WAIT: 1621920
MIN_TIMER_WAIT: 481344
AVG_TIMER_WAIT: 810960
MAX_TIMER_WAIT: 1140576
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
