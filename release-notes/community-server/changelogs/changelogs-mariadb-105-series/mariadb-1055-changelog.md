# MariaDB 10.5.5 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download](https://downloads.mariadb.org/mariadb/10.5.5/)[Release Notes](../../old-releases/10.5/10.5.5.md)[Changelog](mariadb-1055-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 10 Aug 2020

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.5.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.14](../changelogs-mariadb-10-4-series/mariadb-10414-changelog.md)
* Merge [Revision #5b3d3792e2](https://github.com/MariaDB/server/commit/5b3d3792e2) 2020-08-07 13:43:08 +0200 - Merge branch '10.4' into 10.5
* [Revision #ad9d8ffd9f](https://github.com/MariaDB/server/commit/ad9d8ffd9f)\
  2020-08-07 03:04:37 +0300
  * List of unstable tests for 10.5.5 release
* [Revision #2c9430dae2](https://github.com/MariaDB/server/commit/2c9430dae2)\
  2020-08-06 17:54:35 +0200
  * update columnstore
* Merge [Revision #384aeecb63](https://github.com/MariaDB/server/commit/384aeecb63) 2020-08-07 13:41:01 +0200 - Merge branch 'merge-perfschema-5.7' into 10.5
* [Revision #bbbe2c1a44](https://github.com/MariaDB/server/commit/bbbe2c1a44)\
  2020-05-08 18:51:40 +0200
  * 5.7.30
* [Revision #36ebd704de](https://github.com/MariaDB/server/commit/36ebd704de)\
  2019-12-11 21:39:26 +0100
  * 5.7.28
* [Revision #15f60c1a73](https://github.com/MariaDB/server/commit/15f60c1a73)\
  2016-07-28 15:52:12 +0200
  * 5.7.13
* [Revision #cd2924bacb](https://github.com/MariaDB/server/commit/cd2924bacb)\
  2020-08-07 13:37:41 +0200
  * [MDEV-23330](https://jira.mariadb.org/browse/MDEV-23330) Server crash or ASAN negative-size-param in my\_strnncollsp\_binary / `SORT_FIELD_ATTR::compare_packed_varstrings`
* [Revision #e081415040](https://github.com/MariaDB/server/commit/e081415040)\
  2020-08-05 19:59:50 +0300
  * [MDEV-23410](https://jira.mariadb.org/browse/MDEV-23410) buf\_LRU\_scan\_and\_free\_block() fails to stop at first freed block
* [Revision #72f677d302](https://github.com/MariaDB/server/commit/72f677d302)\
  2020-08-05 19:58:26 +0300
  * fixup 58e759a9393f76e558c016a3f84656401b9de1ce: clang -Winconsistent-missing-override
* [Revision #28e714b5f6](https://github.com/MariaDB/server/commit/28e714b5f6)\
  2020-08-05 17:00:14 +0200
  * change buitin plugin types from Alpha to Stable as needed
* [Revision #979af00b7c](https://github.com/MariaDB/server/commit/979af00b7c)\
  2020-08-04 22:55:47 +0200
  * Move ColumnStore dependency on jemalloc from rpm Requires: to Recommends:
* [Revision #694f43644b](https://github.com/MariaDB/server/commit/694f43644b)\
  2020-08-04 22:46:31 +0200
  * CPackRPM support for Recommends:
* [Revision #2b856ecd98](https://github.com/MariaDB/server/commit/2b856ecd98)\
  2020-08-04 14:44:40 +0200
  * [MCOL-4229](https://jira.mariadb.org/browse/MCOL-4229) ColumnStore fails to build on Ubuntu 20.10 due to missing readline
* [Revision #44885273f2](https://github.com/MariaDB/server/commit/44885273f2)\
  2020-08-04 09:35:17 +0200
  * [MDEV-23342](https://jira.mariadb.org/browse/MDEV-23342) MariaDB cannot be installed over MySQL 5.7.30 on Bionic anymore
* [Revision #58e759a939](https://github.com/MariaDB/server/commit/58e759a939)\
  2020-07-27 18:46:37 +0300
  * Added 'final' to some classes to improve generated code
* Merge [Revision #48b5777ebd](https://github.com/MariaDB/server/commit/48b5777ebd) 2020-08-04 17:24:15 +0200 - Merge branch '10.4' into 10.5
* [Revision #bbd70fcc43](https://github.com/MariaDB/server/commit/bbd70fcc43)\
  2020-08-04 06:59:29 +0300
  * [MDEV-23379](https://jira.mariadb.org/browse/MDEV-23379) Deprecate\&ignore InnoDB concurrency throttling parameters
* [Revision #7438fc4f73](https://github.com/MariaDB/server/commit/7438fc4f73)\
  2020-08-04 12:19:40 +1000
  * [MDEV-23362](https://jira.mariadb.org/browse/MDEV-23362): s3 postfix libz -> z
* [Revision #fd1d6969e6](https://github.com/MariaDB/server/commit/fd1d6969e6)\
  2020-08-04 12:09:30 +1000
  * [MDEV-23362](https://jira.mariadb.org/browse/MDEV-23362): s3 - link to zlib
* [Revision #c12d24e291](https://github.com/MariaDB/server/commit/c12d24e291)\
  2020-08-02 20:39:36 +0300
  * [MDEV-23369](https://jira.mariadb.org/browse/MDEV-23369) False sharing in `page_hash_latch::read_lock_wait()`
* Merge [Revision #8ddebb33c2](https://github.com/MariaDB/server/commit/8ddebb33c2) 2020-08-01 14:43:58 +0300 - Merge 10.4 into 10.5
* Merge [Revision #52edc374ac](https://github.com/MariaDB/server/commit/52edc374ac) 2020-08-01 14:43:37 +0300 - Merge 10.4 into 10.5
* Merge [Revision #50a11f396a](https://github.com/MariaDB/server/commit/50a11f396a) 2020-08-01 14:42:51 +0300 - Merge 10.4 into 10.5
* [Revision #842da858b6](https://github.com/MariaDB/server/commit/842da858b6)\
  2020-06-27 15:43:46 +0300
  * Unify config syntax in default files
* [Revision #afbd61811f](https://github.com/MariaDB/server/commit/afbd61811f)\
  2020-06-27 15:41:20 +0300
  * [MDEV-22980](https://jira.mariadb.org/browse/MDEV-22980): Allow plugin-maturity=alpha so S3 plugin loads
* [Revision #a0518ed998](https://github.com/MariaDB/server/commit/a0518ed998)\
  2020-07-31 17:11:17 +0200
  * [MDEV-23357](https://jira.mariadb.org/browse/MDEV-23357) Server crashes in `Sql_cmd_alter_table_exchange_partition::exchange_partition`
* [Revision #c69520c9df](https://github.com/MariaDB/server/commit/c69520c9df)\
  2020-07-29 23:27:25 +0800
  * [MDEV-23030](https://jira.mariadb.org/browse/MDEV-23030): ARM crash on Raspberry Pi 4
* [Revision #f99de8915e](https://github.com/MariaDB/server/commit/f99de8915e)\
  2020-07-04 13:45:56 +0300
  * Deb: Make RocksDB plugin depend on python3 as myrocks\_hotbackup needs it
* [Revision #a10f72aa5e](https://github.com/MariaDB/server/commit/a10f72aa5e)\
  2020-06-28 17:35:02 +0300
  * Deb: Proper DH\_ and DEB\_ flag use in debian/rules
* [Revision #497e7eda8c](https://github.com/MariaDB/server/commit/497e7eda8c)\
  2020-06-28 15:35:30 +0300
  * Deb: Stop suggesting tinyca, upstream project does not exist anymore
* [Revision #bdf8268307](https://github.com/MariaDB/server/commit/bdf8268307)\
  2020-07-11 12:19:00 +0300
  * Deb: Simplify and unify autobake-deb.sh
* [Revision #7a0fa9da03](https://github.com/MariaDB/server/commit/7a0fa9da03)\
  2020-07-11 12:12:34 +0300
  * Deb: Cleanup and document
* [Revision #7c1807a0ad](https://github.com/MariaDB/server/commit/7c1807a0ad)\
  2020-06-19 13:40:50 +0300
  * Deb: On upgrades, stop both mysqld and mariadbd for backwards compat
* [Revision #b8031e362a](https://github.com/MariaDB/server/commit/b8031e362a)\
  2020-06-14 14:25:15 +0300
  * Use mktemp instead of deprecated tempfile
* [Revision #ab48901d54](https://github.com/MariaDB/server/commit/ab48901d54)\
  2020-06-14 14:49:45 +0300
  * Fix spelling errors
* [Revision #05fa4558e0](https://github.com/MariaDB/server/commit/05fa4558e0)\
  2020-07-13 20:23:37 +0300
  * [MDEV-22110](https://jira.mariadb.org/browse/MDEV-22110) InnoDB unnecessarily writes unmodified pages
* [Revision #cf3c3cce1d](https://github.com/MariaDB/server/commit/cf3c3cce1d)\
  2020-07-27 19:33:21 +0300
  * [MDEV-23304](https://jira.mariadb.org/browse/MDEV-23304) Insert into TEMPORARY TABLE fails to invoke `mtr_t::set_modified()`
* [Revision #2c5831b2c5](https://github.com/MariaDB/server/commit/2c5831b2c5)\
  2020-07-13 14:50:43 +0000
  * [MCOL-4166](https://jira.mariadb.org/browse/MCOL-4166) The solution to the minor upgrade issue
* [Revision #6a70398c7a](https://github.com/MariaDB/server/commit/6a70398c7a)\
  2020-07-16 13:01:15 +1000
  * [MDEV-23176](https://jira.mariadb.org/browse/MDEV-23176): s3 curl library path fix
* [Revision #3cb9131ac2](https://github.com/MariaDB/server/commit/3cb9131ac2)\
  2020-07-15 11:23:19 +1000
  * [MDEV-23175](https://jira.mariadb.org/browse/MDEV-23175): my\_timer\_milliseconds clock\_gettime for multiple platfomrs
* [Revision #ba191f7e43](https://github.com/MariaDB/server/commit/ba191f7e43)\
  2020-04-29 18:23:17 +1000
  * mtr: mysqld--help-aria test on OSX fail
* [Revision #fecc6caa27](https://github.com/MariaDB/server/commit/fecc6caa27)\
  2020-06-22 13:31:59 +1000
  * [MDEV-22621](https://jira.mariadb.org/browse/MDEV-22621): perfschema add FreeBSD include header for pthread\_getthreadid\_np
* [Revision #744919552c](https://github.com/MariaDB/server/commit/744919552c)\
  2020-07-24 20:17:43 +0530
  * [MDEV-23229](https://jira.mariadb.org/browse/MDEV-23229) Read of Uninitialized memory during buffer pool resizing
* [Revision #a18639f1a9](https://github.com/MariaDB/server/commit/a18639f1a9)\
  2020-07-23 15:30:29 +0530
  * [MDEV-23216](https://jira.mariadb.org/browse/MDEV-23216): LONGTEXT column with collation doesn't sort
* [Revision #a8d5f57e9a](https://github.com/MariaDB/server/commit/a8d5f57e9a)\
  2020-07-23 11:34:01 +0300
  * Fix test cases Changes to be committed: modified: mysql-test/suite/galera\_3nodes/t/GCF-354.test modified: mysql-test/suite/galera\_3nodes/t/inconsistency\_shutdown.test
* [Revision #ce699df905](https://github.com/MariaDB/server/commit/ce699df905)\
  2020-07-22 17:57:07 +0300
  * thd->m\_transaction\_psi was not properly cleared for new connections
* [Revision #dbcd3384e0](https://github.com/MariaDB/server/commit/dbcd3384e0)\
  2020-07-20 19:26:31 +0300
  * [MDEV-7947](https://jira.mariadb.org/browse/MDEV-7947) strcmp() takes 0.37% in OLTP RO
* [Revision #46ffd47f42](https://github.com/MariaDB/server/commit/46ffd47f42)\
  2020-07-20 19:26:58 +0300
  * Fixed wrong free in comp\_err
* [Revision #d55f8a249e](https://github.com/MariaDB/server/commit/d55f8a249e)\
  2020-07-20 14:15:25 +0300
  * Disable maria.max\_length when using valgrind (too slow)
* [Revision #747479aba2](https://github.com/MariaDB/server/commit/747479aba2)\
  2020-07-17 17:56:17 +0300
  * Fixed removed warning from valgrind in `Protocol::store_str`
* [Revision #61c15ebe32](https://github.com/MariaDB/server/commit/61c15ebe32)\
  2020-07-16 16:30:06 +0300
  * Remove `String::lex_string()` and `String::lex_cstring()`
* [Revision #2682458128](https://github.com/MariaDB/server/commit/2682458128)\
  2020-07-16 12:45:30 +0300
  * Use larger buffer when reading binary and relay logs
* [Revision #c89e927a56](https://github.com/MariaDB/server/commit/c89e927a56)\
  2020-07-16 12:23:37 +0300
  * Clean up Item\_uint() & Item\_int()
* Merge [Revision #5e76e234f5](https://github.com/MariaDB/server/commit/5e76e234f5) 2020-07-23 09:19:06 +0300 - Merge 10.4 into 10.5
* [Revision #92014bd1c6](https://github.com/MariaDB/server/commit/92014bd1c6)\
  2020-07-22 16:09:58 +0530
  * [MDEV-23252](https://jira.mariadb.org/browse/MDEV-23252) Assertion failure `'req_type.is_dblwr_recover() || err == DB_SUCCESS'` for `page_compressed` tables
* [Revision #d96027c84a](https://github.com/MariaDB/server/commit/d96027c84a)\
  2020-07-22 14:40:56 +0530
  * [MDEV-23254](https://jira.mariadb.org/browse/MDEV-23254) Replace `FSP_FLAGS_HAS_PAGE_COMPRESSION` with `fil_space_t::is_compressed`
* [Revision #3d01576af2](https://github.com/MariaDB/server/commit/3d01576af2)\
  2020-07-22 08:48:14 +0300
  * Fix regex on test.
* [Revision #7bffe468b2](https://github.com/MariaDB/server/commit/7bffe468b2)\
  2020-05-19 11:12:26 +0300
  * [MDEV-21910](https://jira.mariadb.org/browse/MDEV-21910) Deadlock between BF abort and manual KILL command
* Merge [Revision #4ec032b492](https://github.com/MariaDB/server/commit/4ec032b492) 2020-07-21 17:33:16 +0300 - Merge 10.4 into 10.5
* [Revision #c89366866b](https://github.com/MariaDB/server/commit/c89366866b)\
  2020-07-17 19:56:33 +0530
  * [MDEV-22970](https://jira.mariadb.org/browse/MDEV-22970) Possible corruption of page\_compressed tables, or when scrubbing is enabled
* Merge [Revision #4d4865de6f](https://github.com/MariaDB/server/commit/4d4865de6f) 2020-07-20 15:55:59 +0300 - Merge 10.4 into 10.5
* Merge [Revision #6c165b4bd6](https://github.com/MariaDB/server/commit/6c165b4bd6) 2020-07-20 15:37:12 +0300 - [MDEV-21910](https://jira.mariadb.org/browse/MDEV-21910): Null-merge 10.4 to 10.5 (FIXME: really merge this!)
* Merge [Revision #054f10365c](https://github.com/MariaDB/server/commit/054f10365c) 2020-07-16 07:15:06 +0300 - Merge 10.4 into 10.5
* [Revision #20512a68d8](https://github.com/MariaDB/server/commit/20512a68d8)\
  2020-07-15 11:23:19 +1000
  * [MDEV-23175](https://jira.mariadb.org/browse/MDEV-23175): my\_timer\_milliseconds ftime deprecated - clock\_gettime replacement
* Merge [Revision #e67daa5653](https://github.com/MariaDB/server/commit/e67daa5653) 2020-07-15 14:51:22 +0300 - Merge 10.4 into 10.5
* [Revision #eb2eaba7fd](https://github.com/MariaDB/server/commit/eb2eaba7fd)\
  2020-07-14 11:48:13 +0400
  * [MDEV-23162](https://jira.mariadb.org/browse/MDEV-23162) Improve Protocol performance for numeric data
* [Revision #be98036f25](https://github.com/MariaDB/server/commit/be98036f25)\
  2020-07-14 11:06:27 +0400
  * Preparatory changes for [MDEV-23162](https://jira.mariadb.org/browse/MDEV-23162) Improve Protocol performance for numeric data
* [Revision #c3afcc7c0a](https://github.com/MariaDB/server/commit/c3afcc7c0a)\
  2020-07-14 16:17:25 +0300
  * [MDEV-16678](https://jira.mariadb.org/browse/MDEV-16678) followup: Adjust the test main.mdl
* [Revision #30e7a0a866](https://github.com/MariaDB/server/commit/30e7a0a866)\
  2020-07-13 19:59:09 +0400
  * [MDEV-23157](https://jira.mariadb.org/browse/MDEV-23157) Remove redundant virtual `Protocol::store()`
* [Revision #5967dfdbbf](https://github.com/MariaDB/server/commit/5967dfdbbf)\
  2020-07-13 16:19:49 +0400
  * [MDEV-23154](https://jira.mariadb.org/browse/MDEV-23154) Add a data type my\_repertoire\_t
* [Revision #d34eb4b1f6](https://github.com/MariaDB/server/commit/d34eb4b1f6)\
  2020-07-13 17:57:11 +0300
  * [MDEV-8139](https://jira.mariadb.org/browse/MDEV-8139) follow-up fix: Remove an unused constexpr
* [Revision #65b4b90317](https://github.com/MariaDB/server/commit/65b4b90317)\
  2020-07-13 17:53:12 +0300
  * [MDEV-22871](https://jira.mariadb.org/browse/MDEV-22871) follow-up: Align buf\_pool.page\_hash.array
* [Revision #9b8bc713b5](https://github.com/MariaDB/server/commit/9b8bc713b5)\
  2020-07-13 17:49:09 +0300
  * Cleanup: Remove redundant #include "ha0ha.h"
* Merge [Revision #af27f17ea1](https://github.com/MariaDB/server/commit/af27f17ea1) 2020-07-13 17:05:13 +0300 - Merge 10.4 into 10.5
* [Revision #2726203994](https://github.com/MariaDB/server/commit/2726203994)\
  2020-07-11 14:04:53 +0000
  * Remove obsolete file from the packaging list.
* [Revision #439377927b](https://github.com/MariaDB/server/commit/439377927b)\
  2020-07-03 16:24:58 +0300
  * Deb: Misc ColumnStore Debian packaging improvements
* [Revision #24ed08c3c4](https://github.com/MariaDB/server/commit/24ed08c3c4)\
  2020-07-09 21:10:47 +0300
  * fix compilation with gcc-10
* [Revision #55c7536a02](https://github.com/MariaDB/server/commit/55c7536a02)\
  2020-06-25 21:59:13 +0300
  * Add man page for new command aria\_s3\_copy
* [Revision #0e86254b05](https://github.com/MariaDB/server/commit/0e86254b05)\
  2020-07-06 15:23:39 +0300
  * [MDEV-22930](https://jira.mariadb.org/browse/MDEV-22930) Unnecessary contention on rw\_lock\_list\_mutex in ibuf\_dummy\_index\_create()
* [Revision #1ae008d272](https://github.com/MariaDB/server/commit/1ae008d272)\
  2020-07-03 12:08:43 +0300
  * replace UT\_LIST with ilist in rw\_lock\_list\_t
* [Revision #ee5841376a](https://github.com/MariaDB/server/commit/ee5841376a)\
  2020-07-06 22:02:16 +0300
  * fix clang compilation
* [Revision #846174c5ba](https://github.com/MariaDB/server/commit/846174c5ba)\
  2020-06-30 15:20:11 +0200
  * [MDEV-23071](https://jira.mariadb.org/browse/MDEV-23071) remove potentially dangerouws casting to Item\_in\_subselect
* [Revision #79c166c56d](https://github.com/MariaDB/server/commit/79c166c56d)\
  2020-07-05 20:38:50 +0300
  * Fix cmake -DWITH\_MSAN=ON
* [Revision #ab4069909d](https://github.com/MariaDB/server/commit/ab4069909d)\
  2020-07-05 16:25:29 +0300
  * After-merge fix for ASAN and MSAN
* Merge [Revision #90d5d90640](https://github.com/MariaDB/server/commit/90d5d90640) 2020-07-04 22:19:49 +0300 - Merge 10.4 into 10.5
* [Revision #a85f81af03](https://github.com/MariaDB/server/commit/a85f81af03)\
  2020-07-04 14:01:55 +0300
  * [MDEV-22535](https://jira.mariadb.org/browse/MDEV-22535) fixup: Define a single-caller function inline
* [Revision #2d00e003b2](https://github.com/MariaDB/server/commit/2d00e003b2)\
  2020-07-04 13:56:38 +0300
  * After-merge fixes for ASAN
* [Revision #478591608e](https://github.com/MariaDB/server/commit/478591608e)\
  2020-06-25 19:21:45 +0200
  * optimize ha\_delete\_table\_force
* [Revision #4227dd2ac6](https://github.com/MariaDB/server/commit/4227dd2ac6)\
  2020-06-25 18:51:45 +0200
  * continue DROP TEMPORARY TABLE t1, t2, t3 after error.
* [Revision #6c52931680](https://github.com/MariaDB/server/commit/6c52931680)\
  2020-06-22 22:14:25 +0200
  * replace HTON\_AUTOMATIC\_DELETE\_TABLE with return -1 from drop\_table()
* [Revision #4876651e0f](https://github.com/MariaDB/server/commit/4876651e0f)\
  2020-06-22 13:21:18 +0200
  * remove mysql\_declare\_plugin declaration from some plugins
* [Revision #7c2ba9e9d7](https://github.com/MariaDB/server/commit/7c2ba9e9d7)\
  2020-06-16 10:33:48 +0200
  * [MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412) Ensure that table is truly dropped when using DROP TABLE
* [Revision #79a3f96166](https://github.com/MariaDB/server/commit/79a3f96166)\
  2020-06-16 09:34:38 +0200
  * rewrite bug#26704 test case
* [Revision #529b6dffe9](https://github.com/MariaDB/server/commit/529b6dffe9)\
  2020-06-15 14:32:53 +0200
  * small cleanup
* [Revision #35f566db8d](https://github.com/MariaDB/server/commit/35f566db8d)\
  2020-06-15 14:06:08 +0200
  * cleanup: make dd\_frm\_type to work as documented
* [Revision #2bb5981c20](https://github.com/MariaDB/server/commit/2bb5981c20)\
  2020-06-15 12:13:44 +0200
  * [MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412) Ensure that table is truly dropped when using DROP TABLE
* [Revision #b014720b6c](https://github.com/MariaDB/server/commit/b014720b6c)\
  2020-06-14 11:48:50 +0200
  * optimization: use hton->drop\_table in few simple cases
* [Revision #c55c292832](https://github.com/MariaDB/server/commit/c55c292832)\
  2020-06-13 21:23:19 +0200
  * introduce hton->drop\_table() method
* [Revision #f17f7a43ba](https://github.com/MariaDB/server/commit/f17f7a43ba)\
  2020-06-16 19:37:27 +0200
  * test dropping of a MEMORY table
* [Revision #d2b852b4ca](https://github.com/MariaDB/server/commit/d2b852b4ca)\
  2020-06-14 11:46:37 +0200
  * cleanup, less #ifdef's
* [Revision #7d75e43261](https://github.com/MariaDB/server/commit/7d75e43261)\
  2020-07-04 02:19:02 +0300
  * Disable rpl\_parallel2 temporarly until we have a proper fix for it in 10.5
* Merge [Revision #0fd89a1a89](https://github.com/MariaDB/server/commit/0fd89a1a89) 2020-07-03 23:31:12 +0300 - Merge remote-tracking branch 'origin/10.4' into 10.5
* [Revision #70684afef2](https://github.com/MariaDB/server/commit/70684afef2)\
  2020-07-03 20:34:46 +0300
  * Atomic write support for ScaleFlux NVMe SSD's
* [Revision #7a4afad969](https://github.com/MariaDB/server/commit/7a4afad969)\
  2020-07-03 15:01:21 +0200
  * compilation fix
* [Revision #6cee9b1953](https://github.com/MariaDB/server/commit/6cee9b1953)\
  2020-06-26 01:47:33 +0300
  * [MDEV-22535](https://jira.mariadb.org/browse/MDEV-22535) `TABLE::initialize_quick_structures()` takes 0.5% in oltp\_read\_only
* [Revision #5cbb18cb44](https://github.com/MariaDB/server/commit/5cbb18cb44)\
  2020-07-02 16:58:35 +0300
  * Fixed typo in InnoDB when compiling with VALGRIND
* Merge [Revision #1813d92d0c](https://github.com/MariaDB/server/commit/1813d92d0c) 2020-07-02 09:41:44 +0300 - Merge 10.4 into 10.5
* [Revision #0fe97c20b3](https://github.com/MariaDB/server/commit/0fe97c20b3)\
  2020-07-02 07:45:19 +0300
  * [MDEV-23017](https://jira.mariadb.org/browse/MDEV-23017): Regression due to unwanted read-ahead
* [Revision #1a4846dedc](https://github.com/MariaDB/server/commit/1a4846dedc)\
  2020-07-01 16:11:58 +0300
  * [MDEV-22690](https://jira.mariadb.org/browse/MDEV-22690) MSAN use-of-uninitialized-value in optimizer\_trace
* [Revision #263f8aff65](https://github.com/MariaDB/server/commit/263f8aff65)\
  2020-06-27 18:44:00 +0200
  * always use python3
* [Revision #d742f282fc](https://github.com/MariaDB/server/commit/d742f282fc)\
  2020-06-29 16:40:55 +0200
  * ColumnStore RPM packaging fixes
* [Revision #04df0bdae7](https://github.com/MariaDB/server/commit/04df0bdae7)\
  2020-06-26 11:29:12 -0400
  * A few important fixes for columnstore.
* Merge [Revision #baca526555](https://github.com/MariaDB/server/commit/baca526555) 2020-06-30 13:18:25 +0200 - Merge remote-tracking branch 'origin/10.5-[MDEV-22729](https://jira.mariadb.org/browse/MDEV-22729)' into 10.5
* [Revision #198a4fee3c](https://github.com/MariaDB/server/commit/198a4fee3c)\
  2020-06-23 14:19:36 +0200
  * [MDEV-22729](https://jira.mariadb.org/browse/MDEV-22729): Additional fix for branch 10.5
* [Revision #0c0f9de40b](https://github.com/MariaDB/server/commit/0c0f9de40b)\
  2020-05-27 21:21:24 +0300
  * [MDEV-22729](https://jira.mariadb.org/browse/MDEV-22729) fixes for galera.galera\_slave\_replay test
* [Revision #d3a2c2eac0](https://github.com/MariaDB/server/commit/d3a2c2eac0)\
  2020-06-30 11:05:03 +0530
  * Make the test func\_json deterministic
* [Revision #baa60b5907](https://github.com/MariaDB/server/commit/baa60b5907)\
  2020-06-29 19:29:35 +0200
  * [MDEV-23038](https://jira.mariadb.org/browse/MDEV-23038) Service registered with deprecated "mysqld.exe --install" crashes on startup
* [Revision #7e19954b9a](https://github.com/MariaDB/server/commit/7e19954b9a)\
  2020-06-29 20:06:28 +0530
  * [MDEV-23029](https://jira.mariadb.org/browse/MDEV-23029): JSON\_OBJECTAGG returns NULL when used together with GROUP BY
* [Revision #c687afbbde](https://github.com/MariaDB/server/commit/c687afbbde)\
  2020-06-29 11:53:43 +0200
  * [MDEV-23039](https://jira.mariadb.org/browse/MDEV-23039) update removed\_variables in mysql\_upgrade\_service for 10.5
* [Revision #baeeb9ba45](https://github.com/MariaDB/server/commit/baeeb9ba45)\
  2020-06-26 23:53:06 +0300
  * Select Handlers: Initialize `JOIN::fields` when running with pushed select
* [Revision #71e8183e41](https://github.com/MariaDB/server/commit/71e8183e41)\
  2020-06-25 01:15:35 +0900
  * [MDEV-22979](https://jira.mariadb.org/browse/MDEV-22979) "mysqld --bootstrap" / mysql\_install\_db hangs when Spider is installed
* [Revision #994026b77f](https://github.com/MariaDB/server/commit/994026b77f)\
  2020-06-26 08:27:08 +0000
  * Cmake now ignores ColumnStore without an explicit -DDEB | -DRPM and -DPLUGIN\_COLUMNSTORE=YES or its analog.
* [Revision #65b93cef38](https://github.com/MariaDB/server/commit/65b93cef38)\
  2020-06-25 13:59:00 +0300
  * fix clang build
* [Revision #1247b36bad](https://github.com/MariaDB/server/commit/1247b36bad)\
  2020-06-24 15:33:30 +0530
  * [MDEV-22951](https://jira.mariadb.org/browse/MDEV-22951): rpl.rpl\_slave\_alias\_replica failed in buildbot with wrong result
* Merge [Revision #e1013725ce](https://github.com/MariaDB/server/commit/e1013725ce) 2020-06-24 14:34:06 +0200 - Merge branch 'github/10.5' into bb-10.5-release
* [Revision #23c53df4b7](https://github.com/MariaDB/server/commit/23c53df4b7)\
  2020-06-24 06:05:16 -0400
  * bump the VERSION
* [Revision #d1bb7f9143](https://github.com/MariaDB/server/commit/d1bb7f9143)\
  2020-06-24 12:51:55 +0300
  * Fixed memory leak in `item_sum.cc::report_cut_value_error()`
* [Revision #d09dd5e86c](https://github.com/MariaDB/server/commit/d09dd5e86c)\
  2020-02-11 15:35:51 -0800
  * Exclude needs to be on receiving side too
* [Revision #89c3b087a3](https://github.com/MariaDB/server/commit/89c3b087a3)\
  2020-02-11 10:27:59 -0800
  * [MDEV-21709](https://jira.mariadb.org/browse/MDEV-21709) ZFS snapdir=visible breaks Galera rsync SST replcation
* [Revision #dbe15e9e5a](https://github.com/MariaDB/server/commit/dbe15e9e5a)\
  2020-05-15 18:39:05 +0300
  * [MDEV-19749](https://jira.mariadb.org/browse/MDEV-19749) MDL scalability regression after backup locks
* [Revision #d712956526](https://github.com/MariaDB/server/commit/d712956526)\
  2020-05-13 01:45:54 +0300
  * [MDEV-19749](https://jira.mariadb.org/browse/MDEV-19749) MDL scalability regression after backup locks
* [Revision #e9c389c334](https://github.com/MariaDB/server/commit/e9c389c334)\
  2020-06-16 23:57:51 +0300
  * [MDEV-22701](https://jira.mariadb.org/browse/MDEV-22701) InnoDB: encapsulate trx\_sys.mutex and trx\_sys.trx\_list into a separate class
* [Revision #ead98fe5d3](https://github.com/MariaDB/server/commit/ead98fe5d3)\
  2020-06-22 23:40:56 +0530
  * Fixing a test
* [Revision #127ed74fd2](https://github.com/MariaDB/server/commit/127ed74fd2)\
  2020-06-05 16:41:25 +0300
  * [MDEV-22420](https://jira.mariadb.org/browse/MDEV-22420) DDL on temporary object is prohibited when XA is in prepare state
* [Revision #545a6194e8](https://github.com/MariaDB/server/commit/545a6194e8)\
  2020-06-22 19:48:46 +0530
  * [MDEV-22187](https://jira.mariadb.org/browse/MDEV-22187): SIGSEGV in `ha_innobase::cmp_ref` on DELETE
* [Revision #9160e4aa95](https://github.com/MariaDB/server/commit/9160e4aa95)\
  2020-06-19 22:04:02 +0300
  * Post-fix for 0a9633ee: Basic `LEX::print` function that supports UPDATEs
* [Revision #572e53d8cc](https://github.com/MariaDB/server/commit/572e53d8cc)\
  2020-06-19 15:24:16 +0530
  * [MDEV-22931](https://jira.mariadb.org/browse/MDEV-22931) `mtr_t::mtr_t()` allocates some memory
* [Revision #451bd32600](https://github.com/MariaDB/server/commit/451bd32600)\
  2020-06-17 14:18:02 +0200
  * [MDEV-22922](https://jira.mariadb.org/browse/MDEV-22922): galera\_ftwrl\_drain test failed

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
