---
description: >-
  Reference of all metrics that GridGain 9 exposes, grouped by metric source,
  with the name and meaning of each metric.
---

# Available Metrics

This topic lists all metrics available in GridGain 9.

## `caches.{cache_name}`

Cache operation metrics.

| Metric name | Description |
| --- | --- |
| Gets | Total number of requests to the cache. This will be equal to the sum of the hits and misses. |
| HitPercentage | The ratio of successful hits to the total number of gets, expressed as a fraction between 0.0 and 1.0. |
| Hits | Number of get requests that were satisfied by the cache (requested key or value exists). Contains / containsAll operations are not included in this metric. |
| MissPercentage | The ratio of misses to the total number of gets, expressed as a fraction between 0.0 and 1.0. |
| Misses | Number of get requests that were not satisfied by the cache (requested key or value does not exist). Contains / containsAll operations are not included in this metric. |
| Puts | Total number of puts to the cache. |
| Removals | Total number of removals from the cache. |

## `client.handler`

The metrics provided by the client handler and related to active clients.

| Metric name | Description |
| --- | --- |
| BytesReceived | Total number of bytes received. |
| BytesSent | Total number of bytes sent. |
| ConnectionsInitiated | Total number of initiated connections. |
| CursorsActive | Number of active cursors. |
| RequestsActive | Number of requests in progress. |
| RequestsFailed | Total number of failed requests. |
| RequestsProcessed | Total number of processed requests. |
| SessionsAccepted | Total number of accepted sessions. |
| SessionsActive | Number of currently active sessions. |
| SessionsRejected | Total number of sessions rejected due to handshake errors. |
| SessionsRejectedTimeout | Total number of sessions rejected due to a timeout. |
| SessionsRejectedTls | Total number of sessions rejected due to TLS handshake errors. |
| TransactionsActive | Number of active transactions. |

## `clock.service`

| Metric name | Description |
| --- | --- |
| ClockSkewExceedingMaxClockSkew | The observed clock skew that exceeded the maximum clock skew. |

## `dcr`

{% hint style="info" %}
These metrics become available when at least one [replication](../data-center-replication/configuring-replication.md) exists.
{% endhint %}

| Metric name | Description |
| --- | --- |
| EntriesObserved | Total number of entries received from the source cluster. |
| EntriesSent | Total number of entries sent to receiver clusters. |
| ReplicationLag | The estimated lag between an entry being sent by the source cluster and received on the target cluster, in milliseconds. |

## `expiration`

| Metric name | Description |
| --- | --- |
| DetailedExpirationMetrics | Detailed expiration metrics. |
| TotalDeletedExpiredRowsCount | Total number of deleted expired rows. |

## `index.builder`

Index builder metrics.

| Metric name | Description |
| --- | --- |
| IndexesReadingStorage | Number of indexes that are currently reading data from storage. |
| IndexesWaitingForReplica | Number of indexes that are currently waiting for a replica response. |
| IndexesWaitingForTransactions | Number of indexes that are currently waiting for transactions to complete. |
| TotalIndexesBuilding | Total number of indexes the node is currently building. |
| TransactionsWaitingFor | Number of transactions that indexes are currently waiting for. |

## `jvm`

The metrics for GridGain Java Virtual Machine resource use.

| Metric name | Description |
| --- | --- |
| gc.CollectionTime | The approximate total time spent on garbage collection in milliseconds, summed across all collectors. |
| gc.CollectionTimePercent | Percentage of time spent on garbage collection relative to JVM uptime. |
| memory.direct.buffers.Capacity | The estimated total capacity of all buffers in the direct pool. |
| memory.direct.buffers.Max | The maximum size of direct buffer allocations. |
| memory.direct.buffers.Used | The estimated amount of memory that the JVM uses for the direct buffer pool. |
| memory.heap.Committed | The committed amount of heap memory. |
| memory.heap.FreePercent | Percentage of free heap memory. |
| memory.heap.Init | The initial amount of heap memory. |
| memory.heap.Max | The maximum amount of heap memory. |
| memory.heap.Used | The currently used amount of heap memory. |
| memory.non-heap.Committed | The committed amount of non-heap memory. |
| memory.non-heap.Init | The initial amount of non-heap memory. |
| memory.non-heap.Max | The maximum amount of non-heap memory. |
| memory.non-heap.Used | The used amount of non-heap memory. |
| UpTime | The uptime of the Java virtual machine in milliseconds. |

