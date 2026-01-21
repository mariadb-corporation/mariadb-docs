# Thread Pool System and Status Variables

This article describes the system and status variables used by the MariaDB thread pool. For a full description, see [Thread Pool in MariaDB](thread-pool-in-mariadb.md).

## System variables

#### `extra_max_connections`

* Description: The number of connections on the [extra\_port](thread-pool-system-status-variables.md#extra_port).
  * See [Thread Pool in MariaDB: Configuring the Extra Port](thread-pool-in-mariadb.md#configuring-the-extra-port) for more information.
* Command line: `--extra-max-connections=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` to `100000`

#### `extra_port`

* Description: Extra port number to use for TCP connections in a `one-thread-per-connection` manner. If set to `0`, then no extra port is used.
  * See [Thread Pool in MariaDB: Configuring the Extra Port](thread-pool-in-mariadb.md#configuring-the-extra-port) for more information.
* Command line: `--extra-port=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`

#### `thread_handling`

* Description: Determines how the server handles threads for client connections. In addition to threads for client connections, this also applies to certain internal server threads, such as [Galera slave threads](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/about-galera-replication#galera-slave-threads). On Windows, if you would like to use the thread pool, then you do not need to do anything, because the default for the thread\_handling system variable is already preset to `pool-of-threads`.
  * When the default `one-thread-per-connection` mode is enabled, the server uses one thread to handle each client connection.
  * When the `pool-of-threads` mode is enabled, the server uses the [thread pool](thread-pool-in-mariadb.md) for client connections.
  * When the `no-threads` mode is enabled, the server uses a single thread for all client connections, which is really only usable for debugging.
* Command line: `--thread-handling=name`
* Scope: Global
* Dynamic: No
* Data Type: `enumeration`
* Default Value: `one-thread-per-connection` (non-Windows), `pool-of-threads` (Windows)
* Valid Values: `no-threads`, `one-thread-per-connection`, `pool-of-threads`.
* Documentation: [Using the thread pool](thread-pool-in-mariadb.md).
* Notes: In MySQL, the thread pool is only available in MySQL Enterprise. In MariaDB it's available in all versions.

#### `thread_pool_dedicated_listener`

* Description: If set to 1, then each group will have its own dedicated listener, and the listener thread will not pick up work items. As a result, the queueing time in the [Information Schema Threadpool\_Queues](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_queues-table.md) and the actual queue size in the [Information Schema Threadpool\_Groups](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_groups-table.md) table will be more exact, since\
  IO requests are immediately dequeued from poll, without delay.
  * This system variable is only meaningful on Unix.
* Command line: `thread-pool-dedicated-listener={0|1}`
* Scope:
* Dynamic:
* Data Type: `boolean`
* Default Value: `0`
* Introduced: MariaDB 10.5.0

#### `thread_pool_exact_stats`

* Description: If set to 1, provides better queueing time statistics by using a high precision timestamp, at a small performance cost, for the time when the connection was added to the queue. This timestamp helps\
  calculate the queuing time shown in the [Information Schema Threadpool\_Queues](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_queues-table.md) table.
  * This system variable is only meaningful on Unix.
* Command line: `thread-pool-exact-stats={0|1}`
* Scope:
* Dynamic:
* Data Type: `boolean`
* Default Value: `0`
* Introduced: MariaDB 10.5.0

#### `thread_pool_idle_timeout`

* Description: The number of seconds before an idle worker thread exits. The default value is `60`. If there is currently no work to do, how long should an idle thread wait before exiting?
  * This system variable is only meaningful on Unix.
  * The [thread\_pool\_min\_threads](thread-pool-system-status-variables.md#thread_pool_min_threads) system variable is comparable for Windows.
* Command line: `thread-pool-idle-timeout=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `60`
* Documentation: [Using the thread pool](thread-pool-in-mariadb.md).

#### `thread_pool_max_threads`

* Description: The maximum number of threads in the [thread pool](thread-pool-in-mariadb.md). Once this limit is reached, no new threads will be created in most cases.
  * On Unix, in rare cases, the actual number of threads can slightly exceed this, because each [thread group](thread-groups-in-the-unix-implementation-of-the-thread-pool.md) needs at least two threads (i.e. at least one worker thread and at least one listener thread) to prevent deadlocks.
* Scope:
* Command line: `thread-pool-max-threads=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `65536`
* Range: `1` to `65536`
* Documentation: [Using the thread pool](thread-pool-in-mariadb.md).

#### `thread_pool_min_threads`

* Description: Minimum number of threads in the [thread pool](thread-pool-in-mariadb.md). In bursty environments, after a period of inactivity, threads would normally be retired. When the next burst arrives, it would take time to reach the optimal level. Setting this value higher than the default would prevent thread retirement even if inactive.
  * This system variable is only meaningful on Windows.
  * The [thread\_pool\_idle\_timeout](thread-pool-system-status-variables.md#thread_pool_idle_timeout) system variable is comparable for Unix.
* Command line: `thread-pool-min-threads=#`
* Data Type: `numeric`
* Default Value: `1`
* Documentation: [Using the thread pool](thread-pool-in-mariadb.md).

#### `thread_pool_oversubscribe`

* Description: Determines how many worker threads in a thread group can remain active at the same time once a thread group is oversubscribed due to stalls. The default value is `3`. Usually, a thread group only has one active worker thread at a time. However, the timer thread can add more active worker threads to a thread group if it detects a stall. There are trade-offs to consider when deciding whether to allow only one thread per CPU to run at a time, or whether to allow more than one thread per CPU to run at a time. Allowing only one thread per CPU means that the thread can have unrestricted access to the CPU while its running, but it also means that there is additional overhead from putting threads to sleep or waking them up more frequently. Allowing more than one thread per CPU means that the threads have to share the CPU, but it also means that there is less overhead from putting threads to sleep or waking them up.
  * See [Thread Groups in the Unix Implementation of the Thread Pool: Thread Group Oversubscription](thread-groups-in-the-unix-implementation-of-the-thread-pool.md#thread-group-oversubscription) for more information.
  * This is primarily for internal use, and it is not meant to be changed for most users.
  * This system variable is only meaningful on Unix.
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `3`
* Range: `1` to `65536`
* Documentation: [Using the thread pool](thread-pool-in-mariadb.md).

#### `thread_pool_prio_kickup_timer`

* Description: Time in milliseconds before a dequeued low-priority statement is moved to the high-priority queue.
  * This system variable is only meaningful on Unix.
* Command line: `thread-pool-kickup-timer=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1000`
* Range: `0` to `4294967295`
* Introduced: MariaDB 10.2.2
* Documentation: [Using the thread pool](thread-pool-in-mariadb.md).

#### `thread_pool_priority`

* Description: [Thread pool](thread-pool-in-mariadb.md) priority. High-priority connections usually start executing earlier than low-priority.\
  If set to 'auto' (the default), the actual priority (low or high) is determined by whether or not the connection is inside a transaction.
* Command line: `--thread-pool-priority=#`
* Scope: Global,Connection
* Data Type: `enum`
* Default Value: `auto`
* Valid Values: `high`, `low`, `auto`.
* Introduced: MariaDB 10.2.2
* Documentation: [Using the thread pool](thread-pool-in-mariadb.md).

#### `thread_pool_size`

* Description: The number of [thread groups](thread-groups-in-the-unix-implementation-of-the-thread-pool.md) in the [thread pool](thread-pool-in-mariadb.md), which determines how many statements can execute simultaneously. The default value is the number of CPUs on the system. When setting this system variable's value at system startup, the max value is 100000. However, it is not a good idea to set it that high. When setting this system variable's value dynamically, the max value is either 128 or the value that was set at system startup--whichever value is higher.
  * See [Thread Groups in the Unix Implementation of the Thread Pool](thread-groups-in-the-unix-implementation-of-the-thread-pool.md) for more information.
  * This system variable is only meaningful on Unix.
* Command line: `--thread-pool-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: Based on the number of processors (but see [MDEV-7806](https://jira.mariadb.org/browse/MDEV-7806)).
* Range: `1` to `128` 
* Documentation: [Using the thread pool](thread-pool-in-mariadb.md).

#### `thread_pool_stall_limit`

* Description: The number of milliseconds between each stall check performed by the timer thread. The default value is `500`. Stall detection is used to prevent a single client connection from monopolizing a thread group. When the timer thread detects that a thread group is stalled, it wakes up a sleeping worker thread in the thread group, if one is available. If there isn't one, then it creates a new worker thread in the thread group. This temporarily allows several client connections in the thread group to run in parallel. However, note that the timer thread will not create a new worker thread if the number of threads in the thread pool is already greater than or equal to the maximum defined by the [thread\_pool\_max\_threads](thread-pool-system-status-variables.md#thread_pool_max_threads) variable, unless the thread group does not already have a listener thread.
  * See [Thread Groups in the Unix Implementation of the Thread Pool: Thread Group Stalls](thread-groups-in-the-unix-implementation-of-the-thread-pool.md#thread-group-stalls) for more information.
  * This system variable is only meaningful on Unix.
  * Note that if you are migrating from the MySQL Enterprise thread pool plugin, then the unit used in their implementation is 10ms, not 1ms.
* Command line: `--thread-pool-stall-limit=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `500`
* Range: `1` to `4294967295` 
* Documentation: [Using the thread pool](thread-pool-in-mariadb.md).

## Status variables

#### `Threadpool_idle_threads`

* Description: Number of inactive threads in the [thread pool](thread-pool-in-mariadb.md). Threads become inactive for various reasons, such as by waiting for new work. However, an inactive thread is not necessarily one that has not been assigned work. Threads are also considered inactive if they are being blocked while waiting on disk I/O, or while waiting on a lock, etc.
  * This status variable is only meaningful on Unix.
* Scope: Global, Session
* Data Type: `numeric`

#### `Threadpool_threads`

* Description: Number of threads in the [thread pool](thread-pool-in-mariadb.md). In rare cases, this can be slightly higher than [thread\_pool\_max\_threads](thread-pool-system-status-variables.md#thread_pool_max_threads), because each thread group needs at least two threads (i.e. at least one worker thread and at least one listener thread) to prevent deadlocks.
* Scope: Global, Session
* Data Type: `numeric`

## See Also

* [Thread Pool in MariaDB](thread-pool-in-mariadb.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
