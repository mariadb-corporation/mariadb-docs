# MariaDB 5.1.55 Release Notes

The most recent release in the [MariaDB 5.1 series](changes-improvements-in-mariadb-5-1.md) is:[**MariaDB 5.1.67**](mariadb-5167-release-notes.md)

[Download](https://downloads.askmonty.org/mariadb/5.1.55) | **Release Notes** | [Changelog](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1) |[Overview of 5.1](changes-improvements-in-mariadb-5-1.md)

**Release date:** 1 Mar 2011

Get notified of new releases automatically by adding the [releases rss feed](https://montyprogram.com/news/feed/mariadb_releases) to your favorite feed reader or by [subscribing](https://mariadb.org) to the announce 'at' mariadb.org announcement list (this is a low traffic, announce-only list).

MariaDB may already be included in your favorite OS distribution. More information can be found [here](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb).

For a list of every change made in [MariaDB 5.1.55](mariadb-5155-release-notes.md), see the [Changelog](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1). For a high-level description of [MariaDB 5.1](changes-improvements-in-mariadb-5-1.md) see the [MariaDB 5.1 overview](changes-improvements-in-mariadb-5-1.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

In addition to the differences noted in previous [release notes](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/release-notes/README.md) and [changelogs](../../../connectors/odbc/changelogs/), the main\
differences between MariaDB and MySQL are:

## Includes MySQL 5.1.55

For [MariaDB 5.1.55](mariadb-5155-release-notes.md) we have merged in all of the upstream changes from MySQL\
5.1.54 and 5.1.55. The MySQL [5.1.54](https://dev.mysql.com/doc/refman/5.1/en/news-5-1-54.html) and [5.1.55](https://dev.mysql.com/doc/refman/5.1/en/news-5-1-55.html) release\
notes have details of what changes were made upstream by MySQL since 5.1.53.

## Includes [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-unmaintained/about-xtradb) 5.1.54-12.5

We have included XtraDB from Percona Server 5.1.54-12.5 in this version of\
MariaDB. See the Percona Server[release\
notes](https://www.percona.com/docs/wiki/percona-server:release_notes_51) for what changes were made upstream by Percona.

## New Debian and Ubuntu Repositories

For this version of MariaDB we are pleased to announce the availability of\
Debian and Ubuntu repositories that we will keep up-to-date going forward. The\
new repositories make use of our world-wide network of MariaDB mirrors and will\
enable hassle-free upgrades to the latest version of MariaDB as soon as it is\
released.

See [Installing MariaDB .deb Files](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files) for\
information how to setup your Debian or Ubuntu system to use the new\
repositories.

## RPM Package Signing

As part of the new Debian and Ubuntu repositories we have also [signed the RPM packages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/checking-mariadb-rpm-package-signatures).\
All RPM package releases going forward will be signed.

## New Downloads System

With this version of MariaDB we are also debuting a new [MariaDB downloads website](https://downloads.askmonty.org). This new site\
allows you to filter the various files to show only the ones you are interested\
in and it will attempt to locate the nearest mirror to you based on your IP\
address.

## Bug Fixes

Like [previous releases](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/release-notes/README.md), [MariaDB 5.1.55](mariadb-5155-release-notes.md) includes several bug\
fixes and other improvements. Specific bugs fixed in [MariaDB 5.1.55](mariadb-5155-release-notes.md) include:

* Various [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) storage engine fixes:
  * [Bug #716890](https://bugs.launchpad.net/bugs/716890) Pre- and post-recovery crash in Aria
  * [Bug #624099](https://bugs.launchpad.net/bugs/624099) ma\_close.c:75: maria\_close: Assertion \`share->in\_trans == 0' failed on UNLOCK TABLES
  * [Bug #700623](https://bugs.launchpad.net/bugs/700623) Aria recovery: ma\_blockrec.c:3930: \_ma\_update\_at\_original\_place: Assertion \`block->org\_bitmap\_value == ..
  * [Bug #670356](https://bugs.launchpad.net/bugs/670356) Aria table "is marked as crashed and should be repaired"
  * [Bug #695006](https://bugs.launchpad.net/bugs/695006) Queries with "converting HEAP to Aria" status do not respond to KILL QUERY
  * [Bug #619731](https://bugs.launchpad.net/bugs/619731) Aria recovery corruption "Page 1: Row: 1 has an extent with wrong information in bitmap"
* Various Windows fixes
  * [Bug #688404](https://bugs.launchpad.net/bugs/688404) Fix pbxt crashes on Windows 64 (misalignment on SSE instruction)
  * [Bug #473914](https://bugs.launchpad.net/bugs/473914) mysql\_client\_test fail on windows x64
  * [Bug #686184](https://bugs.launchpad.net/bugs/686184) merge\_debug test fails in Windows debug compilation
* [Bug #585688](https://bugs.launchpad.net/bugs/585688) maridb crashes in federatedx code
* [Bug #702310](https://bugs.launchpad.net/bugs/702310) Assertion \`table\_ref->has\_record' failed with small value for join\_buffer\_size
* [Bug #675118](https://bugs.launchpad.net/bugs/675118) Elimination of a table results in an invalid execution plan
* [Bug #686010](https://bugs.launchpad.net/bugs/686010) maria.optimize corrupts stack around alloca() call
* [Bug #687320](https://bugs.launchpad.net/bugs/687320) Fix sporadic test failures in innodb\_mysql.test and partition\_innodb\_semi\_consistent.test
* [Bug #677407](https://bugs.launchpad.net/bugs/677407) / [MySQL Bug #48883](https://bugs.mysql.com/bug.php?id=48883) Stale data in INFORMATION\_SCHEMA.INNODB\_LOCKS
* and others...

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
