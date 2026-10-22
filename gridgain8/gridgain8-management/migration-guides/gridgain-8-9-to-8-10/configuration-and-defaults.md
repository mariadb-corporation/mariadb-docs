---
description: >-
  Configuration changes when upgrading from GridGain 8.9 to 8.10: the SFTP host key default, vector search limits, startup messages, JMX metric types, and system properties.
---

# Configuration and Default Value Changes

This topic covers the defaults that change, the new limits, the startup messages for unsupported properties, the JMX metric type change, and the system properties that are new or removed.

## SFTP Snapshot Transport Verifies the Host Key by Default

This section applies if you send snapshots to an SFTP destination.

`SftpConfiguration.strictHostKeyChecking` now defaults to `true`. In 8.9.x it defaulted to `false`. Before the first snapshot transfer to an SFTP destination, add the server to the OpenSSH-format known hosts file, or set `strictHostKeyChecking` to `false` explicitly. Otherwise transfers fail. The file is the one that `knownHostsPath` points at. If `knownHostsPath` is not set, GridGain uses `~/.ssh/known_hosts` of the account that runs the node.

For more information, see [Configuring SFTP Location](../../snapshots/network-backups.md#configuring-sftp-location).

<!-- CHECK: default values verified by reading them from the 8.9.38 and 8.10 master builds; a real SFTP transfer was not run. -->

## Vector Search Limits

This section applies if you use vector search.

Vector search now enforces limits and rejects queries above them:

- The number of dimensions of a vector index is limited by `GRIDGAIN_VECTOR_MAX_DIMENSIONS`, which defaults to 4096. A vector with 4097 or more dimensions is rejected when you put it into the cache (`Field [VEC_VEC] vector's dimensions must be <= [4096]`). The limit applies to indexes that are created after the property is set, so raise it before you create indexes on wider vectors. The memory and search time of an index grow with the number of dimensions, and above 8192 dimensions a vector no longer fits into the 32 KB read buffer of the index storage, so every read spans several buffers.
- A vector query may request at most `GRIDGAIN_VECTOR_MAX_K` neighbors (default 10000). A query with `k` below 1 or above the limit is rejected with a `CacheException`, for example `Vector query 'k' is above the maximum number of neighbors a query may ask for [k=10001, max=10000]`. The limit is read in the JVM that runs the query, so set the property on the application that runs queries as a thick client, and on the server nodes for thin-client queries.

Neither limit exists in 8.9.x. For more information, see [Vector Search](../../../gridgain8-development/vector-search/README.md).

<!-- TODO RE/QA: has a vector index built on 8.9 been opened on 8.10 (rolling upgrade or restart)? Any index-format change? Not tested: 8.9.38 rejects the test license for vector search. Also not tested: the thin-client path of the k limit (confirm with Platforms). The "applies to indexes created after the property is set" wording follows the javadoc of GRIDGAIN_VECTOR_MAX_DIMENSIONS in IgniteSystemProperties; it was not run. -->

## Startup Messages for Stale Properties

This section applies if your configuration or startup scripts set Apache Ignite properties that GridGain does not support.

An unknown property in the Spring XML configuration still fails node startup, as it did in 8.9.x, but the message is now short and names the bean and the property, for example `Configuration property IgniteConfiguration.noSuchProperty does not exist`.

GridGain 8.10 also logs a warning at node start for each Apache Ignite system property or environment variable that GridGain does not support. The list is fixed: the Calcite SQL engine (`IGNITE_CALCITE_*`), `IGNITE_SNAPSHOT_SEQUENTIAL_WRITE`, the performance statistics properties (`IGNITE_PERF_STAT_*`), `IGNITE_ALLOW_MIXED_CACHE_GROUPS`, `IGNITE_ENABLE_OBJECT_INPUT_FILTER_AUTOCONFIGURATION`, `IGNITE_USE_BINARY_ARRAYS`, and `IGNITE_SQL_FORCE_LAZY_RESULT_SET`. The warning names the property and the reason and links to the Apache Ignite migration guide. The node starts normally. Remove these properties from your startup scripts.

## JMX Object Metrics Are Strings

This section applies if a JMX tool reads metrics of the `ObjectMetric` type.

Metric values of the `ObjectMetric` type are exposed through JMX as strings. A JMX tool that reads these attributes gets a `String` instead of the typed object. For example, in the `ignite` metric registry, `localNodeId` was a `UUID`, `userAttributesFormatted` and `lifecycleBeansFormatted` were `List` values, and `longJVMPauseLastEvents` was a `Map` in 8.9.x. In 8.10 all four are `String` values, and the declared attribute type is `java.lang.String`.

{% hint style="info" %}
The metric MBeans exist only if you configure `JmxMetricExporterSpi` in `IgniteConfiguration.metricExporterSpi`. The default exporter does nothing.
{% endhint %}

## System Properties

The following system properties are new or removed in 8.10:

| Property | Change |
| --- | --- |
| `IGNITE_REST_SCAN_QUERY_FILTER_CLASSES` | New. See [REST Scan Queries With a Filter Class](security-and-licensing.md#rest-scan-queries-with-a-filter-class). |
| `GRIDGAIN_VECTOR_MAX_DIMENSIONS`, `GRIDGAIN_VECTOR_MAX_K` | New. See [Vector Search Limits](#vector-search-limits). |
| `GRIDGAIN_VECTOR_BINARY_QUANTIZATION`, `GRIDGAIN_VECTOR_INDEX_DELETES_PCT`, `GRIDGAIN_VECTOR_INDEX_MAX_SEGMENTS`, `GRIDGAIN_VECTOR_INDEX_RAM_BUFFER_MB`, `GRIDGAIN_VECTOR_NOCOPY_SCORER`, `GRIDGAIN_VECTOR_QUERY_CACHE_MIN_SEGMENT_DOCS`, `GRIDGAIN_VECTOR_QUERY_CACHE_MIN_SEGMENT_SIZE_RATIO`, `GRIDGAIN_VECTOR_QUERY_THREADS` | New. Vector index and query tuning. No action is needed. `GRIDGAIN_VECTOR_BINARY_QUANTIZATION` is `false` by default. See [Vector Search](../../../gridgain8-development/vector-search/README.md). |
| `IGNITE_CUSTOM_METRICS_MAX_NAME_LENGTH` | New. Limits the length of custom metric registry and metric names. The default is 256. |
| `IGNITE_TCP_COMM_MSG_QUEUE_WARN_SIZE` | New. When set to a positive number, logs a warning when the outgoing message queue of the TCP communication SPI exceeds it. The default is 0, which prints no warning. |
| `IGNITE_BPLUS_TREE_DISABLE_METRICS` | New. Disables the metrics of the secondary index B+Trees. The default is `false`. |
| `IGNITE_LOCAL_STORE_KEEPS_PRIMARY_ONLY` | Removed with local store support. See [Local Store Support Removed](platform-and-modules.md#local-store-support-removed). |
