# MariaDB ColumnStore 1.1.2 GA Release Notes

**Release date:** 21st November 2017

[MariaDB ColumnStore 1.1.2](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a GA release of MariaDB ColumnStore. This is the third release of the MariaDB ColumnStore 1.1 series. The MariaDB ColumnStore 1.1 series provides several new features and improvements over the MariaDB ColumnStore 1.0 release.

MariaDB ColumnStore 1.1.2 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [Beta](../../../community-server/about/release-criteria.md) release of the Streaming Data Adapters: Out of box adapters for data integration between various data sources for specific use cases
  * [MaxScale CDC Data Adapter](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/clients-and-tools/data-ingestion/columnstore-streaming-data-adapters) is integration of the MaxScale CDC streams into MariaDB ColumnStore
  * [Kafka Data Adapter](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/clients-and-tools/data-ingestion/columnstore-streaming-data-adapters) is integration of the Kafka streams into MariaDB ColumnStore.

## Bugs and issues fixed

* [MCOL-963](https://jira.mariadb.org/browse/MCOL-963) - self join cte queries from tpcds alternately fail with parsing error and succeed but with incorrect results
* [MCOL-976](https://jira.mariadb.org/browse/MCOL-976) - System in DBRM\_READ\_ONLY mode after Non-parent PM recovery under DataRedundancy
* [MCOL-989](https://jira.mariadb.org/browse/MCOL-989) - The addmodule command reported an invalid password error if cluster on the new module is not running
* [MCOL-997](https://jira.mariadb.org/browse/MCOL-997) - postConfigure on a DataRed setup should exiting when system install prompt is answered 'n'
* [MCOL-998](https://jira.mariadb.org/browse/MCOL-998) - MySQL replication is not replicating after installation
* [MCOL-1008](https://jira.mariadb.org/browse/MCOL-1008) - LDI and INSERT...SELECT causes mysqld to crash with long VARCHAR entries
* [MCOL-1009](https://jira.mariadb.org/browse/MCOL-1009) - MCS Replication setup failure - mysqld failed to restart
* [MCOL-1010](https://jira.mariadb.org/browse/MCOL-1010) - Debian 9 package: postConfigure failed to create /etc/rc.d/rc.local file
* [MCOL-1014](https://jira.mariadb.org/browse/MCOL-1014) - Replication setup failed when using ssh key and schema sync enabled
* [MCOL-1016](https://jira.mariadb.org/browse/MCOL-1016) - information\_schema.columnstore\_extents data\_size calculation incorrect
* [MCOL-1020](https://jira.mariadb.org/browse/MCOL-1020) - On ovh data center servers, postConfigure crashed on upgrade
* [MCOL-1021](https://jira.mariadb.org/browse/MCOL-1021) - Dictionary deduplication cache is not working correctly
* [MCOL-1024](https://jira.mariadb.org/browse/MCOL-1024) - postConfigure reported system catalog creation error but database continue to work

In addition, all bugs fixed in MariaDB ColumnStore 1.0.11 and earlier are implicitly included in this release.

## Upgrade

The following procedure outlines upgrading a 1.1.1 ColumnStore install to 1.1.2:

* [1.1.1 RC to 1.1.2 GA upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md)

Multi version upgrades generally will work using the same procedure however we can't test every possible permutation so you should test your specific scenario outside of production first if you wish to try this (and this is good practice regardless).

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
* [MCOL-912](https://jira.mariadb.org/browse/MCOL-912) : After adding two PMs with gluster, cpimport failed on newly added PMs. The system must be restarted after adding PM modules with data redundancy / gluster storage.
* [MCOL-1083](https://jira.mariadb.org/browse/MCOL-1083) : Crash when using blob column in 2 subqueries.
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

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.1.2 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8, Debian 9, RedHat 6, RedHat 7, SUSE 12, and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/downloads/mariadb-ax)
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.1.2". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-1/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/columnstore-1.1.2)
* MariaDB Server - [Source code based on MariaDB Server 10.2.10 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server/tree/columnstore-1.1.2)
* Tools - [Source code for MariaDB ColumnStore Tools](https://github.com/mariadb-corporation/mariadb-columnstore-tools/tree/columnstore-1.1.2)
* Write Data API - [Source code for Write Data API /SDK](https://github.com/mariadb-corporation/mariadb-columnstore-api/tree/columnstore-1.1.2)
* MaxScale CDC and Kafka Data Adapters - [Source Code for data adapters](https://github.com/mariadb-corporation/mariadb-columnstore-data-adapters/tree/columnstore-1.1.2)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
