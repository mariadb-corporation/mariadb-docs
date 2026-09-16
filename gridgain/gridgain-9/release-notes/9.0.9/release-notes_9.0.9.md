---
description: >-
  GridGain 9.0.9 changes CREATE TABLE syntax and adds extended system views, a
  Kafka sink connector, and disaster recovery for system RAFT groups.
---

# GridGain 9.0.9 Release Notes

## Overview

GridGain 9.0.9 is a release that continues work on stability and performance while also bringing new and exciting features.

## Major Changes

### CREATE TABLE Syntax Change

In this release, the SQL `CREATE TABLE` and `CREATE CACHE` command is changed. The `WITH` clause is removed, and the parameters previously specified in it are now part of common syntax:

- `PRIMARY_ZONE` is now specified as `ZONE` or `PRIMARY ZONE`:

  ```sql
  CREATE TABLE IF NOT EXISTS Person (
    id int primary key,
    city_id int,
    name varchar,
    age int,
    company varchar
  ) PRIMARY ZONE MYZONE
  ```

- `STORAGE_PROFILE` is now specified as `PROFILE`:

  ```sql
  CREATE TABLE IF NOT EXISTS Person (
    id int primary key,
    city_id int,
    name varchar,
    age int,
    company varchar
  ) PRIMARY ZONE MYZONE STORAGE PROFILE 'default'
  ```

The functionality of these commands remains the same. For a visual representation of the `CREATE TABLE` command, see [DDL Reference](../../sql-reference/ddl.md#create-table).

### Extended System Views

This release provides multiple new system view, extending information that is readily available. The following new system views were added:

- `COMPUTE_JOBS` - provides information about running compute jobs.
- `TRANSACTIONS` - provides information about currently active transactions.
- `SQL_QUERIES` - provides information about currently running queries.

Additionally, the `GLOBAL_PARTITION_STATES` and `LOCAL_PARTITION_STATES` system views were extended with `TABLE_ID` and `SCHEMA_NAME` fields.

### Kafka Sink Connector

A new GridGain 9 Kafka Sink connector can be used to copy data from Kafka topics to GridGain 9 tables.

GridGain 9 Sink connector features multiple improvements over its GridGain 8 counterpart:

- Kafka-style configuration for all sink properties.
- Arbitrary mapping of Kafka topics to GridGain tables.
- No additional steps are required to prepare GridGain for working with Kafka.

For more information about Kafka Sink connector, see the [Kafka Sink Connector](../../extensions/kafka-sink.md) topic.

### Metastore and CMG Majority Loss Recovery

You can now perform [disaster recovery for system RAFT groups](../../administrators-guide/system-groups-recovery.md) that are essential for the GridGain 9 cluster's normal operation:

- [Cluster Management Group (CMG)](../../administrators-guide/lifecycle.md#cluster-management-group)
- [Metastorage Group (MG)](../../administrators-guide/lifecycle.md#cluster-metastorage-group)

You perform disaster recovery operations on system RAFT groups when a permanent majority loss occurs. Once you have detected that majority has been lost in cluster logs in the console or in the [rotated log files](https://en.wikipedia.org/wiki/Log_rotation), you can use the [CLI commands](../../ignite-cli-tool.md#disaster-recovery-commands) or REST API calls to perform disaster recovery

### Cluster-Wide Metrics Configuration

Prior to this release, [metrics](../../administrators-guide/metrics/configuring-metrics.md) were configured on a per-node basis. Now, you can use the new cluster-wide CLI commands to manage your metrics for the entire cluster, for example:

```bash
cluster metric source enable jvm
```

### Significant Performance and Stability Improvements

This release features significant internal changes and improvements. In-cluster connectivity was significantly improved, and multiple performance bottlenecks were removed, providing a noticeable increase in overall cluster performance.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-25954 | General | IGNITE3_EXTRA_JVM_ARGS environment variable is now available in docker images. |
| IGN-25940 | General | Added TABLE_ID and SCHEMA_NAME fields to GLOBAL_PARTITION_STATES and LOCAL_PARTITION_STATES system views. |
| IGN-25764 | SQL | A new SQL_QUERIES system view was added. |
| IGN-25763 | General | A new TRANSACTIONS system view was added. |
| IGN-25755 | General | A new COMPUTE_JOBS system view was added. |
| IGN-25754 | Platforms and Clients | .NET Client: Upgraded from .NET 6 to .NET 8. |
| IGN-25716 | Platforms and Clients | Java client no longer needs heartbeat messages while under load. |
| IGN-25685 | SQL | CREATE TABLE syntax was changed to match SQL style. |
| IGN-25599 | General | Fixed Catalog API type mapping. |
| IGN-25538 | General | Added support for cluster-wide metrics management. |
| IGN-25494 | Platforms and Clients | ClientKeyValueBinaryView.get() method now no longer returns key column name. |
| IGN-25457 | General | You can now create a table even if the specified storage profile does not exist on the node. |
| IGN-25453 | General | Added configuration of deadlock prevention policy to the transaction configuration. |
| IGN-25067 | Platforms and Clients | Python DB API driver now supports  execution of batch parameters. |
| GG-41122 | Cluster Storage Engine | GRIDGAIN9_EXTRA_JVM_ARGS environment variable is now available in docker images. |
| GG-41055 | Cluster Data Snapshots and Recovery | Changed snapshot operation's ID generation to use UUID. |
| GG-40608 | General | GridGain Kafka-connect support added. |
| GG-40508 | Cluster Affinity and Baseline Topology | You can now reset partition distribution. |

## Known Limitations

### Delay on DDL Requests

DDL requests, such as `CREATE TABLE`, take a few seconds each to complete. Because of that, large database initialization scripts may take longer than expected. This will be addressed in an upcoming release.

### Performance of GridGain 8 Applications

Some scenarios may see lower performance when moving to GridGain 9. This is a temporary limitation, and the performance in these scenarios will be improved in upcoming versions.

### High-Availability with Two Data Copies

When a partition loses majority of its copies, it becomes unavailable. This behavior is required for split-brain protection. Because of this, in a distribution zone with 2 data replicas, losing one node may lead to partial unavailability.

To achieve both split-brain protection and full availability with one node down, use 3 or more replicas.

Upcoming versions will add a high-availability mode that support full availability with one node down when using 2 replicas.

### Data Center Replication with Multiple Data Centers

Complex Data Center Replication topologies (for example, the ones involving cycles) of 3 or more data centers are not supported. This will be addressed in an upcoming release.

### GridGain 8 Features

The following features of GridGain 8 are not available in this version, and will be added in upcoming versions:

- Rack-Awareness
- SQL Offloading
- Tracing
- Service Grid

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
