---
description: >-
  Reference of the built-in GridGain SQL system views in the SYS schema —
  caches, nodes, metrics, transactions, queries, statistics, and more.
---

# System Views

{% hint style="warning" %}
The system views are an experimental feature and can be changed in future releases.
{% endhint %}

GridGain provides a number of built-in SQL views that contain information about cluster nodes and node metrics.
These views are available in the SYS schema.
See the [Understanding Schemas](../../gridgain8-usage/sql/schemas.md) page for the information on how to access a non-default schema.

{% hint style="warning" %}
**Limitations**

1. You cannot create objects in the SYS schema.
2. System views from the SYS schema cannot be joined with user tables.
{% endhint %}

## BASELINE_NODE_ATTRIBUTES

The BASELINE_NODE_ATTRIBUTES view exposes node attributes fixed at a moment when a current baseline topology was set.

|Column|Data Type|Description|
|---|---|---|
|NODE_CONSISTENT_ID|VARCHAR|Node consistent ID.|
|NAME|VARCHAR|Name of the node attribute.|
|VALUE|VARCHAR|Attribute value.|

## CACHES

|Column|Data Type|Description|
|---|---|---|
|CACHE_NAME|string|Cache name.|
|CACHE_ID|int|Cache ID.|
|CACHE_TYPE|string|Cache type.|
|CACHE_MODE|string|Cache mode.|
|ATOMICITY_MODE|string|Atomicity mode.|
|CACHE_GROUP_NAME|string|Cache group name.|
|AFFINITY|string|String representation of affinity function.|
|AFFINITY_MAPPER|string|String representation of affinity mapper.|
|BACKUPS|int|backup count.|
|CACHE_GROUP_ID|int|cache group id.|
|CACHE_LOADER_FACTORY|string|String representation of cache loader factory.|
|CACHE_STORE_FACTORY|string|String representation of cache store factory.|
|CACHE_WRITER_FACTORY|string|String representation of cache writer factory.|
|DATA_REGION_NAME|string|Data region name.|
|DEFAULT_LOCK_TIMEOUT|long|Lock timeout in milliseconds.|
|EVICTION_FILTER|string|String representation of eviction filter.|
|EVICTION_POLICY_FACTORY|string|String representation of eviction policy factory.|
|EXPIRY_POLICY_FACTORY|string|String representation of expiry policy factory.|
|INTERCEPTOR|string|String representation of interceptor.|
|IS_COPY_ON_READ|boolean|Flag indicating whether a copy of the value stored in the on-heap cache.|
|IS_EAGER_TTL|boolean|Flag indicating whether expired cache entries will be eagerly removed from cache.|
|IS_ENCRYPTION_ENABLED|boolean|True if cache data encrypted.|
|IS_EVENTS_DISABLED|boolean|True if events disabled for this cache.|
|IS_INVALIDATE|boolean|True if values will be invalidated (nullified) upon commit in near cache.|
|IS_LOAD_PREVIOUS_VALUE|boolean|True if value should be loaded from store if it is not in the cache.|
|IS_MANAGEMENT_ENABLED|boolean|True if cache management operations are enabled.|
|IS_NEAR_CACHE_ENABLED|boolean|True if near cache enabled.|
|IS_ONHEAP_CACHE_ENABLED|boolean|True if on heap cache enabled.|
|IS_READ_FROM_BACKUP|boolean|True if read operation should be performed from backup node.|
|IS_READ_THROUGH|boolean|True if read from third party storage enabled.|
|IS_SQL_ESCAPE_ALL|boolean|If true all the SQL table and field names will be escaped with double quotes.|
|IS_SQL_ONHEAP_CACHE_ENABLED|boolean|If true SQL on-heap cache is enabled. When enabled, Ignite will cache SQL rows as they are accessed by query engine. Rows are invalidated and evicted from cache when relevant cache entry is either changed or evicted.|
|IS_STATISTICS_ENABLED|boolean|True if cache statistics are enabled.|
|IS_STORE_KEEP_BINARY|boolean|Flag indicating that {@link CacheStore} implementation is working with binary objects instead of Java objects.|
|IS_WRITE_BEHIND_ENABLED|boolean|Flag indicating whether Ignite should use write-behind behavior for the cache store.|
|IS_WRITE_THROUGH|boolean|True if write to third party storage enabled.|
|MAX_CONCURRENT_ASYNC_OPERATIONS|int|Maximum number of allowed concurrent asynchronous operations. If 0 returned then number of concurrent asynchronous operations is unlimited.|
|MAX_QUERY_ITERATORS_COUNT|int|Maximum number of query iterators that can be stored. Iterators are stored to support query. pagination when each page of data is sent to user's node only on demand.|
|NEAR_CACHE_EVICTION_POLICY_FACTORY|string|String representation of near cache eviction policy factory.|
|NEAR_CACHE_START_SIZE|int|Initial cache size for near cache which will be used to pre-create internal hash table after start.|
|NODE_FILTER|string|String representation of node filter.|
|PARTITION_LOSS_POLICY|string|String representation of partition loss policy.|
|QUERY_DETAIL_METRICS_SIZE|int|size of queries detail metrics that will be stored in memory for monitoring purposes. If 0 then history will not be collected.|
|QUERY_PARALLELISM|int|Hint to query execution engine on desired degree of parallelism within a single node.|
|REBALANCE_BATCH_SIZE|int|Size (in bytes) to be loaded within a single rebalance message.|
|REBALANCE_BATCHES_PREFETCH_COUNT|int|Number of batches generated by supply node at rebalancing start.|
|REBALANCE_DELAY|long|Rebalance delay in milliseconds.|
|REBALANCE_MODE|string|Rebalance mode.|
|REBALANCE_ORDER|int|Rebalance order.|
|REBALANCE_THROTTLE|long|Time in milliseconds to wait between rebalance messages to avoid overloading of CPU or network.|
|REBALANCE_TIMEOUT|long|Rebalance timeout in milliseconds.|
|SQL_INDEX_MAX_INLINE_SIZE|int|Index inline size in bytes.|
|SQL_ONHEAP_CACHE_MAX_SIZE|int|Maximum SQL on-heap cache. Measured in number of rows. When maximum size is reached oldest cached rows will be evicted.|
|SQL_SCHEMA|string|Schema name.|
|TOPOLOGY_VALIDATOR|string|String representation of topology validator.|
|WRITE_BEHIND_BATCH_SIZE|int|Maximum batch size for write-behind cache store operations.|
|WRITE_BEHIND_COALESCING|boolean|Write coalescing flag for write-behind cache store operations. Store operations (get or remove) with the same key are combined or coalesced to single, resulting operation to reduce pressure to underlying cache store.|
|WRITE_BEHIND_FLUSH_FREQUENCY|long|Frequency with which write-behind cache is flushed to the cache store in milliseconds.|
|WRITE_BEHIND_FLUSH_SIZE|int|Maximum size of the write-behind cache. If cache size exceeds this value, all cached items are flushed to the cache store and write cache is cleared.|
|WRITE_BEHIND_FLUSH_THREAD_COUNT|int|Number of threads that will perform cache flushing.|
|WRITE_SYNCHRONIZATION_MODE|string|Gets write synchronization mode.|

