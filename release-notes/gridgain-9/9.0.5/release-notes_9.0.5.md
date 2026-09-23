---
description: >-
  GridGain 9.0.5 adds secondary columnar storage support and automatic host
  resolution in the node finder.
---

# GridGain 9.0.5 Release Notes

## Overview

GridGain 9.0.5 is focused on improving CLI reporting and cluster performance.

## New Features

### Secondary Columnar Storage Support

With this release, you can set up a secondary storage for your tables. All data added to the primary table will be automatically copied to secondary table. Currently, only columnar secondary storage is supported.

Secondary storage must be specified on table creation by using the `SECONDARY_STORAGE_PROFILE` parameter, for example:

```sql
CREATE TABLE Person (  id int primary key,  city_id int,  name varchar,  age int,  company varchar) WITH PRIMARY_ZONE='myZone', STORAGE_PROFILE='default', SECONDARY_STORAGE_PROFILE='myColumnarStore'
```

To get data from secondary storage, use the `use_secondary_storage` SQL hint, for example:

{% hint style="info" %}
You can only use the `SELECT` operation with secondary storage. All other operations will be resolved by using the primary storage and copied to secondary storage automatically. If you are using explicit transactions, you must use read-only transactions to work with secondary storage.
{% endhint %}

```sql
SELECT count(*) FROM Person /*+ use_secondary_storage */
```

GridGain will then automatically use the storage that can perform the operation faster.

For more information, see [Columnar Storage](../../administrators-guide/storage/engines/columnar.md).

### Automatic Host Resolution in Node Finder

When specifying nodes in the node finder configuration, you can now specify host address. It will be automatically resolved, including the cases when multiple addresses are assigned the same host name.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-25437 | CLI Tool | CLI tool now has improved highlighting for HOCON configuration. |
| IGN-25430 | CLI Tool | Node and cluster configuration is now displayed in HOCON format. |
| IGN-25418 | CLI Tool | Improved node config update command output. |
| IGN-25412 | SQL | Improved performance of INSERT statements. |
| IGN-25269 | General | Node finder can now resolve host names. |
| IGN-25204 | General | Improved key-value API performance. |
| IGN-25155 | SQL | Improved performance of count command. |
| IGN-25106 | CLI Tool | Improved connect command output when no arguments are provided. |
| IGN-25102 | CLI Tool | Required parameters are now highlighted in CLI. |
| IGN-24480 | SQL | Improved error message when numeric fields overflow. |
| IGN-23167 | General | Improved query performance. |
| IGN-22428 | General | Improved storage performance. |
| GG-40396 | Cluster Security | Improved authentication performance. |
| GG-40203 | Cluster Storage Engine | Added support for creating secondary storages. |
| GG-40200 | Cluster Storage Engine | ALTER TABLE ADD REPLICA and ALTER TABLE DROP REPLICA commands are no longer supported. |
| GG-40019 | Cluster SQL Engine | Added a new USE SEQUENCE permission. |
| GG-39894 | Cluster SQL Engine | Added support for CACHE parameter in the Sequence command. |

## Known Limitations

### Delay on DDL Requests

DDL requests, such as `CREATE TABLE`, take a few seconds each to complete. Because of that, large database initialization scripts may take longer than expected. This will be addressed in upcoming versions.

### Performance of GridGain 8 Applications

Some scenarios may see lower performance when moving to GridGain 9. This is a temporary limitation, and the performance in these scenarios will be improved in upcoming versions.

### High-Availability with Two Data Copies

When a partition loses majority of its copies, it becomes unavailable. This behavior is required for split-brain protection. Because of this, in a distribution zone with 2  data replicas, losing one node may lead to partial unavailability.

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
- Write-Behind Caching

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
