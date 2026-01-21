# MariaDB versus MySQL - Features

MariaDB Corporation has a [**MariaDB vs MySQL**](https://mariadb.com/resources/guides-whitepapers/MariaDB-vs-MySQL) white paper available for download.

See also [**MariaDB vs MySQL - Compatibility**](mariadb-vs-mysql-compatibility.md)

#### Differences Per Release

For differences between specific releases, see

* [Incompatibilities and Feature Differences Between MariaDB Rolling and MySQL 8.0](incompatibilities-and-feature-differences-between-mariadb-rolling-and-mysql.md)
* [Incompatibilities and Feature Differences Between MariaDB 11.4 and MySQL 8.0](incompatibilities-and-feature-differences-between-mariadb-11-4-and-mysql-8.md)
* [Incompatibilities and Feature Differences Between MariaDB 11.3 and MySQL 8.0](incompatibilities-and-feature-differences-between-mariadb-and-mysql-unmaint/incompatibilities-and-feature-differences-between-mariadb-11-3-and-mysql-8.md)
* [Incompatibilities and Feature Differences Between MariaDB 11.2 and MySQL 8.0](incompatibilities-and-feature-differences-between-mariadb-and-mysql-unmaint/incompatibilities-and-feature-differences-between-mariadb-11-2-and-mysql-8.md)
* [Incompatibilities and Feature Differences Between MariaDB 10.11 and MySQL 8.0](incompatibilities-and-feature-differences-between-mariadb-10-11-and-mysql-8.md)
* [Incompatibilities and Feature Differences Between MariaDB 10.6 and MySQL 8.0](incompatibilities-and-feature-differences-between-mariadb-10-6-and-mysql-8.md)
* For unmaintained versions, see [Incompatibilities and Feature Differences Between MariaDB and MySQL - Unmaintained Series](incompatibilities-and-feature-differences-between-mariadb-and-mysql-unmaint/)

For a detailed breakdown of system variable differences, see:

* [System Variable Differences Between MariaDB Rolling and MySQL 8.0](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-rolling-and-mysql-8-0.md)
* [System variable differences between MariaDB 11.4 and MySQL 8.0](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-11-4-and-mysql-8-0.md)
* [System variable differences between MariaDB 11.3 and MySQL 8.0](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-11-3-and-mysql-8-0.md)
* [System variable differences between MariaDB 11.2 and MySQL 8.0](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-11-2-and-mysql-8-0.md)
* [System variable differences between MariaDB 10.11 and MySQL 8.0](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-10-11-and-mysql-8-0.md)
* [System variable differences between MariaDB 10.6 and MySQL 8.0](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-10-6-and-mysql-8-0.md)
* For unmaintained versions, see [System Variable Differences Between MariaDB and MySQL - Unmaintained Series](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/)

For a detailed breakdown of function differences, see:

* [Function Differences Between MariaDB Rolling and MySQL 8.0](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-rolling-and-mysql-8-0.md)
* [Function Differences Between MariaDB 11.4 and MySQL 8.0](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-11-4-and-mysql-8-0.md)
* [Function Differences Between MariaDB 11.3 and MySQL 8.0](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-and-mysql-unmaintained-series/function-differences-between-mariadb-11-3-and-mysql-8-0.md)
* [Function Differences Between MariaDB 11.2 and MySQL 8.0](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-and-mysql-unmaintained-series/function-differences-between-mariadb-11-2-and-mysql-8-0.md)
* [Function Differences Between MariaDB 10.11 and MySQL 8.0](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-10-11-and-mysql-8-0.md)
* [Function Differences Between MariaDB 10.6 and MySQL 8.0](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-10-6-and-mysql-8-0.md)
* For unmaintained versions, see [Function Differences Between MariaDB and MySQL - Unmaintained Series](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-and-mysql-unmaintained-series/)

#### More Storage Engines

In addition to the standard [MyISAM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myisam-storage-engine), [BLACKHOLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/blackhole), [CSV](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/csv), [MEMORY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/memory-storage-engine), [ARCHIVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/archive), and [MERGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/merge) storage engines, the following are also included with MariaDB Source and Binary packages:

* [ColumnStore](../../../columnstore/), a column oriented storage engine optimized for Data warehousing.
* [MyRocks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks), a storage engine with great compression, in 10.2
* [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria), MyISAM replacement with better caching.
* [FederatedX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/federatedx-storage-engine) (drop-in replacement for Federated)
* [OQGRAPH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/oqgraph-storage-engine) (In [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) and later. Disabled in [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) only.)
* [SphinxSE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/sphinx-storage-engine) (In [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) and later)
* [CONNECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) in [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) and later.
* [SEQUENCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/sequence-storage-engine) in [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) and later.
* [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) in [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) and later.
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) (In [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) and later, removed in 10.6)
* [Cassandra](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/cassandra/cassandra-storage-engine-overview) (In [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), removed in 10.6)

#### Speed Improvements

