# MariaDB 11.1.1 Release Notes

The most recent release of [MariaDB 11.1](what-is-mariadb-111.md) is:[**MariaDB 11.1.6**](mariadb-11-1-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.1.6/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.1.6/)

[Download 11.1.1](https://downloads.mariadb.org/mariadb/11.1.1/) | [Release Notes](mariadb-11-1-1-release-notes.md) | [Changelog](../../changelogs/11.1/mariadb-11-1-1-changelog.md) | [Overview of 11.1](what-is-mariadb-111.md)

**Release date:** 6 Jun 2023

**Do not use non-stable (non-GA) releases in production!**

[MariaDB 11.1](what-is-mariadb-111.md) is the current short-term development series of MariaDB, which will be maintained for one year after the Stable (GA) release. It is an evolution of [MariaDB 11.0](../release-notes-mariadb-11-0-series/what-is-mariadb-110.md) with several entirely new features.

[MariaDB 11.1.1](mariadb-11-1-1-release-notes.md) is a [_**Release Candidate (RC)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 11.1**](what-is-mariadb-111.md) **see the**[**What is MariaDB 11.1?**](what-is-mariadb-111.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

* The [transaction\_isolation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#transaction_isolation) option is now a system variable, and the tx\_isolation system variable is deprecated ([MDEV-21921](https://jira.mariadb.org/browse/MDEV-21921))

### InnoDB

* Server crashes in st\_join\_table::choose\_best\_splitting ([MDEV-31403](https://jira.mariadb.org/browse/MDEV-31403))
* Crash with condition pushable into derived and containing outer reference ([MDEV-31240](https://jira.mariadb.org/browse/MDEV-31240))
* InnoDB does not free UNDO after the fix of [MDEV-30671](https://jira.mariadb.org/browse/MDEV-30671) ([MDEV-31234](https://jira.mariadb.org/browse/MDEV-31234))
* InnoDB hang fixes ([MDEV-31158](https://jira.mariadb.org/browse/MDEV-31158), [MDEV-31343](https://jira.mariadb.org/browse/MDEV-31343), [MDEV-31350](https://jira.mariadb.org/browse/MDEV-31350))
* [Innodb\_buffer\_pool\_read\_requests](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#innodb_buffer_pool_read_requests) is not updated correctly ([MDEV-31309](https://jira.mariadb.org/browse/MDEV-31309))
* InnoDB monitor trx\_rseg\_history\_len was accidentally disabled by default ([MDEV-31308](https://jira.mariadb.org/browse/MDEV-31308))
* Revert "[MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster"

### Optimizer

* Crash with condition pushable into derived and containing outer reference ([MDEV-31403](https://jira.mariadb.org/browse/MDEV-31403) [MDEV-31240](https://jira.mariadb.org/browse/MDEV-31240))
* Crash with [EXPLAIN EXTENDED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) for multi-table update of system table ([MDEV-31224](https://jira.mariadb.org/browse/MDEV-31224))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Changelog

For a complete list of changes made in [MariaDB 11.1.1](mariadb-11-1-1-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/11.1/mariadb-11-1-1-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 11.1.1](mariadb-11-1-1-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-11-1-1-11-0-2-now-available/).

**Do not use non-stable (non-GA) releases in production!**

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
