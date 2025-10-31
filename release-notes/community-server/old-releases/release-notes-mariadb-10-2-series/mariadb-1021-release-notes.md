# MariaDB 10.2.1 Release Notes

The most recent release of [MariaDB 10.2](what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.1) | [Release Notes](mariadb-1021-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1021-changelog.md) | [Overview of 10.2](what-is-mariadb-102.md)

**Release date:** 4 Jul 2016

[MariaDB 10.2](what-is-mariadb-102.md) is the current development series of MariaDB. It is an evolution\
of [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.2.1](mariadb-1021-release-notes.md) is an [_**Alpha**_](../../about/release-criteria.md) release.

**Do not use&#x20;**_**Alpha**_**&#x20;releases on production systems!**

**For an overview of** [**MariaDB 10.2**](what-is-mariadb-102.md) **see the**[**What is MariaDB 10.2**](what-is-mariadb-102.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

This is the second alpha release in the [MariaDB 10.2](what-is-mariadb-102.md) series.

* Common Table Expressions - [WITH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/with)
* Support for [CHECK CONSTRAINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/constraint) ([MDEV-7563](https://jira.mariadb.org/browse/MDEV-7563)).
* Support for [DEFAULT with expressions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table#default) ([MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134)).
* [BLOB and TEXT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/blob-and-text-data-types) fields can now have a [DEFAULT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table#default) value.
* Lots of restrictions lifted for [Virtual computed columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/generated-columns).
* Views now support subqueries in the FROM clause ([MDEV-3944](https://jira.mariadb.org/browse/MDEV-3944))
* Number of supported decimals in [DECIMAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/decimal) has increased from `30` to `38`. ([MDEV-10138](https://jira.mariadb.org/browse/MDEV-10138))
* Optimizations for faster connection creation time.
* New variable for setting a directory for storing temporary non-tablespace InnoDB files, [innodb\_tmpdir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables).
* Temporary tables can be referred to many times in the same query ([MDEV-5535](https://jira.mariadb.org/browse/MDEV-5535))
* Various other optimizations and refactorings
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.30-76.3
* [Innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.31
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) updated to 5.6.31
* [PCRE library](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) updated to 8.39
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.30-76.3
* [HeidiSQL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/graphical-and-enhanced-clients/heidisql) updated to 9.3
* Various packages and bintar builds for POWER8 ppc64 and ppc64le architectures now available
* The default value of the [binlog\_checksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) system variable is now`CRC32`.
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 10.2](what-is-mariadb-102.md) for Ubuntu 15.10 "wily"

## Notes

**Do not use&#x20;**_**Alpha**_**&#x20;releases on production systems!**

## Changelog

For a complete list of changes made in [MariaDB 10.2.1](mariadb-1021-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1021-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
