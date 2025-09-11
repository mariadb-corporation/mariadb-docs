# MariaDB ColumnStore 23.02.8 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/columnstore/mariadb-columnstore-23-02-release-notes/MariaDB_Enterprise_ColumnStore/README.md) 23.02.8 is a maintenance release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/columnstore/mariadb-columnstore-23-02-release-notes/MariaDB_Enterprise_ColumnStore/README.md). MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server.

MariaDB Enterprise ColumnStore 23.02.8 was released on 2024-02-16. This release is of General Availability (GA) maturity. MariaDB Enterprise ColumnStore 23.02.8 is the fourth GA release in the 23.02 series.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.14-9.

Users of earlier MariaDB Enterprise ColumnStore releases are encouraged to upgrade.

## Issues Fixed

### Can result in data loss

* Shmem segment remap causes SEGV in ExtentMapIndexImpl::find ([MCOL-5559](https://jira.mariadb.org/browse/MCOL-5559))
* S3 Cluster Left Read-Only | BRM lock state and DBRMSnapshotInterval ([MCOL-5623](https://jira.mariadb.org/browse/MCOL-5623))
* PrimProc Crash | libthreadpool.so | boost10shared\_ptr ([MCOL-5645](https://jira.mariadb.org/browse/MCOL-5645))

### Can result in a hang or crash

* CMAPI python3 binary crash ([MCOL-5650](https://jira.mariadb.org/browse/MCOL-5650))
* `FairThreadScheduler::sendErrorMsg and BPPSeeder::sendErrorMsg` crash PP trying to send to a nullptr sock ([MCOL-5636](https://jira.mariadb.org/browse/MCOL-5636))

### Can result in unexpected behavior

* Continuous workload triggers unknown primitive cmd message in PP log ([MCOL-5637](https://jira.mariadb.org/browse/MCOL-5637))

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 23.02.8 is provided for:

* Debian 11 (x86\_64, ARM64)
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
* [Major Release Upgrades for MariaDB Enterprise ColumnStore](../)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
