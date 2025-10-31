# MariaDB 10.0.27 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.27) | [Release Notes](mariadb-10027-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10027-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 25 Aug 2016

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is a previous stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

This is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.31-77.0
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.31-77.0
* [Innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.32
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) updated to 5.6.32
* The CONNECT engine now supports the [JDBC Table type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect/connect-table-types/connect-jdbc-table-type-accessing-tables-from-another-dbms) - [MDEV-9765](https://jira.mariadb.org/browse/MDEV-9765).
* New status variables; [Handler\_read\_retry](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#handler_read_retry), [Update\_scan](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#update_scan) and [Delete\_scan](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#delete_scan) making it easier to debug certain problems.
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) for Fedora 22.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2016-6662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-6662) ([MDEV-10465](https://jira.mariadb.org/browse/MDEV-10465)). That allowed a malicious user to create a `my.cnf` in the datadir and, under certain circumstances, execute arbitrary code as mysql (or even root) user. This vulnerability was discovered by [Dawid Golunski](https://legalhackers.com).
  * [CVE-2016-5630](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-5630)
  * [CVE-2016-5612](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-5612)

## Changelog

For a complete list of changes made in [MariaDB 10.0.27](mariadb-10027-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10027-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
