# MariaDB 11.5 Changes & Improvements

[MariaDB 11.5](what-is-mariadb-115.md) is an old [rolling release](../../about/release-model.md) and is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

{% include "../../../.gitbook/includes/latest-11-5.md" %}

## Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 10.11 to MariaDB 11.0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-11-to-mariadb-11-0).

## New Features

### Temporary files and tables

* [Limit size of created disk temporary files and tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/limiting-size-of-created-disk-temporary-files-and-tables/limiting-size-of-created-disk-temporary-files-and-tables-overview) ([MDEV-9101](https://jira.mariadb.org/browse/MDEV-9101))
* There are two system variables used for controlling this feature:
  * [max\_tmp\_session\_space\_usage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_session_space_usage-system-variable): Limits the temporary space allowance per user
  * [max\_tmp\_total\_space\_usage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_total_space_usage-system-variable): Limits the temporary space allowance for all users.

### Data Types

* The [TIMESTAMP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/timestamp) range of values was extended. The maximal allowed value for timestamps was '2038-01-19 03:14:07 UTC', and is now '2106-02-07 06:28:15 UTC'. This does not change the storage format, and new tables can be read by old MariaDB servers as long as timestamp values are within the old timestamp range. At the moment this is only supported on 64-bit platforms ([MDEV-32188](https://jira.mariadb.org/browse/MDEV-32188)).

### Optimizer

* [Index condition pushdown](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/index-condition-pushdown) is now supported for partitioned tables ([MDEV-12404](https://jira.mariadb.org/browse/MDEV-12404))
* ANALYZE for statement should show selectivity of pushed index condition ([MDEV-18478](https://jira.mariadb.org/browse/MDEV-18478))

### Protocol

* Permit bulk implementation to return ALL individual results ([MDEV-30366](https://jira.mariadb.org/browse/MDEV-30366))
* Send initial values of system variables in first OK packet ([MDEV-31609](https://jira.mariadb.org/browse/MDEV-31609))

### Observability

* New [USERS table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-users-table) in the Information Schema for storing information about users, [password expiry](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/user-account-management/user-password-expiry), and the limits set by [max\_password\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_password_errors) ([MDEV-23729](https://jira.mariadb.org/browse/MDEV-23729), [MDEV-32218](https://jira.mariadb.org/browse/MDEV-32218))
* Add more columns to Information Schema [TABLE\_STATISTICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-table_statistics-table), [CLIENT\_STATISTICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-client_statistics-table) and [USER STATISTICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-user_statistics-table) tables ([MDEV-33151](https://jira.mariadb.org/browse/MDEV-33151))
* Add QUERIES column to Information Schema [INDEX\_STATISTICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table) table ([MDEV-33152](https://jira.mariadb.org/browse/MDEV-33152))
* Add [FLUSH GLOBAL STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush#flush-status) ([MDEV-33145](https://jira.mariadb.org/browse/MDEV-33145))
* Provide [InnoDB async IO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-asynchronous-io) statistics ([MDEV-32841](https://jira.mariadb.org/browse/MDEV-32841))
  * Including a number of [status variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/status-variables-added-in-mariadb-11-5).
* Extend [Query Response Time plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/query-response-time-plugin) to be compatible with Percona server ([MDEV-33501](https://jira.mariadb.org/browse/MDEV-33501))

### [Sequences](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences)

* Additional features for Sequences ([MDEV-28152](https://jira.mariadb.org/browse/MDEV-28152))
  * [CREATE SEQUENCE ... AS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/create-sequence) permits creating as any [INT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/int) type (including [BIGINT UNSIGNED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/bigint)), extending the range
  * [Information Schema Sequences table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-sequences-table)
  * Parser accepts larger and smaller values for [MINVALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/create-sequence#minvalue) and [MAXVALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/create-sequence#maxvalue)
* [ANALYZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/analyze-table) on [sequences](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences) no longer attempts to collect statistics ([MDEV-33938](https://jira.mariadb.org/browse/MDEV-33938))

### Other

* [REPAIR TABLE ... FORCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/repair-table) ([MDEV-33449](https://jira.mariadb.org/browse/MDEV-33449))
* Deprecate and ignore the [alter\_algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#alter_algorithm) system variable ([MDEV-33655](https://jira.mariadb.org/browse/MDEV-33655))
* Change [default Unicode collation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations) to uca1400\_ai\_ci, a modern Unicode collation with proper support for SMP characters (including emoji)([MDEV-25829](https://jira.mariadb.org/browse/MDEV-25829))
* Parallel dump of multiple databases via [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) with the `--dir` option ([MDEV-33625](https://jira.mariadb.org/browse/MDEV-33625))
* Deprecate [spider\_casual\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables#spider_casual_read) ([MDEV-31789](https://jira.mariadb.org/browse/MDEV-31789))

### Removed Features

The following deprecated features have been removed:

* ... COMPRESSED...
  * the correct syntax is COMPRESSED... ...
* [wsrep\_load\_data\_splitting](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_load_data_splitting)
* [integer latches in OQGraph](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/oqgraph-storage-engine/oqgraph-overview) (and the related [oqgraph\_allow\_create\_integer\_latch](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/oqgraph-system-and-status-variables#oqgraph_allow_create_integer_latch) variable).

### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 11.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-11-5) and [Status Variables Added in MariaDB 11.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/status-variables-added-in-mariadb-11-5).

## Security Vulnerabilities Fixed in [MariaDB 11.5](what-is-mariadb-115.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.\
Add listcve macro here - removed for performance reasons

## List of All [MariaDB 11.5](what-is-mariadb-115.md) Releases

| Date        | Release                                           | Status      | Release Notes                                    | Changelog                                                      |
| ----------- | ------------------------------------------------- | ----------- | ------------------------------------------------ | -------------------------------------------------------------- |
| 14 Aug 2024 | [MariaDB 11.5.2](mariadb-11-5-2-release-notes.md) | Stable (GA) | [Release Notes](mariadb-11-5-2-release-notes.md) | [Changelog](../../changelogs/11.5/mariadb-11-5-2-changelog.md) |
| 30 May 2024 | [MariaDB 11.5.1](mariadb-11-5-1-release-notes.md) | RC          | [Release Notes](mariadb-11-5-1-release-notes.md) | [Changelog](../../changelogs/11.5/mariadb-11-5-1-changelog.md) |
| 18 Mar 2024 | [MariaDB 11.5.0](mariadb-11-5-0-release-notes.md) | Alpha       | [Release Notes](mariadb-11-5-0-release-notes.md) |                                                                |

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
