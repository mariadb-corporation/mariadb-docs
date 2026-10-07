---
description: GridGain 8.8.31 brings stability improvements, including monitoring events support in the Java thin client.
hidden: true
---

# GridGain 8.8.31 Release Notes

GridGain 8.8.31 brings stability improvements for GridGain.

## New Features

### Monitoring Events in Java Thin Client

In this release, new functionality was added that allows you to work with events from Java thin client. For more information about events in GridGain, see [Working with Events](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/events/events) section.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-36682 | Platforms & Thin Clients | C++ thin client: Fixed an issue that could cause crash when several nodes disconnected simultaneously. |
| GG-36615 | Platforms & Thin Clients | .NET: Thin client: Added partition awareness support for types with affinity key. |
| GG-36614 | Cluster SQL Engine | Fixed an issue that sometimes caused duplicate indexes to be created if CREATE INDEX command was performed without explicit index name. |
| GG-36605 | Diagnostics and Failure Handling | Added date information in ISO-8601 format to logs. |
| GG-36528 | Platforms & Thin Clients | Java thin: Fixed query entity index sort order in ClientCache#getConfiguration. |
| GG-36511 | Cluster SQL Engine | Fixed a potential concurrentModificationException for ScanQuerySystemView. |
| GG-36426 | Platforms & Thin Clients | ODBC: Calling SQLTables with parameters that are surrounded by single quotes is now handled properly. |
| GG-36395 | Cluster Storage Engine | Fixed a rare issue that could cause the cluster to stop responding when the cache is re-created. |
| GG-36241 | Platforms & Thin Clients | Java thin: added monitoring events. |
| GG-33353 | Cluster Storage Engine | Reduced heap usage for checkpoint history. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-36529 | GridGain Integrations | Backlog service is now undeployed automatically when FailoverPolicy is changed to a different policy then Backlog. |
| GG-36527 | Cluster Storage Engine | Reduced the load of clearing expired entries (regular entries with expired TTL and tombstones) by using a more accurate scheduling of the clearing task. |
| GG-36261 | Cluster Discovery | Dynamic cache create request from a client node fails with a proper error if cache configuration contains a class that is not available on the server. |
| GG-36208 | GridGain Integrations | Fixed an issue that stopped Kafka Sink Connector from reconnecting to cluster. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35781 | Cluster Data Snapshots and Recovery | Fixed an issue with changing cache name during snapshot restore procedure. |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-36401 | Control Center Agent | Code deployment artifacts will now be redeployed on cluster restart. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.22`, `8.7.28`, `8.7.29-p1`, `8.7.32`, `8.7.34`, `8.7.38`, `8.7.42-p2`, `8.8.1`, `8.8.2`, `8.8.2-p1`, `8.8.3`, `8.8.4`, `8.8.4-p2`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.8-p1`, `8.8.9`, `8.8.9-p1`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`, `8.8.13-p2`, `8.8.14`, `8.8.15`, `8.8.16`, `8.8.16-p2`, `8.8.17`, `8.8.18`, `8.8.18-p1`, `8.8.19`, `8.8.19-p1`, `8.8.20`, `8.8.21`, `8.8.22`, `8.8.22-p1`, `8.8.23`, `8.8.23-p3`, `8.8.24`, `8.8.25`, `8.8.25-p1`, `8.8.26`, `8.8.27`, `8.8.28`, `8.8.29`, `8.8.30`

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.11.1`, `2.12.0`, `2.13.0`,  `2.14.0`

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

#### .NET: GridGain Nuget Package Misses GridGain.Ignite Jars in 8.8.17 and Later

Add the `GridGain.Ignite` dependency to your project, so that jars from it are included.

#### .NET: Docker Images Need Additional Configuration

To run .NET SDK commands, install the .NET SDK. For more details, click [here](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=net60#dependencies).

## We Value Your Feedback
Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
