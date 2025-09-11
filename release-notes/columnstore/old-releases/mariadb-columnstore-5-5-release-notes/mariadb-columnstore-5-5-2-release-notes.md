# MariaDB ColumnStore 5.5.2 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/columnstore/mariadb-columnstore-5-5-release-notes/MariaDB_Enterprise_ColumnStore/README.md) is a columnar storage engine that is included with the MariaDB Enterprise Server. This is the fourth release in the [Enterprise ColumnStore](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview#mariadb-enterprise-columnstore) 5 series.

This release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/columnstore/mariadb-columnstore-5-5-release-notes/MariaDB_Enterprise_ColumnStore/README.md) is included with MariaDB Enterprise Server 10.5.9-6.

This release is of General Availability (GA) maturity.

MariaDB Enterprise ColumnStore 5.5.2 was released on 2021-03-15.

## Notable Changes

* Added the ec2\_iam\_mode=enabled option to storagemanager.cnf, which enables an EC2 instance to authenticate with S3 using its IAM role. ([MCOL-4386](https://jira.mariadb.org/browse/MCOL-4386))
* Added support for CREATE TABLE AS SELECT .. COUNT() .. FROM .. GROUP BY .. ([MCOL-3785](https://jira.mariadb.org/browse/MCOL-3785))
* Removed legacy OAM scripts. ([MCOL-4193](https://jira.mariadb.org/browse/MCOL-4193))
* Consolidated ColumnStore log files in the /var/log/mariadb/columnstore/ directory. ([MCOL-4483](https://jira.mariadb.org/browse/MCOL-4483))
* Moved CMAPI log files to the /var/log/mariadb/columnstore/cmapi/ directory. ([MCOL-4494](https://jira.mariadb.org/browse/MCOL-4494))
* Added more logs to /etc/logrotate.d/columnstore configuration. ([MCOL-4319](https://jira.mariadb.org/browse/MCOL-4319))
* Refactor ColumnStore systemd services to ensure startup waits for network connectivity. ([MCOL-4170](https://jira.mariadb.org/browse/MCOL-4170))
* Results from SELECT .. ORDER BY BINARY(col) now match InnoDB. ([MCOL-4454](https://jira.mariadb.org/browse/MCOL-4454))
* Results from FLOOR() function now match InnoDB for DATETIME, TIMESTAMP, and TIME columns. ([MCOL-4263](https://jira.mariadb.org/browse/MCOL-4263))

## Issues Fixed

### Can result in data loss

* Extent map can become corrupted during startup under 5.5.1 with a large extent map and shared storage. ([MCOL-4546](https://jira.mariadb.org/browse/MCOL-4546))

### Can result in a hang or crash

* A join with different collations crashes the ExeMgr process. ([MCOL-4470](https://jira.mariadb.org/browse/MCOL-4470))
* A time zone conversion results in a hang due to a deadlock in the thread pool. ([MCOL-4486](https://jira.mariadb.org/browse/MCOL-4486))
* When replication is used, INSERT INTO .. SELECT .. FROM ... results in a hang in the SQL thread. ([MCOL-4515](https://jira.mariadb.org/browse/MCOL-4515))

### Can result in unexpected behavior

* Error message from LOAD DATA INFILE statement mentions wrong path for .err and .bad files. ([MCOL-571](https://jira.mariadb.org/browse/MCOL-571))
* Table remains locked when ColumnStore is forced to restart. ([MCOL-3324](https://jira.mariadb.org/browse/MCOL-3324))
* CREATE TABLE AS SELECT .. LIMIT 0 writes a row to the table. ([MCOL-4453](https://jira.mariadb.org/browse/MCOL-4453))
* SELECT DISTINCT col FROM TABLE LIMIT offset, limit statement ignores offset. ([MCOL-4455](https://jira.mariadb.org/browse/MCOL-4455))
* Results from a query with both a left join and an inner join are incorrect. ([MCOL-4493](https://jira.mariadb.org/browse/MCOL-4493))
* Performance regression for queries that filter on small CHAR columns that use latin1 character set. ([MCOL-4527](https://jira.mariadb.org/browse/MCOL-4527))
* Queries on big tables that filter on small CHAR columns ignore the collation. ([MCOL-4539](https://jira.mariadb.org/browse/MCOL-4539))
* Results from a UDAF are incorrect when executed in a non-distributed manner. ([MCOL-4585](https://jira.mariadb.org/browse/MCOL-4585))

### Related to install and upgrade

* Configuration files not moved back into place after in-place upgrade. ([MCOL-4597](https://jira.mariadb.org/browse/MCOL-4597))

## Platforms

In alignment with the [enterprise lifecycle](../../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 5.5.2 is provided for:

* CentOS 8
* CentOS 7
* Debian 10
* Debian 9
* Red Hat Enterprise Linux 8
* Red Hat Enterprise Linux 7
* SUSE Linux Enterprise Server 15
* SUSE Linux Enterprise Server 12
* Ubuntu 20.04
* Ubuntu 18.04
* Ubuntu 16.04

## Installation Instructions

* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore 5 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[ and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 5 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)

## Upgrade Instructions

* [Major Release Upgrades for MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/columnstore-release-notes/README.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