## CONFIGURATION

The CONFIGURATION view contains the configuration properties of node.

|Column|Data Type|Description|
|---|---|---|
|NAME|VARCHAR|Configuration property name.|
|VALUE|VARCHAR|Configuration property value.|

## DATASTREAM_THREADPOOL_QUEUE

This view exposes information about tasks waiting for the execution in the data streamer stripped thread pool.

|Column|Data Type|Description|
|---|---|---|
|STRIPE_INDEX|int|Index of the stripe thread.|
|DESCRIPTION|string|String representation of the task.|
|TASK_NAME|string|Class name of the task.|
|THREAD_NAME|string|Name of the stripe thread.|

## DISTRIBUTED_METASTORAGE

This view exposes the contents of the distributed metastorage cache.

|Column|Data type|Description|
|---|---|---|
|NAME|string|Metastorage name.|
|VALUE|string|String or raw binary (if data could not be deserialized for some reason) representation of an element.|

## DS_ATOMICLONGS

This view exposes the list of `IgniteAtomicLong`.

{% hint style="info" %}
`IgniteAtomicLong` is shown on the non-parent node only after the initial usage on that node.
{% endhint %}

|Column|Data Type|Description|
|---|---|---|
|NAME|string|Data structure name.|
|VALUE|long|Current value.|
|GROUP_NAME|string|Cache group name to store data structure.|
|GROUP_ID|int|Cache group id to store data structure.|
|REMOVED|boolean|True if removed.|

## DS_ATOMICREFERENCES

This view exposes the list of `IgniteAtomicReference`.

{% hint style="info" %}
`IgniteAtomicReference` is shown on the non-parent node only after the initial usage on that node.
{% endhint %}

|Column|Data Type|Description|
|---|---|---|
|NAME|string|Data structure name.|
|VALUE|string|Current value.|
|GROUP_NAME|string|Cache group name to store data structure.|
|GROUP_ID|int|Cache group id to store data structure.|
|REMOVED|boolean|True if removed.|

## DS_ATOMICSEQUENCES

This view exposes the list of `IgniteAtomicSequence`.

{% hint style="info" %}
`IgniteAtomicSequence` is shown on the non-parent node only after the initial usage on that node.
{% endhint %}

|Column|Data Type|Description|
|---|---|---|
|NAME|string|Data structure name.|
|VALUE|long|Current sequence value|
|BATCH_SIZE|long|Local batch size.|
|GROUP_NAME|string|Cache group name to store data structure.|
|GROUP_ID|int|Cache group id to store data structure.|
|REMOVED|boolean|True if removed.|

## DS_ATOMICSTAMPED

This view exposes the list of `IgniteAtomicStamped`.

{% hint style="info" %}
`IgniteAtomicStamped` is shown on the non-parent node only after the initial usage on that node.
{% endhint %}

|Column|Data Type|Description|
|---|---|---|
|NAME|string|Data structure name.|
|VALUE|string|Current value.|
|STAMP|string|Current stamp value|
|GROUP_NAME|string|Cache group name to store data structure.|
|GROUP_ID|int|Cache group id to store data structure.|
|REMOVED|boolean|True if removed.|

## DS_COUNTDOWNLATCHES

This view exposes the list of `IgniteCountDownLatch`.

{% hint style="info" %}
`IgniteCountDownLatch` is shown on the non-parent node only after the initial usage on that node.
{% endhint %}

|Column|Data Type|Description|
|---|---|---|
|NAME|string|Data structure name.|
|COUNT|int|Current count.|
|INITIAL_COUT|int|Initial count.|
|AUTO_DELETE|boolean|True to automatically delete the latch from a cache when its count reaches zero.|
|GROUP_NAME|string|Cache group name to store data structure.|
|GROUP_ID|int|Cache group id to store data structure.|
|REMOVED|boolean|True if removed.|

## DS_QUEUES

This view exposes the list of `IgniteQueue`.

{% hint style="info" %}
`IgniteQueue` is shown on the non-parent node only after the initial usage on that node.
{% endhint %}

|Column|Data Type|Description|
|---|---|---|
|ID|UUID|ID.|
|NAME|string|Data structure name.|
|CAPACITY|int|Capacity.|
|SIZE|int|Current size.|
|GROUP_NAME|string|Cache group name to store data structure.|
|GROUP_ID|int|Cache group id to store data structure.|
|BOUNDED|boolean|True when queue capacity is bounded.|
|COLLOCATED|boolean|True when collocated.|
|REMOVED|boolean|True if removed.|

## DS_REENTRANTLOCKS

This view exposes the contents of `IgniteLock`.

{% hint style="info" %}
`IgniteLock` is shown on the non-parent node only after the initial usage on that node.
{% endhint %}

