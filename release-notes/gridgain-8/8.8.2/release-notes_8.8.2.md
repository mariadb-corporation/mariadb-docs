---
description: GridGain 8.8.2 introduces snapshot encryption, SQL tracing, a C++ thin client SQL API, and new checkpoint metrics, along with many improvements and fixes.
hidden: true
---

# GridGain 8.8.2 Release Notes

## New Features

GridGain 8.8.2 provides access to a variety of new features and improvements.

### Snapshot Encryption

Starting this version, snapshots can be encrypted. To encrypt a snapshot, specify an encryption key
when creating the snapshot:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh snapshot -type=full -encryption_key=SNAPSHOT_MASTER_KEY
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat snapshot -type=full -encryption_key=SNAPSHOT_MASTER_KEY
```
{% endtab %}
{% endtabs %}

Note that Point-in-Time Recovery currently cannot be used together with Encryption.

### SQL Tracing

SQL queries are added to the tracing framework. This feature allows to use such tools
as GridGain Control Center to visualize the execution of an SQL query and see how much time
each execution step takes.

To start collecting SQL traces, use the following command:

{% tabs %}
{% tab title="Unix" %}
```shell
control.sh --tracing-configuration set --scope SQL --sampling-rate 1
```
{% endtab %}
{% tab title="Windows" %}
```shell
control.bat --tracing-configuration set --scope SQL --sampling-rate 1
```
{% endtab %}
{% endtabs %}

### SQL API for C++ Thin Client

Starting this version, C++ users can run SQL queries right from the C++ Thin Client.

```cpp
    SqlFieldsQuery qry('select name from Person');
    QueryFieldsCursor cursor = cache.Query(qry);
    while (cursor.HasNext()) {
        QueryFieldsRow row = cursor.GetNext();
        std::cout << row.GetNext<std::string>() << std::endl;
    }
