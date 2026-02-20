# MariaDB 5.3 Changes & Improvements

[MariaDB 5.3](changes-improvements-in-mariadb-5-3.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

[Download MariaDB 5.3](https://downloads.mariadb.org/mariadb/5.3)

| Date         | Release                     | Status            | Release Notes              | Changelog                                                                            |
| ------------ | --------------------------- | ----------------- | -------------------------- | ------------------------------------------------------------------------------------ |
| 30 Jan 2013  | [MariaDB 5.3.12](5.3.12.md) | Stable (GA)       | [Release Notes](5.3.12.md) | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-5312-changelog.md) |
| 29 Nov 2012  | [MariaDB 5.3.11](5.3.11.md) | Stable (GA)       | [Release Notes](5.3.11.md) | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-5311-changelog.md) |
| 13 Nov 2012  | [MariaDB 5.3.10](5.3.10.md) | Stable (GA)       | [Release Notes](5.3.10.md) | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-5310-changelog.md) |
| 02 Oct 2012  | [MariaDB 5.3.9](5.3.9.md)   | Stable (GA)       | [Release Notes](5.3.9.md)  | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-539-changelog.md)  |
| 28 Aug 2012  | [MariaDB 5.3.8](5.3.8.md)   | Stable (GA)       | [Release Notes](5.3.8.md)  | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-538-changelog.md)  |
| 4 May 2012   | [MariaDB 5.3.7](5.3.7.md)   | Stable (GA)       | [Release Notes](5.3.7.md)  | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-537-changelog.md)  |
| 9 Apr 2012   | [MariaDB 5.3.6](5.3.6.md)   | Stable (GA)       | [Release Notes](5.3.6.md)  | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-536-changelog.md)  |
| 29 Feb 2012  | [MariaDB 5.3.5](5.3.5.md)   | Stable (GA)       | [Release Notes](5.3.5.md)  | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-535-changelog.md)  |
| 15 Feb 2012  | [MariaDB 5.3.4](5.3.4.md)   | Release Candidate | [Release Notes](5.3.4.md)  | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-534-changelog.md)  |
| 21 Dec 2011  | [MariaDB 5.3.3](5.3.3.md)   | Release Candidate | [Release Notes](5.3.3.md)  | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-533-changelog.md)  |
| 14 Oct 2011  | [MariaDB 5.3.2](5.3.2.md)   | Beta              | [Release Notes](5.3.2.md)  | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-532-changelog.md)  |
| 10 Sep 2011  | [MariaDB 5.3.1](5.3.1.md)   | Beta              | [Release Notes](5.3.1.md)  | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-531-changelog.md)  |
| 26 July 2011 | [MariaDB 5.3.0](5.3.0.md)   | Beta              | [Release Notes](5.3.0.md)  | [Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-530-changelog.md)  |

The focus for [MariaDB 5.3](changes-improvements-in-mariadb-5-3.md) is to radically improve performance for\
subqueries, as well as for joins and single-table queries over large\
data sets.

[MariaDB 5.3](changes-improvements-in-mariadb-5-3.md) is based on [MariaDB 5.2](../5.2/changes-improvements-in-mariadb-5-2.md) and thus on [MariaDB 5.1](../5.1/changes-improvements-in-mariadb-5-1.md) and MySQL 5.1. It is no longer being supported.

Some of the code was backported from MySQL 6.0 (a MySQL version that was never\
released as GA by Oracle), some was re-engineered and enriched by new features,\
and some code was written from scratch.

Any new feature or combination of features can be switched on/off dynamically via the [optimizer\_switch](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizer-switch) system variable.

The first stable (GA) release of [MariaDB 5.3](changes-improvements-in-mariadb-5-3.md) was [MariaDB 5.3.5](5.3.5.md), which was released on 29 Feb 2012.

