# MariaDB 10.2.9 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.9)[Release Notes](../../old-releases/10.2/10.2.9.md)[Changelog](mariadb-1029-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 27 Sep 2017

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.9.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #21614f4a85](https://github.com/MariaDB/server/commit/21614f4a85)\
  2017-09-25 09:29:27 +0300
  * [MDEV-13898](https://jira.mariadb.org/browse/MDEV-13898) Corruption during online table-rebuilding ALTER of ROW\_FORMAT=REDUNDANT tables
* [Revision #cd2a85e763](https://github.com/MariaDB/server/commit/cd2a85e763)\
  2017-09-22 21:47:38 +0300
  * Updated list of unstable tests for 10.2.9
* [Revision #ca3c8d9b58](https://github.com/MariaDB/server/commit/ca3c8d9b58)\
  2017-09-22 13:57:25 +0200
  * shut out Connect cmake-time warning about missing Findlibmondgodoc.cmake
* [Revision #68d1a598bc](https://github.com/MariaDB/server/commit/68d1a598bc)\
  2017-09-21 21:21:36 +0200
  * bugfix: copy timestamps correctly in INSERT...SELECT
* [Revision #a5e1f60b31](https://github.com/MariaDB/server/commit/a5e1f60b31)\
  2017-09-21 20:08:59 +0200
  * bugfix: ALTER TABLE and TIMESTAMPs around DST change time
* [Revision #bc4409ab4e](https://github.com/MariaDB/server/commit/bc4409ab4e)\
  2017-09-22 01:12:00 +0200
  * [MDEV-13868](https://jira.mariadb.org/browse/MDEV-13868) cannot insert 1288481126 in a timestamp column in Europe/Moscow
* Merge [Revision #f1ce69f3a9](https://github.com/MariaDB/server/commit/f1ce69f3a9) 2017-09-22 00:58:21 +0200 - Merge branch '10.1' into 10.2
* [Revision #3fbd4aa032](https://github.com/MariaDB/server/commit/3fbd4aa032)\
  2017-09-21 16:05:39 +0000
  * CMake : Do not use FindPkgConfig on Windows
* [Revision #0a44ae6528](https://github.com/MariaDB/server/commit/0a44ae6528)\
  2017-09-21 16:30:24 +0300
  * Fix that FLUSH TABLES FOR EXPORT also works for Aria tables.
* [Revision #05da63f048](https://github.com/MariaDB/server/commit/05da63f048)\
  2017-09-21 12:05:21 +0300
  * Correct debug assertions
* [Revision #02de2385a2](https://github.com/MariaDB/server/commit/02de2385a2)\
  2017-09-21 10:15:27 +0300
  * page\_rec\_is\_leaf(): Fix sign mismatch warnings
* [Revision #9c373d4d1d](https://github.com/MariaDB/server/commit/9c373d4d1d)\
  2017-09-21 10:07:28 +0300
  * Fix bogus rec\_get\_offsets() debug assertion failures for ROW\_FORMAT=REDUNDANT
* [Revision #c9c1adc649](https://github.com/MariaDB/server/commit/c9c1adc649)\
  2017-09-21 08:21:06 +0300
  * Avoid comparison of unsigned to signed
* [Revision #f3b6c49f8f](https://github.com/MariaDB/server/commit/f3b6c49f8f)\
  2017-09-20 12:53:57 +0200
  * [MDEV-13589](https://jira.mariadb.org/browse/MDEV-13589) libmariadbclient18 is broken when using mariadb repo instead of debian's
* [Revision #dc112d2f48](https://github.com/MariaDB/server/commit/dc112d2f48)\
  2017-09-20 22:46:25 +0300
  * Fix -Wimplicit-fallthrough warnings (no functional change)
* [Revision #47cd984a3a](https://github.com/MariaDB/server/commit/47cd984a3a)\
  2017-09-20 22:34:20 +0300
  * Fix ut\_ad(!leaf) failure in rec\_get\_offsets\_func() with spatial index
* [Revision #a1e47974b7](https://github.com/MariaDB/server/commit/a1e47974b7)\
  2017-09-20 18:09:45 +0300
  * Avoid comparison of unsigned to signed
* [Revision #96f06f952d](https://github.com/MariaDB/server/commit/96f06f952d)\
  2017-09-20 16:52:11 +0300
  * [MDEV-13847](https://jira.mariadb.org/browse/MDEV-13847) Allow ALTER TABLE…ADD SPATIAL INDEX…ALGORITHM=INPLACE
* [Revision #e53e58d4e4](https://github.com/MariaDB/server/commit/e53e58d4e4)\
  2017-09-20 14:55:14 +0300
  * Add a missing const qualifier
* [Revision #48192f963a](https://github.com/MariaDB/server/commit/48192f963a)\
  2017-09-19 19:20:11 +0300
  * Add the parameter bool leaf to rec\_get\_offsets()
* Merge [Revision #2d9f5f69d4](https://github.com/MariaDB/server/commit/2d9f5f69d4) 2017-09-20 10:46:09 +0300 - Merge branch '10.1' into 10.2
* Merge [Revision #246d321f67](https://github.com/MariaDB/server/commit/246d321f67) 2017-09-20 10:33:13 +0300 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* [Revision #c53f57c390](https://github.com/MariaDB/server/commit/c53f57c390)\
  2017-09-19 21:53:08 +0300
  * Remove DICT\_UNIVERSAL
* [Revision #5792b016f1](https://github.com/MariaDB/server/commit/5792b016f1)\
  2017-09-20 08:17:06 +0300
  * Fix a typo
* [Revision #6b687a0fde](https://github.com/MariaDB/server/commit/6b687a0fde)\
  2017-09-19 12:40:29 +0300
  * Introduce page\_rec\_is\_leaf() and clean up page0page.h
* [Revision #77b241eb10](https://github.com/MariaDB/server/commit/77b241eb10)\
  2017-09-19 19:24:00 +0300
  * Correct a test result
* [Revision #e42c6d1afe](https://github.com/MariaDB/server/commit/e42c6d1afe)\
  2017-09-20 00:45:09 +0300
  * Update libmariadb submodule
* [Revision #d66856c4f7](https://github.com/MariaDB/server/commit/d66856c4f7)\
  2017-09-20 00:37:51 +0300
  * Update testcase post merge
* [Revision #325718c996](https://github.com/MariaDB/server/commit/325718c996)\
  2017-09-19 17:23:55 +0300
  * Remove libmariadbclient18.links post merge
* [Revision #a1e589be9b](https://github.com/MariaDB/server/commit/a1e589be9b)\
  2017-09-18 18:57:17 +0300
  * [MDEV-13354](https://jira.mariadb.org/browse/MDEV-13354): Server crashes in find\_field\_in\_tables upon PS with window function and subquery
* [Revision #454b9b1bdc](https://github.com/MariaDB/server/commit/454b9b1bdc)\
  2017-09-11 22:46:11 +0300
  * [MDEV-13774](https://jira.mariadb.org/browse/MDEV-13774): Server Crash on Execute of SQL Statement
* [Revision #33209350f7](https://github.com/MariaDB/server/commit/33209350f7)\
  2017-09-11 13:30:39 +0300
  * [MDEV-13649](https://jira.mariadb.org/browse/MDEV-13649): Server crashes in set\_field\_to\_null\_with\_conversions or in Field::set\_notnull
* [Revision #02eda36e4e](https://github.com/MariaDB/server/commit/02eda36e4e)\
  2017-09-11 12:03:16 +0300
  * [MDEV-13358](https://jira.mariadb.org/browse/MDEV-13358): FIRST\_V throw SQL Fehler (1292): Incorrect datetime value
* Merge [Revision #5b9c32ede0](https://github.com/MariaDB/server/commit/5b9c32ede0) 2017-09-19 15:07:32 +0300 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #bf34e9db7b](https://github.com/MariaDB/server/commit/bf34e9db7b)\
  2017-09-11 16:23:06 +0200
  * Enable MONGO for the C driver. Modified: modified: storage/connect/CMakeLists.txt
* [Revision #7e65bdba7b](https://github.com/MariaDB/server/commit/7e65bdba7b)\
  2017-09-04 22:32:02 +0200\
  \*
  * Update version number modified: storage/connect/ha\_connect.cc
* [Revision #703ce16a11](https://github.com/MariaDB/server/commit/703ce16a11)\
  2017-09-02 16:01:31 +0200\
  \*
  * Add more trace to tbl\_thread.test (to debug failure) modified: storage/connect/mysql-test/connect/r/tbl\_thread.result modified: storage/connect/mysql-test/connect/t/tbl\_thread.test
* [Revision #7ccce51b09](https://github.com/MariaDB/server/commit/7ccce51b09)\
  2017-09-02 14:57:49 +0200
  * Disable MONGO modified: storage/connect/CMakeLists.txt
* [Revision #01d86c74af](https://github.com/MariaDB/server/commit/01d86c74af)\
  2017-09-02 10:59:39 +0200\
  \*
  * Fix MongoDB C Driver adding for CMAKE. Requires MongoDB C Driver version 1.7 now available modified: storage/connect/CMakeLists.txt
* [Revision #36b2dec114](https://github.com/MariaDB/server/commit/36b2dec114)\
  2017-08-31 01:22:50 +0200\
  \*
  * Set MONGO\_ENABLED modified: storage/connect/CMakeLists.txt
* [Revision #96252b6abd](https://github.com/MariaDB/server/commit/96252b6abd)\
  2017-08-29 17:35:27 +0200\
  \*
  * New distribution enabling or disabling the MONGO table type modified: storage/connect/CMakeLists.txt modified: storage/connect/ha\_connect.cc modified: storage/connect/mycat.cc
* [Revision #438211a175](https://github.com/MariaDB/server/commit/438211a175)\
  2017-08-26 16:18:43 +0200\
  \*
  * Fix [MDEV-13621](https://jira.mariadb.org/browse/MDEV-13621) Replace sprintf by strcpy for opval modified: storage/connect/ha\_connect.cc
* [Revision #614611d7c0](https://github.com/MariaDB/server/commit/614611d7c0)\
  2017-08-26 11:02:53 +0200\
  \*
  * Fix [MDEV-13621](https://jira.mariadb.org/browse/MDEV-13621) JDBC UPDATE containing single or double quote chars produces wrong result in ha\_connect::GetStringOption modified: storage/connect/ha\_connect.cc
* [Revision #2db52e1704](https://github.com/MariaDB/server/commit/2db52e1704)\
  2017-08-17 16:13:01 +0200\
  \*
  * Fix failing test tbl\_thread on linux (and mask another fail until [MDEV-10179](https://jira.mariadb.org/browse/MDEV-10179) is fixed) modified: storage/connect/mysql-test/connect/r/tbl\_thread.result modified: storage/connect/mysql-test/connect/t/tbl\_thread.test
* Merge [Revision #22c322c649](https://github.com/MariaDB/server/commit/22c322c649) 2017-09-19 12:43:02 +0300 - Merge branch '10.1' into 10.2
* [Revision #7d49aab32c](https://github.com/MariaDB/server/commit/7d49aab32c)\
  2017-09-15 17:30:09 +0200
  * apparmor: allow to read /etc/mysql/mariadb.conf.d/\*
* Merge [Revision #956b5f16e8](https://github.com/MariaDB/server/commit/956b5f16e8) 2017-09-18 19:32:03 +0300 - Merge pull request #446 from darkain/patch-1
* [Revision #7f2fab0106](https://github.com/MariaDB/server/commit/7f2fab0106)\
  2017-09-13 10:48:10 -0700
  * Fixes Galera on FreeBSD
* [Revision #55c5448ab7](https://github.com/MariaDB/server/commit/55c5448ab7)\
  2017-09-15 16:43:06 +0200
  * [MDEV-13751](https://jira.mariadb.org/browse/MDEV-13751) Interrupted SELECT fails with 1030: 'Got error 1 "Operation not permitted" from storage engine MyISAM'
* [Revision #6670b4e58c](https://github.com/MariaDB/server/commit/6670b4e58c)\
  2017-09-15 15:05:39 +0200
  * [MDEV-13712](https://jira.mariadb.org/browse/MDEV-13712) Spelling errors in the error message
* [Revision #203e2176fe](https://github.com/MariaDB/server/commit/203e2176fe)\
  2017-09-15 15:03:41 +0200
  * [MDEV-13698](https://jira.mariadb.org/browse/MDEV-13698) stack overflow (OpenSSL on Windows)
* [Revision #50a8beedfe](https://github.com/MariaDB/server/commit/50a8beedfe)\
  2017-09-15 15:02:24 +0200
  * [MDEV-13708](https://jira.mariadb.org/browse/MDEV-13708) Crash with indexed virtual columns and FK cascading deletes
* [Revision #fb2035a1a3](https://github.com/MariaDB/server/commit/fb2035a1a3)\
  2017-09-15 00:29:56 +0200
  * [MDEV-13673](https://jira.mariadb.org/browse/MDEV-13673) Bad result in view
* [Revision #16b1cb6502](https://github.com/MariaDB/server/commit/16b1cb6502)\
  2017-09-14 19:31:04 +0200
  * [MDEV-13623](https://jira.mariadb.org/browse/MDEV-13623) Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed in virtual longlong Field\_long::val\_int
* [Revision #4c6c352138](https://github.com/MariaDB/server/commit/4c6c352138)\
  2017-09-14 15:10:23 +0200
  * [MDEV-13596](https://jira.mariadb.org/browse/MDEV-13596) CHECK constraints disallow NULL to pass through, violating SQL
* [Revision #e6ce97a592](https://github.com/MariaDB/server/commit/e6ce97a592)\
  2017-09-13 21:02:44 +0200
  * [MDEV-12951](https://jira.mariadb.org/browse/MDEV-12951) Server crash \[mysqld got exception 0xc0000005]
* [Revision #e78712d464](https://github.com/MariaDB/server/commit/e78712d464)\
  2017-09-13 19:54:48 +0200
  * cleanup: remove dead code
* [Revision #0267cad5e2](https://github.com/MariaDB/server/commit/0267cad5e2)\
  2017-09-13 22:45:20 +0200
  * bugfix: mtr non-reliable failure detection
* [Revision #6dfb73a97b](https://github.com/MariaDB/server/commit/6dfb73a97b)\
  2017-09-13 12:42:45 +0200
  * bugfix: deadlock on shutdown
* [Revision #8b1f145c82](https://github.com/MariaDB/server/commit/8b1f145c82)\
  2017-08-26 00:32:43 +0200
  * cleanup
* [Revision #3af191b7e1](https://github.com/MariaDB/server/commit/3af191b7e1)\
  2017-09-08 20:12:57 +0200
  * compiler warning
* [Revision #c4dc2b877a](https://github.com/MariaDB/server/commit/c4dc2b877a)\
  2017-09-12 18:55:05 +0200
  * bugfix: TIME\_FORMAT() should be ok in stored generated columns
* [Revision #3e5cdfae93](https://github.com/MariaDB/server/commit/3e5cdfae93)\
  2017-09-12 18:31:12 +0200
  * bugfix: TIME\_FORMAT() allowed some non-time format specifiers
* [Revision #3878baddf1](https://github.com/MariaDB/server/commit/3878baddf1)\
  2017-09-11 14:29:15 +0200
  * [MDEV-13773](https://jira.mariadb.org/browse/MDEV-13773) client packages need my\_global.h and/or my\_config.h
* [Revision #79ddd86615](https://github.com/MariaDB/server/commit/79ddd86615)\
  2017-09-11 14:39:31 +0200
  * bugfix: don't overwrite tokudb.cnf during the build
* [Revision #bba169b984](https://github.com/MariaDB/server/commit/bba169b984)\
  2017-09-11 12:29:37 +0200
  * [MDEV-12763](https://jira.mariadb.org/browse/MDEV-12763) 10.2 uses deprecated openssl 1.0 apis even with 1.1
* [Revision #031a0404e7](https://github.com/MariaDB/server/commit/031a0404e7)\
  2017-09-14 00:32:37 +0200
  * bugfix: debian dependencies
* [Revision #862fbc277c](https://github.com/MariaDB/server/commit/862fbc277c)\
  2017-09-12 15:07:00 +0200
  * bugfix: debian, fix \*.so symlinks in libmariadb-dev
* [Revision #b5ead3a658](https://github.com/MariaDB/server/commit/b5ead3a658)\
  2017-09-10 13:50:05 +0200
  * [MDEV-13589](https://jira.mariadb.org/browse/MDEV-13589) libmariadbclient18 is broken when using mariadb repo instead of debian's
* [Revision #0757a1b3e2](https://github.com/MariaDB/server/commit/0757a1b3e2)\
  2017-08-24 14:05:32 +0200
  * bugfix: allow dropping a constraint and a column together
* Merge [Revision #429ca9a881](https://github.com/MariaDB/server/commit/429ca9a881) 2017-09-18 11:10:21 +0300 - Merge 10.1 into 10.2
* [Revision #4bf087986f](https://github.com/MariaDB/server/commit/4bf087986f)\
  2017-09-18 11:10:06 +0300
  * Fix the WSREP build
* [Revision #3894fdd47a](https://github.com/MariaDB/server/commit/3894fdd47a)\
  2017-09-13 19:51:30 +0300
  * [MDEV-13678](https://jira.mariadb.org/browse/MDEV-13678): DELETE with CASCADE takes a long time when Galera is enabled
* [Revision #d186b99251](https://github.com/MariaDB/server/commit/d186b99251)\
  2017-08-25 11:33:13 +0300
  * MW-402 cascading FK issue (5.7 version)
* [Revision #16b374b978](https://github.com/MariaDB/server/commit/16b374b978)\
  2017-09-13 19:51:30 +0300
  * [MDEV-13678](https://jira.mariadb.org/browse/MDEV-13678): DELETE with CASCADE takes a long time when Galera is enabled
* [Revision #6a524ca56b](https://github.com/MariaDB/server/commit/6a524ca56b)\
  2017-08-25 11:33:13 +0300
  * MW-402 cascading FK issue (5.7 version)
* [Revision #efb673fe5f](https://github.com/MariaDB/server/commit/efb673fe5f)\
  2017-08-24 10:34:21 +0300
  * MW-402 cascading FK issues
* Merge [Revision #72c838b9fc](https://github.com/MariaDB/server/commit/72c838b9fc) 2017-09-17 13:54:43 +0300 - Null-merge 10.1 into 10.2
* [Revision #d6baf3d364](https://github.com/MariaDB/server/commit/d6baf3d364)\
  2017-09-17 13:46:51 +0300
  * [MDEV-12634](https://jira.mariadb.org/browse/MDEV-12634) after-merge test fix: Exercise row\_merge\_write(), row\_merge\_read()
* Merge [Revision #d9277732d7](https://github.com/MariaDB/server/commit/d9277732d7) 2017-09-16 22:31:53 +0300 - Merge 10.1 into 10.2
* [Revision #c2815c7c2c](https://github.com/MariaDB/server/commit/c2815c7c2c)\
  2017-09-15 20:44:03 +0000
  * add updated result file for [MDEV-13802](https://jira.mariadb.org/browse/MDEV-13802) test.
* [Revision #a07b537b39](https://github.com/MariaDB/server/commit/a07b537b39)\
  2017-09-15 20:09:41 +0300
  * Field\_varstring: Declare get\_data() and get\_length() as public
* [Revision #a449f72a4c](https://github.com/MariaDB/server/commit/a449f72a4c)\
  2017-09-15 17:25:38 +0300
  * Remove the redundant function row\_table\_got\_default\_clust\_index()
* [Revision #74f677fcc2](https://github.com/MariaDB/server/commit/74f677fcc2)\
  2017-09-14 16:42:09 +0000
  * [MDEV-13802](https://jira.mariadb.org/browse/MDEV-13802) mariadb-backup --lock-ddl-per-table fails when table names contain backticks
* [Revision #bb7ab40521](https://github.com/MariaDB/server/commit/bb7ab40521)\
  2017-09-13 12:10:48 +0000
  * mariadb-backup : Fix enumerate\_ibd\_files() to include .isl
* [Revision #a8b3c603c6](https://github.com/MariaDB/server/commit/a8b3c603c6)\
  2017-07-27 11:43:33 +0300
  * MW-394
* [Revision #ed9f68f6ad](https://github.com/MariaDB/server/commit/ed9f68f6ad)\
  2017-07-27 11:39:31 +0300
  * MW-394
* [Revision #f3435fc37e](https://github.com/MariaDB/server/commit/f3435fc37e)\
  2017-07-25 10:56:44 +0300
  * MW-394
* [Revision #e9d2f37abd](https://github.com/MariaDB/server/commit/e9d2f37abd)\
  2017-09-14 16:07:10 +0300
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626) Merge InnoDB test cases from MySQL 5.7 (part 2)
* [Revision #e2b9f6762c](https://github.com/MariaDB/server/commit/e2b9f6762c)\
  2017-09-14 14:30:24 +0400
  * Make compiler happy with the 'fall through' comments.
* [Revision #c94fb7b7c1](https://github.com/MariaDB/server/commit/c94fb7b7c1)\
  2017-09-14 11:16:40 +0400
  * Compiler warning avoided.
* [Revision #3f17f51132](https://github.com/MariaDB/server/commit/3f17f51132)\
  2017-09-14 08:58:31 +0300
  * Follow-up to [MDEV-13563](https://jira.mariadb.org/browse/MDEV-13563) mariadb-backup --lock-ddl-per-table
* [Revision #cfd51c01e1](https://github.com/MariaDB/server/commit/cfd51c01e1)\
  2017-09-14 08:06:40 +0300
  * Fix one more warning for page\_header\_get\_field()
* [Revision #126a581b45](https://github.com/MariaDB/server/commit/126a581b45)\
  2017-09-14 08:00:28 +0300
  * Fix warnings for page\_header\_get\_field() comparisons
* [Revision #88106ef352](https://github.com/MariaDB/server/commit/88106ef352)\
  2017-09-14 07:52:32 +0300
  * Fix a warning for a debug assertion
* [Revision #f5a833c3e0](https://github.com/MariaDB/server/commit/f5a833c3e0)\
  2017-09-13 15:41:04 +0300
  * Clean up the logging of virtual column values in table-rebuilding online ALTER
* [Revision #24062fed70](https://github.com/MariaDB/server/commit/24062fed70)\
  2017-09-13 11:04:49 +0300
  * Remove the debug variables innodb\_purge\_stop\_now, innodb\_purge\_run\_now
* [Revision #d06e4fc6a3](https://github.com/MariaDB/server/commit/d06e4fc6a3)\
  2017-09-13 09:31:13 +0300
  * Do not require a debug non-embedded server in the test
* [Revision #dd35fb35fa](https://github.com/MariaDB/server/commit/dd35fb35fa)\
  2017-09-13 09:27:15 +0300
  * Return uint16\_t instead of ulint
* [Revision #250ca1c1d2](https://github.com/MariaDB/server/commit/250ca1c1d2)\
  2017-09-13 16:45:42 +0400
  * [MDEV-13707](https://jira.mariadb.org/browse/MDEV-13707) Server in ORACLE mode crashes on ALTER with wrong DEFAULT clause
* [Revision #dc82f70e9f](https://github.com/MariaDB/server/commit/dc82f70e9f)\
  2017-09-13 15:17:28 +0400
  * [MDEV-13633](https://jira.mariadb.org/browse/MDEV-13633) JSON\_ARRAY() - bad output with some UTF8 characters.
* [Revision #a237a92099](https://github.com/MariaDB/server/commit/a237a92099)\
  2017-09-13 00:36:09 +0400
  * [MDEV-12877](https://jira.mariadb.org/browse/MDEV-12877) Wrong result from JSON native function.
* [Revision #80a3837283](https://github.com/MariaDB/server/commit/80a3837283)\
  2017-09-12 19:15:31 +0400
  * [MDEV-12877](https://jira.mariadb.org/browse/MDEV-12877) Wrong result from JSON native function.
* [Revision #825c8d793d](https://github.com/MariaDB/server/commit/825c8d793d)\
  2017-09-12 17:30:46 +0400
  * [MDEV-12774](https://jira.mariadb.org/browse/MDEV-12774) JSON\_EXTRACT fails with some escaped unicode as key.
* [Revision #30db4e1fc7](https://github.com/MariaDB/server/commit/30db4e1fc7)\
  2017-09-12 15:33:30 +0400
  * [MDEV-13786](https://jira.mariadb.org/browse/MDEV-13786) compiler complains about uninitialized variable.
* [Revision #0cd731864e](https://github.com/MariaDB/server/commit/0cd731864e)\
  2017-09-12 15:21:53 +0400
  * [MDEV-13104](https://jira.mariadb.org/browse/MDEV-13104) Json functions.
* [Revision #467acc2119](https://github.com/MariaDB/server/commit/467acc2119)\
  2017-09-12 14:40:18 +0400
  * [MDEV-13324](https://jira.mariadb.org/browse/MDEV-13324) JSON\_SET returns NULL instead of object.
* [Revision #49878be331](https://github.com/MariaDB/server/commit/49878be331)\
  2017-09-12 13:32:09 +0300
  * [MDEV-13602](https://jira.mariadb.org/browse/MDEV-13602): rocksdb.index\_merge\_rocksdb2 failed in buildbot
* [Revision #594c6b37f3](https://github.com/MariaDB/server/commit/594c6b37f3)\
  2017-09-12 13:26:03 +0400
  * [MDEV-13138](https://jira.mariadb.org/browse/MDEV-13138) JSON\_OBJECT returns null with strings containing backticks.
* [Revision #66a09bd6ab](https://github.com/MariaDB/server/commit/66a09bd6ab)\
  2017-09-11 16:47:23 +0300
  * [MDEV-13318](https://jira.mariadb.org/browse/MDEV-13318) Crash recovery failure after the server is killed during innodb\_encrypt\_log startup
* [Revision #8ee4b414ae](https://github.com/MariaDB/server/commit/8ee4b414ae)\
  2017-09-12 09:22:11 +0300
  * Relax a too strict debug assertion for mariadb-backup --prepare
* [Revision #ea876b39f3](https://github.com/MariaDB/server/commit/ea876b39f3)\
  2017-09-12 11:58:49 +0400
  * [MDEV-13716](https://jira.mariadb.org/browse/MDEV-13716) point\_big test fails in 10.2.
* [Revision #6352ec2184](https://github.com/MariaDB/server/commit/6352ec2184)\
  2017-09-12 11:20:30 +0400
  * [MDEV-12982](https://jira.mariadb.org/browse/MDEV-12982) JSON\_EXTRACT returns data for invalid JSON.
* [Revision #31774f0ede](https://github.com/MariaDB/server/commit/31774f0ede)\
  2017-09-11 16:45:36 +0000
  * [MDEV-13563](https://jira.mariadb.org/browse/MDEV-13563) lock DDL for mariadb-backup in 10.2
* [Revision #6b5c0effe4](https://github.com/MariaDB/server/commit/6b5c0effe4)\
  2017-09-07 11:13:08 +0200
  * [MDEV-13436](https://jira.mariadb.org/browse/MDEV-13436) PREPARE doesn't work as expected & throws errors but MySQL is working fine
* Merge [Revision #2425f2aedb](https://github.com/MariaDB/server/commit/2425f2aedb) 2017-09-08 15:38:02 +0300 - [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626) Merge InnoDB test cases from MySQL 5.7 (part 1)
* [Revision #672590afaf](https://github.com/MariaDB/server/commit/672590afaf)\
  2017-09-08 15:28:50 +0300
  * Adjust the imported innodb.alter\_crash test for MariaDB
* [Revision #13d4dfd02c](https://github.com/MariaDB/server/commit/13d4dfd02c)\
  2017-09-08 15:33:03 +0300
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626) Merge InnoDB test cases from MySQL 5.7 (part 1)
* [Revision #95f602698a](https://github.com/MariaDB/server/commit/95f602698a)\
  2017-09-08 09:38:42 +0300
  * Make a test more robust
* [Revision #18e17f134c](https://github.com/MariaDB/server/commit/18e17f134c)\
  2017-09-08 08:33:41 +0200
  * Windows : Fix MTR's misuse of servers --console parameter
* [Revision #d471469bd2](https://github.com/MariaDB/server/commit/d471469bd2)\
  2017-09-07 22:53:21 +0000
  * [MDEV-13466](https://jira.mariadb.org/browse/MDEV-13466) Implement --export option for MariaDB Backup
* Merge [Revision #d26fb96a9f](https://github.com/MariaDB/server/commit/d26fb96a9f) 2017-09-07 12:12:31 +0300 - Merge 10.1 into 10.2
* [Revision #3c45aa5895](https://github.com/MariaDB/server/commit/3c45aa5895)\
  2017-09-06 19:32:56 +0300
  * Fix a typo to silence -Wimplicit-fallthrough
* Merge [Revision #70db1e3b8a](https://github.com/MariaDB/server/commit/70db1e3b8a) 2017-09-06 19:28:51 +0300 - Merge 10.1 into 10.2
* [Revision #c59a52b7ba](https://github.com/MariaDB/server/commit/c59a52b7ba)\
  2017-09-06 19:08:55 +0300
  * Fix nondeterministic failure of innodb.table\_flags
* [Revision #b429e8cada](https://github.com/MariaDB/server/commit/b429e8cada)\
  2017-09-06 16:29:58 +0300
  * mariadb-backup: Detach the threads at exit
* [Revision #2b387855df](https://github.com/MariaDB/server/commit/2b387855df)\
  2017-09-06 17:20:31 +0200
  * [MDEV-13523](https://jira.mariadb.org/browse/MDEV-13523): Group By in a View, called within a Stored Routine causes Error Code 1356 when a non-root user runs the routine for a second time
* [Revision #80c90887fe](https://github.com/MariaDB/server/commit/80c90887fe)\
  2017-09-05 23:00:59 +0530
  * [MDEV-13585](https://jira.mariadb.org/browse/MDEV-13585): RocksDB plugin fails to build on macOS because of unknown type `timer_t` etc.
* [Revision #4ae200a97a](https://github.com/MariaDB/server/commit/4ae200a97a)\
  2017-09-05 18:28:05 +0300
  * Update test results for rocksdb.bulk\_load\_rev\_cf\_and\_data
* [Revision #8592ff9e8d](https://github.com/MariaDB/server/commit/8592ff9e8d)\
  2017-07-06 14:03:23 +0300
  * [MDEV-12731](https://jira.mariadb.org/browse/MDEV-12731)
* [Revision #720928782f](https://github.com/MariaDB/server/commit/720928782f)\
  2017-09-03 09:33:27 +0200
  * Fix bash expansion issue in wsrep\_sst\_rsync (#443)
* [Revision #1136c8d366](https://github.com/MariaDB/server/commit/1136c8d366)\
  2017-09-01 22:07:43 +0300
  * Follow-up to [MDEV-13570](https://jira.mariadb.org/browse/MDEV-13570) Assertion failure !srv\_read\_only\_mode in --innodb-read-only shutdown when buf\_resize\_thread is active
* [Revision #b660584b10](https://github.com/MariaDB/server/commit/b660584b10)\
  2017-09-01 11:23:45 +0300
  * After-merge fix for a Galera test result
* [Revision #1b41a54fc9](https://github.com/MariaDB/server/commit/1b41a54fc9)\
  2017-09-01 08:38:19 +0300
  * Fix test for [MDEV-13674](https://jira.mariadb.org/browse/MDEV-13674): Deprecate innodb\_use\_mtflush and innodb\_mtflush\_threads
* Merge [Revision #5660c061fa](https://github.com/MariaDB/server/commit/5660c061fa) 2017-08-31 18:06:11 +0300 - Merge 10.1 into 10.2
* [Revision #a9e71c77e4](https://github.com/MariaDB/server/commit/a9e71c77e4)\
  2017-08-31 14:35:35 +0300
  * Disable a badly written, randomly failing Galera test
* [Revision #e23de9f2e0](https://github.com/MariaDB/server/commit/e23de9f2e0)\
  2017-08-31 13:36:36 +0300
  * [MDEV-13674](https://jira.mariadb.org/browse/MDEV-13674): Deprecate innodb\_use\_mtflush and innodb\_mtflush\_threads
* [Revision #aa22981dd2](https://github.com/MariaDB/server/commit/aa22981dd2)\
  2017-05-11 11:15:37 +0300
  * [MDEV-12741](https://jira.mariadb.org/browse/MDEV-12741): innodb.ibuf\_not\_empty failed in buildbot with "InnoDB: Trying to do I/O to a tablespace which does not exist"
* [Revision #0e45edf350](https://github.com/MariaDB/server/commit/0e45edf350)\
  2017-08-31 11:42:41 +0300
  * [MDEV-13669](https://jira.mariadb.org/browse/MDEV-13669): Some MyRocks test take a long time
* Merge [Revision #2000a9009b](https://github.com/MariaDB/server/commit/2000a9009b) 2017-08-31 11:14:28 +0300 - Merge 10.1 into 10.2
* Merge [Revision #2f20be946f](https://github.com/MariaDB/server/commit/2f20be946f) 2017-08-31 09:35:39 +0300 - Merge 10.1 into 10.2
* [Revision #4386ee8ccc](https://github.com/MariaDB/server/commit/4386ee8ccc)\
  2017-08-31 08:20:29 +0300
  * Add ATTRIBUTE\_NORETURN and ATTRIBUTE\_COLD
* [Revision #03a8eaa072](https://github.com/MariaDB/server/commit/03a8eaa072)\
  2017-08-31 08:20:43 +0300
  * Fix some badly written Galera tests
* Merge [Revision #a36c369bda](https://github.com/MariaDB/server/commit/a36c369bda) 2017-08-31 09:28:59 +0300 - Merge 10.1 into 10.2
* [Revision #eca238aea7](https://github.com/MariaDB/server/commit/eca238aea7)\
  2017-08-29 14:23:34 +0300
  * [MDEV-13557](https://jira.mariadb.org/browse/MDEV-13557): Startup failure, unable to decrypt ibdata1
* [Revision #43b262af55](https://github.com/MariaDB/server/commit/43b262af55)\
  2017-08-28 16:10:25 +0000
  * One more attempt to fix dependencies with mysqld import/export libraries with Visual Studio
* [Revision #49f3fb8feb](https://github.com/MariaDB/server/commit/49f3fb8feb)\
  2017-08-29 14:54:04 +0000
  * small refactoring o innobase/CMakeLists.txt
* [Revision #91826970c5](https://github.com/MariaDB/server/commit/91826970c5)\
  2017-08-30 14:37:16 +0000
  * Fix threadpool to report connections aborted due to wait timeout.
* [Revision #d20fa48599](https://github.com/MariaDB/server/commit/d20fa48599)\
  2017-08-30 11:45:24 +0300
  * [MDEV-13669](https://jira.mariadb.org/browse/MDEV-13669): Some MyRocks test take a long time
* [Revision #acaac7c233](https://github.com/MariaDB/server/commit/acaac7c233)\
  2017-08-22 15:56:53 +1000
  * submodules.cmake: git returns 128 if not in a repository
* Merge [Revision #f192b48d62](https://github.com/MariaDB/server/commit/f192b48d62) 2017-08-29 10:07:33 +0300 - Merge 10.1 into 10.2
* [Revision #71931fdf83](https://github.com/MariaDB/server/commit/71931fdf83)\
  2017-08-28 19:41:13 +0300
  * Fix results for parts/repair\_table test after enabling it for MyISAM
* [Revision #309fe35f29](https://github.com/MariaDB/server/commit/309fe35f29)\
  2017-08-28 13:46:31 +0300
  * Correct a mtr.add\_suppression() expression
* [Revision #f87cb652ac](https://github.com/MariaDB/server/commit/f87cb652ac)\
  2017-08-28 08:57:51 +0300
  * [MDEV-13637](https://jira.mariadb.org/browse/MDEV-13637) InnoDB change buffer housekeeping can cause redo log overrun and possibly deadlocks
* [Revision #a544225d0a](https://github.com/MariaDB/server/commit/a544225d0a)\
  2017-08-24 12:51:05 +0530
  * Update README.md
* [Revision #e7bf8bca2f](https://github.com/MariaDB/server/commit/e7bf8bca2f)\
  2017-08-24 10:13:07 +0300
  * [MDEV-13534](https://jira.mariadb.org/browse/MDEV-13534) InnoDB STATS\_PERSISTENT fails to ignore garbage delete-mark flag on node pointer pages
* [Revision #ae0759ad45](https://github.com/MariaDB/server/commit/ae0759ad45)\
  2017-08-23 18:40:47 +0300
  * [MDEV-13602](https://jira.mariadb.org/browse/MDEV-13602): rocksdb.index\_merge\_rocksdb2 failed in buildbot
* [Revision #06b4b99f3e](https://github.com/MariaDB/server/commit/06b4b99f3e)\
  2017-08-23 14:40:23 +0300
  * The test failed once on Buildbot with the result difference:
* [Revision #81bd81fbe8](https://github.com/MariaDB/server/commit/81bd81fbe8)\
  2017-08-23 11:35:34 +0300
  * Adjust InnoDB debug assertions for Oracle Bug#25551311 aka Bug#23517560
* [Revision #36a971724e](https://github.com/MariaDB/server/commit/36a971724e)\
  2017-08-23 10:01:48 +0300
  * [MDEV-13167](https://jira.mariadb.org/browse/MDEV-13167) InnoDB key rotation is not skipping unused pages
* [Revision #e52dd13c2e](https://github.com/MariaDB/server/commit/e52dd13c2e)\
  2017-08-23 09:47:50 +0300
  * Code clean-up related to [MDEV-13167](https://jira.mariadb.org/browse/MDEV-13167)
* [Revision #59caf2c3c1](https://github.com/MariaDB/server/commit/59caf2c3c1)\
  2017-08-21 18:56:46 +0300
  * [MDEV-13485](https://jira.mariadb.org/browse/MDEV-13485) MTR tests fail massively with --innodb-sync-debug
* [Revision #1621d32eac](https://github.com/MariaDB/server/commit/1621d32eac)\
  2017-08-22 14:56:17 +0300
  * Remove the unused redo log record type MLOG\_INIT\_FILE\_PAGE
* [Revision #825b6a354a](https://github.com/MariaDB/server/commit/825b6a354a)\
  2017-08-23 08:05:50 +0300
  * [MDEV-13452](https://jira.mariadb.org/browse/MDEV-13452) Assertion \`!recv\_no\_log\_write' failed at startup
* [Revision #ef8e1a35cc](https://github.com/MariaDB/server/commit/ef8e1a35cc)\
  2017-08-21 16:12:09 +0300
  * Fix rocksdb.bulk\_load test
* [Revision #4f34ec26fa](https://github.com/MariaDB/server/commit/4f34ec26fa)\
  2017-08-21 15:26:21 +0300
  * [MDEV-13600](https://jira.mariadb.org/browse/MDEV-13600): Update test results for rocksdb.bulk\_load\_rev\_cf
* [Revision #86fc5ece26](https://github.com/MariaDB/server/commit/86fc5ece26)\
  2017-08-18 15:01:32 +0300
  * [MDEV-13559](https://jira.mariadb.org/browse/MDEV-13559) encryption.innodb-redo-badkey failed in buildbot
* [Revision #8a9e9d896e](https://github.com/MariaDB/server/commit/8a9e9d896e)\
  2017-08-18 14:42:53 +0300
  * [MDEV-13570](https://jira.mariadb.org/browse/MDEV-13570) Assertion failure !srv\_read\_only\_mode in --innodb-read-only shutdown when buf\_resize\_thread is active
* [Revision #8a3e2970ad](https://github.com/MariaDB/server/commit/8a3e2970ad)\
  2017-08-18 14:42:18 +0300
  * [MDEV-13575](https://jira.mariadb.org/browse/MDEV-13575) On failure, mariadb-backup --backup --safe-slave-backup may forget to START SLAVE SQL\_THREAD
* [Revision #72ac85cdda](https://github.com/MariaDB/server/commit/72ac85cdda)\
  2017-08-18 12:51:28 -0400
  * bump the VERSION
* [Revision #605b835220](https://github.com/MariaDB/server/commit/605b835220)\
  2017-08-18 10:07:11 +0300
  * [MDEV-13754](https://jira.mariadb.org/browse/MDEV-13754) Memory leak in mariadb-backup.incremental\_backup
* [Revision #74ce0cf148](https://github.com/MariaDB/server/commit/74ce0cf148)\
  2017-08-18 10:00:56 +0300
  * [MDEV-13574](https://jira.mariadb.org/browse/MDEV-13574) related mariadb-backup code cleanup (non-functional change)
* [Revision #e9e051d297](https://github.com/MariaDB/server/commit/e9e051d297)\
  2017-08-18 08:52:41 +0300
  * Follow-up fix to [MDEV-12988](https://jira.mariadb.org/browse/MDEV-12988) backup fails if innodb\_undo\_tablespaces>0
* [Revision #f269915381](https://github.com/MariaDB/server/commit/f269915381)\
  2017-08-18 02:51:30 +0300
  * Updated list of unstable tests for 10.2.8
* [Revision #bcd5622ebb](https://github.com/MariaDB/server/commit/bcd5622ebb)\
  2017-08-18 02:48:43 +0300
  * gcol.gcol\_rollback could fail with errors in server log
* [Revision #edf77043ba](https://github.com/MariaDB/server/commit/edf77043ba)\
  2017-08-17 15:07:44 +0000
  * [MDEV-12948](https://jira.mariadb.org/browse/MDEV-12948) : do not spam error log, if DeviceIoControl(IOCTL\_STORAGE\_QUERY\_PROPERTY) fails with ERROR\_INVALID\_FUNCTION
* [Revision #e6971011c3](https://github.com/MariaDB/server/commit/e6971011c3)\
  2017-08-17 15:38:41 +0300
  * [MDEV-12988](https://jira.mariadb.org/browse/MDEV-12988) backup fails if innodb\_undo\_tablespaces>0

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
