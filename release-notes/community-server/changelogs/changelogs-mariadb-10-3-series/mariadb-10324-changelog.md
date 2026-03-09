# MariaDB 10.3.24 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.24/)[Release Notes](../../old-releases/10.3/10.3.24.md)[Changelog](mariadb-10324-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 10 Aug 2020

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.24.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.33](../changelogs-mariadb-102-series/mariadb-10233-changelog.md)
* Merge [Revision #4668e079ee](https://github.com/MariaDB/server/commit/4668e079ee) 2020-08-06 17:01:44 +0200 - Merge branch '10.2' into 10.3
* [Revision #223aee2ebf](https://github.com/MariaDB/server/commit/223aee2ebf)\
  2020-08-04 02:16:32 +0300
  * List of unstable tests for 10.3.24 release
* Merge [Revision #c32f71af7e](https://github.com/MariaDB/server/commit/c32f71af7e) 2020-08-03 13:41:29 +0200 - Merge branch '10.2' into 10.3
* Merge [Revision #555c6632c6](https://github.com/MariaDB/server/commit/555c6632c6) 2020-08-03 13:04:32 +0200 - Merge branch '10.1' into 10.2
* [Revision #4d41f316c3](https://github.com/MariaDB/server/commit/4d41f316c3)\
  2020-08-02 20:39:47 +0200
  * disable galera.MW-328A test
* Merge [Revision #297746dea0](https://github.com/MariaDB/server/commit/297746dea0) 2020-08-01 10:45:44 +0300 - [MDEV-21201](https://jira.mariadb.org/browse/MDEV-21201): Null-Merge 10.3
* [Revision #976abe64df](https://github.com/MariaDB/server/commit/976abe64df)\
  2020-08-01 10:38:50 +0300
  * [MDEV-21201](https://jira.mariadb.org/browse/MDEV-21201): Add --sorted\_result to the test, for 10.4
* [Revision #7f4c749d64](https://github.com/MariaDB/server/commit/7f4c749d64)\
  2020-08-01 10:38:50 +0300
  * [MDEV-21201](https://jira.mariadb.org/browse/MDEV-21201): Add --sorted\_result to the test, for 10.4
* [Revision #d63631c3fa](https://github.com/MariaDB/server/commit/d63631c3fa)\
  2020-07-08 08:31:32 +0400
  * [MDEV-19632](https://jira.mariadb.org/browse/MDEV-19632) Replication aborts with ER\_SLAVE\_CONVERSION\_FAILED upon CREATE ... SELECT in ORACLE mode
* [Revision #a8458a2345](https://github.com/MariaDB/server/commit/a8458a2345)\
  2020-07-08 16:26:34 +0200
  * [MDEV-21201](https://jira.mariadb.org/browse/MDEV-21201) No records produced in information\_schema query, depending on projection
* Merge [Revision #78c2a5ab70](https://github.com/MariaDB/server/commit/78c2a5ab70) 2020-07-31 14:17:39 +0300 - Merge 10.2 into 10.3
* Merge [Revision #8bb2170d74](https://github.com/MariaDB/server/commit/8bb2170d74) 2020-07-31 14:13:34 +0300 - Merge 10.2 into 10.3
* Merge [Revision #66ec3a770f](https://github.com/MariaDB/server/commit/66ec3a770f) 2020-07-31 13:51:28 +0300 - Merge 10.2 into 10.3
* [Revision #6053eb1ce2](https://github.com/MariaDB/server/commit/6053eb1ce2)\
  2020-07-30 18:40:47 +0300
  * [MDEV-23334](https://jira.mariadb.org/browse/MDEV-23334) Crash in rec\_get\_nth\_cfield()/rec\_offs\_validate()
* [Revision #0435fcf90b](https://github.com/MariaDB/server/commit/0435fcf90b)\
  2020-07-30 12:08:07 +0200
  * [MDEV-21101](https://jira.mariadb.org/browse/MDEV-21101) skip test for embedded
* [Revision #71015d844e](https://github.com/MariaDB/server/commit/71015d844e)\
  2020-07-28 15:59:38 +0200
  * [MDEV-21101](https://jira.mariadb.org/browse/MDEV-21101) unexpected wait\_timeout with pool-of-threads
* [Revision #34f2be3b29](https://github.com/MariaDB/server/commit/34f2be3b29)\
  2018-07-24 01:49:59 +1000
  * [MDEV-16023](https://jira.mariadb.org/browse/MDEV-16023) Unfortunate error message WARN\_VERS\_PART\_FULL (partition is full) when rotation time for the last interval passed
* [Revision #1656ea28e8](https://github.com/MariaDB/server/commit/1656ea28e8)\
  2020-07-23 17:41:44 +0300
  * [MDEV-23244](https://jira.mariadb.org/browse/MDEV-23244) ALTER TABLE…ADD PRIMARY KEY fails to flag duplicates
* [Revision #f7adc4a11d](https://github.com/MariaDB/server/commit/f7adc4a11d)\
  2020-07-22 10:30:00 +0200
  * A bit more safety
* [Revision #0ec641ea1e](https://github.com/MariaDB/server/commit/0ec641ea1e)\
  2020-07-21 14:56:47 +0200
  * [MDEV-22134](https://jira.mariadb.org/browse/MDEV-22134): handle\_fatal\_signal (sig=11) in `__strlen_avx2` on START SLAVE | Assertion \`\`global\_system\_variables.session\_track\_system\_variables'`failed in Session_sysvars_tracker::init |`\*\*\* buffer overflow detected \*\*\*\` (on optimized builds)
* [Revision #c86accc7ac](https://github.com/MariaDB/server/commit/c86accc7ac)\
  2020-07-20 17:57:39 +0530
  * [MDEV-23108](https://jira.mariadb.org/browse/MDEV-23108): Point in time recovery of binary log fails when sql\_mode=ORACLE
* [Revision #b75563cdfd](https://github.com/MariaDB/server/commit/b75563cdfd)\
  2020-07-21 15:59:45 +0300
  * [MDEV-15880](https://jira.mariadb.org/browse/MDEV-15880): ASAN heap-use-after-free with innodb\_evict\_tables\_on\_commit\_debug
* [Revision #e26c822aa0](https://github.com/MariaDB/server/commit/e26c822aa0)\
  2020-07-21 15:12:53 +0300
  * [MDEV-16929](https://jira.mariadb.org/browse/MDEV-16929) Assertion ... in close\_thread\_tables upon killing connection
* [Revision #af83ed9f0e](https://github.com/MariaDB/server/commit/af83ed9f0e)\
  2020-07-20 18:28:08 +0300
  * [MDEV-20661](https://jira.mariadb.org/browse/MDEV-20661) Virtual fields are not recalculated on system fields value assignment
* [Revision #af57c65809](https://github.com/MariaDB/server/commit/af57c65809)\
  2020-07-20 18:28:07 +0300
  * [MDEV-22061](https://jira.mariadb.org/browse/MDEV-22061) InnoDB: Assertion of missing row in sec index row\_start upon REPLACE on a system-versioned table
* Merge [Revision #acc58fd835](https://github.com/MariaDB/server/commit/acc58fd835) 2020-07-20 15:11:59 +0300 - Merge 10.2 into 10.3
* [Revision #2cae58f891](https://github.com/MariaDB/server/commit/2cae58f891)\
  2020-07-17 12:20:23 +0400
  * [MDEV-18371](https://jira.mariadb.org/browse/MDEV-18371) Server crashes in ha\_innobase::cmp\_ref upon UPDATE with PARTITION clause.
* Merge [Revision #73aa31fbfd](https://github.com/MariaDB/server/commit/73aa31fbfd) 2020-07-16 06:55:23 +0300 - Merge 10.2 into 10.3
* Merge [Revision #8a0944080c](https://github.com/MariaDB/server/commit/8a0944080c) 2020-07-14 17:13:37 +0300 - Merge 10.2 into 10.3
* [Revision #f3f23b5c4b](https://github.com/MariaDB/server/commit/f3f23b5c4b)\
  2020-07-05 16:31:34 +0300
  * One more ASAN/MSAN cleanup
* [Revision #453dc4b300](https://github.com/MariaDB/server/commit/453dc4b300)\
  2020-07-04 22:02:30 +0300
  * Fixup the parent commit for MSAN and Valgrind
* [Revision #484931325e](https://github.com/MariaDB/server/commit/484931325e)\
  2020-07-03 18:37:33 +0300
  * Fix for MSAN from Marko related to buf\_pool\_resize
* [Revision #6e81ba0c12](https://github.com/MariaDB/server/commit/6e81ba0c12)\
  2020-07-03 01:16:31 +0300
  * Don't give errors for default value copy in create\_tmp\_table
* [Revision #53ecc354e3](https://github.com/MariaDB/server/commit/53ecc354e3)\
  2020-07-02 23:50:56 +0300
  * Fixed errors found by MSAN
* [Revision #b6ec1e8bbf](https://github.com/MariaDB/server/commit/b6ec1e8bbf)\
  2020-07-02 16:52:13 +0300
  * [MDEV-20377](https://jira.mariadb.org/browse/MDEV-20377) post-fix: Introduce MEM\_MAKE\_ADDRESSABLE
* [Revision #65f831d17c](https://github.com/MariaDB/server/commit/65f831d17c)\
  2020-06-28 20:07:32 +0300
  * Fixed bugs found by valgrind
* [Revision #29f9e679ad](https://github.com/MariaDB/server/commit/29f9e679ad)\
  2019-08-14 23:46:47 +0300
  * Don't copy uninitialized bytes when copying varstrings
* [Revision #3f2044ae99](https://github.com/MariaDB/server/commit/3f2044ae99)\
  2020-06-26 13:42:04 +0300
  * [MDEV-22535](https://jira.mariadb.org/browse/MDEV-22535) `TABLE::initialize_quick_structures()` takes 0.5% in oltp\_read\_only
* Merge [Revision #1df1a63924](https://github.com/MariaDB/server/commit/1df1a63924) 2020-07-02 06:17:51 +0300 - Merge 10.2 into 10.3
* [Revision #6d3747a294](https://github.com/MariaDB/server/commit/6d3747a294)\
  2020-06-28 16:31:55 +0200
  * make rocksdb cmake checks less verbose on repeat
* [Revision #2ed415765a](https://github.com/MariaDB/server/commit/2ed415765a)\
  2020-06-07 09:58:15 +0300
  * Fix RocksDB detection of ZSTD
* [Revision #c032c2ef66](https://github.com/MariaDB/server/commit/c032c2ef66)\
  2019-04-12 17:00:04 +0900
  * [MDEV-18993](https://jira.mariadb.org/browse/MDEV-18993) The keep-alive connection (set spider\_conn\_recycle\_mode = 1) in spider would cause cash in MariaDB (#1269)
* [Revision #e4cff9a855](https://github.com/MariaDB/server/commit/e4cff9a855)\
  2020-06-27 12:30:17 +0300
  * [MDEV-19298](https://jira.mariadb.org/browse/MDEV-19298) Assertion \`space->id != 0xFFFFFFFEU || space == fil\_system.temp\_space' failed in Check::validate upon crash upgrade from 10.2.22
* [Revision #52c4abbff2](https://github.com/MariaDB/server/commit/52c4abbff2)\
  2020-06-27 12:15:17 +0300
  * [MDEV-20213](https://jira.mariadb.org/browse/MDEV-20213) binlog\_encryption.binlog\_incident failed in buildbot, server crashed in Check::validate
* [Revision #3c238ac51c](https://github.com/MariaDB/server/commit/3c238ac51c)\
  2020-06-27 11:46:30 +0300
  * [MDEV-20213](https://jira.mariadb.org/browse/MDEV-20213) binlog\_encryption.binlog\_incident failed in buildbot, server crashed in Check::validate
* [Revision #697273554f](https://github.com/MariaDB/server/commit/697273554f)\
  2020-06-16 01:29:51 +0300
  * [MDEV-22866](https://jira.mariadb.org/browse/MDEV-22866): Crash in join optimizer with constant outer join nest
* [Revision #e72e6663e1](https://github.com/MariaDB/server/commit/e72e6663e1)\
  2020-06-23 00:00:39 +0530
  * Remove rpl\_parallel2 from disabled.def
* [Revision #b633b6a9d8](https://github.com/MariaDB/server/commit/b633b6a9d8)\
  2020-06-16 10:43:53 +0300
  * [MDEV-22906](https://jira.mariadb.org/browse/MDEV-22906) Disallow system\_versioning\_asof in DML
* [Revision #9f37323f06](https://github.com/MariaDB/server/commit/9f37323f06)\
  2020-06-16 12:30:04 +0530
  * [MDEV-22901](https://jira.mariadb.org/browse/MDEV-22901) Accessing btr\_search\_sys->hash\_tables when buffer pool resize happens
* [Revision #29a5829c37](https://github.com/MariaDB/server/commit/29a5829c37)\
  2020-06-16 12:27:09 +0530
  * [MDEV-22901](https://jira.mariadb.org/browse/MDEV-22901) Accessing `btr_search_sys->hash_tables` when buffer pool resize happens
* Merge [Revision #32b34cb95e](https://github.com/MariaDB/server/commit/32b34cb95e) 2020-06-14 10:30:20 +0300 - Merge 10.2 into 10.3
* Merge [Revision #d83a443250](https://github.com/MariaDB/server/commit/d83a443250) 2020-06-13 15:11:43 +0300 - Merge 10.2 into 10.3
* [Revision #6c30bc2181](https://github.com/MariaDB/server/commit/6c30bc2181)\
  2020-06-13 09:30:04 +0400
  * [MDEV-22268](https://jira.mariadb.org/browse/MDEV-22268) virtual longlong Item\_func\_div::int\_op(): Assertion \`0' failed in Item\_func\_div::int\_op
* [Revision #81a08c5462](https://github.com/MariaDB/server/commit/81a08c5462)\
  2020-06-08 11:25:30 +0530
  * [MDEV-11563](https://jira.mariadb.org/browse/MDEV-11563): GROUP\_CONCAT(DISTINCT ...) may produce a non-distinct list
* Merge [Revision #befb0bed68](https://github.com/MariaDB/server/commit/befb0bed68) 2020-06-08 11:09:49 +0300 - Merge 10.2 into 10.3
* [Revision #a9bee9884a](https://github.com/MariaDB/server/commit/a9bee9884a)\
  2020-06-07 16:30:50 +0300
  * Don't allow ALTER TABLE ... ORDER BY on SEQUENCE objects
* [Revision #e6a6382f15](https://github.com/MariaDB/server/commit/e6a6382f15)\
  2020-06-07 16:23:44 +0300
  * Don't allow illegal create options for SEQUENCE
* [Revision #fad348a9a6](https://github.com/MariaDB/server/commit/fad348a9a6)\
  2020-06-07 16:23:47 +0400
  * [MDEV-22822](https://jira.mariadb.org/browse/MDEV-22822) sql\_mode="oracle" cannot declare without variable errors
* Merge [Revision #4612cb88fa](https://github.com/MariaDB/server/commit/4612cb88fa) 2020-06-06 21:38:57 +0300 - Merge 10.2 into 10.3
* Merge [Revision #b3e395a13e](https://github.com/MariaDB/server/commit/b3e395a13e) 2020-06-06 18:50:25 +0300 - Merge 10.2 into 10.3
* [Revision #e14ffd85d0](https://github.com/MariaDB/server/commit/e14ffd85d0)\
  2020-06-06 17:36:25 +0300
  * [MDEV-22721](https://jira.mariadb.org/browse/MDEV-22721) fixup for 32-bit GCC
* Merge [Revision #b9b279ecc4](https://github.com/MariaDB/server/commit/b9b279ecc4) 2020-06-05 17:59:35 +0200 - Merge remote-tracking branch 'origin/10.2' into 10.3
* [Revision #286e52e948](https://github.com/MariaDB/server/commit/286e52e948)\
  2020-06-05 17:45:27 +0300
  * After-merge fix: GCC -Wmaybe-uninitialized
* Merge [Revision #680463a8d9](https://github.com/MariaDB/server/commit/680463a8d9) 2020-06-05 16:51:26 +0300 - Merge 10.2 into 10.3
* [Revision #05693cf214](https://github.com/MariaDB/server/commit/05693cf214)\
  2020-06-04 12:12:49 +0300
  * [MDEV-22112](https://jira.mariadb.org/browse/MDEV-22112) Assertion \`\`tab\_part\_info->part\_type == RANGE\_PARTITION || tab\_part\_info->part\_type == LIST\_PARTITION'\` failed in prep\_alter\_part\_table
* Merge [Revision #8300f639a1](https://github.com/MariaDB/server/commit/8300f639a1) 2020-06-02 10:25:11 +0300 - Merge 10.2 into 10.3
* [Revision #804761a844](https://github.com/MariaDB/server/commit/804761a844)\
  2020-06-02 08:18:17 +0300
  * [MDEV-22770](https://jira.mariadb.org/browse/MDEV-22770) trx\_undo\_report\_rename() fails to release page latches
* [Revision #fd2b46d879](https://github.com/MariaDB/server/commit/fd2b46d879)\
  2020-06-01 15:38:04 +0200
  * fix warning
* [Revision #2e1d10ecac](https://github.com/MariaDB/server/commit/2e1d10ecac)\
  2020-05-30 10:48:11 +0300
  * Add end-of-test markers to ease merges
* Merge [Revision #e9aaa10c11](https://github.com/MariaDB/server/commit/e9aaa10c11) 2020-05-29 22:21:19 +0300 - Merge 10.2 into 10.3
* [Revision #19da9a51ae](https://github.com/MariaDB/server/commit/19da9a51ae)\
  2020-05-28 22:22:20 +0300
  * [MDEV-16937](https://jira.mariadb.org/browse/MDEV-16937) Strict SQL with system versioned tables causes issues
* [Revision #dd9773b723](https://github.com/MariaDB/server/commit/dd9773b723)\
  2020-05-28 22:22:19 +0300
  * [MDEV-22413](https://jira.mariadb.org/browse/MDEV-22413) Server hangs upon UPDATE on a view reading from versioned partitioned table
* [Revision #3e9b96b6ff](https://github.com/MariaDB/server/commit/3e9b96b6ff)\
  2019-06-13 19:29:02 +0300
  * [MDEV-18794](https://jira.mariadb.org/browse/MDEV-18794) append\_drop\_column() small refactoring
* [Revision #dac1280a65](https://github.com/MariaDB/server/commit/dac1280a65)\
  2020-05-28 20:54:38 +0300
  * [MDEV-18794](https://jira.mariadb.org/browse/MDEV-18794) Assertion \`!m\_innodb' failed in ha\_partition::cmp\_ref upon SELECT from partitioned table
* Merge [Revision #dad7a8ee7d](https://github.com/MariaDB/server/commit/dad7a8ee7d) 2020-05-27 17:10:39 +0300 - Merge 10.2 into 10.3
* [Revision #7476e8c7cd](https://github.com/MariaDB/server/commit/7476e8c7cd)\
  2020-05-25 21:42:26 +0530
  * [MDEV-22637](https://jira.mariadb.org/browse/MDEV-22637) Rollback of insert fails when column reorder happens
* Merge [Revision #ecc7f305dd](https://github.com/MariaDB/server/commit/ecc7f305dd) 2020-05-25 19:41:58 +0300 - Merge 10.2 into 10.3
* [Revision #736ca14323](https://github.com/MariaDB/server/commit/736ca14323)\
  2020-05-22 15:42:11 +0300
  * Don't crash if creating sequence under XA
* Merge [Revision #c7cdd049b5](https://github.com/MariaDB/server/commit/c7cdd049b5) 2020-05-20 21:02:39 +0530 - [MDEV-22451](https://jira.mariadb.org/browse/MDEV-22451): SIGSEGV in `memmove_avx_unaligned_erms/memcpy` from `_my_b_write` on CREATE after RESET MASTER
* Merge [Revision #ed41947b78](https://github.com/MariaDB/server/commit/ed41947b78) 2020-05-20 17:07:09 +0300 - Merge 10.2 into 10.3
* [Revision #21e71766f6](https://github.com/MariaDB/server/commit/21e71766f6)\
  2020-05-20 09:37:05 +0000
  * [MDEV-22631](https://jira.mariadb.org/browse/MDEV-22631) fix
* Merge [Revision #f4f0ef3e37](https://github.com/MariaDB/server/commit/f4f0ef3e37) 2020-05-20 11:41:51 +0300 - Merge 10.2 into 10.3
* [Revision #d4f97e2086](https://github.com/MariaDB/server/commit/d4f97e2086)\
  2020-05-20 11:53:09 +0400
  * [MDEV-22391](https://jira.mariadb.org/browse/MDEV-22391) Assertion \`0' failed in Item\_type\_holder::val\_str on utf16 charset table query
* [Revision #294ac1fbab](https://github.com/MariaDB/server/commit/294ac1fbab)\
  2020-05-19 15:15:52 +0000
  * [MDEV-22636](https://jira.mariadb.org/browse/MDEV-22636) XML output for mtr doesn't work with valgrind option
* Merge [Revision #79ed33c184](https://github.com/MariaDB/server/commit/79ed33c184) 2020-05-19 17:05:05 +0300 - Merge 10.2 into 10.3
* [Revision #2e9f4cdc44](https://github.com/MariaDB/server/commit/2e9f4cdc44)\
  2020-05-19 15:43:35 +0300
  * [MDEV-21936](https://jira.mariadb.org/browse/MDEV-21936) Assertion !btr\_search\_own... in btr\_search\_drop\_page\_hash\_index
* [Revision #06fb78c6ac](https://github.com/MariaDB/server/commit/06fb78c6ac)\
  2020-05-18 11:29:43 +0400
  * [MDEV-21995](https://jira.mariadb.org/browse/MDEV-21995) Server crashes in Item\_field::real\_type\_handler with table value constructor
* [Revision #4869e7f4a8](https://github.com/MariaDB/server/commit/4869e7f4a8)\
  2020-05-18 16:39:38 +0200
  * [MDEV-22615](https://jira.mariadb.org/browse/MDEV-22615) system\_time\_zone may be incorrectly reported as "unknown".
* Merge [Revision #5e12aca57f](https://github.com/MariaDB/server/commit/5e12aca57f) 2020-05-18 14:10:11 +0300 - Merge 10.2 into 10.3
* Merge [Revision #f0be95b5b0](https://github.com/MariaDB/server/commit/f0be95b5b0) 2020-05-18 14:09:34 +0300 - Merge 10.2 into 10.3
* [Revision #e0ddb077d9](https://github.com/MariaDB/server/commit/e0ddb077d9)\
  2020-05-15 18:35:19 +0200
  * [MDEV-22554](https://jira.mariadb.org/browse/MDEV-22554): galera\_sst\_mariadb-backup fails with "Failed to start mysqld.2"
* Merge [Revision #03aaa7f7a1](https://github.com/MariaDB/server/commit/03aaa7f7a1) 2020-05-18 10:47:11 +0300 - Merge 10.2 into 10.3
* [Revision #4f26aea51b](https://github.com/MariaDB/server/commit/4f26aea51b)\
  2020-05-17 11:42:50 +0530
  * [MDEV-21269](https://jira.mariadb.org/browse/MDEV-21269) Parallel merging of fts index rebuild fails
* Merge [Revision #54c169a986](https://github.com/MariaDB/server/commit/54c169a986) 2020-05-16 12:28:03 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* Merge [Revision #38d62189a8](https://github.com/MariaDB/server/commit/38d62189a8) 2020-05-16 06:37:24 +0300 - Merge 10.2 into 10.3
* [Revision #85651269b6](https://github.com/MariaDB/server/commit/85651269b6)\
  2020-05-16 06:24:09 +0300
  * [MDEV-18100](https://jira.mariadb.org/browse/MDEV-18100): Clean up test
* Merge [Revision #3d0bb2b7f1](https://github.com/MariaDB/server/commit/3d0bb2b7f1) 2020-05-15 19:11:57 +0300 - Merge 10.2 into 10.3
* Merge [Revision #6a6bcc53b8](https://github.com/MariaDB/server/commit/6a6bcc53b8) 2020-05-15 17:55:01 +0300 - Merge 10.2 into 10.3
* [Revision #3eadb135fd](https://github.com/MariaDB/server/commit/3eadb135fd)\
  2020-05-15 11:51:31 +0300
  * Fixed access to uninitalized memory found by valgrind
* [Revision #a7c4e85dd6](https://github.com/MariaDB/server/commit/a7c4e85dd6)\
  2020-05-15 11:50:59 +0300
  * Use history.h include file if readline is used
* [Revision #d49233caf6](https://github.com/MariaDB/server/commit/d49233caf6)\
  2020-05-14 18:38:49 +0530
  * [MDEV-18100](https://jira.mariadb.org/browse/MDEV-18100): User defined aggregate functions not working correctly when the schema is changed
* [Revision #1408e26d0b](https://github.com/MariaDB/server/commit/1408e26d0b)\
  2020-05-15 06:15:10 +0400
  * [MDEV-22560](https://jira.mariadb.org/browse/MDEV-22560) Crash on a table value constructor with an SP variable
* Merge [Revision #f7cf60991d](https://github.com/MariaDB/server/commit/f7cf60991d) 2020-05-14 12:33:22 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* Merge [Revision #ef65c39ab3](https://github.com/MariaDB/server/commit/ef65c39ab3) 2020-05-14 10:01:54 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* Merge [Revision #15fa70b840](https://github.com/MariaDB/server/commit/15fa70b840) 2020-05-13 11:45:05 +0300 - Merge 10.2 into 10.3
* Merge [Revision #19d4e023c6](https://github.com/MariaDB/server/commit/19d4e023c6) 2020-05-11 20:27:44 +0200 - Merge branch '10.3-release' into 10.3
* [Revision #9f5ab66b72](https://github.com/MariaDB/server/commit/9f5ab66b72)\
  2020-05-11 12:57:01 -0400
  * bump the VERSION
* [Revision #d01d94d77b](https://github.com/MariaDB/server/commit/d01d94d77b)\
  2020-05-06 23:44:34 +0300
  * [MDEV-17568](https://jira.mariadb.org/browse/MDEV-17568): LATERAL DERIVED is not clearly visible in EXPLAIN FORMAT=JSON

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
