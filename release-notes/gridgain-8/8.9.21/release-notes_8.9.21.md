---
description: >-
  GridGain 8.9.21 is a maintenance release that improves data center replication monitoring and product stability.
hidden: true
---

# GridGain 8.9.21 Release Notes

## Overview

GridGain 8.9.21 is a maintenance release that improves data center replication monitoring and product stability.

## New Features

### Improved DR Monitoring

The [data replication events](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/data-center-replication/managing-and-monitoring#data-replication-events) were expanded to provide a way to track activity and verify that the updates were sent and received successfully. The following events were added:

- EVT_DR_RECEIVER_UPDATE_RECEIVED
- EVT_DR_RECEIVER_UPDATE_ACKED
- EVT_DR_RECEIVER_UPDATE_APPLIED
- EVT_DR_RECEIVER_UPDATE_FAILED
- EVT_DR_SENDER_UPDATE_SENT
- EVT_DR_SENDER_UPDATE_ACKED
- EVT_DR_SENDER_UPDATE_FAILED

For more information about tracking data center replication, see [data replication events](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/data-center-replication/managing-and-monitoring#data-replication-events)

## Known Issues

### Snapshot Compression Requires Extra Space

Due to changes in release 8.9.18 compression is only started after the snapshot data is fully gathered. This means that to create a snapshot GridGain needs as much free space as the size of the data that will be compressed.

The extra space is only required to start the snapshot process, the snapshots will be compressed correctly if the space is available.

{% hint style="info" %}
Caches that use [Transparent Data Encryption](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/tde) are not affected.
{% endhint %}

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-43685 | General | Updated commons-beanutils dependency from 1.9.4 to 1.11.0. |
| GG-43602 | Platforms & Thin Clients | .NET: Added support for decimal values with negative scale, such as `1.12E+1`, which is `1.12 scale -1` in Java BigDecimal, and is equivalent to `11.2`. |
| GG-43529 | REST | Fixed path handling in GridLogCommandHandler. |
| GG-43271 | Cluster Storage Engine | Fixed an issue in copying partition meta information during defragmentation for caches created on GridGain 8.7.31 or earlier. |
| GG-42289 | Cluster Data Replication | Fixed FST list control.sh command failure that happened when too many FST tasks were scheduled. |
| GG-41981 | Cluster SQL Engine | Fixed an issue that caused parts of queries to continue execution even when cancelled if no resources were available for cancellation. |
| GG-40393 | Binary Objects | Fixed an issue that caused binary configuration to sometimes be ignored after client reconnect. |
| GG-39574 | Cluster Storage Engine | Inline index size is now limited to 427 bytes. Warning will be logged if existing indexes exceed this value |
| GG-38512 | Cluster Storage Engine | Improved eviction of large cache entries from in-memory data regions. |
| GG-38389 | Cluster Storage Engine | Fixed an issue that could lead to hanging PME when the FSYNC WAL mode was enabled. |
| GG-36398 | Binary Objects | Fix inconsistent behaviour of SimpleNameMapper. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-43691 | General | Updated commons-beanutils dependency from 1.9.4 to 1.11.0. |
| GG-43684 | General | Updated Apache Parquet dependency from 1.15.1 to 1.15.2. |
| GG-42397 | Cluster Data Replication | Added events for transferring DR updates on sender and receiver nodes. |
| GG-41459 | Cluster Data Replication | Expanded trace-level logs for tracking progress of data center replication. |
| GG-40042 | Cluster Data Replication | Fixed a NPE that could be triggered by an update of tombstone.ttl distributed property. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-43152 | Cluster Data Snapshots and Recovery | Fix a rare NotSerializableException that happened on restoring data from a snapshot. |

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

`8.8.4`, `8.8.13`, `8.8.18`, `8.8.22`, `8.8.24`, `8.8.27`, `8.8.30`, `8.8.37`, `8.8.39`, `8.8.43`, `8.8.44`, `8.9.0`, `8.9.1`, `8.9.5`, `8.9.8`, `8.9.9`, `8.9.12`, `8.9.13`, `8.9.14`, `8.9.15`, `8.9.16`, `8.9.16-p1`, `8.9.17`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.21`

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.11.1`, `2.12.0`, `2.13.0`,  `2.14.0`,  `2.15.0`

### Known Limitations

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
