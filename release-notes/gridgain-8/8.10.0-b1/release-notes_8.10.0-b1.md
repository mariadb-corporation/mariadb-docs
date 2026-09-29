---
description: >-
  GridGain 8.10.0-b1 is a major release that raises the Java baseline to Java 17,
  consolidates optional modules and integrations, updates the Spring, Hibernate,
  Lucene, and Cassandra integrations, and extends vector search, the thin clients,
  and Apache Ignite 2 compatibility.
hidden: true
---

# GridGain 8.10.0-b1 Release Notes

## Overview

GridGain 8.10 is a major release. It raises the Java baseline to Java 17, consolidates the optional modules and integrations that ship with the server packages, moves the Spring, Hibernate, Lucene, and Cassandra integrations to current library versions, and extends vector search, the thin clients, and Apache Ignite 2 compatibility.

Upgrading from GridGain 8.9.x requires action. Read [Breaking Changes](#breaking-changes), [Configuration and Default Value Changes](#configuration-and-default-value-changes), and [Security, Permission, and Licensing Changes](#security-permission-and-licensing-changes) before you upgrade a cluster or an embedding application.

Two changes stop working configurations that upgrade unchanged, so check them first: server-side SQL `COPY` against a file or an object store is now closed by default, and the license is now checked feature by feature at node start.

This release note covers the 8.10.0-b1 build. Further changes are planned for the 8.10.0 general availability release, and the ones that are already known are called out in the sections below.

## Breaking Changes

### Java 17 or Later Is Required

GridGain 8.10 requires Java 17 or later. GridGain 8.9.x supported Java 8 and later. The requirement is the same on the server and on the client: every artifact GridGain ships is compiled to Java 17 bytecode, and the Java thin client and the JDBC thin driver are part of `ignite-core` rather than separate downloads, so there is no lower-versioned client artifact to fall back on.

| Component | Minimum | How the requirement is enforced |
|---|---|---|
| Server node | Java 17 | `ignite.sh` and `ignite.bat` refuse to start on anything below 17. In 8.9.x the same check refused anything below 8. |
| Control script, and the other `bin` scripts | Java 17 | `control.sh` and `control.bat` apply the same check. |
| Thick client, or an application that embeds a node | Java 17 | Class file version. Loading `ignite-core` on an older JVM fails with `UnsupportedClassVersionError`. |
| Java thin client, JDBC thin driver | Java 17 | Class file version. Both ship inside `ignite-core`. |
| .NET client, thick mode | Java 17 | Checked at run time against the JVM that the client starts. A `JAVA_HOME` pointing at an older JDK now fails with `Unsupported Java version: <version>. GridGain requires Java 17 or later.` |
| .NET client, thin mode | No JVM | The thin client is fully managed and starts no JVM. The .NET package targets `netstandard2.0`, `net8.0`, and `net10.0`. |
| C++ client, ODBC driver | No JVM | Native, no Java requirement. |
| Control Center agent | Java 17 | Class file version. An agent embedded in an application raises that application's floor to Java 17. |
| A node on the Lucene 10 line | Java 21, or 22 | `ignite-lucene-10` is compiled for Java 21 and `ignite-lucene-10-java22` for Java 22. This applies to the server only. See [Lucene 8 Removed, and a Lucene 10 Line Added](#lucene-8-removed-and-a-lucene-10-line-added). |

Upgrade the JVM on every server node, every client application, and every application that embeds GridGain before you upgrade to 8.10.

The 8.10.0-b1 build is tested on JDK 21. At general availability, GridGain 8.10.0 supports Java 17, 21, and 25.

### Removed and Replaced Modules

The following modules are removed in 8.10.0-b1:

| Removed module | Replacement | Deprecated in |
|---|---|---|
| `ignite-hibernate-4.2`, `ignite-hibernate-5.1`, `ignite-hibernate-5.3`, `ignite-hibernate-core` | `ignite-hibernate-7.4` (Hibernate 7.4 second-level cache) | 8.9.35 |
| `ignite-spring-6` | `ignite-spring` and `ignite-spring-data_2.2`, both built against Spring 7 | Not deprecated in the 8.9.x line |
| `ignite-lucene-8` | `ignite-lucene-9`, which stays the default, or the separate Lucene 10 download | Not deprecated in the 8.9.x line |
| `ignite-aop`, and the Gridify API in `ignite-core` | The [compute API](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/distributed-computing/distributed-computing) | 8.9.37 |
| `ignite-cloud` (`TcpDiscoveryCloudIpFinder`) | Another [IP finder](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/clustering/discovery-in-the-cloud) | 8.9.37 |
| `ignite-ssh` | The Apache Ignite `ignite-ssh-ext` extension | Not deprecated in the 8.9.x line |
| `gridgain-diagnostic`, `gridgain-tools`, `gridgain-yardstick` (Enterprise and Ultimate) | None | Not deprecated in the 8.9.x line |

New in this release: `ignite-hibernate-7.4`; `ignite-lucene-10`, `ignite-lucene-10-java22`, and `lucene-9-10-common`; and, on the Enterprise and Ultimate side, `gridgain-vector-query-common` and `gridgain-vector-query-lucene-10`.

`gridgain-pds-snapshot-utility` and `gridgain-cache-checksum-utility` are unaffected and still ship with the Enterprise and Ultimate packages.

Further module removals and relocations are planned for 8.10.0 GA. See Planned for the 8.10.0 GA Release.

### Hibernate 7.4 Only

The Hibernate second-level cache implementation now targets Hibernate 7.4. Applications on Hibernate 4.2, 5.1, or 5.3 must move to Hibernate 7.4 or stay on GridGain 8.9.x.

### Spring 7 Only

GridGain 8.10 builds against Spring Framework 7.0.8 and Spring Data 4.1. The `ignite-spring` and `ignite-spring-data_2.2` modules are compiled to Java 17 bytecode and target Spring 7. Spring 5 and Spring 6 are no longer supported.

An application that embeds GridGain through Spring must be on Spring 7. Otherwise, stay on GridGain 8.9.x, which keeps the Spring 5 and Spring 6 modules.

### Control Center Agent Requires Spring 7 and Jakarta WebSocket

The Control Center agent is built against Spring 7 and Jakarta WebSocket (Tyrus 2), and the emulator module is removed.

An agent embedded in a Spring 5 or Spring 6 application does not start. Upgrade the host application to Spring 7, or keep using the 8.9.x agent.

### Cassandra Store Uses the DataStax Driver 4

The Cassandra store moves from DataStax Java driver 3.2 to 4.17 (`com.datastax.oss.driver.*`), and from `cassandra-all` 3.11 to 5.0.8, which is required for Java 17. Native protocol versions 1 and 2 are dropped by the driver, so Cassandra 2.1 or later is required, and `setProtocolVersion(1)` or `setProtocolVersion(2)` now fails with `Incorrect protocol version`. Cassandra 3 clusters must be upgraded 3 -> 4 -> 5.

The `DataSource` configuration API changed:

- `setLocalDataCenter()` is now required whenever you specify explicit contact points and do not set a custom load balancing policy. A node that leaves it unset fails with `Cassandra local datacenter is not specified for the data source`.
- Policies are configured by class rather than by instance: `setLoadBalancingPolicyClass()`, `setReconnectionPolicyClass()`, `setRetryPolicyClass()`, `setAddressTranslatorClass()`, and `setSpeculativeExecutionPolicyClass()` replace the former `setLoadBalancingPolicy()`, `setReconnectionPolicy()`, `setRetryPolicy()`, `setAddressTranslator()`, and `setSpeculativeExecutionPolicy()`.
- `setPoolingOptions()`, `setSocketOptions()`, and `setNettyOptions()` are removed. Use `setConfigFile()` and a driver configuration file instead.
- `setSslOptions()` is replaced by `setSslEngineFactory()`.
- `setCollectMetrix()` and `setJmxReporting()` are removed.
- `user` and `password` are now mutually exclusive with `credentials`. Setting both fails the data source with `Both 'user'/'password' and 'credentials' are set for the data source`.

Update the `DataSource` bean definitions in your Spring XML configuration accordingly.

Previously serialized `DataSource` instances - those held by dynamically created caches - cannot be read by 8.10. Deserialization fails with `Unsupported DataSource serialization format version`. Drop and recreate those caches.

Large transactions may now hit the Cassandra `batch_size_fail_threshold` setting.

Only the embedded test server is unsupported on Windows. The runtime client is unaffected.

{% hint style="danger" %}
The `ignite-cassandra` module itself is scheduled for removal in 8.10.0 GA. See Planned for the 8.10.0 GA Release.
{% endhint %}

### Lucene 8 Removed, and a Lucene 10 Line Added

The `ignite-lucene-8` module is removed. If you still run it - the Java 8 workaround documented for GridGain 8.9.18 and later put it in `libs` - move to the Lucene 9 line before you upgrade.

The main 8.10 package still ships the Lucene 9 line, with `ignite-lucene-9` active in `libs`, and that remains the default for vector search and text search. Lucene 10.4 is delivered as its own download instead, because it requires Java 21:

- `ignite-lucene-10` - JDK 21 or later.
- `ignite-lucene-10-java22` - JDK 22 or later. Adds the no-copy `MemorySegment` vector scorer, which is opt-in even on a supported JDK.

A node runs exactly one Lucene line. The two carry the same class names, so they cannot share a classpath. To switch a node to Lucene 10: stop the node, remove `libs/ignite-lucene-9`, copy exactly one of the Lucene 10 module folders into `libs`, and - for vector search - replace `libs/gridgain-vector-query` with `optional/gridgain-vector-query-lucene-10` from the same download. Then start the node.

Use the same line on every node. A cluster running both answers one vector query with different recall depending on which node serves it.

Switching lines does not migrate or invalidate anything on disk: a GridGain Lucene index is held in memory and rebuilt from cache data.

### Gridify API Removed

The Gridify API is removed from `ignite-core`, together with the `ignite-aop` module. This covers the `org.apache.ignite.compute.gridify` package, including the `@Gridify`, `@GridifySetToSet`, and `@GridifySetToValue` annotations and their AOP aspects.

Replace Gridify usage with the [compute API](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/distributed-computing/distributed-computing). The API was deprecated in 8.9.37.

### SSH Support Moves to an Apache Ignite Extension

The `ignite-ssh` module is removed. `IgniteCluster.startNodes()` remains in the API, but the SSH implementation behind it now comes from the Apache Ignite `ignite-ssh-ext` extension.

If you use `startNodes()`, add `ignite-ssh-ext` to the node classpath. GridGain still resolves the SSH implementation by the class name `org.apache.ignite.internal.util.nodestart.IgniteSshHelperImpl`, and a node without it on the classpath still reports the missing component as `ignite-ssh`.

### Cloud IP Finder Removed

The `ignite-cloud` module, including `TcpDiscoveryCloudIpFinder`, is removed. It was deprecated in 8.9.37.

Use the JDBC, static, or Kubernetes [IP finders](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/clustering/discovery-in-the-cloud) instead.

{% hint style="info" %}
The Kubernetes and AWS IP finders are themselves scheduled to leave the server packages in 8.10.0 GA. See Planned for the 8.10.0 GA Release.
{% endhint %}

### Evaluation License Distributions Are No Longer Built

The `eval/` license files are removed, and so are the three evaluation-license assembly descriptors that produced the Enterprise, Ultimate, and z/OS `-evallic` archives. Those archives are no longer built.

### No Community Edition Build

GridGain 8.10 has no Community Edition build.

## Configuration and Default Value Changes

### SFTP Snapshot Transport Verifies the Host Key by Default

The `strictHostKeyChecking` property of `SftpConfiguration` now defaults to `true`. In 8.9.x it defaulted to `false`.

Before the first snapshot transfer to an SFTP destination, either populate the known hosts file that `knownHostsPath` points at, or set `strictHostKeyChecking` to `false` explicitly. Otherwise, transfers fail.

For more information, see [Configuring SFTP Location](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/snapshots/network-backups#configuring-sftp-location).

### Vector Search Limits

Vector search now enforces limits that reject queries instead of accepting them:

- The maximum number of vector dimensions defaults to 4096. Raise the `GRIDGAIN_VECTOR_MAX_DIMENSIONS` property if you index wider vectors. It applies to indexes created after it is set.
- A single vector query may ask for at most 10,000 neighbors, set by `GRIDGAIN_VECTOR_MAX_K`. A query above the limit is rejected.

For more information, see [Vector Search](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/vector).

### Thin Client DNS Resolution

The Java thin client now resolves its configured addresses through `DnsClientAddressFinder` by default. When an address resolves to several IP addresses, the client uses all of them instead of a single address. This affects host names backed by multiple A records or round-robin DNS.

The client also re-resolves its addresses in the background every 30 seconds, and reinitializes its channels when the result changes. Use the new `ClientConfiguration.setBackgroundReResolveAddressesInterval()` property to change the interval.

### Java Thin Client Transactions Are Partition-Aware

Java thin client transactions are partition-aware, and a transaction now starts lazily: `txStart()` no longer sends a `TX_START` message, which is deferred until the first cache operation inside the transaction so that the transaction can be mapped to the affinity node. Applications are not expected to notice, but a transaction that performs no cache operation now never reaches the server, and an error that used to surface at `txStart()` surfaces at the first operation instead.

### Clearer Startup Errors and Warnings for Stale Properties

An unknown property in the Spring XML configuration has always failed node startup. GridGain 8.10 replaces the opaque Spring message with `Configuration property <Bean>.<property> does not exist`, which names the bean and the property - typically an Apache Ignite-only property left behind by a migration.

Separately, GridGain now keeps a registry of Apache Ignite `IGNITE_*` system properties that have no effect in GridGain, and logs a warning for each one that is set at node start, pointing at the migration guide.

Clean up any leftover Apache Ignite properties in your configuration before upgrading.

## Security, Permission, and Licensing Changes

### Server-Side SQL COPY Is Now Disabled by Default

The file and object-store side of server-side SQL `COPY` is secure by default in GridGain 8.10, and it is rejected out of the box. To use it after the upgrade, an operator must do all three of the following:

1. Enable the feature. Set `fileAccessEnabled` to `true` on the new `ImportExportConfiguration` block of the per-node GridGain plugin configuration. It defaults to `false`, and an absent `GridGainConfiguration` or an absent block is treated as fully closed.
2. Populate the allow-lists. Every allow-list on that block starts empty, and an empty list forbids the corresponding access: `importRoots` for local directories, `allowedS3Buckets` and `allowedS3Endpoints` for S3, and `allowedCatalogUris` for Iceberg catalogs.
3. Grant the new `COPY_FROM_FILE` and `COPY_TO_FILE` [security permissions](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authorization-permissions) to every role that runs server-side `COPY`.

`ImportExportConfiguration` is node-local. It is never distributed over discovery, so a `COPY` can succeed or fail depending on which node the client connected to. Configure it identically on every node.

Point `importRoots` at dedicated directories, never at the node work directory: `COPY_TO_FILE` overwrites files inside a root.

{% hint style="warning" %}
This affects every existing `COPY FROM` and `COPY TO` statement that reads or writes a file or an object store. Those statements stop working on 8.10 until the configuration above is in place. Client-side `COPY` is unaffected.
{% endhint %}

For more information about the command, see [Operational Commands](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/operational-commands).

### Stricter Header Verification for Visor Data Transfer Objects

The header check that `VisorDataTransferObject` performs when it deserializes a payload is corrected. The previous check masked the header with the magic number itself, so a header that merely shared bits with the magic number passed. GridGain 8.10 masks the version byte off and compares the full magic number.

No action is required. The serialized form is unchanged, so a mixed 8.9 and 8.10 cluster and an older control script both keep working; what changes is that a malformed or foreign payload is now rejected where it could previously slip through.

### Per-Feature License Checks

GridGain 8.10 checks the license per feature rather than per edition, and it makes those checks at node start. A node whose license does not enable a feature it is configured to use now fails to start with an explicit message.

The following are checked at node start, and each one is satisfied either by its own feature entry in the license or by the `ultimate` feature:

| Configuration that triggers the check | License feature required | Startup error |
|---|---|---|
| A snapshot configuration without an SFTP location | `local_snapshots` | `Local snapshots feature is not allowed by the licence.` |
| A snapshot configuration with an SFTP location | `remote_snapshots` | `Remote snapshots feature is not allowed by the licence.` |
| `SnapshotConfiguration.pointInTimeRecoveryEnabled` | `point_in_time_recovery` | `Point-in-time recovery feature is not allowed by the licence.` |
| `GridGainConfiguration.rollingUpdatesEnabled` | `rolling_upgrades`, or any Enterprise-typed license | `Rolling Upgrade feature is not allowed by the licence.` |
| A non-zero data center ID | `data_center_replication` | `Data center replication feature is not allowed by the licence.` |
| An authenticator, or `IgniteConfiguration.authenticationEnabled` | `security` | `Security feature is not allowed by the licence.` |
| An affinity backup filter on `RendezvousAffinityFunction` | `rack_awareness` | `Rack awareness is not allowed by the licence [cacheName=...]` |
| `CacheConfiguration.encryptionEnabled` | `encryption`, or any Enterprise-typed license | `Encryption is not allowed by the licence [cacheName=...]` |
| A cache with a vector index | `vector-search`, or any Enterprise-typed license | `Vector search is not allowed by the licence [cacheName=...]` |

An Ultimate license carries the `ultimate` feature and satisfies every check, so Ultimate Edition users are unaffected. Data center replication, security, and rack awareness are the checks an Enterprise license does not satisfy by its type alone.

{% hint style="warning" %}
Before you upgrade, confirm that your license enables every feature in the list above that your cluster is configured to use. Contact GridGain support for a reissued license if it does not.
{% endhint %}

The MariaDB license key format is also supported in this release.

For more information, see [GridGain Licensing](https://www.gridgain.com/docs/gridgain8/latest/installation-guide/licenses).

## Deprecation Notice

The following configuration is deprecated but still works. Migrate at your convenience.

| Deprecated | Replacement |
|---|---|
| `DataStorageConfiguration.setSystemRegionInitialSize()` and `setSystemRegionMaxSize()` | `SystemDataRegionConfiguration` |
| `ClientConfiguration.getTimeout()` and `setTimeout()` | `getHandshakeTimeout()` and `getRequestTimeout()`, `setHandshakeTimeout()` and `setRequestTimeout()` |
| `ClientConfiguration.isPartitionAwarenessEnabled()` and `setPartitionAwarenessEnabled()` | `isAffinityAwarenessEnabled()` and `setAffinityAwarenessEnabled()` |
| `ClientCacheConfiguration.getRebalanceBatchSize()`, `getRebalanceBatchesPrefetchCount()`, `getRebalanceThrottle()`, `getRebalanceTimeout()`, and their setters | The equivalent `IgniteConfiguration` properties |
| `ClientCacheConfiguration.getRebalanceDelay()` and `setRebalanceDelay()` | [Baseline topology](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/baseline-topology) |
| `ClientCacheConfiguration.getDefaultLockTimeout()` and `setDefaultLockTimeout()` | None - the property has no effect |

When `getTimeout()` is used with differing handshake and request timeouts, a warning is written to the log.

`IgniteConfiguration.getDefaultQueryTimeout()` and `setDefaultQueryTimeout()` are new in this release and ship deprecated. They are Apache Ignite source-compatibility aliases, added so that Apache Ignite code compiles unchanged; use `SqlConfiguration.getDefaultQueryTimeout()` and `SqlConfiguration.setDefaultQueryTimeout()` in new code.

## New Features

### Baseline Auto-Adjust Scale-Up and Scale-Down Timeouts

Baseline auto-adjust now takes separate timeouts for scale-up and scale-down events. The single combined timeout still works, and the split is exposed on every surface:

- `IgniteCluster.baselineAutoAdjustEnabled()`, `baselineAutoAdjustTimeout()`, and `baselineAutoAdjustStatus()` take an `AutoAdjustMode` argument.
- The control script adds the `scale_up_auto_adjust` and `scale_down_auto_adjust` subcommands of `--baseline`.
- `BaselineAutoAdjustMXBean` exposes per-direction enablement, timeouts, time-until-adjust, and task state.
- The .NET `ICluster` API takes the same `AutoAdjustMode`.

For more information, see [Baseline Topology](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/baseline-topology).

### Vector Search Improvements

- Similarity scores are returned with query results through `ScoredCacheEntry`.
- Vector queries take a single parameter object that carries the filter, the keys-only flag, and the oversample factor.
- HNSW build parameters can be set per index.
- Vectors can be stored as `int8`, with a configurable segment target, query thread count, and deleted-vector budget.
- Binary quantization is supported, node-wide through `GRIDGAIN_VECTOR_BINARY_QUANTIZATION` or per index. A per-index storage choice always wins over the node-wide property, and either only applies to indexes built after it is set.
- The thin client vector protocol moves to version 2.

For more information, see [Vector Search](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/vector).

### Java Thin Client

The Java thin client adds a data streamer, `ClientCache.sizeLong()`, `serviceProxy()` with a `ServiceCallContext`, lifecycle events, `withPartitionRecover()`, partition-aware `getAll()`, an asynchronous `ClientDataStreamer.flush()`, and asynchronous overloads for atomic longs, atomic sequences, sets, cluster operations, and services.

### .NET Client

The .NET client adds asynchronous API parity with the Java API, `IAsyncDisposable` support, `IAsyncEnumerable` for query cursors, continuous queries, and the data streamer, asynchronous service calls, `HandshakeTimeout` and `RequestTimeout` properties, and `IDataStreamerClient.AddAsync()`.

The NuGet package and the archive now ship `netstandard2.0`, `net8.0`, and `net10.0` targets, and the API carries nullable reference type annotations. The change is additive, but projects that enable nullable reference types may see new warnings.

### Apache Ignite 2 Compatibility

- Apache Ignite thin clients can connect to GridGain servers.
- The Apache Ignite 2 snapshot API is supported, including cancel, restore, and status operations, and the matching `control.sh --snapshot` commands.
- Apache Ignite 2 change data capture WAL records can be read.
- The REST API accepts a `keepBinary` query parameter.
- The JSON permission parser tolerates `SecurityPermission` names that exist only in Apache Ignite.

For more information, see [Artifacts and Modules](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/migration-guides/apache-ignite-2x/artifacts-and-modules).

### Core API

Service call interceptors, the `@ServiceContextResource` annotation, `BinaryObject.size()`, `SystemDataRegionConfiguration`, and a set of Apache Ignite source-compatibility alias methods are added.

### Control Script and REST

No REST command and no control script command was removed or renamed in this release. The control script adds the `--system-view` command, the Apache Ignite 2 compatible `--snapshot` commands, and the baseline auto-adjust scale-up and scale-down options.

For more information, see [Control Script](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/control-script) and [REST API](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/restapi).

### Metrics

No system view, metric, or metric registry was removed or renamed in this release. New metrics are added for node network unavailability, data region evictions, cache group inserted and removed bytes, cache metrics carried over from Apache Ignite, the TCP communication connection pool, the client connector, index operations, page read and page replace times, and transaction deadlocks.

The cache group I/O statistics system view gains two columns, `INSERTED_BYTES` and `REMOVED_BYTES`.

The `IGNITE_TCP_COMM_MSG_QUEUE_WARN_SIZE` and `IGNITE_BPLUS_TREE_DISABLE_METRICS` system properties are added.

### Data Center Replication

The replication handshake negotiates the batch format version and the protocol features, so a mixed-version estate keeps replicating across the upgrade.

Data center replication sender monitoring is extended: `DrSenderInMetrics` and `DrSenderOutCacheMetrics` carry additional counters, and the sender's debug logging is throttled.

### Migrating from GridGain 8.9.x

Work through this checklist before you upgrade:

1. Move every node, thick client, and embedding application to Java 17 or later.
2. If you embed GridGain through Spring, move the application to Spring 7. If you use the Control Center agent inside a Spring application, the same requirement applies.
3. If you use the Hibernate second-level cache, move to Hibernate 7.4 and switch to the `ignite-hibernate-7.4` module.
4. If you use the Cassandra store, rework the `DataSource` configuration for the DataStax driver 4, and drop and recreate any dynamically created cache that holds a serialized `DataSource`.
5. If you use vector search or text search, decide which Lucene line to run. Lucene 9 remains the default and needs no action; the separate Lucene 10 download requires Java 21 or later and a manual swap on every node.
6. Replace any use of the Gridify API with the compute API.
7. If you use `IgniteCluster.startNodes()`, add the `ignite-ssh-ext` extension to the classpath.
8. If you use `TcpDiscoveryCloudIpFinder`, switch to a supported IP finder.
9. If you run server-side `COPY FROM` or `COPY TO` against a file or an object store, configure the new `ImportExportConfiguration` block on every node - enable `fileAccessEnabled` and populate the allow-lists - and grant the new `COPY_FROM_FILE` and `COPY_TO_FILE` permissions. Those statements are rejected until you do.
10. Check that your license enables every feature your cluster is configured to use. Data center replication, security, and rack awareness are now checked at node start and are not satisfied by an Enterprise license type alone.
11. If you transfer snapshots over SFTP, configure the known hosts file or set `strictHostKeyChecking` to `false`.
12. Review any vector index wider than 4096 dimensions, and any query that asks for more than 10,000 neighbors.
13. If a thin client connects through a host name and you depend on it holding one address, review the new background DNS re-resolution, which runs every 30 seconds by default.
14. Remove unsupported Apache Ignite `IGNITE_*` system properties from the node configuration and the launch scripts. They are reported as warnings at node start.
15. If you script the copy of files from `libs/optional` or `integration/` into `libs/`, review those scripts against the module list for this release.
