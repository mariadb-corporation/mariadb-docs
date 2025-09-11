# MariaDB ColumnStore 1.2.2 GA Release Notes

**Release date:** 3rd December 2018

[MariaDB ColumnStore 1.2.2](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a GA release of MariaDB ColumnStore. The MariaDB ColumnStore 1.2 series provides several new features and improvements over the MariaDB ColumnStore 1.1 release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-1952](https://jira.mariadb.org/browse/MCOL-1952) - The base MariaDB server version is now [10.3.11](../../../community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10311-release-notes.md) which include several maintenance and security fixes.
* [MCOL-1847](https://jira.mariadb.org/browse/MCOL-1847) - NumBlocksPct and TotalUmMemory can take fixed memory sizes instead of percentages
* [MCOL-1739](https://jira.mariadb.org/browse/MCOL-1739) - mcsapi has been split into separate packages for every programming language
* [MCOL-1890](https://jira.mariadb.org/browse/MCOL-1890) - The kafka package has been renamed

## Bugs and issues fixed

* [MCOL-1519](https://jira.mariadb.org/browse/MCOL-1519) - Query doesn't process certain JOIN types with GROUP BY handler.
* [MCOL-1558](https://jira.mariadb.org/browse/MCOL-1558) - BRM\_saves\_current should use a relative path
* [MCOL-1638](https://jira.mariadb.org/browse/MCOL-1638) - Suse12 regression failure test023 median::nextValue crashing PrimProc
* [MCOL-1716](https://jira.mariadb.org/browse/MCOL-1716) - GROUP BY handler incorrectly process filters with subquery as IN predicate
* [MCOL-1718](https://jira.mariadb.org/browse/MCOL-1718) - Clarify configuration requirements for usage of the -z option
* [MCOL-1742](https://jira.mariadb.org/browse/MCOL-1742) - CentOS 7 - data-adapter repository installation broken
* [MCOL-1777](https://jira.mariadb.org/browse/MCOL-1777) - regr tests depend on table that doesn't exist yet
* [MCOL-1778](https://jira.mariadb.org/browse/MCOL-1778) - WF regression tests need fixing
* [MCOL-1779](https://jira.mariadb.org/browse/MCOL-1779) - tablemode test failing in develop
* [MCOL-1793](https://jira.mariadb.org/browse/MCOL-1793) - regr\_slope() and regr\_r2() produce incorrect result when used as window functions
* [MCOL-1800](https://jira.mariadb.org/browse/MCOL-1800) - test022 regression
* [MCOL-1847](https://jira.mariadb.org/browse/MCOL-1847) - need to be able to specify NumBlocksPct and TotalUmMemory explicitly
* [MCOL-1855](https://jira.mariadb.org/browse/MCOL-1855) - ColumnStore table whose name contains $ cannot be renamed
* [MCOL-1868](https://jira.mariadb.org/browse/MCOL-1868) - func\_concat\_ws type
* [MCOL-1875](https://jira.mariadb.org/browse/MCOL-1875) - getsystemcpu & related commands always return 0 cpu usage
* [MCOL-1877](https://jira.mariadb.org/browse/MCOL-1877) - getactivesqlstatements returns 'file open error'
* [MCOL-1879](https://jira.mariadb.org/browse/MCOL-1879) - csv text "true" is mapped to 0 during import but should be parsed to 1
* [MCOL-1885](https://jira.mariadb.org/browse/MCOL-1885) - Cross engine / Query stats doesn't show specific query errors
* [MCOL-1900](https://jira.mariadb.org/browse/MCOL-1900) - PDI Plugin unresponsive if CS is not available
* [MCOL-1945](https://jira.mariadb.org/browse/MCOL-1945) - mxs\_adapter throws malloc error
* [MCOL-1947](https://jira.mariadb.org/browse/MCOL-1947) - Our aliases break BASH
* [MCOL-1949](https://jira.mariadb.org/browse/MCOL-1949) - vTpch10.sql and vTpch21.sql regression
* [MCOL-1953](https://jira.mariadb.org/browse/MCOL-1953) - columnstoreClusterTester.sh script fails
* [MCOL-1959](https://jira.mariadb.org/browse/MCOL-1959) - mxs\_adapter assertion crash on multi table stream
* [MCOL-1094](https://jira.mariadb.org/browse/MCOL-1094) - mcsapi should have view/clear table lock features
* [MCOL-1362](https://jira.mariadb.org/browse/MCOL-1362) - Add a export function that utilizes (sequential) write from Spark workers
* [MCOL-1739](https://jira.mariadb.org/browse/MCOL-1739) - Split mcsapi installation into different packages for C++, Java and Python
* [MCOL-1740](https://jira.mariadb.org/browse/MCOL-1740) - mcsimport - depend on mcsapi only
* [MCOL-1844](https://jira.mariadb.org/browse/MCOL-1844) - Allow prior/custom changes made to myCnf-include-args.text be added to new myCnf-include-args.text after upgrading
* [MCOL-1790](https://jira.mariadb.org/browse/MCOL-1790) - Implement new CASE item type detection
* [MCOL-1866](https://jira.mariadb.org/browse/MCOL-1866) - Change logo in mcsapi, PDI and mcsimport
* [MCOL-1944](https://jira.mariadb.org/browse/MCOL-1944) - /var/log/mariadb/columnstore ownership set to 777 recursive
* [MCOL-1952](https://jira.mariadb.org/browse/MCOL-1952) - Rebase develop 10.3.11

In addition, all bugs fixed in MariaDB ColumnStore 1.2.1 and earlier are implicitly included in this release.

## Upgrade

The following procedure outlines upgrading a 1.1.6 ColumnStore install to 1.2.2:

* [1.1.6 GA to 1.2.2 GA upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md)

Multi version upgrades generally will work using the same procedure however we can't test every possible permutation so you should test your specific scenario outside of production first if you wish to try this (and this is good practice regardless).

## Known issues and limitations

There are a number bugs and known limitations within this version of MariaDB ColumnStore, the most serious of these are listed below.

* [MCOL-1662](https://jira.mariadb.org/browse/MCOL-1662) - INSERT...SELECT and LOAD DATA INFILE when used in a transaction as well as mcsapi can cause dictionary columns to be badly cached
* [MCOL-1797](https://jira.mariadb.org/browse/MCOL-1797) - resumeDatabaseWrites can cause DML/DDL to go active all on UMs simultaneously
* [MCOL-1990](https://jira.mariadb.org/browse/MCOL-1990) - localquery mode tries to turn on replication and fails.
* [MCOL-2061](https://jira.mariadb.org/browse/MCOL-2061) - Running TRUNCATE on a table that has been upgraded from 1.1 -> 1.2 can cause MariaDB server to crash. As a workaround you can DROP and recreate the table.

## Documentation

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md)

## Packaging

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.2.2 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8, Debian 9, RedHat 6, RedHat 7, SUSE 12, Ubuntu 16.04 and Ubuntu 18.04.
* Packages can be downloaded [here](https://mariadb.com/downloads/mariadb-ax) or can be installed from the [repositories](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md).
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.2.2". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.2.2)
* MariaDB Server - [Source code based on MariaDB Server 10.3.11 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.2.2)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools/tree/columnstore-1.2.2)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api/tree/columnstore-1.2.2)
* MaxScale CDC and Kafka Data Adapters - [Source Code for data adapters](https://github.com/mariadb-corporation/mariadb-columnstore-data-adapters/tree/columnstore-1.2.2)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
