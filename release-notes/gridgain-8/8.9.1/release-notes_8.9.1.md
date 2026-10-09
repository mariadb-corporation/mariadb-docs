---
description: >-
  GridGain 8.9.1 brings significant new features to GridGain ecosystem, as well as major changes to default configuration aimed at making GridGain more stable and consistent in modern environments.
hidden: true
---

# GridGain 8.9.1 Release Notes

## Overview

GridGain 8.9.1 brings significant new features to GridGain ecosystem, as well as major changes to default configuration aimed at making GridGain more stable and consistent in modern environments.

## New Features

### New Method to Get Local Entry Size

GridGain 8.9.1 introduces a new `IgniteCache.localEntrySize()` method that can be used to get local entry sizes. You can use this method to keep track of all entries on the node to only fetch as much as you need.

### New System View

A new `CLIENT_CONNECTION_ATTRIBUTES` system property was added. This view provides extended information about the thin client. For more information, see [System Views](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/monitoring-metrics/system-views#client_connection_attributes) topic.

## Changes in Behavior

### New Default Values

GridGain 8.9.1 introduces a large number of changes to default values. These changes are intended to bring default GridGain behavior more in line with typical use cases, reducing the need for custom configurations.

When migrating to this version, make sure to check [Changed Default Values in GridGain 8.9.1 and Later](#changed-default-values-in-gridgain-8.9.1-and-later). If you already are using custom values for the changed properties, no actions are needed.

{% hint style="info" %}
Rolling upgrade is only possible if all nodes in the cluster have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. This change affects the service framework used by GridGain, and different framework versions are not compatible.
{% endhint %}

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-37805 | Cluster Affinity and Baseline Topology | Added a system property IGNITE_MIN_AFFINITY_HISTORY_SIZE that can be used to set minimum size for affinity assignment history. |
| GG-37739 | Cluster Discovery | TcpDiscoveryVmIpFinder is now used for cluster TCP/IP discovery by default. |
| GG-37737 | General | Message queue limit is now 4096 messages. |
| GG-37704 | Cluster Storage Engine | Added a new method IgniteCache.localEntrySize() that can be used to get entry size in bytes. |
| GG-37687 | Cluster Storage Engine | Fixed an AssertionError that happened when calling cache.get() method inside transactions that contained CacheEntryProcessor with remove operations. |
| GG-37670 | Platforms & Thin Clients | Fixed a potential infinite loop during SSL handshake with malicious or garbage data. |
| GG-37649 | Cluster Security | Updated netty from version 4.1.94 to version 4.1.100. |
| GG-37555 | Platforms & Thin Clients | .NET: Fixed a potential node crash when certain symbols were written to the console from Java and RedirectJavaConsoleOutput was enabled in .NET. |
| GG-37468 | Cluster Storage Engine | Fixed a rare issue that could lead to a long partition map exchange. |
| GG-37466 | Cluster Affinity and Baseline Topology | Fixed a rare issue that could lead to incorrect handling of lost partitions. |
| GG-37463 | Platforms & Thin Clients | ODBC connector: Fixed a memory leak caused by improperly handled disconnects. |
| GG-37438 | General | The IGNITE_ALLOW_ATOMIC_OPS_IN_TX option is now false by default. |
| GG-37434 | General | The DataRegionConfiguration.metricsEnabled setting is now true by default. |
| GG-37433 | General | Verbose log mode is now used by default. Added the '-q' command line argument to set quiet log mode. |
| GG-37432 | General | Checkpointing is now triggered upon reaching 75% of minWalArchiveSize by default. |
| GG-37430 | General | The readFromBackup property of the cache configuration is now false by default. |
| GG-37429 | Cluster Storage Engine | The TX_TIMEOUT_ON_PARTITION_MAP_EXCHANGE property is now 1 minute by default. |
| GG-37304 | Platforms & Thin Clients | .NET: Added UnwrapNullablePrimitiveTypes property to BinaryConfiguration, which fixes binary metadata for nullable value types to match Java behavior. |
| GG-37242 | Cluster Storage Engine | Fixed an issue that caused some WAL segments to be moved to WAL archive and compacted too early. |
| GG-36790 | Platforms & Thin Clients | The ClusterGroup.forNodeId method now handles all provided ids. |
| GG-36789 | Platforms & Thin Clients | Added the CLIENT_CONNECTION_ATTRIBUTES system view. |
| GG-36788 | Platforms & Thin Clients | Added debug level information for client connections  logs. |
| GG-34700 | Cluster Storage Engine | Optimized consumption of memory heap while expiring cache entries. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-37650 | Cluster Security | Updated jetty library from version 9.4.51.v20230217 to version 9.4.53.v20231009 to fix CVE-2023-44487. |
| GG-37523 | GridGain Integrations | Fixed a data loss issue caused by improper reconnect in KafkaSinkConnector. |
| GG-37448 | Cluster Data Replication | Fixed potential deadlock in DrReceiver during cluster deactivation. |
| GG-37437 | General | The allowOverwrite property of the data streamer is now true by default. |
| GG-37435 | General | Data Storage metrics are now enabled by default. |
| GG-37431 | General | Results of sql query execution are now obtained lazily by default. |
| GG-37426 | General | The default implementation of Ignite services is now the event-driven implementation. |
| GG-36804 | Cluster Data Replication | Fixed an issue that was caused by defragmentation of the cache after data center replication. |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-37449 | Control Center Agent | Added support for retrieving binary type metadata. |
| GG-37863 | Control Center Agent | Added support for scan queries. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Migrating From GridGain 8.9.0

GridGain 8.9.1 introduces a large number of changes in default configuration values. Your setup may be affected if you are using default configuration.

When migrating to GridGain 8.9.1, make sure to check [Changed Default Values in GridGain 8.9.1 and Later](#changed-default-values-in-gridgain-8.9.1-and-later) section for any parameters you need to change.

{% hint style="danger" %}
Rolling upgrade is only possible if all nodes in the cluster have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. This change affects the service framework used by GridGain, and different framework versions are not compatible. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Migrating From GridGain 8.X

When migrating from GridGain 8.8 to GridGain 8.9, no special actions are required for core functionality migration. By using [rolling upgrades](https://www.gridgain.com/docs/gridgain8/latest/installation-guide/rolling-upgrades), you can update from any GridGain version listed below. You may need to perform minor configuration changes to ensure stability post migration.

{% hint style="info" %}
While updates from GridGain 8.7.X and earlier 8.8.X  versions are possible, they may require additional actions to your configuration and  depending on cumulative changes in the version.
{% endhint %}

- If you are using GridGain Enterprise or Ultimate, the `COPY` command was reworked as described in the COPY Command Changes section. The syntax for working with CSV remains the same, but the path is now calculated on the **node** and the client. This change does not affect GridGain Community edition.

  To disable this behavior and use the old copy command, pass the `disabledFeatures=SERVER_BULK_LOAD` parameter in the JDBC connection command:

  ```
  jdbc:ignite:thin://127.0.0.1/?disabledFeatures=SERVER_BULK_LOAD
  ```

- If you are using one of the optional modules listed in the Removed Modules section, they will continue to work, but compatibility and stability on GridGain 8.9 is not guaranteed. Consider using the alternatives:
  - Visor CMD and GUI can be replaced by [GridGain Control Center](https://www.gridgain.com/docs/control-center/latest/overview#system-requirements).
  - The spark module can be replaced by the Spark [Ignite Extension](https://github.com/apache/ignite-extensions).
- If you are using default values in your configuration, you may need to set them manually to keep you cluster working the same way as in previous versions. Make sure to check [Changed Default Values in GridGain 8.9.1 and Later](#changed-default-values-in-gridgain-8.9.1-and-later) section for any parameters you need to change.

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.22`, `8.7.28`, `8.7.29-p1`, `8.7.32`, `8.7.34`, `8.7.38`, `8.7.42-p2`, `8.8.1`, `8.8.2`, `8.8.2-p1`, `8.8.3`, `8.8.4`, `8.8.4-p2`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.8-p1`, `8.8.9`, `8.8.9-p1`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`, `8.8.13-p2`, `8.8.14`, `8.8.15`, `8.8.16`, `8.8.16-p2`, `8.8.17`, `8.8.18`, `8.8.18-p1`, `8.8.19`, `8.8.19-p1`, `8.8.20`, `8.8.21`, `8.8.22`, `8.8.22-p1`, `8.8.23`, `8.8.23-p3`, `8.8.24`, `8.8.25`, `8.8.25-p1`, `8.8.26`, `8.8.27`, `8.8.28`, `8.8.29`, `8.8.30`, `8.8.31`, `8.8.32`, `8.8.33`, `8.8.34`, `8.8.35`, `8.8.36`, `8.9.0`

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.11.1`, `2.12.0`, `2.13.0`,  `2.14.0`,  `2.15.0`

### Known Limitations

#### Changed Default Values in GridGain 8.9.1 and Later

{% hint style="danger" %}
The change to `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` prevents rolling upgrade from earlier versions to GridGain 8.9.1 unless the default value is manually configured to be `false`.
{% endhint %}

If you are updating from GridGain 8.8.X or 8.9.0, a large number of default values have been changed.

These changes may affect the stability or performance of your cluster if you are using default values.

We recommend checking the list below to make sure the changes do not have an adverse effect, and setting the value manually if necessary.

- Service processor now use event-driven implementation by default. You can keep the old behavior by setting the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLE` property to `false`. Make sure that all nodes in the cluster are set to the same value.
- Data region metrics are now enabled by default. This may have a minor (within 2%) adverse effect on performance. You can keep the old behavior by setting the `DataRegionConfiguration.metricsEnabled` value to `false`.
- Data storage metrics are now enabled by default. This may have a minor (within 2%) adverse effect on performance. You can keep the old behavior by setting the `DataStorageConfiguration.metricsEnabled` value to `false`.
- `TcpCommunicationSpi` communication protocol now has a limit of 4096 messages for the outgoing messages queue by default.
- Atomic operations are now not allowed in transactions by default. You can keep the old behavior by setting the `IGNITE_ALLOW_ATOMIC_OPS_IN_TX` value to `true`.
- Logs are now in verbose mode by default. You can use the `-q` command line argument in the `ignite.sh` script to keep current log behavior.
- SQL queries are now loaded lazily by default. This reduces memory consumption on medium and large queries and potentially improves garbage collection performance. You can keep the old behavior by setting the `SqlFieldsQuery.setLazy(false)`.
- Cache entries are now read from primary partitions by default, even if an entry is available on the node in a backup partition. This may have a minor performance impact, but significantly increases cluster stability. You can keep the old behavior by setting the `readFromBackup` property to `true`.
- Partition map exchange transactions now time out after 1 minute instead of 0 (infinite) by default. You can keep the old timeout by setting the `TX_TIMEOUT_ON_PARTITION_MAP_EXCHANGE` setting to 0.
- Data streamer now overwrites entries by default. You can keep the old behavior by setting the `stmr.allowOverwrite` property to `false`.
- TCP discovery now uses static IP finder `TcpDiscoveryVmIpFinder` by default. To keep the old behavior, set the IP finder to use [multicast IP finder](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/clustering/tcp-ip-discovery#multicast-ip-finder).
- Checkpointing process now starts upon reaching 75% of `minWalArchiveSize` instead of 25%. You can keep the old behavior by setting the `IGNITE_CHECKPOINT_TRIGGER_ARCHIVE_SIZE_PERCENTAGE` system variable to `0.25`.

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

#### .NET: GridGain Nuget Package Misses GridGain.Ignite Jars in 8.8.17 and Later

Starting with GridGain 8.8.17, the `GridGain.Ignite` dependency is not included in the Nuget package. To use GridGain in your project, make sure to include the dependency explicitly so that jars from it are included.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
