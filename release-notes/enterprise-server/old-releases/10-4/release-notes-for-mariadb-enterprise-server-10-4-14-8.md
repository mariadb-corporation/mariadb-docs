# Release Notes for MariaDB Enterprise Server 10.4.14-8

This eighth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.4.14-8 was released on 2020-09-08.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2021-2022](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2022)                                                                                                 | 4.4             |

## Notable Changes

* Limit innodb\_encryption\_threads to 255 ([MDEV-22258](https://jira.mariadb.org/browse/MDEV-22258))
* Minimum value of [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length) raised to 8 (previously 4) so fixed size data types like [DOUBLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/double) and [BIGINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/bigint) are not truncated for lower values of [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length) . ([MDEV-22715](https://jira.mariadb.org/browse/MDEV-22715))
* Backport from MariaDB Server 10.5.4 of improvements to [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) for InnoDB. (MENT-636)

[UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) privilege for system user mariadb.sys removed for system table [mysql.global\_priv](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-columns_priv-table) ([MDEV-23237](https://jira.mariadb.org/browse/MDEV-23237))

## Issues Fixed

### Can result in data loss

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) doublewrite recovery can corrupt data pages. ([MDEV-11799](https://jira.mariadb.org/browse/MDEV-11799))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table can disappear when trying to change primary key after disabling Foreign Key checks and violating a Foreign Key constraint. (MENT-804)
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) corruption in delete buffering. ([MDEV-22497](https://jira.mariadb.org/browse/MDEV-22497))
* Rollback of [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) fails when column reorder occurs. ([MDEV-22637](https://jira.mariadb.org/browse/MDEV-22637))
* Possible data inconsistency when executing ADD PRIMARY KEY with concurrent DML transactions. ([MDEV-23244](https://jira.mariadb.org/browse/MDEV-23244))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table corruption after [DROP INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-index) ([MDEV-22988](https://jira.mariadb.org/browse/MDEV-22988))
* [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) to extend a [CHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/char) column was incorrectly allowed to be instant. ([MDEV-22771](https://jira.mariadb.org/browse/MDEV-22771))

### Can result in a hang or crash

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) deadlock in [FLUSH TABLES .. FOR EXPORT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) ([MDEV-22890](https://jira.mariadb.org/browse/MDEV-22890))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) data file extension is not crash-safe. ([MDEV-23190](https://jira.mariadb.org/browse/MDEV-23190))
* [innodb\_log\_optimize\_ddl=OFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_optimize_ddl) is not crash safe. ([MDEV-21347](https://jira.mariadb.org/browse/MDEV-21347))
* Deadlock involving parallel workers, [STOP SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica) , and [FLUSH TABLES WITH READ LOCK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) ([MDEV-23089](https://jira.mariadb.org/browse/MDEV-23089))
* Crashes when running a SQL query containing a specific subquery pattern. ([MDEV-23221](https://jira.mariadb.org/browse/MDEV-23221))
* Dropping the adaptive hash index may cause DDL to lock up InnoDB. ([MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456))
* [RESET MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/reset-master) could result in a crash when the value exceeds the max allowed `2147483647` ([MDEV-22451](https://jira.mariadb.org/browse/MDEV-22451))
* Crash on `WITH RECURSIVE` large query ([MDEV-22748](https://jira.mariadb.org/browse/MDEV-22748))
* Crash with Prepared Statement with a ? parameter inside a re-used CTE. ([MDEV-22779](https://jira.mariadb.org/browse/MDEV-22779))
* Possible crash after changing the `query_cache` size. ([MDEV-5924](https://jira.mariadb.org/browse/MDEV-5924))
* Crash in `CREATE TABLE AS SELECT` when the precision of returning type `= 0` ([MDEV-22502](https://jira.mariadb.org/browse/MDEV-22502))
* [ENUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/enum) or [SET](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) in a [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) statement which has a `0x00` byte in one of the values could crash the server. ([MDEV-22111](https://jira.mariadb.org/browse/MDEV-22111))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) recovery can block server startup. (MENT-915)
* Possible crash of a [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) node when [KILL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill) is executed ([MDEV-23147](https://jira.mariadb.org/browse/MDEV-23147))
* Possible crash when executing [FLUSH PRIVILEGES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) . ([MDEV-23009](https://jira.mariadb.org/browse/MDEV-23009))
* Server can hang when started with `--plugin-load-add=server_audit` and records in `mysql.plugin` refer to non-existent libraries. ([MDEV-19918](https://jira.mariadb.org/browse/MDEV-19918))
* Server hangs on start up when loading [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) if old [SERVER\_AUDIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables#server_audit) plugin is installed (MENT-273)

### Can result in unexpected behavior

* Service shutdown fails if OS datetime has been updated backwards. ([MDEV-17481](https://jira.mariadb.org/browse/MDEV-17481))
* `ALTER TABLE .. ANALYZE PARTITION` can run for hours for huge tables if engine-independent persistent statistics are enabled, due to reading and locking of all rows in the [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table instead of for the partition. ([MDEV-21472](https://jira.mariadb.org/browse/MDEV-21472))
* [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) can fail with privilege error when [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) privilege exists at database level but [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) privilege exists at table level. ([MDEV-23010](https://jira.mariadb.org/browse/MDEV-23010))
* Latency and throughput regression identified in write-heavy benchmarks for latest releases in MariaDB Server 10.2, 10.3, and 10.4. (MENT-909)
* When giving a parallel optimistic slave a replication stop position with `START SLAVE UNTIL .. file .. pos` stops at an earlier position earlier than defined if the transaction that spans over the given stop position has to roll back due to conflicts. ([MDEV-15152](https://jira.mariadb.org/browse/MDEV-15152))
* [mariadb-backup](../../10-4/broken-reference/) [--prepare](../../10-4/broken-reference/) does not stop on errors while applying [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) redo log. ([MDEV-22354](https://jira.mariadb.org/browse/MDEV-22354))
* Point in time recovery of binary log fails with syntax error when [sql\_mode=ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode). ([MDEV-23108](https://jira.mariadb.org/browse/MDEV-23108))
* Replication aborts with [ER\_SLAVE\_CONVERSION\_FAILED](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) upon CREATE .. SELECT when [sql\_mode=ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode). ([MDEV-19632](https://jira.mariadb.org/browse/MDEV-19632))
* Regression in Audit Plugin Performance. (MENT-700)
* `ROW_FORMAT` mismatch in instant [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) . An instant `ADD or DROP` column or reorder could create a dummy table object with the wrong `ROW_FORMAT` when [innodb\_default\_row\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_default_row_format) was changed between [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) and [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) . ([MDEV-23295](https://jira.mariadb.org/browse/MDEV-23295))
* Slow [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) shutdown on large instances when using Windows OS. ([MDEV-22778](https://jira.mariadb.org/browse/MDEV-22778))
* Rounding functions return wrong datatype. ([MDEV-23366](https://jira.mariadb.org/browse/MDEV-23366), [MDEV-23367](https://jira.mariadb.org/browse/MDEV-23367), [MDEV-23368](https://jira.mariadb.org/browse/MDEV-23368), [MDEV-23350](https://jira.mariadb.org/browse/MDEV-23350), [MDEV-23351](https://jira.mariadb.org/browse/MDEV-23351), [MDEV-23337](https://jira.mariadb.org/browse/MDEV-23337), [MDEV-23323](https://jira.mariadb.org/browse/MDEV-23323))
* [PAM v2 plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam) produces zombie processes. ([MDEV-21385](https://jira.mariadb.org/browse/MDEV-21385))
* Performance regression when using [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin). (MENT-870)

### Related to install and upgrade

* [UNINSTALL PLUGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin) and [UNINSTALL SONAME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname) can't run if the library file doesn't exist. ([MDEV-21258](https://jira.mariadb.org/browse/MDEV-21258))

## Changes in Storage Engines

* This release includes [ColumnStore 1.4.4.](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md)

## Interface Changes

* [mariadb-backup](../../10-4/broken-reference/) `--help` command-line option added
* [mariadb-backup --mysqld-args](../../10-4/broken-reference/) command-line option added
* [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length) system variable minimum value changed from 4 to 8

## Platforms

In alignment to the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.4.14-8 is provided for:

* Red Hat Enterprise Linux 8
* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 6
* CentOS 8
* CentOS 7
* CentOS 6
* Debian 10
* Debian 9
* Debian 8
* SUSE Linux Enterprise Server 15
* SUSE Linux Enterprise Server 12
* Ubuntu 20.04
* Ubuntu 18.04
* Ubuntu 16.04
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see [MariaDB Corporation Engineering Policies".](https://mariadb.com/engineering-policies)

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policies](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a README file within the download.

## Installation Instructions

* [MariaDB Enterprise Server 10.4](./)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-from-to-specific-versions/upgrading-from-mariadb-10-5-to-mariadb-10-6)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
