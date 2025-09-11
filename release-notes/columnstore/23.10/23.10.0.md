# MariaDB ColumnStore 23.10.0 Release Notes

## Overview

MariaDB Enterprise ColumnStore 23.10.0 is a feature release of MariaDB Enterprise ColumnStore. MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server.

MariaDB Enterprise ColumnStore 23.10.0 was released on 2023-10-11. This release is of General Availability (GA) maturity. MariaDB Enterprise ColumnStore 23.10.0 is the first GA release in the 23.10 series.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.15-10.

The changes listed here are relative to MariaDB Enterprise ColumnStore 23.02.4.

## Notable Changes

* Improved compatibility with InnoDB behavior when performing a WHERE clause with NULL comparison. ([MCOL-271](https://jira.mariadb.org/browse/MCOL-271))
* The default character set and collation have changed.
  * In previous releases, latin1 is the default character set. latin1 uses 1 byte per character.
  * Starting with this release, utf8 (utf8mb3) is the default character set. utf8mb3 uses 3 bytes per character.
  * If an existing table schema contains column types whose byte width now exceed the maximum byte width for that column type, dropping and creating the table with the new version without specifying CHARSET=latin1, will fail. Users who need latin1 character set should specify CHARSET=latin1 when creating tables (CREATE TABLE).\
    For example, create table t1 (a VARCHAR(8000))engine=columnstore; in the new version using utf8mb3 as the default CHARSET will fail, because the maximum allowable character length will be 2666=(8000/3). So if the user wants to use the existing table schema, latin1 should be specified as the CHARSET either at the column-level (for example, create table t1 (a VARCHAR(8000) charset 'latin1')engine=columnstore; or at the table-level in the DDL, for example, create table t1 (a VARCHAR(8000))engine=columnstore default charset=latin1;
* mcs cluster commands support ColumnStore cluster management operations. ([MCOL-4848](https://jira.mariadb.org/browse/MCOL-4848))
  * mcs cluster status - get MCS cluster status
  * mcs cluster stop - stop MCS cluster
  * mcs cluster start - start MCS cluster
  * mcs cluster restart - restart MCS cluster
  * mcs cluster node add –-node \<hostname\IP\FQDN> - add node to MCS cluster. The –-node argument can be used multiple times in one command.
  * mcs cluster node remove –-node \<hostname\IP\FQDN> - remove node from MCS cluster. The –-node argument can be used multiple times in one command.
  * mcs cluster set mode –-mode - set MCS cluster mode. Accepted values are readonly and readwrite
  * mcs cluster set api-key –-key \<api\_key> - set MCS cluster API management key
  * mcs cluster –-help - outputs help on each command

Some commands have one or multiple optional arguments, to see optional argument values, use the --help argument after any command, for example:

```
mcs cluster node remove --help
```

* Collation information is available to the cpimport utility through the system catalog. ([MCOL-5005](https://jira.mariadb.org/browse/MCOL-5005))
* cpimport is character set aware. ([MCOL-4931](https://jira.mariadb.org/browse/MCOL-4931))
* Improved Disk Join step to handle corner cases for large data. ([MCOL-5477](https://jira.mariadb.org/browse/MCOL-5477))
* The columnstore.cnf has been cleaned up and updated. Unused code has been deleted. Certain server settings related to ColumnStore performance that may differ than the server's own defaults have been added, for example, character\_set\_server and collation\_server. ([MCOL-5519](https://jira.mariadb.org/browse/MCOL-5519))

## Issues Fixed

### Can result in unexpected behavior

* After a DML failure, the table lock remains. ([MCOL-4988](https://jira.mariadb.org/browse/MCOL-4988))
* After using ALTER TABLE to add a new AUTOINCREMENT column or to change a column to AUTOINCREMENT, callastinsertid() shows incorrect autoincrement value. ([MCOL-5572](https://jira.mariadb.org/browse/MCOL-5572))
* Trailing spaces behave differently in ColumnStore than in InnoDB causing unexpected results. ([MCOL-4403](https://jira.mariadb.org/browse/MCOL-4403))
* With a query containing a 3 table JOIN, the wrong result can be returned. ([MCOL-5539](https://jira.mariadb.org/browse/MCOL-5539))
* With queries containing a JOIN, a bad result set can be produced. ([MCOL-5522](https://jira.mariadb.org/browse/MCOL-5522))
* After switching JOIN order, the aggregated count on left join result is incorrect. ([MCOL-5543](https://jira.mariadb.org/browse/MCOL-5543))
* After installation or service restart, permissions for the /dev/shm directory are incorrect. ([MCOL-5535](https://jira.mariadb.org/browse/MCOL-5535))

## Interface Changes

* columnstore\_diskjoin\_force\_run system variable added
* columnstore\_diskjoin\_max\_partition\_tree\_depth system variable added
* columnstore\_max\_allowed\_in\_values system variable added
* columnstore\_max\_pm\_join\_result\_count system variable added
* mariadbd --columnstore-diskjoin-force-run command-line option added
* mariadbd --columnstore-diskjoin-max-partition-tree-depth command-line option added
* mariadbd --columnstore-max-allowed-in-values command-line option added
* mariadbd --columnstore-max-pm-join-result-count command-line option added

## Default Values Changed

* character\_set\_client changed from latin1 to utf8mb3
* character\_set\_connection changed from latin1 to utf8mb3
* character\_set\_database changed from latin1 to utf8mb3
* character\_set\_results changed from latin1 to utf8mb3
* character\_set\_server changed from latin1 to utf8mb3
* collation\_connection changed from latin1\_swedish\_ci to utf8mb3\_general\_ci
* collation\_database changed from latin1\_swedish\_ci to utf8mb3\_general\_ci
* collation\_server changed from latin1\_swedish\_ci to utf8mb3\_general\_ci

If an existing table schema contains column types whose byte width now exceed the maximum byte width for that column type, dropping and creating the table with the new version without specifying CHARSET=latin1, will fail. Users should specify CHARSET=latin1 in CREATE TABLE statements.

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 23.10.0 is provided for:

* CentOS 7 (x86\_64)
* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)
* Ubuntu 22.04 (x86\_64, ARM64)

## Installation Instructions

* [ColumnStore Object Storage Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[10](broken-reference)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[10](broken-reference)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[10](broken-reference)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore 23.02 with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[10](broken-reference)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 23.02 with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)[10](broken-reference)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)

## Upgrade Instructions

* Upgrade Multi-Node MariaDB Enterprise ColumnStore from 6 to 23.10
* [Major Release Upgrades for MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/columnstore-release-notes/README.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
