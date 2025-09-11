# MariaDB ColumnStore 5.6.5 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 5.6.5 is a maintenance release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md). MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server. This is the eighth release in the Enterprise ColumnStore 5 series.

MariaDB Enterprise ColumnStore 5.6.5 was released on 2022-02-14. This release is of General Availability (GA) maturity.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.5.13-9 and MariaDB Enterprise Server 10.5.15-10.

## Notable Changes

* CMAPI 1.6.2 was originally included
* CMAPI 1.6.3 is now included
* CMAPI is a REST API for administering MariaDB Enterprise ColumnStore in multi-node topologies.

For additional information, see "Release Notes for CMAPI 1.6.2" and "Release Notes for CMAPI 1.6.3".

## Issues Fixed

* Related to performance
* When performing a bulk data load, performance can be negatively impacted by slow extent map lookups. ([MCOL-4912](https://jira.mariadb.org/browse/MCOL-4912))

## Platforms

In alignment with the [enterprise lifecycle](../../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 5.6.5 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64)
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
