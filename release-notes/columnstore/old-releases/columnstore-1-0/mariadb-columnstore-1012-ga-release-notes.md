# MariaDB ColumnStore 1.0.12 GA Release Notes

**Release date:** 14th December 2017

[MariaDB ColumnStore 1.0.12](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) is a maintenance GA release of MariaDB ColumnStore. This release of MariaDB ColumnStore provides improvements over the previous 1.0.11 GA release.

MariaDB ColumnStore 1.0.12 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-1032](https://jira.mariadb.org/browse/MCOL-1032) - The base MariaDB server version is now [10.1.29](../../../community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10129-release-notes.md) which include several maintenance and security fixes.

## Bugs and issues fixed

* [MCOL-444](https://jira.mariadb.org/browse/MCOL-444) - split character import issue
* [MCOL-445](https://jira.mariadb.org/browse/MCOL-445) - configxml.sh should be case in-sensitive.
* [MCOL-446](https://jira.mariadb.org/browse/MCOL-446) - mycnf config change request
* [MCOL-662](https://jira.mariadb.org/browse/MCOL-662) - Unexpected results in cross engine join
* [MCOL-837](https://jira.mariadb.org/browse/MCOL-837) - postConfigure - WARNING: Mismatch between FilesPerColumnPartition check should be removed
* [MCOL-859](https://jira.mariadb.org/browse/MCOL-859) - Running TRUNCATE on many tables in parallel seems to eventually deadlock
* [MCOL-877](https://jira.mariadb.org/browse/MCOL-877) - Not all data escaped when inserting with select statement from innodb table into columnstore
* [MCOL-890](https://jira.mariadb.org/browse/MCOL-890) - group\_contact returns garbage
* [MCOL-892](https://jira.mariadb.org/browse/MCOL-892) - 1.0.11 upgrade failed when base directory is nfs mounted
* [MCOL-895](https://jira.mariadb.org/browse/MCOL-895) - INSERT after ALTER TABLE can corrupt HWM
* [MCOL-898](https://jira.mariadb.org/browse/MCOL-898) - NULL operand ignored in vtable mode when querying view
* [MCOL-911](https://jira.mariadb.org/browse/MCOL-911) - exemgr crashes with a nested aggregate multiplication query
* [MCOL-936](https://jira.mariadb.org/browse/MCOL-936) - Binary installer fails due to expect skipping
* [MCOL-940](https://jira.mariadb.org/browse/MCOL-940) - merge server 10.1.28
* [MCOL-942](https://jira.mariadb.org/browse/MCOL-942) - Setting up of the Master/Slave Replication should not be done on start system
* [MCOL-943](https://jira.mariadb.org/browse/MCOL-943) - multi-node postConfigure fails when mysql password is set.
* [MCOL-944](https://jira.mariadb.org/browse/MCOL-944) - coalesce with count(distinct) can lead to incorrect results
* [MCOL-945](https://jira.mariadb.org/browse/MCOL-945) - MariaDBReplication slave messages is incorrectly sending updates to PM nodes
* [MCOL-954](https://jira.mariadb.org/browse/MCOL-954) - mysqld crashing on slave replication UMs
* [MCOL-973](https://jira.mariadb.org/browse/MCOL-973) - ArithmaticColumn parsing can cause crash
* [MCOL-976](https://jira.mariadb.org/browse/MCOL-976) - System in DBRM\_READ\_ONLY mode after Non-parent PM recovery under DataRedundancy
* [MCOL-979](https://jira.mariadb.org/browse/MCOL-979) - Crash with LEAD function in ColumnStore with 'char' field type
* [MCOL-985](https://jira.mariadb.org/browse/MCOL-985) - buildAggregateColumn needs to handle error code
* [MCOL-994](https://jira.mariadb.org/browse/MCOL-994) - cpimport failed with a "new extent FBO too high for current file error"
* [MCOL-1008](https://jira.mariadb.org/browse/MCOL-1008) - LDI and INSERT...SELECT causes mysqld to crash with long VARCHAR entries
* [MCOL-1016](https://jira.mariadb.org/browse/MCOL-1016) - information\_schema.columnstore\_extents data\_size calculation incorrect
* [MCOL-1029](https://jira.mariadb.org/browse/MCOL-1029) - Logic issue breaking multiple where conditions
* [MCOL-1032](https://jira.mariadb.org/browse/MCOL-1032) - merge server 10.1.29
* [MCOL-1040](https://jira.mariadb.org/browse/MCOL-1040) - ERROR 2013 (HY000): Lost connection to MySQL server during query
* [MCOL-1055](https://jira.mariadb.org/browse/MCOL-1055) - cluster tester issues - backport from 1.1
* [MCOL-1068](https://jira.mariadb.org/browse/MCOL-1068) - Compression ratio miscalculation when there are uncompressed columns
* [MCOL-1082](https://jira.mariadb.org/browse/MCOL-1082) - row\_count() function always returns 0 for any engine
* [MCOL-1095](https://jira.mariadb.org/browse/MCOL-1095) - debian 9.2 cluster tester issues - fix libiao1

## Upgrade

The following procedure outlines upgrading a 1.0.11 ColumnStore install to 1.0.12:

* [1.0.11 GA to 1.0.12 upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md)\
  Multi version upgrades generally will work using the same procedure however we can't test every possible permutation so you should test your specific scenario outside of production first if you wish to try this (and this is good practice regardless).

## Known issues and limitations

There are a number bugs and known limitations within this version of MariaDB ColumnStore, the most serious of these are listed below.

* [MCOL-73](https://jira.mariadb.org/browse/MCOL-73): Wide table formatted display causes frontend to return error
  * MariaDB ColumnStore supports wide tables storage
  * Displaying the query results on a large number of columns without formatting the column works
  * Displaying the query results on a large number of columns with formatting causes error at MariaDB Server level
* [MCOL-271](https://jira.mariadb.org/browse/MCOL-271) empty string values are treated as NULL. This means you cannot insert empty values into a NOT NULL string column.
* [MCOL-364](https://jira.mariadb.org/browse/MCOL-364): In a multi UM configuration where the default storage engine has been set to columnstore replicated tables are not created as columnstore tables. Avoid overriding the default storage engine and specify engine=columnstore on all table DDL.
* [MCOL-365](https://jira.mariadb.org/browse/MCOL-365): Log files created by load data infile remain in the bulk/data/log and /tmp directories. If storage is a concern these can safely be removed.
* [MCOL-463](https://jira.mariadb.org/browse/MCOL-463) : gluster storage option in installer fails with an error. The installer option to install optimized for gluster storage will fail with an error. Manually set up gluster volumes can be used with the 'External' storage option.
* [MCOL-540](https://jira.mariadb.org/browse/MCOL-540) : In a non root Ubuntu install with local query enabled, the PM servers crash and restart on table creation.
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

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.0.12 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8.6, Debian 9.1, RedHat 6, RedHat 7, SUSE 12, and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/downloads/columnstore)
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.0.12". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.0.12)
* MariaDB Server - [Source code based on MariaDB Server 10.1.29 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.0.12)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
