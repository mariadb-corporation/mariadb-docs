# MariaDB 10.0.15 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.15) | [Release Notes](mariadb-10015-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10015-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 25 Nov 2014

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and\
with backported and reimplemented features from MySQL 5.6.

[MariaDB 10.0.15](mariadb-10015-release-notes.md) is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* This release fixes a serious bug in InnoDB and XtraDB that sometimes could cause a hard lock up of the server ([MDEV-7026](https://jira.mariadb.org/browse/MDEV-7026)).
* This is the first release that includes [Mroonga](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/mroonga) full-text search storage engine.
* When compiled with OpenSSL, MariaDB now supports TLSv1.2 protocol. Limit it to TLSv1.2 ciphers only with `--ssl_cipher=TLSv1.2`. Limit it to SSLv3 ciphers with `--ssl-cipher=SSLv3`. RPM and DEB packages from [MariaDB.org](https://downloads.mariadb.org) are built with OpenSSL, others (for Windows and generic Linux) are built with yaSSL.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2014-6507](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6507)
  * [CVE-2014-6491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6491)
  * [CVE-2014-6500](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6500)
  * [CVE-2014-6469](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6469)
  * [CVE-2014-6555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6555)
  * [CVE-2014-6559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6559)
  * [CVE-2014-6494](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6494)
  * [CVE-2014-6496](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6496)
  * [CVE-2014-6464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6464)
* Bundled [PCRE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) is upgraded to 8.36
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) upgraded to 5.6.21
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) upgraded to 5.6.21-70.0
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) upgraded to 7.5.3
* [SphinxSE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/sphinx-storage-engine) upgraded to 2.2.6
* Updates to the [CONNECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) handler including:
  * A new [VIR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect/connect-table-types/connect-table-types-vir) virtual table type.
  * New variables [connect\_use\_tempfile](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect/connect-system-variables#connect_use_tempfile) and [connect\_exact\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect/connect-system-variables#connect_exact_info)
* We now offer openSUSE repos, see the [repository configuration tool](https://downloads.mariadb.org/mariadb/repositories/)\
  for details on how to use it.

For a complete list of changes made in [MariaDB 10.0.15](mariadb-10015-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10015-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
