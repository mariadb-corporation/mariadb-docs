# MariaDB 10.2.13 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.13)[Release Notes](../../old-releases/10.2/10.2.13.md)[Changelog](mariadb-10213-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 13 Feb 2018

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.13.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #00f0c039d2](https://github.com/MariaDB/server/commit/00f0c039d2)\
  2018-02-12 16:40:05 +0200
  * [MDEV-15270](https://jira.mariadb.org/browse/MDEV-15270) mariadb-backup should not try to use doublewrite buffer
* [Revision #33f70c4d9c](https://github.com/MariaDB/server/commit/33f70c4d9c)\
  2018-02-12 13:35:07 +0200
  * [MDEV-13869](https://jira.mariadb.org/browse/MDEV-13869) MariaDB slow start
* [Revision #7a106d1961](https://github.com/MariaDB/server/commit/7a106d1961)\
  2018-02-12 03:20:09 +0200
  * Updated list of unstable tests for 10.2.13
* Merge [Revision #49bcc82686](https://github.com/MariaDB/server/commit/49bcc82686) 2018-02-11 00:23:17 +0100 - Merge branch '10.1' into 10.2
* [Revision #b88542681b](https://github.com/MariaDB/server/commit/b88542681b)\
  2018-02-10 22:17:49 +0400
  * [MDEV-14611](https://jira.mariadb.org/browse/MDEV-14611) ALTER TABLE EXCHANGE PARTITION does not work properly when used with DATA DIRECTORY.
* [Revision #a2feeb3d6f](https://github.com/MariaDB/server/commit/a2feeb3d6f)\
  2018-02-10 21:51:24 +0400
  * After-merge fixes for "sys\_vars.sysvars\_innodb '32bit,xtradb'" test results.
* Merge [Revision #e07451f71f](https://github.com/MariaDB/server/commit/e07451f71f) 2018-02-09 19:49:19 +0400 - Merge remote-tracking branch 'origin/10.0' into 10.1
* [Revision #b0a92333c0](https://github.com/MariaDB/server/commit/b0a92333c0)\
  2018-02-09 19:47:00 +0400
  * [MDEV-15262](https://jira.mariadb.org/browse/MDEV-15262) Wrong results for SELECT..WHERE non\_indexed\_datetime\_column=indexed\_time\_column
* [Revision #6f0b316fbe](https://github.com/MariaDB/server/commit/6f0b316fbe)\
  2018-02-08 21:12:11 +0200
  * Update wrong xtradb version
* [Revision #564891c532](https://github.com/MariaDB/server/commit/564891c532)\
  2018-02-09 17:17:32 +0200
  * [MDEV-14508](https://jira.mariadb.org/browse/MDEV-14508): encryption.innodb-compressed-blob failed in buildbot, assertion in btr0cur.cc line 1398
* [Revision #b75d8453d4](https://github.com/MariaDB/server/commit/b75d8453d4)\
  2018-02-07 19:08:53 +0100
  * [MDEV-14868](https://jira.mariadb.org/browse/MDEV-14868) MariaDB server crashes after using ROLLBACK TO when encrypt\_tmp\_files=ON
* [Revision #60dfe12be3](https://github.com/MariaDB/server/commit/60dfe12be3)\
  2018-02-07 18:54:11 +0100
  * [MDEV-14868](https://jira.mariadb.org/browse/MDEV-14868) MariaDB server crashes after using ROLLBACK TO when encrypt\_tmp\_files=ON
* [Revision #47d1679ac6](https://github.com/MariaDB/server/commit/47d1679ac6)\
  2018-02-06 20:26:59 +0100
  * fix encryption.tempfiles to check that encrypt\_tmp\_files is ON
* [Revision #06d77eb43a](https://github.com/MariaDB/server/commit/06d77eb43a)\
  2018-02-08 14:55:01 +0200
  * [MDEV-14427](https://jira.mariadb.org/browse/MDEV-14427): encryption.innodb-bad-key-change failed in buildbot
* [Revision #7ed0156384](https://github.com/MariaDB/server/commit/7ed0156384)\
  2018-02-10 14:27:29 +0200
  * Removed compiler warnings
* [Revision #76dc6af24c](https://github.com/MariaDB/server/commit/76dc6af24c)\
  2018-02-10 14:27:06 +0200
  * TokuDB didn't compile with valgrind
* [Revision #12d5307e95](https://github.com/MariaDB/server/commit/12d5307e95)\
  2018-02-10 14:24:15 +0200
  * [MDEV-13508](https://jira.mariadb.org/browse/MDEV-13508) ALTER TABLE that renames columns and CHECK constraints
* Merge [Revision #7beaa5e34e](https://github.com/MariaDB/server/commit/7beaa5e34e) 2018-02-09 13:44:38 +0300 - Merge branch 'bb-10.2-mariarocks' into 10.2
* Merge [Revision #cca9b3a933](https://github.com/MariaDB/server/commit/cca9b3a933) 2018-02-08 13:57:46 +0200 - Merge pull request #595 from MariaDB/add\_myrocks\_gotbackup
* [Revision #adbf6caad6](https://github.com/MariaDB/server/commit/adbf6caad6)\
  2018-02-07 11:36:13 +0000
  * debian/control Include myrocks\_hotbackup into mariadb-plugin-rocksdb
* [Revision #cbe566dc42](https://github.com/MariaDB/server/commit/cbe566dc42)\
  2018-02-07 12:32:58 +0000
  * Add myrocks\_hotbackup part of rocksdb plugin in cmake
* [Revision #699123fdc3](https://github.com/MariaDB/server/commit/699123fdc3)\
  2018-02-07 11:13:29 +0000
  * Fix rocksdb compiler version identification with GCC
* [Revision #9a23b22346](https://github.com/MariaDB/server/commit/9a23b22346)\
  2018-01-25 14:43:18 +0300
  * Adjust myrocks\_hotbackup to work with MariaDB.
* [Revision #e402d779c7](https://github.com/MariaDB/server/commit/e402d779c7)\
  2018-01-25 14:08:11 +0300
  * Import myrocks\_hotbackup from the upstream
* [Revision #7c1bd8fa04](https://github.com/MariaDB/server/commit/7c1bd8fa04)\
  2018-02-09 08:28:42 +0200
  * Add back (and clean up) the test innodb\_zip.prefix\_index\_liftedlimit
* [Revision #e4da20d438](https://github.com/MariaDB/server/commit/e4da20d438)\
  2018-02-09 08:26:47 +0200
  * [MDEV-14238](https://jira.mariadb.org/browse/MDEV-14238) Bogus assertion on row\_get\_rec\_trx\_id()
* [Revision #8411a8ff60](https://github.com/MariaDB/server/commit/8411a8ff60)\
  2018-02-08 09:48:03 -0800
  * Corrected the patch for [MDEV-15119](https://jira.mariadb.org/browse/MDEV-15119) that caused a failure for cte\_nonrecursive.test with --embedded.
* [Revision #f01ce62c8f](https://github.com/MariaDB/server/commit/f01ce62c8f)\
  2018-02-08 13:46:43 +0000
  * add [MDEV-504](https://jira.mariadb.org/browse/MDEV-504) to unstable tests, to fix appveyor
* [Revision #76600199cb](https://github.com/MariaDB/server/commit/76600199cb)\
  2018-02-08 13:03:14 +0000
  * rocksdb : Disable the constantly failing bloomfilter test, until [MDEV-14562](https://jira.mariadb.org/browse/MDEV-14562) is fixed
* [Revision #db25305780](https://github.com/MariaDB/server/commit/db25305780)\
  2018-02-07 16:44:46 +0200
  * [MDEV-14407](https://jira.mariadb.org/browse/MDEV-14407) Assertion failure during rollback
* Merge [Revision #be6307c0fa](https://github.com/MariaDB/server/commit/be6307c0fa) 2018-02-08 13:50:58 +0200 - Merge 10.1 into 10.2
* Merge [Revision #871f2a6ee2](https://github.com/MariaDB/server/commit/871f2a6ee2) 2018-02-08 13:29:08 +0200 - Merge 10.0 into 10.1
* [Revision #9216a4f69f](https://github.com/MariaDB/server/commit/9216a4f69f)\
  2018-02-08 13:26:44 +0200
  * Make the test innodb.recovery\_shutdown more robust
* [Revision #5421e3aee7](https://github.com/MariaDB/server/commit/5421e3aee7)\
  2018-02-08 12:51:19 +0200
  * [MDEV-15249](https://jira.mariadb.org/browse/MDEV-15249) Crash in MVCC read after IMPORT TABLESPACE
* [Revision #b6455479e5](https://github.com/MariaDB/server/commit/b6455479e5)\
  2018-02-07 18:14:45 +0100
  * [MDEV-15230](https://jira.mariadb.org/browse/MDEV-15230): column\_json breaks cyrillic in 10.1.31
* [Revision #b253a0c3a9](https://github.com/MariaDB/server/commit/b253a0c3a9)\
  2018-02-06 12:44:43 -0500
  * bump the VERSION
* [Revision #5c057b3fef](https://github.com/MariaDB/server/commit/5c057b3fef)\
  2018-02-07 17:25:46 +0200
  * Disabled galera\_ist\_progress at it always fails in 10.2
* Merge [Revision #5a7b6db671](https://github.com/MariaDB/server/commit/5a7b6db671) 2018-02-07 15:19:53 +0200 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #fc2d794809](https://github.com/MariaDB/server/commit/fc2d794809)\
  2018-01-03 12:57:41 +0100\
  \*
  * Fix [MDEV-9844](https://jira.mariadb.org/browse/MDEV-9844), [MDEV-10179](https://jira.mariadb.org/browse/MDEV-10179), [MDEV-14214](https://jira.mariadb.org/browse/MDEV-14214) This is done by removing the tbl table type THREAD option that causes a multiple of sporadic bugs. This may be temporary depending on whether a real fix is found. modified: storage/connect/mysql-test/connect/disabled.def modified: storage/connect/tabtbl.cpp modified: storage/connect/tabtbl.h
* [Revision #1c2a2d3c9d](https://github.com/MariaDB/server/commit/1c2a2d3c9d)\
  2018-02-07 15:19:45 +0200
  * Update Connector/C
* [Revision #d743b61f89](https://github.com/MariaDB/server/commit/d743b61f89)\
  2018-01-18 18:48:50 +1100
  * [MDEV-14567](https://jira.mariadb.org/browse/MDEV-14567): CRYPTO\_set\_mem\_functions fails in FIPS mode
* [Revision #10590dd39c](https://github.com/MariaDB/server/commit/10590dd39c)\
  2018-02-06 13:53:20 +0200
  * [MDEV-15199](https://jira.mariadb.org/browse/MDEV-15199) Referential integrity broken in ON DELETE CASCADE
* [Revision #5d7e9fd46c](https://github.com/MariaDB/server/commit/5d7e9fd46c)\
  2018-02-06 14:57:04 +0200
  * InnoDB UPDATE cleanup
* [Revision #b68dac88b3](https://github.com/MariaDB/server/commit/b68dac88b3)\
  2018-02-06 13:39:40 +0200
  * [MDEV-15219](https://jira.mariadb.org/browse/MDEV-15219) FOREIGN KEY CASCADE or SET NULL operations will not resume after lock wait
* [Revision #1789e0ff03](https://github.com/MariaDB/server/commit/1789e0ff03)\
  2018-02-06 10:34:16 +0200
  * Remove useless debug instrumentation row\_print\_geometry\_data
* [Revision #5815c8ee85](https://github.com/MariaDB/server/commit/5815c8ee85)\
  2018-02-06 10:33:42 +0200
  * Remove useless code
* [Revision #4cec63af44](https://github.com/MariaDB/server/commit/4cec63af44)\
  2018-02-06 06:09:47 +0200
  * Foreign key code cleanup
* [Revision #2ef41622e2](https://github.com/MariaDB/server/commit/2ef41622e2)\
  2018-02-06 12:12:19 -0800
  * Fixed [MDEV-15162](https://jira.mariadb.org/browse/MDEV-15162) Query with CTE hangs if assignment operator (:=) is used
* [Revision #bdb87c4965](https://github.com/MariaDB/server/commit/bdb87c4965)\
  2018-02-06 08:32:49 -0800
  * Fixed [MDEV-15119](https://jira.mariadb.org/browse/MDEV-15119) CTE, referencing another CTE, that is declared after, does not return error
* [Revision #90885985b6](https://github.com/MariaDB/server/commit/90885985b6)\
  2018-02-06 08:26:50 -0800
  * Fixed [MDEV-15120](https://jira.mariadb.org/browse/MDEV-15120) CTE table should not belong to database, that is in use
* [Revision #b4fbb4183b](https://github.com/MariaDB/server/commit/b4fbb4183b)\
  2018-02-06 11:49:26 +0100
  * remove bash-ish from SST scripts
* [Revision #00855a62ab](https://github.com/MariaDB/server/commit/00855a62ab)\
  2018-02-06 00:30:00 +0100
  * cleanup: my\_off\_t mmaped\_length -> size\_t
* [Revision #d429f60770](https://github.com/MariaDB/server/commit/d429f60770)\
  2018-02-06 00:20:46 +0100
  * compilation error on windows
* [Revision #775a8a0e4b](https://github.com/MariaDB/server/commit/775a8a0e4b)\
  2018-02-05 20:09:24 +0100
  * compilation error on windows
* [Revision #c98c616e7f](https://github.com/MariaDB/server/commit/c98c616e7f)\
  2018-02-05 16:00:56 +0100
  * no separate 10.2 fix for [MDEV-14743](https://jira.mariadb.org/browse/MDEV-14743) at this point in time
* [Revision #2eb00d1eba](https://github.com/MariaDB/server/commit/2eb00d1eba)\
  2018-02-05 16:00:39 +0100
  * fix Item\_window\_func::print() not to crash before fix\_fields()
* [Revision #c4930a820a](https://github.com/MariaDB/server/commit/c4930a820a)\
  2018-02-05 16:00:13 +0100
  * don't set derived->merged until derived is really irreversibly merged
* Merge [Revision #4771ae4b22](https://github.com/MariaDB/server/commit/4771ae4b22) 2018-02-06 14:50:50 +0100 - Merge branch 'github/10.1' into 10.2
* [Revision #0c25e58db6](https://github.com/MariaDB/server/commit/0c25e58db6)\
  2018-02-06 02:38:01 +0100
  * correctly detect unsupported compiler flags
* [Revision #4418abb267](https://github.com/MariaDB/server/commit/4418abb267)\
  2018-02-06 02:33:56 +0100
  * cleanup: simplify maintainer.cmake
* [Revision #7407313f11](https://github.com/MariaDB/server/commit/7407313f11)\
  2018-02-05 16:03:28 +0100
  * silence the annoying compiler warning
* Merge [Revision #3f42529a6f](https://github.com/MariaDB/server/commit/3f42529a6f) 2018-02-05 09:25:33 +0200 - Merge 10.0 into 10.1
* [Revision #cb5374801e](https://github.com/MariaDB/server/commit/cb5374801e)\
  2018-02-05 09:23:36 +0200
  * [MDEV-15202](https://jira.mariadb.org/browse/MDEV-15202) innodb.log\_file\_size failed in buildbot
* [Revision #60f51af755](https://github.com/MariaDB/server/commit/60f51af755)\
  2018-02-05 18:21:28 +0200
  * [MDEV-15042](https://jira.mariadb.org/browse/MDEV-15042): INSERT ON DUPLICATE KEY UPDATE produces error 1032 (Can't find record)
* Merge [Revision #9390ff53fc](https://github.com/MariaDB/server/commit/9390ff53fc) 2018-02-02 16:19:52 +0200 - [MDEV-14958](https://jira.mariadb.org/browse/MDEV-14958) Merge new release of InnoDB MySQL 5.7.21 to 10.2
* [Revision #d13fbc6212](https://github.com/MariaDB/server/commit/d13fbc6212)\
  2018-02-02 15:27:03 +0200
  * Remove code related to InnoDB native partitioning in MySQL 5.7
* Merge [Revision #d57b2430d7](https://github.com/MariaDB/server/commit/d57b2430d7) 2018-02-02 16:15:50 +0200 - Merge a fix from MySQL 5.7, to presumably dead code
* [Revision #6266493fc3](https://github.com/MariaDB/server/commit/6266493fc3)\
  2017-09-20 01:38:26 +0200
  * Bug #25729649 LOCK0LOCK.CC:NNN:ADD\_POSITION != NULL
* [Revision #4c731a2d7c](https://github.com/MariaDB/server/commit/4c731a2d7c)\
  2018-02-02 15:04:52 +0200
  * Adapt a MySQL 5.7 fix for SET GLOBAL innodb\_buffer\_pool\_size
* [Revision #009e872b1c](https://github.com/MariaDB/server/commit/009e872b1c)\
  2018-02-02 14:28:46 +0200
  * Merge a test case from MySQL 5.7 (no code fix needed)
* [Revision #d4ea179e13](https://github.com/MariaDB/server/commit/d4ea179e13)\
  2018-02-02 09:10:15 +0200
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Merge InnoDB test cases from MySQL 5.7 (part 7)
* [Revision #859fe1f24d](https://github.com/MariaDB/server/commit/859fe1f24d)\
  2018-02-01 20:03:18 +0200
  * Ensure that thd->user\_var\_events\_alloc is always relevant
* [Revision #44314c768f](https://github.com/MariaDB/server/commit/44314c768f)\
  2018-02-01 18:36:03 +0200
  * [MDEV-15165](https://jira.mariadb.org/browse/MDEV-15165) InnoDB purge for index on virtual column is trying to access an incomplete record
* [Revision #29240b50e3](https://github.com/MariaDB/server/commit/29240b50e3)\
  2018-02-01 17:39:10 +0200
  * Correct a comment about incomplete records
* [Revision #78716fffce](https://github.com/MariaDB/server/commit/78716fffce)\
  2018-02-01 17:08:30 +0200
  * Silence a bogus warning about uninitialized m\_size
* [Revision #97a39ba212](https://github.com/MariaDB/server/commit/97a39ba212)\
  2018-02-01 14:08:06 +0200
  * Follow-up to reverting [MDEV-6938](https://jira.mariadb.org/browse/MDEV-6938)
* [Revision #f4f46ec13a](https://github.com/MariaDB/server/commit/f4f46ec13a)\
  2018-02-01 12:37:20 +0000
  * Attempt to fix appveyor
* [Revision #27733c8b12](https://github.com/MariaDB/server/commit/27733c8b12)\
  2018-02-01 12:23:34 +0000
  * auth\_gssapi - fix test result and let the test run on Windows buildbot
* [Revision #13479cef08](https://github.com/MariaDB/server/commit/13479cef08)\
  2018-02-01 12:00:28 +0000
  * Tests : Fix result file
* [Revision #5a9c63ab55](https://github.com/MariaDB/server/commit/5a9c63ab55)\
  2018-02-01 13:35:03 +0200
  * [MDEV-10949](https://jira.mariadb.org/browse/MDEV-10949): innodb\_disallow\_writes does not work as expected
* [Revision #867d8680b2](https://github.com/MariaDB/server/commit/867d8680b2)\
  2018-02-01 09:26:03 +0000
  * Fix sql\_print\_warning formatting
* [Revision #313247db9c](https://github.com/MariaDB/server/commit/313247db9c)\
  2018-02-01 09:01:15 +0000
  * [MDEV-15089](https://jira.mariadb.org/browse/MDEV-15089) Ensure that connection ID is in 32bit range
* [Revision #b56f9fbe2f](https://github.com/MariaDB/server/commit/b56f9fbe2f)\
  2018-01-30 16:30:39 +1100
  * threadpool: release mutex on io\_poll\_create failure
* [Revision #67d89e4d7d](https://github.com/MariaDB/server/commit/67d89e4d7d)\
  2018-01-31 12:01:35 +0200
  * [MDEV-15143](https://jira.mariadb.org/browse/MDEV-15143) InnoDB: Rollback of trx with id 0 completed
* [Revision #f5f56a076b](https://github.com/MariaDB/server/commit/f5f56a076b)\
  2018-01-31 10:08:35 +0100
  * [MDEV-15133](https://jira.mariadb.org/browse/MDEV-15133): array bound (bulk) parameters of NULL propagate on next rows
* [Revision #c744dde711](https://github.com/MariaDB/server/commit/c744dde711)\
  2018-01-30 21:25:36 +0000
  * Roles : Initialize variables that are passed to update\_role\_db()
* [Revision #0ba6aaf030](https://github.com/MariaDB/server/commit/0ba6aaf030)\
  2018-01-26 21:45:25 +0200
  * [MDEV-11415](https://jira.mariadb.org/browse/MDEV-11415) Remove excessive undo logging during ALTER TABLE…ALGORITHM=COPY
* [Revision #446b3d3562](https://github.com/MariaDB/server/commit/446b3d3562)\
  2018-01-30 17:40:40 +0200
  * [MDEV-14875](https://jira.mariadb.org/browse/MDEV-14875): galera\_new\_cluster crashes mysqld when existing server contains databases
* [Revision #cea431e1f7](https://github.com/MariaDB/server/commit/cea431e1f7)\
  2018-01-30 14:56:33 +0200
  * Fix some wrong test result
* [Revision #5010ab26de](https://github.com/MariaDB/server/commit/5010ab26de)\
  2018-01-29 22:28:31 +0200
  * [MDEV-14209](https://jira.mariadb.org/browse/MDEV-14209) innodb\_gis.rtree\_debug produces huge server error logs
* [Revision #d9c77f0341](https://github.com/MariaDB/server/commit/d9c77f0341)\
  2018-01-29 11:10:09 +0200
  * Revert "[MDEV-6928](https://jira.mariadb.org/browse/MDEV-6928): Add trx pointer to struct mtr\_t"
* [Revision #7cdf759c86](https://github.com/MariaDB/server/commit/7cdf759c86)\
  2018-01-27 17:46:31 +0000
  * [MDEV-14485](https://jira.mariadb.org/browse/MDEV-14485) Server hangs on startup in THD::init
* [Revision #1da063a45b](https://github.com/MariaDB/server/commit/1da063a45b)\
  2018-01-28 19:03:07 +0200
  * Remove unused metadata for non-existing sync\_thread\_mutex
* [Revision #95f3933944](https://github.com/MariaDB/server/commit/95f3933944)\
  2018-01-27 15:03:30 +0200
  * Fixed compiler warnings
* [Revision #8ff5ddae23](https://github.com/MariaDB/server/commit/8ff5ddae23)\
  2018-01-27 14:39:33 +0200
  * Disable rocksdb when building with ASAN
* [Revision #c09371dce6](https://github.com/MariaDB/server/commit/c09371dce6)\
  2018-01-26 23:26:39 +0200
  * [MDEV-14721](https://jira.mariadb.org/browse/MDEV-14721) Big transaction events get lost on semisync master when replicate\_events\_marked\_for\_skip=FILTER\_ON\_MASTER
* Merge [Revision #0d31b4b328](https://github.com/MariaDB/server/commit/0d31b4b328) 2018-01-26 16:38:24 +0000 - Merge branch '10.2' of [server](https://github.com/mariadb/server) into 10.2
* [Revision #204739df14](https://github.com/MariaDB/server/commit/204739df14)\
  2018-01-26 15:04:20 +0200
  * Fixed memory overrun in create\_postjoin\_aggr\_table()
* [Revision #067b90c7a9](https://github.com/MariaDB/server/commit/067b90c7a9)\
  2018-01-25 14:50:11 +0000
  * Fix MinSizeRel build on Windows.
* [Revision #477a1bc42b](https://github.com/MariaDB/server/commit/477a1bc42b)\
  2018-01-15 18:59:27 +0000
  * Windows : fix compile warnings C4267, on 32bit first
* [Revision #db28f0f8da](https://github.com/MariaDB/server/commit/db28f0f8da)\
  2018-01-14 12:47:16 +0100
  * update C/C
* [Revision #9891ee5a2a](https://github.com/MariaDB/server/commit/9891ee5a2a)\
  2018-01-12 18:25:02 +0000
  * Fix and reenable Windows compiler warning C4800 (size\_t conversion).
* [Revision #859d100d70](https://github.com/MariaDB/server/commit/859d100d70)\
  2018-01-25 11:28:38 +0200
  * [MDEV-15063](https://jira.mariadb.org/browse/MDEV-15063): InnoDB assertion failure !is\_owned() at dict0defrag\_bg.cc:327
* [Revision #7fc25cfbca](https://github.com/MariaDB/server/commit/7fc25cfbca)\
  2018-01-24 23:33:21 +0200
  * Fix for [MDEV-12730](https://jira.mariadb.org/browse/MDEV-12730)
* [Revision #0dbe3dbe79](https://github.com/MariaDB/server/commit/0dbe3dbe79)\
  2018-01-24 16:28:54 +0200
  * [MDEV-15057](https://jira.mariadb.org/browse/MDEV-15057) Crash when using an unknown identifier as an SP parameter
* [Revision #c269f1d6fe](https://github.com/MariaDB/server/commit/c269f1d6fe)\
  2018-01-24 10:46:04 +0200
  * Allocate page\_cleaner and page\_cleaner.slot\[] statically
* [Revision #ac3e7f788e](https://github.com/MariaDB/server/commit/ac3e7f788e)\
  2018-01-24 10:23:52 +0200
  * [MDEV-15016](https://jira.mariadb.org/browse/MDEV-15016): multiple page cleaner threads use a lot of CPU
* [Revision #12f900228f](https://github.com/MariaDB/server/commit/12f900228f)\
  2018-01-16 14:24:27 +1100
  * mariadbbackup: use defaults-group-suffix even if no --defaults-file
* [Revision #7cc507f22e](https://github.com/MariaDB/server/commit/7cc507f22e)\
  2018-01-23 17:12:29 +0400
  * [MDEV-14603](https://jira.mariadb.org/browse/MDEV-14603) signal 11 with short stacktrace
* [Revision #87db5eb813](https://github.com/MariaDB/server/commit/87db5eb813)\
  2018-01-23 09:12:25 +0000
  * [MDEV-13825](https://jira.mariadb.org/browse/MDEV-13825) mariadb-backup --lock-ddl-per-table does not properly lock FULLTEXT auxiliary tables
* [Revision #29eeb527fd](https://github.com/MariaDB/server/commit/29eeb527fd)\
  2018-01-22 16:53:33 +0200
  * [MDEV-12173](https://jira.mariadb.org/browse/MDEV-12173) "\[Warning] Trying to access missing tablespace"
* [Revision #89ae5d7f2f](https://github.com/MariaDB/server/commit/89ae5d7f2f)\
  2018-01-22 16:30:38 +0200
  * Allocate mutex\_monitor, create\_tracker statically
* [Revision #30f1d2f642](https://github.com/MariaDB/server/commit/30f1d2f642)\
  2018-01-22 16:29:43 +0200
  * Remove useless method LatchCounter::sum\_deregister()
* [Revision #d04e1d4bdc](https://github.com/MariaDB/server/commit/d04e1d4bdc)\
  2018-01-22 15:27:24 +0200
  * [MDEV-15029](https://jira.mariadb.org/browse/MDEV-15029) XA COMMIT and XA ROLLBACK operate on freed transaction object
* [Revision #9b4dfdaa5a](https://github.com/MariaDB/server/commit/9b4dfdaa5a)\
  2018-01-18 15:25:40 +0300
  * [MDEV-13352](https://jira.mariadb.org/browse/MDEV-13352): Server crashes in st\_join\_table::remove\_duplicates
* [Revision #4f8555f1f6](https://github.com/MariaDB/server/commit/4f8555f1f6)\
  2018-01-21 18:23:28 +0200
  * [MDEV-14941](https://jira.mariadb.org/browse/MDEV-14941) Timeouts on persistent statistics tables caused by [MDEV-14511](https://jira.mariadb.org/browse/MDEV-14511)
* [Revision #6b7dcefdc8](https://github.com/MariaDB/server/commit/6b7dcefdc8)\
  2018-01-21 20:16:22 +0200
  * Reset thd->lex->current\_select for SP
* [Revision #f67b8273c0](https://github.com/MariaDB/server/commit/f67b8273c0)\
  2018-01-21 17:17:16 +0200
  * Fixed wrong arguments to printf in InnoDB
* [Revision #30289a2713](https://github.com/MariaDB/server/commit/30289a2713)\
  2018-01-18 15:56:28 -0800
  * Fixed [MDEV-14969](https://jira.mariadb.org/browse/MDEV-14969) Non-recursive Common Table Expressions used in view caused an error
* [Revision #6c09a6542e](https://github.com/MariaDB/server/commit/6c09a6542e)\
  2018-01-18 16:13:50 +0200
  * [MDEV-14985](https://jira.mariadb.org/browse/MDEV-14985) innodb\_undo\_log\_truncate may be blocked if transactions were recovered at startup
* [Revision #cc915cd599](https://github.com/MariaDB/server/commit/cc915cd599)\
  2018-01-18 01:42:51 +0200
  * Fixed some build scripts to work with gprof and gcov
* [Revision #50de7d1303](https://github.com/MariaDB/server/commit/50de7d1303)\
  2018-01-18 01:41:52 +0200
  * Fixed [MDEV-14326](https://jira.mariadb.org/browse/MDEV-14326) engine ARIA with row\_format=FIXED is broken
* [Revision #f44017384a](https://github.com/MariaDB/server/commit/f44017384a)\
  2018-01-16 20:02:38 +0200
  * [MDEV-14968](https://jira.mariadb.org/browse/MDEV-14968) On upgrade, InnoDB reports "started; log sequence number 0"
* [Revision #81378b3947](https://github.com/MariaDB/server/commit/81378b3947)\
  2018-01-16 16:09:51 +0400
  * Moving a change\_list related methods from THD to Item\_change\_list
* [Revision #be85c2dc88](https://github.com/MariaDB/server/commit/be85c2dc88)\
  2018-01-16 13:57:30 +0200
  * mariadb-backup --prepare: Do not access transactions or data dictionary
* [Revision #33ecf8345d](https://github.com/MariaDB/server/commit/33ecf8345d)\
  2018-01-16 13:55:45 +0200
  * Follow-up fix to [MDEV-14441](https://jira.mariadb.org/browse/MDEV-14441): Fix a potential race condition
* [Revision #f5e158183c](https://github.com/MariaDB/server/commit/f5e158183c)\
  2018-01-16 07:46:51 +0200
  * Follow-up fix to [MDEV-14441](https://jira.mariadb.org/browse/MDEV-14441): Correct a misplaced condition
* [Revision #0292cd0a27](https://github.com/MariaDB/server/commit/0292cd0a27)\
  2018-01-15 21:08:00 +0300
  * Better explanation why rpl\_row\_triggers is disabled.
* [Revision #3fdd390791](https://github.com/MariaDB/server/commit/3fdd390791)\
  2018-01-15 19:02:38 +0200
  * [MDEV-14441](https://jira.mariadb.org/browse/MDEV-14441) InnoDB hangs when setting innodb\_adaptive\_hash\_index=OFF during UPDATE
* [Revision #9c6fc7b644](https://github.com/MariaDB/server/commit/9c6fc7b644)\
  2018-01-15 16:38:16 +0200
  * Fix -Wsign-compare introduced by Compilation speed (#546)
* Merge [Revision #27b6b2625e](https://github.com/MariaDB/server/commit/27b6b2625e) 2018-01-15 16:22:02 +0200 - Merge 10.1 into 10.2
* [Revision #85aea5a12b](https://github.com/MariaDB/server/commit/85aea5a12b)\
  2018-01-15 16:50:18 +0300
  * Update .result for rocksdb.rpl\_row\_triggers (not the whole test works yet)
* [Revision #850702da6b](https://github.com/MariaDB/server/commit/850702da6b)\
  2018-01-15 15:37:22 +0200
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Merge InnoDB test cases from MySQL 5.7 (part 6)
* [Revision #ec062c6181](https://github.com/MariaDB/server/commit/ec062c6181)\
  2018-01-15 15:26:02 +0200
  * [MDEV-12121](https://jira.mariadb.org/browse/MDEV-12121) follow-up: Unbreak the WITH\_INNODB\_AHI=OFF build
* [Revision #72136ae75c](https://github.com/MariaDB/server/commit/72136ae75c)\
  2018-01-14 19:50:45 +0300
  * Compilation speed (#546)
* [Revision #fc65577873](https://github.com/MariaDB/server/commit/fc65577873)\
  2018-01-13 18:04:03 +0200
  * [MDEV-14887](https://jira.mariadb.org/browse/MDEV-14887) On a 32-bit system, [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) mishandles data file sizes exceeding 4GiB
* [Revision #09ef28abd7](https://github.com/MariaDB/server/commit/09ef28abd7)\
  2018-01-13 16:38:43 +0200
  * Fixed BUILD scripts
* Merge [Revision #1eea7966f3](https://github.com/MariaDB/server/commit/1eea7966f3) 2018-01-13 01:27:35 +0300 - Merge branch 'bb-10.2-mariarocks' into 10.2
* [Revision #4cafd8e66f](https://github.com/MariaDB/server/commit/4cafd8e66f)\
  2018-01-13 01:26:06 +0300
  * rocksdb.information\_schema testcase is not stable
* [Revision #2da1917912](https://github.com/MariaDB/server/commit/2da1917912)\
  2018-01-12 16:04:29 +0000
  * Attempt to eliminate race conditions in rocksdb.information\_schema
* [Revision #028e2ddc54](https://github.com/MariaDB/server/commit/028e2ddc54)\
  2018-01-12 19:16:36 +0530
  * Added a missing result file to the rocksdb\_sys\_vars result suite
* [Revision #c481fc9ca7](https://github.com/MariaDB/server/commit/c481fc9ca7)\
  2018-01-12 15:57:08 +0300
  * Change MyRocks maturity from Alpha to Beta
* [Revision #d32f5be307](https://github.com/MariaDB/server/commit/d32f5be307)\
  2018-01-12 15:11:56 +0300
  * [MDEV-14372](https://jira.mariadb.org/browse/MDEV-14372): Fix and enable rocksdb.information\_schema test
* [Revision #bf7719111f](https://github.com/MariaDB/server/commit/bf7719111f)\
  2018-01-11 17:09:51 +0200
  * Removed duplicated copyright message
* [Revision #30ecd2884a](https://github.com/MariaDB/server/commit/30ecd2884a)\
  2018-01-11 12:12:31 +0200
  * Fix compilation warnings for libmariadb
* Merge [Revision #e9842de20c](https://github.com/MariaDB/server/commit/e9842de20c) 2018-01-11 12:03:23 +0200 - Merge 10.1 into 10.2
* [Revision #cdb7a8fa69](https://github.com/MariaDB/server/commit/cdb7a8fa69)\
  2018-01-10 20:16:52 +0000
  * Silence warning coming from Windows' own header dbghelp.h
* [Revision #79fc074710](https://github.com/MariaDB/server/commit/79fc074710)\
  2018-01-10 16:43:25 +0000
  * Update CONC
* [Revision #ec97aba284](https://github.com/MariaDB/server/commit/ec97aba284)\
  2018-01-10 19:36:38 +0200
  * Fixed BUILD scripts
* [Revision #dfde5ae912](https://github.com/MariaDB/server/commit/dfde5ae912)\
  2018-01-10 13:53:44 +0200
  * [MDEV-14130](https://jira.mariadb.org/browse/MDEV-14130) InnoDB messages should not refer to the MySQL 5.7 manual
* [Revision #d1cf9b167c](https://github.com/MariaDB/server/commit/d1cf9b167c)\
  2018-01-10 13:18:02 +0200
  * [MDEV-14909](https://jira.mariadb.org/browse/MDEV-14909) [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) refuses to start up after clean shutdown of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md)
* [Revision #b132d4d749](https://github.com/MariaDB/server/commit/b132d4d749)\
  2018-01-09 22:52:01 +0000
  * Windows, compilation : Treat warning as error, if MYSQL\_MAINTAINER\_MODE is set to ERR
* [Revision #7d201d7b30](https://github.com/MariaDB/server/commit/7d201d7b30)\
  2018-01-06 09:32:47 -0800
  * Fixed [MDEV-14879](https://jira.mariadb.org/browse/MDEV-14879) Lost rows for query using recursive CTE with recursive reference in subquery
* [Revision #075f61a1d4](https://github.com/MariaDB/server/commit/075f61a1d4)\
  2018-01-09 11:30:36 +0200
  * Revert part of commit fec844aca88e1c6b9c36bb0b811e92d9d023ffb9
* Merge [Revision #5208e89807](https://github.com/MariaDB/server/commit/5208e89807) 2018-01-08 17:21:23 +0200 - Merge 10.1 into 10.2
* Merge [Revision #d8eef0f611](https://github.com/MariaDB/server/commit/d8eef0f611) 2018-01-08 16:45:58 +0200 - Merge 10.1 into 10.2
* [Revision #899c5899be](https://github.com/MariaDB/server/commit/899c5899be)\
  2018-01-08 12:58:25 +0200
  * MLOG-13101 Debug assertion failed in recv\_parse\_or\_apply\_log\_rec\_body()
* [Revision #8099941b46](https://github.com/MariaDB/server/commit/8099941b46)\
  2018-01-08 10:58:36 +0200
  * [MDEV-13487](https://jira.mariadb.org/browse/MDEV-13487) Assertion failure in rec\_get\_trx\_id()
* [Revision #ae7e1b9b13](https://github.com/MariaDB/server/commit/ae7e1b9b13)\
  2018-01-08 12:25:31 +0200
  * [MDEV-13262](https://jira.mariadb.org/browse/MDEV-13262): innodb.deadlock\_detect failed in buildbot
* Merge [Revision #9ede569260](https://github.com/MariaDB/server/commit/9ede569260) 2018-01-08 09:54:40 +0200 - Merge 10.1 into 10.2
* [Revision #73cf630ffc](https://github.com/MariaDB/server/commit/73cf630ffc)\
  2018-01-06 23:51:37 +0530
  * Fix Compile Error while using Flag '-DUSE\_ARIA\_FOR\_TMP\_TABLES:BOOL=OFF'
* Merge [Revision #59990747bc](https://github.com/MariaDB/server/commit/59990747bc) 2018-01-06 17:39:50 +0000 - Merge remote-tracking branch 'origin/10.1' into 10.2
* Merge [Revision #da39ca1f67](https://github.com/MariaDB/server/commit/da39ca1f67) 2018-01-06 17:39:19 +0000 - Merge branch '10.2' of [server](https://github.com/mariadb/server) into 10.2
* [Revision #15b1840f43](https://github.com/MariaDB/server/commit/15b1840f43)\
  2018-01-05 12:13:23 -0800
  * Added the test case from for [MDEV-14777](https://jira.mariadb.org/browse/MDEV-14777): Crash in [MariaDB 10.2.12](../../old-releases/10.2/10.2.12.md) on query using VIEW and WITH RECURSIVE.
* [Revision #578345305e](https://github.com/MariaDB/server/commit/578345305e)\
  2018-01-05 10:17:29 -0800
  * Added a test case for [MDEV-13454](https://jira.mariadb.org/browse/MDEV-13454): Improper error in ONLY\_FULL\_GROUP\_BY sql\_mode with condition\_pushdown\_for\_derived=on
* Merge [Revision #e6e24fe836](https://github.com/MariaDB/server/commit/e6e24fe836) 2018-01-05 16:52:25 +0000 - Merge branch '10.2' of [server](https://github.com/mariadb/server) into 10.2
* [Revision #0de565a564](https://github.com/MariaDB/server/commit/0de565a564)\
  2018-01-04 23:40:37 -0800
  * Fixed [MDEV-14852](https://jira.mariadb.org/browse/MDEV-14852) Fails to reopen temp table within standard CTE
* Merge [Revision #287d105398](https://github.com/MariaDB/server/commit/287d105398) 2018-01-05 12:11:58 +0200 - Merge 10.1 into 10.2
* [Revision #9c9db1cbe2](https://github.com/MariaDB/server/commit/9c9db1cbe2)\
  2018-01-05 11:58:45 +0200
  * [MDEV-14059](https://jira.mariadb.org/browse/MDEV-14059) Work around a problem exposed by InnoDB GIS debug check
* Merge [Revision #c8e6364407](https://github.com/MariaDB/server/commit/c8e6364407) 2018-01-04 20:47:34 +0200 - Merge branch 10.1 into 10.2
* [Revision #8dc77a72ea](https://github.com/MariaDB/server/commit/8dc77a72ea)\
  2018-01-04 19:16:59 +0200
  * [MDEV-14057](https://jira.mariadb.org/browse/MDEV-14057) InnoDB GIS tests fail
* [Revision #218dbf68b8](https://github.com/MariaDB/server/commit/218dbf68b8)\
  2018-01-04 19:32:29 +0200
  * [MDEV-14058](https://jira.mariadb.org/browse/MDEV-14058) InnoDB Assertion failure !leaf on rem0rec.cc line 566 on test innodb\_gis.rtree\_recovery
* [Revision #0f253d3e64](https://github.com/MariaDB/server/commit/0f253d3e64)\
  2018-01-04 10:41:08 -0500
  * bump the VERSION
* [Revision #5e0b13d173](https://github.com/MariaDB/server/commit/5e0b13d173)\
  2018-01-04 16:21:18 +0200
  * Fixed wrong arguments to printf and related functions
* [Revision #b9e0945397](https://github.com/MariaDB/server/commit/b9e0945397)\
  2018-01-04 16:52:15 +0000
  * update libmariadb
* [Revision #c584a496d7](https://github.com/MariaDB/server/commit/c584a496d7)\
  2018-01-04 14:04:52 +0300
  * Fix out-of-date comments.
* [Revision #af0ba43838](https://github.com/MariaDB/server/commit/af0ba43838)\
  2018-01-03 22:21:32 +0200
  * Do not misspell "fall through"
* Merge [Revision #fcde91114d](https://github.com/MariaDB/server/commit/fcde91114d) 2018-01-03 20:42:09 +0200 - Merge 10.1 into 10.2

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
