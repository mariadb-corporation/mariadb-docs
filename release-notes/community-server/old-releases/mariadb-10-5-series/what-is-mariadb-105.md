# MariaDB 10.5 Changes & Improvements

MariaDB 10.5 is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

{% include "../../../.gitbook/includes/latest-10-5.md" %}

[MariaDB 10.5](what-is-mariadb-105.md) is a previous major release series. The first stable release was in June 2020, and it was [maintained until](https://mariadb.org/about/#maintenance-policy) June 2025.

## Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 10.4 to MariaDB 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5).

## Implemented Features

See the [Differences in MariaDB Enterprise Server 10.5](../../../enterprise-server/about/mariadb-enterprise-server-differences/differences-in-mariadb-enterprise-server-10.5.md) page for items that are different between MariaDB Community Server 10.5 and MariaDB Enterprise Server 10.5.

### ColumnStore

* This release of MariaDB Server includes the [MariaDB ColumnStore](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) storage engine. Note, that plugins have [independent maturity levels](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema) and MariaDB ColumnStore in 10.5.4 has Beta maturity.

### Binaries Named mariadb (mysql Symlinked)

* All binaries previously beginning with `mysql` now begin with `mariadb`, with symlinks for the corresponding `mysql` command. ([MDEV-21303](https://jira.mariadb.org/browse/MDEV-21303))
* When starting the MariaDB server via the systemd service it will be started using the `mariadbd` binary name, so this will now show up in the system process list instead of `mysqld`
* Same for the `mariadbd-safe` wrapper script. Even when called via the `mysqld_safe` symlink, it will start the actual server process as `mariadbd`, not `mysqld` now. This also affects startup via system service init scripts on platforms that don't yet have switched to SystemD

### INET 6 Data Type

* New [INET6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/inet6) data type for storing IPv6 addresses ([MDEV-274](https://jira.mariadb.org/browse/MDEV-274))

### Amazon S3

* The [S3 storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine) allows one to archive MariaDB tables in Amazon S3, or any third-party public or private cloud that implements S3 API ( [MDEV-22606](https://jira.mariadb.org/browse/MDEV-22606))
* Both S3 tables and [partitioned](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/partitioning-tables) S3 tables are discoverable. This means that if you create a partitioned S3 table, both the partitioned table and its partitions can be directly used by another server that has access to the S3 storage. ([MDEV-22088](https://jira.mariadb.org/browse/MDEV-22088))

### Privileges Made More Granular

* Split SUPER [privilege](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) to smaller privileges ([MDEV-21743](https://jira.mariadb.org/browse/MDEV-21743)). New privileges were added so that more fine grained tuning of what each user can do can be applied:
  * [BINLOG ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-admin)
  * [BINLOG REPLAY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-replay)
  * [CONNECTION ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#connection-admin)
  * [FEDERATED ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#federated-admin)
  * [READ\_ONLY ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#read_only-admin)
  * [REPLICATION MASTER ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-master-admin)
  * [REPLICATION SLAVE ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave-admin)
  * [SET USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#set-user)
* The [REPLICATION CLIENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-client) privilege was renamed to [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-monitor). The old syntax is understood for compatibility ([MDEV-21743](https://jira.mariadb.org/browse/MDEV-21743)).
* The [SHOW MASTER STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statement was renamed to [SHOW BINLOG STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) ([MDEV-21743](https://jira.mariadb.org/browse/MDEV-21743)). The old syntax is understood for compatibility.
* A number of statements changed the privileges that they require. The old privileges were historically inappropriately chosen in the upstream. 10.5.2 fixes this problem. Note, these changes are incompatible to previous versions. A number of GRANT commands might be needed after upgrade.
  * [SHOW BINLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) now requires the [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-monitor) privilege (required [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave) prior to 10.5.2).
  * [SHOW SLAVE HOSTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-hosts) now requires the [REPLICATION MASTER ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-master-admin) privilege (required [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave) prior to 10.5.2).
  * [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status) now requires the [REPLICATION SLAVE ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave-admin) or the [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super) privilege (required [REPLICATION CLIENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-client) or [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super) prior to 10.5.2).
  * [SHOW RELAYLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-relaylog-events) now requires the [REPLICATION SLAVE ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave-admin) privilege (required [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave) prior to 10.5.2).
* In order to help the server understand which version a privilege record was written by, the [mysql.global\_priv.priv](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-global_priv-table) field contains a new JSON field, `version_id` ([MDEV-21704](https://jira.mariadb.org/browse/MDEV-21704))
* [SHOW PRIVILEGES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-privileges) now correctly lists the `Delete history` privilege, rather than displaying it as `Delete versioning rows`. ([MDEV-20382](https://jira.mariadb.org/browse/MDEV-20382))

### InnoDB: Performance Improvements etc.

* Extend [SHOW STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-status) LIKE 'Innodb\_%' ([MDEV-18582](https://jira.mariadb.org/browse/MDEV-18582))
* Clean up [INFORMATION\_SCHEMA.INNODB\_](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables) tables ([MDEV-19940](https://jira.mariadb.org/browse/MDEV-19940))
* Doublewrite buffer is unnecessarily used for newly (re)initialized pages ([MDEV-19738](https://jira.mariadb.org/browse/MDEV-19738))
* Defer change buffer merge until pages are requested ([MDEV-19514](https://jira.mariadb.org/browse/MDEV-19514))
* Remove dummy tablespace for the [redo log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-redo-log) ([MDEV-18115](https://jira.mariadb.org/browse/MDEV-18115))
* Optimize access to InnoDB page header fields ([MDEV-21133](https://jira.mariadb.org/browse/MDEV-21133))
* Remove multiple [InnoDB buffer pool](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-buffer-pool) instances ([MDEV-15058](https://jira.mariadb.org/browse/MDEV-15058))
  * Columns that indicated the buffer pool instance from the Information Schema [innodb\_buffer\_page](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_buffer_page-table), [innodb\_buffer\_page\_lru](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_buffer_page_lru-table), [innodb\_buffer\_pool\_stats](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_buffer_pool_stats-table), [innodb\_cmpmem](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_cmpmem-and-innodb_cmpmem_reset-tables) and [innodb\_cmpmem\_reset](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_cmpmem-and-innodb_cmpmem_reset-tables) tables now return a dummy value of `0`.
* Remove buf\_page\_t::newest\_modification ([MDEV-21132](https://jira.mariadb.org/browse/MDEV-21132))
* Replace recv\_sys\_t::addr\_hash with a std::map ([MDEV-19586](https://jira.mariadb.org/browse/MDEV-19586))
* Obsolete internal parser for FK in InnoDB ([MDEV-20480](https://jira.mariadb.org/browse/MDEV-20480))
* InnoDB thread pool for background tasks ([MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264))
* An upgrade will only be possible after a clean shutdown. mariadb-backup --prepare will not work with backups taken before version 10.5.2.
* Efficient InnoDB redo log record format ([MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353))
* Improve InnoDB redo log group commit performance ([MDEV-21534](https://jira.mariadb.org/browse/MDEV-21534))
* Do not acquire InnoDB record locks when covering table locks exist ([MDEV-14479](https://jira.mariadb.org/browse/MDEV-14479))
* Issue a message on changing deprecated innodb\_log\_files\_in\_group ([MDEV-21990](https://jira.mariadb.org/browse/MDEV-21990))
* Optimize append only files for NVDIMM ([MDEV-17084](https://jira.mariadb.org/browse/MDEV-17084))
* Avoid writing freed InnoDB pages ([MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528))

#### InnoDB New Defaults for Variables

* [innodb\_adaptive\_hash\_index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_adaptive_hash_index) now defaults to `OFF` ([MDEV-20487](https://jira.mariadb.org/browse/MDEV-20487))
* [innodb\_checksum\_algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_checksum_algorithm) now defaults to `full_crc32` ([MDEV-19534](https://jira.mariadb.org/browse/MDEV-19534))

#### InnoDB Removed or Deprecated Variables

* [innodb\_buffer\_pool\_instances](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_instances)
* [innodb\_checksums](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_checksums) ([MDEV-19534](https://jira.mariadb.org/browse/MDEV-19534))
* [innodb\_locks\_unsafe\_for\_binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_locks_unsafe_for_binlog) ([MDEV-19544](https://jira.mariadb.org/browse/MDEV-19544))
* [innodb\_log\_checksums](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_checksums) ([MDEV-19543](https://jira.mariadb.org/browse/MDEV-19543))
* [innodb\_log\_files\_in\_group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_files_in_group) ([MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425) & [MDEV-20907](https://jira.mariadb.org/browse/MDEV-20907))
* [innodb\_log\_optimize\_ddl](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_page_cleaners) ([MDEV-19747](https://jira.mariadb.org/browse/MDEV-19747))
* [innodb\_rollback\_segments](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_rollback_segments) ([MDEV-19570](https://jira.mariadb.org/browse/MDEV-19570))
* [innodb\_scrub\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_scrub_log) and [innodb\_scrub\_log\_speed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_scrub_log_speed) ([MDEV-21870](https://jira.mariadb.org/browse/MDEV-21870))
* Remove [INFORMATION\_SCHEMA.INNODB\_TABLESPACES\_SCRUBBING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_scrubbing-table) table and deprecate and ignore:
* [innodb-background-scrub-data-uncompressed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_uncompressed)
* [innodb-background-scrub-data-compressed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_compressed)
* [innodb-background-scrub-data-interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_interval)
* [innodb-background-scrub-data-check-interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_check_interval) ([MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528))
* [innodb\_stats\_sample\_pages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_stats_sample_pages) ([MDEV-19551](https://jira.mariadb.org/browse/MDEV-19551))
* [innodb\_undo\_logs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_logs) ([MDEV-19570](https://jira.mariadb.org/browse/MDEV-19570))
* [innodb\_thread\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_thread_concurrency)
* [innodb\_commit\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_commit_concurrency)
* [innodb\_replication\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_replication_delay)
* [innodb\_concurrency\_tickets](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_concurrency_tickets)
* [innodb\_thread\_sleep\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_thread_sleep_delay)
* [innodb\_adaptive\_max\_sleep\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_adaptive_max_sleep_delay) ([MDEV-23379](https://jira.mariadb.org/browse/MDEV-23379))

### Performance Schema Updates to Match MySQL 5.7 Instrumentation and Tables

* Memory ([MDEV-16431](https://jira.mariadb.org/browse/MDEV-16431))
* Meta data locking (MDL) ([MDEV-16432](https://jira.mariadb.org/browse/MDEV-16432))
* Prepared statements (ps) ([MDEV-16433](https://jira.mariadb.org/browse/MDEV-16433))
* \[show] status instrumentation and tables ([MDEV-16438](https://jira.mariadb.org/browse/MDEV-16438))
* Stored procedures ([MDEV-16434](https://jira.mariadb.org/browse/MDEV-16434))
* Sxlocks ([MDEV-16436](https://jira.mariadb.org/browse/MDEV-16436))
* Transactions ([MDEV-16435](https://jira.mariadb.org/browse/MDEV-16435))
* User variables ([MDEV-16439](https://jira.mariadb.org/browse/MDEV-16439))

### Galera: Full GTID Support

* Add full [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) support to [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) cluster ([commit](https://github.com/MariaDB/server/commit/41bc736871)). With this feature all nodes in a cluster\
  will have the same GTID for replicated events originating from the cluster. Also added a new variable, `wsrep_gtid_seq_no`, to manually update the WSREP GTID sequence number in the cluster (similar to how the `gtid_seq_no` variable is used for non-WSREP transactions).
* Add new mode to wsrep\_OSU\_method in which Galera checks storage engine of the affected table ([MDEV-20051](https://jira.mariadb.org/browse/MDEV-20051))
* Galera: Replicate MariaDB GTID to other nodes in the cluster ([MDEV-20720](https://jira.mariadb.org/browse/MDEV-20720))

### Binary Log and Replication: More Metadata

* [slave\_parallel\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#slave_parallel_mode) now defaults to `optimistic` ([MDEV-18648](https://jira.mariadb.org/browse/MDEV-18648)).
* Make REPLICA a synonym for [SLAVE in SQL statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements) ([MDEV-20601](https://jira.mariadb.org/browse/MDEV-20601))
* `ENFORCE` option for [slave\_run\_triggers\_for\_rbr](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#slave_run_triggers_for_rbr) ([MDEV-21833](https://jira.mariadb.org/browse/MDEV-21833))
* Extended [binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) metadata ([MDEV-20477](https://jira.mariadb.org/browse/MDEV-20477)) to include new fields. This was done to solve replication issues when the Master and Slave table had different definitions for a column which could lead to data loss ([MDEV-19708](https://jira.mariadb.org/browse/MDEV-19708)). It also enables us to do better replication with pluggable data types in the future.
  * The new metadata fields are:
    * Signedness of Numeric Columns
    * Character Set of Character Columns and Binary Columns
    * Column Name
    * String Value of SET Columns
    * String Value of ENUM Columns
    * Primary Key
    * Character Set of SET Columns and ENUM Columns
    * Geometry Type
  * Also added a new global variable, [binlog\_row\_metadata](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_row_metadata) to control the amount of metadata logged. Possible values are:
    * `FULL` - all metadata is logged
    * `MINIMAL` - only metadata required by a worker is logged
    * `NO_LOG` - No metadata is logged (default)
* Binary log DDL entries can now be marked that they should be ignored if the target table doesn't exist (implicit `IF EXISTS`).
* [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) output is extended to show all replication flags. Example of output: `SET @@session.foreign_key_checks=1, @@session.sql_auto_is_null=0, @@session.unique_checks=1, @@session.autocommit=1, @@session.check_constraint_checks=1, @@session.sql_if_exists=0/*!*/`.
* [SHOW BINLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) and [SHOW RELAYLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-relaylog-events) are extended to show replication flags.

### Syntax

* [INSERT ... RETURNING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insertreturning) ([MDEV-10014](https://jira.mariadb.org/browse/MDEV-10014)) - returns SELECT of inserted rows (analogous to [DELETE ... RETURNING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete))
* [REPLACE ... RETURNING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/replacereturning) ([MDEV-10014](https://jira.mariadb.org/browse/MDEV-10014))
* [EXCEPT ALL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations/except#alldistinct) and [INTERSECT ALL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations/intersect#alldistinct) ([MDEV-18844](https://jira.mariadb.org/browse/MDEV-18844))
* Application period tables: [WITHOUT OVERLAPS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/application-time-periods#without-overlaps) ([MDEV-16978](https://jira.mariadb.org/browse/MDEV-16978))
* Setup [default partitions for system versioning](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables#default-partitions) ([MDEV-19903](https://jira.mariadb.org/browse/MDEV-19903))
* Database comments in [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database) and [ALTER DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-database) statements ([MDEV-307](https://jira.mariadb.org/browse/MDEV-307))
* [ALTER TABLE ... RENAME INDEX / KEY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#rename-indexkey) ([MDEV-7318](https://jira.mariadb.org/browse/MDEV-7318))
* [ALTER TABLE ... RENAME COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#rename-column) ([MDEV-16290](https://jira.mariadb.org/browse/MDEV-16290))
* [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) and [RENAME TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/rename-table) now support `IF EXISTS`.
* Add [VISIBLE attribute for indexes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table#visible-index-option) in CREATE TABLE ([MDEV-22199](https://jira.mariadb.org/browse/MDEV-22199))
* Recursive [CTE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions) cycle detection using CYCLE clause ([MDEV-20632](https://jira.mariadb.org/browse/MDEV-20632))
* [RELEASE\_ALL\_LOCKS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/release_all_locks) hold by [GET\_LOCK()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/get_lock) ([MDEV-10569](https://jira.mariadb.org/browse/MDEV-10569))
* Fix [REFERENCES constraint](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys) in column definition ([MDEV-20729](https://jira.mariadb.org/browse/MDEV-20729))

### JSON

* Added [JSON\_ARRAYAGG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_arrayagg). This returns a JSON array containing an element for each value in a given set of JSON or SQL values. It acts on a column or an expression that evaluates to a single value.
* Added [JSON\_OBJECTAGG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_objectagg). This returns a JSON object containing key-value pairs. It takes two expressions that evaluate to a single value, or two column names, as arguments, the first used as a key, and the second as a value.

### Thread Pool

* Information Schema tables ([THREAD\_POOL\_GROUPS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_groups-table), [THREAD\_POOL\_QUEUES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_queues-table), [THREAD\_POOL\_STATS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_stats-table) and [THREAD\_POOL\_WAITS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_waits-table)) for internals of generic thread\_pool ([MDEV-19313](https://jira.mariadb.org/browse/MDEV-19313)).

### Performance Improvements

* Speed up binary row logging code
* Range optimizer speedups. Removed double calls to records\_in\_range() for some cases.
* Costs for using MEMORY tables updated to be more accurate
* Fixed that 'ref' access is preferred over 'range' for the same index.
* Improve connect speed (up to 25%). ([MDEV-19515](https://jira.mariadb.org/browse/MDEV-19515))

#### Query Optimizer

* Improve Protocol performance for numeric data by avoiding unnecessary character string conversions ([MDEV-23162](https://jira.mariadb.org/browse/MDEV-23162), [MDEV-23478](https://jira.mariadb.org/browse/MDEV-23478))
* [ANALYZE for statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-statement) is improved, now it also shows the time spent checking the WHERE clause and doing other auxiliary operations ([MDEV-20854](https://jira.mariadb.org/browse/MDEV-20854))
* [Inferred IS NOT NULL predicates can be used by the range optimizer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/not_null_range_scan-optimization) ([MDEV-15777](https://jira.mariadb.org/browse/MDEV-15777))
* Allow packed sort keys and values of non-sorted fields in the sort buffer ([MDEV-21263](https://jira.mariadb.org/browse/MDEV-21263) & [MDEV-21580](https://jira.mariadb.org/browse/MDEV-21580))
  * Makes filesort temporary files much smaller when [VARCHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/varchar), [CHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/char) or [BLOBs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/blob) are used!

### General

* The [Information Schema SYSTEM\_VARIABLES Table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-system_variables-table) has a new column showing from which config file a variable derives its value ([MDEV-12684](https://jira.mariadb.org/browse/MDEV-12684))
* Switch Perl DBI scripts from DBD::mysql to DBD::MariaDB driver ([MDEV-19755](https://jira.mariadb.org/browse/MDEV-19755))
* The [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) max key length is now 2000 bytes, compared to 1000 bytes in [MyISAM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myisam-storage-engine).
* [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) now reliably deletes table remnants inside a storage engine even if the .frm file is missing ([MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412))
* Accelerated crc32() function for AMD64, ARMv8, POWER 8 ([MDEV-22669](https://jira.mariadb.org/browse/MDEV-22669))
* Binary tarball size has been reduced ([MDEV-21943](https://jira.mariadb.org/browse/MDEV-21943))

### PCRE (Perl Compatible Regular Expressions)

* Migrate to [PCRE2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) ([MDEV-14024](https://jira.mariadb.org/browse/MDEV-14024)), a newer version of the pcre library.

### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-10-5) and [Status Variables Added in MariaDB 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/status-variables-added-in-mariadb-105).
* The [Information Schema SYSTEM\_VARIABLES Table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-system_variables-table) has a new column showing from which config file a variable derives its value ([MDEV-12684](https://jira.mariadb.org/browse/MDEV-12684)).
* Port [show\_old\_temporals](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#show_old_temporals) from MySQL 5.6 ([MDEV-19906](https://jira.mariadb.org/browse/MDEV-19906)). If set, old temporal data types (created with a pre-10.0 version of MariaDB) are displayed with a /\* mariadb-5.3 \*/ comment.
* Numerous deprecated variables removed ([MDEV-18650](https://jira.mariadb.org/browse/MDEV-18650))
  * [multi\_range\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#multi_range_count)
  * [thread\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#thread_concurrency)
  * [timed\_mutexes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#timed_mutexes)

## Security Vulnerabilities Fixed in [MariaDB 10.5](what-is-mariadb-105.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2025-21490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21490): [MariaDB 10.5.28](mariadb-10-5-28-release-notes.md)
* [CVE-2024-21096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21096): [MariaDB 10.5.25](mariadb-10-5-25-release-notes.md)
* [CVE-2023-5157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5157): [MariaDB 10.5.17](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series/broken-reference/README.md)
* [CVE-2023-22084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22084): [MariaDB 10.5.23](mariadb-10-5-23-release-notes.md)
* [CVE-2022-47015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47015): [MariaDB 10.5.20](mariadb-10-5-20-release-notes.md)
* [CVE-2022-38791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38791): [MariaDB 10.5.17](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series/broken-reference/README.md)
* [CVE-2022-32091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32091): [MariaDB 10.5.17](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series/broken-reference/README.md)
* [CVE-2022-32089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32089): [MariaDB 10.5.17](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series/broken-reference/README.md)
* [CVE-2022-32088](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32088): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-32087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32087): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-32086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32086): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-32085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32085): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-32084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32084): [MariaDB 10.5.17](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series/broken-reference/README.md)
* [CVE-2022-32083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32083): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-32082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32082): [MariaDB 10.5.17](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series/broken-reference/README.md)
* [CVE-2022-32081](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32081): [MariaDB 10.5.17](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series/broken-reference/README.md)
* [CVE-2022-31624](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31624): [MariaDB 10.5.13](mariadb-10513-release-notes.md)
* [CVE-2022-27458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27458): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27457](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27457): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27456): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27455): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27452](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27452): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27451): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27449): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27448](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27448): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27447](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27447): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27446): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27445](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27445): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27444): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27387): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27386): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27385): [MariaDB 10.5.13](mariadb-10513-release-notes.md)
* [CVE-2022-27384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27384): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27383](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27383): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27382](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27382): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27381](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27381): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27380): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27379): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27378): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27377](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27377): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-27376](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27376): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2022-24052](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24052): [MariaDB 10.5.14](mariadb-10514-release-notes.md)
* [CVE-2022-24051](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24051): [MariaDB 10.5.14](mariadb-10514-release-notes.md)
* [CVE-2022-24050](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24050): [MariaDB 10.5.14](mariadb-10514-release-notes.md)
* [CVE-2022-24048](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24048): [MariaDB 10.5.14](mariadb-10514-release-notes.md)
* [CVE-2022-21595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21595): [MariaDB 10.5.14](mariadb-10514-release-notes.md)
* [CVE-2022-21451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21451): [MariaDB 10.5.10](mariadb-10510-release-notes.md)
* [CVE-2022-21427](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21427): [MariaDB 10.5.7](mariadb-1057-release-notes.md)
* [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778): [MariaDB 10.5.14](mariadb-10514-release-notes.md)
* [CVE-2021-46669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46669): [MariaDB 10.5.16](mariadb-10516-release-notes.md)
* [CVE-2021-46668](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46668): [MariaDB 10.5.15](mariadb-10515-release-notes.md)
* [CVE-2021-46667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46667): [MariaDB 10.5.13](mariadb-10513-release-notes.md)
* [CVE-2021-46666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46666): [MariaDB 10.5.11](mariadb-10511-release-notes.md)
* [CVE-2021-46665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46665): [MariaDB 10.5.15](mariadb-10515-release-notes.md)
* [CVE-2021-46664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46664): [MariaDB 10.5.15](mariadb-10515-release-notes.md)
* [CVE-2021-46663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46663): [MariaDB 10.5.15](mariadb-10515-release-notes.md)
* [CVE-2021-46662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46662): [MariaDB 10.5.13](mariadb-10513-release-notes.md)
* [CVE-2021-46661](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46661): [MariaDB 10.5.15](mariadb-10515-release-notes.md)
* [CVE-2021-46659](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46659): [MariaDB 10.5.14](mariadb-10514-release-notes.md)
* [CVE-2021-46658](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46658): [MariaDB 10.5.12](mariadb-10512-release-notes.md)
* [CVE-2021-46657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46657): [MariaDB 10.5.11](mariadb-10511-release-notes.md)
* [CVE-2021-35604](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35604): [MariaDB 10.5.13](mariadb-10513-release-notes.md)
* [CVE-2021-27928](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27928): [MariaDB 10.5.9](mariadb-1059-release-notes.md)
* [CVE-2021-2389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2389): [MariaDB 10.5.12](mariadb-10512-release-notes.md)
* [CVE-2021-2372](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2372): [MariaDB 10.5.12](mariadb-10512-release-notes.md)
* [CVE-2021-2194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2194): [MariaDB 10.5.7](mariadb-1057-release-notes.md)
* [CVE-2021-2166](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2166): [MariaDB 10.5.10](mariadb-10510-release-notes.md)
* [CVE-2021-2154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2154): [MariaDB 10.5.10](mariadb-10510-release-notes.md)
* [CVE-2021-2022](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2022): [MariaDB 10.5.5](mariadb-1055-release-notes.md)
* [CVE-2020-28912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28912): [MariaDB 10.5.7](mariadb-1057-release-notes.md)
* [CVE-2020-15180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15180): [MariaDB 10.5.6](mariadb-1056-release-notes.md)
* [CVE-2020-14812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14812): [MariaDB 10.5.7](mariadb-1057-release-notes.md)
* [CVE-2020-14789](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14789): [MariaDB 10.5.7](mariadb-1057-release-notes.md)
* [CVE-2020-14776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14776): [MariaDB 10.5.7](mariadb-1057-release-notes.md)
* [CVE-2020-14765](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14765): [MariaDB 10.5.7](mariadb-1057-release-notes.md)
* [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032): [MariaDB 10.5.17](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series/broken-reference/README.md)

## Resources

* [10.5 and beyond](https://www.youtube.com/watch?v=NG_ClRXdofE) (video presentation by Sergei Golubchik)

## List of All [MariaDB 10.5](what-is-mariadb-105.md) Releases

| Date        | Release                                             | Status      | Release Notes                                     | Changelog                                                                                |
| ----------- | --------------------------------------------------- | ----------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| 8 May 2025  | [MariaDB 10.5.29](mariadb-10-5-29-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-5-29-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-29-changelog.md) |
| 4 Feb 2025  | [MariaDB 10.5.28](mariadb-10-5-28-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-5-28-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-28-changelog.md) |
| 1 Nov 2024  | [MariaDB 10.5.27](mariadb-10-5-27-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-5-27-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-27-changelog.md) |
| 8 Aug 2024  | [MariaDB 10.5.26](mariadb-10-5-26-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-5-26-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-26-changelog.md) |
| 16 May 2024 | [MariaDB 10.5.25](mariadb-10-5-25-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-5-25-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-25-changelog.md) |
| 7 Feb 2024  | [MariaDB 10.5.24](mariadb-10-5-24-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-5-24-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-24-changelog.md) |
| 13 Nov 2023 | [MariaDB 10.5.23](mariadb-10-5-23-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-5-23-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-23-changelog.md) |
| 14 Aug 2023 | [MariaDB 10.5.22](mariadb-10-5-22-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-5-22-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-22-changelog.md) |
| 7 Jun 2023  | [MariaDB 10.5.21](mariadb-10-5-21-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-5-21-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-21-changelog.md) |
| 10 May 2023 | [MariaDB 10.5.20](mariadb-10-5-20-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-5-20-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-20-changelog.md) |
| 6 Feb 2023  | [MariaDB 10.5.19](mariadb-10-5-19-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-5-19-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-19-changelog.md) |
| 7 Nov 2022  | [MariaDB 10.5.18](mariadb-10-5-18-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-5-18-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-18-changelog.md) |
| 15 Aug 2022 | [MariaDB 10.5.17](mariadb-10517-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10517-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10517-changelog.md)   |
| 20 May 2022 | [MariaDB 10.5.16](mariadb-10516-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10516-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10516-changelog.md)   |
| 12 Feb 2022 | [MariaDB 10.5.15](mariadb-10515-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10515-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10515-changelog.md)   |
| 9 Feb 2022  | [MariaDB 10.5.14](mariadb-10514-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10514-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10514-changelog.md)   |
| 8 Nov 2021  | [MariaDB 10.5.13](mariadb-10513-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10513-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10513-changelog.md)   |
| 6 Aug 2021  | [MariaDB 10.5.12](mariadb-10512-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10512-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10512-changelog.md)   |
| 23 Jun 2021 | [MariaDB 10.5.11](mariadb-10511-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10511-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10511-changelog.md)   |
| 7 May 2021  | [MariaDB 10.5.10](mariadb-10510-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10510-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10510-changelog.md)   |
| 22 Feb 2021 | [MariaDB 10.5.9](mariadb-1059-release-notes.md)     | Stable (GA) | [Release Notes](mariadb-1059-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1059-changelog.md)    |
| 11 Nov 2020 | [MariaDB 10.5.8](mariadb-1058-release-notes.md)     | Stable (GA) | [Release Notes](mariadb-1058-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1058-changelog.md)    |
| 3 Nov 2020  | [MariaDB 10.5.7](mariadb-1057-release-notes.md)     | Stable (GA) | [Release Notes](mariadb-1057-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1057-changelog.md)    |
| 7 Oct 2020  | [MariaDB 10.5.6](mariadb-1056-release-notes.md)     | Stable (GA) | [Release Notes](mariadb-1056-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1056-changelog.md)    |
| 10 Aug 2020 | [MariaDB 10.5.5](mariadb-1055-release-notes.md)     | Stable (GA) | [Release Notes](mariadb-1055-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1055-changelog.md)    |
| 24 Jun 2020 | [MariaDB 10.5.4](mariadb-1054-release-notes.md)     | Stable (GA) | [Release Notes](mariadb-1054-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1054-changelog.md)    |
| 12 May 2020 | [MariaDB 10.5.3](mariadb-1053-release-notes.md)     | RC          | [Release Notes](mariadb-1053-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1053-changelog.md)    |
| 26 Mar 2020 | [MariaDB 10.5.2](mariadb-1052-release-notes.md)     | Beta        | [Release Notes](mariadb-1052-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1052-changelog.md)    |
| 14 Feb 2020 | [MariaDB 10.5.1](mariadb-1051-release-notes.md)     | Beta        | [Release Notes](mariadb-1051-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1051-changelog.md)    |
| 3 Dec 2019  | [MariaDB 10.5.0](mariadb-1050-release-notes.md)     | Alpha       | [Release Notes](mariadb-1050-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1050-changelog.md)    |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
