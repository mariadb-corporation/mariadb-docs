---
description: >-
  The Information Schema THREAD_POOL_GROUPS table provides details about the
  thread groups in the thread pool, including active thread counts.
---

# Information Schema THREAD\_POOL\_GROUPS Table

{% hint style="info" %}
This table is available as of MariaDB 10.5.
{% endhint %}

The table provides information about [thread pool](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md) groups, and contains the following columns:

| Column           | Description                                                                                                                                                                                                                                                                            |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GROUP\_ID        | the thread group this row is showing data for                                                                                                                                                                                                                                          |
| CONNECTIONS      | the number of clients currently connected to this thread group                                                                                                                                                                                                                         |
| THREADS          | total number of threads in this group (ACTIVE+STANDBY+LISTENER)                                                                                                                                                                                                                        |
| ACTIVE\_THREADS  | number of threads currently executing a query                                                                                                                                                                                                                                          |
| STANDBY\_THREADS | number of threads in reserve that do not currently execute anything                                                                                                                                                                                                                    |
| QUEUE\_LENGTH    | number of client requests waiting for execution                                                                                                                                                                                                                                        |
| HAS\_LISTENER    | whether there is an active listener thread right now, always 1 if [thread\_pool\_dedicated\_listener](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_dedicated_listener) is ON       |
| IS\_STALLED      | whether there's currently an active worker thread in this group that has exceeded [thread\_pool\_stall\_limit time](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_stall_limit_time) |

Setting [thread\_pool\_dedicated\_listener](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_dedicated_listener) will give each group its own dedicated listener, and the listener thread will not pick up work items. As a result, the actual queue size in the table will be more exact, since IO requests are immediately dequeued from poll, without delay.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
