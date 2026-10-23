---
description: GridGain 8.8.28 is a stability release dedicated to fixing vulnerabilities and improving usability, with no major new features.
hidden: true
---

# GridGain 8.8.28 Release Notes

GridGain 8.8.28 is a  stability release dedicated to fixing vulnerabilities and improving usability. No major new features are added in this release.

## New Features

### Improved Thin Client Endpoint Discovery

In this release, thin client discovery process was improved. A new `EnableClusterDiscovery` configuration property was added to Java and .NET thin clients. When this property is enabled, thin clients will discover all server nodes automatically and maintain a list of servers at all times. This makes it much easier to run thin clients in cloud environments or Kubernetes.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-36507 | Platforms & Thin Clients | .NET: Added IgniteClientConfiguration.EnableClusterDiscovery configuration property that can be used to enable or disable discovery. |
| GG-36503 | Platforms & Thin Clients | Java thin: Initial connection and SSL handshake process now respects the configured timeout. |
| GG-36494 | Cluster SQL Engine | DB2 did not work as external storage for writing if table had several columns in primary key. |
| GG-36493 | Cluster Storage Engine | Transaction records are no longer logged to WAL if no persistent caches participate in the transaction. |
| GG-36488 | Cluster Security | Updated org.apache.rat library from 0.12 to 0.14. |
| GG-36472 | Platforms & Thin Clients | Java thin: Added ClientConfiguration.clusterDiscoveryEnabled configuration property that can be used to enable or disable discovery. |
| GG-36467 | Cluster SQL Engine | Fixed a rare concurrency exception that happened during SQL index scan. |
| GG-36435 | Cluster Storage Engine | Fixed a possible exception during SQL index defragmentation if query parallelism is more than 1. |
| GG-36413 | Cluster Storage Engine | Fixed a rare issue caused by restarting of a node after a checkpoint without first rebuilding indexes. |
| GG-36347 | Cluster SQL Engine | Fixed an issue that caused degraded performance for SQL GROUP BY queries. |
| GG-36301 | Platforms & Thin Clients | Java thin client: Fixed a potential pending requests race condition on close. |
| GG-36242 | Platforms & Thin Clients | Java thin: Added endpoints discovery feature. |
| GG-36231 | Cluster Storage Engine | Added a way to change checkpoint frequency at runtime. |
| GG-36202 | Cluster SQL Engine | It is no longer possible  to create caches with the same index and schema names when using key-value api. |
| GG-35464 | Cluster Security | Added IP address of thin clients to AuthenticationEvent log output. |
| GG-33516 | Cluster Control Script | Added --all mode to reset lost partition command. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-36485 | Cluster Security | Updated Spring version from 5.2.22.RELEASE to 5.2.23.RELEASE. |
| GG-35595 | Cluster Data Replication | Improved data center replication performance during batching process. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-36311 | Cluster Data Snapshots and Recovery | Snapshot no longer fails if the hard drive runs out of space during snapshot compression process. Data that did not fit  on the drive during compression will be left uncompressed. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.29-p1`, `8.7.42-p2`, `8.8.2-p1`, `8.8.4-p2`, `8.8.8-p1`, `8.8.9-p1`, `8.8.13-p2`, `8.8.16-p2`, `8.8.18-p1`, `8.7.22`, `8.7.28`, `8.7.32`, `8.7.34`, `8.7.38`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.9`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`, `8.8.14`, `8.8.15`, `8.8.16`, `8.8.17`, `8.8.18`, `8.8.19`, `8.8.20`, `8.8.21`, `8.8.22`, `8.8.23`, `8.8.23-p1`, `8.8.24`, `8.8.25`, `8.8.25-p1`, `8.8.26`, `8.8.27`

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
Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
