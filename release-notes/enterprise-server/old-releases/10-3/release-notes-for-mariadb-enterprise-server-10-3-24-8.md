# Release Notes for MariaDB Enterprise Server 10.3.24-8

This eighth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.3.24-8 was released on 2020-09-08.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2021-2022](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2022)                                                                                                 | 4.4             |

## Notable Changes

* Limit [innodb\_encryption\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encryption_threads) to 255 ([MDEV-22258](https://jira.mariadb.org/browse/MDEV-22258))
* Minimum value of [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length) raised to 8 (previously 4) so fixed size data types like [DOUBLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/double) and [BIGINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/bigint) are not truncated for lower values of [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length). ([MDEV-22715](https://jira.mariadb.org/browse/MDEV-22715))
* Backport from MariaDB Server 10.5.4 improvements to [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) for InnoDB. (MENT-636)
* Backport option [tls\_version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tls_version) from MariaDB Server 10.4. (MENT-581)

## Issues Fixed

### Can result in data loss

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) doublewrite recovery can corrupt data pages. ([MDEV-11799](https://jira.mariadb.org/browse/MDEV-11799))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table can disappear when trying to change primary key after disabling Foreign Key checks and violating a Foreign Key constraint. (MENT-804)
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) corruption in delete buffering. ([MDEV-22497](https://jira.mariadb.org/browse/MDEV-22497))
* Rollback of insert fails when column reorder happens. ([MDEV-22637](https://jira.mariadb.org/browse/MDEV-22637))
* Possible data inconsistency when executing ADD PRIMARY KEY with concurrent DML transactions. ([MDEV-23244](https://jira.mariadb.org/browse/MDEV-23244))

### Can result in a hang or crash

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) deadlock in [FLUSH TABLES .. FOR EXPORT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) ([MDEV-22890](https://jira.mariadb.org/browse/MDEV-22890))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) data file extension is not crash-safe. ([MDEV-23190](https://jira.mariadb.org/browse/MDEV-23190))
* [innodb\_log\_optimize\_ddl=OFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_optimize_ddl) is not crash safe. ([MDEV-21347](https://jira.mariadb.org/browse/MDEV-21347))
* Deadlock involving parallel workers, [STOP SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica), and [FLUSH TABLES WITH READ LOCK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) ([MDEV-23089](https://jira.mariadb.org/browse/MDEV-23089))
* Crashes when running a SQL query containing a specific subquery pattern. ([MDEV-23221](https://jira.mariadb.org/browse/MDEV-23221))
* Dropping the adaptive hash index may cause DDL to lock up InnoDB. ([MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456))
* [RESET MASTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/reset-master) TO could result in a crash, when the value exceeds the max allowed 2147483647 ([MDEV-22451](https://jira.mariadb.org/browse/MDEV-22451))
* Crash on `WITH RECURSIVE` large query. ([MDEV-22748](https://jira.mariadb.org/browse/MDEV-22748))
* Crash with Prepared Statement with a ? parameter inside a re-used CTE. ([MDEV-22779](https://jira.mariadb.org/browse/MDEV-22779))
* MariaDB could crash after changing the `query_cache` size. ([MDEV-5924](https://jira.mariadb.org/browse/MDEV-5924))
* Crash in `CREATE TABLE AS SELECT` when the precision of returning type `= 0` ([MDEV-22502](https://jira.mariadb.org/browse/MDEV-22502))
* [ENUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/enum) or [SET](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) in a [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) statement which has a `0x00` byte in one of the values could crash the server. ([MDEV-22111](https://jira.mariadb.org/browse/MDEV-22111))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) recovery can block server startup. (MENT-915)

### Can result in unexpected behavior

* Service shutdown fails if OS datetime has been updated backwards. ([MDEV-17481](https://jira.mariadb.org/browse/MDEV-17481))
* `ALTER TABLE .. ANALYZE PARTITION` can run for hours for huge tables if engine-independent persistent statistics are enabled, due to reading and locking of all rows in the [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table instead of for the partition. ([MDEV-21472](https://jira.mariadb.org/browse/MDEV-21472))
* [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) can fail with privilege error when [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) privilege exists at database level but [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) privilege exists at table level. ([MDEV-23010](https://jira.mariadb.org/browse/MDEV-23010))
* Latency and throughput regression identified in write-heavy benchmarks for latest releases in MariaDB Server 10.2, 10.3, and 10.4. (MENT-909)
* `START SLAVE UNTIL .. file ..` pos stops at an earlier position earlier than defined if the transaction that spans over the given stop position has to roll back due to conflicts. ([MDEV-15152](https://jira.mariadb.org/browse/MDEV-15152))
* `mariadb-backup` [--prepare](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) does not stop on errors while applying [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) redo log. ([MDEV-22354](https://jira.mariadb.org/browse/MDEV-22354))
* Point in time recovery of binary log fails with syntax error when [sql\_mode=ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode). ([MDEV-23108](https://jira.mariadb.org/browse/MDEV-23108))
* Replication aborts with [ER\_SLAVE\_CONVERSION\_FAILED](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) upon `CREATE .. SELECT` when [sql\_mode=ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode). ([MDEV-19632](https://jira.mariadb.org/browse/MDEV-19632))
* Regression in Audit Plugin Performance. (MENT-700)

### Related to install and upgrade

* [UNINSTALL PLUGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin) and [UNINSTALL SONAME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname) can't run if the library file doesn't exist. ([MDEV-21258](https://jira.mariadb.org/browse/MDEV-21258))
* [Spider plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) install hangs installation process. (MENT-926)

## Interface Changes

* [mariadb-backup](../../10-3/broken-reference/) [--tls-version](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) command-line option added
* [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length) system variable minimum value changed from 4 to 8
* [mysql\_upgrade --tls-version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-upgrade) command-line option added
* [mysql --tls-version](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb/README.md) command-line option added
* [mysqladmin --tls-version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/mariadb-admin#mariadb-admin) command-line option added
* [mysqlbinlog --tls-version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) command-line option added
* [mysqlcheck --tls-version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/table-tools/mariadb-check) command-line option added
* [mysqld --tls-version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) command-line option added
* [mysqldump --tls-version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) command-line option added
* [mysqlimport --tls-version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-import) command-line option added
* [mysqlshow --tls-version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/mariadb-show) command-line option added
* [mysqlslap --tls-version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/testing-tools/mariadb-slap) command-line option added
* [tls-version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables#tls_version) system variable added

## \* Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.3.24-8 is provided for:

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

{% hint style="info" %}
**Note**

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a `README` file within the download.
{% endhint %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
