# MariaDB 10.4.7 Release Notes

The most recent release of [MariaDB 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) is:[**MariaDB 10.4.34**](mariadb-10-4-34-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.7/) | [Release Notes](mariadb-1047-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1047-changelog.md) | [Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 31 Jul 2019

[MariaDB 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) is the current _stable_ series of MariaDB. It is an evolution\
of [MariaDB 10.3](../release-notes-mariadb-10-3-series/what-is-mariadb-103.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL.

[MariaDB 10.4.7](mariadb-1047-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.4**](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) **see the**[**What is MariaDB 10.4?**](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

Notable changes of this release include:

* [MDEV-19922](https://jira.mariadb.org/browse/MDEV-19922): [HeidiSQL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/graphical-and-enhanced-clients/heidisql) updated to 10.2
* [MDEV-19795](https://jira.mariadb.org/browse/MDEV-19795): Merge upstream [MyRocks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks).
* [MDEV-17228](https://jira.mariadb.org/browse/MDEV-17228): Encrypted temporary tables are not encrypted.
* [MDEV-18328](https://jira.mariadb.org/browse/MDEV-18328): [Disks Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/disks-plugin) is now stable and requires the [FILE privilege](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant).
* [MDEV-16508](https://jira.mariadb.org/browse/MDEV-16508): [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) - [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) not maintained between spider node and data nodes.
* Merge relevant InnoDB changes from MySQL 5.7.27
* Adjust spin loops to the x86 PAUSE instruction latency ([MDEV-19845](https://jira.mariadb.org/browse/MDEV-19845))
* [MDEV-20102](https://jira.mariadb.org/browse/MDEV-20102): When the ctas from a big table is interrupted ,then you can't drop or recreate the table
* [MDEV-19292](https://jira.mariadb.org/browse/MDEV-19292): InnoDB's row size calculations were fixed, which might result in "Row size too large" errors when creating or altering tables with lots columns. This can occur even if previous MariaDB releases did not throw errors for the same tables. Some workarounds are listed at [InnoDB Row Formats Overview: Upgrading Causes Row Size Too Large Errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview#upgrading-causes-row-size-too-large-errors).
* ALTER TABLE: [MDEV-15641](https://jira.mariadb.org/browse/MDEV-15641), [MDEV-19630](https://jira.mariadb.org/browse/MDEV-19630), [MDEV-19916](https://jira.mariadb.org/browse/MDEV-19916), [MDEV-19974](https://jira.mariadb.org/browse/MDEV-19974), [MDEV-17301](https://jira.mariadb.org/browse/MDEV-17301), [MDEV-18266](https://jira.mariadb.org/browse/MDEV-18266)
* Indexed virtual columns: [MDEV-16222](https://jira.mariadb.org/browse/MDEV-16222), [MDEV-17005](https://jira.mariadb.org/browse/MDEV-17005), [MDEV-19870](https://jira.mariadb.org/browse/MDEV-19870)
* FULLTEXT INDEX: [MDEV-14154](https://jira.mariadb.org/browse/MDEV-14154)
* Encryption: [MDEV-17228](https://jira.mariadb.org/browse/MDEV-17228), [MDEV-19914](https://jira.mariadb.org/browse/MDEV-19914)
* Galera + FOREIGN KEY: [MDEV-19660](https://jira.mariadb.org/browse/MDEV-19660)
* Recovery & mariadb-backup: [MDEV-19978](https://jira.mariadb.org/browse/MDEV-19978)
* [MDEV-20091](https://jira.mariadb.org/browse/MDEV-20091): DROP TEMPORARY table is logged despite no CREATE was logged
* [MDEV-19871](https://jira.mariadb.org/browse/MDEV-19871): Add page id matching check in innochecksum tool
* [MDEV-20179](https://jira.mariadb.org/browse/MDEV-20179): Server hangs on shutdown during installation of Spider
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) for OpenSUSE 42.3 and Ubuntu 18.10 "Cosmic"
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2019-2805](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2805)
  * [CVE-2019-2740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2740)
  * [CVE-2019-2739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2739)
  * [CVE-2019-2737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2737)
  * [CVE-2019-2758](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2758)
  * [CVE-2020-2922](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2922)
  * [CVE-2021-2007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2007)

## Changelog

For a complete list of changes made in [MariaDB 10.4.7](mariadb-1047-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1047-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.4.7](mariadb-1047-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-4-7-10-3-17-10-2-26-10-1-41-and-5-5-65-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
