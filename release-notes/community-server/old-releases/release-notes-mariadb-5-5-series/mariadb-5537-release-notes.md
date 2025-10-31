# MariaDB 5.5.37 Release Notes

The most recent release in the [MariaDB 5.5](changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.37) | **Release Notes** | [Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5537-changelog.md) | [Overview of 5.5](changes-improvements-in-mariadb-5-5.md)

**Release date:** 17 Apr 2014

This is a [_**Stable**_](../../about/release-criteria.md) _**(GA)**_ release. In general this\
means that there are no known serious bugs, except for those marked as feature\
requests, that no bugs were fixed since last release that caused notable code\
changes, and that we believe the code is ready for general usage (based on bug\
inflow).

**For a description of** [**MariaDB 5.5**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **see the**[**What is MariaDB 5.5?**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **page.**

For a list of changes made in this release, with links to detailed\
information on each push, see the [MariaDB 5.5.37 Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5537-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

### Updates & Bug Fixes

[MariaDB 5.5.37](mariadb-5537-release-notes.md) is a maintenance release. It includes several bugfixes and updates, including\
from MySQL 5.5.37. Notable updates include:

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to the version from [Percona Server 5.5.36-34.0](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.36-34.0.html)
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to [version 7.1.5](https://www.tokutek.com/wp-content/uploads/2014/03/mariadb-5.5.36-tokudb-7.1.5-users-guide.pdf)
* Default compression for [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) is now `TOKUDB_ZLIB` (instead\
  of `TOKUDB_UNCOMPRESSED`)
* The [MariaDB Audit Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) now included.
* Fixes for the following security vulnerabilities:
  * [CVE-2014-2436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2436)
  * [CVE-2014-2440](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2440)
  * [CVE-2014-2430](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2430)
  * [CVE-2014-2431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2431)
  * [CVE-2019-2481](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2481)

A full list of all changes is in the [changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5537-changelog.md).

Thanks, and enjoy MariaDB!

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
