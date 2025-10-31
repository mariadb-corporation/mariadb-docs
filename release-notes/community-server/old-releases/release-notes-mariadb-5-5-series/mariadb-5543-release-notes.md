# MariaDB 5.5.43 Release Notes

The most recent release in the [MariaDB 5.5](changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.43) | [Release Notes](mariadb-5543-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5543-changelog.md) | [Overview of 5.5](changes-improvements-in-mariadb-5-5.md)

**Release date:** 1 May 2015

This is a [_**Stable**_](../../about/release-criteria.md) _**(GA)**_ release. In general this\
means that there are no known serious bugs, except for those marked as feature\
requests, that no bugs were fixed since last release that caused notable code\
changes, and that we believe the code is ready for general usage (based on bug\
inflow).

**For a description of** [**MariaDB 5.5**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **see the**[**What is MariaDB 5.5?**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **page.**

For a list of changes made in this release, with links to detailed\
information on each push, see the [MariaDB 5.5.43 Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5543-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

### Deprecated Distributions

As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will\
be the final release of [MariaDB 5.5](changes-improvements-in-mariadb-5-5.md) for Fedora 19 "Schrödinger's Cat", Ubuntu\
10.04 LTS "Lucid", and Mint 9 LTS "Isadora". When the next version of [MariaDB\
5.5](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) is released, repositories for these distributions will go away.

### Updates & Bug Fixes

[MariaDB 5.5.43](mariadb-5543-release-notes.md) is a maintenance release. It includes several bugfixes and\
updates, including from MySQL 5.5.43. Notable updates include:

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.5.42-37.1
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to [version 7.5.6](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-5-6)
* [Audit Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) upgraded to 1.3.0, including the QUERY\_DCL filter option.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2015-0501](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0501)
  * [CVE-2015-2571](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2571)
  * [CVE-2015-0505](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0505)
  * [CVE-2015-0499](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0499)
  * [CVE-2015-4757](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4757)

A full list of all changes is in the [changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5543-changelog.md).

Thanks, and enjoy MariaDB!

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
