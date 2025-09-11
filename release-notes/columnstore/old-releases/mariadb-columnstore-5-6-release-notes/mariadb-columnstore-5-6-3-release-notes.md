# MariaDB ColumnStore 5.6.3 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 5.6.3 is a maintenance release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md). MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server. This is the seventh release in the Enterprise ColumnStore 5 series.

MariaDB Enterprise ColumnStore 5.6.3 was released on 2021-12-13. This release is of General Availability (GA) maturity.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.5.13-9.

## Notable Changes

* CMAPI 1.6 is now included
  * CMAPI is a REST API for administering MariaDB Enterprise ColumnStore in multi-node topologies.
  * For additional information, see "Release Notes for CMAPI 1.6".
* ColumnStore now supports compression for temporary files used for disk-based aggregations ([MCOL-4829](https://jira.mariadb.org/browse/MCOL-4829))
  * When disk-based aggregations are enabled, the temporary files use snappy compression by default.

## Issues Fixed

### Can result in a hang or crash

* Replica nodes crash and cannot restart after cpimport is executed. ([MCOL-4805](https://jira.mariadb.org/browse/MCOL-4805))
* Server crashes when a NOT IN(..) subquery contains an IS NULL comparison in an OR predicate. ([MCOL-4642](https://jira.mariadb.org/browse/MCOL-4642))

### Can result in unexpected behavior

* The CMAPI shell aliases fail when the API key contains a = character. ([MCOL-4773](https://jira.mariadb.org/browse/MCOL-4773))

## Platforms

In alignment with the [enterprise lifecycle](../../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 5.6.3 is provided for:

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
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore 5 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[ and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 5 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)

## Upgrade Instructions

* Major Release Upgrades for MariaDB Enterprise ColumnStore.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
