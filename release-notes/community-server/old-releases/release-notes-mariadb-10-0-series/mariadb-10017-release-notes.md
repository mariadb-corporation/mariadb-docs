# MariaDB 10.0.17 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.17) | [Release Notes](mariadb-10017-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10017-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 27 Feb 2015

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

[MariaDB 10.0.17](mariadb-10017-release-notes.md) is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* The new version of the [Audit Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) is 1.2 and includes the following new features:
  * In the audit log, passwords are now masked, i.e. the password characters are replaced with asterisks.
  * It's now possible to filter logging to include only DDL (CREATE, ALTER, etc.) or DML (INSERT, UPDATE, etc.) statements.
  * For more information please refer to the [About the MariaDB Audit Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-log-settings) page. The plugin is disabled by default.
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.23
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.22-72.0
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 7.5.5
* [mroonga](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/mroonga) updated to 5.0
* [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) updated to 3.2.18
* [Connect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) updated to 1.03.0005
* [HeidiSQL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/graphical-and-enhanced-clients/heidisql) updated to 9.1 ([MDEV-7290](https://jira.mariadb.org/browse/MDEV-7290))
* `--galera-sst-mode` option removed from [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) ([MDEV-7615](https://jira.mariadb.org/browse/MDEV-7615))
* `[mysqlbinlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-binlog/) --binlog-row-event-max-size` support added ([MDEV-6703](https://jira.mariadb.org/browse/MDEV-6703))
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2015-2568](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2568)
  * [CVE-2015-2573](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2573)
  * [CVE-2015-0433](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0433)
  * [CVE-2015-0441](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0441)

For a complete list of changes made in [MariaDB 10.0.17](mariadb-10017-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10017-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
