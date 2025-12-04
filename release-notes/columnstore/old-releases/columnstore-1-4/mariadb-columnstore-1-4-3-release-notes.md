# MariaDB ColumnStore 1.4.3 Release Notes

## Overview

MariaDB ColumnStore is a columnar storage engine. This is the first GA release in the ColumnStore 1.4 series. This release contains new features and fixes, compared to MariaDB ColumnStore 1.4.2.

This release of MariaDB ColumnStore is included with [MariaDB Enterprise Server 10.4.12-6](../../../enterprise-server/old-releases/10-4/release-notes-for-mariadb-enterprise-server-10-4-12-6.md).

MariaDB ColumnStore 1.4.3 was released on 2020-03-02.

## Notable Changes

* MariaDB ColumnStore 1.4.3 is the first Generally Available (GA) release of the ColumnStore 1.4 release series. ([MCOL-3686](https://jira.mariadb.org/browse/MCOL-3686))
* Support added for `ALTER TABLE ... ENGINE=ColumnStore` ([MCOL-128](https://jira.mariadb.org/browse/MCOL-128))
* Support added for `CREATE TABLE ... ENGINE=ColumnStore AS SELECT ...` ([MCOL-3349](https://jira.mariadb.org/browse/MCOL-3349))
* Support added to `cpimport` for S3 storage with multi-PM (multi-performance module). ([MCOL-3520](https://jira.mariadb.org/browse/MCOL-3520))

## Issues Fixed

### Can result in data loss

* Potential data loss with S3 StorageManager when `mcsadmin suspendDataWrites` returns before S3 sync is complete. ([MCOL-3736](https://jira.mariadb.org/browse/MCOL-3736))

### Can result in a hang or crash

* Server aborts if `Columnstore.xml` is missing. ([MCOL-3680](https://jira.mariadb.org/browse/MCOL-3680), [MCOL-3853](https://jira.mariadb.org/browse/MCOL-3853))
* A User Module (UM) join memory overflow can cause session hang and fail to free memory. ([MCOL-3713](https://jira.mariadb.org/browse/MCOL-3713))
* Improper StorageManager shutdown can result if process is killed by fatal error. ([MCOL-3748](https://jira.mariadb.org/browse/MCOL-3748))
* Truncation during [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/update) can cause crash. ([MCOL-3749](https://jira.mariadb.org/browse/MCOL-3749))
* Failure to sync timezone variable between queries can trigger a hang. ([MCOL-3776](https://jira.mariadb.org/browse/MCOL-3776))
* Failure in disk space pre-allocation for non-compressed data can trigger a crash in `cpimport` . ([MCOL-3791](https://jira.mariadb.org/browse/MCOL-3791))

### Can result in unexpected behavior

* Incorrect comparison of padded string vs. non-padded column. ([MCOL-1559](https://jira.mariadb.org/browse/MCOL-1559))
* Incorrect query validation for complex `ORDER BY` ([MCOL-975](https://jira.mariadb.org/browse/MCOL-975))
* [NOT IN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/operators/comparison-operators/not-in) subquery does not return rows with NULL qualifying column values. ([MCOL-1734](https://jira.mariadb.org/browse/MCOL-1734))
* `GROUP BY` doesn't process [IN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/operators/comparison-operators/in) and correlate subquery. ([MCOL-1963](https://jira.mariadb.org/browse/MCOL-1963))
* `GROUP BY` doesn't process [NOT IN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/operators/comparison-operators/not-in) and correlate subquery with aggregates. ([MCOL-1964](https://jira.mariadb.org/browse/MCOL-1964))
* Matched and changed row counts may be zero even if rows are changed (`Rows matched: 0 Changed: 0`). ([MCOL-2239](https://jira.mariadb.org/browse/MCOL-2239))
* Queries containing `SPACE()` may return error 1178. ([MCOL-3473](https://jira.mariadb.org/browse/MCOL-3473))

```
ERROR 1178 (42000) at line 1: The storage engine for the table
doesn't support IDB-1001: Function 'space' can only be used in
the outermost select or order by clause and cannot be used in
conjunction with an aggregate function.
```

* StorageManager may log inconsistently. ([MCOL-3638](https://jira.mariadb.org/browse/MCOL-3638))
* [COUNT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/count) with `DISTINCT` and two columns may fail. ([MCOL-3662](https://jira.mariadb.org/browse/MCOL-3662))
* If min/max are set, incorrect [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select) results may be provided after a cpimport due to incorrect extent elimination. ([MCOL-3716](https://jira.mariadb.org/browse/MCOL-3716))
* Impossible `WHERE` and `HAVING` conditions skipping may generate spurious warnings. ([MCOL-3769](https://jira.mariadb.org/browse/MCOL-3769))
* Failure to start when Server is rebooted without mcsadmin shutdownSystem first. ([MCOL-3829](https://jira.mariadb.org/browse/MCOL-3829))
* `ORDER BY` over negative [SEC\_TO\_TIME()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/sec_to_time) results produce an incorrect order. ([MCOL-3598](https://jira.mariadb.org/browse/MCOL-3598))
* Stopping Server with systemd triggers restart by ColumnStore. ([MCOL-3718](https://jira.mariadb.org/browse/MCOL-3718))
* `Note: 1618 COLLATE is ignored in ColumnStore` was not correctly surfaced. ([MCOL-3721](https://jira.mariadb.org/browse/MCOL-3721))
* Subqueries with `ORDER BY ... LIMIT` may produce incorrect result. ([MCOL-3747](https://jira.mariadb.org/browse/MCOL-3747))

### Related to performance

* Performance regression in [LIKE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/like) and [NOT LIKE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/not-like) ([MCOL-3663](https://jira.mariadb.org/browse/MCOL-3663))
* Slow DDL statement execution after a restart. ([MCOL-3745](https://jira.mariadb.org/browse/MCOL-3745))

### Related to install and upgrade

* `postConfigure` aborted due to missing `/tmp/columnstore_tmp_files` directory. ([MCOL-3675](https://jira.mariadb.org/browse/MCOL-3675))
* `postConfigure` output `'unassigned'` alias script name. ([MCOL-3676](https://jira.mariadb.org/browse/MCOL-3676))
* `columnstore-post-install` isn't triggered during package install. ([MCOL-3707](https://jira.mariadb.org/browse/MCOL-3707))
* Package removal doesn't trigger `mcsadmin shutdownSystem` ([MCOL-3708](https://jira.mariadb.org/browse/MCOL-3708))
* Package purge doesn't remove `/var/lib/columnstore` ([MCOL-3709](https://jira.mariadb.org/browse/MCOL-3709))

## Known Issues

* Performance of some queries, such as those containing UNION, may be worse than on ColumnStore 1.2.x.
* [LIKE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/like) and [NOT LIKE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/not-like) queries currently fall back to a slower execution method.

## Interface Changes

* None.

## Platforms

In alignment to the MariaDB Corporation Engineering Policy, MariaDB ColumnStore 1.4.4 is provided for:

* Red Hat Enterprise Linux 8
* Red Hat Enterprise Linux 7
* CentOS 8
* CentOS 7
* Ubuntu 20.04
* Ubuntu 18.04
* Ubuntu 16.04
* Debian 10
* Debian 9
* SUSE Linux Enterprise Server 15
* SUSE Linux Enterprise Server 12

**Note:** MariaDB Enterprise ColumnStore 1.4 is no longer supported. If you would like to deploy Enterprise ColumnStore, please use MariaDB Enterprise ColumnStore 5 or later. For installation and upgrade instructions, see "Deploy".

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
