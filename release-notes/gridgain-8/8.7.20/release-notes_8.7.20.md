---
description: >-
  GridGain 8.7.20 delivers fixes and improvements across discovery, SQL, the storage engine, thin clients, and data replication.
hidden: true
---

# GridGain 8.7.20 Release Notes


## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-29731 | Architecture | The OpenCensus module is now enabled by default. |
| GG-29636 | Continuous Queries | Fixed an issue where a `ConcurrentModificationException` could be thrown during a continuous query execution when DEBUG log level is enabled. |
| GG-29728 | Control Center | Fixed an issue where the Control center agent didn't start after the coordinator node changed. |
| GG-29618 | Control Center | `gridgain-control-center-agent` maven artifact was renamed to `control-center-agent`. |
| GG-29366 | Control Center | GridGain will print a warning to the log when the cluster is trying to connect to Control Center but the cluster's version is not supported. |
| GG-29610 | Discovery | Fixed an issue where `UnknownHostException` was thrown when host names given in the discovery configuration couldn't be resolved. |
| GG-28964 | Discovery | Added support for node discovery using AWS Application ELB. |
| GG-23908 | Discovery | `KubernetesIpFinder` can now discover pods in "not-ready" state. |
| GG-29493 | Platforms & Thin Clients | Added support for Compute API to the .NET thin client. |
| GG-29001 | Scan Query | Fixed an issue that caused the node to fail when a scan query fails during rebalancing. |
| GG-29480 | SQL | Fixed a data race when rebuilding indexes that could result in an incorrect index build status. |
| GG-29468 | SQL | Fixed an issue where a query fails when the CAST function is used in the sort expression. |
| GG-29188 | SQL | Fixed an issue where a query with a distributed join on the primary key could return wrong results. |
| GG-28522 | SQL | Introduced a check for duplicate column names in `CREATE TABLE` statements. |
| GG-29165 | Storage Engine | Improved the performance of page replacement mechanism in some cases. |
| GG-29423 | Storage Engine | Optimized partition map exchange by improving the analysis of WAL segments performed during the exchange. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-14427 | Data Replication | Exceptions in Data Replication threads are now handled by the failure handler, which allows users to configure the desired behavior upon failures related to Data Replication. |
| GG-29239 | Integrations | Fixed an issue with Date and Timestamp datatypes in the GoldenGate handler. |

## Installation and Upgrade Information
See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those.
Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.4.2-p11`, `8.4.3-p1`, `8.4.4`, `8.4.5`, `8.4.6`, `8.4.7`, `8.4.8`, `8.4.8-p8`, `8.4.9`, `8.4.10`, `8.4.11`, `8.4.12`, `8.4.13`, `8.4.14`, `8.4.14-p2`, `8.4.15`, `8.4.16`, `8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`,
`8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.7.2`, `8.7.2-p12`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`

## We Value Your Feedback
Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
