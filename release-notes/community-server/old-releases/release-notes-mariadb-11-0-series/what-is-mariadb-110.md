# MariaDB 11.0 Changes & Improvements

[MariaDB 11.0](what-is-mariadb-110.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

The most recent release of [MariaDB 11.0](what-is-mariadb-110.md) is:[**MariaDB 11.0.6**](mariadb-11-0-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.0.6/)

[MariaDB 11.0](what-is-mariadb-110.md) is a short-term release series, and was [maintained until](https://mariadb.org/about/#maintenance-policy) June 2024.

## Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 10.11 to MariaDB 11.0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-11-to-mariadb-11-0).

## New Features & Improvements

### Functions

* Given a time in picoseconds, the new function [FORMAT\_PICO\_TIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/format_pico_time) returns a human-readable time value and unit indicator ([MDEV-19629](https://jira.mariadb.org/browse/MDEV-19629))

### Optimizer

* Major improvements to the Optimizer. See [The Optimizer Cost Model from MariaDB 11.0](https://mariadb.com/docs/general-resources/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/the-optimizer-cost-model-from-mariadb-11-0).

### InnoDB

* The [InnoDB Change Buffer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-change-buffering) has been removed ([MDEV-29694](https://jira.mariadb.org/browse/MDEV-29694))

### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 11.0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-11-0) and [Status Variables Added in MariaDB 11.0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/status-variables-added-in-mariadb-11-0).
* The default value for [innodb\_undo\_tablespaces](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_tablespaces) has been changed from 0 to 3 ([MDEV-29986](https://jira.mariadb.org/browse/MDEV-29986))
* The following variables have been deprecated:
  * [innodb\_defragment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_defragment)
  * [innodb\_defragment\_n\_pages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_defragment_n_pages)
  * [innodb\_defragment\_stats\_accuracy](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_defragment_stats_accuracy)
  * [innodb\_defragment\_fill\_factor\_n\_recs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_defragment_fill_factor_n_recs)
  * [innodb\_defragment\_fill\_factor](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_defragment_fill_factor)
  * [innodb\_defragment\_frequency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_defragment_frequency)
  * [innodb\_file\_per\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_file_per_table)
  * [innodb\_flush\_method](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_flush_method)
* The following deprecated variables have been removed:
  * [innodb\_change\_buffer\_max\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_change_buffer_max_size)
  * [innodb\_change\_buffering](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_change_buffering)

## Security Vulnerabilities Fixed in [MariaDB 11.0](what-is-mariadb-110.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2024-21096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21096): [MariaDB 11.0.6](mariadb-11-0-6-release-notes.md)
* [CVE-2023-22084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22084): [MariaDB 11.0.4](mariadb-11-0-4-release-notes.md)

## List of All [MariaDB 11.0](what-is-mariadb-110.md) Releases

| Date        | Release                                           | Status                 | Release Notes                                    | Changelog                                                      |
| ----------- | ------------------------------------------------- | ---------------------- | ------------------------------------------------ | -------------------------------------------------------------- |
| 16 May 2024 | [MariaDB 11.0.6](mariadb-11-0-6-release-notes.md) | Stable (GA)            | [Release Notes](mariadb-11-0-6-release-notes.md) | [Changelog](../../changelogs/11.0/mariadb-11-0-6-changelog.md) |
| 7 Feb 2024  | [MariaDB 11.0.5](mariadb-11-0-5-release-notes.md) | Stable (GA)            | [Release Notes](mariadb-11-0-5-release-notes.md) | [Changelog](../../changelogs/11.0/mariadb-11-0-5-changelog.md) |
| 13 Nov 2023 | [MariaDB 11.0.4](mariadb-11-0-4-release-notes.md) | Stable (GA)            | [Release Notes](mariadb-11-0-4-release-notes.md) | [Changelog](../../changelogs/11.0/mariadb-11-0-4-changelog.md) |
| 14 Aug 2023 | [MariaDB 11.0.3](mariadb-11-0-3-release-notes.md) | Stable (GA)            | [Release Notes](mariadb-11-0-3-release-notes.md) | [Changelog](../../changelogs/11.0/mariadb-11-0-3-changelog.md) |
| 6 Jun 2023  | [MariaDB 11.0.2](mariadb-11-0-2-release-notes.md) | Stable (GA)            | [Release Notes](mariadb-11-0-2-release-notes.md) | [Changelog](../../changelogs/11.0/mariadb-11-0-2-changelog.md) |
| 22 Feb 2023 | [MariaDB 11.0.1](mariadb-11-0-1-release-notes.md) | RC (Release Candidate) | [Release Notes](mariadb-11-0-1-release-notes.md) | [Changelog](../../changelogs/11.0/mariadb-11-0-1-changelog.md) |
| 27 Dec 2022 | [MariaDB 11.0.0](mariadb-11-0-0-release-notes.md) | Alpha                  | [Release Notes](mariadb-11-0-0-release-notes.md) |                                                                |

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
