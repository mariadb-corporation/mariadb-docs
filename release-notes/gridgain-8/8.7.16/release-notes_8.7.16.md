---
description: >-
  GridGain 8.7.16 is a maintenance release with fixes and improvements across
  partition consistency, SQL, the storage engine, thin clients, data
  replication, and integrations.
hidden: true
---

# GridGain 8.7.16 Release Notes

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-24471 | Affinity & Baseline Topology | Improved partition consistency validation. |
| GG-27779 | Affinity & Baseline Topology | Improved partition loss handling. |
| GG-23133 | Control Script | Added the "--cache check_index_inline_sizes" command to the control script. The command checks that index inline size is the same on all cluster nodes. The command could be useful to analyze performance problems with SQL queries. |
| GG-28218 | Discovery | Improved Dynamic DNS support in `TcpDiscoveryVmIpFinder`. |
| GG-13034 | Metrics & Monitoring | Added the `IgniteMXBean.getPublicThreadPoolSize` method. `IgniteMXBean.getExecutorServiceFormatted` was deprecated. |
| GG-27581 | Platforms & Thin Clients | .NET: Added partition-based implementations of `AffinityCall` and `AffinityRun`. |
| GG-27289 | Platforms & Thin Clients | ODBC: `SQLRowCount()` now returns non-zero value for select queries. The returned value now depends on the number of rows cached locally by the driver. |
| GG-27288 | Platforms & Thin Clients | ODBC: Added support for cursor column-wise binding. This allows user applications to fetch result set rows in batches (SQL_ATTR_ROW_ARRAY_SIZE > 1). |
| GG-28579 | Platforms & Thin Clients | .NET: Expose data types returned by the `IFieldQueryCursor` query cursor. |
| GG-27286 | Platforms & Thin Clients | ODBC: Some result set metadata such as returned by `SQLNumResultCols()` can now be called after `SQLPrepare()`, no need to call `SQLExecute()`. |
| GG-23897 | Rebalance | Fixed incorrect calculation of rebalance statistics. Added the `IGNITE_WRITE_REBALANCE_PARTITION_DISTRIBUTION_THRESHOLD` system property to configure the output of partition distribution. |
| GG-26250 | SQL | Added a parameter to the COPY FROM operation to define a delimiter for CSV files. |
| GG-28610 | SQL | Improved usability of exception handling when SQL memory quota is exceeded. |
| GG-28463 | SQL | Several SQL-related properties are moved from `IgniteConfiguration` to a new `SqlConfiguration` class. Old properties are deprecated. |
| GG-28386 | SQL | Fixed a memory leak when SQL INSERT statements with non-constant functions were used. |
| GG-27408 | SQL | Added ability to use one timezome for all nodes in a cluster to process SQL date / time values. |
| GG-28388 | Storage Engine | Fixed an issue when a false-positive error message about `ExchangeLatchManager` would appear in the log. |
| GG-27716 | Storage Engine | Fixed a possible `ConcurrentModificationException` in `ExchangeDiscoveryEvents`. |
| GG-27221 | Storage Engine | Added a utility for offline indexes validation. |
| GG-28289 | Storage Engine | Performance suggestions about disabling partition backups are no longer printed to the console. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-28129 | Data Replication | Improved Data Replication thread management. |
| GG-27483 | Integrations | Added support for Oracle GoldenGate for Big Data 19, implemented a generic handler for DML operations. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-28497 | Snapshot utility | Fixed an issue introduced in the previous release where the snapshot management tool's CHECK command required the `ADMIN_CACHE` permission. |
| GG-28505 | Snapshots & PITR | Fixed an issue when an unstable connection to a client node could cause snapshot operations to hang. |
| GG-28091 | Snapshots & PITR | The write throttling threshold and disk limit parameters were added to the CREATE snapshot command in the snapshot management tool. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those.
Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

Rolling-upgrade compatible versions:

`8.7.15`, `8.7.14`, `8.7.13`, `8.7.12`, `8.7.11`, `8.7.10`, `8.7.9`, `8.7.8`, `8.7.7`, `8.7.6`, `8.7.5`, `8.7.4`, `8.7.3`, `8.7.2-p12`, `8.7.2`, `8.5.19`, `8.5.18`, `8.5.17`, `8.5.16`, `8.5.15`, `8.5.14`, `8.5.13`, `8.5.12`, `8.5.11`, `8.5.10`, `8.5.9`, `8.5.8-p6`, `8.5.8`, `8.5.7`, `8.5.6`, `8.5.5`, `8.5.3`, `8.4.16`, `8.4.15`, `8.4.14-p2`, `8.4.14`, `8.4.13`, `8.4.12`, `8.4.11`, `8.4.10`, `8.4.9`, `8.4.8-p8`, `8.4.8`, `8.4.7`, `8.4.6`, `8.4.5`, `8.4.4`, `8.4.3-p1`, `8.4.2-p11`

### Known Limitations

There is a compatibility issue that affects upgrade from version 8.7.13 and earlier to this version.
The issue affects GridGain Enterprise and Ultimate clusters with GridGain Authentication and Authorization enabled.
The issue will be fixed in a future version.
If your cluster is affected and you're planning to upgrade to this version, please contact GridGain Support for details.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
