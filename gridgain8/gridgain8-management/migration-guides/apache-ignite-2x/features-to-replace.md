---
description: >-
  Apache Ignite 2 features that work differently or have no equivalent in
  GridGain 8, with what to do and how to verify each replacement.
---

# Features to Replace

This page is reference material for the [Migration Procedure](migration-procedure.md) and the planning overview in [What to Know Before Migrating](before-you-migrate.md).

Each feature below works differently in GridGain 8 or has no direct equivalent. Every entry answers three questions: does it apply to you, what to do, and how to verify the result. Some of these changes require code.

**CDC (Change Data Capture)**: Applies if you run CDC: `ignite-cdc.sh`, a `CdcConsumer`, or the built-in streamers. CDC and its tooling do not exist in GridGain; the replacement depends on your consumer: Ignite-to-Ignite replication moves to [Data Center Replication](../../data-center-replication/introduction.md) (DCR); Ignite-to-Kafka moves to the GridGain Kafka Connect source connector; Kafka-to-Ignite moves to the Kafka Connect sink connector; a custom `CdcConsumer` is reimplemented with continuous queries. _Verify:_ changes propagate end to end through the replacement under a realistic write load on staging.

**Snapshots**: Applies if you create snapshots with `Ignite.snapshot()` or `control.sh --snapshot`, manually or in automation. A compatibility layer runs Apache Ignite 2 snapshot calls against GridGain snapshots: replace `Ignite.snapshot()` with `IgniteSnapshots.of(ignite)` from `org.gridgain.grid.persistentstore.ai2compat` and leave the rest of your snapshot code unchanged, or keep calling `control.sh --snapshot`. The compatibility layer cannot restore snapshot files written by Apache Ignite, you will need to recreate them. The layer covers `create`, `cancel`, `restore`, and `status`. Cache dumps (`createDump()`) are unavailable. To use the native API and tooling instead, see the [GridGain enterprise snapshot system](../../snapshots/snapshots-and-recovery.md) (the [`snapshot-utility.sh`](../../snapshots/snapshots-management-tool.md) tool or the plugin `getSnapshot()` API). _Verify:_ take a snapshot on staging and restore from it.

**Calcite SQL engine**: Applies if you enabled Calcite: the `ignite-calcite` module, [`CalciteQueryEngineConfiguration`](https://ignite.apache.org/releases/ignite2/2.18.0/javadoc/org/apache/ignite/calcite/CalciteQueryEngineConfiguration.html), the `queryEngine=calcite` connection property, or `QUERY_ENGINE('calcite')` SQL hints. GridGain 8 uses the H2 query engine; remove all of the above. _Verify:_ re-run every query that Calcite previously executed and confirm results and acceptable performance on H2.

**Custom security plugins**: Applies if you use a custom `GridSecurityProcessor` or Ignite's built-in authentication for cluster security. Adopt [GridGain enterprise security](../../../security/authentication.md) (LDAP, Active Directory, JAAS, OIDC, certificate-based, plus role-based access control) instead. Note that the Ignite Sandbox (Java SecurityManager-based sandboxing) is not available in GridGain. Ignite's built-in authentication and its SQL `CREATE`/`ALTER`/`DROP USER` commands are retained; GridGain enterprise security is a separate system, configured through its own authenticator configuration. _Verify:_ on staging, clients authenticate through the new mechanism and authorization rules deny what they should. For the permission grants themselves — which admin permissions were removed or replaced in GridGain 8 — see [Security Authorization Changes](security-authorization.md).

**Service call interceptors**: Applies if you use `ServiceCallInterceptor` or the related session-context types. They are absent in GridGain. Use Java dynamic proxies or AOP around the service proxy. _Verify:_ the interception logic fires in your service tests.

**Metrics API**: Applies if your code calls `Ignite.metrics()`. It is absent. Use JMX or `ReadOnlyMetricRegistry`. _Verify:_ the dashboards and alerts that consumed these metrics receive them from the new source.

**Read Repair**: Applies if you call `IgniteCache.withReadRepair(...)`. It is absent. Use partition reconciliation (`control.sh --cache partition_reconciliation`), which is batch-oriented rather than on-read. _Verify:_ run it on staging and confirm it detects and repairs an inconsistency.

**Transaction-aware queries**: Applies if your code runs SQL inside transactions and expects to see that transaction's uncommitted changes. This is not available: use the cache API (`get`/`put`) inside transactions instead. _Verify:_ re-test the affected transactional flows.

**Cache Dump**: Applies if you use the `org.apache.ignite.dump` package or `control.sh --dump`. They are absent. Export with the `COPY` command (to Parquet), or extract via scan or continuous queries. _Verify:_ a test export contains the expected rows.

**Multi-disk storage**: Applies if you configured extra storage paths. They are not available. Consolidate onto a single storage path and use OS-level RAID or LVM if you need multiple physical disks. _Verify:_ staging runs on the consolidated layout with acceptable capacity and throughput.

**Disk page compression**: Applies if you set `CacheConfiguration.diskPageCompression` or `diskPageCompressionLevel`. GridGain does not support per-cache disk-page compression: those properties are removed, so a node configured with them fails to start. GridGain compresses cache data with a different model — *entry* compression, which compresses each cache entry's value, rather than *disk-page* compression, which compresses storage pages. Because the models differ there is no drop-in alias; you choose and configure entry compression deliberately. Entry compression is a GridGain Enterprise Edition and Ultimate Edition feature and is not available in the Community Edition. WAL page compression (`DataStorageConfiguration.walPageCompression`) is a separate feature, still supported and unchanged.

Configure entry compression through [`CacheConfiguration.setEntryCompressionConfiguration(...)`](https://www.gridgain.com/sdk/gridgain8/latest/javadoc/org/apache/ignite/configuration/CacheConfiguration.html#setEntryCompressionConfiguration-org.apache.ignite.configuration.EntryCompressionConfiguration-) with one of the enterprise implementations (package `org.gridgain.grid.cache.compress`):

| Apache Ignite 2.x | GridGain 8 replacement |
|---|---|
| `CacheConfiguration.diskPageCompression`<br>`CacheConfiguration.diskPageCompressionLevel`<br>(per-cache disk-page compression) | `CacheConfiguration.setEntryCompressionConfiguration(...)` with `GzipCompressionConfiguration` or `ZstdDictionaryCompressionConfiguration`<br>(per-entry compression; Enterprise Edition / Ultimate Edition only) |

_Verify:_ disk usage on staging stays within budget with entry compression.

**Performance Statistics**: Applies if you use `--performance-statistics` or `PerformanceStatisticsMBean`. They are absent. Use JMX metrics or an external APM. _Verify:_ the profiling data you rely on is available from the replacement.

**Thin-client lifecycle callbacks**: Applies if you register a [`ClientLifecycleEventListener`](https://ignite.apache.org/releases/ignite2/2.18.0/javadoc/org/apache/ignite/client/events/ClientLifecycleEventListener.html). It has no direct equivalent; track connection state through the thin client's own connection handling instead. _Verify:_ your client's reconnect handling passes its tests.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
