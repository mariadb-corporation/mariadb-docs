# MariaDB 10.2.7 Release Notes

The most recent release of [MariaDB 10.2](what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.7) | [Release Notes](mariadb-1027-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1027-changelog.md) | [Overview of 10.2](what-is-mariadb-102.md)

**Release date:** 12 Jul 2017

[MariaDB 10.2](what-is-mariadb-102.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.2.7](mariadb-1027-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.2**](what-is-mariadb-102.md) **see the**[**What is MariaDB 10.2?**](what-is-mariadb-102.md) **page.**

## Notable Changes

This is the second stable release in the [MariaDB 10.2](what-is-mariadb-102.md) series.

A file format compatibility bug that was introduced in [MariaDB 10.2.2](mariadb-1022-release-notes.md) was fixed in this version of MariaDB. Creating tables with the attribute [page\_compressed=yes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) created InnoDB internal data dictionary records that are incompatible with [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md). [MariaDB 10.2.7](mariadb-1027-release-notes.md) and later will write the dictionary records in a format that is compatible with [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) and will also support the malformed metadata from affected 10.2 versions.**This may prevent a downgrade to earlier** [**MariaDB 10.2**](what-is-mariadb-102.md) **versions.**[See the commit for details.](https://github.com/MariaDB/server/commit/72378a25830184f91005be7e80cfb28381c79f23)

* The [JSON data type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/json) (an alias for LONGTEXT) was introduced.
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-versions) updated to 5.7.18
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.36-82.0
* [mariadb-backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup) beta now included for Red Hat, CentOS, and Fedora packages. See [MDEV-13311](https://jira.mariadb.org/browse/MDEV-13311) for an important note about restoring with this version.
* [MDEV-13125](https://jira.mariadb.org/browse/MDEV-13125): Core dumps can now be enabled dynamically
* [MDEV-13132](https://jira.mariadb.org/browse/MDEV-13132): Literals in the `COLUMN_DEFAULT` column in the [Information Schema COLUMNS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-columns-table) table are now quoted to distinguish them from expressions.
* New variables:
  * [tmp\_disk\_table\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tmp_disk_table_size)
  * [tmp\_memory\_table\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tmp_memory_table_size)
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 10.2](what-is-mariadb-102.md) for Ubuntu 16.10 "Yakkety"
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Notes

For a complete list of changes made in [MariaDB 10.2.7](mariadb-1027-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1027-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
