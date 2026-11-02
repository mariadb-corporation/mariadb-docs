---
description: >-
  Configuration changes when migrating from Apache Ignite 2.18 to GridGain 8.10:
  changed defaults, removed and unsupported properties, and binary field ordering.
---

# Configuration and Validation Changes

This page covers the configuration defaults that change, the properties GridGain 8 removes, its stricter validation, and the binary object field-ordering setting.

## Server Configuration Differences

### Changed Defaults

This section applies to every migration: review the table and decide each value deliberately, whether you restore the Ignite 2 behavior or keep the GridGain 8 default.

GridGain 8.10 changes a number of configuration defaults relative to Apache Ignite 2.18.

| Setting | Ignite 2 default | GridGain 8 default |
|---|---|---|
| `CacheConfiguration.readFromBackup` | `true` | `false` |
| `IgniteConfiguration.segmentationPolicy` | `USE_FAILURE_HANDLER` (enum member absent in GridGain 8) | `STOP` |
| `SqlConfiguration.sqlGlobalMemoryQuota` | unlimited (field absent) | `"60%"` of heap |
| `DataRegionConfiguration.metricsEnabled`<br>`DataStorageConfiguration.metricsEnabled` | `false` | `true` |
| `TcpDiscoverySpi` IP finder | `TcpDiscoveryMulticastIpFinder` | `TcpDiscoveryVmIpFinder(shared=true)` |
| `TcpCommunicationSpi.messageQueueLimit` | `0` (unlimited) | `4096` |
| `ClientConnectorConfiguration.socketSendBufferSize` / `socketReceiveBufferSize` | `0` (OS default) | `262144` (256 KB) |
| `IgniteDataStreamer.allowOverwrite()` | `false` | `true` (via `IGNITE_DATA_STREAMER_ALLOW_OVERWRITE`, defaulting to `true`) |
| Thin client partition/affinity awareness | `partitionAwarenessEnabled = true` | `affinityAwarenessEnabled = false` (the Ignite-named methods remain as deprecated aliases) |
| Thin client timeouts (`ClientConfiguration`) | `timeout = 0` (infinite) | `handshakeTimeout = 10000` ms, `requestTimeout = 60000` ms (`setTimeout` is deprecated) |
| `TransactionConfiguration.txTimeoutOnPartitionMapExchange` | `0` (no timeout) | `60000` (ms) |
| `SqlConfiguration.longQueryWarningTimeout` | `3000` (ms) | `1000` (ms) |
| `IgniteConfiguration.rebalanceBatchesPrefetchCount` | `3` | `2` |
| `IGNITE_CHECKPOINT_TRIGGER_ARCHIVE_SIZE_PERCENTAGE` (system property) | `0.25` | `0.75` |
| Baseline auto-adjust with persistence | single timeout | separate scale-up (5 minutes) and scale-down (never) timeouts |
| System worker blocked timeout | falls back to `failureDetectionTimeout` (10 s) | 120 s |
| `TcpDiscoverySpi` socket `SO_LINGER` | `0` | `5` |
| `IGNITE_QUIET` / `ignite.sh` log verbosity | quiet | verbose (`-q` makes it quiet) |
| Sensitive data in logs (`IGNITE_SENSITIVE_DATA_LOGGING`) | plain values (`IGNITE_TO_STRING_INCLUDE_SENSITIVE=true`) | `hash` |
| `SftpConfiguration.strictHostKeyChecking` (Ultimate Edition, SFTP snapshot storage; new in 8.10) | not applicable | `true`: requires a known-hosts file or an explicit `false` |

To preserve Ignite 2 behavior, set each changed default explicitly. This template restores the server-side defaults that differ between Ignite 2 and GridGain 8; the settings that live in cache or client code are listed separately below.

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <!-- GridGain default STOP; Ignite's USE_FAILURE_HANDLER is absent in GridGain,
         so choose a GridGain policy deliberately rather than restoring the Ignite value. -->
    <property name="segmentationPolicy" value="STOP"/>

    <!-- GridGain default: 2 -->
    <property name="rebalanceBatchesPrefetchCount" value="3"/>

    <property name="dataStorageConfiguration">
        <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
            <!-- GridGain default: true -->
            <property name="metricsEnabled" value="false"/>
            <property name="defaultDataRegionConfiguration">
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                    <property name="metricsEnabled" value="false"/>
                </bean>
            </property>
        </bean>
    </property>

    <!-- Restore Ignite's unlimited SQL memory (GridGain default: 60% of heap)
         and long-query warning timeout (GridGain default: 1000 ms). -->
    <property name="sqlConfiguration">
        <bean class="org.apache.ignite.configuration.SqlConfiguration">
            <property name="sqlGlobalMemoryQuota" value="0"/>
            <property name="longQueryWarningTimeout" value="3000"/>
        </bean>
    </property>

    <!-- GridGain aborts transactions during a partition map exchange after 60s; Ignite does not (0). -->
    <property name="transactionConfiguration">
        <bean class="org.apache.ignite.configuration.TransactionConfiguration">
            <property name="txTimeoutOnPartitionMapExchange" value="0"/>
        </bean>
    </property>

    <!-- GridGain default: 4096 -->
    <property name="communicationSpi">
        <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="messageQueueLimit" value="0"/>
        </bean>
    </property>

    <!-- GridGain default: 262144 (256 KB) buffers; 0 = OS default, as in Ignite. -->
    <property name="clientConnectorConfiguration">
        <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration">
            <property name="socketSendBufferSize" value="0"/>
            <property name="socketReceiveBufferSize" value="0"/>
        </bean>
    </property>
