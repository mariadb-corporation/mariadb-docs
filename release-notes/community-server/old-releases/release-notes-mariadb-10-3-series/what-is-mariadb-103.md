# MariaDB 10.3 Changes & Improvements

[MariaDB 10.3](what-is-mariadb-103.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

The most recent release of [MariaDB 10.3](what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](mariadb-10-3-39-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[MariaDB 10.3](what-is-mariadb-103.md) is a previous major stable version. The first stable release was in May 2018, and it was [maintained until](https://mariadb.org/about/#maintenance-policy) May 2023.

For details on upgrading from [MariaDB 10.2](../release-notes-mariadb-10-2-series/what-is-mariadb-102.md), see [Upgrading from MariaDB 10.2 to 10.3](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-102-to-mariadb-103).

MariaDB Server 10.3 is included in MariaDB TX 3.0. [Watch the webinar recording](https://go.mariadb.com/mariadbtx3.0_webinar_registration-LP.html?utm_source=kb\&utm_campaign=mariadbtx-ondemand-webinar-kb-changes-improvements) to learn more about the new features included in this release.

The following lists the major new features in [MariaDB 10.3](what-is-mariadb-103.md):

## Implemented Features

### [Sequences](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences)

* [Sequences Overview](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-overview) ([MDEV-10139](https://jira.mariadb.org/browse/MDEV-10139))
* [CREATE SEQUENCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/create-sequence)
* [SHOW CREATE SEQUENCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-sequence)
* [ALTER SEQUENCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/alter-sequence)
* [DROP SEQUENCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/drop-sequence)
* [NEXT VALUE FOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-functions/next-value-for-sequence_name)
* [PREVIOUS VALUE FOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-functions/previous-value-for-sequence_name)
* [SETVAL()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-functions/setval)

### Syntax / General Features

* [System-versioned tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) (also known as AS OF) ([MDEV-12894](https://jira.mariadb.org/browse/MDEV-12894))
* [Table Value Constructors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/table-value-constructors) ([MDEV-12172](https://jira.mariadb.org/browse/MDEV-12172)) — GSoC 2017 project by Galina Shalygina
* [Transform \[NOT\] IN predicate with long list of values INTO \[NOT\] IN subquery](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries) ([MDEV-12176](https://jira.mariadb.org/browse/MDEV-12176)) — GSoC 2017 project by Galina Shalygina
* [ROW TYPE OF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/declare-variable#type-of-row-type-of) now supports local SP variables ([MDEV-14139](https://jira.mariadb.org/browse/MDEV-14139))
* [Aggregate stored functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-functions/stored-aggregate-functions) ([MDEV-7773](https://jira.mariadb.org/browse/MDEV-7773)) — GSoC 2016 project by Varun Gupta
* Support for [LIMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/limit) clause in [GROUP\_CONCAT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/group_concat) ([MDEV-11297](https://jira.mariadb.org/browse/MDEV-11297))
* [PERCENTILE\_CONT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/percentile_cont), [PERCENTILE\_DISC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/percentile_disc), and [MEDIAN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/median) [window functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions) ([MDEV-12985](https://jira.mariadb.org/browse/MDEV-12985))
* [FOR ... END FOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/for) statement ([MDEV-14415](https://jira.mariadb.org/browse/MDEV-14415))
* [XA RECOVER FORMAT='SQL'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/xa-transactions) ([MDEV-14593](https://jira.mariadb.org/browse/MDEV-14593))
* Oracle compatible [SUBSTR()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/substring) function ([MDEV-14012](https://jira.mariadb.org/browse/MDEV-14012)) — contribution by Jérôme Brauge
* [INVISIBLE columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/invisible-columns) ([MDEV-10177](https://jira.mariadb.org/browse/MDEV-10177)) — GSoC 2016 project by Sachin Setiya
* Various scalability improvements ([MDEV-14529](https://jira.mariadb.org/browse/MDEV-14529), [MDEV-14505](https://jira.mariadb.org/browse/MDEV-14505))
* [Semi-sync plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/semisynchronous-replication) merged into the server ([MDEV-13073](https://jira.mariadb.org/browse/MDEV-13073)) — contribution by Alibaba
* [INTERSECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/intersect) and [EXCEPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/except). These are both now [reserved words](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/reserved-words) and can no longer be used as an [identifier](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/identifier-names) without being quoted ([MDEV-10141](https://jira.mariadb.org/browse/MDEV-10141))
* [ROW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/row) data type for [stored routine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-procedures) variables ([MDEV-10914](https://jira.mariadb.org/browse/MDEV-10914), [MDEV-12007](https://jira.mariadb.org/browse/MDEV-12007), [MDEV-12291](https://jira.mariadb.org/browse/MDEV-12291))
* [TYPE OF and ROW TYPE OF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/declare-variable#type-of-row-type-of) anchored data types for [stored routine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-procedures) variables ([MDEV-12461](https://jira.mariadb.org/browse/MDEV-12461))
* [Cursors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors/cursor-overview) with parameters ([MDEV-12457](https://jira.mariadb.org/browse/MDEV-12457))
* [DDL Fast Fail - WAIT/NOWAIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/wait-and-nowait) ([MDEV-11379](https://jira.mariadb.org/browse/MDEV-11379), [MDEV-11388](https://jira.mariadb.org/browse/MDEV-11388))
* [CHR()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/chr) function ([MDEV-12685](https://jira.mariadb.org/browse/MDEV-12685))
* [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) statement can delete from the table that is used in a subquery in the `WHERE` clause ([MDEV-12137](https://jira.mariadb.org/browse/MDEV-12137))
* Stored routine parameters can use [ROW TYPE OF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/declare-variable#type-of-row-type-of) ([MDEV-13581](https://jira.mariadb.org/browse/MDEV-13581))
* The server now [supports the PROXY protocol](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/server-client-software/client-libraries/proxy-protocol-support) - see also the new [proxy\_protocol\_networks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#proxy_protocol_networks) system variable ([MDEV-11159](https://jira.mariadb.org/browse/MDEV-11159))
* [Instant ADD COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-online-ddl/instant-add-column-for-innodb) ([MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369)) — Tencent Game DBA Team, developed by vinchen.
* [UPDATE statements with the same source and target](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update#update-statements-with-the-same-source-and-target) ([MDEV-12874](https://jira.mariadb.org/browse/MDEV-12874)) — from Jerome Brauge.
* [ORDER BY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/order-by) and [LIMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/limit) in multi-table update ([MDEV-13911](https://jira.mariadb.org/browse/MDEV-13911))
* [DATE\_FORMAT(date, format, locale)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/date_format) - 3 argument form of DATE\_FORMAT ([MDEV-11553](https://jira.mariadb.org/browse/MDEV-11553))
* The MariaDB SQL/PL stored procedure dialect (enabled with [sql\_mode=ORACLE](https://mariadb.com/docs/release-notes/compatibility-and-differences/sql_modeoracle)) now supports Oracle style packages. Support for the following statements has been added ([MDEV-10591](https://jira.mariadb.org/browse/MDEV-10591)):
  * [CREATE PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-package)
  * [CREATE PACKAGE BODY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-package-body)
  * [DROP PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-package)
  * [DROP PACKAGE BODY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-package-body)
  * [SHOW CREATE PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-package)
  * [SHOW CREATE PACKAGE BODY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-package-body)
* New [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) `SIMULTANEOUS_ASSIGNMENT` to make the SET part of the [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) statement evaluate all assignments simultaneously, not left-to-right.
* Correctness improvement - TRUNCATE honors transactional locks ([MDEV-15061](https://jira.mariadb.org/browse/MDEV-15061))
* Windows binaries now use high-precision timer when available ([MDEV-15694](https://jira.mariadb.org/browse/MDEV-15694)). This makes much less probable for two queries to have the same `CURRENT_TIMESTAMP(6)` value, for example.
* Two new [ALTER TABLE ... ALGORITHM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#algorithm) options, INSTANT and NOCOPY, which allow operations that would require any data files to be modified, or that would require rebuilding the clustered index respectively, to be refused rather than potentially perform slowly ([MDEV-13134](https://jira.mariadb.org/browse/MDEV-13134))
* [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) `--ignore-database` option ([MDEV-13336](https://jira.mariadb.org/browse/MDEV-13336))

### Compatibility

* As a result of implementing Table Value Constructors, the [VALUES function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/values-value) has been renamed to VALUE() ([MDEV-12172](https://jira.mariadb.org/browse/MDEV-12172))
* When running with [sql\_mode=ORACLE](../../about/compatibility-and-differences/sql_modeoracle.md), the server now understands a subset of Oracle's PL/SQL language instead of the traditional MariaDB syntax for stored routines. See [MDEV-10142](https://jira.mariadb.org/browse/MDEV-10142), [MDEV-10764](https://jira.mariadb.org/browse/MDEV-10764) and [SQL\_MODE=ORACLE From MariaDB 10.3](https://mariadb.com/docs/release-notes/compatibility-and-differences/sql_modeoracle) to know the current status.
* New [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode), EMPTY\_STRING\_IS\_NULL.
* [INTERSECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/intersect) and [EXCEPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/except) are both now [reserved words](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/reserved-words) and can no longer be used as an [identifier](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/identifier-names) without being quoted ([MDEV-10141](https://jira.mariadb.org/browse/MDEV-10141))
* Functions that used to only return 64-bit now can return 32-bit results ([MDEV-12619](https://jira.mariadb.org/browse/MDEV-12619)).

### Compression

* [Storage-engine Independent Column Compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression) ([MDEV-11371](https://jira.mariadb.org/browse/MDEV-11371)) — Tencent Game DBA Team, developed by willhan, also thanks to AliSQL.
* On Linux, shrink the core dumps by omitting the InnoDB buffer pool ([MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814))

### Encryption

* Temporary files created by merge sort and row log are encrypted if [innodb\_encrypt\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) is set to `1`, regardless of whether the table encrypted or not ([MDEV-12634](https://jira.mariadb.org/browse/MDEV-12634)).

### Optimizer/Performance

* Condition pushdown through `PARTITION BY` clause of [window functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions) ([MDEV-10855](https://jira.mariadb.org/browse/MDEV-10855))
* New [Lateral Derived optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizations-for-derived-tables/lateral-derived-optimization) was introduced.
* Numerous performance improvements for high-concurrency load
* Numerous scalability and performance improvements to global data structures, including [MDEV-14756](https://jira.mariadb.org/browse/MDEV-14756), [MDEV-15019](https://jira.mariadb.org/browse/MDEV-15019), [MDEV-14482](https://jira.mariadb.org/browse/MDEV-14482), [MDEV-15059](https://jira.mariadb.org/browse/MDEV-15059), [MDEV-15104](https://jira.mariadb.org/browse/MDEV-15104)
* Performance improvements to persistent data structures: [MDEV-15090](https://jira.mariadb.org/browse/MDEV-15090), [MDEV-15132](https://jira.mariadb.org/browse/MDEV-15132)

### Storage Engines

#### InnoDB

* [innodb\_fast\_shutdown](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) now has a new mode, `3`, which skips the rollback of connected transactions ([MDEV-15832](https://jira.mariadb.org/browse/MDEV-15832))

#### Spider

The [Spider storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) has been updated to 3.3.13. The partitioning storage engine has been updated to support all the new Spider features including:

* Direct join support. This allows Spider to do JOINS and GROUP BYs internally.
* Direct update and delete.
* Direct aggregates.
* [slave\_transaction\_retry\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) and [slave-transaction-retry-interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) allow more control over handling delays or conflicts when applying binary logs.

Most of the features were done as part of [MDEV-7698](https://jira.mariadb.org/browse/MDEV-7698).

#### OQGRAPH

* [OQGraph](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/oqgraph-storage-engine) now supports the "leaves" algorithm ([MDEV-11271](https://jira.mariadb.org/browse/MDEV-11271)) — contribution by Heinz Wiesinger

#### Partition Engine

* Numerous improvements for the partition engine ([MDEV-7698](https://jira.mariadb.org/browse/MDEV-7698)) — contribution by Kentoku Shiba
  * Full text support.
  * Multi-range-read (Gives better performance when handling multiple ranges).
  * Support for condition pushdown.
  * HANDLER support
* Aggregate pushdown
* Bulk update/delete

### Information Schema

* The Information Schema is optimized to use much less memory when selecting from [INFORMATION\_SCHEMA.TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-tables-table) or any other table with many [VARCHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/varchar) or [TEXT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/text) columns ([MDEV-14275](https://jira.mariadb.org/browse/MDEV-14275))
* The [Information Schema Columns table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-columns-table) now displays [system versioning](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) info in the EXTRA column - [MDEV-15062](https://jira.mariadb.org/browse/MDEV-15062)

### Logging

* Disable logging of certain statements to the [general log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/general-query-log) or the [slow query log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/slow-query-log) with the [log\_disabled\_statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_disabled_statements) and [log\_slow\_disabled\_statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_slow_disabled_statements) system variables.
* A new option to [log\_slow\_filter](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_slow_filter), `filsort_priority_queue`.

### Replication

* Per-engine mysql.gtid\_slave\_pos tables ([MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179)) — Implemented by Kristian Nielsen funded by Booking.com.

### Data Type API

10.3 continues refactoring for the data type API started in 10.2, which will make it possible to have user data type plugins. This work is still in progress (see [MDEV-4912](https://jira.mariadb.org/browse/MDEV-4912) for the current status and subtasks). Most of the task in this category do not change the server behavior. Some tasks do have a [visible effect](mariadb-1030-release-notes.md#data-type-api).

### Idle Transactions

Connections with idle transactions can be automatically killed after a specified time period by means of the [idle\_transaction\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#idle_transaction_timeout), [idle\_readonly\_transaction\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#idle_readonly_transaction_timeout) and [idle\_write\_transaction\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#idle_write_transaction_timeout) system variables.

### System Variables

For a list of all new variables, see [System Variables Added in MariaDB 10.3](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-10-3) and [Status Variables Added in MariaDB 10.3](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/status-variables-added-in-mariadb-103).

* New system variable [gtid\_pos\_auto\_engines](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_pos_auto_engines).
* New system variable [secure\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#secure_timestamp) for restricting the direct setting of a session timestamp ([MDEV-15923](https://jira.mariadb.org/browse/MDEV-15923))
* [session variables tracking](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#session_track_system_variables) is enabled by default ([MDEV-11825](https://jira.mariadb.org/browse/MDEV-11825))
* Remove deprecated variables [innodb\_file\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables), [innodb\_file\_format\_check](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables), [innodb\_file\_format\_max](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) and [innodb\_large\_prefix](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables).
* [version\_source\_revision](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#version_source_revision) - permits seeing which version of the source was used for the build ([MDEV-12583](https://jira.mariadb.org/browse/MDEV-12583)).
* Added [bind\_address](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#bind_address) as a system variable ([MDEV-12542](https://jira.mariadb.org/browse/MDEV-12542)).
* The max value of the [max\_prepared\_stmt\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_prepared_stmt_count) system variable has been increased from 1048576 to 4294967295
* The [proxy\_protocol\_networks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#proxy_protocol_networks) variable can now be modified without restarting the server ([MDEV-15501](https://jira.mariadb.org/browse/MDEV-15501))

## Security Vulnerabilities Fixed in [MariaDB 10.3](what-is-mariadb-103.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2023-5157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5157): [MariaDB 10.3.36](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10336-release-notes)
* [CVE-2022-47015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47015): [MariaDB 10.3.39](mariadb-10-3-39-release-notes.md)
* [CVE-2022-38791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38791): [MariaDB 10.3.36](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10336-release-notes)
* [CVE-2022-32091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32091): [MariaDB 10.3.36](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10336-release-notes)
* [CVE-2022-32088](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32088): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-32087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32087): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-32085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32085): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-32084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32084): [MariaDB 10.3.36](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10336-release-notes)
* [CVE-2022-32083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32083): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-31624](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31624): [MariaDB 10.3.32](mariadb-10332-release-notes.md)
* [CVE-2022-27458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27458): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27456): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27452](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27452): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27449): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27448](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27448): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27447](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27447): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27445](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27445): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27387): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27386): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27385): [MariaDB 10.3.32](mariadb-10332-release-notes.md)
* [CVE-2022-27384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27384): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27383](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27383): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27381](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27381): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27380): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27379): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27378): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27377](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27377): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-27376](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27376): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-24052](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24052): [MariaDB 10.3.33](mariadb-10333-release-notes.md)
* [CVE-2022-24051](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24051): [MariaDB 10.3.33](mariadb-10333-release-notes.md)
* [CVE-2022-24050](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24050): [MariaDB 10.3.33](mariadb-10333-release-notes.md)
* [CVE-2022-24048](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24048): [MariaDB 10.3.33](mariadb-10333-release-notes.md)
* [CVE-2022-21595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21595): [MariaDB 10.3.33](mariadb-10333-release-notes.md)
* [CVE-2022-21451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21451): [MariaDB 10.3.29](mariadb-10329-release-notes.md)
* [CVE-2022-21427](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21427): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778): [MariaDB 10.3.33](mariadb-10333-release-notes.md)
* [CVE-2021-46669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46669): [MariaDB 10.3.35](mariadb-10335-release-notes.md)
* [CVE-2021-46668](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46668): [MariaDB 10.3.34](mariadb-10334-release-notes.md)
* [CVE-2021-46667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46667): [MariaDB 10.3.32](mariadb-10332-release-notes.md)
* [CVE-2021-46666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46666): [MariaDB 10.3.30](mariadb-10330-release-notes.md)
* [CVE-2021-46665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46665): [MariaDB 10.3.34](mariadb-10334-release-notes.md)
* [CVE-2021-46664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46664): [MariaDB 10.3.34](mariadb-10334-release-notes.md)
* [CVE-2021-46663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46663): [MariaDB 10.3.34](mariadb-10334-release-notes.md)
* [CVE-2021-46662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46662): [MariaDB 10.3.32](mariadb-10332-release-notes.md)
* [CVE-2021-46661](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46661): [MariaDB 10.3.34](mariadb-10334-release-notes.md)
* [CVE-2021-46659](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46659): [MariaDB 10.3.33](mariadb-10333-release-notes.md)
* [CVE-2021-46658](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46658): [MariaDB 10.3.31](mariadb-10331-release-notes.md)
* [CVE-2021-46657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46657): [MariaDB 10.3.30](mariadb-10330-release-notes.md)
* [CVE-2021-35604](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35604): [MariaDB 10.3.32](mariadb-10332-release-notes.md)
* [CVE-2021-27928](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27928): [MariaDB 10.3.28](mariadb-10328-release-notes.md)
* [CVE-2021-2389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2389): [MariaDB 10.3.31](mariadb-10331-release-notes.md)
* [CVE-2021-2372](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2372): [MariaDB 10.3.31](mariadb-10331-release-notes.md)
* [CVE-2021-2194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2194): [MariaDB 10.3.26](mariadb-10326-release-notes.md)
* [CVE-2021-2166](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2166): [MariaDB 10.3.29](mariadb-10329-release-notes.md)
* [CVE-2021-2154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2154): [MariaDB 10.3.29](mariadb-10329-release-notes.md)
* [CVE-2021-2144](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2144): [MariaDB 10.3.19](mariadb-10319-release-notes.md)
* [CVE-2021-2022](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2022): [MariaDB 10.3.24](mariadb-10324-release-notes.md)
* [CVE-2021-2007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2007): [MariaDB 10.3.17](mariadb-10317-release-notes.md)
* [CVE-2020-2922](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2922): [MariaDB 10.3.17](mariadb-10317-release-notes.md)
* [CVE-2020-28912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28912): [MariaDB 10.3.26](mariadb-10326-release-notes.md)
* [CVE-2020-2814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2814): [MariaDB 10.3.23](mariadb-10323-release-notes.md)
* [CVE-2020-2812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2812): [MariaDB 10.3.23](mariadb-10323-release-notes.md)
* [CVE-2020-2780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2780): [MariaDB 10.3.19](mariadb-10319-release-notes.md)
* [CVE-2020-2760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2760): [MariaDB 10.3.23](mariadb-10323-release-notes.md)
* [CVE-2020-2752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2752): [MariaDB 10.3.23](mariadb-10323-release-notes.md)
* [CVE-2020-2574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2574): [MariaDB 10.3.22](mariadb-10322-release-notes.md)
* [CVE-2020-15180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15180): [MariaDB 10.3.25](mariadb-10325-release-notes.md)
* [CVE-2020-14812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14812): [MariaDB 10.3.26](mariadb-10326-release-notes.md)
* [CVE-2020-14789](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14789): [MariaDB 10.3.26](mariadb-10326-release-notes.md)
* [CVE-2020-14776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14776): [MariaDB 10.3.26](mariadb-10326-release-notes.md)
* [CVE-2020-14765](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14765): [MariaDB 10.3.26](mariadb-10326-release-notes.md)
* [CVE-2020-13249](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13249): [MariaDB 10.3.23](mariadb-10323-release-notes.md)
* [CVE-2019-2974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2974): [MariaDB 10.3.19](mariadb-10319-release-notes.md)
* [CVE-2019-2938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2938): [MariaDB 10.3.19](mariadb-10319-release-notes.md)
* [CVE-2019-2805](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2805): [MariaDB 10.3.17](mariadb-10317-release-notes.md)
* [CVE-2019-2758](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2758): [MariaDB 10.3.17](mariadb-10317-release-notes.md)
* [CVE-2019-2740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2740): [MariaDB 10.3.17](mariadb-10317-release-notes.md)
* [CVE-2019-2739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2739): [MariaDB 10.3.17](mariadb-10317-release-notes.md)
* [CVE-2019-2737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2737): [MariaDB 10.3.17](mariadb-10317-release-notes.md)
* [CVE-2019-2628](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2628): [MariaDB 10.3.15](mariadb-10315-release-notes.md)
* [CVE-2019-2627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2627): [MariaDB 10.3.15](mariadb-10315-release-notes.md)
* [CVE-2019-2614](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2614): [MariaDB 10.3.15](mariadb-10315-release-notes.md)
* [CVE-2019-2537](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2537): [MariaDB 10.3.13](mariadb-10313-release-notes.md)
* [CVE-2019-2510](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2510): [MariaDB 10.3.13](mariadb-10313-release-notes.md)
* [CVE-2019-2503](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2503): [MariaDB 10.3.10](mariadb-10310-release-notes.md)
* [CVE-2018-3284](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3284): [MariaDB 10.3.11](mariadb-10311-release-notes.md)
* [CVE-2018-3282](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3282): [MariaDB 10.3.11](mariadb-10311-release-notes.md)
* [CVE-2018-3277](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3277): [MariaDB 10.3.11](mariadb-10311-release-notes.md)
* [CVE-2018-3251](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3251): [MariaDB 10.3.11](mariadb-10311-release-notes.md)
* [CVE-2018-3200](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3200): [MariaDB 10.3.11](mariadb-10311-release-notes.md)
* [CVE-2018-3185](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3185): [MariaDB 10.3.11](mariadb-10311-release-notes.md)
* [CVE-2018-3174](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3174): [MariaDB 10.3.11](mariadb-10311-release-notes.md)
* [CVE-2018-3173](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3173): [MariaDB 10.3.11](mariadb-10311-release-notes.md)
* [CVE-2018-3162](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3162): [MariaDB 10.3.11](mariadb-10311-release-notes.md)
* [CVE-2018-3156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3156): [MariaDB 10.3.11](mariadb-10311-release-notes.md)
* [CVE-2018-3143](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3143): [MariaDB 10.3.11](mariadb-10311-release-notes.md)
* [CVE-2018-3066](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3066): [MariaDB 10.3.9](mariadb-1039-release-notes.md)
* [CVE-2018-3064](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3064): [MariaDB 10.3.9](mariadb-1039-release-notes.md)
* [CVE-2018-3063](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3063): [MariaDB 10.3.9](mariadb-1039-release-notes.md)
* [CVE-2018-3060](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3060): [MariaDB 10.3.9](mariadb-1039-release-notes.md)
* [CVE-2018-3058](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3058): [MariaDB 10.3.9](mariadb-1039-release-notes.md)
* [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032): [MariaDB 10.3.36](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10336-release-notes)
* [CVE-2016-9843](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-9843): [MariaDB 10.3.11](mariadb-10311-release-notes.md)

## Comparison with MySQL

* [System Variable Differences Between MariaDB 10.3 and MySQL 8.0](../../about/compatibility-and-differences/system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-10-3-and-mysql-8-0.md)
* [Function Differences Between MariaDB 10.3 and MySQL 8.0](../../about/compatibility-and-differences/function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-and-mysql-unmaintained-series/function-differences-between-mariadb-10-3-and-mysql-8-0.md)
* [System Variable Differences Between MariaDB 10.3 and MySQL 5.7](../../about/compatibility-and-differences/system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-10-3-and-mysql-5-7.md)
* [Function Differences Between MariaDB 10.3 and MySQL 5.7](../../about/compatibility-and-differences/function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-and-mysql-unmaintained-series/function-differences-between-mariadb-103-and-mysql-57.md)

## List of All [MariaDB 10.3](what-is-mariadb-103.md) Releases

| Date        | Release                                                                                                                                                                       | Status                 | Release Notes                                                                                                                                                             | Changelog                                                                                 |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 10 May 2023 | [MariaDB 10.3.39](mariadb-10-3-39-release-notes.md)                                                                                                                           | Stable (GA)            | [Release Notes](mariadb-10-3-39-release-notes.md)                                                                                                                         | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10-3-39-changelog.md) |
| 6 Feb 2023  | [MariaDB 10.3.38](mariadb-10-3-38-release-notes.md)                                                                                                                           | Stable (GA)            | [Release Notes](mariadb-10-3-38-release-notes.md)                                                                                                                         | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10-3-38-changelog.md) |
| 7 Nov 2022  | [MariaDB 10.3.37](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10-3-37-release-notes) | Stable (GA)            | [Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series)                             | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10-3-37-changelog.md) |
| 15 Aug 2022 | [MariaDB 10.3.36](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10336-release-notes)   | Stable (GA)            | [Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10336-release-notes) | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10336-changelog.md)   |
| 20 May 2022 | [MariaDB 10.3.35](mariadb-10335-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10335-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10335-changelog.md)   |
| 12 Feb 2022 | [MariaDB 10.3.34](mariadb-10334-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10334-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10334-changelog.md)   |
| 9 Feb 2022  | [MariaDB 10.3.33](mariadb-10333-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10333-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10333-changelog.md)   |
| 8 Nov 2021  | [MariaDB 10.3.32](mariadb-10332-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10332-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10332-changelog.md)   |
| 6 Aug 2021  | [MariaDB 10.3.31](mariadb-10331-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10331-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10331-changelog.md)   |
| 23 Jun 2021 | [MariaDB 10.3.30](mariadb-10330-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10330-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10330-changelog.md)   |
| 7 May 2021  | [MariaDB 10.3.29](mariadb-10329-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10329-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10329-changelog.md)   |
| 22 Feb 2021 | [MariaDB 10.3.28](mariadb-10328-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10328-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10328-changelog.md)   |
| 11 Nov 2020 | [MariaDB 10.3.27](mariadb-10327-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10327-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10327-changelog.md)   |
| 3 Nov 2020  | [MariaDB 10.3.26](mariadb-10326-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10326-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10326-changelog.md)   |
| 7 Oct 2020  | [MariaDB 10.3.25](mariadb-10325-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10325-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10325-changelog.md)   |
| 10 Aug 2020 | [MariaDB 10.3.24](mariadb-10324-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10324-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10324-changelog.md)   |
| 12 May 2020 | [MariaDB 10.3.23](mariadb-10323-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10323-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10323-changelog.md)   |
| 28 Jan 2020 | [MariaDB 10.3.22](mariadb-10322-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10322-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10322-changelog.md)   |
| 11 Dec 2019 | [MariaDB 10.3.21](mariadb-10321-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10321-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10321-changelog.md)   |
| 8 Nov 2019  | [MariaDB 10.3.20](mariadb-10320-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10320-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10320-changelog.md)   |
| 5 Nov 2019  | [MariaDB 10.3.19](mariadb-10319-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10319-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10319-changelog.md)   |
| 11 Sep 2019 | [MariaDB 10.3.18](mariadb-10318-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10318-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10318-changelog.md)   |
| 31 Jul 2019 | [MariaDB 10.3.17](mariadb-10317-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10317-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10317-changelog.md)   |
| 17 Jun 2019 | [MariaDB 10.3.16](mariadb-10316-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10316-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10316-changelog.md)   |
| 14 May 2019 | [MariaDB 10.3.15](mariadb-10315-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10315-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10315-changelog.md)   |
| 2 Apr 2019  | [MariaDB 10.3.14](mariadb-10314-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10314-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10314-changelog.md)   |
| 21 Feb 2019 | [MariaDB 10.3.13](mariadb-10313-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10313-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10313-changelog.md)   |
| 7 Jan 2019  | [MariaDB 10.3.12](mariadb-10312-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10312-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10312-changelog.md)   |
| 20 Nov 2018 | [MariaDB 10.3.11](mariadb-10311-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10311-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10311-changelog.md)   |
| 4 Oct 2018  | [MariaDB 10.3.10](mariadb-10310-release-notes.md)                                                                                                                             | Stable (GA)            | [Release Notes](mariadb-10310-release-notes.md)                                                                                                                           | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10310-changelog.md)   |
| 15 Aug 2018 | [MariaDB 10.3.9](mariadb-1039-release-notes.md)                                                                                                                               | Stable (GA)            | [Release Notes](mariadb-1039-release-notes.md)                                                                                                                            | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1039-changelog.md)    |
| 2 Jul 2018  | [MariaDB 10.3.8](mariadb-1038-release-notes.md)                                                                                                                               | Stable (GA)            | [Release Notes](mariadb-1038-release-notes.md)                                                                                                                            | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1038-changelog.md)    |
| 25 May 2018 | [MariaDB 10.3.7](mariadb-1037-release-notes.md)                                                                                                                               | Stable (GA)            | [Release Notes](mariadb-1037-release-notes.md)                                                                                                                            | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1037-changelog.md)    |
| 16 Apr 2018 | [MariaDB 10.3.6](mariadb-1036-release-notes.md)                                                                                                                               | Release Candidate (RC) | [Release Notes](mariadb-1036-release-notes.md)                                                                                                                            | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1036-changelog.md)    |
| 26 Feb 2018 | [MariaDB 10.3.5](mariadb-1035-release-notes.md)                                                                                                                               | Release Candidate (RC) | [Release Notes](mariadb-1035-release-notes.md)                                                                                                                            | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1035-changelog.md)    |
| 18 Jan 2018 | [MariaDB 10.3.4](mariadb-1034-release-notes.md)                                                                                                                               | Beta                   | [Release Notes](mariadb-1034-release-notes.md)                                                                                                                            | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1034-changelog.md)    |
| 23 Dec 2017 | [MariaDB 10.3.3](mariadb-1033-release-notes.md)                                                                                                                               | Beta                   | [Release Notes](mariadb-1033-release-notes.md)                                                                                                                            | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1033-changelog.md)    |
| 9 Oct 2017  | [MariaDB 10.3.2](mariadb-1032-release-notes.md)                                                                                                                               | Alpha                  | [Release Notes](mariadb-1032-release-notes.md)                                                                                                                            | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1032-changelog.md)    |
| 29 Aug 2017 | [MariaDB 10.3.1](mariadb-1031-release-notes.md)                                                                                                                               | Alpha                  | [Release Notes](mariadb-1031-release-notes.md)                                                                                                                            | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1031-changelog.md)    |
| 16 Apr 2017 | [MariaDB 10.3.0](mariadb-1030-release-notes.md)                                                                                                                               | Alpha                  | [Release Notes](mariadb-1030-release-notes.md)                                                                                                                            | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1030-changelog.md)    |

## See Also

* [Getting, Installing, and Upgrading MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb)
* [View the source tree](https://github.com/MariaDB/server/tree/10.3)
* [10.3 Features/fixes by vote](https://jira.mariadb.org/issues/?jql=project%20%3D%20MDEV%20AND%20fixVersion%20%3D%2010.3%20ORDER%20BY%20votes%20DESC)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
