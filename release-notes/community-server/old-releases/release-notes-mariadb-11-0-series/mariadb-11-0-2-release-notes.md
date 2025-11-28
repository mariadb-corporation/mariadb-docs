# MariaDB 11.0.2 Release Notes

The most recent release of [MariaDB 11.0](what-is-mariadb-110.md) is:[**MariaDB 11.0.6**](mariadb-11-0-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.0.6/)

[Download 11.0.2](https://downloads.mariadb.org/mariadb/11.0.2/) | [Release Notes](mariadb-11-0-2-release-notes.md) | [Changelog](../../changelogs/11.0/mariadb-11-0-2-changelog.md) | [Overview of 11.0](what-is-mariadb-110.md)

**Release date:** 6 Jun 2023

[MariaDB 11.0](what-is-mariadb-110.md) is a current short-term stable series of MariaDB and will be maintained until June 2024. It is an evolution of [MariaDB 10.11](../../10.11/what-is-mariadb-1011.md) with several entirely new features.

[MariaDB 11.0.2](mariadb-11-0-2-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 11.0**](what-is-mariadb-110.md) **see the**[**What is MariaDB 11.0?**](what-is-mariadb-110.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### Functions

* Given a time in picoseconds, the new function [FORMAT\_PICO\_TIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/format_pico_time) returns a human-readable time value and unit indicator ([MDEV-19629](https://jira.mariadb.org/browse/MDEV-19629))

### InnoDB

* InnoDB does not free UNDO after the fix of [MDEV-30671](https://jira.mariadb.org/browse/MDEV-30671) ([MDEV-31234](https://jira.mariadb.org/browse/MDEV-31234))
* InnoDB hang fixes ([MDEV-31158](https://jira.mariadb.org/browse/MDEV-31158), [MDEV-31343](https://jira.mariadb.org/browse/MDEV-31343), [MDEV-31350](https://jira.mariadb.org/browse/MDEV-31350))
* [Innodb\_buffer\_pool\_read\_requests](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#innodb_buffer_pool_read_requests) is not updated correctly ([MDEV-31309](https://jira.mariadb.org/browse/MDEV-31309))
* InnoDB monitor trx\_rseg\_history\_len was accidentally disabled by default ([MDEV-31308](https://jira.mariadb.org/browse/MDEV-31308))
* Revert "[MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster"

### Optimizer

* [Split Materialized](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizations-for-derived-tables/lateral-derived-optimization) optimization is improved to re-fill the materialized table only if necessary. The fewer number of table refills is taken into account when choosing query plan, too ([MDEV-26301](https://jira.mariadb.org/browse/MDEV-26301))
* New optimizer\_switch option, [hash\_join\_cardinality](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/hash_join_cardinality-optimizer_switch-flag), is added. It is ON by default. When set to ON, the optimizer will produce tighter bounds for hash join output cardinality. ([MDEV-30812](https://jira.mariadb.org/browse/MDEV-30812))
* Crash with condition pushable into derived and containing outer reference ([MDEV-31403](https://jira.mariadb.org/browse/MDEV-31403) [MDEV-31240](https://jira.mariadb.org/browse/MDEV-31240))
* Crash with [EXPLAIN EXTENDED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) for multi-table update of system table ([MDEV-31224](https://jira.mariadb.org/browse/MDEV-31224))
* [ANALYZE FORMAT=JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-format-json) now prints more information about [Block Nested Loop joins](https://mariadb.com/docs/general-resources/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms#block-nested-loop-join): `block-nl-join` element now has `r_loops`, `r_effective_rows` and `r_other_time_ms` fields ([MDEV-30806](https://jira.mariadb.org/browse/MDEV-30806), [MDEV-30830](https://jira.mariadb.org/browse/MDEV-30830), [MDEV-30972](https://jira.mariadb.org/browse/MDEV-30972)).

### Variables

* New status variable: [max\_used\_connections\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#max_used_connections_time) ([MDEV-30543](https://jira.mariadb.org/browse/MDEV-30543))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Changelog

For a complete list of changes made in [MariaDB 11.0.2](mariadb-11-0-2-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/11.0/mariadb-11-0-2-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 11.0.2](mariadb-11-0-2-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-11-1-1-11-0-2-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
