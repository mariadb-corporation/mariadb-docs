# MariaDB 5.5.33 Release Notes

The most recent release in the [MariaDB 5.5](changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.33) | **Release Notes** | [Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5533-changelog.md) | [Overview of 5.5](changes-improvements-in-mariadb-5-5.md)

**Release date:** 17 Sep 2013

This is a [_**Stable**_](../../about/release-criteria.md) _**(GA)**_ release. In general this\
means that there are no known serious bugs, except for those marked as feature\
requests, that no bugs were fixed since last release that caused a notable code\
changes, and that we believe the code is ready for general usage (based on bug\
inflow).

**For a description of** [**MariaDB 5.5**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **see the**[**What is MariaDB 5.5?**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **page.**

For a list of changes made in this release, with links to detailed\
information on each push, see the [MariaDB 5.5.33 Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5533-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

## Security fixes

This release includes fixes for the following security vulnerabilities:

* [CVE-2013-5807](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-5807)
* [CVE-2013-3839](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-3839)

## Includes TokuDB Storage Engine

With this release of MariaDB we are pleased to announce the addition of the [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) storage engine from [Tokutek](https://www.tokutek.com/).

It is only available for the following distributions:

* Ubuntu 13.04 "Raring" 64-bit
* Ubuntu 12.10 "Quantal" 64-bit
* Debian 7 "Wheezy" 64-bit
* Fedora 18 64-bit
* Fedora 17 64-bit

The TokuDB package is available in the repositories of the above distributions.\
See [How to Enable TokuDB in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb/installing-tokudb) for\
instructions on installing the package and enabling TokuDB.

The version of TokuDB included with MariaDB is different from the version from\
Tokutek. See the [TokuDB Differences](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb/tokudb-differences) page for details.

## Includes MySQL 5.5.33 and XtraDB 5.5.33

This release includes MySQL 5.5.33. See [Changes in MySQL 5.5.33](https://dev.mysql.com/doc/relnotes/mysql/5.5/en/news-5-5-33.html) for what changed in MySQL.

Also included is [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) from Percona Server 5.5.33-rel31.1

## Other Notable Information

* MariaDB is now built with [jemalloc](https://www.canonware.com/jemalloc/) by default on Linux (not on Solaris or Windows).

Thanks, and enjoy MariaDB!

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
