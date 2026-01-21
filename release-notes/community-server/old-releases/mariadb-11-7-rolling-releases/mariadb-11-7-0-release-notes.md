# MariaDB 11.7.0 Release Notes

{% include "../../../.gitbook/includes/latest-11-7.md" %}

<a href="https://downloads.mariadb.org/mariadb/11.7.0/" class="button primary">Download</a> <a href="mariadb-11-7-0-release-notes.md" class="button secondary">Release Notes</a> <a href="what-is-mariadb-117.md" class="button secondary">Overview of 11.7</a>

**Release date:** 25 Sep 2024

{% include "../../../.gitbook/includes/non-stable.md" %}

[MariaDB 11.7](what-is-mariadb-117.md) is a [rolling release](../../about/release-model.md). It is an evolution of [MariaDB 11.6](../release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116.md) with several entirely new features.

[MariaDB 11.7.0](mariadb-11-7-0-release-notes.md) is a single preview release. Features are to be considered preview, and none are guaranteed to make it into [MariaDB 11.7](what-is-mariadb-117.md).

The preview is available as a container **quay.io/mariadb-foundation/mariadb-devel:11.7-preview**.

Thanks, and enjoy MariaDB!

## Notable Items

### Replication and Binary Log

* When [binlogging](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) is enabled, committing a large transaction no longer freezes all other transactions until completed ([MDEV-32014](https://jira.mariadb.org/browse/MDEV-32014))
* [binlog\_optimize\_thread\_scheduling](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_optimize_thread_scheduling) has been deprecated ([MDEV-33756](https://jira.mariadb.org/browse/MDEV-33756))
* Async rollback prepared transactions during binlog crash recovery ([MDEV-33853](https://jira.mariadb.org/browse/MDEV-33853))
* New variable, [slave\_abort\_blocking\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#slave_abort_blocking_timeout), for aborting long-running queries on a replica ([MDEV-34857](https://jira.mariadb.org/browse/MDEV-34857))
* New variable, [binlog\_large\_commit\_threshold](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_large_commit_threshold), for increasing transaction concurrency for large transactions ([MDEV-32014](https://jira.mariadb.org/browse/MDEV-32014))

### UUID

* New function for generating version 4 UUIDs [UUIDv4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/uuid_v4) ([MDEV-11339](https://jira.mariadb.org/browse/MDEV-11339))
* New function for generating version 7 UUIDs [UUIDv7](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/uuid_v7) ([MDEV-32637](https://jira.mariadb.org/browse/MDEV-32637))

### Optimization

* Optimization improvement for single-table UPDATE/DELETE: make cost-based choice between subquery strategies ([MDEV-25008](https://jira.mariadb.org/browse/MDEV-25008))
* The [Charset Narrowing Optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/charset-narrowing-optimization) is now on by default ([MDEV-34380](https://jira.mariadb.org/browse/MDEV-34380))

### GIS

New GIS functions. These functions improve compatibility with MySQL 8. **Note that these were not included in** [**MariaDB 11.7**](what-is-mariadb-117.md)

* [ST\_Validate](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_validate) ([MDEV-34137](https://jira.mariadb.org/browse/MDEV-34137))
* [MBRCoveredBy](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/mbr-minimum-bounding-rectangle/mbrcoveredby) ([MDEV-34138](https://jira.mariadb.org/browse/MDEV-34138))
* [ST\_Simplify](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_simplify) ([MDEV-34141](https://jira.mariadb.org/browse/MDEV-34141))
* [ST\_GeoHash](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_geohash) ([MDEV-34158](https://jira.mariadb.org/browse/MDEV-34158))
* [ST\_LatFromGeoHash](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_latfromgeohash) ([MDEV-34159](https://jira.mariadb.org/browse/MDEV-34159))
* [ST\_LongFromGeoHash](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_longfromgeohash) ([MDEV-34160](https://jira.mariadb.org/browse/MDEV-34160))
* [ST\_IsValid](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_isvalid) ([MDEV-34276](https://jira.mariadb.org/browse/MDEV-34276))
* [ST\_Collect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_collect) ([MDEV-34278](https://jira.mariadb.org/browse/MDEV-34278))

### System-Versioned Tables

* Allow a [system-versioned table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) to be converted from implicit to explicit row\_start/row\_end columns ([MDEV-27293](https://jira.mariadb.org/browse/MDEV-27293))

### Slow Query Log

* New variable, [log\_slow\_always\_query\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/slow-query-log/log_slow_always_query_time-system-variable), for specifying that all queries longer than this time are logged to the [slow query log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/slow-query-log), regardless of [log\_slow\_min\_examined\_row\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_slow_min_examined_row_limit) and [log\_slow\_rate\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_slow_rate_limit) ([MDEV-33144](https://jira.mariadb.org/browse/MDEV-33144))

### Stored Routines

* ROW data type for stored function return values ([MDEV-12252](https://jira.mariadb.org/browse/MDEV-12252))

### Derived Tables

* Add optional correlation column list for [derived tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/subqueries/subqueries-in-a-from-clause-derived-tables) ([MDEV-31466](https://jira.mariadb.org/browse/MDEV-31466))

### Vectors

* [MariaDB Vector Search](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/vectors) ([MDEV-34939](https://jira.mariadb.org/browse/MDEV-34939))

### \[SHOW] CREATE SERVER

* Implement [SHOW CREATE SERVER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-server) ([MDEV-15696](https://jira.mariadb.org/browse/MDEV-15696))
* Allow arbitrary options in [CREATE SERVER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-server) ([MDEV-34716](https://jira.mariadb.org/browse/MDEV-34716))

### General

* [SESSION\_USER()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/session_user), which used to be an alias for [USER()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/user) now shows the value of [CURRENT\_USER()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/current_user) when the session was created ([MDEV-30908](https://jira.mariadb.org/browse/MDEV-30908))
* CURRENT\_TIMESTAMP should return a TIMESTAMP (WITH TIME ZONE?) ([MDEV-15751](https://jira.mariadb.org/browse/MDEV-15751))
* A warning has been added when [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length) is exceeded. ([MDEV-27277](https://jira.mariadb.org/browse/MDEV-27277))

### Deprecated Variables

* [binlog\_optimize\_thread\_scheduling](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_optimize_thread_scheduling) ([MDEV-33756](https://jira.mariadb.org/browse/MDEV-33756))

#### Spider

* The Spider variables [spider\_table\_crd\_thread\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables#spider_table_crd_thread_count) and [spider\_table\_sts\_thread\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables#spider_table_sts_thread_count) have been deprecated ([MDEV-28009](https://jira.mariadb.org/browse/MDEV-28009))

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
