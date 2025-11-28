# MariaDB 10.8.2 Release notes

The most recent release of [MariaDB 10.8](what-is-mariadb-108.md) is:[**MariaDB 10.8.8**](mariadb-10-8-8-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.8.8/)

[Download 10.8.2](https://downloads.mariadb.org/mariadb/10.8.2/) | [Release Notes](mariadb-1082-release-notes.md) | [Changelog](../../changelogs/10.8/10.8.2.md) | [Overview of 10.8](what-is-mariadb-108.md)

**Release date:** 12 Feb 2022

**Do not use non-stable (non-GA) releases in production!**

[MariaDB 10.8](what-is-mariadb-108.md) is the current development series of MariaDB. It is an evolution\
of [MariaDB 10.7](../release-notes-mariadb-10-7-series/what-is-mariadb-107.md) with several entirely new features.

[MariaDB 10.8.2](mariadb-1082-release-notes.md) is a [_**Release Candidate (RC)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.8**](what-is-mariadb-108.md) **see the**[**What is MariaDB 10.8?**](what-is-mariadb-108.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

* This release fixes a blocking problem with the [MariaDB 10.8.1](mariadb-1081-release-notes.md) release when manually running [mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade). ([MDEV-27789](https://jira.mariadb.org/browse/MDEV-27789))
* See [MariaDB 10.8.1](mariadb-1081-release-notes.md) for other changes since the previous release.

### InnoDB

* Set [innodb\_change\_buffering=none](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_change_buffering) by default ([MDEV-27734](https://jira.mariadb.org/browse/MDEV-27734))

### General

* Fix mismatched braces for non-Linux targets (fails to build) ([MDEV-27790](https://jira.mariadb.org/browse/MDEV-27790))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Changelog

For a complete list of changes made in [MariaDB 10.8.2](mariadb-1082-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/10.8/10.8.2.md).

## Contributors

For a full list of contributors to [MariaDB 10.8.2](mariadb-1082-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-8-2-rc-and-mariadb-10-7-3-10-6-7-10-5-15-10-4-24-10-3-34-and-10-2-43-now-available/).

**Do not use non-stable (non-GA) releases in production!**

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
