# MariaDB ColumnStore 1.0.16 GA Release Notes

**Release date:** 13th February 2018

[MariaDB ColumnStore 1.0.16](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a maintenance GA release of MariaDB ColumnStore. This release of MariaDB ColumnStore provides improvements over the previous 1.0.15 GA release.

MariaDB ColumnStore 1.0.16 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-2115](https://jira.mariadb.org/browse/MCOL-2115) - The base MariaDB server version is now [10.1.38](../../../community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes.md) which include several maintenance and security fixes.
* [MCOL-2136](https://jira.mariadb.org/browse/MCOL-2136) - Use jemalloc as the main memory allocator. Please ensure jemalloc is installed on each ColumnStore node prior to installation or upgrade.

## Bugs and issues fixed

* [MCOL-1654](https://jira.mariadb.org/browse/MCOL-1654) - Querystats table is broken
* [MCOL-2062](https://jira.mariadb.org/browse/MCOL-2062) - cpimport scientific notation conversion problem
* [MCOL-2136](https://jira.mariadb.org/browse/MCOL-2136) - Use jemalloc as the main memory allocator
* [MCOL-2149](https://jira.mariadb.org/browse/MCOL-2149) - Regression in decimal saturation handling in cpimport
* [MCOL-1974](https://jira.mariadb.org/browse/MCOL-1974) - Bug verification for [MCOL-1844](https://jira.mariadb.org/browse/MCOL-1844) for 1.1.7 and 1.0.16
* [MCOL-2115](https://jira.mariadb.org/browse/MCOL-2115) - Merge [MariaDB 10.1.38](../../../community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes.md) into server tree
* [MCOL-2120](https://jira.mariadb.org/browse/MCOL-2120) - Check NUMA devel package is installed on BuildBot instances

## Upgrade

The following procedure outlines upgrading a 1.0.15 ColumnStore install to 1.0.16:

* [1.0.15 GA to 1.0.16 upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md)\
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

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md)

## Packaging

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.0.16 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8.6, Debian 9.1, RedHat 6, RedHat 7, SUSE 12, and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/downloads/columnstore)
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.0.16". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.0.16)
* MariaDB Server - [Source code based on MariaDB Server 10.1.38 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.0.16)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
