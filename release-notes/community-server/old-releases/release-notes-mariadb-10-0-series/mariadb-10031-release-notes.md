# MariaDB 10.0.31 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.31) | [Release Notes](mariadb-10031-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10031-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 23 May 2017

MariaDB 10.0 is a previous stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

This is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.36-82.0
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.36-82.0
* [Innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.36
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) updated to 5.6.36
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) for Ubuntu 12.04 LTS "Precise" and Mint 13 LTS "Maya"
* [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520): Extending an InnoDB data file unnecessarily allocates a large memory buffer on Windows
* [MDEV-11027](https://jira.mariadb.org/browse/MDEV-11027): InnoDB log recovery is too noisy
* [MDEV-12091](https://jira.mariadb.org/browse/MDEV-12091): Shutdown fails to wait for rollback of recovered transactions to finish
* [MDEV-12534](https://jira.mariadb.org/browse/MDEV-12534): Use atomic operations whenever available
* [MDEV-12674](https://jira.mariadb.org/browse/MDEV-12674): Innodb\_row\_lock\_current\_waits has overflow
* [MDEV-12188](https://jira.mariadb.org/browse/MDEV-12188): information schema - errors populating fail to free memory, unlock mutexes
* [MDEV-12358](https://jira.mariadb.org/browse/MDEV-12358): Fixes for GCC 7
* Miscellaneous compiler warning fixes
* [MDEV-6262](https://jira.mariadb.org/browse/MDEV-6262): Fixes from coverity report on MariaDB
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2017-3308](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3308)
  * [CVE-2017-3309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3309)
  * [CVE-2017-3453](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3453)
  * [CVE-2017-3456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3456)
  * [CVE-2017-3464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3464)

## Changelog

For a complete list of changes made in [MariaDB 10.0.31](mariadb-10031-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10031-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
