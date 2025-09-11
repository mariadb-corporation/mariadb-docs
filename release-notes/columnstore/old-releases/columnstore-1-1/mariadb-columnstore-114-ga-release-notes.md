# MariaDB ColumnStore 1.1.4 GA Release Notes

**Release date:** 24th April 2018

[MariaDB ColumnStore 1.1.4](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a GA release of MariaDB ColumnStore. This is the fourth release of the MariaDB ColumnStore 1.1 series. This release of MariaDB ColumnStore provides improvements over the previous 1.1.3 GA release.

MariaDB ColumnStore 1.1.4 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [Beta](../../../community-server/about/release-criteria.md) release of Pentaho Kettle Adapter for integration of MariaDB ColumnStore utilizing Pentaho Kettle.
* [MCOL-1319](https://jira.mariadb.org/browse/MCOL-1319) - The base MariaDB server version is now [10.2.14](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10214-release-notes.md) which include several maintenance and security fixes.
* [MCOL-1321](https://jira.mariadb.org/browse/MCOL-1321) - The Python bulk write SDK binding has an API change around setColumn() to return a status.

## Bugs and issues fixed

* [MCOL-912](https://jira.mariadb.org/browse/MCOL-912) - After adding two PMs, cpimport failed on newly added PMs
* [MCOL-1084](https://jira.mariadb.org/browse/MCOL-1084) - table\_usage() stored procedure show zero total usage when there are no dict columns
* [MCOL-1156](https://jira.mariadb.org/browse/MCOL-1156) - Incorrect 0 row(s) affected on delete
* [MCOL-1182](https://jira.mariadb.org/browse/MCOL-1182) - Cross-engine join query failing (single node)
* [MCOL-1196](https://jira.mariadb.org/browse/MCOL-1196) - Error when using OR in case THEN portion
* [MCOL-1213](https://jira.mariadb.org/browse/MCOL-1213) - SystemCatalog.getTable("table name") doesn't support uppercase letters
* [MCOL-1217](https://jira.mariadb.org/browse/MCOL-1217) - newly added user module didnt have mysql replication slave setup
* [MCOL-1222](https://jira.mariadb.org/browse/MCOL-1222) - ColumnStore start/restart can return before system is ready
* [MCOL-1228](https://jira.mariadb.org/browse/MCOL-1228) - ALTER TABLE...CHANGE COLUMN broken for TEXT data types
* [MCOL-1230](https://jira.mariadb.org/browse/MCOL-1230) - Change spark-connector's default compile option to ON
* [MCOL-1231](https://jira.mariadb.org/browse/MCOL-1231) - Get a cmake error while building releases without both Python versions installed instead of a warning
* [MCOL-1233](https://jira.mariadb.org/browse/MCOL-1233) - Ubuntu package has a bad dependency
* [MCOL-1234](https://jira.mariadb.org/browse/MCOL-1234) - Nested CASE filters not processed
* [MCOL-1235](https://jira.mariadb.org/browse/MCOL-1235) - procmgr crash - too many files open on alarm socket
* [MCOL-1241](https://jira.mariadb.org/browse/MCOL-1241) - Move ColumnStore Kettle plugin to data-adapters git repository
* [MCOL-1245](https://jira.mariadb.org/browse/MCOL-1245) - getting A fatal error in bulkinsert mariadb columnstore java api
* [MCOL-1246](https://jira.mariadb.org/browse/MCOL-1246) - Trailing whitespace in CHAR/VARCHAR break string matches
* [MCOL-1252](https://jira.mariadb.org/browse/MCOL-1252) - CSV load into columnstore table using Pentaho adapter with CS Bulk Import plugin doesn't succeed
* [MCOL-1255](https://jira.mariadb.org/browse/MCOL-1255) - PDI CS Bulk Load plugin can't work with variable defined in kettle.properties file
* [MCOL-1262](https://jira.mariadb.org/browse/MCOL-1262) - PDI CS naming conventions support
* [MCOL-1280](https://jira.mariadb.org/browse/MCOL-1280) - MCSAPI C++ documentation, example incorrect
* [MCOL-1285](https://jira.mariadb.org/browse/MCOL-1285) - Adapter can't recognize database schema with capital letters
* [MCOL-1317](https://jira.mariadb.org/browse/MCOL-1317) - Columnstore Cluster Tester tool does not check the availability of all ports needed to mcs operations
* [MCOL-1321](https://jira.mariadb.org/browse/MCOL-1321) - bulk write sdk python bindings does not support status out param in setColumn
* [MCOL-1323](https://jira.mariadb.org/browse/MCOL-1323) - cpimport Splitter has incorrect SIGPIPE mapping
* [MCOL-1179](https://jira.mariadb.org/browse/MCOL-1179) - Pentaho Data Integration / Kettle - Bulk API Java Binding
* [MCOL-1232](https://jira.mariadb.org/browse/MCOL-1232) - Spark connector - support different ColumnStore configurations
* [MCOL-1283](https://jira.mariadb.org/browse/MCOL-1283) - Try to pack/load the shared bulk write sdk library in/from jar to ease installation process
* [MCOL-1296](https://jira.mariadb.org/browse/MCOL-1296) - Add debug output as an API option
* [MCOL-1312](https://jira.mariadb.org/browse/MCOL-1312) - PDI version number - include git
* [MCOL-1318](https://jira.mariadb.org/browse/MCOL-1318) - Columnstore Cluster Tester tool is evaluating Failure if Firewall Services or SELINUX are enabled
* [MCOL-1264](https://jira.mariadb.org/browse/MCOL-1264) - List of manual tests performed
* [MCOL-1319](https://jira.mariadb.org/browse/MCOL-1319) - Merge [MariaDB 10.2.14](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10214-release-notes.md)
* [MCOL-1333](https://jira.mariadb.org/browse/MCOL-1333) - Document that .tar.gz of RPM files is needed for addModule command
* [MCOL-1261](https://jira.mariadb.org/browse/MCOL-1261) - mcsapi Python wrapper breaks on out of source builds
* [MCOL-1325](https://jira.mariadb.org/browse/MCOL-1325) - rename table fails when database different than current database
* [MCOL-1344](https://jira.mariadb.org/browse/MCOL-1344) - CREATE table STATEMENT from Spark Dataframe structure

In addition, all bugs fixed in MariaDB ColumnStore 1.1.3 and earlier are implicitly included in this release.

## Upgrade

The following procedure outlines upgrading a 1.1.3 ColumnStore install to 1.1.4:

* [1.1.3 GA to 1.1.4 GA upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md)

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

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md)

## Packaging

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.1.4 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8, Debian 9, RedHat 6, RedHat 7, SUSE 12, and Ubuntu 16.04.
* Packages can be downloaded [here](https://mariadb.com/downloads/mariadb-ax) or can be installed from the [repositories](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.1.4". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.1.4)
* MariaDB Server - [Source code based on MariaDB Server 10.2.10 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.1.4)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools/tree/columnstore-1.1.4)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api/tree/columnstore-1.1.4)
* MaxScale CDC and Kafka Data Adapters - [Source Code for data adapters](https://github.com/mariadb-corporation/mariadb-columnstore-data-adapters/tree/columnstore-1.1.4)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
