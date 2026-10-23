---
description: GridGain 8.8.23-p3 re-uploads 8.8.23-p2 artifacts and fixes a critical issue with complex SQL operations that use the IN operator.
hidden: true
---

# GridGain 8.8.23-p3 Release Notes

This is a re-upload of artifacts due to a deployment script failure during 8.8.23-p2 shipping. This release fixes a critical issue with complex SQL operations. This is done by reverting a previous improvement that was supposed to provide improved index usage by IN operator.

## Improvements and Fixed Issues

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-36270 | Cluster SQL Engine | Reverted GG-35682 changes to fix a critical error with complex SQL operations that use IN operator. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.29-p1`, `8.7.42-p2`, `8.8.2-p1`, `8.8.4-p2`, `8.8.8-p1`, `8.8.9-p1`, `8.8.13-p2`, `8.8.16-p2`, `8.8.18-p1`, `8.7.22`, `8.7.28`, `8.7.32`, `8.7.34`, `8.7.38`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.9`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`, `8.8.14`, `8.8.15`, `8.8.16`, `8.8.17`, `8.8.18`, `8.8.19`, `8.8.20`, `8.8.21`, `8.8.22`, `8.8.23`, `8.8.23-p1`

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.7.2`, `2.11.0`, `2.12.0`, `2.13.0`

## We Value Your Feedback
Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
