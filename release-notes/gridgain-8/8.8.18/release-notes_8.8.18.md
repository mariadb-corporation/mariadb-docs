---
description: >-
  GridGain 8.8.18 moves DR metrics to a common metrics manager, adds a control script
  command to read an arbitrary metric, updates Spring, and includes many fixes.
hidden: true
---

# GridGain 8.8.18 Release Notes

## New Features

### DR Metrics Use a Common Manager

DR metrics were moved to a common Ignite metrics manager. To get DR [JMX metrics](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/monitoring-metrics/metrics), set a metric exporter:

```java
cfg.setMetricExporterSpi(new JmxMetricExporterSpi());
```

For example, you can publish metrics to the log in the following way:

```java
LogExporterSpi logExport = new LogExporterSpi();
logExport.setPeriod(5000);
logExport.setExportFilter(reg -> reg.name().startsWith("dr"));
ignCfg.setMetricExporterSpi(logExport);
```

### A New Command to Get Arbitrary Metric

A new `--metric` command was added to the [Control Script](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/control-script). With this command, you can get an arbitrary [metric](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/monitoring-metrics/generic-metrics) from a node of your choice:

{% tabs %}
{% tab title="Unix" %}
```shell
control.sh --metric [--node-id mynode] CpuLoad
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --metric [--node-id mynode] CpuLoad
```
{% endtab %}
{% endtabs %}

### Spring Framework Update

Spring framework was updated to version 5.2.21. This update fixes a number of security vulnerabilities. Older Spring Data integrations (1.x and 2.0) are no longer compatible with new GridGain versions.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35076 | Cluster Compute Grid | Fixed an issue with potential node failure during cancelling of compute jobs with cache operations. |
| GG-35012 | Cluster SQL Engine | Added a warning about possible data inconsistency for remove operations. |
| GG-34971 | Platforms & Thin Clients | .NET: Fixed EntryPointNotFoundException on Alpine Linux. |
| GG-34962 | Platforms & Thin Clients | C++ thin: Added user threadpool size option to public configuration that allows controlling number of threads used by client. |
| GG-34903 | Platforms & Thin Clients | .NET: Fixed missing binary schema when field is removed from a type. |
| GG-34902 | Platforms & Thin Clients | .NET: Added ThinClientConfiguration.SendServerExceptionStackTraceToClient. |
| GG-34892 | Cluster SQL Engine | Index data will now be cleared before rebuilding. |
| GG-34882 | Cluster Compute Grid | Fixed a rare node crash due to peer class-loading issue. |
| GG-34872 | Platforms & Thin Clients | Java Thin: Added periodic heartbeat messages to improve connection reliability. |
| GG-34757 | Platforms & Thin Clients | .NET Thin: Added periodic heartbeat messages to improve connection reliability. |
| GG-34735 | Platforms & Thin Clients | Thin client: Added an option to append server exception stack trace to the error messages. |
| GG-34725 | Cluster Storage Engine | Fixed an issue that led to errors in the discovery thread and cluster instability. |
| GG-34306 | Cluster Storage Engine | Fixed an issue with clearing tombstones. |
| GG-34268 | Cluster Security | Fixed a security issue on thin clients. |
| GG-33982 | Distributed Data Structures | Fixed an issue that caused data structures view to be unavailable on the cluster with Ignite Native Persistence enabled. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35157 | GridGain Integrations | Updated Spring Data to fix CVE-2022-22965. |
| GG-35123 | Cluster Data Replication | DR metrics are now published via common Ignite metrics manager. |
| GG-35087 | GridGain Integrations | Upgraded Spring to version 5.2.21 to avoid CVE-2022-22965 and removed spring-data 1.x and 2.0 integrations. |
| GG-35034 | Cluster Security | Fixed an authorization issue in defragmentation tool. |
| GG-35028 | Cluster Data Replication | Fixed the issue when sender hub dropped connection to receiver under high load if the awaitAcknowledge property was set to false. |
| GG-35019 | Cluster Data Replication | Added a way to enable warning or error log messages instead of assertion errors. |
| GG-35010 | Cluster Data Replication | Added DR metric for rejected batches. |
| GG-35002 | Cluster Data Replication | Fixed an issue when full-state transfer could freeze in an incomplete state. |
| GG-35001 | Cluster Storage Engine | Fixed a possible deadlock on management pool on the clear cache operation. |
| GG-34999 | Cluster Data Replication | Prevent using remote senders if the local one is configured as preferred. |
| GG-34975 | Cluster Data Replication | Fixed an issue when data could not be replicated in background to remote clusters. |
| GG-34967 | Cluster Data Replication | Added a log message about lost tombstones. |
| GG-34963 | Platforms & Thin Clients | .NET: Fixed Docker image. |
| GG-34923 | Cluster Data Replication | Fixed a rare issue that could lead to a DR livelock when multiple caches were in one sender group. |
| GG-34916 | Cluster Data Replication | Fixed an issue related to tombstone TTL configuration. |
| GG-34901 | Cluster SQL Engine | Fixed an issue when sqlline.sh would print errors when running in Docker. |
| GG-34798 | Cluster Storage Engine | Fixed an issue that prevented 8.8.X nodes from joining 8.7.X cluster during the rolling upgrade with enabled transparent data encryption. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35032 | Cluster Data Snapshots and Recovery | Removed a confusing warning message on snapshot restore. |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34774 | Control Center Agent | Control Center Agent now uses management pool instead public for internal messaging. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version. You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

