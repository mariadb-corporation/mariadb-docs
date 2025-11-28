# MariaDB 10.4.5 Release Notes

The most recent release of [MariaDB 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) is:[**MariaDB 10.4.34**](mariadb-10-4-34-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.5) | [Release Notes](mariadb-1045-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1045-changelog.md) | [Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 21 May 2019

[MariaDB 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) is the current _development_ series of MariaDB. It is an evolution\
of [MariaDB 10.3](../release-notes-mariadb-10-3-series/what-is-mariadb-103.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL.

[MariaDB 10.4.5](mariadb-1045-release-notes.md) is a [_**Release Candidate (RC)**_](../../about/release-criteria.md) release.

**Do not use non-stable (non-GA) releases in production!**

**For an overview of** [**MariaDB 10.4**](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) **see the**[**What is MariaDB 10.4?**](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

### General Server

* New [mysqlimport](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqlimport) option, `--ignore-foreign-keys` ([MDEV-788](https://jira.mariadb.org/browse/MDEV-788)).
* Setting [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) to `MSSQL` implements a limited subset of Microsoft SQL Server's language. See [SQL\_MODE=MSSQL](https://mariadb.com/docs/release-notes/compatibility-and-differences/sql_modemssql) ([MDEV-19142](https://jira.mariadb.org/browse/MDEV-19142)).
* Add [CAST(expr AS FLOAT)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/cast) ([MDEV-16872](https://jira.mariadb.org/browse/MDEV-16872)).
* List of slave transaction errors that will result in a retry rather than a halt ([slave\_transaction\_retry\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#slave_transaction_retry_errors)) have been increased by default, assisting [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) setups to be more robust ([MDEV-16543](https://jira.mariadb.org/browse/MDEV-16543)).
* [MDEV-15458](https://jira.mariadb.org/browse/MDEV-15458) - Segfault in heap\_scan() upon UPDATE after ADD SYSTEM VERSIONING
* [MDEV-19235](https://jira.mariadb.org/browse/MDEV-19235) - MariaDB Server compiled for 128 Indexes crashes at startup

### JSON

* [JSON\_MERGE\_PATCH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_merge_patch) and [JSON\_MERGE\_PRESERVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_merge_preserve) ([MDEV-13992](https://jira.mariadb.org/browse/MDEV-13992))

### InnoDB

* Merge InnoDB changes from MySQL 5.6.44 and 5.7.26
* Fixes of corruption or crashes: [MDEV-19241](https://jira.mariadb.org/browse/MDEV-19241), [MDEV-13942](https://jira.mariadb.org/browse/MDEV-13942), [MDEV-19385](https://jira.mariadb.org/browse/MDEV-19385), [MDEV-16060](https://jira.mariadb.org/browse/MDEV-16060), [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220), [MDEV-17540](https://jira.mariadb.org/browse/MDEV-17540)
* InnoDB recovery fixes and speedup: [MDEV-12699](https://jira.mariadb.org/browse/MDEV-12699), [MDEV-19356](https://jira.mariadb.org/browse/MDEV-19356)

### Encryption

* [MDEV-14398](https://jira.mariadb.org/browse/MDEV-14398) - innodb\_encrypt\_tables will work even with innodb\_encryption\_rotate\_key\_age=0

### System-Versioned Tables

* [MDEV-15966](https://jira.mariadb.org/browse/MDEV-15966) - [System-versioned tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) are now protected from [TRUNCATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/truncate-table) statements.

### Information schema

* [MDEV-19490](https://jira.mariadb.org/browse/MDEV-19490) show tables fails when selecting the information\_schema database

### Statistics

* [MDEV-19407](https://jira.mariadb.org/browse/MDEV-19407) - Assertion \`field->table->stats\_is\_read' failed in is\_eits\_usable
* New status variable, [Aborted\_connects\_preauth](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#aborted_connects_preauth), that records the number of connection attempts that were aborted prior to authentication ([MDEV-19277](https://jira.mariadb.org/browse/MDEV-19277)).

### Packaging

* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this is the last release of [MariaDB 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) for Fedora 28
* Packages and a repository for Fedora 30 and Ubuntu 19.04 "disco" have been added with this release, visit the [Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/) for instructions on adding the repository

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2019-2614](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2614)
  * [CVE-2019-2627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2627)
  * [CVE-2019-2628](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2628)

## Changelog

For a complete list of changes made in [MariaDB 10.4.5](mariadb-1045-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1045-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.4.5](mariadb-1045-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-4-5-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
