---
description: >-
  Incompatibilities and feature differences between MariaDB 11.8 and MySQL 8.0,
  covering storage engines, extensions, and implementation differences.
---

# Incompatibilities and Feature Differences Between MariaDB 11.8 and MySQL 8.0

MariaDB maintains high levels of compatibility with MySQL, and most applications that use MySQL will work seamlessly with MariaDB. However, take note of the following incompatibilities and feature differences between [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) and MySQL 8.0. It is based on the versions MySQL 8.0.43 and [MariaDB 11.8.3](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/11.8.3). This page compares against MySQL 8.0 specifically; MySQL 8.4 (LTS) is a separate comparison and is not covered here.

## Storage Engines

In addition to the standard [InnoDB](../../server-usage/storage-engines/innodb/README.md), [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/README.md), [BLACKHOLE](../../server-usage/storage-engines/blackhole.md), [CSV](../../server-usage/storage-engines/csv/README.md), [MEMORY](../../server-usage/storage-engines/memory-storage-engine.md), [ARCHIVE](../../server-usage/storage-engines/archive.md), and [MERGE](../../server-usage/storage-engines/merge.md) storage engines, the following are also available with [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118):

* [ColumnStore](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/RaYUwfaLLE1EkMr1e8Ud/architecture/columnstore-storage-engine-overview) utilizes a massively parallel distributed data architecture and is designed for big data scaling to process petabytes of data.
* [MyRocks](../../server-usage/storage-engines/myrocks/README.md), a storage engine with great compression
* [S3 storage engine](../../server-usage/storage-engines/s3-storage-engine/README.md) allows one to archive MariaDB tables in Amazon S3, or any third-party public or private cloud that implements S3 API.
* [Aria](../../server-usage/storage-engines/aria/README.md), MyISAM replacement with better caching.
* [CONNECT](../../server-usage/storage-engines/connect/README.md)
* [SEQUENCE](../../server-usage/storage-engines/sequence-storage-engine.md)
* [Spider](../../server-usage/storage-engines/spider/README.md)
* [SphinxSE](../../server-usage/storage-engines/sphinx-storage-engine/README.md)
* [FederatedX](../../server-usage/storage-engines/federatedx-storage-engine/README.md) (drop-in replacement for Federated)
* [OQGRAPH](../../server-usage/storage-engines/oqgraph-storage-engine/README.md)

## Extensions and New Features

The most notable features available in MariaDB, but not in MySQL, are:

