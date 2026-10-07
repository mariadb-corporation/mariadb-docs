---
description: GridGain 8.5.20 is a maintenance release with fixes and improvements across the storage engine, monitoring, snapshots, and integrations.
hidden: true
---

# GridGain 8.5.20 Release Notes

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-28330 | Rebalance | Fixed incorrect calculation of rebalance statistics. Added the `IGNITE_WRITE_REBALANCE_PARTITION_DISTRIBUTION_THRESHOLD` system property to configure the output of partition distribution. |
| GG-28439 | Metrics & Monitoring | Added the `IgniteMXBean.getPublicThreadPoolSize` method. `IgniteMXBean.getExecutorServiceFormatted` was deprecated. |
| GG-28481 | Storage Engine | Added a utility for offline indexes validation. |
| GG-28657 | Storage Engine | Fixed a possible `ConcurrentModificationException` in `ExchangeDiscoveryEvents`. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-28484 | Snapshots & PITR | The write throttling threshold and disk limit parameters were added to the CREATE snapshot command in the snapshot management tool. |
| GG-28598 | Snapshots & PITR | Fixed an issue when unstable connection to a client node could cause snapshot operations to hang. |
| GG-28606 | Snapshot utility | Fixed an issue introduced in the previous release where the snapshot management tool's CHECK command required the `ADMIN_CACHE` permission. |
| GG-28495 | Integrations | Added support for Oracle GoldenGate for Big Data 19, implemented a generic handler for DML operations. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version. You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for the information on upgrade options.

Rolling-upgrade compatible versions:

`8.5.19`, `8.5.18`, `8.5.17`, `8.5.16`, `8.5.15`, `8.5.14`, `8.5.13`, `8.5.12`, `8.5.11`, `8.5.10`, `8.5.9`, `8.5.8-p6`, `8.5.8`, `8.5.7`, `8.5.6`, `8.5.5`, `8.5.3`, `8.4.16`, `8.4.15`, `8.4.14-p2`, `8.4.14`, `8.4.13`, `8.4.12`, `8.4.11`, `8.4.10`, `8.4.9`, `8.4.8-p8`, `8.4.8`, `8.4.7`, `8.4.6`, `8.4.5`, `8.4.4`, `8.4.3-p1`, `8.4.2-p11`

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
