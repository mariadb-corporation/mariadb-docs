# MariaDB ColumnStore 1.4.4 Release Notes

## Overview

MariaDB ColumnStore is a columnar storage engine. This is the second GA release in the ColumnStore 1.4 series. This release contains new features and fixes, compared to MariaDB ColumnStore 1.4.3.

This release of MariaDB ColumnStore is included with [MariaDB Enterprise Server 10.4.13-7](../../../enterprise-server/old-releases/10-4/release-notes-for-mariadb-enterprise-server-10-4-13-7.md).

MariaDB ColumnStore 1.4.4 was released on 2020-06-08.

## Notable Changes

columnstore\_use\_import\_for\_batchinsert system variable option ALWAYS added to use cpimport for LOAD DATA LOCAL INFILE and INSERT .. SELECT regardless of whether the query runs in a transaction. This gives the user the ability to use a faster import method, with the caveat that if a user issues a rollback of the transaction, it will have no effect as the data would have already been committed to actual database files by cpimport. ([MCOL-4000](https://jira.mariadb.org/browse/MCOL-4000))

## Issues Fixed

### Can result in data loss

* [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) can modify incorrect data due to incorrect WHERE clause handling. ([MCOL-4023](https://jira.mariadb.org/browse/MCOL-4023))

### Can result in a hang or crash

* A hang may occur in `load_brm` on `dbroot1` failover. ([MCOL-3945](https://jira.mariadb.org/browse/MCOL-3945))
* [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) may be blocked by improper failover. ([MCOL-3999](https://jira.mariadb.org/browse/MCOL-3999))
* Crash may occur when using cpimport ([LOAD DATA LOCAL INFILE](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/mariadb-columnstore/reference/data-manipulation-statements/columnstore-load-data-infile)) to process data containing multi-byte characters. ([MCOL-4005](https://jira.mariadb.org/browse/MCOL-4005))
* Rollback may trigger crash of StorageManager. ([MCOL-4021](https://jira.mariadb.org/browse/MCOL-4021))
* PM failover and `movePmDbrootConfig` failure on CentOS 7 with glusterfs. ([MCOL-3842](https://jira.mariadb.org/browse/MCOL-3842))

### Can result in unexpected behavior

* [ORDER BY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/order-by) over negative `SEC_TO_TIME()` results produce an incorrect order. ([MCOL-3598](https://jira.mariadb.org/browse/MCOL-3598))
* Subqueries with ORDER and LIMIT may produce the wrong answer. ([MCOL-3747](https://jira.mariadb.org/browse/MCOL-3747))
* [IN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/operators/comparison-operators/in) clause in `WHERE` could be evaluated improperly. ([MCOL-2096](https://jira.mariadb.org/browse/MCOL-2096))
* Sub-query with [GROUP BY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/group-by) and [ORDER BY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/order-by) allows non-aggregates in projection. ([MCOL-2166](https://jira.mariadb.org/browse/MCOL-2166))
* `FILE001.cdf:No such file or directory` can occur when query, TRUNCATE and cpimport collide. ([MCOL-3251](https://jira.mariadb.org/browse/MCOL-3251))
* `Internal error: IDB-2035` can occur with BIT\_OR function in projection and subquery in FROM ([MCOL-3356](https://jira.mariadb.org/browse/MCOL-3356))
* Incorrect handling of `ORDER BY` can occur in some queries. ([MCOL-3485](https://jira.mariadb.org/browse/MCOL-3485))
* Unexpected syntax errors could be returned from window functions. ([MCOL-3580](https://jira.mariadb.org/browse/MCOL-3580))
* `Format(c1,0)` returns only sign, without a digit, on a decimal(1) field. ([MCOL-3595](https://jira.mariadb.org/browse/MCOL-3595))
* [TIMEDIFF()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/timediff) returns NULL instead of expected value. ([MCOL-3597](https://jira.mariadb.org/browse/MCOL-3597))
* `MODA()` and `REGR_` UDAFs are not properly created. ([MCOL-3599](https://jira.mariadb.org/browse/MCOL-3599))
* [BIT\_COUNT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bit_count), [CHARSET()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/charset), [UNHEX()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/unhex), and [MINUTE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/minute) functions did not exist. ([MCOL-3600](https://jira.mariadb.org/browse/MCOL-3600))
* `regr_` tests returns doubles with higher precision than in ColumnStore 1.2. ([MCOL-3631](https://jira.mariadb.org/browse/MCOL-3631))
* Window function failures could return results rather than errors. ([MCOL-3632](https://jira.mariadb.org/browse/MCOL-3632))
* `ISTRUE()` function did not exist. ([MCOL-3756](https://jira.mariadb.org/browse/MCOL-3756))
* Alternate behavior for `rand()` vs ColumnStore 1.2. ([MCOL-3760](https://jira.mariadb.org/browse/MCOL-3760))
* Wrong error could be returned on every second run of an error-generating query. ([MCOL-3777](https://jira.mariadb.org/browse/MCOL-3777))
* `Internal error: IDB-2021: 'tablename' is not in GROUP BY clause` could occur. ([MCOL-3782](https://jira.mariadb.org/browse/MCOL-3782))
* [UNION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/union) may complain about table not in query. ([MCOL-3828](https://jira.mariadb.org/browse/MCOL-3828))
* [COUNT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/aggregate-functions/count) as a window function does not work correctly with NULL values. ([MCOL-3839](https://jira.mariadb.org/browse/MCOL-3839))
* SQLYog may encounter an error during ColumnStore cross-engine JOINs. ([MCOL-3845](https://jira.mariadb.org/browse/MCOL-3845))
* [GROUP\_CONCAT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/aggregate-functions/group_concat) with `ORDER BY` and long doubles may fail. ([MCOL-3904](https://jira.mariadb.org/browse/MCOL-3904))
* Error messages may point to the wrong function. ([MCOL-3924](https://jira.mariadb.org/browse/MCOL-3924))
* Microsecond support for [FROM\_UNIXTIME()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/from_unixtime) ([MCOL-3959](https://jira.mariadb.org/browse/MCOL-3959))
* [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert) after a `LOAD DATA LOCAL INFILE` in a transaction may silently fail. ([MCOL-4002](https://jira.mariadb.org/browse/MCOL-4002))
* Unsupported `LIMIT` in correlated subqueries may give erroneous result. ([MCOL-3757](https://jira.mariadb.org/browse/MCOL-3757))

### Related to performance

* Subquery wrapping impacts performance. ([MCOL-3664](https://jira.mariadb.org/browse/MCOL-3664))
* Unoptimized lines (CPU impact and unnecessary rounding error) in `regr_sxx`, `regr-sxy`, and `regr_syy` ([MCOL-3837](https://jira.mariadb.org/browse/MCOL-3837))

### Related to install and upgrade

* `postConfigure` uses invalid device nodes for dbroots. ([MCOL-2022](https://jira.mariadb.org/browse/MCOL-2022))
* `startsystem` allows startup without correct DBROOT 1 assignment. ([MCOL-2153](https://jira.mariadb.org/browse/MCOL-2153))
* Incorrect handling of unassigned IP addresses in configuration file. ([MCOL-2181](https://jira.mariadb.org/browse/MCOL-2181))
* After `shutdownsystem`, first `startsystem` always fails. ([MCOL-3704](https://jira.mariadb.org/browse/MCOL-3704))
* ColumnStore Tools for 1.4 were unavailable. ([MCOL-3847](https://jira.mariadb.org/browse/MCOL-3847))
* `postConfigure` reports false positive that server is running. ([MCOL-3870](https://jira.mariadb.org/browse/MCOL-3870))
* `postConfigure` looks in incorrect location for `columnstore.cnf.rpmsave` during an upgrade. ([MCOL-3887](https://jira.mariadb.org/browse/MCOL-3887))
* Multi-node non-systemd installation with replication enabled fails to start. ([MCOL-3985](https://jira.mariadb.org/browse/MCOL-3985))
* `storagemanager.cnf` variable `$HOME` drew path from user's environment. `$HOME` now points to the current location of ColumnStore data. ([MCOL-4014](https://jira.mariadb.org/browse/MCOL-4014))
* Changing `systemlang` in `Columnstore.xml` to an unrecognized string will prevent ColumnStore startup. ([MCOL-3420](https://jira.mariadb.org/browse/MCOL-3420))

## Known Issues

* Built-in SQL functions do not work in ColumnStore when sql\_mode=ORACLE ([MCOL-4044](https://jira.mariadb.org/browse/MCOL-4044))

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
