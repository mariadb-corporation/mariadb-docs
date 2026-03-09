# MariaDB 10.4.30 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.30](https://downloads.mariadb.org/mariadb/10.4.30/)[Release Notes](../../old-releases/10.4/10.4.30.md)[Changelog](mariadb-10-4-30-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 7 Jun 2023

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.30.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.39](../changelogs-mariadb-10-3-series/mariadb-10-3-39-changelog.md)
* [Revision #928012a27a](https://github.com/MariaDB/server/commit/928012a27a)\
  2023-06-05 16:40:08 +0300
  * [MDEV-31403](https://jira.mariadb.org/browse/MDEV-31403): Server crashes in st\_join\_table::choose\_best\_splitting
* [Revision #eb472f77e3](https://github.com/MariaDB/server/commit/eb472f77e3)\
  2023-06-03 10:35:59 +0200
  * Revert "[MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster"
* [Revision #0fd54c9892](https://github.com/MariaDB/server/commit/0fd54c9892)\
  2023-06-03 10:15:18 +0200
  * Revert "[MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster"
* [Revision #8f3bf593d2](https://github.com/MariaDB/server/commit/8f3bf593d2)\
  2023-05-11 23:34:41 -0700
  * [MDEV-31240](https://jira.mariadb.org/browse/MDEV-31240) Crash with condition pushable into derived and containing outer reference
* [Revision #aa713f5ae2](https://github.com/MariaDB/server/commit/aa713f5ae2)\
  2023-05-09 21:20:10 -0700
  * [MDEV-31224](https://jira.mariadb.org/browse/MDEV-31224) Crash with EXPLAIN EXTENDED for multi-table update of system table
* [Revision #54324e542f](https://github.com/MariaDB/server/commit/54324e542f)\
  2023-05-10 08:11:15 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
