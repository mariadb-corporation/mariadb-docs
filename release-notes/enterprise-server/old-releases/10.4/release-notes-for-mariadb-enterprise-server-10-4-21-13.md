# Release Notes for MariaDB Enterprise Server 10.4.21-13

This thirteenth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4 is a maintenance release. This release includes a variety of fixes.

MariaDB Enterprise Server 10.4.21-13 was released on 2021-09-14.

## Fixed Security Vulnerabilities

| CVE (with cve.org link)                                                         | CVSS base score |
| ------------------------------------------------------------------------------- | --------------- |
| [CVE-2021-2389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2389)   | 5.9             |
| [CVE-2021-46666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46666) | 5.5             |
| [CVE-2021-46658](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46658) | 5.5             |
| [CVE-2021-46657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46657) | 5.5             |
| [CVE-2021-2372](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2372)   | 4.4             |

## Backported Features

This release of MariaDB Enterprise Server includes features backported from MariaDB Enterprise Server 10.6.

* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) allows database-specific and table-specific filters. (MENT-65)\
  For example:

```
{
 "connect_event" : "ALL",
 "table_event" : ["READ","WRITE",{"ignore_tables" : "mysql.*"}],
 "query_event" : ["DDL",{"tables" : "test.t2"}]
}
```

* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) can be configured to not start the server if Audit Filters are invalid. (MENT-1243)
  * Added the new [server\_audit\_load\_on\_error](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables) system variable.
  * To configure server startup to fail if Audit Filters are invalid, set [server\_audit\_load\_on\_error](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables) to OFF and set server-audit to `FORCE` or `FORCE_PLUS_PERMANENT`.
  * The default value of [server\_audit\_load\_on\_error](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables) is `ON`, so the default behavior is the same as in prior releases.
