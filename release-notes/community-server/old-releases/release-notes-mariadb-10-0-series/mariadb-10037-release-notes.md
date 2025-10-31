# MariaDB 10.0.37 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.37) | [Release Notes](mariadb-10037-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10037-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 1 Nov 2018

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is a previous stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

This is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.42
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) updated to 5.6.42
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.41-84.1
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.41-84.1
* Various fixes from MySQL 5.6.42: [MDEV-17533](https://jira.mariadb.org/browse/MDEV-17533), [MDEV-17532](https://jira.mariadb.org/browse/MDEV-17532), [MDEV-17531](https://jira.mariadb.org/browse/MDEV-17531)
* [MDEV-16465](https://jira.mariadb.org/browse/MDEV-16465): fixed a bug with DDL and FOREIGN KEY
* Fulltext index fixes:
  * [MDEV-12547](https://jira.mariadb.org/browse/MDEV-12547): extended the range of [innodb\_ft\_result\_cache\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) on 64-bit systems
  * [MDEV-16865](https://jira.mariadb.org/browse/MDEV-16865): InnoDB fts\_query() ignores KILL
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2018-3282](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3282)
  * [CVE-2016-9843](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-9843)
  * [CVE-2018-3174](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3174)
  * [CVE-2018-3143](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3143)
  * [CVE-2018-3156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3156)
  * [CVE-2018-3251](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3251)
  * [CVE-2019-2503](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2503)

## Changelog

For a complete list of changes made in [MariaDB 10.0.37](mariadb-10037-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10037-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.0.37](mariadb-10037-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-0-37-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