</bean>
```

Some Ignite 2 defaults are restored through system properties (JVM `-D` arguments or environment variables) rather than configuration:

```shell
# GridGain triggers a checkpoint at 75% of the WAL archive size; Ignite at 25%.
IGNITE_CHECKPOINT_TRIGGER_ARCHIVE_SIZE_PERCENTAGE=0.25

# GridGain enables data-streamer overwrite by default; Ignite does not.
# (Or call allowOverwrite(false) per streamer in client code.)
IGNITE_DATA_STREAMER_ALLOW_OVERWRITE=false
```

The remaining defaults are not server-side configuration and must be set where they apply:

- *readFromBackup (per cache).* Set `readFromBackup=true` on each `CacheConfiguration` or cache template. The GridGain 8 default is `false`.
- *Thin-client affinity awareness (client code).* Call `ClientConfiguration.setAffinityAwarenessEnabled(true)`. The GridGain 8 default is `false`.
- *Thin-client timeouts (client code).* Ignite 2 waits indefinitely by default. GridGain 8.10 gives up after 10 s on handshake and 60 s per request, so long-running thin-client operations (large scans, bulk loads) can start failing with timeouts. Set `setHandshakeTimeout` and `setRequestTimeout` explicitly (`0` is infinite).
- *Discovery (environment-specific).* Ignite 2 defaults to multicast discovery. If your cluster relied on it, configure a `TcpDiscoveryMulticastIpFinder` or supply the static address list; GridGain 8 defaults to `TcpDiscoveryVmIpFinder`.

Several of these defaults change behavior in ways that pass functional tests and surface only later: under load, on large data, or during a network event. The ones that most often cause problems:

**Affinity awareness (clients)**: Ignite 2 enables it (as partition awareness) and GridGain 8 disables it, so thin clients no longer route each request to the node that owns the key and every operation takes an extra network hop. This passes functional tests but shows up as a latency and throughput regression under load. Re-enable it unless you have a reason not to. Service awareness in the Java thin client (Ignite 2.16.0 and later, also in GridGain 8.10) works only when partition awareness is enabled. With the GridGain 8 default (disabled), the client sends service calls the standard way: to the node it is connected to, which forwards them to a node that runs the service.

**Discovery IP finder**: Ignite 2 defaults to multicast discovery; GridGain 8 defaults to the static `TcpDiscoveryVmIpFinder`, pre-seeded with `127.0.0.1:47500..47600` only. Nodes on the same host still find each other, but nodes on different hosts no longer do. A multi-host cluster that relied on multicast will not form until you supply the real node addresses or configure the multicast IP finder.

**`readFromBackup`**: Ignite 2 can serve a read from a local backup copy; GridGain 8 (default `false`) routes every read to the primary. Results are unaffected, but read load concentrates on primary nodes and latency can rise where you previously benefited from backup locality. Set it per cache to restore the Ignite 2 behavior.

**SQL memory quota** (`sqlGlobalMemoryQuota`): Ignite 2 runs SQL with no global memory quota; GridGain 8 caps it at 60% of heap. A query that ran in Ignite 2 can fail with a quota error the first time it processes a large result set, not during ordinary testing. Set it to `0` for unlimited, or tune it. See [SQL Changes](apis-and-clients.md#sql-changes).

**Data streamer overwrite** (`allowOverwrite`): Ignite 2's `IgniteDataStreamer` does not overwrite existing keys by default; GridGain 8 enables overwrite. A streaming job that assumed existing entries were left in place will now replace them. Set `allowOverwrite(false)` in client code if you relied on the Ignite 2 behavior.

**Transaction timeout on partition map exchange** (`txTimeoutOnPartitionMapExchange`): Ignite 2 does not time out transactions during a partition map exchange (PME) by default (`0`); GridGain 8 aborts them after 60 seconds. During a long PME, such as a node join or rebalance on a large cluster, transactions that Ignite 2 would have let run can fail in GridGain. Set it to `0` to restore the Ignite 2 behavior, or keep the timeout as a safeguard against PME stalls.

**Checkpoint trigger by WAL archive size** (`IGNITE_CHECKPOINT_TRIGGER_ARCHIVE_SIZE_PERCENTAGE`): Ignite 2 triggers a checkpoint when the WAL archive reaches 25% of its maximum size; GridGain 8 waits until 75%. GridGain 8 checkpoints less often, so WAL archives grow larger and crash recovery can take longer. Set the system property to `0.25` to match Ignite.

**Segmentation policy**: Ignite 2's default `USE_FAILURE_HANDLER` delegates the response to your configured failure handler; that value does not exist in GridGain 8, whose default is `STOP`: a segmented node stops itself. If you relied on a custom failure-handler response to network segmentation, choose a GridGain 8 segmentation policy.

**Logging and system worker timeouts**: GridGain 8 logs more by default (`IGNITE_QUIET` is `false`), hashes sensitive values in logs, and waits 120 s instead of 10 s before declaring a system worker blocked. Log volume and log-parsing tools are affected. The worker timeout alone does not make failure detection faster or slower.

#### Restoring Ignite 2 Discovery

The discovery IP finder is the one changed default with no server-side template entry, because the value you need is environment-specific. Pick one of the following and set it explicitly on `TcpDiscoverySpi`.

*Recommended: static address list.* This option is required in the cloud, where multicast is typically unavailable. List your actual server addresses. The port range per host covers multiple nodes and port autoincrement:

```xml
<property name="discoverySpi">
  <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
    <property name="ipFinder">
      <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
        <property name="addresses">
          <list>
            <value>server1:47500..47509</value>
            <value>server2:47500..47509</value>
            <value>server3:47500..47509</value>
          </list>
        </property>
      </bean>
    </property>
  </bean>