```

### New Checkpoint Metrics

This release adds a variety of new metrics related to the checkpointing mechanism of the GridGain Native Persistence.
These metrics will be of interest to advanced users who want to monitor performance of the persistence on a
fine-grained level.

The list of the new metrics:

- `lastCheckpointStart`
- `beforeLockDuration`
- `listenersExecuteDuration`
- `lockHoldDuration`
- `walCpRecordFsyncDuration`
- `writeCheckpointEntryDuration`
- `splitAndSortCpPagesDuration`
- `CheckpointBeforeLockHistogram`
- `CheckpointLockWaitHistogram`
- `CheckpointListenersExecuteHistogram`
- `CheckpointMarkHistogram`
- `CheckpointLockHoldHistogram`
- `CheckpointPagesWriteHistogram`
- `CheckpointFsyncHistogram`
- `CheckpointWalRecordFsyncHistogram`
- `CheckpointWriteEntryHistogram`
- `CheckpointSplitAndSortPagesHistogram`
- `CheckpointHistogram`

These metrics can be viewed via the usual monitoring tools such as GridGain Control Center.

## Changes in Behavior

### Hiding Sensitive Data in the Logs

In previous versions, potentially sensitive data such as database keys and values could be
printed in the logs by default. To hide this data, a user would set a system property
`IGNITE_TO_STRING_INCLUDE_SENSITIVE=true`.

Starting this version, the default behavior is to replace potentially sensitive data in the logs
with a hash of that data. This behavior can be configured with a system property `IGNITE_SENSITIVE_DATA_LOGGING`.
The property has three possible values:

- `hash` - replace sensitive data with hashes (the default)
- `none` - completely hide sensitive data
- `plain` - show sensitive data in the logs (the old default)

The `IGNITE_TO_STRING_INCLUDE_SENSITIVE` property is now deprecated.

## Managing Point-in-Time Recovery

Before this version, users had to enable a static configuration property `pointInTimeRecoveryEnabled=true` on all nodes
in order to enable Point-in-Time Recovery.

Starting this version, the `pointInTimeRecoveryEnabled` property is deprecated. It is replaced by a dynamic cluster-wide property
controlled by the following command:

{% tabs %}
{% tab title="Unix" %}
```shell
control.sh --property set --name pointInTimeRecoveryEnabled --val true
```
{% endtab %}
{% tab title="Windows" %}
```shell
control.bat --property set --name pointInTimeRecoveryEnabled --val true
```
{% endtab %}
{% endtabs %}

If your cluster already has the deprecated pointInTimeRecoveryEnabled set, its value is used to initialize
the new dynamic property, so the cluster behavior does not change after the upgrade.

## Known Issues

### Rolling Upgrade State is Lost If All Server Nodes are Down

If a rolling upgrade procedure is started, and during the upgrade all server nodes are stopped
at the same time (for example, due to a hardware malfunction), the client nodes observe incorrect rolling upgrade
state. In this case, the client nodes also have to be restarted manually.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32322 | Platforms & Thin Clients | Fixed LINQ to SQL translation for queries with combined JOIN and GROUP BY operators. |
| GG-32290 | Cluster Deployment | Added API for getting cluster tag to IgniteCluster public interface. |
| GG-32287 | Cluster Metrics & Monitoring | Added checkpoint metrics. |
| GG-32274 | Cluster Storage Engine | Fixed bug when only one index was defragmented during defragmentation. |
| GG-32264 | Platforms & Thin Clients | Improved the performance of primitives deserialization. |
| GG-32253 | Platforms & Thin Clients | Improved handling of overloaded service methods. |
| GG-32251 | Platforms & Thin Clients | Binary configuration parameters of the Java Ignite service settings were avoided to simplify calls of the Java service. |
| GG-32237 | Platforms & Thin Clients | Java thin: allow IPv6 server addresses. |
| GG-32218 | Platforms & Thin Clients | Fixed issue with missing array type passed in Services. |
| GG-32209 | Platforms & Thin Clients | Added the BinaryConfiguration.TimestampConverter function to allow custom time zone conversion. |
| GG-32131 | Platforms & Thin Clients | Added BinaryConfiguration.ForceTimestamp function to globally enable the interoperable DateTime format and allow timestamp as key and cache value. |
| GG-32080 | Control Center Agent | Control Center Agent merges schema-only metric messages to one message before sending it to Control Center. |
| GG-32056 | Control Center Agent | Fixed SSL arguments of URL command. |
| GG-32055 | Control Center Agent | Fixed a bug causing propagation of the wrong connection status. |
| GG-32035 | Platforms & Thin Clients | .Net: Added RendezvousAffinityFunction.BackupFilter functionality with only one predefined implementation - ClusterNodeAttributeAffinityBackupFilter. |
| GG-32022 | Control Center Agent | Added support for collecting limited metrics upon request from the Control Center. |
| GG-31989 | Cluster SQL Engine | Fixed an issue with unsupported SQL data type INTERVAL: the INTERVAL value is converted to BIGINT data type for the result set. Implicit conversion from/to numeric types also added. |
| GG-31962 | Cluster Storage Engine | Fixed an issue that led to an `AssertionError` when a client node was joining or leaving concurrently with `ATOMIC` cache updates. |
| GG-31933 | Cluster Storage Engine | Added new system property IGNITE_EXECUTE_DURABLE_BACKGROUND_TASKS_ON_NODE_START_OR_ACTIVATE to turn off execution of background tasks on node start or cluster activation. |
| GG-31881 | GridGain Integrations | Added Spring Expression Language support for Spring Data. |
| GG-31877 | Cluster Storage Engine | Fixed an issue that could lead to node failure when -DIGNITE_PDS_LOG_CP_READ_LOCK_HOLDERS=true option was used. |
| GG-31807 | Cluster Communication | Fixed an issue with the inverse connection request that was not canceled immediately when node failure is detected. |
| GG-31776 | Cluster SQL Engine | Fixed an issue causing duplicated rows in query results when partition eviction was in progress. |
| GG-31751 | Platforms & Thin Clients | .NET: Fixed misleading exception when LINQ expression could not be translated to SQL. |
| GG-31510 | Cluster Storage Engine | Fixed an issue when a node's failure handler could be triggered by a long persistent cache recovery on startup. |
| GG-31395 | Cluster Storage Engine | Fixed issue causing NullPointerException when recovering a transaction. |
| GG-31382 | Cluster SQL Engine | Fixed OutOfMemoryError in SQL queries with the LAZY flag due to ignoring the SqlGlobalMemoryQuota option. |
| GG-31373 | Cluster Storage Engine | Fixed an issue when NullPointerException occurred at node startup. |
| GG-31271 | Cluster Storage Engine | IgniteOutOfMemoryException no longer triggers node's failure handler. |
| GG-31166 | Cluster Metrics & Monitoring | Fixed "allocated RAM" metric for clusters with both persistent and in-memory caches. |
| GG-31113 | Control.(sh/bat) | console.sh "--baseline" command is extended with information about the host's IP addresses. |
| GG-31007 | Cluster Continuous Queries | Fixed an issue where exception in static initializer during remote filter deployment could lead to the server node failure. |
| GG-30932 | Control Center Agent | Fixed a compatibility issue after removing the Control Center agent JAR from the classpath. |
| GG-30870 | Platforms & Thin Clients | C++ thin client: Added SQL API. |
| GG-30684 | Cluster Compute Grid | Fixed exception when stopping a node with Collision SPI enabled. |
| GG-30683 | Platforms & Thin Clients | .NET: Added an ability to enable Java peer class loading via IgniteConfiguration. |
| GG-30610 | Platforms & Thin Clients | .NET: Fixed CachePartialUpdateException when key and value referenced the same objects in an async cache operation. |
| GG-30588 | Cluster Communication | Fixed an issue with the local cluster group using incorrect node id after reconnecting. |
| GG-30501 | Cluster Security | The IGNITE_TO_STRING_INCLUDE_SENSITIVE system property has been deprecated. Added new system property IGNITE_SENSITIVE_DATA_LOGGING with possible values: "plain", "hash", "none". |
| GG-30353 | Cluster Storage Engine | Added new LastCheckpointStart metric indicating the start time of the checkpoint. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32141 | Cluster Data Replication | Fixed a potential failure of the data streamer with allowOverwrite=false and the function of incremental data replication state transfer enabled. |
| GG-32116 | Cluster Data Snapshots and Recovery | Fixed an issue where the snapshot commands MOVE and COPY would throw an exception if there are no WAL segments when point-in-time recovery is enabled. |
| GG-32079 | Cluster Data Snapshots and Recovery | Fixed an issue with starting the cache after canceling the restore of a snapshot using the "force" flag. |
| GG-32111 | Cluster Data Replication | Fixed an issue causing excessive Java heap memory usage when Data Center Replication was enabled for TRANSACTIONAL caches. |
| GG-31987 | Cluster Data Replication | Fixed an issue that could lead to node hanging after a restart when Native Persistence and Data Center Replication were used. |
| GG-31966 | Cluster Data Replication | New DR metrics added for pendingQueue, backupQueue and sender buffer sizes. |
| GG-31838 | Cluster SQL Engine | Fixed an issue causing incorrect SQL results when an open-range predicate over a primary key was used. |
| GG-31343 | Cluster Data Replication | Fixed a bug when connection to remote DC could be unexpectedly closed under load. |
| GG-30117 | Cluster Data Snapshots and Recovery | The entire snapshot chain metadata is now be validated before taking an incremental snapshot. |
| GG-29833 | Cluster Data Snapshots and Recovery | SnapshotConfiguration#pointInTimeRecoveryEnabled is now deprecated. Use control.sh/.bat '--property' command to set 'pointInTimeRecoveryEnabled' property cluster-wide. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`,
`8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`,
`8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`,
`8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`,
`8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`, `8.7.29`, `8.7.30`, `8.7.31`, `8.7.32`,
`8.7.33`,
`8.8.1`

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

