# MariaDB ColumnStore 1.5.2 Release Notes

## Overview

MariaDB ColumnStore is a columnar storage engine included with MariaDB Enterprise Server. This release of MariaDB ColumnStore is included with MariaDB Community Server 10.5.4.

MariaDB ColumnStore 1.5.2 was released on 2020-06-24. It is the first release in the MariaDB ColumnStore 1.5 series. This release is of Beta maturity, and should not be used with production workloads.

## Notable Changes

* Comprehensive rewrite of installation and administration logic. ([MCOL-3836](https://jira.mariadb.org/browse/MCOL-3836))
* Simplified installation:
  * Users no longer need to execute `columnstore-post-install` and `postConfigure`
  * It is a plugin for MariaDB Community Server.
  * It is packaged similar to other MariaDB Community Server plugins.
* Simplified administration:
  * `mcsadmin` has been removed. Instead, ColumnStore 1.5 uses `systemd` for administration
  * The new `systemd` service called `mariadb-columnstore` is used to manage ColumnStore's processes.
* Support for standard MariaDB Community Server collation and character sets. ([MCOL-337](https://jira.mariadb.org/browse/MCOL-337))
* Improved performance for `REGR_*` functions. ([MCOL-3837](https://jira.mariadb.org/browse/MCOL-3837))
* Fixes for defects in tiered storage and S3-compatible object storage.

## New Features

* Support to set up `tempfiles.d` to prevent the OS from flushing `/tmp` on reboot. ([MCOL-2101](https://jira.mariadb.org/browse/MCOL-2101))
* Support for faster replication-slave processing. ([MCOL-3835](https://jira.mariadb.org/browse/MCOL-3835))
* Implements `ISTRUE()` function. ([MCOL-3756](https://jira.mariadb.org/browse/MCOL-3756))
* Creates a systemd unit file for the MariaDB ColumnStore service. ([MCOL-3914](https://jira.mariadb.org/browse/MCOL-3914))
* Implements `MCSNodeControl` package. ([MCOL-3920](https://jira.mariadb.org/browse/MCOL-3920))
* Implements REST API server. ([MCOL-3921](https://jira.mariadb.org/browse/MCOL-3921))
* Merges 3 MariaDB ColumnStore packages into a single package. ([MCOL-3991](https://jira.mariadb.org/browse/MCOL-3991))
* Changing `systemlang` to an unrecognized string now causes MariaDB ColumnStore to not start up. ([MCOL-3420](https://jira.mariadb.org/browse/MCOL-3420))
* Support for [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table) conversion to MariaDB ColumnStore. ([MCOL-3852](https://jira.mariadb.org/browse/MCOL-3852))
* Support for `COLLATE` in DDL and `ORDER BY` clauses. ([MCOL-3862](https://jira.mariadb.org/browse/MCOL-3862))
* Improvements in failover design. ([MCOL-3886](https://jira.mariadb.org/browse/MCOL-3886))

## Changed Features

* `loadbrm` process rewritten in Python (`mcs-loadbrm.py`). Now requires Python 3 as a dependency.

## Issues Fixed

* Fixes [IN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/operators/comparison-operators/in) not evaluating properly in WHERE clauses. ([MCOL-2096](https://jira.mariadb.org/browse/MCOL-2096))
* Fixes DNS error `MessageQueueClient :: setup (): unknown name or service - ExeMgr = unassigned` ([MCOL-2181](https://jira.mariadb.org/browse/MCOL-2181))
* Fixes `FILE001.cdf:No such file or directory` error when query, [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/numeric-functions/truncate) and cpimport collided. ([MCOL-3251](https://jira.mariadb.org/browse/MCOL-3251))
* Fixes internal error IDB-2035 to [BIT_OR()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/aggregate-functions/bit_or) function in projection and subquery. ([MCOL-3356](https://jira.mariadb.org/browse/MCOL-3356))
* Fixes wrong minimum and maximum values after cpimport causing wrong [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select) statement results. ([MCOL-3716](https://jira.mariadb.org/browse/MCOL-3716))
* Fixes truncation during updates causing the Server to assert. ([MCOL-3749](https://jira.mariadb.org/browse/MCOL-3749))
* Fixes [RAND()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/numeric-functions/rand) function returning different results in 1.4 compared to 1.2. ([MCOL-3760](https://jira.mariadb.org/browse/MCOL-3760))
* Fixes issue where the same erroneous statement returns a different error other run. ([MCOL-3777](https://jira.mariadb.org/browse/MCOL-3777))
* Fixes `GROUP BY` ordering error: `IDB-2021: 'ref_genome' is not in GROUP BY clause` ([MCOL-3782](https://jira.mariadb.org/browse/MCOL-3782))
* Fixes MariaDB asserts when connection is closed. ([MCOL-3812](https://jira.mariadb.org/browse/MCOL-3812))
* Fixes incorrect counts in views. ([MCOL-3813](https://jira.mariadb.org/browse/MCOL-3813))
* Fixes issue in `UNION` operations about table not being in query. ([MCOL-3828](https://jira.mariadb.org/browse/MCOL-3828))
* Fixes issue where `systemctl cat mariadb.service` is not working on all systems. ([MCOL-3830](https://jira.mariadb.org/browse/MCOL-3830))
* Optimizes `execute()` of `regr_sxx`, `regr-sxy`, and `regr_syy` ([MCOL-3837](https://jira.mariadb.org/browse/MCOL-3837))
* Fixes [COUNT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/aggregate-functions/count) as window function not working with `NULL` values. ([MCOL-3839](https://jira.mariadb.org/browse/MCOL-3839))
* Fixes Server aborting when `Columnstore.xml` is missing. ([MCOL-3853](https://jira.mariadb.org/browse/MCOL-3853))
* Fixes [COUNT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/aggregate-functions/count) with distinct and 2 columns failing on every other execution. ([MCOL-3857](https://jira.mariadb.org/browse/MCOL-3857))
* Fixes `vTpch22.sql` hanging. ([MCOL-3858](https://jira.mariadb.org/browse/MCOL-3858))
* Fixes issue where renaming table causes schema to go out of sync. ([MCOL-3859](https://jira.mariadb.org/browse/MCOL-3859))
* Fixes errors raised by every other run of the `EXPLAIN` statement. ([MCOL-3860](https://jira.mariadb.org/browse/MCOL-3860))
* Fixes `fatalHandler` usage. ([MCOL-3864](https://jira.mariadb.org/browse/MCOL-3864))
* Fixes intermittent cpimport crashes. ([MCOL-3865](https://jira.mariadb.org/browse/MCOL-3865))
* Fixes `bug3333.sql` mismatch. ([MCOL-3894](https://jira.mariadb.org/browse/MCOL-3894))
* Fixes fails in `Group_concat` in `ORDER BY` with `long double` ([MCOL-3904](https://jira.mariadb.org/browse/MCOL-3904))
* Fixes error message pointing to wrong function. ([MCOL-3924](https://jira.mariadb.org/browse/MCOL-3924))
* Fixes memory leak in XML parser. ([MCOL-3934](https://jira.mariadb.org/browse/MCOL-3934))
* Fixes [IF()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/programming-customizing-mariadb/programmatic-compound-statements/if) function returning incorrect results when using hex constant. ([MCOL-3949](https://jira.mariadb.org/browse/MCOL-3949))
* Fixes microsecond support for [FROM_UNIXTIME()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/from_unixtime) function. ([MCOL-3959](https://jira.mariadb.org/browse/MCOL-3959))
* Fixes issue with single [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert) after a LDI in a transaction. ([MCOL-4002](https://jira.mariadb.org/browse/MCOL-4002))
* Fixes issue using $HOME in `storagemanager.cnf` variable. ([MCOL-4014](https://jira.mariadb.org/browse/MCOL-4014))
* Fixes mishandling of multi-byte characters in DML export to cpimport-1.5. ([MCOL-4017](https://jira.mariadb.org/browse/MCOL-4017))
* Fixes window function issues due to 1.4 returning results where 1.2 returns errors. ([MCOL-3856](https://jira.mariadb.org/browse/MCOL-3856))
* Fixes cpimport S3 multi-PM usage. ([MCOL-3861](https://jira.mariadb.org/browse/MCOL-3861))

## Platforms

In alignment to the MariaDB Corporation Engineering Policy, MariaDB Enterprise ColumnStore 1.5.3 is provided for:

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

**Note:** MariaDB Enterprise ColumnStore 1.5 has been superseded by MariaDB Enterprise ColumnStore 5 in MariaDB Enterprise Server 10.5.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
