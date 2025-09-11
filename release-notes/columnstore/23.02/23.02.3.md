# MariaDB ColumnStore 23.02.3 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 23.02.3 is a maintenance release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md). MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server.

MariaDB Enterprise ColumnStore 23.02.3 was released on 2023-05-03. This release is of General Availability (GA) maturity. MariaDB Enterprise ColumnStore 23.02.3 is the third GA release in the 23.02 series.

MariaDB Enterprise ColumnStore 23.02 replaces MariaDB Enterprise ColumnStore 22.08 in MariaDB Enterprise Server 10.6.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.12-7.

Users of earlier MariaDB Enterprise ColumnStore releases are encouraged to upgrade.

## Issues Fixed

### Can result in a hang or crash

* When the GROUP\_CONCAT() function is used to produce relatively long strings, excessive memory can be used, which can cause PrimProc to crash with a segmentation fault. ([MCOL-5385](https://jira.mariadb.org/browse/MCOL-5385), [MCOL-5429](https://jira.mariadb.org/browse/MCOL-5429))
  * In previous releases, this issue can cause various types of messages to appear in the ColumnStore logs prior to the crash, such as:

```
CAL0005: ThreadPool: Caught exception during execution:  boost::thread_resource_error: Resource temporarily unavailable [generic:11]
CAL0000: TupleAggregateStep::doThreadedAggregate() caught std::bad_alloc         %%10%%
```

In previous releases, this issue can cause clients to see the following error message:

```
ERROR 1815 (HY000): Internal error: InetStreamSocket::readToMagic: Remote is closed
```

**Starting with this release, less memory should be used in this scenario.**

* When multiple ColumnStore threads or processes try to access a managed shared memory segment for the Extent Map concurrently, a read/write conflict can cause the processes to crash with a segmentation fault due to a race condition. ([MCOL-5487](https://jira.mariadb.org/browse/MCOL-5487))
  * In previous releases, cpimport, PrimProc, and DMLProc were observed to crash in this scenario.
  * Starting with this release, the internal RWLock is upgraded to a write lock when a shared memory segment remap is initiated (such as by a long running cpimport job), thus avoiding this read/write conflict.

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 23.02.3 is provided for:

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
