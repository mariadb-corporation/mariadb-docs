# MariaDB 10.10.5 Release Notes

The most recent release of [MariaDB 10.10](what-is-mariadb-1010.md) is:[**MariaDB 10.10.7**](mariadb-10-10-7-release-notes.md) **Stable (GA)** [Download Now](https://downloads.mariadb.org/mariadb/10.10.7)

[Download 10.10.5](https://downloads.mariadb.org/mariadb/10.10.5/)[Release Notes](mariadb-10-10-5-release-notes.md)[Changelog](../../changelogs/10.10/10.10.5.md)[Overview of 10.10](what-is-mariadb-1010.md)

**Release date:** 7 Jun 2023

[MariaDB 10.10](what-is-mariadb-1010.md) is a current short-term stable series of MariaDB, [maintained until](https://mariadb.org/about/#maintenance-policy) November 2023. It is an evolution\
of [MariaDB 10.9](../release-notes-mariadb-10-9-series/what-is-mariadb-109.md) with several entirely new features.

[MariaDB 10.10.5](mariadb-10-10-5-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.10**](what-is-mariadb-1010.md) **see the**[**What is MariaDB 10.10?**](what-is-mariadb-1010.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

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
  * CVE-`-``#`

## Changelog

For a complete list of changes made in [MariaDB 10.10.5](mariadb-10-10-5-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/10.10/10.10.5.md).

## Contributors

For a full list of contributors to [MariaDB 10.10.5](mariadb-10-10-5-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-11-4-10-10-5-10-9-7-10-6-14-10-5-21-10-4-30-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
