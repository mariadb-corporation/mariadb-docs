---
description: >-
  GridGain 9.1.15 brings multiple improvements and support for snapshots of data
  structures, drops support for table-based partition colocation, and updates the
  supported Python versions.
---

# GridGain 9.1.15 Release Notes

## Overview

GridGain 9.1.15 is a private release that brings multiple improvements and support for snapshots of data structures.

## Major Changes

### Partition Colocation

With this release, partition table-based partition colocation is no longer supported. This behavior was deprecated since GridGain 9.1.4.

For clusters created on GridGain 9.1.3 or earlier, or for clusters where `IGNITE_ZONE_BASED_REPLICATION` property was set to `false` (default is `true`), it is now required to manually recreate the cluster and migrate data to it.

For clusters with default colocation settings created on GridGain 9.1.4 or later, no additional actions are required.

### Supported Python Versions

In this release, support for Python 3.9 was dropped and support for Python 3.14 was added in [Python client](../../developers-guide/clients/python-client.md) and [Python DB API](../../developers-guide/clients/python.md).

If you are using Python 3.9, make sure to update to 3.10 or later.

## New Features

### Structure Snapshots

[Data snapshots](../../administrators-guide/snapshots/snapshots-and-recovery.md) now support creating snapshots of [distributed maps](../../developers-guide/data-structures/map-structure.md) and [sequences](../../developers-guide/sql/sql-api.md#using-sequences). When a snapshot is created for a table, any data structures required for it are included in the snapshot automatically. You can also use the new `--structures` parameter to explicitly specify the data structures that you want to include in the snapshot, for example:

```bash
cluster snapshot create --type=full --tables=PERSON --structures=personStruct --destination=relative-path-example
```

### Default Query Staleness Configuration

Since GridGain 9.1.11, you could [configure data staleness](../../sql-reference/ddl.md#create-table) for individual tables. This release improves support for query configuration by providing a way to set it in [cluster-wide SQL configuration](../../administrators-guide/config/cluster-config.md#sql-configuration). The new `minStaleRowsCount` and `staleRowsFraction` allow you to configure the number or row updates since last plan recalculation and the fraction of the table respectively.

You can configure these parameters from the CLI tool, for example:

```bash
cluster config update ignite.sql.createTable.minStaleRowsCount=1000
```

### Ignored Fields in DR Connector

When configuring [data center replication from GridGain 8](../../migration-from-gg-8/dcr-from-gg8.md), you can now configure ignored key fields. The configuration mirrors the previously available configuration for value fields. The example below shows a minimal configuration that ignores fields K4 and V4.

```
dr-service-config = {
  cacheMapping = [
    {
      cache = "cacheName"
      table = "schemaName.tableName"
      keyFields = [
        { field = "K1", column = "COL_1" }
        { field = "K2", column = "COL_2" }
        { field = "K3", column = "COL_3" }
        { field = "K4", column = "ignored_column", ignore = true }
      ]
      valueFields = [
        { field = "V1", column = "COL_4" }
        { field = "V2", column = "COL_5" }
        { field = "V3", column = "COL_6" }
        { field = "V4", column = "ignored_column", ignore = true }
      ]
    }
  ]
}
```

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-29469 | Cluster Storage Engine | Reduced the volume of compactor log messages. |
| IGN-29451 | General | Fixed a rare failure during partition re-encryption after the encryption key update. |
| IGN-29441 | General | Failure handler is no longer called for raft snapshots when a node leaves the cluster. |
| IGN-29415 | Cluster SQL Engine | Condition with LIKE operator is now supported in index scan if pattern represents a prefix search. |
| IGN-29400 | CLI Tool | Updated progressbar library from version 0.9.4 to version 0.10.0. |
| IGN-29393 | Cluster SQL Engine | Fixes an issue with a rare resource leak on query cancellation. |
| IGN-29385 | Cluster Storage Engine | Private information in cluster configuration is no longer printed into logs during cluster initialization. |
| IGN-29383 | Cluster Storage Engine | Fixed an issue that could cause an exception when index was dropped before the table. |
| IGN-29355 | General | Non-colocated data storage is no longer supported. |
| IGN-29306 | Cluster SQL Engine | Fixed an issue that caused certain join operations to return incorrect results. |
| IGN-29288 | General | Fixed critical system error "Causality token mismatch". |
| IGN-29265 | Platforms & Clients | Java client: Fixed SQL ResultSet prefetch logic to avoid exceptions on close, prefetch in sync and async modes. |
| IGN-28954 | General | Reduced latency and improved throughput for implicit getAll/containsAll table operations, initiated from a client. |
| IGN-28815 | Cluster SQL Engine | You can now override default staleness configuration for tables. |
| IGN-28402 | Cluster SQL Engine | GridGain now rebuilds cached plans periodically based on data changes. |
| IGN-27770 | Distributed Computing | .NET: Improve error message when job assembly load has failed due to runtime version mismatch. |
| IGN-27092 | Platforms and Clients | Java client: fixed IllegalStateException in retry/failover logic. |
| GG-46320 | Cluster Data Snapshots and Recovery | Fixed NPE when restoring snapshots created before 9.1.10 without any tables selected. |
| GG-46130 | General | Versions <= 9.1.3 are no longer compatible with new versions. New error code UNSUPPORTED_TABLE_BASED_REPLICATION_ERR introduced. |
| GG-46122 | Cluster SQL Engine | Fixed compatibility with GridGain 9.1.12 and earlier. |
| GG-46059 | Platforms & Clients | C++ Client: Added missing files to the package. |
| GG-45910 | Cluster Rolling Upgrade | Point-in-time recovery is now disabled during rolling upgrade. |
| GG-45776 | Platforms & Clients | Python Client: Added support for Python 3.14 and removed support for Python 3.9. |
| GG-45507 | Cluster Data Snapshots and Recovery | Added CLI api for creating and restoring snapshots containing structures, sequences, and maps. |
| GG-45046 | Cluster SQL Engine | You can now ignore fields in DR Connector configuration. |
| GG-43415 | Cluster Continuous Queries | Continuous Query: fixed query failure in certain cases when one key is created and removed within a single transaction. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`, `9.1.12`, `9.1.13`, `9.1.14`

{% hint style="warning" %}
When performing a rolling upgrade from GridGain 9.1.8 or 9.1.9, it is required to update to 9.1.10 first.
{% endhint %}

When updating from older versions, we recommend updating to version `9.1.8` first, before performing an update to current version.

## Known Limitations

### Rolling Upgrade Over 9.1.10

When performing a rolling upgrade from GridGain 9.1.9 or earlier, it is necessary to first upgrade to 9.1.10 before upgrading to 9.1.11 or a later version. This is caused by improvements in rolling upgrade procedure that make skipping 9.1.10 with a rolling upgrade impossible.

The upgrade to 9.1.10 must be performed for the whole cluster and committed before the next upgrade can be started.

You do not need to perform this intermediary upgrade when upgrading with downtime, as it only affects the rolling upgrade procedure.

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
