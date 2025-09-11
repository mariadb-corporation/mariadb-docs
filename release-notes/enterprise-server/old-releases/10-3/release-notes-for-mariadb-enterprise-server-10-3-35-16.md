# Release Notes for MariaDB Enterprise Server 10.3.35-16

MariaDB Enterprise Server 10.3.35-16 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3. This release includes a variety of fixes.

MariaDB Enterprise Server 10.3.35-16 was released on 2022-06-13.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2022-27458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27458)                                                                                               | 7.5             |
| [CVE-2022-27456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27456)                                                                                               | 7.5             |
| [CVE-2022-27452](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27452)                                                                                               | 7.5             |
| [CVE-2022-27449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27449)                                                                                               | 7.5             |
| [CVE-2022-27448](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27448)                                                                                               | 7.5             |
| [CVE-2022-27447](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27447)                                                                                               | 7.5             |
| [CVE-2022-27445](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27445)                                                                                               | 7.5             |
| [CVE-2022-27387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27387)                                                                                               | 7.5             |
| [CVE-2022-27386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27386)                                                                                               | 7.5             |
| [CVE-2022-27384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27384)                                                                                               | 7.5             |
| [CVE-2022-27383](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27383)                                                                                               | 7.5             |
| [CVE-2022-27381](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27381)                                                                                               | 7.5             |
| [CVE-2022-27380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27380)                                                                                               | 7.5             |
| [CVE-2022-27379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27379)                                                                                               | 7.5             |
| [CVE-2022-27378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27378)                                                                                               | 7.5             |
| [CVE-2022-27377](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27377)                                                                                               | 7.5             |
| [CVE-2022-27376](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27376)                                                                                               | 7.5             |
| [CVE-2022-32088](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32088)                                                                                               | 6.5             |
| [CVE-2022-32087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32087)                                                                                               | 6.5             |
| [CVE-2022-32085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32085)                                                                                               | 6.5             |
| [CVE-2022-32083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32083)                                                                                               | 6.5             |
| [CVE-2021-46669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46669)                                                                                               | 6.5             |
| [CVE-2022-21427](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21427)                                                                                               | 4.9             |

## Backported Features

MariaDB Enterprise Server enables a predictable development and operations experience through an [enterprise lifecycle](../../enterprise-server-lifecycle.md). These new features have been backported after reaching maturity in MariaDB Community Server:

* [mysqldump option --as-of](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) reads data as of specific timestamp from system-versioned tables. (MENT-1457)

## Notable Changes

