---
description: >-
  GridGain 8.8.1 introduces managed rolling upgrade, incremental data center replication,
  native persistence defragmentation, transparent data encryption key rotation, data
  compression, and SQL tracing.
hidden: true
---

# GridGain 8.8.1 Release Notes

## What's New in This Release

### Introduction

GridGain 8.8 provides access to a variety of new features and improvements.

Data pages' defragmentation can help users reduce ownership costs by decreasing the sizes of persistence datafiles and releasing disk capacity.

Users can also enable dictionary data compression to lower memory requirements up to 60% in real-life cases and even accelerate some designs where GridGain has active disk communication.

The release is also changing rolling upgrade control by introducing an additional mode to protect a running cluster from cases that can introduce stability risks.

Significant improvement has been delivered for disaster recovery functionality. Now data can be synchronized between data centers incrementally. The new approach can significantly decrease the required memory resources for the DR Important change has been prepared for the transparent data encryption feature. With a new logic, the user can change encryption keys on the fly, and the functionality can now be used for production use.

The new scopes for the tracing are now added. Now users can trace SQL and atomic put & get operations in addition to already supported transactions and discovery messages.

Also, the release will deliver a set of different fixes, security updates, and stability improvements. External modules are now removed from the binary packages. They can be installed on the top of GridGain to make a package lighter and decrease the number of dependencies.

### New Features

#### Managed Rolling Upgrade

