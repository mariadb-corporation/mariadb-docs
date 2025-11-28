# Release Notes for MariaDB Enterprise Server 10.5.15-10

MariaDB Enterprise Server 10.5.15-10 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.5. This release includes a variety of fixes.

MariaDB Enterprise Server 10.5.15-10 was released on 2022-03-14.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/cve.org) link) | CVSS base score |
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
* On Windows, `core_file` is enabled by default. ([MDEV-18439](https://jira.mariadb.org/browse/MDEV-18439))
* New system variables have been added for the HashiCorp Key Management Plugin: (MENT-864)
  * `hashicorp_key_management_cache_timeout` defines the time (in milliseconds) after which the value of the key stored in the cache becomes invalid, and an attempt to read this data causes a new request to be sent to the vault server. If the value is 0, then the keys will always be considered invalid, but they are still used if the vault server is unavailable and `hashicorp_key_management_use_cache_on_timeout` is enabled. By default, the value is `60000` (1 minute).
  * `hashicorp_key_management_cache_version_timeout` defines the time (in milliseconds) after which the information about latest version number of the key (which is stored in the cache) becomes invalid and an attempt to read this information causes a new request to be sent to the vault server. If the value is `0`, then information about latest key version numbers always considered invalid, but they are still used if the vault server is unavailable and `hashicorp_key_management_use_cache_on_timeout` is enabled. By default, the value is `0`.
  * For maximum flexibility, both of the new system variables can be configured with the `loose` prefix:

```
[mariadb]
loose_hashicorp_key_management_cache_timeout=120000
loose_hashicorp_key_management_cache_version_timeout=120000
```

* Crash recovery improvements for InnoDB ([MDEV-26784](https://jira.mariadb.org/browse/MDEV-26784), [MDEV-27022](https://jira.mariadb.org/browse/MDEV-27022), [MDEV-27183](https://jira.mariadb.org/browse/MDEV-27183), [MDEV-27610](https://jira.mariadb.org/browse/MDEV-27610))
* The default value of [innodb\_change\_buffering](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_change_buffering) has been changed to none. ([MDEV-27734](https://jira.mariadb.org/browse/MDEV-27734))

## Issues Fixed

### Can result in data loss

* Columns in some `INFORMATION_SCHEMA` tables are erroneously declared with `DEFAULT` clauses, which is not compliant with the SQL standard. ([MDEV-18918](https://jira.mariadb.org/browse/MDEV-18918))
  * Consequently, when `sql_mode=EMPTY_STRING_IS_NULL` is set, queries like `CREATE TABLE .. SELECT .. FROM INFORMATION_SCHEMA...` could encounter replication errors like the following:

```
Error 'Invalid default value for 'TABLE_NAME'' on query. Default database: 'test'. Query: 'CREATE TABLE `t1` (`TABLE_NAME` varchar(64) CHARACTER SET utf8 NOT NULL DEFAULT ''
```

* When an [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) statement changes the order of indexes in a MyISAM or Aria table using the `INPLACE` algorithm, the table can become corrupt. ([MDEV-25803](https://jira.mariadb.org/browse/MDEV-25803))
* When [CREATE OR REPLACE SEQUENCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/create-sequence) is written to the binary log, the statement is not flagged as DDL, which causes the replica servers to execute the statement in an unsafe way if parallel replication is enabled. ([MDEV-27365](https://jira.mariadb.org/browse/MDEV-27365))
* After upgrading from [MariaDB 10.3](../../../community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md) or earlier, the names of some triggers can appear empty, and the trigger can't be dropped. ([MDEV-25659](https://jira.mariadb.org/browse/MDEV-25659))

### Can result in a hang or crash

* When a `FULLTEXT` index is added to an InnoDB table with `ALGORITHM=INPLACE` and the indexed column uses the `tis620` character set, the server can crash with a segmentation fault (signal 11). ([MDEV-24901](https://jira.mariadb.org/browse/MDEV-24901))
* When MariaDB Server is used on the ARM architecture, which uses a weak memory model, an internal hash table implementation can cause the server to crash with a segmentation fault (signal 11). ([MDEV-27088](https://jira.mariadb.org/browse/MDEV-27088))
* When [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) and [innodb\_force\_recovery=1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_force_recovery) are set with MariaDB Enterprise Cluster, powered by Galera, the joiner node fails to perform an SST. ([MDEV-26064](https://jira.mariadb.org/browse/MDEV-26064))
  * The SST log contains the following message related to the failure:

```
mariadb-backup: The option "innodb_force_recovery" should only be used with "--prepare".
mariadb-backup: innodb_init_param(): Error occurred.
```

* When [--stream=xbstream](../../10-5/broken-reference/) is set, MariaDB Enterprise Backup can hang on lock acquisitions due to a deadlock. ([MDEV-26558](https://jira.mariadb.org/browse/MDEV-26558))
* When a stored procedure is defined with a query that contains a set function, and the set function's only argument is an outer reference to a column of a mergeable view, a derived table, or a CTE, the second execution of the stored procedure can cause the server to crash. ([MDEV-25086](https://jira.mariadb.org/browse/MDEV-25086))
* When a derived table is created for certain queries that use subqueries over Views or CTEs, the server can crash with a segmentation fault (signal 11). ([MDEV-25631](https://jira.mariadb.org/browse/MDEV-25631))
* When a stored procedure uses a cursor to run a query that requires an internal temporary table (such as queries containing an ORDER BY clause), the server can crash due to a segmentation fault (signal 11). ([MDEV-24827](https://jira.mariadb.org/browse/MDEV-24827))
* Server can crash if a CTE or derived table is not used by the query. ([MDEV-25766](https://jira.mariadb.org/browse/MDEV-25766))
* When [log\_slow\_verbosity = 'explain'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_slow_verbosity) is set and a query is executed that references a derived table, the server can crash while writing the query's execution plan to the slow query log. ([MDEV-26249](https://jira.mariadb.org/browse/MDEV-26249))
* When a stored procedure or a prepared statement is used to execute a query that performs a join which compares a `GEOMETRY` column with a different data type, executing the stored procedure or prepared statement twice can cause the server to crash. ([MDEV-20770](https://jira.mariadb.org/browse/MDEV-20770))
* When a [system versioned table](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/system-versioned-table/README.md) is created with [character\_set\_server=utf8mb4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#character_set_server) and [collation\_server=utf8mb4\_unicode\_1400\_ci](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#collation_server), the server can crash. ([MDEV-27195](https://jira.mariadb.org/browse/MDEV-27195))
* When a [system-versioned table](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/system-versioned-table/README.md) is partitioned by `SYSTEM_TIME`, executing `DELETE FROM .. PARTITION(..)` causes the server to crash. ([MDEV-27217](https://jira.mariadb.org/browse/MDEV-27217))
* When the following conditions are met, executing a prepared statement twice can cause the server to crash: ([MDEV-23182](https://jira.mariadb.org/browse/MDEV-23182))
  * The [in\_predicate\_conversion\_threshold](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#in_predicate_conversion_threshold) system variable must be set to some value n.
  * The query must contain an `IN(...)` clause with more than n string literals.
  * The query must require character set conversions.
* After completing a successful SST with MariaDB Enterprise Cluster, [wsrep\_local\_state\_comment](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables) on the donor node still says `'Donor/Desynced'`. ([MDEV-27459](https://jira.mariadb.org/browse/MDEV-27459))
* With MariaDB Enterprise Cluster, when [REPAIR VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/repair-view) is executed on a view that references [information\_schema.TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables), the server can crash. ([MDEV-25538](https://jira.mariadb.org/browse/MDEV-25538))
* When [ALTER TABLE .. ADD COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) is used to instantly add columns in the middle of an InnoDB table, and then the tablespace is exported with [FLUSH TABLES .. FOR EXPORT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush), and then the tablespace is re-imported with [ALTER TABLE .. IMPORT TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush), the server can crash. ([MDEV-27272](https://jira.mariadb.org/browse/MDEV-27272))
* When [optimizer\_switch='not\_null\_range\_scan=on'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch) is set, the server can crash if an index on an InnoDB table is used to check a condition that can evaluate to `NULL`. ([MDEV-22846](https://jira.mariadb.org/browse/MDEV-22846))
* When a [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) table uses a \[\[|FLOAT|##FLOAT##]] column, the server can crash with an assertion failure. ([MDEV-27184](https://jira.mariadb.org/browse/MDEV-27184))
  * In the MariaDB error log, the following error message could be written about the assertion failure:

```
Assertion `(old_top == initial_top (av) && old_size == 0) || ((unsigned long) (old_size) >= MINSIZE && prev_inuse (old_top) && ((unsigned long) old_end & (pagesize - 1)) == 0)' failed.
```

* With MariaDB Enterprise Cluster, when a [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) statement that defines a Foreign Key constraint is replicated to other cluster nodes, the nodes could apply the statement in parallel with other DML statements that affect the Foreign Key constraint, which causes the node to fail with an assertion failure. ([MDEV-27276](https://jira.mariadb.org/browse/MDEV-27276))
* With MariaDB Enterprise Cluster, when two transactions delete a row from two separate InnoDB tables in parallel and a foreign key causes a delete to cascade for both transactions to the same row in a third table, the server can crash with an assertion failure. ([MDEV-26803](https://jira.mariadb.org/browse/MDEV-26803), [MDEV-26298](https://jira.mariadb.org/browse/MDEV-26298))
  * In previous releases, this issue could be avoided by setting [wsrep\_slave\_threads=1](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_slave_threads).
  * In the MariaDB error log, the following error message about the assertion failure could be written:

```
int wsrep::client_state::bf_abort(wsrep::seqno): Assertion `mode_ == m_local || transaction_.is_streaming()' failed.
[ERROR] mysqld got signal 6 ;
```

* When [innodb\_flush\_log\_at\_trx\_commit=2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_flush_log_at_trx_commit) and [innodb\_flush\_method=O\_DSYNC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_flush_method) are set, the server could crash with an assertion failure. ([MDEV-27754](https://jira.mariadb.org/browse/MDEV-27754))
  * In the MariaDB error log, the following message about the assertion failure could be written:

```
InnoDB: Failing assertion: lsn >= log_sys.get_flushed_lsn()
```

* When InnoDB does not use RAM disk for storage, the server can occasionally hang during a log checkpoint. ([MDEV-27416](https://jira.mariadb.org/browse/MDEV-27416))
* When using [Enterprise Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider), the server can crash due to memory corruption. ([MDEV-27240](https://jira.mariadb.org/browse/MDEV-27240))
* When [mariadbd --help](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#-help) is executed, the server could try to lock the Aria control file. ([MDEV-24788](https://jira.mariadb.org/browse/MDEV-24788))
  * In the MariaDB error log, the following error messages could be written about this:

```
[ERROR] mysqld: Can't lock aria control file '/var/lib/mysql/aria_log_control' for exclusive use, error: 11. Will retry for 0 seconds
[ERROR] Plugin 'Aria' init function returned error.
[ERROR] Plugin 'Aria' registration as a STORAGE ENGINE failed.
```

* When an index is dropped and re-adding to a table in a different position using the `INPLACE` algorithm and the table uses the `MEMORY` storage engine, the server can crash. ([MDEV-25555](https://jira.mariadb.org/browse/MDEV-25555))

### `Can result in unexpected behavior`

* When a multi-byte character set is used, the last character of a [TINYTEXT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/tinytext) column can be truncated, which makes it appear as a question mark ('?). ([MDEV-24335](https://jira.mariadb.org/browse/MDEV-24335))
* Subquery using the `ALL` keyword on [TIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/time) columns produces a wrong result. ([MDEV-27098](https://jira.mariadb.org/browse/MDEV-27098))
* Subquery using the `ALL` keyword on [DATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/date) columns produces a wrong result. ([MDEV-27072](https://jira.mariadb.org/browse/MDEV-27072))
* When float literals are defined using scientific notation and the token also contains certain special characters, the parser incorrectly parses the float value and completely drops it from the request. ([MDEV-27066](https://jira.mariadb.org/browse/MDEV-27066))
* When a double-encapsulated CTE query calls a function which reads a table that has been aliased in the CTE query, the server incorrectly raises an error with the `ER_NO_SUCH_TABLE` error code. ([MDEV-26825](https://jira.mariadb.org/browse/MDEV-26825))
* When a CTE is used in a subquery of a `DELETE` statement, the server incorrectly raises an error with the [ER\_NO\_DB\_ERROR error code](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-5/broken-reference/README.md). ([MDEV-26470](https://jira.mariadb.org/browse/MDEV-26470))
* When MariaDB Enterprise Cluster performs an SST, the SST scripts incorrectly try to read [ssl\_ca](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables) as a path to a directory of TLS CA certificates instead of using [ssl\_capath](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables) for that purpose. ([MDEV-27181](https://jira.mariadb.org/browse/MDEV-27181))
* When MariaDB Enterprise Cluster performs an SST, the SST scripts do not always interpret [log\_bin\_index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) correctly. ([MDEV-26915](https://jira.mariadb.org/browse/MDEV-26915))
* When an index is used for an `ORDER BY .. LIMIT` query, the optimizer does not disable the `Range Checked for Each Record` optimization. ([MDEV-27270](https://jira.mariadb.org/browse/MDEV-27270))
* When [optimizer\_switch='index\_merge\_sort\_intersection=on'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch) is set, the optimizer can incorrectly choose to merge an index that does not help, because the query conditions require the full index to be scanned. ([MDEV-27262](https://jira.mariadb.org/browse/MDEV-27262))
* When the [version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#version) system variable is set, MariaDB Connector/C and the [mariadb client](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb/README.md) do not interpret MariaDB Server's extended metadata properly, which can cause results from some `SHOW ..` to be right-aligned. ([MDEV-27304](https://jira.mariadb.org/browse/MDEV-27304))
* When an `INSERT .. SELECT` statement selects from and inserts into the same table, rows are counted twice, which can cause row numbers to be reported incorrectly in error messages. ([MDEV-26698](https://jira.mariadb.org/browse/MDEV-26698))
* When a replica server's relay log is rotated, `Seconds_Behind_Master` in [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status) can temporarily show an incorrect value that is very high. ([MDEV-16091](https://jira.mariadb.org/browse/MDEV-16091))
* The `collation` column in the [information\_schema.STATISTICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables) table is incorrectly read as NULL. ([MDEV-4621](https://jira.mariadb.org/browse/MDEV-4621))
* When a join performs a comparison between an expression that uses a case-insensitive collation and an [ENUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/enum) column that uses a binary collation, the comparison uses the wrong collation, which can cause results to be incorrect. ([MDEV-26129](https://jira.mariadb.org/browse/MDEV-26129))
* When [innodb\_buffer\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_size) is changed dynamically with [SET GLOBAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set), InnoDB does not enforce the minimum value that is enforced on startup, which can result in an impossibly small buffer pool with some values of [innodb\_buffer\_pool\_chunk\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_size). ([MDEV-27467](https://jira.mariadb.org/browse/MDEV-27467))
* When the [DATABASE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/database) function is used in some queries (such as queries using `UNION ALL`), database names can be truncated to 34 characters, even though database names can have up to 64 characters. ([MDEV-27544](https://jira.mariadb.org/browse/MDEV-27544))
* When the [--symbolic-links](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#-symbolic-links) option is disabled, such as when `--skip-symbolic-links` or `--disable-symbolic-links` is set, InnoDB still allows symbolic links and `.isl` files to be created if tables have the `DATA DIRECTORY` option. ([MDEV-26870](https://jira.mariadb.org/browse/MDEV-26870))
* When `CREATE TABLE t1 LIKE t2` is executed and the `t2` table is a partitioned table that uses the MyISAM or Aria storage engines and has the `DATA DIRECTORY` option defined for partitions, the operation fails with a file system error. ([MDEV-25917](https://jira.mariadb.org/browse/MDEV-25917))
* When [sql\_mode=ONLY\_FULL\_GROUP\_BY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) is set, some window functions incorrectly raise an error with the [ER\_MIX\_OF\_GROUP\_FUNC\_AND\_FIELDS](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-5/broken-reference/README.md) error code. ([MDEV-17785](https://jira.mariadb.org/browse/MDEV-17785))
* When a system-versioned table is partitioned by `SYSTEM_TIME` with a `LIMIT` clause, `CHECK TABLE` can incorrectly return an error. ([MDEV-25552](https://jira.mariadb.org/browse/MDEV-25552))
* The lateral derived optimization is not disabled for queries that use `WITH ROLLUP`, which causes queries that use `GROUP BY` to return incorrect results. ([MDEV-26337](https://jira.mariadb.org/browse/MDEV-26337))
* When [optimizer\_switch='split\_materialized=on'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch) is set, queries that use the split optimization can return the wrong results. ([MDEV-27510](https://jira.mariadb.org/browse/MDEV-27510), [MDEV-27132](https://jira.mariadb.org/browse/MDEV-27132))
* When a row is deleted from an InnoDB table, and then a new row with the same key is inserted into the table by a different transaction, InnoDB's MVCC code can incorrectly hide the new row from transactions that should see the changes: (MENT-1414)
  * Consequently, queries can try to insert another new row with the same key, which results in an error with the [ER\_DUP\_ENTRY](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-5/broken-reference/README.md) error code.
  * When a replica server has [slave\_parallel\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) set to `'optimistic'` or `'aggressive'`, this can result in the following error in `SHOW REPLICA STATUS`:

```
Last_Errno: 1062
Last_Error: Error 'Duplicate entry 'VALUE' for key 'KEY_NAME'' on query. Default database: 'DATABASE_NAME'. Query: 'INSERT INTO ..'
```

* With MariaDB Enterprise Audit, prepared statements can't be used to enable audit logging. (MENT-379)
  * In previous releases, using a prepared statement to set the [server\_audit\_logging](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables) system variable would fail with the following error message:

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
  * In the MariaDB Error Log, the message about the assertion failure could look similar to the following:\
    void trx\_rseg\_update\_wsrep\_checkpoint(trx\_rsegf\_t\*, const XID\*, mtr\_t\*): Assertion \`xid\_seqno > wsrep\_seqno' failed.\
    \[ERROR] mysqld got signal 6 ;
* When the query cache is enabled and older clients or connectors that don't support the `CLIENT_EXTENDED_METADATA` capability flag are used, queries could fail with an unknown error. ([MDEV-24487](https://jira.mariadb.org/browse/MDEV-24487))
  * As part of the fix, the `CLIENT_EXTENDED_METADATA` column has been added to the [information\_schema.QUERY\_CACHE\_INFO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-query_cache_info-table) table.
* When [JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/json) is used with single row sub-selects or hybrid functions (such as `IF()` and `COALESCE()`), the results could be considered normal strings instead of JSON. ([MDEV-27018](https://jira.mariadb.org/browse/MDEV-27018))
* A performance regression exists for updates to InnoDB tables that do not use an index. ([MDEV-27499](https://jira.mariadb.org/browse/MDEV-27499))
* With MariaDB Enterprise Cluster, when [wsrep\_gtid\_mode=ON](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_gtid_mode) is set and the value of [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is changed to a new value, transactions still use the old `server_id` value in GTIDs. ([MDEV-26223](https://jira.mariadb.org/browse/MDEV-26223))
* When `OFFSET` is combined with `SELECT DISTINCT, a JOIN, and IN(..), OFFSET` is ignored. ([MDEV-27382](https://jira.mariadb.org/browse/MDEV-27382))
* When a numeric argument is provided to `COLLATE`, the server always uses a collation of the `latin1` character set instead of a collation of [character\_set\_connection](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#character_set_connection). ([MDEV-24584](https://jira.mariadb.org/browse/MDEV-24584))
  * When a `COLLATE` clause specifies a collation of [character\_set\_connection](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#character_set_connection), the query could fail with the following error message:

```
ERROR 1253 (42000): COLLATION ' …' is not valid for CHARACTER SET 'latin1'
```

### Related to install and upgrade

* When the `mysql.AddGeometryColumn` and `mysql.DropGeometryColumn` stored procedures use the old default `DEFINER = 'root@localhost',` [mariadb-upgrade](../../10-5/broken-reference/) does not alter them to use the new default `DEFINER = 'mariadb.sys@localhost'`. ([MDEV-27124](https://jira.mariadb.org/browse/MDEV-27124))
* When MariaDB Server is upgraded from 10.2, 10.3, or 10.4, InnoDB upgrades the redo log format in a manner that is not crash-safe. ([MDEV-27190](https://jira.mariadb.org/browse/MDEV-27190))

## Changes in Storage Engines

* This release incorporates MariaDB ColumnStore storage engine version 5.6.5.

## `Interface Changes`

* [ER\_VERS\_NOT\_ALLOWED](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-5/broken-reference/README.md) error code added
* [innodb\_buffer\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_size) system variable minimum value changed from `5242880` to `2097152`
* [innodb\_ft\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_cache_size) system variable dynamic changed from `No` to `Yes`
* [innodb\_ft\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_cache_size) system variable maximum value changed from `80000000` to `1099511627776`
* [innodb\_ft\_total\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_total_cache_size) system variable dynamic changed from `No` to `Yes`
* [innodb\_ft\_total\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_total_cache_size) system variable maximum value changed from `1600000000` to `1099511627776`
* `mariadb-upgrade` --check-if-upgrade-is-needed command-line option added
* `mariadbd` --hashicorp-key-management-cache-timeout command-line option added
* `mariadbd` --hashicorp-key-management-cache-version-timeout command-line option added
* `mariadbd` --rocksdb-ignore-datadic-errors command-line option added
* [brocksdb\_ignore\_datadic\_errors](../../10-5/broken-reference/) system variable added

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.5.15-10 is provided for:

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

* [MariaDB Enterprise Server ](../../11.4/whats-new.md)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.5](../../11.4/whats-new.md)
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

* [Upgrade to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-from-mariadb-10-5-to-mariadb-10-6)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
