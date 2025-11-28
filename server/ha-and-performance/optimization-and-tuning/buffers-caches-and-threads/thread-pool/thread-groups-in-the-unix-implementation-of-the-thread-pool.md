# Thread Groups in the Unix Implementation of the Thread Pool

This article does not apply to the thread pool implementation on Windows. On Windows, MariaDB uses a native thread pool created with the [CreateThreadpool](https://docs.microsoft.com/en-us/windows/desktop/api/threadpoolapiset/nf-threadpoolapiset-createthreadpool) APl, which has its own methods to distribute threads between CPUs.

On Unix, the thread pool implementation uses objects called thread groups to divide up client connections into many independent sets of threads. The [thread\_pool\_size](thread-pool-system-status-variables.md#thread_pool_size) system variable defines the number of thread groups on a system. Generally speaking, the goal of the thread group implementation is to have one running thread on each CPU on the system at a time. Therefore, the default value of the [thread\_pool\_size](thread-pool-system-status-variables.md#thread_pool_size) system variable is auto-sized to the number of CPUs on the system.

When setting the [thread\_pool\_size](thread-pool-system-status-variables.md#thread_pool_size) system variable's value at system startup, the max value is `100000`. However, it is not a good idea to set it that high. When setting its value dynamically, the max value is either `128` or the value that was set at system startup--whichever value is higher. It can be changed dynamically with [SET GLOBAL](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```sql
SET GLOBAL thread_pool_size=32;
```

It can also be set in a server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```ini
[mariadb]
..
thread_handling=pool-of-threads
thread_pool_size=32
```

If you do not want MariaDB to use all CPUs on the system for some reason, then you can set it to a lower value than the number of CPUs. For example, this would make sense if the MariaDB Server process is limited to certain CPUs with the [taskset](https://linux.die.net/man/1/taskset) utility on Linux.

If you set the value to the number of CPUs and if you find that the CPUs are still underutilized, then try increasing the value.

The [thread\_pool\_size](thread-pool-system-status-variables.md#thread_pool_size) system variable tends to have the most visible performance effect. It is roughly equivalent to the number of threads that can run at the same time. In this case, run means use CPU, rather than sleep or wait. If a client connection needs to sleep or wait for some reason, then it wakes up another client connection in the thread group before it does so.

One reason that CPU underutilization may occur in rare cases is that the thread pool is not always informed when a thread is going to wait. For example, some waits, such as a page fault or a miss in the OS buffer cache, cannot be detected by MariaDB.

## Distributing Client Connections Between Thread Groups

When a new client connection is created, its thread group is determined using the following calculation:

```
thread_group_id = connection_id % thread_pool_size
```

The `connection_id` value in the above calculation is the same monotonically increasing number that you can use to identify connections in [SHOW PROCESSLIST](../../../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md) output or the [information\_schema.PROCESSLIST](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) table.

This calculation should assign client connections to each thread group in a round-robin manner. In general, this should result in an even distribution of client connections among thread groups.

## Types of Threads

### Thread Group Threads

Thread groups have two different kinds of threads: a **listener thread** and **worker threads**.

* A thread group's worker threads actually perform work on behalf of client connections. A thread group can have many worker threads, but usually, only one will be actively running at a time. This is not always the case. For example, the thread group can become oversubscribed if the thread pool's timer thread detects that the thread group is stalled. This is explained more in the sections below.
* A thread group's listener thread listens for I/O events and distributes work to the worker threads. If it detects that there is a request that needs to be worked on, then it can wake up a sleeping worker thread in the thread group, if any exist. If the listener thread is the only thread in the thread group, then it can also create a new worker thread. If there is only one request to handle, and if the [thread\_pool\_dedicated\_listener](thread-pool-system-status-variables.md#thread_pool_dedicated_listener) system variable is not enabled, then the listener thread can also become a worker thread and handle the request itself. This helps decrease the overhead that may be introduced by excessively waking up sleeping worker threads and excessively creating new worker threads.

### Global Threads

The thread pool has one global thread: a **timer thread**. The **timer thread** performs tasks, such as:

* Checks each thread group for stalls.
* Ensures that each thread group has a listener thread.

## Thread Creation

A new thread is created in a thread group in the scenarios listed below.

In all of the scenarios below, the thread pool implementation prefers to wake up a sleeping **worker thread** that already exists in the thread group, rather than to create a new thread.

### Worker Thread Creation by Listener Thread

A thread group's **listener thread** can create a new **worker thread** when it has more client connection requests to distribute, but no pre-existing **worker threads** are available to work on the requests. This can help to ensure that the thread group always has enough threads to keep one **worker thread** active at a time.

A thread group's **listener thread** creates a new **worker thread** if all of the following conditions are met:

* The listener thread receives a client connection request that needs to be worked on.
* There are more client connection requests in the thread group's work queue that the listener thread still needs to distribute to worker threads, so the listener thread should not become a worker thread.
* There are no active worker threads in the thread group.
* There are no sleeping worker threads in the thread group that the listener thread can wake up.
* And one of the following conditions is also met:
  * The entire thread pool has fewer than [thread\_pool\_max\_threads](thread-pool-system-status-variables.md#thread_pool_max_threads).
  * There are fewer than two threads in the thread group. This is to guarantee that each thread group can have at least two threads, even if [thread\_pool\_max\_threads](thread-pool-system-status-variables.md#thread_pool_max_threads) has already been reached or exceeded.

### Thread Creation by Worker Threads During Waits

A thread group's **worker thread** can create a new **worker thread** when the thread has to wait on something, and the thread group has more client connection requests queued, but no pre-existing **worker threads** are available to work on them. This can help to ensure that the thread group always has enough threads to keep one **worker thread** active at a time. For most workloads, this tends to be the primary mechanism that creates new **worker threads**.

A thread group's **worker thread** creates a new thread if all of the following conditions are met:

* The worker thread has to wait on some request. For example, it might be waiting on disk I/O, or it might be waiting on a lock, or it might just be waiting for a query that called the [SLEEP()](../../../../reference/sql-functions/secondary-functions/miscellaneous-functions/sleep.md) function to finish.
* There are no active worker threads in the thread group.
* There are no sleeping worker threads in the thread group that the worker thread can wake up.
* And one of the following conditions is also met:
  * The entire thread pool has fewer than [thread\_pool\_max\_threads](thread-pool-system-status-variables.md#thread_pool_max_threads).
  * There are fewer than two threads in the thread group. This is to guarantee that each thread group can have at least two threads, even if [thread\_pool\_max\_threads](thread-pool-system-status-variables.md#thread_pool_max_threads) has already been reached or exceeded.
* And one of the following conditions is also met:
  * There are more client connection requests in the thread group's work queue that the listener thread still needs to distribute to worker threads. In this case, the new thread is intended to be a worker thread.
  * There is currently no listener thread in the thread group. For example, if the [thread\_pool\_dedicated\_listener](thread-pool-system-status-variables.md#thread_pool_dedicated_listener) system variable is not enabled, then the thread group's listener thread can became a worker thread, so that it could handle some client connection request. In this case, the new thread can become the thread group's listener thread.

### Listener Thread Creation by Timer Thread

The thread pool's **timer thread** can create a new **listener thread** for a thread group when the thread group has more client connection requests that need to be distributed, but the thread group does not currently have a **listener thread** to distribute them. This can help to ensure that the thread group does not miss client connection requests because it has no **listener thread**.

The thread pool's **timer thread** creates a new **listener thread** for a thread group if all of the following conditions are met:

* The thread group has not handled any I/O events since the last check by the timer thread.
* There is currently no listener thread in the thread group. For example, if the [thread\_pool\_dedicated\_listener](thread-pool-system-status-variables.md#thread_pool_dedicated_listener) system variable is not enabled, then the thread group's listener thread can became a worker thread, so that it could handle some client connection request. In this case, the new thread can become the thread group's listener thread.
* There are no sleeping worker threads in the thread group that the timer thread can wake up.
* And one of the following conditions is also met:
  * The entire thread pool has fewer than [thread\_pool\_max\_threads](thread-pool-system-status-variables.md#thread_pool_max_threads).
  * There are fewer than two threads in the thread group. This is to guarantee that each thread group can have at least two threads, even if [thread\_pool\_max\_threads](thread-pool-system-status-variables.md#thread_pool_max_threads) has already been reached or exceeded.
* If the thread group already has active worker threads, then the following condition also needs to be met:
  * A worker thread has not been created for the thread group within the throttling interval.

### Worker Thread Creation by Timer Thread during Stalls

The thread pool's **timer thread** can create a new **worker thread** for a thread group when the thread group is stalled. This can help to ensure that a long query can't monopole its thread group.

The thread pool's **timer thread** creates a new **worker thread** for a thread group if all of the following conditions are met:

* The timer thread thinks that the thread group is stalled. This means that the following conditions have been met:
  * There are more client connection requests in the thread group's work queue that the listener thread still needs to distribute to worker threads.
  * No client connection requests have been allowed to be dequeued to run since the last stall check by the timer thread.
* There are no sleeping worker threads in the thread group that the timer thread can wake up.
* And one of the following conditions is also met:
  * The entire thread pool has fewer than [thread\_pool\_max\_threads](thread-pool-system-status-variables.md#thread_pool_max_threads).
  * There are fewer than two threads in the thread group. This is to guarantee that each thread group can have at least two threads, even if [thread\_pool\_max\_threads](thread-pool-system-status-variables.md#thread_pool_max_threads) has already been reached or exceeded.
* A worker thread has not been created for the thread group within the throttling interval.

### Thread Creation Throttling

In some of the scenarios listed above, a thread is only created within a thread group if no new threads have been created for the thread group within the _throttling interval_. The throttling interval depends on the number of threads that are already in the thread group.

In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105) and later, thread creation is not throttled until a thread group has more than 1 + [thread\_pool\_oversubscribe](thread-pool-system-status-variables.md#thread_pool_oversubscribe) threads:

| Number of Threads in Thread Group                                                                       | Throttling Interval (milliseconds) |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| 0-(1 + [thread\_pool\_oversubscribe](thread-pool-system-status-variables.md#thread_pool_oversubscribe)) | 0                                  |
| 4-7                                                                                                     | 50 \* `THROTTLING_FACTOR`          |
| 8-15                                                                                                    | 100 \* `THROTTLING_FACTOR`         |
| 16-65536                                                                                                | 20 \* `THROTTLING_FACTOR`          |

The throttling factor is calculated like this (see [thread\_pool\_stall\_limit](thread-pool-system-status-variables.md#thread_pool_stall_limit) for more information):

{% code overflow="wrap" %}
```
THROTTLING_FACTOR = thread_pool_stall_limit / MAX (500,thread_pool_stall_limit)
```
{% endcode %}

## Thread Group Stalls

The thread pool has a feature that allows it to detect if a client connection is executing a long-running query that may be monopolizing its thread group. If a client connection were to monopolize its thread group, then that could prevent other client connections in the thread group from running their queries. In other words, the thread group would appear to be _stalled_.

This stall detection feature is implemented by creating a **timer thread** that periodically checks if any of the thread groups are stalled. There is only a single **timer thread** for the entire thread pool. The [thread\_pool\_stall\_limit](thread-pool-system-status-variables.md#thread_pool_stall_limit) system variable defines the number of milliseconds between each stall check performed by the timer thread. The default value is `500`. It can be changed dynamically with [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/). For example:

```sql
SET GLOBAL thread_pool_stall_limit=300;
```

It can also be set in a server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```ini
[mariadb]
..
thread_handling=pool-of-threads
thread_pool_size=32
thread_pool_stall_limit=300
```

The **timer thread** considers a thread group to be stalled if the following is true:

* There are more client connection requests in the thread group's work queue that the listener thread still needs to distribute to worker threads.
* No client connection requests have been allowed to be dequeued to run since the last stall check by the timer thread.

This indicates that the one or more client connections currently using the active **worker threads** may be monopolizing the thread group, and preventing the queued client connections from performing work. When the **timer thread** detects that a thread group is stalled, it wakes up a sleeping **worker thread** in the thread group, if one is available. If there isn't one, then it creates a new **worker thread** in the thread group. This temporarily allows several client connections in the thread group to run in parallel.

The [thread\_pool\_stall\_limit](thread-pool-system-status-variables.md#thread_pool_stall_limit) system variable essentially defines the limit for what a "fast query" is. If a query takes longer than [thread\_pool\_stall\_limit](thread-pool-system-status-variables.md#thread_pool_stall_limit), then the thread pool is likely to think that it is too slow, and it will either wake up a sleeping worker thread or create a new worker thread to let another client connection in the thread group run a query in parallel.

In general, changing the value of the [thread\_pool\_stall\_limit](thread-pool-system-status-variables.md#thread_pool_stall_limit) system variable has the following effect:

* Setting it to higher values can help avoid starting too many parallel threads if you expect a lot of client connections to execute long-running queries.
* Setting it to lower values can help prevent deadlocks.

### Thread Group Oversubscription

If the **timer thread** were to detect a stall in a thread group, then it would either wake up a sleeping **worker thread** or create a new **worker thread** in that thread group. At that point, the thread group would have multiple active **worker threads**. In other words, the thread group would be _oversubscribed_.

You might expect that the thread pool would shutdown one of the **worker threads** when the stalled client connection finished what it was doing, so that the thread group would only have one active **worker thread** again. However, this does not always happen. Once a thread group is oversubscribed, the [thread\_pool\_oversubscribe](thread-pool-system-status-variables.md#thread_pool_oversubscribe) system variable defines the upper limit for when **worker threads** start shutting down after they finish work for client connections. The default value is `3`. It can be changed dynamically with [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/). For example:

```sql
SET GLOBAL thread_pool_oversubscribe=10;
```

It can also be set in a server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
..
thread_handling=pool-of-threads
thread_pool_size=32
thread_pool_stall_limit=300
thread_pool_oversubscribe=10
```

To clarify, the [thread\_pool\_oversubscribe](thread-pool-system-status-variables.md#thread_pool_oversubscribe) system variable does not play any part in the creation of new **worker threads**. The [thread\_pool\_oversubscribe](thread-pool-system-status-variables.md#thread_pool_oversubscribe) system variable is only used to determine how many **worker threads** should remain active in a thread group, once a thread group is already oversubscribed due to stalls.

In general, the default value of `3` should be adequate for most users. Most users should not need to change the value of the [thread\_pool\_oversubscribe](thread-pool-system-status-variables.md#thread_pool_oversubscribe) system variable.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