* Galera updated to 25.3.37
* Spider storage engine refuses attempts to create a temporary table since the engine cannot itself store data and cannot create temporary tables on a remote server. ([MDEV-28225](https://jira.mariadb.org/browse/MDEV-28225))
* Status variables Innodb\_encryption\_key\_rotation\_list\_length, Innodb\_num\_index\_pages\_written and Innodb\_num\_non\_index\_pages\_written were unused and have been removed. ([MDEV-28541](https://jira.mariadb.org/browse/MDEV-28541), [MDEV-28537](https://jira.mariadb.org/browse/MDEV-28537))
* Starting with this release, when [wsrep\_sst\_method|](release-notes-for-mariadb-enterprise-server-10-3-35-16.md#galera-cluster-system-variables/) is set to `rsync` or `mariadb-backup`, the `sst_max_binlogs` SST option can be specified in the \[`sst`] option group in configuration files. This parameter specifies the number of binary log files to be sent to the joiner node during SST. ([MDEV-27524](https://jira.mariadb.org/browse/MDEV-27524))
  * The default value is `0`:
    * If a binlog exists, it will be transferred.
    * If a binlog does not exist, no binlog will be transferred.

## Issues Fixed

### Can result in data loss

* When the parser converts a string from the binary character set to a multi-byte character set (such as `utf32`), an invalid string could be produced. ([MDEV-23210](https://jira.mariadb.org/browse/MDEV-23210))
* When rows are inserted into an intermediate temporary table via the [LOAD DATA INFILE statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile),and then the rows are copied from the temporary table to a persistent table, the rows are not written to binary log if [binlog\_format=MIXED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is set, which prevents the operation from properly replicating to replica servers. ([MDEV-24667](https://jira.mariadb.org/browse/MDEV-24667))
* When [innodb\_disallow\_writes=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_disallow_writes) is set, [mysqladmin shutdown](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/mariadb-admin) can hang. ([MDEV-25975](https://jira.mariadb.org/browse/MDEV-25975))
  * Starting with this release, the [innodb\_disallow\_writes system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_disallow_writes) has been removed.
* When a replica server's I/O thread receives an incomplete event group from the primary server, the replica server continues writing events to the relay log and does not raise an error. ([MDEV-27697](https://jira.mariadb.org/browse/MDEV-27697))
* Semisync-replica server recovery fails to rollback a prepared transaction. (MENT-1534)

### Can result in a hang or crash

* With MariaDB Enterprise Cluster, powered by Galera, when [wsrep\_sst\_method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) is set to `rsync` or `mariadb-backup`, the donor node does not transfer the correct binary logs to the joiner node with some configurations. ([MDEV-27524](https://jira.mariadb.org/browse/MDEV-27524))
* When a window function is used in the global ORDER BY clause of a [SELECT statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) with a `UNION`, the statement should be rejected, but the server executes the statement and crashes with a segmentation fault. ([MDEV-15208](https://jira.mariadb.org/browse/MDEV-15208))
* When a stored procedure queries a view and uses a for loop, the server can crash with a segmentation fault when the stored procedure is called twice in the same session. ([MDEV-26009](https://jira.mariadb.org/browse/MDEV-26009))
* Server can crash when a procedure that queries a view is called twice. ([MDEV-26009](https://jira.mariadb.org/browse/MDEV-26009))
* When [innochecksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum) is executed on an encrypted tablespace file using the [--page-type-summary or -S option](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum#page-type-summary), `innochecksum` crashes with a segmentation fault unless the [--page-type-dump or -D option](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum#page-type-summary) is also specified. ([MDEV-27835](https://jira.mariadb.org/browse/MDEV-27835))
* When an invalid [CREATE SEQUENCE ... RESTART statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/create-sequence) is used inside of a `CREATE PROCEDURE` or `CREATE FUNCTION` statement, the server can crash while parsing the statement. ([MDEV-28220](https://jira.mariadb.org/browse/MDEV-28220))
* Possible crash on parsing a syntax incorrect statement `CREATE SEQUENCE .. RESTART` inside of a \`\`CREATE PROCEDURE`or`CREATE FUNCTION\` ([MDEV-28220](https://jira.mariadb.org/browse/MDEV-28220))
* When a table contains a virtual generated column that is defined using the `IF()` and `DATE_FORMAT()` functions, inserting a row into the table can cause the server to crash with a segmentation fault. ([MDEV-24176](https://jira.mariadb.org/browse/MDEV-24176))
* Server crash after `INSERT` in a table with virtual column generated using `date_format()` and `if()` ([MDEV-24176](https://jira.mariadb.org/browse/MDEV-24176))
* When a non-updateable view is defined with `ALGORITHM=TEMPTABLE`, selecting data from the view can cause the server to crash with a segmentation fault. ([MDEV-21028](https://jira.mariadb.org/browse/MDEV-21028))
* When a `UNION` of decimal types is performed in an ORDER BY clause, the server can crash with a segmentation fault. ([MDEV-25994](https://jira.mariadb.org/browse/MDEV-25994))
* When a stored procedure executes a query that results in a mergeable derived table, the server can crash with a segmentation fault when the stored procedure is called twice in the same session. ([MDEV-27212](https://jira.mariadb.org/browse/MDEV-27212))
  * Querying views can result in mergeable derived tables.
  * Using subqueries with outer references can result mergeable derived tables.
* When [ANALYZE FORMAT=JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-format-json) is executed with a query that contains a subquery, the server can crash. ([MDEV-28268](https://jira.mariadb.org/browse/MDEV-28268))
* When a query using a window function with an `OVER (PARTITION BY ..)` or `OVER (ORDER BY ..)` clause is executed, the server can crash with a segmentation fault. ([MDEV-19398](https://jira.mariadb.org/browse/MDEV-19398))
  * If the query also uses `WITH ROLLUP`, this crash is more likely.
  * `If the query's`OVER (PARTITION BY ..)`or`OVER (ORDER BY ..)`clause uses an aggregate function, this crash is more likely.`
* When a query contains an outer join expression and a non-correlated subquery that the optimizer determines is low cost, executing the query can cause the server to crash if the optimizer also determines that the inner join expression can be eliminated. ([MDEV-28437](https://jira.mariadb.org/browse/MDEV-28437))
* With MariaDB Enterprise Cluster, a joiner node's binary logs could be deleted during an Incremental State Transfer (IST), which causes the node to fail to start, because it can not read the binary logs. ([MDEV-28583](https://jira.mariadb.org/browse/MDEV-28583))
* This issue is confirmed to happen with [wsrep\_sst\_method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_sst_method) set to `rsync`, but it might also occur with other SST/IST methods.
* `ALTER TABLE` on a large InnoDB table can hang. ([MDEV-28415](https://jira.mariadb.org/browse/MDEV-28415))

### Can result in unexpected behavior

* When [OPTIMIZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table) is executed on a sequence, the server raises an [ER\_BINLOG\_UNSAFE\_STATEMENT warning](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md), even if [binlog\_format](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/binlog_format/README.md) is set to `ROW` or `MIXED`. ([MDEV-24617](https://jira.mariadb.org/browse/MDEV-24617))
  * The warning can appear in the MariaDB Error Log as the following:

```
[Warning] Unsafe statement written to the binary log using statement format since BINLOG_FORMAT = STATEMENT. Statement is unsafe because it uses a system function that may return a different value on the slave Statement: OPTIMIZE TABLE SEQUENCE_NAME
```

* When an [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) or [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) statement uses an `OR` clause, the server raises an [ER\_UPDATE\_WITHOUT\_KEY\_IN\_SAFE\_MODE error](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md). ([MDEV-18304](https://jira.mariadb.org/browse/MDEV-18304))
  * The error can appear on the client as the following:

```
You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column
```

* When an [UPDATE statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) uses a subquery inside an [IN() clause](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/comparison-operators/in), the optimizer could incorrectly choose to perform a full table scan (with `type: ALL`) when a range scan (with `type: range`) would be more efficient. ([MDEV-22377](https://jira.mariadb.org/browse/MDEV-22377))
* When a table contains multiple [ENUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/enum) columns with identical values, the values could become corrupt if multi-byte character sets are used. ([MDEV-28078](https://jira.mariadb.org/browse/MDEV-28078))
* When [DECIMAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/decimal) columns are read from [information\_schema.PROCESSLIST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-processlist-table), the server could incorrectly raise an [ER\_BAD\_DATA](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) warning. ([MDEV-28131](https://jira.mariadb.org/browse/MDEV-28131))
  * The warning can appear on the client as the following after executing `SHOW WARNINGS`:

```
Encountered illegal value '' when converting to DECIMAL
```

* With [sql\_mode=ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode), the parser allows functions to be called using `PACKAGE_NAME.FUNCTION_NAME()`, but the parser raises a [ER\_PARSE\_ERROR error](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) if the function is called using `DATABASE_NAME.PACKAGE_NAME.FUNCTION_NAME()`. ([MDEV-28166](https://jira.mariadb.org/browse/MDEV-28166))
*
  * When a view is used to update multiple rows of a [temporal table](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/temporal-table/README.md) in a single [UPDATE statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update), the server incorrectly raises a [ER\_WARN\_VIEW\_WITHOUT\_KEY warning](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md). ([MDEV-22973](https://jira.mariadb.org/browse/MDEV-22973))
  * The warning can appear on the client as the following after executing [SHOW WARNINGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-warnings):

```
View being updated does not have complete key of underlying table in it
```

* When using [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) with [--raw](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog#raw) and [--stop-never](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-options#options), events from the primary server's currently active log file are not written to their respective log file specified by `--result-file`. ([MDEV-14608](https://jira.mariadb.org/browse/MDEV-14608))
* When a prepared statement is used to execute [EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain), a different query plan can be returned on the second execution. ([MDEV-19631](https://jira.mariadb.org/browse/MDEV-19631))
* When [slave\_compressed\_protocol](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#slave_compressed_protocol) is enabled with semi-synchronous replication, the numbering on packet headers can become out of sync between the primary and replica servers, but the inconsistency does not have any negative impact with release builds of MariaDB Enterprise Server. ([MDEV-25580](https://jira.mariadb.org/browse/MDEV-25580))
* The server and [MariaDB Enterprise Backup](../../10-3/broken-reference/) can raise unnecessary warnings about tablespace IDs in some scenarios. ([MDEV-27343](https://jira.mariadb.org/browse/MDEV-27343))
  * The warning can appear as the following:

```
InnoDB: Allocated tablespace ID TABLESPACE_ID for DATABASE_NAME/TABLE_NAME, old maximum was 0
```

* This warning can be written to standard output (`stdout`) when preparing a backup with MariaDB Enterprise Backup.
* This warning can be written to the MariaDB Error Log when InnoDB performs crash recovery at startup.
* With MariaDB Enterprise Cluster, the joiner node fails to complete an SST when [innodb\_log\_group\_home\_dir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_log_group_home_dir) specifies a directory different than [datadir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datadir). ([MDEV-27740](https://jira.mariadb.org/browse/MDEV-27740))
* When a non-partitioned table using the `DATA DIRECTORY` clause is converted to a partitioned table, the `DATA DIRECTORY` clause is silently ignored, and the partitioned table is moved to the default directory. ([MDEV-27065](https://jira.mariadb.org/browse/MDEV-27065))
* Starting with this release, the server will raise the [WARN\_OPTION\_IGNORED warning](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md).
* When a table contains an invisible column, [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) does not produce the correct [CREATE TABLE statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) in the backup file. ([MDEV-28253](https://jira.mariadb.org/browse/MDEV-28253))
* When a Spider table is queried using `IF(COUNT() ..)`, the server can raise an [ER\_BAD\_FIELD\_ERROR](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) error. ([MDEV-25116](https://jira.mariadb.org/browse/MDEV-25116))
* With MariaDB Enterprise Cluster, State Snapshot Transfers (SSTs) can fail on the donor node when binary logs are enabled. ([MDEV-26201](https://jira.mariadb.org/browse/MDEV-26201))
* With MariaDB Enterprise Cluster, when [wsrep\_node\_address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_node_address) contains an IPv6 address and [wsrep\_sst\_receive\_address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_receive_address) is set to the default value of `AUTO`, State Snapshot Transfers (SST) can fail. ([MDEV-26171](https://jira.mariadb.org/browse/MDEV-26171))
* With [temporal tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables), replication can break if a system versioned table has been created on the replica via mariadb-dump, if the original table was altered before. ([MDEV-28254](https://jira.mariadb.org/browse/MDEV-28254))
* `mariadb-backup` does not detect multi-source replication primary. ([MDEV-21037](https://jira.mariadb.org/browse/MDEV-21037))
* `Master_SSL_Crl` shows `Master_SSL_CA` value in `SHOW SLAVE STATUS` output. ([MDEV-28428](https://jira.mariadb.org/browse/MDEV-28428))
* MariaDB Audit plugin produces corrupted log entries for `CONNECT` events. (MENT-1438)
* `mariadb-dump` does not create a dump where the `sql_mode` is set correctly for SQL/PL packages. ([MDEV-27816](https://jira.mariadb.org/browse/MDEV-27816))
* Missing binlog data for `INSERT .. ON DUPLICATE KEY UPDATE` ([MDEV-28310](https://jira.mariadb.org/browse/MDEV-28310))
* `mariadb-backup prepare` fails for incremental backups if a new schema is created after full backup. ([MDEV-28446](https://jira.mariadb.org/browse/MDEV-28446))
* Optimizer uses all partitions during an `UPDATE` and ignores partitioning filters. ([MDEV-28246](https://jira.mariadb.org/browse/MDEV-28246))
* When [INSERT .. ON DUPLICATE KEY UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) is executed and [binlog\_format](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/binlog_format/README.md) is set to `MIXED`, the server raises an \[e1592|\[`ER_BINLOG_UNSAFE_STATEMENT` warning]] even though the statement is written to the binary log in row-based format. ([MDEV-21810](https://jira.mariadb.org/browse/MDEV-21810))
  * The warning can appear in the MariaDB Error Log as the following:`<<sql inline=false>>` \[Warning] Unsafe statement written to the binary log using statement format since BINLOG\_FORMAT = STATEMENT. INSERT... ON DUPLICATE KEY UPDATE on a table with more than one UNIQUE KEY is unsafe Statement: INSERT INTO TABLE\_NAME VALUES (..) ON DUPLICATE KEY UPDATE KEY\_NAME = KEY\_VALUE `<<sql>>`
* When `INSERT .. ON DUPLICATE KEY UPDATE` is executed and `binlog_row_image` is set to `FULL`, the server does not write unchanged columns to the binary log. ([MDEV-21810](https://jira.mariadb.org/browse/MDEV-21810))
*
  * Crash recovery fails if the configured server ID does not match the server ID in the crashed data directory. (MENT-1535)

### Related to install and upgrade

* Galera snapshot transfer fails to upgrade between some major versions. ([MDEV-27437](https://jira.mariadb.org/browse/MDEV-27437))
* On Windows, MSI installer does not install client shared libraries. ([MDEV-28581](https://jira.mariadb.org/browse/MDEV-28581))
* After upgrade, `mysql.plugin` table has an entry for Semi-sync Replication, though this former plugin functionality is now built-in. ([MDEV-21873](https://jira.mariadb.org/browse/MDEV-21873))

## Interface Changes

* [innodb\_disallow\_writes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#innodb_disallow_writes) system variable removed
* [Innodb\_encryption\_key\_rotation\_list\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#Innodb_encryption_key_rotation_list_length) status variable removed
* [Innodb\_num\_index\_pages\_written](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#Innodb_num_index_pages_written) status variable removed
* [Innodb\_num\_non\_index\_pages\_written](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#Innodb_num_non_index_pages_written) status variable removed
* `mariadb-backup` [--sst-max-binlogs](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/mariadb-binlogs/README.md) command-line option added
* `mysqldump` [--as-of](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) command-line option added

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.3.35-16 is provided for:

* CentOS 7 (x86\_64)
* Debian 9 (x86\_64, ARM64)
* Debian 10 (x86\_64, ARM64)
* Microsoft Windows (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 18.04 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

#### Note

This is the final release for Debian 9.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
