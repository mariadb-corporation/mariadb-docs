# MariaDB 10.0.38 Release Notes

[Download](https://downloads.mariadb.org/mariadb/10.0.38) | [Release Notes](mariadb-10038-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10038-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 31 Jan 2019

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is a previous stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

This is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* [HeidiSQL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/graphical-and-enhanced-clients/heidisql) updated to 9.5
* With this maintenance release, [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) will reach the end of its [maintenance period](https://mariadb.org/about/maintenance-policy/).\
  Generally speaking this means that this will likely be the final release of\
  the 10.0 series of MariaDB
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.43
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) updated to 5.6.43
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.42-84.2
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.42-84.2
* [MDEV-17475](https://jira.mariadb.org/browse/MDEV-17475): Maximum value of [table\_definition\_cache](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#table_definition_cache) is now `2097152`.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2019-2537](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2537)
  * [CVE-2019-2529](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2529)

## Changelog

For a complete list of changes made in [MariaDB 10.0.38](mariadb-10038-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10038-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.0.38](mariadb-10038-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-0-38-mariadb-connector-j-2-4-0-and-mariadb-connector-node-js-2-0-3-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
