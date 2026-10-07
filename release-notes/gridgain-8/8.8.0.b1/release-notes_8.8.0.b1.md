---
description: >-
  GridGain 8.8 Beta (8.8.0.b1) provides early access to Incremental Data Center
  Replication, Managed Rolling Upgrade, Spring 5.2.0 support, and metrics framework
  improvements.
hidden: true
---

# GridGain 8.8.0.b1 BETA Release Notes

## Introduction

GridGain 8.8 Beta provides early access to new features and improvements for development and testing needs.

## New Features

This section lists the features that are introduced in this product release.

### Incremental State Transfer

We've rethought data flow in DR and added Incremental Data Center Replication mode with safer approach to Data Center Replication.
The new mode includes the following improvements:

- higher stability
- less memory requirements
- simplified configuration

**Main advantages:**

- No need to worry about DrSenderStore configuration on sender node anymore. Sender uses non-persistent state transfer buffer instead to smooth network load spikes
and only responsible for routing data to remote Datacenters. DR does not rely on sender store and is fully tolerant to sender-node failure.
- No need to worry about backup queue size for DR purposes that was very hard to configure and provided poor guaranties.
We removed backup queues to prevent potential data-loss in case of primary-node failure.
- Better stability. DrSenderStore (now state transfer buffer) overflow, and a sender-node failure don't cause DR stop.
You don't need to start full state transfer after DR stops due to any reason as all grid nodes track DR progress automatically.
- DR is fully asynchronous background process and introduces no additional latency to cache operations. It cost equals to an additional SQL index.
- "Incremental state transfer over snapshot" feature allows to transfer a "delta" only to remote DC which may helps to save time and network resources in some cases.

**Limitations:**

- **Rolling upgrade is NOT seamless**. New DR mode is NOT compatible with the previous one.
First, you must stop DR for all caches before the beginning of a rolling restart procedure.
A full state transfer may be needed after the upgrade is finished.
- Only a single state transfer per-cache at a time allowed for now.
- Replication to multiple remote data centers within same state transfer operation is still possible,
but notice that DR may stuck if one of DCs become unavailable until the connection will be recovered.
- Full state transfer and background incremental DR process share the same buffer on sender-node. Thus, recent updates has no priority over full state transfer updates.
- "Incremental state transfer over snapshot" scenario will NOT work with a snapshot created on previous grid version.
A try will lead to a full state transfer.

**How to use:**

Set system property `GG_INCREMENTAL_STATE_TRANSFER=true` to start with incremental DR mode.
No additional configuration changes needed, unsupported configuration options will be just ignored.

Use `DrSenderConfiguration.setFullStateTransferBufferSize(long bytes)` to limit DR buffer on sender-node.

**"Incremental state transfer over snapshot" scenario:**

You need to follow next steps to get remote DC in-sync using snapshot:

- take a snapshot in source DC.
- copy it to target DC.
- restore the snapshot on target DC.
- start incrementalStateTransfer providing snapshot id.

### Added support for Spring 5.2.0 and Spring Data 2.2.0

You can now use Spring 5.2.0 and Spring Data 2.2.0 with GridGain.
This integration comes from the `ignite-spring-data_2.2` module. To use it, add a dependency to your pom.xml:

```xml
<dependency>
    <groupId>org.gridgain</groupId>
    <artifactId>ignite-spring-data_2.2</artifactId>
    <version>8.8.0.b1</version>
</dependency>
```

### Managed Rolling Upgrade

The new distributed rolling upgrade allows controlling the process of an upgrade in a predictable and careful way.
It is based on the three following constraints:

- the cluster does not allow to join nodes of different versions until upgrade mode is enabled.
- when upgrade mode is enabled, you can connect another node with only one different version that is larger than the current one.
- new features will not be activated until the upgrade mode is turned off manually.

{% code title="Activating the Rolling Upgrade mode." %}
```shell
./control.sh --rolling-upgrade on --yes

Rolling upgrade mode successfully enabled.
```
{% endcode %}