* Enhanced consistency for Semi-Sync Replication
  * When [rpl\_semi\_sync\_slave\_enabled=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/semisynchronous-replication#rpl_semi_sync_slave_enabled), consistency is guaranteed for a Primary server in an HA (Primary/Replica) topology when using semi-synchronous replication. ([MDEV-21117](https://jira.mariadb.org/browse/MDEV-21117))
  * Prior to this release, when using semi-synchronous replication, if a Primary crashed before sending a transaction to the Replica, on restart the Primary could recover incomplete InnoDB transactions when rejoining as a Replica.
  * With this release, when using semi-synchronous replication and with `rpl_semi_sync_slave_enabled=ON`, incomplete transactions will be rolled-back on the Replica, ensuring the new Primary (former Replica) and new Replica (former Primary) remain in sync.

This release of MariaDB Enterprise Server includes features backported from MariaDB Enterprise Server 10.5.

* Support added for Galera Global Transaction ID in MariaDB Enterprise Cluster (Galera), which replicates MariaDB Global Transaction ID to other nodes in the cluster (MENT-932)

## Notable Changes

* Galera updated to 26.4.9
* ARM64 is now supported for several [#platforms](release-notes-for-mariadb-enterprise-server-10-4-21-13.md#platforms).
* The script `wsrep_sst_mariadb-backup` checks all server-related configuration groups when processing a configuration file. ([MDEV-25669](https://jira.mariadb.org/browse/MDEV-25669))
  * Prior to this release, only the \[`mysqld`] configuration group was checked when processing a configuration file.
* MariaDB Enterprise Backup expects [--stream=mbstream](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) to stream a backup using the included `mbstream` utility. ([MDEV-15730](https://jira.mariadb.org/browse/MDEV-15730))
  * Prior to this release, MariaDB Enterprise Backup expected [--stream=xbstream](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md), even though the `xbstream` utility had been renamed to `mbstream`.
* InnoDB no longer acquires advisory file locks by default. ([MDEV-24393](https://jira.mariadb.org/browse/MDEV-24393))
* The [information\_schema.KEYWORDS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-keywords-table) table has been added and can be used to view details about SQL keywords. ([MDEV-25129](https://jira.mariadb.org/browse/MDEV-25129))
* The [information\_schema.SQL\_FUNCTIONS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-sql_functions-table) table has been added and can be used to view details about built-in functions. ([MDEV-25129](https://jira.mariadb.org/browse/MDEV-25129))
* When using data-at-rest encryption with the [file-key-management-encryption-plugin/](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin) encryption plugin, InnoDB will automatically disable key rotation checks. ([MDEV-14180](https://jira.mariadb.org/browse/MDEV-14180))
  * The [file-key-management-encryption-plugin/](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin) encryption plugin does not support key rotation, so key rotation checks are not required.
  * In previous releases, unnecessary key rotation checks with the [file-key-management-encryption-plugin/](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin) encryption plugin could reduce performance, unless they were explicitly disabled by setting [innodb\_encryption\_rotate\_key\_age=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encryption_rotate_key_age).
* Removed SSL ciphers RC4-MD5 and RC4-SHA for [mariadbd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) binaries compiled with WolfSSL. ([MDEV-26092](https://jira.mariadb.org/browse/MDEV-26092))

## Issues Fixed

### Can result in data loss

* When an [ALTER TABLE ... ADD COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) statement is executed with `ALGORITHM=INSTANT`, a warning is not raised when the operation causes the default value of a `DATE` column to be truncated. ([MDEV-25971](https://jira.mariadb.org/browse/MDEV-25971))

### Can result in a hang or crash

* Possible server crash when pushing a `WHERE` condition over a mergeable derived table / view / CTE DT into a grouping view / derived table / CTE V whose item list contained set functions with constant arguments. ([MDEV-25635](https://jira.mariadb.org/browse/MDEV-25635))
* Server crashes on second execution of a stored procedure or a prepared statement when the corresponding query executes a window function on a view, CTE, or derived table. ([MDEV-25565](https://jira.mariadb.org/browse/MDEV-25565))
* Server crashes possible when executing a prepared statement with a hanging recursive CTE. ([MDEV-26135](https://jira.mariadb.org/browse/MDEV-26135))
* Server crashes while executing query with a CTE in a prepared statement or stored procedure. ([MDEV-26025](https://jira.mariadb.org/browse/MDEV-26025))
* Server crashes while executing query with a recursive CTE that is indirectly used twice. ([MDEV-26202](https://jira.mariadb.org/browse/MDEV-26202))
* Server crashes due to infinite recursion while processing an embedded recursive CTE with missing `RECURSIVE`. ([MDEV-26095](https://jira.mariadb.org/browse/MDEV-26095))
* Server crashes in InnoDB deadlock checker under high load. ([MDEV-25594](https://jira.mariadb.org/browse/MDEV-25594))
* Server crashes when a virtual generated column has a prefix index. ([MDEV-26220](https://jira.mariadb.org/browse/MDEV-26220))
* Server crashes possible when using virtual generated columns. ([MDEV-18166](https://jira.mariadb.org/browse/MDEV-18166), [MDEV-18249](https://jira.mariadb.org/browse/MDEV-18249))
* Server crashes while executing [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) when a [YEAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/year) column is truncated. ([MDEV-17890](https://jira.mariadb.org/browse/MDEV-17890))
* Server crashes while executing [SET ROLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/set-role) when a hostname cannot be resolved. ([MDEV-26081](https://jira.mariadb.org/browse/MDEV-26081))
* Server crashes when a subquery references an outer column in an `ORDER BY` clause. ([MDEV-25629](https://jira.mariadb.org/browse/MDEV-25629))
* Server crashes due to a stack overrun in the query optimizer while executing query with more than 32 equality conditions that compare columns of different tables (such as `tableX.colX=tableY.colY`). ([MDEV-17783](https://jira.mariadb.org/browse/MDEV-17783))
* Server crashes when a window function is the left expression of an `IN(SELECT ..)` subquery. ([MDEV-25630](https://jira.mariadb.org/browse/MDEV-25630))
* Possible deadlock on a Replica server using GTID Replication when [slave\_parallel\_mode=optimistic](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) and [OPTIMIZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table), [REPAIR TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/repair-table), or [ANALYZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/analyze-table) is executed. ([MDEV-17515](https://jira.mariadb.org/browse/MDEV-17515))
* Server crashes when [ALTER TABLE .. ADD FULLTEXT INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) fails on an InnoDB table. ([MDEV-25721](https://jira.mariadb.org/browse/MDEV-25721))
* Server crashes while executing [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate) on an InnoDB table with a Full-Text Index. ([MDEV-25663](https://jira.mariadb.org/browse/MDEV-25663))
* Server crashes while executing [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) on an InnoDB table with virtual generated columns that are indexed. ([MDEV-25872](https://jira.mariadb.org/browse/MDEV-25872))
* Server crashes while executing [CHECK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table) when innodb\_read\_only is enabled. ([MDEV-25886](https://jira.mariadb.org/browse/MDEV-25886))
* Server crashes when a connection is killed while executing [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) after previously locking the table with [LOCK TABLE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/LOCK-TABLE/README.md). ([MDEV-17749](https://jira.mariadb.org/browse/MDEV-17749))
* Server crashes when the global value of the system\_versioning\_asof system variable is set using a stored function that reads the value of another global system variable. ([MDEV-16481](https://jira.mariadb.org/browse/MDEV-16481))
* Server crashes when [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) is active and usernames longer than 256 characters are used. (MENT-1019)
* Server crashes when [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) is active and audit log file rotation is triggered. (MENT-1207)
* Server crashes while executing query with a CTE that is used at least twice and that references an embedded recursive CTE. ([MDEV-26108](https://jira.mariadb.org/browse/MDEV-26108))
* Possible crash with transactions having changes for tables with no primary key to apply in parallel, when using MariaDB Enterprise Cluster. ([MDEV-25551](https://jira.mariadb.org/browse/MDEV-25551))
* Server crashes when executing [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) to create a [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) table with a `COMMENT` value that does not contain embedded double quotes. ([MDEV-26139](https://jira.mariadb.org/browse/MDEV-26139))
* Server crashes when a client connects during shutdown. ([MDEV-18353](https://jira.mariadb.org/browse/MDEV-18353))

### Can result in unexpected behavior

* When [CREATE OR REPLACE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) fails after dropping the table, the DROP TABLE operation is not written into the binary log. ([MDEV-25595](https://jira.mariadb.org/browse/MDEV-25595))
* The [SHOW GRANTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-grants) statement does not quote role names properly for DEFAULT ROLE. ([MDEV-26080](https://jira.mariadb.org/browse/MDEV-26080))
* The [innochecksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum) utility reports errors for freed pages. ([MDEV-25361](https://jira.mariadb.org/browse/MDEV-25361))
* When an unknown column is referenced in the `WHERE` clause of a recursive CTE, the query sometimes succeeds instead of failing with an [ER\_BAD\_FIELD\_ERROR](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md). ([MDEV-26189](https://jira.mariadb.org/browse/MDEV-26189))
* Reusing CTE inside a function fails with the [ER\_NO\_SUCH\_TABLE](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) error code. ([MDEV-23886](https://jira.mariadb.org/browse/MDEV-23886))
* Several fixes for MariaDB Enterprise Cluster (Galera) SST scripts. ([MDEV-20580](https://jira.mariadb.org/browse/MDEV-20580), [MDEV-25818](https://jira.mariadb.org/browse/MDEV-25818), [MDEV-25759](https://jira.mariadb.org/browse/MDEV-25759), [MDEV-25719](https://jira.mariadb.org/browse/MDEV-25719), [MDEV-15639](https://jira.mariadb.org/browse/MDEV-15639), [MDEV-15371](https://jira.mariadb.org/browse/MDEV-15371), [MDEV-18797](https://jira.mariadb.org/browse/MDEV-18797), MENT-1170, [MDEV-24979](https://jira.mariadb.org/browse/MDEV-24979), [MDEV-21192](https://jira.mariadb.org/browse/MDEV-21192))
* With MariaDB Enterprise Cluster, when [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method), MariaDB Enterprise Backup does not inherit server options set by the `Environment` systemd configuration parameter. ([MDEV-24962](https://jira.mariadb.org/browse/MDEV-24962))
* With MariaDB Enterprise Cluster, when [wsrep\_sst\_method=rsync](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) is set and log-bin and/or log-bin-index are set to custom paths, the rsync SST does not copy the binary log index. ([MDEV-25978](https://jira.mariadb.org/browse/MDEV-25978))

As a result of this issue, a Joiner node writes the following error to the [MariaDB Error Log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log):

```
tail: cannot open 'mysql-bin.index' for reading: No such file or directory
```

* With MariaDB Enterprise Cluster, when [wsrep\_sst\_method=rsync](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) is set, `rsync` for a new SST process may be killed rather than the `rsync` for the old SST process. ([MDEV-25880](https://jira.mariadb.org/browse/MDEV-25880))
* With MariaDB Enterprise Cluster, the WSREP threads could write warnings about foreign keys to the [MariaDB Error Log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log) when [wsrep\_debug](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_debug) is not enabled. ([MDEV-26062](https://jira.mariadb.org/browse/MDEV-26062))
  * In prior releases, the following warning could be written to the log:

```
InnoDB: WSREP: referenced FK check fail: Lock wait index `PRIMARY` table `schema`.`child_table`
```

* Starting with this release, the WSREP threads will only write warnings about foreign keys to the [MariaDB Error Log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log) when [wsrep\_debug](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_debug) is enabled.
* The [CREATE INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-index) statement may check the wrong maximum column length. ([MDEV-26203](https://jira.mariadb.org/browse/MDEV-26203))
* The [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) storage engine handles ">=" as ">" in some cases, where multi-column indexes are used. ([MDEV-25985](https://jira.mariadb.org/browse/MDEV-25985))
* The [max\_password\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_password_errors) system variable does not work correctly with the [ed25519](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-ed25519) authentication plugin. ([MDEV-25641](https://jira.mariadb.org/browse/MDEV-25641))
* The `"Condition pushdown into derived table"` optimization cannot be applied if the expression being pushed refers to a derived table column which is computed from an expression that has a stored function call, @session variable reference, or other similar construct. ([MDEV-25969](https://jira.mariadb.org/browse/MDEV-25969))
* A query that uses `ORDER BY .. LIMIT` clause and `"Range checked for each record"` optimization could produce incorrect results. ([MDEV-25858](https://jira.mariadb.org/browse/MDEV-25858))
* An aborted [OPTIMIZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table) statement is logged in the binary log and replicates to the Replica server. ([MDEV-22530](https://jira.mariadb.org/browse/MDEV-22530))
* [EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) shows an execution plan different from actually executed ([MDEV-25682](https://jira.mariadb.org/browse/MDEV-25682))
* For system-versioned tables, the [SHOW INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-index) statement displays the system-invisible `row_end` column as part of the primary key. ([MDEV-16857](https://jira.mariadb.org/browse/MDEV-16857))
* For system-versioned tables partitioned by `SYSTEM_TIME`, overflowing the partitions leads to incorrect results from [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select). result ([MDEV-22247](https://jira.mariadb.org/browse/MDEV-22247))
* For [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) tables, [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statements that use `CASE WHEN .. THEN` can result in syntax error. ([MDEV-24760](https://jira.mariadb.org/browse/MDEV-24760))
* For [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) tables, [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statements that use the JSON\_EXTRACT() function in the `WHERE` clause can result in a syntax error. ([MDEV-24517](https://jira.mariadb.org/browse/MDEV-24517))
* For [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) tables, [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) statements that call native functions using `remove_str` (such as [TRIM()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/trim)) fail with the [ER\_WRONG\_PARAMCOUNT\_TO\_NATIVE\_FCT](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) error code. ([MDEV-24020](https://jira.mariadb.org/browse/MDEV-24020))
* For [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) tables, server-sided prepared statements (created by [PREPARE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/PREPARE/README.md) and executed by [EXECUTE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/EXECUTE/README.md)) incorrectly turn unsigned integer literals into signed integers. ([MDEV-25808](https://jira.mariadb.org/browse/MDEV-25808))
* For [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) tables, statements that use the [JSON\_REPLACE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_replace) function fail with the [ER\_SP\_DOES\_NOT\_EXIST](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) error code. ([MDEV-24523](https://jira.mariadb.org/browse/MDEV-24523))
* With [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin), the [CREATE PROCEDURE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-procedures/create-procedure) and [DROP PROCEDURE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-procedures/drop-procedure) statements are not logged to the audit log. (MENT-1169)
* With MariaDB Enterprise Backup, the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/binary) position written to the `xtrabackup_binlog_info` file during the backup is incorrect for replication. ([MDEV-23080](https://jira.mariadb.org/browse/MDEV-23080))
* With MariaDB Enterprise Cluster, when [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method), a typo in the SST script causes SST failure on the Donor node. ([MDEV-26117](https://jira.mariadb.org/browse/MDEV-26117))
* For [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) tables, [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statements that use `DISTINCT` do not work properly in some cases. ([MDEV-26013](https://jira.mariadb.org/browse/MDEV-26013))
* When [mariadbd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) is compiled with WolfSSL, the server fails to accept connections using TLS 1.3 and AES-GCM cipher. ([MDEV-22221](https://jira.mariadb.org/browse/MDEV-22221))

## Interface Changes

* [KEYWORDS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-keywords-table) information schema table added
* `mysqld` --server-audit-load-on-error command-line option added
* [server\_audit\_load\_on\_error](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables) system variable added
* [SQL\_FUNCTIONS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-sql_functions-table) information schema table added
* [system\_versioning\_asof](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables#system_versioning_asof) system variable default value changed from `DEFAULT` to `""` (empty)

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.4.21-13 is provided for:

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

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
