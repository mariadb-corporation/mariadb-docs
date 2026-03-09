# MariaDB 10.1.24 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.24)[Release Notes](../../old-releases/10.1/10.1.24.md)[Changelog](mariadb-10124-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 31 May 2017

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.24.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #af4421e82d](https://github.com/MariaDB/server/commit/af4421e82d)\
  2017-05-29 00:27:14 -0700
  * Fixed the bug [MDEV-12931](https://jira.mariadb.org/browse/MDEV-12931).
* [Revision #e4d10e09cf](https://github.com/MariaDB/server/commit/e4d10e09cf)\
  2017-05-28 00:40:36 +0530
  * [MDEV-11196](https://jira.mariadb.org/browse/MDEV-11196): Error:Run-Time Check Failure #2 - Stack around the variable 'key\_buff' was corrupted, server crashes in opt\_sum\_query
* Merge [Revision #f42e08f951](https://github.com/MariaDB/server/commit/f42e08f951) 2017-05-26 19:21:19 +0200 - Merge branch '10.0-galera' into 10.1
* [Revision #0e3170e30d](https://github.com/MariaDB/server/commit/0e3170e30d)\
  2017-05-08 16:29:41 +0530
  * Fix galera tests part II(Fix previous commit)
* [Revision #10d7a2f8e0](https://github.com/MariaDB/server/commit/10d7a2f8e0)\
  2017-05-08 16:00:23 +0530
  * Fix galera test failures.
* [Revision #e4a52670f4](https://github.com/MariaDB/server/commit/e4a52670f4)\
  2017-04-05 08:54:20 +0300
  * fix warning "ignoring return value" of fwrite.
* [Revision #09b28b3d10](https://github.com/MariaDB/server/commit/09b28b3d10)\
  2017-04-05 14:35:41 +0300
  * Fix compiler warnings on gcc 6.x.
* Merge [Revision #4b1cf0bba6](https://github.com/MariaDB/server/commit/4b1cf0bba6) 2017-04-05 08:14:18 +0300 - Merge pull request #351 from grooverdan/10.0-galera-[MDEV-7560](https://jira.mariadb.org/browse/MDEV-7560)-check\_galera\_version
* [Revision #5dca5b8007](https://github.com/MariaDB/server/commit/5dca5b8007)\
  2017-03-30 15:02:30 +1100
  * [MDEV-7560](https://jira.mariadb.org/browse/MDEV-7560): check\_galera\_version to account for greater version than specified
* [Revision #d95dc57e75](https://github.com/MariaDB/server/commit/d95dc57e75)\
  2017-03-23 13:18:29 +0530
  * Fix galera.galera\_gcs\_fc\_limit
* [Revision #bb20f6d9e2](https://github.com/MariaDB/server/commit/bb20f6d9e2)\
  2017-03-23 10:26:55 +0530
  * [MDEV-12319](https://jira.mariadb.org/browse/MDEV-12319) Part 2
* [Revision #a136c36781](https://github.com/MariaDB/server/commit/a136c36781)\
  2017-03-22 10:19:06 -0400
  * bump the VERSION
* [Revision #4eb29ecfab](https://github.com/MariaDB/server/commit/4eb29ecfab)\
  2017-03-22 09:40:57 +0530
  * [MDEV-12319](https://jira.mariadb.org/browse/MDEV-12319) Test added to disabled.def
* [Revision #656d0f10e5](https://github.com/MariaDB/server/commit/656d0f10e5)\
  2017-03-21 14:23:45 +0530
  * Fix galera\_admin test
* [Revision #b22026ddfd](https://github.com/MariaDB/server/commit/b22026ddfd)\
  2017-03-21 10:00:02 +0200
  * Fix failure on galera\_toi\_drop\_database test.
* [Revision #0759c9baf5](https://github.com/MariaDB/server/commit/0759c9baf5)\
  2017-03-21 12:14:19 +0530
  * Fix mysqlhotcopy test failures
* [Revision #0b51dee0e3](https://github.com/MariaDB/server/commit/0b51dee0e3)\
  2017-03-20 18:52:18 +0530
  * Change VERSION no to 30
* Merge [Revision #9cf499724f](https://github.com/MariaDB/server/commit/9cf499724f) 2017-03-20 18:11:56 +0530 - Merge branch '10.0' into bb-10.0-galera
* [Revision #53c6195eed](https://github.com/MariaDB/server/commit/53c6195eed)\
  2017-03-20 10:17:13 +0200
  * Fixed test failure on galere\_wsrep\_log\_conflicts on XtraDB.
* Merge [Revision #f66395f7c0](https://github.com/MariaDB/server/commit/f66395f7c0) 2017-03-17 02:05:20 +0530 - Merge tag 'mariadb-10.0.30' into bb-sachin-10.0-galera-merge
* [Revision #c401773c8d](https://github.com/MariaDB/server/commit/c401773c8d)\
  2017-03-16 08:07:58 +0530
  * Fix test cases
* [Revision #5bb7653667](https://github.com/MariaDB/server/commit/5bb7653667)\
  2017-03-16 02:13:31 +0530
  * Fix wsrep\_affected\_rows.
* [Revision #1743d68868](https://github.com/MariaDB/server/commit/1743d68868)\
  2017-03-14 18:41:38 +0530
  * Fix Some failing tests
* [Revision #25070d2a2c](https://github.com/MariaDB/server/commit/25070d2a2c)\
  2017-01-25 09:58:07 +0200
  * Bump WSREP\_PATCH\_VERSION to 19
* [Revision #ad7b00fb90](https://github.com/MariaDB/server/commit/ad7b00fb90)\
  2017-03-14 16:17:28 +0530
  * Galera MTR Tests: do not run innodb.innodb\_stats\_del\_mark and some other tests with Galera, as it produces warnings
* [Revision #69b5bd7ae3](https://github.com/MariaDB/server/commit/69b5bd7ae3)\
  2016-12-16 02:30:09 -0800
  * Galera MTR Tests: Tests for MW-328 Fix unnecessary/silent BF aborts
* [Revision #dd2f023427](https://github.com/MariaDB/server/commit/dd2f023427)\
  2016-12-15 01:22:44 -0800
  * Galera MTR Tests: restore galera\_autoinc\_sst\_xtrabackup.test to use xtrabackup SST
* [Revision #5ac0d5fc24](https://github.com/MariaDB/server/commit/5ac0d5fc24)\
  2016-12-08 05:15:31 -0800
  * Galera MTR Tests: Stability fix for MW-329
* [Revision #17f716062d](https://github.com/MariaDB/server/commit/17f716062d)\
  2016-12-08 00:17:28 -0800
  * Galera MTR Tests: Test for MW-329 Fix incorrect affected rows count after replay
* [Revision #00f1ed6655](https://github.com/MariaDB/server/commit/00f1ed6655)\
  2017-03-14 14:42:52 +0530
  * Galera MTR Tests: fix variable output in galera\_as\_slave\_gtid\_replicate\_do\_db.result
* [Revision #f29c40d0a5](https://github.com/MariaDB/server/commit/f29c40d0a5)\
  2017-03-14 14:31:13 +0530
  * [GAL-480](https://github.com/codership/galera/issues/480) MTR test
* [Revision #6fabf12ba0](https://github.com/MariaDB/server/commit/6fabf12ba0)\
  2016-11-23 02:55:36 -0800
  * Galera MTR Test: Test for MW-28 : Assertion with --wsrep-log-conflicts
* [Revision #0e0ae0bb06](https://github.com/MariaDB/server/commit/0e0ae0bb06)\
  2017-03-14 13:13:22 +0530
  * MW-28, codership/mysql-wsrep#28 Fix sync\_thread\_levels debug assert
* [Revision #471dd11381](https://github.com/MariaDB/server/commit/471dd11381)\
  2016-11-21 10:38:20 +0200
  * refs: MW-319 \* silenced the WSREP\_ERROR, this fires for all replication filtered DDL, and is false positive
* [Revision #c49bfff992](https://github.com/MariaDB/server/commit/c49bfff992)\
  2017-03-14 11:21:16 +0530
  * Galera MTR tests: Make the mysqlhotcopy tests pass on Ubuntu 16.04
* [Revision #e29d7b1d0b](https://github.com/MariaDB/server/commit/e29d7b1d0b)\
  2016-11-08 15:19:37 +0200
  * Bump WSREP\_PATCH\_VERSION to 18
* [Revision #f78332c581](https://github.com/MariaDB/server/commit/f78332c581)\
  2016-11-05 09:15:14 -0700
  * Galera MTR Tests: stability fix for galera#414.test
* [Revision #64bb59fce9](https://github.com/MariaDB/server/commit/64bb59fce9)\
  2017-03-14 11:19:03 +0530
  * Galera MTR Tests: stability fixes
* [Revision #451bf7243a](https://github.com/MariaDB/server/commit/451bf7243a)\
  2016-11-04 01:33:54 -0700
  * Galera MTR Tests: Test for MW-313 Enforce wsrep\_max\_ws\_rows also when binlog is enabled
* [Revision #9dda6cb08d](https://github.com/MariaDB/server/commit/9dda6cb08d)\
  2016-11-03 16:04:22 +0100
  * MW-313 Enforce wsrep\_max\_ws\_rows also when binlog is enabled
* [Revision #395c420f0f](https://github.com/MariaDB/server/commit/395c420f0f)\
  2016-11-03 04:05:05 -0700
  * Galera MTR Tests: MW-305 , re-enable the test for ALTER USER
* [Revision #0a06347333](https://github.com/MariaDB/server/commit/0a06347333)\
  2016-11-03 00:49:20 -0700
  * Galera MTR Tests: Test for MW-309 - Fix wsrep\_max\_ws\_rows so that it does not affect SELECT queries
* [Revision #5d9c747193](https://github.com/MariaDB/server/commit/5d9c747193)\
  2016-11-02 07:04:34 -0700
  * Galera MTR tests: Update galera\_defaults.result for [GAL-360](https://github.com/codership/galera/issues/360)
* [Revision #16e683fdad](https://github.com/MariaDB/server/commit/16e683fdad)\
  2017-03-14 07:11:17 +0530
  * Galera MTR Tests: Tests for [GAL-419](https://github.com/codership/galera/issues/419) Respect safe\_to\_bootstrap flag also with gcomm:
* [Revision #108fd77486](https://github.com/MariaDB/server/commit/108fd77486)\
  2016-11-02 02:01:10 -0700
  * Galera MTR Tests: [GAL-405](https://github.com/codership/galera/issues/405) Initial implementation of GCache recovery on startup.
* [Revision #9be994ba69](https://github.com/MariaDB/server/commit/9be994ba69)\
  2017-03-13 05:30:02 +0530
  * MW-309 Fix wsrep\_max\_ws\_rows so that it does not affect queries
* [Revision #4573924f7d](https://github.com/MariaDB/server/commit/4573924f7d)\
  2017-03-12 23:00:20 +0530
  * Galera MTR Tests: MW-308 , MW-307, GCF-992
* [Revision #c2eaae268d](https://github.com/MariaDB/server/commit/c2eaae268d)\
  2016-10-11 03:37:42 -0700
  * Galera MTR Tests: GCF-981 - galera\_bf\_abort is non deterministic
* [Revision #0e105bc1f2](https://github.com/MariaDB/server/commit/0e105bc1f2)\
  2016-10-03 03:09:49 -0700
  * Galera MTR Tests: Test for GCF-942 - safe\_to\_bootstrap flag in grastate.dat
* [Revision #15298689cb](https://github.com/MariaDB/server/commit/15298689cb)\
  2016-09-14 14:33:59 +0300
  * Bump WSREP\_PATCH\_VERSION to 17
* [Revision #86ec6c221a](https://github.com/MariaDB/server/commit/86ec6c221a)\
  2017-03-12 13:56:29 +0530
  * MW-267: followup to the original pull request, removed unnecessary cast.
* [Revision #3045b60f0f](https://github.com/MariaDB/server/commit/3045b60f0f)\
  2016-08-20 13:42:11 +0200
  * [GAL-401](https://github.com/codership/galera/issues/401): MTR test for the fix.
* [Revision #8c35f105d2](https://github.com/MariaDB/server/commit/8c35f105d2)\
  2017-05-26 19:54:09 +0300
  * Latest additions to the list of unstable tests in 10.1.24
* [Revision #994a5f29f1](https://github.com/MariaDB/server/commit/994a5f29f1)\
  2017-05-26 19:53:29 +0300
  * On a build without performance schema the test failed
* [Revision #808f18c748](https://github.com/MariaDB/server/commit/808f18c748)\
  2017-05-26 19:13:21 +0300
  * [MDEV-12926](https://jira.mariadb.org/browse/MDEV-12926) encryption.innodb\_onlinealter\_encryption, encryption.innodb-bad-key-change failed in buildbot with valgrind
* [Revision #2f29fc3c1c](https://github.com/MariaDB/server/commit/2f29fc3c1c)\
  2017-05-23 12:17:43 +0300
  * 10.1 additions for [MDEV-12052](https://jira.mariadb.org/browse/MDEV-12052) Shutdown crash presumably due to master thread activity
* Merge [Revision #4abc2dd0c7](https://github.com/MariaDB/server/commit/4abc2dd0c7) 2017-05-26 15:11:23 +0300 - Merge 10.0 to 10.1
* [Revision #449a88e1c6](https://github.com/MariaDB/server/commit/449a88e1c6)\
  2017-05-23 12:17:43 +0300
  * [MDEV-12052](https://jira.mariadb.org/browse/MDEV-12052) Shutdown crash presumably due to master thread activity
* [Revision #fde86fc1ed](https://github.com/MariaDB/server/commit/fde86fc1ed)\
  2017-05-23 09:21:28 -0400
  * bump the VERSION
* [Revision #70630e3c92](https://github.com/MariaDB/server/commit/70630e3c92)\
  2017-05-19 15:55:35 +0000
  * Workaround dependency problems (constant rebuilds) in Visual Studio generator
* [Revision #6bc9949210](https://github.com/MariaDB/server/commit/6bc9949210)\
  2017-05-24 20:38:40 +0300
  * Updated list of unstable tests for 10.1.24 release
* [Revision #b430133bb9](https://github.com/MariaDB/server/commit/b430133bb9)\
  2017-05-23 15:35:32 +0200
  * [MDEV-12844](https://jira.mariadb.org/browse/MDEV-12844) numerous issues in MASTER\_GTID\_WAIT()
* [Revision #fc89f5fd40](https://github.com/MariaDB/server/commit/fc89f5fd40)\
  2017-05-20 19:14:06 +0200
  * [MDEV-11335](https://jira.mariadb.org/browse/MDEV-11335) Changing delay\_key\_write option for MyISAM table should not copy rows
* [Revision #c65dd3668b](https://github.com/MariaDB/server/commit/c65dd3668b)\
  2017-05-22 11:02:15 +0200
  * de-obfuscate sys\_vars.delay\_key\_write\_func test
* [Revision #ae76ff4524](https://github.com/MariaDB/server/commit/ae76ff4524)\
  2017-05-22 09:34:39 +0200
  * compiler warning on Win64
* [Revision #ad807aebde](https://github.com/MariaDB/server/commit/ad807aebde)\
  2017-05-21 18:10:33 +0200
  * [MDEV-12612](https://jira.mariadb.org/browse/MDEV-12612) mysqladmin --local flush... to use FLUSH LOCAL
* [Revision #7e0c8fc3fb](https://github.com/MariaDB/server/commit/7e0c8fc3fb)\
  2017-05-21 16:21:15 +0200
  * [MDEV-12389](https://jira.mariadb.org/browse/MDEV-12389) ADD CHECK leaves an orphaned .par file
* [Revision #152aec019d](https://github.com/MariaDB/server/commit/152aec019d)\
  2017-05-21 13:19:38 +0200
  * [MDEV-11650](https://jira.mariadb.org/browse/MDEV-11650) plugins.cracklib\_password\_check, plugins.two\_password\_validations fail in buildbot with valgrind (Conditional jump or move depends on uninitialised value)
* [Revision #fdc1fd6f49](https://github.com/MariaDB/server/commit/fdc1fd6f49)\
  2017-05-20 14:04:03 +0200
  * [MDEV-11311](https://jira.mariadb.org/browse/MDEV-11311) Create federated table does not work as expected.
* [Revision #54caaf6848](https://github.com/MariaDB/server/commit/54caaf6848)\
  2017-05-20 12:32:10 +0200
  * [MDEV-10940](https://jira.mariadb.org/browse/MDEV-10940) plugins.pam still fails in buildbot with valgrind
* [Revision #7e0f40b333](https://github.com/MariaDB/server/commit/7e0f40b333)\
  2017-05-23 18:37:55 +0300
  * [MDEV-12625](https://jira.mariadb.org/browse/MDEV-12625) total\_index\_blocks is uninitialized in ALTER TABLE…ALGORITHM=INPLACE of small tables
* [Revision #a1b6128ded](https://github.com/MariaDB/server/commit/a1b6128ded)\
  2017-05-22 18:27:44 +0000
  * [MDEV-11264](https://jira.mariadb.org/browse/MDEV-11264) Fix DeviceIoControl() usage in innodb.
* Merge [Revision #b61700c221](https://github.com/MariaDB/server/commit/b61700c221) 2017-05-23 08:59:03 +0300 - Merge 10.0 into 10.1
* Merge [Revision #725e47bfb5](https://github.com/MariaDB/server/commit/725e47bfb5) 2017-05-20 00:59:40 +0200 - Merge branch '5.5' into 10.0
* [Revision #7d57ba6e28](https://github.com/MariaDB/server/commit/7d57ba6e28)\
  2017-05-19 13:02:45 +0530
  * [MDEV-11092](https://jira.mariadb.org/browse/MDEV-11092) :- Fix Previous commit of [MDEV-11092](https://jira.mariadb.org/browse/MDEV-11092)
* [Revision #4a846e018d](https://github.com/MariaDB/server/commit/4a846e018d)\
  2017-05-18 19:31:44 +0200
  * Make IF clear.
* [Revision #b5cdf01404](https://github.com/MariaDB/server/commit/b5cdf01404)\
  2017-05-18 17:13:37 +0530
  * [MDEV-11092](https://jira.mariadb.org/browse/MDEV-11092) Assertion \`!writer.checksum\_len || writer.remains == 0' failed
* [Revision #efb9f2617b](https://github.com/MariaDB/server/commit/efb9f2617b)\
  2017-05-17 16:16:54 -0700
  * Fixed the bug [MDEV-12812](https://jira.mariadb.org/browse/MDEV-12812).
* [Revision #7e97163102](https://github.com/MariaDB/server/commit/7e97163102)\
  2017-05-17 14:29:13 -0700
  * Fixed the bug [MDEV-12817](https://jira.mariadb.org/browse/MDEV-12817)/[MDEV-12820](https://jira.mariadb.org/browse/MDEV-12820).
* [Revision #eb30230359](https://github.com/MariaDB/server/commit/eb30230359)\
  2017-05-19 22:27:26 +0200
  * compilation warnings in Connect
* [Revision #6dcc378964](https://github.com/MariaDB/server/commit/6dcc378964)\
  2017-05-18 15:22:45 +0200
  * [MDEV-10788](https://jira.mariadb.org/browse/MDEV-10788) Not able to compile source with -DBUILD\_CONFIG=mysql\_release -DCMAKE\_BUILD\_TYPE=Debug
* [Revision #7c03edf2fe](https://github.com/MariaDB/server/commit/7c03edf2fe)\
  2017-05-17 15:16:24 +0200
  * [MDEV-6262](https://jira.mariadb.org/browse/MDEV-6262) analyze the coverity report on mariadb
* Merge [Revision #70df2bef7a](https://github.com/MariaDB/server/commit/70df2bef7a) 2017-05-22 13:49:37 +0000 - Merge branch 'bb-10.1-wlad' into 10.1
* [Revision #ee4eda40b9](https://github.com/MariaDB/server/commit/ee4eda40b9)\
  2017-05-21 22:19:06 +0000
  * [MDEV-12832](https://jira.mariadb.org/browse/MDEV-12832) : remove libarchive support from mariadb-backup, due to different packaging issues.
* [Revision #2c69c428a7](https://github.com/MariaDB/server/commit/2c69c428a7)\
  2017-05-22 13:33:37 +0300
  * Changing maturity to stable
* [Revision #90c52e5291](https://github.com/MariaDB/server/commit/90c52e5291)\
  2017-05-20 21:49:35 +0300
  * [MDEV-12615](https://jira.mariadb.org/browse/MDEV-12615): InnoDB page compression method snappy mostly does not compress pages
* [Revision #f880200974](https://github.com/MariaDB/server/commit/f880200974)\
  2017-05-20 17:47:07 +0300
  * After-merge fix: Correct the 32-bit XtraDB result diff.
* [Revision #fe291c687d](https://github.com/MariaDB/server/commit/fe291c687d)\
  2017-05-20 08:43:25 +0300
  * After-merge fix: Correct the XtraDB result diff.
* [Revision #45fe62b8d6](https://github.com/MariaDB/server/commit/45fe62b8d6)\
  2017-05-19 22:25:57 +0300
  * Clean up a test
* [Revision #a4d4a5fe82](https://github.com/MariaDB/server/commit/a4d4a5fe82)\
  2017-05-19 14:28:57 +0300
  * After-merge fix for [MDEV-11638](https://jira.mariadb.org/browse/MDEV-11638)
* Merge [Revision #65e1399e64](https://github.com/MariaDB/server/commit/65e1399e64) 2017-05-19 13:59:43 +0300 - Merge 10.0 into 10.1
* [Revision #335c4ab790](https://github.com/MariaDB/server/commit/335c4ab790)\
  2017-05-19 09:51:44 +0300
  * Remove dead code added in merge commit d8b45b0c004edc0b91029b232d7cc9aad02cc822
* [Revision #546a89ca58](https://github.com/MariaDB/server/commit/546a89ca58)\
  2017-05-18 16:16:18 +0300
  * Update xtradb and innodb version to 5.6.36
* [Revision #3c7af6c490](https://github.com/MariaDB/server/commit/3c7af6c490)\
  2017-05-18 15:46:31 +0300
  * Fix xtradb handler compilation post merge
* Merge [Revision #45898c2092](https://github.com/MariaDB/server/commit/45898c2092) 2017-05-18 15:45:55 +0300 - Merge remote-tracking branch 'origin/10.0' into 10.0
* [Revision #648d866150](https://github.com/MariaDB/server/commit/648d866150)\
  2017-05-18 12:24:44 +0200
  * Fixed typo in the case operator.
* [Revision #bc622fb280](https://github.com/MariaDB/server/commit/bc622fb280)\
  2017-05-18 10:47:16 +0300
  * List of unstable tests for 10.0.31 release
* [Revision #0e3ca225ad](https://github.com/MariaDB/server/commit/0e3ca225ad)\
  2017-05-17 22:09:58 +0300
  * Change lower\_case\_file\_system definition to feature MYSQL\_PLUGIN\_IMPORT
* [Revision #8b0db08f36](https://github.com/MariaDB/server/commit/8b0db08f36)\
  2017-05-17 18:39:25 +0300
  * Fix windows compilation in xtradb post-merge
* [Revision #3670d167a6](https://github.com/MariaDB/server/commit/3670d167a6)\
  2017-05-17 16:19:01 +0300
  * Fix tokudb test failures post merge
* [Revision #5fe55b1b02](https://github.com/MariaDB/server/commit/5fe55b1b02)\
  2017-05-17 15:44:11 +0300
  * Fix sys\_vars innodb\_empty\_free\_list\_algorithm\_basic
* Merge [Revision #339a290d22](https://github.com/MariaDB/server/commit/339a290d22) 2017-05-17 15:42:36 +0300 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #934b831281](https://github.com/MariaDB/server/commit/934b831281)\
  2017-05-16 08:24:42 -0700
  * Fixed the bug [MDEV-7791](https://jira.mariadb.org/browse/MDEV-7791).
* [Revision #2e1428c0b5](https://github.com/MariaDB/server/commit/2e1428c0b5)\
  2017-05-15 13:33:59 +0200
  * [MDEV-12799](https://jira.mariadb.org/browse/MDEV-12799) Buffer overflow
* [Revision #e0352fb079](https://github.com/MariaDB/server/commit/e0352fb079)\
  2017-05-15 09:51:01 -0700
  * Fixed the bug [MDEV-7599](https://jira.mariadb.org/browse/MDEV-7599).
* [Revision #9495e018fb](https://github.com/MariaDB/server/commit/9495e018fb)\
  2017-05-12 11:09:27 +0530
  * [MDEV-11718](https://jira.mariadb.org/browse/MDEV-11718) Post-fix
* [Revision #6b97fe067d](https://github.com/MariaDB/server/commit/6b97fe067d)\
  2017-05-09 00:41:45 -0700
  * Fixed the bugs [MDEV-12670](https://jira.mariadb.org/browse/MDEV-12670) and [MDEV-12675](https://jira.mariadb.org/browse/MDEV-12675).
* Merge [Revision #b87873b221](https://github.com/MariaDB/server/commit/b87873b221) 2017-05-17 14:53:28 +0300 - Merge branch 'merge-innodb-5.6' into bb-10.0-vicentiu
* [Revision #0af9818240](https://github.com/MariaDB/server/commit/0af9818240)\
  2017-05-15 17:17:16 +0300
  * 5.6.36
* [Revision #5064623ce4](https://github.com/MariaDB/server/commit/5064623ce4)\
  2017-05-17 12:13:09 +0300
  * Revert "Fix unit test after merge from mysql 5.5.35 perfschema"
* Merge [Revision #d8b45b0c00](https://github.com/MariaDB/server/commit/d8b45b0c00) 2017-05-17 12:11:12 +0300 - Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #360a4a0372](https://github.com/MariaDB/server/commit/360a4a0372)\
  2017-05-16 14:16:11 +0300
  * 5.6.36-82.0
* [Revision #dfeff40706](https://github.com/MariaDB/server/commit/dfeff40706)\
  2017-05-16 17:22:44 +0300
  * Remove tokudb\_dir\_cmd variable
* Merge [Revision #4cdae9c12b](https://github.com/MariaDB/server/commit/4cdae9c12b) 2017-05-16 16:27:50 +0300 - Merge branch 'merge-tokudb-5.6' into 10.0
* [Revision #97c53cdfcc](https://github.com/MariaDB/server/commit/97c53cdfcc)\
  2017-05-16 14:26:11 +0300
  * 5.6.36-82.0
* [Revision #c1b3aaa24e](https://github.com/MariaDB/server/commit/c1b3aaa24e)\
  2017-05-16 14:28:19 +0300
  * Update perfschema version to 5.6.36 post-merge
* Merge [Revision #a111642d32](https://github.com/MariaDB/server/commit/a111642d32) 2017-05-16 14:11:39 +0300 - Merge remote-tracking branch 'connect/10.0' into 10.0
* [Revision #fd0335686b](https://github.com/MariaDB/server/commit/fd0335686b)\
  2017-05-12 11:35:57 +0200
  * [MDEV-12651](https://jira.mariadb.org/browse/MDEV-12651): change error code to ER\_ILLEGAL\_HA in rnd\_pos (ha\_connect.cc)
* [Revision #436070c6e1](https://github.com/MariaDB/server/commit/436070c6e1)\
  2017-05-12 00:33:33 +0200
  * Fix failing test connect.json for [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) Suppressing Uri and dsn from json tables (was MGO) modified: storage/connect/ha\_connect.cc modified: storage/connect/tabdos.cpp modified: storage/connect/tabjson.cpp modified: storage/connect/tabjson.h
* [Revision #1c88b9a8d3](https://github.com/MariaDB/server/commit/1c88b9a8d3)\
  2017-05-11 21:57:21 +0200
  * Fix wrong value of JSON column When null and the column is NOT NULL the value was not reset. modified: storage/connect/tabjson.cpp
* [Revision #531698e0da](https://github.com/MariaDB/server/commit/531698e0da)\
  2017-05-06 00:08:20 +0200
  * Fix [MDEV-12603](https://jira.mariadb.org/browse/MDEV-12603) Insert replaces values in ZIP file modified: storage/connect/filamzip.cpp modified: storage/connect/filamzip.h
* [Revision #a2af3c0d44](https://github.com/MariaDB/server/commit/a2af3c0d44)\
  2017-05-04 18:51:19 +0200
  * Fix [MDEV-12653](https://jira.mariadb.org/browse/MDEV-12653) Cannot add index for ZIP CONNECT table modified: storage/connect/filamzip.cpp modified: storage/connect/ha\_connect.cc modified: storage/connect/tabdos.cpp modified: storage/connect/tabfmt.cpp modified: storage/connect/tabjson.cpp modified: storage/connect/xindex.cpp
* [Revision #6525dc6336](https://github.com/MariaDB/server/commit/6525dc6336)\
  2017-05-03 12:05:05 +0200
  * Disable json tests
* [Revision #1de6440a2e](https://github.com/MariaDB/server/commit/1de6440a2e)\
  2017-05-03 10:32:01 +0200
  * Fix [MDEV-12587](https://jira.mariadb.org/browse/MDEV-12587) MariaDB CONNECT DIR Type - Subfolder Option: SELECT Query Never Ends modified: storage/connect/tabmul.cpp modified: storage/connect/tabmul.h
* [Revision #63b7d9d158](https://github.com/MariaDB/server/commit/63b7d9d158)\
  2017-04-29 19:20:51 +0200
  * Fix [MDEV-12631](https://jira.mariadb.org/browse/MDEV-12631) valgrind warning for zipped tables modified: storage/connect/filamzip.cpp
* [Revision #a091314d27](https://github.com/MariaDB/server/commit/a091314d27)\
  2017-04-22 14:14:11 +0200
  * Fix [MDEV-12520](https://jira.mariadb.org/browse/MDEV-12520): Decimal values can be truncated for JDBC tables modified: storage/connect/jdbconn.cpp
* [Revision #3ac35bb059](https://github.com/MariaDB/server/commit/3ac35bb059)\
  2017-03-28 10:25:21 +0200
  * Fix crash when a line is not ended by \n. modified: storage/connect/filamap.cpp
* [Revision #5de5daa74e](https://github.com/MariaDB/server/commit/5de5daa74e)\
  2017-03-18 12:49:14 +0100
  * Fix [MDEV-12220](https://jira.mariadb.org/browse/MDEV-12220): Crash when doing UPDATE or DELETE on an external table (ODBC, JDBC, MYSQL) with a WHERE clause on an indexed column. Also fix a bugs in TDBEXT::MakeCommand (use of uninitialised Quote) Add in this function the eventual Schema (database) prefixing. modified: storage/connect/connect.cc modified: storage/connect/tabext.cpp
* [Revision #5bc538dd85](https://github.com/MariaDB/server/commit/5bc538dd85)\
  2017-03-11 19:35:03 +0100
  * Commit the 2 last commits merged from 10.1
* [Revision #92d283c026](https://github.com/MariaDB/server/commit/92d283c026)\
  2017-03-06 17:23:56 +0100
  * Fix [MDEV-12142](https://jira.mariadb.org/browse/MDEV-12142) crash when creating CSV table Was an unprepared longjmp (now throw) Also fix a wrong calculation of To\_Line sometimes causing a crash because of buffer overflow. modified: storage/connect/tabdos.cpp
* Merge [Revision #f1861297f0](https://github.com/MariaDB/server/commit/f1861297f0) 2017-05-16 14:07:50 +0300 - Merge branch 'merge-perfschema-5.6' into 10.0
* [Revision #24ff179311](https://github.com/MariaDB/server/commit/24ff179311)\
  2017-05-16 13:53:15 +0300
  * 5.6.36
* Merge [Revision #13a350ac29](https://github.com/MariaDB/server/commit/13a350ac29) 2017-05-19 08:53:58 +0300 - Merge 10.0 into 10.1
* [Revision #54bb04f7ef](https://github.com/MariaDB/server/commit/54bb04f7ef)\
  2017-05-17 16:39:57 +0300
  * Fix some attribute((nonnull)) misuse
* [Revision #a436e349df](https://github.com/MariaDB/server/commit/a436e349df)\
  2017-05-17 16:37:33 +0300
  * ibuf\_get\_volume\_buffered\_hash(): Use a proper type cast
* [Revision #9f57e595b4](https://github.com/MariaDB/server/commit/9f57e595b4)\
  2017-05-17 16:14:41 +0300
  * Refactor trx\_undo\_report\_row\_operation()
* [Revision #8b34aabf86](https://github.com/MariaDB/server/commit/8b34aabf86)\
  2017-05-17 16:09:29 +0300
  * Follow-up to [MDEV-12534](https://jira.mariadb.org/browse/MDEV-12534): Align srv\_sys
* [Revision #9f89b94ba6](https://github.com/MariaDB/server/commit/9f89b94ba6)\
  2017-05-17 14:08:08 +0300
  * [MDEV-12358](https://jira.mariadb.org/browse/MDEV-12358) Work around what looks like a bug in GCC 7.1.0
* [Revision #e22d86a3eb](https://github.com/MariaDB/server/commit/e22d86a3eb)\
  2017-05-17 13:49:51 +0300
  * fil\_create\_new\_single\_table\_tablespace(): Correct a bogus nonnull attribute
* [Revision #956d2540c4](https://github.com/MariaDB/server/commit/956d2540c4)\
  2017-05-17 10:27:01 +0300
  * Remove redundant UT\_LIST\_INIT() calls
* [Revision #4754f88cff](https://github.com/MariaDB/server/commit/4754f88cff)\
  2017-05-16 17:45:22 +0300
  * Never pass NULL to innobase\_get\_stmt()
* [Revision #7972da8aa1](https://github.com/MariaDB/server/commit/7972da8aa1)\
  2017-05-16 20:08:47 +0300
  * Silence bogus GCC 7 warnings -Wimplicit-fallthrough
* [Revision #492c1e4145](https://github.com/MariaDB/server/commit/492c1e4145)\
  2017-05-16 18:33:51 +0300
  * Fix an incorrect debug assertion
* [Revision #b8187fd005](https://github.com/MariaDB/server/commit/b8187fd005)\
  2017-05-16 17:47:04 +0300
  * [MDEV-12071](https://jira.mariadb.org/browse/MDEV-12071) storage/xtradb/handler/ha\_innodb.cc: Cannot assign const\_iterator to iterator
* [Revision #e63e2fe206](https://github.com/MariaDB/server/commit/e63e2fe206)\
  2017-05-16 17:40:52 +0300
  * Fix warnings in innochecksum compilation
* [Revision #8e1056bce0](https://github.com/MariaDB/server/commit/8e1056bce0)\
  2017-05-16 13:14:03 +0200
  * [MDEV-12216](https://jira.mariadb.org/browse/MDEV-12216) main.mysqld--help 'unix' test is failing when profiling support is not present
* [Revision #314f32c8c2](https://github.com/MariaDB/server/commit/314f32c8c2)\
  2017-05-16 12:42:53 +0200
  * [MDEV-5477](https://jira.mariadb.org/browse/MDEV-5477) sphinxSE GROUP BY on multiple attributes
* [Revision #a3cf69e2e5](https://github.com/MariaDB/server/commit/a3cf69e2e5)\
  2017-05-13 13:52:58 +0200
  * [MDEV-10936](https://jira.mariadb.org/browse/MDEV-10936) CONNECT engine JDBC type can't find JdbcInterface
* [Revision #a8773ef380](https://github.com/MariaDB/server/commit/a8773ef380)\
  2017-05-13 13:00:18 +0200
  * [MDEV-12660](https://jira.mariadb.org/browse/MDEV-12660) inconsistent mysql\_stmt\_close
* [Revision #a65623b3eb](https://github.com/MariaDB/server/commit/a65623b3eb)\
  2017-05-12 16:52:09 +0200
  * [MDEV-11883](https://jira.mariadb.org/browse/MDEV-11883) MariaDB crashes with out-of-memory when query information\_schema
* [Revision #71b4503242](https://github.com/MariaDB/server/commit/71b4503242)\
  2017-05-12 15:10:17 +0200
  * [MDEV-9998](https://jira.mariadb.org/browse/MDEV-9998) Fix issues caught by Clang's -Wpointer-bool-conversion warning
* [Revision #f9264280d6](https://github.com/MariaDB/server/commit/f9264280d6)\
  2017-05-12 14:27:49 +0200
  * [MDEV-12761](https://jira.mariadb.org/browse/MDEV-12761) Error return from external\_lock make the server crash
* [Revision #52aa200919](https://github.com/MariaDB/server/commit/52aa200919)\
  2017-05-11 19:48:42 +0200
  * [MDEV-12420](https://jira.mariadb.org/browse/MDEV-12420) max\_recursive\_iterations did not prevent a stack-overflow and segfault
* [Revision #602b5e4c49](https://github.com/MariaDB/server/commit/602b5e4c49)\
  2017-04-18 17:20:34 +1000
  * WIP: global readonly variable pcre\_frame\_size
* [Revision #b30311e52a](https://github.com/MariaDB/server/commit/b30311e52a)\
  2017-04-09 13:30:59 +1000
  * [MDEV-12420](https://jira.mariadb.org/browse/MDEV-12420): pcre recursion overflow test case
* [Revision #fbc057ad36](https://github.com/MariaDB/server/commit/fbc057ad36)\
  2017-04-09 12:54:33 +1000
  * [MDEV-12420](https://jira.mariadb.org/browse/MDEV-12420): add full list of pcre error messages
* [Revision #d672f88ef7](https://github.com/MariaDB/server/commit/d672f88ef7)\
  2017-04-08 22:47:56 +1000
  * [MDEV-12420](https://jira.mariadb.org/browse/MDEV-12420): PCRE stack overflow
* [Revision #217b8115c8](https://github.com/MariaDB/server/commit/217b8115c8)\
  2017-05-15 12:02:19 +0300
  * [MDEV-12188](https://jira.mariadb.org/browse/MDEV-12188) information schema - errors populating fail to free memory, unlock mutexes
* [Revision #8417252b04](https://github.com/MariaDB/server/commit/8417252b04)\
  2017-05-15 10:26:42 +0300
  * Fix the Solaris compilation after [MDEV-12674](https://jira.mariadb.org/browse/MDEV-12674)
* [Revision #d0eb4ee96b](https://github.com/MariaDB/server/commit/d0eb4ee96b)\
  2017-05-17 19:56:51 +0000
  * Backport aws kms build fixes from 10.2
* [Revision #9dffa3072c](https://github.com/MariaDB/server/commit/9dffa3072c)\
  2017-05-16 17:24:21 +0000
  * [MDEV-12810](https://jira.mariadb.org/browse/MDEV-12810) - force static build of crc library
* [Revision #40c7778e05](https://github.com/MariaDB/server/commit/40c7778e05)\
  2017-05-16 17:11:25 +0000
  * [MDEV-12814](https://jira.mariadb.org/browse/MDEV-12814) mariadb-backup : don't try io throttling in copy-back
* [Revision #f302a3cf9d](https://github.com/MariaDB/server/commit/f302a3cf9d)\
  2017-04-28 10:07:03 +0300
  * [MDEV-12593](https://jira.mariadb.org/browse/MDEV-12593): InnoDB page compression should use lz4\_compress\_default if
* [Revision #febe88198e](https://github.com/MariaDB/server/commit/febe88198e)\
  2017-05-17 08:54:16 +0300
  * Make some variables const in fil\_iterate()
* [Revision #408ef65f84](https://github.com/MariaDB/server/commit/408ef65f84)\
  2017-05-16 17:45:22 +0300
  * Never pass NULL to innobase\_get\_stmt()
* [Revision #71cd205956](https://github.com/MariaDB/server/commit/71cd205956)\
  2017-05-16 20:08:47 +0300
  * Silence bogus GCC 7 warnings -Wimplicit-fallthrough
* Merge [Revision #03dca7a333](https://github.com/MariaDB/server/commit/03dca7a333) 2017-05-12 13:12:45 +0300 - Merge 10.0 into 10.1
* [Revision #ff16609374](https://github.com/MariaDB/server/commit/ff16609374)\
  2017-05-11 21:12:37 +0300
  * [MDEV-12674](https://jira.mariadb.org/browse/MDEV-12674) Innodb\_row\_lock\_current\_waits has overflow
* [Revision #d7cfe2c4f3](https://github.com/MariaDB/server/commit/d7cfe2c4f3)\
  2017-05-09 13:40:42 +0300
  * [MDEV-12253](https://jira.mariadb.org/browse/MDEV-12253) post-fix: Do not leak memory in crash recovery
* [Revision #9d2c1d09aa](https://github.com/MariaDB/server/commit/9d2c1d09aa)\
  2017-05-06 23:10:52 +0300
  * [MDEV-12253](https://jira.mariadb.org/browse/MDEV-12253) post-push fix: buf\_read\_page\_low() can return DB\_ERROR
* Merge [Revision #c92168fcd2](https://github.com/MariaDB/server/commit/c92168fcd2) 2017-05-09 12:40:48 +0300 - Merge pull request #389 from iangilfillan/10.1
* [Revision #44eca0f512](https://github.com/MariaDB/server/commit/44eca0f512)\
  2017-05-09 11:24:22 +0200
  * galera\_new\_cluster man page and sh typo
* [Revision #fbdf18f86e](https://github.com/MariaDB/server/commit/fbdf18f86e)\
  2017-05-08 19:23:39 +0200
  * [MDEV-12696](https://jira.mariadb.org/browse/MDEV-12696) Crash with LOAD XML and non-updatable VIEW column
* Merge [Revision #d738722eee](https://github.com/MariaDB/server/commit/d738722eee) 2017-05-08 14:58:49 +0200 - Merge branch '10.0' into 10.1
* Merge [Revision #1c418df722](https://github.com/MariaDB/server/commit/1c418df722) 2017-05-08 12:12:48 +0200 - Merge branch '5.5' into 10.0
* [Revision #15f9931f6d](https://github.com/MariaDB/server/commit/15f9931f6d)\
  2017-05-04 22:45:32 -0700
  * Fixed the bug [MDEV-12673](https://jira.mariadb.org/browse/MDEV-12673).
* [Revision #14fca28ea4](https://github.com/MariaDB/server/commit/14fca28ea4)\
  2017-05-02 19:11:21 -0400
  * bump the VERSION
* [Revision #dbe2c3c5f2](https://github.com/MariaDB/server/commit/dbe2c3c5f2)\
  2017-04-30 13:29:56 +1000
  * mysqld\_safe\_help - remove warning
* [Revision #fc25437aff](https://github.com/MariaDB/server/commit/fc25437aff)\
  2017-05-05 13:08:23 +0300
  * [MDEV-10104](https://jira.mariadb.org/browse/MDEV-10104) Table lock race condition with replication
* [Revision #e3521ab904](https://github.com/MariaDB/server/commit/e3521ab904)\
  2017-05-05 13:03:41 +0300
  * Fixed some bugs in fork\_big.pl which caused some tests to die early
* [Revision #bc5c1d9970](https://github.com/MariaDB/server/commit/bc5c1d9970)\
  2017-05-05 14:04:18 +0300
  * [MDEV-12635](https://jira.mariadb.org/browse/MDEV-12635) innodb.log\_file\_size fails when run with Valgrind
* [Revision #a7c5fd6b4e](https://github.com/MariaDB/server/commit/a7c5fd6b4e)\
  2017-05-03 15:49:19 +0200
  * restore dependencies, removed in f2dc04abea
* [Revision #e1efeaa550](https://github.com/MariaDB/server/commit/e1efeaa550)\
  2017-05-08 12:04:08 +0300
  * [MDEV-12628](https://jira.mariadb.org/browse/MDEV-12628): innodb.innodb\_bug14147491 sporadically fails in buildbot due to wrong error number
* [Revision #57e667357a](https://github.com/MariaDB/server/commit/57e667357a)\
  2017-05-08 11:23:02 +0300
  * [MDEV-12627](https://jira.mariadb.org/browse/MDEV-12627): innodb.innodb\_bug14147491 does not do proper cleanup
* [Revision #c7d85db1c4](https://github.com/MariaDB/server/commit/c7d85db1c4)\
  2017-05-06 01:55:45 +0200
  * Fix AWS key managemennt compile error on Linux
* [Revision #13752faa4d](https://github.com/MariaDB/server/commit/13752faa4d)\
  2017-05-05 16:37:00 +0000
  * Fix compilation of aws\_key\_management plugin
* [Revision #bc6426e44d](https://github.com/MariaDB/server/commit/bc6426e44d)\
  2017-05-02 19:10:01 -0400
  * bump the VERSION
* Merge [Revision #63e4be267b](https://github.com/MariaDB/server/commit/63e4be267b) 2017-05-02 16:31:24 +0300 - Merge pull request #362 from grooverdan/10.1-MDEV-XXXX-mysqltest-replace-regex-vars
* [Revision #bbef745574](https://github.com/MariaDB/server/commit/bbef745574)\
  2017-04-13 00:19:08 +1000
  * tests: sys\_vars.sysvars\_wsrep
* [Revision #d59b94e7fd](https://github.com/MariaDB/server/commit/d59b94e7fd)\
  2017-04-13 16:14:21 +1000
  * Add replace\_regex to not ignore the regex in "$var /regex/val/"
* Merge [Revision #2d457843d6](https://github.com/MariaDB/server/commit/2d457843d6) 2017-05-02 16:29:40 +0300 - Merge pull request #375 from grooverdan/10.1-galera\_new\_cluster--help
* [Revision #a9a38fcd7a](https://github.com/MariaDB/server/commit/a9a38fcd7a)\
  2017-04-30 14:47:34 +1000
  * wsrep\_new\_cluster: Add -h and --help options
* Merge [Revision #6b8225ffe6](https://github.com/MariaDB/server/commit/6b8225ffe6) 2017-05-02 16:28:25 +0300 - Merge pull request #371 from grooverdan/10.1-wsrep-this\_not\_null
* [Revision #3d4882feb2](https://github.com/MariaDB/server/commit/3d4882feb2)\
  2017-04-30 13:58:18 +1000
  * Remove compile warning - "this" canot be null

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
