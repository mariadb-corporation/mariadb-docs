# MariaDB 10.3.5 Release Notes

The most recent release of [MariaDB 10.3](what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](mariadb-10-3-39-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.5/) | [Release Notes](mariadb-1035-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1035-changelog.md) | [Overview of 10.3](what-is-mariadb-103.md)

**Release date:** 26 Feb 2018

[MariaDB 10.3](what-is-mariadb-103.md) is the current development series of MariaDB. It is an evolution\
of [MariaDB 10.2](../release-notes-mariadb-10-2-series/what-is-mariadb-102.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL.

[MariaDB 10.3.5](mariadb-1035-release-notes.md) is a [_**RC**_](../../about/release-criteria.md) release.

**Do not use&#x20;**_**non-GA**_**&#x20;releases on production systems!**

**For an overview of** [**MariaDB 10.3**](what-is-mariadb-103.md) **see the**[**What is MariaDB 10.3?**](what-is-mariadb-103.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* The PL/SQL stored procedure dialect (enabled with [sql\_mode=ORACLE](https://mariadb.com/docs/release-notes/compatibility-and-differences/sql_modeoracle)) now supports Oracle style packages. Support for the following statements has been added ([MDEV-10591](https://jira.mariadb.org/browse/MDEV-10591)):
  * [CREATE PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-package)
  * [CREATE PACKAGE BODY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-package-body)
  * [DROP PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-package)
  * [DROP PACKAGE BODY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-package-body)
  * [SHOW CREATE PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-package)
  * [SHOW CREATE PACKAGE BODY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-package-body)
* The [MyRocks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks) storage engine is now RC.
* Numerous performance improvements for high-concurrency load.
* Useless `@@system_versioning_innodb_algorithm_simple` server variable was removed.
* New [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) `SIMULTANEOUS_ASSIGNMENT` to make the SET part of the [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) statement evaluate all assignments simultaneously, not left-to-right.
* Numerous scalability and performance improvements to global data structures, including [MDEV-14756](https://jira.mariadb.org/browse/MDEV-14756), [MDEV-15019](https://jira.mariadb.org/browse/MDEV-15019), [MDEV-14482](https://jira.mariadb.org/browse/MDEV-14482), [MDEV-15059](https://jira.mariadb.org/browse/MDEV-15059), [MDEV-15104](https://jira.mariadb.org/browse/MDEV-15104)
* Correctness improvement - [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/truncate-table) honors transactional locks ([MDEV-15061](https://jira.mariadb.org/browse/MDEV-15061))
* Performance improvements to persistent data structures: [MDEV-15090](https://jira.mariadb.org/browse/MDEV-15090), [MDEV-15132](https://jira.mariadb.org/browse/MDEV-15132)
* If a user has the [SUPER privilege](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) but not the `DELETE HISTORY` privilege, running [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) will grant `DELETE HISTORY` as well.
* Added `Max_index_length` and `Temporary` to [SHOW TABLE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-table-status)

## Other Changes

* On Linux, shrink the core dumps by omitting the [InnoDB buffer pool](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-buffer-pool) ([MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814))
* Fix upgrades from earlier [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) versions ([MDEV-15370](https://jira.mariadb.org/browse/MDEV-15370))
* New status variable [innodb\_buffer\_pool\_load\_incomplete](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables) ([MDEV-11455](https://jira.mariadb.org/browse/MDEV-11455))
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), 10.3 binary tarball packages for GLIBC\_2.5 (that were built on CentOS 5) have been discontinued.

## Notable Bug Fixes merged from 10.2

[MariaDB 10.3.5](mariadb-1035-release-notes.md) includes all bug fixes from [MariaDB 10.2.13](../release-notes-mariadb-10-2-series/mariadb-10213-release-notes.md), including the following:

* [MDEV-11415](https://jira.mariadb.org/browse/MDEV-11415) Remove excessive undo logging during [ALTER TABLE…ALGORITHM=COPY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#algorithm)
* Faster startup when no crash recovery is deeded ([MDEV-15333](https://jira.mariadb.org/browse/MDEV-15333), [MDEV-13869](https://jira.mariadb.org/browse/MDEV-13869))

**Do not use&#x20;**_**non-GA**_**&#x20;releases on production systems!**

## Changelog

For a complete list of changes made in [MariaDB 10.3.5](mariadb-1035-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1035-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.3.5](mariadb-1035-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-3-5-mariadb-connector-j-2-2-2-1-7-2-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
