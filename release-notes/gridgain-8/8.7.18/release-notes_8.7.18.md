---
description: >-
  GridGain 8.7.18 adds support for GridGain Control Center and includes fixes for
  metrics and monitoring, SQL, and snapshots.
hidden: true
---

# GridGain 8.7.18 Release Notes

## New Features

This release adds support for [GridGain Control Center](https://control.gridgain.com), a management and monitoring tool for GridGain and Apache Ignite clusters.

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-29345 | Metrics & Monitoring | Introduced a tag in tracing spans for discovery events representing the message class. |
| GG-29384 | SQL | Fixed the slow start of a node caused by linear index scan. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-29268 | Snapshots & PITR | Fixed a performance issue when retrieving snapshot information caused by unnecessary hostname resolution. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those.
Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.4.2-p11`, `8.4.3-p1`, `8.4.4`, `8.4.5`, `8.4.6`, `8.4.7`, `8.4.8`, `8.4.8-p8`, `8.4.9`, `8.4.10`, `8.4.11`, `8.4.12`, `8.4.13`, `8.4.14`, `8.4.14-p2`, `8.4.15`, `8.4.16`, `8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.7.2`, `8.7.2-p12`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
