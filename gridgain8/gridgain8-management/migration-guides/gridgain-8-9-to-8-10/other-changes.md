---
description: >-
  Deprecated APIs, changes that need no action, and the new features of GridGain 8.10 that are relevant when you upgrade from 8.9.
---

# Deprecations, Other Changes, and New Features

## Deprecations

The following still work and are deprecated:

| Deprecated | Use instead |
|---|---|
| `TRANSACTIONAL_SNAPSHOT` atomicity mode | `TRANSACTIONAL` or `ATOMIC` |
| `DataStorageConfiguration.setSystemRegionInitialSize()` and `setSystemRegionMaxSize()` | `SystemDataRegionConfiguration` |
| `IgniteConfiguration.setDefaultQueryTimeout()` and `getDefaultQueryTimeout()` | `SqlConfiguration` |
| `ClientConfiguration.setTimeout()` | `setHandshakeTimeout()` and `setRequestTimeout()` |
| `ClientConfiguration.setPartitionAwarenessEnabled()` | `setAffinityAwarenessEnabled()` |
| .NET `IgniteClientConfiguration.SocketTimeout` | `HandshakeTimeout` and `RequestTimeout` |
| `ClientCacheConfiguration` rebalance batch size, batches prefetch count, throttle, and timeout (`getRebalanceBatchSize()`, `getRebalanceBatchesPrefetchCount()`, `getRebalanceThrottle()`, `getRebalanceTimeout()`, and the matching setters) | The same properties in `IgniteConfiguration` |
| `ClientCacheConfiguration.getRebalanceDelay()` and `setRebalanceDelay()` | The baseline topology feature. These methods will be removed in a later release. |
| `ClientCacheConfiguration.getDefaultLockTimeout()` and `setDefaultLockTimeout()` | None. The property has no effect. |
| `ignite-web` module (Web Session Clustering: `WebSessionFilter`, `ServletStartup`, `ServletContextListenerStartup`) | None. The module still ships in `libs/optional` in 8.10 and will be removed in a later release. If you cluster HTTP sessions through GridGain, plan to move off it. |

## Data Center Replication

Data center replication works the same way in 8.9 and 8.10. No configuration property or `control.sh --dr` command changed, so you do not need to change the configuration of a sender hub or a receiver hub to upgrade. 8.10 changes what the hubs send to each other, and adds metrics.

### Handshake and Batch Format

When a sender hub connects to a receiver hub, the two hubs now agree on the batch format and on optional protocol features:

- The sender hub advertises the batch format versions it supports, and the receiver hub picks the highest version that both support. 8.10 supports version 2 and version 1. Version 1 is the 8.9 format.
- If the other hub does not negotiate, as in 8.9, the connection uses version 1. The connection does not fail, and nothing is logged as an error.
- The agreed version applies to one connection. A receiver hub can serve sender hubs on different versions at the same time, and the two directions between a pair of data centers can use different versions.
- An 8.10 sender hub that talks to a version 1 connection converts each batch to the 8.9 format before it sends the batch.
- 8.10 does not define any optional protocol features yet.

Both hubs write the agreed version to the log at the `INFO` level, in the message `DR batch format version agreed with sender hub` on the receiver hub, and `DR batch format version agreed with receiver hub` on the sender hub. When the receiver hub does not negotiate, the sender hub logs `Receiver hub does not negotiate the DR batch format; using version 1`.

### Replication Delay Metrics

Version 2 batches carry the time of the first and the last update in the batch. A receiver hub uses them to measure the replication delay. These metrics exist only when the sender hub and the receiver hub both run 8.10. If either runs 8.9, the connection uses version 1, and the delay metrics stay empty.

The receiver hub registers one metric registry for each pair of source data center and cache, named `dr.receiver.trace.dc<ID>.<cacheName>`. All values are in milliseconds.