- 8.7.2-p15
- 8.7.3
- 8.7.4
- 8.7.5
- 8.7.5-p1
- 8.7.6
- 8.7.6-p1
- 8.7.7
- 8.7.8
- 8.7.9
- 8.7.10
- 8.7.11
- 8.7.12
- 8.7.13
- 8.7.14
- 8.7.15
- 8.7.16
- 8.7.17
- 8.7.18
- 8.7.19
- 8.7.19-p1
- 8.7.20
- 8.7.21
- 8.7.22
- 8.7.23
- 8.7.24
- 8.7.25
- 8.7.26
- 8.7.26-p1
- 8.7.27
- 8.7.27-p1
- 8.7.28
- 8.7.29
- 8.7.29-p1
- 8.7.30
- 8.7.31
- 8.7.32
- 8.7.33
- 8.7.33-p2
- 8.7.34
- 8.7.35
- 8.7.36
- 8.7.37
- 8.7.38
- 8.7.39
- 8.7.40
- 8.7.41
- 8.7.42
- 8.7.43
- 8.8.1
- 8.8.2
- 8.8.3
- 8.8.4
- 8.8.5
- 8.8.6
- 8.8.7
- 8.8.8
- 8.8.9
- 8.8.10
- 8.8.11
- 8.8.12
- 8.8.13
- 8.8.14
- 8.8.15
- 8.8.16

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

To workaround this issue, alter the Jetty configuration to use `org.eclipse.jetty.util.ssl.SslContextFactory$Server` or `org.eclipse.jetty.util.ssl.SslContextFactory$Client`. See the configuration example at the [Client Certificate Authentication](https://www.gridgain.com/docs/latest/administrators-guide/security/authentication#client-certificate-authentication) page.

#### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and Later

In GridGain 8.7.26, the default value of the property `IgniteConfiguration.rebalanceThreadPoolSize` changed from `1` to `min(4, number of CPU / 4)`. It may cause a compatibility issue under the following conditions:

- When a Rolling Upgrade is performed
- The upgrade is performed from 8.5.7 version (or earlier) to 8.5.x or from 8.7.3 (or earlier) to 8.7.x
- The server nodes have at least 8 CPU cores
- The nodes configuration does not have the property `IgniteConfiguration.rebalanceThreadPoolSize`, so the default value is used

In this case, an exception is thrown with an error message similar to the following:

```text
сlass org.apache.ignite.IgniteException: Rebalance configuration mismatch (fix configuration or set -DIGNITE_SKIP_CONFIGURATION_CONSISTENCY_CHECK=true system property).
Different values of such parameter may lead to rebalance process instability and hanging.  [rmtNodeId=5fc58fb7-209d-489a-8034-0127a81abed6, locRebalanceThreadPoolSize = 4, rmtRebalanceThreadPoolSize = 1]
```

To workaround this issue, change the configuration of the server nodes to `rebalanceThreadPoolSize=1` so that it matches the previous default configuration. For example:

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="rebalanceThreadPoolSize" value="1"/>

    <!-- The rest of the configuration goes here -->
</bean>
```

#### Jetty Doesn't Accept Incorrect Configuration in GridGain 8.7.31 and Later

In GridGain 8.7.31 Jetty was upgraded to 9.4.33. Starting that version, Jetty has more strict validation of the provided configuration files. Before that version, an incorrectly spelled property in the configuration file had no effect. Starting this version, errors in the configuration will lead to an error on start.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration for REST
- The custom configuration has errors in it

You will need to fix the custom Jetty configuration before upgrading.

#### `ignite.sh` No Longer Enables Remote JMX by Default in GridGain 8.7.31 and Later

Starting from 8.7.31 version, GridGain no longer attempts to automatically enable the remote JMX. Default settings are known to cause issues if customized (for example, secure the connection). Also, in most cases, remote JMX is not required since many tools use local JMX connections (not using TCP).

Your setup may be affected if:

- You start GridGain nodes via `ignite.sh` script
- You connect to GridGain nodes' JMX interface remotely over TCP using the default configuration

To continue using remote JMX, you need to manually specify the required JMX settings. Please see the example below. Note that you don't need remote JMX if you use a local connection, such as connecting JConsole to a GridGain process on the same host.

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
