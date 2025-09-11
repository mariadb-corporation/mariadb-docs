# MariaDB ColumnStore 1.2.4 GA Release Notes (Release removed)

**Release date:** 29th May 2019

This version has been removed from production due to [MCOL-3395](https://jira.mariadb.org/browse/MCOL-3395) having the potential to corrupt databases.

[MariaDB ColumnStore 1.2.4](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) is a GA release of MariaDB ColumnStore. The MariaDB ColumnStore 1.2 series provides several new features and improvements over the MariaDB ColumnStore 1.1 release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-3315](https://jira.mariadb.org/browse/MCOL-3315) - The base MariaDB server version is now [10.3.15](../../../community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10315-release-notes.md) which include several maintenance and security fixes.
* [MCOL-3270](https://jira.mariadb.org/browse/MCOL-3270) - cpimport performance for dictionary data is up to 2x faster.
* [MCOL-2061](https://jira.mariadb.org/browse/MCOL-2061) - If you are performing a major version upgrade or have in the past there is a new stored procedure called columnstore\_info.columnstore\_upgrade() should be executed.

## Bugs and issues fixed

* [MCOL-537](https://jira.mariadb.org/browse/MCOL-537) - Some compiler warnings need fixing
* [MCOL-1495](https://jira.mariadb.org/browse/MCOL-1495) - Memory leak in WriteEngineServ
* [MCOL-1951](https://jira.mariadb.org/browse/MCOL-1951) - Crash when MySQL aggregate UDF is called against Columnstore table
* [MCOL-1984](https://jira.mariadb.org/browse/MCOL-1984) - SystemConfig / WaitPeriod change lost during upgrade
* [MCOL-2001](https://jira.mariadb.org/browse/MCOL-2001) - mscadmin redistributeData parameters are not accepted as suggested by the help information.
* [MCOL-2035](https://jira.mariadb.org/browse/MCOL-2035) - Some regr\_\* tests aren't deterministic so comparisons are iffy. RANK()
* [MCOL-2061](https://jira.mariadb.org/browse/MCOL-2061) - MariaDB shows warnings and could crash on DDL after upgrade
* [MCOL-2089](https://jira.mariadb.org/browse/MCOL-2089) - High CPU usage and slow performance appears when load data with remote mcsimport
* [MCOL-2091](https://jira.mariadb.org/browse/MCOL-2091) - UDAF doesn't work if there are two count(distinct) in projection list
* [MCOL-2244](https://jira.mariadb.org/browse/MCOL-2244) - There is no way to identify execution thread that causes bottleneck
* [MCOL-2267](https://jira.mariadb.org/browse/MCOL-2267) - Query with SUM() erroring - /rowgroup.h@677: assertion '0' failed
* [MCOL-2273](https://jira.mariadb.org/browse/MCOL-2273) - getSystemDisk showing incorrect root usage and reporting incorrect alarm
* [MCOL-3249](https://jira.mariadb.org/browse/MCOL-3249) - Probably Kafka DA produces '\0' in the end of TEXT or VARCHAR with width > 7
* [MCOL-3268](https://jira.mariadb.org/browse/MCOL-3268) - javamcsapi compatibility test fails
* [MCOL-3293](https://jira.mariadb.org/browse/MCOL-3293) - UPDATE performance improvement contribution - Contributed by ABS Global
* [MCOL-3296](https://jira.mariadb.org/browse/MCOL-3296) - ctrl+c sometimes leaves DMLProc in bad state
* [MCOL-3307](https://jira.mariadb.org/browse/MCOL-3307) - Non-Columnstore Window function causes debug assert
* [MCOL-3311](https://jira.mariadb.org/browse/MCOL-3311) - regression test212 logs integer expression expected error
* [MCOL-3318](https://jira.mariadb.org/browse/MCOL-3318) - RPM warnings appear when installing ColumnStore's MariaDB Server
* [MCOL-593](https://jira.mariadb.org/browse/MCOL-593) - support columnstore tables as slaves to innodb master tables
* [MCOL-1254](https://jira.mariadb.org/browse/MCOL-1254) - Add hidden switch for MariaDB async replication
* [MCOL-2013](https://jira.mariadb.org/browse/MCOL-2013) - API .NET support - Alpha - Contributed by Bill Adams
* [MCOL-2076](https://jira.mariadb.org/browse/MCOL-2076) - Allow simple replication to ColumnStore
* [MCOL-2129](https://jira.mariadb.org/browse/MCOL-2129) - Add a new postConfigure flag to resolve submitted hostnames to correct reverse dns names
* [MCOL-3267](https://jira.mariadb.org/browse/MCOL-3267) - Support ORDER BY within UNION subqueries
* [MCOL-3270](https://jira.mariadb.org/browse/MCOL-3270) - Improve cpimport ingest speed into Dictionary columns - Contributed by ABS Global
* [MCOL-2068](https://jira.mariadb.org/browse/MCOL-2068) - add support for using and defaulting memory based settings to docker image
* [MCOL-3315](https://jira.mariadb.org/browse/MCOL-3315) - Rebase on [MariaDB 10.3.15](../../../community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10315-release-notes.md)

Additional typo fix contribution by Kabike

In addition, all bugs fixed in MariaDB ColumnStore 1.2.3 and earlier are implicitly included in this release.

## Upgrade

The following procedure outlines upgrading a 1.1.7 ColumnStore install to 1.2.4:

* [1.1.7 GA to 1.2.4 GA upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md)

The following procedure outlines upgrading a 1.2.x ColumnStore install to 1.2.4:

* [1.2.x GA to 1.2.4 GA upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md)

Multi version upgrades generally will work using the same procedure however we can't test every possible permutation so you should test your specific scenario outside of production first if you wish to try this (and this is good practice regardless).

## Known issues and limitations

There are a number bugs and known limitations within this version of MariaDB ColumnStore, the most serious of these are listed below.

* [MCOL-1990](https://jira.mariadb.org/browse/MCOL-1990) - localquery mode tries to turn on replication and fails.

## Documentation

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md)

## Packaging

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.2.4 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8, Debian 9, RedHat 6, RedHat 7, SUSE 12, Ubuntu 16.04 and Ubuntu 18.04.
* Packages can be downloaded [here](https://mariadb.com/downloads/mariadb-ax) or can be installed from the [repositories](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md).
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.2.4". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-2/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.2.4)
* MariaDB Server - [Source code based on MariaDB Server 10.3.15 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.2.4)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools/tree/columnstore-1.2.4)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api/tree/columnstore-1.2.4)
* MaxScale CDC and Kafka Data Adapters - [Source Code for data adapters](https://github.com/mariadb-corporation/mariadb-columnstore-data-adapters/tree/columnstore-1.2.4)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
