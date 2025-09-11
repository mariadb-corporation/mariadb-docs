# MariaDB ColumnStore 1.0.5 Release Candidate Release Notes

**Release date:** 24th November 2016

[MariaDB ColumnStore 1.0.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) is a Release Candidate release of MariaDB ColumnStore. This release of MariaDB ColumnStore provides improvements over the previous 1.0.4 beta release.

MariaDB ColumnStore 1.0.5 is a [_**Release Candidate**_](../../../community-server/about/release-criteria.md) release.

**Do not use&#x20;**_**Release Candidate**_**&#x20;releases on production systems!**

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable Changes

* [MCOL-385](https://jira.mariadb.org/browse/MCOL-385) - 10.1.19 Merge : ColumnStore is now based off the MariaDB Server release 10.1.19.
* [MCOL-404](https://jira.mariadb.org/browse/MCOL-404) - non-root install fails on centos7 : Non root installs now work.
* [MCOL-309](https://jira.mariadb.org/browse/MCOL-309) - Support method to report on data set size : Information schema tables are created to support reporting on table and column sizes. This is an initial implementation with some further improvements planned for the GA release. See [documentation](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/reference/columnstore-information-schema-tables) for further details.
* An install for Debian 8.6 is now available.

## Bugs and Issues Fixed

Below is list of some of the bugs and issues fixed. A number of regression test and build related fixes were made in addition. For the complete list please see [here](https://jira.mariadb.org/issues/?jql=project%20%3D%20MCOL%20AND%20status%20%3D%20CLOSED%20and%20fixVersion%20%3D%201.0.5%20ORDER%20BY%20priority%20DESC%2C%20updated%20DESC)

* [MCOL-37](https://jira.mariadb.org/browse/MCOL-37) - Five windowing functions that are returning incorrect results
* [MCOL-61](https://jira.mariadb.org/browse/MCOL-61) - Create AMI for MariaDB ColumnStore
* [MCOL-91](https://jira.mariadb.org/browse/MCOL-91) - SQL Statement cause syntax error when vtable mode = 1
* [MCOL-121](https://jira.mariadb.org/browse/MCOL-121) - MySQL client reports "stage 2 - enabling keys" for every query against a CS table.
* [MCOL-129](https://jira.mariadb.org/browse/MCOL-129) - INSERTIONS are lost, no ERROR reported for out-of-range values in STRICT mode
* [MCOL-218](https://jira.mariadb.org/browse/MCOL-218) - DROP DATABASE on a database with all empty tables is not accepted
* [MCOL-260](https://jira.mariadb.org/browse/MCOL-260) - update two tables with a subquery fails
* [MCOL-263](https://jira.mariadb.org/browse/MCOL-263) - With suspendDatabaseWrite enabled, LDI return an incorrect msg
* [MCOL-273](https://jira.mariadb.org/browse/MCOL-273) - During restart, ProcessManager sometimes generates a warning
* [MCOL-278](https://jira.mariadb.org/browse/MCOL-278) - drop table if exists creates error if table doesn't exist and schema out of synch
* [MCOL-309](https://jira.mariadb.org/browse/MCOL-309) - Support method to report on data set size
* [MCOL-334](https://jira.mariadb.org/browse/MCOL-334) - Bad NULL match in view subquery
* [MCOL-350](https://jira.mariadb.org/browse/MCOL-350) - can't select date value of 0000-00-00
* [MCOL-352](https://jira.mariadb.org/browse/MCOL-352) - substr() on view returns NULL sometimes
* [MCOL-361](https://jira.mariadb.org/browse/MCOL-361) - table mode 0 and 2 has bad result
* [MCOL-370](https://jira.mariadb.org/browse/MCOL-370) - enableLog / disableLog don't work
* [MCOL-372](https://jira.mariadb.org/browse/MCOL-372) - dbrm-worker node continuing issues socket read error log
* [MCOL-385](https://jira.mariadb.org/browse/MCOL-385) - 10.1.19 Merge
* [MCOL-386](https://jira.mariadb.org/browse/MCOL-386) - postConfigure should show cause of write error.
* [MCOL-387](https://jira.mariadb.org/browse/MCOL-387) - releasenum gets messed up when not hard set
* [MCOL-398](https://jira.mariadb.org/browse/MCOL-398) - remove the restriction in postConfigure for UM memory at 16G
* [MCOL-404](https://jira.mariadb.org/browse/MCOL-404) - non-root install fails on centos7

## Upgrade

Multi version upgrades are not supported, please upgrade versions prior to 1.0.4 before upgrading to 1.0.5. Details on upgrading from version to 1.0.4 to 1.0.5 can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md).

Upgrade from MariaDB ColumnStore Alpha versions 1.0.0 to 1.0.2 is not supported, please upgrade to version 1.0.4 prior to upgrading to 1.0.5.

## Known Issues and Limitations

There are a number bugs and known limitations within this beta version of MariaDB ColumnStore, the most serious of these are listed below.

* [MCOL-73](https://jira.mariadb.org/browse/MCOL-73)): Wide table formatted display causes frontend to return error
  * MariaDB ColumnStore supports wide tables storage
  * Displaying the query results on a large number of columns without formatting the column works
  * Displaying the query results on a large number of columns with formatting causes error at MariaDB Server level
* [MCOL-271](https://jira.mariadb.org/browse/MCOL-271) empty string values are treated as NULL. This means you cannot insert empty values into a NOT NULL string column.
* [MCOL-364](https://jira.mariadb.org/browse/MCOL-364): In a multi UM configuration where the default storage engine has been set to columnstore replicated tables are not created as columnstore tables. Avoid overriding the default storage engine and specify engine=columnstore on all table DDL.
* [MCOL-365](https://jira.mariadb.org/browse/MCOL-365): Log files created by load data infile remain in the bulk/data/log and /tmp directories. If storage is a concern these can safely be removed.
* [MCOL-421](https://jira.mariadb.org/browse/MCOL-421): If a password was set for the root localhost user in the prior installed version then upgrade will fail. The workaround is to clear the password temporarily prior to the upgrade and reapply after the upgrade is complete.
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

RPM and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.0.5 RC version.

* The supported OS for this RC version are CentOS 6, CentOS 7, Debian 8.6, and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/my_portal/download/mariadb-columnstore)

## Source Code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine—[Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine)
* MariaDB Server - [Source code based on MariaDB Server 10.1.19 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
