# MariaDB 10.2.24 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.24)[Release Notes](../../old-releases/10.2/10.2.24.md)[Changelog](mariadb-10224-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 9 May 2019

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.24.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* Includes all fixes from [MariaDB 10.1.40](../changelogs-mariadb-101-series/mariadb-10140-changelog.md)
* [Revision #e0271a7b43](https://github.com/MariaDB/server/commit/e0271a7b43)\
  2019-05-08 07:01:20 +0300
  * [MDEV-19408](https://jira.mariadb.org/browse/MDEV-19408) Assertion on trx->state failed in ReadView::copy\_trx\_ids
* [Revision #49ef1c75e3](https://github.com/MariaDB/server/commit/49ef1c75e3)\
  2019-05-08 00:07:57 +0300
  * Updated list of unstable tests for 10.2.24
* [Revision #1214674b71](https://github.com/MariaDB/server/commit/1214674b71)\
  2019-05-05 22:37:58 +0800
  * [MDEV-13942](https://jira.mariadb.org/browse/MDEV-13942) InnoDB SPATIAL INDEX corruption during root page split
* [Revision #a5cfa416b4](https://github.com/MariaDB/server/commit/a5cfa416b4)\
  2019-05-06 22:31:46 +0200
  * Let us close library and only then free defaults.
* [Revision #5496df8e5d](https://github.com/MariaDB/server/commit/5496df8e5d)\
  2019-05-06 19:34:06 +0200
  * changes in innodb has influence on this test in rocksdb test suite
* Merge [Revision #633946fb63](https://github.com/MariaDB/server/commit/633946fb63) 2019-05-06 18:07:40 +0200 - Merge branch '10.1' into 10.2
* [Revision #0573744a83](https://github.com/MariaDB/server/commit/0573744a83)\
  2019-05-06 17:15:32 +0300
  * Revert "[MDEV-19399](https://jira.mariadb.org/browse/MDEV-19399) do not call slow my\_timer\_init() several times"
* [Revision #147c1239f1](https://github.com/MariaDB/server/commit/147c1239f1)\
  2019-05-06 12:12:10 +0200
  * [MDEV-17640](https://jira.mariadb.org/browse/MDEV-17640) UMASK\_DIR configuration for mysql\_install\_db is not applied to mysql database
* [Revision #c83f837053](https://github.com/MariaDB/server/commit/c83f837053)\
  2019-04-26 14:54:44 +0300
  * [MDEV-18214](https://jira.mariadb.org/browse/MDEV-18214) remove some duplicated MONITOR counters
* [Revision #8dc670a5e8](https://github.com/MariaDB/server/commit/8dc670a5e8)\
  2019-05-06 15:38:02 +0300
  * [MDEV-19399](https://jira.mariadb.org/browse/MDEV-19399) do not call slow my\_timer\_init() several times
* [Revision #15f065599e](https://github.com/MariaDB/server/commit/15f065599e)\
  2019-05-02 14:07:24 +0300
  * [MDEV-17883](https://jira.mariadb.org/browse/MDEV-17883): CREATE TABLE IF NOT EXISTS locking changes in 10.3.10
* [Revision #54d0a55adf](https://github.com/MariaDB/server/commit/54d0a55adf)\
  2019-05-05 20:06:29 +0200
  * fix of results
* Merge [Revision #ad53218a9d](https://github.com/MariaDB/server/commit/ad53218a9d) 2019-05-05 09:15:47 +0200 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #4e583a276f](https://github.com/MariaDB/server/commit/4e583a276f)\
  2019-03-25 23:58:04 +0100
  * Fixed compiler warning in connect engine
* [Revision #35bc91e24a](https://github.com/MariaDB/server/commit/35bc91e24a)\
  2019-03-24 17:32:01 +0100
  * Typo
* [Revision #fc1f3908c1](https://github.com/MariaDB/server/commit/fc1f3908c1)\
  2019-03-23 17:51:40 +0100
  * Fix [MDEV-15793](https://jira.mariadb.org/browse/MDEV-15793): Server crash in PlugCloseFile with sql\_mode='' Fixed by replacing sprinf by snprintf in ShowValue to avoid buffer overflow. It nows always use a buffer and returns int
* [Revision #d421df7ea6](https://github.com/MariaDB/server/commit/d421df7ea6)\
  2019-03-03 21:24:02 +0100
  * Fix [MDEV-18292](https://jira.mariadb.org/browse/MDEV-18292): CONNECT Engine JDBC not able to issue simple UPDATE statement from trigger or stored procedure Was not fixed when the same table was called several times with different modes. Fixed by checking if a new statement is compatible in the start\_stmt function. It nows do the same checks than external\_lock
* [Revision #dc8d1ada9f](https://github.com/MariaDB/server/commit/dc8d1ada9f)\
  2019-02-09 18:24:28 +0100
  * Fix xml result by setting eol as lf
* [Revision #ae88fe4519](https://github.com/MariaDB/server/commit/ae88fe4519)\
  2019-02-09 17:03:20 +0100
  * Fix xml result mismatch
* [Revision #58dfdfc0dd](https://github.com/MariaDB/server/commit/58dfdfc0dd)\
  2019-02-09 13:07:56 +0100
  * Fix GetTableName that returned wrong value under Windows
* [Revision #409aba76ee](https://github.com/MariaDB/server/commit/409aba76ee)\
  2019-05-04 17:06:19 +0200
  * update Connector C
* Merge [Revision #8cbb14ef5d](https://github.com/MariaDB/server/commit/8cbb14ef5d) 2019-05-04 17:04:55 +0200 - Merge branch '10.1' into 10.2
* Merge [Revision #b85aa20065](https://github.com/MariaDB/server/commit/b85aa20065) 2019-05-02 17:23:36 +0200 - Merge branch '5.5' into 10.1
* [Revision #aba9115426](https://github.com/MariaDB/server/commit/aba9115426)\
  2019-04-30 12:29:40 +0200
  * [MDEV-19349](https://jira.mariadb.org/browse/MDEV-19349) mysql\_install\_db: segfault at tmp\_file\_prefix check
* [Revision #71a748d575](https://github.com/MariaDB/server/commit/71a748d575)\
  2019-04-29 12:18:18 -0400
  * bump the VERSION
* [Revision #8cda7ab6a2](https://github.com/MariaDB/server/commit/8cda7ab6a2)\
  2019-05-02 10:17:05 -0400
  * bump the VERSION
* [Revision #ca94ce2a58](https://github.com/MariaDB/server/commit/ca94ce2a58)\
  2019-05-01 01:44:45 +0530
  * [MDEV-19352](https://jira.mariadb.org/browse/MDEV-19352): Server crash in alloc\_histograms\_for\_table\_share upon query from information schema
* [Revision #57c37e6c3f](https://github.com/MariaDB/server/commit/57c37e6c3f)\
  2019-05-01 01:19:30 +0530
  * Adjusting sql\_command to align with higher version, this is an adjustment to the patch for [MDEV-17605](https://jira.mariadb.org/browse/MDEV-17605)
* [Revision #4345868382](https://github.com/MariaDB/server/commit/4345868382)\
  2019-05-04 12:34:23 +0530
  * [MDEV-18373](https://jira.mariadb.org/browse/MDEV-18373): DENSE\_RANK is not calculated correctly
* [Revision #a6ea799651](https://github.com/MariaDB/server/commit/a6ea799651)\
  2019-05-03 17:10:51 +0530
  * [MDEV-14791](https://jira.mariadb.org/browse/MDEV-14791): Crash with order by expression containing window functions
* [Revision #e292c67bb2](https://github.com/MariaDB/server/commit/e292c67bb2)\
  2019-05-03 09:35:47 +0530
  * [MDEV-17781](https://jira.mariadb.org/browse/MDEV-17781): Server crashes in next\_linear\_tab
* [Revision #ce195987c3](https://github.com/MariaDB/server/commit/ce195987c3)\
  2019-05-03 16:47:07 +0300
  * [MDEV-19385](https://jira.mariadb.org/browse/MDEV-19385): Inconsistent definition of dtuple\_get\_nth\_v\_field()
* [Revision #3db94d2403](https://github.com/MariaDB/server/commit/3db94d2403)\
  2019-05-03 20:02:11 +0300
  * [MDEV-19346](https://jira.mariadb.org/browse/MDEV-19346): Remove dummy InnoDB log checkpoints
* [Revision #bcc1359223](https://github.com/MariaDB/server/commit/bcc1359223)\
  2019-03-16 21:06:04 +0300
  * [MDEV-17702](https://jira.mariadb.org/browse/MDEV-17702) fix unaligned access UB in sint4korr() and similar functions
* [Revision #13d7c721a5](https://github.com/MariaDB/server/commit/13d7c721a5)\
  2019-05-02 19:44:36 +0100
  * [MDEV-17008](https://jira.mariadb.org/browse/MDEV-17008) prepare with datadir, on Windows, does not set ACL on tablespace files
* [Revision #4b0f010b88](https://github.com/MariaDB/server/commit/4b0f010b88)\
  2019-05-02 14:25:24 +0100
  * [MDEV-18544](https://jira.mariadb.org/browse/MDEV-18544) "missing required privilege PROCESS on _._" using mariadb-backup for SST
* [Revision #ada1074bb1](https://github.com/MariaDB/server/commit/ada1074bb1)\
  2019-05-01 17:24:58 +0530
  * [MDEV-14398](https://jira.mariadb.org/browse/MDEV-14398) innodb\_encryption\_rotate\_key\_age=0 causes innodb\_encrypt\_tables to be ignored
* [Revision #2370eeb028](https://github.com/MariaDB/server/commit/2370eeb028)\
  2018-11-09 06:12:43 -0800
  * [MDEV-17654](https://jira.mariadb.org/browse/MDEV-17654) Incorrect syntax returned for column with CHECK constraint in the "SHOW CREATE TABLE ..." result
* [Revision #dc8e15db7e](https://github.com/MariaDB/server/commit/dc8e15db7e)\
  2018-01-02 12:00:55 +1100
  * [MDEV-15051](https://jira.mariadb.org/browse/MDEV-15051): signal handler - output information about the core generation
* [Revision #b953bf7eb2](https://github.com/MariaDB/server/commit/b953bf7eb2)\
  2019-05-01 13:14:50 +0200
  * compilation fixes for VS 2019
* [Revision #dabef66e66](https://github.com/MariaDB/server/commit/dabef66e66)\
  2019-04-29 20:32:36 +1000
  * [MDEV-19188](https://jira.mariadb.org/browse/MDEV-19188) Server Crash When Using a Trigger With A Number of Virtual Columns on INSERT/UPDATE
* [Revision #810f014ca7](https://github.com/MariaDB/server/commit/810f014ca7)\
  2019-04-29 16:23:21 +0300
  * [MDEV-18429](https://jira.mariadb.org/browse/MDEV-18429): Simpler implementation
* [Revision #092602ac9b](https://github.com/MariaDB/server/commit/092602ac9b)\
  2019-04-29 15:05:25 +0300
  * [MDEV-14130](https://jira.mariadb.org/browse/MDEV-14130) InnoDB messages should not refer to the MySQL 5.7 manual
* [Revision #5fb4c0a8a8](https://github.com/MariaDB/server/commit/5fb4c0a8a8)\
  2019-04-29 14:33:46 +0300
  * Clean up ut\_list
* [Revision #bdd6e33f00](https://github.com/MariaDB/server/commit/bdd6e33f00)\
  2019-04-29 14:05:44 +0300
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Add a test case
* [Revision #61f370a3c9](https://github.com/MariaDB/server/commit/61f370a3c9)\
  2019-04-25 20:24:10 +0300
  * [MDEV-18429](https://jira.mariadb.org/browse/MDEV-18429) Consistent non-locking reads do not appear in TRANSACTIONS section of SHOW ENGINE INNODB STATUS
* [Revision #d6e431dfa8](https://github.com/MariaDB/server/commit/d6e431dfa8)\
  2019-04-29 12:44:00 +0100
  * [MDEV-18131](https://jira.mariadb.org/browse/MDEV-18131) : Update C/C to fix IP address SAN verification in 10.2+
* [Revision #e03ad4f71a](https://github.com/MariaDB/server/commit/e03ad4f71a)\
  2019-04-24 11:44:32 +0100
  * Fix a typo
* [Revision #1b577e4d8b](https://github.com/MariaDB/server/commit/1b577e4d8b)\
  2019-04-29 11:43:22 +0300
  * [MDEV-19356](https://jira.mariadb.org/browse/MDEV-19356) Assertion 'space->free\_limit == 0 || space->free\_limit == free\_limit'
* [Revision #e10b3fa97a](https://github.com/MariaDB/server/commit/e10b3fa97a)\
  2019-04-29 10:04:54 +0300
  * [MDEV-19231](https://jira.mariadb.org/browse/MDEV-19231): Correct an assertion
* [Revision #cc359eae3b](https://github.com/MariaDB/server/commit/cc359eae3b)\
  2019-04-29 09:24:59 +0300
  * Remove a type cast, and use correct format instead
* [Revision #bb4f4b3a1b](https://github.com/MariaDB/server/commit/bb4f4b3a1b)\
  2019-04-29 02:32:13 +0400
  * Make Win compiler happy.
* [Revision #a529188e05](https://github.com/MariaDB/server/commit/a529188e05)\
  2019-04-29 01:25:17 +0400
  * [MDEV-17456](https://jira.mariadb.org/browse/MDEV-17456) Malicious SUPER user can possibly change audit log configuration without leaving traces.
* [Revision #cd26cdcd97](https://github.com/MariaDB/server/commit/cd26cdcd97)\
  2019-04-29 00:11:48 +0400
  * [MDEV-19141](https://jira.mariadb.org/browse/MDEV-19141) server\_audit\_excl\_users accepts only values with less than 1024 chars.
* [Revision #00377147e3](https://github.com/MariaDB/server/commit/00377147e3)\
  2019-04-26 23:06:07 +0400
  * Tests for [MDEV-15881](https://jira.mariadb.org/browse/MDEV-15881) Assertion \`is\_valid\_value\_slow()' failed in Datetime::Datetime or corrupt data after ALTER with indexed persistent column
* Merge [Revision #1a5ba2a4be](https://github.com/MariaDB/server/commit/1a5ba2a4be) 2019-04-26 18:19:50 +0300 - [MDEV-19342](https://jira.mariadb.org/browse/MDEV-19342) Merge new release of InnoDB 5.7.26 to 10.2
* [Revision #f3a9f12bc3](https://github.com/MariaDB/server/commit/f3a9f12bc3)\
  2019-01-25 19:51:57 +0530
  * Bug #29021730 CRASHING INNOBASE\_COL\_CHECK\_FK WITH FOREIGN KEYS
* [Revision #c795a9f3fe](https://github.com/MariaDB/server/commit/c795a9f3fe)\
  2019-04-26 10:13:29 +0300
  * [MDEV-12004](https://jira.mariadb.org/browse/MDEV-12004): Add the Bug#28825718 test case
* [Revision #06ec56f579](https://github.com/MariaDB/server/commit/06ec56f579)\
  2018-11-26 16:17:40 +0530
  * Bug #27850600 INNODB ASYNC IO ERROR HANDLING IN IO\_EVENT
* [Revision #4e9f8c9cc4](https://github.com/MariaDB/server/commit/4e9f8c9cc4)\
  2019-04-26 17:37:19 +0300
  * Remove roll\_node\_t::partial
* [Revision #793bd3ee13](https://github.com/MariaDB/server/commit/793bd3ee13)\
  2019-04-26 17:36:39 +0300
  * lock\_rec\_convert\_impl\_to\_expl\_for\_trx(): Remove unused parameter
* [Revision #1c4d1f3d05](https://github.com/MariaDB/server/commit/1c4d1f3d05)\
  2019-04-26 12:53:37 +0300
  * innobase\_col\_check\_fk(): Remove copying
* [Revision #5cfc7799a3](https://github.com/MariaDB/server/commit/5cfc7799a3)\
  2019-04-26 14:01:21 +0400
  * [MDEV-16518](https://jira.mariadb.org/browse/MDEV-16518) MYSQL57\_GENERATED\_FIELD: The code in TABLE\_SHARE::init\_from\_binary\_frm\_image() is not safe
* [Revision #9a5a86f293](https://github.com/MariaDB/server/commit/9a5a86f293)\
  2019-04-25 13:25:28 +0530
  * [MDEV-17260](https://jira.mariadb.org/browse/MDEV-17260): Memory leaks in mysqlbinlog
* [Revision #4e01bc8c96](https://github.com/MariaDB/server/commit/4e01bc8c96)\
  2018-12-20 09:52:34 +0100
  * [MDEV-16240](https://jira.mariadb.org/browse/MDEV-16240): Assertion \`0' failed in row\_sel\_convert\_mysql\_key\_to\_innobase
* [Revision #3dffdee667](https://github.com/MariaDB/server/commit/3dffdee667)\
  2019-04-25 13:43:31 +0200
  * [MDEV-17036](https://jira.mariadb.org/browse/MDEV-17036): BULK with replace doesn't take the first parameter in account
* [Revision #b2dbc781c7](https://github.com/MariaDB/server/commit/b2dbc781c7)\
  2019-04-25 17:26:23 +0300
  * Implement --debug=d,ib\_log\_checkpoint\_avoid
* [Revision #6c5c1f0b2f](https://github.com/MariaDB/server/commit/6c5c1f0b2f)\
  2019-04-25 16:29:55 +0300
  * [MDEV-19231](https://jira.mariadb.org/browse/MDEV-19231) make DB\_SUCCESS equal to 0
* Merge [Revision #bc145193c1](https://github.com/MariaDB/server/commit/bc145193c1) 2019-04-25 09:04:09 +0300 - Merge 10.1 into 10.2
* [Revision #1f1a61cfc4](https://github.com/MariaDB/server/commit/1f1a61cfc4)\
  2019-04-24 00:16:56 +0530
  * [MDEV-15837](https://jira.mariadb.org/browse/MDEV-15837): Assertion \`item1->type() == Item::FIELD\_ITEM && item2->type() == Item::FIELD\_ITEM' failed in compare\_order\_elements function
* [Revision #5fc8dd8b82](https://github.com/MariaDB/server/commit/5fc8dd8b82)\
  2019-04-23 23:10:46 -0700
  * [MDEV-17796](https://jira.mariadb.org/browse/MDEV-17796) WHERE filter is ignored by DISTINCT IFNULL(GROUP\_CONCAT(X), Y) with GROUP BY + ORDER BY
* [Revision #6b5d3c51b3](https://github.com/MariaDB/server/commit/6b5d3c51b3)\
  2019-04-23 12:44:09 +0100
  * Do fast exit with error code and FATAL ERROR message, if innodb cannot start during prepare.
* [Revision #d315b4ff39](https://github.com/MariaDB/server/commit/d315b4ff39)\
  2019-04-19 12:44:46 +0300
  * Remove IBUF\_COUNT\_DEBUG
* [Revision #169c00994b](https://github.com/MariaDB/server/commit/169c00994b)\
  2019-04-17 12:50:33 +0300
  * [MDEV-12699](https://jira.mariadb.org/browse/MDEV-12699) Improve crash recovery of corrupted data pages
* [Revision #376bf4ede5](https://github.com/MariaDB/server/commit/376bf4ede5)\
  2019-04-17 12:46:08 +0300
  * [MDEV-19241](https://jira.mariadb.org/browse/MDEV-19241) InnoDB fails to write MLOG\_INDEX\_LOAD upon completing ALTER TABLE
* [Revision #bc8d173b9f](https://github.com/MariaDB/server/commit/bc8d173b9f)\
  2019-04-15 19:17:24 +0300
  * [MDEV-14239](https://jira.mariadb.org/browse/MDEV-14239) Missing space: "innodb\_open\_files ... greaterthan"
* [Revision #4ac8fa008d](https://github.com/MariaDB/server/commit/4ac8fa008d)\
  2019-04-10 15:51:22 +0300
  * FSP\_FLAGS\_MEM\_MASK: Remove traces of ATOMIC\_WRITES
* [Revision #03dcec9a9a](https://github.com/MariaDB/server/commit/03dcec9a9a)\
  2019-04-10 10:13:42 +0300
  * Fix wsrep\_thd\_is\_applier macro to point correct function name.
* [Revision #725579c0f4](https://github.com/MariaDB/server/commit/725579c0f4)\
  2019-04-08 23:22:45 +0200
  * cmake: pass CMAKE\_BUILD\_TYPE into src.rpm
* [Revision #7362f11554](https://github.com/MariaDB/server/commit/7362f11554)\
  2019-04-08 17:06:06 +0300
  * Require --big-test for innodb.undo\_truncate\_recover
* [Revision #e7f426d2c9](https://github.com/MariaDB/server/commit/e7f426d2c9)\
  2019-04-08 15:55:09 +0300
  * [MDEV-19212](https://jira.mariadb.org/browse/MDEV-19212): Replace macros with type-safe inline functions
* [Revision #f120a15b93](https://github.com/MariaDB/server/commit/f120a15b93)\
  2019-04-08 15:36:03 +0300
  * [MDEV-19212](https://jira.mariadb.org/browse/MDEV-19212) 4GB Limit on large\_pages - integer overflow
* [Revision #caa8c20abe](https://github.com/MariaDB/server/commit/caa8c20abe)\
  2019-04-08 15:08:04 +0300
  * [MDEV-14192](https://jira.mariadb.org/browse/MDEV-14192) mariadb-backup assertion failure: byte\_offset % OS\_FILE\_LOG\_BLOCK\_SIZE == 0
* [Revision #4b822111ef](https://github.com/MariaDB/server/commit/4b822111ef)\
  2019-04-08 14:41:02 +0300
  * [MDEV-8139](https://jira.mariadb.org/browse/MDEV-8139): Clean up the freeing of B-tree pages
* [Revision #e124ff17e0](https://github.com/MariaDB/server/commit/e124ff17e0)\
  2019-04-08 10:03:46 +0200
  * cmake: force Boost dependency as needed
* [Revision #5023e465a9](https://github.com/MariaDB/server/commit/5023e465a9)\
  2019-04-07 15:49:30 +0200
  * copy-paste error fixed
* [Revision #7d720ca8de](https://github.com/MariaDB/server/commit/7d720ca8de)\
  2019-04-07 00:52:05 +0200
  * cmake: don't use generated files to detect a submodule
* [Revision #7f5849a809](https://github.com/MariaDB/server/commit/7f5849a809)\
  2019-04-07 12:05:12 +0300
  * [MDEV-18309](https://jira.mariadb.org/browse/MDEV-18309): Remove unused code
* [Revision #867617a976](https://github.com/MariaDB/server/commit/867617a976)\
  2019-04-07 10:57:38 +0300
  * [MDEV-18309](https://jira.mariadb.org/browse/MDEV-18309): InnoDB reports bogus errors about missing #sql-\*.ibd on startup
* [Revision #6b3e2ec10f](https://github.com/MariaDB/server/commit/6b3e2ec10f)\
  2019-04-07 10:13:09 +0300
  * Re-record results for MTR\_FEEDBACK\_PLUGIN=1
* [Revision #1d30b7b1d2](https://github.com/MariaDB/server/commit/1d30b7b1d2)\
  2019-04-06 21:23:01 +0300
  * [MDEV-12699](https://jira.mariadb.org/browse/MDEV-12699) preparation: Clean up recv\_sys
* [Revision #aa3f7a107c](https://github.com/MariaDB/server/commit/aa3f7a107c)\
  2019-04-05 15:38:26 +0300
  * [MDEV-12699](https://jira.mariadb.org/browse/MDEV-12699) preparation: Write MLOG\_INDEX\_LOAD for FTS\_ tables
* [Revision #45d338dca8](https://github.com/MariaDB/server/commit/45d338dca8)\
  2019-04-02 14:49:53 +0300
  * [MDEV-12699](https://jira.mariadb.org/browse/MDEV-12699) preparation: Initialize the entire page on MLOG\_ZIP\_PAGE\_COMPRESS
* [Revision #1b95118c5f](https://github.com/MariaDB/server/commit/1b95118c5f)\
  2019-04-06 20:21:06 +0300
  * buf\_page\_get\_gen(): Allow BUF\_GET\_IF\_IN\_POOL with a dummy page\_size
* [Revision #80f29211eb](https://github.com/MariaDB/server/commit/80f29211eb)\
  2019-04-06 20:34:15 +0300
  * Fix a crash in CHECK TABLE for corrupted encrypted root page
* [Revision #1d0380e029](https://github.com/MariaDB/server/commit/1d0380e029)\
  2019-04-06 12:42:41 +0300
  * [MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528) preparation: Do not modify a freed page
* [Revision #56df18be65](https://github.com/MariaDB/server/commit/56df18be65)\
  2019-04-06 12:24:36 +0300
  * Clean up the parsing of MLOG\_INIT\_FILE\_PAGE2
* [Revision #71f9552fd8](https://github.com/MariaDB/server/commit/71f9552fd8)\
  2019-04-04 21:22:43 +0300
  * recv\_recovery\_is\_on(): Add UNIV\_UNLIKELY
* [Revision #c56ae2dfbd](https://github.com/MariaDB/server/commit/c56ae2dfbd)\
  2019-04-06 21:25:10 +0300
  * Re-record plugins.feedback\_plugin\_load
* [Revision #b4a7bde76c](https://github.com/MariaDB/server/commit/b4a7bde76c)\
  2019-04-03 22:52:29 -0700
  * [MDEV-19112](https://jira.mariadb.org/browse/MDEV-19112) WITH clause does not work with information\_schema as default database
* Merge [Revision #b30fb701cc](https://github.com/MariaDB/server/commit/b30fb701cc) 2019-04-04 09:05:45 +0300 - Merge 10.1 into 10.2
* [Revision #f602385776](https://github.com/MariaDB/server/commit/f602385776)\
  2019-04-04 08:57:53 +0300
  * Do not pass table\_name\_t to printf-like functions
* [Revision #b718ec055d](https://github.com/MariaDB/server/commit/b718ec055d)\
  2019-04-03 21:41:19 +0300
  * [MDEV-18836](https://jira.mariadb.org/browse/MDEV-18836): Adjust a suppression
* [Revision #c676de1692](https://github.com/MariaDB/server/commit/c676de1692)\
  2019-04-03 21:00:13 +0300
  * Fix the non-debug build
* Merge [Revision #28636a92ed](https://github.com/MariaDB/server/commit/28636a92ed) 2019-04-03 19:57:29 +0300 - Merge 10.1 into 10.2
* [Revision #cad56fbaba](https://github.com/MariaDB/server/commit/cad56fbaba)\
  2019-04-03 16:10:20 +0300
  * [MDEV-18733](https://jira.mariadb.org/browse/MDEV-18733) MariaDB slow start after crash recovery
* [Revision #7984ea80de](https://github.com/MariaDB/server/commit/7984ea80de)\
  2019-04-03 17:10:54 +0300
  * Remove a useless CHECK TABLE printout for debug builds
* [Revision #a1ec7ac4f4](https://github.com/MariaDB/server/commit/a1ec7ac4f4)\
  2019-04-03 15:56:28 +0300
  * Clean up table\_name\_t
* [Revision #03672a0573](https://github.com/MariaDB/server/commit/03672a0573)\
  2019-04-03 10:50:43 +0300
  * [MDEV-11487](https://jira.mariadb.org/browse/MDEV-11487): Remove dict\_table\_get\_n\_sys\_cols()
* Merge [Revision #dbc716675b](https://github.com/MariaDB/server/commit/dbc716675b) 2019-04-03 10:29:15 +0300 - Merge 10.1 into 10.2
* [Revision #e3f44d8d0e](https://github.com/MariaDB/server/commit/e3f44d8d0e)\
  2019-04-02 16:40:27 +0300
  * [MDEV-19085](https://jira.mariadb.org/browse/MDEV-19085): Remove a bogus debug assertion
* [Revision #5633f83ca4](https://github.com/MariaDB/server/commit/5633f83ca4)\
  2019-04-02 13:46:36 +0300
  * Fix integer type mismatch
* [Revision #8650848ec3](https://github.com/MariaDB/server/commit/8650848ec3)\
  2019-04-02 13:43:22 +0300
  * [MDEV-19128](https://jira.mariadb.org/browse/MDEV-19128) fil\_name\_parse() for MLOG\_FILE\_ is not portable
* Merge [Revision #bce380f2a5](https://github.com/MariaDB/server/commit/bce380f2a5) 2019-04-02 09:14:15 +0300 - Merge 10.1 into 10.2
* [Revision #d59ad6972b](https://github.com/MariaDB/server/commit/d59ad6972b)\
  2019-04-01 18:13:11 +0300
  * [MDEV-19085](https://jira.mariadb.org/browse/MDEV-19085): Fix a typo that was caught by GCC 5.4
* [Revision #f055da9b84](https://github.com/MariaDB/server/commit/f055da9b84)\
  2019-04-01 14:24:15 +0300
  * [MDEV-19085](https://jira.mariadb.org/browse/MDEV-19085) Assertion failures due to virtual columns after upgrading from 10.1
* [Revision #833071b857](https://github.com/MariaDB/server/commit/833071b857)\
  2019-04-01 12:58:51 +0300
  * Disable tests in rocksdb\_stress suite (which was enabled a few commits ago)
* [Revision #fe1dfe3928](https://github.com/MariaDB/server/commit/fe1dfe3928)\
  2019-03-30 20:00:13 +0300
  * [MDEV-19089](https://jira.mariadb.org/browse/MDEV-19089), part #2: mark rocksdb.deadlock as "big test"
* [Revision #c2d9a346ff](https://github.com/MariaDB/server/commit/c2d9a346ff)\
  2019-03-30 19:50:55 +0300
  * [MDEV-19089](https://jira.mariadb.org/browse/MDEV-19089) part #1: adapt rocksdb\_stress suite for MariaDB
* [Revision #76934212eb](https://github.com/MariaDB/server/commit/76934212eb)\
  2018-09-23 12:19:24 +0300
  * remove unneeded code
* [Revision #b66164ab56](https://github.com/MariaDB/server/commit/b66164ab56)\
  2018-08-29 13:50:52 +0300
  * remove dead code
* [Revision #65bd38204b](https://github.com/MariaDB/server/commit/65bd38204b)\
  2019-03-29 12:06:34 +0200
  * Update 10.2 man pages
* [Revision #cc71e7501c](https://github.com/MariaDB/server/commit/cc71e7501c)\
  2019-03-28 12:07:20 +0100
  * post-merge: -Werror fixes in 10.2
* Merge [Revision #f2a0c758da](https://github.com/MariaDB/server/commit/f2a0c758da) 2019-03-29 10:58:20 +0100 - Merge branch '10.1' into 10.2
* [Revision #fc168c3a5e](https://github.com/MariaDB/server/commit/fc168c3a5e)\
  2019-03-29 11:38:45 +0200
  * [MDEV-15587](https://jira.mariadb.org/browse/MDEV-15587) AES test fails, segfaults in EVP\_CipherInit\_ex
* [Revision #8fcd9478cc](https://github.com/MariaDB/server/commit/8fcd9478cc)\
  2019-03-28 15:54:42 +0300
  * [MDEV-18080](https://jira.mariadb.org/browse/MDEV-18080), part#1: MyRocks is slow with log-bin=off
* [Revision #e42192d7b3](https://github.com/MariaDB/server/commit/e42192d7b3)\
  2019-03-28 20:35:39 +0530
  * [MDEV-13895](https://jira.mariadb.org/browse/MDEV-13895): GTID and Master\_Delay causes excessive initial delay
* [Revision #05ad7fc3ed](https://github.com/MariaDB/server/commit/05ad7fc3ed)\
  2019-03-28 11:42:21 +0100
  * [MDEV-19054](https://jira.mariadb.org/browse/MDEV-19054) : mysql\_upgrade\_service now allows MySQL 5.7 to [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) upgrade.
* [Revision #0623cc7c16](https://github.com/MariaDB/server/commit/0623cc7c16)\
  2019-03-27 18:58:43 +0530
  * [MDEV-19051](https://jira.mariadb.org/browse/MDEV-19051) Avoid unnecessary writing MLOG\_INDEX\_LOAD
* [Revision #38cad6875f](https://github.com/MariaDB/server/commit/38cad6875f)\
  2019-03-28 13:14:49 +0530
  * [MDEV-18899](https://jira.mariadb.org/browse/MDEV-18899): Server crashes in Field::set\_warning\_truncated\_wrong\_value
* Merge [Revision #1e9c2b2305](https://github.com/MariaDB/server/commit/1e9c2b2305) 2019-03-27 12:26:11 +0200 - Merge 10.1 into 10.2
* Merge [Revision #c676f58c27](https://github.com/MariaDB/server/commit/c676f58c27) 2019-03-26 17:38:33 +0200 - Merge 10.1 into 10.2
* Merge [Revision #ac4934535d](https://github.com/MariaDB/server/commit/ac4934535d) 2019-03-26 14:59:32 +0200 - Merge 10.1 into 10.2
* Merge [Revision #226ca250ed](https://github.com/MariaDB/server/commit/226ca250ed) 2019-03-26 14:17:19 +0200 - Merge 10.1 into 10.2
* [Revision #b30bbb7d9a](https://github.com/MariaDB/server/commit/b30bbb7d9a)\
  2019-03-25 12:53:20 -0400
  * bump the VERSION
* [Revision #07096ada9b](https://github.com/MariaDB/server/commit/07096ada9b)\
  2019-03-25 17:15:34 +0200
  * Fix the Windows build
* [Revision #525e79b057](https://github.com/MariaDB/server/commit/525e79b057)\
  2019-03-25 16:03:24 +0200
  * [MDEV-19022](https://jira.mariadb.org/browse/MDEV-19022): InnoDB fails to cleanup useless B-tree pages
* [Revision #ade0a0e9d5](https://github.com/MariaDB/server/commit/ade0a0e9d5)\
  2019-03-25 15:55:00 +0200
  * Avoid sign mismatch in comparisons
* [Revision #1bd9815479](https://github.com/MariaDB/server/commit/1bd9815479)\
  2019-03-25 11:27:29 +0200
  * [MDEV-14126](https://jira.mariadb.org/browse/MDEV-14126): Fix type mismatch
* [Revision #72b934e3f7](https://github.com/MariaDB/server/commit/72b934e3f7)\
  2019-03-22 19:21:07 +0200
  * [MDEV-14126](https://jira.mariadb.org/browse/MDEV-14126): Detect unexpected emptying of B-tree pages
* [Revision #a4d0d6828b](https://github.com/MariaDB/server/commit/a4d0d6828b)\
  2019-03-22 19:19:34 +0200
  * [MDEV-14126](https://jira.mariadb.org/browse/MDEV-14126): Improve assertions in btr\_pcur\_store\_position()
* [Revision #b59d484696](https://github.com/MariaDB/server/commit/b59d484696)\
  2019-03-22 19:16:45 +0200
  * [MDEV-14126](https://jira.mariadb.org/browse/MDEV-14126): Remove page\_is\_root()
* [Revision #71c781bfe7](https://github.com/MariaDB/server/commit/71c781bfe7)\
  2019-03-25 10:29:25 +0200
  * [MDEV-18090](https://jira.mariadb.org/browse/MDEV-18090) Assertion failures due to virtual columns after upgrading to 10.2

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
