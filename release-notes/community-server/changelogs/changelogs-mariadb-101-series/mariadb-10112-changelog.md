# MariaDB 10.1.12 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.12)[Release Notes](../../old-releases/10.1/10.1.12.md)[Changelog](mariadb-10112-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 25 Feb 2016

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.12.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #b05158c](https://github.com/MariaDB/server/commit/b05158c)\
  2016-02-24 17:14:38 +0300
  * [MDEV-8988](https://jira.mariadb.org/browse/MDEV-8988): Apparently valid SQL query gives wrong result (nested WHERE)
* [Revision #d044507](https://github.com/MariaDB/server/commit/d044507)\
  2016-02-24 10:27:23 +0100
  * Merge branch 'bb-10.1-serg' into 10.1
* [Revision #5a4ec8e](https://github.com/MariaDB/server/commit/5a4ec8e)\
  2016-02-24 10:26:13 +0100
  * fix test results after the merge
* [Revision #ff2d92b](https://github.com/MariaDB/server/commit/ff2d92b)\
  2016-02-24 13:12:03 +0400
  * [MDEV-7231](https://jira.mariadb.org/browse/MDEV-7231) Field ROUTINE\_DEFINITION in INFORMATION\_SCHEMA.`ROUTINES` contains broken procedure body when used shielding quotes inside.
* [Revision #cceec78](https://github.com/MariaDB/server/commit/cceec78)\
  2016-02-24 01:21:40 -0500
  * Merge branch '10.0-galera' into bb-10.1-serg
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
* [Revision #88576b3](https://github.com/MariaDB/server/commit/88576b3)\
  2016-02-23 22:16:35 +0100
  * Merge tracking branch 'connect/10.1' into 10.1
* [Revision #a5679af](https://github.com/MariaDB/server/commit/a5679af)\
  2016-02-23 21:35:05 +0100
  * Merge branch '10.0' into 10.1
* [Revision #b9c42d7](https://github.com/MariaDB/server/commit/b9c42d7)\
  2016-01-11 11:57:22 +0200
  * Bump WSREP\_PATCH\_VERSION in cmake/wsrep.cmake to 13
* [Revision #28a36f6](https://github.com/MariaDB/server/commit/28a36f6)\
  2016-02-23 14:09:25 +0200
  * Update column bitmaps for delete during binlog row image minimal.
* [Revision #de1fa45](https://github.com/MariaDB/server/commit/de1fa45)\
  2016-02-22 17:50:55 +0200
  * \[[MDEV-8411](https://jira.mariadb.org/browse/MDEV-8411)] Assertion failed in !table->write\_set
* [Revision #0e20137](https://github.com/MariaDB/server/commit/0e20137)\
  2016-02-16 16:15:22 +0200
  * \[Code cleanup] Refactor duplicate code within myisam and maria sort.cc
* [Revision #20c4dfd](https://github.com/MariaDB/server/commit/20c4dfd)\
  2016-02-22 19:55:43 +0100
  * [MDEV-9576](https://jira.mariadb.org/browse/MDEV-9576) syntax error on view with nullif and count
* [Revision #216b5cc](https://github.com/MariaDB/server/commit/216b5cc)\
  2016-02-22 18:49:35 +0100
  * [MDEV-9606](https://jira.mariadb.org/browse/MDEV-9606) Server crashes in fix\_fields, main.null fails with ps-protocol #2
* [Revision #e6d51aa](https://github.com/MariaDB/server/commit/e6d51aa)\
  2016-02-22 12:52:29 +0100
  * [MDEV-9550](https://jira.mariadb.org/browse/MDEV-9550) COUNT(NULL) returns incorrect result with sequence storage engine
* [Revision #9214d04](https://github.com/MariaDB/server/commit/9214d04)\
  2016-02-20 22:26:48 +0100
  * disable SHOW I\_S\_table for built-in I\_S tables
* [Revision #57905d1](https://github.com/MariaDB/server/commit/57905d1)\
  2016-02-20 21:00:51 +0100
  * [MDEV-9535](https://jira.mariadb.org/browse/MDEV-9535) Trigger doing "SET NEW.auctionStart = NOW();" on a timestamp kills MariaDB server
* [Revision #0fcd0ee](https://github.com/MariaDB/server/commit/0fcd0ee)\
  2016-02-20 21:06:20 +0100
  * [MDEV-9500](https://jira.mariadb.org/browse/MDEV-9500) Bug after upgrade to 10.1.10 (and 10.1.11)
* [Revision #a38b705](https://github.com/MariaDB/server/commit/a38b705)\
  2016-02-20 19:30:14 +0100
  * [MDEV-9560](https://jira.mariadb.org/browse/MDEV-9560) [Mariadb 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) Crashes when replicating from 10.0
* [Revision #4cabc60](https://github.com/MariaDB/server/commit/4cabc60)\
  2016-02-19 14:17:35 +0100
  * correct temporal fields in max\_display\_length\_for\_field()
* [Revision #d4b1425](https://github.com/MariaDB/server/commit/d4b1425)\
  2016-02-19 12:06:37 +0100
  * cleanup
* [Revision #ab2a960](https://github.com/MariaDB/server/commit/ab2a960)\
  2016-02-18 12:56:27 +0100
  * [MDEV-9475](https://jira.mariadb.org/browse/MDEV-9475) I can't finish my\_install\_db using binary tar distribution
* [Revision #bb54df6](https://github.com/MariaDB/server/commit/bb54df6)\
  2016-02-23 10:32:06 +0100
  * update test results after [MDEV-9307](https://jira.mariadb.org/browse/MDEV-9307)
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
* [Revision #b128f26](https://github.com/MariaDB/server/commit/b128f26)\
  2016-02-22 18:11:59 +0100
  * Fix build : change MYSQL\_ADD\_PLUGIN to be MACRO again, rather than FUNCTION
* [Revision #c20979b](https://github.com/MariaDB/server/commit/c20979b)\
  2016-02-22 16:26:44 +0100
  * [MDEV-9601](https://jira.mariadb.org/browse/MDEV-9601) Build client plugins, also for the cmake client-only build (-DWITHOUT\_SERVER=1)
* [Revision #d9c640a](https://github.com/MariaDB/server/commit/d9c640a)\
  2015-12-12 10:37:25 +0100
  * SphinxSE: add support for json filtering
* [Revision #3a24f1c](https://github.com/MariaDB/server/commit/3a24f1c)\
  2016-02-22 12:48:03 +0100
  * [MDEV-9307](https://jira.mariadb.org/browse/MDEV-9307) - provide info about DATA/INDEX directory in INFORMATION\_SCHEMA.TA BLES (in CREATE\_OPTIONS column)
* [Revision #ff25158](https://github.com/MariaDB/server/commit/ff25158)\
  2016-02-18 19:11:13 +0100
  * [MDEV-9529](https://jira.mariadb.org/browse/MDEV-9529) - do not install sql script to BINDIR
* [Revision #bcd2a15](https://github.com/MariaDB/server/commit/bcd2a15)\
  2016-02-19 14:42:43 +0100
  * [MDEV-9833](https://jira.mariadb.org/browse/MDEV-9833) - fix mysql\_config --libs for weird cases, where mysqlclient link dependencies contain flags instead of libraries (like -pthread rather than -lpthread)
* [Revision #4b08b10](https://github.com/MariaDB/server/commit/4b08b10)\
  2016-02-18 17:20:48 +0100
  * [MDEV-9489](https://jira.mariadb.org/browse/MDEV-9489):Assertion \`0' failed in Protocol::end\_statement() on UNION ALL
* [Revision #69042ff](https://github.com/MariaDB/server/commit/69042ff)\
  2016-02-20 00:22:16 +0100\
  \*
  * Fix to [MDEV-9579](https://jira.mariadb.org/browse/MDEV-9579) be testing for void result.
* [Revision #5f2f3c4](https://github.com/MariaDB/server/commit/5f2f3c4)\
  2016-02-18 09:22:41 +0100
  * connect engine compiler warnings
* [Revision #fd8e846](https://github.com/MariaDB/server/commit/fd8e846)\
  2016-02-18 11:01:22 +0400
  * [MDEV-9564](https://jira.mariadb.org/browse/MDEV-9564) - added s390x to lib64 INSTALL\_LIBDIR handling
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
* [Revision #a4b2714](https://github.com/MariaDB/server/commit/a4b2714)\
  2016-02-17 21:42:57 +0100
  * Merge branch 'bb-10.0-serg' into 10.0
* [Revision #3eb8b11](https://github.com/MariaDB/server/commit/3eb8b11)\
  2016-02-17 21:42:48 +0100
  * fix InnoDB on Windows
* [Revision #db5b51f](https://github.com/MariaDB/server/commit/db5b51f)\
  2016-01-27 00:46:12 +0100
  * mysqlreport update to 4.0, see [MDEV-573](https://jira.mariadb.org/browse/MDEV-573) for more informations
* [Revision #f22f2a6](https://github.com/MariaDB/server/commit/f22f2a6)\
  2016-01-14 03:59:19 -0800
  * [MDEV-9484](https://jira.mariadb.org/browse/MDEV-9484) - Typo fixes
* [Revision #59b6b99](https://github.com/MariaDB/server/commit/59b6b99)\
  2015-02-28 23:15:17 +1030
  * Added regression test for MDEV\_5871
* [Revision #289fe37](https://github.com/MariaDB/server/commit/289fe37)\
  2016-02-15 18:05:05 +0100
  * [MDEV-9350](https://jira.mariadb.org/browse/MDEV-9350) Fix jemalloc detection for FreeBSD
* [Revision #74d86d1](https://github.com/MariaDB/server/commit/74d86d1)\
  2016-02-17 14:12:05 +0100
  * MYSQL\_ADD\_PLUGIN: fix DISABLED keyword to work
* [Revision #98be6ef](https://github.com/MariaDB/server/commit/98be6ef)\
  2016-02-17 13:50:03 +0100
  * mtr: read both suitedir/disabled.def and suitedir/t/disabled.def
* [Revision #dc92263](https://github.com/MariaDB/server/commit/dc92263)\
  2016-02-17 13:48:13 +0100
  * [MDEV-9308](https://jira.mariadb.org/browse/MDEV-9308) Fix build errors with recent gcc (isfinite)
* [Revision #36ca65b](https://github.com/MariaDB/server/commit/36ca65b)\
  2016-02-17 12:32:07 +0200
  * [MDEV-9559](https://jira.mariadb.org/browse/MDEV-9559): Server without encryption configs crashes if selecting from an implicitly encrypted table
* [Revision #09b5865](https://github.com/MariaDB/server/commit/09b5865)\
  2016-02-17 08:05:00 +0400
  * [MDEV-9511](https://jira.mariadb.org/browse/MDEV-9511) Valgrind warnings 'Invalid read' in Field\_newdate::cmp and Field\_newdate::val\_str
* [Revision #0225962](https://github.com/MariaDB/server/commit/0225962)\
  2016-02-16 17:14:11 -0500
  * Update global\_suppressions for galera suite to include new warning.
* [Revision #77b5484](https://github.com/MariaDB/server/commit/77b5484)\
  2016-02-16 19:35:58 +0100
  * Merge branch 'connect/10.0' into 10.0
* [Revision #b6bcd0f](https://github.com/MariaDB/server/commit/b6bcd0f)\
  2016-02-16 19:15:55 +0100
  * Merge branch 'merge-perfschema-5.6' into 10.0
* [Revision #7e22a1d](https://github.com/MariaDB/server/commit/7e22a1d)\
  2016-02-16 18:56:39 +0100
  * 5.6.29
* [Revision #17a792a](https://github.com/MariaDB/server/commit/17a792a)\
  2016-02-16 18:55:00 +0100
  * Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #c8fcaf8](https://github.com/MariaDB/server/commit/c8fcaf8)\
  2016-02-16 18:32:59 +0100
  * Merge branch 'merge-innodb-5.6' into 10.0
* [Revision #e8085d1](https://github.com/MariaDB/server/commit/e8085d1)\
  2016-02-16 12:49:59 +0400
  * [MDEV-9346](https://jira.mariadb.org/browse/MDEV-9346) - The federatedx and spider engine make mysqld crash when they are configured withtout username
* [Revision #9b73e88](https://github.com/MariaDB/server/commit/9b73e88)\
  2015-12-30 22:26:25 +0800
  * fix-[MDEV-9346](https://jira.mariadb.org/browse/MDEV-9346)
* [Revision #1ac64b7](https://github.com/MariaDB/server/commit/1ac64b7)\
  2016-02-16 12:55:45 +0000
  * [MDEV-9557](https://jira.mariadb.org/browse/MDEV-9557) - fix compilation errors due to missing krb5\_free\_unparsed\_name() in old versions of Heimdal Kerberos
* [Revision #d520d35](https://github.com/MariaDB/server/commit/d520d35)\
  2016-02-16 12:53:24 +0100
  * Revert "[MDEV-8696](https://jira.mariadb.org/browse/MDEV-8696): Adding indexes on empty table is slow with large innodb\_sort\_buffer\_size."
* [Revision #31d2c02](https://github.com/MariaDB/server/commit/31d2c02)\
  2016-02-16 12:13:19 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #220e70f](https://github.com/MariaDB/server/commit/220e70f)\
  2016-02-16 12:07:18 +0100
  * 5.6.29
* [Revision #d76eba6](https://github.com/MariaDB/server/commit/d76eba6)\
  2016-02-16 12:06:16 +0100
  * 5.6.28-76.1
* [Revision #ab9b665](https://github.com/MariaDB/server/commit/ab9b665)\
  2016-02-16 10:49:13 +0200
  * [MDEV-9355](https://jira.mariadb.org/browse/MDEV-9355): parts.partition\_debug\_innodb fails in buildbot on p8-rhel6-bintar-debug
* [Revision #481e643](https://github.com/MariaDB/server/commit/481e643)\
  2016-02-15 23:41:59 +0100\
  \*
  * Fix to [MDEV-9542](https://jira.mariadb.org/browse/MDEV-9542) Connect was not handling NULLs in the answer from catalog functions and tables. It does now and when decimal is NULL defines DOUBLE without parameters.
* [Revision #271fed4](https://github.com/MariaDB/server/commit/271fed4)\
  2016-02-15 22:50:59 +0100
  * Merge branch '5.5' into 10.0
* [Revision #ff26d93](https://github.com/MariaDB/server/commit/ff26d93)\
  2016-02-15 18:23:52 +0100
  * bump the version
* [Revision #a70b896](https://github.com/MariaDB/server/commit/a70b896)\
  2016-02-15 18:38:15 +0200
  * [MDEV-9424](https://jira.mariadb.org/browse/MDEV-9424): Server crashes when slave works with partitioned tables copied from Windows to Linux
* [Revision #c0b6c27](https://github.com/MariaDB/server/commit/c0b6c27)\
  2016-02-15 14:43:42 +0200
  * [MDEV-9548](https://jira.mariadb.org/browse/MDEV-9548): Alter table (renaming and adding index) fails with "Incorrect key file for table" [MDEV-9469](https://jira.mariadb.org/browse/MDEV-9469): 'Incorrect key file' on ALTER TABLE
* [Revision #e1385f2](https://github.com/MariaDB/server/commit/e1385f2)\
  2016-02-15 12:59:47 +0100
  * fix buffer overrun
* [Revision #daa4a2c](https://github.com/MariaDB/server/commit/daa4a2c)\
  2016-02-12 18:12:16 +0100
  * [MDEV-9351](https://jira.mariadb.org/browse/MDEV-9351) Fix CPU detection for TokuDB on FreeBSD
* [Revision #5a0f2f5](https://github.com/MariaDB/server/commit/5a0f2f5)\
  2016-02-12 17:46:34 +0100
  * [MDEV-9149](https://jira.mariadb.org/browse/MDEV-9149) Ctrl-C in MySQL client does not interrupt query, but interrupts the session instead
* [Revision #9630eda](https://github.com/MariaDB/server/commit/9630eda)\
  2016-02-11 20:42:16 +0100
  * [MDEV-9390](https://jira.mariadb.org/browse/MDEV-9390) Function found\_rows() gives incorrect result where the previous SELECT contains ORDER BY clause
* [Revision #38b89a6](https://github.com/MariaDB/server/commit/38b89a6)\
  2016-02-11 12:25:23 +0100
  * [MDEV-9103](https://jira.mariadb.org/browse/MDEV-9103) Altering table comment does a full copy
* [Revision #3c6b771](https://github.com/MariaDB/server/commit/3c6b771)\
  2016-02-10 21:15:24 +0100
  * [MDEV-9045](https://jira.mariadb.org/browse/MDEV-9045) Inconsistent handling of "ALGORITHM=INPLACE" with PERSISTENT generated columns
* [Revision #48ea84f](https://github.com/MariaDB/server/commit/48ea84f)\
  2016-02-10 17:00:31 +0100
  * [MDEV-8427](https://jira.mariadb.org/browse/MDEV-8427) main.connect fails on ppc64el in 10.0 as of 1a8cf15d
* [Revision #9b9522a](https://github.com/MariaDB/server/commit/9b9522a)\
  2016-02-10 15:38:25 +0100
  * [MDEV-8133](https://jira.mariadb.org/browse/MDEV-8133) ALTER TABLE can perform the operation but escape the binary log
* [Revision #1fc6e29](https://github.com/MariaDB/server/commit/1fc6e29)\
  2016-01-13 21:06:29 +0100
  * XtraDB/InnoDB crash with autoinc, vcol and online alter
* [Revision #3889b19](https://github.com/MariaDB/server/commit/3889b19)\
  2016-02-14 22:19:27 +0100
  * more strict ipv6\_ok check in mtr
* [Revision #8f5030e](https://github.com/MariaDB/server/commit/8f5030e)\
  2016-02-14 22:17:38 +0100
  * fix my\_gethwaddr() for solaris
* [Revision #95740bc](https://github.com/MariaDB/server/commit/95740bc)\
  2016-02-14 22:16:50 +0100
  * dtrace in cmake
* [Revision #a5d9597](https://github.com/MariaDB/server/commit/a5d9597)\
  2016-02-14 22:15:16 +0100
  * better inline check
* [Revision #5f078cc](https://github.com/MariaDB/server/commit/5f078cc)\
  2016-02-14 20:57:48 +0100
  * compilation errors on sparc sun studio 10
* [Revision #d163ad3](https://github.com/MariaDB/server/commit/d163ad3)\
  2016-02-15 10:32:30 +0100\
  \*
  * Fix to [MDEV-9542](https://jira.mariadb.org/browse/MDEV-9542) Connect was not handling NULLs in the answer from catalog functions and tables. It does now and when decimal is NULL defines DOUBLE without parameters.
* [Revision #2a47817](https://github.com/MariaDB/server/commit/2a47817)\
  2016-02-14 18:33:20 +0200
  * [MDEV-9225](https://jira.mariadb.org/browse/MDEV-9225) mysql\_upgrade segfault due to missing /etc/my.cnf.d
* [Revision #b7dc830](https://github.com/MariaDB/server/commit/b7dc830)\
  2016-02-14 18:31:06 +0200
  * Fix memory leak when failing to read config file
* [Revision #d23bd26](https://github.com/MariaDB/server/commit/d23bd26)\
  2016-02-13 18:28:36 -0500
  * Merge tag 'mariadb-5.5.48' into 5.5-galera
* [Revision #93e9d81](https://github.com/MariaDB/server/commit/93e9d81)\
  2016-02-12 12:04:11 +0400
  * Errorneous PSI declaration line fixed.
* [Revision #2c79f57](https://github.com/MariaDB/server/commit/2c79f57)\
  2016-02-12 03:47:25 +0200
  * [MDEV-9464](https://jira.mariadb.org/browse/MDEV-9464) perfschema.global\_read\_lock fails when executed after perfschema.dml\_setup\_instruments
* [Revision #5094a4a](https://github.com/MariaDB/server/commit/5094a4a)\
  2016-02-11 13:54:06 +0400
  * Adjusted main.contributors test result.
* [Revision #fbf132b](https://github.com/MariaDB/server/commit/fbf132b)\
  2016-02-11 11:24:45 +0400
  * Merge pull request #155 from iangilfillan/10.0
* [Revision #d859fff](https://github.com/MariaDB/server/commit/d859fff)\
  2016-02-11 11:15:14 +0400
  * Merge pull request #145 from ottok/ok-debpkg-10.0
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
* [Revision #a9a08b1](https://github.com/MariaDB/server/commit/a9a08b1)\
  2016-02-10 10:03:47 +0400
  * [MDEV-9371](https://jira.mariadb.org/browse/MDEV-9371) select insert('a',2,1,'b') doesn't return expected 'a'
* [Revision #0c7dffe](https://github.com/MariaDB/server/commit/0c7dffe)\
  2015-10-22 17:30:20 +0200
  * refs codership/mysql-wsrep#201
* [Revision #8a71fde](https://github.com/MariaDB/server/commit/8a71fde)\
  2015-10-20 17:54:14 +0200
  * refs codership/mysql-wsrep#201
* [Revision #3c5c04b](https://github.com/MariaDB/server/commit/3c5c04b)\
  2016-02-10 03:49:11 +0200
  * [MDEV-7122](https://jira.mariadb.org/browse/MDEV-7122): Assertion \`0' failed in subselect\_hash\_sj\_engine::init
* [Revision #6b614c6](https://github.com/MariaDB/server/commit/6b614c6)\
  2016-02-09 13:50:48 +0100
  * [MDEV-7765](https://jira.mariadb.org/browse/MDEV-7765): Crash (Assertion \`!table || (!table->write\_set || bitmap\_is\_set(table->write\_set, field\_index) || bitmap\_is\_set(table->vcol\_set, field\_index))' fails) on using function over not created table
* [Revision #775cccc](https://github.com/MariaDB/server/commit/775cccc)\
  2016-02-08 22:53:40 +0200
  * [MDEV-7122](https://jira.mariadb.org/browse/MDEV-7122): Assertion \`0' failed in subselect\_hash\_sj\_engine::init
* [Revision #01628ce](https://github.com/MariaDB/server/commit/01628ce)\
  2016-02-09 14:08:36 +0100
  * Merge branch 'bb-5.5-serg' into 5.5
* [Revision #afce541](https://github.com/MariaDB/server/commit/afce541)\
  2016-02-09 14:06:45 +0100
  * Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #5d478f5](https://github.com/MariaDB/server/commit/5d478f5)\
  2016-02-08 20:07:38 +0100
  * Bug#19817021
* [Revision #6703e5b](https://github.com/MariaDB/server/commit/6703e5b)\
  2016-02-08 20:07:09 +0100
  * Bug#20691429 ASSERTION \`CHILD\_L' FAILED IN STORAGE/MYISAMMRG/HA\_MYISAMMRG.CC:631
* [Revision #dece4bc](https://github.com/MariaDB/server/commit/dece4bc)\
  2016-02-09 11:28:44 +0100
  * cleanup: make assert more readable
* [Revision #63d3ccd](https://github.com/MariaDB/server/commit/63d3ccd)\
  2016-02-08 20:04:39 +0100
  * Bug#21205695 DROP TABLE MAY CAUSE SLAVES TO BREAK
* [Revision #f3444df](https://github.com/MariaDB/server/commit/f3444df)\
  2016-02-09 11:27:40 +0100
  * Merge branch 'mysql/5.5' into 5.5
* [Revision #ea0c3fc](https://github.com/MariaDB/server/commit/ea0c3fc)\
  2016-02-09 05:17:41 +0400
  * [MDEV-9438](https://jira.mariadb.org/browse/MDEV-9438) backport feedback-http-proxy to 5.5 and 10.0. The http-proxy option to the FEEDBACK plugin backported.
* [Revision #b17a435](https://github.com/MariaDB/server/commit/b17a435)\
  2016-02-09 02:31:47 +0300
  * [MDEV-6859](https://jira.mariadb.org/browse/MDEV-6859): scalar subqueries in a comparison produced unexpected result
* [Revision #3cfd36b](https://github.com/MariaDB/server/commit/3cfd36b)\
  2016-02-09 00:13:25 +0100
  * 5.5.47-37.7
* [Revision #d443d70](https://github.com/MariaDB/server/commit/d443d70)\
  2016-02-09 01:46:53 +0300
  * [MDEV-7823](https://jira.mariadb.org/browse/MDEV-7823): Server crashes in next\_depth\_first\_tab on nested IN clauses with SQ inside
* [Revision #eb752ac](https://github.com/MariaDB/server/commit/eb752ac)\
  2016-02-08 16:31:27 +0200
  * typo "Bangalore1" -> "Bangalore"
* [Revision #d80b844](https://github.com/MariaDB/server/commit/d80b844)\
  2016-02-07 15:00:30 +0200
  * Fixes needed to compile with musl C library Patch originally by Codarren Velvindron
* [Revision #c4cb240](https://github.com/MariaDB/server/commit/c4cb240)\
  2016-02-06 22:41:58 +0100
  * [MDEV-9024](https://jira.mariadb.org/browse/MDEV-9024) Build fails with VS2015
* [Revision #1e361f2](https://github.com/MariaDB/server/commit/1e361f2)\
  2016-02-06 13:57:59 +0100
  * [MDEV-4664](https://jira.mariadb.org/browse/MDEV-4664) mysql\_upgrade crashes if root's password contains an apostrophe/single quotation mark
* [Revision #9e4e412](https://github.com/MariaDB/server/commit/9e4e412)\
  2016-02-06 13:56:37 +0100
  * unit test for dynstr\_append\_os\_quoted()
* [Revision #41021c0](https://github.com/MariaDB/server/commit/41021c0)\
  2016-02-03 17:15:22 +0100
  * [MDEV-9462](https://jira.mariadb.org/browse/MDEV-9462): Out of memory using explain on 2 empty tables
* [Revision #be19bba](https://github.com/MariaDB/server/commit/be19bba)\
  2016-02-06 12:58:06 +0200
  * Merge pull request #150 from grooverdan/10.0-my\_rnd\_cpp
* [Revision #ad94790](https://github.com/MariaDB/server/commit/ad94790)\
  2016-02-04 14:47:46 +0100
  * [MDEV-9453](https://jira.mariadb.org/browse/MDEV-9453) mysql\_upgrade.exe error when mysql is migrated to mariadb
* [Revision #0a76ad5](https://github.com/MariaDB/server/commit/0a76ad5)\
  2016-02-04 12:51:57 +0100
  * [MDEV-9175](https://jira.mariadb.org/browse/MDEV-9175) Query parser tansforms MICROSECOND into SECOND\_FRAC, which does not work
* [Revision #a90da6e](https://github.com/MariaDB/server/commit/a90da6e)\
  2016-02-05 14:04:24 +0100
  * [MDEV-9314](https://jira.mariadb.org/browse/MDEV-9314) fatal build error: viosslfactories.c:58:5: error: dereferencing pointer to incomplete type ‘DH {aka struct dh\_st}
* [Revision #db5f743](https://github.com/MariaDB/server/commit/db5f743)\
  2016-02-06 12:37:46 +0200
  * Merge pull request #148 from grooverdan/5.5-rpl\_reporting-cppcheck-va\_end
* [Revision #6ecf6d8](https://github.com/MariaDB/server/commit/6ecf6d8)\
  2016-02-05 17:46:01 +0100
  * [MDEV-7827](https://jira.mariadb.org/browse/MDEV-7827): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed in Field\_long::val\_str on EXPLAIN EXTENDED
* [Revision #9f3b53f](https://github.com/MariaDB/server/commit/9f3b53f)\
  2015-12-14 19:16:29 +0100
  * [MDEV-9093](https://jira.mariadb.org/browse/MDEV-9093) Persistent computed column is not updated when update query contains join
* [Revision #113b56e](https://github.com/MariaDB/server/commit/113b56e)\
  2016-02-04 16:03:14 +0200
  * Merge remote-tracking branch 'upstream/10.0' into 10.0
* [Revision #86b2621](https://github.com/MariaDB/server/commit/86b2621)\
  2016-02-04 16:00:11 +0200
  * [MDEV-6821](https://jira.mariadb.org/browse/MDEV-6821), [MDEV-6826](https://jira.mariadb.org/browse/MDEV-6826) - Update authors and contributors
* [Revision #33ac501](https://github.com/MariaDB/server/commit/33ac501)\
  2016-02-04 13:54:57 +0200
  * Use C++ linkage.
* [Revision #1d00d5c](https://github.com/MariaDB/server/commit/1d00d5c)\
  2016-02-03 16:51:23 +0200
  * Fix function visibility as it is used on row0mysql.c in Windows.
* [Revision #a3d843d](https://github.com/MariaDB/server/commit/a3d843d)\
  2016-02-03 15:52:26 +0200
  * Fix function visibility as it is used on row0mysql.c in Windows.
* [Revision #73d23f8](https://github.com/MariaDB/server/commit/73d23f8)\
  2016-02-03 14:34:06 +0200
  * [MDEV-9471](https://jira.mariadb.org/browse/MDEV-9471): Server crashes or returns an error while trying to alter partitioning on a table moved from Windows to Linux
* [Revision #f66d016](https://github.com/MariaDB/server/commit/f66d016)\
  2016-02-03 11:32:51 +0200
  * [MDEV-9471](https://jira.mariadb.org/browse/MDEV-9471): Server crashes or returns an error while trying to alter partitioning on a table moved from Windows to Linux
* [Revision #603c096](https://github.com/MariaDB/server/commit/603c096)\
  2016-02-03 00:43:00 +0100
  * [MDEV-9466](https://jira.mariadb.org/browse/MDEV-9466) : Exception handler on Windows does not output any text, if mysqld runs as service
* [Revision #07b8aef](https://github.com/MariaDB/server/commit/07b8aef)\
  2016-02-03 00:15:49 +0300
  * [MDEV-9504](https://jira.mariadb.org/browse/MDEV-9504): ANALYZE TABLE shows wrong 'rows' value for ORDER BY query
* [Revision #55ea265](https://github.com/MariaDB/server/commit/55ea265)\
  2016-02-02 19:54:18 +0200
  * Fixed warnings and one memory loss found by valgrind
* [Revision #11c2d3c](https://github.com/MariaDB/server/commit/11c2d3c)\
  2016-02-02 13:07:53 +0200
  * Merge branch '10.0' into 10.1
* [Revision #52d695f](https://github.com/MariaDB/server/commit/52d695f)\
  2016-02-01 17:51:57 +0100
  * Fix authentication plugin's tests in case username contains non-alphanumeric character, e.g dash
* [Revision #5cf293f](https://github.com/MariaDB/server/commit/5cf293f)\
  2016-02-01 19:37:06 +0300
  * Merge branch '10.0' of github.com:MariaDB/server into 10.0
* [Revision #74f15e2](https://github.com/MariaDB/server/commit/74f15e2)\
  2016-02-01 19:36:22 +0300
  * [MDEV-9505](https://jira.mariadb.org/browse/MDEV-9505): Valgrind failure in SEL\_ARG::store\_min,find\_used\_partitions
* [Revision #e6dee57](https://github.com/MariaDB/server/commit/e6dee57)\
  2016-02-01 19:06:54 +0300
  * [MDEV-9504](https://jira.mariadb.org/browse/MDEV-9504): ANALYZE TABLE shows wrong 'rows' value for ORDER BY query
* [Revision #91ff017](https://github.com/MariaDB/server/commit/91ff017)\
  2016-02-01 16:40:20 +0100
  * Merge [MDEV-9112](https://jira.mariadb.org/browse/MDEV-9112) into 10.1
* [Revision #955126e](https://github.com/MariaDB/server/commit/955126e)\
  2016-02-01 16:29:00 +0100
  * Merge [MDEV-9112](https://jira.mariadb.org/browse/MDEV-9112) into 10.0
* [Revision #0e84d54](https://github.com/MariaDB/server/commit/0e84d54)\
  2016-02-01 16:27:12 +0100
  * Merge [MDEV-9112](https://jira.mariadb.org/browse/MDEV-9112) into 5.5
* [Revision #8cf1f50](https://github.com/MariaDB/server/commit/8cf1f50)\
  2016-02-01 16:10:49 +0100
  * [MDEV-9112](https://jira.mariadb.org/browse/MDEV-9112): Non-blocking client API missing on non-x86 platforms
* [Revision #a96fbc3](https://github.com/MariaDB/server/commit/a96fbc3)\
  2016-02-01 12:43:19 +0400
  * [MDEV-9503](https://jira.mariadb.org/browse/MDEV-9503) Server crashes in fix\_fields, main.null fails with ps-protocol DBUG\_ASSERT() added in the patch for [MDEV-9181](https://jira.mariadb.org/browse/MDEV-9181) did not take into account special circumstances for the prepared statement EXECUTE. Fixig the assert. Also, extending and fixing comments made during [MDEV-9181](https://jira.mariadb.org/browse/MDEV-9181).
* [Revision #dc50a3d](https://github.com/MariaDB/server/commit/dc50a3d)\
  2016-02-01 01:02:23 +0200
  * Raise the version number
* [Revision #0bee150](https://github.com/MariaDB/server/commit/0bee150)\
  2016-02-01 01:01:29 +0200
  * [MDEV-9502](https://jira.mariadb.org/browse/MDEV-9502) maria.encrypt-wrong-key fails with embedded server
* [Revision #3d794d0](https://github.com/MariaDB/server/commit/3d794d0)\
  2016-01-06 09:15:19 +0100
  * MDEV9494 Fix build for Heimdal Kerberos
* [Revision #d0c5efc](https://github.com/MariaDB/server/commit/d0c5efc)\
  2016-01-29 23:53:44 +0200
  * If one compiled with too long MYSQL\_SERVER\_SUFFIX this caused a memory overrun that caused some test to fail.
* [Revision #a1ddf01](https://github.com/MariaDB/server/commit/a1ddf01)\
  2016-01-29 23:52:15 +0200
  * my\_decimal didn't compile properly with debug
* [Revision #a4ff37e](https://github.com/MariaDB/server/commit/a4ff37e)\
  2016-01-26 22:33:25 +0400
  * [MDEV-6421](https://jira.mariadb.org/browse/MDEV-6421) SQL\_ERROR\_LOG doesn't log comments in Events. Change parser so it saves all the query line to the ';' in the sp\_instr::m\_query.
* [Revision #0bfb5be](https://github.com/MariaDB/server/commit/0bfb5be)\
  2016-01-25 20:01:22 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #62a5e56](https://github.com/MariaDB/server/commit/62a5e56)\
  2016-01-25 18:44:51 +0100\
  \*
  * Change SQL\_NTS to 0 when the string is NULL
* [Revision #1fa15f9](https://github.com/MariaDB/server/commit/1fa15f9)\
  2016-01-25 17:54:28 +0200
  * Updated README and CREDITS
* [Revision #8fb34ea](https://github.com/MariaDB/server/commit/8fb34ea)\
  2016-01-25 14:10:09 +0100\
  \*
  * Fix to [MDEV-9446](https://jira.mariadb.org/browse/MDEV-9446) (using Json UDFs when CONNECT is not installed)
* [Revision #a7a4988](https://github.com/MariaDB/server/commit/a7a4988)\
  2016-01-19 16:53:13 +1100
  * mysys/my\_rnd.c - remove `#ifdef cplusplus`
* [Revision #3e5724f](https://github.com/MariaDB/server/commit/3e5724f)\
  2016-01-19 14:47:41 +1100
  * Add va\_end to make cppcheck happy
* [Revision #ddd62ba](https://github.com/MariaDB/server/commit/ddd62ba)\
  2016-01-18 23:00:40 +0100\
  \*
  * Change SQL\_NTS to 0 when the string is NULL
* [Revision #2a9f84b](https://github.com/MariaDB/server/commit/2a9f84b)\
  2016-01-11 10:28:00 +0200
  * [MDEV-9354](https://jira.mariadb.org/browse/MDEV-9354): Debian: unmask the mysql.service on installation
* [Revision #7cd94c6](https://github.com/MariaDB/server/commit/7cd94c6)\
  2016-01-10 11:57:36 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #0891ae2](https://github.com/MariaDB/server/commit/0891ae2)\
  2016-01-09 20:52:17 +0100\
  \*
  * Fix [MDEV-9239](https://jira.mariadb.org/browse/MDEV-9239). Meanwhile, make all references to the database in XTAB Schema (was sometimes in XTAB Catalog)
* [Revision #e37372c](https://github.com/MariaDB/server/commit/e37372c)\
  2015-12-27 21:14:07 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #6883e5c](https://github.com/MariaDB/server/commit/6883e5c)\
  2015-12-27 19:45:51 +0100\
  \*
  * Fix [MDEV-9322](https://jira.mariadb.org/browse/MDEV-9322).
* [Revision #3f6159f](https://github.com/MariaDB/server/commit/3f6159f)\
  2015-12-14 23:47:05 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #11c339f](https://github.com/MariaDB/server/commit/11c339f)\
  2015-12-14 23:45:23 +0100\
  \*
  * Fix [MDEV-9279](https://jira.mariadb.org/browse/MDEV-9279). Replacing exit(1) in yy\_fatal\_error by a longjmp.

{% @marketo/form formid="4316" formId="4316" %}
