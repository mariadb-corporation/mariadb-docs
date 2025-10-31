# MariaDB 10.1.17 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.17) | [Release Notes](mariadb-10117-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10117-changelog.md) | [Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 30 Aug 2016

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.17](mariadb-10117-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.31-77.0
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.31-77.0
* [Innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.32
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) updated to 5.6.32
* The CONNECT engine now supports the [JDBC Table type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect/connect-table-types/connect-jdbc-table-type-accessing-tables-from-another-dbms) - [MDEV-9765](https://jira.mariadb.org/browse/MDEV-9765).
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) for Fedora 22
* Packages for Fedora 24 are [now available](https://downloads.mariadb.org/mariadb/repositories/)
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2016-6662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-6662) ([MDEV-10465](https://jira.mariadb.org/browse/MDEV-10465)). That allowed a malicious user to create a `my.cnf` in the datadir and, under certain circumstances, execute arbitrary code as mysql (or even root) user. This vulnerability was discovered by [Dawid Golunski](https://legalhackers.com).

### Galera Updates

* Galera wsrep library updated to 25.3.17
* The support for [wsrep\_max\_ws\_rows](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_max_ws_rows) system variable has now been added and thus its values will no longer be ignored by the server. In order to be backward compatible its default value has been changed to 0 (from 131072), which essentially allows writesets of any size.
* The default value of [wsrep\_max\_ws\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_max_ws_size) has been raised from 1GB to 2GB.

## Changelog

For a complete list of changes made in [MariaDB 10.1.17](mariadb-10117-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10117-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
