# MariaDB 10.2.18 Release Notes

The most recent release of [MariaDB 10.2](what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.18) | [Release Notes](mariadb-10218-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10218-changelog.md) | [Overview of 10.2](what-is-mariadb-102.md)

**Release date:** 25 Sep 2018

[MariaDB 10.2](what-is-mariadb-102.md) is the previous stable series of MariaDB. It is an evolution\
of [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.2.18](mariadb-10218-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.2**](what-is-mariadb-102.md) **see the**[**What is MariaDB 10.2?**](what-is-mariadb-102.md) **page.**

Upgrading from earlier 10.2.x versions earlier than 10.2.17 is **highly recommended** for all **Galera** users due to bug [MDEV-12837](https://jira.mariadb.org/browse/MDEV-12837) which caused serious stability issues with earlier versions. See the bug issue page for more information.

Thanks, and enjoy MariaDB!

## Notable Changes

* [MDEV-15511](https://jira.mariadb.org/browse/MDEV-15511) - if available, stunnel can be used during [Galera rsync SST](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster#rsync)
* [MDEV-15088](https://jira.mariadb.org/browse/MDEV-15088) - Remove debuginfo files from Windows .zip files and put in optional supplemental .zip file
* [MDEV-16791](https://jira.mariadb.org/browse/MDEV-16791) - [mariadb-backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup): Support DDL commands during backup
* [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) - Refuse MLOG\_TRUNCATE in mariadb-backup
* [MDEV-16934](https://jira.mariadb.org/browse/MDEV-16934) - add new system variable [eq\_range\_index\_dive\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#eq_range_index_dive_limit) to speed up queries that new long nested `IN` lists. The default value, for backward compatibility, is 0 meaning "unlimited"./25.
* The [Galera library](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md) in the repositories has been updated to version 25.3.24.

### Bug Fixes

* [MDEV-13333](https://jira.mariadb.org/browse/MDEV-13333) - errors on InnoDB lock conflict
* Report all InnoDB redo log corruption
* [MDEV-17043](https://jira.mariadb.org/browse/MDEV-17043) - Purge of indexed virtual columns may cause hang on table-rebuilding DDL
* [MDEV-16868](https://jira.mariadb.org/browse/MDEV-16868) - corruption of InnoDB temporary tables
* [MDEV-16465](https://jira.mariadb.org/browse/MDEV-16465) - Invalid (old?) table or database name or hang in ha\_innobase::delete\_table and log semaphore wait upon concurrent DDL with foreign keys
* [MDEV-17026](https://jira.mariadb.org/browse/MDEV-17026) - Assertion srv\_undo\_sources || ... failed on slow shutdown
* [MDEV-10754](https://jira.mariadb.org/browse/MDEV-10754) - wsrep\_sst\_rsync does not support innodb\_data\_home\_dir

### Code Cleanup

* [MDEV-16557](https://jira.mariadb.org/browse/MDEV-16557) - Remove INNOBASE\_SHARE
* [MDEV-16136](https://jira.mariadb.org/browse/MDEV-16136) - Simplify trx\_lock\_t memory management
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2019-2503](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2503)
  * [CVE-2021-2174](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2174)

When upgrading from [MariaDB 10.2.16](mariadb-10216-release-notes.md) or earlier to [MariaDB 10.2.17](mariadb-10217-release-notes.md) or higher,\
running [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) is **required** due to changes introduced in[MDEV-14637](https://jira.mariadb.org/browse/MDEV-14637).

## Changelog

For a complete list of changes made in [MariaDB 10.2.18](mariadb-10218-release-notes.md) with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10218-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.2.18](mariadb-10218-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-2-18-and-mariadb-connector-node-js-2-0-0-now-available).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
