---
description: >-
  How MariaDB Enterprise Server differs from MariaDB Community Server, and where
  to find the documentation for Enterprise Server features in this space.
---

# Editions & Compatibility

MariaDB Server is available in two editions:

* **MariaDB Community Server** is the open-source edition. Its releases are listed in [MariaDB Community Server Release Notes]({release-notes}/community-server).
* **MariaDB Enterprise Server** is the commercial edition, offered and supported by MariaDB plc. It's built from selected MariaDB Community Server versions that are further stabilized, hardened for security, and extended with Enterprise features. Its releases are listed in [MariaDB Enterprise Server Release Notes]({release-notes}/enterprise-server).

This documentation covers both editions. Where a feature or behavior applies to only one of them, the page says so.

## How the Editions Differ

Besides different release cycles and QA, MariaDB Enterprise Server has different default settings, to be more secure from the start, and includes only features that are fully supported and maintained. It also has Enterprise features that Community Server doesn't have.

For the feature differences in each release series, see [MariaDB Enterprise Server Differences](mariadb-enterprise-server-differences/README.md):

* [Differences in MariaDB Enterprise Server 12.3](mariadb-enterprise-server-differences/differences-in-mariadb-enterprise-server-12.3.md)
* [Differences in MariaDB Enterprise Server 11.8](mariadb-enterprise-server-differences/differences-in-mariadb-enterprise-server-11.8.md)
* [Differences in MariaDB Enterprise Server 11.4](mariadb-enterprise-server-differences/differences-in-mariadb-enterprise-server-11.4.md)
* [Differences in MariaDB Enterprise Server 10.6](mariadb-enterprise-server-differences/differences-in-mariadb-enterprise-server-10.6.md)
* [Differences in Available Plugins for Enterprise Server](mariadb-enterprise-server-differences/differences-in-available-plugins-for-enterprise-server.md)

For the components each Enterprise Server release contains, see [SBOM](sbom.md).

## Enterprise Server Documentation in This Space

These pages cover Enterprise Server features and procedures. Each one lives in the section for its topic:

* [Installing Enterprise Server](../server-management/install-and-upgrade-mariadb/installing-enterprise-server/README.md)
* [MariaDB Enterprise Server Upgrade Paths](../server-management/install-and-upgrade-mariadb/upgrading/upgrade-paths/README.md)
* [MariaDB Enterprise Backup](../server-usage/backup-and-restore/backup-and-restore-with-mariadb-enterprise-server/mariadb-enterprise-backup.md), with [Forming a Backup Strategy](../server-usage/backup-and-restore/backup-and-restore-with-mariadb-enterprise-server/forming-a-backup-strategy.md) and [Backup Optimization](../server-usage/backup-and-restore/backup-and-restore-with-mariadb-enterprise-server/backup-optimization.md)
* [InnoDB Architecture for MariaDB Enterprise Server](../server-usage/storage-engines/innodb/innodb-architecture-for-mariadb-enterprise-server/README.md)
* [MariaDB Enterprise Server InnoDB Operations](../server-usage/storage-engines/innodb/mariadb-enterprise-server-innodb-operations/README.md)
* [MariaDB Enterprise Spider Operations](../server-usage/storage-engines/spider/spider-storage-engine-introduction/mariadb-enterprise-spider-operations/README.md)
* [Authentication with Enterprise Server](../security/authentication-with-enterprise-server/README.md)
* [Security Vulnerabilities (CVE) Fixed in MariaDB Enterprise Server](../security/cve/enterprise-server.md)

## Release Policy

How long each Enterprise Server release series is supported, and when new releases come out, are covered in Release Notes:

* [Enterprise Server Lifecycle]({release-notes}/enterprise-server/about/enterprise-server-lifecycle)
* [Enterprise Server Release Schedule]({release-notes}/enterprise-server/about/enterprise-server-release-schedule)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
