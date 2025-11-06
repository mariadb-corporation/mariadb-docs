# MariaDB 11.1.0 Release Notes

The most recent release of [MariaDB 11.1](what-is-mariadb-111.md) is:[**MariaDB 11.1.6**](mariadb-11-1-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.1.6/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.1.6/)

[Download](https://downloads.mariadb.org/mariadb/11.1.0) | [Release Notes](../release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md) | [Changelog](../../changelogs/11.0/mariadb-11-0-1-changelog.md) | [Overview of 11.1](what-is-mariadb-111.md)

**Release date:** 27 Mar 2023

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

[MariaDB 11.1](what-is-mariadb-111.md) is a current development series of MariaDB, and will be maintained for one year after its Generally Available release. It is an evolution of [MariaDB 11.0](../release-notes-mariadb-11-0-series/what-is-mariadb-110.md) with several entirely new features.

[MariaDB 11.1.0](mariadb-11-1-0-release-notes.md) is a single preview release. Features are to be considered preview, and none are guaranteed to make it into [MariaDB 11.1](what-is-mariadb-111.md).

The preview is available as a container **quay.io/mariadb-foundation/mariadb-devel:11.1-preview**.

**For an overview of** [**MariaDB 11.1**](what-is-mariadb-111.md) **see the**[**What is MariaDB 11.1?**](what-is-mariadb-111.md) **page.**

Thanks, and enjoy MariaDB!

## InnoDB

* Remove [innodb\_defragment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_defragment) and related parameters ([MDEV-30545](https://jira.mariadb.org/browse/MDEV-30545))

## Optimizer

* [Semi-join optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/semi-join-subquery-optimizations) for single-table [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update)/[DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) statements. Update and delete statements that use subqueries can now use all subquery optimization strategies that MariaDB offers, so now if you use subqueries in UPDATE or DELETE, these statements will likely be much faster ([MDEV-7487](https://jira.mariadb.org/browse/MDEV-7487))
* Queries with the [DATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/date-function) or [YEAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/year) functions comparing against a constant can now make use of indexes, so these will be noticeably quicker in certain instances. For example `SELECT * FROM t2 WHERE YEAR(a) = 2019` or `SELECT * FROM t2 WHERE DATE(a) <= '2017-01-01'` ([MDEV-8320](https://jira.mariadb.org/browse/MDEV-8320))

## General

* ALTER ONLINE TABLE - not released in the final [MariaDB 11.1](what-is-mariadb-111.md) ([MDEV-16329](https://jira.mariadb.org/browse/MDEV-16329))

## JSON

* [JSON\_SCHEMA\_VALID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_schema_valid) function for validating a JSON schema ([MDEV-27128](https://jira.mariadb.org/browse/MDEV-27128))

## mariadb-backup

* Rename [mariadb-backup’s](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup) xtrabackup\_\* files to mariadb\_backup\_\* ([MDEV-18931](https://jira.mariadb.org/browse/MDEV-18931))

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
