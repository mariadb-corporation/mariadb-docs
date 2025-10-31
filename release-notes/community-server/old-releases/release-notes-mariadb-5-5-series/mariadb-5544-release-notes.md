# MariaDB 5.5.44 Release Notes

The most recent release in the [MariaDB 5.5](changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.44) | [Release Notes](mariadb-5544-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5544-changelog.md) | [Overview of 5.5](changes-improvements-in-mariadb-5-5.md)

**Release date:** 11 Jun 2015

This is a [_**Stable**_](../../about/release-criteria.md) _**(GA)**_ release. In general this\
means that there are no known serious bugs, except for those marked as feature\
requests, that no bugs were fixed since last release that caused notable code\
changes, and that we believe the code is ready for general usage (based on bug\
inflow).

**For a description of** [**MariaDB 5.5**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **see the**[**What is MariaDB 5.5?**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **page.**

For a list of changes made in this release, with links to detailed\
information on each push, see the [MariaDB 5.5.44 Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5544-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

### Updates & Bug Fixes

[MariaDB 5.5.44](mariadb-5544-release-notes.md) is a maintenance release. It includes several bugfixes and\
updates, including from MySQL 5.5.44. Notable updates include:

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.5.42-37.2
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to [version 7.5.7](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-5-7)
* Client command line option `--ssl-verify-server-cert` (and `MYSQL_OPT_SSL_VERIFY_SERVER_CERT` option of the client API) when used together with `--ssl` will ensure that the established connection is SSL-encrypted and the MariaDB server has a valid certificate. This fixes [CVE-2015-3152](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-3152).
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2015-2582](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2582)
  * [CVE-2015-2620](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2620)
  * [CVE-2015-2643](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2643)
  * [CVE-2015-2648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2648)
  * [CVE-2015-3152](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-3152)
  * [CVE-2015-4752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4752)
  * [CVE-2015-4864](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4864)

A full list of all changes is in the [changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5544-changelog.md).

Thanks, and enjoy MariaDB!

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