|Column|Data Type|Description|
|---|---|---|
|NAME|string|Data structure name.|
|LOCKED|boolean|True if locked.|
|HAS_QUEUED_THREADS|boolean|True if there may be other threads waiting to acquire the lock.|
|FAILOVER_SAFE|boolean|True if failover safe.|
|FAIR|boolean|True if lock is fair.|
|BROKEN|boolean|True if a node failed on this semaphore and FAILOVER_SAFE flag was set to false; false otherwise.|
|GROUP_NAME|string|Cache group name to store data structure.|
|GROUP_ID|int|Cache group id to store data structure.|
|REMOVED|boolean|True if removed.|

## DS_SEMAPHORES

This view exposes the list of `IgniteSemaphore`.

{% hint style="info" %}
`IgniteSemaphore` is shown on the non-parent node only after the initial usage on that node.
{% endhint %}

|Column|Data Type|Description|
|---|---|---|
|NAME|string|Data structure name.|
|AVAILABLE_PERMITS|long|Number of permits available.|
|HAS_QUEUED_THREADS|boolean|True if there may be other threads waiting to acquire the lock.|
|QUEUE_LENGTH|int|The estimated number of nodes waiting for this lock.|
|FAILOVER_SAFE|boolean|True if failover safe.|
|BROKEN|boolean|True if a node failed on this semaphore and FAILOVER_SAFE flag was set to false; false otherwise.|
|GROUP_NAME|string|Cache group name to store data structure.|
|GROUP_ID|int|Cache group id to store data structure.|
|REMOVED|boolean|True if removed.|

## DS_SETS

This view exposes the list of `IgniteSet`.

{% hint style="info" %}
`IgniteSet` is shown on the non-parent node only after the initial usage on that node.
{% endhint %}

|Column|Data Type|Description|
|---|---|---|
|ID|UUID|ID.|
|NAME|string|Data structure name.|
|SIZE|int|Current size.|
|GROUP_NAME|string|Cache group name to store data structure.|
|GROUP_ID|int|Cache group id to store data structure.|
|COLLOCATED|boolean|True when collocated.|
|REMOVED|boolean|True if removed.|

## LOCAL_CACHE_GROUPS_IO

This view exposes cache group's I/O statistics.

|Column|Data Type|Description|
|---|---|---|
|CACHE_GROUP_ID|UUID|Cache group ID.|
|CACHE_GROUP_NAME|string|Cache group name.|
|PHYSICAL_READS|int|Number of physical reads from the node start or last reset (available through JMX IoStatisticsMetricsMXBean).|
|LOGICAL_READS|int|Number of logical reads from the node start or last reset (available through JMX IoStatisticsMetricsMXBean).|

## METRICS

|Column|Data Type|Description|
|---|---|---|
|NAME|string|Metric name.|
|VALUE|string|Current metric value.|
|DESCRIPTION|string|Metric description.|

## SERVICES

|Column|Data Type|Description|
|---|---|---|
|SERVICE_ID|UUID|Service ID.|
|NAME|string|Service name.|
|SERVICE_CLASS|string|Service class name.|
|CACHE_NAME|string|Cache name.|
|ORIGIN_NODE_ID|UUID|Originating node ID.|
|TOTAL_COUNT|int|Total count of service instances.|
|MAX_PER_NODE_COUNT|int|Maximum count of services instances per node.|
|AFFINITY_KEY|string|Affinity key value for service.|
|NODE_FILTER|string|String representation of node filter.|
|STATICALLY_CONFIGURED|boolean|True is service statically configured.|

## NODES

The NODES view contains information about the cluster nodes.

|Column|Data Type|Description|
|---|---|---|
|NODE_ID|UUID|Node ID.|
|CONSISTENT_ID|VARCHAR|Node's consistent ID.|
|VERSION|VARCHAR|Node version.|
|IS_CLIENT|BOOLEAN|Indicates whether the node is a client.|
|IS_DAEMON|BOOLEAN|Indicates whether the node is a daemon node.|
|NODE_ORDER|INT|Node order within the topology.|
|ADDRESSES|VARCHAR|The addresses of the node.|
|HOSTNAMES|VARCHAR|The host names of the node.|

## NODE_ATTRIBUTES

The NODE_ATTRIBUTES view contains the attributes of all nodes.

|Column|Data Type|Description|
|---|---|---|
|NODE_ID|UUID|Node ID.|
|NAME|VARCHAR|Attribute name.|
|VALUE|VARCHAR|Attribute value.|

## BASELINE_NODES

The BASELINE_NODES view contains information about the nodes that are part of the current baseline topology.

|Column|Data Type|Description|
|---|---|---|
|CONSISTENT_ID|VARCHAR|Node consistent ID.|
|ONLINE|BOOLEAN|Indicates whether the node is up and running.|

## BINARY_METADATA

This view exposes information about all available binary types.

|Column|Data type|Description|
|---|---|---|
|TYPE_ID|int|Type ID.|
|TYPE_NAME|string|Type name.|
|AFF_KEY_FIELD_NAME|string|Affinity key field name.|
|FIELDS_COUNT|int|Fields count.|
|FIELDS|string|Recorded object fields.|
|SCHEMAS_IDS|string|Schema IDs registered for this type.|
|IS_ENUM|boolean|Whether this is enum type.|

## NODE_METRICS

The NODE_METRICS view provides various metrics about the state of nodes, resource consumption and other metrics.

