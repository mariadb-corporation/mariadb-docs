# MariaDB 10.1.26 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.26) | [Release Notes](mariadb-10126-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10126-changelog.md) | [Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 10 Aug 2017

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the previous stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.26](mariadb-10126-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* The default for [innodb\_log\_compressed\_pages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) is now `ON` (see [MDEV-13247](https://jira.mariadb.org/browse/MDEV-13247))
* [PCRE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) updated to 8.41
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.36-82.1
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.36-82.1
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.37
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) updated to 5.6.37
* [MariaDB Backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup/) is now stable (GA)
* New [innochecksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum) options
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) for Ubuntu 16.10 "Yakkety" and Fedora 24
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2017-3636](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3636)
  * [CVE-2017-3641](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3641)
  * [CVE-2017-3653](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3653)
  * [CVE-2017-10286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10286)
  * [CVE-2017-10379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10379)
  * [CVE-2017-10384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10384)

A file format compatibility bug that was introduced in [MariaDB 10.1.0](mariadb-10-1-0-release-notes.md) was fixed in [MariaDB 10.1.21](mariadb-10121-release-notes.md).\
Using [page\_compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) or non-default [innodb\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) created files that were incompatible with [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) or MySQL 5.6. [MariaDB 10.1.21](mariadb-10121-release-notes.md) and higher will convert affected files from earlier [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) releases to a compatible format.**This prevents a downgrade to earlier** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **versions.**[See the commit for details.](https://github.com/MariaDB/server/commit/ab1e6fefd869242d962cb91a006f37bb9ad534a7)

## Changelog

For a complete list of changes made in [MariaDB 10.1.26](mariadb-10126-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10126-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
