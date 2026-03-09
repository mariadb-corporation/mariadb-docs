# MariaDB 10.1.17 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.17)[Release Notes](../../old-releases/10.1/10.1.17.md)[Changelog](mariadb-10117-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 30 Aug 2016

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.17.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #a02642b](https://github.com/MariaDB/server/commit/a02642b)\
  2016-06-23 17:50:07 +0200
  * [MDEV-10017](https://jira.mariadb.org/browse/MDEV-10017): Get unexpected `Empty Set` for correlated subquery with aggregate functions (part 1)
* [Revision #00d84ea](https://github.com/MariaDB/server/commit/00d84ea)\
  2016-06-22 11:17:44 +0200
  * [MDEV-10045](https://jira.mariadb.org/browse/MDEV-10045): Server crashes in Time\_and\_counter\_tracker::incr\_loops
* [Revision #7d115e7](https://github.com/MariaDB/server/commit/7d115e7)\
  2016-08-27 19:50:42 +0300
  * [MDEV-10604](https://jira.mariadb.org/browse/MDEV-10604) Create a list of unstable MTR tests to be disabled in distribution builds
* [Revision #467217e](https://github.com/MariaDB/server/commit/467217e)\
  2016-08-26 12:45:48 -0400
  * [MDEV-9510](https://jira.mariadb.org/browse/MDEV-9510): Print extra info to error log
* [Revision #a66092f](https://github.com/MariaDB/server/commit/a66092f) 2016-08-26 10:12:47 +0200 - Merge branch 'bb-10.1-serg' into 10.1
* [Revision #3575618](https://github.com/MariaDB/server/commit/3575618)\
  2016-08-25 21:28:26 -0400
  * Post merge fixes.
* [Revision #90266e8](https://github.com/MariaDB/server/commit/90266e8) 2016-08-25 15:39:39 -0400 - Merge branch '10.0-galera' into bb-10.1-serg
* [Revision #b506d95](https://github.com/MariaDB/server/commit/b506d95) 2016-08-24 19:41:11 -0400 - Merge branch '5.5-galera' into 10.0-galera
* [Revision #d40d3f4](https://github.com/MariaDB/server/commit/d40d3f4)\
  2016-07-19 20:44:02 +0000
  * [MDEV-10314](https://jira.mariadb.org/browse/MDEV-10314) : wsrep\_client\_thread was not set in threadpool.
* [Revision #abfbe80](https://github.com/MariaDB/server/commit/abfbe80)\
  2016-08-10 14:48:44 -0400
  * MW-292: Fix test case
* [Revision #dfadb36](https://github.com/MariaDB/server/commit/dfadb36)\
  2016-07-15 01:13:32 -0700
  * Galera MTR Tests: Test case for MW-292 : NOW() returns stale timestamp after transaction replay
* [Revision #9a809fe](https://github.com/MariaDB/server/commit/9a809fe)\
  2016-07-14 14:29:59 +0200
  * MW-292 Reset timestamp after transaction replay
* [Revision #38a0def](https://github.com/MariaDB/server/commit/38a0def) 2016-08-10 10:34:54 -0400 - Merge tag 'mariadb-5.5.51' into 5.5-galera
* [Revision #44e3046](https://github.com/MariaDB/server/commit/44e3046)\
  2016-08-03 22:15:57 -0400
  * [MDEV-10487](https://jira.mariadb.org/browse/MDEV-10487): Galera SST using rsync does not filter out lost+found
* [Revision #c309e99](https://github.com/MariaDB/server/commit/c309e99) 2016-08-24 19:30:32 -0400 - Merge branch '10.0' into 10.0-galera
* [Revision #8b09db8](https://github.com/MariaDB/server/commit/8b09db8)\
  2016-08-24 17:13:20 -0400
  * Fixes/improvements in galera test suite
* [Revision #1b7c5de](https://github.com/MariaDB/server/commit/1b7c5de)\
  2016-08-24 15:32:48 -0400
  * [MDEV-10566](https://jira.mariadb.org/browse/MDEV-10566): Create role statement replicated inconsistently in Galera Cluster
* [Revision #f381ad5](https://github.com/MariaDB/server/commit/f381ad5)\
  2016-08-21 20:13:51 -0400
  * Update WSREP\_PATCH\_REVNO.
* [Revision #3f481e5](https://github.com/MariaDB/server/commit/3f481e5)\
  2016-08-21 20:09:05 -0400
  * Fixes for failing tests (post-merge).
* [Revision #cced23c](https://github.com/MariaDB/server/commit/cced23c)\
  2016-06-29 16:50:53 -0400
  * [MDEV-9423](https://jira.mariadb.org/browse/MDEV-9423): cannot add new node to the cluser: Binlog..
* [Revision #415823a](https://github.com/MariaDB/server/commit/415823a)\
  2016-06-08 15:19:01 +0300
  * Refs: MW-279
    * fixes in innodb to skip wsrep processing (like kill victim) when running in native mysql mode
    * similar fixes in mysql server side
    * forcing tc\_log\_dummy in native mysql mode when no binlog used. wsrep hton messes up handler counter and used to lead in using tc\_log\_mmap instead. Bad news is that tc\_log\_mmap does not seem to work at all
* [Revision #fec296c](https://github.com/MariaDB/server/commit/fec296c)\
  2016-08-12 10:57:58 +0200
  * refs codership/mysql-wsrep#267 Fix Galera crash at startup when compiled with gcc 6
* [Revision #2e56c7f](https://github.com/MariaDB/server/commit/2e56c7f)\
  2016-08-09 12:34:03 +0300
  * Bump WSREP\_PATCH\_VERSION to 16
* [Revision #f01a16b](https://github.com/MariaDB/server/commit/f01a16b)\
  2016-08-04 00:33:12 -0700
  * Galera MTR Tests: fortify galera\_bf\_abort\_flush\_for\_export against sporadic failures.
* [Revision #30c6ac3](https://github.com/MariaDB/server/commit/30c6ac3)\
  2016-08-03 02:52:39 -0700
  * Galera MTR Tests: Attempt to fortify galera\_kill\_ddl.test against sporadic failures
* [Revision #0656453](https://github.com/MariaDB/server/commit/0656453)\
  2016-07-22 04:16:09 -0700
  * Galera MTR Tests: increase timeouts and adjust some sporadically-failing tests so that the Galera suites can be run with --parallel=4
* [Revision #85b9718](https://github.com/MariaDB/server/commit/85b9718)\
  2016-07-13 03:19:20 -0700
  * Galera MTR Tests: Test case for galera#414 - crash on shutdown with gcs.max\_packet\_size=2
* [Revision #ea3ff73](https://github.com/MariaDB/server/commit/ea3ff73)\
  2016-06-09 09:21:43 +0200
  * GCF-837 Fix crash when loading wrong provider version
* [Revision #bf19492](https://github.com/MariaDB/server/commit/bf19492)\
  2016-06-13 17:49:42 +0200
  * GCF-837 Check wsrep interface version before loading provider
* [Revision #dfa9012](https://github.com/MariaDB/server/commit/dfa9012)\
  2016-06-20 14:35:22 +0200
  * MW-285 MTR test case for broken foreign key constraints
* [Revision #c9ac48f](https://github.com/MariaDB/server/commit/c9ac48f)\
  2016-06-02 16:44:54 +0530
  * PXC#592: Tried closing fk-reference-table that was never opened.
* [Revision #88a1592](https://github.com/MariaDB/server/commit/88a1592)\
  2016-06-14 17:18:21 +0200
  * MW-286 Avoid spurious deadlock errors when wsrep\_on is disabled
* [Revision #a12fa57](https://github.com/MariaDB/server/commit/a12fa57)\
  2016-06-13 06:17:33 -0700
  * Galera MTR Tests: Run galera\_pc\_weight on freshly started servers in order to prevent interaction with other tests
* [Revision #5996c7b](https://github.com/MariaDB/server/commit/5996c7b)\
  2016-06-07 10:46:14 +0300
  * refs: MW-279
    * At startup time global wsrep\_on is set too late and some wsrep paths may be executed because of this. e.g. replication slave restart could happen before wsrep\_on state is defined.
    * This fix checks both global wsrep\_on and wsrep\_provider values to determine if wsrep processing should happen
    * Fix affects all instances where WSREP\_ON macro is used
* [Revision #0e83726](https://github.com/MariaDB/server/commit/0e83726)\
  2016-06-03 04:26:17 -0700
  * Galera MTR Tests: force galera\_3nodes.galera\_pc\_bootstrap.test to run on a fresh cluster in order to avoid interaction with galera\_3nodes.galera\_innobackupex\_backup.test
* [Revision #5609020](https://github.com/MariaDB/server/commit/5609020)\
  2016-06-02 23:56:16 -0700
  * Galera MTR Tests: fortify galera\_parallel\_simple.test against sporadic failures
* [Revision #1cb01fe](https://github.com/MariaDB/server/commit/1cb01fe)\
  2016-06-02 23:39:12 -0700
  * Galera MTR Tests: Fortify galera\_restart\_nochanges.test against sporadic failures due to node not being ready immediately after restart
* [Revision #92162e6](https://github.com/MariaDB/server/commit/92162e6)\
  2016-05-18 11:07:58 +0200
  * MW-175 Fix definitively lost memory in wsrep\_get\_params
* [Revision #137af55](https://github.com/MariaDB/server/commit/137af55)\
  2016-05-17 22:23:51 -0700
  * Galera MTR Tests: stability fixes
* [Revision #db837fd](https://github.com/MariaDB/server/commit/db837fd)\
  2016-05-01 23:29:55 -0700
  * Galera MTR Tests: Adjust tests for xtrabackup 2.4.2
* [Revision #81174c9](https://github.com/MariaDB/server/commit/81174c9)\
  2016-08-15 11:29:48 -0400
  * Fix galera/MW-44 test post-merge.
* [Revision #182787f](https://github.com/MariaDB/server/commit/182787f)\
  2016-04-14 01:25:54 -0700
  * Galera MTR Tests: Adjust galera\_log\_output\_csv.test to account for the fix for MW-44
* [Revision #675bcf3](https://github.com/MariaDB/server/commit/675bcf3)\
  2016-04-14 01:03:37 -0700
  * Galera MTR Tests: A test for MW-44 - Disable general log for applier threads
* [Revision #f49500a](https://github.com/MariaDB/server/commit/f49500a)\
  2016-04-05 14:08:39 +0300
  * MW-44 Disable general log for applier threads
* [Revision #3f22e74](https://github.com/MariaDB/server/commit/3f22e74)\
  2016-08-15 11:14:57 -0400
  * Fix galera/[GAL-382](https://github.com/codership/galera/issues/382) test post-merge.
* [Revision #9b42f09](https://github.com/MariaDB/server/commit/9b42f09)\
  2016-04-04 07:09:32 -0700
  * Galera MTR Tests: Add test for [GAL-382](https://github.com/codership/galera/issues/382), codership/galera#382 - InnoDB: Failing assertion: xid\_seqno > trx\_sys\_cur\_xid\_seqno in trx0sys.cc line 356
* [Revision #fce9217](https://github.com/MariaDB/server/commit/fce9217)\
  2016-04-04 05:32:50 -0700
  * Galera MTR Test: Fix for MW-258.test - do not use SHOW PROCESSLIST
* [Revision #dda1144](https://github.com/MariaDB/server/commit/dda1144)\
  2016-04-04 05:14:13 -0700
  * Galera MTR Tests: Fixed tests to account for [GAL-391](https://github.com/codership/galera/issues/391) , [GAL-374](https://github.com/codership/galera/issues/374)
* [Revision #d45b582](https://github.com/MariaDB/server/commit/d45b582)\
  2016-04-02 22:37:22 -0300
  * MW-259 - moved wsrep desync/resync calls from wsrep\_desync\_update() to wsrep\_desync\_check() method which does not hold the lock and is arguably a more fitting place to change provider state - before changing the actual variable value.
* [Revision #4582a4b](https://github.com/MariaDB/server/commit/4582a4b)\
  2016-08-12 14:03:24 -0400
  * Fix galera\_ist\_recv\_bind.test.
* [Revision #90d92d2](https://github.com/MariaDB/server/commit/90d92d2)\
  2016-04-02 21:51:26 -0300
  * MW-258 - RSU DDL should not rely on the global wsrep\_desync variable value and should always try to desync on its own.
* [Revision #a00f4b2](https://github.com/MariaDB/server/commit/a00f4b2)\
  2016-03-15 03:38:31 -0700
  * Refs codership/galera#105 An MTR test for ist.recv\_bind
* [Revision #b758e92](https://github.com/MariaDB/server/commit/b758e92)\
  2016-08-12 13:42:12 -0400
  * Fix galera\_transaction\_replay.test.
* [Revision #4e4ad17](https://github.com/MariaDB/server/commit/4e4ad17)\
  2016-03-08 18:10:21 +0200
  * Refs MW-255 - popping PS reprepare observer before BF aborted PS replaying begins dangling observer will cause failure in open\_table() ater on - test case for this anomaly
* [Revision #d246630](https://github.com/MariaDB/server/commit/d246630)\
  2016-03-07 23:34:03 +0200
  * Refs MW-252 - changed the condition when to do implicit desync as part of FTWRL to cover only case when node is PC and synced. Donor node has alreaydy desycned and other states mean that node is not in cluster, so desync is not even possible.
* [Revision #f3444c4](https://github.com/MariaDB/server/commit/f3444c4)\
  2016-03-04 14:20:58 +0200
  * Bump WSREP\_PATCH\_VERSION to 14
* [Revision #8b998a4](https://github.com/MariaDB/server/commit/8b998a4)\
  2016-08-12 12:56:41 -0400
  * Update galera version-dependent tests.
* [Revision #65cf1d3](https://github.com/MariaDB/server/commit/65cf1d3)\
  2016-08-11 22:28:57 -0400
  * Refs: MW-252 Test fix post-merge
* [Revision #fe6ebb6](https://github.com/MariaDB/server/commit/fe6ebb6)\
  2016-03-01 08:32:06 -0800
  * Refs: MW-252 MTR tests for FTWRL and desync
* [Revision #a03c45f](https://github.com/MariaDB/server/commit/a03c45f)\
  2016-03-01 10:56:21 +0200
  * Refs: MW-252 - if wsrep\_on==OFF, unlock tables would resume provider even though it was not passed in FTWRL processing. This is fixed in this patch.
* [Revision #8ec50eb](https://github.com/MariaDB/server/commit/8ec50eb)\
  2016-02-29 22:54:58 +0200
  * Refs MW-252 - reverted from tracking donor servicing thread. With xtrabackup SST, xtrabackup thread will call FTWRL and node is desynced upfront - Skipping desync in FTWRL if node is operating as donor
* [Revision #b159b66](https://github.com/MariaDB/server/commit/b159b66)\
  2016-02-29 16:36:17 +0200
  * Refs MW-252 - Calling FTWRL two times in a row caused desync error, this is fixed by making sub-sequent FTWRL calls bail out before wsrep operations
* [Revision #4290117](https://github.com/MariaDB/server/commit/4290117)\
  2016-02-29 15:24:06 +0200
  * Refs MW-252 - enveloped FTWRL processing with wsrep desync/resync calls. This way FTWRL processing node will not cause flow control to kick in - donor servicing thread is unfortunate exception, we must let him to pause provider as part of FTWRL phase, but not desync/resync as this is done as part of donor control on higher level
* [Revision #da9650a](https://github.com/MariaDB/server/commit/da9650a)\
  2016-02-19 13:08:22 +0200
  * Refs: MW-248 - some more code cleanup
* [Revision #ae0fec9](https://github.com/MariaDB/server/commit/ae0fec9)\
  2016-02-19 13:02:59 +0200
  * refs: MW-248 - removed the off topic mtr test
* [Revision #5edf55b](https://github.com/MariaDB/server/commit/5edf55b)\
  2016-02-19 11:48:09 +0200
  * Refs: MW-248 - fixed the test case and extended with autoinc modification is master side
* [Revision #df96eb5](https://github.com/MariaDB/server/commit/df96eb5)\
  2016-02-18 14:34:53 +0200
  * Refs: MW-248 - test cases from PXC for reproducing the issue - initial fix
* [Revision #a53ac77](https://github.com/MariaDB/server/commit/a53ac77)\
  2016-08-10 12:30:57 -0400
  * Cleanup: Remove dead code
* [Revision #58386ca](https://github.com/MariaDB/server/commit/58386ca)\
  2016-01-11 22:43:27 +0200
  * refs codership/mysql-wsrep#239
    * Synced xtrabackup SST scripts from PXC source tree as of PXC 5.6.27-25.13
    * PXC#480: xtrabackup-v2 SST fails with multiple log\_bin directives in my.cn
    * PXC#460: wsrep\_sst\_auth don't work in Percona-XtraDB-Cluster-56-5.6.25-25.
    * PXC-416: Fix SST related issues.
    * PXC-389: Merge remote-tracking branch 'wsrep/5.6' into 5.6-wsrep-pxc389
    * Bug #1431101: SST does not clobber backup-my.cnf
* [Revision #9f211d4](https://github.com/MariaDB/server/commit/9f211d4)\
  2016-07-19 20:44:02 +0000
  * [MDEV-10314](https://jira.mariadb.org/browse/MDEV-10314) : wsrep\_client\_thread was not set in threadpool.
* [Revision #963673e](https://github.com/MariaDB/server/commit/963673e)\
  2016-07-25 21:52:02 -0400
  * MW-292: Fix test case
* [Revision #e572878](https://github.com/MariaDB/server/commit/e572878)\
  2016-07-15 01:13:32 -0700
  * Galera MTR Tests: Test case for MW-292 : NOW() returns stale timestamp after transaction replay
* [Revision #7431368](https://github.com/MariaDB/server/commit/7431368)\
  2016-07-14 14:29:59 +0200
  * MW-292 Reset timestamp after transaction replay
* [Revision #cbc8a84](https://github.com/MariaDB/server/commit/cbc8a84)\
  2016-07-25 11:51:21 -0400
  * MW-267 Enforce wsrep\_max\_ws\_size limit in wsrep provider
* [Revision #74f80b3](https://github.com/MariaDB/server/commit/74f80b3)\
  2016-05-06 16:07:53 +0200
  * MW-267 Enforce wsrep\_max\_ws\_size limit in wsrep provider
* [Revision #5197fcf](https://github.com/MariaDB/server/commit/5197fcf)\
  2016-05-05 13:20:32 +0200
  * MW-269 Fix outstanding issues with wsrep\_max\_ws\_rows
* [Revision #e373f60](https://github.com/MariaDB/server/commit/e373f60)\
  2016-07-20 18:12:17 -0400
  * MW-265 Add support for wsrep\_max\_ws\_rows
* [Revision #3db92ee](https://github.com/MariaDB/server/commit/3db92ee)\
  2016-05-03 16:22:01 +0200
  * MW-265 Add support for wsrep\_max\_ws\_rows
* [Revision #dfa3046](https://github.com/MariaDB/server/commit/dfa3046)\
  2016-08-25 15:11:21 +0200
  * fix a test for windows
* [Revision #6b1863b](https://github.com/MariaDB/server/commit/6b1863b) 2016-08-25 12:40:09 +0200 - Merge branch '10.0' into 10.1
* [Revision #5bbe929](https://github.com/MariaDB/server/commit/5bbe929)\
  2016-08-24 17:39:57 +0300
  * [MDEV-10604](https://jira.mariadb.org/browse/MDEV-10604) Create a list of unstable MTR tests to be disabled in distribution builds
* [Revision #ed99e2c](https://github.com/MariaDB/server/commit/ed99e2c)\
  2016-08-18 14:00:40 +0300
  * [MDEV-10341](https://jira.mariadb.org/browse/MDEV-10341): InnoDB: Failing assertion: mutex\_own(mutex) - mutex\_exit\_func
* [Revision #4eb898b](https://github.com/MariaDB/server/commit/4eb898b)\
  2016-08-16 11:25:11 +0300
  * [MDEV-10563](https://jira.mariadb.org/browse/MDEV-10563) Crash during shutdown in Master\_info\_index::any\_slave\_sql\_running
* [Revision #4da2b83](https://github.com/MariaDB/server/commit/4da2b83)\
  2016-08-23 15:03:31 +0300
  * Fixed compiler error and some warnings on windows
* [Revision #a5051cd](https://github.com/MariaDB/server/commit/a5051cd)\
  2016-08-22 10:19:07 +0300
  * Minor cleanups - Remove impossible test in test\_quick\_select - Ensure that is\_fatal\_error is set if we run out of stack space
* [Revision #b511096](https://github.com/MariaDB/server/commit/b511096)\
  2016-08-22 10:16:00 +0300
  * [MDEV-10630](https://jira.mariadb.org/browse/MDEV-10630) rpl.rpl\_mdev6020 fails in buildbot with timeout
* [Revision #5932fa7](https://github.com/MariaDB/server/commit/5932fa7)\
  2016-08-21 20:38:47 +0300
  * Fixed "Packets out of order" warning message on stdout in clients, compiled for debugging, when the server goes down
* [Revision #6f31dd0](https://github.com/MariaDB/server/commit/6f31dd0)\
  2016-08-21 20:18:39 +0300
  * Added new status variables to make it easier to debug certain problems: - Handler\_read\_retry - Update\_scan - Delete\_scan
* [Revision #8d5a0d6](https://github.com/MariaDB/server/commit/8d5a0d6)\
  2016-08-21 20:14:13 +0300
  * Cleanups and minor fixes
    * Fixed typos
    * Added --core-on-failure to mysql-test-run
    * More DBUG\_PRINT in viosocket.c
    * Don't forget CLIENT\_REMEMBER\_OPTIONS for compressed slave protocol
    * Removed not used stage variables
* [Revision #05f61ba](https://github.com/MariaDB/server/commit/05f61ba)\
  2016-08-16 21:23:57 +0200
  * [MDEV-10559](https://jira.mariadb.org/browse/MDEV-10559): main.mysql\_client\_test\_nonblock crashes in buildbot on 10.0
* [Revision #df09d5e](https://github.com/MariaDB/server/commit/df09d5e)\
  2016-08-15 16:28:19 +0200
  * [MDEV-10559](https://jira.mariadb.org/browse/MDEV-10559): main.mysql\_client\_test\_nonblock crashes in buildbot on 10.0
* [Revision #47a1087](https://github.com/MariaDB/server/commit/47a1087) 2016-08-14 09:16:07 +0200 - Merge branch 'bb-10.0-serg' into 10.0
* [Revision #191f7b0](https://github.com/MariaDB/server/commit/191f7b0)\
  2016-08-10 21:15:51 +0200
  * after merge fixes
* [Revision #2bd9495](https://github.com/MariaDB/server/commit/2bd9495) 2016-08-10 19:58:42 +0200 - Merge branch 'connect/10.0' into 10.0
* [Revision #a2934d2](https://github.com/MariaDB/server/commit/a2934d2)\
  2016-08-10 18:27:31 +0200
  * JdbcInterface: change return type of ...Field function modified: storage/connect/JdbcInterface.java
* [Revision #ec72508](https://github.com/MariaDB/server/commit/ec72508)\
  2016-07-15 00:50:18 +0200
  * Change jdbc test to reflect girls.txt LF ending
* [Revision #44012db](https://github.com/MariaDB/server/commit/44012db)\
  2016-07-14 20:12:22 +0200
  * All changes made on 10.1 for last 11 commits
* [Revision #077f29a](https://github.com/MariaDB/server/commit/077f29a) 2016-08-10 19:57:13 +0200 - Merge branch 'merge/merge-tokudb-5.6' into 10.0
* [Revision #4f2d214](https://github.com/MariaDB/server/commit/4f2d214)\
  2016-08-10 19:30:20 +0200
  * 5.6.31-77.0
* [Revision #3863e72](https://github.com/MariaDB/server/commit/3863e72) 2016-08-10 19:55:45 +0200 - Merge branch 'merge/merge-xtradb-5.6' into 10.0
* [Revision #64752ac](https://github.com/MariaDB/server/commit/64752ac)\
  2016-08-10 19:24:58 +0200
  * 5.6.31-77.0
* [Revision #e672d3f](https://github.com/MariaDB/server/commit/e672d3f) 2016-08-10 19:44:28 +0200 - Merge branch 'merge/merge-perfschema-5.6' into 10.0
* [Revision #0d8bb01](https://github.com/MariaDB/server/commit/0d8bb01)\
  2016-08-10 19:26:54 +0200
  * 5.6.32
* [Revision #57fbc60](https://github.com/MariaDB/server/commit/57fbc60) 2016-08-10 19:43:37 +0200 - Merge branch 'merge/merge-innodb-5.6' into 10.0
* [Revision #b4f97a1](https://github.com/MariaDB/server/commit/b4f97a1)\
  2016-08-10 19:23:00 +0200
  * 5.6.32
* [Revision #309c08c](https://github.com/MariaDB/server/commit/309c08c) 2016-08-10 19:19:05 +0200 - Merge branch '5.5' into 10.0
* [Revision #5ad0206](https://github.com/MariaDB/server/commit/5ad0206)\
  2016-08-09 16:15:10 +0300
  * [MDEV-10341](https://jira.mariadb.org/browse/MDEV-10341): InnoDB: Failing assertion: mutex\_own(mutex) - mutex\_exit\_func
* [Revision #0098d78](https://github.com/MariaDB/server/commit/0098d78)\
  2016-08-09 13:25:40 +0200
  * [MDEV-10465](https://jira.mariadb.org/browse/MDEV-10465) general\_log\_file can be abused
* [Revision #a3f6424](https://github.com/MariaDB/server/commit/a3f6424)\
  2016-08-08 12:58:27 +0200
  * [MDEV-6128](https://jira.mariadb.org/browse/MDEV-6128):\[PATCH] mysqlcheck wrongly escapes '.' in table names
* [Revision #2a54a53](https://github.com/MariaDB/server/commit/2a54a53)\
  2016-08-08 10:27:22 +0200
  * [MDEV-10465](https://jira.mariadb.org/browse/MDEV-10465) general\_log\_file can be abused
* [Revision #a7c43a6](https://github.com/MariaDB/server/commit/a7c43a6)\
  2016-01-26 14:49:25 +0200
  * [MDEV-9304](https://jira.mariadb.org/browse/MDEV-9304): MariaDB crash with specific query
* [Revision #5269d37](https://github.com/MariaDB/server/commit/5269d37)\
  2016-08-08 18:37:02 +0400
  * [MDEV-10468](https://jira.mariadb.org/browse/MDEV-10468) Assertion \`nr >= 0.0' failed in Item\_sum\_std::val\_real()
* [Revision #1b3430a](https://github.com/MariaDB/server/commit/1b3430a)\
  2016-08-08 16:04:40 +0400
  * [MDEV-10500](https://jira.mariadb.org/browse/MDEV-10500) CASE/IF Statement returns multiple values and shifts further result values to the next column
* [Revision #5e23b63](https://github.com/MariaDB/server/commit/5e23b63)\
  2016-08-07 11:02:42 +0200
  * [MDEV-10506](https://jira.mariadb.org/browse/MDEV-10506) Protocol::end\_statement(): Assertion \`0' failed upon ALTER TABLE
* [Revision #93d5cdf](https://github.com/MariaDB/server/commit/93d5cdf)\
  2016-08-04 13:14:45 +0300
  * [MDEV-9946](https://jira.mariadb.org/browse/MDEV-9946): main.xtradb\_mrr fails sporadically
* [Revision #c0cb84b](https://github.com/MariaDB/server/commit/c0cb84b) 2016-08-04 10:57:55 +0200 - Merge branch 'bb-5.5-serg' into 5.5
* [Revision #470f259](https://github.com/MariaDB/server/commit/470f259)\
  2016-08-03 20:56:24 +0200
  * [MDEV-10465](https://jira.mariadb.org/browse/MDEV-10465) general\_log\_file can be abused
* [Revision #0214115](https://github.com/MariaDB/server/commit/0214115)\
  2016-08-01 16:53:57 +0200
  * trivial cleanup
* [Revision #03dec1a](https://github.com/MariaDB/server/commit/03dec1a)\
  2016-08-03 18:05:29 +0200
  * [MDEV-10350](https://jira.mariadb.org/browse/MDEV-10350) "./mtr --report-features" doesn't work
* [Revision #9d2f892](https://github.com/MariaDB/server/commit/9d2f892)\
  2016-08-03 17:58:56 +0200
  * [MDEV-7329](https://jira.mariadb.org/browse/MDEV-7329) plugins.pam\_cleartext fails sporadically in buildbot
* [Revision #75891ed](https://github.com/MariaDB/server/commit/75891ed)\
  2016-08-03 17:50:45 +0200
  * improve pam\_cleartext.test a bit
* [Revision #5265243](https://github.com/MariaDB/server/commit/5265243) 2016-08-03 20:44:08 +0200 - Merge branch 'merge/merge-xtradb-5.5' into 5.5
* [Revision #e316c46](https://github.com/MariaDB/server/commit/e316c46)\
  2016-08-03 20:43:29 +0200
  * 5.5.50-38.0
* [Revision #19fe10c](https://github.com/MariaDB/server/commit/19fe10c)\
  2016-08-03 20:39:47 +0200
  * [MDEV-6581](https://jira.mariadb.org/browse/MDEV-6581) Writing to TEMPORARY TABLE not possible in read-only
* [Revision #a350e53](https://github.com/MariaDB/server/commit/a350e53) 2016-08-03 20:38:25 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #eb32dfd](https://github.com/MariaDB/server/commit/eb32dfd)\
  2016-08-03 11:49:35 +0400
  * [MDEV-10365](https://jira.mariadb.org/browse/MDEV-10365) - Race condition in error handling of INSERT DELAYED
* [Revision #511313b](https://github.com/MariaDB/server/commit/511313b)\
  2016-08-03 13:42:46 +0000
  * [MDEV-10010](https://jira.mariadb.org/browse/MDEV-10010) - potential deadlock on windows due to recursive SRWLock acquisition
* [Revision #141f88d](https://github.com/MariaDB/server/commit/141f88d)\
  2016-08-03 12:41:38 +0000
  * [MDEV-10357](https://jira.mariadb.org/browse/MDEV-10357) my\_context\_continue() does not store current fiber on Windows
* [Revision #ecb7ce7](https://github.com/MariaDB/server/commit/ecb7ce7)\
  2016-08-03 15:55:48 +0400
  * [MDEV-10467](https://jira.mariadb.org/browse/MDEV-10467) Assertion \`nr >= 0.0' failed in Item\_sum\_std::val\_real() Backporting [MDEV-5781](https://jira.mariadb.org/browse/MDEV-5781) from 10.0.
* [Revision #35c9c85](https://github.com/MariaDB/server/commit/35c9c85)\
  2016-08-03 13:40:53 +0300
  * [MDEV-10217](https://jira.mariadb.org/browse/MDEV-10217): innodb.innodb\_bug59641 fails sporadically in buildbot: InnoDB: Failing assertion: current\_rec != insert\_rec in file page0cur.c line 1052
* [Revision #6b71a6d](https://github.com/MariaDB/server/commit/6b71a6d)\
  2016-08-02 18:52:51 +0200
  * [MDEV-10383](https://jira.mariadb.org/browse/MDEV-10383) Named pipes : multiple servers can listen on the same pipename
* [Revision #5fdb3cf](https://github.com/MariaDB/server/commit/5fdb3cf)\
  2016-07-29 18:21:08 +0200
  * [MDEV-10419](https://jira.mariadb.org/browse/MDEV-10419): crash in [mariadb 10.1.16](../../old-releases/10.1/10.1.16.md)-MariaDB-1trusty
* [Revision #c6aaa2a](https://github.com/MariaDB/server/commit/c6aaa2a)\
  2016-07-30 10:53:01 +0300
  * [MDEV-10228](https://jira.mariadb.org/browse/MDEV-10228): update test results
* [Revision #15ef38d](https://github.com/MariaDB/server/commit/15ef38d)\
  2016-07-27 00:38:51 +0300
  * [MDEV-10228](https://jira.mariadb.org/browse/MDEV-10228): Delete missing rows with OR conditions
* [Revision #1b5da2c](https://github.com/MariaDB/server/commit/1b5da2c)\
  2016-07-21 15:32:28 +0400
  * [MDEV-10316](https://jira.mariadb.org/browse/MDEV-10316) - main.type\_date fails around midnight sporadically
* [Revision #5cf49cd](https://github.com/MariaDB/server/commit/5cf49cd)\
  2016-07-15 23:51:30 +0300
  * [MDEV-10248](https://jira.mariadb.org/browse/MDEV-10248) Cannot Remove Test Tables
* [Revision #72290cd](https://github.com/MariaDB/server/commit/72290cd) 2016-08-13 09:27:57 +0300 - Merge branch '10.0' of github.com:MariaDB/server into 10.0
* [Revision #98e36b2](https://github.com/MariaDB/server/commit/98e36b2)\
  2016-08-12 20:02:23 +0300
  * With parallel replication we have had a couple of bugs where DDL's (like DROP TABLE) has been scheduled before conflicting DDL's (like INSERT) are commited.
* [Revision #66ac894](https://github.com/MariaDB/server/commit/66ac894)\
  2016-08-11 17:50:21 +0200
  * [MDEV-10455](https://jira.mariadb.org/browse/MDEV-10455): libmariadbclient18 + MySQL-python leaks memory on failed connections
* [Revision #9b23f80](https://github.com/MariaDB/server/commit/9b23f80)\
  2016-08-11 14:39:47 +0300
  * [MDEV-10535](https://jira.mariadb.org/browse/MDEV-10535): ALTER TABLE causes standalone/wsrep cluster crash
* [Revision #b3df257](https://github.com/MariaDB/server/commit/b3df257)\
  2016-08-09 16:51:35 +0300
  * [MDEV-10469](https://jira.mariadb.org/browse/MDEV-10469): innodb.innodb-alter-tempfile fails in buildbot: InnoDB: Warning: database page corruption or a failed
* [Revision #b5fb2a6](https://github.com/MariaDB/server/commit/b5fb2a6)\
  2016-08-02 14:29:55 +0400
  * Fixed main.contributors failure
* [Revision #246866d](https://github.com/MariaDB/server/commit/246866d) 2016-08-02 10:32:48 +0400 - Merge pull request #207 from iangilfillan/10.0
* [Revision #5d0dfcb](https://github.com/MariaDB/server/commit/5d0dfcb)\
  2016-07-27 15:29:32 +0200
  * Update contributors
* [Revision #df4fddb](https://github.com/MariaDB/server/commit/df4fddb)\
  2016-07-25 01:57:00 +0300
  * [MDEV-10428](https://jira.mariadb.org/browse/MDEV-10428) main.information\_schema\_stats fails sporadically in buildbot
* [Revision #bf2e315](https://github.com/MariaDB/server/commit/bf2e315)\
  2016-07-18 11:50:08 +0400
  * [MDEV-8569](https://jira.mariadb.org/browse/MDEV-8569) build\_table\_filename() doesn't support temporary tables.
* [Revision #ea91bb6](https://github.com/MariaDB/server/commit/ea91bb6)\
  2016-07-26 12:34:04 +0200
  * [MDEV-10361](https://jira.mariadb.org/browse/MDEV-10361) Crash in pam\_securid.so with auth\_pam connecting from SQLyog
* [Revision #2d65679](https://github.com/MariaDB/server/commit/2d65679)\
  2016-08-25 19:47:38 +0300
  * [MDEV-10665](https://jira.mariadb.org/browse/MDEV-10665): Json\_writer produces extra members in output
* [Revision #2024cdd](https://github.com/MariaDB/server/commit/2024cdd)\
  2016-08-22 21:27:20 -0400
  * [MDEV-10518](https://jira.mariadb.org/browse/MDEV-10518): Large wsrep\_gtid\_domain\_id may break IST
* [Revision #3ac0721](https://github.com/MariaDB/server/commit/3ac0721)\
  2016-08-22 19:06:32 -0400
  * [MDEV-10507](https://jira.mariadb.org/browse/MDEV-10507): [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) + wsrep fails to start under systemd post-reboot
* [Revision #294961c](https://github.com/MariaDB/server/commit/294961c)\
  2016-08-22 18:38:06 -0400
  * [MDEV-10538](https://jira.mariadb.org/browse/MDEV-10538): MariaDB fails to start without galera\_recovery in systemd mode
* [Revision #d0d99de](https://github.com/MariaDB/server/commit/d0d99de) 2016-08-18 11:51:47 +0400 - Merge pull request #206 from prohaska7/10.1-with-asan
* [Revision #2f5ae0f](https://github.com/MariaDB/server/commit/2f5ae0f)\
  2016-07-24 10:06:18 -0400
  * [MDEV-10412](https://jira.mariadb.org/browse/MDEV-10412) fix WITH\_ASAN option for 10.1
* [Revision #1e160e5](https://github.com/MariaDB/server/commit/1e160e5)\
  2016-08-17 13:57:34 +0400
  * [MDEV-10404](https://jira.mariadb.org/browse/MDEV-10404) - Improved systemd service hardening causes SELinux problems
* [Revision #48fbb2b](https://github.com/MariaDB/server/commit/48fbb2b)\
  2016-08-16 12:34:58 +0200
  * [MDEV-10553](https://jira.mariadb.org/browse/MDEV-10553): Semi-sync replication hangs when master opens new binlog file
* [Revision #a8c2f68](https://github.com/MariaDB/server/commit/a8c2f68) 2016-08-02 09:53:41 +0300 - Merge pull request #208 from Cona19/10.1-remove-unnecessary-semicolon
* [Revision #558c8ce](https://github.com/MariaDB/server/commit/558c8ce)\
  2016-08-01 12:13:14 +0900
  * Remove unnecessary semicolon
* [Revision #ed48fcf](https://github.com/MariaDB/server/commit/ed48fcf)\
  2016-08-01 17:02:28 -0400
  * [MDEV-10478](https://jira.mariadb.org/browse/MDEV-10478): Trx abort does not work in autocommit mode
* [Revision #84a9e05](https://github.com/MariaDB/server/commit/84a9e05)\
  2016-08-01 12:19:29 +0300
  * [MDEV-10470](https://jira.mariadb.org/browse/MDEV-10470): main.derived fails, buildbot is broken - Update test result (checked)
* [Revision #67480fc](https://github.com/MariaDB/server/commit/67480fc)\
  2016-07-28 15:49:59 -0400
  * [MDEV-10429](https://jira.mariadb.org/browse/MDEV-10429): sys\_vars.sysvars\_wsrep fails in buildbot on host 'work' (valgrind builder)
* [Revision #b522c71](https://github.com/MariaDB/server/commit/b522c71)\
  2016-07-22 19:00:49 -0400
  * [MDEV-10396](https://jira.mariadb.org/browse/MDEV-10396): MariaDB does not restart after upgrade on debian 8
* [Revision #a63ceae](https://github.com/MariaDB/server/commit/a63ceae)\
  2016-07-27 17:01:45 +0300
  * [MDEV-10389](https://jira.mariadb.org/browse/MDEV-10389): Query returns different results on a debug vs non-debug build
* [Revision #a52d3aa](https://github.com/MariaDB/server/commit/a52d3aa)\
  2016-06-22 11:17:44 +0200
  * [MDEV-10045](https://jira.mariadb.org/browse/MDEV-10045): Server crashes in Time\_and\_counter\_tracker::incr\_loops
* [Revision #e6a64e8](https://github.com/MariaDB/server/commit/e6a64e8)\
  2016-07-22 09:19:35 +1000
  * [MDEV-10294](https://jira.mariadb.org/browse/MDEV-10294): MTR using --valgrind-option to specify a tool / fixing callgrind \[10.1] (#200)
* [Revision #f038659](https://github.com/MariaDB/server/commit/f038659)\
  2016-07-19 20:44:02 +0000
  * [MDEV-10314](https://jira.mariadb.org/browse/MDEV-10314) : wsrep\_client\_thread was not set in threadpool.
* [Revision #9b668d7](https://github.com/MariaDB/server/commit/9b668d7)\
  2016-07-18 11:01:03 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
