# MariaDB 10.3.35 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download 10.3.35](https://mariadb.org/download/?tab=mariadb\&release=10.3.35\&product=mariadb)[Release Notes](../../old-releases/10.3/10.3.35.md)[Changelog](mariadb-10335-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 20 May 2022

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.35.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.44](../changelogs-mariadb-102-series/mariadb-10244-changelog.md)
* Merge [Revision #a0d4f0f306](https://github.com/MariaDB/server/commit/a0d4f0f306) 2022-05-18 01:23:47 +0200 - Merge branch '10.2' into 10.3
* [Revision #d388e7eb86](https://github.com/MariaDB/server/commit/d388e7eb86)\
  2022-05-17 11:04:04 +0200
  * [MDEV-28583](https://jira.mariadb.org/browse/MDEV-28583): Galera: binlogs disappear after rsync IST
* [Revision #b081ad8c65](https://github.com/MariaDB/server/commit/b081ad8c65)\
  2022-05-06 02:38:36 +0200
  * [MDEV-28423](https://jira.mariadb.org/browse/MDEV-28423): Galera IST is failing on Joiner node
* [Revision #107623c5c5](https://github.com/MariaDB/server/commit/107623c5c5)\
  2022-05-12 20:19:33 +0300
  * [MDEV-28552](https://jira.mariadb.org/browse/MDEV-28552) Assertion \`inited==RND' failed in handler::ha\_rnd\_end
* [Revision #8609254f4f](https://github.com/MariaDB/server/commit/8609254f4f)\
  2022-05-12 13:23:24 +0200
  * cleanup:have\_log\_bin.inc
* [Revision #74068dd2ac](https://github.com/MariaDB/server/commit/74068dd2ac)\
  2022-05-18 01:20:23 +0200
  * fix tests for embedded
* [Revision #c9b5a05341](https://github.com/MariaDB/server/commit/c9b5a05341)\
  2022-05-17 15:34:58 +0400
  * [MDEV-28588](https://jira.mariadb.org/browse/MDEV-28588) SIGSEGV in memmove\_avx\_unaligned\_erms, strmake\_root
* [Revision #3e564d468d](https://github.com/MariaDB/server/commit/3e564d468d)\
  2022-05-16 13:45:17 +0300
  * [MDEV-28541](https://jira.mariadb.org/browse/MDEV-28541) Unused counter Innodb\_encryption\_key\_rotation\_list\_length
* [Revision #4e1bf2bb23](https://github.com/MariaDB/server/commit/4e1bf2bb23)\
  2022-05-16 13:41:53 +0300
  * [MDEV-28537](https://jira.mariadb.org/browse/MDEV-28537) Unused or useless InnoDB counters num\_index\_pages\_written, num\_non\_index\_pages\_written
* [Revision #730eb1c4be](https://github.com/MariaDB/server/commit/730eb1c4be)\
  2022-05-14 20:19:05 +0300
  * Code cleanup in/around check\_interleaving\_with\_nj()
* [Revision #8c28b27f00](https://github.com/MariaDB/server/commit/8c28b27f00)\
  2022-05-13 21:32:49 +0900
  * [MDEV-28301](https://jira.mariadb.org/browse/MDEV-28301) Spider: Fix GCC warnings, comparing the result of pointer addition ... and NULL
* [Revision #480323f7d6](https://github.com/MariaDB/server/commit/480323f7d6)\
  2022-05-01 14:45:58 +0200
  * [MDEV-19161](https://jira.mariadb.org/browse/MDEV-19161): Let galera\_new\_cluster use "restart" instead of "start"
* [Revision #66d93a809c](https://github.com/MariaDB/server/commit/66d93a809c)\
  2022-05-06 08:42:16 +0300
  * [MDEV-19959](https://jira.mariadb.org/browse/MDEV-19959) : Galera test failure on galera\_binlog\_stmt\_autoinc
* [Revision #79660e59ee](https://github.com/MariaDB/server/commit/79660e59ee)\
  2022-05-08 13:00:35 +0200
  * can't use Item\_default\_value as a field if it's an expression OR a blob
* [Revision #e9a28940c5](https://github.com/MariaDB/server/commit/e9a28940c5)\
  2022-05-08 00:42:43 +0200
  * these tests need ipv6
* Merge [Revision #6f741eb6e4](https://github.com/MariaDB/server/commit/6f741eb6e4) 2022-05-07 11:48:15 +0200 - Merge branch '10.2' into 10.3
* [Revision #0db27eff27](https://github.com/MariaDB/server/commit/0db27eff27)\
  2022-05-07 08:28:19 +1000
  * [MDEV-27816](https://jira.mariadb.org/browse/MDEV-27816): Set sql\_mode before DROP IF EXISTS already (postfix)
* [Revision #221ced92aa](https://github.com/MariaDB/server/commit/221ced92aa)\
  2022-05-06 17:44:33 +1000
  * [MDEV-4875](https://jira.mariadb.org/browse/MDEV-4875) Can't restore a mysqldump if --add-drop-database meets general\_log
* [Revision #9fe3bc2aa8](https://github.com/MariaDB/server/commit/9fe3bc2aa8)\
  2022-04-29 10:10:02 +0200
  * [MDEV-27816](https://jira.mariadb.org/browse/MDEV-27816) Set sql\_mode before DROP IF EXISTS already
* [Revision #06562b84f6](https://github.com/MariaDB/server/commit/06562b84f6)\
  2022-04-22 09:54:08 +0300
  * [MDEV-28388](https://jira.mariadb.org/browse/MDEV-28388): As Travis is not used anymore remove configurations files
* [Revision #db47855eb7](https://github.com/MariaDB/server/commit/db47855eb7)\
  2022-04-26 10:36:41 +0300
  * [MDEV-12275](https://jira.mariadb.org/browse/MDEV-12275): Add switch '--silent' to SySV init upgrade
* [Revision #531935992a](https://github.com/MariaDB/server/commit/531935992a)\
  2022-05-02 12:22:57 +0200
  * test fixes for FreeBSD
* [Revision #2c381d8cf6](https://github.com/MariaDB/server/commit/2c381d8cf6)\
  2022-04-14 14:27:23 +0300
  * [MDEV-17843](https://jira.mariadb.org/browse/MDEV-17843) Assertion \`page\_rec\_is\_leaf(rec)' failed in lock\_rec\_queue\_validate upon SHOW ENGINE INNODB STATUS
* Merge [Revision #9614fde1aa](https://github.com/MariaDB/server/commit/9614fde1aa) 2022-05-03 10:59:54 +0200 - Merge branch '10.2' into 10.3
* [Revision #182b8a29e7](https://github.com/MariaDB/server/commit/182b8a29e7)\
  2022-04-29 17:36:48 +0300
  * [MDEV-20077](https://jira.mariadb.org/browse/MDEV-20077) compilation fix
* [Revision #ddc416c606](https://github.com/MariaDB/server/commit/ddc416c606)\
  2022-04-25 13:58:41 +0300
  * [MDEV-20077](https://jira.mariadb.org/browse/MDEV-20077) Warning on full history partition is delayed until next DML statement
* [Revision #ea2f09979f](https://github.com/MariaDB/server/commit/ea2f09979f)\
  2022-04-24 00:28:54 +0300
  * [MDEV-28271](https://jira.mariadb.org/browse/MDEV-28271) Assertion on TRUNCATE PARTITION for PARTITION BY SYSTEM\_TIME
* [Revision #add5137d84](https://github.com/MariaDB/server/commit/add5137d84)\
  2022-04-28 09:34:21 +0400
  * [MDEV-28429](https://jira.mariadb.org/browse/MDEV-28429) audit plugin report OOOOO.
* [Revision #0806592ac8](https://github.com/MariaDB/server/commit/0806592ac8)\
  2022-04-27 13:16:07 +0300
  * [MDEV-28422](https://jira.mariadb.org/browse/MDEV-28422) Page split breaks a gap lock
* [Revision #b208030ef5](https://github.com/MariaDB/server/commit/b208030ef5)\
  2022-04-25 14:14:02 +0300
  * [MDEV-11415](https://jira.mariadb.org/browse/MDEV-11415) merge fixup: Remove a redundant call
* [Revision #9286c9e647](https://github.com/MariaDB/server/commit/9286c9e647)\
  2022-04-22 15:49:37 +0300
  * [MDEV-28254](https://jira.mariadb.org/browse/MDEV-28254) Wrong position for row\_start, row\_end after adding column to implicit versioned table
* [Revision #88a9f13a90](https://github.com/MariaDB/server/commit/88a9f13a90)\
  2022-04-22 15:49:37 +0300
  * [MDEV-25546](https://jira.mariadb.org/browse/MDEV-25546) LIMIT partitioning does not respect ROLLBACK
* [Revision #4d11290065](https://github.com/MariaDB/server/commit/4d11290065)\
  2022-04-21 10:06:01 +0200
  * .gitignore
* Merge [Revision #6f6c74b0d1](https://github.com/MariaDB/server/commit/6f6c74b0d1) 2022-04-21 10:04:04 +0200 - Merge branch '10.2' into 10.3
* [Revision #4730314a70](https://github.com/MariaDB/server/commit/4730314a70)\
  2022-04-21 09:15:18 +0300
  * [MDEV-28369](https://jira.mariadb.org/browse/MDEV-28369) ibuf\_bitmap\_mutex is an unnecessary contention point
* [Revision #372b0e6355](https://github.com/MariaDB/server/commit/372b0e6355)\
  2022-04-13 18:06:33 +0530
  * [MDEV-20194](https://jira.mariadb.org/browse/MDEV-20194) Warnings inconsistently issued upon CHECK on table from older versions
* [Revision #84b135065c](https://github.com/MariaDB/server/commit/84b135065c)\
  2022-04-19 12:02:34 +0300
  * [MDEV-28314](https://jira.mariadb.org/browse/MDEV-28314) : The Galera cluster primary node goes into hang mode when innodb\_encryption\_threads is enabled
* [Revision #b3c3291f0b](https://github.com/MariaDB/server/commit/b3c3291f0b)\
  2022-04-19 10:29:21 +0300
  * [MDEV-24176](https://jira.mariadb.org/browse/MDEV-24176) fixup: GCC -Wmaybe-uninitialized
* [Revision #08c7ab404f](https://github.com/MariaDB/server/commit/08c7ab404f)\
  2022-04-18 12:44:27 +0300
  * [MDEV-24176](https://jira.mariadb.org/browse/MDEV-24176) Server crashes after insert in the table with virtual column generated using date\_format() and if()
* [Revision #c02ebf3510](https://github.com/MariaDB/server/commit/c02ebf3510)\
  2022-04-18 12:44:27 +0300
  * [MDEV-24176](https://jira.mariadb.org/browse/MDEV-24176) Preparations
* [Revision #7498978e6a](https://github.com/MariaDB/server/commit/7498978e6a)\
  2022-04-13 19:56:34 +0700
  * [MDEV-27699](https://jira.mariadb.org/browse/MDEV-27699) ANALYZE FORMAT=JSON fields are incorrect for UNION ALL queries
* [Revision #83516a33a8](https://github.com/MariaDB/server/commit/83516a33a8)\
  2022-04-14 12:22:28 +0400
  * An additional patch for [MDEV-27690](https://jira.mariadb.org/browse/MDEV-27690) Crash on `CHARACTER SET csname COLLATE DEFAULT` in column definition
* Merge [Revision #9d734cdd61](https://github.com/MariaDB/server/commit/9d734cdd61) 2022-04-14 11:50:34 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* [Revision #f130a5ea3c](https://github.com/MariaDB/server/commit/f130a5ea3c)\
  2022-04-13 15:37:46 +0200
  * [MDEV-28266](https://jira.mariadb.org/browse/MDEV-28266) Crash in Field\_string::type\_handler when calling procedures
* [Revision #e4835bf572](https://github.com/MariaDB/server/commit/e4835bf572)\
  2022-04-13 09:23:52 +0300
  * [MDEV-28304](https://jira.mariadb.org/browse/MDEV-28304) innodb.instant\_alter,8k.rdiff does not apply on FreeBSD
* [Revision #42908dc5fb](https://github.com/MariaDB/server/commit/42908dc5fb)\
  2022-04-12 13:37:27 +0200
  * [MDEV-26171](https://jira.mariadb.org/browse/MDEV-26171): wsrep\_sst\_receive\_address does not parse IPv6 address correctly
* [Revision #d31732e02e](https://github.com/MariaDB/server/commit/d31732e02e)\
  2022-04-12 13:38:41 +0200
  * [MDEV-27834](https://jira.mariadb.org/browse/MDEV-27834) Incorrect provides of MariaDB-shared for CentOS8
* [Revision #bbdec04d59](https://github.com/MariaDB/server/commit/bbdec04d59)\
  2022-04-12 13:07:20 +0200
  * [MDEV-24317](https://jira.mariadb.org/browse/MDEV-24317) Data race in LOGGER::init\_error\_log at sql/log.cc:1443 and in LOGGER::error\_log\_print at sql/log.cc:1181
* [Revision #6891c4874a](https://github.com/MariaDB/server/commit/6891c4874a)\
  2022-04-11 17:30:28 +0300
  * [MDEV-28269](https://jira.mariadb.org/browse/MDEV-28269) Assertion \`save\_errno' in maria\_write or ER\_GET\_ERRNO
* [Revision #2ae92e8981](https://github.com/MariaDB/server/commit/2ae92e8981)\
  2022-04-09 23:01:26 +0400
  * [MDEV-28267](https://jira.mariadb.org/browse/MDEV-28267) ASAN heap-use-after-free in Item\_sp::func\_name\_cstring
* [Revision #d623b5a1dd](https://github.com/MariaDB/server/commit/d623b5a1dd)\
  2022-04-08 00:06:53 +0200
  * [MDEV-22282](https://jira.mariadb.org/browse/MDEV-22282) When using mysqldump to backup a view that contains derived tables, the database name is prepended to each table in the view
* [Revision #3814b04d6b](https://github.com/MariaDB/server/commit/3814b04d6b)\
  2022-04-08 10:23:24 +0400
  * [MDEV-28062](https://jira.mariadb.org/browse/MDEV-28062) Assertion \`(length % 4) == 0' failed in my\_lengthsp\_utf32 on INSERT..SELECT
* [Revision #4194f7b605](https://github.com/MariaDB/server/commit/4194f7b605)\
  2022-02-16 17:56:49 +0900
  * [MDEV-25116](https://jira.mariadb.org/browse/MDEV-25116) Spider: IF(COUNT( trigger SQL Error (1054)\_ Unknown column '' in field list
* [Revision #b725a91757](https://github.com/MariaDB/server/commit/b725a91757)\
  2022-04-07 17:49:59 +0200
  * [MDEV-28253](https://jira.mariadb.org/browse/MDEV-28253) Mysqldump - INVISIBLE column error
* [Revision #7a03128faf](https://github.com/MariaDB/server/commit/7a03128faf)\
  2022-04-05 14:02:52 +0200
  * [MDEV-28205](https://jira.mariadb.org/browse/MDEV-28205): SST via mariadb-backup stops on failure while archiving logs
* [Revision #3c99a48db3](https://github.com/MariaDB/server/commit/3c99a48db3)\
  2022-04-06 15:54:59 +0300
  * [MDEV-28247](https://jira.mariadb.org/browse/MDEV-28247) : Disable background ibuf merge during Galera SST
* [Revision #7355f7b1f5](https://github.com/MariaDB/server/commit/7355f7b1f5)\
  2022-04-07 06:13:22 +0400
  * Adding MTR tests to cover how keywords of different kinds behave in various contexts
* [Revision #e9735a8185](https://github.com/MariaDB/server/commit/e9735a8185)\
  2022-04-06 08:06:49 +0300
  * [MDEV-25975](https://jira.mariadb.org/browse/MDEV-25975) innodb\_disallow\_writes causes shutdown to hang
* Merge [Revision #7c584d8270](https://github.com/MariaDB/server/commit/7c584d8270) 2022-04-06 08:06:35 +0300 - Merge 10.2 into 10.3
* [Revision #2d2c3da8ec](https://github.com/MariaDB/server/commit/2d2c3da8ec)\
  2022-04-04 21:34:05 +0200
  * [MDEV-27673](https://jira.mariadb.org/browse/MDEV-27673) Warning after "select progress from information\_schema.processlist"
* [Revision #cf8d30efd2](https://github.com/MariaDB/server/commit/cf8d30efd2)\
  2022-04-04 21:39:34 +0200
  * Revert "[MDEV-28131](https://jira.mariadb.org/browse/MDEV-28131) Unexpected warning while selecting from information\_schema.processlist"
* [Revision #d7fd76456e](https://github.com/MariaDB/server/commit/d7fd76456e)\
  2022-04-05 13:09:21 +0200
  * [MDEV-19525](https://jira.mariadb.org/browse/MDEV-19525) fix the test for embedded
* [Revision #daed558b2c](https://github.com/MariaDB/server/commit/daed558b2c)\
  2022-04-04 11:28:36 +0200
  * [MDEV-28204](https://jira.mariadb.org/browse/MDEV-28204): The tr utility does not work as expected on rsync SST
* [Revision #0ffaf19c53](https://github.com/MariaDB/server/commit/0ffaf19c53)\
  2022-04-04 09:45:29 +0400
  * Adding a "const" qualifier to arguments of create\_func(), create\_native() etc
* [Revision #d271fbd392](https://github.com/MariaDB/server/commit/d271fbd392)\
  2022-04-04 08:50:24 +0400
  * [MDEV-28224](https://jira.mariadb.org/browse/MDEV-28224) error: cannot initialize return object of type 'bool' with an rvalue of type 'nullptr\_t'
* [Revision #8c169f5e03](https://github.com/MariaDB/server/commit/8c169f5e03)\
  2022-04-02 16:43:51 +0700
  * [MDEV-28220](https://jira.mariadb.org/browse/MDEV-28220): Assert failure in sp\_head::sp\_head on parsing a syntax incorrect statement CREATE SEQUENCE ... RESTART inside CREATE PROCEDURE/CREATE FUNCTION
* [Revision #49aee1a153](https://github.com/MariaDB/server/commit/49aee1a153)\
  2022-04-01 13:29:31 +0300
  * [MDEV-28210](https://jira.mariadb.org/browse/MDEV-28210) : SIGSEGV in the test galera.galera\_sst\_rsync2
* [Revision #1e859d4abc](https://github.com/MariaDB/server/commit/1e859d4abc)\
  2022-03-29 13:44:14 +0300
  * [MDEV-22973](https://jira.mariadb.org/browse/MDEV-22973) Assertion in compare\_record upon multi-update involving versioned table via view
* [Revision #58cd2a8ded](https://github.com/MariaDB/server/commit/58cd2a8ded)\
  2022-03-29 13:44:14 +0300
  * [MDEV-19525](https://jira.mariadb.org/browse/MDEV-19525) remove ER\_VERS\_FIELD\_WRONG\_TYPE from init\_from\_binary\_frm\_image()
* Merge [Revision #020e7d89eb](https://github.com/MariaDB/server/commit/020e7d89eb) 2022-03-29 09:53:15 +0300 - Merge 10.2 into 10.3
* [Revision #739002eec9](https://github.com/MariaDB/server/commit/739002eec9)\
  2022-03-28 09:42:26 +0200
  * [MDEV-28178](https://jira.mariadb.org/browse/MDEV-28178) Windows : sporadic ER\_ERROR\_ON\_RENAME .. (errno: 13 "Permission denied")
* [Revision #e048289e55](https://github.com/MariaDB/server/commit/e048289e55)\
  2022-03-25 11:04:56 -0700
  * [MDEV-27937](https://jira.mariadb.org/browse/MDEV-27937) Assertion failure when executing prepared statement with ? in IN list
* [Revision #549a71e74b](https://github.com/MariaDB/server/commit/549a71e74b)\
  2022-03-25 18:29:39 +0530
  * [MDEV-21873](https://jira.mariadb.org/browse/MDEV-21873): 10.2 to 10.3 upgrade doesn't remove semi-sync reference from mysql.plugin table Fix: Since mysql\_upgrade runs commands from mysql\_system\_tables.fix, added sql commands to check for semisync plugins in INFORMATION\_SCHEMA.PLUGINS and if they aren't there then delete them from mysql.plugin.
* [Revision #fbcf0225e1](https://github.com/MariaDB/server/commit/fbcf0225e1)\
  2022-03-25 13:52:32 +0400
  * [MDEV-19804](https://jira.mariadb.org/browse/MDEV-19804) sql\_mode=ORACLE: call procedure in packages
* [Revision #9b2fa2ae8e](https://github.com/MariaDB/server/commit/9b2fa2ae8e)\
  2022-03-11 10:27:36 +0200
  * [MDEV-24845](https://jira.mariadb.org/browse/MDEV-24845) Oddities around innodb\_fatal\_semaphore\_wait\_threshold and global.innodb\_disallow\_writes
* [Revision #6437b30404](https://github.com/MariaDB/server/commit/6437b30404)\
  2022-03-25 07:05:08 +0400
  * [MDEV-28166](https://jira.mariadb.org/browse/MDEV-28166) sql\_mode=ORACLE: fully qualified package function calls do not work: db.pkg.func()
* [Revision #cd88b0831f](https://github.com/MariaDB/server/commit/cd88b0831f)\
  2021-11-15 16:33:45 -0700
  * DBAAS-7828: Primary/replica: configuration change of autocommit=0 can not be applied
* [Revision #32ab6219be](https://github.com/MariaDB/server/commit/32ab6219be)\
  2021-08-05 12:59:37 -0600
  * [MDEV-25580](https://jira.mariadb.org/browse/MDEV-25580): rpl.rpl\_semi\_sync\_slave\_compressed\_protocol crashes because of wrong packet
* [Revision #bbf02c85ba](https://github.com/MariaDB/server/commit/bbf02c85ba)\
  2022-03-23 12:45:56 -0700
  * [MDEV-24281](https://jira.mariadb.org/browse/MDEV-24281) Reading from freed memory when running main.view with --ps-protocol
* [Revision #cade21b4e0](https://github.com/MariaDB/server/commit/cade21b4e0)\
  2022-03-22 09:27:43 +0200
  * [MDEV-27775](https://jira.mariadb.org/browse/MDEV-27775) : Some Galera tests fail on FreeBSD due to "unknown signal 9"
* [Revision #8f4d7e365e](https://github.com/MariaDB/server/commit/8f4d7e365e)\
  2022-02-10 07:33:02 +0200
  * [MDEV-27775](https://jira.mariadb.org/browse/MDEV-27775) : Some Galera tests fail on FreeBSD due to "unknown signal 9"
* [Revision #0812d0de8d](https://github.com/MariaDB/server/commit/0812d0de8d)\
  2022-03-21 16:42:58 +0400
  * [MDEV-28131](https://jira.mariadb.org/browse/MDEV-28131) Unexpected warning while selecting from information\_schema.processlist
* [Revision #fbc1cc974e](https://github.com/MariaDB/server/commit/fbc1cc974e)\
  2022-03-18 11:13:09 +0100
  * [MDEV-26009](https://jira.mariadb.org/browse/MDEV-26009) Server crash when calling twice procedure using FOR-loop
* [Revision #cf86580f2b](https://github.com/MariaDB/server/commit/cf86580f2b)\
  2022-03-10 12:07:38 +0900
  * [MDEV-28032](https://jira.mariadb.org/browse/MDEV-28032) "git submodule update --depth 1" may fail with old Git
* [Revision #ecb6f9c894](https://github.com/MariaDB/server/commit/ecb6f9c894)\
  2022-03-17 16:57:56 +0100
  * [MDEV-28095](https://jira.mariadb.org/browse/MDEV-28095) crash in multi-update and implicit grouping
* Merge [Revision #6a2d88c132](https://github.com/MariaDB/server/commit/6a2d88c132) 2022-03-16 12:51:22 +1100 - Merge 10.2 to 10.3
* Merge [Revision #0e63023cb8](https://github.com/MariaDB/server/commit/0e63023cb8) 2022-03-15 14:27:04 +0400 - Merge branch 10.2 into 10.3
* Merge [Revision #a950086036](https://github.com/MariaDB/server/commit/a950086036) 2022-03-15 16:44:52 +1100 - Merge 10.2 (part) into 10.3
* [Revision #bfed2c7d57](https://github.com/MariaDB/server/commit/bfed2c7d57)\
  2022-03-11 20:18:22 +0100
  * [MDEV-27753](https://jira.mariadb.org/browse/MDEV-27753) Incorrect ENGINE type of table after crash for CONNECT table
* [Revision #f217c76189](https://github.com/MariaDB/server/commit/f217c76189)\
  2022-02-21 18:16:17 +0100
  * mtr: fix --source lines detection
* [Revision #6789f2cfab](https://github.com/MariaDB/server/commit/6789f2cfab)\
  2021-10-12 18:34:51 +0200
  * [MDEV-18304](https://jira.mariadb.org/browse/MDEV-18304) sql\_safe\_updates does not work with OR clauses
* [Revision #dc680d2119](https://github.com/MariaDB/server/commit/dc680d2119)\
  2022-03-11 16:14:06 +0200
  * Avoid shutdown timeout in innodb.undo\_truncate
* [Revision #1766a18e06](https://github.com/MariaDB/server/commit/1766a18e06)\
  2022-03-02 21:29:53 +0300
  * [MDEV-19577](https://jira.mariadb.org/browse/MDEV-19577) Replication does not work with innodb\_autoinc\_lock\_mode=2
* [Revision #e7cf871dda](https://github.com/MariaDB/server/commit/e7cf871dda)\
  2022-03-03 17:47:54 +0200
  * [MDEV-24617](https://jira.mariadb.org/browse/MDEV-24617) OPTIMIZE on a sequence causes unexpected ER\_BINLOG\_UNSAFE\_STATEMENT
* [Revision #8ea08505a1](https://github.com/MariaDB/server/commit/8ea08505a1)\
  2022-03-08 09:35:03 +1100
  * [MDEV-28022](https://jira.mariadb.org/browse/MDEV-28022): Debian stretch has zstd too old
* [Revision #86c1bf118a](https://github.com/MariaDB/server/commit/86c1bf118a)\
  2022-03-07 13:03:53 +0300
  * [MDEV-27992](https://jira.mariadb.org/browse/MDEV-27992) DELETE fails to delete record after blocking is released
* Merge [Revision #02da00a98c](https://github.com/MariaDB/server/commit/02da00a98c) 2022-03-04 14:29:36 +0200 - Merge 10.2 into 10.3
* [Revision #3c06a0b7dc](https://github.com/MariaDB/server/commit/3c06a0b7dc)\
  2022-03-04 14:23:33 +0200
  * [MDEV-28004](https://jira.mariadb.org/browse/MDEV-28004) ha\_innobase::reset\_auto\_increment() is never executed
* [Revision #1248fe7277](https://github.com/MariaDB/server/commit/1248fe7277)\
  2022-02-03 12:57:32 +0530
  * [MDEV-27582](https://jira.mariadb.org/browse/MDEV-27582) Fulltext DDL decrements the FTS\_DOC\_ID value
* [Revision #0635088deb](https://github.com/MariaDB/server/commit/0635088deb)\
  2022-02-28 12:12:12 +0200
  * [MDEV-27800](https://jira.mariadb.org/browse/MDEV-27800): Avoid garbage TRX\_UNDO\_TRX\_NO on TRX\_UNDO\_CACHED pages
* Merge [Revision #535bef86ad](https://github.com/MariaDB/server/commit/535bef86ad) 2022-02-28 10:17:39 +0200 - Merge 10.2 into 10.3
* Merge [Revision #9ba385a50d](https://github.com/MariaDB/server/commit/9ba385a50d) 2022-02-25 12:40:26 +0200 - Merge 10.2 into 10.3
* Merge [Revision #00b70bbb51](https://github.com/MariaDB/server/commit/00b70bbb51) 2022-02-25 10:43:38 +0200 - Merge 10.2 into 10.3
* [Revision #7ab3db142b](https://github.com/MariaDB/server/commit/7ab3db142b)\
  2022-02-25 10:30:04 +0200
  * [MDEV-27913](https://jira.mariadb.org/browse/MDEV-27913) fixup: sys\_vars.sysvars\_innodb result
* [Revision #a76731e1a1](https://github.com/MariaDB/server/commit/a76731e1a1)\
  2022-02-24 19:42:43 +0530
  * [MDEV-27913](https://jira.mariadb.org/browse/MDEV-27913) innodb\_ft\_cache\_size max possible value (80000000) is too small for practical purposes
* [Revision #a6f258e47f](https://github.com/MariaDB/server/commit/a6f258e47f)\
  2021-11-30 18:22:39 +0300
  * [MDEV-20605](https://jira.mariadb.org/browse/MDEV-20605) Awaken transaction can miss inserted by other transaction records due to wrong persistent cursor restoration
* [Revision #b9ee26e9f4](https://github.com/MariaDB/server/commit/b9ee26e9f4)\
  2022-01-20 07:37:43 +0200
  * [MDEV-27550](https://jira.mariadb.org/browse/MDEV-27550): Disable galera.MW-328D
* [Revision #5f001bd7b8](https://github.com/MariaDB/server/commit/5f001bd7b8)\
  2022-01-11 18:19:39 +0300
  * [MDEV-27025](https://jira.mariadb.org/browse/MDEV-27025) insert-intention lock conflicts with waiting ORDINARY lock
* [Revision #66f55a018b](https://github.com/MariaDB/server/commit/66f55a018b)\
  2022-02-15 16:18:55 +0900
  * [MDEV-27730](https://jira.mariadb.org/browse/MDEV-27730) Add PLUGIN\_VAR\_DEPRECATED flag to plugin variables
* Merge [Revision #5b237e5965](https://github.com/MariaDB/server/commit/5b237e5965) 2022-02-17 10:53:58 +0200 - Merge 10.2 into 10.3
* [Revision #0a92ef458b](https://github.com/MariaDB/server/commit/0a92ef458b)\
  2022-02-16 14:47:26 +0200
  * [MDEV-17223](https://jira.mariadb.org/browse/MDEV-17223) Assertion `thd->killed != 0' failed in ha_maria::enable_indexes [MDEV-22500](https://jira.mariadb.org/browse/MDEV-22500) Assertion` thd->killed != 0' failed in ha\_maria::enable\_indexes
* [Revision #6c3f1f661c](https://github.com/MariaDB/server/commit/6c3f1f661c)\
  2022-02-10 16:04:44 +0700
  * [MDEV-27691](https://jira.mariadb.org/browse/MDEV-27691): make working view-protocol
* Merge [Revision #e928fdbff1](https://github.com/MariaDB/server/commit/e928fdbff1) 2022-02-14 08:49:11 +0200 - Merge 10.2 into 10.3
* Merge [Revision #a6ef239b9e](https://github.com/MariaDB/server/commit/a6ef239b9e) 2022-02-14 08:48:48 +0200 - Merge mariadb-10.3.34 into 10.3
* [Revision #e50421be21](https://github.com/MariaDB/server/commit/e50421be21)\
  2022-02-12 15:18:56 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