## `license`

| Metric name | Description |
| --- | --- |
| license.DaysToLicenseExpiration | Number of days left until the license expires. |
| license.MaxHeapSize | The maximum heap size allowed. Represents the sum of configured maximum heap sizes on cluster nodes (0 is unlimited). |
| license.MaxNumberOfCores | The maximum number of cores allowed. Represents the sum of cores used for all cluster nodes (0 is unlimited). |
| license.MaxNumberOfHosts | The maximum number of hosts allowed. Represents the number of hosts where cluster nodes are located (0 is unlimited). |
| license.MaxNumberOfNodes | The maximum number of nodes allowed. Represents the total number of nodes in the cluster topology (0 is unlimited). |
| license.MaxOffheapSize | The maximum off-heap size allowed. Represents the sum of all storage profiles' sizes on cluster nodes (0 is unlimited). |
| license.MaxRamSize | The maximum RAM size allowed. Represents the sum of available RAM on all hosts (0 is unlimited). |

## `low.watermark`

The metrics in this section track the progress of the [low watermark](../storage/low-watermark.md). Use them to check whether the low watermark is still advancing, and to find what is holding it back when it is not.

| Metric name | Description |
| --- | --- |
| Current | Current low watermark, as epoch milliseconds. `0` until the first low watermark is known after node start. |
| SinceLastUpdateMillis | Time elapsed since the low watermark last advanced successfully, in milliseconds. Reset on node startup. |
| BlockingLockCount | Number of locks holding the in-flight low watermark update back. `0` when nothing holds it. |
| BlockingLockLagMillis | How far behind the data availability value some lock holds the low watermark, in milliseconds. |

## `messaging`

| Metric name | Description |
| --- | --- |
| invokeTimeouts | Total number of invocation timeouts. |
| messageHandlingFailures | Total number of message handling failures. |
| messageRecipientNotFound | Total number of message recipient resolution failures. |
| slowResponses | Total number of responses that took longer than 100ms to generate. |

## `metastorage`

| Metric name | Description |
| --- | --- |
| AvailablePeers | Number of available members of the Meta Storage voting set, calculated based on the current logical topology. |
| MajorityAvailable | `1` if the Meta Storage majority is available, `0` otherwise. Indicates whether Meta Storage can execute commands. Updated every 5 seconds. |
| IdempotentCacheSize | The current size of the cache of idempotent commands' results. |
| SafeTimeLag | Number of milliseconds the local Meta Storage SafeTime lags behind the local logical clock. |

## `mvgc`

The metrics in this section track multi-versioned storage garbage collection, which removes stale row versions below the low watermark. Use them to check whether garbage collection is keeping up with the write rate.

| Metric name | Description |
| --- | --- |
| ActiveWorkers | Number of active garbage collection worker threads. |
| QueueSize | Number of stale row versions awaiting garbage collection across all partitions on this node, measured at the last low watermark update. |
| VacuumedEntriesTotal | Total number of stale row versions removed by garbage collection on this node. |
| LastVacuumedEntries | Number of stale row versions removed by the last completed garbage collection run. |
| LastVacuumedLwm | Low watermark reached by the last completed garbage collection run, as epoch milliseconds. |
| LastRunDurationMillis | Duration of the last completed garbage collection run, in milliseconds. |
| LastRunTimestamp | Time when the last garbage collection run started, as epoch milliseconds. |

## `os`

The metrics in this section provide information about system-level metrics.

| Metric name | Description |
| --- | --- |
| AvailableProcessors | Number of processors available to the Java virtual machine. |
| CpuLoad | The system-wide CPU load. The value is between 0.0 and 1.0, where 0.0 means no CPU load and 1.0 means 100% CPU load. If the CPU load information is not available, a negative value is returned.<br><br>**Warning:** When running in containerized environments, Java 17 or higher is required to access this metric. On Java 11, 0.0 is reported instead. |
| LoadAverage | The system load average for the last minute. The system load average is the sum of the number of runnable entities queued to the available processors and the number of runnable entities running on the available processors, averaged over a period of time. The way in which the load average is calculated depends on the operating system. If the load average is not available, a negative value is returned. |

