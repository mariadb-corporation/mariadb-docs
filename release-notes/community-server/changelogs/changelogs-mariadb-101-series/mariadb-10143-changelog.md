# MariaDB 10.1.43 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.43/)[Release Notes](../../old-releases/10.1/10.1.43.md)[Changelog](mariadb-10143-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 8 Nov 2019

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.43.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 5.5.66](../changelogs-mariadb-55-series/mariadb-5566-changelog.md)
* Merge [Revision #4e99e67c4e](https://github.com/MariaDB/server/commit/4e99e67c4e) 2019-11-06 08:17:03 +0200 - Merge 5.5 into 10.1
* [Revision #cd156e2c3e](https://github.com/MariaDB/server/commit/cd156e2c3e)\
  2019-11-04 18:30:48 +0100
  * [MDEV-20971](https://jira.mariadb.org/browse/MDEV-20971) ASAN heap-use-after-free in list\_delete / heap\_close
* [Revision #5c3bbbd845](https://github.com/MariaDB/server/commit/5c3bbbd845)\
  2019-11-06 10:20:32 +0530
  * [MDEV-20987](https://jira.mariadb.org/browse/MDEV-20987) InnoDB fails to start when fts table has FK relation
* [Revision #6e48f3a062](https://github.com/MariaDB/server/commit/6e48f3a062)\
  2019-11-05 09:55:18 -0500
  * bump the VERSION
* [Revision #dc771113a6](https://github.com/MariaDB/server/commit/dc771113a6)\
  2019-11-05 00:20:13 +0100
  * Fix ninja build
* [Revision #5164f8c206](https://github.com/MariaDB/server/commit/5164f8c206)\
  2019-11-04 15:52:54 +0200
  * Fix GCC 9.2.1 -Wstringop-truncation
* [Revision #eb56339b66](https://github.com/MariaDB/server/commit/eb56339b66)\
  2019-10-09 12:01:19 +0200
  * Fix build on !glibc/powerpc\*
* [Revision #8afe4bba2e](https://github.com/MariaDB/server/commit/8afe4bba2e)\
  2019-10-27 01:48:00 +0530
  * [MDEV-20424](https://jira.mariadb.org/browse/MDEV-20424): New default value for optimizer\_use\_condition-selectivity leads to bad plan
* [Revision #6f86150ab3](https://github.com/MariaDB/server/commit/6f86150ab3)\
  2019-10-10 12:58:29 +0300
  * [MDEV-17896](https://jira.mariadb.org/browse/MDEV-17896) Assertion \`pfs->get\_refcount() > 0' failed
* Also see the [MariaDB 10.1.42 Changelog](mariadb-10142-changelog.md)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
