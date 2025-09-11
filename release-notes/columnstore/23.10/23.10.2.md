# MariaDB ColumnStore 23.10.2 Release Notes

## Overview

MariaDB Enterprise ColumnStore 23.10.2 is a feature release of MariaDB Enterprise ColumnStore. MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server.

MariaDB Enterprise ColumnStore 23.10.2 was released on 2024-08-19. This release is of General Availability (GA) maturity. MariaDB Enterprise ColumnStore 23.10.2 is a GA release in the 23.10 series.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.18-14.

## Notable Changes

* Save EM image locally if S3 fails PUT request or avoid saving if shared memory image is damaged or empty ([MCOL-5709](https://jira.mariadb.org/browse/MCOL-5709))
* No data gets loaded into BLOB column and the value is left NULL ([MCOL-5746](https://jira.mariadb.org/browse/MCOL-5746))
* Using regexp\_substr on table with engine=columnstore results in error:`"Function 'regexp_substr' isn't supported."` ([MCOL-5328](https://jira.mariadb.org/browse/MCOL-5328))
* Interactive "mcs cluster stop" command for CMAPI ([MCOL-5594](https://jira.mariadb.org/browse/MCOL-5594))

## Issues Fixed

* ORDER BY clause if not included in the GROUP BY clause fails ([MCOL-4234](https://jira.mariadb.org/browse/MCOL-4234))
* Group By ... Order By NULL fails ([MCOL-4235](https://jira.mariadb.org/browse/MCOL-4235))
* Alter table add column leaves table unusable ([MCOL-4480](https://jira.mariadb.org/browse/MCOL-4480))
* select \* into file from (select ... group by) produces spurious error ([MCOL-4637](https://jira.mariadb.org/browse/MCOL-4637))
* MariaDB Columnstore all versions: update and inserts behave differently on 0000-00-00 00:00:00 datetime ([MCOL-5035](https://jira.mariadb.org/browse/MCOL-5035))
* Cross-Engine join at text type not supported ([MCOL-5056](https://jira.mariadb.org/browse/MCOL-5056))
* ColumnStore table does not exist after a rename ([MCOL-5197](https://jira.mariadb.org/browse/MCOL-5197))
* Using views leads to an error when an Analyzer report with a measure and a year is built. ([MCOL-5236](https://jira.mariadb.org/browse/MCOL-5236))
* Views with null-replaced timestamps yield incorrect query results ([MCOL-5237](https://jira.mariadb.org/browse/MCOL-5237))
* RAND() uses static seed of 0 ([MCOL-5492](https://jira.mariadb.org/browse/MCOL-5492))
* Resultset will be cut with setting columnstore\_um\_mem\_limit >0 ([MCOL-5689](https://jira.mariadb.org/browse/MCOL-5689))
* CS return error for intersect ([MCOL-5699](https://jira.mariadb.org/browse/MCOL-5699))
* Random columnstore error MCS-2035 with special SELECT structures ([MCOL-5704](https://jira.mariadb.org/browse/MCOL-5704))

### Can result in a hang or crash

* CMAPI: ConnectionRefusedError unhandled exception ([MCOL-5749](https://jira.mariadb.org/browse/MCOL-5749))
* Truncate table failed after PrimProc restarted ([MCOL-5352](https://jira.mariadb.org/browse/MCOL-5352))
* mcs-savebrm stores an empty EM on cluster shutdown rendering the cluster unusable ([MCOL-5405](https://jira.mariadb.org/browse/MCOL-5405))
* NULL & non-zero length string, assertion 'mStr || mLength == 0' failed ([MCOL-5597](https://jira.mariadb.org/browse/MCOL-5597))

### Can result in unexpected behavior

* Disk join step race with parallel join (more than one thread) ([MCOL-5626](https://jira.mariadb.org/browse/MCOL-5626))

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 23.10.2 is provided for:

* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)
* Ubuntu 22.04 (x86\_64, ARM64)
* Ubuntu 24.04 (x86\_64, ARM64)

## Installation Instructions

* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.6 ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[and MariaDB Enterprise ColumnStore 23.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 23.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[ and MariaDB Enterprise ColumnStore 23.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore 23.10 with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[ and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 23.10 with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)

## Upgrade Instructions

* Upgrade Multi-Node MariaDB Enterprise ColumnStore from 6 to 23.10
* [Major Release Upgrades for MariaDB Enterprise ColumnStore](../)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
