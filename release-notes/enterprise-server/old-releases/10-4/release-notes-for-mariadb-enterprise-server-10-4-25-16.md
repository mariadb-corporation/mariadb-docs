# Release Notes for MariaDB Enterprise Server 10.4.25-16

MariaDB Enterprise Server 10.4.25-16 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4. This release includes a variety of fixes.

MariaDB Enterprise Server 10.4.25-16 was released on 2022-06-13.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2022-27458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27458)                                                                                               | 7.5             |
| [CVE-2022-27457](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27457)                                                                                               | 7.5             |
| [CVE-2022-27456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27456)                                                                                               | 7.5             |
| [CVE-2022-27455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27455)                                                                                               | 7.5             |
| [CVE-2022-27452](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27452)                                                                                               | 7.5             |
| [CVE-2022-27451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27451)                                                                                               | 7.5             |
| [CVE-2022-27449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27449)                                                                                               | 7.5             |
| [CVE-2022-27448](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27448)                                                                                               | 7.5             |
| [CVE-2022-27447](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27447)                                                                                               | 7.5             |
| [CVE-2022-27446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27446)                                                                                               | 7.5             |
| [CVE-2022-27445](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27445)                                                                                               | 7.5             |
| [CVE-2022-27444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27444)                                                                                               | 7.5             |
| [CVE-2022-27387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27387)                                                                                               | 7.5             |
| [CVE-2022-27386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27386)                                                                                               | 7.5             |
| [CVE-2022-27384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27384)                                                                                               | 7.5             |
| [CVE-2022-27383](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27383)                                                                                               | 7.5             |
| [CVE-2022-27382](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27382)                                                                                               | 7.5             |
| [CVE-2022-27381](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27381)                                                                                               | 7.5             |
| [CVE-2022-27380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27380)                                                                                               | 7.5             |
| [CVE-2022-27379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27379)                                                                                               | 7.5             |
| [CVE-2022-27378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27378)                                                                                               | 7.5             |
| [CVE-2022-27377](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27377)                                                                                               | 7.5             |
| [CVE-2022-27376](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27376)                                                                                               | 7.5             |
| [CVE-2022-21451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21451)                                                                                               | 7.5             |
| [CVE-2022-32088](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32088)                                                                                               | 6.5             |
| [CVE-2022-32087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32087)                                                                                               | 6.5             |
| [CVE-2022-32086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32086)                                                                                               | 6.5             |
| [CVE-2022-32085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32085)                                                                                               | 6.5             |
| [CVE-2022-32083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32083)                                                                                               | 6.5             |
| [CVE-2021-46669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46669)                                                                                               | 6.5             |
| [CVE-2022-21427](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21427)                                                                                               | 4.9             |

## Backported Features

* MariaDB Enterprise Server enables a predictable development and operations experience through an enterprise lifecycle. These new features have been backported after reaching maturity in MariaDB Community Server:
* [mariadb-dump option --as-of](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) reads data as of specific timestamp from system-versioned tables. (MENT-1457)
* Added [JSON\_EQUALS() function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_equals) to check JSON equality. (MENT-1452)
* Added [JSON\_NORMALIZE() function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_normalize) to normalize JSON values. (MENT-1456)
* Added [password\_reuse\_check password validation plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/password-reuse-check-plugin). (MENT-1451)
* Added Enterprise Spider ODBC support. (MENT-1092)
  * Spider now supports the ODBC wrapper in this release series which was previously supported in MariaDB Enterprise Server 10.5 and 10.6.
  * Spider/ODBC allows federated access to ODBC resources.

## Notable Changes

