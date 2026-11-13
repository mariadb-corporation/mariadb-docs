# Incompatibilities and Feature Differences Between MariaDB 10.3 and MySQL 5.7

MariaDB maintains high levels of compatibility with MySQL, and most applications that use MySQL will work seamlessly with MariaDB. However, take note of the following incompatibilities and feature differences between [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) and MySQL 5.7

## Storage Engines

In addition to the standard [InnoDB](../../../server-usage/storage-engines/innodb/README.md), [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/README.md), [BLACKHOLE](../../../server-usage/storage-engines/blackhole.md), [CSV](../../../server-usage/storage-engines/csv/README.md), [MEMORY](../../../server-usage/storage-engines/memory-storage-engine.md), [ARCHIVE](../../../server-usage/storage-engines/archive.md), and [MERGE](../../../server-usage/storage-engines/merge.md) storage engines, the following are also available with [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103):

* [MyRocks](../../../server-usage/storage-engines/myrocks/README.md), a storage engine with great compression
* [Aria](../../../server-usage/storage-engines/aria/README.md), MyISAM replacement with better caching.
* TokuDB
* [CONNECT](../../../server-usage/storage-engines/connect/README.md)
* [SEQUENCE](../../../server-usage/storage-engines/sequence-storage-engine.md)
* [SphinxSE](../../../server-usage/storage-engines/sphinx-storage-engine/README.md)
* [Spider](../../../server-usage/storage-engines/spider/README.md)
* [FederatedX](../../../server-usage/storage-engines/federatedx-storage-engine/README.md) (drop-in replacement for Federated)
* [OQGRAPH](../../../server-usage/storage-engines/oqgraph-storage-engine/README.md)

## Speed Improvements

* Many optimizer enhancements. [Subqueries](../../../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/README.md) are more usable.\
  The complete list and a comparison with MySQL is [here](../optimizer-feature-comparison-matrix.md).
