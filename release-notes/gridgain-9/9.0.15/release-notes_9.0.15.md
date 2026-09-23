---
description: >-
  GridGain 9.0.15 adds SQL schema support, metastorage compaction, and query and
  transaction cancellation from Java clients.
---

# GridGain 9.0.15 Release Notes

## Overview

GridGain 9.0.15 is a release that brings a large number of new features and several major behavior changes.

## New Features

### SQL Schema Support

Prior to this release, you could only use the PUBLIC schema. You can now create other schemas and use it to create tables.

To create a schema, use the [CREATE SCHEMA](../../sql-reference/ddl.md#create-schema) statement:

```sql
CREATE SCHEMA myschema
```

Once the schema is created, you can create tables in it by providing a qualified table name:

```sql
CREATE TABLE IF NOT EXISTS myschema.Person (
  id int primary key,
  city_id int,
  name varchar,
  age int,
  company varchar
)
```

### Metastorage Compaction

With this release, GridGain will automatically prune metastorage information that is no longer required. As a result, the amount of space required for metastorage is expected to go down.

### Stopping SQL Queries, Transactions and Compute Jobs from Java Clients

With this release, the `CancelHandle` object can be used by Java client to stop queries, transactions and compute jobs.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-26838 | SQL | Added a new SCHEMAS system view. |
| IGN-26835 | CLI Tool | Fixed an issue that sometime prevented using SQL from CLI tool when authentication was enabled. |
| IGN-26681 | SQL | Added a column_ordinal column to TABLE_COLUMNS system view. |
| IGN-25986 | Platforms and Clients | Added support for stopping queries from java clients. |
| IGN-25611 | General | Metastorage is now pruned automatically. |
| IGN-22775 | SQL | Improved readability of EXPLAIN command output. |
| GG-42277 | General | Multiple libraries updated to fix CVEs. |
| GG-41857 | General | Java 17 and 21-based GridGain docker images are now available. |
| GG-41712 | Cluster Data Snapshots and Recovery | Added new ignite.pitr.threadPoolSize configuration. |
| GG-41328 | GridGain Integrations | Kafka source: added source.offset.mode and source.offset.fail.mode to control connector restart behavior. |
| GG-41287 | Cluster SQL Engine | Cache-specific transactions are now available in the transactions system view. |

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to create a snapshot on a cluster if data rebalance happened after table creation. This will be addressed in the next release.
- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### Data Center Replication with Multiple Data Centers

Complex Data Center Replication topologies (for example, the ones involving cycles) of 3 or more data centers are not supported. This will be addressed in an upcoming releases.

### GridGain 8 Features

The following features of GridGain 8 are not available in this version, and will be added in upcoming versions:

- Rack-Awareness
- Tracing
- Service Grid

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
