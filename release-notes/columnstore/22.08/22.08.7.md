# MariaDB ColumnStore 22.08.7 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 22.08.7 is a maintenance release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md). MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server.

MariaDB Enterprise ColumnStore 22.08.7 was released on 2022-12-21. This release is of General Availability (GA) maturity.

MariaDB Enterprise ColumnStore 22.08 replaces MariaDB Enterprise ColumnStore 6 in MariaDB Enterprise Server 10.6.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.11-6.

Users of earlier MariaDB Enterprise ColumnStore 22.08 releases are encouraged to upgrade.

## Issues Fixed

### Can result in a hang or crash

* When the ExeMgr facility in the PrimProc process is restarted, if the SELECT component of an UPDATE statement fails, the DMLProc process performs a ROLLBACK operation, which can hang if the ExeMgr facility is not yet available. ([MCOL-5263](https://jira.mariadb.org/browse/MCOL-5263))
  * Starting with this release, if this scenario occurs, DMLProc avoids the hang by retrying the operation after a timeout period.
* When ExeMgr is writing to the network, the process can sporadically crash due to a race condition. ([MCOL-5264](https://jira.mariadb.org/browse/MCOL-5264))

### Can result in unexpected behavior

* When the primary node is restarted, CMAPI and MaxScale sometimes choose different nodes to be the primary node. ([MCOL-5293](https://jira.mariadb.org/browse/MCOL-5293), [MCOL-5306](https://jira.mariadb.org/browse/MCOL-5306))
  * In previous releases, after the primary node was restarted, CMAPI would continue using the old primary server, but MaxScale would failover to a new primary server. If a user tried to select data from the new primary node, the operation could fail with the following error until the node is restarted:

```
ERROR 1815 (HY000): Internal error: DBRM is not responding. Cannot accept queries
```

**Additionally, the new primary node could write messages like the following to ColumnStore's debug.log file:**

```
NODE_NAME controllernode[409]: 58.561877 |0|0|0| E 29 CAL0000: DBRM: error: SessionManager::getSystemState() failed (network)   %%10%%
NODE_NAME messagequeue[409]: 59.588469 |0|0|0| E 31 CAL0000: messageqcpp::hostnameResolver Name or service not known            %%10%%
NODE_NAME messagequeue[409]: 01.642554 |0|0|0| E 31 CAL0000: messageqcpp::hostnameResolver Name or service not known            %%10%%
```

**Starting with this release, after the primary node is restarted, both CMAPI and MaxScale should failover to the same primary server.**

* When a CTE contains a query that joins an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table and a [ColumnStore](../) table, if the CTE results contain a [TIMESTAMP column](broken-reference), the column can sometimes be returned as a zero-date (which is 0000-00-00 00:00:00). ([MCOL-5311](https://jira.mariadb.org/browse/MCOL-5311))
* When a [VARCHAR column](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/varchar) is NULL and is cast to INT, the conversion would fail, and PrimProc would excessively write log messages to its systemd journal. ([MCOL-5346](https://jira.mariadb.org/browse/MCOL-5346))
  * In previous releases, the systemd journal for PrimProc could contain many messages like the following:

```
error in int conversion from ''
```

**Starting with this release, PrimProc no longer writes those log messages to its systemd journal.**

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 22.08.7 is provided for:

* CentOS 7 (x86\_64)
* Debian 11 (x86\_64, ARM64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)
* Ubuntu 22.04 (x86\_64, ARM64)

## Installation Instructions

* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.6 ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[and MariaDB Enterprise ColumnStore 23.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 23.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[ and MariaDB Enterprise ColumnStore 23.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore 23.10 with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[ and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 23.10 with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)

## Upgrade Instructions

* Upgrade Multi-Node MariaDB Enterprise ColumnStore from 6 to 23.10
* [Major Release Upgrades for MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/columnstore-release-notes/README.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
