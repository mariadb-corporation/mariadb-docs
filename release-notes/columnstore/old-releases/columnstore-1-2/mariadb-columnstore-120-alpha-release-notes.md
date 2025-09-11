# MariaDB ColumnStore 1.2.0 Alpha Release Notes

**Release date:** 17th October 2018

[MariaDB ColumnStore 1.2.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) is an Alpha release of MariaDB ColumnStore. This is the first release of the MariaDB ColumnStore 1.2 series. The MariaDB ColumnStore 1.2 series provides several new features and improvements over the MariaDB ColumnStore 1.1 release.

MariaDB ColumnStore 1.2.0 is a [_**Alpha**_](../../../community-server/about/release-criteria.md) release.

**Do not use&#x20;**_**alpha**_**&#x20;releases on production systems!**

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-1385](https://jira.mariadb.org/browse/MCOL-1385) - The base MariaDB server version is now [10.3.9](../../../community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1039-release-notes.md) which include several maintenance and security fixes.
* [MCOL-392](https://jira.mariadb.org/browse/MCOL-392) - TIME data type is [now supported](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/reference/columnstore-data-types)
* [MCOL-320](https://jira.mariadb.org/browse/MCOL-320) - TIME and DATETIME data types [now support microseconds](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/reference/columnstore-data-types)
* [MCOL-497](https://jira.mariadb.org/browse/MCOL-497) - Cross Engine Joins now support SSL connections
* Improved DDL syntax support
  * [MCOL-497](https://jira.mariadb.org/browse/MCOL-497) - BOOL / BOOLEAN alias for TINYINT [now supported](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/reference/columnstore-data-types) - with thanks to community contributor "tntnatbry"
  * [MCOL-573](https://jira.mariadb.org/browse/MCOL-573) - Backticks & reserved words now supported
  * [MCOL-716](https://jira.mariadb.org/browse/MCOL-716) - Non-alphanumeric table/column names now supported
* [MCOL-1201](https://jira.mariadb.org/browse/MCOL-1201) - User Defined Aggregate / Window Functions now support multiple parameters.
* [MCOL-521](https://jira.mariadb.org/browse/MCOL-521) - [Regression aggregate](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/reference/columnstore-distributed-aggregate-functions) and [windows functions](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/reference/columnstore-window-functions) are now supported.
* [MCOL-1577](https://jira.mariadb.org/browse/MCOL-1577) - CREATE TABLE...LIKE [now supported](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/reference/data-definition-statements/columnstore-create-table)
* [MCOL-1242](https://jira.mariadb.org/browse/MCOL-1242) - A [remote bulk data import tool](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md) is now available which allows loading data directly from any server. This tool is included in the MariaDB ColumnStore Tools package
* [MCOL-1281](https://jira.mariadb.org/browse/MCOL-1281) - [Microsoft Windows 10](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md) support for bulk write SDK
* Pentaho data adapter is now also available for Windows 10

## Bugs and issues fixed

* [MCOL-1322](https://jira.mariadb.org/browse/MCOL-1322) - data corruption when setting NUMERIC columns to NULL through the python and C++ API
* [MCOL-1523](https://jira.mariadb.org/browse/MCOL-1523) - OAM Process failover logic for DDLproc is incorrect - causing DDL to stop working
* [MCOL-1606](https://jira.mariadb.org/browse/MCOL-1606) - PDI 8 - variable substitution doesn't work
* [MCOL-1648](https://jira.mariadb.org/browse/MCOL-1648) - pymcsapi3 on Windows depends on the Python 3 release DLL it was compiled with
* [MCOL-1658](https://jira.mariadb.org/browse/MCOL-1658) - support space names in columnstore table column names
* [MCOL-1701](https://jira.mariadb.org/browse/MCOL-1701) - Change Windows mcsapi build to use libraries from external directory
* [MCOL-1644](https://jira.mariadb.org/browse/MCOL-1644) - PDI plugin CI tests - add check with PDI 8
* [MCOL-1704](https://jira.mariadb.org/browse/MCOL-1704) - javamcsapi - compatibility test fails if executed multiple times
* [MCOL-1761](https://jira.mariadb.org/browse/MCOL-1761) - Test script for Win is searching for wrong named zip file
* [MCOL-1766](https://jira.mariadb.org/browse/MCOL-1766) - Increase Gradle dependency resolution timeout to 5min
* [MCOL-1695](https://jira.mariadb.org/browse/MCOL-1695) - Add OS information to Kettle zip file
* [MCOL-1713](https://jira.mariadb.org/browse/MCOL-1713) - Add Windows suffix to kettle data adapter
* [MCOL-345](https://jira.mariadb.org/browse/MCOL-345) - Saturated time() func handling is different to MariaDB
* [MCOL-346](https://jira.mariadb.org/browse/MCOL-346) - Saturated addtime() func handling is different to MariaDB
* [MCOL-573](https://jira.mariadb.org/browse/MCOL-573) - CS does not support reserved words as column names
* [MCOL-807](https://jira.mariadb.org/browse/MCOL-807) - HOUR() function returns NULL when it should not
* [MCOL-876](https://jira.mariadb.org/browse/MCOL-876) - Renaming a table in non-current database fails
* [MCOL-1002](https://jira.mariadb.org/browse/MCOL-1002) - cpimport with down system say InfiniDB
* [MCOL-1219](https://jira.mariadb.org/browse/MCOL-1219) - Column name can not start with numeric value
* [MCOL-1322](https://jira.mariadb.org/browse/MCOL-1322) - data corruption when setting NUMERIC columns to NULL through the python and C++ API
* [MCOL-1327](https://jira.mariadb.org/browse/MCOL-1327) - CS objects' identifiers doesn't support U+0000..U+007f even when quoted
* [MCOL-1377](https://jira.mariadb.org/browse/MCOL-1377) - ColumnStore system logging not working after 1.1.4 ubuntu-16 install
* [MCOL-1379](https://jira.mariadb.org/browse/MCOL-1379) - Scala connector won't compile in Ubuntu 18.04
* [MCOL-1386](https://jira.mariadb.org/browse/MCOL-1386) - Create table statement doesn't allow usage of C style comments in it
* [MCOL-1520](https://jira.mariadb.org/browse/MCOL-1520) - Forked server crashes in Item\_ident::print() for a Temptable\_field.
* [MCOL-1684](https://jira.mariadb.org/browse/MCOL-1684) - Performance Schema crashes prepared statement
* [MCOL-1701](https://jira.mariadb.org/browse/MCOL-1701) - Change Windows mcsapi build to use libraries from external directory
* [MCOL-1766](https://jira.mariadb.org/browse/MCOL-1766) - Increase Gradle dependency resolution timeout to 5min
* [MCOL-266](https://jira.mariadb.org/browse/MCOL-266) - BOOLEAN data type not supported
* [MCOL-320](https://jira.mariadb.org/browse/MCOL-320) - support query of milli and micro second time parts
* [MCOL-392](https://jira.mariadb.org/browse/MCOL-392) - TIME datatype is not supported
* [MCOL-497](https://jira.mariadb.org/browse/MCOL-497) - support ssl connection in cross engine joins
* [MCOL-521](https://jira.mariadb.org/browse/MCOL-521) - add distributed regression aggregate and window functions
* [MCOL-548](https://jira.mariadb.org/browse/MCOL-548) - clean up engine repo cmake warnings
* [MCOL-569](https://jira.mariadb.org/browse/MCOL-569) - CS does not support reserved words as table names
* [MCOL-716](https://jira.mariadb.org/browse/MCOL-716) - support non alphanumeric characters for table and column names
* [MCOL-978](https://jira.mariadb.org/browse/MCOL-978) - Disable Query Cache for ColumnStore
* [MCOL-1052](https://jira.mariadb.org/browse/MCOL-1052) - Implement GROUP BY pushdown support
* [MCOL-1073](https://jira.mariadb.org/browse/MCOL-1073) - DecomSvr should be removed
* [MCOL-1201](https://jira.mariadb.org/browse/MCOL-1201) - Allow UDAnF to have multiple parameters defined.
* [MCOL-1242](https://jira.mariadb.org/browse/MCOL-1242) - Remote CpImport
* [MCOL-1244](https://jira.mariadb.org/browse/MCOL-1244) - make postConfigure default install non-distributed
* [MCOL-1281](https://jira.mariadb.org/browse/MCOL-1281) - mcsapi Windows support
* [MCOL-1378](https://jira.mariadb.org/browse/MCOL-1378) - Hardening Flags pt 2
* [MCOL-1385](https://jira.mariadb.org/browse/MCOL-1385) - Merge [MariaDB 10.3](../../../community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md)
* [MCOL-1392](https://jira.mariadb.org/browse/MCOL-1392) - Add time field support for PDI plugin
* [MCOL-1424](https://jira.mariadb.org/browse/MCOL-1424) - Make the default installation option to separate instead of combined.
* [MCOL-1577](https://jira.mariadb.org/browse/MCOL-1577) - ColumnStore to allow CREATE TABLE table\_name LIKE ... Syntax
* [MCOL-1633](https://jira.mariadb.org/browse/MCOL-1633) - mcsapi Windows - add needed Windows Redistributables to installer
* [MCOL-1688](https://jira.mariadb.org/browse/MCOL-1688) - Informatica PowerCenter Bulk Write Connector
* [MCOL-1759](https://jira.mariadb.org/browse/MCOL-1759) - Implement regr\_sxx, regr\_syy, regr\_sxy and corr functions as UDAF
* [MCOL-1773](https://jira.mariadb.org/browse/MCOL-1773) - Add mcsimport to PATH
* [MCOL-1547](https://jira.mariadb.org/browse/MCOL-1547) - Investigate renewed in 10.3 CASE implementation.
* [MCOL-1634](https://jira.mariadb.org/browse/MCOL-1634) - Include Windows library build into mcsapi
* [MCOL-1417](https://jira.mariadb.org/browse/MCOL-1417) - TIME: cpimort saturates reserved NULL and empty indicator values incorrectly
* [MCOL-1418](https://jira.mariadb.org/browse/MCOL-1418) - TIME: LDI saturates out-of-range values incorrectly
* [MCOL-1419](https://jira.mariadb.org/browse/MCOL-1419) - TIME: Update saturates out-of-range values incorrectly
* [MCOL-1427](https://jira.mariadb.org/browse/MCOL-1427) - Microsecond values are stored left-justified with trailing 0 padding
* [MCOL-1428](https://jira.mariadb.org/browse/MCOL-1428) - SUBTIME() as a WHERE condition on TIME data type caused primProc to hang
* [MCOL-1429](https://jira.mariadb.org/browse/MCOL-1429) - DAYNAME() and MONTHNAME() on TIME data type columns caused primProc to restart
* [MCOL-1433](https://jira.mariadb.org/browse/MCOL-1433) - Some functions return non-matching results after data type TIME was added to the functions test suite
* [MCOL-1496](https://jira.mariadb.org/browse/MCOL-1496) - Joiner array boundary bug

In addition, all bugs fixed in MariaDB ColumnStore 1.1.6 and earlier are implicitly included in this release.

## Upgrade

The following procedure outlines upgrading a 1.1.6 ColumnStore install to 1.2.0:

* [1.1.6 GA to 1.2.0 Alpha upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md)

Multi version upgrades generally will work using the same procedure however we can't test every possible permutation so you should test your specific scenario outside of production first if you wish to try this (and this is good practice regardless).

## Known issues and limitations

There are a number bugs and known limitations within this version of MariaDB ColumnStore, the most serious of these are listed below.

* [MCOL-1763](https://jira.mariadb.org/browse/MCOL-1763) - mcsapi [MCOL-1408](https://jira.mariadb.org/browse/MCOL-1408) regression
* [MCOL-1776](https://jira.mariadb.org/browse/MCOL-1776) - regression of [MCOL-1403](https://jira.mariadb.org/browse/MCOL-1403), trailing space string matching in VARCHAR
* [MCOL-1782](https://jira.mariadb.org/browse/MCOL-1782) - UPDATE and DELETE reported incorrect affected row count
* [MCOL-1792](https://jira.mariadb.org/browse/MCOL-1792) - mcsapi can incorrectly insert milliseconds
* [MCOL-1799](https://jira.mariadb.org/browse/MCOL-1799) - length() on BLOB data generates an error
* [MCOL-1786](https://jira.mariadb.org/browse/MCOL-1786) - cpimport cannot handle "true" keyword for boolean/numeric data types in cpimport
* [MCOL-1805](https://jira.mariadb.org/browse/MCOL-1805) - mcimport can show a warning about column sizes during import

## Documentation

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md)

## Packaging

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.2.0 Alpha version.

* The supported OS for the Alpha version are CentOS 6, CentOS 7, Debian 8, Debian 9, RedHat 6, RedHat 7, SUSE 12, Ubuntu 16.04 and Ubuntu 18.04.
* Packages can be downloaded [here](https://mariadb.com/downloads/mariadb-ax) or can be installed from the [repositories](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md).
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.2.0". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.2.0)
* MariaDB Server - [Source code based on MariaDB Server 10.3.9 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.2.0)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools/tree/columnstore-1.2.0)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api/tree/columnstore-1.2.0)
* MaxScale CDC and Kafka Data Adapters - [Source Code for data adapters](https://github.com/mariadb-corporation/mariadb-columnstore-data-adapters/tree/columnstore-1.2.0)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
