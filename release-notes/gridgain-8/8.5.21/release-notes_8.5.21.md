---
description: GridGain 8.5.21 is a maintenance release with fixes for deployment, the storage engine, SQL, the web console, and snapshots.
hidden: true
---

# GridGain 8.5.21 Release Notes

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-29245 | Deployment | Fixed an assertion error that happened when a class was concurrently deployed by multiple class loaders. |
| GG-29430 | Storage Engine | Fixed an issue where a deadlock between rebalancing and checkpointing could cause the node to hang on startup. |
| GG-29267 | Storage Engine | Fixed an issue when destroying a cache during rebalance could crash the cluster. |
| GG-29110 | Storage Engine | Added validation for the number of WAL segments configuration parameter. If the value is less than 2, the node will not start. |
| GG-29033 | Storage Engine | Fixed an issue when an exception was thrown when a complex field of a binary object was used as a key or value in cache operations. |
| GG-28910 | Web console | Web console: always show the data region name in the cache configuration. |
| GG-27798 | Control Script | Fixed an issue that caused the `control.sh --baseline` command to fail when the node with the smallest order in the topology is a client. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-29179 | Architecture | Fixed an issue where info level messages were written to the log even though a higher log level was configured. |
| GG-29190 | Snapshot utility | The snapshot schedule command now supports write throttling. |
| GG-28575 | Snapshots & PITR | Removed a requirement for the "WRITE" file permission in WAL iterator. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version. You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.5.20`, `8.5.19`, `8.5.18`, `8.5.17`, `8.5.16`, `8.5.15`, `8.5.14`, `8.5.13`, `8.5.12`, `8.5.11`, `8.5.10`, `8.5.9`, `8.5.8-p11`, `8.5.8-p6`, `8.5.8`, `8.5.7`, `8.5.6`, `8.5.5`, `8.5.3`, `8.4.16`, `8.4.15`, `8.4.14-p2`, `8.4.14`, `8.4.13`, `8.4.12`, `8.4.11`, `8.4.10`, `8.4.9`, `8.4.8-p8`, `8.4.8`, `8.4.7`, `8.4.6`, `8.4.5`, `8.4.4`, `8.4.3-p1`, `8.4.2-p11`

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
