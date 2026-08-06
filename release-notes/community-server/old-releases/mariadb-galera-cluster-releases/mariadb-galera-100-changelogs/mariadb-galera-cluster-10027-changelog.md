# MariaDB Galera Cluster 10.0.27 Changelog

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.27)[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10027-release-notes.md)[Changelog](mariadb-galera-cluster-10027-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 29 Aug 2016

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10027-release-notes.md).\
For changes made in MariaDB, see the [MariaDB 10.0.27 Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10027-changelog.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code
modified in that revision.

* [Revision #16702ec](https://github.com/MariaDB/server/commit/16702ec)\
  2016-08-25 21:19:25 -0400
  * Record wsrep.variables test result (with non-debug galera library).
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
  * Refs: MW-279 - fixes in innodb to skip wsrep processing (like kill victim) when running in native mysql mode
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
  * refs: MW-279 - At startup time global wsrep\_on is set too late and some wsrep paths may be executed because of this. e.g. replication slave restart could happen before wsrep\_on state is defined.
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
  * Refs MW-255
    * popping PS reprepare observer before BF aborted PS replaying begins dangling observer will cause failure in open\_table() ater on
    * test case for this anomaly
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
  * Refs MW-252 - enveloped FTWRL processing with wsrep desync/resync calls. This way FTWRL processing node will not cause flow control to kick in
    * donor servicing thread is unfortunate exception, we must let him to pause provider as part of FTWRL phase, but not desync/resync as this is done as part of donor control on higher level
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
  * refs codership/mysql-wsrep#239 Synced xtrabackup SST scripts from PXC source tree as of PXC 5.6.27-25.13
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

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
