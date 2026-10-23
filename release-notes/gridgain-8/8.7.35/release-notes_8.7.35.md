---
description: >-
  GridGain 8.7.35 adds .NET-to-Java type mapping conventions and WAL Files Reader
  diagnostics, along with improvements and fixed issues across the Community,
  Enterprise, and Ultimate editions.
hidden: true
---

# GridGain 8.7.35 Release Notes

## New Features

GridGain 8.7.35 provides access to several new features and a variety of improvements.

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

### WAL Files Reader

This release introduces new functionality for WAL Files Reader to support additional diagnostics.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32995 | Distributed Data Streamer | Fixed an issue when Data Streamer flushing could freeze due to a connectivity problem. |
| GG-32982 | GridGain Integrations | Updated Netty dependency from version 4.1.52.Final to version 4.1.61.Final in the ignite-cassandra module. |
| GG-32936 | Cluster SQL Engine | Fixed a possible index corruption after simultaneous index drop and node stop. |
| GG-32927 | Platforms & Thin Clients | .NET: Fixed binary type handling when NamespaceToLower or NamespacePrefix was specified. |
| GG-32916 | Cluster Snapshot Utility | Fixed failure handler false positive triggering during checkpoint. |
| GG-32898 | Cluster Storage Engine | Nodes now properly fall back to full rebalance if historical rebalance fails. |
| GG-32866 | Cluster Discovery | Fixed an issue that prevented a node from startup in case it could not obtain IP addresses to connect to. |
| GG-32857 | Cluster Storage Engine | Fixed an issue that could cause an optimistic transaction commit failure with key contention. |
| GG-32855 | Cluster SQL Engine | SQL: Fixed unexpected exception on sorted GROUP BY. |
| GG-32822 | Cluster Deployment | Changed peer class loading error to warning when the node fails to initialize peer class loading for an operation. |
| GG-32814 | Cluster Affinity and Baseline Topology | Fixed an issue that led to the fact that auto adjustment of baseline was not triggered under certain conditions. |
| GG-32799 | Cluster Storage Engine | Added support for the "--pages" argument to the IgniteWalConverter for finding pages in the WAL. |
| GG-32796 | Platforms & Thin Clients | C++ thin: Fixed issue that could prevent transactions from working properly in case of multiple nodes. |
| GG-32780 | Cluster Affinity and Baseline Topology | Fixed an exception that may happen when a thick client was reconnecting. |
| GG-32767 | Platforms & Thin Clients | .NET: Added LongCount support to LINQ provider. |
| GG-32758 | Cluster Communication | Added support of IGNITE_ENABLE_FORCIBLE_NODE_KILL flag when inverse connection protocol is used. |
| GG-32743 | Distributed Data Structures | Fixed an issue that caused an exception during index building on a deactivated cluster. |
| GG-32706 | Cluster Communication | Fixed an issue when connection closed by the one node could lead to infinite connection attempts on the other node. |
| GG-32700 | Platforms & Thin Clients | .NET: Fixed DllNotFoundException in single file deployment on .NET 5. |
| GG-32686 | Cluster Storage Engine | Fixed an issue that led to cluster instability when WAL archive was disabled. |
| GG-32681 | Platforms & Thin Clients | .NET Thin Client: Added an automated check that client binary configuration is compatible to server binary configuration on client start. |
| GG-32614 | Cluster Storage Engine | Fixed an issue that could lead to OutOfMemoryError when rebalance was in progress. |
| GG-32541 | Cluster Storage Engine | Improved collecting of rebalancing statistics. |
| GG-32437 | Cluster Metrics & Monitoring | Added SqlFreeMemoryBytes showing real-time SQL engine memory utilization. |
| GG-32431 | Cluster Discovery | Extended logging of client node failure. |
| GG-32149 | Platforms & Thin Clients | C++ thin client: Added a configuration parameter IgniteClientConfiguration::connectionsLimit, which can be used to limit number of active connections that thin client can have simultaneously. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33028 | GridGain Integrations | Updated Jetty dependency from version 9.4.37 to version 9.4.39. |
| GG-32973 | Cluster Data Replication | Fixed DR failure due to a long running transaction. |
| GG-32961 | Cluster Data Replication | Fixed an issue that could prevent an exchange from completion with DR enabled. |
| GG-32846 | GridGain Integrations | Updated Jetty dependency from version 9.4.35.v20201120 to version 9.4.37.v20210219. |
| GG-32753 | Cluster Security | Prevented snapshot utility from losing connection during long operations on a secure cluster. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32951 | Cluster Data Snapshots and Recovery | Fixed WAL size calculation for the last snapshot in case of PITR. |
| GG-32533 | Cluster Snapshot Utility | Improved snapshot utility by adding '--exec-after' parameter to SCHEDULE command for chain executions. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`, `8.7.29`, `8.7.30`, `8.7.31`, `8.7.32`, `8.7.33`, `8.7.34`, `8.8.1`

## Known Limitations

### Jetty Configuration Incompatibility in GridGain 8.7.21 and Later

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

### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and Later

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

### Jetty Doesn't Accept Incorrect Configuration in GridGain 8.7.31 and Later

In GridGain 8.7.31 Jetty was upgraded to 9.4.33. Starting that version, Jetty has more strict validation of the
provided configuration files. Before that version, an incorrectly spelled property in the configuration file had no effect.
Starting this version, errors in the configuration will lead to an error on start.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration for REST
- The custom configuration has errors in it

You will need to fix the custom Jetty configuration before upgrading.

### `ignite.sh` No Longer Enables Remote JMX by Default in GridGain 8.7.31 and Later

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

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
