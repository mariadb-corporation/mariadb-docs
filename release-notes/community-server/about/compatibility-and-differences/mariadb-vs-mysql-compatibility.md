# MariaDB versus MySQL - Compatibility

See also [**MariaDB vs MySQL - Features**](mariadb-vs-mysql-features.md)

## Replacement for MySQL

Until [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), MariaDB versions functioned as a "drop-in replacement" for the equivalent MySQL version, with some limitations. From [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), it is usually still very easy to upgrade from MySQL.

* MariaDB's data files are generally binary compatible with those from the equivalent MySQL version.
  * All filenames and paths are generally the same.
  * Data and table definition files (.frm) files are binary compatible.
  * See note below for an incompatibility with views!
* MariaDB's client protocol is binary compatible with MySQL's client protocol.
  * All client APIs and structs are identical.
  * All ports and sockets are generally the same.
  * All MySQL connectors (PHP, Perl, Python, Java, .NET, MyODBC, Ruby, MySQL C\
    connector etc) work unchanged with MariaDB.
  * There are some [installation issues with PHP5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues/installation-issues-with-php5) that you should be aware of (a bug in how the old PHP5 client checks library compatibility).

This means that for many cases, you can just uninstall MySQL and [install MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb) and you are good to go. There is not generally any need to convert any data files.

However, you must still run [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) to finish the upgrade. This is needed to ensure that your mysql privilege and event tables are updated with the new fields MariaDB uses.

That said, MariaDB has a lot of [new options, extension, storage engines and bug fixes](mariadb-vs-mysql-features.md) that are not in MySQL. You can find the feature set for the different MariaDB versions on the [What is in the different MariaDB Releases](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-in-the-different-mariadb-releases/README.md) page.

### Drop-in Compatibility of Specific MariaDB Versions

[MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md), [MariaDB 10.3](../../old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md), and [MariaDB 10.4](../../old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104.md) function as limited drop-in replacements for MySQL 5.7, as far as [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) is concerned. However, the implementation differences continue to grow in each new MariaDB version.

[MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) and [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) function as limited drop-in replacements for MySQL 5.6, as far as [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) is concerned. However, there are some implementation differences in some features.

[MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) functions as a drop-in replacement for MySQL 5.5.

[MariaDB 5.1](../../old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md), [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md), and [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) function as drop-in replacements for MySQL 5.1.

## Replication Compatibility

See [Replication Compatibility Between MariaDB and MySQL](replication-compatibility-between-mariadb-and-mysql.md).

## Incompatibilities between Currently Maintained MariaDB Versions and MySQL

### Incompatibilities between MariaDB Rolling and MySQL 8.0

* See [Incompatibilities and Feature Differences Between MariaDB Rolling and MySQL 8.0](incompatibilities-and-feature-differences-between-mariadb-rolling-and-mysql.md) for details.
* [Function Differences Between MariaDB Rolling and MySQL 8.0](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-rolling-and-mysql-8-0.md)
* [System Variable Differences Between MariaDB Rolling and MySQL 8.0](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-rolling-and-mysql-8-0.md)

### Incompatibilities between [MariaDB 11.4](../../11.4/what-is-mariadb-114.md) and MySQL 8.0

* See [Incompatibilities and Feature Differences Between MariaDB 11.4 and MySQL 8.0](incompatibilities-and-feature-differences-between-mariadb-11-4-and-mysql-8.md) for details.
* [Function Differences Between MariaDB 11.4 and MySQL 8.0](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-11-4-and-mysql-8-0.md)
* [System Variable Differences Between MariaDB 11.4 and MySQL 8.0](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-11-4-and-mysql-8-0.md)

### Incompatibilities between [MariaDB 11.2](../../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md) and MySQL 8.0

* See [Incompatibilities and Feature Differences Between MariaDB 11.2 and MySQL 8.0](incompatibilities-and-feature-differences-between-mariadb-and-mysql-unmaint/incompatibilities-and-feature-differences-between-mariadb-11-2-and-mysql-8.md) for details.
* [Function Differences Between MariaDB 11.2 and MySQL 8.0](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-and-mysql-unmaintained-series/function-differences-between-mariadb-11-2-and-mysql-8-0.md)
* [System Variable Differences Between MariaDB 11.2 and MySQL 8.0](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-11-2-and-mysql-8-0.md)

