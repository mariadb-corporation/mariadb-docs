---
description: GridGain 8.5.25 is a maintenance release with fixes for continuous queries, the SQL engine, and the snapshot utility.
hidden: true
---

# GridGain 8.5.25 Release Notes

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-30918 | Cluster Continuous Queries | Fixed an issue where Continuous Query deployment, after client node reconnection with the new node id, could lead to remote nodes failure when peer class loading is enabled, and remote nodes don't have a remote filter in the classpath. |
| GG-30698 | Cluster SQL Engine | Fixed possible deadlock on parallel destroy of multiple SQL caches. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-30881 | Cluster Snapshot Utility | Snapshot utility will now work correctly when connected to a client node. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version. You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.5.23`, `8.5.24`

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
