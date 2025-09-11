# Release Notes for Cluster Management API 6.4.1

Cluster Management API (CMAPI) 6.4.1 is a maintenance release of CMAPI. CMAPI is a REST API for administering [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) in multi-node topologies.

Cluster Management API 6.4.1 was released on 2022-07-12. This release is of General Availability (GA) maturity.

CMAPI 6.4.1 is compatible with MariaDB Enterprise ColumnStore 6. CMAPI 6.4.1 was first released with [MariaDB Enterprise ColumnStore 6.4.1.](../old-releases/mariadb-columnstore-6-release-notes/mariadb-columnstore-6-4-1-release-notes.md)

## Notable Changes

* Failover can now be disabled in the CMAPI configuration file. ([MCOL-4939](https://jira.mariadb.org/browse/MCOL-4939))
  * The `auto_failover` option can be set to `True` or `False` in the `[application]` section:

```
[application]
auto_failover = False
```

* The default value of the `auto_failover` option is `True`.
* The `auto_failover` option should be set to `False` when [non-shared local storage](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview#storage-architecture) is used.
* The format and logic of CMAPI logging has been improved. ([MCOL-4907](https://jira.mariadb.org/browse/MCOL-4907))
* Transaction IDs are included more consistently in exception messages. ([MCOL-4921](https://jira.mariadb.org/browse/MCOL-4921))

## Issues Fixed

* The status endpoint returns the "`dbroots`" attribute as an empty array even when ColumnStore is working. ([MCOL-4762](https://jira.mariadb.org/browse/MCOL-4762))
* When CMAPI tries to verify a node's hostname, the verification can fail if the short hostname was provided, but the fully qualified domain name (FQDN) is in `/etc/hosts`. ([MCOL-4865](https://jira.mariadb.org/browse/MCOL-4865))

## Platforms

In alignment to the MariaDB Corporation Engineering Policy, CMAPI 6.4.1 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64)
* Rocky Linux 8 (x86\_64)
* Ubuntu 18.04 (x86\_64)
* Ubuntu 20.04 (x86\_64)

## Installation Instructions

* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore 6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[10](broken-reference)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and MariaDB Enterprise ColumnStore 6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
