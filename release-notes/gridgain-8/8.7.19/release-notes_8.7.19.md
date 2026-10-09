---
description: >-
  GridGain 8.7.19 adds experimental OpenCensus tracing of the transaction API and
  Java thin client enhancements, together with fixes across SQL, storage, thin
  clients, and data replication.
hidden: true
---

# GridGain 8.7.19 Release Notes

## New Features

- Experimental: Tracing of GridGain transaction API with OpenCensus.
- Java thin client enhancements:
  - Added distributed computing API.
  - Added ability to specify an expiry policy when creating a cache using `CacheConfiguration`.

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-28974 | Architecture | Fixed an issue where a node did not start when the parent user thread group that used the instance of `Ignite` was destroyed. |
| GG-28633 | Discovery | Fixed an issue where a node did not shut down after a failed attempt to start. |
| GG-29162 | Metrics & Monitoring | Added instrumentation of the transaction API with OpenCensus for distributed tracing. |
| GG-29472 | Platforms & Thin Clients | .NET thin client can now automatically discover all server nodes after connecting to one of them. |
| GG-29024 | Platforms & Thin Clients | Java thin client: Added support for distributed computing. |
| GG-28399 | Platforms & Thin Clients | Java thin client: Added ability to specify a cache expiry policy when creating a cache using `CacheConfiguration`. |
| GG-28227 | Platforms & Thin Clients | .NET: Added support for running compute tasks in a custom executor. |
| GG-28816 | Platforms & Thin Clients | C++ platform no longer requires autotools to build. |
| GG-27285 | Platforms & Thin Clients | ODBC: Fixed the implementation of SQLPrepare to return the metadata about a request without executing it. |
| GG-24013 | Platforms & Thin Clients | Added support for user attributes in Java thin client and JDBC. |
| GG-29322 | SQL | Fixed an issue with parsing empty values in CSV files for the SQL COPY FROM command. |
| GG-28975 | SQL | Fixed an issue where a mismatch between index field type and actual field type caused a node failure. |
| GG-28965 | SQL | Improved the log message about too low merge table size. |
| GG-25361 | SQL | Fixed an issue where a metadata request through a JDBC Connection could fail if the metadata is requested for a cache for which there is no explicit query entity configured. |
| GG-29415 | Storage Engine | Fixed an issue where a deadlock between rebalancing and checkpointing could cause the node to hang on startup. |
| GG-28433 | Storage Engine | Identified several more cases when historical rebalance should be triggered. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-29150 | Architecture | Fixed a compatibility issue introduced in 8.7.14 which could cause problems with a rolling upgrade in case authentication was configured. |
| GG-29358 | Data Replication | Fixed an NPE on node stop after a startup failure. |
| GG-26542 | Data Replication | Added proper validation of arguments in the DR Sender MBean. |
| GG-24106 | Data Replication | Added ability to cancel a full state transfer. |
| GG-28432 | Security | The `CACHE_CREATE` and `CACHE_DESTROY` permissions can now be set both as a cache and as a system permissions. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those.
Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.4.2-p11`, `8.4.3-p1`, `8.4.4`, `8.4.5`, `8.4.6`, `8.4.7`, `8.4.8`, `8.4.8-p8`, `8.4.9`, `8.4.10`, `8.4.11`, `8.4.12`, `8.4.13`, `8.4.14`, `8.4.14-p2`, `8.4.15`, `8.4.16`, `8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.7.2`, `8.7.2-p12`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
