# MariaDB 10.2.40 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download 10.2.40](https://downloads.mariadb.org/mariadb/10.2.40/)[Release Notes](../../old-releases/10.2/10.2.40.md)[Changelog](mariadb-10240-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 6 Aug 2021

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.40.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #b549af6913](https://github.com/MariaDB/server/commit/b549af6913)\
  2021-07-23 14:16:34 +0300
  * [MDEV-26220](https://jira.mariadb.org/browse/MDEV-26220) Server crashes with indexed by prefix virtual column
* [Revision #8b6c8a6ce9](https://github.com/MariaDB/server/commit/8b6c8a6ce9)\
  2021-08-02 10:30:18 +0200
  * Revert "[MDEV-26220](https://jira.mariadb.org/browse/MDEV-26220) Server crashes with indexed by prefix virtual column"
* [Revision #2cdf8a9327](https://github.com/MariaDB/server/commit/2cdf8a9327)\
  2021-07-31 08:48:14 +0200
  * [MDEV-23752](https://jira.mariadb.org/browse/MDEV-23752) SHOW EXPLAIN FOR thd waits for sleep
* [Revision #22709897b0](https://github.com/MariaDB/server/commit/22709897b0)\
  2021-07-06 10:17:22 +0300
  * [MDEV-20154](https://jira.mariadb.org/browse/MDEV-20154) Assertion `len <= col->len | ...` failed in row\_merge\_buf\_add
* [Revision #0e8981ef93](https://github.com/MariaDB/server/commit/0e8981ef93)\
  2021-07-29 09:15:03 +0300
  * Cleanup: Remove redundant conditions
* [Revision #9b8e207ce0](https://github.com/MariaDB/server/commit/9b8e207ce0)\
  2021-07-28 11:07:49 +0200
  * [MDEV-26220](https://jira.mariadb.org/browse/MDEV-26220) Server crashes with indexed by prefix virtual column Server crashes in Field::register\_field\_in\_read\_map upon select from partitioned table with indexed by prefix virtual column.
* [Revision #fb8be6a631](https://github.com/MariaDB/server/commit/fb8be6a631)\
  2021-07-28 09:40:20 +0300
  * Cleanup: Remove dead code
* [Revision #dfadc90303](https://github.com/MariaDB/server/commit/dfadc90303)\
  2021-07-27 18:56:00 +0200
  * latest C/C
* [Revision #65e3d08538](https://github.com/MariaDB/server/commit/65e3d08538)\
  2021-07-27 19:21:39 +0200
  * [MDEV-7209](https://jira.mariadb.org/browse/MDEV-7209) mroonga storage engine fails to build on OpenBSD
* Merge [Revision #aaac2477ca](https://github.com/MariaDB/server/commit/aaac2477ca) 2021-07-27 18:51:32 +0200 - Merge remote-tracking branch 'merge/merge-pcre' into 10.2
* [Revision #4683ce82d2](https://github.com/MariaDB/server/commit/4683ce82d2)\
  2021-07-27 18:45:35 +0200
  * 8.45
* Merge [Revision #a32373b65a](https://github.com/MariaDB/server/commit/a32373b65a) 2021-07-27 18:25:42 +0200 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #fc98a6d54a](https://github.com/MariaDB/server/commit/fc98a6d54a)\
  2021-07-24 18:31:59 +0200
  * Fix compile error for centos 74
* [Revision #5049887c8d](https://github.com/MariaDB/server/commit/5049887c8d)\
  2021-07-24 18:24:20 +0200
  * Replace Mongo2.jar and Mongo3.jar with ne versions
* [Revision #0f18135ec8](https://github.com/MariaDB/server/commit/0f18135ec8)\
  2021-07-24 16:28:57 +0200
  * Make user variable prefix recognized by IsArgJson and IsJson
* [Revision #1c4b917f0e](https://github.com/MariaDB/server/commit/1c4b917f0e)\
  2021-06-25 18:35:26 +0200
  * Fix clang compile error in value.cpp
* [Revision #7863554e42](https://github.com/MariaDB/server/commit/7863554e42)\
  2021-06-25 12:54:34 +0200
  * Fix clang compile error in tabjson and typo in tabbson.cpp
* [Revision #af7a0895ac](https://github.com/MariaDB/server/commit/af7a0895ac)\
  2021-06-25 12:30:10 +0200
  * Fix clang compile error in tabjson.cpp and tabbson.cpp
* [Revision #6239e2a4ec](https://github.com/MariaDB/server/commit/6239e2a4ec)\
  2021-06-25 11:38:16 +0200
  * Fix clang compile error in tabjson.cpp and tabbson.cpp
* [Revision #5c5d60b897](https://github.com/MariaDB/server/commit/5c5d60b897)\
  2021-06-25 01:15:51 +0200
  * Fix compile error in value.h and remove unused variables in ha\_connect.cc
* [Revision #330b32ebd9](https://github.com/MariaDB/server/commit/330b32ebd9)\
  2021-06-24 23:56:13 +0200
  * Fix clang compile error
* [Revision #ed70f76cf7](https://github.com/MariaDB/server/commit/ed70f76cf7)\
  2021-06-24 00:46:12 +0200
  * Make function strz return null when LEX\_STRING is null
* [Revision #5f64276fb2](https://github.com/MariaDB/server/commit/5f64276fb2)\
  2021-06-08 17:44:43 +0200
  * Fix [MDEV-25863](https://jira.mariadb.org/browse/MDEV-25863) : Replace WIN by \_WIN32
* [Revision #be7e41db96](https://github.com/MariaDB/server/commit/be7e41db96)\
  2021-05-24 16:56:12 +0200
  * Mongo defined columns
* [Revision #e0edfc277f](https://github.com/MariaDB/server/commit/e0edfc277f)\
  2021-05-18 16:42:19 +0200
  * Fix [MDEV-25715](https://jira.mariadb.org/browse/MDEV-25715)
* [Revision #17533c1ffc](https://github.com/MariaDB/server/commit/17533c1ffc)\
  2021-05-17 19:17:31 +0200
  * Put all jar files in the SHARE directory (was PLUGIN)
* [Revision #5ae67c6d63](https://github.com/MariaDB/server/commit/5ae67c6d63)\
  2021-05-05 00:31:21 +0200
  * All this concern Json or Mongo tables based on MongoDB collections.
  * Limit decimals of doubles printed from MongoDB Done in function Mini for Mongo C Driver and Java Driver Done in function SerializeValue for Java tables using the J Driver
* [Revision #3b5dabeb96](https://github.com/MariaDB/server/commit/3b5dabeb96)\
  2021-05-02 11:59:54 +0200
  * Typo
* [Revision #2294f9de8d](https://github.com/MariaDB/server/commit/2294f9de8d)\
  2021-05-02 11:03:21 +0200
  * Fix compile warning as error
* [Revision #ef0829ef40](https://github.com/MariaDB/server/commit/ef0829ef40)\
  2021-05-01 22:29:38 +0200
  * Major update of the json/bson/mongo table types programs. Fix several bugs, chiefly concerning CURL operations
* [Revision #afe00bb7cc](https://github.com/MariaDB/server/commit/afe00bb7cc)\
  2021-07-27 10:44:01 +0300
  * [MDEV-25998](https://jira.mariadb.org/browse/MDEV-25998) fixup: Avoid a hang
* [Revision #e11cae71fe](https://github.com/MariaDB/server/commit/e11cae71fe)\
  2021-07-27 09:26:24 +0300
  * [MDEV-25998](https://jira.mariadb.org/browse/MDEV-25998) fixup: Assert that a mutex is being held
* [Revision #da094188f6](https://github.com/MariaDB/server/commit/da094188f6)\
  2021-07-27 08:52:59 +0300
  * [MDEV-24393](https://jira.mariadb.org/browse/MDEV-24393) InnoDB disregards --skip-external-locking
* [Revision #cf1fc59856](https://github.com/MariaDB/server/commit/cf1fc59856)\
  2021-07-27 08:52:01 +0300
  * [MDEV-25594](https://jira.mariadb.org/browse/MDEV-25594): Improve debug checks
* [Revision #0bd9f755b7](https://github.com/MariaDB/server/commit/0bd9f755b7)\
  2021-07-02 08:56:23 +0300
  * [MDEV-26062](https://jira.mariadb.org/browse/MDEV-26062) : InnoDB: WSREP: referenced FK check fail: Lock wait index `PRIMARY` table `schema`.`child_table`
* [Revision #ce870b2a2a](https://github.com/MariaDB/server/commit/ce870b2a2a)\
  2021-07-26 14:19:26 +0530
  * [MDEV-25998](https://jira.mariadb.org/browse/MDEV-25998) InnoDB removes the tablespace from default encrypt list early
* [Revision #0711a53a33](https://github.com/MariaDB/server/commit/0711a53a33)\
  2021-07-26 12:35:48 +0300
  * fix clang build: check alignment the other way
* [Revision #af0b26f9b7](https://github.com/MariaDB/server/commit/af0b26f9b7)\
  2020-12-08 16:05:07 +0530
  * [MDEV-23786](https://jira.mariadb.org/browse/MDEV-23786): Assertion \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed for TokuDB engine CREATE TABLE
* [Revision #f29b3d6d82](https://github.com/MariaDB/server/commit/f29b3d6d82)\
  2021-07-24 21:32:52 +0300
  * Some tests can take very long time when run with valgrind
* [Revision #173e562dc2](https://github.com/MariaDB/server/commit/173e562dc2)\
  2021-07-23 17:20:57 +0300
  * [MDEV-26228](https://jira.mariadb.org/browse/MDEV-26228) ASAN heap-use-after-free with ON UPDATE CASCADE
* [Revision #4c4237e63f](https://github.com/MariaDB/server/commit/4c4237e63f)\
  2021-07-23 08:21:28 +0200
  * [MDEV-26080](https://jira.mariadb.org/browse/MDEV-26080) fixup: fixed .result file for galera\_roles test (one word must be enclosed in single quotes).
* [Revision #2820ad1c22](https://github.com/MariaDB/server/commit/2820ad1c22)\
  2021-07-22 17:07:17 -0700
  * [MDEV-26202](https://jira.mariadb.org/browse/MDEV-26202) Unexpected failure with query using indirectly a recursive CTE twice
* Merge [Revision #742b3a0d39](https://github.com/MariaDB/server/commit/742b3a0d39) 2021-07-22 18:07:37 +0300 - [MDEV-26205](https://jira.mariadb.org/browse/MDEV-26205) Merge new release of InnoDB 5.7.35 to 10.2
* [Revision #236f825ebf](https://github.com/MariaDB/server/commit/236f825ebf)\
  2021-05-26 18:36:16 +0530
  * Bug #31576731 INNODB\_FT\_TOTAL\_CACHE\_SIZE NOT CAPPED WHEN SET TO 32000000
* [Revision #c4295b9be9](https://github.com/MariaDB/server/commit/c4295b9be9)\
  2021-03-18 15:56:36 +0100
  * Bug #32460315 ONLINE RESIZING BUFFER POOL CAN CRASH CONCURRENT BP LOOKUP
* [Revision #efae374efa](https://github.com/MariaDB/server/commit/efae374efa)\
  2021-07-22 17:55:05 +0300
  * [MDEV-26203](https://jira.mariadb.org/browse/MDEV-26203) CREATE INDEX may enforce incorrect maximum column length
* [Revision #8ad6971a1a](https://github.com/MariaDB/server/commit/8ad6971a1a)\
  2021-07-22 17:54:49 +0300
  * Update libmariadb
* [Revision #124dc0d85b](https://github.com/MariaDB/server/commit/124dc0d85b)\
  2021-07-22 17:53:43 +0300
  * [MDEV-25361](https://jira.mariadb.org/browse/MDEV-25361) fixup: Fix integer type mismatch
* [Revision #b30f26e3fe](https://github.com/MariaDB/server/commit/b30f26e3fe)\
  2021-07-22 09:19:18 +0200
  * Record tempfiles\_encrypted test failure
* [Revision #4aeb2b1c6c](https://github.com/MariaDB/server/commit/4aeb2b1c6c)\
  2021-07-20 23:14:43 -0700
  * [MDEV-26189](https://jira.mariadb.org/browse/MDEV-26189) Missing handling of unknown column in WHERE of recursive CTE
* [Revision #bd711d4f3d](https://github.com/MariaDB/server/commit/bd711d4f3d)\
  2021-07-21 10:30:01 +0300
  * Typo fixes in item\_strfunc.cc
* [Revision #751ebe44fd](https://github.com/MariaDB/server/commit/751ebe44fd)\
  2017-08-09 21:39:18 +0200
  * Add feature summary at the end of cmake.
* [Revision #2b017367c7](https://github.com/MariaDB/server/commit/2b017367c7)\
  2021-07-13 16:18:53 +0300
  * Delete unused MYSQL\_CHECK\_{LZ4|LZO}\_STATIC macros
* [Revision #4c387945f0](https://github.com/MariaDB/server/commit/4c387945f0)\
  2021-07-09 18:56:34 -0700
  * [MDEV-25565](https://jira.mariadb.org/browse/MDEV-25565) Crash on 2-nd execution of SP/PS for query calculating window functions from view
* [Revision #872422dcbb](https://github.com/MariaDB/server/commit/872422dcbb)\
  2021-07-20 00:07:31 -0700
  * [MDEV-26025](https://jira.mariadb.org/browse/MDEV-26025) Server crashes while executing query with CTE in PS/SP
* [Revision #7da1cfb07a](https://github.com/MariaDB/server/commit/7da1cfb07a)\
  2021-06-25 18:00:47 +0300
  * avoid searching std::map twice in innochecksum
* [Revision #1918bdf32c](https://github.com/MariaDB/server/commit/1918bdf32c)\
  2021-06-21 14:54:26 +0300
  * [MDEV-25361](https://jira.mariadb.org/browse/MDEV-25361) innochecksum must not report errors for freed pages
* [Revision #5f8651ac23](https://github.com/MariaDB/server/commit/5f8651ac23)\
  2021-07-13 16:05:29 +0000
  * Fix switch case statement in trx\_flush\_log\_if\_needed\_low()
* [Revision #1cfcf32cd0](https://github.com/MariaDB/server/commit/1cfcf32cd0)\
  2021-07-20 10:56:49 +0200
  * fix libmariadb compilation, on GCC.
* [Revision #ce2a2bff0f](https://github.com/MariaDB/server/commit/ce2a2bff0f)\
  2021-07-19 22:06:42 +0200
  * [MDEV-20787](https://jira.mariadb.org/browse/MDEV-20787) Script dgcov.pl does not work
* [Revision #6638cf2e9e](https://github.com/MariaDB/server/commit/6638cf2e9e)\
  2021-07-19 22:02:10 +0200
  * [MDEV-20787](https://jira.mariadb.org/browse/MDEV-20787) Script dgcov.pl does not work
* [Revision #0151590d8f](https://github.com/MariaDB/server/commit/0151590d8f)\
  2021-07-19 17:50:09 +0200
  * Update libmariadb
* [Revision #f053349797](https://github.com/MariaDB/server/commit/f053349797)\
  2021-07-16 22:46:50 -0700
  * [MDEV-26135](https://jira.mariadb.org/browse/MDEV-26135) Assertion failure when executing PS with a hanging recursive CTE
* [Revision #b7886f55eb](https://github.com/MariaDB/server/commit/b7886f55eb)\
  2021-07-18 23:52:50 +0200
  * fix mysqld\_safe --help
* [Revision #bab989ab38](https://github.com/MariaDB/server/commit/bab989ab38)\
  2021-07-19 19:25:11 +0700
  * [MDEV-26145](https://jira.mariadb.org/browse/MDEV-26145): Incorrect metadata is sent on running query with union in PS mode
* [Revision #c47e4aab62](https://github.com/MariaDB/server/commit/c47e4aab62)\
  2021-06-26 20:11:56 +0300
  * [MDEV-23597](https://jira.mariadb.org/browse/MDEV-23597) Assertion \`marked\_for\_read()' failed while evaluating DEFAULT
* [Revision #6a89f346de](https://github.com/MariaDB/server/commit/6a89f346de)\
  2021-06-10 23:54:14 +0300
  * [MDEV-25858](https://jira.mariadb.org/browse/MDEV-25858): Query results are incorrect when indexes are added
* [Revision #da495b1b69](https://github.com/MariaDB/server/commit/da495b1b69)\
  2021-01-14 14:35:45 +0100
  * Typo fix in extrabackup.cc and innobackupex.cc
* [Revision #0f6e170c34](https://github.com/MariaDB/server/commit/0f6e170c34)\
  2021-07-08 04:24:38 +0000
  * [MDEV-25985](https://jira.mariadb.org/browse/MDEV-25985) Spider handle ">=" as ">" in some cases
* [Revision #165a6dc97a](https://github.com/MariaDB/server/commit/165a6dc97a)\
  2021-07-13 14:30:40 +0700
  * [MDEV-26119](https://jira.mariadb.org/browse/MDEV-26119) RPM packages on RHEL-8 require the latest minor
* [Revision #191cae2d0d](https://github.com/MariaDB/server/commit/191cae2d0d)\
  2021-06-25 04:23:27 +0300
  * [MDEV-18249](https://jira.mariadb.org/browse/MDEV-18249) ASSERT\_COLUMN\_MARKED\_FOR\_READ failed in ANALYZE TABLE
* [Revision #f64a4f672a](https://github.com/MariaDB/server/commit/f64a4f672a)\
  2021-06-28 21:31:14 +0300
  * follow-up [MDEV-18166](https://jira.mariadb.org/browse/MDEV-18166): rename marking functions
* [Revision #0f6a5b4390](https://github.com/MariaDB/server/commit/0f6a5b4390)\
  2021-06-22 18:30:53 +0300
  * \[2/2] [MDEV-18166](https://jira.mariadb.org/browse/MDEV-18166) ASSERT\_COLUMN\_MARKED\_FOR\_READ failed on tables with vcols
* [Revision #7d9ba57da4](https://github.com/MariaDB/server/commit/7d9ba57da4)\
  2021-06-21 17:48:45 +0300
  * \[1/2] [MDEV-18166](https://jira.mariadb.org/browse/MDEV-18166) ASSERT\_COLUMN\_MARKED\_FOR\_READ failed on tables with vcols
* [Revision #0e9ba176bf](https://github.com/MariaDB/server/commit/0e9ba176bf)\
  2021-06-21 04:00:16 +0300
  * [MDEV-17890](https://jira.mariadb.org/browse/MDEV-17890) Server crash on DELETE with YEAR field with truncated expr
* [Revision #b082716892](https://github.com/MariaDB/server/commit/b082716892)\
  2021-07-02 09:34:25 +0300
  * [MDEV-21206](https://jira.mariadb.org/browse/MDEV-21206) Can't link zlib library during DBD::mysql installation
* [Revision #fb0b28932c](https://github.com/MariaDB/server/commit/fb0b28932c)\
  2021-07-08 17:47:24 +0530
  * [MDEV-25998](https://jira.mariadb.org/browse/MDEV-25998) encryption.innodb\_encryption\_filekeys failure in buildbot
* [Revision #85063aebda](https://github.com/MariaDB/server/commit/85063aebda)\
  2020-10-28 19:45:54 +0100
  * Update description of mariadb-common package
* [Revision #d2dddbff4e](https://github.com/MariaDB/server/commit/d2dddbff4e)\
  2021-07-02 15:11:25 +0200
  * [MDEV-26080](https://jira.mariadb.org/browse/MDEV-26080): SHOW GRANTS does not quote role names properly for DEFAULT ROLE
* [Revision #83e442fc34](https://github.com/MariaDB/server/commit/83e442fc34)\
  2021-07-06 14:38:32 -0700
  * [MDEV-26095](https://jira.mariadb.org/browse/MDEV-26095) Infinite recursion when processing embedded recursive CTE with missing RECURSIVE
* [Revision #621fae3cbc](https://github.com/MariaDB/server/commit/621fae3cbc)\
  2021-07-06 11:36:59 +0200
  * [MDEV-25802](https://jira.mariadb.org/browse/MDEV-25802) mtr: race condition if the test quickly restarts twice
* [Revision #1223cfe1d3](https://github.com/MariaDB/server/commit/1223cfe1d3)\
  2021-07-05 21:46:00 +0200
  * [MDEV-25802](https://jira.mariadb.org/browse/MDEV-25802) mtr: race condition if the test quickly restarts twice
* [Revision #6a466db00a](https://github.com/MariaDB/server/commit/6a466db00a)\
  2021-07-05 22:02:23 +0200
  * [MDEV-25857](https://jira.mariadb.org/browse/MDEV-25857) MTR should report at least last test that was executed in case of shutdown and not-completed
* [Revision #22e4baaa5d](https://github.com/MariaDB/server/commit/22e4baaa5d)\
  2021-05-05 20:14:27 +0300
  * [MDEV-25595](https://jira.mariadb.org/browse/MDEV-25595) DROP part of failed CREATE OR REPLACE is not written into binary log
* [Revision #99f700a820](https://github.com/MariaDB/server/commit/99f700a820)\
  2021-07-03 11:41:49 +0300
  * [MDEV-25013](https://jira.mariadb.org/browse/MDEV-25013): SIGSEGV in best\_extension\_by\_limited\_search | SIGSEGV in restore\_prev\_nj\_state
* [Revision #d4177a7e09](https://github.com/MariaDB/server/commit/d4177a7e09)\
  2021-05-20 18:16:55 +0300
  * [MDEV-23937](https://jira.mariadb.org/browse/MDEV-23937): SIGSEGV in looped best\_extension\_by\_limited\_search from greedy\_search
* [Revision #cdb29960d2](https://github.com/MariaDB/server/commit/cdb29960d2)\
  2021-05-20 18:03:35 +0300
  * [MDEV-17783](https://jira.mariadb.org/browse/MDEV-17783): AddressSanitizer: stack-buffer-overflow in table\_cond\_selectivity
* [Revision #7c02e8717d](https://github.com/MariaDB/server/commit/7c02e8717d)\
  2021-07-02 15:13:37 +0200
  * [MDEV-26081](https://jira.mariadb.org/browse/MDEV-26081) set role crashes when a hostname cannot be resolved
* [Revision #ffe744e77d](https://github.com/MariaDB/server/commit/ffe744e77d)\
  2021-07-02 13:07:36 +0300
  * submodules.cmake: add missing --depth=1
* [Revision #2bf6f2c054](https://github.com/MariaDB/server/commit/2bf6f2c054)\
  2021-07-02 11:15:35 +0300
  * [MDEV-26077](https://jira.mariadb.org/browse/MDEV-26077) Assertion err != DB\_DUPLICATE\_KEY or unexpected ER\_TABLE\_EXISTS\_ERROR
* [Revision #5a2b625843](https://github.com/MariaDB/server/commit/5a2b625843)\
  2021-07-02 11:08:48 +0300
  * [MDEV-25129](https://jira.mariadb.org/browse/MDEV-25129) fixup: Adjust test result
* [Revision #c22f7f2323](https://github.com/MariaDB/server/commit/c22f7f2323)\
  2021-07-02 15:57:50 +1000
  * [MDEV-25129](https://jira.mariadb.org/browse/MDEV-25129) postfix for windows
* [Revision #eb20c91b55](https://github.com/MariaDB/server/commit/eb20c91b55)\
  2021-06-29 16:31:28 +0300
  * [MDEV-25969](https://jira.mariadb.org/browse/MDEV-25969): Condition pushdown into derived table doesn't work if select list uses SP
* [Revision #768c51880a](https://github.com/MariaDB/server/commit/768c51880a)\
  2021-06-24 14:16:11 +0300
  * [MDEV-25129](https://jira.mariadb.org/browse/MDEV-25129) Add KEYWORDS view to the INFORMATION\_SCHEMA
* [Revision #58252fff15](https://github.com/MariaDB/server/commit/58252fff15)\
  2021-06-29 14:28:23 +0300
  * [MDEV-26040](https://jira.mariadb.org/browse/MDEV-26040) os\_file\_set\_size() may not work on O\_DIRECT files
* [Revision #8147d2e618](https://github.com/MariaDB/server/commit/8147d2e618)\
  2021-06-28 11:52:00 +0400
  * [MDEV-25461](https://jira.mariadb.org/browse/MDEV-25461) Assertion \`je->state == JST\_KEY' failed in Geometry::create\_from\_json.
* [Revision #4e4f742ed7](https://github.com/MariaDB/server/commit/4e4f742ed7)\
  2021-06-26 23:11:10 -0700
  * Adjusted test results after the fix for [MDEV-20411](https://jira.mariadb.org/browse/MDEV-20411) (2)
* [Revision #8b3f816cab](https://github.com/MariaDB/server/commit/8b3f816cab)\
  2021-06-26 08:51:17 -0700
  * Adjusted test results after the fix for [MDEV-20411](https://jira.mariadb.org/browse/MDEV-20411)
* [Revision #12c80df482](https://github.com/MariaDB/server/commit/12c80df482)\
  2021-06-25 18:03:29 -0700
  * [MDEV-20411](https://jira.mariadb.org/browse/MDEV-20411) Procedure containing CTE incorrectly stored in mysql.proc
* [Revision #4ad148b148](https://github.com/MariaDB/server/commit/4ad148b148)\
  2021-06-25 06:48:17 +0200
  * [MDEV-26019](https://jira.mariadb.org/browse/MDEV-26019): Upgrading MariaDB breaks TLS mariadb-backup SST
* [Revision #9258cfa4b4](https://github.com/MariaDB/server/commit/9258cfa4b4)\
  2021-06-22 15:44:44 +0300
  * [MDEV-25978](https://jira.mariadb.org/browse/MDEV-25978) : rsync SST does not work with custom binlog name
* [Revision #83464029ce](https://github.com/MariaDB/server/commit/83464029ce)\
  2021-06-18 10:16:38 +0300
  * Fix try for Galera test lp1376747-4
* [Revision #f67aee000d](https://github.com/MariaDB/server/commit/f67aee000d)\
  2021-06-22 22:00:23 -0400
  * bump the VERSION
* [Revision #aaaed9baa0](https://github.com/MariaDB/server/commit/aaaed9baa0)\
  2021-06-22 18:57:01 +0700
  * [MDEV-25960](https://jira.mariadb.org/browse/MDEV-25960) yum update overwrites customized logrotation config (/etc/logrotate.d/mysql)
* [Revision #19716ad5a8](https://github.com/MariaDB/server/commit/19716ad5a8)\
  2021-06-22 09:11:41 +0300
  * [MDEV-25982](https://jira.mariadb.org/browse/MDEV-25982) Upgrade of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) log crashes due to missing encryption key
* [Revision #cc0bd8431f](https://github.com/MariaDB/server/commit/cc0bd8431f)\
  2021-06-21 16:15:07 -0700
  * [MDEV-25679](https://jira.mariadb.org/browse/MDEV-25679) Wrong result selecting from simple view with LIMIT and ORDER BY
* [Revision #773a07b655](https://github.com/MariaDB/server/commit/773a07b655)\
  2021-06-21 08:18:34 +0300
  * Remove Travis CI status
* [Revision #cd1a195b22](https://github.com/MariaDB/server/commit/cd1a195b22)\
  2021-06-17 16:10:11 +0530
  * [MDEV-25947](https://jira.mariadb.org/browse/MDEV-25947) innodb\_fts.misc\_debug fails in buildbot
* [Revision #35b57c37bb](https://github.com/MariaDB/server/commit/35b57c37bb)\
  2021-05-13 17:54:15 +0200
  * [MDEV-25617](https://jira.mariadb.org/browse/MDEV-25617) 10.5.10 upgrade: "scriptlet / line 6 : \[: is-active : binary operator expected"
* [Revision #c307dc6efd](https://github.com/MariaDB/server/commit/c307dc6efd)\
  2021-06-16 07:50:04 +0300
  * Remove a unused variable
* [Revision #2edb8e12e1](https://github.com/MariaDB/server/commit/2edb8e12e1)\
  2021-06-15 06:24:38 +0200
  * [MDEV-25880](https://jira.mariadb.org/browse/MDEV-25880) part 2: Improving reliability of the SST scripts
* [Revision #18d5be5b54](https://github.com/MariaDB/server/commit/18d5be5b54)\
  2021-06-09 03:41:37 +0200
  * [MDEV-25880](https://jira.mariadb.org/browse/MDEV-25880): rsync may be mistakenly killed when overlapping SST
* [Revision #1c35a3f6fd](https://github.com/MariaDB/server/commit/1c35a3f6fd)\
  2021-06-15 13:09:15 +0300
  * fix clang build
* [Revision #7d591cf850](https://github.com/MariaDB/server/commit/7d591cf850)\
  2021-06-15 13:14:39 +0530
  * [MDEV-24713](https://jira.mariadb.org/browse/MDEV-24713) Assertion \`dict\_table\_is\_comp(index->table)' failed in row\_merge\_buf\_add()
* [Revision #7229107e3e](https://github.com/MariaDB/server/commit/7229107e3e)\
  2021-06-15 13:13:01 +0530
  * [MDEV-25872](https://jira.mariadb.org/browse/MDEV-25872) InnoDB: Assertion failure in row\_merge\_read\_clustered\_index upon ALTER on table with indexed virtual columns
* [Revision #8c7d8b716c](https://github.com/MariaDB/server/commit/8c7d8b716c)\
  2021-06-15 13:12:15 +0530
  * [MDEV-14180](https://jira.mariadb.org/browse/MDEV-14180) Automatically disable key rotation checks for file\_key\_managment plugin
* [Revision #7d2c338c48](https://github.com/MariaDB/server/commit/7d2c338c48)\
  2021-06-14 19:37:06 +0530
  * [MDEV-14180](https://jira.mariadb.org/browse/MDEV-14180) preparation: Rename key\_rotation\_list
* [Revision #be243ed9e3](https://github.com/MariaDB/server/commit/be243ed9e3)\
  2021-06-15 12:40:33 +1000
  * cmake OpenBSD copyright notice correction
* [Revision #ec4df51414](https://github.com/MariaDB/server/commit/ec4df51414)\
  2021-06-15 12:34:23 +1000
  * eventscheduler mismatch of my\_{malloc,free}, delete
* [Revision #2e33f574b3](https://github.com/MariaDB/server/commit/2e33f574b3)\
  2021-06-14 23:45:31 +0200
  * update libmariadb
* [Revision #c9f9e38bb5](https://github.com/MariaDB/server/commit/c9f9e38bb5)\
  2021-06-12 12:38:45 +0200
  * fix mysqlest crash on ./mtr --sp innodb\_fts.innodb-fts-stopword
* [Revision #887f46a618](https://github.com/MariaDB/server/commit/887f46a618)\
  2021-06-12 12:23:07 +0200
  * fix mysqltest crash report output
* [Revision #4352c77c5a](https://github.com/MariaDB/server/commit/4352c77c5a)\
  2021-06-10 20:01:44 -0400
  * Link with libexecinfo on OpenBSD for stacktrace functionality.
* [Revision #152c83d49c](https://github.com/MariaDB/server/commit/152c83d49c)\
  2021-05-30 15:42:04 -0700
  * [MDEV-20392](https://jira.mariadb.org/browse/MDEV-20392): Skip ABI check if 'diff' is not found
* [Revision #396864c6b3](https://github.com/MariaDB/server/commit/396864c6b3)\
  2021-06-10 11:17:40 +0300
  * Remove orphan type name trx\_sig\_t
* [Revision #7a1eff0a9d](https://github.com/MariaDB/server/commit/7a1eff0a9d)\
  2021-06-09 15:28:35 +0300
  * [MDEV-25884](https://jira.mariadb.org/browse/MDEV-25884) Tests use environment $USER variable without quotes
* [Revision #c872125a66](https://github.com/MariaDB/server/commit/c872125a66)\
  2021-05-22 15:53:33 +0300
  * [MDEV-25630](https://jira.mariadb.org/browse/MDEV-25630): Crash with window function in left expr of IN subquery

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
