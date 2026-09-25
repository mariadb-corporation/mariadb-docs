---
description: >-
  Configuration changes when migrating from Apache Ignite 2 to GridGain 8:
  changed defaults, removed and unsupported properties, and binary field ordering.
---

# Configuration and Validation Changes

This topic covers the configuration defaults that change, the properties GridGain removes, its stricter validation, and the binary object field-ordering setting.

## Server Configuration Differences

### Changed Defaults

This section applies to every migration: review the table and decide each value deliberately, whether you restore the Ignite behavior or keep the GridGain default.

GridGain 8 changes a number of configuration defaults relative to Apache Ignite 2.

| Setting | Ignite default | GridGain default |
|---|---|---|
| `CacheConfiguration.readFromBackup` | `true` | `false` |
| `IgniteConfiguration.segmentationPolicy` | `USE_FAILURE_HANDLER` (enum member absent in GG) | `STOP` |
| `SqlConfiguration.sqlGlobalMemoryQuota` | unlimited (field absent) | `"60%"` of heap |
| `DataRegionConfiguration.metricsEnabled` | `false` | `true` |
| `TcpDiscoverySpi` IP finder | `TcpDiscoveryMulticastIpFinder` | `TcpDiscoveryVmIpFinder(shared=true)` |
| `TcpCommunicationSpi.messageQueueLimit` | `0` (unlimited) | `4096` |
| `ClientConnectorConfiguration.socketSendBufferSize` / `socketReceiveBufferSize` | `0` (OS default) | `262144` (256 KB) |
| `IgniteDataStreamer.allowOverwrite()` | `false` | `true` (via `IGNITE_DATA_STREAMER_ALLOW_OVERWRITE`, defaulting to `true`) |
| Thin client partition/affinity awareness | `partitionAwarenessEnabled = true` | `affinityAwarenessEnabled = false` (also renamed) |
| `TransactionConfiguration.txTimeoutOnPartitionMapExchange` | `0` (no timeout) | `60000` (ms) |
| `SqlConfiguration.longQueryWarningTimeout` | `3000` (ms) | `1000` (ms) |
| `IgniteConfiguration.rebalanceBatchesPrefetchCount` | `3` | `2` |
| `IGNITE_CHECKPOINT_TRIGGER_ARCHIVE_SIZE_PERCENTAGE` (system property) | `0.25` | `0.75` |

To preserve Ignite behavior, set each changed default explicitly. Use the following as a starting template and adapt it to your deployment. It restores the server-side defaults that differ between Apache Ignite 2.x and GridGain 8; the settings that live in cache or client code are listed separately below.

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <!-- GG default STOP; Ignite's USE_FAILURE_HANDLER is absent in GG,
         so choose a GG policy deliberately rather than restoring the Ignite value. -->
    <property name="segmentationPolicy" value="STOP"/>

    <!-- GG default: 2 -->
    <property name="rebalanceBatchesPrefetchCount" value="3"/>

    <property name="dataStorageConfiguration">
        <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
            <!-- GG default: true -->
            <property name="metricsEnabled" value="false"/>
            <property name="defaultDataRegionConfiguration">
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                    <property name="metricsEnabled" value="false"/>
                </bean>
            </property>
        </bean>
    </property>

    <!-- Restore Ignite's unlimited SQL memory (GG default: 60% of heap)
         and long-query warning timeout (GG default: 1000 ms). -->
    <property name="sqlConfiguration">
        <bean class="org.apache.ignite.configuration.SqlConfiguration">
            <property name="sqlGlobalMemoryQuota" value="0"/>
            <property name="longQueryWarningTimeout" value="3000"/>
        </bean>
    </property>

    <!-- GG aborts transactions during a partition map exchange after 60s; Ignite does not (0). -->
    <property name="transactionConfiguration">
        <bean class="org.apache.ignite.configuration.TransactionConfiguration">
            <property name="txTimeoutOnPartitionMapExchange" value="0"/>
        </bean>
    </property>

    <!-- GG default: 4096 -->
    <property name="communicationSpi">
        <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="messageQueueLimit" value="0"/>
        </bean>
    </property>

    <!-- GG default: 262144 (256 KB) buffers; 0 = OS default, as in Ignite. -->
    <property name="clientConnectorConfiguration">
        <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration">
            <property name="socketSendBufferSize" value="0"/>
            <property name="socketReceiveBufferSize" value="0"/>
        </bean>
    </property>
</bean>
```

Some Ignite defaults are restored through system properties (JVM `-D` arguments or environment variables) rather than configuration:

```shell
# GG triggers a checkpoint at 75% of the WAL archive size; Ignite at 25%.
IGNITE_CHECKPOINT_TRIGGER_ARCHIVE_SIZE_PERCENTAGE=0.25

