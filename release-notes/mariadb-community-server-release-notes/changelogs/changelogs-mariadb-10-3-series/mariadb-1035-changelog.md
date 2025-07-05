# MariaDB 10.3.5 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/release-notes-mariadb-10-3-series/mariadb-10-3-39-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.5)[Release Notes](../../old-releases/release-notes-mariadb-10-3-series/mariadb-1035-release-notes.md)[Changelog](mariadb-1035-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 26 Feb 2018

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-3-series/mariadb-1035-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #583eb96c24](https://github.com/MariaDB/server/commit/583eb96c24)\
  2017-08-18 23:36:42 +0400
  * [MDEV-11952](https://jira.mariadb.org/browse/MDEV-11952) Oracle-style packages: stage#5
* [Revision #83ea839fb1](https://github.com/MariaDB/server/commit/83ea839fb1)\
  2018-02-25 13:58:16 +0100
  * [MDEV-15405](https://jira.mariadb.org/browse/MDEV-15405) Mixed replication fails with "Could not execute Delete\_rows\_v1 event" upon DELETE HISTORY
* [Revision #ac2d4d49a0](https://github.com/MariaDB/server/commit/ac2d4d49a0)\
  2018-02-25 12:55:12 +0100
  * fix THD::system\_time to follow, well, system time
* [Revision #30981dcf56](https://github.com/MariaDB/server/commit/30981dcf56)\
  2018-02-24 21:53:33 +0100
  * cleanup: remove redundant vers\_field->set\_notnull();
* [Revision #8936b17510](https://github.com/MariaDB/server/commit/8936b17510)\
  2018-02-24 14:43:26 +0100
  * update server maturity
* [Revision #9b59f78d16](https://github.com/MariaDB/server/commit/9b59f78d16)\
  2018-02-24 09:45:46 +0100
  * [MDEV-15395](https://jira.mariadb.org/browse/MDEV-15395) Wrong result or Assertion \`old\_part\_id == m\_last\_part' failed in ha\_partition::update\_row on slave
* [Revision #ad0f8fef3d](https://github.com/MariaDB/server/commit/ad0f8fef3d)\
  2018-02-24 09:18:42 +0100
  * fixes for test failures
* [Revision #8f9c64000e](https://github.com/MariaDB/server/commit/8f9c64000e)\
  2018-02-23 20:00:32 +0100
  * [MDEV-15336](https://jira.mariadb.org/browse/MDEV-15336) Server crashes in handler::print\_error / ha\_partition::print\_error upon query timeout
* [Revision #22073cbf3b](https://github.com/MariaDB/server/commit/22073cbf3b)\
  2018-02-23 20:33:48 +0100
  * omit system invisible fields from the duplicate key error
* [Revision #5c7a40e3cf](https://github.com/MariaDB/server/commit/5c7a40e3cf)\
  2018-02-23 20:22:09 +0100
  * [MDEV-15330](https://jira.mariadb.org/browse/MDEV-15330) Server crash or assertion \`table->insert\_values' failure in write\_record upon LOAD DATA
* [Revision #fd240a10e3](https://github.com/MariaDB/server/commit/fd240a10e3)\
  2018-02-23 19:05:17 +0100
  * [MDEV-15395](https://jira.mariadb.org/browse/MDEV-15395) Wrong result or Assertion \`old\_part\_id == m\_last\_part' failed in ha\_partition::update\_row on slave
* [Revision #485325e7e3](https://github.com/MariaDB/server/commit/485325e7e3)\
  2018-02-23 13:42:34 +0100
  * don't allow TIMESTAMP(6) versioning and FK with CASCADE or SET NULL
* [Revision #794f71cbc4](https://github.com/MariaDB/server/commit/794f71cbc4)\
  2018-02-23 13:41:46 +0100
  * create a reusable function that tells what FK actions can write
* [Revision #17f8e0ecdf](https://github.com/MariaDB/server/commit/17f8e0ecdf)\
  2018-02-23 12:51:43 +0100
  * unify error messages a bit
* [Revision #5282d0dce1](https://github.com/MariaDB/server/commit/5282d0dce1)\
  2018-02-23 11:40:24 +0100
  * cleanup: use enum, not uint, for enum variables
* [Revision #d717fe76e1](https://github.com/MariaDB/server/commit/d717fe76e1)\
  2018-02-23 03:04:46 +0200
  * Adjust test results to reflect the new system table
* [Revision #f3088112cb](https://github.com/MariaDB/server/commit/f3088112cb)\
  2018-02-22 01:24:02 +0100
  * [MDEV-14645](https://jira.mariadb.org/browse/MDEV-14645): AS OF TIMESTAMP is misused as TRX\_ID
* [Revision #33366b1098](https://github.com/MariaDB/server/commit/33366b1098)\
  2018-02-22 01:09:01 +0100
  * remove @@system\_versioning\_innodb\_algorithm\_simple
* [Revision #b9c70b889c](https://github.com/MariaDB/server/commit/b9c70b889c)\
  2018-02-22 00:57:49 +0100
  * remove always-false variable
* [Revision #5fb08323e1](https://github.com/MariaDB/server/commit/5fb08323e1)\
  2018-02-16 11:34:52 +0300
  * Tests: versioning.foreign check row\_end after constraint execution
* [Revision #052668f500](https://github.com/MariaDB/server/commit/052668f500)\
  2018-02-21 21:45:59 +0100
  * simplify versioning tests
* [Revision #dd7d169593](https://github.com/MariaDB/server/commit/dd7d169593)\
  2018-02-14 17:02:11 +0300
  * [MDEV-14767](https://jira.mariadb.org/browse/MDEV-14767) system\_versioning\_alter\_history breaks ALTER replication
* [Revision #3f4d03b0dd](https://github.com/MariaDB/server/commit/3f4d03b0dd)\
  2018-02-13 21:36:14 +0300
  * Tests: partitioning cases for duplicate bugs
* [Revision #68c994436a](https://github.com/MariaDB/server/commit/68c994436a)\
  2018-02-21 19:01:13 +0100
  * [MDEV-15168](https://jira.mariadb.org/browse/MDEV-15168) Unexpected ER\_VERS\_ENGINE\_UNSUPPORTED upon dropping versioning on a partitioned table
* [Revision #f685604aaa](https://github.com/MariaDB/server/commit/f685604aaa)\
  2018-02-21 18:34:37 +0100
  * [MDEV-15103](https://jira.mariadb.org/browse/MDEV-15103) Assertion in ha\_partition::part\_records() for updating VIEW
* [Revision #62b5427394](https://github.com/MariaDB/server/commit/62b5427394)\
  2018-02-21 18:26:22 +0100
  * cannot rotate both by INTERVAL and LIMIT
* [Revision #dfb6f96eaf](https://github.com/MariaDB/server/commit/dfb6f96eaf)\
  2018-02-21 18:14:04 +0100
  * [MDEV-15190](https://jira.mariadb.org/browse/MDEV-15190) Bad error for non-versioned table PARTITION BY SYSTEM\_TIME
* [Revision #edeeaac451](https://github.com/MariaDB/server/commit/edeeaac451)\
  2018-02-02 15:01:53 +0300
  * [MDEV-14829](https://jira.mariadb.org/browse/MDEV-14829) Assertion \`0' failed in Protocol::end\_statement upon concurrent UPDATE
* [Revision #75afaa7e00](https://github.com/MariaDB/server/commit/75afaa7e00)\
  2018-01-22 17:10:19 +0300
  * [MDEV-15001](https://jira.mariadb.org/browse/MDEV-15001) no tests for system\_versioning\_innodb\_algorithm\_simple
* [Revision #e36c5ec0a5](https://github.com/MariaDB/server/commit/e36c5ec0a5)\
  2018-02-21 15:16:19 +0100
  * PARTITION BY SYSTEM\_TIME INTERVAL ...
* [Revision #7961bc4b89](https://github.com/MariaDB/server/commit/7961bc4b89)\
  2018-02-19 15:53:31 +0100
  * helper append\_interval(String\*)
* [Revision #7e2c686b3f](https://github.com/MariaDB/server/commit/7e2c686b3f)\
  2018-02-21 15:16:45 +0100
  * remove partition-specific methods from the base handler class
* [Revision #4ff089489b](https://github.com/MariaDB/server/commit/4ff089489b)\
  2018-02-21 14:53:16 +0100
  * create ROW\_START/ROW\_END columns NOT NULL
* [Revision #c4c81a5b04](https://github.com/MariaDB/server/commit/c4c81a5b04)\
  2018-02-18 12:24:51 +0100
  * cleanup: partition\_info::check\_constants
* [Revision #f38ef43013](https://github.com/MariaDB/server/commit/f38ef43013)\
  2018-02-17 14:49:42 +0100
  * cleanup: remove \*.opt files from the versioning suite
* [Revision #f1bd02d994](https://github.com/MariaDB/server/commit/f1bd02d994)\
  2018-02-16 19:07:32 +0100
  * [MDEV-15004](https://jira.mariadb.org/browse/MDEV-15004) parser greedily parses AS OF TIMESTAMP
* [Revision #e2f70d6e10](https://github.com/MariaDB/server/commit/e2f70d6e10)\
  2018-01-27 13:44:34 +0300
  * Vers SQL: Refactoring: better init of vers\_conditions
* [Revision #df0e1817c7](https://github.com/MariaDB/server/commit/df0e1817c7)\
  2018-01-26 12:46:14 +0300
  * Vers SQL: partition rotation by INTERVAL fix
* [Revision #45e1c9bb6d](https://github.com/MariaDB/server/commit/45e1c9bb6d)\
  2018-02-15 21:34:01 +0100
  * cleanup: remove a pretty formatting function from a test
* [Revision #9fa715b84d](https://github.com/MariaDB/server/commit/9fa715b84d)\
  2018-01-18 06:28:37 +0300
  * [MDEV-14798](https://jira.mariadb.org/browse/MDEV-14798) Add, drop system versioning semantic and syntax
* [Revision #9f6a7ed2d7](https://github.com/MariaDB/server/commit/9f6a7ed2d7)\
  2018-02-15 17:13:48 +0100
  * SQL: Truncate history of partitioned table \[fixes #399, closes #403]
* [Revision #187a163c78](https://github.com/MariaDB/server/commit/187a163c78)\
  2018-02-15 16:26:31 +0100
  * cleanup: ha\_partition::update\_row/delete\_row
* [Revision #221d010f3e](https://github.com/MariaDB/server/commit/221d010f3e)\
  2018-02-15 13:31:22 +0100
  * [MDEV-14789](https://jira.mariadb.org/browse/MDEV-14789) Creating federated table on versioned table fails
* [Revision #5f6b3f9c07](https://github.com/MariaDB/server/commit/5f6b3f9c07)\
  2018-02-14 19:15:05 +0100
  * [MDEV-13982](https://jira.mariadb.org/browse/MDEV-13982) Server crashes in ha\_partition::engine\_name
* [Revision #ce0e2c82af](https://github.com/MariaDB/server/commit/ce0e2c82af)\
  2018-02-13 17:17:35 +0100
  * Fix a typo
* Merge [Revision #2732fcc608](https://github.com/MariaDB/server/commit/2732fcc608) 2018-02-23 08:43:34 +0100 - Merge branch 'bb-10.2-ext' into 10.3
* Merge [Revision #b8af22af15](https://github.com/MariaDB/server/commit/b8af22af15) 2018-02-22 19:29:52 +0100 - Merge branch '10.2' into bb-10.2-ext
* [Revision #e92cc09765](https://github.com/MariaDB/server/commit/e92cc09765)\
  2018-02-22 15:58:07 +0100
  * [MDEV-15345](https://jira.mariadb.org/browse/MDEV-15345) Compilation fails to build my\_addr\_resolve.c
* Merge [Revision #e4a73acc63](https://github.com/MariaDB/server/commit/e4a73acc63) 2018-02-22 14:15:24 +0100 - Merge branch '10.1' into 10.2
* Merge [Revision #a04e4f531a](https://github.com/MariaDB/server/commit/a04e4f531a) 2018-02-22 14:12:02 +0100 - Merge branch '10.0' into 10.1
* Merge [Revision #b728641e86](https://github.com/MariaDB/server/commit/b728641e86) 2018-02-22 09:22:03 +0100 - Merge branch '5.5' into 10.0
* [Revision #7bd258c44c](https://github.com/MariaDB/server/commit/7bd258c44c)\
  2018-02-15 10:06:14 +0100
  * fix plugins.server\_audit test for --ps
* [Revision #03de234baf](https://github.com/MariaDB/server/commit/03de234baf)\
  2018-02-14 19:12:23 +0100
  * [MDEV-13982](https://jira.mariadb.org/browse/MDEV-13982) Server crashes in ha\_partition::engine\_name
* [Revision #2709380587](https://github.com/MariaDB/server/commit/2709380587)\
  2018-02-14 18:14:24 +0100
  * [MDEV-13748](https://jira.mariadb.org/browse/MDEV-13748) Assertion \`status\_var.local\_memory\_used == 0 || !debug\_assert\_on\_not\_freed\_memory' failed in virtual THD::THD after query with INTERSECT
* [Revision #c8afe7daac](https://github.com/MariaDB/server/commit/c8afe7daac)\
  2018-02-05 14:13:26 +0100
  * cleanup: remove a duplicated test case
* [Revision #7c6cf7fefe](https://github.com/MariaDB/server/commit/7c6cf7fefe)\
  2018-01-25 14:25:48 +0100
  * bug: ha\_heap was unilaterally increasing reclength
* [Revision #88d1c1c551](https://github.com/MariaDB/server/commit/88d1c1c551)\
  2018-02-12 15:12:49 +0100
  * [MDEV-15288](https://jira.mariadb.org/browse/MDEV-15288) Configure errors when building without INNOBASE
* [Revision #504beb1325](https://github.com/MariaDB/server/commit/504beb1325)\
  2018-02-22 12:20:46 +0200
  * Add supressions for possible warning.
* [Revision #e119799a92](https://github.com/MariaDB/server/commit/e119799a92)\
  2018-02-22 08:40:54 +0100
  * fix compilation wih -DPLUGIN\_PARTITION=NO
* Merge [Revision #2daa005800](https://github.com/MariaDB/server/commit/2daa005800) 2018-02-22 08:39:24 +0100 - Merge branch '10.1' into 10.2
* [Revision #5d8ac1ece1](https://github.com/MariaDB/server/commit/5d8ac1ece1)\
  2018-02-14 13:30:52 +0100
  * log all mtr output in vardir/log/stdout.log
* [Revision #50359719f0](https://github.com/MariaDB/server/commit/50359719f0)\
  2018-02-14 12:35:47 +0100
  * fix compilation -DWITH\_PERFSCHEMA=NO
* [Revision #18455ec3f1](https://github.com/MariaDB/server/commit/18455ec3f1)\
  2018-02-14 12:35:12 +0100
  * fix compilation wih -DPLUGIN\_PARTITION=NO
* [Revision #4e6dab94d0](https://github.com/MariaDB/server/commit/4e6dab94d0)\
  2018-02-21 19:38:57 +0530
  * [MDEV-15254](https://jira.mariadb.org/browse/MDEV-15254) - 10.1.31 does not join an existing cluster with SST xtrabackup-v2
* [Revision #56d6776524](https://github.com/MariaDB/server/commit/56d6776524)\
  2018-02-20 20:03:23 +0000
  * Windows : remove freopen(), "to keep fd = 0 busy".
* [Revision #c3a3b77f9a](https://github.com/MariaDB/server/commit/c3a3b77f9a)\
  2018-02-20 09:27:31 +0200
  * Disable failing Galera tests:
* [Revision #3a7126cbb7](https://github.com/MariaDB/server/commit/3a7126cbb7)\
  2018-02-20 09:17:29 +0200
  * Disable galera\_gtid until 1047: WSREP has not yet prepared node for application use is fixed.
* [Revision #b697f213a7](https://github.com/MariaDB/server/commit/b697f213a7)\
  2018-02-19 13:53:35 +0400
  * [MDEV-14541](https://jira.mariadb.org/browse/MDEV-14541) - Workaround GCC ICE on ARM64
* [Revision #7a84688e2c](https://github.com/MariaDB/server/commit/7a84688e2c)\
  2018-02-18 07:47:47 +0200
  * [MDEV-14814](https://jira.mariadb.org/browse/MDEV-14814): encryption.innodb\_encryption-page-compression failed in buildbot with timeout on wait condition
* [Revision #9ea3ad6d75](https://github.com/MariaDB/server/commit/9ea3ad6d75)\
  2018-02-18 07:32:19 +0200
  * Disable failing test.
* [Revision #0e8cb572f1](https://github.com/MariaDB/server/commit/0e8cb572f1)\
  2018-02-17 15:18:14 +0200
  * Fix innodb\_encryption-page-compression test by force flushing dirty pages.
* [Revision #55bc3f1dd9](https://github.com/MariaDB/server/commit/55bc3f1dd9)\
  2018-02-17 18:04:06 +0200
  * Fixed performance problem with Aria in find\_head()
* [Revision #965e16376c](https://github.com/MariaDB/server/commit/965e16376c)\
  2018-02-17 17:48:23 +0200
  * TokuDB didn't compile with valgrind
* [Revision #f853b8ed26](https://github.com/MariaDB/server/commit/f853b8ed26)\
  2018-02-17 17:47:18 +0200
  * partition\_alter\_myisam produces warning if no symlink support
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
* [Revision #868bca5c4f](https://github.com/MariaDB/server/commit/868bca5c4f)\
  2018-02-20 10:19:55 +1100
  * [MDEV-15356](https://jira.mariadb.org/browse/MDEV-15356): tp\_timeout\_handler needs to call set\_killed\_no\_mutex as it has the mutex
* [Revision #23d7b77358](https://github.com/MariaDB/server/commit/23d7b77358)\
  2018-02-21 18:22:43 +0000
  * Fix truncation warning on Windows.
* [Revision #144c7f8b6e](https://github.com/MariaDB/server/commit/144c7f8b6e)\
  2018-02-21 13:11:04 +0400
  * Adding Field\_timestamp::sql\_mode\_for\_timestamp() to reuse duplicate code
* [Revision #5417002dae](https://github.com/MariaDB/server/commit/5417002dae)\
  2018-02-21 08:18:44 +0400
  * A cleanup for [MDEV-15340](https://jira.mariadb.org/browse/MDEV-15340) + fix [MDEV-15363](https://jira.mariadb.org/browse/MDEV-15363) Wrong result for CAST(LAST\_DAY(TIME'00:00:00') AS TIME)
* [Revision #aef530bb69](https://github.com/MariaDB/server/commit/aef530bb69)\
  2018-02-19 23:41:01 +0400
  * [MDEV-15340](https://jira.mariadb.org/browse/MDEV-15340) Wrong result HOUR(case\_expression\_with\_time\_and\_datetime)
* [Revision #5c3d0c6bad](https://github.com/MariaDB/server/commit/5c3d0c6bad)\
  2018-02-15 10:19:05 +0100
  * apply XA RECOVER FORMAT=... from [MDEV-14593](https://jira.mariadb.org/browse/MDEV-14593) to Oracle parser variant, too
* [Revision #131d9a5d0c](https://github.com/MariaDB/server/commit/131d9a5d0c)\
  2018-02-22 20:46:42 +0400
  * Allocate lock\_sys statically
* Merge [Revision #59dd0464a9](https://github.com/MariaDB/server/commit/59dd0464a9) 2018-02-23 08:17:23 +0200 - [MDEV-11455](https://jira.mariadb.org/browse/MDEV-11455) shutdown or abort during innodb buffer pool load (from file) causing incomplete save
* [Revision #9b8d0d9ff9](https://github.com/MariaDB/server/commit/9b8d0d9ff9)\
  2016-12-06 16:39:23 +1100
  * [MDEV-11455](https://jira.mariadb.org/browse/MDEV-11455): test case for status variable innodb\_buffer\_pool\_load\_incomplete
* [Revision #8440e8fa98](https://github.com/MariaDB/server/commit/8440e8fa98)\
  2016-10-06 15:16:18 +0200
  * [MDEV-11455](https://jira.mariadb.org/browse/MDEV-11455): create status variable innodb\_buffer\_pool\_load\_incomplete
* [Revision #907b236112](https://github.com/MariaDB/server/commit/907b236112)\
  2018-02-22 10:08:49 -0800
  * Fixed [MDEV-14883](https://jira.mariadb.org/browse/MDEV-14883) Usage of EXCEPT and INTERSECT in recursive CTE is not supported
* [Revision #988ec800ed](https://github.com/MariaDB/server/commit/988ec800ed)\
  2018-02-22 12:20:00 +0400
  * [MDEV-15155](https://jira.mariadb.org/browse/MDEV-15155) - ReadView::is\_open() assertion failure
* [Revision #a8656d58d4](https://github.com/MariaDB/server/commit/a8656d58d4)\
  2018-02-22 09:49:50 +0200
  * Fix the startup with innodb\_force\_recovery=5
* [Revision #fb335b48b5](https://github.com/MariaDB/server/commit/fb335b48b5)\
  2018-02-22 09:30:41 +0200
  * Allocate purge\_sys statically
* [Revision #a3a2b898a0](https://github.com/MariaDB/server/commit/a3a2b898a0)\
  2018-02-22 09:18:53 +0200
  * Cleanup: Do not pass globals as parameters
* [Revision #fe0e263e6d](https://github.com/MariaDB/server/commit/fe0e263e6d)\
  2018-02-21 19:02:32 +0200
  * [MDEV-15370](https://jira.mariadb.org/browse/MDEV-15370) Upgrade fails when both insert\_undo and update\_undo exist
* [Revision #6a370e4301](https://github.com/MariaDB/server/commit/6a370e4301)\
  2018-02-21 18:04:25 +0200
  * Refactor TrxUndoRsegsIterator for further simplification
* [Revision #6ae7fa6878](https://github.com/MariaDB/server/commit/6ae7fa6878)\
  2018-02-21 16:15:20 +0200
  * Simplify TrxUndoRsegs
* [Revision #d4187bdc51](https://github.com/MariaDB/server/commit/d4187bdc51)\
  2018-02-21 12:54:33 +0200
  * Replace purge\_iter\_t with purge\_sys\_t::iterator
* [Revision #28d844fd07](https://github.com/MariaDB/server/commit/28d844fd07)\
  2018-02-21 11:53:41 +0200
  * Rename the purge\_sys\_t iterators
* Merge [Revision #7bfe33ee28](https://github.com/MariaDB/server/commit/7bfe33ee28) 2018-02-21 19:15:20 +0200 - [MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814) innodb large allocations - Don't dump
* [Revision #094cf73045](https://github.com/MariaDB/server/commit/094cf73045)\
  2018-02-21 09:46:51 +0200
  * Avoid some dead code
* [Revision #b600f30786](https://github.com/MariaDB/server/commit/b600f30786)\
  2017-04-25 16:49:27 +1000
  * [MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814): Innodb large allocations - madvise - Don't dump
* [Revision #8f50a26eb7](https://github.com/MariaDB/server/commit/8f50a26eb7)\
  2018-02-20 10:19:55 +1100
  * [MDEV-15356](https://jira.mariadb.org/browse/MDEV-15356): tp\_timeout\_handler needs to call set\_killed\_no\_mutex as it has the mutex
* [Revision #e2ac8d3ff1](https://github.com/MariaDB/server/commit/e2ac8d3ff1)\
  2018-02-21 16:33:55 +0000
  * Windows : Fix /permissive- compile error
* [Revision #56e7b7eaed](https://github.com/MariaDB/server/commit/56e7b7eaed)\
  2018-02-20 21:17:36 +0000
  * Make possible to use clang on Windows (clang-cl) -DWITH\_ASAN can be used as well now, on x64
* [Revision #9d97e6010e](https://github.com/MariaDB/server/commit/9d97e6010e)\
  2018-02-14 00:19:38 +0200
  * [MDEV-14835](https://jira.mariadb.org/browse/MDEV-14835) Server crashes in Field\_iterator\_table::create\_item when number of elements of BIGINT or YEAR type in the IN list reaches in\_predicate\_conversion\_threshold
* [Revision #947efe17ed](https://github.com/MariaDB/server/commit/947efe17ed)\
  2018-02-20 15:10:03 +0200
  * [MDEV-15158](https://jira.mariadb.org/browse/MDEV-15158) On commit, do not write to the TRX\_SYS page
* Merge [Revision #f6544353e0](https://github.com/MariaDB/server/commit/f6544353e0) 2018-02-20 15:08:16 +0200 - Pull request #625: ASAN unpoison system versioning related buffer
* [Revision #d4822bef04](https://github.com/MariaDB/server/commit/d4822bef04)\
  2018-02-20 15:09:31 +0300
  * remove uint
* [Revision #8ed9ef54f9](https://github.com/MariaDB/server/commit/8ed9ef54f9)\
  2018-02-20 13:50:23 +0300
  * ASAN unpoison system versioning related buffer
* [Revision #cd63f43c40](https://github.com/MariaDB/server/commit/cd63f43c40)\
  2018-02-20 13:08:43 +0200
  * Fix the Windows build
* [Revision #1fa14a7c08](https://github.com/MariaDB/server/commit/1fa14a7c08)\
  2018-02-20 10:16:52 +0200
  * Replace trx\_undo\_mem\_free() with ut\_free()
* [Revision #60a68fdf71](https://github.com/MariaDB/server/commit/60a68fdf71)\
  2018-02-20 10:02:42 +0200
  * Clarify the access to trx\_sys.rseg\_history\_len
* [Revision #d23fcc427c](https://github.com/MariaDB/server/commit/d23fcc427c)\
  2018-02-19 23:29:51 +0400
  * [MDEV-14593](https://jira.mariadb.org/browse/MDEV-14593) human-readable XA RECOVER.
* Merge [Revision #5521994ce2](https://github.com/MariaDB/server/commit/5521994ce2) 2018-02-19 11:37:45 +0200 - Pull request #614: various small code changes
* [Revision #f02f1eda7e](https://github.com/MariaDB/server/commit/f02f1eda7e)\
  2018-02-16 22:15:51 +0300
  * review fixes
* [Revision #6de8f79b11](https://github.com/MariaDB/server/commit/6de8f79b11)\
  2018-02-14 14:55:46 +0300
  * remove unneeded variable
* [Revision #de4c9f460c](https://github.com/MariaDB/server/commit/de4c9f460c)\
  2018-02-13 23:29:51 +0300
  * change some ibool to bool
* [Revision #e14790b89d](https://github.com/MariaDB/server/commit/e14790b89d)\
  2018-02-13 23:22:20 +0300
  * let buf\_page\_hash\_lock\_get() be function, not macro
* [Revision #365f478240](https://github.com/MariaDB/server/commit/365f478240)\
  2018-02-13 23:08:38 +0300
  * make buf\_block\_t::lock\_hash\_val uint32\_t
* [Revision #af2d260b37](https://github.com/MariaDB/server/commit/af2d260b37)\
  2018-02-13 23:02:46 +0300
  * merge btr\_page\_get\_level\_low() and btr\_page\_get\_level()
* [Revision #9d46bd8a24](https://github.com/MariaDB/server/commit/9d46bd8a24)\
  2018-02-13 22:48:32 +0300
  * flst\_add\_to\_empty(): read len only in debug build
* [Revision #aaf71116ee](https://github.com/MariaDB/server/commit/aaf71116ee)\
  2018-02-13 22:36:43 +0300
  * remove unused stuff:
* [Revision #399ec84847](https://github.com/MariaDB/server/commit/399ec84847)\
  2018-02-13 22:27:30 +0300
  * prettify lock\_rec\_has\_to\_wait()
* [Revision #e4fa5492a9](https://github.com/MariaDB/server/commit/e4fa5492a9)\
  2018-02-13 22:03:26 +0300
  * prettify lock\_has\_to\_wait
* Merge [Revision #2ba487cfe8](https://github.com/MariaDB/server/commit/2ba487cfe8) 2018-02-19 11:37:29 +0200 - Merge bb-10.2-ext into 10.3
* [Revision #ef3147b1d6](https://github.com/MariaDB/server/commit/ef3147b1d6)\
  2018-02-19 11:27:21 +0200
  * Fix for [MDEV-15105](https://jira.mariadb.org/browse/MDEV-15105) (memory loss with LOCK sequence)
* [Revision #06ba07c269](https://github.com/MariaDB/server/commit/06ba07c269)\
  2018-02-19 11:26:25 +0200
  * Test case for [MDEV-12887](https://jira.mariadb.org/browse/MDEV-12887) (bug fixed long ago)
* Merge [Revision #278c036275](https://github.com/MariaDB/server/commit/278c036275) 2018-02-19 09:01:06 +0200 - Merge 10.2 into bb-10.2-ext
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
* [Revision #9a46d97149](https://github.com/MariaDB/server/commit/9a46d97149)\
  2018-02-17 14:20:33 +0200
  * [MDEV-15333](https://jira.mariadb.org/browse/MDEV-15333) MariaDB (still) slow start
* [Revision #a351f40cba](https://github.com/MariaDB/server/commit/a351f40cba)\
  2018-02-16 14:14:43 +0400
  * [MDEV-14541](https://jira.mariadb.org/browse/MDEV-14541) - Workaround GCC ICE on ARM64
* [Revision #21e5335154](https://github.com/MariaDB/server/commit/21e5335154)\
  2018-02-16 10:19:57 +0200
  * [MDEV-9962](https://jira.mariadb.org/browse/MDEV-9962): encryption.innodb\_encryption\_filekeys stalled waiting for key encryption threads to decrypt all required spaces
* [Revision #d3fbff38b9](https://github.com/MariaDB/server/commit/d3fbff38b9)\
  2018-02-16 08:21:19 +0200
  * [MDEV-14814](https://jira.mariadb.org/browse/MDEV-14814): encryption.innodb\_encryption-page-compression failed in buildbot with timeout on wait condition
* [Revision #8bf2c08d54](https://github.com/MariaDB/server/commit/8bf2c08d54)\
  2018-02-16 21:02:35 +0200
  * Add a suppression for background page read error
* [Revision #fed51b80fb](https://github.com/MariaDB/server/commit/fed51b80fb)\
  2018-02-17 19:16:56 +0400
  * Adding "const" qualifier to the MYSQL\_TIME parameter of Item\_temporal\_literal constructors
* Merge [Revision #a55ded1b89](https://github.com/MariaDB/server/commit/a55ded1b89) 2018-02-16 13:52:02 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #6668da2216](https://github.com/MariaDB/server/commit/6668da2216)\
  2018-02-16 13:44:24 +0400
  * [MDEV-15289](https://jira.mariadb.org/browse/MDEV-15289) Binding an out-of-range DATETIME value in binary protocol breaks replication
* [Revision #144616034c](https://github.com/MariaDB/server/commit/144616034c)\
  2018-02-16 01:35:19 +0200
  * Don't run sql\_sequence.grant for embeddes server
* [Revision #8df787d375](https://github.com/MariaDB/server/commit/8df787d375)\
  2018-02-15 18:39:29 +0200
  * Follow-up for 54db0be3be59 (Added Max\_index\_length and Temporary)
* [Revision #afc56a509c](https://github.com/MariaDB/server/commit/afc56a509c)\
  2018-02-17 00:11:45 +0600
  * merge two the same consistently 'if' clauses into one
* [Revision #f8bdf4d1ee](https://github.com/MariaDB/server/commit/f8bdf4d1ee)\
  2018-02-13 00:47:15 +0600
  * remove duplicated inclusion of derror.h
* [Revision #8ab37bbd69](https://github.com/MariaDB/server/commit/8ab37bbd69)\
  2018-02-12 00:47:48 +0600
  * fix comment in my\_decimal\_set\_zero()
* [Revision #990289a78f](https://github.com/MariaDB/server/commit/990289a78f)\
  2018-02-15 14:16:55 +0000
  * Fix DBUG\_PRINT formatting for ulonglong alter\_info.flags
* Merge [Revision #633d252e32](https://github.com/MariaDB/server/commit/633d252e32) 2018-02-15 16:12:15 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #4074c74556](https://github.com/MariaDB/server/commit/4074c74556) 2018-02-15 15:41:47 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #5ab4602810](https://github.com/MariaDB/server/commit/5ab4602810)\
  2018-02-15 15:34:15 +0200
  * [MDEV-15323](https://jira.mariadb.org/browse/MDEV-15323) Follow-up to [MDEV-14905](https://jira.mariadb.org/browse/MDEV-14905): Skip FTS processing if innodb\_read\_only
* [Revision #f40c11d88b](https://github.com/MariaDB/server/commit/f40c11d88b)\
  2018-02-15 16:10:59 +0200
  * After-merge fix: Use matching format
* Merge [Revision #cc3b5d1fe7](https://github.com/MariaDB/server/commit/cc3b5d1fe7) 2018-02-15 11:48:30 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #22770a9f9a](https://github.com/MariaDB/server/commit/22770a9f9a) 2018-02-15 10:57:27 +0200 - Merge 10.2 into bb-10.2-ext
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
* [Revision #7bd81c726b](https://github.com/MariaDB/server/commit/7bd81c726b)\
  2018-02-14 17:06:24 +0200
  * Crash when giving error message for ALTER SEQUENCE
* [Revision #c17a06abf8](https://github.com/MariaDB/server/commit/c17a06abf8)\
  2018-02-14 22:58:34 +0400
  * [MDEV-15310](https://jira.mariadb.org/browse/MDEV-15310) Range optimizer does not work well for "WHERE temporal\_column NOT IN (const\_list)"
* [Revision #1fe9092d06](https://github.com/MariaDB/server/commit/1fe9092d06)\
  2018-02-14 16:43:22 +0200
  * Fix privilege checking for sequence
* Merge [Revision #b006d2ead4](https://github.com/MariaDB/server/commit/b006d2ead4) 2018-02-15 10:22:03 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #dc09f8f29c](https://github.com/MariaDB/server/commit/dc09f8f29c) 2018-02-14 10:12:53 +0200 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #c6e35276f1](https://github.com/MariaDB/server/commit/c6e35276f1) 2018-02-14 10:01:16 +0200 - Merge 10.1 into 10.2
* [Revision #a33c9a07e5](https://github.com/MariaDB/server/commit/a33c9a07e5)\
  2017-11-13 11:36:21 +0000
  * [GAL-506](https://github.com/codership/galera/issues/506) breaks galera\_defaults MTR test by upping repl.proto\_max again. Fix this once and for all by overwriting it with constant string since it makes little sense to check for it in this test.
* [Revision #ab8ea23a75](https://github.com/MariaDB/server/commit/ab8ea23a75)\
  2018-02-13 11:23:14 -0500
  * bump the VERSION
* [Revision #95d075a0e5](https://github.com/MariaDB/server/commit/95d075a0e5)\
  2018-02-13 20:37:31 +0400
  * [MDEV-15293](https://jira.mariadb.org/browse/MDEV-15293) CAST(AS TIME) returns bad results for LAST\_VALUE(),NAME\_CONST(),SP variable
* Merge [Revision #0c4aeef976](https://github.com/MariaDB/server/commit/0c4aeef976) 2018-02-13 16:51:45 +0200 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #d9955b22e9](https://github.com/MariaDB/server/commit/d9955b22e9) 2018-02-13 14:49:47 +0200 - Merge 10.1 into 10.2
* Merge [Revision #2202afd541](https://github.com/MariaDB/server/commit/2202afd541) 2018-02-13 14:32:17 +0200 - Merge 10.0 into 10.1
* [Revision #c051eaba46](https://github.com/MariaDB/server/commit/c051eaba46)\
  2018-02-13 13:01:14 +0200
  * [MDEV-14988](https://jira.mariadb.org/browse/MDEV-14988) innodb\_read\_only tries to modify files if transactions were recovered in COMMITTED state
* [Revision #a778a62822](https://github.com/MariaDB/server/commit/a778a62822)\
  2018-02-13 15:56:48 +0200
  * Re-record a result; repl.proto\_max is 8, not 7
* [Revision #991649e3ed](https://github.com/MariaDB/server/commit/991649e3ed)\
  2018-02-13 09:33:06 +0400
  * A cleanup for [MDEV-15287](https://jira.mariadb.org/browse/MDEV-15287): removung unused code
* [Revision #54db0be3be](https://github.com/MariaDB/server/commit/54db0be3be)\
  2018-02-10 14:42:59 +0200
  * Added Max\_index\_length and Temporary to SHOW TABLE STATUS
* [Revision #19dd14e648](https://github.com/MariaDB/server/commit/19dd14e648)\
  2018-02-07 19:16:45 +0200
  * Updated galera .result files
* [Revision #4087683e1a](https://github.com/MariaDB/server/commit/4087683e1a)\
  2018-02-12 17:55:48 +0400
  * [MDEV-15287](https://jira.mariadb.org/browse/MDEV-15287) Bad result for LEAST/GREATEST(datetime\_alike\_string, time)
* Merge [Revision #da99e086f9](https://github.com/MariaDB/server/commit/da99e086f9) 2018-02-12 10:03:28 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* Merge [Revision #5559905d41](https://github.com/MariaDB/server/commit/5559905d41) 2018-02-09 12:48:23 +0200 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #c567369ad7](https://github.com/MariaDB/server/commit/c567369ad7) 2018-02-08 17:48:19 +0200 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #3cad31f2a7](https://github.com/MariaDB/server/commit/3cad31f2a7) 2018-02-08 19:06:25 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #b782971c58](https://github.com/MariaDB/server/commit/b782971c58)\
  2018-02-13 19:51:13 +0400
  * [MDEV-15246](https://jira.mariadb.org/browse/MDEV-15246) - premature history data deletion
* [Revision #ba125eca55](https://github.com/MariaDB/server/commit/ba125eca55)\
  2018-02-13 18:06:15 +0400
  * [MDEV-15215](https://jira.mariadb.org/browse/MDEV-15215) main.partition\_explicit\_prune fails in bulidbot with assertion failures and server crashes.
* [Revision #3c87973235](https://github.com/MariaDB/server/commit/3c87973235)\
  2018-02-13 00:23:57 +0100
  * [MDEV-14990](https://jira.mariadb.org/browse/MDEV-14990) mysql\_upgrade fails with ERROR 1408 (HY000) at line 566: Event Scheduler: An error occurred when initializing system tables
* [Revision #f7621f17bd](https://github.com/MariaDB/server/commit/f7621f17bd)\
  2018-02-12 16:26:11 +0100
  * rename mysql.user and mysql.db column
* [Revision #f51ecfee93](https://github.com/MariaDB/server/commit/f51ecfee93)\
  2018-02-12 00:06:40 +0100
  * [MDEV-15146](https://jira.mariadb.org/browse/MDEV-15146) SQLError\[4122]: View is not system versioned
* [Revision #39157fbf05](https://github.com/MariaDB/server/commit/39157fbf05)\
  2018-02-11 18:26:44 +0100
  * Remove ER\_NON\_VERSIONED\_FIELD\_IN\_HISTORICAL\_QUERY
* [Revision #d0f5e56a20](https://github.com/MariaDB/server/commit/d0f5e56a20)\
  2018-02-10 20:34:18 +0100
  * [MDEV-14785](https://jira.mariadb.org/browse/MDEV-14785) SYSTEM\_INVISIBLE behaviour not consistent
* [Revision #34ee747f55](https://github.com/MariaDB/server/commit/34ee747f55)\
  2018-02-10 19:10:59 +0100
  * cleanup: remove MARK\_COLUMNS\_NONE
* [Revision #103715d0fa](https://github.com/MariaDB/server/commit/103715d0fa)\
  2018-02-09 19:43:42 +0100
  * cleanup: renames
* [Revision #8cd3d2d941](https://github.com/MariaDB/server/commit/8cd3d2d941)\
  2018-02-09 18:37:36 +0100
  * fixes for ctags
* [Revision #4fd48678ae](https://github.com/MariaDB/server/commit/4fd48678ae)\
  2018-02-09 17:30:20 +0100
  * ALTER TABLE ... DROP COLUMN sys\_start
* [Revision #dfd42ed990](https://github.com/MariaDB/server/commit/dfd42ed990)\
  2018-02-09 16:42:12 +0100
  * ALTER TABLE ... DROP COLUMN sys\_start should rename a "dropped" column
* [Revision #c847089e6e](https://github.com/MariaDB/server/commit/c847089e6e)\
  2018-02-08 23:03:35 +0100
  * Cannot DROP VERSIONING without dropping all visible AS ROW fields
* [Revision #f3a49e7020](https://github.com/MariaDB/server/commit/f3a49e7020)\
  2018-02-08 22:50:57 +0100
  * Don't allow adding AS ROW START column to a not versioned table
* [Revision #bc0ac28f69](https://github.com/MariaDB/server/commit/bc0ac28f69)\
  2018-02-01 15:50:56 +0100
  * ALTER TABLE ... DROP VERSIONING
* [Revision #59ca71d496](https://github.com/MariaDB/server/commit/59ca71d496)\
  2018-02-08 17:34:30 +0100
  * INVISIBLE columns in USING and NATURAL JOIN
* [Revision #7a42f28e16](https://github.com/MariaDB/server/commit/7a42f28e16)\
  2018-02-08 17:32:11 +0100
  * cleanup: mark\_common\_columns()
* [Revision #031c85ca56](https://github.com/MariaDB/server/commit/031c85ca56)\
  2018-02-07 19:28:34 +0100
  * cleanup: remove duplicated code
* [Revision #7fa88d4435](https://github.com/MariaDB/server/commit/7fa88d4435)\
  2018-02-01 16:34:50 +0100
  * cleanup: simplify fill\_record()
* [Revision #34857b9166](https://github.com/MariaDB/server/commit/34857b9166)\
  2018-01-30 22:30:52 +0100
  * cleanup: find\_field\_in\_table()
* [Revision #f894f902a4](https://github.com/MariaDB/server/commit/f894f902a4)\
  2018-01-30 22:29:55 +0100
  * cleanup: TABLE::find\_field\_by\_name
* [Revision #711f3dd7f5](https://github.com/MariaDB/server/commit/711f3dd7f5)\
  2018-01-29 17:07:45 +0100
  * [MDEV-13417](https://jira.mariadb.org/browse/MDEV-13417) UPDATE produces wrong values if an updated column is later used as an update source
* [Revision #d943d7f712](https://github.com/MariaDB/server/commit/d943d7f712)\
  2018-01-29 16:53:39 +0100
  * [MDEV-13417](https://jira.mariadb.org/browse/MDEV-13417) UPDATE produces wrong values if an updated column is later used as an update source
* [Revision #355ee6877b](https://github.com/MariaDB/server/commit/355ee6877b)\
  2017-10-10 22:47:18 +0200
  * [MDEV-13946](https://jira.mariadb.org/browse/MDEV-13946) Server RPMs have dependency on "which"
* [Revision #2232784f00](https://github.com/MariaDB/server/commit/2232784f00)\
  2018-02-10 00:07:39 +0000
  * Fix inadverent change in Sql\_alloc
* [Revision #17c9ed6725](https://github.com/MariaDB/server/commit/17c9ed6725)\
  2018-02-10 00:00:10 +0000
  * Fix perfschema tests in debug mode.
* [Revision #e3cf577948](https://github.com/MariaDB/server/commit/e3cf577948)\
  2018-02-08 22:45:16 +0200
  * [MDEV-14663](https://jira.mariadb.org/browse/MDEV-14663) Assertion page\_is\_root(block->frame) failed in innobase\_add\_instant\_try
* [Revision #32170f8c6d](https://github.com/MariaDB/server/commit/32170f8c6d)\
  2018-02-08 22:34:21 +0200
  * Add page\_has\_prev(), page\_has\_next(), page\_has\_siblings()
* [Revision #3969d97e6a](https://github.com/MariaDB/server/commit/3969d97e6a)\
  2018-02-08 14:55:01 +0200
  * [MDEV-14427](https://jira.mariadb.org/browse/MDEV-14427): encryption.innodb-bad-key-change failed in buildbot
* [Revision #627d33d9cf](https://github.com/MariaDB/server/commit/627d33d9cf)\
  2018-02-08 12:16:06 +0000
  * Innodb, Windows : Reenable compiler optimizations for mem0mem.cc
* [Revision #6c5d364956](https://github.com/MariaDB/server/commit/6c5d364956)\
  2018-02-08 12:02:49 +0000
  * [MDEV-14953](https://jira.mariadb.org/browse/MDEV-14953) - rename libmysqld.so to libmariadbd.so
* [Revision #bbdb47ffe4](https://github.com/MariaDB/server/commit/bbdb47ffe4)\
  2018-02-08 12:28:07 +0200
  * Revert an accidental change
* [Revision #7660d8c94e](https://github.com/MariaDB/server/commit/7660d8c94e)\
  2018-02-07 17:40:33 +0200
  * Remove dict\_table\_t::is\_clust()
* [Revision #609d0a9194](https://github.com/MariaDB/server/commit/609d0a9194)\
  2018-02-07 16:44:46 +0200
  * [MDEV-14407](https://jira.mariadb.org/browse/MDEV-14407) Assertion failure during rollback
* [Revision #e2387835ef](https://github.com/MariaDB/server/commit/e2387835ef)\
  2018-02-07 20:23:10 +0000
  * Cleanup - removed warning suppression - no longer needed.
* [Revision #53476abce8](https://github.com/MariaDB/server/commit/53476abce8)\
  2018-02-07 01:40:16 +0000
  * Windows, compiling : use /permissive- switch to improve conformance
* [Revision #8fe04a3df3](https://github.com/MariaDB/server/commit/8fe04a3df3)\
  2018-02-06 23:32:02 +0000
  * Windows, compile : reenable previously disabled warning C4291 no matching operator delete found; memory will not be freed if initialization throws an exception
* [Revision #282b652028](https://github.com/MariaDB/server/commit/282b652028)\
  2018-02-07 20:17:38 +0000
  * Windows, compiling : reenable warning C4996 (deprecated functions)
* [Revision #d995dd2865](https://github.com/MariaDB/server/commit/d995dd2865)\
  2018-02-06 17:14:05 +0000
  * Windows : reenable warning C4805 (unsafe mix of types in bool operations)
* [Revision #7bcf5e2907](https://github.com/MariaDB/server/commit/7bcf5e2907)\
  2018-02-07 19:56:16 +0200
  * [MDEV-15238](https://jira.mariadb.org/browse/MDEV-15238) rpl.perf\_buildin\_semisync\_issue40 sporadically fails on BB
* [Revision #029ab11cc8](https://github.com/MariaDB/server/commit/029ab11cc8)\
  2018-02-07 13:29:08 +0200
  * Update wrong result test found by fix to mysql\_upgrade
* [Revision #6ba06cf763](https://github.com/MariaDB/server/commit/6ba06cf763)\
  2018-02-07 02:39:40 +0200
  * On upgrade Truncate\_versioning\_privilege was not correct set
* [Revision #a0417ccc3a](https://github.com/MariaDB/server/commit/a0417ccc3a)\
  2018-02-06 20:38:19 +0200
  * Added error message for index file full
* Merge [Revision #883496782f](https://github.com/MariaDB/server/commit/883496782f) 2018-02-06 17:12:17 +0200 - Merge bb-10.2-ext into 10.3
* [Revision #560b9895d4](https://github.com/MariaDB/server/commit/560b9895d4)\
  2018-02-06 17:09:26 +0200
  * [MDEV-15115](https://jira.mariadb.org/browse/MDEV-15115) Assertion failure in CREATE SEQUENCE...ROW\_FORMAT=REDUNDANT
* [Revision #b4db96da58](https://github.com/MariaDB/server/commit/b4db96da58)\
  2018-02-05 13:22:58 +0400
  * [MDEV-15176](https://jira.mariadb.org/browse/MDEV-15176): comment fix "1 00:10:10" -> "24:10:10"
* [Revision #d67dcb7bb5](https://github.com/MariaDB/server/commit/d67dcb7bb5)\
  2018-02-04 22:55:54 +0400
  * [MDEV-15205](https://jira.mariadb.org/browse/MDEV-15205) Remove mysql\_type\_to\_time\_type()
* [Revision #eda142590f](https://github.com/MariaDB/server/commit/eda142590f)\
  2018-02-06 15:44:21 +0200
  * Improve the documentation of some TRX\_RSEG fields
* [Revision #502e2445e6](https://github.com/MariaDB/server/commit/502e2445e6)\
  2018-02-06 14:22:15 +0100
  * Fix warnings
* [Revision #6c279ad6a7](https://github.com/MariaDB/server/commit/6c279ad6a7)\
  2018-02-06 12:55:58 +0000
  * [MDEV-15091](https://jira.mariadb.org/browse/MDEV-15091) : Windows, 64bit: reenable and fix warning C4267 (conversion from 'size\_t' to 'type', possible loss of data)
* [Revision #f271100836](https://github.com/MariaDB/server/commit/f271100836)\
  2018-02-05 18:07:31 -0800
  * Fixed [MDEV-15162](https://jira.mariadb.org/browse/MDEV-15162) Query with CTE hangs if assignment operator (:=) is used
* [Revision #465979eabf](https://github.com/MariaDB/server/commit/465979eabf)\
  2018-02-05 10:47:59 -0800
  * Fixed [MDEV-15119](https://jira.mariadb.org/browse/MDEV-15119) CTE, referencing another CTE, that is declared after, does not return error
* Merge [Revision #217fc122c8](https://github.com/MariaDB/server/commit/217fc122c8) 2018-02-04 18:40:06 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #28d4cf0c1b](https://github.com/MariaDB/server/commit/28d4cf0c1b)\
  2018-02-04 16:43:02 +0400
  * [MDEV-15176](https://jira.mariadb.org/browse/MDEV-15176) Storing DATETIME-alike VARCHAR data into TIME produces wrong results
* [Revision #2ecf2f9b2a](https://github.com/MariaDB/server/commit/2ecf2f9b2a)\
  2018-02-03 17:27:43 +0400
  * Adding "const" qualifier to the MYSQL\_TIME\* argument of Field::store\_time\_dec()
* [Revision #705283f7e3](https://github.com/MariaDB/server/commit/705283f7e3)\
  2018-02-02 15:38:15 +0400
  * Setting Field::field\_index for Virtual\_tmp\_table fields
* [Revision #d69642dedd](https://github.com/MariaDB/server/commit/d69642dedd)\
  2018-02-02 11:08:36 +0200
  * Added name to MEM\_ROOT for esier debugging
* [Revision #1e5e3d562b](https://github.com/MariaDB/server/commit/1e5e3d562b)\
  2018-01-31 19:49:48 +0400
  * A cleanup in sp\_rcontext, as requested by Monty
* [Revision #df2d678248](https://github.com/MariaDB/server/commit/df2d678248)\
  2018-01-31 11:37:02 +0100
  * [MDEV-15133](https://jira.mariadb.org/browse/MDEV-15133): array bound (bulk) parameters of NULL propagate on next rows
* [Revision #e300f0c961](https://github.com/MariaDB/server/commit/e300f0c961)\
  2018-01-30 21:32:19 +0200
  * [MDEV-15133](https://jira.mariadb.org/browse/MDEV-15133) array bound (bulk) parameters of NULL propagate on next rows
* [Revision #d6ed077fc8](https://github.com/MariaDB/server/commit/d6ed077fc8)\
  2018-02-04 13:11:49 +0200
  * Clarify a comment after [MDEV-15061](https://jira.mariadb.org/browse/MDEV-15061)
* [Revision #c8299e6278](https://github.com/MariaDB/server/commit/c8299e6278)\
  2018-02-01 18:58:55 +0530
  * This commit solves a couple of issues
* [Revision #16be7469ac](https://github.com/MariaDB/server/commit/16be7469ac)\
  2018-01-29 12:31:07 +0530
  * [MDEV-14849](https://jira.mariadb.org/browse/MDEV-14849) CREATE + ALTER with user-invisible columns produce ...
* [Revision #2d73b58101](https://github.com/MariaDB/server/commit/2d73b58101)\
  2018-01-30 14:04:05 +0530
  * [MDEV-15085](https://jira.mariadb.org/browse/MDEV-15085) Invisible Column Non-constant Default value results...
* [Revision #782f8e743b](https://github.com/MariaDB/server/commit/782f8e743b)\
  2018-02-01 19:46:42 +0200
  * Removed 'thd' from THD::reset\_for\_next\_command()
* [Revision #1951e7f05a](https://github.com/MariaDB/server/commit/1951e7f05a)\
  2018-01-31 10:15:17 -0800
  * Fixed [MDEV-15120](https://jira.mariadb.org/browse/MDEV-15120) CTE table should not belong to database, that is in use
* [Revision #bc7a1dc1fb](https://github.com/MariaDB/server/commit/bc7a1dc1fb)\
  2018-01-30 20:59:42 +0400
  * [MDEV-15104](https://jira.mariadb.org/browse/MDEV-15104) - Optimise MVCC snapshot
* [Revision #c0d5d7c0ef](https://github.com/MariaDB/server/commit/c0d5d7c0ef)\
  2018-01-28 16:02:48 +0400
  * [MDEV-15104](https://jira.mariadb.org/browse/MDEV-15104) - Remove trx\_sys\_t::serialisation\_list
* [Revision #53cc9aa5be](https://github.com/MariaDB/server/commit/53cc9aa5be)\
  2018-01-27 19:30:18 +0400
  * [MDEV-15104](https://jira.mariadb.org/browse/MDEV-15104) - Remove trx\_sys\_t::rw\_trx\_ids
* [Revision #af566d8a63](https://github.com/MariaDB/server/commit/af566d8a63)\
  2018-01-28 17:17:11 +0400
  * Reduce number of trx\_sys.mutex references
* [Revision #dcc09afa63](https://github.com/MariaDB/server/commit/dcc09afa63)\
  2018-01-31 13:13:29 +0200
  * Follow-up fix to [MDEV-15132](https://jira.mariadb.org/browse/MDEV-15132) Avoid accessing the TRX\_SYS page
* [Revision #7eb084fe2c](https://github.com/MariaDB/server/commit/7eb084fe2c)\
  2018-01-30 13:48:45 +1100
  * mariadb-backup: gcc7 - snprintf output overflow warning
* [Revision #464ba0e97f](https://github.com/MariaDB/server/commit/464ba0e97f)\
  2018-01-30 13:40:52 +1100
  * versioning: add explict fallthough to prevent gcc warning
* [Revision #5db9c6e490](https://github.com/MariaDB/server/commit/5db9c6e490)\
  2018-01-30 21:58:23 +0200
  * [MDEV-15132](https://jira.mariadb.org/browse/MDEV-15132) Avoid accessing the TRX\_SYS page
* [Revision #c7d0448797](https://github.com/MariaDB/server/commit/c7d0448797)\
  2018-01-31 10:24:19 +0200
  * [MDEV-15132](https://jira.mariadb.org/browse/MDEV-15132) Avoid accessing the TRX\_SYS page
* [Revision #bb441ca4ad](https://github.com/MariaDB/server/commit/bb441ca4ad)\
  2018-01-30 16:31:10 +0200
  * Clean up trx\_undo\_page\_get\_end()
* [Revision #6058f92f5c](https://github.com/MariaDB/server/commit/6058f92f5c)\
  2018-01-30 14:16:09 +0200
  * Simplify undo log access during InnoDB startup
* [Revision #d24229baa2](https://github.com/MariaDB/server/commit/d24229baa2)\
  2018-01-30 13:55:00 +0200
  * Do not call trx\_rseg\_mem\_restore() when creating rollback segment
* [Revision #0ead8d9520](https://github.com/MariaDB/server/commit/0ead8d9520)\
  2018-01-30 13:10:57 +0200
  * Clean up some undo page accessor functions
* [Revision #648e8c12e5](https://github.com/MariaDB/server/commit/648e8c12e5)\
  2018-01-30 12:56:30 +0200
  * Remove unnecessary function parameters
* [Revision #8d1d38f953](https://github.com/MariaDB/server/commit/8d1d38f953)\
  2018-01-30 10:34:43 +0200
  * Simplify access to the TRX\_SYS page
* [Revision #54c715acca](https://github.com/MariaDB/server/commit/54c715acca)\
  2018-01-30 13:39:48 +0200
  * Avoid an assertion failure on aborted startup
* [Revision #7a9611aee2](https://github.com/MariaDB/server/commit/7a9611aee2)\
  2018-01-30 21:12:11 -0800
  * Fixed [MDEV-14994](https://jira.mariadb.org/browse/MDEV-14994) Assertion \`join->best\_read < double(1.79...15e+308L)' or server crash in JOIN::fix\_all\_splittings\_in\_plan
* [Revision #a1e0e64a47](https://github.com/MariaDB/server/commit/a1e0e64a47)\
  2018-01-23 09:43:11 +0200
  * Don't give warning about usage of --language with full path
* [Revision #f10fae7e4f](https://github.com/MariaDB/server/commit/f10fae7e4f)\
  2018-01-21 22:39:10 +0200
  * Remove compiler warnings
* [Revision #486c86dd39](https://github.com/MariaDB/server/commit/486c86dd39)\
  2018-01-19 19:56:34 +0200
  * Added some checking that LEX\_CSTRING is \0 terminated
* [Revision #f55dc7f733](https://github.com/MariaDB/server/commit/f55dc7f733)\
  2018-01-08 15:33:23 +0200
  * Change C\_STRING\_WITH\_LEN to STRING\_WITH\_LEN
* [Revision #18e22cb69f](https://github.com/MariaDB/server/commit/18e22cb69f)\
  2018-01-08 15:02:13 +0200
  * Removed not used functions and variables
* [Revision #bbe0055fee](https://github.com/MariaDB/server/commit/bbe0055fee)\
  2018-01-08 14:59:42 +0200
  * Added defines for mysqld\_error\_find\_printf\_error\_used
* [Revision #29fd049a7b](https://github.com/MariaDB/server/commit/29fd049a7b)\
  2018-01-08 14:56:21 +0200
  * Renamed Item\_user\_var\_as\_out\_param::name to org\_name
* [Revision #b9b17e6340](https://github.com/MariaDB/server/commit/b9b17e6340)\
  2018-01-08 11:35:08 +0200
  * Updated error message for wrong foreign key constraint
* [Revision #a2393ff22e](https://github.com/MariaDB/server/commit/a2393ff22e)\
  2018-01-07 23:53:42 +0200
  * Fixed wrong arguments to printf
* [Revision #a7e352b54d](https://github.com/MariaDB/server/commit/a7e352b54d)\
  2018-01-07 18:03:44 +0200
  * Changed database, tablename and alias to be LEX\_CSTRING
* Merge [Revision #921c5e9314](https://github.com/MariaDB/server/commit/921c5e9314) 2018-01-30 21:18:39 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #0c1f220611](https://github.com/MariaDB/server/commit/0c1f220611) 2018-01-30 20:42:42 +0200 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #33714d2065](https://github.com/MariaDB/server/commit/33714d2065) 2018-01-30 21:04:48 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #6d390bab4a](https://github.com/MariaDB/server/commit/6d390bab4a) 2018-01-30 20:18:25 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #8317ce73d4](https://github.com/MariaDB/server/commit/8317ce73d4)\
  2018-01-29 20:36:38 +0400
  * [MDEV-15112](https://jira.mariadb.org/browse/MDEV-15112) Inconsistent evaluation of spvariable=0 in strict mode
* [Revision #926adcfeea](https://github.com/MariaDB/server/commit/926adcfeea)\
  2018-01-30 17:08:36 +0400
  * [MDEV-14694](https://jira.mariadb.org/browse/MDEV-14694) ALTER COLUMN IF EXISTS .. causes syntax error.
* [Revision #5478547c96](https://github.com/MariaDB/server/commit/5478547c96)\
  2018-01-30 15:04:08 +0200
  * Fixed failing tests
* [Revision #775aa5542d](https://github.com/MariaDB/server/commit/775aa5542d)\
  2018-01-29 23:51:04 -0800
  * Fixed [MDEV-15017](https://jira.mariadb.org/browse/MDEV-15017) Server crashes in st\_join\_table::fix\_splitting
* [Revision #4808996b12](https://github.com/MariaDB/server/commit/4808996b12)\
  2018-01-29 23:07:26 +0000
  * Fix result file
* [Revision #160a94ee7a](https://github.com/MariaDB/server/commit/160a94ee7a)\
  2018-01-29 20:04:13 +0000
  * Fix result files (changed error message)
* [Revision #c6a6c02e8f](https://github.com/MariaDB/server/commit/c6a6c02e8f)\
  2018-01-29 22:19:42 +0300
  * Create rocksdb\_rpl.mdev12179 by taking tokudb\_rpl.mdev12179 and adjusting it
* [Revision #0bbd299161](https://github.com/MariaDB/server/commit/0bbd299161)\
  2018-01-29 22:08:44 +0300
  * Fix a merge error in [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179) code in process\_gtid\_pos\_table
* [Revision #28d412411d](https://github.com/MariaDB/server/commit/28d412411d)\
  2018-01-29 18:31:26 +0000
  * Fix type truncation warnings.
* [Revision #8b673d44ce](https://github.com/MariaDB/server/commit/8b673d44ce)\
  2018-01-29 19:07:35 +0200
  * Fix an integer type mismatch
* [Revision #9bb93b86c2](https://github.com/MariaDB/server/commit/9bb93b86c2)\
  2018-01-29 17:01:58 +0000
  * Fix warnings.
* Merge [Revision #3415228718](https://github.com/MariaDB/server/commit/3415228718) 2018-01-29 16:42:33 +0000 - Merge branch '10.3' of [server](https://github.com/mariadb/server) into 10.3
* [Revision #2e43c4584e](https://github.com/MariaDB/server/commit/2e43c4584e)\
  2018-01-29 19:52:34 +0400
  * Fixing versioning.insert and versioning.replace test failes.
* [Revision #f74023b955](https://github.com/MariaDB/server/commit/f74023b955)\
  2018-01-29 14:52:04 +0200
  * [MDEV-15090](https://jira.mariadb.org/browse/MDEV-15090) Reduce the overhead of writing undo log records
* [Revision #5d3c3b4927](https://github.com/MariaDB/server/commit/5d3c3b4927)\
  2018-01-29 14:48:53 +0200
  * [MDEV-15090](https://jira.mariadb.org/browse/MDEV-15090) Reduce the overhead of writing undo log records
* [Revision #4981f95ffa](https://github.com/MariaDB/server/commit/4981f95ffa)\
  2018-01-29 13:30:22 +0200
  * trx\_undo\_seg\_create(): Remove an unused parameter
* [Revision #a7e12fd42b](https://github.com/MariaDB/server/commit/a7e12fd42b)\
  2018-01-29 14:53:13 +0200
  * Fixed failing tests rpl\_semi\_sync\_skip\_repl.test
* Merge [Revision #c7a2f23a7b](https://github.com/MariaDB/server/commit/c7a2f23a7b) 2018-01-29 12:44:20 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #b12430adc7](https://github.com/MariaDB/server/commit/b12430adc7)\
  2018-01-29 12:01:17 +0400
  * [MDEV-15107](https://jira.mariadb.org/browse/MDEV-15107) Add virtual Field::sp\_prepare\_and\_store\_item(), make sp\_rcontext symmetric for scalar and ROW
* [Revision #ffcedfab46](https://github.com/MariaDB/server/commit/ffcedfab46)\
  2018-01-28 15:54:17 +0200
  * Added TRASH\_FREED\_MEMORY compilation option
* Merge [Revision #84514ec643](https://github.com/MariaDB/server/commit/84514ec643) 2018-01-27 15:20:01 +0200 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* Merge [Revision #071f528399](https://github.com/MariaDB/server/commit/071f528399) 2018-01-24 20:37:36 +0200 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #b4a2baffa8](https://github.com/MariaDB/server/commit/b4a2baffa8)\
  2018-01-29 11:01:14 +0400
  * [MDEV-11084](https://jira.mariadb.org/browse/MDEV-11084) Select statement with partition selection against MyISAM table opens all partitions.
* [Revision #041a32abcd](https://github.com/MariaDB/server/commit/041a32abcd)\
  2018-01-26 23:23:11 +0200
  * Remove trx\_mod\_tables\_t::vers\_by\_trx
* [Revision #b8c92d752c](https://github.com/MariaDB/server/commit/b8c92d752c)\
  2018-01-26 10:50:20 +0400
  * Fixed compiler warning
* [Revision #55277e8840](https://github.com/MariaDB/server/commit/55277e8840)\
  2018-01-25 18:29:59 +0400
  * [MDEV-15059](https://jira.mariadb.org/browse/MDEV-15059) - Misc small InnoDB scalability fixes
* [Revision #064bd78038](https://github.com/MariaDB/server/commit/064bd78038)\
  2018-01-24 22:10:16 +0400
  * [MDEV-15059](https://jira.mariadb.org/browse/MDEV-15059) - Misc small InnoDB scalability fixes
* [Revision #0499693910](https://github.com/MariaDB/server/commit/0499693910)\
  2018-01-23 13:23:35 +0400
  * [MDEV-15059](https://jira.mariadb.org/browse/MDEV-15059) - Misc small InnoDB scalability fixes
* [Revision #8389b45b7f](https://github.com/MariaDB/server/commit/8389b45b7f)\
  2018-01-22 23:58:52 +0400
  * [MDEV-15059](https://jira.mariadb.org/browse/MDEV-15059) - Misc small InnoDB scalability fixes
* [Revision #ce04790065](https://github.com/MariaDB/server/commit/ce04790065)\
  2018-01-24 20:09:14 +0400
  * [MDEV-14482](https://jira.mariadb.org/browse/MDEV-14482) - Cache line contention on ut\_rnd\_ulint\_counter()
* [Revision #92d233a512](https://github.com/MariaDB/server/commit/92d233a512)\
  2018-01-25 09:13:21 +0200
  * [MDEV-15061](https://jira.mariadb.org/browse/MDEV-15061) TRUNCATE must honor InnoDB table locks
* [Revision #f1ff69cf76](https://github.com/MariaDB/server/commit/f1ff69cf76)\
  2018-01-25 19:48:52 +0200
  * Bug fix
* Merge [Revision #52760731df](https://github.com/MariaDB/server/commit/52760731df) 2018-01-24 20:33:54 +0000 - Merge branch '10.3' of [server](https://github.com/mariadb/server) into 10.3
* [Revision #9aa461b187](https://github.com/MariaDB/server/commit/9aa461b187)\
  2018-01-24 14:01:45 +0200
  * Minor cleanup
* [Revision #4575ae70da](https://github.com/MariaDB/server/commit/4575ae70da)\
  2018-01-24 14:00:42 +0200
  * Plug a memory leak
* Merge [Revision #9875d5c3e1](https://github.com/MariaDB/server/commit/9875d5c3e1) 2018-01-24 14:00:33 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #62740e02c8](https://github.com/MariaDB/server/commit/62740e02c8) 2018-01-24 11:15:11 +0200 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #ec6b8c546a](https://github.com/MariaDB/server/commit/ec6b8c546a) 2018-01-23 17:43:12 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* Merge [Revision #c425dcd8f2](https://github.com/MariaDB/server/commit/c425dcd8f2) 2018-01-22 09:04:32 +0200 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #27a5d96bcb](https://github.com/MariaDB/server/commit/27a5d96bcb) 2018-01-21 20:32:48 +0200 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #6fe953cb71](https://github.com/MariaDB/server/commit/6fe953cb71)\
  2017-12-23 21:14:50 +0800
  * Fix build on OSX with 10.13 SDK
* [Revision #8e1adff959](https://github.com/MariaDB/server/commit/8e1adff959)\
  2018-01-21 14:10:06 +0400
  * Simplified away ReadView::complete()
* [Revision #4dc30f3c17](https://github.com/MariaDB/server/commit/4dc30f3c17)\
  2018-01-20 17:45:42 +0400
  * [MDEV-15019](https://jira.mariadb.org/browse/MDEV-15019) - InnoDB: store ReadView on trx
* Merge [Revision #c9d6da4d13](https://github.com/MariaDB/server/commit/c9d6da4d13) 2018-01-21 13:56:29 +0000 - Merge branch '10.3' of [server](https://github.com/mariadb/server) into 10.3
* [Revision #ec32c05072](https://github.com/MariaDB/server/commit/ec32c05072)\
  2018-01-19 23:03:18 +0400
  * Get rid of trx->read\_view pointer juggling
* [Revision #95070bf939](https://github.com/MariaDB/server/commit/95070bf939)\
  2018-01-19 21:42:33 +0400
  * MVCC simplifications
* [Revision #90bf55673e](https://github.com/MariaDB/server/commit/90bf55673e)\
  2018-01-19 19:05:43 +0400
  * Misc trx\_sys scalability fixes
* [Revision #64048bafe0](https://github.com/MariaDB/server/commit/64048bafe0)\
  2018-01-19 19:11:16 +0400
  * Removed purge\_trx\_id\_age and purge\_view\_trx\_id\_age
* [Revision #db5bb785f9](https://github.com/MariaDB/server/commit/db5bb785f9)\
  2018-01-17 19:43:08 +0400
  * Allocate trx\_sys.mvcc at link time
* [Revision #f8882cce93](https://github.com/MariaDB/server/commit/f8882cce93)\
  2017-12-22 16:15:41 +0200
  * Replace trx\_sys\_t\* trx\_sys with trx\_sys\_t trx\_sys
* [Revision #7078203389](https://github.com/MariaDB/server/commit/7078203389)\
  2017-12-27 20:07:20 +0400
  * [MDEV-14756](https://jira.mariadb.org/browse/MDEV-14756) - Remove trx\_sys\_t::rw\_trx\_list
* [Revision #c6d2842d9a](https://github.com/MariaDB/server/commit/c6d2842d9a)\
  2017-12-27 16:23:53 +0400
  * [MDEV-14756](https://jira.mariadb.org/browse/MDEV-14756) - Remove trx\_sys\_t::rw\_trx\_list
* [Revision #a447980ff3](https://github.com/MariaDB/server/commit/a447980ff3)\
  2017-12-27 15:38:23 +0400
  * [MDEV-14756](https://jira.mariadb.org/browse/MDEV-14756) - Remove trx\_sys\_t::rw\_trx\_list
* [Revision #886af392d3](https://github.com/MariaDB/server/commit/886af392d3)\
  2017-12-27 14:24:34 +0400
  * [MDEV-14756](https://jira.mariadb.org/browse/MDEV-14756) - Remove trx\_sys\_t::rw\_trx\_list
* [Revision #02270b44d0](https://github.com/MariaDB/server/commit/02270b44d0)\
  2017-12-24 21:23:10 +0400
  * [MDEV-14756](https://jira.mariadb.org/browse/MDEV-14756) - Remove trx\_sys\_t::rw\_trx\_list
* [Revision #d8c0caad32](https://github.com/MariaDB/server/commit/d8c0caad32)\
  2017-12-24 19:57:11 +0400
  * [MDEV-14756](https://jira.mariadb.org/browse/MDEV-14756) - Remove trx\_sys\_t::rw\_trx\_list
* [Revision #900b07908b](https://github.com/MariaDB/server/commit/900b07908b)\
  2017-12-27 01:04:08 +0400
  * [MDEV-14756](https://jira.mariadb.org/browse/MDEV-14756) - Remove trx\_sys\_t::rw\_trx\_list
* [Revision #a0b385ea2b](https://github.com/MariaDB/server/commit/a0b385ea2b)\
  2017-12-26 23:53:38 +0400
  * [MDEV-14756](https://jira.mariadb.org/browse/MDEV-14756) - Remove trx\_sys\_t::rw\_trx\_list
* [Revision #868c77df3e](https://github.com/MariaDB/server/commit/868c77df3e)\
  2017-12-21 17:20:14 +0400
  * [MDEV-14756](https://jira.mariadb.org/browse/MDEV-14756) - Remove trx\_sys\_t::rw\_trx\_list
* [Revision #d09f146934](https://github.com/MariaDB/server/commit/d09f146934)\
  2017-12-21 15:45:40 +0400
  * [MDEV-14756](https://jira.mariadb.org/browse/MDEV-14756) - Remove trx\_sys\_t::rw\_trx\_list
* [Revision #07c0bac039](https://github.com/MariaDB/server/commit/07c0bac039)\
  2018-01-19 14:07:41 -0800
  * Fixed [MDEV-14947](https://jira.mariadb.org/browse/MDEV-14947) Assertion \`0' fails in Field\_null::can\_optimize\_keypart\_ref when number of NULLs in IN list reaches in\_predicate\_conversion\_threshold
* [Revision #e15f4af4dc](https://github.com/MariaDB/server/commit/e15f4af4dc)\
  2018-01-18 12:43:56 -0500
  * bump the VERSION
* [Revision #ae05c1bb34](https://github.com/MariaDB/server/commit/ae05c1bb34)\
  2018-01-18 14:32:56 +0000
  * Keep the ER\_OUT\_OF\_RESOURCES message short and OS neutral.
* [Revision #745e6498ea](https://github.com/MariaDB/server/commit/745e6498ea)\
  2018-01-18 09:25:22 +0200
  * After-merge fix to a test
* Merge [Revision #4ef2e43080](https://github.com/MariaDB/server/commit/4ef2e43080) 2018-01-17 16:33:40 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #c6cd64f3cb](https://github.com/MariaDB/server/commit/c6cd64f3cb) 2018-01-17 16:22:27 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #656f66def2](https://github.com/MariaDB/server/commit/656f66def2)\
  2018-01-17 15:53:30 +0200
  * Follow-up fix to [MDEV-14585](https://jira.mariadb.org/browse/MDEV-14585) Automatically remove #sql- tables in InnoDB dictionary during recovery
* [Revision #04eef79bf9](https://github.com/MariaDB/server/commit/04eef79bf9)\
  2018-01-17 11:28:02 +0200
  * Do not define unused function mark\_blocks\_free()
* Merge [Revision #822f4e6c10](https://github.com/MariaDB/server/commit/822f4e6c10) 2018-01-16 07:51:02 +0200 - Merge 10.2 into bb-10.2-ext

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
