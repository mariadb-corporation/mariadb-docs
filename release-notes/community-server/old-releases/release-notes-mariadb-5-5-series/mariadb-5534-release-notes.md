# MariaDB 5.5.34 Release Notes

The most recent release in the [MariaDB 5.5](changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.34) | **Release Notes** | [Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5534-changelog.md) | [Overview of 5.5](changes-improvements-in-mariadb-5-5.md)

**Release date:** 21 Nov 2013

This is a [_**Stable**_](../../about/release-criteria.md) _**(GA)**_ release. In general this\
means that there are no known serious bugs, except for those marked as feature\
requests, that no bugs were fixed since last release that caused a notable code\
changes, and that we believe the code is ready for general usage (based on bug\
inflow).

**For a description of** [**MariaDB 5.5**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **see the**[**What is MariaDB 5.5?**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/broken-reference/README.md) **page.**

For a list of changes made in this release, with links to detailed\
information on each push, see the [MariaDB 5.5.34 Changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5534-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

### Updates & Bug Fixes

[MariaDB 5.5.34](mariadb-5534-release-notes.md) is a maintenance release. It includes all bugfixes and updates from the following:

* MySQL 5.5.34
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) from Percona-Server-5.5.34-rel32.0
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) 7.1.0
* [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) no longer sets the `write-binlog` option by default.
* Also included are fixes for the following security vulnerabilities:
  * [CVE-2014-0402](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0402)
  * [CVE-2014-0386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0386)
  * [CVE-2013-5891](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-5891)
  * [CVE-2014-0393](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0393)

Also, as per [MDEV-5038](https://jira.mariadb.org/browse/MDEV-5038), TokuDB is now included in the MariaDB Server package, instead of as a separate .rpm or .deb package. **Note:** _because of this change, you need to use_ **`apt-get dist-upgrade`**_, not_`apt-get upgrade`_to upgrade to this release from our Debian and Ubuntu APT repositories._

Full details of all changes are in the [changelog](../../changelogs/changelogs-mariadb-55-series/mariadb-5534-changelog.md).

## Fedora & Ubuntu

As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the final release of MariaDB for Fedora 17. When the next version of [MariaDB 5.5](changes-improvements-in-mariadb-5-5.md) is released, the Fedora 17 repositories will go away. This will likely also be the final release of MariaDB for Fedora 18.

With this release Fedora 19 "Schrödinger's Cat" and Ubuntu 13.10 "Saucy Salamander" repositories have been added. It is worth noting that MariaDB is included in the official Fedora 19 repositories, so there is no need to add our repositories unless you are using [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) or for testing and development.

We plan to add Fedora 20 "Heisenbug" repositories soon after it is released in mid December.

Thanks, and enjoy MariaDB!

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
