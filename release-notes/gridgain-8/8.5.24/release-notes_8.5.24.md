---
description: GridGain 8.5.24 is a maintenance release with fixes for affinity configuration, continuous queries, SQL, and the storage engine.
hidden: true
---

# GridGain 8.5.24 Release Notes

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-22193 | Affinity & Baseline Topology | Added a check to verify affinity key configuration. A node will fail to join the cluster if its affinity configuration differs from that of other nodes. |
| GG-30412 | Continuous Queries | Continuous queries are no longer deployed to client nodes, since client nodes don't store data. |
| GG-30072 | SQL | Fixed an issue where a node crashed if an index was created on a field with a mismatched data type. Now the index creation will be rolled back instead. |
| GG-30446 | Storage Engine | Fixed an issue when a node could crash during Point-in-Time Recovery procedure. Also fixed an issue when a historical rebalance erroneously wouldn't start. |
| GG-30408 | Storage Engine | Fixed an issue when WAL archive could not be cleaned up after a historical rebalance. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-30193 | Snapshots & PITR | Fixed a bug causing an incremental snapshot to always contain the whole index.bin file. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version. You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.5.23`, `8.5.22`, `8.5.21`, `8.5.20`, `8.5.19`, `8.5.18`, `8.5.17`, `8.5.16`, `8.5.15`, `8.5.14`, `8.5.13`, `8.5.12`, `8.5.11`, `8.5.10`, `8.5.9`, `8.5.8-p11`, `8.5.8-p6`, `8.5.8`, `8.5.7`, `8.5.6`, `8.5.5`, `8.5.3`, `8.4.16`, `8.4.15`, `8.4.14-p2`, `8.4.14`, `8.4.13`, `8.4.12`, `8.4.11`, `8.4.10`, `8.4.9`, `8.4.8-p8`, `8.4.8`, `8.4.7`, `8.4.6`, `8.4.5`, `8.4.4`, `8.4.3-p1`, `8.4.2-p11`

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
