# MariaDB 10.1.1 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.1)[Release Notes](../../old-releases/10.1/10.1.1.md)[Changelog](mariadb-10-1-1-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 17 Oct 2014

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.1.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #1e79138](https://github.com/MariaDB/server/commit/1e79138)\
  2014-10-16 00:30:29 +0200
  * Merge branch 'bb-10.1-merge' into 10.1
* [Revision #42f359f](https://github.com/MariaDB/server/commit/42f359f)\
  2014-10-15 22:42:08 +0200
  * after-merge fixes
* [Revision #f62c12b](https://github.com/MariaDB/server/commit/f62c12b)\
  2014-10-15 12:59:13 +0200
  * Merge 10.0.14 into 10.1
* [Revision #7aed441](https://github.com/MariaDB/server/commit/7aed441)\
  2014-10-14 09:41:25 -0700
  * Merge branch '10.1' of ../10.1-mdev334 into 10.1
* [Revision #3c4bb0e](https://github.com/MariaDB/server/commit/3c4bb0e)\
  2014-10-14 09:36:50 -0700
  * [MDEV-334](https://jira.mariadb.org/browse/MDEV-334): Backport of UNION ALL optimization from mysql-5.7.
* [Revision #e813f9b](https://github.com/MariaDB/server/commit/e813f9b)\
  2014-10-14 14:58:35 +0400
  * [MDEV-6693](https://jira.mariadb.org/browse/MDEV-6693) - Atomic operations with explicit memory barrier
* [Revision #f947f73](https://github.com/MariaDB/server/commit/f947f73)\
  2014-10-13 21:47:56 +0200
  * Merge branch '10.1' of [server](https://github.com/ottok/server) into ottok-10.1
* [Revision #fec5ab5](https://github.com/MariaDB/server/commit/fec5ab5)\
  2014-10-12 20:48:07 +0400
  * [MDEV-6396](https://jira.mariadb.org/browse/MDEV-6396): ANALYZE INSERT/REPLACE is accepted, but does not produce a plan
* [Revision #5c33632](https://github.com/MariaDB/server/commit/5c33632)\
  2014-10-12 14:26:27 +0400
  * engine\_condition\_pushdown has been deprecated
* [Revision #698fcc5](https://github.com/MariaDB/server/commit/698fcc5)\
  2014-10-11 16:00:52 +0200
  * fix unstable test results
* [Revision #2f294db](https://github.com/MariaDB/server/commit/2f294db)\
  2014-10-11 10:18:55 +0200
  * fix a big test
* [Revision #5ca5f92](https://github.com/MariaDB/server/commit/5ca5f92)\
  2014-10-08 09:40:39 +0200
  * [MDEV-5749](https://jira.mariadb.org/browse/MDEV-5749) Please add a .pc file to MariaDB for easy use via pkg-config
* [Revision #7f5e51b](https://github.com/MariaDB/server/commit/7f5e51b)\
  2014-08-21 18:11:46 +0200
  * [MDEV-34](https://jira.mariadb.org/browse/MDEV-34) delete storage/ndb and sql/_ndb_ (and collateral changes)
* [Revision #57dd1f6](https://github.com/MariaDB/server/commit/57dd1f6)\
  2014-09-15 13:25:53 +0200
  * [MDEV-6108](https://jira.mariadb.org/browse/MDEV-6108) update userstat feature from percona server
* [Revision #43450fc](https://github.com/MariaDB/server/commit/43450fc)\
  2014-08-25 18:28:40 +0200
  * rename status\_user.test -> userstat.test
* [Revision #3182938](https://github.com/MariaDB/server/commit/3182938)\
  2014-08-25 19:08:55 +0200
  * move userstat tables to a plugin
* [Revision #db8af31](https://github.com/MariaDB/server/commit/db8af31)\
  2014-08-25 19:08:01 +0200
  * SHOW and FLUSH for I\_S tables.
* [Revision #932eaf3](https://github.com/MariaDB/server/commit/932eaf3)\
  2014-08-25 14:22:22 +0200
  * cleanup: sort struct members by size
* [Revision #3f7cc41](https://github.com/MariaDB/server/commit/3f7cc41)\
  2014-08-25 09:51:46 +0200
  * cleanup: remove dead code
* [Revision #534cbc1](https://github.com/MariaDB/server/commit/534cbc1)\
  2014-08-25 19:05:38 +0200
  * cleanup: my\_init\_dynamic\_array2 -> init\_dynamic\_array2
* [Revision #236556d](https://github.com/MariaDB/server/commit/236556d)\
  2014-09-04 14:38:29 +0200
  * fix TokuDB not to build ft-index library when disabled
* [Revision #e24c1c0](https://github.com/MariaDB/server/commit/e24c1c0)\
  2014-09-04 14:37:43 +0200
  * cleanup: remove unnecessary hack from federated/CMakeLists.txt
* [Revision #c006105](https://github.com/MariaDB/server/commit/c006105)\
  2014-10-09 21:43:48 +0200
  * make sysvars\_\* tests to work on 32-bit too
* [Revision #41756a3](https://github.com/MariaDB/server/commit/41756a3)\
  2014-10-11 10:19:56 +0200
  * portability fixes for sysvar\_\* tests
* [Revision #2a4e881](https://github.com/MariaDB/server/commit/2a4e881)\
  2014-09-03 15:16:43 +0200
  * GLOBAL\_VALUE\_ORIGIN=AUTO
* [Revision #3fa8c27](https://github.com/MariaDB/server/commit/3fa8c27)\
  2014-09-01 20:29:58 +0200
  * INFORMATION\_SCHEMA.SYSTEM\_VARIABLES.GLOBAL\_VALUE\_ORIGIN
* [Revision #513f584](https://github.com/MariaDB/server/commit/513f584)\
  2014-09-03 20:16:51 +0200
  * [MDEV-6138](https://jira.mariadb.org/browse/MDEV-6138) show sysvar's help in I\_S tables
* [Revision #beb2422](https://github.com/MariaDB/server/commit/beb2422)\
  2014-09-03 20:16:13 +0200
  * cleanup: @@mutex\_deadlock\_detector -> @@debug\_mutex\_deadlock\_detector
* [Revision #15623fd](https://github.com/MariaDB/server/commit/15623fd)\
  2014-09-01 14:46:20 +0200
  * mysqltest bug: replace\_regex /^foo/bar/ didn't work
* [Revision #a7b2c95](https://github.com/MariaDB/server/commit/a7b2c95)\
  2014-09-03 20:05:51 +0200
  * bugs in sys\_var::val\_\* code
* [Revision #b969a69](https://github.com/MariaDB/server/commit/b969a69)\
  2014-08-31 13:39:05 +0200
  * cleanup: simplify sys\_var::val\* methods, introduce val\_str\_nolock()
* [Revision #a4e7d33](https://github.com/MariaDB/server/commit/a4e7d33)\
  2014-08-31 13:21:06 +0200
  * cleanup: VARIABLE\_VALUE column should be NOT NULL
* [Revision #5389300](https://github.com/MariaDB/server/commit/5389300)\
  2014-08-29 13:59:08 +0200
  * cleanup: option\_type -> scope
* [Revision #99677cc](https://github.com/MariaDB/server/commit/99677cc)\
  2014-08-28 20:07:27 +0200
  * cleanup: move safe\_str\*() from sql\_acl.cc to m\_string.h
* [Revision #9bd5d54](https://github.com/MariaDB/server/commit/9bd5d54)\
  2014-08-28 09:33:00 +0200
  * correct fix for the old Bug#39955 (warnings in I\_S.VARIABLES)
* [Revision #d281faf](https://github.com/MariaDB/server/commit/d281faf)\
  2014-08-27 23:54:51 +0200
  * cleanup: sql\_show.cc
* [Revision #d508ef7](https://github.com/MariaDB/server/commit/d508ef7)\
  2014-08-28 09:23:15 +0200
  * cleanup: more 'const' qualifiers
* [Revision #9ccaa62](https://github.com/MariaDB/server/commit/9ccaa62)\
  2014-08-27 23:28:59 +0200
  * sys\_var\_pluginvar: populate my\_option and misc cleanup
* [Revision #28ebc2a](https://github.com/MariaDB/server/commit/28ebc2a)\
  2014-08-27 20:32:32 +0200
  * cleanup: sysvar, only one common check\_update\_type()
* [Revision #051c132](https://github.com/MariaDB/server/commit/051c132)\
  2014-08-27 16:05:54 +0200
  * cleanup: sysvar, SHOW\_VALUE\_IN\_HELP->GETOPT\_ONLY\_HELP
* [Revision #db2399b](https://github.com/MariaDB/server/commit/db2399b)\
  2014-08-27 10:23:20 +0200
  * small cleanup
* [Revision #8f15bf9](https://github.com/MariaDB/server/commit/8f15bf9)\
  2014-08-27 09:40:52 +0200
  * cleanup: remove hidden I\_S.VARIABLES and I\_S.STATUS tables
* [Revision #2fae1b5](https://github.com/MariaDB/server/commit/2fae1b5)\
  2014-09-08 09:39:43 +0200
  * prefer to use new flag name when possible
* [Revision #ab34aec](https://github.com/MariaDB/server/commit/ab34aec)\
  2014-08-25 23:13:37 +0200
  * [MDEV-6513](https://jira.mariadb.org/browse/MDEV-6513) deprecate engine\_condition\_pushdown value of the @@optimizer\_switch
* [Revision #686f102](https://github.com/MariaDB/server/commit/686f102)\
  2014-08-20 21:36:23 +0200
  * [MDEV-6609](https://jira.mariadb.org/browse/MDEV-6609) SQL inside an anonymous block is executed with wrong SQL\_MODE [MDEV-6606](https://jira.mariadb.org/browse/MDEV-6606) Server crashes in String::append on selecting sql\_mode inside anonymous block
* [Revision #30ea6dd](https://github.com/MariaDB/server/commit/30ea6dd)\
  2014-08-20 20:57:32 +0200
  * [MDEV-6603](https://jira.mariadb.org/browse/MDEV-6603) SBR failure upon executing a prepared statement with input placeholder under anonymous block
* [Revision #013f0f6](https://github.com/MariaDB/server/commit/013f0f6)\
  2014-08-20 17:25:44 +0200
  * cleanup: query rewrites for Item\_param and Item\_splocal
* [Revision #d7c1e0e](https://github.com/MariaDB/server/commit/d7c1e0e)\
  2014-08-18 21:36:11 +0200
  * [MDEV-5317](https://jira.mariadb.org/browse/MDEV-5317) Compound statement / anonymous blocks
* [Revision #a99af48](https://github.com/MariaDB/server/commit/a99af48)\
  2014-08-13 21:04:05 +0200
  * [MDEV-5317](https://jira.mariadb.org/browse/MDEV-5317) out parameters in PREPARE "SELECT ... INTO"
* [Revision #278f7fd](https://github.com/MariaDB/server/commit/278f7fd)\
  2014-08-19 21:06:20 +0200
  * cleanup: get rid of (Item\_splocal\*)item downcast
* [Revision #932100c](https://github.com/MariaDB/server/commit/932100c)\
  2014-08-17 20:36:40 +0200
  * cleanup sql\_yacc.yy: remove redundant ev\_sql\_stmt\_inner rule
* [Revision #60475b8](https://github.com/MariaDB/server/commit/60475b8)\
  2014-08-17 20:35:39 +0200
  * cleanup sql\_yacc.yy: rules for the CASE ... END CASE statement
* [Revision #319f206](https://github.com/MariaDB/server/commit/319f206)\
  2014-08-17 13:28:27 +0200
  * cleanup sql\_yacc.yy: s/IF/IF\_SYM/
* [Revision #09c1af9](https://github.com/MariaDB/server/commit/09c1af9)\
  2014-08-17 20:54:48 +0200
  * cleanup sql\_yacc.yy: reduce code duplication in rules for BEGIN...END with and without label
* [Revision #d49e118](https://github.com/MariaDB/server/commit/d49e118)\
  2014-08-17 20:51:59 +0200
  * cleanup sql\_yacc.yy: factor out duplicate code in PROCEDURE/FUNCTION/TRIGGER/EVENT grammar
* [Revision #352723c](https://github.com/MariaDB/server/commit/352723c)\
  2014-08-17 20:50:53 +0200
  * cleanup sql\_yacc.yy: rename rules for loops with and without label to follow BEGIN...END rule naming
* [Revision #45907be](https://github.com/MariaDB/server/commit/45907be)\
  2014-08-17 20:48:48 +0200
  * cleanup sql\_yacc.yy: remove duplicate code in opt\_union rule
* [Revision #71485e7](https://github.com/MariaDB/server/commit/71485e7)\
  2014-08-17 20:46:46 +0200
  * cleanup sql\_yacc: introduce opt\_not rule, combine otherwise duplicate rules
* [Revision #c655609](https://github.com/MariaDB/server/commit/c655609)\
  2014-08-17 20:37:49 +0200
  * cleanup sql\_yacc.yy: s/YYABORT/MYSQL\_YYABORT/
* [Revision #fdf32f5](https://github.com/MariaDB/server/commit/fdf32f5)\
  2014-08-16 08:47:29 +0200
  * cleanup: param\_marker rule in the parser
* [Revision #1e0a11a](https://github.com/MariaDB/server/commit/1e0a11a)\
  2014-08-16 08:46:27 +0200
  * cleanup: class my\_var
* [Revision #624888b](https://github.com/MariaDB/server/commit/624888b)\
  2014-08-16 08:17:29 +0200
  * cleanup: inherit from Sql\_alloc
* [Revision #43d1f0b](https://github.com/MariaDB/server/commit/43d1f0b)\
  2014-08-15 17:35:07 +0200
  * cleanup: rename List<> methods
* [Revision #aabb33c](https://github.com/MariaDB/server/commit/aabb33c)\
  2014-08-16 08:17:08 +0200
  * cleanup: public Item\_param::get\_settable\_routine\_parameter()
* [Revision #e8fb246](https://github.com/MariaDB/server/commit/e8fb246)\
  2014-08-16 08:16:44 +0200
  * cleanup: use null\_lex\_str where appropriate
* [Revision #6e05aab](https://github.com/MariaDB/server/commit/6e05aab)\
  2014-08-16 08:16:18 +0200
  * cleanup: case SQLCOM\_CALL
* [Revision #3d9aa6c](https://github.com/MariaDB/server/commit/3d9aa6c)\
  2014-10-08 18:49:34 +0200
  * Plugin API: increase SHOW\_VAR\_FUNC\_BUFF\_SIZE for 64-bit CPUs
* [Revision #03ec351](https://github.com/MariaDB/server/commit/03ec351)\
  2014-10-08 18:47:16 +0200
  * cleanup: galera misc cleanups
* [Revision #8596b70](https://github.com/MariaDB/server/commit/8596b70)\
  2014-10-07 20:28:33 +0200
  * cleanup: simplify the usage of WSREP\_FORMAT macro
* [Revision #d103e35](https://github.com/MariaDB/server/commit/d103e35)\
  2014-10-08 08:47:22 +0200
  * followup changes to timeout commit
* [Revision #e6152f9](https://github.com/MariaDB/server/commit/e6152f9)\
  2014-10-10 21:30:23 +0400
  * [MDEV-6702](https://jira.mariadb.org/browse/MDEV-6702): analyze\_stmt test fails in --embedded 10.1
* [Revision #988f3fb](https://github.com/MariaDB/server/commit/988f3fb)\
  2014-10-10 14:40:21 +0400
  * [MDEV-6846](https://jira.mariadb.org/browse/MDEV-6846): Test tokudb\_mariadb.mdev6657 fails in buildbot
* [Revision #4439d1f](https://github.com/MariaDB/server/commit/4439d1f)\
  2014-10-07 11:40:10 +0300
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #4af97bc](https://github.com/MariaDB/server/commit/4af97bc)\
  2014-10-07 11:39:42 +0300
  * Removed files that had been accidentally committed Removed compiler warnings
* [Revision #cc8aed3](https://github.com/MariaDB/server/commit/cc8aed3)\
  2014-10-07 11:37:36 +0300
  * MDEV 4427: query timeouts
* [Revision #f7c57b4](https://github.com/MariaDB/server/commit/f7c57b4)\
  2014-10-06 15:26:09 -0400
  * [MDEV-6667](https://jira.mariadb.org/browse/MDEV-6667): Merged fix from maria-10.0-galera.
* [Revision #1a7d1731](https://github.com/MariaDB/server/commit/1a7d1731)\
  2014-10-06 12:21:53 +0400
  * Merge ../10.1-orderby-fixes into 10.1
* [Revision #61d8b4a](https://github.com/MariaDB/server/commit/61d8b4a)\
  2014-10-04 13:59:07 -0400
  * [MDEV-6833](https://jira.mariadb.org/browse/MDEV-6833): SIGSEGV on shutdown with non-default wsrep\_slave\_threads
* [Revision #c768af7](https://github.com/MariaDB/server/commit/c768af7)\
  2014-10-04 13:53:33 -0400
  * Minor modifications
* [Revision #7474e7b](https://github.com/MariaDB/server/commit/7474e7b)\
  2014-10-02 21:01:57 +0300
  * [MDEV-6807](https://jira.mariadb.org/browse/MDEV-6807): InnoDB: Assertion failure in file lock0lock.cc (lock != ctx->wait\_lock)
* [Revision #ebe4fad](https://github.com/MariaDB/server/commit/ebe4fad)\
  2014-10-02 18:54:01 +0200
  * when running mtr tests don't let galera-started rsyncd to log to syslog
* [Revision #251239a](https://github.com/MariaDB/server/commit/251239a)\
  2014-10-02 15:09:17 +0300
  * Fix Windows compiler error 'log2f': identifier not found
* [Revision #f13cf62](https://github.com/MariaDB/server/commit/f13cf62)\
  2014-09-30 11:04:38 +0200
  * don't enable SECURITY\_HARDENED on old gcc
* [Revision #2156f62](https://github.com/MariaDB/server/commit/2156f62)\
  2014-09-29 19:50:56 +0200
  * portability: use getifaddrs()
* [Revision #edd1de3](https://github.com/MariaDB/server/commit/edd1de3)\
  2014-09-28 17:50:02 +0200
  * cleanup: introduce CF\_SKIP\_WSREP\_CHECK
* [Revision #b346952](https://github.com/MariaDB/server/commit/b346952)\
  2014-09-28 16:43:44 +0200
  * cleanup: remove OPT\_WSREP\_START\_POSITION and OPT\_WSREP\_SST\_AUTH
* [Revision #eaec266](https://github.com/MariaDB/server/commit/eaec266)\
  2014-09-28 12:41:51 +0200
  * restore and fix wsrep status variables
* [Revision #13af416](https://github.com/MariaDB/server/commit/13af416)\
  2014-09-28 11:08:07 +0200
  * cleanup: wsrep\_check\_opts
* [Revision #425dc6d](https://github.com/MariaDB/server/commit/425dc6d)\
  2014-09-28 09:13:05 +0200
  * small cleanup
* [Revision #7aabc2d](https://github.com/MariaDB/server/commit/7aabc2d)\
  2014-09-27 22:29:10 +0200
  * fixing embedded: WaaS. Wsrep as a Service.
* [Revision #8877adb](https://github.com/MariaDB/server/commit/8877adb)\
  2014-09-26 17:02:47 +0200
  * fixing embedded: first set of changes (storage engines don't work yet)
* [Revision #c6b9522](https://github.com/MariaDB/server/commit/c6b9522)\
  2014-09-26 20:03:38 +0200
  * use MD5 service in innodb/xtradb
* [Revision #d6141a5](https://github.com/MariaDB/server/commit/d6141a5)\
  2014-09-26 20:03:20 +0200
  * MD5 service
* [Revision #11b6452](https://github.com/MariaDB/server/commit/11b6452)\
  2014-09-26 18:49:47 +0200
  * extend SHA1 service. cleanup of sha1 wrappers
* [Revision #93b50e6](https://github.com/MariaDB/server/commit/93b50e6)\
  2014-09-26 10:22:44 +0200
  * cleanup: remove galera/wsrep magic from mtr
* [Revision #4bb49d8](https://github.com/MariaDB/server/commit/4bb49d8)\
  2014-09-26 15:54:42 +0200
  * correct handling on defaults\[-extra]-file is SST scripts
* [Revision #dc113e2](https://github.com/MariaDB/server/commit/dc113e2)\
  2014-09-26 12:55:56 +0200
  * fix cmake detection of bfd.h
* [Revision #d06b5b6](https://github.com/MariaDB/server/commit/d06b5b6)\
  2014-09-26 10:22:18 +0200
  * disable wsrep by default. fix wsrep not to crash when started disabled
* [Revision #4b9bf9d](https://github.com/MariaDB/server/commit/4b9bf9d)\
  2014-09-26 07:04:33 +0200
  * bugfix: remove the code that broke XA recovery
* [Revision #3620910](https://github.com/MariaDB/server/commit/3620910)\
  2014-09-25 23:00:45 +0200
  * cleanup: galera merge, simple changes
* [Revision #b04f848](https://github.com/MariaDB/server/commit/b04f848)\
  2014-09-20 21:36:51 +0200
  * cleanup: use is\_supported\_parser\_charset
* [Revision #1a731af](https://github.com/MariaDB/server/commit/1a731af)\
  2014-09-19 21:10:06 +0200
  * cleanup: remove redundant clauses from sys\_vars.cc
* [Revision #b054e4b](https://github.com/MariaDB/server/commit/b054e4b)\
  2014-09-19 12:51:33 +0200
  * bugfix: disabling partitioning in already built tree
* [Revision #88cebbdf](https://github.com/MariaDB/server/commit/88cebbdf)\
  2014-09-11 10:08:48 +0200
  * cleanup: remove libedit, move readline to extra/
* [Revision #74a552d](https://github.com/MariaDB/server/commit/74a552d)\
  2014-09-05 16:08:58 +0200
  * cleanup: remove table->status from some engines
* [Revision #fe0ff58](https://github.com/MariaDB/server/commit/fe0ff58)\
  2014-09-04 21:37:10 +0200
  * compiler warnings
* [Revision #605b48d](https://github.com/MariaDB/server/commit/605b48d)\
  2014-09-30 19:22:27 +0400
  * [MDEV-6814](https://jira.mariadb.org/browse/MDEV-6814): Server crashes in calculate\_key\_len on query with ORDER BY - if test\_if\_skip\_sort\_order() decides to switch to using an index, or switch from using ref to using quick select, it should set all members accordingly.
* [Revision #fc2df3c](https://github.com/MariaDB/server/commit/fc2df3c)\
  2014-09-30 14:50:34 +0300
  * [MDEV-6812](https://jira.mariadb.org/browse/MDEV-6812): Merge Kakao: Add global status variables which tell you the progress of inplace alter table and row log buffer usage
* [Revision #0b15557](https://github.com/MariaDB/server/commit/0b15557)\
  2014-09-26 15:54:35 +0400
  * [MDEV-6796](https://jira.mariadb.org/browse/MDEV-6796): Unable to skip filesort when using implicit extended key
* [Revision #bef30f2](https://github.com/MariaDB/server/commit/bef30f2)\
  2014-09-26 12:16:05 +0300
  * Fix test failures seen on -- innodb-wl5522-debug-zip (path differences win/unix) -- innodb\_defragment\_fill\_factor (stabilise) -- innodb\_force\_pk (case difference win/unix)
* [Revision #236cc6c](https://github.com/MariaDB/server/commit/236cc6c)\
  2014-09-25 20:59:15 -0400
  * wsrep-related changes: removed some unnecessary files & minor modifications.
* [Revision #a756ac6](https://github.com/MariaDB/server/commit/a756ac6)\
  2014-09-25 22:12:52 +0400
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #98c95ff](https://github.com/MariaDB/server/commit/98c95ff)\
  2014-09-25 22:12:18 +0400
  * Better comments about KEY::ext\_key\_part\_map
* [Revision #d6a67ce](https://github.com/MariaDB/server/commit/d6a67ce)\
  2014-09-25 13:32:55 -0400
  * Fix for syntax error in debian control file.
* [Revision #a28c9a5](https://github.com/MariaDB/server/commit/a28c9a5)\
  2014-09-25 11:46:52 -0400
  * [MDEV-6790](https://jira.mariadb.org/browse/MDEV-6790): 10.1: debian build failure Updated 33\_scriptsmysql\_create\_system\_tablesno\_test.dpatch to reflect user.default\_role.
* [Revision #30fab5f](https://github.com/MariaDB/server/commit/30fab5f)\
  2014-09-25 19:14:16 +0400
  * [MDEV-6788](https://jira.mariadb.org/browse/MDEV-6788): The variable 'role' is being used without being initialized at sql\_acl.cc:8840
* [Revision #532334c](https://github.com/MariaDB/server/commit/532334c)\
  2014-09-25 18:27:20 +0400
  * [MDEV-6788](https://jira.mariadb.org/browse/MDEV-6788): The variable 'role' is being used without being initialized at sql\_acl.cc:8840
* [Revision #9ce830d](https://github.com/MariaDB/server/commit/9ce830d)\
  2014-09-25 14:30:59 +0400
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #e74bf07](https://github.com/MariaDB/server/commit/e74bf07)\
  2014-09-25 14:29:14 +0400
  * Better comments
* [Revision #3f2d9a9](https://github.com/MariaDB/server/commit/3f2d9a9)\
  2014-09-24 23:52:17 +0300
  * Fixed failing test temp\_table\_frm
* [Revision #f1afc00](https://github.com/MariaDB/server/commit/f1afc00)\
  2014-09-24 15:41:42 +0200
  * [MDEV-6743](https://jira.mariadb.org/browse/MDEV-6743) crash in GROUP\_CONCAT(IF () ORDER BY 1)
* [Revision #3416fac](https://github.com/MariaDB/server/commit/3416fac)\
  2014-09-24 17:27:00 +0400
  * [MDEV-6776](https://jira.mariadb.org/browse/MDEV-6776) ujis and eucjmps erroneously accept 0x8EA0 as a valid byte sequence
* [Revision #9fa62b4](https://github.com/MariaDB/server/commit/9fa62b4)\
  2014-09-24 13:08:47 +0200
  * remove the bug fix for [MDEV-6743](https://jira.mariadb.org/browse/MDEV-6743) "crash in GROUP\_CONCAT(IF () ORDER BY 1)"
* [Revision #15ad0d0](https://github.com/MariaDB/server/commit/15ad0d0)\
  2014-09-24 12:17:15 +0400
  * Merge ../10.1-mdev6657 into bb-10.1-orderby-fixes
* [Revision #c7d45c2](https://github.com/MariaDB/server/commit/c7d45c2)\
  2014-09-24 12:04:16 +0400
  * Merge ../10.1-mdev6402 into bb-10.1-orderby-fixes
* [Revision #f5d8454](https://github.com/MariaDB/server/commit/f5d8454)\
  2014-09-24 11:56:22 +0400
  * Better comments
* [Revision #06d6552](https://github.com/MariaDB/server/commit/06d6552)\
  2014-09-23 23:55:29 +0200
  * 5.5 merge
* [Revision #53a4491](https://github.com/MariaDB/server/commit/53a4491)\
  2014-09-23 23:37:35 +0200
  * merge
* [Revision #b91432b](https://github.com/MariaDB/server/commit/b91432b)\
  2014-09-23 22:03:35 +0200
  * tokudb 7.5.0
* [Revision #a3bd38d](https://github.com/MariaDB/server/commit/a3bd38d)\
  2014-09-23 15:58:54 +0400
  * Adding tests for handling 0x5C as the second byte in a multi-byte sequence, and as a escape character when SET NAMES xxx, character\_set\_connection=binary; for cp932,big5,gbk,sjis
* [Revision #348a24a](https://github.com/MariaDB/server/commit/348a24a)\
  2014-09-23 13:57:55 +0300
  * Allow tokudb test to pass even if jemalloc is not available.
* [Revision #bab638d](https://github.com/MariaDB/server/commit/bab638d)\
  2014-09-23 13:57:29 +0300
  * [MDEV-6743](https://jira.mariadb.org/browse/MDEV-6743) crash in GROUP\_CONCAT(IF () ORDER BY 1)
* [Revision #504c6cc](https://github.com/MariaDB/server/commit/504c6cc)\
  2014-09-22 23:25:56 +0300
  * Fixed test failures Added comments Ensure that tokudb test works even if jemalloc is not installed Removed not referenced function Item::remove\_fixed()
* [Revision #34f3aa9](https://github.com/MariaDB/server/commit/34f3aa9)\
  2014-09-19 09:21:51 +0200
  * remove unused (obsolete) declarations from slave.h
* [Revision #989dd4d](https://github.com/MariaDB/server/commit/989dd4d)\
  2014-09-18 21:54:45 +0200
  * 5.5 merge
* [Revision #e41bca0](https://github.com/MariaDB/server/commit/e41bca0)\
  2014-09-18 17:00:44 +0200
  * support statically linked jemalloc. use that for release builds
* [Revision #152f1cd](https://github.com/MariaDB/server/commit/152f1cd)\
  2014-09-18 15:24:30 +0200
  * print binlog unsafe errors at log\_warnings level 1, not 2.
* [Revision #8286bcd](https://github.com/MariaDB/server/commit/8286bcd)\
  2014-09-18 12:40:55 +0400
  * [MDEV-6752](https://jira.mariadb.org/browse/MDEV-6752) Trailing incomplete characters are not replaced to question marks on conversion
* [Revision #391fddf](https://github.com/MariaDB/server/commit/391fddf)\
  2014-09-18 09:26:30 +0900
  * Merge Spider 3.2.11
* [Revision #c338772](https://github.com/MariaDB/server/commit/c338772)\
  2014-09-17 19:38:42 +0200
  * fixes for valgrind failures
* [Revision #b04748c](https://github.com/MariaDB/server/commit/b04748c)\
  2014-09-17 15:11:24 +0200
  * fix intermittent failures of main.create\_or\_replace test in buildbot
* [Revision #a006813](https://github.com/MariaDB/server/commit/a006813)\
  2014-09-16 14:08:05 +0200
  * merge
* [Revision #d017953](https://github.com/MariaDB/server/commit/d017953)\
  2014-09-16 14:04:50 +0200
  * fixes for test cases
* [Revision #7e29c1b](https://github.com/MariaDB/server/commit/7e29c1b)\
  2014-09-16 14:03:17 +0200
  * 5.5 merge
* [Revision #33656e0](https://github.com/MariaDB/server/commit/33656e0)\
  2014-09-16 13:35:28 +0200
  * for mysql-test: fix mysqlhotcopy script to return a predictable exit code
* [Revision #ec46381](https://github.com/MariaDB/server/commit/ec46381)\
  2014-09-16 07:37:00 +0300
  * Avoid using log\_sys mutex when printing out show engine innodb status, instead peek (maybe) old data.
* [Revision #8db1f72](https://github.com/MariaDB/server/commit/8db1f72)\
  2014-09-16 00:06:05 +0300
  * Auto merge
* [Revision #8e4566e](https://github.com/MariaDB/server/commit/8e4566e)\
  2014-09-16 00:00:47 +0300
  * Don't give warning if there are two unique keys used with INSERT .. ON DUPLICATE KEY UPDATE. We should assume that the store engine will report the first duplicate key for this case.
* [Revision #e167c48](https://github.com/MariaDB/server/commit/e167c48)\
  2014-09-15 23:52:40 +0300
  * Fixed randomly failing test
* [Revision #bb75cf0](https://github.com/MariaDB/server/commit/bb75cf0)\
  2014-09-15 14:49:16 -0400
  * DB-720 run the cluster key partition test on mariadb
* [Revision #f18b140](https://github.com/MariaDB/server/commit/f18b140)\
  2014-09-15 18:55:17 +0200
  * debian: require jemalloc >= 3.0.0, because 2.2.5 (on precise) crashes
* [Revision #b41d5ae](https://github.com/MariaDB/server/commit/b41d5ae)\
  2014-09-15 20:33:11 +0400
  * Changes in storage\_engine test suite:
* [Revision #7a50ce1](https://github.com/MariaDB/server/commit/7a50ce1)\
  2014-09-15 17:11:01 +0300
  * Use LOCK\_show\_status when we add things to all\_status\_vars This was missing in my last commit for fixing possible lockups in SHOW STATUS.
* [Revision #b183d81](https://github.com/MariaDB/server/commit/b183d81)\
  2014-09-15 07:47:43 -0400
  * DB-714 read free replication
* [Revision #ac45ebc](https://github.com/MariaDB/server/commit/ac45ebc)\
  2014-09-15 07:27:18 -0400
  * DB-720 test case for clustering keys on partitioned tokudb tables
* [Revision #d85b993](https://github.com/MariaDB/server/commit/d85b993)\
  2014-09-13 16:06:55 -0400
  * DB-504 redo bulk fetch select tests in partitioned tables
* [Revision #e3deed4](https://github.com/MariaDB/server/commit/e3deed4)\
  2014-09-13 21:32:49 +0200
  * ft-index: restore a chunk that was lost in the merge and other fixes for gcc-4.9.1 on sid
* [Revision #50e67fe](https://github.com/MariaDB/server/commit/50e67fe)\
  2014-09-13 17:15:11 +0400\
  \*
  * Adding big5, cp932, gbk, sjis tests covering characters that can have 0x5C as the second byte in a multi-byte character. - Adding big5 tests covering an unassigned character 0xC840 being stored into char/varchar/text/enum columns.
* [Revision #77a0c9b](https://github.com/MariaDB/server/commit/77a0c9b)\
  2014-09-13 08:32:53 +0200
  * tokudb: use thd\_killed() api function, not thd->killed directly
* [Revision #e7ddd89](https://github.com/MariaDB/server/commit/e7ddd89)\
  2014-09-13 08:16:00 +0200
  * tokudb tests: master-slave.inc should be included _last_
* [Revision #1e3e81a](https://github.com/MariaDB/server/commit/1e3e81a)\
  2014-09-13 00:30:46 +0200
  * sphinx 2.1.9
* [Revision #aef3818](https://github.com/MariaDB/server/commit/aef3818)\
  2014-09-13 00:28:15 +0200
  * tokudb 7.1.8
* [Revision #c799d65](https://github.com/MariaDB/server/commit/c799d65)\
  2014-09-12 16:51:41 +0200
  * 5.3 merge
* [Revision #86957d4](https://github.com/MariaDB/server/commit/86957d4)\
  2014-09-12 16:44:27 +0200
  * 10.0-connect merge
* [Revision #b23af85](https://github.com/MariaDB/server/commit/b23af85)\
  2014-09-12 16:06:18 +0400
  * [MDEV-6737](https://jira.mariadb.org/browse/MDEV-6737) Stored routines do now work with swe7: "The table mysql.proc is missing, corrupt, or contains bad data" Fixed the bug itself. Also, added "SET NAMES swe7" which was forgotten in the previous commit, so latin1 was actually tested lati1 instead of swe7 in a mistake. Now it tests swe7.
* [Revision #fa51a22](https://github.com/MariaDB/server/commit/fa51a22)\
  2014-09-12 14:49:24 +0300
  * Fixed compiler warnings
* [Revision #e36d6f0](https://github.com/MariaDB/server/commit/e36d6f0)\
  2014-09-12 14:49:13 +0300
  * Don't use LOCK\_status for the duration of SHOW STATUS because of possible lookups. Instead we use LOCK\_status only to protect summary of thread statistics and use a new mutex, LOCK\_show\_status to protect concurrent SHOW STATUS.
* [Revision #9276e0e](https://github.com/MariaDB/server/commit/9276e0e)\
  2014-09-12 14:45:11 +0300
  * Cleanup of my\_hash\_sort patch
* [Revision #b73bef2](https://github.com/MariaDB/server/commit/b73bef2)\
  2014-09-12 07:31:01 -0400
  * DB-716 use jemalloc 3.6.0 in debug env
* [Revision #6a576f1](https://github.com/MariaDB/server/commit/6a576f1)\
  2014-09-12 12:57:27 +0400
  * Adding thorough tests covering what happens with escaped sequences in the SQL parser.
* [Revision #32360bb](https://github.com/MariaDB/server/commit/32360bb)\
  2014-09-12 08:41:44 +0200
  * [MDEV-6526](https://jira.mariadb.org/browse/MDEV-6526) INFO\_SRC and INFO\_BIN installed wrong
* [Revision #269f0a6](https://github.com/MariaDB/server/commit/269f0a6)\
  2014-09-12 08:41:35 +0200
  * [MDEV-6619](https://jira.mariadb.org/browse/MDEV-6619) SHOW PROCESSLIST returns empty result set after KILL QUERY
* [Revision #3d94523](https://github.com/MariaDB/server/commit/3d94523)\
  2014-09-12 08:41:16 +0200
  * [MDEV-6613](https://jira.mariadb.org/browse/MDEV-6613) build system endianness test fails for ppc64le (i.e. Ubuntu)
* [Revision #d2ae40a](https://github.com/MariaDB/server/commit/d2ae40a)\
  2014-09-12 03:21:54 +0400
  * Fixes in storage\_engine test suite
* [Revision #8aa88db](https://github.com/MariaDB/server/commit/8aa88db)\
  2014-09-12 02:19:49 +0400
  * [MDEV-6402](https://jira.mariadb.org/browse/MDEV-6402): Optimizer doesn't choose best execution plan when composite...
* [Revision #c6051a4](https://github.com/MariaDB/server/commit/c6051a4)\
  2014-09-11 23:50:31 +0300
  * Automatic merge
* [Revision #c4f5326](https://github.com/MariaDB/server/commit/c4f5326)\
  2014-09-11 22:42:35 +0300
  * [MDEV-6255](https://jira.mariadb.org/browse/MDEV-6255) DUPLICATE KEY Errors on SELECT .. GROUP BY that uses temporary and filesort.
* [Revision #4a68817](https://github.com/MariaDB/server/commit/4a68817)\
  2014-09-11 16:44:16 +0200
  * XtraDB 5.6.20-68.0
* [Revision #75796d9](https://github.com/MariaDB/server/commit/75796d9)\
  2014-09-11 16:42:54 +0200
  * InnoDB 5.6.20
* [Revision #c30a844](https://github.com/MariaDB/server/commit/c30a844)\
  2014-09-11 15:41:30 +0300
  * [MDEV-6729](https://jira.mariadb.org/browse/MDEV-6729): InnoDB: Failing assertion: state == TRX\_STATE\_NOT\_STARTED in file trx0trx.ic line 60
* [Revision #89b6517](https://github.com/MariaDB/server/commit/89b6517)\
  2014-09-11 10:15:01 +0200
  * percona-server-5.6.20-68.0
* [Revision #f16be24](https://github.com/MariaDB/server/commit/f16be24)\
  2014-09-11 10:14:20 +0200
  * 2.1.9-release
* [Revision #993395b](https://github.com/MariaDB/server/commit/993395b)\
  2014-09-11 10:13:35 +0200
  * 5.6.20
* [Revision #d0a5f33](https://github.com/MariaDB/server/commit/d0a5f33)\
  2014-09-11 07:10:37 +0300
  * Remove incorrect test file.
* [Revision #9596d75](https://github.com/MariaDB/server/commit/9596d75)\
  2014-09-10 18:18:53 -0400
  * DB-548 generate dirty upgrade test cases with old rollback nodes
* [Revision #3bffb9d](https://github.com/MariaDB/server/commit/3bffb9d)\
  2014-09-10 14:52:18 -0400
  * FT-592 add tokuftdump --node N parameter
* [Revision #7e2bc14](https://github.com/MariaDB/server/commit/7e2bc14)\
  2014-09-10 20:19:41 +0300
  * Remove unnecessary debug output causing unnecessary warnings.
* [Revision #595bcb7](https://github.com/MariaDB/server/commit/595bcb7)\
  2014-09-10 18:48:26 +0300
  * Fix merge error on binlog\_remove\_pending\_rows causing failure on binlog\_innodb\_row test.
* [Revision #3a91af9](https://github.com/MariaDB/server/commit/3a91af9)\
  2014-09-10 17:45:09 +0200
  * [MDEV-6647](https://jira.mariadb.org/browse/MDEV-6647) MariaDB CLI client doesnt show CREATE INDEX progress
* [Revision #12bf329](https://github.com/MariaDB/server/commit/12bf329)\
  2014-09-10 09:48:11 -0400
  * FT-273 Fix a bug where we'd overactively assert that the memcmp magic bits were inconsistent though the handle was opened without those bits set. This caused dbremove to always fail.
* [Revision #30d7860](https://github.com/MariaDB/server/commit/30d7860)\
  2014-09-10 13:22:44 +0200
  * [MDEV-6459](https://jira.mariadb.org/browse/MDEV-6459) max\_relay\_log\_size and sql\_slave\_skip\_counter misbehave on PPC64
* [Revision #b2c54a9](https://github.com/MariaDB/server/commit/b2c54a9)\
  2014-09-10 13:22:20 +0200
  * [MDEV-6523](https://jira.mariadb.org/browse/MDEV-6523) CONNECT temporary table created
* [Revision #4ff2a68](https://github.com/MariaDB/server/commit/4ff2a68)\
  2014-09-10 13:22:01 +0200
  * [MDEV-6565](https://jira.mariadb.org/browse/MDEV-6565) search order for my.cnf inconsistent in docs/use, and global override with build-time -DDEFAULT\_SYSCONFDIR is ignored
* [Revision #1e7dd85](https://github.com/MariaDB/server/commit/1e7dd85)\
  2014-09-10 13:10:24 +0200
  * [MDEV-6579](https://jira.mariadb.org/browse/MDEV-6579) IMPORT\_EXECUTABLES feature broken by addition of gen\_pfs\_lex\_token
* [Revision #b67e1d3](https://github.com/MariaDB/server/commit/b67e1d3)\
  2014-09-10 09:44:57 +0300
  * Adjusted defrag test that fails randomly (timing problem) and fix result of innodb\_sys\_index test.
* [Revision #5023bb8](https://github.com/MariaDB/server/commit/5023bb8)\
  2014-09-09 16:44:54 -0700
  * Fixed bug [MDEV-6292](https://jira.mariadb.org/browse/MDEV-6292). Avoided exponential recursive calls of JOIN\_CACHE::join\_records() in the case of non-nested outer joins. A different solution is required to resolve this performance problem for nested outer joins.
* [Revision #ae3cc4f](https://github.com/MariaDB/server/commit/ae3cc4f)\
  2014-09-09 19:03:05 +0200
  * [MDEV-6561](https://jira.mariadb.org/browse/MDEV-6561) libedit detection is broken
* [Revision #2362d98](https://github.com/MariaDB/server/commit/2362d98)\
  2014-09-09 17:37:08 +0300
  * [MDEV-6698](https://jira.mariadb.org/browse/MDEV-6698): safe\_mutex: Found wrong usage of mutex 'log\_space\_lock' and 'LOCK\_log'
* [Revision #20e92c1](https://github.com/MariaDB/server/commit/20e92c1)\
  2014-09-09 06:47:11 -0400
  * FT-591 fix valgrind uninitialized value error in block allocator test caused by reading past the end of a the blockpair array
* [Revision #6748976](https://github.com/MariaDB/server/commit/6748976)\
  2014-09-09 13:35:39 +0300
  * Fix test failure on rpl\_statements test by not listing wsrep variable.
* [Revision #8707f17](https://github.com/MariaDB/server/commit/8707f17)\
  2014-09-09 13:46:33 +0400
  * Merge 10.1 into bb-10.1-mdev6657
* [Revision #bf30585](https://github.com/MariaDB/server/commit/bf30585)\
  2014-09-09 13:26:23 +0400
  * [MDEV-465](https://jira.mariadb.org/browse/MDEV-465): Optimizer : wrong index choice: Add a testcase.
* [Revision #8bd4716](https://github.com/MariaDB/server/commit/8bd4716)\
  2014-09-09 13:05:28 +0400
  * Merge ../10.1-orderby-fixes into 10.1
* [Revision #9c79227](https://github.com/MariaDB/server/commit/9c79227)\
  2014-09-08 20:56:56 +0300
  * Fixed two bugs with CREATE OR REPLACE and LOCK TABLES: [MDEV-6560](https://jira.mariadb.org/browse/MDEV-6560) Assertion `! is_set() ' failed in Diagnostics_area::set_ok_status on killing CREATE OR REPLACE [MDEV-6525](https://jira.mariadb.org/browse/MDEV-6525) Assertion` table->pos\_in\_locked \_tables == null || table->pos\_in\_locked\_tables->table = table' failed in mark\_used\_tables\_as\_free\_for\_reuse, locking problems and binlogging problems on CREATE OR REPLACE under lock.
* [Revision #26e048f](https://github.com/MariaDB/server/commit/26e048f)\
  2014-09-08 13:19:20 -0400
  * Merged sys\_vars.wsrep\_\* tests from maria-10.0-galera tree.
* [Revision #6b720ae](https://github.com/MariaDB/server/commit/6b720ae)\
  2014-09-08 18:38:13 +0200
  * [MDEV-6605](https://jira.mariadb.org/browse/MDEV-6605) Multiple Clients Inserting Causing Error: Failed to read auto-increment value from storage engine
* [Revision #8deb906](https://github.com/MariaDB/server/commit/8deb906)\
  2014-09-08 17:10:48 +0200
  * fix compilation on windows - wrong include file
* [Revision #7c58dd8](https://github.com/MariaDB/server/commit/7c58dd8)\
  2014-09-08 15:12:18 +0300
  * Fix another set of test failures caused by galera merge.
* [Revision #4d4ce59](https://github.com/MariaDB/server/commit/4d4ce59)\
  2014-09-08 12:59:57 +0200
  * compilation fixes for WITH\_ATOMIC\_OPS=rwlocks
* [Revision #d7fd3ff](https://github.com/MariaDB/server/commit/d7fd3ff)\
  2014-09-08 09:36:15 +0300
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #d3ceb93](https://github.com/MariaDB/server/commit/d3ceb93)\
  2014-09-08 09:34:03 +0300
  * [MDEV-6701](https://jira.mariadb.org/browse/MDEV-6701): InnoDB tests fail in 10.1
* [Revision #efc93eb](https://github.com/MariaDB/server/commit/efc93eb)\
  2014-09-07 22:04:29 +0200
  * typos in cmake -DWITH\_ATOMIC\_OPS=xxx
* [Revision #0835f57](https://github.com/MariaDB/server/commit/0835f57)\
  2014-09-07 20:40:36 +0200
  * [MDEV-6638](https://jira.mariadb.org/browse/MDEV-6638) mysql\_options4 symbol missing from libmysqlclient.so.18
* [Revision #bab6dab](https://github.com/MariaDB/server/commit/bab6dab)\
  2014-09-07 20:19:29 +0200
  * compilation failure on x86
* [Revision #9f0bdda](https://github.com/MariaDB/server/commit/9f0bdda)\
  2014-09-07 20:19:12 +0200
  * [MDEV-6580](https://jira.mariadb.org/browse/MDEV-6580) Assertion \`thd' failed in my\_malloc\_size\_cb\_func upon writing status report into error log
* [Revision #ca35033](https://github.com/MariaDB/server/commit/ca35033)\
  2014-09-07 20:18:17 +0200
  * [MDEV-6562](https://jira.mariadb.org/browse/MDEV-6562) [MDEV-6410](https://jira.mariadb.org/browse/MDEV-6410) breaks WITHOUT\_SERVER build
* [Revision #a1c3656](https://github.com/MariaDB/server/commit/a1c3656)\
  2014-09-06 18:08:28 +0200\
  \*
  * Fix [MDEV-6624](https://jira.mariadb.org/browse/MDEV-6624) (indexing on void table) modified: storage/connect/ha\_connect.cc
* [Revision #638075e](https://github.com/MariaDB/server/commit/638075e)\
  2014-09-06 09:59:01 +0200
  * [MDEV-6577](https://jira.mariadb.org/browse/MDEV-6577) auth\_socket.so does not build in kFreeBSD
* [Revision #695781a](https://github.com/MariaDB/server/commit/695781a)\
  2014-09-06 09:51:34 +0200
  * [MDEV-6595](https://jira.mariadb.org/browse/MDEV-6595) \[PATCH] HPPA: storage/xtradb/os/os0stacktrace.c:88:54: error: invalid operands to binary & (have 'void \*' and 'long unsigned int')
* [Revision #0c148e4](https://github.com/MariaDB/server/commit/0c148e4)\
  2014-09-06 09:46:41 +0200
  * [MDEV-6610](https://jira.mariadb.org/browse/MDEV-6610) Assertion \`thd->is\_error() || thd->killed' failed in mysql\_execute\_command on executing an SP with repeated CREATE TABLE .. SELECT
* [Revision #3da7619](https://github.com/MariaDB/server/commit/3da7619)\
  2014-09-06 08:33:56 +0200
  * [MDEV-6616](https://jira.mariadb.org/browse/MDEV-6616) Server crashes in my\_hash\_first if shutdown is performed when FLUSH LOGS is running
* [Revision #1a43425](https://github.com/MariaDB/server/commit/1a43425)\
  2014-09-05 09:49:27 -0400
  * DB-310 run tokudb\_support\_xa.test on mysql and [mariadb 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series)
* [Revision #4aac44d](https://github.com/MariaDB/server/commit/4aac44d)\
  2014-09-05 14:18:31 +0200\
  \*
  * Fix [MDEV-6686](https://jira.mariadb.org/browse/MDEV-6686) (buffer overflow in MakeRecord) modified: storage/connect/ha\_connect.cc
* [Revision #ef579d8](https://github.com/MariaDB/server/commit/ef579d8)\
  2014-09-05 13:17:54 +0800
  * DB-310 add tokudb\_support\_xa variable this variable scope is Global, Session type is boolean and default value is TRUE
* [Revision #9392d0e](https://github.com/MariaDB/server/commit/9392d0e)\
  2014-09-04 21:58:48 +0400\
  \*
  * [MDEV-6695](https://jira.mariadb.org/browse/MDEV-6695) Bad column name for UCS2 string literals The Item\_string constructors called set\_name() on the source string, which was wrong because in case of UCS2/UTF16/UTF32 the source value might be a not well formed string (e.g. have incomplete leftmost character). Now set\_name() is called on str\_value after its copied (with optionally left zero padding) from the source string. - [MDEV-6694](https://jira.mariadb.org/browse/MDEV-6694) Illegal mix of collation with a PS parameter Item\_param::convert\_str\_value() did not set repertoire. Introducing a new structure MY\_STRING\_METADATA to collect character length and repertoire of a string in a single loop, to avoid two separate loops. Adding a new class Item\_basic\_value::Metadata as a convenience wrapper around MY\_STRING\_METADATA, to reuse the code between Item\_string and Item\_param.
* [Revision #bf4347e](https://github.com/MariaDB/server/commit/bf4347e)\
  2014-09-04 12:43:41 +0400
  * Creating a new class in\_string::Item\_string\_for\_in\_vector and moving set\_value() from Item\_string to Item\_string\_for\_in\_vector, as set\_value() updates the members incompletely (e.g. does not update max\_length), so it was dangerous to have set\_value() available in Item\_string.
* [Revision #c9d3b27](https://github.com/MariaDB/server/commit/c9d3b27)\
  2014-09-04 12:15:05 +0400
  * Using more Item\_string\_sys
* [Revision #58eb51d](https://github.com/MariaDB/server/commit/58eb51d)\
  2014-09-04 08:50:06 +0400
  * [MDEV-6044](https://jira.mariadb.org/browse/MDEV-6044) MySQL BUG#12735829 - SPACE() FUNCTION WARNING REFERS TO REPEAT() IN ER\_WARN\_ALLOWED\_PACKET\_OVERFLOWED Merged from 5.6
* [Revision #d161546](https://github.com/MariaDB/server/commit/d161546)\
  2014-09-04 01:12:49 +0400
  * [MDEV-6689](https://jira.mariadb.org/browse/MDEV-6689): valgrind errors in view.test in 10.1
* [Revision #cf3dae3](https://github.com/MariaDB/server/commit/cf3dae3)\
  2014-09-03 14:52:48 -0400
  * FT-273 Be more specific about why memcmp magic is interesting
* [Revision #40165a1](https://github.com/MariaDB/server/commit/40165a1)\
  2014-09-03 14:38:04 -0400
  * FT-273 Prevent setting the memcmp magic on db handles for which a FT is already open. Improve comments. Add a test.
* [Revision #1e66871](https://github.com/MariaDB/server/commit/1e66871)\
  2014-09-03 18:24:31 +0400
  * Adding Item\_string\_sys and Item\_string\_ascii to reduce duplicate code
* [Revision #e42f4e3](https://github.com/MariaDB/server/commit/e42f4e3)\
  2014-09-03 16:31:47 +0400
  * [MDEV-6688](https://jira.mariadb.org/browse/MDEV-6688) Illegal mix of collation with bit string B'01100001'
* [Revision #507da24](https://github.com/MariaDB/server/commit/507da24)\
  2014-09-03 08:13:49 -0400
  * DB-718 test case for broken error handling in tokudb\_fractal\_tree\_info info schema plugin
* [Revision #b7feee7](https://github.com/MariaDB/server/commit/b7feee7)\
  2014-09-03 07:50:03 -0400
  * Merge branch 'master' of github.com:Tokutek/tokudb-engine
* [Revision #f7c43e4](https://github.com/MariaDB/server/commit/f7c43e4)\
  2014-09-03 07:49:52 -0400
  * DB-718 handle errors in tokudb info schema plugins
* [Revision #454037b](https://github.com/MariaDB/server/commit/454037b)\
  2014-09-03 07:37:13 +0300
  * [MDEV-6682](https://jira.mariadb.org/browse/MDEV-6682) innodb.innodb\_simulate\_comp\_failures\_small is too slow if it's run on a real disk
* [Revision #ddc9e74](https://github.com/MariaDB/server/commit/ddc9e74)\
  2014-09-02 16:23:32 -0400
  * DB-717 add iterations limit to tokustat
* [Revision #d4fb687](https://github.com/MariaDB/server/commit/d4fb687)\
  2014-09-02 15:44:49 -0400
  * Merge branch 'master' of github.com:Tokutek/tokudb-engine
* [Revision #561edb1](https://github.com/MariaDB/server/commit/561edb1)\
  2014-09-02 15:44:40 -0400
  * DB-717 add iterations limit to tokustat
* [Revision #6ee0e1c](https://github.com/MariaDB/server/commit/6ee0e1c)\
  2014-09-02 13:01:56 -0400
  * DB-716 use jemalloc 3.6.0 in tokudb builds
* [Revision #9d28e3a](https://github.com/MariaDB/server/commit/9d28e3a)\
  2014-09-02 12:29:55 -0400
  * FT-548 fix dirty upgrade build on osx problem
* [Revision #2f04fc2](https://github.com/MariaDB/server/commit/2f04fc2)\
  2014-09-02 11:53:49 -0400
  * FT-548 fix dirty upgrade build on osx problem
* [Revision #c945233](https://github.com/MariaDB/server/commit/c945233)\
  2014-09-02 18:54:29 +0400
  * [MDEV-6657](https://jira.mariadb.org/browse/MDEV-6657): Poor plan choice for ORDER BY key DESC optimization...
* [Revision #ed9df11](https://github.com/MariaDB/server/commit/ed9df11)\
  2014-09-02 09:55:24 -0400
  * FT-548 support upgrade after dirty shutdown of versions 25 through 27
* [Revision #36f50be](https://github.com/MariaDB/server/commit/36f50be)\
  2014-09-02 14:07:01 +0200
  * [MDEV-6462](https://jira.mariadb.org/browse/MDEV-6462): Slave replicating using GTID doesn't recover correctly when master crashes in the middle of transaction
* [Revision #fbaaf36](https://github.com/MariaDB/server/commit/fbaaf36)\
  2014-09-03 01:56:21 +0400
  * Moving Item::str\_value from public to protected.
* [Revision #658a1e9](https://github.com/MariaDB/server/commit/658a1e9)\
  2014-09-03 01:47:39 +0400
  * [MDEV-6683](https://jira.mariadb.org/browse/MDEV-6683) A parameter and a string literal with the same values are not recognized as equal by the optimizer
* [Revision #c70caca](https://github.com/MariaDB/server/commit/c70caca)\
  2014-09-02 22:04:48 +0400
  * [MDEV-6679](https://jira.mariadb.org/browse/MDEV-6679) Different optimizer plan for "a BETWEEN 'string' AND ?" and "a BETWEEN ? AND 'string'" Item\_string::eq() and Item\_param::eq() in string context behaved differently. Introducing a new class Item\_basic\_value to share the eq() code between literals (Item\_int, Item\_double, Item\_string, Item\_null) and Item\_param.
* [Revision #e2bf602](https://github.com/MariaDB/server/commit/e2bf602)\
  2014-09-02 17:50:09 +0300
  * [MDEV-6682](https://jira.mariadb.org/browse/MDEV-6682) innodb.innodb\_simulate\_comp\_failures\_small is too slow if it's run on a real disk
* [Revision #b088609](https://github.com/MariaDB/server/commit/b088609)\
  2014-09-02 17:34:29 +0400
  * A clean-up for the previous patch
* [Revision #7c1af79](https://github.com/MariaDB/server/commit/7c1af79)\
  2014-09-02 01:40:15 +0200\
  \*
  * Initialise min/max buffer to 0 to avoid valgrind complaining that uninitialised characters be written in op file. modified: storage/connect/tabdos.cpp
* [Revision #1427e1d](https://github.com/MariaDB/server/commit/1427e1d)\
  2014-09-01 20:57:32 +0400
  * [MDEV-6661](https://jira.mariadb.org/browse/MDEV-6661) PI() does not work well in UCS2/UTF16/UTF32 context [MDEV-6666](https://jira.mariadb.org/browse/MDEV-6666) Malformed result for CONCAT(utf8\_column, binary\_string)
* [Revision #6389fd3](https://github.com/MariaDB/server/commit/6389fd3)\
  2014-08-31 19:55:11 +0200
  * [MDEV-6673](https://jira.mariadb.org/browse/MDEV-6673) I\_S.SESSION\_VARIABLES shows global values
* [Revision #6827d3b](https://github.com/MariaDB/server/commit/6827d3b)\
  2014-08-30 06:35:59 -0400
  * FT-312 compile big-shutdown on osx
* [Revision #16de351](https://github.com/MariaDB/server/commit/16de351)\
  2014-08-29 14:22:25 +0200\
  \*
  * Avoid uninitialised warning from valgrind modified: storage/connect/tabdos.cpp
* [Revision #c01c819](https://github.com/MariaDB/server/commit/c01c819)\
  2014-08-29 16:14:11 +0400
  * Backport from 10.0:
* [Revision #4049757](https://github.com/MariaDB/server/commit/4049757)\
  2014-08-29 16:02:46 +0400
  * Backport from 10.0:
* [Revision #e44751b](https://github.com/MariaDB/server/commit/e44751b)\
  2014-08-29 10:11:08 +0300
  * Merge revision 3882 from lp:maria/maria-10.0-galera
* [Revision #31a9411](https://github.com/MariaDB/server/commit/31a9411)\
  2014-08-28 16:25:14 -0400
  * MX-1217 fix TokuMergeLibs to handle empty libs
* [Revision #f7ee3d4](https://github.com/MariaDB/server/commit/f7ee3d4)\
  2014-08-28 15:11:55 -0400
  * DB-712 fix tokudb locks info schema test results due to new schema
* [Revision #967fcd6](https://github.com/MariaDB/server/commit/967fcd6)\
  2014-08-28 06:19:59 -0400
  * Merge branch 'db703' of github.com:Tokutek/tokudb-engine into db703
* [Revision #08eb88e](https://github.com/MariaDB/server/commit/08eb88e)\
  2014-08-28 06:19:32 -0400
  * DB-712 split locks and lock\_waits dname into schema, table, and dictionary
* [Revision #8c5cd26](https://github.com/MariaDB/server/commit/8c5cd26)\
  2014-08-28 06:19:32 -0400
  * DB-703 DB-704 split dname into schema, table, and dictionary
* [Revision #5a684f8](https://github.com/MariaDB/server/commit/5a684f8)\
  2014-08-28 07:01:06 +0300
  * Fix typo.
* [Revision #eff5ef7](https://github.com/MariaDB/server/commit/eff5ef7)\
  2014-08-28 06:49:58 +0300
  * Rule for configure wsrep-notify was missing.
* [Revision #b585b4f](https://github.com/MariaDB/server/commit/b585b4f)\
  2014-08-27 18:00:57 -0400
  * DB-713 separate some long running tokudb tests so that valgrind runs without --big-test can exclude them
* [Revision #5c4c580](https://github.com/MariaDB/server/commit/5c4c580)\
  2014-08-27 18:00:19 -0400
  * DB-713 separate some long running tokudb tests so that valgrind runs without --big-test can exclude them
* [Revision #f8f8a59](https://github.com/MariaDB/server/commit/f8f8a59)\
  2014-08-27 23:31:27 +0400
  * Forgot one file in previous commit
* [Revision #f883f3e](https://github.com/MariaDB/server/commit/f883f3e)\
  2014-08-12 14:05:35 +0200
  * git: ignore errmsg.sys and typescript, better diff header for C/C++ files
* [Revision #f704ecb](https://github.com/MariaDB/server/commit/f704ecb)\
  2014-08-27 14:49:11 -0400
  * DB-712 split locks and lock\_waits dname into schema, table, and dictionary
* [Revision #aed2c26](https://github.com/MariaDB/server/commit/aed2c26)\
  2014-08-27 14:07:16 -0400
  * DB-703 DB-704 split dname into schema, table, and dictionary
* [Revision #422b99e](https://github.com/MariaDB/server/commit/422b99e)\
  2014-08-27 20:00:13 +0300
  * Fix incorrect merge.
* [Revision #8cd0871](https://github.com/MariaDB/server/commit/8cd0871)\
  2014-08-27 19:53:19 +0300
  * Move galera\_sst\_mode test to correct location. This test tests mysqldump option.
* [Revision #f1a1683](https://github.com/MariaDB/server/commit/f1a1683)\
  2014-08-27 20:08:32 +0400
  * [MDEV-6384](https://jira.mariadb.org/browse/MDEV-6384): It seems like OPTIMIZER take into account the order of indexes in the table
* [Revision #be00e27](https://github.com/MariaDB/server/commit/be00e27)\
  2014-08-27 18:47:33 +0400
  * [MDEV-6480](https://jira.mariadb.org/browse/MDEV-6480): Remove conditions for which range optimizer returned SEL\_ARG::IMPOSSIBLE
* [Revision #6650427](https://github.com/MariaDB/server/commit/6650427)\
  2014-08-27 10:31:45 -0400
  * DB-702 print upgrade failed clean shutdown required error message
* [Revision #86a3343](https://github.com/MariaDB/server/commit/86a3343)\
  2014-08-27 14:56:20 +0200\
  \*
  * Fix a bug in DOSFAM::OpenTableFile. Bin was not set to TRUE for blocked tables. This caused a CR character to be left in the line and in particular caused the updelx test to fail on Windows. modified: storage/connect/filamtxt.cpp
* [Revision #6907da2](https://github.com/MariaDB/server/commit/6907da2)\
  2014-08-27 15:35:49 +0300
  * Fix small error on LZMA compression error printout.
* [Revision #a60ea19](https://github.com/MariaDB/server/commit/a60ea19)\
  2014-08-27 15:19:45 +0300
  * Fix compiler error when WITH\_WSREP is not used.
* [Revision #ab15012](https://github.com/MariaDB/server/commit/ab15012)\
  2014-08-27 13:15:37 +0300
  * [MDEV-6247](https://jira.mariadb.org/browse/MDEV-6247): Merge 10.0-galera to 10.1.
* [Revision #66ffa09](https://github.com/MariaDB/server/commit/66ffa09)\
  2014-08-27 00:49:07 +0200\
  \*
  * Fix a test failure. Due to mmap on void file being accepted on Windows while returning an error on Linux. Now accepted on linux. modified: storage/connect/maputil.cpp
* [Revision #8db687e](https://github.com/MariaDB/server/commit/8db687e)\
  2014-08-26 14:28:16 -0400
  * FT-590 Calculate a node's weight using a 64 bit integer to prevent overflow
* [Revision #20e20f6](https://github.com/MariaDB/server/commit/20e20f6)\
  2014-08-26 15:46:19 +0300
  * Merge branch 'bb-10.1-galera' of github.com:MariaDB/server into bb-10.1-galera
* [Revision #df4dd59](https://github.com/MariaDB/server/commit/df4dd59)\
  2014-08-06 15:39:15 +0300
  * [MDEV-6247](https://jira.mariadb.org/browse/MDEV-6247): Merge 10.0-galera to 10.1.
* [Revision #9534fd8](https://github.com/MariaDB/server/commit/9534fd8)\
  2014-08-26 16:24:40 +0400
  * [MDEV-6634](https://jira.mariadb.org/browse/MDEV-6634): Wrong estimates for ref(const): Update test result
* [Revision #ea4103d](https://github.com/MariaDB/server/commit/ea4103d)\
  2014-08-26 14:32:15 +0300
  * Add missing test files for new configuration variables.
* [Revision #bb11eb8](https://github.com/MariaDB/server/commit/bb11eb8)\
  2014-08-26 14:57:09 +0400
  * [MDEV-6305](https://jira.mariadb.org/browse/MDEV-6305) - UNINIT\_VAR emits code in non-debug builds
* [Revision #fe4f467](https://github.com/MariaDB/server/commit/fe4f467)\
  2014-08-26 12:32:21 +0300
  * Merge lp:maria/maria-10.0-galera revisions 3867..3869 and 3871..3879.
* [Revision #8f0e752](https://github.com/MariaDB/server/commit/8f0e752)\
  2014-08-25 18:51:53 +0200\
  \*
  * Adding a test for indexed UPDATE/DELETE added: storage/connect/mysql-test/connect/r/updelx.result storage/connect/mysql-test/connect/t/updelx.inc storage/connect/mysql-test/connect/t/updelx.test
* [Revision #da69d41](https://github.com/MariaDB/server/commit/da69d41)\
  2014-08-25 18:34:51 +0200\
  \*
  * Make storing and sorting values using less memory allocation (while doing indexed UPDATE/DELETE) modified: storage/connect/array.cpp storage/connect/filamtxt.cpp
* [Revision #dd25e7f](https://github.com/MariaDB/server/commit/dd25e7f)\
  2014-08-25 16:58:19 +0200
  * [MDEV-6601](https://jira.mariadb.org/browse/MDEV-6601) Assertion \`!thd->in\_active\_multi\_stmt\_transa ction() || thd->in\_multi\_stmt\_transaction\_mode()' failed on executing a stored procedure with commit
* [Revision #18b307a](https://github.com/MariaDB/server/commit/18b307a)\
  2014-08-25 13:35:33 +0300
  * [MDEV-6590](https://jira.mariadb.org/browse/MDEV-6590): InnoDB recover ends in signal 11
* [Revision #a0150fe](https://github.com/MariaDB/server/commit/a0150fe)\
  2014-08-24 12:56:35 -0400
  * FT-312 fix centos compile
* [Revision #88a7ade](https://github.com/MariaDB/server/commit/88a7ade)\
  2014-08-24 08:45:19 -0400
  * FT-312 speedup shutdown by parallelizing compression
* [Revision #22e8ab4](https://github.com/MariaDB/server/commit/22e8ab4)\
  2014-08-24 11:19:02 +0200\
  \*
  * Fix a compile error on Linux modified: storage/connect/tabmul.cpp
* [Revision #378878e](https://github.com/MariaDB/server/commit/378878e)\
  2014-08-24 12:36:51 +0400
  * [MDEV-6634](https://jira.mariadb.org/browse/MDEV-6634): Wrong estimates for ref(const) and key IS NULL predicate
* [Revision #74a4672](https://github.com/MariaDB/server/commit/74a4672)\
  2014-08-23 19:17:15 +0200\
  \*
  * Move DataPath from the MYCAT catalog to the ha\_connect handler. Indeed it belongs to each tables and the catalog being share between several instances of CONNECT, when a query implied several tables belonging to different databases, some where pointing on the wrong database. This fix bugs occuring in queries such as: INSERT into db1.t1 select \* from db2.t2; Where the t1 data file was made in db2. modified: storage/connect/catalog.h storage/connect/connect.cc storage/connect/filamdbf.cpp storage/connect/filamdbf.h storage/connect/ha\_connect.cc storage/connect/ha\_connect.h storage/connect/mycat.cc storage/connect/mycat.h storage/connect/plgdbsem.h storage/connect/plgdbutl.cpp storage/connect/reldef.cpp storage/connect/reldef.h storage/connect/tabfix.h storage/connect/tabfmt.cpp storage/connect/tabfmt.h storage/connect/tabmul.cpp
* [Revision #b5dd1e7](https://github.com/MariaDB/server/commit/b5dd1e7)\
  2014-08-23 10:58:26 -0400
  * FT-586 FT-563 change ft-verify to work with promotion
* [Revision #62f40f4](https://github.com/MariaDB/server/commit/62f40f4)\
  2014-08-22 21:59:56 +0300
  * Fix merge errors.
* [Revision #f930f4e](https://github.com/MariaDB/server/commit/f930f4e)\
  2014-08-22 17:30:22 +0200\
  \*
  * Add a new CONNECT global variable allowing to tell whether or not a temporary file should be used for UPDATE/DELETE of file tables. Also use the "sorted" argument of index\_init to help decide if sorting of positions must be done. modified: storage/connect/checklvl.h storage/connect/connect.cc storage/connect/connect.h storage/connect/filamdbf.cpp storage/connect/filamfix.cpp storage/connect/filamfix.h storage/connect/filamtxt.cpp storage/connect/ha\_connect.cc storage/connect/mysql-test/connect/r/part\_table.result storage/connect/plgdbsem.h storage/connect/plgdbutl.cpp storage/connect/reldef.cpp storage/connect/tabdos.cpp storage/connect/tabdos.h storage/connect/tabfix.cpp storage/connect/tabfmt.cpp storage/connect/tabvct.cpp storage/connect/tabvct.h storage/connect/xindex.cpp
* [Revision #6119509](https://github.com/MariaDB/server/commit/6119509)\
  2014-08-22 07:57:47 -0400
  * FT-584 use trylock inside of the lock tree manager get\_status function so that it is non-blocking
* [Revision #4521a53](https://github.com/MariaDB/server/commit/4521a53)\
  2014-08-22 08:43:57 +0300
  * Fix merge error.
* [Revision #ff5a25c](https://github.com/MariaDB/server/commit/ff5a25c)\
  2014-08-21 19:21:21 -0400
  * FT-584 use trylock inside of the lock tree manager get\_status function so that it is non-blocking
* [Revision #4cb144d](https://github.com/MariaDB/server/commit/4cb144d)\
  2014-08-21 16:29:50 -0400
  * Add common cmake build directory names to .gitignore
* [Revision #f176b29](https://github.com/MariaDB/server/commit/f176b29)\
  2014-08-21 15:35:07 -0400
  * FT-396 Rename various tokudb-containing functions and comments to instead refer to tokuft
* [Revision #7316bac](https://github.com/MariaDB/server/commit/7316bac)\
  2014-08-21 15:35:06 -0400
  * FT-396 Rename TokuDB to TokuFT in each license header
* [Revision #d569f7a](https://github.com/MariaDB/server/commit/d569f7a)\
  2014-08-21 15:35:06 -0400
  * FT-513 Remove some windows cruft
* [Revision #a57387d](https://github.com/MariaDB/server/commit/a57387d)\
  2014-08-21 15:35:06 -0400
  * FT-512 Remove the majority of the remaining BDB artifacts
* [Revision #feb5b70](https://github.com/MariaDB/server/commit/feb5b70)\
  2014-08-21 15:35:06 -0400
  * FT-582 Remove remaining artifacts from the ICC days
* [Revision #1a34a13](https://github.com/MariaDB/server/commit/1a34a13)\
  2014-08-21 15:35:06 -0400
  * FT-581 Remove dead rdtsc code
* [Revision #addd9c3](https://github.com/MariaDB/server/commit/addd9c3)\
  2014-08-21 15:35:06 -0400
  * FT-580 Remove unused scripts
* [Revision #674454b](https://github.com/MariaDB/server/commit/674454b)\
  2014-08-21 15:35:06 -0400
  * FT-583 Remove sub\_block\_map.h, dead code from old format verisons
* [Revision #9b00476](https://github.com/MariaDB/server/commit/9b00476)\
  2014-08-21 15:34:22 -0400
  * FT-585 Move serialize and compression size calculations around so we can malloc one large buffer to serialize a node instead of many smaller ones, which should hopefully put less pressure on jemalloc during checkpoints etc.
* [Revision #effa06e](https://github.com/MariaDB/server/commit/effa06e)\
  2014-08-21 15:34:18 -0400
  * Clean up toku\_ft\_handle\_close
* [Revision #5a18a1b](https://github.com/MariaDB/server/commit/5a18a1b)\
  2014-08-21 15:34:14 -0400
  * FT-440 Use a scoped malloc during garbage collection and for checkpoint cachefiles, also clean up some formatting.
* [Revision #57a43b8](https://github.com/MariaDB/server/commit/57a43b8)\
  2014-08-21 21:25:22 +0200
  * [MDEV-6625](https://jira.mariadb.org/browse/MDEV-6625) SHOW GRANTS for current\_user\_name@wrong\_host\_name
* [Revision #79180d8](https://github.com/MariaDB/server/commit/79180d8)\
  2014-08-21 19:35:13 +0300
  * Fix Windows compiler errors.
* [Revision #21b4dec](https://github.com/MariaDB/server/commit/21b4dec)\
  2014-08-21 16:08:51 +0300
  * Review fixes.
* [Revision #1826cca](https://github.com/MariaDB/server/commit/1826cca)\
  2014-08-20 11:22:26 -0400
  * Tokutek/mariadb-5.5#71 run part\_index\_scan on mariadb
* [Revision #56ed8eb](https://github.com/MariaDB/server/commit/56ed8eb)\
  2014-08-20 11:21:35 -0400
  * \#261 run multiple queries in part\_index\_scan
* [Revision #9120714](https://github.com/MariaDB/server/commit/9120714)\
  2014-08-19 17:09:28 -0400
  * DB-708 move test scripts
* [Revision #e502d3e](https://github.com/MariaDB/server/commit/e502d3e)\
  2014-08-19 17:09:11 -0400
  * DB-504 test replace select triggers for bulk fetch
* [Revision #bdef225](https://github.com/MariaDB/server/commit/bdef225)\
  2014-08-19 17:08:51 -0400
  * DB-504 move bulk fetch tests
* [Revision #4acb007](https://github.com/MariaDB/server/commit/4acb007)\
  2014-08-19 17:08:33 -0400
  * DB-504 test insert select with various triggers to make sure that bulk fetch will work
* [Revision #71208af](https://github.com/MariaDB/server/commit/71208af)\
  2014-08-19 17:08:14 -0400
  * DB-500 allow simple deletes to use bulk fetch
* [Revision #667401c](https://github.com/MariaDB/server/commit/667401c)\
  2014-08-19 17:07:48 -0400
  * FT-502 print huge pages guy when env fails to open
* [Revision #09223b2](https://github.com/MariaDB/server/commit/09223b2)\
  2014-08-19 13:07:19 -0400
  * DB-708 move test scripts
* [Revision #5569132](https://github.com/MariaDB/server/commit/5569132)\
  2014-08-19 19:28:35 +0300
  * [MDEV-6450](https://jira.mariadb.org/browse/MDEV-6450) - MariaDB crash on Power8 when built with advance tool chain
* [Revision #f1c1c04](https://github.com/MariaDB/server/commit/f1c1c04)\
  2014-08-19 15:18:18 +0400
  * [MDEV-4262](https://jira.mariadb.org/browse/MDEV-4262) - P\_S discovery
* [Revision #adf1e56](https://github.com/MariaDB/server/commit/adf1e56)\
  2014-08-18 15:58:49 -0400
  * DB-504 test replace select triggers for bulk fetch
* [Revision #401e0e5](https://github.com/MariaDB/server/commit/401e0e5)\
  2014-08-18 15:57:12 -0400
  * DB-504 move bulk fetch tests
* [Revision #0bce0db](https://github.com/MariaDB/server/commit/0bce0db)\
  2014-08-18 14:45:39 -0400
  * DB-504 test insert select with various triggers to make sure that bulk fetch will work
* [Revision #96fbab5](https://github.com/MariaDB/server/commit/96fbab5)\
  2014-08-18 13:38:51 -0400
  * DB-500 allow simple deletes to use bulk fetch
* [Revision #9e079da](https://github.com/MariaDB/server/commit/9e079da)\
  2014-08-18 09:13:29 -0400
  * FT-502 print huge pages guy when env fails to open
* [Revision #e7669cf](https://github.com/MariaDB/server/commit/e7669cf)\
  2014-08-18 10:55:01 +0300
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #8984bef](https://github.com/MariaDB/server/commit/8984bef)\
  2014-08-18 10:52:59 +0300
  * [MDEV-6172](https://jira.mariadb.org/browse/MDEV-6172): Monitor progress of ALTER TABLE ... ADD INDEX, ALGORITHM=INPLACE for InnoDB
* [Revision #55b4764](https://github.com/MariaDB/server/commit/55b4764)\
  2014-08-15 22:54:07 +0100
  * [MDEV-6579](https://jira.mariadb.org/browse/MDEV-6579): Properly handle gen\_pfs\_lex\_token when cross-compiling
* [Revision #8b9ed85](https://github.com/MariaDB/server/commit/8b9ed85)\
  2014-08-15 18:05:10 +0200\
  \*
  * Remove a gcc warning modified: storage/connect/xindex.cpp
* [Revision #3a69c85](https://github.com/MariaDB/server/commit/3a69c85)\
  2014-08-16 16:46:35 +0200\
  \*
  * Modifies the way indexed UPDATE/DELETE are sorted in order to execute them sorted by file position. Firstly a new value is stored in indexes to know if they are sorted, preventing to do the sorting when it is not needed. Secondly, almost all in now done in connect instead of being done by the different file access method classes. This pepares the future use of temporary files for all table types and also fix the bug that was occuring when partially using a multi-column index because of false MRR like call of position followed by unsorted rnd\_pos no more using indexing. modified: storage/connect/connect.cc storage/connect/filamap.cpp storage/connect/filamap.h storage/connect/filamdbf.cpp storage/connect/filamdbf.h storage/connect/filamfix.cpp storage/connect/filamfix.h storage/connect/filamtxt.cpp storage/connect/filamtxt.h storage/connect/filamvct.cpp storage/connect/filamvct.h storage/connect/tabdos.cpp storage/connect/tabdos.h storage/connect/tabfix.h storage/connect/tabfmt.cpp storage/connect/tabfmt.h storage/connect/xindex.cpp storage/connect/xindex.h storage/connect/xtable.h
* [Revision #65547f3](https://github.com/MariaDB/server/commit/65547f3)\
  2014-08-14 15:18:56 -0400
  * DB-506 add a session variable to enable/disable bulk fetch default enabled
* [Revision #b16b461](https://github.com/MariaDB/server/commit/b16b461)\
  2014-08-14 15:18:27 -0400
  * DB-506 add a session variable to enable/disable bulk fetch default enabled
* [Revision #0c5e04f](https://github.com/MariaDB/server/commit/0c5e04f)\
  2014-08-13 18:07:51 +0400
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #8d3a432](https://github.com/MariaDB/server/commit/8d3a432)\
  2014-08-13 18:06:53 +0400
  * [MDEV-6575](https://jira.mariadb.org/browse/MDEV-6575): main.view --ps-protocol fails in ANALYZE code
* [Revision #f2cbca7](https://github.com/MariaDB/server/commit/f2cbca7)\
  2014-08-13 15:46:39 +0200
  * Change a couple of permissions that cause lintian warnings in .deb packaging and don't really hurt to fix.
* [Revision #6b47e89](https://github.com/MariaDB/server/commit/6b47e89)\
  2014-08-13 15:24:32 +0300
  * Basic test of slave\_run\_triggers\_for\_rbr variable added.
* [Revision #9dc738b](https://github.com/MariaDB/server/commit/9dc738b)\
  2014-08-13 09:37:12 +0300
  * [MDEV-6546](https://jira.mariadb.org/browse/MDEV-6546): innodb.innodb\_simulate\_comp\_failures\_small fails sporadically
* [Revision #2062c9a](https://github.com/MariaDB/server/commit/2062c9a)\
  2014-08-13 09:03:28 +0300
  * [MDEV-6567](https://jira.mariadb.org/browse/MDEV-6567): Raw debug output in the error log.
* [Revision #2345dfa](https://github.com/MariaDB/server/commit/2345dfa)\
  2014-08-12 16:16:02 -0400
  * \#268 Adding bulk fetch MTR test and result files
* [Revision #f011f45](https://github.com/MariaDB/server/commit/f011f45)\
  2014-08-12 16:03:34 -0400
  * \#268 Adding bulk fetch MTR test and result files
* [Revision #880fac8](https://github.com/MariaDB/server/commit/880fac8)\
  2014-08-12 14:41:35 -0400
  * \#272 set tokudb product name
* [Revision #0b72d47](https://github.com/MariaDB/server/commit/0b72d47)\
  2014-08-12 12:56:15 -0400
  * \#272 set TokuDB product name
* [Revision #fd8da99](https://github.com/MariaDB/server/commit/fd8da99)\
  2014-08-12 17:12:08 +0200
  * disable still racy tokudb tests
* [Revision #04eec20](https://github.com/MariaDB/server/commit/04eec20)\
  2014-08-12 16:39:12 +0200
  * [MDEV-5706](https://jira.mariadb.org/browse/MDEV-5706) MariaDB does not build on hurd-i386
* [Revision #fd4a4b8](https://github.com/MariaDB/server/commit/fd4a4b8)\
  2014-08-11 22:43:29 +0100
  * [MDEV-6562](https://jira.mariadb.org/browse/MDEV-6562): Fix WITHOUT\_SERVER build
* [Revision #6a92fe5](https://github.com/MariaDB/server/commit/6a92fe5)\
  2014-08-11 16:47:36 -0400
  * \#271 turn off FT debug flags by default. can be overridden by cmake arguments
* [Revision #ec2641f](https://github.com/MariaDB/server/commit/ec2641f)\
  2014-08-11 16:46:06 -0400
  * Tokutek/mariadb-5.5#71 run part\_index\_scan on mariadb
* [Revision #fd25ba7](https://github.com/MariaDB/server/commit/fd25ba7)\
  2014-08-11 15:05:13 -0400
  * FT-300 Add the ability to include/exclude certain strategies and clean up report formatting a bit. Also strengthen malformed trace detection.
* [Revision #22a6404](https://github.com/MariaDB/server/commit/22a6404)\
  2014-08-11 05:45:45 +0400
  * [MDEV-6274](https://jira.mariadb.org/browse/MDEV-6274) Collation usage statistics Adding collation usage statistics into the feedback plugin I\_S table.
* [Revision #b5ebc21](https://github.com/MariaDB/server/commit/b5ebc21)\
  2014-08-10 14:36:17 +0200
  * sanity
* [Revision #935309b](https://github.com/MariaDB/server/commit/935309b)\
  2014-08-20 15:02:10 +0200
  * Fix test case that requires dbug to not fail in release build.
* [Revision #c6a60f6](https://github.com/MariaDB/server/commit/c6a60f6)\
  2014-08-20 10:59:39 +0200
  * [MDEV-6321](https://jira.mariadb.org/browse/MDEV-6321): close\_temporary\_tables() in format description event not serialised correctly
* [Revision #453c29c](https://github.com/MariaDB/server/commit/453c29c)\
  2014-08-19 14:26:42 +0200
  * [MDEV-6321](https://jira.mariadb.org/browse/MDEV-6321): close\_temporary\_tables() in format description event not serialised correctly
* [Revision #e2b2bde](https://github.com/MariaDB/server/commit/e2b2bde)\
  2014-08-03 15:26:47 +0300
  * Made sql\_log\_slow a session variable
* [Revision #7375f02](https://github.com/MariaDB/server/commit/7375f02)\
  2014-08-03 15:16:56 +0300
  * Changes for using build scripts
* [Revision #b4c74e2](https://github.com/MariaDB/server/commit/b4c74e2)\
  2014-08-03 15:12:53 +0300
  * Change MySQL -> MariaDB inc scripts
* [Revision #3bde139](https://github.com/MariaDB/server/commit/3bde139)\
  2014-08-03 15:12:10 +0300
  * Minor cleanups, fix compiler warnings
* [Revision #78b1bdd](https://github.com/MariaDB/server/commit/78b1bdd)\
  2014-08-08 19:53:44 +0200\
  \*
  * Update part\_file.result to match the test change modified: storage/connect/mysql-test/connect/r/part\_file.result
* [Revision #61c2e7b](https://github.com/MariaDB/server/commit/61c2e7b)\
  2014-08-08 19:46:02 +0200\
  \*
  * Fix [MDEV-6502](https://jira.mariadb.org/browse/MDEV-6502) modified: storage/connect/ha\_connect.cc
* [Revision #4105cbf](https://github.com/MariaDB/server/commit/4105cbf)\
  2014-08-08 17:58:45 +0200
  * after-merge fixes for 10.0-connect
* [Revision #2894758](https://github.com/MariaDB/server/commit/2894758)\
  2014-08-08 16:15:29 +0200
  * 10.0-connect merge
* [Revision #9fffe99](https://github.com/MariaDB/server/commit/9fffe99)\
  2014-08-08 13:53:43 +0200
  * buildbot found failures
* [Revision #ffd9c77](https://github.com/MariaDB/server/commit/ffd9c77)\
  2014-08-08 01:16:32 +0200
  * merge
* [Revision #e19b07e](https://github.com/MariaDB/server/commit/e19b07e)\
  2014-08-07 21:45:54 +0200
  * crash in main.views (and other view + PS tests)
* [Revision #f835588](https://github.com/MariaDB/server/commit/f835588)\
  2014-08-07 19:12:45 +0200\
  \*
  * Commiting merge files
* [Revision #7a7e65b](https://github.com/MariaDB/server/commit/7a7e65b)\
  2014-08-07 18:08:50 +0200
  * Fix rpl.rpl\_semi\_sync\_uninstall\_plugin to work reliably
* [Revision #6fb17a0](https://github.com/MariaDB/server/commit/6fb17a0)\
  2014-08-07 18:06:56 +0200
  * 5.5.39 merge
* [Revision #0219ac1](https://github.com/MariaDB/server/commit/0219ac1)\
  2014-08-07 17:59:21 +0200
  * This is a major update that fixes most of the issues and bugs that have been created by the last addition of new CONNECT features. The version previous to this one is a preliminary test version and should not be distributed.
* [Revision #8035c98](https://github.com/MariaDB/server/commit/8035c98)\
  2014-08-07 09:59:08 -0400
  * [MDEV-6490](https://jira.mariadb.org/browse/MDEV-6490): Post-fix for the failing test.
* [Revision #d87ffeb](https://github.com/MariaDB/server/commit/d87ffeb)\
  2014-08-07 13:44:00 +0300
  * [MDEV-6548](https://jira.mariadb.org/browse/MDEV-6548): Incorrect compression on LZMA.
* [Revision #50777e2](https://github.com/MariaDB/server/commit/50777e2)\
  2014-08-07 13:41:46 +0300
  * Fix Windows compiler error by disabling for now the nullptr class implementation.
* [Revision #42b6c07](https://github.com/MariaDB/server/commit/42b6c07)\
  2014-08-06 19:42:03 -0400
  * [MDEV-6490](https://jira.mariadb.org/browse/MDEV-6490): mysqldump unknown option --galera-sst-mode
* [Revision #abbdc7a](https://github.com/MariaDB/server/commit/abbdc7a)\
  2014-08-06 19:31:13 -0400
  * [MDEV-6118](https://jira.mariadb.org/browse/MDEV-6118): Unable to install "MariaDB-connect-engine" when using "MariaDB-Galera-server"
* [Revision #2023fac](https://github.com/MariaDB/server/commit/2023fac)\
  2014-08-06 20:05:10 +0200
  * innodb-5.6.19
* [Revision #a7f39aa](https://github.com/MariaDB/server/commit/a7f39aa)\
  2014-08-06 19:57:06 +0200
  * xtradb-5.6.19-67.0
* [Revision #098a9c6](https://github.com/MariaDB/server/commit/098a9c6)\
  2014-08-06 19:41:33 +0200
  * perfschema 5.6.20
* [Revision #75af0fc](https://github.com/MariaDB/server/commit/75af0fc)\
  2014-08-06 19:29:02 +0200
  * mysql-5.6.20
* [Revision #415fe3f](https://github.com/MariaDB/server/commit/415fe3f)\
  2014-08-06 19:23:35 +0200
  * percona-server-5.6.19-67.0
* [Revision #627caa3](https://github.com/MariaDB/server/commit/627caa3)\
  2014-08-06 15:53:31 +0200
  * fix the error message when getaddrinfo() fails. on windows "\*" doesn't mean "any address"
* [Revision #5ebb396](https://github.com/MariaDB/server/commit/5ebb396)\
  2014-08-06 15:39:15 +0300
  * [MDEV-6247](https://jira.mariadb.org/browse/MDEV-6247): Merge 10.0-galera to 10.1.
* [Revision #6dad23f](https://github.com/MariaDB/server/commit/6dad23f)\
  2014-08-06 15:28:58 +0300
  * [MDEV-5834](https://jira.mariadb.org/browse/MDEV-5834): Merge Kakao Defragmentation implementation to [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)
* [Revision #75f0f17](https://github.com/MariaDB/server/commit/75f0f17)\
  2014-08-06 14:02:05 +0200
  * [MDEV-6543](https://jira.mariadb.org/browse/MDEV-6543) Crash if enable 'federatedx' when 'federated' plugin already enabled, and vice-versa
* [Revision #071a14c](https://github.com/MariaDB/server/commit/071a14c)\
  2014-08-06 13:31:55 +0200
  * cleanup: remove have\_mysql\_upgrade.inc
* [Revision #15a9103](https://github.com/MariaDB/server/commit/15a9103)\
  2014-08-06 13:27:44 +0200
  * [MDEV-6535](https://jira.mariadb.org/browse/MDEV-6535) Ordering of mysql\_upgrade tasks is not optimal
* [Revision #3390291](https://github.com/MariaDB/server/commit/3390291)\
  2014-08-06 12:44:57 +0200
  * typo fixed: only use -ggdb3 when it's supported by the compiler
* [Revision #16e43df](https://github.com/MariaDB/server/commit/16e43df)\
  2014-08-06 11:47:26 +0200
  * main.ipv4\_and\_ipv6 - fails on sid
* [Revision #7629381](https://github.com/MariaDB/server/commit/7629381)\
  2014-08-06 10:26:25 +0200
  * fix main.key\_cache failures on x86
* [Revision #be25382](https://github.com/MariaDB/server/commit/be25382)\
  2014-08-06 10:11:08 +0200
  * compilation failure on labrador
* [Revision #9f252fc](https://github.com/MariaDB/server/commit/9f252fc)\
  2014-08-06 13:07:16 +0400
  * [MDEV-6469](https://jira.mariadb.org/browse/MDEV-6469) - rpl.rpl\_gtid\_basic, rpl.rpl\_gtid\_stop\_start, rpl.rpl\_gtid\_crash fail on PPC64
* [Revision #68d72f9](https://github.com/MariaDB/server/commit/68d72f9)\
  2014-08-05 20:22:57 +0200
  * fix tokudb version
* [Revision #15c3454](https://github.com/MariaDB/server/commit/15c3454)\
  2014-08-12 19:14:52 +0400
  * Increased the version number
* [Revision #a4ab243](https://github.com/MariaDB/server/commit/a4ab243)\
  2014-08-05 20:22:57 +0200
  * fix tokudb version
* [Revision #761ed3d](https://github.com/MariaDB/server/commit/761ed3d)\
  2014-08-05 18:35:20 +0200
  * change Aria engine maturity to STABLE
* [Revision #b81b6d3](https://github.com/MariaDB/server/commit/b81b6d3)\
  2014-08-05 17:01:41 +0200\
  \*
  * Fix failing tests. part\_file.test failure was due to a new alter flag that were not taken in acount in check\_if\_supported\_inplace\_alter. mysql.test failure is strange, the suppressed warning should not be made anyway. modified: storage/connect/ha\_connect.cc storage/connect/mysql-test/connect/r/mysql.result
* [Revision #f94e36a](https://github.com/MariaDB/server/commit/f94e36a)\
  2014-08-05 10:28:32 -0400
  * FT-309 Default padded fit alignment should be 4096
* [Revision #053d5ed](https://github.com/MariaDB/server/commit/053d5ed)\
  2014-08-05 14:39:00 +0200
  * [MDEV-5151](https://jira.mariadb.org/browse/MDEV-5151) mysql\_upgrade does not fix "last\_update" in "mysql.innodb\_table\_stats"
* [Revision #aafe43b](https://github.com/MariaDB/server/commit/aafe43b)\
  2014-08-05 14:37:05 +0200
  * cleanup (move ALTER TABLE for comment to be applicable again)
* [Revision #cf4814b](https://github.com/MariaDB/server/commit/cf4814b)\
  2014-08-05 11:47:58 +0200
  * [MDEV-6052](https://jira.mariadb.org/browse/MDEV-6052) Inconsistent results with bit type
* [Revision #ba4cc58](https://github.com/MariaDB/server/commit/ba4cc58)\
  2014-08-04 15:49:28 -0400
  * \#271 turn off FT debug flags by default. can be overridden by cmake arguments
* [Revision #321f589](https://github.com/MariaDB/server/commit/321f589)\
  2014-08-04 21:36:02 +0200
  * [MDEV-6181](https://jira.mariadb.org/browse/MDEV-6181) EITS could eat all tmpdir space and hang
* [Revision #fece177](https://github.com/MariaDB/server/commit/fece177)\
  2014-08-04 21:19:24 +0200
  * mysqltest: support pairs of delimiters in replace\_regex
* [Revision #20fff8e](https://github.com/MariaDB/server/commit/20fff8e)\
  2014-08-04 10:05:51 -0700
  * Merge.
* [Revision #089938c](https://github.com/MariaDB/server/commit/089938c)\
  2014-08-04 18:17:56 +0400
  * Merge 10.0->10.0-connect
* [Revision #82ce2a2](https://github.com/MariaDB/server/commit/82ce2a2)\
  2014-08-04 11:55:38 +0400
  * [MDEV-6450](https://jira.mariadb.org/browse/MDEV-6450) - MariaDB crash on Power8 when built with advance tool chain
* [Revision #ef2bf18](https://github.com/MariaDB/server/commit/ef2bf18)\
  2014-08-03 21:43:59 +0200
  * [MDEV-4379](https://jira.mariadb.org/browse/MDEV-4379) expand MariaDB dual-stack support
* [Revision #6145e16](https://github.com/MariaDB/server/commit/6145e16)\
  2014-08-03 18:58:53 +0200
  * remove unused OPT\_xxx values from mysqld.cc and the related dead code
* [Revision #0661c73](https://github.com/MariaDB/server/commit/0661c73)\
  2014-08-03 18:39:36 +0200
  * [MDEV-6352](https://jira.mariadb.org/browse/MDEV-6352) \[PATCH] mysql\_config prints usage to stdout and exit with 0 if run with unknow option
* [Revision #91c47e6](https://github.com/MariaDB/server/commit/91c47e6)\
  2014-08-03 17:13:56 +0200
  * [MDEV-6485](https://jira.mariadb.org/browse/MDEV-6485) Hard-coded paths in the source cannot be opt-out
* [Revision #c722e5f](https://github.com/MariaDB/server/commit/c722e5f)\
  2014-08-03 13:38:54 +0200
  * [MDEV-6507](https://jira.mariadb.org/browse/MDEV-6507) tokudb release builds compiled with debug code on
* [Revision #50e192a](https://github.com/MariaDB/server/commit/50e192a)\
  2014-08-03 12:45:14 +0200
  * Bug#17638477 UNINSTALL AND INSTALL SEMI-SYNC PLUGIN CAUSES SLAVES TO BREAK
* [Revision #359d764](https://github.com/MariaDB/server/commit/359d764)\
  2014-08-03 07:38:41 +0200
  * fix xtradb on windows (again)
* [Revision #1c6ad62](https://github.com/MariaDB/server/commit/1c6ad62)\
  2014-08-02 21:26:16 +0200
  * mysql-5.5.39 merge
* [Revision #bade886](https://github.com/MariaDB/server/commit/bade886)\
  2014-08-01 13:29:00 -0400
  * FT-300 Proceed with leaked allocators, so that we can partially anaylze a running trace (that is, a trace that is still getting written to by some process)
* [Revision #214f662](https://github.com/MariaDB/server/commit/214f662)\
  2014-08-01 12:59:48 -0400
  * FT-300 Report before and after fragmentation reports so we can see how fragmentation changed
* [Revision #20a2dd6](https://github.com/MariaDB/server/commit/20a2dd6)\
  2014-08-01 12:38:57 -0400
  * FT-300 Use portable printf format strings in the block allocator's tracing code
* [Revision #66fb8ff](https://github.com/MariaDB/server/commit/66fb8ff)\
  2014-08-01 11:29:37 -0400
  * FT-309 Change the way padded-fit allocation alignment works
* [Revision #14200df](https://github.com/MariaDB/server/commit/14200df)\
  2014-08-01 17:04:15 +0200
  * tokudb-7.1.7
* [Revision #4b4de01](https://github.com/MariaDB/server/commit/4b4de01)\
  2014-08-01 16:51:12 +0200
  * 5.3 merge
* [Revision #d8a9bb4](https://github.com/MariaDB/server/commit/d8a9bb4)\
  2014-08-01 14:33:49 +0300
  * Add missing results file.
* [Revision #681fbca](https://github.com/MariaDB/server/commit/681fbca)\
  2014-08-01 12:04:55 +0200
  * fix func\_time.test to be independent from the system time zone
* [Revision #27d23c0](https://github.com/MariaDB/server/commit/27d23c0)\
  2014-08-01 12:54:56 +0300
  * Merged percona-server-5.5.38-35.2.
* [Revision #f735822](https://github.com/MariaDB/server/commit/f735822)\
  2014-07-31 22:17:43 -0700
  * Fixed bug [MDEV-5721](https://jira.mariadb.org/browse/MDEV-5721). Do not define a look-up key for a temporary table if its length exceeds the maximum length of such keys.
* [Revision #30f97cc](https://github.com/MariaDB/server/commit/30f97cc)\
  2014-07-31 22:43:37 -0400
  * FT-300 Add mean / stddev tracking for block allocation sizes to ba\_replay
* [Revision #600a864](https://github.com/MariaDB/server/commit/600a864)\
  2014-07-31 20:57:41 -0400
  * FT-300 Print terse results when verbose = false
* [Revision #b5c0a60](https://github.com/MariaDB/server/commit/b5c0a60)\
  2014-07-31 20:37:35 -0400
  * FT-300 Gather simple trace stats during the first canonical trace replay
* [Revision #bb0b14b](https://github.com/MariaDB/server/commit/bb0b14b)\
  2014-07-31 20:10:47 -0400
  * FT-309 Control heat zone and padded fit size via environment variables
* [Revision #f114195](https://github.com/MariaDB/server/commit/f114195)\
  2014-07-31 19:40:28 -0400
  * FT-300 Fix an issue where \`free' calls on blocks created during create\_from\_blockpairs would crash the replay. Also fix parsing bugs.
* [Revision #4a152ec](https://github.com/MariaDB/server/commit/4a152ec)\
  2014-07-31 18:17:31 -0400
  * FT-309 Fix up tracing code, add a lock (to extend fprintf atomicity to multiple calls), support create\_from\_blockpairs in the allocator and trace tool
* [Revision #4dbb45f](https://github.com/MariaDB/server/commit/4dbb45f)\
  2014-07-31 18:17:31 -0400
  * FT-309 Fix a bug in heat zone, pretty-up the replay's output
* [Revision #a9e8b57](https://github.com/MariaDB/server/commit/a9e8b57)\
  2014-07-31 21:25:13 +0200
  * percona-server-5.5.38-35.2
* [Revision #ed9a5d5](https://github.com/MariaDB/server/commit/ed9a5d5)\
  2014-07-31 12:24:04 -0400
  * \#269 use bulk fetch for replace select
* [Revision #0b49d86](https://github.com/MariaDB/server/commit/0b49d86)\
  2014-07-31 12:23:23 -0400
  * \#269 use bulk fetch for replace select
* [Revision #8fc7c28](https://github.com/MariaDB/server/commit/8fc7c28)\
  2014-07-31 12:19:41 -0400
  * FT-311 create data and log files with the execute bit OFF
* [Revision #59e976d](https://github.com/MariaDB/server/commit/59e976d)\
  2014-07-31 11:04:49 -0400
  * FT-311 create data and log files with the execute bit OFF
* [Revision #53360fd](https://github.com/MariaDB/server/commit/53360fd)\
  2014-07-31 14:31:05 +0400
  * [MDEV-6450](https://jira.mariadb.org/browse/MDEV-6450) - MariaDB crash on Power8 when built with advance tool chain
* [Revision #a40be4c](https://github.com/MariaDB/server/commit/a40be4c)\
  2014-07-31 18:14:37 +0200
  * fix failures in embedded tests
* [Revision #37ba4f3](https://github.com/MariaDB/server/commit/37ba4f3)\
  2014-07-31 13:13:33 +0300
  * Fixed memory overflow
* [Revision #8867a49](https://github.com/MariaDB/server/commit/8867a49)\
  2014-07-31 12:03:20 +0200
  * [MDEV-6050](https://jira.mariadb.org/browse/MDEV-6050) MySQL Bug#13036505 62540: TABLE LOCKS WITHIN STORED FUNCTIONS ARE BACK IN 5.5 WITH MIXED AND ROW BI
* [Revision #de4a3c2](https://github.com/MariaDB/server/commit/de4a3c2)\
  2014-07-31 11:08:56 +0200
  * [MDEV-6312](https://jira.mariadb.org/browse/MDEV-6312) HA\_MUST\_USE\_TABLE\_CONDITION\_PUSHDOWN is not accounted by init\_read\_record()
* [Revision #c39a501](https://github.com/MariaDB/server/commit/c39a501)\
  2014-07-31 14:43:35 +0300
  * Try to fix compiler error seen on Labrador.
* [Revision #e974b56](https://github.com/MariaDB/server/commit/e974b56)\
  2014-07-31 11:31:39 +0300
  * [MDEV-6512](https://jira.mariadb.org/browse/MDEV-6512): InnoDB: Assertion failure in thread 4537024512 in file buf0buf.cc line 2642.
* [Revision #3e9d454](https://github.com/MariaDB/server/commit/3e9d454)\
  2014-07-31 09:51:05 +0200
  * [MDEV-6340](https://jira.mariadb.org/browse/MDEV-6340) [Mariadb 10.0.12](../../old-releases/10.0/10.0.12.md) fatal "Lost connection" error w/ GCC 4.9 'Release' build; workaround \~ CFLAGS="-fno-delete-null-pointer-checks"
* [Revision #c253676](https://github.com/MariaDB/server/commit/c253676)\
  2014-07-31 10:32:52 +0300
  * [MDEV-6506](https://jira.mariadb.org/browse/MDEV-6506): InnoDB: Assertion failure in thread 2810182464 in file buf0flu.cc line 549.
* [Revision #a270e8a](https://github.com/MariaDB/server/commit/a270e8a)\
  2014-07-31 10:11:10 +0300
  * [MDEV-6441](https://jira.mariadb.org/browse/MDEV-6441): memory leak
* [Revision #f9eeeae](https://github.com/MariaDB/server/commit/f9eeeae)\
  2014-07-30 23:16:49 +0300
  * Fixed failing testcase
* [Revision #f680b2c](https://github.com/MariaDB/server/commit/f680b2c)\
  2014-07-30 16:12:42 -0400
  * FT-309 Fix replay tool to not crash when replaying padded-fit
* [Revision #ff647c8](https://github.com/MariaDB/server/commit/ff647c8)\
  2014-07-30 15:44:11 -0400
  * FT-272 Simple block allocator strategy unit test, improved base unit test
* [Revision #1a3d33c](https://github.com/MariaDB/server/commit/1a3d33c)\
  2014-07-30 22:05:47 +0300
  * Automatic merge
* [Revision #14d00cd](https://github.com/MariaDB/server/commit/14d00cd)\
  2014-07-30 22:01:10 +0300
  * Fixed [MDEV-6451](https://jira.mariadb.org/browse/MDEV-6451): "Error 'Table 't1' already exists' on query" with slave\_ddl\_exec\_mode=IDEMPOTENT
* [Revision #7019d45](https://github.com/MariaDB/server/commit/7019d45)\
  2014-07-30 21:58:26 +0300
  * Fixed wrong usage of global\_query\_id. (It's not protected by LOCK\_thread\_count)
* [Revision #0b8ad62](https://github.com/MariaDB/server/commit/0b8ad62)\
  2014-07-30 14:12:25 -0400
  * FT-309 Add padded-fit allocation strategy
* [Revision #5364315](https://github.com/MariaDB/server/commit/5364315)\
  2014-07-30 13:27:52 +0300
  * Fix for [MDEV-6493](https://jira.mariadb.org/browse/MDEV-6493): Assertion \`table->file->stats.records > 0 || error' failure, or 'Invalid write' valgrind warnings, or crash on scenario with Aria table, view, LOCK TABLES
* [Revision #a1c1700](https://github.com/MariaDB/server/commit/a1c1700)\
  2014-07-30 10:05:01 +0300
  * Fixed some compiler warnings
* [Revision #1c61686](https://github.com/MariaDB/server/commit/1c61686)\
  2014-07-29 12:56:43 +0200
  * fix the test to pass on windows (lower\_case\_file\_system)
* [Revision #c1c6f6f](https://github.com/MariaDB/server/commit/c1c6f6f)\
  2014-07-29 12:05:58 +0200
  * [MDEV-5924](https://jira.mariadb.org/browse/MDEV-5924) MariaDB could crash after changing the query\_cache size with SET GLOBAL
* [Revision #6ef1397](https://github.com/MariaDB/server/commit/6ef1397)\
  2014-07-29 09:09:52 +0200
  * [MDEV-6497](https://jira.mariadb.org/browse/MDEV-6497) InnoDB deadlocks on UNINSTALL PLUGIN
* [Revision #4e3796d](https://github.com/MariaDB/server/commit/4e3796d)\
  2014-07-29 06:10:18 +0300
  * Fix compiler error on Windows.
* [Revision #5b452ae](https://github.com/MariaDB/server/commit/5b452ae)\
  2014-07-28 13:47:55 +0400
  * [MDEV-4511](https://jira.mariadb.org/browse/MDEV-4511) Assertion \`scale <= precision' fails on GROUP BY TIMEDIFF with incorrect types [MDEV-6302](https://jira.mariadb.org/browse/MDEV-6302) Wrong result set when using GROUP BY FROM\_UNIXTIME(...)+0 Fixed.
* [Revision #0aa40c3](https://github.com/MariaDB/server/commit/0aa40c3)\
  2014-07-28 13:31:46 +0400
  * [MDEV-6378](https://jira.mariadb.org/browse/MDEV-6378) mtr engines iuds time tests fail
* [Revision #c57c5be](https://github.com/MariaDB/server/commit/c57c5be)\
  2014-07-28 12:47:14 +0400
  * [MDEV-5745](https://jira.mariadb.org/browse/MDEV-5745) analyze MySQL fix for bug#12368495
* [Revision #01faff0](https://github.com/MariaDB/server/commit/01faff0)\
  2014-07-28 09:42:52 +0200
  * disable the test for [MDEV-6351](https://jira.mariadb.org/browse/MDEV-6351) on embedded
* [Revision #a6071cc](https://github.com/MariaDB/server/commit/a6071cc)\
  2014-07-27 21:02:00 +0200
  * [MDEV-6082](https://jira.mariadb.org/browse/MDEV-6082) Assertion \`0' fails in TC\_LOG\_DUMMY::log\_and\_order on DML after installing TokuDB at runtime on server with disabled InnoDB
* [Revision #2936bfd](https://github.com/MariaDB/server/commit/2936bfd)\
  2014-07-27 08:47:37 +0300
  * Merge revision 4244 from 5.5. Fix compiler error on sparc.
* [Revision #1987819](https://github.com/MariaDB/server/commit/1987819)\
  2014-07-26 23:08:38 +0200
  * [MDEV-6428](https://jira.mariadb.org/browse/MDEV-6428) \[PATCH] MariaDB start script doesn't realize failure of MariaDB startup
* [Revision #42b9758](https://github.com/MariaDB/server/commit/42b9758)\
  2014-07-27 08:44:45 +0300
  * Fix compiler error on sparc.
* [Revision #8ae2674](https://github.com/MariaDB/server/commit/8ae2674)\
  2014-07-26 21:14:21 +0300
  * Fix InnoDB: Assertion failure in thread 2868898624 in file buf0lru.c line 1000 InnoDB: Failing assertion: mutex\_own(\&buf\_pool->LRU\_list\_mutex)
* [Revision #476feba](https://github.com/MariaDB/server/commit/476feba)\
  2014-07-26 20:17:59 +0300
  * Fix unnecessary printout of same writer thread more than once. Fixed also a compiler warning.
* [Revision #1f69ff4](https://github.com/MariaDB/server/commit/1f69ff4)\
  2014-07-25 18:45:14 +0300
  * Fix compiler error on Windows.
* [Revision #b95aca7](https://github.com/MariaDB/server/commit/b95aca7)\
  2014-07-25 10:06:39 -0400
  * FT-279 Fix a few missed initializers found by src/tests/keyrange.tdb --get 0 test failure
* [Revision #35c78a1](https://github.com/MariaDB/server/commit/35c78a1)\
  2014-07-25 17:02:47 +0400
  * [MDEV-6489](https://jira.mariadb.org/browse/MDEV-6489) - rpl.rpl\_insert, rpl.rpl\_insert\_delayed and main.mysqlslap fail on PPC64
* [Revision #be667b8](https://github.com/MariaDB/server/commit/be667b8)\
  2014-07-25 14:15:33 +0200
  * [MDEV-5706](https://jira.mariadb.org/browse/MDEV-5706) MariaDB does not build on hurd-i386
* [Revision #56c4b01](https://github.com/MariaDB/server/commit/56c4b01)\
  2014-07-25 14:37:10 +0300
  * Fiix random test failures on fil\_decompress\_page\_2 function.
* [Revision #4d0587c](https://github.com/MariaDB/server/commit/4d0587c)\
  2014-07-25 11:37:07 +0200\
  \*
  * Fix an error pointed out by Valgrind due to uninitialised Correlated variable. This variable is not to be used by CONNECT. modified: storage/connect/array.cpp storage/connect/array.h
* [Revision #a3acd72](https://github.com/MariaDB/server/commit/a3acd72)\
  2014-07-25 10:30:16 +0300
  * Merge InnoDB fixes from 5.5 revisions 4229, 4230, 4233, 4237 and 4238 i.e.
* [Revision #cc4d84a](https://github.com/MariaDB/server/commit/cc4d84a)\
  2014-07-24 16:30:16 -0400
  * FT-279 Constify the comparison operators for cleaniless (and to please the osx build)
* [Revision #45794ea](https://github.com/MariaDB/server/commit/45794ea)\
  2014-07-24 15:38:12 -0400
  * FT-279 Clean up ftnode\_fetch\_extra struct and, most importantly, its initialization code
* [Revision #3e8a298](https://github.com/MariaDB/server/commit/3e8a298)\
  2014-07-24 13:19:30 -0400
  * FT-300 Add 'heat' to the block allocator API, which is a hint for how likely the allocation will need to move again at the next checkpoint (we pass the node height for this value). The new heat zone allocation strategy uses the heat value to put nonleaf nodes towards the end of the file and leaf nodes towards the beginning.
* [Revision #6192f0b](https://github.com/MariaDB/server/commit/6192f0b)\
  2014-07-24 18:12:32 +0400
  * [MDEV-6483](https://jira.mariadb.org/browse/MDEV-6483) - Deadlock around rw\_lock\_debug\_mutex on PPC64
* [Revision #de3ee46](https://github.com/MariaDB/server/commit/de3ee46)\
  2014-07-24 15:50:29 +0200\
  \*
  * Try to fix some test failure modified: storage/connect/mysql-test/connect/t/part\_table.test
* [Revision #44aacfc](https://github.com/MariaDB/server/commit/44aacfc)\
  2014-07-24 09:51:51 +0200
  * fix remaining warnings in manpages (for debian lint ?)
* [Revision #8fc3724](https://github.com/MariaDB/server/commit/8fc3724)\
  2014-07-23 21:44:35 +0200
  * [MDEV-5958](https://jira.mariadb.org/browse/MDEV-5958) Inconsitent handling of invalid arguments for mysqld\_safe
* [Revision #82a4d5d](https://github.com/MariaDB/server/commit/82a4d5d)\
  2014-07-23 13:55:22 -0400
  * Update README.md
* [Revision #f17d5c1](https://github.com/MariaDB/server/commit/f17d5c1)\
  2014-07-23 13:50:34 -0400
  * \#261 run multiple queries in part\_index\_scan
* [Revision #4e6e720](https://github.com/MariaDB/server/commit/4e6e720)\
  2014-07-23 19:36:15 +0200
  * [MDEV-6290](https://jira.mariadb.org/browse/MDEV-6290) Crash in KILL HARD QUERY USER x@y when slave threads are running
* [Revision #0d9ac29](https://github.com/MariaDB/server/commit/0d9ac29)\
  2014-07-23 10:03:34 -0400
  * \#267 fix mdev5932 test and result
* [Revision #fc526ce](https://github.com/MariaDB/server/commit/fc526ce)\
  2014-07-23 10:03:13 -0400
  * \#261 Tokutek/mariadb-5.5#69 run part\_index\_scan test on mariadb
* [Revision #3d4e10e](https://github.com/MariaDB/server/commit/3d4e10e)\
  2014-07-23 10:00:13 -0400
  * \#267 fix mdev5932 test and result
* [Revision #911c481](https://github.com/MariaDB/server/commit/911c481)\
  2014-07-23 12:51:51 +0200
  * cleanup and updated test results
* [Revision #bb66e66](https://github.com/MariaDB/server/commit/bb66e66)\
  2014-07-20 03:23:57 +0000
  * Changed set\_default\_role\_for test to clean up correctly
* [Revision #a3550fe](https://github.com/MariaDB/server/commit/a3550fe)\
  2014-07-20 03:20:15 +0000
  * Extended create\_and\_drop\_role\_invalid\_user\_table
* [Revision #5298996](https://github.com/MariaDB/server/commit/5298996)\
  2014-07-20 03:14:07 +0000
  * Fixed comment.
* [Revision #64b27c7](https://github.com/MariaDB/server/commit/64b27c7)\
  2014-07-13 23:57:10 +0000
  * Added default role implementation
* [Revision #43351fa](https://github.com/MariaDB/server/commit/43351fa)\
  2014-07-13 22:22:31 +0000
  * Added extra error messages for default role.
* [Revision #c55f5d1](https://github.com/MariaDB/server/commit/c55f5d1)\
  2014-05-30 17:54:13 +0300
  * Added default\_role column to mysql\_system\_tables
* [Revision #1907bf0](https://github.com/MariaDB/server/commit/1907bf0)\
  2014-07-23 12:01:05 +0200
  * [MDEV-6409](https://jira.mariadb.org/browse/MDEV-6409) CREATE VIEW replication problem if error occurs in mysql\_register\_view
* [Revision #c104965](https://github.com/MariaDB/server/commit/c104965)\
  2014-07-25 09:34:05 +0300
  * Fix test failure caused by simulated compression failure on IBUF\_DUMMY table.
* [Revision #7bf45be](https://github.com/MariaDB/server/commit/7bf45be)\
  2014-07-24 14:35:09 +0300
  * Fix too agressive long semaphore wait output and add guard against introducing compression failures on insert buffer.
* [Revision #06655a1](https://github.com/MariaDB/server/commit/06655a1)\
  2014-07-23 22:48:31 +0400
  * [MDEV-6322](https://jira.mariadb.org/browse/MDEV-6322): The PARTITION engine can return wrong query results MySQL Bug#71095: Wrong results with PARTITION BY LIST COLUMNS() MySQL Bug#72803: Wrong "Impossible where" with LIST partitioning [MDEV-6240](https://jira.mariadb.org/browse/MDEV-6240): Wrong "Impossible where" with LIST partitioning - Backprot the fix from MySQL Bug#71095.
* [Revision #6b353dd](https://github.com/MariaDB/server/commit/6b353dd)\
  2014-07-23 19:53:29 +0400
  * [MDEV-6289](https://jira.mariadb.org/browse/MDEV-6289) : Unexpected results when querying information\_schema - When traversing JOIN\_TABs with first\_linear\_tab/next\_linear\_tab(), don't forget to enter the semi-join nest when it is the first table in the join order. Failure to do so could cause e.g. I\_S tables not to be filled.
* [Revision #07cb53c](https://github.com/MariaDB/server/commit/07cb53c)\
  2014-07-23 14:59:23 +0400
  * Merge 5.3->5.5
* [Revision #be00265](https://github.com/MariaDB/server/commit/be00265)\
  2014-07-23 13:52:17 +0300
  * Fix compiler errors on product build.
* [Revision #80708da](https://github.com/MariaDB/server/commit/80708da)\
  2014-07-23 13:38:48 +0400
  * [MDEV-5750](https://jira.mariadb.org/browse/MDEV-5750) Assertion \`ltime->year == 0' fails on a query with EXTRACT DAY\_MINUTE and TIME column Item\_func\_min\_max::get\_date() did not clear ltime->year when returning a TIME value.
* [Revision #6b99985](https://github.com/MariaDB/server/commit/6b99985)\
  2014-07-23 11:56:36 +0300
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #47daf3b](https://github.com/MariaDB/server/commit/47daf3b)\
  2014-07-23 11:55:34 +0300
  * Fix default value for innodb\_compression\_algorithm to 0 (uncompressed) to avoid test failures.
* [Revision #d466ed9](https://github.com/MariaDB/server/commit/d466ed9)\
  2014-07-23 12:55:26 +0400
  * [MDEV-6473](https://jira.mariadb.org/browse/MDEV-6473) - main.statistics fails on PPC64
* [Revision #c1d1dc2](https://github.com/MariaDB/server/commit/c1d1dc2)\
  2014-07-22 19:45:25 +0200\
  \*
  * Modif avglen calculation and add AVG\_ROW\_LENGTH option to test This is to get same test results on Linux and Windows modified: storage/connect/mysql-test/connect/r/part\_file.result storage/connect/mysql-test/connect/r/part\_table.result storage/connect/mysql-test/connect/t/part\_file.test storage/connect/mysql-test/connect/t/part\_table.test storage/connect/tabdos.cpp
* [Revision #a1e41e3](https://github.com/MariaDB/server/commit/a1e41e3)\
  2014-07-22 19:31:45 +0300
  * [MDEV-6470](https://jira.mariadb.org/browse/MDEV-6470): Restrict number of error messages about persistent statictic tables not found
* [Revision #fa0628a](https://github.com/MariaDB/server/commit/fa0628a)\
  2014-07-22 19:50:47 +0400
  * [MDEV-6456](https://jira.mariadb.org/browse/MDEV-6456): Add progress indication for "Reading tablespace information from the .ibd files"
* [Revision #2df69f5](https://github.com/MariaDB/server/commit/2df69f5)\
  2014-07-22 11:03:08 -0400
  * \#261 Tokutek/mariadb-5.5#69 run part\_index\_scan test on mariadb
* [Revision #a168015](https://github.com/MariaDB/server/commit/a168015)\
  2014-07-22 10:17:25 -0400
  * FT-304 Fix a maybe-uninitialized warning found by gcc 4.9
* [Revision #decc23c](https://github.com/MariaDB/server/commit/decc23c)\
  2014-07-22 15:51:21 +0200\
  \*
  * Fix bugs in handling of remote index when updating and deleting modified: storage/connect/ha\_connect.cc storage/connect/tabdos.cpp storage/connect/tabfmt.cpp storage/connect/tabmysql.cpp
* [Revision #465cca9](https://github.com/MariaDB/server/commit/465cca9)\
  2014-07-22 09:36:36 -0400
  * FT-304 Fix a memory leak by further separating initialization paths in the block table
* [Revision #d4a3c6f](https://github.com/MariaDB/server/commit/d4a3c6f)\
  2014-07-22 08:57:48 -0400
  * FT-300 Add best-fit strategy for replay testing
* [Revision #6d2968d](https://github.com/MariaDB/server/commit/6d2968d)\
  2014-07-22 08:57:48 -0400
  * FT-300 Fix a bunch of issues with the replay tool, including: - Failure to handle multiple allocators at once (oops) - Failure to handle a clean shutdown where allocators are destroyed by the trace gracefully and so we can't get stats for them after the run (need to clean this up eventually) - Added line numbers to error messages so debugging is easier
* [Revision #1f9a77d](https://github.com/MariaDB/server/commit/1f9a77d)\
  2014-07-22 08:57:48 -0400
  * FT-300 Use an environment variable to determine which file the block allocator trace gets written to
* [Revision #a0252cb](https://github.com/MariaDB/server/commit/a0252cb)\
  2014-07-22 08:57:22 -0400
  * FT-304 Fix an oops in the blocktable, first exposed in a MySQl test and now by src/tests/stress\_test7.cc
* [Revision #7c03c64](https://github.com/MariaDB/server/commit/7c03c64)\
  2014-07-22 08:57:17 -0400
  * FT-304 Add stress test coverage for db->get\_fragmentation(db)
* [Revision #15a529e](https://github.com/MariaDB/server/commit/15a529e)\
  2014-07-22 15:28:15 +0500
  * gis-precise.test fixed to work on Power8.
* [Revision #2b61466](https://github.com/MariaDB/server/commit/2b61466)\
  2014-07-22 14:54:38 +0400
  * [MDEV-6469](https://jira.mariadb.org/browse/MDEV-6469) - rpl.rpl\_gtid\_basic, rpl.rpl\_gtid\_stop\_start, rpl.rpl\_gtid\_crash fail on PPC64
* [Revision #ef67c3a](https://github.com/MariaDB/server/commit/ef67c3a)\
  2014-07-22 13:17:16 +0300
  * [MDEV-6443](https://jira.mariadb.org/browse/MDEV-6443): Server crashed with assertaion failure in file ha\_innodb.cc line 8473
* [Revision #fe3859c](https://github.com/MariaDB/server/commit/fe3859c)\
  2014-07-22 13:08:32 +0300
  * [MDEV-6443](https://jira.mariadb.org/browse/MDEV-6443): Server crashed with assertaion failure in file ha\_innodb.cc line 8473
* [Revision #4ad2abc](https://github.com/MariaDB/server/commit/4ad2abc)\
  2014-07-22 10:49:28 +0500
  * [MDEV-5756](https://jira.mariadb.org/browse/MDEV-5756) CMake option to build without thread pool. Check if the threadpool is available on the system and set HAVE\_POOL\_OF\_THREADS respectively.
* [Revision #0bb0230](https://github.com/MariaDB/server/commit/0bb0230)\
  2014-07-22 10:10:56 +0300
  * [MDEV-6426](https://jira.mariadb.org/browse/MDEV-6426): Maria DB crashes randomly on creating indexes
* [Revision #dbc79ce](https://github.com/MariaDB/server/commit/dbc79ce)\
  2014-07-21 22:21:30 +0300
  * [MDEV-6354](https://jira.mariadb.org/browse/MDEV-6354): Implement a way to read MySQL 5.7.4-labs-tplc page compression format (Fusion-IO).
* [Revision #dd1d921](https://github.com/MariaDB/server/commit/dd1d921)\
  2014-07-21 13:07:48 +0500
  * gis-precise test fixed to pass on Power8.
* [Revision #7e02ba5](https://github.com/MariaDB/server/commit/7e02ba5)\
  2014-07-21 13:16:08 +0400
  * [MDEV-6465](https://jira.mariadb.org/browse/MDEV-6465) - rpl.rpl\_gtid\_master\_promote fails on PPC64
* [Revision #26e4b69](https://github.com/MariaDB/server/commit/26e4b69)\
  2014-07-20 20:39:17 +0200\
  \*
  * FIX errors and some gcc warnings modified: storage/connect/array.cpp storage/connect/array.h storage/connect/blkfil.cpp storage/connect/blkfil.h storage/connect/filter.cpp storage/connect/filter.h storage/connect/ha\_connect.cc storage/connect/tabdos.cpp
* [Revision #e3ac16d](https://github.com/MariaDB/server/commit/e3ac16d)\
  2014-07-20 20:55:44 +0300
  * Add executable bit to scripts that are supposed to have it. More info at: [MDEV-6153?focusedCommentId=55397\&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-55397](https://jira.mariadb.org/browse/MDEV-6153?focusedCommentId=55397\&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-55397)
* [Revision #4b2092e](https://github.com/MariaDB/server/commit/4b2092e)\
  2014-07-20 12:31:42 +0200
  * This is a new version of the CONNECT storage engine. It was developed in a sub-branch of this one and merged by pushing all the changes from it. This version adds the following to CONNECT:
* [Revision #f0f2072](https://github.com/MariaDB/server/commit/f0f2072)\
  2014-07-19 17:46:08 +0300
  * Fixed problem with very slow shutdown when using 100,000 MyISAM tables with delay\_key\_write
* [Revision #ff205b2](https://github.com/MariaDB/server/commit/ff205b2)\
  2014-07-19 13:38:40 +0300
  * Fixed assert in perfschema/pfs.cc::start\_idle\_wait\_v1 when using performance schema and big packets in debug version.
* [Revision #e9b2f5b](https://github.com/MariaDB/server/commit/e9b2f5b)\
  2014-07-19 11:24:21 +0530
  * [WL#7219](https://askmonty.org/worklog/?tid=7219): Reverting the [WL#7219](https://askmonty.org/worklog/?tid=7219) patch in mysql-5.5.39-release branch
* [Revision #54f9828](https://github.com/MariaDB/server/commit/54f9828)\
  2014-07-18 14:50:29 -0400
  * FT-304 Remove inconsistent 'struct' keyword which made the osx build sad.
* [Revision #4057358](https://github.com/MariaDB/server/commit/4057358)\
  2014-07-18 14:06:44 -0400
  * FT-304 Move the blocktable into its own class, fix tests.
* [Revision #54538b4](https://github.com/MariaDB/server/commit/54538b4)\
  2014-07-18 19:45:21 +0400
  * [MDEV-6459](https://jira.mariadb.org/browse/MDEV-6459) - max\_relay\_log\_size and sql\_slave\_skip\_counter misbehave on PPC64
*
  * \[
  * R
  * e
  * v
  * i
  * s
  * i
  * o
  * n
  *
  *
  * d
  * 9
  * 4
  * c
  * 2
  * e
  * 2
  * ]
  * (
  * h
  * t
  * t
  * p
  * s
  * :
  * /
  * /
  * g
  * i
  * t
  * h
  * u
  * b
  * .
  * c
  * o
  * m
  * /
  * M
  * a
  * r
  * i
  * a
  * D
  * B
  * /
  * s
  * e
  * r
  * v
  * e
  * r
  * /
  * c
  * o
  * m
  * m
  * i
  * t
  * /
  * d
  * 9
  * 4
  * c
  * 2
  * e
  * 2
  * )
  *
  * 2
  * 0
  * 1
  * 4
  *
    *
  * 0
  * 7
  *
    *
  * 1
  * 8
  *
  * 2
  * 0
  * :
  * 5
  * 5
  * :
  * 5
  * 2
  *
  *
    *
  * 0
  * 5
  * 3
  * 0
  *
* [Revision #c0ebb3f](https://github.com/MariaDB/server/commit/c0ebb3f)\
  2014-07-18 15:16:25 +0400
  * [MDEV-6450](https://jira.mariadb.org/browse/MDEV-6450) - MariaDB crash on Power8 when built with advance tool chain
* [Revision #7960878](https://github.com/MariaDB/server/commit/7960878)\
  2014-07-18 06:40:52 -0400
  * \#261 auto detect index scans to fix perf problem with partitions
* [Revision #4c8f691](https://github.com/MariaDB/server/commit/4c8f691)\
  2014-07-18 06:40:34 -0400
  * update to 7.1.7
* [Revision #444af9c](https://github.com/MariaDB/server/commit/444af9c)\
  2014-07-18 06:40:10 -0400
  * \#261 debug prelocking for index scans
* [Revision #0304874](https://github.com/MariaDB/server/commit/0304874)\
  2014-07-18 06:39:07 -0400
  * \#261 auto detect index scans to fix perf problem with partitions
* [Revision #c168595](https://github.com/MariaDB/server/commit/c168595)\
  2014-07-17 14:50:13 -0400
  * update to 7.1.7
* [Revision #6c8fbe6](https://github.com/MariaDB/server/commit/6c8fbe6)\
  2014-07-17 19:28:28 +0200
  * Commit merged files.
* [Revision #1904284](https://github.com/MariaDB/server/commit/1904284)\
  2014-07-17 18:13:51 +0200
  * This commit brings many changes, in particular two important ones: 1) Support of partitioning by connect. A table can be partitioned by files, this is an enhanced MULTIPLE table. It can be also partitioned by sub-tables like TBL and this enables table sharding. 2) Handling a CONNECT bug that causes in some cases extraneous rows to remain in the table after an UPDATE or DELETE when the command uses indexing (for not fixed file tables). Until a real fix is done, CONNECT tries to ignore indexing and if it cannot do it abort the command with an error message.
* [Revision #e892e71](https://github.com/MariaDB/server/commit/e892e71)\
  2014-07-17 19:21:56 +0530
  * [WL#7219](https://askmonty.org/worklog/?tid=7219): Pushing it to release 5.5.39-release branch
* [Revision #e543cf1](https://github.com/MariaDB/server/commit/e543cf1)\
  2014-07-16 10:13:37 -0400
  * \#263 enable bulk fetch for insert select sql commands
* [Revision #871dbcf](https://github.com/MariaDB/server/commit/871dbcf)\
  2014-07-16 10:13:16 -0400
  * \#262 enable bulk fetch for create select sql commands
* [Revision #862d17b](https://github.com/MariaDB/server/commit/862d17b)\
  2014-07-16 10:03:00 -0400
  * \#261 debug prelocking for index scans
* [Revision #36a5ead](https://github.com/MariaDB/server/commit/36a5ead)\
  2014-07-16 07:39:11 -0400
  * temporary fix for gcov build
* [Revision #53231b1](https://github.com/MariaDB/server/commit/53231b1)\
  2014-07-15 15:45:48 -0400
  * \#263 enable bulk fetch for insert select sql commands
* [Revision #7941179](https://github.com/MariaDB/server/commit/7941179)\
  2014-07-15 13:13:30 -0400
  * \#262 enable bulk fetch for create select sql commands
* [Revision #c599cc6](https://github.com/MariaDB/server/commit/c599cc6)\
  2014-07-15 10:57:53 +0300
  * [MDEV-6444](https://jira.mariadb.org/browse/MDEV-6444): sys\_vars.innodb\_simulate\_comp\_failures\_basic missing result file
* [Revision #501c56e](https://github.com/MariaDB/server/commit/501c56e)\
  2014-07-11 12:06:47 +0200
  * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262), [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914), [MDEV-5941](https://jira.mariadb.org/browse/MDEV-5941), [MDEV-6020](https://jira.mariadb.org/browse/MDEV-6020): Deadlocks during parallel replication causing replication to fail.
* [Revision #fd0abec](https://github.com/MariaDB/server/commit/fd0abec)\
  2014-07-11 11:17:50 +0200
  * Fix test failure seen in buildbot on power8.
* [Revision #e81ecc9](https://github.com/MariaDB/server/commit/e81ecc9)\
  2014-07-11 10:54:43 +0200
  * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262), [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914), [MDEV-5941](https://jira.mariadb.org/browse/MDEV-5941), [MDEV-6020](https://jira.mariadb.org/browse/MDEV-6020): Deadlocks during parallel replication causing replication to fail.
* [Revision #989b04f](https://github.com/MariaDB/server/commit/989b04f)\
  2014-07-10 17:12:34 -0400
  * FT-308 support deferred XA recovery with txn discard and dirty environment shutdown
* [Revision #c5e9952](https://github.com/MariaDB/server/commit/c5e9952)\
  2014-07-10 16:30:40 -0400
  * \#258 support deferred XA recovery with discard of prepared txns and dirty shutdown of the FT environment
* [Revision #5b75891](https://github.com/MariaDB/server/commit/5b75891)\
  2014-07-10 14:24:53 +0200
  * Fix compile failure in non-debug build.
* [Revision #8f21a31](https://github.com/MariaDB/server/commit/8f21a31)\
  2014-07-10 13:55:53 +0200
  * [MDEV-6435](https://jira.mariadb.org/browse/MDEV-6435): Assertion \`m\_status == DA\_ERROR' failed in Diagnostics\_area::sql\_errno() with parallel replication
* [Revision #afbb2e2](https://github.com/MariaDB/server/commit/afbb2e2)\
  2014-07-10 12:44:20 +0400
  * Coding style fixes: remove trailing spaces.
* [Revision #01d47a4](https://github.com/MariaDB/server/commit/01d47a4)\
  2014-07-10 10:00:21 +0400
  * Coding style fixes: remove trailing spaces.
* [Revision #48a6883](https://github.com/MariaDB/server/commit/48a6883)\
  2014-07-09 15:50:15 -0400
  * \#258 support deferred XA recovery with discard of prepared txns and dirty shutdown of the FT environment
* [Revision #2bb482b](https://github.com/MariaDB/server/commit/2bb482b)\
  2014-07-09 15:39:57 -0400
  * FT-308 support deferred XA recovery with txn discard and dirty environment shutdown
* [Revision #45f6262](https://github.com/MariaDB/server/commit/45f6262)\
  2014-07-09 13:02:52 +0200
  * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262), [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914), [MDEV-5941](https://jira.mariadb.org/browse/MDEV-5941), [MDEV-6020](https://jira.mariadb.org/browse/MDEV-6020): Deadlocks during parallel replication causing replication to fail.
* [Revision #8aff914](https://github.com/MariaDB/server/commit/8aff914)\
  2014-07-08 16:08:40 -0400
  * FT-300 Fix OSX build
* [Revision #2548a42](https://github.com/MariaDB/server/commit/2548a42)\
  2014-07-08 15:37:35 -0400
  * FT-307 Add a 'memcmp magic' API, where users can specify that a particular value for the first byte of a key means it may be compared with memcmp and a length check.
* [Revision #17c5b4d](https://github.com/MariaDB/server/commit/17c5b4d)\
  2014-07-08 15:15:10 -0400
  * FT-300 Block allocator trace replay tool
* [Revision #e9de022](https://github.com/MariaDB/server/commit/e9de022)\
  2014-07-08 13:32:51 -0400
  * FT-306 Fix logger long wait status text
* [Revision #ba4e56d](https://github.com/MariaDB/server/commit/ba4e56d)\
  2014-07-08 15:59:03 +0200
  * Fix small merge errors after rebase
* [Revision #1cd4af2](https://github.com/MariaDB/server/commit/1cd4af2)\
  2014-07-08 09:08:45 -0400
  * \#259 add TOKUDB\_CACHETABLE\_SIZE\_CLONED variable
* [Revision #92577cc](https://github.com/MariaDB/server/commit/92577cc)\
  2014-07-08 14:54:53 +0200
  * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262), [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914), [MDEV-5941](https://jira.mariadb.org/browse/MDEV-5941), [MDEV-6020](https://jira.mariadb.org/browse/MDEV-6020): Deadlocks during parallel replication causing replication to fail.
* [Revision #3073b5b](https://github.com/MariaDB/server/commit/3073b5b)\
  2014-07-08 13:55:42 +0200
  * Bug#19155121 - Remove perl(GD) and dtrace dependencies and bench fix
* [Revision #98fc5b3](https://github.com/MariaDB/server/commit/98fc5b3)\
  2014-07-08 12:54:47 +0200
  * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262), [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914), [MDEV-5941](https://jira.mariadb.org/browse/MDEV-5941), [MDEV-6020](https://jira.mariadb.org/browse/MDEV-6020): Deadlocks during parallel replication causing replication to fail.
* [Revision #a7163ce](https://github.com/MariaDB/server/commit/a7163ce)\
  2014-07-08 11:13:37 +0200
  * Applying patch for bug 18779944
* [Revision #982fc1c](https://github.com/MariaDB/server/commit/982fc1c)\
  2014-07-07 16:27:58 -0400
  * moved to jira for issues
* [Revision #a6a936b](https://github.com/MariaDB/server/commit/a6a936b)\
  2014-07-07 13:34:13 -0400
  * remove gcc 4.7 artifacts from nightly scripts
* [Revision #77fb45a](https://github.com/MariaDB/server/commit/77fb45a)\
  2014-07-05 14:06:29 -0400
  * FT-300 Add simple, compile-time enabled stderr tracing for each block allocator.
* [Revision #f98b52a](https://github.com/MariaDB/server/commit/f98b52a)\
  2014-07-05 15:20:49 +0400
  * Increased the version number
* [Revision #c536154](https://github.com/MariaDB/server/commit/c536154)\
  2014-07-05 00:49:10 -0400
  * updated branding to tokuft
* [Revision #8025d26](https://github.com/MariaDB/server/commit/8025d26)\
  2014-07-04 10:15:49 +0200
  * remove a couple of old unused #defines
* [Revision #e5149fa](https://github.com/MariaDB/server/commit/e5149fa)\
  2014-07-04 07:44:55 +0200
  * Fix that gap locks are only skipped within one group commit.
* [Revision #dc07bf7](https://github.com/MariaDB/server/commit/dc07bf7)\
  2014-07-03 15:51:23 -0400
  * FT-302 Organize allocation strategy code into its own header / source file.
* [Revision #5883b9a](https://github.com/MariaDB/server/commit/5883b9a)\
  2014-07-03 15:27:26 -0400
  * FT-302 Correctly use the new interface (oops)
* [Revision #0acaea9](https://github.com/MariaDB/server/commit/0acaea9)\
  2014-07-03 15:19:58 -0400
  * FT-302 Add block allocation strategy to the block allocator. Default to the one and only strategy so far - first fit.
* [Revision #46ab993](https://github.com/MariaDB/server/commit/46ab993)\
  2014-07-03 12:57:00 -0400
  * FT-276 Remove alignment from toku\_mempool\_malloc API
* [Revision #84c5d22](https://github.com/MariaDB/server/commit/84c5d22)\
  2014-07-03 12:36:25 -0400
  * FT-291 Remove the remaining cilk artifacts
* [Revision #c81c06b](https://github.com/MariaDB/server/commit/c81c06b)\
  2014-07-03 12:36:25 -0400
  * FT-292 Fix leak in comparator-test
* [Revision #85d55da](https://github.com/MariaDB/server/commit/85d55da)\
  2014-07-03 12:36:25 -0400
  * FT-293 Remove examples/, which hasn't been built or maintained in years
* [Revision #e91c66c](https://github.com/MariaDB/server/commit/e91c66c)\
  2014-07-03 12:36:25 -0400
  * FT-297 Move tools to tools/
* [Revision #157e180](https://github.com/MariaDB/server/commit/157e180)\
  2014-07-03 12:36:13 -0400
  * FT-294 Move cachetable files to ft/cachetable, txn files to ft/txn FT-295 Move ybt.h to utils/dbt.h
* [Revision #c821fd5](https://github.com/MariaDB/server/commit/c821fd5)\
  2014-07-03 12:30:17 -0400
  * FT-294 Move the logging code to its own sudbdirectory, logger/
* [Revision #6e3d772](https://github.com/MariaDB/server/commit/6e3d772)\
  2014-07-03 12:30:17 -0400
  * FT-294 Move serialization code to its own subdirectory, serialize/
* [Revision #40ea904](https://github.com/MariaDB/server/commit/40ea904)\
  2014-07-03 12:30:17 -0400
  * FT-299 Clean up XIDs abstraction
* [Revision #7ad1f1b](https://github.com/MariaDB/server/commit/7ad1f1b)\
  2014-07-03 12:30:17 -0400
  * FT-298 Start breaking up ft-internal.h by moving serialization code to its own header
* [Revision #7ffd1fa](https://github.com/MariaDB/server/commit/7ffd1fa)\
  2014-07-03 12:29:48 -0400
  * FT-242 Break up fttypes.h completely. FT-296 Move bytestring class to utils/
* [Revision #da70298](https://github.com/MariaDB/server/commit/da70298)\
  2014-07-03 11:14:41 -0400
  * FT-288 Fix warn-uninitialized errors found by gcc 4.9
* [Revision #cb182c2](https://github.com/MariaDB/server/commit/cb182c2)\
  2014-07-03 09:09:12 -0400
  * FT-287, fix typo
* [Revision #28833bd](https://github.com/MariaDB/server/commit/28833bd)\
  2014-07-03 08:44:51 -0400
  * \#257 disable missing field initializer warning
* [Revision #4df6616](https://github.com/MariaDB/server/commit/4df6616)\
  2014-07-03 08:44:40 -0400
  * \#256 only force MDL X for certain alter table operations
* [Revision #b83136c](https://github.com/MariaDB/server/commit/b83136c)\
  2014-07-03 08:44:34 -0400
  * \#255 run iibench on PS 5.6
* [Revision #518fa8b](https://github.com/MariaDB/server/commit/518fa8b)\
  2014-07-03 08:42:42 -0400
  * \#264 tokuftdump should dump header with default args
* [Revision #86fbfc3](https://github.com/MariaDB/server/commit/86fbfc3)\
  2014-07-03 06:13:29 -0400
  * \#264 tokuftdump should dump header with default args
* [Revision #3a030fa](https://github.com/MariaDB/server/commit/3a030fa)\
  2014-07-02 13:27:37 -0400
  * \#257 disable missing field initializer warning
* [Revision #3bdf1bb](https://github.com/MariaDB/server/commit/3bdf1bb)\
  2014-07-02 11:18:13 -0400
  * FT-287, have engine status report the amount of cloned data in the cachetable
* [Revision #01046e7](https://github.com/MariaDB/server/commit/01046e7)\
  2014-07-02 16:18:28 +0300
  * RBR triggers enabling in 10.1
* [Revision #4cb1e0e](https://github.com/MariaDB/server/commit/4cb1e0e)\
  2014-07-02 12:51:45 +0200
  * [MDEV-6321](https://jira.mariadb.org/browse/MDEV-6321): close\_temporary\_tables() in format description event not serialised correctly
* [Revision #bd2117d](https://github.com/MariaDB/server/commit/bd2117d)\
  2014-08-19 21:35:14 +0300
  * Automatic merge from 5.5 Fixed 2 failing tests by replacing result files
* [Revision #cfa1ce8](https://github.com/MariaDB/server/commit/cfa1ce8)\
  2014-08-15 11:31:13 +0200
  * [MDEV-6551](https://jira.mariadb.org/browse/MDEV-6551): Some replication errors are ignored if slave\_parallel\_threads > 0
* [Revision #65ac881](https://github.com/MariaDB/server/commit/65ac881)\
  2014-08-14 15:38:08 +0300
  * If one uses 3 --verbose options to mysql\_upgrade or mysqlcheck one will now get on stdout all ALTER, RENAME and CHECK commands that mysqlcheck executes. If one uses 4 --verbose to mysql\_upgrade it will also write out all mysqlcheck commands invoked.
* [Revision #258ecf5](https://github.com/MariaDB/server/commit/258ecf5)\
  2014-08-14 15:36:48 +0300
  * Added Innobase .ic and errmsg-utf8.txt to tagged files Fixed compiler warning
* [Revision #ec05fea](https://github.com/MariaDB/server/commit/ec05fea)\
  2014-08-13 13:34:28 +0200
  * [MDEV-6549](https://jira.mariadb.org/browse/MDEV-6549), failing to update gtid\_slave\_pos for a transaction that was retried.
* [Revision #354f3f1](https://github.com/MariaDB/server/commit/354f3f1)\
  2014-08-13 09:10:56 +0300
  * [MDEV-6546](https://jira.mariadb.org/browse/MDEV-6546): innodb.innodb\_simulate\_comp\_failures\_small fails sporadically
* [Revision #d93bd84](https://github.com/MariaDB/server/commit/d93bd84)\
  2014-08-12 19:16:44 +0400
  * Increased the version number
* [Revision #02d92e3](https://github.com/MariaDB/server/commit/02d92e3)\
  2014-08-12 07:52:19 +0400
  * Recoding feedback\_plugin\_send.result (forgotten in the previous commit).
* [Revision #d362511](https://github.com/MariaDB/server/commit/d362511)\
  2014-07-02 09:38:43 +0200
  * Unconditionally disable dtrace for rpm, barfs on Oracle dtrace
* [Revision #d28b07a](https://github.com/MariaDB/server/commit/d28b07a)\
  2014-07-01 15:19:30 +0200
  * Unconditionally disable dtrace for rpm-oel, barfs on Oracle dtrace
* [Revision #9406108](https://github.com/MariaDB/server/commit/9406108)\
  2014-06-30 19:24:25 +0530
  * Bug #17357528 BACKPORT BUG#16513435 TO 5.5 AND 5.6
* [Revision #cbe72db](https://github.com/MariaDB/server/commit/cbe72db)\
  2014-06-30 12:31:44 +0200
  * BUG#18779944: MYSQLDUMP BUFFER OVERFLOW
* [Revision #4ee6bf2](https://github.com/MariaDB/server/commit/4ee6bf2)\
  2014-06-29 22:44:12 +0200
  * deb hack: don't set CASSANDRA\_DEB\_FILES unless cassandra can be built
* [Revision #b35c591](https://github.com/MariaDB/server/commit/b35c591)\
  2014-06-28 13:53:18 +0300
  * [MDEV-6376](https://jira.mariadb.org/browse/MDEV-6376): InnoDB: Assertion failure in thread 139995225970432 in file buf0mtflu.cc line 570.
*
  * \[
  * R
  * e
  * v
  * i
  * s
  * i
  * o
  * n
  *
  *
  * 8
  * e
  * 4
  * a
  * e
  * 8
  * c
  * ]
  * (
  * h
  * t
  * t
  * p
  * s
  * :
  * /
  * /
  * g
  * i
  * t
  * h
  * u
  * b
  * .
  * c
  * o
  * m
  * /
  * M
  * a
  * r
  * i
  * a
  * D
  * B
  * /
  * s
  * e
  * r
  * v
  * e
  * r
  * /
  * c
  * o
  * m
  * m
  * i
  * t
  * /
  * 8
  * e
  * 4
  * a
  * e
  * 8
  * c
  * )
  *
  * 2
  * 0
  * 1
  * 4
  *
    *
  * 0
  * 6
  *
    *
  * 2
  * 7
  *
  * 1
  * 9
  * :
  * 3
  * 0
  * :
  * 1
  * 9
  *
  *
    *
  * 0
  * 5
  * 3
  * 0
  *
* [Revision #f384ba7](https://github.com/MariaDB/server/commit/f384ba7)\
  2014-06-27 17:17:04 +0530
  * Bug#18903155: BACKPORT BUG-18008907 TO 5.5+ VERSIONS.
* [Revision #36e86ba](https://github.com/MariaDB/server/commit/36e86ba)\
  2014-06-27 15:39:44 +0400
  * Remove out-of-date comments
* [Revision #14aa44b](https://github.com/MariaDB/server/commit/14aa44b)\
  2014-06-27 17:04:08 +0530
  * Bug#18903155: BACKPORT BUG-18008907 TO 5.5+ VERSIONS.
* [Revision #854da5e](https://github.com/MariaDB/server/commit/854da5e)\
  2014-06-27 12:41:49 +0200
  * Bug#16395459 TEST AND RESULT FILES WITH EXECUTE BIT
* [Revision #220c933](https://github.com/MariaDB/server/commit/220c933)\
  2014-06-27 11:27:27 +0200
  * BUG#18779944: MYSQLDUMP BUFFER OVERFLOW
* [Revision #ca032f3](https://github.com/MariaDB/server/commit/ca032f3)\
  2014-06-26 15:24:47 -0400
  * \#256 only force MDL X for certain alter table operations

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
