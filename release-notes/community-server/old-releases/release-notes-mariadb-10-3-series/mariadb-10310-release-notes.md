# MariaDB 10.3.10 Release Notes

The most recent release of [MariaDB 10.3](what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](mariadb-10-3-39-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.10) | [Release Notes](mariadb-10310-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10310-changelog.md) | [Overview of 10.3](what-is-mariadb-103.md)

**Release date:** 4 Oct 2018

[MariaDB 10.3](what-is-mariadb-103.md) is an evolution\
of [MariaDB 10.2](../release-notes-mariadb-10-2-series/what-is-mariadb-102.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL.

[MariaDB 10.3.10](mariadb-10310-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of MariaDB Server 10.3 see the** [**What is MariaDB 10.3?**](what-is-mariadb-103.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

Notable changes of this release include:

* [MDEV-14474](https://jira.mariadb.org/browse/MDEV-14474) - Added the [Information Schema CHECK\_CONSTRAINTS Table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-check_constraints-table)
* [MDEV-15511](https://jira.mariadb.org/browse/MDEV-15511) - if available, stunnel can be used during [Galera rsync SST](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster#rsync)
* [MDEV-16934](https://jira.mariadb.org/browse/MDEV-16934) - add new system variable [eq\_range\_index\_dive\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#eq_range_index_dive_limit) to speed up queries that new long nested `IN` lists. For backward compatibility the default value is `0`, meaning "unlimited".
* [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) - mariadb-backup does not work with TRUNCATE
* [MDEV-15872](https://jira.mariadb.org/browse/MDEV-15872) - Crash in online ALTER TABLE...ADD PRIMARY KEY after instant ADD COLUMN...NULL
* [MDEV-17003](https://jira.mariadb.org/browse/MDEV-17003) - service\_manager\_extend\_timeout() being called too often
* [MDEV-17196](https://jira.mariadb.org/browse/MDEV-17196) - Crash during instant ADD COLUMN with long DEFAULT value
* [MDEV-16328](https://jira.mariadb.org/browse/MDEV-16328) - ALTER TABLE...page\_compression\_level should not rebuild table
* The [Galera library](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md) in the repositories has been updated to version 25.3.24.
* Also all changes from [MariaDB 10.2.18](../release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md)
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2019-2503](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2503)

When upgrading from [MariaDB 10.3.8](mariadb-1038-release-notes.md) or earlier to [MariaDB 10.3.9](mariadb-1039-release-notes.md) or higher,\
running [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) is **required** due to changes introduced in[MDEV-14637](https://jira.mariadb.org/browse/MDEV-14637).

## Changelog

For a complete list of changes made in [MariaDB 10.3.10](mariadb-10310-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10310-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.3.10](mariadb-10310-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-3-10-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
