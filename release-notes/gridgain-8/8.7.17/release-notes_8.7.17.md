---
description: >-
  GridGain 8.7.17 adds partition awareness to the Java thin client, along with
  fixes across the control script, SQL, the storage engine, data replication,
  and snapshots.
hidden: true
---

# GridGain 8.7.17 Release Notes

## New Features

- Added [partition awareness](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/thin-clients/getting-started-with-thin-clients#partition-awareness) in Java thin client.

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-28153 | Control Script | Fixed a bug that caused the `validate_indexes` command to terminate when the connection to the initiator breaks. |
| GG-19140 | Data Structures | Fixed critical failure occurring when trying to create a cache in a non-existing data region. |
| GG-29108 | Deployment | Fixed an issue when a node could fail during concurrent class deployment via pear class loading. |
| GG-28828 | Platforms & Thin Clients | Added support for partition awareness in Java thin client. |
| GG-26434 | SQL | Added new security permissions:<br>- `GET_QUERY_VIEWS` — query the `LOCAL_SQL_RUNNING_QUERIES` or `LOCAL_SQL_QUERY_HISTORY` system views,<br>- `KILL_QUERY` — execute the `KILL QUERY` command. |
| GG-26047 | SQL | Added support for inlining BigDecimal values into indexes. |
| GG-13936 | Storage Engine | Added validation for the number of WAL segments configuration parameter. If the value is less than 2, the node will not start. |
| GG-28299 | Storage Engine | Extended logging for historical rebalance. |
| GG-28246 | Storage Engine | Improved payload detection logic for the `idle_verify` and `validate_indexes` commands of the control script. |
| GG-28740 | Storage Engine | The binary metadata folders are now located under the `{WORK_DIR}/db` directory. |
| GG-28749 | Storage Engine | Fixed a possible index tree corruption in case the same composite object is used both as the key and as a part of the value. |
| GG-28558 | Web Console | Web console: always show the data region name in the cache configuration. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-25984 | Data Replication | Introduced a separate shared thread-pool for internal DR tasks. The pool replaces per-cache control threads. |
| GG-27177 | Data Replication | Introduced new configuration options for background replication batch size (in bytes) and full-state transfer batch size (in bytes). |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-29159 | Snapshot utility | Added snapshot throttling support to the `schedule` command. |
| GG-27227 | Snapshots & PITR | Removed requirement for the "WRITE" file permission in WAL iterator. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those.
Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.4.2-p11`, `8.4.3-p1`, `8.4.4`, `8.4.5`, `8.4.6`, `8.4.7`, `8.4.8`, `8.4.8-p8`, `8.4.9`, `8.4.10`, `8.4.11`, `8.4.12`, `8.4.13`, `8.4.14`, `8.4.14-p2`, `8.4.15`, `8.4.16`, `8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.7.2`, `8.7.2-p12`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`

### Known Limitations

There is a compatibility issue that affects upgrade from version 8.7.13 and earlier to this version.
The issue affects GridGain Enterprise and Ultimate clusters with GridGain Authentication and Authorization enabled.
The issue will be fixed in a future version.
If your cluster is affected and you're planning to upgrade to this version, please contact GridGain Support for details.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