{% code title="Checking the status of the Rolling Upgrade." %}
```shell
./control.sh --rolling-upgrade status

Rolling upgrade is enabled
Initial version: 8.8.0#20200714-sha1:35c405b6
Target version: N/A
List of alive nodes in the cluster that are not updated yet: 54a088fb
List of alive nodes in the cluster that are updated:
```
{% endcode %}

{% code title="Stopping the Rolling Upgrade." %}
```shell
./control.sh --port 11311  --rolling-upgrade off

Rolling upgrade mode successfully disabled.
```
{% endcode %}

### Metrics framework updates and improvements

A new object lists engine for exporting internal objects information as system views was added, existing system views were updated to use new lists engine. These system views export only local objects available on a node being queried. A number of system views exporting information about Ignite internal runtime objects were added, for example:

- Topology details are available via `SYS.NODES`, `SYS.NODE_ATTRIBUTES`, and `SYS.BASELINE_NODES` system views
- Compute tasks details are available via `SYS.TASKS` and `SYS.JOBS` system views
- Query details are available via `SYS.SQL_QUERIES`, `SYS.SCAN_QUERIES`, `SYS.CONTINUOUS_QUERIES`, `SYS.SQL_QUERIES_HISTORY` system views
- Services details are available via `SYS.SERVICES` system view
- Running transactions details are available via `SYS.TRANSACTIONS` system view
- Various caches details are available via `SYS.CACHES`, `SYS.CACHE_GROUPS`, `SYS.PARTITION_STATES` system views
- The system views list and column details are available via `SYS.VIEWS` and `SYS.VIEW_COLUMNS` system views

Alongside with the lists monitoring engine, a number of improvements in the metrics framework were made, such as adding histograms for transaction commit/rollback and cache put/get/remove operation timings.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-29029 | Cluster Metrics & Monitoring | Various improvements to the cluster metrics. |
| GG-31063 | GridGain Integrations | Support for Spring 5.2.0 and Spring Data 2.2.0. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30403 | Cluster Rolling Upgrade | Improved management and stability of the Rolling Upgrade feature. |
| GG-31117 | Cluster Data Replication | New Incremental Data Center Replication feature. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

See the list of product versions that are compatible with the current version below.
You can perform a rolling-upgrade for any product version that is on the list. Compatibility with other versions is not guaranteed.
If you use a version that is not listed, please contact GridGain for more information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`,
`8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`,
`8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`,
`8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`,
`8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`, `8.7.29`, `8.7.30`

### Known Limitations

#### Jetty configuration incompatibility in GridGain 8.7.21 and later

If you are upgrading from 8.7.20 version or earlier, consider an incompatibility issue related to Jetty configuration introduced in GridGain 8.7.21.

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

#### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and later

In GridGain 8.7.26, the default value of the property `IgniteConfiguration.rebalanceThreadPoolSize` changed from `1` to `min(4, number of CPU / 4)`.
It may cause a compatibility issue under the following conditions:

- When a Rolling Upgrade is performed
- The upgrade is performed from 8.5.7 version (or earlie) to 8.5.x or from 8.7.3 (or earlier) to 8.7.x
- The server nodes have at least 8 CPU cores
- The nodes configuration does not have the property IgniteConfiguration.rebalanceThreadPoolSize , so the default value is used

In this case, an exception is thrown with an error message similar to the following:

```text
сlass org.apache.ignite.IgniteException: Rebalance configuration mismatch (fix configuration or set -DIGNITE_SKIP_CONFIGURATION_CONSISTENCY_CHECK=true system property).
Different values of such parameter may lead to rebalance process instability and hanging.  [rmtNodeId=5fc58fb7-209d-489a-8034-0127a81abed6, locRebalanceThreadPoolSize = 4, rmtRebalanceThreadPoolSize = 1]
```

To workaround this issue, change the configuration of the server nodes to rebalanceThreadPoolSize=1 so that it matches the previous default configuration. For example:

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="rebalanceThreadPoolSize" value="1"/>

    <!-- The rest of the configuration goes here -->
</bean>
```

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) page for more information.
