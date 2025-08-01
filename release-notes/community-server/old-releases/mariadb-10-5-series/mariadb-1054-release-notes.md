# MariaDB 10.5.4 Release Notes

{% include "../../../.gitbook/includes/latest-10-5.md" %}

<a href="https://downloads.mariadb.org/mariadb/10.5.4/" class="button primary">Download</a> <a href="mariadb-1054-release-notes.md" class="button secondary">Release Notes</a> <a href="../../changelogs/changelogs-mariadb-105-series/mariadb-1054-changelog.md" class="button secondary">Changelog</a> <a href="what-is-mariadb-105.md" class="button secondary">Overview of 10.5</a>

**Release date:** 24 Jun 2020

[MariaDB 10.5](what-is-mariadb-105.md) is the current _stable_ series of MariaDB. It is an evolution\
of [MariaDB 10.4](../release-notes-mariadb-10-4-series/what-is-mariadb-104.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL.

[MariaDB 10.5.4](mariadb-1054-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

Thanks, and enjoy MariaDB!

## Notable Changes

This is the first Stable (GA) release in the [MariaDB 10.5](what-is-mariadb-105.md) series.

* This release of MariaDB Server includes the [S3 storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine). Note, that plugins have [independent maturity levels](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema) and S3 storage engine in 10.5.4 has Alpha maturity.
* This release of MariaDB Server includes the [MariaDB ColumnStore](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) storage engine. Note, that plugins have [independent maturity levels](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema) and MariaDB ColumnStore in 10.5.4 has Beta maturity.
* New [Gamma](../../about/release-criteria.md) version of the [Spider Storage Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider), 3.3.15.
* [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) now reliably deletes table remnants inside a storage engine even if the .frm file is missing ([MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412))
* Accelerated `crc32()` function for AMD64, ARMv8, POWER 8 ([MDEV-22669](https://jira.mariadb.org/browse/MDEV-22669))
* Lots of bug fixes, see the [changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1054-changelog.md).
* [Galera wsrep library](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-guide) updated to 26.4.5

### Variables

* Limit [innodb\_encryption\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encryption_threads) to 255 ([MDEV-22258](https://jira.mariadb.org/browse/MDEV-22258)).
* Minimum value of [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#max_sort_length) raised to 8 (previously 4)\
  so fixed size [data types](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types) like [DOUBLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/double) and [BIGINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/bigint) are not truncated for lower values of max\_sort\_length ([MDEV-22715](https://jira.mariadb.org/browse/MDEV-22715)).

### InnoDB

* [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) improvements: [MDEV-8069](https://jira.mariadb.org/browse/MDEV-8069), [MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412), [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456)
* InnoDB Performance improvements: [MDEV-15053](https://jira.mariadb.org/browse/MDEV-15053), [MDEV-22593](https://jira.mariadb.org/browse/MDEV-22593), [MDEV-22697](https://jira.mariadb.org/browse/MDEV-22697), [MDEV-22871](https://jira.mariadb.org/browse/MDEV-22871), [MDEV-22841](https://jira.mariadb.org/browse/MDEV-22841)

## Changelog

For a complete list of changes made in [MariaDB 10.5.4](mariadb-1054-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1054-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.5.4](mariadb-1054-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-5-4-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
