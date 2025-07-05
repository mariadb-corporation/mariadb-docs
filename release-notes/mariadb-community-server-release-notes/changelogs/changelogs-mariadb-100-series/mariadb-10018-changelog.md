# MariaDB 10.0.18 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.18)[Release Notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10018-release-notes.md)[Changelog](mariadb-10018-changelog.md)[Overview of 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)

**Release date:** 7 May 2015

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10018-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #5c83368](https://github.com/MariaDB/server/commit/5c83368)\
  2015-05-06 12:41:21 +0200
  * Merge [MDEV-8103](https://jira.mariadb.org/browse/MDEV-8103) into 10.0
* [Revision #ef99edf](https://github.com/MariaDB/server/commit/ef99edf)\
  2015-05-06 12:24:15 +0200
  * [MDEV-8103](https://jira.mariadb.org/browse/MDEV-8103): Missing DBUG\_RETURN in open\_table\_uncached()
* [Revision #b9c89ad](https://github.com/MariaDB/server/commit/b9c89ad)\
  2015-05-05 22:37:00 +0200
  * Merge branch 'Buggynours:10.0' into 10.0
* [Revision #a82f475](https://github.com/MariaDB/server/commit/a82f475)\
  2015-05-05 11:37:21 +0200
  * Fix a regression bug on (XML) HTML tables.
* [Revision #c09c265](https://github.com/MariaDB/server/commit/c09c265)\
  2015-05-05 22:05:05 +0200
  * Fix [MDEV-8090](https://jira.mariadb.org/browse/MDEV-8090) in tabmysql.cpp
* [Revision #95797b9](https://github.com/MariaDB/server/commit/95797b9)\
  2015-05-05 20:23:22 +0200
  * [MDEV-8096](https://jira.mariadb.org/browse/MDEV-8096) vio timeouts are multiplied by 1000 for ssl
* [Revision #d3a3adb](https://github.com/MariaDB/server/commit/d3a3adb)\
  2015-05-05 21:19:53 +0300
  * [MDEV-7985](https://jira.mariadb.org/browse/MDEV-7985): MySQL Users Break when Migrating to MariaDB, part 2
* [Revision #7b70b0d](https://github.com/MariaDB/server/commit/7b70b0d)\
  2015-05-05 16:31:53 +0200
  * Merge branch 'bb-10.0-serg' into 10.0
* [Revision #9304737](https://github.com/MariaDB/server/commit/9304737)\
  2015-05-05 16:28:23 +0200
  * mroonga doesn't work in embedded anymore
* [Revision #1d3ea9e](https://github.com/MariaDB/server/commit/1d3ea9e)\
  2015-05-05 15:23:47 +0200
  * perfschema 5.6.24
* [Revision #e4fde09](https://github.com/MariaDB/server/commit/e4fde09)\
  2015-05-05 15:39:32 +0400
  * Temporarily disabling Mroonga on Solaris (See [MDEV-7440](https://jira.mariadb.org/browse/MDEV-7440) Build fails in libgroonga on Solaris)
* [Revision #73c2356](https://github.com/MariaDB/server/commit/73c2356)\
  2015-05-05 13:22:09 +0400
  * [MDEV-7778](https://jira.mariadb.org/browse/MDEV-7778) impossible create copy of table, if table contain default value for timestamp field [MDEV-8082](https://jira.mariadb.org/browse/MDEV-8082) ON UPDATE is not preserved by CREATE TABLE .. SELECT
* [Revision #dd0207b](https://github.com/MariaDB/server/commit/dd0207b)\
  2015-05-05 08:53:52 +0200
  * .gitignore: add generated mroonga \*.result files
* [Revision #d08b7ed](https://github.com/MariaDB/server/commit/d08b7ed)\
  2015-05-05 08:19:20 +0200
  * Merge branch 'Kentoku:10.0' into 10.0
* [Revision #d4dd936](https://github.com/MariaDB/server/commit/d4dd936)\
  2015-05-05 16:26:45 +0900
  * Merge branch 'ks-Mroonga-5.02' into 10.0
* [Revision #5dcb111](https://github.com/MariaDB/server/commit/5dcb111)\
  2015-05-05 07:50:31 +0200
  * Merge branch 'Buggynours:10.0' into 10.0
* [Revision #872cbb8](https://github.com/MariaDB/server/commit/872cbb8)\
  2015-05-05 13:48:54 +0900
  * revert CMakeList.txt at groonga-normalizer-mysql/normalizers
* [Revision #bbcc8e6](https://github.com/MariaDB/server/commit/bbcc8e6)\
  2015-05-05 00:08:58 +0200
  * XtraDB-5.6.23-72.1
* [Revision #70a3fec](https://github.com/MariaDB/server/commit/70a3fec)\
  2015-05-05 00:06:23 +0200
  * InnoDB-5.6.24
* [Revision #d33cef1](https://github.com/MariaDB/server/commit/d33cef1)\
  2015-05-05 05:26:06 +0900
  * add -fPIC for groonga-normalizer-mysql
* [Revision #0b4f506](https://github.com/MariaDB/server/commit/0b4f506)\
  2015-05-04 22:25:57 +0200
  * Merge branch 'merge-pcre' into 10.0
* [Revision #c4cc91c](https://github.com/MariaDB/server/commit/c4cc91c)\
  2015-05-04 22:19:22 +0200
  * 8.37
* [Revision #a4416ab](https://github.com/MariaDB/server/commit/a4416ab)\
  2015-05-04 22:17:04 +0200
  * 5.6.23-72.1
* [Revision #d71d411](https://github.com/MariaDB/server/commit/d71d411)\
  2015-05-04 22:16:00 +0200
  * 5.6.24
* [Revision #085297a](https://github.com/MariaDB/server/commit/085297a)\
  2015-05-04 22:13:46 +0200
  * 5.6.24
* [Revision #6c5ee86](https://github.com/MariaDB/server/commit/6c5ee86)\
  2015-05-04 22:09:21 +0200
  * Null-merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #41e8126](https://github.com/MariaDB/server/commit/41e8126)\
  2015-05-04 22:08:06 +0200
  * Null-merge branch 'merge-sphinx' into 10.0
* [Revision #18b9f48](https://github.com/MariaDB/server/commit/18b9f48)\
  2015-05-04 22:05:39 +0200
  * Null-merge branch 'merge-innodb-5.6' into 10.0
* [Revision #49c853f](https://github.com/MariaDB/server/commit/49c853f)\
  2015-05-04 22:00:24 +0200
  * Merge branch '5.5' into 10.0
* [Revision #9130cc7](https://github.com/MariaDB/server/commit/9130cc7)\
  2015-05-05 03:09:34 +0900
  * update Spider to 3.2.21
* [Revision #d18becc](https://github.com/MariaDB/server/commit/d18becc)\
  2015-05-05 02:43:19 +0900
  * add -fPIC for groonga-normalizer-mysql
* [Revision #e2a87bd](https://github.com/MariaDB/server/commit/e2a87bd)\
  2015-05-04 19:20:59 +0200
  * move to storage/sphinx
* [Revision #6d06fbb](https://github.com/MariaDB/server/commit/6d06fbb)\
  2015-05-04 19:17:21 +0200
  * move to storage/innobase
* [Revision #14a142f](https://github.com/MariaDB/server/commit/14a142f)\
  2015-05-04 19:15:28 +0200
  * move to storage/xtradb
* [Revision #ae18a28](https://github.com/MariaDB/server/commit/ae18a28)\
  2015-05-04 08:32:05 +0200
  * [MDEV-7973](https://jira.mariadb.org/browse/MDEV-7973) bigint fail with gcc 5.0
* [Revision #2983686](https://github.com/MariaDB/server/commit/2983686)\
  2015-05-03 18:26:02 +0200
  * [MDEV-8045](https://jira.mariadb.org/browse/MDEV-8045) Assertion \`0' fails in Protocol::end\_statement on CREATE VIEW after another connection aborted
* [Revision #8e797ae](https://github.com/MariaDB/server/commit/8e797ae)\
  2015-05-03 14:43:34 +0200
  * [MDEV-8014](https://jira.mariadb.org/browse/MDEV-8014) MariaDB client can hang in an infinite loop
* [Revision #aa50956](https://github.com/MariaDB/server/commit/aa50956)\
  2015-05-03 11:51:31 +0200
  * [MDEV-7781](https://jira.mariadb.org/browse/MDEV-7781) cannot install/uninstall plugins during bootstrap
* [Revision #dbe97bc](https://github.com/MariaDB/server/commit/dbe97bc)\
  2015-05-03 11:51:22 +0200
  * clarify the test case
* [Revision #c8c51ce](https://github.com/MariaDB/server/commit/c8c51ce)\
  2015-05-03 11:32:13 +0200
  * [MDEV-7390](https://jira.mariadb.org/browse/MDEV-7390) alter online table xxxx (no options) should be possible
* [Revision #532de70](https://github.com/MariaDB/server/commit/532de70)\
  2015-05-03 11:31:04 +0200
  * more tests, moving code around
* [Revision #a229750](https://github.com/MariaDB/server/commit/a229750)\
  2015-05-03 11:22:25 +0200
  * Fix connection thread handling to address [MDEV-6282](https://jira.mariadb.org/browse/MDEV-6282) [MDEV-6345](https://jira.mariadb.org/browse/MDEV-6345) and [MDEV-6784](https://jira.mariadb.org/browse/MDEV-6784)
* [Revision #ef1eb9c](https://github.com/MariaDB/server/commit/ef1eb9c)\
  2015-05-02 12:32:10 +0200
  * SSL: Verbosely report SSL initialization errors
* [Revision #601dcd4](https://github.com/MariaDB/server/commit/601dcd4)\
  2015-05-02 08:46:04 +0200
  * [MDEV-7794](https://jira.mariadb.org/browse/MDEV-7794) MariaDB - mysql-test - fips: some ssl tests with cipher are failing
* [Revision #7e7dd8e](https://github.com/MariaDB/server/commit/7e7dd8e)\
  2015-05-02 08:45:10 +0200
  * [MDEV-7695](https://jira.mariadb.org/browse/MDEV-7695) MariaDB - ssl - fips: can not connect with --ssl-cipher=DHE-RSA-AES256-SHA - handshake failure
* [Revision #e1e1f94](https://github.com/MariaDB/server/commit/e1e1f94)\
  2015-05-01 18:53:18 +0200
  * remove unused file and unnecessary #include
* [Revision #93c563d](https://github.com/MariaDB/server/commit/93c563d)\
  2015-05-01 18:52:29 +0200
  * [MDEV-7788](https://jira.mariadb.org/browse/MDEV-7788) my\_md5 crashes with openssl in fips mode
* [Revision #cc12a35](https://github.com/MariaDB/server/commit/cc12a35)\
  2015-05-01 17:56:47 +0200
  * [MDEV-7697](https://jira.mariadb.org/browse/MDEV-7697) Client reports ERROR 2006 (MySQL server has gone away) or ERROR 2013 (Lost connection to MySQL server during query) while executing AES\* functions under SSL
* [Revision #f875c9f](https://github.com/MariaDB/server/commit/f875c9f)\
  2015-04-30 19:48:11 +0200
  * [MDEV-5114](https://jira.mariadb.org/browse/MDEV-5114) seconds\_behind\_master flips to 0 & spikes back, when running show slaves status
* [Revision #e6d918c](https://github.com/MariaDB/server/commit/e6d918c)\
  2015-05-03 06:44:08 +0200
  * init\_status\_vars() was not invoked for embedded
* [Revision #91f8931](https://github.com/MariaDB/server/commit/91f8931)\
  2015-05-03 06:51:33 +0200
  * reformat long strings
* [Revision #6c55e52](https://github.com/MariaDB/server/commit/6c55e52)\
  2015-03-13 20:12:22 +0200
  * [MDEV-7774](https://jira.mariadb.org/browse/MDEV-7774): Crash when dropping user within rebuild\_role\_grants
* [Revision #acab0fa](https://github.com/MariaDB/server/commit/acab0fa)\
  2015-05-02 21:46:32 +0300
  * [MDEV-7038](https://jira.mariadb.org/browse/MDEV-7038) Assertion \`status\_var.memory\_used == 0' failed in THD::THD() on disconnect after executing EXPLAIN for multi-table UPDATE
* [Revision #f5b05a1](https://github.com/MariaDB/server/commit/f5b05a1)\
  2015-05-01 15:59:12 +0200
  * Fix bug on updating JSON expanded values
* [Revision #37093eb](https://github.com/MariaDB/server/commit/37093eb)\
  2015-05-01 14:51:50 +0300
  * [MDEV-8079](https://jira.mariadb.org/browse/MDEV-8079): Crash when running MariaDB Debug with InnoDB on Windows
* [Revision #2bb0e71](https://github.com/MariaDB/server/commit/2bb0e71)\
  2015-03-12 07:08:31 +1100
  * Alter online table x (no options) possible
* [Revision #320240b](https://github.com/MariaDB/server/commit/320240b)\
  2015-04-30 10:23:36 -0400
  * Merge test for bug#72594 from upstream
* [Revision #a0fdb25](https://github.com/MariaDB/server/commit/a0fdb25)\
  2015-04-30 04:44:30 +0900
  * Update Mroonga to the latest version on 2015-04-30T04:44:30+0900
* [Revision #4c87f72](https://github.com/MariaDB/server/commit/4c87f72)\
  2015-04-29 16:24:52 +0200
  * Merge branch '5.5' into bb-5.5-serg
* [Revision #a4477d2](https://github.com/MariaDB/server/commit/a4477d2)\
  2015-04-29 14:14:45 +0300
  * Fix failing test cases for [MDEV-7912](https://jira.mariadb.org/browse/MDEV-7912) patch
* [Revision #f632b51](https://github.com/MariaDB/server/commit/f632b51)\
  2015-04-28 21:27:43 +0200
  * [MDEV-7987](https://jira.mariadb.org/browse/MDEV-7987) Fatal error: Please read "Security" section of the manual to find out how to run mysqld as root!
* [Revision #6f17e23](https://github.com/MariaDB/server/commit/6f17e23)\
  2015-04-28 21:24:32 +0200
  * post-merge fixes
* [Revision #9088f26](https://github.com/MariaDB/server/commit/9088f26)\
  2015-04-29 11:29:25 +0200
  * [MDEV-7802](https://jira.mariadb.org/browse/MDEV-7802): group commit status variable addition
* [Revision #f9c02d7](https://github.com/MariaDB/server/commit/f9c02d7)\
  2015-04-28 21:11:49 +0200
  * Merge branch 'openquery/[MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916)-maria-5.5-check\_view-r4408' into 5.5
* [Revision #fbab068](https://github.com/MariaDB/server/commit/fbab068)\
  2015-04-28 13:57:21 +0200
  * post-merge changes, fixes, and tests
* [Revision #67a3ddf](https://github.com/MariaDB/server/commit/67a3ddf)\
  2015-04-28 13:54:37 +0200
  * Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #40e9560](https://github.com/MariaDB/server/commit/40e9560)\
  2015-04-28 13:42:58 +0200
  * percona-server-5.5.42-37.1.tar.gz
* [Revision #c581ae0](https://github.com/MariaDB/server/commit/c581ae0)\
  2015-04-28 13:37:54 +0200
  * Null-merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #a5fa434](https://github.com/MariaDB/server/commit/a5fa434)\
  2015-04-28 15:31:49 +0500
  * [MDEV-7779](https://jira.mariadb.org/browse/MDEV-7779) View definition changes upon creation. Fixed by using POINT instead of ST\_POINT in the item. Later need to fix that with proper ST\_POINT implementation
* [Revision #4c174fc](https://github.com/MariaDB/server/commit/4c174fc)\
  2015-04-28 15:28:29 +0300
  * [MDEV-8020](https://jira.mariadb.org/browse/MDEV-8020): innodb.innodb-[MDEV-7055](https://jira.mariadb.org/browse/MDEV-7055) produces valgrind warnings in buildbot
* [Revision #ac2b92c](https://github.com/MariaDB/server/commit/ac2b92c)\
  2015-04-28 15:09:04 +0300
  * [MDEV-7912](https://jira.mariadb.org/browse/MDEV-7912) multitable delete with wrongly set sort\_buffer\_size crashes in merge\_buffers
* [Revision #ed701c6](https://github.com/MariaDB/server/commit/ed701c6)\
  2015-04-28 11:56:54 +0200
  * [MDEV-7864](https://jira.mariadb.org/browse/MDEV-7864): Slave SQL: stopping on non-last RBR event with annotations results in SEGV (signal 11)
* [Revision #fd39c56](https://github.com/MariaDB/server/commit/fd39c56)\
  2015-04-27 23:37:51 +0200
  * move to storage/xtradb/
* [Revision #0f12ada](https://github.com/MariaDB/server/commit/0f12ada)\
  2015-04-27 21:04:06 +0200
  * Merge remote-tracking branch 'mysql/5.5' into 5.5
* [Revision #e4df6e5](https://github.com/MariaDB/server/commit/e4df6e5)\
  2015-04-27 16:19:54 +0200
  * Merge commit 'tokudb-engine/tokudb-7.5.6' into 5.5
* [Revision #2f446f2](https://github.com/MariaDB/server/commit/2f446f2)\
  2015-04-27 16:04:39 +0200
  * Merge commit 'tokudb-ft-index/tokudb-7.5.6' into 5.5
* [Revision #939a233](https://github.com/MariaDB/server/commit/939a233)\
  2015-04-27 15:56:39 +0200
  * Merge remote-tracking branch 'openquery/[MDEV-8060](https://jira.mariadb.org/browse/MDEV-8060)-shm-path' into 5.5
* [Revision #245cc73](https://github.com/MariaDB/server/commit/245cc73)\
  2015-04-27 12:47:39 +0200
  * [MDEV-7434](https://jira.mariadb.org/browse/MDEV-7434) XtraDB does not build on Solaris
* [Revision #e26b207](https://github.com/MariaDB/server/commit/e26b207)\
  2015-04-26 16:27:41 +0200
  * [MDEV-7938](https://jira.mariadb.org/browse/MDEV-7938) MariaDB Crashes Suddenly while writing binlogs
* [Revision #053143e](https://github.com/MariaDB/server/commit/053143e)\
  2015-04-25 21:56:46 +0200
  * [MDEV-7883](https://jira.mariadb.org/browse/MDEV-7883) Segmentation failure when running mysqladmin -u root -p
* [Revision #18215dd](https://github.com/MariaDB/server/commit/18215dd)\
  2015-04-25 17:22:46 +0200
  * [MDEV-7859](https://jira.mariadb.org/browse/MDEV-7859) SSL hostname verification fails for long subject names
* [Revision #9fd65db](https://github.com/MariaDB/server/commit/9fd65db)\
  2015-04-25 00:19:20 +0200
  * [MDEV-7585](https://jira.mariadb.org/browse/MDEV-7585) Assertion \`thd->is\_error() || kill\_errno || thd->killed == ABORT\_QUERY' failed in ha\_rows filesort
* [Revision #8e78160](https://github.com/MariaDB/server/commit/8e78160)\
  2015-04-24 21:41:00 +0200
  * [MDEV-6870](https://jira.mariadb.org/browse/MDEV-6870) Not possible to use FIFO file as a general\_log file
* [Revision #c05d431](https://github.com/MariaDB/server/commit/c05d431)\
  2015-04-24 21:03:43 +0200
  * bug: crash when sync() or close() of a log file fails on shutdown
* [Revision #8f499c3](https://github.com/MariaDB/server/commit/8f499c3)\
  2015-04-24 21:02:37 +0200
  * bug: debug assert crash when seek on log file fails
* [Revision #5fd0088](https://github.com/MariaDB/server/commit/5fd0088)\
  2015-04-27 15:31:12 +0200
  * [MDEV-8058](https://jira.mariadb.org/browse/MDEV-8058): funcs\_1.innodb\_views and funcs\_1.memory\_views fail
* [Revision #574227c](https://github.com/MariaDB/server/commit/574227c)\
  2015-04-27 21:15:23 +1000
  * /run/shm is the general replacement for /dev/shm in newer distros
* [Revision #f832021](https://github.com/MariaDB/server/commit/f832021)\
  2015-04-23 08:26:57 +0200
  * [MDEV-7126](https://jira.mariadb.org/browse/MDEV-7126) replication slave - deadlock in terminate\_slave\_thread with stop slave and show variables of replication filters and show global status
* [Revision #2d6c0a5](https://github.com/MariaDB/server/commit/2d6c0a5)\
  2015-04-24 13:44:22 +0200
  * Merge pull request #39 from openquery/[MDEV-7977](https://jira.mariadb.org/browse/MDEV-7977)-mutex-unlock\_LOCK\_log-in-MYSQL\_BIN\_LOG\_write\_incident
* [Revision #060ec5b](https://github.com/MariaDB/server/commit/060ec5b)\
  2015-04-24 12:38:59 +0200
  * [MDEV-7130](https://jira.mariadb.org/browse/MDEV-7130): MASTER\_POS\_WAIT(log\_name,log\_pos,timeout,"connection\_name") hangs, does not respect the timeout
* [Revision #44d1e85](https://github.com/MariaDB/server/commit/44d1e85)\
  2015-04-24 11:00:34 +0400
  * [MDEV-7649](https://jira.mariadb.org/browse/MDEV-7649) wrong result when comparing utf8 column with an invalid literal
* [Revision #f9b2704](https://github.com/MariaDB/server/commit/f9b2704)\
  2015-04-23 23:06:14 +0300
  * Testcase for: [MDEV-7893](https://jira.mariadb.org/browse/MDEV-7893) table\_elimination works wrong ...
* [Revision #2010971](https://github.com/MariaDB/server/commit/2010971)\
  2015-04-14 23:18:54 +0200
  * [MDEV-6892](https://jira.mariadb.org/browse/MDEV-6892): WHERE does not apply
* [Revision #b616991](https://github.com/MariaDB/server/commit/b616991)\
  2015-04-23 14:09:15 +0200
  * [MDEV-8031](https://jira.mariadb.org/browse/MDEV-8031): Parallel replication stops on "connection killed" error (probably incorrectly handled deadlock kill)
* [Revision #8cbaafd](https://github.com/MariaDB/server/commit/8cbaafd)\
  2015-04-22 10:14:11 +0200
  * [MDEV-8018](https://jira.mariadb.org/browse/MDEV-8018): main.multi\_update fails with --ps-protocol
* [Revision #e428c80](https://github.com/MariaDB/server/commit/e428c80)\
  2015-04-21 15:41:01 +0300
  * [MDEV-7911](https://jira.mariadb.org/browse/MDEV-7911): crash in Item\_cond::eval\_not\_null\_tables
* [Revision #4760528](https://github.com/MariaDB/server/commit/4760528)\
  2015-04-21 10:16:14 +0200
  * [MDEV-8029](https://jira.mariadb.org/browse/MDEV-8029): test failure in rpl.rpl\_parallel\_temptable
* [Revision #519ad0f](https://github.com/MariaDB/server/commit/519ad0f)\
  2015-04-20 12:59:46 +0200
  * [MDEV-8016](https://jira.mariadb.org/browse/MDEV-8016): Replication aborts on DROP /\*!40005 TEMPORARY \*/ TABLE IF EXISTS
* [Revision #0759568](https://github.com/MariaDB/server/commit/0759568)\
  2015-04-20 18:36:19 +1000
  * test case for install plugin on boostrap
* [Revision #f1f8adf](https://github.com/MariaDB/server/commit/f1f8adf)\
  2015-04-20 05:02:10 +0200
  * tokuftdump: Install to ${INSTALL\_BINDIR} instead of bin
* [Revision #87d5438](https://github.com/MariaDB/server/commit/87d5438)\
  2015-04-20 02:43:26 +0300
  * Increase the version number
* [Revision #4cfb7f9](https://github.com/MariaDB/server/commit/4cfb7f9)\
  2015-04-19 15:49:35 +0300
  * Increase the version number
* [Revision #eae8318](https://github.com/MariaDB/server/commit/eae8318)\
  2015-04-17 20:05:41 +0200
  * Fix Catalog JSON table crash when no Jpath
  * Added JSON OBJECT specification for pretty != 2.
  * Fix NULL values not recognized for nullable JSON columns
  * Issue an error message when a JSON table is created without specifying LRECL if PRETTY != 2.
  * Make JSONColumns use a TDBJSON class.
  * Make JSON table using MAPFAM
* [Revision #1115a59](https://github.com/MariaDB/server/commit/1115a59)\
  2015-04-15 19:14:20 +0300
  * Merge pull request #41 from MariaDB/5.5-[MDEV-7820](https://jira.mariadb.org/browse/MDEV-7820)
* [Revision #eb47b22](https://github.com/MariaDB/server/commit/eb47b22)\
  2015-04-15 16:23:43 +0300
  * [MDEV-7820](https://jira.mariadb.org/browse/MDEV-7820) Server crashes in my\_strcasecmp\_utf8 on subquery in ORDER BY clause of GROUP\_CONCAT
* [Revision #59d847b](https://github.com/MariaDB/server/commit/59d847b)\
  2015-04-15 12:08:37 +0400
  * [MDEV-7814](https://jira.mariadb.org/browse/MDEV-7814) Assertion \`args\[0]->fixed' fails in Item\_func\_conv\_charset::Item\_func\_conv\_charset Removing a wrong assertion.
* [Revision #b9a7586](https://github.com/MariaDB/server/commit/b9a7586)\
  2015-03-05 16:34:13 +0100
  * [MDEV-7613](https://jira.mariadb.org/browse/MDEV-7613): [MariaDB 5.5.40](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5540-release-notes.md) server crash on update table left join with a view
* [Revision #a852355](https://github.com/MariaDB/server/commit/a852355)\
  2015-04-14 14:23:35 +0200
  * Merge [MDEV-7975](https://jira.mariadb.org/browse/MDEV-7975) into 10.0
* [Revision #5d2b85a](https://github.com/MariaDB/server/commit/5d2b85a)\
  2015-04-14 13:03:11 +0200
  * [MDEV-7975](https://jira.mariadb.org/browse/MDEV-7975): sporadic failure in test case rpl.rpl\_gtid\_startpos
* [Revision #83ce352](https://github.com/MariaDB/server/commit/83ce352)\
  2015-04-14 13:26:55 +1000
  * quote table name in mysql\_check:is\_view. increment version too
* [Revision #4987080](https://github.com/MariaDB/server/commit/4987080)\
  2015-04-14 13:26:22 +1000
  * Don't run upgrade-views if not mysql or --upgrade-system-tables
* [Revision #97e0aea](https://github.com/MariaDB/server/commit/97e0aea)\
  2015-04-14 12:43:50 +1000
  * mysqlcheck fix-view-algorithm -> upgrade-views
* [Revision #808608c](https://github.com/MariaDB/server/commit/808608c)\
  2015-04-14 11:26:13 +1000
  * corrected mysql\_upgrade to always list output for every phase
* [Revision #c584058](https://github.com/MariaDB/server/commit/c584058)\
  2015-04-14 11:01:31 +1000
  * Update tests for mysql\_upgrade\_view
* [Revision #76c18f7](https://github.com/MariaDB/server/commit/76c18f7)\
  2015-04-13 23:25:23 +1000
  * sql\_print\_information corrected
* [Revision #622891c](https://github.com/MariaDB/server/commit/622891c)\
  2015-04-13 22:58:45 +1000
  * mariadb\_fix\_view to allow fixing of view->mariadb\_version
* [Revision #8a827d5](https://github.com/MariaDB/server/commit/8a827d5)\
  2015-04-13 22:39:37 +1000
  * avoid calling runctiosn in DBUG\_RETURN
* [Revision #29721d7](https://github.com/MariaDB/server/commit/29721d7)\
  2015-04-13 22:31:44 +1000
  * mariadb\_fix\_view need only check view->mariadb\_version
* [Revision #7229b19](https://github.com/MariaDB/server/commit/7229b19)\
  2015-04-13 22:28:12 +1000
  * remove include sql\_view.h from sql\_table.cc - unneeded
* [Revision #17aff4b](https://github.com/MariaDB/server/commit/17aff4b)\
  2015-04-13 14:27:25 +0200
  * Merge [MDEV-7936](https://jira.mariadb.org/browse/MDEV-7936) into 10.0.
* [Revision #60d094a](https://github.com/MariaDB/server/commit/60d094a)\
  2015-04-13 09:52:56 +0200
  * [MDEV-7936](https://jira.mariadb.org/browse/MDEV-7936): Assertion \`!table || table->in\_use == \_current\_thd()' failed on parallel replication in optimistic mode
* [Revision #fc277cd](https://github.com/MariaDB/server/commit/fc277cd)\
  2015-04-13 22:17:57 +1000
  * Add --fix-tables option to mysql-check
* [Revision #c47fe0e](https://github.com/MariaDB/server/commit/c47fe0e)\
  2015-03-09 13:06:32 +0100
  * [MDEV-7668](https://jira.mariadb.org/browse/MDEV-7668): Intermediate master groups CREATE TEMPORARY with INSERT, causing parallel replication failure
* [Revision #28b1731](https://github.com/MariaDB/server/commit/28b1731)\
  2015-04-13 21:12:23 +1000
  * Allow REPAIR NO\_WRITE\_TO\_BINLOG as per serg's review
* [Revision #f91dafc](https://github.com/MariaDB/server/commit/f91dafc)\
  2015-04-13 20:52:19 +1000
  * correct phase numbering in test results
* [Revision #eaa3da8](https://github.com/MariaDB/server/commit/eaa3da8)\
  2015-04-13 20:41:49 +1000
  * Add mysql-test/std\_data/mysql\_upgrade/\* for [MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916)
* [Revision #4409e04](https://github.com/MariaDB/server/commit/4409e04)\
  2015-04-12 21:40:07 +1000
  * correct server side error messages
* [Revision #9b067a3](https://github.com/MariaDB/server/commit/9b067a3)\
  2015-04-12 21:05:01 +1000
  * Corrections to mysqlcheck
* [Revision #96e277a](https://github.com/MariaDB/server/commit/96e277a)\
  2015-04-12 20:42:13 +1000
  * mysql\_upgrade to pass binlog option to mysqlcheck
* [Revision #c8dbef2](https://github.com/MariaDB/server/commit/c8dbef2)\
  2015-04-12 20:41:28 +1000
  * [MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916) REPAIR VIEW / mysql migration
* [Revision #e5191dd](https://github.com/MariaDB/server/commit/e5191dd)\
  2015-04-12 17:26:50 +1000
  * mysql-upgrade -> fix-view-algorithm as mysqlcheck option
* [Revision #25872e2](https://github.com/MariaDB/server/commit/25872e2)\
  2015-04-12 17:21:02 +1000
  * Correct phase count on mysql\_upgrade
* [Revision #ebd3c6c](https://github.com/MariaDB/server/commit/ebd3c6c)\
  2015-04-12 17:05:02 +1000
  * Remove mysql-upgrade / skip-mysql-upgrade options from mysql-upgrade.c
* [Revision #87f5bae](https://github.com/MariaDB/server/commit/87f5bae)\
  2015-04-12 16:50:16 +1000
  * Get my\_getop to parse opt\_mysql\_upgrade in mysqlcheck
* [Revision #70960e7](https://github.com/MariaDB/server/commit/70960e7)\
  2015-04-12 15:56:21 +1000
  * [MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916): Upgrade from MySQL to MariaDB breaks already created views
* [Revision #85660d7](https://github.com/MariaDB/server/commit/85660d7)\
  2015-04-11 18:13:08 +1000
  * [MDEV-7977](https://jira.mariadb.org/browse/MDEV-7977) MYSQL\_BIN\_LOG::write\_incident failing to release LOCK\_log
* [Revision #50d98e9](https://github.com/MariaDB/server/commit/50d98e9)\
  2015-04-09 10:13:17 +0200
  * Merge [MDEV-7940](https://jira.mariadb.org/browse/MDEV-7940) into 10.0
* [Revision #15a2b5a](https://github.com/MariaDB/server/commit/15a2b5a)\
  2015-04-09 10:02:16 +0200
  * [MDEV-7940](https://jira.mariadb.org/browse/MDEV-7940): Sporadic failure in rpl.rpl\_gtid\_until
* [Revision #670d4dd](https://github.com/MariaDB/server/commit/670d4dd)\
  2015-04-08 15:10:22 +0200
  * Merge [MDEV-7910](https://jira.mariadb.org/browse/MDEV-7910)' into 10.0
* [Revision #b3c7c8c](https://github.com/MariaDB/server/commit/b3c7c8c)\
  2015-04-08 15:07:23 +0200
  * [MDEV-7910](https://jira.mariadb.org/browse/MDEV-7910): innodb.binlog\_consistent fails sporadically in buildbot
* [Revision #accdabd](https://github.com/MariaDB/server/commit/accdabd)\
  2015-04-08 13:19:22 +0200
  * Merge [MDEV-7888](https://jira.mariadb.org/browse/MDEV-7888) and [MDEV-7929](https://jira.mariadb.org/browse/MDEV-7929) into 10.0.
* [Revision #3b96134](https://github.com/MariaDB/server/commit/3b96134)\
  2015-04-08 11:01:18 +0200
  * [MDEV-7888](https://jira.mariadb.org/browse/MDEV-7888), [MDEV-7929](https://jira.mariadb.org/browse/MDEV-7929): Parallel replication hangs sometimes on ANALYZE TABLE or DDL
* [Revision #e9c10f9](https://github.com/MariaDB/server/commit/e9c10f9)\
  2015-04-06 17:38:51 +0300
  * [MDEV-7908](https://jira.mariadb.org/browse/MDEV-7908): assertion in innobase\_release\_savepoint
* [Revision #05b30fb](https://github.com/MariaDB/server/commit/05b30fb)\
  2015-04-04 19:29:34 +0200
  * Fix [MDEV-7890](https://jira.mariadb.org/browse/MDEV-7890)
* [Revision #836740c](https://github.com/MariaDB/server/commit/836740c)\
  2015-04-02 11:36:53 +0200
  * Correct a typo that made multiple 1 tables to return 0 lines on Linux
* [Revision #cc84ac3](https://github.com/MariaDB/server/commit/cc84ac3)\
  2015-03-31 13:10:43 +0500
  * [MDEV-7596](https://jira.mariadb.org/browse/MDEV-7596) audit plugin - record full query / document line length / make buffer configurable. The serve\_audit\_query\_log\_limit variable implemented. Also QUERY\_DCL filter added.
* [Revision #b53bcd4](https://github.com/MariaDB/server/commit/b53bcd4)\
  2015-03-30 18:53:10 +0300
  * [MDEV-7367](https://jira.mariadb.org/browse/MDEV-7367): Updating a virtual column corrupts table which crashes server
* [Revision #0563f49](https://github.com/MariaDB/server/commit/0563f49)\
  2015-03-17 16:03:05 +0200
  * [MDEV-7754](https://jira.mariadb.org/browse/MDEV-7754): innodb assert "array->n\_elems < array->max\_elems" on a huge blob update
* [Revision #8721d20](https://github.com/MariaDB/server/commit/8721d20)\
  2015-03-30 19:03:57 +0200
  * Fix [MDEV-7879](https://jira.mariadb.org/browse/MDEV-7879) by adding a test in all SetValue\_pval function to return when valp == this.
* [Revision #c41e4d3](https://github.com/MariaDB/server/commit/c41e4d3)\
  2015-03-30 14:51:25 +0200
  * Merge [MDEV-7847](https://jira.mariadb.org/browse/MDEV-7847) and [MDEV-7882](https://jira.mariadb.org/browse/MDEV-7882) into 10.0.
* [Revision #880f227](https://github.com/MariaDB/server/commit/880f227)\
  2015-03-30 14:33:44 +0200
  * [MDEV-7847](https://jira.mariadb.org/browse/MDEV-7847): "Slave worker thread retried transaction 10 time(s) in vain, giving up", followed by replication hanging
* [Revision #a408291](https://github.com/MariaDB/server/commit/a408291)\
  2015-03-30 14:16:57 +0200
  * [MDEV-7882](https://jira.mariadb.org/browse/MDEV-7882): Excessive transaction retry in parallel replication
* [Revision #995f622](https://github.com/MariaDB/server/commit/995f622)\
  2015-03-30 00:49:16 +0300
  * [MDEV-7858](https://jira.mariadb.org/browse/MDEV-7858): main.subselect\_sj2\_jcl6 fails in buildbot
* [Revision #daa8b6b](https://github.com/MariaDB/server/commit/daa8b6b)\
  2015-03-28 20:18:46 +0100
  * D:\Ber\Develop\git3.msg
* [Revision #323a7e9](https://github.com/MariaDB/server/commit/323a7e9)\
  2015-03-25 19:44:31 +0300
  * Backport from 10.1 to 10.0: Merge pull request #33 from k0da/[MDEV-7839](https://jira.mariadb.org/browse/MDEV-7839)
* [Revision #86f46a3d](https://github.com/MariaDB/server/commit/86f46a3d)\
  2015-03-23 09:49:32 +0200
  * [MDEV-7301](https://jira.mariadb.org/browse/MDEV-7301): Unknown column quoted with backticks in HAVING clause when using function.
* [Revision #9cace99](https://github.com/MariaDB/server/commit/9cace99)\
  2015-03-22 11:34:29 +0100
  * Fix a bug that caused a crash when doing delete on a json table with wrong syntax file
* [Revision #9253064](https://github.com/MariaDB/server/commit/9253064)\
  2015-03-10 12:34:17 +0200
  * [MDEV-7682](https://jira.mariadb.org/browse/MDEV-7682) Incorrect use of SPATIAL KEY for query plan
* [Revision #5e20df2](https://github.com/MariaDB/server/commit/5e20df2)\
  2015-03-19 19:46:08 +0400
  * [MDEV-7641](https://jira.mariadb.org/browse/MDEV-7641) Server crash on set global server\_audit\_incl\_users=null.
* [Revision #1020d56](https://github.com/MariaDB/server/commit/1020d56)\
  2015-03-18 15:17:17 +0200
  * Better and more correct comment.
* [Revision #2bb4280](https://github.com/MariaDB/server/commit/2bb4280)\
  2015-03-18 13:30:14 +0100
  * This commit includes changes done in a previous (deleted) branch plus new ones.
* [Revision #2bdbfd3](https://github.com/MariaDB/server/commit/2bdbfd3)\
  2015-03-18 12:18:39 +0200
  * Fix assertion failure seen on Buildbot win32-debug
* [Revision #c14d9c2](https://github.com/MariaDB/server/commit/c14d9c2)\
  2015-03-18 06:25:10 +0200
  * Make sure that sync level vector is emptied.
* [Revision #99a2c06](https://github.com/MariaDB/server/commit/99a2c06)\
  2015-03-17 20:35:05 +0200
  * [MDEV-7754](https://jira.mariadb.org/browse/MDEV-7754): innodb assert "array->n\_elems < array->max\_elems" on a huge blob update
* [Revision #c020d36](https://github.com/MariaDB/server/commit/c020d36)\
  2015-03-17 13:26:33 +0300
  * [MDEV-7474](https://jira.mariadb.org/browse/MDEV-7474): Semi-Join's DuplicateWeedout strategy skipped ...
* [Revision #3d48501](https://github.com/MariaDB/server/commit/3d48501)\
  2015-03-17 10:36:38 +0100
  * Fix embarrassing bug in test case that caused sporadic test failures.
* [Revision #57aacce](https://github.com/MariaDB/server/commit/57aacce)\
  2015-03-16 17:37:00 +0100
  * Adding files to ignore from C C++ and Visual Studio
  * Making result files to be ended by LF to avoid test failures
* [Revision #2e82a82](https://github.com/MariaDB/server/commit/2e82a82)\
  2015-03-16 10:54:47 +0100
  * [MDEV-7785](https://jira.mariadb.org/browse/MDEV-7785): errorneous -> erroneous spelling mistake
* [Revision #fd97739](https://github.com/MariaDB/server/commit/fd97739)\
  2015-03-15 14:50:22 +1100
  * Allow {un,}install plugins during bootstrap/skip-grant-tables
* [Revision #184f718](https://github.com/MariaDB/server/commit/184f718)\
  2015-03-13 10:46:00 +0100
  * [MDEV-7249](https://jira.mariadb.org/browse/MDEV-7249): Performance problem in parallel replication with multi-level slaves
* [Revision #bc902a2](https://github.com/MariaDB/server/commit/bc902a2)\
  2015-03-13 16:12:54 +0400
  * [MDEV-7387](https://jira.mariadb.org/browse/MDEV-7387) \[PATCH] Alter table xxx CHARACTER SET utf8, CONVERT TO CHARACTER SET latin1 should fail A contribution from Daniel Black, with minor additional enhancements.
* [Revision #5a3bf84](https://github.com/MariaDB/server/commit/5a3bf84)\
  2015-03-12 18:53:31 +0200
  * [MDEV-7692](https://jira.mariadb.org/browse/MDEV-7692) MariaDB - mysql-test - SUITE:percona - percona.innodb\_sys\_index 'xtradb' fails - @@version\_comment
* [Revision #702fdc5](https://github.com/MariaDB/server/commit/702fdc5)\
  2015-03-12 18:37:32 +0200
  * [MDEV-7714](https://jira.mariadb.org/browse/MDEV-7714): Make possible to get innodb internal primary key for wrapper type storage engine.
* [Revision #ed04c40](https://github.com/MariaDB/server/commit/ed04c40)\
  2015-03-11 09:18:16 +0100
  * [MDEV-5289](https://jira.mariadb.org/browse/MDEV-5289): master server starts slave parallel threads
* [Revision #a7fd11b](https://github.com/MariaDB/server/commit/a7fd11b)\
  2015-03-09 18:21:48 +0200
  * [MDEV-7685](https://jira.mariadb.org/browse/MDEV-7685): MariaDB - server crashes when inserting more rows than available space on disk
* [Revision #ec16d1b](https://github.com/MariaDB/server/commit/ec16d1b)\
  2015-03-09 02:07:47 +0200
  * [MDEV-7107](https://jira.mariadb.org/browse/MDEV-7107) Sporadic test failure in multi\_source.multisource
* [Revision #34f37aa](https://github.com/MariaDB/server/commit/34f37aa)\
  2015-03-02 19:18:10 +0200
  * [MDEV-7643](https://jira.mariadb.org/browse/MDEV-7643) MTR creates nested links when tests are run with --mem
* [Revision #96784eb](https://github.com/MariaDB/server/commit/96784eb)\
  2015-03-09 13:06:32 +0100
  * [MDEV-7668](https://jira.mariadb.org/browse/MDEV-7668): Intermediate master groups CREATE TEMPORARY with INSERT, causing parallel replication failure
* [Revision #040027c](https://github.com/MariaDB/server/commit/040027c)\
  2015-03-09 09:47:25 +0200
  * [MDEV-7627](https://jira.mariadb.org/browse/MDEV-7627) :Some symbols in table name can cause to Error Code: 1050 when created FK
* [Revision #6fc0a8a](https://github.com/MariaDB/server/commit/6fc0a8a)\
  2015-03-08 23:12:19 +0200
  * [MDEV-7187](https://jira.mariadb.org/browse/MDEV-7187) perfschema.aggregate fails sporadically in buildbot
* [Revision #d61573d](https://github.com/MariaDB/server/commit/d61573d)\
  2015-03-06 20:49:48 +0100
  * fix connect.json\_udf test for static builds
* [Revision #c0af821](https://github.com/MariaDB/server/commit/c0af821)\
  2015-03-06 13:32:46 +0100
  * [MDEV-7669](https://jira.mariadb.org/browse/MDEV-7669) tmp\_table\_count-7586 fails in ps and embedded
* [Revision #5f510a9](https://github.com/MariaDB/server/commit/5f510a9)\
  2015-03-06 18:41:32 +0100
  * Merge branch '5.5' into 10.0
* [Revision #17a3779](https://github.com/MariaDB/server/commit/17a3779)\
  2015-03-06 18:13:06 +0100
  * after innodb/xtradb merge: use the correct visibility for internal functions
* [Revision #d7d1907](https://github.com/MariaDB/server/commit/d7d1907)\
  2015-03-06 17:03:46 +0100
  * [MDEV-6838](https://jira.mariadb.org/browse/MDEV-6838) Using too big key for internal temp tables
* [Revision #12d87c3](https://github.com/MariaDB/server/commit/12d87c3)\
  2015-03-06 11:15:55 +0100
  * [MDEV-7659](https://jira.mariadb.org/browse/MDEV-7659) buildbot may leave stale mysqld
* [Revision #206b111](https://github.com/MariaDB/server/commit/206b111)\
  2015-03-06 11:19:23 +0200
  * [MDEV-7672](https://jira.mariadb.org/browse/MDEV-7672): Crash creating an InnoDB table with foreign keys
* [Revision #e13459a](https://github.com/MariaDB/server/commit/e13459a)\
  2015-03-05 15:30:11 +0400
  * [MDEV-7148](https://jira.mariadb.org/browse/MDEV-7148) - Recurring: InnoDB: Failing assertion: !lock->recursive
* [Revision #f66fbe8](https://github.com/MariaDB/server/commit/f66fbe8)\
  2015-03-05 12:05:59 +0200
  * [MDEV-7578](https://jira.mariadb.org/browse/MDEV-7578) :Slave is 10x slower to execute set of statements compared to master when using RBR
* [Revision #7dee7a0](https://github.com/MariaDB/server/commit/7dee7a0)\
  2015-03-05 09:40:12 +0100
  * GTID: Add missing test of reconnecting into out-of-order binlog.
* [Revision #3ef0b9b](https://github.com/MariaDB/server/commit/3ef0b9b)\
  2015-03-04 13:36:54 +0100
  * Merge [MDEV-6589](https://jira.mariadb.org/browse/MDEV-6589) and [MDEV-6403](https://jira.mariadb.org/browse/MDEV-6403) into 10.0.
* [Revision #78c74db](https://github.com/MariaDB/server/commit/78c74db)\
  2015-03-04 13:10:37 +0100
  * [MDEV-6403](https://jira.mariadb.org/browse/MDEV-6403): Temporary tables lost at STOP SLAVE in GTID mode if master has not rotated binlog since restart
* [Revision #ad0d203](https://github.com/MariaDB/server/commit/ad0d203)\
  2015-02-18 12:22:50 +0100
  * [MDEV-6589](https://jira.mariadb.org/browse/MDEV-6589): Incorrect relay log start position when restarting SQL thread after error in parallel replication
* [Revision #eb2f763](https://github.com/MariaDB/server/commit/eb2f763)\
  2015-03-03 12:39:42 +0100
  * Add #include in dict0mem.h and change iterator to const\_iterator in dic0mem.cc
* [Revision #e33b48a](https://github.com/MariaDB/server/commit/e33b48a)\
  2015-03-02 16:47:43 +0100
  * Merge remote-tracking branch 'origin/10.0' into 10.0
* [Revision #c06c465](https://github.com/MariaDB/server/commit/c06c465)\
  2015-03-02 16:45:44 +0100
  * 10.0-connect merge
* [Revision #b9a9b82](https://github.com/MariaDB/server/commit/b9a9b82)\
  2015-03-02 00:35:56 +0100
  * Make json\_udf test work on Windows
* [Revision #5f4909b](https://github.com/MariaDB/server/commit/5f4909b)\
  2015-03-01 23:55:09 +0100
  * Making json\_udf test working on linux
* [Revision #34c8959](https://github.com/MariaDB/server/commit/34c8959)\
  2015-03-01 19:29:56 +0100
  * Remove a signed/unsigned warning.
* [Revision #5c8862e](https://github.com/MariaDB/server/commit/5c8862e)\
  2015-03-01 19:20:40 +0100
  * Fix crash when Json\_Value was called without arguments. Correct memory calculation in Serialize. Correct some UDF's messages. Add and modify the json tests
* [Revision #d862d7c](https://github.com/MariaDB/server/commit/d862d7c)\
  2015-02-28 23:01:55 +0100
  * Implement random access to ODBC tables
* [Revision #45b6edb](https://github.com/MariaDB/server/commit/45b6edb)\
  2015-02-28 23:44:55 +0200
  * [MDEV-6838](https://jira.mariadb.org/browse/MDEV-6838): Using too big key for internal temp tables
* [Revision #a235504](https://github.com/MariaDB/server/commit/a235504)\
  2015-02-28 22:43:18 +1030
  * Ensure VERBOSE\_DEBUG is off by default
* [Revision #2b9aba3](https://github.com/MariaDB/server/commit/2b9aba3)\
  2015-02-28 22:43:04 +1030
  * Updated © message to 2015, and changelog
* [Revision #c65f323](https://github.com/MariaDB/server/commit/c65f323)\
  2014-11-05 20:11:32 +1030
  * Fixed more cases for [MDEV-6282](https://jira.mariadb.org/browse/MDEV-6282)
* [Revision #e32dafe](https://github.com/MariaDB/server/commit/e32dafe)\
  2014-10-30 22:47:48 +1030
  * Hopefully finally fixes [MDEV-6282](https://jira.mariadb.org/browse/MDEV-6282), [MDEV-5748](https://jira.mariadb.org/browse/MDEV-5748) and [MDEV-6345](https://jira.mariadb.org/browse/MDEV-6345)
* [Revision #f8e0f1a](https://github.com/MariaDB/server/commit/f8e0f1a)\
  2014-10-28 21:50:34 +1030
  * Minor code cleanup: validation of options to member function.
* [Revision #fbcabb2](https://github.com/MariaDB/server/commit/fbcabb2)\
  2014-10-28 21:45:47 +1030
  * Fixed minor spelling mistake.
* [Revision #6ff6bf8](https://github.com/MariaDB/server/commit/6ff6bf8)\
  2014-10-25 21:36:55 +1030
  * Added regression test for [MDEV-6345](https://jira.mariadb.org/browse/MDEV-6345)
* [Revision #a657abd](https://github.com/MariaDB/server/commit/a657abd)\
  2014-10-25 21:36:29 +1030
  * Added extra debug to support [MDEV-6282](https://jira.mariadb.org/browse/MDEV-6282)
* [Revision #e72abc5](https://github.com/MariaDB/server/commit/e72abc5)\
  2014-10-25 21:23:34 +1030
  * Minor fix: make sure alter table wont try to change our storage engine to something else.
* [Revision #79246eb](https://github.com/MariaDB/server/commit/79246eb)\
  2014-10-30 23:00:07 +1030
  * Partial code tidy: move plugin description to end with other items, and added status variable for debug.
* [Revision #13e30c0](https://github.com/MariaDB/server/commit/13e30c0)\
  2014-10-25 21:17:13 +1030
  * Removed dead code and support for dead (<10.0.5) versions of mariadb
* [Revision #abf1e25](https://github.com/MariaDB/server/commit/abf1e25)\
  2014-10-25 20:00:41 +1030
  * Partial whitespace cleanup.
* [Revision #8261413](https://github.com/MariaDB/server/commit/8261413)\
  2014-06-15 21:39:23 +0930
  * Added regression test for [MDEV-6282](https://jira.mariadb.org/browse/MDEV-6282)
* [Revision #1973c00](https://github.com/MariaDB/server/commit/1973c00)\
  2014-06-22 19:59:42 +0930
  * Update 2014 © message
* [Revision #fa87fc7](https://github.com/MariaDB/server/commit/fa87fc7)\
  2015-02-27 18:28:40 +0100
  * update tokudb version after merge
* [Revision #aa845d1](https://github.com/MariaDB/server/commit/aa845d1)\
  2015-02-27 14:32:33 +0100
  * [MDEV-6391](https://jira.mariadb.org/browse/MDEV-6391): GTID binlog state not recovered if mariadb-bin.state is removed
* [Revision #ec4ff9a](https://github.com/MariaDB/server/commit/ec4ff9a)\
  2015-02-26 23:06:18 +0200
  * [MDEV-7586](https://jira.mariadb.org/browse/MDEV-7586): Merged derived tables/VIEWs increment created\_tmp\_tables
* [Revision #aa107ef](https://github.com/MariaDB/server/commit/aa107ef)\
  2015-02-25 11:59:00 +0100
  * FIX assert failure when sorting JSON tables
* [Revision #e027f5e](https://github.com/MariaDB/server/commit/e027f5e)\
  2015-02-24 23:18:04 +0100
  * Fix [MDEV-7616](https://jira.mariadb.org/browse/MDEV-7616) by adding SQLCOM\_SET\_OPTION to the accepted command list.
* [Revision #b5d6aa5](https://github.com/MariaDB/server/commit/b5d6aa5)\
  2015-02-23 13:27:51 +0100
  * [MDEV-7310](https://jira.mariadb.org/browse/MDEV-7310): last\_commit\_pos\_offset set to wrong value after binlog rotate in group commit

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
