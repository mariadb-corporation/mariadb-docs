# MariaDB 10.2 Changes & Improvements

[MariaDB 10.2](what-is-mariadb-102.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

The most recent release of [MariaDB 10.2](what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[MariaDB 10.2](what-is-mariadb-102.md) is a previous major stable version. The first stable release was in May 2017.

For details on upgrading from [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md), see [Upgrading from MariaDB 10.1 to 10.2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-101-to-mariadb-102).

The following lists the major new features in [MariaDB 10.2](what-is-mariadb-102.md):

## Implemented Features

### InnoDB as Default

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) is now the default storage engine. Until [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md), MariaDB used the XtraDB storage engine as default. XtraDB in 10.2 is not up to date with the latest features of InnoDB and cannot be used. As the InnoDB on disk format is identical to XtraDB's this will not cause any problems when upgrading to [MariaDB 10.2](what-is-mariadb-102.md). See [Why does MariaDB 10.2 use InnoDB instead of XtraDB?](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-101-to-mariadb-102#innodb-instead-of-xtradb)

### Syntax / General Features

* [MyRocks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks) storage engine added. (It has its own [maturity level](../../about/release-criteria.md). In [MariaDB 10.2.14](mariadb-10214-release-notes.md), it is considered Gamma) ([MDEV-9658](https://jira.mariadb.org/browse/MDEV-9658))
* [Window functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions) have been introduced.
* The [SHOW CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-user) statement was introduced
* New [CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/create-user) options for limiting resource usage and tls/ssl
* New [ALTER USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/alter-user) statement
* [Non-recursive Common Table Expressions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/non-recursive-common-table-expressions-overview)
* [Recursive Common Table Expressions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/recursive-common-table-expressions-overview) ([MDEV-9864](https://jira.mariadb.org/browse/MDEV-9864))
* New [WITH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/with) statement. `WITH` is a common table expression that allows you to refer to a subquery expression many times in a query ([MDEV-8308](https://jira.mariadb.org/browse/MDEV-8308) & [MDEV-9864](https://jira.mariadb.org/browse/MDEV-9864)) — Original code from Galina Shalygina
* Support for [CHECK CONSTRAINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/constraint) ([MDEV-7563](https://jira.mariadb.org/browse/MDEV-7563))
* Support for [DEFAULT with expressions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table#default) ([MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134))
* [BLOB and TEXT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/blob-and-text-data-types) fields can now have a [DEFAULT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table#default) value
* Lots of restrictions lifted for [Virtual computed columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/generated-columns)
* Number of supported decimals in [DECIMAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/decimal) has increased from `30` to `38` ([MDEV-10138](https://jira.mariadb.org/browse/MDEV-10138))
* Added catchall for [list partitions](https://mariadb.com/docs/server/server-usage/partitioning-tables/partitioning-types/list-partitioning-type) ([MDEV-8348](https://jira.mariadb.org/browse/MDEV-8348))
* Oracle-style [EXECUTE IMMEDIATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/prepared-statements/execute-immediate) statement ([MDEV-10585](https://jira.mariadb.org/browse/MDEV-10585))
* [PREPARE Statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/prepared-statements/prepare-statement)/Dynamic SQL now understand most expressions ([MDEV-10866](https://jira.mariadb.org/browse/MDEV-10866), [MDEV-10709](https://jira.mariadb.org/browse/MDEV-10709)).
* InnoDB tables now support [spatial indexes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry/spatial-index)
* [ed25519 authentication plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-ed25519) ([MDEV-12160](https://jira.mariadb.org/browse/MDEV-12160))
* Better InnoDB crash recovery progress reporting ([MDEV-11027](https://jira.mariadb.org/browse/MDEV-11027))
* Improvements to InnoDB startup/shutdown to make it more robust
* [AWS Key Management plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin) added for Windows, CentOS, RHEL, and Fedora packages
* [Atomic writes support made more general](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/atomic-write-support). [Shannon system SSD cards](https://www.shannon-sys.com) are now supported.

### Incompatible Changes

* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) has been split into a separate package, mariadb-plugin-tokudb.
* [SQL\_MODE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) has been changed; in particular, NOT NULL fields with no default will no longer fall back to a dummy value for inserts which do not specify a value for that field.
* Replication from legacy MySQL servers may require setting [binlog\_checksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) to NONE.
* New [reserved words](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/reserved-words): OVER, RECURSIVE, and ROWS.

### Triggers

* Multiple [triggers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/triggers-events/triggers/trigger-overview) for the same event ([MDEV-6112](https://jira.mariadb.org/browse/MDEV-6112))
* The FOLLOWS/PRECEDES clauses have been added to the [CREATE TRIGGER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/triggers-events/triggers/create-trigger) statement
* Multiple triggers are now counted in the Executed\_triggers status variable ([MDEV-10915](https://jira.mariadb.org/browse/MDEV-10915))
* [SHOW TRIGGERS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-triggers) and [SHOW CREATE TRIGGER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-trigger) now include the date and time the trigger was created

### Replication / Binary Log

* DML\_only [flashback](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/flashback) can rollback instances/databases/tables to an old snapshot ([MDEV-10570](https://jira.mariadb.org/browse/MDEV-10570))
* New variable [read\_binlog\_speed\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) permits restricting the speed at which the slave reads the binlog from the master ([MDEV-11064](https://jira.mariadb.org/browse/MDEV-11064)) — Original code from Tencent Game DBA Team, developed by chouryzhou.
* [Delayed replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/delayed-replication) is supported ([MDEV-7145](https://jira.mariadb.org/browse/MDEV-7145)) — Backported from MySQL 5.6 by Kristian Nielsen funded by Booking.com.
* [Compression of events in the binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/compressing-events-to-reduce-size-of-the-binary-log) is supported ([MDEV-11065](https://jira.mariadb.org/browse/MDEV-11065)) — Original code from Tencent Game DBA Team, developed by vinchen.
* Default [binary log format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) changed to mixed ([MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635))
* Default value of [replicate\_annotate\_row\_events](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) changed to `ON` ([MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635))
* Default value of [slave\_net\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) reduced to 60 seconds ([MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635))
* Default [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) changed from `0` to `1`

### GeoJSON / JSON

* The [JSON data type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/json) (an alias for LONGTEXT) was introduced.
* [JSON functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions) added ([MDEV-9143](https://jira.mariadb.org/browse/MDEV-9143))
* Implement [ST\_AsGeoJSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-constructors/geojson-st_asgeojson) and [ST\_GeomFromGeoJSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-constructors/st_geomfromgeojson) functions so the spatial features can be imported/exported using GeoJSON format ([MDEV-11042](https://jira.mariadb.org/browse/MDEV-11042))

### Information Schema

* An information schema plugin to report all user variables, which creates the [Information Schema USER\_VARIABLES Table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-user_variables-table) ([MDEV-7331](https://jira.mariadb.org/browse/MDEV-7331))
* Changes to the [Information Schema COLUMNS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-columns-table) table. Literals are now quoted in the `COLUMN_DEFAULT` column to distinguish them from expressions ([MDEV-13132](https://jira.mariadb.org/browse/MDEV-13132)), and two new columns added providing information about [generated (virtual, or computed)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/generated-columns) columns ([MDEV-9255](https://jira.mariadb.org/browse/MDEV-9255)).

### EXPLAIN

* [EXPLAIN FORMAT=JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain-format-json) now shows `outer_ref_condition` field which contains the condition that the(?) SELECT checks on each re-execution ([MDEV-9652](https://jira.mariadb.org/browse/MDEV-9652))
* [EXPLAIN FORMAT=JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain-format-json) now shows `sort_key` field which shows the sort criteria used by `filesort` operation. ([commit 2078392](https://github.com/MariaDB/server/commit/2078392cc9bb49720ca3949731078af113ae4f43))
* EXPLAIN used to show incorrect information about how the optimizer resolved `ORDER BY` clause or `Distinct`. This was a long-standing problem with roots back in MySQL. Now, after [MDEV-8646](https://jira.mariadb.org/browse/MDEV-8646) and related fixes, the problem doesn't exist anymore. (For test cases, see [MDEV-7982](https://jira.mariadb.org/browse/MDEV-7982), [MDEV-8857](https://jira.mariadb.org/browse/MDEV-8857), [MDEV-7885](https://jira.mariadb.org/browse/MDEV-7885), [MDEV-326](https://jira.mariadb.org/browse/MDEV-326))

### Optimizations

* Connection setup was made faster by moving creation of THD to new thread ([MDEV-6150](https://jira.mariadb.org/browse/MDEV-6150))
* Pushdown conditions into non-mergeable views/derived tables ([MDEV-9197](https://jira.mariadb.org/browse/MDEV-9197), [condition-pushdown-into-derived-table-optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizations-for-derived-tables/condition-pushdown-into-derived-table-optimization) ) — Original code from Galina Shalygina
* [ANALYZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/analyze-table) has been re-implemented so as not to lock the entire table when collecting engine independent statistics ([MDEV-7901](https://jira.mariadb.org/browse/MDEV-7901))
* Internal CRC32 routines use the optimized implementation on Power8 — [MDEV-9872](https://jira.mariadb.org/browse/MDEV-9872)
* Table cache can automatically partition itself as needed to reduce the contention ([MDEV-10296](https://jira.mariadb.org/browse/MDEV-10296))

### Compatibility

* 88 new [NO PAD collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/char) added. In `NO PAD` collations, end spaces are significant in comparisons ([MDEV-9711](https://jira.mariadb.org/browse/MDEV-9711)) — Original code from Daniil Medvedev
* MariaDB now works when started with a MySQL 5.7.6+ data directory ([MDEV-11170](https://jira.mariadb.org/browse/MDEV-11170))

### CONNECT

* [Zipped File Tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect/connect-table-types/connect-zipped-file-tables) for the CONNECT storage engine ([MDEV-11295](https://jira.mariadb.org/browse/MDEV-11295))
* The CONNECT engine now supports the [JDBC Table type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect/connect-table-types/connect-jdbc-table-type-accessing-tables-from-another-dbms) ([MDEV-9765](https://jira.mariadb.org/browse/MDEV-9765))

### System Variables

For a list of all new system variables, see [System Variables Added in MariaDB 10.2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-102). Variable changes include:

* New variable to disable deadlock detection [innodb\_deadlock\_detect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables)
* [aria\_recover](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-system-variables#aria_recover) has been renamed to [aria\_recover\_options](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-system-variables#aria_recover_options) ([MDEV-8542](https://jira.mariadb.org/browse/MDEV-8542))
* Default values of the [aria\_recover](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-system-variables#aria_recover) and [myisam\_recover\_options](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myisam-storage-engine/myisam-system-variables#myisam_recover_options) system variables changed to `BACKUP,QUICK`
* The server version can now be faked to work around dated applications that require a particular [version string](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/version) ([MDEV-7780](https://jira.mariadb.org/browse/MDEV-7780))
* [slave\_parallel\_workers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is now an alias for slave\_parallel\_threads
* New status variables [com\_alter\_user](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#com_alter_user), [com\_multi](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#com_multi) and [com\_show\_create\_user](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#com_show_create_user)
* New variable for setting a directory for storing temporary non-tablespace InnoDB files, [innodb\_tmpdir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables)
* New variable [read\_binlog\_speed\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) permits restricting the speed at which the slave reads the binlog from the master ([MDEV-11064](https://jira.mariadb.org/browse/MDEV-11064))
* [innodb\_log\_files\_in\_group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) can now be set to `1` ([MDEV-12061](https://jira.mariadb.org/browse/MDEV-12061))
* The thread pool now gives higher priority to connections that have an active transaction. This can be controlled with the new [thread\_pool\_prio\_kickup\_timer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables) and [thread\_pool\_priority](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables) system variables. ([MDEV-10297](https://jira.mariadb.org/browse/MDEV-10297))
* Default value of [group\_concat\_max\_len](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#group_concat_max_len) changed to 1M ([MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635))
* Default value of [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#sql_mode) changed to STRICT\_TRANS\_TABLES,ERROR\_FOR\_DIVISION\_BY\_ZERO,NO\_AUTO\_CREATE\_USER,NO\_ENGINE\_SUBSTITUTION ([MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635)) ([MariaDB 10.2.4](mariadb-1024-release-notes.md) and later)
* Default value of [innodb\_compression\_algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) changed to `zlib` - this does not mean pages are now compressed by default, see [compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) ([MDEV-11838](https://jira.mariadb.org/browse/MDEV-11838))
* Default value of [innodb\_log\_compressed\_pages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) changed to `ON` from [MariaDB 10.1.2](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes) to [MariaDB 10.1.25](../release-notes-mariadb-10-1-series/mariadb-10125-release-notes.md) ([MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635) and [MDEV-13247](https://jira.mariadb.org/browse/MDEV-13247))
* Default value of [innodb\_use\_atomic\_writes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) and [innodb\_use\_trim](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) changed to `ON`
* The unused [innodb\_api\_\*](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) variables have been removed ([MDEV-12050](https://jira.mariadb.org/browse/MDEV-12050))
* [tmp\_disk\_table\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tmp_disk_table_size) was added to allow one to limit the size of temporary disk tables stored in tmpdir. At the same time [tmp\_memory\_table\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tmp_memory_table_size) was added an alias for [tmp\_table\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tmp_table_size). At some point we plan to deprecate `tmp_table_size`. ([MariaDB 10.2.7](mariadb-1027-release-notes.md) and later).

### Status Variables

For a list of all new status variables, see [Status Variables Added in MariaDB 10.2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/status-variables-added-in-mariadb-102).

### Scripts

* Continuous binary log backup has been added to [mysqlbinlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) ([MDEV-8713](https://jira.mariadb.org/browse/MDEV-8713))
* [mysql\_zap](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_zap) and mysqlbug have been removed ([MDEV-7376](https://jira.mariadb.org/browse/MDEV-7376), [MDEV-8654](https://jira.mariadb.org/browse/MDEV-8654))

### Other Changes

* Added support for OpenSSL 1.1 and LibreSSL ([MDEV-10332](https://jira.mariadb.org/browse/MDEV-10332))
* Persistent [AUTO\_INCREMENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/auto_increment) for InnoDB ([MDEV-6076](https://jira.mariadb.org/browse/MDEV-6076))
* Support COM\_RESET\_CONNECTION ([MDEV-10340](https://jira.mariadb.org/browse/MDEV-10340))
* "fast mutexes" have been removed. These aren't faster than normal mutexes, and have been disabled by default for years ([MDEV-8111](https://jira.mariadb.org/browse/MDEV-8111))
* Old GPL client library is gone; now MariaDB Server comes with the LGPL Connector/C client library ([MDEV-9055](https://jira.mariadb.org/browse/MDEV-9055))
* MariaDB is no longer compiled with jemalloc
* TokuDB is now a separate package, not part of the server RPM (because TokuDB still needs jemalloc).
* Upgrading to a new major release no longer requires setting [innodb\_fast\_shutdown](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) to `0`. Omitting it can make the upgrade process a lot faster. ([MDEV-12289](https://jira.mariadb.org/browse/MDEV-12289))

#### Security Vulnerabilities Fixed in [MariaDB 10.2](what-is-mariadb-102.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2022-32088](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32088): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2022-32083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32083): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2022-31624](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31624): [MariaDB 10.2.41](mariadb-10241-release-notes.md)
* [CVE-2022-27445](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27445): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2022-27387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27387): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2022-27386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27386): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2022-27384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27384): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2022-27383](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27383): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2022-27381](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27381): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2022-27380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27380): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2022-27378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27378): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2022-27377](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27377): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2022-24052](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24052): [MariaDB 10.2.42](mariadb-10242-release-notes.md)
* [CVE-2022-24051](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24051): [MariaDB 10.2.42](mariadb-10242-release-notes.md)
* [CVE-2022-24050](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24050): [MariaDB 10.2.42](mariadb-10242-release-notes.md)
* [CVE-2022-24048](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24048): [MariaDB 10.2.42](mariadb-10242-release-notes.md)
* [CVE-2022-21595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21595): [MariaDB 10.2.42](mariadb-10242-release-notes.md)
* [CVE-2022-21451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21451): [MariaDB 10.2.38](mariadb-10238-release-notes.md)
* [CVE-2022-21427](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21427): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778): [MariaDB 10.2.42](mariadb-10242-release-notes.md)
* [CVE-2021-46669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46669): [MariaDB 10.2.44](mariadb-10244-release-notes.md)
* [CVE-2021-46668](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46668): [MariaDB 10.2.43](mariadb-10243-release-notes.md)
* [CVE-2021-46667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46667): [MariaDB 10.2.41](mariadb-10241-release-notes.md)
* [CVE-2021-46666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46666): [MariaDB 10.2.39](mariadb-10239-release-notes.md)
* [CVE-2021-46665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46665): [MariaDB 10.2.43](mariadb-10243-release-notes.md)
* [CVE-2021-46664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46664): [MariaDB 10.2.43](mariadb-10243-release-notes.md)
* [CVE-2021-46663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46663): [MariaDB 10.2.43](mariadb-10243-release-notes.md)
* [CVE-2021-46661](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46661): [MariaDB 10.2.43](mariadb-10243-release-notes.md)
* [CVE-2021-46659](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46659): [MariaDB 10.2.42](mariadb-10242-release-notes.md)
* [CVE-2021-46658](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46658): [MariaDB 10.2.40](mariadb-10240-release-notes.md)
* [CVE-2021-46657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46657): [MariaDB 10.2.39](mariadb-10239-release-notes.md)
* [CVE-2021-35604](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35604): [MariaDB 10.2.41](mariadb-10241-release-notes.md)
* [CVE-2021-27928](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27928): [MariaDB 10.2.37](mariadb-10237-release-notes.md)
* [CVE-2021-2389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2389): [MariaDB 10.2.40](mariadb-10240-release-notes.md)
* [CVE-2021-2372](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2372): [MariaDB 10.2.40](mariadb-10240-release-notes.md)
* [CVE-2021-2194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2194): [MariaDB 10.2.35](mariadb-10235-release-notes.md)
* [CVE-2021-2180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2180): [MariaDB 10.2.38](mariadb-10238-release-notes.md)
* [CVE-2021-2174](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2174): [MariaDB 10.2.18](mariadb-10218-release-notes.md)
* [CVE-2021-2166](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2166): [MariaDB 10.2.38](mariadb-10238-release-notes.md)
* [CVE-2021-2154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2154): [MariaDB 10.2.38](mariadb-10238-release-notes.md)
* [CVE-2021-2144](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2144): [MariaDB 10.2.28](mariadb-10228-release-notes.md)
* [CVE-2021-2022](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2022): [MariaDB 10.2.33](mariadb-10233-release-notes.md)
* [CVE-2021-2011](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2011): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2021-2007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2007): [MariaDB 10.2.26](mariadb-10226-release-notes.md)
* [CVE-2020-2922](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2922): [MariaDB 10.2.26](mariadb-10226-release-notes.md)
* [CVE-2020-28912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28912): [MariaDB 10.2.35](mariadb-10235-release-notes.md)
* [CVE-2020-2814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2814): [MariaDB 10.2.32](mariadb-10232-release-notes.md)
* [CVE-2020-2812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2812): [MariaDB 10.2.32](mariadb-10232-release-notes.md)
* [CVE-2020-2780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2780): [MariaDB 10.2.28](mariadb-10228-release-notes.md)
* [CVE-2020-2760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2760): [MariaDB 10.2.32](mariadb-10232-release-notes.md)
* [CVE-2020-2752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2752): [MariaDB 10.2.32](mariadb-10232-release-notes.md)
* [CVE-2020-2574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2574): [MariaDB 10.2.31](mariadb-10231-release-notes.md)
* [CVE-2020-15180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15180): [MariaDB 10.2.34](mariadb-10234-release-notes.md)
* [CVE-2020-14812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14812): [MariaDB 10.2.35](mariadb-10235-release-notes.md)
* [CVE-2020-14789](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14789): [MariaDB 10.2.35](mariadb-10235-release-notes.md)
* [CVE-2020-14776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14776): [MariaDB 10.2.35](mariadb-10235-release-notes.md)
* [CVE-2020-14765](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14765): [MariaDB 10.2.35](mariadb-10235-release-notes.md)
* [CVE-2020-14550](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14550): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2020-13249](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13249): [MariaDB 10.2.32](mariadb-10232-release-notes.md)
* [CVE-2019-2974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2974): [MariaDB 10.2.28](mariadb-10228-release-notes.md)
* [CVE-2019-2938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2938): [MariaDB 10.2.28](mariadb-10228-release-notes.md)
* [CVE-2019-2805](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2805): [MariaDB 10.2.26](mariadb-10226-release-notes.md)
* [CVE-2019-2758](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2758): [MariaDB 10.2.26](mariadb-10226-release-notes.md)
* [CVE-2019-2740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2740): [MariaDB 10.2.26](mariadb-10226-release-notes.md)
* [CVE-2019-2739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2739): [MariaDB 10.2.26](mariadb-10226-release-notes.md)
* [CVE-2019-2737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2737): [MariaDB 10.2.26](mariadb-10226-release-notes.md)
* [CVE-2019-2628](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2628): [MariaDB 10.2.24](mariadb-10224-release-notes.md)
* [CVE-2019-2627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2627): [MariaDB 10.2.24](mariadb-10224-release-notes.md)
* [CVE-2019-2614](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2614): [MariaDB 10.2.24](mariadb-10224-release-notes.md)
* [CVE-2019-2537](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2537): [MariaDB 10.2.22](mariadb-10222-release-notes.md)
* [CVE-2019-2510](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2510): [MariaDB 10.2.22](mariadb-10222-release-notes.md)
* [CVE-2019-2503](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2503): [MariaDB 10.2.18](mariadb-10218-release-notes.md)
* [CVE-2019-2455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2455): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-3284](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3284): [MariaDB 10.2.19](mariadb-10219-release-notes.md)
* [CVE-2018-3282](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3282): [MariaDB 10.2.19](mariadb-10219-release-notes.md)
* [CVE-2018-3277](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3277): [MariaDB 10.2.19](mariadb-10219-release-notes.md)
* [CVE-2018-3251](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3251): [MariaDB 10.2.19](mariadb-10219-release-notes.md)
* [CVE-2018-3200](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3200): [MariaDB 10.2.19](mariadb-10219-release-notes.md)
* [CVE-2018-3185](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3185): [MariaDB 10.2.19](mariadb-10219-release-notes.md)
* [CVE-2018-3174](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3174): [MariaDB 10.2.19](mariadb-10219-release-notes.md)
* [CVE-2018-3173](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3173): [MariaDB 10.2.19](mariadb-10219-release-notes.md)
* [CVE-2018-3162](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3162): [MariaDB 10.2.19](mariadb-10219-release-notes.md)
* [CVE-2018-3156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3156): [MariaDB 10.2.19](mariadb-10219-release-notes.md)
* [CVE-2018-3143](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3143): [MariaDB 10.2.19](mariadb-10219-release-notes.md)
* [CVE-2018-3133](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3133): [MariaDB 10.2.12](mariadb-10212-release-notes.md)
* [CVE-2018-3081](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3081): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-3066](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3066): [MariaDB 10.2.17](mariadb-10217-release-notes.md)
* [CVE-2018-3064](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3064): [MariaDB 10.2.17](mariadb-10217-release-notes.md)
* [CVE-2018-3063](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3063): [MariaDB 10.2.17](mariadb-10217-release-notes.md)
* [CVE-2018-3060](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3060): [MariaDB 10.2.17](mariadb-10217-release-notes.md)
* [CVE-2018-3058](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3058): [MariaDB 10.2.17](mariadb-10217-release-notes.md)
* [CVE-2018-2819](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2819): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2817): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2813](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2813): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2810](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2810): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2787](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2787): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2786](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2786): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2784](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2784): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2782): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2781): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2777](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2777): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2771): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2767](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2767): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2766](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2766): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2761](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2761): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2759](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2759): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2755](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2755): [MariaDB 10.2.15](mariadb-10215-release-notes.md)
* [CVE-2018-2668](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2668): [MariaDB 10.2.13](mariadb-10213-release-notes.md)
* [CVE-2018-2665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2665): [MariaDB 10.2.13](mariadb-10213-release-notes.md)
* [CVE-2018-2640](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2640): [MariaDB 10.2.13](mariadb-10213-release-notes.md)
* [CVE-2018-2622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2622): [MariaDB 10.2.13](mariadb-10213-release-notes.md)
* [CVE-2018-2612](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2612): [MariaDB 10.2.13](mariadb-10213-release-notes.md)
* [CVE-2018-2562](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2562): [MariaDB 10.2.13](mariadb-10213-release-notes.md)
* [CVE-2017-3653](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3653): [MariaDB 10.2.8](mariadb-1028-release-notes.md)
* [CVE-2017-3641](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3641): [MariaDB 10.2.8](mariadb-1028-release-notes.md)
* [CVE-2017-3636](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3636): [MariaDB 10.2.8](mariadb-1028-release-notes.md)
* [CVE-2017-3464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3464): [MariaDB 10.2.6](mariadb-1026-release-notes.md)
* [CVE-2017-3456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3456): [MariaDB 10.2.6](mariadb-1026-release-notes.md)
* [CVE-2017-3453](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3453): [MariaDB 10.2.6](mariadb-1026-release-notes.md)
* [CVE-2017-3313](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3313): [MariaDB 10.2.5](mariadb-1025-release-notes.md)
* [CVE-2017-3309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3309): [MariaDB 10.2.6](mariadb-1026-release-notes.md)
* [CVE-2017-3308](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3308): [MariaDB 10.2.6](mariadb-1026-release-notes.md)
* [CVE-2017-3302](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3302): [MariaDB 10.2.5](mariadb-1025-release-notes.md)
* [CVE-2017-3257](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3257): [MariaDB 10.2.8](mariadb-1028-release-notes.md)
* [CVE-2017-15365](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-15365): [MariaDB 10.2.10](mariadb-10210-release-notes.md)
* [CVE-2017-10384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10384): [MariaDB 10.2.8](mariadb-1028-release-notes.md)
* [CVE-2017-10379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10379): [MariaDB 10.2.8](mariadb-1028-release-notes.md)
* [CVE-2017-10378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10378): [MariaDB 10.2.10](mariadb-10210-release-notes.md)
* [CVE-2017-10365](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10365): [MariaDB 10.2.8](mariadb-1028-release-notes.md)
* [CVE-2017-10320](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10320): [MariaDB 10.2.8](mariadb-1028-release-notes.md)
* [CVE-2017-10286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10286): [MariaDB 10.2.8](mariadb-1028-release-notes.md)
* [CVE-2017-10268](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10268): [MariaDB 10.2.10](mariadb-10210-release-notes.md)
* [CVE-2016-9843](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-9843): [MariaDB 10.2.19](mariadb-10219-release-notes.md)

## Comparison with MySQL

* [Incompatibilities and Feature Differences Between MariaDB 10.2 and MySQL 5.7](../../about/compatibility-and-differences/incompatibilities-and-feature-differences-between-mariadb-and-mysql-unmaint/incompatibilities-and-feature-differences-between-mariadb-10-2-and-mysql-5.md)
* [System Variable Differences Between MariaDB 10.2 and MySQL 5.7](../../about/compatibility-and-differences/system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-10-2-and-mysql-5-7.md)
* [Function Differences Between MariaDB 10.2 and MySQL 5.7](../../about/compatibility-and-differences/function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-and-mysql-unmaintained-series/function-differences-between-mariadb-102-and-mysql-57.md)
* [System Variable Differences Between MariaDB 10.2 and MySQL 5.6](../../about/compatibility-and-differences/system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-10-2-and-mysql-5-6.md)
* [Function Differences Between MariaDB 10.2 and MySQL 5.6](../../about/compatibility-and-differences/function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-and-mysql-unmaintained-series/function-differences-between-mariadb-102-and-mysql-56.md)

## List of All [MariaDB 10.2](what-is-mariadb-102.md) Releases

| Date        | Release                                                                                                                                                                   | Status      | Release Notes                                                                                                                                 | Changelog                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| 20 May 2022 | [MariaDB 10.2.44](mariadb-10244-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10244-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10244-changelog.md) |
| 12 Feb 2022 | [MariaDB 10.2.43](mariadb-10243-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10243-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10243-changelog.md) |
| 9 Feb 2022  | [MariaDB 10.2.42](mariadb-10242-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10242-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10242-changelog.md) |
| 8 Nov 2021  | [MariaDB 10.2.41](mariadb-10241-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10241-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10241-changelog.md) |
| 6 Aug 2021  | [MariaDB 10.2.40](mariadb-10240-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10240-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10240-changelog.md) |
| 23 Jun 2021 | [MariaDB 10.2.39](mariadb-10239-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10239-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10239-changelog.md) |
| 7 May 2021  | [MariaDB 10.2.38](mariadb-10238-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10238-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10238-changelog.md) |
| 22 Feb 2021 | [MariaDB 10.2.37](mariadb-10237-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10237-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10237-changelog.md) |
| 11 Nov 2020 | [MariaDB 10.2.36](mariadb-10236-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10236-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10236-changelog.md) |
| 3 Nov 2020  | [MariaDB 10.2.35](mariadb-10235-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10235-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10235-changelog.md) |
| 7 Oct 2020  | [MariaDB 10.2.34](mariadb-10234-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10234-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10234-changelog.md) |
| 10 Aug 2020 | [MariaDB 10.2.33](mariadb-10233-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10233-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10233-changelog.md) |
| 12 May 2020 | [MariaDB 10.2.32](mariadb-10232-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10232-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10232-changelog.md) |
| 28 Jan 2020 | [MariaDB 10.2.31](mariadb-10231-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10231-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10231-changelog.md) |
| 11 Dec 2019 | [MariaDB 10.2.30](mariadb-10230-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10230-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10230-changelog.md) |
| 8 Nov 2019  | [MariaDB 10.2.29](mariadb-10229-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10229-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10229-changelog.md) |
| 5 Nov 2019  | [MariaDB 10.2.28](mariadb-10228-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10228-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10228-changelog.md) |
| 11 Sep 2019 | [MariaDB 10.2.27](mariadb-10227-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10227-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10227-changelog.md) |
| 31 Jul 2019 | [MariaDB 10.2.26](mariadb-10226-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10226-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10226-changelog.md) |
| 17 Jun 2019 | [MariaDB 10.2.25](mariadb-10225-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10225-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10225-changelog.md) |
| 9 May 2019  | [MariaDB 10.2.24](mariadb-10224-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10224-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10224-changelog.md) |
| 25 Mar 2019 | [MariaDB 10.2.23](mariadb-10223-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10223-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10223-changelog.md) |
| 11 Feb 2019 | [MariaDB 10.2.22](mariadb-10222-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10222-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10222-changelog.md) |
| 2 Jan 2019  | [MariaDB 10.2.21](mariadb-10221-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10221-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10221-changelog.md) |
| 24 Dec 2018 | [MariaDB 10.2.20](mariadb-10220-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10220-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10220-changelog.md) |
| 19 Nov 2018 | [MariaDB 10.2.19](mariadb-10219-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10219-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10219-changelog.md) |
| 25 Sep 2018 | [MariaDB 10.2.18](mariadb-10218-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10218-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10218-changelog.md) |
| 14 Aug 2018 | [MariaDB 10.2.17](mariadb-10217-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10217-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10217-changelog.md) |
| 26 Jun 2018 | [MariaDB 10.2.16](mariadb-10216-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10216-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10216-changelog.md) |
| 17 May 2018 | [MariaDB 10.2.15](mariadb-10215-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10215-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10215-changelog.md) |
| 27 Mar 2018 | [MariaDB 10.2.14](mariadb-10214-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10214-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10214-changelog.md) |
| 13 Feb 2018 | [MariaDB 10.2.13](mariadb-10213-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10213-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10213-changelog.md) |
| 4 Jan 2018  | [MariaDB 10.2.12](mariadb-10212-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10212-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10212-changelog.md) |
| 28 Nov 2017 | [MariaDB 10.2.11](mariadb-10211-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10211-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10211-changelog.md) |
| 31 Oct 2017 | [MariaDB 10.2.10](mariadb-10210-release-notes.md)                                                                                                                         | Stable (GA) | [Release Notes](mariadb-10210-release-notes.md)                                                                                               | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10210-changelog.md) |
| 27 Sep 2017 | [MariaDB 10.2.9](mariadb-1029-release-notes.md)                                                                                                                           | Stable (GA) | [Release Notes](mariadb-1029-release-notes.md)                                                                                                | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1029-changelog.md)  |
| 18 Aug 2017 | [MariaDB 10.2.8](mariadb-1028-release-notes.md)                                                                                                                           | Stable (GA) | [Release Notes](mariadb-1028-release-notes.md)                                                                                                | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1028-changelog.md)  |
| 12 Jul 2017 | [MariaDB 10.2.7](mariadb-1027-release-notes.md)                                                                                                                           | Stable (GA) | [Release Notes](mariadb-1027-release-notes.md)                                                                                                | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1027-changelog.md)  |
| 23 May 2017 | [MariaDB 10.2.6](mariadb-1026-release-notes.md)                                                                                                                           | Stable (GA) | [Release Notes](mariadb-1026-release-notes.md)                                                                                                | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1026-changelog.md)  |
| 5 Apr 2017  | [MariaDB 10.2.5](mariadb-1025-release-notes.md)                                                                                                                           | RC          | [Release Notes](mariadb-1025-release-notes.md)                                                                                                | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1025-changelog.md)  |
| 17 Feb 2017 | [MariaDB 10.2.4](mariadb-1024-release-notes.md)                                                                                                                           | RC          | [Release Notes](mariadb-1024-release-notes.md)                                                                                                | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1024-changelog.md)  |
| 24 Dec 2016 | [MariaDB 10.2.3](mariadb-1023-release-notes.md)                                                                                                                           | Beta        | [Release Notes](mariadb-1023-release-notes.md)                                                                                                | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1023-changelog.md)  |
| 27 Sep 2016 | [MariaDB 10.2.2](mariadb-1022-release-notes.md)                                                                                                                           | Beta        | [Release Notes](mariadb-1022-release-notes.md)                                                                                                | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1022-changelog.md)  |
| 4 Jul 2016  | [MariaDB 10.2.1](mariadb-1021-release-notes.md)                                                                                                                           | Alpha       | [Release Notes](mariadb-1021-release-notes.md)                                                                                                | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1021-changelog.md)  |
| 18 Apr 2016 | [MariaDB 10.2.0](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1020-release-notes) | Alpha       | [Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series) | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1020-changelog.md)  |

## See Also

* [Getting, Installing, and Upgrading MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb)
* Plans for 10.x for features under consideration for features under consideration
* [10.2 Features/fixes by vote (JIRA)](https://jira.mariadb.org/issues/?jql=project%20%3D%20MDEV%20AND%20fixVersion%20%3D%2010.2%20ORDER%20BY%20votes%20DESC)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
