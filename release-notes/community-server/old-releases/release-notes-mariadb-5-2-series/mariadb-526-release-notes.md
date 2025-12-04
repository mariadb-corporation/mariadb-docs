# MariaDB 5.2.6 Release Notes

The most recent release in the [MariaDB 5.2 series](changes-improvements-in-mariadb-5-2.md) is:[**MariaDB 5.2.14**](mariadb-5214-release-notes.md)

[Download](https://downloads.askmonty.org/mariadb/5.2.6) |**Release Notes** |[Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-526-changelog.md) |[Overview of 5.2](changes-improvements-in-mariadb-5-2.md)

**Release date:** 12 May 2011

[MariaDB 5.2.6](mariadb-526-release-notes.md) is a [Stable release](../../about/release-criteria.md). In general this means there are no known serious bugs and we believe the code is ready for general usage. A "stable" MariaDB release is equivalent to a MySQL "GA" release.

For a high-level description of [MariaDB 5.2.6](mariadb-526-release-notes.md) see the [What is MariaDB 5.2](changes-improvements-in-mariadb-5-2.md) page.

For a list of every change made in [MariaDB 5.2.6](mariadb-526-release-notes.md), including the various bugs\
that were fixed and links to detailed information on each push, see the [MariaDB 5.2.6 Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-526-changelog.md). For a high-level description\
of [MariaDB 5.2](changes-improvements-in-mariadb-5-2.md) see the [MariaDB 5.2 Overview](changes-improvements-in-mariadb-5-2.md) page.

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

Be notified of new releases automatically by adding the [releases rss feed](https://montyprogram.com/news/feed/mariadb_releases) to\
your favorite feed reader or by [subscribing](https://mariadb.org) to the\
announce 'at' mariadb.org announcement list (this is a low traffic,\
announce-only list).

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the [Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

[MariaDB 5.2.6](mariadb-526-release-notes.md) contains the following changes:

## Includes Updates from MySQL 5.1

MariaDB includes a merge from MySQL 5.1 bazaar trunk. This merge does\
not correspond to a particular version of MySQL, but includes part of MySQL\
5.1.57 and part of 5.1.58. The actual revision merged is`revid:nirbhay.choubey@oracle.com-20110427115410-vpeshiv6u5snkvzi` and the changes can be found in the source at [Revision #2643.124.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.124.2) .

## Includes XtraDB 5.1.56-12.7

We have included [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-unmaintained/about-xtradb) from Percona Server 5.1.56-12.7 in\
this version of MariaDB. See the Percona Server[release\
notes](https://www.percona.com/docs/wiki/percona-server:release_notes_51) for what changes were made upstream by Percona since Percona Server\
5.1.54-12.5 (the version of XtraDB included in [MariaDB 5.2.5](mariadb-525-release-notes.md)).

## Ubuntu 11.04 "Natty" Packages Now Available

In this version of MariaDB we have started building .deb packages for Ubuntu\
11.04 "Natty Narwhal". Both i386 and x86\_64 packages are available.

See [Installing MariaDB .deb Files](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files) for\
information how to setup your Debian or Ubuntu system to use the new\
repositories.

## 64-bit Packages for Windows

In addition to packages for 32-bit Windows, we now also have 64-bit Windows\
packages in this version of MariaDB.

## New Windows MSI Installer

In this version of MariaDB we have done a lot of work on our Windows builds and\
we have created a new MSI installer for MariaDB which has lots of improvements\
over the old .exe installer.

See [Installing MariaDB MSI Packages on Windows](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows)\
for more details and instructions on how to use the new installer.

## Improved Windows ZIP Packages

The Windows ZIP package has been improved in this version of MariaDB. See [Installing MariaDB Windows ZIP packages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-windows-zip-packages)\
for more details.

## New Windows-specific mysql\_install\_db

A Windows-specific version of mysql\_install\_db is being introduced in the\
Windows builds of this version of MariaDB. `mysql_install_db.exe` is\
comparable to the shell script `mysql_install_db` that is used on Unix-like\
platforms, but with several Windows-specific enhancements.

See the [mysql\_install\_db.exe](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/installing-system-tables-mariadb-install-db/mariadb-install-db-exe) page for details.

## Windows Upgrade Wizard

In this version of MariaDB there is an upgrade wizard for converting MySQL\
instances to MariaDB.

See [Upgrading MariaDB on Windows](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-mariadb-on-windows) for\
instructions on using the upgrade wizard.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
