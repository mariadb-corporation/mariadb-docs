# TokuDB Differences

TokuDB has been deprecated by its upstream maintainer. It is disabled from [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105) and has been removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106) - [MDEV-19780](https://jira.mariadb.org/browse/MDEV-19780). We recommend [MyRocks](../myrocks/) as a long-term migration path.

Because we, the MariaDB developers, don't want to add a lot of new features or big code changes to a stable release, not all TokuDB features will be merged at once into MariaDB. Instead they will be added in stages.

On this page we list all the known differences between the TokuDB from [Tokutek](https://www.tokutek.com) and the default MariaDB version from [MariaDB.org](https://downloads.mariadb.org):

## All MariaDB versions

* TokuDB is not the default storage engine.
  * If you want to enable this, you have to start mysqld with: `--default-storage-engine=tokudb`.
* Auto increment for second part of a key behaves as documented (and as it does in MyISAM and other storage engines).
* The DDL syntax is different. While binaries from Tokutek have the patched SQL parser, TokuDB in MariaDB uses the special [Storage Engine API extension](../storage-engines-storage-engine-development/engine-defined-new-tablefieldindex-attributes.md). Thus in Tokutek binaries you write `CLUSTERED KEY (columns)` and, for example, `ROW_FORMAT=TOKUDB_LZMA`. And in MariaDB you write `KEY (columns) CLUSTERING=YES` and `COMPRESSION=TOKUDB_LZMA`.

## Features missing in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

* No online [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table.md).
  * All alter table that changes data or indexes requires a table copy.
* No online [OPTIMIZE TABLE](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md).
* No `INSERT NOAR` or `UPDATE NOAR` commands.
* No gdb stack trace on sigsegv
* IMPORTANT: the compression type does not default to the [tokudb\_row\_format](tokudb-system-variables.md#tokudb_row_format) session variable as it does with Tokutek's builds. If `COMPRESSION=` is not included in `CREATE TABLE` or `ALTER TABLE ENGINE=TokuDB` then the TokuDB table will be uncompressed (before 5.5.37) or zlib-compressed (5.5.37 and later).

## Features missing in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

[MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) (starting from 10.0.5) has online [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table.md). So the features missing will be:

* No `INSERT NOAR` or `UPDATE NOAR` commands.
  * We are working with Tokutek to improve this feature before adding it to MariaDB.
* No online [OPTIMIZE TABLE](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) before [10.0.11](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/storage-engines/tokudb/broken-reference/README.md) ([r4199](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4199))
* No gdb stack trace on sigsegv
* Before 10.0.10 the compression type did not default to the [tokudb\_row\_format](tokudb-system-variables.md#tokudb_row_format) session variable. If `COMPRESSION=` was not included in `CREATE TABLE` or `ALTER TABLE ENGINE=TokuDB` then the TokuDB table was created uncompressed.

## Version of the TokuDB plugin included on MariaDB

This is found on the [TokuDB](./) page.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