* MariaDB now provides much faster privilege checks for setups with many user accounts or many database
* The new [FLUSH SSL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) command allows SSL certificates to be reloaded without restarting the server
* Many optimizer enhancements in [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md). [Subqueries](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/subqueries) are now finally usable.\
  The complete list and a comparison with MySQL is [here](optimizer-feature-comparison-matrix.md). A benchmark can be found [here](https://mariadb.com/blog/mariadb-53-optimizer-benchmark).
* Faster and safer replication:[Group commit for the binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log). This makes many setups that use replication and lots of updates [more than 2x times faster](https://www.facebook.com/note.php?note_id=10150211546215933).
* [Parallel replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/parallel-replication) — new in 10.0
* [Improvements](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/general-info/quality/benchmarks-and-long-running-tests/benchmarks/mariadb-53-asynchronous-io-on-windows-with-innodb) for InnoDB asynchronous IO subsystem on Windows.
* Indexes for the [MEMORY(HEAP)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/memory-storage-engine) engine are faster. According to a simple test, 24% faster on INSERT for integer index and 60% faster for index on a CHAR(20) column. Fixed in [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) and MySQL 5.7.
* [Segmented Key Cache](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/segmented-key-cache) for MyISAM. Can speed up MyISAM tables with up to 4x\
  — new in 5.2
* [Adjustable hash size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myisam-storage-engine/myisam-system-variables#key_cache_file_hash_size) for MyISAM and Aria. This can greatly improve shutdown time (from hours to minutes) if using a lot of MyISAM/Aria tables with delayed keys — new in 10.0.13
* [CHECKSUM TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/checksum-table) is faster.
* We improved the performance of character set conversions (and removed conversions when they were not really needed). Overall speed improvement is 1-5 % (according to sql-bench) but can be\
  higher for big result sets with all characters between 0x00-0x7f.
* [Pool of Threads in MariaDB 5.1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb-51-53) and even better in [MariaDB 5.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb). This allows MariaDB to run with 200,000+ connections and with a notable speed improvement when using many connections.
* Several speed improvements when a client connects to MariaDB. Many of the improvements were done in [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) and [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md).
* There are some improvements to the DBUG code to make its execution faster when debug is compiled in but not used.
* Our use of the Aria storage engine enables faster complex queries (queries which normally use disk-based temporary tables). The [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) storage engine is used for internal temporary tables, which should give a speedup when doing complex selects. Aria is usually faster for temporary tables when\
  compared to MyISAM because Aria caches row data in memory and normally doesn't have to write the temporary rows to disk. The test suite has been extended and now runs much faster than before, even though it tests more things.

#### Extensions & New Features

We've added a lot of new features to MariaDB. If a patch or feature is useful, safe, and stable — we make every effort to include it in MariaDB. The most notable features are:

* Support introduced for [System-versioned tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables). Allows queries to access both current and historic data, aiding in managing retention, analysis and point-in-time recovery. — new in 10.3
* [ALTER TABLE... DROP COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#drop-column) can now run as Instant operations. Can also now change the ordering of columns. — new in 10.4
* Support introduced for password expiration, using the [user password expiry](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/user-account-management/user-password-expiry) — new in 10.4
* In order to support the use of multiple authentication plugins for a single user, the [mysql.user](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-user-table) system table has been retired in favor of the [mysql.glob\_priv](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-global_priv-table) system table. — new in 10.4
* The [unix\_socket authentication plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) is now the default on Unix-like systems. This represents a major change to authentication in MariaDB — new in 10.4
* Support introduced for [Optimizer Trace](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/compatibility-and-differences/broken-reference/README.md), which provides detailed information on how the Optimizer processes queries. To enable Optimizer Trace, set the [optimizer\_trace](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_trace) system variable — new in 10.4
* The MariaDB SQL/PL stored procedure dialect (enabled with [sql\_mode=ORACLE](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/compatibility-and-differences/broken-reference/README.md)) now supports Oracle style packages. Support for the following statements are available: [CREATE PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-package), [CREATE PACKAGE BODY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-package-body), [DROP PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-package), [DROP PACKAGE BODY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-package-body), [SHOW CREATE PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-package), [SHOW CREATE PACKAGE BODY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-package-body) — new in 10.3
* Automatic collection of [Engine Independent Table Statistics](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics) — new in 10.4
* Support for the use of parentheses (brackets) for specifying precedence in the ordering of execution for [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statements and [Table Value Operations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations/precedence-control-in-table-operations), (including the use of [UNION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations/union), [EXCEPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations/except), [INTERSECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations/intersect) operations) — new in 10.4
* Support for [anchored data types](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/declare-variable#type-of-row-type-of) added to local stored procedure variables. — new in 10.3
* Support added for [Stored Aggregate](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-functions/stored-aggregate-functions) functions — new in 10.3
* Oracle compatible [SUBSTR()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/substring) function is available — new in 10.3
* Oracle compatible SEQUENCE support is provided — new in 10.3
* Support for [anchored data types](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/declare-variable#type-of-row-type-of) added to [stored routine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-procedures) variables — new in 10.3
* Support for [anchored data types](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/declare-variable#type-of-row-type-of) added to stored routine parameters — new in 10.3
* [Cursors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors/cursor-overview) with parameters are now supported — new in 10.3
* [INVISIBLE columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/invisible-columns) are now supported — new in 10.3
* [Instant ADD COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-online-ddl/instant-add-column-for-innodb) is now available for InnoDB — new in 10.3
* [Window functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions) are supported — new in 10.2
* Number of supported decimals in [DECIMAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/decimal) has increased from `30` to `38` — new in 10.2
* [Recursive Common Table Expressions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/recursive-common-table-expressions-overview) — new in 10.2
* New [WITH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/with) statement. `WITH` is a common table expression that allows one to refer to a subquery expression many times in a query — new in 10.2
* [CHECK CONSTRAINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/constraint) — new in 10.2
* [DEFAULT expression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table), including `DEFAULT` for `BLOB` and `TEXT` — new in 10.2
* Added catchall for [list partitions](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/compatibility-and-differences/broken-reference/README.md) — new in 10.2
* Oracle-style [EXECUTE IMMEDIATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/prepared-statements/execute-immediate) statement — new in 10.2
* Several new [JSON functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions) — new in 10.2
* [Microsecond Precision in Processlist](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/time_ms-column-in-information_schemaprocesslist)
* [Table Elimination](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/table-elimination)
* [Virtual Columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/generated-columns) — new in 5.2
* [Microseconds in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/microseconds-in-mariadb) — new in 5.3
* [Extended User Statistics](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics) — new in 5.2
* [KILL all queries for a user](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill) — new in 5.3,
* [KILL QUERY ID - terminates the query by query\_id, leaving the connection intact](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill) — new in 10.0.5,
* [Pluggable Authentication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/pluggable-authentication-overview) — new in 5.2
* [Storage-engine-specific CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/storage-engines-storage-engine-development/engine-defined-new-tablefieldindex-attributes) — new in 5.2
* [Enhancements to INFORMATION SCHEMA.PLUGINS table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema) — new in 5.2
* [Group commit for the binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log). This makes [replication notably faster!](https://www.facebook.com/note.php?note_id=10150261692455933) — new in 5.3
* Added `--rewrite-db` [mysqlbinlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) option to change the used database — new in 5.2
* [Progress reporting](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting) for [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) and [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) — new in 5.3
* Faster [joins and subqueries](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations) — new in 5.3
* [HandlerSocket](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/nosql/handlersocket) and faster [HANDLER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/nosql/handler) calls — new in 5.3
* [Dynamic Columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/nosql/dynamic-columns) support — new in 5.3
* [GIS Functionality](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry) — new in 5.3
* [Multi-source replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/multi-source-replication) — new in 10.0
* [Global Transaction ID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) — new in 10.0
* [SHOW EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-explain) gives the EXPLAIN plan for a query running in another thread. — new in 10.0
* [Roles](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/user-account-management/roles) — new in 10.0
* [PCRE Regular Expressions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) (including [REGEXP\_REPLACE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/regexp_replace)) — new in 10.0
* [CREATE OR REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table#create-or-replace)
* [DELETE ... RETURNING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) — new in 10.0
* MariaDB [supports more collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations) than MySQL.

For a full list, please see [features for each release](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-in-the-different-mariadb-releases/README.md)

#### Better Testing

* More tests in the test suite.
* Bugs in tests fixed.
* Test builds with different configure options to get better feature testing.
* Remove invalid tests. (e.g. don't test feature ''X'' if that feature is not\
  in the tested build)

#### Fewer Warnings and Fewer Bugs

* Bugs are bad. Fix as many bugs as possible and try to not introduce new ones.
* Compiler warnings are also bad. Eliminate as many compiler warnings as possible.

#### Truly Open Source

* All code in MariaDB is released under GPL, LGPL or BSD.
* MariaDB does not have closed source modules like the ones that can be found in MySQL Enterprise Edition. In fact, all the closed source features in MySQL 5.5 Enterprise Edition are found in the MariaDB open source version.
* MariaDB client libraries (for C, for Java (JDBC), for Windows (ODBC)) are released under LGPL to allow linking with closed source software. MySQL client libraries are released under GPL that does not allow linking with closed source software.
* MariaDB includes test cases for all fixed bugs. Oracle doesn't provide test cases for new bugs fixed in MySQL 5.5.
* All [bugs](https://jira.mariadb.org) and [development plans](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/general-info/mariadb-server-roadmap) are public.
* MariaDB is developed by the community in true open source spirit.

#### Related Links

* [Compatiblity between MariaDB and MySQL](mariadb-vs-mysql-compatibility.md)
* [Moving from MySQL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql)
* [Troubleshooting Installation Issues](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
