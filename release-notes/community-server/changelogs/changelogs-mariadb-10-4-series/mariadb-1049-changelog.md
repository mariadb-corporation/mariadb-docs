# MariaDB 10.4.9 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

After an upgrade MariaDB Server can crash if InnoDB tables exist with a `FULLTEXT INDEX` and a `FOREIGN KEY` constraint attached to them. We got reports that the crash already will be encountered on startup, but a crash is also possible at a later stage. See [MDEV-20987](https://jira.mariadb.org/browse/MDEV-20987) for more details.**Do not download or use this release.**

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.4/10.4.9.md)[Changelog](mariadb-1049-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.4.9/)

**Release date:** 5 Nov 2019

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.9.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.19](../changelogs-mariadb-10-3-series/mariadb-10319-changelog.md)
* [Revision #0339cbe2f6](https://github.com/MariaDB/server/commit/0339cbe2f6)\
  2019-11-03 20:41:47 +0200
  * List of unstable tests for 10.4.9 release
* [Revision #903f5fea30](https://github.com/MariaDB/server/commit/903f5fea30)\
  2019-11-02 18:54:01 +0100
  * Revert "wolfssl 4.2.0" (it is not ready jet)
* [Revision #dacd1794e4](https://github.com/MariaDB/server/commit/dacd1794e4)\
  2019-11-02 12:11:39 +0100
  * wolfssl 4.2.0
* [Revision #6818f40adf](https://github.com/MariaDB/server/commit/6818f40adf)\
  2019-11-02 08:40:43 +0100
  * Postmerge fix of rocksdb test results
* Merge [Revision #f566889a79](https://github.com/MariaDB/server/commit/f566889a79) 2019-11-01 20:01:44 +0100 - Merge branch '10.3' into 10.4
* Merge [Revision #ec40980ddd](https://github.com/MariaDB/server/commit/ec40980ddd) 2019-11-01 15:23:18 +0200 - Merge 10.3 into 10.4
* [Revision #6801f80afa](https://github.com/MariaDB/server/commit/6801f80afa)\
  2019-11-01 14:28:33 +0200
  * [MDEV-19457](https://jira.mariadb.org/browse/MDEV-19457) sys\_vars.wsrep\_provider\_basic failed
* [Revision #366f4f299e](https://github.com/MariaDB/server/commit/366f4f299e)\
  2019-10-30 17:41:39 +0200
  * Fix that BACKUP STAGE BLOCK\_COMMIT flushes binary log
* [Revision #fcd65b0376](https://github.com/MariaDB/server/commit/fcd65b0376)\
  2019-10-31 19:44:29 +0300
  * [MDEV-17171](https://jira.mariadb.org/browse/MDEV-17171): RocksDB Tables do not have "Creation Date"
* [Revision #eafc9d8516](https://github.com/MariaDB/server/commit/eafc9d8516)\
  2019-10-30 10:18:09 +0300
  * [MDEV-17171](https://jira.mariadb.org/browse/MDEV-17171): RocksDB Tables do not have "Creation Date"
* [Revision #ad8266a5c2](https://github.com/MariaDB/server/commit/ad8266a5c2)\
  2019-10-09 03:13:13 -0500
  * [MDEV-20732](https://jira.mariadb.org/browse/MDEV-20732) MDB now correctly estimates a length of the FORMAT() result for doubles in scientific notation with a big integer part.
* [Revision #6535827885](https://github.com/MariaDB/server/commit/6535827885)\
  2019-10-30 15:24:00 +0100
  * [MDEV-19516](https://jira.mariadb.org/browse/MDEV-19516) mysql\_secure\_installation doesn't set password\_last\_changed while setting password for root
* [Revision #f4ba775914](https://github.com/MariaDB/server/commit/f4ba775914)\
  2019-10-30 09:45:22 +0100
  * [MDEV-17099](https://jira.mariadb.org/browse/MDEV-17099) Preliminary changes for Galera XA support (#1404)
* [Revision #576c96a938](https://github.com/MariaDB/server/commit/576c96a938)\
  2019-10-29 19:10:52 +0200
  * [MDEV-20917](https://jira.mariadb.org/browse/MDEV-20917): Fix dict\_table\_t::instant\_column()
* [Revision #d4e1fa39f0](https://github.com/MariaDB/server/commit/d4e1fa39f0)\
  2019-10-29 11:58:11 +0200
  * Use C++11 "range for" in crash recovery code
* [Revision #dadc53ff0b](https://github.com/MariaDB/server/commit/dadc53ff0b)\
  2019-10-26 10:43:10 +0200
  * [MDEV-19882](https://jira.mariadb.org/browse/MDEV-19882) pam v2: auth\_pam\_tool truncates passwords that are not null-terminated
* [Revision #d67ea8151f](https://github.com/MariaDB/server/commit/d67ea8151f)\
  2019-10-28 14:54:28 +0200
  * Rename LOG\_HEADER\_FORMAT\_ to log\_t::FORMAT\_
* [Revision #8f46e3833c](https://github.com/MariaDB/server/commit/8f46e3833c)\
  2019-10-28 16:16:21 +0200
  * Revert [MDEV-17099](https://jira.mariadb.org/browse/MDEV-17099) Preliminary changes for Galera XA support (#1401)
* [Revision #9afbb1069a](https://github.com/MariaDB/server/commit/9afbb1069a)\
  2019-10-25 12:32:11 +0300
  * Add wait\_condition to stabilize.
* [Revision #2b5f4b3ed6](https://github.com/MariaDB/server/commit/2b5f4b3ed6)\
  2019-10-24 13:05:33 +0200
  * [MDEV-17099](https://jira.mariadb.org/browse/MDEV-17099) Preliminary changes for Galera XA support (#1401)
* [Revision #82f22d2f25](https://github.com/MariaDB/server/commit/82f22d2f25)\
  2019-10-18 08:26:54 +0300
  * [MDEV-18590](https://jira.mariadb.org/browse/MDEV-18590) galera.versioning\_trx\_id: Test failure: mysqltest: Result content mismatch
* [Revision #1036886b70](https://github.com/MariaDB/server/commit/1036886b70)\
  2019-10-16 14:02:16 +0300
  * Stabilize tests.
* [Revision #9c735784ae](https://github.com/MariaDB/server/commit/9c735784ae)\
  2019-10-20 15:48:20 +0300
  * Ensure that full\_crc32\_import doesn't fail
* [Revision #c2e0a0b175](https://github.com/MariaDB/server/commit/c2e0a0b175)\
  2019-10-20 14:42:59 +0300
  * Server crashes with BACKUP STAGE and FLUSH TABLE table\_name
* [Revision #5b6b16636d](https://github.com/MariaDB/server/commit/5b6b16636d)\
  2019-10-17 23:20:34 +0200
  * [MDEV-20730](https://jira.mariadb.org/browse/MDEV-20730): Syntax error on SELECT INTO @variable with CTE
* [Revision #421d52e896](https://github.com/MariaDB/server/commit/421d52e896)\
  2019-10-16 07:51:36 +0300
  * [MDEV-6860](https://jira.mariadb.org/browse/MDEV-6860) Parallel async replication hangs (#1400)
* Merge [Revision #899c843f11](https://github.com/MariaDB/server/commit/899c843f11) 2019-10-12 22:03:31 +0300 - Merge 10.3 into 10.4
* Merge [Revision #0a473de08d](https://github.com/MariaDB/server/commit/0a473de08d) 2019-10-12 15:47:20 +0300 - Null-merge 10.3 into 10.4
* [Revision #dba743b653](https://github.com/MariaDB/server/commit/dba743b653)\
  2019-10-12 06:57:02 +0300
  * Fix -Wunused-variable
* Merge [Revision #55c75b6bb3](https://github.com/MariaDB/server/commit/55c75b6bb3) 2019-10-12 06:50:12 +0300 - Merge 10.3 into 10.4
* [Revision #36824d2bef](https://github.com/MariaDB/server/commit/36824d2bef)\
  2019-10-07 12:34:08 +0200
  * [MDEV-20728](https://jira.mariadb.org/browse/MDEV-20728): /usr/sbin/mysqld: unknown variable 'defaults-group-suffix=mysqld1
* [Revision #b05be3ef8c](https://github.com/MariaDB/server/commit/b05be3ef8c)\
  2019-10-11 08:24:30 +0300
  * Add encryption.innodb-redo-badkey,strict\_full\_crc32
* Merge [Revision #09afd3da1a](https://github.com/MariaDB/server/commit/09afd3da1a) 2019-10-10 21:30:40 +0300 - Merge 10.3 into 10.4
* [Revision #0f7732d1d1](https://github.com/MariaDB/server/commit/0f7732d1d1)\
  2019-10-10 15:19:44 +0300
  * [MDEV-19335](https://jira.mariadb.org/browse/MDEV-19335) adjustment for innodb\_checksum\_algorithm=full\_crc32
* Merge [Revision #c11e5cdd12](https://github.com/MariaDB/server/commit/c11e5cdd12) 2019-10-10 11:19:25 +0300 - Merge 10.3 into 10.4
* [Revision #62dce14d15](https://github.com/MariaDB/server/commit/62dce14d15)\
  2019-10-09 11:42:50 +0300
  * [MDEV-20782](https://jira.mariadb.org/browse/MDEV-20782) : Galera test failure on galera\_sr.galera\_sr\_mysqldump\_sst
* [Revision #44a11a7c08](https://github.com/MariaDB/server/commit/44a11a7c08)\
  2019-10-09 11:41:14 +0300
  * [MDEV-20780](https://jira.mariadb.org/browse/MDEV-20780) : Galera test failure on galera\_sr.galera\_sr\_ddl\_master
* [Revision #57b666b2e5](https://github.com/MariaDB/server/commit/57b666b2e5)\
  2019-10-08 15:04:39 +0300
  * Fix test case wsrep.mdev\_6832 we need to wait until wsrep\_ready is ON before test can end.
* [Revision #6bc75a4253](https://github.com/MariaDB/server/commit/6bc75a4253)\
  2019-10-08 13:05:35 +0300
  * [MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528) preparation: Remove a constant parameter
* [Revision #c339487030](https://github.com/MariaDB/server/commit/c339487030)\
  2019-10-07 08:47:42 +0300
  * Try to fix galera\_parallel\_simple test case.
* [Revision #37570e845b](https://github.com/MariaDB/server/commit/37570e845b)\
  2019-10-04 20:16:39 +0300
  * [MDEV-20740](https://jira.mariadb.org/browse/MDEV-20740): Odd computations in calculate\_cond\_selectivity\_for\_table
* [Revision #a5c34bc200](https://github.com/MariaDB/server/commit/a5c34bc200)\
  2019-10-04 10:11:47 +0200
  * if the test uses example plugin, it has to check whether plugin exists
* [Revision #b710d01dc7](https://github.com/MariaDB/server/commit/b710d01dc7)\
  2019-09-25 16:57:05 +0200
  * mark PAMv2 plugin stable
* [Revision #fe4f766e81](https://github.com/MariaDB/server/commit/fe4f766e81)\
  2019-10-04 14:44:16 +0300
  * Add wait\_condition to wait that node returns to ready state before accessing it.
* [Revision #5709a7777b](https://github.com/MariaDB/server/commit/5709a7777b)\
  2019-10-04 10:27:55 +0300
  * [MDEV-19956](https://jira.mariadb.org/browse/MDEV-19956): Do not dereference an uninitialized pointer
* [Revision #eb0a10b072](https://github.com/MariaDB/server/commit/eb0a10b072)\
  2019-10-03 07:03:15 +0300
  * Add missing have\_debug to galera.[MDEV-20225](https://jira.mariadb.org/browse/MDEV-20225) test case.
* [Revision #97d82c3429](https://github.com/MariaDB/server/commit/97d82c3429)\
  2019-10-01 12:40:29 +0300
  * galera\_sp\_bf\_abort requires debug Galera library.
* [Revision #c42c4233cb](https://github.com/MariaDB/server/commit/c42c4233cb)\
  2019-10-01 10:41:33 +0300
  * [MDEV-20225](https://jira.mariadb.org/browse/MDEV-20225) BF aborting SP execution (#1394)
* Merge [Revision #dc588e3d3f](https://github.com/MariaDB/server/commit/dc588e3d3f) 2019-10-01 10:45:52 +0400 - Merge remote-tracking branch 'origin/10.3' into 10.4
* [Revision #f1dcbc2d9a](https://github.com/MariaDB/server/commit/f1dcbc2d9a)\
  2019-09-28 12:34:57 +0400
  * [MDEV-20639](https://jira.mariadb.org/browse/MDEV-20639) ASAN SEGV in get\_prefix upon modifying base column type with existing indexed virtual column
* Merge [Revision #9b5cdeeb0f](https://github.com/MariaDB/server/commit/9b5cdeeb0f) 2019-09-27 16:26:53 +0300 - Merge 10.3 into 10.4
* [Revision #ea2b19dee6](https://github.com/MariaDB/server/commit/ea2b19dee6)\
  2019-09-27 16:01:55 +0300
  * [MDEV-20117](https://jira.mariadb.org/browse/MDEV-20117): Fix another scenario
* [Revision #1f4ee3fa5a](https://github.com/MariaDB/server/commit/1f4ee3fa5a)\
  2019-09-26 19:45:10 +0300
  * [MDEV-20117](https://jira.mariadb.org/browse/MDEV-20117) Assertion 0 failed in row\_sel\_get\_clust\_rec\_for\_mysql
* Merge [Revision #bb5afc7ceb](https://github.com/MariaDB/server/commit/bb5afc7ceb) 2019-09-26 16:56:02 +0300 - Merge 10.3 into 10.4
* [Revision #e3c39c0be8](https://github.com/MariaDB/server/commit/e3c39c0be8)\
  2019-09-26 10:25:34 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) follow-up: Remove dead code
* Merge [Revision #d3350c160a](https://github.com/MariaDB/server/commit/d3350c160a) 2019-09-25 10:14:33 +0300 - Merge 10.3 into 10.4
* [Revision #a39c4b5f9f](https://github.com/MariaDB/server/commit/a39c4b5f9f)\
  2019-09-16 18:56:29 +0300
  * Update mysqld\_multi.sh
* [Revision #b44171428a](https://github.com/MariaDB/server/commit/b44171428a)\
  2019-09-20 09:03:38 -0700
  * [MDEV-19956](https://jira.mariadb.org/browse/MDEV-19956) Queries with subqueries containing UNION are not parsed
* [Revision #e3da362c03](https://github.com/MariaDB/server/commit/e3da362c03)\
  2019-09-22 21:04:00 +0300
  * [MDEV-19189](https://jira.mariadb.org/browse/MDEV-19189) ASAN memcpy-param-overlap in fill\_alter\_inplace\_info upon adding indexes
* Merge [Revision #5a92ccbaea](https://github.com/MariaDB/server/commit/5a92ccbaea) 2019-09-23 17:35:29 +0300 - Merge 10.3 into 10.4
* [Revision #c997af7d1f](https://github.com/MariaDB/server/commit/c997af7d1f)\
  2019-09-23 10:33:10 +0300
  * Remove reference to dict\_sys->mutex
* [Revision #631c5ab45f](https://github.com/MariaDB/server/commit/631c5ab45f)\
  2019-06-12 12:33:34 +0000
  * Removing obsolete register keyword
* [Revision #d99216356d](https://github.com/MariaDB/server/commit/d99216356d)\
  2019-04-09 22:28:10 +0200
  * cmake: support new libedit interface
* [Revision #2f88bd2da2](https://github.com/MariaDB/server/commit/2f88bd2da2)\
  2019-09-20 10:36:20 +0400
  * [MDEV-20634](https://jira.mariadb.org/browse/MDEV-20634) Report disallowed subquery errors as such (instead of parse error)
* [Revision #b9dea911bf](https://github.com/MariaDB/server/commit/b9dea911bf)\
  2019-07-27 15:56:58 -0300
  * Extend mysql\_instal\_db to search plugins also from lib/\*/mariadb19/plugin
* [Revision #97cd583df7](https://github.com/MariaDB/server/commit/97cd583df7)\
  2019-07-26 18:36:42 -0300
  * Deb: Sync non-functional changes from official Debian 10.4 packaging
* [Revision #ffd36093f1](https://github.com/MariaDB/server/commit/ffd36093f1)\
  2019-07-24 20:49:12 -0300
  * Deb: Run 'wrap-and-sort -a' so comparison across releases is easier
* [Revision #bf617c3654](https://github.com/MariaDB/server/commit/bf617c3654)\
  2019-09-18 09:51:13 +0400
  * [MDEV-20423](https://jira.mariadb.org/browse/MDEV-20423) Assertion `0' failed or` btr\_validate\_index(index, 0, false)' in row\_upd\_sec\_index\_entry or error code 126: Index is corrupted upon DELETE with TIME\_ROUND\_FRACTIONAL
* [Revision #efefafd02f](https://github.com/MariaDB/server/commit/efefafd02f)\
  2019-09-17 04:58:20 -0300
  * fix for thread getting stuck after BF ABORT (#1362)
* [Revision #c793f07841](https://github.com/MariaDB/server/commit/c793f07841)\
  2019-09-16 14:57:39 +0300
  * Re-record galera\_shutdown\_nonprim for 10.4.
* [Revision #da76ae2162](https://github.com/MariaDB/server/commit/da76ae2162)\
  2019-09-16 14:57:18 +0300
  * Disable galera\_var\_notify\_cmd as it causes hang.
* [Revision #509d103810](https://github.com/MariaDB/server/commit/509d103810)\
  2019-09-13 09:18:11 +0300
  * [MDEV-20561](https://jira.mariadb.org/browse/MDEV-20561) Galera node shutdown fails in non-Primary (#1386)
* [Revision #c946b5f38a](https://github.com/MariaDB/server/commit/c946b5f38a)\
  2019-09-13 14:23:13 +0300
  * Re-record galera.galera\_pc\_ignore\_sb test result for 10.4.
* [Revision #e73dbec1c8](https://github.com/MariaDB/server/commit/e73dbec1c8)\
  2019-09-13 11:10:54 +0300
  * Disable wsrep.variables until fixed.
* [Revision #1f1f172002](https://github.com/MariaDB/server/commit/1f1f172002)\
  2019-09-13 11:03:26 +0300
  * Re-record galera.galera\_events2 test case.
* [Revision #8711f5505a](https://github.com/MariaDB/server/commit/8711f5505a)\
  2019-09-13 09:22:10 +0300
  * Fix galera.galera\_sst\_mysqldump\_with\_key test case for 10.4
* [Revision #7ced6fa141](https://github.com/MariaDB/server/commit/7ced6fa141)\
  2019-09-13 20:03:43 +0400
  * [MDEV-20228](https://jira.mariadb.org/browse/MDEV-20228) `mysql_upgrade` fails on every version upgrade: "ERROR 1267 (HY000) at line 7: Illegal mix of collations (utf8mb4\_unicode\_ci,COERCIBLE) and (utf8mb4\_general\_ci,COERCIBLE) for operation 'like'"
* [Revision #c924e39fab](https://github.com/MariaDB/server/commit/c924e39fab)\
  2019-09-13 11:04:23 +0400
  * [MDEV-18153](https://jira.mariadb.org/browse/MDEV-18153) Assertion `0' or Assertion` btr\_validate\_index(index, 0)' failed in row\_upd\_sec\_index\_entry or error code 126: Index is corrupted upon UPDATE with TIME\_ROUND\_FRACTIONAL
* [Revision #368e64aaed](https://github.com/MariaDB/server/commit/368e64aaed)\
  2019-09-13 10:42:10 +0300
  * [MDEV-19826](https://jira.mariadb.org/browse/MDEV-19826): Avoid unused variable in cmake -DPLUGIN\_PERFSCHEMA=NO
* [Revision #d0b74bbacc](https://github.com/MariaDB/server/commit/d0b74bbacc)\
  2019-09-12 19:07:56 +0300
  * [MDEV-20440](https://jira.mariadb.org/browse/MDEV-20440): Optimizer trace: print more details about semi-join optimization
* Merge [Revision #60c04be659](https://github.com/MariaDB/server/commit/60c04be659) 2019-09-12 12:16:40 +0300 - Merge 10.3 into 10.4
* [Revision #ebddd8699c](https://github.com/MariaDB/server/commit/ebddd8699c)\
  2019-09-12 11:42:48 +0300
  * [MDEV-20565](https://jira.mariadb.org/browse/MDEV-20565) Assertion failure on CHANGE COLUMN...SYSTEM VERSIONING
* [Revision #9bacc9d0c1](https://github.com/MariaDB/server/commit/9bacc9d0c1)\
  2019-09-11 13:13:37 +0300
  * [MDEV-20505](https://jira.mariadb.org/browse/MDEV-20505): Server crash on startup beacuse of bad wsrep configuration
* [Revision #5c5452a5a0](https://github.com/MariaDB/server/commit/5c5452a5a0)\
  2019-09-11 09:15:28 -0400
  * bump the VERSION
* [Revision #71c57bcf8f](https://github.com/MariaDB/server/commit/71c57bcf8f)\
  2019-09-10 14:01:31 +0530
  * Moved the function trace\_plan\_prefix to the optimizer trace file
* [Revision #7b988e5ceb](https://github.com/MariaDB/server/commit/7b988e5ceb)\
  2019-09-04 19:51:27 +0530
  * [MDEV-20444](https://jira.mariadb.org/browse/MDEV-20444): More information regarding access of a table to be printed inside the optimizer\_trace
* Merge [Revision #e980cf91cd](https://github.com/MariaDB/server/commit/e980cf91cd) 2019-09-10 16:09:14 +0300 - Merge mariadb-10.4.8 to 10.4
* [Revision #e2f570bff8](https://github.com/MariaDB/server/commit/e2f570bff8)\
  2019-09-10 17:41:26 +0530
  * [MDEV-20320](https://jira.mariadb.org/browse/MDEV-20320) Tablespace flags mismatch for full\_crc32 format
* [Revision #13f740904a](https://github.com/MariaDB/server/commit/13f740904a)\
  2019-09-10 12:43:48 +0300
  * [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112)/[MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026): Enable the test for full\_crc32
* [Revision #fe4a4bb0a4](https://github.com/MariaDB/server/commit/fe4a4bb0a4)\
  2019-09-08 23:40:08 +0300
  * List of unstable tests for 10.4.8 release
* [Revision #c1a2778e68](https://github.com/MariaDB/server/commit/c1a2778e68)\
  2019-09-07 10:34:46 +0300
  * [MDEV-17171](https://jira.mariadb.org/browse/MDEV-17171): RocksDB Tables do not have "Creation Date"
* [Revision #2d93efc001](https://github.com/MariaDB/server/commit/2d93efc001)\
  2019-09-06 22:11:29 +0300
  * [MDEV-17171](https://jira.mariadb.org/browse/MDEV-17171): RocksDB Tables do not have "Creation Date"

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
