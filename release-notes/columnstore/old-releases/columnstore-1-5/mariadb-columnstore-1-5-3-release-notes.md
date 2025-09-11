# MariaDB ColumnStore 1.5.3 Release Notes

## Overview

MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server. This is the first release in the Enterprise ColumnStore 1.5 series, and marks the first major release since integration with MariaDB Enterprise Server.

This release is focused on architectural change, product quality, and improved alignment to MariaDB Enterprise Server.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.5.4-2.

This release is of Gamma maturity, and should not be used with production workloads.

MariaDB Enterprise ColumnStore 1.5.3 was released on 2020-07-16.

* [Documentation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines)

## Notable Changes

* Comprehensive rewrite of installation, administration, cluster management, and failover logic. ([MCOL-3836](https://jira.mariadb.org/browse/MCOL-3836))
* Simplified installation
  * Users no longer need to execute columnstore-post-install and postConfigure
  * It is a plugin for MariaDB Enterprise Server.
  * It is packaged similar to other MariaDB Enterprise Server plugins.
  * See Installation for more details.
* Simplified administration:
  * mcsadmin has been removed. Instead, Enterprise ColumnStore 1.5 uses systemd for administration of single-node and multi-node deployments, and it also adds a new REST API for administration of multi-node deployments.
  * The new systemd service called mariadb-columnstore is used to manage ColumnStore's processes.
  * The new REST API is used to manage multi-node ColumnStore deployments.
  * The new REST API provides an interface for MariaDB MaxScale 2.5 to orchestrate the multi-node Enterprise ColumnStore deployment.
  * See OAM Replacement for more details.
* This release was the source for fixes previously backported to ColumnStore 1.4.4.
* This release includes correction of regressions present in ColumnStore 1.4.4 vs pre-integration.
* Fixes for defects in tiered storage and S3-compatible object storage.
* Support for standard MariaDB Enterprise Server collation and character sets. ([MCOL-337](https://jira.mariadb.org/browse/MCOL-337))
* Improved performance for REGR\_\* functions. ([MCOL-3837](https://jira.mariadb.org/browse/MCOL-3837))

## Issues Fixed

### Can result in a hang or crash

* mariadbd will abort if Columnstore.xml is missing. ([MCOL-3853](https://jira.mariadb.org/browse/MCOL-3853))
* Intermittent crash of cpimport in some complicated workflows. ([MCOL-3865](https://jira.mariadb.org/browse/MCOL-3865))
* Exceeding thread limits will cause queries against S3-compatible object storage to hang. ([MCOL-3858](https://jira.mariadb.org/browse/MCOL-3858))
* Error was not properly returned when a COMMIT or ROLLBACK failed, triggering an assertion. ([MCOL-4124](https://jira.mariadb.org/browse/MCOL-4124))

### Can result in unexpected behavior

* mcs-storagemanager attempted startup when not needed. ([MCOL-4151](https://jira.mariadb.org/browse/MCOL-4151))
* COUNT(DISTINCT) on more than one column produces an error. ([MCOL-3857](https://jira.mariadb.org/browse/MCOL-3857))
* REVERSE() function does not work with non-Latin characters. ([MCOL-2221](https://jira.mariadb.org/browse/MCOL-2221))
* Multi-table DROP IF EXISTS generates an error instead of a warning. ([MCOL-4164](https://jira.mariadb.org/browse/MCOL-4164))
* UPDATE with SELECT returning nulls may produce wrong answer. ([MCOL-4116](https://jira.mariadb.org/browse/MCOL-4116))
* rand() calls with the same seed value return different results. ([MCOL-3760](https://jira.mariadb.org/browse/MCOL-3760))
* Attempt to INSERT a TINYINT with an out-of-range value can generate a spurious error message. ([MCOL-3777](https://jira.mariadb.org/browse/MCOL-3777))
* A query containing a Common Table Expression (CTE) can return the wrong error message, that a field is not in the GROUP BY clause even if it is. ([MCOL-3782](https://jira.mariadb.org/browse/MCOL-3782))
* Complex queries using UNION can return the wrong error message, table not found. ([MCOL-3828](https://jira.mariadb.org/browse/MCOL-3828))
* COUNT(NULL) doesn't work as a window function. ([MCOL-3839](https://jira.mariadb.org/browse/MCOL-3839))
* The wrong error message is given when a function not supported by ColumnStore is used inside a function that is supported by ColumnStore. ([MCOL-3924](https://jira.mariadb.org/browse/MCOL-3924))
* microsecond support for from\_unixtime
* INSERT after a LOAD DATA LOCAL INFILE in a transaction may silently fail. ([MCOL-4002](https://jira.mariadb.org/browse/MCOL-4002))
* IN clause in WHERE could be evaluated improperly. ([MCOL-2096](https://jira.mariadb.org/browse/MCOL-2096))
* A spurious "file not found" error message can occur when query, truncate, and cpimport collided. ([MCOL-3521](https://jira.mariadb.org/browse/MCOL-3521))
* Internal error: IDB-2035 can occur with BIT\_OR function in projection and subquery in FROM ([MCOL-3356](https://jira.mariadb.org/browse/MCOL-3356))
* Multi-byte characters mishandled in DML export to cpimport-1.5. ([MCOL-4017](https://jira.mariadb.org/browse/MCOL-4017))
* GROUP\_CONCAT() with ORDER BY and long doubles may fail. ([MCOL-3904](https://jira.mariadb.org/browse/MCOL-3904))
* CONV() returned less characters in the resulting string. ([MCOL-3596](https://jira.mariadb.org/browse/MCOL-3596))
* MODA() produces memory leak. ([MCOL-4042](https://jira.mariadb.org/browse/MCOL-4042))
* Memory leaks. ([MCOL-4043](https://jira.mariadb.org/browse/MCOL-4043), [MCOL-3934](https://jira.mariadb.org/browse/MCOL-3934))
* EXPLAIN generates error on every other (alternating) execution. ([MCOL-3860](https://jira.mariadb.org/browse/MCOL-3860))
* Renaming a table causes schema to become out of sync between MariaDB Server catalog and ColumnStore. ([MCOL-3859](https://jira.mariadb.org/browse/MCOL-3859))
* Incorrect COUNT(\*) with a complex view. ([MCOL-3813](https://jira.mariadb.org/browse/MCOL-3813))

### Related to install and upgrade

* storagemanager.cnf variable $HOME drew path from user's environment. $HOME now points to the current location of ColumnStore data. ([MCOL-4014](https://jira.mariadb.org/browse/MCOL-4014))

## Known Issues

* Built-in SQL functions do not work in ColumnStore when sql\_mode=ORACLE ([MCOL-4044](https://jira.mariadb.org/browse/MCOL-4044))

## Interface Changes

None.

## Platforms

In alignment to the MariaDB Corporation Engineering Policy, MariaDB Enterprise ColumnStore 1.5.3 is provided for:

* Red Hat Enterprise Linux 8
* Red Hat Enterprise Linux 7
* CentOS 8
* CentOS 7
* Ubuntu 20.04
* Ubuntu 18.04
* Ubuntu 16.04
* Debian 10
* Debian 9
* SUSE Linux Enterprise Server 15
* SUSE Linux Enterprise Server 12

| Note | MariaDB Enterprise ColumnStore 1.5 has been superseded by MariaDB Enterprise ColumnStore 5 in MariaDB Enterprise Server 10.5. |
| ---- | ----------------------------------------------------------------------------------------------------------------------------- |

## Installation Instructions

* ​[ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore 5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* ​[ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)​[10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)​
* ​[HTAP Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)​[10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and MariaDB Enterprise ColumnStore ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)​
* ​[Single-Node Enterprise ColumnStore ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)​[10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)​
* ​[Single-Node Enterprise ColumnStore ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)[5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[ with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)​[10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)

## Upgrade Instructions

* [Major Release Upgrades for MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/columnstore-release-notes/README.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
