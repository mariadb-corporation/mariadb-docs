# MariaDB ColumnStore 6.4.1 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 6.4.1 is a maintenance release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) . MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server. This is the fifth release in the Enterprise ColumnStore 6 series.

MariaDB Enterprise ColumnStore 6.4.1 was released on 2022-07-12. This release is of General Availability (GA) maturity.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.8-4.

## Notable Changes

* ColumnStore now includes Cluster Management API (CMAPI) 6.4.1.
* ColumnStore has optimized the storage and usage of the Extent Map to improve scalability. ([MCOL-4917](https://jira.mariadb.org/browse/MCOL-4917))
  * The Extent Map is now stored as a red-black tree instead of a linear array.
  * The Extent Map's new data structure provides optimizations for many operations.
* The mcsRebuildEM utility now supports both the ColumnStore Object Storage Topology and the ColumnStore Shared Local Storage Topology. ([MCOL-5106](https://jira.mariadb.org/browse/MCOL-5106))
* The mcsRebuildEM utility now calculates the high water mark for system catalog files. ([MCOL-5131](https://jira.mariadb.org/browse/MCOL-5131))

## Issues Fixed

### Can result in a hang or crash

* ColumnStore's systemd unit files use startup and shutdown timeouts that are too low, which can lead to race conditions during startup and shutdown. ([MCOL-4775](https://jira.mariadb.org/browse/MCOL-4775), [MCOL-4867](https://jira.mariadb.org/browse/MCOL-4867), [MCOL-5105](https://jira.mariadb.org/browse/MCOL-5105))
  * The race conditions could cause the Extent Map to become corrupt.
  * The race conditions could also cause the DMLProc process to repeatedly try to rollback the same transactions in a crash loop.
* When a recursive CTE is executed with a ColumnStore table, the server crashes. ([MCOL-4778](https://jira.mariadb.org/browse/MCOL-4778))
  * Starting with this release, when a recursive CTE is executed with a ColumnStore table, the ER\_CHECK\_NOT\_IMPLEMENTED error code is raised to the client with the following message:\
    <`.`\
    `ERROR 1178 (42000): The storage engine for the table doesn't support Recursive CTE`\
    `<`>
* When a disk-based JOIN is executed, ExeMgr can crash. ([MCOL-5042](https://jira.mariadb.org/browse/MCOL-5042))

### Can result in unexpected behavior

* When testS3Connection is executed, it does not check for permission to perform the s3:ListBucket action. ([MCOL-4989](https://jira.mariadb.org/browse/MCOL-4989))
* When ColumnStore is down or starting up, the mcssystemready() function returns an inaccurate value. ([MCOL-5065](https://jira.mariadb.org/browse/MCOL-5065))

## Related to install and upgrade

* Internal installation scripts refer to legacy OAM components and can break some installations. ([MCOL-5060](https://jira.mariadb.org/browse/MCOL-5060))

## Platforms

In alignment with the [enterprise lifecycle](../../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 6.4.1 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64)
* Rocky Linux 8 (x86\_64)
* Ubuntu 18.04 (x86\_64)
* Ubuntu 20.04 (x86\_64)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
