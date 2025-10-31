# MariaDB 10.0.33 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.33) | [Release Notes](mariadb-10033-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10033-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 30 Oct 2017

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is a previous stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

This is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.37-82.2
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.37-82.2
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.38
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) updated to 5.6.38
* [CONNECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) updated to 1.6.0005
* [MDEV-12422](https://jira.mariadb.org/browse/MDEV-12422): [CHECK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table) no longer returns an error when run on a [CONNECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) table
* [MDEV-14051](https://jira.mariadb.org/browse/MDEV-14051): 'Undo log record is too big.' error occurring in very narrow range of string lengths
* [MDEV-13918](https://jira.mariadb.org/browse/MDEV-13918): Race condition between [INFORMATION\_SCHEMA.INNODB\_SYS\_TABLESTATS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tablestats-table) and [ALTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table)/[DROP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table)/[TRUNCATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/truncate-table)
* [MDEV-13838](https://jira.mariadb.org/browse/MDEV-13838): Wrong result after altering a partitioned table
* fixed bugs in InnoDB [FULLTEXT INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes)
  * [MDEV-12676](https://jira.mariadb.org/browse/MDEV-12676): InnoDB FTS duplicate key error
  * [MDEV-13051](https://jira.mariadb.org/browse/MDEV-13051): InnoDB crash after failed ADD INDEX and table\_definition\_cache eviction
  * [MDEV-13446](https://jira.mariadb.org/browse/MDEV-13446): fts\_create\_doc\_id() unnecessarily allocates 8 bytes for every inserted row
* [MDEV-13899](https://jira.mariadb.org/browse/MDEV-13899): [IMPORT TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#import-tablespace) may corrupt [ROW\_FORMAT=REDUNDANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview) tables
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2017-10378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10378), [MDEV-13819](https://jira.mariadb.org/browse/MDEV-13819)
  * [CVE-2017-10268](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10268)

## Changelog

For a complete list of changes made in [MariaDB 10.0.33](mariadb-10033-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10033-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
