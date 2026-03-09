# MariaDB 10.3.26 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download 10.3.26](https://downloads.mariadb.org/mariadb/10.3.26/)[Release Notes](../../old-releases/10.3/10.3.26.md)[Changelog](mariadb-10326-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 3 Nov 2020

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.26.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.35](../changelogs-mariadb-102-series/mariadb-10235-changelog.md)
* [Revision #d5ce782444](https://github.com/MariaDB/server/commit/d5ce782444)\
  2020-11-01 02:56:29 +0200
  * List of unstable tests for 10.3.26 release
* Merge [Revision #794f665139](https://github.com/MariaDB/server/commit/794f665139) 2020-10-30 17:23:53 +0100 - Merge branch '10.2' into 10.3
* [Revision #14d43f4fa6](https://github.com/MariaDB/server/commit/14d43f4fa6)\
  2020-10-29 18:34:26 +0200
  * [MDEV-23222](https://jira.mariadb.org/browse/MDEV-23222) SIGSEG in maria\_create() because of double free
* [Revision #4c99e3e948](https://github.com/MariaDB/server/commit/4c99e3e948)\
  2020-10-29 17:36:49 +0200
  * Fixed bug in detection of getgrouplist parameters.
* [Revision #14798d3cd1](https://github.com/MariaDB/server/commit/14798d3cd1)\
  2020-10-29 16:20:57 +0200
  * [MDEV-23159](https://jira.mariadb.org/browse/MDEV-23159) Assertion \`table\_share->tmp\_table != NO\_TMP\_TABLE || m\_lock\_type != 2'...
* [Revision #1e778a3b56](https://github.com/MariaDB/server/commit/1e778a3b56)\
  2020-10-29 08:02:33 +0200
  * [MDEV-21201](https://jira.mariadb.org/browse/MDEV-21201) fixup: GCC 10.2.0 -Wparentheses
* [Revision #dee6902922](https://github.com/MariaDB/server/commit/dee6902922)\
  2020-10-28 18:48:14 +0200
  * After-merge fix: sys\_vars.sysvars\_innodb,32bit
* Merge [Revision #2b6f804490](https://github.com/MariaDB/server/commit/2b6f804490) 2020-10-28 10:44:40 +0200 - Merge 10.2 into 10.3
* Merge [Revision #a8de8f261d](https://github.com/MariaDB/server/commit/a8de8f261d) 2020-10-28 10:01:50 +0200 - Merge 10.2 into 10.3
* [Revision #e183aec1d7](https://github.com/MariaDB/server/commit/e183aec1d7)\
  2020-10-27 12:16:53 +0100
  * [MDEV-24018](https://jira.mariadb.org/browse/MDEV-24018): SIGSEGV in Item\_func\_nextval::update\_table on SELECT SETVAL
* [Revision #e64084d5a3](https://github.com/MariaDB/server/commit/e64084d5a3)\
  2020-08-01 13:12:50 +0200
  * [MDEV-21201](https://jira.mariadb.org/browse/MDEV-21201) No records produced in information\_schema query, depending on projection
* [Revision #6cefe7d31e](https://github.com/MariaDB/server/commit/6cefe7d31e)\
  2020-08-02 10:30:46 +0200
  * cleanup: use predefined CMAKE\_DL\_LIBS
* [Revision #641f81baf4](https://github.com/MariaDB/server/commit/641f81baf4)\
  2020-08-01 13:19:59 +0200
  * cleanup: use my\_multi\_malloc(), etc
* [Revision #5a9484b784](https://github.com/MariaDB/server/commit/5a9484b784)\
  2020-10-22 14:00:17 +0400
  * [MDEV-19443](https://jira.mariadb.org/browse/MDEV-19443) server\_audit plugin doesn't log proxy users.
* [Revision #81870e499f](https://github.com/MariaDB/server/commit/81870e499f)\
  2020-08-31 16:36:32 +0200
  * [MDEV-21786](https://jira.mariadb.org/browse/MDEV-21786) mysqldump will forget sequence definition details on --no-data dump
* Merge [Revision #e3d692aa09](https://github.com/MariaDB/server/commit/e3d692aa09) 2020-10-22 08:26:28 +0300 - Merge 10.2 into 10.3
* [Revision #88d22f0e65](https://github.com/MariaDB/server/commit/88d22f0e65)\
  2020-04-16 00:44:20 +0900
  * [MDEV-20100](https://jira.mariadb.org/browse/MDEV-20100) [MariaDB 10.3.9](../../old-releases/10.3/10.3.9.md) Crash "\[ERROR] mysqld got signal 11 ;"
* [Revision #9b46d8e5c4](https://github.com/MariaDB/server/commit/9b46d8e5c4)\
  2020-10-20 10:49:54 +0300
  * [MDEV-23968](https://jira.mariadb.org/browse/MDEV-23968) CREATE TEMPORARY TABLE .. LIKE (system versioned table) returns error if unique index is defined in the table
* [Revision #ddea8f6a39](https://github.com/MariaDB/server/commit/ddea8f6a39)\
  2020-10-20 10:49:54 +0300
  * [MDEV-23779](https://jira.mariadb.org/browse/MDEV-23779) Error upon querying the view, that selecting from versioned table with partitions
* [Revision #a3c379ea61](https://github.com/MariaDB/server/commit/a3c379ea61)\
  2020-10-20 10:49:54 +0300
  * [MDEV-23799](https://jira.mariadb.org/browse/MDEV-23799) CREATE .. SELECT wrong result on join versioned table
* [Revision #7b7ea33124](https://github.com/MariaDB/server/commit/7b7ea33124)\
  2020-10-15 13:26:18 +0530
  * [MDEV-23072](https://jira.mariadb.org/browse/MDEV-23072) Diskspace not reused for Blob in data file
* [Revision #00bf48827f](https://github.com/MariaDB/server/commit/00bf48827f)\
  2020-10-08 23:05:35 +0530
  * [MDEV-23445](https://jira.mariadb.org/browse/MDEV-23445): LIMIT ROWS EXAMINED throws error in Debug build only
* [Revision #311b7f94e6](https://github.com/MariaDB/server/commit/311b7f94e6)\
  2020-10-16 15:36:12 +0300
  * [MDEV-23248](https://jira.mariadb.org/browse/MDEV-23248) Server crashes in mi\_extra / ha\_partition::loop\_extra\_alter upon REORGANIZE
* Merge [Revision #469a249a5b](https://github.com/MariaDB/server/commit/469a249a5b) 2020-10-07 18:42:26 +0200 - Merge tag 'mariadb-10.3.25' into 10.3
* [Revision #89fc49321a](https://github.com/MariaDB/server/commit/89fc49321a)\
  2020-10-07 11:25:40 -0400
  * bump the VERSION
* Merge [Revision #d99f787244](https://github.com/MariaDB/server/commit/d99f787244) 2020-10-01 13:33:51 +0300 - Merge 10.2 into 10.3
* Merge [Revision #323500bfa9](https://github.com/MariaDB/server/commit/323500bfa9) 2020-09-30 16:25:06 +0300 - Merge 10.2 into 10.3
* Merge [Revision #6cbbd6bd96](https://github.com/MariaDB/server/commit/6cbbd6bd96) 2020-09-28 17:27:42 +0530 - Merge branch '10.2' into 10.3
* [Revision #a6987d9fb9](https://github.com/MariaDB/server/commit/a6987d9fb9)\
  2020-09-28 09:49:46 +0200
  * [MDEV-23823](https://jira.mariadb.org/browse/MDEV-23823) Crash in SELECT NEXT VALUE on locked view
* Merge [Revision #d9d9c30b70](https://github.com/MariaDB/server/commit/d9d9c30b70) 2020-09-22 21:12:48 +0300 - Merge 10.2 into 10.3
* Merge [Revision #fde3d895d9](https://github.com/MariaDB/server/commit/fde3d895d9) 2020-09-22 14:33:03 +0300 - Merge 10.2 into 10.3
* Merge [Revision #2cf489d430](https://github.com/MariaDB/server/commit/2cf489d430) 2020-09-21 16:39:23 +0300 - Merge 10.2 into 10.3
* [Revision #fba6ffe433](https://github.com/MariaDB/server/commit/fba6ffe433)\
  2020-09-21 12:10:27 +0300
  * [MDEV-23741](https://jira.mariadb.org/browse/MDEV-23741): Fix the result
* Merge [Revision #cbcb4ecabb](https://github.com/MariaDB/server/commit/cbcb4ecabb) 2020-09-21 11:04:04 +0300 - Merge 10.2 into 10.3
* [Revision #ade782c001](https://github.com/MariaDB/server/commit/ade782c001)\
  2020-09-17 22:27:45 +0200
  * [MDEV-23741](https://jira.mariadb.org/browse/MDEV-23741) Windows : error when renaming file in ALTER TABLE
* Merge [Revision #7e07e38cf6](https://github.com/MariaDB/server/commit/7e07e38cf6) 2020-09-09 13:06:46 +0300 - Merge 10.2 into 10.3
* [Revision #e976f461d8](https://github.com/MariaDB/server/commit/e976f461d8)\
  2020-09-04 22:10:57 +0900
  * [MDEV-7098](https://jira.mariadb.org/browse/MDEV-7098) spider/bg.spider\_fixes failed in buildbot with safe\_mutex: Trying to unlock mutex conn->mta\_conn\_mutex that wasn't locked at storage/spider/spd\_db\_conn.cc, line 671
* Merge [Revision #c5cb59ce77](https://github.com/MariaDB/server/commit/c5cb59ce77) 2020-09-04 12:31:58 +0300 - Merge 10.2 into 10.3
* [Revision #1a3ce7e77c](https://github.com/MariaDB/server/commit/1a3ce7e77c)\
  2020-09-04 12:17:35 +0300
  * [MDEV-23651](https://jira.mariadb.org/browse/MDEV-23651): Fix the Windows build
* [Revision #a7dd7c8993](https://github.com/MariaDB/server/commit/a7dd7c8993)\
  2020-09-03 14:49:11 +0300
  * [MDEV-23651](https://jira.mariadb.org/browse/MDEV-23651) InnoDB: Failing assertion: !space->referenced()
* [Revision #33ae1616e0](https://github.com/MariaDB/server/commit/33ae1616e0)\
  2020-09-03 14:10:42 +0300
  * [MDEV-21578](https://jira.mariadb.org/browse/MDEV-21578) : CREATE OR REPLACE TRIGGER in Galera cluster not replicating
* Merge [Revision #c3752cef3c](https://github.com/MariaDB/server/commit/c3752cef3c) 2020-09-03 09:26:54 +0300 - Merge 10.2 into 10.3
* [Revision #56ae0adee3](https://github.com/MariaDB/server/commit/56ae0adee3)\
  2020-09-02 11:23:18 +1000
  * travis: update osx to xcode12u in attempt to solve openssl build failure
* [Revision #594aad7b06](https://github.com/MariaDB/server/commit/594aad7b06)\
  2020-09-01 21:12:01 +1000
  * travis: osx build time out storing cache. Ensure not Cellar
* [Revision #caa35f8e25](https://github.com/MariaDB/server/commit/caa35f8e25)\
  2020-08-11 21:45:09 +0300
  * [MDEV-16372](https://jira.mariadb.org/browse/MDEV-16372) ER\_BASE64\_DECODE\_ERROR upon replaying binary log via mysqlbinlog --verbose
* Merge [Revision #6a042281bd](https://github.com/MariaDB/server/commit/6a042281bd) 2020-08-26 10:45:47 +0300 - Merge 10.2 into 10.3
* [Revision #65f30050aa](https://github.com/MariaDB/server/commit/65f30050aa)\
  2020-08-24 17:22:21 +0530
  * [MDEV-18335](https://jira.mariadb.org/browse/MDEV-18335): Assertion \`!error || error == 137' failed in subselect\_rowid\_merge\_engine::init
* [Revision #95831888e8](https://github.com/MariaDB/server/commit/95831888e8)\
  2020-08-25 22:21:08 +0300
  * part\_records() signature fix
* [Revision #6586bb51f3](https://github.com/MariaDB/server/commit/6586bb51f3)\
  2020-08-25 22:21:07 +0300
  * [MDEV-23467](https://jira.mariadb.org/browse/MDEV-23467) SIGSEGV in fill\_record/fill\_record\_n\_invoke\_before\_triggers on INSERT DELAYED
* Merge [Revision #c277bcd591](https://github.com/MariaDB/server/commit/c277bcd591) 2020-08-21 19:18:34 +0300 - Merge 10.2 into 10.3
* Merge [Revision #9be0b61407](https://github.com/MariaDB/server/commit/9be0b61407) 2020-08-21 10:17:22 +0300 - Merge 10.2 into 10.3
* Merge [Revision #de0e7cd72a](https://github.com/MariaDB/server/commit/de0e7cd72a) 2020-08-20 09:12:16 +0300 - Merge 10.2 into 10.3
* [Revision #90c8d773ed](https://github.com/MariaDB/server/commit/90c8d773ed)\
  2020-08-04 10:13:35 +0300
  * [MDEV-21251](https://jira.mariadb.org/browse/MDEV-21251) CHECK TABLE fails to check info\_bits of records
* [Revision #b811c6ecc7](https://github.com/MariaDB/server/commit/b811c6ecc7)\
  2020-08-13 18:21:30 +0300
  * Fix GCC 10.2.0 -Og -Wmaybe-uninitialized
* Merge [Revision #4bd56a697f](https://github.com/MariaDB/server/commit/4bd56a697f) 2020-08-13 18:18:25 +0300 - Merge 10.2 into 10.3
* [Revision #863e28ff3e](https://github.com/MariaDB/server/commit/863e28ff3e)\
  2020-08-07 17:03:17 +0200
  * [MDEV-22066](https://jira.mariadb.org/browse/MDEV-22066): out-of-source build fails with WITHOUT\_SERVER=ON
* [Revision #e0c06f5396](https://github.com/MariaDB/server/commit/e0c06f5396)\
  2020-08-11 09:08:05 +0300
  * Work around [MDEV-23445](https://jira.mariadb.org/browse/MDEV-23445) in the [MDEV-14836](https://jira.mariadb.org/browse/MDEV-14836) test case
* Merge [Revision #bafc5c1321](https://github.com/MariaDB/server/commit/bafc5c1321) 2020-08-10 18:40:57 +0300 - Merge 10.2 into 10.3
* Merge [Revision #0025eb3f96](https://github.com/MariaDB/server/commit/0025eb3f96) 2020-08-10 17:56:08 +0300 - Merge mariadb-10.3.24
* [Revision #c19335ea53](https://github.com/MariaDB/server/commit/c19335ea53)\
  2020-08-10 10:26:37 -0400
  * bump the VERSION
* [Revision #d496765903](https://github.com/MariaDB/server/commit/d496765903)\
  2020-08-04 09:49:44 +0400
  * [MDEV-22022](https://jira.mariadb.org/browse/MDEV-22022) Various mangled SQL statements will crash 10.3 to 10.5 debug builds
* [Revision #b3e9798ff3](https://github.com/MariaDB/server/commit/b3e9798ff3)\
  2020-08-03 13:35:53 +0200
  * Fix named\_pipe test so it can be used with --repeat
* [Revision #ccb9f673b4](https://github.com/MariaDB/server/commit/ccb9f673b4)\
  2020-08-03 13:23:38 +0200
  * [MDEV-23348](https://jira.mariadb.org/browse/MDEV-23348) vio\_shutdown does not prevent later ReadFile on named pipe

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