|Column|Data Type|Description|
|---|---|---|
|NODE_ID|UUID|Node ID.|
|LAST_UPDATE_TIME|TIMESTAMP|Last time the metrics were updated.|
|MAX_ACTIVE_JOBS|INT|Maximum number of concurrent jobs this node ever had at one time.|
|CUR_ACTIVE_JOBS|INT|Number of currently active jobs running on the node.|
|AVG_ACTIVE_JOBS|FLOAT|Average number of active jobs concurrently executing on the node.|
|MAX_WAITING_JOBS|INT|Maximum number of waiting jobs this node ever had at one time.|
|CUR_WAITING_JOBS|INT|Number of queued jobs currently waiting to be executed.|
|AVG_WAITING_JOBS|FLOAT|Average number of waiting jobs this node ever had at one time.|
|MAX_REJECTED_JOBS|INT|Maximum number of jobs rejected at once during a single collision resolution operation.|
|CUR_REJECTED_JOBS|INT|Number of jobs rejected as a result of the most recent collision resolution operation.|
|AVG_REJECTED_JOBS|FLOAT|Average number of jobs this node rejected as a result of collision resolution operations.|
|TOTAL_REJECTED_JOBS|INT|Total number of jobs this node has rejected as a result of collision resolution operations since the node startup.|
|MAX_CANCELED_JOBS|INT|Maximum number of cancelled jobs this node ever had running concurrently.|
|CUR_CANCELED_JOBS|INT|Number of cancelled jobs that are still running.|
|AVG_CANCELED_JOBS|FLOAT|Average number of cancelled jobs this node ever had running concurrently.|
|TOTAL_CANCELED_JOBS|INT|Number of jobs cancelled since the node startup.|
|MAX_JOBS_WAIT_TIME|TIME|Maximum time a job ever spent waiting in a queue before being executed.|
|CUR_JOBS_WAIT_TIME|TIME|Longest wait time among the jobs that are currently waiting for execution.|
|AVG_JOBS_WAIT_TIME|TIME|Average time jobs spend in the queue before being executed.|
|MAX_JOBS_EXECUTE_TIME|TIME|Maximum job execution time.|
|CUR_JOBS_EXECUTE_TIME|TIME|Longest time a current job has been executing for.|
|AVG_JOBS_EXECUTE_TIME|TIME|Average job execution time on this node.|
|TOTAL_JOBS_EXECUTE_TIME|TIME|Total time all finished jobs took to execute on this node since the node startup.|
|TOTAL_EXECUTED_JOBS|INT|Total number of jobs handled by the node since the node startup.|
|TOTAL_EXECUTED_TASKS|INT|Total number of tasks handled by the node.|
|TOTAL_BUSY_TIME|TIME|Total time this node spent executing jobs.|
|TOTAL_IDLE_TIME|TIME|Total time this node spent idling (not executing any jobs).|
|CUR_IDLE_TIME|TIME|Time this node has spent idling since executing the last job.|
|BUSY_TIME_PERCENTAGE|FLOAT|Percentage of job execution vs idle time.|
|IDLE_TIME_PERCENTAGE|FLOAT|Percentage of idle vs job execution time.|
|TOTAL_CPU|INT|Number of CPUs available to the Java Virtual Machine.|
|CUR_CPU_LOAD|DOUBLE|Percentage of CPU usage expressed as a fraction in the range [0, 1].|
|AVG_CPU_LOAD|DOUBLE|Average percentage of CPU usage expressed as a fraction in the range [0, 1].|
|CUR_GC_CPU_LOAD|DOUBLE|Average time spent in GC since the last update of the metrics. By default, metrics are updated every 2 seconds.|
|HEAP_MEMORY_INIT|LONG|Amount of heap memory in bytes that the JVM initially requests from the operating system for memory management. Shows `-1` if the initial memory size is undefined.|
|HEAP_MEMORY_USED|LONG|Current heap size that is used for object allocation. The heap consists of one or more memory pools. This value is the sum of used heap memory values of all heap memory pools.|
|HEAP_MEMORY_COMMITED|LONG|Amount of heap memory in bytes that is committed for the JVM to use. This amount of memory is guaranteed for the JVM to use. The heap consists of one or more memory pools. This value is the sum of committed heap memory values of all heap memory pools.|
|HEAP_MEMORY_MAX|LONG|Maximum amount of heap memory in bytes that can be used for memory management. The column displays `-1` if the maximum memory size is undefined.|
|HEAP_MEMORY_TOTAL|LONG|Total amount of heap memory in bytes. The column displays `-1` if the total memory size is undefined.|
|NONHEAP_MEMORY_INIT|LONG|Amount of non-heap memory in bytes that the JVM initially requests from the operating system for memory management. The column displays `-1` if the initial memory size is undefined.|
|NONHEAP_MEMORY_USED|LONG|Current non-heap memory size that is used by Java VM. The non-heap memory consists of one or more memory pools. This value is the sum of used non-heap memory values of all non-heap memory pools.|
|NONHEAP_MEMORY_COMMITED|LONG|Amount of non-heap memory in bytes that is committed for the JVM to use. This amount of memory is guaranteed for the JVM to use. The non-heap memory consists of one or more memory pools. This value is the sum of committed non-heap memory values of all non-heap memory pools.|
|NONHEAP_MEMORY_MAX|LONG|Returns the maximum amount of non-heap memory in bytes that can be used for memory management. The column displays `-1` if the maximum memory size is undefined.|
|NONHEAP_MEMORY_TOTAL|LONG|Total amount of non-heap memory in bytes that can be used for memory management. The column displays `-1` if the total memory size is undefined.|
|UPTIME|TIME|Uptime of the JVM.|
|JVM_START_TIME|TIMESTAMP|Start time of the JVM.|
|NODE_START_TIME|TIMESTAMP|Start time of the node.|
|LAST_DATA_VERSION|LONG|In-Memory Data Grid assigns incremental versions to all cache operations. This column contains the latest data version on the node.|
|CUR_THREAD_COUNT|INT|Number of live threads including both daemon and non-daemon threads.|
|MAX_THREAD_COUNT|INT|Maximum live thread count since the JVM started or peak was reset.|
|TOTAL_THREAD_COUNT|LONG|Total number of threads  started since the JVM started.|
|CUR_DAEMON_THREAD_COUNT|INT|Number of live daemon threads.|
|SENT_MESSAGES_COUNT|INT|Number of node communication messages sent.|
|SENT_BYTES_COUNT|LONG|Amount of bytes sent.|
|RECEIVED_MESSAGES_COUNT|INT|Number of node communication messages received.|
|RECEIVED_BYTES_COUNT|LONG|Amount of bytes received.|
|OUTBOUND_MESSAGES_QUEUE|INT|Outbound messages queue size.|
|UNACKNOWLEDGED_MESSAGES_QUEUE|INT|The number of unacknowledged messages in all communication connections of the node.|

