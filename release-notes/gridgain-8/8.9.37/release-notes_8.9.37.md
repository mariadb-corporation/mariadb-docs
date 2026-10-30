---
description: >-
  GridGain 8.9.37 adds REST commands for inspecting caches and rebalance progress, along with SFTP host key verification for network backups and a number of security, thin client, and replication fixes.
hidden: true
---

# GridGain 8.9.37 Release Notes

## Overview

GridGain 8.9.37 adds REST commands for inspecting caches and rebalance progress, along with SFTP host key verification for network backups and a number of security, thin client, and replication fixes.

## Deprecation Notice

### Gridify API

Starting with this release, the Gridify API is deprecated and will be removed in a future release. This includes the `@Gridify`, `@GridifySetToSet`, and `@GridifySetToValue` annotations, their supporting classes, and the AOP aspects in the `ignite-aop` module.

To distribute a method call across the cluster, use the [compute API](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/distributed-computing/distributed-computing) instead.

### ignite-cloud Module

Starting with this release, the `ignite-cloud` module and its `TcpDiscoveryCloudIpFinder` are deprecated and will be removed in a future release. Use the [Amazon S3 IP Finder](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/clustering/discovery-in-the-cloud#amazon-s3-ip-finder), [Amazon ELB Based Discovery](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/clustering/discovery-in-the-cloud#amazon-elb-based-discovery), or [Google Compute Discovery](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/clustering/discovery-in-the-cloud#google-compute-discovery) instead.

## New Features

### Supply Status REST Command

With this release, the REST API provides a `supply-status` command that reports whether a node is still supplying partitions to other nodes. Use it before you stop a node during a rolling restart to confirm that the node is no longer serving rebalance demand.

```shell
http://host:port/ignite?cmd=supply-status
```

For more information about the REST API, see the [REST API](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/restapi) documentation.

### Cache List and Cache Distribution REST Commands

With this release, the REST API provides `cachelist` and `cachedistribution` commands. These are the REST equivalents of the `control.sh --cache list` and `control.sh --cache distribution` commands and report the same information, so you can inspect caches over HTTP without running the control script.

```shell
http://host:port/ignite?cmd=cachelist
http://host:port/ignite?cmd=cachedistribution
```

Neither command has a dedicated REST permission. On a secured cluster, the caller needs the same permissions that the corresponding control script command requires, so no security configuration change is needed when you move from `control.sh` to the REST API.

For more information, see [Cache List](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/restapi#cache-list) and [Cache Distribution](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/restapi#cache-distribution).

### SFTP Host Key Verification for Network Backups

With this release, GridGain can verify the SSH host key of an SFTP server before it transfers snapshot data. Set the `strictHostKeyChecking` property of `SftpConfiguration` to `true` to enable verification, and use `knownHostsPath` to point to the known hosts file. If `knownHostsPath` is not set, GridGain uses the `~/.ssh/known_hosts` file of the account running the node.

Verification is disabled by default, so existing configurations continue to work unchanged.

For more information, see [Configuring SFTP Location](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/snapshots/network-backups#configuring-sftp-location).

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-50963 | Platforms & Thin Clients | .NET: Fixed non-monotonic clock used for request duration checks. |
| GG-50955 | Platforms & Thin Clients | .NET: Fixed round-robin fail on negative index. |
| GG-50764 | Binary Objects | The marshaller class filter is now honored for nested Visor DTO blobs. |
| GG-50760 | Platforms & Thin Clients | Fixed memory leak on thin client SQL query timeout. |
| GG-50719 | Cluster Storage Engine | Bulk cache operations that exceed the maximum marshalled byte array size now fail with an actionable error. |
| GG-50716 | Platforms & Thin Clients | .NET: Fixed connection leaks when client startup fails. |
| GG-50698 | Control Center Agent | Fixed Spring Framework dependency conflicts when embedding the Control Center agent into host applications. |
| GG-50681 | Platforms & Thin Clients | Java thin: fixed duplicate connections to the same server node after topology changes or cluster restarts. |
| GG-50657 | Platforms & Thin Clients | Improved security posture of client continuous queries with remote filter. |
| GG-50638 | Platforms & Thin Clients | .NET: Thin client: fixed open socket leak on node id mismatch when cluster discovery is enabled. |
| GG-50635 | Cluster SQL Engine | Fixed the issue when SQL query against just created cache failed. |
| GG-50577 | Cluster Metrics & Monitoring | Fixed cmd=probe&kind=readiness REST commands ignoring the cmd=drain flag. |
| GG-50556 | Cluster Compute Grid | The Gridify API is now deprecated and will be removed in a future release. |
| GG-50501 | Builds and Deliveries | Updated jackson from 2.16.0 to 2.18.9. |
| GG-50476 | Cluster Control Script | Added REST APIs mirroring `--cache list` and `cache distribution` CLI commands. |
| GG-50474 | Platforms & Thin Clients | Java Thin Client: Fixed partition awareness not working after cluster restart with the same topology version. |
| GG-50462 | Cluster Discovery | The optional ignite-cloud module, including TcpDiscoveryCloudIpFinder, is deprecated. |
| GG-50331 | Platforms & Thin Clients | Java thin: Fixed stale client cluster group data after cluster restart. |
| GG-50214 | Cluster Service Grid | Fixed legacy service processor dropping the service call context for locally-deployed services. |
| GG-50106 | Cluster Control Script | Fixed misleading "Latest topology update failed." error in control.sh when a node is unreachable. |
| GG-50105 | Diagnostics and Failure Handling | Fixed configuration consistency check if there is a client with mismatching config in the topology. |
| GG-49833 | Cluster Metrics & Monitoring | Added `cmd=supply-status` REST command. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-50933 | GridGain Integrations | Fixed Kafka sink task recovery on client disconnect. |
| GG-50680 | Cluster Data Snapshots and Recovery | Snapshot transfers over SFTP now verify the backup host's SSH key. |
| GG-50637 | GridGain Integrations | Kafka sink: fixed regression in shallProcessUpdates config property. |
| GG-50499 | Cluster Data Snapshots and Recovery | Failed snapshot deletions are now resumed automatically. |
| GG-50417 | Cluster Data Snapshots and Recovery | Fixed an intermittent failure of snapshot MOVE to an SFTP destination when several nodes created the destination directory concurrently. |
| GG-50241 | Cluster Data Replication | GridGain now sets the upper limit for the amount of memory allocated for DR batches. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Migrating from GridGain 8.9.17 or Earlier With Java 8

Starting GridGain 8.9.18, GridGain uses Lucene 9 by default. As Lucene 9 requires Java 11, it will be impossible to run GridGain on Java 8 with default configuration.

To continue using Java 8 when migrating to GridGain 8.9.18 or later, replace the `{GRIDGAIN_HOME}/libs/ignite-lucene-9` folder with `{GRIDGAIN_HOME}/libs/optional/ignite-lucene-8`.

### Migrating From GridGain 8.9.0

GridGain 8.9.1 introduced a large number of changes in default configuration values. Your setup may be affected if you are using default configuration.

When migrating to GridGain 8.10, make sure to check [Changed Default Values in GridGain 8.9.1 and Later](#changed-default-values-in-gridgain-8.9.1-and-later) section for any parameters you need to change.

{% hint style="danger" %}
Rolling upgrade is only possible if all nodes in the cluster have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. This change affects the service framework used by GridGain, and different framework versions are not compatible. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Migrating From GridGain 8.X

When migrating from GridGain 8.8 to GridGain 8.9, no special actions are required for core functionality migration. By using [rolling upgrades](https://www.gridgain.com/docs/gridgain8/latest/installation-guide/rolling-upgrades), you can update from any GridGain version listed below. You may need to perform minor configuration changes to ensure stability post migration.

{% hint style="info" %}
While updates from GridGain 8.7.X and earlier 8.8.X versions are possible, they may require additional actions to your configuration and  depending on cumulative changes in the version.
{% endhint %}

- If you are using GridGain Enterprise or Ultimate, the `COPY` command was reworked as described in the COPY Command Changes section. The syntax for working with CSV remains the same, but the path is now calculated on the **node** and the client. This change does not affect GridGain Community edition.

  To disable this behavior and use the old copy command, pass the `disabledFeatures=SERVER_BULK_LOAD` parameter in the JDBC connection command:

  ```
  jdbc:ignite:thin://127.0.0.1/?disabledFeatures=SERVER_BULK_LOAD
  ```

- If you are using one of the optional modules listed in the Removed Modules section, they will continue to work, but compatibility and stability on GridGain 8.9 is not guaranteed. Consider using the alternatives:
  - Visor CMD and GUI can be replaced by [GridGain Control Center](https://www.gridgain.com/docs/control-center/latest/overview#system-requirements).
  - The spark module can be replaced by the Spark [Ignite Extension](https://github.com/apache/ignite-extensions).
- If you are using default values in your configuration, you may need to set them manually to keep you cluster working the same way as in previous versions. Make sure to check [Changed Default Values in GridGain 8.9.1 and Later](#changed-default-values-in-gridgain-8.9.1-and-later) section for any parameters you need to change.

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`, `8.9.33`, `8.9.34`, `8.9.35`, `8.9.36`

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Older Thin Clients Compatibility

In most cases, older versions of thin clients should be compatible with newer versions of GridGain.
Below is the list of versions of thin clients that are tested for compatibility with the latest version.
The compatibility also means that you can safely update from any version on the list to any subsequent version.

`8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`, `8.9.33`, `8.9.34`, `8.9.35`, `8.9.36`

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.11.1`, `2.12.0`, `2.13.0`,  `2.14.0`,  `2.15.0`

Apache Ignite thin clients are not compatible with GridGain. When switching to GridGain, follow the [migration instructions](https://www.gridgain.com/docs/gridgain8/latest/installation-guide/migrating-from-ignite) to switch to GridGain clients.

### Known Limitations

#### LEFT OUTER JOIN Behavior Change in GridGain 8.9.31

GridGain 8.9.31 fixes an issue in which the `WHERE` conditions could be incorrectly pushed down into the right branch of LEFT OUTER JOIN operations during query optimization. This optimization could cause queries to return incorrect results by effectively converting `LEFT OUTER JOIN` operations into `INNER JOIN`.

Starting with GridGain 8.9.31, the query optimizer correctly prevents `WHERE` conditions from being pushed down into the right branch of `LEFT OUTER JOIN`, ensuring that queries return the correct results according to SQL standards.

If your environment expects incorrect results, you set the new `DIGNITE_FORCE_PUSHDOWN_CONDITIONS_TO_LEFT_JOIN` system property to `true` on each node in your cluster. Review all affected queries and update them as needed before removing this property.

#### Java 8 Support in GridGain 8.9.18 and Later

Starting GridGain 8.9.18, GridGain uses Lucene 9 by default. As Lucene 9 requires Java 11, it will be impossible to run GridGain on Java 8 with default configuration.

We recommend switching to Java 11 or later before updating to GridGain 8.9.18 or later.

To continue using Java 8, replace the `{GRIDGAIN_HOME}/libs/ignite-lucene-9` folder with `{GRIDGAIN_HOME}/libs/optional/ignite-lucene-8`.

#### Unsupported Features When Using Java 8 in GridGain 8.9.17

In GridGain 8.9.17, full text search is not supported when GridGain is running on Java 8. The new vector search feature requires using Java 11.

Additionally, GridGain 8.9.16 or earlier automatically created full text indexes for caches with string values, which may cause issues for working with the cache while using Java 8. To avoid this behavior, set the `sql.disableCreateLuceneIndexForStringValueType` property to `true`. If such index is already built for a cache with persistence, contact our support team for assistance with removing it.

We recommend switching to Java 11 or later before updating to GridGain 8.9.17 if you plan to use these features.

#### Changed Permissions for Control Center Agent in GridGain 8.9.4 and Later

GridGain 8.9.4 introduced stricter permissions checking for Control Center Agent. When running secured clusters, some actions that previously were available without permissions, will now require additional permissions.

Before updating, make sure to provide the [required permissions](https://www.gridgain.com/docs/control-center/latest/gg8/auth/authorization-permissions), otherwise some actions may become unavailable.

#### New TRACING_CONFIGURATION_UPDATE Permission in GridGain 8.9.2 and Later

GridGain 8.9.2 introduced the `TRACING_CONFIGURATION_UPDATE` [permission](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authorization-permissions). If you were using security on a cluster before updating to this version, make sure that you provide the permissions to control utilities or users who need to update cluster permissions. Otherwise, they will not be able to update

#### Changed Default Values in GridGain 8.9.1 and Later

{% hint style="danger" %}
The change to `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` prevents rolling upgrade from earlier versions to GridGain 8.9.1 unless the value is manually configured to be `false`. For more information on changing service processor implementation, see [Services](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/services/services#new-igniteservices-framework) documentation.
{% endhint %}

If you are updating from GridGain 8.8.X or 8.9.0, a large number of default values have been changed.

These changes may affect the stability or performance of your cluster if you are using default values.

We recommend checking the list below to make sure the changes do not have an adverse effect, and setting the value manually if necessary.

- Service processor now use event-driven implementation by default. You can keep the old behavior by setting the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLE` property to `false`. Make sure that all nodes in the cluster are set to the same value. See [Services](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/services/services#new-igniteservices-framework) documentation for more information.
- Data region metrics are now enabled by default. This may have a minor (within 2%) adverse effect on performance. You can keep the old behavior by setting the `DataRegionConfiguration.metricsEnabled` value to `false`.
- Data storage metrics are now enabled by default. This may have a minor (within 2%) adverse effect on performance. You can keep the old behavior by setting the `DataStorageConfiguration.metricsEnabled` value to `false`.
- `TcpCommunicationSpi` communication protocol now has a limit of 4096 messages for the outgoing messages queue by default.
- Atomic operations are now not allowed in transactions by default. You can keep the old behavior by setting the `IGNITE_ALLOW_ATOMIC_OPS_IN_TX` value to `true`.
- Logs are now in verbose mode by default. You can use the `-q` command line argument in the `ignite.sh` script to keep current log behavior.
- SQL queries are now loaded lazily by default. This reduces memory consumption on medium and large queries and potentially improves garbage collection performance. You can keep the old behavior by setting the `SqlFieldsQuery.setLazy(false)`.
- Cache entries are now read from primary partitions by default, even if an entry is available on the node in a backup partition. This may have a minor performance impact, but significantly increases cluster stability. You can keep the old behavior by setting the `readFromBackup` property to `true`.
- Partition map exchange transactions now time out after 1 minute instead of 0 (infinite) by default. You can keep the old timeout by setting the `TX_TIMEOUT_ON_PARTITION_MAP_EXCHANGE` setting to 0.
- Data streamer now overwrites entries by default. You can keep the old behavior by setting the `stmr.allowOverwrite` property to `false`.
- TCP discovery now uses static IP finder `TcpDiscoveryVmIpFinder` by default. To keep the old behavior, set the IP finder to use [multicast IP finder](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/clustering/tcp-ip-discovery#multicast-ip-finder).
- Checkpointing process now starts upon reaching 75% of `minWalArchiveSize` instead of 25%. You can keep the old behavior by setting the `IGNITE_CHECKPOINT_TRIGGER_ARCHIVE_SIZE_PERCENTAGE` system variable to `0.25`.
