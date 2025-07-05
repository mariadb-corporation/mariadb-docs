# MariaDB 10.1.0 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.0)[Release Notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-0-release-notes.md)[Changelog](mariadb-10-1-0-changelog.md)[Overview of 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)

**Release date:** 30 Jun 2014

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-0-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #c235de1](https://github.com/MariaDB/server/commit/c235de1)\
  2014-06-26 22:06:41 +0400
  * [MDEV-6394](https://jira.mariadb.org/browse/MDEV-6394): ANALYZE DELETE .. RETURNING fails with ERROR 2027 Malformed packet (now, the code)
* [Revision #9394f2f](https://github.com/MariaDB/server/commit/9394f2f)\
  2014-06-26 22:04:04 +0400
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #3d7eeb6](https://github.com/MariaDB/server/commit/3d7eeb6)\
  2014-06-26 22:03:13 +0400
  * [MDEV-6394](https://jira.mariadb.org/browse/MDEV-6394): ANALYZE DELETE .. RETURNING fails with ERROR 2027 Malformed packet
* [Revision #c6d29cd](https://github.com/MariaDB/server/commit/c6d29cd)\
  2014-06-26 20:47:08 +0300
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #3e59948](https://github.com/MariaDB/server/commit/3e59948)\
  2014-06-26 20:45:27 +0300
  * [MDEV-6392](https://jira.mariadb.org/browse/MDEV-6392): Change innodb\_have\_lzo and innodb\_have\_lz4 as a static variables and reduce the number of ifdef's
* [Revision #be885eb](https://github.com/MariaDB/server/commit/be885eb)\
  2014-06-26 20:12:18 +0400
  * Code cleanup, more tests.
* [Revision #c6be744](https://github.com/MariaDB/server/commit/c6be744)\
  2014-06-26 19:09:23 +0400
  * [MDEV-6398](https://jira.mariadb.org/browse/MDEV-6398): ANALYZE UPDATE does not populate r\_rows
* [Revision #a787edd](https://github.com/MariaDB/server/commit/a787edd)\
  2014-06-26 18:32:18 +0400
  * [MDEV-6395](https://jira.mariadb.org/browse/MDEV-6395): Make ANALYZE UPDATE/DELETE handle the degenerate query plans.
* [Revision #12d6f89](https://github.com/MariaDB/server/commit/12d6f89)\
  2014-06-26 15:55:25 +0400
  * [MDEV-6393](https://jira.mariadb.org/browse/MDEV-6393): ANALYZE SELECT crashes ... Don't try printing EXPLAIN if we had an error.
* [Revision #b7d10e5](https://github.com/MariaDB/server/commit/b7d10e5)\
  2014-06-26 12:46:33 +0200
  * [MDEV-5730](https://jira.mariadb.org/browse/MDEV-5730) enhance security using special compilation options
* [Revision #da4f826](https://github.com/MariaDB/server/commit/da4f826)\
  2014-06-16 21:39:09 +0200
  * [MDEV-5730](https://jira.mariadb.org/browse/MDEV-5730) enhance security using special compilation options
* [Revision #6c0e3ef](https://github.com/MariaDB/server/commit/6c0e3ef)\
  2014-06-16 21:30:48 +0200
  * cmake cleanup: use MY\_CHECK\_AND\_SET\_COMPILER\_FLAG.
* [Revision #afa4c36](https://github.com/MariaDB/server/commit/afa4c36)\
  2014-06-16 21:24:30 +0200
  * cmake: prefer INSTALL(PROGRAMS over INSTALL(FILES
* [Revision #6c9dd84](https://github.com/MariaDB/server/commit/6c9dd84)\
  2014-06-16 22:16:21 +0200
  * remove unused sql/examples
* [Revision #b95ec13](https://github.com/MariaDB/server/commit/b95ec13)\
  2014-06-26 11:37:24 +0500
  * Revert "[MDEV-12](https://jira.mariadb.org/browse/MDEV-12) OpenGIS: create required tables: GeometryColumns, related views."
* [Revision #648b957](https://github.com/MariaDB/server/commit/648b957)\
  2014-06-26 10:48:08 +0400
  * Merge branch 'bb-10.1-explain-analyze' into 10.1
* [Revision #68bf3c5](https://github.com/MariaDB/server/commit/68bf3c5)\
  2014-06-26 10:43:58 +0400
  * Code cleanup
* [Revision #18d5a74](https://github.com/MariaDB/server/commit/18d5a74)\
  2014-06-26 01:22:50 +0400
  * [MDEV-406](https://jira.mariadb.org/browse/MDEV-406): ANALYZE $stmt: Make multi-table UPDATE/DELETE work, code cleanup.
* [Revision #0bf9fd8](https://github.com/MariaDB/server/commit/0bf9fd8)\
  2014-06-26 00:46:21 +0500
  * [MDEV-12](https://jira.mariadb.org/browse/MDEV-12) OpenGIS: create required tables: GeometryColumns, related views. Scripts added that create OpenGIS-required views and tables they're based upon.
* [Revision #aa22471](https://github.com/MariaDB/server/commit/aa22471)\
  2014-06-25 21:00:24 +0300
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #4a7cacd](https://github.com/MariaDB/server/commit/4a7cacd)\
  2014-06-25 20:47:54 +0400
  * [MDEV-406](https://jira.mariadb.org/browse/MDEV-406): ANALYZE $stmt: fix "explain UPDATE view problem".
* [Revision #5893ae0](https://github.com/MariaDB/server/commit/5893ae0)\
  2014-06-25 19:04:44 +0300
  * Fix test failure when trying to set compression algorithm to 3
* [Revision #3da81ab](https://github.com/MariaDB/server/commit/3da81ab)\
  2014-06-25 18:35:30 +0400
  * [MDEV-406](https://jira.mariadb.org/browse/MDEV-406): ANALYZE $stmt: more testcases, fix memory leak
* [Revision #424d5de](https://github.com/MariaDB/server/commit/424d5de)\
  2014-06-25 16:46:42 +0400
  * Merge bb-10.1-explain-analyze into 10.1
* [Revision #b561a98](https://github.com/MariaDB/server/commit/b561a98)\
  2014-06-25 16:01:09 +0400
  * [MDEV-406](https://jira.mariadb.org/browse/MDEV-406): ANALYZE $stmt: add some tests for joins
* [Revision #7711999](https://github.com/MariaDB/server/commit/7711999)\
  2014-06-25 15:15:38 +0400
  * [MDEV-406](https://jira.mariadb.org/browse/MDEV-406): ANALYZE $stmt: add support for BNL join buffering
* [Revision #3bca019](https://github.com/MariaDB/server/commit/3bca019)\
  2014-06-25 08:46:54 +0300
  * [MDEV-6361](https://jira.mariadb.org/browse/MDEV-6361): innodb\_compression\_algorithm configuration variable can be set to unsupported value.
* [Revision #c3cfb69](https://github.com/MariaDB/server/commit/c3cfb69)\
  2014-06-24 23:58:13 +0400
  * [MDEV-406](https://jira.mariadb.org/browse/MDEV-406): ANALYZE $stmt: Scans that never executed will have r\_rows=NULL
* [Revision #06a87d7](https://github.com/MariaDB/server/commit/06a87d7)\
  2014-06-24 23:38:49 +0400
  * Fix compile on Windows: use rint() instead of round().
* [Revision #1dd5d31](https://github.com/MariaDB/server/commit/1dd5d31)\
  2014-06-24 22:21:34 +0400
  * [MDEV-406](https://jira.mariadb.org/browse/MDEV-406): ANALYZE $stmt: fix order\_by.test
* [Revision #c08de06](https://github.com/MariaDB/server/commit/c08de06)\
  2014-06-24 19:41:43 +0400
  * [MDEV-406](https://jira.mariadb.org/browse/MDEV-406): ANALYZE $stmt: get ANALYZE work for subqueries
* [Revision #787ec31](https://github.com/MariaDB/server/commit/787ec31)\
  2014-06-23 12:09:00 +0200
  * [MDEV-6248](https://jira.mariadb.org/browse/MDEV-6248) GUI-friendly cmake options to enable/disable plugins
* [Revision #da9bb66](https://github.com/MariaDB/server/commit/da9bb66)\
  2014-06-17 10:59:40 +0200
  * cmake GUI cleanup
* [Revision #242e7f9](https://github.com/MariaDB/server/commit/242e7f9)\
  2014-06-23 16:23:51 +0200
  * [MDEV-4549](https://jira.mariadb.org/browse/MDEV-4549) \[PATCH] Clean up code working with ACL tables
* [Revision #f321d3e](https://github.com/MariaDB/server/commit/f321d3e)\
  2014-06-21 08:56:49 +0200
  * main.temp\_table\_frm failure on fulltest (--embedded, when TMPDIR=/tmp)
* [Revision #ce6a63e](https://github.com/MariaDB/server/commit/ce6a63e)\
  2014-06-20 11:34:24 +0200
  * [MDEV-4260](https://jira.mariadb.org/browse/MDEV-4260) Don't create frm files for temporary tables
* [Revision #cc5b399](https://github.com/MariaDB/server/commit/cc5b399)\
  2014-06-18 11:53:42 +0200
  * remove HTON\_FLUSH\_AFTER\_RENAME (BDB-ism, unused for years)
* [Revision #fb8818c](https://github.com/MariaDB/server/commit/fb8818c)\
  2014-06-17 17:57:18 +0200
  * Fix CMakeLists.txt for cmake Ninja generator
* [Revision #dc64ba2](https://github.com/MariaDB/server/commit/dc64ba2)\
  2014-06-19 12:02:23 +0200
  * [MDEV-6137](https://jira.mariadb.org/browse/MDEV-6137) better help for SET/ENUM sysvars
* [Revision #0cb7c19](https://github.com/MariaDB/server/commit/0cb7c19)\
  2014-06-18 15:00:58 +0200
  * update sys\_vars.innodb\_compression\_algorithm\_basic to pass
* [Revision #5f02051](https://github.com/MariaDB/server/commit/5f02051)\
  2014-06-17 11:33:50 +0300
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #89e0514](https://github.com/MariaDB/server/commit/89e0514)\
  2014-06-17 08:40:54 +0300
  * Fixed test failure introduced by adding a new dynamic configuration variable innodb\_compression\_algorithm. Removed unnecessary test for removed configuration variable.
* [Revision #581b889](https://github.com/MariaDB/server/commit/581b889)\
  2014-06-16 13:34:03 +0400
  * Update analyze\_stmt.result after the last commit
* [Revision #cf1a09e](https://github.com/MariaDB/server/commit/cf1a09e)\
  2014-06-14 22:15:52 +0200
  * [MDEV-6107](https://jira.mariadb.org/browse/MDEV-6107) merge default\_tmp\_storage\_engine
* [Revision #2edcf8f](https://github.com/MariaDB/server/commit/2edcf8f)\
  2014-06-15 12:19:33 +0200
  * .gitignore ninja files
* [Revision #24133e6](https://github.com/MariaDB/server/commit/24133e6)\
  2014-06-14 18:24:22 +0200
  * fix bison warnings (clash != <>)
* [Revision #f61f36b](https://github.com/MariaDB/server/commit/f61f36b)\
  2014-06-13 16:10:25 +0200
  * Merge branch '10.0' into 10.1
* [Revision #2caeda4](https://github.com/MariaDB/server/commit/2caeda4)\
  2014-06-04 14:43:05 +0400
  * Amend "make distclean" message to mention "git clean -Xdf"
* [Revision #917b223](https://github.com/MariaDB/server/commit/917b223)\
  2014-06-03 19:04:59 +0400
  * [MDEV-406](https://jira.mariadb.org/browse/MDEV-406): ANALYZE $stmt - Testcase for ANALYZE UNION - Provide r\_rows for union result.
* [Revision #5621aa3](https://github.com/MariaDB/server/commit/5621aa3)\
  2014-06-03 17:59:01 +0400
  * [MDEV-406](https://jira.mariadb.org/browse/MDEV-406): ANALYZE $stmt - Support tracking for UNIONs, temporary-table based ORDER BYs, and both.
* [Revision #0925ab9](https://github.com/MariaDB/server/commit/0925ab9)\
  2014-05-27 20:16:51 +0400
  * [MDEV-406](https://jira.mariadb.org/browse/MDEV-406): ANALYZE $stmt -Add analyze\_stmt.test/result
* [Revision #eaba1ba](https://github.com/MariaDB/server/commit/eaba1ba)\
  2014-05-27 20:13:17 +0400
  * Re-commit in git: [MDEV-406](https://jira.mariadb.org/browse/MDEV-406): ANALYZE $stmt - Ported the old patch to new explain code - New SQL syntax (ANALYZE $stmt) - ANALYZE UPDATE/DELETE is now supported (because EXPLAIN UPDATE/DELETE is supported) - Basic counters are calculated for basic kinds of queries (still need to see what happens with join buffer, ORDER BY...LIMIT queries, etc)
* [Revision #1e702f3](https://github.com/MariaDB/server/commit/1e702f3)\
  2014-05-27 14:29:05 +0200
  * don't include \<linux/falloc.h> when it's not really needed
* [Revision #5a61516](https://github.com/MariaDB/server/commit/5a61516)\
  2014-05-26 21:14:33 +0200
  * Merge remote-tracking branch 'origin/10.1' into 10.1-serg-merge
* [Revision #6a85b10](https://github.com/MariaDB/server/commit/6a85b10)\
  2014-05-26 21:11:53 +0200
  * merge the compilation fixes from 10.0-FusionIO
* [Revision #4e68faf](https://github.com/MariaDB/server/commit/4e68faf)\
  2014-05-26 20:42:06 +0200
  * compilation failure on Win64
* [Revision #8eaa1d9](https://github.com/MariaDB/server/commit/8eaa1d9)\
  2014-05-26 20:41:10 +0200
  * use ENUM not ULONG for innodb-compression-algorithm command-line option
* [Revision #5035495](https://github.com/MariaDB/server/commit/5035495)\
  2014-05-26 20:31:03 +0200
  * compilation failure on Windows
* [Revision #7e7e1bf](https://github.com/MariaDB/server/commit/7e7e1bf)\
  2014-05-26 20:27:14 +0200
  * don't include the file that 1) not present everywhere 2) not used anyway
* [Revision #9ad97c4](https://github.com/MariaDB/server/commit/9ad97c4)\
  2014-05-26 20:26:51 +0200
  * temporarily disable lzo compression
* [Revision #45d389f](https://github.com/MariaDB/server/commit/45d389f)\
  2014-05-26 20:26:04 +0200
  * lzo.cmake: don't use the same symbol for two different tests
* [Revision #ac4d784](https://github.com/MariaDB/server/commit/ac4d784)\
  2014-05-25 17:20:15 +0200
  * more files in .gitignore
* [Revision #eef1201](https://github.com/MariaDB/server/commit/eef1201)\
  2014-05-25 17:17:50 +0200
  * set version to 10.1.0
* [Revision #c2b9d99](https://github.com/MariaDB/server/commit/c2b9d99)\
  2014-05-25 10:18:07 +0200
  * Merge branch '10.1' of bzr::/usr/home/serg/Abk/mysql into 10.1
* [Revision #1016ee9](https://github.com/MariaDB/server/commit/1016ee9)\
  2014-05-24 21:37:21 +0300
  * Merge 10.0 -> 10.1
* [Revision #a85186d](https://github.com/MariaDB/server/commit/a85186d)\
  2014-05-23 16:40:10 +0200
  * split README into the actual README and third-party licenses
* [Revision #a8e1fa1](https://github.com/MariaDB/server/commit/a8e1fa1)\
  2014-05-22 11:08:14 +0200
  * fix file\_contents to pass with git
* [Revision #3e48269](https://github.com/MariaDB/server/commit/3e48269)\
  2014-05-21 15:30:06 +0200
  * git support in cmake files
* [Revision #05df71a](https://github.com/MariaDB/server/commit/05df71a)\
  2014-05-21 14:50:01 +0200
  * remove support for per-plugin bzr repositories
* [Revision #91128dd](https://github.com/MariaDB/server/commit/91128dd)\
  2014-05-24 12:14:06 +0200
  * remove now-obsolete "5.5+5.6 merge" TODO file
* [Revision #c39a10b](https://github.com/MariaDB/server/commit/c39a10b)\
  2014-05-24 12:13:03 +0200
  * add .gitignore
* [Revision #6d46076](https://github.com/MariaDB/server/commit/6d46076)\
  2014-05-23 08:20:43 +0300
  * Fix compiler warnings.
* [Revision #105060e](https://github.com/MariaDB/server/commit/105060e)\
  2014-05-23 08:10:54 +0300
  * Fix compiler warnings.
* [Revision #76c6cd0](https://github.com/MariaDB/server/commit/76c6cd0)\
  2014-05-22 21:05:35 +0300
  * Fixed compiler error if LZO is not installed.
* [Revision #192790e](https://github.com/MariaDB/server/commit/192790e)\
  2014-05-22 21:03:26 +0300
  * Fix compiler error if LZO is not installed.
* [Revision #a64dace](https://github.com/MariaDB/server/commit/a64dace)\
  2014-05-22 19:48:34 +0300
  * Fixed compiler errors caused by merge error.
* [Revision #ff3f63c](https://github.com/MariaDB/server/commit/ff3f63c)\
  2014-05-22 19:01:41 +0300
  * Fix compiler errors caused by merge error.
* [Revision #b5cdc5a](https://github.com/MariaDB/server/commit/b5cdc5a)\
  2014-05-22 16:31:31 +0300
  * Fix some compiler warnings and small errors on code.
* [Revision #d12dbe7](https://github.com/MariaDB/server/commit/d12dbe7)\
  2014-05-22 14:24:00 +0300
  * [MDEV-6246](https://jira.mariadb.org/browse/MDEV-6246): Merge 10.0.10-FusionIO to 10.1.
* [Revision #972a14b](https://github.com/MariaDB/server/commit/972a14b)\
  2014-05-16 15:30:13 +0300
  * Code cleanup after review.
* [Revision #9d399c9](https://github.com/MariaDB/server/commit/9d399c9)\
  2014-05-13 13:28:57 +0300
  * [MDEV-6075](https://jira.mariadb.org/browse/MDEV-6075): Allow > 16K pages on InnoDB
* [Revision #0eb84da](https://github.com/MariaDB/server/commit/0eb84da)\
  2014-05-08 13:09:15 +0400
  * Merge 10.0 -> 10.1
* [Revision #d6afa80](https://github.com/MariaDB/server/commit/d6afa80)\
  2014-04-28 07:52:41 +0300
  * Fixed small error on compression failure error text.
* [Revision #b186575](https://github.com/MariaDB/server/commit/b186575)\
  2014-04-23 23:14:29 -0700
  * Merge 10.0->10.1
* [Revision #2d340f9](https://github.com/MariaDB/server/commit/2d340f9)\
  2014-04-23 19:23:11 +0300
  * Fixed bug on free buffer space calculation when LZO is used. Fixed bug on function call when InnoDB plugin is used.
* [Revision #271ea3c](https://github.com/MariaDB/server/commit/271ea3c)\
  2014-04-17 08:22:54 +0300
  * Merge lp:maria/10.0 up to mariadb-10.0.10 revision 4140.
* [Revision #2f46e5b](https://github.com/MariaDB/server/commit/2f46e5b)\
  2014-04-16 16:55:36 +0300
  * [MDEV-6070](https://jira.mariadb.org/browse/MDEV-6070): FusionIO: Failure to create a table with ATOMIC\_WRITES option leaves the database in inconsistent state,
* [Revision #13c73c3](https://github.com/MariaDB/server/commit/13c73c3)\
  2014-04-15 14:28:25 +0300
  * Added support for LZO compression method.
* [Revision #88765c3](https://github.com/MariaDB/server/commit/88765c3)\
  2014-03-29 16:51:28 +0200
  * Disable failing test cases that fail because of upstream.
* [Revision #3b61030](https://github.com/MariaDB/server/commit/3b61030)\
  2014-03-28 08:42:53 +0200
  * Fix error on innodb\_mtflush\_threads parameter.
* [Revision #0b92fe9](https://github.com/MariaDB/server/commit/0b92fe9)\
  2014-03-27 12:21:16 +0200
  * Fixed windows compiler errors.
* [Revision #cd8c3b7](https://github.com/MariaDB/server/commit/cd8c3b7)\
  2014-03-27 10:00:30 +0200
  * Fix bug [bug1295268](https://code.launchpad.net/~laurynas-biveinis/percona-server/bug1295268) (Inadequate background LRU flushing for write workloads with InnoDB compression).
* [Revision #5027338](https://github.com/MariaDB/server/commit/5027338)\
  2014-03-27 09:35:24 +0200
  * Fix bug [bug1295268](https://code.launchpad.net/~laurynas-biveinis/percona-server/bug1295268) (Inadequate background LRU flushing for write workloads with InnoDB compression).
* [Revision #f761835](https://github.com/MariaDB/server/commit/f761835)\
  2014-03-25 21:31:27 +0200
  * Fix candidate for XtraDB and row compressed tables.
* [Revision #a81f8fd](https://github.com/MariaDB/server/commit/a81f8fd)\
  2014-03-22 11:30:03 +0200
  * Fix test cases to contain new status variables introduced.
* [Revision #6a756b3](https://github.com/MariaDB/server/commit/6a756b3)\
  2014-03-21 15:46:36 +0200
  * Code cleanup: Removed some unnecessary outputs from standard builds (available on special builds UNIV\_PAGECOMPRESS\_DEBUG and UNIV\_MTFLUSH\_DEBUG).
* [Revision #3ea72a2](https://github.com/MariaDB/server/commit/3ea72a2)\
  2014-03-12 14:47:38 +0200
  * Removed options innodb\_compress\_index\_pages and innodb\_trim\_pct. Both are unnecessary. There is a lot more index pages than there is normal pages. Earlier all pages were compressed and this provided best performance and compression ratio. Added status variable to show how many non index pages are written.
* [Revision #0fcddbc](https://github.com/MariaDB/server/commit/0fcddbc)\
  2014-03-11 13:49:52 +0200
  * Added multi-key unique test case.
* [Revision #4e02c2f](https://github.com/MariaDB/server/commit/4e02c2f)\
  2014-03-11 13:40:29 +0200
  * [MDEV-5335](https://jira.mariadb.org/browse/MDEV-5335): Force PK option. Added a new dynamic configuration variable innodb\_force\_primary\_key default off. If option is true, create table without primary key or unique key where all keyparts are NOT NULL is not accepted. Instead an error message is printed. Variable value can be changed with set global innodb\_force\_primary\_key = .
* [Revision #e7df30b](https://github.com/MariaDB/server/commit/e7df30b)\
  2014-03-11 07:57:54 +0200
  * Merge lp:maria/10.0 up to revision 4040 = [MariaDB 10.0.9](../../old-releases/release-notes-mariadb-10-0-series/mariadb-1009-release-notes.md) RC
* [Revision #c556b9d](https://github.com/MariaDB/server/commit/c556b9d)\
  2014-03-07 08:20:43 +0200
  * Changed so that innodb\_compress\_index pages means that if true also index pages are compressed if false index pages are not compressed.
* [Revision #67cb55c](https://github.com/MariaDB/server/commit/67cb55c)\
  2014-03-07 07:42:28 +0200
  * Merge lp:maria/10.0 up to revision 4032 (10.0.9).
* [Revision #3a4b887](https://github.com/MariaDB/server/commit/3a4b887)\
  2014-03-04 20:12:32 +0200
  * Set index page compression on by default and remove innodb\_trim\_pct as it is not used/implemented.
* [Revision #d64fa1d](https://github.com/MariaDB/server/commit/d64fa1d)\
  2014-03-04 18:56:18 +0200
  * Additional merge to lp:maria/10.0
* [Revision #7322270](https://github.com/MariaDB/server/commit/7322270)\
  2014-03-04 17:14:08 +0200
  * Set actual compressed page size also on read code path to buffer pool so that we can later use it to avoid unnecessary trim operations.
* [Revision #fd38dca](https://github.com/MariaDB/server/commit/fd38dca)\
  2014-03-03 18:14:29 +0200
  * Fixed a hang. The core issues is with the heap-thrashing by the individual queue's. Tried to minimize memory allocation from heap whenever it is unnecessary.
* [Revision #81318f0](https://github.com/MariaDB/server/commit/81318f0)\
  2014-03-03 15:51:54 +0200
  * Yet more windows fixes.
* [Revision #e656a8a](https://github.com/MariaDB/server/commit/e656a8a)\
  2014-03-03 15:43:38 +0200
  * Fix windows os\_file\_write.
* [Revision #b8e0bc3](https://github.com/MariaDB/server/commit/b8e0bc3)\
  2014-03-03 15:26:58 +0200
  * Additional windows fixes.
* [Revision #6cde211](https://github.com/MariaDB/server/commit/6cde211)\
  2014-03-03 15:15:00 +0200
  * Fix typo.
* [Revision #ec45160](https://github.com/MariaDB/server/commit/ec45160)\
  2014-03-03 15:02:39 +0200
  * Fix windows compiler erros.
* [Revision #be50724](https://github.com/MariaDB/server/commit/be50724)\
  2014-03-03 14:45:45 +0200
  * Fix compiler error on windows.
* [Revision #96100d6](https://github.com/MariaDB/server/commit/96100d6)\
  2014-03-03 14:27:56 +0200
  * Merge: lp:maria/10.0 latest.
* [Revision #b67892c](https://github.com/MariaDB/server/commit/b67892c)\
  2014-03-03 12:34:33 +0200
  * Turn all new features off by default.
* [Revision #e667c0f](https://github.com/MariaDB/server/commit/e667c0f)\
  2014-02-28 09:05:36 +0200
  * Fix compiler error.
* [Revision #c88a0d4](https://github.com/MariaDB/server/commit/c88a0d4)\
  2014-02-28 08:53:09 +0200
  * Temporal fix for flush thread hang.
* [Revision #b620e73](https://github.com/MariaDB/server/commit/b620e73)\
  2014-02-26 19:00:24 +0200
  * Small fixes to work\_item handling.
* [Revision #24235e9](https://github.com/MariaDB/server/commit/24235e9)\
  2014-02-25 13:15:55 +0200
  * Fixed memory leak on queue nodes by using local memory heap on normal execution and global memory heap on shutdown.
* [Revision #38471a6](https://github.com/MariaDB/server/commit/38471a6)\
  2014-02-21 12:51:03 +0200
  * Remove incorrect trim\_len calculation. We have already alligned actual page data write.
* [Revision #3c77143](https://github.com/MariaDB/server/commit/3c77143)\
  2014-02-21 10:20:18 +0200
  * Write size was not correctly alligned to SECT\_SIZE. This lead to situation where trim corrupted the database. Fixed the issue and added temporal guards against unalligned write/trim.
* [Revision #fc86a1f](https://github.com/MariaDB/server/commit/fc86a1f)\
  2014-02-20 09:28:18 +0200
  * Make tokudb working with 10.1
* [Revision #24bc031](https://github.com/MariaDB/server/commit/24bc031)\
  2014-02-19 20:25:55 +0200
  * Removed unnecessary memory initialization of page compressed buffer and added guard against unalligned trim size.
* [Revision #2531803](https://github.com/MariaDB/server/commit/2531803)\
  2014-02-15 09:51:06 +0200
  * Fixed hang seen on TPC-C measure phase. We should not use timedwait on threads waiting for a job. They should sleep and let other threads to their work. At shutdown, we know that we put "work" and that is handled as soon as possible.
* [Revision #cae21c5](https://github.com/MariaDB/server/commit/cae21c5)\
  2014-02-14 15:02:26 +0200
  * Fix timing on queues, this could clearly lead to starvation.
* [Revision #9c61466](https://github.com/MariaDB/server/commit/9c61466)\
  2014-02-13 12:35:37 +0200
  * Fixed compiler warnings.
* [Revision #dfc2950](https://github.com/MariaDB/server/commit/dfc2950)\
  2014-02-13 12:23:55 +0200
  * Fixed small issue with dictionary.
* [Revision #d17ecff](https://github.com/MariaDB/server/commit/d17ecff)\
  2014-02-13 09:13:56 +0200
  * Fixed issue on data dictionary corruption. Fixed issue on multi-threaded flush at shutdown. Removed unnecessary startup option innodb\_compress\_pages. Added a new startup option innodb\_mtflush\_threads, default 8.
* [Revision #da927da](https://github.com/MariaDB/server/commit/da927da)\
  2014-02-12 18:00:03 +0200
  * Fixed issue on atomic writes and system tables. Atomic writes can be used also on system tables but not per table.
* [Revision #1fa19bf](https://github.com/MariaDB/server/commit/1fa19bf)\
  2014-02-12 12:52:34 +0200
  * Fixed issue on atomic writes setup and atomic blobs setup on system tables.
* [Revision #f6ad325](https://github.com/MariaDB/server/commit/f6ad325)\
  2014-02-12 10:55:45 +0200
  * Code cleanup. Removed those questions that are now addressed.
* [Revision #184e302](https://github.com/MariaDB/server/commit/184e302)\
  2014-02-12 07:09:06 +0200
  * Fix compiler error if lz4 is not found on the system.
* [Revision #fa9f5f6](https://github.com/MariaDB/server/commit/fa9f5f6)\
  2014-02-11 20:05:09 +0200
  * Removed unnecessary files and set lz4 under HAVE\_LZ4 compiler option using cmake find\_library. Fixed bunch of compiler warnings.
* [Revision #a5cf3a8](https://github.com/MariaDB/server/commit/a5cf3a8)\
  2014-02-07 15:31:31 +0200
  * Merged latest mt-flush code to xtradb. Cleaned up thread statistic output code.
* [Revision #18353c6](https://github.com/MariaDB/server/commit/18353c6)\
  2014-02-06 17:49:55 +0200
  * Fixed issue on file space extension. File space should be extended from current offset to desired size if posix\_fallocate is used.
* [Revision #7f3950a](https://github.com/MariaDB/server/commit/7f3950a)\
  2014-02-06 17:25:26 +0200
  * Moved mt-flush code to buf0mtflu.\[cc|h] and cleaned it up. This is for InnoDB.
* [Revision #195e089](https://github.com/MariaDB/server/commit/195e089)\
  2014-02-06 00:14:15 +0400
  * Change version number to 10.1
* [Revision #921d87d](https://github.com/MariaDB/server/commit/921d87d)\
  2014-02-05 15:32:29 +0200
  * Fixed issue on xtradb shutdown merge error. Multi-threaded flush threads where not shut down properly.
* [Revision #862b034](https://github.com/MariaDB/server/commit/862b034)\
  2014-02-04 20:08:59 +0200
  * Fixed compiler errors.
* [Revision #55fab3d](https://github.com/MariaDB/server/commit/55fab3d)\
  2014-02-04 14:52:02 +0200
  * Fixed issue on atomic writes on startup, removed incorrect assert.
* [Revision #8c5d5bc](https://github.com/MariaDB/server/commit/8c5d5bc)\
  2014-02-03 10:08:15 +0200
  * Fixed merge error on InnoDB page compression level handling.
* [Revision #febe99e](https://github.com/MariaDB/server/commit/febe99e)\
  2014-01-27 13:00:36 +0200
  * Merge lp:maria/10.0 10.0.7 revision 3961
* [Revision #58ce551](https://github.com/MariaDB/server/commit/58ce551)\
  2014-01-13 15:02:31 +0200
  * Removed some unnecessary assertions to debug build and enhanced the page\_compression and page\_compression\_level fetch.
* [Revision #ec82572](https://github.com/MariaDB/server/commit/ec82572)\
  2014-01-10 12:11:36 +0200
  * Enhancement: Change atomic\_writes table option to enum type. Now every file can either use atomic writes, not use it or use default.
* [Revision #2b5a0a2](https://github.com/MariaDB/server/commit/2b5a0a2)\
  2014-01-09 12:33:29 +0200
  * Feature: In first write if we trim we set write\_size to actual bytes written and rest of the page is trimmed. In following writes there is no need to trim again if write\_size only increases because rest of the page is already trimmed. If actual write size decreases we need to trim again. Need to research if this can happen frequently enough to make any effect.
* [Revision #e80f246](https://github.com/MariaDB/server/commit/e80f246)\
  2014-01-09 08:30:09 +0200
  * Fixed issues with atomic writes and compressed pages.
* [Revision #f6a1965](https://github.com/MariaDB/server/commit/f6a1965)\
  2013-12-20 08:59:34 +0200
  * Temporally disable posix\_fallocate on os\_file\_set\_size because currently Fusion-io SSD drive does not support setting file size without fysically writing pages with zeroes when fallocate with PUCH\_HOLE is used.
* [Revision #f023715](https://github.com/MariaDB/server/commit/f023715)\
  2013-12-20 06:50:58 +0200
  * Need to disable fast file extension with posix\_fallocate for Fusion-io currently.
* [Revision #9ba5909](https://github.com/MariaDB/server/commit/9ba5909)\
  2013-12-19 18:04:26 +0200
  * Atomic writes require also atomic\_blobs. Add that missing flag to dictionary setting and from there it will be stored to table space.
* [Revision #5e55d1c](https://github.com/MariaDB/server/commit/5e55d1c)\
  2013-12-19 14:36:38 +0200
  * Changes for Fusion-io multi-threaded flush, page compressed tables and tables using atomic write/table.
* [Revision #1f4f425](https://github.com/MariaDB/server/commit/1f4f425)\
  2013-12-06 19:02:55 +0400
  * [MDEV-5297](https://jira.mariadb.org/browse/MDEV-5297) TIME(0), TIMESTAMP(0) and DATETIME(0) are self-incompatible during replication (upstream) Fixed.
* [Revision #0afd292](https://github.com/MariaDB/server/commit/0afd292)\
  2013-12-05 16:54:50 +0400
  * Fixing an MSVC warning about double "const" data type qualifier in the code merged from MySQL-5.6:

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
