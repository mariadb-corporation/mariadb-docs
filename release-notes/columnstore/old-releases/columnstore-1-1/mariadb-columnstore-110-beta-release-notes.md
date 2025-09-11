# MariaDB ColumnStore 1.1.0 Beta Release Notes

**Release date:** 18th September 2017

[MariaDB ColumnStore 1.1.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a Beta release of MariaDB ColumnStore. This is the first release of the MariaDB ColumnStore 1.1 series. The MariaDB ColumnStore 1.1 series provides several new features and improvements over the MariaDB ColumnStore 1.0 release.

MariaDB ColumnStore 1.1.0 is a [_**Beta**_](../../../community-server/about/release-criteria.md) release.

**Do not use&#x20;**_**beta**_**&#x20;releases on production systems!**

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

## New Features

1. MariaDB ColumnStore 1.1.0 is based on MariaDB Server 10.2.8
2. The Window functions have been re-implemented with MariaDB Server 10.2.8 code.
3. [MariaDB ColumnStore Data API to programmatically load data into PM nodes](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
4. Text and Blob Data Types.
5. [User defined distributed aggregate and window functions.](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/reference/columnstore-user-defined-aggregate-and-window-functions)
6. [ColumnStore Backup/Restore Tool](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/management/columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards).
7. MariaDB Server [Audit Plugin Integration](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/management/columnstore-system/columnstore-audit-plugin).
8. Built-in data redundancy using GlusterFS integration for installations that use local disks for data storage on PMs. Please refer to [Preparing ColumnStore Installation](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md) for using GlusterFS with MariaDB ColumnStore.
9. Several performance improvements in string handling, memory utilization and general area.

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Bugs and issues fixed

* [MCOL-1](https://jira.mariadb.org/browse/MCOL-1) - Query Failed after a redistributeDB while ddl/dml/queries were active
* [MCOL-267](https://jira.mariadb.org/browse/MCOL-267) - TEXT and BLOB data types are not supported
* [MCOL-317](https://jira.mariadb.org/browse/MCOL-317) - replace drizzle with maria client library
* [MCOL-318](https://jira.mariadb.org/browse/MCOL-318) - switch to using os distribution version of snappy
* [MCOL-356](https://jira.mariadb.org/browse/MCOL-356) - BLOB data type not supported
* [MCOL-377](https://jira.mariadb.org/browse/MCOL-377) - columnstore queries show as vtable query rather than original query in audit log
* [MCOL-397](https://jira.mariadb.org/browse/MCOL-397) - binary package install doesnt check for package dependencies
* [MCOL-463](https://jira.mariadb.org/browse/MCOL-463) : gluster storage option in installer fails with an error.
* [MCOL-468](https://jira.mariadb.org/browse/MCOL-468) - update default replication configuration
* [MCOL-480](https://jira.mariadb.org/browse/MCOL-480) - warning error reported after upgrade to 1.0.6
* [MCOL-507](https://jira.mariadb.org/browse/MCOL-507) - More performance improvements to ExeMgr
* [MCOL-511](https://jira.mariadb.org/browse/MCOL-511) - native write data api
* [MCOL-513](https://jira.mariadb.org/browse/MCOL-513) - analyze and implement thread pools and memory buffers for performance optimization
* [MCOL-518](https://jira.mariadb.org/browse/MCOL-518) - backup (cold) and restore tool
* [MCOL-519](https://jira.mariadb.org/browse/MCOL-519) - productize glusterfs support and add tools to automate
* [MCOL-522](https://jira.mariadb.org/browse/MCOL-522) - support pre-installed software in postConfigure and addModule - phase I
* [MCOL-523](https://jira.mariadb.org/browse/MCOL-523) - support user defined aggregate functions
* [MCOL-534](https://jira.mariadb.org/browse/MCOL-534) - postCfg upgrade output refers to calpont
* [MCOL-550](https://jira.mariadb.org/browse/MCOL-550) - Possible mem leak and crash in columnstore's mysqld
* [MCOL-553](https://jira.mariadb.org/browse/MCOL-553) - "Too many open files" errors during DBT3 performance test
* [MCOL-561](https://jira.mariadb.org/browse/MCOL-561) - Can't create view by using ColumnStore's windowing funcion SQL
* [MCOL-574](https://jira.mariadb.org/browse/MCOL-574) - Cross Engine step tries to use a bad UDS path for localhost
* [MCOL-579](https://jira.mariadb.org/browse/MCOL-579) - Enabled harderning compile flags
* [MCOL-622](https://jira.mariadb.org/browse/MCOL-622) - [MariaDB 10.2](../../../community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) create front end for "VAR\_SAMP" window function
* [MCOL-623](https://jira.mariadb.org/browse/MCOL-623) - [MariaDB 10.2](../../../community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) create "STDDEV\_SAMP" Windows function
* [MCOL-628](https://jira.mariadb.org/browse/MCOL-628) - getSystemResourceUsage doesnt work on non-root install
* [MCOL-636](https://jira.mariadb.org/browse/MCOL-636) - Performance improvement with string handling
* [MCOL-642](https://jira.mariadb.org/browse/MCOL-642) - Add BLOB/TEXT detection
* [MCOL-663](https://jira.mariadb.org/browse/MCOL-663) - Restarting installation fails if installed on secondary interface
* [MCOL-664](https://jira.mariadb.org/browse/MCOL-664) - TEXT columns need to support the same functions as VARCHAR
* [MCOL-675](https://jira.mariadb.org/browse/MCOL-675) - calsettrace(1) can cause a mysqld crash
* [MCOL-677](https://jira.mariadb.org/browse/MCOL-677) - Columnstore executes join on incompatible types
* [MCOL-686](https://jira.mariadb.org/browse/MCOL-686) - Using BETWEEN together with date functions in WHERE clause 100x slower than InfiniDB
* [MCOL-702](https://jira.mariadb.org/browse/MCOL-702) - multi node package install with non login su won't start
* [MCOL-703](https://jira.mariadb.org/browse/MCOL-703) - postConfigure should check for local rpm / bins existing
* [MCOL-729](https://jira.mariadb.org/browse/MCOL-729) - Columnstore Cluster Test Tool - add check for mariadb-libs base install
* [MCOL-787](https://jira.mariadb.org/browse/MCOL-787) - run command to create system tables after startsystem
* [MCOL-799](https://jira.mariadb.org/browse/MCOL-799) - INSERT...SELECT with window functions fail
* [MCOL-819](https://jira.mariadb.org/browse/MCOL-819) - mysqld not shutdown by shutdownsystem commands, sometimes
* [MCOL-833](https://jira.mariadb.org/browse/MCOL-833) - could not open file for OID after a outage recover from pm2 PrimProc
* [MCOL-887](https://jira.mariadb.org/browse/MCOL-887) - Merge [MariaDB 10.2.8](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)
* [MCOL-892](https://jira.mariadb.org/browse/MCOL-892) - 1.0.11 upgrade failed when base directory is nfs mounted

In addition, all bugs fixed in MariaDB ColumnStore 1.0.11 and earlier are implicitly included in this release.

## Upgrade

Multi version upgrades are not supported, please upgrade versions prior to 1.0.11 before upgrading to 1.1.0:

* [1.0.11 GA to 1.1.0 Beta upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md)

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
* [MCOL-783](https://jira.mariadb.org/browse/MCOL-783) : Recursive Common Table Expressions caused mysqld to crash
* [MCOL-895](https://jira.mariadb.org/browse/MCOL-895) : INSERT after ALTER TABLE can corrupt HWM
* [MCOL-912](https://jira.mariadb.org/browse/MCOL-912) : fter adding two PMs with gluster, cpimport failed on newly added PMs. The system must be restarted after adding PM modules with data redundancy / gluster storage.
* [MCOL-916](https://jira.mariadb.org/browse/MCOL-916) : Gluster failover: Stack did not recover completely after PM1 reboot. Under certain topologies (replication count < pm count) failover may not work correctly. Recommend limiting testing to replication count = pm count.
* [MCOL-926](https://jira.mariadb.org/browse/MCOL-926) : multiple application of a UDAF on the same column will result in a null value except for the first occurence.
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

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.1.0 Beta version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8.6, Debian 9.1, RedHat 6, RedHat 7, SUSE 12, and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/downloads/columnstore)
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.1.0". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.1.0)
* MariaDB Server - [Source code based on MariaDB Server 10.2.8 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.1.0)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
