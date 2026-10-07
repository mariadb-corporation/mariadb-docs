---
description: >-
  GridGain 8.7.12 is a maintenance release with a number of bug fixes across the
  control script, SQL, storage engine, transactions, and the snapshot utility.
hidden: true
---

# GridGain 8.7.12 Release Notes

## What's New in This Release

This release includes a number of bugfixes.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-27362 | Control script | The control.sh script will no longer require trust/keystore passwords to be entered twice. |
| GG-27217 | Diagnostics & Failure Handling | Added ability to enable extra logging for index rebuild process. Extra logging can be enabled by setting the IGNITE_ENABLE_EXTRA_INDEX_REBUILD_LOGGING system property to true. |
| GG-27390 | Javadocs | Introduced the @IgniteExperimental annotation to mark APIs which are unstable or likely to change in the future. |
| GG-27196 | Security | Updated several dependencies to address the vulnerabilities reported by npm audit. |
| GG-27065 | SQL | Fixed an issue where the INSERT and MERGE INTO commands did not work without the list of column names provided explicitly. |
| GG-27376 | Storage Engine | Introduced cluster ID and cluster tag as internal labels that identify a cluster. |
| GG-26091 | Storage Engine | Improved the performance of free list management |
| GG-27388 | Transactions | Fixed an issue where a transaction could get stuck in the rolled back state after it was suspended and then timed out. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-27195 | Snapshot utility | Fixed a possible issue with restoring replicated caches with an expiry policy from a snapshot. |

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
