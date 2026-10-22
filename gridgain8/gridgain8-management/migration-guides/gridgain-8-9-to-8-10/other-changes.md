---
description: >-
  Deprecated APIs, changes that need no action, and the new features of GridGain 8.10 that are relevant when you upgrade from 8.9.
---

# Deprecations, Other Changes, and New Features

This topic lists what still works but is deprecated, the changes that need no action, and the features that 8.10 adds.

## Deprecations

The following still work and are deprecated:

- `TRANSACTIONAL_SNAPSHOT` atomicity mode. Use `TRANSACTIONAL` or `ATOMIC`. Also deprecated in 8.9.38.
- `DataStorageConfiguration.setSystemRegionInitialSize()` and `setSystemRegionMaxSize()`. Use `SystemDataRegionConfiguration`.
- `IgniteConfiguration.setDefaultQueryTimeout()` and `getDefaultQueryTimeout()`. Use `SqlConfiguration`.
- `ClientConfiguration.setTimeout()`. Use `setHandshakeTimeout()` and `setRequestTimeout()`.
- `ClientConfiguration.setPartitionAwarenessEnabled()`. Use `setAffinityAwarenessEnabled()`.
- .NET `IgniteClientConfiguration.SocketTimeout`. Use `HandshakeTimeout` and `RequestTimeout`.
- The rebalance settings of `ClientCacheConfiguration`.

## Changes That Need No Action

- *Baseline auto-adjust.* New separate scale-up and scale-down timeouts are available in the Java API, `control.sh` (`--baseline scale_up_auto_adjust` and `--baseline scale_down_auto_adjust`), the MXBean, and .NET. The single timeout still works: `control.sh --baseline auto_adjust enable timeout <ms>` sets both timeouts. The output of `control.sh --baseline` now shows a separate line for scale-up and scale-down. When scale-down auto-adjust is disabled, its line shows `softTimeout=9223372036854775807` (the largest `long` value). This is not a real timeout, and no scale-down happens.
- *`VisorDataTransferObject` header check.* The header check that `VisorDataTransferObject` performs when it reads a payload now compares the full magic number. The header is written the same way in 8.9 and 8.10, so no action is needed, and only a malformed or foreign payload is rejected where it could previously pass.
- *New SQL views and metrics.* Four SQL views are new in `SYS`: `CACHE_LOCKS`, `CACHE_EXPLICIT_LOCKS`, `PLUGINS`, and `SQL_PLANS_HISTORY`. A new metric registry, `communication.tcp.connectionPool`, is available. Nothing was removed from either list.
- *New `control.sh` commands.* `--snapshot create|restore|status|cancel` (Apache Ignite style, with `--incremental`), `--baseline scale_up_auto_adjust` and `scale_down_auto_adjust`, and the `--node-ids` and `--all-nodes` options of `--system-view`. The GridGain `snapshot-utility.sh` keeps working with 8.9 snapshots (full and incremental), and it is the tool to use for the upgrade and rollback steps in this guide. `control.sh --snapshot` is an Apache Ignite 2 compatible front end for GridGain snapshots, intended for scripts written for Apache Ignite 2. It needs the Ultimate edition with snapshots configured, and otherwise fails with `Snapshots are not enabled on this GridGain cluster, Ultimate edition is required.` GridGain 8.9 has no `control.sh --snapshot` command.
- *Data center replication handshake.* The handshake between data centers now negotiates the batch format version and optional protocol features. With a peer that does not negotiate, for example an 8.9 cluster, it uses the previous format.
- *New tools and packages.* `bin/schema-import.sh` and a `mcp` folder with the GridGain MCP server are included in the 8.10 distribution.

<!-- CHECK: odd values in the `control.sh --baseline` output ("will happen in '9223370244437924903' ms" for scale-down, and a scale-up countdown that ignores the new timeout) are a question for the developers; not described here. -->
<!-- CHECK: the control.sh --snapshot text follows SnapshotCommand ("AI2 API compatible"), the VisorIgniteSnapshot*Task jobs and IgniteSnapshotTranslator in ggprivate, and GG-49474 / GG-49762. Not tested: whether a snapshot made with snapshot-utility.sh can be restored with control.sh --snapshot, or the other way round. -->
<!-- TODO Mikhail Pochatkin (GG-50908): upgrade order for two clusters connected by data center replication, and whether an 8.9 and an 8.10 cluster were run together end to end. In source the order should not matter: the batch format version is negotiated per connection, and an 8.10 sender re-encodes batches to the legacy format for an 8.9 receiver (DrProtocolVersion, DrReceiver, DrSenderRemoteDataCenterNode). Open: the sender store keeps every batch in the V2 format (DrSenderImpl, DrExternalBatchRequestV2, wire type 8), so can an 8.9 node read batches that are still in the store after a rollback of the sender cluster? The handshake text above follows the ticket (negotiation with a fallback for peers that do not negotiate, proven by wire-level tests); it is on master only and was not backported to 8.9. The DCR configuration, metric, and behavior changes for customers are also still missing. Views and registries that only appear when a feature is configured were not listed. -->

## New Features

GridGain 8.10 also adds the following features. You do not need them to upgrade, and they need no action. For details, see the 8.10 release notes and the documentation of each feature.

- *Vector search.* Similarity scores, filters and keys-only queries, per-index HNSW parameters, `int8` storage, binary quantization, a `PARTITIONED` vector index, and version 2 of the thin client vector protocol. See [Vector Search](../../../gridgain8-development/vector-search/README.md) and [Vector Search Limits](configuration-and-defaults.md#vector-search-limits).
- *Apache Ignite thin clients.* Apache Ignite thin clients can connect to a GridGain server.
- *Java thin client.* `DataStreamer`, asynchronous overloads of the cache operations, and service awareness.
- *.NET.* More asynchronous API methods, to match the Java API.
- *Compatibility with Apache Ignite 2.* The Apache Ignite snapshot API, CDC WAL records, and `keepBinary` in the REST API.
- *Metrics.* A custom metrics API, a `snapshot` metric registry, and further metrics that Apache Ignite 2 has, so that JMX metrics match it more closely. Data center replication has new handshake and delay metrics. A role that registers custom metrics needs the new `CUSTOM_METRICS_MANAGE` system permission, for example `{system:['CUSTOM_METRICS_MANAGE']}` in the permission string.

<!-- CHECK: confirm the CUSTOM_METRICS_MANAGE permission name with Viacheslav Koptilin (GG-51064). It is the only item in this list that affects a role configuration. -->
