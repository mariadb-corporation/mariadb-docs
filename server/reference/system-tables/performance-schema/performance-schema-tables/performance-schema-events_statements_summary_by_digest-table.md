---
description: >-
  This table aggregates statement events by schema and digest, providing
  execution counts, latency, and locking statistics for normalized queries.
---

# Performance Schema events\_statements\_summary\_by\_digest Table

The [Performance Schema digest](../performance-schema-digests.md) is a hashed, normalized form of a statement with the specific data values removed. It allows statistics to be gathered for similar kinds of statements.

The [Performance Schema](../) `events_statements_summary_by_digest` table records statement events summarized by schema and digest. It contains the following columns:

| Column                          | Description                                                                                                      |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| SCHEMA NAME                     | Database name. Records are summarised together with DIGEST.                                                      |
| DIGEST                          | [Performance Schema digest](../performance-schema-digests.md). Records are summarised together with SCHEMA NAME. |
| DIGEST TEXT                     | The unhashed form of the digest.                                                                                 |
| COUNT\_STAR                     | Number of summarized events                                                                                      |
| SUM\_TIMER\_WAIT                | Total wait time of the summarized events that are timed.                                                         |
| MIN\_TIMER\_WAIT                | Minimum wait time of the summarized events that are timed.                                                       |
| AVG\_TIMER\_WAIT                | Average wait time of the summarized events that are timed.                                                       |
| MAX\_TIMER\_WAIT                | Maximum wait time of the summarized events that are timed.                                                       |
| SUM\_LOCK\_TIME                 | Sum of the LOCK\_TIME column in the events\_statements\_current table.                                           |
| SUM\_ERRORS                     | Sum of the ERRORS column in the events\_statements\_current table.                                               |
| SUM\_WARNINGS                   | Sum of the WARNINGS column in the events\_statements\_current table.                                             |
| SUM\_ROWS\_AFFECTED             | Sum of the ROWS\_AFFECTED column in the events\_statements\_current table.                                       |
| SUM\_ROWS\_SENT                 | Sum of the ROWS\_SENT column in the events\_statements\_current table.                                           |
| SUM\_ROWS\_EXAMINED             | Sum of the ROWS\_EXAMINED column in the events\_statements\_current table.                                       |
| SUM\_CREATED\_TMP\_DISK\_TABLES | Sum of the CREATED\_TMP\_DISK\_TABLES column in the events\_statements\_current table.                           |
| SUM\_CREATED\_TMP\_TABLES       | Sum of the CREATED\_TMP\_TABLES column in the events\_statements\_current table.                                 |
| SUM\_SELECT\_FULL\_JOIN         | Sum of the SELECT\_FULL\_JOIN column in the events\_statements\_current table.                                   |
| SUM\_SELECT\_FULL\_RANGE\_JOIN  | Sum of the SELECT\_FULL\_RANGE\_JOIN column in the events\_statements\_current table.                            |
| SUM\_SELECT\_RANGE              | Sum of the SELECT\_RANGE column in the events\_statements\_current table.                                        |
| SUM\_SELECT\_RANGE\_CHECK       | Sum of the SELECT\_RANGE\_CHECK column in the events\_statements\_current table.                                 |
| SUM\_SELECT\_SCAN               | Sum of the SELECT\_SCAN column in the events\_statements\_current table.                                         |
| SUM\_SORT\_MERGE\_PASSES        | Sum of the SORT\_MERGE\_PASSES column in the events\_statements\_current table.                                  |
| SUM\_SORT\_RANGE                | Sum of the SORT\_RANGE column in the events\_statements\_current table.                                          |
| SUM\_SORT\_ROWS                 | Sum of the SORT\_ROWS column in the events\_statements\_current table.                                           |
| SUM\_SORT\_SCAN                 | Sum of the SORT\_SCAN column in the events\_statements\_current table.                                           |
| SUM\_NO\_INDEX\_USED            | Sum of the NO\_INDEX\_USED column in the events\_statements\_current table.                                      |
| SUM\_NO\_GOOD\_INDEX\_USED      | Sum of the NO\_GOOD\_INDEX\_USED column in the events\_statements\_current table.                                |
| FIRST\_SEEN                     | Time at which the digest was first seen.                                                                         |
| LAST\_SEEN                      | Time at which the digest was most recently seen.                                                                 |

The `*_TIMER_WAIT` columns only calculate results for timed events, as non-timed events have a `NULL` wait time.

The `events_statements_summary_by_digest` table is limited in size by the [performance\_schema\_digests\_size](../performance-schema-system-variables.md#performance_schema_digests_size) system variable. Once the limit has been reached and the table is full, all entries are aggregated in a row with a `NULL` digest. The `COUNT_STAR` value of this `NULL` row indicates how many digests are recorded in the row and therefore gives an indication of whether `performance_schema_digests_size` should be increased to provide more accurate statistics.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
