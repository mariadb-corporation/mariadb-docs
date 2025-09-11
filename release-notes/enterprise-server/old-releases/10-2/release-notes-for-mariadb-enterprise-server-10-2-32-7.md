# Release Notes for MariaDB Enterprise Server 10.2.32-7

This seventh release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.2 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.2.32-7 was released on 2020-06-08.

## Fixed Security Vulnerabilities

| CVE (with cve.org link)                                                         | CVSS base score                                                              |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [CVE-2020-2760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2760)   | 5.5                                                                          |
| [CVE-2020-2752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2752)   | 5.3                                                                          |
| [CVE-2020-2814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2814)   | 4.9                                                                          |
| [CVE-2020-2812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2812)   | 4.9                                                                          |
| [CVE-2020-13249](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13249) | N/A (Medium)[#1](release-notes-for-mariadb-enterprise-server-10-2-32-7.md#1) |

`#1`:\
MariaDB CVEs are assigned a word rating instead of a CVSS base score. See the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies/) for details.

## Notable Changes

* [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) now displays a warning when upgrading a replica from MySQL Server to MariaDB Enterprise Server if data was present in the `mysql.slave_master_info` and `mysql.slave_relay_log_info` tables. A warning is needed as this information will be ignored. ([MDEV-10047](https://jira.mariadb.org/browse/MDEV-10047))
* [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) has a new `--ignore-table-data=<table>` option. When used, the dump will include the table definition for the listed tables, but not the [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) statements for the data in the table. ([MDEV-22037](https://jira.mariadb.org/browse/MDEV-22037))
* [mariadb-backup](../../10-2/broken-reference/) has a new [--rollback-xa](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) option. By default, [mariadb-backup](../../10-2/broken-reference/) will not commit or rollback uncommitted XA transactions, and when the backup is restored any uncommitted XA transactions must be manually committed using XA [COMMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/commit) or be manually rolled-back using [XA ROLLBACK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/rollback). The [--rollback-xa](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) option can be used to rollback uncommitted XA transactions while performing a [--prepare](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/prepared-statements/prepare-statement) operation, eliminating the need for manual commit or rollback when the backup is restored. ([MDEV-21168](https://jira.mariadb.org/browse/MDEV-21168))
* [innodb\_encryption\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_encryption_threads) is now limited to `255`. ([MDEV-22258](https://jira.mariadb.org/browse/MDEV-22258))

## Issues Fixed

### Can result in data loss

* Possible crash with data loss when an executing an update of PRIMARY KEY columns on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table with a [BLOB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/blob) column. ([MDEV-22384](https://jira.mariadb.org/browse/MDEV-22384))

### Can result in a hang or crash

* [MariaDB Enterprise Backup](../../10-2/broken-reference/) ignored the timeout setting [--ftwrl-wait-timeout](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) when an explicit `LOCK TABLES ... WRITE` was active in another session. As a result, MariaDB Enterprise Server waited for release of the lock even if the timeout was reached. ([MDEV-20230](https://jira.mariadb.org/browse/MDEV-20230))
* When additional `open_table_caches_instances` have been created, a crash could occur due to exceeding the limit of open file descriptors. ([MDEV-18027](https://jira.mariadb.org/browse/MDEV-18027))

### Can result in unexpected behavior

* Replication could be aborted when the replication data includes nested version-based conditional comments.
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) and `mysqld_safe` processes showed as running after a server shutdown. ([MDEV-21563](https://jira.mariadb.org/browse/MDEV-21563))
* [MariaDB Enterprise Backup](../../10-2/broken-reference/) ignored the [ignore\_db\_dirs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#ignore_db_dirs) configuration from the server configuration file. ([MDEV-19347](https://jira.mariadb.org/browse/MDEV-19347))
* A duplicate key error showed the duplicate key value truncated to 64 characters without indicating the truncation. ([MDEV-20604](https://jira.mariadb.org/browse/MDEV-20604))
* Using `SET GLOBAL` for the [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) variables [innodb\_ft\_aux\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_ft_aux_table), [innodb\_ft\_server\_stopword\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_ft_server_stopword_table) , [innodb\_ft\_user\_stopword\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_ft_user_stopword_table) , and [innodb\_buffer\_pool\_filename](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_buffer_pool_filename) could lead to corrupted strings for the settings. ([MDEV-22393](https://jira.mariadb.org/browse/MDEV-22393))
* Changing the `Server-Id` could lead to events being disabled for replicas, even if a single node configuration without a replica was used. ([MDEV-21758](https://jira.mariadb.org/browse/MDEV-21758))

### Related to installation or upgrade

* The plugin `pam_user_map.so` was not provided with binary tarball packages. ([MDEV-21913](https://jira.mariadb.org/browse/MDEV-21913))
* Installing MariaDB Enterprise Server on SUSE Linux Enterprise Server 12 or 15 could result in file conflicts. (MENT-730)

## Interface Changes

* [innodb\_encryption\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_encryption_threads) system variable maximum value changed from 4294967295 to 255
* [mariadb-backup --rollback-xa](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) command-line option added
* [mysqldump --ignore-table-data](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) command-line option added

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.2.32-7 is provided for:

* Red Hat Enterprise Linux 8
* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 6
* CentOS 8
* CentOS 7
* CentOS 6
* Ubuntu 18.04
* Ubuntu 16.04
* Debian 10
* Debian 9
* Debian 8
* SUSE Linux Enterprise Server 15
* SUSE Linux Enterprise Server 12
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies/)".

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies/). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads/). Instructions for installation are included as a `README` file within the download.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
