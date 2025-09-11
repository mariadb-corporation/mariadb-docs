# MariaDB ColumnStore 1.1.5 GA Release Notes

**Release date:** 19th June 2018

[MariaDB ColumnStore 1.1.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) is a GA release of MariaDB ColumnStore. This is the fourth release of the MariaDB ColumnStore 1.1 series. This release of MariaDB ColumnStore provides improvements over the previous 1.1.4 GA release.

MariaDB ColumnStore 1.1.5 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-1435](https://jira.mariadb.org/browse/MCOL-1435) - The base MariaDB server version is now [10.2.15](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md) which include several maintenance and security fixes.
* [MCOL-1412](https://jira.mariadb.org/browse/MCOL-1412) - Ubuntu 18.04 is supported from this release onwards.

## Bugs and issues fixed

* [MCOL-1197](https://jira.mariadb.org/browse/MCOL-1197) - CPIMPORT fails and Abandoned when data row is too BIG to Handle
* [MCOL-1229](https://jira.mariadb.org/browse/MCOL-1229) - IS.columnstore\_columns crashes when DDL is simultaneously executing
* [MCOL-1261](https://jira.mariadb.org/browse/MCOL-1261) - mcsapi Python wrapper breaks on out of source builds
* [MCOL-1321](https://jira.mariadb.org/browse/MCOL-1321) - bulk write sdk python bindings does not support status out param in setColumn
* [MCOL-1342](https://jira.mariadb.org/browse/MCOL-1342) - A restriction for allowed length of the table and column names is not implemented
* [MCOL-1348](https://jira.mariadb.org/browse/MCOL-1348) - ExeMgr failes to process SELECT with any field preceding UDAF functor.
* [MCOL-1349](https://jira.mariadb.org/browse/MCOL-1349) - Selecting VIEW throws 1815. Internal error when the VIEW definition contains nested and non nested LEFT JOINS and On clause filter on the nested JOIN
* [MCOL-1359](https://jira.mariadb.org/browse/MCOL-1359) - Spark connector does not allow NULL values
* [MCOL-1361](https://jira.mariadb.org/browse/MCOL-1361) - Spark connector doesn't handle null values
* [MCOL-1370](https://jira.mariadb.org/browse/MCOL-1370) - Network Error incorrect handled, Amazon DBROOT detach failed, but dbroot still was reassigned
* [MCOL-1377](https://jira.mariadb.org/browse/MCOL-1377) - ColumnStore system logging not working after 1.1.4 ubuntu-16 install
* [MCOL-1384](https://jira.mariadb.org/browse/MCOL-1384) - Couldn't use reserved words in idents even with quotes(backport from develop)
* [MCOL-1390](https://jira.mariadb.org/browse/MCOL-1390) - SUBSTRING\_INDEX returns NULL when the number parameter is negative
* [MCOL-1394](https://jira.mariadb.org/browse/MCOL-1394) - kafka avro adapter install avro library issues
* [MCOL-1396](https://jira.mariadb.org/browse/MCOL-1396) - VARCHAR returning NULL when StringStore memory limit exceeded
* [MCOL-1400](https://jira.mariadb.org/browse/MCOL-1400) - update pdi data adapter to use explicit mcsapi version numbers
* [MCOL-1403](https://jira.mariadb.org/browse/MCOL-1403) - Trailing whitespace in CHAR/VARCHAR break string matches - Revisited
* [MCOL-1405](https://jira.mariadb.org/browse/MCOL-1405) - Mysqld PID is missed in the output of mcsadmin getSystemInfo
* [MCOL-1406](https://jira.mariadb.org/browse/MCOL-1406) - Cannot create pv\_facts table in develop
* [MCOL-1408](https://jira.mariadb.org/browse/MCOL-1408) - Columnstore table unable to accept writes after thousands of commits via Bulk SDK
* [MCOL-1430](https://jira.mariadb.org/browse/MCOL-1430) - CDC Connector v2.2.5-1 unable to connect to MaxScale
* [MCOL-1440](https://jira.mariadb.org/browse/MCOL-1440) - rename the data-adapter kettle package to match the others
* [MCOL-1444](https://jira.mariadb.org/browse/MCOL-1444) - mcsapi's dataconvert-decimal fails for Ubuntu 18.04
* [MCOL-1455](https://jira.mariadb.org/browse/MCOL-1455) - mariadb-columnstore-kafka-adapters has been deprecated - remove from building
* [MCOL-1460](https://jira.mariadb.org/browse/MCOL-1460) - Build for Kettle adapter is not created
* [MCOL-1463](https://jira.mariadb.org/browse/MCOL-1463) - Columnstore provided udf median()/avg\_mode() not working
* [MCOL-1179](https://jira.mariadb.org/browse/MCOL-1179) - Pentaho Data Integration / Kettle - Bulk API Java Binding
* [MCOL-1232](https://jira.mariadb.org/browse/MCOL-1232) - Spark connector - support different ColumnStore configurations
* [MCOL-1259](https://jira.mariadb.org/browse/MCOL-1259) - ColumnStore Data-Adapters needs a top level cmake for building all Data-Adapters
* [MCOL-1344](https://jira.mariadb.org/browse/MCOL-1344) - CREATE table STATEMENT from Spark Dataframe structure
* [MCOL-1364](https://jira.mariadb.org/browse/MCOL-1364) - Update mariadb-columnstore-api package names to amd64 in make file for Debian/Ubuntu
* [MCOL-1412](https://jira.mariadb.org/browse/MCOL-1412) - Backport Ubuntu 18.04 support to 1.1
* [MCOL-1435](https://jira.mariadb.org/browse/MCOL-1435) - Merge [MariaDB 10.2.15](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md) into 1.1

In addition, all bugs fixed in MariaDB ColumnStore 1.1.4 and earlier are implicitly included in this release.

## Upgrade

The following procedure outlines upgrading a 1.1.4 ColumnStore install to 1.1.5:

* [1.1.4 GA to 1.1.5 GA upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md)

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
* [MCOL-1491](https://jira.mariadb.org/browse/MCOL-1491): auth\_pam.so plugin missing from server package
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

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.1.5 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8, Debian 9, RedHat 6, RedHat 7, SUSE 12, Ubuntu 16.04 and Ubuntu 18.04.
* Packages can be downloaded [here](https://mariadb.com/downloads/mariadb-ax) or can be installed from the [repositories](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.1.5". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.1.5)
* MariaDB Server - [Source code based on MariaDB Server 10.2.15 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.1.5)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools/tree/columnstore-1.1.5)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api/tree/columnstore-1.1.5)
* MaxScale CDC and Kafka Data Adapters - [Source Code for data adapters](https://github.com/mariadb-corporation/mariadb-columnstore-data-adapters/tree/columnstore-1.1.5)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