## `placement-driver`

| Metric name | Description |
| --- | --- |
| AcceptedLeases | Number of active leases. Equals the number of replication groups for which a primary replica has been elected. |
| LeaseNegotiations | Number of leases currently in negotiation. Represents the number of replication groups for which the primary replica has not yet been selected. |
| ReplicationGroups | Total number of replication groups. Each group first appears in `LeaseNegotiations`. After the primary is elected, its entry moves to `AcceptedLeases` and is removed from `LeaseNegotiations`. |

## `raft`

| Metric name | Description |
| --- | --- |
| raft.fsmcaller.disruptor.Batch | The histogram of the batch size to handle in the state machine for partitions. |
| raft.fsmcaller.disruptor.Stripes | The histogram of distribution data by stripes in the state machine for partitions. |
| raft.groups.localLeadersCount | Number of raft groups where this node is the leader. |
| raft.log.storage.CmgLogStorageSize | Number of bytes occupied on disk by the CMG log. |
| raft.log.storage.MetastorageLogStorageSize | Number of bytes occupied on disk by the Meta Storage group log. |
| raft.log.storage.PartitionsLogStorageSize | Number of bytes occupied on disk by the logs of persistent zone partitions groups. |
| raft.log.storage.PartitionsLogStorageSpilloutSize | Number of bytes occupied on disk by the spillout of volatile zone partitions groups logs. |
| raft.log.storage.TotalLogStorageSize | Number of bytes occupied on disk by logs of all replication groups. |
| raft.logmanager.disruptor.Batch | The histogram of the batch size to handle in the log for partitions. |
| raft.logmanager.disruptor.Stripes | The histogram of distribution data by stripes in the log for partitions. |
| raft.nodeimpl.disruptor.Batch | The histogram of the batch size to handle node operations for partitions. |
| raft.nodeimpl.disruptor.Stripes | The histogram of distribution data by stripes for node operations for partitions. |
| raft.readonlyservice.disruptor.Batch | The histogram of the batch size to handle read-only operations for partitions. |
| raft.readonlyservice.disruptor.Stripes | The histogram of distribution data by stripes for read-only operations for partitions. |
| raft.SaveMetaDuration | The histogram of the time taken to persist Raft metadata, in milliseconds. |

## `raft.fsmcaller.{group_id}`

State machine metrics for a single Raft group. GridGain registers one instance of this metric source for every Raft group hosted on the node, where `{group_id}` is the identifier of the group.

| Metric name | Description |
| --- | --- |
| ApplyTasksSize | The histogram of the number of tasks in an applied batch. |
| ApplyTasksTime | The histogram of the time taken to apply a batch of tasks, in milliseconds. |
| CommitTime | The histogram of the time taken to commit a task, in milliseconds. |
| ErrorDuration | The histogram of the time taken to process an error task, in milliseconds. |
| FlushDuration | The histogram of the time taken to process a flush task, in milliseconds. |
| IdleDuration | The histogram of the time taken to process an idle task, in milliseconds. |
| LeaderStartDuration | The histogram of the time taken to process a leader start task, in milliseconds. |
| LeaderStopDuration | The histogram of the time taken to process a leader stop task, in milliseconds. |
| ShutdownDuration | The histogram of the time taken to process a shutdown task, in milliseconds. |
| SnapshotLoadDuration | The histogram of the time taken to load a snapshot, in milliseconds. |
| SnapshotSaveDuration | The histogram of the time taken to save a snapshot, in milliseconds. |
| StartFollowingDuration | The histogram of the time taken to process a start following task, in milliseconds. |
| StopFollowingDuration | The histogram of the time taken to process a stop following task, in milliseconds. |

## `raft.logmanager.{group_id}`

Raft log metrics for a single Raft group. GridGain registers one instance of this metric source for every Raft group hosted on the node.

