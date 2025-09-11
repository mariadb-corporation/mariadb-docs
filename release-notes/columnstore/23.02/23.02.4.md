# MariaDB ColumnStore 23.02.4 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 23.02.4 is a maintenance release of MariaDB Enterprise ColumnStore. MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server.

MariaDB Enterprise ColumnStore 23.02.4 was released on 2023-07-03. This release is of General Availability (GA) maturity. MariaDB Enterprise ColumnStore 23.02.4 is the fourth GA release in the 23.02 series.

MariaDB Enterprise ColumnStore 23.02 replaces MariaDB Enterprise ColumnStore 22.08 in MariaDB Enterprise Server 10.6.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.14-9.

Users of earlier MariaDB Enterprise ColumnStore releases are encouraged to upgrade.

## Notable Changes

* When deploying the ColumnStore Object Storage topology, Cohesity S3 is supported as a hardware storage option by the ColumnStore S3 Storage Manager. ([MCOL-5175](https://jira.mariadb.org/browse/MCOL-5175))
* The cgroup v2 API is now supported, and values from the cgroup v1 API hierarchy are now validated. ([MCOL-5500](https://jira.mariadb.org/browse/MCOL-5500))

## Issues Fixed

### Can result in a hang or crash

* When exporting data from a ColumnStore table using SELECT .. INTO OUTFILE or adding data to a ColumnStore table from another ColumnStore table using INSERT .. SELECT, if the size of the ColumnStore table exceeds the amount of RAM on the server, the PrimProc process uses all of the available memory, which cause the out-of-memory (OOM) killer to kill the process and results in the following error: ([MCOL-5489](https://jira.mariadb.org/browse/MCOL-5489))

```
ERROR 1815 (HY000): Internal error: MCS-2004: Cannot connect to ExeMgr.
```

* When the JSON\_ARRAYAGG() function is used to produce long strings, excessive memory can be used, which can cause PrimProc to crash with a segmentation fault. ([MCOL-5491](https://jira.mariadb.org/browse/MCOL-5491))
  * In previous releases, this issue can cause various types of messages to appear in the ColumnStore logs prior to the crash, such as:

```
CAL0000: InetStreamSocket::readToMagic(): I/O error1: rc-1; poll signal interrupt ( POLLHUP POLLERR )         %%10%%
CAL0001: Table does not exist in ColumnStore.
```

**In previous releases, this issue can cause clients to see the following error message:**

```
ERROR 1815 (HY000): Internal error: InetStreamSocket::readToMagic: Remote is closed
```

**Starting with this release, less memory should be used in this scenario.**

* When a node communicates with itself over memory, the node effectively has an unlimited message queue, which causes memory usage to increase until the out-of-memory (OOM) killer kills the process. ([MCOL-5499](https://jira.mariadb.org/browse/MCOL-5499))
  * In previous releases, when a node communicated with itself over memory, the FlowControl mechanism was effectively disabled. Without FlowControl, if a slow consumer exists somewhere in the query execution pipeline, the Distributed Engine Communication (DEC) receive queue can be overloaded.
  * Starting with this release, FlowControl is enabled when a node communicates with itself over memory.

### Can result in unexpected behavior

* The EXTRACT(QUARTER FROM \<date\_value>) function can return an incorrect quarter value. ([MCOL-5068](https://jira.mariadb.org/browse/MCOL-5068), [MCOL-5503](https://jira.mariadb.org/browse/MCOL-5503))
* When executing a query that contains multiple nested SELECT statements that involve a UNION in the inner SELECT statements, an error is returned when columns with the same name are referenced by alias. ([MCOL-5357](https://jira.mariadb.org/browse/MCOL-5357))
  * In previous releases, an error is raised similar to:

```
ERROR 1815 (HY000): Internal error: MCS-3009: Unknown column '.TABLE_ALIAS.COLUMN_ALIAS'.
```

* When columnstore\_use\_import\_for\_batchinsert is enabled, the LOAD DATA INFILE statement loads values incorrectly for the MEDIUMINT, TIME, and TIMESTAMP data types. ([MCOL-5480](https://jira.mariadb.org/browse/MCOL-5480))
* When using the columnstore\_info.load\_from\_s3 stored procedure, even if the data is successfully loaded to the ColumnStore table, the procedure reports an import failure: ([MCOL-5509](https://jira.mariadb.org/browse/MCOL-5509))

```
{"success": false, "inserted": 0, "processed": 0}
```

* When using the columnstore\_info.load\_from\_s3 stored procedure, if cpimport fails, the user connection hangs until the connection times out without any error messages. ([MCOL-5510](https://jira.mariadb.org/browse/MCOL-5510))
  * Starting with this release, the following error message is raised:

```
{"error": "2023-06-19 19:12:27 (13398) ERR : Actual error row count(11) exceeds the max error rows(10) allowed for table DATABASE_NAME.TABLE_NAME [1451]\n"}
```

* When performing a join with a large table, the post-join filters are not applied. ([MCOL-5512](https://jira.mariadb.org/browse/MCOL-5512))
  * In previous releases, this could cause results to be incorrect.

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 23.02.4 is provided for:

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
