# Release Notes for Cluster Management API 1.6.0

Cluster Management API (CMAPI) 1.6.0 is a maintenance release of [CMAPI](./). CMAPI is a REST API for administering [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) in multi-node topologies.

Cluster Management API 1.6.0 was released on 2021-12-13. This release is of General Availability (GA) maturity.

CMAPI 1.6.0 is compatible with MariaDB Enterprise ColumnStore 5.6 and 6. CMAPI 1.6.0 was first released with [MariaDB Enterprise ColumnStore 5.6.3](../old-releases/mariadb-columnstore-5-6-release-notes/mariadb-columnstore-5-6-3-release-notes.md) and [MariaDB Enterprise ColumnStore 6.2.2.](../old-releases/mariadb-columnstore-6-release-notes/mariadb-columnstore-6-2-2-release-notes.md)

## Notable Changes

* CMAPI now disables the [ExeMgr process](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/mariadb-enterprise-columnstore-query-evaluation#exemgr-process-facility) on replica nodes to avoid unnecessary CPU usage. ([MCOL-4860](https://jira.mariadb.org/browse/MCOL-4860))
* To avoid conflicts between systemd and CMAPI, the mariadb-columnstore systemd unit is disabled when CMAPI is installed and re-enabled when CMAPI is uninstalled. ([MCOL-4938](https://jira.mariadb.org/browse/MCOL-4938))
* Some CMAPI Log messages have been clarified. ([MCOL-4851](https://jira.mariadb.org/browse/MCOL-4851))
* CMAPI properly applies configuration changes to multiple nodes. ([MCOL-4851](https://jira.mariadb.org/browse/MCOL-4851))
* Behavior for DBRM socket send and receive has been fixed. ([MCOL-4851](https://jira.mariadb.org/browse/MCOL-4851))
* The CMAPI configuration file is now automatically created by default if it is not found. ([MCOL-4851](https://jira.mariadb.org/browse/MCOL-4851))

## Platforms

In alignment with the MariaDB Corporation Engineering Policy, CMAPI 1.6.0 is provided for:

* CentOS 7 (x86\_64)
* Debian 9 (x86\_64)
* Debian 10 (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64)
* Ubuntu 18.04 (x86\_64)
* Ubuntu 20.04 (x86\_64)

## Installation Instructions

* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore 6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[10](broken-reference)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and MariaDB Enterprise ColumnStore 6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
