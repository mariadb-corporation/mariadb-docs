# MariaDB 10.1.27 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

A regression was discovered after the release of [MariaDB 10.1.27](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10127-release-notes.md). It has been pulled from the downloads system, but some mirrors may still have it. **Do not download or install this version.** Stay with [MariaDB 10.1.26](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10126-release-notes.md) until 10.1.28 is released.

[Download](https://downloads.mariadb.org/mariadb/10.1.27)[Release Notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10127-release-notes.md)[Changelog](mariadb-10127-changelog.md)[Overview of 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)

**Release date:** 25 Sep 2017

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10127-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #d8fe5fa131](https://github.com/MariaDB/server/commit/d8fe5fa131)\
  2017-09-22 17:54:23 +0300
  * Updated list of unstable tests for 10.1.27 release
* [Revision #a753caf135](https://github.com/MariaDB/server/commit/a753caf135)\
  2017-09-22 13:40:04 +0200
  * update rdiff after merge
* Merge [Revision #e0ebe3d083](https://github.com/MariaDB/server/commit/e0ebe3d083) 2017-09-22 10:31:49 +0300 - Merge 10.0 into 10.1
* [Revision #f6cb4f0a19](https://github.com/MariaDB/server/commit/f6cb4f0a19)\
  2017-09-22 10:28:14 +0300
  * [MDEV-13814](https://jira.mariadb.org/browse/MDEV-13814) Extra logging when innodb\_log\_archive=ON
* [Revision #f8a800bec8](https://github.com/MariaDB/server/commit/f8a800bec8)\
  2017-09-19 23:50:32 +0200
  * bugfix: copy timestamps correctly in INSERT...SELECT
* [Revision #f4f48e0621](https://github.com/MariaDB/server/commit/f4f48e0621)\
  2017-09-19 11:18:45 +0200
  * [MDEV-12672](https://jira.mariadb.org/browse/MDEV-12672) Replicated TIMESTAMP fields given wrong value near DST change
* [Revision #46a2917c0f](https://github.com/MariaDB/server/commit/46a2917c0f)\
  2017-09-20 00:02:06 +0200
  * [MDEV-13208](https://jira.mariadb.org/browse/MDEV-13208) Cannot import libmariadbclient.so.18 from python
* Merge [Revision #2e3a16e366](https://github.com/MariaDB/server/commit/2e3a16e366) 2017-09-21 22:02:21 +0200 - Merge branch '10.0' into 10.1
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
* [Revision #bb7a70c955](https://github.com/MariaDB/server/commit/bb7a70c955)\
  2017-09-11 17:46:56 +0530
  * [MDEV-10767](https://jira.mariadb.org/browse/MDEV-10767) /tmp/wsrep\_recovery.${RANDOM} file created in unallowed SELinux context
* Merge [Revision #c9e111202e](https://github.com/MariaDB/server/commit/c9e111202e) 2017-09-20 10:35:11 +0300 - Merge branch '10.0' into 10.1
* Merge [Revision #20d4cac6db](https://github.com/MariaDB/server/commit/20d4cac6db) 2017-09-20 10:24:31 +0300 - Merge branch 'bb-10.0-vicentiu' into 10.0
* [Revision #97c2a7354b](https://github.com/MariaDB/server/commit/97c2a7354b)\
  2017-09-19 15:55:59 +0200
  * [MDEV-13290](https://jira.mariadb.org/browse/MDEV-13290): Assertion `!is_set() || (m_status == DA_OK_BULK && is_bulk_op())' or` ! is\_set()' failed
* [Revision #389f7cdf3c](https://github.com/MariaDB/server/commit/389f7cdf3c)\
  2017-09-19 13:08:24 +0400
  * [MDEV-13137](https://jira.mariadb.org/browse/MDEV-13137) MySQL 5.6.23 Crashes when SET GLOBAL server\_audit\_logging=OFF;
* Merge [Revision #78f6f2b73b](https://github.com/MariaDB/server/commit/78f6f2b73b) 2017-09-20 10:25:51 +0300 - Merge branch 'bb-10.1-vicentiu' into 10.1
* Merge [Revision #ec6042bda0](https://github.com/MariaDB/server/commit/ec6042bda0) 2017-09-19 12:06:50 +0300 - Merge branch '10.0' into 10.1
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
* Merge [Revision #e7bb818116](https://github.com/MariaDB/server/commit/e7bb818116) 2017-09-19 00:31:15 +0300 - Merge remote-tracking branch 'merge/merge-xtradb-5.5' into 5.5
* [Revision #f534eef794](https://github.com/MariaDB/server/commit/f534eef794)\
  2017-09-19 00:25:34 +0300
  * 5.5.57-38.9
* [Revision #d947d1bf6e](https://github.com/MariaDB/server/commit/d947d1bf6e)\
  2017-08-18 13:35:40 +0300
  * Do not stop repeating a test even if some executions are skipped
* [Revision #bcc1ba9218](https://github.com/MariaDB/server/commit/bcc1ba9218)\
  2017-08-16 19:18:39 +0200
  * [MDEV-11240](https://jira.mariadb.org/browse/MDEV-11240): Server crashes in check\_view\_single\_update or Assertion \`derived->table' failed in mysql\_derived\_merge\_for\_insert
* [Revision #e866e4cdbe](https://github.com/MariaDB/server/commit/e866e4cdbe)\
  2017-08-15 20:10:04 +0300
  * MTR's internal check of main.log\_tables-big failed
* [Revision #0739179857](https://github.com/MariaDB/server/commit/0739179857)\
  2017-08-08 21:13:45 +0530
  * [MDEV-13458](https://jira.mariadb.org/browse/MDEV-13458): Wrong result for aggregate function with distinct clause when the value for tmp\_table\_size is small
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
* Merge [Revision #ba0ee91077](https://github.com/MariaDB/server/commit/ba0ee91077) 2017-09-19 10:20:01 +0300 - Merge branch '10.0-galera' into 10.1
* [Revision #eba0120d8f](https://github.com/MariaDB/server/commit/eba0120d8f)\
  2017-08-31 08:27:59 +0300
  * Fix test failures on embedded server.
* [Revision #0b9437951c](https://github.com/MariaDB/server/commit/0b9437951c)\
  2017-09-20 09:56:45 +0300
  * [MDEV-13850](https://jira.mariadb.org/browse/MDEV-13850): Uninitialized variable at wsrep\_binlog.cc:455
* [Revision #99fbf3eb59](https://github.com/MariaDB/server/commit/99fbf3eb59)\
  2017-09-19 13:08:24 +0400
  * [MDEV-13137](https://jira.mariadb.org/browse/MDEV-13137) MySQL 5.6.23 Crashes when SET GLOBAL server\_audit\_logging=OFF;
* [Revision #532333ee48](https://github.com/MariaDB/server/commit/532333ee48)\
  2017-09-18 17:17:52 +0300
  * [MDEV-12893](https://jira.mariadb.org/browse/MDEV-12893) innodb.log\_data\_file\_size failed in buildbot with InnoDB: Database page corruption
* [Revision #a5ee77393f](https://github.com/MariaDB/server/commit/a5ee77393f)\
  2017-09-17 20:01:38 +0200
  * [MDEV-13157](https://jira.mariadb.org/browse/MDEV-13157) Specifying DATA DIRECTORY in tables leads to failing EXCHANGE PARTITION
* [Revision #be3490f01f](https://github.com/MariaDB/server/commit/be3490f01f)\
  2017-09-17 19:45:16 +0200
  * cleanup parts.partition\_exch\_\* tests
* [Revision #f7294f5b36](https://github.com/MariaDB/server/commit/f7294f5b36)\
  2017-09-16 20:02:12 +0200
  * [MDEV-13208](https://jira.mariadb.org/browse/MDEV-13208) Cannot import libmariadbclient.so.18 from python
* [Revision #1fce368089](https://github.com/MariaDB/server/commit/1fce368089)\
  2017-09-16 00:21:22 +0200
  * [MDEV-13636](https://jira.mariadb.org/browse/MDEV-13636) ALTER TABLE ... DELAY\_KEY\_WRITE=1 creates table copy for MyISAM table with DATA DIRECTORY/INDEX DIRECTORY options
* [Revision #7e56e9ea77](https://github.com/MariaDB/server/commit/7e56e9ea77)\
  2017-06-26 20:06:12 +0200
  * [MDEV-13650](https://jira.mariadb.org/browse/MDEV-13650) Backport fix for [MDEV-13060](https://jira.mariadb.org/browse/MDEV-13060) (crash when both AWS plugin and server\_audit are loaded) to 10.1
* [Revision #df24f8469d](https://github.com/MariaDB/server/commit/df24f8469d)\
  2017-09-18 09:05:16 +0300
  * [MDEV-12893](https://jira.mariadb.org/browse/MDEV-12893) innodb.log\_data\_file\_size failed in buildbot with InnoDB: Database page corruption
* [Revision #372dba097d](https://github.com/MariaDB/server/commit/372dba097d)\
  2017-09-17 14:13:32 +0300
  * Silence a -Wimplicit-fallthrough warning
* [Revision #d1253e19a1](https://github.com/MariaDB/server/commit/d1253e19a1)\
  2017-09-16 22:19:16 +0200
  * Fix compilation in mariadb-backup
* [Revision #836d4e74d9](https://github.com/MariaDB/server/commit/836d4e74d9)\
  2017-09-16 16:55:16 +0300
  * Write proper tests for [MDEV-12634](https://jira.mariadb.org/browse/MDEV-12634): Uninitialised ROW\_MERGE\_RESERVE\_SIZE bytes
* [Revision #f24d36ae1e](https://github.com/MariaDB/server/commit/f24d36ae1e)\
  2017-09-16 21:13:47 +0300
  * Clean up a directory to avoid a failure of another test
* [Revision #75dd3bcb4c](https://github.com/MariaDB/server/commit/75dd3bcb4c)\
  2017-09-16 15:05:22 +0300
  * Clean up after commit 93087d5fe74b0078e0b6db4233710648c79043cc
* [Revision #1d7bc3b582](https://github.com/MariaDB/server/commit/1d7bc3b582)\
  2017-09-16 09:44:52 +0000
  * Innodb : do not call fflush() in os\_get\_last\_error\_low(), if no error message was written.
* [Revision #ad17e8e518](https://github.com/MariaDB/server/commit/ad17e8e518)\
  2017-09-16 09:36:21 +0000
  * [MDEV-13821](https://jira.mariadb.org/browse/MDEV-13821) : mariadb-backup sometimes could lose ib\_logf(FATAL) messages,
* [Revision #93087d5fe7](https://github.com/MariaDB/server/commit/93087d5fe7)\
  2017-09-15 15:10:36 +0000
  * Fix some warnings
* [Revision #8c4df595b8](https://github.com/MariaDB/server/commit/8c4df595b8)\
  2017-09-16 09:53:29 +0300
  * [MDEV-13807](https://jira.mariadb.org/browse/MDEV-13807) mariadb-backup --apply-log-only does generate redo log by performing rollback and possibly other tasks
* [Revision #65d26d1f31](https://github.com/MariaDB/server/commit/65d26d1f31)\
  2017-09-15 20:59:04 +0400
  * [MDEV-10191](https://jira.mariadb.org/browse/MDEV-10191) non convertible chars convert() resulted in Null instead "?" on Windows
* [Revision #fa2701c6f7](https://github.com/MariaDB/server/commit/fa2701c6f7)\
  2017-09-14 09:23:20 +0300
  * [MDEV-12634](https://jira.mariadb.org/browse/MDEV-12634): Uninitialised ROW\_MERGE\_RESERVE\_SIZE bytes written to tem… …porary file
* Merge [Revision #112d721a74](https://github.com/MariaDB/server/commit/112d721a74) 2017-09-07 12:08:34 +0300 - Merge 10.0 into 10.1
* [Revision #d861822c4f](https://github.com/MariaDB/server/commit/d861822c4f)\
  2017-09-07 12:01:07 +0300
  * [MDEV-13253](https://jira.mariadb.org/browse/MDEV-13253) After rebuilding redo logs, InnoDB can leak data from redo log buffer
* [Revision #ee844f6c34](https://github.com/MariaDB/server/commit/ee844f6c34)\
  2017-09-07 11:59:26 +0300
  * Make the SEARCH\_ABORT logic actually work
* [Revision #3ec8268b4a](https://github.com/MariaDB/server/commit/3ec8268b4a)\
  2017-09-07 11:58:21 +0300
  * Follow-up to [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103): Do not add attribute((nonnull))
* [Revision #7008d46164](https://github.com/MariaDB/server/commit/7008d46164)\
  2017-09-06 16:13:20 +0300
  * Follow-up to [MDEV-13227](https://jira.mariadb.org/browse/MDEV-13227): Shorten the test
* [Revision #a793b7fd8b](https://github.com/MariaDB/server/commit/a793b7fd8b)\
  2017-09-06 15:57:42 +0300
  * Follow-up to [MDEV-13227](https://jira.mariadb.org/browse/MDEV-13227): Do not run unnecessary test combinations
* Merge [Revision #cd694d76ce](https://github.com/MariaDB/server/commit/cd694d76ce) 2017-09-06 15:32:56 +0300 - Merge 10.0 into 10.1
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
* [Revision #17589989ee](https://github.com/MariaDB/server/commit/17589989ee)\
  2017-01-17 13:09:04 +0100
  * [MDEV-10972](https://jira.mariadb.org/browse/MDEV-10972): Insert from select / view / union -- repeatable crash in 10.1, 10.2 Linux/Mac/Windows
* Merge [Revision #be45f083e6](https://github.com/MariaDB/server/commit/be45f083e6) 2017-08-31 18:04:44 +0300 - Merge 10.0 into 10.1
* [Revision #6be93c3b8a](https://github.com/MariaDB/server/commit/6be93c3b8a)\
  2017-08-31 14:50:45 +0000
  * [MDEV-13693](https://jira.mariadb.org/browse/MDEV-13693) : Fix parameter passing to my\_error.
* [Revision #66eb9774e4](https://github.com/MariaDB/server/commit/66eb9774e4)\
  2017-08-31 12:33:46 +0000
  * [MDEV-13691](https://jira.mariadb.org/browse/MDEV-13691) : my\_write() sets inappropriate errno for ERROR\_FILE\_SYSTEM\_LIMITATON
* [Revision #38ca9be4de](https://github.com/MariaDB/server/commit/38ca9be4de)\
  2017-08-31 11:08:43 +0300
  * [MDEV-13684](https://jira.mariadb.org/browse/MDEV-13684) InnoDB race condition between fil\_crypt\_thread and btr\_scrub\_init
* [Revision #28b2896a43](https://github.com/MariaDB/server/commit/28b2896a43)\
  2017-08-31 09:15:23 +0300
  * Fixed test failure on innodb\_encryption
* [Revision #b29f26d774](https://github.com/MariaDB/server/commit/b29f26d774)\
  2017-08-31 08:27:59 +0300
  * Fix test failures on embedded server.
* [Revision #1831042279](https://github.com/MariaDB/server/commit/1831042279)\
  2017-08-30 16:55:45 +0300
  * Temporarily disable encryption.innodb\_encryption after the merge
* Merge [Revision #829752973b](https://github.com/MariaDB/server/commit/829752973b) 2017-08-30 13:06:13 +0300 - Merge branch '10.0' into 10.1
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
* [Revision #4c91fd4cd6](https://github.com/MariaDB/server/commit/4c91fd4cd6)\
  2017-08-30 12:29:17 +0300
  * Galera after-merge fixes
* Merge [Revision #01209de763](https://github.com/MariaDB/server/commit/01209de763) 2017-08-29 20:30:18 +0300 - Merge remote-tracking branch 'origin/bb-10.1-jplindst' into 10.1
* [Revision #bbfd53cd32](https://github.com/MariaDB/server/commit/bbfd53cd32)\
  2017-08-24 11:46:23 +0300
  * Add galera suite to default suites and disable failing test cases.
* Merge [Revision #efc0ec7631](https://github.com/MariaDB/server/commit/efc0ec7631) 2017-08-24 11:18:21 +0300 - Merge remote-tracking branch 'origin/bb-10.1-galera' into 10.1
* [Revision #5077cc0b1a](https://github.com/MariaDB/server/commit/5077cc0b1a)\
  2017-08-23 16:49:42 +0530
  * Fix Merge Error
* [Revision #0aeff8c36a](https://github.com/MariaDB/server/commit/0aeff8c36a)\
  2017-08-21 14:48:30 +0300
  * Fix compiler error.
* Merge [Revision #c23efc7d50](https://github.com/MariaDB/server/commit/c23efc7d50) 2017-08-21 13:35:00 +0300 - Merge remote-tracking branch 'origin/10.0-galera' into 10.1
* [Revision #f1af211499](https://github.com/MariaDB/server/commit/f1af211499)\
  2017-08-21 07:11:04 +0300
  * Add galera\_admin to disabled.
* [Revision #d20923debb](https://github.com/MariaDB/server/commit/d20923debb)\
  2017-08-20 07:49:07 +0300
  * Add more disabled test.
* [Revision #449a996c6a](https://github.com/MariaDB/server/commit/449a996c6a)\
  2017-08-19 07:52:31 +0300
  * Add more disabled tests and one ignored warning.
* [Revision #f7e1b99895](https://github.com/MariaDB/server/commit/f7e1b99895)\
  2017-08-16 13:29:38 +0300
  * Galera test fixes and add remaining test failures as disabled.
* [Revision #352d27ce36](https://github.com/MariaDB/server/commit/352d27ce36)\
  2017-08-29 14:23:34 +0300
  * [MDEV-13557](https://jira.mariadb.org/browse/MDEV-13557): Startup failure, unable to decrypt ibdata1
* [Revision #dda40b9304](https://github.com/MariaDB/server/commit/dda40b9304)\
  2017-08-28 18:28:07 +0000
  * AWS Key Management : Introduce "mock" variable, available in debug build.
* Merge [Revision #11352d52cd](https://github.com/MariaDB/server/commit/11352d52cd) 2017-08-28 15:05:46 +0300 - Merge 10.0 into 10.1
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
* [Revision #61096ff214](https://github.com/MariaDB/server/commit/61096ff214)\
  2017-08-28 09:45:54 +0300
  * [MDEV-13591](https://jira.mariadb.org/browse/MDEV-13591): InnoDB: Database page corruption on disk or a failed file read and assertion failure
* [Revision #882f4566e5](https://github.com/MariaDB/server/commit/882f4566e5)\
  2017-08-19 02:52:35 +0300
  * Combinations with innodb-undo-tablespaces to use in test files
* [Revision #97f9d3c080](https://github.com/MariaDB/server/commit/97f9d3c080)\
  2017-08-23 10:01:48 +0300
  * [MDEV-13167](https://jira.mariadb.org/browse/MDEV-13167) InnoDB key rotation is not skipping unused pages
* [Revision #a00b74d994](https://github.com/MariaDB/server/commit/a00b74d994)\
  2017-08-22 13:03:40 +0000
  * fix auth\_plugin\_win test
* [Revision #9af7561eb4](https://github.com/MariaDB/server/commit/9af7561eb4)\
  2017-08-21 17:16:12 +0000
  * [MDEV-13608](https://jira.mariadb.org/browse/MDEV-13608) : set client plugin directory with mysql\_options()
* [Revision #06106c0148](https://github.com/MariaDB/server/commit/06106c0148)\
  2017-08-17 16:13:32 +0300
  * [MDEV-12988](https://jira.mariadb.org/browse/MDEV-12988) backup fails if innodb\_undo\_tablespaces>0
* [Revision #109b858258](https://github.com/MariaDB/server/commit/109b858258)\
  2017-08-17 07:19:12 +0300
  * [MDEV-13432](https://jira.mariadb.org/browse/MDEV-13432): Assertion failure in buf0rea.cc line 577
* Merge [Revision #48fe832650](https://github.com/MariaDB/server/commit/48fe832650) 2017-08-15 09:50:31 +0200 - Merge branch '10.0' into 10.1
* [Revision #7581fb23e2](https://github.com/MariaDB/server/commit/7581fb23e2)\
  2017-08-14 18:37:53 +0200
  * compilation fix for SLES 11 SP4
* [Revision #fc556a8d94](https://github.com/MariaDB/server/commit/fc556a8d94)\
  2017-08-10 12:03:48 +0200
  * compilation fix for SLES 11 SP4
* [Revision #3e20a42bfb](https://github.com/MariaDB/server/commit/3e20a42bfb)\
  2017-08-11 13:59:53 +0400
  * [MDEV-8579](https://jira.mariadb.org/browse/MDEV-8579) - Some sysvars in I\_S are missing any meaningful help (comment) text
* [Revision #f066c89a97](https://github.com/MariaDB/server/commit/f066c89a97)\
  2017-08-10 16:02:54 +0200
  * [MDEV-8579](https://jira.mariadb.org/browse/MDEV-8579) Expand system variable documentation
* [Revision #a4c882f0e5](https://github.com/MariaDB/server/commit/a4c882f0e5)\
  2017-08-13 23:47:26 +0200
  * allow OpenSSL 0.9.8 again
* [Revision #1ff65c271f](https://github.com/MariaDB/server/commit/1ff65c271f)\
  2017-08-10 10:16:05 -0400
  * bump the VERSION
* Merge [Revision #31e794bcac](https://github.com/MariaDB/server/commit/31e794bcac) 2017-08-09 17:14:40 +0300 - Merge 10.0 into 10.1
* [Revision #cb9648a6b5](https://github.com/MariaDB/server/commit/cb9648a6b5)\
  2017-08-09 14:29:22 +0300
  * Revert an InnoDB Memcached plugin fix that was merged from MySQL 5.6.37

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