* Galera updated to 26.4.12
* Spider storage engine refuses attempts to create a temporary table since the engine cannot itself store data and cannot create temporary tables on a remote server. ([MDEV-28225](https://jira.mariadb.org/browse/MDEV-28225))
* Status variables `Innodb_encryption_key_rotation_list_length`, `Innodb_num_index_pages_written` and `Innodb_num_non_index_pages_written` were unused and have been removed. ([MDEV-28541](https://jira.mariadb.org/browse/MDEV-28541), [MDEV-28537](https://jira.mariadb.org/browse/MDEV-28537))
* Starting with this release, when [wsrep\_sst\_method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) is set to `rsync` or `mariadb-backup`, the `sst_max_binlogs` SST option can be specified in the \[`sst`] option group in configuration files. This parameter specifies the number of binary log files to be sent to the joiner node during SST. ([MDEV-27524](https://jira.mariadb.org/browse/MDEV-27524))
  * The default value is `0`:
    * If a binlog exists, it will be transferred.
    * If a binlog does not exist, no binlog will be transferred.
* Server error messages are available in Chinese. ([MDEV-28227](https://jira.mariadb.org/browse/MDEV-28227))
* MariaDB ColumnStore support is discontinued for MariaDB Enterprise Server 10.4. (MENT-1433)

## Issues Fixed

### Can result in data loss

* When the parser converts a string from the binary character set to a multi-byte character set (such as `utf32`), an invalid string could be produced. ([MDEV-23210](https://jira.mariadb.org/browse/MDEV-23210))
* When rows are inserted into an intermediate temporary table via the [LOAD DATA INFILE statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile), and then the rows are copied from the temporary table to a persistent table, the rows are not written to binary log if [binlog\_format=MIXED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is set, which prevents the operation from properly replicating to replica servers. ([MDEV-24667](https://jira.mariadb.org/browse/MDEV-24667))
* When [innodb\_disallow\_writes=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_disallow_writes) is set, [mariadb-admin shutdown](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/mariadb-admin) can hang. ([MDEV-25975](https://jira.mariadb.org/browse/MDEV-25975))
  * Starting with this release, the [innodb\_disallow\_writes system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_disallow_writes) has been removed.
* When a replica server's I/O thread receives an incomplete event group from the primary server, the replica server continues writing events to the relay log and does not raise an error. ([MDEV-27697](https://jira.mariadb.org/browse/MDEV-27697))
* Semisync-replica server recovery fails to rollback a prepared transaction. (MENT-1534)
* If a primary is shutdown during an active semi-sync connection during the period when the primary is awaiting an ACK, the primary hard kills the active communication thread and does not ensure the transaction was received by a replica. This can lead to an inconsistent replication state. ([MDEV-11853](https://jira.mariadb.org/browse/MDEV-11853))

### Can result in a hang or crash

* With MariaDB Enterprise Cluster, powered by Galera, when [wsrep\_sst\_method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) is set to rsync or `mariadb-backup`, the donor node does not transfer the correct binary logs to the joiner node with some configurations. ([MDEV-27524](https://jira.mariadb.org/browse/MDEV-27524))
* When a window function is used in the global ORDER BY clause of a `SELECT` statement with a `UNION`, the statement should be rejected, but the server executes the statement and crashes with a segmentation fault. ([MDEV-15208](https://jira.mariadb.org/browse/MDEV-15208))
* When a stored procedure queries a view and uses a for loop, the server can crash with a segmentation fault when the stored procedure is called twice in the same session. ([MDEV-26009](https://jira.mariadb.org/browse/MDEV-26009))
* When [innochecksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum) is executed on an encrypted tablespace file using the [--page-type-summary or -S option](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum#options), innochecksum crashes with a segmentation fault unless the [--page-type-dump or -D option](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum#options) is also specified. ([MDEV-27835](https://jira.mariadb.org/browse/MDEV-27835))
* When an invalid [CREATE SEQUENCE ... RESTART statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/create-sequence) is used inside of a [CREATE PROCEDURE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-procedures/create-procedure) or [CREATE FUNCTION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-function) statement, the server can crash while parsing the statement. ([MDEV-28220](https://jira.mariadb.org/browse/MDEV-28220))
* When a table contains a virtual generated column that is defined using the [IF()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/if) and [DATE\_FORMAT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/date_format) functions, inserting a row into the table can cause the server to crash with a segmentation fault. ([MDEV-24176](https://jira.mariadb.org/browse/MDEV-24176))
* When a non-updateable view is defined with `ALGORITHM=TEMPTABLE`, selecting data from the view can cause the server to crash with a segmentation fault. ([MDEV-21028](https://jira.mariadb.org/browse/MDEV-21028))
* When a `UNION` of decimal types is performed in an `ORDER BY` clause, the server can crash with a segmentation fault. ([MDEV-25994](https://jira.mariadb.org/browse/MDEV-25994))
* When a stored procedure executes a query that results in a mergeable derived table, the server can crash with a segmentation fault when the stored procedure is called twice in the same session. ([MDEV-27212](https://jira.mariadb.org/browse/MDEV-27212))
  * Querying views can result in mergeable derived tables.
  * Using subqueries with outer references can result mergeable derived tables.
* When [ANALYZE FORMAT=JSON](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/ANALYZE/README.md) is executed with a query that contains a subquery, the server can crash. ([MDEV-28268](https://jira.mariadb.org/browse/MDEV-28268))
* When a query using a window function with an `OVER (PARTITION BY ..)` or `OVER (ORDER BY ..)` clause is executed, the server can crash with a segmentation fault. ([MDEV-19398](https://jira.mariadb.org/browse/MDEV-19398))
  * If the query also uses `WITH ROLLUP`, this crash is more likely.
  * If the query's `OVER (PARTITION BY ..)` or `OVER (ORDER BY ..)` clause uses an aggregate function, this crash is more likely.
* When a query contains an outer join expression and a non-correlated subquery that the optimizer determines is low cost, executing the query can cause the server to crash if the optimizer also determines that the inner join expression can be eliminated. ([MDEV-28437](https://jira.mariadb.org/browse/MDEV-28437))
* With MariaDB Enterprise Cluster, a joiner node's binary logs could be deleted during an Incremental State Transfer (IST), which causes the node to fail to start, because it can not read the binary logs. ([MDEV-28583](https://jira.mariadb.org/browse/MDEV-28583))
  * This issue is confirmed to happen with [wsrep\_sst\_method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) set to `rsync`, but it might also occur with other SST/IST methods.

`ALTER TABLE` on a large InnoDB table can hang. ([MDEV-28415](https://jira.mariadb.org/browse/MDEV-28415))

* Online DDL fails while checking for instant alter condition. ([MDEV-28060](https://jira.mariadb.org/browse/MDEV-28060))
* With MariaDB Enterprise Cluster (Galera), parallel async replication hangs on a Galera node when `slave-parallel-threads` greater than `1` is used. ([MDEV-27568](https://jira.mariadb.org/browse/MDEV-27568))
* With MariaDB Enterprise Cluster (Galera), possible crash after a conflict of the applier thread with a stored procedure call triggered by the event scheduler. ([MDEV-27713](https://jira.mariadb.org/browse/MDEV-27713))
* Server crashes when executing a shutdown statement after starting an XA transaction. ([MDEV-26575](https://jira.mariadb.org/browse/MDEV-26575))
* Possible server crash during `mariadbd` initialization if the number of GTIDs added since the last purge of the `mysql.gtid_slave_pos` tables is greater than or equal to the `--gtid-cleanup-batch-size` value. ([MDEV-26473](https://jira.mariadb.org/browse/MDEV-26473))
* Possible server crash if an `INSERT .. SELECT or REPLACE .. SELECT` statement contains an `ON` expression in the top-level select and this expression used a subquery with a column reference. ([MDEV-28578](https://jira.mariadb.org/browse/MDEV-28578))

### Can result in unexpected behavior

* When [OPTIMIZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table) is executed on a sequence, the server raises an [ER\_BINLOG\_UNSAFE\_STATEMENT warning](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md), even if [binlog\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is set to `ROW` or `MIXED`. ([MDEV-24617](https://jira.mariadb.org/browse/MDEV-24617))
  * The warning can appear in the [MariaDB Error Log](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/error/README.md) as the following:`[Warning] Unsafe statement written to the binary log using statement format since BINLOG_FORMAT = STATEMENT. Statement is unsafe because it uses a system function that may return a different value on the slave Statement: OPTIMIZE TABLE SEQUENCE_NAME`
* When an [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) or [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) statement uses an [OR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/logical-operators/or) clause, the server raises an [ER\_UPDATE\_WITHOUT\_KEY\_IN\_SAFE\_MODE error](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md). ([MDEV-18304](https://jira.mariadb.org/browse/MDEV-18304))
  * The error can appear on the client as the following:`You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column`
* When an [UPDATE statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) uses a subquery inside an [IN()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/comparison-operators/in) clause, the optimizer could incorrectly choose to perform a full table scan (with `type: ALL`) when a range scan (with `type: range`) would be more efficient. ([MDEV-22377](https://jira.mariadb.org/browse/MDEV-22377))
* When a table contains multiple [ENUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/enum) columns with identical values, the values could become corrupt if multi-byte character sets are used. ([MDEV-28078](https://jira.mariadb.org/browse/MDEV-28078))
* When [DECIMAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/decimal) columns are read from [information\_schema.PROCESSLIST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-processlist-table), the server could incorrectly raise an [ER\_BAD\_DATA warning](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md). ([MDEV-28131](https://jira.mariadb.org/browse/MDEV-28131))
  * The warning can appear on the client as the following after executing [SHOW WARNINGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-warnings): `Encountered illegal value '' when converting to DECIMAL`

With [sql\_mode=ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode), the parser allows functions to be called using `PACKAGE_NAME.FUNCTION_NAME()`, but the parser raises a [ER\_PARSE\_ERROR error](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) if the function is called using `DATABASE_NAME.PACKAGE_NAME.FUNCTION_NAME()`. ([MDEV-28166](https://jira.mariadb.org/browse/MDEV-28166))

* When a view is used to update multiple rows of a [temporal table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables) in a single [UPDATE statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update), the server incorrectly raises a [ER\_WARN\_VIEW\_WITHOUT\_KEY warning](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md). ([MDEV-22973](https://jira.mariadb.org/browse/MDEV-22973))
  * The warning can appear on the client as the following after executing [SHOW WARNINGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-warnings): `View being updated does not have complete key of underlying table in it`
* When using [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) with [--raw](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-options#options) and [--stop-never](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-options#options), events from the primary server's currently active log file are not written to their respective log file specified by [--result-file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-options#options). ([MDEV-14608](https://jira.mariadb.org/browse/MDEV-14608))
* When a prepared statement is used to execute [EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain), a different query plan can be returned on the second execution. ([MDEV-19631](https://jira.mariadb.org/browse/MDEV-19631))
* When [slave\_compressed\_protocol](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is enabled with semi-synchronous replication, the numbering on packet headers can become out of sync between the primary and replica servers, but the inconsistency does not have any negative impact with release builds of MariaDB Enterprise Server. ([MDEV-25580](https://jira.mariadb.org/browse/MDEV-25580))
* The server and MariaDB Enterprise Backup can raise unnecessary warnings about tablespace IDs in some scenarios. ([MDEV-27343](https://jira.mariadb.org/browse/MDEV-27343))
  * The warning can appear as the following: `InnoDB: Allocated tablespace ID TABLESPACE_ID for DATABASE_NAME/TABLE_NAME, old maximum was 0`
  * This warning can be written to standard output (stdout) when preparing a backup with [MariaDB Enterprise Backup](../../10-4/broken-reference/).
  * This warning can be written to the [MariaDB Error Log](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/error/README.md) when InnoDB performs crash recovery at startup.
* With MariaDB Enterprise Cluster, the joiner node fails to complete an SSwhen [innodb\_log\_group\_home\_dir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_group_home_dir) specifies a directory different than [server-system-variables/#datadir##datadir##](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datadir). ([MDEV-27740](https://jira.mariadb.org/browse/MDEV-27740))
* When a non-partitioned table using the `DATA DIRECTORY` clause is converted to a partitioned table, the DATA DIRECTORY clause is silently ignored, and the partitioned table is moved to the default directory. ([MDEV-27065](https://jira.mariadb.org/browse/MDEV-27065))
* Starting with this release, the server will raise the [WARN\_OPTION\_IGNORED warning](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md).
* When a table contains an invisible column, [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) does not produce the correct [CREATE TABLE statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) in the backup file. ([MDEV-28253](https://jira.mariadb.org/browse/MDEV-28253))
* When a Spider table is queried using `IF(COUNT() ..)`, the server can raise an [ER\_BAD\_FIELD\_ERROR error](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md). ([MDEV-25116](https://jira.mariadb.org/browse/MDEV-25116))
* With MariaDB Enterprise Cluster, State Snapshot Transfers (SSTs) can fail on the donor nodwhen binary logs are enabled. ([MDEV-26201](https://jira.mariadb.org/browse/MDEV-26201))
* With MariaDB Enterprise Cluster, when [wsrep\_node\_address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_node_address) contains an IPv6 address and [wsrep\_sst\_receive\_address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_receive_address) is set to the default value of `AUTO`, State Snapshot Transfers (SST) can fail. ([MDEV-26171](https://jira.mariadb.org/browse/MDEV-26171))
* With [temporal tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables), replication can break if a system versioned table has been created on the replica via mariadb-dump, if the original table was altered before. ([MDEV-28254](https://jira.mariadb.org/browse/MDEV-28254))
* `mariadb-backup` does not detect multi-source replication primary. ([MDEV-21037](https://jira.mariadb.org/browse/MDEV-21037))
* `Master_SSL_Crl` shows `Master_SSL_CA` value in `SHOW SLAVE STATUS` output. ([MDEV-28428](https://jira.mariadb.org/browse/MDEV-28428))
* MariaDB Audit plugin produces corrupted log entries for `CONNECT` events. (MENT-1438)
* `mariadb-dump` does not create a dump where the `sql_mode` is set correctly for SQL/PL packages. ([MDEV-27816](https://jira.mariadb.org/browse/MDEV-27816))
* Missing binlog data for `INSERT .. ON DUPLICATE KEY UPDATE` ([MDEV-28310](https://jira.mariadb.org/browse/MDEV-28310))
* `mariadb-backup` prepare fails for incremental backups if a new schema is created after full backup. ([MDEV-28446](https://jira.mariadb.org/browse/MDEV-28446))
* Optimizer uses all partitions during an UPDATE and ignores partitioning filters. ([MDEV-28246](https://jira.mariadb.org/browse/MDEV-28246))
* When [INSERT .. ON DUPLICATE KEY UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) is executed and [binlog\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_format) is set to `MIXED`, the server raises an [ER\_BINLOG\_UNSAFE\_STATEMENT warning](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) even though the statement is written to the binary log in row-based format. ([MDEV-21810](https://jira.mariadb.org/browse/MDEV-21810))
  * The warning can appear in the [MariaDB Error Log](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/error/README.md) as the following: `<<sql>>`\[Warning] Unsafe statement written to the binary log using statement format since BINLOG\_FORMAT = STATEMENT. INSERT... ON DUPLICATE KEY UPDATE on a table with more than one UNIQUE KEY is unsafe Statement: INSERT INTO TABLE\_NAME VALUES (..) ON DUPLICATE KEY UPDATE KEY\_NAME = KEY\_VALUE<\</sql\* >>
* When `INSERT .. ON DUPLICATE KEY UPDATE` is executed and `binlog_row_image` is set to `FULL`, the server does not write unchanged columns to the binary log. ([MDEV-21810](https://jira.mariadb.org/browse/MDEV-21810))
* Crash recovery fails if the configured server ID does not match the server ID in the crashed data directory. (MENT-1535)
* PAM v2 plugin (`auth_pam`) produces zombie processes. (MENT-1443)
* With MariaDB Enterprise Cluster (Galera), `wsrep_incoming_addresses` does not include address details. (MENT-1527)
* With HashiCorp key management (`hashicorp_key_management`), dynamic changes to `hashicorp_key_management_cache_timeout` and h`ashicorp_key_management_cache_version_timeout` system variables are ignored. (MENT-1512)

### Related to install and upgrade

Galera snapshot transfer fails to upgrade between some major versions. ([MDEV-27437](https://jira.mariadb.org/browse/MDEV-27437))

On Windows, MSI installer does not install client shared libraries. ([MDEV-28581](https://jira.mariadb.org/browse/MDEV-28581))

After upgrade, `mysql.plugin` table has an entry for Semi-sync Replication, though this former plugin functionality is now built-in. ([MDEV-21873](https://jira.mariadb.org/browse/MDEV-21873))

* On RPM-based distributions, the Spider storage engine is distributed as a separate RPM package. (MENT-1092)
  * In prior releases, Spider's components were installed with the server's RPM package.
  * Starting with this release, Spider adds `unixODBC` as a dependency, so Spider has been moved to a separate RPM package to avoid adding new dependencies to the server's RPM package. For users of RPM-based distributions who loaded the Spider plugin with previous ES 10.4 releases, Spider's new RPM package and dependencies must be installed after upgrading to this release.
  * To install Spider's new package and dependencies on CentOS, Red Hat Enterprise Linux (RHEL), or Rocky Linux: `$ sudo yum install MariaDB-spider-engine`\
    To install Spider's new package and dependencies on SUSE Linux Enterprise Server (SLES): `$ sudo zypper install MariaDB-spider-engine`
* When the [hashicorp\_key\_management encryption plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin) encryption plugin is loaded, [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) should be used to take a logical backup before all minor and major upgrades due to changes that are not backward-compatible:
  * Starting with this release, the [hashicorp\_key\_management encryption plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin) rejects encryption keys that contain non-digit characters in the hex notation.
  * If a database is encrypted with encryption keys that only contain digit characters in the hex notation, the encryption keys will continue to work with the new version.
  * If a database is encrypted with encryption keys that are no longer valid, it is recommended to upgrade by installing the new version to a clean system and restoring a logical backup of the data. However, another alternative is to migrate the system to a new encryption key that only contains digit characters in the hex notation prior to the upgrade. If the alternative route is taken, extra care must be taken to ensure that all encrypted data uses the new encryption key. For help with this process, contact [MariaDB Support](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/support).
  * When performing minor and major upgrades on Debian and Ubuntu, a logical backup must be taken before upgrading the server and plugin packages. When the old packages are upgraded, a message about plugin incompatibility is printed, but the server and plugin packages are upgraded anyway.
  * When performing minor upgrades on CentOS, RHEL, Rocky Linux, and SUSE, a logical backup can be taken before or after upgrading the server package. When the old packages are upgraded, a message about plugin incompatibility is printed, and the server package is upgraded, but the plugin package is not. The old plugin package must be manually removed, and then the new plugin package can be installed.
  * When performing major upgrades on CentOS, RHEL, Rocky Linux, and SUSE, a logical backup must be taken before upgrading the server and plugin packages. The old server and plugin packages must be manually removed, and then the new server and plugin packages can be installed.
  * When the plugin package is manually removed, the plugin configuration file can also be removed, so it is recommended to backup the file.

## Interface Changes

* [hashicorp\_key\_management\_check\_kv\_version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin) system variable added
* [innodb\_disallow\_writes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_disallow_writes) system variable removed
* [Innodb\_encryption\_key\_rotation\_list\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables) status variable removed
* [Innodb\_num\_index\_pages\_written](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#Innodb_num_index_pages_written) status variable removed
* [Innodb\_num\_non\_index\_pages\_written](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#Innodb_num_non_index_pages_written) status variable removed
* [JSON\_EQUALS()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_equals) function added
* [JSON\_NORMALIZE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_normalize) function added
* `mariadb-backup` --sst-max-binlogs command-line option added
* `mysqld` --hashicorp-key-management-check-kv-version command-line option added
* `mysqld` --password-reuse-check command-line option added
* `mysqld` --password-reuse-check-interval command-line option added
* `mysqld` --spider-buffer-size command-line option added
* `mysqld` --spider-wrapper-protocols command-line option added
* `mariadb-dump` --as-of command-line option added
* `password_reuse_check password_reuse_check.so` plugin added
* [password\_reuse\_check\_history](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/password_reuse_check_interval) system table added
* [password\_reuse\_check\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/password_reuse_check_interval) system variable added
* [spider\_buffer\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) system variable added
* [SPIDER\_WRAPPER\_PROTOCOLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/information-schema-spider_wrapper_protocols-table) information schema table added
* `SPIDER_WRAPPER_PROTOCOLS ha_spider.so` plugin added

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.4.25-16 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64 Red Hat Enterprise Linux 8 packages)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see [MariaDB Corporation Engineering Policies".](https://mariadb.com/engineering-policies).

## Installation Instructions

* [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
