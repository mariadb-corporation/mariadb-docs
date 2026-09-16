---
description: >-
  GridGain 9.1.0 introduces secondary columnar storage, a new JSON license format, reworked node and cluster configuration, and numerous SQL and client improvements.
---

# GridGain 9.1.0 Release Notes

## Overview

GridGain 9.1.0 is a big milestone release with support for new storage type, big license changes and a host of improvements and enhancements.

## Major Changes

### Configuration Changes

This release features a major rework of node and cluster configuration, making configuration names more consistent and reorganizing some parameters.

Below is the summary of the changes:

- Configuration property names now include the units used.
- Multiple system-related properties were combined in `ignite.system` configuration.
- Eviction and expiration configurations are now combined under `ignite.table` configuration.
- Several configuration options were renamed.

Previously used configurations must be updated for this release.

### License Changes

With this release, GridGain 9 license format is changed. Previously issued license keys will continue to work.

New licenses are provided in JSON format, simplifying their usage in REST requests and CLI.

## New Features

### Secondary Columnar Storage

This release brings support for secondary columnar storage. The columnar package is included in the release package.

If columnar storage is enabled, you can use it to store the second instance of data in it, providing a way to search data in columnar format.

To set up columnar storage for your tables:

- Create a new storage profile with `columnar` storage engine:
  ```bash
  node config update "ignite.storage.profiles:{columnar_storage{engine:columnar}}"
  ```

- Restart the node to apply configuration changes.
- Then, include this profile in a distribution zone you use. Distribution zone can also include the storage profile to that will be used to write data:
  ```sql
  CREATE ZONE myZone WITH STORAGE_PROFILES='default, columnar_storage';
  ```

- Create a new table that has a `SECONDARY STORAGE PROFILE` specified and uses columnar storage for it:
  ```sql
  CREATE TABLE Person (  id int primary key,  city_id int,  name varchar,  age int,  company varchar) PRIMARY ZONE MYZONE PRIMARY STORAGE PROFILE 'default' SECONDARY ZONE MYZONE SECONDARY STORAGE PROFILE 'columnar_storage';
  ```

{% hint style="info" %}
In this release, you can only specify secondary storage for new tables. You can also specify separate distribution zones for primary and columnar storage.
{% endhint %}

When data is written to the primary storage, it will automatically be propagated to secondary storage. To read data from columnar storage, use the `use_secondary_storage` query hint:

```sql
SELECT /*+ use_secondary_storage */ * FROM Person;
```

For more information on columnar storage, see [Columnar Storage](../../administrators-guide/storage/engines/columnar.md) documentation.

### Streamer Support in Kafka Sink

Kafka Sink now supports receiving data via [data streamer](../../developers-guide/data-streamer.md).

To enable data streamer support, specify the name of the receiver class in the `ignite.streamer.receiver.class.name` kafka sink configuration property. You can specify the deployment units containing the class in the `ignite.streamer.receiver.deployment.units` property.

### Expanded COPY INTO Syntax

The [COPY INTO](../../sql-reference/operational-commands.md#copy-into) command syntax is expanded with new optional parameters that help support importing data from CSV files with various syntax rules. The following parameters were added:

- `quoteChar` - defines the quote character;
- `escapeChar` - defines the character to use for escaping a separator or quote;
- `ignoreLeadingWhiteSpace` - defines if leading whitespace are ignored;
- `ignoreQuotations` - defines if quoted elements are ignored;
- `strictQuotes` - defines if characters outside the quoted elements are ignored.

These parameters can be specified in the `WITH` clause, for example:

```sql
COPY FROM '/path/to/dir/data.csv'
INTO Table1 (name, age)
FORMAT CSV
WITH 'quoteChar'='~'
```

### Expanded Continuous Queries

Continuous query API was expanded with new properties:

- The `TableRowEventBatch#watermark` property can be used to create a watermark that can be used to continue the continuous query from the specific batch of data in case of interrupted connection or other issues.
- The `ContinuousQueryOptions#enableEmptyBatches`, if set to `true`, allows empty batches in continuous queries. These batches will be sent only when there is no load, and can be used to update the watermark.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-27635 | Platforms and Clients | Fixed potential deadlock in data streamer. |
| IGN-27381 | General | Low watermark update is no longer paused while table is being deleted. |
| IGN-27347 | SQL | Table identifier can now correctly start with underscore without being enclosed in quote symbols. |
| IGN-27278 | General | Fixed an issue that could lead to a race when destroying partitions, and to failure to create indexes. |
| IGN-27255 | Distributed Computing | Code deployment now supports files over 10 MB. |
| IGN-27189 | General | Fixed an issue that could cause catalog compaction to hang. |
| IGN-27171 | Platforms and Clients | .NET: Fixed OperationCanceledException in client log on graceful disconnect. |
| IGN-27109 | SQL | Added pk_column_ordinal and colocation_column_ordinal columns to table_columns system view. |
| IGN-27049 | General | Fixed a warning in log that could happen at the end of data rebalance. |
| IGN-26934 | SQL | Fixed a serialization issue in Java client that could prevent users from working with columns that contain special symbols. |
| IGN-26932 | General | Added the bytesValue method to table api. |
| IGN-26898 | SQL | Improved error message when DEFAULT column is specified incorrectly. |
| IGN-26598 | SQL | .NET: Added ITable.QualifiedName API. |
| IGN-25152 | General | Public error code numbers updated to keep numbers continuous. |
| IGN-25150 | General | A new STORAGE_BROKEN error code was added. |
| IGN-24817 | Configuration | Renamed idleSyncTimeInterval configuration to idleSafeTimeSyncInterval, and it is now part of ignite.system configuration. |
| IGN-24813 | Configuration | Moved the ignite.storageUpdate.batchByteLength configuration to ignite.replication.raft.batchSizeBytes. |
| IGN-24811 | Configuration | Configuration parameters now include the value used. |
| IGN-24810 | Configuration | The ignite.compute.threadPoolStopTimeoutMillis configuration was removed. |
| IGN-24808 | Configuration | The criticalWorkers configuration is now part of ignite.system configuration. |
| IGN-24807 | Configuration | The ignite.deploymentLocation is renamed to ignite.location. |
| GG-43206 | SQL | New optional parameters were added to the COPY INTO SQL command. |
| GG-43197 | General | Continuous Query: added TableRowEventBatch#watermark and ContinuousQueryOptions#enableEmptyBatches properties. |
| GG-43139 | SQL | COPY FROM command now works correctly when column names are quoted. |
| GG-42858 | Cluster Storage Engine | Removed duplicated log line on node start. |
| GG-42822 | Cluster Data Snapshots and Recovery | Reduced memory requirements for snapshot operations. |
| GG-42771 | General | Added docker images for arm64 architecture. |
| GG-42764 | General | Python DB API can now be used on Windows. |
| GG-42612 | CLI Tool | The new --license parameter must be used when initializing the cluster. |
| GG-42398 | Licenses | License format is changed. |
| GG-42135 | GridGain Integrations | Kafka sink: added streamer receiver support. |
| GG-41691 | SQL | A correct error message is now posted if a non-existing table or column is used in the COPY FROM query. |

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### Data Center Replication With Complex Topologies

Complex Data Center Replication topologies (for example, the ones involving cycles) of 3 or more data centers are not supported. This will be addressed in an upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
