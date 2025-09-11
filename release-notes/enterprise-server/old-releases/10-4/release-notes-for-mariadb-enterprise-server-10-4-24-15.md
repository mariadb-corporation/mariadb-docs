# Release Notes for MariaDB Enterprise Server 10.4.24-15

MariaDB Enterprise Server 10.4.24-15 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4. This release includes a variety of fixes.

MariaDB Enterprise Server 10.4.24-15 was released on 2022-03-14.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2021-46668](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46668)                                                                                               | 5.5             |
| [CVE-2021-46665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46665)                                                                                               | 5.5             |
| [CVE-2021-46664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46664)                                                                                               | 5.5             |
| [CVE-2021-46663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46663)                                                                                               | 5.5             |
| [CVE-2021-46661](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46661)                                                                                               | 5.5             |
| [CVE-2021-46659](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46659)                                                                                               | 5.5             |
| [CVE-2022-21595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21595)                                                                                               | 4.4             |

## Notable Changes

* Galera updated to 26.4.11
* The maximum values for [innodb\_ft\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_cache_size) and [innodb\_ft\_total\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_total_cache_size) have been changed from `80000000` to `1099511627776` (1 TB). (MENT-1428)
* On Windows, [core\_file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#core_file) is enabled by default. ([MDEV-18439](https://jira.mariadb.org/browse/MDEV-18439))
* New system variables have been added for the HashiCorp Key Management Plugin: (MENT-864)
  * `hashicorp_key_management_cache_timeout` defines the time (in milliseconds) after which the value of the key stored in the cache becomes invalid, and an attempt to read this data causes a new request to be sent to the vault server. If the value is `0`, then the keys will always be considered invalid, but they are still used if the vault server is unavailable and `hashicorp_key_management_use_cache_on_timeout` is enabled. By default, the value is 60000 (1 minute).
  * `hashicorp_key_management_cache_version_timeout` defines the time (in milliseconds) after which the information about latest version number of the key (which is stored in the cache) becomes invalid and an attempt to read this information causes a new request to be sent to the vault server. If the value is `0`, then information about latest key version numbers always considered invalid, but they are still used if the vault server is unavailable and `hashicorp_key_management_use_cache_on_timeout` is enabled. By default, the value is 0.
  * For maximum flexibility, both of the new system variables can be configured with the loose prefix:

```
[mariadb]
loose_hashicorp_key_management_cache_timeout=120000
loose_hashicorp_key_management_cache_version_timeout=120000
```

## Issues Fixed

### Can result in data loss

* Columns in some `INFORMATION_SCHEMA` tables are erroneously declared with `DEFAULT` clauses, which is not compliant with the SQL standard. ([MDEV-18918](https://jira.mariadb.org/browse/MDEV-18918))
* Consequently, when `sql_mode=EMPTY_STRING_IS_NULL` is set, queries like `CREATE TABLE .. SELECT .. FROM INFORMATION_SCHEMA...` could encounter replication errors like the following:

```
Error 'Invalid default value for 'TABLE_NAME'' on query. Default database: 'test'. Query: 'CREATE TABLE `t1` (`TABLE_NAME` varchar(64) CHARACTER SET utf8 NOT NULL DEFAULT ''
```

* When an [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) statement changes the order of indexes in a MyISAM or Aria table using the INPLACE algorithm, the table can become corrupt. ([MDEV-25803](https://jira.mariadb.org/browse/MDEV-25803))
* When [CREATE OR REPLACE SEQUENCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/create-sequence) is written to the binary log, the statement is not flagged as DDL, which causes the replica servers to execute the statement in an unsafe way if parallel replication is enabled. ([MDEV-27365](https://jira.mariadb.org/browse/MDEV-27365))
* After upgrading from [MariaDB 10.3](../../../community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md) or earlier, the names of some triggers can appear empty, and the trigger can't be dropped. ([MDEV-25659](https://jira.mariadb.org/browse/MDEV-25659))

### Can result in a hang or crash

* When a `FULLTEXT` index is added to an InnoDB table with `ALGORITHM=INPLAC`E and the indexed column uses the `tis620` character set, the server can crash with a segmentation fault (signal 11). ([MDEV-24901](https://jira.mariadb.org/browse/MDEV-24901))
* When MariaDB Server is used on the ARM architecture, which uses a weak memory model, an internal hash table implementation can cause the server to crash with a segmentation fault (signal 11). ([MDEV-27088](https://jira.mariadb.org/browse/MDEV-27088))
* When [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) and [innodb\_force\_recovery=1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_force_recovery) are set with MariaDB Enterprise Cluster, powered by Galera, the joiner node fails to perform an SST. ([MDEV-26064](https://jira.mariadb.org/browse/MDEV-26064))
  * The SST log contains the following message related to the failure:

```
mariadb-backup: The option "innodb_force_recovery" should only be used with "--prepare".
mariadb-backup: innodb_init_param(): Error occurred.
```

* When [--stream=xbstream](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) is set, MariaDB Enterprise Backup can hang on lock acquisitions due to a deadlock. ([MDEV-26558](https://jira.mariadb.org/browse/MDEV-26558))
* When a stored procedure is defined with a query that contains a set function, and the set function's only argument is an outer reference to a column of a mergeable view, a derived table, or a CTE, the second execution of the stored procedure can cause the server to crash. ([MDEV-25086](https://jira.mariadb.org/browse/MDEV-25086))
* When a derived table is created for certain queries that use subqueries over Views or CTEs, the server can crash with a segmentation fault (signal 11). ([MDEV-25631](https://jira.mariadb.org/browse/MDEV-25631))
* When a stored procedure uses a cursor to run a query that requires an internal temporary table (such as queries containing an `ORDER BY` clause), the server can crash due to a segmentation fault (signal 11). ([MDEV-24827](https://jira.mariadb.org/browse/MDEV-24827))
* Server can crash if a CTE or derived table is not used by the query. ([MDEV-25766](https://jira.mariadb.org/browse/MDEV-25766))
* When [log\_slow\_verbosity = 'explain'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_slow_verbosity) is set and a query is executed that references a derived table, the server can crash while writing the query's execution plan to the slow query log. ([MDEV-26249](https://jira.mariadb.org/browse/MDEV-26249))
* When a stored procedure or a prepared statement is used to execute a query that performs a join which compares a `GEOMETRY` column with a different data type, executing the stored procedure or prepared statement twice can cause the server to crash. ([MDEV-20770](https://jira.mariadb.org/browse/MDEV-20770))
* When a system versioned table is created with [character\_set\_server=utf8mb4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#character_set_server) and [collation\_server=utf8mb4\_unicode\_1400\_ci](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#collation_server), the server can crash. ([MDEV-27195](https://jira.mariadb.org/browse/MDEV-27195))
* When a system-versioned table is partitioned by `SYSTEM_TIME`, executing [DELETE FROM .. PARTITION(..)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) causes the server to crash. ([MDEV-27217](https://jira.mariadb.org/browse/MDEV-27217))
*
  * When the following conditions are met, executing a prepared statement twice can cause the server to crash: ([MDEV-23182](https://jira.mariadb.org/browse/MDEV-23182))
  * The [in\_predicate\_conversion\_threshold](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#in_predicate_conversion_threshold) system variable must be set to some value n.
  * The query must contain an `IN(...)` clause with more than n string literals.
  * The query must require character set conversions.
* After completing a successful SST with MariaDB Enterprise Cluster, [wsrep\_local\_state\_comment](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables) on the donor node still says `'Donor/Desynced'`. ([MDEV-27459](https://jira.mariadb.org/browse/MDEV-27459))
* With MariaDB Enterprise Cluster, \* when [REPAIR VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/repair-view) is executed on a view that references [information\_schema.TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-tables-table), the server can crash. ([MDEV-25538](https://jira.mariadb.org/browse/MDEV-25538))
* When [ALTER TABLE .. ADD COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) is used to instantly add columns in the middle of an InnoDB table, and then the tablespace is exported with [FLUSH TABLES .. FOR EXPORT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush), and then the tablespace is re-imported with [ALTER TABLE .. IMPORT TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table), the server can crash. ([MDEV-27272](https://jira.mariadb.org/browse/MDEV-27272))
* When [optimizer\_switch='not\_null\_range\_scan=on'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch) is set, the server can crash if an index on an InnoDB table is used to check a condition that can evaluate to `NULL`. ([MDEV-22846](https://jira.mariadb.org/browse/MDEV-22846))
* When a [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) table uses a [FLOAT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/float) column, the server can crash with an assertion failure. ([MDEV-27184](https://jira.mariadb.org/browse/MDEV-27184))
  * In the MariaDB error log, the following error message could be written about the assertion failure:

```
Assertion `(old_top == initial_top (av) && old_size == 0) || ((unsigned long) (old_size) >= MINSIZE && prev_inuse (old_top) && ((unsigned long) old_end & (pagesize - 1)) == 0)' failed.
```

* With MariaDB Enterprise Cluster, \* when a [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) statement that defines a Foreign Key constraint is replicated to other cluster nodes, the nodes could apply the statement in parallel with other DML statements that affect the Foreign Key constraint, which causes the node to fail with an assertion failure. ([MDEV-27276](https://jira.mariadb.org/browse/MDEV-27276))
* With MariaDB Enterprise Cluster, \* when two transactions delete a row from two separate InnoDB tables in parallel and a foreign key causes a delete to cascade for both transactions to the same row in a third table, the server can crash with an assertion failure. ([MDEV-26803](https://jira.mariadb.org/browse/MDEV-26803), [MDEV-26298](https://jira.mariadb.org/browse/MDEV-26298))
  * In previous releases, this issue could be avoided by setting [wsrep\_slave\_threads=1](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_slave_threads).
  * In the MariaDB error log, the following error message about the assertion failure could be written:

```
int wsrep::client_state::bf_abort(wsrep::seqno): Assertion `mode_ == m_local || transaction_.is_streaming()' failed.
[ERROR] mysqld got signal 6 ;
```

* With MariaDB Enterprise Cluster, \* when a node tries to write to the [mysql.slow\_log system table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-slow_log-table) and [wsrep\_trx\_fragment\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_trx_fragment_size) is greater than 0, the server can crash with an assertion failure. ([MDEV-27338](https://jira.mariadb.org/browse/MDEV-27338))
  * In the MariaDB error log, the following error message about the assertion failure could be written:

```
int wsrep::client_state::after_row(): Assertion `state_ == s_exec' failed.
[ERROR] mysqld got signal 6 ;
```

### Can result in unexpected behavior

* When a multi-byte character set is used, the last character of a [TINYTEXT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/tinytext) column can be truncated, which makes it appear as a question mark (`'?`). ([MDEV-24335](https://jira.mariadb.org/browse/MDEV-24335))
* Subquery using the `ALL` keyword on [TIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/time) columns produces a wrong result. ([MDEV-27098](https://jira.mariadb.org/browse/MDEV-27098))
* Subquery using the `ALL` keyword on [DATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/date) columns produces a wrong result. ([MDEV-27072](https://jira.mariadb.org/browse/MDEV-27072))
* When float literals are defined using scientific notation and the token also contains certain special characters, the parser incorrectly parses the float value and completely drops it from the request. ([MDEV-27066](https://jira.mariadb.org/browse/MDEV-27066))
* When a double-encapsulated CTE query calls a function which reads a table that has been aliased in the CTE query, the server incorrectly raises an error with the [ER\_NO\_SUCH\_TABLE](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) error code. ([MDEV-26825](https://jira.mariadb.org/browse/MDEV-26825))
* When a CTE is used in a subquery of a [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) statement, the server incorrectly raises an error with the `ER_NO_DB_ERROR` error code. ([MDEV-26470](https://jira.mariadb.org/browse/MDEV-26470))
* When MariaDB Enterprise Cluster performs an SST, the SST scripts incorrectly try to read [ssl\_ca](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables) as a path to a directory of TLS CA certificates instead of using [ssl\_capath](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables) for that purpose. ([MDEV-27181](https://jira.mariadb.org/browse/MDEV-27181))
* When MariaDB Enterprise Cluster performs an SST, the SST scripts do not always interpret [log\_bin\_index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) correctly. ([MDEV-26915](https://jira.mariadb.org/browse/MDEV-26915))
* When an index is used for an `ORDER BY .. LIMIT` query, the optimizer does not disable the `Range Checked for Each Record` optimization. ([MDEV-27270](https://jira.mariadb.org/browse/MDEV-27270))
* When [optimizer\_switch='index\_merge\_sort\_intersection=on'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch) is set, the optimizer can incorrectly choose to merge an index that does not help, because the query conditions require the full index to be scanned. ([MDEV-27262](https://jira.mariadb.org/browse/MDEV-27262))
* When the [version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#version) system variable is set, MariaDB Connector/C and the [mariadb client](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb/README.md) do not interpret MariaDB Server's extended metadata properly, which can cause results from some [SHOW ..](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show) to be right-aligned. ([MDEV-27304](https://jira.mariadb.org/browse/MDEV-27304))
* When an `INSERT .. SELECT` statement selects from and inserts into the same table, rows are counted twice, which can cause row numbers to be reported incorrectly in error messages. ([MDEV-26698](https://jira.mariadb.org/browse/MDEV-26698))
* When a replica server's relay log is rotated, `Seconds_Behind_Master` in [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status) can temporarily show an incorrect value that is very high. ([MDEV-16091](https://jira.mariadb.org/browse/MDEV-16091))

The `collation` column in the [information\_schema.STATISTICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables) table is incorrectly read as `NULL`. ([MDEV-4621](https://jira.mariadb.org/browse/MDEV-4621))

* When a join performs a comparison between an expression that uses a case-insensitive collation and an ENUM column that uses a binary collation, the comparison uses the wrong collation, which can cause results to be incorrect. ([MDEV-26129](https://jira.mariadb.org/browse/MDEV-26129))
* When #[#innodb\_buffer\_pool\_size##](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_size) is changed dynamically with [SET GLOBAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set), InnoDB does not enforce the minimum value that is enforced on startup, which can result in an impossibly small buffer pool with some values of [innodb\_buffer\_pool\_chunk\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_chunk_size). ([MDEV-27467](https://jira.mariadb.org/browse/MDEV-27467))
* When the [DATABASE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/database) function is used in some queries (such as queries using `UNION ALL`), database names can be truncated to 34 characters, even though database names can have up to 64 characters. ([MDEV-27544](https://jira.mariadb.org/browse/MDEV-27544))
* When the [--symbolic-links](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#-symbolic-links) option is disabled, such as \* when [--skip-symbolic-links](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#other-options) or [--disable-symbolic-links](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#other-options) is set, InnoDB still allows symbolic links and `.isl` files to be created if tables have the `DATA DIRECTORY` option. ([MDEV-26870](https://jira.mariadb.org/browse/MDEV-26870))
* When `CREATE TABLE t1 LIKE t2` is executed and the `t2` table is a partitioned table that uses the MyISAM or Aria storage engines and has the `DATA DIRECTORY` option defined for partitions, the operation fails with a file system error. ([MDEV-25917](https://jira.mariadb.org/browse/MDEV-25917))
* When [sql\_mode=ONLY\_FULL\_GROUP\_BY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode) is set, some window functions incorrectly raise an error with the [ER\_MIX\_OF\_GROUP\_FUNC\_AND\_FIELDS](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) error code. ([MDEV-17785](https://jira.mariadb.org/browse/MDEV-17785))
* When the [JSON\_COMPACT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_compact) function is called with values from a subquery, the output is not always returned as the JSON data type. ([MDEV-18284](https://jira.mariadb.org/browse/MDEV-18284))
* When a system-versioned table is partitioned by [SYSTEM\_TIME\` with a \`\`LIMIT clause, CHECK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table) can incorrectly return an error. ([MDEV-25552](https://jira.mariadb.org/browse/MDEV-25552))
* The lateral derived optimization is not disabled for queries that use `WITH ROLLUP`, which causes queries that use `GROUP BY` to return incorrect results. ([MDEV-26337](https://jira.mariadb.org/browse/MDEV-26337))
* When [optimizer\_switch='split\_materialized=on'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch) is set, queries that use the split optimization can return the wrong results. ([MDEV-27510](https://jira.mariadb.org/browse/MDEV-27510), [MDEV-27132](https://jira.mariadb.org/browse/MDEV-27132))
* When a row is deleted from an InnoDB table, and then a new row with the same key is inserted into the table by a different transaction, InnoDB's MVCC code can incorrectly hide the new row from transactions that should see the changes: (MENT-1414)
  * Consequently, queries can try to insert another new row with the same key, which results in an error with the [ER\_DUP\_ENTRY](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) error code.
  * When a replica server has [slave\_parallel\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) set to '`optimistic`' or '`aggressive`', this can result in the following error in [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status):

```
Last_Errno: 1062
Last_Error: Error 'Duplicate entry 'VALUE' for key 'KEY_NAME'' on query. Default database: 'DATABASE_NAME'. Query: 'INSERT INTO ..'
```

* With MariaDB Enterprise Audit, prepared statements can't be used to enable audit logging. (MENT-379)
  * In previous releases, using a prepared statement to set the `server_audit_logging` system variable would fail with the following error message:

```
ERROR 1 (HY000): Logging cannot be enabled.
```

* When a proxy user is used for authentication, the server checks the proxy user account for the following security controls: ([MDEV-26339](https://jira.mariadb.org/browse/MDEV-26339))
  * SSL/TLS requirements
  * Account locking
  * Password expiration
  * Starting with this release, the server checks the original user account for the security controls mentioned above.
* When [wsrep\_osu\_method='TOI'](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_osu_method) is set with MariaDB Enterprise Cluster, [ALTER SEQUENCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/alter-sequence) is not replicated to other nodes as DDL. ([MDEV-19353](https://jira.mariadb.org/browse/MDEV-19353))
* With MariaDB Enterprise Cluster, a race condition in group commit logic could cause cluster nodes to apply transactions in the wrong order, which could cause the server to fail with an assertion. ([MDEV-27348](https://jira.mariadb.org/browse/MDEV-27348))
  * In the MariaDB Error Log, the message about the assertion failure could look similar to the following:

```
void trx_rseg_update_wsrep_checkpoint(trx_rsegf_t*, const XID*, mtr_t*): Assertion `xid_seqno > wsrep_seqno' failed.
[ERROR] mysqld got signal 6 ;
```

* With the default [optimizer\_use\_condition\_selectivity=4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_use_condition_selectivity), the optimizer could sometimes produce worse execution plans than with [optimizer\_use\_condition\_selectivity=1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_use_condition_selectivity), except when [optimizer\_switch='extended\_keys=off'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch) is set. ([MDEV-25830](https://jira.mariadb.org/browse/MDEV-25830))

### Related to install and upgrade

* When [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) is set, SSTs for MariaDB Enterprise Cluster could fail after upgrading to MariaDB Enterprise Server 10.4 if MariaDB Enterprise Backup is not manually upgraded. ([MDEV-19815](https://jira.mariadb.org/browse/MDEV-19815))
* When the `mysql.AddGeometryColumn` and `mysql.DropGeometryColumn` stored procedures use the old default `DEFINER = 'root@localhost', [mariadb-upgrade##](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-upgrade) does not alter them to use the new default`DEFINER = 'mariadb.sys@localhost'`. ([MDEV-27124](https://jira.mariadb.org/browse/MDEV-27124))`

## Changes in Storage Engines

* This release discontinues support for MariaDB Enterprise ColumnStore 1.4 in MariaDB Enterprise Server 10.4. (MENT-1433)
  * MariaDB recommends using MariaDB Enterprise ColumnStore 6 in MariaDB Enterprise Server 10.6 or MariaDB Enterprise ColumnStore 5 in MariaDB Enterprise Server 10.5.

## Interface Changes

* [ER\_VERS\_NOT\_ALLOWED](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) error code added
* [innodb\_buffer\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_size) system variable minimum value changed from `5242880` to `2097152`
* [innodb\_ft\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_cache_size) system variable dynamic changed from `No` to `Yes`
* [innodb\_ft\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_cache_size) system variable maximum value changed from `80000000` to 1099511627776\`\`
* [innodb\_ft\_total\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_total_cache_size) system variable dynamic changed from `No` to Yes`##`
* [innodb\_ft\_total\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_total_cache_size) system variable maximum value changed from `1600000000` to `1099511627776`
* `mysql_upgrade` [--check-if-upgrade-is-needed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-upgrade#mariadb-upgrade-20) command-line option added
* `mysqld` [--hashicorp-key-management-cache-timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin#hashicorp-key-management-cache-timeout) command-line option added
* `mysqld` [--hashicorp-key-management-cache-version-timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin#hashicorp-key-management-cache-version-timeout) command-line option added
* `mysqld` --rocksdb-ignore-datadic-errors command-line option added
* [rocksdb\_ignore\_datadic\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables) system variable added

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.4.24-15 is provided for:

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
