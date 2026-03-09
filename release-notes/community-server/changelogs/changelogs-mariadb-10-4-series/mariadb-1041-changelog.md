# MariaDB 10.4.0 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.1/)[Release Notes](../../old-releases/10.4/10.4.1.md)[Changelog](mariadb-1041-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 20 Dec 2018

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.1.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #30641f9df7](https://github.com/MariaDB/server/commit/30641f9df7)\
  2018-12-18 16:38:08 +0100
  * Fix of maturity status
* Merge [Revision #1b3770acda](https://github.com/MariaDB/server/commit/1b3770acda) 2018-12-18 11:53:31 +0200 - Merge 10.3 into 10.4
* Merge [Revision #75e7e0b90f](https://github.com/MariaDB/server/commit/75e7e0b90f) 2018-12-18 11:51:44 +0200 - Merge 10.2 into 10.3
* Merge [Revision #0032170940](https://github.com/MariaDB/server/commit/0032170940) 2018-12-18 10:01:15 +0200 - Merge 10.1 into 10.2
* [Revision #84f119f25c](https://github.com/MariaDB/server/commit/84f119f25c)\
  2018-12-18 09:52:28 +0200
  * [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112)/[MDEV-12114](https://jira.mariadb.org/browse/MDEV-12114): Relax strict\_innodb, strict\_none
* Merge [Revision #af9731071d](https://github.com/MariaDB/server/commit/af9731071d) 2018-12-18 09:44:49 +0200 - Merge pull request #1031 from tempesta-tech/sysprg/[MDEV-17786](https://jira.mariadb.org/browse/MDEV-17786)
* [Revision #dcef75df9f](https://github.com/MariaDB/server/commit/dcef75df9f)\
  2018-12-12 13:49:45 +0100
  * DEV-17786: Add mariadb-backup test case for galera\_sst\_xtrabackup-v2\_data\_dir
* Merge [Revision #b5763ecd01](https://github.com/MariaDB/server/commit/b5763ecd01) 2018-12-18 11:33:53 +0200 - Merge 10.3 into 10.4
* Merge [Revision #45531949ae](https://github.com/MariaDB/server/commit/45531949ae) 2018-12-18 09:15:41 +0200 - Merge 10.2 into 10.3
* [Revision #ed13a0d221](https://github.com/MariaDB/server/commit/ed13a0d221)\
  2018-12-17 22:45:21 +0200
  * [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112): Support WITH\_INNODB\_BUG\_ENDIAN\_CRC32
* Merge [Revision #fae7e350a8](https://github.com/MariaDB/server/commit/fae7e350a8) 2018-12-17 22:35:32 +0200 - Merge 10.1 into 10.2
* [Revision #51a1fc737c](https://github.com/MariaDB/server/commit/51a1fc737c)\
  2018-12-17 22:35:22 +0200
  * Fix a compiler warning
* Merge [Revision #7d245083a4](https://github.com/MariaDB/server/commit/7d245083a4) 2018-12-17 20:04:03 +0200 - Merge 10.1 into 10.2
* [Revision #8c43f96388](https://github.com/MariaDB/server/commit/8c43f96388)\
  2018-12-17 19:00:35 +0200
  * Follow-up to [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112): corruption in encrypted table may be overlooked
* Merge [Revision #517c59c540](https://github.com/MariaDB/server/commit/517c59c540) 2018-12-17 07:45:14 +0200 - Merge pull request #1026 from codership/10.1-galera-defaults
* [Revision #6b81883170](https://github.com/MariaDB/server/commit/6b81883170)\
  2018-12-14 21:29:17 +0200
  * Remove provider defaults check from 'galera\_defaults' MTR test
* [Revision #ee543beabf](https://github.com/MariaDB/server/commit/ee543beabf)\
  2018-12-17 07:05:27 +0200
  * [MDEV-18021](https://jira.mariadb.org/browse/MDEV-18021): Galera test galera\_sst\_mariadb-backup\_table\_options fails if AES\_CTR is not available
* [Revision #8a46b9fe3b](https://github.com/MariaDB/server/commit/8a46b9fe3b)\
  2018-11-27 15:26:18 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* [Revision #10e01b56f7](https://github.com/MariaDB/server/commit/10e01b56f7)\
  2018-12-17 16:33:23 +0200
  * Fix USE\_AFTER\_FREE (CWE-416)
* [Revision #32eeed2129](https://github.com/MariaDB/server/commit/32eeed2129)\
  2018-12-17 00:35:44 +0530
  * [MDEV-17676](https://jira.mariadb.org/browse/MDEV-17676): Assertion \`inited==NONE || (inited==RND && scan)' failed in handler::ha\_rnd\_init
* [Revision #20011c8b14](https://github.com/MariaDB/server/commit/20011c8b14)\
  2018-12-16 18:43:51 +0400
  * [MDEV-14576](https://jira.mariadb.org/browse/MDEV-14576) Include full name of object in message about incorrect value for column.
* [Revision #d1fb52afff](https://github.com/MariaDB/server/commit/d1fb52afff)\
  2018-12-16 14:51:51 +0400
  * [MDEV-14576](https://jira.mariadb.org/browse/MDEV-14576) Include full name of object in message about incorrect value for column.
* [Revision #c4ab352b67](https://github.com/MariaDB/server/commit/c4ab352b67)\
  2018-12-16 02:21:41 +0400
  * [MDEV-14576](https://jira.mariadb.org/browse/MDEV-14576) Include full name of object in message about incorrect value for column.
* [Revision #0a2edddbf4](https://github.com/MariaDB/server/commit/0a2edddbf4)\
  2018-12-15 00:06:00 +0100
  * [MDEV-14975](https://jira.mariadb.org/browse/MDEV-14975) : fix last commit's typo.
* [Revision #5716c71c54](https://github.com/MariaDB/server/commit/5716c71c54)\
  2018-12-14 23:36:21 +0100
  * [MDEV-14975](https://jira.mariadb.org/browse/MDEV-14975) mariadb-backup starts with unprivileged user.
* Merge [Revision #36b7f8f4b0](https://github.com/MariaDB/server/commit/36b7f8f4b0) 2018-12-17 18:37:56 +0200 - Merge pull request #1030 from tempesta-tech/sysprg/[MDEV-17848](https://jira.mariadb.org/browse/MDEV-17848)
* [Revision #d48ac8b414](https://github.com/MariaDB/server/commit/d48ac8b414)\
  2018-12-12 13:44:58 +0100
  * [MDEV-17848](https://jira.mariadb.org/browse/MDEV-17848): Galera test failure on galera\_sst\_xtrabackup-v2\[\_data\_dir]
* [Revision #375256bae7](https://github.com/MariaDB/server/commit/375256bae7)\
  2018-12-14 11:30:34 +0400
  * [MDEV-18010](https://jira.mariadb.org/browse/MDEV-18010) Add classes Inet4 and Inet6
* [Revision #3b8c868aa1](https://github.com/MariaDB/server/commit/3b8c868aa1)\
  2018-12-15 01:26:01 +0530
  * Enabling innodb.innodb-alter-table, main.column\_compression\_parts and main.partition\_explicit\_prune
* Merge [Revision #fd37344feb](https://github.com/MariaDB/server/commit/fd37344feb) 2018-12-14 16:19:49 +0200 - Merge 10.3 into 10.4
* Merge [Revision #5fefcb0a21](https://github.com/MariaDB/server/commit/5fefcb0a21) 2018-12-14 16:13:35 +0200 - Merge 10.2 into 10.3
* Merge [Revision #94fa02f4d0](https://github.com/MariaDB/server/commit/94fa02f4d0) 2018-12-14 16:11:05 +0200 - Merge 10.1 into 10.2
* [Revision #fb252f70c1](https://github.com/MariaDB/server/commit/fb252f70c1)\
  2018-12-14 15:44:51 +0200
  * [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112) corruption in encrypted table may be overlooked
* [Revision #a2f2f686cb](https://github.com/MariaDB/server/commit/a2f2f686cb)\
  2018-12-14 15:50:01 +0200
  * Work around the crash in [MDEV-17814](https://jira.mariadb.org/browse/MDEV-17814)
* Merge [Revision #cfe8386296](https://github.com/MariaDB/server/commit/cfe8386296) 2018-12-14 13:58:45 +0200 - Merge 10.2 into 10.3
* [Revision #dbb39a778d](https://github.com/MariaDB/server/commit/dbb39a778d)\
  2018-12-14 13:44:30 +0200
  * [MDEV-17958](https://jira.mariadb.org/browse/MDEV-17958): Make innochecksum follow the build option
* [Revision #c1caada886](https://github.com/MariaDB/server/commit/c1caada886)\
  2018-12-13 17:06:26 +0100
  * [MDEV-16278](https://jira.mariadb.org/browse/MDEV-16278): Missing DELETE operation in COM\_STMT\_BULK\_STMT
* [Revision #67e3d1ee93](https://github.com/MariaDB/server/commit/67e3d1ee93)\
  2018-12-14 11:32:36 +0200
  * Reduce the number of dict\_table\_page\_size() calls
* [Revision #f648145717](https://github.com/MariaDB/server/commit/f648145717)\
  2018-12-14 11:28:22 +0200
  * dict\_table\_t::init\_instant(): Remove a bogus assertion
* [Revision #a87e501945](https://github.com/MariaDB/server/commit/a87e501945)\
  2018-12-14 06:49:55 +0200
  * [MDEV-18007](https://jira.mariadb.org/browse/MDEV-18007) innodb.instant\_alter\_crash: Assertion failed: n < tuple->n\_fields
* [Revision #330c6218dd](https://github.com/MariaDB/server/commit/330c6218dd)\
  2018-11-27 22:25:11 +0300
  * Replace dict\_instant\_t::non\_pk\_col\_map with field\_map
* [Revision #a044e326a8](https://github.com/MariaDB/server/commit/a044e326a8)\
  2018-11-13 16:42:49 +0200
  * Introduce dict\_table\_t::init\_instant()
* [Revision #b32a31913a](https://github.com/MariaDB/server/commit/b32a31913a)\
  2018-11-08 12:22:10 +0200
  * Add dict\_col\_t::same\_format()
* [Revision #7a27db778e](https://github.com/MariaDB/server/commit/7a27db778e)\
  2018-11-07 19:31:28 +0200
  * [MDEV-15563](https://jira.mariadb.org/browse/MDEV-15563): Instantly change a column to NULL
* [Revision #62d28f83b6](https://github.com/MariaDB/server/commit/62d28f83b6)\
  2018-12-13 22:19:09 +0200
  * [MDEV-17958](https://jira.mariadb.org/browse/MDEV-17958): Remove WITH\_INNODB\_BUG\_ENDIAN\_CRC32
* Merge [Revision #6dbc50a376](https://github.com/MariaDB/server/commit/6dbc50a376) 2018-12-13 22:05:34 +0200 - Merge 10.3 into 10.4
* Merge [Revision #f6e16bdc62](https://github.com/MariaDB/server/commit/f6e16bdc62) 2018-12-13 21:58:35 +0200 - Merge 10.2 into 10.3
* [Revision #e3dda3d95e](https://github.com/MariaDB/server/commit/e3dda3d95e)\
  2018-12-13 21:25:12 +0200
  * [MDEV-17989](https://jira.mariadb.org/browse/MDEV-17989) InnoDB: Failing assertion: dict\_tf2\_is\_valid(flags, flags2)
* [Revision #1a780eefc9](https://github.com/MariaDB/server/commit/1a780eefc9)\
  2018-12-13 17:57:10 +0200
  * [MDEV-17958](https://jira.mariadb.org/browse/MDEV-17958) Make bug-endian innodb\_checksum\_algorithm=crc32 optional
* Merge [Revision #2e5aea4bab](https://github.com/MariaDB/server/commit/2e5aea4bab) 2018-12-13 15:47:38 +0200 - Merge 10.1 into 10.2
* Merge [Revision #621041b676](https://github.com/MariaDB/server/commit/621041b676) 2018-12-13 13:37:21 +0200 - Merge 10.0 into 10.1
* [Revision #8e613458e1](https://github.com/MariaDB/server/commit/8e613458e1)\
  2018-12-13 12:36:57 +0200
  * Fix cmake -DWITH\_PARTITION\_STORAGE\_ENGINE:BOOL=OFF
* [Revision #5ab91f5914](https://github.com/MariaDB/server/commit/5ab91f5914)\
  2018-12-13 12:15:18 +0200
  * Remove space before #ifdef
* [Revision #5f5e73f1fe](https://github.com/MariaDB/server/commit/5f5e73f1fe)\
  2018-12-11 16:16:11 +0530
  * [MDEV-17957](https://jira.mariadb.org/browse/MDEV-17957) Make Innodb\_checksum\_algorithm stricter for strict\_\* values
* [Revision #ce1669af12](https://github.com/MariaDB/server/commit/ce1669af12)\
  2018-12-13 00:26:54 +0530
  * Fix compile error when building without the partition engine
* Merge [Revision #b58f28725b](https://github.com/MariaDB/server/commit/b58f28725b) 2018-12-12 20:19:06 +0100 - Merge branch '5.5' into 10.0
* [Revision #32b7d456d5](https://github.com/MariaDB/server/commit/32b7d456d5)\
  2018-11-28 19:19:16 +0100
  * mysqltest: use a dynamically growing command buffer
* [Revision #c362ea3ffd](https://github.com/MariaDB/server/commit/c362ea3ffd)\
  2014-06-25 12:32:22 +0200
  * Added Master\_Host to the Replication information
* [Revision #9eadef013e](https://github.com/MariaDB/server/commit/9eadef013e)\
  2018-12-12 15:05:14 +0800
  * Fix UNICODE issue of dlerror
* [Revision #541500295a](https://github.com/MariaDB/server/commit/541500295a)\
  2018-12-11 11:38:30 +0100
  * debian install/upgrade fixes
* [Revision #ad3346dddf](https://github.com/MariaDB/server/commit/ad3346dddf)\
  2018-11-16 14:00:36 +0100
  * add more dbug helpers for gdb
* [Revision #c913cd2b66](https://github.com/MariaDB/server/commit/c913cd2b66)\
  2018-12-12 16:31:34 +0200
  * [MDEV-17885](https://jira.mariadb.org/browse/MDEV-17885) TRUNCATE on temporary table causes ER\_GET\_ERRNO
* [Revision #4752a039b5](https://github.com/MariaDB/server/commit/4752a039b5)\
  2018-12-13 15:09:03 +0400
  * [MDEV-17995](https://jira.mariadb.org/browse/MDEV-17995) INET6\_NTOA(ucs2\_input) erroneously returns NULL
* [Revision #5c0730e0ce](https://github.com/MariaDB/server/commit/5c0730e0ce)\
  2018-12-12 19:00:41 +0100
  * Fix clang-cl format warning
* [Revision #19d3d3e861](https://github.com/MariaDB/server/commit/19d3d3e861)\
  2018-12-11 18:23:54 +0100
  * [MDEV-16266](https://jira.mariadb.org/browse/MDEV-16266) - New command FLUSH SSL to reload server's SSL certificate(private key,CRL,etc)
* [Revision #f570da5153](https://github.com/MariaDB/server/commit/f570da5153)\
  2018-12-12 23:28:18 +0200
  * Fix TokuDB results after merge
* [Revision #351c2f1425](https://github.com/MariaDB/server/commit/351c2f1425)\
  2018-12-12 23:12:46 +0200
  * Fix a sign mismatch on comparison
* [Revision #bf096f2919](https://github.com/MariaDB/server/commit/bf096f2919)\
  2018-12-12 23:06:37 +0200
  * Fix btr\_corruption\_report() declaration on Windows
* [Revision #61967b90d7](https://github.com/MariaDB/server/commit/61967b90d7)\
  2018-12-11 18:00:43 +0200
  * btr\_corruption\_report(): Add ATTRIBUTE\_NORETURN
* Merge [Revision #c64265f3f9](https://github.com/MariaDB/server/commit/c64265f3f9) 2018-12-12 13:51:37 +0200 - Merge 10.3 into 10.4
* Merge [Revision #839cf16bb2](https://github.com/MariaDB/server/commit/839cf16bb2) 2018-12-12 13:46:06 +0200 - Merge 10.2 into 10.3
* [Revision #91173f9863](https://github.com/MariaDB/server/commit/91173f9863)\
  2018-12-12 13:30:40 +0200
  * fts\_is\_charset\_cjk(): Avoid referencing global symbols
* [Revision #e0aebf5cf1](https://github.com/MariaDB/server/commit/e0aebf5cf1)\
  2018-12-12 13:10:52 +0200
  * [MDEV-17815](https://jira.mariadb.org/browse/MDEV-17815) Assertion failed in btr\_node\_ptr\_max\_size for CHAR(0)
* Merge [Revision #db1210f939](https://github.com/MariaDB/server/commit/db1210f939) 2018-12-12 12:13:43 +0200 - Merge 10.1 into 10.2
* Merge [Revision #f77f8f6d1a](https://github.com/MariaDB/server/commit/f77f8f6d1a) 2018-12-12 10:48:53 +0200 - Merge 10.0 into 10.1
* [Revision #d956709b4b](https://github.com/MariaDB/server/commit/d956709b4b)\
  2018-12-11 22:03:44 +0300
  * [MDEV-17833](https://jira.mariadb.org/browse/MDEV-17833) ALTER TABLE is not enforcing prefix index size limit
* [Revision #4886d14827](https://github.com/MariaDB/server/commit/4886d14827)\
  2018-12-07 02:12:22 +0530
  * [MDEV-17032](https://jira.mariadb.org/browse/MDEV-17032): Estimates are higher for partitions of a table with @@use\_stat\_tables= PREFERABLY
* [Revision #dce2cc1c6a](https://github.com/MariaDB/server/commit/dce2cc1c6a)\
  2018-12-12 11:35:21 +0100
  * fix handler test failures on s390x
* [Revision #56d3a0e73b](https://github.com/MariaDB/server/commit/56d3a0e73b)\
  2018-12-07 00:33:51 +0100
  * [MDEV-17967](https://jira.mariadb.org/browse/MDEV-17967) Add a solution of the 8 queens problem to the regression test for CTE
* [Revision #ac31ff6275](https://github.com/MariaDB/server/commit/ac31ff6275)\
  2018-12-10 23:31:54 +0100
  * [MDEV-15760](https://jira.mariadb.org/browse/MDEV-15760) - don't build mariadb-backup with -DPLUGIN\_INNOBASE=DYNAMIC
* [Revision #8aef7f2bb9](https://github.com/MariaDB/server/commit/8aef7f2bb9)\
  2018-12-10 00:34:41 +0530
  * [MDEV-17778](https://jira.mariadb.org/browse/MDEV-17778): Alter table leads to a truncation warning with ANALYZE command
* [Revision #b6a44b4c24](https://github.com/MariaDB/server/commit/b6a44b4c24)\
  2018-12-12 13:49:13 +0200
  * row\_undo\_mod\_clust(): Fix stack-use-after-scope
* [Revision #c1e695c90e](https://github.com/MariaDB/server/commit/c1e695c90e)\
  2018-12-12 12:09:18 +0200
  * [MDEV-17763](https://jira.mariadb.org/browse/MDEV-17763) Assertion \`len == 20U' failed in rec\_convert\_dtuple\_to\_rec\_comp on DROP COLUMN
* [Revision #2681ca04f2](https://github.com/MariaDB/server/commit/2681ca04f2)\
  2018-12-12 14:10:45 +0400
  * The last commit was pushed with a wrong title: [MDEV-17968](https://jira.mariadb.org/browse/MDEV-17968) Error 174 "Fatal error during initialization of handler" from storage engine Aria upon DELETE from partitioned table
* [Revision #c8774408cb](https://github.com/MariaDB/server/commit/c8774408cb)\
  2018-12-12 14:07:27 +0400
  * [MDEV-17968](https://jira.mariadb.org/browse/MDEV-17968) Error 174 "Fatal error during initialization of handler" from storage engine Aria upon DELETE from partitioned table
* [Revision #c353b2a8fc](https://github.com/MariaDB/server/commit/c353b2a8fc)\
  2018-12-12 10:39:06 +0400
  * \--echo

## --echo

## [MDEV-17979](https://jira.mariadb.org/browse/MDEV-17979) Assertion \`0' failed in Item::val\_native upon SELECT with timestamp, NULLIF, GROUP BY --echo

* [Revision #4abb8216a0](https://github.com/MariaDB/server/commit/4abb8216a0)\
  2018-11-24 14:13:41 +0100
  * [MDEV-17658](https://jira.mariadb.org/browse/MDEV-17658) change the structure of mysql.user table
* [Revision #d68d7e50f9](https://github.com/MariaDB/server/commit/d68d7e50f9)\
  2018-11-28 18:16:46 +0100
  * json helpers
* [Revision #a76aadf7bc](https://github.com/MariaDB/server/commit/a76aadf7bc)\
  2018-11-22 16:16:53 +0100
  * [MDEV-17658](https://jira.mariadb.org/browse/MDEV-17658) change the structure of mysql.user table
* [Revision #9887d2e881](https://github.com/MariaDB/server/commit/9887d2e881)\
  2018-11-22 10:23:12 +0100
  * cleanup: simplify opening of priv tables
* [Revision #a701426b43](https://github.com/MariaDB/server/commit/a701426b43)\
  2018-11-18 19:25:11 +0100
  * cleanup: refactor grant table classes in sql\_acl.cc
* [Revision #3df7287d21](https://github.com/MariaDB/server/commit/3df7287d21)\
  2018-11-28 12:20:37 +0100
  * fix the test for the empty password hash string
* [Revision #1db6c3a207](https://github.com/MariaDB/server/commit/1db6c3a207)\
  2018-12-08 13:28:00 +0100
  * extend the test case to better emulate 5.7 user table
* [Revision #07e9b13898](https://github.com/MariaDB/server/commit/07e9b13898)\
  2018-12-07 13:05:34 +0100
  * mysqld: ignore SIGHUP sent by the kernel
* [Revision #97dbb3562b](https://github.com/MariaDB/server/commit/97dbb3562b)\
  2018-12-07 12:54:10 +0100
  * simplify usage of logger.set\_handlers()
* [Revision #a4ac987cbc](https://github.com/MariaDB/server/commit/a4ac987cbc)\
  2018-12-11 18:22:40 +0100
  * more tests for mysql\_install\_db.exe
* [Revision #7af62f8a03](https://github.com/MariaDB/server/commit/7af62f8a03)\
  2018-12-07 18:14:20 +0100
  * [MDEV-17926](https://jira.mariadb.org/browse/MDEV-17926) FederatedX TODO is obsolete
* [Revision #b1527ef51c](https://github.com/MariaDB/server/commit/b1527ef51c)\
  2018-12-12 01:49:39 +0400
  * [MDEV-5313](https://jira.mariadb.org/browse/MDEV-5313) Improving audit api.
* [Revision #dc6ad59765](https://github.com/MariaDB/server/commit/dc6ad59765)\
  2018-12-11 20:50:22 +0200
  * [MDEV-17901](https://jira.mariadb.org/browse/MDEV-17901) Crash after instant DROP COLUMN of AUTO\_INCREMENT column
* [Revision #8dc460b844](https://github.com/MariaDB/server/commit/8dc460b844)\
  2018-12-11 21:17:39 +0800
  * Fix UNICODE issue of dlerror()
* [Revision #1b31d8852c](https://github.com/MariaDB/server/commit/1b31d8852c)\
  2018-12-11 13:45:24 +0200
  * [MDEV-17899](https://jira.mariadb.org/browse/MDEV-17899): Fix a regression from [MDEV-17793](https://jira.mariadb.org/browse/MDEV-17793)
* [Revision #1c53aeff58](https://github.com/MariaDB/server/commit/1c53aeff58)\
  2018-12-10 22:52:24 +0400
  * Fixed sporadic main.mdl\_sync failure
* [Revision #0fcb141fbd](https://github.com/MariaDB/server/commit/0fcb141fbd)\
  2018-12-10 21:01:18 +0400
  * Fixed main.create-big failure
* [Revision #8049160936](https://github.com/MariaDB/server/commit/8049160936)\
  2018-12-10 17:18:17 +0100
  * [MDEV-17946](https://jira.mariadb.org/browse/MDEV-17946) : Unsorted acl\_dbs after RENAME USER
* [Revision #34eb98387f](https://github.com/MariaDB/server/commit/34eb98387f)\
  2018-12-08 19:39:23 +0400
  * [MDEV-13995](https://jira.mariadb.org/browse/MDEV-13995) MAX(timestamp) returns a wrong result near DST change
* [Revision #5b3db87134](https://github.com/MariaDB/server/commit/5b3db87134)\
  2018-12-10 19:37:36 +0530
  * Updated the result for innodb.innodb\_mysql
* [Revision #f69879baca](https://github.com/MariaDB/server/commit/f69879baca)\
  2018-12-10 15:58:32 +0200
  * [MDEV-17899](https://jira.mariadb.org/browse/MDEV-17899) Assertion failures on rollback of instant ADD/DROP
* [Revision #3efed7533c](https://github.com/MariaDB/server/commit/3efed7533c)\
  2018-12-10 14:01:46 +0100
  * Fix lock\_ddl\_per\_table handling in mariadb-backup.
* Merge [Revision #fcb6bb4bcc](https://github.com/MariaDB/server/commit/fcb6bb4bcc) 2018-12-10 13:16:03 +0200 - Merge 10.3 into 10.4
* [Revision #a72516348b](https://github.com/MariaDB/server/commit/a72516348b)\
  2018-12-10 13:02:04 +0200
  * [MDEV-17938](https://jira.mariadb.org/browse/MDEV-17938): ALTER TABLE error handling accesses freed memory
* Merge [Revision #1d18665e0b](https://github.com/MariaDB/server/commit/1d18665e0b) 2018-12-10 12:28:31 +0200 - Merge 10.2 into 10.3
* [Revision #0d7cf06af5](https://github.com/MariaDB/server/commit/0d7cf06af5)\
  2018-12-10 11:44:39 +0200
  * [MDEV-17938](https://jira.mariadb.org/browse/MDEV-17938) ALTER TABLE reports ER\_TABLESPACE\_EXISTS after failed ALTER TABLE
* [Revision #705fd4e943](https://github.com/MariaDB/server/commit/705fd4e943)\
  2018-12-08 22:53:47 +0100
  * Fix another random failure in rpl.rpl\_gtid\_crash
* [Revision #e5144f4bad](https://github.com/MariaDB/server/commit/e5144f4bad)\
  2018-12-10 13:06:20 +0400
  * Cleanup: Datetime() constructors accepting Longlong\_hybrid/Sec6 do not need THD
* [Revision #8cf7e3459d](https://github.com/MariaDB/server/commit/8cf7e3459d)\
  2018-12-06 19:23:24 +0400
  * Moved early check for table existance to mysql\_execute\_command()
* [Revision #c0ca164b1c](https://github.com/MariaDB/server/commit/c0ca164b1c)\
  2018-11-19 20:43:04 +0100
  * [MDEV-17308](https://jira.mariadb.org/browse/MDEV-17308) mariadb-backup to use the BACKUP statement instead of FTWRL
* [Revision #c53aab974b](https://github.com/MariaDB/server/commit/c53aab974b)\
  2018-11-13 01:34:37 +0200
  * Added syntax and implementation for BACKUP STAGE's
* [Revision #965311ee8b](https://github.com/MariaDB/server/commit/965311ee8b)\
  2018-11-06 17:05:24 +0200
  * Added new MDL\_BACKUP locks for all backup stages
* [Revision #f386b70beb](https://github.com/MariaDB/server/commit/f386b70beb)\
  2018-11-27 16:59:29 +0200
  * Honor lock\_wait\_timeout when updating stats tables
* [Revision #e54643a063](https://github.com/MariaDB/server/commit/e54643a063)\
  2018-11-13 01:02:53 +0200
  * Simplify test for updateable TABLE\_CATEGORY's
* [Revision #f1867505a6](https://github.com/MariaDB/server/commit/f1867505a6)\
  2018-10-30 02:00:46 +0400
  * Acquire global read lock (MDL\_BACKUP\_STMT) after share is acquired
* [Revision #7a9dfdd8d9](https://github.com/MariaDB/server/commit/7a9dfdd8d9)\
  2018-10-30 00:09:02 +0400
  * Combine GLOBAL and COMMIT namespaces into BACKUP namespace.
* [Revision #7fb9d64989](https://github.com/MariaDB/server/commit/7fb9d64989)\
  2018-10-31 22:52:29 +0200
  * Changed FLUSH TABLES to not change share version
* [Revision #7bb3a5220e](https://github.com/MariaDB/server/commit/7bb3a5220e)\
  2018-11-06 13:24:43 +0200
  * Fixed race condition between flush tables and insert delayed
* [Revision #163b34fe25](https://github.com/MariaDB/server/commit/163b34fe25)\
  2018-10-09 18:55:18 +0300
  * Optimize flush tables with read lock (FTWRL) to not wait for select's
* [Revision #306b7a2243](https://github.com/MariaDB/server/commit/306b7a2243)\
  2018-11-18 21:34:58 +0200
  * Added API for copying aria tables in mariadb-backup
* [Revision #2aff2f2f34](https://github.com/MariaDB/server/commit/2aff2f2f34)\
  2018-11-16 16:50:12 +0200
  * Added --print-log-control-file option to aria\_read\_log
* [Revision #1077f320e4](https://github.com/MariaDB/server/commit/1077f320e4)\
  2018-10-06 16:49:54 +0300
  * Added backup handler calls
* [Revision #ecdf97924c](https://github.com/MariaDB/server/commit/ecdf97924c)\
  2018-12-09 16:53:19 +0200
  * Fixed that CREATE TABLE code used the right create\_info
* [Revision #4f541c5f43](https://github.com/MariaDB/server/commit/4f541c5f43)\
  2018-10-10 17:27:17 +0300
  * Added timing of bootstrap to mtr
* [Revision #5280af2b4e](https://github.com/MariaDB/server/commit/5280af2b4e)\
  2018-12-07 16:37:45 +0200
  * Cleaned up some MTR tests
* [Revision #dc91330d98](https://github.com/MariaDB/server/commit/dc91330d98)\
  2018-11-30 01:04:55 +0200
  * Fixed test case bug in purge\_thread\_shutdown
* [Revision #8561a0ac9e](https://github.com/MariaDB/server/commit/8561a0ac9e)\
  2018-11-19 20:06:02 +0200
  * Disabled some galera tests that always fails on OpenSuse 10.5
* [Revision #84c0563a27](https://github.com/MariaDB/server/commit/84c0563a27)\
  2018-11-19 19:52:07 +0200
  * Fixed BUILD scripts to by default work with galera and tokudb
* [Revision #c8250ed6c5](https://github.com/MariaDB/server/commit/c8250ed6c5)\
  2018-10-10 17:26:50 +0300
  * Add --without-wsrep option to BUILD scripts
* [Revision #fa8d7f3675](https://github.com/MariaDB/server/commit/fa8d7f3675)\
  2018-11-21 19:24:43 +0200
  * Fixed that mtr --extern works with --include/have\_innodb.inc
* [Revision #c82855d882](https://github.com/MariaDB/server/commit/c82855d882)\
  2018-11-07 13:16:29 +0200
  * Changed some MySQL names in messages to MariaDB
* [Revision #ae58cd6b87](https://github.com/MariaDB/server/commit/ae58cd6b87)\
  2018-10-09 19:08:16 +0300
  * Simple cleanups (no logic changes)
* [Revision #9207a838ed](https://github.com/MariaDB/server/commit/9207a838ed)\
  2018-12-09 13:25:27 +0530
  * [MDEV-17255](https://jira.mariadb.org/browse/MDEV-17255): New optimizer defaults and ANALYZE TABLE
* [Revision #93c360e3a5](https://github.com/MariaDB/server/commit/93c360e3a5)\
  2018-05-31 15:51:59 +0530
  * [MDEV-15253](https://jira.mariadb.org/browse/MDEV-15253): Default optimizer setting changes for [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/)
* [Revision #a25ce5ab4b](https://github.com/MariaDB/server/commit/a25ce5ab4b)\
  2018-12-08 16:10:44 +0400
  * [MDEV-17928](https://jira.mariadb.org/browse/MDEV-17928) Conversion from TIMESTAMP to VARCHAR SP variables does not work well on fractional digits
* [Revision #fac997feef](https://github.com/MariaDB/server/commit/fac997feef)\
  2018-12-08 02:19:37 +0100
  * Fix Win64 build
* [Revision #b1c41e112c](https://github.com/MariaDB/server/commit/b1c41e112c)\
  2018-12-08 01:16:05 +0100
  * [MDEV-17932](https://jira.mariadb.org/browse/MDEV-17932) : assertion in multi RENAME USER command.
* Merge [Revision #a80f5fdbd1](https://github.com/MariaDB/server/commit/a80f5fdbd1) 2018-12-08 00:12:55 +0200 - Merge 10.3 into 10.4
* [Revision #2fd0acd30f](https://github.com/MariaDB/server/commit/2fd0acd30f)\
  2018-12-07 23:58:42 +0200
  * Fix the 64-bit Windows build
* [Revision #a02cac47f6](https://github.com/MariaDB/server/commit/a02cac47f6)\
  2018-12-07 17:20:31 +0100
  * Fix an occational test failure in rpl.rpl\_gtid\_crash
* Merge [Revision #ce8716a1ed](https://github.com/MariaDB/server/commit/ce8716a1ed) 2018-12-07 16:12:17 +0200 - Merge 10.3 into 10.4
* Merge [Revision #21069c528e](https://github.com/MariaDB/server/commit/21069c528e) 2018-12-07 15:39:34 +0200 - Merge 10.2 into 10.3
* [Revision #53440e2dda](https://github.com/MariaDB/server/commit/53440e2dda)\
  2018-12-07 15:31:43 +0200
  * [MDEV-17923](https://jira.mariadb.org/browse/MDEV-17923): Fix the pointer arithmetics
* [Revision #52778e2e3e](https://github.com/MariaDB/server/commit/52778e2e3e)\
  2018-12-07 15:13:39 +0200
  * After-merge fix
* Merge [Revision #5e5deabdbc](https://github.com/MariaDB/server/commit/5e5deabdbc) 2018-12-07 13:41:10 +0200 - Merge 10.1 into 10.2
* Merge [Revision #ecd3a7e00d](https://github.com/MariaDB/server/commit/ecd3a7e00d) 2018-12-07 13:17:32 +0200 - Merge 10.0 into 10.1
* [Revision #12b1ba195c](https://github.com/MariaDB/server/commit/12b1ba195c)\
  2018-12-07 12:54:02 +0200
  * [MDEV-17904](https://jira.mariadb.org/browse/MDEV-17904) Crash in fts\_is\_sync\_needed() after failed ALTER or CREATE TABLE
* [Revision #2a2e8ea8fe](https://github.com/MariaDB/server/commit/2a2e8ea8fe)\
  2018-12-06 19:26:00 +0100
  * [MDEV-17917](https://jira.mariadb.org/browse/MDEV-17917) MTR: fixed race conditions in perfschema.socket\_connect, main.connect
* Merge [Revision #6491c591b2](https://github.com/MariaDB/server/commit/6491c591b2) 2018-12-06 15:08:42 +0100 - Merge branch '10.0' into 10.1
* [Revision #daca7e70d7](https://github.com/MariaDB/server/commit/daca7e70d7)\
  2018-12-06 01:17:44 +0100
  * [MDEV-17898](https://jira.mariadb.org/browse/MDEV-17898) FLUSH PRIVILEGES crashes server with segfault
* [Revision #eed0013bed](https://github.com/MariaDB/server/commit/eed0013bed)\
  2018-12-06 00:48:41 +0100
  * correct order of arguments for Dynamic\_array<>::CMP\_FUNC2
* [Revision #8a37ce0767](https://github.com/MariaDB/server/commit/8a37ce0767)\
  2018-12-06 00:48:00 +0100
  * cleanup: DYNAMIC\_ARRAY -> Dynamic\_array\<ACL\_DB> acl\_dbs
* [Revision #17e8570285](https://github.com/MariaDB/server/commit/17e8570285)\
  2018-12-05 19:27:34 +0530
  * Added a testcase for [MDEV-17734](https://jira.mariadb.org/browse/MDEV-17734)
* [Revision #14f6b0cdfd](https://github.com/MariaDB/server/commit/14f6b0cdfd)\
  2018-11-20 20:12:29 +0530
  * [MDEV-17734](https://jira.mariadb.org/browse/MDEV-17734): AddressSanitizer: use-after-poison in create\_key\_parts\_for\_pseudo\_indexes
* [Revision #328d7779bc](https://github.com/MariaDB/server/commit/328d7779bc)\
  2018-11-26 08:58:38 +0200
  * Fortify galera\_sst\_mariadb-backup\_table\_options test.
* [Revision #1037edcb11](https://github.com/MariaDB/server/commit/1037edcb11)\
  2018-11-22 16:33:20 +0200
  * [MDEV-17804](https://jira.mariadb.org/browse/MDEV-17804): Galera tests cause mysql\_socket.h:738: inline\_mysql\_socket\_send: Assertion \`mysql\_socket.fd != -1' failed.
* [Revision #244cc35e7b](https://github.com/MariaDB/server/commit/244cc35e7b)\
  2018-11-22 16:30:20 +0200
  * [MDEV-17801](https://jira.mariadb.org/browse/MDEV-17801): Galera test failure on galera\_var\_reject\_queries
* [Revision #49a50a19a1](https://github.com/MariaDB/server/commit/49a50a19a1)\
  2018-12-07 11:54:03 +0200
  * [MDEV-17923](https://jira.mariadb.org/browse/MDEV-17923) Assertion failed in trx\_undo\_page\_report\_modify after CREATE FULLTEXT INDEX
* [Revision #5ec9b88e11](https://github.com/MariaDB/server/commit/5ec9b88e11)\
  2018-12-04 15:29:49 +0200
  * Disable a frequently failing test
* [Revision #a00f8bc3ad](https://github.com/MariaDB/server/commit/a00f8bc3ad)\
  2018-12-07 12:12:29 +0400
  * Cleanup: removing unused zeroing Datetime() constructor
* [Revision #34f11b06e6](https://github.com/MariaDB/server/commit/34f11b06e6)\
  2018-10-14 20:41:49 +0200
  * Move deletion of old GTID rows to slave background thread
* [Revision #24a45d3bd7](https://github.com/MariaDB/server/commit/24a45d3bd7)\
  2018-12-06 21:51:38 +0100
  * Fix windows build : re-record .result file
* [Revision #50c850c9b1](https://github.com/MariaDB/server/commit/50c850c9b1)\
  2018-12-06 15:09:17 +0100
  * Windows : create a minimalistic MTR test for mysql\_install\_db.exe
* [Revision #f77895ebf3](https://github.com/MariaDB/server/commit/f77895ebf3)\
  2018-11-26 21:24:05 +0100
  * [MDEV-15649](https://jira.mariadb.org/browse/MDEV-15649) Speedup search in acl\_users and acl\_dbs array, sorting them by usernames first, and then by get\_sort() value.
* [Revision #bb9b4182e4](https://github.com/MariaDB/server/commit/bb9b4182e4)\
  2018-12-05 14:06:49 +0400
  * [MDEV-17906](https://jira.mariadb.org/browse/MDEV-17906) Class Binary\_string
* [Revision #24d6ec8db8](https://github.com/MariaDB/server/commit/24d6ec8db8)\
  2018-12-05 11:03:46 +0400
  * [MDEV-17907](https://jira.mariadb.org/browse/MDEV-17907) Class Static\_binary\_string
* [Revision #d6a00d9b18](https://github.com/MariaDB/server/commit/d6a00d9b18)\
  2018-12-05 08:16:24 +0400
  * [MDEV-17905](https://jira.mariadb.org/browse/MDEV-17905) Add class Charset
* [Revision #470e9a9fb6](https://github.com/MariaDB/server/commit/470e9a9fb6)\
  2018-09-17 02:51:36 -0700
  * Add CONTRIBUTING file and modify README file about live QA regarding new contributors
* [Revision #1c37ac84ef](https://github.com/MariaDB/server/commit/1c37ac84ef)\
  2018-12-04 18:11:45 +0400
  * [MDEV-8894](https://jira.mariadb.org/browse/MDEV-8894) Inserting fractional seconds into MySQL 5.6 master breaks consistency on MariaDB 10 slave
* [Revision #269da4bf19](https://github.com/MariaDB/server/commit/269da4bf19)\
  2018-12-03 21:26:07 +0400
  * [MDEV-5377](https://jira.mariadb.org/browse/MDEV-5377) Row-based replication of MariaDB temporal data types with FSP>0 into a different column type
* Merge [Revision #88a480cecb](https://github.com/MariaDB/server/commit/88a480cecb) 2018-12-04 13:22:26 +0200 - Merge 10.3 into 10.4
* Merge [Revision #b6f203984b](https://github.com/MariaDB/server/commit/b6f203984b) 2018-12-04 13:18:14 +0200 - Merge 10.2 into 10.3
* [Revision #157d3c3bc1](https://github.com/MariaDB/server/commit/157d3c3bc1)\
  2018-12-03 15:57:21 +0530
  * [MDEV-17432](https://jira.mariadb.org/browse/MDEV-17432) Assertion \`lock\_trx\_has\_sys\_table\_locks(trx) == 0' failed upon ALTER TABLE .. ADD FOREIGN KEY
* [Revision #f2c7972a3d](https://github.com/MariaDB/server/commit/f2c7972a3d)\
  2018-12-03 01:12:04 +0530
  * [MDEV-17432](https://jira.mariadb.org/browse/MDEV-17432) Assertion \`lock\_trx\_has\_sys\_table\_locks(trx) == 0' failed upon ALTER TABLE .. ADD FOREIGN KEY
* [Revision #46960365b1](https://github.com/MariaDB/server/commit/46960365b1)\
  2018-12-01 15:06:04 -0800
  * [MDEV-17871](https://jira.mariadb.org/browse/MDEV-17871) Crash when running explain with CTE
* [Revision #3e5162d814](https://github.com/MariaDB/server/commit/3e5162d814)\
  2018-11-30 15:54:21 +0200
  * Re-disable a failing test
* [Revision #7826b9b983](https://github.com/MariaDB/server/commit/7826b9b983)\
  2018-11-28 11:53:40 +0200
  * Fix syntax error on galera/disabled.def file
* [Revision #b4d102e828](https://github.com/MariaDB/server/commit/b4d102e828)\
  2018-11-27 13:16:19 +0200
  * [MDEV-17810](https://jira.mariadb.org/browse/MDEV-17810): Improve error printout when decryption fails or we identify page as both encrypted and unencrypted
* [Revision #0070830cb8](https://github.com/MariaDB/server/commit/0070830cb8)\
  2018-12-04 00:53:36 +0400
  * Enable main.connect-abstract
* [Revision #466335a44c](https://github.com/MariaDB/server/commit/466335a44c)\
  2018-12-03 13:29:27 +0400
  * [MDEV-16707](https://jira.mariadb.org/browse/MDEV-16707) Add an accessor in Item\_func\_like class for the negated attribute
* [Revision #f89a27b4e5](https://github.com/MariaDB/server/commit/f89a27b4e5)\
  2018-12-02 18:59:04 +0400
  * [MDEV-17319](https://jira.mariadb.org/browse/MDEV-17319) Assertion \`ts\_type != MYSQL\_TIMESTAMP\_TIME' failed upon inserting into TIME field
* [Revision #17e371fffe](https://github.com/MariaDB/server/commit/17e371fffe)\
  2018-11-30 21:48:45 +0200
  * More InnoDB preprocessor cleanup
* Merge [Revision #757530b83c](https://github.com/MariaDB/server/commit/757530b83c) 2018-11-30 15:50:45 +0200 - Merge 10.3 into 10.4
* [Revision #95f3c142a4](https://github.com/MariaDB/server/commit/95f3c142a4)\
  2018-11-30 15:48:33 +0200
  * [MDEV-17881](https://jira.mariadb.org/browse/MDEV-17881): Fix a debug assertion
* Merge [Revision #3afae13b54](https://github.com/MariaDB/server/commit/3afae13b54) 2018-11-30 12:47:38 +0200 - Merge 10.3 into 10.4
* [Revision #e46a3aa42e](https://github.com/MariaDB/server/commit/e46a3aa42e)\
  2018-11-30 12:40:03 +0200
  * [MDEV-17881](https://jira.mariadb.org/browse/MDEV-17881) Assertion failure in cmp\_dtuple\_rec\_with\_match\_bytes after instant ADD COLUMN
* Merge [Revision #b374246730](https://github.com/MariaDB/server/commit/b374246730) 2018-11-30 10:55:53 +0200 - Merge 10.3 into 10.4
* Merge [Revision #0abd2766b1](https://github.com/MariaDB/server/commit/0abd2766b1) 2018-11-30 09:23:23 +0200 - Merge 10.2 into 10.3
* [Revision #33fdb443ea](https://github.com/MariaDB/server/commit/33fdb443ea)\
  2018-11-27 10:52:53 +0200
  * Fix xtrabackup SST tests by using innodb-safe-truncate=OFF. Disable tests that do not yet pass.
* [Revision #447e493179](https://github.com/MariaDB/server/commit/447e493179)\
  2018-11-29 12:53:44 +0200
  * Remove some unnecessary InnoDB #include
* [Revision #be998bfdc5](https://github.com/MariaDB/server/commit/be998bfdc5)\
  2018-11-29 09:16:48 +0200
  * [MDEV-17859](https://jira.mariadb.org/browse/MDEV-17859): Clean up the FOREIGN KEY handling
* [Revision #3a393f8c84](https://github.com/MariaDB/server/commit/3a393f8c84)\
  2018-11-28 20:47:27 +0200
  * Merge dict\_index\_copy\_rec\_order\_prefix() to its only caller
* Merge [Revision #3fe0369309](https://github.com/MariaDB/server/commit/3fe0369309) 2018-11-28 19:54:48 +0200 - Merge 10.3 into 10.4
* Merge [Revision #35184902db](https://github.com/MariaDB/server/commit/35184902db) 2018-11-28 15:23:23 +0200 - Merge 10.2 into 10.3
* [Revision #b26e603aeb](https://github.com/MariaDB/server/commit/b26e603aeb)\
  2018-11-28 15:17:56 +0200
  * [MDEV-17859](https://jira.mariadb.org/browse/MDEV-17859) Operating system errors in file operations after failed CREATE
* [Revision #0485e51935](https://github.com/MariaDB/server/commit/0485e51935)\
  2018-11-28 12:38:52 +0300
  * [MDEV-13155](https://jira.mariadb.org/browse/MDEV-13155): XA recovery not supported for RocksDB
* [Revision #218c75eb1d](https://github.com/MariaDB/server/commit/218c75eb1d)\
  2018-11-28 10:46:19 +0400
  * Making the test for [MDEV-17854](https://jira.mariadb.org/browse/MDEV-17854) independent from the host time zone
* [Revision #d6bcf3a4c8](https://github.com/MariaDB/server/commit/d6bcf3a4c8)\
  2018-11-28 06:18:05 +0400
  * [MDEV-17854](https://jira.mariadb.org/browse/MDEV-17854) Assertion \`decimals <= 6' failed in my\_time\_fraction\_remainder on SELECT with NULLIF and FROM\_UNIXTIME on incorrect time
* Merge [Revision #926b04e550](https://github.com/MariaDB/server/commit/926b04e550) 2018-11-28 01:18:30 +0200 - Merge 10.3 into 10.4
* Merge [Revision #babb000a36](https://github.com/MariaDB/server/commit/babb000a36) 2018-11-28 01:02:46 +0200 - Merge 10.2 into 10.3
* [Revision #4a92165ff0](https://github.com/MariaDB/server/commit/4a92165ff0)\
  2018-11-28 00:52:30 +0200
  * Remove unused mem\_heap\_allocator
* [Revision #e82e216e37](https://github.com/MariaDB/server/commit/e82e216e37)\
  2018-11-27 14:49:20 +0200
  * [MDEV-17849](https://jira.mariadb.org/browse/MDEV-17849) Undo tablespace truncation recovery fails to shrink file
* [Revision #eb6364619f](https://github.com/MariaDB/server/commit/eb6364619f)\
  2018-11-27 14:28:07 +0200
  * Remove the redundant variable fil\_n\_file\_opened
* [Revision #b9824074a6](https://github.com/MariaDB/server/commit/b9824074a6)\
  2018-11-27 14:02:24 +0200
  * [MDEV-17851](https://jira.mariadb.org/browse/MDEV-17851) Assertion failure srv\_undo\_tablespaces > 1
* [Revision #861038f2e8](https://github.com/MariaDB/server/commit/861038f2e8)\
  2018-11-26 17:30:39 +0200
  * [MDEV-17816](https://jira.mariadb.org/browse/MDEV-17816): Follow-up fix
* [Revision #4b88d5ee51](https://github.com/MariaDB/server/commit/4b88d5ee51)\
  2018-11-27 15:26:18 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* [Revision #555921a9c3](https://github.com/MariaDB/server/commit/555921a9c3)\
  2018-11-20 10:58:34 +0100
  * [MDEV-15073](https://jira.mariadb.org/browse/MDEV-15073): Generic UDAF parser code in server for windows functions
* [Revision #a956260d82](https://github.com/MariaDB/server/commit/a956260d82)\
  2018-11-27 14:19:54 +0400
  * [MDEV-16715](https://jira.mariadb.org/browse/MDEV-16715) Add accessors for Item\_sum and Item\_func\_group\_concat classes
* [Revision #19a6a018e8](https://github.com/MariaDB/server/commit/19a6a018e8)\
  2018-11-27 14:13:31 +0400
  * [MDEV-16705](https://jira.mariadb.org/browse/MDEV-16705) Add two accessors for multi\_delete class
* [Revision #e963b0d12f](https://github.com/MariaDB/server/commit/e963b0d12f)\
  2018-11-27 14:08:03 +0400
  * [MDEV-16725](https://jira.mariadb.org/browse/MDEV-16725) Add accessor methods for classes in item\_timefunc.h
* [Revision #2dd6cd5f15](https://github.com/MariaDB/server/commit/2dd6cd5f15)\
  2018-11-27 08:06:10 +0400
  * Fixing embedded tests for [MDEV-16991](https://jira.mariadb.org/browse/MDEV-16991)
* Merge [Revision #7dcbc33db5](https://github.com/MariaDB/server/commit/7dcbc33db5) 2018-11-26 17:20:07 +0200 - Merge 10.3 into 10.4
* Merge [Revision #36359157cf](https://github.com/MariaDB/server/commit/36359157cf) 2018-11-26 16:44:11 +0200 - Merge 10.2 into 10.3
* [Revision #971e1d8677](https://github.com/MariaDB/server/commit/971e1d8677)\
  2018-11-26 16:39:36 +0200
  * [MDEV-17831](https://jira.mariadb.org/browse/MDEV-17831) TRUNCATE TABLE removes ROW\_FORMAT=COMPRESSED
* Merge [Revision #1afed20774](https://github.com/MariaDB/server/commit/1afed20774) 2018-11-26 14:05:15 +0200 - Merge 10.2 into 10.3
* [Revision #9669536c23](https://github.com/MariaDB/server/commit/9669536c23)\
  2018-11-26 12:57:35 +0200
  * [MDEV-17811](https://jira.mariadb.org/browse/MDEV-17811): Add deprecation information for xtrabackup
* [Revision #2a31b82831](https://github.com/MariaDB/server/commit/2a31b82831)\
  2018-11-26 12:50:27 +0200
  * [MDEV-17816](https://jira.mariadb.org/browse/MDEV-17816) Crash in TRUNCATE TABLE when table creation fails
* [Revision #a81fceafb1](https://github.com/MariaDB/server/commit/a81fceafb1)\
  2018-11-26 10:10:49 +0200
  * [MDEV-14409](https://jira.mariadb.org/browse/MDEV-14409) Assertion \`page\_rec\_is\_leaf(rec)' failed in lock\_rec\_validate\_page
* [Revision #3728b11f87](https://github.com/MariaDB/server/commit/3728b11f87)\
  2018-11-22 16:33:20 +0200
  * [MDEV-17804](https://jira.mariadb.org/browse/MDEV-17804): Galera tests cause mysql\_socket.h:738: inline\_mysql\_socket\_send: Assertion \`mysql\_socket.fd != -1' failed.
* [Revision #dde0a83fff](https://github.com/MariaDB/server/commit/dde0a83fff)\
  2018-11-22 16:30:20 +0200
  * [MDEV-17801](https://jira.mariadb.org/browse/MDEV-17801): Galera test failure on galera\_var\_reject\_queries
* [Revision #2b49e15686](https://github.com/MariaDB/server/commit/2b49e15686)\
  2018-11-22 10:22:00 +0200
  * [MDEV-15522](https://jira.mariadb.org/browse/MDEV-15522): Change galera suite MTR tests to use mariadb-backup instead of xtrabackup
* [Revision #00c88a7122](https://github.com/MariaDB/server/commit/00c88a7122)\
  2018-11-22 10:17:58 +0200
  * [MDEV-15522](https://jira.mariadb.org/browse/MDEV-15522): Change galera suite MTR tests to use mariadb-backup instead of xtrabackup
* [Revision #4b1b4b3920](https://github.com/MariaDB/server/commit/4b1b4b3920)\
  2018-11-22 10:16:58 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* Merge [Revision #06063e8a41](https://github.com/MariaDB/server/commit/06063e8a41) 2018-11-21 16:59:11 +0200 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #8324e5e84d](https://github.com/MariaDB/server/commit/8324e5e84d)\
  2018-11-21 09:05:47 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* [Revision #41fa9a5986](https://github.com/MariaDB/server/commit/41fa9a5986)\
  2018-11-20 07:49:46 +0200
  * Add missing .rdiff file to test galera\_sst\_xtrabackup-v2\_data\_dir for debug build.
* [Revision #6fad15d02a](https://github.com/MariaDB/server/commit/6fad15d02a)\
  2018-11-19 17:34:22 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* [Revision #ea03eac5d7](https://github.com/MariaDB/server/commit/ea03eac5d7)\
  2018-10-03 16:25:24 +0300
  * fiexed debug build failure of galera\_ist\_mariadb-backup\_innodb\_flush\_logs
* [Revision #0529c9e93e](https://github.com/MariaDB/server/commit/0529c9e93e)\
  2018-10-03 14:40:56 +0300
  * fiexed debug build failure of galera\_ist\_mariadb-backup test
* [Revision #c85912c8c6](https://github.com/MariaDB/server/commit/c85912c8c6)\
  2018-10-01 18:21:47 +0300
  * added galera\_ist\_mariadb-backup\_innodb\_flush\_logs test
* [Revision #2160e075dc](https://github.com/MariaDB/server/commit/2160e075dc)\
  2018-10-01 12:23:26 +0300
  * fixed the test comments of galera\_sst\_mariadb-backup\_encrypt\_with\_key test
* [Revision #ace0b7215e](https://github.com/MariaDB/server/commit/ace0b7215e)\
  2018-09-28 19:05:01 +0300
  * added test galera\_sst\_mariadb-backup\_encrypt\_with\_key; corrected path to galera\_ist\_mariadb-backup test
* [Revision #92e99775e9](https://github.com/MariaDB/server/commit/92e99775e9)\
  2018-09-28 17:35:28 +0300
  * added test case galera\_ist\_mariadb-backup
* [Revision #bae7c1ebd4](https://github.com/MariaDB/server/commit/bae7c1ebd4)\
  2018-09-28 15:34:57 +0300
  * added galera\_autoinc\_sst\_mariadb-backup test
* [Revision #de0eeb800e](https://github.com/MariaDB/server/commit/de0eeb800e)\
  2018-11-19 11:00:56 +0200
  * [MDEV-16890](https://jira.mariadb.org/browse/MDEV-16890): Galera test failure on galera\_sst\_mysqldump\_with\_key
* [Revision #ae0361ab39](https://github.com/MariaDB/server/commit/ae0361ab39)\
  2018-11-16 10:21:11 +0200
  * [MDEV-13881](https://jira.mariadb.org/browse/MDEV-13881): galera.partition failed in buildbot with wrong result
* [Revision #3b64663287](https://github.com/MariaDB/server/commit/3b64663287)\
  2018-11-16 14:19:58 +0200
  * Updated check-cpu from 10.3 to get it to work with gcc 7.3.1
* [Revision #06972b2fbc](https://github.com/MariaDB/server/commit/06972b2fbc)\
  2018-11-23 10:28:07 +1100
  * travis: xcode10.1
* [Revision #06e5f28f9f](https://github.com/MariaDB/server/commit/06e5f28f9f)\
  2018-11-22 17:07:35 +0200
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Remove a level of pointer indirection
* [Revision #0c69f2e1ee](https://github.com/MariaDB/server/commit/0c69f2e1ee)\
  2018-11-21 16:55:57 +0200
  * Fixed compiler warnings
* [Revision #8fe34dd45f](https://github.com/MariaDB/server/commit/8fe34dd45f)\
  2018-11-26 16:41:53 +0200
  * [MDEV-17831](https://jira.mariadb.org/browse/MDEV-17831) Assertion \`supports\_instant()' failed in dict\_table\_t::prepare\_instant upon ADD COLUMN on table with KEY\_BLOCK\_SIZE
* [Revision #4447a02cf1](https://github.com/MariaDB/server/commit/4447a02cf1)\
  2018-11-23 19:04:42 +0400
  * [MDEV-16991](https://jira.mariadb.org/browse/MDEV-16991) Rounding vs truncation for TIME, DATETIME, TIMESTAMP
* [Revision #27f3329ff6](https://github.com/MariaDB/server/commit/27f3329ff6)\
  2018-11-23 18:36:44 +0200
  * [MDEV-17813](https://jira.mariadb.org/browse/MDEV-17813): Fix the test for release builds
* [Revision #2c4844c9e7](https://github.com/MariaDB/server/commit/2c4844c9e7)\
  2018-11-23 16:22:14 +0200
  * [MDEV-17813](https://jira.mariadb.org/browse/MDEV-17813) Crash in instant ALTER TABLE due to purge concurrently emptying table
* [Revision #46a411088c](https://github.com/MariaDB/server/commit/46a411088c)\
  2018-11-22 17:29:49 +0200
  * Fix the -DWITH\_WSREP:BOOL=OFF build
* [Revision #4be0855cf5](https://github.com/MariaDB/server/commit/4be0855cf5)\
  2018-11-22 15:36:50 +0200
  * [MDEV-17794](https://jira.mariadb.org/browse/MDEV-17794) Do not assign persistent ID for temporary tables
* [Revision #23ff318d03](https://github.com/MariaDB/server/commit/23ff318d03)\
  2018-11-22 11:17:55 +0200
  * [MDEV-17793](https://jira.mariadb.org/browse/MDEV-17793) follow-up: Also update SYS\_VIRTUAL
* [Revision #740ce108a5](https://github.com/MariaDB/server/commit/740ce108a5)\
  2018-11-22 14:53:25 +0400
  * [MDEV-17792](https://jira.mariadb.org/browse/MDEV-17792) New class Timestamp and cleanups in Date, Datetime, Field for rounding
* [Revision #2ebb110c36](https://github.com/MariaDB/server/commit/2ebb110c36)\
  2018-11-22 10:41:15 +0200
  * [MDEV-17793](https://jira.mariadb.org/browse/MDEV-17793) Crash in purge after instant DROP and emptying the table
* [Revision #0fe90263c8](https://github.com/MariaDB/server/commit/0fe90263c8)\
  2018-11-22 01:08:15 +0200
  * Fixed compiler warnings in tokudb\_sysvars.cc
* [Revision #9fdb8c59eb](https://github.com/MariaDB/server/commit/9fdb8c59eb)\
  2018-11-21 13:59:04 +0200
  * [MDEV-17721](https://jira.mariadb.org/browse/MDEV-17721): Corrupted data dictionary after instant DROP COLUMN
* Merge [Revision #1ee0144db7](https://github.com/MariaDB/server/commit/1ee0144db7) 2018-11-21 12:28:00 +0200 - Merge 10.3 into 10.4
* [Revision #d07a6e33dd](https://github.com/MariaDB/server/commit/d07a6e33dd)\
  2018-11-20 17:31:07 +0100
  * Check that default() do not see invisible field.
* [Revision #02b70702d9](https://github.com/MariaDB/server/commit/02b70702d9)\
  2018-11-20 09:04:11 -0500
  * bump the VERSION
* Merge [Revision #4210e7bf6f](https://github.com/MariaDB/server/commit/4210e7bf6f) 2018-11-20 15:08:41 +0200 - Merge 10.2 into 10.3
* [Revision #b86e18cb44](https://github.com/MariaDB/server/commit/b86e18cb44)\
  2018-11-20 14:55:44 +0200
  * [MDEV-17780](https://jira.mariadb.org/browse/MDEV-17780) innodb.truncate\_recover crashes in recovery due to out-of-bounds page read
* [Revision #ae96b47f9e](https://github.com/MariaDB/server/commit/ae96b47f9e)\
  2018-11-18 17:38:48 +0200
  * [MDEV-17507](https://jira.mariadb.org/browse/MDEV-17507) Make MTR tests work for builds without Aria for temporary tables
* Merge [Revision #92996c9aa9](https://github.com/MariaDB/server/commit/92996c9aa9) 2018-11-20 15:08:30 +0200 - Merge bb-10.3-release into 10.3
* [Revision #ae2004c616](https://github.com/MariaDB/server/commit/ae2004c616)\
  2018-11-21 12:24:49 +0200
  * [MDEV-17721](https://jira.mariadb.org/browse/MDEV-17721): Corrupted data dictionary after instant DROP COLUMN
* [Revision #ce32cae207](https://github.com/MariaDB/server/commit/ce32cae207)\
  2018-11-21 11:29:01 +0400
  * Fixing compilation failure on Windows introduced by [MDEV-17776](https://jira.mariadb.org/browse/MDEV-17776)
* [Revision #f0f0d07250](https://github.com/MariaDB/server/commit/f0f0d07250)\
  2018-11-16 18:28:01 +0100
  * [MDEV-14500](https://jira.mariadb.org/browse/MDEV-14500) filesort to support engines with slow rnd\_pos
* [Revision #cd29aee50d](https://github.com/MariaDB/server/commit/cd29aee50d)\
  2018-11-16 18:24:58 +0100
  * misc cleanup
* [Revision #1823ce7304](https://github.com/MariaDB/server/commit/1823ce7304)\
  2018-11-16 18:24:22 +0100
  * cleanup: rename a flag, keep old name for compatibility
* [Revision #649465db41](https://github.com/MariaDB/server/commit/649465db41)\
  2018-11-16 18:23:15 +0100
  * cleanup: remove HA\_WANTS\_PRIMARY\_KEY as redundant
* [Revision #5aaee3746e](https://github.com/MariaDB/server/commit/5aaee3746e)\
  2018-11-20 13:32:20 +0200
  * [MDEV-17721](https://jira.mariadb.org/browse/MDEV-17721): Corrupted data dictionary after instant DROP COLUMN
* [Revision #21a5884081](https://github.com/MariaDB/server/commit/21a5884081)\
  2018-11-20 13:47:52 +0400
  * [MDEV-17776](https://jira.mariadb.org/browse/MDEV-17776) CAST(x AS INTERVAL DAY\_SECOND(N))
* Merge [Revision #dde2ca4aa1](https://github.com/MariaDB/server/commit/dde2ca4aa1) 2018-11-19 19:58:27 +0200 - Merge 10.3 into 10.4
* Merge [Revision #fd58bb71e2](https://github.com/MariaDB/server/commit/fd58bb71e2) 2018-11-19 18:45:53 +0200 - Merge 10.2 into 10.3
* [Revision #e669e705a1](https://github.com/MariaDB/server/commit/e669e705a1)\
  2018-11-19 13:13:39 +0200
  * Fix the Windows build
* [Revision #ff88e4bb8a](https://github.com/MariaDB/server/commit/ff88e4bb8a)\
  2018-11-19 11:42:14 +0200
  * Remove many redundant #include from InnoDB
* [Revision #cb5bca721b](https://github.com/MariaDB/server/commit/cb5bca721b)\
  2018-11-19 11:40:10 +0200
  * [MDEV-17765](https://jira.mariadb.org/browse/MDEV-17765) lock\_discard\_page() may fail to discard locks for SPATIAL INDEX
* [Revision #f037b91098](https://github.com/MariaDB/server/commit/f037b91098)\
  2018-11-19 11:11:53 +0200
  * [MDEV-17726](https://jira.mariadb.org/browse/MDEV-17726): Fix compiler warning
* [Revision #ab812c1089](https://github.com/MariaDB/server/commit/ab812c1089)\
  2018-11-16 10:36:57 +0200
  * [MDEV-17726](https://jira.mariadb.org/browse/MDEV-17726): A better fix
* [Revision #705abdebaf](https://github.com/MariaDB/server/commit/705abdebaf)\
  2018-11-16 10:39:08 +0530
  * [MDEV-13170](https://jira.mariadb.org/browse/MDEV-13170): Database service (MySQL) stops after update with trigger
* [Revision #37d6d3b661](https://github.com/MariaDB/server/commit/37d6d3b661)\
  2018-11-16 16:54:33 +0200
  * Max transid was not stored directly after Aria recovery
* [Revision #a93ac8d95f](https://github.com/MariaDB/server/commit/a93ac8d95f)\
  2018-11-13 13:10:32 +0100
  * [MDEV-16448](https://jira.mariadb.org/browse/MDEV-16448) mysql\_upgrade\_service remove my.ini variables that are no more valid [MDEV-16447](https://jira.mariadb.org/browse/MDEV-16447) incorporate Innodb slow shutdown into mysql\_upgrade\_service.exe
* [Revision #efc235d84d](https://github.com/MariaDB/server/commit/efc235d84d)\
  2018-11-12 17:11:14 +0100
  * Fix test result.
* [Revision #b5ac863f14](https://github.com/MariaDB/server/commit/b5ac863f14)\
  2018-11-19 12:41:01 +0400
  * Grammar cleanup: adding missing and removing redundant semicolons
* [Revision #7debbd7859](https://github.com/MariaDB/server/commit/7debbd7859)\
  2018-11-18 15:50:43 +0200
  * Fix a compilation error
* [Revision #075820ab23](https://github.com/MariaDB/server/commit/075820ab23)\
  2018-11-18 15:27:50 +0200
  * [MDEV-17750](https://jira.mariadb.org/browse/MDEV-17750): Fix the Windows build
* [Revision #d2ba9edd66](https://github.com/MariaDB/server/commit/d2ba9edd66)\
  2018-11-16 19:18:17 +0400
  * [MDEV-17740](https://jira.mariadb.org/browse/MDEV-17740) Extend EXTRACT(x AS DAY\*) to understand long time intervals
* [Revision #f92d223fe2](https://github.com/MariaDB/server/commit/f92d223fe2)\
  2018-11-16 19:36:04 +0200
  * [MDEV-17750](https://jira.mariadb.org/browse/MDEV-17750): Remove dict\_index\_get\_sys\_col\_pos()
* [Revision #eea0c3c3e7](https://github.com/MariaDB/server/commit/eea0c3c3e7)\
  2018-11-16 19:31:58 +0200
  * [MDEV-17750](https://jira.mariadb.org/browse/MDEV-17750): Remove unnecessary rec\_get\_offsets() in IMPORT TABLESPACE
* [Revision #3773bc594d](https://github.com/MariaDB/server/commit/3773bc594d)\
  2018-11-16 18:19:12 +0200
  * [MDEV-17750](https://jira.mariadb.org/browse/MDEV-17750): Avoid some rec\_get\_offsets() for accessing FTS\_DOC\_ID
* [Revision #0cbf578ac8](https://github.com/MariaDB/server/commit/0cbf578ac8)\
  2018-11-16 20:10:33 +0200
  * Add dict\_index\_t member functions for determining index type
* [Revision #16d43150ae](https://github.com/MariaDB/server/commit/16d43150ae)\
  2018-11-16 16:25:43 +0200
  * [MDEV-17721](https://jira.mariadb.org/browse/MDEV-17721) Corrupted data dictionary after instant ADD COLUMN
* [Revision #f85012246c](https://github.com/MariaDB/server/commit/f85012246c)\
  2018-11-16 13:28:37 +0200
  * [MDEV-17735](https://jira.mariadb.org/browse/MDEV-17735) Assertion failure in row\_parse\_int() on first ADD/DROP COLUMN
* [Revision #89337d510e](https://github.com/MariaDB/server/commit/89337d510e)\
  2018-06-25 22:31:32 +0300
  * [MDEV-16580](https://jira.mariadb.org/browse/MDEV-16580) Remove unused monitor counters from InnoDB
* [Revision #c75a277afe](https://github.com/MariaDB/server/commit/c75a277afe)\
  2018-11-16 10:09:12 +0400
  * A cleanup for "[MDEV-17477](https://jira.mariadb.org/browse/MDEV-17477) Wrong result for TIME('-2001-01-01 10:20:30')"
* [Revision #b9a9055793](https://github.com/MariaDB/server/commit/b9a9055793)\
  2018-11-14 16:00:38 +0400
  * [MDEV-17712](https://jira.mariadb.org/browse/MDEV-17712) Remove C\_TIME\_FUZZY\_DATES, C\_TIME\_DATETIME\_ONLY, C\_TIME\_TIME\_ONLY
* [Revision #62bcd74712](https://github.com/MariaDB/server/commit/62bcd74712)\
  2018-11-14 07:38:28 +0400
  * [MDEV-17694](https://jira.mariadb.org/browse/MDEV-17694) Add method LEX::sp\_proc\_stmt\_statement\_finalize()
* [Revision #fde5386d16](https://github.com/MariaDB/server/commit/fde5386d16)\
  2018-11-12 17:01:56 +0200
  * Add dict\_table\_t::not\_redundant()
* [Revision #92f6c23407](https://github.com/MariaDB/server/commit/92f6c23407)\
  2018-11-12 16:42:56 +0200
  * [MDEV-17138](https://jira.mariadb.org/browse/MDEV-17138): Adjust a test
* [Revision #3ea7de9a78](https://github.com/MariaDB/server/commit/3ea7de9a78)\
  2018-11-09 18:00:07 +0200
  * [MDEV-15562](https://jira.mariadb.org/browse/MDEV-15562) post-push cleanup
* [Revision #7810a4f4a2](https://github.com/MariaDB/server/commit/7810a4f4a2)\
  2018-11-09 17:33:54 +0200
  * Fix embedded test results
* [Revision #409e70e231](https://github.com/MariaDB/server/commit/409e70e231)\
  2018-11-09 09:53:56 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
