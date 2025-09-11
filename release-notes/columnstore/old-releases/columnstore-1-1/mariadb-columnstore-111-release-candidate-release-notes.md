# MariaDB ColumnStore 1.1.1 Release Candidate Release Notes

**Release date:** 3rd November 2017

[MariaDB ColumnStore 1.1.1](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) is a Release Candidate release of MariaDB ColumnStore. This is the second release of the MariaDB ColumnStore 1.1 series. The MariaDB ColumnStore 1.1 series provides several new features and improvements over the MariaDB ColumnStore 1.0 release.

MariaDB ColumnStore 1.1.1 is a [_**Release Candidate**_](../../../community-server/about/release-criteria.md) release.

**Do not use&#x20;**_**Release Candidate**_**&#x20;releases on production systems!**

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

1. MariaDB ColumnStore 1.1.1 is based on MariaDB Server 10.2.10
2. Java and Python bindings are available for the Write Data API

## Bugs and issues fixed

* [MCOL-662](https://jira.mariadb.org/browse/MCOL-662) - Unexpected results in cross engine join
* [MCOL-667](https://jira.mariadb.org/browse/MCOL-667) - Installation of MCS updates the root .bashrc file
* [MCOL-750](https://jira.mariadb.org/browse/MCOL-750) - make the remote server install scripts run faster by checking for ssh/scp return codes
* [MCOL-783](https://jira.mariadb.org/browse/MCOL-783) - Recursive Common Table Expressions caused mysqld to crash
* [MCOL-786](https://jira.mariadb.org/browse/MCOL-786) - redistribute remove moved data from removed node to one node
* [MCOL-859](https://jira.mariadb.org/browse/MCOL-859) - Running TRUNCATE on many tables in parallel seems to eventually deadlock
* [MCOL-877](https://jira.mariadb.org/browse/MCOL-877) - Not all data escaped when inserting with select statement from innodb table into columnstore
* [MCOL-895](https://jira.mariadb.org/browse/MCOL-895) - INSERT after ALTER TABLE can corrupt HWM
* [MCOL-898](https://jira.mariadb.org/browse/MCOL-898) - NULL operand ignored in vtable mode when querying view
* [MCOL-911](https://jira.mariadb.org/browse/MCOL-911) - exemgr crashes with a nested aggregate multiplication query
* [MCOL-913](https://jira.mariadb.org/browse/MCOL-913) - DistributeConfigFile Failed messages after adding modules
* [MCOL-914](https://jira.mariadb.org/browse/MCOL-914) - Warning messages for the RemoveModule command should be improved
* [MCOL-915](https://jira.mariadb.org/browse/MCOL-915) - Improve the output from the RemoveModule command
* [MCOL-916](https://jira.mariadb.org/browse/MCOL-916) - Gluster failover: Stack did not recover completely after PM1 reboot
* [MCOL-926](https://jira.mariadb.org/browse/MCOL-926) - UDAF returns null for 2nd or more applications against same column
* [MCOL-928](https://jira.mariadb.org/browse/MCOL-928) - postConfigure is not detecting glusterfs on Debian9.1 for non-root user
* [MCOL-929](https://jira.mariadb.org/browse/MCOL-929) - switchparentoammodule cores when pm2 is active on a 1um/2pm Data Redundancy system
* [MCOL-938](https://jira.mariadb.org/browse/MCOL-938) - columnstore replication failover from master updates server-id
* [MCOL-943](https://jira.mariadb.org/browse/MCOL-943) - multi-node postConfigure fails when mysql password is set.
* [MCOL-944](https://jira.mariadb.org/browse/MCOL-944) - coalesce with count(distinct) can lead to incorrect results
* [MCOL-945](https://jira.mariadb.org/browse/MCOL-945) - MariaDBReplication slave messages is incorrectly sending updates to PM nodes
* [MCOL-946](https://jira.mariadb.org/browse/MCOL-946) - migrate to swig for mcsapi python binding
* [MCOL-951](https://jira.mariadb.org/browse/MCOL-951) - tpcds query 17 fails with invalid colum width
* [MCOL-959](https://jira.mariadb.org/browse/MCOL-959) - invalid LD\_LIBRARY\_PATH for non root install
* [MCOL-963](https://jira.mariadb.org/browse/MCOL-963) - self join cte queries from tpcds alternately fail with parsing error and succeed but with incorrect results
* [MCOL-965](https://jira.mariadb.org/browse/MCOL-965) - group\_contact with order by on joined table causes error
* [MCOL-971](https://jira.mariadb.org/browse/MCOL-971) - 1.0 to 1.1 non-root upgrade issue - problem shows after a reboot, still using 1.0 ENV variables
* [MCOL-972](https://jira.mariadb.org/browse/MCOL-972) - PmMaxMemorySmallSide configuration value not carried forward in upgrade
* [MCOL-973](https://jira.mariadb.org/browse/MCOL-973) - ArithmaticColumn parsing can cause crash
* [MCOL-979](https://jira.mariadb.org/browse/MCOL-979) - Crash with LEAD function in ColumnStore with 'char' field type
* [MCOL-982](https://jira.mariadb.org/browse/MCOL-982) - Merge [MariaDB 10.2.9](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1029-release-notes.md) into ColumnStore
* [MCOL-984](https://jira.mariadb.org/browse/MCOL-984) - Error 1815 after several executions of example/basic\_bulk\_insert having SMALLINT in t1
* [MCOL-988](https://jira.mariadb.org/browse/MCOL-988) - 1um/2pm DataRep system starting up without a ProcessManager in HOT\_STANDBY state
* [MCOL-990](https://jira.mariadb.org/browse/MCOL-990) - provide a resetRow method
* [MCOL-992](https://jira.mariadb.org/browse/MCOL-992) - java binding for mcsapi
* [MCOL-1000](https://jira.mariadb.org/browse/MCOL-1000) - Merge [MariaDB 10.2.10](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10210-release-notes.md)

In addition, all bugs fixed in MariaDB ColumnStore 1.0.11 and earlier are implicitly included in this release.

## Upgrade

Multi version upgrades are not supported, please upgrade versions prior to 1.1.0 before upgrading to 1.1.1:

* [1.1.0 Beta to 1.1.1 RC upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md)

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
* [MCOL-912](https://jira.mariadb.org/browse/MCOL-912) : fter adding two PMs with gluster, cpimport failed on newly added PMs. The system must be restarted after adding PM modules with data redundancy / gluster storage.
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

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.1.1 RC version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8.6, Debian 9.1, RedHat 6, RedHat 7, SUSE 12, and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/downloads/columnstore)
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.1.0". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.1.1)
* MariaDB Server - [Source code based on MariaDB Server 10.2.10 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.1.1)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools/tree/columnstore-1.1.0)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api/tree/columnstore-1.1.1)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