## PAGES_TIMESTAMP_HISTOGRAM

The PAGES_TIMESTAMP_HISTOGRAM view provides information about the number of pages touched during the specific interval.

|Column|Data Type|Description|
|---|---|---|
|DATA_REGION_NAME|STRING|The name of the data region.|
|INTERVAL_START|TIMESTAMP|Start of the interval to get information for.|
|INTERVAL_END|TIMESTAMP|End of the interval to get information for.|
|PAGES_COUNT|LONG|The number of pages that were touched during the interval.|

## PARTITION_STATES

This view exposes information about the distribution of cache group partitions across cluster nodes.

|Column|Data type|Description|
|---|---|---|
|CACHE_GROUP_ID|int|Cache group ID.|
|PARTITION_ID|int|Partition ID.|
|NODE_ID|UUID|Node ID.|
|STATE|string|Partition state. Possible states: MOVING - partition is being loaded from another node to this node; OWNING - this node is either a primary or backup owner; RENTING - this node is neither primary nor back up owner (is being currently evicted); EVICTED - partition has been evicted; LOST - partition state is invalid, the partition should not be used.|
|IS_PRIMARY|boolean|Primary partition flag.|

## TRANSACTIONS

This view exposes information about currently running transactions.

|Column|Data Type|Description|
|---|---|---|
|ORIGINATING_NODE_ID|UUID|The node the transaction started from.|
|STATE|string|Current transaction status.|
|XID|UUID|Unique transaction identifier.|
|LABEL|string|Transaction label.|
|START_TIME|long|Start time of the transaction.|
|ISOLATION|string|Isolation level.|
|CONCURRENCY|string|Concurrency setting.|
|KEYS_COUNT|int|The number of keys in the transaction.|
|CACHE_IDS|string|The IDs of caches involved in the transaction.|
|COLOCATED|boolean|If the data for the transaction is colocated.|
|DHT|boolean|If the DHT is used.|
|DURATION|long|Transaction duration.|
|IMPLICIT|boolean|If the transaction is implicit.|
|IMPLICIT_SINGLE|boolean|If the transaction is part of the batch.|
|INTERNAL|boolean|If the transaction is internal.|
|LOCAL|boolean|If the transaction is performed on a local node.|
|LOCAL_NODE_ID|UUID|The id of the node.|
|NEAR|boolean|If the transaction is near.|
|ONE_PHASE_COMMIT|boolean|If the commit was done in a single phase.|
|OTHER_NODE_ID|UUID|The id of the remote node involved in the transaction.|
|SUBJECT_ID|UUID|The subject ID of the transaction.|
|SYSTEM|boolean|If the transaction is system-related.|
|THREAD_ID|long|The id of the thread involved in the transaction.|
|TIMEOUT|long|Transaction timeout.|
|TOP_VER|string|Transaction limits.|

## SQL_QUERIES

This view exposes information about currently running SQL queries.

