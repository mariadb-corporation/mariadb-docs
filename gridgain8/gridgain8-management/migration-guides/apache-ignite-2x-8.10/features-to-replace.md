---
description: >-
  Apache Ignite 2 features that work differently or have no equivalent in
  GridGain 8, with what to do and how to verify each replacement.
---

# Features to Replace

This page is reference material for the [Migration Procedure](migration-procedure.md) and the planning overview in [What to Know Before Migrating](before-you-migrate.md).

Each feature below works differently in GridGain 8.10 or has no direct equivalent. Every entry answers three questions: does it apply to you, what to do, and how to verify the result. Some of these changes require code.

GridGain 8.10 supports the following Apache Ignite 2.18 APIs, so you only recompile: service call interceptors (`ServiceCallInterceptor`, `ServiceCallContext`) in Java, `Ignite.metrics()` and the `MetricRegistry` API, thin-client lifecycle listeners (`ClientLifecycleEventListener`), and the Apache Ignite 2 snapshot API through a compatibility layer (see Snapshots). Custom metric registries need the `CUSTOM_METRICS_MANAGE` permission. The .NET thick client has no service interceptors.

**CDC (Change Data Capture)**: Applies if you run CDC: `ignite-cdc.sh`, a `CdcConsumer`, or the built-in streamers. GridGain has no CDC and no CDC tooling, but it starts on persistence that Apache Ignite wrote with CDC enabled. Remove `cdcEnabled`, `cdcWalPath`, and `cdcWalDirectoryMaxSize` from the configuration, because the node does not start with them. The replacement depends on your consumer:

- Ignite-to-Ignite replication: [Data Center Replication](../../data-center-replication/introduction.md) (DCR).
- Ignite-to-Kafka: the GridGain Kafka Connect source connector.
- Kafka-to-Ignite: the Kafka Connect sink connector.
- A custom `CdcConsumer`: reimplement it with continuous queries.

_Verify:_ changes propagate end to end through the replacement under a realistic write load on staging.

**Snapshots**: Applies if you create snapshots with `Ignite.snapshot()` or `control.sh --snapshot`, manually or in automation. GridGain Ultimate Edition runs Apache Ignite 2 snapshot calls through a compatibility layer, so most snapshot code stays as it is:

- In code, replace `Ignite.snapshot()` with `IgniteSnapshots.of(ignite)` from `org.gridgain.grid.persistentstore.ai2compat`. `Ignite.snapshot()` no longer exists, but the rest of your snapshot code does not change.
- In scripts, keep calling `control.sh --snapshot`.
- The layer covers `create`, incremental snapshots, `cancel`, `restore` (with cache groups and increment index), and `status`. Snapshot names must be unique, and an incremental snapshot extends only the latest full one.
- Cache dumps (`createDump()`) are not supported and throw `UnsupportedOperationException`.
- The layer cannot restore snapshot files that Apache Ignite wrote. `control.sh --snapshot restore <ignite-snapshot-name>` fails with `No full snapshot named '...' exists`, even if you copy the files into the GridGain snapshot directory. Take a new snapshot on GridGain after the cutover.
- You can use a full snapshot from a single Apache Ignite node as a persistence directory. Copy its `db/` directory (`binary_meta`, `marshaller`, and `<consistentId>`) to the work directory of a GridGain node with the same `consistentId`, and start it as in the [Migration Procedure](migration-procedure.md). Multi-node snapshots are not covered here.

To use the native API and tooling instead, see the [GridGain enterprise snapshot system](../../snapshots/snapshots-and-recovery.md) (the [`snapshot-utility.sh`](../../snapshots/snapshots-management-tool.md) tool or the plugin `getSnapshot()` API). _Verify:_ take a snapshot on staging and restore from it.

