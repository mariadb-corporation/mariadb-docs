# Release Notes for Cluster Management API 22.08.2

Cluster Management API (CMAPI) 22.08.2 is a maintenance release of CMAPI. CMAPI is a REST API for administering [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) in multi-node topologies.

Cluster Management API 22.08.2 was released on 2022-11-15. This release is of General Availability (GA) maturity.

CMAPI 22.08.2 is compatible with MariaDB Enterprise ColumnStore 22.08. CMAPI 22.08.2 was first released with [MariaDB Enterprise ColumnStore 22.08.3.](../22.08/22.08.3.md)

Users of CMAPI 22.08.1 are encouraged to upgrade.

## Issues Fixed

* The cluster is not correctly reconfigured when a PM fails and recovers: ([MCOL-5286](https://jira.mariadb.org/browse/MCOL-5286))
  * DDL will fail after a PM fails.
  * Selects will fail after the PM recovers.

## Platforms

In alignment to the MariaDB Corporation Engineering Policy, CMAPI 22.08.2 is provided for:

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

* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore 6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[10](broken-reference)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and MariaDB Enterprise ColumnStore 6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
