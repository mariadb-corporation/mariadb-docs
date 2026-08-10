# MariaDB Galera Cluster 10.0.24 Changelog

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.24)[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10024-release-notes.md)[Changelog](mariadb-galera-cluster-10024-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 26 Feb 2016

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10024-release-notes.md).\
For changes made in MariaDB, see the [MariaDB 10.0.24 Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10024-changelog.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code
modified in that revision.

* [Revision #01897db](https://github.com/MariaDB/server/commit/01897db)\
  2016-02-24 17:40:12 -0500
  * Skip galera\_sync\_wait\_show.test on non-debug builds.
* [Revision #f67d6fc](https://github.com/MariaDB/server/commit/f67d6fc)\
  2015-12-04 15:09:08 +0530\
  \*
  * PXC#480: xtrabackup-v2 SST fails with multiple log\_bin directives in my.cnf
* [Revision #0cf66e4](https://github.com/MariaDB/server/commit/0cf66e4)\
  2015-10-22 14:56:29 +0530\
  \*
  * PXC#460: wsrep\_sst\_auth don't work in Percona-XtraDB-Cluster-56-5.6.25-25.12.1.el7
* [Revision #0fd9d5a](https://github.com/MariaDB/server/commit/0fd9d5a)\
  2016-02-23 21:24:00 -0500
  * Update WSREP\_PATCH\_REVNO.
* [Revision #1b0d811](https://github.com/MariaDB/server/commit/1b0d811)\
  2016-02-23 21:08:42 -0500
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #0d58323](https://github.com/MariaDB/server/commit/0d58323)\
  2016-02-23 20:53:29 -0500
  * Merge tag 'mariadb-10.0.24' into 10.0-galera
* [Revision #276d65b](https://github.com/MariaDB/server/commit/276d65b)\
  2016-02-23 20:33:21 -0500
  * Fix for test failures.
* [Revision #b9c42d7](https://github.com/MariaDB/server/commit/b9c42d7)\
  2016-01-11 11:57:22 +0200
  * Bump WSREP\_PATCH\_VERSION in cmake/wsrep.cmake to 13
* [Revision #15118d3](https://github.com/MariaDB/server/commit/15118d3)\
  2016-02-23 00:30:47 -0500
  * refs codership/mysql-wsrep#237: Add sync point for mtr test.
* [Revision #b633dbd](https://github.com/MariaDB/server/commit/b633dbd)\
  2015-12-23 09:44:32 +0200
  * refs codership/mysql-wsrep#237 - test for FLUSH TABLES hang in slave node
* [Revision #32df0b1](https://github.com/MariaDB/server/commit/32df0b1)\
  2015-12-02 23:20:10 +0200
  * refs codership/mysql-wsrep#233 - avoiding the race condition, by not grabbing thd->LOCK\_wsrep\_thd for accessing thd->wsrep\_exec\_mode. The caller is same thread and exec mode can only be changed by self.
* [Revision #90e5e2f](https://github.com/MariaDB/server/commit/90e5e2f)\
  2015-12-02 23:16:25 +0200
  * refs codership/mysql-wsrep#233 - added mtr test case for this issue - not a perfect one, depends on some sleeps instead of checking if sync points are met
* [Revision #2cdcde9](https://github.com/MariaDB/server/commit/2cdcde9)\
  2016-02-23 00:19:41 -0500
  * Merge sync point from previous commit to XtraDB.
* [Revision #18f160d](https://github.com/MariaDB/server/commit/18f160d)\
  2015-12-02 22:57:46 +0200
  * refs codership/mysql-wsrep#233 - added dbug sync points for further mtr test for this issue
* [Revision #bf9572b](https://github.com/MariaDB/server/commit/bf9572b)\
  2015-11-25 03:36:26 -0800
  * refs codership/mysql-wsrep#228 - a test for wsrep\_sync\_wait and SHOW
* [Revision #1e14db1](https://github.com/MariaDB/server/commit/1e14db1)\
  2015-11-16 11:57:38 +0100
  * refs codership/mysql-wsrep#228
* [Revision #5ebf6ce](https://github.com/MariaDB/server/commit/5ebf6ce)\
  2015-11-16 04:06:38 -0800
  * Bump WSREP\_PATCH\_VERSION in cmake/wsrep.cmake to 12
* [Revision #2b7a5d9](https://github.com/MariaDB/server/commit/2b7a5d9)\
  2015-11-16 03:00:27 -0800
  * Galera MTR Tests: adjust the galera.galera\_defaults test for the new MTR default value for repl.causal\_read\_timeout
* [Revision #8504330](https://github.com/MariaDB/server/commit/8504330)\
  2015-11-13 04:03:39 -0800
  * Galera MTR Tests: misc test stability fixes
* [Revision #c665934](https://github.com/MariaDB/server/commit/c665934)\
  2015-11-03 14:16:08 +0100
  * refs codership/mysql-wsrep#201
* [Revision #c05d85f](https://github.com/MariaDB/server/commit/c05d85f)\
  2016-02-22 22:35:48 -0500
  * Refs codership/mysql-wsrep#198 : Fix test case
* [Revision #e9d805b](https://github.com/MariaDB/server/commit/e9d805b)\
  2015-10-23 00:01:16 -0700
  * Refs codership/mysql-wsrep#198 . MTR test case
* [Revision #d45f0c1](https://github.com/MariaDB/server/commit/d45f0c1)\
  2016-02-22 22:30:14 -0500
  * refs codership/mysql-wsrep#198: Revert test changes from previous commit
* [Revision #ea0b183](https://github.com/MariaDB/server/commit/ea0b183)\
  2015-10-23 09:38:33 +0300
  * refs codership/mysql-wsrep#198 Removed code duplication, PXC specifics
* [Revision #235bebe](https://github.com/MariaDB/server/commit/235bebe)\
  2015-10-22 17:30:20 +0200
  * refs codership/mysql-wsrep#201
* [Revision #17ac959](https://github.com/MariaDB/server/commit/17ac959)\
  2016-02-22 22:07:59 -0500
  * Bug#1421360: Add Percona Server specific FLUSH statements.
* [Revision #5d4fb15](https://github.com/MariaDB/server/commit/5d4fb15)\
  2016-02-22 22:05:16 -0500
  * Fix for compilation failure.
* [Revision #7d89deb](https://github.com/MariaDB/server/commit/7d89deb)\
  2015-10-22 14:59:53 +0300
  * refs codership/mysql-wsrep#198 fixed merge issues
* [Revision #0ecc4fe](https://github.com/MariaDB/server/commit/0ecc4fe)\
  2015-07-07 14:20:22 +0530
  * Bug#1421360: Add Percona Server specific FLUSH statements.
* [Revision #1077eef](https://github.com/MariaDB/server/commit/1077eef)\
  2015-07-16 05:24:13 -0700
  * PXC-391: Avoid Total Order Isolation (TOI) for LOCAL sql admin commands.
* [Revision #5be449d](https://github.com/MariaDB/server/commit/5be449d)\
  2015-10-21 01:25:32 -0700
  * Galera MTR Tests: attempt to work around codership/QA#179 in galera\_as\_slave\_nonprim.test
* [Revision #d794f05](https://github.com/MariaDB/server/commit/d794f05)\
  2015-10-21 01:15:52 -0700
  * Galera MTR Tests: stability fix for galera\_gcs\_fragment.test (TCP port was output to the .result file)
* [Revision #ace86a2](https://github.com/MariaDB/server/commit/ace86a2)\
  2015-10-20 17:54:14 +0200
  * refs codership/mysql-wsrep#201
* [Revision #c1ea057](https://github.com/MariaDB/server/commit/c1ea057)\
  2016-02-22 16:51:45 -0500
  * refs codership/mysql-wsrep#184
* [Revision #251c53a](https://github.com/MariaDB/server/commit/251c53a)\
  2015-10-19 11:17:13 +0200
  * refs codership/mysql-wsrep#184
* [Revision #5ad30e8](https://github.com/MariaDB/server/commit/5ad30e8)\
  2015-10-16 15:57:22 +0300
  * MTR test for checking correctness of fragmentation over CCs
* [Revision #cf43620](https://github.com/MariaDB/server/commit/cf43620)\
  2015-10-16 11:51:11 +0200
  * refs codership/galera#308
* [Revision #8c89e84](https://github.com/MariaDB/server/commit/8c89e84)\
  2015-10-16 10:22:30 +0200
  * refs codership/galera#308
* [Revision #2c56142](https://github.com/MariaDB/server/commit/2c56142)\
  2016-02-22 16:36:05 -0500
  * refs codership/mysql-wsrep#184
* [Revision #1d21676](https://github.com/MariaDB/server/commit/1d21676)\
  2015-10-15 15:13:29 +0200
  * refs codership/mysql-wsrep#184
* [Revision #267d429](https://github.com/MariaDB/server/commit/267d429)\
  2015-10-05 11:01:04 +0200
  * refs codership/mysql-wsrep#31
* [Revision #c0dac42](https://github.com/MariaDB/server/commit/c0dac42)\
  2015-10-05 09:42:03 +0200
  * refs codership/mysql-wsrep#31
* [Revision #0ec457b](https://github.com/MariaDB/server/commit/0ec457b)\
  2015-10-02 10:16:55 +0200
  * refs codership/galera#308
* [Revision #00b058a](https://github.com/MariaDB/server/commit/00b058a)\
  2015-10-01 17:05:48 +0300
  * refs codership/mysql-wsrep#202 Added schema info into wsrep messages
* [Revision #7ce84cf](https://github.com/MariaDB/server/commit/7ce84cf)\
  2015-09-29 23:29:54 -0700
  * Galera MTR Tests: stability fixes
* [Revision #2f870f5](https://github.com/MariaDB/server/commit/2f870f5)\
  2015-09-15 13:20:55 +0300
  * Restore original value of wsrep\_on after waiting for sync point.
* [Revision #d01328d](https://github.com/MariaDB/server/commit/d01328d)\
  2015-09-13 18:57:20 +0300
  * Helpers to deal with galera dbug sync points.
* [Revision #17b5cb6](https://github.com/MariaDB/server/commit/17b5cb6)\
  2016-02-17 22:56:38 -0500
  * codership/mysql-wsrep#247: Fix test case
* [Revision #a6d93b2](https://github.com/MariaDB/server/commit/a6d93b2)\
  2016-02-16 23:42:42 -0800
  * Galera MTR Tests: MW-246 codership/mysql-wsrep#247 Stability fix for galera.mysql-wsrep#247.test
* [Revision #2438afb](https://github.com/MariaDB/server/commit/2438afb)\
  2016-02-16 03:12:58 -0800
  * Galera MTR tests: MW-246 codership/mysql-wsrep#247 Additional tests around RSU and wsrep\_desync
* [Revision #13627d4](https://github.com/MariaDB/server/commit/13627d4)\
  2016-02-16 11:55:03 +0200
  * refs MW-246 - created mtr test for testing explicit desyncing with RSU mode DDL
* [Revision #4bdf025](https://github.com/MariaDB/server/commit/4bdf025)\
  2016-02-15 23:33:55 +0200
  * refs MW-246 - skipping desync and resync before and after DDL execution in RSU mode, if wsrep\_desync is set upfront
* [Revision #3042d65](https://github.com/MariaDB/server/commit/3042d65)\
  2016-02-17 15:50:01 -0500
  * [MDEV-9577](https://jira.mariadb.org/browse/MDEV-9577): sys\_vars.ignore\_db\_dirs\_basic fails under Valgrind
* [Revision #0225962](https://github.com/MariaDB/server/commit/0225962)\
  2016-02-16 17:14:11 -0500
  * Update global\_suppressions for galera suite to include new warning.
* [Revision #d23bd26](https://github.com/MariaDB/server/commit/d23bd26)\
  2016-02-13 18:28:36 -0500
  * Merge tag 'mariadb-5.5.48' into 5.5-galera
* [Revision #b83de11](https://github.com/MariaDB/server/commit/b83de11)\
  2016-02-10 18:04:08 -0500
  * Update WSREP\_PATCH\_REVNO.
* [Revision #a6d0903](https://github.com/MariaDB/server/commit/a6d0903)\
  2016-01-11 12:03:35 +0200
  * Bump WSREP\_PATCH\_VERSION in cmake/wsrep.cmake to 14
* [Revision #403a8bf](https://github.com/MariaDB/server/commit/403a8bf)\
  2015-11-16 04:07:08 -0800
  * Bump WSREP\_PATCH\_VERSION in cmake/wsrep.cmake to 13
* [Revision #1ce821b](https://github.com/MariaDB/server/commit/1ce821b)\
  2015-11-12 10:33:04 +0200
  * Refs codership/mysql-wsrep#221 - disabling certain IB atomic builtins, which caused complete hangs
* [Revision #bd1d2b9](https://github.com/MariaDB/server/commit/bd1d2b9)\
  2015-11-06 10:50:21 +0100
  * refs codership/mysql-wsrep#201
* [Revision #8a93a7c](https://github.com/MariaDB/server/commit/8a93a7c)\
  2015-11-04 16:19:48 +0200
  * refs codership/mysql-wsrep#226 Limit binlog recovery to found wsrep position
* [Revision #652e4c1](https://github.com/MariaDB/server/commit/652e4c1)\
  2016-02-10 17:29:28 -0500
  * Fix for a build failure.
* [Revision #484bbd3](https://github.com/MariaDB/server/commit/484bbd3)\
  2015-11-04 09:36:01 +0100
  * refs codership/mysql-wsrep#201
* [Revision #0c7dffe](https://github.com/MariaDB/server/commit/0c7dffe)\
  2015-10-22 17:30:20 +0200
  * refs codership/mysql-wsrep#201
* [Revision #8a71fde](https://github.com/MariaDB/server/commit/8a71fde)\
  2015-10-20 17:54:14 +0200
  * refs codership/mysql-wsrep#201

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
