---
description: GridGain 8.8.25 is a stability release dedicated to fixing issues, with no major new features.
hidden: true
---

# GridGain 8.8.25 Release Notes

GridGain 8.8.25 is a stability release dedicated to fixing issues. No major new features are added in this release.

## Known Issues

### Complex SQL Operation With IN Operator Working Incorrectly

In GridGain 8.8.25, complex SQL operations that evaluate index key prefix and index key suffix in the same operation will return duplicate values for non-aggregate functions, or incorrect values for aggregate functions. Here is the example of the condition that can trigger the issue for index with `a, b, c` columns:
```
a=X AND c in (Y, Z)
```
If you use similar conditions in your environment, avoid updating to GridGain 8.8.25. A fix is available in release [GridGain 8.8.25-p1](../8.8.25/release-notes_8.8.25-p1.md).

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-36209 | Cluster Storage Engine | Fixed a rare case that could lead to a deadlock on partition map exchange in case of using transactions and Ignite Native Persistence. |
| GG-36199 | Cluster Storage Engine | Fixed a rare case when joining a thick client to a cluster could hang on the initial partition map exchange. |
| GG-36161 | Cluster Storage Engine | Added logging to direct io to track if read byte count is not equal to requested byte count. |
| GG-36127 | Cluster Metrics & Monitoring | Rejection timeout metric no longer increments when the session is declined due to incorrect authentication. |
| GG-36123 | Platforms & Thin Clients | .NET: Fixed platform cache invalidation on client nodes with near cache. |
| GG-36030 | Cluster Storage Engine | Fixed a rare issue with defragmentation when Direct IO was enabled. |
| GG-36024 | Cluster Storage Engine | Fixed NPE when getting transaction metricks. |
| GG-36023 | Cluster SQL Engine | Removed a mistaken error message when tracking free memory after closing a large result set. |
| GG-35987 | Cluster Storage Engine | Improved logging for caches where the 'index.bin' file was removed. |
| GG-35959 | Cluster Metrics & Monitoring | Fixed an issue that could happen on stopping a thin client and could lead to internal background processes net being stopped. |
| GG-35895 | Diagnostics and Failure Handling | Fixed network issues that caused ClosedChannelException and NullPointerException. |
| GG-35708 | Cluster Storage Engine | Fixed a rare case when a node failed to start. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-36195 | Cluster Data Replication | Fixed an issue when data center replication was stopped after restoring a snapshot over existed cache. |
| GG-36171 | Cluster Security | Fixed issues that could happen when some control.sh commands were executed with security enabled. |
| GG-36159 | Cluster Security | Fixed issues that could happen during data center replication with security enabled. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35870 | Cluster Data Snapshots and Recovery | Fixed GridGain occasionally using wrong strategy calculation for snapshot check/restore. |
| GG-35864 | Cluster Data Snapshots and Recovery | Improved resource utilization of long-running full snapshots. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.29-p1`, `8.7.42-p2`, `8.8.2-p1`, `8.8.4-p2`, `8.8.8-p1`, `8.8.9-p1`, `8.8.13-p2`, `8.8.16-p2`, `8.8.18-p1`, `8.7.22`, `8.7.28`, `8.7.32`, `8.7.34`, `8.7.38`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.9`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`, `8.8.14`, `8.8.15`, `8.8.16`, `8.8.17`, `8.8.18`, `8.8.19`, `8.8.20`, `8.8.21`, `8.8.22`, `8.8.23`, `8.8.23-p1`, `8.8.24`

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

#### .NET: GridGain Nuget Package Misses GridGain.Ignite Jars in 8.8.17

Set `<PrivateAssets>None</PrivateAssets>` for the `GridGain.Ignite` dependency in GridGain project, so that jars from there are included.

#### .NET: Docker Images Need Additional Configuration

To run .NET SDK commands, install the .NET SDK. For more details, click [here](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=net60#dependencies).

## We Value Your Feedback
Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
