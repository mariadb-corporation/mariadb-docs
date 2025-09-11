# Release Notes for MariaDB Enterprise Server 10.2.33-8

This eighth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.2 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.2.33-8 was released on 2020-09-08.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-2/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2021-2022](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2022)                                                                                                 | 4.4             |

## Notable Changes

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.7.29.
* Limit [innodb\_encryption\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_encryption_threads) to `255` ([MDEV-22258](https://jira.mariadb.org/browse/MDEV-22258))
* Minimum value of [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length) raised to `8` (previously `4`) so fixed size data types like [DOUBLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/double) and [BIGINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/bigint) are not truncated for lower values of [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length). ([MDEV-22715](https://jira.mariadb.org/browse/MDEV-22715))
* [INFORMATION\_SCHEMA.INNODB\_TABLESPACES\_ENCRYPTION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_encryption-table) requires [PROCESS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#process) instead of [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super) privilege. ([MDEV-23003](https://jira.mariadb.org/browse/MDEV-23003))
* Backport from MariaDB Server 10.5.4 of improvements to [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) for InnoDB. (MENT-636)

## Issues Fixed

### Can result in data loss

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) doublewrite recovery can corrupt data pages. ([MDEV-11799](https://jira.mariadb.org/browse/MDEV-11799))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table can disappear when trying to change primary key after disabling Foreign Key checks and violating a Foreign Key constraint. (MENT-804)
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) corruption in delete buffering. ([MDEV-22497](https://jira.mariadb.org/browse/MDEV-22497))

### Can result in a hang or crash

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) deadlock in [FLUSH TABLES .. FOR EXPORT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) ([MDEV-22890](https://jira.mariadb.org/browse/MDEV-22890))\*
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) data file extension is not crash-safe. ([MDEV-23190](https://jira.mariadb.org/browse/MDEV-23190))
* [innodb\_log\_optimize\_ddl](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_log_optimize_ddl) =off is not crash safe. ([MDEV-21347](https://jira.mariadb.org/browse/MDEV-21347))
* Deadlock involving parallel workers, [STOP SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica), and [FLUSH TABLES WITH READ LOCK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) ([MDEV-23089](https://jira.mariadb.org/browse/MDEV-23089))
* Crashes when running a SQL query containing a specific subquery pattern. ([MDEV-23221](https://jira.mariadb.org/browse/MDEV-23221))
* Dropping the adaptive hash index may cause DDL to lock up [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) ([MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456))
* [RESET MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/reset-master) could result in a crash, when the value exceeds the max allowed `2147483647` ([MDEV-22451](https://jira.mariadb.org/browse/MDEV-22451))
* Crash on `WITH RECURSIVE` large query. ([MDEV-22748](https://jira.mariadb.org/browse/MDEV-22748))
* Crash with Prepared Statement with a `?` parameter inside a re-used CTE. ([MDEV-22779](https://jira.mariadb.org/browse/MDEV-22779))
* MariaDB could crash after changing the `query_cache` size. ([MDEV-5924](https://jira.mariadb.org/browse/MDEV-5924))
* Crash in `CREATE TABLE AS SELECT` when the precision of returning type `= 0` ([MDEV-22502](https://jira.mariadb.org/browse/MDEV-22502))
* [ENUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/enum) or [SET](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) in a [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) statement, which has a 0x00 byte in one of the values could crash the server. ([MDEV-22111](https://jira.mariadb.org/browse/MDEV-22111))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) recovery can block server startup. (MENT-915)

### Can result in unexpected behavior

* Service shutdown fails if OS datetime has been updated backwards. ([MDEV-17481](https://jira.mariadb.org/browse/MDEV-17481))
* `ALTER TABLE .. ANALYZE PARTITION` can run for hours for huge tables if engine-independent persistent statistics are enabled, due to reading and locking of all rows in the \* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table instead of for the partition. ([MDEV-21472](https://jira.mariadb.org/browse/MDEV-21472))
* [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) can fail with privilege error when [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) privilege exists at database level but [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) privilege exists at table level. ([MDEV-23010](https://jira.mariadb.org/browse/MDEV-23010))
* Latency and throughput regression identified in write-heavy benchmarks for latest releases in MariaDB Server 10.2, 10.3, and 10.4. (MENT-909)
* `START SLAVE UNTIL .. file .. pos` stops at an earlier position earlier than defined if the transaction that spans over the given stop position has to roll back due to conflicts. ([MDEV-15152](https://jira.mariadb.org/browse/MDEV-15152))
* [mariadb-backup --prepare](../../10-2/broken-reference/) does not stop on errors while applying InnoDB redo log. ([MDEV-22354](https://jira.mariadb.org/browse/MDEV-22354))

### Related to install and upgrade

* [UNINSTALL PLUGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin) and [UNINSTALL SONAME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname) can't run if the library file doesn't exist. ([MDEV-21258](https://jira.mariadb.org/browse/MDEV-21258))

## Interface Changes

* [ER\_TRANSACTIONAL\_ARIA\_LOG\_ENGINE](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) error code added
* [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length) system variable minimum value changed from 4 to 8

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.2.33-8 is provided for:

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

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

#### Note\*\*

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a README file within the download.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
