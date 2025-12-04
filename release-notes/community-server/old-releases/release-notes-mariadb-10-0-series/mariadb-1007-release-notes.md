# MariaDB 10.0.7 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.7) | **Release Notes** | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1007-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 27 Dec 2013

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current development version of MariaDB. It is an evolution\
of the [MariaDB 5.5 series](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new\
features not found anywhere else and with backported and\
reimplemented features from MySQL 5.6.

[MariaDB 10.0.7](mariadb-1007-release-notes.md) is a [_**Beta**_](../../about/release-criteria.md) release. This is the\
eighth 10.0-based release, and the third beta release. We are releasing it now\
to get it into the hands of any who might want to test it. All features planned\
for inclusion in the stable (GA) [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series are included in this\
release. This is still a beta however, not a final, production-ready, release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Bug fixes

[MariaDB 10.0.7](mariadb-1007-release-notes.md) is primarily a bug-fix release including fixes for the following bugs and security vulnerabilities:

* [CVE-2014-0402](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0402)
* [CVE-2014-0386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0386)
* [CVE-2013-5891](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-5891)
* [CVE-2014-0393](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0393)
* [EXTRACT (HOUR FROM ...)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/extract) now adheres to the SQL standard and returns values from 0 to 23. Previously it could return greater values.

For a list of changes made in [MariaDB 10.0.7](mariadb-1007-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1007-changelog.md).

## Plugins

The following plugins were updated or added in [MariaDB 10.0.7](mariadb-1007-release-notes.md):

* [XtraDB storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-unmaintained/about-xtradb) was upgraded to the 5.6 version. Now one can use XtraDB with [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md). Unlike [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), in 10.0 XtraDB is not the default engine, the default is InnoDB, and XtraDB is available as a dynamic plugin.
* [OQGraph storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/oqgraph-storage-engine) was upgraded to the version 3. Unlike OQGraph v2, that stores all the data in memory, new OQGraph v3 stores them in a table of another storage engine, on disk. Which makes your graphs persistent and also can support much larger graphs. See the [OQGraph](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/oqgraph-storage-engine) documentation for details.
* A new plugin [metadata\_lock\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/metadata-lock-info-plugin) was added. It implements a new table `INFORMATION_SCHEMA.METADATA_LOCK_INFO` that shows active metadata locks.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