To workaround this issue, alter the Jetty configuration to use `org.eclipse.jetty.util.ssl.SslContextFactory$Server` or `org.eclipse.jetty.util.ssl.SslContextFactory$Client`.
See the configuration example at the [Client Certificate Authentication](https://www.gridgain.com/docs/latest/administrators-guide/security/authentication#client-certificate-authentication) page.

#### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and Later

In GridGain 8.7.26, the default value of the property `IgniteConfiguration.rebalanceThreadPoolSize` changed from `1` to `min(4, number of CPU / 4)`.
It may cause a compatibility issue under the following conditions:

- When a Rolling Upgrade is performed
- The upgrade is performed from 8.5.7 version (or earlier) to 8.5.x or from 8.7.3 (or earlier) to 8.7.x
- The server nodes have at least 8 CPU cores
- The nodes configuration does not have the property `IgniteConfiguration.rebalanceThreadPoolSize`, so the default value is used

In this case, an exception is thrown with an error message similar to the following:

```text
сlass org.apache.ignite.IgniteException: Rebalance configuration mismatch (fix configuration or set -DIGNITE_SKIP_CONFIGURATION_CONSISTENCY_CHECK=true system property).
Different values of such parameter may lead to rebalance process instability and hanging.  [rmtNodeId=5fc58fb7-209d-489a-8034-0127a81abed6, locRebalanceThreadPoolSize = 4, rmtRebalanceThreadPoolSize = 1]
```

To workaround this issue, change the configuration of the server nodes to `rebalanceThreadPoolSize=1` so that it matches
the previous default configuration. For example:

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="rebalanceThreadPoolSize" value="1"/>

    <!-- The rest of the configuration goes here -->
</bean>
```

#### Jetty Doesn't Accept Incorrect Configuration in GridGain 8.7.31 and Later

In GridGain 8.7.31 Jetty was upgraded to 9.4.33. Starting that version, Jetty has more strict validation of the
provided configuration files. Before that version, an incorrectly spelled property in the configuration file had no effect.
Starting this version, errors in the configuration will lead to an error on start.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration for REST
- The custom configuration has errors in it

You will need to fix the custom Jetty configuration before upgrading.

#### `ignite.sh` No Longer Enables Remote JMX by Default in GridGain 8.7.31 and Later

Starting from 8.7.31 version, GridGain no longer attempts to automatically enable the remote JMX.
Default settings are known to cause issues if customized (for example, secure the connection).
Also, in most cases, remote JMX is not required since many tools use local JMX connections (not using TCP).

Your setup may be affected if:

- You start GridGain nodes via `ignite.sh` script
- You connect to GridGain nodes' JMX interface remotely over TCP using the default configuration

To continue using remote JMX, you need to manually specify the required JMX settings.
Please see the example below.
Note that you don't need remote JMX if you use a local connection,
such as connecting JConsole to a GridGain process on the same host.

```bash
export JVM_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=33333 \
    -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false"

bin/ignite.sh
```

### Rolling Upgrade from GridGain 8.7.9 and Earlier Fails if Data Center Replication is Enabled

Rolling upgrades from GridGain 8.7.9 and earlier to current GridGain version fails if [data center replication](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/data-center-replication/introduction) is enabled and under load.

To work around this issue, you can first upgrade to GridGain 8.7.21, or a later 8.7.x version, and then to current version.

## We Value Your Feedback
Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
