# MariaDB ColumnStore 1.4.2 Release Notes

## Overview

MariaDB ColumnStore is a columnar storage engine. This is the first release in the ColumnStore 1.4 series. This release contains new features and fixes, compared to MariaDB ColumnStore 1.2.5.

This release of MariaDB ColumnStore is included with [MariaDB Enterprise Server 10.4.11-5](../../../enterprise-server/old-releases/10-4/release-notes-for-mariadb-enterprise-server-10-4-11-5.md).

MariaDB ColumnStore 1.4.2 was released on 2020-01-06.

## MariaDB Server Convergence

Until now, MariaDB ColumnStore has been maintained as a custom fork of MariaDB Server, to handle the unique way that queries are handled for distributed processing.

With this release, a joint project between the MariaDB Server and MariaDB ColumnStore engineering teams, ColumnStore now works as a pluggable storage engine on the standard MariaDB Enterprise Server 10.4 platform.

MariaDB Enterprise Server 10.4 includes distributed processing engine support features. These features are not present in the older 10.3 and 10.2 release series.

A standard MariaDB Server is now used for ColumnStore UM (User Module) nodes. ColumnStore users can now enjoy the benefits of MariaDB Server 10.4, and MariaDB Server 10.4 users are now able to deploy ColumnStore on top of their existing stack.

## New Features

### S3 Storage Manager

MariaDB ColumnStore now has the ability to use any object store that is Amazon S3 API compatible. The new Storage Manager uses a persistent disk cache for read/write operations so that it has minimal performance impact on ColumnStore. In some cases it will perform better than local disk operations.

Usage instructions:

1. Before running `postConfigure`, edit the `storagemanager.cnf` configuration file to specify the S3 connection parameters (as detailed in the S3 section of that file), and the local machine configuration (as detailed in the ObjectStorage and Cache sections). The configuration file is documented in-line. Enable the Storage Manager by setting ObjectStorage/Service to S3
2. Run `postConfigure`, and when promoted for type of storage, select the `StorageManager` option.

### cpimport S3 Support

cpimport is a high-speed bulk data loading utility for ColumnStore. cpimport now includes command-line options for loading a CSV file from Amazon S3 (and compatible) buckets.

| Option | Description                                                |
| ------ | ---------------------------------------------------------- |
| -y     | S3 Authentication Key                                      |
| -K     | S3 Secret Key                                              |
| -t     | S3 Bucket                                                  |
| -H     | S3 Hostname (omit if using Amazon S3, this is the default) |
| -g     | S3 Region                                                  |

When these options are set, `cpimport` will use the path/filename provided to load an object from object storage instead of a local file. Current behavior is to download the entire file into memory before processing.

### Expanded Data Type Support

* [TIMESTAMP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/timestamp) (with `CURRENT_TIMESTAMP`)
* [BOOLEAN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/data-types-numeric-data-types/boolean)
* [MEDIUMINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/data-types-numeric-data-types/mediumint)

Please note that for `cpimport` the current system time of the PM node is used.

### MODA() Mode Average UDAF

The `MODA()` UDAF (User-Defined Aggregate Function) determines the mode average. MODA() has tie-break behavior to use the closest to the average, and then the smallest absolute value.

### Statement-Based Replication Support

Statement-based replication into ColumnStore tables is supported by setting `columnstore_replication_slave=on` on the UM that will apply the replication data. Row-based replication events on ColumnStore replica (slave) tables will currently fail, generating an error viewable with [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-status)

## Notable Changes

### Performance Enhancements

* The performance of BRM (Block Resolution Manager) snapshots has been increased for improved performance when committing data to ColumnStore.
* To reduce SSD wear and increase write performance for large data sets containing many columns, ColumnStore now allocates disk as-needed, writing only real data and padding to fill the remainder of an 8KB block. ColumnStore previously wrote twice -- once to pre-allocate an empty file for each new extent (8 million item file for a column), and a second time to fill the file with real data.
* The outer "ORDER BY" of a query is now processed using ColumnStore's engine instead of MariaDB server. This uses a faster sorting algorithm for higher performance with larger result sets.
* Joins use a new hash algorithm which is significantly faster and requires significantly less initial memory to execute.
* Memory cleanup after query execution now occurs in a separate thread. This previously occurred in the main ExeMgr thread, which could delay execution of new queries.

### InfiniDB Alias Eliminated

ColumnStore 1.2 and earlier included the InfiniDB engine as an alias. This alias has now been removed. All ColumnStore tables must now be created with the engine name "columnstore". All MariaDB system variables prefixed with "infinidb\_" have now been removed.

