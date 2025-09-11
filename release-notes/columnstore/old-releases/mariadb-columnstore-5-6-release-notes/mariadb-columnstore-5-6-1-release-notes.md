# MariaDB ColumnStore 5.6.1 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a columnar storage engine included with [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md). This is the fifth release in the Enterprise ColumnStore 5 series.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.5.10-7.

This release is of General Availability (GA) maturity.

MariaDB Enterprise ColumnStore 5.6.1 was released on 2021-06-14.

## Notable Changes

* LOOR() now returns a fully-formatted DATETIME in alignment to CEIL() behavior. ([MCOL-4263](https://jira.mariadb.org/browse/MCOL-4263))
* MariaDB Enterprise ColumnStore now supports disk-based aggregation. Prior to this release, all aggregation could occur only in memory. With disk-based aggregation, larger aggregated result sets can be handled than would fit in memory. ([MCOL-563](https://jira.mariadb.org/browse/MCOL-563))\
  To enable disk-based aggregation, edit `Columnstore.xml`and within the RowAggregation section configure:
  * `AllowDiskBasedAggregation=Y` to enable the feature. The default is N
  * `TempDir`to the directory path for storing temporary files. The default is /tmp/columnstore\_tmp\_files/aggregates
* SSL certificate verification can now be disabled for S3-compatible storage. We recommend that SSL certificate verification be disabled only when necessary, and where appropriate compensatory controls exist. ([MCOL-3542](https://jira.mariadb.org/browse/MCOL-3542))

To disable SSL certificate verification, edit storagemanager.cnf and configure:**`ssl_verify = disabled` to disable SSL certificate verification. The default is `ssl_verify = enabled`, which enables SSL certificate verification when connecting by HTTPS to S3-compatible storage.**

* HTTP connections can now be made to S3-compatible storage. We recommend using HTTPS connections, and to use HTTP connections only when necessary and where appropriate compensatory controls exist. ([MCOL-3542](https://jira.mariadb.org/browse/MCOL-3542))

To enable HTTP connections, edit storagemanager.cnf and configure:**`use_http = enabled` to enable HTTP connections to S3-compatible storage. The default is `use_http = disabled`, which uses HTTPS connections to S3-compatible storage.**

* TCP port number for S3-compatible storage connections can now be specified by setting port\_number in storagemanager.cnf ([MCOL-3542](https://jira.mariadb.org/browse/MCOL-3542))
* CMAPI now pushes storagemanager.cnf changes to newly-added nodes. Prior to this release, storagemanager.cnf to nodes before they were added. ([MCOL-4363](https://jira.mariadb.org/browse/MCOL-4363))
* Performance enhancements for general query execution, LIKE, and for subqueries containing a UNION ([MCOL-4692](https://jira.mariadb.org/browse/MCOL-4692), [MCOL-4498](https://jira.mariadb.org/browse/MCOL-4498), [MCOL-4589](https://jira.mariadb.org/browse/MCOL-4589))
* `TRIM(), CONCAT(), REPLACE(), ENCODE(), and DECODE()` functions, and the || (concatenate) operator now work when `sql_mode=ORACLE` ([MCOL-4044](https://jira.mariadb.org/browse/MCOL-4044))
* Update to CMAPI REST API for node add:
  * Old:

```
curl -X PUT https://127.0.0.1:8640/cmapi/0.4.0/cluster/add-node --header 'Content-Type:application/json' --header 'x-api-key:somekey123' --data '{"timeout":20, "node": "172.31.2.106"}' -k
```

* New:

```
curl -X PUT https://127.0.0.1:8640/cmapi/0.4.0/cluster/node --header 'Content-Type:application/json' --header 'x-api-key:somekey123' --data '{"timeout":20, "node": "172.31.3.254"}' -k | jq .
```

* Update to CMAPI REST API for node removal:
  * Old:

```
curl -X PUT https://127.0.0.1:8640/cmapi/0.4.0/cluster/remove-node --header 'Content-Type:application/json' --header 'x-api-key:somekey123' --data '{"timeout":20, "node": "172.31.2.106"}' -k
```

* New:

```
curl -X DELETE https://127.0.0.1:8640/cmapi/0.4.0/cluster/node --header 'Content-Type:application/json' --header 'x-api-key:somekey123' --data '{"timeout":20, "node": "172.31.11.19"}' -k | jq .
```

## Issues Fixed

### Can result in data loss

* CMAPI shutdown of cluster is abrupt, and may occur in the middle of transaction execution or rollback. ([MCOL-4675](https://jira.mariadb.org/browse/MCOL-4675))

### Can result in a hang or crash

* Crash with JOIN when using certain collations. ([MCOL-4470](https://jira.mariadb.org/browse/MCOL-4470))
* Crash or performance impact due to SELECT bypassing select handler when @variables are involved in the query projection list. ([MCOL-4410](https://jira.mariadb.org/browse/MCOL-4410))
* Assert in COUNT(DISTINCT) in a JOIN on Ubuntu 20.04. ([MCOL-4638](https://jira.mariadb.org/browse/MCOL-4638))
* Assert when a function is used in an aggregation on Ubuntu 20.04. ([MCOL-4620](https://jira.mariadb.org/browse/MCOL-4620))
* Delay in execution of first query after ColumnStore restart. ([MCOL-4071](https://jira.mariadb.org/browse/MCOL-4071))
* Long command strings cause crash of cpimport ([MCOL-3394](https://jira.mariadb.org/browse/MCOL-3394))
* Failover hangs with multi-node ColumnStore 5.4 when using S3 storage, requiring an API call to restart cluster. ([MCOL-4440](https://jira.mariadb.org/browse/MCOL-4440))
* Crash with concurrent Pentaho ETL and queries. ([MCOL-4555](https://jira.mariadb.org/browse/MCOL-4555))

### Can result in unexpected behavior

* Incorrect result from UNION of a huge narrow DECIMAL (such as 17,1) and BIGINT ([MCOL-4613](https://jira.mariadb.org/browse/MCOL-4613))
* UDAF can return a bad value instead of expected value NULL ([MCOL-4643](https://jira.mariadb.org/browse/MCOL-4643))
* DISTINCT is case sensitive even when using case insensitive collation. ([MCOL-4065](https://jira.mariadb.org/browse/MCOL-4065))
* WHERE is not collation aware on CHAR(1) and CHAR(2) ([MCOL-4726](https://jira.mariadb.org/browse/MCOL-4726))
* GROUP and DISTINCT are not collation aware on CHAR(1) ([MCOL-4721](https://jira.mariadb.org/browse/MCOL-4721))
* LIKE is not collation-aware. ([MCOL-4498](https://jira.mariadb.org/browse/MCOL-4498))
* Performance impacted on nested queries with aggregates. ([MCOL-4543](https://jira.mariadb.org/browse/MCOL-4543))
* INSERT .. SELECT \* FROM (subselect) throws is not in GROUP BY clause even when it is part of the GROUP BY clause. ([MCOL-3890](https://jira.mariadb.org/browse/MCOL-3890))
* ERROR 1815 (HY000): Internal error: IDB-1000 on FROM subquery containing nested JOINs. ([MCOL-4680](https://jira.mariadb.org/browse/MCOL-4680))
* INSERT from VIEW generates error IDB-1011: Insert on VIEW is currently not supported. ([MCOL-4687](https://jira.mariadb.org/browse/MCOL-4687))

## Related to install and upgrade

* .DEB packages missing /usr/bin/testS3Connection ([MCOL-4443](https://jira.mariadb.org/browse/MCOL-4443))

## Platforms

In alignment with the [enterprise lifecycle](../../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 5.5.2 is provided for:

* CentOS 7
* CentOS 8
* Debian 9
* Debian 10
* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 8
* SUSE Linux Enterprise Server 12
* SUSE Linux Enterprise Server 15
* Ubuntu 18.04
* Ubuntu 20.04

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
