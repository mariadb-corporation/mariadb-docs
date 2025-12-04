# MariaDB 5.2.4 Release Notes

The most recent release in the [MariaDB 5.2 series](changes-improvements-in-mariadb-5-2.md) is:[**MariaDB 5.2.14**](mariadb-5214-release-notes.md)

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.2.4) | **Release Notes** | [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-524-changelog.md) |[Overview of 5.2](changes-improvements-in-mariadb-5-2.md)

**Release date:** 6 Dec 2010

This is a [stable release](../../about/release-criteria.md). In general this means there are\
no known serious bugs and we believe the code is ready for general usage. For a high-level description of [MariaDB 5.2](changes-improvements-in-mariadb-5-2.md) see the [MariaDB 5.2 overview](changes-improvements-in-mariadb-5-2.md).

See the [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-524-changelog.md) for a list of all changes included in this release.

## Includes [MariaDB 5.1.53](../release-notes-mariadb-5-1-series/mariadb-5153-release-notes.md)

[MariaDB 5.2.4](mariadb-524-release-notes.md) has all changes from [MariaDB 5.1.53](../release-notes-mariadb-5-1-series/mariadb-5153-release-notes.md), including MySQL 5.1.53.

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

## Includes [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-unmaintained/about-xtradb) 5.1.52-11.6

We have included XtraDB from Percona-server-5.1.52-11.6 in this version of\
MariaDB.

## New Packages

For this version of MariaDB we have started building Ubuntu 10.10 "Maverick"\
and Debian 6 "Squeeze" packages.

## Bug Fixes

Like [previous releases](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/release-notes/README.md), [MariaDB 5.2.4](mariadb-524-release-notes.md) includes several bug\
fixes and other improvements. Specific bugs fixed in [MariaDB 5.2.4](mariadb-524-release-notes.md) include:

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
