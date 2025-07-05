# MariaDB 10.2.8 Release Notes

The most recent release of [MariaDB 10.2](what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.8)[Release Notes](mariadb-1028-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1028-changelog.md)[Overview of 10.2](what-is-mariadb-102.md)

**Release date:** 18 Aug 2017

[MariaDB 10.2](what-is-mariadb-102.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.2.8](mariadb-1028-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.2**](what-is-mariadb-102.md) **see the**[**What is MariaDB 10.2?**](what-is-mariadb-102.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-versions) updated to 5.7.19
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/tokudb) updated to 5.6.36-82.1
* [CONNECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) engine updated to 1.06.0001
  * Beta support for [MongoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect/connect-table-types/connect-mongo-table-type) added
* Fix [ST\_GeomFromGeoJSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-constructors/st_geomfromgeojson) ([MDEV-12181](https://jira.mariadb.org/browse/MDEV-12181))
* Fix [ST\_AsGeoJSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-constructors/geojson-st_asgeojson) ([MDEV-12180](https://jira.mariadb.org/browse/MDEV-12180))
* Fixed bug that permitted columns being dropped which would result in an additional constraint being added to the table. See the example in [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#drop-column-if-exists-col_name-cascaderestrict) ([MDEV-11114](https://jira.mariadb.org/browse/MDEV-11114)).
* Nonsensical combinations of SIGNED, UNSIGNED and ZEROFILL are no longer permitted - see [Numeric Data Type Overview](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/numeric-data-type-overview) ([MDEV-8659](https://jira.mariadb.org/browse/MDEV-8659)).
* [mariadb-backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup) now included for Debian and Ubuntu (in [MariaDB 10.2.7](mariadb-1027-release-notes.md) it was released only for Red Hat, CentOS, and Fedora)
* Fedora 26 repositories have been added in this release.
* As per the [MariaDB Deprecation Policy](../../../mariadb-platform-deprecation-policy.md), this will be the last release of [MariaDB 10.2](what-is-mariadb-102.md) for Fedora 24.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2017-3636](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3636)
  * [CVE-2017-3641](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3641)
  * [CVE-2017-3653](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3653)
  * [CVE-2017-10320](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10320)
  * [CVE-2017-10365](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10365)
  * [CVE-2017-10379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10379)
  * [CVE-2017-10384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10384)
  * [CVE-2017-10286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10286)
  * [CVE-2017-3257](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3257)

## Notes

For a complete list of changes made in [MariaDB 10.2.8](mariadb-1028-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1028-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
