# MariaDB 5.5.35 Release Notes

The most recent release in the [MariaDB 5.5](changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.35) | **Release Notes** | [Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5535-changelog.md) | [Overview of 5.5](changes-improvements-in-mariadb-5-5.md)

**Release date:** 29 Jan 2014

This is a [_**Stable**_](../../about/release-criteria.md) _**(GA)**_ release. In general this\
means that there are no known serious bugs, except for those marked as feature\
requests, that no bugs were fixed since last release that caused a notable code\
changes, and that we believe the code is ready for general usage (based on bug\
inflow).

**For a description of** [**MariaDB 5.5**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **see the**[**What is MariaDB 5.5?**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **page.**

For a list of changes made in this release, with links to detailed\
information on each push, see the [MariaDB 5.5.35 Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5535-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

### Updates & Bug Fixes

[MariaDB 5.5.35](mariadb-5535-release-notes.md) is a maintenance release. It includes all bugfixes and updates\
from the following:

* MySQL 5.5.35
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) from Percona-Server-5.5.35-rel33.0
* [OLD\_MODE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/old_mode), to emulate behavior from old MySQL/MariaDB versions.
* [EXTRACT (HOUR FROM ...)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/extract) now adheres to the SQL standard and returns values from 0 to 23. Previously it could return greater values.
* Also included are fixes for the following security vulnerabilities:
  * [CVE-2014-0412](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0412)
  * [CVE-2014-0401](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0401)
  * [CVE-2014-0437](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0437)
  * [CVE-2014-0420](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0420)
  * [CVE-2013-5908](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-5908)

Full details of all changes are in the [changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5535-changelog.md).

## Fedora, Ubuntu, and Mint

As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will\
be the final release of MariaDB for Fedora 18 "Spherical Cow", Ubuntu 13.04\
"Raring", and Mint 15 "Olivia". When the next version of [MariaDB 5.5](changes-improvements-in-mariadb-5-5.md) is\
released, repositories for these distributions will go away.

Thanks, and enjoy MariaDB!

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
