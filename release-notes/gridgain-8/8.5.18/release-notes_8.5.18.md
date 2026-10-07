---
description: GridGain 8.5.18 is a maintenance release that includes a number of bug fixes.
hidden: true
---

# GridGain 8.5.18 Release Notes

## What's New in This Release

This release includes a number of bugfixes.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-27838 | Deployment | Fixed assertion error when unmarshalling a message from a failed node. |
| GG-21951 | Diagnostics & Failure Handling | Improved node start-up and periodic metrics logging. |
| GG-27930 | Discovery | Fixed an issue that caused TCP discovery to get stuck in reading from socket operation. |
| GG-27943 | SQL | Fixed an issue causing an incorrect query plan output for a long-running query. |
| GG-27920 | SQL | Fixed an issue with executing distributed joins when the number of joined tables is more than 7. |
| GG-27835 | SQL | Fixed an issue where the `enforceJoinOrder` flag was ignored when one of the previous queries had the identical SQL text and a different value of the flag. |
| GG-27598 | SQL | Added a thread pool to create and rebuild indexes. Removed the `INDEX_REBUILDING_PARALLELISM` system property and added the `IgniteConfiguration#setBuildIndexThreadPoolSize` configuration property. |
| GG-27584 | Storage Engine | Fixed partition desynchronization after rebalancing if a partition was remapped to a historical supplier which lost the history. |
| GG-28110 | Transactions | Fixed a bug that could possibly cause a deadlock on concurrent `putAll` invocations. |
| GG-27942 | Transactions | The "Too many open files" error for socket connection now triggers a critical failure to prevent the cluster from hanging. |
| GG-26507 | Transactions | Fixed an NPE during start of a backup transaction and partition desync issue if an evicted partition is assigned back to the original node. |

### GridGain Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-27676 | Snapshot utility | Fixed an issue with snapshot restore operations for snapshots created with caches with an expiry policy. |
| GG-22135 | Snapshot utility | The `idle_verify` option was removed from the snapshot utility, use "control.sh --cache idle_verify" instead. |

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
- 8.5.17

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
