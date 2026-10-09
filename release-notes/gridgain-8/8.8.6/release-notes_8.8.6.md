---
description: >-
  GridGain 8.8.6 adds data streaming and an extended streaming API to the .NET thin client.
hidden: true
---

# GridGain 8.8.6 Release Notes

## New Features

### .NET Thin Client Supports Data Streaming

Data streaming was added to .NET thin client. You can now use it in your thin clients in the same way you use it in [normal client](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/data-streaming).

### .NET Streaming API Extended

Data streaming API for .NET client was extended:

- `AddData` and `RemoveData` methods were deprecated.
- `void Add` and `void Remove` methods were added and should be used instead.
- The new `BatchTask` property was added. You can use it to get the task for the current batch.

```csharp
using System;
using System.Threading.Tasks;
using Apache.Ignite.Core;
namespace IgniteNewDataStreamerApi
{
    class Program
    {
        static async Task Main(string[] args)
        {
            using var ignite = Ignition.Start();
            var cache = ignite.CreateCache<int, string>("my-cache");
            using var streamer = ignite.GetDataStreamer<int, string>(cache.Name);
            streamer.AllowOverwrite = true;
            streamer.Add(1, "Hello");
            streamer.Add(2, "World");
            streamer.Remove(3);
            await streamer.FlushAsync();
            Console.WriteLine(streamer.GetCurrentBatchTask().Status);
        }
    }
}
```

### Gzip Data Compression Now Supports Snapshots

With this release you can use gzip data compression to create caches for nodes with snapshots. You can also disable dictionaries for ZSTD compression with `dictionaryRequired=false dictionarySize=0` to work with snapshots, but using gzip is recommended.

### -XX:+DisableExplicitGC JVM option no Longer Recommended

Due to improvements in GridGain 8.8.6 it is no longer recommended to use `-XX:+DisableExplicitGC` JVM option. Using this option no longer provides any benefits and can cause the heap to no longer be reclaimed.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33301 | Platforms & Thin Clients | .NET: Added thin client DataStreamer API. |
| GG-33288 | Platforms & Thin Clients | Thin clients: enable partition awareness by default (Java, .NET, C++). |
| GG-33274 | Cluster Storage Engine | Fixed an issue when multiple checkpoints in a single WAL segment could lead to incorrect WAL reservation. |
| GG-33258 | Cluster SQL Engine | SqlOffloadingEnabled setting is now correctly logged. |
| GG-33232 | Cluster SQL Engine | Improved performance of SQL queries that use DISTINCT expression. |
| GG-33213 | Platforms & Thin Clients | ODBC now works with GUID data type on Windows. |
| GG-33174 | Cluster SQL Engine | Added parameters to ANALYZE command to manually override statistics. Added manually overridden values to statistics_configuration system view. |
| GG-33157 | Platforms & Thin Clients | .NET: Improved DataStreamer API - added FlushAsync, deprecated and replaced confusing methods and properties, fixed resource cleanup. |
| GG-33148 | Cluster Discovery | Improved local node discovery and default configuration on z/OS. |
| GG-33139 | Distributed Data Structures | Added more messages to DEBUG logs of data structures. |
| GG-32624 | Cluster Storage Engine | Fixed AssertionError that could happen on the first checkpoint after a node start. |
| GG-28934 | GridGain Integrations | Error during Cassandra Cache Store initialization was fixed. |
| GG-28295 | Cluster SQL Engine | Fixed an issue when a node restart during index rebuild caused errors or index corruption. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33357 | Cluster Data Replication | Fixed an issue when incremental state transfer future could never be completed. |
| GG-33267 | Cluster Data Replication | Fixed AssertionError during cluster rolling restart when DR is enabled. |
| GG-33262 | Cluster Rolling Upgrade | Fixed "Authorization failed" error when the rolling upgrade was started on a cluster with security enabled. |
| GG-33220 | Cluster Data Replication | Fixed memory consumption when Data center replication is enabled and a network issue between the data centers occurs. |
| GG-33178 | Cluster Storage Engine | Fixed data corruption in GG Ultimate Edition when TDE-enabled caches are used. |
| GG-33160 | Cluster Storage Engine | It is now possible to use snapshots together with data compression that uses Gzip or Zstandard without dictionary. |
| GG-33112 | Cluster Metrics & Monitoring | Added new metrics for monitoring the number of memory pages related to SQL indexes. These metrics can be made available through JMX and viewed as part of data region and cache group properties under the `InMemoryIndexPages` name. |
| GG-33008 | Control Center Agent | Running SQL queries from Control Center no longer requires superfluous ADMIN_OPS permission. |
| GG-30986 | Binary Objects | Added gzip-based data compression feature. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32764 | Cluster Data Snapshots and Recovery | Optimized snapshots restoration from shared network folders. |
| GG-30981 | Cluster Snapshot Utility | Snapshot-utility.sh commands (move, check, delete) now log on INFO level instead of WARN. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.2-p15`, `8.7.3`, `8.7.33-p2`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`,
`8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.26-p1`, `8.7.27`, `8.7.27-p1`, `8.7.28`, `8.7.29`, `8.7.29-p1`,
`8.7.30`, `8.7.31`, `8.7.32`, `8.7.33`, `8.7.34`, `8.7.35`, `8.7.36`, `8.7.5-p1`,  `8.7.6-p1`,
`8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`

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

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
