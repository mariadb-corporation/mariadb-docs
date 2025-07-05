# MariaDB 10.2.15 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/release-notes-mariadb-10-2-series/mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.15)[Release Notes](../../old-releases/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md)[Changelog](mariadb-10215-changelog.md)[Overview of 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md)

**Release date:** 17 May 2018

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #bb045e7931](https://github.com/MariaDB/server/commit/bb045e7931)\
  2018-05-16 11:15:08 +0200
  * [MDEV-16183](https://jira.mariadb.org/browse/MDEV-16183) TokuDB tests fail on Fedora 28
* [Revision #cb21e117ba](https://github.com/MariaDB/server/commit/cb21e117ba)\
  2018-05-16 18:03:06 +0200
  * [MDEV-16187](https://jira.mariadb.org/browse/MDEV-16187) Ubuntu Bionic MariaDB has epoch version that makes 10.1 and 10.2 installs fail
* Merge [Revision #ebc24950e6](https://github.com/MariaDB/server/commit/ebc24950e6) 2018-05-16 15:07:24 +0530 - [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626) Merge InnoDB test cases from MySQL 5.7
* [Revision #a54b581d03](https://github.com/MariaDB/server/commit/a54b581d03)\
  2015-12-22 22:07:13 +0800
  * BUG#22385442 - INNODB: DIFFICULT TO FIND FREE BLOCKS IN THE BUFFER POOL
* [Revision #64d6a65ab2](https://github.com/MariaDB/server/commit/64d6a65ab2)\
  2018-05-14 19:31:38 +0530\
  \*
  * Adjusted the test case for MariaDB
* [Revision #0ba299da02](https://github.com/MariaDB/server/commit/0ba299da02)\
  2015-08-17 13:44:52 +0300
  * Bug#21628087 innodb\_log\_checkpoint\_now not fully compatible with [WL#7142](https://askmonty.org/worklog/?tid=7142)
* [Revision #be465cfb8c](https://github.com/MariaDB/server/commit/be465cfb8c)\
  2018-05-14 19:22:26 +0530
  * Move the test case from innodb.alter\_page\_size to innodb.innodb-online-alter-gis
* [Revision #21e02b2c92](https://github.com/MariaDB/server/commit/21e02b2c92)\
  2014-08-05 17:25:57 +0530
  * Bug #19077964 ASSERT PAGE\_SIZE.EQUALS\_TO SPACE\_PAGE\_SIZE BTR\_COPY\_BLOB\_PREFIX
* [Revision #6e76b402d4](https://github.com/MariaDB/server/commit/6e76b402d4)\
  2018-05-14 19:00:52 +0530
  * Adjust the alter\_foreign\_crash test case for MariaDB
* [Revision #a1f392a944](https://github.com/MariaDB/server/commit/a1f392a944)\
  2015-04-20 14:45:47 +0530
  * Bug #20476395 DICT\_LOAD\_FOREIGNS() FAILED IN COMMIT\_INPLACE\_ALTER\_TABLE
* [Revision #91659983eb](https://github.com/MariaDB/server/commit/91659983eb)\
  2018-05-14 18:46:25 +0530
  * Adjust the tests for MariaDB. New added test case: alter\_kill in innodb suite.
* [Revision #ac2410f6d8](https://github.com/MariaDB/server/commit/ac2410f6d8)\
  2014-08-11 10:43:11 +0300
  * Bug#19330255 [WL#7142](https://askmonty.org/worklog/?tid=7142) - CRASH DURING ALTER TABLE LEADS TO DATA DICTIONARY INCONSISTENCY
* [Revision #6f4534e622](https://github.com/MariaDB/server/commit/6f4534e622)\
  2018-05-15 01:44:03 +0530
  * [MDEV-14695](https://jira.mariadb.org/browse/MDEV-14695): Assertion \`n < m\_size' failed in Bounds\_checked\_array\<Element\_type>::operator
* [Revision #d9f9cd1a10](https://github.com/MariaDB/server/commit/d9f9cd1a10)\
  2018-05-15 23:42:20 +0300
  * Updated list of unstable tests for 10.2.15
* [Revision #4ab180ad5e](https://github.com/MariaDB/server/commit/4ab180ad5e)\
  2018-05-15 17:02:08 +0300
  * [MDEV-15461](https://jira.mariadb.org/browse/MDEV-15461) Check Constraints with binary logging makes insert inconsistent
* [Revision #0e296947db](https://github.com/MariaDB/server/commit/0e296947db)\
  2018-05-15 15:12:54 +0200
  * add missing test result
* [Revision #182db5a1b7](https://github.com/MariaDB/server/commit/182db5a1b7)\
  2018-05-15 10:18:39 +0200
  * disable galera.pxc-421 test
* [Revision #77cd754229](https://github.com/MariaDB/server/commit/77cd754229)\
  2018-05-14 23:24:26 +0200
  * [MDEV-16110](https://jira.mariadb.org/browse/MDEV-16110) ALTER with ALGORITHM=INPLACE breaks temporary table with virtual columns
* [Revision #c29312421e](https://github.com/MariaDB/server/commit/c29312421e)\
  2018-05-14 21:21:59 +0200
  * [MDEV-14750](https://jira.mariadb.org/browse/MDEV-14750) Valgrind Invalid read, ASAN heap-use-after-free in Item\_ident::print upon SHOW CREATE on partitioned table
* [Revision #c14c958c6c](https://github.com/MariaDB/server/commit/c14c958c6c)\
  2018-05-14 21:05:51 +0200
  * cleanup: vcol\_in\_partition\_func\_processor
* [Revision #445ac662c3](https://github.com/MariaDB/server/commit/445ac662c3)\
  2018-05-14 16:44:03 +0200
  * [MDEV-15755](https://jira.mariadb.org/browse/MDEV-15755) Query crashing MariaDB in cleanup\_after\_query
* [Revision #93efa48a7b](https://github.com/MariaDB/server/commit/93efa48a7b)\
  2018-05-13 18:50:21 +0200
  * fix failing main.mysql\_client\_test test on 32bit
* [Revision #9d6ec6d14a](https://github.com/MariaDB/server/commit/9d6ec6d14a)\
  2018-05-12 12:50:34 +0200
  * update C/C
* [Revision #21bcfeb996](https://github.com/MariaDB/server/commit/21bcfeb996)\
  2018-05-15 12:34:10 +0300
  * [MDEV-16155](https://jira.mariadb.org/browse/MDEV-16155): UPDATE on RocksDB table with unique constraint does not work
* [Revision #681e8ca35e](https://github.com/MariaDB/server/commit/681e8ca35e)\
  2018-05-15 08:18:44 +0300
  * [MDEV-16142](https://jira.mariadb.org/browse/MDEV-16142): Update the InnoDB version number to 5.7.22
* [Revision #95e9c7054f](https://github.com/MariaDB/server/commit/95e9c7054f)\
  2018-05-14 16:30:25 -0700
  * [MDEV-16101](https://jira.mariadb.org/browse/MDEV-16101): ADD PARTITION on table partitioned by list does not work with more than 32 list values.
* [Revision #0d033b6d34](https://github.com/MariaDB/server/commit/0d033b6d34)\
  2018-05-14 23:54:07 +0300
  * Down-scale rocksdb.bulk\_load\* tests by 2x. This should fix [MDEV-13904](https://jira.mariadb.org/browse/MDEV-13904)
* Merge [Revision #2879fb08d2](https://github.com/MariaDB/server/commit/2879fb08d2) 2018-05-14 23:33:43 +0300 - [MDEV-16142](https://jira.mariadb.org/browse/MDEV-16142): Merge one more fix from MySQL 5.7.22
* [Revision #2b24b04220](https://github.com/MariaDB/server/commit/2b24b04220)\
  2018-05-14 23:22:59 +0300
  * Bug 27122803 - BACKPORT FIX FOR BUG 25899959 TO MYSQL-5.7
* [Revision #4d2a36e8bc](https://github.com/MariaDB/server/commit/4d2a36e8bc)\
  2018-05-14 20:25:02 +0300
  * Post-merge fix for rocksdb.add\_index\_inplace\_sstfilewriter
* [Revision #279184a04d](https://github.com/MariaDB/server/commit/279184a04d)\
  2018-05-14 19:50:21 +0300
  * [MDEV-14562](https://jira.mariadb.org/browse/MDEV-14562): rocksdb.bloomfilter failed in buildbot
* [Revision #fb5d579462](https://github.com/MariaDB/server/commit/fb5d579462)\
  2018-05-14 18:04:25 +0300
  * [MDEV-13987](https://jira.mariadb.org/browse/MDEV-13987) Hang in FLUSH TABLES...FOR EXPORT
* [Revision #16a8a241c2](https://github.com/MariaDB/server/commit/16a8a241c2)\
  2018-05-14 17:57:33 +0300
  * [MDEV-14375](https://jira.mariadb.org/browse/MDEV-14375): rocksdb.bulk\_load\_unsorted fails
* [Revision #7e7592ade5](https://github.com/MariaDB/server/commit/7e7592ade5)\
  2018-05-14 15:59:51 +0300
  * [MDEV-16154](https://jira.mariadb.org/browse/MDEV-16154): Server crashes in myrocks::ha\_rocksdb::load\_auto\_incr\_value\_from\_index
* [Revision #6c0f3dd341](https://github.com/MariaDB/server/commit/6c0f3dd341)\
  2018-05-12 20:32:16 +0200
  * [MDEV-16090](https://jira.mariadb.org/browse/MDEV-16090): Server crash in Item\_func\_in::val\_int or assertion \`in\_item' failure upon SELECT with impossible condition
* [Revision #8b26fea835](https://github.com/MariaDB/server/commit/8b26fea835)\
  2018-05-10 23:01:41 +0200
  * [MDEV-16088](https://jira.mariadb.org/browse/MDEV-16088): Pushdown into materialized views/derived tables doesn't work in the IN subqueries
* [Revision #77867c147b](https://github.com/MariaDB/server/commit/77867c147b)\
  2018-05-12 10:28:54 +0300
  * dict\_create\_index\_tree\_in\_mem(): Remove dead code
* [Revision #8c4f3b316e](https://github.com/MariaDB/server/commit/8c4f3b316e)\
  2018-05-12 10:27:19 +0300
  * After-merge fix
* Merge [Revision #9b18f5a5da](https://github.com/MariaDB/server/commit/9b18f5a5da) 2018-05-11 19:11:12 +0300 - [MDEV-16142](https://jira.mariadb.org/browse/MDEV-16142) Merge new release of InnoDB MySQL 5.7.22 to 10.2
* [Revision #0da98472b7](https://github.com/MariaDB/server/commit/0da98472b7)\
  2018-02-14 12:51:05 +0530
  * Bug #23593654 CRASH IN BUF\_BLOCK\_FROM\_AHI WHEN LARGE PAGES AND AHI ARE ENABLED
* [Revision #4c7ea34ef6](https://github.com/MariaDB/server/commit/4c7ea34ef6)\
  2018-02-08 01:25:10 +0530
  * FOLLOW-UP FIX FOR BUG#27141613
* [Revision #279f992b85](https://github.com/MariaDB/server/commit/279f992b85)\
  2018-01-29 18:47:23 +0530
  * Bug #27141613 ASSERTION: TRX0REC.CC:319:COL->IS\_VIRTUAL() / CRASH IN TRX\_UNDO\_READ\_V\_COLS
* [Revision #c88ac735b1](https://github.com/MariaDB/server/commit/c88ac735b1)\
  2018-05-11 16:56:02 +0300
  * Adjust the test case for MariaDB
* [Revision #280879ebd9](https://github.com/MariaDB/server/commit/280879ebd9)\
  2018-01-29 17:17:21 +0530
  * Bug #27304661 MYSQL CRASH DOING SYNC INDEX ] \[FATAL] INNODB: SEMAPHORE WAIT HAS LASTED > 600
* [Revision #b7e333f98a](https://github.com/MariaDB/server/commit/b7e333f98a)\
  2017-12-18 18:40:08 +0530
  * Bug #26805833 INNODB COMPLAINS OF SYNTAX ERROR, BUT DOES NOT SAY WHICH OPTION
* [Revision #671a37f60e](https://github.com/MariaDB/server/commit/671a37f60e)\
  2018-05-11 15:08:08 +0300
  * Adjust the test case for MariaDB
* [Revision #3d10966b7d](https://github.com/MariaDB/server/commit/3d10966b7d)\
  2017-12-05 19:13:12 +0530
  * Bug #26731689 FK ON TABLE WITH GENERATED COLS: ASSERTION POS < N\_DEF
* [Revision #e26b07dbc6](https://github.com/MariaDB/server/commit/e26b07dbc6)\
  2018-05-11 18:17:26 +0300
  * Add a test case for a MySQL 5.7 bug that did not affect MariaDB
* Merge [Revision #82f0dc35aa](https://github.com/MariaDB/server/commit/82f0dc35aa) 2018-05-11 18:33:58 +0300 - Merge 10.1 into 10.2
* Merge [Revision #3b99a274a8](https://github.com/MariaDB/server/commit/3b99a274a8) 2018-05-11 17:32:20 +0300 - Merge 10.0 into 10.1
* [Revision #197bf0fe35](https://github.com/MariaDB/server/commit/197bf0fe35)\
  2018-02-22 18:45:38 +0530
  * Bug #26334149 - MYSQL CRASHES WHEN FULL TEXT INDEXES IBD FILES ARE ORPHANED DUE TO RENAME TABLE
* [Revision #9c03ba8f0d](https://github.com/MariaDB/server/commit/9c03ba8f0d)\
  2017-12-27 11:56:11 +0530
  * Bug #27041445 SERVER ABORTS IF FTS\_DOC\_ID EXCEEDS FTS\_DOC\_ID\_MAX\_STEP
* Merge [Revision #c70fc6b16a](https://github.com/MariaDB/server/commit/c70fc6b16a) 2018-05-11 14:07:05 +0300 - Merge 5.5 into 10.0 (no changes)
* [Revision #318097bb8f](https://github.com/MariaDB/server/commit/318097bb8f)\
  2018-05-10 19:00:54 +0400
  * [MDEV-15480](https://jira.mariadb.org/browse/MDEV-15480) Audit plugin does not respect QUERY\_DML for audit plugin.
* [Revision #580a8061a7](https://github.com/MariaDB/server/commit/580a8061a7)\
  2018-05-11 13:48:57 +0300
  * Remove a redundant condition added by the 5.6.40 merge
* [Revision #3cbfe8cc47](https://github.com/MariaDB/server/commit/3cbfe8cc47)\
  2018-05-10 19:00:54 +0400
  * [MDEV-15480](https://jira.mariadb.org/browse/MDEV-15480) Audit plugin does not respect QUERY\_DML for audit plugin.
* [Revision #dab4abbb09](https://github.com/MariaDB/server/commit/dab4abbb09)\
  2018-05-10 19:00:54 +0400
  * [MDEV-15480](https://jira.mariadb.org/browse/MDEV-15480) Audit plugin does not respect QUERY\_DML for audit plugin.
* [Revision #7d521bcc46](https://github.com/MariaDB/server/commit/7d521bcc46)\
  2018-05-09 17:43:08 -0400
  * bump the VERSION
* [Revision #c407ee0976](https://github.com/MariaDB/server/commit/c407ee0976)\
  2018-05-11 16:24:51 +0300
  * [MDEV-16145](https://jira.mariadb.org/browse/MDEV-16145) Crash in ALTER TABLE…AUTO\_INCREMENT=1 after DISCARD TABLESPACE
* [Revision #64f4576be4](https://github.com/MariaDB/server/commit/64f4576be4)\
  2018-05-11 10:08:00 +0300
  * [MDEV-15697](https://jira.mariadb.org/browse/MDEV-15697) post-fix: Remove an unused variable
* [Revision #c686483264](https://github.com/MariaDB/server/commit/c686483264)\
  2018-05-11 13:55:03 +0300
  * [MDEV-12427](https://jira.mariadb.org/browse/MDEV-12427): rocksdb.write\_sync fails
* [Revision #16319409bf](https://github.com/MariaDB/server/commit/16319409bf)\
  2018-05-08 15:00:17 +0530
  * [MDEV-15853](https://jira.mariadb.org/browse/MDEV-15853): Assertion \`tab->filesort\_result == 0' failed
* [Revision #e5bd75fb4e](https://github.com/MariaDB/server/commit/e5bd75fb4e)\
  2018-05-10 21:46:57 +0300
  * MyRocks: disable rocksdb.check\_ignore\_unknown\_options on Windows
* Merge [Revision #83cdccdb1a](https://github.com/MariaDB/server/commit/83cdccdb1a) 2018-05-10 20:21:09 +0300 - Merge branch 'bb-10.2-mariarocks' into 10.2
* [Revision #ffb48234df](https://github.com/MariaDB/server/commit/ffb48234df)\
  2018-05-10 20:16:15 +0300
  * MyRocks on windows: make bulk\_load\_unsorted pass.
* [Revision #b0269816a5](https://github.com/MariaDB/server/commit/b0269816a5)\
  2018-05-10 19:05:13 +0300
  * MyRocks: post-merge fixes for Windows: take into account FN\_LIBCHAR2
* [Revision #4d51009a77](https://github.com/MariaDB/server/commit/4d51009a77)\
  2018-05-08 13:00:26 +0300
  * MyRocks: fix rocksdb.rocksdb\_range test attempt 3
* [Revision #45ef87ee92](https://github.com/MariaDB/server/commit/45ef87ee92)\
  2018-05-07 22:13:18 +0300
  * Post-merge fixes: fix rocksdb.rocksdb\_checksums test
* Merge [Revision #69b46aac9f](https://github.com/MariaDB/server/commit/69b46aac9f) 2018-05-10 20:20:49 +0300 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* Merge [Revision #1d411a8a44](https://github.com/MariaDB/server/commit/1d411a8a44) 2018-05-10 13:02:19 +0200 - Merge branch 'connect/10.2' into 10.2
* [Revision #0138220ff6](https://github.com/MariaDB/server/commit/0138220ff6)\
  2018-05-07 00:27:13 +0200\
  \*
  * Fix [MDEV-15735](https://jira.mariadb.org/browse/MDEV-15735) CONNECT \[filamtxt.cpp:429]: Suspicious condition modified: storage/connect/filamtxt.cpp
* [Revision #213b1da256](https://github.com/MariaDB/server/commit/213b1da256)\
  2018-03-27 17:08:39 +0200\
  \*
  * Fix [MDEV-15577](https://jira.mariadb.org/browse/MDEV-15577) CONNECT engine JDBC remote index prevents UPDATE Fixed in TDBJDBC::OpenDB because query can be null for updates modified: storage/connect/tabjdbc.cpp
* Merge [Revision #9b1824dcd2](https://github.com/MariaDB/server/commit/9b1824dcd2) 2018-05-10 13:01:42 +0200 - Merge branch '10.1' into 10.2
* [Revision #ff579bc814](https://github.com/MariaDB/server/commit/ff579bc814)\
  2018-05-09 12:10:56 +0200
  * install disks plugin on debian
* Merge [Revision #d06ca5bbf6](https://github.com/MariaDB/server/commit/d06ca5bbf6) 2018-05-09 15:58:04 +0300 - Merge 10.0 into 10.1
* [Revision #4f42f0d1ea](https://github.com/MariaDB/server/commit/4f42f0d1ea)\
  2018-05-09 15:06:48 +0300
  * [MDEV-16119](https://jira.mariadb.org/browse/MDEV-16119) InnoDB lock->index refers to a freed object after failed ADD INDEX
* [Revision #b2fc197b56](https://github.com/MariaDB/server/commit/b2fc197b56)\
  2018-05-09 09:16:20 +0300
  * [MDEV-15351](https://jira.mariadb.org/browse/MDEV-15351): wsrep\_sst\_xtrabackup is broken in 10.1.31
* [Revision #f98496da96](https://github.com/MariaDB/server/commit/f98496da96)\
  2018-05-08 15:08:08 +0100
  * [MDEV-16105](https://jira.mariadb.org/browse/MDEV-16105): mariadb-backup does not support SSL
* [Revision #b62224e232](https://github.com/MariaDB/server/commit/b62224e232)\
  2018-05-08 22:39:14 +0300
  * Mroonga cmake failure - LZ4\_LIBS = NOTFOUND
* Merge [Revision #1bc3899a52](https://github.com/MariaDB/server/commit/1bc3899a52) 2018-05-08 14:13:01 +0200 - Merge branch '10.0' into 10.1
* [Revision #34045af03f](https://github.com/MariaDB/server/commit/34045af03f)\
  2018-05-06 22:46:56 +0200
  * [MDEV-15216](https://jira.mariadb.org/browse/MDEV-15216) Assertion \`! is\_set() || m\_can\_overwrite\_status' failed in Diagnostics\_area::set\_error\_status upon operation inside XA
* [Revision #087ea8f820](https://github.com/MariaDB/server/commit/087ea8f820)\
  2018-05-08 10:31:35 +0200
  * de-obfuscate rpl\_\*\_implicit\_commit\_binlog test
* [Revision #0d429dcb37](https://github.com/MariaDB/server/commit/0d429dcb37)\
  2018-05-06 22:47:30 +0200
  * rename a test
* [Revision #de0e5fe17c](https://github.com/MariaDB/server/commit/de0e5fe17c)\
  2018-05-08 13:32:40 +0400
  * [MDEV-14541](https://jira.mariadb.org/browse/MDEV-14541) - Workaround GCC ICE on ARM64
* [Revision #92a13148e8](https://github.com/MariaDB/server/commit/92a13148e8)\
  2018-04-16 23:14:28 +0200
  * [MDEV-15746](https://jira.mariadb.org/browse/MDEV-15746) ASAN heap-use-after-free in Item\_change\_list::rollback\_item\_tree\_changes on ALTER executed as PS
* [Revision #88a0bb83df](https://github.com/MariaDB/server/commit/88a0bb83df)\
  2018-04-11 16:23:49 +0200
  * [MDEV-15626](https://jira.mariadb.org/browse/MDEV-15626) Assertion on update virtual column in partitioned table
* [Revision #8ba0eea65c](https://github.com/MariaDB/server/commit/8ba0eea65c)\
  2018-05-09 23:04:18 +0100
  * Fix warning VS2017 15.7 update.
* [Revision #df420cbbfd](https://github.com/MariaDB/server/commit/df420cbbfd)\
  2018-05-01 14:14:06 -0700
  * [MDEV-15697](https://jira.mariadb.org/browse/MDEV-15697): Remote user used by Spider needs SUPER privilege
* [Revision #fe95cb2e40](https://github.com/MariaDB/server/commit/fe95cb2e40)\
  2018-05-09 19:00:30 +0530
  * [MDEV-16125](https://jira.mariadb.org/browse/MDEV-16125) Shutdown crash when innodb\_force\_recovery >= 2
* [Revision #0ea625b325](https://github.com/MariaDB/server/commit/0ea625b325)\
  2018-05-09 12:07:55 +0300
  * [MDEV-15916](https://jira.mariadb.org/browse/MDEV-15916) Change buffer crash during TRUNCATE or DROP TABLE
* [Revision #bd1d152d05](https://github.com/MariaDB/server/commit/bd1d152d05)\
  2018-05-08 19:27:08 +0530
  * [MDEV-16106](https://jira.mariadb.org/browse/MDEV-16106) Record in index was not found on rollback, trying to insert: TUPLE
* [Revision #9bcd0f5fea](https://github.com/MariaDB/server/commit/9bcd0f5fea)\
  2018-05-07 13:22:00 -0700
  * Added the test case from [MDEV-16086](https://jira.mariadb.org/browse/MDEV-16086) tfixed by the patch for [MDEV-15575](https://jira.mariadb.org/browse/MDEV-15575)
* Merge [Revision #dbe73588cd](https://github.com/MariaDB/server/commit/dbe73588cd) 2018-05-07 21:38:18 +0300 - Merge branch 'bb-10.2-mariarocks-merge' of github.com:MariaDB/server into 10.2
* [Revision #03edf2ed04](https://github.com/MariaDB/server/commit/03edf2ed04)\
  2018-05-07 20:33:14 +0300
  * Undo the incorrect part of commit 7e700bd2a81ae4b37145f1c32bb0902c72856d2d
* [Revision #e3661b9f7c](https://github.com/MariaDB/server/commit/e3661b9f7c)\
  2018-05-07 20:21:35 +0300
  * Cherry-picked from MyRocks upstream: Issue #809: Wrong query result with bloom filters
* [Revision #39fbafbcc2](https://github.com/MariaDB/server/commit/39fbafbcc2)\
  2018-04-19 16:28:05 +0300
  * Post-merge fixes: make rocksdb.allow\_to\_start\_after\_corruption pass
* [Revision #955233256e](https://github.com/MariaDB/server/commit/955233256e)\
  2018-04-19 15:41:13 +0300
  * MyRocks: fix rocksdb.information\_schema testcase.
* [Revision #6bea5e9e0f](https://github.com/MariaDB/server/commit/6bea5e9e0f)\
  2018-04-17 15:04:15 +0300
  * MyRocks: Post-merge fixes in bulk\_load\_error.test
* [Revision #a7e5049fec](https://github.com/MariaDB/server/commit/a7e5049fec)\
  2018-04-17 11:10:11 +0300
  * MyRocks: Fix link error on Windows
* [Revision #959362c020](https://github.com/MariaDB/server/commit/959362c020)\
  2018-04-16 21:09:14 +0300
  * Fix compilation on windows
* [Revision #40bed2d39e](https://github.com/MariaDB/server/commit/40bed2d39e)\
  2018-04-16 11:06:43 +0300
  * MyRocks: Add files lost during the merge
* [Revision #ce4149fc9b](https://github.com/MariaDB/server/commit/ce4149fc9b)\
  2018-04-15 21:15:21 +0300
  * Post-merge fixes: make rocksdb.use\_direct\_reads\_writes pass
* [Revision #0fad97a9ec](https://github.com/MariaDB/server/commit/0fad97a9ec)\
  2018-04-15 15:34:06 +0300
  * Post-merge fixes: add a suppression for rocksdb.skip\_validate\_tmP\_table
* [Revision #261d4755f4](https://github.com/MariaDB/server/commit/261d4755f4)\
  2018-04-15 14:34:56 +0300
  * Post-merge fixes: rocksdb.check\_ignore\_unknown\_options
* [Revision #8496e84f05](https://github.com/MariaDB/server/commit/8496e84f05)\
  2018-04-15 12:52:27 +0300
  * Trivial post-merge fixes
* [Revision #78e42153b5](https://github.com/MariaDB/server/commit/78e42153b5)\
  2018-04-13 20:26:40 +0300
  * Fix compile on windows: O\_SYNC is not available, use a my\_sync() call instead.
* [Revision #5545753b0b](https://github.com/MariaDB/server/commit/5545753b0b)\
  2018-04-13 00:39:51 +0300
  * Update test results
* [Revision #34e6b5fa6f](https://github.com/MariaDB/server/commit/34e6b5fa6f)\
  2018-04-12 20:28:54 +0300
  * Undo fix for [MDEV-13852](https://jira.mariadb.org/browse/MDEV-13852): RocksDB now has a proper WinWriteableFile::IsSyncThreadSafe()
* [Revision #5715177a76](https://github.com/MariaDB/server/commit/5715177a76)\
  2018-04-11 18:39:06 +0300\
  \*
  * Fix a merge error - Test result updates
* [Revision #7e700bd2a8](https://github.com/MariaDB/server/commit/7e700bd2a8)\
  2018-04-09 19:12:23 +0300
  * Fix ha\_rocksdb::calc\_eq\_cond\_len() to handle HA\_READ\_PREFIX\_LAST\_OR\_PREV correctly This is Variant#2. - Undo Variant#1 - Instead, swap the range bounds if we are doing a reverse-ordered scan.
* [Revision #8628c589f6](https://github.com/MariaDB/server/commit/8628c589f6)\
  2018-04-09 15:27:35 +0300
  * Fix ha\_rocksdb::calc\_eq\_cond\_len() to handle HA\_READ\_PREFIX\_LAST\_OR\_PREV correctly
* [Revision #e7efc79350](https://github.com/MariaDB/server/commit/e7efc79350)\
  2018-04-09 01:10:43 +0300
  * Make rocksdb.information\_schema test stable
* [Revision #34ff2967c5](https://github.com/MariaDB/server/commit/34ff2967c5)\
  2018-02-08 19:25:19 +0530
  * Post merge fix
* [Revision #48cfb3b80d](https://github.com/MariaDB/server/commit/48cfb3b80d)\
  2018-02-01 23:37:41 +0000
  * Post-merge fixes: rocksdb.i\_s\_ddl
* [Revision #d0fd44fc52](https://github.com/MariaDB/server/commit/d0fd44fc52)\
  2018-02-01 19:44:48 +0000
  * Post-merge fixes: MariaDB-fication of rdb\_i\_s\_deadlock\_info
* [Revision #f457a113ab](https://github.com/MariaDB/server/commit/f457a113ab)\
  2018-02-01 11:56:31 +0000
  * Post-merge fixes: update .result for rocksdb.i\_s\_deadlock
* [Revision #ba03577a1f](https://github.com/MariaDB/server/commit/ba03577a1f)\
  2018-01-31 14:31:44 +0000
  * Post-merge fixes: make rocksdb.bulk\_load\_unsorted\_rev to work.
* [Revision #669e910a6a](https://github.com/MariaDB/server/commit/669e910a6a)\
  2018-01-30 12:50:30 +0000
  * More post-merge fixes
* [Revision #819adb44a8](https://github.com/MariaDB/server/commit/819adb44a8)\
  2018-01-29 16:07:23 +0300
  * Post-merge fixes - Fix rocksdb.rocksdb test - Update rocksdb.autoinc\_crash\_safe\_partition\* tests
* Merge [Revision #e3a03da2bc](https://github.com/MariaDB/server/commit/e3a03da2bc) 2018-01-27 11:52:34 +0000 - Merge from merge-myrocks: commit 445e518bc7aa5f4bb48d98e798905c9c0b0ce673 Author: Sergei Petrunia [psergey@askmonty.org](mailto:psergey@askmonty.org) Date: Sat Jan 27 10:18:20 2018 +0000
* [Revision #445e518bc7](https://github.com/MariaDB/server/commit/445e518bc7)\
  2018-01-27 10:18:20 +0000
  * Copy of commit f8f364b47f2784f16b401f27658f1c16eaf348ec Author: Jay Edgar [jkedgar@fb.com](mailto:jkedgar@fb.com) Date: Tue Oct 17 15:19:31 2017 -0700
* [Revision #e44ca6cc9c](https://github.com/MariaDB/server/commit/e44ca6cc9c)\
  2018-05-07 15:30:57 +0300
  * [MDEV-14825](https://jira.mariadb.org/browse/MDEV-14825) Assertion \`col->ord\_part' in row\_build\_index\_entry\_low upon ROLLBACK or DELETE with concurrent ALTER on partitioned table
* [Revision #d257c425f2](https://github.com/MariaDB/server/commit/d257c425f2)\
  2018-05-04 15:50:21 +0300
  * [MDEV-15764](https://jira.mariadb.org/browse/MDEV-15764) InnoDB may write uninitialized garbage to redo log
* [Revision #da3c5c3c9a](https://github.com/MariaDB/server/commit/da3c5c3c9a)\
  2018-05-01 18:47:04 -0700
  * [MDEV-15698](https://jira.mariadb.org/browse/MDEV-15698): Spider ignores syntax errors in connection string in COMMENT field
* [Revision #8fdeb079b9](https://github.com/MariaDB/server/commit/8fdeb079b9)\
  2018-04-30 19:44:02 -0700
  * [MDEV-15712](https://jira.mariadb.org/browse/MDEV-15712): If remote server used by Spider table is unavailable, some operations hang for a long time
* [Revision #bcc26dce3a](https://github.com/MariaDB/server/commit/bcc26dce3a)\
  2018-04-28 20:28:50 +0300
  * Revert "Fix mtr to be able to wait for >1 exited mysqld"
* [Revision #b4c5e4a717](https://github.com/MariaDB/server/commit/b4c5e4a717)\
  2018-04-26 22:46:39 +0300
  * Follow-up fix to [MDEV-14705](https://jira.mariadb.org/browse/MDEV-14705): Flush log at shutdown
* [Revision #5569b3eb09](https://github.com/MariaDB/server/commit/5569b3eb09)\
  2018-04-26 20:56:14 +0300
  * [MDEV-16041](https://jira.mariadb.org/browse/MDEV-16041) Do not write for null update (properly fix MySQL Bug#29157)
* [Revision #c5ea43fc99](https://github.com/MariaDB/server/commit/c5ea43fc99)\
  2018-04-26 14:15:57 +0300
  * innobase\_init(): Remove some dead code
* [Revision #6e04af1b78](https://github.com/MariaDB/server/commit/6e04af1b78)\
  2018-04-26 12:59:13 +0300
  * Remove dead code HAVE\_LZO1X
* [Revision #c026e2c006](https://github.com/MariaDB/server/commit/c026e2c006)\
  2018-04-26 09:25:46 +0300
  * [MDEV-15507](https://jira.mariadb.org/browse/MDEV-15507) Assertion failed in dict\_check\_sys\_tables on upgrade from 5.5
* [Revision #f033fbd9f2](https://github.com/MariaDB/server/commit/f033fbd9f2)\
  2018-04-24 12:33:56 -0700
  * Changed the test case for [MDEV-15571](https://jira.mariadb.org/browse/MDEV-15571)
* [Revision #7b5543b21d](https://github.com/MariaDB/server/commit/7b5543b21d)\
  2018-04-24 20:24:11 +0300
  * [MDEV-15030](https://jira.mariadb.org/browse/MDEV-15030) Add ASAN instrumentation to trx\_t Pool
* Merge [Revision #8346acaf80](https://github.com/MariaDB/server/commit/8346acaf80) 2018-04-24 13:00:09 +0300 - Pull request #522: Remove C++ register keyword
* [Revision #7b2bdd8984](https://github.com/MariaDB/server/commit/7b2bdd8984)\
  2017-12-27 16:03:16 +0300
  * register keyword c++17 warning
* [Revision #39a4985520](https://github.com/MariaDB/server/commit/39a4985520)\
  2018-04-24 12:14:35 +0300
  * Remove most 'register' use in C++
* [Revision #2a00bdeb4a](https://github.com/MariaDB/server/commit/2a00bdeb4a)\
  2018-04-24 12:06:28 +0300
  * Remove unused function FixNull()
* [Revision #36d28f210a](https://github.com/MariaDB/server/commit/36d28f210a)\
  2018-04-24 11:53:04 +0300
  * [MDEV-15865](https://jira.mariadb.org/browse/MDEV-15865) Crash in dict\_index\_set\_merge\_threshold() on CREATE TABLE
* Merge [Revision #4cd7979c56](https://github.com/MariaDB/server/commit/4cd7979c56) 2018-04-24 09:39:45 +0300 - Merge 10.1 into 10.2
* [Revision #619dc2b24f](https://github.com/MariaDB/server/commit/619dc2b24f)\
  2018-04-23 09:29:32 +0300
  * Fix test results after merge from 10.1
* [Revision #211842dd86](https://github.com/MariaDB/server/commit/211842dd86)\
  2018-04-23 11:22:58 +0530
  * [MDEV-15374](https://jira.mariadb.org/browse/MDEV-15374) Server hangs and aborts with long semaphore wait or assertion \`len < ((ulint) srv\_page\_size)' fails in trx\_undo\_rec\_copy upon ROLLBACK on temporary table
* [Revision #469a4b02ce](https://github.com/MariaDB/server/commit/469a4b02ce)\
  2018-04-21 20:59:26 +0300
  * Fix an intermittent test failure
* Merge [Revision #ea94717983](https://github.com/MariaDB/server/commit/ea94717983) 2018-04-21 11:58:32 +0300 - Merge 10.1 into 10.2
* [Revision #0c02c91bc1](https://github.com/MariaDB/server/commit/0c02c91bc1)\
  2018-04-19 14:11:53 +0300
  * MyRocks: [MDEV-15911](https://jira.mariadb.org/browse/MDEV-15911): Reduce debug logging on default levels in error log
* [Revision #efae12680e](https://github.com/MariaDB/server/commit/efae12680e)\
  2018-04-08 22:25:37 +0530
  * [MDEV-15611](https://jira.mariadb.org/browse/MDEV-15611) Due to the failure of foreign key detection, Galera... slave node killed himself.
* [Revision #66c14d3a8d](https://github.com/MariaDB/server/commit/66c14d3a8d)\
  2018-04-18 13:52:30 +0530
  * [MDEV-14377](https://jira.mariadb.org/browse/MDEV-14377) innodb\_zip.cmp\_per\_index failed in buildbot, result length mismatch
* [Revision #341edddc3d](https://github.com/MariaDB/server/commit/341edddc3d)\
  2018-04-18 12:39:39 +0530
  * [MDEV-15826](https://jira.mariadb.org/browse/MDEV-15826) Purge attempts to free BLOB page after BEGIN;INSERT;UPDATE;ROLLBACK
* [Revision #1d98333ad9](https://github.com/MariaDB/server/commit/1d98333ad9)\
  2018-04-17 10:35:55 -0700
  * [MDEV-15894](https://jira.mariadb.org/browse/MDEV-15894) Error, while using aggregated functions/window functions in anchor part
* [Revision #e34d3184fd](https://github.com/MariaDB/server/commit/e34d3184fd)\
  2018-04-16 10:31:30 -0700
  * [MDEV-15556](https://jira.mariadb.org/browse/MDEV-15556) MariaDB crash with big\_tables=1 and CTE
* [Revision #612850782d](https://github.com/MariaDB/server/commit/612850782d)\
  2018-04-16 08:55:15 -0700
  * [MDEV-15571](https://jira.mariadb.org/browse/MDEV-15571) Wrong results with big\_tables=1 and CTE
* [Revision #224f7af911](https://github.com/MariaDB/server/commit/224f7af911)\
  2018-04-16 07:19:19 -0700
  * [MDEV-15575](https://jira.mariadb.org/browse/MDEV-15575) different results when using CTE and big\_tables=1.
* [Revision #87af52d7dd](https://github.com/MariaDB/server/commit/87af52d7dd)\
  2018-04-16 13:21:13 +0200
  * [MDEV-15866](https://jira.mariadb.org/browse/MDEV-15866) Mysql CRASH : Json connect + [MariaDB 10.3.4](../../old-releases/release-notes-mariadb-10-3-series/mariadb-1034-release-notes.md)
* Merge [Revision #29d4ac2ceb](https://github.com/MariaDB/server/commit/29d4ac2ceb) 2018-04-16 14:19:09 +0300 - Merge pull request #665 from codership/10.2-fix-mtr-wait
* [Revision #72deed5988](https://github.com/MariaDB/server/commit/72deed5988)\
  2018-03-19 08:41:33 +0100
  * Fix mtr to be able to wait for >1 exited mysqld
* [Revision #47ea2227e5](https://github.com/MariaDB/server/commit/47ea2227e5)\
  2018-04-14 23:59:59 +0100
  * fix typo, amend last commit
* [Revision #043a9b4e1b](https://github.com/MariaDB/server/commit/043a9b4e1b)\
  2018-04-14 23:51:23 +0100
  * Windows, innodb : reduce noise from os\_file\_get\_block\_size()
* [Revision #4ea636d5e7](https://github.com/MariaDB/server/commit/4ea636d5e7)\
  2018-04-13 12:50:03 +0300
  * [MDEV-15672](https://jira.mariadb.org/browse/MDEV-15672): encryption.innodb\_encryption\_filekeys - typo in I\_S column name: ENCRYPTION\_SHCEME
* [Revision #f638c37abe](https://github.com/MariaDB/server/commit/f638c37abe)\
  2018-04-13 09:25:52 +0300
  * [MDEV-12632](https://jira.mariadb.org/browse/MDEV-12632): Source and destination overlap in memcpy, encryption.innodb-discard-import-change fails in buildbot with valgrind
* [Revision #e341da4711](https://github.com/MariaDB/server/commit/e341da4711)\
  2018-04-12 16:02:25 +0300
  * [MDEV-15580](https://jira.mariadb.org/browse/MDEV-15580): Assertion \`!lex->explain' failed in lex\_start(THD\*):
* [Revision #d13e3547e4](https://github.com/MariaDB/server/commit/d13e3547e4)\
  2018-04-13 01:56:01 +0300
  * [MDEV-14460](https://jira.mariadb.org/browse/MDEV-14460): Memory leak with only SELECT statements
* [Revision #12e2d03948](https://github.com/MariaDB/server/commit/12e2d03948)\
  2018-04-05 14:23:31 -0700
  * [MDEV-15692](https://jira.mariadb.org/browse/MDEV-15692): install\_spider.sql can fail with some collations
* [Revision #36c0116720](https://github.com/MariaDB/server/commit/36c0116720)\
  2018-04-12 11:00:48 +0300
  * [MDEV-12632](https://jira.mariadb.org/browse/MDEV-12632): Source and destination overlap in memcpy, encryption.innodb-discard-import-change fails in buildbot with valgrind
* [Revision #2f1f160979](https://github.com/MariaDB/server/commit/2f1f160979)\
  2018-04-11 14:06:29 +0300
  * [MDEV-12903](https://jira.mariadb.org/browse/MDEV-12903): encryption.innodb\_encryption\_discard\_import fails in buildbot with FOUND vs NOT FOUND
* [Revision #93aded05ea](https://github.com/MariaDB/server/commit/93aded05ea)\
  2018-04-12 03:26:39 +0300
  * Use same connection convention of specifying IPs
* [Revision #990283b65c](https://github.com/MariaDB/server/commit/990283b65c)\
  2018-04-12 02:34:51 +0300
  * Fix perfschema.hostcache\_ipv4\_max\_con
* [Revision #4c7a1a1b9e](https://github.com/MariaDB/server/commit/4c7a1a1b9e)\
  2018-04-11 23:22:33 +0100
  * [MDEV-15780](https://jira.mariadb.org/browse/MDEV-15780) : mariadb-backup does not handle absolute names in for system tablespaces
* [Revision #740fc2ae08](https://github.com/MariaDB/server/commit/740fc2ae08)\
  2018-04-10 18:07:29 -0700
  * Fixed [MDEV-15765](https://jira.mariadb.org/browse/MDEV-15765) BETWEEN not working in certain cases
* Merge [Revision #45e6d0aebf](https://github.com/MariaDB/server/commit/45e6d0aebf) 2018-04-10 17:43:18 +0300 - Merge branch '10.1' into 10.2
* [Revision #f5cb66fb97](https://github.com/MariaDB/server/commit/f5cb66fb97)\
  2018-04-10 14:27:18 +0400
  * Test cleanup for [MDEV-15833](https://jira.mariadb.org/browse/MDEV-15833) (uncommenting forgotten tests)
* [Revision #4d9c5844b8](https://github.com/MariaDB/server/commit/4d9c5844b8)\
  2018-04-10 13:15:57 +0400
  * [MDEV-15833](https://jira.mariadb.org/browse/MDEV-15833) Row format replication between LONGBLOB and MEDIUMBLOB does not work for long values
* [Revision #141592cedb](https://github.com/MariaDB/server/commit/141592cedb)\
  2018-04-10 02:07:31 +0300
  * Clean up a test
* [Revision #7b16291c36](https://github.com/MariaDB/server/commit/7b16291c36)\
  2018-04-05 13:17:17 +0100
  * [MDEV-15707](https://jira.mariadb.org/browse/MDEV-15707) : deadlock in Innodb IO code, caused by change buffering.
* [Revision #b4c2ceb214](https://github.com/MariaDB/server/commit/b4c2ceb214)\
  2018-04-07 15:03:15 +0300
  * [MDEV-15769](https://jira.mariadb.org/browse/MDEV-15769): Assertion \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed
* [Revision #1cb2e0333d](https://github.com/MariaDB/server/commit/1cb2e0333d)\
  2018-04-07 14:05:28 +0300
  * [MDEV-12466](https://jira.mariadb.org/browse/MDEV-12466) : Assertion \`thd->transaction.stmt.is\_empty() || thd->in\_sub\_stmt || ...
* [Revision #5ccf3f96ac](https://github.com/MariaDB/server/commit/5ccf3f96ac)\
  2018-04-05 17:36:59 +0400
  * Fix misuse of MY\_CHECK\_CXX\_COMPILER\_FLAG
* [Revision #4fde1361a6](https://github.com/MariaDB/server/commit/4fde1361a6)\
  2018-04-05 15:01:17 +0300
  * [MDEV-15553](https://jira.mariadb.org/browse/MDEV-15553) Assertion failed in dict\_table\_get\_col\_name
* [Revision #bc2501453c](https://github.com/MariaDB/server/commit/bc2501453c)\
  2018-04-03 16:58:35 +0300
  * Remove an unused variable
* [Revision #3c21eccb8c](https://github.com/MariaDB/server/commit/3c21eccb8c)\
  2018-04-03 15:58:13 +0300
  * [MDEV-15764](https://jira.mariadb.org/browse/MDEV-15764) InnoDB may write uninitialized garbage to redo log
* [Revision #d9c5a46678](https://github.com/MariaDB/server/commit/d9c5a46678)\
  2018-04-03 16:43:36 +0530
  * [MDEV-15737](https://jira.mariadb.org/browse/MDEV-15737) assertion in mariadb-backup.exe!recv\_calc\_lsn\_on\_data\_add()
* [Revision #6223f1dd98](https://github.com/MariaDB/server/commit/6223f1dd98)\
  2018-03-25 22:12:38 +0200
  * [MDEV-15579](https://jira.mariadb.org/browse/MDEV-15579) Crash in Item\_field::used\_tables() called by Item::derived\_field\_transformer\_for\_having
* [Revision #27c24808f7](https://github.com/MariaDB/server/commit/27c24808f7)\
  2018-03-29 22:13:01 +0000
  * [MDEV-15636](https://jira.mariadb.org/browse/MDEV-15636) mariadb-backup --lock-ddl-per-table hangs if ALTER table is running concurrently.
* [Revision #a1d68faa38](https://github.com/MariaDB/server/commit/a1d68faa38)\
  2018-03-29 21:41:05 +0000
  * CMake : Move INNODB\_DISALLOW\_WRITES from top-level CMakeLists.txt to innodb
* [Revision #55f4e4800b](https://github.com/MariaDB/server/commit/55f4e4800b)\
  2018-03-29 22:00:07 +0300
  * [MDEV-15325](https://jira.mariadb.org/browse/MDEV-15325) fixup: Disable test for --embedded
* [Revision #402c7584a8](https://github.com/MariaDB/server/commit/402c7584a8)\
  2018-03-23 12:58:11 +1100
  * [MDEV-13785](https://jira.mariadb.org/browse/MDEV-13785): move defination HAVE\_LARGE\_PAGES -> HAVE\_LINUX\_LARGE\_PAGES
* [Revision #014dfe473a](https://github.com/MariaDB/server/commit/014dfe473a)\
  2018-03-29 16:58:59 +0300
  * [MDEV-15719](https://jira.mariadb.org/browse/MDEV-15719): Adjust a test case
* [Revision #3eb73bf630](https://github.com/MariaDB/server/commit/3eb73bf630)\
  2018-03-24 08:38:08 +0200
  * Remove unnecessary SysTablespace references
* [Revision #622d21e2b8](https://github.com/MariaDB/server/commit/622d21e2b8)\
  2018-03-27 12:25:30 +0300
  * row\_drop\_table\_for\_mysql(): Use a constant string
* [Revision #b922741074](https://github.com/MariaDB/server/commit/b922741074)\
  2018-03-29 13:59:21 +0300
  * [MDEV-15472](https://jira.mariadb.org/browse/MDEV-15472): Assertion \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failure
* [Revision #adaee46a90](https://github.com/MariaDB/server/commit/adaee46a90)\
  2018-03-29 13:22:59 +0300
  * [MDEV-15682](https://jira.mariadb.org/browse/MDEV-15682) mariadb-backup.unsupported\_redo fails in buildbot with wrong result code
* [Revision #6cccef21a6](https://github.com/MariaDB/server/commit/6cccef21a6)\
  2018-03-29 13:22:16 +0300
  * [MDEV-15720](https://jira.mariadb.org/browse/MDEV-15720) ib\_buffer\_pool unnecessarily includes the temporary tablespace
* [Revision #4d9969c216](https://github.com/MariaDB/server/commit/4d9969c216)\
  2018-03-29 12:55:24 +0300
  * [MDEV-15719](https://jira.mariadb.org/browse/MDEV-15719) ALTER TABLE…ALGORITHM=INPLACE is unnecessarily refused due to innodb\_force\_recovery
* [Revision #0d2fffb612](https://github.com/MariaDB/server/commit/0d2fffb612)\
  2018-03-29 11:08:32 +0300
  * [MDEV-15686](https://jira.mariadb.org/browse/MDEV-15686): Loading MyRocks plugin back after it has been unloaded causes a crash
* [Revision #d18a66147c](https://github.com/MariaDB/server/commit/d18a66147c)\
  2018-03-28 20:40:09 +0300
  * recv\_validate\_tablespace(): Fix -Wmissing-fallthrough
* [Revision #5beddfa08c](https://github.com/MariaDB/server/commit/5beddfa08c)\
  2018-03-28 20:39:57 +0300
  * fil\_node\_open\_file(): Add a missing space to message
* [Revision #011586c04d](https://github.com/MariaDB/server/commit/011586c04d)\
  2018-03-27 17:21:22 +0300
  * [MDEV-15686](https://jira.mariadb.org/browse/MDEV-15686): Loading MyRocks plugin back after it has been unloaded causes a crash
* [Revision #907aae2502](https://github.com/MariaDB/server/commit/907aae2502)\
  2018-03-28 14:28:58 +0300
  * [MDEV-15708](https://jira.mariadb.org/browse/MDEV-15708): rocksdb.mariadb\_plugin fails on winx64, Cannot enable tc-log at run-time
* [Revision #3b119d9d30](https://github.com/MariaDB/server/commit/3b119d9d30)\
  2018-03-28 13:14:24 +0300
  * [MDEV-11531](https://jira.mariadb.org/browse/MDEV-11531): encryption.innodb\_lotoftables failed in buildbot
* [Revision #aafb9d44d6](https://github.com/MariaDB/server/commit/aafb9d44d6)\
  2018-03-27 13:31:07 -0400
  * bump the VERSION
* [Revision #73af8af094](https://github.com/MariaDB/server/commit/73af8af094)\
  2018-03-27 13:47:56 +0530
  * [MDEV-15325](https://jira.mariadb.org/browse/MDEV-15325) Incomplete validation of missing tablespace during recovery
* [Revision #60438451c3](https://github.com/MariaDB/server/commit/60438451c3)\
  2018-03-26 21:22:40 +0300
  * [MDEV-14843](https://jira.mariadb.org/browse/MDEV-14843): Assertion \`s\_tx\_list.size() == 0' failed in myrocks::Rdb\_transaction::term\_mutex

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
