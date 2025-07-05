# MariaDB 10.0.4 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.4) |**Release Notes** |[Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1004-changelog.md) |[Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 16 Aug 2013

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current development version of MariaDB. It is built on the [MariaDB 5.5 series](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with backported and reimplemented\
features from MySQL 5.6 and entirely new features not found anywhere else.

[MariaDB 10.0.4](mariadb-1004-release-notes.md) is an [_**Alpha**_](../../../mariadb-release-criteria.md) release.\
This is the fifth 10.0-based release, and we are releasing it now to get it\
into the hands of any who might want to test it. Not all features planned for\
the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series are included in this release. Additional features will\
be pushed in future releases.**Do not use alpha releases on production systems.**

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

For a list of changes made in [MariaDB 10.0.4](mariadb-1004-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1004-changelog.md).

## Based on [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)

The [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series builds off of the [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) series. It also includes\
features imported from MySQL 5.6, and completely new features.

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

## Security fixes

This release includes fixes for the following security vulnerabilities:

* [CVE-2013-1861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-1861)
* [CVE-2013-3809](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-3809)
* [CVE-2013-3793](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-3793)
* [CVE-2013-3802](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-3802)
* [CVE-2013-3804](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-3804)
* [CVE-2013-3783](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-3783)
* [CVE-2013-3812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-3812)
* [CVE-2016-0502](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0502)

## Newly Implemented Features

* [MDEV-4438](https://jira.mariadb.org/browse/MDEV-4438) - [Spider storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider)
* [MDEV-4568](https://jira.mariadb.org/browse/MDEV-4568) - Port Percona response time distribution as audit plugin
* [MDEV-4702](https://jira.mariadb.org/browse/MDEV-4702) - Reduce usage of LOCK\_open

## Features and Fixes Merged or Backported from MySQL 5.6.10

* [MDEV-330](https://jira.mariadb.org/browse/MDEV-330) - Support for MySQL-5.6 created tables (frm and data files) that have columns of types TIME(N), DATETIME(N) and TIMESTAMP(N). Previously, an attempt to open such a table in MariaDB would return an error.
* [MDEV-3838](https://jira.mariadb.org/browse/MDEV-3838) - Support for standard SQL temporal literals
* [MDEV-4058](https://jira.mariadb.org/browse/MDEV-4058) - Merge the [host\_cache P\_S table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-host_cache-table)
* WL #5185 Remove deprecated 5.1 features
* InnoDB from MySQL 5.6.10
* [Performance schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/performance-schema) updates, including new defaults.
* [Information Schema updates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema), including new defaults.
* [InnoDB persistent statistics](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics).
* Online ALTER for InnoDB and thread information for in-place operations
* EXCHANGE PARTITION
* Partition selection
* For temporary tables created with the `CREATE TEMPORARY TABLE` statement, the privilege model has changed ([MySQL Bug #27480](https://bugs.mysql.com/bug.php?id=27480), Bug #11746602)
* GET DIAGNOSTICS statement

For full details, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1004-changelog.md).

## [CONNECT Storage Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) Updates

### New features added to CONNECT

1. The connection parameter of MYSQL type tables and PROXY tables\
   on MySQL tables can now refer to a [Federated](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/federatedx-storage-engine) server.
2. The SERVID special column is now implemented. It returns the Federated server\
   name for tables using one, the host name of the server for MYSQL tables,\
   "ODBC" for ODBC tables and "Current" for all other table types. For PROXY\
   and PROXY based tables, this value is the one of the source proxied table(s).

### Modifications to CONNECT Behavior

1. Table locking (read and write) is now supported. When a table is write\
   locked, indexes are not updated on table changes. They are when the table is\
   unlocked. Consequently, SELECT statements do not use indexing while locked.
2. CONNECT no longers uses the query cache. This is because it is working on\
   external data which is prone to be modified outside of MariaDB (it was also\
   causing a crash with PIVOT tables)

### Modifications to CONNECT Error messages

Some messages were changed from error to warning to prevent a server crash.\
Some have been added, in particular:

1. When trying to index a null-able column (not supported yet)
2. When inserting on an INI table without specifying the sectio name.
3. When specifying ENUM column (not supported yet)
4. Better message for CONNECT unspported commands

### CONNECT Engine Bugs fixed:

A few bugs were fixed, in particular:

* [MDEV-4494](https://jira.mariadb.org/browse/MDEV-4494): Unsupported use of nullable column for index is not caught,\
  causes assertion failure or unspecified error (122)
* [MDEV-4495](https://jira.mariadb.org/browse/MDEV-4495): Assertion failure in Diagnostics\_area::set\_error\_status or\
  unspecified error instead of a duplicate key error
* [MDEV-4524](https://jira.mariadb.org/browse/MDEV-4524): Server crashes when querying from multiple file CONNECT table
* [MDEV-4638](https://jira.mariadb.org/browse/MDEV-4638): Server crashes with an indexed not-null ENUM column
* [MDEV-4771](https://jira.mariadb.org/browse/MDEV-4771): Connection dies using table\_type=pivot
* [MDEV-4853](https://jira.mariadb.org/browse/MDEV-4853): DML on table\_type=INI gives no error even MySQLd has not the\
  privilege to change the file
* [MDEV-4854](https://jira.mariadb.org/browse/MDEV-4854): table\_type=mysql does not send the WHERE part (not a bug)
* [MDEV-4855](https://jira.mariadb.org/browse/MDEV-4855): If SERVID is not supported, it should be removed from doc.
* [MDEV-4878](https://jira.mariadb.org/browse/MDEV-4878): LOCK TABLE is not working with ConnectSE
* [MDEV-4881](https://jira.mariadb.org/browse/MDEV-4881): Pivot throws an error
* Fixed a bug causing the whole section to be deleted when deleting one key of\
  a INI table with layout=Row. The same happens for layout=column but this is\
  normal as one line is one section.
* Fixed a bug causing connect\_assisted\_discovery to fail on some table types\
  (WMI).
* A fix concerning a memory leak or uninitialised memory warning issued by\
  Valgrind.
* A few more code changes have been made to suppress compilation warnings.

## Other Features

Other features are planned for inclusion in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md). They are listed on the [What is MariaDB 10.0?](changes-improvements-in-mariadb-10-0.md) and Plans for 10x pages.

Thanks, and enjoy MariaDB!

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
