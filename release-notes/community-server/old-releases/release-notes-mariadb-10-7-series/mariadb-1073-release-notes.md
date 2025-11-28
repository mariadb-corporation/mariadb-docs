# MariaDB 10.7.3 Release Notes

The most recent release of [MariaDB 10.7](what-is-mariadb-107.md) is:[**MariaDB 10.7.8**](mariadb-10-7-8-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.7.8/)

[Download 10.7.3](https://downloads.mariadb.org/mariadb/10.7.3/) | [Release Notes](mariadb-1073-release-notes.md) | [Changelog](../../changelogs/10.7/10.7.3.md) | [Overview of 10.7](what-is-mariadb-107.md)

**Release date:** 12 Feb 2022

[MariaDB 10.7](what-is-mariadb-107.md) is the current short-term maintenance stable series of MariaDB. It is an evolution\
of [MariaDB 10.6](../../10.6/what-is-mariadb-106.md) with several entirely new features.

[MariaDB 10.7.3](mariadb-1073-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.7**](what-is-mariadb-107.md) **see the**[**What is MariaDB 10.7?**](what-is-mariadb-107.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

* This release fixes a blocking problem with the [MariaDB 10.7.2](mariadb-1072-release-notes.md) release when manually running [mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade). ([MDEV-27789](https://jira.mariadb.org/browse/MDEV-27789))
* See [MariaDB 10.7.2](mariadb-1072-release-notes.md) for other changes since the previous release.

### InnoDB

* Set [innodb\_change\_buffering=none](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_change_buffering) by default ([MDEV-27734](https://jira.mariadb.org/browse/MDEV-27734))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2021-46665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46665)
  * [CVE-2021-46664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46664)
  * [CVE-2021-46661](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46661)
  * [CVE-2021-46668](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46668)
  * [CVE-2021-46663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46663)

## Changelog

For a complete list of changes made in [MariaDB 10.7.3](mariadb-1073-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/10.7/10.7.3.md).

## Contributors

For a full list of contributors to [MariaDB 10.7.3](mariadb-1073-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-8-2-rc-and-mariadb-10-7-3-10-6-7-10-5-15-10-4-24-10-3-34-and-10-2-43-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
