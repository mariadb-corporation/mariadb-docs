# MariaDB 10.2.38 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download 10.2.38](https://downloads.mariadb.org/mariadb/10.2.38/)[Release Notes](../../old-releases/10.2/10.2.38.md)[Changelog](mariadb-10238-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 7 May 2021

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.38.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #a20195bba5](https://github.com/MariaDB/server/commit/a20195bba5)\
  2021-05-03 23:26:30 +0200
  * [MDEV-21603](https://jira.mariadb.org/browse/MDEV-21603) Crashing SHOW TABLES with derived table in WHERE condition
* [Revision #72fa9dabad](https://github.com/MariaDB/server/commit/72fa9dabad)\
  2021-05-02 23:24:28 +0300
  * Connect: remove Mongo dependencies
* [Revision #098e4efd33](https://github.com/MariaDB/server/commit/098e4efd33)\
  2021-05-02 14:02:47 +0200
  * new CC
* [Revision #562c88257f](https://github.com/MariaDB/server/commit/562c88257f)\
  2021-05-03 16:30:52 +0300
  * [MDEV-10674](https://jira.mariadb.org/browse/MDEV-10674): main.show\_explain failed in buildbot
* [Revision #a910e1ee9e](https://github.com/MariaDB/server/commit/a910e1ee9e)\
  2021-05-03 15:34:52 +0200
  * [MDEV-25584](https://jira.mariadb.org/browse/MDEV-25584) Implement posix semantics file deletion for Windows 10
* [Revision #abe6eb10a6](https://github.com/MariaDB/server/commit/abe6eb10a6)\
  2021-04-30 18:12:43 +0530
  * [MDEV-16146](https://jira.mariadb.org/browse/MDEV-16146): MariaDB slave stops with following errors.
* [Revision #13b9af50e4](https://github.com/MariaDB/server/commit/13b9af50e4)\
  2021-04-30 20:05:12 +0530
  * [MDEV-25536](https://jira.mariadb.org/browse/MDEV-25536) InnoDB: Failing assertion: sym\_node->table != NULL in pars\_retrieve\_table\_def
* [Revision #0024524d54](https://github.com/MariaDB/server/commit/0024524d54)\
  2021-04-29 12:31:06 +0530
  * [MDEV-25536](https://jira.mariadb.org/browse/MDEV-25536) InnoDB: Failing assertion: sym\_node->table != NULL in pars\_retrieve\_table\_def
* [Revision #65d2fbaf77](https://github.com/MariaDB/server/commit/65d2fbaf77)\
  2021-04-30 09:37:50 +0300
  * [MDEV-25568](https://jira.mariadb.org/browse/MDEV-25568) RENAME TABLE causes "Ignoring data file" messages
* [Revision #26148e2a67](https://github.com/MariaDB/server/commit/26148e2a67)\
  2021-04-30 00:22:41 +0300
  * Revert "update CC"
* [Revision #8880dff2d9](https://github.com/MariaDB/server/commit/8880dff2d9)\
  2021-04-29 13:14:57 +0300
  * update CC
* Merge [Revision #695c1e287b](https://github.com/MariaDB/server/commit/695c1e287b) 2021-04-28 15:25:28 +0300 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #4df6952ce3](https://github.com/MariaDB/server/commit/4df6952ce3)\
  2021-04-09 16:10:37 +0200
  * Typo modified: CMakeLists.txt
* [Revision #36fd94aa5c](https://github.com/MariaDB/server/commit/36fd94aa5c)\
  2021-04-09 15:24:34 +0200
  * Remove add\_jar modified: CMakeLists.txt
* [Revision #46340ad8d1](https://github.com/MariaDB/server/commit/46340ad8d1)\
  2021-04-09 14:41:50 +0200
  * Fix add\_jar modified: CMakeLists.txt
* [Revision #03f929aea8](https://github.com/MariaDB/server/commit/03f929aea8)\
  2021-04-09 11:58:13 +0200
  * Fix install modified: CMakeLists.txt
* [Revision #bbec4aafda](https://github.com/MariaDB/server/commit/bbec4aafda)\
  2021-04-08 19:04:07 +0200
  * typo tabrest.cpp
* [Revision #710e1bac5a](https://github.com/MariaDB/server/commit/710e1bac5a)\
  2021-04-07 23:43:08 +0200
  * tabrest.cpp
* [Revision #757aaa3bcc](https://github.com/MariaDB/server/commit/757aaa3bcc)\
  2021-04-07 19:15:31 +0200
  * tabrest.cpp
* [Revision #e4c23fe2d0](https://github.com/MariaDB/server/commit/e4c23fe2d0)\
  2021-04-07 17:40:24 +0200
  * tabrest.cpp
* [Revision #953c84657b](https://github.com/MariaDB/server/commit/953c84657b)\
  2021-04-07 16:48:14 +0200
  * try to fix tabrest.cpp compile error
* [Revision #26e5ba4b51](https://github.com/MariaDB/server/commit/26e5ba4b51)\
  2021-04-07 15:53:46 +0200\
  \*
  * Fix Linux compile errors modified: storage/connect/tabrest.cpp modified: storage/connect/CMakeLists.txt
* [Revision #d1b6cad028](https://github.com/MariaDB/server/commit/d1b6cad028)\
  2021-04-06 14:16:38 +0200
  * Test tabrest.cpp fix
* Merge [Revision #c030f4c625](https://github.com/MariaDB/server/commit/c030f4c625) 2021-04-06 12:52:44 +0200 - Commit last pull from origin
* [Revision #28b76afcea](https://github.com/MariaDB/server/commit/28b76afcea)\
  2021-04-06 00:10:07 +0200\
  \*
  * Fix(?) Linux compile errors modified: storage/connect/tabrest.cpp modified: storage/connect/CMakeLists.txt
* [Revision #2aefe0bee1](https://github.com/MariaDB/server/commit/2aefe0bee1)\
  2021-04-05 18:33:37 +0200\
  \*
  * Fix crash when not specifying the collection for MongoDB modified: storage/connect/cmgoconn.cpp
* [Revision #caff19ada5](https://github.com/MariaDB/server/commit/caff19ada5)\
  2021-04-05 17:01:43 +0200\
  \*
  * Copy Mongo2.jar and Mongo3.jar in plugin directory modified: storage/connect/CMakeLists.txt modified: storage/connect/javaconn.cpp
* [Revision #e85006e670](https://github.com/MariaDB/server/commit/e85006e670)\
  2021-03-16 23:32:58 +0100\
  \*
  * Fix bug making REST table fail using CURL This when the HTTP contains & characters modified: storage/connect/tabbson.cpp modified: storage/connect/tabjson.cpp
* [Revision #801a6d500f](https://github.com/MariaDB/server/commit/801a6d500f)\
  2021-02-16 00:31:27 +0100\
  \*
  * Add new JPATH features modified: storage/connect/bson.cpp modified: storage/connect/bsonudf.cpp modified: storage/connect/bsonudf.h modified: storage/connect/json.cpp modified: storage/connect/jsonudf.cpp modified: storage/connect/jsonudf.h modified: storage/connect/mysql-test/connect/r/json\_udf.result modified: storage/connect/tabbson.cpp modified: storage/connect/tabjson.cpp modified: storage/connect/tabjson.h
* [Revision #d788225b66](https://github.com/MariaDB/server/commit/d788225b66)\
  2021-02-05 18:07:43 +0100
  * Fix bson\_object\_grp inverted args. Modified: storage/connect/bsonudf.cpp and bson\_udf.result
* [Revision #ca63004190](https://github.com/MariaDB/server/commit/ca63004190)\
  2021-02-05 11:55:47 +0100\
  \*
  * Fix bug causing bnx base wrong after CheckMemory Add negative array indexes starting from the last modified: storage/connect/bson.cpp modified: storage/connect/bsonudf.cpp modified: storage/connect/json.cpp
* [Revision #b1ac251bf1](https://github.com/MariaDB/server/commit/b1ac251bf1)\
  2021-04-28 17:39:04 -0700
  * Another correction of the patch for [MDEV-24823](https://jira.mariadb.org/browse/MDEV-24823).
* [Revision #e788738e18](https://github.com/MariaDB/server/commit/e788738e18)\
  2021-04-28 10:42:20 +0700
  * [MDEV-25543](https://jira.mariadb.org/browse/MDEV-25543): Building failure on MacOS in case MariadDB server is compiled with XCode 12.5
* [Revision #24693c6fcf](https://github.com/MariaDB/server/commit/24693c6fcf)\
  2021-04-27 16:08:33 +0200
  * Bug#29363867: LOST CONNECTION TO MYSQL SERVER DURING QUERY
* [Revision #e85b389b76](https://github.com/MariaDB/server/commit/e85b389b76)\
  2021-04-27 14:50:21 +0300
  * [MDEV-25319](https://jira.mariadb.org/browse/MDEV-25319) : Long BF log wait turns on InnoDB Monitor output without telling, never turns it off
* [Revision #f946192e6f](https://github.com/MariaDB/server/commit/f946192e6f)\
  2021-04-27 10:41:36 +0300
  * [MDEV-25258](https://jira.mariadb.org/browse/MDEV-25258) : SET PASSWORD command fail with wsrep api
* [Revision #c6dbabed56](https://github.com/MariaDB/server/commit/c6dbabed56)\
  2020-10-21 11:39:24 +0300
  * [MDEV-21514](https://jira.mariadb.org/browse/MDEV-21514) : Galera test failure on galera.galera\_wan\_restart\_sst
* [Revision #b9fbd102dd](https://github.com/MariaDB/server/commit/b9fbd102dd)\
  2021-04-28 00:36:19 +0200
  * [MDEV-19198](https://jira.mariadb.org/browse/MDEV-19198) - DBUG assert in CREATE IF NOT EXIST under LOCK TABLES WRITE
* [Revision #a6e97dad8a](https://github.com/MariaDB/server/commit/a6e97dad8a)\
  2021-04-26 12:19:01 +0200
  * [MDEV-25232](https://jira.mariadb.org/browse/MDEV-25232) update libmariadb
* [Revision #b07a6f45fe](https://github.com/MariaDB/server/commit/b07a6f45fe)\
  2021-04-26 12:18:39 +0200
  * [MDEV-25232](https://jira.mariadb.org/browse/MDEV-25232) - CMake deprecation warning about CMAKE\_MINIMUM\_REQUIRED < 2.8.12
* [Revision #91599701d0](https://github.com/MariaDB/server/commit/91599701d0)\
  2021-04-26 22:32:58 +0200
  * Bug#29363867: LOST CONNECTION TO MYSQL SERVER DURING QUERY
* [Revision #4f63b6cf53](https://github.com/MariaDB/server/commit/4f63b6cf53)\
  2021-04-26 16:52:32 +0200
  * Bug #31674599: THE UDF\_INIT() FUNCTION CAUSE SERVER CRASH
* [Revision #883b723d7c](https://github.com/MariaDB/server/commit/883b723d7c)\
  2021-04-27 11:19:10 +0200
  * [MDEV-25326](https://jira.mariadb.org/browse/MDEV-25326) mysql\_install\_db help text incomplete
* [Revision #b862377c3e](https://github.com/MariaDB/server/commit/b862377c3e)\
  2021-04-27 16:46:54 +0530
  * [MDEV-25503](https://jira.mariadb.org/browse/MDEV-25503) InnoDB hangs on startup during recovery
* [Revision #2b0d5b78c2](https://github.com/MariaDB/server/commit/2b0d5b78c2)\
  2021-04-26 22:20:44 +0530
  * [MDEV-22928](https://jira.mariadb.org/browse/MDEV-22928) InnoDB fails to fetch index type when index mismatch happens
* [Revision #43e879c717](https://github.com/MariaDB/server/commit/43e879c717)\
  2021-03-24 01:02:26 +0300
  * [MDEV-24583](https://jira.mariadb.org/browse/MDEV-24583) SELECT aborts after failed REPLACE into table with vcol
* [Revision #f85afa5124](https://github.com/MariaDB/server/commit/f85afa5124)\
  2021-03-23 16:48:02 +0300
  * [MDEV-19011](https://jira.mariadb.org/browse/MDEV-19011) Assertion \`file->s->base.reclength < file->s->vreclength' failed
* [Revision #6ba5f81c7d](https://github.com/MariaDB/server/commit/6ba5f81c7d)\
  2021-04-06 21:31:00 +0300
  * [MDEV-16962](https://jira.mariadb.org/browse/MDEV-16962) Assertion failed in open\_purge\_table upon concurrent ALTER/FLUSH
* [Revision #300253acf1](https://github.com/MariaDB/server/commit/300253acf1)\
  2019-07-25 22:17:04 +1000
  * revive innodb\_debug\_sync
* [Revision #a35cde8cd8](https://github.com/MariaDB/server/commit/a35cde8cd8)\
  2021-04-27 08:17:37 +1000
  * [MDEV-25513](https://jira.mariadb.org/browse/MDEV-25513): raise systemd LimitNOFILE limits to match server defaults
* [Revision #2f6912dabc](https://github.com/MariaDB/server/commit/2f6912dabc)\
  2021-04-23 19:45:09 +0300
  * [MDEV-24898](https://jira.mariadb.org/browse/MDEV-24898): Server crashes in st\_select\_lex::next\_select
* [Revision #c72c77ca3b](https://github.com/MariaDB/server/commit/c72c77ca3b)\
  2021-04-23 19:28:48 +0300
  * [MDEV-24925](https://jira.mariadb.org/browse/MDEV-24925): Server crashes in Item\_subselect::init\_expr\_cache\_tracker
* [Revision #14a18d7d7f](https://github.com/MariaDB/server/commit/14a18d7d7f)\
  2021-04-24 09:37:46 +0300
  * [MDEV-23026](https://jira.mariadb.org/browse/MDEV-23026)/[MDEV-25474](https://jira.mariadb.org/browse/MDEV-25474) fixup: Assertion ib\_table->stat\_initialized
* [Revision #25ed665a20](https://github.com/MariaDB/server/commit/25ed665a20)\
  2021-04-23 14:49:32 +0300
  * [MDEV-25459](https://jira.mariadb.org/browse/MDEV-25459) MVCC read from index on CHAR or VARCHAR wrongly omits rows
* [Revision #1288dfffe7](https://github.com/MariaDB/server/commit/1288dfffe7)\
  2021-04-23 14:32:20 -0700
  * This patch complements the patch for [MDEV-24823](https://jira.mariadb.org/browse/MDEV-24823).
* [Revision #42f8548ff6](https://github.com/MariaDB/server/commit/42f8548ff6)\
  2021-03-26 11:44:54 +0300
  * [MDEV-25091](https://jira.mariadb.org/browse/MDEV-25091) CREATE TABLE: field references qualified by a wrong table name succeed
* [Revision #4649ba7493](https://github.com/MariaDB/server/commit/4649ba7493)\
  2021-03-25 11:33:11 +0300
  * [MDEV-23455](https://jira.mariadb.org/browse/MDEV-23455) Hangs + Sig11 in unknown location(s) due to single complex FK query
* [Revision #018d7440fd](https://github.com/MariaDB/server/commit/018d7440fd)\
  2021-04-22 11:18:30 +0200
  * remove EXCEPTIONS-CLIENT
* [Revision #b3b5d57e78](https://github.com/MariaDB/server/commit/b3b5d57e78)\
  2021-04-19 19:52:06 -0700
  * [MDEV-24823](https://jira.mariadb.org/browse/MDEV-24823) Crash with invalid multi-table update of view in 2nd execution of SP
* [Revision #5c5d24c772](https://github.com/MariaDB/server/commit/5c5d24c772)\
  2021-04-22 16:59:30 +0200
  * [MDEV-25456](https://jira.mariadb.org/browse/MDEV-25456) - fix predicate in ib::error\_or\_warn
* [Revision #78bb9533f4](https://github.com/MariaDB/server/commit/78bb9533f4)\
  2021-04-22 15:49:00 +0200
  * [MDEV-25456](https://jira.mariadb.org/browse/MDEV-25456) mariadb-backup logs "\[ERROR]" on Invalid log block checksum
* [Revision #f6542a7af8](https://github.com/MariaDB/server/commit/f6542a7af8)\
  2021-04-01 23:01:19 +0200
  * Update timezone data on Windows
* [Revision #fb96ac0a49](https://github.com/MariaDB/server/commit/fb96ac0a49)\
  2021-04-21 21:12:33 +0530
  * [MDEV-25474](https://jira.mariadb.org/browse/MDEV-25474) Background thread returns uninitialized statistics to mysql interpreter
* [Revision #64eeb250eb](https://github.com/MariaDB/server/commit/64eeb250eb)\
  2021-04-20 22:33:22 +0300
  * [MDEV-25457](https://jira.mariadb.org/browse/MDEV-25457) Server crashes in row\_undo\_mod\_clust\_low upon rollback of read-only transaction
* [Revision #2a7dd64425](https://github.com/MariaDB/server/commit/2a7dd64425)\
  2021-01-05 18:08:25 +0200
  * [MDEV-24526](https://jira.mariadb.org/browse/MDEV-24526) binlog rotate via FLUSH LOGS may obsolate binlog file for recovery too eary
* [Revision #ef2749c90d](https://github.com/MariaDB/server/commit/ef2749c90d)\
  2021-04-21 09:21:24 +0300
  * Fixup: Event\_queue\_element\_for\_exec initializer list not supported on gcc-4.1
* [Revision #9e6e0eaee2](https://github.com/MariaDB/server/commit/9e6e0eaee2)\
  2021-04-20 12:10:24 +0900
  * fixed some korean error messages
* [Revision #df18fa4cae](https://github.com/MariaDB/server/commit/df18fa4cae)\
  2021-04-21 02:44:14 +0300
  * Smoke test collection should not be executable
* [Revision #3635280cf7](https://github.com/MariaDB/server/commit/3635280cf7)\
  2021-04-21 01:03:32 +0300
  * [MDEV-25288](https://jira.mariadb.org/browse/MDEV-25288) Create a list of tests for distributions
* [Revision #6244876488](https://github.com/MariaDB/server/commit/6244876488)\
  2021-04-20 23:09:01 +0300
  * [MDEV-24807](https://jira.mariadb.org/browse/MDEV-24807):A possibility for double free in dtor of Event\_queue\_element\_for\_exec in the case of OOM
* Merge [Revision #922e676b43](https://github.com/MariaDB/server/commit/922e676b43) 2021-04-20 17:33:36 +0300 - [MDEV-25466](https://jira.mariadb.org/browse/MDEV-25466) Merge new release of InnoDB 5.7.34 to 10.2
* [Revision #72432ec7b3](https://github.com/MariaDB/server/commit/72432ec7b3)\
  2021-02-24 07:49:37 +0530
  * Bug #32032897 DEADLOCKING WAIT GRAPH ON BUSY SERVER
* [Revision #635b5ce355](https://github.com/MariaDB/server/commit/635b5ce355)\
  2021-04-16 09:53:16 -0700
  * [MDEV-25362](https://jira.mariadb.org/browse/MDEV-25362) Incorrect name resolution for subqueries in ON expressions
* [Revision #73bf62469e](https://github.com/MariaDB/server/commit/73bf62469e)\
  2020-11-20 16:55:03 +1100
  * [MDEV-15064](https://jira.mariadb.org/browse/MDEV-15064): IO\_CACHE mysys read\_pos, not libmaria rc\_pos
* [Revision #ab5dc62545](https://github.com/MariaDB/server/commit/ab5dc62545)\
  2021-04-13 20:32:16 +0300
  * [MDEV-25407](https://jira.mariadb.org/browse/MDEV-25407): EXISTS subquery with correlation in ON expression crashes
* [Revision #a3871cd283](https://github.com/MariaDB/server/commit/a3871cd283)\
  2021-03-31 16:36:36 +0300
  * [MDEV-22255](https://jira.mariadb.org/browse/MDEV-22255) SIGABRT: Assertion `id' failed in trx_write_trx_id on INSERT | Assertion` id > 0' failed in trx\_write\_trx\_id | Assertion `val > 0' failed in row_upd_index_entry_sys_field | Assertion` thr\_get\_trx(thr)->id || index->table->no\_rollback()' failed.
* [Revision #7fa12b1e34](https://github.com/MariaDB/server/commit/7fa12b1e34)\
  2021-04-12 21:18:14 +0530
  * [MDEV-23026](https://jira.mariadb.org/browse/MDEV-23026) purge fails with assert !rw\_lock\_own\_flagged(lock, RW\_LOCK\_FLAG\_X | RW\_LOCK\_FLAG\_S)
* [Revision #343fe4e232](https://github.com/MariaDB/server/commit/343fe4e232)\
  2021-04-14 20:01:51 +0200
  * update C/C
* [Revision #499e617182](https://github.com/MariaDB/server/commit/499e617182)\
  2021-04-13 19:52:40 +0200
  * [MDEV-25403](https://jira.mariadb.org/browse/MDEV-25403) ALTER TABLE wrongly checks for field's default value if AFTER is used
* [Revision #3ebd6cd3ad](https://github.com/MariaDB/server/commit/3ebd6cd3ad)\
  2021-03-30 18:48:56 +0100
  * signal handler, display coredump file pattern similarly to [MDEV-25294](https://jira.mariadb.org/browse/MDEV-25294) but for FreeBSD, thankfully the sysctl OID is the same.
* [Revision #022d3fa652](https://github.com/MariaDB/server/commit/022d3fa652)\
  2021-04-14 14:46:47 +0200
  * Update mysqlbinlog man page with --table option
* [Revision #7b791b82b8](https://github.com/MariaDB/server/commit/7b791b82b8)\
  2021-04-13 18:32:05 +0200
  * [MDEV-25363](https://jira.mariadb.org/browse/MDEV-25363) binlog\_stm\_datetime\_ranges\_mdev15289 failed in bb
* [Revision #2557064873](https://github.com/MariaDB/server/commit/2557064873)\
  2021-04-14 02:17:48 +0200
  * [MDEV-25354](https://jira.mariadb.org/browse/MDEV-25354): Fix my\_print\_defaults wording
* [Revision #55a7682a30](https://github.com/MariaDB/server/commit/55a7682a30)\
  2021-04-13 16:44:09 +0200
  * -DMYSQL\_MAINTAINER\_MODE=NO
* [Revision #e262eb165c](https://github.com/MariaDB/server/commit/e262eb165c)\
  2021-04-13 10:09:16 +0530
  * [MDEV-24971](https://jira.mariadb.org/browse/MDEV-24971) InnoDB access freed virtual column after rollback of secondary index
* [Revision #f776fa96b4](https://github.com/MariaDB/server/commit/f776fa96b4)\
  2021-02-03 12:04:06 +0300
  * [MDEV-24135](https://jira.mariadb.org/browse/MDEV-24135): Print warnings in XML, save test retries in XML, save the combinations in XML, replace the special symbols in the XML comment
* [Revision #68e0defc5b](https://github.com/MariaDB/server/commit/68e0defc5b)\
  2021-04-12 15:46:23 +0200
  * [MDEV-25182](https://jira.mariadb.org/browse/MDEV-25182) Complex query in Store procedure corrupts results
* [Revision #f8bf2a0170](https://github.com/MariaDB/server/commit/f8bf2a0170)\
  2021-04-12 19:28:10 +0700
  * [MDEV-25108](https://jira.mariadb.org/browse/MDEV-25108): Running of the EXPLAIN EXTENDED statement produces extra warning in case it is executed in PS (prepared statement) mode
* [Revision #e95cdc451a](https://github.com/MariaDB/server/commit/e95cdc451a)\
  2021-04-12 04:11:28 +0200
  * [MDEV-21484](https://jira.mariadb.org/browse/MDEV-21484): galera\_sst\_mariadb-backup\_encrypt\_with\_key test failed
* [Revision #cf2c6b7f8d](https://github.com/MariaDB/server/commit/cf2c6b7f8d)\
  2021-04-09 21:30:43 +0530
  * [MDEV-24971](https://jira.mariadb.org/browse/MDEV-24971) InnoDB access freed virtual column after rollback of secondary index
* [Revision #ea2d44d01b](https://github.com/MariaDB/server/commit/ea2d44d01b)\
  2021-04-12 11:29:32 +0300
  * [MDEV-18802](https://jira.mariadb.org/browse/MDEV-18802) Assertion table->stat\_initialized failed in dict\_stats\_update\_if\_needed()
* [Revision #75dd7a0483](https://github.com/MariaDB/server/commit/75dd7a0483)\
  2021-04-12 10:53:08 +0300
  * [MDEV-24434](https://jira.mariadb.org/browse/MDEV-24434) Assertion trx->in\_rw\_trx\_list... in trx\_sys\_any\_active\_transactions()
* [Revision #058d93d47a](https://github.com/MariaDB/server/commit/058d93d47a)\
  2021-04-11 22:05:52 -0700
  * Deb: Stop depending on empty transitional package dh-systemd
* [Revision #966c5a35af](https://github.com/MariaDB/server/commit/966c5a35af)\
  2021-04-01 07:01:11 +0200
  * [MDEV-25307](https://jira.mariadb.org/browse/MDEV-25307): The value of the auto-increment variables changes during the test
* [Revision #3eecb8db22](https://github.com/MariaDB/server/commit/3eecb8db22)\
  2021-04-11 17:07:36 +0200
  * [MDEV-25356](https://jira.mariadb.org/browse/MDEV-25356): SST scripts should use the new mariadb-backup interface
* [Revision #bf1e09e0c4](https://github.com/MariaDB/server/commit/bf1e09e0c4)\
  2021-04-07 16:53:23 +0200
  * Removed extra spaces in generated command lines (minor "cosmetic" change after [MDEV-24197](https://jira.mariadb.org/browse/MDEV-24197))
* [Revision #d5dacca4c5](https://github.com/MariaDB/server/commit/d5dacca4c5)\
  2021-04-07 16:49:10 +0200
  * Clarified abbreviated option names in some tests, to avoid problems with ambiguous options in the future.
* [Revision #8ff0ac45dc](https://github.com/MariaDB/server/commit/8ff0ac45dc)\
  2021-04-07 16:44:30 +0200
  * [MDEV-25328](https://jira.mariadb.org/browse/MDEV-25328): --innodb command line option causes mariadb-backup to fail
* [Revision #1ac4d0c168](https://github.com/MariaDB/server/commit/1ac4d0c168)\
  2021-04-09 17:38:21 +0530
  * BtrBulk::table\_name(): Return the table name while displaying table name for fts diagnostics
* [Revision #5a3151bcda](https://github.com/MariaDB/server/commit/5a3151bcda)\
  2021-04-09 12:01:42 +0530
  * Improve diagnostics in order to catch [MDEV-18868](https://jira.mariadb.org/browse/MDEV-18868) and similar bugs
* [Revision #c6d0531cad](https://github.com/MariaDB/server/commit/c6d0531cad)\
  2021-04-08 09:46:56 +0300
  * [MDEV-13467](https://jira.mariadb.org/browse/MDEV-13467) fixup: Improve error handling
* [Revision #72da83ff99](https://github.com/MariaDB/server/commit/72da83ff99)\
  2021-03-30 18:42:28 +0530
  * [MDEV-25019](https://jira.mariadb.org/browse/MDEV-25019) memory allocation failures during startup because server failure in different, confusing ways
* [Revision #82a2ea64b4](https://github.com/MariaDB/server/commit/82a2ea64b4)\
  2021-03-19 17:11:04 +0700
  * Fix postinst trigger when systemd is not running (Closes: #983563)
* [Revision #c32edd7515](https://github.com/MariaDB/server/commit/c32edd7515)\
  2021-04-06 18:51:41 +0530
  * [MDEV-25295](https://jira.mariadb.org/browse/MDEV-25295) Aborted FTS\_DOC\_ID\_INDEX considered as existing FTS\_DOC\_ID\_INDEX during DDL
* [Revision #6fe624b5ac](https://github.com/MariaDB/server/commit/6fe624b5ac)\
  2021-04-03 12:12:15 +0200
  * [MDEV-25242](https://jira.mariadb.org/browse/MDEV-25242) Server crashes in check\_grant upon invoking function with userstat enabled
* [Revision #fb9d151934](https://github.com/MariaDB/server/commit/fb9d151934)\
  2021-04-01 21:47:30 +0200
  * [MDEV-25321](https://jira.mariadb.org/browse/MDEV-25321): mariadb-backup failed if password is passed via environment variable
* [Revision #5bc5ecce08](https://github.com/MariaDB/server/commit/5bc5ecce08)\
  2021-04-01 15:03:59 +0530
  * [MDEV-24197](https://jira.mariadb.org/browse/MDEV-24197): Add "innodb\_force\_recovery" for "mariadb-backup --prepare"
* [Revision #f93e087d74](https://github.com/MariaDB/server/commit/f93e087d74)\
  2021-03-31 11:29:51 +0200
  * [MDEV-25047](https://jira.mariadb.org/browse/MDEV-25047): SIGSEGV in mach\_read\_from\_n\_little\_endian
* [Revision #453bac08c2](https://github.com/MariaDB/server/commit/453bac08c2)\
  2021-03-31 14:26:10 +0200
  * CMake - when searching bison, look also for win\_bison
* [Revision #08cb5d8483](https://github.com/MariaDB/server/commit/08cb5d8483)\
  2021-03-31 14:23:56 +0200
  * [MDEV-25221](https://jira.mariadb.org/browse/MDEV-25221) Do not remove source file, if copy\_file() fails in mariadb-backup --move-back
* [Revision #35ee4aa4e3](https://github.com/MariaDB/server/commit/35ee4aa4e3)\
  2021-03-31 09:06:44 +0300
  * [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103) fixup: Actually fix a crash during IMPORT TABLESPACE
* [Revision #99945d77d7](https://github.com/MariaDB/server/commit/99945d77d7)\
  2021-03-30 09:24:25 +0100
  * [MDEV-25294](https://jira.mariadb.org/browse/MDEV-25294) signal handler display coredump on mac
* [Revision #b771ab242b](https://github.com/MariaDB/server/commit/b771ab242b)\
  2021-03-29 18:51:36 +0530
  * [MDEV-25200](https://jira.mariadb.org/browse/MDEV-25200) Index count mismatch due to aborted FULLTEXT INDEX
* [Revision #108ba4c380](https://github.com/MariaDB/server/commit/108ba4c380)\
  2021-03-30 20:34:39 +0530
  * [MDEV-15527](https://jira.mariadb.org/browse/MDEV-15527) page\_compressed compressed page partially during import tablespace
* [Revision #7c423c26d9](https://github.com/MariaDB/server/commit/7c423c26d9)\
  2021-03-30 16:14:19 +0300
  * Add missing have\_perfschema.inc
* [Revision #c468d5cb50](https://github.com/MariaDB/server/commit/c468d5cb50)\
  2021-03-30 15:18:06 +0530
  * [MDEV-15527](https://jira.mariadb.org/browse/MDEV-15527) page\_compressed compressed page partially during import tablespace
* [Revision #dfda1c9283](https://github.com/MariaDB/server/commit/dfda1c9283)\
  2021-03-30 08:08:21 +0300
  * Add supression for warning.
* [Revision #d217a925b2](https://github.com/MariaDB/server/commit/d217a925b2)\
  2021-03-03 12:14:23 +0200
  * [MDEV-24923](https://jira.mariadb.org/browse/MDEV-24923) : Port selected Galera conflict resolution changes from 10.6
* [Revision #c44273329e](https://github.com/MariaDB/server/commit/c44273329e)\
  2021-03-30 16:18:30 +1100
  * remove broken tests/grant.pl
* [Revision #fb3b2eb517](https://github.com/MariaDB/server/commit/fb3b2eb517)\
  2021-03-30 16:16:24 +1100
  * mallinfo2: whitespace fix
* [Revision #add24e7889](https://github.com/MariaDB/server/commit/add24e7889)\
  2021-03-29 14:32:36 +0200
  * Windows - suppress nonsensical(for this OS) system check.
* [Revision #85b6a81805](https://github.com/MariaDB/server/commit/85b6a81805)\
  2021-01-14 16:55:35 +1100
  * [MDEV-24586](https://jira.mariadb.org/browse/MDEV-24586): remove mysql\_to\_mariadb.sql
* [Revision #4d870b591d](https://github.com/MariaDB/server/commit/4d870b591d)\
  2021-03-15 14:35:08 +0200
  * Don't pass password to innobackup via command line, use environment instead
* [Revision #94dea8ef5b](https://github.com/MariaDB/server/commit/94dea8ef5b)\
  2021-03-27 22:54:18 +0400
  * [MDEV-25457](https://jira.mariadb.org/browse/MDEV-25457) CREATE / DROP PROCEDURE not logged with audit plugin.
* [Revision #c0ca3c4ffa](https://github.com/MariaDB/server/commit/c0ca3c4ffa)\
  2021-03-26 18:01:10 +0700
  * [MDEV-25240](https://jira.mariadb.org/browse/MDEV-25240) minor upgrade does not perform server restart
* [Revision #2fc76a5022](https://github.com/MariaDB/server/commit/2fc76a5022)\
  2021-03-27 21:02:09 +0100
  * [MDEV-13467](https://jira.mariadb.org/browse/MDEV-13467): Feature request: Support for ST\_Distance\_Sphere()
* [Revision #5eda18f0ca](https://github.com/MariaDB/server/commit/5eda18f0ca)\
  2021-03-27 10:54:57 +0100
  * [MDEV-25272](https://jira.mariadb.org/browse/MDEV-25272): Wrong function name in error messages upon ST\_GeomFromGeoJSON call
* [Revision #6769d1a078](https://github.com/MariaDB/server/commit/6769d1a078)\
  2020-10-29 01:40:31 +0100
  * [MDEV-13467](https://jira.mariadb.org/browse/MDEV-13467): Feature request: Support for ST\_Distance\_Sphere()
* [Revision #48141f3c17](https://github.com/MariaDB/server/commit/48141f3c17)\
  2021-03-26 20:48:59 +0100
  * Replace mallinfo with mallinfo2 on supported systems
* [Revision #36a05268e7](https://github.com/MariaDB/server/commit/36a05268e7)\
  2021-03-24 13:17:49 +0300
  * cmake cleanup: drop support for ancient clang in WITH\_ASAN option
* [Revision #dfae51de36](https://github.com/MariaDB/server/commit/dfae51de36)\
  2021-03-24 13:15:03 +0300
  * [MDEV-25238](https://jira.mariadb.org/browse/MDEV-25238) add support for -fsanitize-address-use-after-scope
* [Revision #a6d66fe75e](https://github.com/MariaDB/server/commit/a6d66fe75e)\
  2021-03-26 14:12:39 +0200
  * [MDEV-24786](https://jira.mariadb.org/browse/MDEV-24786): row\_upd\_clust\_step() skips mtr\_t::commit() on virtual column error
* [Revision #da26e2e673](https://github.com/MariaDB/server/commit/da26e2e673)\
  2021-03-25 08:41:27 +0100
  * Cleanup - reduce duplicate code, in SSL IO error handling.
* [Revision #5a79807119](https://github.com/MariaDB/server/commit/5a79807119)\
  2021-03-24 23:12:16 +0100
  * [MDEV-25242](https://jira.mariadb.org/browse/MDEV-25242) Server crashes in check\_grant upon invoking function with userstat enabled
* [Revision #cdb86faf82](https://github.com/MariaDB/server/commit/cdb86faf82)\
  2021-03-24 08:55:36 +0100
  * [MDEV-23740](https://jira.mariadb.org/browse/MDEV-23740) postfix - potentially uninitialized variable passed to vio\_socket\_io\_wait.
* [Revision #c4807c107a](https://github.com/MariaDB/server/commit/c4807c107a)\
  2021-03-23 21:53:27 +0100
  * [MDEV-24879](https://jira.mariadb.org/browse/MDEV-24879) Client crash on undefined charsetsdir
* [Revision #3dae564703](https://github.com/MariaDB/server/commit/3dae564703)\
  2021-03-22 11:36:33 +0100
  * Follow up fixes for making @@wsrep\_provider read-only
* [Revision #9e57bd278f](https://github.com/MariaDB/server/commit/9e57bd278f)\
  2021-03-23 12:37:55 +0700
  * fixed typo in postinst script
* [Revision #8f7a6cde58](https://github.com/MariaDB/server/commit/8f7a6cde58)\
  2021-03-22 22:04:54 -0700
  * [MDEV-24767](https://jira.mariadb.org/browse/MDEV-24767) Wrong result when forced BNLH is used for join supported by compound index
* [Revision #56274bd5e4](https://github.com/MariaDB/server/commit/56274bd5e4)\
  2021-03-22 18:11:44 +0200
  * [MDEV-23076](https://jira.mariadb.org/browse/MDEV-23076) Misleading "InnoDB: using atomic writes"
* [Revision #0f8caadc96](https://github.com/MariaDB/server/commit/0f8caadc96)\
  2021-03-22 17:46:49 +0200
  * [MDEV-22653](https://jira.mariadb.org/browse/MDEV-22653): Remove the useless parameter innodb\_simulate\_comp\_failures
* [Revision #0e96570171](https://github.com/MariaDB/server/commit/0e96570171)\
  2021-03-22 18:55:59 +0700
  * Added missed ' -- ' between the end of the lldb command options and the beginning of the arguments.
* [Revision #b58b289827](https://github.com/MariaDB/server/commit/b58b289827)\
  2021-03-19 10:56:10 +1100
  * [MDEV-25195](https://jira.mariadb.org/browse/MDEV-25195): pam check getgrouplist function
* [Revision #209e8ecf9a](https://github.com/MariaDB/server/commit/209e8ecf9a)\
  2021-03-20 10:46:43 +0200
  * [MDEV-22240](https://jira.mariadb.org/browse/MDEV-22240): don't use pc.splitbrain=true on node2 in galera.galera\_gcache\_recover
* [Revision #96dd4b53c1](https://github.com/MariaDB/server/commit/96dd4b53c1)\
  2021-03-19 16:10:33 +0200
  * [MDEV-8708](https://jira.mariadb.org/browse/MDEV-8708) fixup: Remove dead code
* [Revision #a74fa579b9](https://github.com/MariaDB/server/commit/a74fa579b9)\
  2021-03-19 03:24:55 +0100
  * [MDEV-24903](https://jira.mariadb.org/browse/MDEV-24903): mariadb-backup SST fails while adding --log-bin in startup command
* [Revision #4e825b0e8a](https://github.com/MariaDB/server/commit/4e825b0e8a)\
  2021-03-19 11:46:07 +0100
  * update libmariadb
* [Revision #4ca4d606ac](https://github.com/MariaDB/server/commit/4ca4d606ac)\
  2021-03-19 11:14:47 +1100
  * myseek: AIX has no "tell"
* [Revision #b34bb81eaf](https://github.com/MariaDB/server/commit/b34bb81eaf)\
  2021-03-15 22:48:30 -0700
  * [MDEV-25112](https://jira.mariadb.org/browse/MDEV-25112) MIN/MAX aggregation over an indexed column may return wrong result
* [Revision #c557e9540a](https://github.com/MariaDB/server/commit/c557e9540a)\
  2021-03-18 12:22:11 +0200
  * [MDEV-10682](https://jira.mariadb.org/browse/MDEV-10682) Race condition between ANALYZE and STATS\_AUTO\_RECALC
* [Revision #6505662c23](https://github.com/MariaDB/server/commit/6505662c23)\
  2021-03-18 12:18:16 +0200
  * [MDEV-25121](https://jira.mariadb.org/browse/MDEV-25121): innodb\_flush\_method=O\_DIRECT fails on compressed tables
* [Revision #00f620b27e](https://github.com/MariaDB/server/commit/00f620b27e)\
  2021-03-17 12:12:10 +0100
  * [MDEV-21584](https://jira.mariadb.org/browse/MDEV-21584) - portability fix
* [Revision #14a8b700f3](https://github.com/MariaDB/server/commit/14a8b700f3)\
  2021-03-17 14:09:05 +0200
  * Cleanup: Remove unused OS\_DATA\_TEMP\_FILE
* [Revision #c9ba668992](https://github.com/MariaDB/server/commit/c9ba668992)\
  2021-03-16 13:02:44 +0200
  * [MDEV-24916](https://jira.mariadb.org/browse/MDEV-24916) : Assertion \`current\_stmt\_binlog\_format == BINLOG\_FORMAT\_STMT || current\_stmt\_binlog\_format == BINLOG\_FORMAT\_ROW' failed in THD::is\_current\_stmt\_binlog\_format\_row
* [Revision #f4e14f0e24](https://github.com/MariaDB/server/commit/f4e14f0e24)\
  2021-03-17 12:58:32 +0200
  * [MDEV-18874](https://jira.mariadb.org/browse/MDEV-18874) : Galera test MW-286 causes Mutex = TTASEventMutex]: Assertion \`!is\_owned()' failed. assertion
* [Revision #6974058121](https://github.com/MariaDB/server/commit/6974058121)\
  2021-03-18 14:35:52 +1100
  * mariadb.pc: plugindir is used
* [Revision #66106130a6](https://github.com/MariaDB/server/commit/66106130a6)\
  2021-03-17 11:01:15 +0300
  * switch off storage/innobase/.clang-format: InnoDB uses a common formatting style for all new code
* [Revision #bf303e824c](https://github.com/MariaDB/server/commit/bf303e824c)\
  2021-02-17 04:45:53 +0100
  * [MDEV-21039](https://jira.mariadb.org/browse/MDEV-21039): Server fails to start with unknown mysqld\_safe options
* [Revision #f2c79eda4b](https://github.com/MariaDB/server/commit/f2c79eda4b)\
  2021-03-16 00:15:34 +0100
  * [MDEV-24554](https://jira.mariadb.org/browse/MDEV-24554) Windows authenticode signing stopped working
* [Revision #987cfa227d](https://github.com/MariaDB/server/commit/987cfa227d)\
  2020-10-12 21:15:24 +0200
  * [MDEV-23740](https://jira.mariadb.org/browse/MDEV-23740) - X509\_R\_CERT\_ALREADY\_IN\_HASH\_TABLE when establishing SSL connection connection.
* [Revision #30dea4599e](https://github.com/MariaDB/server/commit/30dea4599e)\
  2021-03-04 14:28:50 +0200
  * [MDEV-24978](https://jira.mariadb.org/browse/MDEV-24978) : SIGABRT in libc\_message
* [Revision #ba7d86a659](https://github.com/MariaDB/server/commit/ba7d86a659)\
  2021-03-12 10:35:08 +0100
  * update libmariadb
* [Revision #390de205cc](https://github.com/MariaDB/server/commit/390de205cc)\
  2021-02-26 20:38:20 +0530
  * [MDEV-24519](https://jira.mariadb.org/browse/MDEV-24519): Server crashes in Charset::set\_charset upon SELECT
* [Revision #1f3f90318f](https://github.com/MariaDB/server/commit/1f3f90318f)\
  2021-03-10 11:52:06 +0200
  * Update sponsors
* [Revision #374ec82f08](https://github.com/MariaDB/server/commit/374ec82f08)\
  2021-03-09 15:11:44 -0800
  * [MDEV-24597](https://jira.mariadb.org/browse/MDEV-24597) Explicit column name error in CTE of UNION
* [Revision #90780bb5a9](https://github.com/MariaDB/server/commit/90780bb5a9)\
  2021-03-10 17:26:43 -0800
  * [MDEV-21104](https://jira.mariadb.org/browse/MDEV-21104) Wrong result (extra rows and wrong values) with incremental BNLH
* [Revision #1af8558193](https://github.com/MariaDB/server/commit/1af8558193)\
  2021-03-10 11:08:51 +0200
  * [MDEV-25101](https://jira.mariadb.org/browse/MDEV-25101) Assertion !strcmp(field->name, "table\_name") failed
* [Revision #ee12b055ff](https://github.com/MariaDB/server/commit/ee12b055ff)\
  2021-03-01 14:29:29 +0100
  * reenable tests from engines/funcs
* [Revision #4020e4aee0](https://github.com/MariaDB/server/commit/4020e4aee0)\
  2021-03-04 23:02:47 -0800
  * [MDEV-25002](https://jira.mariadb.org/browse/MDEV-25002) ON expressions cannot contain outer references
* [Revision #dc6667805d](https://github.com/MariaDB/server/commit/dc6667805d)\
  2021-03-07 01:33:51 +0100
  * Correct the value of global memory\_used
* [Revision #2c0b3141f3](https://github.com/MariaDB/server/commit/2c0b3141f3)\
  2021-03-08 14:53:54 +0100
  * update wsrep service version after 7345d371418
* [Revision #7345d37141](https://github.com/MariaDB/server/commit/7345d37141)\
  2021-03-08 05:03:06 +0100
  * [MDEV-24853](https://jira.mariadb.org/browse/MDEV-24853): Duplicate key generated during cluster configuration change
* [Revision #545cba13eb](https://github.com/MariaDB/server/commit/545cba13eb)\
  2021-03-04 23:09:22 +0100
  * [MDEV-22929](https://jira.mariadb.org/browse/MDEV-22929) fixup. Print "completed OK!" if page corruption and --log-innodb-page-corruption
* [Revision #7759991a06](https://github.com/MariaDB/server/commit/7759991a06)\
  2021-03-04 18:11:25 +0200
  * fixup 58b56f14a096285a0e51b2233fc35398f1b01f5a: Remove dead code
* [Revision #978e48c96c](https://github.com/MariaDB/server/commit/978e48c96c)\
  2021-03-04 17:15:38 +0200
  * [MDEV-25051](https://jira.mariadb.org/browse/MDEV-25051) Race condition between persistent statistics and RENAME TABLE or TRUNCATE
* [Revision #5da6ffe227](https://github.com/MariaDB/server/commit/5da6ffe227)\
  2021-03-02 15:37:12 +0200
  * [MDEV-25032](https://jira.mariadb.org/browse/MDEV-25032): Window functions without column references get removed from ORDER BY
* [Revision #b044898b97](https://github.com/MariaDB/server/commit/b044898b97)\
  2021-03-01 21:16:13 +0530
  * [MDEV-24748](https://jira.mariadb.org/browse/MDEV-24748) extern column check missing in btr\_index\_rec\_validate()
* [Revision #f080863501](https://github.com/MariaDB/server/commit/f080863501)\
  2021-03-03 15:37:03 +0530
  * [MDEV-20648](https://jira.mariadb.org/browse/MDEV-20648) InnoDB: Failing assertion: !(\*node)->being\_extended, innodb.log\_data\_file\_size failed in buildbot, assertion \`!space->is\_stopping()'
* [Revision #676987c4a1](https://github.com/MariaDB/server/commit/676987c4a1)\
  2021-03-02 14:08:38 +0200
  * [MDEV-24532](https://jira.mariadb.org/browse/MDEV-24532) Table corruption ER\_NO\_SUCH\_TABLE\_IN\_ENGINE .. on table with foreign key
* [Revision #fc77431624](https://github.com/MariaDB/server/commit/fc77431624)\
  2021-03-02 19:09:44 +0700
  * [MDEV-25006](https://jira.mariadb.org/browse/MDEV-25006): Failed assertion on executing EXPLAIN DELETE statement as a prepared statement
* [Revision #dd9e5827a6](https://github.com/MariaDB/server/commit/dd9e5827a6)\
  2021-02-25 14:10:25 +0100
  * mtr --gdb: fix for --rr and for a warning
* [Revision #259e5243fa](https://github.com/MariaDB/server/commit/259e5243fa)\
  2021-02-25 14:20:11 +0700
  * [MDEV-24860](https://jira.mariadb.org/browse/MDEV-24860): Incorrect behaviour of SET STATEMENT in case it is executed as a prepared statement
* [Revision #0a95c922c8](https://github.com/MariaDB/server/commit/0a95c922c8)\
  2021-02-25 12:42:01 +0530
  * Fixed the innodb\_ext\_key test by adding replace\_column
* [Revision #577c970c52](https://github.com/MariaDB/server/commit/577c970c52)\
  2021-01-29 09:37:22 +1100
  * [MDEV-24728](https://jira.mariadb.org/browse/MDEV-24728): Debian include client caching\_sha2\_password plugin
* [Revision #1635686b50](https://github.com/MariaDB/server/commit/1635686b50)\
  2021-02-15 12:31:31 +1100
  * [MDEV-23510](https://jira.mariadb.org/browse/MDEV-23510): arm64 lf\_hash alignment of pointers
* [Revision #9e259d58c2](https://github.com/MariaDB/server/commit/9e259d58c2)\
  2021-02-18 15:30:03 +0200
  * Remove race condition during `make dist`
* [Revision #787c47586e](https://github.com/MariaDB/server/commit/787c47586e)\
  2021-02-23 13:55:39 +0530
  * [MDEV-24913](https://jira.mariadb.org/browse/MDEV-24913) Assertion !recv\_no\_log\_write in log\_write\_up\_to()
* [Revision #3c021485c9](https://github.com/MariaDB/server/commit/3c021485c9)\
  2021-02-19 16:54:58 +0100
  * fix binlog\_xa\_recover test
* [Revision #bb98c6bf44](https://github.com/MariaDB/server/commit/bb98c6bf44)\
  2021-02-19 16:48:19 +0100
  * cleanup: renames, no need to create a new .inc file
* [Revision #7fe351aba4](https://github.com/MariaDB/server/commit/7fe351aba4)\
  2021-02-03 16:59:26 +0100
  * mtr fixes for old (5.10.1) perl
* [Revision #77c23c62ae](https://github.com/MariaDB/server/commit/77c23c62ae)\
  2021-01-26 11:56:17 +0100
  * support for mtr --valgdb
* [Revision #feacc0aaf2](https://github.com/MariaDB/server/commit/feacc0aaf2)\
  2021-01-25 13:16:04 +0100
  * unify mtr handling of debuggers
* [Revision #3b0b4e614c](https://github.com/MariaDB/server/commit/3b0b4e614c)\
  2021-01-24 21:57:37 +0100
  * cleanup: remove dead code in mtr
* [Revision #c4f0133444](https://github.com/MariaDB/server/commit/c4f0133444)\
  2021-02-01 13:16:40 +0100
  * cleanup: stat tables
* [Revision #06a791aa12](https://github.com/MariaDB/server/commit/06a791aa12)\
  2021-02-01 13:01:12 +0100
  * [MDEV-23753](https://jira.mariadb.org/browse/MDEV-23753): SIGSEGV in Column\_stat::store\_stat\_fields
* [Revision #caad32ca92](https://github.com/MariaDB/server/commit/caad32ca92)\
  2021-02-01 12:57:14 +0100
  * Revert "[MDEV-23753](https://jira.mariadb.org/browse/MDEV-23753): SIGSEGV in Column\_stat::store\_stat\_fields"
* Merge [Revision #a638f1577a](https://github.com/MariaDB/server/commit/a638f1577a) 2021-02-22 18:43:03 +0100 - Merge branch 'bb-10.2-release' into 10.2
* [Revision #6aa909745d](https://github.com/MariaDB/server/commit/6aa909745d)\
  2021-02-22 10:04:25 -0500
  * bump the VERSION
* [Revision #d7fc4f5236](https://github.com/MariaDB/server/commit/d7fc4f5236)\
  2021-02-22 18:07:15 +0530
  * [MDEV-24863](https://jira.mariadb.org/browse/MDEV-24863) AHI entries mismatch with the index while reloading the evicted tables.
* [Revision #374f4c3f8c](https://github.com/MariaDB/server/commit/374f4c3f8c)\
  2021-02-18 10:09:30 +0200
  * Suppress warning on galera\_ssl\_upgrade test.
* [Revision #5ecaf52d42](https://github.com/MariaDB/server/commit/5ecaf52d42)\
  2021-02-16 12:19:19 +0200
  * [MDEV-24873](https://jira.mariadb.org/browse/MDEV-24873) : galera.galera\_as\_slave\_ctas MTR failed: Assertion \`(&(\&LOCK\_thd\_data)->m\_mutex)->count > 0 && pthread\_equal(pthread\_self(), (&(\&LOCK\_thd\_data)->m\_mutex)->thread)' failed in sql\_class.cc on THD::awake(killed\_state)
* [Revision #45e33e05e2](https://github.com/MariaDB/server/commit/45e33e05e2)\
  2021-02-16 12:05:45 +0200
  * [MDEV-24872](https://jira.mariadb.org/browse/MDEV-24872) : galera.galera\_insert\_multi MTR failed: crash with SIGABRT
* [Revision #4d300ab1a8](https://github.com/MariaDB/server/commit/4d300ab1a8)\
  2021-02-16 11:52:50 +0200
  * [MDEV-24867](https://jira.mariadb.org/browse/MDEV-24867) : wsrep.variables MTR failed: Result length mismatch
* [Revision #067465cd2f](https://github.com/MariaDB/server/commit/067465cd2f)\
  2021-02-16 12:07:48 +0200
  * [MDEV-15641](https://jira.mariadb.org/browse/MDEV-15641) fixup: Make the test faster
* [Revision #3544643f09](https://github.com/MariaDB/server/commit/3544643f09)\
  2021-02-15 16:30:55 +0530
  * [MDEV-23291](https://jira.mariadb.org/browse/MDEV-23291): SUM column from a derived table returns invalid values
* [Revision #7e9a6b7f09](https://github.com/MariaDB/server/commit/7e9a6b7f09)\
  2021-02-15 16:28:44 +0530
  * [MDEV-24779](https://jira.mariadb.org/browse/MDEV-24779): main.subselect fails in buildbot with --ps-protocol
* [Revision #a461e4d306](https://github.com/MariaDB/server/commit/a461e4d306)\
  2021-02-09 20:27:21 +0530
  * [MDEV-19474](https://jira.mariadb.org/browse/MDEV-19474): Histogram statistics are used even with optimizer\_use\_condition\_selectivity=3
* [Revision #e926964cb8](https://github.com/MariaDB/server/commit/e926964cb8)\
  2021-02-15 18:04:17 +0200
  * Remove useless test innodb.innodb\_bug60049
* [Revision #6f14230643](https://github.com/MariaDB/server/commit/6f14230643)\
  2021-02-15 13:41:44 +0100
  * [MDEV-11862](https://jira.mariadb.org/browse/MDEV-11862) rpl.rpl\_semi\_sync\_event\_after\_sync 'fails if there is no semisync plugin
* [Revision #da3211e487](https://github.com/MariaDB/server/commit/da3211e487)\
  2021-02-12 14:03:25 +0200
  * [MDEV-24763](https://jira.mariadb.org/browse/MDEV-24763) fixup: Use deterministic ORDER BY
* [Revision #6f3f191cfa](https://github.com/MariaDB/server/commit/6f3f191cfa)\
  2021-02-12 09:48:36 +0200
  * [MDEV-24763](https://jira.mariadb.org/browse/MDEV-24763) ALTER TABLE fails to rename a column in SYS\_FIELDS
* [Revision #028ba10d0b](https://github.com/MariaDB/server/commit/028ba10d0b)\
  2021-02-12 09:41:15 +0200
  * [MDEV-18468](https://jira.mariadb.org/browse/MDEV-18468) fixup: Make test case robust w.r.t. deferred DROP TABLE
* [Revision #95003eab45](https://github.com/MariaDB/server/commit/95003eab45)\
  2021-02-10 14:04:25 +0100
  * [MDEV-19950](https://jira.mariadb.org/browse/MDEV-19950): Galera test failure on galera\_ssl\_upgrade
* [Revision #362dcf9e01](https://github.com/MariaDB/server/commit/362dcf9e01)\
  2021-02-11 08:02:24 +0200
  * Update Galera disabled.def
* [Revision #afc5bac49d](https://github.com/MariaDB/server/commit/afc5bac49d)\
  2021-02-05 19:50:05 +0400
  * [MDEV-24790](https://jira.mariadb.org/browse/MDEV-24790) CAST('0e1111111111' AS DECIMAL(38,0)) returns a wrong result
* [Revision #739abf5195](https://github.com/MariaDB/server/commit/739abf5195)\
  2021-02-07 14:31:48 +0200
  * Make innodb\_gis.rtree\_purge run faster
* [Revision #eef4c5d378](https://github.com/MariaDB/server/commit/eef4c5d378)\
  2021-01-18 14:00:13 +0530
  * [MDEV-22741](https://jira.mariadb.org/browse/MDEV-22741): \*SAN: ERROR: AddressSanitizer: use-after-poison on address in instrings/strmake.c:36 from change\_master (on optimized builds)
* [Revision #6ede84f477](https://github.com/MariaDB/server/commit/6ede84f477)\
  2021-02-02 10:28:31 +0100
  * [MDEV-24762](https://jira.mariadb.org/browse/MDEV-24762) - HeidiSQL 11.2
* [Revision #ceb3976191](https://github.com/MariaDB/server/commit/ceb3976191)\
  2021-02-01 17:59:38 +0530
  * Updating test results in rocksdb test suite after [MDEV-11172](https://jira.mariadb.org/browse/MDEV-11172) is fixed
* [Revision #26f5033555](https://github.com/MariaDB/server/commit/26f5033555)\
  2021-01-31 19:55:07 +0530
  * [MDEV-23449](https://jira.mariadb.org/browse/MDEV-23449): alias do not exist and a query do not report an error
* [Revision #072b39da66](https://github.com/MariaDB/server/commit/072b39da66)\
  2021-01-30 22:36:51 +0530
  * [MDEV-22583](https://jira.mariadb.org/browse/MDEV-22583): Selectivity for BIT columns in filtered column for EXPLAIN is incorrect
* [Revision #b87c342da5](https://github.com/MariaDB/server/commit/b87c342da5)\
  2021-01-29 00:27:19 +0530
  * [MDEV-11172](https://jira.mariadb.org/browse/MDEV-11172): EXPLAIN shows non-sensical value for key\_len with type=index
* [Revision #0921656734](https://github.com/MariaDB/server/commit/0921656734)\
  2021-01-28 23:29:43 +0200
  * Skip TokuDB within autobake-deb.sh
* [Revision #a4d4836f2b](https://github.com/MariaDB/server/commit/a4d4836f2b)\
  2021-01-29 19:31:07 +0200
  * List of unstable tests for 10.2.37 release

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
