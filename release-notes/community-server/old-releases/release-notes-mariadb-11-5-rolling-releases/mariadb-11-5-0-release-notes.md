# MariaDB 11.5.0 Release Notes

{% include "../../../.gitbook/includes/latest-11-5.md" %}

<a href="https://downloads.mariadb.org/mariadb/11.5.0/" class="button primary">Download</a> <a href="mariadb-11-5-0-release-notes.md" class="button secondary">Release Notes</a> <a href="what-is-mariadb-115.md" class="button secondary">Overview of 11.5</a>

**Release date:** 18 March 2024

{% include "../../../.gitbook/includes/non-stable.md" %}

[MariaDB 11.5](what-is-mariadb-115.md) is an upcoming development series of MariaDB. It is an evolution of [MariaDB 11.4](../../11.4/what-is-mariadb-114.md) with several entirely new features.

[MariaDB 11.5.0](mariadb-11-5-0-release-notes.md) is a single preview release. Features are to be considered preview, and none are guaranteed to make it into [MariaDB 11.5](what-is-mariadb-115.md).

The preview is available as a container **quay.io/mariadb-foundation/mariadb-devel:11.5-preview**.

Thanks, and enjoy MariaDB!

## New Features

### Temporary files and tables

* [Limit size of created disk temporary files and tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/limiting-size-of-created-disk-temporary-files-and-tables/limiting-size-of-created-disk-temporary-files-and-tables-overview) ([MDEV-9101](https://jira.mariadb.org/browse/MDEV-9101))
* There are two system variables used for controlling this feature:
  * [max\_tmp\_space\_usage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_session_space_usage-system-variable): Limits the temporary space allowance per user
  * [max\_total\_tmp\_space\_usage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_total_space_usage-system-variable): Limits the temporary space allowance for all users.

### Data Types

* The [TIMESTAMP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/timestamp) range of values was extended. The maximal allowed value for timestamps was '2038-01-19 03:14:07 UTC', and is now '2106-02-07 06:28:15 UTC'. This does not change the storage format, and new tables can be read by old MariaDB servers as long as timestamp values are within the old timestamp range. At the moment this is only supported on 64-bit platforms ([MDEV-32188](https://jira.mariadb.org/browse/MDEV-32188)).

### Optimizer

* [Index condition pushdown](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/index-condition-pushdown) is now supported for partitioned tables ([MDEV-12404](https://jira.mariadb.org/browse/MDEV-12404))
* ANALYZE FORMAT=JSON now [shows selectivity of pushed index condition](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-interpreting-rows-and-filtered-members) ([MDEV-18478](https://jira.mariadb.org/browse/MDEV-18478))

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
* Show variable deprecation for [mariadbd --help](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#-help) output ([MDEV-28671](https://jira.mariadb.org/browse/MDEV-28671))
* Extend [Query Response Time plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/query-response-time-plugin) to be compatible with Percona server ([MDEV-33501](https://jira.mariadb.org/browse/MDEV-33501))
* New variable, [log\_slow\_always\_query\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/slow-query-log/log_slow_always_query_time-system-variable) for additional control over what is logged to the [slow query log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/slow-query-log). This setting did not make it into [MariaDB 11.5](what-is-mariadb-115.md), but was added in [MariaDB 11.7](../mariadb-11-7-rolling-releases/what-is-mariadb-117.md) ([MDEV-33144](https://jira.mariadb.org/browse/MDEV-33144))

### [Sequences](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences)

* Additional features for Sequences ([MDEV-28152](https://jira.mariadb.org/browse/MDEV-28152))
  * [CREATE SEQUENCE ... AS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/create-sequence) permits creating as any [INT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/int) type (including [BIGINT UNSIGNED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/bigint)), extending the range
  * [Information Schema Sequences table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-sequences-table)
  * Parser accepts larger and smaller values for [MINVALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/create-sequence#minvalue) and [MAXVALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/create-sequence#maxvalue)

### Other

* [REPAIR TABLE ... FORCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/repair-table) ([MDEV-33449](https://jira.mariadb.org/browse/MDEV-33449))
* Deprecate and ignore the [alter\_algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#alter_algorithm) system variable ([MDEV-33655](https://jira.mariadb.org/browse/MDEV-33655))
* Change [default Unicode collation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations) to uca1400\_ai\_ci, a modern Unicode collation with proper support for SMP characters (including emoji)([MDEV-25829](https://jira.mariadb.org/browse/MDEV-25829))
* Parallel dump of multiple databases via [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) with the `--dir` option ([MDEV-33625](https://jira.mariadb.org/browse/MDEV-33625))
* Deprecate [spider\_casual\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables#spider_casual_read) ([MDEV-31789](https://jira.mariadb.org/browse/MDEV-31789))

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
