# Release Notes for Cluster Management API 1.6.3

Cluster Management API (CMAPI) 1.6.3 is a maintenance release of CMAPI. CMAPI is a REST API for administering [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) in multi-node topologies.

Cluster Management API 1.6.3 was released on 2022-04-20. This release is of General Availability (GA) maturity.

CMAPI 1.6.3 is compatible with MariaDB Enterprise ColumnStore 5.6 and 6. CMAPI 1.6.3 was first released with [MariaDB Enterprise ColumnStore 5.6.5](../old-releases/mariadb-columnstore-5-6-release-notes/mariadb-columnstore-5-6-5-release-notes.md) and [MariaDB Enterprise ColumnStore 6.2.3.](../old-releases/mariadb-columnstore-6-release-notes/mariadb-columnstore-6-2-3-release-notes.md)

## Notable Changes

* When a node is added to the cluster using a DNS name, the node's DNS name is added to `Columnstore.xml` instead of the node's IP address. ([MCOL-4804](https://jira.mariadb.org/browse/MCOL-4804))
  * Prior to this release, when a node's IP address changed after it was added to the cluster, `Columnstore.xml` still contained the node's old IP address.
  * Starting with this release, CMAPI can adapt to changing IP addresses when the DNS name in `Columnstore.xml` resolves to the new IP address.

## Issues Fixed

After the primary server is killed and restarted, MaxScale and CMAPI could each choose different primary servers. ([MCOL-5052](https://jira.mariadb.org/browse/MCOL-5052))

## Platforms

In alignment to the MariaDB Corporation Engineering Policy, CMAPI 1.6.3 is provided for:

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
