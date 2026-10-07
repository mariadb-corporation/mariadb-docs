---
description: GridGain 8.5.17 is a maintenance release that includes a number of bug fixes.
hidden: true
---

# GridGain 8.5.17 Release Notes

## What's New in This Release

This release includes a number of bug fixes.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version. You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for the information on upgrade options.

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
- 8.5.1-p166
- 8.5.3
- 8.5.4
- 8.5.5
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

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-27381 | Continuous Queries | Optimized continuous queries memory consumption. |
| GG-27279 | Data Structures | Volatile data structures are now stored in a non-persistent data region. |
| GG-27536 | Security | Resolved vulnerabilities reported by npm audit. |
| GG-27429 | SQL | Added support for Update/Delete keywords for Spring Data. |
| GG-27653 | Storage Engine | Fixed an exception in ZooKeeperDiscoverySpi that could cause the node to hang. |
| GG-27527 | Storage Engine | Fixed a cache internal data structure corruption which could happen during an intensive cache update when TTL is enabled. |
| GG-27252 | Storage Engine | Fixed an issue where partitions may get permanently stuck in an outdated state after rebalancing. |
| GG-27567 | Storage Engine | Caches with SYNC rebalancing mode are now always rebalanced prior to caches with ASYNC rebalancing mode when rebalancing order is the same. |
| GG-27987 | Storage Engine | Fixed an issue that caused an assertion error during throttling on checkpoint. |
| GG-26739 | Transactions | Long operations dump timeout can now be changed via MXBean. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-27983 | Data Replication | Fixed an issue when Visor/Web Console can't collect cache metrics when Data Replication is enabled. |

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
