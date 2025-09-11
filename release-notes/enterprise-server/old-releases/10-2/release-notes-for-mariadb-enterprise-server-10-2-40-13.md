# Release Notes for MariaDB Enterprise Server 10.2.40-13

This thirteenth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.2 is a maintenance release. This release includes a variety of fixes.

MariaDB Enterprise Server 10.2.40-13 was released on 2021-09-14.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-2/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2021-2389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2389)                                                                                                 | 5.9             |
| [CVE-2021-46666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46666)                                                                                               | 5.5             |
| [CVE-2021-46658](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46658)                                                                                               | 5.5             |
| [CVE-2021-46657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46657)                                                                                               | 5.5             |
| [CVE-2021-2372](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2372)                                                                                                 | 4.4             |

## Notable Changes

* Galera updated to 25.3.34
* ARM64 is now supported for several [platforms](release-notes-for-mariadb-enterprise-server-10-2-40-13.md#platforms)
* The script `wsrep_sst_mariadb-backup` checks all server-related configuration groups when processing a configuration file. ([MDEV-25669](https://jira.mariadb.org/browse/MDEV-25669))
  * Prior to this release, only the `[mysqld]` configuration group was checked when processing a configuration file.
* MariaDB Enterprise Backup expects [--stream=mbstream](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) to stream a backup using the included `mbstream` utility. ([MDEV-15730](https://jira.mariadb.org/browse/MDEV-15730))
  * Prior to this release, MariaDB Enterprise Backup expected [--stream=mbstream](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md), even though the `xbstream` utility had been renamed to `mbstream.`
* InnoDB no longer acquires advisory file locks by default. ([MDEV-24393](https://jira.mariadb.org/browse/MDEV-24393))
* The [information\_schema.KEYWORDS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-keywords-table) table has been added and can be used to view details about SQL keywords. ([MDEV-25129](https://jira.mariadb.org/browse/MDEV-25129))
* The [information\_schema.SQL\_FUNCTIONS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-sql_functions-table) table has been added and can be used to view details about built-in functions. ([MDEV-25129](https://jira.mariadb.org/browse/MDEV-25129))
* When using data-at-rest encryption with the [file\_key\_management](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin) encryption plugin, InnoDB will automatically disable key rotation checks. ([MDEV-14180](https://jira.mariadb.org/browse/MDEV-14180))
  * The [file\_key\_management](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin) encryption plugin does not support key rotation, so key rotation checks are not required.
  * In previous releases, unnecessary key rotation checks with the [file\_key\_management](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin) encryption plugin could reduce performance, unless they were explicitly disabled by setting [innodb\_encryption\_rotate\_key\_age=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encryption_rotate_key_age).

## Issues Fixed

### Can result in a hang or crash

* Possible server crash when pushing a `WHERE` condition over a mergeable derived table / view / CTE DT into a grouping view / derived table / CTE V whose item list contained set functions with constant arguments. ([MDEV-25635](https://jira.mariadb.org/browse/MDEV-25635))
* Server crashes on second execution of a stored procedure or a prepared statement when the corresponding query executes a window function on a view, CTE, or derived table. ([MDEV-25565](https://jira.mariadb.org/browse/MDEV-25565))
* Server crashes possible when executing a prepared statement with a hanging recursive CTE. ([MDEV-26135](https://jira.mariadb.org/browse/MDEV-26135))
* Server crashes while executing query with a CTE in a prepared statement or stored procedure. ([MDEV-26025](https://jira.mariadb.org/browse/MDEV-26025))
* Server crashes while executing query with a recursive CTE that is indirectly used twice. ([MDEV-26202](https://jira.mariadb.org/browse/MDEV-26202))
* Server crashes due to infinite recursion while processing an embedded recursive CTE with missing RECURSIVE. ([MDEV-26095](https://jira.mariadb.org/browse/MDEV-26095))
* Server crashes in InnoDB deadlock checker under high load. ([MDEV-25594](https://jira.mariadb.org/browse/MDEV-25594))
* Server crashes when a virtual generated column has a prefix index. ([MDEV-26220](https://jira.mariadb.org/browse/MDEV-26220))
* Server crashes possible when using virtual generated columns. ([MDEV-18166](https://jira.mariadb.org/browse/MDEV-18166), [MDEV-18249](https://jira.mariadb.org/browse/MDEV-18249))
* Server crashes while executing [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) when a [YEAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/year) column is truncated. ([MDEV-17890](https://jira.mariadb.org/browse/MDEV-17890))
* Server crashes while executing [SET ROLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/set-role) when a hostname cannot be resolved. ([MDEV-26081](https://jira.mariadb.org/browse/MDEV-26081))
* Server crashes when a subquery references an outer column in an `ORDER BY` clause. ([MDEV-25629](https://jira.mariadb.org/browse/MDEV-25629))
* Server crashes due to a stack overrun in the query optimizer while executing query with more than 32 equality conditions that compare columns of different tables (such as `tableX.colX=tableY.colY`). ([MDEV-17783](https://jira.mariadb.org/browse/MDEV-17783))
* Server crashes when a window function is the left expression of an IN(`SELECT ..`) subquery. ([MDEV-25630](https://jira.mariadb.org/browse/MDEV-25630))
* Possible deadlock on a Replica server using GTID Replication when [slave\_parallel\_mode=optimistic](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#slave_parallel_mode) and [OPTIMIZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table), [REPAIR TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/repair-table), or [ANALYZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/analyze-table) is executed. ([MDEV-17515](https://jira.mariadb.org/browse/MDEV-17515))
* Server crashes when [ALTER TABLE .. ADD FULLTEXT INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) fails on an InnoDB table. ([MDEV-25721](https://jira.mariadb.org/browse/MDEV-25721))
* Server crashes while executing [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate) on an InnoDB table with a Full-Text Index. ([MDEV-25663](https://jira.mariadb.org/browse/MDEV-25663))
* Server crashes while executing [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) on an InnoDB table with virtual generated columns that are indexed. ([MDEV-25872](https://jira.mariadb.org/browse/MDEV-25872))

### Can result in unexpected behavior

* When [CREATE OR REPLACE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) fails after dropping the table, the `DROP TABLE` operation is not written into the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/binary). ([MDEV-25595](https://jira.mariadb.org/browse/MDEV-25595))
* The [SHOW GRANTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-grants) statement does not quote role names properly for DEFAULT ROLE. ([MDEV-26080](https://jira.mariadb.org/browse/MDEV-26080))
* The [innochecksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum) utility reports errors for freed pages. ([MDEV-25361](https://jira.mariadb.org/browse/MDEV-25361))
* When an unknown column is referenced in the `WHERE` clause of a recursive CTE, the query sometimes succeeds instead of failing with an [ER\_BAD\_FIELD\_ERROR](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md). ([MDEV-26189](https://jira.mariadb.org/browse/MDEV-26189))
* Reusing CTE inside a function fails with the [ER\_NO\_SUCH\_TABLE](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) error code. ([MDEV-23886](https://jira.mariadb.org/browse/MDEV-23886))
* Several fixes for MariaDB Enterprise Cluster (Galera) SST scripts. ([MDEV-20580](https://jira.mariadb.org/browse/MDEV-20580), [MDEV-25818](https://jira.mariadb.org/browse/MDEV-25818), [MDEV-25759](https://jira.mariadb.org/browse/MDEV-25759), [MDEV-25719](https://jira.mariadb.org/browse/MDEV-25719), [MDEV-15639](https://jira.mariadb.org/browse/MDEV-15639), [MDEV-15371](https://jira.mariadb.org/browse/MDEV-15371), [MDEV-18797](https://jira.mariadb.org/browse/MDEV-18797), MENT-1170, [MDEV-24979](https://jira.mariadb.org/browse/MDEV-24979), [MDEV-21192](https://jira.mariadb.org/browse/MDEV-21192))
* With MariaDB Enterprise Cluster, when [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method), MariaDB Enterprise Backup does not inherit server options set by the Environment systemd configuration parameter. ([MDEV-24962](https://jira.mariadb.org/browse/MDEV-24962))
* With MariaDB Enterprise Cluster, when [wsrep\_sst\_method=rsync](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) is set and [log-bin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) and/or [log-bin-index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) are set to custom paths, the rsync SST does not copy the binary log index. ([MDEV-25978](https://jira.mariadb.org/browse/MDEV-25978))

As a result of this issue, a Joiner node writes the following error to the [MariaDB Error Log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log)

```
tail: cannot open 'mysql-bin.index' for reading: No such file or directory
```

* With MariaDB Enterprise Cluster, when [wsrep\_sst\_method=rsync](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) is set, `rsync` for a new SST process may be killed rather than the `rsync` for the old SST process. ([MDEV-25880](https://jira.mariadb.org/browse/MDEV-25880))
* With MariaDB Enterprise Cluster, the WSREP threads could write warnings about foreign keys to the MariaDB Error Log when [wsrep\_debug](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_debug) is not enabled. ([MDEV-26062](https://jira.mariadb.org/browse/MDEV-26062))
  * In prior releases, the following warning could be written to the log:

```
InnoDB: WSREP: referenced FK check fail: Lock wait index `PRIMARY` table `schema`.`child_table`
```

* Starting with this release, the WSREP threads will only write warnings about foreign keys to the MariaDB Error Log when wsrep\_debug is enabled.
* The [CREATE INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-index) statement may check the wrong maximum column length. ([MDEV-26203](https://jira.mariadb.org/browse/MDEV-26203))
* The [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) storage engine handles `">="` as `">"` in some cases, where multi-column indexes are used. ([MDEV-25985](https://jira.mariadb.org/browse/MDEV-25985))
* The [max\_password\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_password_errors) system variable does not work correctly with the [ed25519](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive-of-2x.xx-versions/mariadb-maxscale-23-02/mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-ed25519-authenticator) authentication plugin. ([MDEV-25641](https://jira.mariadb.org/browse/MDEV-25641))
* The `"Condition pushdown into derived table"` optimization cannot be applied if the expression being pushed refers to a derived table column which is computed from an expression that has a stored function call, @session variable reference, or other similar construct. ([MDEV-25969](https://jira.mariadb.org/browse/MDEV-25969))
* A query that uses `ORDER BY .. LIMIT` clause and `"Range checked for each record"` optimization could produce incorrect results. ([MDEV-25858](https://jira.mariadb.org/browse/MDEV-25858))
* An aborted [OPTIMIZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table) statement is logged in the binary log and replicates to the Replica server. ([MDEV-22530](https://jira.mariadb.org/browse/MDEV-22530))
* [EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) shows an execution plan different from actually executed. ([MDEV-25682](https://jira.mariadb.org/browse/MDEV-25682))
* Wrong result when selecting from views, derived tables, or CTEs with the form (`SELECT .. LIMIT <n>) ORDER BY ..` ([MDEV-25679](https://jira.mariadb.org/browse/MDEV-25679))
* Procedure containing CTE incorrectly stored in the [mysql.proc](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-proc-table) system table. ([MDEV-20411](https://jira.mariadb.org/browse/MDEV-20411))

## Interface Changes

* [KEYWORDS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-keywords-table) information schema table added
* [SQL\_FUNCTIONS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-sql_functions-table) information schema table added

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.2.40-13 is provided for:

* CentOS 7 (x86\_64)
* CentOS 8 (x86\_64, ARM64)
* Debian 9 (x86\_64, ARM64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 18.04 (x86\_64, ARM64)
* Microsoft Windows (x86\_64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
