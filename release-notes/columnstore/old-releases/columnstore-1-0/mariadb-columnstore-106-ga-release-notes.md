# MariaDB ColumnStore 1.0.6 GA Release Notes

**Release date:** 14th December 2016

[MariaDB ColumnStore 1.0.6](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) is a GA release of MariaDB ColumnStore. This release of MariaDB ColumnStore provides improvements over the previous 1.0.5 RC release.

MariaDB ColumnStore 1.0.6 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable Changes

* [MCOL-272](https://jira.mariadb.org/browse/MCOL-272) - generate debian packages: A debian package build is now available for Debian and Ubuntu in addition to the binary install.
* [MCOL-307](https://jira.mariadb.org/browse/MCOL-307) - implement redistribution logic : An mcsadmin utility command is provided to support redistribution of partitions. For more details see the [columnstore-redistribute-data](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/management/columnstore-system/columnstore-redistribute-data) article.
* [MCOL-311](https://jira.mariadb.org/browse/MCOL-311) - utility for finding objects file : An mcsadmin utility command is provided to support locating files by table or column. For more details run 'help findObjectFile'\
  in the mcsadmin utility.
* [MCOL-406](https://jira.mariadb.org/browse/MCOL-406) - Stored procedures required for I\_S tables : Convenience stored procedures are now provided for common tasks in querying the ColumnStore information schema tables. For more details see the [columnstore-information-schema-tables](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/reference/columnstore-information-schema-tables) article.

## Bugs and Issues Fixed

* [MCOL-272](https://jira.mariadb.org/browse/MCOL-272) - generate debian packages
* [MCOL-307](https://jira.mariadb.org/browse/MCOL-307) - implement redistribution logic
* [MCOL-311](https://jira.mariadb.org/browse/MCOL-311) - utility for finding objects file
* [MCOL-398](https://jira.mariadb.org/browse/MCOL-398) - remove the restriction in postConfigure for UM memory at 16G
* [MCOL-406](https://jira.mariadb.org/browse/MCOL-406) - Stored procedures required for I\_S tables
* [MCOL-420](https://jira.mariadb.org/browse/MCOL-420) - Add alias for cpimport in columnstoreAlias
* [MCOL-421](https://jira.mariadb.org/browse/MCOL-421) - system upgrade install fails when a mysql root password is set
* [MCOL-422](https://jira.mariadb.org/browse/MCOL-422) - Amazon AMI single-server Columnstore didn't restart on a stop/start
* [MCOL-424](https://jira.mariadb.org/browse/MCOL-424) - cross engine subquery losing where clause causing incorrect results
* [MCOL-430](https://jira.mariadb.org/browse/MCOL-430) - invalid null date values for cross engine join query
* [MCOL-433](https://jira.mariadb.org/browse/MCOL-433) - Small row results can cause CrossEngine buffer underflow
* [MCOL-434](https://jira.mariadb.org/browse/MCOL-434) - DecomSvr fails to cleanly start when a Amazon Instance is stopped/started
* [MCOL-435](https://jira.mariadb.org/browse/MCOL-435) - Amazon AMi multi-node system didnt successfully restart after a stop/start
* [MCOL-441](https://jira.mariadb.org/browse/MCOL-441) - Segfault on query after an error
* [MCOL-442](https://jira.mariadb.org/browse/MCOL-442) - Default date value doesn't allow zero date
* [MCOL-457](https://jira.mariadb.org/browse/MCOL-457) - null bit header error when the number of NULL columns is divisible by 8 and the last column is a NOT NULL

## Upgrade

Multi version upgrades are not supported, please upgrade versions prior to 1.0.4 before upgrading to 1.0.6:

* [1.0.4 Beta to 1.0.6 upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md)
* [1.0.5 RC to 1.0.6 upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md)

Upgrade from MariaDB ColumnStore Alpha versions 1.0.0 to 1.0.2 is not supported, please upgrade to version 1.0.4 or 1.0.5 prior to upgrading to 1.0.6.

## Known Issues and Limitations

There are a number bugs and known limitations within this beta version of MariaDB ColumnStore, the most serious of these are listed below.

* [MCOL-73](https://jira.mariadb.org/browse/MCOL-73)): Wide table formatted display causes frontend to return error
  * MariaDB ColumnStore supports wide tables storage
  * Displaying the query results on a large number of columns without formatting the column works
  * Displaying the query results on a large number of columns with formatting causes error at MariaDB Server level
* [MCOL-271](https://jira.mariadb.org/browse/MCOL-271) empty string values are treated as NULL. This means you cannot insert empty values into a NOT NULL string column.
* [MCOL-364](https://jira.mariadb.org/browse/MCOL-364): In a multi UM configuration where the default storage engine has been set to columnstore replicated tables are not created as columnstore tables. Avoid overriding the default storage engine and specify engine=columnstore on all table DDL.
* [MCOL-365](https://jira.mariadb.org/browse/MCOL-365): Log files created by load data infile remain in the bulk/data/log and /tmp directories. If storage is a concern these can safely be removed.
* [MCOL-454](https://jira.mariadb.org/browse/MCOL-454) : columnstore\_info's total\_usage() and table\_usage() reported 0 usage on multi-node configuration. The stored procedures and information\_schema.columnstore\_files return incorrect path and size information for a multi node install.
* [MCOL-463](https://jira.mariadb.org/browse/MCOL-463) : gluster storage option in installer fails withe error. The installer option to install optimized for gluster storage will fail with an error. Manually set up gluster volumes can be used with the 'External' storage option.
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

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.0.6 RC version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8.6, RedHat 6, RedHat 7, and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/downloads/columnstore)
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.0.6". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md).
* Instructions for setting up OS software repositories as the download mechanism will be published shortly.

## Source Code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine)
* MariaDB Server - [Source code based on MariaDB Server 10.1.19 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
