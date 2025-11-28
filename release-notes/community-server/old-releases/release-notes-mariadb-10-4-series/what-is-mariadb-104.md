# MariaDB 10.4 Changes & Improvements

[MariaDB 10.4](what-is-mariadb-104.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

The most recent release of [MariaDB 10.4](what-is-mariadb-104.md) is:[**MariaDB 10.4.34**](mariadb-10-4-34-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[MariaDB 10.4](what-is-mariadb-104.md) is a previous major stable version. The first stable release of 10.4 was in June 2019, and it was [maintained until](https://mariadb.org/about/#maintenance-policy) June 2024.

## Implemented Features

See the [Differences in MariaDB Enterprise Server 10.4](../../../enterprise-server/mariadb-enterprise-server-differences/differences-in-mariadb-enterprise-server-10-4.md) page for items that are different between MariaDB Community Server 10.4 and MariaDB Enterprise Server 10.4.

### Authentication

* See [Authentication from MariaDB 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/user-account-management/authentication-from-mariadb-10-4) for an overview of the changes.
* The [unix\_socket authentication plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) is now default on Unix-like systems, which is a major change to authentication in MariaDB ([MDEV-12484](https://jira.mariadb.org/browse/MDEV-12484))
* [User password expiry](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/user-account-management/user-password-expiry) ([MDEV-7597](https://jira.mariadb.org/browse/MDEV-7597))
* [Account Locking](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/user-account-management/account-locking) ([MDEV-13095](https://jira.mariadb.org/browse/MDEV-13095))
* The obsolete [mysql.host table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/obsolete-mysql-database-tables/mysql-host-table) is no longer created ([MDEV-15851](https://jira.mariadb.org/browse/MDEV-15851))
* Much faster privilege checks for MariaDB setups with many user accounts or many database grants ([MDEV-15649](https://jira.mariadb.org/browse/MDEV-15649))
* [mysql.user](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-user-table) table is retired. User accounts and global privileges are now stored in the [mysql.global\_priv](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-global_priv-table) table ([MDEV-17658](https://jira.mariadb.org/browse/MDEV-17658))
* [SET PASSWORD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/set-password) support for [ed25519](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-ed25519) and other [authentication plugins](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins) ([MDEV-12321](https://jira.mariadb.org/browse/MDEV-12321))

### InnoDB

* Added instant [DROP COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#drop-column) and changing of the order of columns ([MDEV-15562](https://jira.mariadb.org/browse/MDEV-15562))
* More Instant VARCHAR extension or ROW\_FORMAT=DYNAMIC and ROW\_FORMAT=COMPACT ([MDEV-15563](https://jira.mariadb.org/browse/MDEV-15563))
  * change CHAR(0) to any VARCHAR
  * change a CHAR that is longer than 255 bytes to VARCHAR or wider CHAR
  * change a VARCHAR that is shorter than 128 bytes into any longer VARCHAR
* Instant collation or charset changes for non-indexed columns ([MDEV-15564](https://jira.mariadb.org/browse/MDEV-15564))
* Reduced redo log volume for undo tablespace initialization ([MDEV-17138](https://jira.mariadb.org/browse/MDEV-17138))
* Removed crash-upgrade support for pre-10.2.19 TRUNCATE TABLE ([MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564))
* Added key rotation for [innodb\_encrypt\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encrypt_log) ([MDEV-12041](https://jira.mariadb.org/browse/MDEV-12041))
* Implement [innodb\_checksum\_algorithm=full\_crc32](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_checksum_algorithm) ([MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026))

### Optimizer

* Implementation of the [optimizer trace](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/mariadb-internals-documentation-optimizer-trace/optimizer-trace-overview), one can enable the optimizer trace by enabling the system variable [optimizer\_trace](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_trace) ([MDEV-6111](https://jira.mariadb.org/browse/MDEV-6111))
* [Engine Independent Table Statistics](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics) is now enabled by default; new default values are [use\_stat\_tables=PREFERABLY\_FOR\_QUERIES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#use_stat_tables) and [optimizer\_use\_condition\_selectivity=4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_use_condition_selectivity) ([MDEV-15253](https://jira.mariadb.org/browse/MDEV-15253))
  * Two new values for the variable [use\_stat\_tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#use_stat_tables): `COMPLEMENTARY_FOR_QUERIES` and `PREFERABLY_FOR_QUERIES` ([MDEV-17255](https://jira.mariadb.org/browse/MDEV-17255))
  * [Histograms](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics) are now used (but not collected) by default ([MDEV-18608](https://jira.mariadb.org/browse/MDEV-18608)).
  * [analyze\_sample\_percentage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#analyze_sample_percentage) variable added. The default value is 100 (`ANALYZE` will use the whole table), but one can also set analyze to only use a sample of table data to collect the statistics.
* Condition pushdown optimization now has bigger scope:
  * [Conditions can be pushed into materialized IN-subqueries](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/condition-pushdown-into-in-subqueries) ([MDEV-12387](https://jira.mariadb.org/browse/MDEV-12387))
  * Conditions in `HAVING` clause can be pushed to WHERE. This behavior is controlled through [optimizer switch](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizer-switch) flag `condition_pushdown_from_having`.
* The [optimizer switch](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizer-switch) flag `optimize_join_buffer_size` now defaults to `on` ([MDEV-17903](https://jira.mariadb.org/browse/MDEV-17903))
* [Rowid Filtering optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/rowid-filtering-optimization) added ([MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188)). It is controlled through [optimizer switch](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizer-switch) flag `rowid_filter` .

### Syntax

* [Temporal tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables) extended with support for [application-time periods](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/application-time-periods) ([MDEV-16973](https://jira.mariadb.org/browse/MDEV-16973), [MDEV-16974](https://jira.mariadb.org/browse/MDEV-16974), [MDEV-16975](https://jira.mariadb.org/browse/MDEV-16975), [MDEV-17082](https://jira.mariadb.org/browse/MDEV-17082))
* Support of brackets (parentheses) for specifying precedence in [UNION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/union)/[EXCEPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/except)/[INTERSECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/intersect) operations ([MDEV-11953](https://jira.mariadb.org/browse/MDEV-11953))
* New [FLUSH SSL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) command to reload SSL certificates without server restart ([MDEV-16266](https://jira.mariadb.org/browse/MDEV-16266))
* New `CAST` target — `CAST(x AS INTERVAL DAY_SECOND(N))` ([MDEV-17776](https://jira.mariadb.org/browse/MDEV-17776))
* `IF NOT EXISTS` clause added to [INSTALL PLUGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin) and `IF EXISTS` clause added to [UNINSTALL PLUGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin) and [UNINSTALL SONAME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname) ([MDEV-16294](https://jira.mariadb.org/browse/MDEV-16294))
* Unique indexes can be created on [BLOB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/blob) or [TEXT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/text) fields ([MDEV-371](https://jira.mariadb.org/browse/MDEV-371))

### Variables

For a list of all new variables, see [System Variables Added in MariaDB 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-10-4) and [Status Variables Added in MariaDB 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/status-variables-added-in-mariadb-104).

* Added to the [tcp\_nodelay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tcp_nodelay) system variable ([MDEV-16277](https://jira.mariadb.org/browse/MDEV-16277))
* Removed the [Innodb\_pages0\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables) status variable ([MDEV-15705](https://jira.mariadb.org/browse/MDEV-15705)).
* New [sql-mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) setting, `TIME_ROUND_FRACTIONAL` ([MDEV-16991](https://jira.mariadb.org/browse/MDEV-16991))
* New variable [gtid\_cleanup\_batch\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_cleanup_batch_size) for determining how many old rows must accumulate in the [mysql.gtid\_slave\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table) table before a background job will be run to delete them.
* The default for [eq\_range\_index\_dive\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#eq_range_index_dive_limit) is now `200` (previously `0`) ([MDEV-18551](https://jira.mariadb.org/browse/MDEV-18551))
* [core\_file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#core_file) on Windows now defaults to `ON` ([MDEV-18439](https://jira.mariadb.org/browse/MDEV-18439))

### Replication

* Speed up rotation of binary logs, `SHOW BINARY LOGS` etc with optimizing binary log index file locking ([MDEV-19116](https://jira.mariadb.org/browse/MDEV-19116), [MDEV-19117](https://jira.mariadb.org/browse/MDEV-19117)).
* A new server command, [SHUTDOWN WAIT FOR ALL SLAVES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/shutdown), and a new [mysqladmin shutdown --wait-for-all-slaves](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqladmin#options) option, are added to instruct the server to wait for the last binlog event to be sent to all connected slaves before shutting down. ([MDEV-18450](https://jira.mariadb.org/browse/MDEV-18450)).

### Backup

* [BACKUP STAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/backup-commands/backup-stage) allows one to implement very efficient backups with minimal locking. [MDEV-5336](https://jira.mariadb.org/browse/MDEV-5336).

### Galera 4

In [MariaDB 10.4.2](mariadb-1042-release-notes.md) and later, [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) has been upgraded from Galera 3 to Galera 4.

#### Galera 4 Versions

The following table lists each version of the [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) 4 wsrep provider, and it lists which version of MariaDB each one was first released in. If you would like to install [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) 4 using [yum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum), [apt](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files#installing-mariadb-with-apt), or [zypper](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper), then the package is called `galera-4`.

| Galera Version | Released in MariaDB Version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 26.4.21        | [11.8.1](../../11.8/11.8.1.md), [11.7.2](../mariadb-11-7-rolling-releases/mariadb-11-7-2-release-notes.md), [11.4.5](../../11.4/11.4.5.md),[10.11.11](../../10.11/10.11.11.md), [10.6.21](../../10.6/10.6.21.md), [10.5.28](../mariadb-10-5-series/mariadb-10-5-28-release-notes.md)                                                                                                                                                                                                                                    |
| 26.4.20        | [11.7.1](../mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes.md), [11.6.2](../release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md), [11.4.4](../../11.4/11.4.4.md), [11.2.6](../release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md), [10.11.10](../../10.11/10.11.10.md), [10.6.20](../../10.6/10.6.20.md), [10.5.27](../mariadb-10-5-series/mariadb-10-5-27-release-notes.md)                                                                                         |
| 26.4.19        | [11.4.3](../../11.4/11.4.3.md), [11.2.5](../release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes.md), [11.1.6](../release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes.md), [10.11.9](../../10.11/10.11.9.md), [10.6.19](../../10.6/10.6.19.md), [10.5.26](../mariadb-10-5-series/mariadb-10-5-26-release-notes.md)                                                                                                                                                                                 |
| 26.4.18        | [11.2.4](../release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes.md), [11.1.5](../release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes.md), [11.0.6](../release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes.md), [10.11.8](../../10.11/10.11.8.md), [10.6.18](../../10.6/10.6.18.md), [10.5.25](../mariadb-10-5-series/mariadb-10-5-25-release-notes.md), [10.4.34](mariadb-10-4-34-release-notes.md)                                                                                    |
| 26.4.16        | [11.2.2](../release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md), [11.1.3](../release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md), [11.0.4](../release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [10.11.6](../../10.11/10.11.6.md), [10.10.7](../release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes.md), [10.6.16](../../10.6/10.6.16.md), [10.5.23](../mariadb-10-5-series/mariadb-10-5-23-release-notes.md), [10.4.32](mariadb-10-4-32-release-notes.md) |
| 26.4.14        | [10.10.3](../release-notes-mariadb-10-10-series/mariadb-10-10-3-release-notes.md), [10.9.5](../release-notes-mariadb-10-9-series/mariadb-10-9-5-release-notes.md), [10.8.7](../release-notes-mariadb-10-8-series/mariadb-10-8-7-release-notes.md), [10.7.8](../release-notes-mariadb-10-7-series/mariadb-10-7-8-release-notes.md), [10.6.12](../../10.6/10.6.12.md), [10.5.19](../mariadb-10-5-series/mariadb-10-5-19-release-notes.md), [10.4.28](mariadb-10-4-28-release-notes.md)                                    |
| 26.4.13        | [10.10.2](../release-notes-mariadb-10-10-series/mariadb-10-10-2-release-notes.md), [10.9.4](../release-notes-mariadb-10-9-series/mariadb-10-9-4-release-notes.md), [10.8.6](../release-notes-mariadb-10-8-series/mariadb-10-8-6-release-notes.md), [10.7.7](../release-notes-mariadb-10-7-series/mariadb-10-7-7-release-notes.md), [10.6.11](../../10.6/10.6.11.md), [10.5.18](../mariadb-10-5-series/mariadb-10-5-18-release-notes.md), [10.4.27](mariadb-10-4-27-release-notes.md)                                    |
| 26.4.12        | [10.10.1](../release-notes-mariadb-10-10-series/mariadb-10101-release-notes.md), [10.9.2](../release-notes-mariadb-10-9-series/mariadb-1092-release-notes.md), [10.8.4](../release-notes-mariadb-10-8-series/mariadb-1084-release-notes.md), [10.7.5](../release-notes-mariadb-10-7-series/mariadb-1075-release-notes.md), [10.6.9](../../10.6/10.6.9.md), [10.5.17](../mariadb-10-5-series/mariadb-10517-release-notes.md), [10.4.26](mariadb-10426-release-notes.md)                                                  |
| 26.4.11        | [10.8.1](../release-notes-mariadb-10-8-series/mariadb-1081-release-notes.md), [10.7.2](../release-notes-mariadb-10-7-series/mariadb-1072-release-notes.md), [10.6.6](../../10.6/10.6.6.md), [10.5.14](../mariadb-10-5-series/mariadb-10514-release-notes.md), [10.4.22](mariadb-10422-release-notes.md)                                                                                                                                                                                                                 |
| 26.4.9         | [10.6.4](../../10.6/10.6.4.md), [10.5.12](../mariadb-10-5-series/mariadb-10512-release-notes.md), [10.4.21](mariadb-10421-release-notes.md)                                                                                                                                                                                                                                                                                                                                                                             |
| 26.4.8         | [10.6.1](../../10.6/10.6.1.md), [10.5.10](../mariadb-10-5-series/mariadb-10510-release-notes.md), [10.4.19](mariadb-10419-release-notes.md)                                                                                                                                                                                                                                                                                                                                                                             |
| 26.4.7         | [10.5.9](../mariadb-10-5-series/mariadb-1059-release-notes.md), [10.4.18](mariadb-10418-release-notes.md)                                                                                                                                                                                                                                                                                                                                                                                                               |
| 26.4.6         | [10.5.7](../mariadb-10-5-series/mariadb-1057-release-notes.md), [10.4.16](mariadb-10416-release-notes.md)                                                                                                                                                                                                                                                                                                                                                                                                               |
| 26.4.5         | [10.5.4](../mariadb-10-5-series/mariadb-1054-release-notes.md), [10.4.14](mariadb-10414-release-notes.md)                                                                                                                                                                                                                                                                                                                                                                                                               |
| 26.4.4         | [10.5.1](../mariadb-10-5-series/mariadb-1051-release-notes.md), [10.4.13](mariadb-10413-release-notes.md)                                                                                                                                                                                                                                                                                                                                                                                                               |
| 26.4.3         | [10.5.0](../mariadb-10-5-series/mariadb-1050-release-notes.md), [10.4.9](mariadb-1049-release-notes.md)                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 26.4.2         | [10.4.4](mariadb-1044-release-notes.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 26.4.1         | [10.4.3](mariadb-1043-release-notes.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 26.4.0         | [10.4.2](mariadb-1042-release-notes.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

#### New Features in Galera 4

The [mysql](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/) database contains new tables related to Galera replication:

* `wsrep_cluster`
* `wsrep_cluster_members`
* `wsrep_streaming_log`

End users may read but not modify these tables.

The new streaming replication feature allows replicating transactions of\
unlimited size. With streaming replication, a cluster is replicating a\
transaction in small fragments during transaction execution. This transaction\
fragmenting is controlled by two new configuration variables:

* [wsrep\_trx\_fragment\_unit](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_trx_fragment_unit) (bytes, rows, statements) defines the metrics for\
  how to measure transaction size limit for fragmenting. Possible values are:
  * `bytes`: transaction’s binlog events buffer size in bytes
  * `rows`: number of rows affected by the transaction
  * `statements`: number of SQL statements executed in the multi-statement\
    transaction
* [wsrep\_trx\_fragment\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_trx_fragment_size) defines the limit for fragmenting. When a\
  transaction’s size, in terms of the configured fragment unit, has grown over\
  this limit, a new fragment will be replicated.

Transactions replicated through galera replication will now process the commit\
phase using MariaDB's group commit logic. This will affect transaction\
throughput, especially when binary logging is enabled in the cluster.

#### Limitations in Galera 4

**Rolling Upgrades from Galera 3 to Galera 4**

Rolling upgrades from [MariaDB 10.3](../release-notes-mariadb-10-3-series/what-is-mariadb-103.md) (or earlier) to [MariaDB 10.4](what-is-mariadb-104.md) also require an upgrade from [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) 3 to [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) 4. Galera 4 has a lot of changes and improvements that were not present in Galera 3.

Prior to the General Availability (GA) releases of [MariaDB 10.4](what-is-mariadb-104.md) and Galera 4, earlier versions of [MariaDB 10.4](what-is-mariadb-104.md) and Galera 4 had bugs that could lead to problems if Galera 4 nodes were in a cluster with Galera 3 nodes during a rolling upgrade. In these versions, rolling upgrades were not supported. This meant that, in order to upgrade a cluster, the cluster had to be completely stopped, and the nodes could only be restarted after the entire cluster had been upgraded to [MariaDB 10.4](what-is-mariadb-104.md) and Galera 4.

These bugs have been fixed in more recent versions, and rolling upgrades from Galera 3 to Galera 4 are supported. In order to perform a rolling upgrade, it is recommended to upgrade to [MariaDB 10.4.6](mariadb-1046-release-notes.md) or later and Galera 26.4.2 or later. However, as a general rule, users should try to ensure that they are upgrading to the latest versions of [MariaDB 10.4](what-is-mariadb-104.md) and Galera 4.

For more detailed information on how to upgrade, see [Upgrading from MariaDB 10.3 to MariaDB 10.4 with Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster/upgrading-from-mariadb-10-3-to-mariadb-10-4-with-galera-cluster).

### General

* Crash safe [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria)-based [system tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables) ([MDEV-16421](https://jira.mariadb.org/browse/MDEV-16421))
* Added Linux abstract socket support ([MDEV-15655](https://jira.mariadb.org/browse/MDEV-15655))
* Enabled C++11 ([MDEV-16410](https://jira.mariadb.org/browse/MDEV-16410))
* Performance improvements in [Unicode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/unicode) collations ([MDEV-17534](https://jira.mariadb.org/browse/MDEV-17534), [MDEV-17511](https://jira.mariadb.org/browse/MDEV-17511), [MDEV-17502](https://jira.mariadb.org/browse/MDEV-17502), [MDEV-17474](https://jira.mariadb.org/browse/MDEV-17474))
* User data type plugins ([MDEV-4912](https://jira.mariadb.org/browse/MDEV-4912), in progress)
* Improvements with SQL standard INTERVAL support to help functions [TIMESTAMP()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/timestamp)\
  and [ADDTIME()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/addtime) return more predictable results.
  * Historically, MariaDB uses the TIME data type for both "time of the day"\
    values and "duration" values. In the first meaning the natural value range\
    is from '00:00:00' to '23:59:59.999999', in the second meaning the range is\
    from '-838:59:59.999999' to '+838:59:59.999999'.
  * To remove this ambiguity and for the SQL standard conformance we plan to\
    introduce a dedicated data type INTERVAL that will be able to store values\
    in the range at least from '-87649415:59:59.999999' to\
    '+87649415:59:59.999999', which will be enough to represent the time\
    difference between TIMESTAMP'0001-01-01 00:00:00' and TIMESTAMP'9999-12-31\
    23:59:59.999999'.
  * As a first step we support this range of values for intermediate\
    calculations when TIME-alike string and numeric values are used in INTERVAL\
    (i.e. duration) context, e.g. as the second argument of SQL functions\
    TIMESTAMP(ts,interval) and ADDTIME(ts,interval), so the following can now be\
    calculated:

```sql
SELECT ADDTIME(TIMESTAMP'0001-01-01 00:00:00', '87649415:59:59.999999');
-> '9999-12-31 23:59:59.999999'  

SELECT TIMESTAMP(DATE'0001-01-01', '87649415:59:59.999999')
-> '9999-12-31 23:59:59.999999'  

SELECT ADDTIME(TIME'-838:59:59.999999', '1677:59:59.999998');
-> '838:59:59.999999'
```

* Support for window [UDF functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/user-defined-functions) via the new method [x\_remove](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/user-defined-functions/user-defined-functions-calling-sequences#x_remove) ([MDEV-15073](https://jira.mariadb.org/browse/MDEV-15073))
* Json service for plugins ([MDEV-5313](https://jira.mariadb.org/browse/MDEV-5313))
* Change in behavior for [FLUSH TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) ([MDEV-5336](https://jira.mariadb.org/browse/MDEV-5336)).
* The [JSON\_VALID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_valid) function is automatically used as a [CHECK constraint](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/constraint#check-constraints) for the [JSON data type alias](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/json) in order to ensure that a valid json document is inserted ([MDEV-13916](https://jira.mariadb.org/browse/MDEV-13916))
* MariaDB Named Commands ([MDEV-17591](https://jira.mariadb.org/browse/MDEV-17591))
* MariaDB systemd multi-instance service have changed. See [systemd page](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/systemd#interacting-with-multiple-mariadb-server-processes) for details.

## Security Vulnerabilities Fixed in [MariaDB 10.4](what-is-mariadb-104.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2023-5157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5157): [MariaDB 10.4.26](mariadb-10426-release-notes.md)
* [CVE-2023-22084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22084): [MariaDB 10.4.32](mariadb-10-4-32-release-notes.md)
* [CVE-2022-47015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47015): [MariaDB 10.4.29](mariadb-10-4-29-release-notes.md)
* [CVE-2022-38791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38791): [MariaDB 10.4.26](mariadb-10426-release-notes.md)
* [CVE-2022-32091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32091): [MariaDB 10.4.26](mariadb-10426-release-notes.md)
* [CVE-2022-32089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32089): [MariaDB 10.4.26](mariadb-10426-release-notes.md)
* [CVE-2022-32088](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32088): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-32087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32087): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-32086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32086): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-32085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32085): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-32084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32084): [MariaDB 10.4.26](mariadb-10426-release-notes.md)
* [CVE-2022-32083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32083): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-32081](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32081): [MariaDB 10.4.26](mariadb-10426-release-notes.md)
* [CVE-2022-31624](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31624): [MariaDB 10.4.22](mariadb-10422-release-notes.md)
* [CVE-2022-27458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27458): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27457](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27457): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27456): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27455): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27452](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27452): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27451): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27449): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27448](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27448): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27447](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27447): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27446): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27445](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27445): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27444): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27387): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27386): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27385): [MariaDB 10.4.22](mariadb-10422-release-notes.md)
* [CVE-2022-27384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27384): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27383](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27383): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27382](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27382): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27381](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27381): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27380): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27379): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27378): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27377](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27377): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-27376](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27376): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-24052](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24052): [MariaDB 10.4.23](mariadb-10423-release-notes.md)
* [CVE-2022-24051](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24051): [MariaDB 10.4.23](mariadb-10423-release-notes.md)
* [CVE-2022-24050](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24050): [MariaDB 10.4.23](mariadb-10423-release-notes.md)
* [CVE-2022-24048](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24048): [MariaDB 10.4.23](mariadb-10423-release-notes.md)
* [CVE-2022-21595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21595): [MariaDB 10.4.23](mariadb-10423-release-notes.md)
* [CVE-2022-21451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21451): [MariaDB 10.4.19](mariadb-10419-release-notes.md)
* [CVE-2022-21427](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21427): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778): [MariaDB 10.4.23](mariadb-10423-release-notes.md)
* [CVE-2021-46669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46669): [MariaDB 10.4.25](mariadb-10425-release-notes.md)
* [CVE-2021-46668](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46668): [MariaDB 10.4.24](mariadb-10424-release-notes.md)
* [CVE-2021-46667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46667): [MariaDB 10.4.22](mariadb-10422-release-notes.md)
* [CVE-2021-46666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46666): [MariaDB 10.4.20](mariadb-10420-release-notes.md)
* [CVE-2021-46665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46665): [MariaDB 10.4.24](mariadb-10424-release-notes.md)
* [CVE-2021-46664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46664): [MariaDB 10.4.24](mariadb-10424-release-notes.md)
* [CVE-2021-46663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46663): [MariaDB 10.4.24](mariadb-10424-release-notes.md)
* [CVE-2021-46662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46662): [MariaDB 10.4.22](mariadb-10422-release-notes.md)
* [CVE-2021-46661](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46661): [MariaDB 10.4.24](mariadb-10424-release-notes.md)
* [CVE-2021-46659](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46659): [MariaDB 10.4.23](mariadb-10423-release-notes.md)
* [CVE-2021-46658](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46658): [MariaDB 10.4.21](mariadb-10421-release-notes.md)
* [CVE-2021-46657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46657): [MariaDB 10.4.20](mariadb-10420-release-notes.md)
* [CVE-2021-35604](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35604): [MariaDB 10.4.22](mariadb-10422-release-notes.md)
* [CVE-2021-27928](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27928): [MariaDB 10.4.18](mariadb-10418-release-notes.md)
* [CVE-2021-2389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2389): [MariaDB 10.4.21](mariadb-10421-release-notes.md)
* [CVE-2021-2372](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2372): [MariaDB 10.4.21](mariadb-10421-release-notes.md)
* [CVE-2021-2194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2194): [MariaDB 10.4.16](mariadb-10416-release-notes.md)
* [CVE-2021-2166](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2166): [MariaDB 10.4.19](mariadb-10419-release-notes.md)
* [CVE-2021-2154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2154): [MariaDB 10.4.19](mariadb-10419-release-notes.md)
* [CVE-2021-2144](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2144): [MariaDB 10.4.9](mariadb-1049-release-notes.md)
* [CVE-2021-2022](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2022): [MariaDB 10.4.14](mariadb-10414-release-notes.md)
* [CVE-2021-2007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2007): [MariaDB 10.4.7](mariadb-1047-release-notes.md)
* [CVE-2020-7221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7221): [MariaDB 10.4.12](mariadb-10412-release-notes.md)
* [CVE-2020-2922](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2922): [MariaDB 10.4.7](mariadb-1047-release-notes.md)
* [CVE-2020-28912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28912): [MariaDB 10.4.16](mariadb-10416-release-notes.md)
* [CVE-2020-2814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2814): [MariaDB 10.4.13](mariadb-10413-release-notes.md)
* [CVE-2020-2812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2812): [MariaDB 10.4.13](mariadb-10413-release-notes.md)
* [CVE-2020-2780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2780): [MariaDB 10.4.9](mariadb-1049-release-notes.md)
* [CVE-2020-2760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2760): [MariaDB 10.4.13](mariadb-10413-release-notes.md)
* [CVE-2020-2752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2752): [MariaDB 10.4.13](mariadb-10413-release-notes.md)
* [CVE-2020-2574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2574): [MariaDB 10.4.12](mariadb-10412-release-notes.md)
* [CVE-2020-15180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15180): [MariaDB 10.4.15](mariadb-10415-release-notes.md)
* [CVE-2020-14812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14812): [MariaDB 10.4.16](mariadb-10416-release-notes.md)
* [CVE-2020-14789](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14789): [MariaDB 10.4.16](mariadb-10416-release-notes.md)
* [CVE-2020-14776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14776): [MariaDB 10.4.16](mariadb-10416-release-notes.md)
* [CVE-2020-14765](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14765): [MariaDB 10.4.16](mariadb-10416-release-notes.md)
* [CVE-2020-13249](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13249): [MariaDB 10.4.13](mariadb-10413-release-notes.md)
* [CVE-2019-2974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2974): [MariaDB 10.4.9](mariadb-1049-release-notes.md)
* [CVE-2019-2938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2938): [MariaDB 10.4.9](mariadb-1049-release-notes.md)
* [CVE-2019-2805](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2805): [MariaDB 10.4.7](mariadb-1047-release-notes.md)
* [CVE-2019-2758](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2758): [MariaDB 10.4.7](mariadb-1047-release-notes.md)
* [CVE-2019-2740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2740): [MariaDB 10.4.7](mariadb-1047-release-notes.md)
* [CVE-2019-2739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2739): [MariaDB 10.4.7](mariadb-1047-release-notes.md)
* [CVE-2019-2737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2737): [MariaDB 10.4.7](mariadb-1047-release-notes.md)
* [CVE-2019-2628](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2628): [MariaDB 10.4.5](mariadb-1045-release-notes.md)
* [CVE-2019-2627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2627): [MariaDB 10.4.5](mariadb-1045-release-notes.md)
* [CVE-2019-2614](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2614): [MariaDB 10.4.5](mariadb-1045-release-notes.md)
* [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032): [MariaDB 10.4.26](mariadb-10426-release-notes.md)

## List of All [MariaDB 10.4](what-is-mariadb-104.md) Releases

| Date        | Release                                             | Status      | Release Notes                                     | Changelog                                                                                 |
| ----------- | --------------------------------------------------- | ----------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 16 May 2024 | [MariaDB 10.4.34](mariadb-10-4-34-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-4-34-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10-4-34-changelog.md) |
| 7 Feb 2024  | [MariaDB 10.4.33](mariadb-10-4-33-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-4-33-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10-4-33-changelog.md) |
| 13 Nov 2023 | [MariaDB 10.4.32](mariadb-10-4-32-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-4-32-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10-4-32-changelog.md) |
| 14 Aug 2023 | [MariaDB 10.4.31](mariadb-10-4-31-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-4-31-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10-4-31-changelog.md) |
| 7 Jun 2023  | [MariaDB 10.4.30](mariadb-10-4-30-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-4-30-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10-4-30-changelog.md) |
| 10 May 2023 | [MariaDB 10.4.29](mariadb-10-4-29-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-4-29-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10-4-29-changelog.md) |
| 6 Feb 2023  | [MariaDB 10.4.28](mariadb-10-4-28-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-4-28-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10-4-28-changelog.md) |
| 7 Nov 2022  | [MariaDB 10.4.27](mariadb-10-4-27-release-notes.md) | Stable (GA) | [Release Notes](mariadb-10-4-27-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10-4-27-changelog.md) |
| 15 Aug 2022 | [MariaDB 10.4.26](mariadb-10426-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10426-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10426-changelog.md)   |
| 20 May 2022 | [MariaDB 10.4.25](mariadb-10425-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10425-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10425-changelog.md)   |
| 12 Feb 2022 | [MariaDB 10.4.24](mariadb-10424-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10424-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10424-changelog.md)   |
| 9 Feb 2022  | [MariaDB 10.4.23](mariadb-10423-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10423-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10423-changelog.md)   |
| 8 Nov 2021  | [MariaDB 10.4.22](mariadb-10422-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10422-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10422-changelog.md)   |
| 6 Aug 2021  | [MariaDB 10.4.21](mariadb-10421-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10421-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10421-changelog.md)   |
| 23 Jun 2021 | [MariaDB 10.4.20](mariadb-10420-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10420-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10420-changelog.md)   |
| 7 May 2021  | [MariaDB 10.4.19](mariadb-10419-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10419-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10419-changelog.md)   |
| 22 Feb 2021 | [MariaDB 10.4.18](mariadb-10418-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10418-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10418-changelog.md)   |
| 11 Nov 2020 | [MariaDB 10.4.17](mariadb-10417-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10417-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10417-changelog.md)   |
| 3 Nov 2020  | [MariaDB 10.4.16](mariadb-10416-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10416-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10416-changelog.md)   |
| 7 Oct 2020  | [MariaDB 10.4.15](mariadb-10415-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10415-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10415-changelog.md)   |
| 10 Aug 2020 | [MariaDB 10.4.14](mariadb-10414-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10414-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10414-changelog.md)   |
| 12 May 2020 | [MariaDB 10.4.13](mariadb-10413-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10413-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10413-changelog.md)   |
| 28 Jan 2020 | [MariaDB 10.4.12](mariadb-10412-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10412-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10412-changelog.md)   |
| 11 Dec 2019 | [MariaDB 10.4.11](mariadb-10411-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10411-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10411-changelog.md)   |
| 8 Nov 2019  | [MariaDB 10.4.10](mariadb-10410-release-notes.md)   | Stable (GA) | [Release Notes](mariadb-10410-release-notes.md)   | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10410-changelog.md)   |
| 5 Nov 2019  | [MariaDB 10.4.9](mariadb-1049-release-notes.md)     | Stable (GA) | [Release Notes](mariadb-1049-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1049-changelog.md)    |
| 11 Sep 2019 | [MariaDB 10.4.8](mariadb-1048-release-notes.md)     | Stable (GA) | [Release Notes](mariadb-1048-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1048-changelog.md)    |
| 31 Jul 2019 | [MariaDB 10.4.7](mariadb-1047-release-notes.md)     | Stable (GA) | [Release Notes](mariadb-1047-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1047-changelog.md)    |
| 18 Jun 2019 | [MariaDB 10.4.6](mariadb-1046-release-notes.md)     | Stable (GA) | [Release Notes](mariadb-1046-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1046-changelog.md)    |
| 21 May 2019 | [MariaDB 10.4.5](mariadb-1045-release-notes.md)     | RC          | [Release Notes](mariadb-1045-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1045-changelog.md)    |
| 7 Apr 2019  | [MariaDB 10.4.4](mariadb-1044-release-notes.md)     | RC          | [Release Notes](mariadb-1044-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1044-changelog.md)    |
| 25 Feb 2019 | [MariaDB 10.4.3](mariadb-1043-release-notes.md)     | RC          | [Release Notes](mariadb-1043-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1043-changelog.md)    |
| 29 Jan 2019 | [MariaDB 10.4.2](mariadb-1042-release-notes.md)     | Beta        | [Release Notes](mariadb-1042-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1042-changelog.md)    |
| 20 Dec 2018 | [MariaDB 10.4.1](mariadb-1041-release-notes.md)     | Beta        | [Release Notes](mariadb-1041-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1041-changelog.md)    |
| 9 Nov 2018  | [MariaDB 10.4.0](mariadb-1040-release-notes.md)     | Alpha       | [Release Notes](mariadb-1040-release-notes.md)    | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1040-changelog.md)    |

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
