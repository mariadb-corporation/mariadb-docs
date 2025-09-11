# Release Notes for MariaDB Enterprise Server 10.3.23-7

This seventh release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.3.23-7 was released on 2020-06-08.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/cve.org) link) | CVSS base score                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [CVE-2020-2760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2760)                                                                                                 | 5.5                                                                          |
| [CVE-2020-2752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2752)                                                                                                 | 5.3                                                                          |
| [CVE-2020-2814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2814)                                                                                                 | 4.9                                                                          |
| [CVE-2020-2812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2812)                                                                                                 | 4.9                                                                          |
| [CVE-2020-13249](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13249)                                                                                               | N/A (Medium)[#1](release-notes-for-mariadb-enterprise-server-10-3-23-7.md#1) |

`#1`:\
MariaDB CVEs are assigned a word rating instead of a CVSS base score. See the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies) for details.

## Notable Changes

* [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) now displays a warning when upgrading a replica from MySQL Server to MariaDB Enterprise Server if data was present in the `mysql.slave_master_info` and `mysql.slave_relay_log_info` tables. A warning is needed as this information will be ignored. ([MDEV-10047](https://jira.mariadb.org/browse/MDEV-10047))
* [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) has a new `--ignore-table-data=<table>` option. When used, the dump will include the table definition for the listed tables, but not the INSERT statements for the data in the table. ([MDEV-22037](https://jira.mariadb.org/browse/MDEV-22037))
* [mariadb-backup](../../10-3/broken-reference/) has a new [--rollback-xa option](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md). By default, mariadb-backup will not commit or rollback uncommitted XA transactions, and when the backup is restored any uncommitted XA transactions must be manually committed using XA [COMMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/commit) or be manually rolled-back using [XA ROLLBACK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/rollback). The [--rollback-xa option](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) can be used to rollback uncommitted XA transactions while performing a --prepare operation, eliminating the need for manual commit or rollback when the backup is restored. ([MDEV-21168](https://jira.mariadb.org/browse/MDEV-21168))
* [innodb\_encryption\_thread](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encryption_threads) is now limited to 255. ([MDEV-22258](https://jira.mariadb.org/browse/MDEV-22258))
* [shutdown-wait-for-slaves](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables) system variable added, to control that a primary server only completes the shutdown after the last binary log has been sent to all connected slaves. This behavior is not active by default. Before the addition of this system variable, this was achieved using `mysqladmin shutdown --wait_for_all_slaves` for a master. (MENT-202)
* `aria_pack` tool now provides the options `--datadir, --ignore-control-file, --require-control-file` for [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) tables with auto-recovery enabled (`TRANSACTION=1``). (MENT-657)`
* [innodb\_instant\_alter\_column\_allowed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_instant_alter_column_allowed) system variable added to control whether an instant `ADD` or `DROP` column or reorder can change an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) format. The default is `add_last` to allow an instant `ADD COLUMN` as the last column of the table. Option `never` should be used if a tablespace import to older version of MariaDB Server should be possible. ([MDEV-20590](https://jira.mariadb.org/browse/MDEV-20590))

## Issues Fixed

### Can result in data loss

* Possible crash with data loss when an executing an update of `PRIMARY KEY` columns on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table with a [BLOB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/blob) column. ([MDEV-22384](https://jira.mariadb.org/browse/MDEV-22384))

### Can result in a hang or crash

* [MariaDB Enterprise Backup](../../10-3/broken-reference/) ignored the timeout setting [--ftwrl-wait-timeout](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) when an explicit `LOCK TABLES ... WRITE` was active in another session. As a result, MariaDB Enterprise Server waited for release of the lock even if the timeout was reached. ([MDEV-20230](https://jira.mariadb.org/browse/MDEV-20230))
* When additional `open_table_caches_instances` have been created, a crash could occur due to exceeding the limit of open file descriptors. ([MDEV-18027](https://jira.mariadb.org/browse/MDEV-18027))
* Clean shutdown of [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) was not possible due to a deadlock situation between Galera Nodes. (MENT-432)
* Adding a column to discarded [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) tablespace was possible, resulting in a crash. ([MDEV-22446](https://jira.mariadb.org/browse/MDEV-22446))

### Can result in unexpected behavior

* Replication could be aborted when the replication data includes nested version-based conditional comments.
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) and `mysqld_safe` processes showed as running after a server shutdown. ([MDEV-21563](https://jira.mariadb.org/browse/MDEV-21563))
* [MariaDB Enterprise Backup](../../10-3/broken-reference/) ignored the [ignore\_db\_dirs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#ignore_db_dirs) configuration from the server configuration file. ([MDEV-19347](https://jira.mariadb.org/browse/MDEV-19347))
* A duplicate key error showed the duplicate key value truncated to 64 characters without indicating the truncation. ([MDEV-20604](https://jira.mariadb.org/browse/MDEV-20604))
* Using `SET GLOBAL` for the [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) variables [innodb\_ft\_aux\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_aux_table), i [innodb\_ft\_server\_stopword\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_server_stopword_table), [innodb\_ft\_user\_stopword\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_ft_user_stopword_table) , and [innodb\_buffer\_pool\_filename](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename) could lead to corrupted strings for the settings. ([MDEV-22393](https://jira.mariadb.org/browse/MDEV-22393))
* Changing the `Server-Id` could lead to events being disabled for replicas, even if a single node configuration without a replica was used. ([MDEV-21758](https://jira.mariadb.org/browse/MDEV-21758))
* [SHOW PRIVILEGES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-privileges) incorrectly shows the privilege `Delete versioning rows` instead of `Delete history` ([MDEV-20382](https://jira.mariadb.org/browse/MDEV-20382))
* Wrong query results have been returned with [optimizer\_switch="split\_materialized=on"](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch) ([MDEV-21614](https://jira.mariadb.org/browse/MDEV-21614))
* [SHOW-GRANTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-grants) does not quote role names properly for a user granted to this role. ([MDEV-20076](https://jira.mariadb.org/browse/MDEV-20076))
* Partitioning could choose a wrong partition for RANGE partitioning by [DECIMAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/decimal) column. ([MDEV-21195](https://jira.mariadb.org/browse/MDEV-21195))

### Related to installation or upgrade

* The plugin `pam_user_map.so` was not provided with binary tarball packages. ([MDEV-21913](https://jira.mariadb.org/browse/MDEV-21913))

## Interface Changes

* [innodb\_encryption\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encryption_threads) system variable maximum value changed from 4294967295 to 255
* [innodb\_instant\_alter\_column\_allowed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_instant_alter_column_allowed) system variable added
* [mariadb-backup](../../10-3/broken-reference/) [--rollback-xa](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) command-line option added
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--innodb-instant-alter-column-allowed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-instant-alter-algorithm) command-line option added
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--shutdown-wait-for-slaves](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/shutdown) command-line option added
* [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) [--ignore-table-data](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) command-line option added
* [shutdown\_wait\_for\_slaves](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables) system variable added

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.3.23-7 is provided for:

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

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a `README` file within the download.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
