---
description: GridGain 8.8.19 adds DR diagnostic and partition repair tools and scan query support for the C++ and C# thin clients, along with numerous fixes across all editions.
hidden: true
---

# GridGain 8.8.19 Release Notes

## New Features

### DR Diagnostic Tool

A new option was added to control script. With it, you can check if all partition counters are in order.

```
control.sh --dr check-partition-counters [--caches cache1,cache2]
```

### Partition Repair Tool for DR

A new option was added to control script. With it, you can repair partition counters for specific caches during data center replication.

```
control.sh --dr repair-partition-counters [--caches cache1,cache2]
```

### ScanQuery for C++ and C# Thin Clients

You can now perform [scan queries](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/key-value-api/using-scan-queries) from both C++ and C# thin clients.

{% code title="C++" %}
```cpp
using namespace ignite::cache;
using namespace ignite::cache::query;

CacheClient myCache = client.GetCache<int32_t, std::string>("myCache");

ScanQuery qry;
QueryCursor<int32_t, std::string> cursor = myCache.Query(qry);

while (cursor.HasNext())
{
	CacheEntry<int32_t, std::string> entry = cursor.GetNext();

	std::cout << entry.GetKey() << ": " << entry.GetValue() << std::endl;
}
```
{% endcode %}

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35290 | Platforms & Thin Clients | C++ thin: Implemented ScanQuery. |
| GG-35243 | Platforms & Thin Clients | .NET: Fixed net461 release binaries. |
| GG-35239 | Platforms & Thin Clients | Java thin: Added AtomicLong. |
| GG-35102 | Platforms & Thin Clients | .NET: Improved debug logging when locating JVM. |
| GG-35051 | Cluster SQL Engine | Fixed some requests causing an exception when sql tracing is enabled. |
| GG-35037 | Platforms & Thin Clients | C++ thin: Implemented ScanQuery. |
| GG-35027 | Cluster Discovery | Changed log level of "Failed to initialize connection" message from ERROR to WARN. |
| GG-34907 | Cluster Compute Grid | Removed the "Failed to execute job due to unexpected runtime exception" error from log. |
| GG-34906 | Cluster Communication | Changed log level of "Connection reset by peer" message from ERROR to WARN. |
| GG-34880 | GridGain Integrations | Fixed the following CVEs: CVE-2021-40110, CVE-2021-38542, CVE-2021-40111, CVE-2021-40525. |
| GG-34879 | GridGain Integrations | Fixed the following CVEs: CVE-2008-7271 and CVE-2010-4647. |
| GG-34878 | GridGain Integrations | Fixed the following CVEs: CVE-2015-5191, CVE-2014-4200, CVE-2014-4199, CVE-2016-7080, CVE-2016-5328. |
| GG-34877 | GridGain Integrations | Fixed CVE-2020-8897. |
| GG-34737 | Cluster Metrics & Monitoring | Added the LifecycleAware support for local event listeners. |
| GG-34615 | Binary Objects | Fixed a rare issue with SQL Insert operation. |
| GG-33770 | Cluster Storage Engine | Added automatic rebuild of corrupted indexes in maintenance mode. |
| GG-33647 | Cluster Storage Engine | Added new sys variable IGNITE_PARTITION_RELEASE_FUTURE_WARN_LIMIT that allows to reduce a number diagnostic messages. |
| GG-32939 | Platforms & Thin Clients | ODBC: Fixed an issue when the same Date/Time value put on nodes in different timezones resulted in different actual values on servers. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35180 | GridGain Integrations | Updated jackson-databind to fix CVE-2020-36518. |
| GG-35104 | Cluster SQL Engine | Fixed DR schema registration when DrReceiverConfiguration#setLazyBinaryMetadataRegistration is true. |
| GG-35090 | Cluster SQL Engine | Fixed DR Conflict Resolver being occasionally called before the cache was initialized. |
| GG-35088 | Cluster Compute Grid | Deferred interruption of a compute task after it has been cancelled. |
| GG-35080 | Cluster Rolling Upgrade | The default value of the "rollingUpdatesEnabled" property changed to "true". |
| GG-34990 | Cluster Data Replication | Fixed an issue causing an assertion to be thrown in case of cross replication with incremental DR enabled |
| GG-34981 | Cluster Data Replication | Added partition repair tool for DR to control.sh. |
| GG-34968 | Cluster Data Replication | Added partition diagnostic tool for DR to control.sh. |
| GG-34900 | Cluster Data Replication | Fixed a rare issue in DR related to frequent cache destroy operations. |
| GG-34893 | Cluster SQL Engine | Made H2Tree comparator capable to change comparing algorithm according to index creation version. |
| GG-34717 | Cluster Data Replication | Removed unnececcary errors from logs during DR process. |
| GG-32676 | Cluster Data Replication | Improved binary schema registration logic in DR. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35282 | Cluster Data Snapshots and Recovery | Fixed calculation of progress for snasphots with compression. |
| GG-35169 | Cluster Data Snapshots and Recovery | Snapshot files compression is now started after at least one partition file is stored on disk. |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35143 | Control Center Agent | Fixed shading of Spring for CC agent. |
| GG-32980 | Control Center Agent | Changed output format for status command in management script. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.29-p1`, `8.7.42-p2`, `8.8.2-p1`, `8.8.4-p2`, `8.8.8-p1`, `8.8.9-p1`, `8.8.13-p1`, `8.8.16-p2`, `8.7.22`, `8.7.28`, `8.7.32`, `8.7.34`, `8.7.38`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.9`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`, `8.8.14`, `8.8.15`, `8.8.16`, `8.8.17`, `8.8.18`

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
