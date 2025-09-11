# MariaDB ColumnStore 1.2.3 GA Release Notes

**Release date:** 21st March 2019

[MariaDB ColumnStore 1.2.3](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a GA release of MariaDB ColumnStore. The MariaDB ColumnStore 1.2 series provides several new features and improvements over the MariaDB ColumnStore 1.1 release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-2218](https://jira.mariadb.org/browse/MCOL-2218) - The base MariaDB server version is now [10.3.13](../../../community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes.md) which include several maintenance and security fixes.
* [MCOL-2176](https://jira.mariadb.org/browse/MCOL-2176) - Jemalloc is a new dependency for MariaDB ColumnStore.
* [MCOL-1822](https://jira.mariadb.org/browse/MCOL-1822) - The maximum possible value for AVG() and SUM() has significantly increased due to the usage of long double.

## Bugs and issues fixed

* [MCOL-901](https://jira.mariadb.org/browse/MCOL-901) - group\_concat() consumes a great amount of memory
* [MCOL-1456](https://jira.mariadb.org/browse/MCOL-1456) - Query doesn't try REDO\_PHASE1
* [MCOL-1559](https://jira.mariadb.org/browse/MCOL-1559) - Regression on working\_tpch1/misc/bug3669 string pad compare not correct
* [MCOL-1607](https://jira.mariadb.org/browse/MCOL-1607) - postConfigure must support hostnames as cluster nodes network endpoints.
* [MCOL-1637](https://jira.mariadb.org/browse/MCOL-1637) - [MCOL-1052](https://jira.mariadb.org/browse/MCOL-1052) causes regression
* [MCOL-1662](https://jira.mariadb.org/browse/MCOL-1662) - WriteEngine bulk methods do not version dictionaries correctly
* [MCOL-1702](https://jira.mariadb.org/browse/MCOL-1702) - Joblist thread pool leaks if mariadb client connection drops its connection early.
* [MCOL-1726](https://jira.mariadb.org/browse/MCOL-1726) - mcsapi stale transactions
* [MCOL-1741](https://jira.mariadb.org/browse/MCOL-1741) - Debian 9 - data-adapter package dependencies broken
* [MCOL-1755](https://jira.mariadb.org/browse/MCOL-1755) - Informatica: delete statement doesn't escape reserved names for column names
* [MCOL-1795](https://jira.mariadb.org/browse/MCOL-1795) - Remote Cpimport / API: Text overlaps MariaDB logo in installer windows
* [MCOL-1797](https://jira.mariadb.org/browse/MCOL-1797) - resumedatabasewrites causes both DDL/DML to go active on um1/um2
* [MCOL-1829](https://jira.mariadb.org/browse/MCOL-1829) - Output of 'select \* (with order by limit) queries' returns unexpected result
* [MCOL-1883](https://jira.mariadb.org/browse/MCOL-1883) - RENAME crashes when tablename contains `/` symbol
* [MCOL-1890](https://jira.mariadb.org/browse/MCOL-1890) - Deb package name change broken
* [MCOL-1945](https://jira.mariadb.org/browse/MCOL-1945) - mxs\_adapter throws malloc error
* [MCOL-1980](https://jira.mariadb.org/browse/MCOL-1980) - javamcsapi's shared library gets generated with the version number appended twice
* [MCOL-1981](https://jira.mariadb.org/browse/MCOL-1981) - regr\_avgx and regr\_avgy should return NULL if count is zero
* [MCOL-1983](https://jira.mariadb.org/browse/MCOL-1983) - regr\_intercept, regr\_r2, regr\_slope and possibly other regr functions should return NULL with only one row.
* [MCOL-1995](https://jira.mariadb.org/browse/MCOL-1995) - javamcsapi - MillionRow test fails on Ubuntu 16.04 and 18.04
* [MCOL-2009](https://jira.mariadb.org/browse/MCOL-2009) - Fix jobstep abort
* [MCOL-2018](https://jira.mariadb.org/browse/MCOL-2018) - Dictionary null comparison check can crash
* [MCOL-2050](https://jira.mariadb.org/browse/MCOL-2050) - ORDER BY with OFFSET in subquery produces random and incorrect result
* [MCOL-2052](https://jira.mariadb.org/browse/MCOL-2052) - IS.columnstore\_files maximum contains incorrect number of records for any relation.
* [MCOL-2062](https://jira.mariadb.org/browse/MCOL-2062) - cpimport scientific notation conversion problem
* [MCOL-2070](https://jira.mariadb.org/browse/MCOL-2070) - pentaho kettle adapter lock session with bulk columnstore and dml transaction(delete/update operation).
* [MCOL-2071](https://jira.mariadb.org/browse/MCOL-2071) - PDI CS Bulk Load plugin not able to read transformations with empty configuration
* [MCOL-2165](https://jira.mariadb.org/browse/MCOL-2165) - Autoswitch broken in some cases in 1.2.2
* [MCOL-2180](https://jira.mariadb.org/browse/MCOL-2180) - UDAF docs are currently broken
* [MCOL-2182](https://jira.mariadb.org/browse/MCOL-2182) - PrimProc crash - signal 11, Segmentation fault - funcexp::Func\_lpad::getStrVal
* [MCOL-1688](https://jira.mariadb.org/browse/MCOL-1688) - Informatica PowerCenter Bulk Write Connector
* [MCOL-1814](https://jira.mariadb.org/browse/MCOL-1814) - Add Windows builder to buildbot for Kettle
* [MCOL-1815](https://jira.mariadb.org/browse/MCOL-1815) - Add Windows builder to buildbot for mcsimport
* [MCOL-1822](https://jira.mariadb.org/browse/MCOL-1822) - Change the default to use double when overflow occurs in SUM() and AVG()
* [MCOL-1897](https://jira.mariadb.org/browse/MCOL-1897) - Add API test suite to buildbot
* [MCOL-1898](https://jira.mariadb.org/browse/MCOL-1898) - Add data-adapters test suite to buildbot
* [MCOL-1899](https://jira.mariadb.org/browse/MCOL-1899) - Add tools test suite to buildbot
* [MCOL-1961](https://jira.mariadb.org/browse/MCOL-1961) - javamcsapi, pymcsapi known isTableLock and TableLockInfo limitations
* [MCOL-2082](https://jira.mariadb.org/browse/MCOL-2082) - Write Spark and PySpark documentation for mcsapi
* [MCOL-2110](https://jira.mariadb.org/browse/MCOL-2110) - Cant build engine out-of-source
* [MCOL-2120](https://jira.mariadb.org/browse/MCOL-2120) - Check NUMA devel package is installed on BuildBot instances
* [MCOL-2176](https://jira.mariadb.org/browse/MCOL-2176) - Use jemalloc as the main memory allocator - testing for 1.2.3-1
* [MCOL-2218](https://jira.mariadb.org/browse/MCOL-2218) - Rebase 1.2 on [MariaDB 10.3.13](../../../community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes.md)

In addition, all bugs fixed in MariaDB ColumnStore 1.2.2 and earlier are implicitly included in this release.

## Upgrade

The following procedure outlines upgrading a 1.1.7 ColumnStore install to 1.2.3:

* [1.1.7 GA to 1.2.3 GA upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md)

Multi version upgrades generally will work using the same procedure however we can't test every possible permutation so you should test your specific scenario outside of production first if you wish to try this (and this is good practice regardless).

## Known issues and limitations

There are a number bugs and known limitations within this version of MariaDB ColumnStore, the most serious of these are listed below.

* [MCOL-1990](https://jira.mariadb.org/browse/MCOL-1990) - localquery mode tries to turn on replication and fails.
* [MCOL-2061](https://jira.mariadb.org/browse/MCOL-2061) - Running TRUNCATE on a table that has been upgraded from 1.1 -> 1.2 can cause MariaDB server to crash. As a workaround you can DROP and recreate the table.

## Documentation

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md)

## Packaging

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.2.3 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8, Debian 9, RedHat 6, RedHat 7, SUSE 12, Ubuntu 16.04 and Ubuntu 18.04.
* Packages can be downloaded [here](https://mariadb.com/downloads/mariadb-ax) or can be installed from the [repositories](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md).
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.2.3". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.2.3)
* MariaDB Server - [Source code based on MariaDB Server 10.3.13 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.2.3)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools/tree/columnstore-1.2.3)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api/tree/columnstore-1.2.3)
* MaxScale CDC and Kafka Data Adapters - [Source Code for data adapters](https://github.com/mariadb-corporation/mariadb-columnstore-data-adapters/tree/columnstore-1.2.3)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
