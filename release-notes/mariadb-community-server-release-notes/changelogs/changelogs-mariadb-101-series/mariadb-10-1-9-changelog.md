# MariaDB 10.1.9 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.9)[Release Notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-9-release-notes.md)[Changelog](mariadb-10-1-9-changelog.md)[Overview of 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)

**Release date:** 23 Nov 2015

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-9-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #370a2cb](https://github.com/MariaDB/server/commit/370a2cb)\
  2015-11-20 19:49:16 -0500
  * Fix syntax error in wsrep\_sst\_common.sh
* [Revision #2fc3dc3](https://github.com/MariaDB/server/commit/2fc3dc3)\
  2015-11-20 09:31:13 +0100
  * Merge branch '10.1' into bb-10.1-serg
* [Revision #e52c753](https://github.com/MariaDB/server/commit/e52c753)\
  2015-11-20 09:15:30 +0100
  * cleanup
* [Revision #df25018](https://github.com/MariaDB/server/commit/df25018)\
  2015-11-19 12:52:55 -0500
  * [MDEV-6264](https://jira.mariadb.org/browse/MDEV-6264): CentOS missing lsof as dependency for MariaDB-server (10.1)
* [Revision #87c3068](https://github.com/MariaDB/server/commit/87c3068)\
  2015-11-19 21:20:14 +0100
  * update test results
* [Revision #1e156e1](https://github.com/MariaDB/server/commit/1e156e1)\
  2015-11-20 10:00:06 +0200
  * Fixed compile warnings on Solaris
* [Revision #981b474](https://github.com/MariaDB/server/commit/981b474)\
  2015-11-20 09:57:58 +0200
  * Updated configure.pl to new plugin syntax --with-plugin-name=xxxx --with-plugins= now uses =AUTO instead of =1
* [Revision #fdba672](https://github.com/MariaDB/server/commit/fdba672)\
  2015-11-19 18:13:01 +0100
  * Post-merge fixes for Connect engine
* [Revision #e3d37bf](https://github.com/MariaDB/server/commit/e3d37bf)\
  2015-11-19 18:09:06 +0100
  * Merge branch 'connect/10.1' into 10.1
* [Revision #7f19330](https://github.com/MariaDB/server/commit/7f19330)\
  2015-11-19 17:48:36 +0100
  * Merge branch 'github/10.0-galera' into 10.1
* [Revision #4046ed1](https://github.com/MariaDB/server/commit/4046ed1)\
  2015-11-19 17:04:19 +0100
  * rbr and savepoint in a subtatement
* [Revision #33ab30d](https://github.com/MariaDB/server/commit/33ab30d)\
  2015-11-19 16:39:40 +0100
  * fix tokudb compilation with bundled zlib
* [Revision #d4017d4](https://github.com/MariaDB/server/commit/d4017d4)\
  2015-11-17 13:39:04 +0100
  * fix for windows builders
* [Revision #c99fba2](https://github.com/MariaDB/server/commit/c99fba2)\
  2015-11-16 22:13:28 +0100
  * compilation warning
* [Revision #beded7d](https://github.com/MariaDB/server/commit/beded7d)\
  2015-11-19 15:52:14 +0100
  * Merge branch '10.0' into 10.1
* [Revision #af71da5](https://github.com/MariaDB/server/commit/af71da5)\
  2015-11-19 14:01:16 +0100
  * remove duplicated like
* [Revision #2553f14](https://github.com/MariaDB/server/commit/2553f14)\
  2015-11-19 10:17:40 +0100
  * fix feedback plugin not to crash in debug builds
* [Revision #ab476a8](https://github.com/MariaDB/server/commit/ab476a8)\
  2015-11-18 22:03:02 +0100
  * Merge branch '5.5' into 10.0
* [Revision #f91798d](https://github.com/MariaDB/server/commit/f91798d)\
  2015-11-18 21:31:45 +0300
  * [MDEV-7370](https://jira.mariadb.org/browse/MDEV-7370): Server deadlocks on renaming a table for which persistent statistics exists
* [Revision #c2ec897](https://github.com/MariaDB/server/commit/c2ec897)\
  2015-11-18 17:42:39 +0200
  * Fixed buildbot failures on Solaris 64 bit
* [Revision #f383cbc](https://github.com/MariaDB/server/commit/f383cbc)\
  2015-11-18 14:46:30 +0200
  * Added some selects to rpl\_parallel2.test to find out where it fails in buildbot
* [Revision #43a5090](https://github.com/MariaDB/server/commit/43a5090)\
  2015-11-18 11:20:59 +0100
  * [MDEV-9051](https://jira.mariadb.org/browse/MDEV-9051) mysqld got signal 11, after upgrade to 10.1.8
* [Revision #7261629](https://github.com/MariaDB/server/commit/7261629)\
  2015-11-18 10:58:51 +0100
  * feedback plugin debug
* [Revision #f47124c](https://github.com/MariaDB/server/commit/f47124c)\
  2015-11-18 02:11:20 -0500
  * Incorrect statements binlogged on slave with do\_domain\_ids=(...)
* [Revision #dd90dae](https://github.com/MariaDB/server/commit/dd90dae)\
  2015-11-17 18:33:08 +0100
  * [MDEV-7588](https://jira.mariadb.org/browse/MDEV-7588) Add thd\_wait\_begin/end to notify threadpool of binlog waits
* [Revision #836275b](https://github.com/MariaDB/server/commit/836275b)\
  2015-11-17 00:42:18 +0400
  * [MDEV-4829](https://jira.mariadb.org/browse/MDEV-4829) BEFORE INSERT triggers dont issue 1406 error. Turn the 'abort\_on\_warning' on for assigning value to fields.
* [Revision #e669a5f](https://github.com/MariaDB/server/commit/e669a5f)\
  2015-11-17 18:33:08 +0100
  * [MDEV-7588](https://jira.mariadb.org/browse/MDEV-7588) Add thd\_wait\_begin/end to notify threadpool of binlog waits
* [Revision #905613f](https://github.com/MariaDB/server/commit/905613f)\
  2015-11-17 18:19:59 +0200
  * Fixed wrong tests found by buildbot
* [Revision #19d99fa](https://github.com/MariaDB/server/commit/19d99fa)\
  2015-11-16 15:41:09 +0100
  * [MDEV-8734](https://jira.mariadb.org/browse/MDEV-8734) mysqlbinlog --start-position isn't bigint
* [Revision #c0216f1](https://github.com/MariaDB/server/commit/c0216f1)\
  2015-11-17 09:45:55 +0200
  * [MDEV-9099](https://jira.mariadb.org/browse/MDEV-9099): Test encryption.innodb\_encryption\_discard\_import fails on buildbot
* [Revision #f4421c8](https://github.com/MariaDB/server/commit/f4421c8)\
  2015-11-16 12:39:56 -0500
  * Fix for some failing tests.
* [Revision #c78fc8b](https://github.com/MariaDB/server/commit/c78fc8b)\
  2015-11-16 12:35:06 -0500
  * MTR: rsync process is left running if pid file is removed
* [Revision #3228ad3](https://github.com/MariaDB/server/commit/3228ad3)\
  2015-11-13 19:21:45 +0100
  * [MDEV-8973](https://jira.mariadb.org/browse/MDEV-8973) Build failure on missing alloca.h
* [Revision #0c5f36d](https://github.com/MariaDB/server/commit/0c5f36d)\
  2015-11-13 18:41:11 +0100
  * [MDEV-8969](https://jira.mariadb.org/browse/MDEV-8969) groonga is compiled even with -DPLUGIN\_MROONGA=NO
* [Revision #12c32bd](https://github.com/MariaDB/server/commit/12c32bd)\
  2015-11-13 18:41:58 +0100
  * [MDEV-8962](https://jira.mariadb.org/browse/MDEV-8962) TokuDB tries to build on OS X, even when disabled in compile flag
* [Revision #2963381](https://github.com/MariaDB/server/commit/2963381)\
  2015-11-13 17:53:16 +0100
  * [MDEV-8453](https://jira.mariadb.org/browse/MDEV-8453) Alter table not returning engine errors
* [Revision #daf3551](https://github.com/MariaDB/server/commit/daf3551)\
  2015-11-11 15:48:08 +0100
  * add missing DBUG\_RETURN-s
* [Revision #2e0ac16](https://github.com/MariaDB/server/commit/2e0ac16)\
  2015-11-10 17:01:14 +0100
  * remove obsolete workaround
* [Revision #da95731](https://github.com/MariaDB/server/commit/da95731)\
  2015-11-10 16:57:44 +0100
  * compiler warning (no return in non-void function)
* [Revision #29dd634](https://github.com/MariaDB/server/commit/29dd634)\
  2015-11-10 16:57:15 +0100
  * dbug: correct trace for DBUG\_RETURN(func()); -- gcc only
* [Revision #8f60656](https://github.com/MariaDB/server/commit/8f60656)\
  2015-11-06 16:43:40 +0100
  * [MDEV-9039](https://jira.mariadb.org/browse/MDEV-9039) Can't upgrade MariaDB to 10.1.8 version from 10.0.21
* [Revision #a716433](https://github.com/MariaDB/server/commit/a716433)\
  2015-11-03 20:59:36 +0100
  * [MDEV-7298](https://jira.mariadb.org/browse/MDEV-7298) plugins.cracklib\_password\_check test fails
* [Revision #4165961](https://github.com/MariaDB/server/commit/4165961)\
  2015-10-16 01:07:06 +0200
  * disable innodb on sol10-64
* [Revision #dcb7996](https://github.com/MariaDB/server/commit/dcb7996)\
  2015-11-15 17:24:47 -0500
  * Fix/disable failing tests.
* [Revision #0dfa0ee](https://github.com/MariaDB/server/commit/0dfa0ee)\
  2015-11-15 10:44:20 +0100
  * [MDEV-8957](https://jira.mariadb.org/browse/MDEV-8957) \[PATCH] Useless ssl\_ctx\_set\_tmp\_dh call in libmysql
* [Revision #d85490a](https://github.com/MariaDB/server/commit/d85490a)\
  2015-11-14 10:19:53 +0100
  * Merge branch 'bb-10.1-knielsen' into 10.1
* [Revision #4008a3e](https://github.com/MariaDB/server/commit/4008a3e)\
  2015-11-14 10:11:09 +0100
  * Merge branch 'bb-10.0-knielsen' into 10.0
* [Revision #063a51c](https://github.com/MariaDB/server/commit/063a51c)\
  2015-11-14 07:21:03 +0200
  * Fixed buildbot failures with system\_mysql\_db\_fix
* [Revision #a9cda44](https://github.com/MariaDB/server/commit/a9cda44)\
  2015-11-13 23:43:11 +0200
  * [MDEV-8066](https://jira.mariadb.org/browse/MDEV-8066) Crash on unloading semisync\_master plugin
* [Revision #1774230](https://github.com/MariaDB/server/commit/1774230)\
  2015-11-13 19:47:31 +0200
  * Fixed regexp to fix buildbot failures
* [Revision #e46c8bb](https://github.com/MariaDB/server/commit/e46c8bb)\
  2015-11-13 15:32:55 +0100
  * Merge branch 'mdev7818-4' into bb-10.1-knielsen
* [Revision #65986b8](https://github.com/MariaDB/server/commit/65986b8)\
  2015-11-13 15:30:48 +0100
  * Merge branch 'mdev7818-4' into bb-10.0-knielsen
* [Revision #d5d87c9](https://github.com/MariaDB/server/commit/d5d87c9)\
  2015-11-13 15:30:37 +0100
  * Fix embedded server build after [MDEV-7818](https://jira.mariadb.org/browse/MDEV-7818) patch
* [Revision #8f2e05f](https://github.com/MariaDB/server/commit/8f2e05f)\
  2015-11-13 14:24:40 +0100
  * Merge branch 'mdev7818-4' into 10.1
* [Revision #6bf88cd](https://github.com/MariaDB/server/commit/6bf88cd)\
  2015-11-13 14:08:38 +0100
  * Merge branch 'mdev7818-4' into bb-10.0-knielsen
* [Revision #1e63a81](https://github.com/MariaDB/server/commit/1e63a81)\
  2015-11-13 15:07:45 +0200
  * Follow-up for a change [MDEV-9040](https://jira.mariadb.org/browse/MDEV-9040): fixed the 32-bit rdiff
* [Revision #ba02550](https://github.com/MariaDB/server/commit/ba02550)\
  2015-10-22 11:18:34 +0200
  * [MDEV-7818](https://jira.mariadb.org/browse/MDEV-7818): Deadlock occurring with parallel replication and FTWRL
* [Revision #6d96fab](https://github.com/MariaDB/server/commit/6d96fab)\
  2015-05-28 12:32:19 +0200
  * [MDEV-7818](https://jira.mariadb.org/browse/MDEV-7818): Deadlock occurring with parallel replication and FTWRL
* [Revision #75dc267](https://github.com/MariaDB/server/commit/75dc267)\
  2015-10-22 10:28:51 +0200
  * Change Seconds\_behind\_master to be updated only at commit in parallel replication
* [Revision #2828c2b](https://github.com/MariaDB/server/commit/2828c2b)\
  2015-11-13 03:23:22 +0200
  * [MDEV-9124](https://jira.mariadb.org/browse/MDEV-9124) mysqldump does not dump data if table name is same as view earlier on
* [Revision #2776159](https://github.com/MariaDB/server/commit/2776159)\
  2015-11-12 22:21:47 +0300
  * [MDEV-7383](https://jira.mariadb.org/browse/MDEV-7383): Update test results
* [Revision #73d4c4d](https://github.com/MariaDB/server/commit/73d4c4d)\
  2015-11-12 15:16:53 +0200
  * Remove compiler warning
* [Revision #e8c1b35](https://github.com/MariaDB/server/commit/e8c1b35)\
  2015-11-12 14:51:01 +0200
  * [MDEV-8476](https://jira.mariadb.org/browse/MDEV-8476) Race condition in slave SQL thread shutdown Patch backported from [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)
* [Revision #83ed38d](https://github.com/MariaDB/server/commit/83ed38d)\
  2015-05-11 20:18:30 +0800
  * fix [MDEV-8140](https://jira.mariadb.org/browse/MDEV-8140)
* [Revision #a430df3](https://github.com/MariaDB/server/commit/a430df3)\
  2015-11-10 17:47:39 +0100
  * Fix compile error on Windows
* [Revision #6c8f650](https://github.com/MariaDB/server/commit/6c8f650)\
  2015-11-09 16:17:17 +0100
  * [MDEV-9089](https://jira.mariadb.org/browse/MDEV-9089) Server crashes in MDL\_key::mdl\_key\_init (main.lowercase\_table4 test fails)
* [Revision #3f24cf2](https://github.com/MariaDB/server/commit/3f24cf2)\
  2015-11-10 13:47:28 +0200
  * Don't delete non existing .TMD and .OLD files for Aria internal temporary tables (Simple speedup)
* [Revision #65151e0](https://github.com/MariaDB/server/commit/65151e0)\
  2015-11-10 13:42:35 +0200
  * Change stage\_copying\_to\_tmp\_table to stage\_creating\_tmp\_table like in MySQL. (We were using stage\_copying\_to\_tmp\_table twice)
* [Revision #2f63e2e](https://github.com/MariaDB/server/commit/2f63e2e)\
  2015-11-10 13:40:15 +0200
  * [MDEV-8426](https://jira.mariadb.org/browse/MDEV-8426) mysqlbinlog: "Corrupted replication event was detected. Not printing the value" with binlog-row-image=minimal"
* [Revision #7877118](https://github.com/MariaDB/server/commit/7877118)\
  2015-11-09 15:07:13 +0200
  * Ignore MySQL 5.7 log events not relevant for MariaDB - XA - Transaction\_context\_event (used by MysQL group replication) - View change event (used by MysQL group replication)
* [Revision #78ffeaa](https://github.com/MariaDB/server/commit/78ffeaa)\
  2015-11-06 14:42:43 +0200
  * Fix that one can run rpl\_binlog\_errors with --debug
* [Revision #05ed9fec](https://github.com/MariaDB/server/commit/05ed9fec)\
  2015-11-06 13:18:40 +0200
  * Use MEM\_CHECK\_DEFINED to check if blocks contain uninitialized data Fixed failure in tests when running optimized code - Some assert() was using code that had to be executed Fixed copying of some uninitialized data (fixed valgrind warning)
* [Revision #e3868ee](https://github.com/MariaDB/server/commit/e3868ee)\
  2015-11-06 13:02:19 +0200
  * Don't store vcol bitmaps in TABLE if table doesn't have virtual fields. (Makes TABLE a bit smaller)
* [Revision #93d1e5c](https://github.com/MariaDB/server/commit/93d1e5c)\
  2015-11-05 22:09:58 +0200
  * table->write\_set was changed if binary logging was used, which caused the changes in query execution plans. Fixed by introducing table->rpl\_write\_set which holds which columns should be stored in the binary log.
* [Revision #cb4737c](https://github.com/MariaDB/server/commit/cb4737c)\
  2015-11-02 10:35:59 +0200
  * Fixed compiler warning
* [Revision #7cd2095](https://github.com/MariaDB/server/commit/7cd2095)\
  2015-10-23 18:44:13 +0300
  * Sage cleanup in heap storage engine Removed old not needed code withing #if Changed 0x%lx to %p
* [Revision #7e4da9b](https://github.com/MariaDB/server/commit/7e4da9b)\
  2015-11-06 16:36:41 +0100
  * DEV-8632 Segmentation fault on INSERT
* [Revision #9f862ce](https://github.com/MariaDB/server/commit/9f862ce)\
  2015-11-09 17:58:35 +0300
  * [MDEV-7383](https://jira.mariadb.org/browse/MDEV-7383): engine-independent-stats column\_stats has limited values for max/min values
* [Revision #7ec6558](https://github.com/MariaDB/server/commit/7ec6558)\
  2015-11-06 14:38:03 -0500
  * [MDEV-9021](https://jira.mariadb.org/browse/MDEV-9021): MYSQLD SEGFAULTS WHEN BUILT USING --WITH-MAX-INDEXES=128
* [Revision #1694d81](https://github.com/MariaDB/server/commit/1694d81)\
  2015-11-09 12:29:26 +0100
  * [MDEV-8533](https://jira.mariadb.org/browse/MDEV-8533) Debug embedded server does not build on Windows
* [Revision #5d754fc](https://github.com/MariaDB/server/commit/5d754fc)\
  2015-11-09 09:23:32 +0200
  * [MDEV-8854](https://jira.mariadb.org/browse/MDEV-8854): New warning messages are unreadable
* [Revision #ad916ef](https://github.com/MariaDB/server/commit/ad916ef)\
  2015-11-08 14:56:48 +0100
  * Merge branch 'ob-10.1' into 10.1
* [Revision #0a85259](https://github.com/MariaDB/server/commit/0a85259)\
  2015-11-08 14:54:56 +0100
  * PATCH-P0-FIX-UPSTREAM: Fix possible buffer overflow ([MDEV-8317](https://jira.mariadb.org/browse/MDEV-8317)) Maintainer: Michal Hrusecky [Michal.Hrusecky@opensuse.org](mailto:Michal.Hrusecky@opensuse.org) (modified by O. Bertrand --> adding and using the XSTR macro)
* [Revision #d6b430c](https://github.com/MariaDB/server/commit/d6b430c)\
  2015-11-07 13:40:44 +1100
  * [MDEV-8995](https://jira.mariadb.org/browse/MDEV-8995): systemd - 16K open-files-limit by default
* [Revision #99283ba](https://github.com/MariaDB/server/commit/99283ba)\
  2015-11-06 20:02:45 -0500
  * [MDEV-8974](https://jira.mariadb.org/browse/MDEV-8974): boostrap systemd service for galera is confusing
* [Revision #c88ca2c](https://github.com/MariaDB/server/commit/c88ca2c)\
  2015-11-06 17:56:56 +0100
  * [MDEV-8701](https://jira.mariadb.org/browse/MDEV-8701) Crash on derived query [MDEV-8938](https://jira.mariadb.org/browse/MDEV-8938) Server Crash on Update with joins
* [Revision #f1daf9c](https://github.com/MariaDB/server/commit/f1daf9c)\
  2015-11-06 17:24:23 +0100
  * [MDEV-9024](https://jira.mariadb.org/browse/MDEV-9024) Build fails with VS2015
* [Revision #125cf48](https://github.com/MariaDB/server/commit/125cf48)\
  2015-11-06 17:52:57 +0200
  * Fixed engine test results in accordance with changes made in scope of commit 6b20342651bb5207b6c125d2d11b664a1bebcc41
* [Revision #4e42168](https://github.com/MariaDB/server/commit/4e42168)\
  2015-11-06 16:35:00 +0300
  * Merge pull request #112 from openquery/[MDEV-8981](https://jira.mariadb.org/browse/MDEV-8981)
* [Revision #a36048d](https://github.com/MariaDB/server/commit/a36048d)\
  2015-11-06 12:26:03 +0400
  * [MDEV-7550](https://jira.mariadb.org/browse/MDEV-7550) TokuDB crashes in build tests on Launchpad
* [Revision #b80cc31](https://github.com/MariaDB/server/commit/b80cc31)\
  2015-11-05 13:57:24 +0400
  * [MDEV-9082](https://jira.mariadb.org/browse/MDEV-9082) - Debian: mysql\_install\_db is called on upgrade
* [Revision #7f5e005](https://github.com/MariaDB/server/commit/7f5e005)\
  2015-11-04 20:13:15 +0400
  * [MDEV-9080](https://jira.mariadb.org/browse/MDEV-9080) - Debian: incorrect empty password check in postinst
* [Revision #60ad339](https://github.com/MariaDB/server/commit/60ad339)\
  2015-11-03 14:02:49 +0400
  * [MDEV-8437](https://jira.mariadb.org/browse/MDEV-8437) - plugin variables conflict with bootstrap
* [Revision #8e40f9b](https://github.com/MariaDB/server/commit/8e40f9b)\
  2015-11-03 12:08:23 +0400
  * [MDEV-8437](https://jira.mariadb.org/browse/MDEV-8437) - plugin variables conflict with bootstrap
* [Revision #5079d69](https://github.com/MariaDB/server/commit/5079d69)\
  2015-11-05 21:52:19 -0500
  * [MDEV-8975](https://jira.mariadb.org/browse/MDEV-8975): 10.1 Fails To Join Existing Galera Cluster
* [Revision #5041de9](https://github.com/MariaDB/server/commit/5041de9)\
  2015-11-03 09:31:20 +0100
  * [MDEV-8701](https://jira.mariadb.org/browse/MDEV-8701) Crash on derived query
* [Revision #d911971](https://github.com/MariaDB/server/commit/d911971)\
  2015-11-03 18:14:13 +0100
  * [MDEV-9041](https://jira.mariadb.org/browse/MDEV-9041) connect-timeout has no effect on Windows
* [Revision #25f8738](https://github.com/MariaDB/server/commit/25f8738)\
  2015-11-05 09:42:23 +0200
  * [MDEV-9040](https://jira.mariadb.org/browse/MDEV-9040): 10.1.8 fails after upgrade from 10.0.21
* [Revision #e947a52](https://github.com/MariaDB/server/commit/e947a52)\
  2015-11-04 21:58:07 -0500
  * Update global\_suppressions.
* [Revision #2399f1a](https://github.com/MariaDB/server/commit/2399f1a)\
  2015-11-04 21:56:46 -0500
  * Fix for build failure.
* [Revision #f9e320c](https://github.com/MariaDB/server/commit/f9e320c)\
  2015-11-04 15:00:34 -0500
  * [MDEV-9026](https://jira.mariadb.org/browse/MDEV-9026): Revert patch for [MDEV-6069](https://jira.mariadb.org/browse/MDEV-6069)
* [Revision #1216429](https://github.com/MariaDB/server/commit/1216429)\
  2015-11-04 13:17:40 +0100
  * [MDEV-8738](https://jira.mariadb.org/browse/MDEV-8738) Application Verifier stop during server shutdown
* [Revision #95289e5](https://github.com/MariaDB/server/commit/95289e5)\
  2015-11-03 11:55:30 -0500
  * Revert "[MDEV-6069](https://jira.mariadb.org/browse/MDEV-6069): Remove old logic for 3.23-to-higher upgrades from upgrade SQL scripts"
* [Revision #d68b083](https://github.com/MariaDB/server/commit/d68b083)\
  2015-11-03 11:54:37 -0500
  * Revert "[MDEV-6069](https://jira.mariadb.org/browse/MDEV-6069): Remove old logic for 3.23-to-higher upgrades from upgrade SQL scripts"
* [Revision #245bfc5](https://github.com/MariaDB/server/commit/245bfc5)\
  2015-11-03 17:41:06 +0100
  * [MDEV-8669](https://jira.mariadb.org/browse/MDEV-8669) MTR client connections on Windows became much slower. The regression is caused by change bind-address server parameter in [MDEV-8083](https://jira.mariadb.org/browse/MDEV-8083), so now server listens on IPv4 only by default.
* [Revision #6189951](https://github.com/MariaDB/server/commit/6189951)\
  2015-11-03 16:03:25 +0200
  * [MDEV-9063](https://jira.mariadb.org/browse/MDEV-9063): encryption.innodb-log-encrypt produces warnings in error logs on builds with bundled SSL
* [Revision #a574407](https://github.com/MariaDB/server/commit/a574407)\
  2015-11-02 23:19:37 -0500
  * [MDEV-9007](https://jira.mariadb.org/browse/MDEV-9007): Bootstrap does not work in CentOS start script
* [Revision #d8ecc2a](https://github.com/MariaDB/server/commit/d8ecc2a)\
  2015-10-25 11:22:12 +1100
  * [MDEV-9007](https://jira.mariadb.org/browse/MDEV-9007): systemd - service mariadb bootstrap
* [Revision #a2c3549](https://github.com/MariaDB/server/commit/a2c3549)\
  2015-10-15 15:38:45 +0200
  * [MDEV-427](https://jira.mariadb.org/browse/MDEV-427): systemd - use galera\_new\_cluster instead of bootstrap
* [Revision #7877438](https://github.com/MariaDB/server/commit/7877438)\
  2015-11-03 03:25:38 +0200
  * Increased the version number
* [Revision #641644a](https://github.com/MariaDB/server/commit/641644a)\
  2015-11-01 20:37:23 +0400
  * [MDEV-8992](https://jira.mariadb.org/browse/MDEV-8992) MariaDB crashes when accessing table with GIS features. we don't test for not-existing gis extra in FRM.
* [Revision #4d15112](https://github.com/MariaDB/server/commit/4d15112)\
  2015-10-31 18:07:02 -0400
  * Merge tag 'mariadb-10.0.22' into 10.0-galera
* [Revision #3e043b3](https://github.com/MariaDB/server/commit/3e043b3)\
  2015-10-30 12:10:54 -0400
  * [MDEV-8991](https://jira.mariadb.org/browse/MDEV-8991): bind-address appears twice in default my.cnf
* [Revision #fa1438c](https://github.com/MariaDB/server/commit/fa1438c)\
  2015-10-27 11:17:52 +0100
  * [MDEV-8913](https://jira.mariadb.org/browse/MDEV-8913) Derived queries with same column names as final projection causes issues when using Order By
* [Revision #bf18631](https://github.com/MariaDB/server/commit/bf18631)\
  2015-10-30 13:06:02 +0100
  * fix compilation with -DENABLED\_PROFILING=OFF
* [Revision #81d3584](https://github.com/MariaDB/server/commit/81d3584)\
  2015-10-30 13:12:30 +0200
  * [MDEV-9011](https://jira.mariadb.org/browse/MDEV-9011): Redo log encryption does not work
* [Revision #3e98383](https://github.com/MariaDB/server/commit/3e98383)\
  2015-10-30 08:37:40 +0200
  * Fix test failures seen on buildbot.
* [Revision #59dd58b](https://github.com/MariaDB/server/commit/59dd58b)\
  2015-10-30 10:10:43 +0400
  * [MDEV-8692](https://jira.mariadb.org/browse/MDEV-8692) prefschema test failures on ARM (on Debian build system) A few tests assumes that the CYCLE timer is always available, which is not true on some platforms (e.g. ARM). Fixing the tests not to reply on the CYCLE availability.
* [Revision #923827e](https://github.com/MariaDB/server/commit/923827e)\
  2015-05-17 15:10:45 +0200
  * [MDEV-7949](https://jira.mariadb.org/browse/MDEV-7949): Item\_field::used\_tables() takes 0.29% in OLTP RO
* [Revision #fb4358f](https://github.com/MariaDB/server/commit/fb4358f)\
  2015-05-13 16:17:22 +0200
  * [MDEV-7949](https://jira.mariadb.org/browse/MDEV-7949): Item\_field::used\_tables() takes 0.29% in OLTP RO
* [Revision #937aa7a](https://github.com/MariaDB/server/commit/937aa7a)\
  2015-10-29 09:58:11 +0100
  * [MDEV-9010](https://jira.mariadb.org/browse/MDEV-9010) Encryption preset file contains different configuration preset then documentation
* [Revision #239e0c5](https://github.com/MariaDB/server/commit/239e0c5)\
  2015-10-29 10:11:07 +0100
  * [MDEV-8551](https://jira.mariadb.org/browse/MDEV-8551) compilation fails with 10.1.6
* [Revision #9164a24](https://github.com/MariaDB/server/commit/9164a24)\
  2015-10-29 10:35:37 +0200
  * Test debug\_key\_management fails sporadically in buildbot.
* [Revision #0fe5eb5](https://github.com/MariaDB/server/commit/0fe5eb5)\
  2015-10-29 08:21:28 +0200
  * [MDEV-9032](https://jira.mariadb.org/browse/MDEV-9032): [MariaDB 10.1.8](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md) crashes at startup
* [Revision #56f04e0](https://github.com/MariaDB/server/commit/56f04e0)\
  2015-10-28 21:32:07 +0100
  * [MDEV-9014](https://jira.mariadb.org/browse/MDEV-9014) SHOW TRIGGERS not case sensitive
* [Revision #1108c1c](https://github.com/MariaDB/server/commit/1108c1c)\
  2015-10-28 14:30:30 +0200
  * [MDEV-8950](https://jira.mariadb.org/browse/MDEV-8950): encryption.innodb\_encryption\_discard\_import fails sporadically in buildbot
* [Revision #d775ecd](https://github.com/MariaDB/server/commit/d775ecd)\
  2015-10-28 08:11:54 +0100
  * [MDEV-8543](https://jira.mariadb.org/browse/MDEV-8543) mysql.server script not correctly handle --pid-file.
* [Revision #d88aaaa](https://github.com/MariaDB/server/commit/d88aaaa)\
  2015-10-28 08:34:08 +0100
  * [MDEV-8525](https://jira.mariadb.org/browse/MDEV-8525) [mariadb 10.0.20](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10020-release-notes.md) crashing when data is read by Kodi media center ([kodi.tv](https://kodi.tv)).
* [Revision #b0e3f48](https://github.com/MariaDB/server/commit/b0e3f48)\
  2015-10-22 16:08:45 +0200
  * [MDEV-8756](https://jira.mariadb.org/browse/MDEV-8756) [MariaDB 10.0.21](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10021-release-notes.md) crashes during PREPARE
* [Revision #ac67f9a](https://github.com/MariaDB/server/commit/ac67f9a)\
  2015-10-28 12:53:23 +0400
  * Removed mistakenly committed test file.
* [Revision #ce1b450](https://github.com/MariaDB/server/commit/ce1b450)\
  2015-10-22 13:57:44 +0200
  * [MDEV-7930](https://jira.mariadb.org/browse/MDEV-7930) Assertion \`table\_share->tmp\_table != NO\_TMP\_TABLE || m\_lock\_type != 2' failed in handler::ha\_index\_read\_map
* [Revision #e1ed331](https://github.com/MariaDB/server/commit/e1ed331)\
  2014-07-01 16:52:35 +0530
  * [MDEV-8805](https://jira.mariadb.org/browse/MDEV-8805) - Assertion \`!m\_ordered\_rec\_buffer' failed in ha\_partition::init\_record\_priority\_queue()
* [Revision #f2ab9ab](https://github.com/MariaDB/server/commit/f2ab9ab)\
  2015-10-28 09:14:22 +0200
  * [MDEV-9000](https://jira.mariadb.org/browse/MDEV-9000): storage/xtradb/fil/fil0pagecompress.cc fails to compile on i686-linux
* [Revision #4834d82](https://github.com/MariaDB/server/commit/4834d82)\
  2015-10-28 08:42:51 +0200
  * [MDEV-8932](https://jira.mariadb.org/browse/MDEV-8932): innodb buffer pool hit rate is less than zero
* [Revision #a9b5a8d](https://github.com/MariaDB/server/commit/a9b5a8d)\
  2015-10-28 00:08:18 +0100
  * Merge branch 'bb-10.0-serg' into 10.0
* [Revision #3c5733c](https://github.com/MariaDB/server/commit/3c5733c)\
  2015-10-27 18:57:28 +0100
  * Merge branch 'connect/10.0' into 10.0
* [Revision #13884cf](https://github.com/MariaDB/server/commit/13884cf)\
  2015-10-27 13:00:15 +0200
  * [MDEV-8696](https://jira.mariadb.org/browse/MDEV-8696): Adding indexes on empty table is slow with large innodb\_sort\_buffer\_size.
* [Revision #d6480f4](https://github.com/MariaDB/server/commit/d6480f4)\
  2015-10-11 10:32:44 +0200
  * Fixed Fedora 22 package build failure.
* [Revision #e4f9d20](https://github.com/MariaDB/server/commit/e4f9d20)\
  2015-10-23 15:06:43 +0400
  * [MDEV-8498](https://jira.mariadb.org/browse/MDEV-8498) - mysql\_secure\_installation can't find "mysql" in basedir
* [Revision #e7fa7e0](https://github.com/MariaDB/server/commit/e7fa7e0)\
  2015-10-25 21:19:45 +0100
  * Fix error and warnings raised by gcc on Linux: Define O\_RDONLY in jsonudf.cpp Correct wrong deinit function names Make Locate functions use the variable more Avoid signed/unsigned warning in ha\_connect.cc GetIntegerTableOption Initialize oom in tabodbc MakeInsert
* [Revision #abe87bb](https://github.com/MariaDB/server/commit/abe87bb)\
  2015-10-25 21:11:04 +0100
  * Fix error and warnings raised by gcc on Linux: Define O\_RDONLY in jsonudf.cpp Correct wrong deinit function names Make Locate functions use the variable more Avoid signed/unsigned warning in ha\_connect.cc GetIntegerTableOption Initialize oom in tabodbc MakeInsert
* [Revision #c918522](https://github.com/MariaDB/server/commit/c918522)\
  2015-10-25 22:45:48 +0400
  * [MDEV-8358](https://jira.mariadb.org/browse/MDEV-8358) ALTER TABLE .. ADD PRIMARY KEY IF NOT EXISTS -> ERROR 1068 (42000): Multiple primary key defined Checks for multiple primary keys added.
* [Revision #de19721](https://github.com/MariaDB/server/commit/de19721)\
  2015-10-25 17:46:20 +0100
  * Fix of error and warnings when compiling on linux
* [Revision #6a28882](https://github.com/MariaDB/server/commit/6a28882)\
  2015-10-24 20:06:59 +0200
  * merge commit 02b00b154
* [Revision #84da154](https://github.com/MariaDB/server/commit/84da154)\
  2015-10-23 22:21:50 +0200
  * [MDEV-8883](https://jira.mariadb.org/browse/MDEV-8883) more cross-compiling fixes
* [Revision #fb87133](https://github.com/MariaDB/server/commit/fb87133)\
  2015-10-23 11:31:18 +0200
  * remove unneded #include's that had a dubious explanation
* [Revision #2c0bcff](https://github.com/MariaDB/server/commit/2c0bcff)\
  2015-10-24 20:16:06 +0400
  * [MDEV-8693](https://jira.mariadb.org/browse/MDEV-8693) Tests connect.bin connect.endian fail on armhf (on Debian build system)
* [Revision #0b8144a](https://github.com/MariaDB/server/commit/0b8144a)\
  2015-10-23 23:23:36 +1100
  * [MDEV-8981](https://jira.mariadb.org/browse/MDEV-8981): Analyze stmt - cycles can overflow
* [Revision #d546d1c](https://github.com/MariaDB/server/commit/d546d1c)\
  2015-10-23 18:49:02 +0300
  * Fixed [MDEV-8408](https://jira.mariadb.org/browse/MDEV-8408) Assertion \`inited==INDEX' failed in int handler::ha\_index\_first(uchar\*)
* [Revision #8a09280](https://github.com/MariaDB/server/commit/8a09280)\
  2015-10-22 17:01:46 +0300
  * Removed not needed note when doing mysqld --version
* [Revision #c3ebd78](https://github.com/MariaDB/server/commit/c3ebd78)\
  2015-10-22 17:00:58 +0300
  * Remove THD argment from Log\_event->net\_send() and Protocol::pack\_info() as THD is already available in Protocol
* [Revision #df8832c](https://github.com/MariaDB/server/commit/df8832c)\
  2015-10-22 15:23:18 +0200
  * [MDEV-8883](https://jira.mariadb.org/browse/MDEV-8883) more cross-compiling fixes
* [Revision #0bf2b1c](https://github.com/MariaDB/server/commit/0bf2b1c)\
  2015-10-12 12:53:03 +0300
  * Ignore tokudb tool
* [Revision #581d852](https://github.com/MariaDB/server/commit/581d852)\
  2015-10-22 13:55:55 +0200
  * [MDEV-8868](https://jira.mariadb.org/browse/MDEV-8868) Consider adding a check for libjemalloc version in cmake and/or at runtime
* [Revision #6f07547](https://github.com/MariaDB/server/commit/6f07547)\
  2015-10-22 13:09:38 +0200
  * [MDEV-8614](https://jira.mariadb.org/browse/MDEV-8614) Assertion \`status == 0' failed in add\_role\_user\_mapping\_action on RENAME USER
* [Revision #956e92d](https://github.com/MariaDB/server/commit/956e92d)\
  2015-10-22 11:58:54 +0200
  * [MDEV-8609](https://jira.mariadb.org/browse/MDEV-8609) Server crashes in is\_invalid\_role\_name on reloading ACL with a blank role name
* [Revision #27328ca](https://github.com/MariaDB/server/commit/27328ca)\
  2015-10-22 10:27:36 +0200
  * add comment to a test
* [Revision #3e1c743](https://github.com/MariaDB/server/commit/3e1c743)\
  2015-10-22 07:23:59 +0200
  * [MDEV-7656](https://jira.mariadb.org/browse/MDEV-7656) init\_file option does not allow changing passwords
* [Revision #e257b8b](https://github.com/MariaDB/server/commit/e257b8b)\
  2015-10-21 16:22:20 +0200
  * fix the dbug tag name
* [Revision #e5cce2b](https://github.com/MariaDB/server/commit/e5cce2b)\
  2015-10-22 07:15:23 +0200
  * fix build on sol10-64
* [Revision #e498d32](https://github.com/MariaDB/server/commit/e498d32)\
  2015-10-22 09:11:23 +0400
  * Adding "const" qualifier to arguments of date2my\_decimal() and ErrConvString::ErrConvString(String \*).
* [Revision #bdc03e0](https://github.com/MariaDB/server/commit/bdc03e0)\
  2015-10-22 08:11:31 +0400
  * [MDEV-7195](https://jira.mariadb.org/browse/MDEV-7195) AVG() loses precision in INT context The fix for [MDEV-8918](https://jira.mariadb.org/browse/MDEV-8918) previously fixed the problem reported in [MDEV-7195](https://jira.mariadb.org/browse/MDEV-7195). Adding a test case from [MDEV-7195](https://jira.mariadb.org/browse/MDEV-7195) only.
* [Revision #41a3c58](https://github.com/MariaDB/server/commit/41a3c58)\
  2015-10-21 19:40:38 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #1816eca](https://github.com/MariaDB/server/commit/1816eca)\
  2015-10-21 19:26:35 +0200
  * Fix [MDEV-8882](https://jira.mariadb.org/browse/MDEV-8882)
* [Revision #b35f997](https://github.com/MariaDB/server/commit/b35f997)\
  2015-10-21 19:24:01 +0200
  * Fix [MDEV-8882](https://jira.mariadb.org/browse/MDEV-8882)
* [Revision #18f7dfe](https://github.com/MariaDB/server/commit/18f7dfe)\
  2015-10-15 12:11:17 +0300
  * Allow mysql\_upgrade to enable event after table is corrected
* [Revision #95faf34](https://github.com/MariaDB/server/commit/95faf34)\
  2015-10-12 13:05:31 +0300
  * Set opt\_noacl (running with--skip-grant-tables) to 0 if we reload grant tables.
* [Revision #0d90b8b](https://github.com/MariaDB/server/commit/0d90b8b)\
  2015-10-21 14:59:36 +0200
  * Merge branch '5.5' into 10.0
* [Revision #df80420](https://github.com/MariaDB/server/commit/df80420)\
  2015-10-21 14:42:56 +0200
  * fix events\_1 test for October 2015
* [Revision #17b0b45](https://github.com/MariaDB/server/commit/17b0b45)\
  2015-10-21 09:20:54 +0300
  * Code cleanup.
* [Revision #2445b1b](https://github.com/MariaDB/server/commit/2445b1b)\
  2015-10-20 18:49:33 +0200
  * Typo
* [Revision #ac9141c](https://github.com/MariaDB/server/commit/ac9141c)\
  2015-10-20 18:45:45 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #d51e466](https://github.com/MariaDB/server/commit/d51e466)\
  2015-10-20 13:20:10 +0200
  * Fix [MDEV-8966](https://jira.mariadb.org/browse/MDEV-8966)
* [Revision #f3e3624](https://github.com/MariaDB/server/commit/f3e3624)\
  2015-10-20 13:41:14 +0300
  * [MDEV-8869](https://jira.mariadb.org/browse/MDEV-8869): Potential lock\_sys->mutex deadlock
* [Revision #76701c6](https://github.com/MariaDB/server/commit/76701c6)\
  2015-10-19 14:17:36 +0300
  * Merge pull request #105 from philip-galera/10.0-galera-mysql-wsrep-gh202
* [Revision #52a9103](https://github.com/MariaDB/server/commit/52a9103)\
  2015-10-19 04:14:51 -0700
  * refs codership/mysql-wsrep#202 Fix bad cherry-pick (and the compiler warnings it generated)
* [Revision #9a3ff07](https://github.com/MariaDB/server/commit/9a3ff07)\
  2015-10-19 12:15:49 +0200
  * [MDEV-8565](https://jira.mariadb.org/browse/MDEV-8565): COLUMN\_CHECK fails on valid data
* [Revision #3ec139a](https://github.com/MariaDB/server/commit/3ec139a)\
  2015-10-19 12:05:25 +0300
  * Merge pull request #104 from philip-galera/10.0-galera-mysql-wsrep-gh202
* [Revision #43b2a45](https://github.com/MariaDB/server/commit/43b2a45)\
  2015-10-19 01:56:04 -0700
  * refs codership/mysql-wsrep#202 Added schema info into wsrep messages
* [Revision #7cd9af6](https://github.com/MariaDB/server/commit/7cd9af6)\
  2015-10-18 15:55:32 +0200
  * Fix [MDEV-8926](https://jira.mariadb.org/browse/MDEV-8926)
* [Revision #f515422](https://github.com/MariaDB/server/commit/f515422)\
  2015-10-18 15:06:14 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #9020946](https://github.com/MariaDB/server/commit/9020946)\
  2015-10-18 15:03:45 +0200
  * Fix [MDEV-8926](https://jira.mariadb.org/browse/MDEV-8926)
* [Revision #100be0b](https://github.com/MariaDB/server/commit/100be0b)\
  2015-10-17 17:23:11 +0200
  * Update JSON UDFs to version 1.04.0004
* [Revision #978c2a3](https://github.com/MariaDB/server/commit/978c2a3)\
  2015-10-11 17:06:03 -0400
  * [MDEV-7640](https://jira.mariadb.org/browse/MDEV-7640): CHANGE MASTER TO doesn't work with prepared statements
* [Revision #151f967](https://github.com/MariaDB/server/commit/151f967)\
  2015-10-11 17:06:03 -0400
  * [MDEV-7640](https://jira.mariadb.org/browse/MDEV-7640): CHANGE MASTER TO doesn't work with prepared statements
* [Revision #608ad38](https://github.com/MariaDB/server/commit/608ad38)\
  2015-10-04 11:57:57 +0200
  * Temporary changes for making compile to work
* [Revision #4d33f9d](https://github.com/MariaDB/server/commit/4d33f9d)\
  2015-09-25 14:57:56 -0400
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #13615c5](https://github.com/MariaDB/server/commit/13615c5)\
  2015-09-25 13:56:02 -0400
  * [MDEV-8208](https://jira.mariadb.org/browse/MDEV-8208): Sporadic SEGFAULT on startup
* [Revision #d54bc3c](https://github.com/MariaDB/server/commit/d54bc3c)\
  2015-09-21 20:49:31 -0400
  * Cleanup: remove dead code which could also lead to race.
* [Revision #9d5767c](https://github.com/MariaDB/server/commit/9d5767c)\
  2015-09-21 20:47:05 -0400
  * Post-merge fix.
* [Revision #a575d90](https://github.com/MariaDB/server/commit/a575d90)\
  2015-09-21 21:14:18 +0200
  * Fold all json UDF names to lower case
* [Revision #9c6405f](https://github.com/MariaDB/server/commit/9c6405f)\
  2015-09-18 18:39:08 +0200
  * Commit resolved conflicts
* [Revision #db2e21b](https://github.com/MariaDB/server/commit/db2e21b)\
  2015-09-16 23:20:57 -0400
  * [MDEV-8208](https://jira.mariadb.org/browse/MDEV-8208): Sporadic SEGFAULT on startup
* [Revision #80d1237](https://github.com/MariaDB/server/commit/80d1237)\
  2015-09-16 12:14:59 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #019c9e0](https://github.com/MariaDB/server/commit/019c9e0)\
  2015-09-16 12:11:28 +0200
  * Fix assert error for where clause with UDF's was fixed in HA\_CONNECT::CondFilter moving res= pval->val\_str(\&tmp) but this was wrong. Now res is only used for strings.
* [Revision #fd1b2e4](https://github.com/MariaDB/server/commit/fd1b2e4)\
  2015-09-15 17:07:41 -0400
  * [MDEV-8803](https://jira.mariadb.org/browse/MDEV-8803): Debian jessie 8.2 + [MariaDB 10.1.7](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes.md) + GaleraCluster
* [Revision #653aadc](https://github.com/MariaDB/server/commit/653aadc)\
  2015-09-15 16:27:04 -0400
  * [MDEV-8804](https://jira.mariadb.org/browse/MDEV-8804): bootstrap command missing in debian init script
* [Revision #f4fe138](https://github.com/MariaDB/server/commit/f4fe138)\
  2015-09-15 20:42:51 +0200
  * Fix assert error for where clause with UDF's was fixed in HA\_CONNECT::CondFilter moving res= pval->val\_str(\&tmp) but this was wrong. Now res is only used for strings. Change version number
* [Revision #eac8e43](https://github.com/MariaDB/server/commit/eac8e43)\
  2015-09-14 15:43:16 -0400
  * Avoid caching wsrep threads (fixed the erroneous condition).
* [Revision #a401c11](https://github.com/MariaDB/server/commit/a401c11)\
  2015-09-14 15:26:50 -0400
  * Fix failing test cases
* [Revision #ceac344](https://github.com/MariaDB/server/commit/ceac344)\
  2015-09-10 09:57:08 -0400
  * [Bug #1372840](https://bugs.launchpad.net/bugs/1372840) - test case
* [Revision #f479b5a](https://github.com/MariaDB/server/commit/f479b5a)\
  2015-09-10 00:29:06 -0400
  * Update WSREP\_PATCH\_REVNO
* [Revision #f951071](https://github.com/MariaDB/server/commit/f951071)\
  2015-09-08 22:11:56 -0700
  * Galera MTR Tests: fix typo in the galera\_as\_slave\_nonprim test, in suite/galera/galera\_3nodes\_as\_slave.cnf
* [Revision #b3ec0a8](https://github.com/MariaDB/server/commit/b3ec0a8)\
  2015-09-08 05:04:47 -0700
  * Galera MTR Tests: a test for async slave + non-prim
* [Revision #db66d2f](https://github.com/MariaDB/server/commit/db66d2f)\
  2015-09-10 00:20:49 -0400
  * refs codership/mysql-wsrep#188
* [Revision #2012a81](https://github.com/MariaDB/server/commit/2012a81)\
  2015-09-10 00:14:24 -0400
  * refs codership/mysql-wsrep#181
* [Revision #c915d8c](https://github.com/MariaDB/server/commit/c915d8c)\
  2015-09-01 00:57:20 -0700
  * Galera MTR Tests: attempt to work around codership/mysql-wsrep#179
* [Revision #25bbfe8](https://github.com/MariaDB/server/commit/25bbfe8)\
  2015-08-31 02:16:43 -0700
  * Galera MTR Tests: Instruct xtrabackup SST's socat to use 1024-bit DH keys to avoid 'error:14082174:SSL routines:SSL3\_CHECK\_CERT\_AND\_ALGORITHM:dh key too small'
* [Revision #b6f8033](https://github.com/MariaDB/server/commit/b6f8033)\
  2015-08-31 02:15:37 -0700
  * Galera MTR Tests: Tests around do-\* and ignore-\* binlog options
* [Revision #f7885fb](https://github.com/MariaDB/server/commit/f7885fb)\
  2015-08-27 00:54:26 -0700
  * Correct WSREP\_PATCH\_VERSION for 5.6 is 11
* [Revision #52c9235](https://github.com/MariaDB/server/commit/52c9235)\
  2015-08-25 06:15:20 -0700
  * Galera MTR Tests: Add known Galera and mysql-wsrep Valgrind issues to valgrind.supp
* [Revision #371dc33](https://github.com/MariaDB/server/commit/371dc33)\
  2015-08-24 06:56:30 -0700
  * refs codership/mysql-wsrep#90 MTR test case for mysql-wsrep#90
* [Revision #e5b595e](https://github.com/MariaDB/server/commit/e5b595e)\
  2015-08-14 05:14:53 -0700
  * Galera MTR Tests: fix typo in suite/galera/galera\_2nodes\_as\_slave.cnf
* [Revision #ee22ac3](https://github.com/MariaDB/server/commit/ee22ac3)\
  2015-08-14 01:16:25 -0700
  * Galera MTR Tests: Various test stability fixes (take #5)
* [Revision #7d73931](https://github.com/MariaDB/server/commit/7d73931)\
  2015-08-12 06:40:59 -0700
  * Galera MTR Tests: Various test stability fixes (take #4)
* [Revision #ff76214](https://github.com/MariaDB/server/commit/ff76214)\
  2015-08-12 05:32:18 -0700
  * Galera MTR Tests: Various test stability fixes (take #3)
* [Revision #fd0aaad](https://github.com/MariaDB/server/commit/fd0aaad)\
  2015-08-12 01:03:21 -0700
  * Galera MTR Tests: Various test stability fixes (take #2)
* [Revision #997119d](https://github.com/MariaDB/server/commit/997119d)\
  2015-08-11 04:22:38 -0700
  * Galera MTR Tests: Various test stability fixes.
* [Revision #182b237](https://github.com/MariaDB/server/commit/182b237)\
  2015-08-07 21:15:02 -0700
  * Galera MTR Tests: remove variable output from galera\_gra\_log.test (take #2)
* [Revision #c9d4581](https://github.com/MariaDB/server/commit/c9d4581)\
  2015-08-06 20:55:30 -0700
  * Galera MTR Tests: remove variable output from galera\_gra\_log.test
* [Revision #2316a4e](https://github.com/MariaDB/server/commit/2316a4e)\
  2015-08-06 00:34:00 -0700
  * Galera MTR Tests: Tests for GRA\*.log files, replication bundle, preordered events, forced binlog format
* [Revision #a1a7414](https://github.com/MariaDB/server/commit/a1a7414)\
  2015-08-03 03:20:52 -0700
  * Galera MTR Tests: An end-to-end test with restoring a node from xtrabackup; a test for restoring the primary component via pc.bootstrap
* [Revision #1e29068](https://github.com/MariaDB/server/commit/1e29068)\
  2015-07-23 04:30:07 -0700
  * Galera MTR Tests: Valgrind suppression for codership/galera#306
* [Revision #3893b5c](https://github.com/MariaDB/server/commit/3893b5c)\
  2015-07-23 04:29:40 -0700
  * Galera MTR Tests: mark all tests operating on large data sets with --source include/big-test.inc to help with Valgrind
* [Revision #83579c2](https://github.com/MariaDB/server/commit/83579c2)\
  2015-07-10 07:17:20 -0700
  * Galera MTR Tests: fixes for mysqldump SST/IST tests
* [Revision #10f5c08](https://github.com/MariaDB/server/commit/10f5c08)\
  2015-07-08 01:52:45 -0700
  * Refs codership/QA#47. Additional tests for FTWRL.
* [Revision #6104a27](https://github.com/MariaDB/server/commit/6104a27)\
  2015-07-07 06:01:00 -0700
  * Galera MTR Tests: increase lock wait timeout in suite/galera/t/galera\_many\_rows.test
* [Revision #4a630ce](https://github.com/MariaDB/server/commit/4a630ce)\
  2015-07-07 06:00:22 -0700
  * Galera MTR Tests: A test for xtrabackup with key+cert encryption.
* [Revision #edd9bd3](https://github.com/MariaDB/server/commit/edd9bd3)\
  2015-07-07 03:42:03 -0700
  * Fixes codership/mysql-wsrep#153 use --defaults-extra-file with mysqldump SST
* [Revision #5d531f0](https://github.com/MariaDB/server/commit/5d531f0)\
  2015-07-01 03:13:04 -0700
  * Galera MTR Tests: Use SET GLOBAL when setting wsrep\_replicate\_myisam, as it is a GLOBAL variable in MySQL Galera Cluster and SESSION in Percona XTraDB Cluster
* [Revision #fbe739c](https://github.com/MariaDB/server/commit/fbe739c)\
  2015-06-29 16:42:58 +0530
  * Bug#1421360: Add 'FLUSH TABLES' to Total Order Isolation execution.
* [Revision #5a002ad](https://github.com/MariaDB/server/commit/5a002ad)\
  2015-06-26 01:30:01 -0700
  * Galera MTR Tests: various tests and test fixes
* [Revision #f1a00ed](https://github.com/MariaDB/server/commit/f1a00ed)\
  2015-06-17 05:14:36 -0700
  * Galera MTR Tests: Use wsrep\_sst\_auth for tests that use xtrabackup + IST
* [Revision #2ea16b9](https://github.com/MariaDB/server/commit/2ea16b9)\
  2015-06-08 21:06:22 +0300
  * This commit fixes
    * errno handling in wsp::env::append() method, where error could be returned by mistake
    * return code of sst\_prepare\_other() when pthread\_create() fails
    * it was returning positive error code which by convention is treated as success.
* [Revision #0ccbbff](https://github.com/MariaDB/server/commit/0ccbbff)\
  2015-06-08 12:23:53 +0300
  * Slight cleanup improvement on a previous commit.
* [Revision #bc796c2](https://github.com/MariaDB/server/commit/bc796c2)\
  2015-06-08 01:43:27 -0700
  * Refs codership/mysql-wsrep#143 . Account for the case where the SST password is empty
* [Revision #86ee30c](https://github.com/MariaDB/server/commit/86ee30c)\
  2015-06-06 01:08:41 +0300
  * Refs codership/mysql-wsrep#141: this commit
    1. Passes wsrep\_sst\_auth\_value to SST scripts via WSREP\_SST\_OPT\_AUTH envronmental variable, so it never appears on the command line
    2. In mysqldump and xtrabackup\* SST scripts which rely on MySQL authentication, instead of passing password on the command line, SST script sets MYSQL\_PWD environment variable, so that password also never appears on the mysqldump/innobackupex command line.
* [Revision #197e9d2](https://github.com/MariaDB/server/commit/197e9d2)\
  2015-05-26 15:44:34 +0300
  * Refs codership/mysql-wsrep#132 - fix for THD::m\_digest initialization, according to Raghu
* [Revision #483078b](https://github.com/MariaDB/server/commit/483078b)\
  2015-05-15 02:15:58 -0700
  * Fixes codership/QA#87 . An MTR test for SERIALIZABLE
* [Revision #4102d52](https://github.com/MariaDB/server/commit/4102d52)\
  2015-05-11 02:21:39 -0700
  * Refs codership/mysql-wsrep#113 - tests around FLUSH TABLE, FLUSH TABLES, LOCK TABLE
* [Revision #2106fed](https://github.com/MariaDB/server/commit/2106fed)\
  2015-05-10 21:49:36 +0300
  * Refs codership/mysql-wsrep#113 - changed BF thread's MDL wait to never timeout - all explicit locks are now honored by BF threads
* [Revision #f9805e4](https://github.com/MariaDB/server/commit/f9805e4)\
  2015-05-08 03:21:50 -0700
  * Galera MTR Tests: tests for WAN restart, xtrabackup options and others.
* [Revision #ef7b089](https://github.com/MariaDB/server/commit/ef7b089)\
  2015-05-06 10:35:02 +0300
  * Fixes codership/mysql-wsrep#122 - causal/casual typos fixed in wsrep code
* [Revision #bace2a9](https://github.com/MariaDB/server/commit/bace2a9)\
  2015-05-05 01:21:55 -0700
  * Galera MTR Tests: add a test for socket.ssl\_compression
* [Revision #b5ef2bb](https://github.com/MariaDB/server/commit/b5ef2bb)\
  2015-04-28 23:34:47 -0700
  * Re-enable tests previously disabled due to mysql-wsrep#114
* [Revision #63c5bee](https://github.com/MariaDB/server/commit/63c5bee)\
  2015-04-28 20:38:25 +0300
  * Refs codership/mysql-wsrep#113 - Extended the protection of local FLUSH sessions to cover all exclusive MDL locks
* [Revision #417f778](https://github.com/MariaDB/server/commit/417f778)\
  2015-04-28 00:55:50 -0700
  * Galera MTR tests: disable innodb.innodb\_stats\_\* due to mysql-wsrep#114
* [Revision #6bb890c](https://github.com/MariaDB/server/commit/6bb890c)\
  2015-04-24 10:39:42 +0300
  * refs codership/mysql-wsrep#114 - skipping TOI if not using wsrep provider
* [Revision #c666090](https://github.com/MariaDB/server/commit/c666090)\
  2015-04-21 16:22:53 +0300
  * Refs codership/mysql-wsrep#113 Protecting non replicated FLUSH session from brute force aborts
* [Revision #045b31c](https://github.com/MariaDB/server/commit/045b31c)\
  2015-04-20 05:58:24 -0700
  * Test cases for codership/mysql-wsrep/110
* [Revision #dc9e325](https://github.com/MariaDB/server/commit/dc9e325)\
  2015-04-20 13:18:21 +0300
  * refs codership/mysql-wsrep#110 - clear table map events on SAVEPOINT
* [Revision #d0e24c6](https://github.com/MariaDB/server/commit/d0e24c6)\
  2015-04-01 02:52:24 -0700
  * Galera MTR Tests: Attempt to remove rare sporadic failures in galera\_transaction\_replay.test by waiting for all transactions to get blocked before proceeding.
* [Revision #f8b724d](https://github.com/MariaDB/server/commit/f8b724d)\
  2015-03-31 06:43:38 -0700
  * Galera MTR Tests: Enable the use of --parallel for port-intensive Galera tests by additionally specifying --port-group-size=50
* [Revision #9f716ae](https://github.com/MariaDB/server/commit/9f716ae)\
  2015-03-29 23:56:21 -0700
  * Galera MTR: Disable rpl.rpl\_rotate\_logs binlog.binlog\_index due to codership/mysql-wsrep#71
* [Revision #fa5f18d](https://github.com/MariaDB/server/commit/fa5f18d)\
  2015-09-09 20:51:39 -0400
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #37ae601](https://github.com/MariaDB/server/commit/37ae601)\
  2015-09-09 18:54:14 -0400
  * Update WSREP\_PATCH\_REVNO
* [Revision #760b0c4](https://github.com/MariaDB/server/commit/760b0c4)\
  2015-08-27 00:41:56 -0700
  * Bump WSREP\_PATCH\_VERSION in cmake/wsrep.cmake to 12
* [Revision #bee94cc](https://github.com/MariaDB/server/commit/bee94cc)\
  2015-07-07 22:34:25 -0700
  * Fixes codership/mysql-wsrep#153 use --defaults-extra-file with mysqldump SST
* [Revision #55dfddf](https://github.com/MariaDB/server/commit/55dfddf)\
  2015-06-09 17:02:26 +0300
  * Fixing donate callback return code
* [Revision #0465e3a](https://github.com/MariaDB/server/commit/0465e3a)\
  2015-06-09 11:36:31 +0300
  * Logging message cleanup
* [Revision #d809fcc](https://github.com/MariaDB/server/commit/d809fcc)\
  2015-06-08 21:06:22 +0300
  * This commit fixes
    * errno handling in wsp::env::append() method, where error could be returned by mistake
    * return code of sst\_prepare\_other() when pthread\_create() fails
    * it was returning positive error code which by convention is treated as success.
* [Revision #1b1410c](https://github.com/MariaDB/server/commit/1b1410c)\
  2015-06-08 12:23:53 +0300
  * Slight cleanup improvement on a previous commit.
* [Revision #62c2539](https://github.com/MariaDB/server/commit/62c2539)\
  2015-06-08 01:46:20 -0700
  * Refs codership/mysql-wsrep#143 . Account for the case where the SST password is empty
* [Revision #a7ea3ec](https://github.com/MariaDB/server/commit/a7ea3ec)\
  2015-06-06 01:38:07 +0300
  * Synced xtrabackup SST fixes from Percona tree (as of PXC 5.6.24-25.11 release). This fixes/adresses the following LP bugs:
    * LP1380697: wsrep\_sst\_xtrabackup-v2 doesn't stop when mysql is SIGKILLed. (full fix for this (as engineeered by Percona) requires Linux-specific patch that we don't carry, but keep xtrabackup scripts as close as possible)
    * LP1399134: Log the innobackupex/SST logs in SST to syslog if possible. (fixed)
    * LP1405668: Race condition between donor and joiner in PXB SST. (fixed)
    * LP1405985: Fail early if xtrabackup\_checkkpoints is missing. (fixed)
    * LP1407599: wsrep\_sst\_xtrabackup-v2 script causes innobackupex to print a false positive stack trace into the log. (fixed)
    * LP1441762: IST Fails with SST script error. (fixed)
    * LP1451670: Fail when move-back fails in xtrabackup SST. (fixed)
* [Revision #d78110e](https://github.com/MariaDB/server/commit/d78110e)\
  2015-06-06 01:08:41 +0300
  * Refs codership/mysql-wsrep#141: this commit 1. Passes wsrep\_sst\_auth\_value to SST scripts via WSREP\_SST\_OPT\_AUTH envronmental variable, so it never appears on the command line 2. In mysqldump and xtrabackup\* SST scripts which rely on MySQL authentication, instead of passing password on the command line, SST script sets MYSQL\_PWD environment variable, so that password also never appears on the mysqldump/innobackupex command line.
* [Revision #4f4f3a5](https://github.com/MariaDB/server/commit/4f4f3a5)\
  2015-05-02 22:25:39 +0300
  * Fixes codership/mysql-wsrep#118
* [Revision #d69931e](https://github.com/MariaDB/server/commit/d69931e)\
  2015-09-09 01:28:04 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #e939ea5](https://github.com/MariaDB/server/commit/e939ea5)\
  2015-09-09 01:26:00 +0200
  * Fix assert error for where clause with UDF's was fixed in HA\_CONNECT::CondFilter moving pval->val\_str(\&tmp)
* [Revision #8a154ec](https://github.com/MariaDB/server/commit/8a154ec)\
  2015-09-07 18:53:25 +0200
  * Add Json\_Get\_Item (and Bson\_File?) functions
* [Revision #7915abf](https://github.com/MariaDB/server/commit/7915abf)\
  2015-09-06 15:51:48 +0200
  * Add experimental Bson\_Array function (not documented) Change names of functions not returning Json.
* [Revision #175ef097](https://github.com/MariaDB/server/commit/175ef097)\
  2015-08-22 18:11:42 +0200
  * Handle is\_null and error arguments Fix wrong calling sequence for RESULT\_INT and RESULT\_REAL functions.
* [Revision #f741fcc](https://github.com/MariaDB/server/commit/f741fcc)\
  2015-08-22 12:13:37 +0200
  * Handle constant function and argument
* [Revision #ffc0f5b](https://github.com/MariaDB/server/commit/ffc0f5b)\
  2015-08-19 17:52:33 +0200
  * Add new UDF noconst.
* [Revision #69ce20c](https://github.com/MariaDB/server/commit/69ce20c)\
  2015-08-18 12:03:29 +0200
  * Add new json UDF Json\_Object\_List.
* [Revision #55cb3d8](https://github.com/MariaDB/server/commit/55cb3d8)\
  2015-08-14 17:07:50 +0200
  * Add new json UDFs and make possible to use a json file name as json item.
* [Revision #cd9b919](https://github.com/MariaDB/server/commit/cd9b919)\
  2015-08-14 15:49:46 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #6d46c97](https://github.com/MariaDB/server/commit/6d46c97)\
  2015-08-14 14:23:14 +0200
  * Fix crash when SetValue\_char is called with a negative length value. This can happen in odbconn.cpp when SQLFetch returns SQL\_NO\_TOTAL (-4) as length.
* [Revision #335ec7a](https://github.com/MariaDB/server/commit/335ec7a)\
  2015-08-11 21:15:33 +0200
  * Prevent wrong update of expanded columns when pretty is not 2.
* [Revision #0eacebf](https://github.com/MariaDB/server/commit/0eacebf)\
  2015-08-08 10:54:47 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #5f53303](https://github.com/MariaDB/server/commit/5f53303)\
  2015-08-06 17:46:47 +0200
  * Fix the TDBDOS::EstimatedLength function that was wrongly counting its calculation virtual and special columns.
* [Revision #3b040a0](https://github.com/MariaDB/server/commit/3b040a0)\
  2015-07-22 15:49:38 +0200
  * Fix (?) retrieving integer arguments in JSON UDF's
* [Revision #a392c79](https://github.com/MariaDB/server/commit/a392c79)\
  2015-07-16 11:05:20 +0200
  * Fix and Enhance remote indexing:
    * Apply to ODBC tables as well as MYSQL tables
    * Fix and enhance the CheckCond routine Make ReadKey and MakeKeyWhere handle all conditions
* [Revision #3a9a3b9](https://github.com/MariaDB/server/commit/3a9a3b9)\
  2015-06-08 00:03:52 +0200
  * Fix test txt files line endings
* [Revision #7482f07](https://github.com/MariaDB/server/commit/7482f07)\
  2015-06-06 19:23:06 +0200
  * Commit od last modifications made for version 10.0
* [Revision #1c75651](https://github.com/MariaDB/server/commit/1c75651)\
  2015-06-05 23:54:19 +0200
  * Commit win and CONNECT resolved files
* [Revision #5d038d3](https://github.com/MariaDB/server/commit/5d038d3)\
  2015-06-05 23:33:23 +0200
  * commit win/ changes
* [Revision #f8fa5fe](https://github.com/MariaDB/server/commit/f8fa5fe)\
  2015-06-05 23:24:39 +0200
  * Commit merge resolve
* [Revision #2b2c61c](https://github.com/MariaDB/server/commit/2b2c61c)\
  2015-06-05 17:21:04 +0200
  * Commit changes to json\_udf.inc
* [Revision #2a3166f](https://github.com/MariaDB/server/commit/2a3166f)\
  2015-06-03 17:54:11 +0200
  * Fix swapping key numeric values on Big Endian machines. Fix typo error in CntIndexRange (kp instead of p) Change version date
* [Revision #5a9e2e6](https://github.com/MariaDB/server/commit/5a9e2e6)\
  2015-06-03 16:59:45 +0200
  * Merge branch '10.1' of [MariaDB](https://github.com/Buggynours/MariaDB) into 10.1
* [Revision #36d2bd6](https://github.com/MariaDB/server/commit/36d2bd6)\
  2015-06-03 16:58:42 +0200
  * Handle ODBC table null values
* [Revision #30fd69e](https://github.com/MariaDB/server/commit/30fd69e)\
  2015-06-02 11:53:22 +0200
  * Handle ODBC table null values
* [Revision #e8ea671](https://github.com/MariaDB/server/commit/e8ea671)\
  2015-06-02 10:34:51 +0200
  * Commit changes pulled from ob-10.0
* [Revision #893631a](https://github.com/MariaDB/server/commit/893631a)\
  2015-05-20 12:39:17 +0200
  * All the last changes made in the ob-10.0 branch including also changes of line endings of some test files
* [Revision #83ca074](https://github.com/MariaDB/server/commit/83ca074)\
  2015-05-10 12:52:28 +0200
  * Last commit was done with wrong files
* [Revision #9dee994](https://github.com/MariaDB/server/commit/9dee994)\
  2015-05-10 11:58:23 +0200
  * Get rid of GCC warnings about unused parameters
* [Revision #1db5b84](https://github.com/MariaDB/server/commit/1db5b84)\
  2015-05-05 18:38:54 +0200
  * Fix a regression bug on (XML) HTML tables.
* [Revision #13c0a60](https://github.com/MariaDB/server/commit/13c0a60)\
  2015-05-02 15:49:02 +0200
  * Fix [MDEV-8090](https://jira.mariadb.org/browse/MDEV-8090) in tabmysql.cpp
* [Revision #6dda9e0](https://github.com/MariaDB/server/commit/6dda9e0)\
  2015-05-01 18:53:50 +0200
  * Same as last 10.0 commit
* [Revision #b3f9838](https://github.com/MariaDB/server/commit/b3f9838)\
  2015-04-19 12:15:58 +0200
  * Update 10.1 with changes from 10.0
* [Revision #48a77e6](https://github.com/MariaDB/server/commit/48a77e6)\
  2015-04-05 14:03:35 +0200
  * Make this repository aligned with 10.0 one
* [Revision #464947e](https://github.com/MariaDB/server/commit/464947e)\
  2015-03-22 11:31:10 +0100
  * Fix a bug that caused a crash when doing delete on a json table with wrong syntax file
* [Revision #7733b24](https://github.com/MariaDB/server/commit/7733b24)\
  2015-03-19 12:21:08 +0100
  * Same changes than in version 10.0.17
* [Revision #73d0427](https://github.com/MariaDB/server/commit/73d0427)\
  2015-03-16 17:22:50 +0100
  * Changes to avoid compiling error with Visual Studio 2008
* [Revision #6cf2093](https://github.com/MariaDB/server/commit/6cf2093)\
  2015-03-15 14:31:43 +0100
  * Commit changes to .gitignore

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
