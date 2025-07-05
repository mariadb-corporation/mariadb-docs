# Release Notes for MariaDB Enterprise Server 10.5.18-13

MariaDB Enterprise Server 10.5.18-13 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.5. This release includes a variety of fixes.

MariaDB Enterprise Server 10.5.18-13 was released on 2022-12-21.

## Backported Features

MariaDB Enterprise Server enables a predictable development and operations experience through an enterprise lifecycle. These new features have been backported after reaching maturity in MariaDB Community Server:

* The new [slave\_max\_statement\_time system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is available to set the maximum execution time for queries on replica nodes. (MENT-1566, [MDEV-27161](https://jira.mariadb.org/browse/MDEV-27161))
  * When a query takes more than `slave_max_statement_time` seconds to run on the replica (slave) node, the query is aborted, and replication stops with an error.
  * The system variable can be set to a decimal value, where the decimal component has microsecond precision.
  * When set to `0`, there is no timeout.
  * The default value is `0`.

## Notable Changes

* The [information\_schema.INNODB\_SYS\_TABLESPACES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tablespaces-table) view shows details about the InnoDB temporary tablespace, which is the tablespace where InnoDB temporary tables are stored. ([MDEV-29479](https://jira.mariadb.org/browse/MDEV-29479))
  * Starting with this release, the details about the InnoDB temporary tablespace can be shown by querying for the name `innodb_temporary`:

```sql
SELECT * FROM information_schema.INNODB_SYS_TABLESPACES
 WHERE name LIKE 'innodb_temporary';
```

* When a table's default collation is set to the default collation for the table's character set, [SHOW CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-table) shows the `COLLATE` clause. ([MDEV-29446](https://jira.mariadb.org/browse/MDEV-29446))
  * In previous releases, MariaDB Enterprise Server reduced the size of `SHOW CREATE TABLE` output by excluding the `COLLATE` clause if the table's default collation was set to the default collation for the table's character set.

## Issues Fixed

### Can result in data loss

* When a column is renamed in a partitioned table with [ALTER TABLE .. RENAME COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) using the [NOCOPY algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-nocopy-alter-algorithm), the table can be corrupted. ([MDEV-28576](https://jira.mariadb.org/browse/MDEV-28576))
* When the InnoDB storage engine performs change buffer operations, the [InnoDB Redo Log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-redo-log) can overflow, which can cause table corruption. (MENT-1661, [MDEV-29905](https://jira.mariadb.org/browse/MDEV-29905))

### Can result in a hang or crash

* When a query contains an `IN/ALL/ANY` predicand and the subquery contains a GROUP BY clause with an `IN/ALL/ANY` predicand with a single-value subquery as the left operand, the server can crash. ([MDEV-29350](https://jira.mariadb.org/browse/MDEV-29350))
* If an InnoDB table contains a foreign key constraint and the child table's `DATABASE_NAME/TABLE_NAME.ibd` is longer than 330 characters, when the parent table is renamed, the server can crash. ([MDEV-29409](https://jira.mariadb.org/browse/MDEV-29409))
* When a DDL statement is executed using the [INPLACE algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-inplace-alter-algorithm) and [innodb\_adaptive\_hash\_index=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_adaptive_hash_index) is set, the server can hang. ([MDEV-27700](https://jira.mariadb.org/browse/MDEV-27700), [MDEV-29384](https://jira.mariadb.org/browse/MDEV-29384))
* When renaming a table to a long name, the server can crash. ([MDEV-29258](https://jira.mariadb.org/browse/MDEV-29258))
* When an [ALTER TABLE statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) causes InnoDB to rebuild a table with a spatial index, the server can crash. ([MDEV-29520](https://jira.mariadb.org/browse/MDEV-29520))
* When an InnoDB temporary table contains a spatial index, the server can crash if the temporary table is dropped due to `DROP TEMPORARY TABLE` or client disconnect. ([MDEV-29507](https://jira.mariadb.org/browse/MDEV-29507))
* When querying a partitioned table using the `PARTITION` syntax, if the `WHERE` clause results in an index merge, the server can crash. ([MDEV-21134](https://jira.mariadb.org/browse/MDEV-21134))
* When detecting CTE dependencies of nested CTEs that includes one or more recursive CTEs, infinite recursion can occur until the server crashes. ([MDEV-29361](https://jira.mariadb.org/browse/MDEV-29361))
* When the [wsrep\_notify\_cmd system variable](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_notify_cmd) is configured to use the bundled `wsrep_notify.sh` script, the server can hang during startup. ([MDEV-27682](https://jira.mariadb.org/browse/MDEV-27682))
* When selecting from InnoDB's [information\_schema views](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/views/information-schema-views-table) (such as [INNODB\_TRX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_trx-table), [INNODB\_LOCKS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_locks-table), and [INNODB\_LOCK\_WAITS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_lock_waits-table)), if connections with open XA transactions are disconnected or killed at the same time, the server can crash. ([MDEV-29575](https://jira.mariadb.org/browse/MDEV-29575))
* For some queries that involve tables with different but convertible character sets for columns taking part in the query, a repeatable execution of such queries in the prepared statement mode or as part of a stored routine can crash the server. ([MDEV-16128](https://jira.mariadb.org/browse/MDEV-16128))
* When executing a `SELECT .. UNION .. SELECT` or [EXPLAIN EXTENDED](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/EXPLAIN-EXTENDED/README.md) statement, the server can crash. ([MDEV-23160](https://jira.mariadb.org/browse/MDEV-23160))
* When [optimizer\_switch='condition\_pushdown\_for\_derived=on'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#optimizer_switch) is set and a view that includes a subquery is queried, the server crashes. ([MDEV-16549](https://jira.mariadb.org/browse/MDEV-16549))
* When an application-time period with an empty name is added to a table using [ALTER TABLE .. ADD PERIOD IF NOT EXISTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table), the server can crash. ([MDEV-18873](https://jira.mariadb.org/browse/MDEV-18873))
  * In previous releases, statements like the following could cause the server to crash:

```sql
ALTER TABLE t
 ADD PERIOD IF NOT EXISTS FOR `` (s,e);
```

* When the Spider storage engine's ODBC foreign data wrapper is used with MariaDB Connector/ODBC 3.1.10 and later, the server can crash. (MENT-1415)
* If the InnoDB change buffer is corrupted, the server can hang during shutdown. (MENT-1673, [MDEV-30009](https://jira.mariadb.org/browse/MDEV-30009))
* When an InnoDB tablespace is in the non-canonical format from a previous [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) operation that used the [INSTANT algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-instant-alter-algorithm), InnoDB can fail to apply changes to the table during crash recovery and while preparing a backup with [MariaDB Enterprise Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup). ([MDEV-29438](https://jira.mariadb.org/browse/MDEV-29438))
* When InnoDB tries to apply a `INSERT_HEAP_DYNAMIC`record to a secondary index in a table with [ROW\_FORMAT=DYNAMIC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_default_row_format) during crash recovery, the operation can fail with an error. ([MDEV-29559](https://jira.mariadb.org/browse/MDEV-29559))
  * In previous releases, the [MariaDB ES error log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log) could have errors like the following:

```
[ERROR] InnoDB: Not applying INSERT_HEAP_DYNAMIC due to corruption on [page id: space=5, page number=4]
```

* When a prepared statement is used to execute an [INSERT .. RETURNING statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insertreturning) containing a subquery, the server can crash: ([MDEV-28740](https://jira.mariadb.org/browse/MDEV-28740))

### Can result in unexpected behavior

* In the presence of replication filters, revoking privileges from a non-existing user on a primary (master) breaks replication on the replica (slave). ([MDEV-28530](https://jira.mariadb.org/browse/MDEV-28530))
* When [replicate\_wild\_ignore\_table='mysql.%'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is set on a replica node, the replica node does not skip replicated [SET DEFAULT ROLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/set-default-role) statements. ([MDEV-28294](https://jira.mariadb.org/browse/MDEV-28294))
* When a Spider table has a prefix index, query results can be incorrect. ([MDEV-27172](https://jira.mariadb.org/browse/MDEV-27172))
* InnoDB can extend tablespace files when additional capacity is not required. ([MDEV-13013](https://jira.mariadb.org/browse/MDEV-13013))
* When an InnoDB table is being rebuilt and a [BLOB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/blob) is updated during the online rebuild, a memory leak can occur. ([MDEV-29600](https://jira.mariadb.org/browse/MDEV-29600))
* When a view is queried using a prepared statement, the query fails with the [ER\_NEED\_REPREPARE error code](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1600-to-1699/e1615). ([MDEV-17124](https://jira.mariadb.org/browse/MDEV-17124))
  * In previous releases, the following error would occur:

```
ERROR 1615 (HY000): Prepared statement needs to be re-prepared
```

* When an InnoDB table contains virtual generated columns that are indexed, InnoDB fails to purge secondary index records. ([MDEV-29666](https://jira.mariadb.org/browse/MDEV-29666))
* When using the InnoDB adaptive hash index, non-locking reads can return wrong results due to a potential ACID violation. ([MDEV-28709](https://jira.mariadb.org/browse/MDEV-28709), [MDEV-29635](https://jira.mariadb.org/browse/MDEV-29635), [MDEV-27927](https://jira.mariadb.org/browse/MDEV-27927))
* When [SHOW COLUMNS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-columns) is used on a temporary table, an empty result set is returned. ([MDEV-28455](https://jira.mariadb.org/browse/MDEV-28455))
* When a sequence is used as the default value in a table, rows inserted by an `INSERT ... SELECT` statement can be assigned the wrong values. ([MDEV-29540](https://jira.mariadb.org/browse/MDEV-29540))
* When a column has both a [UNIQUE index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations) and a [FULLTEXT index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations), full-text search using `MATCH(..) AGAINST(..)` does not work properly. ([MDEV-29778](https://jira.mariadb.org/browse/MDEV-29778))
* If the server is started with the [--ssl option](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#-ssl) enabled, but the TLS certificates and keys are not configured, the server will advertise the TLS support in the handshake, but will not actually be able to use it. ([MDEV-29811](https://jira.mariadb.org/browse/MDEV-29811))
* With MariaDB Enterprise Cluster, when [wsrep\_sst\_method='mariadb-backup'](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) is configured, the joiner node ignores custom values for the [innodb\_buffer\_pool\_filename system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename), and the SST copies the buffer pool file to the default location instead. ([MDEV-28968](https://jira.mariadb.org/browse/MDEV-28968))
* When a [TIMESTAMP column](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/timestamp) is filtered in a subquery inside the [ALL operator](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-and-all), the results can be incorrect. ([MDEV-27101](https://jira.mariadb.org/browse/MDEV-27101))
* When the [wsrep\_node\_incoming\_address system variable](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_node_incoming_address) does not contain a port number, the [wsrep\_incoming\_addresses status variable](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables) shows 0 as the port number. ([MDEV-28868](https://jira.mariadb.org/browse/MDEV-28868))
* When [optimizer\_switch='rowid\_filter=on'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#optimizer_switch) is enabled, performance is impacted if the `rowid` filter contains no elements. ([MDEV-28846](https://jira.mariadb.org/browse/MDEV-28846))
* When a [INET6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/inet6) column is filtered in a subquery inside the [ALL operator](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-and-all), the results can be incorrect. ([MDEV-27099](https://jira.mariadb.org/browse/MDEV-27099))
* When `XA COMMIT` is executed without an open XA transaction, the operation is still logged to the binary log. ([MDEV-25616](https://jira.mariadb.org/browse/MDEV-25616))
  * In previous releases, when a replica node tried to apply the event, it would fail with the [ER\_XAER\_NOTA error code](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1300-to-1399/e1397):

```
Last_SQL_Errno	1397
Last_SQL_Error	Error 'XAER_NOTA: Unknown XID' on query. Default database: 'DATABASE_NAME'. Query: 'XA COMMIT ..'
```

* When a tablespace file was originally built with MariaDB Enterprise Server 10.4 and earlier, InnoDB would refuse to add a column to the table using the [INSTANT algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-instant-alter-algorithm). ([MDEV-28822](https://jira.mariadb.org/browse/MDEV-28822))
  * In previous releases, the operation would fail with the following error message:

```
ERROR 1845 (0A000): ALGORITHM=INSTANT is not supported for this operation. Try ALGORITHM=INPLACE
```

### Related to install and upgrade

* When [mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup) is executed, spurious errors about table rebuilds are logged. ([MDEV-29481](https://jira.mariadb.org/browse/MDEV-29481))
  * In previous releases, the following messages would be logged, even though the tool already mitigated the issues itself:

```
error: Table rebuild required. Please do "ALTER TABLE `TABLE_NAME` FORCE" or dump/reload to fix it!"
```

### Changes in Storage Engines

* This release incorporates MariaDB ColumnStore storage engine version 5.6.8.

## Interface Changes

* [ER\_BINLOG\_UNSAFE\_SKIP\_LOCKED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4175) error code added
* [ER\_CM\_OPTION\_MISSING\_REQUIREMENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4191) error code added
* [ER\_INCONSISTENT\_SLAVE\_TEMP\_TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4188) error code added
* [ER\_JSON\_HISTOGRAM\_PARSE\_FAILED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4186) error code added
* [ER\_JSON\_TABLE\_ALIAS\_REQUIRED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4177) error code added
* [ER\_JSON\_TABLE\_ERROR\_ON\_FIELD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4176) error code added
* [ER\_JSON\_TABLE\_MULTIPLE\_MATCHES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4179) error code added
* [ER\_JSON\_TABLE\_SCALAR\_EXPECTED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4178) error code added
* [ER\_PARTITION\_CONVERT\_SUBPARTITIONED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4184) error code added
* [ER\_PK\_INDEX\_CANT\_BE\_IGNORED](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4174) error code added
* [ER\_PROVIDER\_NOT\_LOADED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4185) error code added
* [ER\_REMOVED\_ORPHAN\_TRIGGER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4181) error code added
* [ER\_SF\_OUT\_INOUT\_ARG\_NOT\_ALLOWED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4187) error code added
* [ER\_SLAVE\_STATEMENT\_TIMEOUT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4192) error code added
* [ER\_STORAGE\_ENGINE\_DISABLED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4182) error code added
* [ER\_VERS\_HIST\_PART\_FAILED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4189) error code added
* [ER\_WITH\_TIES\_NEEDS\_ORDER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4180) error code added
* [mariadbd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) --slave-max-statement-time command-line option added
* [slave\_max\_statement\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) system variable added
* [WARN\_OPTION\_CHANGING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4190) error code added
* [WARN\_SFORMAT\_ERROR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4183) error code added

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.5.18-13 is provided for:

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

## Installation Instructions

* [MariaDB Enterprise Server ](../11-4/whats-new-in-mariadb-enterprise-server-11-4.md)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.5](../11-4/whats-new-in-mariadb-enterprise-server-11-4.md)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage) [and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore 23.02 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 23.02 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-from-to-specific-versions/upgrading-from-mariadb-10-5-to-mariadb-10-6)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