| Metric | Description |
|---|---|
| `Batches` | The number of batches that the receiver hub received for this pair. |
| `BatchesWithTrace` | The number of batches that carried the time information. The difference from `Batches` is the number of batches without it. |
| `DelayFloor*` | The time from the youngest update in a batch to the moment the receiver hub receives the batch: the lowest possible delay of the batch. |
| `DelayCeiling*` | The time from the oldest update in a batch to the moment the receiver hub receives the batch: the highest possible delay of the batch. |
| `LegacyBatchesOnV2Session` | The number of version 1 batches that arrived on a connection that agreed on version 2. This happens during a rolling upgrade and while a sender hub store sends batches that it saved before the upgrade. A steady increase after that is not expected. |
| `V2BatchesOnV1Session` | The number of version 2 batches that arrived on a connection that agreed on version 1. This happens after you roll a sender hub back to 8.9 and it sends batches that 8.10 saved in its store. The receiver hub applies the data and ignores the time information. In other cases, the value is expected to stay at 0. |

Each of `DelayFloor*` and `DelayCeiling*` has these metrics: `Last`, `Max`, `Min`, `Negatives`, and `Histogram`. `Negatives` counts the batches whose delay is below 0, which means that the clock of the source data center is ahead of the clock of the receiver by at least that value. `Histogram` counts only delays that are 0 or higher.

The registries are removed when the receiver hub stops, including when the cluster is deactivated, and are created again when the next batch arrives.

### Upgrade and Recovery to 8.9

You can upgrade the sender cluster and the receiver cluster in either order. A sender hub on 8.9 replicates to a receiver hub on 8.10, and a sender hub on 8.10 replicates to a receiver hub on 8.9, over the version 1 format. The delay metrics stay empty for such a link. A receiver hub on 8.9.39 also receives the batches that a sender hub on 8.10 accumulated while replication was paused, both from the store and from the in-memory buffer of incremental replication.

A sender hub that keeps batches in its store keeps working across the upgrade. This applies to non-incremental replication, and to incremental replication with the `GG_INCREMENTAL_DR_USE_REGULAR_STORE` system property set to `true`. A sender hub on 8.10 sends the batches that 8.9 saved in its store, and the receiver hub on 8.10 counts them in `LegacyBatchesOnV2Session`.

