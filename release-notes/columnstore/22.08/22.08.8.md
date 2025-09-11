# MariaDB ColumnStore 22.08.8 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 22.08.8 is a maintenance release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md). MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server.

MariaDB Enterprise ColumnStore 22.08.8 was released on 2023-02-10. This release is of General Availability (GA) maturity.

MariaDB Enterprise ColumnStore 22.08 replaces MariaDB Enterprise ColumnStore 6 in MariaDB Enterprise Server 10.6.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.11-6.

Users of earlier MariaDB Enterprise ColumnStore 22.08 releases are encouraged to upgrade.

## Notable Changes

* The JSON\_ARRAYAGG function is supported for ColumnStore tables as a distributed aggregate function and can be used to aggregate a column's values into a JSON array. ([MCOL-5224](https://jira.mariadb.org/browse/MCOL-5224), [MCOL-5227](https://jira.mariadb.org/browse/MCOL-5227))
  * In previous releases, the following error can be raised when the JSON\_ARRAYAGG function is called in a query on a ColumnStore table and the ColumnStore select handler is enabled:

```
ERROR 1178 (42000): The storage engine for the table doesn't support Non supported aggregate type on the select clause
```

* Starting with this release, the JSON\_ARRAYAGG function can be called in a query on a ColumnStore table when the ColumnStore select handler is enabled. The function accepts a column or expression as an argument. The expression is evaluated for every column in the result set, and all of the values are aggregated into a single JSON array:

```
CREATE TABLE t (a INT, b INT)
ENGINE=ColumnStore;
```

```
INSERT INTO t VALUES
  (1,3), (1,5), (8,2), (5,7),
  (5,6), (10,1), (6,4), (3,9),
  (3,9), (7,2), (7,5), (2,6),
  (9,10), (9,5), (4,8);
```

```
SELECT a, JSON_ARRAYAGG(b)
 FROM t
 GROUP BY a;
```

```
+------+------------------+
| a    | JSON_ARRAYAGG(b) |
+------+------------------+
|    1 | [3,5]            |
|    2 | [6]              |
|    3 | [9,9]            |
|    4 | [8]              |
|    5 | [7,6]            |
|    6 | [4]              |
|    7 | [2,5]            |
|    8 | [2]              |
|    9 | [10,5]           |
|   10 | [1]              |
+------+------------------+
```

**In many cases, when a query uses the GROUP\_CONCAT function, the query can be converted to use the JSON\_ARRAYAGG function instead. The primary benefit is that the JSON\_ARRAYAGG function returns a JSON array, and there are many functions and external tools available for reading and manipulating JSON.**

