---
description: >-
  The Information Schema THREAD_POOL_QUEUES table shows the status of the queues
  within the thread pool, detailing pending connections.
---

# Information Schema THREAD\_POOL\_QUEUES Table

{% hint style="info" %}
This table is available from MariaDB 10.5.
{% endhint %}

The table provides information about [thread pool](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md) queues, and contains the following columns:

| Column                       | Description                                                                                                                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GROUP\_ID                    | the thread group this row is showing data for                                                                                                                                                        |
| POSITION                     | position in the groups queue                                                                                                                                                                         |
| PRIORITY                     | request priority, see [priority scheduling](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md#configuring-priority-scheduling) |
| CONNECTION\_ID               | ID of the client connection that submitted the queued request                                                                                                                                        |
| QUEUEING\_TIME\_MICROSECONDS | how long the request has already been waiting in the queue in microseconds                                                                                                                           |

Setting [thread\_poll\_exact\_stats](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_exact_stats) will provides better queueing time statistics by using a high precision timestamp, at a small performance cost, for the time when the connection was added to the queue. This timestamp helps calculate the queuing time shown in the table.

Setting [thread\_pool\_dedicated\_listener](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_dedicated_listener) will give each group its own dedicated listener, and the listener thread will not pick up work items. As a result, the queueing time in the table will be more exact, since IO requests are immediately dequeued from poll, without delay.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
