# TokuDB Differences

{% include "../../../../.gitbook/includes/tokudb-has-been-deprecated-....md" %}

Because we, the MariaDB developers, don't want to add a lot of new features or big code changes to a stable release, not all TokuDB features are merged at once into MariaDB. Instead they are added in stages.

On this page we list all the known differences between the TokuDB from [Tokutek](https://www.tokutek.com) and the default MariaDB version from [MariaDB.org](https://downloads.mariadb.org):

## All MariaDB versions

* TokuDB is not the default storage engine.
  * If you want to enable this, you have to start mysqld with: `--default-storage-engine=tokudb`.
* Auto increment for second part of a key behaves as documented (and as it does in MyISAM and other storage engines).
* The DDL syntax is different. While binaries from Tokutek have the patched SQL parser, TokuDB in MariaDB uses the special [Storage Engine API extension](../../storage-engines-storage-engine-development/engine-defined-new-tablefieldindex-attributes.md). Thus in Tokutek binaries you write `CLUSTERED KEY (columns)` and, for example, `ROW_FORMAT=TOKUDB_LZMA`. And in MariaDB you write `KEY (columns) CLUSTERING=YES` and `COMPRESSION=TOKUDB_LZMA`.

## Features missing in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

* No online [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/).
  * All alter table that changes data or indexes requires a table copy.
* No online [OPTIMIZE TABLE](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md).
* No `INSERT NOAR` or `UPDATE NOAR` commands.
* No gdb stack trace on sigsegv
* IMPORTANT: the compression type does not default to the [tokudb\_row\_format](tokudb-system-variables.md#tokudb_row_format) session variable as it does with Tokutek's builds. If `COMPRESSION=` is not included in `CREATE TABLE` or `ALTER TABLE ENGINE=TokuDB` then the TokuDB table are uncompressed (before 5.5.37) or zlib-compressed (5.5.37 and later).

## Features missing in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

[MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) (starting from 10.0.5) has online [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/). So the features missing are:

* No `INSERT NOAR` or `UPDATE NOAR` commands.
  * We are working with Tokutek to improve this feature before adding it to MariaDB.
* No online [OPTIMIZE TABLE](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) before [10.0.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes) (r4199)
* No gdb stack trace on sigsegv
* Before 10.0.10 the compression type did not default to the [tokudb\_row\_format](tokudb-system-variables.md#tokudb_row_format) session variable. If `COMPRESSION=` was not included in `CREATE TABLE` or `ALTER TABLE ENGINE=TokuDB` then the TokuDB table was created uncompressed.

## Version of the TokuDB plugin included on MariaDB

This is found on the [TokuDB](./) page.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
