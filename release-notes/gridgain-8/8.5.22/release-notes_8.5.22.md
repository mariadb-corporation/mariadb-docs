---
description: GridGain 8.5.22 is a maintenance release with fixes for communication, discovery, thin clients, partition map exchange, and integrations.
hidden: true
---

# GridGain 8.5.22 Release Notes

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-29536 | Communication | Fixed an assertion error when SSL configuration is incorrect. |
| GG-29689 | Communication | Fixed an issue with grid-timeout-worker that could cause a deadlock. |
| GG-29563 | Discovery | KubernetesIpFinder can now discover pods in "not-ready" state. |
| GG-29496 | Discovery | Fixed an issue where a node did not shut down after a failed attempt to start. |
| GG-29638 | Platforms & Thin Clients | Fixed an issue with compilation of the SSL module for the ODBC driver on Linux. |
| GG-29448 | Partition Map Exchange | Optimized partition map exchange by improving the analysis of WAL segments performed during the exchange. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-29540 | Integrations | Fixed an issue with Date and Timestamp datatypes in the GoldenGate handler. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version. You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.5.21`, `8.5.20`, `8.5.19`, `8.5.18`, `8.5.17`, `8.5.16`, `8.5.15`, `8.5.14`, `8.5.13`, `8.5.12`, `8.5.11`, `8.5.10`, `8.5.9`, `8.5.8-p11`, `8.5.8-p6`, `8.5.8`, `8.5.7`, `8.5.6`, `8.5.5`, `8.5.3`, `8.4.16`, `8.4.15`, `8.4.14-p2`, `8.4.14`, `8.4.13`, `8.4.12`, `8.4.11`, `8.4.10`, `8.4.9`, `8.4.8-p8`, `8.4.8`, `8.4.7`, `8.4.6`, `8.4.5`, `8.4.4`, `8.4.3-p1`, `8.4.2-p11`

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
