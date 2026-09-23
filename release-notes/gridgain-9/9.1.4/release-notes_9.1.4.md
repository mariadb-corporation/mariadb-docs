---
description: >-
  GridGain 9.1.4 enables partition colocation by default and improves SSL support, metrics, and near cache handling.
---

# GridGain 9.1.4 Release Notes

## Overview

GridGain 9.1.4 is a release with multiple minor improvements and significant improvements on cluster stability and performance.

## Major Changes

### Partition Colocation

This release features a major rework of how partitions are distributed to the nodes and organized.

With partition colocation enabled by default for new clusters, partitions with the same index for all tables in the same distribution zone will now be stored on the same node and use the same RAFT group. This change results in improved performance, as the cluster requires fewer resources to manage distribution zones.

For nodes started with persistent storage from previous versions, partition colocation will be disabled by default. Due to major changes in partitions management, persistent storage from previous versions is not compatible with colocation. We recommend recreating persistent storage on a new 9.1.4 cluster and manually migrating data to it.

If you receive the incompatible colocation mode error when the node attempts to join the cluster, clear the persistent data on the node and explicitly set the replication mode by setting the `IGNITE_ZONE_BASED_REPLICATION` system property to true (to enable colocation mode) or false (to disable colocation mode).

## Improved Features

### Improved SSL Support

This release introduces support for SSL in [Python DB API](../../developers-guide/clients/python.md) and [ODBC Driver](../../developers-guide/sql/odbc/odbc-driver.md). You can now securely connect to your cluster from both.

To securely connect from python DB API, specify the ssl key file and certificate in the connection configuration:

```python
pyignite_dbapi.connect(
	address='127.0.0.1',
	use_ssl=True,
	ssl_keyfile='<path_to_ssl_keyfile.pem>',
	ssl_certfile='<path_to_ssl_certfile.pem>'
)
```

For ODBC driver, specify it in the connection string:

```
DRIVER={Apache Ignite 3};ADDRESS=localhost:10800;SCHEMA=yourSchemaName;SSL_MODE=require;SSL_KEY_FILE=<path_to_ssl_keyfile.pem>;SSL_CERT_FILE=<path_to_ssl_certfile.pem>
```

### Extended Metrics

This release includes multiple new metrics that can enhance monitoring your clusters:

- New SQL thread pool metrics
- New sql query execution metrics.
- Extended data region metrics.
- A new data center replication lag metric.

For a full list of metrics, see the [Available Metrics](../../administrators-guide/metrics/metrics-list.md).

### Improved Near Cache Support

Prior to this release, [Near Caches](../../developers-guide/near-cache.md) were only configurable for clients. This release introduces support for initializing them from embedded mode.

The example below shows how you can create a near cache from an embedded node:

```java
// Grab the embedded mode client.
Ignite ignite = node.api();

// Configure near cache options.
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
KeyValueView<Tuple, Tuple> kvView = ignite.tables().table(myTable).keyValueView(tableViewOptions);

// Get a value from the view.
Tuple key = Tuple.create().set("id", 0);
Tuple value = kvView.get(null, key);
System.out.println("Retrieved value:" + value.intValue("id"));
```

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-28077 | Platforms & Clients | Added SSL support to Python DB API Driver. |
| IGN-28074 | Platforms & Clients | Added SSL support for ODBC driver. |
| IGN-28014 | General | Colocation is now enabled for new clusters. |
| IGN-27984 | Cluster SQL Engine | Fixed partition pruning for tables that have keys of the TIMESTAMP WITH LOCAL TIME ZONE data type. |
| IGN-27964 | General | Added sql thread pool metrics. |
| IGN-27957 | General | Added data region metrics for aipersist storage engine. |
| IGN-27860 | Cluster SQL Engine | The Limit node on top of Sort node is now merged into Sort node. |
| IGN-27840 | Distributed Data Streamer | Fixed data streamer to respect backpressure in auto-flush timer. |
| IGN-27591 | Distributed Computing | .NET: Improved platform job execution performance by caching assembly load contexts and job type information. |
| IGN-27589 | SQL | Updated Calcite from version 1.39 to version 1.40. |
| IGN-27005 | Distributed Computing | Clients: fixed causality guarantees for compute jobs and streamer receiver. When a client runs a job or receiver which updates table data, the changes can now be observed from that client immediately. |
| IGN-26772 | General | Added a new ignite.raft.disruptors.queueSize node configuration property. |
| IGN-24188 | General | OS information is now logged on node start. |
| GG-44042 | Builds and Deliveries | Update Kafka client dependency from 3.9.0 to 3.9.1. |
| GG-44008 | Cluster Storage Engine | Fixed a rare issue that caused a node to be unable to join a cluster after complete cluster restart due to errors in metastore. |
| GG-44001 | Builds and Deliveries | Updated httpclient5 to version 5.4.3. |
| GG-43610 | Cluster SQL Engine | You can now install GridGain DR connector from Docker. |
| GG-43606 | Cluster Data Snapshots and Recovery | Global status of snapshot is now printed in allNodes mode. |
| GG-43568 | Cluster Storage Engine | Near caches are now supported in embedded mode. |
| GG-43561 | Cluster Metrics & Monitoring | Added data region metrics. |
| GG-43402 | Cluster Storage Engine | Added requirements for distribution zone used for secondary storage. |
| GG-43342 | Cluster Metrics & Monitoring | Added sql query execution metrics. |
| GG-43037 | Cluster Storage Engine | You can now use the ARCHIVE_AT condition to only remove data from primary storage. |
| GG-42853 | Cluster Data Snapshots and Recovery | Added configurable direct memory limits for snapshot restoration process. |
| GG-42727 | Cluster Data Replication | Added a metric that can be used to track lag between source and target of data center replication. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.0`, `9.1.1`, `9.1.2`, `9.1.3`

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
