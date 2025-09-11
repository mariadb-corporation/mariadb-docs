# MariaDB ColumnStore 1.1.7 GA Release Notes

**Release date:** 21st February 2019

[MariaDB ColumnStore 1.1.7](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) is a GA release of MariaDB ColumnStore. This is the fourth release of the MariaDB ColumnStore 1.1 series. This release of MariaDB ColumnStore provides improvements over the previous 1.1.6 GA release.

MariaDB ColumnStore 1.1.7 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-2158](https://jira.mariadb.org/browse/MCOL-2158) - The base MariaDB server version is now [10.2.22](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes.md) which include several maintenance and security fixes.
* [MCOL-2136](https://jira.mariadb.org/browse/MCOL-2136) - Use jemalloc as the main memory allocator. Please ensure jemalloc is installed on each ColumnStore node prior to installation or upgrade.

## Bugs and issues fixed

* [MCOL-1183](https://jira.mariadb.org/browse/MCOL-1183) - Incorrectly formatted file can cause cpimport to crash and leave behind locks
* [MCOL-1188](https://jira.mariadb.org/browse/MCOL-1188) - assertion 'fColumn.get() && fSub && fFunc' failed , caused lost connection to MySQL server during query and crash of mysql
* [MCOL-1307](https://jira.mariadb.org/browse/MCOL-1307) - Adapter can't recognize database schema written with backtick
* [MCOL-1322](https://jira.mariadb.org/browse/MCOL-1322) - data corruption when setting NUMERIC columns to NULL through the python and C++ API
* [MCOL-1347](https://jira.mariadb.org/browse/MCOL-1347) - ALTER TABLE ADD COLUMN creates a column with incorrect width for a varchar columns.
* [MCOL-1459](https://jira.mariadb.org/browse/MCOL-1459) - CDC adapter: Name of the cpio file is different from the name of rpm package
* [MCOL-1505](https://jira.mariadb.org/browse/MCOL-1505) - ExeMgr can crash in cleanTmpDir()
* [MCOL-1507](https://jira.mariadb.org/browse/MCOL-1507) - ExeMgr over using memory causing swap and system restarts to occur
* [MCOL-1523](https://jira.mariadb.org/browse/MCOL-1523) - OAM Process failover logic for DDLproc is incorrect - causing DDL to stop working
* [MCOL-1554](https://jira.mariadb.org/browse/MCOL-1554) - PDI CS not work in the Pentaho Sever repository
* [MCOL-1563](https://jira.mariadb.org/browse/MCOL-1563) - Data corruption when inserting out-of-bounds data
* [MCOL-1606](https://jira.mariadb.org/browse/MCOL-1606) - PDI 8 - variable substitution doesn't work
* [MCOL-1643](https://jira.mariadb.org/browse/MCOL-1643) - PDI plugin CI tests - minor changes in redme file are needed
* [MCOL-1648](https://jira.mariadb.org/browse/MCOL-1648) - pymcsapi3 on Windows depends on the Python 3 release DLL it was compiled with
* [MCOL-1654](https://jira.mariadb.org/browse/MCOL-1654) - Querystats table is broken
* [MCOL-1658](https://jira.mariadb.org/browse/MCOL-1658) - support space names in columnstore table column names
* [MCOL-1659](https://jira.mariadb.org/browse/MCOL-1659) - Unable to have spaces in column names in ddl
* [MCOL-1660](https://jira.mariadb.org/browse/MCOL-1660) - Table naming does not allow for spaces
* [MCOL-1662](https://jira.mariadb.org/browse/MCOL-1662) - WriteEngine bulk methods do not version dictionaries correctly
* [MCOL-1676](https://jira.mariadb.org/browse/MCOL-1676) - AVG as Window function with OVER(sort by) gives bad answer.
* [MCOL-1694](https://jira.mariadb.org/browse/MCOL-1694) - Add better logging for uncaught exceptions in DDLProc/DMLProc
* [MCOL-1695](https://jira.mariadb.org/browse/MCOL-1695) - Add OS information to Kettle zip file
* [MCOL-1701](https://jira.mariadb.org/browse/MCOL-1701) - Change Windows mcsapi build to use libraries from external directory
* [MCOL-1702](https://jira.mariadb.org/browse/MCOL-1702) - Joblist thread pool leaks if mariadb client connection drops its connection early.
* [MCOL-1704](https://jira.mariadb.org/browse/MCOL-1704) - javamcsapi - compatibility test fails if executed multiple times
* [MCOL-1709](https://jira.mariadb.org/browse/MCOL-1709) - DDL for creation of a new table in columnstore produces syntax error when it runs on columnstore
* [MCOL-1720](https://jira.mariadb.org/browse/MCOL-1720) - ColumnStoreDateTime(dateTime, format) can not be initialized on Debian 9
* [MCOL-1726](https://jira.mariadb.org/browse/MCOL-1726) - mcsapi stale transactions
* [MCOL-1746](https://jira.mariadb.org/browse/MCOL-1746) - Error while connecting to the MariadDB maxscale with tx
* [MCOL-1750](https://jira.mariadb.org/browse/MCOL-1750) - Thread stack memory leak in ThreadPool
* [MCOL-1761](https://jira.mariadb.org/browse/MCOL-1761) - Test script for Win is searching for wrong named zip file
* [MCOL-1766](https://jira.mariadb.org/browse/MCOL-1766) - Increase Gradle dependency resolution timeout to 5min
* [MCOL-1797](https://jira.mariadb.org/browse/MCOL-1797) - resumedatabasewrites causes both DDL/DML to go active on um1/um2
* [MCOL-1810](https://jira.mariadb.org/browse/MCOL-1810) - setConfig can hang on low core count
* [MCOL-1826](https://jira.mariadb.org/browse/MCOL-1826) - PrimProc crash in float/double to string conversion
* [MCOL-1829](https://jira.mariadb.org/browse/MCOL-1829) - Output of 'select \* (with order by limit) queries' returns unexpected result
* [MCOL-1852](https://jira.mariadb.org/browse/MCOL-1852) - Spark Exporter uses collect() instead of toLocalIterator() on DataFrames to export and therefore uses too much memory on the Driver
* [MCOL-1868](https://jira.mariadb.org/browse/MCOL-1868) - func\_concat\_ws type
* [MCOL-1887](https://jira.mariadb.org/browse/MCOL-1887) - PDI Kettle Plugin help page
* [MCOL-1945](https://jira.mariadb.org/browse/MCOL-1945) - mxs\_adapter throws malloc error
* [MCOL-1947](https://jira.mariadb.org/browse/MCOL-1947) - Our aliases break BASH
* [MCOL-2007](https://jira.mariadb.org/browse/MCOL-2007) - Add git version information to builds
* [MCOL-2009](https://jira.mariadb.org/browse/MCOL-2009) - Fix jobstep abort
* [MCOL-2018](https://jira.mariadb.org/browse/MCOL-2018) - Dictionary null comparison check can crash
* [MCOL-2052](https://jira.mariadb.org/browse/MCOL-2052) - IS.columnstore\_files maximum contains incorrect number of records for any relation.
* [MCOL-2062](https://jira.mariadb.org/browse/MCOL-2062) - cpimport scientific notation conversion problem
* [MCOL-2070](https://jira.mariadb.org/browse/MCOL-2070) - pentaho kettle adapter lock session with bulk columnstore and dml transaction(delete/update operation).
* [MCOL-2071](https://jira.mariadb.org/browse/MCOL-2071) - PDI CS Bulk Load plugin not able to read transformations with empty configuration
* [MCOL-2136](https://jira.mariadb.org/browse/MCOL-2136) - Use jemalloc as the main memory allocator
* [MCOL-1633](https://jira.mariadb.org/browse/MCOL-1633) - mcsapi Windows - add needed Windows Redistributables to installer
* [MCOL-1644](https://jira.mariadb.org/browse/MCOL-1644) - PDI plugin CI tests - add check with PDI 8
* [MCOL-1670](https://jira.mariadb.org/browse/MCOL-1670) - Windows mcsapi - add option to install libraries directly into Python
* [MCOL-1671](https://jira.mariadb.org/browse/MCOL-1671) - Windows mcsapi - add option to install libraries directly into Java
* [MCOL-1698](https://jira.mariadb.org/browse/MCOL-1698) - Add Distinct capability to specific UDAnF Window Functions
* [MCOL-1340](https://jira.mariadb.org/browse/MCOL-1340) - Remove dpkg purge from docs
* [MCOL-1634](https://jira.mariadb.org/browse/MCOL-1634) - Include Windows library build into mcsapi
* [MCOL-1713](https://jira.mariadb.org/browse/MCOL-1713) - Add Windows suffix to kettle data adapter
* [MCOL-1743](https://jira.mariadb.org/browse/MCOL-1743) - Documentation issue in repoinstallation of columnstore-kafka-adapter
* [MCOL-1744](https://jira.mariadb.org/browse/MCOL-1744) - Remove unnecessary CentOS 7 mcsapi package dependencies
* [MCOL-1754](https://jira.mariadb.org/browse/MCOL-1754) - Change libmysql dependency for Windows api tests to libmariadb
* [MCOL-1974](https://jira.mariadb.org/browse/MCOL-1974) - Bug verification for [MCOL-1844](https://jira.mariadb.org/browse/MCOL-1844) for 1.1.7 and 1.0.16
* [MCOL-2005](https://jira.mariadb.org/browse/MCOL-2005) - Merge [MariaDB 10.2.21](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10221-release-notes.md) into develop-1.1
* [MCOL-2107](https://jira.mariadb.org/browse/MCOL-2107) - execute tpc-ds performance test suite on dev v1.1.7 with purpose of regression performance testing
* [MCOL-2120](https://jira.mariadb.org/browse/MCOL-2120) - Check NUMA devel package is installed on BuildBot instances
* [MCOL-2158](https://jira.mariadb.org/browse/MCOL-2158) - Merge [MariaDB 10.2.22](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes.md)

In addition, all bugs fixed in MariaDB ColumnStore 1.1.6 and earlier are implicitly included in this release.

## Upgrade

The following procedure outlines upgrading a 1.1.6 ColumnStore install to 1.1.7:

* [1.1.6 GA to 1.1.7 GA upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md)

Multi version upgrades generally will work using the same procedure however we can't test every possible permutation so you should test your specific scenario outside of production first if you wish to try this (and this is good practice regardless).

## Known issues and limitations

There are a number bugs and known limitations within this version of MariaDB ColumnStore, the most serious of these are listed below.

* [MCOL-271](https://jira.mariadb.org/browse/MCOL-271) empty string values are treated as NULL. This means you cannot insert empty values into a NOT NULL string column.
* [MCOL-365](https://jira.mariadb.org/browse/MCOL-365): Log files created by load data infile remain in the bulk/data/log and /tmp directories. If storage is a concern these can safely be removed.
* [MCOL-540](https://jira.mariadb.org/browse/MCOL-540) : In a non root Ubuntu install with local query enabled, the PM servers crash and restart on table creation.
* [MCOL-624](https://jira.mariadb.org/browse/MCOL-624) :[MariaDB 10.2](../../../community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) WF create MEDIAN, PERCENTILE\_CONT and PERCENTILE\_DISC Window functions. MariaDB ColumnStore 1.1 was rewritten to use the [MariaDB 10.2](../../../community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) server parser code which does not support the percentile window functions. This will be added in a later release. A median function has been provided instead as part of the User Defined Aggregate Function framework that provides similar functionality or can be adapted to support percentiles other than 0.5.
* [MCOL-631](https://jira.mariadb.org/browse/MCOL-631) :Create table caused primproc crashed for a specific configuration
* [MCOL-643](https://jira.mariadb.org/browse/MCOL-643) :Implement ha\_calpont\_impl\_rnd\_pos. Sorting of long text columns may fail.
* [MCOL-695](https://jira.mariadb.org/browse/MCOL-695) :Implement joins between CHAR/VARCHAR and INT columns. ColumnStore now fails more consistently on incompatible join types. Explicit type casts must be used if this error is hit.
* [MCOL-713](https://jira.mariadb.org/browse/MCOL-713) : Some functions return "The maximum row size" error when TEXT/LONGTEXT is used in a table
* [MCOL-1224](https://jira.mariadb.org/browse/MCOL-1224): post-install non-root has incorrect permissions for /etc/rc.local
* [MCOL-1225](https://jira.mariadb.org/browse/MCOL-1225): LD\_LIBRARY\_PATH not set correctly in centos6 non-root install
* /dev/shm may be set to 755 permissions prior to 1.1.6 which could cause problems with other non-root processes, from 1.1.6 onwards ColumnStore does not try to do this. You should change this to 777 if it is causing problems with your installation.
* The current logging default generates full verbose debug logs. This can be controlled by making logging configuration changes as described [here](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/management/columnstore-system/columnstore-system-monitoring-configuration).
* While Millisecond and Microsecond storage is supported for datetime, time and timestamp columns, at this time the query results cannot return millisecond and microseconds.
* UTF-8 Limitation
  * UTF-8 must be declared at the table level if the instance has been set up with a UTF-8 profile. Tables created with a non-matching character set will yield indeterminate results.
  * Viewing SQL output should be done using client software that supports UTF-8 character sets.
  * UTF-8 characters are not supported in object names.
* Known security issues and fixes are documented [here](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/security/columnstore-security-vulnerabilities).

## Documentation

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md)

## Packaging

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.1.7 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8, Debian 9, RedHat 6, RedHat 7, SUSE 12, Ubuntu 16.04 and Ubuntu 18.04.
* Packages can be downloaded [here](https://mariadb.com/downloads/mariadb-ax) or can be installed from the [repositories](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.1.7". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.1.7)
* MariaDB Server - [Source code based on MariaDB Server 10.2.15 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.1.7)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools/tree/columnstore-1.1.7)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api/tree/columnstore-1.1.7)
* MaxScale CDC and Kafka Data Adapters - [Source Code for data adapters](https://github.com/mariadb-corporation/mariadb-columnstore-data-adapters/tree/columnstore-1.1.7)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
