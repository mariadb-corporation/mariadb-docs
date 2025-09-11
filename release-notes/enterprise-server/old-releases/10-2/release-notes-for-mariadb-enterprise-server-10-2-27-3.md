# Release Notes for MariaDB Enterprise Server 10.2.27-3

This third release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.2 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.2.27-3 was released on 2019-09-30.

## Issues Fixed

### Can result in data loss

* Due to a race condition in InnoDB, an exclusive lock to an inserted record could be wrongly granted to multiple transactions when the [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) transaction commits. This could lead to a server crash or data loss. ([MDEV-15326](https://jira.mariadb.org/browse/MDEV-15326))
* INSERT...ON DUPLICATE KEY UPDATE, when there is more than one key, could result in inconsistent data between Primary and replica for replication mode [MIXED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/binary-log-formats#mixed-logging) and [STATEMENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/binary-log-formats#statement-based-logging). This has been fixed for MIXED, but cannot be controlled by the replication for STATEMENT based replication.
* Inconsistent replicas need to be set up again from the Primary. ([MDEV-17614](https://jira.mariadb.org/browse/MDEV-17614))

### Can result in a hang or crash

* Replication could hang for [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) transactions as [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) has its own concurrency control [innodb\_thread\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_thread_concurrency). ([MDEV-20247](https://jira.mariadb.org/browse/MDEV-20247))

### Can result in unexpected behavior

* After setting [SET foreign\_key\_checks=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#foreign_key_checks) it is possible to drop indexes from referenced (parent) tables, which could cause [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) to behave as if table `doesn't exist in engine` ([MDEV-17187](https://jira.mariadb.org/browse/MDEV-17187))
* Corner case where [MariaDB Backup](broken-reference) could fail because encrypted data files could not be copied if created shortly before the backup was started. ([MDEV-18128](https://jira.mariadb.org/browse/MDEV-18128))
* [MariaDB Backup](broken-reference) could fail in the prepare face if the redo log is bigger than 512GB. ([MDEV-20060](https://jira.mariadb.org/browse/MDEV-20060))
* Basic 3-way join queries are not parsed. ([MDEV-19421](https://jira.mariadb.org/browse/MDEV-19421))

### Related to performance

* Optimized scanning of the undo log versions while scanning the secondary index versions. ([MDEV-20301](https://jira.mariadb.org/browse/MDEV-20301))

## Interface Changes

* None.

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.2.27-3 is provided for:

* CentOS 8
* CentOS 7
* CentOS 6
* Debian 10
* Debian 9
* Debian 8
* Red Hat Enterprise Linux 8
* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 6
* Ubuntu 18.04
* Ubuntu 16.04
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies/)".

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies/). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads/). Instructions for installation are included as a `README` file within the download.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
