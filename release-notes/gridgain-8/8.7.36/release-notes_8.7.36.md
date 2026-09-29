---
description: >-
  GridGain 8.7.36 adds the index-reader and wal-reader diagnostic tools and
  continuous query support in the Java thin client, along with improvements and
  fixed issues across the Community and Ultimate editions.
hidden: true
---

# GridGain 8.7.36 Release Notes

## New Features

GridGain 8.7.36 provides access to several new features and a variety of improvements.

### Added New Debug Tools

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

Java thin clients can now use [Continuous Queries](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/key-value-api/continuous-queries).

You can use continuous queries in Java thin clients in the same way you use them normally:

```java
IgniteCache<Integer, String> cache = ignite.getOrCreateCache("myCache");

ContinuousQuery<Integer, String> query = new ContinuousQuery<>();

query.setLocalListener(new CacheEntryUpdatedListener<Integer, String>() {

    @Override
    public void onUpdated(Iterable<CacheEntryEvent<? extends Integer, ? extends String>> events)
        throws CacheEntryListenerException {
        // react to the update events here
    }
});

cache.query(query);;
```

## Known Issues

### Snapshot Utility Fails to Read Snapshots for GridGain 8.8.2 and Later

Due to a compatibility issue between GridGain 8.7.36 and 8.8.2 and later, snapshot utility of 8.7.36 version cannot read data from snapshots created for GridGain 8.8.2 and later versions. This leads to `LIST`, `INFO`, and `CREATE` utility commands failing. This issue will be fixed in one of the upcoming releases.

**Workaround**: Use the snapshot management tool for GridGain 8.7.35 and earlier, or 8.8.2 or later.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33227 | Cluster Storage Engine | Fixed copying WAL files in WAL working directory. |
| GG-33144 | Platforms & Thin Clients | .NET: Added a warning to the log when alternate stack check is not enabled. |
| GG-33135 | Cluster Storage Engine | The control.sh --cache partition_reconciliation command can now be run on system caches. |
| GG-33131 | Cluster Storage Engine | Fixed a server failure when another node left the cluster before completing peer class loading for a query. |
| GG-33111 | Cluster Storage Engine | Fixed an issue when WAL was incorrectly considered disabled after a cache was recreated. |
| GG-33110 | Binary Objects | Fixed an issue that caused an error when complex objects with nested collections were updated. |
| GG-33109 | Cluster Discovery | Shortened topology update log message when a node leaves or joins the cluster. |
| GG-33105 | Platforms & Thin Clients | .NET: Added string.Compare support to LINQ provider. |
| GG-33104 | Cluster Deployment | Improved log messages of peer class loading problems. |
| GG-33101 | Platforms & Thin Clients | Fixed possible deadlocks and performance issues due to async continuations executing on the striped pool. Added IgniteConfiguration#asyncContinuationExecutor that defaults to ForkJoinPool#commonPool. |
| GG-33067 | Platforms & Thin Clients | Java thin client: Added support for continuous queries. |
| GG-33056 | Cluster SQL Engine | Fixed SQL query hangs when the table is dropped concurrently. |
| GG-32997 | Cluster Deployment | Fixed a node failure when a class was not found by UriDeploymentSpi. |
| GG-32985 | Cluster Communication | Added extended information to the error message about client connection loss. |
| GG-32938 | Binary Objects | Added IgniteBinary.registerClass method to register binary metadata for a specified Java class. |
| GG-32912 | Cluster Storage Engine | Fixed WAL state inconsistency when WAL was enabled or disabled while concurrently stopping or starting nodes. |
| GG-32815 | Cluster Storage Engine | Fixed a rare error caused by a combination of sequential rebalances and checkpoint process. |
| GG-32288 | Cluster Metrics & Monitoring | Added extended step-by-step metrics for checkpoints. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33091 | Cluster Snapshot Utility | Added more information to the output of the snapshot-utility.sh DELETE command when it fails. |
| GG-32989 | Cluster Data Snapshots and Recovery | Snapshot utility now prints information about the cluster nodes' versions when running LIST or INFO commands. |
| GG-32963 | Cluster Snapshot Utility | Fixed a rare error that occurred at the end of the work of snapshot utility. |
| GG-32712 | Cluster Data Snapshots and Recovery | Fixed race condition in SFTP snapshots. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`, `8.7.29`, `8.7.30`, `8.7.31`, `8.7.32`, `8.7.33`, `8.7.34`, `8.7.35`, `8.8.1`

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
