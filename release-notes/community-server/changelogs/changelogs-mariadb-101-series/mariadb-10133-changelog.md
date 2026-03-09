# MariaDB 10.1.33 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.33)[Release Notes](../../old-releases/10.1/10.1.33.md)[Changelog](mariadb-10133-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 9 May 2018

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.33.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #1025363a35](https://github.com/MariaDB/server/commit/1025363a35)\
  2018-05-08 02:13:07 +0300
  * Updated list of unstable tests for 10.1.33 release
* Merge [Revision #0db66ab18f](https://github.com/MariaDB/server/commit/0db66ab18f) 2018-05-07 12:07:58 +0300 - Merge 10.0 into 10.1
* [Revision #7b9486d2eb](https://github.com/MariaDB/server/commit/7b9486d2eb)\
  2018-05-07 11:52:05 +0300
  * [MDEV-14693](https://jira.mariadb.org/browse/MDEV-14693) XA: Assertion \`!clust\_index->online\_log' failed in rollback\_inplace\_alter\_table
* [Revision #b4e8ad5080](https://github.com/MariaDB/server/commit/b4e8ad5080)\
  2018-05-06 14:59:15 +0200
  * update test results
* [Revision #f214d36512](https://github.com/MariaDB/server/commit/f214d36512)\
  2018-04-17 00:44:34 +0200
  * ASAN error in is\_stat\_table()
* Merge [Revision #9989c26bc9](https://github.com/MariaDB/server/commit/9989c26bc9) 2018-05-05 14:01:59 +0200 - Merge branch '10.0' into 10.1
* Merge [Revision #3c07ed141c](https://github.com/MariaDB/server/commit/3c07ed141c) 2018-05-04 17:35:09 +0200 - Merge branch '5.5' into 10.0
* [Revision #1d58d184c2](https://github.com/MariaDB/server/commit/1d58d184c2)\
  2018-05-04 00:09:45 +0200
  * protocol: verify that number of rows is correct
* [Revision #04b1e61d69](https://github.com/MariaDB/server/commit/04b1e61d69)\
  2018-05-04 15:51:13 +0200
  * compiler warning
* [Revision #1cb7c4bfc0](https://github.com/MariaDB/server/commit/1cb7c4bfc0)\
  2018-05-03 16:14:54 +0100
  * [MDEV-16084](https://jira.mariadb.org/browse/MDEV-16084) Calling exit() from a signal handler is unsafe.
* [Revision #a411910dd6](https://github.com/MariaDB/server/commit/a411910dd6)\
  2018-05-03 10:26:00 -0400
  * bump the VERSION
* Merge [Revision #b432d4ad66](https://github.com/MariaDB/server/commit/b432d4ad66) 2018-05-03 11:42:19 +0300 - [MDEV-16080](https://jira.mariadb.org/browse/MDEV-16080) Crash in online table rebuild with concurrent DELETE of many BLOBs
* [Revision #f47eac2882](https://github.com/MariaDB/server/commit/f47eac2882)\
  2018-01-10 20:54:09 +0530
  * Bug #25928471: ONLINE ALTER AND CONCURRENT DELETE ON TABLE WITH MANY TEXT COLUMNS CAUSES CRASH
* [Revision #39d248fa55](https://github.com/MariaDB/server/commit/39d248fa55)\
  2018-05-04 22:41:36 +0300
  * [MDEV-16092](https://jira.mariadb.org/browse/MDEV-16092) Crash in encryption.create\_or\_replace
* Merge [Revision #74abc32d30](https://github.com/MariaDB/server/commit/74abc32d30) 2018-04-30 12:54:32 +0300 - Merge pull request #731 from codership/[MDEV-15803](https://jira.mariadb.org/browse/MDEV-15803)
* Merge [Revision #cf333b7fda](https://github.com/MariaDB/server/commit/cf333b7fda) 2018-04-30 12:54:14 +0300 - Merge branch '10.1' into [MDEV-15803](https://jira.mariadb.org/browse/MDEV-15803)
* Merge [Revision #89a7ad636c](https://github.com/MariaDB/server/commit/89a7ad636c) 2018-04-30 07:36:16 +0300 - Merge pull request #732 from codership/galera\_gcs\_fragment\_auto\_inc
* [Revision #b8d4ae0838](https://github.com/MariaDB/server/commit/b8d4ae0838)\
  2018-04-27 12:02:23 +0200
  * Save / restore auto\_increment\_offset in test galera\_gcs\_fragment
* Merge [Revision #ed1d9c802d](https://github.com/MariaDB/server/commit/ed1d9c802d) 2018-04-27 14:42:47 +0300 - Merge pull request #729 from codership/[MDEV-15794](https://jira.mariadb.org/browse/MDEV-15794)
* [Revision #58c03e8f30](https://github.com/MariaDB/server/commit/58c03e8f30)\
  2018-04-26 12:56:24 +0200
  * [MDEV-15794](https://jira.mariadb.org/browse/MDEV-15794) Fix and re-enable test galera\_var\_retry\_autocommit
* Merge [Revision #e0208e51d0](https://github.com/MariaDB/server/commit/e0208e51d0) 2018-04-27 13:37:45 +0300 - Merge pull request #730 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-galera\_ist\_mysqldump
* [Revision #9f9bce5f3e](https://github.com/MariaDB/server/commit/9f9bce5f3e)\
  2018-04-26 13:58:31 +0200
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Record and re-enable galera\_ist\_mysqldump
* [Revision #74f22939dc](https://github.com/MariaDB/server/commit/74f22939dc)\
  2018-04-27 11:05:04 +0200
  * [MDEV-15803](https://jira.mariadb.org/browse/MDEV-15803) Fix and re-enable test galera\_var\_auto\_inc\_control\_on
* Merge [Revision #e2c5283568](https://github.com/MariaDB/server/commit/e2c5283568) 2018-04-27 09:17:01 +0300 - Merge pull request #723 from codership/10.1-[MDEV-16005](https://jira.mariadb.org/browse/MDEV-16005)
* [Revision #2f0b8f3e02](https://github.com/MariaDB/server/commit/2f0b8f3e02)\
  2018-04-24 10:26:34 +0300
  * [MDEV-16005](https://jira.mariadb.org/browse/MDEV-16005) sporadic failures with galera tests MW-328B and MW-328C
* [Revision #a1ea8d6f81](https://github.com/MariaDB/server/commit/a1ea8d6f81)\
  2018-04-26 22:44:09 +0300
  * Follow-up fix to [MDEV-14705](https://jira.mariadb.org/browse/MDEV-14705): Flush log at shutdown
* [Revision #dc0613edc4](https://github.com/MariaDB/server/commit/dc0613edc4)\
  2018-04-26 12:23:19 +0300
  * [MDEV-15809](https://jira.mariadb.org/browse/MDEV-15809): Test failure on galera.MW-44
* Merge [Revision #779343235b](https://github.com/MariaDB/server/commit/779343235b) 2018-04-25 10:24:08 +0300 - Merge pull request #722 from codership/[MDEV-16006](https://jira.mariadb.org/browse/MDEV-16006)
* [Revision #dfb1fdabab](https://github.com/MariaDB/server/commit/dfb1fdabab)\
  2018-04-24 16:32:44 +0200
  * [MDEV-16006](https://jira.mariadb.org/browse/MDEV-16006) Fix test galera\_kill\_nochanges
* Merge [Revision #2cdaa5696c](https://github.com/MariaDB/server/commit/2cdaa5696c) 2018-04-25 08:47:54 +0300 - Merge pull request #719 from codership/[MDEV-15811](https://jira.mariadb.org/browse/MDEV-15811)
* [Revision #92cd6bb510](https://github.com/MariaDB/server/commit/92cd6bb510)\
  2018-04-24 14:29:56 +0200
  * [MDEV-15811](https://jira.mariadb.org/browse/MDEV-15811) Fix and re-enable test galera.galera\_pc\_ignore\_sb
* Merge [Revision #9c34a4124d](https://github.com/MariaDB/server/commit/9c34a4124d) 2018-04-24 09:26:40 +0300 - Merge 10.0 into 10.1
* [Revision #5b79303b40](https://github.com/MariaDB/server/commit/5b79303b40)\
  2018-04-23 18:14:15 +0300
  * [MDEV-15988](https://jira.mariadb.org/browse/MDEV-15988) Crash in ./mtr mariadb-backup.undo\_space\_id
* Merge [Revision #82d4f08186](https://github.com/MariaDB/server/commit/82d4f08186) 2018-04-23 14:25:34 +0300 - Merge pull request #713 from codership/[MDEV-15948](https://jira.mariadb.org/browse/MDEV-15948)
* [Revision #63e5307afd](https://github.com/MariaDB/server/commit/63e5307afd)\
  2018-04-23 12:00:49 +0200
  * [MDEV-15948](https://jira.mariadb.org/browse/MDEV-15948) Followup commit
* [Revision #9e5671f1cc](https://github.com/MariaDB/server/commit/9e5671f1cc)\
  2018-04-20 14:44:27 +0200
  * [MDEV-15948](https://jira.mariadb.org/browse/MDEV-15948) Fix error "Lost connection to MySQL server..." in test galera\_sst\_mysqldump
* Merge [Revision #31a19683f5](https://github.com/MariaDB/server/commit/31a19683f5) 2018-04-23 07:46:45 +0300 - Merge pull request #711 from codership/[MDEV-15929](https://jira.mariadb.org/browse/MDEV-15929)
* [Revision #3aa5f00e69](https://github.com/MariaDB/server/commit/3aa5f00e69)\
  2018-04-19 10:29:13 +0200
  * [MDEV-15929](https://jira.mariadb.org/browse/MDEV-15929) Fix lock wait timeout on `SELECT @@GLOBAL.WSREP_ON`
* [Revision #3d1ad2a5e8](https://github.com/MariaDB/server/commit/3d1ad2a5e8)\
  2018-04-16 15:06:41 +0300
  * [MDEV-13516](https://jira.mariadb.org/browse/MDEV-13516): encryption.create\_or\_replace test fails in buildbot with InnoDB assertion failure
* [Revision #3e12e39fb3](https://github.com/MariaDB/server/commit/3e12e39fb3)\
  2018-04-13 22:18:36 +0200
  * skip innodb-table-online,crypt tests if no encryption plugin
* [Revision #2bf355fa81](https://github.com/MariaDB/server/commit/2bf355fa81)\
  2018-04-13 12:50:03 +0300
  * [MDEV-15672](https://jira.mariadb.org/browse/MDEV-15672): encryption.innodb\_encryption\_filekeys - typo in I\_S column name: ENCRYPTION\_SHCEME
* [Revision #3855943fe0](https://github.com/MariaDB/server/commit/3855943fe0)\
  2018-04-13 09:25:52 +0300
  * [MDEV-12632](https://jira.mariadb.org/browse/MDEV-12632): Source and destination overlap in memcpy, encryption.innodb-discard-import-change fails in buildbot with valgrind
* [Revision #82e968197a](https://github.com/MariaDB/server/commit/82e968197a)\
  2018-04-12 16:02:25 +0300
  * [MDEV-15580](https://jira.mariadb.org/browse/MDEV-15580): Assertion \`!lex->explain' failed in lex\_start(THD\*):
* [Revision #c2dc72c0c3](https://github.com/MariaDB/server/commit/c2dc72c0c3)\
  2018-04-12 12:09:32 +0100
  * [MDEV-15779](https://jira.mariadb.org/browse/MDEV-15779) - mariadb-backup incremental prepare fails on CIFS mount.
* [Revision #15071226a0](https://github.com/MariaDB/server/commit/15071226a0)\
  2018-04-11 23:07:23 +0100
  * [MDEV-15780](https://jira.mariadb.org/browse/MDEV-15780) : mariadb-backup with absolute paths in innodb\_data\_file\_path
* [Revision #0ae13b51d7](https://github.com/MariaDB/server/commit/0ae13b51d7)\
  2018-04-12 11:00:48 +0300
  * [MDEV-12632](https://jira.mariadb.org/browse/MDEV-12632): Source and destination overlap in memcpy, encryption.innodb-discard-import-change fails in buildbot with valgrind
* [Revision #9518ddd1fb](https://github.com/MariaDB/server/commit/9518ddd1fb)\
  2018-04-11 14:06:29 +0300
  * [MDEV-12903](https://jira.mariadb.org/browse/MDEV-12903): encryption.innodb\_encryption\_discard\_import fails in buildbot with FOUND vs NOT FOUND
* [Revision #d98514690f](https://github.com/MariaDB/server/commit/d98514690f)\
  2018-04-11 15:44:31 +0100
  * Make mroonga respect -DWITHOUT\_DYNAMIC\_PLUGINS.
* Merge [Revision #c6c679e947](https://github.com/MariaDB/server/commit/c6c679e947) 2018-04-11 16:19:59 +0300 - Merge pull request #700 from codership/[MDEV-15804](https://jira.mariadb.org/browse/MDEV-15804)
* [Revision #4dc60dc3f1](https://github.com/MariaDB/server/commit/4dc60dc3f1)\
  2018-04-11 14:24:39 +0200
  * [MDEV-15804](https://jira.mariadb.org/browse/MDEV-15804) Fix and re-enable MTR test galera.pxc-421
* Merge [Revision #8be2c72bd5](https://github.com/MariaDB/server/commit/8be2c72bd5) 2018-04-11 15:53:46 +0300 - Merge pull request #699 from codership/[MDEV-15808](https://jira.mariadb.org/browse/MDEV-15808)
* [Revision #73b3ace8b2](https://github.com/MariaDB/server/commit/73b3ace8b2)\
  2018-04-11 09:14:35 +0200
  * [MDEV-15808](https://jira.mariadb.org/browse/MDEV-15808) Fix and re-enable test galera.galera\_gra\_log
* [Revision #2e91eb7547](https://github.com/MariaDB/server/commit/2e91eb7547)\
  2018-04-10 17:34:56 +0300
  * Fix warnings in InnoDB & XtraDB post [MDEV-14705](https://jira.mariadb.org/browse/MDEV-14705)
* [Revision #1fd07d21a7](https://github.com/MariaDB/server/commit/1fd07d21a7)\
  2018-04-10 13:25:19 +0300
  * [MDEV-15823](https://jira.mariadb.org/browse/MDEV-15823): Test failure on galera.galera\_var\_slave\_threads
* [Revision #f932d3f879](https://github.com/MariaDB/server/commit/f932d3f879)\
  2018-04-10 08:40:08 +0300
  * [MDEV-14705](https://jira.mariadb.org/browse/MDEV-14705): Extend timeout for waiting for transactions
* [Revision #8eff803a1b](https://github.com/MariaDB/server/commit/8eff803a1b)\
  2018-04-10 08:29:29 +0300
  * Revert "[MDEV-14705](https://jira.mariadb.org/browse/MDEV-14705): Do not rollback on InnoDB shutdown"
* [Revision #ecf6675cfc](https://github.com/MariaDB/server/commit/ecf6675cfc)\
  2018-04-09 19:16:50 +0100
  * [MDEV-15713](https://jira.mariadb.org/browse/MDEV-15713) mariadb-backup: throw warning, if --stream is used without --backup
* [Revision #37f24806fc](https://github.com/MariaDB/server/commit/37f24806fc)\
  2018-04-09 16:22:15 +0100
  * [MDEV-15825](https://jira.mariadb.org/browse/MDEV-15825) mariadb-backup help mentions Percona and PXC but not MariaDB
* [Revision #8ff897265a](https://github.com/MariaDB/server/commit/8ff897265a)\
  2018-04-09 16:49:41 +0300
  * Update test cases post [MDEV-10286](https://jira.mariadb.org/browse/MDEV-10286)
* [Revision #803ded5148](https://github.com/MariaDB/server/commit/803ded5148)\
  2018-04-09 14:43:32 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* [Revision #fe61e287e9](https://github.com/MariaDB/server/commit/fe61e287e9)\
  2018-04-09 07:49:00 +0300
  * [MDEV-15810](https://jira.mariadb.org/browse/MDEV-15810): Test failure on galera.lp1376747 and galera.lp1376747-2
* [Revision #767d6ce38c](https://github.com/MariaDB/server/commit/767d6ce38c)\
  2018-04-09 07:28:13 +0300
  * [MDEV-15807](https://jira.mariadb.org/browse/MDEV-15807): Test failure on galera.galera\_lock\_table
* [Revision #8bb40f2404](https://github.com/MariaDB/server/commit/8bb40f2404)\
  2018-04-08 13:04:38 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* [Revision #1568950a7d](https://github.com/MariaDB/server/commit/1568950a7d)\
  2018-04-08 09:03:55 +0300
  * [MDEV-15806](https://jira.mariadb.org/browse/MDEV-15806): Test failure on galera.galera\_parallel\_simple
* [Revision #c4b1a57b13](https://github.com/MariaDB/server/commit/c4b1a57b13)\
  2018-04-08 08:24:36 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* [Revision #d9c85ee45a](https://github.com/MariaDB/server/commit/d9c85ee45a)\
  2018-04-07 19:52:35 +0300
  * [MDEV-15752](https://jira.mariadb.org/browse/MDEV-15752) Possible race between DDL and accessing I\_S.INNODB\_TABLESPACES\_ENCRYPTION
* Merge [Revision #4c89cff558](https://github.com/MariaDB/server/commit/4c89cff558) 2018-04-07 17:11:22 +0300 - Merge branch '10.0' into 10.1
* [Revision #4ede2fec4c](https://github.com/MariaDB/server/commit/4ede2fec4c)\
  2018-04-07 08:52:24 +0300
  * Disable galera\_var\_auto\_inc\_control\_on test.
* Merge [Revision #3756e27aa7](https://github.com/MariaDB/server/commit/3756e27aa7) 2018-04-07 08:51:33 +0300 - Merge pull request #694 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-galera\_wsrep\_desync\_wsrep\_on
* [Revision #7925cdff6b](https://github.com/MariaDB/server/commit/7925cdff6b)\
  2018-04-06 14:59:16 +0200
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Fix test galera.galera\_wsrep\_desync\_wsrep\_on
* [Revision #c0b781d25e](https://github.com/MariaDB/server/commit/c0b781d25e)\
  2018-04-06 16:33:41 +0300
  * Disable test galera\_var\_auto\_inc\_control\_on as it fails.
* [Revision #8325d71f6c](https://github.com/MariaDB/server/commit/8325d71f6c)\
  2018-04-06 13:10:01 +0300
  * Fix a compilation error
* [Revision #81075d45c6](https://github.com/MariaDB/server/commit/81075d45c6)\
  2018-04-06 12:55:43 +0300
  * [MDEV-15566](https://jira.mariadb.org/browse/MDEV-15566): System tablespace does not easily key rotate to unencrypted
* [Revision #3be6cef593](https://github.com/MariaDB/server/commit/3be6cef593)\
  2018-04-06 12:35:25 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* [Revision #3498a656c9](https://github.com/MariaDB/server/commit/3498a656c9)\
  2018-04-06 12:25:41 +0300
  * [MDEV-14705](https://jira.mariadb.org/browse/MDEV-14705): Follow-up fixes
* [Revision #d61ed5dd8a](https://github.com/MariaDB/server/commit/d61ed5dd8a)\
  2018-04-06 12:27:18 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* [Revision #1479273cdb](https://github.com/MariaDB/server/commit/1479273cdb)\
  2017-11-30 13:37:59 +1100
  * [MDEV-14705](https://jira.mariadb.org/browse/MDEV-14705): slow innodb startup/shutdown can exceed systemd timeout
* [Revision #e7f4e61f6e](https://github.com/MariaDB/server/commit/e7f4e61f6e)\
  2018-03-24 17:44:19 +1100
  * [MDEV-14705](https://jira.mariadb.org/browse/MDEV-14705): Speed up InnoDB shutdown
* [Revision #76ec37f522](https://github.com/MariaDB/server/commit/76ec37f522)\
  2018-04-05 18:15:10 +0300
  * [MDEV-14705](https://jira.mariadb.org/browse/MDEV-14705): Do not rollback on InnoDB shutdown
* [Revision #3a6283cb3c](https://github.com/MariaDB/server/commit/3a6283cb3c)\
  2018-04-06 08:48:11 +0300
  * Fix out of array access.
* [Revision #afbd45a791](https://github.com/MariaDB/server/commit/afbd45a791)\
  2018-04-05 15:23:13 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* [Revision #6449f0559b](https://github.com/MariaDB/server/commit/6449f0559b)\
  2018-04-05 14:18:57 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* [Revision #33b103b4ca](https://github.com/MariaDB/server/commit/33b103b4ca)\
  2018-04-05 13:30:41 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* [Revision #b1bf571e3d](https://github.com/MariaDB/server/commit/b1bf571e3d)\
  2018-04-05 12:40:11 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* [Revision #a41bd33d3b](https://github.com/MariaDB/server/commit/a41bd33d3b)\
  2018-04-05 12:23:53 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* Merge [Revision #e2e1483dd2](https://github.com/MariaDB/server/commit/e2e1483dd2) 2018-04-05 17:13:53 +0300 - Merge pull request #675 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-MW-284
* [Revision #45eca6178e](https://github.com/MariaDB/server/commit/45eca6178e)\
  2018-03-27 14:29:43 +0200
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Fix and re-enable MTR test galera.MW-284
* [Revision #87d763015a](https://github.com/MariaDB/server/commit/87d763015a)\
  2018-04-05 10:31:42 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* Merge [Revision #2ad51c3153](https://github.com/MariaDB/server/commit/2ad51c3153) 2018-04-05 08:59:28 +0300 - Merge pull request #686 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-mysql-wsrep#90
* [Revision #390e5ab794](https://github.com/MariaDB/server/commit/390e5ab794)\
  2018-03-29 15:50:06 +0200
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Fix and re-enable MTR test galera.mysql-wsrep#90
* Merge [Revision #4f3d2e60ad](https://github.com/MariaDB/server/commit/4f3d2e60ad) 2018-04-04 15:26:05 +0300 - Merge pull request #690 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-galera\_gra\_log
* [Revision #eeb684221d](https://github.com/MariaDB/server/commit/eeb684221d)\
  2018-04-03 16:30:58 +0200
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Fix and re-enable MTR test galera.galera\_gra\_log
* [Revision #ed33296246](https://github.com/MariaDB/server/commit/ed33296246)\
  2018-01-19 00:24:39 +0100
  * Fix LibreSSL X509 (SSL) certificate hostname checking.
* [Revision #7ffa82b03c](https://github.com/MariaDB/server/commit/7ffa82b03c)\
  2018-03-22 08:51:43 +0200
  * [MDEV-14616](https://jira.mariadb.org/browse/MDEV-14616): WSREP has not yet prepared node for application use error
* [Revision #992370693f](https://github.com/MariaDB/server/commit/992370693f)\
  2017-09-15 16:56:36 +0200
  * MW-405 Remove wait\_until\_connected\_again.inc from kill\_galera.inc
* [Revision #54652161a2](https://github.com/MariaDB/server/commit/54652161a2)\
  2017-09-14 16:54:53 +0200
  * MW-405 Adjust galera\_pc\_weight to new wait\_until\_connected\_again
* [Revision #fc26fd1c47](https://github.com/MariaDB/server/commit/fc26fd1c47)\
  2017-09-14 11:48:50 +0200
  * MW-405 Remove redundant conditions
* [Revision #d970f805e6](https://github.com/MariaDB/server/commit/d970f805e6)\
  2017-09-14 13:46:34 +0200
  * MW-405 Make sure wsrep is ready in wait\_until\_connected\_again.inc
* Merge [Revision #d21adb53a5](https://github.com/MariaDB/server/commit/d21adb53a5) 2018-03-29 08:07:47 +0300 - Merge pull request #676 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-galera\_gtid\_slave
* [Revision #e376122460](https://github.com/MariaDB/server/commit/e376122460)\
  2018-03-28 11:35:09 +0200
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Fix and re-enable MTR test galera.galera\_gtid\_slave
* Merge [Revision #e550063ad9](https://github.com/MariaDB/server/commit/e550063ad9) 2018-03-28 15:44:47 +0300 - Merge pull request #674 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-galera\_as\_master
* [Revision #58fad0400c](https://github.com/MariaDB/server/commit/58fad0400c)\
  2018-03-27 14:23:45 +0200
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Fix and re-enable MTR test galera.galera\_as\_master
* Merge [Revision #11ac2df027](https://github.com/MariaDB/server/commit/11ac2df027) 2018-03-28 08:09:40 +0300 - Merge pull request #673 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-galera\_suspend\_slave
* [Revision #832025b512](https://github.com/MariaDB/server/commit/832025b512)\
  2018-03-27 12:05:33 +0200
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Fix and re-enable test galera.galera\_suspend\_slave
* [Revision #db16ae54f6](https://github.com/MariaDB/server/commit/db16ae54f6)\
  2018-03-27 12:56:59 -0400
  * bump the VERSION
* [Revision #2f2e7f8c9d](https://github.com/MariaDB/server/commit/2f2e7f8c9d)\
  2018-03-25 14:05:30 +0300
  * Fixed compiler warnings in sphinx
* [Revision #8bb51f612e](https://github.com/MariaDB/server/commit/8bb51f612e)\
  2018-03-25 13:38:12 +0300
  * disable some galera tests that fails regurarly
* [Revision #9aa1ab5a59](https://github.com/MariaDB/server/commit/9aa1ab5a59)\
  2018-03-23 14:52:14 +0200
  * Fixed compiler warning
* [Revision #ca0c96fc89](https://github.com/MariaDB/server/commit/ca0c96fc89)\
  2018-03-22 20:03:54 +0200
  * Adjust table\_open\_cache to avoid getting error 24 (too many open files)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
