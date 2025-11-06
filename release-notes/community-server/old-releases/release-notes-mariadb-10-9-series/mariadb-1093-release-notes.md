# MariaDB 10.9.3 Release Notes

The most recent release of [MariaDB 10.9](what-is-mariadb-109.md) is:[**MariaDB 10.9.8**](mariadb-10-9-8-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.9.8/)

[Download 10.9.3](https://downloads.mariadb.org/mariadb/10.9.3/) | [Release Notes](mariadb-1093-release-notes.md) | [Changelog](../../changelogs/10.9/10.9.3.md) | [Overview of 10.9](what-is-mariadb-109.md)

**Release date:** 19 Sep 2022

[MariaDB 10.9](what-is-mariadb-109.md) is the current short-term maintenance stable series of MariaDB, maintained until August 2023. It is an evolution of [MariaDB 10.8](../release-notes-mariadb-10-8-series/what-is-mariadb-108.md) with several entirely new features.

[MariaDB 10.9.3](mariadb-1093-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.9**](what-is-mariadb-109.md) **see the**[**What is MariaDB 10.9?**](what-is-mariadb-109.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### Issues Fixed

* Assertion mysql\_mutex\_assert\_owner(\&log\_sys.flush\_order\_mutex) failed in mtr\_t::commit() ([MDEV-29383](https://jira.mariadb.org/browse/MDEV-29383))
* Frequent "Data structure corruption" in InnoDB after OOM ([MDEV-29374](https://jira.mariadb.org/browse/MDEV-29374))
* Recovery or backup of instant ALTER TABLE is incorrect ([MDEV-29438](https://jira.mariadb.org/browse/MDEV-29438))
* InnoDB Temporary Tablespace (ibtmp1) is continuously growing ([MDEV-28240](https://jira.mariadb.org/browse/MDEV-28240))
* Full text index corruption if shutdown before changes are fully flushed ([MDEV-29342](https://jira.mariadb.org/browse/MDEV-29342))
* [JSON\_VALUE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_value) does not parse NULL properties properly ([MDEV-27151](https://jira.mariadb.org/browse/MDEV-27151))
* InnoDB hangs on multiple concurrent requests of a cold ROW\_FORMAT=COMPRESSED page ([MDEV-27983](https://jira.mariadb.org/browse/MDEV-27983))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-`-``#`

## Changelog

For a complete list of changes made in [MariaDB 10.9.3](mariadb-1093-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/10.9/10.9.3.md).

## Contributors

For a full list of contributors to [MariaDB 10.9.3](mariadb-1093-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-9-3-10-8-5-10-7-6-and-10-6-10-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
