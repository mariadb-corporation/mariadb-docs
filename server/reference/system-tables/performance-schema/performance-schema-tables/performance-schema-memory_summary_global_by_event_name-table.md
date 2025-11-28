---
description: >-
  This table provides a global summary of memory usage events aggregated by
  event name, showing total memory allocation across the server.
---

# Performance Schema memory\_summary\_global\_by\_event\_name Table

{% hint style="info" %}
The `memory_summary_global_by_event_name` table is available from MariaDB 10.5.2.
{% endhint %}

There are five memory summary tables in the Performance Schema that share a number of fields in common. These include:

* [memory\_summary\_by\_account\_by\_event\_name](performance-schema-memory_summary_by_account_by_event_name-table.md)
* [memory\_summary\_by\_host\_by\_event\_name](performance-schema-memory_summary_by_host_by_event_name-table.md)
* [memory\_summary\_by\_thread\_by\_event\_name](performance-schema-memory_summary_by_thread_by_event_name-table.md)
* [memory\_summary\_by\_user\_by\_event\_name](performance-schema-memory_summary_by_user_by_event_name-table.md)
* memory\_summary\_global\_by\_event\_name

The `memory_summary_global_by_event_name` table contains memory usage statistics aggregated by event and event.

The table contains the following columns:

| Field                            | Type                | Null | Default | Description                                                                           |
| -------------------------------- | ------------------- | ---- | ------- | ------------------------------------------------------------------------------------- |
| EVENT\_NAME                      | varchar(128)        | NO   | NULL    | Event name.                                                                           |
| COUNT\_ALLOC                     | bigint(20) unsigned | NO   | NULL    | Total number of allocations to memory.                                                |
| COUNT\_FREE                      | bigint(20) unsigned | NO   | NULL    | Total number of attempts to free the allocated memory.                                |
| SUM\_NUMBER\_OF\_BYTES\_ALLOC    | bigint(20) unsigned | NO   | NULL    | Total number of bytes allocated.                                                      |
| SUM\_NUMBER\_OF\_BYTES\_FREE     | bigint(20) unsigned | NO   | NULL    | Total number of bytes freed                                                           |
| LOW\_COUNT\_USED                 | bigint(20)          | NO   | NULL    | Lowest number of allocated blocks (lowest value of CURRENT\_COUNT\_USED).             |
| CURRENT\_COUNT\_USED             | bigint(20)          | NO   | NULL    | Currently allocated blocks that have not been freed (COUNT\_ALLOC minus COUNT\_FREE). |
| HIGH\_COUNT\_USED                | bigint(20)          | NO   | NULL    | Highest number of allocated blocks (highest value of CURRENT\_COUNT\_USED).           |
| LOW\_NUMBER\_OF\_BYTES\_USED     | bigint(20)          | NO   | NULL    | Lowest number of bytes used.                                                          |
| CURRENT\_NUMBER\_OF\_BYTES\_USED | bigint(20)          | NO   | NULL    | Current number of bytes used (total allocated minus total freed).                     |
| HIGH\_NUMBER\_OF\_BYTES\_USED    | bigint(20)          | NO   | NULL    | Highest number of bytes used.                                                         |

## Example

Seeing what memory was most often allocated for:

```
SELECT * FROM memory_summary_global_by_event_name 
  ORDER BY count_alloc DESC LIMIT 1\G
*************************** 1. row ***************************
                  EVENT_NAME: memory/sql/QUICK_RANGE_SELECT::alloc
                 COUNT_ALLOC: 147976
                  COUNT_FREE: 147976
   SUM_NUMBER_OF_BYTES_ALLOC: 600190656
    SUM_NUMBER_OF_BYTES_FREE: 600190656
              LOW_COUNT_USED: 0
          CURRENT_COUNT_USED: 0
             HIGH_COUNT_USED: 68
    LOW_NUMBER_OF_BYTES_USED: 0
CURRENT_NUMBER_OF_BYTES_USED: 0
   HIGH_NUMBER_OF_BYTES_USED: 275808
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
