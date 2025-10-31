# MariaDB 10.1.46 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.46/) | [Release Notes](mariadb-10146-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10146-changelog.md) | [Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 10 Aug 2020

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is a previous stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.46](mariadb-10146-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

### Variables

* Limit [innodb\_encryption\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encryption_threads) to 255 ([MDEV-22258](https://jira.mariadb.org/browse/MDEV-22258)).
* Minimum value of [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length) raised to 8 (previously 4)\
  so fixed size [data types](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types) like [DOUBLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/double) and [BIGINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/bigint) are not truncated for lower values of max\_sort\_length ([MDEV-22715](https://jira.mariadb.org/browse/MDEV-22715)).

### InnoDB

* [Innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.49
* Fixed corruption in delete buffering ([MDEV-22497](https://jira.mariadb.org/browse/MDEV-22497))
* Fixed a deadlock in FLUSH TABLES…FOR EXPORT ([MDEV-22890](https://jira.mariadb.org/browse/MDEV-22890))
* InnoDB data file extension is not crash-safe ([MDEV-23190](https://jira.mariadb.org/browse/MDEV-23190))
* Minor fixes related to encryption and FULLTEXT INDEX
* Crash recovery fix ([MDEV-23190](https://jira.mariadb.org/browse/MDEV-23190))

### Replication

* Make the binlog dump thread to log into errorlog a requested GTID position ([MDEV-20428](https://jira.mariadb.org/browse/MDEV-20428))
* Fix stop of the optimistic parallel slave at requested START-SLAVE-UNTIL position ([MDEV-15152](https://jira.mariadb.org/browse/MDEV-15152))
* Properly handle `RESET MASTER TO` value, when the value exceeds the max allowed `2147483647` ([MDEV-22451](https://jira.mariadb.org/browse/MDEV-22451))
* Correct 'relay-log.info' updating by concurrent parallel workers ([MDEV-22806](https://jira.mariadb.org/browse/MDEV-22806))
* Eliminate deadlock involving parallel workers, `STOP SLAVE` and `FLUSH TABLES WITH READ LOCK` ([MDEV-23089](https://jira.mariadb.org/browse/MDEV-23089))

### Optimizer

* ALTER TABLE ... ANALYZE PARTITION ... with EITS reads and locks all rows ... ([MDEV-21472](https://jira.mariadb.org/browse/MDEV-21472))
* Print ranges in the optimizer trace created for non-indexed columns when `optimizer_use_condition_selectivity >2` Now the optimizer trace shows the ranges constructed while getting estimates from EITS ([MDEV-22665](https://jira.mariadb.org/browse/MDEV-22665))
* `LATERAL DERIVED` is not clearly visible in `EXPLAIN FORMAT=JSON`, make `LATERAL DERIVED` tables visible in `EXPLAIN FORMAT=JSON` output ([MDEV-17568](https://jira.mariadb.org/browse/MDEV-17568))

### Other

* [div\_precision\_increment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#div_precision_increment) is now taken into account for all intermediate calculations. Previously results could be unpredictable. Note that this means results will have a lower precision in some cases - see [div\_precision\_increment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#div_precision_increment) ([MDEV-19232](https://jira.mariadb.org/browse/MDEV-19232))
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.49-89.0
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.49-89.0
* MariaDB could crash after changing the query\_cache size ([MDEV-5924](https://jira.mariadb.org/browse/MDEV-5924))
* Errors and SIGSEGV on CREATE TABLE w/ various charsets ([MDEV-22111](https://jira.mariadb.org/browse/MDEV-22111))
* Crash in `CREATE TABLE AS SELECT` when the precision of returning type = 0 ([MDEV-22502](https://jira.mariadb.org/browse/MDEV-22502))
* XA: Reject DDL operations between PREPARE and COMMIT ([MDEV-22420](https://jira.mariadb.org/browse/MDEV-22420))
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2021-2022](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2022)

## Changelog

For a complete list of changes made in [MariaDB 10.1.46](mariadb-10146-release-notes.md) with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10146-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.1.46](mariadb-10146-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-5-5-10-4-14-10-3-24-10-2-33-and-10-1-46-now-available/).

A file format compatibility bug that was introduced in [MariaDB 10.1.0](mariadb-10-1-0-release-notes.md) was fixed in [MariaDB 10.1.21](mariadb-10121-release-notes.md).\
Using [page\_compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) or non-default [innodb\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) created files that were incompatible with [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) or MySQL 5.6. [MariaDB 10.1.21](mariadb-10121-release-notes.md) and higher will convert affected files from earlier [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) releases to a compatible format.**This prevents a downgrade to earlier** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **versions.**[See the commit for details.](https://github.com/MariaDB/server/commit/ab1e6fefd869242d962cb91a006f37bb9ad534a7)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
