# MariaDB ColumnStore 23.10.1 Release Notes

## Overview

MariaDB Enterprise ColumnStore 23.10.1 is a feature release of MariaDB Enterprise ColumnStore. MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server.

MariaDB Enterprise ColumnStore 23.10.1 was released on 2024-03-11. This release is of General Availability (GA) maturity. MariaDB Enterprise ColumnStore 23.10.1 is a GA release in the 23.10 series.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.17-12.

The changes listed here are relative to MariaDB Enterprise ColumnStore 23.02.4.

## Notable Changes

* Cross db table rename fails ([MCOL-4202](https://jira.mariadb.org/browse/MCOL-4202))
* Columnstore throws error when using GROUP BY on DB-Views where field name is identical in two different tables ([MCOL-5463](https://jira.mariadb.org/browse/MCOL-5463))
* GROUP BY on duplicate expressions using functions throws error "IDB-2001: ... is not in GROUP BY clause." on Columnstore ([MCOL-5476](https://jira.mariadb.org/browse/MCOL-5476))
* Support WITH ROLLUP ([MCOL-678](https://jira.mariadb.org/browse/MCOL-678))

## Issues Fixed

### Can result in data loss

* Shmem segment remap causes SEGV in ExtentMapIndexImpl::find ([MCOL-5559](https://jira.mariadb.org/browse/MCOL-5559))

### Can result in a hang or crash

* Queries stuck in MariaDB waiting for an answer from PrimProc ([MCOL-5565](https://jira.mariadb.org/browse/MCOL-5565))
* LIKE '%1%' in WHERE part never finishes ([MCOL-5599](https://jira.mariadb.org/browse/MCOL-5599))
* PrimProc goes in a loop, 100% CPU usage on a single core ([MCOL-5602](https://jira.mariadb.org/browse/MCOL-5602))
* PrimProc crashes in json\_key\_matches ([MCOL-5607](https://jira.mariadb.org/browse/MCOL-5607))
* FairThreadScheduler::sendErrorMsg and BPPSeeder::sendErrorMsg crash PP trying to send to a nullptr sock ([MCOL-5636](https://jira.mariadb.org/browse/MCOL-5636))

### Can result in unexpected behavior

* UPDATE returns wrong "Rows matched" on multi-tables ([MCOL-4740](https://jira.mariadb.org/browse/MCOL-4740))
* json data returns differently by same query ([MCOL-5350](https://jira.mariadb.org/browse/MCOL-5350))
* Columnstore query returns incorrect value instead of expected out-of-range error ([MCOL-5568](https://jira.mariadb.org/browse/MCOL-5568))
* JSON\_QUERY is stateful (may segfault on big amount of data) ([MCOL-5625](https://jira.mariadb.org/browse/MCOL-5625))
* Continuous workload triggers unknown primitive cmd message in PP log ([MCOL-5637](https://jira.mariadb.org/browse/MCOL-5637))

## Related to performance

* CPU wastes time in wait and sys because of urandom access in RowStorage ([MCOL-5472](https://jira.mariadb.org/browse/MCOL-5472))

## Related to install and upgrade

* Wrong metadata in CMAPI packages ([MCOL-5595](https://jira.mariadb.org/browse/MCOL-5595))

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 23.10.1 is provided for:

* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)
* Ubuntu 22.04 (x86\_64, ARM64)
* Ubuntu 24.04 (x86\_64, ARM64)

## Installation Instructions

* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.6 ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[and MariaDB Enterprise ColumnStore 23.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 23.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[ and MariaDB Enterprise ColumnStore 23.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore 23.10 with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[ and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 23.10 with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)

## Upgrade Instructions

* Upgrade Multi-Node MariaDB Enterprise ColumnStore from 6 to 23.10
* [Major Release Upgrades for MariaDB Enterprise ColumnStore](../)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