8.10 saves batches in its store in the version 2 format, and an 8.9 node cannot read it. If you move the sender cluster back to 8.9 (see [Recovery Path](upgrade-procedure.md#recovery-path)) while the store still holds such batches, a receiver hub on 8.9 rejects them with `Unknown DR message type: 8` and closes the connection. The sender hub on 8.9 logs that it connected to the receiver again every few seconds, and no data is replicated.

To avoid this, check the `StoreSize` metric of the `dr.sender.store.global` registry on each sender hub node before you move the cluster back to 8.9 (by reverting the rolling upgrade or restoring a backup). The value is in bytes, and it is `0` when the store holds no batches. Move back only after it reaches `0`. If the cluster is already back on 8.9, upgrade the receiver hub to 8.10: it applies the stored batches and logs `V2-format DR batch on a session that negotiated version 1; the trace is ignored`.

With the default incremental replication, the sender hub does not write regular batches to the store. It keeps them in memory, and the `StoreSize` metric of the `dr.sender.buffer.global` registry shows their size. The memory is lost when the node restarts.

### Full State Transfer Counters

The sender hub metrics also count full state transfer batches separately: `batchesSentFst` and `batchesAckedFst` in `DrSenderOutCacheMetrics`, and `batchesRejectedFst` in `DrSenderInMetrics`. Each is a subset of `batchesSent`, `batchesAcked`, and `batchesRejected`.

## Other Changes and New Features

None of the following requires action to upgrade. For details on the new features, see the 8.10 release notes and the documentation of each feature.

- *Baseline auto-adjust.* New separate scale-up and scale-down timeouts are available in the Java API, `control.sh` (`--baseline scale_up_auto_adjust` and `--baseline scale_down_auto_adjust`), the MXBean, and .NET. The single timeout still works: `control.sh --baseline auto_adjust enable timeout <ms>` sets both timeouts. The output of `control.sh --baseline` now shows a separate line for scale-up and scale-down. When scale-down auto-adjust is disabled, its line shows `softTimeout=9223372036854775807` (the largest `long` value). No scale-down happens. Separate timeouts are used only when every node runs 8.10, so during a rolling upgrade the cluster keeps the single timeout. If you recover to 8.9, the separate scale-up and scale-down settings are ignored, and `control.sh --baseline` shows only the single 8.9 setting.
- *New `control.sh` commands.* `--snapshot create|restore|status|cancel` (with `--incremental`), `--baseline scale_up_auto_adjust` and `scale_down_auto_adjust`, and the `--node-ids` and `--all-nodes` options of `--system-view`. `control.sh --snapshot` is an Apache Ignite 2 compatible front end for scripts written for Apache Ignite 2. For the upgrade and recovery steps in this guide, use `snapshot-utility.sh`, which keeps working with 8.9 snapshots. A snapshot that `control.sh --snapshot create` makes also appears in `snapshot-utility.sh list` and restores with `snapshot-utility.sh restore -id=<ID>`. A snapshot that `snapshot-utility.sh` makes restores only with `snapshot-utility.sh`.
- *New tools and packages.* `bin/schema-import.sh` is included in the 8.10 distribution. The Ultimate Edition package also has an `mcp` folder with GridGain MCP Server, which is available as a separate download and as the `gridgain/mcp` container image. See [GridGain MCP Server](../../../integrations/ai/mcp-server/README.md).
- *SQL views and metrics.* New `SYS` views: `CACHE_LOCKS`, `CACHE_EXPLICIT_LOCKS`, `PLUGINS`, and `SQL_PLANS_HISTORY`. New metrics include a custom metrics API, a `snapshot` metric registry, the `communication.tcp.connectionPool` registry, and delay metrics for data center replication (see [Data Center Replication](#data-center-replication)). A role that registers custom metrics needs the new `CUSTOM_METRICS_MANAGE` system permission, for example `{system:['CUSTOM_METRICS_MANAGE']}` in the permission string.
- *Vector search.* Similarity scores, filters and keys-only queries, per-index HNSW parameters, `int8` storage, binary quantization, a `PARTITIONED` vector index, and version 2 of the thin client vector protocol. A `PARTITIONED` vector index exists only in 8.10: an 8.9 node supports a vector index only on a `REPLICATED` cache and does not start on data that has a `PARTITIONED` one (see [Recovery Path](upgrade-procedure.md#recovery-path)). Binary quantization on a `PARTITIONED` cache needs the Lucene 10 line: on the Lucene 9 line the cache fails to start with `BINARY quantization was requested but the Lucene 9.10 build of this module has no format for it`. Use the `gridgain-vector-query-lucene-10` module (see [Lucene](platform-and-modules.md#lucene)). See [Vector Search](../../../gridgain8-development/vector-search/README.md) and [Vector Search Limits](configuration-and-defaults.md#vector-search-limits).
- *Apache Ignite thin clients.* The Apache Ignite 2 Java thin client, .NET thin client, and JDBC thin driver can connect to a GridGain 8.10 server. The server recognizes an Apache Ignite client during the handshake and translates the feature flags in both directions, so GridGain clients of any version are not affected. GridGain tested the Java thin client and the JDBC driver from Apache Ignite 2.16.0, 2.17.0, and 2.18.0, and the .NET thin client from 2.18.0. Apart from the handshake, the clients behave as they do with GridGain clients, with these exceptions:
  - A client does not get the features that only GridGain has, such as the 8.10 vector search protocol.
  - The server does not support three Apache Ignite thin client features: query labels (`SqlFieldsQuery.setLabel()` and the query initiator ID are ignored), the cache configuration affinity feature, and the service call context (`SERVICE_INVOKE_CALLCTX`).
  - The JDBC driver connects with Apache Ignite protocol versions 2.9.0, 2.13.0, and 2.17.0. A connection that sets `queryEngine` to anything other than `h2` fails with `Query engine not supported: '<engine>'. Only H2 is supported.` The `local=true` connection property is ignored, and the server logs a warning: the query runs on the whole cluster, not only on the node of the connection. The transaction parameters that Apache Ignite 2.17 sends for transaction-aware queries are also ignored.
- *Java thin client.* `DataStreamer`, asynchronous overloads of the cache operations, and service awareness. With service awareness, the client sends a service call to a node that runs the service, instead of to the node it is connected to. It works only when `affinityAwarenessEnabled` is set to `true` in `ClientConfiguration` (the default is `false`) and the server is 8.10 or later.
- *.NET.* More asynchronous API methods, to match the Java API.
- *REST API.* The SQL query, SQL fields query, and scan query commands accept the `keepBinary` parameter. The default is `false`, so existing calls behave as before.
