# Release Notes for MariaDB Enterprise Server 10.5.5-3

This third release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.5 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.5.5-3 was released on 2020-09-08.

### Note

With MariaDB Enterprise Server 10.5 "mysql" command names are replaced with "mariadb" command names. Symbolic links are in place to maintain backward compatibility with the old names and prevent disruption. ([MDEV-21303](https://jira.mariadb.org/browse/MDEV-21303))

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2021-2022](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2022)                                                                                                 | 4.4             |

## Notable Changes

* [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) privilege for system user `mariadb.sys` removed for system table [mysql.global\_priv](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-global_priv-table) ([MDEV-23237](https://jira.mariadb.org/browse/MDEV-23237))
* Deprecated [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) configuration parameters: ([MDEV-23379](https://jira.mariadb.org/browse/MDEV-23379))
  * [innodb\_thread\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_thread_concurrency)
  * [innodb\_commit\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_commit_concurrency)
  * [innodb\_replication\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_replication_delay)
  * [innodb\_concurrency\_tickets](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_concurrency_tickets)
  * [innodb\_thread\_sleep\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_thread_sleep_delay)
  * [innodb\_adaptive\_max\_sleep\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_adaptive_max_sleep_delay)
* [Spider storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) now allows parameters `driver` and `filedsn` for the ODBC wrapper. System tables [spider\_link\_mon\_servers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/spider-mysql-database-tables/mysql-spider_link_mon_servers-table) , [spider\_tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/spider-mysql-database-tables/mysql-spider_tables-table) , [spider\_xa\_member](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/spider-mysql-database-tables/mysql-spider_xa_member-table) , and [spider\_xa\_failed\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/spider-mysql-database-tables/mysql-spider_xa_failed_log-table) updated. (MENT-812)
* Setting [SHUTDOWN\_WAIT\_FOR\_SLAVES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/shutdown) now only requires [SHUTDOWN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#shutdown) privilege, not the generic [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super) privilege. (MENT-731)

## Issues Fixed

### Can result in data loss

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) doublewrite recovery can corrupt data pages. ([MDEV-11799](https://jira.mariadb.org/browse/MDEV-11799))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table can disappear when trying to change primary key after disabling Foreign Key checks and violating a Foreign Key constraint. (MENT-804)
* Possible data inconsistency when executing `ADD PRIMARY KEY` with concurrent DML transactions. ([MDEV-23244](https://jira.mariadb.org/browse/MDEV-23244))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table corruption can occur after [DROP INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-index) ([MDEV-22988](https://jira.mariadb.org/browse/MDEV-22988))
* [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) to extend a [CHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/char) column was incorrectly allowed to be instant. ([MDEV-22771](https://jira.mariadb.org/browse/MDEV-22771))

### Can result in a hang or crash

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) deadlock in [FLUSH TABLES .. FOR EXPORT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) ([MDEV-22890](https://jira.mariadb.org/browse/MDEV-22890))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) data file extension is not crash-safe. ([MDEV-23190](https://jira.mariadb.org/browse/MDEV-23190))
* [innodb\_log\_optimize\_ddl=OFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_optimize_ddl) is not crash safe. ([MDEV-21347](https://jira.mariadb.org/browse/MDEV-21347))
* Deadlock involving parallel workers, [STOP SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica), and [FLUSH TABLES WITH READ LOCK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) ([MDEV-23089](https://jira.mariadb.org/browse/MDEV-23089))
* Crashes when running a SQL query containing a specific subquery pattern. ([MDEV-23221](https://jira.mariadb.org/browse/MDEV-23221))
* Possible crash of a [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) node when [KILL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill) is executed. ([MDEV-23147](https://jira.mariadb.org/browse/MDEV-23147))
* Possible crash when executing [FLUSH PRIVILEGES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) ([MDEV-23009](https://jira.mariadb.org/browse/MDEV-23009))
* Server can hang when started with [--plugin-load-add=server\_audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#-plugin-load-add) and records in [mysql.plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-plugin-table) refer to non-existent libraries. ([MDEV-19918](https://jira.mariadb.org/browse/MDEV-19918))
* Server crashes upon [SHOW CREATE PROCEDURE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-procedure) for stored procedures after upgrade from MariaDB Server 10.3. (MENT-819)
* Crash with `CREATE TEMPORARY TABLE .. ENGINE=SPIDER` using wrapper `odbc` (MENT-807)

### Can result in unexpected behavior

* Service shutdown fails if OS datetime has been updated backwards. ([MDEV-17481](https://jira.mariadb.org/browse/MDEV-17481))
* `ALTER TABLE .. ANALYZE PARTITION` can run for hours for huge tables if engine-independent persistent statistics are enabled, due to reading and locking of all rows in the [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table instead of for the partition. ([MDEV-21472](https://jira.mariadb.org/browse/MDEV-21472))
* [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) can fail with privilege error when [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#update) privilege exists at database level but [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) privilege exists at table level. ([MDEV-23010](https://jira.mariadb.org/browse/MDEV-23010))
* Latency and throughput regression identified in write-heavy benchmarks for latest releases in MariaDB Server 10.2, 10.3, and 10.4. (MENT-909)
* Point in time recovery of binary log fails with syntax error when [sql\_mode=ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode). ([MDEV-23108](https://jira.mariadb.org/browse/MDEV-23108))
* Replication aborts with [ER\_SLAVE\_CONVERSION\_FAILED](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-5/broken-reference/README.md) upon `CREATE .. SELECT` when [sql\_mode=ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode). ([MDEV-19632](https://jira.mariadb.org/browse/MDEV-19632))
* Regression in Audit Plugin Performance. (MENT-700)
* `ROW_FORMAT` mismatch in instant [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) . An instant `ADD` or `DROP` column or reorder could create a dummy table object with the wrong `ROW_FORMAT` when innodb\_default\_row\_format was changed between [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) and [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table). ([MDEV-23295](https://jira.mariadb.org/browse/MDEV-23295))
* Slow [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) shutdown on large instance when using Windows OS. ([MDEV-22778](https://jira.mariadb.org/browse/MDEV-22778))
* Rounding functions return wrong datatype. ([MDEV-23366](https://jira.mariadb.org/browse/MDEV-23366), [MDEV-23367](https://jira.mariadb.org/browse/MDEV-23367), [MDEV-23368](https://jira.mariadb.org/browse/MDEV-23368), [MDEV-23350](https://jira.mariadb.org/browse/MDEV-23350), [MDEV-23351](https://jira.mariadb.org/browse/MDEV-23351), [MDEV-23337](https://jira.mariadb.org/browse/MDEV-23337), [MDEV-23323](https://jira.mariadb.org/browse/MDEV-23323))
* PAM v2 plugin produces zombie processes. ([MDEV-21385](https://jira.mariadb.org/browse/MDEV-21385))
* Performance regression when using [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin). (MENT-870)
* Fixes to performance regressions introduced in [MariaDB 10.5.4](../../../community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes.md). ([MDEV-23369](https://jira.mariadb.org/browse/MDEV-23369), [MDEV-23410](https://jira.mariadb.org/browse/MDEV-23410))
* Change in [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) I/O thread count is not reflected in system variables. (MENT-866)

### Related to install and upgrade

* [UNINSTALL PLUGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin) and [UNINSTALL SONAME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname) can't run if the library file doesn't exist. ([MDEV-21258](https://jira.mariadb.org/browse/MDEV-21258))

## Changes in Storage Engines

* This release includes Enterprise [ColumnStore 1.5.3](../../../columnstore/old-releases/columnstore-1-5/mariadb-columnstore-1-5-3-release-notes.md) (plugin version 1.5.3.2).
* This release includes [Enterprise Spider 3.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-storage-engine-overview#spider-versions-in-mariadb), including ODBC Wrapper support.

## Interface Changes

* [innodb\_adaptive\_max\_sleep\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_adaptive_max_sleep_delay) system variable default value changed from `150000` to `0` (now deprecated)
* [innodb\_concurrency\_tickets](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_concurrency_tickets) system variable default value changed from `5000` to `0` (now deprecated)
* [innodb\_thread\_sleep\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_thread_sleep_delay) system variable default value changed from `10000` to `0` (now deprecated)
* [spider\_link\_mon\_servers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/spider-mysql-database-tables/mysql-spider_link_mon_servers-table) system table schema changed
* [spider\_tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/spider-mysql-database-tables/mysql-spider_tables-table) system table schema changed
* [spider\_xa\_failed\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/spider-mysql-database-tables/mysql-spider_xa_failed_log-table) system table schema changed
* [spider\_xa\_member](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/spider-mysql-database-tables/mysql-spider_xa_member-table) system table schema changed

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.5.5-3 is provided for:

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

#### Note

MariaDB Enterprise Server 10.5 removes support for Red Hat Enterprise Linux (RHEL) 6 and CentOS 6.

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

* [Upgrade to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-from-to-specific-versions/upgrading-from-mariadb-10-5-to-mariadb-10-6)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
