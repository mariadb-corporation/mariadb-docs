---
description: >-
  GridGain 8.8 Beta (8.8.0.b2) provides early access to PDS defragmentation,
  Maintenance Mode, Transparent Data Encryption with key rotation, and dictionary-based
  data compression.
hidden: true
---

# GridGain 8.8.0.b2 BETA Release Notes

## Introduction

GridGain 8.8 Beta provides early access to new features and improvements for development and testing needs.

## New Features

This section lists the features that are introduced in this product release.

### PDS Defragmentation

When used with Native Persistence, Ignite persists caches' data to disk to enable durability. These files grow automatically when new data is added to the caches, but don't shrink when existing data is removed. In most scenarios it is not an issue as space is reused when new data is added again, but in some situations it is possible that the files occupy much more disk space than required.

Defragmentation feature enables to compact the files and return disk space back to operating system.

Node executing defragmentation cannot serve usual workload and has to enter a special Maintenance Mode where it does not join the cluster, but starts in isolation to defragment its data files.

The following commands are used to manage defragmentation:

```shell
control.sh --defragmentation schedule --nodes <nodes' consistent IDs>
control.sh --defragmentation schedule --nodes <nodes' consistent IDs> --caches <caches' names>
```

Schedules defragmentation on the set of nodes with optional set of cache names. After the defragmentation is scheduled on a node, it should be restarted to enter Maintenance Mode and start defragmenting necessary caches.

```shell
control.sh --defragmentation cancel
```

Cancels ongoing defragmentation process. As nodes executing defragmentation are isolated from the rest of the cluster, particular host and port of the node should be specified.

### Maintenance Mode

In special situations, like Persistent Store files corruption or Defragmentation, node should not join the rest of the cluster but stay isolated allowing user to step in and do necessary actions.

Node enters Maintenance Mode on a restart if it finds a maintenance task. This task is created automatically in case of Store files corruption or explicitly by the user request if Defragmentation is scheduled.
To schedule a defragmentation in the simplest way, use a command similar to the following:

```shell
control.sh --defragmentation schedule --nodes <nodes' consistent IDs>
```

Defragmentation section describes other forms of the command.

When maintenance task is completed, the node has to be restarted again to exit Maintenance Mode and return to normal operations.

### Transparent Data Encryption

Transparent data encryption automatically and silently protects data in rest (persistence).
If cache/table encryption is configured, GridGain generates a key (a cache encryption key) and uses this key to encrypt/decrypt the cache's data.
The cache encryption key is held in the system cache and cannot be accessed by users.
When the key needs to be sent to other nodes or saved to disk (when the node goes down), it is encrypted using the user provided key — the master key.
In the current release, a support of master key and cache keys rotation is added.

To control the master key rotation process,  use some of the following interfaces:

{% code title="Starting master key rotation" %}
```java
String masterKeyName = "master-key-name-example";
ignite.encryption().changeMasterKey(masterKeyName);
```
{% endcode %}

{% code title="Getting current master key name." %}
```java
String masterKeyName = ignite.encryption().getMasterKeyName();
```
{% endcode %}

Note: Cache start and node join during the key changing process is prohibited and will be rejected.
If a node was unavailable during the master key rotation process, it will not be able to join the cluster with an old master key.
The node should re-encrypt group keys during recovery on startup. The actual master key
name should be set via `IgniteSystemProperties#IGNITE_MASTER_KEY_NAME_TO_CHANGE_BEFORE_STARTUP`.

The process of cache encryption key rotation contains two steps:

- Rotate cache group key - add a new encryption key on each node and set it for writing.

- Schedule background re-encryption for archived data and cleanup the old key when it completes.

Note: Node join is rejected during the rotation of a cache group encryption key. Background re-encryption of
the existing data in the specified cache group(s) begins after the encryption key(s) is changed. During
the re-encryption, joining of a node is not rejected, the cluster remains fully functional. It is a fault-tolerant operation
that automatically continues after restart. Secondary rotation of the cache group encryption key is possible only after the background re-encryption of the existing data in this cache group is completed.

To start a cache group encryption key change process from java API, use the following method:

```java
ignite.encryption().changeCacheGroupKey(Collection<String> cacheOrGroupNames)
```

### Data Compression

Added the support of dictionary-based data entry compression using [Zstandard library](https://github.com/facebook/zstd).
The Entry compression allows to save RAM and disk space by storing compressed data in cache entries, at cost of spending CPU time on compression and decompression.
Enabling entry compression leads to Off-Heap utilization and checkpoint directory size reduction, as well as it slightly shortens WAL. If native persistence is used and the load pattern is I/O bound, it is possible to save space while improving the performance.

{% code title="Enabling Data Compression." %}
```java
ZstdDictionaryCompressionConfiguration compressionCfg = new ZstdDictionaryCompressionConfiguration();
// Default values for all properties listed below:
compressionCfg.setCompressKeys(false);
compressionCfg.setRequireDictionary(true);
compressionCfg.setDictionarySize(1024);
compressionCfg.setSamplesBufferSize(4 * 1024 * 1024);
compressionCfg.setCompressionLevel(2);

CacheConfiguration cacheCfg = new CacheConfiguration("cache-name");
cacheCfg.setEntryCompressionConfiguration(compressionCfg);
```
{% endcode %}

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30589 | Cluster Storage Engine | Maintenance Mode: |
| GG-31718 | Cluster Storage Engine | New PDS Defragmentation feature. |
| GG-28240 | Cluster Storage Engine | New dictionary-based cache entry compression feature. |
| GG-31013 | Cluster Storage Engine | New Transparent Data Encryption feature. |
| GG-31186 | Cluster SQL Engine | The SQL system schema changed to "SYS" from "IGNITE". |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

See the list of product versions that are compatible with the current version below.
You can perform a rolling-upgrade for any product version that is on the list. Compatibility with other versions is not guaranteed.
If you use a version that is not listed, please contact GridGain for more information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`,
`8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`,
`8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`,
`8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`,
`8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`, `8.7.29`, `8.7.30`, `8.7.31`

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
