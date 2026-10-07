---
description: GridGain 8.5.13 is a maintenance release that includes a number of bug fixes.
hidden: true
---

# GridGain 8.5.13 Release Notes

## What's New in This Release

This maintenance release includes a number of bug fixes.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Known Issues

| Issue ID | Description |
|---|---|
|  |  |

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-25647 | Continuous Queries | [8.5.13]-[GG-19412]-[IGNITE-11907] Registration of continuous query should fail if nodes don't have remote filter class |
| GG-25239 | Metrics & Monitoring | [8.5.13]-[GG-18936]-[IGNITE-11512] Add counter left partition for index rebuild in CacheGroupMetricsMXBean |
| GG-25151 | Rebalance | [8.5.13]-[GG-23437]-[IGNITE-3195] Rebalancing: IgniteConfiguration.rebalanceThreadPoolSize is wrongly treated |
| GG-25613 | SQL | [8.5.13]-[GG-24838] Use ignite thread for notifier about long query |
| GG-25674 | Storage Engine | [8.5.13]-[GG-23963] Eliminate contention on ConcurrentHashMap.size() |
| GG-25509 | Storage Engine | [8.5.13]-[GG-25395] Improve logging for async writing of Binary Metadata |
| GG-25174 | Storage Engine | [8.5.13]-[GG-19492] Add debug output for org.apache.ignite.internal.processors.cache.persistence.GridCacheOffheapManager#restorePartitionStates method. |
| GG-24879 | Storage Engine | [8.5.13]-[GG-24505]-[IGNITE-12099] Don't write metadata to disk in discovery thread |
| GG-25527 | Transactions | [8.5.13]-[GG-22287] IgniteCacheGroupsTest.testConcurrentOperationsAndCacheDestroy is flaky (25% rate) and consumes 10 minutes in case of fail |
| GG-25161 | Transactions | [8.5.13]-[GG-24306] IgniteException "Failed to resolve nodes topology" during cache.removeAll() and constantly changing topology |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-25175 | Affinity & Baseline Topology | Fixed metastorage migration. |

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
