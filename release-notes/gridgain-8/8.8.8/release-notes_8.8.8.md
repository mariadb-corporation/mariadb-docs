---
description: >-
  GridGain 8.8.8 adds C++ support for Java compute, compute tasks in C++ thin clients, Hibernate L2 cache templates, and configurable page replacement algorithms.
hidden: true
---

# GridGain 8.8.8 Release Notes

## New Features

## Improvements and Fixed Issues

### Added Support for C++ Java Compute

You can now use the new `Compute::ExecuteJavaTask` method to execute Java compute tasks from C++ code by their names. For example:

{% code title="C++" %}
```cpp
Ignite ignite = Ignition::Get();
compute::Compute compute = ignite.GetCompute();

std::string echoValue = "Task returns this value";

std::string res = compute.ExecuteJavaTask<std::string>("my.company.MyEchoTask", echoValue);

assert(res == echoValue);
```
{% endcode %}

### Added Support for Compute Tasks in C++ Thin Clients

Compute tasks can now be performed by using C++ thin clients. For example, here is how you can execute a newly added compute task on :

{% code title="C++" %}
```cpp
IgniteClient client = IgniteClient::Start();
compute::ComputeClient compute = ignite.GetCompute();

std::string echoValue = "Task returns this value";

std::string res = compute.ExecuteJavaTask<std::string>("my.company.MyEchoTask", echoValue);

assert(res == echoValue);
```
{% endcode %}

### Added Support for Cache Templates in Hibernate L2

When working with Hibernate L2, you may want to use the same cache configuration for multiple caches. Now you can use preconfigured Cache Templates to apply the same configuration to multiple caches.

For example, the following configuration uses a single `transactional-cache` bean for multiple entities:

{% code title="XML" %}
```xml
<bean parent="transactional-cache">
    <property name="name" value="com.mycompany.*"/>
</bean>
```
{% endcode %}

### Implemented Page Replacement Algorithms

When the amount of data stored on disk is bigger than the off-heap memory amount allocated for the data region, another page should be removed from off-heap to the disk to preload an appropriate page to off-heap memory.

There are three available algorithms:

- Random-LRU algorithm;
- Segmented-LRU algorithm;
- CLOCK algorithm.

