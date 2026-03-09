# MariaDB 10.3.31 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download 10.3.31](https://downloads.mariadb.org/mariadb/10.3.31/)[Release Notes](../../old-releases/10.3/10.3.31.md)[Changelog](mariadb-10331-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.3.31/)

**Release date:** 6 Aug 2021

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.31.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.40](../changelogs-mariadb-102-series/mariadb-10240-changelog.md)
* Merge [Revision #7f264997dd](https://github.com/MariaDB/server/commit/7f264997dd) 2021-08-02 11:41:00 +0200 - Merge branch '10.2' into 10.3
* [Revision #1423cf5e3d](https://github.com/MariaDB/server/commit/1423cf5e3d)\
  2021-07-29 17:16:52 +0200
  * fix [MDEV-16026](https://jira.mariadb.org/browse/MDEV-16026) [MDEV-16481](https://jira.mariadb.org/browse/MDEV-16481) embedded server results and rests
* Merge [Revision #83d7e4faf6](https://github.com/MariaDB/server/commit/83d7e4faf6) 2021-07-29 13:51:02 +0200 - Merge branch '10.2' into 10.3
* [Revision #6152ab7b42](https://github.com/MariaDB/server/commit/6152ab7b42)\
  2021-07-27 23:45:30 +0200
  * [MDEV-24511](https://jira.mariadb.org/browse/MDEV-24511) null field is created with CREATE..SELECT
* [Revision #c86f813afe](https://github.com/MariaDB/server/commit/c86f813afe)\
  2019-04-23 13:45:28 +0400
  * [MDEV-9234](https://jira.mariadb.org/browse/MDEV-9234) Add Type\_handler::union\_element\_finalize()
* [Revision #9d5967f74b](https://github.com/MariaDB/server/commit/9d5967f74b)\
  2021-07-29 02:08:11 +0300
  * fixup 0bd9f755b [MDEV-26062](https://jira.mariadb.org/browse/MDEV-26062)
* [Revision #43099af95b](https://github.com/MariaDB/server/commit/43099af95b)\
  2021-07-28 23:19:36 +0800
  * [MDEV-24020](https://jira.mariadb.org/browse/MDEV-24020): Trim with remove\_str Fails on Spider
* [Revision #6ed47508c8](https://github.com/MariaDB/server/commit/6ed47508c8)\
  2019-07-18 03:15:55 +1000
  * add const qualifiers to sys\_var::value\_ptr functions and fix const casts
* [Revision #c6bff46958](https://github.com/MariaDB/server/commit/c6bff46958)\
  2019-07-18 23:11:16 +1000
  * [MDEV-16026](https://jira.mariadb.org/browse/MDEV-16026) [MDEV-16481](https://jira.mariadb.org/browse/MDEV-16481) refactor Sys\_var\_vers\_asof
* Merge [Revision #f50eb0d398](https://github.com/MariaDB/server/commit/f50eb0d398) 2021-07-27 10:47:17 +0300 - Merge 10.2 into 10.3
* [Revision #2575eaa502](https://github.com/MariaDB/server/commit/2575eaa502)\
  2021-07-26 12:39:56 +0200
  * dissapear -> disappear
* [Revision #f52d39369a](https://github.com/MariaDB/server/commit/f52d39369a)\
  2021-07-25 17:51:36 +0000
  * [MDEV-24517](https://jira.mariadb.org/browse/MDEV-24517) follow-up: Fix for test with --ps-protocol
* [Revision #eaae13059f](https://github.com/MariaDB/server/commit/eaae13059f)\
  2021-07-24 09:18:50 +0200
  * [MDEV-25808](https://jira.mariadb.org/browse/MDEV-25808) PREPARE/EXECUTE makes signed integer out of unsigned
* [Revision #9fde2bbacf](https://github.com/MariaDB/server/commit/9fde2bbacf)\
  2021-07-23 06:42:50 -0700
  * [MDEV-25484](https://jira.mariadb.org/browse/MDEV-25484) Crash when parsing query using derived table containing TVC
* [Revision #73d32cc100](https://github.com/MariaDB/server/commit/73d32cc100)\
  2021-07-23 22:36:27 +0800
  * [MDEV-24517](https://jira.mariadb.org/browse/MDEV-24517): JSON\_EXTRACT as conditions triggers syntax error on Spider (#1839)
* [Revision #dba7cd25e1](https://github.com/MariaDB/server/commit/dba7cd25e1)\
  2021-06-28 20:59:29 +0300
  * [MDEV-25560](https://jira.mariadb.org/browse/MDEV-25560) Creating table with certain generated column crashes server
* Merge [Revision #b50ea90063](https://github.com/MariaDB/server/commit/b50ea90063) 2021-07-22 18:57:54 +0300 - Merge 10.2 into 10.3
* Merge [Revision #6190a02f35](https://github.com/MariaDB/server/commit/6190a02f35) 2021-07-21 20:11:07 +0200 - Merge branch '10.2' into 10.3
* [Revision #cf6d83e7d6](https://github.com/MariaDB/server/commit/cf6d83e7d6)\
  2021-07-19 12:10:45 +0000
  * [MDEV-24760](https://jira.mariadb.org/browse/MDEV-24760) SELECT..CASE statement syntax error at Spider Engine table
* [Revision #efa311ab8e](https://github.com/MariaDB/server/commit/efa311ab8e)\
  2021-07-18 21:08:23 +0700
  * [MDEV-26147](https://jira.mariadb.org/browse/MDEV-26147): The test main.sp-row fails in case it is run in PS mode
* [Revision #de85e29436](https://github.com/MariaDB/server/commit/de85e29436)\
  2021-07-15 17:43:13 +0200
  * [MDEV-25326](https://jira.mariadb.org/browse/MDEV-25326) mysql\_install\_db help text incomplete
* [Revision #3fbe30024f](https://github.com/MariaDB/server/commit/3fbe30024f)\
  2021-07-07 10:58:25 +0200
  * [MDEV-26080](https://jira.mariadb.org/browse/MDEV-26080): SHOW GRANTS does not quote role names properly for DEFAULT ROLE
* [Revision #07fade6d18](https://github.com/MariaDB/server/commit/07fade6d18)\
  2021-07-06 01:02:10 +0300
  * [MDEV-22247](https://jira.mariadb.org/browse/MDEV-22247) History partition overflow leads to wrong SELECT result
* [Revision #e09e304b78](https://github.com/MariaDB/server/commit/e09e304b78)\
  2021-07-06 01:02:09 +0300
  * [MDEV-16857](https://jira.mariadb.org/browse/MDEV-16857) system-invisible row\_end is displayed in SHOW INDEX
* Merge [Revision #f9194d02da](https://github.com/MariaDB/server/commit/f9194d02da) 2021-07-02 14:41:41 +0300 - Merge 10.2 into 10.3
* [Revision #a6adefad4b](https://github.com/MariaDB/server/commit/a6adefad4b)\
  2021-07-02 14:41:32 +0300
  * Fixup 586870f9effa48831fda2590f2aee2b95b30be39
* Merge [Revision #05f7fd571f](https://github.com/MariaDB/server/commit/05f7fd571f) 2021-07-02 11:44:51 +0300 - Merge 10.2 into 10.3
* [Revision #e34877ab63](https://github.com/MariaDB/server/commit/e34877ab63)\
  2021-07-01 16:14:09 +0530
  * [MDEV-25971](https://jira.mariadb.org/browse/MDEV-25971) Instant ADD COLUMN fails to issue truncation warnings
* [Revision #7ce5984d6d](https://github.com/MariaDB/server/commit/7ce5984d6d)\
  2021-07-02 15:50:21 +1000
  * mtr: fix tests funcs\_1.is\_tables\_is & sql\_sequence.rebuild
* Merge [Revision #a88ddb168f](https://github.com/MariaDB/server/commit/a88ddb168f) 2021-07-02 16:35:49 +1000 - Merge branch '10.2' into 10.3
* [Revision #0a9487b62b](https://github.com/MariaDB/server/commit/0a9487b62b)\
  2021-07-02 13:00:34 +1000
  * mtr: aix - no pool of threads
* [Revision #3f2c4758b0](https://github.com/MariaDB/server/commit/3f2c4758b0)\
  2021-06-11 17:13:19 +1000
  * [MDEV-25894](https://jira.mariadb.org/browse/MDEV-25894): support AIX as a platform in mtr
* [Revision #4a6e2d3437](https://github.com/MariaDB/server/commit/4a6e2d3437)\
  2021-06-30 16:43:43 +0300
  * Post-merge fix: update derived\_cond\_pushdown.result
* Merge [Revision #586870f9ef](https://github.com/MariaDB/server/commit/586870f9ef) 2021-06-30 15:06:54 +0300 - Merge 10.2->10.3
* [Revision #29098083f7](https://github.com/MariaDB/server/commit/29098083f7)\
  2021-06-25 06:48:17 +0200
  * [MDEV-26019](https://jira.mariadb.org/browse/MDEV-26019): Upgrading MariaDB breaks TLS mariadb-backup SST
* [Revision #05a4996c5c](https://github.com/MariaDB/server/commit/05a4996c5c)\
  2021-06-22 15:44:44 +0300
  * [MDEV-25978](https://jira.mariadb.org/browse/MDEV-25978) : rsync SST does not work with custom binlog name
* [Revision #1deb630484](https://github.com/MariaDB/server/commit/1deb630484)\
  2021-06-22 22:21:24 -0400
  * bump the VERSION
* [Revision #35a9aaebe2](https://github.com/MariaDB/server/commit/35a9aaebe2)\
  2021-06-22 09:30:25 +0300
  * [MDEV-25981](https://jira.mariadb.org/browse/MDEV-25981) InnoDB upgrade fails
* Merge [Revision #e07f0a2d80](https://github.com/MariaDB/server/commit/e07f0a2d80) 2021-06-22 09:15:38 +0300 - Merge 10.2 into 10.3
* [Revision #6e94ef4185](https://github.com/MariaDB/server/commit/6e94ef4185)\
  2021-06-21 22:25:37 -0700
  * [MDEV-25679](https://jira.mariadb.org/browse/MDEV-25679) Wrong result selecting from simple view with LIMIT and ORDER BY
* [Revision #9dc50ea229](https://github.com/MariaDB/server/commit/9dc50ea229)\
  2021-06-21 18:13:28 +0300
  * [MDEV-25979](https://jira.mariadb.org/browse/MDEV-25979) Invalid page number written to DB\_ROLL\_PTR
* [Revision #e46f76c974](https://github.com/MariaDB/server/commit/e46f76c974)\
  2021-06-21 12:34:07 +0300
  * [MDEV-15912](https://jira.mariadb.org/browse/MDEV-15912): Remove traces of insert\_undo
* [Revision #241d30d3fa](https://github.com/MariaDB/server/commit/241d30d3fa)\
  2021-06-21 12:09:00 +0300
  * After-merge fixes for [MDEV-14180](https://jira.mariadb.org/browse/MDEV-14180)
* Merge [Revision #c9a85fb1b1](https://github.com/MariaDB/server/commit/c9a85fb1b1) 2021-06-21 09:07:40 +0300 - Merge 10.2 into 10.3
* [Revision #068246c006](https://github.com/MariaDB/server/commit/068246c006)\
  2021-06-19 00:45:49 +0200
  * fix spider tests for --ps
* [Revision #a5f6eca50d](https://github.com/MariaDB/server/commit/a5f6eca50d)\
  2021-06-19 00:22:15 +0200
  * spider tests aren't big

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
