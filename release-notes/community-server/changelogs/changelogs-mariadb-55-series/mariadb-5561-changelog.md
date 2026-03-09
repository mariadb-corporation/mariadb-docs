# MariaDB 5.5.61 Changelog

The most recent release in the [MariaDB 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.61)[Release Notes](../../old-releases/5.5/5.5.61.md)[Changelog](mariadb-5561-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 31 Jul 2018

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.61.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

*
  * \[
  * R
  * e
  * v
  * i
  * s
  * i
  * o
  * n
  *
  *
  * a
  * 4
  * 9
  * e
  * c
  * 9
  * 8
  * 0
  * 4
  * 2
  * ]
  * (
  * h
  * t
  * t
  * p
  * s
  * :
  * /
  * /
  * g
  * i
  * t
  * h
  * u
  * b
  * .
  * c
  * o
  * m
  * /
  * M
  * a
  * r
  * i
  * a
  * D
  * B
  * /
  * s
  * e
  * r
  * v
  * e
  * r
  * /
  * c
  * o
  * m
  * m
  * i
  * t
  * /
  * a
  * 4
  * 9
  * e
  * c
  * 9
  * 8
  * 0
  * 4
  * 2
  * )
  *
  * 2
  * 0
  * 1
  * 8
  *
    *
  * 0
  * 2
  *
    *
  * 1
  * 4
  *
  * 0
  * 9
  * :
  * 3
  * 5
  * :
  * 1
  * 8
  *
  *
    *
  * 0
  * 5
  * 3
  * 0
  *
* Merge [Revision #fceda2dab6](https://github.com/MariaDB/server/commit/fceda2dab6) 2018-07-29 13:10:29 +0200 - Merge remote-tracking branch 'mysql/5.5' into 5.5
* [Revision #bd0b368119](https://github.com/MariaDB/server/commit/bd0b368119)\
  2018-07-27 11:34:34 +0530
  * Fix added along with a test for a case missed in the patch for [MDEV-16751](https://jira.mariadb.org/browse/MDEV-16751)
* [Revision #37dee22d27](https://github.com/MariaDB/server/commit/37dee22d27)\
  2018-07-25 21:17:50 +0530
  * [MDEV-15454](https://jira.mariadb.org/browse/MDEV-15454): Nested SELECT IN returns wrong results
* [Revision #f9b43c2565](https://github.com/MariaDB/server/commit/f9b43c2565)\
  2018-07-25 14:20:16 +0530
  * [MDEV-16751](https://jira.mariadb.org/browse/MDEV-16751): Server crashes in st\_join\_table::cleanup or TABLE\_LIST::is\_with\_table\_recursive\_reference with join\_cache\_level>2
* [Revision #d567f1611e](https://github.com/MariaDB/server/commit/d567f1611e)\
  2018-07-24 20:00:28 -0700
  * [MDEV-16820](https://jira.mariadb.org/browse/MDEV-16820) Lost 'Impossible where' from query with inexpensive subquery
* [Revision #9cea4ccf12](https://github.com/MariaDB/server/commit/9cea4ccf12)\
  2018-07-19 15:31:30 -0700
  * [MDEV-16726](https://jira.mariadb.org/browse/MDEV-16726) Assertion \`tab->type == JT\_REF || tab->type == JT\_EQ\_REF' failed
* [Revision #8c45eb3ea5](https://github.com/MariaDB/server/commit/8c45eb3ea5)\
  2018-01-13 12:27:28 +1100
  * [MDEV-15050](https://jira.mariadb.org/browse/MDEV-15050) scripts: mysql\_install\_db.{sh|pl}, mysqld\_multi - mysqld is in @sbindir@
* [Revision #2fbf2277ff](https://github.com/MariaDB/server/commit/2fbf2277ff)\
  2018-07-11 10:43:38 +0300
  * [MDEV-15982](https://jira.mariadb.org/browse/MDEV-15982): Incorrect results when subquery is materialized
* [Revision #24a0a74f5d](https://github.com/MariaDB/server/commit/24a0a74f5d)\
  2018-07-10 13:54:04 +0530
  * [MDEV-16307](https://jira.mariadb.org/browse/MDEV-16307): Incorrect results when using BNLH join instead of BNL join with views
* [Revision #90cb721274](https://github.com/MariaDB/server/commit/90cb721274)\
  2018-06-29 22:46:38 -0700
  * [MDEV-16603](https://jira.mariadb.org/browse/MDEV-16603) Crash with set join\_cache\_level=4
* [Revision #9d41dd2f39](https://github.com/MariaDB/server/commit/9d41dd2f39)\
  2018-06-27 15:34:11 +0400
  * [MDEV-8540](https://jira.mariadb.org/browse/MDEV-8540) - Crash on server shutdown since 10.0.16
* [Revision #937c193188](https://github.com/MariaDB/server/commit/937c193188)\
  2018-06-27 13:17:18 +0300
  * Fixed [MDEV-16512](https://jira.mariadb.org/browse/MDEV-16512), crashing on re-execution of failing SP
* [Revision #faef2e6a44](https://github.com/MariaDB/server/commit/faef2e6a44)\
  2018-06-27 13:18:30 +0300
  * Added more help text in case mysql\_install\_db fails.
* [Revision #1f6a89a8fd](https://github.com/MariaDB/server/commit/1f6a89a8fd)\
  2018-06-27 13:18:03 +0300
  * Added valgrind suppression for OpenSuse 42.2
* [Revision #90e608c6ac](https://github.com/MariaDB/server/commit/90e608c6ac)\
  2018-06-26 11:42:02 +0400
  * A test cleanup for [MDEV-15834](https://jira.mariadb.org/browse/MDEV-15834): fixing failure in "mtr --embedded"
* [Revision #2b8f2b3e88](https://github.com/MariaDB/server/commit/2b8f2b3e88)\
  2018-06-20 23:30:49 +0200
  * Fix unit suite on Windows and in out-of-source builds
* [Revision #0a9d78f51d](https://github.com/MariaDB/server/commit/0a9d78f51d)\
  2018-06-20 23:27:23 +0200
  * Revert "[MDEV-16075](https://jira.mariadb.org/browse/MDEV-16075): Workaround to run MTR test suite for make test"
* [Revision #170b43c156](https://github.com/MariaDB/server/commit/170b43c156)\
  2018-06-20 16:36:46 +0400
  * [MDEV-16534](https://jira.mariadb.org/browse/MDEV-16534) PPC64: Unexpected error with a negative value into auto-increment columns in HEAP, MyISAM, ARIA
* [Revision #15b92915ed](https://github.com/MariaDB/server/commit/15b92915ed)\
  2018-06-19 13:02:02 +0400
  * [MDEV-15834](https://jira.mariadb.org/browse/MDEV-15834) The code in TABLE\_SHARE::init\_from\_binary\_frm\_image() is not safe
* [Revision #e425216045](https://github.com/MariaDB/server/commit/e425216045)\
  2018-01-31 09:35:38 +0100
  * [MDEV-15113](https://jira.mariadb.org/browse/MDEV-15113): Hang in Aria loghandler
* [Revision #147744d455](https://github.com/MariaDB/server/commit/147744d455)\
  2018-06-11 08:52:26 -0700
  * [MDEV-16235](https://jira.mariadb.org/browse/MDEV-16235) Server crashes in my\_utf8\_uni or in my\_strtod\_int upon SELECT .. LIMIT 0 (new variant)
* [Revision #ca733d03c8](https://github.com/MariaDB/server/commit/ca733d03c8)\
  2018-06-10 21:19:11 +0200
  * [MDEV-15729](https://jira.mariadb.org/browse/MDEV-15729) Server crashes in Field::make\_field upon HANDLER READ executed with PS protocol
* [Revision #6da8192174](https://github.com/MariaDB/server/commit/6da8192174)\
  2018-06-10 17:23:53 +0200
  * mysqltest: Allow HANDLER READ in --ps-protocol tests
* [Revision #e7ca377cb7](https://github.com/MariaDB/server/commit/e7ca377cb7)\
  2018-06-05 15:21:45 +0200
  * [MDEV-16342](https://jira.mariadb.org/browse/MDEV-16342) SHOW ENGINES: MyISAM description is useless
* [Revision #1d43f71c7b](https://github.com/MariaDB/server/commit/1d43f71c7b)\
  2018-06-10 11:19:39 +0300
  * [MDEV-15021](https://jira.mariadb.org/browse/MDEV-15021): mysqldump --tables --routines generates non importable dump file
* [Revision #953d70f960](https://github.com/MariaDB/server/commit/953d70f960)\
  2018-06-10 16:37:49 +0300
  * [MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Remove packed attr from omt\_ and subtree\_ classes
* [Revision #21246066b2](https://github.com/MariaDB/server/commit/21246066b2)\
  2018-06-10 15:54:57 +0300
  * Make TokuDB compile with GCC-8
* [Revision #7fca4b50ff](https://github.com/MariaDB/server/commit/7fca4b50ff)\
  2018-06-10 15:20:43 +0300
  * Revert "[MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Remove packed attr from omt\_ and subtree\_ classes"
* [Revision #d39629f01e](https://github.com/MariaDB/server/commit/d39629f01e)\
  2018-05-07 22:40:27 +0300
  * [MDEV-16075](https://jira.mariadb.org/browse/MDEV-16075): Workaround to run MTR test suite for make test
* [Revision #0e6d6354bf](https://github.com/MariaDB/server/commit/0e6d6354bf)\
  2018-05-15 10:25:47 +0300
  * Also ignore macOS .DS\_Store Finder junk.
* [Revision #814a284f22](https://github.com/MariaDB/server/commit/814a284f22)\
  2018-04-12 13:33:39 +0300
  * Ignore .cbp QtCreator && CodeBlocks project files
* [Revision #1735fa340a](https://github.com/MariaDB/server/commit/1735fa340a)\
  2018-05-09 16:54:16 +0300
  * [MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Remove packed attr from omt\_ and subtree\_ classes
* [Revision #b8e267c0c5](https://github.com/MariaDB/server/commit/b8e267c0c5)\
  2018-05-09 15:14:57 +0300
  * [MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Manually backport TokuDB macOS fixes from 10.0
* [Revision #d9b159a202](https://github.com/MariaDB/server/commit/d9b159a202)\
  2018-04-17 15:00:15 -0400
  * [MDEV-15789](https://jira.mariadb.org/browse/MDEV-15789) - mysqlslap use incorrect table def
* [Revision #75b4eb5cc9](https://github.com/MariaDB/server/commit/75b4eb5cc9)\
  2018-06-06 15:27:57 +0200
  * Catch of OOM situation.
* [Revision #72b6d01848](https://github.com/MariaDB/server/commit/72b6d01848)\
  2018-06-05 22:13:19 +0100
  * [MDEV-10246](https://jira.mariadb.org/browse/MDEV-10246) ssl-\* config file options have no effect without mysql\_ssl\_set()
* [Revision #5fb2c586f2](https://github.com/MariaDB/server/commit/5fb2c586f2)\
  2018-06-02 11:52:48 +0530
  * [MDEV-16225](https://jira.mariadb.org/browse/MDEV-16225): wrong resultset from query with semijoin=on
* [Revision #1ada4afb0a](https://github.com/MariaDB/server/commit/1ada4afb0a)\
  2018-04-29 19:47:48 +0300
  * mtr: use process launch -- args to start mysqld in lldb
* [Revision #6a04c2a1aa](https://github.com/MariaDB/server/commit/6a04c2a1aa)\
  2018-05-22 12:09:05 -0700
  * [MDEV-16235](https://jira.mariadb.org/browse/MDEV-16235) Server crashes in my\_utf8\_uni or in my\_strtod\_int upon SELECT .. LIMIT 0
* [Revision #27a7365f42](https://github.com/MariaDB/server/commit/27a7365f42)\
  2018-05-18 00:23:15 +0100
  * [MDEV-16220](https://jira.mariadb.org/browse/MDEV-16220) MTR - do not pass UTF8 on the command line for mysql client.
* [Revision #1b2078b4d8](https://github.com/MariaDB/server/commit/1b2078b4d8)\
  2018-05-15 17:34:47 +0200
  * [MDEV-15318](https://jira.mariadb.org/browse/MDEV-15318) CREATE .. SELECT VALUES produces invalid table structure
* [Revision #aa2e1ade17](https://github.com/MariaDB/server/commit/aa2e1ade17)\
  2018-05-16 21:01:26 +0400
  * (almost) sane core handling in mtr
* [Revision #2b749a7bf4](https://github.com/MariaDB/server/commit/2b749a7bf4)\
  2018-05-15 11:46:55 +0300
  * [MDEV-654](https://jira.mariadb.org/browse/MDEV-654) Assertion \`share->now\_transactional' failed in flush\_log\_for\_bitmap on concurrent workload with Aria tables
* [Revision #318097bb8f](https://github.com/MariaDB/server/commit/318097bb8f)\
  2018-05-10 19:00:54 +0400
  * [MDEV-15480](https://jira.mariadb.org/browse/MDEV-15480) Audit plugin does not respect QUERY\_DML for audit plugin.
* [Revision #1d58d184c2](https://github.com/MariaDB/server/commit/1d58d184c2)\
  2018-05-04 00:09:45 +0200
  * protocol: verify that number of rows is correct
* [Revision #fab383aac0](https://github.com/MariaDB/server/commit/fab383aac0)\
  2018-04-30 23:06:09 +0200
  * Use after free in authentication
* [Revision #a52c46e069](https://github.com/MariaDB/server/commit/a52c46e069)\
  2018-04-30 13:50:59 +0200
  * Bug#25471090: MYSQL USE AFTER FREE
* [Revision #5cfe52314e](https://github.com/MariaDB/server/commit/5cfe52314e)\
  2018-04-27 11:21:55 +0200
  * Bug#25471090: MYSQL USE AFTER FREE
* [Revision #eb057dce20](https://github.com/MariaDB/server/commit/eb057dce20)\
  2018-04-24 15:51:49 -0700
  * [MDEV-15035](https://jira.mariadb.org/browse/MDEV-15035) Wrong results when calling a stored procedure multiple times with different arguments.
* [Revision #adaa891ae7](https://github.com/MariaDB/server/commit/adaa891ae7)\
  2018-04-12 14:55:43 +0200
  * [MDEV-13699](https://jira.mariadb.org/browse/MDEV-13699): Assertion \`!new\_field->field\_name.str || strlen(new\_field->field\_name.str) == new\_field->field\_name.length' failed in create\_tmp\_table on 2nd execution of PS with semijoin
* [Revision #7f6561225a](https://github.com/MariaDB/server/commit/7f6561225a)\
  2018-04-23 12:25:03 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
