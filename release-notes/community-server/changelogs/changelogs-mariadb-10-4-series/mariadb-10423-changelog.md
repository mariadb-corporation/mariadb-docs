# MariaDB 10.4.23 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.23](https://mariadb.org/download/?tab=mariadb\&release=10.4.23\&product=mariadb|)[Release Notes](../../old-releases/10.4/10.4.23.md)[Changelog](mariadb-10423-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 9 Feb 2022

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.23.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.33](../changelogs-mariadb-10-3-series/mariadb-10333-changelog.md)
* [Revision #c04a203a10](https://github.com/MariaDB/server/commit/c04a203a10)\
  2022-01-31 08:37:33 +0100
  * Rocksdb result fix after merge
* [Revision #2d85188627](https://github.com/MariaDB/server/commit/2d85188627)\
  2022-01-30 18:14:27 +0100
  * Fix galera result after merge
* [Revision #ca41fdba22](https://github.com/MariaDB/server/commit/ca41fdba22)\
  2022-01-30 17:52:15 +0100
  * fix [MDEV-27217](https://jira.mariadb.org/browse/MDEV-27217) (4d5ae2b3258d0d4eb3addd61fdabf49d9a6314e7)
* Merge [Revision #a576a1cea5](https://github.com/MariaDB/server/commit/a576a1cea5) 2022-01-30 09:46:52 +0100 - Merge branch '10.3' into 10.4
* [Revision #12cad0c346](https://github.com/MariaDB/server/commit/12cad0c346)\
  2022-01-25 16:39:13 +0100
  * [MDEV-27615](https://jira.mariadb.org/browse/MDEV-27615) Assertion \`server\_id.is\_undefined() == false' failed
* [Revision #3d69213e74](https://github.com/MariaDB/server/commit/3d69213e74)\
  2021-11-02 16:02:56 +0400
  * [MDEV-26953](https://jira.mariadb.org/browse/MDEV-26953) Assertion \`!str || str != Ptr || !is\_alloced()' failed in String::copy upon SELECT with sjis
* [Revision #4775677457](https://github.com/MariaDB/server/commit/4775677457)\
  2022-01-27 11:09:11 +1100
  * [MDEV-23326](https://jira.mariadb.org/browse/MDEV-23326): fix - not embedded main.mysql\_tzinfo\_to\_sql\_symlink
* [Revision #c9356223c9](https://github.com/MariaDB/server/commit/c9356223c9)\
  2022-01-18 13:57:27 +0200
  * [MDEV-19555](https://jira.mariadb.org/browse/MDEV-19555) assert Diagnostics\_area::sql\_errno() in ha\_rollback\_trans
* [Revision #e9aac09153](https://github.com/MariaDB/server/commit/e9aac09153)\
  2022-01-26 12:42:17 +0200
  * [MDEV-25440](https://jira.mariadb.org/browse/MDEV-25440): Indexed CHAR columns are broken with NO\_PAD collations
* [Revision #37144afbb0](https://github.com/MariaDB/server/commit/37144afbb0)\
  2021-10-01 09:12:01 +0300
  * Cleanup: Simplify cmp\_geometry\_field() and cmp\_whole\_field()
* [Revision #be1d965384](https://github.com/MariaDB/server/commit/be1d965384)\
  2022-01-24 20:00:35 +0100
  * [MDEV-27373](https://jira.mariadb.org/browse/MDEV-27373) wolfSSL 5.1.1
* [Revision #8db47403ff](https://github.com/MariaDB/server/commit/8db47403ff)\
  2022-01-24 17:22:30 +0100
  * WolfSSL v5.1.1
* [Revision #057178072c](https://github.com/MariaDB/server/commit/057178072c)\
  2022-01-25 10:51:13 +0200
  * Add have\_debug.inc
* [Revision #882f820c66](https://github.com/MariaDB/server/commit/882f820c66)\
  2022-01-24 20:23:35 +0200
  * [MDEV-27451](https://jira.mariadb.org/browse/MDEV-27451) gcol.virtual\_index\_drop fails with LeakSanitizer errors
* [Revision #49e3bd2cbc](https://github.com/MariaDB/server/commit/49e3bd2cbc)\
  2022-01-20 17:16:44 +0100
  * [MDEV-27553](https://jira.mariadb.org/browse/MDEV-27553) Assertion \`inited==INDEX' failed: in ha\_index\_end()
* [Revision #b915f79e4e](https://github.com/MariaDB/server/commit/b915f79e4e)\
  2021-09-29 15:13:57 +0400
  * [MDEV-25904](https://jira.mariadb.org/browse/MDEV-25904) New collation functions to compare InnoDB style trimmed NO PAD strings
* [Revision #db574173d1](https://github.com/MariaDB/server/commit/db574173d1)\
  2022-01-20 15:40:11 +0200
  * Fixed test case for [MDEV-25830](https://jira.mariadb.org/browse/MDEV-25830)
* [Revision #47463e5796](https://github.com/MariaDB/server/commit/47463e5796)\
  2022-01-20 15:44:13 +0400
  * [MDEV-27552](https://jira.mariadb.org/browse/MDEV-27552) Change the return type of my\_uca\_context\_weight\_find() to MY\_CONTRACTION\*
* [Revision #fdec885201](https://github.com/MariaDB/server/commit/fdec885201)\
  2022-01-19 18:34:45 +0200
  * [MDEV-25830](https://jira.mariadb.org/browse/MDEV-25830) optimizer\_use\_condition\_selectivity=4 sometimes produces worse plan than optimizer\_use\_condition\_selectivity=1
* [Revision #c75bee9478](https://github.com/MariaDB/server/commit/c75bee9478)\
  2022-01-13 12:51:54 +0100
  * [MDEV-25538](https://jira.mariadb.org/browse/MDEV-25538) Crash on REPAIR VIEW that was created from IS table
* [Revision #f8c3d59274](https://github.com/MariaDB/server/commit/f8c3d59274)\
  2022-01-04 13:21:14 +0900
  * [MDEV-26583](https://jira.mariadb.org/browse/MDEV-26583) SIGSEGV's in spider\_get\_select\_limit\_from\_select\_lex when DELAYED INSERT is used
* [Revision #e128d852e8](https://github.com/MariaDB/server/commit/e128d852e8)\
  2022-01-17 18:18:30 +0300
  * [MDEV-27272](https://jira.mariadb.org/browse/MDEV-27272) Crash on EXPORT/IMPORT tablespace with column added in the middle
* [Revision #f43ef9ba3a](https://github.com/MariaDB/server/commit/f43ef9ba3a)\
  2022-01-11 14:37:30 +0200
  * [MDEV-25977](https://jira.mariadb.org/browse/MDEV-25977) : Warning: Memory not freed: 32 on SET GLOBAL wsrep\_sst\_auth=USER
* [Revision #cf3adaaa9e](https://github.com/MariaDB/server/commit/cf3adaaa9e)\
  2022-01-11 13:53:34 +0200
  * [MDEV-25494](https://jira.mariadb.org/browse/MDEV-25494) : Assertion \`tl->table == null' failed in bool THD::open\_temporary\_table(TABLE\_LIST\*)
* [Revision #7b555ff2c5](https://github.com/MariaDB/server/commit/7b555ff2c5)\
  2022-01-05 22:55:07 +0100
  * [MDEV-27341](https://jira.mariadb.org/browse/MDEV-27341) Use SET PASSWORD to change PAM service
* [Revision #da76d25ab4](https://github.com/MariaDB/server/commit/da76d25ab4)\
  2021-12-27 18:32:44 +0100
  * [MDEV-26339](https://jira.mariadb.org/browse/MDEV-26339) Account specifics to be handled before proxying
* [Revision #5e04c08d0a](https://github.com/MariaDB/server/commit/5e04c08d0a)\
  2022-01-14 18:18:49 +1100
  * [MDEV-23326](https://jira.mariadb.org/browse/MDEV-23326): mtr fix - slow on timezone intialisation
* [Revision #7b0c2a9980](https://github.com/MariaDB/server/commit/7b0c2a9980)\
  2022-01-14 15:58:38 +0900
  * Revert "[MDEV-26345](https://jira.mariadb.org/browse/MDEV-26345) SELECT MIN on Spider table returns more rows than expected"
* [Revision #2832b949fc](https://github.com/MariaDB/server/commit/2832b949fc)\
  2022-01-13 14:20:05 +0400
  * [MDEV-25659](https://jira.mariadb.org/browse/MDEV-25659) trigger name is empty after upgrade to 10.4
* [Revision #6d8794e567](https://github.com/MariaDB/server/commit/6d8794e567)\
  2022-01-12 15:13:58 +0300
  * [MDEV-21650](https://jira.mariadb.org/browse/MDEV-21650) Non-empty statement transaction on global rollback after TRT update error
* [Revision #6b4f0d782c](https://github.com/MariaDB/server/commit/6b4f0d782c)\
  2021-12-08 12:10:06 +1100
  * [MDEV-23326](https://jira.mariadb.org/browse/MDEV-23326): Aria significantly slow on timezone intialisation
* [Revision #b9730226dc](https://github.com/MariaDB/server/commit/b9730226dc)\
  2021-08-22 19:52:10 +0000
  * [MDEV-26345](https://jira.mariadb.org/browse/MDEV-26345) SELECT MIN on Spider table returns more rows than expected
* [Revision #5a6de6f40c](https://github.com/MariaDB/server/commit/5a6de6f40c)\
  2022-01-05 11:52:33 +0200
  * [MDEV-18848](https://jira.mariadb.org/browse/MDEV-18848) : Galera: 10.4 node crashed with Assertion `client_state.transaction().active()` after altering SEQUENCE table's engine to myisam and back to innodb
* [Revision #c6a890a795](https://github.com/MariaDB/server/commit/c6a890a795)\
  2022-01-04 14:18:34 +0200
  * [MDEV-19353](https://jira.mariadb.org/browse/MDEV-19353) : Alter Sequence do not replicate to another nodes with in Galera Cluster
* [Revision #2ead5bd90a](https://github.com/MariaDB/server/commit/2ead5bd90a)\
  2021-12-27 11:03:14 +0200
  * [MDEV-20886](https://jira.mariadb.org/browse/MDEV-20886) galera.[MDEV-20225](https://jira.mariadb.org/browse/MDEV-20225)
* [Revision #7dfa1168b4](https://github.com/MariaDB/server/commit/7dfa1168b4)\
  2022-01-08 19:56:13 +0100
  * [MDEV-27446](https://jira.mariadb.org/browse/MDEV-27446) Windows, MSI - fix redistributable merge module path for VS2022
* [Revision #8265d6d9f6](https://github.com/MariaDB/server/commit/8265d6d9f6)\
  2022-01-07 11:52:25 -0800
  * [MDEV-22846](https://jira.mariadb.org/browse/MDEV-22846) Server crashes in handler\_index\_cond\_check on SELECT
* [Revision #c18896f9c1](https://github.com/MariaDB/server/commit/c18896f9c1)\
  2021-12-27 18:51:00 +0200
  * [MDEV-14907](https://jira.mariadb.org/browse/MDEV-14907) FEDERATEDX doesn't respect DISTINCT
* [Revision #a48d2ec866](https://github.com/MariaDB/server/commit/a48d2ec866)\
  2021-12-28 16:37:14 +0200
  * Add --valgrind to VERSION() string for valgrind builds
* [Revision #5045509b72](https://github.com/MariaDB/server/commit/5045509b72)\
  2021-12-23 21:07:28 +0900
  * [MDEV-27184](https://jira.mariadb.org/browse/MDEV-27184) Assertion `(old_top == initial_top (av) && old_size == 0) || ((unsigned long) (old_size) >= MINSIZE && prev_inuse (old_top) && ((unsigned long) old_end & (pagesize - 1)) == 0)' failed, Assertion` str.alloced\_length() >= str.length() + data\_len' failed
* Merge [Revision #681b7784b6](https://github.com/MariaDB/server/commit/681b7784b6) 2021-12-25 12:13:03 +0100 - Merge branch 10.3 into 10.4
* [Revision #4b020bfd9a](https://github.com/MariaDB/server/commit/4b020bfd9a)\
  2021-12-23 12:03:09 +0300
  * Fix typos in optimizer trace output
* [Revision #397f5cf71e](https://github.com/MariaDB/server/commit/397f5cf71e)\
  2021-12-23 12:00:05 +0300
  * [MDEV-27238](https://jira.mariadb.org/browse/MDEV-27238): Assertion \`got\_name == named\_item\_expected()' failed in Json\_writer
* [Revision #0165a06322](https://github.com/MariaDB/server/commit/0165a06322)\
  2021-09-13 11:20:22 -0300
  * result of wsrep logic in queue\_for\_group\_commit was being ignored
* [Revision #ca2ea4ff41](https://github.com/MariaDB/server/commit/ca2ea4ff41)\
  2020-05-19 20:15:00 +0300
  * Only apply wsrep\_trx\_fragment\_size to InnoDB tables
* [Revision #4eec6b99e1](https://github.com/MariaDB/server/commit/4eec6b99e1)\
  2020-07-15 11:23:19 +1000
  * [MDEV-23175](https://jira.mariadb.org/browse/MDEV-23175): my\_timer\_milliseconds clock\_gettime for multiple platfomrs
* [Revision #61a66d81b2](https://github.com/MariaDB/server/commit/61a66d81b2)\
  2021-12-20 12:07:20 +0200
  * [MDEV-27297](https://jira.mariadb.org/browse/MDEV-27297) wsrep error log messages drop last character
* [Revision #49791cbc6f](https://github.com/MariaDB/server/commit/49791cbc6f)\
  2021-12-15 22:29:32 +0200
  * 10.4-[MDEV-27275](https://jira.mariadb.org/browse/MDEV-27275) CREATE TABLE with FK not safe for PA
* [Revision #4b25790eb3](https://github.com/MariaDB/server/commit/4b25790eb3)\
  2021-12-20 08:32:11 +0200
  * Update wsrep-lib submodule
* [Revision #53de922ae5](https://github.com/MariaDB/server/commit/53de922ae5)\
  2021-12-17 09:55:01 +0200
  * Enable galera\_sr.GCF-1060 test case as it is now fixed.
* [Revision #c1846c4fcf](https://github.com/MariaDB/server/commit/c1846c4fcf)\
  2021-12-09 18:12:20 +0200
  * [MDEV-26803](https://jira.mariadb.org/browse/MDEV-26803) PA unsafety with FK cascade delete operation
* [Revision #20f22dfa2f](https://github.com/MariaDB/server/commit/20f22dfa2f)\
  2021-12-15 23:29:04 +0200
  * Fixed some tests that failes when built with valgrind
* [Revision #607b14c4dc](https://github.com/MariaDB/server/commit/607b14c4dc)\
  2021-10-19 16:41:45 +0300
  * Add --optimizer\_trace option to mysqltest
* [Revision #3691cc1575](https://github.com/MariaDB/server/commit/3691cc1575)\
  2021-12-15 16:28:01 +0200
  * [MDEV-18187](https://jira.mariadb.org/browse/MDEV-18187) Aria engine: Redo phase failed with "error 192 when executing record redo\_index\_new\_page" upon startup on a restored datadir
* [Revision #dda0bfaaec](https://github.com/MariaDB/server/commit/dda0bfaaec)\
  2021-12-14 03:47:59 +0100
  * [MDEV-27181](https://jira.mariadb.org/browse/MDEV-27181): Galera SST scripts should use ssl\_capath for CA directory
* [Revision #66b492f3e4](https://github.com/MariaDB/server/commit/66b492f3e4)\
  2021-12-13 12:13:03 +0200
  * Fix for the test galera.galera\_UK\_conflict
* [Revision #74b3d4252a](https://github.com/MariaDB/server/commit/74b3d4252a)\
  2021-12-10 11:38:27 +0200
  * [MDEV-27218](https://jira.mariadb.org/browse/MDEV-27218) mtr test galera.[MDEV-20793](https://jira.mariadb.org/browse/MDEV-20793) has sporadic false positive failures
* [Revision #5e8148819e](https://github.com/MariaDB/server/commit/5e8148819e)\
  2021-12-08 14:28:42 +0100
  * minor cleanup of backup\_lock\_binlog.test, so that test passes also with statement binlog format
* [Revision #5c8e628dda](https://github.com/MariaDB/server/commit/5c8e628dda)\
  2021-12-02 22:26:01 +0200
  * wsrep-lib update: bugfixes, cleanups, event API, state transition cleanups
* Merge [Revision #e8a91c18ea](https://github.com/MariaDB/server/commit/e8a91c18ea) 2021-12-07 09:47:42 +0100 - Merge branch '10.3' into 10.4
* [Revision #f458acc81e](https://github.com/MariaDB/server/commit/f458acc81e)\
  2021-12-03 09:56:30 +0200
  * [MDEV-27160](https://jira.mariadb.org/browse/MDEV-27160) Out of memory in main.long\_unique
* [Revision #658a1e1fed](https://github.com/MariaDB/server/commit/658a1e1fed)\
  2019-04-03 08:54:06 +0200
  * Use mysqladmin ping instead of pid files
* [Revision #1b0fb2faa9](https://github.com/MariaDB/server/commit/1b0fb2faa9)\
  2018-11-22 11:54:10 +0100
  * Fix logrotate problem with twice configured pid-file option
* [Revision #d7b37de936](https://github.com/MariaDB/server/commit/d7b37de936)\
  2021-11-27 09:56:56 +0200
  * Fix bad galera tests
* [Revision #cca4e14f9b](https://github.com/MariaDB/server/commit/cca4e14f9b)\
  2021-11-19 12:17:14 +0300
  * Make the Optimizer Trace of reqular query and PS EXECUTE be identical
* Merge [Revision #4da2273876](https://github.com/MariaDB/server/commit/4da2273876) 2021-11-29 10:59:22 +0200 - Merge 10.3 into 10.4
* [Revision #e9572e53e6](https://github.com/MariaDB/server/commit/e9572e53e6)\
  2021-10-15 23:20:48 +0000
  * [MDEV-27124](https://jira.mariadb.org/browse/MDEV-27124): Update definer of Add/DropGeometryColumn procedures from 'root' to 'mariadb.sys'
* [Revision #b53ee760ff](https://github.com/MariaDB/server/commit/b53ee760ff)\
  2021-11-24 12:42:31 +0200
  * Cleanup: offsetof instead of my\_offsetof
* [Revision #7e7235faa9](https://github.com/MariaDB/server/commit/7e7235faa9)\
  2021-11-24 09:55:29 +0200
  * Cleanup: offsetof instead of my\_offsetof
* [Revision #1c7dd233a7](https://github.com/MariaDB/server/commit/1c7dd233a7)\
  2021-11-23 04:41:14 +0100
  * [MDEV-26915](https://jira.mariadb.org/browse/MDEV-26915) post-fix: deleted unnecessary file
* [Revision #1ea7d59650](https://github.com/MariaDB/server/commit/1ea7d59650)\
  2021-11-16 07:32:14 +0100
  * [MDEV-26915](https://jira.mariadb.org/browse/MDEV-26915): SST scripts do not take log\_bin\_index setting into account
* [Revision #f21a36d5e1](https://github.com/MariaDB/server/commit/f21a36d5e1)\
  2021-11-23 02:35:46 +0100
  * [MDEV-26064](https://jira.mariadb.org/browse/MDEV-26064): mariadb-backup SST fails when starting with --innodb-force-recovery
* [Revision #d4d71153db](https://github.com/MariaDB/server/commit/d4d71153db)\
  2021-11-15 00:42:26 +0200
  * Json\_writer\_object add integers
* [Revision #8101af68fa](https://github.com/MariaDB/server/commit/8101af68fa)\
  2021-11-14 06:11:12 +0200
  * [MDEV-27036](https://jira.mariadb.org/browse/MDEV-27036): allow Json\_writer\_\[array|object] from Json\_writer
* Merge [Revision #70e788b1e5](https://github.com/MariaDB/server/commit/70e788b1e5) 2021-11-17 13:59:42 +0200 - Merge 10.3 into 10.4
* [Revision #878f7e38c7](https://github.com/MariaDB/server/commit/878f7e38c7)\
  2021-11-17 13:40:21 +0200
  * [MDEV-23805](https://jira.mariadb.org/browse/MDEV-23805) fixup: Adjsut the [MDEV-16131](https://jira.mariadb.org/browse/MDEV-16131) and [MDEV-24730](https://jira.mariadb.org/browse/MDEV-24730) tests
* [Revision #d270525dfd](https://github.com/MariaDB/server/commit/d270525dfd)\
  2021-11-12 17:46:35 +0530
  * [MDEV-23805](https://jira.mariadb.org/browse/MDEV-23805) Make Online DDL to Instant DDL when table is empty
* Merge [Revision #c5380c30b5](https://github.com/MariaDB/server/commit/c5380c30b5) 2021-11-12 00:16:37 +0100 - Merge branch '10.3' into 10.4
* [Revision #94ef277b5b](https://github.com/MariaDB/server/commit/94ef277b5b)\
  2021-11-09 20:06:22 +0200
  * [MDEV-23766](https://jira.mariadb.org/browse/MDEV-23766): fix by assert (Windows)
* [Revision #04ad98b500](https://github.com/MariaDB/server/commit/04ad98b500)\
  2021-11-05 19:01:43 +0200
  * [MDEV-23766](https://jira.mariadb.org/browse/MDEV-23766): Re-add Json\_writer unit test.
* [Revision #c1e1ca20f4](https://github.com/MariaDB/server/commit/c1e1ca20f4)\
  2019-06-29 15:28:20 +0300
  * In case WITH\_WSREP is enabled, build wsrep as plugin If it is not enabled, build wsrep as static "stub" library from wsrep\_dummy.cc ´
* [Revision #009f3e06f3](https://github.com/MariaDB/server/commit/009f3e06f3)\
  2019-06-28 13:21:39 +0200
  * improve build, allow sql library to be built in parallel with builtins
* [Revision #7acf31783c](https://github.com/MariaDB/server/commit/7acf31783c)\
  2019-05-26 12:54:46 +0200
  * Add new option NOT\_EMBEDDED, for plugins
* [Revision #f7c6c02a06](https://github.com/MariaDB/server/commit/f7c6c02a06)\
  2021-11-09 15:43:10 +0200
  * Revert "improve build, allow sql library to be built in parallel with builtins"
* [Revision #ff08e948d3](https://github.com/MariaDB/server/commit/ff08e948d3)\
  2021-11-09 15:40:50 +0200
  * Revert "In case WITH\_WSREP is enabled, build wsrep as plugin"
* [Revision #9960b98267](https://github.com/MariaDB/server/commit/9960b98267)\
  2021-11-09 15:42:57 +0200
  * [MDEV-23766](https://jira.mariadb.org/browse/MDEV-23766): buildfix: postpone new unittest until its dependency resolution
* [Revision #e9b76b896a](https://github.com/MariaDB/server/commit/e9b76b896a)\
  2021-11-08 21:11:05 +0200
  * [MDEV-23766](https://jira.mariadb.org/browse/MDEV-23766): fix by my\_json\_writer test
* [Revision #5e988ff80f](https://github.com/MariaDB/server/commit/5e988ff80f)\
  2021-11-05 20:01:43 +0300
  * [MDEV-23766](https://jira.mariadb.org/browse/MDEV-23766): Make Json\_writer assert when one tries to author invalid JSON
* [Revision #c9b5b9321f](https://github.com/MariaDB/server/commit/c9b5b9321f)\
  2021-11-05 14:36:59 +0300
  * [MDEV-23766](https://jira.mariadb.org/browse/MDEV-23766): Make Json\_writer assert when one tries to author invalid JSON
* [Revision #e45f7f485a](https://github.com/MariaDB/server/commit/e45f7f485a)\
  2019-06-29 15:28:20 +0300
  * In case WITH\_WSREP is enabled, build wsrep as plugin If it is not enabled, build wsrep as static "stub" library from wsrep\_dummy.cc ´
* [Revision #1a3570dec3](https://github.com/MariaDB/server/commit/1a3570dec3)\
  2019-06-28 13:21:39 +0200
  * improve build, allow sql library to be built in parallel with builtins
* [Revision #b17576322b](https://github.com/MariaDB/server/commit/b17576322b)\
  2021-10-25 00:19:37 +0300
  * [MDEV-23766](https://jira.mariadb.org/browse/MDEV-23766): add Json\_writer consistency asserts to check array/object sequence
* [Revision #cf047efd42](https://github.com/MariaDB/server/commit/cf047efd42)\
  2021-11-02 14:01:54 +0200
  * [MDEV-23766](https://jira.mariadb.org/browse/MDEV-23766): Fix get\_best\_disjunct\_quick by assert:
* [Revision #1f1ee085fb](https://github.com/MariaDB/server/commit/1f1ee085fb)\
  2021-10-29 01:32:21 +0300
  * [MDEV-23766](https://jira.mariadb.org/browse/MDEV-23766): Fix fix\_semijoin\_strategies\_for\_picked\_join\_order by assert
* Merge [Revision #47ab793d71](https://github.com/MariaDB/server/commit/47ab793d71) 2021-11-09 08:40:14 +0200 - Merge 10.3 into 10.4
* Merge [Revision #de2fa9eced](https://github.com/MariaDB/server/commit/de2fa9eced) 2021-11-08 19:39:13 +0100 - Merge branch '10.4' into bb-10.4-release
* [Revision #227b782ad6](https://github.com/MariaDB/server/commit/227b782ad6)\
  2021-11-08 12:39:31 -0500
  * bump the VERSION
* [Revision #d352bc5b67](https://github.com/MariaDB/server/commit/d352bc5b67)\
  2021-10-29 11:44:09 +0300
  * [MDEV-26929](https://jira.mariadb.org/browse/MDEV-26929): Make the main testsuite runnable with optimizer trace enabled
* [Revision #1fdac57447](https://github.com/MariaDB/server/commit/1fdac57447)\
  2021-10-28 03:37:23 +0300
  * [MDEV-26453](https://jira.mariadb.org/browse/MDEV-26453) Assertion \`0' failed in row\_upd\_sec\_index\_entry & corruption
* [Revision #fcca0c67b6](https://github.com/MariaDB/server/commit/fcca0c67b6)\
  2021-10-28 18:35:33 +0300
  * [MDEV-26929](https://jira.mariadb.org/browse/MDEV-26929): fixed opt\_trace test for --mysqld=--optimizer\_trace=enabled=on

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
