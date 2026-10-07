---
description: >-
  GridGain 8.8.5 adds a GZIP compression option, new index-reader and WAL-reader debug tools, and the Continuous Query API in the Java thin client.
hidden: true
---

# GridGain 8.8.5 Release Notes

## New Features

### Added GZIP Compression Option

With the new `GzipCompressionConfiguration` you can use the **gzip** algorithm for compression instead of **Zstandard**. You can switch the algorithm to improve performance, or run gzip on systems that do not support Zstandard.

Here is how you can create a new cache configuration and switch it to gzip algorithm:

```
ignite.getOrCreateCache(
new CacheConfiguration<>("foo").setEntryCompressionConfiguration(
new GzipCompressionConfiguration()))
```

### Added new debug tools

New **index-reader.sh** and **wal-reader.sh** CLI were added to provide more information on inssues with SQL indexes and WAL issues.

Here is how you can check indexes in the persistent storage:

{% tabs %}
{% tab title="Linux" %}
```shell
index-reader.sh --dir <cache directory>
```
{% endtab %}
{% tab title="Windows" %}
```shell
index-reader.bat --dir <cache directory>
```
{% endtab %}
{% endtabs %}

And here is how to use wal-reader:

{% tabs %}
{% tab title="Linux" %}
```shell
.\wal-reader.sh --wal-dir <wal directory>
```
{% endtab %}
{% tab title="Windows" %}
```shell
.\wal-reader.bat --wal-dir <wal directory>
```
{% endtab %}
{% endtabs %}

You can also read WAL archive:

{% tabs %}
{% tab title="Linux" %}
```shell
.\wal-reader.sh --wal-archive-dir <wal archive dir>
```
{% endtab %}
{% tab title="Windows" %}
```shell
.\wal-reader.bat --wal-archive-dir <wal archive dir>
```
{% endtab %}
{% endtabs %}

### Added Continuous Query API in Java Thin Client.

Java Thin clients can now use [Continuous Queries](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/key-value-api/continuous-queries).

You can use Continuous queries in Java thin clients in the same way you use them normally:

```
IgniteCache<Integer, String> cache = ignite.getOrCreateCache("myCache");

ContinuousQuery<Integer, String> query = new ContinuousQuery<>();

query.setLocalListener(new CacheEntryUpdatedListener<Integer, String>() {

@Override
public void onUpdated(Iterable<CacheEntryEvent<? extends Integer, ? extends String>> events)
throws CacheEntryListenerException {
}
});

cache.query(query);;
```

## Known Issues

### Rolling Upgrade Fails to Start when Security is Enabled

In GridGain 8.8.5, starting a rolling upgrade with the security feature enabled may cause the **Authorization failed** error.

**Workaround**: Use the `control-utility.sh` to start the rolling upgrade and explicitly specify the coordinator node host with the `--host xxxx --port xxxx` parameters   (coordinator node is the oldest node in cluster topology).

### AssertionError on Quick Node Restart

If the node is quickly restarted after a shutdown, it can throw the `AssertionError` in the log exception in the log.

**Workaround**: There are two ways to deal with this issue:

1. Start nodes slowly, so new node’s `NODE_JOINED` event (for data nodes) arrives after DR processor has started.
2. Disable assertions. To do this, launch JVM without the `-ea` option.

### CorruptedTreeException on Node Restart

If the node unexpectedly exits the cluster and then reenters it during data center replication, `CorruptedTreeException` may occur.

**Workaround**: Disable assertions.  To do this, launch JVM without the `-ea` option.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33221 | Cluster Storage Engine | Copying WAL files in WAL working directory is fixed |
| GG-33143 | Platforms & Thin Clients | .NET: Added a warning to the log when alternate stack check is not enabled. |
| GG-33125 | Cluster Storage Engine | Fixed a server failure when another node left the cluster before completing peer class loading for a query. |
| GG-33106 | Binary Objects | Fixed an issue that caused an error when complex objects with nested collections were updated. |
| GG-33102 | Platforms & Thin Clients | .NET: Added string.Compare support to LINQ provider. |
| GG-33094 | Cluster Storage Engine | Fixed an issue when WAL was incorrectly considered disabled after a cache was recreated. |
| GG-33033 | Cluster Storage Engine | The control.sh --cache partition_reconciliation command can now be run on system caches. |
| GG-33016 | Platforms & Thin Clients | Java thin client: Added support for continuous queries. |
| GG-33000 | Cluster SQL Engine | Added an ability to restart control.sh --cache indexes_force_rebuild if the first attempt failed. |
| GG-32856 | Cluster Storage Engine | Fixed possible deadlocks and performance issues due to async continuations executing on the striped pool. Added IgniteConfiguration#asyncContinuationExecutor that defaults to ForkJoinPool#commonPool. |
| GG-32845 | Cluster Deployment | Improved log messages of peer class loading problems. |
| GG-32830 | Cluster Communication | Added extended information to the error message about client connection loss. |
| GG-32559 | Cluster Storage Engine | Fixed a rare error caused by a combination of sequential rebalances and checkpoint process. |
| GG-32500 | Cluster Deployment | Fixed a node failure when a class was not found by UriDeploymentSpi. |
| GG-31970 | Cluster Discovery | Shortened topology update log message when a node leaves or joins the cluster. |
| GG-31195 | Cluster Storage Engine | Fixed WAL state inconsistency when WAL was enabled or disabled while concurrently stopping or starting nodes. |
| GG-30691 | Cluster Metrics & Monitoring | Fixed CPU load and memory metrics displaying negative values on Java 11. |
| GG-28550 | Binary Objects | Added IgniteBinary.registerClass method to register binary metadata for a specified Java class. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33159 | Cluster Data Replication | Fixed node crash after upgrade to 8.8.4 if the data center replication was enabled and the node was not stopped gracefully before the upgrade. |
| GG-32193 | Cluster Storage Engine | Fixed an error when the same object was put in two compressed caches. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32352 | Cluster Snapshot Utility | Added more information to the output of the snapshot-utility.sh DELETE command when it fails. |
| GG-31703 | Cluster Data Snapshots and Recovery | Snapshot utility now prints information about the cluster nodes' versions when running LIST or INFO commands. |
| GG-26867 | Cluster Snapshot Utility | Fixed a rare error that occurred at the end of the work of snapshot utility. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.2-p15`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`,
`8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`, `8.7.29`,
`8.7.30`, `8.7.31`, `8.7.32`, `8.7.33`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`

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
