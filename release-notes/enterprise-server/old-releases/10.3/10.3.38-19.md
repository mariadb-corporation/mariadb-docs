# Release Notes for MariaDB Enterprise Server 10.3.38-19

MariaDB Enterprise Server 10.3.38-19 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3. This release includes a variety of fixes.

MariaDB Enterprise Server 10.3.38-19 was released on 2023-03-13.

## Issues Fixed

### Can result in data loss

* When executing a `DELETE` or `UPDATE` with a subselect, the server can crash. ([MDEV-10087](https://jira.mariadb.org/browse/MDEV-10087))
* When performing an incremental backup, MariaDB Enterprise Backup does not reflect databases that have been dropped and created. ([MDEV-23335](https://jira.mariadb.org/browse/MDEV-23335))

### Can result in a hang or crash

* When `DELETE HISTORY` is executed for a system versioned table with full text index, the server can crash. ([MDEV-25004](https://jira.mariadb.org/browse/MDEV-25004))
* When an `ALTER TABLE` statement causes InnoDB to rebuild a table with a spatial index, the server can crash. ([MDEV-29856](https://jira.mariadb.org/browse/MDEV-29856))
* When using `SPIDER` with `SPIDER_DIRECT_SQL` and `spider_udf_ds_use_real_table=1`, the server can crash. ([MDEV-29855](https://jira.mariadb.org/browse/MDEV-29855))
* When executing `REPLACE INTO ... PARTITION(...)`, the server can crash. ([MDEV-29636](https://jira.mariadb.org/browse/MDEV-29636))
* `Galera SST` doesn't properly handle undo\* files from InnoDB. As a result, SST may terminate incorrectly when `--innodb-undo-tablespaces` is set to 3 or more. ([MDEV-30157](https://jira.mariadb.org/browse/MDEV-30157))
* With a query containing nested `WINDOW` clauses, the server can crash. ([MDEV-30052](https://jira.mariadb.org/browse/MDEV-30052))
* When executing a `SELECT` from complex a view with `WHERE` clause and with the `setting derived_merge=on`, the server can crash. ([MDEV-30081](https://jira.mariadb.org/browse/MDEV-30081))
* Infinite sequence of recursive calls when processing embedded `CTE`, when such a reference has the same table name as the name of the `CTE`. ([MDEV-30248](https://jira.mariadb.org/browse/MDEV-30248))
* A deadlock between `InnoDB` statistics updates and `BLOB` insert can result in a server hang. ([MDEV-29883](https://jira.mariadb.org/browse/MDEV-29883))

### Can result in unexpeted behavior

* `log_query_not_using_indexes=OFF` is ignored when `log_slow_filter` is an empty string. ([MDEV-21187](https://jira.mariadb.org/browse/MDEV-21187))
* MariaDB Enterprise Backup returns with an error when the option `--galera-info` is used for creating a backup of a MariaDB Server instance, which is not a MariaDB Enterprise Cluster node. `Failed to get master wsrep state from SHOW STATUS` ([MDEV-30293](https://jira.mariadb.org/browse/MDEV-30293))
* When querying a table with virtual generated columns using full text search, these columns are not generated and are always `NULL` in the result set. ([MDEV-29169](https://jira.mariadb.org/browse/MDEV-29169))
* Identifiers are not quoted for the output of `SHOW GRANTS`. Using the result to execute the grant statement results in a syntax error, if reserved keywords are used. ([MDEV-30056](https://jira.mariadb.org/browse/MDEV-30056))
* Spider table with CHARSET `utf32/utf16/ucs2` tries to set client CHARSET to unsupported value. ([MDEV-29562](https://jira.mariadb.org/browse/MDEV-29562))
* Incorrect results are returned when using `STDDEV_SAMP()` with a view. ([MDEV-19071](https://jira.mariadb.org/browse/MDEV-19071))
* A spurious error can be generated: `ERROR 1292 (22007) at the line 15: Truncated incorrect DECIMAL value:#`([MDEV-30342](https://jira.mariadb.org/browse/MDEV-30342))
* When running `mariadb-binlog` using the option --verbose, cannot read row events with compressed columns: `Error: Don't know how to handle column type:...` ([MDEV-25277](https://jira.mariadb.org/browse/MDEV-25277))
* Incorrect results are returned with outer join, merged derived table, and view. ([MDEV-28602](https://jira.mariadb.org/browse/MDEV-28602))
* Some DDL, such as `ANALYZE`, can be completed out of order on parallel replicas. ([MDEV-30323](https://jira.mariadb.org/browse/MDEV-30323))
* `seconds_behind_master` is incorrect for delayed parallel replicas. ([MDEV-29639](https://jira.mariadb.org/browse/MDEV-29639))

## Platforms

In alignment with the [enterprise lifecycle](../../about/enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.3.38-19 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 18.04 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see ["MariaDB Corporation Engineering Policies"](https://mariadb.com/engineering-policies).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
