# MariaDB ColumnStore 23.10.3 Release Notes

## Overview

MariaDB Enterprise ColumnStore 23.10.3 is a maintenance release of MariaDB Enterprise ColumnStore. MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server.

MariaDB Enterprise ColumnStore 23.10.3 was released on 2025-01-27. This release is of General Availability (GA) maturity. MariaDB Enterprise ColumnStore 23.10.3 is a GA release in the 23.10 series.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.20-16.

## Notable Changes

* NOT LIKE is not compatible with MariaDB on explicit NULL ([MCOL-4499](https://jira.mariadb.org/browse/MCOL-4499))
* LEFT(str, negativeInt) returns a wrong result ([MCOL-4671](https://jira.mariadb.org/browse/MCOL-4671))
* Having not() provokes an ERROR 2013 ([MCOL-4756](https://jira.mariadb.org/browse/MCOL-4756))
* MariaDB Columnstore produces wrong averages on extracted null-datetime fields (like year) ([MCOL-5241](https://jira.mariadb.org/browse/MCOL-5241))
* select-union-select gives corrupted values ([MCOL-5307](https://jira.mariadb.org/browse/MCOL-5307))
* Wrong result ('`pNuLl_`' instead of NULL) in the TEXT column when LEFT OUTER JOIN is used with WHERE condition ([MCOL-5581](https://jira.mariadb.org/browse/MCOL-5581))
* Incorrect columnstore result | implicit self joins ([MCOL-5651](https://jira.mariadb.org/browse/MCOL-5651))
* UNION query returns incorrect results when one table is ENGINE COLUMNSTORE ([MCOL-5669](https://jira.mariadb.org/browse/MCOL-5669))
* DAY function returns wrong result in query on Columnstore table ([MCOL-5670](https://jira.mariadb.org/browse/MCOL-5670))
* Different Resultset with AllowDiskBasedAggregation = Y ([MCOL-5691](https://jira.mariadb.org/browse/MCOL-5691))
* UNION`/`INTERSECT`/`EXCEPT VALUES crashes the server if a ColumnStore table is involved ([MCOL-5703](https://jira.mariadb.org/browse/MCOL-5703))
* Columnstore: SELECT SUM(0) may cause data type unknown error ([MCOL-5708](https://jira.mariadb.org/browse/MCOL-5708))
* ALTER Column VARCHAR | Not Supported ([MCOL-5779](https://jira.mariadb.org/browse/MCOL-5779))
* MariaDB Columnstore 23.10.2: wrong COUNT DISTINCT`s in` GROUP BY ([MCOL-5875](https://jira.mariadb.org/browse/MCOL-5875))
* SELECT GROUP BY is not picking not-NULL values ([MCOL-5755](https://jira.mariadb.org/browse/MCOL-5755))
* SELECT CONCAT() throws error: MCS-2021 ([MCOL-5776](https://jira.mariadb.org/browse/MCOL-5776))

## Issues Fixed

### Can result in hang or crash

* Reading a Columnstore table via a view using "count" crashes when the view has "order by" in definition ([MCOL-5249](https://jira.mariadb.org/browse/MCOL-5249))
* CMAPI self-signed cert are expired after one year.. which leads to "Connection refused" messages ([MCOL-5454](https://jira.mariadb.org/browse/MCOL-5454))
* Columnstore crashes/unstable on too large selects ([MCOL-5587](https://jira.mariadb.org/browse/MCOL-5587))
* OOM occurs during disk based aggregation with um\_mem\_limit > 0 ([MCOL-5715](https://jira.mariadb.org/browse/MCOL-5715))
* SM doesn't quit endless loop when S3 service returns non-retryable error ([MCOL-5785](https://jira.mariadb.org/browse/MCOL-5785))
* MCS crashes when PMSmallSide is raised > 1GB(the current default) ([MCOL-5787](https://jira.mariadb.org/browse/MCOL-5787))
* Memory leaks in plugin code ([MCOL-5791](https://jira.mariadb.org/browse/MCOL-5791))
* RGData ui32 counters limits us with addressing big data ([MCOL-5794](https://jira.mariadb.org/browse/MCOL-5794))
* Separated UM/PM topologies are broken b/c DEC sends request to impossible PM id ([MCOL-5805](https://jira.mariadb.org/browse/MCOL-5805))
* UM/PM roles are broken in DEC::writeToClients ([MCOL-5808](https://jira.mariadb.org/browse/MCOL-5808))
* Columnstore Server crashes when REGEX is matched to function return value ([MCOL-5812](https://jira.mariadb.org/browse/MCOL-5812))
* Pass UBSAN sanity checks ([MCOL-5844](https://jira.mariadb.org/browse/MCOL-5844))

### Related to performance

* ByteStreamProcessor is slow with UM JOIN ([MCOL-5788](https://jira.mariadb.org/browse/MCOL-5788))
* Remove boost::iequals from the code because it takes a global lock getting a locale ([MCOL-4696](https://jira.mariadb.org/browse/MCOL-4696))

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 23.10.3 is provided for:

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
