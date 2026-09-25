---
description: >-
  The GridGain generic metrics system — metric registers, exporters (JMX, SQL
  view, log, OpenCensus, OpenTelemetry), and the full catalog of available metrics.
---

# Generic Metrics

This page describes generic GridGain metrics - a new system that is designed to replace the [legacy metrics system](jmx-metrics.md). Generic metrics provide a cleaner decoupling between metric collecting/storing and viewing/exporting. This page offers the basics of the new metrics system and explains how you can use it to monitor your cluster.

There are different types of metrics in GridGain. Each metric has a name and a return value. The return value can be a simple value like `string`, `long`, or `double`. Alternatively, the value can represent a Java object. Some metrics represent [Histograms](#histograms).

There are different ways to export metrics - so called [Metric Exporters](#metric-exporters).

## Metric Registers

Metrics are grouped into categories called *registers*. Each register has a name. The full name of a specific metric within the register consists of the register name followed by a dot, followed by the name of the metric: `<register_name>.<metric_name>`.
For example, the register for data storage metrics is called `io.datastorage`. The metric that return the storage size is called `io.datastorage.StorageSize`.

## Metric Exporters

An exporter provides a mechanism for accessing all the available metrics.

GridGain includes the following exporters:

- [JMX](#jmx) (default)
- [SQL View](#sql-view)
- [Log](#log)
- [OpenCensus](#opencensus)
- [OpenTelemetry](#opentelemetry)

You can create a custom exporter by implementing the [MetricExporterSpi](https://www.gridgain.com/sdk/latest/javadoc/org/apache/ignite/spi/metric/MetricExporterSpi.html) interface.

If you want to enable metrics, configure one or multiple metric exporters in the node configuration.
This is a node-specific configuration, which means it enables metrics only on the node where it is specified.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="metricExporterSpi">
        <list>
            <bean class="org.apache.ignite.spi.metric.jmx.JmxMetricExporterSpi"/>
            <bean class="org.apache.ignite.spi.metric.log.LogExporterSpi"/>
            <bean class="org.apache.ignite.spi.metric.opencensus.OpenCensusMetricExporterSpi"/>
            <bean class="org.apache.ignite.spi.metric.otlp.OpenTelemetryMetricExporterSpi"/>
        </list>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();
cfg.setMetricExporterSpi(new JmxMetricExporterSpi());
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

The following sections describe the exporters available in Ignite by default.

### JMX

`org.apache.ignite.spi.metric.jmx.JmxMetricExporterSpi` exposes metrics via JMX beans.

{% tabs %}
{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();
JmxMetricExporterSpi jmxExporter = new JmxMetricExporterSpi();
//export cache metrics only
jmxExporter.setExportFilter(mreg -> mreg.name().startsWith("cache."));
cfg.setMetricExporterSpi(jmxExporter);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### SQL View

`SqlViewMetricExporterSpi` is enabled by default, `SqlViewMetricExporterSpi` exposes metrics via the `SYS.METRICS` view.
Each metric is displayed as a single record.
You can use any supported SQL tool to view the metrics:

```shell
> select name, value from SYS.METRICS where name LIKE 'cache.myCache.%';
+-----------------------------------+--------------------------------+
|                NAME               |             VALUE              |
+-----------------------------------+--------------------------------+
| cache.myCache.CacheTxRollbacks    | 0                              |
| cache.myCache.OffHeapRemovals     | 0                              |
| cache.myCache.QueryCompleted      | 0                              |
| cache.myCache.QueryFailed         | 0                              |
| cache.myCache.EstimatedRebalancingKeys | 0                         |
| cache.myCache.CacheEvictions      | 0                              |
| cache.myCache.CommitTime          | [J@2eb66498                    |
....
```

### Log

`org.apache.ignite.spi.metric.log.LogExporterSpi` prints the metrics to the log file at regular intervals (1 min by default) at INFO level.

{% tabs %}
{% tab title="XML" %}
```xml
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:util="http://www.springframework.org/schema/util" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="         http://www.springframework.org/schema/beans         http://www.springframework.org/schema/beans/spring-beans.xsd         http://www.springframework.org/schema/util         http://www.springframework.org/schema/util/spring-util.xsd">
    <bean class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="metricExporterSpi">
            <list>
                <bean class="org.apache.ignite.spi.metric.log.LogExporterSpi"/>
            </list>
        </property>
    </bean>
</beans>
```
{% endtab %}

{% tab title="Java" %}
If you use programmatic configuration, you can change the print frequency as follows:

```java
IgniteConfiguration cfg = new IgniteConfiguration();
LogExporterSpi logExporter = new LogExporterSpi();
logExporter.setPeriod(600_000);
//export cache metrics only
logExporter.setExportFilter(mreg -> mreg.name().startsWith("cache."));
cfg.setMetricExporterSpi(logExporter);
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### OpenCensus

`org.apache.ignite.spi.metric.opencensus.OpenCensusMetricExporterSpi` adds integration with the OpenCensus library.

To use the OpenCensus exporter:

1. [Enable the 'ignite-opencensus' module](../../gridgain8-usage/setup.md#enabling-modules).
2. Add `org.apache.ignite.spi.metric.opencensus.OpenCensusMetricExporterSpi` to the list of exporters in the node configuration.
3. Configure OpenCensus StatsCollector to export to a specific system. See [OpenCensusMetricsExporterExample.java](https://github.com/apache/ignite/blob/master/examples/src/main/java/org/apache/ignite/examples/opencensus/OpenCensusMetricsExporterExample.java) for an example and OpenCensus documentation for additional information.

Configuration parameters:

- `filter` - predicate that filters metrics.
- `period` - export period.
- `sendInstanceName` - if enabled, a tag with the Ignite instance name is added to each metric.
- `sendNodeId` - if enabled, a tag with the Ignite node id is added to each metric.
- `sendConsistentId` - if enabled, a tag with the Ignite node consistent id is added to each metric.

### OpenTelemetry

`org.apache.ignite.spi.metric.otlp.OpenTelemetryMetricExporterSpi` adds integration with [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/). When enabled, the exporter periodically sends metrics to the configured Open Telemetry exporter.

To use the OpenTelemetry exporter:

- [Enable the 'ignite-opentelemetry' module](../../gridgain8-usage/setup.md#enabling-modules).
- Add `org.apache.ignite.spi.metric.otlp.OpenTelemetryMetricExporterSpi` to the list of exporters in the node configuration.
- Configure OpenTelemetry exported to send metrics to your endpoint.

The example below shows a simple configuration:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="metricExporterSpi">
        <list>
            <bean class="org.apache.ignite.spi.metric.otlp.OpenTelemetryMetricExporterSpi">
                <property name="endpoint" value="http://my-endpoint:4317"/>
                <property name="protocol" value="GRPC"/>
                <property name="compression" value="NONE"/>
                <property name="period" value="30000"/>
                <property name="serviceNamespace" value="my-org"/>
                <property name="serviceName" value="ignite-cluster"/>
            </bean>
        </list>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

OpenTelemetryMetricExporterSpi otelExporter = new OpenTelemetryMetricExporterSpi();
otelExporter.setEndpoint("http://my-endpoint:4317");
otelExporter.setProtocol(Protocol.GRPC);
otelExporter.setCompression(Compression.GZIP);
otelExporter.setPeriod(30_000L);
otelExporter.setServiceNamespace("my-org");
otelExporter.setServiceName("ignite-cluster");
//export cache metrics only
otelExporter.setExportFilter(mreg -> mreg.name().startsWith("cache."));

cfg.setMetricExporterSpi(otelExporter);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Each node identifies itself by using the following [OpenTelemetry service resource attributes](https://opentelemetry.io/docs/specs/semconv/resource/service):

- `service.namespace` - set via `serviceNamespace`.
- `service.name` - set via `serviceName`. Defaults to the cluster tag if not specified.
- `service.instance.id` - automatically set to the node's consistent ID.

The following configuration parameters are available:

- `endpoint` - OTLP endpoint to connect to. Default value is `http://localhost:4317`.
- `protocol` - the protocol to use. Supported values are `GRPC` (default) and `HTTP`.
- `compression` - payload compression type. Supported values are `NONE` (default) and `GZIP`.
- `period` - export period in milliseconds.
- `filter` - predicate that filters metric registries. Can only be set programmatically via `setExportFilter()`. The filter operates at the register level — an entire register is either exported or skipped. For example:

  ```java
  // Export only cache metrics:
  otelExporter.setExportFilter(mreg -> mreg.name().startsWith("cache."));

  // Export everything except SQL metrics:
  otelExporter.setExportFilter(mreg -> !mreg.name().startsWith("sql."));
  ```

- `serviceNamespace` - logical namespace for the service name.
- `serviceName` - logical name of the service. Defaults to the cluster tag.
- `connectionHeaders` - arbitrary HTTP/gRPC metadata headers (e.g. authentication tokens) added to every export request. Can only be set programmatically via `setConnectionHeaders(Map)`.
- `sslEnabled` - enables SSL/TLS for the connection. Default is `false`.
- `useIgniteSslContextFactory` - if `true`, reuses the `SSLContext` factory from `IgniteConfiguration`. Default is `true`.
- `sslContextFactory` - a custom `Factory<SSLContext>` for secure connections. An instance of `SslContextFactory` is recommended as it provides both the `SSLContext` and the `TrustManager`.
- `trustManagerFactory` - a custom `Factory<TrustManager>`. Required when using a custom `sslContextFactory` that is not an instance of `SslContextFactory`.

## Available Metrics

### System

System metrics such as JVM or CPU metrics.

Register name: `sys`

|Name|Type|Description|
|---|---|---|
|CpuLoad|double|CPU load.|
|CurrentThreadCpuTime|long|The total CPU time for the current thread in nanoseconds.|
|CurrentThreadUserTime|long|The CPU time that the current thread has executed in user mode in nanoseconds.|
|DaemonThreadCount|integer|The current number of live daemon threads.|
|GcCpuLoad|double|GC CPU load.|
|PeakThreadCount|integer|The peak live thread count since the Java virtual machine started or peak was reset.|
|SystemLoadAverage|java.lang.Double|The system load average for the last minute.|
|ThreadCount|integer|The current number of live threads including both daemon and non-daemon threads.|
|TotalExecutedTasks|long|Total executed tasks.|
|TotalStartedThreadCount|long|The total number of threads created and also started since the JVM.|
|UpTime|long|The uptime of the Java virtual machine in milliseconds.|
|memory.heap.committed|long|The amount of memory in bytes that is committed for the JVM to use.|
|memory.heap.init|long|The amount of memory in bytes that the JVM initially requests from the operating system for memory management.|
|memory.heap.used|long|The amount of used memory in bytes.|
|memory.nonheap.committed|long|The amount of memory in bytes that is committed for the JVM to use.|
|memory.nonheap.init|long|The amount of memory in bytes that the JVM initially requests from the operating system for memory management.|
|memory.nonheap.max|long|The maximum amount of memory in bytes that can be used for memory management.|
|memory.nonheap.used|long|The amount of used memory in bytes.|
|memory.direct.buffers.max|long|The maximum amount of memory that can be reserved for all direct byte buffers.|
|memory.direct.buffers.totalCapacity|long|The estimated total capacity of all buffers in the direct memory pool, in bytes.|
|memory.direct.buffers.used|long|The estimated amount of memory, in bytes, currently used by the direct memory pool.|

### Caches

Cache metrics.
Register name: `cache.{cache_name}.{near}`

{% hint style="info" %}
Metrics such as `QueryCompleted`, `QueryExecuted`, `QueryFailed`, `QueryMaximumTime`, `QueryMinimalTime`, and `QuerySumTime` track operations performed via the `IgniteCache.query()` API, including scan, continuous, and text queries. However, they do not cover SQL queries executed through JDBC.
{% endhint %}

|Name|Type|Description|
|---|---|---|
|CacheEvictions|long|The total number of evictions from the cache.|
|CacheGets|long|The total number of gets to the cache.|
|CacheHits|long|The number of get requests that were satisfied by the cache.|
|CacheMisses|long|A miss is a get request that is not satisfied.|
|CachePuts|long|The total number of puts to the cache.|
|CacheRemovals|long|The total number of removals from the cache.|
|CacheTxCommits|long|Total number of transaction commits.|
|CacheTxRollbacks|long|Total number of transaction rollbacks.|
|CacheSize|long|Local cache size.|
|CommitTime|histogram|Commit time in nanoseconds.|
|CommitTimeTotal|long|The total time of commit, in nanoseconds.|
|EntryProcessorHits|long|The total number of invocations on keys, which exist in cache.|
|EntryProcessorInvokeTimeNanos|long|The total time of cache invocations for which this node is the initiator, in nanoseconds.|
|EntryProcessorMaxInvocationTime|long|So far, the maximum time to execute cache invokes for which this node is the initiator.|
|EntryProcessorMinInvocationTime|long|So far, the minimum time to execute cache invokes for which this node is the initiator.|
|EntryProcessorMisses|long|The total number of invocations on keys, which don't exist in cache.|
|EntryProcessorPuts|long|The total number of cache invocations, caused update.|
|EntryProcessorReadOnlyInvocations|long|The total number of cache invocations, caused no updates.|
|EntryProcessorRemovals|long|The total number of cache invocations, caused removals.|
|EstimatedRebalancingKeys|long|Number estimated to rebalance keys.|
|GetAllTime|histogram|GetAll time for which this node is the initiator, in nanoseconds.|
|GetTime|histogram|Get time for which this node is the initiator, in nanoseconds.|
|GetTimeTotal|long|The total time of cache gets for which this node is the initiator, in nanoseconds.|
|HeapEntriesCount|long|Onheap entries count.|
|IndexBuildPartitionsLeftCount|int|The number of local node partitions that remain to be processed to complete indexing.|
|IndexRebuildKeyProcessed|long|The number of keys with rebuilt indexes.|
|IsIndexRebuildInProgress|boolean|True if index build or rebuild is in progress.|
|OffHeapBackupEntriesCount|long|Offheap backup entries count.|
|OffHeapEntriesCount|long|Offheap entries count.|
|OffHeapEvictions|long|The total number of evictions from the off-heap memory.|
|OffHeapGets|long|The total number of get requests to the off-heap memory.|
|OffHeapHits|long|The number of get requests that were satisfied by the off-heap memory.|
|OffHeapMisses|long|A miss is a get request that is not satisfied by off-heap memory.|
|OffHeapPrimaryEntriesCount|long|Offheap primary entries count.|
|OffHeapPuts|long|The total number of put requests to the off-heap memory.|
|OffHeapRemovals|long|The total number of removals from the off-heap memory.|
|PutAllTime|histogram|PutAll time for which this node is the initiator, in nanoseconds.|
|PutTime|histogram|Put time for which this node is the initiator, in nanoseconds.|
|PutTimeTotal|long|The total time of cache puts for which this node is the initiator, in nanoseconds.|
|QueryCompleted|long|Count of completed queries.|
|QueryExecuted|long|Count of executed queries.|
|QueryFailed|long|Count of failed queries.|
|QueryMaximumTime|long|Maximum query execution time.|
|QueryMinimalTime|long|Minimum query execution time.|
|QuerySumTime|long|Query summary time.|
|RebalanceClearingPartitionsLeft|long|Number of partitions need to be cleared before actual rebalance start.|
|RebalanceStartTime|long|Rebalance start time.|
|RebalancedKeys|long|Number of already rebalanced keys.|
|RebalancingBytesRate|long|Estimated rebalancing speed in bytes.|
|RebalancingKeysRate|long|Estimated rebalancing speed in keys.|
|RemoveAllTime|histogram|RemoveAll time for which this node is the initiator, in nanoseconds.|
|RemoveTime|histogram|Remove time for which this node is the initiator, in nanoseconds.|
|RemoveTimeTotal|long|The total time of cache removal for which this node is the initiator, in nanoseconds.|
|RollbackTime|histogram|Rollback time in nanoseconds.|
|RollbackTimeTotal|long|The total time of rollback, in nanoseconds.|
|TotalRebalancedBytes|long|Number of already rebalanced bytes.|
|getCacheTouches|long|The total number of `touch()` requests to the cache. Equal to the sum of hits and misses.|
|getCacheTouchHits|long|The number of `touch()` requests that were satisfied by the cache, i.e., "hits."|
|getCacheTouchMisses|long|The number of `touch()` requests that were not satisfied by the cache, i.e., "misses," either because the requested key was not found in the cache or TTL value was not changed.|
|getCacheTouchHitPercentage|float|The percentage of cache `touch()` requests that were satisfied by the cache. Calculated as `getCacheTouchHits` divided by `getCacheTouches` multiplied by 100.|
|getCacheTouchMissPercentage|float|The percentage of cache `touch()` requests that were not satisfied by the cache. Calculated as `getCacheTouchMisses` divided by `getCacheTouches` multiplied by 100.|

### Cache Groups

Register name: `cacheGroups.{group_name}`

|Name|Type|Description|
|---|---|---|
|AffinityPartitionsAssignmentMap|java.util.Map|Affinity partitions assignment map.|
|Caches|java.util.ArrayList|List of caches|
|IndexBuildCountPartitionsLeft|long|Number of partitions need processed for finished indexes create or rebuilding.|
|LocalNodeMovingPartitionsCount|integer|Count of partitions with state `MOVING` for this cache group located on this node.|
|LocalNodeOwningPartitionsCount|integer|Count of partitions with state `OWNING` for this cache group located on this node.|
|LocalNodeRentingEntriesCount|long|Count of entries remains to evict in `RENTING` partitions located on this node for this cache group.|
|LocalNodeRentingPartitionsCount|integer|Count of partitions with state `RENTING` for this cache group located on this node.|
|MaximumNumberOfPartitionCopies|integer|Maximum number of partition copies for all partitions of this cache group.|
|MinimumNumberOfPartitionCopies|integer|Minimum number of partition copies for all partitions of this cache group.|
|MovingPartitionsAllocationMap|java.util.Map|Allocation map of partitions with state `MOVING` in the cluster.|
|OwningPartitionsAllocationMap|java.util.Map|Allocation map of partitions with state `OWNING` in the cluster.|
|PartitionIds|java.util.ArrayList|Local partition ids.|
|SparseStorageSize|long|Storage space allocated for group adjusted for possible sparsity, in bytes.|
|StorageSize|long|Storage space allocated for group, in bytes.|
|TotalAllocatedPages|long|Cache group total allocated pages.|
|TotalAllocatedSize|long|Total size of memory allocated for group, in bytes.|

### Transactions

Transaction metrics.

Register name: `tx`

|Name|Type|Description|
|---|---|---|
|AllOwnerTransactions|java.util.HashMap|Map of local node owning transactions.|
|LockedKeysNumber|long|The number of keys locked on the node.|
|OwnerTransactionsNumber|long|The number of active transactions for which this node is the initiator.|
|TransactionsHoldingLockNumber|long|The number of active transactions holding at least one key lock.|
|LastCommitTime|long|Last commit time.|
|nodeSystemTimeHistogram|histogram|Transactions system times on node represented as histogram.|
|nodeUserTimeHistogram|histogram|Transactions user times on node represented as histogram.|
|LastRollbackTime|long|Last rollback time.|
|totalNodeSystemTime|long|Total transactions system time on node.|
|totalNodeUserTime|long|Total transactions user time on node.|
|txCommits|integer|Number of transaction commits.|
|txRollbacks|integer|Number of transaction rollbacks.|
|txDeadlocks|integer|Number of transaction deadlocks.|

### Partition Map Exchange

Partition map exchange metrics.

Register name: `pme`

|Name|Type|Description|
|---|---|---|
|CacheOperationsBlockedDuration|long|Current PME cache operations blocked duration in milliseconds.|
|CacheOperationsBlockedDurationHistogram|histogram|Histogram of cache operations blocked PME durations in milliseconds.|
|Duration|long|Current PME duration in milliseconds.|
|DurationHistogram|histogram|Histogram of PME durations in milliseconds.|

### Compute Jobs

Register name: `compute.jobs`

|Name|Type|Description|
|---|---|---|
|compute.jobs.Active|long|Number of active jobs currently executing.|
|compute.jobs.Canceled|long|Number of cancelled jobs that are still running.|
|compute.jobs.ExecutionTime|long|Total execution time of jobs.|
|compute.jobs.Finished|long|Number of finished jobs.|
|compute.jobs.Rejected|long|Number of jobs rejected after more recent collision resolution operation.|
|compute.jobs.Started|long|Number of started jobs.|
|compute.jobs.Waiting|long|Number of currently queued jobs waiting to be executed.|
|compute.jobs.WaitingTime|long|Total time jobs spent on waiting queue.|

### Thread Pools

Register name: `threadPools.{thread_pool_name}`

|Name|Type|Description|
|---|---|---|
|ActiveCount|long|Approximate number of threads that are actively executing tasks.|
|CompletedTaskCount|long|Approximate total number of tasks that have completed execution.|
|CorePoolSize|long|The core number of threads.|
|KeepAliveTime|long|Thread keep-alive time, which is the amount of time which threads in excess of the core pool size may remain idle before being terminated.|
|LargestPoolSize|long|Largest number of threads that have ever simultaneously been in the pool.|
|MaximumPoolSize|long|The maximum allowed number of threads.|
|PoolSize|long|Current number of threads in the pool.|
|QueueSize|long|Current size of the execution queue.|
|RejectedExecutionHandlerClass|string|Class name of current rejection handler.|
|Shutdown|boolean|True if this executor has been shut down.|
|TaskCount|long|Approximate total number of tasks that have been scheduled for execution.|
|Terminated|boolean|True if all tasks have completed following shut down.|
|Terminating|long|True if terminating but not yet terminated.|
|ThreadFactoryClass|string|Class name of thread factory used to create new threads.|

### Cache Group IO

Register name: `io.statistics.cacheGroups.{group_name}`

|Name|Type|Description|
|---|---|---|
|LOGICAL_READS|long|Number of logical reads|
|PHYSICAL_READS|long|Number of physical reads|
|grpId|integer|Group id|
|name|string|Name of the index|
|startTime|long|Statistics collect start time|

### Sorted Indexes

Register name: `io.statistics.sortedIndexes.{cache_name}.{index_name}`

|Name|Type|Description|
|---|---|---|
|LOGICAL_READS_INNER|long|Number of logical reads for inner tree node|
|LOGICAL_READS_LEAF|long|Number of logical reads for leaf tree node|
|PHYSICAL_READS_INNER|long|Number of physical reads for inner tree node|
|PHYSICAL_READS_LEAF|long|Number of physical reads for leaf tree node|
|indexName|string|Name of the index|
|name|string|Name of the cache|
|startTime|long|Statistics collection start time|

### Hash Indexes

Register name: `io.statistics.hashIndexes.{cache_name}.{index_name}`

|Name|Type|Description|
|---|---|---|
|LOGICAL_READS_INNER|long|Number of logical reads for inner tree node|
|LOGICAL_READS_LEAF|long|Number of logical reads for leaf tree node|
|PHYSICAL_READS_INNER|long|Number of physical reads for inner tree node|
|PHYSICAL_READS_LEAF|long|Number of physical reads for leaf tree node|
|indexName|string|Name of the index|
|name|string|Name of the cache|
|startTime|long|Statistics collection start time|

### Index Operations

Register name: `index.{schema_name}.{table_name}.{index_name}`

GridGain creates one register per SQL secondary index, containing a pair of metrics for each type of B+tree page operation the index performs.
In the metric names below, `{operation}` is one of `Search`, `Insert`, `Replace`, `RemoveFromLeaf`, `AskNeighbor`, `LockTail`, `LockTailExact`, `LockTailForward`, `LockBackAndTail`, or `LockBackAndRmvFromLeaf`.

|Name|Type|Description|
|---|---|---|
|`{operation}Count`|long|Number of `{operation}` operations|
|`{operation}Time`|long|Total duration of `{operation}` operations, in nanoseconds|

These metrics are collected only while statistics are enabled for the cache the index belongs to.
If you disable statistics, the metrics stop accumulating and retain their current values; enabling statistics again resumes collection.
See [Disabling Cache Metrics](../../gridgain8-management/monitoring/configuring-metrics.md#disabling-cache-metrics).

The register is removed when the index or its cache is dropped.

To stop collecting these metrics altogether, see [Disabling Index Operation Metrics](../../gridgain8-management/monitoring/configuring-metrics.md#disabling-index-operation-metrics).

### Communication IO

Register name: `io.communication`

|Name|Type|Description|
|---|---|---|
|ActiveSessionsCount|integer|Active TCP sessions count.|
|OutboundMessagesQueueSize|integer|Outbound messages queue size.|
|SentMessagesCount|integer|Sent messages count.|
|SentBytesCount|long|Sent bytes count.|
|ReceivedBytesCount|long|Received bytes count.|
|ReceivedMessagesCount|integer|Received messages count.|
|RejectedSslSessionsCount|integer|TCP sessions count that were rejected due to the SSL errors (metric is exported only if SSL is enabled).|
|SslEnabled|boolean|Indicates whether SSL is enabled.|
|SslHandshakeDurationHistogram|histogram|Histogram of SSL handshake duration in milliseconds (metric is exported only if SSL is enabled).|

### Ignite Thin Client Connector

Register name: `client.connector`

|Name|Type|Description|
|---|---|---|
|ActiveSessionsCount|integer|Active TCP sessions count.|
|AcceptedSessionsCount|integer|Total number of TCP sessions accepted since server startup.|
|AffinityKeyRequestsHits|long|The number of affinity-aware cache key requests that were sent to the primary node.|
|AffinityKeyRequestsMisses|long|The number of affinity-aware cache key requests that missed the primary node.|
|AffinityQueryRequestsHits|long|The number of affinity-aware query requests that were sent to the primary node.|
|AffinityQueryRequestsMisses|long|The number of affinity-aware query requests that missed the primary node.|
|ReceivedBytesCount|long|Received bytes count.|
|RejectedSslSessionsCount|integer|TCP sessions count that were rejected due to the SSL errors (metric is exported only if SSL is enabled).|
|RejectedSessionsTimeout|integer|TCP sessions count that were rejected due to handshake timeout.|
|RejectedSessionsAuthenticationFailed|integer|TCP sessions count that were rejected due to failed authentication.|
|RejectedSessionsTotal|integer|Total number of rejected TCP connections.|
|`{clientType}.AcceptedSessions`|integer|Number of successfully established sessions for the client type.|
|`{clientType}.ActiveSessions`|integer|Number of active sessions for the client type.|
|SentBytesCount|long|Sent bytes count.|
|SslEnabled|boolean|Indicates whether SSL is enabled.|
|SslHandshakeDurationHistogram|histogram|Histogram of SSL handshake duration in milliseconds (metric is exported only if SSL is enabled).|

### Ignite REST Client Connector

Register name: `rest.client`

|Name|Type|Description|
|---|---|---|
|ActiveSessionsCount|integer|Active TCP sessions count.|
|ReceivedBytesCount|long|Received bytes count.|
|RejectedSslSessionsCount|integer|TCP sessions count that were rejected due to the SSL errors (metric is exported only if SSL is enabled).|
|SentBytesCount|long|Sent bytes count.|
|SslEnabled|boolean|Indicates whether SSL is enabled.|
|SslHandshakeDurationHistogram|histogram|Histogram of SSL handshake duration in milliseconds (metric is exported only if SSL is enabled).|

### Discovery IO

Register name: `io.discovery`

|Name|Type|Description|
|---|---|---|
|CoordinatorSince|long|Timestamp since which the local node became the coordinator (metric is exported only from server nodes).|
|Coordinator|UUID|Coordinator ID (metric is exported only from server nodes).|
|CurrentTopologyVersion|long|Current topology version.|
|JoinedNodes|integer|Joined nodes count.|
|LeftNodes|integer|Left nodes count.|
|MessageWorkerQueueSize|integer|Current message worker queue size.|
|PendingMessagesRegistered|integer|Pending registered messages count.|
|RejectedSslConnectionsCount|integer|TCP discovery connections count that were rejected due to the SSL errors.|
|SslEnabled|boolean|Indicates whether SSL is enabled.|
|TotalProcessedMessages|integer|Total processed messages count.|
|TotalReceivedMessages|integer|Total received messages count.|

### Data Region IO

Register name: `io.dataregion.{data_region_name}`

|Name|Type|Description|
|---|---|---|
|AllocationRate|long|Allocation rate (pages per second) averaged across rateTimeInternal.|
|CheckpointBufferSize|long|Checkpoint buffer size in bytes.|
|DirtyPages|long|Number of pages in memory not yet synchronized with persistent storage.|
|EmptyDataPages|long|Calculates empty data pages count for region. It counts only totally free pages that can be reused (e. g. pages that are contained in reuse bucket of free list).|
|EvictionRate|long|Eviction rate (pages per second).|
|LargeEntriesPagesCount|long|Count of pages that fully occupied by large entries that go beyond page size|
|OffHeapSize|long|Offheap size in bytes.|
|OffheapUsedSize|long|Offheap used size in bytes.|
|PagesFillFactor|double|The percentage of the used space.|
|PagesRead|long|Number of pages read from last restart.|
|PagesReadTime|long|Total time spent reading pages from persistent storage since last restart (nanoseconds).|
|PagesReplaceAge|long|Average age at which pages in memory are replaced with pages from persistent storage (milliseconds).|
|PagesReplaceRate|long|Rate at which pages in memory are replaced with pages from persistent storage (pages per second).|
|PagesReplaceTime|long|Total time spent replacing pages in memory with pages from persistent storage since last restart (nanoseconds).|
|PagesReplaced|long|Number of pages replaced from last restart.|
|PagesWritten|long|Number of pages written from last restart.|
|PhysicalMemoryPages|long|Number of pages residing in physical RAM.|
|PhysicalMemorySize|long|Total size of pages loaded to the RAM, in bytes.|
|SizeUsedByData|long|The number of bytes, occupied by data. Similar to `TotalUsedSize`, but it also takes into account the empty space in non-empty pages.|
|TotalUsedSize|long|Gets an amount of bytes, occupied by non-empty pages allocated in the data region|
|TotalUsedPages|long|Gets an amount of non-empty pages allocated in the data region.|
|TotalAllocatedPages|long|Total number of allocated pages.|
|TotalAllocatedSize|long|Gets a total size of memory allocated in the data region, in bytes.|
|TotalThrottlingTime|long|Total throttling threads time in milliseconds. The Ignite throttles threads that generate dirty pages during the ongoing checkpoint.|
|UsedCheckpointBufferSize|long|Gets used checkpoint buffer size in bytes|

### Data Storage

Data Storage metrics.

Register name: `io.datastorage`

|Name|Type|Description|
|---|---|---|
|CheckpointBeforeLockHistogram|histogram|Histogram of checkpoint action before taken write lock duration in milliseconds.|
|CheckpointFsyncHistogram|histogram|Histogram of checkpoint fsync duration in milliseconds.|
|CheckpointHistogram|histogram|Histogram of checkpoint duration in milliseconds.|
|CheckpointListenersExecuteHistogram|histogram|Histogram of checkpoint execution listeners under write lock duration in milliseconds.|
|CheckpointLockHoldHistogram|histogram|Histogram of checkpoint lock hold duration in milliseconds.|
|CheckpointLockWaitHistogram|histogram|Histogram of checkpoint lock wait duration in milliseconds.|
|CheckpointMarkHistogram|histogram|Histogram of checkpoint mark duration in milliseconds.|
|CheckpointPagesWriteHistogram|histogram|Histogram of checkpoint pages write duration in milliseconds.|
|CheckpointSplitAndSortPagesHistogram|histogram|Histogram of splitting and sorting checkpoint pages duration in milliseconds.|
|CheckpointTotalTime|long|Total duration of checkpoint|
|CheckpointWalRecordFsyncHistogram|histogram|Histogram of the WAL fsync after logging CheckpointRecord on begin of checkpoint duration in milliseconds.|
|CheckpointWriteEntryHistogram|histogram|Histogram of entry buffer writing to file duration in milliseconds.|
|LastCheckpointBeforeLockDuration|long|Duration of the checkpoint action before taken write lock in milliseconds.|
|LastCheckpointCopiedOnWritePagesNumber|long|Number of pages copied to a temporary checkpoint buffer during the last checkpoint.|
|LastCheckpointDataPagesNumber|long|Total number of data pages written during the last checkpoint.|
|LastCheckpointDuration|long|Duration of the last checkpoint in milliseconds.|
|LastCheckpointFsyncDuration|long|Duration of the sync phase of the last checkpoint in milliseconds.|
|LastCheckpointListenersExecuteDuration|long|Duration of the checkpoint execution listeners under write lock in milliseconds.|
|LastCheckpointLockHoldDuration|long|Duration of the checkpoint lock hold in milliseconds.|
|LastCheckpointLockWaitDuration|long|Duration of the checkpoint lock wait in milliseconds.|
|LastCheckpointMarkDuration|long|Duration of the checkpoint mark in milliseconds.|
|LastCheckpointPagesWriteDuration|long|Duration of the checkpoint pages write in milliseconds.|
|LastCheckpointTotalPagesNumber|long|Total number of pages written during the last checkpoint.|
|LastCheckpointSplitAndSortPagesDuration|long|Duration of splitting and sorting checkpoint pages of the last checkpoint in milliseconds.|
|LastCheckpointStart|long|Start timestamp of the last checkpoint.|
|LastCheckpointWalRecordFsyncDuration|long|Duration of the WAL fsync after logging CheckpointRecord on the start of the last checkpoint in milliseconds.|
|LastCheckpointWriteEntryDuration|long|Duration of entry buffer writing to file of the last checkpoint in milliseconds.|
|SparseStorageSize|long|Storage space allocated adjusted for possible sparsity, in bytes.|
|StorageSize|long|Storage space allocated, in bytes.|
|WalArchiveSegments|integer|Current number of WAL segments in the WAL archive.|
|WalBuffPollSpinsRate|long|WAL buffer poll spins number over the last time interval.|
|WalFsyncTimeDuration|long|Total duration of fsync|
|WalFsyncTimeNum|long|Total count of fsync|
|WalLastRollOverTime|long|Time of the last WAL segment rollover.|
|WalLoggingRate|long|Average number of WAL records per second written during the last time interval.|
|WalTotalSize|long|Total size in bytes for storage wal files.|
|WalWritingRate|long|Average number of bytes per second written during the last time interval.|

### Defragmentation

Defragmentation monitoring and management metrics.

Register name: `defragmentation`

|Name|Type|Description|
|---|---|---|
|inProgress|boolean|True if the defragmentation is currently in progress, false otherwise.|
|processedPartitions|integer|Number of partitions that have been processed during defragmentation.|
|totalPartitions|integer|Total number of partitions to be defragmented.|
|startTime|long|Timestamp when the current defragmentation process started.|

### Cluster

Cluster metrics.

Register name: `cluster`

|Name|Type|Description|
|---|---|---|
|ActiveBaselineNodes|integer|Active baseline nodes count.|
|Rebalanced|boolean|True if the cluster has fully achieved rebalanced state. Note that an inactive cluster always has this metric in False regardless of the real partitions state.|
|TotalBaselineNodes|integer|Total baseline nodes count.|
|TotalClientNodes|integer|Client nodes count.|
|TotalServerNodes|integer|Server nodes count.|

## SQL

SQL metrics.

### Memory Quotas

Register name: `sql.memory.quotas`

|Name|Type|Description|
|---|---|---|
|OffloadedQueriesNumber|number|Number of queries that were offloaded to disk locally|
|OffloadingRead|bytes|Number of bytes read from the disk during SQL query offloading|
|OffloadingWritten|bytes|Number of bytes written to the disk during SQL query offloading|
|freeMem|bytes|Amount of memory left available for the queries on this node, in bytes (negative value if SQL memory quotas are disabled)|
|maxMem|bytes|Total amount of memory available for all queries on the current node (negative value if SQL memory quotas are disabled)|
|requests|number|Total number of times memory quota has been requested on the current node by all the queries|

### Parser Cache

Register name: `sql.parser.cache`

|Name|Type|Description|
|---|---|---|
|hits|number|Number of hits for queries cache|
|misses|number|Number of misses for queries cache|

### User Queries

Register name: `sql.parser.cache`

|Name|Type|Description|
|---|---|---|
|canceled|number|Number of canceled queries initiated by the current node. This number is included in the general 'failed' metric.|
|failed|number|Number of failed queries (including OOME) initiated by the current node|
|failedByOOM|number|Number of queries failed due to out of memory protection initiated by the current node. This number is included in the general 'failed' metric.|
|success|number|Number of successfully executed queries initiated by the current node|

### Throttling

Throttling metrics for the Write operation. Speed-based throttling protects the checkpoint buffer and the clean pages in the region. The checkpoint buffer needs a stronger protection because an overflow of this buffer makes a node crash. When performing a Write operation, we first check whether the checkpoint buffer is in danger. If it is, we employ the exponential backoff algorithm to protect the buffer: each subsequent "sleep" time is K times longer than the previous one. If the checkpoint buffer is not in danger, we calculate the "sleep" time using the speed-based algorithm to protect the pool of clean pages.

Register name: `io.dataregion`

|Name|Type|Description|
|---|---|---|
|SpeedBasedThrottlingPercentage|double|Fraction of throttling time within average marking time (e.g., "quarter" = 0.25).|
|MarkDirtySpeed|long|Speed of marking pages dirty, in pages/second. Value is averaged over the last 3 fragments, 0.25 sec each, plus the current fragment, 0-0.25 sec (0.75-1.0 sec total).|
|CpWriteSpeed|long|Checkpoint write speed, in pages/second. Value is averaged over the last 3 checkpoints plus the current one.|
|LastEstimatedSpeedForMarkAll|long|Last estimated speed of marking all clean pages dirty to the end of a checkpoint, in pages/second.|
|CurrDirtyRatio|double|Current ratio of dirty pages (dirty vs total), expressed as a fraction. The fraction is computed for each segment in the current region, and the highest value becomes "current."|
|TargetDirtyRatio|double|Ratio of dirty pages (dirty vs total), expressed as a fraction. Throttling starts when this ratio is reached.|
|ThrottleParkTime|long|Park (sleep) time for the Write operation, in nanoseconds. Value is averaged over the last 3 fragments, 0.25 sec each, plus the current fragment, 0-0.25 sec (0.75-1.0 sec total). It defines  park periods for either the checkpoint buffer protection or the clean page pool protection.|
|CpTotalPages|int|Number of pages in the current checkpoint.|
|CpEvictedPages|int|Number of evicted pages in the current checkpoint.|
|CpWrittenPages|int|Number of written pages in the current checkpoint.|
|CpSyncedPages|int|Number of fsynced pages in the current checkpoint.|
|CheckpointBufferPagesCount|int|Number of occupied pages in the checkpoint buffer.|
|CheckpointBufferPagesSize|int|Total number of pages in the checkpoint buffer.|

## Data Center Replication

### Receiver Metrics

Register name: `dr.receiver.dc<ID>.<cacheName>`

|Attribute|Type|Description|Scope|
|---|---|---|---|
|BatchesReceived|int|Total size of batches received from remote DC <dcID>.|Node|
|EntriesReceived|long|Total number of entries received from remote DC <dcID>.|Node|
|BytesReceived|long|Total number of batches received from remote DC <dcID>.|Node|
|BytesAcked|long|Total size of batches acked from remote DC in bytes.|Node|
|EntriesAcked|long|Total number of entries acked from remote DC.|Node|
|BatchesAcked|int|Total number of batches acked from remote DC.|Node|
|BatchesSent|int|Number of batches waiting to be stored in cache.|Node|
|EntriesSent|long|Number of entries waiting to be stored in cache.|Node|
|BytesSent|long|Number of entries waiting to be stored in cache.|Node|
|AverageBatchAckTime|double|Average time in milliseconds between sending batch to receiver cache nodes and successfully storing it.|Node|

### Sender Metrics

Register name: `dr.sender.dc<ID>.<cacheName>`

|Attribute|Type|Description|Scope|
|---|---|---|---|
|BytesReceived|long|Total size of batches in bytes received by the sender from data nodes.|Node|
|EntriesReceived|long|Total number of entries were received by the sender from data nodes.|Node|
|BatchesReceived|int|Total number of batches received by the sender from data nodes.|Node|
|BatchesSent|int|Number of sent batches.|Node|
|BatchesSentFst|int|Number of full state transfer (FST) batches sent to the receiver hubs. A subset of BatchesSent.|Node|
|EntriesSent|long|Number of sent entries.|Node|
|BytesSent|long|Number of sent bytes.|Node|
|BatchesAcked|int|Number of acknowledged batches.|Node|
|BatchesAckedFst|int|Number of acknowledged full state transfer (FST) batches. A subset of BatchesAcked.|Node|
|EntriesAcked|long|Number of acknowledged sent entries.|Node|
|BytesAcked|long|Number of acknowledged bytes.|Node|
|BatchesFailed|int|Number of sent batches that caused an error.|Node|
|BatchesFailedFst|int|Number of failed full state transfer (FST) batches. A subset of BatchesFailed.|Node|
|EntriesError|long|Number of sent entries that caused an error.|Node|
|BytesError|long|Number of sent bytes that caused an error.|Node|
|AverageBatchAckTime|double|Total time in milliseconds between sending batches for the first time and receiving acknowledgement.|Node|

### Cache Metrics

Register name: `dr.cache.<cacheName>`

|Attribute|Type|Description|Scope|
|---|---|---|---|
|pendingQueueSize|long|Number of cache updates in the DR pending queue.|Node|
|backupQueueSize|long|Number of cache updates in the DR backup queue.|Node|

## Histograms

Metrics that represent histograms are available in the JMX exporter only. Histogram metrics are exported as a set of values where each value corresponds to a specific bucket, and is available through a separate JMX bean attribute. The attribute names of a histogram metric have the following format:

```
{metric_name}_{low_bound}_{high_bound}
```

where

- `{metric_name}` - the name of the metric
- `{low_bound}` - start of the bound, `0` for the first bound
- `{high_bound}` - end of the bound, `inf` for the last bound

Examples of the metric names if the bounds are [10,100]:

- histogram_0_10 - less than 10
- histogram_10_100 - between 10 and 100
- histogram_100_inf - more than 100

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
