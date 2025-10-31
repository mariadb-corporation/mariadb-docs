# MariaDB 10.1.22 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.22) | [Release Notes](mariadb-10122-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10122-changelog.md) | [Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 14 Mar 2017

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.22](mariadb-10122-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

Updating from [MariaDB 10.1.21](mariadb-10121-release-notes.md) to [MariaDB 10.1.22](mariadb-10122-release-notes.md) is **highly recommended** due to two high-priority regression fixes. See below for links to the relevant MDEVs.

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.35-80.0
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.35-80.0
* [PCRE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) updated to 8.40
* [MDEV-12160](https://jira.mariadb.org/browse/MDEV-12160): [ed25519 authentication plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-ed25519)
* [MDEV-11842](https://jira.mariadb.org/browse/MDEV-11842): Fix a 10.1.21 regression with failed INSERT, BEFORE INSERT triggers, and columns with no default value
* [MDEV-12075](https://jira.mariadb.org/browse/MDEV-12075): Fix a 10.1.21 regression in the InnoDB data file extension code
* [MDEV-11027](https://jira.mariadb.org/browse/MDEV-11027): better InnoDB crash recovery progress reporting
* [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520): improvements to how InnoDB data files are extended
* Improvements to InnoDB startup/shutdown to make it more robust
* [MDEV-11233](https://jira.mariadb.org/browse/MDEV-11233): fix for FULLTEXT index crash
* [MDEV-9734](https://jira.mariadb.org/browse/MDEV-9734): [systemd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/systemd) compatible bintar files now available
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) for Fedora 23, CentOS 5, RHEL 5, and openSUSE 13
* OpenSUSE 42 repositories have been added in this release
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2017-3313](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3313)
  * [CVE-2017-3302](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3302)

A file format compatibility bug that was introduced in [MariaDB 10.1.0](mariadb-10-1-0-release-notes.md) was fixed in [MariaDB 10.1.21](mariadb-10121-release-notes.md).\
Using [page\_compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) or non-default [innodb\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) created files that were incompatible with [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) or MySQL 5.6. [MariaDB 10.1.21](mariadb-10121-release-notes.md) and higher will convert affected files from earlier [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) releases to a compatible format.**This prevents a downgrade to earlier** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **versions.**[See the commit for details.](https://github.com/MariaDB/server/commit/ab1e6fefd869242d962cb91a006f37bb9ad534a7)

## Changelog

For a complete list of changes made in [MariaDB 10.1.22](mariadb-10122-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10122-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
