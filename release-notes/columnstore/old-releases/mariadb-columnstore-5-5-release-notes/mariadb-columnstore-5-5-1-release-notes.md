# MariaDB ColumnStore 5.5.1 Release Notes

## Overview

MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server. This is the third release in the Enterprise ColumnStore 5 series.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.5.8-5.

This release is of General Availability (GA) maturity.

MariaDB Enterprise ColumnStore 5.5.1 was released on 2020-12-14.

* Documentation

## Notable Changes

* ColumnStore VARCHAR was sized in bytes, which required customers with multi-byte data to account for the byte variance within their capacity calculations and column definitions. VARCHAR is now sized by characters (which may be multi-byte) in alignment to the behavior of InnoDB and as required by SQL standard (ISO/IEC 9075:2016 feature E021 - Character string types). ([MCOL-2000](https://jira.mariadb.org/browse/MCOL-2000))
* Non-equality comparison operators previously produced storage engine-specific results with NOPAD collations. This behavior now aligns to the behavior of InnoDB. ([MCOL-4417](https://jira.mariadb.org/browse/MCOL-4417))
* Added ENCODE() and DECODE() function support. ([MCOL-4323](https://jira.mariadb.org/browse/MCOL-4323))
* ColumnStore now respects case-insensitive comparison during JOIN when called for by the specified collation. ([MCOL-495](https://jira.mariadb.org/browse/MCOL-495), [MCOL-4064](https://jira.mariadb.org/browse/MCOL-4064))
* Enhanced performance of multi-node ColumnStore startup. ([MCOL-4337](https://jira.mariadb.org/browse/MCOL-4337))

## Issues Fixed

### Can result in a hang or crash

* Possible crash in mariadbd when calling stored procedures in the columnstore\_info database. ([MCOL-4105](https://jira.mariadb.org/browse/MCOL-4105))
* INSERT .. SELECT hangs on cpimport when MariaDB Enterprise ColumnStore is installed in a non-default path. ([MCOL-4425](https://jira.mariadb.org/browse/MCOL-4425))

### Can result in unexpected behavior

* Incorrect error message shown when using unsupported JSON functions. ([MCOL-4108](https://jira.mariadb.org/browse/MCOL-4108))
* Equality does not respect the NOPAD collation attribute. ([MCOL-4388](https://jira.mariadb.org/browse/MCOL-4388))
* ROUND() function returns incorrect answer for DATE data type. ([MCOL-4255](https://jira.mariadb.org/browse/MCOL-4255), [MCOL-4281](https://jira.mariadb.org/browse/MCOL-4281))
* calgetshowpartitions fails if MariaDB Enterprise Server started before MariaDB Enterprise ColumnStore. ([MCOL-4397](https://jira.mariadb.org/browse/MCOL-4397))

### Related to install and upgrade

* mcs-loadbrm and mcs-savebrm have hard coded paths to load\_brm and save\_brm ([MCOL-4295](https://jira.mariadb.org/browse/MCOL-4295))
* In-place upgrade from 1.5 to 5.5 failed due to DEB package conflicts. ([MCOL-4166](https://jira.mariadb.org/browse/MCOL-4166))
* A configuration file x-columnstore.cnf previously existed during Beta and Gamma releases of ColumnStore. This file has been removed as it is no longer required. ([MCOL-4155](https://jira.mariadb.org/browse/MCOL-4155))

## Platforms

In alignment with the [enterprise lifecycle](../../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 5.5.1 is provided for:

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
* [Single-Node Enterprise ColumnStore 5 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[ and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 5 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)

## Upgrade Instructions

* [Major Release Upgrades for MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/columnstore-release-notes/README.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