| Metric name | Description |
| --- | --- |
| AppendLogsCount | Total number of entries appended to the log. |
| AppendLogsDuration | The histogram of the time taken to append entries to the log, in milliseconds. |
| AppendLogsSize | Total size of entries appended to the log. |
| LogBytesInMemory | Estimated memory size, in bytes, of log entries currently cached in memory. |
| LogEntriesInMemory | Number of log entries currently cached in memory. |
| TruncateLogPrefixDuration | The histogram of the time taken to truncate the log prefix, in milliseconds. |
| TruncateLogSuffixDuration | The histogram of the time taken to truncate the log suffix, in milliseconds. |

## `raft.node.{group_id}`

Raft node metrics for a single Raft group. GridGain registers one instance of this metric source for every Raft group hosted on the node.

| Metric name | Description |
| --- | --- |
| AppendEntriesBatchSize | The histogram of the number of entries in a successfully handled append entries request. |
| GetLeaderDuration | The histogram of the time taken to handle a get leader request, in milliseconds. |
| HandleAppendEntriesDuration | The histogram of the time taken to handle an append entries request, in milliseconds. This path includes writing to disk. |
| HeartbeatRequestDuration | The histogram of the time taken to handle a received heartbeat request, in milliseconds. |
| InstallSnapshotDuration | The histogram of the time taken to handle an install snapshot request, in milliseconds. |
| LockBlockedCount | Number of times the node lock was contended. |
| LockBlockedDuration | The histogram of the time the node lock was blocked, in milliseconds. |
| OverloadCount | Number of times the node apply queue was overloaded. |
| PreVoteDuration | The histogram of the round-trip time of a pre-vote request, in milliseconds. Measured on the sender and includes network time. |
| ReadRequestBatchSize | The histogram of the number of entries in a read request. |
| ReadRequestDuration | The histogram of the time taken to handle a read request, in milliseconds. |
| RequestVoteDuration | The histogram of the round-trip time of a request vote request, in milliseconds. Measured on the sender and includes network time. |

## `raft.readonlyservice.{group_id}`

Read-only request metrics for a single Raft group. GridGain registers one instance of this metric source for every Raft group hosted on the node.

| Metric name | Description |
| --- | --- |
| IndexReadDuration | The histogram of the time taken to complete a read index operation, in milliseconds. |
| OverloadTimes | Number of times the read-only service was overloaded. |

## `raft.snapshots`

Metrics related to Raft snapshots of partition replicas.

| Metric name | Description |
| --- | --- |
| IncomingSnapshots | Number of incoming Raft snapshots in progress. |
| IncomingSnapshotsLoadingMeta | Number of incoming Raft snapshots loading metadata. |
| IncomingSnapshotsLoadingMvData | Number of incoming Raft snapshots loading multi-versioned data. |
| IncomingSnapshotsLoadingTxMeta | Number of incoming Raft snapshots loading transaction metadata. |
| IncomingSnapshotsPreparingIndexForBuild | Number of incoming Raft snapshots preparing indexes for build. |
| IncomingSnapshotsPreparingStorages | Number of incoming Raft snapshots preparing storages. |
| IncomingSnapshotsWaitingCatalog | Number of incoming Raft snapshots waiting for catalog. |
| OutgoingSnapshots | Number of outgoing Raft snapshots in progress. |

## `resource.vacuum`

| Metric name | Description |
| --- | --- |
| MarkedForVacuumTransactionMetaCount | The count of transaction metas that have been marked for vacuum. |
| SkippedForFurtherProcessingUnfinishedTransactionCount | The current number of unfinished transactions that are skipped by the vacuumizer for further processing. |
| VacuumizedPersistentTransactionMetaCount | The count of persistent transaction metas that have been vacuumized. |
| VacuumizedVolatileTxnMetaCount | The count of volatile transaction metas that have been vacuumized. |

## `schema.sync`

| Metric name | Description |
| --- | --- |
| Waits | Histogram of schema synchronization wait times in milliseconds. High values may indicate Meta Storage unavailability or slowness. Includes distribution buckets from 0-1ms to 5000ms+. |

## `sql.client`

SQL client metrics.

| Metric name | Description |
| --- | --- |
| OpenCursors | Number of currently open cursors. |

## `sql.memory`

