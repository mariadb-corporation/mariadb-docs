# MariaDB ColumnStore 1.0.4 Beta Release Notes

**Release date:** 26th October 2016

[MariaDB ColumnStore 1.0.4](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a beta release of MariaDB ColumnStore. This is the first beta release of MariaDB ColumnStore with improvements over the previous 1.0.3 alpha release.

MariaDB ColumnStore 1.0.4 is a [_**Beta**_](../../../community-server/about/release-criteria.md) release.

**Do not use&#x20;**_**beta**_**&#x20;releases on production systems!**

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable Changes

* [MCOL-303](https://jira.mariadb.org/browse/MCOL-303) - A build related performance regression in the 1.0.2 release has been fixed restoring performance to be comparable with the prior Infinidb versions.
* [MCOL-251](https://jira.mariadb.org/browse/MCOL-251) - MariaDB ColumnStore no longer issues snmp traps. As a result of this 2 prompts are removed from the postConfigure script relating to this.
* [MCOL-325](https://jira.mariadb.org/browse/MCOL-325) - the WEEK and YEARWEEK functions are now consistent with the MariaDB server implementation.
* [MCOL-305](https://jira.mariadb.org/browse/MCOL-305) - The base MariaDB server version is now 10.1.18. As a result of this the perl-DBD-MySQL package may need to be installed using an OS appropriate tool prior to installation of MariaDB ColumnStore.

## Bugs and Issues Fixed

Below is list of some of the bugs and issues fixed. A number of regression test and build related fixes were made in addition. For the complete list please see [here](https://jira.mariadb.org/issues/?jql=project%20%3D%20MCOL%20AND%20status%20%3D%20CLOSED%20and%20fixVersion%20%3D%201.0.4%20ORDER%20BY%20priority%20DESC%2C%20updated%20DESC)

* [MCOL-21](https://jira.mariadb.org/browse/MCOL-21) - Create table failed due to Error updating BRM block version buffer overflow error
* [MCOL-74](https://jira.mariadb.org/browse/MCOL-74) - Nth\_value() windowing function does not exist error
* [MCOL-75](https://jira.mariadb.org/browse/MCOL-75) - Last\_value() Windowing function returned an syntax error
* [MCOL-78](https://jira.mariadb.org/browse/MCOL-78) - ROUND() function returns incorrect value
* [MCOL-98](https://jira.mariadb.org/browse/MCOL-98) - Behavioral differences between MariaDB and ColumnStore for few functions
* [MCOL-99](https://jira.mariadb.org/browse/MCOL-99) - EXTRACT() function returns an exception when processing \*MICROSECONDS
* [MCOL-115](https://jira.mariadb.org/browse/MCOL-115) - Auto rollback is not occur when update caused a version-buffer-full error (autocommit=1)
* [MCOL-176](https://jira.mariadb.org/browse/MCOL-176) - DIV operator crashes PrimProc
* [MCOL-251](https://jira.mariadb.org/browse/MCOL-251) - does columnstore need to issue snmp traps?
* [MCOL-285](https://jira.mariadb.org/browse/MCOL-285) - Columnstore is few times slower than InfiniDB for DBT3 query #1
* [MCOL-287](https://jira.mariadb.org/browse/MCOL-287) - CPImport performance slowdown by 27% or more from a1.0.1 to 1.0.2
* [MCOL-289](https://jira.mariadb.org/browse/MCOL-289) - test001 bug2954.sql fails
* [MCOL-290](https://jira.mariadb.org/browse/MCOL-290) - decomsrv app reporting incorrect state
* [MCOL-292](https://jira.mariadb.org/browse/MCOL-292) - CentOS 7 RPM's don't depend on Boost
* [MCOL-297](https://jira.mariadb.org/browse/MCOL-297) - CHARACTER\_LENGTH(datetime) returns wrong length
* [MCOL-299](https://jira.mariadb.org/browse/MCOL-299) - CHARACTER\_LENGTH(float/decimal) returns wrong length
* [MCOL-302](https://jira.mariadb.org/browse/MCOL-302) - rpm -U reports errors
* [MCOL-303](https://jira.mariadb.org/browse/MCOL-303) - Performance drop between 1.0.1 and 1.0.2
* [MCOL-305](https://jira.mariadb.org/browse/MCOL-305) - MariaDB Server 10.1.18 Merge
* [MCOL-308](https://jira.mariadb.org/browse/MCOL-308) - Add CMake and RPM build checks for net-snmp
* [MCOL-325](https://jira.mariadb.org/browse/MCOL-325) - WEEK() handling needs to match MySQL's
* [MCOL-326](https://jira.mariadb.org/browse/MCOL-326) - RAND() behaves differently with negative seeds
* [MCOL-328](https://jira.mariadb.org/browse/MCOL-328) - REVERSE() adds extra character
* [MCOL-329](https://jira.mariadb.org/browse/MCOL-329) - Functions casting date/datetime 0 to NULL
* [MCOL-330](https://jira.mariadb.org/browse/MCOL-330) - Datetime to int conversion returns strange values
* [MCOL-331](https://jira.mariadb.org/browse/MCOL-331) - INSERT() function misbehaves with our of range parameters
* [MCOL-332](https://jira.mariadb.org/browse/MCOL-332) - MONTHNAME() to int should equal 0
* [MCOL-333](https://jira.mariadb.org/browse/MCOL-333) - subtime() off by one second
* [MCOL-335](https://jira.mariadb.org/browse/MCOL-335) - Many Window Functions erroniously return 0
* [MCOL-341](https://jira.mariadb.org/browse/MCOL-341) - mts\_insert\_select producing bad results
* [MCOL-343](https://jira.mariadb.org/browse/MCOL-343) - ha\_calpont\_execplan assigns String::ptr() to std::string
* [MCOL-347](https://jira.mariadb.org/browse/MCOL-347) - NULLIF datetime compare with date fails

## Upgrade

Multi version upgrades are not supported, please upgrade versions prior to 1.0.3 before upgrading to 1.0.4. Details on upgrading from version to 1.0.3 to 1.0.4 can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md).

Upgrade from MariaDB ColumnStore Alpha versions 1.0.0 to 1.0.2 is not supported, please upgrade to version 1.0.3 prior to upgrading to 1.0.4.

## Known Issues and Limitations

There are a number bugs and known limitations within this beta version of MariaDB ColumnStore, the most serious of these are listed below. These are expected to be fixed before the GA release.

* [MCOL-37](https://jira.mariadb.org/browse/MCOL-37): Following three window functions do not return correct value
  * FIRST\_VALUE
  * LEAD
  * LAG
* [MCOL-73](https://jira.mariadb.org/browse/MCOL-73)): Wide table formatted display causes frontend to return error
  * MariaDB ColumnStore supports wide tables storage
  * Displaying the query results on a large number of columns without formatting the column works
  * Displaying the query results on a large number of columns with formatting causes error at MariaDB Server level
* [MCOL-129](https://jira.mariadb.org/browse/MCOL-129) Direct insert of column store reserved values, for example -128 for tinyint in STRICT\_ALL\_TABLES mode will result in no insert and no warning. Be aware of the range limits for datatypes and avoid using STRICT\_ALL\_TABLES mode.
* [MCOL-271](https://jira.mariadb.org/browse/MCOL-271) empty string values are treated as NULL. This means you cannot insert empty values into a NOT NULL string column.
* [MCOL-334](https://jira.mariadb.org/browse/MCOL-334): Subquery using IN with VIEW returns incorrect results. Queries selecting from view and using IN in where clause with a subquery on another view returns incorrect results. If this functionality is desired then run set infinidb\_vtable\_mode=0; before executing the query. This will have a reduced performance impact.
* [MCOL-350](https://jira.mariadb.org/browse/MCOL-350): Selects with a where clause of = '0000-00-00' do not match. Datetime is not affected.
* [MCOL-364](https://jira.mariadb.org/browse/MCOL-364): In a multi UM configuration where the default storage engine has been set to columnstore replicated tables are not created as columnstore tables. Avoid overriding the default storage engine and specify engine=columnstore on all table DDL.
* [MCOL-365](https://jira.mariadb.org/browse/MCOL-365): Log files created by load data infile remain in the bulk/data/log and /tmp directories. If storage is a concern these can safely be removed.
* [MCOL-372](https://jira.mariadb.org/browse/MCOL-372): Frequent socket timeout logging. This can be suppressed through configuring a syslog blacklist file and restart the syslog daemon, for example /etc/rsyslog.d/01-blocklist.conf contains:

```
:msg,contains,"CAL0071: InetStreamSocket::read: timeout during readToMagic: socket read error: Success; InetStreamSocket:" ~
```

* [MCOL-404](https://jira.mariadb.org/browse/MCOL-404): Non root user install does not work. Install as root instead for this release.
* The current logging default generates full verbose debug logs. This can be controlled by making logging configuration changes as described [here](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/management/columnstore-system/columnstore-system-monitoring-configuration).
* While Millisecond and Microsecond storage is supported for datetime, time and timestamp columns, at this time the query results cannot return millisecond and microseconds.
* UTF-8 Limitation
  * UTF-8 must be declared at the table level if the instance has been set up with a UTF-8 profile. Tables created with a non-matching character set will yield indeterminate results.
  * Viewing SQL output should be done using client software that supports UTF-8 character sets.
  * UTF-8 characters are not supported in object names.
* Known security issues are documented [here](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/security/columnstore-security-vulnerabilities).

## Documentation

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md)

## Packaging

RPM and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.0.4 beta version.

* The supported OS for this Alpha version are CentOS 6, CentOS 7 and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/my_portal/download/mariadb-columnstore)

## Source Code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine)
* MariaDB Server - [Source code based on MariaDB Server 10.1.18 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
