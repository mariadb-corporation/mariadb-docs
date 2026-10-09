---
description: GridGain 8.5.19 is a maintenance release that fixes a number of issues.
hidden: true
---

# GridGain 8.5.19 Release Notes

This maintenance release fixes a number of issues.

## Known Issues

| Issue ID | Description |
|---|---|
| GG-28497 | The snapshot management tool requires incorrect permission (`ADMIN_CACHE`) when performing the CHECK operation. This will be fixed in the next release. |

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-28486 | Communication | DNS reverse lookup will not be performed if node's 'localHost' property is set as an IP address. Add `IGNITE_TCP_COMM_SET_ATTR_HOST_NAMES=true` to the JVM startup options to return to old behavior (DNS lookup will be performed even if 'localHost' is an IP address). |
| GG-28242 | Control Script | Added the `--verbose` option to control.sh\|bat, which prints stacktrace when available. |
| GG-27459 | Control Script | Added the `--check-sizes` option to the `validate_indexes` command to check whether index and cache size are equal. |
| GG-28351 | Metrics & Monitoring | Fixed incorrect calculation of the "indexBuildCountPartitionsLeft" metric. |
| GG-28150 | SQL | File-related SQL functions are now disabled. This does not affect the COPY command. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-28312 | Snapshots & PITR | Fixed an issue when an incremental snapshot of a partition would always fail to be created, and a full snapshot would be taken instead. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version. You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for the information on upgrade options.

- 8.4.2-p11
- 8.4.3-p1
- 8.4.4
- 8.4.5
- 8.4.6
- 8.4.7
- 8.4.8
- 8.4.8-p8
- 8.4.9
- 8.4.10
- 8.4.11
- 8.4.12
- 8.4.13
- 8.4.14
- 8.4.14-p2
- 8.4.15
- 8.4.16
- 8.5.1-p166
- 8.5.3
- 8.5.4
- 8.5.5
- 8.5.5-p3
- 8.5.6
- 8.5.7
- 8.5.8
- 8.5.8-p6
- 8.5.9
- 8.5.10
- 8.5.11
- 8.5.12
- 8.5.13
- 8.5.14
- 8.5.15
- 8.5.16
- 8.5.17
- 8.5.18

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
