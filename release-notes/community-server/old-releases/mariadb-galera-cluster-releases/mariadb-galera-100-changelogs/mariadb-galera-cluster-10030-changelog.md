# MariaDB Galera Cluster 10.0.30 Changelog

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.30)[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10030-release-notes.md)[Changelog](mariadb-galera-cluster-10030-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 22 Mar 2017

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10030-release-notes.md).\
For changes made in MariaDB, see the [MariaDB 10.0.30 Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10030-changelog.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code
modified in that revision.

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
* [Revision #9cf499724f](https://github.com/MariaDB/server/commit/9cf499724f) 2017-03-20 18:11:56 +0530 - Merge branch '10.0' into bb-10.0-galera
* [Revision #4c35dce296](https://github.com/MariaDB/server/commit/4c35dce296)\
  2017-03-18 22:50:14 +0200
  * Clean up the test mentioned in [MDEV-12052](https://jira.mariadb.org/browse/MDEV-12052).
* [Revision #8971286a3c](https://github.com/MariaDB/server/commit/8971286a3c)\
  2017-03-16 14:03:17 +0100
  * compiler warning
* [Revision #2d0c579a86](https://github.com/MariaDB/server/commit/2d0c579a86)\
  2017-03-06 16:25:01 +0200
  * Wait for slave threads to start during startup
* [Revision #e7f55fde88](https://github.com/MariaDB/server/commit/e7f55fde88)\
  2017-03-06 16:02:50 +0200
  * Removed wrong assert
* [Revision #2c2bd8c155](https://github.com/MariaDB/server/commit/2c2bd8c155)\
  2017-03-15 11:46:54 +0100
  * [MDEV-12261](https://jira.mariadb.org/browse/MDEV-12261) build failure without P\_S
* [Revision #06f1f1aa6e](https://github.com/MariaDB/server/commit/06f1f1aa6e)\
  2017-03-14 00:24:06 +0200
  * Make ELOOP be considered a File Not Found error when it comes from handlerton
* [Revision #032678ad18](https://github.com/MariaDB/server/commit/032678ad18)\
  2017-03-10 18:33:38 +0200
  * [MDEV-12091](https://jira.mariadb.org/browse/MDEV-12091) Shutdown fails to wait for rollback of recovered transactions to finish
* [Revision #1d47bd61d5](https://github.com/MariaDB/server/commit/1d47bd61d5)\
  2017-03-09 16:52:57 +0200
  * Remove leftover merge conflict marker
* [Revision #1b2b209519](https://github.com/MariaDB/server/commit/1b2b209519)\
  2017-03-09 11:28:07 +0200
  * Use correct integer format with printf-like functions.
* [Revision #8805fe0d5c](https://github.com/MariaDB/server/commit/8805fe0d5c)\
  2017-03-09 11:27:24 +0200
  * Use %pure-parser instead of the deprecated %pure\_parser.
* [Revision #2158de8865](https://github.com/MariaDB/server/commit/2158de8865)\
  2017-03-09 11:26:36 +0200
  * Remove unused variables.
* [Revision #9fe92a9770](https://github.com/MariaDB/server/commit/9fe92a9770)\
  2017-03-08 11:13:34 -0500
  * bump the VERSION
* [Revision #e1e04c3d68](https://github.com/MariaDB/server/commit/e1e04c3d68)\
  2017-03-08 14:40:02 +0200
  * Correct a merge error.
* [Revision #fc0a6dd57f](https://github.com/MariaDB/server/commit/fc0a6dd57f) 2017-03-08 12:21:13 +0200 - Merge branch '5.5' into 10.0
* [Revision #f65c9f825d](https://github.com/MariaDB/server/commit/f65c9f825d)\
  2017-03-07 15:52:17 +0200
  * mysql\_client\_test\_nonblock fails when compiled with clang
* [Revision #74fe0e03d5](https://github.com/MariaDB/server/commit/74fe0e03d5)\
  2017-03-08 11:46:34 +0200
  * Remove unused declarations.
* [Revision #47396ddea9](https://github.com/MariaDB/server/commit/47396ddea9) 2017-03-08 11:40:43 +0200 - Merge 5.5 into 10.0
* [Revision #6860a4b556](https://github.com/MariaDB/server/commit/6860a4b556)\
  2017-03-08 10:31:06 +0200
  * [MDEV-12206](https://jira.mariadb.org/browse/MDEV-12206) Query\_cache::send\_result\_to\_client() may corrupt THD::query\_plan\_flags
* [Revision #9c47beb8bd](https://github.com/MariaDB/server/commit/9c47beb8bd)\
  2017-03-08 10:07:50 +0200
  * [MDEV-11027](https://jira.mariadb.org/browse/MDEV-11027) InnoDB log recovery is too noisy
* [Revision #1fd3cc8c1f](https://github.com/MariaDB/server/commit/1fd3cc8c1f)\
  2017-03-08 10:06:34 +0200
  * Fix a compiler warning.
* [Revision #17a1b194e2](https://github.com/MariaDB/server/commit/17a1b194e2)\
  2017-03-08 10:03:35 +0200
  * Fix some GCC 6.3.0 warnings in MyISAM and Maria.
* [Revision #30cac41c2f](https://github.com/MariaDB/server/commit/30cac41c2f)\
  2017-03-06 23:07:59 +0400
  * [MDEV-11084](https://jira.mariadb.org/browse/MDEV-11084) server\_audit does not work with mysql\_community 5.7.16.
* [Revision #43903745e5](https://github.com/MariaDB/server/commit/43903745e5)\
  2017-03-05 10:58:05 +0530
  * [MDEV-11078](https://jira.mariadb.org/browse/MDEV-11078): NULL NOT IN (non-empty subquery) should never return results
* [Revision #6b8173b6e9](https://github.com/MariaDB/server/commit/6b8173b6e9)\
  2017-03-03 11:47:31 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520): Retry posix\_fallocate() after EINTR.
* [Revision #75f6067e89](https://github.com/MariaDB/server/commit/75f6067e89)\
  2017-02-28 17:39:28 +0100
  * [MDEV-9635](https://jira.mariadb.org/browse/MDEV-9635): Server crashes in part\_of\_refkey or assertion \`!created && key\_to\_save < (int)s->keys' failed in TABLE::use\_index(int) or with join\_cache\_level>2
* [Revision #53c6195eed](https://github.com/MariaDB/server/commit/53c6195eed)\
  2017-03-20 10:17:13 +0200
  * Fixed test failure on galere\_wsrep\_log\_conflicts on XtraDB.
* [Revision #f66395f7c0](https://github.com/MariaDB/server/commit/f66395f7c0) 2017-03-17 02:05:20 +0530 - Merge tag 'mariadb-10.0.30' into bb-sachin-10.0-galera-merge
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

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
