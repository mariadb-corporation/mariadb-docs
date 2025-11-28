---
description: >-
  This table summarizes memory usage events aggregated by user name and event
  name, useful for identifying users with high memory footprints.
---

# Performance Schema memory\_summary\_by\_user\_by\_event\_name Table

{% hint style="info" %}
The `memory_summary_by_user_by_event_name` table is available from MariaDB 10.5.2.
{% endhint %}

There are five memory summary tables in the Performance Schema that share a number of fields in common. These include:

* [memory\_summary\_by\_account\_by\_event\_name](performance-schema-memory_summary_by_account_by_event_name-table.md)
* [memory\_summary\_by\_host\_by\_event\_name](performance-schema-memory_summary_by_host_by_event_name-table.md)
* [memory\_summary\_by\_thread\_by\_event\_name](performance-schema-memory_summary_by_thread_by_event_name-table.md)
* memory\_summary\_by\_user\_by\_event\_name
* [memory\_global\_by\_event\_name](performance-schema-memory_summary_global_by_event_name-table.md)

The `memory_summary_by_user_by_event_name` table contains memory usage statistics aggregated by user and event.

The table contains the following columns:

| Field                            | Type                | Null | Default | Description                                                                           |
| -------------------------------- | ------------------- | ---- | ------- | ------------------------------------------------------------------------------------- |
| USER                             | char(32)            | YES  | NULL    | User portion of the account.                                                          |
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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
