# Release Notes for MariaDB Enterprise Server 10.2.43-15

MariaDB Enterprise Server 10.2.43-15 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.2. This release includes a variety of fixes.

MariaDB Enterprise Server 10.2.43-15 was released on 2022-03-14.

MariaDB Enterprise Server 10.2 is EOL (end-of-life) as of 2022-05-23. Users of this release series should upgrade to a more recent Enterprise Server release series.

## Fixed Security Vulnerabilities

| CVE (with cve.org link)                                                         | CVSS base score |
| ------------------------------------------------------------------------------- | --------------- |
| [CVE-2021-46668](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46668) | 5.5             |
| [CVE-2021-46665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46665) | 5.5             |
| [CVE-2021-46664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46664) | 5.5             |
| [CVE-2021-46663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46663) | 5.5             |
| [CVE-2021-46661](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46661) | 5.5             |
| [CVE-2021-46659](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46659) | 5.5             |
| [CVE-2022-21595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21595) | 4.4             |

## Notable Changes

* Galera updated to 25.3.35

## Issues Fixed

### Can result in data loss

* Columns in some `INFORMATION_SCHEMA` tables are erroneously declared with `DEFAULT` clauses, which is not compliant with the SQL standard. ([MDEV-18918](https://jira.mariadb.org/browse/MDEV-18918))
  * Consequently, when `sql_mode=EMPTY_STRING_IS_NULL` is set, queries like `CREATE TABLE .. SELECT .. FROM INFORMATION_SCHEMA...` could encounter replication errors like the following:

```
Error 'Invalid default value for 'TABLE_NAME'' on query. Default database: 'test'. Query: 'CREATE TABLE `t1` (`TABLE_NAME` varchar(64) CHARACTER SET utf8 NOT NULL DEFAULT ''
```

### Can result in a hang or crash

* When a `FULLTEXT` index is added to an InnoDB table with `ALGORITHM=INPLACE` and the indexed column uses the tis620 character set, the server can crash with a segmentation fault (signal 11). ([MDEV-24901](https://jira.mariadb.org/browse/MDEV-24901))
* When MariaDB Server is used on the ARM architecture, which uses a weak memory model, an internal hash table implementation can cause the server to crash with a segmentation fault (signal 11). ([MDEV-27088](https://jira.mariadb.org/browse/MDEV-27088))
* When [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) and [innodb\_force\_recovery=1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_force_recovery) are set with MariaDB Enterprise Cluster, powered by Galera, the joiner node fails to perform an SST. ([MDEV-26064](https://jira.mariadb.org/browse/MDEV-26064))
  * The SST log contains the following message related to the failure:

```
mariadb-backup: The option "innodb_force_recovery" should only be used with "--prepare".
mariadb-backup: innodb_init_param(): Error occurred.
```

* When [--stream=xbstream](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) is set, MariaDB Enterprise Backup can hang on lock acquisitions due to a deadlock. ([MDEV-26558](https://jira.mariadb.org/browse/MDEV-26558))
* When a stored procedure is defined with a query that contains a set function, and the set function's only argument is an outer reference to a column of a mergeable view, a derived table, or a CTE, the second execution of the stored procedure can cause the server to crash. ([MDEV-25086](https://jira.mariadb.org/browse/MDEV-25086))
* When a derived table is created for certain queries that use subqueries over Views or CTEs, the server can crash with a segmentation fault (signal 11). ([MDEV-25631](https://jira.mariadb.org/browse/MDEV-25631))
* When a stored procedure uses a cursor to run a query that requires an internal temporary table (such as queries containing an ORDER BY clause), the server can crash due to a segmentation fault (signal 11). ([MDEV-24827](https://jira.mariadb.org/browse/MDEV-24827))
* Server can crash if a CTE or derived table is not used by the query. ([MDEV-25766](https://jira.mariadb.org/browse/MDEV-25766))
* When [log\_slow\_verbosity = 'explain'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_slow_verbosity) is set and a query is executed that references a derived table, the server can crash while writing the query's execution plan to the slow query log. ([MDEV-26249](https://jira.mariadb.org/browse/MDEV-26249))
* When a stored procedure or a prepared statement is used to execute a query that performs a join which compares a `GEOMETRY` column with a different data type, executing the stored procedure or prepared statement twice can cause the server to crash. ([MDEV-20770](https://jira.mariadb.org/browse/MDEV-20770))
* With MariaDB Enterprise Cluster, when [wsrep\_cluster\_address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_cluster_address) is set to an unknown address and [wsrep\_slave\_threads](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_slave_threads) is set to `0`, the server crashes. ([MDEV-25472](https://jira.mariadb.org/browse/MDEV-25472))

### Can result in unexpected behavior

* When a multi-byte character set is used, the last character of a [TINYTEXT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/tinytext) column can be truncated, which makes it appear as a question mark (`'?`). ([MDEV-24335](https://jira.mariadb.org/browse/MDEV-24335))
* Subquery using the `ALL` keyword on [TIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/time) columns produces a wrong result. ([MDEV-27098](https://jira.mariadb.org/browse/MDEV-27098))
* Subquery using the `ALL` keyword on [DATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/date) columns produces a wrong result. ([MDEV-27072](https://jira.mariadb.org/browse/MDEV-27072))
* When float literals are defined using scientific notation and the token also contains certain special characters, the parser incorrectly parses the float value and completely drops it from the request. ([MDEV-27066](https://jira.mariadb.org/browse/MDEV-27066))
* When a double-encapsulated CTE query calls a function which reads a table that has been aliased in the CTE query, the server incorrectly raises an error with the [ER\_NO\_SUCH\_TABLE](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) error code. ([MDEV-26825](https://jira.mariadb.org/browse/MDEV-26825))
* When a CTE is used in a subquery of a [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) statement, the server incorrectly raises an error with the [ER\_NO\_DB\_ERROR](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) error code. ([MDEV-26470](https://jira.mariadb.org/browse/MDEV-26470))
* When MariaDB Enterprise Cluster performs an SST, the SST scripts incorrectly try to read [ssl\_ca](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables) as a path to a directory of TLS CA certificates instead of using [ssl\_capath](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables) for that purpose. ([MDEV-27181](https://jira.mariadb.org/browse/MDEV-27181))
* When MariaDB Enterprise Cluster performs an SST, the SST scripts do not always interpret [log\_bin\_index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) correctly. ([MDEV-26915](https://jira.mariadb.org/browse/MDEV-26915))
* When an index is used for an `ORDER BY .. LIMIT` query, the optimizer does not disable the `Range Checked for Each Record` optimization. ([MDEV-27270](https://jira.mariadb.org/browse/MDEV-27270))
* When [optimizer\_switch='index\_merge\_sort\_intersection=on'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch) is set, the optimizer can incorrectly choose to merge an index that does not help, because the query conditions require the full index to be scanned. ([MDEV-27262](https://jira.mariadb.org/browse/MDEV-27262))
* When the [version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#version) system variable is set, MariaDB Connector/C and the [mariadb](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb/README.md) client do not interpret MariaDB Server's extended metadata properly, which can cause results from some [SHOW ..](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show) to be right-aligned. ([MDEV-27304](https://jira.mariadb.org/browse/MDEV-27304))
* When an `INSERT .. SELECT` statement selects from and inserts into the same table, rows are counted twice, which can cause row numbers to be reported incorrectly in error messages. ([MDEV-26698](https://jira.mariadb.org/browse/MDEV-26698))
* When a replica server's relay log is rotated, `Seconds_Behind_Master` in [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-status-variables) can temporarily show an incorrect value that is very high. ([MDEV-16091](https://jira.mariadb.org/browse/MDEV-16091))
* The `collation` column in the [information\_schema.STATISTICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table) table is incorrectly read as `NULL`. ([MDEV-4621](https://jira.mariadb.org/browse/MDEV-4621))
* When a join performs a comparison between an expression that uses a case-insensitive collation and an ENUM column that uses a binary collation, the comparison uses the wrong collation, which can cause results to be incorrect. ([MDEV-26129](https://jira.mariadb.org/browse/MDEV-26129))
* When [innodb\_buffer\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_size) is changed dynamically with [SET GLOBAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set), InnoDB does not enforce the minimum value that is enforced on startup, which can result in an impossibly small buffer pool with some values of [innodb\_buffer\_pool\_chunk\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_chunk_size). ([MDEV-27467](https://jira.mariadb.org/browse/MDEV-27467))
* When the [DATABASE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/database) function is used in some queries (such as queries using `UNION ALL`), database names can be truncated to 34 characters, even though database names can have up to 64 characters. ([MDEV-27544](https://jira.mariadb.org/browse/MDEV-27544))
* When the [--symbolic-links](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#-symbolic-links) option is disabled, such as when `--skip-symbolic-links` or `--disable-symbolic-links` is set, InnoDB still allows symbolic links and `.is`l files to be created if tables have the `DATA DIRECTORY` option. ([MDEV-26870](https://jira.mariadb.org/browse/MDEV-26870))
* When `CREATE TABLE t1 LIKE t2` is executed and the `t2` table is a partitioned table that uses the MyISAM or Aria storage engines and has the DATA DIRECTORY option defined for partitions, the operation fails with a file system error. ([MDEV-25917](https://jira.mariadb.org/browse/MDEV-25917))
* When [sql\_mode=ONLY\_FULL\_GROUP\_BY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode) is set, some window functions incorrectly raise an error with the [ER\_MIX\_OF\_GROUP\_FUNC\_AND\_FIELDS](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) error code. ([MDEV-17785](https://jira.mariadb.org/browse/MDEV-17785))
* When `DEFAULT(COLUMN_NAME)` is used in a `WHERE` clause, the result can be incorrect. ([MDEV-21639](https://jira.mariadb.org/browse/MDEV-21639))
* When a CTE is used with a `UNION` in a [CREATE TABLE .. AS ..](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) statement, the server incorrectly raises an error with the [ER\_NO\_DB\_ERROR](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) error code. ([MDEV-27086](https://jira.mariadb.org/browse/MDEV-27086))
* When the [JSON\_COMPACT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_compact) function is called with values from a subquery, the output is not always returned as the [JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/json) data type. ([MDEV-18284](https://jira.mariadb.org/browse/MDEV-18284))

### Related to install and upgrade

* When [wsrep\_sst\_method=mariadb-backup](../../10-2/broken-reference/) is set for MariaDB Enterprise Cluster, but MariaDB Enterprise Backup is not installed on the joiner node, the joiner node fails to start. ([MDEV-15209](https://jira.mariadb.org/browse/MDEV-15209))

## Interface Changes

* [innodb\_buffer\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_buffer_pool_size) system variable minimum value changed from 5242880 to 2097152
* `mysql_upgrade` [--check-if-upgrade-is-needed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#check-if-upgrade-is-needed) command-line option added
* `mysqld` [--rocksdb-ignore-datadic-errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#rocksdb-ignore-datadic-errors) command-line option added
* [rocksdb\_ignore\_datadic\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#rocksdb_ignore_datadic_errors) system variable added

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.2.43-15 is provided for:

* CentOS 7 (x86\_64)
* Debian 9 (x86\_64, ARM64)
* Microsoft Windows (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 18.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".\*

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
