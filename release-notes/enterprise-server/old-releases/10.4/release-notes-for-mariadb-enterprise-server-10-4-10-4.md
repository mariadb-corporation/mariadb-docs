# Release Notes for MariaDB Enterprise Server 10.4.10-4

This fourth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.4.10-4 was released on 2019-11-18.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2020-2780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2780)                                                                                                 | 6.5             |
| [CVE-2019-2974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2974)                                                                                                 | 6.5             |
| [CVE-2019-2938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2938)                                                                                                 | 4.4             |

## Notable Changes

* New option `innodb_change_buffer_dump` added to Debug builds. This option dumps the contents of the [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) change buffer to the server error log at startup. This is useful when a slow shutdown cannot be performed successfully. ([MDEV-20864](https://jira.mariadb.org/browse/MDEV-20864))
* Eliminated unnecessary logging of warnings to the error log regarding [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) maximum row size for DML statements which should be present only for DDL operations. (MENT-454)
* Improved \[\[[galera-cluster | MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md)]] error logging to explain that GCache recovery is not possible when GCache encryption is enabled. (MENT-373)

## Issues Fixed

### Can result in data loss

* [mariadb-backup](../../10-4/broken-reference/) [--prepare](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) [--export](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) ... could overwrite binary logs if certain conditions were present. ([MDEV-20703](https://jira.mariadb.org/browse/MDEV-20703))\
  Conditions which must be present to trigger this bug:
  * [mariadb-backup](../../10-4/broken-reference/) is executed on the MariaDB Server host, and
  * Configuration files from the master are used, and
  * Configuration files enable binary logging

If unable to upgrade to MariaDB Enterprise Server 10.4.10-4, where this bug is fixed, a workaround is available: use the `--defaults` option to [mariadb-backup](../../10-4/broken-reference/) to avoid the bug-triggering conditions by specifying a different configuration file.

### Can result in a hang or crash

* Prior removal of a `FULLTEXT` index from an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table can cause a hang on startup. ([MDEV-19647](https://jira.mariadb.org/browse/MDEV-19647))
* Removal of a `FULLTEXT` index from an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table can cause a hang. ([MDEV-19529](https://jira.mariadb.org/browse/MDEV-19529))
* Change to a [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table containing a `FULLTEXT` index can cause Server to become unresponsive. ([MDEV-20987](https://jira.mariadb.org/browse/MDEV-20987))
* Removal of a virtual column used by an index can result in a crash. (MENT-434)
* [CREATE INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-index), [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table), or [OPTIMIZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table) on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table can cause Server to become unresponsive. ([MDEV-20852](https://jira.mariadb.org/browse/MDEV-20852))
* `INSTANT ADD COLUMN` on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table which includes a `OREIGN KEY` definition can result in a crash. (MENT-435)
* `INSTANT` column `DROP` or column reorder can result in a crash. Server restart can also crash unless [innodb\_force\_recovery](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_force_recovery) is set to E`2E` or greater. ([MDEV-20117](https://jira.mariadb.org/browse/MDEV-20117))

### Can result in unexpected behavior

* Unnecessary logging of warnings to the error log regarding [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) maximum row size for DML statements which should be present only for DDL operations. (MENT-454)
* After server restart, a [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) using a `FULLTEXT` index on [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) tables can fail to return some data. ([MDEV-19073](https://jira.mariadb.org/browse/MDEV-19073))
* [MariaDB Enterprise Backup](../../10-4/broken-reference/) and MariaDB Backup, when using `mbstream`, recreated `xtrabackup_info` in the same directory as the backup file. Repeated extract of the backup could fail. ([MDEV-18438](https://jira.mariadb.org/browse/MDEV-18438))
* `mysqld_multi.sh` script could not be launched and returned a syntax error. (MENT-433)
* Though not supported on Microsoft Windows, the [server\_audit\_output\_type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables) system variable for the Audit plugin accepted a `SYSLOG` value. ([MDEV-19851](https://jira.mariadb.org/browse/MDEV-19851))
* `FOREIGN KEY` constraints have been ignored during [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) when parent table is [System-Versioned](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/system-versioned-table/README.md). ([MDEV-16210](https://jira.mariadb.org/browse/MDEV-16210))
* [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) from child table with `FOREIGN KEY` was not possible when the table is [System-Versioned](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/system-versioned-table/README.md). ([MDEV-20812](https://jira.mariadb.org/browse/MDEV-20812))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) cannot perform GCache recovery when GCache encryption is enabled, but no warning was sent to the error log. (MENT-373)

### Related to install and upgrade

* Installing MariaDB Enterprise Server from repository failed on CentOS 7 due to package dependencies. (MENT-420)

## Interface Changes

* `WARN_INNODB_PARTITION_OPTION_IGNORED` error code added

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.4.10-4 is provided for:

* CentOS 8
* CentOS 7
* CentOS 6
* Debian 10
* Debian 9
* Debian 8
* Red Hat Enterprise Linux 8
* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 6
* SUSE Linux Enterprise Server 15
* SUSE Linux Enterprise Server 12
* Ubuntu 18.04
* Ubuntu 16.04
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a README file within the download.

## Installation Instructions

* [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
