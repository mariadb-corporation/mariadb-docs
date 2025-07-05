# MariaDB 10.0.33 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.33)[Release Notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10033-release-notes.md)[Changelog](mariadb-10033-changelog.md)[Overview of 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)

**Release date:** 30 Oct 2017

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10033-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #c3592ca7b8](https://github.com/MariaDB/server/commit/c3592ca7b8)\
  2017-10-27 03:19:59 +0300
  * List of unstable tests for 10.0.33 release
* [Revision #eadcf09bc4](https://github.com/MariaDB/server/commit/eadcf09bc4)\
  2017-10-27 03:17:23 +0300
  * [MDEV-13860](https://jira.mariadb.org/browse/MDEV-13860) CONNECT engine does not build with JDBC without ODBC
* [Revision #b933a8c354](https://github.com/MariaDB/server/commit/b933a8c354)\
  2017-10-26 13:29:28 +0300
  * [MDEV-12569](https://jira.mariadb.org/browse/MDEV-12569) InnoDB suggests filing bugs at MySQL bug tracker
* [Revision #c9ee5d9960](https://github.com/MariaDB/server/commit/c9ee5d9960)\
  2017-10-25 23:40:54 +0300
  * Squashed commit of the following:
* Merge [Revision #bd9a2363e5](https://github.com/MariaDB/server/commit/bd9a2363e5) 2017-10-26 12:47:24 +0300 - Merge branch 'merge-perfschema-5.6' into 10.0
* [Revision #98470fc800](https://github.com/MariaDB/server/commit/98470fc800)\
  2017-10-25 22:04:17 +0300
  * 5.6.38
* Merge [Revision #3b35d745c3](https://github.com/MariaDB/server/commit/3b35d745c3) 2017-10-26 12:46:47 +0300 - Merge branch 'merge-innodb-5.6' into 10.0
* [Revision #4ef64e01a7](https://github.com/MariaDB/server/commit/4ef64e01a7)\
  2017-10-25 21:35:33 +0300
  * 5.6.38
* Merge [Revision #4274d0bf57](https://github.com/MariaDB/server/commit/4274d0bf57) 2017-10-26 11:13:07 +0300 - Merge 5.5 into 10.0
* [Revision #cfb3361748](https://github.com/MariaDB/server/commit/cfb3361748)\
  2017-10-26 11:02:19 +0300
  * [MDEV-12569](https://jira.mariadb.org/browse/MDEV-12569) InnoDB suggests filing bugs at MySQL bug tracker
* [Revision #fc7b9af267](https://github.com/MariaDB/server/commit/fc7b9af267)\
  2017-10-25 16:21:52 +0300
  * Remove comments to removed parameters
* Merge [Revision #44ed243522](https://github.com/MariaDB/server/commit/44ed243522) 2017-10-24 19:25:19 +0300 - Merge 5.5 into 10.0
* [Revision #439a7c994a](https://github.com/MariaDB/server/commit/439a7c994a)\
  2017-10-24 15:20:54 +0300
  * [MDEV-14051](https://jira.mariadb.org/browse/MDEV-14051) 'Undo log record is too big.' error occurring in very narrow range of string lengths
* [Revision #fb5fe497e5](https://github.com/MariaDB/server/commit/fb5fe497e5)\
  2017-10-18 02:36:55 -0400
  * bump the VERSION
* [Revision #a1a79aa576](https://github.com/MariaDB/server/commit/a1a79aa576)\
  2017-10-23 15:35:10 -0700
  * [MDEV-13776](https://jira.mariadb.org/browse/MDEV-13776) mysqld got signal 11 on delete returning
* [Revision #acb336f75e](https://github.com/MariaDB/server/commit/acb336f75e)\
  2017-10-23 15:33:13 -0700
  * [MDEV-13607](https://jira.mariadb.org/browse/MDEV-13607) MariaDB crash in fix\_semijoin\_strategies\_for\_picked\_join\_order
* [Revision #2eb3c5e542](https://github.com/MariaDB/server/commit/2eb3c5e542)\
  2017-10-18 21:19:33 +0300
  * [MDEV-13918](https://jira.mariadb.org/browse/MDEV-13918) Race condition between INFORMATION\_SCHEMA.INNODB\_SYS\_TABLESTATS and ALTER/DROP/TRUNCATE TABLE
* Merge [Revision #da4503e956](https://github.com/MariaDB/server/commit/da4503e956) 2017-10-18 15:14:39 +0200 - Merge branch '5.5' into 10.0
* [Revision #babbf8c6fc](https://github.com/MariaDB/server/commit/babbf8c6fc)\
  2017-10-18 10:20:25 +0300
  * fts\_query\_free(): Fix a potential assertion failure
* [Revision #30e89acd95](https://github.com/MariaDB/server/commit/30e89acd95)\
  2017-10-18 09:52:19 +0300
  * Import, adapt and extend a test from Oracle
* [Revision #9817479563](https://github.com/MariaDB/server/commit/9817479563)\
  2017-10-18 08:25:04 +0300
  * Add a test of LIMIT with FULLTEXT INDEX
* [Revision #dfd010ef90](https://github.com/MariaDB/server/commit/dfd010ef90)\
  2017-10-18 06:35:11 +0300
  * [MDEV-14086](https://jira.mariadb.org/browse/MDEV-14086) Setting innodb\_buffer\_pool\_load\_now or innodb\_buffer\_load\_abort will crash if innodb\_read\_only
* [Revision #4090ef820e](https://github.com/MariaDB/server/commit/4090ef820e)\
  2017-10-17 15:33:19 +0300
  * Fix check\_role\_is\_granted for embedded
* [Revision #9a791c9c8d](https://github.com/MariaDB/server/commit/9a791c9c8d)\
  2017-10-16 13:21:11 +0300
  * [MDEV-12676](https://jira.mariadb.org/browse/MDEV-12676) MySQL#78423 InnoDB FTS duplicate key error
* [Revision #1eee3a3fb7](https://github.com/MariaDB/server/commit/1eee3a3fb7)\
  2017-10-16 12:06:43 +0300
  * [MDEV-13051](https://jira.mariadb.org/browse/MDEV-13051) MySQL#86607 InnoDB crash after failed ADD INDEX and table\_definition\_cache eviction
* [Revision #b9418ed333](https://github.com/MariaDB/server/commit/b9418ed333)\
  2017-10-09 13:32:40 +0300
  * [MDEV-13676](https://jira.mariadb.org/browse/MDEV-13676): Field "create Procedure" is NULL, even if the user has role which is the definer. (SHOW CREATE PROCEDURE)
* [Revision #fc9ff69578](https://github.com/MariaDB/server/commit/fc9ff69578)\
  2017-10-10 10:19:10 +0300
  * [MDEV-13838](https://jira.mariadb.org/browse/MDEV-13838): Wrong result after altering a partitioned table
* [Revision #2db5e4d1f9](https://github.com/MariaDB/server/commit/2db5e4d1f9)\
  2017-10-10 14:31:33 +0200
  * smaller stack size on quantal-x86 and wheezy-x86
* [Revision #1cfcb58539](https://github.com/MariaDB/server/commit/1cfcb58539)\
  2017-10-09 20:30:52 +0300
  * Fix oqgraph compilation with Boost versions <=1.49
* [Revision #440157cbbe](https://github.com/MariaDB/server/commit/440157cbbe)\
  2017-10-05 15:01:38 +0200
  * [MDEV-13412](https://jira.mariadb.org/browse/MDEV-13412) main.func\_regexp\_pcre fails in buildbot on ppc64le
* [Revision #4d33c74224](https://github.com/MariaDB/server/commit/4d33c74224)\
  2016-10-20 21:36:05 +0200
  * [MDEV-10980](https://jira.mariadb.org/browse/MDEV-10980): Fix reverse queries in OQGRAPH.
* [Revision #172cc70bf8](https://github.com/MariaDB/server/commit/172cc70bf8)\
  2017-10-09 12:18:12 +0300
  * [MDEV-13446](https://jira.mariadb.org/browse/MDEV-13446) fts\_create\_doc\_id() unnecessarily allocates 8 bytes for every inserted row
* [Revision #bc85d22bf0](https://github.com/MariaDB/server/commit/bc85d22bf0)\
  2017-10-09 02:49:50 +0300
  * [MDEV-12263](https://jira.mariadb.org/browse/MDEV-12263) Feature: skipped test file
* [Revision #9b897d663a](https://github.com/MariaDB/server/commit/9b897d663a)\
  2017-10-09 01:43:31 +0300
  * [MDEV-12263](https://jira.mariadb.org/browse/MDEV-12263) Feature: skipped test file
* [Revision #ca948e335e](https://github.com/MariaDB/server/commit/ca948e335e)\
  2017-10-07 13:42:11 +0400
  * [MDEV-9886](https://jira.mariadb.org/browse/MDEV-9886) Illegal mix of collations with a view comparing a field to a binary constant
* [Revision #dbeffabc83](https://github.com/MariaDB/server/commit/dbeffabc83)\
  2017-10-06 00:08:36 -0700
  * Fixed the bug [MDEV-11574](https://jira.mariadb.org/browse/MDEV-11574).
* [Revision #e6862cf1ff](https://github.com/MariaDB/server/commit/e6862cf1ff)\
  2017-10-03 00:13:58 +0000
  * Windows MSI : dump server error log to MSI log on installation failure.
* Merge [Revision #de4a00d4f7](https://github.com/MariaDB/server/commit/de4a00d4f7) 2017-10-02 10:42:55 +0300 - Merge 5.5 into 10.0
* [Revision #19d21b9366](https://github.com/MariaDB/server/commit/19d21b9366)\
  2017-09-25 09:29:27 +0300
  * Cherry-pick the [MDEV-13898](https://jira.mariadb.org/browse/MDEV-13898) test changes from 10.2 to 10.0
* [Revision #78b63425a3](https://github.com/MariaDB/server/commit/78b63425a3)\
  2017-09-24 10:11:16 +0300
  * [MDEV-13899](https://jira.mariadb.org/browse/MDEV-13899) IMPORT TABLESPACE may corrupt ROW\_FORMAT=REDUNDANT tables
* [Revision #7128fefa4c](https://github.com/MariaDB/server/commit/7128fefa4c)\
  2017-09-23 23:23:05 +0200
  * Fix compile with -DWITHOUT\_DYNAMIC\_PLUGINS on Unix
* [Revision #f6cb4f0a19](https://github.com/MariaDB/server/commit/f6cb4f0a19)\
  2017-09-22 10:28:14 +0300
  * [MDEV-13814](https://jira.mariadb.org/browse/MDEV-13814) Extra logging when innodb\_log\_archive=ON
* [Revision #8d0448d507](https://github.com/MariaDB/server/commit/8d0448d507)\
  2017-09-21 18:05:07 +0200
  * [MDEV-13861](https://jira.mariadb.org/browse/MDEV-13861) Assertion \`0' failed in Protocol::end\_statement
* [Revision #cb1b466c0c](https://github.com/MariaDB/server/commit/cb1b466c0c)\
  2017-08-16 13:26:53 +0200
  * CONNECT: compilation fix
* [Revision #db7fd021fe](https://github.com/MariaDB/server/commit/db7fd021fe)\
  2017-09-21 12:31:30 +0300
  * Add have\_debug.inc to skip the test faster in non-debug builds
* [Revision #1015196e0a](https://github.com/MariaDB/server/commit/1015196e0a)\
  2017-09-21 10:03:40 +0200
  * cleanup: TABLE\_LIST::view\_check\_option
* [Revision #e84f5356c3](https://github.com/MariaDB/server/commit/e84f5356c3)\
  2017-09-21 13:22:49 +0530
  * [MDEV-12290](https://jira.mariadb.org/browse/MDEV-12290) Wrong timestamps in binary log causes replication issues
* [Revision #378beed0a6](https://github.com/MariaDB/server/commit/378beed0a6)\
  2017-09-20 20:02:01 +0200
  * [MDEV-13290](https://jira.mariadb.org/browse/MDEV-13290): Assertion `!is_set() || (m_status == DA_OK_BULK && is_bulk_op())' or` ! is\_set()' failed
* [Revision #b7434bacbd](https://github.com/MariaDB/server/commit/b7434bacbd)\
  2017-09-20 17:51:43 +0200
  * include/master-slave.inc must always be included last
* [Revision #8f3fd98d25](https://github.com/MariaDB/server/commit/8f3fd98d25)\
  2017-09-20 17:07:05 +0200
  * connect fixes after-merge
* [Revision #d3976cf72a](https://github.com/MariaDB/server/commit/d3976cf72a)\
  2017-09-20 15:59:40 +0200
  * remove an empty file with a wrong name
* Merge [Revision #20d4cac6db](https://github.com/MariaDB/server/commit/20d4cac6db) 2017-09-20 10:24:31 +0300 - Merge branch 'bb-10.0-vicentiu' into 10.0
* [Revision #b337a06829](https://github.com/MariaDB/server/commit/b337a06829)\
  2017-09-19 11:53:59 +0300
  * Revert d9bc5e03d788b958ce8c76e157239953db60adb2 from Oracle (in XtraDB)
* [Revision #dab6f56098](https://github.com/MariaDB/server/commit/dab6f56098)\
  2017-09-19 11:37:50 +0300
  * Revert Bug #25175249 ASSERTION: (TEMPL->IS\_VIRTUAL && !FIELD) || (FIELD && FIELD->PREFIX\_LEN ? FIELD
* Merge [Revision #cbd62feee5](https://github.com/MariaDB/server/commit/cbd62feee5) 2017-09-19 11:35:09 +0300 - Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #b4606367d7](https://github.com/MariaDB/server/commit/b4606367d7)\
  2017-09-19 00:44:27 +0300
  * 5.6.37-82.2
* Merge [Revision #745cd57ae7](https://github.com/MariaDB/server/commit/745cd57ae7) 2017-09-19 11:18:17 +0300 - Merge branch 'merge-tokudb-5.6' into 10.0
* [Revision #618d8fdf37](https://github.com/MariaDB/server/commit/618d8fdf37)\
  2017-09-19 10:58:12 +0300
  * 5.6.37-82.2
* [Revision #0e15396341](https://github.com/MariaDB/server/commit/0e15396341)\
  2017-09-19 11:17:35 +0300
  * Fix fall-through warning
* [Revision #b2c0cca6b0](https://github.com/MariaDB/server/commit/b2c0cca6b0)\
  2017-09-19 09:26:27 +0300
  * Fix connect merge problems
* [Revision #df2675a9cc](https://github.com/MariaDB/server/commit/df2675a9cc)\
  2017-09-19 02:04:05 +0300
  * Merge connect/10.0 into 10.0
* [Revision #0f44c8ab28](https://github.com/MariaDB/server/commit/0f44c8ab28)\
  2017-09-19 02:04:45 +0300
  * Fix merge error
* Merge [Revision #d6a7de2022](https://github.com/MariaDB/server/commit/d6a7de2022) 2017-09-19 01:02:01 +0300 - Merge branch '5.5' into 10.0
* [Revision #97c2a7354b](https://github.com/MariaDB/server/commit/97c2a7354b)\
  2017-09-19 15:55:59 +0200
  * [MDEV-13290](https://jira.mariadb.org/browse/MDEV-13290): Assertion `!is_set() || (m_status == DA_OK_BULK && is_bulk_op())' or` ! is\_set()' failed
* [Revision #389f7cdf3c](https://github.com/MariaDB/server/commit/389f7cdf3c)\
  2017-09-19 13:08:24 +0400
  * [MDEV-13137](https://jira.mariadb.org/browse/MDEV-13137) MySQL 5.6.23 Crashes when SET GLOBAL server\_audit\_logging=OFF;
* [Revision #a870099817](https://github.com/MariaDB/server/commit/a870099817)\
  2017-09-15 16:20:16 +0000
  * Windows : support vsjitdebugger in MTR's --debugger.
* [Revision #a73b55a9f8](https://github.com/MariaDB/server/commit/a73b55a9f8)\
  2017-09-15 16:19:14 +0000
  * Windows : fix a warning in popular header file
* [Revision #434e283507](https://github.com/MariaDB/server/commit/434e283507)\
  2017-09-15 12:25:06 +0400
  * [MDEV-13685](https://jira.mariadb.org/browse/MDEV-13685) Can not replay binary log due to Illegal mix of collations (latin1\_swedish\_ci,IMPLICIT) and (utf8mb4\_general\_ci,COERCIBLE) for operation 'concat'
* Merge [Revision #65c94238f8](https://github.com/MariaDB/server/commit/65c94238f8) 2017-09-09 10:55:47 +0000 - Merge branch 'bb-10.0-wlad' into 10.0
* [Revision #a46679dcf7](https://github.com/MariaDB/server/commit/a46679dcf7)\
  2017-09-08 16:08:44 +0000
  * Build improvements and cleanups.
* [Revision #d861822c4f](https://github.com/MariaDB/server/commit/d861822c4f)\
  2017-09-07 12:01:07 +0300
  * [MDEV-13253](https://jira.mariadb.org/browse/MDEV-13253) After rebuilding redo logs, InnoDB can leak data from redo log buffer
* [Revision #ee844f6c34](https://github.com/MariaDB/server/commit/ee844f6c34)\
  2017-09-07 11:59:26 +0300
  * Make the SEARCH\_ABORT logic actually work
* [Revision #3ec8268b4a](https://github.com/MariaDB/server/commit/3ec8268b4a)\
  2017-09-07 11:58:21 +0300
  * Follow-up to [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103): Do not add attribute((nonnull))
* [Revision #6b45355e6b](https://github.com/MariaDB/server/commit/6b45355e6b)\
  2017-09-06 14:01:15 +0300
  * [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103) Assertion \`flags & BUF\_PAGE\_PRINT\_NO\_CRASH' failed in buf\_page\_print
* [Revision #641baa5d03](https://github.com/MariaDB/server/commit/641baa5d03)\
  2017-08-31 14:22:05 +0300
  * Post-push for [MDEV-13437](https://jira.mariadb.org/browse/MDEV-13437)
* [Revision #0500899904](https://github.com/MariaDB/server/commit/0500899904)\
  2017-09-04 09:46:47 +0300
  * [MDEV-13705](https://jira.mariadb.org/browse/MDEV-13705) 10.0.32 does not compile on architectures without 64-bit atomics
* [Revision #7f99381288](https://github.com/MariaDB/server/commit/7f99381288)\
  2017-09-01 15:29:34 +0300
  * Fix compiler warnings
* [Revision #6be93c3b8a](https://github.com/MariaDB/server/commit/6be93c3b8a)\
  2017-08-31 14:50:45 +0000
  * [MDEV-13693](https://jira.mariadb.org/browse/MDEV-13693) : Fix parameter passing to my\_error.
* [Revision #66eb9774e4](https://github.com/MariaDB/server/commit/66eb9774e4)\
  2017-08-31 12:33:46 +0000
  * [MDEV-13691](https://jira.mariadb.org/browse/MDEV-13691) : my\_write() sets inappropriate errno for ERROR\_FILE\_SYSTEM\_LIMITATON
* [Revision #eb389d5c39](https://github.com/MariaDB/server/commit/eb389d5c39)\
  2017-08-30 09:32:03 +0300
  * Add missing {} to silence a compiler warning
* [Revision #e634fdcd5b](https://github.com/MariaDB/server/commit/e634fdcd5b)\
  2017-08-29 21:58:02 +0300
  * [WL#8845](https://askmonty.org/worklog/?tid=8845): Clarify the message about redo log format incompatibility
* Merge [Revision #fdbdd3b131](https://github.com/MariaDB/server/commit/fdbdd3b131) 2017-08-29 18:36:03 +0300 - [MDEV-13625](https://jira.mariadb.org/browse/MDEV-13625) Merge InnoDB test cases from MySQL 5.6 (part 1)
* [Revision #9e9a3b8ede](https://github.com/MariaDB/server/commit/9e9a3b8ede)\
  2017-08-29 13:15:35 +0300
  * Merge innodb.create-index test changes from MySQL 5.6 to MariaDB
* [Revision #f56bd70f51](https://github.com/MariaDB/server/commit/f56bd70f51)\
  2017-08-29 15:40:37 +0300
  * Adjust the imported MySQL 5.6 tests for MariaDB
* [Revision #8d9298167e](https://github.com/MariaDB/server/commit/8d9298167e)\
  2017-08-29 11:27:28 +0300
  * [MDEV-13625](https://jira.mariadb.org/browse/MDEV-13625) Merge InnoDB test cases from MySQL 5.6 (part 1)
* [Revision #888a8b69bd](https://github.com/MariaDB/server/commit/888a8b69bd)\
  2017-08-29 10:52:52 +0300
  * [MDEV-13437](https://jira.mariadb.org/browse/MDEV-13437) InnoDB fails to return error for XA COMMIT or XA ROLLBACK in read-only mode
* [Revision #05e7d35e89](https://github.com/MariaDB/server/commit/05e7d35e89)\
  2017-08-24 23:15:55 +0300
  * [MDEV-13583](https://jira.mariadb.org/browse/MDEV-13583) Improvements for MTR rebootstrap introduced in [MDEV-12042](https://jira.mariadb.org/browse/MDEV-12042)
* [Revision #582545a384](https://github.com/MariaDB/server/commit/582545a384)\
  2017-08-24 15:38:05 +0300
  * [MDEV-13637](https://jira.mariadb.org/browse/MDEV-13637) InnoDB change buffer housekeeping can cause redo log overrun and possibly deadlocks
* [Revision #cd35dd6a05](https://github.com/MariaDB/server/commit/cd35dd6a05)\
  2017-08-24 15:49:50 +0000
  * Windows : Do not use CRT routine to dump memory leaks.
* [Revision #dd229430a9](https://github.com/MariaDB/server/commit/dd229430a9)\
  2017-08-24 08:05:11 +0000
  * Windows compile : make compilation fail on "uninitialized variable used" warning C4700
* [Revision #7aa846e9e3](https://github.com/MariaDB/server/commit/7aa846e9e3)\
  2017-08-23 23:30:51 +0000
  * CONNECT engine: install ha\_connect.lib
* [Revision #7b36395ee9](https://github.com/MariaDB/server/commit/7b36395ee9)\
  2017-08-23 23:29:59 +0000
  * [MDEV-13630](https://jira.mariadb.org/browse/MDEV-13630) : dont install connect-specific JAR files if connect is not built.
* [Revision #db51ad1e01](https://github.com/MariaDB/server/commit/db51ad1e01)\
  2017-08-23 18:11:24 +0000
  * Remove workaround for ancient and already fixed CMake bug in MSI creation.
* [Revision #b8b3ba632b](https://github.com/MariaDB/server/commit/b8b3ba632b)\
  2017-08-23 13:03:13 +0300
  * [MDEV-13606](https://jira.mariadb.org/browse/MDEV-13606) XA PREPARE transactions should survive innodb\_force\_recovery=1 or 2
* [Revision #ce6c0e584e](https://github.com/MariaDB/server/commit/ce6c0e584e)\
  2017-07-27 13:17:13 +0300
  * [MDEV-8960](https://jira.mariadb.org/browse/MDEV-8960): Can't refer the same column twice in one ALTER TABLE
* [Revision #7581fb23e2](https://github.com/MariaDB/server/commit/7581fb23e2)\
  2017-08-14 18:37:53 +0200
  * compilation fix for SLES 11 SP4
* [Revision #fc556a8d94](https://github.com/MariaDB/server/commit/fc556a8d94)\
  2017-08-10 12:03:48 +0200
  * compilation fix for SLES 11 SP4
* [Revision #cb9648a6b5](https://github.com/MariaDB/server/commit/cb9648a6b5)\
  2017-08-09 14:29:22 +0300
  * Revert an InnoDB Memcached plugin fix that was merged from MySQL 5.6.37
* [Revision #ef2e51c396](https://github.com/MariaDB/server/commit/ef2e51c396)\
  2017-08-07 10:09:23 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
