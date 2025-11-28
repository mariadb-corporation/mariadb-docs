---
description: >-
  This table summarizes stage events aggregated by the client account and the
  specific event name, showing counts and wait times.
---

# Performance Schema events\_transactions\_summary\_by\_account\_by\_event\_name Table

{% hint style="info" %}
The `events_transactions_summary_by_account_by_event_name` table is available from MariaDB 10.5.2.
{% endhint %}

The `events_transactions_summary_by_account_by_event_name` table contains information on transaction events aggregated by account and event name.

The table contains the following columns:

| Column                  | Type                | Description                                                                                                                                                                                                  |
| ----------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| USER                    | char(32)            | User for which summary is generated.                                                                                                                                                                         |
| HOST                    | char(60)            | Host for which summary is generated.                                                                                                                                                                         |
| EVENT\_NAME             | varchar(128)        | Event name for which summary is generated.                                                                                                                                                                   |
| COUNT\_STAR             | bigint(20) unsigned | The number of summarized events. This value includes all events, whether timed or nontimed.                                                                                                                  |
| SUM\_TIMER\_WAIT        | bigint(20) unsigned | The total wait time of the summarized timed events. This value is calculated only for timed events because nontimed events have a wait time of NULL. The same is true for the other xxx\_TIMER\_WAIT values. |
| MIN\_TIMER\_WAIT        | bigint(20) unsigned | The minimum wait time of the summarized timed events.                                                                                                                                                        |
| AVG\_TIMER\_WAIT        | bigint(20) unsigned | The average wait time of the summarized timed events.                                                                                                                                                        |
| MAX\_TIMER\_WAIT        | bigint(20) unsigned | The maximum wait time of the summarized timed events.                                                                                                                                                        |
| COUNT\_READ\_WRITE      | bigint(20) unsigned | The total number of only READ/WRITE transaction events.                                                                                                                                                      |
| SUM\_TIMER\_READ\_WRITE | bigint(20) unsigned | The total wait time of only READ/WRITE transaction events.                                                                                                                                                   |
| MIN\_TIMER\_READ\_WRITE | bigint(20) unsigned | The minimum wait time of only READ/WRITE transaction events.                                                                                                                                                 |
| AVG\_TIMER\_READ\_WRITE | bigint(20) unsigned | The average wait time of only READ/WRITE transaction events.                                                                                                                                                 |
| MAX\_TIMER\_READ\_WRITE | bigint(20) unsigned | The maximum wait time of only READ/WRITE transaction events.                                                                                                                                                 |
| COUNT\_READ\_ONLY       | bigint(20) unsigned | The total number of only READ ONLY transaction events.                                                                                                                                                       |
| SUM\_TIMER\_READ\_ONLY  | bigint(20) unsigned | The total wait time of only READ ONLY transaction events.                                                                                                                                                    |
| MIN\_TIMER\_READ\_ONLY  | bigint(20) unsigned | The minimum wait time of only READ ONLY transaction events.                                                                                                                                                  |
| AVG\_TIMER\_READ\_ONLY  | bigint(20) unsigned | The average wait time of only READ ONLY transaction events.                                                                                                                                                  |
| MAX\_TIMER\_READ\_ONLY  | bigint(20) unsigned | The maximum wait time of only READ ONLY transaction events.                                                                                                                                                  |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
