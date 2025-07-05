# MariaDB 10.2.10 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/release-notes-mariadb-10-2-series/mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.10)[Release Notes](../../old-releases/release-notes-mariadb-10-2-series/mariadb-10210-release-notes.md)[Changelog](mariadb-10210-changelog.md)[Overview of 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md)

**Release date:** 31 Oct 2017

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-2-series/mariadb-10210-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.2) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #58e0dcb93d](https://github.com/MariaDB/server/commit/58e0dcb93d)\
  2017-10-30 10:06:47 +0200
  * Add a missing space to an error message
* [Revision #de6bfbd5e9](https://github.com/MariaDB/server/commit/de6bfbd5e9)\
  2017-10-30 03:25:49 +0200
  * Updated list of unstable tests for 10.2.10
* [Revision #a269173e97](https://github.com/MariaDB/server/commit/a269173e97)\
  2017-10-30 03:24:35 +0200
  * Workaround for [MDEV-13852](https://jira.mariadb.org/browse/MDEV-13852) (tests don't run on Windows)
* [Revision #7cca0df0d7](https://github.com/MariaDB/server/commit/7cca0df0d7)\
  2017-10-29 22:55:51 +0300
  * Fix rocksdb.rocksdb test
* [Revision #e5678c3fac](https://github.com/MariaDB/server/commit/e5678c3fac)\
  2017-10-29 13:21:23 +0300
  * [MDEV-13904](https://jira.mariadb.org/browse/MDEV-13904): rocksdb.add\_index\_inplace\_sstfilewriter timed out
* [Revision #34188ac455](https://github.com/MariaDB/server/commit/34188ac455)\
  2017-10-29 09:41:40 +0000
  * Organize information in storage/rocksdb/mysql-test/rocksdb/t/disabled.def
* [Revision #a6dc22fc73](https://github.com/MariaDB/server/commit/a6dc22fc73)\
  2017-10-29 11:49:18 +0300
  * MyRocks: enable a few tests that do not seem to fail anymore
* [Revision #b6d4859547](https://github.com/MariaDB/server/commit/b6d4859547)\
  2017-10-29 11:39:52 +0300
  * [MDEV-14181](https://jira.mariadb.org/browse/MDEV-14181): rocksdb.rocksdb fails: line 1117: query 'reap' succeeded - should have failed
* Merge [Revision #8abe840085](https://github.com/MariaDB/server/commit/8abe840085) 2017-10-29 11:27:24 +0300 - Merge branch 'bb-10.2-mariarocks' of github.com:MariaDB/server into 10.2
* [Revision #3d46ebbc89](https://github.com/MariaDB/server/commit/3d46ebbc89)\
  2017-10-27 17:48:17 +0300
  * [MDEV-11934](https://jira.mariadb.org/browse/MDEV-11934): MariaRocks: Group Commit with binlog
* [Revision #6cfbffad5b](https://github.com/MariaDB/server/commit/6cfbffad5b)\
  2017-10-23 10:04:55 +0000
  * Code cleanup
* [Revision #97df230aed](https://github.com/MariaDB/server/commit/97df230aed)\
  2017-10-27 23:42:02 +0000
  * [MDEV-14115](https://jira.mariadb.org/browse/MDEV-14115) : Do not use lpNumberOfBytesRead/Written params in ReadFile/WriteFile operations.
* [Revision #067f83969c](https://github.com/MariaDB/server/commit/067f83969c)\
  2017-10-27 19:33:38 +0300
  * [MDEV-14132](https://jira.mariadb.org/browse/MDEV-14132) follow-up fix: Make os\_file\_get\_size() thread-safe
* [Revision #9dfe84d5de](https://github.com/MariaDB/server/commit/9dfe84d5de)\
  2017-10-27 19:01:24 +0300
  * Remove a bogus page\_is\_root() debug assertion on btr\_create() failure
* [Revision #5f5ffdc76b](https://github.com/MariaDB/server/commit/5f5ffdc76b)\
  2017-10-27 18:59:22 +0300
  * [MDEV-14132](https://jira.mariadb.org/browse/MDEV-14132) follow-up fix: Validate the posix\_fallocate() argument
* [Revision #057a6cf768](https://github.com/MariaDB/server/commit/057a6cf768)\
  2017-10-27 11:56:10 +0000
  * [MDEV-14132](https://jira.mariadb.org/browse/MDEV-14132) : fix posix\_fallocate() calls to workaround some (ancient) Linux bugs
* [Revision #1792a80af4](https://github.com/MariaDB/server/commit/1792a80af4)\
  2017-10-27 12:33:27 +0300
  * Disable rocksdb.col\_opt\_zerofill due to [MDEV-14165](https://jira.mariadb.org/browse/MDEV-14165).
* [Revision #b94a62b5df](https://github.com/MariaDB/server/commit/b94a62b5df)\
  2017-10-27 11:16:32 +0300
  * [MDEV-13890](https://jira.mariadb.org/browse/MDEV-13890) mariadb-backup.xb\_compressed\_encrypted failed in buildbot, InnoDB: assertion failure
* [Revision #f29cfa1d7e](https://github.com/MariaDB/server/commit/f29cfa1d7e)\
  2017-10-27 10:43:06 +0300
  * Remove dead code for MLOG\_UNDO\_HDR\_DISCARD
* [Revision #02ba15a9da](https://github.com/MariaDB/server/commit/02ba15a9da)\
  2017-10-27 10:20:22 +0300
  * Relax a too strict assertion at shutdown
* Merge [Revision #00c4668153](https://github.com/MariaDB/server/commit/00c4668153) 2017-10-27 10:36:42 +0300 - Merge two innodb\_fts tests from MySQL 5.7
* [Revision #b4f104c9f0](https://github.com/MariaDB/server/commit/b4f104c9f0)\
  2017-10-26 17:08:07 +0300
  * Adjust the innodb\_fts.sync and innodb\_fts.sync\_block tests for MariaDB
* [Revision #4136288705](https://github.com/MariaDB/server/commit/4136288705)\
  2017-10-26 16:29:08 +0300
  * Import the innodb\_fts.sync tests from MySQL
* Merge [Revision #786a722eba](https://github.com/MariaDB/server/commit/786a722eba) 2017-10-27 10:24:02 +0300 - Merge 10.1 into 10.2
* Merge [Revision #38e12db478](https://github.com/MariaDB/server/commit/38e12db478) 2017-10-26 13:36:38 +0300 - Merge 10.0 into 10.1
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
* [Revision #965c72d331](https://github.com/MariaDB/server/commit/965c72d331)\
  2017-10-26 18:21:20 +0300
  * [MDEV-12474](https://jira.mariadb.org/browse/MDEV-12474) - Fails in fulltest
* [Revision #771305b21d](https://github.com/MariaDB/server/commit/771305b21d)\
  2017-10-26 14:11:38 +0300
  * [MDEV-12569](https://jira.mariadb.org/browse/MDEV-12569) InnoDB suggests filing bugs at MySQL bug tracker
* [Revision #550c8bdb81](https://github.com/MariaDB/server/commit/550c8bdb81)\
  2017-10-26 13:49:11 +0300
  * Make debug multi thread safe
* Merge [Revision #5144861be9](https://github.com/MariaDB/server/commit/5144861be9) 2017-10-26 09:00:08 +0300 - Merge pull request #475 from grooverdan/10.2-no\_recv\_sys\_mem\_free
* [Revision #91dc18dcf5](https://github.com/MariaDB/server/commit/91dc18dcf5)\
  2017-10-26 16:40:21 +1100
  * innodb: remove recv\_sys\_mem\_free - unused
* [Revision #e99c7c8334](https://github.com/MariaDB/server/commit/e99c7c8334)\
  2017-10-25 19:12:08 +0200
  * [MDEV-13836](https://jira.mariadb.org/browse/MDEV-13836) mariadb\_config & mysql\_config output differ
* [Revision #230350872c](https://github.com/MariaDB/server/commit/230350872c)\
  2017-10-26 00:04:42 +0200
  * update C/C
* Merge [Revision #a8136719fe](https://github.com/MariaDB/server/commit/a8136719fe) 2017-10-26 00:00:16 +0200 - Merge branch 'connect/10.2' into 10.2
* [Revision #74ffcbc135](https://github.com/MariaDB/server/commit/74ffcbc135)\
  2017-10-17 21:50:17 +0200\
  \*
  * Typo (from 10.1) Modified: storage/connect/value.cpp
* [Revision #c83e2a6345](https://github.com/MariaDB/server/commit/c83e2a6345)\
  2017-10-16 15:08:17 +0200\
  \*
  * Fix a bug in TYPVAL compute causing it sometime not to be executed This was the cause of the bug in CalculateArray modified: storage/connect/jsonudf.cpp modified: storage/connect/tabjson.cpp modified: storage/connect/value.cpp
* [Revision #6691d12e2d](https://github.com/MariaDB/server/commit/6691d12e2d)\
  2017-10-16 00:48:03 +0200\
  \*
  * Make another temporary fix for the compiler bug in CalculateArray modified: storage/connect/jsonudf.cpp modified: storage/connect/tabjson.cpp
* [Revision #bcfb5b2de9](https://github.com/MariaDB/server/commit/bcfb5b2de9)\
  2017-10-15 16:13:23 +0200\
  \*
  * Update version number modified: storage/connect/ha\_connect.cc
* Merge [Revision #cbd0da66e4](https://github.com/MariaDB/server/commit/cbd0da66e4) 2017-10-25 17:17:21 +0300 - Merge 10.1 into 10.2
* [Revision #909cdafd35](https://github.com/MariaDB/server/commit/909cdafd35)\
  2017-10-25 09:06:45 +0300
  * [MDEV-13496](https://jira.mariadb.org/browse/MDEV-13496) Use "mariadb-backup" rather than "xtrabackup" in console output
* Merge [Revision #db203d7471](https://github.com/MariaDB/server/commit/db203d7471) 2017-10-24 19:26:24 +0300 - Merge 10.0 into 10.1
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
* [Revision #4330505629](https://github.com/MariaDB/server/commit/4330505629)\
  2017-10-23 14:17:50 +0000
  * Do not use File::Which, it is not always available.
* [Revision #72407e544e](https://github.com/MariaDB/server/commit/72407e544e)\
  2017-10-23 10:37:28 +0000
  * [MDEV-13496](https://jira.mariadb.org/browse/MDEV-13496) Use "mariadb-backup" rather than "xtrabackup" in console output
* [Revision #125ce6f82f](https://github.com/MariaDB/server/commit/125ce6f82f)\
  2017-10-23 10:30:17 +0000
  * [MDEV-14102](https://jira.mariadb.org/browse/MDEV-14102) restore --remove-original options for mariadb-backup
* [Revision #a02551b0ba](https://github.com/MariaDB/server/commit/a02551b0ba)\
  2017-10-25 10:10:18 +0000
  * Windows- "my\_safe\_kill dump" will now also dump child processes
* [Revision #a6a4c25bf7](https://github.com/MariaDB/server/commit/a6a4c25bf7)\
  2017-10-12 17:21:04 +0300
  * MariaDB adjustments to innodb\_gis tests.
* [Revision #42e3e57426](https://github.com/MariaDB/server/commit/42e3e57426)\
  2017-10-12 16:21:21 +0300
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Merge InnoDB test cases from MySQL 5.7
* [Revision #f7090df712](https://github.com/MariaDB/server/commit/f7090df712)\
  2017-10-24 20:59:54 +0200
  * [MDEV-13968](https://jira.mariadb.org/browse/MDEV-13968) sst fails with "WSREP\_SST\_OPT\_PORT: readonly variable"
* [Revision #24bffb080b](https://github.com/MariaDB/server/commit/24bffb080b)\
  2017-10-24 23:19:54 +0300
  * [MDEV-13918](https://jira.mariadb.org/browse/MDEV-13918) Race condition between INFORMATION\_SCHEMA.INNODB\_SYS\_TABLESTATS and ALTER/DROP/TRUNCATE TABLE
* [Revision #632f0e71f8](https://github.com/MariaDB/server/commit/632f0e71f8)\
  2017-10-24 16:03:05 +0000
  * Fix my\_safe\_kill's create crashdump functionality on Windows.
* [Revision #b56560ed39](https://github.com/MariaDB/server/commit/b56560ed39)\
  2017-10-24 15:56:54 +0000
  * Fix a warning on Win64
* Merge [Revision #e0a1c745ec](https://github.com/MariaDB/server/commit/e0a1c745ec) 2017-10-24 14:53:18 +0200 - Merge branch '10.1' into 10.2
* [Revision #2aa51f528f](https://github.com/MariaDB/server/commit/2aa51f528f)\
  2017-10-22 13:18:38 +0200
  * Various compier warnings
* Merge [Revision #9d2e2d7533](https://github.com/MariaDB/server/commit/9d2e2d7533) 2017-10-22 13:03:41 +0200 - Merge branch '10.0' into 10.1
* [Revision #2eb3c5e542](https://github.com/MariaDB/server/commit/2eb3c5e542)\
  2017-10-18 21:19:33 +0300
  * [MDEV-13918](https://jira.mariadb.org/browse/MDEV-13918) Race condition between INFORMATION\_SCHEMA.INNODB\_SYS\_TABLESTATS and ALTER/DROP/TRUNCATE TABLE
* Merge [Revision #da4503e956](https://github.com/MariaDB/server/commit/da4503e956) 2017-10-18 15:14:39 +0200 - Merge branch '5.5' into 10.0
* [Revision #b000e16956](https://github.com/MariaDB/server/commit/b000e16956)\
  2017-10-17 10:57:51 +0200
  * Bug#26361149 MYSQL SERVER CRASHES AT: COL IN(IFNULL(CONST, COL), NAME\_CONST('NAME', NULL))
* Merge [Revision #df5f25fa7a](https://github.com/MariaDB/server/commit/df5f25fa7a) 2017-10-17 10:18:17 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #b036b6b594](https://github.com/MariaDB/server/commit/b036b6b594)\
  2017-10-16 12:34:17 +0200
  * [MDEV-13937](https://jira.mariadb.org/browse/MDEV-13937) Aria engine: Internal Error 160 after partition handling
* [Revision #19a702a85c](https://github.com/MariaDB/server/commit/19a702a85c)\
  2017-10-14 15:59:54 +0200
  * [MDEV-14056](https://jira.mariadb.org/browse/MDEV-14056) DROP TEMPORARY TABLE IF EXISTS causes error 1290 with read\_only option
* [Revision #421716391b](https://github.com/MariaDB/server/commit/421716391b)\
  2017-10-14 15:03:43 +0200
  * [MDEV-13912](https://jira.mariadb.org/browse/MDEV-13912) Can't refer the same column twice in one ALTER TABLE
* [Revision #93144b9e92](https://github.com/MariaDB/server/commit/93144b9e92)\
  2017-10-13 21:26:30 +0200
  * [MDEV-13440](https://jira.mariadb.org/browse/MDEV-13440) mysql\_install\_db fails with hard-coded langdir
* [Revision #52516706c8](https://github.com/MariaDB/server/commit/52516706c8)\
  2017-10-13 20:53:55 +0200
  * cleanup mysql\_install\_db
* [Revision #d76f5774fe](https://github.com/MariaDB/server/commit/d76f5774fe)\
  2017-09-16 14:52:42 +0200
  * [MDEV-13459](https://jira.mariadb.org/browse/MDEV-13459) Warnings, when compiling with gcc-7.x
* [Revision #3b7aa3017b](https://github.com/MariaDB/server/commit/3b7aa3017b)\
  2017-10-13 18:41:38 +0200
  * Cleanup usage of DBUG\_ASSERTS.
* [Revision #235b68299b](https://github.com/MariaDB/server/commit/235b68299b)\
  2017-02-18 17:47:31 +0100
  * [MDEV-9619](https://jira.mariadb.org/browse/MDEV-9619): Assertion \`null\_ref\_table' failed in virtual table\_map Item\_direct\_view\_ref::used\_tables() const on 2nd execution of PS
* [Revision #2bab29ebba](https://github.com/MariaDB/server/commit/2bab29ebba)\
  2017-10-13 07:24:35 -0700
  * Fixed the bug [MDEV-13135](https://jira.mariadb.org/browse/MDEV-13135).
* [Revision #8be76a6a90](https://github.com/MariaDB/server/commit/8be76a6a90)\
  2017-10-12 13:30:02 +0400
  * [MDEV-10892](https://jira.mariadb.org/browse/MDEV-10892) - rpl.rpl\_semi\_sync\_uninstall\_plugin fails with Assertion \`0' failure in buildbot
* [Revision #a4868c3509](https://github.com/MariaDB/server/commit/a4868c3509)\
  2016-12-19 22:03:28 +0100
  * [MDEV-9208](https://jira.mariadb.org/browse/MDEV-9208): Function->Function->View = Mysqld segfault (Server crashes in Dependency\_marker::visit\_field on 2nd execution with merged subquery)
* [Revision #991b9ee735](https://github.com/MariaDB/server/commit/991b9ee735)\
  2017-10-13 07:06:09 +0400
  * [MDEV-13530](https://jira.mariadb.org/browse/MDEV-13530) VARBINARY doesn't convert to BLOB for sizes 65533, 65534 and 65535
* [Revision #93aadda513](https://github.com/MariaDB/server/commit/93aadda513)\
  2017-10-08 22:15:00 +0300
  * [MDEV-13149](https://jira.mariadb.org/browse/MDEV-13149) -- show function status now works with PAD\_CHAR\_TO\_FULL\_LENGTH
* [Revision #c2509a1588](https://github.com/MariaDB/server/commit/c2509a1588)\
  2017-10-10 10:35:12 +0400
  * [MDEV-13972](https://jira.mariadb.org/browse/MDEV-13972) crash in Item\_func\_sec\_to\_time::get\_date
* [Revision #e30b6a983f](https://github.com/MariaDB/server/commit/e30b6a983f)\
  2017-10-06 18:23:40 +0400
  * [MDEV-11819](https://jira.mariadb.org/browse/MDEV-11819) NO\_ZERO\_IN\_DATE: Incorrect generated column value
* [Revision #bea99275de](https://github.com/MariaDB/server/commit/bea99275de)\
  2017-10-05 15:07:21 +0200
  * [MDEV-13595](https://jira.mariadb.org/browse/MDEV-13595): mariadb-10.2.8/storage/maria/ma\_loghandler.c:2730]: (style) Array index 'chunk\_offset' is used before limits check.
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
* [Revision #d11af09865](https://github.com/MariaDB/server/commit/d11af09865)\
  2017-10-16 20:54:07 +0300
  * [MDEV-14076](https://jira.mariadb.org/browse/MDEV-14076) InnoDB: Failing assertion when accessing INFORMATION\_SCHEMA.INNODB\_SYS\_TABLESPACES upon upgrade from 10.1.0 to 10.1.20
* [Revision #98cd0ec536](https://github.com/MariaDB/server/commit/98cd0ec536)\
  2017-10-14 19:43:16 +0400
  * [MDEV-10802](https://jira.mariadb.org/browse/MDEV-10802) TIMESTAMP NOT NULL field with explicit\_defaults\_for\_timestamp and NO\_ZERO\_DATE shouldn't throw error
* [Revision #9534c04515](https://github.com/MariaDB/server/commit/9534c04515)\
  2017-10-11 01:08:14 +0530
  * Bug Fix
* [Revision #9749568deb](https://github.com/MariaDB/server/commit/9749568deb)\
  2017-10-09 18:22:24 +0200
  * [MDEV-13946](https://jira.mariadb.org/browse/MDEV-13946) Server RPMs have dependency on "which"
* [Revision #9b11956e86](https://github.com/MariaDB/server/commit/9b11956e86)\
  2017-10-06 18:16:46 +0200
  * [MDEV-13049](https://jira.mariadb.org/browse/MDEV-13049) Querying INFORMATION\_SCHEMA becomes slow in [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)
* [Revision #559dec33cc](https://github.com/MariaDB/server/commit/559dec33cc)\
  2017-10-06 19:38:56 +0200
  * cleanup: is\_show\_command(thd)
* [Revision #494d1bf885](https://github.com/MariaDB/server/commit/494d1bf885)\
  2017-10-09 10:22:47 +0200
  * [MDEV-14010](https://jira.mariadb.org/browse/MDEV-14010) merge issue in wsrep\_sst\_xtrabackup-v2
* [Revision #5eb666ad37](https://github.com/MariaDB/server/commit/5eb666ad37)\
  2017-10-07 14:17:45 +0400
  * [MDEV-12705](https://jira.mariadb.org/browse/MDEV-12705) 10.1.18-MariaDB-1jessie - mysqld got signal 11.
* [Revision #4ec88ea9c3](https://github.com/MariaDB/server/commit/4ec88ea9c3)\
  2017-10-23 22:01:19 +0000
  * Fix a warning on Win64
* Merge [Revision #9d47c4cfdb](https://github.com/MariaDB/server/commit/9d47c4cfdb) 2017-10-23 09:47:10 +0000 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mariarocks
* [Revision #7c42b091b7](https://github.com/MariaDB/server/commit/7c42b091b7)\
  2017-10-20 13:36:55 +0300
  * Make rocksdb.index\_merge\_rocksdb2 test stable
* [Revision #607d8f9e97](https://github.com/MariaDB/server/commit/607d8f9e97)\
  2017-10-18 14:37:10 +0200
  * [MDEV-14081](https://jira.mariadb.org/browse/MDEV-14081) ALTER TABLE CHANGE COLUMN Corrupts Index Leading to Crashes in 10.2
* [Revision #e6df6031f6](https://github.com/MariaDB/server/commit/e6df6031f6)\
  2017-10-16 19:33:06 +0200
  * [MDEV-13969](https://jira.mariadb.org/browse/MDEV-13969) sst mysqldump and xtrabackup-v2 handle WSREP\_SST\_OPT\_CONF incorrectly
* [Revision #4c2c057d40](https://github.com/MariaDB/server/commit/4c2c057d40)\
  2017-10-16 17:49:52 +0200
  * [MDEV-13968](https://jira.mariadb.org/browse/MDEV-13968) sst fails with "WSREP\_SST\_OPT\_PORT: readonly variable"
* [Revision #30faf331b8](https://github.com/MariaDB/server/commit/30faf331b8)\
  2017-10-11 21:53:43 +0200
  * [MDEV-13836](https://jira.mariadb.org/browse/MDEV-13836) mariadb\_config & mysql\_config output differ
* [Revision #a75884e701](https://github.com/MariaDB/server/commit/a75884e701)\
  2017-10-08 21:01:03 +0200
  * [MDEV-13836](https://jira.mariadb.org/browse/MDEV-13836) mariadb\_config & mysql\_config output differ
* [Revision #98cc7a8eef](https://github.com/MariaDB/server/commit/98cc7a8eef)\
  2017-10-18 17:04:15 +0300
  * Fixed compiler warnings
* Merge [Revision #3294f6c30d](https://github.com/MariaDB/server/commit/3294f6c30d) 2017-10-18 11:54:18 +0300 - [MDEV-14085](https://jira.mariadb.org/browse/MDEV-14085) Merge new release of InnoDB MySQL 5.7.20 to 10.2
* [Revision #59d3ba0b5d](https://github.com/MariaDB/server/commit/59d3ba0b5d)\
  2017-10-18 07:01:46 +0300
  * Adjust the instrumentation and test
* [Revision #7c9651a371](https://github.com/MariaDB/server/commit/7c9651a371)\
  2017-06-01 10:14:05 +0530
  * BUG#25479538 ASSERT:SIZE == SPACE->SIZE DURING BUF\_READ\_AHEAD\_RANDOM
* [Revision #3bc094d32a](https://github.com/MariaDB/server/commit/3bc094d32a)\
  2017-10-18 08:58:39 +0300
  * Remove dead code for pushing down LIMIT to InnoDB FULLTEXT INDEX queries
* [Revision #a63102226e](https://github.com/MariaDB/server/commit/a63102226e)\
  2017-10-17 10:58:46 +0300
  * [MDEV-14082](https://jira.mariadb.org/browse/MDEV-14082) Enforcing innodb\_open\_files leads to fil\_system->mutex problem
* [Revision #ad46ce658a](https://github.com/MariaDB/server/commit/ad46ce658a)\
  2017-10-14 14:28:11 +0300
  * [MDEV-14055](https://jira.mariadb.org/browse/MDEV-14055) Assertion \`page\_rec\_is\_leaf(rec)' failed in lock\_rec\_validate\_page
* [Revision #bcd1a08eb3](https://github.com/MariaDB/server/commit/bcd1a08eb3)\
  2017-10-13 19:40:06 +0000
  * Fix mtr to create a process dump on Window for hanging or looping processes
* [Revision #9ee840cd0a](https://github.com/MariaDB/server/commit/9ee840cd0a)\
  2017-10-13 22:22:03 +0300
  * mariadb-backup: Properly call os\_thread\_exit() with detach=true
* [Revision #d577b1a9c2](https://github.com/MariaDB/server/commit/d577b1a9c2)\
  2017-10-23 09:45:47 +0000
  * [MDEV-11934](https://jira.mariadb.org/browse/MDEV-11934): MariaRocks: Group Commit with binlog
* [Revision #4995091c33](https://github.com/MariaDB/server/commit/4995091c33)\
  2017-10-20 14:15:37 +0000
  * Temporarily disable rocksdb.rpl\_ddl\_high\_priority test
* [Revision #cd7fa0fd62](https://github.com/MariaDB/server/commit/cd7fa0fd62)\
  2017-10-17 12:04:53 +0300
  * [MDEV-11934](https://jira.mariadb.org/browse/MDEV-11934): MariaRocks: Group Commit with binlog
* Merge [Revision #f11eaaa3f6](https://github.com/MariaDB/server/commit/f11eaaa3f6) 2017-10-13 14:37:04 +0300 - Merge branch 'bb-10.2-mariarocks' of github.com:MariaDB/server into 10.2
* [Revision #c52ffbeba9](https://github.com/MariaDB/server/commit/c52ffbeba9)\
  2017-08-18 16:26:12 +0300
  * Remove garbage code
* [Revision #575afea786](https://github.com/MariaDB/server/commit/575afea786)\
  2017-08-18 16:22:05 +0300
  * MyRocks: Remove todo-#ifdef in Rdb\_trx\_info\_aggregator::process\_tran
* [Revision #fba53e7775](https://github.com/MariaDB/server/commit/fba53e7775)\
  2017-08-18 15:42:58 +0300
  * Make MyRocks test stable: Data\_length may vary slightly as well
* [Revision #765519694d](https://github.com/MariaDB/server/commit/765519694d)\
  2017-08-17 22:59:41 +0300
  * Enable basic XA between MyRocks and the binlog
* Merge [Revision #0507b09402](https://github.com/MariaDB/server/commit/0507b09402) 2017-10-13 13:25:46 +0300 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mariarocks-merge
* [Revision #a4fa940bad](https://github.com/MariaDB/server/commit/a4fa940bad)\
  2017-10-12 12:56:20 +0300
  * [MDEV-11336](https://jira.mariadb.org/browse/MDEV-11336): Enable defragmentation on 10.2 when tests pass
* [Revision #4c9d19ee65](https://github.com/MariaDB/server/commit/4c9d19ee65)\
  2017-10-11 08:37:35 -0700
  * Fixed the bug [MDEV-13796](https://jira.mariadb.org/browse/MDEV-13796).
* [Revision #dc8ac122bb](https://github.com/MariaDB/server/commit/dc8ac122bb)\
  2017-10-11 21:51:09 +0530
  * [MDEV-13928](https://jira.mariadb.org/browse/MDEV-13928): Missing symbols building RocksDB on macOS 10.12.6
* [Revision #3062445a64](https://github.com/MariaDB/server/commit/3062445a64)\
  2017-10-11 18:13:44 +0400
  * [MDEV-14038](https://jira.mariadb.org/browse/MDEV-14038) ALTER TABLE does not exit on error with InnoDB + bad default function
* [Revision #f9066dc347](https://github.com/MariaDB/server/commit/f9066dc347)\
  2017-10-10 21:49:09 +0200
  * [MDEV-14023](https://jira.mariadb.org/browse/MDEV-14023) 10.1 InnoDB tables with virtual columns cannot be accessed in 10.2
* [Revision #18a979df6f](https://github.com/MariaDB/server/commit/18a979df6f)\
  2017-10-11 11:52:25 +0300
  * Fix a warning about unused variable
* [Revision #a0df2693a2](https://github.com/MariaDB/server/commit/a0df2693a2)\
  2017-10-11 11:41:31 +0300
  * Remove an unused parameter
* [Revision #8e255b98ab](https://github.com/MariaDB/server/commit/8e255b98ab)\
  2017-10-11 12:21:40 +0400
  * [MDEV-13923](https://jira.mariadb.org/browse/MDEV-13923) Assertion \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed upon altering table with geometry field.
* [Revision #fe0d2e1a2b](https://github.com/MariaDB/server/commit/fe0d2e1a2b)\
  2017-10-11 11:57:26 +0400
  * [MDEV-13923](https://jira.mariadb.org/browse/MDEV-13923) Assertion \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed upon altering table with geometry field.
* [Revision #dd85ec6f28](https://github.com/MariaDB/server/commit/dd85ec6f28)\
  2017-10-11 08:45:59 +0200
  * Update AWS C++ SDK version
* [Revision #93690b96e2](https://github.com/MariaDB/server/commit/93690b96e2)\
  2017-10-11 08:44:24 +0200
  * Fix warnings in Win64
* [Revision #daabb4d055](https://github.com/MariaDB/server/commit/daabb4d055)\
  2017-10-11 08:36:04 +0200
  * Fix truncation warnings in connect
* [Revision #4de344a8d7](https://github.com/MariaDB/server/commit/4de344a8d7)\
  2017-10-10 19:04:54 +0300
  * Reapply a MySQL 5.6.23/5.7.10 Oracle Bug#20029625 fix that was inadvertently reverted in [MariaDB 10.2.2](../../old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md)
* [Revision #ac2ae901e8](https://github.com/MariaDB/server/commit/ac2ae901e8)\
  2017-10-10 23:56:13 +0530
  * [MDEV-13974](https://jira.mariadb.org/browse/MDEV-13974): Build failure in rocksdb/rdb\_datadic.cc
* [Revision #f2a0fa8685](https://github.com/MariaDB/server/commit/f2a0fa8685)\
  2017-10-10 16:53:15 +0300
  * Fix test failure on galera.view caused by incorrect location
* [Revision #1b478a7aba](https://github.com/MariaDB/server/commit/1b478a7aba)\
  2017-10-10 10:28:54 +0300
  * [MDEV-13311](https://jira.mariadb.org/browse/MDEV-13311) Presence of old logs in 10.2.7 will corrupt restored instance (change in behavior)
* [Revision #dc93ce8dea](https://github.com/MariaDB/server/commit/dc93ce8dea)\
  2017-10-09 19:53:27 +0000
  * Windows : Fix truncation warnings in sql/
* [Revision #fa7a1a57d9](https://github.com/MariaDB/server/commit/fa7a1a57d9)\
  2017-10-09 17:41:20 +0000
  * Windows : small optimization in os\_is\_sparse\_file\_supported()
* [Revision #ff2d9e125f](https://github.com/MariaDB/server/commit/ff2d9e125f)\
  2017-10-09 12:13:05 +0000
  * [MDEV-13941](https://jira.mariadb.org/browse/MDEV-13941) followup.
* [Revision #fe18e6b064](https://github.com/MariaDB/server/commit/fe18e6b064)\
  2017-10-08 22:05:54 +0000
  * [MDEV-13822](https://jira.mariadb.org/browse/MDEV-13822) mariadb-backup incremental prepare incorrectly sets file size. [MDEV-13310](https://jira.mariadb.org/browse/MDEV-13310) Preparing an incremental backup twice can corrupt data
* [Revision #b731a5bcf2](https://github.com/MariaDB/server/commit/b731a5bcf2)\
  2017-10-08 00:13:05 +0000
  * Innodb : Refactor os\_file\_set\_size() to be compatible 10.1
* [Revision #0b5a5258ab](https://github.com/MariaDB/server/commit/0b5a5258ab)\
  2017-10-06 09:49:42 +0300
  * MW-416 DDL replication moved after acl checking
* [Revision #70c23321de](https://github.com/MariaDB/server/commit/70c23321de)\
  2017-10-04 22:47:59 +0300
  * MW-416
* [Revision #1841ef1c54](https://github.com/MariaDB/server/commit/1841ef1c54)\
  2017-10-03 23:37:02 +0300
  * MW-416
* [Revision #e1d9a23797](https://github.com/MariaDB/server/commit/e1d9a23797)\
  2017-10-09 15:05:17 +0300
  * [MDEV-14023](https://jira.mariadb.org/browse/MDEV-14023) 10.1 InnoDB tables with virtual columns cannot be accessed in 10.2
* [Revision #3edd007cea](https://github.com/MariaDB/server/commit/3edd007cea)\
  2017-10-09 14:08:46 +0300
  * btr\_free\_root(): Relax a too strict debug assertion
* Merge [Revision #da05d0276a](https://github.com/MariaDB/server/commit/da05d0276a) 2017-10-07 17:43:26 +0000 - merge 10.1->10.2
* Merge [Revision #01e656a685](https://github.com/MariaDB/server/commit/01e656a685) 2017-10-07 08:46:37 +0000 - Merge branch 'bb-10.1-wlad' into 10.1
* [Revision #bb3f4fbb59](https://github.com/MariaDB/server/commit/bb3f4fbb59)\
  2017-10-07 07:36:17 +0000
  * [MDEV-13310](https://jira.mariadb.org/browse/MDEV-13310) Preparing an incremental backup twice can corrupt data
* [Revision #8d1fb47e1d](https://github.com/MariaDB/server/commit/8d1fb47e1d)\
  2017-10-06 22:40:28 +0000
  * [MDEV-13798](https://jira.mariadb.org/browse/MDEV-13798) - fix incorrect alignment of the buffer in incremental backup
* [Revision #0f8295d7d5](https://github.com/MariaDB/server/commit/0f8295d7d5)\
  2017-10-06 22:34:51 +0000
  * [MDEV-13822](https://jira.mariadb.org/browse/MDEV-13822) mariadb-backup incremental prepare incorrectly sets file size.
* [Revision #420798a81a](https://github.com/MariaDB/server/commit/420798a81a)\
  2017-10-06 16:36:40 +0000
  * Refactor os\_file\_set\_size to extend already existing files.
* [Revision #0373e05a59](https://github.com/MariaDB/server/commit/0373e05a59)\
  2017-10-05 18:38:29 +0000
  * Refactor os\_file\_set\_size() so it can be used to extend existing file, not just for creating new files.
* [Revision #f9b50c0657](https://github.com/MariaDB/server/commit/f9b50c0657)\
  2017-10-06 17:51:29 +0300
  * [MDEV-13512](https://jira.mariadb.org/browse/MDEV-13512) buf\_flush\_update\_zip\_checksum() corrupts SPATIAL INDEX in ROW\_FORMAT=COMPRESSED tables
* [Revision #1cfaafafee](https://github.com/MariaDB/server/commit/1cfaafafee)\
  2017-10-05 13:41:16 +0400
  * [MDEV-13242](https://jira.mariadb.org/browse/MDEV-13242) Wrong results for queries with row constructors and information\_schema
* [Revision #ea4e8bab32](https://github.com/MariaDB/server/commit/ea4e8bab32)\
  2017-10-07 14:17:45 +0400
  * [MDEV-12705](https://jira.mariadb.org/browse/MDEV-12705) 10.1.18-MariaDB-1jessie - mysqld got signal 11.
* [Revision #8f6266e927](https://github.com/MariaDB/server/commit/8f6266e927)\
  2017-10-11 14:41:09 +0300
  * [MDEV-13852](https://jira.mariadb.org/browse/MDEV-13852): temporarily disable running tests on windows
* [Revision #d1eee0407f](https://github.com/MariaDB/server/commit/d1eee0407f)\
  2017-10-09 13:35:43 +0300
  * Temporarily disable tests that rely on FB-only features
* [Revision #f62f9d661a](https://github.com/MariaDB/server/commit/f62f9d661a)\
  2017-10-09 13:29:09 +0300
  * Fix rocksdb.perf\_context test
* [Revision #6ff8d57128](https://github.com/MariaDB/server/commit/6ff8d57128)\
  2017-10-09 12:56:31 +0300
  * Fix mege error in rocksdb.use\_direct\_reads\_writes test
* [Revision #1b79437c7d](https://github.com/MariaDB/server/commit/1b79437c7d)\
  2017-10-07 13:18:13 +0300
  * Post-merge fix: put back UTF-8 text that kdiff3 destroyed
* Merge [Revision #70af9cf5ed](https://github.com/MariaDB/server/commit/70af9cf5ed) 2017-10-06 18:27:39 +0300 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mariarocks-merge
* [Revision #a659291e85](https://github.com/MariaDB/server/commit/a659291e85)\
  2017-10-06 13:25:20 +0400
  * [MDEV-11586](https://jira.mariadb.org/browse/MDEV-11586) UNION of FLOAT type results in erroneous precision
* [Revision #3557de68d1](https://github.com/MariaDB/server/commit/3557de68d1)\
  2017-10-06 10:01:35 +0400
  * [MDEV-12312](https://jira.mariadb.org/browse/MDEV-12312) JSON\_CONTAINS\_PATH does not detect invalid path and returns TRUE.
* [Revision #a3ba8c3660](https://github.com/MariaDB/server/commit/a3ba8c3660)\
  2017-10-06 09:28:33 +0400
  * [MDEV-13703](https://jira.mariadb.org/browse/MDEV-13703) Illegal mix of collations for operation 'json\_object' on using JSON\_UNQUOTE as an argument.
* [Revision #41e581b30b](https://github.com/MariaDB/server/commit/41e581b30b)\
  2017-10-05 14:08:06 +0300
  * ha\_innobase::open(): Simplify a consistency check
* [Revision #f1a20ec396](https://github.com/MariaDB/server/commit/f1a20ec396)\
  2017-10-05 23:46:25 +0400
  * [MDEV-12311](https://jira.mariadb.org/browse/MDEV-12311) Insufficient check for argument validity in JSON functions.
* [Revision #1f6ada8da8](https://github.com/MariaDB/server/commit/1f6ada8da8)\
  2017-10-05 23:23:39 +0400
  * [MDEV-13306](https://jira.mariadb.org/browse/MDEV-13306) JSON\_CONTAINS returns wrong value.
* Merge [Revision #08c493c62a](https://github.com/MariaDB/server/commit/08c493c62a) 2017-10-04 18:36:58 +0200 - Merge branch '10.1' into 10.2
* [Revision #bcda03b4fa](https://github.com/MariaDB/server/commit/bcda03b4fa)\
  2017-10-02 13:30:48 +0530
  * [MDEV-13950](https://jira.mariadb.org/browse/MDEV-13950) mysqld\_safe could not start Galera node after upgrade ...
* [Revision #8898c1614d](https://github.com/MariaDB/server/commit/8898c1614d)\
  2017-10-04 18:32:45 +0200
  * cleanup: remove test include file, clarify the comment
* [Revision #a62ebf2590](https://github.com/MariaDB/server/commit/a62ebf2590)\
  2017-09-29 10:51:00 +0200
  * cppcheck harmless warnings
* [Revision #ebda6e958f](https://github.com/MariaDB/server/commit/ebda6e958f)\
  2017-09-28 20:28:01 +0200
  * enable MongoDB support in CONNECT
* [Revision #6ca35c1428](https://github.com/MariaDB/server/commit/6ca35c1428)\
  2017-10-04 08:07:41 +0300
  * Replace a non-ASCII character in a comment
* [Revision #8d413c32dc](https://github.com/MariaDB/server/commit/8d413c32dc)\
  2017-10-03 19:43:43 +0000
  * Fix several truncation and formatting warnings.
* [Revision #4732767981](https://github.com/MariaDB/server/commit/4732767981)\
  2017-10-03 19:42:16 +0000
  * Fix Windows warnings : fix server\_audit not to use my\_win\_open and Co functions.
* [Revision #35a4591e12](https://github.com/MariaDB/server/commit/35a4591e12)\
  2017-10-03 19:38:28 +0000
  * Update C/C
* [Revision #b716231238](https://github.com/MariaDB/server/commit/b716231238)\
  2017-10-03 20:14:18 +0300
  * [MDEV-13901](https://jira.mariadb.org/browse/MDEV-13901) Assertion \`!space->stop\_new\_ops' failed in TRUNCATE TABLE with many indexes
* [Revision #ebc2f0dad3](https://github.com/MariaDB/server/commit/ebc2f0dad3)\
  2017-10-03 16:05:24 +0300
  * Avoid using HA\_POS\_ERROR constant when passing around values of type double.
* Merge [Revision #325e071c11](https://github.com/MariaDB/server/commit/325e071c11) 2017-10-03 15:52:27 +0300 - Merge pull request #457 from smtalk/10.2
* [Revision #36ef89c999](https://github.com/MariaDB/server/commit/36ef89c999)\
  2017-10-01 15:45:51 +0200
  * wrep\_sst\_common: Setting "-c ''" for my\_print\_defaults just takes no values from config at all. $MY\_PRINT\_DEFAULTS is already set at the top of the script to have --defaults-file and --defaults-extra-file. If WSREP\_SST\_OPT\_CONF if set to "--defaults-file=/etc/my.cnf --defaults-extra-file=/etc/my.extra.cnf", then "my\_print\_defaults -c "" --defaults-file=/etc/my.cnf" succeeds, but if WSREP\_SST\_OPT\_CONF is empty - no default values are taken at all. wsrep\_sst\_xtrabackup-v2: innobackupex does not support --defaults-extra-file, so ${WSREP\_SST\_OPT\_CONF} cannot be used as an argument, it has been changed to ${WSREP\_SST\_OPT\_DEFAULT}. Removed --defaults-file= from INNOMOVE line, because WSREP\_SST\_OPT\_CONF already includes it (INNOBACKUP was fine, INNOMOVE - not).
* [Revision #770231f355](https://github.com/MariaDB/server/commit/770231f355)\
  2017-10-03 11:37:38 +0300
  * Remove dict\_disable\_redo\_if\_temporary()
* [Revision #387bdf07ae](https://github.com/MariaDB/server/commit/387bdf07ae)\
  2017-10-02 10:10:02 +0300
  * Remove MYSQL\_REPLACE\_TRX\_IN\_THD
* [Revision #cc3057fde7](https://github.com/MariaDB/server/commit/cc3057fde7)\
  2017-10-02 11:43:30 +0300
  * Remove dict\_table\_t::big\_rows
* [Revision #d6f857ddbc](https://github.com/MariaDB/server/commit/d6f857ddbc)\
  2017-10-02 11:27:53 +0300
  * Remove a constant parameter commit=false
* Merge [Revision #3c4cff3357](https://github.com/MariaDB/server/commit/3c4cff3357) 2017-10-02 11:12:19 +0300 - Merge 10.1 into 10.2
* Merge [Revision #ac0b5a2e79](https://github.com/MariaDB/server/commit/ac0b5a2e79) 2017-10-02 10:45:55 +0300 - Merge 10.0 into 10.1
* Merge [Revision #de4a00d4f7](https://github.com/MariaDB/server/commit/de4a00d4f7) 2017-10-02 10:42:55 +0300 - Merge 5.5 into 10.0
* [Revision #028d253dd7](https://github.com/MariaDB/server/commit/028d253dd7)\
  2017-10-02 10:22:42 +0300
  * [MDEV-13980](https://jira.mariadb.org/browse/MDEV-13980) InnoDB fails to discard record lock when discarding an index page
* [Revision #a47d16907d](https://github.com/MariaDB/server/commit/a47d16907d)\
  2017-09-19 13:08:24 +0400
  * [MDEV-13137](https://jira.mariadb.org/browse/MDEV-13137) MySQL 5.6.23 Crashes when SET GLOBAL server\_audit\_logging=OFF;
* [Revision #b8488e5cf5](https://github.com/MariaDB/server/commit/b8488e5cf5)\
  2017-09-29 14:12:38 +0300
  * [MDEV-13932](https://jira.mariadb.org/browse/MDEV-13932): fil0pagecompress.cc fails to compile with lzo 2.10
* [Revision #4d01dd79a1](https://github.com/MariaDB/server/commit/4d01dd79a1)\
  2017-09-28 12:38:51 +0300
  * [MDEV-12634](https://jira.mariadb.org/browse/MDEV-12634): Uninitialised ROW\_MERGE\_RESERVE\_SIZE bytes written to temporary file
* [Revision #4aeec7275f](https://github.com/MariaDB/server/commit/4aeec7275f)\
  2017-09-27 18:27:39 -0400
  * bump the VERSION
* [Revision #76953c0e45](https://github.com/MariaDB/server/commit/76953c0e45)\
  2017-10-02 10:03:47 +0300
  * Remove remaining InnoDB references to the TABLESPACE keyword
* [Revision #157d130a87](https://github.com/MariaDB/server/commit/157d130a87)\
  2017-09-29 20:14:03 +0000
  * Fix some conversion warnings.
* [Revision #298c56cd6a](https://github.com/MariaDB/server/commit/298c56cd6a)\
  2017-09-29 18:15:57 +0000
  * Fix "ib::fatal::fatal': destructor never returns, potential memory leak" warning
* [Revision #a3835fad0c](https://github.com/MariaDB/server/commit/a3835fad0c)\
  2017-09-29 18:15:20 +0000
  * Correct definition of ATTRIBUTE\_NORETURN on Windows.
* [Revision #96b9c61787](https://github.com/MariaDB/server/commit/96b9c61787)\
  2017-09-29 17:29:21 +0000
  * [MDEV-13941](https://jira.mariadb.org/browse/MDEV-13941) Fix high NTFS fragmentation on 10.2
* [Revision #24d9664ad0](https://github.com/MariaDB/server/commit/24d9664ad0)\
  2017-09-29 16:44:53 +0000
  * In table cache code, fix casts from longlong to long for 'version' variables.
* [Revision #8e8a7f85a9](https://github.com/MariaDB/server/commit/8e8a7f85a9)\
  2017-09-29 17:12:14 +0000
  * Fix DBUG\_PRINT formatting in query cache.
* [Revision #7cd4a66de6](https://github.com/MariaDB/server/commit/7cd4a66de6)\
  2017-09-29 16:19:28 +0300
  * Remove unused parameters and dead code
* [Revision #358ab5d6b1](https://github.com/MariaDB/server/commit/358ab5d6b1)\
  2017-09-29 15:42:25 +0300
  * Remove remaining references to InnoDB native partitioning
* [Revision #ccf21c9962](https://github.com/MariaDB/server/commit/ccf21c9962)\
  2017-09-28 12:21:16 +0000
  * fix some conversion warnings
* [Revision #7354dc6773](https://github.com/MariaDB/server/commit/7354dc6773)\
  2017-09-28 10:38:02 +0000
  * [MDEV-13384](https://jira.mariadb.org/browse/MDEV-13384) - misc Windows warnings fixed
* [Revision #509928718d](https://github.com/MariaDB/server/commit/509928718d)\
  2017-09-28 10:36:00 +0000
  * [MDEV-13384](https://jira.mariadb.org/browse/MDEV-13384) Fix Windows warnings. thd\_alloc functions now use size\_t parameters
* [Revision #eba44874ca](https://github.com/MariaDB/server/commit/eba44874ca)\
  2017-09-19 17:45:17 +0000
  * [MDEV-13844](https://jira.mariadb.org/browse/MDEV-13844) : Fix Windows warnings. Fix DBUG\_PRINT.
* [Revision #de7c2e5e54](https://github.com/MariaDB/server/commit/de7c2e5e54)\
  2017-09-28 15:12:00 +0300
  * Avoid implicit conversion from unsigned to signed
* [Revision #5a0cd753be](https://github.com/MariaDB/server/commit/5a0cd753be)\
  2017-09-28 11:59:28 +0300
  * Added missing test if table is transactional or not in Aria
* [Revision #8d006b9b12](https://github.com/MariaDB/server/commit/8d006b9b12)\
  2017-09-27 18:25:32 -0400
  * bump the VERSION
* [Revision #06f7a7620f](https://github.com/MariaDB/server/commit/06f7a7620f)\
  2017-09-26 21:51:10 +0300
  * Fixed compiler warning
* [Revision #2fdbe15032](https://github.com/MariaDB/server/commit/2fdbe15032)\
  2017-09-27 22:19:26 +0300
  * Correct test output after variable comment change
* [Revision #c6e8d66e59](https://github.com/MariaDB/server/commit/c6e8d66e59)\
  2017-09-27 17:55:48 +0000
  * Fix buildbot error on windows.
* [Revision #fd2c5d19d0](https://github.com/MariaDB/server/commit/fd2c5d19d0)\
  2017-09-26 15:35:34 +0300
  * fix a data race
* [Revision #a02b81daea](https://github.com/MariaDB/server/commit/a02b81daea)\
  2017-09-26 00:12:36 +0300
  * Moved autosetting of host\_cache\_size and back\_log to proper place
* [Revision #742263df4f](https://github.com/MariaDB/server/commit/742263df4f)\
  2017-09-25 17:24:52 +0300
  * [MDEV-13256](https://jira.mariadb.org/browse/MDEV-13256) innodb.truncate\_debug fails in buildbot
* Merge [Revision #7dcb8816a1](https://github.com/MariaDB/server/commit/7dcb8816a1) 2017-09-25 13:46:54 +0300 - Merge 10.1 into 10.2
* [Revision #8acb2b7b28](https://github.com/MariaDB/server/commit/8acb2b7b28)\
  2017-09-22 23:20:28 -0400
  * README.md - Secure (HTTPS) Links
* [Revision #262d7e4c09](https://github.com/MariaDB/server/commit/262d7e4c09)\
  2017-09-19 17:20:36 +0300
  * Post-merge test fixes part #3.
* [Revision #da9c385fd6](https://github.com/MariaDB/server/commit/da9c385fd6)\
  2017-09-19 17:00:54 +0300
  * Post-merge test fixes part #2.
* [Revision #f321f0823b](https://github.com/MariaDB/server/commit/f321f0823b)\
  2017-09-19 16:15:08 +0300
  * Post-merge fixes part #1.
* Merge [Revision #6b0588018a](https://github.com/MariaDB/server/commit/6b0588018a) 2017-09-19 15:34:38 +0300 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mariarocks-merge
* [Revision #a2d2866e80](https://github.com/MariaDB/server/commit/a2d2866e80)\
  2017-09-19 14:28:30 +0300
  * Post-merge fix for compilation on Windows
* Merge [Revision #ba3209e219](https://github.com/MariaDB/server/commit/ba3209e219) 2017-09-18 14:06:01 +0300 - Merge mergetrees/merge-myrocks into bb-10.2-mariarocks-merge
* [Revision #3fae64b196](https://github.com/MariaDB/server/commit/3fae64b196)\
  2017-09-15 10:04:49 +0000
  * Copy of commit 184a4a2d82f4f6f3cbcb1015bcdb32bebe73315c Author: Abhinav Sharma [abhinavsharma@fb.com](mailto:abhinavsharma@fb.com) Date: Thu Sep 14 11:40:08 2017 -0700

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
