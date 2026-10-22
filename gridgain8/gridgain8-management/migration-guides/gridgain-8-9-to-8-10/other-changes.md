---
description: >-
  Deprecated APIs, changes that need no action, and the new features of GridGain 8.10 that are relevant when you upgrade from 8.9.
---

# Deprecations, Other Changes, and New Features

## Deprecations

The following still work and are deprecated:

- `TRANSACTIONAL_SNAPSHOT` atomicity mode. Use `TRANSACTIONAL` or `ATOMIC`. Also deprecated in 8.9.38.
- `DataStorageConfiguration.setSystemRegionInitialSize()` and `setSystemRegionMaxSize()`. Use `SystemDataRegionConfiguration`.
- `IgniteConfiguration.setDefaultQueryTimeout()` and `getDefaultQueryTimeout()`. Use `SqlConfiguration`.
- `ClientConfiguration.setTimeout()`. Use `setHandshakeTimeout()` and `setRequestTimeout()`.
- `ClientConfiguration.setPartitionAwarenessEnabled()`. Use `setAffinityAwarenessEnabled()`.
- .NET `IgniteClientConfiguration.SocketTimeout`. Use `HandshakeTimeout` and `RequestTimeout`.
- The rebalance settings of `ClientCacheConfiguration`.

## Other Changes and New Features

None of the following requires action to upgrade. For details on the new features, see the 8.10 release notes and the documentation of each feature.

- *Baseline auto-adjust.* New separate scale-up and scale-down timeouts are available in the Java API, `control.sh` (`--baseline scale_up_auto_adjust` and `--baseline scale_down_auto_adjust`), the MXBean, and .NET. The single timeout still works: `control.sh --baseline auto_adjust enable timeout <ms>` sets both timeouts. The output of `control.sh --baseline` now shows a separate line for scale-up and scale-down. When scale-down auto-adjust is disabled, its line shows `softTimeout=9223372036854775807` (the largest `long` value). No scale-down happens. Separate timeouts are used only when every node runs 8.10, so during a rolling upgrade the cluster keeps the single timeout.
- *New `control.sh` commands.* `--snapshot create|restore|status|cancel` (with `--incremental`), `--baseline scale_up_auto_adjust` and `scale_down_auto_adjust`, and the `--node-ids` and `--all-nodes` options of `--system-view`. `control.sh --snapshot` is an Apache Ignite 2 compatible front end for scripts written for Apache Ignite 2. For the upgrade and rollback steps in this guide, use `snapshot-utility.sh`, which keeps working with 8.9 snapshots. A snapshot that `control.sh --snapshot create` makes also appears in `snapshot-utility.sh list` and restores with `snapshot-utility.sh restore -id=<ID>`. A snapshot that `snapshot-utility.sh` makes restores only with `snapshot-utility.sh`.
- *Data center replication handshake.* The handshake between data centers now negotiates the batch format version and optional protocol features. With a peer that does not negotiate, for example an 8.9 cluster, it uses the previous format.
- *New tools and packages.* `bin/schema-import.sh` and a `mcp` folder with the GridGain MCP server are included in the 8.10 distribution.
- *SQL views and metrics.* New `SYS` views: `CACHE_LOCKS`, `CACHE_EXPLICIT_LOCKS`, `PLUGINS`, and `SQL_PLANS_HISTORY`. New metrics include a custom metrics API, a `snapshot` metric registry, the `communication.tcp.connectionPool` registry, and handshake and delay metrics for data center replication. A role that registers custom metrics needs the new `CUSTOM_METRICS_MANAGE` system permission, for example `{system:['CUSTOM_METRICS_MANAGE']}` in the permission string.
- *Vector search.* Similarity scores, filters and keys-only queries, per-index HNSW parameters, `int8` storage, binary quantization, a `PARTITIONED` vector index, and version 2 of the thin client vector protocol. See [Vector Search](../../../gridgain8-development/vector-search/README.md) and [Vector Search Limits](configuration-and-defaults.md#vector-search-limits).
- *Apache Ignite thin clients.* Apache Ignite thin clients can connect to a GridGain server.
- *Java thin client.* `DataStreamer`, asynchronous overloads of the cache operations, and service awareness. With service awareness, the client sends a service call to a node that runs the service, instead of to the node it is connected to. It works only when `affinityAwarenessEnabled` is set to `true` in `ClientConfiguration` (the default is `false`) and the server is 8.10 or later.
- *.NET.* More asynchronous API methods, to match the Java API.
- *REST API.* The SQL query, SQL fields query, and scan query commands accept the `keepBinary` parameter. The default is `false`, so existing calls behave as before.

<!-- TODO Mikhail Pochatkin (GG-50908): this guide has no data center replication section yet. GG-50908 (version negotiation in the DCR handshake) is merged to master only (ggprivate 5b9dbb00f, #2376), not to 8.9, and has no fix version. Please answer: (1) Does the upgrade order of two DCR-linked clusters matter? The source says no (the batch format is negotiated per connection, and an 8.10 sender re-encodes batches for an 8.9 receiver), but an 8.9 and an 8.10 cluster were never run together. (2) After a rollback of the sender cluster, can an 8.9 node read batches that the sender store kept in the V2 format? (3) Which DCR configuration, metric, and behavior changes must customers know? Please add them as a section here. -->
