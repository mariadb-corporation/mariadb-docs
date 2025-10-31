# MariaDB 10.0.23 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.23) | [Release Notes](mariadb-10023-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10023-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 18 Dec 2015

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is a previous stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

[MariaDB 10.0.23](mariadb-10023-release-notes.md) is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to XtraDB-5.6.27-76.0
* [Innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to InnoDB-5.6.28
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) updated to 5.6.28
* [Connect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) updated to 1.04.0005
  * numerous new [JSON User Defined Functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect/connect-table-types/connect-json-table-type#json-user-defined-functions).
* [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) updated to 3.2.37
  * new variable, [spider\_connect\_error\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.26-74.0
* [PCRE Regular Expressions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) updated to 8.38
* The [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status) field, `seconds_behind_master`, is now, with [parallel replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/parallel-replication), only updated after transactions commit.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2016-0546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0546)
  * [CVE-2016-0505](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0505)
  * [CVE-2016-0596](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0596)
  * [CVE-2016-0597](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0597)
  * [CVE-2016-0616](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0616)
  * [CVE-2016-0598](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0598)
  * [CVE-2016-0600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0600)
  * [CVE-2016-0606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0606)
  * [CVE-2016-0608](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0608)
  * [CVE-2016-0609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0609)
  * [CVE-2016-0642](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0642)
  * [CVE-2016-0651](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0651)
  * [CVE-2016-2047](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-2047): [MDEV-9212](https://jira.mariadb.org/browse/MDEV-9212): Fixed incorrect implementation of the `--ssl-verify-server-cert`\
    option that allowed a malicious attacker (with a capability to perform a\
    man-in-the-middle attack) to replace the server SSL certificate, bypassing\
    the client-side hostname verification. This vulnerability was discovered by\
    Paul Kehrer and Alex Gaynor.

### SLES 11 Support

Previous builds of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) for Suse Linux Enterprise Server (SLES) 11 only\
supported SLES 11 SP3 and SP4. Starting with this release, SLES 11 builds for\
x86\_64 also support SLES 11 SP1 and SP2.

### Deprecated Distributions

As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the\
last release of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) for Fedora 21.

## Changelog

For a complete list of changes made in [MariaDB 10.0.23](mariadb-10023-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10023-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
