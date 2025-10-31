# MariaDB 5.5.42 Release Notes

The most recent release in the [MariaDB 5.5](changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.42) | [Release Notes](mariadb-5542-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5542-changelog.md) | [Overview of 5.5](changes-improvements-in-mariadb-5-5.md)

**Release date:** 19 Feb 2015

This is a [_**Stable**_](../../about/release-criteria.md) _**(GA)**_ release. In general this\
means that there are no known serious bugs, except for those marked as feature\
requests, that no bugs were fixed since last release that caused notable code\
changes, and that we believe the code is ready for general usage (based on bug\
inflow).

**For a description of** [**MariaDB 5.5**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **see the**[**What is MariaDB 5.5?**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **page.**

For a list of changes made in this release, with links to detailed\
information on each push, see the [MariaDB 5.5.42 Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5542-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

### Moved to Git

With this release of [MariaDB 5.5](changes-improvements-in-mariadb-5-5.md), the source code has been moved to Github. See\
the [Using Git](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/general-info/tools/using-git-with-mariadb/using-git) page for more information on how to checkout and\
work with the 5.5 branch.

### MariaDB Audit Plugin

The MariaDB Audit Plugin is now included by default in MariaDB. Some new\
functionality has been added to it and it's also now declared to have maturity\
Stable. The new version of the Audit Plugin is 1.2 and it includes the\
following new features:

* In the audit log passwords are now masked, i.e. the password characters are\
  replaced with asterisks.
* It's now possible to filter logging to include only DDL (CREATE, ALTER, etc.)\
  or DML (INSERT, UPDATE, etc.) statements.

For more information please refer to the [About the MariaDB Audit Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-log-settings) page. The\
plugin is disabled by default.

### Low-level network Client API

With this release we introduce a low-level Client API. Applications, linked with `libmysqlclient` client library can use these functions to read and parse raw protocol packets:

* `unsigned long mysql_net_read_packet(MYSQL *mysql);`
* `unsigned long mysql_net_field_length(unsigned char **packet);`

### Updates & Bug Fixes

[MariaDB 5.5.42](mariadb-5542-release-notes.md) is a maintenance release. It includes several bugfixes and\
updates, including from MySQL 5.5.42. Notable updates include:

* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to [version 7.5.5](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-5-5)
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2015-2568](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2568)
  * [CVE-2015-2573](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2573)
  * [CVE-2015-0433](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0433)
  * [CVE-2015-0441](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0441)

A full list of all changes is in the [changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5542-changelog.md).

Thanks, and enjoy MariaDB!

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
