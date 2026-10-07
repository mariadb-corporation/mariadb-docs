---
description: >-
  GridGain 8.9.9-p1 fixes a known issue with outer joins in SQL.
hidden: true
---

# GridGain 8.9.9-p1 Release Notes

## Overview

GridGain 8.9.9-p1 fixes a known issue with outer joins in SQL.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-41800 | Cluster SQL Engine | Fixed an issue that could cause an outer join to fail after a column was added to the table. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.22`, `8.7.28`, `8.7.29-p1`, `8.7.32`, `8.7.34`, `8.7.38`, `8.7.39-p2`, `8.7.42-p2`, `8.8.1`, `8.8.2`, `8.8.2-p1`, `8.8.3`, `8.8.4`, `8.8.4-p1`, `8.8.4-p2`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.8-p1`, `8.8.9`, `8.8.9-p1`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`, `8.8.13-p1`, `8.8.13-p2`, `8.8.14`, `8.8.15`, `8.8.16`, `8.8.16-p1`, `8.8.16-p2`, `8.8.17`, `8.8.18`, `8.8.18-p1`, `8.8.19`, `8.8.19-p1`, `8.8.20`, `8.8.21`, `8.8.22`, `8.8.22-p1`, `8.8.22-p2`, `8.8.23`, `8.8.23-p1`, `8.8.23-p2`, `8.8.23-p3`, `8.8.24`, `8.8.25`, `8.8.25-p1`, `8.8.26`, `8.8.27`, `8.8.28`, `8.8.29`, `8.8.30`, `8.8.31`, `8.8.32`, `8.8.33`, `8.8.34`, `8.8.35`, `8.8.36`, `8.8.37`, `8.8.37-p1`, `8.8.38`, `8.8.39`, `8.8.40`, `8.8.41`, `8.9.0`, `8.9.1`, `8.9.2`, `8.9.3`, `8.9.4`, `8.9.5`, `8.9.6`, `8.9.7`, `8.9.8`, `8.9.9`

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.11.1`, `2.12.0`, `2.13.0`,  `2.14.0`,  `2.15.0`
