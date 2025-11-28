---
description: >-
  This table summarizes statement events aggregated by client account and event
  name, detailing execution counts and timer statistics.
---

# Performance Schema events\_statements\_summary\_by\_account\_by\_event\_name Table

The [Performance Schema](../) events\_statements\_summary\_by\_account\_by\_event\_name table contains statement events summarized by account and event name. It contains the following columns:

| Column                          | Description                                                                            |
| ------------------------------- | -------------------------------------------------------------------------------------- |
| USER                            | User. Used together with HOST and EVENT\_NAME for grouping events.                     |
| HOST                            | Host. Used together with USER and EVENT\_NAME for grouping events.                     |
| EVENT\_NAME                     | Event name. Used together with USER and HOST for grouping events.                      |
| COUNT\_STAR                     | Number of summarized events                                                            |
| SUM\_TIMER\_WAIT                | Total wait time of the summarized events that are timed.                               |
| MIN\_TIMER\_WAIT                | Minimum wait time of the summarized events that are timed.                             |
| AVG\_TIMER\_WAIT                | Average wait time of the summarized events that are timed.                             |
| MAX\_TIMER\_WAIT                | Maximum wait time of the summarized events that are timed.                             |
| SUM\_LOCK\_TIME                 | Sum of the LOCK\_TIME column in the events\_statements\_current table.                 |
| SUM\_ERRORS                     | Sum of the ERRORS column in the events\_statements\_current table.                     |
| SUM\_WARNINGS                   | Sum of the WARNINGS column in the events\_statements\_current table.                   |
| SUM\_ROWS\_AFFECTED             | Sum of the ROWS\_AFFECTED column in the events\_statements\_current table.             |
| SUM\_ROWS\_SENT                 | Sum of the ROWS\_SENT column in the events\_statements\_current table.                 |
| SUM\_ROWS\_EXAMINED             | Sum of the ROWS\_EXAMINED column in the events\_statements\_current table.             |
| SUM\_CREATED\_TMP\_DISK\_TABLES | Sum of the CREATED\_TMP\_DISK\_TABLES column in the events\_statements\_current table. |
| SUM\_CREATED\_TMP\_TABLES       | Sum of the CREATED\_TMP\_TABLES column in the events\_statements\_current table.       |
| SUM\_SELECT\_FULL\_JOIN         | Sum of the SELECT\_FULL\_JOIN column in the events\_statements\_current table.         |
| SUM\_SELECT\_FULL\_RANGE\_JOIN  | Sum of the SELECT\_FULL\_RANGE\_JOIN column in the events\_statements\_current table.  |
| SUM\_SELECT\_RANGE              | Sum of the SELECT\_RANGE column in the events\_statements\_current table.              |
| SUM\_SELECT\_RANGE\_CHECK       | Sum of the SELECT\_RANGE\_CHECK column in the events\_statements\_current table.       |
| SUM\_SELECT\_SCAN               | Sum of the SELECT\_SCAN column in the events\_statements\_current table.               |
| SUM\_SORT\_MERGE\_PASSES        | Sum of the SORT\_MERGE\_PASSES column in the events\_statements\_current table.        |
| SUM\_SORT\_RANGE                | Sum of the SORT\_RANGE column in the events\_statements\_current table.                |
| SUM\_SORT\_ROWS                 | Sum of the SORT\_ROWS column in the events\_statements\_current table.                 |
| SUM\_SORT\_SCAN                 | Sum of the SORT\_SCAN column in the events\_statements\_current table.                 |
| SUM\_NO\_INDEX\_USED            | Sum of the NO\_INDEX\_USED column in the events\_statements\_current table.            |
| SUM\_NO\_GOOD\_INDEX\_USED      | Sum of the NO\_GOOD\_INDEX\_USED column in the events\_statements\_current table.      |

The `*_TIMER_WAIT` columns only calculate results for timed events, as non-timed events have a `NULL` wait time.

## Example

```sql
SELECT * FROM events_statements_summary_by_account_by_event_name\G
...
*************************** 521. row ***************************
                       USER: NULL
                       HOST: NULL
                 EVENT_NAME: statement/com/Error
                 COUNT_STAR: 0
             SUM_TIMER_WAIT: 0
             MIN_TIMER_WAIT: 0
             AVG_TIMER_WAIT: 0
             MAX_TIMER_WAIT: 0
              SUM_LOCK_TIME: 0
                 SUM_ERRORS: 0
               SUM_WARNINGS: 0
          SUM_ROWS_AFFECTED: 0
              SUM_ROWS_SENT: 0
          SUM_ROWS_EXAMINED: 0
SUM_CREATED_TMP_DISK_TABLES: 0
     SUM_CREATED_TMP_TABLES: 0
       SUM_SELECT_FULL_JOIN: 0
 SUM_SELECT_FULL_RANGE_JOIN: 0
           SUM_SELECT_RANGE: 0
     SUM_SELECT_RANGE_CHECK: 0
            SUM_SELECT_SCAN: 0
      SUM_SORT_MERGE_PASSES: 0
             SUM_SORT_RANGE: 0
              SUM_SORT_ROWS: 0
              SUM_SORT_SCAN: 0
          SUM_NO_INDEX_USED: 0
     SUM_NO_GOOD_INDEX_USED: 0
*************************** 522. row ***************************
                       USER: NULL
                       HOST: NULL
                 EVENT_NAME: statement/com/
                 COUNT_STAR: 0
             SUM_TIMER_WAIT: 0
             MIN_TIMER_WAIT: 0
             AVG_TIMER_WAIT: 0
             MAX_TIMER_WAIT: 0
              SUM_LOCK_TIME: 0
                 SUM_ERRORS: 0
               SUM_WARNINGS: 0
          SUM_ROWS_AFFECTED: 0
              SUM_ROWS_SENT: 0
          SUM_ROWS_EXAMINED: 0
SUM_CREATED_TMP_DISK_TABLES: 0
     SUM_CREATED_TMP_TABLES: 0
       SUM_SELECT_FULL_JOIN: 0
 SUM_SELECT_FULL_RANGE_JOIN: 0
           SUM_SELECT_RANGE: 0
     SUM_SELECT_RANGE_CHECK: 0
            SUM_SELECT_SCAN: 0
      SUM_SORT_MERGE_PASSES: 0
             SUM_SORT_RANGE: 0
              SUM_SORT_ROWS: 0
              SUM_SORT_SCAN: 0
          SUM_NO_INDEX_USED: 0
     SUM_NO_GOOD_INDEX_USED: 0
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
