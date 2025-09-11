# MariaDB ColumnStore 22.08.1 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 22.08.1 is a maintenance release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) . MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server. This is the first release in the Enterprise ColumnStore 22.08 series.

MariaDB Enterprise ColumnStore 22.08.1 was released on 2022-09-12. This release is of General Availability (GA) maturity.

MariaDB Enterprise ColumnStore 22.08 replaces MariaDB Enterprise ColumnStore 6 in MariaDB Enterprise Server 10.6.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.9-5.

This release has been withdrawn. Users of MariaDB Enterprise ColumnStore 22.08.1 should upgrade to MariaDB Enterprise ColumnStore 22.08.3.

## Notable Changes

### JOINs

* Support has been added for JOINs with an ON clause that reference tables that are not involved in the join. ([MCOL-5167](https://jira.mariadb.org/browse/MCOL-5167))
* Support has been added for circular outer JOINs. ([MCOL-4699](https://jira.mariadb.org/browse/MCOL-4699))
* Support has been added for complex JOINs in views. ([MCOL-5061](https://jira.mariadb.org/browse/MCOL-5061), [MCOL-4902](https://jira.mariadb.org/browse/MCOL-4902))
* Support has been added for combining outer JOINs and IS NULL filters. ([MCOL-4715](https://jira.mariadb.org/browse/MCOL-4715))

### Query Performance

* In single-node ColumnStore, query performance has been improved by removing a network hop. ([MCOL-5166](https://jira.mariadb.org/browse/MCOL-5166))
* Performance has been enhanced for queries that filter on numbers. ([MCOL-5140](https://jira.mariadb.org/browse/MCOL-5140), [MCOL-4995](https://jira.mariadb.org/browse/MCOL-4995))
* Performance has been enhanced for DELETE queries. ([MCOL-5021](https://jira.mariadb.org/browse/MCOL-5021))

### Functions

* Support for CHAR and VARCHAR have been added for the MODA() function. ([MCOL-5161](https://jira.mariadb.org/browse/MCOL-5161))
* Distributed implementations of most JSON functions have been added to ColumnStore. ([MCOL-785](https://jira.mariadb.org/browse/MCOL-785))
  * This feature does not include JSON\_ARRAYAGG, JSON\_OBJECTAGG, or JSON\_TABLE.
* ColumnStore's functions that use the cal prefix have been changed to use the mcs prefix. ([MCOL-4984](https://jira.mariadb.org/browse/MCOL-4984))

### Tooling

* ColumnStore now includes Cluster Management API (CMAPI) 22.08.1.
* Some internal improvements have been made to the mcsRebuildEM utility. ([MCOL-5172](https://jira.mariadb.org/browse/MCOL-5172))

### Operating Systems

* Operating system compatibility has changed, as designated in MariaDB Engineering Policy, including:
  * Support for Debian 11, Red Hat Enterprise Linux 9, Rocky Linux 9, and Ubuntu 22.04 have been added.
  * Support for Debian 9, Debian 10, and Ubuntu 18.04 have been removed.

### CPU Compatibility

* When ColumnStore is installed and started, ColumnStore's binaries check the system's CPU to confirm that the CPU supports the SIMD instructions required by ColumnStore. ([MCOL-5180](https://jira.mariadb.org/browse/MCOL-5180))
  * On x86\_64, ColumnStore requires SSE4.2.
  * On ARM64, ColumnStore requires NEON.
  * If the ColumnStore installation scripts determine that the required SIMD instructions are not supported, the following error is raised:

```
error: this machine CPU lacks of support for Intel SSE4.2 or ARM Advanced SIMD instructions. Columnstore requires one of this instruction sets, installation aborted
```

**If the ColumnStore binaries are started and determine that the required SIMD instructions are not supported, the following error is raised:**

```
Unsupported CPU architecture. ARM Advanced SIMD or x86_64 SSE4.2 required; aborting.
```

### Internal Processes

* Internal stability improvements have been made to the processes that write data. ([MCOL-5163](https://jira.mariadb.org/browse/MCOL-5163))
  * The WriteEngineServer, DMLProc, and DDLProc processes have been improved.
* PrimProc thread pool has been changed to use a fair scheduler. ([MCOL-5044](https://jira.mariadb.org/browse/MCOL-5044))
* The ExeMgr process has been merged with the PrimProc process. ([MCOL-5001](https://jira.mariadb.org/browse/MCOL-5001), [MCOL-5109](https://jira.mariadb.org/browse/MCOL-5109))

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 22.08.1 is provided for:

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
