---
description: GridGain 8.8.20 is dedicated to fixing issues and improving stability, with continued new thin client features.
hidden: true
---

# GridGain 8.8.20 Release Notes

GridGain 8.8.20 is dedicated to fixing issues and improving stability, including fixes to `IGNITE_LOCAL_HOST` property interaction. Our thin client team continues to bring new features to thin clients.

## New Features

### Java Thin: Changed Retrieve Binary Configuration Behavior

Java thin client now retrieves binary configuration from cluster. Name mapper and compact footer settings are set according to cluster configuration. To disable this behavior, set the `ClientConfiguration#autoBinaryConfigurationEnabled` property to `false`.

## Known Issues

### Crash With Older ODBC Protocol Versions on Linux

When using older ODBC protocol versions to connect to a GridGain 8.8.20 node on Linux, the driver may crash. We recommend using the default version configured in the driver instead.
This issue will be fixed in the upcoming release.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35455 | Cluster Storage Engine | Fixed GridGain not running long running background tasks after joining a node after activating the cluster. |
| GG-35453 | Cluster SQL Engine | Failure handler will be called if sql parsing engine is down. |
| GG-35398 | Cluster Discovery | Host names will not be resolved if IGNITE_LOCAL_HOST property is defined. |
| GG-35383 | Cluster Communication | Sped up OptimizedMarshaller. |
| GG-35349 | Platforms & Thin Clients | .NET: Improved Java detection on Linux. |
| GG-35343 | Cluster Storage Engine | Improved speed-based write throttling for cases when dirty pages ratio is low. |
| GG-35339 | Cluster Communication | Fixed race condition which occurs when closing a connection and opening a new connection at the same time. |
| GG-35301 | Cluster SQL Engine | Fixed setting INLINE_SIZE manually affecting types with a fixed length. |
| GG-35281 | Platforms & Thin Clients | .NET thin: Added AtomicLong. |
| GG-35273 | GridGain Integrations | Fixed CVE-2021-22573. |
| GG-35195 | Diagnostics and Failure Handling | Lowered logging level of error messages for situations when some messages could not be sent to a client that left the topology. |
| GG-35170 | Platforms & Thin Clients | Java thin: Added IgniteSet. |
| GG-35168 | Platforms & Thin Clients | Fixed an issue that caused errors on thin clients when using user name or password larger than ~64KB. |
| GG-35038 | Cluster Storage Engine | Fixed possible partition divergency after SQL DELETE happens during rebalance. |
| GG-35036 | Platforms & Thin Clients | C++ thin: SqlFieldsQuery now supports setting a partition. |
| GG-34941 | Platforms & Thin Clients | ODBC: Fix linking failure on Linux when trying to use DSN with a driver that was built with CMake. |
| GG-34911 | Platforms & Thin Clients | .NET: Fixed platform service with node filter cancellation on joining pure java node. |
| GG-34382 | Platforms & Thin Clients | Java thin: Added automatic binary configuration. Name mapper and compact footer settings will be set according to cluster configuration. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35407 | Cluster Data Replication | Added automatic rebuild of corrupted DR index in maintenance mode. |
| GG-35362 | Cluster Data Replication | Fixed incremental active-active data replication erroneously replicating entries back to DC where they have been replicated from. |
| GG-35334 | GridGain Integrations | Fixed CVE-2020-36518. |
| GG-35317 | Cluster Storage Engine | Fixed an issue that could lead to full rebalance of cache instead of historical in case of using the TDE feature. |
| GG-35289 | Cluster Data Replication | Fixed DR running unneeded system cache scans on cluster activation. |
| GG-35250 | GridGain Integrations | Fixed a rare issue that caused a ClassNotFoundException when SQL table was replicated and BACKLOG policy was enabled. |
| GG-35013 | Cluster Data Replication | Fixed inconsistent DR methods when both incremental DR and NearCache were enabled. |
| GG-31900 | Cluster Data Replication | Added a separate property to configure incremental state transfer pool. |
| GG-30859 | Cluster Data Replication | Fixed full garbage collection happening too often on DR sender nodes. |
| GG-29420 | Cluster Data Replication | Fixed a compatibility issue in DR when a node of old version may fail during RU. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35409 | Cluster Data Snapshots and Recovery | Fixed an issue with snapshot security digest when cache is encrypted. |
| GG-35341 | Cluster Data Snapshots and Recovery | Fixed an issue with post-processing of snapshot partitions. |
| GG-35291 | Cluster Data Snapshots and Recovery | Eliminated a race condition between the checkpointer and the snapshot manager that could potentially cause broken snapshots. |
| GG-35236 | Cluster Snapshot Utility | Lowered logging level on server nodes for validation exceptions produced by snapshot-utility commands. |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35421 | Control Center Agent | Changed date representation for query results. |
| GG-35215 | Control Center Agent | Made it possible to remove the last configured Maven repository. |
| GG-35214 | Control Center Agent | Implemented a way to update artifact dependencies of a deployment unit draft. |
| GG-35212 | Control Center Agent | Implemented clone, and clone and deploy deployment unit actions. |
| GG-35200 | Control Center Agent | Implemented update of deployment unit artifacts on node join. |
| GG-35199 | Control Center Agent | Implemented an endpoint to delete outdated deployment unit versions. |
| GG-35198 | Control Center Agent | Added a way to create a code deployment draft. |
| GG-34673 | Control Center Agent | A failed deployment unit now keeps its state when a deployment unit of the next version is successfully deployed. |
| GG-34652 | Control Center Agent | Enabled code deployment functionality for Control Center Agent by default. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.29-p1`, `8.7.42-p2`, `8.8.2-p1`, `8.8.4-p2`, `8.8.8-p1`, `8.8.9-p1`, `8.8.13-p2`, `8.8.16-p2`, `8.8.18-p1`, `8.7.22`, `8.7.28`, `8.7.32`, `8.7.34`, `8.7.38`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.9`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`, `8.8.14`, `8.8.15`, `8.8.16`, `8.8.17`, `8.8.18`, `8.8.19`

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
Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
