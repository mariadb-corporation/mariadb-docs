# MariaDB 5.5.50 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.50)[Release Notes](../../old-releases/5.5/5.5.50.md)[Changelog](mariadb-5550-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 17 Jun 2016

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.50.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #12ae840](https://github.com/MariaDB/server/commit/12ae840)\
  2016-06-16 22:04:24 +0300
  * Fix typo bug that cause myisam repair to fail
* [Revision #c7eef02](https://github.com/MariaDB/server/commit/c7eef02)\
  2016-06-16 22:00:16 +0300
  * Increase the number of default build thread ids possibilities
* [Revision #7ab7abd](https://github.com/MariaDB/server/commit/7ab7abd)\
  2016-06-16 18:52:46 +0300
  * Fix compilation failure when compiling with std=c90
* [Revision #b644661](https://github.com/MariaDB/server/commit/b644661)\
  2016-06-14 22:29:24 +0200
  * [MDEV-9256](https://jira.mariadb.org/browse/MDEV-9256) : Crashes on Windows x64 with aria\_pagecache\_buffer\_size > 4GB
* [Revision #34a104b](https://github.com/MariaDB/server/commit/34a104b)\
  2016-06-14 12:28:05 +0300
  * [MDEV-10229](https://jira.mariadb.org/browse/MDEV-10229): TokuDB fails to build with CLang
* [Revision #1bf2509](https://github.com/MariaDB/server/commit/1bf2509)\
  2016-06-13 23:32:50 +0300
  * [MDEV-10162](https://jira.mariadb.org/browse/MDEV-10162): Update repair testcase
* [Revision #2b47832](https://github.com/MariaDB/server/commit/2b47832)\
  2015-12-10 03:56:31 +0200
  * Fixed compilation failure using clang
* [Revision #6a34ba3](https://github.com/MariaDB/server/commit/6a34ba3)\
  2016-02-16 16:15:22 +0200
  * \[Code cleanup] Refactor duplicate code within myisam and maria sort.cc
* [Revision #bfef17b](https://github.com/MariaDB/server/commit/bfef17b)\
  2016-06-13 18:30:02 +0300
  * [MDEV-9433](https://jira.mariadb.org/browse/MDEV-9433): \[PATCH} cppcheck reported a number of minor coding errors
* [Revision #0089af8](https://github.com/MariaDB/server/commit/0089af8)\
  2016-06-13 18:11:31 +0300
  * [MDEV-9433](https://jira.mariadb.org/browse/MDEV-9433): \[PATCH] cppcheck reported a number of minor coding errors
* [Revision #cf721d2](https://github.com/MariaDB/server/commit/cf721d2)\
  2015-12-10 17:00:14 +1100
  * [MDEV-9257](https://jira.mariadb.org/browse/MDEV-9257): Increase limit on parallel workers in mysql-test-run
* [Revision #05bb3b9](https://github.com/MariaDB/server/commit/05bb3b9)\
  2016-06-14 16:28:07 +0200
  * fix main.ssl\_ca test for windows
* [Revision #a4cfd32](https://github.com/MariaDB/server/commit/a4cfd32)\
  2016-06-14 14:52:43 +0200
  * main.openssl\_1 failure
* [Revision #c73b987](https://github.com/MariaDB/server/commit/c73b987)\
  2016-06-14 13:18:05 +0200
  * [MDEV-8328](https://jira.mariadb.org/browse/MDEV-8328) Evaluation of two "!" operators depends on space in beetween
* [Revision #c3c272c](https://github.com/MariaDB/server/commit/c3c272c)\
  2016-06-10 13:47:00 +0200
  * [MDEV-10166](https://jira.mariadb.org/browse/MDEV-10166) probes\_mysql\_nodtrace.h is not provided anymore by mariadb-10.0.25
* [Revision #260699e](https://github.com/MariaDB/server/commit/260699e) 2016-06-14 13:59:41 +0200 - Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #f54dcf1](https://github.com/MariaDB/server/commit/f54dcf1)\
  2016-06-14 12:38:47 +0200
  * 5.5.49-37.9
* [Revision #90eb302](https://github.com/MariaDB/server/commit/90eb302)\
  2016-06-14 13:57:49 +0200
  * fix main.ssl\_ca from mysql-5.5.50
* [Revision #ae29ea2](https://github.com/MariaDB/server/commit/ae29ea2) 2016-06-14 13:55:28 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #1b50d59](https://github.com/MariaDB/server/commit/1b50d59)\
  2016-06-14 14:44:09 +0400
  * [MDEV-9945](https://jira.mariadb.org/browse/MDEV-9945) - main.kill\_processlist-6619 fails sporadically
* [Revision #d6a1bae](https://github.com/MariaDB/server/commit/d6a1bae)\
  2016-06-13 17:10:31 +0400
  * [MDEV-10218](https://jira.mariadb.org/browse/MDEV-10218) - rpl.rpl\_binlog\_errors fails in buildbot with valgrind warnings - bytes are possibly lost
* [Revision #2db724c](https://github.com/MariaDB/server/commit/2db724c)\
  2016-06-13 15:54:12 +0400
  * [MDEV-10218](https://jira.mariadb.org/browse/MDEV-10218) - rpl.rpl\_binlog\_errors fails in buildbot with valgrind warnings - bytes are possibly lost
* [Revision #3c77a00](https://github.com/MariaDB/server/commit/3c77a00)\
  2016-03-08 13:27:18 +0200
  * [MDEV-8012](https://jira.mariadb.org/browse/MDEV-8012): Wrong exit code when asking for help
* [Revision #416006a](https://github.com/MariaDB/server/commit/416006a)\
  2016-06-12 22:45:15 +0300
  * [MDEV-8012](https://jira.mariadb.org/browse/MDEV-8012): Wrong exit code when asking for help
* [Revision #67b4a6f](https://github.com/MariaDB/server/commit/67b4a6f)\
  2016-06-12 20:14:51 +0300
  * [MDEV-8859](https://jira.mariadb.org/browse/MDEV-8859) rpl.rpl\_mdev382 sporadically fails to finish due to disappeared expect file
* [Revision #87007dc](https://github.com/MariaDB/server/commit/87007dc)\
  2016-06-08 15:03:18 +0400
  * [MDEV-9994](https://jira.mariadb.org/browse/MDEV-9994) - Aria service threads are not "joined"
* [Revision #4155d09](https://github.com/MariaDB/server/commit/4155d09)\
  2016-06-10 17:06:38 +0400
  * [MDEV-8402](https://jira.mariadb.org/browse/MDEV-8402) Bug #77473 Truncated data with subquery & UTF8
* [Revision #df14488](https://github.com/MariaDB/server/commit/df14488)\
  2016-06-10 15:50:19 +0400
  * [MDEV-10181](https://jira.mariadb.org/browse/MDEV-10181) Illegal mix of collation for a field and an ASCII string as a view field
* [Revision #7adf04e](https://github.com/MariaDB/server/commit/7adf04e)\
  2016-01-05 22:48:50 +0100
  * [MDEV-9366](https://jira.mariadb.org/browse/MDEV-9366) : do\_shutdown\_server fails to detect server shutdown on Windows. Fix test whether process is alive in mysqltest.
* [Revision #a4848e9](https://github.com/MariaDB/server/commit/a4848e9)\
  2016-06-08 19:04:12 +0400
  * [MDEV-9972](https://jira.mariadb.org/browse/MDEV-9972) Least function retuns date in date time format
* [Revision #b31976f](https://github.com/MariaDB/server/commit/b31976f) 2016-06-08 15:15:55 +0200 - Merge branch 'mdev9991' into mdev9991-5.5
* [Revision #196d96c](https://github.com/MariaDB/server/commit/196d96c)\
  2016-06-08 15:12:44 +0200
  * Fix compiler check for stack unwind hint
* [Revision #0f25270](https://github.com/MariaDB/server/commit/0f25270)\
  2016-06-08 08:40:10 +0300
  * [MDEV-7139](https://jira.mariadb.org/browse/MDEV-7139): Sporadic failure in innodb.innodb\_corrupt\_bit on P8
* [Revision #ff832e0](https://github.com/MariaDB/server/commit/ff832e0)\
  2016-05-24 17:37:23 +0200
  * Restore COMPONENT Embedded for Windows embedded libs.
* [Revision #221adbc](https://github.com/MariaDB/server/commit/221adbc)\
  2016-05-24 17:01:08 +0200
  * Fix warnings on Windows, compiler option -ggdb3 option is nonexistent
* [Revision #535160b](https://github.com/MariaDB/server/commit/535160b)\
  2016-05-24 16:57:03 +0200
  * [MDEV-10117](https://jira.mariadb.org/browse/MDEV-10117) - update HeidiSQL to current version
* [Revision #9eb0fbd](https://github.com/MariaDB/server/commit/9eb0fbd)\
  2016-05-24 14:20:53 +0200
  * [MDEV-10071](https://jira.mariadb.org/browse/MDEV-10071) Block installation on XP/Windows 2003 Server(they are no more supported)
* [Revision #18487ed](https://github.com/MariaDB/server/commit/18487ed)\
  2016-05-24 14:18:55 +0200
  * [MDEV-10108](https://jira.mariadb.org/browse/MDEV-10108) Fix errors in installations by domain user
* [Revision #964c4f0](https://github.com/MariaDB/server/commit/964c4f0)\
  2016-05-10 19:13:06 +0400
  * [MDEV-10052](https://jira.mariadb.org/browse/MDEV-10052) Illegal mix of collations with DAYNAME(date\_field)<>varchar\_field
* [Revision #672bbcd](https://github.com/MariaDB/server/commit/672bbcd)\
  2016-04-27 16:13:14 +0200
  * [MDEV-9973](https://jira.mariadb.org/browse/MDEV-9973) : Do not set permissions for serviceaccount user (Win7 and later) This appears to break some installation, and it did not do anything useful anyway.
* [Revision #4f1ad43](https://github.com/MariaDB/server/commit/4f1ad43)\
  2016-04-26 16:15:15 +0400
  * [MDEV-9987](https://jira.mariadb.org/browse/MDEV-9987) - gen\_lex\_hash leaks memory, making LeakSanitizer builds fail
* [Revision #29868de](https://github.com/MariaDB/server/commit/29868de)\
  2016-04-26 12:58:14 +0200
  * [MDEV-9986](https://jira.mariadb.org/browse/MDEV-9986) Full-text search of the utf8mb4 column causes crash
* [Revision #7f5ceb7](https://github.com/MariaDB/server/commit/7f5ceb7)\
  2016-04-26 11:49:35 +0200
  * disable main.wait\_timeout\_not\_windows for embedded
* [Revision #2220480](https://github.com/MariaDB/server/commit/2220480)\
  2016-04-25 18:59:41 +0200
  * [MDEV-7775](https://jira.mariadb.org/browse/MDEV-7775) Wrong error message (Unknown error) when idle sessions are killed after wait\_timeout
* [Revision #a98ecc2](https://github.com/MariaDB/server/commit/a98ecc2)\
  2016-04-23 12:19:40 +0200
  * support SEARCH\_RANGE in search\_pattern\_in\_file.inc
* [Revision #2b7573e](https://github.com/MariaDB/server/commit/2b7573e)\
  2016-04-24 13:36:51 +0400
  * [MDEV-9975](https://jira.mariadb.org/browse/MDEV-9975) - main.partition\_innodb\_plugin fails sporadically
* [Revision #19e3597](https://github.com/MariaDB/server/commit/19e3597)\
  2016-04-07 10:47:46 +0300
  * [MDEV-9142](https://jira.mariadb.org/browse/MDEV-9142) :Adding Constraint with no database reference results in ERROR 1046 (3D000) at line 13: No database selected.
* [Revision #0ea4c73](https://github.com/MariaDB/server/commit/0ea4c73)\
  2016-04-23 12:15:18 +0400
  * Fixed compilation failure due to unused var.
* [Revision #618e300](https://github.com/MariaDB/server/commit/618e300)\
  2016-04-22 12:57:39 +0400
  * [MDEV-9970](https://jira.mariadb.org/browse/MDEV-9970) - main.sp-threads fails sporadically
* [Revision #bd75ee7](https://github.com/MariaDB/server/commit/bd75ee7)\
  2016-04-22 09:10:00 -0400
  * bump the VERSION
* [Revision #3f0d07e](https://github.com/MariaDB/server/commit/3f0d07e)\
  2016-04-22 16:04:20 +0400
  * [MDEV-9372](https://jira.mariadb.org/browse/MDEV-9372) select 100 between 1 and 9223372036854775808 returns false

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