</property>
```

*To keep the Ignite 2 behavior: multicast finder.* Use it only where the network supports multicast (typically bare-metal or on-premises LANs, not cloud). The defaults match Ignite 2: multicast group `228.1.2.4`, port `47400`.

```xml
<property name="discoverySpi">
  <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
    <property name="ipFinder">
      <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.multicast.TcpDiscoveryMulticastIpFinder"/>
    </property>
  </bean>
</property>
```

### Removed Configuration Properties

*Skip this section if your Ignite 2 deployment used none of the removed features listed below (CDC, snapshot paths, Calcite, multi-disk storage, disk page compression, SQL validation) and set no `IGNITE_*` system properties (see [unsupported system properties](#unsupported-system-properties)).*

GridGain 8 removes two kinds of properties, and they fail in opposite ways.

*Configuration properties* (XML or bean) fail loudly. GridGain 8 does not start until you remove or replace a property that belongs to a removed feature:

- CDC: `DataStorageConfiguration.cdcWalPath` and `cdcWalDirectoryMaxSize`, `DataRegionConfiguration.cdcEnabled`, and the `CdcConfiguration` bean
- SQL: `SqlConfiguration.queryEnginesConfiguration` and `validationEnabled`, `TransactionConfiguration.txAwareQueriesEnabled`, and the Calcite, `IndexingQueryEngineConfiguration`, and `QueryEngineConfiguration` beans
- Storage: `walForceArchiveTimeout`, `writeRecoveryDataOnCheckpoint` (and its `checkpointRecoveryDataCompression` / `checkpointRecoveryDataCompressionLevel` companions), `extraStoragePaths`, `extraSnapshotPaths`, and per-cache `storagePaths`, `indexPath`, `diskPageCompression`, `diskPageCompressionLevel`
- Snapshots: `IgniteConfiguration.snapshotPath` and `snapshotThreadPoolSize`, and the `DumpReaderConfiguration` bean
- Other: `IgniteConfiguration.distributedPropertiesDefaultValues`, `TcpDiscoverySpi.addressFilter`, `ClientConfiguration.partitionAwarenessMapperFactory`, `ServiceConfiguration.statisticsEnabled`

`sqlPlanHistorySize` exists in GridGain 8.10 and does not need to be removed.

{% hint style="info" %}
An unknown XML or bean property fails startup with a message naming the offending property, for example `Configuration property CacheConfiguration.<name> does not exist`. Use it to find and remove the leftover Ignite-only property in your configuration.
{% endhint %}

*System properties* (`IGNITE_*`, set as JVM `-D` arguments or environment variables) behave the opposite way. An unrecognized one does not block startup, so a setting you relied on can stop taking effect with no failure. Audit your `-D` flags and environment against the [unsupported system properties](#unsupported-system-properties) below.

### Unsupported System Properties

Many Ignite 2 `IGNITE_*` system properties have no effect in GridGain. If you set one, whether as a JVM `-D` argument or an environment variable, GridGain 8 ignores it and logs a warning at node startup:

```text
Property IGNITE_USE_BINARY_ARRAYS is not supported in GridGain (reason: Typed binary arrays are not available in GridGain). See https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/migration-guides/apache-ignite-2x.
```

Remove the following properties from your startup configuration when migrating:

| Property | Reason it is unsupported | GridGain 8 alternative |
|---|---|---|
| `IGNITE_CALCITE_EXEC_IN_BUFFER_SIZE`<br>`IGNITE_CALCITE_EXEC_IO_BATCH_CNT`<br>`IGNITE_CALCITE_EXEC_IO_BATCH_SIZE`<br>`IGNITE_CALCITE_EXEC_MODIFY_BATCH_SIZE`<br>`IGNITE_CALCITE_REL_JSON_PRETTY_PRINT` | The GridGain SQL engine is H2-based; Calcite is not available. | See [SQL Changes](apis-and-clients.md#sql-changes). |
| `IGNITE_SNAPSHOT_SEQUENTIAL_WRITE` | The GridGain 8 snapshot subsystem differs from Ignite 2. | Use [GridGain snapshots](../../snapshots/snapshots-and-recovery.md). |
| `IGNITE_PERF_STAT_BUFFER_SIZE`<br>`IGNITE_PERF_STAT_CACHED_STRINGS_THRESHOLD`<br>`IGNITE_PERF_STAT_FILE_MAX_SIZE`<br>`IGNITE_PERF_STAT_FLUSH_SIZE` | The Performance Statistics subsystem is not implemented in GridGain. | Use [GridGain metrics and monitoring](../../monitoring/intro.md). |
| `IGNITE_ALLOW_MIXED_CACHE_GROUPS` | Mixed cache groups are not available in GridGain. |  |
| `IGNITE_ENABLE_OBJECT_INPUT_FILTER_AUTOCONFIGURATION` | Object input filter auto-configuration is not available in GridGain. |  |
| `IGNITE_USE_BINARY_ARRAYS` | Typed binary arrays are not available in GridGain. | Confirm it was not enabled on the Ignite 2 source before migrating data. An explicitly enabled binary-array format changes the on-disk and on-wire layout. |
| `IGNITE_SQL_FORCE_LAZY_RESULT_SET` | Not available in the GridGain H2-based SQL engine. | Enable lazy execution per query with `SqlFieldsQuery.setLazy(true)` or the JDBC thin `lazy` connection parameter. See [Lazy SQL Queries](../../../tuning-and-troubleshooting/performance-tuning/sql-tuning.md#lazy-sql-queries). |

Two other Ignite 2 properties are not on the warning list but are absent from GridGain 8, so they are ignored with *no* log line: `IGNITE_DATA_CENTER_ID` (use the data center ID of GridGain Data Center Replication) and `IGNITE_LOCAL_STORE_KEEPS_PRIMARY_ONLY` (the local-store feature was removed).

### Stricter Validation

GridGain 8 rejects things Ignite 2 allowed: duplicate SQL schema or index names, invalid cache names, and nodes that disagree on the binary field-sort setting (see [Binary Object Field Ordering](#binary-object-field-ordering)).

## Binary Object Field Ordering

The `IGNITE_BINARY_SORT_OBJECT_FIELDS` system property controls the order in which a binary object's fields are laid out on disk and on the wire. The value must be the same on every node and every client, and it must match the value that was set when the persisted data was written.

The default is `false` on both Ignite 2 and GridGain 8.x. *If your Ignite 2 cluster never set this property, the migration needs no action; skip the rest of this section.*

### 1. Check the Source Value

Search for `IGNITE_BINARY_SORT_OBJECT_FIELDS` in the JVM arguments and environment of the running Ignite 2 nodes. If it is not set, the source uses the default. Otherwise, record the value.

### 2. Apply the Value in GridGain

Set `-DIGNITE_BINARY_SORT_OBJECT_FIELDS=<source-value>` as a JVM system property on every GridGain 8 server node and every client. Roll it out everywhere at once. Any node or client with a different value is rejected at startup.

### 3. Verify After Start

After the first GridGain 8 node starts, run two checks:

* *Look at the logs.* A topology-validation or handshake error mentioning `IGNITE_BINARY_SORT_OBJECT_FIELDS` means a server or client is running with a different value.
* *Smoke-test a known key.* Run a key-based `get` against a row you know exists. If it returns nothing while `SELECT` over the same row succeeds, GridGain 8 is using a different value than what is on disk.

For background, see [Working with Binary Objects](../../../gridgain8-development/key-value-api/binary-objects.md).
