# Release Notes for Cluster Management API 1.6.2

Cluster Management API (CMAPI) 1.6.2 is a maintenance release of CMAPI. CMAPI is a REST API for administering [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) in multi-node topologies.

Cluster Management API 1.6.2 was released on 2022-02-23. This release is of General Availability (GA) maturity.

CMAPI 1.6.2 is compatible with MariaDB Enterprise ColumnStore 5.6 and 6. CMAPI 1.6.2 was first released with [MariaDB Enterprise ColumnStore 5.6.5](../old-releases/mariadb-columnstore-5-6-release-notes/mariadb-columnstore-5-6-5-release-notes.md) and [MariaDB Enterprise ColumnStore 6.2.3.](../old-releases/mariadb-columnstore-6-release-notes/mariadb-columnstore-6-2-3-release-notes.md)

## Notable Changes

* Compatibility added for MariaDB ColumnStore 6.2.3. ([MCOL-4954](https://jira.mariadb.org/browse/MCOL-4954))
* Compatibility added for Enterprise ColumnStore 6.2.3 cross engine join encrypted passwords. ([MCOL-4978](https://jira.mariadb.org/browse/MCOL-4978))
* Added support for using a custom port for cross engine join support. ([MCOL-4898](https://jira.mariadb.org/browse/MCOL-4898))

## Issues Fixed

* During upgrade CMAPI configuration information is lost. Customer data is not impacted. ([MCOL-4979](https://jira.mariadb.org/browse/MCOL-4979))
* `mcsStatus` incorrectly returns `"cluster_mode": null`. This is a cosmetic issue that does not affect operation. ([MCOL-4973](https://jira.mariadb.org/browse/MCOL-4973))

## Platforms

In alignment to the MariaDB Corporation Engineering Policy, CMAPI 1.6.2 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64)
* Ubuntu 18.04 (x86\_64)
* Ubuntu 20.04 (x86\_64)

## Installation Instructions

* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore 6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[10](broken-reference)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and MariaDB Enterprise ColumnStore 6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
