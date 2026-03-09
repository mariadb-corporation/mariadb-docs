# MariaDB 10.3.6 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.6)[Release Notes](../../old-releases/10.3/10.3.6.md)[Changelog](mariadb-1036-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 16 Apr 2018

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.6.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #5607431986](https://github.com/MariaDB/server/commit/5607431986)\
  2018-04-13 21:46:12 +0200
  * disable failing galera test for now
* [Revision #95811f01f3](https://github.com/MariaDB/server/commit/95811f01f3)\
  2018-04-12 15:16:29 +0300
  * [MDEV-15796](https://jira.mariadb.org/browse/MDEV-15796) MariaDB crashes on startup with semisync master enabled
* [Revision #93b3a48436](https://github.com/MariaDB/server/commit/93b3a48436)\
  2018-04-13 12:50:03 +0300
  * [MDEV-15672](https://jira.mariadb.org/browse/MDEV-15672): encryption.innodb\_encryption\_filekeys - typo in I\_S column name: ENCRYPTION\_SHCEME
* [Revision #71ceed7523](https://github.com/MariaDB/server/commit/71ceed7523)\
  2018-04-13 09:25:52 +0300
  * [MDEV-12632](https://jira.mariadb.org/browse/MDEV-12632): Source and destination overlap in memcpy, encryption.innodb-discard-import-change fails in buildbot with valgrind
* [Revision #fe20fe0d0a](https://github.com/MariaDB/server/commit/fe20fe0d0a)\
  2018-04-12 16:02:25 +0300
  * [MDEV-15580](https://jira.mariadb.org/browse/MDEV-15580): Assertion \`!lex->explain' failed in lex\_start(THD\*):
* [Revision #479fb6c1e9](https://github.com/MariaDB/server/commit/479fb6c1e9)\
  2018-04-12 20:40:58 +0200
  * ./mtr --client-gdb
* [Revision #1f6bd88c24](https://github.com/MariaDB/server/commit/1f6bd88c24)\
  2018-04-12 09:58:09 +0200
  * [MDEV-15728](https://jira.mariadb.org/browse/MDEV-15728) main.thread\_id\_overflow fails in ps-protocol
* [Revision #41983fd3b1](https://github.com/MariaDB/server/commit/41983fd3b1)\
  2018-04-10 21:15:46 +0200
  * [MDEV-15788](https://jira.mariadb.org/browse/MDEV-15788) versioning.partition, versioning.rpl fail on most windows builds in buildbot
* Merge [Revision #09eb313375](https://github.com/MariaDB/server/commit/09eb313375) 2018-04-12 11:57:29 -0700 - [MDEV-15692](https://jira.mariadb.org/browse/MDEV-15692): install\_spider.sql can fail with some collations
* [Revision #ff0bf451db](https://github.com/MariaDB/server/commit/ff0bf451db)\
  2018-04-05 14:23:31 -0700
  * [MDEV-15692](https://jira.mariadb.org/browse/MDEV-15692): install\_spider.sql can fail with some collations
* [Revision #18e8d420b7](https://github.com/MariaDB/server/commit/18e8d420b7)\
  2018-04-12 16:50:33 +0100
  * Feedback plugin - MSI installation checkbox switched to OFF again.
* Merge [Revision #65eefcdc60](https://github.com/MariaDB/server/commit/65eefcdc60) 2018-04-12 12:41:19 +0300 - Merge remote-tracking branch '10.2' into 10.3
* [Revision #36c0116720](https://github.com/MariaDB/server/commit/36c0116720)\
  2018-04-12 11:00:48 +0300
  * [MDEV-12632](https://jira.mariadb.org/browse/MDEV-12632): Source and destination overlap in memcpy, encryption.innodb-discard-import-change fails in buildbot with valgrind
* [Revision #2f1f160979](https://github.com/MariaDB/server/commit/2f1f160979)\
  2018-04-11 14:06:29 +0300
  * [MDEV-12903](https://jira.mariadb.org/browse/MDEV-12903): encryption.innodb\_encryption\_discard\_import fails in buildbot with FOUND vs NOT FOUND
* [Revision #93aded05ea](https://github.com/MariaDB/server/commit/93aded05ea)\
  2018-04-12 03:26:39 +0300
  * Use same connection convention of specifying IPs
* [Revision #990283b65c](https://github.com/MariaDB/server/commit/990283b65c)\
  2018-04-12 02:34:51 +0300
  * Fix perfschema.hostcache\_ipv4\_max\_con
* [Revision #4c7a1a1b9e](https://github.com/MariaDB/server/commit/4c7a1a1b9e)\
  2018-04-11 23:22:33 +0100
  * [MDEV-15780](https://jira.mariadb.org/browse/MDEV-15780) : mariadb-backup does not handle absolute names in for system tablespaces
* [Revision #740fc2ae08](https://github.com/MariaDB/server/commit/740fc2ae08)\
  2018-04-10 18:07:29 -0700
  * Fixed [MDEV-15765](https://jira.mariadb.org/browse/MDEV-15765) BETWEEN not working in certain cases
* Merge [Revision #45e6d0aebf](https://github.com/MariaDB/server/commit/45e6d0aebf) 2018-04-10 17:43:18 +0300 - Merge branch '10.1' into 10.2
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
* [Revision #400a8eb60f](https://github.com/MariaDB/server/commit/400a8eb60f)\
  2018-04-06 13:33:08 +0400
  * [MDEV-15291](https://jira.mariadb.org/browse/MDEV-15291) - OQGraph fails to build on FreeBSD
* [Revision #8901155780](https://github.com/MariaDB/server/commit/8901155780)\
  2018-04-04 23:35:47 +0200
  * Update contributors
* Merge [Revision #6a72b9096a](https://github.com/MariaDB/server/commit/6a72b9096a) 2018-04-03 18:08:30 +0300 - Merge branch '5.5' into 10.0
* [Revision #f5369faf5b](https://github.com/MariaDB/server/commit/f5369faf5b)\
  2018-03-29 15:25:08 +0200
  * don't disable SSL when connecting via libmysqld
* [Revision #df6197c8b9](https://github.com/MariaDB/server/commit/df6197c8b9)\
  2018-02-23 18:50:12 +0100
  * compiler warning
* [Revision #606e21867c](https://github.com/MariaDB/server/commit/606e21867c)\
  2018-04-03 16:28:52 +0400
  * [MDEV-15630](https://jira.mariadb.org/browse/MDEV-15630) uuid() function evaluates at wrong time in query
* [Revision #bdab8b74ff](https://github.com/MariaDB/server/commit/bdab8b74ff)\
  2018-03-24 03:31:18 +0530
  * [MDEV-11274](https://jira.mariadb.org/browse/MDEV-11274): Executing EXPLAIN of complex query over join limit causes server to crash
* [Revision #e8c2366bf8](https://github.com/MariaDB/server/commit/e8c2366bf8)\
  2018-03-27 09:40:10 +0400
  * [MDEV-15620](https://jira.mariadb.org/browse/MDEV-15620) Crash when using "SET @@NEW.a=expr" inside a trigger
* [Revision #8ffbb825e6](https://github.com/MariaDB/server/commit/8ffbb825e6)\
  2018-03-27 07:55:56 +1100
  * increase upper value of max\_prepared\_stmt\_count to UINT32\_MAX
* [Revision #10f6b7001b](https://github.com/MariaDB/server/commit/10f6b7001b)\
  2018-04-02 13:14:30 +0300
  * [MDEV-9744](https://jira.mariadb.org/browse/MDEV-9744): session optimizer\_use\_condition\_selectivity=5 causing SQL Error (1918): Encountered illegal value '' when converting to DECIMAL
* [Revision #6aff5fa27a](https://github.com/MariaDB/server/commit/6aff5fa27a)\
  2018-03-26 10:33:58 +0400
  * [MDEV-15619](https://jira.mariadb.org/browse/MDEV-15619) using CONVERT() inside AES\_ENCRYPT() in an UPDATE corrupts data
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
* [Revision #4d83b01537](https://github.com/MariaDB/server/commit/4d83b01537)\
  2018-03-26 17:14:08 +0300
  * Updated list of unstable tests for 10.1.32 release
* [Revision #f5cb66fb97](https://github.com/MariaDB/server/commit/f5cb66fb97)\
  2018-04-10 14:27:18 +0400
  * Test cleanup for [MDEV-15833](https://jira.mariadb.org/browse/MDEV-15833) (uncommenting forgotten tests)
* [Revision #4d9c5844b8](https://github.com/MariaDB/server/commit/4d9c5844b8)\
  2018-04-10 13:15:57 +0400
  * [MDEV-15833](https://jira.mariadb.org/browse/MDEV-15833) Row format replication between LONGBLOB and MEDIUMBLOB does not work for long values
* [Revision #141592cedb](https://github.com/MariaDB/server/commit/141592cedb)\
  2018-04-10 02:07:31 +0300
  * Clean up a test
* [Revision #7b16291c36](https://github.com/MariaDB/server/commit/7b16291c36)\
  2018-04-05 13:17:17 +0100
  * [MDEV-15707](https://jira.mariadb.org/browse/MDEV-15707) : deadlock in Innodb IO code, caused by change buffering.
* [Revision #b4c2ceb214](https://github.com/MariaDB/server/commit/b4c2ceb214)\
  2018-04-07 15:03:15 +0300
  * [MDEV-15769](https://jira.mariadb.org/browse/MDEV-15769): Assertion \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed
* [Revision #1cb2e0333d](https://github.com/MariaDB/server/commit/1cb2e0333d)\
  2018-04-07 14:05:28 +0300
  * [MDEV-12466](https://jira.mariadb.org/browse/MDEV-12466) : Assertion \`thd->transaction.stmt.is\_empty() || thd->in\_sub\_stmt || ...
* [Revision #5ccf3f96ac](https://github.com/MariaDB/server/commit/5ccf3f96ac)\
  2018-04-05 17:36:59 +0400
  * Fix misuse of MY\_CHECK\_CXX\_COMPILER\_FLAG
* [Revision #4fde1361a6](https://github.com/MariaDB/server/commit/4fde1361a6)\
  2018-04-05 15:01:17 +0300
  * [MDEV-15553](https://jira.mariadb.org/browse/MDEV-15553) Assertion failed in dict\_table\_get\_col\_name
* [Revision #9c42b9038d](https://github.com/MariaDB/server/commit/9c42b9038d)\
  2018-04-12 11:00:48 +0300
  * [MDEV-12632](https://jira.mariadb.org/browse/MDEV-12632): Source and destination overlap in memcpy, encryption.innodb-discard-import-change fails in buildbot with valgrind
* [Revision #91245909a2](https://github.com/MariaDB/server/commit/91245909a2)\
  2018-04-11 14:06:29 +0300
  * [MDEV-12903](https://jira.mariadb.org/browse/MDEV-12903): encryption.innodb\_encryption\_discard\_import fails in buildbot with FOUND vs NOT FOUND
* [Revision #dd127799bc](https://github.com/MariaDB/server/commit/dd127799bc)\
  2018-04-10 18:01:21 +0300
  * [MDEV-15832](https://jira.mariadb.org/browse/MDEV-15832) With innodb\_fast\_shutdown=3, skip the rollback of connected transactions
* [Revision #8334aced00](https://github.com/MariaDB/server/commit/8334aced00)\
  2018-04-10 16:17:15 +0100
  * [MDEV-14380](https://jira.mariadb.org/browse/MDEV-14380) Reduce possibility to timing-induced error in test
* [Revision #9e9ea4f64a](https://github.com/MariaDB/server/commit/9e9ea4f64a)\
  2018-04-10 15:34:20 +0400
  * [MDEV-15821](https://jira.mariadb.org/browse/MDEV-15821) Row format replication from LONGBLOB COMPRESSED to LONGBLOB does not work
* [Revision #9bd3af97df](https://github.com/MariaDB/server/commit/9bd3af97df)\
  2018-04-02 19:35:27 +0200
  * [MDEV-15413](https://jira.mariadb.org/browse/MDEV-15413) Unexpected errors upon CREATE TABLE .. WITH SYSTEM VERSIONING AS SELECT ...
* [Revision #72dd813f7e](https://github.com/MariaDB/server/commit/72dd813f7e)\
  2018-02-27 18:08:49 +0300
  * [MDEV-15427](https://jira.mariadb.org/browse/MDEV-15427) IB: TRX\_ID based operations inside transaction generate history
* [Revision #a4251d6f18](https://github.com/MariaDB/server/commit/a4251d6f18)\
  2018-03-03 17:44:40 +0300
  * [MDEV-15391](https://jira.mariadb.org/browse/MDEV-15391) Server crashes in JOIN::fix\_all\_splittings\_in\_plan or Assertion \`join->best\_read < double(1.79...e+308L)' failed
* [Revision #1a86fc5f14](https://github.com/MariaDB/server/commit/1a86fc5f14)\
  2018-03-03 20:58:30 +0300
  * [MDEV-15378](https://jira.mariadb.org/browse/MDEV-15378) Valid query causes invalid view definition due to syntax limitation in FOR SYSTEM\_TIME
* [Revision #bb56a06d26](https://github.com/MariaDB/server/commit/bb56a06d26)\
  2018-03-16 15:47:48 +0300
  * [MDEV-15062](https://jira.mariadb.org/browse/MDEV-15062) Information Schema COLUMNS Table does not show system versioning information
* [Revision #339b905579](https://github.com/MariaDB/server/commit/339b905579)\
  2018-03-30 23:13:17 +0200
  * ./mtr --gdb='b mysql\_parse;r'
* [Revision #041e9de6f8](https://github.com/MariaDB/server/commit/041e9de6f8)\
  2018-03-30 19:15:55 +0200
  * wording: don't prohibit
* [Revision #689f83d0ce](https://github.com/MariaDB/server/commit/689f83d0ce)\
  2018-03-29 20:24:29 +0200
  * [MDEV-14790](https://jira.mariadb.org/browse/MDEV-14790) System versioning for system tables does not work as expected
* [Revision #dba43f4bec](https://github.com/MariaDB/server/commit/dba43f4bec)\
  2018-03-30 18:54:52 +0200
  * fix comparison of row\_start/row\_end
* [Revision #08a901cc0b](https://github.com/MariaDB/server/commit/08a901cc0b)\
  2018-03-30 18:53:33 +0200
  * cleanup: remove XString::operator== and !=
* [Revision #0dcb47cae9](https://github.com/MariaDB/server/commit/0dcb47cae9)\
  2018-03-30 15:42:38 +0200
  * change lex\_string\_eq to return what it says
* [Revision #479bd5a6fe](https://github.com/MariaDB/server/commit/479bd5a6fe)\
  2018-03-29 23:23:19 +0200
  * improve strmake\_buf() to detect wrong usage reliably
* [Revision #7dcf1b5049](https://github.com/MariaDB/server/commit/7dcf1b5049)\
  2018-02-26 18:33:46 +0100
  * dead code in versioning/common.inc
* [Revision #35678c9572](https://github.com/MariaDB/server/commit/35678c9572)\
  2018-02-26 17:17:17 +0100
  * dead code - related to vtmd
* [Revision #09e6280147](https://github.com/MariaDB/server/commit/09e6280147)\
  2018-02-26 16:29:59 +0100
  * remove unused THD::query\_start\_used
* [Revision #85194bd6ba](https://github.com/MariaDB/server/commit/85194bd6ba)\
  2018-04-03 14:14:00 +0200
  * fix detection of "-Wa,-nH" compiler flags on SunOS/i386
* Merge [Revision #e7cbb2afa1](https://github.com/MariaDB/server/commit/e7cbb2afa1) 2018-04-10 10:41:20 +0300 - Merge pull request #696 from tempesta-tech/tt-10.3-kevgs
* [Revision #1513630d30](https://github.com/MariaDB/server/commit/1513630d30)\
  2018-04-09 17:21:21 +0300
  * remove dead code
* [Revision #7980364804](https://github.com/MariaDB/server/commit/7980364804)\
  2018-04-09 23:09:03 +0300
  * Deb: Fix commit c0f5addecb - also rename .install file
* Merge [Revision #0c8d6fd66c](https://github.com/MariaDB/server/commit/0c8d6fd66c) 2018-04-09 11:02:24 +0300 - [MDEV-15364](https://jira.mariadb.org/browse/MDEV-15364) FOREIGN CASCADE operations in system versioned referenced tables
* [Revision #7477b97e91](https://github.com/MariaDB/server/commit/7477b97e91)\
  2018-04-06 17:38:14 +0300
  * rename "where" to "row\_end\_data"
* [Revision #e41ae769c1](https://github.com/MariaDB/server/commit/e41ae769c1)\
  2018-04-06 17:20:45 +0300
  * use dedicated heap for upd\_node\_t::historical\_row and corresponding stuff to make its lifetime as short as possible
* [Revision #19a182b1ea](https://github.com/MariaDB/server/commit/19a182b1ea)\
  2018-03-19 17:25:58 +0300
  * [MDEV-15364](https://jira.mariadb.org/browse/MDEV-15364) FOREIGN CASCADE operations in system versioned referenced tables
* [Revision #fd73c6dda4](https://github.com/MariaDB/server/commit/fd73c6dda4)\
  2018-02-22 19:14:58 +0300
  * Vers IB: Mark unversioned fields in system versioning tables
* [Revision #0cf97ad5b9](https://github.com/MariaDB/server/commit/0cf97ad5b9)\
  2018-01-13 00:19:16 +0300
  * IB: CASCADE operation for DELETE
* [Revision #5a9e7bc6fe](https://github.com/MariaDB/server/commit/5a9e7bc6fe)\
  2018-04-09 09:39:58 +0300
  * [MDEV-13603](https://jira.mariadb.org/browse/MDEV-13603) innodb\_fast\_shutdown=0 may fail to purge all history
* [Revision #df44e75b42](https://github.com/MariaDB/server/commit/df44e75b42)\
  2018-04-08 18:11:49 +0300
  * Minor clean-up of purge code
* [Revision #0f6186c550](https://github.com/MariaDB/server/commit/0f6186c550)\
  2018-04-08 12:09:22 +0300
  * Make my\_atomic\_\*lint type-safe
* [Revision #8beeeddd83](https://github.com/MariaDB/server/commit/8beeeddd83)\
  2018-04-08 17:57:16 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266) fixup: Fix bug in row\_ins\_sec\_index\_entry()
* [Revision #c0f5addecb](https://github.com/MariaDB/server/commit/c0f5addecb)\
  2018-01-12 20:39:56 +0000
  * Deb: Remove versioning of MariaDB Backup and depend on client
* [Revision #1730ac5c4a](https://github.com/MariaDB/server/commit/1730ac5c4a)\
  2018-04-06 18:54:35 +0300
  * [MDEV-15348](https://jira.mariadb.org/browse/MDEV-15348) Failure to load CREATE SEQUENCE...ROW\_FORMAT=REDUNDANT
* [Revision #8692973031](https://github.com/MariaDB/server/commit/8692973031)\
  2018-04-06 13:15:40 +0300
  * Fixed wrong argument to my\_snprintf()
* [Revision #e27bfeca6a](https://github.com/MariaDB/server/commit/e27bfeca6a)\
  2018-04-06 12:31:13 +0300
  * Added test case for [MDEV-15742](https://jira.mariadb.org/browse/MDEV-15742) to prove that it works
* [Revision #a1a966fc0e](https://github.com/MariaDB/server/commit/a1a966fc0e)\
  2018-04-05 21:27:33 +0400
  * Cleanup: renaming methods make\_field(Send\_field\*) to make\_send\_field(..)
* [Revision #d8da97b09a](https://github.com/MariaDB/server/commit/d8da97b09a)\
  2018-04-05 15:16:20 +0300
  * [MDEV-14762](https://jira.mariadb.org/browse/MDEV-14762) Server crashes in MDL\_ticket::has\_stronger\_or\_equal\_type upon inserting into temporary sequence
* [Revision #3dd01669b4](https://github.com/MariaDB/server/commit/3dd01669b4)\
  2018-02-24 12:42:13 -0500
  * Misc. typos
* [Revision #7c68930031](https://github.com/MariaDB/server/commit/7c68930031)\
  2018-04-05 13:53:46 +0300
  * Fix compiler warnings in connect
* [Revision #1d7b4c2689](https://github.com/MariaDB/server/commit/1d7b4c2689)\
  2018-04-05 13:50:12 +0300
  * [MDEV-15738](https://jira.mariadb.org/browse/MDEV-15738) Server crashes in my\_strcasecmp\_utf8 on query from I\_S with UNION executed as PS
* [Revision #30f692f016](https://github.com/MariaDB/server/commit/30f692f016)\
  2018-04-01 12:30:50 +0300
  * Deb: Make AWS key management plugin a special plugin not in Linux distros
* [Revision #c720a1f8b8](https://github.com/MariaDB/server/commit/c720a1f8b8)\
  2018-04-01 12:54:10 +0300
  * Deb: Build RocksDB only on 64-bit and small endian architectures
* [Revision #e88e967a3d](https://github.com/MariaDB/server/commit/e88e967a3d)\
  2018-04-01 12:01:42 +0300
  * Deb: Exclude libnuma-dev as build-dep on armhf where is does not exist
* [Revision #ec53e031bb](https://github.com/MariaDB/server/commit/ec53e031bb)\
  2018-03-31 22:35:51 +0300
  * Deb: Bump epoch to supercede 1:10.1.29-6 in Debian
* Merge [Revision #2b0c6b7aa1](https://github.com/MariaDB/server/commit/2b0c6b7aa1) 2018-04-04 11:34:20 -0700 - [MDEV-7914](https://jira.mariadb.org/browse/MDEV-7914): spider/bg.ha, spider/bg.ha\_part crash server sporadically in buildbot
* [Revision #eabfadce5d](https://github.com/MariaDB/server/commit/eabfadce5d)\
  2018-04-02 15:25:08 -0700
  * [MDEV-7914](https://jira.mariadb.org/browse/MDEV-7914): spider/bg.ha, spider/bg.ha\_part crash server sporadically in buildbot
* [Revision #7c8c9a8bfa](https://github.com/MariaDB/server/commit/7c8c9a8bfa)\
  2018-04-04 19:04:14 +0530
  * [MDEV-15241](https://jira.mariadb.org/browse/MDEV-15241): make SIGNAL maximum MESSAGE\_TEXT length a larger value
* [Revision #e6a9ce2759](https://github.com/MariaDB/server/commit/e6a9ce2759)\
  2018-03-30 16:16:27 +0400
  * [MDEV-15773](https://jira.mariadb.org/browse/MDEV-15773) - Simplified away trx\_sys\_t::m\_views
* [Revision #3d5f7ad23a](https://github.com/MariaDB/server/commit/3d5f7ad23a)\
  2018-03-30 15:10:40 +0400
  * [MDEV-15773](https://jira.mariadb.org/browse/MDEV-15773) - Simplified away trx\_free\_for\_(mysql|background)
* [Revision #0993d6b81b](https://github.com/MariaDB/server/commit/0993d6b81b)\
  2018-03-30 00:33:58 +0400
  * [MDEV-15773](https://jira.mariadb.org/browse/MDEV-15773) - trx\_sys.mysql\_trx\_list -> trx\_sys.trx\_list
* [Revision #061c767cce](https://github.com/MariaDB/server/commit/061c767cce)\
  2018-03-29 23:09:16 +0400
  * [MDEV-15773](https://jira.mariadb.org/browse/MDEV-15773) - Simplified away trx\_t::in\_mysql\_trx\_list
* [Revision #d6d58836bb](https://github.com/MariaDB/server/commit/d6d58836bb)\
  2018-03-29 22:38:26 +0400
  * [MDEV-15773](https://jira.mariadb.org/browse/MDEV-15773) - trx\_allocate\_for\_background() -> trx\_create()
* Merge [Revision #a5da1c64f8](https://github.com/MariaDB/server/commit/a5da1c64f8) 2018-04-04 08:24:57 +0300 - Merge 10.2 into 10.3
* [Revision #bc2501453c](https://github.com/MariaDB/server/commit/bc2501453c)\
  2018-04-03 16:58:35 +0300
  * Remove an unused variable
* [Revision #3c21eccb8c](https://github.com/MariaDB/server/commit/3c21eccb8c)\
  2018-04-03 15:58:13 +0300
  * [MDEV-15764](https://jira.mariadb.org/browse/MDEV-15764) InnoDB may write uninitialized garbage to redo log
* [Revision #d9c5a46678](https://github.com/MariaDB/server/commit/d9c5a46678)\
  2018-04-03 16:43:36 +0530
  * [MDEV-15737](https://jira.mariadb.org/browse/MDEV-15737) assertion in mariadb-backup.exe!recv\_calc\_lsn\_on\_data\_add()
* [Revision #6223f1dd98](https://github.com/MariaDB/server/commit/6223f1dd98)\
  2018-03-25 22:12:38 +0200
  * [MDEV-15579](https://jira.mariadb.org/browse/MDEV-15579) Crash in Item\_field::used\_tables() called by Item::derived\_field\_transformer\_for\_having
* [Revision #27c24808f7](https://github.com/MariaDB/server/commit/27c24808f7)\
  2018-03-29 22:13:01 +0000
  * [MDEV-15636](https://jira.mariadb.org/browse/MDEV-15636) mariadb-backup --lock-ddl-per-table hangs if ALTER table is running concurrently.
* [Revision #a1d68faa38](https://github.com/MariaDB/server/commit/a1d68faa38)\
  2018-03-29 21:41:05 +0000
  * CMake : Move INNODB\_DISALLOW\_WRITES from top-level CMakeLists.txt to innodb
* [Revision #12ed50cc8d](https://github.com/MariaDB/server/commit/12ed50cc8d)\
  2018-04-04 08:21:53 +0300
  * [MDEV-15767](https://jira.mariadb.org/browse/MDEV-15767) innodb.101\_compatibility fails
* [Revision #b7ea563491](https://github.com/MariaDB/server/commit/b7ea563491)\
  2018-04-03 20:06:57 +0400
  * Cleanup in the system variable parsing code
* [Revision #94ecd2314d](https://github.com/MariaDB/server/commit/94ecd2314d)\
  2018-03-30 11:23:28 +0200
  * [MDEV-15739](https://jira.mariadb.org/browse/MDEV-15739) sql\_mode=ORACLE: Make LPAD and RPAD return NULL instead of empty string
* [Revision #1eee986e0c](https://github.com/MariaDB/server/commit/1eee986e0c)\
  2018-04-02 19:12:12 -0700
  * [MDEV-10991](https://jira.mariadb.org/browse/MDEV-10991): Server crashes in spider\_udf\_direct\_sql\_create\_conn - tests in spider/oracle\* suites crash the server
* [Revision #131ed6c273](https://github.com/MariaDB/server/commit/131ed6c273)\
  2018-04-02 22:49:32 +0200
  * [MDEV-15743](https://jira.mariadb.org/browse/MDEV-15743) Avoid a PFS warning by shortening key name for proxy protocol rwlock
* [Revision #342d3df6b1](https://github.com/MariaDB/server/commit/342d3df6b1)\
  2018-04-02 22:36:38 +0400
  * Cleanup: removing duplicate code, adding "const", etc
* [Revision #443b9a418c](https://github.com/MariaDB/server/commit/443b9a418c)\
  2018-03-21 13:54:15 +0400
  * [MDEV-14929](https://jira.mariadb.org/browse/MDEV-14929) - AddressSanitizer: memcpy-param-overlap in Field\_longstr::compress
* [Revision #69efa1343a](https://github.com/MariaDB/server/commit/69efa1343a)\
  2018-04-02 12:40:40 +0300
  * Fixed valgrind warning in DBUG\_PRINT as thd->stmt\_lex is not initalized
* [Revision #7d2e283562](https://github.com/MariaDB/server/commit/7d2e283562)\
  2018-04-02 12:40:02 +0300
  * Fix for [MDEV-14831](https://jira.mariadb.org/browse/MDEV-14831)
* [Revision #19bb7fdcd6](https://github.com/MariaDB/server/commit/19bb7fdcd6)\
  2018-03-27 20:10:17 +0000
  * [MDEV-15694](https://jira.mariadb.org/browse/MDEV-15694) Windows : use GetSystemTimePreciseAsFileTime if available for high resolution time
* [Revision #04bac13b30](https://github.com/MariaDB/server/commit/04bac13b30)\
  2018-03-30 21:36:56 +0300
  * Revert "[MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Remove lookups when dropping indexes"
* Merge [Revision #e895041ba9](https://github.com/MariaDB/server/commit/e895041ba9) 2018-03-30 18:27:02 +0300 - Merge 10.2 into 10.3
* [Revision #55f4e4800b](https://github.com/MariaDB/server/commit/55f4e4800b)\
  2018-03-29 22:00:07 +0300
  * [MDEV-15325](https://jira.mariadb.org/browse/MDEV-15325) fixup: Disable test for --embedded
* [Revision #402c7584a8](https://github.com/MariaDB/server/commit/402c7584a8)\
  2018-03-23 12:58:11 +1100
  * [MDEV-13785](https://jira.mariadb.org/browse/MDEV-13785): move defination HAVE\_LARGE\_PAGES -> HAVE\_LINUX\_LARGE\_PAGES
* [Revision #d266036292](https://github.com/MariaDB/server/commit/d266036292)\
  2018-03-30 18:23:09 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Remove lookups when dropping indexes
* [Revision #556a9202ce](https://github.com/MariaDB/server/commit/556a9202ce)\
  2018-03-30 14:29:23 +0400
  * Cleanup: moving timestamp\_to\_TIME() as a method to THD
* [Revision #17bbab5fb0](https://github.com/MariaDB/server/commit/17bbab5fb0)\
  2018-03-29 09:05:24 +0200
  * cleanup: remove get\_datetime\_value()
* [Revision #c43a0e0a77](https://github.com/MariaDB/server/commit/c43a0e0a77)\
  2018-03-28 20:52:06 +0200
  * bugfix: Item\_cache\_temporal::convert\_to\_basic\_const\_item assumed DATETIME
* [Revision #7601331140](https://github.com/MariaDB/server/commit/7601331140)\
  2018-03-28 20:36:36 +0200
  * bugfix: Item\_cache\_temporal::get\_date() didn't set null\_value
* [Revision #7a903784b7](https://github.com/MariaDB/server/commit/7a903784b7)\
  2018-03-28 20:16:13 +0200
  * cleanup: Item\_func\_case
* [Revision #4c77ef36c6](https://github.com/MariaDB/server/commit/4c77ef36c6)\
  2018-03-28 19:19:17 +0200
  * compilation w/o partitioning
* [Revision #ae6355f56e](https://github.com/MariaDB/server/commit/ae6355f56e)\
  2018-03-30 08:55:42 +0300
  * Fix bogus error: Failed to find tablespace
* [Revision #cbc45d2914](https://github.com/MariaDB/server/commit/cbc45d2914)\
  2018-03-30 01:25:48 +0300
  * [MDEV-14592](https://jira.mariadb.org/browse/MDEV-14592): Custom Aggregates Usage Status Variable
* [Revision #87ee85634c](https://github.com/MariaDB/server/commit/87ee85634c)\
  2018-03-29 22:07:17 +0300
  * Fix a WITH\_WSREP=OFF warning
* [Revision #4cad42392a](https://github.com/MariaDB/server/commit/4cad42392a)\
  2018-03-27 16:31:10 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Change dict\_table\_t::space to fil\_space\_t\*
* [Revision #c02c329a8e](https://github.com/MariaDB/server/commit/c02c329a8e)\
  2018-03-27 13:56:39 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Skip a lookup when checking free space
* [Revision #330ecb906d](https://github.com/MariaDB/server/commit/330ecb906d)\
  2018-03-27 11:49:57 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): fsp\_flags\_try\_adjust(): Remove lookup
* [Revision #05863142ad](https://github.com/MariaDB/server/commit/05863142ad)\
  2018-03-27 11:34:43 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Remove fil\_system\_t::named\_spaces
* [Revision #9043bec954](https://github.com/MariaDB/server/commit/9043bec954)\
  2018-03-26 17:23:47 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Make trx\_rseg\_t::space a pointer
* [Revision #39ed074317](https://github.com/MariaDB/server/commit/39ed074317)\
  2018-03-26 16:38:43 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Remove trx\_undo\_t::space
* [Revision #5dd5b6cadc](https://github.com/MariaDB/server/commit/5dd5b6cadc)\
  2018-03-26 16:13:17 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Clean up btr\_search\_drop\_page\_hash\_when\_freed()
* [Revision #e2bf76cb32](https://github.com/MariaDB/server/commit/e2bf76cb32)\
  2018-03-26 15:47:54 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Cleanup DISCARD TABLESPACE
* [Revision #f8d1bd011d](https://github.com/MariaDB/server/commit/f8d1bd011d)\
  2018-03-26 14:54:12 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Cleanup TRUNCATE
* [Revision #f2a581e6c7](https://github.com/MariaDB/server/commit/f2a581e6c7)\
  2018-03-26 10:42:07 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Clean up recv\_recover\_page()
* [Revision #332e805e2c](https://github.com/MariaDB/server/commit/332e805e2c)\
  2018-03-26 10:04:28 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Refactor trx\_rseg\_header\_create()
* [Revision #428e02895b](https://github.com/MariaDB/server/commit/428e02895b)\
  2018-03-23 17:25:56 +0200
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Remove dict\_index\_t::table\_name
* [Revision #604fea1ad6](https://github.com/MariaDB/server/commit/604fea1ad6)\
  2018-03-22 19:40:38 +0200
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Remove dict\_index\_t::space
* [Revision #e7980f9cee](https://github.com/MariaDB/server/commit/e7980f9cee)\
  2018-03-22 15:30:54 +0200
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Add dict\_index\_t::set\_modified(mtr)
* [Revision #39cbba19d7](https://github.com/MariaDB/server/commit/39cbba19d7)\
  2018-03-22 14:56:24 +0200
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): dict\_recreate\_index\_tree(): Keep the fil\_space\_t
* [Revision #c577192d6c](https://github.com/MariaDB/server/commit/c577192d6c)\
  2018-03-22 14:17:43 +0200
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): fsp\_flags\_try\_adjust(): Remove a lookup
* [Revision #2ac8b1a907](https://github.com/MariaDB/server/commit/2ac8b1a907)\
  2018-03-28 09:29:14 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Add fil\_system.sys\_space, temp\_space
* [Revision #600c85e85a](https://github.com/MariaDB/server/commit/600c85e85a)\
  2018-03-28 09:00:06 +0300
  * Allocate the singleton fil\_system statically
* [Revision #1f0f7d5907](https://github.com/MariaDB/server/commit/1f0f7d5907)\
  2018-03-28 11:11:59 +0300
  * Remove dict\_build\_tablespace\_for\_table()
* [Revision #60ef478c2e](https://github.com/MariaDB/server/commit/60ef478c2e)\
  2018-03-23 11:19:27 +0200
  * Remove an unnecessary global declaration
* [Revision #d177a0ed14](https://github.com/MariaDB/server/commit/d177a0ed14)\
  2018-03-28 10:38:20 +0300
  * Remove unused function fil\_space\_get\_id\_by\_name()
* Merge [Revision #980dd09be6](https://github.com/MariaDB/server/commit/980dd09be6) 2018-03-29 17:03:34 +0300 - Merge 10.2 into 10.3
* [Revision #014dfe473a](https://github.com/MariaDB/server/commit/014dfe473a)\
  2018-03-29 16:58:59 +0300
  * [MDEV-15719](https://jira.mariadb.org/browse/MDEV-15719): Adjust a test case
* [Revision #3eb73bf630](https://github.com/MariaDB/server/commit/3eb73bf630)\
  2018-03-24 08:38:08 +0200
  * Remove unnecessary SysTablespace references
* [Revision #622d21e2b8](https://github.com/MariaDB/server/commit/622d21e2b8)\
  2018-03-27 12:25:30 +0300
  * row\_drop\_table\_for\_mysql(): Use a constant string
* [Revision #b922741074](https://github.com/MariaDB/server/commit/b922741074)\
  2018-03-29 13:59:21 +0300
  * [MDEV-15472](https://jira.mariadb.org/browse/MDEV-15472): Assertion \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failure
* [Revision #adaee46a90](https://github.com/MariaDB/server/commit/adaee46a90)\
  2018-03-29 13:22:59 +0300
  * [MDEV-15682](https://jira.mariadb.org/browse/MDEV-15682) mariadb-backup.unsupported\_redo fails in buildbot with wrong result code
* [Revision #6cccef21a6](https://github.com/MariaDB/server/commit/6cccef21a6)\
  2018-03-29 13:22:16 +0300
  * [MDEV-15720](https://jira.mariadb.org/browse/MDEV-15720) ib\_buffer\_pool unnecessarily includes the temporary tablespace
* [Revision #4d9969c216](https://github.com/MariaDB/server/commit/4d9969c216)\
  2018-03-29 12:55:24 +0300
  * [MDEV-15719](https://jira.mariadb.org/browse/MDEV-15719) ALTER TABLE…ALGORITHM=INPLACE is unnecessarily refused due to innodb\_force\_recovery
* [Revision #0d2fffb612](https://github.com/MariaDB/server/commit/0d2fffb612)\
  2018-03-29 11:08:32 +0300
  * [MDEV-15686](https://jira.mariadb.org/browse/MDEV-15686): Loading MyRocks plugin back after it has been unloaded causes a crash
* [Revision #d18a66147c](https://github.com/MariaDB/server/commit/d18a66147c)\
  2018-03-28 20:40:09 +0300
  * recv\_validate\_tablespace(): Fix -Wmissing-fallthrough
* [Revision #5beddfa08c](https://github.com/MariaDB/server/commit/5beddfa08c)\
  2018-03-28 20:39:57 +0300
  * fil\_node\_open\_file(): Add a missing space to message
* [Revision #011586c04d](https://github.com/MariaDB/server/commit/011586c04d)\
  2018-03-27 17:21:22 +0300
  * [MDEV-15686](https://jira.mariadb.org/browse/MDEV-15686): Loading MyRocks plugin back after it has been unloaded causes a crash
* [Revision #907aae2502](https://github.com/MariaDB/server/commit/907aae2502)\
  2018-03-28 14:28:58 +0300
  * [MDEV-15708](https://jira.mariadb.org/browse/MDEV-15708): rocksdb.mariadb\_plugin fails on winx64, Cannot enable tc-log at run-time
* [Revision #3b119d9d30](https://github.com/MariaDB/server/commit/3b119d9d30)\
  2018-03-28 13:14:24 +0300
  * [MDEV-11531](https://jira.mariadb.org/browse/MDEV-11531): encryption.innodb\_lotoftables failed in buildbot
* [Revision #4277c173a9](https://github.com/MariaDB/server/commit/4277c173a9)\
  2018-03-29 14:16:35 +0300
  * [MDEV-15149](https://jira.mariadb.org/browse/MDEV-15149) Assert upon concurrent creating / querying sequences
* [Revision #cd93eeeb1d](https://github.com/MariaDB/server/commit/cd93eeeb1d)\
  2018-03-29 12:25:17 +0300
  * [MDEV-15149](https://jira.mariadb.org/browse/MDEV-15149) Assert upon concurrent creating / querying sequences
* [Revision #e2664ee836](https://github.com/MariaDB/server/commit/e2664ee836)\
  2018-03-26 17:22:41 +0300
  * [MDEV-14275](https://jira.mariadb.org/browse/MDEV-14275) Improving memory utilization for information schema
* [Revision #33fa6abd02](https://github.com/MariaDB/server/commit/33fa6abd02)\
  2018-03-26 17:23:21 +0300
  * Ensure that map->mutex is reset in my\_bitmap\_init
* [Revision #75dd94c7ce](https://github.com/MariaDB/server/commit/75dd94c7ce)\
  2018-03-25 14:05:30 +0300
  * Fixed compiler warnings
* [Revision #d572c19f22](https://github.com/MariaDB/server/commit/d572c19f22)\
  2018-03-15 12:31:59 +0200
  * Added flush tables to acl\_load\_mutex-5170.test
* [Revision #410d093089](https://github.com/MariaDB/server/commit/410d093089)\
  2018-03-23 18:58:06 +0200
  * Move extra/rpl\_tests/table\_index\_statistics to suite/innodb
* [Revision #39018f2a5a](https://github.com/MariaDB/server/commit/39018f2a5a)\
  2018-03-09 15:14:33 +0200
  * Move mysql-test-run/extra/rpl\_tests to suite/rpl/include
* [Revision #108ed22854](https://github.com/MariaDB/server/commit/108ed22854)\
  2018-03-09 15:05:22 +0200
  * Move mysql-test-run/extra/binlog to suite/binlog/include
* [Revision #a7abddeffa](https://github.com/MariaDB/server/commit/a7abddeffa)\
  2018-03-09 14:05:35 +0200
  * Create 'main' test directory and move 't' and 'r' there
* [Revision #ab1941266c](https://github.com/MariaDB/server/commit/ab1941266c)\
  2018-02-19 11:23:20 +0200
  * Move alter partition flags to alter\_info->partition\_flags
* [Revision #2dbeebdb16](https://github.com/MariaDB/server/commit/2dbeebdb16)\
  2018-02-16 10:56:03 +0200
  * Changed static const in Alter\_info and Alter\_online\_info to defines
* [Revision #0631f20ff7](https://github.com/MariaDB/server/commit/0631f20ff7)\
  2018-02-14 03:27:54 +0200
  * Fixed some DBUG\_PRINT to use %p properly
* [Revision #c3f37c070c](https://github.com/MariaDB/server/commit/c3f37c070c)\
  2018-02-14 02:30:11 +0200
  * Fixed alter online table for Aria tables
* [Revision #209375fdd0](https://github.com/MariaDB/server/commit/209375fdd0)\
  2018-03-27 09:08:30 +0200
  * [MDEV-15664](https://jira.mariadb.org/browse/MDEV-15664) : sql\_mode=ORACLE: Make TRIM return NULL instead of empty string
* [Revision #4faf34ad63](https://github.com/MariaDB/server/commit/4faf34ad63)\
  2018-03-26 17:28:21 +0400
  * Clean-up trx\_sys.mutex misuse
* [Revision #b36da48ad3](https://github.com/MariaDB/server/commit/b36da48ad3)\
  2018-03-27 16:05:50 +0400
  * [MDEV-15612](https://jira.mariadb.org/browse/MDEV-15612) - Latching violation in trx\_roll\_must\_shutdown
* [Revision #2a13b3db50](https://github.com/MariaDB/server/commit/2a13b3db50)\
  2018-03-29 11:26:37 +0400
  * [MDEV-15714](https://jira.mariadb.org/browse/MDEV-15714) Remove the use of STRING\_ITEM from the parser
* [Revision #b81a403e69](https://github.com/MariaDB/server/commit/b81a403e69)\
  2018-03-27 23:17:25 +0300
  * lock\_rec\_enqueue\_waiting(): Fix diagnostics
* [Revision #1924594b80](https://github.com/MariaDB/server/commit/1924594b80)\
  2018-03-27 22:57:04 +0300
  * Minor (mainly non-functional) cleanup
* Merge [Revision #b1818dccf7](https://github.com/MariaDB/server/commit/b1818dccf7) 2018-03-28 17:06:27 +0200 - Merge branch '10.2' into 10.3
* [Revision #aafb9d44d6](https://github.com/MariaDB/server/commit/aafb9d44d6)\
  2018-03-27 13:31:07 -0400
  * bump the VERSION
* [Revision #73af8af094](https://github.com/MariaDB/server/commit/73af8af094)\
  2018-03-27 13:47:56 +0530
  * [MDEV-15325](https://jira.mariadb.org/browse/MDEV-15325) Incomplete validation of missing tablespace during recovery
* [Revision #60438451c3](https://github.com/MariaDB/server/commit/60438451c3)\
  2018-03-26 21:22:40 +0300
  * [MDEV-14843](https://jira.mariadb.org/browse/MDEV-14843): Assertion \`s\_tx\_list.size() == 0' failed in myrocks::Rdb\_transaction::term\_mutex
* [Revision #c346029958](https://github.com/MariaDB/server/commit/c346029958)\
  2018-03-28 11:26:02 +0400
  * [MDEV-15702](https://jira.mariadb.org/browse/MDEV-15702) Remove the use of STRING\_ITEM from Item\_func\_date\_format::fix\_length\_and\_dec() Implementing the task according to the description. Additionally, implementing Item\_func\_date\_format::check\_arguments().
* [Revision #068450a382](https://github.com/MariaDB/server/commit/068450a382)\
  2018-03-27 15:44:40 +0400
  * [MDEV-15689](https://jira.mariadb.org/browse/MDEV-15689) Fix Item\_func\_set\_collation to pass the collation using CHARSET\_INFO instead of Item
* [Revision #0f26f71b49](https://github.com/MariaDB/server/commit/0f26f71b49)\
  2018-03-27 13:10:53 +0400
  * [MDEV-15316](https://jira.mariadb.org/browse/MDEV-15316) Assertion \`(thd->lex)->var\_list.is\_empty()' failed in MYSQLparse
* [Revision #902ace0968](https://github.com/MariaDB/server/commit/902ace0968)\
  2018-03-23 14:23:48 +0400
  * [MDEV-15620](https://jira.mariadb.org/browse/MDEV-15620) Crash when using "SET @@NEW.a=expr" inside a trigger
* [Revision #ad647cc84e](https://github.com/MariaDB/server/commit/ad647cc84e)\
  2018-03-25 00:15:11 +0400
  * [MDEV-15561](https://jira.mariadb.org/browse/MDEV-15561) json\_extract returns NULL with numbers in scientific notation.
* [Revision #843b414891](https://github.com/MariaDB/server/commit/843b414891)\
  2018-03-24 10:54:07 +0100
  * [MDEV-15501](https://jira.mariadb.org/browse/MDEV-15501) postfix - Adjust test results
* [Revision #96ecf3ff23](https://github.com/MariaDB/server/commit/96ecf3ff23)\
  2018-03-21 18:09:52 +0000
  * [MDEV-15501](https://jira.mariadb.org/browse/MDEV-15501) : Make `proxy_protocol_networks` variable read-write.
* Merge [Revision #865cec928a](https://github.com/MariaDB/server/commit/865cec928a) 2018-03-21 16:29:30 +0200 - [MDEV-15505](https://jira.mariadb.org/browse/MDEV-15505) Fix wsrep XID storage byte order
* [Revision #33aad1d273](https://github.com/MariaDB/server/commit/33aad1d273)\
  2018-03-21 12:02:09 +0200
  * [MDEV-15505](https://jira.mariadb.org/browse/MDEV-15505) Fixes to compilation without -DWITH\_WSREP:BOOL=ON
* [Revision #b125ae0a84](https://github.com/MariaDB/server/commit/b125ae0a84)\
  2018-03-12 12:39:30 +0200
  * [MDEV-15505](https://jira.mariadb.org/browse/MDEV-15505) New wsrep XID format for backwards compatibility
* [Revision #dd74b94823](https://github.com/MariaDB/server/commit/dd74b94823)\
  2018-03-07 18:40:15 +0200
  * [MDEV-15505](https://jira.mariadb.org/browse/MDEV-15505) Fix wsrep XID seqno byte order
* [Revision #4359c6b480](https://github.com/MariaDB/server/commit/4359c6b480)\
  2018-03-20 15:21:22 +0400
  * A cleanup for [MDEV-15597](https://jira.mariadb.org/browse/MDEV-15597): fixing compilation failure on 32-bit Windows
* [Revision #e263530bea](https://github.com/MariaDB/server/commit/e263530bea)\
  2018-03-20 13:02:44 +0400
  * [MDEV-15597](https://jira.mariadb.org/browse/MDEV-15597) Add class Load\_data\_outvar and avoid using Item::STRING\_ITEM for Item\_user\_var\_as\_out\_param detection
* [Revision #85ddd9e8ce](https://github.com/MariaDB/server/commit/85ddd9e8ce)\
  2018-03-17 12:56:23 +0200
  * Revert pull request #640 from grooverdan/10.3-[MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743)-wsrep\_sst\_common-close-fds
* Merge [Revision #c231a228ca](https://github.com/MariaDB/server/commit/c231a228ca) 2018-03-16 09:09:02 +0200 - Pull request #660: Simplify os\_file\_create\_tmpfile()
* [Revision #7bb661cd40](https://github.com/MariaDB/server/commit/7bb661cd40)\
  2018-03-15 13:47:28 +1100
  * innodb: os\_file\_create\_tmpfile always called with NULL -> simplify
* [Revision #9472f0f4a4](https://github.com/MariaDB/server/commit/9472f0f4a4)\
  2018-03-15 23:29:48 +0400
  * Adding "const" qualifier into a few methods and parameters in the LOAD code
* Merge [Revision #d509981498](https://github.com/MariaDB/server/commit/d509981498) 2018-03-15 13:39:26 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* Merge [Revision #42433a2dbc](https://github.com/MariaDB/server/commit/42433a2dbc) 2018-03-13 14:22:28 +0400 - Merge pull request #652 from halfspawn/bb-10.2-ext
* [Revision #3e6893e29a](https://github.com/MariaDB/server/commit/3e6893e29a)\
  2018-03-13 10:34:28 +0100
  * [MDEV-10574](https://jira.mariadb.org/browse/MDEV-10574) / SUBSTR - sql\_mode=Oracle: return null instead of empty string
* Merge [Revision #1a0b573b2b](https://github.com/MariaDB/server/commit/1a0b573b2b) 2018-03-15 08:44:54 +0200 - Merge pull request #640 from grooverdan/10.3-[MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743)-wsrep\_sst\_common-close-fds
* [Revision #04ed70fa55](https://github.com/MariaDB/server/commit/04ed70fa55)\
  2018-03-02 20:16:16 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): wsrep\_sst\_common close FDs > 2
* Merge [Revision #f66a315910](https://github.com/MariaDB/server/commit/f66a315910) 2018-03-15 08:38:05 +0200 - Merge pull request #638 from grooverdan/10.3-[MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743)-fopen\_o\_cloexec
* [Revision #fafec1a9cc](https://github.com/MariaDB/server/commit/fafec1a9cc)\
  2018-03-14 13:31:28 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): where O\_CLOEXEC is available, use for innodb buf\_dump
* [Revision #0a63c91ab0](https://github.com/MariaDB/server/commit/0a63c91ab0)\
  2018-03-02 10:16:46 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): fopen mode e (glibc only) to prevent galera SST scripts accessing server files
* Merge [Revision #7fb03d7abf](https://github.com/MariaDB/server/commit/7fb03d7abf) 2018-03-13 08:15:06 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #1c4b6afbaa](https://github.com/MariaDB/server/commit/1c4b6afbaa) 2018-03-13 08:11:54 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #036b9dc9a1](https://github.com/MariaDB/server/commit/036b9dc9a1)\
  2018-03-12 22:08:08 +0200
  * After-merge fix
* Merge [Revision #e0792e7603](https://github.com/MariaDB/server/commit/e0792e7603) 2018-03-12 14:48:53 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #09c5c335e3](https://github.com/MariaDB/server/commit/09c5c335e3)\
  2018-03-09 20:33:41 +0200
  * Follow-up to [MDEV-13690](https://jira.mariadb.org/browse/MDEV-13690): Remove unused globals
* [Revision #6ec3de5d2d](https://github.com/MariaDB/server/commit/6ec3de5d2d)\
  2018-03-07 19:52:00 +0400
  * [MDEV-15497](https://jira.mariadb.org/browse/MDEV-15497) Wrong empty value in a GEOMETRY column on LOAD DATA
* [Revision #2ef2863c30](https://github.com/MariaDB/server/commit/2ef2863c30)\
  2018-03-02 10:09:55 +1100
  * my\_fdopen: list all args in comment
* [Revision #08fa321877](https://github.com/MariaDB/server/commit/08fa321877)\
  2018-03-06 09:20:14 +0200
  * [MDEV-15474](https://jira.mariadb.org/browse/MDEV-15474) Update server.cnf section to mariadb-10.3
* [Revision #8f361a83cc](https://github.com/MariaDB/server/commit/8f361a83cc)\
  2018-03-06 23:08:45 +0200
  * ReadView::snapshot(): Define inline
* [Revision #93d495f365](https://github.com/MariaDB/server/commit/93d495f365)\
  2018-03-06 23:33:35 +0200
  * [MDEV-15418](https://jira.mariadb.org/browse/MDEV-15418) innodb\_force\_recovery=5 displays bogus warnings
* [Revision #67f6d40bd9](https://github.com/MariaDB/server/commit/67f6d40bd9)\
  2018-03-06 23:29:38 +0200
  * [MDEV-15443](https://jira.mariadb.org/browse/MDEV-15443) Properly read wsrep XID and binlog position from rollback segment headers
* Merge [Revision #d70573564c](https://github.com/MariaDB/server/commit/d70573564c) 2018-03-02 12:09:41 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #88a9d4ab42](https://github.com/MariaDB/server/commit/88a9d4ab42)\
  2018-03-02 11:31:27 +0400
  * [MDEV-15444](https://jira.mariadb.org/browse/MDEV-15444) Querying I\_S.PARAMETERS can crash with a corrupted mysql.proc
* [Revision #4025cfaec0](https://github.com/MariaDB/server/commit/4025cfaec0)\
  2018-02-28 23:05:57 +0400
  * [MDEV-15416](https://jira.mariadb.org/browse/MDEV-15416) Crash when reading I\_S.PARAMETERS
* [Revision #5cf0662d76](https://github.com/MariaDB/server/commit/5cf0662d76)\
  2018-02-20 16:04:29 +0100
  * [MDEV-13749](https://jira.mariadb.org/browse/MDEV-13749): Server crashes in \_ma\_unique\_hash / JOIN\_CACHE::generate\_full\_extensions on INTERSECT
* [Revision #92993d92e4](https://github.com/MariaDB/server/commit/92993d92e4)\
  2018-02-28 09:29:30 -0500
  * bump the VERSION
* Merge [Revision #ab31335d66](https://github.com/MariaDB/server/commit/ab31335d66) 2018-02-27 15:49:42 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #5f7c764fe7](https://github.com/MariaDB/server/commit/5f7c764fe7)\
  2017-08-18 23:36:42 +0400
  * [MDEV-11952](https://jira.mariadb.org/browse/MDEV-11952) Oracle-style packages: stage#5

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