### vtable Replaced by Query Execution Handlers

vtable has been replaced with a set of query execution handlers: `Select Handler`, `Derived Handler`, and table API mode.

The vtable mode switch (`infinidb_vtable_mode` system variable) has been eliminated. Two new session variables have been added: `columnstore_select_handler`, `columnstore_derived_handler`

The `Select Handler` is the replacement for a vtable, and is the default query execution handler. It is expected to provide the fastest execution path for the whole query.

Select Handler lacks support for some vtable features, including:

* Cartesian JOIN
* Non-Equi JOIN
* INSERT .. SELECT
* SELECT INTO OUTFILE

If the `Select Handler` fails to execute a query, an error is returned. If a query fails under the Select Handler, set `columnstore_select_handler=off` for the session. This will cause the Server to hand-off query execution to the Derived Handler. The query must be restarted after the session variable has been set.

If the `Derived Handler` fails to execute a query, an error is returned. If a query fails under both the `Select Handler` and `Derived Handler`, set columnstore\_select\_handler=off and `columnstore_derived_handler=off` for the session. This will cause table API execution, an equivalent to disabled vtable mode in ColumnStore 1.2.x and earlier. The query must be restarted after the session variables have been set.

### Deployment Methods

ColumnStore 1.4 is included with MariaDB Enterprise Server 10.4 on select Platforms.

ColumnStore is available for deployment from package tarball and repository. ColumnStore is not available for deployment from binary tarballs.

### "Distributed Install" Method Eliminated

The "distributed install" method which pushed packages onto other nodes during postConfigure has been removed. ColumnStore packages must now be installed on all nodes prior to startup.

### Configuration Path Changes

ColumnStore XML configuration files have moved to `/etc/columnstore`

MariaDB Enterprise Server configuration options for ColumnStore have moved to `/etc/my.cnf.d/columnstore.cnf` and the default MariaDB Enterprise Server `my.cnf` will load this file.

### Data Directory Path Change

The ColumnStore data directory has moved to `/var/lib/columnstore` and is separate from the MariaDB Server data directory at `/var/lib/mysql`

### Executable Path Changes

ColumnStore binaries have moved to `/usr/bin` or `/usr/sbin`, and the libraries are in the OS standard `/usr` library path. Some ColumnStore binaries have been renamed to avoid conflict, including:

| Old Filename | New Filename             |
| ------------ | ------------------------ |
| post-install | columnstore-post-install |
| getConfig    | mcsGetConfig             |
| setConfig    | mcsSetConfig             |

### User Account for Cross-Engine Joins

Cross-engine joins depend on TCP connection from ExeMgr to the Server process. Since the database `root` user in MariaDB Enterprise Server 10.4 authenticates only by UNIX socket, a dedicated user must be created to support cross-engine joins. The cross engine section of `Columnstore.xml` should be edited accordingly.

## Issues Fixed

### Can result in data loss

