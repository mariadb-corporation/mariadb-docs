# MariaDB 10.4.5 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.5)[Release Notes](../../old-releases/10.4/10.4.5.md)[Changelog](mariadb-1045-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 21 May 2019

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.5.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.15](../changelogs-mariadb-10-3-series/mariadb-10315-changelog.md)
* [Revision #dafe41edea](https://github.com/MariaDB/server/commit/dafe41edea)\
  2019-05-20 09:38:08 +0200
  * Removing of dead code.
* [Revision #1d00f81921](https://github.com/MariaDB/server/commit/1d00f81921)\
  2019-05-19 23:31:56 +0200
  * fix of Galera test
* Merge [Revision #c07325f932](https://github.com/MariaDB/server/commit/c07325f932) 2019-05-19 20:55:37 +0200 - Merge branch '10.3' into 10.4
* [Revision #2ae83affef](https://github.com/MariaDB/server/commit/2ae83affef)\
  2019-05-18 11:38:43 +0200
  * update a test result, followup fae6539ef72
* Merge [Revision #c1fd027115](https://github.com/MariaDB/server/commit/c1fd027115) 2019-05-17 17:23:01 +0200 - Merge branch '10.2' into 10.3
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
* [Revision #e506bef430](https://github.com/MariaDB/server/commit/e506bef430)\
  2019-05-13 14:19:10 +0200
  * [MDEV-15458](https://jira.mariadb.org/browse/MDEV-15458) Segfault in heap\_scan() upon UPDATE after ADD SYSTEM VERSIONING
* [Revision #43623f04a9](https://github.com/MariaDB/server/commit/43623f04a9)\
  2019-05-13 14:22:49 +0200
  * [MDEV-15458](https://jira.mariadb.org/browse/MDEV-15458) Segfault in heap\_scan() upon UPDATE after ADD SYSTEM VERSIONING
* [Revision #73de06c48f](https://github.com/MariaDB/server/commit/73de06c48f)\
  2019-05-10 16:38:54 +0300
  * make method const
* [Revision #3d649c6e37](https://github.com/MariaDB/server/commit/3d649c6e37)\
  2019-05-10 16:21:22 +0300
  * [MDEV-15408](https://jira.mariadb.org/browse/MDEV-15408) Confusing error message upon ER\_VERS\_FIELD\_WRONG\_TYPE while omitting UNSIGNED in BIGINT
* Merge [Revision #3d56adbfac](https://github.com/MariaDB/server/commit/3d56adbfac) 2019-05-16 14:24:29 +0300 - Merge 10.2 into 10.3
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
* [Revision #b7d22a843e](https://github.com/MariaDB/server/commit/b7d22a843e)\
  2019-05-16 10:16:09 +0400
  * [MDEV-16872](https://jira.mariadb.org/browse/MDEV-16872) Add CAST(expr AS FLOAT)
* Merge [Revision #e0e805759f](https://github.com/MariaDB/server/commit/e0e805759f) 2019-05-15 17:06:05 +0300 - Merge 10.2 into 10.3
* [Revision #56976e60f5](https://github.com/MariaDB/server/commit/56976e60f5)\
  2019-05-14 17:59:47 +0300
  * [MDEV-13080](https://jira.mariadb.org/browse/MDEV-13080) \[ERROR] InnoDB: Missing MLOG\_CHECKPOINT between the checkpoint x and the end y
* [Revision #fde29f3a22](https://github.com/MariaDB/server/commit/fde29f3a22)\
  2019-05-15 16:33:13 +0400
  * A cleanup for [MDEV-19468](https://jira.mariadb.org/browse/MDEV-19468): Adding a missing #include
* [Revision #6434e495c1](https://github.com/MariaDB/server/commit/6434e495c1)\
  2019-05-15 15:22:06 +0400
  * A cleanup for [MDEV-19468](https://jira.mariadb.org/browse/MDEV-19468) Hybrid type expressions return wrong format for FLOAT
* [Revision #462d689397](https://github.com/MariaDB/server/commit/462d689397)\
  2019-05-14 21:47:38 +0400
  * [MDEV-19468](https://jira.mariadb.org/browse/MDEV-19468) Hybrid type expressions return wrong format for FLOAT
* [Revision #4937339705](https://github.com/MariaDB/server/commit/4937339705)\
  2019-05-14 19:40:21 +0300
  * [MDEV-19445](https://jira.mariadb.org/browse/MDEV-19445): After-merge fix
* Merge [Revision #73e038520f](https://github.com/MariaDB/server/commit/73e038520f) 2019-05-14 18:10:06 +0300 - Merge 10.2 into 10.3
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
* Merge [Revision #874f8f30f2](https://github.com/MariaDB/server/commit/874f8f30f2) 2019-05-14 17:25:25 +0300 - Merge 10.2 into 10.3
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
* Merge [Revision #be85d3e61b](https://github.com/MariaDB/server/commit/be85d3e61b) 2019-05-14 17:18:46 +0300 - Merge 10.2 into 10.3
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
* [Revision #c0bc9480e7](https://github.com/MariaDB/server/commit/c0bc9480e7)\
  2019-05-14 10:07:57 -0400
  * bump the VERSION
* Merge [Revision #518cb2bb97](https://github.com/MariaDB/server/commit/518cb2bb97) 2019-05-14 14:23:35 +0200 - Merge branch 'bb-10.3-release' into 10.3
* [Revision #06b50da770](https://github.com/MariaDB/server/commit/06b50da770)\
  2019-05-13 14:54:35 +0000
  * Fix typo THRASH\_FREED\_MEMORY->TRASH\_FREED\_MEMORY
* [Revision #374dae3ecc](https://github.com/MariaDB/server/commit/374dae3ecc)\
  2019-05-13 14:31:15 +0000
  * [MDEV-19452](https://jira.mariadb.org/browse/MDEV-19452) - fix incorrect push\_warning\_printf
* [Revision #0c188d5efc](https://github.com/MariaDB/server/commit/0c188d5efc)\
  2019-05-13 10:08:42 +0000
  * Make TRASH\_FREED\_MEMORY a cmake option, similar to SAFEMALLOC
* [Revision #7f8187bc43](https://github.com/MariaDB/server/commit/7f8187bc43)\
  2019-05-19 20:48:39 +0200
  * fix tcp disconnect and perl
* [Revision #04fa127bc9](https://github.com/MariaDB/server/commit/04fa127bc9)\
  2019-05-19 20:35:38 +0200
  * More fixed for perl test
* [Revision #8feb78ef53](https://github.com/MariaDB/server/commit/8feb78ef53)\
  2019-05-11 16:56:41 +0200
  * cleanup: replace a magic constant with a define
* [Revision #d199591cf2](https://github.com/MariaDB/server/commit/d199591cf2)\
  2019-05-11 16:25:01 +0200
  * generalize the error message
* [Revision #ececc50252](https://github.com/MariaDB/server/commit/ececc50252)\
  2019-05-11 12:18:34 +0200
  * [MDEV-15966](https://jira.mariadb.org/browse/MDEV-15966) Behavior for TRUNCATE versioned table is not documented and not covered by tests
* [Revision #2400e06946](https://github.com/MariaDB/server/commit/2400e06946)\
  2019-05-09 19:12:34 +0200
  * remove -fno-rtti
* [Revision #2c08436959](https://github.com/MariaDB/server/commit/2c08436959)\
  2019-02-24 21:00:36 +0200
  * Fix default\_password\_lifetime message typo
* [Revision #d9f392848a](https://github.com/MariaDB/server/commit/d9f392848a)\
  2019-05-18 07:26:56 +0400
  * A cleanup for [MDEV-19284](https://jira.mariadb.org/browse/MDEV-19284), [MDEV-19285](https://jira.mariadb.org/browse/MDEV-19285)
* [Revision #b86175747d](https://github.com/MariaDB/server/commit/b86175747d)\
  2019-05-17 19:30:29 +0300
  * [MDEV-19513](https://jira.mariadb.org/browse/MDEV-19513): Fix the non-debug build
* [Revision #198ed24cac](https://github.com/MariaDB/server/commit/198ed24cac)\
  2019-05-17 15:17:37 +0300
  * [MDEV-19513](https://jira.mariadb.org/browse/MDEV-19513): Rename dict\_operation\_lock to dict\_sys.latch
* [Revision #b390447e71](https://github.com/MariaDB/server/commit/b390447e71)\
  2019-05-17 15:25:12 +0300
  * [MDEV-19513](https://jira.mariadb.org/browse/MDEV-19513): Remove rw\_lock\_t::magic\_n
* [Revision #5fd7502e77](https://github.com/MariaDB/server/commit/5fd7502e77)\
  2019-05-17 14:32:53 +0300
  * [MDEV-19513](https://jira.mariadb.org/browse/MDEV-19513): Allocate dict\_sys statically
* [Revision #d682dc2e70](https://github.com/MariaDB/server/commit/d682dc2e70)\
  2019-05-17 08:08:11 +0400
  * [MDEV-8919](https://jira.mariadb.org/browse/MDEV-8919) Wrong result for CAST(9999999999999999999.0)
* [Revision #cacdcfd0e4](https://github.com/MariaDB/server/commit/cacdcfd0e4)\
  2019-05-16 13:12:21 +0530
  * [MDEV-18970](https://jira.mariadb.org/browse/MDEV-18970): uninited var can be read in gtid\_delete\_pending()
* [Revision #c59d6395a6](https://github.com/MariaDB/server/commit/c59d6395a6)\
  2019-04-19 15:18:38 +0400
  * A joint patch for [MDEV-19284](https://jira.mariadb.org/browse/MDEV-19284) and [MDEV-19285](https://jira.mariadb.org/browse/MDEV-19285) (INSTANT ALTER)
* [Revision #9aa80fcf46](https://github.com/MariaDB/server/commit/9aa80fcf46)\
  2019-05-16 14:33:24 +0300
  * [MDEV-19485](https://jira.mariadb.org/browse/MDEV-19485): Crash on purge after ADD SPATIAL INDEX
* [Revision #d448cfc92a](https://github.com/MariaDB/server/commit/d448cfc92a)\
  2019-05-10 12:47:44 +0300
  * [MDEV-19134](https://jira.mariadb.org/browse/MDEV-19134): EXISTS() slower if ORDER BY is defined
* [Revision #b1f828a82a](https://github.com/MariaDB/server/commit/b1f828a82a)\
  2019-05-04 21:33:39 +0300
  * [MDEV-19134](https://jira.mariadb.org/browse/MDEV-19134): EXISTS() slower if ORDER BY is defined
* [Revision #366bf10475](https://github.com/MariaDB/server/commit/366bf10475)\
  2019-02-23 23:48:55 +0000
  * Fix echo message
* [Revision #ea77162452](https://github.com/MariaDB/server/commit/ea77162452)\
  2019-05-14 11:34:22 +0300
  * [MDEV-19423](https://jira.mariadb.org/browse/MDEV-19423): Galera test failure on galera.[MDEV-16509](https://jira.mariadb.org/browse/MDEV-16509)
* [Revision #5cf4022340](https://github.com/MariaDB/server/commit/5cf4022340)\
  2019-05-15 09:13:31 +0200
  * fix the test for windows
* [Revision #51dcdf2adb](https://github.com/MariaDB/server/commit/51dcdf2adb)\
  2019-05-14 15:54:48 +0530
  * Added a 32 bit rdiff for myisam\_mrr instead of a 64 bit rdiff
* [Revision #30ddf96113](https://github.com/MariaDB/server/commit/30ddf96113)\
  2019-05-14 23:47:12 +0400
  * Fixed ya main.flush\_read\_lock sporadic failure
* [Revision #29a0f5acf3](https://github.com/MariaDB/server/commit/29a0f5acf3)\
  2019-05-13 21:34:16 +0200
  * [MDEV-19277](https://jira.mariadb.org/browse/MDEV-19277): Add status variable that gets incremented if connection is aborted prior to authentication [MDEV-19282](https://jira.mariadb.org/browse/MDEV-19282): Log more specific warning with log\_warnings=2 if connection is aborted prior to authentication
* [Revision #c3ea52c92a](https://github.com/MariaDB/server/commit/c3ea52c92a)\
  2019-05-14 12:35:42 +0300
  * [MDEV-17958](https://jira.mariadb.org/browse/MDEV-17958): Remove IS\_BIG\_ENDIAN
* [Revision #3d8cacee6e](https://github.com/MariaDB/server/commit/3d8cacee6e)\
  2019-05-13 12:46:50 +0300
  * [MDEV-19404](https://jira.mariadb.org/browse/MDEV-19404): Assertion failure on !is\_thread\_specific || (mysqld\_server\_initialized && thd)
* [Revision #41779561ec](https://github.com/MariaDB/server/commit/41779561ec)\
  2019-05-13 22:41:28 +0530
  * Fixed myisam\_mrr for 32 bit systems
* [Revision #7a6c36b547](https://github.com/MariaDB/server/commit/7a6c36b547)\
  2019-05-13 17:56:31 +0400
  * Fixed main.flush\_read\_lock sporadic failure
* [Revision #341c3379ae](https://github.com/MariaDB/server/commit/341c3379ae)\
  2019-05-13 12:58:47 +0300
  * Removed obsolete file maria\_rename.sh
* [Revision #60518a6b85](https://github.com/MariaDB/server/commit/60518a6b85)\
  2019-05-13 12:57:26 +0300
  * Make maria-autozerofill a bit more rebust
* [Revision #6a365e0bf2](https://github.com/MariaDB/server/commit/6a365e0bf2)\
  2019-05-11 20:44:18 +0530
  * [MDEV-13628](https://jira.mariadb.org/browse/MDEV-13628): ORed condition in pushed index condition is not removed from the WHERE
* [Revision #9965966a49](https://github.com/MariaDB/server/commit/9965966a49)\
  2019-05-10 13:42:34 +0300
  * Fixed that storage/funcs tests works with Aria
* [Revision #6f3b09993f](https://github.com/MariaDB/server/commit/6f3b09993f)\
  2019-05-03 02:21:55 +0800
  * add Hygon Dhyana support in check-cpu
* [Revision #d2fa5f8cfc](https://github.com/MariaDB/server/commit/d2fa5f8cfc)\
  2018-12-16 17:57:47 +1100
  * [MDEV-8553](https://jira.mariadb.org/browse/MDEV-8553): Impossible where for a!=a, a\<a, a>a
* [Revision #ad36d38024](https://github.com/MariaDB/server/commit/ad36d38024)\
  2019-05-09 17:38:22 +0200
  * [MDEV-19235](https://jira.mariadb.org/browse/MDEV-19235) MariaDB Server compiled for 128 Indexes crashes at startup
* [Revision #44b8b002f5](https://github.com/MariaDB/server/commit/44b8b002f5)\
  2019-05-09 11:24:06 +0300
  * Disable 5733\_tokudb as the result is not stable
* [Revision #a3a48d4561](https://github.com/MariaDB/server/commit/a3a48d4561)\
  2019-05-07 17:05:58 +0000
  * [MDEV-19403](https://jira.mariadb.org/browse/MDEV-19403) Remove mysql\_secure\_installation.pl
* [Revision #fd386e39cd](https://github.com/MariaDB/server/commit/fd386e39cd)\
  2019-05-06 11:14:39 -0700
  * [MDEV-18689](https://jira.mariadb.org/browse/MDEV-18689) Simple query with extra brackets stopped working
* [Revision #b8259e4b59](https://github.com/MariaDB/server/commit/b8259e4b59)\
  2019-05-05 12:58:25 +0300
  * [MDEV-19384](https://jira.mariadb.org/browse/MDEV-19384) Deadlock in FTWRL
* [Revision #60bd353bdf](https://github.com/MariaDB/server/commit/60bd353bdf)\
  2019-05-03 18:59:07 +0000
  * Fixes for atomic writes on Windows.
* [Revision #59a266a9f9](https://github.com/MariaDB/server/commit/59a266a9f9)\
  2019-05-03 12:59:46 +0000
  * [MDEV-17380](https://jira.mariadb.org/browse/MDEV-17380): fix incorrect #ifdef
* [Revision #c477623f04](https://github.com/MariaDB/server/commit/c477623f04)\
  2019-05-03 12:58:11 +0000
  * [MDEV-19388](https://jira.mariadb.org/browse/MDEV-19388) Improve SSD detection on Windows
* [Revision #f81007f8d8](https://github.com/MariaDB/server/commit/f81007f8d8)\
  2019-05-05 22:59:53 +0300
  * Fix the Windows build
* Merge [Revision #d3dcec5d65](https://github.com/MariaDB/server/commit/d3dcec5d65) 2019-05-05 15:03:48 +0300 - Merge 10.3 into 10.4
* Merge [Revision #b132b8895e](https://github.com/MariaDB/server/commit/b132b8895e) 2019-05-05 10:23:14 +0300 - Merge 10.3 into 10.4
* [Revision #27980b0f83](https://github.com/MariaDB/server/commit/27980b0f83)\
  2019-05-05 12:24:54 +0530
  * [MDEV-19365](https://jira.mariadb.org/browse/MDEV-19365) Assertion failure in LONG Unique after 10.3 merge
* [Revision #d18ef804bb](https://github.com/MariaDB/server/commit/d18ef804bb)\
  2019-05-03 10:13:32 +0300
  * [MDEV-18552](https://jira.mariadb.org/browse/MDEV-18552) [MDEV-18699](https://jira.mariadb.org/browse/MDEV-18699) allowing SR only in galera 4 cluster (#1293)
* [Revision #ca098107a2](https://github.com/MariaDB/server/commit/ca098107a2)\
  2019-05-03 09:46:00 +0530
  * [MDEV-18117](https://jira.mariadb.org/browse/MDEV-18117): Crash with Explain extended when using limit rows examined
* [Revision #186635392d](https://github.com/MariaDB/server/commit/186635392d)\
  2019-05-02 20:06:03 +0300
  * Fixed deadlock in main.flush\_read\_lock
* [Revision #0cc7c6085e](https://github.com/MariaDB/server/commit/0cc7c6085e)\
  2019-05-02 16:11:32 +0300
  * Enable mysqlcheck and flush\_read\_lock tests
* [Revision #2b7e080fae](https://github.com/MariaDB/server/commit/2b7e080fae)\
  2019-05-01 18:20:06 -0700
  * [MDEV-19363](https://jira.mariadb.org/browse/MDEV-19363) Assertion \`select\_lex' failed in LEX::pop\_select
* [Revision #ea679c88c3](https://github.com/MariaDB/server/commit/ea679c88c3)\
  2019-05-01 08:47:04 +0400
  * [MDEV-19377](https://jira.mariadb.org/browse/MDEV-19377) Replace Virtual\_column\_info::field\_type to Type\_handler
* [Revision #0cbc930616](https://github.com/MariaDB/server/commit/0cbc930616)\
  2019-04-30 21:39:08 +0900
  * [MDEV-18992](https://jira.mariadb.org/browse/MDEV-18992) Crash when using 'insert into on duplicate update'if session charset different from table charset (#1290)
* [Revision #218ab0deed](https://github.com/MariaDB/server/commit/218ab0deed)\
  2019-04-29 22:24:44 +0100
  * re-record performance schema test
* [Revision #892c2ec097](https://github.com/MariaDB/server/commit/892c2ec097)\
  2019-04-29 22:21:55 +0100
  * Revert "Adjust perfschema.privilege\_table\_io result"
* [Revision #77109285f9](https://github.com/MariaDB/server/commit/77109285f9)\
  2019-04-29 13:52:02 +0100
  * [MDEV-19354](https://jira.mariadb.org/browse/MDEV-19354) : Change default service name in MSI UI to MariaDB.
* [Revision #703a5ef130](https://github.com/MariaDB/server/commit/703a5ef130)\
  2019-04-27 21:31:04 -0700
  * [MDEV-19351](https://jira.mariadb.org/browse/MDEV-19351) statistics\_for\_command\_is\_needed: Conditional jump or move depends on uninitialised value
* [Revision #4c995eb168](https://github.com/MariaDB/server/commit/4c995eb168)\
  2019-04-29 09:32:43 +0300
  * Correct the result for a few tests
* [Revision #2f1f02817e](https://github.com/MariaDB/server/commit/2f1f02817e)\
  2019-04-29 09:27:32 +0300
  * After-merge fix for rocksdb
* [Revision #589dc00d94](https://github.com/MariaDB/server/commit/589dc00d94)\
  2019-04-29 09:25:42 +0400
  * Test for [MDEV-11874](https://jira.mariadb.org/browse/MDEV-11874) "Data too long for column" instead of "Invalid default value for" upon ALTER in strict mode
* [Revision #81f6a3b0e5](https://github.com/MariaDB/server/commit/81f6a3b0e5)\
  2019-04-27 20:01:59 +0300
  * Adjust perfschema.privilege\_table\_io result
* [Revision #5dee4a99d9](https://github.com/MariaDB/server/commit/5dee4a99d9)\
  2019-04-26 17:55:12 -0700
  * [MDEV-19324](https://jira.mariadb.org/browse/MDEV-19324) Wrong results from query, using brackets with ORDER BY ..LIMIT
* [Revision #d1a43973ef](https://github.com/MariaDB/server/commit/d1a43973ef)\
  2019-04-26 12:50:26 +0530
  * Adjusted result for tokudb\_bugs.db756\_card\_part\_hash\_2\_pick
* [Revision #87472974cd](https://github.com/MariaDB/server/commit/87472974cd)\
  2019-04-25 22:05:54 +0530
  * Results updated for tokudb tests
* [Revision #6599cd985e](https://github.com/MariaDB/server/commit/6599cd985e)\
  2019-04-26 00:51:28 +0900
  * [MDEV-18988](https://jira.mariadb.org/browse/MDEV-18988) Wrong result when query with group by x order by y limit n (#1286)
* [Revision #82d0698962](https://github.com/MariaDB/server/commit/82d0698962)\
  2019-04-25 23:28:04 +0900
  * [MDEV-18995](https://jira.mariadb.org/browse/MDEV-18995) Some bugs in direct join (#1285)
* Merge [Revision #e6bdf77e4b](https://github.com/MariaDB/server/commit/e6bdf77e4b) 2019-04-25 16:05:20 +0300 - Merge 10.3 into 10.4
* [Revision #1599825ffc](https://github.com/MariaDB/server/commit/1599825ffc)\
  2019-04-22 00:04:14 +0400
  * trans\_xa\_detach() framework
* [Revision #210855ce5d](https://github.com/MariaDB/server/commit/210855ce5d)\
  2019-04-18 15:36:06 +0400
  * Move XID\_STATE::xid to XID\_cache\_element
* [Revision #b7fd7ce286](https://github.com/MariaDB/server/commit/b7fd7ce286)\
  2019-04-19 19:17:27 +0400
  * Moved normal transaction xid to implicit\_xid
* [Revision #228514e52f](https://github.com/MariaDB/server/commit/228514e52f)\
  2019-04-18 16:30:10 +0400
  * Move XID\_STATE::xa\_state to XID\_cache\_element
* [Revision #a168cfb396](https://github.com/MariaDB/server/commit/a168cfb396)\
  2019-04-21 13:27:27 +0400
  * Move XID\_state::xa\_state handing inside xa.cc
* [Revision #f189f34ed4](https://github.com/MariaDB/server/commit/f189f34ed4)\
  2019-04-19 00:48:15 +0400
  * Move XID\_STATE::rm\_error to XID\_cache\_element
* [Revision #07140f171d](https://github.com/MariaDB/server/commit/07140f171d)\
  2019-04-18 14:43:40 +0400
  * Just move, no code changes otherwise.
* [Revision #ca7fbcea6c](https://github.com/MariaDB/server/commit/ca7fbcea6c)\
  2019-04-24 15:47:49 +0400
  * [MDEV-19317](https://jira.mariadb.org/browse/MDEV-19317) TEXT column accepts too long literals as a default value
* [Revision #baadbe9601](https://github.com/MariaDB/server/commit/baadbe9601)\
  2019-04-23 13:45:28 +0400
  * [MDEV-9234](https://jira.mariadb.org/browse/MDEV-9234) Add Type\_handler::union\_element\_finalize()
* [Revision #a765b19e5c](https://github.com/MariaDB/server/commit/a765b19e5c)\
  2019-04-22 16:19:55 +0300
  * [MDEV-19245](https://jira.mariadb.org/browse/MDEV-19245): Impossible WHERE should be noticed earlier after HAVING pushdown
* [Revision #a65d3b2c16](https://github.com/MariaDB/server/commit/a65d3b2c16)\
  2019-04-19 16:17:51 -0700
  * [MDEV-19255](https://jira.mariadb.org/browse/MDEV-19255) Server crash in st\_join\_table::save\_explain\_data or assertion \`sel->quick' failure in JOIN::make\_range\_rowid\_filters upon query with rowid\_filter=ON
* [Revision #38f390f549](https://github.com/MariaDB/server/commit/38f390f549)\
  2019-04-19 13:22:01 +0300
  * [MDEV-19224](https://jira.mariadb.org/browse/MDEV-19224) Assertion \`marked\_for\_read()' failed
* [Revision #c07e346ca6](https://github.com/MariaDB/server/commit/c07e346ca6)\
  2019-04-19 13:20:15 +0300
  * [MDEV-19252](https://jira.mariadb.org/browse/MDEV-19252) Problem with DBUG\_ASSERT\_AS\_PRINTF and marked\_for\_write()
* [Revision #a024649081](https://github.com/MariaDB/server/commit/a024649081)\
  2019-04-19 13:15:46 +0300
  * Fixed compiler warnings form gcc 7.3.1
* [Revision #4233b28489](https://github.com/MariaDB/server/commit/4233b28489)\
  2019-04-19 07:00:17 +0400
  * [MDEV-19283](https://jira.mariadb.org/browse/MDEV-19283) Move the code from Field\_str::is\_equal() to Field\_string::is\_equal()
* [Revision #878ca5ca4f](https://github.com/MariaDB/server/commit/878ca5ca4f)\
  2019-04-18 18:56:14 +0300
  * [MDEV-19266](https://jira.mariadb.org/browse/MDEV-19266): Crash in EITS code when enabling 128 indexes
* [Revision #7b216ceb90](https://github.com/MariaDB/server/commit/7b216ceb90)\
  2019-04-18 14:28:39 +0300
  * Avoid DROP DATABASE test
* [Revision #6812fb7971](https://github.com/MariaDB/server/commit/6812fb7971)\
  2019-04-18 05:50:59 +0100
  * [MDEV-19274](https://jira.mariadb.org/browse/MDEV-19274) mariadb does not build on OSes that do not have HAVE\_POOL\_OF\_THREADS
* [Revision #59ed5f3aa4](https://github.com/MariaDB/server/commit/59ed5f3aa4)\
  2019-04-17 21:37:29 -0700
  * [MDEV-19164](https://jira.mariadb.org/browse/MDEV-19164) Assertion \`fixed' failed in Item\_func\_inet\_aton::val\_int
* Merge [Revision #e7029e864f](https://github.com/MariaDB/server/commit/e7029e864f) 2019-04-17 15:45:53 +0300 - Merge 10.3 into 10.4
* [Revision #ee4a2fef18](https://github.com/MariaDB/server/commit/ee4a2fef18)\
  2019-04-17 08:16:41 +0400
  * Adding missing ';' at the end of a rule
* [Revision #f202f3dfe6](https://github.com/MariaDB/server/commit/f202f3dfe6)\
  2019-04-16 23:02:54 +0200
  * [MDEV-19263](https://jira.mariadb.org/browse/MDEV-19263): Server crashes in mysql\_handle\_single\_derived upon 2nd execution of PS
* [Revision #653a56fd95](https://github.com/MariaDB/server/commit/653a56fd95)\
  2019-04-17 01:55:03 +0900
  * [MDEV-17508](https://jira.mariadb.org/browse/MDEV-17508) Fix bug for spider when using "not like" (#1282)
* [Revision #645f77a6bc](https://github.com/MariaDB/server/commit/645f77a6bc)\
  2019-04-08 11:21:53 -0700
  * [MDEV-19195](https://jira.mariadb.org/browse/MDEV-19195) Active Record unit test fails with [MariaDB 10.4.3](../../old-releases/10.4/10.4.3.md)
* [Revision #d9d79e4d01](https://github.com/MariaDB/server/commit/d9d79e4d01)\
  2019-04-16 16:35:21 +0300
  * [MDEV-17494](https://jira.mariadb.org/browse/MDEV-17494) Refuse ALGORITHM=INSTANT when the row size is too large
* [Revision #f66e006b08](https://github.com/MariaDB/server/commit/f66e006b08)\
  2019-04-16 22:10:05 +0800
  * fix bug for spider where using "not like" (#890)
* [Revision #8701e5b095](https://github.com/MariaDB/server/commit/8701e5b095)\
  2019-04-16 11:58:56 +0200
  * Cleanup of sql\_derived.cc file
* [Revision #eb056f8726](https://github.com/MariaDB/server/commit/eb056f8726)\
  2019-04-02 15:04:45 +0200
  * [MDEV-17362](https://jira.mariadb.org/browse/MDEV-17362): SIGSEGV in JOIN::optimize\_inner or Assertion \`fixed == 0' failed in Item\_equal::fix\_fields, server crashes after 2nd execution of PS
* [Revision #6c306a729d](https://github.com/MariaDB/server/commit/6c306a729d)\
  2019-04-02 14:46:36 +0200
  * Cleanup of derived table interface
* [Revision #3bc863b208](https://github.com/MariaDB/server/commit/3bc863b208)\
  2019-04-16 08:20:57 +0400
  * [MDEV-19256](https://jira.mariadb.org/browse/MDEV-19256) sql\_acl.cc does not compile with WITH\_VALGRIND with gcc 8.0
* [Revision #e4c5551964](https://github.com/MariaDB/server/commit/e4c5551964)\
  2019-04-15 13:07:53 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Temporarily restore a call to work around a bug
* [Revision #c2a2e72164](https://github.com/MariaDB/server/commit/c2a2e72164)\
  2019-04-03 15:40:45 +0400
  * [MDEV-19142](https://jira.mariadb.org/browse/MDEV-19142) sql\_mode=MSSQL: Bracket identifiers
* [Revision #3c352b59eb](https://github.com/MariaDB/server/commit/3c352b59eb)\
  2019-04-13 20:28:25 +0900
  * fix vargrind errors of Spider (#1273)
* [Revision #3e89e0f2ba](https://github.com/MariaDB/server/commit/3e89e0f2ba)\
  2019-04-13 05:54:30 +0900
  * [MDEV-16543](https://jira.mariadb.org/browse/MDEV-16543) Replicating to spider is fragile without retries (#1272)
* [Revision #1e8279a958](https://github.com/MariaDB/server/commit/1e8279a958)\
  2019-04-12 23:37:57 +0900
  * [MDEV-16530](https://jira.mariadb.org/browse/MDEV-16530) Spider datanodes needs adjusted wait\_timeout for long running queries on spider head node (#1258)
* [Revision #857310c218](https://github.com/MariaDB/server/commit/857310c218)\
  2019-04-12 22:58:37 +0900
  * [MDEV-16543](https://jira.mariadb.org/browse/MDEV-16543) Replicating to spider is fragile without retries (#1259)
* Merge [Revision #7896503686](https://github.com/MariaDB/server/commit/7896503686) 2019-04-12 12:45:06 +0300 - Merge 10.3 into 10.4
* [Revision #1d48c4a025](https://github.com/MariaDB/server/commit/1d48c4a025)\
  2019-04-12 17:00:04 +0900
  * [MDEV-18993](https://jira.mariadb.org/browse/MDEV-18993) The keep-alive connection (set spider\_conn\_recycle\_mode = 1) in spider would cause cash in MariaDB (#1269)
* [Revision #71848585f8](https://github.com/MariaDB/server/commit/71848585f8)\
  2019-04-10 11:19:38 +0300
  * Fix InnoDB dynamic plugin compile errors on wsrep patch.
* [Revision #304ae942f7](https://github.com/MariaDB/server/commit/304ae942f7)\
  2019-04-08 17:43:06 +0300
  * [MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528) preparation: Write MLOG\_INIT\_FREE\_PAGE
* Merge [Revision #edd1a53a55](https://github.com/MariaDB/server/commit/edd1a53a55) 2019-04-08 21:58:18 +0300 - Merge 10.3 into 10.4
* [Revision #1e7ad5bb1c](https://github.com/MariaDB/server/commit/1e7ad5bb1c)\
  2019-04-08 09:00:25 +0300
  * [MDEV-15584](https://jira.mariadb.org/browse/MDEV-15584): Do not invoke open(dir=NULL)
* Merge [Revision #d8303c3ee7](https://github.com/MariaDB/server/commit/d8303c3ee7) 2019-04-08 08:22:34 +0300 - Merge 10.3 into 10.4
* [Revision #a2afba8b01](https://github.com/MariaDB/server/commit/a2afba8b01)\
  2019-04-07 13:47:22 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
