---
description: >-
  MariaDB Server versions supported on MariaDB Cloud: 11.8, 11.4, 10.11, 10.6,
  and 10.5 (current minor versions), available across both serverless and
  provisioned deployments.
---

# MariaDB Server Version Support

## Server Versions

| Version  |
| -------- |
| 11.8     |
| 11.4     |
| 10.11.11 |
| 10.6     |
| 10.5.25  |

## Serverless and Provisioned Availability

The same MariaDB Server versions are offered for MariaDB Serverless and MariaDB Provisioned single-node databases. For Serverless, one of them is the default version:

* Launching a Serverless database on the **default** version claims an instance MariaDB Cloud already has ready, so it starts in milliseconds.
* Launching a Serverless database on **any other** version builds it on demand, so creation takes longer. The database is serverless in every other respect.

Selecting a version other than the default requires a paid plan. On a trial with no payment method on file, only the default version is offered.

Your [service tier](../readme/service-tiers.md) determines which edition you get: MariaDB Enterprise Server builds are offered on the Power and PowerPlus tiers, and MariaDB Community Server builds on all tiers.

Minor version upgrades stay within a major version. MariaDB Cloud does not upgrade a database across major versions, and does not downgrade.

## Notes

For more information about specific features and capabilities of each version, please refer to the MariaDB [Server documentation](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/) and [release notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
