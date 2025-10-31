# MariaDB 10.1.44 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.44/) | [Release Notes](mariadb-10144-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10144-changelog.md) | [Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 28 Jan 2020

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is a previous stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.44](mariadb-10144-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [Innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.47
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.46-86.2
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.46-86.2
* [MDEV-21337](https://jira.mariadb.org/browse/MDEV-21337): fix aligned\_malloc()
* [MDEV-21343](https://jira.mariadb.org/browse/MDEV-21343): Threadpool/Unix- wait\_begin() function does not wake/create threa\
  ds, when it should
* Bug#29630767: Use of uninitialized value in libmysql (client.cc function run\_plugin\_auth)
* [MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046): Crashes caused by random values to the offset option of SHOW BINLOG EVENT offset command
* [MDEV-19376](https://jira.mariadb.org/browse/MDEV-19376): Semisync Master could crash when it executed RESET MASTER and a replica reconnects using GTID protocol
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2020-2574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2574)

## Changelog

For a complete list of changes made in [MariaDB 10.1.44](mariadb-10144-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10144-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.1.44](mariadb-10144-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-4-12-10-3-22-and-10-2-31-10-1-44-and-5-5-67-now-available/).

A file format compatibility bug that was introduced in [MariaDB 10.1.0](mariadb-10-1-0-release-notes.md) was fixed in [MariaDB 10.1.21](mariadb-10121-release-notes.md).\
Using [page\_compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) or non-default [innodb\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) created files that were incompatible with [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) or MySQL 5.6. [MariaDB 10.1.21](mariadb-10121-release-notes.md) and higher will convert affected files from earlier [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) releases to a compatible format.**This prevents a downgrade to earlier** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **versions.**[See the commit for details.](https://github.com/MariaDB/server/commit/ab1e6fefd869242d962cb91a006f37bb9ad534a7)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
