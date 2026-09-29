---
description: GridGain 8.8.4 introduces new features and improvements, including .NET to Java type mappings and incremental Data Replication state transfer by default.
hidden: true
---

# GridGain 8.8.4 Release Notes

## New Features

### .NET to Java Type Mappings

Default naming conventions specific for both platforms are now supported. For example:

```java
com.company.Model (Java)
```

and

```csharp
Com.Company.Model (.NET)
```

are now interoperable.

### Snapshot Utility and WAL Files Reader

This release introduces new functionality for WAL Files Reader to support additional diagnostics.
WAL segments information is now shown in the Snapshot Utility `LIST` command output.

## Changes in Behavior

The default mode for the Data Replication State transfer is now Incremental.
See the [Data Replication Incremental State Transfer](https://www.gridgain.com/docs/latest/administrators-guide/data-center-replication/managing-and-monitoring#data-replication-incremental-state-transfer) page for details. You can keep using the old behavior by setting the `GG_INCREMENTAL_STATE_TRANSFER` property to `false`. This should be done as a temporary measure for migrating to a newer GridGain version and not used in production environments.

## Known Issues

### Nodes May Crash During Update if Data Center Replication is Enabled on GridGain 8.8.4

GridGain updates data structure each time it receives a version update. Due to a bug in GridGain 8.8.4, entries from WAL logical records may cause errors if the version update was performed under load.

**Workaround**: If your nodes are affected, set  the`-DGG_INCREMENTAL_STATE_TRANSFER=false` parameter while you use GridGain 8.8.4, or remove load from the node before update.

### Rolling Upgrade Fails to Start when Security is Enabled

In GridGain 8.8.4, starting a rolling upgrade with the security feature enabled may cause the **Authorization failed** error.

**Workaround**: Use the `control-utility.sh` to start the rolling upgrade and explicitly specify the coordinator node host with the `--host xxxx --port xxxx` parameters   (coordinator node is the oldest node in cluster topology).

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32968 | Distributed Data Streamer | Fixed an issue when Data Streamer flushing could freeze due to a connectivity problem. |
| GG-32932 | GridGain Integrations | Updated Netty dependency from version 4.1.52.Final to version 4.1.61.Final in the ignite-cassandra module. |
| GG-32931 | Cluster SQL Engine | Fixed a possible index corruption after simultaneous index drop and node stop. |
| GG-32897 | Cluster Storage Engine | Fixed failure handler false positive triggering during checkpoint. |
| GG-32874 | Platforms & Thin Clients | .NET: Fixed binary type handling when NamespaceToLower or NamespacePrefix was specified. |
| GG-32831 | Platforms & Thin Clients | .NET: Fixed an issue with the AffinityKey not working when used as a QueryEntity key. |
| GG-32817 | Cluster Storage Engine | Nodes now properly fall back to full rebalance if historical rebalance fails. |
| GG-32795 | Platforms & Thin Clients | C++ thin: Fixed an issue that could prevent transactions from working properly when used with multiples nodes. |
| GG-32793 | Cluster Storage Engine | Fixed an issue that could cause an optimistic transaction commit failure with key contention. |
| GG-32789 | Platforms & Thin Clients | .NET: Extended ConfigurationManager dependency version range. |
| GG-32781 | Platforms & Thin Clients | .NET: Fixed race condition in Events example. |
| GG-32749 | Cluster SQL Engine | SQL: Fixed unexpected exception on sorted GROUP BY. |
| GG-32748 | Platforms & Thin Clients | .NET: Added LongCount support to LINQ provider. |
| GG-32740 | Cluster Storage Engine | Added support for the "--pages" argument to the IgniteWalConverter for finding pages in the WAL. |
| GG-32713 | Platforms & Thin Clients | .NET: Added NamespacePrefix and NamespaceToLower to BinaryBasicNameMapper. |
| GG-32604 | Distributed Data Structures | Fixed an issue that caused an exception during index building on a deactivated cluster. |
| GG-32398 | Cluster Deployment | Change peer class loading error to warning when the node fails to initialize peer class loading for an operation. |
| GG-32298 | Cluster Metrics & Monitoring | Added SqlFreeMemoryBytes showing real-time SQL engine memory utilization. |
| GG-32092 | Cluster Compute Grid | Improved memory footprint for compute tasks with the same name loaded by different class loaders. |
| GG-32076 | Cluster SQL Engine | Added new distributed property statistics.usage.state (ON,NO_UPDATE,OFF) to control statistics usages. |
| GG-31928 | Cluster Discovery | Fixed an issue that prevented a node from startup in case it could not obtain IP addresses to connect to. |
| GG-31913 | Cluster Discovery | Extended logging of client node failure. |
| GG-31908 | Cluster Affinity and Baseline Topology | Fixed an exception that could happen when a thick client was reconnecting. |
| GG-31837 | Platforms & Thin Clients | C++ thin client: Added a configuration parameter IgniteClientConfiguration::connectionsLimit, which can be used to limit number of active connections that thin client can have simultaneously. |
| GG-30902 | Cluster Storage Engine | Added progress logging when restoring the statuses of partitions along with the output of the top partitions, the processing time of which took the longest. |
| GG-30750 | Cluster SQL Engine | Added new statistics related SQL system views: STATISTICS_PARTITION_DATA, STATISTICS_LOCAL_DATA and STATISTICS_CONFIGURATION |
| GG-29829 | Cluster Data Snapshots and Recovery | Added metrics for the number of written and compressed bytes for WAL. |
| GG-18641 | Cluster SQL Engine | SQL statistics are now invalidated after 15% of rows are changed. This can be overridden by `ANALYZE <TABLE> WITH 'MAX_CHANGED_PARTITION_ROWS_PERCENT=30'`. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33028 | GridGain Integrations | Updated Jetty dependency from version 9.4.37 to version 9.4.39. |
| GG-32943 | Cluster Data Replication | Added a warning log message in case of removal operation information being lost before it was replicated to a remote DC. |
| GG-32915 | Cluster Data Replication | Fixed DR failure due to a long running transaction. |
| GG-32888 | GridGain Integrations | Docker images: Included dependency for Zstandard compression library. |
| GG-32832 | GridGain Integrations | Updated Jetty dependency from version 9.4.35.v20201120 to version 9.4.37.v20210219. |
| GG-32784 | GridGain Integrations | Updated org.bouncycastle dependencies from version 1.60 to version 1.68. |
| GG-32720 | Cluster Data Replication | Incremental datacenter replication is now enabled by default. |
| GG-32579 | Cluster Data Replication | Fixed a few issues in Incremental DR that lead to broken metrics and wrong DR state. |
| GG-32553 | Cluster Data Replication | Fixed NPE on getting incremental DR state via MBean. |
| GG-31337 | Cluster Data Replication | Removed deprecated methods from org.gridgain.grid.cache.dr.CacheDrMBean interface. |
| GG-30548 | Binary Objects | Avoid compressing keys for pure read operations. |
| GG-26664 | Cluster Security | Prevented snapshot utility from losing connection during long operations on a secure cluster. |
| GG-32613 | Cluster Data Replication | Fixed DR failure due to a long running transaction. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32935 | Cluster Data Snapshots and Recovery | Fixed WAL size calculation for the last snapshot in case of PITR. |
| GG-30672 | Cluster Data Snapshots and Recovery | Fixed an error when a client node with no snapshot configuration could not issue snapshot commands. |
| GG-30596 | Cluster Snapshot Utility | Improved snapshot utility by adding '--exec-after' parameter to SCHEDULE command for chain executions. |
| GG-29834 | Cluster Data Snapshots and Recovery | Added display of time intervals of Point-in-Time Recovery for command snapshot-utility.sh list. |
| GG-29832 | Cluster Data Snapshots and Recovery | Warning is shown now if a snapshot schedule is not set up properly for using PITR. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.5.3`, `8.5.4`, `8.5.4-p1`, `8.5.5`, `8.5.7-p2`, `8.5.8`, `8.5.8-p7`, `8.5.9`, `8.5.10`, `8.5.10-p1`, `8.5.11`, `8.5.12`,
`8.5.13`, `8.5.14`, `8.5.14-p2`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.18-p1`, `8.5.19`, `8.5.20`, `8.5.21`, 
`8.5.22`, `8.5.23`, `8.5.24`, `8.5.25`, `8.5.26`  `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`,
`8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, 
`8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`, `8.7.29`,
`8.7.30`, `8.7.31`, `8.7.32`, `8.7.33`, `8.8.1`, `8.8.2`, `8.8.3`

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
Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
