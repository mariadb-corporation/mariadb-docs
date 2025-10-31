# MariaDB 10.0.35 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.35) | [Release Notes](mariadb-10035-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10035-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 3 May 2018

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is a previous stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

This is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* [PCRE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) updated to 8.42
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.39-83.1
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.39-83.1
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.40
* The embedded server library now supports SSL when connecting to remote servers.
* [MDEV-15249](https://jira.mariadb.org/browse/MDEV-15249) - Crash in MVCC read after IMPORT TABLESPACE
* [MDEV-14988](https://jira.mariadb.org/browse/MDEV-14988) - innodb\_read\_only tries to modify files if transactions were recovered in COMMITTED state
* [MDEV-14773](https://jira.mariadb.org/browse/MDEV-14773) - DROP TABLE hangs for InnoDB table with FULLTEXT index
* [MDEV-15723](https://jira.mariadb.org/browse/MDEV-15723) - Crash in INFORMATION\_SCHEMA.INNODB\_SYS\_TABLES when accessing corrupted record
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be\
  the last release of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) for Debian 7 Wheezy
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2018-2755](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2755)
  * [CVE-2018-2761](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2761)
  * [CVE-2018-2766](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2766)
  * [CVE-2018-2767](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2767)
  * [CVE-2018-2771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2771)
  * [CVE-2018-2781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2781)
  * [CVE-2018-2782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2782)
  * [CVE-2018-2784](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2784)
  * [CVE-2018-2787](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2787)
  * [CVE-2018-2813](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2813)
  * [CVE-2018-2817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2817)
  * [CVE-2018-2819](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-2819)
  * [CVE-2018-3081](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3081)
  * [CVE-2019-2455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2455)
  * [CVE-2020-14550](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14550)
  * [CVE-2021-2011](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2011)

## Changelog

For a complete list of changes made in [MariaDB 10.0.35](mariadb-10035-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10035-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.0.35](mariadb-10035-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-0-35-mariadb-galera-cluster-5-5-60-and-mariadb-connector-c-3-0-4-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