**Calcite SQL engine**: Applies if you enabled Calcite: the `ignite-calcite` module, [`CalciteQueryEngineConfiguration`](https://ignite.apache.org/releases/ignite2/2.18.0/javadoc/org/apache/ignite/calcite/CalciteQueryEngineConfiguration.html), the `queryEngine=calcite` connection property, or `QUERY_ENGINE('calcite')` SQL hints. GridGain 8 uses the H2 query engine; remove all of the above. _Verify:_ re-run every query that Calcite previously executed and confirm results and acceptable performance on H2.

**Custom security plugins**: Applies if you use a custom `GridSecurityProcessor` or Ignite's built-in authentication for cluster security. Adopt [GridGain enterprise security](../../../security/authentication.md) (LDAP, Active Directory, JAAS, OIDC, certificate-based, plus role-based access control) instead. The Ignite Sandbox (Java SecurityManager-based sandboxing) is not available in GridGain. Ignite's built-in authentication and its SQL `CREATE`/`ALTER`/`DROP USER` commands are retained; GridGain enterprise security is a separate system, configured through its own authenticator configuration. _Verify:_ on staging, clients authenticate through the new mechanism and authorization rules deny what they should. For the permission grants themselves, meaning which admin permissions were removed or replaced in GridGain 8, see [Security Authorization Changes](security-authorization.md).

**Read Repair**: Applies if you call `IgniteCache.withReadRepair(...)`. It is absent. Use partition reconciliation (`control.sh --cache partition_reconciliation`), which is batch-oriented rather than on-read. _Verify:_ run it on staging and confirm it detects and repairs an inconsistency.

**Transaction-aware queries**: Applies if your code runs SQL inside transactions and expects to see that transaction's uncommitted changes. This is not available: use the cache API (`get`/`put`) inside transactions instead. _Verify:_ re-test the affected transactional flows.

**Index queries**: Applies if you run [index queries](../../../gridgain8-development/key-value-api/using-index-queries.md) (`IndexQuery`) against caches. The API is the same as in Apache Ignite, but two behaviors differ:

- A range criterion (`lt()`, `lte()`, `gt()`, `gte()`, `between()`) with a `null` bound throws `NullPointerException` in GridGain. Apache Ignite accepts it and returns rows whose value is `null`. Remove `null` bounds from your criteria.
- A criterion on a field that the index does not cover runs in GridGain and returns rows, but it is not guaranteed to be efficient. Apache Ignite rejects it with `Index doesn't match criteria`.

Make sure your criteria fields match table indexes and that your code can handle unsorted results. _Verify:_ re-run your index queries on staging and confirm both correct results and acceptable performance.

**Cache Dump**: Applies if you use the `org.apache.ignite.dump` package or `control.sh --dump`. They are absent. Export with the `COPY` command (to Parquet), or extract via scan or continuous queries. _Verify:_ a test export contains the expected rows.

**Multi-disk storage**: Applies if you configured extra storage paths. They are not available. Consolidate onto a single storage path and use OS-level RAID or LVM if you need multiple physical disks. _Verify:_ staging runs on the consolidated layout with acceptable capacity and throughput.

**Disk page compression**: Applies if you set `CacheConfiguration.diskPageCompression` or `diskPageCompressionLevel`. GridGain does not support per-cache disk-page compression: those properties are removed, so a node configured with them fails to start. GridGain compresses cache data differently: *entry* compression compresses each cache entry's value, while *disk-page* compression compresses storage pages. There is no drop-in alias, so you choose and configure entry compression yourself. Entry compression is a GridGain Enterprise Edition and Ultimate Edition feature. WAL page compression (`DataStorageConfiguration.walPageCompression`) is a separate feature, still supported and unchanged.

Configure entry compression through [`CacheConfiguration.setEntryCompressionConfiguration(...)`](https://www.gridgain.com/sdk/gridgain8/latest/javadoc/org/apache/ignite/configuration/CacheConfiguration.html#setEntryCompressionConfiguration-org.apache.ignite.configuration.EntryCompressionConfiguration-) with one of the enterprise implementations (package `org.gridgain.grid.cache.compress`):

| Apache Ignite 2.x | GridGain 8 replacement |
|---|---|
| `CacheConfiguration.diskPageCompression`<br>`CacheConfiguration.diskPageCompressionLevel`<br>(per-cache disk-page compression) | `CacheConfiguration.setEntryCompressionConfiguration(...)` with `GzipCompressionConfiguration` or `ZstdDictionaryCompressionConfiguration`<br>(per-entry compression; Enterprise Edition / Ultimate Edition only) |

_Verify:_ disk usage on staging stays within budget with entry compression.

**Performance Statistics**: Applies if you use `--performance-statistics` or `PerformanceStatisticsMBean`. They are absent. Use JMX metrics or an external APM. _Verify:_ the profiling data you rely on is available from the replacement.