# GG enables data-streamer overwrite by default; Ignite does not.
# (Or call allowOverwrite(false) per streamer in client code.)
IGNITE_DATA_STREAMER_ALLOW_OVERWRITE=false
```

The remaining defaults are not server-side configuration and must be set where they apply:

- *readFromBackup (per cache).* Set `readFromBackup=true` on each `CacheConfiguration` or cache template (GG default `false`).
- *Thin-client affinity awareness (client code).* Set `ClientConfiguration.setAffinityAwarenessEnabled(true)` (GG default `false`; renamed from `setPartitionAwarenessEnabled`).
- *Discovery (environment-specific).* Ignite defaults to multicast discovery. If your cluster relied on it, configure a `TcpDiscoveryMulticastIpFinder` or supply the static address list; GridGain defaults to `TcpDiscoveryVmIpFinder`.

Several of these defaults change behavior in ways that pass functional tests and surface only later: under load, on large data, or during a network event. The ones most likely to catch you out:

**Partition/affinity awareness (clients)**: Ignite enables it; GridGain disables it (and renames `setPartitionAwarenessEnabled` to `setAffinityAwarenessEnabled`). With it off, thin clients no longer route each request to the node that owns the key, so every operation takes an extra network hop. This passes functional tests but shows up as a latency and throughput regression under load. Re-enable it explicitly unless you have a reason not to.

**Discovery IP finder**: Ignite defaults to multicast discovery; GridGain defaults to the static `TcpDiscoveryVmIpFinder`, pre-seeded with `127.0.0.1:47500..47600` only. Nodes on the same host still find each other, but nodes on different hosts no longer do. A multi-host cluster that relied on multicast will not form until you supply the real node addresses or configure the multicast IP finder.

**`readFromBackup`**: Ignite can serve a read from a local backup copy; GridGain (default `false`) routes every read to the primary. Results are unaffected, but read load concentrates on primary nodes and latency can rise where you previously benefited from backup locality. Set it per cache to restore the Ignite behavior.

**SQL memory quota** (`sqlGlobalMemoryQuota`): Ignite runs SQL with no global memory quota; GridGain caps it at 60% of heap. A query that ran in Ignite can fail with a quota error the first time it processes a large result set, not during ordinary testing. Set it to `0` for unlimited, or tune it. See [SQL Changes](apis-and-clients.md#sql-changes).

**Data streamer overwrite** (`allowOverwrite`): Ignite's `IgniteDataStreamer` does not overwrite existing keys by default; GridGain enables overwrite. A streaming job that assumed existing entries were left in place will now replace them. Set `allowOverwrite(false)` in client code if you relied on the Ignite behavior.

**Transaction timeout on partition map exchange** (`txTimeoutOnPartitionMapExchange`): Ignite does not time out transactions during a partition map exchange (PME) by default (`0`); GridGain aborts them after 60 seconds. During a long PME, such as a node join or rebalance on a large cluster, transactions that Ignite would have let run can fail in GridGain. Set it to `0` to restore the Ignite behavior, or keep the timeout as a safeguard against PME stalls.

**Checkpoint trigger by WAL archive size** (`IGNITE_CHECKPOINT_TRIGGER_ARCHIVE_SIZE_PERCENTAGE`): Ignite triggers a checkpoint when the WAL archive reaches 25% of its maximum size; GridGain waits until 75%. GridGain checkpoints less often, so WAL archives grow larger and crash recovery can take longer. Set the system property to `0.25` to match Ignite.

**Segmentation policy**: Ignite's default `USE_FAILURE_HANDLER` delegates the response to your configured failure handler; that value does not exist in GridGain, whose default is `STOP`: a segmented node stops itself. If you relied on a custom failure-handler response to network segmentation, choose a GridGain segmentation policy deliberately.

#### Restoring Ignite Discovery

The discovery IP finder is the one changed default with no server-side template entry, because the value you need is environment-specific. Pick one of the following and set it explicitly on `TcpDiscoverySpi`.

*Recommended — static address list.* Best practice in every environment and required in the cloud, where multicast is typically unavailable. List your actual server addresses; the port range per host accommodates multiple nodes and port autoincrement:

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

*To preserve the exact Ignite behavior — multicast finder.* Use only where the network supports multicast (typically bare-metal or on-premises LANs, not cloud). The defaults match Ignite: multicast group `228.1.2.4`, port `47400`.

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

You can skip this section if your Apache Ignite deployment used none of the removed features listed below (CDC, snapshots, Calcite, multi-disk storage, SQL plan-history and validation) and set no `IGNITE_*` system properties (see [unsupported system properties](#unsupported-system-properties)).

GridGain 8 removes two kinds of properties, and they fail in opposite ways.

*Configuration properties* (XML or bean) fail loudly: a property tied to a removed feature will not parse, and GridGain will not start until you remove or replace it:

- CDC: `cdcWalPath`, `cdcEnabled`, `cdcWalDirectoryMaxSize`
- SQL: `queryEnginesConfiguration`, `sqlPlanHistorySize`, `validationEnabled`, `txAwareQueriesEnabled`
- Storage: `walForceArchiveTimeout`, `writeRecoveryDataOnCheckpoint` (and its `checkpointRecoveryDataCompression` / `checkpointRecoveryDataCompressionLevel` companions), multi-disk storage paths
- Snapshots and service interceptors: all related properties

{% hint style="info" %}
An unknown XML or bean property fails startup with a message naming the offending property, for example `Configuration property CacheConfiguration.<name> does not exist`. Use it to find and remove the leftover Ignite-only property in your configuration.
{% endhint %}

*System properties* (`IGNITE_*`, set as JVM `-D` arguments or environment variables) behave the opposite way: an unrecognized one does not block startup and is simply ignored, so a setting you relied on can stop taking effect with no failure. Audit your `-D` flags and environment against the [unsupported system properties](#unsupported-system-properties) below.

### Unsupported System Properties

A number of Apache Ignite `IGNITE_*` system properties have no effect in GridGain. If you set one, whether as a JVM `-D` argument or an environment variable, GridGain ignores it and logs a throttled warning at node startup:

```text
Property IGNITE_USE_BINARY_ARRAYS is not supported in GridGain. See https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/migration-guides/apache-ignite-2x/configuration.
```

Remove the following properties from your startup configuration when migrating:

| Property | Reason it is unsupported | GridGain alternative |
|---|---|---|
| `IGNITE_CALCITE_EXEC_IN_BUFFER_SIZE`<br>`IGNITE_CALCITE_EXEC_IO_BATCH_CNT`<br>`IGNITE_CALCITE_EXEC_IO_BATCH_SIZE`<br>`IGNITE_CALCITE_EXEC_MODIFY_BATCH_SIZE`<br>`IGNITE_CALCITE_REL_JSON_PRETTY_PRINT` | The GridGain SQL engine is H2-based; Calcite is not available. | See [SQL Changes](apis-and-clients.md#sql-changes). |
| `IGNITE_SNAPSHOT_SEQUENTIAL_WRITE` | The GridGain snapshot subsystem differs from Apache Ignite. | Use [GridGain snapshots](../../snapshots/snapshots-and-recovery.md). |
| `IGNITE_PERF_STAT_BUFFER_SIZE`<br>`IGNITE_PERF_STAT_CACHED_STRINGS_THRESHOLD`<br>`IGNITE_PERF_STAT_FILE_MAX_SIZE`<br>`IGNITE_PERF_STAT_FLUSH_SIZE` | The Performance Statistics subsystem is not implemented in GridGain. | Use [GridGain metrics and monitoring](../../monitoring/intro.md). |
| `IGNITE_ALLOW_MIXED_CACHE_GROUPS` | Mixed cache groups are not available in GridGain. |  |
| `IGNITE_ENABLE_OBJECT_INPUT_FILTER_AUTOCONFIGURATION` | Object input filter auto-configuration is not available in GridGain. |  |
| `IGNITE_USE_BINARY_ARRAYS` | Typed binary arrays are not available in GridGain. | Confirm it was not enabled on the Apache Ignite source before migrating data; an explicitly enabled binary-array format changes the on-disk and on-wire layout. |
| `IGNITE_SQL_FORCE_LAZY_RESULT_SET` | Not available in the GridGain H2-based SQL engine. | Enable lazy execution per query with `SqlFieldsQuery.setLazy(true)` or the JDBC thin `lazy` connection parameter. See [Lazy SQL Queries](../../../ha-and-performance/performance-tuning/sql-tuning.md#lazy-sql-queries). |
| `IGNITE_THIN_CLIENT_ASYNC_REQUESTS_WAIT_TIMEOUT` | This thin-client async request setting is not available in GridGain. |  |

### Stricter Validation

GridGain rejects things Ignite allowed: duplicate SQL schema or index names, invalid cache names, and nodes that disagree on the binary field-sort setting (see [Binary Object Field Ordering](#binary-object-field-ordering)).

## Binary Object Field Ordering

The `IGNITE_BINARY_SORT_OBJECT_FIELDS` system property controls the order in which a binary object's fields are laid out on disk and on the wire. The value must be the same on every node and every client, and it must match the value that was set when the persisted data was written.

The default is `false` on both Apache Ignite 2.x and GridGain 8.x. *If your Ignite cluster never set this property, the migration needs no action; skip the rest of this section.*

### 1. Check the Source Value

Search for `IGNITE_BINARY_SORT_OBJECT_FIELDS` in the JVM arguments and environment of the running Ignite nodes. If it is not set, the source uses the default. Otherwise, record the value.

### 2. Apply the Value in GridGain

Set `-DIGNITE_BINARY_SORT_OBJECT_FIELDS=<source-value>` as a JVM system property on every GridGain server node and every client. Roll it out everywhere at once. Any node or client with a different value is rejected at startup.

### 3. Verify After Start

After the first GridGain node starts, run two checks:

* *Look at the logs.* A topology-validation or handshake error mentioning `IGNITE_BINARY_SORT_OBJECT_FIELDS` means a server or client is running with a different value.
* *Smoke-test a known key.* Run a key-based `get` against a row you know exists. If it returns nothing while `SELECT` over the same row succeeds, GridGain is using a different value than what is on disk.

For background, see [Working with Binary Objects](../../../gridgain8-usage/key-value-api/binary-objects.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
