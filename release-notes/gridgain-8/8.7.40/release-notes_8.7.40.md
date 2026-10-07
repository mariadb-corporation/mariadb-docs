---
description: >-
  GridGain 8.7.40 adds extended snapshot compression options and a new option to
  exclude caches from snapshot operations, along with a number of improvements and
  bug fixes.
hidden: true
---

# GridGain 8.7.40 Release Notes

GridGain 8.7.40 provides access to a number of improvements and bug fixes.

## New Features

### Extended Snapshot Compression Options

New options were added to the `-archive` option in the [snapshot management tool](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/snapshots/snapshots-management-tool). You can now select between ZIP, ZSTD, LZ4, and SNAPPY compression options, or disable compression completely with a `NONE` option. To set a new compression option:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh snapshot -type=full -caches=cache1,cache2 -dest={work_folder} -archive=ZSTD
```
{% endtab %}

{% tab title="Windows" %}
```shell
snapshot-utility.bat snapshot -type=full -caches=cache1,cache2 -dest={work_folder} -archive=ZSTD
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
These options are disabled on some systems (for example, z/OS) by default. If you want to use them, contact our support team for information on enabling these options safely.
{% endhint %}

### New Option to Exclude Caches from Operation

A new `excluded_caches` option was added to the snapshot [snapshot management tool](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/snapshots/snapshots-management-tool). You can use it to exclude specific caches from the snapshot.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh snapshot -type=full -excluded_caches=cache1 -dest={work_folder}
```
{% endtab %}

{% tab title="Windows" %}
```shell
snapshot-utility.bat snapshot -type=full -excluded_caches=cache1 -dest={work_folder}
```
{% endtab %}
{% endtabs %}

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-34302 | Cluster Deployment | Fixed a bug with cluster crashing if a class with higher bytecode version was received from the client |
| GG-34296 | Cluster SQL Engine | Fixed an issue with comparing indexed fields with values that have different types. |
| GG-34291 | Control Center Agent | Increased security in management script command outputs. |
| GG-34287 | GridGain Integrations | Updated Cassandra module to fix a CVE. |
| GG-34260 | Platforms & Thin Clients | .NET: Fixed potential cache startup error when one of the loaded assemblies has certain compiler-generated type names that can't be parsed by Ignite. |
| GG-34254 | Platforms & Thin Clients | .NET: Fixed thin client streamer not creating SQL table entries. |
| GG-34252 | Platforms & Thin Clients | .NET: Fixed NullReferenceException in thin client due to late logger setter. |
| GG-34249 | Platforms & Thin Clients | .NET: Fixed thin client SslStreamFactory to allow SSL connection without client-side certificate. |
| GG-34226 | Distributed Data Structures | Fixed potential data corruption during rapid delete and update operations. |
| GG-34223 | Platforms & Thin Clients | Java thin: Fixed connection logic to follow user-defined endpoint order and try the default port first. |
| GG-34215 | Cluster SQL Engine | Added a check for indexed field type with a type that was used in the put operation. |
| GG-34153 | Cluster Storage Engine | Improved logging related to the persistent data structure message for in-memory data region. |
| GG-34140 | Binary Objects | Fixed a rare error with modifying binary objects that contain collections or references to objects. |
| GG-34117 | Distributed Data Structures | Fixed an issue that could lead to incorrect operation of the IgniteLock after reconnecting the client node. |
| GG-34051 | Platforms & Thin Clients | CPP Thin: Added SQLSTATE string to SQL-related error messages. |
| GG-34045 | Cluster Discovery | Fixed spontaneous SocketTimeoutException in server socket accept (JDK-8247750). |
| GG-34001 | Cluster Storage Engine | Fixed freezing the client when an implicit transaction happens simultaneously with dropping the same cache. |
| GG-33985 | Cluster Storage Engine | Fixed a freeze when the transaction time ends and initiator node fails. |
| GG-33972 | Cluster SQL Engine | Fixed an issue when several logically identical but physically different compound PKs could be written as different keys, leading to corrupted indexes. |
| GG-33932 | Platforms & Thin Clients | Java: Fixed NullPointerException on client creation with BinaryConfiguration. |
| GG-33931 | Platforms & Thin Clients | Java Thin: Fixed ClassNotFoundException on service call after failover. |
| GG-33920 | Diagnostics and Failure Handling | Fixed a possible infinite loop when an exception is suppressed with itself. |
| GG-33904 | Cluster SQL Engine | The CREATE INDEX command now forbids creating duplicate fields. |
| GG-33824 | GridGain Integrations | Upgraded Jackson from 2.11.0 to 2.11.4 version to fix a vulnerability. |
| GG-33696 | Cluster Metrics & Monitoring | Fix walTotalSize jmx property to account for scenarios when wal archiving is turned off. |
| GG-33580 | Platforms & Thin Clients | CPP: Added support for Affinity Fields. Define the void BinaryType<T>::GetAffinityFieldName(std::string&) static method to provide it. |
| GG-33350 | Cluster Storage Engine | Fixed OutOfBoundsException during write-behind flusher lookup. |
| GG-33314 | Cluster Storage Engine | Improved log messages when rebalance fails. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-34159 | Diagnostics and Failure Handling | Fixed NPE in snapshot operation. |
| GG-34098 | Cluster Storage Engine | Fixed a consistency issue for persistent atomic caches that occurred rarely when a cache remove operation was performed on an offline node. |
| GG-33535 | Platforms & Thin Clients | Client nodes cannot authorize another local client anymore. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-34147 | Cluster Snapshot Utility | ZSTD, LZ4, SNAPPY compression options were added for snapshot operations. |
| GG-34006 | Cluster Data Snapshots and Recovery | Fixed a rare freeze during incremental snapshot. |
| GG-33987 | Cluster Data Snapshots and Recovery | Incremental snapshots schedule persists after a cluster restart. |
| GG-33828 | Cluster Data Snapshots and Recovery | Fixed potential snapshot corruption for the statically configured caches. |
| GG-33430 | Cluster Snapshot Utility | Added the -excluded_caches parameter to snapshot-utility.sh.: Cache groups can now be passed to -caches and -excluded_caches parameters. |
| GG-33429 | Cluster Snapshot Utility | Added a new --excluded_caches parameter for create, check, and restore operations. This parameter and the --caches parameter for these operations now support cache groups. |

### Control Center Agent Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-34299 | Control Center Agent | Fixed node versions on Cluster page in GridGain Portal. |
| GG-34293 | Control Center Agent | Added an ability to override control-center-agent.properties via system properties with the same names. |
| GG-34277 | Control Center Agent | Fixed error with Control Center Agent reconnecting Control Center after restart. |
| GG-34247 | Control Center Agent | Use portal.gridgain.com as default server for Control Center agent |
| GG-34210 | Control Center Agent | Added support for redirects to Control Center Agent. |
| GG-34038 | Control Center Agent | Upgraded httpclient to 4.5.13. |
| GG-34003 | Control Center Agent | Improved tracing performance for large SpanBatch. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.26-p1`, `8.7.27`, `8.7.27-p1`, `8.7.28`, `8.7.29`, `8.7.29-p1`, `8.7.30`, `8.7.31`, `8.7.32`, `8.7.33`, `8.7.33-p2`, `8.7.34`, `8.7.35`, `8.7.36`, `8.7.37`, `8.7.38`, `8.7.39`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.9`

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

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
