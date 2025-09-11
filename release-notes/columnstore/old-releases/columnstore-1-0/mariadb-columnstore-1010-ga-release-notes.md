# MariaDB ColumnStore 1.0.10 GA Release Notes

**Release date:** 28th July 2017

[MariaDB ColumnStore 1.0.10](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) is a maintenance GA release of MariaDB ColumnStore. This release of MariaDB ColumnStore provides improvements over the previous 1.0.9 GA release.

MariaDB ColumnStore 1.0.10 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-802](https://jira.mariadb.org/browse/MCOL-802) - MariaDB ColumnStore is now based on MariaDB Server 10.1.25.
* [MCOL-723](https://jira.mariadb.org/browse/MCOL-723) - The MariaDB ColumnStore Cluster Tester tool is included in the install. This can be run to validate ColumnStore pre-requisities across servers prior to performing a multi node postConfigure. For further details please see [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md).

## Bugs and issues fixed

* [MCOL-379](https://jira.mariadb.org/browse/MCOL-379) - system down and high memory alarm set after install
* [MCOL-472](https://jira.mariadb.org/browse/MCOL-472) - mysqld not shutdown by shutdownsystem commands, sometimes
* [MCOL-538](https://jira.mariadb.org/browse/MCOL-538) - Argument in alias circumvents /.my.cnf option file
* [MCOL-626](https://jira.mariadb.org/browse/MCOL-626) - addModule should not be alowed on single-server installs
* [MCOL-674](https://jira.mariadb.org/browse/MCOL-674) - Update a column with a subquery resulted NULLs in the target column
* [MCOL-699](https://jira.mariadb.org/browse/MCOL-699) - mcsadmin display issue for getModuleDisk
* [MCOL-711](https://jira.mariadb.org/browse/MCOL-711) - GROUP\_CONCAT function got ColumnStore stuck in "Join or subselect exceeds memory limit" error
* [MCOL-715](https://jira.mariadb.org/browse/MCOL-715) - Amazon Install - error when setting up UM storage as 'io1' volume type
* [MCOL-719](https://jira.mariadb.org/browse/MCOL-719) - Unexpected results using LEAST or GREATEST on aggregate
* [MCOL-723](https://jira.mariadb.org/browse/MCOL-723) - MariabDB ColumnStore Cluster tester tool
* [MCOL-730](https://jira.mariadb.org/browse/MCOL-730) - cross engine join query select on decimal bad precision/scale
* [MCOL-732](https://jira.mariadb.org/browse/MCOL-732) - Merge Server 10.1.24
* [MCOL-734](https://jira.mariadb.org/browse/MCOL-734) - Error messages referenced an invalid OAM command unassignPmDbrootConfig
* [MCOL-736](https://jira.mariadb.org/browse/MCOL-736) - transaction gets autocommitted if non columnstore query executed
* [MCOL-773](https://jira.mariadb.org/browse/MCOL-773) - system not startup up via postConfigure/startsSystem - remote\_command issue
* [MCOL-793](https://jira.mariadb.org/browse/MCOL-793) - ORDER BY NULL breaks subsequent query
* [MCOL-794](https://jira.mariadb.org/browse/MCOL-794) - query cache not work with all engine with columnstore
* [MCOL-802](https://jira.mariadb.org/browse/MCOL-802) - Merge [MariaDB 10.1.25](../../../community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10125-release-notes.md) into 1.0
* [MCOL-811](https://jira.mariadb.org/browse/MCOL-811) - Logs going to system journal in Ubuntu instead of log files
* [MCOL-814](https://jira.mariadb.org/browse/MCOL-814) - PrimProc could not open file for OID after a outage recover from pm2 PrimProc
* [MCOL-829](https://jira.mariadb.org/browse/MCOL-829) - Implement stored procedure INSERT...SELECT
* [MCOL-834](https://jira.mariadb.org/browse/MCOL-834) - PrimProc thread leak if ExeMgr dies

## Upgrade

Multi version upgrades are not supported, please upgrade versions prior to 1.0.9 before upgrading to 1.0.10:

* [1.0.9 GA to 1.0.10 upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md)

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

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.0.10 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8.6, RedHat 6, RedHat 7, SUSE 12, and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/downloads/columnstore)
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.0.10". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine)
* MariaDB Server - [Source code based on MariaDB Server 10.1.25 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
