# MariaDB 11.1 Changes & Improvements

[MariaDB 11.1](what-is-mariadb-111.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

The most recent release of [MariaDB 11.1](what-is-mariadb-111.md) is:[**MariaDB 11.1.6**](mariadb-11-1-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.1.6/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.1.6/)

[MariaDB 11.1](what-is-mariadb-111.md) is a short-term release series, and was [maintained until](https://mariadb.org/about/#maintenance-policy) August 2024.

## Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 11.0 to MariaDB 11.1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-11-0-to-mariadb-11-1).

## New Features & Improvements

### JSON

* [JSON\_SCHEMA\_VALID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_schema_valid) function for validating a JSON schema ([MDEV-27128](https://jira.mariadb.org/browse/MDEV-27128))

### Optimizer

* [Semi-join optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/semi-join-subquery-optimizations) for single-table [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update)/[DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) statements. Update and delete statements that use subqueries can now use all subquery optimization strategies that MariaDB offers, so now if you use subqueries in UPDATE or DELETE, these statements will likely be much faster ([MDEV-7487](https://jira.mariadb.org/browse/MDEV-7487))
* Queries with the [DATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/date-function) or [YEAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/year) functions comparing against a constant can now make use of indexes, so these will be noticeably quicker in certain instances. For example `SELECT * FROM t2 WHERE YEAR(a) = 2019` or `SELECT * FROM t2 WHERE DATE(a) <= '2017-01-01'`. See [Sargable DATE and YEAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/sargable-date-and-year) ([MDEV-8320](https://jira.mariadb.org/browse/MDEV-8320))

### Transactions

* The [transaction\_isolation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#transaction_isolation) option is now a system variable, and the tx\_isolation system variable is deprecated ([MDEV-21921](https://jira.mariadb.org/browse/MDEV-21921))

### InnoDB

* Remove [innodb\_defragment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_defragment) and related parameters ([MDEV-30545](https://jira.mariadb.org/browse/MDEV-30545))

### mariadb-backup

* Rename [mariadb-backup’s](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup) xtrabackup\_\* files to mariadb\_backup\_\* ([MDEV-18931](https://jira.mariadb.org/browse/MDEV-18931))

### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 11.1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-11-1).

## Security Vulnerabilities Fixed in [MariaDB 11.1](what-is-mariadb-111.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2024-21096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21096): [MariaDB 11.1.5](mariadb-11-1-5-release-notes.md)
* [CVE-2023-22084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22084): [MariaDB 11.1.3](mariadb-11-1-3-release-notes.md)

## List of All [MariaDB 11.1](what-is-mariadb-111.md) Releases

| Date        | Release                                           | Status      | Release Notes                                    | Changelog                                                      |
| ----------- | ------------------------------------------------- | ----------- | ------------------------------------------------ | -------------------------------------------------------------- |
| 8 Aug 2024  | [MariaDB 11.1.6](mariadb-11-1-6-release-notes.md) | Stable (GA) | [Release Notes](mariadb-11-1-6-release-notes.md) | [Changelog](../../changelogs/11.1/mariadb-11-1-6-changelog.md) |
| 16 May 2024 | [MariaDB 11.1.5](mariadb-11-1-5-release-notes.md) | Stable (GA) | [Release Notes](mariadb-11-1-5-release-notes.md) | [Changelog](../../changelogs/11.1/mariadb-11-1-5-changelog.md) |
| 7 Feb 2024  | [MariaDB 11.1.4](mariadb-11-1-4-release-notes.md) | Stable (GA) | [Release Notes](mariadb-11-1-4-release-notes.md) | [Changelog](../../changelogs/11.1/mariadb-11-1-4-changelog.md) |
| 13 Nov 2023 | [MariaDB 11.1.3](mariadb-11-1-3-release-notes.md) | Stable (GA) | [Release Notes](mariadb-11-1-3-release-notes.md) | [Changelog](../../changelogs/11.1/mariadb-11-1-3-changelog.md) |
| 21 Aug 2023 | [MariaDB 11.1.2](mariadb-11-1-2-release-notes.md) | Stable (GA) | [Release Notes](mariadb-11-1-2-release-notes.md) | [Changelog](../../changelogs/11.1/mariadb-11-1-2-changelog.md) |
| 6 Jun 2023  | [MariaDB 11.1.1](mariadb-11-1-1-release-notes.md) | RC          | [Release Notes](mariadb-11-1-1-release-notes.md) | [Changelog](../../changelogs/11.1/mariadb-11-1-1-changelog.md) |
| 27 Mar 2023 | [MariaDB 11.1.0](mariadb-11-1-0-release-notes.md) | Alpha       | [Release Notes](mariadb-11-1-0-release-notes.md) |                                                                |

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
