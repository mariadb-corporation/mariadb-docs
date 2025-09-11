# MariaDB ColumnStore 1.2.5 GA Release Notes

**Release date:** 23rd July 2019

[MariaDB ColumnStore 1.2.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a GA release of MariaDB ColumnStore. The MariaDB ColumnStore 1.2 series provides several new features and improvements over the MariaDB ColumnStore 1.1 release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-3398](https://jira.mariadb.org/browse/MCOL-3398) - The base MariaDB server version is now [10.3.16](../../../community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10316-release-notes.md) which include several maintenance and security fixes.
* [MCOL-3395](https://jira.mariadb.org/browse/MCOL-3395) - Critical regression in the dictionary storage of 1.2.4 fixed.

## Bugs and issues fixed

* [MCOL-1375](https://jira.mariadb.org/browse/MCOL-1375) - Assertion failure when using HAVING with constant values
* [MCOL-1985](https://jira.mariadb.org/browse/MCOL-1985) - Fix up regr functions in regrmysql.cpp so regr\_\* funtions work correcly for InnoDB tables
* [MCOL-2225](https://jira.mariadb.org/browse/MCOL-2225) - cross engine join with space in column names in on condition cause fatal error
* [MCOL-2230](https://jira.mariadb.org/browse/MCOL-2230) - DATE/TIME type math is broken -- TIMEDIFF, TIMESTAMPDIFF and date math
* [MCOL-3239](https://jira.mariadb.org/browse/MCOL-3239) - CS incorrectly pushes function filter predicate into a subquery.
* [MCOL-3304](https://jira.mariadb.org/browse/MCOL-3304) - Window functions in queries with embedded selects produce bad numbers
* [MCOL-3314](https://jira.mariadb.org/browse/MCOL-3314) - Exemgr crash on query happening when we increase 2 variables, MaxOutStandingRequests and RequestSize
* [MCOL-3353](https://jira.mariadb.org/browse/MCOL-3353) - Possible memory corruption in execplan
* [MCOL-3367](https://jira.mariadb.org/browse/MCOL-3367) - ColumnStore API rpm packages failed to install
* [MCOL-3373](https://jira.mariadb.org/browse/MCOL-3373) - Bug in funcexp while throwing an exception
* [MCOL-3384](https://jira.mariadb.org/browse/MCOL-3384) - Crash in mxs\_adapter
* [MCOL-3385](https://jira.mariadb.org/browse/MCOL-3385) - Strings returned by the Avro C API include the null terminator in thestring length
* [MCOL-3391](https://jira.mariadb.org/browse/MCOL-3391) - columnstore\_upgrade failed from 1.2.2 to 1.2.4 when database including multibyte table name
* [MCOL-3395](https://jira.mariadb.org/browse/MCOL-3395) - regression: dictionary de-duplication cache bleeding between columns
* [MCOL-3399](https://jira.mariadb.org/browse/MCOL-3399) - Regression in LDI string length handling
* [MCOL-3404](https://jira.mariadb.org/browse/MCOL-3404) - tpcds query #98 failed with an internal error
* [MCOL-3321](https://jira.mariadb.org/browse/MCOL-3321) - some regr\_\* function tests need order by to make them deterministic
* [MCOL-3343](https://jira.mariadb.org/browse/MCOL-3343) - Window Functions don't work with arithmetic operators or other functions
* [MCOL-1968](https://jira.mariadb.org/browse/MCOL-1968) - wrong string comparisation after dataimport and extents
* [MCOL-1989](https://jira.mariadb.org/browse/MCOL-1989) - Querying view results in internal error: column is not found in info map
* [MCOL-3398](https://jira.mariadb.org/browse/MCOL-3398) - Rebase 1.2 on [MariaDB 10.3.16](../../../community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10316-release-notes.md)

In addition, all bugs fixed in MariaDB ColumnStore 1.2.4 and earlier are implicitly included in this release.

## Upgrade

The following procedure outlines upgrading a 1.1.7 ColumnStore install to 1.2.5:

* [1.1.7 GA to 1.2.5 GA upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md)

The following procedure outlines upgrading a 1.2.x ColumnStore install to 1.2.5:

* [1.2.x GA to 1.2.5 GA upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md)

Multi version upgrades generally will work using the same procedure however we can't test every possible permutation so you should test your specific scenario outside of production first if you wish to try this (and this is good practice regardless).

## Known issues and limitations

There are a number bugs and known limitations within this version of MariaDB ColumnStore, the most serious of these are listed below.

* [MCOL-1990](https://jira.mariadb.org/browse/MCOL-1990) - localquery mode tries to turn on replication and fails.

## Documentation

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md)

## Packaging

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.2.5 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8, Debian 9, RedHat 6, RedHat 7, SUSE 12, Ubuntu 16.04 and Ubuntu 18.04.
* Packages can be downloaded [here](https://mariadb.com/downloads/mariadb-ax) or can be installed from the [repositories](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md).
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.2.5". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.2.5)
* MariaDB Server - [Source code based on MariaDB Server 10.3.16 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.2.5)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools/tree/columnstore-1.2.5)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api/tree/columnstore-1.2.5)
* MaxScale CDC and Kafka Data Adapters - [Source Code for data adapters](https://github.com/mariadb-corporation/mariadb-columnstore-data-adapters/tree/columnstore-1.2.5)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
