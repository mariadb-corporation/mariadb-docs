# MariaDB 10.4.1 Release Notes

The most recent release of [MariaDB 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) is:[**MariaDB 10.4.34**](mariadb-10-4-34-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.1/) | [Release Notes](mariadb-1041-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1041-changelog.md) | [Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 20 Dec 2018

[MariaDB 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) is the current _development_ series of MariaDB. It is an evolution of [MariaDB 10.3](../release-notes-mariadb-10-3-series/what-is-mariadb-103.md) with several entirely new features not found anywhere else and with backported and reimplemented features from MySQL.

[MariaDB 10.4.1](mariadb-1041-release-notes.md) is a [_**Beta**_](../../about/release-criteria.md) release.

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

**For an overview of** [**MariaDB 10.4**](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) **see the**[**What is MariaDB 10.4?**](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

This will be the first beta release in the [MariaDB 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) series.

Notable changes of this release include:

### Syntax

* New [FLUSH SSL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) command to reload SSL certificates without server restart ([MDEV-16266](https://jira.mariadb.org/browse/MDEV-16266))
* New `CAST` target — `CAST(x AS INTERVAL DAY_SECOND(N))` ([MDEV-17776](https://jira.mariadb.org/browse/MDEV-17776))

### Variables

* New [sql-mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) setting, `TIME_ROUND_FRACTIONAL` ([MDEV-16991](https://jira.mariadb.org/browse/MDEV-16991))
* Two new values for the variable [use\_stat\_tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#use_stat_tables): `COMPLEMENTARY_FOR_QUERIES` and `PREFERABLY_FOR_QUERIES` ([MDEV-17255](https://jira.mariadb.org/browse/MDEV-17255))
* [Engine Independent Table Statistics](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics) is now enabled by default; new default values are [use\_stat\_tables=PREFERABLY\_FOR\_QUERIES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#use_stat_tables) and [optimizer\_use\_condition\_selectivity=4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_use_condition_selectivity) ([MDEV-15253](https://jira.mariadb.org/browse/MDEV-15253))
* New variable [gtid\_cleanup\_batch\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_cleanup_batch_size) for determining how many old rows must accumulate in the [mysql.gtid\_slave\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table) table before a background job will be run to delete them.

### Other Features

* Support for window [UDF functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/user-defined-functions) via the new method [x\_remove](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/user-defined-functions/user-defined-functions-calling-sequences#x_remove) ([MDEV-15073](https://jira.mariadb.org/browse/MDEV-15073))
* Json service for plugins ([MDEV-5313](https://jira.mariadb.org/browse/MDEV-5313))
* Much faster privilege checks for MariaDB setups with many user accounts or many database grants ([MDEV-15649](https://jira.mariadb.org/browse/MDEV-15649))
* [mysql.user](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-user-table) table is retired. User accounts and global privileges are now stored in the [mysql.global\_priv](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-global_priv-table) table ([MDEV-17658](https://jira.mariadb.org/browse/MDEV-17658))
* Change in behavior for [FLUSH TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) ([MDEV-5336](https://jira.mariadb.org/browse/MDEV-5336)).

### Bug Fixes

Lots of miscellaneous fixes, including:

* Bug fixes for [MDEV-15562](https://jira.mariadb.org/browse/MDEV-15562) instant [DROP COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#drop-column)

## Changelog

For a complete list of changes made in [MariaDB 10.4.1](mariadb-1041-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1041-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.4.1](mariadb-1041-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-4-1-and-mariadb-connector-node-js-2-0-2-now-available/).

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
