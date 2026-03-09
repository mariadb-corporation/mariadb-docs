# MariaDB 10.2.14 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.14)[Release Notes](../../old-releases/10.2/10.2.14.md)[Changelog](mariadb-10214-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 27 Mar 2018

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.14.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #b3cdafcb93](https://github.com/MariaDB/server/commit/b3cdafcb93)\
  2018-03-26 19:36:39 +0300
  * Updated list of unstable tests for 10.2.14
* [Revision #dcb59373d5](https://github.com/MariaDB/server/commit/dcb59373d5)\
  2018-03-26 17:36:04 +0530\
  \*
  * Fixing innodb.purge\_secondary test case failure
* [Revision #c813d9485a](https://github.com/MariaDB/server/commit/c813d9485a)\
  2018-03-26 13:37:45 +0300
  * Fix result after commit e27535093d1670fde6034c92366e8128b683b903
* [Revision #e27535093d](https://github.com/MariaDB/server/commit/e27535093d)\
  2018-03-26 15:48:27 +0530\
  \*
  * Follow-up fix to [MDEV-15229](https://jira.mariadb.org/browse/MDEV-15229)
* Merge [Revision #c764bc0a78](https://github.com/MariaDB/server/commit/c764bc0a78) 2018-03-25 13:02:52 +0200 - Merge branch '10.1' into 10.2 (see the [MariaDB 10.1.32 Changelog](../changelogs-mariadb-101-series/mariadb-10132-changelog.md) for details)
* [Revision #d702e46390](https://github.com/MariaDB/server/commit/d702e46390)\
  2018-03-25 00:15:11 +0400
  * [MDEV-15561](https://jira.mariadb.org/browse/MDEV-15561) json\_extract returns NULL with numbers in scientific notation.
* [Revision #7003067a09](https://github.com/MariaDB/server/commit/7003067a09)\
  2018-03-23 13:27:33 +0530\
  \*
  * Fixing innodb.purge\_secondary test case.
* [Revision #f249d8467a](https://github.com/MariaDB/server/commit/f249d8467a)\
  2018-03-22 15:07:33 +0100
  * [MDEV-15570](https://jira.mariadb.org/browse/MDEV-15570) Assertion \`Item\_cache\_temporal::field\_type() != MYSQL\_TYPE\_TIME' failed in Item\_cache\_temporal::val\_datetime\_packed
* [Revision #e147a4a067](https://github.com/MariaDB/server/commit/e147a4a067)\
  2018-03-22 22:47:40 +0400
  * Fixed build failure
* [Revision #1123f87b5c](https://github.com/MariaDB/server/commit/1123f87b5c)\
  2018-03-22 21:01:20 +0200
  * Fix unused variable thd warning in embedded
* [Revision #fc05777eac](https://github.com/MariaDB/server/commit/fc05777eac)\
  2018-03-22 17:56:45 +0200
  * Enable --suite=innodb\_undo
* Merge [Revision #e80a842000](https://github.com/MariaDB/server/commit/e80a842000) 2018-03-22 18:02:40 +0200 - Merge 10.1 into 10.2
* [Revision #2fb31821de](https://github.com/MariaDB/server/commit/2fb31821de)\
  2018-03-22 11:26:38 +0200
  * [MDEV-11984](https://jira.mariadb.org/browse/MDEV-11984) Avoid accessing SYS\_TABLESPACES unnecessarily
* [Revision #b98d80eb84](https://github.com/MariaDB/server/commit/b98d80eb84)\
  2018-03-22 10:58:22 +0200
  * Correct a wait condition in a disabled test
* [Revision #8d32959b09](https://github.com/MariaDB/server/commit/8d32959b09)\
  2018-01-31 20:30:46 +0300
  * fix data races
* [Revision #03a80e20f7](https://github.com/MariaDB/server/commit/03a80e20f7)\
  2018-03-21 16:15:02 +0200
  * pfs\_os\_file\_read\_no\_error\_handling\_int\_fd\_func(): Remove a variable
* Merge [Revision #3d7915f000](https://github.com/MariaDB/server/commit/3d7915f000) 2018-03-21 16:18:21 +0200 - Merge 10.1 into 10.2
* Merge [Revision #82aeb6b596](https://github.com/MariaDB/server/commit/82aeb6b596) 2018-03-21 10:36:49 +0200 - Merge branch '10.1' into 10.2
* [Revision #34b03da211](https://github.com/MariaDB/server/commit/34b03da211)\
  2018-03-18 15:11:48 +0200
  * Update Connector/C
* Merge [Revision #a0f9cbc931](https://github.com/MariaDB/server/commit/a0f9cbc931) 2018-03-18 15:05:27 +0200 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #f9cf2df077](https://github.com/MariaDB/server/commit/f9cf2df077)\
  2018-03-11 23:46:33 +0100\
  \*
  * Fix [MDEV-15429](https://jira.mariadb.org/browse/MDEV-15429) CONNECT engine JDBC handling Postgresql UUID type Also handle Postgresql sending type VARCHAR for TEXT column and setting length to b x7FFFFFF when the length is unknown. modified: storage/connect/Client.java modified: storage/connect/JavaWrappers.jar modified: storage/connect/JdbcInterface.java modified: storage/connect/PostgresqlInterface.java modified: storage/connect/global.h modified: storage/connect/ha\_connect.cc modified: storage/connect/jdbconn.cpp modified: storage/connect/jdbconn.h modified: storage/connect/mysql-test/connect/r/jdbc\_postgresql.result modified: storage/connect/mysql-test/connect/t/jdbc\_postgresql.test modified: storage/connect/mysql-test/connect/t/jdbconn.inc modified: storage/connect/plgdbsem.h modified: storage/connect/tabjdbc.cpp modified: storage/connect/tabjdbc.h
* [Revision #175ce0e7f5](https://github.com/MariaDB/server/commit/175ce0e7f5)\
  2018-02-25 14:31:28 +0100\
  \*
  * Remove warning on not used tabtyp variable in connect\_assisted\_discovery modified: storage/connect/ha\_connect.cc
* [Revision #273233119c](https://github.com/MariaDB/server/commit/273233119c)\
  2018-02-12 16:26:12 +0100\
  \*
  * Fix a bug causing CONNECT to loop when expanding a JSON column when the expanded column value is null or void array. - Adding the FullArray option to JSON tables. - Skipping expanded JSON lines when the expanded column value is null. modified: storage/connect/connect.cc modified: storage/connect/tabdos.h modified: storage/connect/tabjson.cpp modified: storage/connect/tabjson.h
* [Revision #efe80675f5](https://github.com/MariaDB/server/commit/efe80675f5)\
  2018-02-02 15:27:45 +0100\
  \*
  * Remove warning on not used tabtyp variable in connect\_assisted\_discovery modified: storage/connect/ha\_connect.cc
* [Revision #79c1df4c23](https://github.com/MariaDB/server/commit/79c1df4c23)\
  2018-01-31 01:08:52 +0100\
  \*
  * Change the connect\_xtrace variable to from int to set modified: storage/connect/ha\_connect.cc modified: storage/connect/libdoc.cpp
* [Revision #dd07e30cb0](https://github.com/MariaDB/server/commit/dd07e30cb0)\
  2018-01-30 23:30:06 +0100\
  \*
  * Change the connect\_xtrace variable to from int to set modified: storage/connect/inihandl.cpp
* [Revision #5abdd20ca9](https://github.com/MariaDB/server/commit/5abdd20ca9)\
  2018-01-30 15:43:20 +0100\
  \*
  * Use delayed load for the MongoDB C Drive on Windows modified: storage/connect/CMakeLists.txt modified: storage/connect/cmgoconn.cpp modified: storage/connect/ha\_connect.cc
* [Revision #6d1d5c3aeb](https://github.com/MariaDB/server/commit/6d1d5c3aeb)\
  2018-03-16 20:55:55 +0530
  * [MDEV-14545](https://jira.mariadb.org/browse/MDEV-14545) Backup fails due to MLOG\_INDEX\_LOAD record
* [Revision #27c54b77c1](https://github.com/MariaDB/server/commit/27c54b77c1)\
  2018-03-14 10:00:19 +0200
  * Make some locking primitives inline
* [Revision #d2a15092c1](https://github.com/MariaDB/server/commit/d2a15092c1)\
  2018-03-14 09:39:47 +0200
  * lock\_table\_create(), lock\_rec\_create(): Clean up the WSREP code
* [Revision #61e192fa40](https://github.com/MariaDB/server/commit/61e192fa40)\
  2018-03-14 09:33:38 +0200
  * lock\_reset\_lock\_and\_trx\_wait(): Remove diagnostics
* [Revision #27d4333cb9](https://github.com/MariaDB/server/commit/27d4333cb9)\
  2018-03-13 17:37:03 +0200
  * [MDEV-13935](https://jira.mariadb.org/browse/MDEV-13935) INSERT stuck at state Unlocking tables
* [Revision #f93a219c72](https://github.com/MariaDB/server/commit/f93a219c72)\
  2018-03-13 14:19:03 +0200
  * [MDEV-13935](https://jira.mariadb.org/browse/MDEV-13935) INSERT stuck at state Unlocking tables
* [Revision #cac373f533](https://github.com/MariaDB/server/commit/cac373f533)\
  2018-03-13 14:15:46 +0200
  * Add missing #ifdef WITH\_WSREP
* [Revision #788b3ee86d](https://github.com/MariaDB/server/commit/788b3ee86d)\
  2018-03-13 14:06:30 +0200
  * Reduce the diff from 5.7 in DeadlockChecker::search()
* [Revision #bd7ed1b923](https://github.com/MariaDB/server/commit/bd7ed1b923)\
  2018-03-11 23:34:23 +0200
  * [MDEV-13935](https://jira.mariadb.org/browse/MDEV-13935) INSERT stuck at state Unlocking tables
* [Revision #e15e879fae](https://github.com/MariaDB/server/commit/e15e879fae)\
  2018-03-13 11:07:34 +0200
  * Remove the unreachable error DB\_QUE\_THR\_SUSPENDED
* [Revision #84129fb1b5](https://github.com/MariaDB/server/commit/84129fb1b5)\
  2018-03-16 14:35:42 +0200
  * After-merge fix for commit 98eb9518db1da854048b09d94244a982a1d32f9a
* Merge [Revision #98eb9518db](https://github.com/MariaDB/server/commit/98eb9518db) 2018-03-16 14:12:00 +0200 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #b0c43d0c38](https://github.com/MariaDB/server/commit/b0c43d0c38)\
  2018-03-16 12:30:36 +0530
  * [MDEV-15384](https://jira.mariadb.org/browse/MDEV-15384) buf\_flush\_LRU\_list\_batch() always reports n->flushed=0, n->evicted=0 [MDEV-14545](https://jira.mariadb.org/browse/MDEV-14545) Backup fails due to MLOG\_INDEX\_LOAD record
* [Revision #d251cedd8d](https://github.com/MariaDB/server/commit/d251cedd8d)\
  2018-03-13 02:53:48 +0200
  * [MDEV-15478](https://jira.mariadb.org/browse/MDEV-15478): Lost name of a explicitly named CTE column used in the non-recursive CTE defined with UNION
* [Revision #8c8028ca68](https://github.com/MariaDB/server/commit/8c8028ca68)\
  2018-03-15 19:15:09 +0530
  * [MDEV-15384](https://jira.mariadb.org/browse/MDEV-15384) buf\_flush\_LRU\_list\_batch() always reports n->flushed=0, n->evicted=0
* Merge [Revision #be3651b700](https://github.com/MariaDB/server/commit/be3651b700) 2018-03-15 13:59:22 +0200 - Merge pull request #649 from codership/10.2-[MDEV-15540](https://jira.mariadb.org/browse/MDEV-15540)
* [Revision #c439fdc953](https://github.com/MariaDB/server/commit/c439fdc953)\
  2018-03-11 16:50:37 +0200
  * [MDEV-15540](https://jira.mariadb.org/browse/MDEV-15540)
* [Revision #27d94b7e03](https://github.com/MariaDB/server/commit/27d94b7e03)\
  2018-03-13 11:23:06 +0100
  * cleanup: remove get\_datetime\_value()
* [Revision #42529c4341](https://github.com/MariaDB/server/commit/42529c4341)\
  2018-03-12 20:35:38 +0100
  * [MDEV-15141](https://jira.mariadb.org/browse/MDEV-15141) Check constraint validation on a datetime field crashes the process
* [Revision #d390e501eb](https://github.com/MariaDB/server/commit/d390e501eb)\
  2018-03-12 20:16:33 +0100
  * [MDEV-11839](https://jira.mariadb.org/browse/MDEV-11839) move value caching from get\_datetime\_value to fix\_fields time
* [Revision #1c6f6dc892](https://github.com/MariaDB/server/commit/1c6f6dc892)\
  2018-03-12 20:15:18 +0100
  * bugfix: Item\_cache\_temporal::convert\_to\_basic\_const\_item assumed DATETIME
* [Revision #885edc4fa5](https://github.com/MariaDB/server/commit/885edc4fa5)\
  2018-03-12 20:13:55 +0100
  * bugfix: Item\_cache\_temporal::get\_date() didn't set null\_value
* [Revision #622115ee07](https://github.com/MariaDB/server/commit/622115ee07)\
  2018-03-12 20:13:36 +0100
  * cleanup: extend Item\_cache::get\_cache() to accept f\_type
* [Revision #24d6cd7d62](https://github.com/MariaDB/server/commit/24d6cd7d62)\
  2018-03-12 20:13:05 +0100
  * cleanup: Arg\_comparator::cache\_converted\_constant()
* [Revision #c2671e97a3](https://github.com/MariaDB/server/commit/c2671e97a3)\
  2018-03-12 20:08:01 +0100
  * cleanup: make find\_date\_time\_item() static
* [Revision #e0d3d4059f](https://github.com/MariaDB/server/commit/e0d3d4059f)\
  2018-03-12 20:11:33 +0100
  * cleanup: add Item::convert\_time\_to\_datetime() helper
* [Revision #75ac5789b4](https://github.com/MariaDB/server/commit/75ac5789b4)\
  2018-03-11 16:41:56 +0100
  * cleanup: typos, comments, whitespace
* [Revision #bf1ca14ff3](https://github.com/MariaDB/server/commit/bf1ca14ff3)\
  2018-03-12 18:53:59 +0100
  * cleanup: Item\_func\_case
* [Revision #c14733f64e](https://github.com/MariaDB/server/commit/c14733f64e)\
  2018-03-14 11:57:05 +0530
  * [MDEV-14545](https://jira.mariadb.org/browse/MDEV-14545) Backup fails due to MLOG\_INDEX\_LOAD record
* Merge [Revision #e452546c45](https://github.com/MariaDB/server/commit/e452546c45) 2018-03-13 16:40:14 -0700 - Merge branch 'bb-10.2-[MDEV-14019](https://jira.mariadb.org/browse/MDEV-14019)' into 10.2
* Merge [Revision #1b82bec3c9](https://github.com/MariaDB/server/commit/1b82bec3c9) 2018-03-13 16:15:37 -0700 - Merge branch '10.2' into bb-10.2-[MDEV-14019](https://jira.mariadb.org/browse/MDEV-14019)
* [Revision #90247658e0](https://github.com/MariaDB/server/commit/90247658e0)\
  2018-03-09 19:14:20 -0800
  * [MDEV-14019](https://jira.mariadb.org/browse/MDEV-14019): Spider + binlog\_format = ROW => CRASH
* [Revision #649b7a64ef](https://github.com/MariaDB/server/commit/649b7a64ef)\
  2018-03-13 14:42:15 +0400
  * [MDEV-9592](https://jira.mariadb.org/browse/MDEV-9592) - New 'Normal shutdown' log format can be confusing
* [Revision #30019a48bf](https://github.com/MariaDB/server/commit/30019a48bf)\
  2018-02-09 15:00:23 +0200
  * [MDEV-12746](https://jira.mariadb.org/browse/MDEV-12746) rpl.rpl\_parallel\_optimistic\_nobinlog fails committing out of order at retry
* [Revision #76ae6e725d](https://github.com/MariaDB/server/commit/76ae6e725d)\
  2018-03-13 15:20:00 +0530
  * [MDEV-15384](https://jira.mariadb.org/browse/MDEV-15384) buf\_flush\_LRU\_list\_batch() always reports n->flushed=0, n->evicted=0
* [Revision #ff909acfa4](https://github.com/MariaDB/server/commit/ff909acfa4)\
  2018-03-13 15:19:30 +0530
  * [MDEV-14545](https://jira.mariadb.org/browse/MDEV-14545) Backup fails due to MLOG\_INDEX\_LOAD record
* Merge [Revision #94e00da9f1](https://github.com/MariaDB/server/commit/94e00da9f1) 2018-03-13 09:43:13 +0200 - Merge 10.1 into 10.2
* [Revision #71f9cc1221](https://github.com/MariaDB/server/commit/71f9cc1221)\
  2018-03-13 09:35:37 +0200
  * [MDEV-15554](https://jira.mariadb.org/browse/MDEV-15554) InnoDB page\_cleaner shutdown sometimes hangs
* [Revision #9d95b8665a](https://github.com/MariaDB/server/commit/9d95b8665a)\
  2018-03-12 23:43:42 +0400
  * [MDEV-15217](https://jira.mariadb.org/browse/MDEV-15217) Assertion \`thd->transaction.xid\_state.xid.is\_null()' failed in trans\_xa\_start.
* [Revision #68482a2215](https://github.com/MariaDB/server/commit/68482a2215)\
  2018-03-12 18:38:40 +0000
  * [MDEV-14581](https://jira.mariadb.org/browse/MDEV-14581) - changded .result file
* [Revision #248e5d01a5](https://github.com/MariaDB/server/commit/248e5d01a5)\
  2018-03-12 18:29:31 +0000
  * [MDEV-14581](https://jira.mariadb.org/browse/MDEV-14581) Warning info not cleared when caching THD
* [Revision #5511e8ed59](https://github.com/MariaDB/server/commit/5511e8ed59)\
  2018-03-05 17:43:30 +0100
  * [MDEV-15328](https://jira.mariadb.org/browse/MDEV-15328): [MariaDB 10.2.13](../../old-releases/10.2/10.2.13.md) Crashes upon CALL PROCEDURE PARAM LAST\_INSERT\_ID ()
* Merge [Revision #3a93ec53c1](https://github.com/MariaDB/server/commit/3a93ec53c1) 2018-03-12 14:27:17 +0200 - Merge 10.1 into 10.2
* [Revision #cd109592ca](https://github.com/MariaDB/server/commit/cd109592ca)\
  2018-03-12 08:30:08 +0400
  * [MDEV-15217](https://jira.mariadb.org/browse/MDEV-15217) Assertion \`thd->transaction.xid\_state.xid.is\_null()' failed in trans\_xa\_start.
* [Revision #28777046b4](https://github.com/MariaDB/server/commit/28777046b4)\
  2018-03-08 11:43:55 +0100
  * [MDEV-15245](https://jira.mariadb.org/browse/MDEV-15245): Assertion \`false' failed in myrocks::ha\_rocksdb::position
* [Revision #112df06996](https://github.com/MariaDB/server/commit/112df06996)\
  2018-03-09 21:25:20 +0200
  * [MDEV-15529](https://jira.mariadb.org/browse/MDEV-15529) IMPORT TABLESPACE unnecessarily uses the doublewrite buffer
* [Revision #54765aaa4d](https://github.com/MariaDB/server/commit/54765aaa4d)\
  2018-03-09 13:43:32 +0200
  * [MDEV-15524](https://jira.mariadb.org/browse/MDEV-15524) Do not disable page checksums for temporary tables
* [Revision #4fa18d52b5](https://github.com/MariaDB/server/commit/4fa18d52b5)\
  2018-03-09 13:40:46 +0200
  * [MDEV-15524](https://jira.mariadb.org/browse/MDEV-15524) Do not write garbage for temporary tables
* [Revision #1e4cb8403c](https://github.com/MariaDB/server/commit/1e4cb8403c)\
  2018-03-09 13:25:28 +0200
  * buf\_page\_io\_complete(): Minor code cleanup
* [Revision #aec4734f61](https://github.com/MariaDB/server/commit/aec4734f61)\
  2018-03-08 12:25:01 +0200
  * [MDEV-13935](https://jira.mariadb.org/browse/MDEV-13935): INSERT INTO stuck at state "Unlocking tables"
* [Revision #a050189773](https://github.com/MariaDB/server/commit/a050189773)\
  2018-03-06 09:16:08 +0200
  * [MDEV-15474](https://jira.mariadb.org/browse/MDEV-15474) Update server.cnf section to mariadb-10.2
* [Revision #8f98835bb8](https://github.com/MariaDB/server/commit/8f98835bb8)\
  2018-03-03 01:59:52 +0200
  * [MDEV-15448](https://jira.mariadb.org/browse/MDEV-15448) Remove "innodb\_additional\_mem\_pool\_size" setting from my-innodb-heavy-4G.cnf file
* [Revision #d0cc7a5225](https://github.com/MariaDB/server/commit/d0cc7a5225)\
  2018-02-25 23:59:01 +0400
  * [MDEV-15420](https://jira.mariadb.org/browse/MDEV-15420) Wrong result for CAST from TIME or DATETIME with zero integer part and non-zero microseconds to DECIMAL(X,Y)
* [Revision #e826d1e64d](https://github.com/MariaDB/server/commit/e826d1e64d)\
  2018-02-24 18:03:41 +0200
  * [MDEV-14814](https://jira.mariadb.org/browse/MDEV-14814): encryption.innodb\_encryption-page-compression failed in buildbot with timeout on wait condition
* [Revision #e92cc09765](https://github.com/MariaDB/server/commit/e92cc09765)\
  2018-02-22 15:58:07 +0100
  * [MDEV-15345](https://jira.mariadb.org/browse/MDEV-15345) Compilation fails to build my\_addr\_resolve.c
* Merge [Revision #e4a73acc63](https://github.com/MariaDB/server/commit/e4a73acc63) 2018-02-22 14:15:24 +0100 - Merge branch '10.1' into 10.2
* [Revision #e119799a92](https://github.com/MariaDB/server/commit/e119799a92)\
  2018-02-22 08:40:54 +0100
  * fix compilation wih -DPLUGIN\_PARTITION=NO
* Merge [Revision #2daa005800](https://github.com/MariaDB/server/commit/2daa005800) 2018-02-22 08:39:24 +0100 - Merge branch '10.1' into 10.2
* [Revision #db0484f355](https://github.com/MariaDB/server/commit/db0484f355)\
  2018-02-21 17:27:46 +0300
  * Change MyRocks Maturity Level from Beta to Gamma (RC)
* [Revision #00a556c0c2](https://github.com/MariaDB/server/commit/00a556c0c2)\
  2018-02-21 17:00:03 +0300
  * [MDEV-15372](https://jira.mariadb.org/browse/MDEV-15372): Parallel slave speedup very limited when log\_slave\_updates=OFF
* [Revision #01e89d6a86](https://github.com/MariaDB/server/commit/01e89d6a86)\
  2018-02-21 15:42:34 +0300
  * [MDEV-15372](https://jira.mariadb.org/browse/MDEV-15372): Parallel slave speedup very limited when log\_slave\_updates=OFF
* [Revision #a128fe4346](https://github.com/MariaDB/server/commit/a128fe4346)\
  2018-02-20 01:16:50 +0200
  * [MDEV-14297](https://jira.mariadb.org/browse/MDEV-14297): Lost name of a explicitly named CTE column used in the non-recursive CTE via prepared statement
* [Revision #84e8e07e8e](https://github.com/MariaDB/server/commit/84e8e07e8e)\
  2018-02-19 16:37:08 +0000
  * Revert "Fix 2 more VS2015 warnings"
* [Revision #0ea45725d8](https://github.com/MariaDB/server/commit/0ea45725d8)\
  2018-02-19 15:21:54 +0000
  * Fix 2 more VS2015 warnings
* [Revision #852c35f571](https://github.com/MariaDB/server/commit/852c35f571)\
  2018-02-19 14:58:05 +0200
  * [MDEV-11581](https://jira.mariadb.org/browse/MDEV-11581) follow-up fix: Correct a condition
* [Revision #83b471348d](https://github.com/MariaDB/server/commit/83b471348d)\
  2018-02-19 16:51:15 +0400
  * [MDEV-14318](https://jira.mariadb.org/browse/MDEV-14318) - cmake updates to build on arm64
* [Revision #112cb56182](https://github.com/MariaDB/server/commit/112cb56182)\
  2018-02-19 08:53:49 +0200
  * Add suppressions for background page read errors
* [Revision #3c419fde5f](https://github.com/MariaDB/server/commit/3c419fde5f)\
  2018-02-19 08:50:42 +0200
  * Cleanup after commit ac8e3c85a40467de0ffc908dd9c5214acf23b38a
* Merge [Revision #acab33a1f2](https://github.com/MariaDB/server/commit/acab33a1f2) 2018-02-18 10:49:46 +0000 - Merge branch '10.2-backup-fixes' into 10.2
* Merge [Revision #e917188f99](https://github.com/MariaDB/server/commit/e917188f99) 2018-02-18 10:47:23 +0000 - Merge branch 'bb-10.2-wlad' into 10.2-backup-fixes
* [Revision #2bb19230d8](https://github.com/MariaDB/server/commit/2bb19230d8)\
  2018-02-15 15:34:15 +0200
  * [MDEV-15323](https://jira.mariadb.org/browse/MDEV-15323) Follow-up to [MDEV-14905](https://jira.mariadb.org/browse/MDEV-14905): Skip FTS processing if innodb\_read\_only
* [Revision #03400d974d](https://github.com/MariaDB/server/commit/03400d974d)\
  2018-02-15 09:50:03 +0200
  * Dead code removal: sess\_t
* [Revision #37af958d23](https://github.com/MariaDB/server/commit/37af958d23)\
  2018-02-15 09:46:02 +0200
  * [MDEV-14905](https://jira.mariadb.org/browse/MDEV-14905) Fulltext index modification committed during shutdown
* [Revision #6f314edac7](https://github.com/MariaDB/server/commit/6f314edac7)\
  2018-02-14 15:18:55 +0200
  * [MDEV-14648](https://jira.mariadb.org/browse/MDEV-14648) Restore fix for MySQL BUG#39053 - UNINSTALL PLUGIN does not allow the storage engine to cleanup open connections
* [Revision #54e66eefb8](https://github.com/MariaDB/server/commit/54e66eefb8)\
  2018-02-02 20:12:23 +0300
  * Prevent building WSREP without INNODB
* [Revision #743b073c46](https://github.com/MariaDB/server/commit/743b073c46)\
  2018-02-15 11:53:46 +0000
  * Add more testsuites to Windows buildbot builder
* [Revision #f082c7557e](https://github.com/MariaDB/server/commit/f082c7557e)\
  2018-02-15 01:26:09 +0000
  * fix signed/unsigned mismatch on Windows
* [Revision #d49f8e9f05](https://github.com/MariaDB/server/commit/d49f8e9f05)\
  2018-02-14 23:21:58 +0000
  * Windows,tests : fix pcre\_test\_bat test from pcre library.
* [Revision #8a923a6de5](https://github.com/MariaDB/server/commit/8a923a6de5)\
  2018-02-14 19:45:26 +0000
  * Update C/C
* [Revision #24462cece4](https://github.com/MariaDB/server/commit/24462cece4)\
  2018-02-14 19:13:08 +0000
  * Disable noisy warning in old compiler (VS2015)
* [Revision #ac8e3c85a4](https://github.com/MariaDB/server/commit/ac8e3c85a4)\
  2018-02-14 18:39:56 +0000
  * [MDEV-15295](https://jira.mariadb.org/browse/MDEV-15295) Type mismatch for srv\_fatal\_semaphore\_wait\_threshold
* [Revision #1a10b261d0](https://github.com/MariaDB/server/commit/1a10b261d0)\
  2018-02-14 17:01:07 +0000
  * Add some hints for finding bison on its usual locations on Windows.
* [Revision #2dd8a732f3](https://github.com/MariaDB/server/commit/2dd8a732f3)\
  2018-02-14 16:58:57 +0000
  * Windows, compiling - disable pkg\_config
* [Revision #46496b1a8c](https://github.com/MariaDB/server/commit/46496b1a8c)\
  2018-02-14 16:52:18 +0000
  * Windows, mtr - correctly determine CPU count, for --parallel=auto
* [Revision #2129eab7e2](https://github.com/MariaDB/server/commit/2129eab7e2)\
  2018-02-15 21:08:18 +0000
  * [MDEV-15071](https://jira.mariadb.org/browse/MDEV-15071) backup does not store xtrabackup\_info in the --extra-lsndir directory
* [Revision #a08121c978](https://github.com/MariaDB/server/commit/a08121c978)\
  2018-02-15 17:40:14 +0000
  * [MDEV-14997](https://jira.mariadb.org/browse/MDEV-14997) mariadb-backup crashes with invalid --innodb-flush-method
* Merge [Revision #970ce270c9](https://github.com/MariaDB/server/commit/970ce270c9) 2018-02-17 14:54:12 +0200 - Merge 10.1 into 10.2
* [Revision #8bf2c08d54](https://github.com/MariaDB/server/commit/8bf2c08d54)\
  2018-02-16 21:02:35 +0200
  * Add a suppression for background page read error
* [Revision #6668da2216](https://github.com/MariaDB/server/commit/6668da2216)\
  2018-02-16 13:44:24 +0400
  * [MDEV-15289](https://jira.mariadb.org/browse/MDEV-15289) Binding an out-of-range DATETIME value in binary protocol breaks replication
* [Revision #5ab4602810](https://github.com/MariaDB/server/commit/5ab4602810)\
  2018-02-15 15:34:15 +0200
  * [MDEV-15323](https://jira.mariadb.org/browse/MDEV-15323) Follow-up to [MDEV-14905](https://jira.mariadb.org/browse/MDEV-14905): Skip FTS processing if innodb\_read\_only
* [Revision #27ea2963fc](https://github.com/MariaDB/server/commit/27ea2963fc)\
  2018-02-15 09:50:03 +0200
  * Dead code removal: sess\_t
* [Revision #7baea2efa2](https://github.com/MariaDB/server/commit/7baea2efa2)\
  2018-02-15 09:46:02 +0200
  * [MDEV-14905](https://jira.mariadb.org/browse/MDEV-14905) Fulltext index modification committed during shutdown
* [Revision #5fe9b4a7ae](https://github.com/MariaDB/server/commit/5fe9b4a7ae)\
  2018-02-14 15:18:55 +0200
  * [MDEV-14648](https://jira.mariadb.org/browse/MDEV-14648) Restore fix for MySQL BUG#39053 - UNINSTALL PLUGIN does not allow the storage engine to cleanup open connections
* [Revision #8db54f1ad5](https://github.com/MariaDB/server/commit/8db54f1ad5)\
  2018-02-02 20:12:23 +0300
  * Prevent building WSREP without INNODB
* Merge [Revision #c6e35276f1](https://github.com/MariaDB/server/commit/c6e35276f1) 2018-02-14 10:01:16 +0200 - Merge 10.1 into 10.2
* [Revision #ab8ea23a75](https://github.com/MariaDB/server/commit/ab8ea23a75)\
  2018-02-13 11:23:14 -0500
  * bump the VERSION
* Merge [Revision #d9955b22e9](https://github.com/MariaDB/server/commit/d9955b22e9) 2018-02-13 14:49:47 +0200 - Merge 10.1 into 10.2

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
