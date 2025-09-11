# MariaDB ColumnStore 1.0.1 Alpha Release Notes

**Release date:** 14 June 2016

[MariaDB ColumnStore 1.0.1](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) is the development version of MariaDB ColumnStore. It is built by porting InfiniDB 4.6.2 on [MariaDB 10.1.14](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md).

MariaDB ColumnStore 1.0.1 is an [_**Alpha**_](../../../community-server/about/release-criteria.md) release.

**Do not use&#x20;**_**alpha**_**&#x20;releases on production systems!**

This is the first MariaDB ColumnStore release, and we are releasing it now to get it into the hands of any one who might want to test it. We plan to do several Alpha releases, each with increased stability and more features.

Note that this is an early Alpha release of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) in [MariaDB 10.1.14.](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md) The porting work from MySQL 5.1 is done, but not all features have been fully tested. This release is only meant for testing, not for using in production!

To understand what to expect from this release, a little background is needed: [MariaDB ColumnStore](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) is based on the MySQL 5.1 InfiniDB release, which was a stable product with a lot of happy users. To make this more modern and easier to develop, we moved the InfiniDB code to [MariaDB 10.1.14](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md) and renamed it ColumnStore. As most of the [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) code is unchanged and as [MariaDB 10.1.14](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md) code is stable, the possible problems are mostly in the interface between MariaDB Server and MariaDB ColumnStore.

We have not yet had time to ourselves to extensively test all [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) features, and MariaDB ColumnStore has not yet been tested by a larger community, so there may be some issues that need to be fixed in the next releases. We do, however, expect that most things should work and be reasonably stable.

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable Features

* Porting of InfiniDB source code as “columnstore” storage engine on [MariaDB 10.1.14](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md)
* All client applications using ODBC, JDBC, MySQL Clients, or MariaDB Clients can connect to and query MariaDB ColumnStore
* Windowing Functions Supported: AVG, COUNT, CUME\_DIST, DENSE\_RANK, MAX, MEDIAN, MIN, NTILE, PERCENT\_RANK, PERCENTILE\_CONT, PERCENTILE\_DISC, RANK, ROW\_NUMBER, STDDEV, STDDEV\_POP, STDDEV\_SAMP, SUM, VARIANCE, VAR\_POP, VAR\_SAMP
* Bulk Data Load—High-speed data loading utility cpimport
* ACID transactions
* MariaDB SQL Syntax compliance (with the exceptions noted in known limitations and issues)
* Cross Engine joins
* Built-in HA

### Changes for old InfiniDB users

* Renaming of the engine to columnstore
* Console command line utility is now called mcsadmin and an alias ma is created upon install for the same
* SQL client utility alias is now called mcsmysql
* Install directory is now under /usr/local/mariadb/columnstore
* Log directory is now under /var/log/mariadb/columnstore
* The numeric data type range values for MariaDB ColumnStore are different from that of other storage engines in MariaDB Server 10.1 as documented here

## Known Issues and Limitations

There are a number bugs and known limitations within this early Alpha version of MariaDB ColumnStore, the most serious of these are listed below. These are expected to be fixed way before the Beta release.\
There are some known security issues. They are listed here

* [MCOL-82](https://jira.mariadb.org/browse/MCOL-82): Subquery using IN with VIEW returns incorrect results. Queries selecting from view and using IN in where clause with a subquery on another view returns incorrect results.
* [MCOL-66](https://jira.mariadb.org/browse/MCOL-66), [MCOL-64](https://jira.mariadb.org/browse/MCOL-64), [MCOL-14](https://jira.mariadb.org/browse/MCOL-14): When multiple connection tries to perform DDL statements (Create Table/Drop Table/Alter Table) in parallel, system catalog tables get locked returning errors
  * Create Table, Drop Table and Alter Table must be done through a single connection at a time
* [MCOL-37](https://jira.mariadb.org/browse/MCOL-37): Following three window functions do not return correct value
  * FIRST\_VALUE
  * LEAD
  * LAG
* [MCOL-75](https://jira.mariadb.org/browse/MCOL-75) and [MCOL-74](https://jira.mariadb.org/browse/MCOL-74): NTH\_VALUE and LAST\_VALUE functions return syntax errors.
* [MCOL-73](https://jira.mariadb.org/browse/MCOL-73)): Wide table formatted display causes frontend to return error
  * MariaDB ColumnStore supports wide tables storage
  * Displaying the query results on a large number of columns without formatting the column works
  * Displaying the query results on a large number of columns with formatting causes error at MariaDB Server level
* [MCOL-45](https://jira.mariadb.org/browse/MCOL-45) : CREATE PROCEDURE fails.
  * Do not use stored procedure with this Alpha version [MCOL-16](https://jira.mariadb.org/browse/MCOL-16): LOAD DATA INFILE into datetime columns, data got saturated.
  * Do not use LOAD DATA INFILE when importing data into datetime columns
  * Use cpimport to bulk load data into MariaDB Columnstore instead. cpimports works correctly for datetime columns as well.
  * INSERT INTO works for datetime columns
* [MCOL-49](https://jira.mariadb.org/browse/MCOL-49): Drop table does not work if the PM node runs out of space.
* [MCOL-58](https://jira.mariadb.org/browse/MCOL-58): Non-Root install does not work in this release
  * Use root access to install this Alpha version
* [MCOL-39](https://jira.mariadb.org/browse/MCOL-39): console command "getSystemConfig" returns error for some parameter names\
  While Millisecond and Microsecond storage is supported for datetime, time and timestamp columns, at this time the query results cannot return millisecond and microseconds.
* UTF-8 Limitation
  * UTF-8 must be declared at the table level if the instance has been set up with a UTF-8 profile. Tables created with a non-matching character set will yield indeterminate results.
  * Viewing SQL output should be done using client software that supports UTF-8 character sets.
  * UTF-8 characters are not supported in object names.

The building of the software needs a special build environment. We're working on making it available for everyone to build.

## Documentation

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) include architecture, getting started, SQL Syntax guide, How to manage and How to load data into MariaDB ColumnStore.

Detailed Installation Guide will be available in next version of the MariaDB ColumnStore 1.0 series

## Packaging

RPM and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.0.1 Alpha version.

* The supported OS for this Alpha version are CentOS 6 and CentOS 7.
* Packages can be downloaded [here](https://mariadb.com/my_portal/download/mariadb-columnstore)

## Source Code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.\
The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine)
* MariaDB Server - [Source code based on MariaDB Server 10.1 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
