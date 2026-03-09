# MariaDB 10.2.25 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.25/)[Release Notes](../../old-releases/10.2/10.2.25.md)[Changelog](mariadb-10225-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 17 Jun 2019

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.25.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #21eed902f3](https://github.com/MariaDB/server/commit/21eed902f3)\
  2019-06-14 21:23:53 +0300
  * Updated list of unstable tests for 10.2.25
* [Revision #b40c2d2c51](https://github.com/MariaDB/server/commit/b40c2d2c51)\
  2019-06-14 12:28:51 +0200
  * [MDEV-19633](https://jira.mariadb.org/browse/MDEV-19633) ASAN use-after-poison in tree\_insert() in main.func\_gconcat
* Merge [Revision #50653e021f](https://github.com/MariaDB/server/commit/50653e021f) 2019-06-13 16:42:21 +0200 - Merge branch '10.1' into 10.2
* Merge [Revision #5b65d61d93](https://github.com/MariaDB/server/commit/5b65d61d93) 2019-06-12 22:54:46 +0200 - Merge branch '5.5' into 10.1
* [Revision #7a7d9904e1](https://github.com/MariaDB/server/commit/7a7d9904e1)\
  2019-06-11 12:02:26 +0300
  * [MDEV-18479](https://jira.mariadb.org/browse/MDEV-18479): Avoid COST\_MULT(records, 1)
* [Revision #96ee9ea02e](https://github.com/MariaDB/server/commit/96ee9ea02e)\
  2019-06-10 22:38:55 -0700
  * [MDEV-18479](https://jira.mariadb.org/browse/MDEV-18479) Another complement
* [Revision #6db2ebbb2a](https://github.com/MariaDB/server/commit/6db2ebbb2a)\
  2019-06-09 10:39:52 -0700
  * [MDEV-19580](https://jira.mariadb.org/browse/MDEV-19580) Unrelated JOINs corrupt usage of 'WHERE function() IN (subquery)'
* [Revision #6660c072ad](https://github.com/MariaDB/server/commit/6660c072ad)\
  2019-05-22 21:56:36 +0200
  * [MDEV-19491](https://jira.mariadb.org/browse/MDEV-19491) update query stopped working after mariadb upgrade 10.2.23 -> 10.2.24
* [Revision #1d4ac3d4d3](https://github.com/MariaDB/server/commit/1d4ac3d4d3)\
  2019-05-22 22:05:56 +0200
  * cleanup
* [Revision #5de08a53ef](https://github.com/MariaDB/server/commit/5de08a53ef)\
  2019-04-11 15:46:39 +0300
  * [MDEV-13631](https://jira.mariadb.org/browse/MDEV-13631) Make use of clang-format
* [Revision #cbb90f77cd](https://github.com/MariaDB/server/commit/cbb90f77cd)\
  2019-05-28 23:26:36 -0700
  * [MDEV-18479](https://jira.mariadb.org/browse/MDEV-18479) Complement
* [Revision #eb09580b67](https://github.com/MariaDB/server/commit/eb09580b67)\
  2019-05-28 14:53:08 -0700
  * [MDEV-19588](https://jira.mariadb.org/browse/MDEV-19588) Wrong results from query, using left join.
* [Revision #e9145aab44](https://github.com/MariaDB/server/commit/e9145aab44)\
  2019-06-13 16:31:06 +0530
  * [MDEV-19435](https://jira.mariadb.org/browse/MDEV-19435) buf\_fix\_count > 0 for corrupted page when it exits the LRU list
* [Revision #371a8a6615](https://github.com/MariaDB/server/commit/371a8a6615)\
  2019-06-13 13:18:54 +0300
  * Galera test cleanup.
* [Revision #06be8cd38f](https://github.com/MariaDB/server/commit/06be8cd38f)\
  2019-06-12 19:18:47 +0300
  * Clean up the test innodb.innodb-64k-crash
* Merge [Revision #1d31bed212](https://github.com/MariaDB/server/commit/1d31bed212) 2019-06-12 19:12:00 +0300 - Merge 10.1 into 10.2
* [Revision #56c60b2fc5](https://github.com/MariaDB/server/commit/56c60b2fc5)\
  2019-06-12 19:02:08 +0300
  * [MDEV-16111](https://jira.mariadb.org/browse/MDEV-16111) encryption.innodb\_lotoftables failed in buildbot with wrong result
* Merge [Revision #90fec9602f](https://github.com/MariaDB/server/commit/90fec9602f) 2019-06-12 16:28:45 +0300 - Merge 10.1 into 10.2
* [Revision #efc3cb9322](https://github.com/MariaDB/server/commit/efc3cb9322)\
  2019-06-12 12:50:19 +0300
  * [MDEV-19563](https://jira.mariadb.org/browse/MDEV-19563) Removed references to deprecated option innodb\_locks\_unsafe\_for\_binlog
* [Revision #9d886de499](https://github.com/MariaDB/server/commit/9d886de499)\
  2019-06-12 13:09:41 +0400
  * [MDEV-16467](https://jira.mariadb.org/browse/MDEV-16467) - MariaDB crashes because of "long semaphore wait"after migrating from 10.1 to 10.3
* [Revision #94e665596d](https://github.com/MariaDB/server/commit/94e665596d)\
  2019-06-12 16:17:23 +0300
  * [MDEV-19740](https://jira.mariadb.org/browse/MDEV-19740): Remove some broken InnoDB systemd code
* Merge [Revision #4bbd8be482](https://github.com/MariaDB/server/commit/4bbd8be482) 2019-06-12 10:25:34 +0300 - Merge 10.1 into 10.2
* [Revision #b2f76bac03](https://github.com/MariaDB/server/commit/b2f76bac03)\
  2019-06-12 12:25:00 +0530
  * [MDEV-16866](https://jira.mariadb.org/browse/MDEV-16866) InnoDB fails to start upon crash recovery with "\[ERROR] InnoDB: Redo log crypto: failed to decrypt log block"
* [Revision #c5fe1b8fc1](https://github.com/MariaDB/server/commit/c5fe1b8fc1)\
  2019-06-12 12:17:13 +0530
  * [MDEV-16866](https://jira.mariadb.org/browse/MDEV-16866) InnoDB fails to start upon crash recovery with "\[ERROR] InnoDB: Redo log crypto: failed to decrypt log block"
* [Revision #e7695f95ae](https://github.com/MariaDB/server/commit/e7695f95ae)\
  2019-06-07 12:24:27 +0400
  * [MDEV-19360](https://jira.mariadb.org/browse/MDEV-19360) - Disable \_FORTIFY\_SOURCE for ASAN builds
* [Revision #c97c8c28b5](https://github.com/MariaDB/server/commit/c97c8c28b5)\
  2019-06-05 19:42:21 +0200
  * [MDEV-17103](https://jira.mariadb.org/browse/MDEV-17103) MY\_CHECK\_{C,CXX}\_COMPILER\_FLAG do not work on with localized gcc messages
* [Revision #b003b0c934](https://github.com/MariaDB/server/commit/b003b0c934)\
  2019-06-03 12:42:36 +0400
  * [MDEV-19675](https://jira.mariadb.org/browse/MDEV-19675) Wrong charset is chosen when opening a pre-4.1 table
* [Revision #5a19908b95](https://github.com/MariaDB/server/commit/5a19908b95)\
  2019-05-31 15:24:40 +0400
  * [MDEV-19653](https://jira.mariadb.org/browse/MDEV-19653) Add class Sql\_cmd\_create\_table
* [Revision #dd939d6f7e](https://github.com/MariaDB/server/commit/dd939d6f7e)\
  2019-05-30 19:34:08 +0400
  * [MDEV-15734](https://jira.mariadb.org/browse/MDEV-15734) - calculation inside sizeof() warning
* [Revision #78c1be8b6b](https://github.com/MariaDB/server/commit/78c1be8b6b)\
  2019-05-30 12:11:57 +0530
  * [MDEV-18913](https://jira.mariadb.org/browse/MDEV-18913): typo in error log
* [Revision #a47464d1c1](https://github.com/MariaDB/server/commit/a47464d1c1)\
  2019-05-29 17:35:29 +0530
  * [MDEV-11094](https://jira.mariadb.org/browse/MDEV-11094): Blackhole table updates on slave fail when row annotation is enabled
* [Revision #b347396181](https://github.com/MariaDB/server/commit/b347396181)\
  2019-05-28 14:20:39 +0530
  * [MDEV-11094](https://jira.mariadb.org/browse/MDEV-11094): Blackhole table updates on slave fail when row annotation is enabled
* [Revision #34b38ad726](https://github.com/MariaDB/server/commit/34b38ad726)\
  2019-06-12 08:24:30 +0300
  * [MDEV-19736](https://jira.mariadb.org/browse/MDEV-19736): Galera test failure on
* [Revision #cbac8f9351](https://github.com/MariaDB/server/commit/cbac8f9351)\
  2019-06-10 18:15:25 +0300
  * [MDEV-19725](https://jira.mariadb.org/browse/MDEV-19725) Incorrect error handling in ALTER TABLE
* [Revision #5d06edfb26](https://github.com/MariaDB/server/commit/5d06edfb26)\
  2019-06-08 02:28:29 +0300
  * [MDEV-19714](https://jira.mariadb.org/browse/MDEV-19714): JOIN::pseudo\_bits\_cond is not visible in EXPLAIN FORMAT=JSON
* [Revision #9b22354a59](https://github.com/MariaDB/server/commit/9b22354a59)\
  2019-06-07 00:07:14 +0200
  * Fix mysql-test-run.pl to work after d6d5c168cf1
* [Revision #dfe7968c6e](https://github.com/MariaDB/server/commit/dfe7968c6e)\
  2019-06-06 16:38:03 +0300
  * Fixed typo in Config.pgm
* [Revision #b83aff56f1](https://github.com/MariaDB/server/commit/b83aff56f1)\
  2019-06-06 15:25:15 +0300
  * Support skip-plugin-load
* [Revision #d6d5c168cf](https://github.com/MariaDB/server/commit/d6d5c168cf)\
  2019-06-06 15:23:12 +0300
  * Fixed that test suite doesn't remove duplicate options
* [Revision #bb5d04c9b8](https://github.com/MariaDB/server/commit/bb5d04c9b8)\
  2019-06-06 12:49:34 +0530
  * [MDEV-19695](https://jira.mariadb.org/browse/MDEV-19695) Import tablespace doesn't work with ROW\_FORMAT=COMPRESSED encrypted tablespace
* [Revision #d7c8423a3d](https://github.com/MariaDB/server/commit/d7c8423a3d)\
  2019-02-27 08:31:35 +0000
  * fix [MDEV-18750](https://jira.mariadb.org/browse/MDEV-18750): failed to flashback large-size binlog file
* [Revision #b4287ec386](https://github.com/MariaDB/server/commit/b4287ec386)\
  2019-06-05 16:36:51 +0530
  * [MDEV-19541](https://jira.mariadb.org/browse/MDEV-19541) InnoDB crashes when trying to recover a corrupted page
* [Revision #7906bee67b](https://github.com/MariaDB/server/commit/7906bee67b)\
  2019-06-04 12:41:52 +0530
  * [MDEV-18015](https://jira.mariadb.org/browse/MDEV-18015): Assertion \`global\_status\_var.global\_memory\_used == 0' failed when using UDF , window functions and views
* [Revision #aa83b9cf4f](https://github.com/MariaDB/server/commit/aa83b9cf4f)\
  2019-05-18 11:38:43 +0200
  * update a test result, followup fae6539ef72
* [Revision #40becbc3c7](https://github.com/MariaDB/server/commit/40becbc3c7)\
  2019-06-02 16:30:33 +0300
  * Fixed bug in online alter table when not compiled with performance schema
* [Revision #1bfa7ceb72](https://github.com/MariaDB/server/commit/1bfa7ceb72)\
  2019-06-02 13:53:48 +0300
  * Supress some valgrind warnings
* [Revision #05f8120d0e](https://github.com/MariaDB/server/commit/05f8120d0e)\
  2019-06-02 13:53:16 +0300
  * Fixed compiler warning
* [Revision #76f14be10f](https://github.com/MariaDB/server/commit/76f14be10f)\
  2019-06-02 11:47:36 +0300
  * Ensure that tests and programs can restore variables
* [Revision #2d89a70fac](https://github.com/MariaDB/server/commit/2d89a70fac)\
  2019-06-02 11:35:12 +0300
  * Fix plugin linking on Windows
* [Revision #724aefa56d](https://github.com/MariaDB/server/commit/724aefa56d)\
  2019-06-03 13:52:33 +0200
  * Fix linking error, for GNU linker.
* [Revision #e730ea1e3e](https://github.com/MariaDB/server/commit/e730ea1e3e)\
  2019-06-03 09:55:40 +0200
  * Only link mysys\_ssl when required.
* [Revision #c9b49a4be7](https://github.com/MariaDB/server/commit/c9b49a4be7)\
  2019-05-24 13:09:13 +0300
  * [MDEV-18207](https://jira.mariadb.org/browse/MDEV-18207): ASAN heap-use-after-free in \_ma\_get\_status upon concurrent operations with sequence
* [Revision #9d142a895c](https://github.com/MariaDB/server/commit/9d142a895c)\
  2019-05-30 20:59:34 +0300
  * Define page\_id\_t in buf0types.h
* [Revision #80a142f146](https://github.com/MariaDB/server/commit/80a142f146)\
  2019-05-30 17:19:13 +0400
  * Lintian complains about script-not-executable
* [Revision #4adf52a048](https://github.com/MariaDB/server/commit/4adf52a048)\
  2019-05-22 12:53:35 +0200
  * Add missing script header
* [Revision #1d0c27412c](https://github.com/MariaDB/server/commit/1d0c27412c)\
  2019-05-29 13:03:32 +0300
  * [MDEV-19541](https://jira.mariadb.org/browse/MDEV-19541): Suppress an error also on Windows
* [Revision #6eefeb6fea](https://github.com/MariaDB/server/commit/6eefeb6fea)\
  2019-05-29 11:20:56 +0300
  * [MDEV-19541](https://jira.mariadb.org/browse/MDEV-19541): Avoid infinite loop of reading a corrupted page
* [Revision #eeee1832d7](https://github.com/MariaDB/server/commit/eeee1832d7)\
  2019-05-29 08:28:15 +0300
  * Speed up buildbot by requiring --big-test for some slow tests
* [Revision #642ddc3131](https://github.com/MariaDB/server/commit/642ddc3131)\
  2019-05-29 08:14:49 +0300
  * [MDEV-19541](https://jira.mariadb.org/browse/MDEV-19541): Add a forgotten test case
* [Revision #1ca75ae1c8](https://github.com/MariaDB/server/commit/1ca75ae1c8)\
  2019-05-28 16:43:02 +0300
  * [MDEV-19587](https://jira.mariadb.org/browse/MDEV-19587) innodb\_force\_recovery=5 crash on DROP SCHEMA
* [Revision #96d9f03328](https://github.com/MariaDB/server/commit/96d9f03328)\
  2019-05-28 18:31:20 +0530
  * [MDEV-19602](https://jira.mariadb.org/browse/MDEV-19602) Replace mysql\_version check with frm\_version for virtual columns inside InnoDB
* Merge [Revision #d59e15bdb9](https://github.com/MariaDB/server/commit/d59e15bdb9) 2019-05-28 15:56:24 +0300 - Merge 10.1 into 10.2
* [Revision #8358c6f03e](https://github.com/MariaDB/server/commit/8358c6f03e)\
  2019-05-28 15:24:32 +0300
  * [MDEV-19614](https://jira.mariadb.org/browse/MDEV-19614): Fix innodb\_plugin on Windows
* Merge [Revision #bf8fe324d2](https://github.com/MariaDB/server/commit/bf8fe324d2) 2019-05-28 11:25:45 +0300 - Merge 5.5 into 10.1
* [Revision #0955462d0a](https://github.com/MariaDB/server/commit/0955462d0a)\
  2019-05-27 19:08:00 -0700
  * [MDEV-18479](https://jira.mariadb.org/browse/MDEV-18479) Assertion \`join->best\_read < double(1.79769313486231570815e+308L)' or server crashes in JOIN::fix\_all\_splittings\_in\_plan after EXPLAIN
* [Revision #4584c18631](https://github.com/MariaDB/server/commit/4584c18631)\
  2019-05-22 00:52:15 +0200
  * make CPACK\_RPM\_DEBUGINFO\_PACKAGE configurable from the command-line
* [Revision #5034b31b01](https://github.com/MariaDB/server/commit/5034b31b01)\
  2019-05-20 18:23:10 +0200
  * [MDEV-17799](https://jira.mariadb.org/browse/MDEV-17799) Add ASAN-poisoned redzones for MEM\_ROOT
* [Revision #7b59ec6f34](https://github.com/MariaDB/server/commit/7b59ec6f34)\
  2018-11-28 13:25:43 +0300
  * [MDEV-17799](https://jira.mariadb.org/browse/MDEV-17799) Add ASAN-poisoned redzones for MEM\_ROOT and mem\_heap\_t
* [Revision #2c9844a438](https://github.com/MariaDB/server/commit/2c9844a438)\
  2019-05-19 11:44:34 -0700
  * [MDEV-18896](https://jira.mariadb.org/browse/MDEV-18896) Crash in convert\_join\_subqueries\_to\_semijoins : Correction
* [Revision #626f2a1c17](https://github.com/MariaDB/server/commit/626f2a1c17)\
  2019-05-28 10:50:17 +0300
  * [MDEV-19614](https://jira.mariadb.org/browse/MDEV-19614) SET GLOBAL innodb\_ deadlock due to LOCK\_global\_system\_variables
* [Revision #242a28c320](https://github.com/MariaDB/server/commit/242a28c320)\
  2019-05-28 08:07:45 +0300
  * [MDEV-6812](https://jira.mariadb.org/browse/MDEV-6812): Remove the wrapper my\_log2f()
* [Revision #661289f462](https://github.com/MariaDB/server/commit/661289f462)\
  2019-05-21 09:20:49 +0300
  * Mention the sample IPv4 address 10.0.0.1
* [Revision #aaf53ea0b6](https://github.com/MariaDB/server/commit/aaf53ea0b6)\
  2019-05-23 21:12:14 +0300
  * [MDEV-17948](https://jira.mariadb.org/browse/MDEV-17948) Assertion \`thd\_killed(thd) || !m\_active\_tranxs ..
* [Revision #e57bb1f76c](https://github.com/MariaDB/server/commit/e57bb1f76c)\
  2019-05-14 23:58:56 -0700
  * [MDEV-19258](https://jira.mariadb.org/browse/MDEV-19258) RIGHT JOIN hangs in MariaDB
* [Revision #aad4e5637d](https://github.com/MariaDB/server/commit/aad4e5637d)\
  2019-05-22 12:20:02 +0300
  * Stale files cause intermittent failure when ordering is unfortunate
* [Revision #6dbc2ab8b3](https://github.com/MariaDB/server/commit/6dbc2ab8b3)\
  2019-05-20 17:44:55 +0530
  * [MDEV-17752](https://jira.mariadb.org/browse/MDEV-17752): Plan changes from hash\_index\_merge to index\_merge with new optimizer defaults
* [Revision #aaa920dad3](https://github.com/MariaDB/server/commit/aaa920dad3)\
  2019-05-21 14:54:03 +0200
  * [MDEV-19537](https://jira.mariadb.org/browse/MDEV-19537): Document mysqlimport option ignore-foreign-keys
* [Revision #88157247fc](https://github.com/MariaDB/server/commit/88157247fc)\
  2019-05-17 20:32:51 +0530
  * [MDEV-19509](https://jira.mariadb.org/browse/MDEV-19509) InnoDB skips the tablespace in rotation list
* [Revision #79b46ab2a6](https://github.com/MariaDB/server/commit/79b46ab2a6)\
  2019-05-23 14:25:54 +0530
  * [MDEV-19541](https://jira.mariadb.org/browse/MDEV-19541) InnoDB crashes when trying to recover a corrupted page
* [Revision #b8b74e141d](https://github.com/MariaDB/server/commit/b8b74e141d)\
  2019-05-27 21:28:33 +0530
  * [MDEV-19027](https://jira.mariadb.org/browse/MDEV-19027) create\_table\_def fails when virtual column is present between stored columns
* [Revision #35522455e0](https://github.com/MariaDB/server/commit/35522455e0)\
  2018-11-22 14:51:31 +1100
  * RocksDB: use crc32c optimised version for POWER
* [Revision #bff9b8026b](https://github.com/MariaDB/server/commit/bff9b8026b)\
  2019-05-16 11:04:39 +0300
  * [MDEV-14192](https://jira.mariadb.org/browse/MDEV-14192): mariadb-backup.incremental\_backup failed in buildbot with Failing assertion: byte\_offset % OS\_FILE\_LOG\_BLOCK\_SIZE == 0
* [Revision #c874040729](https://github.com/MariaDB/server/commit/c874040729)\
  2019-05-24 10:22:34 +0300
  * Declare INFORMATION\_SCHEMA.INNODB\_SYS\_VIRTUAL stable
* Merge [Revision #b90918dae3](https://github.com/MariaDB/server/commit/b90918dae3) 2019-05-21 15:45:52 +0300 - Merge 10.1 into 10.2
* [Revision #91efcc6392](https://github.com/MariaDB/server/commit/91efcc6392)\
  2019-05-17 19:17:19 +0300
  * Better comment from Monty for code in make\_join\_select
* [Revision #c84f390df2](https://github.com/MariaDB/server/commit/c84f390df2)\
  2019-05-14 10:50:49 +0300
  * [MDEV-16021](https://jira.mariadb.org/browse/MDEV-16021): galera mtr test galera\_evs\_suspect\_timeout crashed
* [Revision #61469b3a3b](https://github.com/MariaDB/server/commit/61469b3a3b)\
  2019-05-13 13:23:52 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Timeout in wait\_condition.inc for PROCESSLIST
* [Revision #579c1a8c20](https://github.com/MariaDB/server/commit/579c1a8c20)\
  2019-05-13 11:31:01 +0300
  * [MDEV-17061](https://jira.mariadb.org/browse/MDEV-17061): Test failure on galera.galera\_gcs\_fc\_limit
* [Revision #3a871c39a9](https://github.com/MariaDB/server/commit/3a871c39a9)\
  2017-09-05 16:24:29 +0300
  * Fixed monitor.test to handle statistics >= 10
* [Revision #71ee69c81c](https://github.com/MariaDB/server/commit/71ee69c81c)\
  2019-05-20 17:45:32 +0400
  * [MDEV-17456](https://jira.mariadb.org/browse/MDEV-17456) Malicious SUPER user can possibly change audit log configuration without leaving traces.
* [Revision #74904a667e](https://github.com/MariaDB/server/commit/74904a667e)\
  2019-05-20 17:00:21 +0300
  * Remove UT\_NOT\_USED
* [Revision #5a2110e7cf](https://github.com/MariaDB/server/commit/5a2110e7cf)\
  2019-05-16 16:36:20 +0530
  * [MDEV-19076](https://jira.mariadb.org/browse/MDEV-19076): rpl\_parallel\_temptable result mismatch '-33 optimistic'
* [Revision #d4e9a50e88](https://github.com/MariaDB/server/commit/d4e9a50e88)\
  2019-05-19 23:50:23 +0400
  * [MDEV-17456](https://jira.mariadb.org/browse/MDEV-17456) Malicious SUPER user can possibly change audit log configuration without leaving traces.
* [Revision #395ce1dcb3](https://github.com/MariaDB/server/commit/395ce1dcb3)\
  2019-05-14 10:50:49 +0300
  * [MDEV-16021](https://jira.mariadb.org/browse/MDEV-16021): galera mtr test galera\_evs\_suspect\_timeout crashed
* [Revision #cd87e4e134](https://github.com/MariaDB/server/commit/cd87e4e134)\
  2019-05-13 13:23:52 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Timeout in wait\_condition.inc for PROCESSLIST
* [Revision #bc511443b1](https://github.com/MariaDB/server/commit/bc511443b1)\
  2019-05-13 11:31:01 +0300
  * [MDEV-17061](https://jira.mariadb.org/browse/MDEV-17061): Test failure on galera.galera\_gcs\_fc\_limit
* [Revision #fae6539ef7](https://github.com/MariaDB/server/commit/fae6539ef7)\
  2019-05-17 16:52:05 +0200
  * restore the correct test result
* [Revision #cd16d6d518](https://github.com/MariaDB/server/commit/cd16d6d518)\
  2019-05-17 11:53:58 +0400
  * [MDEV-13992](https://jira.mariadb.org/browse/MDEV-13992) Implement JSON\_MERGE\_PATCH.
* [Revision #da6e55f022](https://github.com/MariaDB/server/commit/da6e55f022)\
  2019-05-17 13:01:00 +0530
  * [MDEV-19472](https://jira.mariadb.org/browse/MDEV-19472): eq\_range\_index\_dive\_limit cannot be configured in server.cnf Fixed, now server can be configured with eq\_range\_index\_dive\_limit set in cnf file
* [Revision #b546e92a6b](https://github.com/MariaDB/server/commit/b546e92a6b)\
  2019-05-16 20:28:00 +0400
  * Fixed rocksdb.mariadb\_plugin on Windows
* [Revision #ef04a7123a](https://github.com/MariaDB/server/commit/ef04a7123a)\
  2019-05-16 18:30:31 +0300
  * [MDEV-19490](https://jira.mariadb.org/browse/MDEV-19490) show tables fails when selecting the information\_schema database
* [Revision #5f66c58f6d](https://github.com/MariaDB/server/commit/5f66c58f6d)\
  2019-05-16 18:27:28 +0400
  * Issue #904: Crash in rocksdb::IOStatsContext::Reset, this=NULL Fix both code paths: - Change the test source code so it doesn't cause the "Unused variable" warning (which -Werror converted into error and caused CMake not to set HAVE\_THREAD\_LOCAL)
* [Revision #76a94a03db](https://github.com/MariaDB/server/commit/76a94a03db)\
  2019-05-16 17:48:47 +0400
  * [MDEV-19090](https://jira.mariadb.org/browse/MDEV-19090) - Split rocksdb.locking\_issues
* [Revision #a24dffdba3](https://github.com/MariaDB/server/commit/a24dffdba3)\
  2019-05-16 12:41:19 +0400
  * Fixed RocksDB to follow THD ha\_data protocol
* [Revision #8a880d69ec](https://github.com/MariaDB/server/commit/8a880d69ec)\
  2019-05-16 14:54:54 +0400
  * Fixed InnoDB to not use broken thd\_ha\_data()
* [Revision #796486d19b](https://github.com/MariaDB/server/commit/796486d19b)\
  2019-05-16 14:17:22 +0300
  * [MDEV-19485](https://jira.mariadb.org/browse/MDEV-19485): Add a test case
* Merge [Revision #c41407210c](https://github.com/MariaDB/server/commit/c41407210c) 2019-05-16 11:55:18 +0300 - Merge 10.1 into 10.2
* [Revision #70a5fb49a7](https://github.com/MariaDB/server/commit/70a5fb49a7)\
  2019-05-16 13:49:47 +0530
  * Fixed the case when statistics were not getting read because we had the statistics tables in the FROM list of the select. The statistics for tables are not read in such cases, so we need to check this case separately.
* [Revision #6ab9d1627a](https://github.com/MariaDB/server/commit/6ab9d1627a)\
  2019-05-15 01:38:28 +0530
  * [MDEV-19407](https://jira.mariadb.org/browse/MDEV-19407): Assertion \`field->table->stats\_is\_read' failed in is\_eits\_usable
* [Revision #a941e58fb8](https://github.com/MariaDB/server/commit/a941e58fb8)\
  2019-05-13 12:30:35 +0300
  * [MDEV-788](https://jira.mariadb.org/browse/MDEV-788) mysqlimport should support the ability to disable foreign keys
* [Revision #56976e60f5](https://github.com/MariaDB/server/commit/56976e60f5)\
  2019-05-14 17:59:47 +0300
  * [MDEV-13080](https://jira.mariadb.org/browse/MDEV-13080) \[ERROR] InnoDB: Missing MLOG\_CHECKPOINT between the checkpoint x and the end y
* [Revision #409e210e74](https://github.com/MariaDB/server/commit/409e210e74)\
  2019-05-14 15:29:24 +0300
  * [MDEV-19449](https://jira.mariadb.org/browse/MDEV-19449) Got error 168 for valid TRUNCATE (temporary) TABLE
* [Revision #95fb88d546](https://github.com/MariaDB/server/commit/95fb88d546)\
  2018-09-12 16:36:45 +0400
  * [MDEV-17167](https://jira.mariadb.org/browse/MDEV-17167) - InnoDB: Failing assertion: table->get\_ref\_count() == 0 upon truncating a temporary table
* [Revision #43bbf88dcb](https://github.com/MariaDB/server/commit/43bbf88dcb)\
  2019-05-14 16:06:55 +0530
  * [MDEV-19158](https://jira.mariadb.org/browse/MDEV-19158): [MariaDB 10.2.22](../../old-releases/10.2/10.2.22.md) is writing duplicate entries into binary log
* Merge [Revision #d0d663f3db](https://github.com/MariaDB/server/commit/d0d663f3db) 2019-05-14 16:05:09 +0530 - Merge branch '10.1' into 10.2
* [Revision #47637a3dd1](https://github.com/MariaDB/server/commit/47637a3dd1)\
  2019-05-14 13:03:06 +0530
  * [MDEV-11095](https://jira.mariadb.org/browse/MDEV-11095): rpl.rpl\_row\_mysqlbinlog test fails if row annotation enabled
* Merge [Revision #50999738ea](https://github.com/MariaDB/server/commit/50999738ea) 2019-05-13 18:47:30 +0300 - Merge 10.1 into 10.2
* [Revision #2647fd101d](https://github.com/MariaDB/server/commit/2647fd101d)\
  2019-05-13 17:16:42 +0300
  * [MDEV-19445](https://jira.mariadb.org/browse/MDEV-19445) heap-use-after-free related to innodb\_ft\_aux\_table
* [Revision #1c97e07f8f](https://github.com/MariaDB/server/commit/1c97e07f8f)\
  2019-05-13 17:07:13 +0300
  * fts\_optimize\_words(): Remove stray output
* [Revision #c7c54ce606](https://github.com/MariaDB/server/commit/c7c54ce606)\
  2019-05-13 11:32:20 +0300
  * fts\_doc\_ids\_free(): Define inline
* [Revision #7f7211073c](https://github.com/MariaDB/server/commit/7f7211073c)\
  2019-05-13 08:48:22 +0300
  * [MDEV-19441](https://jira.mariadb.org/browse/MDEV-19441) Typo in error message "InnoDB: FTS Doc ID must be large than"
* [Revision #b93ecea65c](https://github.com/MariaDB/server/commit/b93ecea65c)\
  2019-05-13 18:26:59 +0300
  * Remove unnecessary pointer indirection for rw\_lock\_t
* Merge [Revision #26a14ee130](https://github.com/MariaDB/server/commit/26a14ee130) 2019-05-13 17:47:26 +0300 - Merge 10.1 into 10.2
* Merge [Revision #cb248f8806](https://github.com/MariaDB/server/commit/cb248f8806) 2019-05-11 22:19:05 +0300 - Merge branch '5.5' into 10.1
* [Revision #5543b75550](https://github.com/MariaDB/server/commit/5543b75550)\
  2019-05-11 21:29:06 +0300
  * Update FSF Address
* [Revision #c0ac0b8860](https://github.com/MariaDB/server/commit/c0ac0b8860)\
  2019-05-11 19:25:02 +0300
  * Update FSF address
* Merge [Revision #f177f125d4](https://github.com/MariaDB/server/commit/f177f125d4) 2019-05-11 19:15:57 +0300 - Merge branch '5.5' into 10.1
* [Revision #15f1e03d46](https://github.com/MariaDB/server/commit/15f1e03d46)\
  2019-05-11 18:08:32 +0300
  * Follow-up to changing FSF address
* [Revision #17b4f99928](https://github.com/MariaDB/server/commit/17b4f99928)\
  2019-05-10 20:49:46 +0300
  * Update FSF address
* [Revision #8ce702aa90](https://github.com/MariaDB/server/commit/8ce702aa90)\
  2019-05-10 10:49:09 +0300
  * [MDEV-17540](https://jira.mariadb.org/browse/MDEV-17540) Server crashes in row\_purge after TRUNCATE TABLE
* Merge [Revision #b2f3755c8e](https://github.com/MariaDB/server/commit/b2f3755c8e) 2019-05-10 08:02:21 +0300 - Merge 10.1 into 10.2
* [Revision #3e8cab51cb](https://github.com/MariaDB/server/commit/3e8cab51cb)\
  2019-05-07 12:53:50 +0530
  * [MDEV-13893](https://jira.mariadb.org/browse/MDEV-13893) encryption.innodb-redo-badkey failed in buildbot with page cannot be decrypted
* [Revision #542f32649b](https://github.com/MariaDB/server/commit/542f32649b)\
  2019-05-09 10:41:10 +0300
  * [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220): race condition in fts\_get\_table\_name()
* [Revision #f3718a112a](https://github.com/MariaDB/server/commit/f3718a112a)\
  2019-05-09 09:31:30 +0300
  * [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220): Backport some code from [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md)
* [Revision #f92749ed36](https://github.com/MariaDB/server/commit/f92749ed36)\
  2019-05-08 12:18:52 +0300
  * [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220): heap-use-after-free in fts\_get\_table\_name\_prefix()
* [Revision #5b3f7c0c33](https://github.com/MariaDB/server/commit/5b3f7c0c33)\
  2019-05-09 14:08:49 +0300
  * [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220): Remove some redundant data structures
* [Revision #06442e3e9f](https://github.com/MariaDB/server/commit/06442e3e9f)\
  2019-05-06 22:30:35 +0300
  * [MDEV-19399](https://jira.mariadb.org/browse/MDEV-19399) do not call slow my\_timer\_init() several times
* [Revision #d0ee3b5500](https://github.com/MariaDB/server/commit/d0ee3b5500)\
  2019-05-09 16:55:08 +0200
  * [MDEV-19427](https://jira.mariadb.org/browse/MDEV-19427) mysql\_upgrade\_service throws exception upgrading from 10.0 to 10.3
* [Revision #410585ca63](https://github.com/MariaDB/server/commit/410585ca63)\
  2019-05-01 15:22:22 +0400
  * Removed dead code
* [Revision #d0b73fb8d3](https://github.com/MariaDB/server/commit/d0b73fb8d3)\
  2019-03-29 19:08:22 +0400
  * [MDEV-16060](https://jira.mariadb.org/browse/MDEV-16060) - InnoDB: Failing assertion: ut\_strcmp(index->name, key->name)
* [Revision #136a27d9f1](https://github.com/MariaDB/server/commit/136a27d9f1)\
  2019-05-09 11:55:54 -0400
  * bump the VERSION
* [Revision #8f9c8579d0](https://github.com/MariaDB/server/commit/8f9c8579d0)\
  2019-01-09 15:00:56 +0200
  * Appveyor configuration and addition of badge
* Merge [Revision #9d3e2a7ca2](https://github.com/MariaDB/server/commit/9d3e2a7ca2) 2019-05-08 20:05:30 +0300 - Merge 10.1 into 10.2
* [Revision #3e5526b0df](https://github.com/MariaDB/server/commit/3e5526b0df)\
  2019-05-08 09:54:26 -0400
  * bump the VERSION
* Merge [Revision #4ad720282d](https://github.com/MariaDB/server/commit/4ad720282d) 2019-05-08 16:46:38 +0300 - Null merge mariadb-10.1.40 into 10.1
* [Revision #7b93d71a4b](https://github.com/MariaDB/server/commit/7b93d71a4b)\
  2019-05-07 15:21:41 +0530
  * [MDEV-19387](https://jira.mariadb.org/browse/MDEV-19387) innodb\_ft\_result\_cache\_limit\_32 fails on s390x
* [Revision #db9622f1f5](https://github.com/MariaDB/server/commit/db9622f1f5)\
  2019-05-07 12:51:59 +0300
  * [MDEV-19405](https://jira.mariadb.org/browse/MDEV-19405): Galera test failure on galera\_parallel\_autoinc\_largetrx
* [Revision #27232a9fa2](https://github.com/MariaDB/server/commit/27232a9fa2)\
  2018-05-31 17:42:54 -0700
  * edit MariaDB license info so that GitHub recognizes it
* [Revision #f2e27d53da](https://github.com/MariaDB/server/commit/f2e27d53da)\
  2019-04-24 12:47:40 +0300
  * [MDEV-19139](https://jira.mariadb.org/browse/MDEV-19139): pushdown condition with Item\_func\_set\_user\_var

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
