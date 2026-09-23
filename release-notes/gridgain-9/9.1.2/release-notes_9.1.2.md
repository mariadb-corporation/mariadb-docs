---
description: >-
  GridGain 9.1.2 reintroduces near caches and adds cluster topology metrics along with multiple SQL and client fixes.
---

# GridGain 9.1.2 Release Notes

## Overview

GridGain 9.1.2 is a big milestone release with support for new storage type, big license changes and a host of improvements and enhancements.

## New Features

### Near Caches

This release reintroduces support for near caches in GridGain 9. Near caches provide a way to store data locally on your clients and avoid lengthy network queries for latest data from the cluster.

You can configure near cache for any [table view](../../developers-guide/table-api.md#basic-table-operations). Data will be queried from the cluster when it is read, and stored locally for the configured duration for repeated access.

Below is a simple example of configuring near cache for a table:

```java
NearCacheOptions nearCacheOptions = NearCacheOptions
  .builder()
  .expireAfterAccess(5000)
  .expireAfterUpdate(100000)
  .maxEntries(100)
  .build();
// Create table view configuration.
TableViewOptions tableViewOptions = TableViewOptions
  .builder()
  .nearCacheOptions(nearCacheOptions)
  .build();
// Create a qualified table name object.
QualifiedName myTable = QualifiedName.parse("PUBLIC.accounts");
// Get a view that will also create a near cache on the client.
KeyValueView<Tuple, Tuple> kvView = client.tables().table(myTable).keyValueView(tableViewOptions);
```

For more information on near caches, as well as limitations, see [Near Cache](../../developers-guide/near-cache.md) documentation.

### Mapping Empty Values in COPY INTO Command

With this release, you can configure how empty values are mapped on import, and `null` values are mapped to on export. You do this by adding the `null` parameter and assigning a new value.

```sql
/* Import data from CSV with custom quotation character */
COPY FROM '/path/to/dir/data.csv'
INTO Table1 (name, age, empty)
FORMAT CSV
WITH 'null'='no data'
```

### Cluster Topology Metrics

This release includes new cluster topology metrics, that provide information about node name, id and version, as well as cluster name, id, and number of nodes in the cluster. For more information about these sources, see [Available Metrics](../../administrators-guide/metrics/metrics-list.md).

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-27805 | Platforms and Clients | .NET: Fixed job executor compatibility to allow the users to run .NET compute jobs compiled against different Ignite versions. |
| IGN-27792 | Metrics | Added cluster topology metrics. |
| IGN-27758 | General | Default size of all storage engines' in-memory data regions is now calculated to be 20% of available RAM. |
| IGN-27750 | Platforms and Clients | Fixed cluster id mismatch error text in Java client. |
| IGN-27740 | General | Added the --file parameter to node config update and cluster config update commands. |
| IGN-27701 | SQL | Added support for simplified EXPLAIN PLAN FOR command. |
| IGN-27696 | SQL | Fixed an issue that caused queries to sometimes hang after a quick node restart. |
| IGN-27695 | Platforms and Clients | Fixed unnecessary lock contention in data streamer. |
| IGN-27691 | Platforms and Clients | .NET: Fixed ReceiverDescriptor generic parameters to match receiver signature and enable compiler type inference for the API calls. |
| IGN-27526 | SQL | JDBC ResultSet getTime, getDate, and getTimestamp methods now take connection's time zone into account when underlying data has timestamp with local time zone data type. |
| IGN-27416 | SQL | The SQL EXPLAIN command output is improved. |
| IGN-27250 | SQL | Improved EXPLAIN command output for queries with join operations. |
| IGN-26976 | SQL | DESCRIBE statement now correctly throws an exception. |
| IGN-26601 | Platforms and Clients | You can now use schema-quaified table names from C++ clients. |
| GG-43576 | Cluster Data Snapshots and Recovery | Fixed an issue that prevented restoring snapshots created on previous version. |
| GG-43517 | SQL | The SQL DROP SEQUENCE command now checks if the sequence is in use before deleting it. |
| GG-43464 | SQL | You can now map empty strings to specific values in COPY INTO command. |
| GG-43201 | Cluster Storage Engine | Implemented Near Cache for Java Client. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.0`, `9.1.1`

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
