---
description: >-
  The Information Schema THREAD_POOL_STATS table provides performance statistics
  for the thread pool, such as thread creation and efficiency.
---

# Information Schema THREAD\_POOL\_STATS Table

{% hint style="info" %}
This table is available from MariaDB 10.5.
{% endhint %}

The table provides performance counter information for the [thread pool](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md), and contains the following columns:

| Column                            | Description                                                                                                                                                                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| GROUP\_ID                         | the thread group this row is showing data for                                                                                                                                                                                                                            |
| THREAD\_CREATIONS                 | number of threads created for this group so far                                                                                                                                                                                                                          |
| THREAD\_CREATIONS\_DUE\_TO\_STALL | number of threads created due to detected stalls                                                                                                                                                                                                                         |
| WAKES                             | standby thread wakeups                                                                                                                                                                                                                                                   |
| WAKES\_DUE\_TO\_STALL             | wakeups due to stalls                                                                                                                                                                                                                                                    |
| THROTTLES                         | how often thread creation was throttled, see also: [thread-creation-throttling](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-groups-in-the-unix-implementation-of-the-thread-pool.md#thread-creation-throttling) |
| STALLS                            | number of detected stalls                                                                                                                                                                                                                                                |
| POLLS\_BY\_LISTENER               |                                                                                                                                                                                                                                                                          |
| POLLS\_BY\_WORKER                 |                                                                                                                                                                                                                                                                          |
| DEQUEUES\_BY\_LISTENER            |                                                                                                                                                                                                                                                                          |
| DEQUEUES\_BY\_WORKER              |                                                                                                                                                                                                                                                                          |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