| Metric name | Description |
| --- | --- |
| Limit | The SQL memory limit (bytes). |
| MaxReserved | The maximum memory usage by SQL so far (bytes). |
| Reserved | The current memory usage by SQL (bytes). |
| StatementLimit | The memory limit per SQL statement (bytes). |

## `sql.offloading`

| Metric name | Description |
| --- | --- |
| DataLimit | The SQL offloading data limit in bytes. |
| DiskUsage | The amount of space currently used by the offloading in bytes. |
| MaxDiskUsage | The maximum amount of space used by the offloading in bytes. |
| OffloadedActiveQueries | Number of active queries that have been spilled to disk. |
| OpenedFilesCount | Number of open files used for offloading. |
| TotalBytesRead | Total number of bytes read from disk by the offloading. |
| TotalBytesWritten | Total number of bytes written to disk by the offloading. |
| TotalOffloadedQueries | Total number of queries that have been spilled to disk. |
| TotalReadOperationsCount | Total number of read operations performed by the offloading. |
| TotalWriteOperationsCount | Total number of write operations performed by the offloading. |

## `sql.plan.cache`

Metrics for SQL cache planning.

| Metric name | Description |
| --- | --- |
| Hits | Total number of cache plan hits. |
| Misses | Total number of cache plan misses. |

## `sql.queries`

| Metric name | Description |
| --- | --- |
| Canceled | Total number of canceled queries. |
| ExceededMemoryQuota | Total number of queries that failed due to exceeding the memory quota. |
| Failed | Total number of failed queries. This metric includes all unsuccessful queries, regardless of reason. |
| Succeeded | Total number of successful queries. |
| TimedOut | Total number of queries that failed due to a time-out. |

## `storage.aipersist`

| Metric name | Description |
| --- | --- |
| StorageSize | Size of the entire storage in bytes. |

## `storage.aipersist.checkpoint`

| Metric name | Description |
| --- | --- |
| LastCheckpointBeforeLockDuration | The duration of actions before hold lock by the last checkpoint in milliseconds. |
| LastCheckpointDuration | The duration of the last checkpoint in milliseconds. |
| LastCheckpointFsyncDuration | The duration of the sync phase of the last checkpoint in milliseconds. |
| LastCheckpointLockHoldDuration | The duration of the last checkpoint lock hold in milliseconds. |
| LastCheckpointLockWaitDuration | The duration of the last checkpoint lock wait in milliseconds. |
| LastCheckpointPagesWriteDuration | The duration of the last checkpoint pages write in milliseconds. |
| LastCheckpointReplicatorLogSyncDuration | The duration of the replicator log sync phase of the last checkpoint in milliseconds. |
| LastCheckpointSplitAndSortPagesDuration | The duration of the split and sort dirty pages phase of the last checkpoint in milliseconds. |
| LastCheckpointTotalPagesNumber | Total number of pages written during the last checkpoint. |
| LastCheckpointWaitPageReplacementDuration | The duration of the wait page replacement phase of the last checkpoint in milliseconds. |
| ReadLockAcquisitionTime | Time from requesting checkpoint read lock until acquisition in nanoseconds. |
| ReadLockHoldTime | Duration between checkpoint read lock acquisition and release in nanoseconds. |
| ReadLockWaitingThreads | Current number of threads waiting for checkpoint read lock. |

## `storage.aipersist.consistency`

| Metric name | Description |
| --- | --- |
| RunConsistentlyActiveCount | Current number of active runConsistently calls. |
| RunConsistentlyDuration | Time spent in runConsistently closures in nanoseconds. |
| RunConsistentlyStarted | Total number of runConsistently invocations started. |

## `storage.aipersist.io`

| Metric name | Description |
| --- | --- |
| ReadsTime | Time spent in disk read operation in microseconds. |
| TotalBytesRead | Cumulative bytes read from disk since startup. |
| TotalBytesWritten | Cumulative bytes written to disk since startup. |
| WritesTime | Time spent in disk write operation in microseconds. |

## `storage.aipersist.tables.{table_name}`

