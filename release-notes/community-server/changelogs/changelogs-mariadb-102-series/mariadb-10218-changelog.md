# MariaDB 10.2.18 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.18)[Release Notes](../../old-releases/10.2/10.2.18.md)[Changelog](mariadb-10218-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 25 Sep 2018

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.18.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #2dfb4a8abe](https://github.com/MariaDB/server/commit/2dfb4a8abe)\
  2018-09-25 02:45:40 +0300
  * Updated list of unstable tests for 10.2.18
* [Revision #339edd462f](https://github.com/MariaDB/server/commit/339edd462f)\
  2018-09-24 20:37:22 +0200
  * fixed auto-merge gone bad
* [Revision #dcbd51cee6](https://github.com/MariaDB/server/commit/dcbd51cee6)\
  2018-09-24 15:34:23 +0200
  * update libmariadb
* Merge [Revision #5ae8fce50b](https://github.com/MariaDB/server/commit/5ae8fce50b) 2018-09-23 20:26:35 +0200 - Merge branch '10.1' into 10.2
* Merge [Revision #1fc5a6f30c](https://github.com/MariaDB/server/commit/1fc5a6f30c) 2018-09-23 12:58:11 +0200 - Merge branch '10.0' into 10.1
* [Revision #1144acbcbd](https://github.com/MariaDB/server/commit/1144acbcbd)\
  2018-09-22 15:21:20 +0200
  * tokudb: create and destroy TOKUDB\_SHARE::\_open\_tables\_mutex dynamically
* [Revision #3a9276bad3](https://github.com/MariaDB/server/commit/3a9276bad3)\
  2018-09-22 15:19:40 +0200
  * sanitize tokudb locking macros
* Merge [Revision #a4131c51f5](https://github.com/MariaDB/server/commit/a4131c51f5) 2018-09-21 18:17:32 +0400 - Merge remote-tracking branch 'origin/5.5' into bb-10.0-bar
* [Revision #fc70f21e0a](https://github.com/MariaDB/server/commit/fc70f21e0a)\
  2018-09-21 18:04:56 +0400
  * Fixing the comment not to mention the removed class Item\_copy\_int.
* [Revision #b514a5f9e8](https://github.com/MariaDB/server/commit/b514a5f9e8)\
  2018-09-21 18:03:23 +0400
  * A cleanup for [MDEV-17249](https://jira.mariadb.org/browse/MDEV-17249) MAKETIME(-1e50,0,0) returns a wrong result
* Merge [Revision #acc97298e5](https://github.com/MariaDB/server/commit/acc97298e5) 2018-09-21 14:41:11 +0300 - Merge 5.5 into 10.0
* Merge [Revision #948e888097](https://github.com/MariaDB/server/commit/948e888097) 2018-09-21 12:02:52 +0300 - Pull request #868: [MDEV-17248](https://jira.mariadb.org/browse/MDEV-17248) Improve ASAN memory pool instrumentation
* [Revision #5b25dc6fa4](https://github.com/MariaDB/server/commit/5b25dc6fa4)\
  2018-09-19 22:01:00 +0300
  * [MDEV-17248](https://jira.mariadb.org/browse/MDEV-17248) Improve ASAN memory pool instrumentation
* [Revision #d533f6d58b](https://github.com/MariaDB/server/commit/d533f6d58b)\
  2018-09-21 09:32:17 +0400
  * After-merge cleanup: adjust the test to work in 10.0
* Merge [Revision #80bcb05b24](https://github.com/MariaDB/server/commit/80bcb05b24) 2018-09-21 08:37:42 +0400 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #e07118946a](https://github.com/MariaDB/server/commit/e07118946a)\
  2018-09-20 17:11:36 +0400
  * [MDEV-17250](https://jira.mariadb.org/browse/MDEV-17250) Remove unused Item\_copy\_xxx
* [Revision #935a163dd9](https://github.com/MariaDB/server/commit/935a163dd9)\
  2018-09-20 16:51:56 +0400
  * [MDEV-17244](https://jira.mariadb.org/browse/MDEV-17244) MAKETIME(900,0,0.111) returns a wrong result
* [Revision #0c6455aa46](https://github.com/MariaDB/server/commit/0c6455aa46)\
  2018-09-20 16:02:58 +0400
  * [MDEV-17249](https://jira.mariadb.org/browse/MDEV-17249) MAKETIME(-1e50,0,0) returns a wrong result
* [Revision #e43bc02e7b](https://github.com/MariaDB/server/commit/e43bc02e7b)\
  2018-07-16 15:35:16 +0300
  * [MDEV-16741](https://jira.mariadb.org/browse/MDEV-16741) Assertion `m_extra_cache` failed in ha\_partition::late\_extra\_cache
* [Revision #ff34436a2e](https://github.com/MariaDB/server/commit/ff34436a2e)\
  2018-08-03 13:04:43 +0200
  * Bug#27230925: HANDLE\_FATAL\_SIGNAL (SIG=11) IN SHOW\_ROUTINE\_GRANTS
* [Revision #14ddcb1ff2](https://github.com/MariaDB/server/commit/14ddcb1ff2)\
  2018-08-02 22:28:04 +0200
  * Bug#27407480: AUTOMATIC\_SP\_PRIVILEGES REQUIRES NEED THE INSERT PRIVILEGES FOR MYSQL.USER TABLE
* [Revision #327b271721](https://github.com/MariaDB/server/commit/327b271721)\
  2018-09-07 14:50:10 +0400
  * [MDEV-14410](https://jira.mariadb.org/browse/MDEV-14410) - Assertion failed in mark\_used\_tables\_as\_free\_for\_reuse
* [Revision #b7944343dd](https://github.com/MariaDB/server/commit/b7944343dd)\
  2018-09-10 14:26:11 +0200
  * Update contributors
* [Revision #87dc4e98dd](https://github.com/MariaDB/server/commit/87dc4e98dd)\
  2018-09-23 13:53:57 +0300
  * [MDEV-17276](https://jira.mariadb.org/browse/MDEV-17276): Adjust Galera tests after Galera library 25.3.24
* [Revision #eefaf4fdc9](https://github.com/MariaDB/server/commit/eefaf4fdc9)\
  2018-09-20 15:44:04 +0300
  * Adjust disabled Galera tests.
* [Revision #428669fa83](https://github.com/MariaDB/server/commit/428669fa83)\
  2018-09-20 06:51:40 +0300
  * [MDEV-15805](https://jira.mariadb.org/browse/MDEV-15805): Test failure on galera.query\_cache
* [Revision #3177d26627](https://github.com/MariaDB/server/commit/3177d26627)\
  2018-09-19 13:10:54 +0300
  * [MDEV-13873](https://jira.mariadb.org/browse/MDEV-13873): galera.galera\_suspend\_slave failed in buildbot with wrong error code
* [Revision #45712a9a1f](https://github.com/MariaDB/server/commit/45712a9a1f)\
  2018-09-19 12:19:30 +0300
  * [MDEV-13871](https://jira.mariadb.org/browse/MDEV-13871): galera.galera\_unicode\_identifiers failed in buildbot with 'Unknown database'
* [Revision #82524239c4](https://github.com/MariaDB/server/commit/82524239c4)\
  2018-09-19 11:42:43 +0300
  * [MDEV-17208](https://jira.mariadb.org/browse/MDEV-17208): Test failure on galera.MW-286
* [Revision #cd363fecbf](https://github.com/MariaDB/server/commit/cd363fecbf)\
  2018-09-19 01:24:46 -0700
  * Removed duplicate tests.
* [Revision #cc616bea53](https://github.com/MariaDB/server/commit/cc616bea53)\
  2018-09-17 18:18:19 +0300
  * Test galera.query\_cache is still failing on bb.
* [Revision #145c947b88](https://github.com/MariaDB/server/commit/145c947b88)\
  2018-09-17 12:03:41 +0300
  * [MDEV-17206](https://jira.mariadb.org/browse/MDEV-17206): Test failure on galera.galera\_ist\_\* in debug builds
* [Revision #dbf4e68704](https://github.com/MariaDB/server/commit/dbf4e68704)\
  2018-09-17 09:05:52 +0300
  * [MDEV-13879](https://jira.mariadb.org/browse/MDEV-13879): galera.galera\_wan fails in buildbot with Stray state UUID msg or with "Transport endpoint is not connected" or with a failure to start a node
* [Revision #6a31e86bbd](https://github.com/MariaDB/server/commit/6a31e86bbd)\
  2018-09-17 08:11:38 +0300
  * Adjust Galera disabled tests based on test results.
* [Revision #d3a8b5aa9c](https://github.com/MariaDB/server/commit/d3a8b5aa9c)\
  2018-09-14 13:10:48 +0300
  * [MDEV-14143](https://jira.mariadb.org/browse/MDEV-14143): galera.galera\_kill\_smallchanges, galera.galera\_kill\_ddl fail in buildbot with "Last Applied Action message in non-primary configuration from member 0"
* [Revision #c886368a3a](https://github.com/MariaDB/server/commit/c886368a3a)\
  2018-09-14 11:16:54 +0300
  * Test galera\_sst\_rsync\_data\_dir has different result on release and debug builds. Modified version for 10.1 from following commit:
* [Revision #ed7a0e5efc](https://github.com/MariaDB/server/commit/ed7a0e5efc)\
  2018-09-14 10:35:37 +0300
  * [MDEV-13876](https://jira.mariadb.org/browse/MDEV-13876): galera.MW-328A failed in buildbot with wrong result or timeout
* [Revision #6c47c1c456](https://github.com/MariaDB/server/commit/6c47c1c456)\
  2018-09-13 13:27:03 -0700
  * [MDEV-16912](https://jira.mariadb.org/browse/MDEV-16912): Spider Order By column\[datatime] limit 5 returns 3 rows
* [Revision #c9d6728c36](https://github.com/MariaDB/server/commit/c9d6728c36)\
  2018-09-13 11:15:22 +0200
  * try to fix version detection
* Merge [Revision #ec457c08d7](https://github.com/MariaDB/server/commit/ec457c08d7) 2018-09-13 08:29:41 +0300 - Merge pull request #865 from grooverdan/[MDEV-17173](https://jira.mariadb.org/browse/MDEV-17173)-wsrep\_sst
* [Revision #b96d36344e](https://github.com/MariaDB/server/commit/b96d36344e)\
  2018-09-13 09:58:50 +1000
  * [MDEV-17173](https://jira.mariadb.org/browse/MDEV-17173): correct parsing of 12.13.14.15:4444/xtrabackup\_sst leaving LSN/SST\_VER blank
* [Revision #6c7910ee22](https://github.com/MariaDB/server/commit/6c7910ee22)\
  2018-09-12 11:25:47 +0300
  * Fix test galera#505 galera library version check.
* [Revision #e63b84b916](https://github.com/MariaDB/server/commit/e63b84b916)\
  2018-09-09 21:07:46 +0300
  * [MDEV-17155](https://jira.mariadb.org/browse/MDEV-17155): Incorrect ORDER BY optimization: full index scan is used instead of range
* [Revision #038804d594](https://github.com/MariaDB/server/commit/038804d594)\
  2018-09-12 14:56:48 +0300
  * Update disabled Galera tests.
* [Revision #794e89ed3f](https://github.com/MariaDB/server/commit/794e89ed3f)\
  2018-09-12 14:54:59 +0300
  * [MDEV-17108](https://jira.mariadb.org/browse/MDEV-17108): Test failure on galera.galera\_kill\_ddl
* [Revision #c76ee73dc7](https://github.com/MariaDB/server/commit/c76ee73dc7)\
  2018-09-12 13:32:14 +0300
  * [MDEV-13743](https://jira.mariadb.org/browse/MDEV-13743): galera\_toi\_truncate may fail with: query 'reap' succeeded - should have failed with errno 1213
* [Revision #16384fae63](https://github.com/MariaDB/server/commit/16384fae63)\
  2018-08-29 16:45:28 +0200
  * [MDEV-15845](https://jira.mariadb.org/browse/MDEV-15845) Test failure on galera.galera\_concurrent\_ctas
* [Revision #e46b2a3e94](https://github.com/MariaDB/server/commit/e46b2a3e94)\
  2018-09-11 20:59:35 +0100
  * [MDEV-12956](https://jira.mariadb.org/browse/MDEV-12956) provide default datadir for mariadb-backup --copy-back
* [Revision #21829bd743](https://github.com/MariaDB/server/commit/21829bd743)\
  2018-09-11 08:19:16 +0300
  * [MDEV-17106](https://jira.mariadb.org/browse/MDEV-17106): Test failure on galera.galera\_binlog\_stmt\_autoinc
* [Revision #bdaace9b30](https://github.com/MariaDB/server/commit/bdaace9b30)\
  2018-09-10 13:43:37 +0300
  * [MDEV-17151](https://jira.mariadb.org/browse/MDEV-17151): Galera test failure on galera.galera\_var\_node\_address
* [Revision #c1f308054d](https://github.com/MariaDB/server/commit/c1f308054d)\
  2018-09-08 16:57:31 +0300
  * [MDEV-17143](https://jira.mariadb.org/browse/MDEV-17143): Galera test failure on galera.MW-44
* [Revision #76098f45b8](https://github.com/MariaDB/server/commit/76098f45b8)\
  2018-09-22 22:46:45 +0200
  * RocksDB: workaround a compiler error on ppc64le
* [Revision #2b45eb77f7](https://github.com/MariaDB/server/commit/2b45eb77f7)\
  2018-09-23 13:41:08 +0300
  * [MDEV-17261](https://jira.mariadb.org/browse/MDEV-17261): sysbench oltp read only too slow for MyRocks
* [Revision #61a6f4bd96](https://github.com/MariaDB/server/commit/61a6f4bd96)\
  2018-09-21 20:38:14 +0200
  * [MDEV-14560](https://jira.mariadb.org/browse/MDEV-14560) Extra engines enabled through additional config are not loaded on first installation
* [Revision #e7d152293d](https://github.com/MariaDB/server/commit/e7d152293d)\
  2018-09-21 20:16:36 +0200
  * [MDEV-13089](https://jira.mariadb.org/browse/MDEV-13089) identifier quoting in partitioning
* [Revision #e4b466aa3d](https://github.com/MariaDB/server/commit/e4b466aa3d)\
  2018-09-21 19:56:55 +0200
  * [MDEV-16792](https://jira.mariadb.org/browse/MDEV-16792) Assertion `m_status == DA_ERROR` failed in Diagnostics\_area::sql\_errno or wrong result upon SHOW TABLE STATUS after adding partition under ANSI\_QUOTES
* [Revision #1ebec10375](https://github.com/MariaDB/server/commit/1ebec10375)\
  2018-09-11 10:28:14 +0200
  * InnoDB: fix compilation with -DDBUG\_OFF
* [Revision #21d157abaa](https://github.com/MariaDB/server/commit/21d157abaa)\
  2018-09-08 19:42:53 +0200
  * [MDEV-14560](https://jira.mariadb.org/browse/MDEV-14560) Extra engines enabled through additional config are not loaded on first installation
* [Revision #5c83305c4c](https://github.com/MariaDB/server/commit/5c83305c4c)\
  2018-09-08 19:45:39 +0200
  * RPM: generate per-plugin.cnf files where git will ignore them
* [Revision #8b6b2c3ea1](https://github.com/MariaDB/server/commit/8b6b2c3ea1)\
  2018-09-21 11:18:59 +0300
  * Fix mariadb-backup leaks (except my\_load\_defaults)
* [Revision #82675100d1](https://github.com/MariaDB/server/commit/82675100d1)\
  2018-09-21 10:24:15 +0300
  * Remove an unused variable
* [Revision #c139dc6d38](https://github.com/MariaDB/server/commit/c139dc6d38)\
  2018-09-20 19:27:59 +0100
  * Windows : Fix application verifier errors.
* [Revision #0fa35ddf1f](https://github.com/MariaDB/server/commit/0fa35ddf1f)\
  2018-09-20 14:08:57 +0100
  * Amend fix for [MDEV-17236](https://jira.mariadb.org/browse/MDEV-17236)
* [Revision #7e4bbd3aa6](https://github.com/MariaDB/server/commit/7e4bbd3aa6)\
  2018-09-20 17:13:12 +0530
  * [MDEV-17236](https://jira.mariadb.org/browse/MDEV-17236) mariadb-backup incorrectly tries to open ibdata1 if custom undo tablespace is defined
* [Revision #654b587999](https://github.com/MariaDB/server/commit/654b587999)\
  2018-09-19 11:33:22 +0300
  * [MDEV-17208](https://jira.mariadb.org/browse/MDEV-17208): Test failure on galera.MW-286
* [Revision #4a026596f5](https://github.com/MariaDB/server/commit/4a026596f5)\
  2018-09-18 21:30:03 +0100
  * [MDEV-15088](https://jira.mariadb.org/browse/MDEV-15088) Lighter version of Windows Zip distributions
* Merge [Revision #09f8941a91](https://github.com/MariaDB/server/commit/09f8941a91) 2018-09-18 09:05:26 +0100 - Merge branch 'bb-10.2-wlad-release' into 10.2
* [Revision #f0ee8496d2](https://github.com/MariaDB/server/commit/f0ee8496d2)\
  2018-09-14 18:53:27 +0100
  * [MDEV-15088](https://jira.mariadb.org/browse/MDEV-15088) Lighter version of Windows Zip distributions
* [Revision #6858d5346c](https://github.com/MariaDB/server/commit/6858d5346c)\
  2018-09-17 23:15:56 -0700
  * [MDEV-17201](https://jira.mariadb.org/browse/MDEV-17201) dropped anchor rows with non-null recursion query
* [Revision #65474d92f5](https://github.com/MariaDB/server/commit/65474d92f5)\
  2018-09-17 09:53:49 +0300
  * Follow-up to "Fixed wrong printf in mariadb-backup"
* [Revision #4fa9eaf454](https://github.com/MariaDB/server/commit/4fa9eaf454)\
  2018-09-17 08:49:02 +0300
  * Remove unused ha\_innobase::lock
* [Revision #bd7c31621f](https://github.com/MariaDB/server/commit/bd7c31621f)\
  2018-09-16 11:22:32 +0300
  * [MDEV-17065](https://jira.mariadb.org/browse/MDEV-17065) Crash on SHOW CREATE TABLE with CHECK CONSTRAINT
* [Revision #4dc20ff687](https://github.com/MariaDB/server/commit/4dc20ff687)\
  2018-09-16 11:20:07 +0300
  * Fixed wrong printf in mariadb-backup
* [Revision #e89b611dc9](https://github.com/MariaDB/server/commit/e89b611dc9)\
  2018-09-16 10:22:32 +0400
  * [MDEV-16050](https://jira.mariadb.org/browse/MDEV-16050) cte + geometry functions lead to crash.
* [Revision #7419f72b71](https://github.com/MariaDB/server/commit/7419f72b71)\
  2018-09-15 15:43:08 -0700
  * Fixed a compiler warning.
* [Revision #7c76f8aa3a](https://github.com/MariaDB/server/commit/7c76f8aa3a)\
  2018-09-15 21:54:22 +0300
  * Disable incompatible tests
* [Revision #3473e0452e](https://github.com/MariaDB/server/commit/3473e0452e)\
  2018-09-13 00:35:28 -0700
  * [MDEV-17154](https://jira.mariadb.org/browse/MDEV-17154) Multiple selects from parametrized CTE fails with syntax error
* [Revision #6b2da93359](https://github.com/MariaDB/server/commit/6b2da93359)\
  2018-09-14 09:35:18 +0100
  * [MDEV-17192](https://jira.mariadb.org/browse/MDEV-17192) Backup with -no-lock should fail, if DDL is detected at the end of backup
* Merge [Revision #28f08d3753](https://github.com/MariaDB/server/commit/28f08d3753) 2018-09-14 08:47:22 +0200 - Merge branch '10.1' into 10.2
* [Revision #f1bcfbb437](https://github.com/MariaDB/server/commit/f1bcfbb437)\
  2018-09-08 11:34:22 -0400
  * bump the VERSION
* [Revision #f01c4a10d7](https://github.com/MariaDB/server/commit/f01c4a10d7)\
  2018-09-08 08:12:55 +0300
  * Add one more wait for truncate in MW-44.
* Merge [Revision #908ac40bdb](https://github.com/MariaDB/server/commit/908ac40bdb) 2018-09-07 20:24:49 +0200 - Merge branch 'bb-10.1-release' into 10.1
* [Revision #0254be96f7](https://github.com/MariaDB/server/commit/0254be96f7)\
  2018-09-07 15:43:03 +0200
  * remove doubly-installed file
* [Revision #edb3a32c6c](https://github.com/MariaDB/server/commit/edb3a32c6c)\
  2018-09-06 14:16:09 +0300
  * [MDEV-17143](https://jira.mariadb.org/browse/MDEV-17143): Galera test failure on galera.MW-44
* Merge [Revision #3866589308](https://github.com/MariaDB/server/commit/3866589308) 2018-09-13 11:41:55 -0700 - [MDEV-16912](https://jira.mariadb.org/browse/MDEV-16912): Spider Order By column\[datatime] limit 5 returns 3 rows
* [Revision #eb2ca3d445](https://github.com/MariaDB/server/commit/eb2ca3d445)\
  2018-09-11 16:29:44 -0700
  * [MDEV-16912](https://jira.mariadb.org/browse/MDEV-16912): Spider Order By column\[datatime] limit 5 returns 3 rows
* [Revision #8e68876477](https://github.com/MariaDB/server/commit/8e68876477)\
  2018-09-13 15:06:44 +0200
  * Fix of the test which has debug version
* [Revision #d85a7220dc](https://github.com/MariaDB/server/commit/d85a7220dc)\
  2018-09-13 14:59:12 +0300
  * [MDEV-17188](https://jira.mariadb.org/browse/MDEV-17188): rocksdb.2pc\_group\_commit fails intermittently in BB
* [Revision #f54485eadb](https://github.com/MariaDB/server/commit/f54485eadb)\
  2018-09-13 13:42:09 +0400
  * [MDEV-17001](https://jira.mariadb.org/browse/MDEV-17001) JSON\_MERGE returns nullwhen merging empty array.
* Merge [Revision #2b46dca5d7](https://github.com/MariaDB/server/commit/2b46dca5d7) 2018-09-13 10:09:28 +0200 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #dbf25197c1](https://github.com/MariaDB/server/commit/dbf25197c1)\
  2018-08-08 12:20:26 +0200
  * Comment out failing Cyrillic test in xml2.test
* [Revision #b291daaccd](https://github.com/MariaDB/server/commit/b291daaccd)\
  2018-08-07 19:46:11 +0200
  * Delete an assert(qrp) from JCATPARM \*AllocCatInfo that is called with qrp=NULL from JDBConn::SetUUID. Also delete a clone of this function that was duplicated in javaconn.cpp.
* [Revision #a93363022c](https://github.com/MariaDB/server/commit/a93363022c)\
  2018-09-12 21:57:28 +0400
  * [MDEV-17018](https://jira.mariadb.org/browse/MDEV-17018) JSON\_SEARCH and User-Defined Variables.
* [Revision #c3124174c3](https://github.com/MariaDB/server/commit/c3124174c3)\
  2018-09-11 15:23:58 +0100
  * [MDEV-17168](https://jira.mariadb.org/browse/MDEV-17168) mariadb-backup reports "failed to open bitmap directory"
* [Revision #c8bb43a938](https://github.com/MariaDB/server/commit/c8bb43a938)\
  2018-09-11 14:37:45 +0400
  * [MDEV-17121](https://jira.mariadb.org/browse/MDEV-17121) JSON\_ARRAY\_APPEND.
* [Revision #4d9ec7cb6c](https://github.com/MariaDB/server/commit/4d9ec7cb6c)\
  2018-08-31 14:15:09 +0200
  * [MDEV-16052](https://jira.mariadb.org/browse/MDEV-16052) galera mtr galera\_certification\_double\_failure fails with deadlock
* [Revision #e76c4c06f1](https://github.com/MariaDB/server/commit/e76c4c06f1)\
  2018-09-05 14:44:07 +0400
  * [MDEV-16773](https://jira.mariadb.org/browse/MDEV-16773) - Assertion failed in tdc\_remove\_table
* [Revision #4d991abd4f](https://github.com/MariaDB/server/commit/4d991abd4f)\
  2018-09-07 20:10:04 -0700
  * [MDEV-17024](https://jira.mariadb.org/browse/MDEV-17024) Crash on large query
* [Revision #59950df533](https://github.com/MariaDB/server/commit/59950df533)\
  2018-08-29 12:14:55 +0300
  * Remove some debug-only global status variables
* [Revision #0927332961](https://github.com/MariaDB/server/commit/0927332961)\
  2018-08-28 17:14:54 +0300
  * Make some declarations private
* [Revision #93ed717b3d](https://github.com/MariaDB/server/commit/93ed717b3d)\
  2018-08-28 16:48:19 +0300
  * Relax debug assertions for undo tablespace recovery
* [Revision #9f6a0d291f](https://github.com/MariaDB/server/commit/9f6a0d291f)\
  2018-08-28 13:19:26 +0300
  * row\_purge\_parse\_undo\_rec(): Deduplicate some code
* [Revision #68466bb485](https://github.com/MariaDB/server/commit/68466bb485)\
  2018-08-28 13:18:31 +0300
  * innobase\_init(): Remove an unnecessary condition
* [Revision #58389c71c2](https://github.com/MariaDB/server/commit/58389c71c2)\
  2018-09-07 18:18:14 +0100
  * [MDEV-16671](https://jira.mariadb.org/browse/MDEV-16671) - crash in mariadb-backup with my.cnf with plugin-load=ha\_rocksdb
* Merge [Revision #727324c1e9](https://github.com/MariaDB/server/commit/727324c1e9) 2018-09-07 01:14:19 +0200 - Merge tag 'mariadb-10.2.17' into 10.2
* [Revision #a0631e7221](https://github.com/MariaDB/server/commit/a0631e7221)\
  2018-09-06 15:31:29 +0100
  * [MDEV-17149](https://jira.mariadb.org/browse/MDEV-17149) mariadb-backup hangs if innodb is not started
* [Revision #67b87e1d76](https://github.com/MariaDB/server/commit/67b87e1d76)\
  2018-09-05 19:32:31 +0100
  * Rocksdb, Windows - better fix for broken WIN32\_LEAN\_AND\_MEAN
* [Revision #2676f3371c](https://github.com/MariaDB/server/commit/2676f3371c)\
  2018-09-03 12:19:16 +0300
  * Post-merge fixes: Disable rpl\_mts\_dependency\_unique\_key\_conflicts test
* Merge [Revision #08d0a2a8cf](https://github.com/MariaDB/server/commit/08d0a2a8cf) 2018-09-01 18:43:05 +0300 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mariarocks-merge
* [Revision #6aa9219ae4](https://github.com/MariaDB/server/commit/6aa9219ae4)\
  2018-08-31 18:10:55 +0300
  * Remove a reference to a non-existing test
* [Revision #4ea74a2dae](https://github.com/MariaDB/server/commit/4ea74a2dae)\
  2018-08-31 18:09:30 +0300
  * After-merge fix: Rename tokudb\_logdump to tokudb\_logprint
* [Revision #186eb2c0e0](https://github.com/MariaDB/server/commit/186eb2c0e0)\
  2018-09-01 15:06:16 +0300
  * Fix BB failure: file INSTALL cannot find ... man/tokuft\_logdump.1.
* Merge [Revision #865831c683](https://github.com/MariaDB/server/commit/865831c683) 2018-08-31 16:36:27 +0300 - Merge branch 'bb-10.2-mariarocks-merge' into 10.2
* [Revision #52e0dee037](https://github.com/MariaDB/server/commit/52e0dee037)\
  2018-08-31 16:30:21 +0300
  * MyRocks: post-merge fixes: disable rocksdb.use\_direct\_reads
* [Revision #a55309d926](https://github.com/MariaDB/server/commit/a55309d926)\
  2018-08-31 13:21:46 +0300
  * MyRocks: post-merge fixes: Make it compile on Windows.
* [Revision #2770eb1b56](https://github.com/MariaDB/server/commit/2770eb1b56)\
  2018-08-30 22:30:26 +0300
  * MyRocks: post-merge fixes part #10: disable rocksdb.percona\_nonflushing\_analyze\_debug
* [Revision #9793398142](https://github.com/MariaDB/server/commit/9793398142)\
  2018-08-30 22:16:16 +0300
  * MyRocks: post-merge fixes part #9: disable rocksdb\_rpl.rpl\_missing\_columns\_sk\_update
* [Revision #206aba5910](https://github.com/MariaDB/server/commit/206aba5910)\
  2018-08-30 21:30:40 +0300
  * MyRocks: post-merge fixes part #8: make rocksdb.validate\_datadic test pass
* [Revision #d4f3c5c42f](https://github.com/MariaDB/server/commit/d4f3c5c42f)\
  2018-08-30 21:18:53 +0300
  * MyRocks: post-merge fixes part #7: make rocksdb.check\_ignore\_unknown\_options test pass
* [Revision #290368e740](https://github.com/MariaDB/server/commit/290368e740)\
  2018-08-30 12:55:03 +0300
  * MyRocks: post-merge fixes part #6: make rocksdb.allow\_no\_primary\_key test pass
* [Revision #5e4f3af9b7](https://github.com/MariaDB/server/commit/5e4f3af9b7)\
  2018-08-29 17:25:58 +0300
  * MyRocks: post-merge fixes part #5: make rocksdb.rocksdb\_checksums test pass
* [Revision #3d2c0f61e7](https://github.com/MariaDB/server/commit/3d2c0f61e7)\
  2018-08-28 17:35:52 +0300
  * MyRocks: Post-merge testcase fixes part #4
* [Revision #138605c3b7](https://github.com/MariaDB/server/commit/138605c3b7)\
  2018-08-28 16:30:22 +0300
  * MyRocks: Post-merge testcase fixes part #3
* [Revision #f561e63fdd](https://github.com/MariaDB/server/commit/f561e63fdd)\
  2018-08-28 16:18:02 +0300
  * MyRocks: Post-merge testcase fixes part #2
* [Revision #a01823a33f](https://github.com/MariaDB/server/commit/a01823a33f)\
  2018-08-28 12:43:00 +0000
  * MyRocks: Post-merge testcase fixes part #1
* Merge [Revision #c930afd47e](https://github.com/MariaDB/server/commit/c930afd47e) 2018-08-28 14:09:04 +0300 - Merge branch 'merge-myrocks' of github.com:MariaDB/mergetrees into bb-10.2-mariarocks-merge
* [Revision #faa4d8f8c6](https://github.com/MariaDB/server/commit/faa4d8f8c6)\
  2018-08-28 08:23:44 +0000
  * Copy of commit de1e8c7bfe7c875ea284b55040e8f3cd3a56fcc2 Author: Abhinav Sharma [abhinavsharma@fb.com](mailto:abhinavsharma@fb.com) Date: Thu Aug 23 14:34:39 2018 -0700
* [Revision #c8a3c2bc96](https://github.com/MariaDB/server/commit/c8a3c2bc96)\
  2018-08-31 15:30:44 +0300
  * Disable failing Galera tests.
* Merge [Revision #206528f722](https://github.com/MariaDB/server/commit/206528f722) 2018-08-31 13:47:48 +0300 - Merge 10.1 into 10.2
* [Revision #b245023fe0](https://github.com/MariaDB/server/commit/b245023fe0)\
  2018-08-30 00:51:39 -0700
  * [MDEV-16992](https://jira.mariadb.org/browse/MDEV-16992) Assertion `table_ref->table || table_ref->view` failed in Field\_iterator\_table\_ref::set\_field\_iterator
* [Revision #a8bf27c715](https://github.com/MariaDB/server/commit/a8bf27c715)\
  2018-08-09 14:15:58 +0200
  * [MDEV-14927](https://jira.mariadb.org/browse/MDEV-14927): Missing man pages
* [Revision #55163ba1bd](https://github.com/MariaDB/server/commit/55163ba1bd)\
  2018-08-01 20:44:59 +0300
  * [MDEV-16803](https://jira.mariadb.org/browse/MDEV-16803): Pushdown Item\_func\_in item that uses vectors in several SELECTs
* [Revision #2b76f6f61d](https://github.com/MariaDB/server/commit/2b76f6f61d)\
  2018-08-16 10:28:29 -0700
  * [MDEV-16703](https://jira.mariadb.org/browse/MDEV-16703): Update AUTO\_INCREMENT in the UPDATE statement
* [Revision #2a361ebe1b](https://github.com/MariaDB/server/commit/2a361ebe1b)\
  2018-03-17 01:22:53 +0800
  * [MDEV-15204](https://jira.mariadb.org/browse/MDEV-15204): lag/lead function order list mandatory
* [Revision #c826b6b8da](https://github.com/MariaDB/server/commit/c826b6b8da)\
  2018-08-24 20:53:00 -0700
  * Added a new parameter for the function eq\_ranges\_exceeds\_limit() introduced in the patch fo [MDEV-16934](https://jira.mariadb.org/browse/MDEV-16934).
* Merge [Revision #8b949d961c](https://github.com/MariaDB/server/commit/8b949d961c) 2018-08-24 15:11:43 +0300 - [MDEV-15511](https://jira.mariadb.org/browse/MDEV-15511) Use stunnel during rsync SST if available
* [Revision #4c652fc62e](https://github.com/MariaDB/server/commit/4c652fc62e)\
  2018-02-12 22:08:57 +0100
  * Use stunnel during rsync SST if available
* [Revision #1b4c5b7327](https://github.com/MariaDB/server/commit/1b4c5b7327)\
  2018-08-24 09:38:52 +0300
  * [MDEV-16868](https://jira.mariadb.org/browse/MDEV-16868) Same query gives different results
* [Revision #c164d0cc62](https://github.com/MariaDB/server/commit/c164d0cc62)\
  2018-08-23 17:02:50 +0300
  * fil\_name\_process(): Remove unused return value
* [Revision #9a815401c6](https://github.com/MariaDB/server/commit/9a815401c6)\
  2018-08-23 13:11:11 +0300
  * [MDEV-17043](https://jira.mariadb.org/browse/MDEV-17043) Purge of indexed virtual columns may cause hang on table-rebuilding DDL
* [Revision #5d650d366d](https://github.com/MariaDB/server/commit/5d650d366d)\
  2018-08-22 22:06:40 +0200
  * [MDEV-16961](https://jira.mariadb.org/browse/MDEV-16961) Assertion failed upon concurrent DELETE and DDL with virtual blob column
* [Revision #b0ef1b388b](https://github.com/MariaDB/server/commit/b0ef1b388b)\
  2018-08-21 16:52:59 +0300
  * After-merge fix: Revert [MDEV-15511](https://jira.mariadb.org/browse/MDEV-15511)
* Merge [Revision #9258097fa3](https://github.com/MariaDB/server/commit/9258097fa3) 2018-08-21 15:20:34 +0300 - Merge 10.1 into 10.2
* Merge [Revision #cdc8debcaa](https://github.com/MariaDB/server/commit/cdc8debcaa) 2018-08-21 12:10:21 +0300 - [MDEV-16557](https://jira.mariadb.org/browse/MDEV-16557) Remove INNOBASE\_SHARE
* [Revision #1a7a018939](https://github.com/MariaDB/server/commit/1a7a018939)\
  2018-07-18 14:57:27 +0300
  * [MDEV-16557](https://jira.mariadb.org/browse/MDEV-16557) Remove INNOBASE\_SHARE::idx\_trans\_tbl
* [Revision #cccdb176a6](https://github.com/MariaDB/server/commit/cccdb176a6)\
  2018-08-21 08:54:21 +0300
  * [MDEV-16862](https://jira.mariadb.org/browse/MDEV-16862) build failure for WITH\_INNODB\_AHI=0
* [Revision #0de3c423cc](https://github.com/MariaDB/server/commit/0de3c423cc)\
  2018-08-20 17:42:49 +0300
  * [MDEV-16765](https://jira.mariadb.org/browse/MDEV-16765): Missing rows with pushdown condition defined with CASE using Item\_cond
* [Revision #862a97749d](https://github.com/MariaDB/server/commit/862a97749d)\
  2018-08-17 19:29:01 -0700
  * [MDEV-17011](https://jira.mariadb.org/browse/MDEV-17011) “condition\_pushdown\_for\_derived” optimization not used when using INSERT INTO
* [Revision #4eac5df3fc](https://github.com/MariaDB/server/commit/4eac5df3fc)\
  2018-08-17 14:27:42 -0700
  * [MDEV-16934](https://jira.mariadb.org/browse/MDEV-16934) Query with very large IN clause lists runs slowly
* [Revision #d6f7fd6016](https://github.com/MariaDB/server/commit/d6f7fd6016)\
  2018-08-16 16:10:18 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Refuse MLOG\_TRUNCATE in mariadb-backup
* [Revision #1b49c89429](https://github.com/MariaDB/server/commit/1b49c89429)\
  2018-08-16 15:29:40 +0300
  * Re-enable the test mariadb-backup.unsupported\_redo
* [Revision #f926c5f4fa](https://github.com/MariaDB/server/commit/f926c5f4fa)\
  2018-08-16 08:37:54 +0100
  * [MDEV-16996](https://jira.mariadb.org/browse/MDEV-16996) mariadb-backup --prepare does not use native AIO on Linux by default
* [Revision #05153a670d](https://github.com/MariaDB/server/commit/05153a670d)\
  2018-08-16 06:35:28 +0300
  * Report all redo log corruption
* [Revision #a0ce321627](https://github.com/MariaDB/server/commit/a0ce321627)\
  2018-08-15 18:45:15 +0300
  * [MDEV-16136](https://jira.mariadb.org/browse/MDEV-16136) Various ASAN failures after [MDEV-15030](https://jira.mariadb.org/browse/MDEV-15030)
* [Revision #fa2a74e08d](https://github.com/MariaDB/server/commit/fa2a74e08d)\
  2018-08-13 13:32:05 +0300
  * [MDEV-16136](https://jira.mariadb.org/browse/MDEV-16136): Prevent wrong reuse in trx\_reference()
* [Revision #6583506570](https://github.com/MariaDB/server/commit/6583506570)\
  2018-08-13 12:34:12 +0300
  * Rename lock\_pool\_t to lock\_list
* [Revision #3ce8a0fc49](https://github.com/MariaDB/server/commit/3ce8a0fc49)\
  2018-08-13 11:46:22 +0300
  * [MDEV-16136](https://jira.mariadb.org/browse/MDEV-16136): Simplify trx\_lock\_t memory management
* [Revision #b795134802](https://github.com/MariaDB/server/commit/b795134802)\
  2018-08-14 18:58:41 +0200
  * [MDEV-16859](https://jira.mariadb.org/browse/MDEV-16859) MyRocks: support SSE42 CRC32-C instruction.
* [Revision #964ad0c426](https://github.com/MariaDB/server/commit/964ad0c426)\
  2018-08-14 12:32:44 -0400
  * bump the VERSION
* [Revision #922e7badfc](https://github.com/MariaDB/server/commit/922e7badfc)\
  2018-08-09 15:06:52 +0100
  * [MDEV-16791](https://jira.mariadb.org/browse/MDEV-16791) mariadb-backup : Support DDL commands during backup
* [Revision #9a4998a35a](https://github.com/MariaDB/server/commit/9a4998a35a)\
  2018-08-13 23:42:20 +0100
  * adjust result file
* [Revision #1faaaa9718](https://github.com/MariaDB/server/commit/1faaaa9718)\
  2018-08-13 22:39:31 +0100
  * [MDEV-15680](https://jira.mariadb.org/browse/MDEV-15680) xb\_aws\_key\_management fails in buildbot.
* [Revision #562dd53c29](https://github.com/MariaDB/server/commit/562dd53c29)\
  2018-08-13 18:56:52 +0300
  * [MDEV-16575](https://jira.mariadb.org/browse/MDEV-16575): rocksdb.bulk\_load\_errors fails in buildbot with wrong result
* [Revision #ba10ffe0f4](https://github.com/MariaDB/server/commit/ba10ffe0f4)\
  2018-08-12 22:10:32 +0300
  * [MDEV-16203](https://jira.mariadb.org/browse/MDEV-16203): autoinc\_debug of rocksdb test suite fails
* [Revision #9dd3e5ea3c](https://github.com/MariaDB/server/commit/9dd3e5ea3c)\
  2018-08-06 22:30:14 +0300
  * Deb: Make libmariadb3 Breaks+Replaces libmariadbclient18 so upgrade pass
* [Revision #29150e2391](https://github.com/MariaDB/server/commit/29150e2391)\
  2018-08-10 17:01:53 +0300
  * Revert part of b853b4fd88b441f36eeb7eabdce79918ef10538a
* [Revision #b853b4fd88](https://github.com/MariaDB/server/commit/b853b4fd88)\
  2018-08-10 13:02:01 +0300
  * Report InnoDB redo log corruption better
* [Revision #0e15ae1602](https://github.com/MariaDB/server/commit/0e15ae1602)\
  2018-08-10 10:00:47 +0300
  * recv\_report\_corrupt\_log(): Avoid buffer overflow
* [Revision #bdf50c3ebd](https://github.com/MariaDB/server/commit/bdf50c3ebd)\
  2018-08-09 19:42:46 +0300
  * log\_group\_read\_log\_seg(): Validate the length

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