* DBRM files could be deleted during a failover scenario. ([MCOL-2152](https://jira.mariadb.org/browse/MCOL-2152))

### Can result in a hang or crash

* Certain window function queries could crash the Server process. ([MCOL-3434](https://jira.mariadb.org/browse/MCOL-3434))

### Can result in unexpected behavior

* `group_concat()` with `DISTINCT` concatenates even non-distinct values. ([MCOL-2146](https://jira.mariadb.org/browse/MCOL-2146))
* Wrong results could be returned for a complex query with subquery and window functions over decimal(12,4) column. ([MCOL-3423](https://jira.mariadb.org/browse/MCOL-3423))
* Pipe operator (|) could return wrong results. ([MCOL-174](https://jira.mariadb.org/browse/MCOL-174))
* [DIV](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/numeric-functions/div) operator could return wrong results. ([MCOL-179](https://jira.mariadb.org/browse/MCOL-179))
* Comparison of padded strings could provide incorrect results. ([MCOL-1559](https://jira.mariadb.org/browse/MCOL-1559))
* [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/create/create-table) could fail when table name contained space and certain characters; not `A-Z a-z 0-9 _` ([MCOL-2219](https://jira.mariadb.org/browse/MCOL-2219))
* `DISTINCT` could be performed in incorrect order relative to Window functions and UNION ([MCOL-3492](https://jira.mariadb.org/browse/MCOL-3492))
* `cpimport` outputs value truncation warning when read buffer (`-b`) is set to `1` ([MCOL-774](https://jira.mariadb.org/browse/MCOL-774))
* Cross-engine joins with query using `DISTINCT` could return `NULL` ([MCOL-3588](https://jira.mariadb.org/browse/MCOL-3588))
* Bulk write API writes were possible when writes were suspended. ([MCOL-3576](https://jira.mariadb.org/browse/MCOL-3576))
* Multi-column [IN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/operators/comparison-operators/in) statements could produce incorrect results. ([MCOL-3448](https://jira.mariadb.org/browse/MCOL-3448))
* `JOIN` could significantly waste memory. ([MCOL-1758](https://jira.mariadb.org/browse/MCOL-1758))
* Memory leaks. ([MCOL-3621](https://jira.mariadb.org/browse/MCOL-3621))
* Plugin metadata was inconsistent. ([MCOL-3681](https://jira.mariadb.org/browse/MCOL-3681), [MCOL-3669](https://jira.mariadb.org/browse/MCOL-3669))

### Related to install and upgrade

* Cosmetic typo in `postConfigure` output. Output upon success is now `MariaDB ColumnStore Install Successfully Completed, System is Active` ([MCOL-1598](https://jira.mariadb.org/browse/MCOL-1598))

## Known Issues

* Performance of some queries, such as those containing UNION, may be worse than on ColumnStore 1.2.x.
* [LIKE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/like) and [NOT LIKE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/not-like) queries currently fall back to a slower execution method.

## Interface Changes

* `Columnstore_commit_hash` status variable added
* `Columnstore_version` status variable added
* `columnstore_compression_type` system variable added
* `columnstore_decimal_scale` system variable added
* `columnstore_derived_handler` system variable added
* `columnstore_diskjoin_bucketsize` system variable added
* `columnstore_diskjoin_largesidelimit` system variable added
* `columnstore_diskjoin_smallsidelimit` system variable added
* `columnstore_double_for_decimal_math` system variable added
* `columnstore_group_by_handler` system variable added
* `columnstore_import_for_batchinsert_delimiter` system variable added
* `columnstore_import_for_batchinsert_enclosed_by` system variable added
* `columnstore_local_query` system variable added
* `columnstore_orderby_threads` system variable added
* `columnstore_ordered_only` system variable added
* `columnstore_replication_slave` system variable added
* `columnstore_select_handler` system variable added
* `columnstore_string_scan_threshold` system variable added
* `columnstore_stringtable_threshold` system variable added
* `columnstore_um_mem_limit` system variable added
* `columnstore_use_decimal_scale` system variable added
* `columnstore_use_import_for_batchinsert` system variable added
* `columnstore_varbin_always_hex` system variable added
* `Columnstore ha_columnstore.so` plugin added
* `COLUMNSTORE_COLUMNS` information schema table added
* `COLUMNSTORE_EXTENTS` information schema table added
* `COLUMNSTORE_FILES` information schema table added
* `COLUMNSTORE_TABLES` information schema table added
* `mysqld --columnstore-columns` command-line option added
* `mysqld --columnstore-compression-type` command-line option added
* `mysqld --columnstore-decimal-scale` command-line option added
* `mysqld --columnstore-derived-handler` command-line option added
* `mysqld --columnstore-diskjoin-bucketsize` command-line option added
* `mysqld --columnstore-diskjoin-largesidelimit` command-line option added
* `mysqld --columnstore-diskjoin-smallsidelimit` command-line option added
* `mysqld --columnstore-double-for-decimal-math` command-line option added
* `mysqld --columnstore-extents` command-line option added
* `mysqld --columnstore-files` command-line option added
* `mysqld --columnstore-group-by-handler` command-line option added
* `mysqld --columnstore-import-for-batchinsert-delimiter` command-line option added
* `mysqld --columnstore-import-for-batchinsert-enclosed-by` command-line option added
* `mysqld --columnstore-local-query` command-line option added
* `mysqld --columnstore-orderby-threads` command-line option added
* `mysqld --columnstore-ordered-only` command-line option added
* `mysqld --columnstore-replication-slave` command-line option added
* `mysqld --columnstore-select-handler` command-line option added
* `mysqld --columnstore-string-scan-threshold` command-line option added
* `mysqld --columnstore-stringtable-threshold` command-line option added
* `mysqld --columnstore-tables` command-line option added
* `mysqld --columnstore-um-mem-limit` command-line option added
* `mysqld --columnstore-use-decimal-scale` command-line option added
* `mysqld --columnstore-use-import-for-batchinsert` command-line option added
* `mysqld --columnstore-varbin-always-hex` command-line option added
* `mysqld --columnstore` command-line option added

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
