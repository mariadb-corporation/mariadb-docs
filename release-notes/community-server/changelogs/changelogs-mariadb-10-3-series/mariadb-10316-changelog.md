# MariaDB 10.3.16 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.16/)[Release Notes](../../old-releases/10.3/10.3.16.md)[Changelog](mariadb-10316-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 17 Jun 2019

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.16.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.25](../changelogs-mariadb-102-series/mariadb-10225-changelog.md)
* [Revision #0789a1a18f](https://github.com/MariaDB/server/commit/0789a1a18f)\
  2019-06-15 01:21:40 +0300
  * Updated list of unstable tests for 10.3.16 release
* Merge [Revision #1135244a64](https://github.com/MariaDB/server/commit/1135244a64) 2019-06-14 14:22:14 +0200 - Merge branch '10.2-release' into 10.3-release
* [Revision #2e73561c6c](https://github.com/MariaDB/server/commit/2e73561c6c)\
  2019-05-20 19:08:03 +0200
  * [MDEV-16804](https://jira.mariadb.org/browse/MDEV-16804) SYSTEM VERSIONING columns not showing as GENERATED
* Merge [Revision #4a3d51c76c](https://github.com/MariaDB/server/commit/4a3d51c76c) 2019-06-14 07:36:47 +0200 - Merge branch '10.2' into 10.3
* [Revision #d9fe615ef6](https://github.com/MariaDB/server/commit/d9fe615ef6)\
  2019-06-14 07:16:53 +0300
  * spider\_db\_init(): Do not return uninitialized error\_num
* Merge [Revision #cf78b8c699](https://github.com/MariaDB/server/commit/cf78b8c699) 2019-06-12 08:26:32 +0300 - Merge 10.2 into 10.3
* Merge [Revision #b42dbdbccd](https://github.com/MariaDB/server/commit/b42dbdbccd) 2019-06-11 13:00:18 +0300 - Merge 10.2 into 10.3
* [Revision #490dcfd5d7](https://github.com/MariaDB/server/commit/490dcfd5d7)\
  2019-06-05 20:57:09 +0200
  * [MDEV-19698](https://jira.mariadb.org/browse/MDEV-19698): Cleanup READ\_RECORD::record
* [Revision #f7579518e2](https://github.com/MariaDB/server/commit/f7579518e2)\
  2019-05-27 10:40:04 +0300
  * [MDEV-19600](https://jira.mariadb.org/browse/MDEV-19600): The optimizer should be able to produce rows=1 estimate for unique index with NULLable columns
* [Revision #7060b0320d](https://github.com/MariaDB/server/commit/7060b0320d)\
  2019-05-29 15:14:09 +0300
  * Fixed c++11 narrowing error in table.cc
* Merge [Revision #e99ed820d7](https://github.com/MariaDB/server/commit/e99ed820d7) 2019-05-29 13:04:33 +0300 - Merge 10.2 into 10.3
* Merge [Revision #90a9193685](https://github.com/MariaDB/server/commit/90a9193685) 2019-05-29 11:32:46 +0300 - Merge 10.2 into 10.3
* [Revision #fcb68ffe3d](https://github.com/MariaDB/server/commit/fcb68ffe3d)\
  2018-05-29 23:25:50 +0300
  * Simplified away READ\_RECORD::struct\_length
* [Revision #5d46eeefad](https://github.com/MariaDB/server/commit/5d46eeefad)\
  2018-05-29 23:25:50 +0300
  * Simplified away READ\_RECORD::cache\_records
* [Revision #3950a98a34](https://github.com/MariaDB/server/commit/3950a98a34)\
  2018-05-29 23:25:50 +0300
  * Cleanup unused READ\_RECORD::index
* [Revision #c8d9ec2cbb](https://github.com/MariaDB/server/commit/c8d9ec2cbb)\
  2018-05-29 23:25:50 +0300
  * Cleanup unused READ\_RECORD::forms
* [Revision #617d34ae80](https://github.com/MariaDB/server/commit/617d34ae80)\
  2019-05-27 16:30:17 +0300
  * Fixed wrong reset of join\_cache\_level in join\_outer\*test
* [Revision #592dc59d7a](https://github.com/MariaDB/server/commit/592dc59d7a)\
  2019-05-09 09:36:43 +0200
  * [MDEV-17458](https://jira.mariadb.org/browse/MDEV-17458) Unable to start galera node
* [Revision #d0ef948d70](https://github.com/MariaDB/server/commit/d0ef948d70)\
  2019-02-22 17:06:12 +0200
  * Non-functional change: Remove #ifdef UNIV\_DEBUG
* [Revision #c86773f46f](https://github.com/MariaDB/server/commit/c86773f46f)\
  2019-02-06 22:26:52 +0300
  * [MDEV-18136](https://jira.mariadb.org/browse/MDEV-18136) Server crashes in Item\_func\_dyncol\_create::prepare\_arguments
* [Revision #6473641b9a](https://github.com/MariaDB/server/commit/6473641b9a)\
  2019-02-21 18:59:28 +0300
  * [MDEV-18512](https://jira.mariadb.org/browse/MDEV-18512) using DATETIME(6) as row\_start/row\_end crashes server
* [Revision #b77460508e](https://github.com/MariaDB/server/commit/b77460508e)\
  2019-05-20 13:02:22 +0300
  * [MDEV-19486](https://jira.mariadb.org/browse/MDEV-19486): Fix -Wsign-compare
* [Revision #48a662dae5](https://github.com/MariaDB/server/commit/48a662dae5)\
  2019-05-19 23:15:55 +0300
  * [MDEV-19486](https://jira.mariadb.org/browse/MDEV-19486) Server crashes in row\_upd or row\_upd\_del\_mark\_clust\_rec on REPLACE into a versioned table
* [Revision #7056812ed1](https://github.com/MariaDB/server/commit/7056812ed1)\
  2019-05-20 00:35:30 +0530
  * [MDEV-16214](https://jira.mariadb.org/browse/MDEV-16214): Incorrect plan taken by the optimizer , uses INDEX instead of ref access with ORDER BY
* [Revision #2ae83affef](https://github.com/MariaDB/server/commit/2ae83affef)\
  2019-05-18 11:38:43 +0200
  * update a test result, followup fae6539ef72
* Merge [Revision #c1fd027115](https://github.com/MariaDB/server/commit/c1fd027115) 2019-05-17 17:23:01 +0200 - Merge branch '10.2' into 10.3
* [Revision #e506bef430](https://github.com/MariaDB/server/commit/e506bef430)\
  2019-05-13 14:19:10 +0200
  * [MDEV-15458](https://jira.mariadb.org/browse/MDEV-15458) Segfault in heap\_scan() upon UPDATE after ADD SYSTEM VERSIONING
* [Revision #43623f04a9](https://github.com/MariaDB/server/commit/43623f04a9)\
  2019-05-13 14:22:49 +0200
  * [MDEV-15458](https://jira.mariadb.org/browse/MDEV-15458) Segfault in heap\_scan() upon UPDATE after ADD SYSTEM VERSIONING
* [Revision #73de06c48f](https://github.com/MariaDB/server/commit/73de06c48f)\
  2019-05-10 16:38:54 +0300
  * make method const
* [Revision #3d649c6e37](https://github.com/MariaDB/server/commit/3d649c6e37)\
  2019-05-10 16:21:22 +0300
  * [MDEV-15408](https://jira.mariadb.org/browse/MDEV-15408) Confusing error message upon ER\_VERS\_FIELD\_WRONG\_TYPE while omitting UNSIGNED in BIGINT
* Merge [Revision #3d56adbfac](https://github.com/MariaDB/server/commit/3d56adbfac) 2019-05-16 14:24:29 +0300 - Merge 10.2 into 10.3
* [Revision #b7d22a843e](https://github.com/MariaDB/server/commit/b7d22a843e)\
  2019-05-16 10:16:09 +0400
  * [MDEV-16872](https://jira.mariadb.org/browse/MDEV-16872) Add CAST(expr AS FLOAT)
* Merge [Revision #e0e805759f](https://github.com/MariaDB/server/commit/e0e805759f) 2019-05-15 17:06:05 +0300 - Merge 10.2 into 10.3
* [Revision #fde29f3a22](https://github.com/MariaDB/server/commit/fde29f3a22)\
  2019-05-15 16:33:13 +0400
  * A cleanup for [MDEV-19468](https://jira.mariadb.org/browse/MDEV-19468): Adding a missing #include
* [Revision #6434e495c1](https://github.com/MariaDB/server/commit/6434e495c1)\
  2019-05-15 15:22:06 +0400
  * A cleanup for [MDEV-19468](https://jira.mariadb.org/browse/MDEV-19468) Hybrid type expressions return wrong format for FLOAT
* [Revision #462d689397](https://github.com/MariaDB/server/commit/462d689397)\
  2019-05-14 21:47:38 +0400
  * [MDEV-19468](https://jira.mariadb.org/browse/MDEV-19468) Hybrid type expressions return wrong format for FLOAT
* [Revision #4937339705](https://github.com/MariaDB/server/commit/4937339705)\
  2019-05-14 19:40:21 +0300
  * [MDEV-19445](https://jira.mariadb.org/browse/MDEV-19445): After-merge fix
* Merge [Revision #73e038520f](https://github.com/MariaDB/server/commit/73e038520f) 2019-05-14 18:10:06 +0300 - Merge 10.2 into 10.3
* Merge [Revision #874f8f30f2](https://github.com/MariaDB/server/commit/874f8f30f2) 2019-05-14 17:25:25 +0300 - Merge 10.2 into 10.3
* Merge [Revision #be85d3e61b](https://github.com/MariaDB/server/commit/be85d3e61b) 2019-05-14 17:18:46 +0300 - Merge 10.2 into 10.3
* [Revision #c0bc9480e7](https://github.com/MariaDB/server/commit/c0bc9480e7)\
  2019-05-14 10:07:57 -0400
  * bump the VERSION
* Merge [Revision #518cb2bb97](https://github.com/MariaDB/server/commit/518cb2bb97) 2019-05-14 14:23:35 +0200 - Merge branch 'bb-10.3-release' into 10.3
* [Revision #06b50da770](https://github.com/MariaDB/server/commit/06b50da770)\
  2019-05-13 14:54:35 +0000
  * Fix typo THRASH\_FREED\_MEMORY->TRASH\_FREED\_MEMORY
* [Revision #374dae3ecc](https://github.com/MariaDB/server/commit/374dae3ecc)\
  2019-05-13 14:31:15 +0000
  * [MDEV-19452](https://jira.mariadb.org/browse/MDEV-19452) - fix incorrect push\_warning\_printf
* [Revision #0c188d5efc](https://github.com/MariaDB/server/commit/0c188d5efc)\
  2019-05-13 10:08:42 +0000
  * Make TRASH\_FREED\_MEMORY a cmake option, similar to SAFEMALLOC

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
