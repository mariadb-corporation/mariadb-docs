# Release Notes for MariaDB Enterprise Server 10.4.13-7

This seventh release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.4.13-7 was released on 2020-06-08.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/cve.org) link) | CVSS base score                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [CVE-2020-2760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2760)                                                                                                 | 5.5                                                                          |
| [CVE-2020-2752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2752)                                                                                                 | 5.3                                                                          |
| [CVE-2020-2814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2814)                                                                                                 | 4.9                                                                          |
| [CVE-2020-2812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2812)                                                                                                 | 4.9                                                                          |
| [CVE-2020-13249](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13249)                                                                                               | N/A (Medium)[#1](release-notes-for-mariadb-enterprise-server-10-4-13-7.md#1) |

`#1`:\
MariaDB CVEs are assigned a word rating instead of a CVSS base score. See the MariaDB Engineering Policy for details.

## Notable Changes

* MariaDB ColumnStore 1.4.4 is included in this release. Specific details on this component may be found in the ColumnStore 1.4.4 release notes.
* [mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-upgrade) now displays a warning when upgrading a replica from MySQL Server to MariaDB Enterprise Server if data was present in the `mysql.slave_master_info` and `mysql.slave_relay_log_info` tables. A warning is needed as this information will be ignored. ([MDEV-10047](https://jira.mariadb.org/browse/MDEV-10047))
* [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) has a new `--ignore-table-data=<table>` option. When used, the dump will include the table definition for the listed tables, but not the [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) statements for the data in the table. ([MDEV-22037](https://jira.mariadb.org/browse/MDEV-22037))
* [mariadb-backup](../../10-4/broken-reference/) has a new --rollback-xa option. By default, [mariadb-backup](../../10-4/broken-reference/) will not commit or rollback uncommitted XA transactions, and when the backup is restored any uncommitted XA transactions must be manually committed using XA COMMIT or be manually rolled-back using XA ROLLBACK. The --rollback-xa option can be used to rollback uncommitted XA transactions while performing a --prepare operation, eliminating the need for manual commit or rollback when the backup is restored. ([MDEV-21168](https://jira.mariadb.org/browse/MDEV-21168))
* [innodb\_encryption\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encryption_threads) is now limited to 255. ([MDEV-22258](https://jira.mariadb.org/browse/MDEV-22258))
* [shutdown-wait-for-slaves](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#shutdown-wait-for-slaves) system variable added, to control that a primary server only completes the shutdown after the last binary log has been sent to all connected slaves. This behavior is not active by default. Before the addition of this system variable, this was achieved using `mariadb-admin` shutdown `--wait_for_all_slaves` for a master. (MENT-202)
* `aria_pack` tool now provides the options `--datadir`, `--ignore-control-file`, `--require-control-file` for [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) tables with auto-recovery enabled (TRANSACTION=1). (MENT-657)
* [innodb\_instant\_alter\_column\_allowed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_instant_alter_column_allowed) system variable added to control whether an instant `ADD` or `DROP` column or reorder can change an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) format. The default is `add_drop_reorder` to allow a format change for all types of [ALTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter) . Option `never` should be used if a tablespace import to older versions of MariaDB Server should be possible. `add_last` should be used if a tablespace import into MariaDB Enterprise Server 10.3 or 10.4 should be possible. Instant [ALTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter) resulting in reordering of columns will not be possible, but an instant `ADD` column as the last column can be done (behavior of MariaDB Enterprise Server 10.3). ([MDEV-20590](https://jira.mariadb.org/browse/MDEV-20590))
* [require\_secure\_transport](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#require_secure_transport) system variable added, to enforce TLS secure connections. (MENT-66)
* Index length limit for the [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) and S3 storage engines has been increased from `1000` to `2000` bytes. (MENT-401)
* `IF EXISTS` clause can now be used with [RENAME TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/rename-table) and [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) (MENT-725)
* [sql\_if\_exists](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#sql_if_exists)) system variable implicitly applies IF EXISTS clause to several DDL statements, including [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table), [ALTER VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/views/alter-view), [ALTER FUNCTION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-function), [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table), [DROP VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/views/drop-view), [DROP FUNCTION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-functions/drop-function), `DROP PACKAGE`, and [RENAME TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/rename-table). (MENT-725)
* [S3 storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine) now provides support for replication. A new system parameter [s3\_slave\_ignore\_updates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine/s3-storage-engine-system-variables#s3_slave_ignore_updates) was added to define whether S3 replication is the same S3 storage for primary and replica. A new system parameter [s3\_replicate\_alter\_as\_create\_select](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine/s3-storage-engine-system-variables#s3_replicate_alter_as_create_select) controls whether all rows should be added to the binary log when a S3 table is altered to a local table. (MENT-725)
* [S3 storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine) now supports partitioning with the limitation that `REBUILD PARTITION`, `TRUNCATE PARTITION`, and `REORGANIZE PARTITION` cannot be used. (MENT-725)
* System user `mariadb.sys` has been added. ([MDEV-19650](https://jira.mariadb.org/browse/MDEV-19650))

## Issues Fixed

### Can result in data loss

* Possible crash with data loss when an executing an update of `PRIMARY KEY` columns on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table with a [BLOB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/blob) column. ([MDEV-22384](https://jira.mariadb.org/browse/MDEV-22384))

### Can result in a hang or crash

* [MariaDB Enterprise Backup](../../10-4/broken-reference/) ignored the timeout setting [--ftwrl-wait-timeout](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) when an explicit `LOCK TABLES ... WRITE` was active in another session. As a result, MariaDB Enterprise Server waited for release of the lock even if the timeout was reached. ([MDEV-20230](https://jira.mariadb.org/browse/MDEV-20230))
* When additional `open_table_caches_instances` have been created, a crash could occur due to exceeding the limit of open file descriptors. ([MDEV-18027](https://jira.mariadb.org/browse/MDEV-18027))
* Clean shutdown of [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) was not possible due to a deadlock situation between Galera Nodes. (MENT-432)
* Adding a column to discarded [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) tablespace was possible, resulting in a crash. ([MDEV-22446](https://jira.mariadb.org/browse/MDEV-22446))
* [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table could crash when an index field has been converted from `utf8mb3` to `utf8mb4` character set. ([MDEV-20726](https://jira.mariadb.org/browse/MDEV-20726))
* A [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) Node (Galera) could hang on rejoining the cluster during IST. ([MDEV-21002](https://jira.mariadb.org/browse/MDEV-21002))

### Can result in unexpected behavior

* Replication could be aborted when the replication data includes nested version-based conditional comments.
* [mariadbd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) and `mariadbd-safe` processes showed as running after a server shutdown. ([MDEV-21563](https://jira.mariadb.org/browse/MDEV-21563))
* [MariaDB Enterprise Backup](../../10-4/broken-reference/) ignored the [ignore\_db\_dirs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#ignore_db_dirs) configuration from the server configuration file. ([MDEV-19347](https://jira.mariadb.org/browse/MDEV-19347))
* A duplicate key error showed the duplicate key value truncated to 64 characters without indicating the truncation. ([MDEV-20604](https://jira.mariadb.org/browse/MDEV-20604))
* Using `SET GLOBAL` for the InnoDB variables [innodb\_ft\_aux\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_aux_table), [innodb\_ft\_server\_stopword\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_server_stopword_table) , [innodb\_ft\_user\_stopword\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_user_stopword_table) , and [innodb\_buffer\_pool\_filename](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename) could lead to corrupted strings for the settings. ([MDEV-22393](https://jira.mariadb.org/browse/MDEV-22393))
* Changing the `Server-Id` could lead to events being disabled for replicas, even if a single node configuration without a replica was used. ([MDEV-21758](https://jira.mariadb.org/browse/MDEV-21758))
* [SHOW PRIVILEGES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-privileges) incorrectly shows the privilege `Delete versioning rows` instead of [Delete history](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#table-privileges) . ([MDEV-20382](https://jira.mariadb.org/browse/MDEV-20382))
* Wrong query results have been returned with [optimizer\_switch="split\_materialized=on"](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch) ([MDEV-21614](https://jira.mariadb.org/browse/MDEV-21614))
* [SHOW GRANTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-grants) does not quote role names properly for a user granted to this role. ([MDEV-20076](https://jira.mariadb.org/browse/MDEV-20076))
* Partitioning could choose a wrong partition for `RANGE` partitioning by [DECIMAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/decimal) column. ([MDEV-21195](https://jira.mariadb.org/browse/MDEV-21195))
* A performance regression when optimizer flag `rowid_filter` is activated. ([MDEV-21794](https://jira.mariadb.org/browse/MDEV-21794))
* An [ALTER USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/alter-user) defining the authentication plugin did not remove any other authentication plugin from mysql.global\_priv for this user. ([MDEV-21928](https://jira.mariadb.org/browse/MDEV-21928))
* An online `ADD PRIMARY KEY` could fail after instant DROP or reorder was executed for fields of the same [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table. ([MDEV-21658](https://jira.mariadb.org/browse/MDEV-21658))
* Dropping an indexed column could occur as an instant operation although [DROP INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-index) is not instantaneous. ([MDEV-22465](https://jira.mariadb.org/browse/MDEV-22465))
* A [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) query with many `JOIN` and `UNION ALL` clauses could result in `ERROR 9 (HY000) Unexpected end-of-file` (MENT-750)

### Related to installation or upgrade

* The plugin `pam_user_map.so` was not provided with binary tarball packages. ([MDEV-21913](https://jira.mariadb.org/browse/MDEV-21913))
* Upgrade to MariaDB Enterprise Server 10.4 could result in inability to access the [mysql.user](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-user-table) system table, if the `root` user was renamed before the upgrade. In MariaDB Enterprise Server 10.4, [mysql.user](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-user-table) became a view owned by `root` user. This view is now owned by the `mariadb.sys` system internal user. ([MDEV-19650](https://jira.mariadb.org/browse/MDEV-19650))
* Upgrade from an older MariaDB Server or MySQL Server version to MariaDB Enterprise Server could lead to an empty [mysql.global\_priv](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-global_priv-table) system table if the existing [mysql.user](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-user-table) system table includes an `auth_string` field. This field was renamed to `authentication_string` with MariaDB Server 5.5. ([MDEV-21244](https://jira.mariadb.org/browse/MDEV-21244))

## Interface Changes

* [ER\_SLAVE\_IGNORED\_SHARED\_TABLE](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) error code added
* [innodb\_encryption\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encryption_threads) system variable maximum value changed from 4294967295 to 255
* [innodb\_instant\_alter\_column\_allowed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_instant_alter_column_allowed) system variable added
* [mariadb-backup](../../10-4/broken-reference/) --rollback-xa command-line option added
* mariadbd --innodb-instant-alter-column-allowed command-line option added
* mariadbd --s3-replicate-alter-as-create-select command-line option added
* mariadbd --s3-slave-ignore-updates command-line option added
* [mariadbd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) --shutdown-wait-for-slaves command-line option added
* [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) --ignore-table-data command-line option added
* [shutdown\_wait\_for\_slaves](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables) system variable added
* [sql\_if\_exists](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#sql_if_exists) system variable added

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.4.13-7 is provided for:

* Red Hat Enterprise Linux 8
* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 6
* CentOS 8
* CentOS 7
* CentOS 6
* Ubuntu 20.04
* Ubuntu 18.04
* Ubuntu 16.04
* Debian 10
* Debian 9
* Debian 8
* SUSE Linux Enterprise Server 15
* SUSE Linux Enterprise Server 12
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see [MariaDB Corporation Engineering Policies".](https://mariadb.com/engineering-policies)

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a `README` file within the download.

## Installation Instructions

* [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions)

##

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
