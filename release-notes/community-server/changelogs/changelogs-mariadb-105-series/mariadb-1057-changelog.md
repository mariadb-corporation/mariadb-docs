# MariaDB 10.5.7 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.7](https://downloads.mariadb.org/mariadb/10.5.7/)[Release Notes](../../old-releases/10.5/10.5.7.md)[Changelog](mariadb-1057-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 3 Nov 2020

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.7.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.16](../changelogs-mariadb-10-4-series/mariadb-10416-changelog.md)
* [Revision #90f43d260e](https://github.com/MariaDB/server/commit/90f43d260e)\
  2020-11-03 12:41:41 +0200
  * [MDEV-24101](https://jira.mariadb.org/browse/MDEV-24101) innodb\_random\_read\_ahead=ON causes hang on DDL or shutdown
* [Revision #95fcd567bd](https://github.com/MariaDB/server/commit/95fcd567bd)\
  2020-11-02 04:15:13 +0200
  * List of unstable tests for 10.5.7 release
* Merge [Revision #8e1e2856f2](https://github.com/MariaDB/server/commit/8e1e2856f2) 2020-11-01 14:26:15 +0100 - Merge branch '10.4' into 10.5
* [Revision #b0ff791618](https://github.com/MariaDB/server/commit/b0ff791618)\
  2020-10-30 19:06:50 +0200
  * [MDEV-24054](https://jira.mariadb.org/browse/MDEV-24054) Assertion in\_LRU\_list failed in buf\_flush\_try\_neighbors()
* Merge [Revision #03357ded17](https://github.com/MariaDB/server/commit/03357ded17) 2020-10-30 13:53:10 +0200 - Merge 10.4 into 10.5
* [Revision #066773e2f0](https://github.com/MariaDB/server/commit/066773e2f0)\
  2020-10-30 11:46:12 +0100
  * after-merge fix: update the test to pass in --ps
* Merge [Revision #898521e2dd](https://github.com/MariaDB/server/commit/898521e2dd) 2020-10-30 11:15:30 +0200 - Merge 10.4 into 10.5
* [Revision #571bcf9aaa](https://github.com/MariaDB/server/commit/571bcf9aaa)\
  2020-10-30 15:09:18 +1100
  * deb: logrotate - fix my\_print\_defaults arg
* [Revision #6d3356c12e](https://github.com/MariaDB/server/commit/6d3356c12e)\
  2020-10-29 15:51:09 +0200
  * [MDEV-24053](https://jira.mariadb.org/browse/MDEV-24053) MSAN use-of-uninitialized-value in tpool::simulated\_aio::simulated\_aio\_callback()
* [Revision #8cfdddac71](https://github.com/MariaDB/server/commit/8cfdddac71)\
  2020-10-29 08:49:03 +0200
  * MYSQL\_JSON: Update test case to omit .so or .dll extension
* [Revision #8b2800d076](https://github.com/MariaDB/server/commit/8b2800d076)\
  2020-10-29 08:37:27 +0200
  * Fix decimals to 0 for MySQL JSON
* [Revision #f3c5a92490](https://github.com/MariaDB/server/commit/f3c5a92490)\
  2020-10-28 23:04:55 +0200
  * Add type\_mysql\_json.so to debian packages
* [Revision #a041b94032](https://github.com/MariaDB/server/commit/a041b94032)\
  2020-10-28 23:00:21 +0200
  * Move vers\_type\_timestamp within the CC file
* [Revision #76fabe816f](https://github.com/MariaDB/server/commit/76fabe816f)\
  2020-10-28 21:33:20 +0200
  * Expose utf8mb4\_bin charset for plugins
* [Revision #17ec6d6ce1](https://github.com/MariaDB/server/commit/17ec6d6ce1)\
  2020-10-28 21:21:15 +0200
  * Skip MYSQL\_JSON related tests if the plugin is not compiled
* [Revision #9a4398b048](https://github.com/MariaDB/server/commit/9a4398b048)\
  2020-10-28 00:58:38 +0100
  * update columnstore
* [Revision #05bd281697](https://github.com/MariaDB/server/commit/05bd281697)\
  2020-10-28 21:53:35 +0100
  * SPIDER storage engine plugin -> Stable
* [Revision #7f04686a2a](https://github.com/MariaDB/server/commit/7f04686a2a)\
  2020-10-29 09:15:35 +0200
  * [MDEV-24049](https://jira.mariadb.org/browse/MDEV-24049) InnoDB: Failing assertion: node->is\_open() in fil\_space\_t::flush\_low
* [Revision #e33d452b4d](https://github.com/MariaDB/server/commit/e33d452b4d)\
  2020-10-29 08:16:44 +0200
  * Fix bogus -Wmaybe-uninitialized in GCC 10.2.0 -Og
* [Revision #f6549e9544](https://github.com/MariaDB/server/commit/f6549e9544)\
  2020-10-15 18:02:24 +0300
  * [MDEV-18323](https://jira.mariadb.org/browse/MDEV-18323) Convert MySQL JSON type to MariaDB TEXT in mysql\_upgrade
* [Revision #85c686e2d1](https://github.com/MariaDB/server/commit/85c686e2d1)\
  2020-10-15 17:37:31 +0300
  * cleanup: Static\_binary\_string need not take non-const double parameter
* [Revision #9478368d81](https://github.com/MariaDB/server/commit/9478368d81)\
  2020-10-27 20:54:03 +0100
  * [MDEV-24037](https://jira.mariadb.org/browse/MDEV-24037) Use NtFlushBuffersFileEx(FLUSH\_FLAGS\_FILE\_DATA\_SYNC\_ONLY) on Windows
* [Revision #db56f9b852](https://github.com/MariaDB/server/commit/db56f9b852)\
  2020-10-26 12:05:47 +0530
  * [MDEV-24015](https://jira.mariadb.org/browse/MDEV-24015): SQL Error (1038): Out of sort memory when enough memory for the sort buffer is provided
* [Revision #2cec0523eb](https://github.com/MariaDB/server/commit/2cec0523eb)\
  2020-10-27 16:45:35 +0100
  * INET6 type plugin -> Beta
* [Revision #00ddea4f2f](https://github.com/MariaDB/server/commit/00ddea4f2f)\
  2020-10-27 09:52:42 +0200
  * [MDEV-24024](https://jira.mariadb.org/browse/MDEV-24024) innodb.ibuf\_not\_empty failed in buildbot
* [Revision #c27e53f459](https://github.com/MariaDB/server/commit/c27e53f459)\
  2020-10-26 16:43:52 +0200
  * [MDEV-23855](https://jira.mariadb.org/browse/MDEV-23855): Use normal mutex for log\_sys.mutex, log\_sys.flush\_order\_mutex
* [Revision #a5a2ef079c](https://github.com/MariaDB/server/commit/a5a2ef079c)\
  2020-10-23 12:53:40 +0300
  * [MDEV-23855](https://jira.mariadb.org/browse/MDEV-23855): Implement asynchronous doublewrite
* [Revision #ef3f71fa74](https://github.com/MariaDB/server/commit/ef3f71fa74)\
  2020-10-23 12:29:11 +0300
  * [MDEV-23399](https://jira.mariadb.org/browse/MDEV-23399) fixup: Interleaved doublewrite batches
* [Revision #8cb01c51fb](https://github.com/MariaDB/server/commit/8cb01c51fb)\
  2020-10-23 10:49:03 +0300
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) fixup: Clean up asynchronous I/O
* [Revision #118e258aaa](https://github.com/MariaDB/server/commit/118e258aaa)\
  2020-10-26 16:04:12 +0200
  * [MDEV-23855](https://jira.mariadb.org/browse/MDEV-23855): Shrink fil\_space\_t
* [Revision #45ed9dd957](https://github.com/MariaDB/server/commit/45ed9dd957)\
  2020-10-26 15:59:30 +0200
  * [MDEV-23855](https://jira.mariadb.org/browse/MDEV-23855): Remove fil\_system.LRU and reduce fil\_system.mutex contention
* [Revision #3a9a3be1c6](https://github.com/MariaDB/server/commit/3a9a3be1c6)\
  2020-10-26 16:35:47 +0200
  * [MDEV-23855](https://jira.mariadb.org/browse/MDEV-23855): Improve InnoDB log checkpoint performance
* [Revision #bd67cb9284](https://github.com/MariaDB/server/commit/bd67cb9284)\
  2020-10-26 17:07:17 +0200
  * [MDEV-23399](https://jira.mariadb.org/browse/MDEV-23399) fixup: Assertion bpage->in\_file() failed
* [Revision #59a0236da4](https://github.com/MariaDB/server/commit/59a0236da4)\
  2020-10-16 14:38:07 +0300
  * Cleanup: Speed up mariadb-backup --prepare
* [Revision #5999d5120e](https://github.com/MariaDB/server/commit/5999d5120e)\
  2020-10-26 15:04:24 +0200
  * [MDEV-23399](https://jira.mariadb.org/browse/MDEV-23399) fixup: Avoid crash on mariadb-backup shutdown
* [Revision #d8515c8d35](https://github.com/MariaDB/server/commit/d8515c8d35)\
  2020-08-27 18:59:09 +0200
  * S3 plugin fails to load depending on loaded storage engines
* [Revision #e764d11829](https://github.com/MariaDB/server/commit/e764d11829)\
  2020-09-25 12:52:37 +0200
  * fix occasisonal test failures: SELECT without ORDER BY
* [Revision #606a281162](https://github.com/MariaDB/server/commit/606a281162)\
  2020-09-23 12:24:16 +0200
  * [MDEV-22100](https://jira.mariadb.org/browse/MDEV-22100) TokuDB compilation error
* [Revision #73a2ae9f89](https://github.com/MariaDB/server/commit/73a2ae9f89)\
  2020-09-19 19:17:04 +0200
  * [MDEV-23764](https://jira.mariadb.org/browse/MDEV-23764) Slave crashes in ha\_storage\_engine\_is\_enabled upon rename of view
* [Revision #3cd4d8ddba](https://github.com/MariaDB/server/commit/3cd4d8ddba)\
  2020-09-17 16:08:23 +0200
  * parser optimization
* [Revision #d8fbd463a0](https://github.com/MariaDB/server/commit/d8fbd463a0)\
  2020-09-17 16:04:21 +0200
  * don't use deprecated \_LIB\_DEPENDS. CMP0073
* [Revision #9df99151da](https://github.com/MariaDB/server/commit/9df99151da)\
  2020-10-24 00:16:56 +0400
  * [MDEV-23437](https://jira.mariadb.org/browse/MDEV-23437) Item\_func\_json\_objectagg::print is not implemented.
* [Revision #bff82f51ba](https://github.com/MariaDB/server/commit/bff82f51ba)\
  2020-10-21 19:12:54 +0000
  * Fixed compilation issues with debug build and install test issues for Ubuntu Xenial
* [Revision #0d581562d8](https://github.com/MariaDB/server/commit/0d581562d8)\
  2020-10-22 17:09:18 +0300
  * Fix memory leak on Alter\_drop allocation
* Merge [Revision #1657b7a583](https://github.com/MariaDB/server/commit/1657b7a583) 2020-10-22 17:08:49 +0300 - Merge 10.4 to 10.5
* [Revision #cca75c95bc](https://github.com/MariaDB/server/commit/cca75c95bc)\
  2020-10-22 14:40:11 +0300
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659) Update Galera disabled.def file
* [Revision #b30ad01d40](https://github.com/MariaDB/server/commit/b30ad01d40)\
  2020-04-16 00:44:20 +0900
  * [MDEV-20100](https://jira.mariadb.org/browse/MDEV-20100) [MariaDB 10.3.9](../../old-releases/10.3/10.3.9.md) Crash "\[ERROR] mysqld got signal 11 ;"
* [Revision #1668465f68](https://github.com/MariaDB/server/commit/1668465f68)\
  2020-10-21 10:56:26 +0300
  * [MDEV-23998](https://jira.mariadb.org/browse/MDEV-23998) Race between buf\_page\_optimistic\_get() and buf\_page\_t::init()
* [Revision #05cd5acba6](https://github.com/MariaDB/server/commit/05cd5acba6)\
  2020-10-21 10:53:55 +0300
  * [MDEV-23986](https://jira.mariadb.org/browse/MDEV-23986): fil\_page\_type\_validate() fails on crash recovery
* [Revision #8c074df6ac](https://github.com/MariaDB/server/commit/8c074df6ac)\
  2020-10-19 22:04:45 +0300
  * [MDEV-23648](https://jira.mariadb.org/browse/MDEV-23648) s3.partition\_move 'innodb' test failure - object deleted before copy attempted
* [Revision #21c15cc20b](https://github.com/MariaDB/server/commit/21c15cc20b)\
  2020-10-16 15:45:50 +0300
  * Fixed compiler warning in connect/filemazip.cpp
* [Revision #2912f1f866](https://github.com/MariaDB/server/commit/2912f1f866)\
  2020-10-16 15:45:30 +0300
  * Fixed typo in mtr\_cases.pm
* [Revision #3c4b8440eb](https://github.com/MariaDB/server/commit/3c4b8440eb)\
  2020-09-13 15:51:26 +0300
  * Trivial fixups, no code changes
* [Revision #dd757ee02f](https://github.com/MariaDB/server/commit/dd757ee02f)\
  2020-09-10 16:55:24 +0300
  * Update S3 engine to maturity Gamma
* [Revision #2c8c15483d](https://github.com/MariaDB/server/commit/2c8c15483d)\
  2020-10-16 19:36:24 +0300
  * [MDEV-23730](https://jira.mariadb.org/browse/MDEV-23730) s3.replication\_partition 'innodb,mix' segv
* [Revision #71d263a198](https://github.com/MariaDB/server/commit/71d263a198)\
  2020-09-13 15:45:41 +0300
  * [MDEV-23691](https://jira.mariadb.org/browse/MDEV-23691) S3 storage engine: delayed slave can drop the table
* [Revision #5902d5e0eb](https://github.com/MariaDB/server/commit/5902d5e0eb)\
  2020-09-13 14:20:10 +0300
  * Added wait-for-pos-timeout=NUM argument to mtr
* [Revision #f9c432c5a9](https://github.com/MariaDB/server/commit/f9c432c5a9)\
  2020-09-10 16:28:12 +0300
  * Disable from valgrind big innodb tests that doesn't run well in valgrind
* [Revision #edfeb12919](https://github.com/MariaDB/server/commit/edfeb12919)\
  2020-10-20 13:08:16 +0000
  * MCS engine ref update
* [Revision #e3fc9c1db0](https://github.com/MariaDB/server/commit/e3fc9c1db0)\
  2020-10-20 11:55:52 +0400
  * [MDEV-19275](https://jira.mariadb.org/browse/MDEV-19275) Provide SQL service to plugins.
* [Revision #d1667fb837](https://github.com/MariaDB/server/commit/d1667fb837)\
  2020-10-20 11:16:40 +0300
  * [MDEV-23852](https://jira.mariadb.org/browse/MDEV-23852) alter table rename column to uppercase doesn't work
* [Revision #5ca14dafbe](https://github.com/MariaDB/server/commit/5ca14dafbe)\
  2020-10-19 16:51:52 +0400
  * [MDEV-19275](https://jira.mariadb.org/browse/MDEV-19275) Provide SQL service to plugins.
* [Revision #6dc037a9d1](https://github.com/MariaDB/server/commit/6dc037a9d1)\
  2020-10-16 22:02:54 +0300
  * [MDEV-23399](https://jira.mariadb.org/browse/MDEV-23399) fixup: Remove double-free of a buffer page
* [Revision #bdbec5a2e9](https://github.com/MariaDB/server/commit/bdbec5a2e9)\
  2020-10-16 17:28:23 +0300
  * [MDEV-23973](https://jira.mariadb.org/browse/MDEV-23973) Change buffer corruption when reallocating an recently freed page
* [Revision #a0113683d7](https://github.com/MariaDB/server/commit/a0113683d7)\
  2020-10-16 07:51:37 +0300
  * Fixup 9028cc6b865222cae8c396b4ec3e317c8ee068d1
* [Revision #9028cc6b86](https://github.com/MariaDB/server/commit/9028cc6b86)\
  2020-10-15 16:28:19 +0300
  * Cleanup: Make InnoDB page numbers uint32\_t
* [Revision #61161d51d7](https://github.com/MariaDB/server/commit/61161d51d7)\
  2020-10-15 15:04:43 +0300
  * Cleanup: Remove export\_vars.innodb\_num\_open\_files
* [Revision #ecb913c2a5](https://github.com/MariaDB/server/commit/ecb913c2a5)\
  2020-10-15 13:21:52 +0300
  * Cleanup: Compare page\_id\_t directly
* [Revision #abb678b618](https://github.com/MariaDB/server/commit/abb678b618)\
  2020-10-15 13:27:09 +0300
  * [MDEV-19514](https://jira.mariadb.org/browse/MDEV-19514) fixup: Simplify buf\_page\_read\_complete()
* [Revision #7cffb5f6e8](https://github.com/MariaDB/server/commit/7cffb5f6e8)\
  2020-10-15 12:10:42 +0300
  * [MDEV-23399](https://jira.mariadb.org/browse/MDEV-23399): Performance regression with write workloads
* [Revision #46b1f50098](https://github.com/MariaDB/server/commit/46b1f50098)\
  2020-10-15 10:27:25 +0300
  * [MDEV-23399](https://jira.mariadb.org/browse/MDEV-23399): Remove buf\_pool.flush\_rbt
* [Revision #b535a79044](https://github.com/MariaDB/server/commit/b535a79044)\
  2020-10-15 10:26:52 +0300
  * [MDEV-23399](https://jira.mariadb.org/browse/MDEV-23399): Remove recv\_writer\_thread
* [Revision #fa70c1462a](https://github.com/MariaDB/server/commit/fa70c1462a)\
  2020-10-15 09:49:20 +0300
  * [MDEV-23399](https://jira.mariadb.org/browse/MDEV-23399) preparation: Remove buf\_pool.zip\_clean
* [Revision #308f8350c7](https://github.com/MariaDB/server/commit/308f8350c7)\
  2020-10-15 09:40:19 +0300
  * [MDEV-23190](https://jira.mariadb.org/browse/MDEV-23190) after-merge fix: remove unused code
* [Revision #cea6a6669e](https://github.com/MariaDB/server/commit/cea6a6669e)\
  2020-04-15 13:54:49 +0300
  * Travis-CI: Use new Ubuntu 20.04 as base, streamline and document
* [Revision #a891fe6aa5](https://github.com/MariaDB/server/commit/a891fe6aa5)\
  2020-10-09 12:47:58 +0300
  * [MDEV-23927](https://jira.mariadb.org/browse/MDEV-23927) Crash in ./mtr --skip-innodb-fast-shutdown innodb.temporary\_tables
* [Revision #d312d64146](https://github.com/MariaDB/server/commit/d312d64146)\
  2020-10-08 11:13:47 +0300
  * [MDEV-23909](https://jira.mariadb.org/browse/MDEV-23909) innodb\_flush\_neighbors=2 is treated like innodb\_flush\_neighbors=0
* Merge [Revision #2ff2e8463b](https://github.com/MariaDB/server/commit/2ff2e8463b) 2020-10-07 18:59:23 +0200 - Merge tag 'mariadb-10.5.6' into 10.5
* [Revision #0c7f52939c](https://github.com/MariaDB/server/commit/0c7f52939c)\
  2020-10-07 11:28:28 -0400
  * bump the VERSION
* [Revision #861cd4ce28](https://github.com/MariaDB/server/commit/861cd4ce28)\
  2020-10-05 13:05:11 +0300
  * [MDEV-22871](https://jira.mariadb.org/browse/MDEV-22871) fixup: Remove SYNC\_BUF\_PAGE\_HASH
* [Revision #7fba16d53f](https://github.com/MariaDB/server/commit/7fba16d53f)\
  2020-10-02 14:04:16 +0300
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) fixup: Remove unused fts\_optimize\_wq->event
* [Revision #0ccdf8b11b](https://github.com/MariaDB/server/commit/0ccdf8b11b)\
  2020-10-02 10:19:00 +0400
  * [MDEV-19275](https://jira.mariadb.org/browse/MDEV-19275) Provide SQL service to plugins.
* [Revision #82bc007ffb](https://github.com/MariaDB/server/commit/82bc007ffb)\
  2020-10-02 07:11:53 +0300
  * Cleanup: Remove non-existing parameters
* [Revision #91d39f630d](https://github.com/MariaDB/server/commit/91d39f630d)\
  2020-10-02 07:10:16 +0300
  * Cleanup: Remove unused mutex keys
* [Revision #b15224c71a](https://github.com/MariaDB/server/commit/b15224c71a)\
  2020-10-01 14:35:42 +0300
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) fixup: Remove unused declarations
* Merge [Revision #1c65ab26de](https://github.com/MariaDB/server/commit/1c65ab26de) 2020-10-01 14:30:17 +0300 - Merge 10.4 into 10.5
* [Revision #a9550c47e4](https://github.com/MariaDB/server/commit/a9550c47e4)\
  2020-09-30 14:28:11 +0300
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) fixup: Remove unused code and data
* [Revision #c7399db645](https://github.com/MariaDB/server/commit/c7399db645)\
  2020-09-28 12:23:48 +0300
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174) fixup: Remove buf\_dblwr\_being\_created
* [Revision #8bc4ebed67](https://github.com/MariaDB/server/commit/8bc4ebed67)\
  2020-09-30 13:48:20 +0300
  * [MDEV-21534](https://jira.mariadb.org/browse/MDEV-21534) fixup: Remove traces of removed log\_sys.write\_mutex
* [Revision #ef254efc65](https://github.com/MariaDB/server/commit/ef254efc65)\
  2020-09-27 13:24:09 +0300
  * Cleanup: Simplify sync\_array\_object\_signalled()
* [Revision #363da42190](https://github.com/MariaDB/server/commit/363da42190)\
  2020-09-27 13:05:00 +0300
  * Cleanup: Remove unnecessary declarations
* [Revision #bac16c7e0c](https://github.com/MariaDB/server/commit/bac16c7e0c)\
  2020-09-27 10:26:06 +0300
  * Cleanup: Remove unnecessary #include
* [Revision #216ed17934](https://github.com/MariaDB/server/commit/216ed17934)\
  2020-09-17 10:36:25 +1000
  * [MDEV-22678](https://jira.mariadb.org/browse/MDEV-22678): Debian Upgrade from MySQL-5.7 CE fails with "Plugin 'auth\_socket' is not loaded
* Merge [Revision #25ede13611](https://github.com/MariaDB/server/commit/25ede13611) 2020-09-29 16:59:36 +0530 - Merge branch '10.4' into 10.5
* [Revision #080522dcd7](https://github.com/MariaDB/server/commit/080522dcd7)\
  2020-09-26 18:04:17 +0400
  * [MDEV-23825](https://jira.mariadb.org/browse/MDEV-23825) Join select\_handler and Pushdown\_select + XPand changes
* [Revision #d111e6ae0c](https://github.com/MariaDB/server/commit/d111e6ae0c)\
  2020-09-27 01:01:41 +0200
  * Fix clang-cl build
* [Revision #d34523faee](https://github.com/MariaDB/server/commit/d34523faee)\
  2020-09-25 17:29:33 +0300
  * [MDEV-15053](https://jira.mariadb.org/browse/MDEV-15053) fixup: Remove redundant code
* [Revision #50c9687013](https://github.com/MariaDB/server/commit/50c9687013)\
  2020-09-25 17:28:54 +0300
  * [MDEV-23807](https://jira.mariadb.org/browse/MDEV-23807) ut\_a(n\_pending\_flushes) failed in fil\_node\_t::prepare\_to\_close\_or\_detach()
* [Revision #1adb537806](https://github.com/MariaDB/server/commit/1adb537806)\
  2020-09-24 16:16:16 +0300
  * [MDEV-23456](https://jira.mariadb.org/browse/MDEV-23456): After-merge fix
* [Revision #e57c1167ab](https://github.com/MariaDB/server/commit/e57c1167ab)\
  2020-09-24 14:12:22 +0300
  * [MDEV-23806](https://jira.mariadb.org/browse/MDEV-23806) Undo page corruption on recovery
* [Revision #6736fe92d7](https://github.com/MariaDB/server/commit/6736fe92d7)\
  2020-09-24 13:08:43 +0200
  * Fix GCC warning: this decimal constant is unsigned only in ISO C90
* Merge [Revision #882ce206db](https://github.com/MariaDB/server/commit/882ce206db) 2020-09-23 11:32:43 +0300 - Merge 10.4 into 10.5
* [Revision #6ab6b1510e](https://github.com/MariaDB/server/commit/6ab6b1510e)\
  2020-09-20 17:26:15 +0300
  * [MDEV-23650](https://jira.mariadb.org/browse/MDEV-23650) Test S3 in buildbot
* [Revision #29a6d23622](https://github.com/MariaDB/server/commit/29a6d23622)\
  2020-09-20 00:07:37 +0300
  * [MDEV-23767](https://jira.mariadb.org/browse/MDEV-23767): IN-to-subquery conversion is not visible in optimizer trace
* [Revision #ccbe6bb6fc](https://github.com/MariaDB/server/commit/ccbe6bb6fc)\
  2020-09-17 16:07:37 +0200
  * [MDEV-19935](https://jira.mariadb.org/browse/MDEV-19935) Create unified CRC-32 interface
* [Revision #ab56cbcd81](https://github.com/MariaDB/server/commit/ab56cbcd81)\
  2020-09-15 12:50:19 +0300
  * Stabilize and clean up a test
* [Revision #d61c5696fa](https://github.com/MariaDB/server/commit/d61c5696fa)\
  2020-09-10 14:10:15 +0300
  * Make a test more robust
* [Revision #00cd53d39a](https://github.com/MariaDB/server/commit/00cd53d39a)\
  2020-09-11 15:55:30 +0300
  * [MDEV-23719](https://jira.mariadb.org/browse/MDEV-23719): Make lock\_sys use page\_id\_t
* [Revision #852771ba1e](https://github.com/MariaDB/server/commit/852771ba1e)\
  2020-09-11 15:52:22 +0300
  * [MDEV-23719](https://jira.mariadb.org/browse/MDEV-23719): Remove buf\_block\_t::lock\_hash\_val
* [Revision #2bac9782aa](https://github.com/MariaDB/server/commit/2bac9782aa)\
  2020-09-12 10:33:33 +0200
  * make install: don't assume $DESTDIR exists
* [Revision #fd5cbbb91e](https://github.com/MariaDB/server/commit/fd5cbbb91e)\
  2020-09-14 11:48:36 +0300
  * [MDEV-23591](https://jira.mariadb.org/browse/MDEV-23591) : galera\_3nodes.GCF-354 MTR failed: 1047: WSREP has not yet prepared node for application use
* [Revision #5f2728d594](https://github.com/MariaDB/server/commit/5f2728d594)\
  2020-08-24 11:25:37 +0100
  * Define variable to override endpoint url
* [Revision #897b51db43](https://github.com/MariaDB/server/commit/897b51db43)\
  2020-09-10 12:12:47 +0200
  * make S3 tests to run when S3 is statically linked
* [Revision #5ad36aa3b8](https://github.com/MariaDB/server/commit/5ad36aa3b8)\
  2020-09-08 18:54:56 +0200
  * de-virtualize redundantly virtual Item method
* [Revision #d2bf1ed030](https://github.com/MariaDB/server/commit/d2bf1ed030)\
  2020-08-31 09:54:46 +0200
  * [MDEV-23492](https://jira.mariadb.org/browse/MDEV-23492) performance\_schema\_digests\_size changing from default to 5000 when enabling performance\_schema
* Merge [Revision #3421223363](https://github.com/MariaDB/server/commit/3421223363) 2020-09-09 16:57:30 +0300 - Merge 10.4 into 10.5
* [Revision #a569dc55fb](https://github.com/MariaDB/server/commit/a569dc55fb)\
  2020-09-09 14:46:17 +0300
  * [MDEV-23592](https://jira.mariadb.org/browse/MDEV-23592) : galera\_3nodes.inconsistency\_shutdown MTR failed: Could not open '../galera/include/galera\_have\_debug\_sync.inc' for reading, errno: 2
* [Revision #e17d0eb6d2](https://github.com/MariaDB/server/commit/e17d0eb6d2)\
  2020-09-09 14:16:07 +0300
  * [MDEV-23593](https://jira.mariadb.org/browse/MDEV-23593) : galera\_3nodes.GCF-376 MTR failed: Table 'test.t1' doesn't exist
* [Revision #d252f44c5d](https://github.com/MariaDB/server/commit/d252f44c5d)\
  2020-09-07 16:07:11 +0300
  * Update libmarias3 to PR#92: updated PR#91, adds capability to support port number
* [Revision #7478e0858f](https://github.com/MariaDB/server/commit/7478e0858f)\
  2020-09-05 22:24:32 +0300
  * Update libmarias3 to PR#91 which adds capability to specify port number
* [Revision #f98b8d36bd](https://github.com/MariaDB/server/commit/f98b8d36bd)\
  2020-09-04 10:44:05 +1000
  * [MDEV-23662](https://jira.mariadb.org/browse/MDEV-23662): Make S3 Storage Engine tests better
* [Revision #64c10b03a0](https://github.com/MariaDB/server/commit/64c10b03a0)\
  2020-09-04 10:23:28 +1000
  * [MDEV-23662](https://jira.mariadb.org/browse/MDEV-23662): Make S3 Storage Engine tests usable
* [Revision #e38ac39104](https://github.com/MariaDB/server/commit/e38ac39104)\
  2020-09-04 00:15:22 +0300
  * [MDEV-23662](https://jira.mariadb.org/browse/MDEV-23662): Make S3 Storage Engine usable with MinIO
* [Revision #c5517cd864](https://github.com/MariaDB/server/commit/c5517cd864)\
  2020-09-08 11:14:37 +0300
  * [MDEV-23638](https://jira.mariadb.org/browse/MDEV-23638) : DROP TRIGGER in Galera Cluster not replicating
* [Revision #9842ed4e6d](https://github.com/MariaDB/server/commit/9842ed4e6d)\
  2020-09-07 21:54:08 +0300
  * [MDEV-23549](https://jira.mariadb.org/browse/MDEV-23549) CREATE fails after DROP without FRM
* [Revision #92ffab382c](https://github.com/MariaDB/server/commit/92ffab382c)\
  2020-08-13 21:37:09 +0300
  * [MDEV-23473](https://jira.mariadb.org/browse/MDEV-23473) Query\_log\_event::pack\_info does not check flags2\_inited
* [Revision #30ff616403](https://github.com/MariaDB/server/commit/30ff616403)\
  2020-09-07 12:08:26 +0200
  * [MDEV-23680](https://jira.mariadb.org/browse/MDEV-23680) Assertion \`data' failed in crcr32\_calc\_pclmulqdq
* [Revision #2cc9e45693](https://github.com/MariaDB/server/commit/2cc9e45693)\
  2020-09-04 22:10:57 +0900
  * [MDEV-7098](https://jira.mariadb.org/browse/MDEV-7098) spider/bg.spider\_fixes failed in buildbot with safe\_mutex: Trying to unlock mutex conn->mta\_conn\_mutex that wasn't locked at storage/spider/spd\_db\_conn.cc, line 671
* [Revision #d25f806d73](https://github.com/MariaDB/server/commit/d25f806d73)\
  2020-09-04 14:33:13 +0200
  * [MDEV-22749](https://jira.mariadb.org/browse/MDEV-22749) Implement portable PCLMUL accelerated crc32() with Intel intrinsics
* Merge [Revision #5ff7e68c7e](https://github.com/MariaDB/server/commit/5ff7e68c7e) 2020-09-04 18:44:44 +0300 - Merge 10.4 into 10.5
* [Revision #938db04898](https://github.com/MariaDB/server/commit/938db04898)\
  2020-09-03 16:40:28 +0300
  * Cleanup: Remove os0proc.\*
* [Revision #48ab5a4997](https://github.com/MariaDB/server/commit/48ab5a4997)\
  2020-08-29 11:24:13 +0400
  * Part2: [MDEV-23568](https://jira.mariadb.org/browse/MDEV-23568) Improve performance of my\_{time|date|datetime}\_to\_str()
* [Revision #0af6e52521](https://github.com/MariaDB/server/commit/0af6e52521)\
  2020-09-01 21:12:01 +1000
  * travis: osx build time out storing cache. Ensure not Cellar
* [Revision #c34cb16588](https://github.com/MariaDB/server/commit/c34cb16588)\
  2020-09-01 11:34:03 +0200
  * fix compiler error on clang-cl
* [Revision #31e6c96b04](https://github.com/MariaDB/server/commit/31e6c96b04)\
  2020-08-31 10:27:58 +0300
  * [MDEV-20386](https://jira.mariadb.org/browse/MDEV-20386) WITH\_MSAN fails due to inline asm
* [Revision #9ef36faa61](https://github.com/MariaDB/server/commit/9ef36faa61)\
  2020-08-28 14:44:36 +0300
  * [MDEV-23618](https://jira.mariadb.org/browse/MDEV-23618) InnoDB lacks IA-32 CRC-32C acceleration on GCC 4
* [Revision #c14ecc7500](https://github.com/MariaDB/server/commit/c14ecc7500)\
  2020-08-25 15:56:25 +0400
  * [MDEV-23568](https://jira.mariadb.org/browse/MDEV-23568) Improve performance of my\_{time|date|datetime}\_to\_str()
* [Revision #482cf29e16](https://github.com/MariaDB/server/commit/482cf29e16)\
  2020-08-07 00:00:40 -0400
  * [MDEV-23091](https://jira.mariadb.org/browse/MDEV-23091): perfschema Add support for OpenBSD's getthrid() to retrieve the thread id
* [Revision #fe5dbfe723](https://github.com/MariaDB/server/commit/fe5dbfe723)\
  2020-08-27 11:42:35 +0300
  * [MDEV-23585](https://jira.mariadb.org/browse/MDEV-23585): Fix the 32-bit build on GCC 4
* [Revision #05aa7ae7ba](https://github.com/MariaDB/server/commit/05aa7ae7ba)\
  2020-08-26 22:25:26 +0900
  * Fix a compiler warning
* [Revision #b47d61d04f](https://github.com/MariaDB/server/commit/b47d61d04f)\
  2020-08-27 09:34:53 +0300
  * [MDEV-23585](https://jira.mariadb.org/browse/MDEV-23585): Fix HAVE\_CLMUL\_INSTRUCTION
* Merge [Revision #bb284e3fdb](https://github.com/MariaDB/server/commit/bb284e3fdb) 2020-08-27 09:34:23 +0300 - Merge 10.4 into 10.5
* Merge [Revision #97a4a3872e](https://github.com/MariaDB/server/commit/97a4a3872e) 2020-08-26 12:02:07 +0300 - Merge 10.4 into 10.5
* [Revision #8f8f2aea93](https://github.com/MariaDB/server/commit/8f8f2aea93)\
  2020-08-25 20:41:33 +0900
  * [MDEV-23561](https://jira.mariadb.org/browse/MDEV-23561) Spider doesn't work with ps protocol
* [Revision #e1a9b7ca7b](https://github.com/MariaDB/server/commit/e1a9b7ca7b)\
  2020-08-24 10:29:23 +0900
  * Fix indents of Spider
* [Revision #d8ba2930d6](https://github.com/MariaDB/server/commit/d8ba2930d6)\
  2020-08-25 15:25:22 +0300
  * [MDEV-23566](https://jira.mariadb.org/browse/MDEV-23566) SIGSEGV in mtr\_t::init
* [Revision #65ee216c35](https://github.com/MariaDB/server/commit/65ee216c35)\
  2020-08-23 12:30:14 +0900
  * [MDEV-22246](https://jira.mariadb.org/browse/MDEV-22246) Result rows duplicated by spider engine
* [Revision #c58e184b14](https://github.com/MariaDB/server/commit/c58e184b14)\
  2020-08-24 10:58:13 +1000
  * [MDEV-18841](https://jira.mariadb.org/browse/MDEV-18841): /var/run -> /run for apparmor/systemd service
* Merge [Revision #6f42cae0a1](https://github.com/MariaDB/server/commit/6f42cae0a1) 2020-08-23 15:55:50 +0400 - Merge remote-tracking branch 'origin/10.4' into 10.5
* Merge [Revision #6708e67acc](https://github.com/MariaDB/server/commit/6708e67acc) 2020-08-22 08:56:58 +0400 - Merge remote-tracking branch 'origin/10.4' into 10.5
* [Revision #ee61c8c0b7](https://github.com/MariaDB/server/commit/ee61c8c0b7)\
  2020-08-11 14:30:34 +0200
  * Fix spelling mistake in error message
* [Revision #151fc0ed88](https://github.com/MariaDB/server/commit/151fc0ed88)\
  2020-08-13 06:41:21 +0000
  * [MDEV-23495](https://jira.mariadb.org/browse/MDEV-23495): Refine Arm64 PMULL runtime check in MariaDB
* Merge [Revision #0b4ed0b7fb](https://github.com/MariaDB/server/commit/0b4ed0b7fb) 2020-08-21 20:32:04 +0300 - Merge 10.4 into 10.5
* [Revision #d98ccbe1e1](https://github.com/MariaDB/server/commit/d98ccbe1e1)\
  2020-08-21 11:54:16 +0300
  * [MDEV-23526](https://jira.mariadb.org/browse/MDEV-23526) InnoDB leaks memory for some static objects
* Merge [Revision #f2739e2a96](https://github.com/MariaDB/server/commit/f2739e2a96) 2020-08-21 11:53:55 +0300 - Merge 10.4 into 10.5
* [Revision #0775717479](https://github.com/MariaDB/server/commit/0775717479)\
  2020-08-21 11:53:30 +0300
  * [MDEV-23466](https://jira.mariadb.org/browse/MDEV-23466): Fix the result for different GTID format in 10.5
* [Revision #3ef65f2783](https://github.com/MariaDB/server/commit/3ef65f2783)\
  2020-08-20 19:33:33 +0300
  * Added DBUG\_PUSH\_EMPTY and DBUG\_POP\_EMPTY to speed up DBUG
* [Revision #b1ba3a199c](https://github.com/MariaDB/server/commit/b1ba3a199c)\
  2020-08-20 17:32:00 +0300
  * Reduce number of syncs to create a transactional aria table from 6 to 3
* [Revision #2c9be1e6ee](https://github.com/MariaDB/server/commit/2c9be1e6ee)\
  2020-08-20 17:29:40 +0300
  * Fixed wrong value of "wsrep" in SHOW STATUS
* [Revision #76a9227001](https://github.com/MariaDB/server/commit/76a9227001)\
  2020-08-20 17:28:12 +0300
  * Added support of WITH\_GPROF to cmake
* [Revision #65c43bcfe2](https://github.com/MariaDB/server/commit/65c43bcfe2)\
  2020-08-20 13:35:26 +0300
  * After-merge fix of the Windows build
* Merge [Revision #d5d8756de3](https://github.com/MariaDB/server/commit/d5d8756de3) 2020-08-20 12:52:44 +0300 - Merge 10.4 into 10.5
* [Revision #b205e478a3](https://github.com/MariaDB/server/commit/b205e478a3)\
  2020-08-19 15:47:11 +0300
  * Work around [MDEV-23416](https://jira.mariadb.org/browse/MDEV-23416) (change Warning to Note)
* [Revision #314a90e12b](https://github.com/MariaDB/server/commit/314a90e12b)\
  2020-08-17 09:45:03 +0900
  * [MDEV-20827](https://jira.mariadb.org/browse/MDEV-20827) Wrong param parsing in spider\_direct\_sql() when param contain comma
* [Revision #ad1a3ce418](https://github.com/MariaDB/server/commit/ad1a3ce418)\
  2020-08-13 05:36:23 +0900
  * [MDEV-19794](https://jira.mariadb.org/browse/MDEV-19794) Spider crash with XA
* [Revision #b01c426146](https://github.com/MariaDB/server/commit/b01c426146)\
  2020-08-14 21:04:25 +0400
  * [MDEV-19275](https://jira.mariadb.org/browse/MDEV-19275) Provide SQL service to plugins.
* [Revision #68cba09173](https://github.com/MariaDB/server/commit/68cba09173)\
  2020-08-14 14:45:36 +0300
  * Add QT\_ITEM\_IDENT\_DISABLE\_DB\_TABLE\_NAMES flag for Item::print
* [Revision #16d8d18907](https://github.com/MariaDB/server/commit/16d8d18907)\
  2020-08-14 14:43:26 +0300
  * Basic Optimizer Trace support for table condition pushdown
* [Revision #eab219d594](https://github.com/MariaDB/server/commit/eab219d594)\
  2020-08-10 11:44:42 +0300
  * [MDEV-22543](https://jira.mariadb.org/browse/MDEV-22543) : Galera SST donation fails, FLUSH TABLES WITH READ LOCK times out
* Merge [Revision #cf87f3e08c](https://github.com/MariaDB/server/commit/cf87f3e08c) 2020-08-14 11:33:35 +0300 - Merge 10.4 into 10.5
* [Revision #1bf77cde5c](https://github.com/MariaDB/server/commit/1bf77cde5c)\
  2020-08-14 11:32:46 +0300
  * [MDEV-23162](https://jira.mariadb.org/browse/MDEV-23162): Fix clang -Winconsistent-missing-override
* [Revision #48cbb2c021](https://github.com/MariaDB/server/commit/48cbb2c021)\
  2020-08-14 11:04:39 +0400
  * [MDEV-23478](https://jira.mariadb.org/browse/MDEV-23478) Improve Protocol performance for numeric data - version 2
* [Revision #c55f24cd99](https://github.com/MariaDB/server/commit/c55f24cd99)\
  2020-07-24 08:07:04 +0400
  * [MDEV-23162](https://jira.mariadb.org/browse/MDEV-23162) Improve Protocol performance for numeric data
* [Revision #f1a9700fec](https://github.com/MariaDB/server/commit/f1a9700fec)\
  2020-07-24 06:46:40 +0400
  * Revert "[MDEV-23162](https://jira.mariadb.org/browse/MDEV-23162) Improve Protocol performance for numeric data"
* [Revision #e96f66b93d](https://github.com/MariaDB/server/commit/e96f66b93d)\
  2020-07-23 14:48:04 +0400
  * [MDEV-23270](https://jira.mariadb.org/browse/MDEV-23270) Remove a String parameter from Protocol::store(double/float)
* [Revision #0ac8e2cfdb](https://github.com/MariaDB/server/commit/0ac8e2cfdb)\
  2020-08-13 21:44:46 +0300
  * Add a Github CODEOWNERS file to project
* [Revision #5eff7c0226](https://github.com/MariaDB/server/commit/5eff7c0226)\
  2020-08-12 21:38:03 +0200
  * [MDEV-23462](https://jira.mariadb.org/browse/MDEV-23462) Upgrade wizard not offered during 10.5 MSI installation on Windows
* [Revision #7541080214](https://github.com/MariaDB/server/commit/7541080214)\
  2020-08-12 21:18:21 +0200
  * [MDEV-23461](https://jira.mariadb.org/browse/MDEV-23461) mysql\_upgrade\_wizard.exe differs from mariadb-upgrade-wizard.exe
* [Revision #602d3dafa9](https://github.com/MariaDB/server/commit/602d3dafa9)\
  2020-08-11 17:39:43 +0000
  * [MDEV-23279](https://jira.mariadb.org/browse/MDEV-23279) postfix - delay accepting connections until server startup is finished.
* [Revision #6a7e646df3](https://github.com/MariaDB/server/commit/6a7e646df3)\
  2020-08-11 12:35:19 +0400
  * [MDEV-23054](https://jira.mariadb.org/browse/MDEV-23054) Assertion \`!item->null\_value' failed in Type\_handler\_inet6::make\_sort\_key\_part (#2)
* Merge [Revision #0718b8ecbf](https://github.com/MariaDB/server/commit/0718b8ecbf) 2020-08-11 11:12:45 +0300 - Merge 10.4 into 10.5
* Merge [Revision #1c58748196](https://github.com/MariaDB/server/commit/1c58748196) 2020-08-10 21:38:55 +0300 - Merge 10.4 into 10.5
* Merge [Revision #17be2b47ba](https://github.com/MariaDB/server/commit/17be2b47ba) 2020-08-10 21:11:54 +0300 - Merge mariadb-10.5.5
* [Revision #4ea915e28c](https://github.com/MariaDB/server/commit/4ea915e28c)\
  2020-08-10 17:33:48 +0000
  * [MDEV-23279](https://jira.mariadb.org/browse/MDEV-23279) main.named\_pipe test timeouts if called twice in a row
* [Revision #5611df6774](https://github.com/MariaDB/server/commit/5611df6774)\
  2020-08-10 10:37:16 -0400
  * bump the VERSION
* [Revision #6f84150c21](https://github.com/MariaDB/server/commit/6f84150c21)\
  2020-08-10 17:03:54 +0300
  * [MDEV-23422](https://jira.mariadb.org/browse/MDEV-23422) innodb\_zip.restart fails with extra #sql-ib\*.ibd
* [Revision #9b2fe4bd12](https://github.com/MariaDB/server/commit/9b2fe4bd12)\
  2020-08-09 14:25:22 +0400
  * [MDEV-23435](https://jira.mariadb.org/browse/MDEV-23435) Functions do not convert numbers to character\_set\_results
* [Revision #2b6dd87b2c](https://github.com/MariaDB/server/commit/2b6dd87b2c)\
  2020-08-07 15:10:37 +1000
  * debian: 99-enable-encryption.cnf.preset file, not symlink
* [Revision #699a43704b](https://github.com/MariaDB/server/commit/699a43704b)\
  2020-08-07 14:59:48 +1000
  * debian: remove gcc check. don't package rocksdb on x86\_32
* [Revision #cca55a9ca9](https://github.com/MariaDB/server/commit/cca55a9ca9)\
  2020-08-07 14:58:59 +1000
  * debian: disable rocksdb on 32bit with valid cmake directive
* [Revision #be974e5620](https://github.com/MariaDB/server/commit/be974e5620)\
  2020-08-05 18:28:53 +0400
  * [MDEV-22278](https://jira.mariadb.org/browse/MDEV-22278) change temp-pool to be 0 by default

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
