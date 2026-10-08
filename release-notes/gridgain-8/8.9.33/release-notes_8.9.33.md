---
description: >-
  GridGain 8.9.33 introduces an OpenTelemetry metrics exporter, tunable binary configuration for the JDBC thin driver, SWID tags in release packages, and S3-compatible storage support for COPY INTO.
hidden: true
---

# GridGain 8.9.33 Release Notes

## Overview

GridGain 8.9.33 introduces an OpenTelemetry metrics exporter, tunable binary configuration for the JDBC thin driver, SWID tags in release packages, and S3-compatible storage support for the COPY INTO command, alongside stability fixes and dependency updates.

## Major Changes

### Optional AWS Credentials

Starting with this release, S3 credentials for the `COPY INTO` command are optional. If you omit the `s3.access-key-id` and `s3.secret-access-key` properties, GridGain uses the default AWS credentials provider chain (environment variables, Java system properties, the credentials profile file, or the container/instance IAM role). Previously, both properties were required to access S3 storage. Commands that specify both properties are unaffected.

## New Features

### Tunable Binary Configuration in JDBC Driver

With this release, you can align the JDBC thin driver's `BinaryConfiguration` with the server when custom binary name or ID mappers are in use. Three new JDBC URL parameters control how binary types are resolved on the client side:

- `useLowerCaseForBinaryTypes` (boolean) - lowercase binary type and field names during ID resolution.
- `useSimpleNamesForBinaryTypes` (boolean) - use simple (unqualified) class names for binary type name resolution.
- `binaryConfigurationFactory` (FQCN) - class name of a `Factory<BinaryConfiguration>` that produces the connection's binary configuration.

`binaryConfigurationFactory` is mutually exclusive with the two flag parameters; combining them fails connection establishment with `SQLException`. Defaults preserve prior behavior.

Example usage:

```text
jdbc:ignite:thin://host:10800?useLowerCaseForBinaryTypes=true&useSimpleNamesForBinaryTypes=true
```

For more information about JDBC connection parameters, see the [JDBC Thin Driver](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/SQL/JDBC/jdbc-driver) documentation.

### OpenTelemetry Metrics Exporter

With this release, you can use the new [OpenTelemetry](https://opentelemetry.io/docs/specs/otlp/) metrics exporter.

To use the OpenTelemetry exporter:

- [Enable the 'ignite-opentelemetry' module](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/setup#enabling-modules).
- Add `org.apache.ignite.spi.metric.otlp.OpenTelemetryMetricExporterSpi` to the list of exporters in the node configuration.
- Configure OpenTelemetry exported to send metrics to your endpoint.

Example usage:

```java
IgniteConfiguration cfg = new IgniteConfiguration();

OpenTelemetryMetricExporterSpi otelExporter = new OpenTelemetryMetricExporterSpi();
otelExporter.setEndpoint("http://my-endpoint:4317");
otelExporter.setProtocol(Protocol.GRPC);
otelExporter.setCompression(Compression.GZIP);
otelExporter.setPeriod(30_000L);
otelExporter.setServiceNamespace("my-org");
otelExporter.setServiceName("ignite-cluster");
//export cache metrics only
otelExporter.setExportFilter(mreg -> mreg.name().startsWith("cache."));

cfg.setMetricExporterSpi(otelExporter);
```

For more information about OpenTelemetry exporter, see [Metric Exporters](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/monitoring-metrics/generic-metrics#opentelemetry) section.

### SWID Tags

GridGain release packages now ship with Software Identification (SWID) tag.

The tag is included in every release archive under the `swidtag/` directory, and is additionally placed at the standard system location `/usr/share/swidtag/` in Docker images. Each edition ships its own tag, with a unique tag ID following the pattern `com.gridgain.<edition>_<version>` (for example, `com.gridgain.ultimate_8.9.33`).

### S3-Compatible Storage Support for COPY INTO

With this release, the `COPY INTO` command can import and export data using S3-compatible object stores, such as MinIO or LocalStack, in addition to AWS S3. Set the new `s3.endpoint` property to the endpoint URL of your service.

The example below shows importing a CSV file from an S3-compatible endpoint.

```sql
COPY FROM 's3://mybucket/data.csv'
INTO Table1(name, age)
FORMAT CSV
PROPERTIES('s3.client-region' = 'eu-central-1', 's3.endpoint' = 'https://s3.example.com')
```

For more information, see the [Operational Commands](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/operational-commands) documentation.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-47851 | Cluster Compute Grid | Fixed long job activation in PriorityQueueCollisionSpi. |
| GG-47568 | Cluster Discovery | Fixed a coordinator deadlock that could occur when a WAL mode change ran concurrently with cache update operations. |
| GG-43609 | Cluster Compute Grid | Improved PriorityQueueCollisionSpi performance under high concurrency. |
| GG-38703 | Binary Objects | Introduced new connection params for fine-grained tuning of binary configuration on JDBC client side. |
| GG-30260 | Cluster Metrics & Monitoring | Added OpenTelemetry metrics exporter. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-48158 | Builds and Deliveries | Updated aircompressor to version 2.0.3. |
| GG-47877 | Builds and Deliveries | Updated log4j from version 2.25.3 to version 2.25.4. |
| GG-47858 | Cluster SQL Engine | COPY INTO now supports S3-compatible object stores (new `s3.endpoint` property) and optional S3 credentials. |
| GG-46864 | General | Added SWID tags to release packages. |
| GG-46305 | Cluster Storage Engine | Introduced a new system property: IGNITE_PARTITION_CALCULATION_STRATEGY that allows defining a strategy for calculating a partition index for batch atomic operations. |
| GG-42930 | Cluster Data Replication | The "dr pause" control script command now affects all the senders when pausing replication to a particular datacenter. |
| GG-38770 | Cluster Control Script | The control.sh --meta commands now display the affinity key field name for binary types. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-42609 | Cluster Data Snapshots and Recovery | GridGain will now automatically attempt to recover on CRC exception during snapshot creation. |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-47386 | Control Center Agent | The Control Center Agent now sends snapshot size and compression options as part of snapshot information. |

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

`8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Older Thin Clients Compatibility

In most cases, older versions of thin clients should be compatible with newer versions of GridGain.
Below is the list of versions of thin clients that are tested for compatibility with the latest version.
The compatibility also means that you can safely update from any version on the list to any subsequent version.

`8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`

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