You can download [the latest binaries of MariaDB 5.3 here](https://downloads.askmonty.org/MariaDB/5.3/),\
or get the latest [source code from launchpad](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code).

## Feature Comparison Matrix

We have created an [Optimizer Feature Comparison Matrix](../../about/compatibility-and-differences/optimizer-feature-comparison-matrix.md) showing the new optimizer features in [MariaDB 5.5](../5.5/changes-improvements-in-mariadb-5-5.md) and 5.3 compared to MySQL 5.5 and 5.6.

## Query optimizer

### Subquery optimizations

Subqueries are finally usable in practice. It is no longer necessary to\
rewrite subqueries manually into joins or into separate queries. [MariaDB 5.3](changes-improvements-in-mariadb-5-3.md)\
aims to provide reasonably efficient handling for all kinds of subqueries.\
All problems with `EXPLAIN` taking a long time have also been resolved.

* [Semi-join subquery optimizations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/semi-join-subquery-optimizations)\
  These transform subqueries into 'semi-joins', entities similar to inner joins,\
  and then use join optimizer to pick the best semi-join execution strategy. Overall\
  the process is similar to how joins are processed in MySQL,MariaDB and other database systems.
  * [Table pullout optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/table-pullout-optimization)
  * [FirstMatch execution strategy](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimization-strategies/firstmatch-strategy)
  * [Semi-join Materialization execution strategy](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimization-strategies/semi-join-materialization-strategy)
  * [LooseScan execution strategy](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimization-strategies/loosescan-strategy)
  * [DuplicateWeedout execution strategy](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimization-strategies/duplicateweedout-strategy)
* [Non-semi-join optimizations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations)\
  If a subquery is not a semi-join, [MariaDB 5.3](changes-improvements-in-mariadb-5-3.md) will make a cost-based choice between these two strategies:
  * Materialization for non-correlated subqueries, with [efficient NULL-aware execution](https://askmonty.org/worklog/Server-Sprint/?tid=68)
  * IN-to-EXISTS transformation (the only optimization inherited from [MariaDB 5.2](../5.2/changes-improvements-in-mariadb-5-2.md) and MySQL 5.1/5.5)
* [Subquery Cache](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/subquery-cache)\
  The subquery cache makes sure that subqueries are re-executed as few times as possible,\
  improving performance of already optimized subqueries.
* Subqueries are never executed during `EXPLAIN`, thus resulting in almost\
  instant `EXPLAIN`.
* DISTINCT and GROUP BY without HAVING are [optimized away](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/optimizing-group-by) from subqueries.

The [Subquery Optimizations Map](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/subquery-optimizations-map) shows new subqueries optimizations graphically.

### Optimizations for derived tables and views

* No early materialization of derived tables (e.g. subqueries in a `FROM`\
  clause) and materialized views (`EXPLAIN` is always instantaneous)
* Thanks to [Derived Table Merge optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizations-for-derived-tables/derived-table-merge-optimization), mergeable derived tables are now processed like mergeable VIEWs.
* [Derived Table with Keys](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizations-for-derived-tables/derived-table-with-key-optimization) optimization gives the optimizer an option to create indexes over materialized derived tables
* Fields of merge-able views and derived tables are involved now in all\
  optimizations employing equalities

### Disk access optimization

* [Index Condition Pushdown](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/index-condition-pushdown)
* [Multi-Range-Read optimization (MRR)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/mariadb-internal-optimizations/multi-range-read-optimization)
  * Key-ordered retrieval

### Join optimizations

* [Block-based Join Algorithms](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms)
* Block Nested Loop algorithm can be used for outer joins
* Block Hash Join (classic algorithm) is implemented and can be used for any\
  equi-joins
* Block Index Join (Batch Key Access Join) is supported and can exploit the\
  benefits of ordered retrievals for primary and secondary keys provided by the\
  new implementation of [MRR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/mariadb-internal-optimizations/multi-range-read-optimization)
* All block based algorithms for joins can use the benefits of new incremental\
  join buffers
* All block based algorithms fully support outer joins including nested outer\
  joins
* All block based algorithms can use the benefits of the first match\
  optimization for semi-joins and the non-exist optimization for outer joins
* All block based algorithms for joins can exploit the benefits of index\
  condition push-down.
* The total memory space used by the query for join buffers can be limited now,\
  and block based algorithms can allocate join buffers up to their needs (not\
  exceeding the set limits).
* Condition over outer tables extracted from ON expressions of outer joins are\
  evaluated before inner tables are accessed (supported for both regular index\
  join and block index join)
* Early checks for nulls for the fields from any null-rejecting conditions are\
  performed

### Index Merge improvements

* Correct optimization of index\_merge vs range access: [Fair choice between range and index\_merge optimizations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/mariadb-internal-optimizations/fair-choice-between-range-and-index_merge-optimizations)
* [index\_merge/sort\_intersection](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/index_merge-sort_intersection) strategy

### Optimizer control

* [@@optimizer\_switch variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizer-switch) can be used to turn on/off all new optimizations.

## NoSQL-style interfaces

* [HandlerSocket](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/nosql/handlersocket) plugin included.
* Faster [HANDLER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/nosql/handler/handler-commands) commands; [HANDLER READ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/nosql/handler/handler-commands) now also work with prepared statements.
* [Dynamic Columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/nosql/dynamic-columns) support.

## Replication and binary logging

* [Group commit for the binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log) —[MariaDB 5.3](changes-improvements-in-mariadb-5-3.md) implements group commit which works when using XtraDB with the\
  binary log enabled. (In previous MariaDB releases, and all MySQL releases at\
  the time of writing, group commit works in InnoDB/XtraDB when the binary log\
  is disabled, but stops working when the binary log is enabled).
* [Annotation of row-based replication events with the original SQL statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog/annotate_rows_log_event) —\
  When using row-based replication, the binary log does not contain SQL\
  statements, only discrete single-row insert/update/delete events. This\
  can make it harder to read mysqlbinlog output and understand where in an\
  application a given event may have originated, complicating analysis and\
  debugging.This feature adds an option to include the original SQL statement as a\
  comment in the binary log (and shown in mysqlbinlog output) for row-based\
  replication events.
* [Checksums for binlog events](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/binlog-event-checksums). This is a backport of\
  the same feature in MySQL 5.6. It was implemented in [MWL#180](https://askmonty.org/worklog/?tid=180).
* [Enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/enhancements-for-start-transaction-with-consistent-snapshot) —\
  In [MariaDB 5.3](changes-improvements-in-mariadb-5-3.md), `START TRANSACTION WITH CONSISTENT SNAPSHOT` now also works\
  with the binary log. This means it is possible to obtain the binlog position\
  corresponding to a transactional snapshot of the database without blocking\
  any other queries. This is used by the command\
  "`mysqldump` `--single-transaction` `--master-data`" to do a fully\
  non-blocking backup which can be used to provision a new slave.\
  "`START` `TRANSACTION` `WITH` `CONSISTENT` `SNAPSHOT`" now also\
  works consistently between transactions involving more than one storage\
  engine (currently XTraDB and PBXT support this).
* [Row-based replication for tables with no primary key](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/row-based-replication-with-no-primary-key) —\
  This feature can improve the performance of row-based replication on tables\
  that do not have a primary key (or other unique key), but which do have\
  another index that can help locate rows to update or delete. With this\
  feature, index cardinality information from `ANALYZE TABLE` is considered\
  when selecting the index to use (before this feature is implemented, the\
  first index was selected unconditionally).
* `mysqlbinlog` will now omit redundant `use` statements\
  around `BEGIN`, `SAVEPOINT`, `COMMIT`, and `ROLLBACK` events when\
  reading MySQL 5.0 binlogs.

## Datatypes

* [Microsecond](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/microseconds-in-mariadb) support for [NOW()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/now) and [timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/timestamp), [time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/time), and [datetime](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/datetime) columns.
* [CAST()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/cast) now supports AS DECIMAL\[(M,D)] and AS INT.
* [CAST()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/cast) and all other datetime/time functions now supports microsecond fully.

## Windows performance improvements

* Backported [Windows performance patches](https://www.facebook.com/note.php?note_id=238505812835782) from MySQL 5.5.
* Asynchronous IO in XtraDB\
  is [redesigned](https://www.facebook.com/note.php?note_id=238687382817625)\
  and is now faster, due to the use of IO completion ports.
* Additional durability option for XtraDB : `innodb_flush_method` can now\
  be `O_DSYNC`, like on Unixes. The effect of using this option is that the\
  log file is opened with `FILE_FLAG_WRITETHROUGH`,\
  and `FlushFileBuffers()` is not done. This may improve speed in write-heavy\
  scenarios.
* A new Windows [MSI installer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows).
* Includes a GUI-tool, [HeidiSQL](https://www.heidisql.com/).

## Miscellaneous

* [GIS precise operations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry/gis-features-in-533)
* New status variables: `Rows_tmp_read`, `Handler_tmp_write`,\
  and `Handler_tmp_update` which count what happens with internal temporary\
  tables. `Rows_read`, `Handler_write` and `Handler_update` no longer\
  count operations on internal temporary tables.
* New status variable `Handler_read_rnd_deleted`, which is number of deleted rows found and skipped while scanning a table. Before this was part of `Handler_read_rnd_next`.
* New variable 'in\_transaction' that is 1 if you are in a transaction, 0 otherwise.
* [Progress reports](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting) for `ALTER TABLE`\
  and `LOAD DATA INFILE`. In addition Aria tables gives progress reports\
  for `REPAIR TABLE` and `CHECK TABLE`. The progress can be seen\
  in `SHOW PROCESSLIST`, `INFORMATION_SCHEMA.PROCESSLIST` and is sent to\
  MariaDB clients that calls `mysql_real_connect()` with the\
  new `CLIENT_PROGRESS` flag. `mysql` command line client supports the new\
  progress indications.
* [PBXT consistent commit ordering](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/enhancements-for-start-transaction-with-consistent-snapshot) —\
  This feature implements the new commit ordering storage engine API in PBXT.\
  With this feature, it is possible to use\
  "`START TRANSACTION WITH CONSISTENT SNAPSHOT`" and get consistency among\
  transactions which involve both XtraDB and InnoDB. (Without this feature,\
  there is no such consistency guarantee. For example, even after running\
  "`START TRANSACTION WITH CONSISTENT SNAPSHOT`" it was still possible for\
  the InnoDB/XtraDB part of some transaction T to be visible and the PBXT\
  part of the same transaction T to not be visible.)
* MariaDB unique error numbers now start from `1900` to not clash with MySQL\
  error numbers.
* \`/\*M!

**\*/\` new** [**executed comment syntax**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/comment-syntax) **that can be**

used when you want use new MariaDB syntax but still want your program to be\
compatible with MySQL.

* A MariaDB optimized version of [mytop](https://www.mysqlfanboy.com/mytop) is included in the MariaDB distribution.
* Enhanced [KILL syntax](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill):

```sql
KILL [HARD | SOFT] [CONNECTION | QUERY] [thread_id | USER user_name]
```

* `max_user_connections` (both the global variable and\
  the `GRANT` option) can be set to `-1` to stop users from connecting to\
  the server. The global `max_user_connections` variable does\
  not affect users with the `SUPER` privilege.
* The [IGNORE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/ignore) directive does not ignore all errors (like fatal errors), only things that are safe to ignore.

You can access the [MariaDB 5.3](changes-improvements-in-mariadb-5-3.md) tree from [launchpad](https://launchpad.net/maria/5.3).

## Security Vulnerabilities Fixed in [MariaDB 5.3](changes-improvements-in-mariadb-5-3.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/cve)\
page.

* [CVE-2013-1531](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-1531): [MariaDB 5.3.12](5.3.12.md)[CVE-2013-0389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0389): [MariaDB 5.3.12](5.3.12.md)[CVE-2013-0385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0385): [MariaDB 5.3.12](5.3.12.md)[CVE-2013-0384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0384): [MariaDB 5.3.12](5.3.12.md)[CVE-2013-0383](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0383): [MariaDB 5.3.12](5.3.12.md)[CVE-2013-0375](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0375): [MariaDB 5.3.12](5.3.12.md)[CVE-2012-5627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5627): [MariaDB 5.3.12](5.3.12.md) \[[2](../../changelogs/changelogs-mariadb-53-series/mariadb-5312-changelog.md)][CVE-2012-5615](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5615): [MariaDB 5.3.12](5.3.12.md) \[[2](../../changelogs/changelogs-mariadb-53-series/mariadb-5312-changelog.md)][CVE-2012-5612](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5612): [MariaDB 5.3.12](5.3.12.md)[CVE-2012-5611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5611): [MariaDB 5.3.12](5.3.12.md), [MariaDB 5.3.11](5.3.11.md)[CVE-2012-4414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-4414): [MariaDB 5.3.8](5.3.8.md) \[[2](../../changelogs/changelogs-mariadb-53-series/mariadb-538-changelog.md)][CVE-2012-1705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1705): [MariaDB 5.3.12](5.3.12.md)[CVE-2012-1702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1702): [MariaDB 5.3.12](5.3.12.md)[CVE-2012-0574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0574): [MariaDB 5.3.12](5.3.12.md)[CVE-2012-0572](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0572): [MariaDB 5.3.12](5.3.12.md)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
