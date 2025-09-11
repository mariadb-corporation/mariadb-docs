# Release Notes for MariaDB Enterprise Server 10.5.4-2

This second release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-enterprise-server/README.md) 10.5 is the first GA (Generally Available) release. It Includes a variety of new features.

MariaDB Enterprise Server 10.5.4-2 was released on 2020-07-16.

#### Note

With MariaDB Enterprise Server 10.5 "mysql" command names are replaced with "mariadb" command names. Symbolic links are in place to maintain backward compatibility with the old names and prevent disruption. ([MDEV-21303](https://jira.mariadb.org/browse/MDEV-21303))

## Notable Changes

MariaDB Enterprise ColumnStore is a columnar storage engine for analytical workloads. MariaDB Enterprise ColumnStore 1.5.3 is included in this release. Specific details on this component may be found in the [Enterprise ColumnStore 1.5.3 release notes](../../../columnstore/old-releases/columnstore-1-5/mariadb-columnstore-1-5-3-release-notes.md).

## Changes in Storage Engines

* New in storage engine ColumnStore:
  * This release includes Enterprise [ColumnStore 1.5.3 release notes](../../../columnstore/old-releases/columnstore-1-5/mariadb-columnstore-1-5-3-release-notes.md).
  * Comprehensive rewrite of installation, cluster management, and failover logic
  * Support for standard MariaDB Server collations and character sets
* New in storage engine InnoDB:
  * Online resizing of the [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) redo log
  * [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) Buffer Pool optimizations ([MDEV-15058](https://jira.mariadb.org/browse/MDEV-15058))
  * Number of [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) purge threads can be changed at runtime
  * New thread pool implementation for [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) background tasks ([MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264))
  * Information Schema tables [THREAD\_POOL\_GROUPS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_groups-table), [THREAD\_POOL\_QUEUES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_queues-table), and [THREAD\_POOL\_STATS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_stats-table) added for insights into internals of the new [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) Thread Pool ([MDEV-19313](https://jira.mariadb.org/browse/MDEV-19313))
  * Status variables added for [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) storage engine parameters previously exposed only in `SHOW ENGINE INNODB STATUS` ([MDEV-18582](https://jira.mariadb.org/browse/MDEV-18582))
  * Improvements to Group Commit performance for [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) Redo Log ([MDEV-21534](https://jira.mariadb.org/browse/MDEV-21534))
  * [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) file format constraints to ALTER TABLE statements allow compatibility with older versions ([MDEV-20590](https://jira.mariadb.org/browse/MDEV-20590))
  * Improvements to [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) for [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) ([MDEV-8069](https://jira.mariadb.org/browse/MDEV-8069), [MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412), [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456))
  * [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) performance improvements ([MDEV-15053](https://jira.mariadb.org/browse/MDEV-15053), [MDEV-22593](https://jira.mariadb.org/browse/MDEV-22593), [MDEV-22697](https://jira.mariadb.org/browse/MDEV-22697), [MDEV-22871](https://jira.mariadb.org/browse/MDEV-22871), [MDEV-22841](https://jira.mariadb.org/browse/MDEV-22841))
* New in storage engine S3:
  * Enhancements to partition support
  * Replication support using shared or separate S3 storage backend for Primary and Secondary Node
* New in storage engine Spider:
  * This release includes Enterprise Spider 3.4, which adds support for an [ODBC foreign data wrapper](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/creating-a-data-source-with-mariadb-connectorodbc).
  * For ODBC Spider Tables, [Enterprise Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) uses the ODBC foreign data wrapper to read from and write to an ODBC Data Source.
  * The ODBC foreign data wrapper has beta maturity.
  * [information\_schema.SPIDER\_WRAPPER\_PROTOCOLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/information-schema-spider_wrapper_protocols-table) table added to provide information about supported foreign data wrappers

## SQL Level Enhancements

* MariaDB SQL statements support `REPLICA` a synonym for `SLAVE` ([MDEV-20601](https://jira.mariadb.org/browse/MDEV-20601))
* `RETURNING` clause can be used for `INSERT` and `REPLACE` statements to return a result set of the inserted rows or another specified SQL statement ([MDEV-10014](https://jira.mariadb.org/browse/MDEV-10014))
* `INTERSECT` and `EXCEPT` statements support ALL, so result sets can now include duplicate rows ([MDEV-18844](https://jira.mariadb.org/browse/MDEV-18844))
* Comments can be added for a database in the [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database) statement, formerly limited to field level ([MDEV-307](https://jira.mariadb.org/browse/MDEV-307))
* JSON function [JSON\_ARRAYAGG()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_arrayagg) can be used to create a JSON array from the values of a column ([MDEV-16620](https://jira.mariadb.org/browse/MDEV-16620))
* JSON function [JSON\_OBJECTAGG()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_objectagg) can be used to build an JSON object from the result set of a query ([MDEV-16620](https://jira.mariadb.org/browse/MDEV-16620))
* Support added for creating custom Data Types using the new Data Type API ([MDEV-274](https://jira.mariadb.org/browse/MDEV-274))
  * `INET` data type plugin added for storing IPv4 and IPv6 addresses
* `RENAME INDEX` and `RENAME KEY` can be used with [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) ([MDEV-7318](https://jira.mariadb.org/browse/MDEV-7318))
* `RENAME COLUMN` can now be used with [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) ([MDEV-16290](https://jira.mariadb.org/browse/MDEV-16290))
* Support added for recursive CTE cycle detection using the `CYCLE` clause ([MDEV-20632](https://jira.mariadb.org/browse/MDEV-20632))
* `IF EXIST` keywords are now supported in [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) and [RENAME TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/rename-table) statements
* Support added for `WITHOUT OVERLAPS` for Application-Time Period temporal tables ([MDEV-16978](https://jira.mariadb.org/browse/MDEV-16978))

## Replication and High Availability (HA)

* Replica aware server shutdown (MENT-731)
  * Primary only shuts down when replication transactions have been processed
  * Added the [shutdown\_wait\_for\_slaves](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables) system variable to control default behavior
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md) based on Galera 4.1
  * New non-blocking DDL mode: set [wsrep\_osu\_method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_osu_method) system variable to `NBO` to allow DDL to not block the whole cluster for ALTER TABLE statements, which use a lock mode `SHARED` or `EXCLUSIVE`
  * Galera Black Box as debug message storage for troubleshooting
  * A new inconsistency voting protocol in MariaDB Cluster can be used avoiding a full cluster shutdown while ensuring hardening the cluster against potential threats for data consistency ([MDEV-17048](https://jira.mariadb.org/browse/MDEV-17048))
  * Support added for Galera Global Transaction ID in MariaDB Cluster, which replicates MariaDB Global Transaction ID to other nodes in the cluster ([MDEV-20720](https://jira.mariadb.org/browse/MDEV-20720))
  * Support added for Non Blocking Operations method in [wsrep\_osu\_method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_osu_method) system variable ([MDEV-20051](https://jira.mariadb.org/browse/MDEV-20051))

## Privileges and Security Features

* Key Management plugin for HashiCorp Vault System
* System variable [require\_secure\_transport](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#require_secure_transport) for rejecting connections attempted using insecure transport ([MDEV-13662](https://jira.mariadb.org/browse/MDEV-13662))
* [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super) privilege split into several smaller privileges, allowing for more fine grained tuning of what each user can do: [BINLOG ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-admin), [BINLOG REPLAY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-replay), [CONNECTION ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#connection-admin), [FEDERATED ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#federated-admin), [READ\_ONLY ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#read_only-admin), [REPLICATION MASTER ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-master-admin), [REPLICATION SLAVE ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave), and [SET USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#SET-USER) ([MDEV-21743](https://jira.mariadb.org/browse/MDEV-21743))

## Optimizer Changes

* For filesort, the mode `addon_fields`, `addon_fields`, or `packed_addon_fields` used for sorting will be shown in `ANALYZE FORMAT=JSON` ([MDEV-21838](https://jira.mariadb.org/browse/MDEV-21838))
* Through enhancement to Query Optimizer, [ANALYZE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/ANALYZE/README.md) now shows the time spent for checking WHERE clauses and performing other auxiliary operations ([MDEV-20854](https://jira.mariadb.org/browse/MDEV-20854))
* Enhancement for the sort buffer to allow packed values of non-sorted fields in the sort buffer ([MDEV-21263](https://jira.mariadb.org/browse/MDEV-21263))
* Optimizer can now use packed sort keys in the sort buffer ([MDEV-21580](https://jira.mariadb.org/browse/MDEV-21580))

## Interface Changes

### Tools

* `aria_pack` supports transactional tables
* `aria_pack` now supports `--datadir`, `--ignore-control-file`, and `--require-control-file` options
* [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) now supports `--ignore-table-data` option ([MDEV-22037](https://jira.mariadb.org/browse/MDEV-22037))

### Privileges and Security

* [REPLICATION CLIENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-client) privilege renamed to [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#BINLOG-MONITOR), the old syntax still understood for compatibility ([MDEV-21743](https://jira.mariadb.org/browse/MDEV-21743))
* Several statements changed required privileges and may require a number of [GRANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) statements to be issued after upgrade:
  * [SHOW BINLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#show-binlog-events) now requires BINLOG MONITOR privilege, instead of [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave)
  * [SHOW SLAVE HOSTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#show-slave-hosts) now requires [REPLICATION SLAVE ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave-admin) or [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super) privileges, instead of [REPLICATION CLIENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-client) or [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super)
  * [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#show-slave-status) now requires [REPLICATION SLAVE ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave-admin) or [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super) privileges, instead of [REPLICATION CLIENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-client) or [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super)
  * [SHOW RELAYLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#show-relaylog-events) now requires [REPLICATION SLAVE ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave-admin) privilege, instead of [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave)

### New defaults

* Increased `gcache.size` option default in [wsrep\_provider\_options](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_provider_options) system variable to 1 GB via the MariaDB Enterprise Server config file
* Changed [innodb\_adaptive\_hash\_index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_adaptive_hash_index) system variable default to `OFF` ([MDEV-20487](https://jira.mariadb.org/browse/MDEV-20487))
* Changed [innodb\_checksum\_algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_checksum_algorithm) system variable default to `full_crc32` ([MDEV-19534](https://jira.mariadb.org/browse/MDEV-19534))
* Changed [innodb\_log\_files\_in\_group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_files_in_group) system variable default to `1` ([MDEV-20907](https://jira.mariadb.org/browse/MDEV-20907))
* Default for the [slave\_parallel\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) system variable changed to `optimistic` ([MDEV-18648](https://jira.mariadb.org/browse/MDEV-18648))

### Configuration Options

* Upgraded Performance Schema instrumentation and tables ([MDEV-6114](https://jira.mariadb.org/browse/MDEV-6114))
* Support added for `ENFORCE` option with `slave_run_triggers_for_rbr` system variable ([MDEV-21833](https://jira.mariadb.org/browse/MDEV-21833))
* Support added for `sql_if_exists` session system variable, which provides an implicit `IF EXISTS` to SQL statements altering, renaming, or dropping tables, views, functions, and packages ([MDEV-19964](https://jira.mariadb.org/browse/MDEV-19964))
* Column added to Information Schema `SYSTEM_VARIABLES` table showing the configuration file from which it received its value ([MDEV-12684](https://jira.mariadb.org/browse/MDEV-12684))
* Columns that indicate InnoDB Buffer Pool instance now return a value of 0 on the Information Schema `INNODB_BUFFER_PAGE`, `INNODB_BUFFER_PAGE_LRU`, `INNODB_BUFFER_POOL_STATS`, `INNODB_CMPMEM`, and `INNODB_CMPMEM_RESET` ([MDEV-15058](https://jira.mariadb.org/browse/MDEV-15058))
* `SHOW MASTER STATUS` statement renamed to `SHOW BINLOG STATUS`, the old syntax still understood for compatibility ([MDEV-21743](https://jira.mariadb.org/browse/MDEV-21743))
* [innodb\_encryption\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encryption_threads) now capped at `255` ([MDEV-22258](https://jira.mariadb.org/browse/MDEV-22258))
* Minimum value of `max_sort_length` raised to 8 (previously 4), so fixed size data types like `DOUBLE` and `BIGINT` are not truncated for lower values of `max_sort_length` ([MDEV-22715](https://jira.mariadb.org/browse/MDEV-22715))

Deprecated/Removed System Variables

* [innodb\_checksums](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_checksums) system variable removed ([MDEV-19534](https://jira.mariadb.org/browse/MDEV-19534))
* [innodb\_log\_checksums](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_checksums) system variable deprecated ([MDEV-19543](https://jira.mariadb.org/browse/MDEV-19543))
* [innodb\_locks\_unsafe\_for\_binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_locks_unsafe_for_binlog) system variable removed ([MDEV-19544](https://jira.mariadb.org/browse/MDEV-19544))
* [innodb\_stats\_sample\_pages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_stats_sample_pages) system variable removed ([MDEV-19551](https://jira.mariadb.org/browse/MDEV-19551))
* [innodb\_undo\_logs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_logs) system variable deprecated ([MDEV-19570](https://jira.mariadb.org/browse/MDEV-19570))
* [innodb\_rollback\_segments](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_rollback_segments) system variable removed ([MDEV-19570](https://jira.mariadb.org/browse/MDEV-19570))
* [innodb\_buffer\_pool\_instances](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_instances) system variable deprecated and ignored
* [innodb\_page\_cleaners](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_page_cleaners) system variable deprecated and ignored
* [innodb\_log\_optimize\_ddl](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_optimize_ddl) system variable deprecated and ignored ([MDEV-19747](https://jira.mariadb.org/browse/MDEV-19747))
* [multi\_range\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#multi_range_count) system variable deprecated and removed ([MDEV-18650](https://jira.mariadb.org/browse/MDEV-18650))
* [thread\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#thread_concurrency) system variable deprecated and removed ([MDEV-18650](https://jira.mariadb.org/browse/MDEV-18650))
* [timed\_mutexes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#timed_mutexes) system variable deprecated and removed ([MDEV-18650](https://jira.mariadb.org/browse/MDEV-18650))
* [innodb\_scrub\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_scrub_log) system variable deprecated and ignored ([MDEV-21870](https://jira.mariadb.org/browse/MDEV-21870))
* [innodb\_scrub\_log\_speed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_scrub_log_speed) system variable deprecated and ignored ([MDEV-21870](https://jira.mariadb.org/browse/MDEV-21870))
* [innodb\_background\_scrub\_data\_uncompressed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_uncompressed) system variable deprecated and ignored ([MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528))
* [innodb\_background\_scrub\_data\_compressed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_compressed) system variable deprecated and ignored ([MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528))
* [innodb\_background\_scrub\_data\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_interval) system variable deprecated and ignored ([MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528))
* [innodb\_background\_scrub\_data\_check\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_check_interval) system variable deprecated and ignored ([MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528))
* [innodb\_log\_files\_in\_group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_files_in_group) system variable deprecated and ignored ([MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425))

### Deprecated/Removed Information Schema

* Information Schema [INNODB\_TABLESPACES\_SCRUBBING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_scrubbing-table) table removed ([MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528))

### Aria Storage Engine

* Maximum key length for [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) storage engine increased from `1000` to `2000` bytes

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.5.4-2 is provided for:

* AlmaLinux 8 (x86\_64, ARM64)
* AlmaLinux 9 (x86\_64, ARM64)
* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

#### Note

MariaDB Enterprise Server 10.5 removes support for Red Hat Enterprise Linux (RHEL) 6 and CentOS 6.

## Installation Instructions

* [MariaDB Enterprise Server ](../../11.4/whats-new.md)[10](broken-reference)[.5](../../11.4/whats-new.md)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](broken-reference)[.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage) [and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore 23.02 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 23.02 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.5](broken-reference)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.5](broken-reference)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-from-to-specific-versions/upgrading-from-mariadb-10-5-to-mariadb-10-6)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
