# MariaDB 10.1.36 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.36) | [Release Notes](mariadb-10136-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10136-changelog.md) | [Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 8 Sep 2018

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is a previous stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.36](mariadb-10136-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.41-84.1
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/tokudb) updated to 5.6.41-84.1
* if available, stunnel can be used during [Galera rsync SST](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster#rsync) - [MDEV-15511](https://jira.mariadb.org/browse/MDEV-15511)
* fix of regression introduced in 10.1.32: [MDEV-13333](https://jira.mariadb.org/browse/MDEV-13333)
* fix of regression affecting 10.1.35 only: [MDEV-16647](https://jira.mariadb.org/browse/MDEV-16647) InnoDB fails to drop large temporary table on disconnect
* Galera: [MDEV-10754](https://jira.mariadb.org/browse/MDEV-10754) wsrep\_sst\_rsync does not support innodb\_data\_home\_dir

### Security Fixes

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2019-2503](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2503)

## Changelog

For a complete list of changes made in [MariaDB 10.1.36](mariadb-10136-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10136-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.1.36](mariadb-10136-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-1-36-and-mariadb-connector-c-2-3-7-connector-j-2-3-0-and-connector-odbc-2-0-18-now-available/).

A file format compatibility bug that was introduced in [MariaDB 10.1.0](mariadb-10-1-0-release-notes.md) was fixed in [MariaDB 10.1.21](mariadb-10121-release-notes.md).\
Using [page\_compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) or non-default [innodb\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) created files that were incompatible with [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) or MySQL 5.6. [MariaDB 10.1.21](mariadb-10121-release-notes.md) and higher will convert affected files from earlier [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) releases to a compatible format.**This prevents a downgrade to earlier** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **versions.**[See the commit for details.](https://github.com/MariaDB/server/commit/ab1e6fefd869242d962cb91a006f37bb9ad534a7)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
