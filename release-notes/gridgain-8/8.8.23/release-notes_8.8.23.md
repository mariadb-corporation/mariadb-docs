---
description: GridGain 8.8.23 adds Java 17 support, thin client and metrics improvements, and a cache destroy control script command, along with many fixes.
hidden: true
---

# GridGain 8.8.23 Release Notes

## New Features

### Java 17 Support

You can now use Java 17 to run GridGain. Due to changes in Java configuration parameters, you may need to change your JVM configuration. For more information on Java configuration, see [GridGain Quick Start Guide for Java](https://www.gridgain.com/docs/gridgain8/latest/getting-started/quick-start/java)

#### Known Issues

### Java 17 Security Issues

Launching GridGain on Java 17 may cause issues on nodes with the Security plugin enabled. This is a known issue that will be fixed in the upcoming release.

### Complex SQL Operation With IN Operator Working Incorrectly
In GridGain 8.8.23, complex SQL operations that evaluate index key prefix and index key suffix in the same operation will return duplicate values for non-aggregate functions, or incorrect values for aggregate functions. Here is the example of the condition that can trigger the issue for index with `a, b, c` columns:
```
a=X AND c in (Y, Z)
```
If you use similar conditions in your environment, avoid updating to GridGain 8.8.23. An emergency 8.8.25-p1 patch release is scheduled soon.
If you already use it and encounter the issue, update to [GridGain 8.8.25-p1](../8.8.25/release-notes_8.8.25-p1.md) version as soon as possible to fix the issue.

### Thin Client Improvements

A number of new features were added to thin clients:

- Logging is now supported in Java Thin Client.
- .NET clients now use a standardized approach to [Services](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/services/services).
- A way to get service call context was added to.NET thin clients.

### More Metrics Improvements

As part of continued push to improve metric accuracy and coverage, a number of metric improvements were done in this release:

- `PagesFillFactor` metric accuracy improved.
- `TotalUsedPages` metric is now available through other metric sources (not only JMX).
- `TotalUsedSize` metric was introduced. It provides information on the amount of memory occupied by `TotalUsedPages` metric.
- `SizeUsedByData` metric was introduced. It displays the amount of memory occupied by user and system data.

### Cache Destroy Command Added

A new `destroy` command was added to the control script. Here is a simple example of how you can destroy a cache:

```
control.sh --cache destroy --caches sampleCache
```

### Snapshot Catalog Feature Removed

Snapshot tool catalog support was removed from GridGain. This removes the requirement to include related libraries and closes related vulnerabilities.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35878 | Cluster SQL Engine | Fixed issues with ordered requests if CacheConfiguration#queryParallelism was different from default. |
| GG-35833 | Cluster Metrics & Monitoring | Fixed an issue that could lead to incorrect cache metrics calculation after re-activation a cluster |
| GG-35817 | Platforms & Thin Clients | .NET: Added support for default interface methods to Services. |
| GG-35789 | Cluster Metrics & Monitoring | Added new JMX attribute that allows to read current cluster state |
| GG-35765 | Cluster SQL Engine | Fixed a possible issue with a cluster when SQL statistic state update comes to a deadlock. |
| GG-35764 | Platforms & Thin Clients | Java thin: Fixed exception handling for RetryPolicy#shouldRetry call. |
| GG-35762 | Cluster Metrics & Monitoring | Multiple metrics improvements. |
| GG-35730 | Cluster SQL Engine | Sql engine not using the index from hint for queries containing `group by` statement. |
| GG-35715 | Cluster Control Script | Added missing "--add-opens" for Java 15+ runtime. |
| GG-35712 | Cluster Communication | Fixed thread pool starvation during the binary metadata and marshaller mapping propagation for the client node |
| GG-35709 | Cluster SQL Engine | Fixed JDBC thin client ignoring the timeout configuration for initial connection. |
| GG-35705 | Platforms & Thin Clients | Thin clients: Fixed propagation of a service call exception stacktrace to the client side. |
| GG-35703 | Cluster Storage Engine | Fixed wrong checkpoint lock count calculation during checkpointing process. |
| GG-35697 | Cluster Machine Learning Engine | Updated hadoop-common from 2.9.2 to 3.3.2 to fix CWE-611. |
| GG-35682 | Cluster SQL Engine | Improved index usage by H2 IN operator in case of simple multi-column conditions. |
| GG-35627 | Cluster SQL Engine | SQL: Fixed the issue when a commented line of multi-statement query produced an extra empty resultset. |
| GG-35619 | Cluster Communication | Fixed a rare node crash due to CancelledKeyException. |
| GG-35532 | Platforms & Thin Clients | Java thin: Added logging. |
| GG-35521 | Cluster Storage Engine | Fixed an issue that could lead to data corruption of atomic cache when a new updated entry is greater than WAL buffer size. |
| GG-35335 | Cluster SQL Engine | Fixed incorrect type conversion for index scans (for example, when indexed field has string data type and search row has numeric data type). |
| GG-34938 | Platforms & Thin Clients | .NET: Added service call context. |
| GG-34937 | Platforms & Thin Clients | Java thick: Added service request attributes |
| GG-34027 | Cluster Control Script | Added a new command that allows to destroy a cache by using the control script. |
| GG-33629 | Cluster SQL Engine | Fixed JDBC not closing a connection after cache.invoke() over write-behind enabled cache. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35821 | General | Update multiple jackson modules to fix CVE-2022-42003 and CVE-2022-42004. |
| GG-35662 | Control Center Agent | Fixed Control Center Agent collecting extra logs. |
| GG-35235 | GridGain Integrations | Added an option for kafka source connector to be able to handle entry expiration events. |
| GG-35231 | Cluster Rolling Upgrade | Removed spring-jcl dependency to improve logging during rolling upgrade. |
| GG-34960 | Cluster Storage Engine | Fixed an issue when a node that did not own any partitions was stopped during a rebalance. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35588 | Cluster Data Snapshots and Recovery | Removed Snapshot Catalog feature. |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35891 | Control Center Agent | Fixed Control Center displaying incorrect cluster status after enabling the Control Center agent. |
| GG-35756 | Control Center Agent | Fixed a possible null pointer exception on coordinator node change. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.29-p1`, `8.7.42-p2`, `8.8.2-p1`, `8.8.4-p2`, `8.8.8-p1`, `8.8.9-p1`, `8.8.13-p2`, `8.8.16-p2`, `8.8.18-p1`, `8.7.22`, `8.7.28`, `8.7.32`, `8.7.34`, `8.7.38`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.9`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`, `8.8.14`, `8.8.15`, `8.8.16`, `8.8.17`, `8.8.18`, `8.8.19`, `8.8.20`, `8.8.21`, `8.8.22`

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.7.2`, `2.11.0`, `2.12.0`, `2.13.0`

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
