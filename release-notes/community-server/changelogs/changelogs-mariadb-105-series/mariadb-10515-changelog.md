# MariaDB 10.5.15 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.15](https://mariadb.org/download/?tab=mariadb\&release=10.5.15\&product=mariadb)[Release Notes](../../old-releases/10.5/10.5.15.md)[Changelog](mariadb-10515-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 12 Feb 2022

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.15.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.24](../changelogs-mariadb-10-4-series/mariadb-10424-changelog.md)
* Merge [Revision #9aa3564e8a](https://github.com/MariaDB/server/commit/9aa3564e8a) 2022-02-10 21:04:51 +0100 - Merge branch '10.4' into 10.5
* [Revision #012e724deb](https://github.com/MariaDB/server/commit/012e724deb)\
  2022-02-10 17:25:12 +0100
  * [MDEV-27796](https://jira.mariadb.org/browse/MDEV-27796) Windows - starting server with huge innodb-log-buffer-size may fail
* [Revision #9e39d0ae44](https://github.com/MariaDB/server/commit/9e39d0ae44)\
  2022-02-10 11:27:14 +0100
  * [MDEV-25787](https://jira.mariadb.org/browse/MDEV-25787) Bug report: crash on SELECT DISTINCT thousands\_blob\_fields
* [Revision #fd101daa84](https://github.com/MariaDB/server/commit/fd101daa84)\
  2022-02-09 15:10:10 +0200
  * [MDEV-27716](https://jira.mariadb.org/browse/MDEV-27716) mtr\_t::commit() acquires log\_sys.mutex when writing no log
* Merge [Revision #34c5019698](https://github.com/MariaDB/server/commit/34c5019698) 2022-02-09 08:57:41 +0100 - Merge branch '10.5' into bb-10.5-release
* [Revision #5c46751f23](https://github.com/MariaDB/server/commit/5c46751f23)\
  2022-02-09 08:36:41 +0200
  * [MDEV-27734](https://jira.mariadb.org/browse/MDEV-27734) Set innodb\_change\_buffering=none by default
* [Revision #f7704d74cb](https://github.com/MariaDB/server/commit/f7704d74cb)\
  2022-02-08 17:31:40 -0500
  * bump the VERSION
* [Revision #38058c04a4](https://github.com/MariaDB/server/commit/38058c04a4)\
  2022-02-02 14:25:25 +0200
  * [MDEV-26585](https://jira.mariadb.org/browse/MDEV-26585) Wrong query results when `using index for group-by`
* [Revision #d314bd2664](https://github.com/MariaDB/server/commit/d314bd2664)\
  2022-02-02 14:09:21 +0200
  * [MDEV-27442](https://jira.mariadb.org/browse/MDEV-27442) Wrong result upon query with DISTINCT and EXISTS subquery
* [Revision #a1c2380753](https://github.com/MariaDB/server/commit/a1c2380753)\
  2022-02-06 16:05:48 +0200
  * MENT-328 Retry BACKUP STAGE BLOCK DDL in case of deadlocks
* [Revision #0ec27d7b1f](https://github.com/MariaDB/server/commit/0ec27d7b1f)\
  2022-02-02 14:26:38 +0200
  * Don't run innodb\_defgragment under valgrind (too slow)
* [Revision #88fb89acb7](https://github.com/MariaDB/server/commit/88fb89acb7)\
  2022-02-02 16:41:13 +0200
  * Fixes some compiler issues on AIX (
* [Revision #df02de68f3](https://github.com/MariaDB/server/commit/df02de68f3)\
  2020-08-17 19:01:43 +0300
  * Fixed my\_addr\_resolve (cherry picked from 10.6)
* [Revision #881918bf77](https://github.com/MariaDB/server/commit/881918bf77)\
  2022-02-07 00:23:14 +0100
  * [MDEV-27754](https://jira.mariadb.org/browse/MDEV-27754) : Assertion with innodb\_flush\_method=O\_DSYNC

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
