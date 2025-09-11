# Release Notes for Cluster Management API 22.08.1

Cluster Management API (CMAPI) 22.08.1 is a maintenance release of CMAPI. CMAPI is a REST API for administering [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) in multi-node topologies.

Cluster Management API 22.08.1 was released on 2022-09-12. This release is of General Availability (GA) maturity.

CMAPI 22.08.1 is compatible with MariaDB Enterprise ColumnStore 22.08. CMAPI 22.08.1 was first released with [MariaDB Enterprise ColumnStore 22.08.1.](../22.08/22.08.1.md)

## Notable Changes

* CMAPI configures ColumnStore to allow read queries to be executed on any node. ([MCOL-4770](https://jira.mariadb.org/browse/MCOL-4770))
  * In previous releases, CMAPI only added an `ExeMgr` section for the primary node to `Columnstore.xml`.
  * Starting with this release, CMAPI adds an `ExeMgr` section for every node to `Columnstore.xml`, which means that any node can execute read queries.
* Since Enterprise ColumnStore 22.08 merges the `ExeMgr` process into the PrimProc process, CMAPI no longer tries to start ExeMgr on a node when the binary is not present. ([MCOL-5138](https://jira.mariadb.org/browse/MCOL-5138))
* Some redundant log messages have been removed from the CMAPI log. ([MCOL-5157](https://jira.mariadb.org/browse/MCOL-5157))

## Platforms

In alignment to the MariaDB Corporation Engineering Policy, CMAPI 22.08.1 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64, ARM64)
* Debian 11 (x86\_64, ARM64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)
* Ubuntu 22.04 (x86\_64, ARM64)

## Installation Instructions

* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore 6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[10](broken-reference)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and MariaDB Enterprise ColumnStore 6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