The new [Distributed rolling upgrade](https://www.gridgain.com/docs/latest/installation-guide/rolling-upgrades) allows controlling the process of an upgrade in a predictable and careful way. It is based on the three following constraints:

- The cluster does not allow to join nodes of different versions until upgrade mode is enabled.
- When upgrade mode is enabled, you can connect another node with only one different version larger than the current one.
- New features will not be activated until the upgrade mode is turned off manually.

{% code title="Activating the Rolling Upgrade mode." %}
```shell
./control.sh --rolling-upgrade start --yes

Rolling upgrade mode successfully enabled.
```
{% endcode %}

{% code title="Checking the status of the Rolling Upgrade." %}
```shell
./control.sh --rolling-upgrade status

Rolling upgrade is enabled
Initial version: 8.8.0#20200714-sha1:35c405b6
Target version: N/A
List of alive nodes in the cluster that are not updated yet: 54a088fb
List of alive nodes in the cluster that are updated:
```
{% endcode %}

{% code title="Stopping the Rolling Upgrade." %}
```shell
./control.sh --rolling-upgrade finish

Rolling upgrade mode successfully disabled.
```
{% endcode %}

#### Incremental State Transfer

We have rethought data flow in DR and added the [Incremental Data Center Replication](https://www.gridgain.com/docs/latest/administrators-guide/data-center-replication/managing-and-monitoring) mode with a safer approach to Data Center Replication. This new model features the following improvements:

- Higher stability
- Fewer memory requirements
- Simplified configuration

**Main advantages:**

- It is not necessary to configure DrSenderStore on the sender node anymore. The sender uses a non-persistent state transfer buffer instead to smooth network load spikes; it is only responsible for routing data to remote Data Centers. Data replication does not rely on a sender store being entirely tolerant of sender-node failure.
- You do not have to worry about backup queue size, which is very hard to configure. The backup queues are now removed to prevent potential data loss in case of primary-node failure.
- DR Incremental State transfer ensures better stability. DrSenderStore (state transfer buffer) overflow and a sender-node failure stop data replication. Therefore, you don’t need to start full state transfer after data replication stops due to any reason because all grid nodes track DR progress automatically.
- It features a fully asynchronous background process and introduces no additional latency to cache operations; its cost does not exceed an additional SQL index.
- DR Incremental State transfer has the "Incremental state transfer over snapshot" feature that enables transferring a "delta" only to remote DC, which may help to save time and network resources in some cases.

**Limitations:**

- **IMPORTANT:** Rolling upgrade is NOT seamless. The new mode is not compatible with the previous one. DR should be stopped for all caches before the rolling restart procedure.
- **IMPORTANT:** Only single state transfer per-cache at a time allowed.
- **IMPORTANT:** Remove operation is not replicated (will be fixed in the next versions).
- Replication to multiple remote data centers is possible. However, DR may get stuck when one of the DCs becomes unavailable until the failed DC connection will be recovered.
- Full state transfer and background replication process use the same buffer on the sender, and recent updates have no priority over full state transfer updates.

**How to use:**

Set system property `GG_INCREMENTAL_STATE_TRANSFER=true` to start with incremental DR mode. No additional configuration changes needed, unsupported configuration options will be just ignored.

Use `DrSenderConfiguration.setFullStateTransferBufferSize(long bytes)` to limit DR buffer on sender-node.

**"Incremental state transfer over snapshot" scenario:**

You need to perform the following next steps to get remote DC in-sync using snapshot:

1. Take a snapshot in source DC.
2. Copy it to target DC.
3. Restore the snapshot on target DC.
4. Start incrementalStateTransfer providing snapshot id.

#### Support for Spring 5.2.0 and Spring Data 2.2.0

You can now use Spring 5.2.0 and Spring Data 2.2.0 with GridGain. This integration comes from the `ignite-spring-data_2.2` module. To use it, add a dependency to your pom.xml:

```xml
<dependency>
    <groupId>org.gridgain</groupId>
    <artifactId>ignite-spring-data_2.2</artifactId>
    <version>8.8.0.b1</version>
</dependency>
```

#### Native Persistence Defragmentation

The persistent store enables users to store their caches' data durably on disk, still benefiting from the in-memory nature of Apache Ignite. Data of caches is stored in files created for every primary or backup partition assigned to that node and in an additional file for all user indexes. Files in the filesystem are allocated lazily (only if some data is stored in a particular partition) and grow automatically when more data is added to the cache. The files cannot shrink even if all data is removed. The system only marks such files for further reuse. GridGain can only create or reuse pages for user data but never clear them from files.

Therefore, the GridGain persistent data can only grow and never shrinks. It doesn't cause any problems as once created page can be reused multiple times in most use cases. However, in certain cases, it is possible that the cache contains very little data but occupies large chunks of disk space because a significant volume of data was removed from the cache.

Defragmentation enables a user to shrink data files and claim back disk space (see [Persistence Defragmentation](https://gridgain.com/docs/latest/administrators-guide/data-center-replication/defragmentation)).

The following commands are used to manage defragmentation:

```shell
control.sh --defragmentation schedule --nodes <nodes' consistent IDs>
control.sh --defragmentation schedule --nodes <nodes' consistent IDs> --caches <caches' names>
```

Schedules defragmentation on the set of nodes with optional set of cache names. After the defragmentation is scheduled on a node, it should be restarted to enter Maintenance Mode and start defragmenting necessary caches.

```shell
control.sh --defragmentation cancel
```

Cancels ongoing defragmentation process. As nodes executing defragmentation are isolated from the rest of the cluster, particular host and port of the node should be specified.

**Maintenance Mode**

In special situations, such as Persistent Store files corruption or Defragmentation, the node should not join the rest of the cluster but stay isolated, allowing the user to step in and do necessary actions.

Node enters Maintenance Mode on a restart if it finds a maintenance task. This task is created automatically if Store files corrupt or explicitly by the user request if Defragmentation is scheduled. To schedule defragmentation most simply, use a command similar to the following:

```shell
control.sh --defragmentation schedule --nodes <nodes' consistent IDs>
```

When the maintenance task is completed, the node has to be restarted again to exit Maintenance Mode and return to normal operations.

#### Transparent Data Encryption

Transparent data encryption automatically and silently protects data at rest (persistence) (see [Transparent Data Encryption](https://www.gridgain.com/docs/latest/administrators-guide/security/tde)).

If cache/table encryption is configured, GridGain generates a key (a cache encryption key) and uses it to encrypt/decrypt the cache's data. The cache encryption key is held in the system cache and cannot be accessed by users. When the key needs to be sent to other nodes or saved to disk (when the node goes down), it is encrypted using the user-provided key — the master key. In the current release, support of master key and cache keys rotation is added.

To control the master key rotation process, use some of the available interfaces, for example:

{% code title="Starting master key rotation" %}
```java
String masterKeyName = "master-key-name-example";
ignite.encryption().changeMasterKey(masterKeyName);

```
{% endcode %}

{% code title="Getting current master key name." %}
```java
String masterKeyName = ignite.encryption().getMasterKeyName();
```
{% endcode %}

**Note**: Starting cache and joining node during the key changing process is prohibited and will be rejected. If a node is unavailable during the master key rotation process, it cannot join the cluster with an old master key. The node should re-encrypt group keys during recovery on startup.

The process of cache encryption key rotation consists of the following steps:

1. Rotate cache group key - add a new encryption key on each node and set it for writing.
2. Schedule background re-encryption for archived data and clean up the old key when it completes.

You can manage the process of cache key rotation (and cache re-encryption) through the command line by executing the following commands:

To start a cache group encryption key change process from java API, use the following method:

```java
ignite.encryption().changeCacheGroupKey(Collection<String> cacheOrGroupNames)
```

#### Data Compression

Added the support of dictionary-based data entry compression using [Zstandard library](https://github.com/facebook/zstd). The Entry compression allows saving RAM and disk space by storing compressed data in cache entries, at the cost of spending CPU time on compression and decompression. Enabling entry compression leads to Off-Heap utilization and checkpoint directory size reduction; it also slightly shortens WAL. If native persistence is used and the load pattern is I/O bound, it is possible to save space while improving the performance. For details, see [Entry Compression](https://www.gridgain.com/docs/latest/developers-guide/configuring-caches/entry-compression).

{% code title="Enabling Data Compression" %}
```java
ZstdDictionaryCompressionConfiguration compressionCfg = new ZstdDictionaryCompressionConfiguration();
// Default values for all properties listed below:
compressionCfg.setCompressKeys(false);
compressionCfg.setRequireDictionary(true);
compressionCfg.setDictionarySize(1024);
compressionCfg.setSamplesBufferSize(4 * 1024 * 1024);
compressionCfg.setCompressionLevel(2);

CacheConfiguration cacheCfg = new CacheConfiguration("cache-name");
cacheCfg.setEntryCompressionConfiguration(compressionCfg);
```
{% endcode %}

#### SQL Tracing

A number of APIs in Ignite are instrumented for tracing with [OpenCensus](https://opencensus.io/tracing/). You can collect distributed traces of various tasks executed in your cluster and use this information to diagnose latency problems.

We suggest you get familiar with [enabling tracing](https://www.gridgain.com/docs/control-center/latest/connect-gridgain-cluster#enabling-tracing) in the GridGain documentation before reading this chapter.

The following Ignite APIs are instrumented for tracing:

- Discovery
- Communication
- Exchange
- Transactions

To view traces, you must export them into an external system. You can use one of the OpenCensus exporters or write your own, but in any case, you will have to write code that registers an exporter in Ignite. For details, refer to [Tracing](https://www.gridgain.com/docs/latest/administrators-guide/monitoring-metrics/tracing).

#### Metrics Framework Updates and Improvements

A new object lists engine for exporting internal objects information as system views were added. The existing system views were updated to use a new lists engine. The system views export only local objects available on a node being queried. Several system views exporting information about Ignite internal runtime objects were added, for example:

- Topology details are available via `SYS.NODES`, `SYS.NODE_ATTRIBUTES`, and `SYS.BASELINE_NODES` system views
- Compute tasks details are available via `SYS.TASKS` and `SYS.JOBS` system views
- Query details are available via `SYS.SQL_QUERIES`, `SYS.SCAN_QUERIES`, `SYS.CONTINUOUS_QUERIES`, `SYS.SQL_QUERIES_HISTORY` system views
- Services details are available via `SYS.SERVICES` system view
- Running transactions details are available via `SYS.TRANSACTIONS` system view
- Various caches details are available via `SYS.CACHES`, `SYS.CACHE_GROUPS`, `SYS.PARTITION_STATES` system views
- The system views list and column details are available via `SYS.VIEWS` and `SYS.VIEW_COLUMNS` system views

Alongside with the lists monitoring engine, a number of improvements in the metrics framework were made, such as adding histograms for transaction commit/rollback and cache put/get/remove operation timings. See [Generic Metrics](https://www.gridgain.com/docs/latest/administrators-guide/monitoring-metrics/generic-metrics) for details.

### Changes in Behavior

#### Log4J 1.x Integration is Not Included in Binaries

Logging framework log4j of versions 1.x has been out of support for many years. Starting this version, the integration module for log4j 1.x - `ignite-log4j` is no longer included into the binary discributions (`.zip` archives) of all GridGain editions. Also, `ignite-log4j` is no longer auto-discovered by the nodes, i.e. it won't be used unless `IgniteLogger` is explicitly configured.

`ignite-log4j` is still available as a Maven artifact.

Users of `ignite-log4j` should use the module `ignite-log4j2` instead. If you have to continue using `ignite-log4j`, the module can be downloaded and installed manually. Please see the [Configuring Logging](https://www.gridgain.com/docs/latest/developers-guide/logging) page for more details.

#### `maxWalArchiveSize` is Now Enforced With Point-in-Time Recovery

Before this release, `maxWalArchiveSize` setting was ignored when Point-in-Time Recovery feature was enabled. It ensured that Point-in-Time Recovery will have the necessary data but could lead to disk overflow.

Starting with this release, `maxWalArchiveSize` is considered even if Point-in-Time Recovery is enabled. It means that Write-Ahead Log will be cleaned up when its size exceeds the specified limit. If the Write-Ahead Log is insufficient, the Point-in-Time Recovery feature may mean not be able to restore to certain time periods.

Make sure to take cluster snapshots and move them to a centralized location periodically to avoid local node storage and Write-Ahead Log size limits overflow,

#### Deactivating an In-Memory Cluster

Starting this version, `control.sh --deactivate` command requires an additional parameter `--force` to deactivate a fully in-memory cluster. Deactivating an in-memory cluster causes all data to disappear which is normally not the indented result. The new parameter is added in order for the user to be able to additionally acknowledge the operation.

#### Extension Modules Externalization

The following extension modules are no longer part of the GridGain release:

- Camel Streamer
- Flink Streamer
- Flume Sink
- JMS Streamer
- Kafka Streamer
- MQTT Streamer
- RocketMQ Streamer
- Storm Streamer
- ZeroMQ Streamer
- Twitter Streamer

These modules' sources are available in [Apache Ignite Extensions repository](https://github.com/apache/ignite-extensions). Binaries are available in Maven Repository. For example, the following snippet should be added to the `pom.xml` file in order to add the Kafka Streamer to a project:

```xml
<dependency>
    <groupId>org.apache.ignite</groupId>
    <artifactId>ignite-kafka</artifactId>
    <version>2.9.0</version>
</dependency>
```

Binaries must be available to a GridGain node at runtime. It could be achieved by copying the corresponding `jar`-files to the `libs` folder of the GridGain distribution directory.

#### System Views SQL Schema Changed from `IGNITE` to `SYS`

This release brings a number of changes to the metrics and monitoring framework. Alongside the new features, the SQL schema used by the system views which were already available changes.

The views which previously could be accessed via the `IGNITE` schema should now be accessed by using the `SYS` schema.

#### Deprecations

The following JVM Beans have been deprecated in version 8.8.0:

- `java.org.apache.ignite.mxbean.ThreadPoolMXBean`
- `java.org.apache.ignite.mxbean.DataStorageMetricsMXBean`
- `java.org.apache.ignite.mxbean.DataRegionMetricsMXBean`

#### Visor GUI deprecation

GridGain is announcing the deprecation of the VisorGUI monitoring tool for GridGain. GridGain currently offers two tools that provide monitoring and metrics for GridGain and Apache Ignite clusters; VisorGUI and GridGain Web Console. VisorGUI was the initial monitoring tool for monitoring of local GridGain/Ignite clusters.

Since its introduction, GridGain Web Console has steadily added features to support management of GridGain and Apache Ignite applications from metrics analysis and querying to rolling upgrades and snapshotting. Web Console has reached a point in its maturity where it is at feature parity with and exceeds the capabilities of VisorGUI in many respects.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-31846 | Platforms & Thin Clients | .NET: Fixed a NullPointerException when IIgnite.GetAffinity is called before IIgnite.GetCache |
| GG-31798 | Cluster Control Script | `control.sh --indexes_list` will now correctly print indexes added via `CREATE INDEX` statement |
| GG-31772 | Platforms & Thin Clients | Java Thin Client: Idle connections will not longer unexpectedly close |
| GG-31559 | Cluster Data Replication | Fixed an issue when a node occasionally wouldn't stop gracefully while Full State Transfer is active |
| GG-31545 | Cluster Storage Engine | Added control.(sh\|bat) command to clean and backup corrupted cache files. |
| GG-31513 | Cluster Control Script | `control.sh --diagnostic connectivity` now works properly if topology change happens during the command execution |
| GG-31179 | Common Lang | ignite-log4j module is no longer a part of the binary package. ignite-log4j is no longer enabled automatically when it is available on the classpath - ignite-log4j2 is enabled automatically instead |
| GG-31092 | Control Center Agent | Control Center Agent threads now have meaningful names |
| GG-29922 | Cluster Storage Engine | Fixed an error when metrics are collected for an empty data region |
| GG-29756 | Cluster Affinity and Baseline Topology | `control.sh --deactivate` now requires an additional option `--force` to deactivate an in-memory cluster |
| GG-29194 | Cluster SQL Engine | Added ability to create tables for existed caches |
| GG-28316 | Cluster SQL Engine | Added limited support for LEFT JOIN from REPLICATED tables to PARTITIONED. See "SQL Joins" documentation section for details |
| GG-18652 | Cluster SQL Engine | Improved SQL statistics and optimizer. Note that SQL execution plans may change due to this improvement |
| GG-31915 | Common Lang | Upgraded google-api-client from 1.30.10 to 1.31.1, opencensus from 0.22.0 to 0.28.2, grpc-context from 1.19.0 to 1.27.2 |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-14570 | Cluster Data Snapshots and Recovery | maxWalArchiveSize will be considered when Point-in-Time Recovery is enabled |
| GG-31355 | Cluster Data Snapshots and Recovery | Add consistency checker of nextSnapshotTag and lastSuccessfulSnapshotTag for snapshots. |
| GG-30538 | Cluster Data Snapshots and Recovery | Point-in-Time Recovery will now work correctly if multiple nodes use the same persistence folder |
| GG-30351 | Cluster Data Snapshots and Recovery | Added snapshot events for tracking snapshot create, check, copy and delete operations. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version. You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

- 8.5.3
- 8.5.5
- 8.5.6
- 8.5.7
- 8.5.8
- 8.5.8-p6
- 8.5.9
- 8.5.10
- 8.5.11
- 8.5.12
- 8.5.13
- 8.5.14
- 8.5.15
- 8.5.16
- 8.5.17
- 8.5.18
- 8.5.19
- 8.5.20
- 8.5.22
- 8.5.23
- 8.5.24
- 8.7.2
- 8.7.2-p12
- 8.7.2-p13
- 8.7.3
- 8.7.4
- 8.7.5
- 8.7.6
- 8.7.7
- 8.7.8
- 8.7.9
- 8.7.10
- 8.7.11
- 8.7.12
- 8.7.13
- 8.7.14
- 8.7.15
- 8.7.16
- 8.7.17
- 8.7.18
- 8.7.19
- 8.7.19-p1
- 8.7.20
- 8.7.21
- 8.7.22
- 8.7.23
- 8.7.24
- 8.7.25
- 8.7.26
- 8.7.27
- 8.7.28
- 8.7.29
- 8.7.30
- 8.7.31
- 8.7.32

### Known Limitations

#### Jetty Configuration Incompatibility in GridGain 8.7.21 and Later

If you are upgrading from version 8.7.20 or earlier, consider an incompatibility issue related to Jetty configuration introduced in GridGain 8.7.21.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration that enables SSL for REST
- Your Jetty configuration uses the `org.eclipse.jetty.util.ssl.SslContextFactory` class
- The keystore specified in the Jetty configuration contains both the CA certificate and the private certificate

In this case, after starting a new version, an exception is thrown with an error message similar to the following:

```text
java.lang.IllegalStateException: KeyStores with multiple certificates are not supported on the base class
org.eclipse.jetty.util.ssl.SslContextFactory. (Use org.eclipse.jetty.util.ssl.SslContextFactory$Server
or org.eclipse.jetty.util.ssl.SslContextFactory$Client instead)
```

To workaround this issue, alter the Jetty configuration to use `org.eclipse.jetty.util.ssl.SslContextFactory$Server` or `org.eclipse.jetty.util.ssl.SslContextFactory$Client`. See the configuration example at the [Client Certificate Authentication](https://www.gridgain.com/docs/latest/administrators-guide/security/authentication#client-certificate-authentication) page.

#### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and Later

In GridGain 8.7.26, the default value of the property `IgniteConfiguration.rebalanceThreadPoolSize` changed from `1` to `min(4, number of CPU / 4)`. It may cause a compatibility issue under the following conditions:

- When a Rolling Upgrade is performed
- The upgrade is performed from 8.5.7 version (or earlier) to 8.5.x or from 8.7.3 (or earlier) to 8.7.x
- The server nodes have at least 8 CPU cores
- The nodes configuration does not have the property `IgniteConfiguration.rebalanceThreadPoolSize`, so the default value is used

In this case, an exception is thrown with an error message similar to the following:

```text
сlass org.apache.ignite.IgniteException: Rebalance configuration mismatch (fix configuration or set -DIGNITE_SKIP_CONFIGURATION_CONSISTENCY_CHECK=true system property).
Different values of such parameter may lead to rebalance process instability and hanging.  [rmtNodeId=5fc58fb7-209d-489a-8034-0127a81abed6, locRebalanceThreadPoolSize = 4, rmtRebalanceThreadPoolSize = 1]
```

To workaround this issue, change the configuration of the server nodes to `rebalanceThreadPoolSize=1` so that it matches the previous default configuration. For example:

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="rebalanceThreadPoolSize" value="1"/>

    <!-- The rest of the configuration goes here -->
</bean>
```

#### Jetty Doesn't Accept Incorrect Configuration in GridGain 8.7.31 and Later

In GridGain 8.7.31 Jetty was upgraded to 9.4.33. Starting that version, Jetty has more strict validation of the provided configuration files. Before that version, an incorrectly spelled property in the configuration file had no effect. Starting this version, errors in the configuration will lead to an error on start.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration for REST
- The custom configuration has errors in it

You will need to fix the custom Jetty configuration before upgrading.

#### `ignite.sh` No Longer Enables Remote JMX by Default in GridGain 8.7.31 and Later

Starting from 8.7.31 version, GridGain no longer attempts to automatically enable the remote JMX. Default settings are known to cause issues if customized (for example, secure the connection). Also, in most cases, remote JMX is not required since many tools use local JMX connections (not using TCP).

Your setup may be affected if:

- You start GridGain nodes via `ignite.sh` script
- You connect to GridGain nodes' JMX interface remotely over TCP using the default configuration

To continue using remote JMX, you need to manually specify the required JMX settings. Please see the example below. Note that you don't need remote JMX if you use a local connection, such as connecting JConsole to a GridGain process on the same host.

```bash
export JVM_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=33333 \
    -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false"

bin/ignite.sh
```

### Rolling Upgrade from GridGain 8.7.9 and Earlier Fails if Data Center Replication is Enabled

Rolling upgrades from GridGain 8.7.9 and earlier to current GridGain version fails if [data center replication](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/data-center-replication/introduction) is enabled and under load.

To work around this issue, you can first upgrade to GridGain 8.7.21, or a later 8.7.x version, and then to current version.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
