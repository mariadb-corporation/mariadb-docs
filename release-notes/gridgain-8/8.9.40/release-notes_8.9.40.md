---
description: >-
  GridGain 8.9.40 merges binary metadata by field ID, adds bulk cache removal to the .NET thin client and a DR sender metric, and fixes security and DR issues.
  Released on 2026-11-19.
---

# GridGain 8.9.40 Release Notes

**Release date:** 19 Nov 2026

## Overview

GridGain 8.9.40 adds a method that destroys several caches in one request to the .NET thin client and a data center replication metric for unacknowledged batches.

## New Features

### Destroying Several Caches From the .NET Thin Client

The .NET thin client has a new `IIgniteClient.DestroyCaches` method. It destroys all listed caches in a single request, which causes less cluster-wide work than destroying the caches one by one. For details, see the [.NET Thin Client]({connectors}/gridgain-8/clients/dotnet-thin-client#destroying-caches) documentation.

### DR Sender Metric for Unacknowledged Batches

The DR sender hub has a new `OldestUnacknowledgedBatchAge` metric: the age, in milliseconds, of the oldest batch sent to the receiver hubs and not acknowledged yet. A value that keeps growing means the receiver hubs are not acknowledging batches, so the sender storage cannot be cleaned up. For details, see the [Generic Metrics]({gridgain8}/reference/monitoring/generic-metrics#sender-metrics) documentation.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| GG-53210 | Cluster Deployment | Fixed an issue with the `GRACEFUL` shutdown policy where nodes that had left the cluster and client nodes were counted as stopping nodes when a server node checked whether it could stop safely. |
| GG-53055 | Cluster Security | Fixed an SQL DDL injection through an unescaped double quote in a cache schema, table, field, or index name. A client that could create a cache could use it to run arbitrary H2 statements on the server. |
| GG-52988 | Builds and Deliveries | The `ignite-gce` module now includes Guava, so the GCE IP finder no longer fails with `NoClassDefFoundError`. |
| GG-52973 | Platforms & Thin Clients | Java thin client: Fixed a possible `NullPointerException` in the retry logic. |
| GG-52969 | Diagnostics and Failure Handling | Rebalance and PME log messages now list partitions individually instead of as ranges. |
| GG-52951 | Platforms & Thin Clients | .NET: Added `IIgniteClient.DestroyCaches`, which destroys several caches in a single request. |
| GG-52881 | Platforms & Thin Clients | .NET: Fixed an issue where the thin client data streamer `Flush()` sometimes completed without an error even though the flush failed. |
| GG-52718 | Platforms & Thin Clients | Thin clients: Improved the performance of cache operations when the cluster has many caches. |
| GG-52664 | Binary Objects | Binary metadata is now merged by field ID instead of field name, so field names that differ only in case denote the same field. Use the new `IGNITE_BINARY_METADATA_MERGE_BY_FIELD_ID_FEATURE` system property to turn this off. |
| GG-52214 | Cluster Security | Thin clients: Fixed a security issue where continuous query remote filters passed by class name were not checked against `IGNITE_MARSHALLER_WHITELIST` and `IGNITE_MARSHALLER_BLACKLIST`. |
| GG-53105 | Cluster Data Replication | Added the `OldestUnacknowledgedBatchAge` DR sender hub metric. |
| GG-53046 | GridGain Integrations | Kafka connector: The source task now recovers from Ignite client disconnects. |
| GG-52691 | Cluster Data Replication | Fixed an issue where transactional caches relayed updates received from other clusters even when `GG_DR_DISABLE_TRANSITIVE_UPDATES` was enabled. |

## Installation and Upgrade Information

See the [Rolling Upgrades]({gridgain8}/gridgain8-management/installation/upgrade/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

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

When migrating from GridGain 8.8 to GridGain 8.9, no special actions are required for core functionality migration. By using [rolling upgrades]({gridgain8}/gridgain8-management/installation/upgrade/rolling-upgrades), you can update from any GridGain version listed below. You may need to perform minor configuration changes to ensure stability post migration.

{% hint style="info" %}
While updates from GridGain 8.7.X and earlier 8.8.X versions are possible, they may require additional actions to your configuration and  depending on cumulative changes in the version.
{% endhint %}

- If you are using GridGain Enterprise or Ultimate, the `COPY` command was reworked as described in the COPY Command Changes section. The syntax for working with CSV remains the same, but the path is now calculated on the **node** and the client. This change does not affect GridGain Community edition.

  To disable this behavior and use the old copy command, pass the `disabledFeatures=SERVER_BULK_LOAD` parameter in the JDBC connection command:

  ```
  jdbc:ignite:thin://127.0.0.1/?disabledFeatures=SERVER_BULK_LOAD
  ```

- If you are using one of the optional modules listed in the Removed Modules section, they will continue to work, but compatibility and stability on GridGain 8.9 is not guaranteed. Consider using the alternatives:
  - Visor CMD and GUI can be replaced by [GridGain Control Center]({tools}/enterprise/control-center#system-requirements).
  - The spark module can be replaced by the Spark [Ignite Extension](https://github.com/apache/ignite-extensions).
- If you are using default values in your configuration, you may need to set them manually to keep you cluster working the same way as in previous versions. Make sure to check [Changed Default Values in GridGain 8.9.1 and Later](#changed-default-values-in-gridgain-8.9.1-and-later) section for any parameters you need to change.

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.9.0`, `8.9.1`, `8.9.5`, `8.9.8`, `8.9.9`, `8.9.12`, `8.9.13`, `8.9.14`, `8.9.14-p2`, `8.9.15`, `8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.20-p2`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.23-p1`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`, `8.9.33`, `8.9.33-p1`, `8.9.34`, `8.9.35`, `8.9.36`, `8.9.37`, `8.9.38`, `8.9.39`

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Older Thin Clients Compatibility

In most cases, older versions of thin clients should be compatible with newer versions of GridGain.
Below is the list of versions of thin clients that are tested for compatibility with the latest version.
The compatibility also means that you can safely update from any version on the list to any subsequent version.

`8.9.0`, `8.9.1`, `8.9.5`, `8.9.8`, `8.9.9`, `8.9.12`, `8.9.13`, `8.9.14`, `8.9.14-p2`, `8.9.15`, `8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.20-p2`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.23-p1`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`, `8.9.33`, `8.9.33-p1`, `8.9.34`, `8.9.35`, `8.9.36`, `8.9.37`, `8.9.38`, `8.9.39`

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.11.1`, `2.12.0`, `2.13.0`,  `2.14.0`,  `2.15.0`,  `2.16.0`,  `2.17.0`,  `2.18.0`

Apache Ignite thin clients are not compatible with GridGain 8.9. When switching to GridGain, follow the [migration instructions]({gridgain8}/gridgain8-management/migration-guides/apache-ignite-2x-8.9) to switch to GridGain clients, or use GridGain 8.10.

### Known Limitations

#### Binary Metadata Merged by Field ID in GridGain 8.9.40

Starting with GridGain 8.9.40, binary metadata is merged by field ID. The default ID mapper ignores case, so the cluster rejects a field whose name differs from an existing field name only in case, if it has a different type. Such a write fails with a `BinaryObjectException` or, for `ALTER TABLE ... ADD COLUMN`, an `IgniteSQLException` that names both fields and their types. The new behavior applies only when all nodes in the cluster run GridGain 8.9.40 or later.

To keep merging by field name, set the `IGNITE_BINARY_METADATA_MERGE_BY_FIELD_ID_FEATURE` system property to `false` on one of the cluster nodes. While any node has this property set to `false`, the whole cluster merges by field name. For details on fixing the data model, see the [Troubleshooting]({gridgain8}/tuning-and-troubleshooting/troubleshooting#field-type-conflict-between-field-names-that-differ-in-case) documentation.

#### Thin Client Continuous Query Filters Checked in GridGain 8.9.40

Starting with GridGain 8.9.40, remote filters that a thin client passes by class name for a continuous query are checked against `IGNITE_MARSHALLER_WHITELIST` and `IGNITE_MARSHALLER_BLACKLIST`. A filter class that the lists do not allow fails with `Deserialization of class <class name> is disallowed.` If you use `IGNITE_MARSHALLER_WHITELIST`, add the remote filter classes of your thin client continuous queries to the whitelist before upgrading.

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

Before updating, make sure to provide the [required permissions]({tools}/enterprise/control-center/gg8/authorization-permissions), otherwise some actions may become unavailable.

#### New TRACING_CONFIGURATION_UPDATE Permission in GridGain 8.9.2 and Later

GridGain 8.9.2 introduced the `TRACING_CONFIGURATION_UPDATE` [permission]({gridgain8}/security/authentication-and-authorization/authorization-permissions). If you were using security on a cluster before updating to this version, make sure that you provide the permissions to control utilities or users who need to update cluster permissions. Otherwise, they will not be able to update

#### Changed Default Values in GridGain 8.9.1 and Later

{% hint style="danger" %}
The change to `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` prevents rolling upgrade from earlier versions to GridGain 8.9.1 unless the value is manually configured to be `false`. For more information on changing service processor implementation, see [Services]({gridgain8}/gridgain8-development/distributed-computing-and-services/services#new-igniteservices-framework) documentation.
{% endhint %}

If you are updating from GridGain 8.8.X or 8.9.0, a large number of default values have been changed.

These changes may affect the stability or performance of your cluster if you are using default values.

We recommend checking the list below to make sure the changes do not have an adverse effect, and setting the value manually if necessary.

- Service processor now use event-driven implementation by default. You can keep the old behavior by setting the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLE` property to `false`. Make sure that all nodes in the cluster are set to the same value. See [Services]({gridgain8}/gridgain8-development/distributed-computing-and-services/services#new-igniteservices-framework) documentation for more information.
- Data region metrics are now enabled by default. This may have a minor (within 2%) adverse effect on performance. You can keep the old behavior by setting the `DataRegionConfiguration.metricsEnabled` value to `false`.
- Data storage metrics are now enabled by default. This may have a minor (within 2%) adverse effect on performance. You can keep the old behavior by setting the `DataStorageConfiguration.metricsEnabled` value to `false`.
- `TcpCommunicationSpi` communication protocol now has a limit of 4096 messages for the outgoing messages queue by default.
- Atomic operations are now not allowed in transactions by default. You can keep the old behavior by setting the `IGNITE_ALLOW_ATOMIC_OPS_IN_TX` value to `true`.
- Logs are now in verbose mode by default. You can use the `-q` command line argument in the `ignite.sh` script to keep current log behavior.
- SQL queries are now loaded lazily by default. This reduces memory consumption on medium and large queries and potentially improves garbage collection performance. You can keep the old behavior by setting the `SqlFieldsQuery.setLazy(false)`.
- Cache entries are now read from primary partitions by default, even if an entry is available on the node in a backup partition. This may have a minor performance impact, but significantly increases cluster stability. You can keep the old behavior by setting the `readFromBackup` property to `true`.
- Partition map exchange transactions now time out after 1 minute instead of 0 (infinite) by default. You can keep the old timeout by setting the `TX_TIMEOUT_ON_PARTITION_MAP_EXCHANGE` setting to 0.
- Data streamer now overwrites entries by default. You can keep the old behavior by setting the `stmr.allowOverwrite` property to `false`.
- TCP discovery now uses static IP finder `TcpDiscoveryVmIpFinder` by default. To keep the old behavior, set the IP finder to use [multicast IP finder]({gridgain8}/gridgain8-management/cluster-configuration/clustering/tcp-ip-discovery#multicast-ip-finder).
- Checkpointing process now starts upon reaching 75% of `minWalArchiveSize` instead of 25%. You can keep the old behavior by setting the `IGNITE_CHECKPOINT_TRIGGER_ARCHIVE_SIZE_PERCENTAGE` system variable to `0.25`.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