* Collection of histogram statistics is supported on ColumnStore tables and can be used for cost-based optimization of joins. ([MCOL-5191](https://jira.mariadb.org/browse/MCOL-5191))
  * In previous releases, queries containing complex joins on ColumnStore tables can fail with the following error:

```
ERROR 1815 (HY000) at line 6: Internal error: IDB-1003: Circular joins are not supported.
```

* Starting with this release, when histogram statistics are available for a ColumnStore table, the storage engine can use the histogram statistics to determine the uniqueness of a column and process the join graph more efficiently. To collect histogram statistics on a ColumnStore table, use the ANALYZE TABLE statement:

```
ANALYZE TABLE t1;
```

## Issues Fixed

### Can result in data loss

* When ColumnStore is configured to use S3-compatible storage, if the endpoint and region parameters in /etc/columnstore/storagemanager.cnf do not refer to the same region where bucket is located, ColumnStore fails to send data to cloud storage, but does not detect the failure. ([MCOL-5177](https://jira.mariadb.org/browse/MCOL-5177))
  * In previous releases, the endpoint would send ColumnStore an HTTP 301 status code to indicate a failure, but ColumnStore would incorrectly treat it as a success.
    * Starting with this release, ColumnStore correctly identifies the failure and raises an error message:

```
S3Storage::putObject(): Bucket location not match provided endpoint:, bucket = BUCKET, endpoint = ENDPOINT.
```

### Can result in a hang or crash

* When processing a hash join, ExeMgr can crash with a SIGABRT. ([MCOL-5265](https://jira.mariadb.org/browse/MCOL-5265))

### Can result in unexpected behavior

* When a SELECT statement calls SUM(COLUMN=VALUE), the statement fails with an unclear error message. ([MCOL-603](https://jira.mariadb.org/browse/MCOL-603))
  * In previous releases, the following error is raised:

```
ERROR 1815 (HY000): Internal error: std::bad_typeid
```

**Starting with this release, the following error is raised:**\
&#xNAN;**<`.`**

`ERROR 1178 (42000): The storage engine for the table doesn't support MCS-2027: Non supported item in aggregate function SUM(COLUMN=VALUE).`\
`<`.

* When the ANALYZE statement is executed with a SQL statement as an argument, ColumnStore can return an error. ([MCOL-1170](https://jira.mariadb.org/browse/MCOL-1170))
  * In previous releases, the following error is sometimes raised:

```
ERROR 1815 (HY000): Internal error: Unknown error
```

* Starting with this release, an error should not be raised, and the execution plan should be printed:

```
ANALYZE SELECT * FROM t1 WHERE c1 = 1;
```

```
+------+---------------+-------+------+---------------+------+---------+------+------+--------+----------+------------+-------+
| id   | select_type   | table | type | possible_keys | key  | key_len | ref  | rows | r_rows | filtered | r_filtered | Extra |
+------+---------------+-------+------+---------------+------+---------+------+------+--------+----------+------------+-------+
|    1 | PUSHED SELECT | NULL  | NULL | NULL          | NULL | NULL    | NULL | NULL | NULL   |     NULL |       NULL | NULL  |
+------+---------------+-------+------+---------------+------+---------+------+------+--------+----------+------------+-------+
```

* When a column is added to a table on a primary node with multi-node ColumnStore, ColumnStore tries to add the new column to the table twice on the replica nodes, which causes a replication failure. ([MCOL-5000](https://jira.mariadb.org/browse/MCOL-5000))
  * In previous releases, when replication failed, messages like the following appear in the MariaDB error log:`<<ocde>>`\
    \[ERROR] Slave SQL: Error 'Got error 1815 "Unknown error 1815" from storage engine ColumnStore' on query. Default database: 'db1'. Query: 'ALTER TABLE t1 ADD COLUMN (col2 varchar(100))', Gtid GTID\_POS, Internal MariaDB error code: 1030\
    \[Warning] Slave: Got error 1815 "Unknown error 1815" from storage engine ColumnStore Error\_code: 1030\
    \[ERROR] Error running query, slave SQL thread aborted. Fix the problem, and restart the slave SQL thread with "SLAVE START". We stopped at log 'LOG\_FILE' position LOG\_POS; GTID position 'GTID\_POS'\
    <>
  * Starting with this release, ColumnStore only adds the new column to the table once on the replica nodes, so the replication failure does not occur.
* When querytstats is enabled, if a query contains a LEFT JOIN and the ON clause contains the LOWER() function, an error is written to the ColumnStore log. ([MCOL-5223](https://jira.mariadb.org/browse/MCOL-5223))
  * In previous releases, the following error is written to the ColumnStore log:

```
1e3afaf1eaef Calpont[135]: 37.906020 |0|0|0| E 00 CAL0000: /home/buildbot/buildbot/padding_for_CPACK_RPM_BUILD_SOURCE_DIRS_PREFIX/mariadb-10.6.8/storage/columnstore/columnstore/dbcon/joblist/tuplehashjoin.cpp@1095: assertion 'idlsz > 1' failed
```

**Starting with this release, the query can be executed without raising an error.**

* When the TRUNCATE() function is called with a CHAR or VARCHAR column that contains numeric characters, an incorrect value is returned. ([MCOL-5248](https://jira.mariadb.org/browse/MCOL-5248))
* When multi-node ColumnStore is configured to use shared local storage, replica nodes can overwrite their local copies of the extent map files multiple times during shutdown. ([MCOL-5302](https://jira.mariadb.org/browse/MCOL-5302))
* When columnstore\_use\_import\_for\_batchinsert=ON is set on multi-node ColumnStore, INSERT INTO .. SELECT statements in a transaction report that rows were inserted, even though no rows are inserted. ([MCOL-5367](https://jira.mariadb.org/browse/MCOL-5367))
* When ExeMgr finishes serving a request from MariaDB Server, ExeMgr's TCP connection can remain open, and its thread can continue running, which can cause ColumnStore to use more resources than required. ([MCOL-5384](https://jira.mariadb.org/browse/MCOL-5384))

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 22.08.8 is provided for:

* CentOS 7 (x86\_64)
* Debian 11 (x86\_64, ARM64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)
* Ubuntu 22.04 (x86\_64, ARM64)

## Installation Instructions

* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.6 ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[and MariaDB Enterprise ColumnStore 23.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 23.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[ and MariaDB Enterprise ColumnStore 23.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore 23.10 with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[ and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 23.10 with MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)

## Upgrade Instructions

* Upgrade Multi-Node MariaDB Enterprise ColumnStore from 6 to 23.10
* [Major Release Upgrades for MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/columnstore-release-notes/README.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
