# MariaDB 11.4 Changes & Improvements

{% include "../../.gitbook/includes/latest-11-4.md" %}

[MariaDB 11.4](what-is-mariadb-114.md) is a current long-term series, maintained until May 2029.

### Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 10.11 to MariaDB 11.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-from-mariadb-10-11-to-mariadb-11-4).

### New Features

This list includes all features since the previous long-term release, [MariaDB 10.11](../10.11/what-is-mariadb-1011.md) (those introduced in the [MariaDB 11.0](../old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110.md), [MariaDB 11.1](../old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111.md) and [MariaDB 11.2](../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md) short-term releases, and the [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md) rolling release).

#### Optimizer

* Major improvements to the Optimizer. See [The Optimizer Cost Model from MariaDB 11.0](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/the-optimizer-cost-model-from-mariadb-11-0).
* [Semi-join optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/semi-join-subquery-optimizations) for single-table [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update)/[DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) statements. Update and delete statements that use subqueries can now use all subquery optimization strategies that MariaDB offers, so now if you use subqueries in UPDATE or DELETE, these statements will likely be much faster ([MDEV-7487](https://jira.mariadb.org/browse/MDEV-7487), [MariaDB 11.1](../old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111.md))
* Queries with the [DATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/date-function) or [YEAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/year) functions comparing against a constant can now make use of indexes, so these will be noticeably quicker in certain instances. For example `SELECT * FROM t2 WHERE YEAR(a) = 2019` or `SELECT * FROM t2 WHERE DATE(a) <= '2017-01-01'`. See [Sargable DATE and YEAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/sargable-date-and-year) ([MDEV-8320](https://jira.mariadb.org/browse/MDEV-8320), [MariaDB 11.1](../old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111.md))
* Queries like [UCASE(varchar\_col)=...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/upper) can now use an index on `varchar_col` if its collation is case insensitive. An [optimizer\_switch](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizer-switch) option, [sargable\_casefold=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/sargable-upper), has been added to enable this optimization. ([MDEV-31496](https://jira.mariadb.org/browse/MDEV-31496), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))
* Not only ascending, but also [descending indexes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table#index-types) can now be used to optimize [MIN()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/min) and [MAX()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/max) ([MDEV-27576](https://jira.mariadb.org/browse/MDEV-27576))

#### InnoDB

* Shrink [temporary tablespaces](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-tablespaces/innodb-temporary-tablespaces) without restart by setting the [innodb\_truncate\_temporary\_tablespace\_now](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_truncate_temporary_tablespace_now) system variable. ([MDEV-28699](https://jira.mariadb.org/browse/MDEV-28699), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))
* The [InnoDB system tablespace](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces) is now shrunk by reclaiming unused space at startup ([MDEV-14795](https://jira.mariadb.org/browse/MDEV-14795), [MariaDB 11.2](../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md))

#### Online Schema Change

* [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) can now do most operations with `ALGORITHM=COPY, LOCK=NONE`, that is, in most cases, unless the algorithm and lock level are explicitly specified, `ALTER TABLE` will be performed using the [COPY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#algorithmcopy) algorithm while simultaneously allowing concurrent [DML statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation) on the altered table. ([MariaDB 11.2](../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md))

For more information, refer to, [Online Schema Change](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table/online-schema-change).

#### Replication and Binary Log

* [Binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) writing speed was improved by moving checksum calculations out of the global binlog mutex ([MDEV-31273](https://jira.mariadb.org/browse/MDEV-31273)). The [binlog\_legacy\_event\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_legacy_event_pos) system variable is available if the old behavior is desired. This is a contribution by Kristian Nielsen
* New system variable [max\_binlog\_total\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#max_binlog_total_size) enables binary log purging when the total size of all binary logs exceeds the specified threshold. The implementation is based on the patch from Percona ([MDEV-31404](https://jira.mariadb.org/browse/MDEV-31404))
* New system variable [slave\_connections\_needed\_for\_purge](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#slave_connections_needed_for_purge) disables binary log purging until the number of connected slaves reaches the specified threshold ([MDEV-31404](https://jira.mariadb.org/browse/MDEV-31404)).
* `FULL_NODUP` is a new value for the [binlog\_row\_image](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_row_image) system variable. It essentially works like `FULL`, that is all columns are included in the event, but it takes less space, because the after image omits columns that were not changed by the `UPDATE` statement, and have same values as in the before image. This is a contribution from Alibaba ([MDEV-32589](https://jira.mariadb.org/browse/MDEV-32589))
* [mariadb-binlog --flashback](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/flashback) support for the [FULL\_NODUP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_row_image) mode. This is a contribution from Alibaba ([MDEV-32894](https://jira.mariadb.org/browse/MDEV-32894)).
* MariaDB can optionally maintain a [special index of GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#binlog-indexing) and their location in the binary log. If enabled (the default), it allows finding very quickly where a new connecting replica should start replicating from. Without an index, this required scanning the binlog. This is a contribution by Kristian Nielsen ([MDEV-4991](https://jira.mariadb.org/browse/MDEV-4991)).
* Add keywords "SQL\_BEFORE\_GTIDS" and "SQL\_AFTER\_GTIDS" for [START SLAVE UNTIL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#sql_before_gtidssql_after_gtids) ([MDEV-27247](https://jira.mariadb.org/browse/MDEV-27247), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md)).\
  SQL\_BEFORE\_GTIDS stops the replica when it sees gtids of the option's argument list, without executing them. ([MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))
* All binlog\* variables are now visible as system variables, specifically [binlog\_do\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_do_db), [binlog\_ignore\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_ignore_db), [binlog\_row\_event\_max\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_row_event_max_size) ([MDEV-30188](https://jira.mariadb.org/browse/MDEV-30188), [MariaDB 11.2](../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md))

#### SSL/TLS

* [SSL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption) is now enabled in the server by default. No configuration necessary, if no server certificate was provided a self-signed certificate will be automatically generated by the server. See [Mission Impossible: Zero-Configuration SSL](https://mariadb.org/mission-impossible-zero-configuration-ssl/) for details ([MDEV-31856](https://jira.mariadb.org/browse/MDEV-31856)).
* Clients now can validate self-signed server certificates if the [mysql\_native\_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-mysql_native_password) or [ed25519](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-ed25519) authentication is used and account password is not empty ([MDEV-31855](https://jira.mariadb.org/browse/MDEV-31855)).
* Clients now require SSL and have [--ssl-verify-server-cert](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#-ssl-verify-server-cert) enabled by default ([MDEV-31857](https://jira.mariadb.org/browse/MDEV-31857)).
* Replication clients do that too, [MASTER\_SSL\_VERIFY\_SERVER\_CERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to#master_ssl_verify_server_cert) is enabled by default.
* Use `--disable-ssl` or `--disable-ssl-verify-server-cert` to revert to the old behavior.
* Clients can use new command line options [--ssl-fp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#-ssl-fpname) and [--ssl-fplist](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#-ssl-fplistname) to verify the server certificate by its fingerprint

#### JSON

* [JSON\_TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_table) now allows retrieval of the key when iterating on JSON objects ([MDEV-30145](https://jira.mariadb.org/browse/MDEV-30145), [MariaDB 11.2](../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md))
* New functions [JSON\_OBJECT\_FILTER\_KEYS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_object_filter_keys), [JSON\_OBJECT\_TO\_ARRAY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_object_to_array) and [JSON\_ARRAY\_INTERSECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_array_intersect) to check for JSON intersection ([MDEV-26182](https://jira.mariadb.org/browse/MDEV-26182), [MariaDB 11.2](../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md))
* [JSON\_KEY\_VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_key_value) extracts key/value pairs from a JSON object ([MDEV-30145](https://jira.mariadb.org/browse/MDEV-30145), [MariaDB 11.2](../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md))
* [JSON\_SCHEMA\_VALID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_schema_valid) function for validating a JSON schema ([MDEV-27128](https://jira.mariadb.org/browse/MDEV-27128), [MariaDB 11.1](../old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111.md))

#### Data Types

* It is now possible to create [partitions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/partitioning-tables) on tables that contain [GEOMETRY types](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry/geometry-types) ([MDEV-19177](https://jira.mariadb.org/browse/MDEV-19177), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))
* [INET4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/inet4) data types can now be cast into [INET6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/inet6) types ([MDEV-31626](https://jira.mariadb.org/browse/MDEV-31626), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))
* This means INET4 values can be compared with INET6 values and can be inserted into INET6 columns;\
  the server can automatically convert INET4 value into INET6 as needed ([MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))

#### Backup and Restore

* New [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) option, `-j`, `--parallel=` for increased parallelism, specifies the number of dump table jobs executed in parallel (only for use with the `--tab` option). Also added to [mariadb-import](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-import), with `--use-threads` as a synonym. ([MDEV-32216](https://jira.mariadb.org/browse/MDEV-32216))
* [mariadb-backup --innobackupex](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#innobackupex) mode has been deprecated ([MDEV-31505](https://jira.mariadb.org/browse/MDEV-31505), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))
* Rename [mariadb-backup’s](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup) xtrabackup\_\* files to mariadb\_backup\_\* ([MDEV-18931](https://jira.mariadb.org/browse/MDEV-18931), [MariaDB 11.1](../old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111.md))

#### Application-Time Periods

* Add views for [periods](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/application-time-periods) in information\_schema ([MDEV-22597](https://jira.mariadb.org/browse/MDEV-22597)), in particular
* New view [INFORMATION\_SCHEMA.PERIODS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-periods-table)
* New view [INFORMATION\_SCHEMA.KEY\_PERIOD\_USAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-key_period_usage-table)
* New columns `IS_SYSTEM_TIME_PERIOD_START` and `IS_SYSTEM_TIME_PERIOD_END` in the [INFORMATION\_SCHEMA.COLUMNS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-columns-table) view

#### Sys Schema

* New view [sys.privileges\_by\_table\_by\_level](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/sys-schema/sys-schema-views/privileges_by_table_by_level-sys-schema-view) shows granted privileges broken down by table on which they allow access and level on which they were granted. For example, if a user `x` has `SELECT` privilege granted `ON db.*`, this view will list all tables in the `db` schema with the user `x` having `SELECT` privilege on them. This is different from [INFORMATION\_SCHEMA.TABLE\_PRIVILEGES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-table_privileges-table), which only lists privileges granted on the table level ([MDEV-24486](https://jira.mariadb.org/browse/MDEV-24486))

#### Partitioning

* [ALTER TABLE … EXCHANGE PARTITION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/partitioning-tables/partitioning-overview#exchanging-partitions) and [ALTER TABLE … CONVERT TABLE … TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/partitioning-tables/partitioning-overview#converting-partitions-to-from-tables) now support the `WITH VALIDATION` and `WITHOUT VALIDATION` clauses. If neither is specified, the default behavior is `WITH VALIDATION` ([MDEV-22164](https://jira.mariadb.org/browse/MDEV-22164))

#### Collations

From [MariaDB 11.4.5](11.4.5.md):

* 44 new [collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations#collations) added. These are aliases for MySQL collations to make it easier to replicate from MySQL to MariaDB ([MDEV-35256](https://jira.mariadb.org/browse/MDEV-35256))
  * The [Information Schema Collations table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-collations-table) includes a new column, `COMMENT` which contains information about which collation the alias refers to.

#### Connection Redirection

* Added a [redirect mechanism](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/connection-redirection-mechanism-in-the-mariadb-clientserver-protocol) using the [redirect\_url](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#redirect_url) system variable ([MDEV-15935](https://jira.mariadb.org/browse/MDEV-15935), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))
* At the moment client-side support is missing

#### Privileges

* Add a new database-level [privilege](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant), `SHOW CREATE ROUTINE` that allows one to see the routine definition even if the user isn't the routine owner ([MDEV-29167](https://jira.mariadb.org/browse/MDEV-29167), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))

#### Spider

* The preferred way to specify [Spider parameters](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-table-parameters) is to use the dedicated Spider table options (implemented in [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md)). Abusing the table `COMMENT` clause is now deprecated ([MDEV-28861](https://jira.mariadb.org/browse/MDEV-28861))
* The [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) storage engine now supports table options instead of having to encode them in COMMENT/CONNECTION strings. When any table option is specified, Spider will ignore COMMENT/CONNECTION strings at the same table/partition/subpartition. A new variable [spider\_ignore\_comments](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables#spider_ignore_comments) is introduced to ignore them globally at all levels (table/partition/subpartition). Another variable, [spider\_suppress\_comment\_ignored\_warning](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables#spider_suppress_comment_ignored_warning), is introduced to suppress warnings when Spider ignores COMMENT/CONNECTION strings. ([MDEV-28856](https://jira.mariadb.org/browse/MDEV-28856), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))

#### Miscellaneous Functions

* [CONV()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/conv) function now supports conversion up to base 62 ([MDEV-30879](https://jira.mariadb.org/browse/MDEV-30879))
* Values generated by the Key Derivation Function [KDF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/kdf) are resistant against password hashing generators, so are good for strongly hashed passwords ([MDEV-31474](https://jira.mariadb.org/browse/MDEV-31474))
* Given a time in picoseconds, the new function [FORMAT\_PICO\_TIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/format_pico_time) returns a human-readable time value and unit indicator ([MDEV-19629](https://jira.mariadb.org/browse/MDEV-19629), [MariaDB 11.0](../old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110.md))

#### Date and Time

* [DATE\_FORMAT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/date_format) function can now print the current time zone abbreviation and current time zone offset from UTC with `%Z` and `%z` format specifiers. ([MDEV-31684](https://jira.mariadb.org/browse/MDEV-31684), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))

#### Processlist

* Added a `SENT_ROWS` column to the [Information Schema PROCESSLIST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-processlist-table) table, as well as extended the display size for the columns in processlist to ensure\
  that most results will fit in display ([MDEV-3953](https://jira.mariadb.org/browse/MDEV-3953), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))

#### Miscellaneous

* Added support for packages ([CREATE PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-package)) outside of [ORACLE sql\_mode](../about/compatibility-and-differences/sql_modeoracle.md) ([MDEV-32101](https://jira.mariadb.org/browse/MDEV-32101))
* Setting a non-default [old\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/old-mode) value will now always issue a deprecation warning ([MDEV-31811](https://jira.mariadb.org/browse/MDEV-31811), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))
* [ALTER TABLE IMPORT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) enhancement ([MDEV-26137](https://jira.mariadb.org/browse/MDEV-26137), [MariaDB 11.2](../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md))
* Temporary tables are now displayed in the [Information Schema TABLES Table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-tables-table), [SHOW TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-tables) and [SHOW TABLE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-table-status) ([MDEV-12459](https://jira.mariadb.org/browse/MDEV-12459), [MariaDB 11.2](../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md))
* [Stored programs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines): validation of stored program statements ([MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816), [MariaDB 11.2](../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md))
* Extend [AES\_ENCRYPT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_encrypt) and [AES\_DECRYPT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_decrypt) to support an initialization vector and algorithm ([MDEV-9069](https://jira.mariadb.org/browse/MDEV-9069), [MariaDB 11.2](../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md))
* The [transaction\_isolation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#transaction_isolation) option is now a system variable, and the tx\_isolation system variable is deprecated ([MDEV-21921](https://jira.mariadb.org/browse/MDEV-21921), [MariaDB 11.1](../old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111.md))

#### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 11.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-variables-added-in-mariadb-11-4).

**Removed**

* Remove thr\_alarm from server codebase
  * Includes removal of the [debug\_no\_thread\_alarm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#debug_no_thread_alarm) system variable ([MDEV-32567](https://jira.mariadb.org/browse/MDEV-32567))
* In addition, the following deprecated features and system variables have been removed ([MDEV-32104](https://jira.mariadb.org/browse/MDEV-32104), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md)):
  * sr\_YU [locale](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale) (deprecated since [MariaDB 10.0.11](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-11-4-series/broken-reference/README.md))
  * "engine\_condition\_pushdown" in [optimizer\_switch](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizer-switch) (deprecated since [MariaDB 10.1.1](../old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes.md))
  * [date\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#date_format), [datetime\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datetime_format), [time\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#time_format), [max\_tmp\_tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_tmp_tables) (deprecated since [MariaDB 10.1.2](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-11-4-series/broken-reference/README.md))
  * [wsrep\_causal\_reads](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_causal_reads) (deprecated since [MariaDB 10.1.3](../old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes.md))
  * "parser" in [mroonga](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/mroonga) table comment (deprecated since [MariaDB 10.2.11](../old-releases/release-notes-mariadb-10-2-series/mariadb-10211-release-notes.md))
  * [old\_alter\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#old_alter_table) variable ([MDEV-30905](https://jira.mariadb.org/browse/MDEV-30905), [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))
  * [innodb\_defragment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_defragment) and related parameters ([MDEV-30545](https://jira.mariadb.org/browse/MDEV-30545), [MariaDB 11.1](../old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111.md))
  * The [InnoDB Change Buffer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-change-buffering) has been removed ([MDEV-29694](https://jira.mariadb.org/browse/MDEV-29694), [MariaDB 11.0](../old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110.md))

### Security Vulnerabilities Fixed in [MariaDB 11.4](what-is-mariadb-114.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2025-21490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21490): [MariaDB 11.4.5](11.4.5.md)
* [CVE-2024-21096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21096): [MariaDB 11.4.2](11.4.2.md)

### List of All [MariaDB 11.4](what-is-mariadb-114.md) Releases

| Date        | Release        | Status      | Release Notes              | Changelog                                 |
| ----------- | -------------- | ----------- | -------------------------- | ----------------------------------------- |
| 6 Nov 2025  | MariaDB 11.4.9 | Stable (GA) | [Release Notes](11.4.9.md) | [Changelog](../changelogs/11.4/11.4.9.md) |
| 6 Aug 2025  | MariaDB 11.4.8 | Stable (GA) | [Release Notes](11.4.8.md) | [Changelog](../changelogs/11.4/11.4.8.md) |
| 22 May 2025 | MariaDB 11.4.7 | Stable (GA) | [Release Notes](11.4.7.md) | [Changelog](../changelogs/11.4/11.4.7.md) |
| 6 May 2025  | MariaDB 11.4.6 | Stable (GA) | [Release Notes](11.4.6.md) | [Changelog](../changelogs/11.4/11.4.6.md) |
| 4 Feb 2025  | MariaDB 11.4.5 | Stable (GA) | [Release Notes](11.4.5.md) | [Changelog](../changelogs/11.4/11.4.5.md) |
| 1 Nov 2024  | MariaDB 11.4.4 | Stable (GA) | [Release Notes](11.4.4.md) | [Changelog](../changelogs/11.4/11.4.4.md) |
| 8 Aug 2024  | MariaDB 11.4.3 | Stable (GA) | [Release Notes](11.4.3.md) | [Changelog](../changelogs/11.4/11.4.3.md) |
| 29 May 2024 | MariaDB 11.4.2 | Stable (GA) | [Release Notes](11.4.2.md) | [Changelog](../changelogs/11.4/11.4.2.md) |
| 16 Feb 2024 | MariaDB 11.4.1 | RC          | [Release Notes](11.4.1.md) | [Changelog](../changelogs/11.4/11.4.1.md) |
| 24 Dec 2023 | MariaDB 11.4.0 | Alpha       | [Release Notes](11.4.0.md) |                                           |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