|Column|Data Type|Description|
|---|---|---|
|QUERY_ID|UUID|Query ID.|
|SQL|string|Query text.|
|ORIGIN_NODE_ID|UUID|Node that started query.|
|START_TIME|date|Query start time.|
|DURATION|long|Query execution duration.|
|INITIATOR_ID|string|User defined query initiator ID.|
|LOCAL|boolean|True if local only.|
|SCHEMA_NAME|string|Schema name.|
|DISK_ALLOCATION_CURRENT|long|Disk allocation for the query at the current moment.|
|DISK_ALLOCATION_MAX|long|Maximum disk allocation during the query run.|
|DISK_ALLOCATION_TOTAL|long|Total disk allocation during the query run.|
|MEMORY_CURRENT|long|Current memory usage.|
|MEMORY_MAX|long|Maximum memory allocation during the query run.|
|DISTRIBUTED_JOINS|boolean|True if distributed joins for the query are enabled.|
|ENFORCE_JOIN_ORDER|boolean|True if the join order enforcement for the query is enabled.|
|LAZY|boolean|True if lazy loading of the query results is enabled.|
|LABEL|string|Query label. See [SQL Query Labels](../../ha-and-performance/performance-tuning/sql-tuning.md#sql-query-labels) for more information.|

## SQL_QUERIES_HISTORY

|Column|Data Type|Description|
|---|---|---|
|SCHEMA_NAME|string|Schema name.|
|SQL|string|Query text.|
|LOCAL|boolean|True if local only.|
|EXECUTIONS|long|Count of executions.|
|FAILURES|long|Count of failures.|
|DURATION_MIN|long|Minimal duration of execution.|
|DURATION_MAX|long|Maximum duration of execution.|
|LAST_START_TIME|date|Last execution date.|
|DISK_ALLOCATION_MIN|long|Minimum disk allocation among the query runs.|
|DISK_ALLOCATION_MAX|long|Maximum disk allocation among the query runs.|
|DISK_ALLOCATION_TOTAL_MIN|long|Minimum total disk allocation among the query runs.|
|DISK_ALLOCATION_TOTAL_MAX|long|Maximum total disk allocation among the query runs.|
|MEMORY_MIN|long|Minimum memory allocation among the query runs.|
|MEMORY_MAX|long|Maximum memory allocation among the query runs.|
|DISTRIBUTED_JOINS|boolean|True if distributed joins were enabled during the query execution.|
|ENFORCE_JOIN_ORDER|boolean|True if the join order enforcement was enabled during the query execution.|
|LAZY|boolean|True if lazy loading of the query results was enabled during the query execution.|

## SCHEMAS

This view exposes information about SQL schemas.

|Column|Data Type|Description|
|---|---|---|
|NAME|string|Name of the schema|
|PREDEFINED|boolean|If true, schema is predefined.|

## TASKS

This view exposes information about currently running compute tasks started by a node. For instance, let's assume that an
application started a compute task using the Ignite thick client and the task's job was executed on one of the server nodes.
In this case, the thick client will report statistics related to the task via this system view while the server node will
be updating the thick client with task-related execution details.

|Column|Data Type|Description|
|---|---|---|
|ID|UUID|Task id.|
|SESSION_ID|UUID|Session id.|
|TASK_NODE_ID|UUID|Task originating node id.|
|TASK_NAME|string|Task name.|
|TASK_CLASS_NAME|string|Task class name.|
|AFFINITY_PARTITION_ID|int|Cache partition id.|
|AFFINITY_CACHE_NAME|string|Cache name.|
|START_TIME|long|Start time.|
|END_TIME|long|End time.|
|EXEC_NAME|string|Thread pool name executing task.|
|INTERNAL|boolean|True if task is internal.|
|USER_VERSION|string|Task user version.|

## JOBS

This system view shows a list of compute jobs started by a node as part of a compute task.
To view the status of the compute task refer to the `TASKS` system view.

|Column|Data Type|Description|
|---|---|---|
|ID|UUID|Job ID|
|SESSION_ID|UUID|Job's session ID. Note, `SESSION_ID` is equal to `TASKS.SESSION_ID` for the jobs belonging to a specific task.|
|ORIGIN_NODE_ID|UUID|The id of the node that started the job.|
|TASK_NAME|string|The name of the task.|
|TASK_CLASSNAME|string|Class name of the task.|
|AFFINITY_CACHE_IDS|string|IDs of one or more caches if the job is executed against one of the `IgniteCompute.affinity` methods. The parameter is empty, if you use `IgniteCompute` APIs that don't target specific caches.|
|AFFINITY_PARTITION_ID|int|IDs of one or more partitions if the job is executed via one of the `IgniteCompute.affinity` methods. The parameter is empty, if you use `IgniteCompute` APIs that don't target specific partitions.|
|CREATE_TIME|long|Job's creation time.|
|START_TIME|long|Job's start time.|
|FINISH_TIME|long|Job's finish time.|
|EXECUTOR_NAME|string|The name of the task's executor.|
|IS_FINISHING|boolean|`True` if the job is finishing.|
|IS_INTERNAL|boolean|`True` if the job is internal.|
|IS_STARTED|boolean|`True` if the job has been started.|
|IS_TIMEDOUT|boolean|`True` if the job timed out before completing.|
|STATE|string|Possible values:<br>`ACTIVE` - Job is being executed.<br>`PASSIVE` - Job is added to the execution queue (see `CollisionSPI` for details).<br>`CANCELED` - Job is canceled.|

## TABLES

The TABLES view contains information about the SQL tables.

|Column|Data Type|Description|
|---|---|---|
|CACHE_GROUP_ID|INT|The id of the cache group.|
|CACHE_GROUP_NAME|VARCHAR|The name of the cache group.|
|CACHE_ID|INT|The ID of the cache corresponding to the table.|
|CACHE_NAME|VARCHAR|The name of the cache corresponding to the table.|
|SCHEMA_NAME|VARCHAR|The name of the schema.|
|TABLE_NAME|VARCHAR|The name of the table.|
|AFFINITY_KEY_COLUMN|VARCHAR|The column that is used as the affinity key.|
|KEY_ALIAS|VARCHAR|The alias for the key fields.|
|VALUE_ALIAS|VARCHAR|The alias for the value field.|
|KEY_TYPE_NAME|VARCHAR|The type of the key field.|
|VALUE_TYPE_NAME|VARCHAR|The type of the value field.|
|BINARY_AFFINITY_FIELD|VARCHAR|The name of the affinity field declared on the key binary type, if any.|

## TABLE_COLUMNS

This view exposes information about SQL table columns.

|Column|Data Type|Description|
|---|---|---|
|AFFINITY_COLUMN|boolean|True if the column is the affinity key.|
|AUTO_INCREMENT|boolean|True if auto incremented.|
|COLUMN_NAME|string|Column name.|
|DEFAULT_VALUE|string|Default column value.|
|NULLABLE|boolean|True if nullable.|
|PK|boolean|True if primary key.|
|PRECISION|int|Column precision.|
|SCALE|int|Column scale.|
|SCHEMA_NAME|string|Schema name.|
|TABLE_NAME|string|Table name.|
|TYPE|string|Column type.|

## VIEWS

This view exposes information about SQL views.

|Column|Data Type|Description|
|---|---|---|
|NAME|string|Name|
|SCHEMA|string|Schema.|
|DESCRIPTION|string|Description.|

## VIEW_COLUMNS

This view exposes information about SQL views columns.

|Column|Data Type|Description|
|---|---|---|
|COLUMN_NAME|string|Name of the column.|
|DEFAULT_VALUE|string|Column default value.|
|NULLABLE|boolean|True if column nullable.|
|PRECISION|int|Column precision.|
|SCALE|int|Column scale.|
|SCHEMA_NAME|string|Name of the view.|
|TYPE|string|Column type.|
|VIEW_NAME|string|Name of the view.|

## CACHE_GROUPS

The CACHE_GROUPS view contains information about the [cache groups](../../gridgain8-usage/configuring-caches/cache-groups.md).

|Column|Data Type|Description|
|---|---|---|
|CACHE_GROUP_ID|INT|The ID of the cache group.|
|CACHE_GROUP_NAME|VARCHAR|The name of the cache group.|
|IS_SHARED|BOOLEAN|If this group contains more than one cache.|
|CACHE_COUNT|INT|The number of caches in the cache group.|
|CACHE_MODE|VARCHAR|The cache mode.|
|ATOMICITY_MODE|VARCHAR|The [atomicity mode](../../gridgain8-usage/configuring-caches/atomicity-modes.md) of the cache group.|
|AFFINITY|VARCHAR|The string representation of the affinity function defined for the cache group.|
|PARTITIONS_COUNT|INT|The number of partitions.|
|NODE_FILTER|VARCHAR|The string representation of the node filter defined for the cache group.|
|DATA_REGION_NAME|VARCHAR|The name of the [data region](../../gridgain8-usage/memory-configuration/data-regions.md).|
|TOPOLOGY_VALIDATOR|VARCHAR|The string representation of the topology validator defined for the cache group.|
|PARTITION_LOSS_POLICY|VARCHAR|[Partition loss policy](../../architecture/rebalancing/partition-loss-policy.md).|
|REBALANCE_MODE|VARCHAR|[Rebalancing mode](../../architecture/rebalancing/data-rebalancing.md#configuring-rebalancing-mode).|
|REBALANCE_DELAY|LONG|[Rebalancing delay](../../architecture/rebalancing/data-rebalancing.md#other-properties).|
|REBALANCE_ORDER|INT|[Rebalancing order](../../architecture/rebalancing/data-rebalancing.md#other-properties).|
|BACKUPS|INT|The number of [backup partitions](../../gridgain8-usage/configuring-caches/configuring-backups.md) configured for the cache group.|

## CACHE_GROUP_PAGE_LISTS

|Column|Data Type|Description|
|---|---|---|
|CACHE_GROUP_ID|int|Cache group ID.|
|PARTITION_ID|int|Partition ID.|
|NAME|string|Page list name.|
|BUCKET_NUMBER|int|Bucket number.|
|BUCKET_SIZE|long|Count of pages in the bucket.|
|STRIPES_COUNT|int|Count of stripes used by this bucket. Stripes are used to avoid contention.|
|CACHED_PAGES_COUNT|int|Count of pages in an on-heap page list cache for this bucket.|
|PAGE_FREE_SPACE|int|Free space (in bytes) available to use for each page in this bucket.|

## DATA_REGION_PAGE_LISTS

|Column|Data Type|Description|
|---|---|---|
|NAME|string|Page list name.|
|BUCKET_NUMBER|int|Bucket number.|
|BUCKET_SIZE|long|Count of pages in the bucket.|
|STRIPES_COUNT|int|Count of stripes used by this bucket. Stripes are used to avoid contention.|
|CACHED_PAGES_COUNT|int|Count of pages in an on-heap page list cache for this bucket.|
|PAGE_FREE_SPACE|int|Free space (in bytes) available to use for each page in this bucket.|

## STRIPED_THREADPOOL_QUEUE

This view exposes information about tasks waiting for the execution in the system striped thread pool.

|Column|Data Type|Description|
|---|---|---|
|DESCRIPTION|string|String representation of the task.|
|STRIPE_INDEX|int|Index of the stripe thread.|
|TASK_NAME|string|Class name of the task.|
|THREAD_NAME|string|Name of the stripe thread.|

## SCAN_QUERIES

This view exposes information about currently running scan queries.

|Column|Data Type|Description|
|---|---|---|
|CACHE_GROUP_ID|int|Cache group ID.|
|CACHE_GROUP_NAME|string|Cache group name.|
|CACHE_ID|int|Cache ID.|
|CACHE_NAME|string|Cache name.|
|CANCELED|boolean|True if canceled.|
|DURATION|long|Query duration.|
|FILTER|string|String representation of filter.|
|KEEP_BINARY|boolean|True if keepBinary enabled.|
|LOCAL|boolean|True if query local only.|
|ORIGIN_NODE_ID|UUID|Node id started query.|
|PAGE_SIZE|int|Page size.|
|PARTITION|int|Query partition ID.|
|QUERY_ID|long|Query ID.|
|START_TIME|long|Query start time.|
|SUBJECT_ID|UUID|User ID started query.|
|TASK_NAME|string|Task name.|
|TOPOLOGY|string|Topology version.|
|TRANSFORMER|string|String representation of transformer.|

## CONTINUOUS_QUERIES

This view exposes information about currently running continuous queries.

|Column|Data Type|Description|
|---|---|---|
|AUTO_UNSUBSCRIBE|boolean|True if query should be stopped when node disconnected or originating node left.|
|BUFFER_SIZE|int|Event batch buffer size.|
|CACHE_NAME|string|Cache name.|
|DELAYED_REGISTER|boolean|True if query would be started when corresponding cache started.|
|INTERVAL|long|Notify interval.|
|IS_EVENTS|boolean|True if used for subscription to remote events.|
|IS_MESSAGING|boolean|True if used for subscription to messages.|
|IS_QUERY|boolean|True if user started continuous query.|
|KEEP_BINARY|boolean|True if keepBinary enabled.|
|LAST_SEND_TIME|long|Last time event batch sent to query originating node.|
|LOCAL_LISTENER|string|String representation of local listener.|
|LOCAL_TRANSFORMED_LISTENER|string|String representation of local transformed listener.|
|NODE_ID|UUID|Originating node id.|
|NOTIFY_EXISTING|boolean|True if listener should be notified about existing entries.|
|OLD_VALUE_REQUIRED|boolean|True if old entry value should be included in event.|
|REMOTE_FILTER|string|String representation of remote filter.|
|REMOTE_TRANSFORMER|string|String representation of remote transformer.|
|ROUTINE_ID|UUID|Query ID.|
|TOPIC|string|Query topic name.|

## CLIENT_CONNECTIONS

This view exposes information about currently opened client connections: JDBC, ODBC, Thin clients.

|Column|Data Type|Description|
|---|---|---|
|CONNECTION_ID|long|ID of the connection.|
|LOCAL_ADDRESS|IP|address  IP address of the local node.|
|REMOTE_ADDRESS|IP|address  IP address of the remote node.|
|TYPE|string|Type of the connection.|
|USER|string|User name.|
|VERSION|string|Protocol version.|

## CLIENT_CONNECTION_ATTRIBUTES

The CLIENT_CONNECTION_ATTRIBUTES view exposes user defined attributes of client connections (thin, JDBC, ODBC). Attributes for the connection are provided by clients. For example, attributes for java thin client can be specified using `ClientConfiguration.setUserAttributes` method.

|Column|Data Type|Description|
|---|---|---|
|CONNECTION_ID|long|ID of the connection.|
|NAME|VARCHAR|Name of the attribute.|
|VALUE|VARCHAR|Attribute value.|

## INDEXES

The INDEXES view contains information about SQL indexes.

|Column|Data Type|Description|
|---|---|---|
|INDEX_NAME|VARCHAR|The name of the index.|
|INDEX_TYPE|VARCHAR|The type of the index.|
|COLUMNS|VARCHAR|The columns included in the index.|
|SCHEMA_NAME|VARCHAR|The schema name.|
|TABLE_NAME|VARCHAR|The table name.|
|CACHE_GROUP_ID|VARCHAR|The cache group ID.|
|CACHE_GROUP_NAME|VARCHAR|The cache group name.|
|CACHE_NAME|VARCHAR|The cache name.|
|CACHE_ID|INT|Cache ID.|
|INLINE_SIZE|INT|The [inline size](../../ha-and-performance/performance-tuning/sql-tuning.md#increasing-index-inline-size) in bytes.|
|IS_PK|BOOLEAN|Indicates whether the index is for the primary key.|
|IS_UNIQUE|BOOLEAN|Indicates if the index is unique.|

## STATISTICS_CONFIGURATION

The STATISTICS_CONFIGURATION view contains information about [SQL statistics](../sql-statistics.md) configuration.

|Column|Data Type|Description|
|---|---|---|
|SCHEMA|VARCHAR|Schema name.|
|TYPE|VARCHAR|Object type.|
|NAME|VARCHAR|Object name.|
|COLUMN|VARCHAR|Column name.|
|MAX_PARTITION_OBSOLESCENCE_PERCENT|TINYINT|Maximum percentage of obsolescent rows in statistics. See the [SQL Statistics](../sql-statistics.md#statistics-obsolescence) page for more details.|
|MANUAL_NULLS|BIGINT|If not null - overridden number of null values.|
|MANUAL_DISTINCT|BIGINT|If not null - overridden number of distinct values.|
|MANUAL_TOTAL|BIGINT|If not null - overridden total number of values.|
|MANUAL_SIZE|INT|If not null - overridden average size of non null values in column.|
|VERSION|BIGINT|Configuration version.|

## STATISTICS_LOCAL_DATA

The STATISTICS_LOCAL_DATA view contains [SQL statistics](../sql-statistics.md) for locally managed (or stored) data. This view is node-specific, so each node has an instance of the view that contains information about its local data statistics.

|Column|Data Type|Description|
|---|---|---|
|SCHEMA|VARCHAR|Schema name.|
|TYPE|VARCHAR|Object type.|
|NAME|VARCHAR|Object name.|
|COLUMN|VARCHAR|Column name.|
|ROWS_COUNT|BIGINT|Count of column rows.|
|DISTINCT|BIGINT|Number of unique non-null values.|
|NULLS|BIGINT|Number of null values.|
|TOTAL|BIGINT|Total number of values in column.|
|SIZE|INTEGER|Average value size in bytes.|
|VERSION|BIGINT|Statistics version.|
|LAST_UPDATE_TIME|VARCHAR|Maximum time of all partition statistics which was used to generate local one.|

## STATISTICS_PARTITION_DATA

The STATISTICS_PARTITION_DATA view contains information about [SQL statistics](../sql-statistics.md) on every partition data stored on a local node.

|Column|Data Type|Description|
|---|---|---|
|SCHEMA|VARCHAR|Schema name.|
|TYPE|VARCHAR|Object type.|
|NAME|VARCHAR|Object name.|
|COLUMN|VARCHAR|Column name.|
|PARTITION|INTEGER|Partition number.|
|ROWS_COUNT|BIGINT|Count of column rows.|
|UPDATE_COUNTER|BIGINT|Partition counter update when statistics are collected.|
|DISTINCT|BIGINT|Number of unique non-null values.|
|NULLS|BIGINT|Number of null values.|
|TOTAL|BIGINT|Total number of values in column.|
|SIZE|INTEGER|Average value size in bytes.|
|VERSION|BIGINT|Statistics version.|
|LAST_UPDATE_TIME|VARCHAR|Maximum time of all partition statistics which was used to generate local one.|

## SERVICES_DISTRIBUTION

|Column|Data Type|Description|
|---|---|---|
|NODEID|UUID|ID of the node the service runs on.|
|SERVICEID|UUID|Service ID.|
|SERVICESCOUNT|INTEGER|Total number of service instances.|

## Examples

To query the system views using the [SQLLine](../tools/sqlline.md) tool, connect to the SYS schema as follows:

```shell
./sqlline.sh -u jdbc:ignite:thin://127.0.0.1/SYS
```

If your node is running on a remote server, replace `127.0.0.1` with the IP address of the server.

Run a query:

```sql
-- get the list of nodes
select * from NODES;

-- view the CPU load as a percentage for a specific node
select CUR_CPU_LOAD * 100 from NODE_METRICS where NODE_ID = 'a1b77663-b37f-4ddf-87a6-1e2d684f3bae'

```

The same example using [Java Thin Client]({connectors}/thin-clients/java-thin-client):

```java
ClientConfiguration cfg = new ClientConfiguration().setAddresses("127.0.0.1:10800");

try (IgniteClient igniteClient = Ignition.startClient(cfg)) {

    // getting the id of the first node
    UUID nodeId = (UUID) igniteClient.query(new SqlFieldsQuery("SELECT * from NODES").setSchema("SYS"))
    .getAll().iterator().next().get(0);

    double cpu_load = (double) igniteClient
    .query(new SqlFieldsQuery("select CUR_CPU_LOAD * 100 from NODE_METRICS where NODE_ID = ? ")
    .setSchema("SYS").setArgs(nodeId.toString()))
    .getAll().iterator().next().get(0);

    System.out.println("node's cpu load = " + cpu_load);

} catch (ClientException e) {
    System.err.println(e.getMessage());
} catch (Exception e) {
    System.err.format("Unexpected failure: %s\n", e);
}

```

You can also query system views in the Control Center UI, form the **SQL** screen. Add `SYS.` before the view name; for example: `select * FROM SYS.CLIENT_CONNECTIONS;`.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
