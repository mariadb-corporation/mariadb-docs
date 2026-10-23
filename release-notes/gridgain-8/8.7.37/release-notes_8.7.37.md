---
description: >-
  GridGain 8.7.37 adds data streaming to the .NET thin client, extends the .NET
  streaming API, and delivers improvements and fixed issues across the Community,
  Enterprise, and Ultimate editions.
hidden: true
---

# GridGain 8.7.37 Release Notes

## New Features

GridGain 8.7.37 provides access to a number of improvements and bug fixes.

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

### -XX:+DisableExplicitGC JVM option no Longer Recommended

Due to improvements in GridGain 8.7.37 it is no longer recommended to use `-XX:+DisableExplicitGC` JVM option. Using this option no longer provides any benefits and can cause the heap to no longer be reclaimed.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33315 | Distributed Data Structures | Added more messages to DEBUG logs of data structures. |
| GG-33312 | Platforms & Thin Clients | Thin clients: enable partition awareness by default (Java, .NET, C++). |
| GG-33309 | Cluster SQL Engine | Fixed an issue when a node restart during index rebuild caused errors or index corruption. |
| GG-33302 | Platforms & Thin Clients | .NET: Added thin client DataStreamer API. |
| GG-33282 | Cluster Storage Engine | Fixed an issue when multiple checkpoints in a single WAL segment could lead to incorrect WAL reservation. |
| GG-33280 | Platforms & Thin Clients | .NET: Improved DataStreamer API - added FlushAsync, deprecated and replaced confusing methods and properties, fixed resource cleanup. |
| GG-33273 | Cluster SQL Engine | SqlOffloadingEnabled setting is now correctly logged. |
| GG-33254 | Cluster SQL Engine | Improved performance of SQL queries that use DISTINCT expression. |
| GG-33229 | Cluster Rolling Upgrade | Fixed possible deadlock in concurrent cache data store initialization, exchange initialization and start of checkpoint. |
| GG-33209 | Cluster Storage Engine | Prevents restoration of partially committed transactions. |
| GG-33173 | Cluster Discovery | Improved local node discovery and default configuration on z/OS. |
| GG-33018 | Cluster Storage Engine | Fixed AssertionError that could happen on the first checkpoint after a node start. |
| GG-32362 | Cluster Continuous Queries | Fixed an issue where exception in static initializer during remote filter deployment could lead to the server node failure. |
| GG-31060 | GridGain Integrations | Fixed an error during Cassandra Cache Store initialization. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33276 | Control Center Agent | Running SQL queries from Control Center no longer requires superfluous ADMIN_OPS permission. |
| GG-33190 | Cluster Storage Engine | Fixed data corruption in GG Ultimate Edition when TDE-enabled caches are used. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33311 | Cluster Snapshot Utility | Fixed a compatibility issue between GridGain 8.8.5 or later and GridGain 8.7.36. |
| GG-33278 | Cluster Data Snapshots and Recovery | Fixed an error when a client node with no snapshot configuration could not issue snapshot commands. |
| GG-30850 | Cluster Data Snapshots and Recovery | Multithreaded check and restoration of snapshot. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.2-p15`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.26-p1`, `8.7.27`, `8.7.27-p1`, `8.7.28`, `8.7.29`, `8.7.30`, `8.7.31`, `8.7.32`, `8.7.33`, `8.7.33-p2`, `8.7.34`, `8.7.35`, `8.7.36`, `8.8.3`, `8.8.4`, `8.8.5`

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