* [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) is a standard part of MariaDB Server.
* [Vector search](../../reference/sql-structure/vectors/vector-overview.md) using the [VECTOR](../../reference/data-types/numeric-data-types/vector.md) data type and vector indexes (`CREATE ... VECTOR INDEX`) for approximate-nearest-neighbor search. MySQL 8.0 has no vector data type or vector index.
* [Temporal data tables](../../reference/sql-structure/temporal-tables/README.md) in the form of:
  * [System-versioned tables](../../reference/sql-structure/temporal-tables/system-versioned-tables.md) (allow you to query and operate on historic data).
  * [Application-time periods](../../reference/sql-structure/temporal-tables/application-time-periods.md) (allow you to query and operate on a temporal range of data), including the [WITHOUT OVERLAPS](../../reference/sql-structure/temporal-tables/application-time-periods.md#without-overlaps) clause.
  * [Bitemporal tables](../../reference/sql-structure/temporal-tables/bitemporal-tables.md) (which combine both system-versioning and application-time periods).
* [DML-only flashback](../../server-management/server-monitoring-logs/binary-log/flashback.md), allowing instances, databases or tables to be rolled back to an old snapshot.
* [Oracle compatibility mode](sql_modeoracle.md)
* MariaDB supports [localization](../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/setting-the-language-for-error-messages.md) in a number of additional languages: Bulgarian, Chinese, Georgian, Hindi, Serbian, and Ukrainian.
* MariaDB has made major improvements to the optimizer.
* [Sequences](../../reference/sql-structure/sequences/README.md)
* [Table Value Constructors](../../reference/sql-structure/sql-language-structure/table-value-constructors.md)
* [Dynamic Columns](../../reference/sql-structure/nosql/dynamic-columns.md) support
* [Semi-sync plugin](../../ha-and-performance/standard-replication/semisynchronous-replication.md) merged into the server
* OR REPLACE syntax for [CREATE](../../reference/sql-statements/data-definition/create/README.md) statements, such as [CREATE OR REPLACE TABLE](../../reference/sql-statements/data-definition/create/create-table.md#create-or-replace), [CREATE OR REPLACE DATABASE](../../reference/sql-statements/data-definition/create/create-database.md#or-replace), etc
* [DELETE ... RETURNING](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md), [INSERT ... RETURNING](../../reference/sql-statements/data-manipulation/inserting-loading-data/insertreturning.md), [REPLACE ... RETURNING](../../reference/sql-statements/data-manipulation/changing-deleting-data/replacereturning.md)
* [GRANT to PUBLIC](../../reference/sql-statements/account-management-sql-statements/grant.md#to-public) - [MDEV-5215](https://jira.mariadb.org/browse/MDEV-5215) ([blog post](https://mariadb.org/grant-to-public-in-mariadb/))
* [WAIT](../../reference/sql-statements/transactions/wait-and-nowait.md) syntax for setting the lock wait timeout.
* [UUID](../../reference/data-types/string-data-types/uuid-data-type.md) data type for storing UUIDs.
* [UUID\_v7()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/uuid_v7.md) and [UUID\_v4()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/uuid_v4.md) functions for generating version 7 and version 4 UUIDs.
* [INET6](../../reference/data-types/string-data-types/inet6.md) and [INET4](../../reference/data-types/string-data-types/inet4.md) data types for storing IPv6 and IPv4 addresses.
* Extended [TIMESTAMP](../../reference/data-types/date-and-time-data-types/timestamp.md) range up to `2106-02-07 06:28:15 UTC` on 64-bit platforms, whereas MySQL 8.0 is limited to `2038-01-19 03:14:07 UTC` - [MDEV-32188](https://jira.mariadb.org/browse/MDEV-32188)
* [PARSEC authentication plugin](../../reference/plugins/authentication-plugins/authentication-plugin-parsec.md) - [MDEV-32618](https://jira.mariadb.org/browse/MDEV-32618)
* Server-side limits on temporary file and table space, via [max\_tmp\_session\_space\_usage](../../security/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_session_space_usage-system-variable.md) and `max_tmp_total_space_usage` - [MDEV-9101](https://jira.mariadb.org/browse/MDEV-9101)
* [SUPER privileges](../../reference/sql-statements/account-management-sql-statements/grant.md) made more granular.
* [PROXY protocol support](../../clients-and-utilities/server-client-software/client-libraries/proxy-protocol-support.md)
* Multiple [compression algorithms available as plugins](../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md)
* Number of supported decimals in [DECIMAL](../../reference/data-types/numeric-data-types/decimal.md) has increased from `30` to `38`
* Number of parts of an index increased from `16` to `32`.
* Added catchall for [list partitions](../../server-usage/partitioning-tables/partitioning-types/list-partitioning-type.md)
* Oracle-style [EXECUTE IMMEDIATE](../../reference/sql-statements/prepared-statements/execute-immediate.md) statement
* Lots of new [JSON functions](../../reference/sql-functions/special-functions/json-functions/README.md)
* [Microsecond Precision in Processlist](../../reference/system-tables/information-schema/time_ms-column-in-information_schemaprocesslist.md)
* [Table Elimination](../../ha-and-performance/optimization-and-tuning/query-optimizations/table-elimination/README.md)
* [Virtual Columns](../../reference/sql-statements/data-definition/create/generated-columns.md)
* [Extended User Statistics](../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md)
* [KILL all queries for a user](../../reference/sql-statements/administrative-sql-statements/kill.md)
* [Storage-engine-specific CREATE TABLE](../../reference/product-development/plugin-development/storage-engines-storage-engine-development/engine-defined-new-tablefieldindex-attributes.md)
* MariaDB [supports more collations](../../reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations.md) (550) than MySQL (286).
* [FLUSH SSL](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) command to reload SSL certificates without server restart.
* `IF NOT EXISTS` clause added to [INSTALL PLUGIN](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) and `IF EXISTS` clause added to [UNINSTALL PLUGIN](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) and [UNINSTALL SONAME](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)
* [Enhancements to INFORMATION SCHEMA.PLUGINS table](../../reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [Group commit for the binary log](../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md). This makes [replication notably faster!](https://www.facebook.com/note.php?note_id=10150261692455933)
* [BACKUP STAGE](../../reference/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md) allows one to implement very efficient backups with minimal locking.
* [Progress reporting](../../reference/product-development/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting.md) for [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/README.md) and [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)
* [SHOW EXPLAIN](../../reference/sql-statements/administrative-sql-statements/show/show-explain.md) gives the EXPLAIN plan for a query running in another thread. MySQL introduced the EXPLAIN FOR CONNECTION syntax to do the same thing.
* MariaDB uses [PCRE (Perl Compatible Regular Expressions)](../../reference/sql-functions/string-functions/regular-expressions-functions/pcre.md) for its regular-expression functions, giving different syntax and features from MySQL 8.0's ICU-based regex engine. (Both support functions such as [REGEXP\_REPLACE()](../../reference/sql-functions/string-functions/regular-expressions-functions/regexp_replace.md).)
* [HandlerSocket](../../reference/sql-structure/nosql/handlersocket/README.md) and faster [HANDLER](../../reference/sql-structure/nosql/handler/README.md) calls
* MySQL 8.0 does not support [PROCEDURE ANALYSE](../../reference/sql-functions/secondary-functions/information-functions/procedure-analyse.md)

## Incompatibilities and Differences in Implementation

When moving from MySQL 8.0 to [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118), please take note of the following incompatibilities:

* For a list of function differences, see [Function Differences Between MariaDB 11.8 and MySQL 8.0](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-11.8-and-mysql-8.0.md).
* For a list of system variable differences, see [System Variable Differences Between MariaDB 11.8 and MySQL 8.0](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-11.8-and-mysql-8.0.md).
* For replication, see [Replication Compatibility Between MariaDB and MySQL](replication-compatibility-between-mariadb-and-mysql.md).
* MariaDB does not support MySQL's SET PERSIST - [MDEV-16228](https://jira.mariadb.org/browse/MDEV-16228)
* MariaDB's GTID is not compatible with MySQL's. Note that MariaDB and MySQL also have different [GTID system variables](../../ha-and-performance/standard-replication/gtid/gtid-system-variables.md), so these need to be adjusted when migrating.
* The [unix\_socket authentication plugin](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) is now default on Unix-like systems, which is a major change to authentication in MariaDB. See [Authentication from MariaDB 10.4](../../security/user-account-management/authentication-from-mariadb-10-4.md) for an overview of the changes.
* All mysql\* binaries are now named mariadb\* (the previous mysql named is retained as a symlink for compatibility purposes)
* Not all [character sets and collations](../../reference/data-types/string-data-types/character-sets/README.md) are [supported](../../reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations.md) across both MySQL and MariaDB. [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) supports 40 character sets and 550 collations (including the 44 collation aliases added in [MariaDB 11.4.5](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.5) to ease replication from MySQL to MariaDB). As of 8.0.35, MySQL supports 41 character sets (`gb18030` being the additional one - [MDEV-7495](https://jira.mariadb.org/browse/MDEV-7495)) and 286 collations.
* MariaDB indicates collation pad status as part of the name (e.g. `utf8mb3_unicode_nopad_ci`), while MySQL indicates pad status by means of an extra column in [SHOW COLLATION](../../reference/sql-statements/administrative-sql-statements/show/show-collation.md).
* To make CREATE TABLE ... SELECT work the same way in statement based and row based replication it's by default executed as [CREATE OR REPLACE TABLE](../../reference/sql-statements/data-definition/create/create-table.md#create-or-replace) on the replica. One benefit of this is that if the replica dies in the middle of CREATE ... SELECT it will be able to continue.
  * One can use the [slave-ddl-exec-mode](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) variable to specify how `CREATE TABLE` and `DROP TABLE` is replicated.
* Users created with MySQL's SHA256 password algorithm cannot be used in [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) - [MDEV-9804](https://jira.mariadb.org/browse/MDEV-9804).
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) does not support Lateral Derived Tables - [MDEV-19078](https://jira.mariadb.org/browse/MDEV-19078).
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) does not support CIDR notation for user accounts - [MDEV-25515](https://jira.mariadb.org/browse/MDEV-25515).
* MariaDB stores [JSON](../../reference/sql-functions/special-functions/json-functions/README.md) as true text, not in binary format as MySQL. MariaDB's JSON functions are much faster than MySQL's so there is no need to store in binary format, which would add complexity when manipulating JSON objects.
* For the same reason, MariaDB's [JSON data type](../../reference/data-types/string-data-types/json.md) is an alias for [LONGTEXT](../../reference/data-types/string-data-types/longtext.md). If you want to replicate JSON columns from MySQL to MariaDB, you should store JSON objects in MySQL in a TEXT or LONGTEXT column or use statement-based replication. If you are using JSON columns and want to upgrade to MariaDB, use the [mysql\_json](../../reference/plugins/other-plugins/mysql_json.md) plugin to automatically convert MySQL JSON to TEXT, or alternatively you need to either convert them to TEXT or use mysqldump to copy these tables to MariaDB.
* In MySQL, JSON is compared according to json values. In MariaDB JSON strings are normal strings and compared as strings.
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) does not support MySQL's JSON operators (`->` and `->>`) - [MDEV-13594](https://jira.mariadb.org/browse/MDEV-13594). Support for the [`->` and `->>` operators](../../reference/sql-functions/special-functions/json-functions/json-arrow-operators.md) was added in MariaDB 13.1.
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) supports the standard by producing null and a warning for [JSON\_SEARCH](../../reference/sql-functions/special-functions/json-functions/json_search.md) when given invalid data, while MySQL produces an error.
* [Roles](../../security/user-account-management/roles/README.md)
  * MariaDB never allows authentication via roles, while MySQL permits this.
  * MySQL permits activating multiple roles at the same time. MariaDB can achieve the same result by creating an intermediate aggregate role.
  * In the [INFORMATION\_SCHEMA.ENABLED\_ROLES table](../../reference/system-tables/information-schema/information-schema-tables/information-schema-enabled_roles-table.md), MySQL reports just the direct list of enabled roles, while MariaDB reports the enabled role, plus the effective inherited roles.
  * MySQL extends the [INFORMATION\_SCHEMA.APPLICABLE\_ROLES table](../../reference/system-tables/information-schema/information-schema-tables/information-schema-applicable_roles-table.md) .
  * MySQL includes the tables INFORMATION\_SCHEMA.ROLE\_TABLE\_GRANTS, INFORMATION\_SCHEMA.ROLE\_ROUTINE\_GRANTS, INFORMATION\_SCHEMA.ROLE\_COLUMN\_GRANTS, and INFORMATION\_SCHEMA ADMINISTRABLE\_ROLE\_AUTHORIZATIONS.
* MySQL has the [performance schema](../../reference/system-tables/performance-schema/README.md) enabled by default. For performance reasons [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) has it disabled by default. You can enable it by starting `mariadbd` with the option `--performance-schema`.
* MariaDB has removed the [InnoDB Change Buffer](../../server-usage/storage-engines/innodb/innodb-change-buffering.md).
* In [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118), using [FLUSH TABLES](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) without any table list will only close tables not in use, and tables not locked by the FLUSH TABLES connection. If there are no locked tables, FLUSH TABLES will be instant and will not cause any waits, as it no longer waits for tables in use. When a table list is provided, the server will wait for the end of any transactions that are using the tables. In MySQL, FLUSH TABLES only waits for the statements to complete.
* MariaDB binaries (`mariadbd`, [myisamchk](../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) etc.) give a warning if one uses a unique prefix of an option (such as `--big-table` instead of `--big-tables`). MySQL binaries require the full option name.
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) implements [InnoDB encryption](../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-tde-fundamentals.md) in a different way to MySQL 8.0.
* MySQL's implementation of [aborting statements that exceed a certain time to execute](../../ha-and-performance/optimization-and-tuning/query-optimizations/aborting-statements.md) can only kill SELECTs, while MariaDB's can kill any queries (excluding stored procedures).
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) does not support MySQL's `SELECT /*+ MAX_EXECUTION_TIME(n) */ ...` - see [Aborting Statements that Exceed a Certain Time to Execute](../../ha-and-performance/optimization-and-tuning/query-optimizations/aborting-statements.md).
* MySQL 8.0 does not support the [Query Cache](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md).
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) does not support the MySQL Memcached plugin (which has been deprecated in MySQL 8.0). However, data stored using memcached can be retrieved because the data is stored as InnoDB tables. MariaDB is able to start successfully with an error message of not being able to find libmemcached.so library.
* In MySQL, `X'HHHH'`, the standard SQL syntax for binary string literals, erroneously works in the same way as `0xHHHH`, which could work as a number or string depending on the context. In MariaDB, this has been fixed to behave as a string in all contexts (and never as a number). See [CAST](../../reference/sql-functions/string-functions/cast.md) and [Hexadecimal Literals](../../reference/sql-structure/sql-language-structure/hexadecimal-literals.md) for more details and examples.
* In [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118), [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) does not quote the DEFAULT value of an integer. [MariaDB 10.2](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and earlier, and MySQL, do. Since MariaDB can support defaults for [BLOB](../../reference/data-types/string-data-types/blob.md) and [TEXT](../../reference/data-types/string-data-types/text.md) fields, while MySQL does not, [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) will also append `DEFAULT NULL` where no default is explicitly provided to nullable BLOB or TEXT fields in MariaDB.
* As a result of implementing [Table Value Constructors](../../reference/sql-structure/sql-language-structure/table-value-constructors.md), the [VALUES function](../../reference/sql-functions/secondary-functions/miscellaneous-functions/values-value.md) has been renamed to VALUE().
* MariaDB's [NOWAIT](../../reference/sql-statements/transactions/wait-and-nowait.md) supports SELECT statements, LOCK TABLES and various DDL statements, while MySQL's NOWAIT only supports SELECT.
* MariaDB's [NOWAIT](../../reference/sql-statements/transactions/wait-and-nowait.md) cannot be added on [views](../../server-usage/views/README.md) and [stored procedures](../../server-usage/stored-routines/stored-procedures/README.md) while MySQL's can - [MDEV-25247](https://jira.mariadb.org/browse/MDEV-25247)
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) supports `SELECT ... FOR UPDATE` and `LOCK IN SHARE MODE`, including the `WAIT n`, `NOWAIT`, and `SKIP LOCKED` modifiers. It does not support MySQL 8.0's `FOR SHARE` spelling (use `LOCK IN SHARE MODE` instead) or the `OF tbl_name` clause for locking only specific tables in a join - [MDEV-17514](https://jira.mariadb.org/browse/MDEV-17514).
* MariaDB does not support [RENAME](../../reference/sql-statements/data-definition/rename-table.md) table while it is write-locked - [MDEV-30814](https://jira.mariadb.org/browse/MDEV-30814)
* MariaDB returns an `ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction` when unable to lock within the time, while MySQL returns `ERROR 3572 (HY000): Statement aborted because lock(s) could not be acquired immediately and NOWAIT is set`
* MariaDB does not support the optional init\_vector argument for [AES\_ENCRYPT](../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_encrypt.md) and [AES\_DECRYPT](../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_decrypt.md) or the block\_encryption\_mode variable - [MDEV-9069](https://jira.mariadb.org/browse/MDEV-9069)
* MariaDB does not support the `--initialize` option. Use [mariadb-install-db](../../clients-and-utilities/deployment-tools/mariadb-install-db.md) instead. - [MDEV-19010](https://jira.mariadb.org/browse/MDEV-19010)
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) does not support the ngram and MeCab full-text parser plugins - [MDEV-10267](https://jira.mariadb.org/browse/MDEV-10267), [MDEV-10268](https://jira.mariadb.org/browse/MDEV-10268).
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) does not support the [MySQL X plugin](https://dev.mysql.com/doc/refman/8.0/en/x-plugin.html).
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) does not support [CREATE TABLESPACE](../../reference/sql-statements/data-definition/create/create-tablespace.md) for InnoDB.
* The MySQL 8.0 and [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) [INFORMATION\_SCHEMA.COLUMNS](../../reference/system-tables/information-schema/information-schema-tables/information-schema-columns-table.md) table contain slightly different fields.
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) client executables allow the connection protocol to be forced by specifying only connection properties on the command-line. See [mariadb Command-line client](../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#specify-which-protocol-to-use)
* The MySQL binary log includes the thread\_id, while MariaDB's [binary log](../../server-management/server-monitoring-logs/binary-log/README.md) does not - [MDEV-7850](https://jira.mariadb.org/browse/MDEV-7850)
* The MariaDB syntax supporting Spatial Reference System IDs for spatial data type columns with [REF\_SYSTEM\_ID](../../reference/sql-statements/data-definition/create/create-table.md#ref_system_id) is not supported by MySQL. MySQL 8.0 introduced `CREATE SPATIAL REFERENCE SYSTEM`, which is not supported by MariaDB - [MDEV-29953](https://jira.mariadb.org/browse/MDEV-29953)
* [MariaDB 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) does not support the RESTART statement - [MDEV-30813](https://jira.mariadb.org/browse/MDEV-30813)
* [Compressing the binary log in MariaDB](../../server-management/server-monitoring-logs/binary-log/compressing-events-to-reduce-size-of-the-binary-log.md) uses a different compression algorithm, and different system variables to manage.

For protocol differences, see [MariaDB protocol difference with MySQL](../../reference/clientserver-protocol/mariadb-protocol-differences-with-mysql.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
