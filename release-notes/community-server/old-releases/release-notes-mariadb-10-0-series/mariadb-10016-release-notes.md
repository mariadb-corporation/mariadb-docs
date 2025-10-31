# MariaDB 10.0.16 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.16) | [Release Notes](mariadb-10016-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10016-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 27 Jan 2015

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current stable series of MariaDB. It is an evolution of\
the [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and\
with backported and reimplemented features from MySQL 5.6.

[MariaDB 10.0.16](mariadb-10016-release-notes.md) is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* The [innodb\_stats\_traditional](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) system variable enables a larger sample of pages for larger tables for the purposes of index statistics calculation.
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) upgraded to 5.6.22
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) upgraded to 5.6.22-71.0
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) upgraded to 7.5.4
* Updates to the [CONNECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) handler (supporting the [JSON table type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect/connect-table-types/connect-json-table-type))
* [innochecksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum) now works with compressed pages, and has a new option to skip corrupt pages.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2015-0411](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0411)
  * [CVE-2015-0382](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0382)
  * [CVE-2015-0381](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0381)
  * [CVE-2015-0432](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0432)
  * [CVE-2014-6568](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6568)
  * [CVE-2015-0374](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0374)

For a complete list of changes made in [MariaDB 10.0.16](mariadb-10016-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10016-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
