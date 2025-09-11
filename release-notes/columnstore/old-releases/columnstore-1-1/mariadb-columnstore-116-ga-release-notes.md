# MariaDB ColumnStore 1.1.6 GA Release Notes

**Release date:** 7th September 2018

[MariaDB ColumnStore 1.1.6](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a GA release of MariaDB ColumnStore. This is the fourth release of the MariaDB ColumnStore 1.1 series. This release of MariaDB ColumnStore provides improvements over the previous 1.1.5 GA release.

MariaDB ColumnStore 1.1.6 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-1615](https://jira.mariadb.org/browse/MCOL-1615) - The base MariaDB server version is now [10.2.17](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10217-release-notes.md) which include several maintenance and security fixes.

## Bugs and issues fixed

* [MCOL-970](https://jira.mariadb.org/browse/MCOL-970) - MariaDB's slow query log only logging vtable information
* [MCOL-1037](https://jira.mariadb.org/browse/MCOL-1037) - Race condition in FIFO buffer
* [MCOL-1155](https://jira.mariadb.org/browse/MCOL-1155) - NOT with null safe operator fails
* [MCOL-1195](https://jira.mariadb.org/browse/MCOL-1195) - mcsapi BadUsage.AssertTableLock test creates phantom transaction
* [MCOL-1301](https://jira.mariadb.org/browse/MCOL-1301) - mcsapi won't compile with Python3 in Debug mode in CentOS 7
* [MCOL-1421](https://jira.mariadb.org/browse/MCOL-1421) - test200 needs tuning
* [MCOL-1445](https://jira.mariadb.org/browse/MCOL-1445) - mcsapi Java test fails on Ubuntu 18.04 and Java 10
* [MCOL-1453](https://jira.mariadb.org/browse/MCOL-1453) - mcsapi doesn't detect when WriteEngineServer has gone away
* [MCOL-1468](https://jira.mariadb.org/browse/MCOL-1468) - CDC adapter: mxs\_adapter doesn't measure transaction insert time as expected
* [MCOL-1472](https://jira.mariadb.org/browse/MCOL-1472) - where does not properly evaluate case when case when on varchar columns
* [MCOL-1474](https://jira.mariadb.org/browse/MCOL-1474) - PriorityThreadPool can crash
* [MCOL-1490](https://jira.mariadb.org/browse/MCOL-1490) - Data-Adapter package has different names for RPM and DEB
* [MCOL-1491](https://jira.mariadb.org/browse/MCOL-1491) - auth\_pam.so plugin missing from server package
* [MCOL-1498](https://jira.mariadb.org/browse/MCOL-1498) - Installation failed in Replication Distribution command
* [MCOL-1525](https://jira.mariadb.org/browse/MCOL-1525) - Non-root Install - core dumps not working
* [MCOL-1527](https://jira.mariadb.org/browse/MCOL-1527) - Incorrect 0 row(s) affected on delete with cross engine join
* [MCOL-1531](https://jira.mariadb.org/browse/MCOL-1531) - ColumnStore fails to make inner join if using CASE in predicate.
* [MCOL-1535](https://jira.mariadb.org/browse/MCOL-1535) - Case when\~ vs case \~ when \~
* [MCOL-1545](https://jira.mariadb.org/browse/MCOL-1545) - Compiler error in GCC 8.1
* [MCOL-1566](https://jira.mariadb.org/browse/MCOL-1566) - mcsapi documentation build issue in CentOS 7
* [MCOL-1579](https://jira.mariadb.org/browse/MCOL-1579) - ColumnStore as root crashes processes using shm
* [MCOL-1588](https://jira.mariadb.org/browse/MCOL-1588) - javamcsapi ColumnStoreBulkInsert can't manually be garbage collected
* [MCOL-1594](https://jira.mariadb.org/browse/MCOL-1594) - mxs\_adapter requires -t to gracefully exit
* [MCOL-1595](https://jira.mariadb.org/browse/MCOL-1595) - mxs\_adapter state file is stored in the current directory
* [MCOL-1605](https://jira.mariadb.org/browse/MCOL-1605) - sendAlarmReport error: InetStreamSocket::connect: connect() error: Connection timed
* [MCOL-1612](https://jira.mariadb.org/browse/MCOL-1612) - python spark connector - broken
* [MCOL-1635](https://jira.mariadb.org/browse/MCOL-1635) - insert into select crashes for a BLOB column
* [MCOL-1655](https://jira.mariadb.org/browse/MCOL-1655) - Yacc debug hard coded on
* [MCOL-1664](https://jira.mariadb.org/browse/MCOL-1664) - data-adatper centos7 package rename not executed
* [MCOL-1675](https://jira.mariadb.org/browse/MCOL-1675) - Incorrect HWM calculation if the table's first column width > 1
* [MCOL-1684](https://jira.mariadb.org/browse/MCOL-1684) - Performance Schema crashes prepared statement
* [MCOL-1705](https://jira.mariadb.org/browse/MCOL-1705) - check hardcoded uses of root user for mysql
* [MCOL-1330](https://jira.mariadb.org/browse/MCOL-1330) - Make ColumnStore work under valgrind
* [MCOL-1376](https://jira.mariadb.org/browse/MCOL-1376) - Support Ubuntu 18.04
* [MCOL-1475](https://jira.mariadb.org/browse/MCOL-1475) - Improve cross engine error handling
* [MCOL-1484](https://jira.mariadb.org/browse/MCOL-1484) - Use condition pushdown in I\_S tables
* [MCOL-1521](https://jira.mariadb.org/browse/MCOL-1521) - Java - mcsapi - introduce new function getJavaMcsapiVersion()
* [MCOL-1524](https://jira.mariadb.org/browse/MCOL-1524) - Backward / Forward compatibility test for javamcsapi and mcsapi
* [MCOL-1551](https://jira.mariadb.org/browse/MCOL-1551) - Ability to configure ColumnStore to use domain names instead of IP addresses
* [MCOL-1591](https://jira.mariadb.org/browse/MCOL-1591) - add UMASK check to ColumnStore Cluster Tester script
* [MCOL-1596](https://jira.mariadb.org/browse/MCOL-1596) - mxs\_adapter multi-table support
* [MCOL-1661](https://jira.mariadb.org/browse/MCOL-1661) - Transform CDC events into UPDATE and DELETE statements
* [MCOL-1145](https://jira.mariadb.org/browse/MCOL-1145) - One step configuration of Single Server Node
* [MCOL-1146](https://jira.mariadb.org/browse/MCOL-1146) - One step configuration of Multi Server Node
* [MCOL-1439](https://jira.mariadb.org/browse/MCOL-1439) - Documentation for Python API missing
* [MCOL-1615](https://jira.mariadb.org/browse/MCOL-1615) - Merge [MariaDB 10.2.17](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10217-release-notes.md)
* [MCOL-1617](https://jira.mariadb.org/browse/MCOL-1617) - remove generated build doc from mcsapi in favor of its Readme.md in Github
* [MCOL-1646](https://jira.mariadb.org/browse/MCOL-1646) - Update AX docs for 18.04
* [MCOL-1496](https://jira.mariadb.org/browse/MCOL-1496) - Joiner array boundary bug

In addition, all bugs fixed in MariaDB ColumnStore 1.1.5 and earlier are implicitly included in this release.

## Upgrade

The following procedure outlines upgrading a 1.1.5 ColumnStore install to 1.1.6:

* [1.1.5 GA to 1.1.6 GA upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md)

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
* [MCOL-1654](https://jira.mariadb.org/browse/MCOL-1654): The QueryStats table is missing
* /dev/shm may be set to 755 permissions prior to 1.1.6 which could cause problems with other non-root processes, from 1.1.6 onwards ColumnStore does not try to do this. You should change this to 777 if it is causing problems with your installation.
* The current logging default generates full verbose debug logs. This can be controlled by making logging configuration changes as described [here](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/management/columnstore-system/columnstore-system-monitoring-configuration).
* While Millisecond and Microsecond storage is supported for datetime, time and timestamp columns, at this time the query results cannot return millisecond and microseconds.
* UTF-8 Limitation
  * UTF-8 must be declared at the table level if the instance has been set up with a UTF-8 profile. Tables created with a non-matching character set will yield indeterminate results.
  * Viewing SQL output should be done using client software that supports UTF-8 character sets.
  * UTF-8 characters are not supported in object names.
* Known security issues and fixes are documented [here](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/security/columnstore-security-vulnerabilities).

## Documentation

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md)

## Packaging

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.1.6 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8, Debian 9, RedHat 6, RedHat 7, SUSE 12, Ubuntu 16.04 and Ubuntu 18.04.
* Packages can be downloaded [here](https://mariadb.com/downloads/mariadb-ax) or can be installed from the [repositories](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.1.6". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.1.6)
* MariaDB Server - [Source code based on MariaDB Server 10.2.15 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.1.6)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools/tree/columnstore-1.1.6)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api/tree/columnstore-1.1.6)
* MaxScale CDC and Kafka Data Adapters - [Source Code for data adapters](https://github.com/mariadb-corporation/mariadb-columnstore-data-adapters/tree/columnstore-1.1.6)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