By default, [CLOCK](https://en.wikipedia.org/wiki/Page_replacement_algorithm#Clock) algorithm is used.

Page replacement algorithm is configured by the `PageReplacementMode` property of `DataRegionConfiguration`.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
<!-- Memory configuration. -->
<property name="dataStorageConfiguration">
<bean class="org.apache.ignite.configuration.DataStorageConfiguration">
<property name="dataRegionConfigurations">
<list>
<!--
Defining a persistent data region with Segmented LRU page replacement mode.
-->
<bean class="org.apache.ignite.configuration.DataRegionConfiguration">
<!-- Data region name. -->
<property name="name" value="persistent_data_region"/>
<!-- Enable persistence. -->
<property name="persistenceEnabled" value="true"/>
<!-- 20 GB maximum size (RAM). -->
<property name="maxSize" value="#{20L * 1024 * 1024 * 1024}"/>
<!-- Enabling SEGMENTED_LRU page replacement for this region.  -->
<property name="pageReplacementMode" value="SEGMENTED_LRU"/>
</bean>
</list>
</property>
</bean>
</property>
<!-- The rest of the configuration. -->
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
// Node configuration.
IgniteConfiguration cfg = new IgniteConfiguration();

// Memory configuration.
DataStorageConfiguration storageCfg = new DataStorageConfiguration();

// Creating a new data region.
DataRegionConfiguration regionCfg = new DataRegionConfiguration();

// Region name.
regionCfg.setName("persistent_data_region");

// Enabling persistence.
regionCfg.setPersistenceEnabled(true);

// 20 GB max size (RAM).
regionCfg.setMaxSize(20L * 1024 * 1024 * 1024);

// Enabling SEGMENTED_LRU page replacement for this region.
regionCfg.setPageReplacementMode(PageReplacementMode.SEGMENTED_LRU);

// Setting the data region configuration.
storageCfg.setDataRegionConfigurations(regionCfg);

// Applying the new configuration.
cfg.setDataStorageConfiguration(storageCfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
Not supported on this platform.
{% endtab %}
{% tab title="C++" %}
Not supported on this platform.
{% endtab %}
{% endtabs %}

## Known Issues

### Index Page Usage Metric is Incorrect

Index pages allocation metric is currently not being tracked correctly. This issue that will be fixed in the upcoming release.

### GridGain May Crash when Using OpenJDK 11

In some rare environments, GridGain servers may crash with a `SocketTimeoutException` exception when running on OpenJDK 11. Consider using OpenJDK 8 or a different JDK provider instead.

Here is an example of the exception that can occur:

```
Exception in thread "main" java.net.SocketTimeoutException: Accept timed out
        at java.base/java.net.PlainSocketImpl.socketAccept(Native Method)
        at java.base/java.net.AbstractPlainSocketImpl.accept(AbstractPlainSocketImpl.java:458)
        at java.base/java.net.ServerSocket.implAccept(ServerSocket.java:565)
        at java.base/java.net.ServerSocket.accept(ServerSocket.java:533)
        at Example.main(Example.java:6)
```

You can track the status of this issue in [openJDK issue tracker](https://bugs.openjdk.java.net/browse/JDK-8237858).

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33676 | Cluster Storage Engine | Fixed an issue that could lead to data desynchronization if a node is restarted during rebalancing under the load. |
| GG-33662 | Cluster Metrics & Monitoring | Fixed an error with unregistering JMX metric. |
| GG-33652 | GridGain Integrations | User can provide template cache configuration with an asterisk in the name (e.g. "org.example.app.entity.*") and this template will be used for the auto creation of the Hibernate L2 cache. |
| GG-33631 | Platforms & Thin Clients | Added compute functionality to C++ thin client. |
| GG-33630 | Platforms & Thin Clients | CPP: Added an ability to run Java tasks by name: Compute::ExecuteJavaTask. |
| GG-33584 | Cluster Storage Engine | Returned IGNITE_THRESHOLD_WAL_ARCHIVE_SIZE_PERCENTAGE for backwards compatibility. |
| GG-33575 | Cluster Security | Upgraded Hadoop from 2.7.7 to 2.8.5 version to fix vulnerability. |
| GG-33574 | Cluster Security | Upgraded Tomcat from 9.0.21 to 9.0.52 version to fix vulnerability. |
| GG-33572 | Cluster Security | Upgraded slf4j from 1.7.7. to 1.7.32 version to fix vulnerability. |
| GG-33560 | Cluster Data Replication | Fixed a race when changing update log, leading to the B+Tree corrupt in incremental DR. |
| GG-33519 | Cluster Storage Engine | Fixed a rare issue on joins with empty LFS. |
| GG-33456 | Cluster Communication | Exception while processing messages by the NIO server no longer affects other messages. |
| GG-33454 | Cluster Storage Engine | Added automatic release of WAL segments when reaching the DataStorageConfiguration#maxWalArchiveSize. |
| GG-33444 | Cluster Storage Engine | Added new page replacement algorithms: Replaced default implementation with the Clock algorithm. |
| GG-33442 | Cluster SQL Engine | Log messages about long running and huge results queries are now throttled. |
| GG-33321 | Cluster Storage Engine | Corrected exception handling for checkpoint marker reading error. |
| GG-33285 | Cluster SQL Engine | Added a 'sql.createLuceneIndexForStringValueType' distributed SQL property to disable creation of lucene index by default. |
| GG-32986 | Cluster Storage Engine | Fixed possible failure of background cleanup of dropped SQL indexes. |
| GG-32940 | Cluster Security | Fixed cache group re-encryption after cluster secondary activation. |
| GG-32178 | Diagnostics and Failure Handling | Improved diagnostic capabilities for assertion errors in internal data structures. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33677 | Cluster Security | Fixed an issue that could cause PME freezing during the expiration of thin clients security sessions. |
| GG-33613 | Cluster Data Replication | Fixed wrong sender node detection for nodes in different DR modes in grid during RU. |
| GG-33591 | Cluster Storage Engine | Fixed an issue when a node starts with a WAL archive size over the maxWalArchiveSize setting. |
| GG-33570 | Cluster Communication | Updated Jetty dependency to fix CVE. |
| GG-33538 | Platforms & Thin Clients | .NET: Removed unnecessary code analysis results from the release package. |
| GG-21977 | Cluster Storage Engine | TransactionMXBean parameters now propagate to cluster correctly, including newly joined nodes. |
| GG-14936 | Cluster Data Replication | Improved DR logging to show information on SSL/TLS statuses. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33583 | Cluster Data Snapshots and Recovery | Fixed potential deadlock during snapshot creation. |
| GG-32372 | Cluster Snapshot Utility | Fix an error message when creating a snapshot fails. |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33533 | Control Center Agent | The cache schema is not sent until the cluster attaches. |
| GG-33469 | Control Center Agent | Old deployment unit versions are now stored in metastore. |
| GG-33263 | Control Center Agent | Fixed an issue with Control Center Agent on zOS systems. |
| GG-33107 | Control Center Agent | Sanitized sensitive information sent to Control Center by Control Center Agent. |
| GG-32797 | Control Center Agent | You can now change Control Center URI without changing Control Center Agent status. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.2-p15`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.5-p1`, `8.7.6`, `8.7.6-p1`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.26-p1`, `8.7.27`, `8.7.27-p1`, `8.7.28`, `8.7.29`, `8.7.29-p1`, `8.7.30`, `8.7.31`, `8.7.32`, `8.7.33`, `8.7.33-p2`, `8.7.34`, `8.7.35`, `8.7.36`, `8.7.37`, `8.7.38`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`, `8.8.6`, `8.8.7`

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

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
