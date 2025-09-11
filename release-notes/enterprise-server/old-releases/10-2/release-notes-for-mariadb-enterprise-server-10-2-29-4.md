# Release Notes for MariaDB Enterprise Server 10.2.29-4

This fourth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.2 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.2.29-4 was released on 2019-11-18.

## Fixed Security Vulnerabilities

| CVE (with cve.org link)                                                       | CVSS base score |
| ----------------------------------------------------------------------------- | --------------- |
| [CVE-2020-2780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2780) | 6.5             |
| [CVE-2019-2974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2974) | 6.5             |
| [CVE-2019-2938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2938) | 4.4             |

## Notable Changes

* New option `innodb_change_buffer_dump` added to Debug builds. This option dumps the contents of the [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) change buffer to the server error log at startup. This is useful when a slow shutdown cannot be performed successfully. ([MDEV-20864](https://jira.mariadb.org/browse/MDEV-20864))
* Eliminated unnecessary logging of warnings to the error log regarding [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) maximum row size for DML statements which should be present only for DDL operations. (MENT-454)

## Issues Fixed

### Can result in data loss

* mariadb-backup --prepare --export ... could overwrite binary logs if certain conditions were present. ([MDEV-20703](https://jira.mariadb.org/browse/MDEV-20703))\
  Conditions which must be present to trigger this bug:
  * [mariadb-backup](../../10-2/broken-reference/) is executed on the MariaDB Server host, and
  * Configuration files from the master are used, and
  * Configuration files enable binary logging

If unable to upgrade to MariaDB Enterprise Server 10.2.29-4, where this bug is fixed, a workaround is available: use the `--defaults` option to [mariadb-backup](../../10-2/broken-reference/) to avoid the bug-triggering conditions by specifying a different configuration file.

### Can result in a hang or crash

* Prior removal of a `FULLTEXT` index from an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table can cause a hang on startup. ([MDEV-19647](https://jira.mariadb.org/browse/MDEV-19647))
* Removal of a `FULLTEXT` index from an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table can cause a hang. ([MDEV-19529](https://jira.mariadb.org/browse/MDEV-19529))
* Change to a [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table containing a `FULLTEXT` index can cause Server to become unresponsive. ([MDEV-20987](https://jira.mariadb.org/browse/MDEV-20987))
* Removal of a virtual column used by an index can result in a crash. (MENT-434)
* [CREATE INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-index), [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table), or [OPTIMIZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table) on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table can cause Server to become unresponsive. ([MDEV-20852](https://jira.mariadb.org/browse/MDEV-20852))

### Can result in unexpected behavior

* Unnecessary logging of warnings to the error log regarding [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) maximum row size for DML statements which should be present only for DDL operations. (MENT-454)
* After server restart, a [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) using a `FULLTEXT` index on [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) tables can fail to return some data. ([MDEV-19073](https://jira.mariadb.org/browse/MDEV-19073))
* [MariaDB Enterprise Backup](../../10-2/broken-reference/) and MariaDB Backup, when using `mbstream`, recreated `xtrabackup_info` in the same directory as the backup file. Repeated extract of the backup could fail. ([MDEV-18438](https://jira.mariadb.org/browse/MDEV-18438))
* `mysqld_multi.sh` script could not be launched and returned a syntax error. (MENT-433)
* Though not supported on Microsoft Windows, the [server\_audit\_output\_type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables) system variable for the Audit plugin accepted a `SYSLOG` value. ([MDEV-19851](https://jira.mariadb.org/browse/MDEV-19851))

### Related to install and upgrade

* Installing MariaDB Enterprise Server from repository failed on CentOS 7 due to package dependencies. (MENT-420)

## Interface Changes

* [WARN\_INNODB\_PARTITION\_OPTION\_IGNORED](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) error code added

## Platforms

In alignment to the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.2.29-4 is provided for:

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

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies/)".

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies/). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads/). Instructions for installation are included as a `README` file within the download.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