### Incompatibilities between [MariaDB 10.11](../../10.11/what-is-mariadb-1011.md) and MySQL 8.0

* See [Incompatibilities and Feature Differences Between MariaDB 10.11 and MySQL 8.0](incompatibilities-and-feature-differences-between-mariadb-10-11-and-mysql-8.md) for details.
* [Function Differences Between MariaDB 10.11 and MySQL 8.0](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-10-11-and-mysql-8-0.md)
* [System Variable Differences Between MariaDB 10.11 and MySQL 8.0](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-10-11-and-mysql-8-0.md)

### Incompatibilities between [MariaDB 10.6](../../10.6/what-is-mariadb-106.md) and MySQL 8.0

* See [Incompatibilities and Feature Differences Between MariaDB 10.6 and MySQL 8.0](incompatibilities-and-feature-differences-between-mariadb-10-6-and-mysql-8.md) for details.
* [Function Differences Between MariaDB 10.6 and MySQL 8.0](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-10-6-and-mysql-8-0.md)
* [System Variable Differences Between MariaDB 10.6 and MySQL 8.0](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-10-6-and-mysql-8-0.md)

## Incompatibilities between Unmaintained MariaDB Versions and MySQL

For unmaintained versions, see:

* [Incompatibilities and Feature Differences Between MariaDB and MySQL - Unmaintained Series](incompatibilities-and-feature-differences-between-mariadb-and-mysql-unmaint/)
* [Function Differences Between MariaDB and MySQL - Unmaintained Series](function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-and-mysql-unmaintained-series/)
* [System Variable Differences Between MariaDB and MySQL - Unmaintained Series](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/)

### Incompatibilities between [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) and MySQL 5.7

* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) and above does not support MySQL 5.7's packed JSON objects. MariaDB follows the SQL standard and stores the JSON as a normal TEXT/BLOB. If you want to replicate JSON columns from MySQL to MariaDB, you should store JSON objects in MySQL in a TEXT column or use statement based replication. If you are using JSON columns and want to upgrade to MariaDB, you can either convert the JSON columns to TEXT or use [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) to copy these tables to MariaDB. In MySQL, JSON is compared according to json values. In MariaDB JSON strings are normal strings and compared as strings.
* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)'s InnoDB encryption is implemented differently than MySQL 5.7's InnoDB encryption.
* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) does not support the ngram and MeCab full-text parser plugins - [MDEV-10267](https://jira.mariadb.org/browse/MDEV-10267), [MDEV-10268](https://jira.mariadb.org/browse/MDEV-10268).
* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) does not support multiple triggers for a table - [MDEV-6112](https://jira.mariadb.org/browse/MDEV-6112). This is fixed in [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md)
* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) does not support [CREATE TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-tablespace) for InnoDB.
* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) does not support MySQL 5.7's “native” InnoDB partitioning handler. Fixed in [MariaDB 10.6.15](../../10.6/10.6.15.md).
* MariaDB does not support MySQL 5.7's X protocol.
* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) does not support the use of multiple triggers of the same type for a table. This feature was introduced in [MariaDB 10.2.2](../../old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md).
* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) does not support MySQL 5.7's transportable tablespaces for partitioned InnoDB tables. ALTER TABLE ... {DISCARD|IMPORT} PARTITION is not supported. For a workaround [see the following blog post](https://www.geoffmontee.com/importing-innodb-partitions-in-mysql-5-6-and-mariadb-10-010-1/).
* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) does not support MySQL 5.7's online undo tablespace truncation. However, this feature was added to [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md).
* MySQL 5.7 features a new implementation of the `performance_schema` and a `sys` schema wrapper. These are not yet supported in MariaDB.
* MySQL 5.7 adds multi-source replication and replication channels. [Multi-source replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/multi-source-replication) was added to MariaDB previously, in [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), and uses a different syntax.
* MySQL 5.7 adds group replication. This feature is incompatible with MariaDB's [galera-cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) replication.
* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) does not support MySQL 5.7's, `ACCOUNT LOCK/UNLOCK` synax for `CREATE USER` and `ALTER USER` statements.
* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) does not support MySQL 5.7's `ALTER TABLE...RENAME INDEX` statements.
* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) does not support MySQL 5.7's `STACKED` operation for [GET DIAGNOSTICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/get-diagnostics) statements.
* [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) does not support MySQL 5.7's `{WITH|WITHOUT} VALIDATION` syntax for `ALTER TABLE.. EXCHANGE PARTITION` statements.
* MariaDB does not support the optional init\_vector argument for [AES\_ENCRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_encrypt) and [AES\_DECRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_decrypt) or the block\_encryption\_mode variable - [MDEV-9069](https://jira.mariadb.org/browse/MDEV-9069)
* MariaDB does not support the `--initialize` option. Use [mysql\_install\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_install_db) instead. - [MDEV-19010](https://jira.mariadb.org/browse/MDEV-19010)
* Also see Incompatibilities between [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) and MySQL 5.6.
* Also see a detailed breakdown of [System variable differences between MariaDB 10.1and MySQL 5.7](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-10-1-and-mysql-5-7.md).

### Incompatibilities between [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) and MySQL 5.6

* MySQL does not support MariaDB's [Spider Storage Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider).
* All MySQL binaries (`mysqld`, [myisamchk](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/myisam-clients-and-utilities/myisamchk) etc.) give a warning if one uses a prefix of an option (such as `--big-table` instead of `--big-tables`). MariaDB binaries work in the same way as most other Unix commands and don't give warnings when using unique prefixes.
* MariaDB GTID is not compatible with MySQL 5.6. This means that one can't have MySQL 5.6 as a slave for [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md). However [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) can be a slave of MySQL 5.6 or any earlier MySQL/MariaDB version. Note that MariaDB and MySQL also have different [GTID system variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#system-variables-for-global-transaction-id), so these need to be adjusted when migrating.
* [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) [multi-source replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/multi-source-replication) is not supported in MySQL 5.6.
* To make CREATE TABLE ... SELECT work the same way in statement based and row based replication it's by default executed as [CREATE OR REPLACE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table#create-or-replace) on the slave. One benefit of this is that if the slave dies in the middle of CREATE ... SELECT it will be able to continue.
  * One can use the [slave-ddl-exec-mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) variable to specify how `CREATE TABLE` and `DROP TABLE` is replicated.
* See also a detailed breakdown of [System variable differences between MariaDB 10.0 and MySQL 5.6](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-100-and-mysql-56.md).
* MySQL 5.6 has [performance schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) enabled by default. For performance reasons [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) has it disabled by default. You can enable it by starting `mysqld` with the option `--performance-schema`.
* [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) does not support the MySQL Memcached plugin. However, data stored using memcached can be retrieved because the data is stored as InnoDB tables. MariaDB is able to start successfully with an error message of not being able to find libmemcached.so library.
* Users created with MySQL's SHA256 password algorithm cannot be used in [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) as MariaDB does not include MySQL's `sha256_password` plugin.
* [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) does not support delayed replication - [MDEV-7145](https://jira.mariadb.org/browse/MDEV-7145).
* Also see a detailed breakdown of [System variable differences between MariaDB 10.0 and MySQL 5.6](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-100-and-mysql-56.md).
* The low-level temporal format used by TIME, DATETIME and TIMESTAMP is different in MySQL 5.6 and [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md). (In [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md), the MySQL implementation is used by default - see [mysql56\_temporal\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#mysql56_temporal_format).)
* MariaDB implements some changes in the SQL query optimizer over what's available in MySQL. This can result in [EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) statements showing different plans.
* MySQL delayed replication, (through `MASTER_DELAY`), is not supported in [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), it was implemented in [MariaDB 10.2.5](../../old-releases/release-notes-mariadb-10-2-series/mariadb-1025-release-notes.md)
* MariaDB does not support the optional init\_vector argument for [AES\_ENCRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_encrypt) and [AES\_DECRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_decrypt) or the block\_encryption\_mode variable - [MDEV-9069](https://jira.mariadb.org/browse/MDEV-9069)

### Incompatibilities between [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) and MySQL 5.5

* Views with definition ALGORITHM=MERGE or ALGORITHM=TEMPTABLE got accidentally swapped between MariaDB and MySQL! You have to re-create views created with either of these definitions!
* [INSERT IGNORE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/ignore) also gives warnings for duplicate key errors. You can turn this off by setting `OLD_MODE=NO_DUP_KEY_WARNINGS_WITH_IGNORE` (see [OLD\_MODE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/old-mode)).
* Before [MariaDB 5.5.31](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5531-release-notes.md), `X'HHHH'`, the standard SQL syntax for binary string literals, erroneously worked in the same way as `0xHHHH`, which could work as a number or string depending on the context. In 5.5.31 this was fixed to behave as a string in all contexts (and never as a number), introducing an incompatibility with previous versions of MariaDB, and all versions of MySQL. See [CAST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/cast) and [Hexadecimal Literals](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/hexadecimal-literals) for more details and examples.
* MariaDB [dynamic columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/nosql/dynamic-columns) are not supported by MySQL.
* MariaDB [virtual columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/generated-columns) are not supported by MySQL.
* MariaDB's [HandlerSocket plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/nosql/handlersocket) is not supported by MySQL.
* MariaDB's [Cassandra Storage Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/cassandra) is not supported by MySQL.
* As of [MariaDB 5.5.35](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5535-release-notes.md), [EXTRACT (HOUR FROM ...)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/extract) adheres to the SQL standard and returns a result from 0 to 23. In MySQL, and earlier versions of MariaDB, the result can be greater than 23.
* See also a detailed breakdown of [System variable differences between MariaDB 5.5 and MySQL 5.5](system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-55-and-mysql-55.md).

### Incompatibilities between [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) and MySQL 5.1

* Views with definition ALGORITHM=MERGE or ALGORITHM=TEMPTABLE got accidentally swapped between [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) and [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)! You have to re-create views created with either of these definitions!
* A few error messages related to wrong conversions are different as MariaDB\
  provides more information in the message about what went wrong.
* Error numbers for MariaDB-specific errors have been moved to start from 1900 so as not to conflict with MySQL errors.
* Microseconds now work in all contexts; MySQL, in some contexts, lost the microsecond part from datetime and time.
* [UNIX\_TIMESTAMP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/unix_timestamp)(constant-date-string) returns a timestamp with 6 decimals in MariaDB while MySQL returns it without a decimal. This can cause a problem if you are using UNIX\_TIMESTAMP() as a partitioning function. You can fix this by using [FLOOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/floor)(UNIX\_TIMESTAMP(..)) or changing the date string to a date number, like 20080101000000.
* MariaDB performs stricter checking of date, datetime and timestamp values. For example [UNIX\_TIMESTAMP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/unix_timestamp)('x') now returns NULL instead of 0.
* The old `--maria-` startup options are removed. You should use\
  the `--aria-` prefix instead. ([MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) supports both `--maria-`\
  and `--aria-`)
* [SHOW PROCESSLIST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-processlist) has an extra `Progress` column\
  which shows progress for some commands. You can disable it by\
  starting `mysqld` with either `--old-mode=NO_PROGRESS_INFO` or with the `--old` flag (see [OLD\_MODE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/old-mode)).
* `INFORMATION_SCHEMA.PROCESSLIST` has three new columns for progress\
  reporting: `STAGE`, `MAX_STAGE`, and `PROGRESS`.
* [Long comments](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/comment-syntax) which start with `/*M!`\
  or `/*M!#####` are executed.
* If you use [max\_user\_connections=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_user_connections) (which means any number of connections) when starting mysqld, you can't change the global variable anymore while mysqld remains running. This is because when mysqld is started with `max_user_connections=0` it does not allocate counting\
  structures (which also involve a mutex for each connection). This would lead to wrong counters if you later changed the variable. If you want to be able to change this variable at runtime, set it to a high value at startup.
* You can set `max_user_connections` (both the global variable and the `GRANT` option) to `-1` to stop users from connecting to the server. The global `max_user_connections` variable does not affect users with the `SUPER` privilege.
* The [IGNORE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/ignore) directive does not ignore all errors (like fatal errors), only things that are safe to ignore.

### Incompatibilities between [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) and MySQL 5.1

The list is the same as between [MariaDB 5.1](../../old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) and MySQL 5.1, with one addition:

* A new [SQL\_MODE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode) value was added:`IGNORE_BAD_TABLE_OPTIONS`. If it is not set, using a table,\
  field, or index attribute (option) that is not supported by the chosen storage engine will cause an error. This change might cause warnings in the error log about incorrectly defined tables from the `mysql` database, fix that with [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade).

For all practical purposes, [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) is a drop in replacement for [MariaDB 5.1](../../old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) and MySQL 5.1.

### Incompatibilities between [MariaDB 5.1](../../old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) and MySQL 5.1

In some few cases MariaDB has to be incompatible to allow MariaDB to provide more and better information than MySQL.

Here is the list of all known user level incompatibilities you may see when using [MariaDB 5.1](../../old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) instead of MySQL 5.1.

* The installation package names start with MariaDB instead of MySQL.
* Timings may be different as MariaDB is in many cases faster than MySQL.
* mysqld in MariaDB also reads the `[mariadb]` sections of your\
  my.cnf files.
* You can't use a binary only storage engine library with MariaDB if it's not compiled for exactly the same MariaDB version. (This is because the server internal structure THD is different between MySQL and MariaDB. This is common also between different MySQL versions). This should not be a problem as most people don't load new storage engines and MariaDB comes with [more storage engines](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines) than MySQL.
* `CHECKSUM TABLE` may give different result as MariaDB doesn't ignore NULLs in the columns as MySQL 5.1 does (Future MySQL versions should calculate checksums the same way as MariaDB). You can get the 'old style' checksum in MariaDB by starting mysqld with the `--old` option. Note however that that the MyISAM and Aria storage engines in MariaDB are using the new checksum\
  internally, so if you are using `--old`, the `CHECKSUM` command will be slower as it needs to calculate the checksum row by row.
* The slow query log has [more information](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/slow-query-log-extended-statistics) about the query, which may be a problem if you have a script which parses the slow query log.
* MariaDB by default takes a bit more memory than MySQL because we have by default enabled the [Aria storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) for handling internal temporary tables. If you need MariaDB to take very little\
  memory (at the expense of performance), you can set the value of `aria_pagecache_buffer_size` to `1M` (the default is `128M`).
* If you are using [new command options](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files),[new features of MariaDB](mariadb-vs-mysql-features.md) or [new storage engines](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines), you can't move easily back and forth between MySQL and MariaDB anymore.

## Old, Unsupported Configuration Options

If you are using any of the following options in your `/etc/my.cnf` or other`my.cnf` file you should remove them. This is also true for MySQL 5.1 or newer:

* `skip-bdb`

## Replacing a MySQL RPM

If you uninstalled a MySQL RPM to install MariaDB, note that the MySQL RPM on uninstall renames `/etc/my.cnf` to `/etc/my.cnf.rpmsave`.

After installing MariaDB you should do the following to restore your old\
configuration options:

```bash
mv -vi /etc/my.cnf.rpmsave /etc/my.cnf
```

## Incompatibilities between MariaDB and MySQL-Proxy

A MySQL client API is able to connect to MariaDB using MySQL-Proxy but a MariaDB client API will receive progress reporting information that MySQL-Proxy does not implement, to get full compatibility in all case just disable progress reporting on the client or server side.

Another option is to use the [MariaDB MaxScale proxy](https://app.gitbook.com/s/JqgUabdZsoY5EiaJmqgn/mariadb-faqs/database-proxies-and-routers), that works with both MySQL and MariaDB.

## Related Links

* [MariaDB vs MySQL - Features](mariadb-vs-mysql-features.md)
* [Moving from MySQL to MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql)
* [Troubleshooting Installation Issues](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues)
* [Projects and applications that work with MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/server-client-software/applications-supporting-mariadb)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
