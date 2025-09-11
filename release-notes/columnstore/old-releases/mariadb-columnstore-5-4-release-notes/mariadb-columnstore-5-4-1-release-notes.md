# MariaDB ColumnStore 5.4.1 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a columnar storage engine included with MariaDB Enterprise Server. This is the first release in the [Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 5 series, which succeeds Enterprise ColumnStore 1.5.3.

This release is focused on architectural change, product quality, and improved alignment to MariaDB Enterprise Server.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.5.6-4.

This release is of General Availability (GA) maturity.

[MariaDB Enterprise ColumnStore](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview#mariadb-enterprise-columnstore) 5.4.1 was released on 2020-10-20.

* Documentation

## Notable Changes

### Multi-Node Changes

* Multi-node Enterprise ColumnStore 5.4.1 requires MaxScale 2.5.
* Multi-node Enterprise ColumnStore 5.4.1 requires shared storage, such as GlusterFS, EFS, and NFS. It also optionally supports S3-compatible storage for data, but it still requires shared storage for metadata.
* The CMAPI (Cluster Management API) has been updated. Multi-node Enterprise ColumnStore 5.4.1 uses CMAPI 1.1, which still uses version 0.4.0 of the REST API. ([MCOL-3909](https://jira.mariadb.org/browse/MCOL-3909))

### Security Changes

* Support for IAM roles for Amazon S3. ([MCOL-3976](https://jira.mariadb.org/browse/MCOL-3976))
* Support for ColumnStore running as non-root user. ([MCOL-4012](https://jira.mariadb.org/browse/MCOL-4012))

### Client Changes

* Support for Power BI Direct Query Adapter. ([MCOL-3935](https://jira.mariadb.org/browse/MCOL-3935))

## Issues Fixed

* Changed default configuration for memory usage, blocks, and set table names. ([MCOL-4252](https://jira.mariadb.org/browse/MCOL-4252))
* Prepared Statements causing Signal 11. ([MCOL-4282](https://jira.mariadb.org/browse/MCOL-4282))
* Running COUNT() when the sql\_select\_limit system variable is set may leave the table badly ([MCOL-4278](https://jira.mariadb.org/browse/MCOL-4278))
* New segments files created during bulk insertion with cpimport belong to root ([MCOL-4328](https://jira.mariadb.org/browse/MCOL-4328))
* Join operations return errors when using upper-case table names. ([MCOL-4290](https://jira.mariadb.org/browse/MCOL-4290))
* Permissions issue in /tmp/columnstore\_tmp\_files ([MCOL-4265](https://jira.mariadb.org/browse/MCOL-4265))
* RENAME TABLE leaving table unusable. ([MCOL-3701](https://jira.mariadb.org/browse/MCOL-3701))
* Errors returned when using upper-case database names. ([MCOL-4144](https://jira.mariadb.org/browse/MCOL-4144))
* Server crashing when running queries where no default schema was provided. ([MCOL-3464](https://jira.mariadb.org/browse/MCOL-3464))
* Regression in subqueries. ([MCOL-4179](https://jira.mariadb.org/browse/MCOL-4179))
* CMAPI issues configuring multi-node ColumnStore deployment. ([MCOL-4226](https://jira.mariadb.org/browse/MCOL-4226))
* Changed default common\_prefix\_depth for S3 to accommodate new paths. ([MCOL-3651](https://jira.mariadb.org/browse/MCOL-3651))
* Join operations failing on views. ([MCOL-3814](https://jira.mariadb.org/browse/MCOL-3814))
* Crash/assertion failure after "RWLock failed to attach to the InfiniDB-shm-00020000 shared mem segment, got Permission denied" ([MCOL-4283](https://jira.mariadb.org/browse/MCOL-4283))
* SUM() and AVG() functions in subqueries returning 0. ([MCOL-4247](https://jira.mariadb.org/browse/MCOL-4247))
* CEILING() function returning wrong answer for datetimes. ([MCOL-4236](https://jira.mariadb.org/browse/MCOL-4236))
* CMAPI Server not gracefully handling first nodes with unresolved names in /etc/hostname ([MCOL-4223](https://jira.mariadb.org/browse/MCOL-4223))
* Case sensitivity in LOCATE(), INSTR(), and FIND\_IN\_SET() functions. ([MCOL-4100](https://jira.mariadb.org/browse/MCOL-4100))
* INSERT() function not inserting. ([MCOL-4099](https://jira.mariadb.org/browse/MCOL-4099))
* SQL syntax error when uninstalling Columnstore plugin package. ([MCOL-4087](https://jira.mariadb.org/browse/MCOL-4087))
* Replication of InnoDB into ColumnStore ends in SEGV in plugin. ([MCOL-4181](https://jira.mariadb.org/browse/MCOL-4181))
* Unclear error message when postConfigure fails to access online S3 storage. ([MCOL-3494](https://jira.mariadb.org/browse/MCOL-3494))
* Integrate with the cluster management code. ([MCOL-4055](https://jira.mariadb.org/browse/MCOL-4055))
* Column not found in info map when querying views. ([MCOL-3827](https://jira.mariadb.org/browse/MCOL-3827))
* Query failures on UPDATE statements to InnoDB tables when WHERE clause includes a sub-query on a ColumnStore table. ([MCOL-4264](https://jira.mariadb.org/browse/MCOL-4264))
* UPDATE... SET statements not updating when using another table. ([MCOL-4303](https://jira.mariadb.org/browse/MCOL-4303))
* Multi-node not working after executing stop and start commands. ([MCOL-4227](https://jira.mariadb.org/browse/MCOL-4227))
* Custom cross-engine join user unable to connect. ([MCOL-4322](https://jira.mariadb.org/browse/MCOL-4322))
* Hangs when requesting data from ColumnStore extents or files. ([MCOL-4330](https://jira.mariadb.org/browse/MCOL-4330))
* columnstore-post-install and mariadb-columnstore-start.sh fixed to use absolute paths. ([MCOL-4335](https://jira.mariadb.org/browse/MCOL-4335))
* Procedures hanging when using ColumnStore tables. ([MCOL-4334](https://jira.mariadb.org/browse/MCOL-4334))
* CMAPI returning error messages when using custom replication user credentials. ([MCOL-4289](https://jira.mariadb.org/browse/MCOL-4289))
* CMAP incorrectly sed parsing & character for CMAPI key. ([MCOL-4297](https://jira.mariadb.org/browse/MCOL-4297))
* Database user access unrestricted by IP addresses. ([MCOL-4293](https://jira.mariadb.org/browse/MCOL-4293))
* Stored procedures failing for Information Schema tables. ([MCOL-4332](https://jira.mariadb.org/browse/MCOL-4332))

## Interface Changes

* [columnstore\_cache\_flush\_threshold](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) system variable added
* [columnstore\_cache\_inserts](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) system variable added
* [columnstore\_select\_handler\_in\_stored\_procedures](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) system variable added
* [mariadbd --columnstore-cache-flush-threshold](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) command-line option added
* [mariadbd --columnstore-cache-inserts](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) command-line option added
* [mariadbd --columnstore-select-handler-in-stored-procedures](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) command-line option added

## Platforms

In alignment with the [enterprise lifecycle](../../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 5.4.1 is provided for:

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
* [Single-Node Enterprise ColumnStore 23.10 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[ and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 23.10 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)

## Upgrade Instructions

* [Major Release Upgrades for MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/columnstore-release-notes/README.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
