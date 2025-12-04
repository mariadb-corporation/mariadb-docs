# Release Notes for MariaDB Enterprise Server 10.5.9-6

This sixth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.5 is a maintenance release. This release includes security fixes.

MariaDB Enterprise Server 10.5.9-6 was released on 2021-03-15.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/cve.org) link) | CVSS base score                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [CVE-2021-27928](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27928)                                                                                               | N/A (Critical)[#1](release-notes-for-mariadb-enterprise-server-10-5-9-6.md#1) |

`#1`:\
MariaDB CVEs are assigned a word rating instead of a CVSS base score. See the MariaDB Engineering Policy for details.

## Notable Changes

* The new mariadb-dump `--system={all, users, plugins, udfs, servers, stats, timezones}` command-line option allows dumping system information in logical form. ([MDEV-23630](https://jira.mariadb.org/browse/MDEV-23630))
* Added primary host and port info to replica stop messages. ([MDEV-10272](https://jira.mariadb.org/browse/MDEV-10272))
* Parameter [innodb\_idle\_flush\_pct](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_idle_flush_pct) has no effect and is defined as deprecated. ([MDEV-24536](https://jira.mariadb.org/browse/MDEV-24536))
* New [MariaDB Enterprise Backup](../../10-5/broken-reference/) option --log-innodb-page-corruption to continue the backup process when corruption is encountered. Corrupted pages are logged in `backup_corrupted` file in the backup destination directory. ([MDEV-22929](https://jira.mariadb.org/browse/MDEV-22929))
* [MariaDB Enterprise Backup](../../10-5/broken-reference/) adds `completed with Error!` to the end of the log file if the backup is started with parameter --log-innodb-page-corruption and completed with corrupted tables. The new log entry `canceled with Error!` will be used when the backup could not be completed. (MENT-1059)
* [wsrep\_provider](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_provider) and [wsrep\_notify\_cmd](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_notify_cmd) system variables are read-only. ([MDEV-25179](https://jira.mariadb.org/browse/MDEV-25179))
* Galera `wsrep` library updated to 26.4.7 in [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md).
* [CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/create-user) and [ALTER USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/alter-user) allow either order for `ACCOUNT LOCK` and `PASSWORD EXPIRE` ([MDEV-24098](https://jira.mariadb.org/browse/MDEV-24098))

## Issues Fixed

### Can result in data loss

* Crash on recovery after server kill during instant `ADD COLUMN` ([MDEV-24323](https://jira.mariadb.org/browse/MDEV-24323))

### Can result in a hang or crash

* Possible segfault on [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) with explicit `FTS_DOC_ID_INDEX` using multiple fields. ([MDEV-24403](https://jira.mariadb.org/browse/MDEV-24403))
* Server crashes upon attempt to update view through second execution of a stored procedure. ([MDEV-16940](https://jira.mariadb.org/browse/MDEV-16940))
* [CREATE VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/views/create-view) containing [WITH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/with) clause can crash. ([MDEV-22781](https://jira.mariadb.org/browse/MDEV-22781))
* Possible crash for a query using recursive CTE without having a default schema defined. ([MDEV-24019](https://jira.mariadb.org/browse/MDEV-24019))
* Server crash on `WITH RECURSIVE UNION ALL` (CTE) query. ([MDEV-23619](https://jira.mariadb.org/browse/MDEV-23619))
* Server hang due to [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) lock conflict resolution. ([MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328))
* Possible crash in replication when applying a transaction that contains cascading foreign key delete for a table and that has an indexed virtual column. ([MDEV-23033](https://jira.mariadb.org/browse/MDEV-23033))
* Possible lock conflicts between two wsrep high priority threads in [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) on tables having unique secondary keys. ([MDEV-23851](https://jira.mariadb.org/browse/MDEV-23851))
* Server crash when [VALUE()](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/VALUE/README.md) uses a subselect. ([MDEV-24675](https://jira.mariadb.org/browse/MDEV-24675))
* Possible crash of the server when audit logging is active. (MENT-1098)
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) crash after execution of XA START ([MDEV-24469](https://jira.mariadb.org/browse/MDEV-24469))
* Hang with [innodb\_use\_native\_aio=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_use_native_aio) and [innodb\_write\_io\_threads=1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_write_io_threads) ([MDEV-24313](https://jira.mariadb.org/browse/MDEV-24313))
* Encryption is modifying a freed page for InnoDB, which results in a crash. ([MDEV-24695](https://jira.mariadb.org/browse/MDEV-24695))
* A query on a table with composite key and range condition on multiple attributes can result in a crash. (MENT-1126)

### Can result in unexpected behavior

* [SHOW GRANTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-grants) is missing the WITH GRANT privilege for roles. ([MDEV-24289](https://jira.mariadb.org/browse/MDEV-24289))
* `mysqld_safe` log messages are missing in the error log file. ([MDEV-21367](https://jira.mariadb.org/browse/MDEV-21367))
* `CHECK_CLAUSE` field in [INFORMATION\_SCHEMA.CHECK\_CONSTRAINTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-check_constraints-table) truncates check constraints expressions. ([MDEV-24139](https://jira.mariadb.org/browse/MDEV-24139))
* Unexpected error message when selecting from view that uses mergeable derived table. ([MDEV-24314](https://jira.mariadb.org/browse/MDEV-24314))
* Permission denied error message is returned on users with [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) permissions for nested CTEs. ([MDEV-20751](https://jira.mariadb.org/browse/MDEV-20751))
* Regression: `SELECT .. UNION ..` with inconsistent column names fails. ([MDEV-19179](https://jira.mariadb.org/browse/MDEV-19179))
* Race condition between [KILL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill) and transaction commit with [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md). ([MDEV-23536](https://jira.mariadb.org/browse/MDEV-23536))
* Plugin system variables and activation options can break [mariadbd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--wsrep\_recover](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_recover) for [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md). ([MDEV-20717](https://jira.mariadb.org/browse/MDEV-20717))
* `SELECT INTO OUTFILE` used permission `666` where `644` should be used to limit the privileges to change the file. ([MDEV-23875](https://jira.mariadb.org/browse/MDEV-23875))
* Syntax error on correct syntax for [CREATE VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/views/create-view) that includes `X is null = 0` ([MDEV-24194](https://jira.mariadb.org/browse/MDEV-24194))
* Altered connection limits for user have no effect. ([MDEV-17852](https://jira.mariadb.org/browse/MDEV-17852))
* Syntax error when using `COLLATE` for creating virtual columns. ([MDEV-12161](https://jira.mariadb.org/browse/MDEV-12161))
* Auto purge of relaylogs stops when relay-log-file is `slave-relay-log.999999` and [slave\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is enabled. ([MDEV-8134](https://jira.mariadb.org/browse/MDEV-8134))
* `ORDER BY` in view definition leads to wrong result with GROUP BY on query using view. ([MDEV-23826](https://jira.mariadb.org/browse/MDEV-23826))
* [SUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/sum) column from a derived table returns invalid values. ([MDEV-23291](https://jira.mariadb.org/browse/MDEV-23291))
* [server\_audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins) doesn't respect filters for PROXY\_CONNECT events. ([MDEV-24318](https://jira.mariadb.org/browse/MDEV-24318))
* [server\_audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins) plugin doesn't consider proxy users in [server\_audit\_excl\_users](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables) and [server\_audit\_excl\_users](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables) ([MDEV-19442](https://jira.mariadb.org/browse/MDEV-19442))
* With `ALTER USER .. IDENTIFIED` BY command, password isn't replaced by asterisks in audit log. (MENT-1128)
* [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) does not insert history row for [system versioned](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/system-versioned-table/README.md) or application period based tables if the row has not changed. ([MDEV-23446](https://jira.mariadb.org/browse/MDEV-23446))
* Wrong duplicate primary key error between the history row generated on referential action and the history row on evaluating foreign referential action for self-reference in a [system versioned](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/system-versioned-table/README.md) table. ([MDEV-21138](https://jira.mariadb.org/browse/MDEV-21138), [MDEV-23644](https://jira.mariadb.org/browse/MDEV-23644))
* Wrong number of decimal digits in certain `UNION` or subquery constellations, like union of unsigned and NULL type. ([MDEV-24387](https://jira.mariadb.org/browse/MDEV-24387))
* `[CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/create/create-table) .. SELECT` FROM does not create table if [VALUE()](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/VALUE/README.md) is not using a scalar value. ([MDEV-24618](https://jira.mariadb.org/browse/MDEV-24618))
* InnoDB may report incorrect binlog position information after [RESET MASTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/reset-master) ([MDEV-22351](https://jira.mariadb.org/browse/MDEV-22351))
* Sequences which are used as default by a table are not dumped in right order by [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) ([MDEV-21785](https://jira.mariadb.org/browse/MDEV-21785))
* [SHOW CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-user) generates invalid SQL for user where password expiry and account lock set. ([MDEV-24098](https://jira.mariadb.org/browse/MDEV-24098))
* `Garbd` of [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) can't initiate `SST` ([MDEV-23647](https://jira.mariadb.org/browse/MDEV-23647))
* Misleading error message from [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) might be interpreted as a point in time recovery is not possible. ([MDEV-23846](https://jira.mariadb.org/browse/MDEV-23846))
* High memory usage in the optimizer when a query is using `SELECT .. FROM tbl .. WHERE unique_key not in (long-list) AND .. unique_key not in (long-list) AND ..` ([MDEV-24711](https://jira.mariadb.org/browse/MDEV-24711))
* [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) for tables with `CHECK CONSTRAINTS` returns with `Out of Memory` error. ([MDEV-24274](https://jira.mariadb.org/browse/MDEV-24274))
* Alter rename table does not remove table from [performance\_schema.objects\_summary\_global\_by\_type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-objects_summary_global_by_type-table) when using `algorithm=copy` ([MDEV-24364](https://jira.mariadb.org/browse/MDEV-24364))
* Persistent statistics are lost for [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table after [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) ([MDEV-24564](https://jira.mariadb.org/browse/MDEV-24564))
* The default setting of [innodb\_max\_dirty\_pages\_pct\_lwm=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_max_dirty_pages_pct_lwm) has effects on [innodb\_adaptive\_flushing=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_max_dirty_pages_pct_lwm) with results in a performance regression. ([MDEV-24537](https://jira.mariadb.org/browse/MDEV-24537))
* Accessing [INFORMATION\_SCHEMA.INNODB\_TABLESPACES\_ENCRYPTION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_encryption-table) may break innodb\_open\_files logic. ([MDEV-24190](https://jira.mariadb.org/browse/MDEV-24190))
* [performance\_schema.events\_transactions\_history\_long.trx\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-events_transactions_history_long-table) reports garbage. ([MDEV-24600](https://jira.mariadb.org/browse/MDEV-24600))
* S3, same-backend replication: Dropping a table on primary causes error on replica. ([MDEV-24351](https://jira.mariadb.org/browse/MDEV-24351))
* [BINLOG REPLAY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-replay) privilege is missing from [SHOW PRIVILEGES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-privileges) ([MDEV-24344](https://jira.mariadb.org/browse/MDEV-24344))
* Flushing starts only when 90% (`srv_max_buf_pool_modified_pct`) pages are modified. ([MDEV-24917](https://jira.mariadb.org/browse/MDEV-24917))
* Quick memory exhaustion with `extended_keys=on` on queries having multiple [IN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/comparison-operators/in) or [NOT IN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/comparison-operators/not-in) using InnoDB. ([MDEV-9750](https://jira.mariadb.org/browse/MDEV-9750))

### Related to install and upgrade

* [mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-upgrade) fails with error messages `ALGORITHM=INSTANT is not supported for this operation` ([MDEV-16735](https://jira.mariadb.org/browse/MDEV-16735))
* [mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-upgrade) hangs when executing [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) on the [mysql.event](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-event-table) system table, if the table is not empty ([MDEV-24452](https://jira.mariadb.org/browse/MDEV-24452))
* Enterprise upgrade from 10.4 to 10.5 fails with option `disable-s3` in the 10.4 configuration file. (MENT-1068)

## Changes in Storage Engines

This release incorporates MariaDB ColumnStore storage engine version 5.5.2.

## Interface Changes

* [aria\_sort\_buffer\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-system-variables) system variable maximum value changed from `18446744073709551615` to `9223372036854775807`
* [CHECK\_CONSTRAINTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-check_constraints-table) information schema table schema changed
* [group\_concat\_max\_len](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#group_concat_max_len) system variable maximum value changed from `18446744073709551615` to `4294967295`
* [innodb\_idle\_flush\_pct](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_idle_flush_pct) system variable removed
* [innodb\_write\_io\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_write_io_threads) system variable minimum value changed from `1` to `2`
* mariadb-backup --log-innodb-page-corruption command-line option added
* mariadb-dump --system command-line option added
* mariadb\_es\_repo\_setup --include-unsupported command-line option added
* mariadb\_es\_repo\_setup --skip-check-installed command-line option added
* mariadb\_es\_repo\_setup --version command-line option added
* mariadb\_repo\_setup --version command-line option added
* mariadbd --innodb-idle-flush-pct command-line option removed
* mariadbd --optimizer-max-sel-arg-weight command-line option added
* [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length) system variable minimum value changed from `8` to `64`
* [optimizer\_max\_sel\_arg\_weight](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_max_sel_arg_weight) system variable added
* [setup\_actors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-setup_actors-table) performance schema table schema changed
* [THREAD\_POOL\_QUEUES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_queues-table) information schema table schema changed

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.5.9-6 is provided for:

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