| Metric name | Description |
| --- | --- |
| DeltaFilesSize | Total bytes occupied on disk by this node's delta files of a given table. |
| MainFileSize | Total bytes occupied on disk by this node's main partition files of a given table. |
| PagesFillFactor | Average fill factor of pages allocated by the `aipersist` storage engine for a given table, expressed as a percentage. Fill factor is calculated as the ratio of `TotalDataSize` to `TotalUsedSize`, multiplied by 100. |
| TotalAllocatedSize | Total size of all pages allocated by the `aipersist` storage engine for a given table, in bytes. |
| TotalDataSize | Total space occupied by data contained in pages allocated by the `aipersist` storage engine for a given table, in bytes. |
| TotalEmptySize | Total size of completely empty pages allocated by the `aipersist` storage engine for a given table, in bytes. |
| TotalUsedSize | Total size of non-empty pages allocated by the `aipersist` storage engine for a given table, in bytes. |

## `storage.aipersist.{profile}`

{% hint style="info" %}
Each [storage profile](../storage/README.md) with `aipersist` storage engine has an individual metrics exporter.
{% endhint %}

| Metric name | Description |
| --- | --- |
| CpEvictedPages | Number of evicted pages in the current checkpoint. |
| CpSyncedPages | Number of fsynced pages in the current checkpoint. |
| CpTotalPages | Number of pages in the current checkpoint. |
| CpWriteSpeed | The checkpoint write speed, in pages per second. The value is averaged over the last 3 checkpoints plus the current one. |
| CpWrittenPages | Number of written pages in the current checkpoint. |
| CurrDirtyRatio | The current ratio of dirty pages (dirty vs total), expressed as a fraction. The fraction is computed for each segment in the current region, and the highest value becomes "current." |
| DirtyPages | The current number of dirty pages in memory. |
| LastEstimatedSpeedForMarkAll | The last estimated speed of marking all clean pages dirty to the end of a checkpoint, in pages per second. |
| LoadedPages | The current number of pages loaded in memory. |
| MarkDirtySpeed | The speed of marking pages dirty, in pages per second. The value is averaged over the last 3 fragments, 0.25 sec each, plus the current fragment, 0–0.25 sec (0.75–1.0 sec total). |
| MaxSize | The maximum in-memory region size in bytes. |
| PageCacheHits | Number of times a page was found in the page cache. |
| PageCacheMisses | Number of times a page was not found in the page cache and had to be loaded from disk. |
| PageReplacements | Number of times a page was replaced (evicted) from the page cache. |
| PagesFillFactor | Average fill factor of pages allocated by the `aipersist` storage engine, expressed as a percentage. Fill factor is calculated as the ratio of `TotalDataSize` to `TotalUsedSize`, multiplied by 100. |
| PagesRead | Number of pages read from disk since the last restart. |
| PagesWritten | Number of pages written to disk since the last restart. |
| SpeedBasedThrottlingPercentage | The fraction of throttling time within average marking time (e.g., "quarter" = 0.25). |
| TargetDirtyRatio | The ratio of dirty pages (dirty vs total), expressed as a fraction. Throttling starts when this ratio is reached. |
| ThrottleParkTime | The park (sleep) time for the write operation, in nanoseconds. The value is averaged over the last 3 fragments, 0.25 sec each, plus the current fragment, 0–0.25 sec (0.75–1.0 sec total). It defines park periods for either the checkpoint buffer protection or the clean page pool protection. |
| TotalAllocatedSize | Total size of all pages allocated by the `aipersist` storage engine, in bytes. |
| TotalDataSize | Total space occupied by data contained in pages allocated by the `aipersist` storage engine, in bytes. |
| TotalEmptySize | Total size of completely empty pages allocated by the `aipersist` storage engine, in bytes. |
| TotalUsedSize | Total size of non-empty pages allocated by the `aipersist` storage engine, in bytes. |

## `storage.partition.table.{table_id}.partition.{partition_id}`

{% hint style="info" %}
Per-partition storage metrics. Disabled by default.
{% endhint %}

| Metric name | Description |
| --- | --- |
| DeltaFilesSize | Bytes occupied on disk by the delta files of the partition. |
| MainFileSize | Bytes occupied on disk by the main partition file. |

## `tables.{table_name}`

Table metrics.

