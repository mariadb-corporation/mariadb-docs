---
description: >-
  GridGain 8.8.11 adds new metrics, extended snapshot compression options, and a new
  option to exclude caches from snapshot operations, along with numerous fixes.
hidden: true
---

# GridGain 8.8.11 Release Notes

## New Features

### New Metrics

A large number of options were added to GridGain:

- New metrics for tracking the number of connected thin clients with the `client.connector` register name.
- New metrics for monitoring SSL connections were added to the `io.communication` register name.
- A new `cluster` register name was added with metrics for cluster status.
- The `cache` register name was extended with additional heap metrics.

You can view the updated metrics list in the [Generic Metrics](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/monitoring-metrics/generic-metrics) section.

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

## Known Issues

In rare cases, an SQL entry that was added in GridGain versions 8.8.9 and earlier and updated in GridGain versions 8.8.10 and later may lead to a corrupted index. The scenario below showcases one of possible cases:

{% code title="Java" %}
```java
// Before 8.8.10
//
// Create a table with a composite PK and a secondary index.
sql("CREATE TABLE test (id1 INT, id2 INT, val INT, CONSTRAINT PK PRIMARY KEY (id1, id2)) with \"cache_name=MY_CACHE\"");
sql("CREATE index my_idx on test (val)");

// Value is inserted by using an incomplete PK (id2 is NULL by default)
sql("insert into test(id1, val) values (1,1);");

...
// Upgrade to 8.8.10 or later.
...


// After the upgrade, use the same incomplete PK key (id2 is NULL by default),
// you might end up with index inconsistency.
sql("insert into test(id1, val) values (1,2);");
// prints [[1]]
System.out.println(sql("select count(1) from test USE INDEX(\"_key_PK\")").getAll());
// prints [[2]]
System.out.println(sql("select count(1) from test USE INDEX(my_idx)").getAll());
// prints 2
System.out.println(grid(0).cache("MY_CACHE").size());
```
{% endcode %}

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34256 | Platforms & Thin Clients | .NET: Fixed potential cache startup error when one of the loaded assemblies has certain compiler-generated type names that can't be parsed by Ignite. |
| GG-34235 | GridGain Integrations | Updated Cassandra module to fix a CVE. |
| GG-34208 | Cluster Metrics & Monitoring | Fixed an error with getting cache size through mbean if the cluster is inactive. |
| GG-34190 | Platforms & Thin Clients | .NET: Fixed thin client streamer not creating SQL table entries. |
| GG-34172 | Cluster SQL Engine | Added a check for indexed field type with a type that is used in the put operation. |
| GG-34169 | Platforms & Thin Clients | .NET: Fixed thin client SslStreamFactory to allow SSL connection without client-side certificate. |
| GG-34139 | Cluster Metrics & Monitoring | Extended cache metrics. |
| GG-34134 | Binary Objects | Fixed a rare error with modifying binary objects that contain collections or references to objects. |
| GG-34133 | Cluster Storage Engine | Fixed additional resource consuption by clearing obsolete entries. |
| GG-34128 | Platforms & Thin Clients | Java thin: Fixed connection logic to follow user-defined endpoint order and try the default port first. |
| GG-34092 | Cluster Metrics & Monitoring | Extended cluster topology metrics. |
| GG-34075 | Platforms & Thin Clients | .NET: Fixed NullReferenceException in thin client due to late logger setter. |
| GG-34005 | Cluster SQL Engine | Fixed possible assertion error when dropping a table. |
| GG-33876 | Platforms & Thin Clients | Discovery statistics metrics migrated to a new framework. |
| GG-33720 | Platforms & Thin Clients | Added SSL connection metrics. |
| GG-33697 | Distributed Data Structures | Fixed an issue that could lead to incorrect operation of the IgniteLock after reconnecting the client node. |
| GG-33043 | Cluster Storage Engine | Improved logging related to the persistent data structure message for in-memory data region. |
| GG-32942 | Cluster Metrics & Monitoring | Added metrics for the number of connected thin clients. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34325 | Cluster Rolling Upgrade | Fixed an issue with snapshot utility not being able to capture snapshot on mixed cluster |
| GG-34110 | Diagnostics and Failure Handling | Fixed NPE in snapshot operation. |
| GG-33425 | Cluster Storage Engine | Fixed a consistency issue for persistent atomic caches that occurred rarely when a cache remove operation was performed on an offline node. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33437 | Cluster Snapshot Utility | ZSTD, LZ4, SNAPPY compression options were added for snapshot operations. |
| GG-33418 | Cluster Snapshot Utility | Added the -excluded_caches parameter to snapshot-utility.sh.: Cache groups can now be passed to -caches and -excluded_caches parameters. |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34233 | Control Center Agent | Fixed an error with Control Center Agent reconnecting Control Center after restart. |
| GG-34217 | Control Center Agent | Reverted SSL validation for Control Center Agent. |
| GG-34074 | Control Center Agent | Added support for redirects to Control Center Agent. |
| GG-34073 | Control Center Agent | Extended log information for a failed connection. |

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

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
