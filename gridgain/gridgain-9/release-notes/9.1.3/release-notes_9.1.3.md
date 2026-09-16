---
description: >-
  GridGain 9.1.3 adds cache creation from Java and a new method to get the local node, along with multiple stability and performance improvements.
---

# GridGain 9.1.3 Release Notes

## Overview

GridGain 9.1.3 is a release with multiple minor improvements and significant improvements on cluster stability and performance.

## Major Changes

### Changed Syntax for Getting Nodes in Java

The `ignite.clusterNodes()` method was deprecated in this release and is replaced by `ignite.cluster().nodes()` method. This method now returns nodes in the logical topology.

The `clusterNodes()` will continue to work for backwards compatiblily, however we recommend changing your code to use the new method.

```java
Ignite ignite = node.api();

// Deprecated method for getting cluster nodes
var oldClusterNodes = ignite.clusterNodes();

// New method for getting cluster nodes
var newClusterNodes = ignite.cluster().nodes()
```

## New Features

### Creating Caches From Java

With this release, you can use the `@Cache` annotation in Java to create caches from Java classes. You can create caches from Key-Value POJOs. Once a cache is created, you can work with it as described in [cache](../../developers-guide/cache.md) documentation.

```java
class PojoKey {
    @Id
    Integer id;

    @Id(SortOrder.DESC)
    @Column(value = "id_str", length = 20)
    String idStr;
}

@Cache(
    value = "kv_pojo",
    zone = @Zone(
		value = "zone_test",
		replicas = 2,
		storageProfiles = "default"
   ),
    colocateBy = { @ColumnRef("id"), @ColumnRef("id_str") },
    indexes = { @Index(value = "ix", columns = {
                    @ColumnRef(value = "f_name"),
                    @ColumnRef(value = "l_name") })
    }
)
class PojoValue {
    @Column("f_name")
    String firstName;

    @Column("l_name")
    String lastName;

    String str;
}

Table myTable = ignite.catalog().createCache(PojoKey.class, PojoValue.class);

KeyValueView<PojoKey, PojoValue> view =  myTable.keyValueView(PojoKey.class, PojoValue.class);
```

### New Method to Get Local Node

With this release, you can use the new `ignite.cluster().localNode()` method to quickly get the local [embedded node](../../quick-start/embedded-mode.md).

## Improvements and Fixed Issues

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| IGN-27966 | Metrics and Monitoring | Added CpuLoad metric to os metric source and UpTime metric to jvm metric source. |
| IGN-27959 | Configuration | You can now use old configuration from before 9.1.0 release after update. |
| IGN-27922 | General | Added `IgniteCluster` interface with `nodes()` and `localNode()` methods. Deprecated `Ignite#clusterNodes`. Fixed `nodes()` to return only members of logical topology. |
| IGN-27861 | SQL | In the EXPLAIN command output, offset and fetch attributes now have consistent meaning in Sort and Limit sections. |
| IGN-27835 | SQL | Changed the column name resolution algorithm for columns with the same name during JOIN operation. An index with a $ separator is now added to the column to avoid collision. |
| IGN-27820 | SQL | JDBC driver now provides correct metadata for all available schemas. |
| IGN-27787 | SQL | Improved EXPLAIN command output. |
| IGN-27742 | SQL | Fixed an issue that caused the createTableAsync method to not fetch the table when using non-default schema. |
| IGN-27724 | Platforms and Clients | C++ client now supports heartbeats. |
| IGN-27702 | SQL | Added support for EXPLAIN MAPPING FOR command. |
| IGN-27676 | Data Streamer | Data Streamer: fixed the receiver API. Added `payloadMarshaller`, `argumentMarshaller`, `resultMarshaller`. Added `DataStreamerReceiverDescriptor<T, A, R>`. Deprecated `ReceiverDescriptor<A>`. Added new `DataStreamerTarget#streamData` overload with `DataStreamerReceiverDescriptor` and deprecated the old one. |
| IGN-27650 | SQL | Fixed incorrect parsing of DATE, TIME, TIMESTAMP, and TIMESTAMP WITH LOCAL TIME ZONE in the CAST(string AS <datetime type> FORMAT 'format-string') operation. |
| IGN-27631 | SQL | You now need to commit the explicit transaction in the script for it to be executed. |
| IGN-25829 | Platforms and Clients | .NET: Added overloads with `CancellationToken` to SQL and Compute APIs. |
| GG-43835 | Cluster Data Snapshots and Recovery | Fixed an issue that could lead to some data not being restored from snapshots. |
| GG-43814 | Cluster Rolling Upgrade | Fixed an issue that prevented older node from joining GridGain 9.1.2 cluster during rolling upgrade. |
| GG-43642 | SQL | Added support for automatic conversion of values of legacy java time api during DCR from GridGain 8. |
| GG-43626 | SQL | Updated parquet-avro to version 1.15.2. |
| GG-43534 | Cluster Continuous Queries | Fixed continuous query returning incorrect results on primary replica miss. |
| GG-43419 | Cluster Storage Engine | Cluster nodes will no longer start if there are storage profiles with storage engines that are forbidden by the provided license in the node configuration. |
| GG-43392 | Builds and Deliveries | RPM packages are now correctly signed. |
| GG-43177 | Cluster SQL Engine | Improved performance of COPY FROM command when exporting data into parquet format. |
| GG-43136 | Cluster SQL Engine | Fixes an issue with creating sequences in SQL scripts |
| GG-41861 | Cluster Architecture | You can now create caches by using Catalog API. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.0`, `9.1.1`, `9.1.2`

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
