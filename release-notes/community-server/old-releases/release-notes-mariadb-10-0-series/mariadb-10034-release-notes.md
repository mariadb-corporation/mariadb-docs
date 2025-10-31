# MariaDB 10.0.34 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.34) | [Release Notes](mariadb-10034-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10034-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 30 Jan 2018

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is a previous stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

This is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.38-83.0
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.38-83.0
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.39
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) updated to 5.6.39
* [MDEV-12173](https://jira.mariadb.org/browse/MDEV-12173) - "Error: trying to do an operation on a dropped tablespace"
* [MDEV-7049](https://jira.mariadb.org/browse/MDEV-7049) - MySQL#74585 - InnoDB: Failing assertion: \*mbmaxlen < 5 in file ha\_innodb.cc line 1904
* [MDEV-14916](https://jira.mariadb.org/browse/MDEV-14916) - InnoDB reports warning for "Purge reached the head of the history list"
* [MDEV-14174](https://jira.mariadb.org/browse/MDEV-14174) - crash on start with innodb-track-changed-pages
* [MDEV-13205](https://jira.mariadb.org/browse/MDEV-13205) - InnoDB: Failing assertion: !dict\_index\_is\_online\_ddl(index) upon ALTER TABLE
* [MDEV-14799](https://jira.mariadb.org/browse/MDEV-14799) - After UPDATE of indexed columns, old values will not be purged from secondary indexes
* [MDEV-12827](https://jira.mariadb.org/browse/MDEV-12827) - Assertion failure when reporting duplicate key error in online table rebuild
* [MDEV-12323](https://jira.mariadb.org/browse/MDEV-12323) - Rollback progress log messages during crash recovery are intermixed with unrelated log messages
* [MDEV-12352](https://jira.mariadb.org/browse/MDEV-12352) - InnoDB shutdown should not be blocked by a large transaction rollback
* [MDEV-13797](https://jira.mariadb.org/browse/MDEV-13797) - InnoDB may hang if shutdown is initiated soon after startup while rolling back recovered incomplete transactions
* [MDEV-14140](https://jira.mariadb.org/browse/MDEV-14140) - IMPORT TABLESPACE must not go beyond FSP\_FREE\_LIMIT
* Backport [MDEV-13890](https://jira.mariadb.org/browse/MDEV-13890) from 10.2 (InnoDB/XtraDB shutdown failure)
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2018-2562](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2562)
  * [CVE-2018-2622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2622)
  * [CVE-2018-2640](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2640)
  * [CVE-2018-2665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2665)
  * [CVE-2018-2668](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2668)
  * [CVE-2018-2612](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2612)
  * [CVE-2018-3133](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3133)

## Changelog

For a complete list of changes made in [MariaDB 10.0.34](mariadb-10034-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10034-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