| Metric name | Description |
| --- | --- |
| RoReads | Total number of reads performed within read-only transactions. |
| RwReads | Total number of reads performed within read-write transactions. |
| Writes | Total number of write operations for this table. |

## `thread.pools.{thread-pool-executor-name}`

| Metric name | Description |
| --- | --- |
| ActiveCount | The approximate number of threads that are actively executing tasks. For striped thread pools, the top-level value is the sum across all stripes. |
| ConcurrencyLevel | Concurrency level of the striped thread pool executor. |
| CompletedTaskCount | The approximate total number of tasks that have completed execution. |
| CorePoolSize | The core number of threads. |
| IdleCount | The approximate number of threads that are idle (`MaximumPoolSize` minus `ActiveCount`). For striped thread pools, the top-level value is the sum across all stripes. |
| KeepAliveTime | The thread keep-alive time, which is the amount of time threads in excess of the core pool size may remain idle before being terminated. |
| LargestPoolSize | The largest number of threads that have ever simultaneously been in the pool. |
| MaximumPoolSize | The maximum allowed number of threads. |
| PoolSize | The current number of threads in the pool. |
| QueueSize | The current size of the execution queue. For striped thread pools, the top-level value is the sum across all stripes. |
| TaskCount | The approximate total number of tasks that have been scheduled for execution. |

{% hint style="info" %}
For striped thread pools, only a subset of these metrics is exposed at the top level; the rest are available per stripe under the prefix `stripe.<index>.` (for example, `stripe.0.CompletedTaskCount`).
{% endhint %}

| Metric | Top-level (aggregated across stripes) | Per-stripe (`stripe.<index>.<metric>`) |
| --- | --- | --- |
| `ConcurrencyLevel` | Yes | No |
| `ActiveCount` | Yes (sum) | Yes |
| `IdleCount` | Yes (sum) | No |
| `QueueSize` | Yes (sum) | Yes |
| `CompletedTaskCount` | No | Yes |
| `CorePoolSize` | No | Yes |
| `KeepAliveTime` | No | Yes |
| `LargestPoolSize` | No | Yes |
| `MaximumPoolSize` | No | Yes |
| `PoolSize` | No | Yes |
| `TaskCount` | No | Yes |

## `topology.cluster`

Metrics for the cluster topology.

| Metric name | Description |
| --- | --- |
| ClusterId | The unique identifier of the cluster. |
| ClusterName | The unique name of the cluster. |
| TotalNodes | Total number of nodes in the logical topology. |

## `topology.local`

Metrics with node information.

| Metric name | Description |
| --- | --- |
| NetworkAddress | Network address of the local node. |
| NetworkPort | Network port of the local node. |
| NodeId | The unique identifier of the node. |
| NodeName | The unique name of the node. |
| NodeVersion | The GridGain version on the node. |

## `transactions`

Transaction metrics.

| Metric name | Description |
| --- | --- |
| PendingWriteIntents | Total number of unresolved write intents across all local partitions on this node. |
| RoCommits | Total number of read-only transaction commits. |
| RoDuration | The histogram representation of read-only transaction latency. |
| RoRollbacks | Total number of read-only transaction rollbacks. |
| RwCommits | Total number of read-write transaction commits. |
| RwDuration | The histogram representation of read-write transaction latency. |
| RwRollbacks | Total number of read-write transaction rollbacks. |
| TotalCommits | Total number of transaction commits. |
| TotalRollbacks | Total number of transaction rollbacks. |

## `upgrade.rolling`

| Metric name | Description |
| --- | --- |
| InitialVersion | Initial cluster version. |
| State | State of the rolling upgrade. Indicates whether a rolling upgrade is in progress or not. |
| TargetVersion | Target cluster version. May be `null` or empty if no upgrade is in progress. |
| UpgradedNodes | Set of node IDs that have been upgraded. |
| NotUpgradedNodes | Set of node IDs that have not been upgraded yet. |

## `zones.{zone_name}`

| Metric name | Description |
| --- | --- |
| LocalUnrebalancedPartitionsCount | Number of partitions that should be moved to this node. |
| TotalUnrebalancedPartitionsCount | Total number of partitions that should be moved to a new owner. |
