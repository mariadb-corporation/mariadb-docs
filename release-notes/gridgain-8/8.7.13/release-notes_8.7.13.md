---
description: >-
  GridGain 8.7.13 delivers a number of improvements and bug fixes across the
  storage engine, SQL, transactions, data replication, and snapshots.
hidden: true
---

# GridGain 8.7.13 Release Notes

## What's New in This Release

This release includes a number of improvements and bug fixes.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those.
Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

- 8.4.2-p11
- 8.4.3-p1
- 8.4.4
- 8.4.5
- 8.4.6
- 8.4.7
- 8.4.8
- 8.4.8-p8
- 8.4.9
- 8.4.10
- 8.4.11
- 8.4.12
- 8.4.13
- 8.4.14
- 8.4.14-p2
- 8.4.15
- 8.4.16
- 8.5.3
- 8.5.4
- 8.5.5
- 8.5.5-p3
- 8.5.6
- 8.5.7
- 8.5.8
- 8.5.8-p6
- 8.5.9
- 8.5.10
- 8.5.11
- 8.5.12
- 8.5.13
- 8.5.14
- 8.5.15
- 8.5.16
- 8.7.2
- 8.7.2-p12
- 8.7.3
- 8.7.4
- 8.7.5
- 8.7.6
- 8.7.7
- 8.7.8
- 8.7.9
- 8.7.10
- 8.7.11
- 8.7.12

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-27533 | Cache | Print a warning of a potential deadlock when unordered collection is passed to a putAll-style bulk cache operation. |
| GG-27380 | Continuous Queries | Fixed an issue where continuous queries could produce excessive memory usage. |
| GG-27797 | Control Script | Fixed exceptional termination of the control.sh baseline command when the client node has the smallest order. |
| GG-27066 | Data Structures | Introduced a separate data region for volatile data structures. |
| GG-27986 | Storage Engine | Fixed an intermittent error occurring during checkpointing when throttling is applied. |
| GG-17349 | Storage Engine | A new optimization was introduced for Partition Map Exchange - PME blocking duration is greatly reduced when a baseline node left and the topology had been stable before. |
| GG-27652 | Storage Engine | Fixed NPE in Zookeeper Discovery SPI. |
| GG-27674 | Storage Engine | Caches with CacheRebalanceMode#SYNC rebalancing mode always take precedence over caches with CacheRebalanceMode#ASYNC rebalancing mode in the group of caches with the same rebalance order. |
| GG-27251 | Storage Engine | Fixed an issue where the rebalancing process hangs when it was completed during exchange. |
| GG-27525 | Storage Engine | Fixed an issue where a node could hang up when stopped during writing to the metastore. |
| GG-27632 | SQL | SQL offload statistics is now exposed via the Metrics API. |
| GG-27575 | SQL | Fixed Ignite Spring Query annotations to support case-insensitive keywords. |
| GG-27563 | SQL | Memory quota parameter for JDBC and JDBC thin connections has been disabled. It could be enabled by setting the `IGNITE_SQL_ENABLE_CONNECTION_MEMORY_QUOTA` system property to `true`. |
| GG-25877 | SQL | Indexing of JavaObject has been improved. Now we store only the hash, which reduces the size of the index as well as the time of objects comparison. |
| GG-27124 | SQL | Memory quota and offloading can now be configured both statically with XML file or IgniteConfiguration and dynamically via JMX. The memory quota value can be set in bytes, kilobytes, megabytes and gigabytes. |
| GG-23559 | Transactions | Added support for suspend/resume of PESSIMISTIC transactions. |
| GG-27631 | Transactions | MVCC-related APIs are marked as @IgniteExperimental to stress the beta status of the feature. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-27963 | Data Replication | Fixed an issue when Visor\Web Console cannot collect cache metrics if data replication is enabled. |
| GG-27319 | Data Replication | Fixed incorrect GridGainConfiguration validation. |
| GG-27622 | Snapshots & PITR | Removed redundant checks on a snapshot creation operation. |
| GG-27421 | Snapshots & PITR | Fixed an exception during WAL log compaction when records of certain types are encountered. |

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
