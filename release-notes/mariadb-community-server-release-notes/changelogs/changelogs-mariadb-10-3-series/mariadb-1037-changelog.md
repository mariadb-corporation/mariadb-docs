# MariaDB 10.3.7 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/release-notes-mariadb-10-3-series/mariadb-10-3-39-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.7)[Release Notes](../../old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)[Changelog](mariadb-1037-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 25 May 2018

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #037df4189f](https://github.com/MariaDB/server/commit/037df4189f)\
  2018-05-22 15:56:09 +0200
  * promote the server to "stable"
* [Revision #82e9b49f54](https://github.com/MariaDB/server/commit/82e9b49f54)\
  2018-05-22 15:55:48 +0200
  * promote Spider to "stable"
* [Revision #2609783aac](https://github.com/MariaDB/server/commit/2609783aac)\
  2018-05-21 15:44:54 +0200
  * [MDEV-15627](https://jira.mariadb.org/browse/MDEV-15627) debian packages install /etc/mysql/mariadb.cnf however its not read by default
* [Revision #aa5683d12e](https://github.com/MariaDB/server/commit/aa5683d12e)\
  2018-05-17 09:33:04 +0300
  * [MDEV-15380](https://jira.mariadb.org/browse/MDEV-15380) Index for versioned table gets corrupt after partitioning and DELETE
* Merge [Revision #4ec8598c1d](https://github.com/MariaDB/server/commit/4ec8598c1d) 2018-05-22 11:47:09 +0200 - Merge branch 'github/10.2' into 10.3
* [Revision #afe5a51c2d](https://github.com/MariaDB/server/commit/afe5a51c2d)\
  2018-05-21 18:16:03 -0700
  * [MDEV-12900](https://jira.mariadb.org/browse/MDEV-12900): spider tests failed in buildbot with valgrind
* [Revision #31584c8bb8](https://github.com/MariaDB/server/commit/31584c8bb8)\
  2018-05-21 13:43:50 +0300
  * Set MyRocks plugin version to Stable
* [Revision #36043c58f5](https://github.com/MariaDB/server/commit/36043c58f5)\
  2018-05-20 20:26:40 +0200
  * .gitignore
* Merge [Revision #ff1d10ef9c](https://github.com/MariaDB/server/commit/ff1d10ef9c) 2018-05-20 02:07:21 +0200 - Merge branch '10.1' into 10.2
* Merge [Revision #91dfb6141f](https://github.com/MariaDB/server/commit/91dfb6141f) 2018-05-19 16:30:36 +0200 - Merge branch '10.0' into 10.1
* Merge [Revision #c1b5d2801e](https://github.com/MariaDB/server/commit/c1b5d2801e) 2018-05-19 15:38:34 +0200 - Merge branch '5.5' into 10.0
* [Revision #27a7365f42](https://github.com/MariaDB/server/commit/27a7365f42)\
  2018-05-18 00:23:15 +0100
  * [MDEV-16220](https://jira.mariadb.org/browse/MDEV-16220) MTR - do not pass UTF8 on the command line for mysql client.
* [Revision #1b2078b4d8](https://github.com/MariaDB/server/commit/1b2078b4d8)\
  2018-05-15 17:34:47 +0200
  * [MDEV-15318](https://jira.mariadb.org/browse/MDEV-15318) CREATE .. SELECT VALUES produces invalid table structure
* [Revision #aa2e1ade17](https://github.com/MariaDB/server/commit/aa2e1ade17)\
  2018-05-16 21:01:26 +0400
  * (almost) sane core handling in mtr
* [Revision #2b749a7bf4](https://github.com/MariaDB/server/commit/2b749a7bf4)\
  2018-05-15 11:46:55 +0300
  * [MDEV-654](https://jira.mariadb.org/browse/MDEV-654) Assertion \`share->now\_transactional' failed in flush\_log\_for\_bitmap on concurrent workload with Aria tables
* [Revision #cf5226174b](https://github.com/MariaDB/server/commit/cf5226174b)\
  2018-05-19 15:34:17 +0200
  * [MDEV-11129](https://jira.mariadb.org/browse/MDEV-11129) CREATE OR REPLACE TABLE t1 AS SELECT spfunc() crashes if spfunc() references t1
* [Revision #ef295c31e3](https://github.com/MariaDB/server/commit/ef295c31e3)\
  2018-05-16 21:51:46 +0300
  * [MDEV-11129](https://jira.mariadb.org/browse/MDEV-11129) CREATE OR REPLACE TABLE t1 AS SELECT spfunc() crashes if spfunc() references t1
* [Revision #d703e09cd6](https://github.com/MariaDB/server/commit/d703e09cd6)\
  2017-09-21 16:30:24 +0300
  * Fix that FLUSH TABLES FOR EXPORT also works for Aria tables.
* [Revision #b050df4fd3](https://github.com/MariaDB/server/commit/b050df4fd3)\
  2018-05-15 12:30:32 +0300
  * [MDEV-14943](https://jira.mariadb.org/browse/MDEV-14943) Alter table ORDER BY bug
* [Revision #f76a17e355](https://github.com/MariaDB/server/commit/f76a17e355)\
  2018-05-18 11:14:26 -0700
  * [MDEV-7914](https://jira.mariadb.org/browse/MDEV-7914): spider/bg.ha, spider/bg.ha\_part crash server sporadically in buildbot
* [Revision #0bd2b80254](https://github.com/MariaDB/server/commit/0bd2b80254)\
  2018-05-07 17:42:55 +0200
  * [MDEV-15347](https://jira.mariadb.org/browse/MDEV-15347): Valgrind or ASAN errors in mysql\_make\_view on query from information\_schema
* [Revision #6f530c63cd](https://github.com/MariaDB/server/commit/6f530c63cd)\
  2018-05-19 09:06:04 +0200
  * cleanup: specify memroot explicitly in `new Explain_xxx`
* [Revision #1cc67e090e](https://github.com/MariaDB/server/commit/1cc67e090e)\
  2018-05-18 19:12:35 +0200
  * [MDEV-16153](https://jira.mariadb.org/browse/MDEV-16153) Server crashes in Apc\_target::disable, ASAN heap-use-after-free in Explain\_query::Explain\_query upon/after EXECUTE IMMEDIATE
* [Revision #207e5ba316](https://github.com/MariaDB/server/commit/207e5ba316)\
  2018-05-19 17:04:47 +0000
  * mariadb-backup : Fix race condition when killing query waiting for MDL
* [Revision #dd51082eca](https://github.com/MariaDB/server/commit/dd51082eca)\
  2018-05-19 00:26:35 +0300
  * [MDEV-12465](https://jira.mariadb.org/browse/MDEV-12465): Server crashes in my\_scan\_weight\_utf8\_bin upon collecting stats for RocksDB table
* [Revision #06aaaef51a](https://github.com/MariaDB/server/commit/06aaaef51a)\
  2018-05-18 23:58:24 +0300
  * [MDEV-16200](https://jira.mariadb.org/browse/MDEV-16200): -DPLUGIN\_ROCKSDB=YES leads to errors during build
* [Revision #727d0d4f9b](https://github.com/MariaDB/server/commit/727d0d4f9b)\
  2018-05-18 17:26:12 +0300
  * [MDEV-15304](https://jira.mariadb.org/browse/MDEV-15304): Server crash in print\_keydup\_error / key\_unpack or unexpected ER\_DUP\_KEY
* [Revision #de86997160](https://github.com/MariaDB/server/commit/de86997160)\
  2018-05-17 22:56:27 -0700
  * [MDEV-15581](https://jira.mariadb.org/browse/MDEV-15581) Incorrect result (missing row) with UNION DISTINCT in anchor parts
* [Revision #52c98bf830](https://github.com/MariaDB/server/commit/52c98bf830)\
  2018-05-18 00:35:59 -0400
  * bump the VERSION
* [Revision #d309c2fc88](https://github.com/MariaDB/server/commit/d309c2fc88)\
  2018-05-17 15:47:17 -0700
  * [MDEV-16212](https://jira.mariadb.org/browse/MDEV-16212) Memory leak with recursive CTE that uses global ORDER BY with recursive subquery
* [Revision #ab9d420df3](https://github.com/MariaDB/server/commit/ab9d420df3)\
  2018-05-17 11:21:13 -0700
  * [MDEV-7914](https://jira.mariadb.org/browse/MDEV-7914): spider/bg.ha, spider/bg.ha\_part crash server sporadically in buildbot
* Merge [Revision #50275321c3](https://github.com/MariaDB/server/commit/50275321c3) 2018-05-17 11:25:35 +0200 - Merge branch '10.2' into bb-10.2-release
* [Revision #fe3bf136b6](https://github.com/MariaDB/server/commit/fe3bf136b6)\
  2018-05-22 08:34:10 +0400
  * A cleanup for [MDEV-15818](https://jira.mariadb.org/browse/MDEV-15818) Fix shift-reduce conflicts in the new 10.3 syntax
* Merge [Revision #b9cf26f726](https://github.com/MariaDB/server/commit/b9cf26f726) 2018-05-21 17:49:52 -0700 - [MDEV-12900](https://jira.mariadb.org/browse/MDEV-12900): spider tests failed in buildbot with valgrind
* [Revision #4d576d9dac](https://github.com/MariaDB/server/commit/4d576d9dac)\
  2018-05-21 17:30:39 -0700
  * [MDEV-12900](https://jira.mariadb.org/browse/MDEV-12900): spider tests failed in buildbot with valgrind
* Merge [Revision #ff1af15f6d](https://github.com/MariaDB/server/commit/ff1af15f6d) 2018-05-21 16:34:45 +0000 - Merge branch '10.3' into bb-10.3-cc
* Merge [Revision #e1e6d37515](https://github.com/MariaDB/server/commit/e1e6d37515) 2018-05-21 16:17:05 +0000 - Merge branch 'bb-10.3-cc' into 10.3
* [Revision #3400430b93](https://github.com/MariaDB/server/commit/3400430b93)\
  2018-05-20 14:04:38 +0400
  * OS X warnings fixes
* [Revision #cbeb2b306d](https://github.com/MariaDB/server/commit/cbeb2b306d)\
  2018-05-20 13:45:29 +0400
  * Better crash reports on OS X
* [Revision #912a75d428](https://github.com/MariaDB/server/commit/912a75d428)\
  2018-05-20 11:05:14 +0400
  * Added support for lldb core analysis in mtr
* [Revision #a5fb0fa329](https://github.com/MariaDB/server/commit/a5fb0fa329)\
  2018-05-19 10:07:21 +0200
  * bugfix: EE\_OPEN\_WARNING could be statistically wrong
* [Revision #59785df59f](https://github.com/MariaDB/server/commit/59785df59f)\
  2018-03-14 15:33:47 +1100
  * [MDEV-15635](https://jira.mariadb.org/browse/MDEV-15635) mysys: THR\_LOCK\_open reduce usage
* [Revision #20fadaac99](https://github.com/MariaDB/server/commit/20fadaac99)\
  2018-03-02 10:19:43 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): use mkostemp when available with O\_CLOEXEC
* [Revision #f56d141778](https://github.com/MariaDB/server/commit/f56d141778)\
  2018-05-18 10:28:53 +0200
  * cleanup: report\_error() in sql\_plugin.cc
* [Revision #44b7f5f3ab](https://github.com/MariaDB/server/commit/44b7f5f3ab)\
  2018-05-17 22:53:57 +0200
  * cleanup: create\_temp\_file()
* [Revision #7e45b7ac1f](https://github.com/MariaDB/server/commit/7e45b7ac1f)\
  2018-03-15 15:48:26 +1100
  * [MDEV-15583](https://jira.mariadb.org/browse/MDEV-15583) create\_temp\_file: remove tempnam implementation
* [Revision #d7a047c4c9](https://github.com/MariaDB/server/commit/d7a047c4c9)\
  2018-03-01 16:25:36 +0800
  * [MDEV-15550](https://jira.mariadb.org/browse/MDEV-15550) Add error handling for fopen
* [Revision #b5a6f823a6](https://github.com/MariaDB/server/commit/b5a6f823a6)\
  2018-02-17 00:39:26 +0600
  * [MDEV-15513](https://jira.mariadb.org/browse/MDEV-15513) use EVP\_MD\_CTX\_{new,free} instead of EVP\_MD\_CTX\_{create, destroy}
* [Revision #44d00fba43](https://github.com/MariaDB/server/commit/44d00fba43)\
  2018-05-21 13:26:16 +0400
  * Addressing Monty's review suggestions for [MDEV-11952](https://jira.mariadb.org/browse/MDEV-11952) Oracle-style packages (partial)
* [Revision #cc231c9f1e](https://github.com/MariaDB/server/commit/cc231c9f1e)\
  2018-05-21 10:16:13 +0400
  * A cleanup for 2a33d248e0bd910ec10a2bb68e47f17b47e3a980
* [Revision #d69cc7301b](https://github.com/MariaDB/server/commit/d69cc7301b)\
  2018-05-21 09:47:53 +0400
  * Cleanup: fixing shift-reduce conflicts in expr/bool\_pri/predicate
* [Revision #7ad9b3588f](https://github.com/MariaDB/server/commit/7ad9b3588f)\
  2018-05-20 14:04:38 +0400
  * OS X warnings fixes
* [Revision #c8e5026958](https://github.com/MariaDB/server/commit/c8e5026958)\
  2018-05-20 13:45:29 +0400
  * Better crash reports on OS X
* [Revision #646385c9fd](https://github.com/MariaDB/server/commit/646385c9fd)\
  2018-05-20 11:05:14 +0400
  * Added support for lldb core analysis in mtr
* [Revision #8f47c65867](https://github.com/MariaDB/server/commit/8f47c65867)\
  2018-05-19 10:07:21 +0200
  * bugfix: EE\_OPEN\_WARNING could be statistically wrong
* [Revision #0322ced7e5](https://github.com/MariaDB/server/commit/0322ced7e5)\
  2018-03-14 15:33:47 +1100
  * [MDEV-15635](https://jira.mariadb.org/browse/MDEV-15635) mysys: THR\_LOCK\_open reduce usage
* [Revision #6ed6a0454c](https://github.com/MariaDB/server/commit/6ed6a0454c)\
  2018-03-02 10:19:43 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): use mkostemp when available with O\_CLOEXEC
* [Revision #d974726867](https://github.com/MariaDB/server/commit/d974726867)\
  2018-05-18 10:28:53 +0200
  * cleanup: report\_error() in sql\_plugin.cc
* [Revision #ff1ec6e958](https://github.com/MariaDB/server/commit/ff1ec6e958)\
  2018-05-17 22:53:57 +0200
  * cleanup: create\_temp\_file()
* [Revision #3537267db3](https://github.com/MariaDB/server/commit/3537267db3)\
  2018-03-15 15:48:26 +1100
  * [MDEV-15583](https://jira.mariadb.org/browse/MDEV-15583) create\_temp\_file: remove tempnam implementation
* [Revision #f428a12342](https://github.com/MariaDB/server/commit/f428a12342)\
  2018-03-01 16:25:36 +0800
  * [MDEV-15550](https://jira.mariadb.org/browse/MDEV-15550) Add error handling for fopen
* [Revision #d218b5c33a](https://github.com/MariaDB/server/commit/d218b5c33a)\
  2018-02-17 00:39:26 +0600
  * [MDEV-15513](https://jira.mariadb.org/browse/MDEV-15513) use EVP\_MD\_CTX\_{new,free} instead of EVP\_MD\_CTX\_{create, destroy}
* [Revision #1e69d3f196](https://github.com/MariaDB/server/commit/1e69d3f196)\
  2018-05-21 13:26:16 +0400
  * Addressing Monty's review suggestions for [MDEV-11952](https://jira.mariadb.org/browse/MDEV-11952) Oracle-style packages (partial)
* [Revision #7d91d98ac1](https://github.com/MariaDB/server/commit/7d91d98ac1)\
  2018-05-21 10:16:13 +0400
  * A cleanup for 2a33d248e0bd910ec10a2bb68e47f17b47e3a980
* [Revision #b73083c57a](https://github.com/MariaDB/server/commit/b73083c57a)\
  2018-05-21 09:47:53 +0400
  * Cleanup: fixing shift-reduce conflicts in expr/bool\_pri/predicate
* [Revision #508373d500](https://github.com/MariaDB/server/commit/508373d500)\
  2018-05-20 14:04:38 +0400
  * OS X warnings fixes
* [Revision #8c55277dcb](https://github.com/MariaDB/server/commit/8c55277dcb)\
  2018-05-20 13:45:29 +0400
  * Better crash reports on OS X
* [Revision #9692f37d29](https://github.com/MariaDB/server/commit/9692f37d29)\
  2018-05-20 11:05:14 +0400
  * Added support for lldb core analysis in mtr
* [Revision #a1d57ca1ab](https://github.com/MariaDB/server/commit/a1d57ca1ab)\
  2018-05-19 10:07:21 +0200
  * bugfix: EE\_OPEN\_WARNING could be statistically wrong
* [Revision #5c81cb880a](https://github.com/MariaDB/server/commit/5c81cb880a)\
  2018-03-14 15:33:47 +1100
  * [MDEV-15635](https://jira.mariadb.org/browse/MDEV-15635) mysys: THR\_LOCK\_open reduce usage
* [Revision #f165077aa9](https://github.com/MariaDB/server/commit/f165077aa9)\
  2018-03-02 10:19:43 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): use mkostemp when available with O\_CLOEXEC
* [Revision #d5db2f1084](https://github.com/MariaDB/server/commit/d5db2f1084)\
  2018-05-18 10:28:53 +0200
  * cleanup: report\_error() in sql\_plugin.cc
* [Revision #3a7d7e180a](https://github.com/MariaDB/server/commit/3a7d7e180a)\
  2018-05-17 22:53:57 +0200
  * cleanup: create\_temp\_file()
* [Revision #2534ae20fd](https://github.com/MariaDB/server/commit/2534ae20fd)\
  2018-03-15 15:48:26 +1100
  * [MDEV-15583](https://jira.mariadb.org/browse/MDEV-15583) create\_temp\_file: remove tempnam implementation
* [Revision #8307fb23bd](https://github.com/MariaDB/server/commit/8307fb23bd)\
  2018-03-01 16:25:36 +0800
  * [MDEV-15550](https://jira.mariadb.org/browse/MDEV-15550) Add error handling for fopen
* [Revision #00eb5bf3bb](https://github.com/MariaDB/server/commit/00eb5bf3bb)\
  2018-02-17 00:39:26 +0600
  * [MDEV-15513](https://jira.mariadb.org/browse/MDEV-15513) use EVP\_MD\_CTX\_{new,free} instead of EVP\_MD\_CTX\_{create, destroy}
* [Revision #f51e5e4557](https://github.com/MariaDB/server/commit/f51e5e4557)\
  2018-05-21 10:32:39 +0000
  * update C/C
* [Revision #798ba1ed51](https://github.com/MariaDB/server/commit/798ba1ed51)\
  2018-05-19 23:15:34 +0000
  * update C/C
* [Revision #d31c2416dd](https://github.com/MariaDB/server/commit/d31c2416dd)\
  2018-05-19 23:37:16 +0400
  * Updated libmariadb: fixed connect failure on OS X
* [Revision #62289c7948](https://github.com/MariaDB/server/commit/62289c7948)\
  2018-05-19 18:52:08 +0000
  * update C/C
* Merge [Revision #3a50a13071](https://github.com/MariaDB/server/commit/3a50a13071) 2018-05-19 15:56:44 +0000 - Merge remote-tracking branch 'origin/10.3' into bb-10.3-cc
* [Revision #e4e0aea644](https://github.com/MariaDB/server/commit/e4e0aea644)\
  2018-05-19 14:23:06 +0300
  * Follow-up for be6ae0bb6baa8a - fix test results
* [Revision #36779e624d](https://github.com/MariaDB/server/commit/36779e624d)\
  2018-05-18 17:42:12 +0530
  * [MDEV-14623](https://jira.mariadb.org/browse/MDEV-14623): Output of show function code does not show FETCH GROUP NEXT ROW for custom aggregates
* [Revision #89b1c2712a](https://github.com/MariaDB/server/commit/89b1c2712a)\
  2018-05-17 17:19:33 +0530
  * [MDEV-14520](https://jira.mariadb.org/browse/MDEV-14520): Custom aggregate functions work incorrectly with WITH ROLLUP clause
* Merge [Revision #0d4df3cd13](https://github.com/MariaDB/server/commit/0d4df3cd13) 2018-05-19 15:44:31 +0000 - Merge branch '10.3' into bb-10.3-cc
* [Revision #7bf4a006b3](https://github.com/MariaDB/server/commit/7bf4a006b3)\
  2018-05-18 22:43:44 +0000
  * Revert "update C/C (now, using 10.3-server branch for 10.3)"
* [Revision #a620985f8f](https://github.com/MariaDB/server/commit/a620985f8f)\
  2018-05-18 20:32:57 +0300
  * [MDEV-15373](https://jira.mariadb.org/browse/MDEV-15373) post-push: fixing type mismatch alerted by windows build.
* [Revision #4cc7f96512](https://github.com/MariaDB/server/commit/4cc7f96512)\
  2018-05-19 15:14:24 +0000
  * support older cmake versions in C/C
* [Revision #0040e2932d](https://github.com/MariaDB/server/commit/0040e2932d)\
  2018-05-19 15:13:53 +0000
  * pipe and shared memory protocol should be statically compiled into C/C
* [Revision #4a9acaa524](https://github.com/MariaDB/server/commit/4a9acaa524)\
  2018-05-19 12:44:15 +0000
  * adjust MTR code after C/C changed the location of plugin libraries
* [Revision #ae77a0986d](https://github.com/MariaDB/server/commit/ae77a0986d)\
  2018-05-19 12:36:43 +0000
  * try using C/C as base for 10.3-server
* [Revision #685961a085](https://github.com/MariaDB/server/commit/685961a085)\
  2018-05-18 16:30:32 +0100
  * update C/C (now, using 10.3-server branch for 10.3)
* [Revision #9df656db65](https://github.com/MariaDB/server/commit/9df656db65)\
  2018-05-08 22:17:18 +0300
  * [MDEV-15373](https://jira.mariadb.org/browse/MDEV-15373) engine gtid\_slave\_pos table name disobeys lower-case-table-names
* [Revision #2a33d248e0](https://github.com/MariaDB/server/commit/2a33d248e0)\
  2018-05-18 15:48:25 +0400
  * [MDEV-15975](https://jira.mariadb.org/browse/MDEV-15975) PL/SQL parser does not understand historical queries
* [Revision #395c8ca708](https://github.com/MariaDB/server/commit/395c8ca708)\
  2018-05-15 14:01:24 +0530
  * [MDEV-14853](https://jira.mariadb.org/browse/MDEV-14853) Grant does not work correctly when table contains... SYSTEM\_INVISIBLE or COMPLETELY\_INVISIBLE
* [Revision #ff0e9b2fce](https://github.com/MariaDB/server/commit/ff0e9b2fce)\
  2018-05-18 06:51:21 +0400
  * Adding "SET sql\_mode=ORACLE" forgotten in fdcc95143de96ce12b5c0c84e07f4c7541260ba5
* [Revision #fdcc95143d](https://github.com/MariaDB/server/commit/fdcc95143d)\
  2018-05-18 06:47:54 +0400
  * sql\_yacc\_ora.yy: mering [MDEV-13384](https://jira.mariadb.org/browse/MDEV-13384) "window" seems like a reserved column name but it's not listed as one
* [Revision #023c789a55](https://github.com/MariaDB/server/commit/023c789a55)\
  2018-05-17 21:47:53 +0400
  * [MDEV-15818](https://jira.mariadb.org/browse/MDEV-15818) Fix shift-reduce conflicts in the new 10.3 syntax
* [Revision #f38d8c1701](https://github.com/MariaDB/server/commit/f38d8c1701)\
  2018-05-17 22:03:53 +0530
  * [MDEV-16201](https://jira.mariadb.org/browse/MDEV-16201) CREATE TABLE creates extra transaction
* Merge [Revision #15425767e8](https://github.com/MariaDB/server/commit/15425767e8) 2018-05-17 15:48:50 +0200 - Merge remote-tracking branch 'github/10.3' into 10.3
* [Revision #50d71c8b37](https://github.com/MariaDB/server/commit/50d71c8b37)\
  2018-05-17 16:25:09 +0400
  * Cleanup: moving keyword comments such as SQL-2003-R from rules to %token commands
* [Revision #b2f56085d4](https://github.com/MariaDB/server/commit/b2f56085d4)\
  2018-05-17 15:16:55 +0300
  * [MDEV-16045](https://jira.mariadb.org/browse/MDEV-16045): Fix a heap allocation
* [Revision #10d44db5d4](https://github.com/MariaDB/server/commit/10d44db5d4)\
  2018-05-17 16:01:20 +0400
  * [MDEV-16202](https://jira.mariadb.org/browse/MDEV-16202) Latest changes made erroneously some keywords reserved in sql\_mode=ORACLE
* [Revision #21b12e3359](https://github.com/MariaDB/server/commit/21b12e3359)\
  2018-05-17 09:37:22 +0300
  * [MDEV-16172](https://jira.mariadb.org/browse/MDEV-16172): Disable failing rpl tests
* [Revision #66afb5ecb7](https://github.com/MariaDB/server/commit/66afb5ecb7)\
  2018-05-17 09:35:35 +0300
  * [MDEV-16172](https://jira.mariadb.org/browse/MDEV-16172): Enable skipped tests
* Merge [Revision #4c7608aeb1](https://github.com/MariaDB/server/commit/4c7608aeb1) 2018-05-17 08:42:53 +0300 - Merge 10.2 into 10.3
* [Revision #a4e7800701](https://github.com/MariaDB/server/commit/a4e7800701)\
  2018-05-16 16:35:33 +0300
  * [MDEV-13779](https://jira.mariadb.org/browse/MDEV-13779) InnoDB fails to shut down purge workers, causing hang
* [Revision #21eccff625](https://github.com/MariaDB/server/commit/21eccff625)\
  2018-04-25 17:13:20 +0300
  * [MDEV-15979](https://jira.mariadb.org/browse/MDEV-15979) DELETE HISTORY from a table with transaction-precise versioning causes Assertion \`table\_list->vers\_conditions.type == SYSTEM\_TIME\_BEFORE' failure
* [Revision #60319afff7](https://github.com/MariaDB/server/commit/60319afff7)\
  2018-05-07 14:36:52 +0300
  * [MDEV-15969](https://jira.mariadb.org/browse/MDEV-15969) System versioning and FEDERATED don't work well together: DML and discovery fail
* [Revision #dfd6702a29](https://github.com/MariaDB/server/commit/dfd6702a29)\
  2018-05-14 10:47:13 +0200
  * [MDEV-16157](https://jira.mariadb.org/browse/MDEV-16157) federated corrupts timestamps
* [Revision #28dbdf3d79](https://github.com/MariaDB/server/commit/28dbdf3d79)\
  2018-04-04 15:34:40 +0200
  * [MDEV-14551](https://jira.mariadb.org/browse/MDEV-14551) Can't find record in table on multi-table update with ORDER BY
* [Revision #e17e798599](https://github.com/MariaDB/server/commit/e17e798599)\
  2018-04-10 11:33:47 +0200
  * cleanup: simplify multi-update's juggling with positions
* [Revision #c368878fac](https://github.com/MariaDB/server/commit/c368878fac)\
  2018-04-10 14:08:14 +0200
  * cleanup: comments and whitespaces
* [Revision #4b061ec4ea](https://github.com/MariaDB/server/commit/4b061ec4ea)\
  2018-04-09 22:54:32 +0200
  * bugfix: correct list assignment operator
* [Revision #c2352c45fb](https://github.com/MariaDB/server/commit/c2352c45fb)\
  2018-05-16 10:31:13 +0300
  * [MDEV-14669](https://jira.mariadb.org/browse/MDEV-14669) Assertion \`file->trn == trn' failed in ha\_maria::start\_stmt
* [Revision #48d7038861](https://github.com/MariaDB/server/commit/48d7038861)\
  2018-05-16 21:58:28 +0400
  * Token precedence cleanup in \*.yy
* [Revision #c2df4e9d62](https://github.com/MariaDB/server/commit/c2df4e9d62)\
  2018-05-16 17:21:31 +0400
  * [MDEV-16186](https://jira.mariadb.org/browse/MDEV-16186) Concatenation operator || returns wrong results in sql\_mode=ORACLE
* [Revision #66360506f0](https://github.com/MariaDB/server/commit/66360506f0)\
  2018-05-16 10:15:31 +0300
  * [MDEV-16168](https://jira.mariadb.org/browse/MDEV-16168): Resurrect the record MLOG\_UNDO\_INIT
* [Revision #a639eff594](https://github.com/MariaDB/server/commit/a639eff594)\
  2018-05-16 09:44:22 +0400
  * [MDEV-15813](https://jira.mariadb.org/browse/MDEV-15813) ASAN use-after-poison in hp\_hashnr upon HANDLER READ on a versioned HEAP table.
* [Revision #cd15e764a8](https://github.com/MariaDB/server/commit/cd15e764a8)\
  2018-05-15 14:39:50 +0300
  * [MDEV-16159](https://jira.mariadb.org/browse/MDEV-16159) Use atomic memory access for purge\_sys
* [Revision #442a6e6b25](https://github.com/MariaDB/server/commit/442a6e6b25)\
  2018-05-15 08:57:21 +0300
  * [MDEV-16172](https://jira.mariadb.org/browse/MDEV-16172) Remove InnoDB 5.7 version number from [MariaDB 10.3](../../old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md) onwards
* [Revision #27f12c5d5b](https://github.com/MariaDB/server/commit/27f12c5d5b)\
  2018-05-15 22:48:40 +0300
  * [MDEV-16143](https://jira.mariadb.org/browse/MDEV-16143) Assertion failure in rec\_offs\_get\_n\_alloc() due to row\_trx\_id\_offset()
* [Revision #93b69825ad](https://github.com/MariaDB/server/commit/93b69825ad)\
  2018-05-15 13:47:28 +0300
  * [MDEV-16169](https://jira.mariadb.org/browse/MDEV-16169) InnoDB: Failing assertion: !space->referenced()
* [Revision #2b812abd1a](https://github.com/MariaDB/server/commit/2b812abd1a)\
  2018-05-15 12:53:48 +0300
  * Correct a comment
* [Revision #dd0e960f4d](https://github.com/MariaDB/server/commit/dd0e960f4d)\
  2018-05-15 19:52:28 +0200
  * Fix of the test after null processing fix.
* [Revision #2e0c23d82b](https://github.com/MariaDB/server/commit/2e0c23d82b)\
  2018-05-15 18:04:01 +0400
  * Removing redundant "%left INTERVAL\_SYM" and "%prec INTERVAL\_SYM"
* [Revision #06f539dab5](https://github.com/MariaDB/server/commit/06f539dab5)\
  2018-05-15 17:17:09 +0300
  * Revert the following patch brought in by "Merge pull request #753 from shinnok/10.3-macfixes"
* [Revision #0dd1ebcb27](https://github.com/MariaDB/server/commit/0dd1ebcb27)\
  2018-05-09 13:39:13 +0200
  * [MDEV-15576](https://jira.mariadb.org/browse/MDEV-15576): Server crashed in Cached\_item\_str::cmp / sortcmp or Assertion \`item->null\_value' failed in Type\_handler\_temporal\_result::make\_sort\_key upon SELECT with NULLIF and ROLLUP
* [Revision #8a9048bcf3](https://github.com/MariaDB/server/commit/8a9048bcf3)\
  2018-05-15 13:38:01 +0300
  * [MDEV-16170](https://jira.mariadb.org/browse/MDEV-16170) Server crashes in Item\_null\_result::type\_handler on SELECT with ROLLUP
* [Revision #e7fc8cd683](https://github.com/MariaDB/server/commit/e7fc8cd683)\
  2018-05-14 15:27:52 +0300
  * [MDEV-654](https://jira.mariadb.org/browse/MDEV-654) Assertion \`share->now\_transactional' failed in flush\_log\_for\_bitmap on concurrent workload with Aria tables
* [Revision #e06c029849](https://github.com/MariaDB/server/commit/e06c029849)\
  2018-05-15 14:10:19 +0400
  * [MDEV-15465](https://jira.mariadb.org/browse/MDEV-15465) Server crash or ASAN heap-use-after-free in Item\_func\_match::cleanup upon using FT search with partitioning.
* Merge [Revision #a0048378f9](https://github.com/MariaDB/server/commit/a0048378f9) 2018-05-15 12:20:16 +0300 - Merge pull request #753 from shinnok/10.3-macfixes
* [Revision #6620fbd62a](https://github.com/MariaDB/server/commit/6620fbd62a)\
  2018-05-10 12:23:35 +0300
  * [MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): On macOS pthread\_t is opaque, requires explicit cast
* [Revision #70e88b5089](https://github.com/MariaDB/server/commit/70e88b5089)\
  2018-05-10 12:21:37 +0300
  * [MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Rocksdb missing linkage to dbug library
* [Revision #9ee5406e2f](https://github.com/MariaDB/server/commit/9ee5406e2f)\
  2018-04-26 16:49:27 +0530
  * [MDEV-15965](https://jira.mariadb.org/browse/MDEV-15965) Invisible columns and LOAD DATA don't work well together:... ER\_WARN\_TOO\_FEW\_RECORDS
* [Revision #46be31982a](https://github.com/MariaDB/server/commit/46be31982a)\
  2018-05-15 09:33:29 +0400
  * [MDEV-16094](https://jira.mariadb.org/browse/MDEV-16094) Crash when using AS OF with a stored function [MDEV-16100](https://jira.mariadb.org/browse/MDEV-16100) FOR SYSTEM\_TIME erroneously resolves string user variables as transaction IDs
* [Revision #1b45ede6ab](https://github.com/MariaDB/server/commit/1b45ede6ab)\
  2018-05-14 19:00:25 -0700
  * Adjusted test results after [MDEV-15159](https://jira.mariadb.org/browse/MDEV-15159).
* Merge [Revision #86f9932e80](https://github.com/MariaDB/server/commit/86f9932e80) 2018-05-14 15:12:40 -0700 - [MDEV-16101](https://jira.mariadb.org/browse/MDEV-16101): ADD PARTITION on table partitioned by list does not work with more than 32 list values.
* [Revision #8e01598620](https://github.com/MariaDB/server/commit/8e01598620)\
  2018-05-11 14:45:09 -0700
  * [MDEV-16101](https://jira.mariadb.org/browse/MDEV-16101): ADD PARTITION on table partitioned by list does not work with more than 32 list values.
* [Revision #e74181e3c2](https://github.com/MariaDB/server/commit/e74181e3c2)\
  2018-05-14 14:38:17 -0700
  * [MDEV-15159](https://jira.mariadb.org/browse/MDEV-15159) NULL is treated as 0 in CTE
* [Revision #4a5e23e257](https://github.com/MariaDB/server/commit/4a5e23e257)\
  2018-05-14 11:36:22 +0400
  * [MDEV-16152](https://jira.mariadb.org/browse/MDEV-16152) Expressions with INTERVAL return bad results in some cases
* [Revision #1cb4caa66d](https://github.com/MariaDB/server/commit/1cb4caa66d)\
  2018-05-11 14:14:33 +0300
  * [MDEV-15970](https://jira.mariadb.org/browse/MDEV-15970) Crash when doing truncate on locked sequence
* [Revision #be6ae0bb6b](https://github.com/MariaDB/server/commit/be6ae0bb6b)\
  2018-05-11 17:33:40 +0300
  * Don't report errors from open\_table() twice
* [Revision #d853042b5f](https://github.com/MariaDB/server/commit/d853042b5f)\
  2018-05-09 06:39:38 +0300
  * Added missing write\_unlock() in case of errors
* Merge [Revision #15419a5583](https://github.com/MariaDB/server/commit/15419a5583) 2018-05-12 22:14:59 +0300 - Merge 10.2 into 10.3
* [Revision #5e84ea9634](https://github.com/MariaDB/server/commit/5e84ea9634)\
  2018-05-12 10:11:38 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Remove dict\_table\_is\_discarded()
* [Revision #c57e9835ff](https://github.com/MariaDB/server/commit/c57e9835ff)\
  2018-05-12 09:42:53 +0300
  * Replace dict\_col\_is\_virtual(col) with col->is\_virtual()
* [Revision #ba43914ec4](https://github.com/MariaDB/server/commit/ba43914ec4)\
  2018-05-12 09:38:46 +0300
  * Replace dict\_table\_is\_temporary(table) with table->is\_temporary()
* [Revision #edaf57e966](https://github.com/MariaDB/server/commit/edaf57e966)\
  2018-05-12 10:14:03 +0200
  * disable galera.pxc-421 test
* [Revision #f08b8fd58d](https://github.com/MariaDB/server/commit/f08b8fd58d)\
  2018-04-27 18:09:05 +0300
  * [MDEV-15980](https://jira.mariadb.org/browse/MDEV-15980) FOR SYSTEM\_TIME BETWEEN and FROM .. TO work with negative intervals
* [Revision #b1e75d290e](https://github.com/MariaDB/server/commit/b1e75d290e)\
  2018-04-24 12:10:52 +0300
  * [MDEV-14823](https://jira.mariadb.org/browse/MDEV-14823), [MDEV-15956](https://jira.mariadb.org/browse/MDEV-15956) Versioning error messages fixes
* [Revision #ce2cf855bf](https://github.com/MariaDB/server/commit/ce2cf855bf)\
  2018-04-28 14:18:02 +0300
  * [MDEV-16043](https://jira.mariadb.org/browse/MDEV-16043) Assertion thd->Item\_change\_list::is\_empty() failed in mysql\_parse upon SELECT from a view reading from a versioned table
* [Revision #8b2fa0ab25](https://github.com/MariaDB/server/commit/8b2fa0ab25)\
  2018-05-09 13:40:27 +0200
  * remove obsolete rdiff
* [Revision #68cad6aa24](https://github.com/MariaDB/server/commit/68cad6aa24)\
  2018-04-25 23:33:08 +0300
  * [MDEV-16024](https://jira.mariadb.org/browse/MDEV-16024) transaction\_registry.begin\_timestamp is wrong for explicit transactions
* [Revision #fd4153f083](https://github.com/MariaDB/server/commit/fd4153f083)\
  2018-04-28 17:02:00 +0300
  * [MDEV-16010](https://jira.mariadb.org/browse/MDEV-16010) Too many rows with AS OF point\_in\_the\_past\_or\_NULL
* [Revision #fddaaf7295](https://github.com/MariaDB/server/commit/fddaaf7295)\
  2018-04-28 20:40:34 +0300
  * [MDEV-15978](https://jira.mariadb.org/browse/MDEV-15978) Add Feature\_system\_versioning status variable
* [Revision #da25860d4a](https://github.com/MariaDB/server/commit/da25860d4a)\
  2018-04-27 19:23:17 +0300
  * [MDEV-15995](https://jira.mariadb.org/browse/MDEV-15995) Drop extra semicolon in VARIABLE\_COMMENT for SYSTEM\_VERSIONING\_ALTER\_HISTORY
* [Revision #fe10bf870c](https://github.com/MariaDB/server/commit/fe10bf870c)\
  2018-04-17 09:53:44 +0300
  * [MDEV-15893](https://jira.mariadb.org/browse/MDEV-15893) Rename VTQ to TRT
* [Revision #a4272bf154](https://github.com/MariaDB/server/commit/a4272bf154)\
  2018-05-02 21:53:12 +0200
  * versioning: use @@timestamp
* [Revision #4203f572ae](https://github.com/MariaDB/server/commit/4203f572ae)\
  2018-05-02 17:55:00 +0200
  * [MDEV-15923](https://jira.mariadb.org/browse/MDEV-15923) option to control who can set session @@timestamp
* [Revision #bbf5cf4ddf](https://github.com/MariaDB/server/commit/bbf5cf4ddf)\
  2018-05-02 15:16:22 +0200
  * cleanup: sys\_vars.cc
* [Revision #735203e6de](https://github.com/MariaDB/server/commit/735203e6de)\
  2018-05-02 15:45:51 +0200
  * cleanup: quoted\_string
* [Revision #47573cee4d](https://github.com/MariaDB/server/commit/47573cee4d)\
  2018-05-02 20:57:22 +0200
  * cleanup: include/have\_rbr\_triggers.inc
* [Revision #7bf39888f7](https://github.com/MariaDB/server/commit/7bf39888f7)\
  2018-05-02 15:24:27 +0200
  * CONNECT: remove an outdated declaration
* [Revision #b1a6d2826a](https://github.com/MariaDB/server/commit/b1a6d2826a)\
  2018-04-24 13:19:44 +0200
  * cleanup: versioning style fixes
* [Revision #531acda484](https://github.com/MariaDB/server/commit/531acda484)\
  2018-04-18 14:29:48 +0200
  * [MDEV-14820](https://jira.mariadb.org/browse/MDEV-14820) System versioning is applied incorrectly to CTEs
* [Revision #0f956a0676](https://github.com/MariaDB/server/commit/0f956a0676)\
  2018-04-14 00:09:11 +0200
  * cleanup: hide HA\_ERR\_RECORD\_DELETED in ha\_rnd\_next()
* [Revision #5441bbd3b1](https://github.com/MariaDB/server/commit/5441bbd3b1)\
  2018-04-18 13:28:22 +0200
  * ./mtr --gdb testname
* [Revision #0a1c0a439a](https://github.com/MariaDB/server/commit/0a1c0a439a)\
  2018-04-13 19:15:00 +0200
  * compilation warnings w/o partitioning
* [Revision #c982924242](https://github.com/MariaDB/server/commit/c982924242)\
  2018-05-02 13:45:44 +0400
  * [MDEV-15592](https://jira.mariadb.org/browse/MDEV-15592) - Column COMPRESSED should select a 'high order' datatype
* [Revision #8ad12b6664](https://github.com/MariaDB/server/commit/8ad12b6664)\
  2018-05-11 10:11:48 +0800
  * User \_server\_host per discussion.
* [Revision #ee8dfc688e](https://github.com/MariaDB/server/commit/ee8dfc688e)\
  2018-05-10 03:53:29 +0000
  * Add host name to session attributes.
* [Revision #4a126bf3e1](https://github.com/MariaDB/server/commit/4a126bf3e1)\
  2018-05-11 18:02:16 +0400
  * Removing some duplicate code in THD::convert\_string() & friends
* [Revision #af682525a8](https://github.com/MariaDB/server/commit/af682525a8)\
  2018-05-11 13:15:47 +0200
  * compiler warning
* [Revision #e19915d5d2](https://github.com/MariaDB/server/commit/e19915d5d2)\
  2018-05-10 19:45:09 +0200
  * [MDEV-15746](https://jira.mariadb.org/browse/MDEV-15746) ASAN heap-use-after-free in Item\_change\_list::rollback\_item\_tree\_changes on ALTER executed as PS
* Merge [Revision #c9717dc019](https://github.com/MariaDB/server/commit/c9717dc019) 2018-05-11 13:12:18 +0200 - Merge branch '10.2' into 10.3
* [Revision #33721d9138](https://github.com/MariaDB/server/commit/33721d9138)\
  2018-05-10 19:30:43 +0400
  * [MDEV-16134](https://jira.mariadb.org/browse/MDEV-16134) Wrong I\_S.COLUMNS.CHARACTER\_XXX\_LENGTH value for compressed columns
* [Revision #fc63c1e17a](https://github.com/MariaDB/server/commit/fc63c1e17a)\
  2018-05-10 15:55:33 +0400
  * [MDEV-16117](https://jira.mariadb.org/browse/MDEV-16117) SP with a single FOR statement creates but further fails to load
* Merge [Revision #8b087c63b5](https://github.com/MariaDB/server/commit/8b087c63b5) 2018-05-09 12:00:08 -0700 - [MDEV-15697](https://jira.mariadb.org/browse/MDEV-15697): Remote user used by Spider needs SUPER privilege
* [Revision #72f0efac67](https://github.com/MariaDB/server/commit/72f0efac67)\
  2018-05-01 14:14:06 -0700
  * [MDEV-15697](https://jira.mariadb.org/browse/MDEV-15697): Remote user used by Spider needs SUPER privilege
* [Revision #85ccdd9ff0](https://github.com/MariaDB/server/commit/85ccdd9ff0)\
  2018-05-09 17:06:21 +0300
  * Rename a test (fix merge error)
* [Revision #d94a9553db](https://github.com/MariaDB/server/commit/d94a9553db)\
  2018-05-09 19:28:40 +0530
  * [MDEV-16125](https://jira.mariadb.org/browse/MDEV-16125) Crash or ASAN heap-buffer-overflow in mach\_read\_from\_n\_little\_endian upon ALTER TABLE with blob
* Merge [Revision #e9f2609747](https://github.com/MariaDB/server/commit/e9f2609747) 2018-05-09 16:52:45 +0300 - Merge 10.2 into 10.3
* Merge [Revision #9be99dac90](https://github.com/MariaDB/server/commit/9be99dac90) 2018-05-09 16:12:08 +0300 - [MDEV-15437](https://jira.mariadb.org/browse/MDEV-15437) POWER8 implementation of CRC-32C in C
* [Revision #69ae6499e6](https://github.com/MariaDB/server/commit/69ae6499e6)\
  2018-05-09 13:03:10 +1000
  * Add CRC32\_VPMSUM\_LIBRARY to libmysqld/mysqlserver libraries
* [Revision #9748659981](https://github.com/MariaDB/server/commit/9748659981)\
  2018-05-07 17:04:18 +1000
  * mtr: extend func\_math (CRC32)
* [Revision #c28be510d1](https://github.com/MariaDB/server/commit/c28be510d1)\
  2017-08-22 15:54:15 +1000
  * Power8: use C implementation of crc32 instead of ASM
* [Revision #891f202193](https://github.com/MariaDB/server/commit/891f202193)\
  2017-09-04 15:09:53 +1000
  * tests: extend func\_math crc32 to a larger size to hit crc32-vpmsum accelerated functions
* [Revision #fc0f5adb7f](https://github.com/MariaDB/server/commit/fc0f5adb7f)\
  2018-05-08 23:32:11 -0700
  * [MDEV-16104](https://jira.mariadb.org/browse/MDEV-16104) Server crash in JOIN::fix\_all\_splittings\_in\_plan upon select with view and subqueries
* [Revision #2deb17fd54](https://github.com/MariaDB/server/commit/2deb17fd54)\
  2018-05-09 02:05:25 +0300
  * sql\_sequence.debug\_sync fails upon server startup
* [Revision #1d30a23fcc](https://github.com/MariaDB/server/commit/1d30a23fcc)\
  2018-05-09 00:16:32 +0400
  * Moving a few static functions in sql\_lex.cc to new methods in Lex\_input\_stream
* [Revision #971268dc14](https://github.com/MariaDB/server/commit/971268dc14)\
  2018-05-08 22:32:31 +0400
  * Fixing tabs to spaces in sql\_lex.cc and sql\_lex.h (and coding style slightly)
* Merge [Revision #1b8749f73b](https://github.com/MariaDB/server/commit/1b8749f73b) 2018-05-08 17:18:55 +0300 - Merge 10.2 into 10.3
* [Revision #4513de3127](https://github.com/MariaDB/server/commit/4513de3127)\
  2018-05-08 10:40:05 +0300
  * Remove a "register" keyword from C++ code
* [Revision #a536664e80](https://github.com/MariaDB/server/commit/a536664e80)\
  2018-05-08 13:29:29 +0300
  * Added test case for [MDEV-13029](https://jira.mariadb.org/browse/MDEV-13029)
* [Revision #bd09c5ca86](https://github.com/MariaDB/server/commit/bd09c5ca86)\
  2018-05-07 16:39:53 +0300
  * Added test case for [MDEV-13007](https://jira.mariadb.org/browse/MDEV-13007) ALTER .. ENGINE on temporary sequence may go wrong
* [Revision #d405bee058](https://github.com/MariaDB/server/commit/d405bee058)\
  2018-04-04 20:16:30 +1000
  * mysys: disable "optimized" memcpy from 18 years ago
* Merge [Revision #1a4c355a1c](https://github.com/MariaDB/server/commit/1a4c355a1c) 2018-05-07 15:50:38 +0300 - Merge 10.2 into 10.3
* [Revision #005d53f6d5](https://github.com/MariaDB/server/commit/005d53f6d5)\
  2018-05-07 09:40:57 +1000
  * sp\_cache\_package\_routine: fix compile warning
* [Revision #c5b28e55f6](https://github.com/MariaDB/server/commit/c5b28e55f6)\
  2018-05-07 14:56:53 +0530
  * [MDEV-13134](https://jira.mariadb.org/browse/MDEV-13134) Introduce ALTER TABLE attributes ALGORITHM=NOCOPY and ALGORITHM=INSTANT
* [Revision #85cc6b70bd](https://github.com/MariaDB/server/commit/85cc6b70bd)\
  2018-05-07 14:54:58 +0530
  * [MDEV-13134](https://jira.mariadb.org/browse/MDEV-13134) Introduce ALTER TABLE attributes ALGORITHM=NOCOPY and ALGORITHM=INSTANT
* [Revision #a0bc3b7eee](https://github.com/MariaDB/server/commit/a0bc3b7eee)\
  2018-04-12 09:28:29 +0300
  * Change read\_to\_buffer to use ulong instead of uint
* [Revision #062a3176e7](https://github.com/MariaDB/server/commit/062a3176e7)\
  2018-04-12 02:57:19 +0300
  * Remove mem\_alloc\_error()
* [Revision #70c1110a29](https://github.com/MariaDB/server/commit/70c1110a29)\
  2018-04-17 00:08:03 +0300
  * Optimize performance schema likely/unlikely
* [Revision #9d6dc39ad9](https://github.com/MariaDB/server/commit/9d6dc39ad9)\
  2018-04-11 02:08:02 +0300
  * Add checking of correct likely/unlikely
* [Revision #30ebc3ee9e](https://github.com/MariaDB/server/commit/30ebc3ee9e)\
  2018-04-04 12:16:12 +0300
  * Add likely/unlikely to speed up execution
* [Revision #a22a339f8e](https://github.com/MariaDB/server/commit/a22a339f8e)\
  2018-04-26 19:58:43 +0200
  * [MDEV-13024](https://jira.mariadb.org/browse/MDEV-13024): Server crashes in my\_store\_ptr upon DELETE from sequence in multi-table format
* [Revision #724ab9a1cb](https://github.com/MariaDB/server/commit/724ab9a1cb)\
  2018-04-30 13:05:01 +0530
  * [MDEV-16057](https://jira.mariadb.org/browse/MDEV-16057): Using optimization Splitting with Group BY we see an unnecessary attached condition t1.pk IS NOT NULL where pk is a PRIMARY KEY
* [Revision #0bfd45f634](https://github.com/MariaDB/server/commit/0bfd45f634)\
  2018-05-06 19:39:48 +0300
  * Fix for [MDEV-15812](https://jira.mariadb.org/browse/MDEV-15812) Assert in SEQUENCE when forcing STATEMEMT format
* [Revision #529c1a3b6c](https://github.com/MariaDB/server/commit/529c1a3b6c)\
  2018-05-06 16:22:09 +0300
  * Fixed compiler warnings in spider
* [Revision #4891d514b6](https://github.com/MariaDB/server/commit/4891d514b6)\
  2018-05-06 16:10:49 +0400
  * [MDEV-16095](https://jira.mariadb.org/browse/MDEV-16095) Oracle-style placeholder inside GROUP BY..WITH ROLLUP breaks replication
* Merge [Revision #b20039dd80](https://github.com/MariaDB/server/commit/b20039dd80) 2018-05-04 16:09:22 +0300 - Merge 10.2 into 10.3
* [Revision #3b50cd2492](https://github.com/MariaDB/server/commit/3b50cd2492)\
  2018-05-04 14:42:53 +0300
  * Make a test independent of the build options
* [Revision #d36034b6d8](https://github.com/MariaDB/server/commit/d36034b6d8)\
  2018-05-03 20:54:23 +0300
  * Follow up for 9a8498066865b5 - adjustments to storage\_engine tests
* [Revision #ca174051d8](https://github.com/MariaDB/server/commit/ca174051d8)\
  2018-05-03 09:49:03 -0700
  * [MDEV-14019](https://jira.mariadb.org/browse/MDEV-14019): Spider + binlog\_format = ROW => CRASH
* [Revision #57c3dd991b](https://github.com/MariaDB/server/commit/57c3dd991b)\
  2018-05-03 17:49:16 +0300
  * [MDEV-15106](https://jira.mariadb.org/browse/MDEV-15106) Unexpected ER\_WRONG\_INSERT\_INTO\_SEQUENCE upon INSERT with multiple locks on sequences
* [Revision #6c43068d63](https://github.com/MariaDB/server/commit/6c43068d63)\
  2018-05-03 15:17:16 +0300
  * [MDEV-15060](https://jira.mariadb.org/browse/MDEV-15060) Assertion in row\_log\_table\_apply\_op after instant ADD when the table is emptied during subsequent ALTER TABLE
* [Revision #01843d1910](https://github.com/MariaDB/server/commit/01843d1910)\
  2018-05-03 10:21:07 +0300
  * Follow-up to [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Do not display table->space
* [Revision #73a10cbcc5](https://github.com/MariaDB/server/commit/73a10cbcc5)\
  2018-05-02 15:44:52 +0300
  * [MDEV-16065](https://jira.mariadb.org/browse/MDEV-16065) Assertion failed in btr\_pcur\_restore\_position\_func on UPDATE
* [Revision #dcc5de66f4](https://github.com/MariaDB/server/commit/dcc5de66f4)\
  2018-05-02 16:42:00 +0530
  * [MDEV-16071](https://jira.mariadb.org/browse/MDEV-16071) Server crashed in innobase\_build\_col\_map / prepare\_inplace\_alter\_table\_dict or Assertion \`tuple' failed in dtuple\_get\_nth\_field upon altering table with virtual column
* [Revision #8a941bad7d](https://github.com/MariaDB/server/commit/8a941bad7d)\
  2018-05-02 13:55:34 +0530
  * [MDEV-14168](https://jira.mariadb.org/browse/MDEV-14168) Unconditionally allow ALGORITHM=INPLACE for setting a column NOT NULL
* Merge [Revision #a7852e3ec8](https://github.com/MariaDB/server/commit/a7852e3ec8) 2018-05-01 16:45:03 -0700 - [MDEV-15698](https://jira.mariadb.org/browse/MDEV-15698): Spider ignores syntax errors in connection string in COMMENT field
* [Revision #c10da98b62](https://github.com/MariaDB/server/commit/c10da98b62)\
  2018-04-13 17:51:51 -0700
  * [MDEV-15698](https://jira.mariadb.org/browse/MDEV-15698): Spider ignores syntax errors in connection string in COMMENT field
* [Revision #2b27ac8282](https://github.com/MariaDB/server/commit/2b27ac8282)\
  2018-05-01 01:10:37 +0300
  * Fix many -Wunused-parameter
* [Revision #87b0434e0f](https://github.com/MariaDB/server/commit/87b0434e0f)\
  2018-05-01 15:39:36 +1000
  * [MDEV-12645](https://jira.mariadb.org/browse/MDEV-12645): mysql\_install\_db --no-test (postfix
* Merge [Revision #bf92784d38](https://github.com/MariaDB/server/commit/bf92784d38) 2018-04-30 19:07:44 -0700 - [MDEV-15712](https://jira.mariadb.org/browse/MDEV-15712): If remote server used by Spider table is unavailable, some operations hang for a long time
* [Revision #6ee6933a37](https://github.com/MariaDB/server/commit/6ee6933a37)\
  2018-04-23 22:00:27 -0700
  * [MDEV-15712](https://jira.mariadb.org/browse/MDEV-15712): If remote server used by Spider table is unavailable, some operations hang for a long time
* [Revision #68cbabbfb0](https://github.com/MariaDB/server/commit/68cbabbfb0)\
  2018-04-25 14:42:38 +0400
  * [MDEV-15938](https://jira.mariadb.org/browse/MDEV-15938) - TINYTEXT CHARACTER SET utf8 COMPRESSED truncates data
* [Revision #9a84980668](https://github.com/MariaDB/server/commit/9a84980668)\
  2018-04-11 16:50:32 +0400
  * [MDEV-12645](https://jira.mariadb.org/browse/MDEV-12645) - mysql\_install\_db: no install test db option
* [Revision #8bbcc0d505](https://github.com/MariaDB/server/commit/8bbcc0d505)\
  2018-04-30 18:12:14 +0300
  * [MDEV-12218](https://jira.mariadb.org/browse/MDEV-12218): Put back mariadb-backup --innodb-flush-method
* [Revision #9801715cb0](https://github.com/MariaDB/server/commit/9801715cb0)\
  2018-04-30 15:46:09 +0300
  * Use compile\_time\_assert() in InnoDB
* [Revision #8cd55ae2a9](https://github.com/MariaDB/server/commit/8cd55ae2a9)\
  2018-04-30 13:45:25 +0300
  * Fix WITH\_INNODB\_EXTRA\_DEBUG
* [Revision #a1fe7d75dc](https://github.com/MariaDB/server/commit/a1fe7d75dc)\
  2018-04-30 15:21:52 +0300
  * Removed even more warning that was found with -Wunused
* [Revision #7d6b55b99a](https://github.com/MariaDB/server/commit/7d6b55b99a)\
  2018-04-30 14:24:48 +0300
  * Added version of lex\_string\_eq that compares with const char \*
* [Revision #862e602b5a](https://github.com/MariaDB/server/commit/862e602b5a)\
  2018-04-27 08:26:28 +0300
  * Added more test to sql-bench
* [Revision #cb16bc95ff](https://github.com/MariaDB/server/commit/cb16bc95ff)\
  2018-04-30 11:25:36 +0300
  * [MDEV-14906](https://jira.mariadb.org/browse/MDEV-14906) Assertion index->is\_instant() failed on DELETE
* [Revision #38bc4bcc96](https://github.com/MariaDB/server/commit/38bc4bcc96)\
  2018-04-30 10:33:03 +0300
  * [MDEV-16058](https://jira.mariadb.org/browse/MDEV-16058) Unnecessary computations for SPATIAL INDEX
* [Revision #d73241c0a9](https://github.com/MariaDB/server/commit/d73241c0a9)\
  2018-04-30 10:28:50 +0300
  * Simplify dict\_stats\_analyze\_index\_level()
* [Revision #9b1313e849](https://github.com/MariaDB/server/commit/9b1313e849)\
  2018-04-30 07:55:11 +0300
  * rtr\_estimate\_n\_rows\_in\_range(): Simplify code
* [Revision #935025f891](https://github.com/MariaDB/server/commit/935025f891)\
  2018-04-30 07:46:22 +0300
  * Add an explicit cast from double to ha\_rows
* [Revision #b2c4740034](https://github.com/MariaDB/server/commit/b2c4740034)\
  2018-04-29 17:39:48 +0300
  * Fix some -Wsign-conversion
* [Revision #baa5a43d8c](https://github.com/MariaDB/server/commit/baa5a43d8c)\
  2018-04-27 13:17:18 +0300
  * [MDEV-16045](https://jira.mariadb.org/browse/MDEV-16045): Replace log\_group\_t with log\_t::files
* [Revision #d73a898d64](https://github.com/MariaDB/server/commit/d73a898d64)\
  2018-04-27 10:06:14 +0300
  * [MDEV-16045](https://jira.mariadb.org/browse/MDEV-16045): Allocate log\_sys statically
* [Revision #715e4f4320](https://github.com/MariaDB/server/commit/715e4f4320)\
  2018-04-29 09:41:42 +0300
  * [MDEV-12218](https://jira.mariadb.org/browse/MDEV-12218) Clean up InnoDB parameter validation
* [Revision #9ed2b2b2b8](https://github.com/MariaDB/server/commit/9ed2b2b2b8)\
  2018-04-27 14:26:43 +0300
  * Do not divide or multiply by srv\_page\_size
* [Revision #a90100d756](https://github.com/MariaDB/server/commit/a90100d756)\
  2018-04-27 13:49:25 +0300
  * Replace univ\_page\_size and UNIV\_PAGE\_SIZE
* [Revision #ba19764209](https://github.com/MariaDB/server/commit/ba19764209)\
  2018-04-28 15:49:09 +0300
  * Fix most -Wsign-conversion in InnoDB
* [Revision #e37df0f95a](https://github.com/MariaDB/server/commit/e37df0f95a)\
  2018-04-28 16:28:30 +0300
  * Fix some -Wsign-conversion
* [Revision #1292a01c7f](https://github.com/MariaDB/server/commit/1292a01c7f)\
  2018-04-28 19:47:21 +0300
  * Simplify simple\_counter
* [Revision #8861d442d6](https://github.com/MariaDB/server/commit/8861d442d6)\
  2018-04-27 09:41:34 +0300
  * Correct member function comments
* Merge [Revision #704ef98d0a](https://github.com/MariaDB/server/commit/704ef98d0a) 2018-04-28 20:36:31 +0300 - Merge 10.2 into 10.3
* [Revision #4968049799](https://github.com/MariaDB/server/commit/4968049799)\
  2018-04-28 15:16:45 +0400
  * [MDEV-11084](https://jira.mariadb.org/browse/MDEV-11084) Select statement with partition selection against MyISAM table opens all partitions.
* [Revision #9df0eab327](https://github.com/MariaDB/server/commit/9df0eab327)\
  2018-04-28 08:49:07 +0400
  * Cleanup for [MDEV-16020](https://jira.mariadb.org/browse/MDEV-16020) (fixing compilation failure on Windows)
* [Revision #96a301bbbe](https://github.com/MariaDB/server/commit/96a301bbbe)\
  2018-04-27 22:11:18 +0400
  * [MDEV-16020](https://jira.mariadb.org/browse/MDEV-16020) SP variables inside GROUP BY..WITH ROLLUP break replication
* [Revision #6c5e60f1b1](https://github.com/MariaDB/server/commit/6c5e60f1b1)\
  2018-04-26 16:38:56 -0700
  * [MDEV-16038](https://jira.mariadb.org/browse/MDEV-16038) Assertion \`map->n\_bits > 0' failed (my\_bitmap.c:386: bitmap\_is\_clear\_all)
* Merge [Revision #99fa7c6c2f](https://github.com/MariaDB/server/commit/99fa7c6c2f) 2018-04-26 22:58:41 +0300 - Merge 10.2 into 10.3
* [Revision #2898c7ec9e](https://github.com/MariaDB/server/commit/2898c7ec9e)\
  2018-04-25 22:40:24 +0300
  * [MDEV-15914](https://jira.mariadb.org/browse/MDEV-15914): Make mtr\_buf\_t a plain class
* [Revision #362151e8c8](https://github.com/MariaDB/server/commit/362151e8c8)\
  2018-04-25 22:29:58 +0300
  * [MDEV-15914](https://jira.mariadb.org/browse/MDEV-15914): Simplify mlog\_open\_and\_write\_index()
* [Revision #6f88bc4511](https://github.com/MariaDB/server/commit/6f88bc4511)\
  2018-04-25 13:27:22 +0300
  * [MDEV-15914](https://jira.mariadb.org/browse/MDEV-15914): Use buf\_block\_t\* for undo, not page\_t\*
* [Revision #76c62bc69c](https://github.com/MariaDB/server/commit/76c62bc69c)\
  2018-04-25 13:05:40 +0300
  * [MDEV-15914](https://jira.mariadb.org/browse/MDEV-15914): Restore MLOG\_UNDO\_INSERT
* [Revision #83bd4dd1ee](https://github.com/MariaDB/server/commit/83bd4dd1ee)\
  2018-04-25 10:41:32 +0300
  * [MDEV-15914](https://jira.mariadb.org/browse/MDEV-15914): Remove trx\_t::undo\_mutex
* [Revision #f7cac5e26c](https://github.com/MariaDB/server/commit/f7cac5e26c)\
  2018-04-25 11:07:34 +0300
  * [MDEV-12288](https://jira.mariadb.org/browse/MDEV-12288)/[MDEV-15132](https://jira.mariadb.org/browse/MDEV-15132)/[MDEV-15158](https://jira.mariadb.org/browse/MDEV-15158): Adjust a comment
* [Revision #ff0000cdd2](https://github.com/MariaDB/server/commit/ff0000cdd2)\
  2018-04-25 09:56:03 +0300
  * [MDEV-15914](https://jira.mariadb.org/browse/MDEV-15914): Remove trx\_undo\_t::empty
* [Revision #c121574dff](https://github.com/MariaDB/server/commit/c121574dff)\
  2018-04-25 09:37:14 +0300
  * [MDEV-15914](https://jira.mariadb.org/browse/MDEV-15914): buf\_pool\_is\_obsolete(): Add UNIV\_UNLIKELY
* [Revision #7b7e4d679a](https://github.com/MariaDB/server/commit/7b7e4d679a)\
  2018-04-25 09:34:50 +0300
  * [MDEV-15914](https://jira.mariadb.org/browse/MDEV-15914): Simplify row\_search\_mvcc()
* [Revision #30553aa37b](https://github.com/MariaDB/server/commit/30553aa37b)\
  2018-04-25 08:50:56 +0300
  * [MDEV-15914](https://jira.mariadb.org/browse/MDEV-15914): Fast path for rw\_trx\_hash::find()
* [Revision #6e42d19f25](https://github.com/MariaDB/server/commit/6e42d19f25)\
  2018-04-26 23:12:51 +0400
  * [MDEV-15915](https://jira.mariadb.org/browse/MDEV-15915) Add Feature\_json status variable.
* [Revision #cd48c1e23a](https://github.com/MariaDB/server/commit/cd48c1e23a)\
  2018-04-26 17:57:38 +0300
  * Removed some old #if MYSQL\_VERSION
* [Revision #2ccd6716fc](https://github.com/MariaDB/server/commit/2ccd6716fc)\
  2018-04-26 16:33:05 +0300
  * Fix a lot of compiler warnings found by -Wunused
* [Revision #0bdc15d86e](https://github.com/MariaDB/server/commit/0bdc15d86e)\
  2018-04-25 21:32:47 +0200
  * [MDEV-15732](https://jira.mariadb.org/browse/MDEV-15732): Assertion \`next\_free\_value % real\_increment == offset && next\_free\_value >= reserved\_until' failed in sequence\_definition::adjust\_values upon SETVAL for sequence with INCREMENT 0
* [Revision #7f89d9c9e3](https://github.com/MariaDB/server/commit/7f89d9c9e3)\
  2018-04-21 15:44:55 +1000
  * tests: func\_math, correct crc32 for mariadb
* [Revision #1a011e5b5a](https://github.com/MariaDB/server/commit/1a011e5b5a)\
  2018-04-21 15:07:51 +1000
  * BUG#26495791: CONTRIBUTION: EXPAND TEST SUITE TO INCLUDE CRC32 TESTS
* [Revision #5bba69f816](https://github.com/MariaDB/server/commit/5bba69f816)\
  2018-04-25 18:22:56 -0700
  * Fixed a compiler error
* [Revision #b4ee699a89](https://github.com/MariaDB/server/commit/b4ee699a89)\
  2018-04-18 19:34:12 +0200
  * [MDEV-11975](https://jira.mariadb.org/browse/MDEV-11975): SQLCOM\_PREPARE of EXPLAIN & ANALYZE statement do not return correct metadata info
* [Revision #0544d7c457](https://github.com/MariaDB/server/commit/0544d7c457)\
  2018-04-24 12:04:59 +0200
  * [MDEV-13695](https://jira.mariadb.org/browse/MDEV-13695): INTERSECT precedence is not in line with Oracle even in SQL\_MODE=Oracle
* [Revision #43c5dd0250](https://github.com/MariaDB/server/commit/43c5dd0250)\
  2018-04-23 12:09:10 +0200
  * [MDEV-15079](https://jira.mariadb.org/browse/MDEV-15079): Parameter array operation inserts wrong values in autoincrement field if indicator was specified
* Merge [Revision #9477a2a9ba](https://github.com/MariaDB/server/commit/9477a2a9ba) 2018-04-25 07:58:46 +0300 - Merge 10.2 into 10.3
* [Revision #e3fb8e9569](https://github.com/MariaDB/server/commit/e3fb8e9569)\
  2018-04-25 00:14:12 +0300
  * Remove trx\_t::undo\_rseg\_space
* Merge [Revision #7396dfcca7](https://github.com/MariaDB/server/commit/7396dfcca7) 2018-04-24 20:59:57 +0300 - Merge 10.2 into 10.3
* Merge [Revision #f79c5a658c](https://github.com/MariaDB/server/commit/f79c5a658c) 2018-04-24 10:06:31 +0200 - Merge branch '10.3' into bb-10.3-[MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814)
* [Revision #4f9977d8d3](https://github.com/MariaDB/server/commit/4f9977d8d3)\
  2018-04-24 13:15:35 +0530
  * [MDEV-14168](https://jira.mariadb.org/browse/MDEV-14168) Unconditionally allow ALGORITHM=INPLACE for setting a column NOT NULL
* Merge [Revision #47ac7252ff](https://github.com/MariaDB/server/commit/47ac7252ff) 2018-04-24 09:32:10 +0200 - Merge branch 'grooverdan-10.2-[MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814)-dont-dump-query-cache' into bb-10.3-[MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814)
* Merge [Revision #abb4db4c3f](https://github.com/MariaDB/server/commit/abb4db4c3f) 2018-04-24 09:31:10 +0200 - Merge branch '10.2-[MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814)-dont-dump-query-cache' of [mariadb-server](https://github.com/grooverdan/mariadb-server) into grooverdan-10.2-[MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814)-dont-dump-query-cache
* [Revision #31aa277768](https://github.com/MariaDB/server/commit/31aa277768)\
  2018-02-26 18:13:59 +1100
  * [MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814): Don't coredump query cache
* Merge [Revision #0805a9565f](https://github.com/MariaDB/server/commit/0805a9565f) 2018-02-25 15:25:54 +1100 - Merge branch '10.3' into 10.2-[MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814)-dont-dump-query-cache
* [Revision #3188131b15](https://github.com/MariaDB/server/commit/3188131b15)\
  2017-04-25 17:49:15 +1000
  * [MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814): Coredumps to exclude query cache (Linux)
* [Revision #461de7edea](https://github.com/MariaDB/server/commit/461de7edea)\
  2018-04-23 18:34:06 +0400
  * [MDEV-15946](https://jira.mariadb.org/browse/MDEV-15946) MEDIUMINT(N<8) creates a wrong data type on conversion to string
* [Revision #8fce4065e5](https://github.com/MariaDB/server/commit/8fce4065e5)\
  2018-04-23 17:03:25 +0400
  * "AS OF" clean in Type\_handler
* [Revision #14f84d2071](https://github.com/MariaDB/server/commit/14f84d2071)\
  2018-04-23 10:35:33 +0200
  * [MDEV-13232](https://jira.mariadb.org/browse/MDEV-13232): Assertion \`(&(\&share->intern\_lock)->m\_mutex)->count > 0 && pthread\_equal(pthread\_self(), (&(\&share->intern\_lock)->m\_mutex)->thread)' failed in \_ma\_state\_info\_write
* [Revision #de942c9f61](https://github.com/MariaDB/server/commit/de942c9f61)\
  2018-04-23 13:15:54 +0300
  * [MDEV-15983](https://jira.mariadb.org/browse/MDEV-15983) Reduce fil\_system.mutex contention further
* [Revision #6c64101bf0](https://github.com/MariaDB/server/commit/6c64101bf0)\
  2018-04-23 13:14:28 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266) follow-up fix to mariadb-backup
* Merge [Revision #c6ba758d1d](https://github.com/MariaDB/server/commit/c6ba758d1d) 2018-04-23 09:49:58 +0300 - Merge 10.2 into 10.3
* [Revision #6426b52ed4](https://github.com/MariaDB/server/commit/6426b52ed4)\
  2018-04-23 09:31:17 +0400
  * [MDEV-15957](https://jira.mariadb.org/browse/MDEV-15957) Unexpected "Data too long" when doing CREATE..SELECT with stored func
* [Revision #9f84451d87](https://github.com/MariaDB/server/commit/9f84451d87)\
  2018-04-22 15:52:46 +0400
  * [MDEV-15960](https://jira.mariadb.org/browse/MDEV-15960) Wrong data type on CREATE..SELECT char\_or\_enum\_or\_text\_spvar
* [Revision #c555dc768f](https://github.com/MariaDB/server/commit/c555dc768f)\
  2018-04-22 13:30:31 +0400
  * [MDEV-15971](https://jira.mariadb.org/browse/MDEV-15971) Split the code for CHARACTER\_OCTET\_LENGTH and CHARACTER\_MAXIMUM\_LENGTH into methods in Field
* [Revision #6242036f27](https://github.com/MariaDB/server/commit/6242036f27)\
  2018-04-21 17:20:20 -0700
  * [MDEV-15940](https://jira.mariadb.org/browse/MDEV-15940) Crash when using CURSOR with VALUES()
* [Revision #c39f8a80c9](https://github.com/MariaDB/server/commit/c39f8a80c9)\
  2018-04-21 17:53:37 +0300
  * Quote 'rank' in test-ATIS so that it can be run with MySQL 8.0
* [Revision #6b1a8b2c72](https://github.com/MariaDB/server/commit/6b1a8b2c72)\
  2018-04-21 18:38:58 +0530
  * [MDEV-15846](https://jira.mariadb.org/browse/MDEV-15846): Sever crashed with MEDIAN() window function
* [Revision #c058117c6c](https://github.com/MariaDB/server/commit/c058117c6c)\
  2018-04-20 23:15:27 +0400
  * Adding more tests for IN/EXIST subqueries for better coverage
* [Revision #791fb9ea24](https://github.com/MariaDB/server/commit/791fb9ea24)\
  2018-04-20 18:28:38 +0400
  * Fixed compiler warning
* [Revision #9aaf62d058](https://github.com/MariaDB/server/commit/9aaf62d058)\
  2018-04-20 18:11:27 +0400
  * [MDEV-15926](https://jira.mariadb.org/browse/MDEV-15926) MEDIUMINT returns wrong I\_S attributes
* [Revision #38c799c9a5](https://github.com/MariaDB/server/commit/38c799c9a5)\
  2018-04-03 18:34:46 +0400
  * [MDEV-15763](https://jira.mariadb.org/browse/MDEV-15763) - VARCHAR(1) COMPRESSED crashes the server
* [Revision #3dec6c48bc](https://github.com/MariaDB/server/commit/3dec6c48bc)\
  2018-04-03 16:19:37 +0400
  * [MDEV-15762](https://jira.mariadb.org/browse/MDEV-15762) - VARCHAR(0) COMPRESSED crashes the server
* [Revision #43ab88f0ea](https://github.com/MariaDB/server/commit/43ab88f0ea)\
  2018-04-20 16:52:51 +0530
  * Buildbot fixes
* [Revision #615ad709a3](https://github.com/MariaDB/server/commit/615ad709a3)\
  2018-04-19 18:40:31 -0700
  * [MDEV-15902](https://jira.mariadb.org/browse/MDEV-15902) Assertion \`n < m\_size' failed, sql\_array.h:64: Element\_type& Bounds\_checked\_array\<Element\_type>::operator\[] (size\_t) \[with Element\_type = Item\*; size\_t = long unsigned int]
* [Revision #cd8b8169b6](https://github.com/MariaDB/server/commit/cd8b8169b6)\
  2018-04-19 22:11:41 +0530
  * [MDEV-15167](https://jira.mariadb.org/browse/MDEV-15167) Server crashes in bitmap\_bits\_set upon REPAIR PARTITION... after rebuilding under test\_pseudo\_invisible
* Merge [Revision #d71a8855ee](https://github.com/MariaDB/server/commit/d71a8855ee) 2018-04-19 15:23:21 +0300 - Merge 10.2 to 10.3
* [Revision #419385dbf1](https://github.com/MariaDB/server/commit/419385dbf1)\
  2018-04-19 14:31:20 +0530
  * [MDEV-10664](https://jira.mariadb.org/browse/MDEV-10664) Add statuses about optimistic parallel replication stalls
* [Revision #547b00d910](https://github.com/MariaDB/server/commit/547b00d910)\
  2018-04-19 13:04:58 +0530
  * [MDEV-12924](https://jira.mariadb.org/browse/MDEV-12924) No --innodb-numa-interleave in mysqld binaries
* [Revision #dde0ba5aaa](https://github.com/MariaDB/server/commit/dde0ba5aaa)\
  2018-04-16 16:27:11 +0530
  * [MDEV-15754](https://jira.mariadb.org/browse/MDEV-15754) Server crashes in fill\_record\_n\_invoke\_before\_triggers upon ... insert into table with TIMESTAMP INVISIBLE
* [Revision #fa68b88b5d](https://github.com/MariaDB/server/commit/fa68b88b5d)\
  2018-04-18 13:39:03 +0530
  * [MDEV-15828](https://jira.mariadb.org/browse/MDEV-15828) Server crash or assertion \`num\_fts\_index <= 1' failure up on ALTER TABLE adding two fulltext indexes
* [Revision #cff60be7fe](https://github.com/MariaDB/server/commit/cff60be7fe)\
  2018-04-17 23:39:40 -0700
  * [MDEV-15899](https://jira.mariadb.org/browse/MDEV-15899) Server crashes in st\_join\_table::is\_inner\_table\_of\_outer\_join
* [Revision #bb5f4967f5](https://github.com/MariaDB/server/commit/bb5f4967f5)\
  2018-04-17 16:10:47 +0400
  * [MDEV-13584](https://jira.mariadb.org/browse/MDEV-13584) Assertion \`!part\_elem->tablespace\_name && !table\_create\_info->tablespace' failed during EXCHANGE PARTITION with different TABLESPACE.
* [Revision #02e897ca57](https://github.com/MariaDB/server/commit/02e897ca57)\
  2018-04-16 20:34:55 +0300
  * [MDEV-15889](https://jira.mariadb.org/browse/MDEV-15889) Semisync ack thread hits an LOCK\_plugin assert at shutdown
* [Revision #321771f89f](https://github.com/MariaDB/server/commit/321771f89f)\
  2018-04-15 15:29:55 +0100
  * [MDEV-15895](https://jira.mariadb.org/browse/MDEV-15895) : make Innodb merge temp tables use pfs\_os\_file\_t for file IO, rather than int.
* [Revision #7d991feb75](https://github.com/MariaDB/server/commit/7d991feb75)\
  2018-04-17 00:24:44 +0300
  * Fixed failing testcase rename\_table\_debug
* [Revision #0f7022c6f3](https://github.com/MariaDB/server/commit/0f7022c6f3)\
  2018-04-12 05:15:39 +0300
  * Renamed compile-pentium scripts to compile-pentium32
* [Revision #1074b9b8be](https://github.com/MariaDB/server/commit/1074b9b8be)\
  2018-04-11 11:46:27 +0300
  * Ensure that max\_local\_memory\_used is initialized
* [Revision #3bae6a2b98](https://github.com/MariaDB/server/commit/3bae6a2b98)\
  2018-04-11 03:18:03 +0300
  * Remove not needed calls to print\_error
* [Revision #ddc5764303](https://github.com/MariaDB/server/commit/ddc5764303)\
  2018-04-11 02:20:22 +0300
  * Remove compiler warnings
* [Revision #dbbe70e1cf](https://github.com/MariaDB/server/commit/dbbe70e1cf)\
  2018-04-16 11:31:02 -0400
  * bump the VERSION
* [Revision #4c136f80a5](https://github.com/MariaDB/server/commit/4c136f80a5)\
  2018-04-16 17:41:29 +0800
  * Updated apparmor-profile for spelling errors
* [Revision #c9839cb0b3](https://github.com/MariaDB/server/commit/c9839cb0b3)\
  2018-01-19 19:09:05 +1100
  * [MDEV-13336](https://jira.mariadb.org/browse/MDEV-13336): mysqldump --ignore-database address review comments
* [Revision #784e9391c9](https://github.com/MariaDB/server/commit/784e9391c9)\
  2017-07-30 16:11:25 +0200
  * [MDEV-13336](https://jira.mariadb.org/browse/MDEV-13336) Add --ignore-database option to mysqldump
* [Revision #f0e4f94c23](https://github.com/MariaDB/server/commit/f0e4f94c23)\
  2018-04-15 18:23:19 +0300
  * [MDEV-15871](https://jira.mariadb.org/browse/MDEV-15871) Crash in btr\_search\_build\_page\_hash\_index()
* [Revision #97e51d24cb](https://github.com/MariaDB/server/commit/97e51d24cb)\
  2018-04-15 10:21:15 +0300
  * [MDEV-13697](https://jira.mariadb.org/browse/MDEV-13697) DB\_TRX\_ID is not always reset

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
