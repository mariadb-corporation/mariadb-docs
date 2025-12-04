# MariaDB 5.1.53 Release Notes

The most recent release in the [MariaDB 5.1 series](changes-improvements-in-mariadb-5-1.md) is:[**MariaDB 5.1.67**](mariadb-5167-release-notes.md)

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.1.53) | **Release Notes** | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5153-changelog.md) |[Overview of 5.1](changes-improvements-in-mariadb-5-1.md)

**Release date:** 6 Dec 2010

For a list of every change made in this release, see the [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5153-changelog.md). For a description of this release see the [MariaDB 5.1 overview](changes-improvements-in-mariadb-5-1.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

In addition to the differences noted in previous [release notes](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/release-notes/README.md) and [changelogs](../../../connectors/odbc/changelogs/), the main\
differences between MariaDB and MySQL are:

## Includes MySQL 5.1.53

For [MariaDB 5.1.53](mariadb-5153-release-notes.md) we have merged in all of the upstream changes from MySQL\
5.1.52 and 5.1.53. The MySQL [5.1.52](https://dev.mysql.com/doc/refman/5.1/en/news-5-1-52.html) and [5.1.53](https://dev.mysql.com/doc/refman/5.1/en/news-5-1-53.html) release\
notes have details of what changes were made upstream by MySQL since 5.1.51.

## Includes [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-unmaintained/about-xtradb) 5.1.52-11.6

We have included XtraDB from Percona-server-5.1.52-11.6 in this version of\
MariaDB.

## New Packages

For this version of MariaDB we have started building Ubuntu 10.10 "Maverick"\
and Debian 6 "Squeeze" packages.

## Bug Fixes

Like [previous releases](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/release-notes/README.md), [MariaDB 5.1.53](mariadb-5153-release-notes.md) includes several bug\
fixes and other improvements. Specific bugs fixed in [MariaDB 5.1.53](mariadb-5153-release-notes.md) include:

* [Bug #643463](https://bugs.launchpad.net/bugs/643463) slow shutdown of XtraDB
* A fix from MySQL 5.1.52 for a serious regression: [Bug #678047](https://bugs.launchpad.net/bugs/678047) and [MySQL Bug #56821](https://bugs.mysql.com/bug.php?id=56821) Windows service cannot start
* Various fixes for .deb packaging:
  * [Bug #675185](https://bugs.launchpad.net/bugs/675185) mysqld\_safe hangs spinning at 100% CPU
  * [Bug #509535](https://bugs.launchpad.net/bugs/509535) .debs should link with system libraries, not bundled
  * [Bug #674812](https://bugs.launchpad.net/bugs/674812) PHP compile failure
  * [Bug #616307](https://bugs.launchpad.net/bugs/616307) Upgrade failure on Debian 6 "Squeeze"
* and others...

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
