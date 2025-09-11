# MariaDB ColumnStore 1.1.3 GA Release Notes

**Release date:** 21st February 2018

[MariaDB ColumnStore 1.1.3](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a GA release of MariaDB ColumnStore. This is the fourth release of the MariaDB ColumnStore 1.1 series. This release of MariaDB ColumnStore provides improvements over the previous 1.1.2 GA release.

MariaDB ColumnStore 1.1.3 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [Beta](../../../community-server/about/release-criteria.md) release of [Apache Spark Adapter](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md) for integration of MariaDB ColumnStore utilizing the Spark SQL feature.
* [GA](../../../community-server/about/release-criteria.md) release of [MaxScale CDC Adapter](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/clients-and-tools/data-ingestion/columnstore-streaming-data-adapters)
* [GA](../../../community-server/about/release-criteria.md) release of [Aache Kafka Data Adapter](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/clients-and-tools/data-ingestion/columnstore-streaming-data-adapters)
* [MCOL-1121](https://jira.mariadb.org/browse/MCOL-1121) - The Kafka adapter has been made to work with more generic streams
* [MCOL-1214](https://jira.mariadb.org/browse/MCOL-1214) - The base MariaDB server version is now [10.2.13](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10213-release-notes.md) which include several maintenance and security fixes.
* Package repositories for [MariaDB AX and MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md) now available

## Bugs and issues fixed

* [MCOL-258](https://jira.mariadb.org/browse/MCOL-258) - Window function create is hidden
* [MCOL-436](https://jira.mariadb.org/browse/MCOL-436) - Alarms is being incorrect processed on local node
* [MCOL-782](https://jira.mariadb.org/browse/MCOL-782) - Non-recursive Common Table Expressions used in view caused an error
* [MCOL-927](https://jira.mariadb.org/browse/MCOL-927) - RPM packages for Centos 6.7 returned an libmariadb.so.3 loading error
* [MCOL-939](https://jira.mariadb.org/browse/MCOL-939) - mysqld logs wrong columnstore version number
* [MCOL-952](https://jira.mariadb.org/browse/MCOL-952) - UDAF incorrect error on some joins
* [MCOL-954](https://jira.mariadb.org/browse/MCOL-954) - mysqld crashing on slave replication UMs
* [MCOL-964](https://jira.mariadb.org/browse/MCOL-964) - tpcds query78 alternately fails and works with incorrect results
* [MCOL-994](https://jira.mariadb.org/browse/MCOL-994) - cpimport failed with a "new extent FBO too high for current file error"
* [MCOL-1029](https://jira.mariadb.org/browse/MCOL-1029) - Logic issue breaking multiple where conditions
* [MCOL-1034](https://jira.mariadb.org/browse/MCOL-1034) - DDl/DML incorrect starts when active on um2 during a pm outage
* [MCOL-1040](https://jira.mariadb.org/browse/MCOL-1040) - ERROR 2013 (HY000): Lost connection to MySQL server during query
* [MCOL-1042](https://jira.mariadb.org/browse/MCOL-1042) - Server and Engine should use CPACK\_DEBIAN\_PACKAGE\_SHLIBDEPS
* [MCOL-1044](https://jira.mariadb.org/browse/MCOL-1044) - inconsistent library naming for JAVA write SDK
* [MCOL-1045](https://jira.mariadb.org/browse/MCOL-1045) - postConfigure on debian 9.2 fails with libreadline.so.5 link error
* [MCOL-1047](https://jira.mariadb.org/browse/MCOL-1047) - debian 9.2 cluster tester issues
* [MCOL-1048](https://jira.mariadb.org/browse/MCOL-1048) - debian9 api python bindings built for python3 but installed in python2
* [MCOL-1061](https://jira.mariadb.org/browse/MCOL-1061) - Post Configure reports incomplete name for script to run
* [MCOL-1062](https://jira.mariadb.org/browse/MCOL-1062) - High concurrency can lock up PrimProc
* [MCOL-1066](https://jira.mariadb.org/browse/MCOL-1066) - non-root install- getsystemdisk doesnt show any info
* [MCOL-1068](https://jira.mariadb.org/browse/MCOL-1068) - Compression ratio miscalculation when there are uncompressed columns
* [MCOL-1070](https://jira.mariadb.org/browse/MCOL-1070) - tupleconstantstep assert when query executed as view
* [MCOL-1078](https://jira.mariadb.org/browse/MCOL-1078) - mcsapi packet stitching can fail
* [MCOL-1079](https://jira.mariadb.org/browse/MCOL-1079) - mcsapi getTableLock not failing
* [MCOL-1082](https://jira.mariadb.org/browse/MCOL-1082) - row\_count() function always returns 0 for any engine
* [MCOL-1083](https://jira.mariadb.org/browse/MCOL-1083) - cannot execute 2 subqueries with blob in select part
* [MCOL-1086](https://jira.mariadb.org/browse/MCOL-1086) - ssh certificates aren't used in postConfigure nonDistributed installation with DataRedundancy between PMs enabled.
* [MCOL-1087](https://jira.mariadb.org/browse/MCOL-1087) - ColumnStore API is missing dependencies in the documentation for the Debian installation
* [MCOL-1091](https://jira.mariadb.org/browse/MCOL-1091) - crash with large writes on java binding of write sdk
* [MCOL-1106](https://jira.mariadb.org/browse/MCOL-1106) - multi-node install fails, mysqld didnt startup in time
* [MCOL-1108](https://jira.mariadb.org/browse/MCOL-1108) - After rollback() an active transaction is reported by mcsadmin shutdownSystem
* [MCOL-1114](https://jira.mariadb.org/browse/MCOL-1114) - Set cpack deb minimum version to 3.4
* [MCOL-1128](https://jira.mariadb.org/browse/MCOL-1128) - exemgr becomes non responsive
* [MCOL-1129](https://jira.mariadb.org/browse/MCOL-1129) - Initialization of the Java Swig library within the parent class loader on package import
* [MCOL-1133](https://jira.mariadb.org/browse/MCOL-1133) - mcsapi string->decimal conversion corruption for long and negative data
* [MCOL-1134](https://jira.mariadb.org/browse/MCOL-1134) - non-root install - columnstoreAlias file not update and reference by postConfigure
* [MCOL-1135](https://jira.mariadb.org/browse/MCOL-1135) - non-root install - post-install accidentally starts columnstore service
* [MCOL-1137](https://jira.mariadb.org/browse/MCOL-1137) - Mysql replication master and slave both setup after a masternode failover
* [MCOL-1138](https://jira.mariadb.org/browse/MCOL-1138) - pm1 failover testing - didnt leave a HOT\_STANDBY ProcMgr on remainng node
* [MCOL-1147](https://jira.mariadb.org/browse/MCOL-1147) - multiple mcsapi sessions use the same txnID
* [MCOL-1152](https://jira.mariadb.org/browse/MCOL-1152) - change columnstore debian package name from cmake
* [MCOL-1153](https://jira.mariadb.org/browse/MCOL-1153) - Small memory leak in mcsapi
* [MCOL-1160](https://jira.mariadb.org/browse/MCOL-1160) - Bulk write API doesn't start new block for dictionary
* [MCOL-1165](https://jira.mariadb.org/browse/MCOL-1165) - Use the threadpool automatic idle down facility
* [MCOL-1167](https://jira.mariadb.org/browse/MCOL-1167) - postConfigure - option -c not working
* [MCOL-1168](https://jira.mariadb.org/browse/MCOL-1168) - SystemCatalog Test fails
* [MCOL-1176](https://jira.mariadb.org/browse/MCOL-1176) - 10Mio Row test fails, only 9988608 rows are written to ColumnStore
* [MCOL-1177](https://jira.mariadb.org/browse/MCOL-1177) - SparkConnector runs out of memory for large datasets, JDBC can handle the datasets just fine
* [MCOL-1178](https://jira.mariadb.org/browse/MCOL-1178) - empty result with "case .. when" with where condition and multiple parameter in "IN" clause
* [MCOL-1184](https://jira.mariadb.org/browse/MCOL-1184) - non-root Log Rotation not working
* [MCOL-1185](https://jira.mariadb.org/browse/MCOL-1185) - configAlarm error: Oam::setAlarmConfig: error opening file /usr/local/mariadb/columnstore/etc/AlarmConfig.xml: Permission denied
* [MCOL-1190](https://jira.mariadb.org/browse/MCOL-1190) - Process ID of mysqld is missed in the output of mcsadmin getSystemInfo
* [MCOL-1194](https://jira.mariadb.org/browse/MCOL-1194) - columnstoreRestore version check broken
* [MCOL-1198](https://jira.mariadb.org/browse/MCOL-1198) - Let the Spark Connector use the native floating point datastructure
* [MCOL-1202](https://jira.mariadb.org/browse/MCOL-1202) - columnstoreRestore does not restore correct config file
* [MCOL-1210](https://jira.mariadb.org/browse/MCOL-1210) - columnstore\_info procedures can only be used from within columnstore\_info
* [MCOL-1212](https://jira.mariadb.org/browse/MCOL-1212) - An aborted query during an aggregate will crash ExeMgr
* [MCOL-444](https://jira.mariadb.org/browse/MCOL-444) - split character import issue
* [MCOL-446](https://jira.mariadb.org/browse/MCOL-446) - mycnf config change request
* [MCOL-962](https://jira.mariadb.org/browse/MCOL-962) - Funtcion/table to find out if ColumnStore instance (UM) is ready to process SQL queries against ColumnStore tables
* [MCOL-1058](https://jira.mariadb.org/browse/MCOL-1058) - cluster tester enhancements - check for mysql password and mariadb-libs package
* [MCOL-1085](https://jira.mariadb.org/browse/MCOL-1085) - Add automatic stack trace to ColumnStore binaries
* [MCOL-1107](https://jira.mariadb.org/browse/MCOL-1107) - Basic Java example of cpimport which uses the columnstore API
* [MCOL-1119](https://jira.mariadb.org/browse/MCOL-1119) - spark connector for publishing dataframe results using mcsapi to columnstore.
* [MCOL-1171](https://jira.mariadb.org/browse/MCOL-1171) - Introduce benchmarks to test the performance with regards to jdbc
* [MCOL-1172](https://jira.mariadb.org/browse/MCOL-1172) - Create a consistent naming for scala and python spark exporter
* [MCOL-1199](https://jira.mariadb.org/browse/MCOL-1199) - Forward Bulk Write API C++ Exceptions to Java
* [MCOL-1200](https://jira.mariadb.org/browse/MCOL-1200) - Forward Bulk Write API C++ Exceptions to Python
* [MCOL-304](https://jira.mariadb.org/browse/MCOL-304) - MariaDB ColumnStore Package Repository
* [MCOL-1060](https://jira.mariadb.org/browse/MCOL-1060) - ColumnStore Cluster Test tool - wording improvmenets
* [MCOL-1069](https://jira.mariadb.org/browse/MCOL-1069) - Merge [MariaDB 10.2.11](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10211-release-notes.md)
* [MCOL-1075](https://jira.mariadb.org/browse/MCOL-1075) - Clarifications for the Bulk Write SDK documentation
* [MCOL-1099](https://jira.mariadb.org/browse/MCOL-1099) - Clarification for the Bulk Write SDK documentation
* [MCOL-1121](https://jira.mariadb.org/browse/MCOL-1121) - Generic Kafka Data Adapter
* [MCOL-1122](https://jira.mariadb.org/browse/MCOL-1122) - build api for both python 2 and 3
* [MCOL-1142](https://jira.mariadb.org/browse/MCOL-1142) - support group install of AX
* [MCOL-1143](https://jira.mariadb.org/browse/MCOL-1143) - package build of mariadb-columnstore-tools
* [MCOL-1159](https://jira.mariadb.org/browse/MCOL-1159) - Merge [MariaDB 10.2.12](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10212-release-notes.md)
* [MCOL-1214](https://jira.mariadb.org/browse/MCOL-1214) - Merge [MariaDB 10.2.13](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10213-release-notes.md)

In addition, all bugs fixed in MariaDB ColumnStore 1.1.2 and earlier are implicitly included in this release.

## Upgrade

The following procedure outlines upgrading a 1.1.2 ColumnStore install to 1.1.3:

* [1.1.2 GA to 1.1.3 GA upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md)

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
* [MCOL-912](https://jira.mariadb.org/browse/MCOL-912) : After adding two PMs with gluster, cpimport failed on newly added PMs. The system must be restarted after adding PM modules with data redundancy / gluster storage.
* [MCOL-1217](https://jira.mariadb.org/browse/MCOL-1217): A newly added user module didn't have MariaDB replication slave setup
* [MCOL-1222](https://jira.mariadb.org/browse/MCOL-1222): ColumnStore start/restart can return before system is ready
* [MCOL-1224](https://jira.mariadb.org/browse/MCOL-1224): post-install non-root has incorrect permissions for /etc/rc.local
* [MCOL-1225](https://jira.mariadb.org/browse/MCOL-1225): LD\_LIBRARY\_PATH not set correctly in centos6 non-root install
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

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.1.3 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8, Debian 9, RedHat 6, RedHat 7, SUSE 12, and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/downloads/mariadb-ax) or can be installed from the [repositories](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.1.3". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.1.3)
* MariaDB Server - [Source code based on MariaDB Server 10.2.10 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.1.3)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools/tree/columnstore-1.1.3)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api/tree/columnstore-1.1.3)
* MaxScale CDC and Kafka Data Adapters - [Source Code for data adapters](https://github.com/mariadb-corporation/mariadb-columnstore-data-adapters/tree/columnstore-1.1.3)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