* [Instant ADD COLUMN](../../../server-usage/storage-engines/innodb/innodb-online-ddl/instant-add-column-for-innodb.md)
* [DDL Fast Fail - WAIT/NOWAIT](../../../reference/sql-statements/transactions/wait-and-nowait.md)
* Faster and safer replication:[Group commit for the binary log](../../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md). This makes many setups that use replication and lots of updates [more than 2x times faster](https://www.facebook.com/note.php?note_id=10150211546215933).
* Improvements for Innodb asynchronous IO subsystem on Windows.
* [Segmented Key Cache](../../../ha-and-performance/optimization-and-tuning/system-variables/segmented-key-cache.md) for MyISAM. Can speed up MyISAM tables with up to 4x
* [Adjustable hash size](../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_file_hash_size) for MyISAM and Aria. This can greatly improve shutdown time (from hours to minutes) if you are using a lot of MyISAM/Aria tables with delayed keys.
* [CHECKSUM TABLE](../../../reference/sql-statements/table-statements/checksum-table.md) is faster.
* We improved the performance of character set conversions (and removed conversions when they were not really needed).\
  Overall speed improvement is 1-5 % (according to sql-bench) but can be higher for big result sets with all characters between 0x00-0x7f.
* [MariaDB Thread pool](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md) allows MariaDB to run with 200,000+ connections and with a notable speed improvement when using many connections.
* Lots of speed improvements when a client connects to MariaDB.
* There are some improvements to the DBUG code to make its execution faster when debug is compiled in but not used.
* Our use of the Aria storage engine enables faster complex queries (queries which normally use disk-based temporary tables). The [Aria](../../../server-usage/storage-engines/aria/README.md) storage engine is used for internal temporary tables, which should give a speedup when doing complex selects. Aria is usually faster for temporary tables when compared to MyISAM because Aria caches row data in memory and normally doesn't have to write the temporary rows to disk.
* The test suite has been extended and faster than before, even though it tests more things.

## Extensions and New Features

We've added a lot of new features to MariaDB. If a patch or feature is useful, safe, and stable — we make every effort to include it in MariaDB. The most notable features are:

* [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) is a standard part of MariaDB Server.
* [System-versioned tables](../../../reference/sql-structure/temporal-tables/system-versioned-tables.md) (also known as AS OF)
* [DML-only flashback](../../../server-management/server-monitoring-logs/binary-log/flashback.md), allowing instances, databases or tables to be rolled back to an old snapshot.
* [Oracle compatibility mode](../sql_modeoracle.md)
* [Sequences](../../../reference/sql-structure/sequences/README.md)
* [Invisible Columns](../../../reference/sql-statements/data-definition/create/invisible-columns.md)
* [Table Value Constructors](../../../reference/sql-structure/sql-language-structure/table-value-constructors.md)
* [Semi-sync plugin](../../../ha-and-performance/standard-replication/semisynchronous-replication.md) merged into the server
* [INTERSECT](../../../reference/sql-statements/data-manipulation/selecting-data/set-operations/intersect.md) and [EXCEPT](../../../reference/sql-statements/data-manipulation/selecting-data/set-operations/except.md).
* [PROXY protocol support](../../../clients-and-utilities/server-client-software/client-libraries/proxy-protocol-support.md)
* [Window functions](../../../reference/sql-functions/special-functions/window-functions/README.md)
* Number of supported decimals in [DECIMAL](../../../reference/data-types/numeric-data-types/decimal.md) has increased from `30` to `38`
* [Recursive Common Table Expressions](../../../reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/recursive-common-table-expressions-overview.md)
* New [WITH](../../../reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/with.md) statement. `WITH` is a common table expression that allows you to refer to a subquery expression many times in a query.
* [CHECK CONSTRAINT](../../../reference/sql-statements/data-definition/constraint.md)
* [DEFAULT expression](../../../reference/sql-statements/data-definition/create/create-table.md#default-column-option), including `DEFAULT` for [BLOB](../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../reference/data-types/string-data-types/text.md)
* Added catchall for [list partitions](../../../server-usage/partitioning-tables/partitioning-types/list-partitioning-type.md)
* Oracle-style [EXECUTE IMMEDIATE](../../../reference/sql-statements/prepared-statements/execute-immediate.md) statement
* Lots of new [JSON functions](../../../reference/sql-functions/special-functions/json-functions/README.md)
* [Microsecond Precision in Processlist](../../../reference/system-tables/information-schema/time_ms-column-in-information_schemaprocesslist.md)
* [Table Elimination](../../../ha-and-performance/optimization-and-tuning/query-optimizations/table-elimination/README.md)
* [Virtual Columns](../../../reference/sql-statements/data-definition/create/generated-columns.md)
* [Extended User Statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md)
* [KILL all queries for a user](../../../reference/sql-statements/administrative-sql-statements/kill.md)
* [KILL QUERY ID - terminates the query by query\_id, leaving the connection intact](../../../reference/sql-statements/administrative-sql-statements/kill.md)
* [Pluggable Authentication](../../../reference/plugins/authentication-plugins/pluggable-authentication-overview.md)
* [Storage-engine-specific CREATE TABLE](../../../reference/product-development/plugin-development/storage-engines-storage-engine-development/engine-defined-new-tablefieldindex-attributes.md)
* [Enhancements to INFORMATION SCHEMA.PLUGINS table](../../../reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [Group commit for the binary log](../../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md). This makes [replication notably faster!](https://www.facebook.com/note.php?note_id=10150261692455933)
* The binary log in MariaDB [can be compressed](../../../server-management/server-monitoring-logs/binary-log/compressing-events-to-reduce-size-of-the-binary-log.md).
* [Progress reporting](../../../reference/product-development/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting.md) for [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/README.md) and [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)
* Faster [joins and subqueries](../../../reference/sql-structure/joins-subqueries-set.md)
* [HandlerSocket](../../../reference/sql-structure/nosql/handlersocket/README.md) and faster [HANDLER](../../../reference/sql-structure/nosql/handler/README.md) calls
* [Dynamic Columns](../../../reference/sql-structure/nosql/dynamic-columns.md) support
* [SHOW EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/show/show-explain.md) gives the EXPLAIN plan for a query running in another thread. MySQL introduced the EXPLAIN FOR CONNECTION syntax to do the same thing.
* [Roles](../../../security/user-account-management/roles/README.md)
* [PCRE Regular Expressions](../../../reference/sql-functions/string-functions/regular-expressions-functions/pcre.md) (including [REGEXP\_REPLACE()](../../../reference/sql-functions/string-functions/regular-expressions-functions/regexp_replace.md))
* OR REPLACE syntax for [CREATE](../../../reference/sql-statements/data-definition/create/README.md) statements, such as [CREATE OR REPLACE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md#create-or-replace), [CREATE OR REPLACE DATABASE](../../../reference/sql-statements/data-definition/create/create-database.md#or-replace), etc.
* [DELETE ... RETURNING](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md)
* MariaDB [supports expressions](../../../reference/sql-statements/data-definition/create/create-table.md#default-column-option) in the DEFAULT clause, while MySQL does not.
* MariaDB [supports more collations](../../../reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations.md) than MySQL, including `NO PAD` collations.
* MariaDB supports Spatial Reference System IDs for spatial data type columns with [REF\_SYSTEM\_ID](../../../reference/sql-statements/data-definition/create/create-table.md#ref_system_id).

## Incompatibilities

When upgrading from MySQL 5.7 to [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103), please take note of the following incompatibilities:

* For a list of function differences, see [Function Differences Between MariaDB 10.3 and MySQL 5.7](../function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-and-mysql-unmaintained-series/function-differences-between-mariadb-103-and-mysql-57.md)
* For a list of system variable differences, see [System Variable Differences Between MariaDB 10.3 and MySQL 5.7](../system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-10-3-and-mysql-5-7.md)
* MariaDB binaries (`mysqld`, [myisamchk](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) etc.) give a warning if one uses a unique prefix of an option (such as `--big-table` instead of `--big-tables`). MySQL binaries require the full option name.
* MariaDB's GTID is not compatible with MySQL's. This means that one can't have MySQL 5.7 as a slave for [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103). However [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) can be a slave of MySQL 5.7 or any earlier MySQL/MariaDB version. Note that MariaDB and MySQL also have different [GTID system variables](../../../ha-and-performance/standard-replication/gtid/gtid-system-variables.md), so these need to be adjusted when migrating.
* To make CREATE TABLE ... SELECT work the same way in statement based and row based replication it's by default executed as [CREATE OR REPLACE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md#create-or-replace) on the slave. One benefit of this is that if the slave dies in the middle of CREATE ... SELECT it will be able to continue.
  * One can use the [slave-ddl-exec-mode](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) variable to specify how `CREATE TABLE` and `DROP TABLE` is replicated.
* MySQL has the [performance schema](../../../reference/system-tables/performance-schema/README.md) enabled by default. For performance reasons [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) has it disabled by default. You can enable it by starting `mysqld` with the option `--performance-schema`.
* MySQL 5.7 features a new implementation of the performance\_schema and a sys schema wrapper. These are not yet supported in MariaDB.
* [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) implements [InnoDB encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-tde-fundamentals.md) in a different way to MySQL 5.7.
* [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) does not support [CREATE TABLESPACE](../../../reference/sql-statements/data-definition/create/create-tablespace.md) for InnoDB.
* The OVER, ROWS and RECURSIVE keywords are [reserved words](../../../reference/sql-structure/sql-language-structure/reserved-words.md) in [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103), but not in MySQL 5.7. Note that in MySQL 8.0 these are also reserved words.
* MariaDB stores [JSON](../../../reference/sql-functions/special-functions/json-functions/README.md) as true text, not in binary format as MySQL. MariaDB's JSON functions are much faster than MySQL's so there is no need to store in binary format, which would add complexity when manipulating JSON objects.
* For the same reason, MariaDB's [JSON data type](../../../reference/data-types/string-data-types/json.md) is an alias for [LONGTEXT](../../../reference/data-types/string-data-types/longtext.md). If you want to replicate JSON columns from MySQL to MariaDB, you should store JSON objects in MySQL in a TEXT or LONGTEXT column or use statement based replication. If you are using JSON columns and want to upgrade to MariaDB, you need to either convert them to TEXT or use mysqldump to copy these tables to MariaDB.
* In MySQL, JSON is compared according to json values. In MariaDB JSON strings are normal strings and compared as strings.
* [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) does not support MySQL's JSON operators (`->` and `->>`) ([MDEV-13594](https://jira.mariadb.org/browse/MDEV-13594))
* [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) supports the standard by producing null and a warning for [JSON\_SEARCH](../../../reference/sql-functions/special-functions/json-functions/json_search.md) when given invalid data, while MySQL produces an error.
* [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) does not support the ngram and MeCab full-text parser plugins - [MDEV-10267](https://jira.mariadb.org/browse/MDEV-10267), [MDEV-10268](https://jira.mariadb.org/browse/MDEV-10268).
* [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) does not support the [MySQL X plugin](https://dev.mysql.com/doc/refman/5.7/en/x-plugin.html).
* [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) does not support MySQL 5.7's “native” InnoDB partitioning handler.
* [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) does not support MySQL 5.7's ALTER TABLE...RENAME INDEX statements.
* MySQL's implementation of [aborting statements that exceed a certain time to execute](../../../ha-and-performance/optimization-and-tuning/query-optimizations/aborting-statements.md) can only kill SELECTs, while MariaDB's can kill any queries (excluding stored procedures).
* [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) does not support MySQL's `SELECT MAX_STATEMENT_TIME = N ...` for MySQL older than 5.7.8 or `SELECT /*+ MAX_EXECUTION_TIME(n) */ ...` for MySQL 5.7.8 and higher - see [Aborting Statements that Exceed a Certain Time to Execute](../../../ha-and-performance/optimization-and-tuning/query-optimizations/aborting-statements.md).
* The MySQL version of [max\_statement\_time](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_statement_time) is defined in milliseconds, not seconds.
* [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) does not support the MySQL Memcached plugin. However, data stored using memcached can be retrieved because the data is stored as InnoDB tables. MariaDB is able to start successfully with an error message of not being able to find libmemcached.so library.
* Users created with MySQL's SHA256 password algorithm cannot be used in [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) - [MDEV-9804](https://jira.mariadb.org/browse/MDEV-9804).
* [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) doesn't support user [ACCOUNT LOCKs](../../../security/user-account-management/account-locking.md) or [PASSWORD EXPIRE](../../../security/user-account-management/user-password-expiry.md) (MariaDB 10.4 does)
* In MySQL, `X'HHHH'`, the standard SQL syntax for binary string literals, erroneously works in the same way as `0xHHHH`, which could work as a number or string depending on the context. In MariaDB, this has been fixed to behave as a string in all contexts (and never as a number). See [CAST](../../../reference/sql-functions/string-functions/cast.md) and [Hexadecimal Literals](../../../reference/sql-structure/sql-language-structure/hexadecimal-literals.md) for more details and examples.
* In [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103), [SHOW CREATE TABLE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) does not quote the DEFAULT value of an integer. Older versions of MariaDB, and MySQL, do. Since [MariaDB 10.3]({release-notes}/community-server/old-releases/10.3/what-is-mariadb-103) can support defaults for [BLOB](../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../reference/data-types/string-data-types/text.md) fields, while MySQL does not, [SHOW CREATE TABLE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) will also append `DEFAULT NULL` where no default is explicitly provided to nullable BLOB or TEXT fields in MariaDB.
* Since MariaDB [supports expressions](../../../reference/sql-statements/data-definition/create/create-table.md#default-column-option) in the DEFAULT clause, in MariaDB, the [INFORMATION\_SCHEMA.COLUMNS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-columns-table.md) table contains extra fields, and also quotes the DEFAULT value of a string in the `COLUMN_DEFAULT` field in order to distinguish it from an expression.
* Since MariaDB supports [INTERSECT](../../../reference/sql-statements/data-manipulation/selecting-data/set-operations/intersect.md) and [EXCEPT](../../../reference/sql-statements/data-manipulation/selecting-data/set-operations/except.md), these are both [reserved words](../../../reference/sql-structure/sql-language-structure/reserved-words.md) and can't be used as an [identifier](../../../reference/sql-structure/sql-language-structure/identifier-names.md) without being quoted.
* As a result of implementing [Table Value Constructors](../../../reference/sql-structure/sql-language-structure/table-value-constructors.md), the [VALUES function](../../../reference/sql-functions/secondary-functions/miscellaneous-functions/values-value.md) has been renamed to VALUE().
* MariaDB does not support the optional init\_vector argument for [AES\_ENCRYPT](../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_encrypt.md) and [AES\_DECRYPT](../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_decrypt.md) or the block\_encryption\_mode variable - [MDEV-9069](https://jira.mariadb.org/browse/MDEV-9069)
* MariaDB does not support the `--initialize` option. Use mysql\_install\_db instead. - [MDEV-19010](https://jira.mariadb.org/browse/MDEV-19010)
* Not all [character sets and collations](../../../reference/data-types/string-data-types/character-sets/README.md) are [supported](../../../reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations.md) across both MySQL and MariaDB. As of 10.3.24, MariaDB supports 40 character sets and 322 collations. As of 5.7.29, MySQL supports 41 character sets (`gb18030` being the additional one) and 222 collations.
* The MySQL binary log includes the thread\_id, while MariaDB's [binary log](../../../server-management/server-monitoring-logs/binary-log/README.md) does not. ([MDEV-7850](https://jira.mariadb.org/browse/MDEV-7850))
* Also see [Incompatibilities between MariaDB 10.2 and MySQL 5.7](incompatibilities-and-feature-differences-between-mariadb-10-2-and-mysql-5.md) and Incompatibilities between MariaDB 10.1 and MySQL 5.7.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
