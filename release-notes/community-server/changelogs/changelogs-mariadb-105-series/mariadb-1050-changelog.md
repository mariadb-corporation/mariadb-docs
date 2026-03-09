# MariaDB 10.5.0 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download](https://downloads.mariadb.org/mariadb/10.5.0/)[Release Notes](../../old-releases/10.5/10.5.0.md)[Changelog](mariadb-1050-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 3 Dec 2019

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.0.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #7c7f9bef28](https://github.com/MariaDB/server/commit/7c7f9bef28)\
  2019-11-25 14:41:13 +0100
  * Fix shutdown hang in dict\_stats , caused by [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264)
* [Revision #312569e2fd](https://github.com/MariaDB/server/commit/312569e2fd)\
  2019-11-25 09:39:51 +0200
  * [MDEV-21132](https://jira.mariadb.org/browse/MDEV-21132) Remove buf\_page\_t::newest\_modification
* [Revision #777b399618](https://github.com/MariaDB/server/commit/777b399618)\
  2019-06-30 14:53:52 +0300
  * [MDEV-19903](https://jira.mariadb.org/browse/MDEV-19903) Setup default partitions for system versioning
* [Revision #f60eeee952](https://github.com/MariaDB/server/commit/f60eeee952)\
  2019-11-21 01:51:34 +0100
  * [MDEV-21062](https://jira.mariadb.org/browse/MDEV-21062) Do not use popen() in text mode for mysql\_upgrade.
* [Revision #9d4da68502](https://github.com/MariaDB/server/commit/9d4da68502)\
  2019-11-22 07:44:05 +0100
  * Fix MTR suppressions in inconsistency voting tests (#1412)
* [Revision #e76edf700f](https://github.com/MariaDB/server/commit/e76edf700f)\
  2019-11-21 12:29:07 +0400
  * [MDEV-21110](https://jira.mariadb.org/browse/MDEV-21110) Unify turn\_parser\_debug\_on() in sql\_yacc.yy and sql\_yacc\_ora.yy
* [Revision #747bed2e72](https://github.com/MariaDB/server/commit/747bed2e72)\
  2019-11-21 05:34:00 +0800
  * Upgrade accidentally downgraded libmariadb
* Merge [Revision #5b686af2ec](https://github.com/MariaDB/server/commit/5b686af2ec) 2019-11-20 15:47:16 +0200 - Merge 10.4 into 10.5
* [Revision #6cedb671e9](https://github.com/MariaDB/server/commit/6cedb671e9)\
  2019-11-20 14:12:53 +0800
  * [MDEV-21088](https://jira.mariadb.org/browse/MDEV-21088) Table cannot be loaded after instant ADD/DROP COLUMN
* Merge [Revision #1c92406337](https://github.com/MariaDB/server/commit/1c92406337) 2019-11-20 14:11:54 +0800 - Merge 10.3 into 10.4
* [Revision #aa3d28ac34](https://github.com/MariaDB/server/commit/aa3d28ac34)\
  2019-11-20 14:02:30 +0800
  * [MDEV-21088](https://jira.mariadb.org/browse/MDEV-21088): Follow-up fix for ROW\_FORMAT=REDUNDANT
* [Revision #89f487f2e2](https://github.com/MariaDB/server/commit/89f487f2e2)\
  2019-11-20 13:03:34 +0800
  * [MDEV-21088](https://jira.mariadb.org/browse/MDEV-21088) Table cannot be loaded after instant ADD/DROP COLUMN
* [Revision #7b5654f3e9](https://github.com/MariaDB/server/commit/7b5654f3e9)\
  2019-11-20 00:33:32 +0400
  * [MDEV-14667](https://jira.mariadb.org/browse/MDEV-14667) Assertion \`used\_parts > 0' failed in ha\_partition::init\_record\_priority\_queue.
* [Revision #b40cab657b](https://github.com/MariaDB/server/commit/b40cab657b)\
  2019-11-19 15:55:36 +0400
  * Bison parser cleanups: define yyerror() instead of MYSQLerror()/ORAerror()
* [Revision #927ea88084](https://github.com/MariaDB/server/commit/927ea88084)\
  2019-11-20 13:19:01 +0300
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) fix unused variable ‘save\_psi\_thread’
* [Revision #daabc5cc68](https://github.com/MariaDB/server/commit/daabc5cc68)\
  2019-11-20 13:18:54 +0300
  * [MDEV-20729](https://jira.mariadb.org/browse/MDEV-20729) Fix REFERENCES constraint in column definition
* [Revision #5130f5206c](https://github.com/MariaDB/server/commit/5130f5206c)\
  2019-11-20 13:18:31 +0300
  * [MDEV-20480](https://jira.mariadb.org/browse/MDEV-20480) Obsolete internal parser for FK in InnoDB
* [Revision #20b474be5b](https://github.com/MariaDB/server/commit/20b474be5b)\
  2019-11-18 20:05:28 +0530
  * [MDEV-21063](https://jira.mariadb.org/browse/MDEV-21063) Very many test failures on big-endian PowerPC
* [Revision #251c6e1726](https://github.com/MariaDB/server/commit/251c6e1726)\
  2019-11-18 16:41:21 +0400
  * [MDEV-21073](https://jira.mariadb.org/browse/MDEV-21073) Collect different grammar rules into a single chunk
* Merge [Revision #a9846f3299](https://github.com/MariaDB/server/commit/a9846f3299) 2019-11-19 10:45:28 +0800 - Merge 10.4 into 10.5
* Merge [Revision #589a1235b6](https://github.com/MariaDB/server/commit/589a1235b6) 2019-11-19 01:32:50 +0200 - Merge 10.3 into 10.4
* [Revision #39d8652ca5](https://github.com/MariaDB/server/commit/39d8652ca5)\
  2019-11-19 00:42:10 +0200
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) follow-up: Remove unused code
* Merge [Revision #613e13072c](https://github.com/MariaDB/server/commit/613e13072c) 2019-11-19 00:37:01 +0200 - Merge 10.2 into 10.3
* [Revision #b80df9eba2](https://github.com/MariaDB/server/commit/b80df9eba2)\
  2019-11-17 21:57:16 +0200
  * [MDEV-21069](https://jira.mariadb.org/browse/MDEV-21069) Crash on DROP TABLE if the data file is corrupted
* [Revision #bd2b05df6c](https://github.com/MariaDB/server/commit/bd2b05df6c)\
  2019-11-15 11:14:25 +0100
  * update create\_w\_max\_indexes\_128.result
* [Revision #409ed60bb8](https://github.com/MariaDB/server/commit/409ed60bb8)\
  2019-11-16 13:18:24 +0300
  * Fix compile failure on Windows: use explicit type casts
* [Revision #86167e908f](https://github.com/MariaDB/server/commit/86167e908f)\
  2019-11-15 23:37:28 +0300
  * [MDEV-20611](https://jira.mariadb.org/browse/MDEV-20611): MRR scan over partitioned InnoDB table produces "Out of memory" error
* [Revision #77a245fe56](https://github.com/MariaDB/server/commit/77a245fe56)\
  2019-11-17 20:04:11 +0200
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Remove an unused return value
* [Revision #009674dc52](https://github.com/MariaDB/server/commit/009674dc52)\
  2019-11-15 15:37:25 +0100
  * Fix a couple of clang-cl warnings
* [Revision #6df0bb7d38](https://github.com/MariaDB/server/commit/6df0bb7d38)\
  2019-11-13 21:12:48 +0100
  * [MDEV-21062](https://jira.mariadb.org/browse/MDEV-21062) Buildbot, Windows - sporadically missing lines from mtr's "exec"
* [Revision #6d373e8b81](https://github.com/MariaDB/server/commit/6d373e8b81)\
  2019-11-15 17:37:59 +0400
  * [MDEV-21064](https://jira.mariadb.org/browse/MDEV-21064) Add a new class sp\_expr\_lex and a new grammar rule expr\_lex
* [Revision #c233d406cb](https://github.com/MariaDB/server/commit/c233d406cb)\
  2019-11-15 23:51:49 +0100
  * Fix compile error on centos6. it does not like std::this\_thread::sleep()
* [Revision #15c7f684ec](https://github.com/MariaDB/server/commit/15c7f684ec)\
  2019-11-15 22:54:42 +0200
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264): Minor cleanup
* [Revision #a69cff295c](https://github.com/MariaDB/server/commit/a69cff295c)\
  2019-11-15 19:55:40 +0200
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264): Remove IORequest::IGNORE\_MISSING
* [Revision #8040998624](https://github.com/MariaDB/server/commit/8040998624)\
  2019-11-15 19:55:13 +0200
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264): Fix some white space
* [Revision #37f1ab2323](https://github.com/MariaDB/server/commit/37f1ab2323)\
  2019-11-14 16:58:58 +0200
  * [MDEV-21054](https://jira.mariadb.org/browse/MDEV-21054) Crash on shutdown due to btr\_search\_latches=NULL
* [Revision #a808c18b73](https://github.com/MariaDB/server/commit/a808c18b73)\
  2019-11-13 18:14:44 +0100
  * Make .clang-format work with clang-8
* [Revision #4e30a57e6b](https://github.com/MariaDB/server/commit/4e30a57e6b)\
  2019-10-30 08:08:19 +0100
  * [MDEV-20839](https://jira.mariadb.org/browse/MDEV-20839) innodb-redo-badkey fails sporadically
* [Revision #5e62b6a5e0](https://github.com/MariaDB/server/commit/5e62b6a5e0)\
  2019-10-29 22:37:12 +0100
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) Use threadpool for Innodb background work.
* [Revision #00ee8d85c9](https://github.com/MariaDB/server/commit/00ee8d85c9)\
  2019-10-29 18:17:24 +0100
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264): Add threadpool library
* [Revision #7e08dd85d6](https://github.com/MariaDB/server/commit/7e08dd85d6)\
  2019-10-29 18:32:14 +0100
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) prerequisite patch, ha\_preshutdown.
* [Revision #e7549917e1](https://github.com/MariaDB/server/commit/e7549917e1)\
  2019-10-29 18:35:38 +0100
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) - prerequisite patch - true background THDs
* [Revision #2fb23b896e](https://github.com/MariaDB/server/commit/2fb23b896e)\
  2019-10-29 18:37:14 +0100
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) prerequisite patch, enable thr\_timer in embedded
* [Revision #ad17c98dd5](https://github.com/MariaDB/server/commit/ad17c98dd5)\
  2019-10-29 18:20:21 +0100
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) - prerequisite patch, periodic thr\_timer
* [Revision #786b004972](https://github.com/MariaDB/server/commit/786b004972)\
  2019-11-15 14:55:38 +0200
  * Cleanup: More use of mtr\_memo\_type\_t
* Merge [Revision #ae90f8431b](https://github.com/MariaDB/server/commit/ae90f8431b) 2019-11-14 14:49:20 +0200 - Merge 10.4 into 10.5
* Merge [Revision #89ae01fd00](https://github.com/MariaDB/server/commit/89ae01fd00) 2019-11-14 13:23:36 +0200 - Merge 10.3 into 10.4
* [Revision #3d4a801533](https://github.com/MariaDB/server/commit/3d4a801533)\
  2019-11-14 11:40:33 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) preparation: Replace mtr\_x\_lock() and friends
* Merge [Revision #746ee78535](https://github.com/MariaDB/server/commit/746ee78535) 2019-11-14 13:22:29 +0200 - [MDEV-20949](https://jira.mariadb.org/browse/MDEV-20949): Merge 10.3 into 10.4
* Merge [Revision #4ded5fb9ac](https://github.com/MariaDB/server/commit/4ded5fb9ac) 2019-11-14 11:26:49 +0200 - [MDEV-20949](https://jira.mariadb.org/browse/MDEV-20949): Merge 10.2 into 10.3
* [Revision #98694ab0cb](https://github.com/MariaDB/server/commit/98694ab0cb)\
  2019-11-03 00:15:29 +0300
  * [MDEV-20949](https://jira.mariadb.org/browse/MDEV-20949) Stop issuing 'row size' error on DML
* Merge [Revision #3bee95d769](https://github.com/MariaDB/server/commit/3bee95d769) 2019-11-14 13:20:57 +0200 - Merge 10.3 into 10.4
* Merge [Revision #bc5cfe7769](https://github.com/MariaDB/server/commit/bc5cfe7769) 2019-11-14 10:51:06 +0200 - Merge 10.2 into 10.3
* [Revision #3b573c0783](https://github.com/MariaDB/server/commit/3b573c0783)\
  2019-11-13 09:51:28 +0200
  * Clean up mtr\_t::commit() further
* [Revision #abd45cdc38](https://github.com/MariaDB/server/commit/abd45cdc38)\
  2019-11-13 09:26:10 +0200
  * [MDEV-20934](https://jira.mariadb.org/browse/MDEV-20934): Correct a debug assertion
* [Revision #f127fb9807](https://github.com/MariaDB/server/commit/f127fb9807)\
  2019-11-12 20:05:17 +0900
  * Fix a typo in mariadb-plugin-mroonga.prerm
* [Revision #d4edb0510e](https://github.com/MariaDB/server/commit/d4edb0510e)\
  2019-11-13 18:53:59 +0300
  * [MDEV-20646](https://jira.mariadb.org/browse/MDEV-20646): 10.3.18 is slower than 10.3.17
* [Revision #caa79081c3](https://github.com/MariaDB/server/commit/caa79081c3)\
  2019-10-14 12:08:28 +0530
  * [MDEV-20707](https://jira.mariadb.org/browse/MDEV-20707): Missing memory barrier in parallel replication error handler in wait\_for\_prior\_commit()
* [Revision #c454b8964c](https://github.com/MariaDB/server/commit/c454b8964c)\
  2019-10-04 00:45:32 -0700
  * [MDEV-4476](https://jira.mariadb.org/browse/MDEV-4476): mytop tracker
* Merge [Revision #c99470b366](https://github.com/MariaDB/server/commit/c99470b366) 2019-11-13 20:38:14 +0200 - Merge 10.4 into 10.5
* [Revision #49019dde65](https://github.com/MariaDB/server/commit/49019dde65)\
  2019-11-13 18:35:04 +0200
  * [MDEV-17138](https://jira.mariadb.org/browse/MDEV-17138) follow-up: Optimize index page creation
* [Revision #2b7aa60b7e](https://github.com/MariaDB/server/commit/2b7aa60b7e)\
  2019-11-13 14:34:52 +0200
  * Use constexpr for constants on data pages
* [Revision #ae72205e31](https://github.com/MariaDB/server/commit/ae72205e31)\
  2019-11-12 18:15:26 +0700
  * cleanup: replace List\_iterator(\_fast) in handler0alter.cc
* [Revision #83a0eaec08](https://github.com/MariaDB/server/commit/83a0eaec08)\
  2019-11-13 00:32:27 +0900
  * [MDEV-18987](https://jira.mariadb.org/browse/MDEV-18987) bug in "load data local infile xxx replace into " (#1408)
* [Revision #29b11cffb5](https://github.com/MariaDB/server/commit/29b11cffb5)\
  2019-11-13 13:16:46 +0400
  * [MDEV-21043](https://jira.mariadb.org/browse/MDEV-21043) Collect different bison %type declarations into a single chunk
* Merge [Revision #1fe6e5a1a5](https://github.com/MariaDB/server/commit/1fe6e5a1a5) 2019-11-12 17:21:37 +0200 - Merge 10.4 into 10.5
* Merge [Revision #33cb10d4e9](https://github.com/MariaDB/server/commit/33cb10d4e9) 2019-11-12 16:55:44 +0200 - Merge 10.3 into 10.4
* Merge [Revision #5098d708a0](https://github.com/MariaDB/server/commit/5098d708a0) 2019-11-12 16:30:57 +0200 - Merge 10.2 into 10.3
* [Revision #2570cb8b91](https://github.com/MariaDB/server/commit/2570cb8b91)\
  2019-11-12 15:46:57 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) preparation: Clean up mtr\_t
* [Revision #dc8380b65d](https://github.com/MariaDB/server/commit/dc8380b65d)\
  2019-11-12 14:41:24 +0200
  * [MDEV-14602](https://jira.mariadb.org/browse/MDEV-14602): Cleanup recv\_dblwr\_t::find\_page()
* Merge [Revision #2350066e63](https://github.com/MariaDB/server/commit/2350066e63) 2019-11-12 14:36:37 +0200 - Merge 10.1 into 10.2
* [Revision #7df07c7666](https://github.com/MariaDB/server/commit/7df07c7666)\
  2019-11-05 15:01:29 +0530
  * [MDEV-20953](https://jira.mariadb.org/browse/MDEV-20953): binlog\_encryption.rpl\_corruption failed in buildbot due to wrong error code
* [Revision #40e65e878e](https://github.com/MariaDB/server/commit/40e65e878e)\
  2019-11-11 21:12:14 +0200
  * rpl\_semi\_sync\_gtid\_reconnect results merge
* Merge [Revision #d103c5a489](https://github.com/MariaDB/server/commit/d103c5a489) 2019-11-11 16:28:21 +0200 - merge 10.2->10.3 with conflict resolutions
* Merge [Revision #26fd880d5e](https://github.com/MariaDB/server/commit/26fd880d5e) 2019-11-11 16:03:43 +0200 - manual merge 10.1->10.2
* [Revision #13db50fc03](https://github.com/MariaDB/server/commit/13db50fc03)\
  2019-11-06 17:05:58 +0200
  * [MDEV-19376](https://jira.mariadb.org/browse/MDEV-19376) Repl\_semi\_sync\_master::commit\_trx assertion failure: ... || !m\_active\_tranxs->is\_tranx\_end\_pos(trx\_wait\_binlog\_name, trx\_wait\_binlog\_pos)
* [Revision #c4a844ca51](https://github.com/MariaDB/server/commit/c4a844ca51)\
  2019-11-08 08:03:49 +0100
  * [MDEV-20981](https://jira.mariadb.org/browse/MDEV-20981) wsrep\_sst\_mariadb-backup fails silently when mariadb-backup is not installed (#1406)
* [Revision #b1ab2ba583](https://github.com/MariaDB/server/commit/b1ab2ba583)\
  2019-11-07 15:24:21 +0530
  * [MDEV-20519](https://jira.mariadb.org/browse/MDEV-20519): Query plan regression with optimizer\_use\_condition\_selectivity > 1
* [Revision #e5f99a0c0c](https://github.com/MariaDB/server/commit/e5f99a0c0c)\
  2019-10-30 13:55:52 +0300
  * [MDEV-20297](https://jira.mariadb.org/browse/MDEV-20297) Support C++11 range-based for loop for List
* [Revision #e26d049197](https://github.com/MariaDB/server/commit/e26d049197)\
  2019-11-12 12:20:30 +0400
  * [MDEV-21023](https://jira.mariadb.org/browse/MDEV-21023) Move LEX methods and related functions from sql\_yacc.yy to sql\_lex.cc
* [Revision #68ed3a81f2](https://github.com/MariaDB/server/commit/68ed3a81f2)\
  2019-11-09 21:03:23 +0300
  * [MDEV-20854](https://jira.mariadb.org/browse/MDEV-20854): ANALYZE for statements: not clear where the time is spent
* Merge [Revision #0117d0e65a](https://github.com/MariaDB/server/commit/0117d0e65a) 2019-11-11 15:21:58 +0200 - Merge 10.4 into 10.5
* [Revision #0308de94ee](https://github.com/MariaDB/server/commit/0308de94ee)\
  2019-11-11 15:09:23 +0200
  * [MDEV-17138](https://jira.mariadb.org/browse/MDEV-17138) follow-up: Optimize fseg\_create()
* Merge [Revision #3da895a736](https://github.com/MariaDB/server/commit/3da895a736) 2019-11-11 15:03:46 +0200 - Merge 10.3 into 10.4
* Merge [Revision #4fcfdb60e7](https://github.com/MariaDB/server/commit/4fcfdb60e7) 2019-11-11 14:56:51 +0200 - Merge 10.2 into 10.3
* [Revision #142442d571](https://github.com/MariaDB/server/commit/142442d571)\
  2019-11-11 14:18:50 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Cleanup XDES\_CLEAN\_BIT
* [Revision #878bc854d9](https://github.com/MariaDB/server/commit/878bc854d9)\
  2019-11-11 14:07:01 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Clean up dict\_hdr\_create()
* [Revision #33f74e8fcf](https://github.com/MariaDB/server/commit/33f74e8fcf)\
  2019-11-11 14:02:38 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Clean up IMPORT TABLESPACE
* [Revision #dfdd96214b](https://github.com/MariaDB/server/commit/dfdd96214b)\
  2019-11-11 13:56:55 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Clean up btr\_root\_raise\_and\_insert()
* [Revision #fc2ca2be4e](https://github.com/MariaDB/server/commit/fc2ca2be4e)\
  2019-11-11 13:43:24 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Clean up page allocation
* [Revision #98e1d603bf](https://github.com/MariaDB/server/commit/98e1d603bf)\
  2019-11-08 11:04:26 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Optimize writing BTR\_EXTERN\_LEN
* [Revision #3621df70ca](https://github.com/MariaDB/server/commit/3621df70ca)\
  2019-11-11 13:26:19 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Clean up rtr\_adjust\_upper\_level()
* [Revision #29d67d051a](https://github.com/MariaDB/server/commit/29d67d051a)\
  2019-11-11 13:36:21 +0200
  * Cleanup btr\_page\_get\_prev(), btr\_page\_get\_next()
* [Revision #1d2458f813](https://github.com/MariaDB/server/commit/1d2458f813)\
  2019-11-11 13:26:19 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Clean up rtr\_adjust\_upper\_level()
* [Revision #bce71a2909](https://github.com/MariaDB/server/commit/bce71a2909)\
  2019-11-08 13:32:25 +0200
  * Cleanup: Replace xdes\_set\_bit()
* [Revision #5ed54e78ac](https://github.com/MariaDB/server/commit/5ed54e78ac)\
  2019-11-08 12:43:04 +0200
  * Cleanup: Remove redundant XDES\_FREE\_BIT parameters
* Merge [Revision #74b7d0182d](https://github.com/MariaDB/server/commit/74b7d0182d) 2019-11-08 13:43:45 +0200 - Merge 10.4 into 10.5
* [Revision #15b713cadc](https://github.com/MariaDB/server/commit/15b713cadc)\
  2019-11-08 13:36:20 +0200
  * [MDEV-17138](https://jira.mariadb.org/browse/MDEV-17138) follow-up: Use MLOG\_MEMSET in xdes\_init()
* [Revision #b5ef7ffa59](https://github.com/MariaDB/server/commit/b5ef7ffa59)\
  2019-11-08 12:46:08 +0200
  * Use uint16\_t for FIL\_PAGE\_TYPE
* [Revision #a6d614fb4a](https://github.com/MariaDB/server/commit/a6d614fb4a)\
  2019-11-08 11:04:26 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) preparation: Remove redundant writes
* [Revision #5b72e8136f](https://github.com/MariaDB/server/commit/5b72e8136f)\
  2019-11-08 06:29:20 +0200
  * Cleanup: Do not pass mtr\_t\* as NULL
* [Revision #5d596064d6](https://github.com/MariaDB/server/commit/5d596064d6)\
  2019-11-08 06:28:29 +0200
  * Cleanup: Define FIL\_PAGE\_TYPE constants as constexpr
* Merge [Revision #52246dff2c](https://github.com/MariaDB/server/commit/52246dff2c) 2019-11-08 09:43:41 +0200 - Merge 10.4 into 10.5
* [Revision #78d0d2cdc5](https://github.com/MariaDB/server/commit/78d0d2cdc5)\
  2019-11-08 09:41:06 +0200
  * Cleanup: Remove mach\_read\_ulint()
* [Revision #8a5eb4141b](https://github.com/MariaDB/server/commit/8a5eb4141b)\
  2019-11-08 08:59:59 +0200
  * [MDEV-17138](https://jira.mariadb.org/browse/MDEV-17138) follow-up: Use MLOG\_MEMSET for writing FIL\_NULL
* [Revision #db56543993](https://github.com/MariaDB/server/commit/db56543993)\
  2019-11-07 20:25:04 +0300
  * Compilation fix with partitioning off ([MDEV-17553](https://jira.mariadb.org/browse/MDEV-17553))
* [Revision #1e73d7d6c6](https://github.com/MariaDB/server/commit/1e73d7d6c6)\
  2019-11-07 19:21:42 +0300
  * [MDEV-17553](https://jira.mariadb.org/browse/MDEV-17553) Enable setting start datetime for interval partitioned history of system versioned tables
* Merge [Revision #77e8a311e1](https://github.com/MariaDB/server/commit/77e8a311e1) 2019-11-07 10:34:33 +0200 - Merge 10.4 into 10.5
* Merge [Revision #3ad37ed0eb](https://github.com/MariaDB/server/commit/3ad37ed0eb) 2019-11-05 16:15:20 +0100 - Merge 10.4 into 10.5
* [Revision #46f2f24ec4](https://github.com/MariaDB/server/commit/46f2f24ec4)\
  2019-11-05 22:37:45 +0400
  * [MDEV-20985](https://jira.mariadb.org/browse/MDEV-20985) Add LEX methods stmt\_drop\_{function|procedure}() and stmt\_alter\_{function|procedure}\_start()
* [Revision #79e295b601](https://github.com/MariaDB/server/commit/79e295b601)\
  2019-11-05 17:35:26 +0400
  * Cleanup: moving '(' after the stmt\_create\_stored\_function\_start() call
* [Revision #0858500f2f](https://github.com/MariaDB/server/commit/0858500f2f)\
  2019-11-05 17:06:34 +0400
  * Cleanup: reusing opt\_sp\_parenthesized\_fdparam\_list and removing duplicate rules.
* [Revision #51fb39bf17](https://github.com/MariaDB/server/commit/51fb39bf17)\
  2019-11-04 16:13:43 +0200
  * [MDEV-19586](https://jira.mariadb.org/browse/MDEV-19586): Restore pointer indirection for recv\_t::data
* [Revision #f89436b592](https://github.com/MariaDB/server/commit/f89436b592)\
  2019-11-04 15:11:51 +0200
  * [MDEV-18115](https://jira.mariadb.org/browse/MDEV-18115): Remove a unused variable
* [Revision #8f40c029db](https://github.com/MariaDB/server/commit/8f40c029db)\
  2019-11-04 15:00:44 +0200
  * Fix -Wmaybe-uninitialized
* [Revision #541b00a3ba](https://github.com/MariaDB/server/commit/541b00a3ba)\
  2019-11-04 09:26:27 +0200
  * [MDEV-19586](https://jira.mariadb.org/browse/MDEV-19586): Clean up recv\_t a little
* [Revision #64a02e4fa2](https://github.com/MariaDB/server/commit/64a02e4fa2)\
  2019-11-04 08:52:05 +0200
  * [MDEV-19586](https://jira.mariadb.org/browse/MDEV-19586): Add const qualifiers
* [Revision #9d1bbdc56c](https://github.com/MariaDB/server/commit/9d1bbdc56c)\
  2019-11-03 12:22:55 +0100
  * Fix linking errors on Windows
* [Revision #3ef01d1118](https://github.com/MariaDB/server/commit/3ef01d1118)\
  2019-11-03 12:11:23 +0100
  * compilation failure, gcc 8.3.0
* [Revision #e5fed3b94d](https://github.com/MariaDB/server/commit/e5fed3b94d)\
  2019-11-01 16:56:44 +0200
  * [MDEV-19586](https://jira.mariadb.org/browse/MDEV-19586): Avoid std::map::emplace()
* [Revision #b7fc2c899e](https://github.com/MariaDB/server/commit/b7fc2c899e)\
  2019-11-01 15:06:31 +0200
  * Refactor recv\_sys\_t::recs\_t into page\_recv\_t
* [Revision #2aa1f77ef1](https://github.com/MariaDB/server/commit/2aa1f77ef1)\
  2019-11-01 14:12:55 +0200
  * [MDEV-19586](https://jira.mariadb.org/browse/MDEV-19586): Rename recv\_sys.empty() to recv\_sys.clear()
* [Revision #00c3a28820](https://github.com/MariaDB/server/commit/00c3a28820)\
  2019-10-11 14:12:38 +0200
  * cleanup: data type plugins
* [Revision #779978217c](https://github.com/MariaDB/server/commit/779978217c)\
  2019-10-10 17:40:21 +0200
  * Data type plugins - minor fixes
* [Revision #82b62924d7](https://github.com/MariaDB/server/commit/82b62924d7)\
  2019-10-30 14:58:31 +0200
  * Fixed wrong result files in test suite
* [Revision #74b4171591](https://github.com/MariaDB/server/commit/74b4171591)\
  2019-10-30 16:05:36 +0400
  * sql\_yacc\_ora.yy: syncing grammar for "[MDEV-18844](https://jira.mariadb.org/browse/MDEV-18844) Implement EXCEPT ALL and INTERSECT ALL operations"
* [Revision #f2cff12556](https://github.com/MariaDB/server/commit/f2cff12556)\
  2019-10-30 11:56:13 +0400
  * [MDEV-20924](https://jira.mariadb.org/browse/MDEV-20924) Unify grammar rules: field\_type\_string and sp\_param\_field\_type\_string
* [Revision #0ccfdc8eff](https://github.com/MariaDB/server/commit/0ccfdc8eff)\
  2019-10-30 07:31:39 +0200
  * Remove InnoDB wrappers of \<string.h> functions
* [Revision #7440e61a64](https://github.com/MariaDB/server/commit/7440e61a64)\
  2019-10-22 18:52:56 +0200
  * [MDEV-18115](https://jira.mariadb.org/browse/MDEV-18115): Remove the only async write (of redo log)
* Merge [Revision #2b710090aa](https://github.com/MariaDB/server/commit/2b710090aa) 2019-10-29 16:31:40 +0200 - Merge 10.4 into 10.5
* [Revision #b62a846642](https://github.com/MariaDB/server/commit/b62a846642)\
  2019-10-29 13:33:38 +0400
  * [MDEV-20913](https://jira.mariadb.org/browse/MDEV-20913) sql\_mode=ORACLE: INET6 does not work as a routine parameter type and return type
* [Revision #f1e9a0acc8](https://github.com/MariaDB/server/commit/f1e9a0acc8)\
  2019-10-29 07:22:41 +0400
  * Cleanups in the two \*.yy grammar files
* [Revision #1c022aaf58](https://github.com/MariaDB/server/commit/1c022aaf58)\
  2019-10-28 21:28:21 +0200
  * [MDEV-20487](https://jira.mariadb.org/browse/MDEV-20487): Fix a test
* [Revision #613e9e7d4d](https://github.com/MariaDB/server/commit/613e9e7d4d)\
  2019-10-28 17:11:10 +0200
  * [MDEV-20907](https://jira.mariadb.org/browse/MDEV-20907) Set innodb\_log\_files\_in\_group=1 by default
* Merge [Revision #3043f38436](https://github.com/MariaDB/server/commit/3043f38436) 2019-10-28 17:10:34 +0200 - Merge 10.4 into 10.5
* [Revision #658289ca53](https://github.com/MariaDB/server/commit/658289ca53)\
  2019-10-28 16:22:48 +0200
  * [MDEV-20844](https://jira.mariadb.org/browse/MDEV-20844): Add missing override qualifiers
* [Revision #adae286e35](https://github.com/MariaDB/server/commit/adae286e35)\
  2019-10-28 16:21:42 +0200
  * Amend 3ea51b518bf8c2ec55e125794a14fb152079839c
* [Revision #8ba5af7eaf](https://github.com/MariaDB/server/commit/8ba5af7eaf)\
  2019-10-24 14:00:48 +0400
  * [MDEV-20890](https://jira.mariadb.org/browse/MDEV-20890) Illegal mix of collations with UUID()
* [Revision #88cdfc5c7d](https://github.com/MariaDB/server/commit/88cdfc5c7d)\
  2019-10-23 17:43:31 +0300
  * [MDEV-20487](https://jira.mariadb.org/browse/MDEV-20487) Set innodb\_adaptive\_hash\_index=OFF by default
* [Revision #18a44b4b4b](https://github.com/MariaDB/server/commit/18a44b4b4b)\
  2019-10-20 12:16:52 +0300
  * Don't crash in S3 if Aria is not initialzed
* [Revision #017150b747](https://github.com/MariaDB/server/commit/017150b747)\
  2019-10-20 12:16:09 +0300
  * Fixed compilation issue
* [Revision #ec171a94a3](https://github.com/MariaDB/server/commit/ec171a94a3)\
  2019-10-18 13:09:37 +0400
  * [MDEV-20844](https://jira.mariadb.org/browse/MDEV-20844) RBR from binary(16) to inet6 fails with error 171: The event was corrupt, leading to illegal data being read
* [Revision #9a833dc688](https://github.com/MariaDB/server/commit/9a833dc688)\
  2019-10-18 08:07:40 +0400
  * [MDEV-20856](https://jira.mariadb.org/browse/MDEV-20856) Bad values in metadata views for partitions on VARBINARY
* [Revision #9c96061525](https://github.com/MariaDB/server/commit/9c96061525)\
  2019-10-16 16:22:04 +0400
  * Part2: [MDEV-20837](https://jira.mariadb.org/browse/MDEV-20837) Add MariaDB\_FUNCTION\_PLUGIN
* [Revision #5a052ab6b1](https://github.com/MariaDB/server/commit/5a052ab6b1)\
  2019-10-16 12:43:24 +0400
  * Part1: [MDEV-20837](https://jira.mariadb.org/browse/MDEV-20837) Add MariaDB\_FUNCTION\_PLUGIN
* [Revision #22b645ef52](https://github.com/MariaDB/server/commit/22b645ef52)\
  2019-10-15 13:50:41 +0400
  * [MDEV-20831](https://jira.mariadb.org/browse/MDEV-20831) Table partitioned by LIST/RANGE COLUMNS(inet6) can be created, but not inserted into
* [Revision #8ec978142b](https://github.com/MariaDB/server/commit/8ec978142b)\
  2019-10-14 14:44:25 +0400
  * [MDEV-20822](https://jira.mariadb.org/browse/MDEV-20822) INET6 crashes in combination with RBR extended metadata
* [Revision #a11694b80d](https://github.com/MariaDB/server/commit/a11694b80d)\
  2019-10-14 18:26:25 +0400
  * [MDEV-20826](https://jira.mariadb.org/browse/MDEV-20826) Wrong result of MIN(inet6) with GROUP BY
* [Revision #ba8e5e689c](https://github.com/MariaDB/server/commit/ba8e5e689c)\
  2019-10-14 14:24:22 +0400
  * [MDEV-16620](https://jira.mariadb.org/browse/MDEV-16620) JSON\_ARRAYAGG and JSON\_OBJECTAGG.
* [Revision #b1c2c4ee1b](https://github.com/MariaDB/server/commit/b1c2c4ee1b)\
  2019-10-11 14:39:05 +0200
  * [MDEV-10014](https://jira.mariadb.org/browse/MDEV-10014) Add RETURNING to INSERT
* [Revision #904dc93439](https://github.com/MariaDB/server/commit/904dc93439)\
  2019-10-08 14:54:52 +0200
  * bugfix: PS and dependent subqueries
* [Revision #837ad9ab97](https://github.com/MariaDB/server/commit/837ad9ab97)\
  2019-06-02 00:51:46 +0530
  * [MDEV-10014](https://jira.mariadb.org/browse/MDEV-10014) Add RETURNING to INSERT
* [Revision #57a09a72a3](https://github.com/MariaDB/server/commit/57a09a72a3)\
  2019-10-07 20:25:55 +0200
  * cleanup st\_select\_lex\_unit::explainable
* [Revision #721a9df751](https://github.com/MariaDB/server/commit/721a9df751)\
  2019-10-07 22:17:05 +0200
  * cleanup: formatting
* [Revision #828d9ae597](https://github.com/MariaDB/server/commit/828d9ae597)\
  2019-10-01 11:36:18 +0200
  * cleanup: reduce code duplication
* [Revision #a4a025f5d1](https://github.com/MariaDB/server/commit/a4a025f5d1)\
  2019-09-22 23:23:28 +0200
  * cleanup: don't pass wild\_num to setup\_wild()
* [Revision #c7320830a6](https://github.com/MariaDB/server/commit/c7320830a6)\
  2019-09-24 19:47:45 +0200
  * outer references in subqueries in INSERT
* [Revision #173ae63114](https://github.com/MariaDB/server/commit/173ae63114)\
  2019-09-29 22:07:48 +0200
  * [MDEV-12684](https://jira.mariadb.org/browse/MDEV-12684) Show what config file a sysvar got a value from
* [Revision #f217612fad](https://github.com/MariaDB/server/commit/f217612fad)\
  2019-09-29 16:30:57 +0200
  * [MDEV-12684](https://jira.mariadb.org/browse/MDEV-12684) Show what config file a sysvar got a value from
* [Revision #927521a2c1](https://github.com/MariaDB/server/commit/927521a2c1)\
  2019-09-29 14:48:11 +0200
  * [MDEV-12684](https://jira.mariadb.org/browse/MDEV-12684) Show what config file a sysvar got a value from
* [Revision #f7b8d14490](https://github.com/MariaDB/server/commit/f7b8d14490)\
  2019-10-13 00:19:54 +0200
  * cleanup: don't use my\_getopt\_is\_args\_separator()
* [Revision #3e56972712](https://github.com/MariaDB/server/commit/3e56972712)\
  2019-10-12 21:21:50 +0200
  * cleanup: unify --defaults\* option handling
* [Revision #3ea51b518b](https://github.com/MariaDB/server/commit/3ea51b518b)\
  2019-09-29 20:30:28 +0200
  * cleanup: my\_getopt, get\_one\_option isn't optional
* [Revision #eb3431d529](https://github.com/MariaDB/server/commit/eb3431d529)\
  2019-09-29 14:38:53 +0200
  * cleanup: my\_getopt, consistency
* [Revision #8965ae27b9](https://github.com/MariaDB/server/commit/8965ae27b9)\
  2019-09-28 20:05:11 +0200
  * cleanup: my\_defaults, remove Process\_option\_func
* [Revision #5392726e3c](https://github.com/MariaDB/server/commit/5392726e3c)\
  2019-10-14 08:21:08 +0400
  * [MDEV-20818](https://jira.mariadb.org/browse/MDEV-20818) ER\_CRASHED\_ON\_USAGE or Assertion \`length <= column->length' failed in write\_block\_record on temporary table
* [Revision #fa8437908b](https://github.com/MariaDB/server/commit/fa8437908b)\
  2019-10-13 23:14:36 +0400
  * clang failed to compile the embedded library with unused constant errors
* [Revision #9853026cec](https://github.com/MariaDB/server/commit/9853026cec)\
  2019-10-13 23:07:48 +0400
  * [MDEV-20800](https://jira.mariadb.org/browse/MDEV-20800) Server crashes in Field\_inet6::store\_warning upon updating table statistics
* [Revision #2cb7047f69](https://github.com/MariaDB/server/commit/2cb7047f69)\
  2019-10-13 22:00:30 +0400
  * Removing redundant `--source include/have_innodb.inc` from type\_inet6\_{memory|myisam}.test
* [Revision #93cf67fda8](https://github.com/MariaDB/server/commit/93cf67fda8)\
  2019-10-13 18:32:48 +0400
  * Adding the "override" keyword to Item\_char\_typecast\_func\_handler\_inet6\_to\_binary::type\_handler\_for\_create\_select()
* [Revision #ebeb4f93e8](https://github.com/MariaDB/server/commit/ebeb4f93e8)\
  2019-10-11 13:08:53 +0200
  * [MDEV-16327](https://jira.mariadb.org/browse/MDEV-16327): Server doesn't account for engines that supports OFFSET on their own.
* [Revision #a6de640804](https://github.com/MariaDB/server/commit/a6de640804)\
  2019-09-30 17:20:28 +0200
  * [MDEV-18553](https://jira.mariadb.org/browse/MDEV-18553): [MDEV-16327](https://jira.mariadb.org/browse/MDEV-16327) pre-requisits part 3: move kill check in one place
* [Revision #1ae02f0e0d](https://github.com/MariaDB/server/commit/1ae02f0e0d)\
  2019-10-11 12:26:15 +0200
  * [MDEV-18553](https://jira.mariadb.org/browse/MDEV-18553): [MDEV-16327](https://jira.mariadb.org/browse/MDEV-16327) pre-requisits part 2: uniform of LIMIT/OFFSET handling
* [Revision #eb0804ef5e](https://github.com/MariaDB/server/commit/eb0804ef5e)\
  2019-09-26 09:49:50 +0200
  * [MDEV-18553](https://jira.mariadb.org/browse/MDEV-18553): [MDEV-16327](https://jira.mariadb.org/browse/MDEV-16327) pre-requisits part 1: isolation of LIMIT/OFFSET handling
* Merge [Revision #8336371441](https://github.com/MariaDB/server/commit/8336371441) 2019-10-12 22:06:47 +0300 - Merge 10.4 into 10.5
* [Revision #6860d6f8be](https://github.com/MariaDB/server/commit/6860d6f8be)\
  2019-10-12 15:28:40 +0400
  * Fixing a mysqld crash on Ubuntu-10.2 (Quantal)
* [Revision #530f3f7cfc](https://github.com/MariaDB/server/commit/530f3f7cfc)\
  2019-10-11 23:16:01 +0400
  * [MDEV-20806](https://jira.mariadb.org/browse/MDEV-20806) Federated does not work with INET6, returns NULL with warning ER\_TRUNCATED\_WRONG\_VALUE
* [Revision #a0d3a351b8](https://github.com/MariaDB/server/commit/a0d3a351b8)\
  2019-10-11 22:51:01 +0400
  * [MDEV-20790](https://jira.mariadb.org/browse/MDEV-20790) CSV table with INET6 can be created and inserted into, but cannot be read from
* [Revision #5d6d28f274](https://github.com/MariaDB/server/commit/5d6d28f274)\
  2019-10-11 22:19:30 +0400
  * [MDEV-20798](https://jira.mariadb.org/browse/MDEV-20798) Conversion from INET6 to other types performed without errors or warnings
* [Revision #d8e599bb80](https://github.com/MariaDB/server/commit/d8e599bb80)\
  2019-10-11 20:11:42 +0400
  * [MDEV-20808](https://jira.mariadb.org/browse/MDEV-20808) CAST from INET6 to FLOAT does not produce an error
* [Revision #b42294bc64](https://github.com/MariaDB/server/commit/b42294bc64)\
  2019-10-11 17:28:15 +0300
  * [MDEV-19514](https://jira.mariadb.org/browse/MDEV-19514) Defer change buffer merge until pages are requested
* [Revision #b5fae7f743](https://github.com/MariaDB/server/commit/b5fae7f743)\
  2019-10-11 14:50:11 +0400
  * [MDEV-20795](https://jira.mariadb.org/browse/MDEV-20795) CAST(inet6 AS BINARY) returns wrong result
* Merge [Revision #d04f2de80a](https://github.com/MariaDB/server/commit/d04f2de80a) 2019-10-11 08:41:36 +0300 - Merge 10.4 into 10.5
* [Revision #5e17b1f7cb](https://github.com/MariaDB/server/commit/5e17b1f7cb)\
  2019-10-10 22:19:53 +0400
  * A small cleanup for [MDEV-16309](https://jira.mariadb.org/browse/MDEV-16309) Split ::create\_tmp\_field() into virtual methods in Item
* Merge [Revision #f5833a4e45](https://github.com/MariaDB/server/commit/f5833a4e45) 2019-10-10 15:26:38 +0400 - Merge branch '10.5' into bb-10.5-hf
* [Revision #dba7ae5fdb](https://github.com/MariaDB/server/commit/dba7ae5fdb)\
  2019-10-10 12:08:28 +0300
  * [MDEV-274](https://jira.mariadb.org/browse/MDEV-274): Fix unresolved link-time references
* Merge [Revision #241b4a303d](https://github.com/MariaDB/server/commit/241b4a303d) 2019-10-10 08:58:54 +0400 - Merge branch '10.5' into bb-10.5-hf
* [Revision #312ba3cc3d](https://github.com/MariaDB/server/commit/312ba3cc3d)\
  2019-10-10 08:12:14 +0400
  * [MDEV-20783](https://jira.mariadb.org/browse/MDEV-20783) INET6 cannot be converted to BINARY(16)
* Merge [Revision #7dc74bb3b5](https://github.com/MariaDB/server/commit/7dc74bb3b5) 2019-10-10 00:31:59 +0400 - Merge branch '[MDEV-16620](https://jira.mariadb.org/browse/MDEV-16620)' of [server](https://github.com/markus456/server) into bb-10.5-hf
* [Revision #d0fc07c85f](https://github.com/MariaDB/server/commit/d0fc07c85f)\
  2019-07-04 13:12:08 +0300
  * [MDEV-16620](https://jira.mariadb.org/browse/MDEV-16620): Add JSON\_ARRAYAGG function
* [Revision #b37386d854](https://github.com/MariaDB/server/commit/b37386d854)\
  2019-10-09 22:25:58 +0400
  * [MDEV-20785](https://jira.mariadb.org/browse/MDEV-20785) Converting INET6 to CHAR(39) produces garbage without a warning
* [Revision #c78ae293b4](https://github.com/MariaDB/server/commit/c78ae293b4)\
  2019-10-09 13:39:27 +0400
  * Adding missing "override" keywords, to make clang happy.
* [Revision #6ea5c2b5b6](https://github.com/MariaDB/server/commit/6ea5c2b5b6)\
  2019-10-08 08:05:21 +0400
  * [MDEV-274](https://jira.mariadb.org/browse/MDEV-274) The data type for IPv6/IPv4 addresses in MariaDB
* [Revision #89bd5623b0](https://github.com/MariaDB/server/commit/89bd5623b0)\
  2019-10-08 17:00:54 +0530
  * [MDEV-20582](https://jira.mariadb.org/browse/MDEV-20582) Asan failure in table\_def::calc\_field\_size
* [Revision #fc33c3cda5](https://github.com/MariaDB/server/commit/fc33c3cda5)\
  2019-10-08 16:54:48 +0530
  * [MDEV-20591](https://jira.mariadb.org/browse/MDEV-20591) Wrong Number of rows in mysqlbinlog output
* [Revision #a07be05302](https://github.com/MariaDB/server/commit/a07be05302)\
  2019-10-08 08:29:09 +0400
  * Fixing --ps test failures in "[MDEV-20016](https://jira.mariadb.org/browse/MDEV-20016) Add MariaDB\_DATA\_TYPE\_PLUGIN"
* [Revision #6afb2a37fd](https://github.com/MariaDB/server/commit/6afb2a37fd)\
  2019-10-07 21:37:06 +0400
  * [MDEV-20768](https://jira.mariadb.org/browse/MDEV-20768) Turn INET functions into a function collection plugin
* [Revision #e0117f1120](https://github.com/MariaDB/server/commit/e0117f1120)\
  2019-10-07 19:23:09 +0400
  * A cleanup for: [MDEV-18010](https://jira.mariadb.org/browse/MDEV-18010) Add classes Inet4 and Inet6
* [Revision #cbf6beba40](https://github.com/MariaDB/server/commit/cbf6beba40)\
  2019-10-07 10:46:25 +0400
  * [MDEV-20764](https://jira.mariadb.org/browse/MDEV-20764) Add MariaDB\_FUNCTION\_COLLECTION\_PLUGIN
* [Revision #3616175fdd](https://github.com/MariaDB/server/commit/3616175fdd)\
  2019-10-05 18:16:37 +0400
  * [MDEV-20760](https://jira.mariadb.org/browse/MDEV-20760) Add Type\_handler::KEY\_pack\_flags()
* [Revision #c717483c9d](https://github.com/MariaDB/server/commit/c717483c9d)\
  2019-10-04 18:33:09 +0400
  * [MDEV-20016](https://jira.mariadb.org/browse/MDEV-20016) Add MariaDB\_DATA\_TYPE\_PLUGIN
* Merge [Revision #627027a674](https://github.com/MariaDB/server/commit/627027a674) 2019-10-04 10:56:47 +0300 - Merge 10.4 into 10.5
* [Revision #1950e32464](https://github.com/MariaDB/server/commit/1950e32464)\
  2019-10-04 10:39:24 +0300
  * [MDEV-20706](https://jira.mariadb.org/browse/MDEV-20706): Add missing override qualifiers
* [Revision #57ce0bab32](https://github.com/MariaDB/server/commit/57ce0bab32)\
  2019-10-04 10:12:27 +0400
  * A cleanup for [MDEV-19908](https://jira.mariadb.org/browse/MDEV-19908) Add class Type\_collection
* [Revision #c2d8db66be](https://github.com/MariaDB/server/commit/c2d8db66be)\
  2019-10-03 16:03:32 +0400
  * [MDEV-20735](https://jira.mariadb.org/browse/MDEV-20735) Allow non-reserved keywords as user defined type names
* [Revision #d168601e83](https://github.com/MariaDB/server/commit/d168601e83)\
  2019-10-03 14:02:00 +0400
  * [MDEV-20734](https://jira.mariadb.org/browse/MDEV-20734) Allow reserved keywords as user defined type names
* [Revision #54606df1a3](https://github.com/MariaDB/server/commit/54606df1a3)\
  2019-10-03 10:26:46 +0400
  * A cleanup for [MDEV-19908](https://jira.mariadb.org/browse/MDEV-19908) Add class Type\_collection
* [Revision #cefe5bb6b3](https://github.com/MariaDB/server/commit/cefe5bb6b3)\
  2019-10-02 18:10:58 +0400
  * A cleanup for [MDEV-20042](https://jira.mariadb.org/browse/MDEV-20042) Implement EXTRA2\_FIELD\_DATA\_TYPE\_INFO in FRM
* [Revision #5e356ce707](https://github.com/MariaDB/server/commit/5e356ce707)\
  2019-10-02 11:11:12 +0400
  * [MDEV-20721](https://jira.mariadb.org/browse/MDEV-20721) Implement sql\_type() for Field\_real and Field\_int
* [Revision #9c031fc218](https://github.com/MariaDB/server/commit/9c031fc218)\
  2019-10-01 23:41:03 +0400
  * [MDEV-20716](https://jira.mariadb.org/browse/MDEV-20716) Unify make\_table\_field() and make\_table\_field\_from\_def() for integer and real types
* [Revision #4b5a76741e](https://github.com/MariaDB/server/commit/4b5a76741e)\
  2019-10-01 22:30:28 +0400
  * [MDEV-20712](https://jira.mariadb.org/browse/MDEV-20712) Wrong data type for CAST(@a AS BINARY) for a numeric variable
* [Revision #c06397f615](https://github.com/MariaDB/server/commit/c06397f615)\
  2019-10-01 17:10:41 +0400
  * Fixing a Windows compilation failure introduced by [MDEV-20706](https://jira.mariadb.org/browse/MDEV-20706)
* [Revision #7474deec49](https://github.com/MariaDB/server/commit/7474deec49)\
  2019-10-01 17:04:22 +0400
  * [MDEV-20708](https://jira.mariadb.org/browse/MDEV-20708) Change make\_table\_field() to get TABLE\_SHARE rather than TABLE
* [Revision #02dea3ffd5](https://github.com/MariaDB/server/commit/02dea3ffd5)\
  2019-10-01 13:12:46 +0400
  * [MDEV-20706](https://jira.mariadb.org/browse/MDEV-20706) Store scale in Column\_definition::decimals rather than Column\_definition::pack\_flag
* Merge [Revision #1ae09ec863](https://github.com/MariaDB/server/commit/1ae09ec863) 2019-10-01 10:50:32 +0400 - Merge remote-tracking branch 'origin/10.4' into 10.5
* [Revision #4cd79588de](https://github.com/MariaDB/server/commit/4cd79588de)\
  2019-09-30 15:23:04 +0300
  * SQL: override qualifier for Type\_handler\_int\_result
* [Revision #19b5b17773](https://github.com/MariaDB/server/commit/19b5b17773)\
  2018-09-18 14:20:09 +0300
  * SQL: followup misc rename on versioning
* [Revision #58fdf5b2fa](https://github.com/MariaDB/server/commit/58fdf5b2fa)\
  2018-08-28 19:45:34 +0300
  * [MDEV-16144](https://jira.mariadb.org/browse/MDEV-16144) Default TIMESTAMP clause for SELECT from versioned
* [Revision #f610529d23](https://github.com/MariaDB/server/commit/f610529d23)\
  2019-09-29 22:10:42 +0400
  * [MDEV-20696](https://jira.mariadb.org/browse/MDEV-20696) Remove Column\_definition::key\_length
* [Revision #cd41ffe1f1](https://github.com/MariaDB/server/commit/cd41ffe1f1)\
  2019-09-18 14:17:26 +0200
  * [MDEV-19713](https://jira.mariadb.org/browse/MDEV-19713) Remove big\_tables system variable
* [Revision #de9ef03ae6](https://github.com/MariaDB/server/commit/de9ef03ae6)\
  2019-09-18 14:18:08 +0200
  * fix max\_rows calculations for internal on-disk temp tables
* [Revision #fab84ec979](https://github.com/MariaDB/server/commit/fab84ec979)\
  2019-09-18 11:03:33 +0200
  * removes references to a sysvar that disappeared 6 years ago
* [Revision #32efbaa19a](https://github.com/MariaDB/server/commit/32efbaa19a)\
  2019-09-17 20:11:04 +0200
  * [MDEV-7481](https://jira.mariadb.org/browse/MDEV-7481) Replace max\_long\_data\_size functionality with max\_allowed\_packet
* Merge [Revision #12414cd9f2](https://github.com/MariaDB/server/commit/12414cd9f2) 2019-09-27 19:12:07 +0300 - Merge 10.4 into 10.5
* Merge [Revision #72f671ab7b](https://github.com/MariaDB/server/commit/72f671ab7b) 2019-09-27 07:15:07 +0300 - Merge 10.4 into 10.5
* [Revision #08de2540ac](https://github.com/MariaDB/server/commit/08de2540ac)\
  2019-09-26 11:06:54 +0400
  * [MDEV-20674](https://jira.mariadb.org/browse/MDEV-20674) Reuse val\_native() in ExtractValue() and UpdateXML()
* [Revision #a340af9223](https://github.com/MariaDB/server/commit/a340af9223)\
  2019-09-25 16:08:48 +0300
  * btr\_block\_get(): Remove redundant parameters
* [Revision #5d0bab47fc](https://github.com/MariaDB/server/commit/5d0bab47fc)\
  2019-09-24 15:09:15 +0300
  * btr\_block\_get(), btr\_block\_get\_func(): Change the parameter to const dict\_index\_t&
* Merge [Revision #fba9883bc4](https://github.com/MariaDB/server/commit/fba9883bc4) 2019-09-25 10:18:22 +0300 - Merge 10.4 into 10.5
* [Revision #8e92d5e5e3](https://github.com/MariaDB/server/commit/8e92d5e5e3)\
  2019-09-22 01:17:30 +0530
  * [MDEV-20468](https://jira.mariadb.org/browse/MDEV-20468): Allocating more space than required for JOIN\_TAB array for a query with SJM table
* [Revision #f5c3ad1913](https://github.com/MariaDB/server/commit/f5c3ad1913)\
  2019-06-20 18:02:40 +0400
  * [MDEV-16470](https://jira.mariadb.org/browse/MDEV-16470) - Session user variables tracker
* [Revision #ad77e3ac09](https://github.com/MariaDB/server/commit/ad77e3ac09)\
  2019-09-20 22:52:00 +0400
  * Cleanup session tracker
* Merge [Revision #edef6a0074](https://github.com/MariaDB/server/commit/edef6a0074) 2019-09-24 12:41:38 +0400 - Merge remote-tracking branch 'origin/10.4' into 10.5
* Merge [Revision #1333da90b5](https://github.com/MariaDB/server/commit/1333da90b5) 2019-09-24 10:07:56 +0300 - Merge 10.4 into 10.5
* [Revision #8887effe13](https://github.com/MariaDB/server/commit/8887effe13)\
  2019-09-19 08:35:21 +0300
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) preparation: page\_mem\_alloc\_heap()
* [Revision #71e856e152](https://github.com/MariaDB/server/commit/71e856e152)\
  2019-09-18 10:53:31 +0300
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) preparation: Clean up page directory operations
* [Revision #2eeac53715](https://github.com/MariaDB/server/commit/2eeac53715)\
  2019-09-13 16:07:26 +0530
  * Fix compile error in macOS caused by [MDEV-20477](https://jira.mariadb.org/browse/MDEV-20477)
* [Revision #386f9d14bd](https://github.com/MariaDB/server/commit/386f9d14bd)\
  2019-09-13 16:01:44 +0530
  * Disable part of binlog\_table\_map\_optional\_metadata.test (because of [MDEV-20582](https://jira.mariadb.org/browse/MDEV-20582))
* Merge [Revision #46a6cea5c5](https://github.com/MariaDB/server/commit/46a6cea5c5) 2019-09-17 09:07:52 +0300 - Merge 10.4 into 10.5
* [Revision #74551b2b6f](https://github.com/MariaDB/server/commit/74551b2b6f)\
  2019-09-17 08:00:37 +0400
  * Cleanup: removing Type\_handler members m\_name\_xxx
* [Revision #9b1866fd84](https://github.com/MariaDB/server/commit/9b1866fd84)\
  2019-09-17 07:15:02 +0400
  * Cleanup: removing Type\_handler members m\_version\_xxx
* [Revision #c11e26946f](https://github.com/MariaDB/server/commit/c11e26946f)\
  2019-09-12 21:30:02 -0700
  * Fixed a typo in the patch for [MDEV-15777](https://jira.mariadb.org/browse/MDEV-15777)
* [Revision #61bbf39915](https://github.com/MariaDB/server/commit/61bbf39915)\
  2019-09-12 17:23:25 +0300
  * Fix GCC -Woverloaded-virtual
* Merge [Revision #d28686ada6](https://github.com/MariaDB/server/commit/d28686ada6) 2019-09-12 16:36:46 +0300 - Merge 10.4 into 10.5
* [Revision #9d26f3dabb](https://github.com/MariaDB/server/commit/9d26f3dabb)\
  2019-09-12 15:39:45 +0300
  * Add C++11 override qualifiers to Field member functions
* [Revision #0b578882e7](https://github.com/MariaDB/server/commit/0b578882e7)\
  2019-09-12 14:18:53 +0300
  * [MDEV-20477](https://jira.mariadb.org/browse/MDEV-20477): Add missing override
* [Revision #3f1b569a1d](https://github.com/MariaDB/server/commit/3f1b569a1d)\
  2019-09-10 13:58:58 +0200
  * [MDEV-19887](https://jira.mariadb.org/browse/MDEV-19887): Document --copy-s3-tables option on mysqldump man page
* [Revision #a43c367286](https://github.com/MariaDB/server/commit/a43c367286)\
  2019-09-12 14:32:17 +0530
  * Fix sysvars\_server\_embedded.test
* [Revision #a039b0888d](https://github.com/MariaDB/server/commit/a039b0888d)\
  2019-09-12 10:28:00 +0530
  * Fix sysvars\_server\_notembedded
* [Revision #fdd00665c2](https://github.com/MariaDB/server/commit/fdd00665c2)\
  2019-09-11 13:50:28 +0400
  * Revert "Part3: [MDEV-18156](https://jira.mariadb.org/browse/MDEV-18156) Assertion `0' failed or` btr\_validate\_index(index, 0, false)' in row\_upd\_sec\_index\_entry or error code 126: Index is corrupted upon DELETE with PAD\_CHAR\_TO\_FULL\_LENGTH"
* [Revision #967c14c04e](https://github.com/MariaDB/server/commit/967c14c04e)\
  2019-09-01 13:25:16 +0530
  * [MDEV-20477](https://jira.mariadb.org/browse/MDEV-20477) Merge binlog extended metadata support from the upstream
* Merge [Revision #0636645e7e](https://github.com/MariaDB/server/commit/0636645e7e) 2019-09-11 11:46:31 +0400 - Merge remote-tracking branch 'origin/10.4' into 10.5
* [Revision #2f99e1a2e9](https://github.com/MariaDB/server/commit/2f99e1a2e9)\
  2019-09-09 12:06:29 +0200
  * Fix connect RESTSDK support.
* [Revision #b09c588700](https://github.com/MariaDB/server/commit/b09c588700)\
  2019-09-08 14:20:06 +0200
  * [MDEV-20525](https://jira.mariadb.org/browse/MDEV-20525) rocksdb debug compilation fails on Windows due to unresolved my\_assert variable
* Merge [Revision #4081b7b27a](https://github.com/MariaDB/server/commit/4081b7b27a) 2019-09-06 17:16:40 +0300 - Merge 10.4 into 10.5
* Merge [Revision #780d2bb8a7](https://github.com/MariaDB/server/commit/780d2bb8a7) 2019-09-06 14:25:20 +0300 - Merge 10.4 into 10.5
* [Revision #db9e41ddc3](https://github.com/MariaDB/server/commit/db9e41ddc3)\
  2019-09-06 07:19:14 +0400
  * [MDEV-20496](https://jira.mariadb.org/browse/MDEV-20496) Assertion \`field.is\_sane()' failed in Protocol\_text::store\_field\_metadata
* [Revision #18e10e89bb](https://github.com/MariaDB/server/commit/18e10e89bb)\
  2019-08-26 22:32:58 +0200
  * Update server.cnf section to mariadb-10.5
* Merge [Revision #45a4dbdca4](https://github.com/MariaDB/server/commit/45a4dbdca4) 2019-08-31 23:39:12 -0700 - Merge remote-tracking branch 'origin/bb-[MDEV-18844](https://jira.mariadb.org/browse/MDEV-18844)' into 10.5
* [Revision #c9fe6fbb61](https://github.com/MariaDB/server/commit/c9fe6fbb61)\
  2019-08-31 22:44:58 -0700
  * Merge branch '[MDEV-18844](https://jira.mariadb.org/browse/MDEV-18844)' of [server](https://github.com/waynexia/server) into [MDEV-18844](https://jira.mariadb.org/browse/MDEV-18844)
* [Revision #2707af2dec](https://github.com/MariaDB/server/commit/2707af2dec)\
  2019-08-30 14:47:12 +0800
  * (1)mod: counter type from longlong to ha\_rows (2)fix: bug when call create tmp table
* [Revision #95f35bb75d](https://github.com/MariaDB/server/commit/95f35bb75d)\
  2019-08-28 12:04:02 +0800
  * (1) fix type error (2) remove empty "--error ER\_PARSE\_ERROR" (3) change three members in class select\_unit to protected.
* [Revision #a896bebfa6](https://github.com/MariaDB/server/commit/a896bebfa6)\
  2019-08-24 21:42:35 +0800
  * [MDEV-18844](https://jira.mariadb.org/browse/MDEV-18844) Implement EXCEPT ALL and INTERSECT ALL operations
* [Revision #9380850d87](https://github.com/MariaDB/server/commit/9380850d87)\
  2019-08-30 18:47:14 -0700
  * [MDEV-15777](https://jira.mariadb.org/browse/MDEV-15777) Use inferred IS NOT NULL predicates in the range optimizer
* [Revision #fac81c6752](https://github.com/MariaDB/server/commit/fac81c6752)\
  2019-08-29 12:49:56 +0300
  * Updated libmarias3 to latest version
* [Revision #41fa564c88](https://github.com/MariaDB/server/commit/41fa564c88)\
  2019-08-28 07:19:24 +0100
  * [MDEV-17048](https://jira.mariadb.org/browse/MDEV-17048) Inconsistency voting support (#1373)
* [Revision #53ee9c6cf9](https://github.com/MariaDB/server/commit/53ee9c6cf9)\
  2019-08-26 00:00:42 +0200
  * compilation failure Win32
* [Revision #85bef794f7](https://github.com/MariaDB/server/commit/85bef794f7)\
  2019-08-16 11:35:06 +0200
  * [MDEV-19780](https://jira.mariadb.org/browse/MDEV-19780) Remove the TokuDB storage engine
* [Revision #5931a45890](https://github.com/MariaDB/server/commit/5931a45890)\
  2019-08-24 16:18:48 +0200
  * compilation fix for cmake 2.18
* [Revision #2bacce8bc8](https://github.com/MariaDB/server/commit/2bacce8bc8)\
  2019-08-18 12:43:41 +0300
  * Updated result for rocksdb tests after merge
* [Revision #1fbaf8b6a8](https://github.com/MariaDB/server/commit/1fbaf8b6a8)\
  2019-08-17 17:05:46 +0300
  * Decrease stack space usage of mysql\_execute\_command()
* [Revision #e21408b799](https://github.com/MariaDB/server/commit/e21408b799)\
  2019-08-23 16:44:51 +0200
  * Decrease stack space usage of mysql\_execute\_command()
* [Revision #f8018a356e](https://github.com/MariaDB/server/commit/f8018a356e)\
  2019-08-23 14:43:32 +0200
  * hide have\_sanitizer variable in non-ASAN builds
* [Revision #d90fa9ad28](https://github.com/MariaDB/server/commit/d90fa9ad28)\
  2019-08-15 23:42:07 +0300
  * Added asan options to mysql-test-run
* [Revision #97dd057702](https://github.com/MariaDB/server/commit/97dd057702)\
  2019-08-12 15:47:24 +0300
  * Fixed issues when running mtr with --valgrind
* [Revision #b444b6b910](https://github.com/MariaDB/server/commit/b444b6b910)\
  2019-08-08 22:53:33 +0300
  * Removed some warnings from InnoDB when compiled with clang
* [Revision #a38f47e90c](https://github.com/MariaDB/server/commit/a38f47e90c)\
  2019-08-08 22:52:22 +0300
  * Fixed compiler warnings from connect engine
* [Revision #de8b51fdc9](https://github.com/MariaDB/server/commit/de8b51fdc9)\
  2019-08-08 22:45:55 +0300
  * Fixed some test that failed randomly
* [Revision #76ce6ae4bb](https://github.com/MariaDB/server/commit/76ce6ae4bb)\
  2019-08-08 22:44:34 +0300
  * Removed some compiler warnings found by clang
* [Revision #4a75b480e9](https://github.com/MariaDB/server/commit/4a75b480e9)\
  2019-08-14 00:14:27 +0300
  * Fixed BUILD scripts for gcc 6.x
* [Revision #e6bad1c75d](https://github.com/MariaDB/server/commit/e6bad1c75d)\
  2019-08-23 13:58:11 +0200
  * move Aria/S3 specific flag into Aria code
* [Revision #1b5e5bdef3](https://github.com/MariaDB/server/commit/1b5e5bdef3)\
  2019-08-14 00:18:58 +0300
  * [MDEV-20306](https://jira.mariadb.org/browse/MDEV-20306) Assert when converting encrypted Aria table to S3
* [Revision #bb6d674df9](https://github.com/MariaDB/server/commit/bb6d674df9)\
  2019-08-08 20:13:10 +0300
  * Fixed assertion Assertion \`!table->pos\_in\_locked\_tables' failed
* [Revision #2e665fb294](https://github.com/MariaDB/server/commit/2e665fb294)\
  2019-08-22 20:24:15 +0200
  * alloc\_on\_stack: simplify the API
* [Revision #6c50875a38](https://github.com/MariaDB/server/commit/6c50875a38)\
  2019-08-08 23:04:05 +0300
  * [MDEV-20279](https://jira.mariadb.org/browse/MDEV-20279) Increase Aria index length limit
* [Revision #afe969ba05](https://github.com/MariaDB/server/commit/afe969ba05)\
  2019-08-06 14:04:38 +0400
  * Removed redundant log\_type == LOG\_BIN checks
* [Revision #6b0b25a25b](https://github.com/MariaDB/server/commit/6b0b25a25b)\
  2019-08-06 13:29:57 +0400
  * Cleanup log\_type\_arg of MYSQL\_BIN\_LOG::open()
* [Revision #e976d95614](https://github.com/MariaDB/server/commit/e976d95614)\
  2019-08-06 13:04:18 +0400
  * Cleanup MYSQL\_LOG
* [Revision #1d58e62d5b](https://github.com/MariaDB/server/commit/1d58e62d5b)\
  2019-08-19 20:57:59 +0400
  * [MDEV-20384](https://jira.mariadb.org/browse/MDEV-20384) Assertion \`field.is\_sane()' failed in Protocol\_text::store\_field\_metadata
* [Revision #da53fb6d7d](https://github.com/MariaDB/server/commit/da53fb6d7d)\
  2019-08-17 16:18:56 +0300
  * Updated spider result file
* [Revision #cb4dcf39e7](https://github.com/MariaDB/server/commit/cb4dcf39e7)\
  2019-08-16 22:49:56 +0400
  * [MDEV-20363](https://jira.mariadb.org/browse/MDEV-20363) Assertion \`is\_unsigned() == attr.unsigned\_flag' failed in Type\_handler\_longlong::make\_table\_field
* Merge [Revision #67ddb6507d](https://github.com/MariaDB/server/commit/67ddb6507d) 2019-08-16 14:35:32 +0300 - Merge 10.4 into 10.5
* [Revision #6073049a36](https://github.com/MariaDB/server/commit/6073049a36)\
  2019-08-15 13:16:00 +0400
  * [MDEV-20353](https://jira.mariadb.org/browse/MDEV-20353) Add separate type handlers for unsigned integer data types
* [Revision #ae4b9b7689](https://github.com/MariaDB/server/commit/ae4b9b7689)\
  2019-08-15 11:34:44 +0300
  * Fixed crash introduced with change to memcpy\_field\_possible
* [Revision #c9c689e1a3](https://github.com/MariaDB/server/commit/c9c689e1a3)\
  2019-08-14 23:47:31 +0300
  * Updated prototype of ha\_s3::write\_row() to get s3 to compile
* [Revision #fa490e8022](https://github.com/MariaDB/server/commit/fa490e8022)\
  2019-08-14 23:46:47 +0300
  * Don't copy uninitialized bytes when copying varstrings
* [Revision #afe6eb499d](https://github.com/MariaDB/server/commit/afe6eb499d)\
  2019-08-14 20:27:00 +0400
  * Revert "[MDEV-20342](https://jira.mariadb.org/browse/MDEV-20342) Turn Field::flags from a member to a method"
* [Revision #e86010f909](https://github.com/MariaDB/server/commit/e86010f909)\
  2019-08-14 10:26:18 +0400
  * [MDEV-20342](https://jira.mariadb.org/browse/MDEV-20342) Turn Field::flags from a member to a method
* Merge [Revision #fa21952e25](https://github.com/MariaDB/server/commit/fa21952e25) 2019-08-14 12:01:04 +0300 - Merge 10.4 into 10.5
* Merge [Revision #1c83c30064](https://github.com/MariaDB/server/commit/1c83c30064) 2019-08-14 10:33:17 +0300 - Merge 10.4 into 10.5
* [Revision #34b937835e](https://github.com/MariaDB/server/commit/34b937835e)\
  2019-08-14 09:32:37 +0300
  * Re-record innodb.innodb-system-table-view
* Merge [Revision #c1599821a5](https://github.com/MariaDB/server/commit/c1599821a5) 2019-08-13 23:49:10 +0400 - Merge remote-tracking branch 'origin/10.4' into 10.5
* Merge [Revision #624dd71b94](https://github.com/MariaDB/server/commit/624dd71b94) 2019-08-13 18:57:00 +0300 - Merge 10.4 into 10.5
* [Revision #d4d865fcc8](https://github.com/MariaDB/server/commit/d4d865fcc8)\
  2019-08-12 23:11:36 +0400
  * [MDEV-20332](https://jira.mariadb.org/browse/MDEV-20332) Wrong UNSIGNED metadata flag returned for COALESCE(unsigned\_field,timestamp\_field)
* [Revision #0e0d57141e](https://github.com/MariaDB/server/commit/0e0d57141e)\
  2019-08-12 21:46:20 +0400
  * [MDEV-20331](https://jira.mariadb.org/browse/MDEV-20331) Add class Type\_numeric\_attributes
* [Revision #e7525beac8](https://github.com/MariaDB/server/commit/e7525beac8)\
  2019-08-12 18:41:02 +0400
  * [MDEV-20326](https://jira.mariadb.org/browse/MDEV-20326) Add class DTCollation\_numeric
* [Revision #f6e386f00b](https://github.com/MariaDB/server/commit/f6e386f00b)\
  2019-08-11 21:55:39 +0300
  * Myrocks: Get the upstream's valgrind suppressions to work
* [Revision #d2a04ae55d](https://github.com/MariaDB/server/commit/d2a04ae55d)\
  2019-08-11 13:17:30 +0300
  * [MDEV-20315](https://jira.mariadb.org/browse/MDEV-20315): MyRocks tests produce valgrind failures
* [Revision #d5f5cd2831](https://github.com/MariaDB/server/commit/d5f5cd2831)\
  2019-08-09 23:17:01 +0400
  * A cleanup: removing duplicate code: Item\_func::val\_decimal()
* [Revision #3e27677b59](https://github.com/MariaDB/server/commit/3e27677b59)\
  2019-08-08 17:31:42 +0400
  * Cleanup: moving the definition of Lex\_cstring from vers\_string.h to lex\_string.h
* [Revision #e98f3bcf53](https://github.com/MariaDB/server/commit/e98f3bcf53)\
  2019-08-08 15:44:31 +0400
  * Adding the `override` keyword into all classes in the Type\_handler hierarchy, for consistency.
* [Revision #3f7659b838](https://github.com/MariaDB/server/commit/3f7659b838)\
  2019-08-08 14:55:39 +0400
  * Fixing -Winconsistent-missing-override with CLANG
* [Revision #e81db2baed](https://github.com/MariaDB/server/commit/e81db2baed)\
  2019-07-09 21:20:00 +1000
  * Add const qualifiers to Field::cmp, Field::cmp\_max and Field::cmp\_binary
* [Revision #46553c2508](https://github.com/MariaDB/server/commit/46553c2508)\
  2019-05-31 04:18:24 +0200
  * Fix compiler warnings GCC8
* [Revision #0d5d8d2e7a](https://github.com/MariaDB/server/commit/0d5d8d2e7a)\
  2019-07-04 12:59:18 +0300
  * Always print slave host in SHOW SLAVE HOSTS
* [Revision #1e9aa46dc3](https://github.com/MariaDB/server/commit/1e9aa46dc3)\
  2019-07-22 15:51:39 +0200
  * [MDEV-6521](https://jira.mariadb.org/browse/MDEV-6521): 10.5 Server HELP
* [Revision #ddce859076](https://github.com/MariaDB/server/commit/ddce859076)\
  2019-07-25 22:52:45 +0900
  * [MDEV-18737](https://jira.mariadb.org/browse/MDEV-18737) Spider "Out of memory" on armv7hl (#1363)
* [Revision #061a0f0b8d](https://github.com/MariaDB/server/commit/061a0f0b8d)\
  2019-07-25 04:38:05 +0400
  * [MDEV-20175](https://jira.mariadb.org/browse/MDEV-20175) Move Type\_handler\_row from Type\_collection\_std to Type\_collection\_row
* [Revision #5cc2096f93](https://github.com/MariaDB/server/commit/5cc2096f93)\
  2019-06-07 16:30:27 +0200
  * Switch Perl DBI scripts from DBD::mysql to DBD::MariaDB driver
* [Revision #9a7d96e832](https://github.com/MariaDB/server/commit/9a7d96e832)\
  2019-07-01 17:21:57 +0200
  * Update man pages for 10.5
* [Revision #e6ff3f9d1c](https://github.com/MariaDB/server/commit/e6ff3f9d1c)\
  2019-07-12 06:58:51 +0400
  * [MDEV-20052](https://jira.mariadb.org/browse/MDEV-20052) Add a MEM\_ROOT pointer argument to Type\_handler::make\_xxx\_field()
* [Revision #1517087b54](https://github.com/MariaDB/server/commit/1517087b54)\
  2019-07-11 14:50:39 +0400
  * [MDEV-20042](https://jira.mariadb.org/browse/MDEV-20042) Implement EXTRA2\_FIELD\_DATA\_TYPE\_INFO in FRM
* [Revision #c8e94e5eda](https://github.com/MariaDB/server/commit/c8e94e5eda)\
  2019-07-11 16:45:18 +0400
  * Adding `-Dcplusplus` into the ABI check command line
* [Revision #265a7d1613](https://github.com/MariaDB/server/commit/265a7d1613)\
  2019-07-10 11:55:16 +0400
  * [MDEV-20009](https://jira.mariadb.org/browse/MDEV-20009) Add CAST(expr AS pluggable\_type)
* [Revision #e37d7a3715](https://github.com/MariaDB/server/commit/e37d7a3715)\
  2019-07-10 07:17:25 +0400
  * [MDEV-20006](https://jira.mariadb.org/browse/MDEV-20006) Move geometry specific code in Field\_blob::get\_key\_image() to Field\_geom
* [Revision #aca5532113](https://github.com/MariaDB/server/commit/aca5532113)\
  2019-07-10 05:14:02 +0400
  * A cleanup `[MDEV-19994](https://jira.mariadb.org/browse/MDEV-19994) Add class Function_collection` (buildbot warnings)
* [Revision #feb2695ed3](https://github.com/MariaDB/server/commit/feb2695ed3)\
  2019-07-09 19:47:57 +0400
  * [MDEV-20004](https://jira.mariadb.org/browse/MDEV-20004) Move Field\_geom from field.cc to sql\_type\_geom.cc
* [Revision #4dc85973b4](https://github.com/MariaDB/server/commit/4dc85973b4)\
  2019-07-09 12:47:42 +0400
  * [MDEV-19994](https://jira.mariadb.org/browse/MDEV-19994) Add class Function\_collection
* [Revision #0940e25d69](https://github.com/MariaDB/server/commit/0940e25d69)\
  2019-07-09 13:02:26 +0400
  * [MDEV-19991](https://jira.mariadb.org/browse/MDEV-19991) Turn I\_S tables GEOMETRY\_COLUMNS and SPATIAL\_REF\_SYS into a plugin
* [Revision #a179de0402](https://github.com/MariaDB/server/commit/a179de0402)\
  2019-07-06 11:09:06 +0400
  * [MDEV-19991](https://jira.mariadb.org/browse/MDEV-19991) Turn I\_S tables GEOMETRY\_COLUMNS and SPATIAL\_REF\_SYS into a plugin
* [Revision #aca29bb754](https://github.com/MariaDB/server/commit/aca29bb754)\
  2019-07-08 14:58:18 +0300
  * Fix test case for [MDEV-16222](https://jira.mariadb.org/browse/MDEV-16222)
* [Revision #ed33a5df8b](https://github.com/MariaDB/server/commit/ed33a5df8b)\
  2019-05-27 23:29:43 +0300
  * [MDEV-19175](https://jira.mariadb.org/browse/MDEV-19175) Server crashes in ha\_partition::vers\_can\_native upon INSERT DELAYED into versioned partitioned table
* [Revision #08baaa14b9](https://github.com/MariaDB/server/commit/08baaa14b9)\
  2019-06-25 10:53:33 +0300
  * [MDEV-16222](https://jira.mariadb.org/browse/MDEV-16222) Assertion \`0' failed in row\_purge\_remove\_sec\_if\_poss\_leaf on table with virtual columns and indexes
* [Revision #b27dc3d93c](https://github.com/MariaDB/server/commit/b27dc3d93c)\
  2019-06-25 18:26:09 +0300
  * Tests: versioning suite fix when no test\_versioning plugin
* [Revision #29ffaf405e](https://github.com/MariaDB/server/commit/29ffaf405e)\
  2019-06-17 11:44:53 +0300
  * [MDEV-19785](https://jira.mariadb.org/browse/MDEV-19785) Storage CONNECT compilation error: unknown type name 'UNZFAM'
* [Revision #a6946c55d3](https://github.com/MariaDB/server/commit/a6946c55d3)\
  2019-07-05 20:52:59 +0400
  * [MDEV-19972](https://jira.mariadb.org/browse/MDEV-19972) Move GIS code from Item\_bool\_func::get\_full\_func\_mm\_tree() to Item\_func\_spatial\_rel::get\_mm\_leaf()
* [Revision #2e57c8cc70](https://github.com/MariaDB/server/commit/2e57c8cc70)\
  2019-07-04 22:45:56 +0400
  * [MDEV-19957](https://jira.mariadb.org/browse/MDEV-19957) Move Type\_handler\_geometry code from sql\_type.h/cc to sql\_type\_geom.h/cc
* [Revision #b3161bd995](https://github.com/MariaDB/server/commit/b3161bd995)\
  2019-07-04 18:26:59 +0400
  * A cleanup (to fix ASAN problem) for [MDEV-19863](https://jira.mariadb.org/browse/MDEV-19863) Add const to TYPELIB pointers
* [Revision #4d6a90942c](https://github.com/MariaDB/server/commit/4d6a90942c)\
  2019-07-04 10:25:36 +0200
  * Fix ASAN on clang-cl
* [Revision #4513e73e0f](https://github.com/MariaDB/server/commit/4513e73e0f)\
  2019-07-01 00:46:41 +0200
  * Remove os\_aio\_simulated\_put\_read\_threads\_to\_sleep()
* [Revision #cdb91533ad](https://github.com/MariaDB/server/commit/cdb91533ad)\
  2019-07-01 00:44:02 +0200
  * Fix clang-cl warning
* [Revision #2a9441d115](https://github.com/MariaDB/server/commit/2a9441d115)\
  2019-07-01 00:43:26 +0200
  * Do not compile socket IO code in WolfSSL
* [Revision #bd4f0dd7b2](https://github.com/MariaDB/server/commit/bd4f0dd7b2)\
  2019-07-01 00:41:36 +0200
  * Windows, compiling cleanups
* [Revision #bd917e0811](https://github.com/MariaDB/server/commit/bd917e0811)\
  2019-07-01 00:39:45 +0200
  * Fix clang-cl warnings
* [Revision #9c9e0ac73d](https://github.com/MariaDB/server/commit/9c9e0ac73d)\
  2019-07-03 20:08:10 +0400
  * [MDEV-19944](https://jira.mariadb.org/browse/MDEV-19944) Remove GIS data types from keyword list in lex.h
* [Revision #695230c067](https://github.com/MariaDB/server/commit/695230c067)\
  2019-07-04 00:42:40 +0300
  * [MDEV-19940](https://jira.mariadb.org/browse/MDEV-19940): Fix integer type mismatch
* [Revision #8773bee9f7](https://github.com/MariaDB/server/commit/8773bee9f7)\
  2019-07-04 00:29:38 +0300
  * [MDEV-18582](https://jira.mariadb.org/browse/MDEV-18582): Fix the 32-bit build
* [Revision #412533b4a7](https://github.com/MariaDB/server/commit/412533b4a7)\
  2019-07-03 17:31:20 +0300
  * [MDEV-18582](https://jira.mariadb.org/browse/MDEV-18582): Extend SHOW STATUS LIKE 'Innodb\_%'
* [Revision #61e26289fc](https://github.com/MariaDB/server/commit/61e26289fc)\
  2019-07-03 16:05:34 +0300
  * [MDEV-18582](https://jira.mariadb.org/browse/MDEV-18582) preparation: Allocate ibuf statically
* [Revision #d09aec7a15](https://github.com/MariaDB/server/commit/d09aec7a15)\
  2019-06-28 11:20:46 +0300
  * [MDEV-19940](https://jira.mariadb.org/browse/MDEV-19940) Clean up INFORMATION\_SCHEMA.INNODB\_ tables
* [Revision #d8b8f55af3](https://github.com/MariaDB/server/commit/d8b8f55af3)\
  2019-07-03 09:04:29 +0300
  * [MDEV-19908](https://jira.mariadb.org/browse/MDEV-19908): Add override keywords
* [Revision #7b5bfa53aa](https://github.com/MariaDB/server/commit/7b5bfa53aa)\
  2019-07-03 18:02:22 +0400
  * A cleanup for [MDEV-19923](https://jira.mariadb.org/browse/MDEV-19923) Add type handlers for geometry sub-types
* [Revision #b511202335](https://github.com/MariaDB/server/commit/b511202335)\
  2019-07-03 13:05:15 +0400
  * [MDEV-19923](https://jira.mariadb.org/browse/MDEV-19923) Add type handlers for geometry sub-types
* [Revision #c1519d62d0](https://github.com/MariaDB/server/commit/c1519d62d0)\
  2019-07-01 22:07:32 +0800
  * Fix github urls of submodules
* [Revision #2a8ae4bdce](https://github.com/MariaDB/server/commit/2a8ae4bdce)\
  2019-06-25 15:02:34 +0530
  * [MDEV-19855](https://jira.mariadb.org/browse/MDEV-19855): Create "Sql\_cmd\_show\_slave\_status" class for "SHOW SLAVE STATUS" command.
* [Revision #b3b965a94d](https://github.com/MariaDB/server/commit/b3b965a94d)\
  2019-06-28 05:55:57 +0000
  * Fix build failure on CentOS for MariaDB official CI
* [Revision #97c268f864](https://github.com/MariaDB/server/commit/97c268f864)\
  2019-06-30 00:19:28 +0200
  * Windows, compiling . various cleanups, use /Zi instead of /Z7
* [Revision #0efe50ec35](https://github.com/MariaDB/server/commit/0efe50ec35)\
  2019-06-29 23:53:09 +0200
  * Remove the most annoying clang-cl warnings
* [Revision #0179aad633](https://github.com/MariaDB/server/commit/0179aad633)\
  2019-06-29 23:51:24 +0200
  * Windows, compiling : Reenable /MP for connect engine.
* [Revision #460de628a9](https://github.com/MariaDB/server/commit/460de628a9)\
  2019-06-29 14:28:20 +0200
  * In case WITH\_WSREP is enabled, build wsrep as plugin If it is not enabled, build wsrep as static "stub" library from wsrep\_dummy.cc ´
* [Revision #db80f04751](https://github.com/MariaDB/server/commit/db80f04751)\
  2019-06-28 15:53:49 +0200
  * Cleanup - do not dllexport statically built plugins
* [Revision #6dc71d4f10](https://github.com/MariaDB/server/commit/6dc71d4f10)\
  2019-06-28 13:21:39 +0200
  * improve build, allow sql library to be built in parallel with builtins
* [Revision #a89f1faf7b](https://github.com/MariaDB/server/commit/a89f1faf7b)\
  2019-06-27 21:08:14 +0200
  * Remove feedback from Windows MSI
* [Revision #cccfa9dcfe](https://github.com/MariaDB/server/commit/cccfa9dcfe)\
  2019-06-29 09:48:54 +0400
  * [MDEV-19908](https://jira.mariadb.org/browse/MDEV-19908) Add class Type\_collection
* [Revision #5de9dd7b47](https://github.com/MariaDB/server/commit/5de9dd7b47)\
  2019-06-28 21:12:57 +0400
  * A cleanup for [MDEV-19897](https://jira.mariadb.org/browse/MDEV-19897) Rename source code variable names from utf8 to utf8mb3
* [Revision #3e7e87ddcc](https://github.com/MariaDB/server/commit/3e7e87ddcc)\
  2019-06-28 09:05:12 +0400
  * [MDEV-19897](https://jira.mariadb.org/browse/MDEV-19897) Rename source code variable names from utf8 to utf8mb3
* [Revision #323a87b591](https://github.com/MariaDB/server/commit/323a87b591)\
  2019-06-28 12:35:02 +0400
  * [MDEV-19888](https://jira.mariadb.org/browse/MDEV-19888) Add abstract class Item\_json\_func
* [Revision #cff7cf15d7](https://github.com/MariaDB/server/commit/cff7cf15d7)\
  2019-06-27 20:05:01 +0200
  * Windows MSI : small cleanups, disable Windows 7/8
* [Revision #74a744b51f](https://github.com/MariaDB/server/commit/74a744b51f)\
  2019-06-27 19:33:25 +0200
  * Windows : Do not package redistributable C runtime , nor merge modules into Windows installers
* [Revision #b60aee58c7](https://github.com/MariaDB/server/commit/b60aee58c7)\
  2019-06-27 19:25:33 +0200
  * [MDEV-17279](https://jira.mariadb.org/browse/MDEV-17279) Windows : link C runtime dynamically Improve previous patch so we do not depend on (tiny) compiler-version dependent libraries, i.e vcruntime140.dll, and msvcp140.dll
* [Revision #93942dfe8f](https://github.com/MariaDB/server/commit/93942dfe8f)\
  2019-06-21 23:21:22 +0200
  * Windows - simplify code in my\_getsystime.
* [Revision #79cd2f5ef1](https://github.com/MariaDB/server/commit/79cd2f5ef1)\
  2019-06-27 01:58:48 +0300
  * Added type conversion to fix compilation error on windows
* [Revision #e133aa1e2e](https://github.com/MariaDB/server/commit/e133aa1e2e)\
  2019-06-27 01:33:15 +0300
  * Added testcase for [MDEV-19585](https://jira.mariadb.org/browse/MDEV-19585)
* Merge [Revision #1a41fc77dd](https://github.com/MariaDB/server/commit/1a41fc77dd) 2019-06-27 01:21:41 +0300 - Merge remote-tracking branch 'origin/10.4' into 10.5
* [Revision #8e2a24bb33](https://github.com/MariaDB/server/commit/8e2a24bb33)\
  2019-06-26 21:00:51 +0300
  * Added s3\_protocol\_version=auto
* [Revision #0765d823e4](https://github.com/MariaDB/server/commit/0765d823e4)\
  2019-06-26 20:16:38 +0300
  * Updated to latest libmarias3 to fix some compatiblity issues
* [Revision #f48943468f](https://github.com/MariaDB/server/commit/f48943468f)\
  2019-06-26 18:24:04 +0300
  * [MDEV-19575](https://jira.mariadb.org/browse/MDEV-19575) Fixed assert in ma\_pagecache
* [Revision #f44c687815](https://github.com/MariaDB/server/commit/f44c687815)\
  2019-06-26 18:22:18 +0300
  * S3: Don't do discover in mysql database (makes boot faster and safer)
* [Revision #9ca517613a](https://github.com/MariaDB/server/commit/9ca517613a)\
  2019-06-26 18:21:02 +0300
  * BUILD scripts: Don't build with-plugin-test\_sql\_discovery staticly
* [Revision #5c5ea59bf8](https://github.com/MariaDB/server/commit/5c5ea59bf8)\
  2019-05-28 11:02:16 +0300
  * [MDEV-19867](https://jira.mariadb.org/browse/MDEV-19867): fix mysqldump to by default not copy S3 tables
* [Revision #878ad986fd](https://github.com/MariaDB/server/commit/878ad986fd)\
  2019-06-03 08:30:37 +0300
  * [MDEV-19464](https://jira.mariadb.org/browse/MDEV-19464): Altering partitioned table into S3 causes an obscure error
* [Revision #6f3612fa4d](https://github.com/MariaDB/server/commit/6f3612fa4d)\
  2019-06-26 06:46:55 +0400
  * [MDEV-19861](https://jira.mariadb.org/browse/MDEV-19861) Add intfastructure to have ENUM columns in INFORMATION\_SCHEMA
* [Revision #677133f1b3](https://github.com/MariaDB/server/commit/677133f1b3)\
  2019-06-26 05:29:44 +0400
  * [MDEV-19863](https://jira.mariadb.org/browse/MDEV-19863) Add const to TYPELIB pointers
* [Revision #8d4c159b1b](https://github.com/MariaDB/server/commit/8d4c159b1b)\
  2019-06-25 13:09:06 +0300
  * Added s3\_debug to be able to debug s3 connections
* [Revision #e6297bbe37](https://github.com/MariaDB/server/commit/e6297bbe37)\
  2019-06-24 12:14:31 +0300
  * Updated to latest libmarias3
* [Revision #6aebaafe03](https://github.com/MariaDB/server/commit/6aebaafe03)\
  2019-06-24 12:13:19 +0300
  * Added S3 test case with InnoDB
* [Revision #c62eaa7bdf](https://github.com/MariaDB/server/commit/c62eaa7bdf)\
  2019-06-22 09:15:37 +0400
  * [MDEV-19843](https://jira.mariadb.org/browse/MDEV-19843) Modify ST\_FIELD\_INFO to use Type\_handler and LEX\_CSTRING
* [Revision #5e474f92b5](https://github.com/MariaDB/server/commit/5e474f92b5)\
  2019-06-22 07:08:14 +0400
  * [MDEV-19836](https://jira.mariadb.org/browse/MDEV-19836) Reuse new I\_S table definition helper classes for RocksDB
* [Revision #8d0983330f](https://github.com/MariaDB/server/commit/8d0983330f)\
  2019-06-22 06:03:33 +0400
  * [MDEV-19833](https://jira.mariadb.org/browse/MDEV-19833) Reuse new I\_S table definition helper classes for Mronga
* [Revision #1cbbe35450](https://github.com/MariaDB/server/commit/1cbbe35450)\
  2019-06-22 05:45:48 +0400
  * [MDEV-19832](https://jira.mariadb.org/browse/MDEV-19832) Reuse new I\_S table definition helper classes for Spider
* [Revision #1c27a050e5](https://github.com/MariaDB/server/commit/1c27a050e5)\
  2019-06-21 06:48:04 +0400
  * [MDEV-19818](https://jira.mariadb.org/browse/MDEV-19818) Reuse new I\_S table definition helper classes for TokuDB
* [Revision #9561b0b47e](https://github.com/MariaDB/server/commit/9561b0b47e)\
  2019-06-19 10:49:49 +0400
  * [MDEV-19810](https://jira.mariadb.org/browse/MDEV-19810) Reuse new I\_S table definition helper classes for InnoDB
* Merge [Revision #49e5323dbd](https://github.com/MariaDB/server/commit/49e5323dbd) 2019-06-20 09:22:10 +0300 - Merge 10.4 into 10.5
* [Revision #16ac8404ac](https://github.com/MariaDB/server/commit/16ac8404ac)\
  2019-06-17 15:50:59 +0100
  * [MDEV-19787](https://jira.mariadb.org/browse/MDEV-19787) Speedup Table\_map\_iterator, via compiler intrinsics
* [Revision #4594d68d10](https://github.com/MariaDB/server/commit/4594d68d10)\
  2019-06-15 16:04:49 +0200
  * [MDEV-19702](https://jira.mariadb.org/browse/MDEV-19702) Refactor Bitmap to be based on ulonglong, not on uint32
* Merge [Revision #3c88ce4cd1](https://github.com/MariaDB/server/commit/3c88ce4cd1) 2019-06-18 11:30:06 +0300 - Merge 10.4 into 10.5
* [Revision #44d06cd39d](https://github.com/MariaDB/server/commit/44d06cd39d)\
  2019-06-18 09:02:52 +0200
  * Fix compile warning/error on Windows.
* [Revision #10ebabc364](https://github.com/MariaDB/server/commit/10ebabc364)\
  2019-06-17 22:33:17 +0100
  * Windows related cleanups, remove old code.
* [Revision #73be875c8e](https://github.com/MariaDB/server/commit/73be875c8e)\
  2019-06-17 21:54:44 +0100
  * [MDEV-19773](https://jira.mariadb.org/browse/MDEV-19773) : simplify implementation of Windows rwlock
* [Revision #4156b1a260](https://github.com/MariaDB/server/commit/4156b1a260)\
  2019-06-16 07:51:59 +0400
  * [MDEV-19772](https://jira.mariadb.org/browse/MDEV-19772) Add helper classes for ST\_FIELD\_INFO
* Merge [Revision #984d7100cd](https://github.com/MariaDB/server/commit/984d7100cd) 2019-06-13 18:36:09 +0300 - Merge 10.4 into 10.5
* [Revision #d46db415ce](https://github.com/MariaDB/server/commit/d46db415ce)\
  2019-06-12 19:47:40 +0300
  * [MDEV-19738](https://jira.mariadb.org/browse/MDEV-19738): Skip doublewrite on MLOG\_ZIP\_PAGE\_COMPRESS
* [Revision #8bb4ea2e6f](https://github.com/MariaDB/server/commit/8bb4ea2e6f)\
  2019-06-12 19:36:54 +0300
  * [MDEV-19738](https://jira.mariadb.org/browse/MDEV-19738): Doublewrite buffer is unnecessarily used for newly (re)initialized pages
* [Revision #38018f48b6](https://github.com/MariaDB/server/commit/38018f48b6)\
  2019-06-12 19:36:30 +0300
  * [MDEV-19586](https://jira.mariadb.org/browse/MDEV-19586): Remove unnecessary iteration
* [Revision #b6e0d2475c](https://github.com/MariaDB/server/commit/b6e0d2475c)\
  2019-06-12 12:25:24 +0300
  * Move server\_threads.erase() under lightweight cleanup as when plugins\_are\_initialized we already called unlink\_thd() and that calls server\_threads.erase()
* [Revision #e68d3e4557](https://github.com/MariaDB/server/commit/e68d3e4557)\
  2019-06-11 15:50:44 +0300
  * test commit
* [Revision #177a571e01](https://github.com/MariaDB/server/commit/177a571e01)\
  2019-06-11 11:03:18 +0300
  * [MDEV-19586](https://jira.mariadb.org/browse/MDEV-19586) Replace recv\_sys\_t::addr\_hash with a std::map
* [Revision #992d2494e7](https://github.com/MariaDB/server/commit/992d2494e7)\
  2019-05-30 20:59:34 +0300
  * Define page\_id\_t in buf0types.h
* [Revision #f42bda6d75](https://github.com/MariaDB/server/commit/f42bda6d75)\
  2019-06-11 07:54:37 +0400
  * [MDEV-19727](https://jira.mariadb.org/browse/MDEV-19727) Add Type\_handler::Key\_part\_spec\_init\_ft
* [Revision #163665640a](https://github.com/MariaDB/server/commit/163665640a)\
  2019-06-10 13:59:45 +0400
  * [MDEV-19724](https://jira.mariadb.org/browse/MDEV-19724) Add Field::tmp\_engine\_column\_type()
* [Revision #b685109596](https://github.com/MariaDB/server/commit/b685109596)\
  2019-06-07 07:46:14 +0400
  * [MDEV-19710](https://jira.mariadb.org/browse/MDEV-19710) Split the server side code in rpl\_utility.cc into virtual methods in Type\_handler
* [Revision #9d6d37b5d0](https://github.com/MariaDB/server/commit/9d6d37b5d0)\
  2019-06-07 06:43:14 +0400
  * Cleanup: adding "const" qualifiers to methods in Field
* [Revision #bf70430ead](https://github.com/MariaDB/server/commit/bf70430ead)\
  2019-04-24 09:00:59 +0300
  * [MDEV-17709](https://jira.mariadb.org/browse/MDEV-17709) Remove handlerton::state
* [Revision #ab190194cf](https://github.com/MariaDB/server/commit/ab190194cf)\
  2019-06-04 12:44:24 +0400
  * [MDEV-19686](https://jira.mariadb.org/browse/MDEV-19686) Add method Type\_handler::dyncol\_type
* [Revision #7966258a64](https://github.com/MariaDB/server/commit/7966258a64)\
  2019-06-04 10:56:53 +0400
  * [MDEV-19345](https://jira.mariadb.org/browse/MDEV-19345) Cleanup inconsistency in setting HA\_(BLOB|VAR\_LENGTH|BIT)\_PART flags
* [Revision #bf5a144e16](https://github.com/MariaDB/server/commit/bf5a144e16)\
  2019-05-31 16:44:17 +0400
  * [MDEV-19639](https://jira.mariadb.org/browse/MDEV-19639) + [MDEV-19640](https://jira.mariadb.org/browse/MDEV-19640) fix + preparatory changes for [WL#4179](https://askmonty.org/worklog/?tid=4179)
* Merge [Revision #f859789e7d](https://github.com/MariaDB/server/commit/f859789e7d) 2019-06-03 13:24:41 +0200 - Merge branch '10.4' into 10.5
* [Revision #c51f615bf5](https://github.com/MariaDB/server/commit/c51f615bf5)\
  2019-06-01 13:36:52 +0300
  * Added options --s3-protocol-version and --s3-host-name
* [Revision #3e83034ee6](https://github.com/MariaDB/server/commit/3e83034ee6)\
  2019-06-01 13:34:57 +0300
  * Fixed build scripts to not use -fno-rtti
* [Revision #f2d608dd49](https://github.com/MariaDB/server/commit/f2d608dd49)\
  2019-05-31 15:33:04 +0300
  * Update to latest libmarias3
* [Revision #daeaa600ef](https://github.com/MariaDB/server/commit/daeaa600ef)\
  2019-05-31 08:28:22 +0000
  * [MDEV-19312](https://jira.mariadb.org/browse/MDEV-19312) Make throttling interval depend on thread\_pool\_stall\_limit
* Merge [Revision #28fad39de7](https://github.com/MariaDB/server/commit/28fad39de7) 2019-05-29 22:29:05 +0300 - Merge 10.4 into 10.5
* [Revision #da65298f36](https://github.com/MariaDB/server/commit/da65298f36)\
  2019-05-28 17:02:50 +0400
  * Adding a forgotten --source include/have\_debug.inc into alter\_table\_debug.test
* [Revision #f021317ae1](https://github.com/MariaDB/server/commit/f021317ae1)\
  2019-05-28 15:50:11 +0400
  * [MDEV-19612](https://jira.mariadb.org/browse/MDEV-19612) Split ALTER related data type specific code in sql\_table.cc to Type\_handler
* [Revision #d1d6fe9abf](https://github.com/MariaDB/server/commit/d1d6fe9abf)\
  2019-05-28 10:26:08 +0400
  * Using more of Sql\_mode\_save. Adding a similar class for THD::abort\_on\_warnings.
* Merge [Revision #c0cd662b98](https://github.com/MariaDB/server/commit/c0cd662b98) 2019-05-27 11:08:51 +0300 - Merge 10.4 to 10.5
* [Revision #ff10e0f646](https://github.com/MariaDB/server/commit/ff10e0f646)\
  2019-05-26 15:55:14 +0200
  * [MDEV-19313](https://jira.mariadb.org/browse/MDEV-19313) Add test for thread\_pool\_info
* [Revision #307ca69356](https://github.com/MariaDB/server/commit/307ca69356)\
  2019-05-26 13:35:07 +0200
  * Add some variables to the generic threadpool, that could help to analyze stalls etc better.
* [Revision #2fc13d04d1](https://github.com/MariaDB/server/commit/2fc13d04d1)\
  2019-05-26 13:25:12 +0200
  * [MDEV-19313](https://jira.mariadb.org/browse/MDEV-19313) Threadpool : provide information schema tables for internals of generic threadpool
* [Revision #5f18bd3a35](https://github.com/MariaDB/server/commit/5f18bd3a35)\
  2019-05-26 12:54:46 +0200
  * Add new option NOT\_EMBEDDED, for plugins
* [Revision #9f23f8e598](https://github.com/MariaDB/server/commit/9f23f8e598)\
  2019-05-26 06:17:35 +0400
  * [MDEV-19599](https://jira.mariadb.org/browse/MDEV-19599) Change db\_name, table\_name to LEX\_CSTRING in Item\_ident and Send\_field
* [Revision #ac93d7d674](https://github.com/MariaDB/server/commit/ac93d7d674)\
  2019-05-25 11:40:48 +0400
  * [MDEV-19593](https://jira.mariadb.org/browse/MDEV-19593) Split create\_schema\_table() into virtual methods in Type\_handler
* [Revision #0928596a8b](https://github.com/MariaDB/server/commit/0928596a8b)\
  2019-05-24 22:20:27 +0800
  * Armv8 CRC32 optimization (#772)
* [Revision #a74b01ea0e](https://github.com/MariaDB/server/commit/a74b01ea0e)\
  2019-05-23 15:09:40 +0400
  * [MDEV-16548](https://jira.mariadb.org/browse/MDEV-16548) - Innodb fails to start on older kernels that don't support F\_DUPFD\_CLOEXEC
* [Revision #5f5a0b3bb6](https://github.com/MariaDB/server/commit/5f5a0b3bb6)\
  2019-05-23 12:55:03 +0400
  * [MDEV-16548](https://jira.mariadb.org/browse/MDEV-16548) - Innodb fails to start on older kernels that don't support F\_DUPFD\_CLOEXEC
* [Revision #893472d005](https://github.com/MariaDB/server/commit/893472d005)\
  2019-05-23 17:34:08 +0300
  * [MDEV-19570](https://jira.mariadb.org/browse/MDEV-19570) Deprecate and ignore innodb\_undo\_logs, remove innodb\_rollback\_segments
* [Revision #c83018751c](https://github.com/MariaDB/server/commit/c83018751c)\
  2019-05-23 14:57:29 +0400
  * [MDEV-19566](https://jira.mariadb.org/browse/MDEV-19566) Remove Item::name related strlen() calls in constructors of some Item\_string descendands
* Merge [Revision #826f9d4f7e](https://github.com/MariaDB/server/commit/826f9d4f7e) 2019-05-23 10:32:21 +0300 - Merge 10.4 into 10.5
* [Revision #e5d71e0b3d](https://github.com/MariaDB/server/commit/e5d71e0b3d)\
  2019-05-22 15:19:50 +0300
  * [MDEV-19551](https://jira.mariadb.org/browse/MDEV-19551) Remove alias innodb\_stats\_sample\_pages
* [Revision #1a6f470464](https://github.com/MariaDB/server/commit/1a6f470464)\
  2019-05-22 14:49:38 +0300
  * [MDEV-19544](https://jira.mariadb.org/browse/MDEV-19544) Remove innodb\_locks\_unsafe\_for\_binlog
* [Revision #47cede646b](https://github.com/MariaDB/server/commit/47cede646b)\
  2019-05-22 10:31:44 +0300
  * [MDEV-19543](https://jira.mariadb.org/browse/MDEV-19543) Deprecate and ignore innodb\_log\_checksums
* [Revision #3eef9f213f](https://github.com/MariaDB/server/commit/3eef9f213f)\
  2019-05-21 19:12:57 +0300
  * [MDEV-17841](https://jira.mariadb.org/browse/MDEV-17841): Fix -Wsometimes-uninitialized
* [Revision #483536ec3a](https://github.com/MariaDB/server/commit/483536ec3a)\
  2019-05-23 10:16:23 +0300
  * Adjust innodb.innodb-wl5522-debug result
* [Revision #55a2ca3e6a](https://github.com/MariaDB/server/commit/55a2ca3e6a)\
  2019-05-22 08:53:24 +0400
  * [MDEV-19550](https://jira.mariadb.org/browse/MDEV-19550) Move specific parts of log\_event.cc to log\_event\_client.cc and log\_event\_server.cc
* [Revision #ebfe8c4e0e](https://github.com/MariaDB/server/commit/ebfe8c4e0e)\
  2019-05-17 16:34:35 +0300
  * Make it trivial to get stack traces from external programs.
* [Revision #ab38b7511b](https://github.com/MariaDB/server/commit/ab38b7511b)\
  2019-04-15 18:16:02 +0300
  * [MDEV-17841](https://jira.mariadb.org/browse/MDEV-17841) S3 storage engine
* [Revision #2ca2dcac6a](https://github.com/MariaDB/server/commit/2ca2dcac6a)\
  2019-05-05 19:50:12 +0200
  * aria is mandatory now, so don't bother with CMAKE\_DEPENDENT\_OPTION
* [Revision #043a3a0176](https://github.com/MariaDB/server/commit/043a3a0176)\
  2019-05-08 23:39:29 +0300
  * Avoid not needed renames in ALTER TABLE
* [Revision #10e8ba13c6](https://github.com/MariaDB/server/commit/10e8ba13c6)\
  2019-05-08 23:15:16 +0300
  * ha\_discover\_table\_names() now always remove duplicates
* [Revision #007f68c37f](https://github.com/MariaDB/server/commit/007f68c37f)\
  2019-05-08 23:12:01 +0300
  * Replace ha\_notify\_table\_changed() with notify\_tabledef\_changed()
* [Revision #96037a6f03](https://github.com/MariaDB/server/commit/96037a6f03)\
  2019-05-08 23:14:09 +0300
  * Updated error message for HA\_ERR\_INCOMPATIBLE\_DEFINITION
* [Revision #e533ba9b84](https://github.com/MariaDB/server/commit/e533ba9b84)\
  2019-05-08 23:20:51 +0300
  * Renamed tmp file using #sql\_#\_

## to #sql-#-\#

* [Revision #ebf372ddae](https://github.com/MariaDB/server/commit/ebf372ddae)\
  2019-05-08 23:22:00 +0300
  * Indentation cleanups
* [Revision #0b9f7f86f8](https://github.com/MariaDB/server/commit/0b9f7f86f8)\
  2019-04-16 16:13:27 +0300
  * Removed not used function maria\_clone()
* [Revision #2faa7dcd5c](https://github.com/MariaDB/server/commit/2faa7dcd5c)\
  2019-05-15 12:08:14 +0300
  * Updated debian packages to 10.5
* [Revision #437da7bc54](https://github.com/MariaDB/server/commit/437da7bc54)\
  2019-05-21 18:57:57 +0300
  * [MDEV-19534](https://jira.mariadb.org/browse/MDEV-19534) Make innodb\_checksum\_algorithm=full\_crc32 by default, and remove innodb\_checksums
* [Revision #424dc49d41](https://github.com/MariaDB/server/commit/424dc49d41)\
  2019-05-21 19:27:26 +0400
  * Attempt fixing ERR\_remove\_state warning
* [Revision #54b81cf6ca](https://github.com/MariaDB/server/commit/54b81cf6ca)\
  2019-05-19 20:18:16 +0400
  * mysql\_socket\_accept() microoptimisations
* [Revision #a61baa7a25](https://github.com/MariaDB/server/commit/a61baa7a25)\
  2019-05-19 17:00:31 +0400
  * Maintain connection\_count atomically
* [Revision #0bee021b78](https://github.com/MariaDB/server/commit/0bee021b78)\
  2019-05-18 20:43:29 +0400
  * Simplified away wake\_thread
* [Revision #34dfcbe3a6](https://github.com/MariaDB/server/commit/34dfcbe3a6)\
  2019-05-18 23:01:44 +0400
  * Move thread re-initialisation out of cache\_thread
* [Revision #ebc55c8577](https://github.com/MariaDB/server/commit/ebc55c8577)\
  2019-05-19 02:10:40 +0400
  * Simplified away scheduler\_functions::end\_thread()
* [Revision #6900aaf417](https://github.com/MariaDB/server/commit/6900aaf417)\
  2019-05-19 01:04:22 +0400
  * Simplified away init\_new\_connection\_thread()
* [Revision #8d9d4aa6d6](https://github.com/MariaDB/server/commit/8d9d4aa6d6)\
  2019-05-18 00:02:04 +0400
  * Signal COND\_thread\_cache out of mutex
* [Revision #5d183df77b](https://github.com/MariaDB/server/commit/5d183df77b)\
  2019-05-17 20:26:49 +0400
  * Try accept a few times before falling back to poll
* [Revision #87775402cd](https://github.com/MariaDB/server/commit/87775402cd)\
  2019-05-16 00:50:58 +0400
  * Improved ha\_close\_connection() scalability
* [Revision #5e139437a5](https://github.com/MariaDB/server/commit/5e139437a5)\
  2019-05-16 15:18:15 +0400
  * Adiue thd\_ha\_data(), you've broke many hearts
* [Revision #ec926b0f40](https://github.com/MariaDB/server/commit/ec926b0f40)\
  2019-05-16 12:41:19 +0400
  * Fixed RocksDB to follow THD ha\_data protocol
* [Revision #8c8d584f06](https://github.com/MariaDB/server/commit/8c8d584f06)\
  2019-05-16 14:54:54 +0400
  * Fixed InnoDB to not use broken thd\_ha\_data()
* [Revision #5e1b3cc8dc](https://github.com/MariaDB/server/commit/5e1b3cc8dc)\
  2019-05-16 15:07:53 +0400
  * Fixed Aria to follow THD ha\_data protocol
* [Revision #ba59cc0f37](https://github.com/MariaDB/server/commit/ba59cc0f37)\
  2019-05-16 14:48:24 +0400
  * Fixed Sphinx to follow THD ha\_data protocol
* [Revision #00e533c78b](https://github.com/MariaDB/server/commit/00e533c78b)\
  2019-05-16 14:37:08 +0400
  * Fixed Mroonga to follow THD ha\_data protocol
* [Revision #5c18ba6c88](https://github.com/MariaDB/server/commit/5c18ba6c88)\
  2019-05-19 17:39:15 +0400
  * Fixed Spider to follow THD ha\_data protocol
* [Revision #762d2b96fa](https://github.com/MariaDB/server/commit/762d2b96fa)\
  2019-05-16 14:19:05 +0400
  * Fixed FederatedX to follow THD ha\_data protocol
* [Revision #ce30c99478](https://github.com/MariaDB/server/commit/ce30c99478)\
  2019-05-17 00:38:35 +0400
  * Moved vio allocation to connection thread
* [Revision #efb61c12a9](https://github.com/MariaDB/server/commit/efb61c12a9)\
  2019-05-12 11:15:53 +0400
  * Simplified away CONNECT::real\_id
* [Revision #7192d7b700](https://github.com/MariaDB/server/commit/7192d7b700)\
  2019-05-12 02:55:57 +0400
  * Simplified away CONNECT::extra\_port
* [Revision #c90c769807](https://github.com/MariaDB/server/commit/c90c769807)\
  2019-05-12 02:24:51 +0400
  * Simplified away CONNECT::host
* [Revision #56b1cdde37](https://github.com/MariaDB/server/commit/56b1cdde37)\
  2019-05-12 01:26:12 +0400
  * Removed duplicate thread cache check
* [Revision #701e2a7edb](https://github.com/MariaDB/server/commit/701e2a7edb)\
  2019-05-11 23:19:30 +0400
  * Optimised fcntl() when accepting connections
* [Revision #218a68bbc5](https://github.com/MariaDB/server/commit/218a68bbc5)\
  2019-05-15 23:23:27 +0400
  * Less shared variables loads under the mutex
* [Revision #8268fa881f](https://github.com/MariaDB/server/commit/8268fa881f)\
  2019-05-11 20:08:55 +0400
  * Moved set\_timespec out of LOCK\_thread\_cache mutex
* [Revision #ca847584eb](https://github.com/MariaDB/server/commit/ca847584eb)\
  2019-05-11 19:51:31 +0400
  * Cleanup redundant abort\_loop checks
* [Revision #042f5165e3](https://github.com/MariaDB/server/commit/042f5165e3)\
  2019-05-14 17:19:43 +0300
  * [MDEV-307](https://jira.mariadb.org/browse/MDEV-307) review minor edits, add yacc\_ora support
* [Revision #e9c6d5a1e8](https://github.com/MariaDB/server/commit/e9c6d5a1e8)\
  2018-08-26 00:25:52 -0400
  * [MDEV-307](https://jira.mariadb.org/browse/MDEV-307) Add functionality for database comments
* Merge [Revision #9a8d1d84f8](https://github.com/MariaDB/server/commit/9a8d1d84f8) 2019-05-16 12:56:02 +0300 - Merge remote-tracking branch 'origin/10.4' into 10.5
* [Revision #a868e799c7](https://github.com/MariaDB/server/commit/a868e799c7)\
  2019-05-13 15:16:29 +0300
  * Change version to 10.5.0

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
