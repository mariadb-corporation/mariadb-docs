# Release Notes for MariaDB Enterprise Server 10.4.11-5

This fifth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.4.11-5 was released on 2020-01-06.

## Notable Changes

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) no longer sends unnecessary warnings to the error log about maximum row size for DDL statements when [innodb\_strict\_mode=OFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_strict_mode) and [log\_warnings<=2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_warnings) ([MDEV-20832](https://jira.mariadb.org/browse/MDEV-20832))
* Redundant writes to the [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) redo log have been removed. ([MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024))
* The default for the plugin load option plugin-maturity is now `stable` (MENT-240)
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) and the MariaDB Audit plugin trace now add the user who initiated statements with the `DELAYED` option. In previous versions a system user was added. (MENT-237)
* MariaDB ColumnStore, a columnar storage engine, is now included with MariaDB Enterprise Server 10.4. Specific details on this component may be found in the [ColumnStore 1.4.2 release notes](../../../columnstore/old-releases/columnstore-1-4/).
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) no longer permits [server\_audit\_output\_type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables) to be set to `SYSLOG` on Microsoft Windows. (MENT-258)

## Issues Fixed

### Can result in data loss

* A table could not be loaded after an instant `ALTER ... ADD COLUMN` or `ALTER ... DROP COLUMN`, if the primary key is a `CHAR` column with variable-length encoding like `UTF8` ([MDEV-21088](https://jira.mariadb.org/browse/MDEV-21088))
* In rare conditions commits could be applied in the wrong order if the replica is running in optimistic mode. ([MDEV-20707](https://jira.mariadb.org/browse/MDEV-20707))

### Can result in a hang or crash

* Primary (master) could crash when it executes [RESET MASTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/reset-master) and a replica (slave) reconnects having reset its connection status with the primary (e.g., `CHANGE MASTER TO MASTER_USE_GTID = slave_pos`). (MENT-19376)
* `"Out of memory"` error could occur when accessing partitioned [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) tables. ([MDEV-20611](https://jira.mariadb.org/browse/MDEV-20611))
* A crash could occur when `ADD PRIMARY KEY` was executed by a connection just after another connection issued an instant `ADD COLUMN` to the same [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table and if DMLs were executed at the same time. ([MDEV-21045](https://jira.mariadb.org/browse/MDEV-21045))
* A crash could occur when rowid filtering optimization is enabled using [optimizer\_switch='rowid\_filter=on'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch) ([MDEV-20407](https://jira.mariadb.org/browse/MDEV-20407))

### Can result in unexpected behavior

* Client received error `SEC_E_INVALID_TOKEN` when SSL is used and connecting to MariaDB Enterprise Server running on Microsoft Windows. ([MDEV-13492](https://jira.mariadb.org/browse/MDEV-13492))
* The restore of [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) tables was not always possible if MariaDB Backup was using the parameters [--prepare](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) `--incremental` ([MDEV-18310](https://jira.mariadb.org/browse/MDEV-18310))
* An incomplete result set was returned when [sort\_buffer\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#sort_buffer_size) was too small. ([MDEV-21044](https://jira.mariadb.org/browse/MDEV-21044))
* A query with system versioning filters did not show an error when executed on not [system versioned tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables). ([MDEV-18929](https://jira.mariadb.org/browse/MDEV-18929))
* [CHECK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table) erroneously reported error `"Found a misplaced row"` for [system versioned tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) with history partition. ([MDEV-21011](https://jira.mariadb.org/browse/MDEV-21011))
* An instant operation could fail when adding a column and changing the collation on a non-indexed column. ([MDEV-20190](https://jira.mariadb.org/browse/MDEV-20190))

Interface Changes

* None.

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.4.11-5 is provided for:

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

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a `README` file within the download.

## Installation Instructions

* [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](broken-reference)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.4](broken-reference)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.4](broken-reference)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
