# MariaDB 10.0.31 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.31)[Release Notes](../../old-releases/10.0/10.0.31.md)[Changelog](mariadb-10031-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 23 May 2017

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.31.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Merge [Revision #725e47bfb5](https://github.com/MariaDB/server/commit/725e47bfb5) 2017-05-20 00:59:40 +0200 - Merge branch '5.5' into 10.0
* [Revision #7d57ba6e28](https://github.com/MariaDB/server/commit/7d57ba6e28)\
  2017-05-19 13:02:45 +0530
  * [MDEV-11092](https://jira.mariadb.org/browse/MDEV-11092) :- Fix Previous commit of [MDEV-11092](https://jira.mariadb.org/browse/MDEV-11092)
* [Revision #4a846e018d](https://github.com/MariaDB/server/commit/4a846e018d)\
  2017-05-18 19:31:44 +0200
  * Make IF clear.
* [Revision #b5cdf01404](https://github.com/MariaDB/server/commit/b5cdf01404)\
  2017-05-18 17:13:37 +0530
  * [MDEV-11092](https://jira.mariadb.org/browse/MDEV-11092) Assertion \`!writer.checksum\_len || writer.remains == 0' failed
* [Revision #efb9f2617b](https://github.com/MariaDB/server/commit/efb9f2617b)\
  2017-05-17 16:16:54 -0700
  * Fixed the bug [MDEV-12812](https://jira.mariadb.org/browse/MDEV-12812).
* [Revision #7e97163102](https://github.com/MariaDB/server/commit/7e97163102)\
  2017-05-17 14:29:13 -0700
  * Fixed the bug [MDEV-12817](https://jira.mariadb.org/browse/MDEV-12817)/[MDEV-12820](https://jira.mariadb.org/browse/MDEV-12820).
* [Revision #eb30230359](https://github.com/MariaDB/server/commit/eb30230359)\
  2017-05-19 22:27:26 +0200
  * compilation warnings in Connect
* [Revision #6dcc378964](https://github.com/MariaDB/server/commit/6dcc378964)\
  2017-05-18 15:22:45 +0200
  * [MDEV-10788](https://jira.mariadb.org/browse/MDEV-10788) Not able to compile source with -DBUILD\_CONFIG=mysql\_release -DCMAKE\_BUILD\_TYPE=Debug
* [Revision #7c03edf2fe](https://github.com/MariaDB/server/commit/7c03edf2fe)\
  2017-05-17 15:16:24 +0200
  * [MDEV-6262](https://jira.mariadb.org/browse/MDEV-6262) analyze the coverity report on mariadb
* [Revision #335c4ab790](https://github.com/MariaDB/server/commit/335c4ab790)\
  2017-05-19 09:51:44 +0300
  * Remove dead code added in merge commit d8b45b0c004edc0b91029b232d7cc9aad02cc822
* [Revision #546a89ca58](https://github.com/MariaDB/server/commit/546a89ca58)\
  2017-05-18 16:16:18 +0300
  * Update xtradb and innodb version to 5.6.36
* [Revision #3c7af6c490](https://github.com/MariaDB/server/commit/3c7af6c490)\
  2017-05-18 15:46:31 +0300
  * Fix xtradb handler compilation post merge
* Merge [Revision #45898c2092](https://github.com/MariaDB/server/commit/45898c2092) 2017-05-18 15:45:55 +0300 - Merge remote-tracking branch 'origin/10.0' into 10.0
* [Revision #648d866150](https://github.com/MariaDB/server/commit/648d866150)\
  2017-05-18 12:24:44 +0200
  * Fixed typo in the case operator.
* [Revision #bc622fb280](https://github.com/MariaDB/server/commit/bc622fb280)\
  2017-05-18 10:47:16 +0300
  * List of unstable tests for 10.0.31 release
* [Revision #54bb04f7ef](https://github.com/MariaDB/server/commit/54bb04f7ef)\
  2017-05-17 16:39:57 +0300
  * Fix some attribute((nonnull)) misuse
* [Revision #a436e349df](https://github.com/MariaDB/server/commit/a436e349df)\
  2017-05-17 16:37:33 +0300
  * ibuf\_get\_volume\_buffered\_hash(): Use a proper type cast
* [Revision #9f57e595b4](https://github.com/MariaDB/server/commit/9f57e595b4)\
  2017-05-17 16:14:41 +0300
  * Refactor trx\_undo\_report\_row\_operation()
* [Revision #8b34aabf86](https://github.com/MariaDB/server/commit/8b34aabf86)\
  2017-05-17 16:09:29 +0300
  * Follow-up to [MDEV-12534](https://jira.mariadb.org/browse/MDEV-12534): Align srv\_sys
* [Revision #9f89b94ba6](https://github.com/MariaDB/server/commit/9f89b94ba6)\
  2017-05-17 14:08:08 +0300
  * [MDEV-12358](https://jira.mariadb.org/browse/MDEV-12358) Work around what looks like a bug in GCC 7.1.0
* [Revision #e22d86a3eb](https://github.com/MariaDB/server/commit/e22d86a3eb)\
  2017-05-17 13:49:51 +0300
  * fil\_create\_new\_single\_table\_tablespace(): Correct a bogus nonnull attribute
* [Revision #956d2540c4](https://github.com/MariaDB/server/commit/956d2540c4)\
  2017-05-17 10:27:01 +0300
  * Remove redundant UT\_LIST\_INIT() calls
* [Revision #4754f88cff](https://github.com/MariaDB/server/commit/4754f88cff)\
  2017-05-16 17:45:22 +0300
  * Never pass NULL to innobase\_get\_stmt()
* [Revision #7972da8aa1](https://github.com/MariaDB/server/commit/7972da8aa1)\
  2017-05-16 20:08:47 +0300
  * Silence bogus GCC 7 warnings -Wimplicit-fallthrough
* [Revision #492c1e4145](https://github.com/MariaDB/server/commit/492c1e4145)\
  2017-05-16 18:33:51 +0300
  * Fix an incorrect debug assertion
* [Revision #b8187fd005](https://github.com/MariaDB/server/commit/b8187fd005)\
  2017-05-16 17:47:04 +0300
  * [MDEV-12071](https://jira.mariadb.org/browse/MDEV-12071) storage/xtradb/handler/ha\_innodb.cc: Cannot assign const\_iterator to iterator
* [Revision #e63e2fe206](https://github.com/MariaDB/server/commit/e63e2fe206)\
  2017-05-16 17:40:52 +0300
  * Fix warnings in innochecksum compilation
* [Revision #8e1056bce0](https://github.com/MariaDB/server/commit/8e1056bce0)\
  2017-05-16 13:14:03 +0200
  * [MDEV-12216](https://jira.mariadb.org/browse/MDEV-12216) main.mysqld--help 'unix' test is failing when profiling support is not present
* [Revision #314f32c8c2](https://github.com/MariaDB/server/commit/314f32c8c2)\
  2017-05-16 12:42:53 +0200
  * [MDEV-5477](https://jira.mariadb.org/browse/MDEV-5477) sphinxSE GROUP BY on multiple attributes
* [Revision #0e3ca225ad](https://github.com/MariaDB/server/commit/0e3ca225ad)\
  2017-05-17 22:09:58 +0300
  * Change lower\_case\_file\_system definition to feature MYSQL\_PLUGIN\_IMPORT
* [Revision #8b0db08f36](https://github.com/MariaDB/server/commit/8b0db08f36)\
  2017-05-17 18:39:25 +0300
  * Fix windows compilation in xtradb post-merge
* [Revision #3670d167a6](https://github.com/MariaDB/server/commit/3670d167a6)\
  2017-05-17 16:19:01 +0300
  * Fix tokudb test failures post merge
* [Revision #5fe55b1b02](https://github.com/MariaDB/server/commit/5fe55b1b02)\
  2017-05-17 15:44:11 +0300
  * Fix sys\_vars innodb\_empty\_free\_list\_algorithm\_basic
* Merge [Revision #339a290d22](https://github.com/MariaDB/server/commit/339a290d22) 2017-05-17 15:42:36 +0300 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #934b831281](https://github.com/MariaDB/server/commit/934b831281)\
  2017-05-16 08:24:42 -0700
  * Fixed the bug [MDEV-7791](https://jira.mariadb.org/browse/MDEV-7791).
* [Revision #2e1428c0b5](https://github.com/MariaDB/server/commit/2e1428c0b5)\
  2017-05-15 13:33:59 +0200
  * [MDEV-12799](https://jira.mariadb.org/browse/MDEV-12799) Buffer overflow
* [Revision #e0352fb079](https://github.com/MariaDB/server/commit/e0352fb079)\
  2017-05-15 09:51:01 -0700
  * Fixed the bug [MDEV-7599](https://jira.mariadb.org/browse/MDEV-7599).
* [Revision #9495e018fb](https://github.com/MariaDB/server/commit/9495e018fb)\
  2017-05-12 11:09:27 +0530
  * [MDEV-11718](https://jira.mariadb.org/browse/MDEV-11718) Post-fix
* [Revision #6b97fe067d](https://github.com/MariaDB/server/commit/6b97fe067d)\
  2017-05-09 00:41:45 -0700
  * Fixed the bugs [MDEV-12670](https://jira.mariadb.org/browse/MDEV-12670) and [MDEV-12675](https://jira.mariadb.org/browse/MDEV-12675).
* Merge [Revision #b87873b221](https://github.com/MariaDB/server/commit/b87873b221) 2017-05-17 14:53:28 +0300 - Merge branch 'merge-innodb-5.6' into bb-10.0-vicentiu
* [Revision #0af9818240](https://github.com/MariaDB/server/commit/0af9818240)\
  2017-05-15 17:17:16 +0300
  * 5.6.36
* [Revision #5064623ce4](https://github.com/MariaDB/server/commit/5064623ce4)\
  2017-05-17 12:13:09 +0300
  * Revert "Fix unit test after merge from mysql 5.5.35 perfschema"
* Merge [Revision #d8b45b0c00](https://github.com/MariaDB/server/commit/d8b45b0c00) 2017-05-17 12:11:12 +0300 - Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #360a4a0372](https://github.com/MariaDB/server/commit/360a4a0372)\
  2017-05-16 14:16:11 +0300
  * 5.6.36-82.0
* [Revision #dfeff40706](https://github.com/MariaDB/server/commit/dfeff40706)\
  2017-05-16 17:22:44 +0300
  * Remove tokudb\_dir\_cmd variable
* Merge [Revision #4cdae9c12b](https://github.com/MariaDB/server/commit/4cdae9c12b) 2017-05-16 16:27:50 +0300 - Merge branch 'merge-tokudb-5.6' into 10.0
* [Revision #97c53cdfcc](https://github.com/MariaDB/server/commit/97c53cdfcc)\
  2017-05-16 14:26:11 +0300
  * 5.6.36-82.0
* [Revision #c1b3aaa24e](https://github.com/MariaDB/server/commit/c1b3aaa24e)\
  2017-05-16 14:28:19 +0300
  * Update perfschema version to 5.6.36 post-merge
* Merge [Revision #a111642d32](https://github.com/MariaDB/server/commit/a111642d32) 2017-05-16 14:11:39 +0300 - Merge remote-tracking branch 'connect/10.0' into 10.0
* [Revision #fd0335686b](https://github.com/MariaDB/server/commit/fd0335686b)\
  2017-05-12 11:35:57 +0200
  * [MDEV-12651](https://jira.mariadb.org/browse/MDEV-12651): change error code to ER\_ILLEGAL\_HA in rnd\_pos (ha\_connect.cc)
* [Revision #436070c6e1](https://github.com/MariaDB/server/commit/436070c6e1)\
  2017-05-12 00:33:33 +0200
  * Fix failing test connect.json for [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) Suppressing Uri and dsn from json tables (was MGO) modified: storage/connect/ha\_connect.cc modified: storage/connect/tabdos.cpp modified: storage/connect/tabjson.cpp modified: storage/connect/tabjson.h
* [Revision #1c88b9a8d3](https://github.com/MariaDB/server/commit/1c88b9a8d3)\
  2017-05-11 21:57:21 +0200
  * Fix wrong value of JSON column When null and the column is NOT NULL the value was not reset. modified: storage/connect/tabjson.cpp
* [Revision #531698e0da](https://github.com/MariaDB/server/commit/531698e0da)\
  2017-05-06 00:08:20 +0200
  * Fix [MDEV-12603](https://jira.mariadb.org/browse/MDEV-12603) Insert replaces values in ZIP file modified: storage/connect/filamzip.cpp modified: storage/connect/filamzip.h
* [Revision #a2af3c0d44](https://github.com/MariaDB/server/commit/a2af3c0d44)\
  2017-05-04 18:51:19 +0200
  * Fix [MDEV-12653](https://jira.mariadb.org/browse/MDEV-12653) Cannot add index for ZIP CONNECT table modified: storage/connect/filamzip.cpp modified: storage/connect/ha\_connect.cc modified: storage/connect/tabdos.cpp modified: storage/connect/tabfmt.cpp modified: storage/connect/tabjson.cpp modified: storage/connect/xindex.cpp
* [Revision #6525dc6336](https://github.com/MariaDB/server/commit/6525dc6336)\
  2017-05-03 12:05:05 +0200
  * Disable json tests
* [Revision #1de6440a2e](https://github.com/MariaDB/server/commit/1de6440a2e)\
  2017-05-03 10:32:01 +0200
  * Fix [MDEV-12587](https://jira.mariadb.org/browse/MDEV-12587) MariaDB CONNECT DIR Type - Subfolder Option: SELECT Query Never Ends modified: storage/connect/tabmul.cpp modified: storage/connect/tabmul.h
* [Revision #63b7d9d158](https://github.com/MariaDB/server/commit/63b7d9d158)\
  2017-04-29 19:20:51 +0200
  * Fix [MDEV-12631](https://jira.mariadb.org/browse/MDEV-12631) valgrind warning for zipped tables modified: storage/connect/filamzip.cpp
* [Revision #a091314d27](https://github.com/MariaDB/server/commit/a091314d27)\
  2017-04-22 14:14:11 +0200
  * Fix [MDEV-12520](https://jira.mariadb.org/browse/MDEV-12520): Decimal values can be truncated for JDBC tables modified: storage/connect/jdbconn.cpp
* [Revision #3ac35bb059](https://github.com/MariaDB/server/commit/3ac35bb059)\
  2017-03-28 10:25:21 +0200
  * Fix crash when a line is not ended by \n. modified: storage/connect/filamap.cpp
* [Revision #5de5daa74e](https://github.com/MariaDB/server/commit/5de5daa74e)\
  2017-03-18 12:49:14 +0100
  * Fix [MDEV-12220](https://jira.mariadb.org/browse/MDEV-12220): Crash when doing UPDATE or DELETE on an external table (ODBC, JDBC, MYSQL) with a WHERE clause on an indexed column. Also fix a bugs in TDBEXT::MakeCommand (use of uninitialised Quote) Add in this function the eventual Schema (database) prefixing. modified: storage/connect/connect.cc modified: storage/connect/tabext.cpp
* [Revision #5bc538dd85](https://github.com/MariaDB/server/commit/5bc538dd85)\
  2017-03-11 19:35:03 +0100
  * Commit the 2 last commits merged from 10.1
* [Revision #92d283c026](https://github.com/MariaDB/server/commit/92d283c026)\
  2017-03-06 17:23:56 +0100
  * Fix [MDEV-12142](https://jira.mariadb.org/browse/MDEV-12142) crash when creating CSV table Was an unprepared longjmp (now throw) Also fix a wrong calculation of To\_Line sometimes causing a crash because of buffer overflow. modified: storage/connect/tabdos.cpp
* Merge [Revision #f1861297f0](https://github.com/MariaDB/server/commit/f1861297f0) 2017-05-16 14:07:50 +0300 - Merge branch 'merge-perfschema-5.6' into 10.0
* [Revision #24ff179311](https://github.com/MariaDB/server/commit/24ff179311)\
  2017-05-16 13:53:15 +0300
  * 5.6.36
* [Revision #a3cf69e2e5](https://github.com/MariaDB/server/commit/a3cf69e2e5)\
  2017-05-13 13:52:58 +0200
  * [MDEV-10936](https://jira.mariadb.org/browse/MDEV-10936) CONNECT engine JDBC type can't find JdbcInterface
* [Revision #a8773ef380](https://github.com/MariaDB/server/commit/a8773ef380)\
  2017-05-13 13:00:18 +0200
  * [MDEV-12660](https://jira.mariadb.org/browse/MDEV-12660) inconsistent mysql\_stmt\_close
* [Revision #a65623b3eb](https://github.com/MariaDB/server/commit/a65623b3eb)\
  2017-05-12 16:52:09 +0200
  * [MDEV-11883](https://jira.mariadb.org/browse/MDEV-11883) MariaDB crashes with out-of-memory when query information\_schema
* [Revision #71b4503242](https://github.com/MariaDB/server/commit/71b4503242)\
  2017-05-12 15:10:17 +0200
  * [MDEV-9998](https://jira.mariadb.org/browse/MDEV-9998) Fix issues caught by Clang's -Wpointer-bool-conversion warning
* [Revision #f9264280d6](https://github.com/MariaDB/server/commit/f9264280d6)\
  2017-05-12 14:27:49 +0200
  * [MDEV-12761](https://jira.mariadb.org/browse/MDEV-12761) Error return from external\_lock make the server crash
* [Revision #52aa200919](https://github.com/MariaDB/server/commit/52aa200919)\
  2017-05-11 19:48:42 +0200
  * [MDEV-12420](https://jira.mariadb.org/browse/MDEV-12420) max\_recursive\_iterations did not prevent a stack-overflow and segfault
* [Revision #602b5e4c49](https://github.com/MariaDB/server/commit/602b5e4c49)\
  2017-04-18 17:20:34 +1000
  * WIP: global readonly variable pcre\_frame\_size
* [Revision #b30311e52a](https://github.com/MariaDB/server/commit/b30311e52a)\
  2017-04-09 13:30:59 +1000
  * [MDEV-12420](https://jira.mariadb.org/browse/MDEV-12420): pcre recursion overflow test case
* [Revision #fbc057ad36](https://github.com/MariaDB/server/commit/fbc057ad36)\
  2017-04-09 12:54:33 +1000
  * [MDEV-12420](https://jira.mariadb.org/browse/MDEV-12420): add full list of pcre error messages
* [Revision #d672f88ef7](https://github.com/MariaDB/server/commit/d672f88ef7)\
  2017-04-08 22:47:56 +1000
  * [MDEV-12420](https://jira.mariadb.org/browse/MDEV-12420): PCRE stack overflow
* [Revision #217b8115c8](https://github.com/MariaDB/server/commit/217b8115c8)\
  2017-05-15 12:02:19 +0300
  * [MDEV-12188](https://jira.mariadb.org/browse/MDEV-12188) information schema - errors populating fail to free memory, unlock mutexes
* [Revision #8417252b04](https://github.com/MariaDB/server/commit/8417252b04)\
  2017-05-15 10:26:42 +0300
  * Fix the Solaris compilation after [MDEV-12674](https://jira.mariadb.org/browse/MDEV-12674)
* [Revision #ff16609374](https://github.com/MariaDB/server/commit/ff16609374)\
  2017-05-11 21:12:37 +0300
  * [MDEV-12674](https://jira.mariadb.org/browse/MDEV-12674) Innodb\_row\_lock\_current\_waits has overflow
* Merge [Revision #1c418df722](https://github.com/MariaDB/server/commit/1c418df722) 2017-05-08 12:12:48 +0200 - Merge branch '5.5' into 10.0
* [Revision #15f9931f6d](https://github.com/MariaDB/server/commit/15f9931f6d)\
  2017-05-04 22:45:32 -0700
  * Fixed the bug [MDEV-12673](https://jira.mariadb.org/browse/MDEV-12673).
* [Revision #14fca28ea4](https://github.com/MariaDB/server/commit/14fca28ea4)\
  2017-05-02 19:11:21 -0400
  * bump the VERSION
* [Revision #dbe2c3c5f2](https://github.com/MariaDB/server/commit/dbe2c3c5f2)\
  2017-04-30 13:29:56 +1000
  * mysqld\_safe\_help - remove warning
* [Revision #fc25437aff](https://github.com/MariaDB/server/commit/fc25437aff)\
  2017-05-05 13:08:23 +0300
  * [MDEV-10104](https://jira.mariadb.org/browse/MDEV-10104) Table lock race condition with replication
* [Revision #e3521ab904](https://github.com/MariaDB/server/commit/e3521ab904)\
  2017-05-05 13:03:41 +0300
  * Fixed some bugs in fork\_big.pl which caused some tests to die early
* [Revision #bc5c1d9970](https://github.com/MariaDB/server/commit/bc5c1d9970)\
  2017-05-05 14:04:18 +0300
  * [MDEV-12635](https://jira.mariadb.org/browse/MDEV-12635) innodb.log\_file\_size fails when run with Valgrind
* [Revision #a7c5fd6b4e](https://github.com/MariaDB/server/commit/a7c5fd6b4e)\
  2017-05-03 15:49:19 +0200
  * restore dependencies, removed in f2dc04abea
* Merge [Revision #49552cf1f7](https://github.com/MariaDB/server/commit/49552cf1f7) 2017-04-25 16:30:39 +0200 - Merge branch '5.5' into bb-10.0-merge-5.5
* [Revision #2e7ba70a94](https://github.com/MariaDB/server/commit/2e7ba70a94)\
  2017-04-22 10:30:55 -0700
  * Fixed the bug [MDEV-10693](https://jira.mariadb.org/browse/MDEV-10693).
* [Revision #57fea99eeb](https://github.com/MariaDB/server/commit/57fea99eeb)\
  2017-04-24 16:42:35 +0300
  * Add and adjust a test from MySQL:
* [Revision #864548c4ec](https://github.com/MariaDB/server/commit/864548c4ec)\
  2017-04-24 13:40:36 +0300
  * Add and adjust a test from MySQL:
* [Revision #fac2a7a85d](https://github.com/MariaDB/server/commit/fac2a7a85d)\
  2017-04-22 22:51:43 +0400
  * [MDEV-12495](https://jira.mariadb.org/browse/MDEV-12495) Conditional jump depends on uninitialised value for: SELECT NULL UNION geom\_expression
* [Revision #97fb1f2679](https://github.com/MariaDB/server/commit/97fb1f2679)\
  2017-04-21 14:34:24 -0700
  * Fixed bug [MDEV-10053](https://jira.mariadb.org/browse/MDEV-10053).
* [Revision #26ed68dcae](https://github.com/MariaDB/server/commit/26ed68dcae)\
  2017-04-18 16:28:14 +0200
  * fix "cmake -DWITH\_PCRE=bundled"
* Merge [Revision #8d75a7533e](https://github.com/MariaDB/server/commit/8d75a7533e) 2017-04-21 18:34:06 +0200 - Merge branch '5.5' into 10.0
* [Revision #c6ee3fe9d4](https://github.com/MariaDB/server/commit/c6ee3fe9d4)\
  2017-04-19 20:31:05 +0200
  * respect client's desire to force ssl even when WITH\_SSL=NO
* [Revision #4fe65ca33a](https://github.com/MariaDB/server/commit/4fe65ca33a)\
  2017-04-18 12:35:05 +0200
  * [MDEV-12230](https://jira.mariadb.org/browse/MDEV-12230) include/my\_sys.h:600:43: error: unknown type name ‘PSI\_file\_key’" when -DWITHOUT\_SERVER=1
* [Revision #0001049be0](https://github.com/MariaDB/server/commit/0001049be0)\
  2017-04-18 11:36:11 +0200
  * [MDEV-12276](https://jira.mariadb.org/browse/MDEV-12276) Missing DBUG\_RETURN or DBUG\_VOID\_RETURN macro in function "do\_exec"
* [Revision #036b689f18](https://github.com/MariaDB/server/commit/036b689f18)\
  2017-04-18 11:29:02 +0200
  * [MDEV-12310](https://jira.mariadb.org/browse/MDEV-12310) openat(, ...O\_EXEC) fails on Illumos / Solaris
* [Revision #786363e89b](https://github.com/MariaDB/server/commit/786363e89b)\
  2017-04-18 10:29:59 +0200
  * compiler warning
* [Revision #39f1917f46](https://github.com/MariaDB/server/commit/39f1917f46)\
  2016-09-10 20:42:20 +0200
  * Attempt to fix strange rpm dependency issue following prior patch
* [Revision #d185f1d68b](https://github.com/MariaDB/server/commit/d185f1d68b)\
  2017-04-19 14:30:52 +0200
  * Fix use of `require` in mysql-test-run.
* [Revision #d53b541389](https://github.com/MariaDB/server/commit/d53b541389)\
  2017-04-13 09:35:57 -0400
  * bump the VERSION
* Merge [Revision #663068c6ee](https://github.com/MariaDB/server/commit/663068c6ee) 2017-04-11 10:18:04 -0400 - Merge remote-tracking branch 'mysql/5.5' into 5.5
* [Revision #5c579482eb](https://github.com/MariaDB/server/commit/5c579482eb)\
  2017-04-07 16:25:02 -0700
  * Adjusted test results after the fix for [MDEV-12429](https://jira.mariadb.org/browse/MDEV-12429).
* [Revision #b0395d8701](https://github.com/MariaDB/server/commit/b0395d8701)\
  2017-04-04 10:04:52 -0700
  * Fixed the bug [MDEV-12429](https://jira.mariadb.org/browse/MDEV-12429) and its duplicates [MDEV-12145](https://jira.mariadb.org/browse/MDEV-12145) and [MDEV-9886](https://jira.mariadb.org/browse/MDEV-9886).
* [Revision #e056d1f1ca](https://github.com/MariaDB/server/commit/e056d1f1ca)\
  2017-04-21 17:39:12 +0300
  * Fix some InnoDB type mismatch
* [Revision #e48ae21b0e](https://github.com/MariaDB/server/commit/e48ae21b0e)\
  2017-04-21 16:22:46 +0300
  * Follow-up to [MDEV-12534](https://jira.mariadb.org/browse/MDEV-12534): Fix warnings on 32-bit systems
* [Revision #87b6df31c4](https://github.com/MariaDB/server/commit/87b6df31c4)\
  2017-04-21 04:36:50 +0300
  * [MDEV-12488](https://jira.mariadb.org/browse/MDEV-12488) Remove type mismatch in InnoDB printf-like calls
* [Revision #d34a67b067](https://github.com/MariaDB/server/commit/d34a67b067)\
  2017-04-19 22:30:18 +0300
  * [MDEV-12534](https://jira.mariadb.org/browse/MDEV-12534) Use atomic operations whenever available
* [Revision #88613e1df6](https://github.com/MariaDB/server/commit/88613e1df6)\
  2016-12-01 09:59:58 +0100
  * [MDEV-11201](https://jira.mariadb.org/browse/MDEV-11201): gtid\_ignore\_duplicates incorrectly ignores statements when GTID replication is not enabled
* [Revision #7dd6efeaab](https://github.com/MariaDB/server/commit/7dd6efeaab)\
  2017-04-02 16:43:43 +1000
  * Don't use full path of libtool
* [Revision #57a699b0a0](https://github.com/MariaDB/server/commit/57a699b0a0)\
  2016-06-17 16:51:11 +0200
  * [MDEV-8642](https://jira.mariadb.org/browse/MDEV-8642): WHERE Clause not applied on View - Empty result set returned
* [Revision #8e36216a06](https://github.com/MariaDB/server/commit/8e36216a06)\
  2017-04-05 14:46:35 +0300
  * Import two ALTER TABLE…ALGORITHM=INPLACE tests from MySQL 5.6.
* [Revision #f2dc04abea](https://github.com/MariaDB/server/commit/f2dc04abea)\
  2017-04-03 18:48:48 +0000
  * Compiling, Windows . Avoid unnecessary rebuilds with MSVC.
* [Revision #ff6f4d7db1](https://github.com/MariaDB/server/commit/ff6f4d7db1)\
  2017-04-03 15:18:46 +0000
  * Windows : Fix compiling with VS2013
* Merge [Revision #c51fc679f5](https://github.com/MariaDB/server/commit/c51fc679f5) 2017-03-24 18:19:15 +0200 - Merge 5.5 into 10.0
* [Revision #a821ef7605](https://github.com/MariaDB/server/commit/a821ef7605)\
  2017-03-24 18:01:56 +0200
  * [MDEV-11802](https://jira.mariadb.org/browse/MDEV-11802) innodb.innodb\_bug14676111 fails on buildbot
* Merge [Revision #0d622bed4f](https://github.com/MariaDB/server/commit/0d622bed4f) 2017-03-21 11:35:50 +0100 - Merge branch '5.5' into 10.0
* [Revision #577915def8](https://github.com/MariaDB/server/commit/577915def8)\
  2017-03-20 18:53:45 +0100
  * remove COPYING.LESSER
* [Revision #8efdf89e42](https://github.com/MariaDB/server/commit/8efdf89e42)\
  2017-03-17 20:07:39 +0000
  * [MDEV-12126](https://jira.mariadb.org/browse/MDEV-12126) Correct German error message.
* [Revision #adbe1c5fe9](https://github.com/MariaDB/server/commit/adbe1c5fe9)\
  2017-03-14 17:31:29 +0530
  * [MDEV-6486](https://jira.mariadb.org/browse/MDEV-6486): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed with SELECT SQ, TEXT field
* [Revision #3990e55fef](https://github.com/MariaDB/server/commit/3990e55fef)\
  2017-03-13 23:31:03 +0000
  * Windows : Fix packaging when building with VS2017
* [Revision #c99d71a29c](https://github.com/MariaDB/server/commit/c99d71a29c)\
  2017-03-12 01:10:04 +0100
  * [MDEV-12231](https://jira.mariadb.org/browse/MDEV-12231) MariaDB fails to restart after 10.0.30-1.el7 update
* [Revision #2abc313c37](https://github.com/MariaDB/server/commit/2abc313c37)\
  2017-03-09 12:34:06 +0300
  * Use correct function name in DEBUG\_ENTER
* [Revision #65ef8ec8aa](https://github.com/MariaDB/server/commit/65ef8ec8aa)\
  2017-03-08 11:12:12 +0000
  * [MDEV-12207](https://jira.mariadb.org/browse/MDEV-12207) Include windows compatibility manifest into executable to make GetVersionEx work correctly
* [Revision #4c35dce296](https://github.com/MariaDB/server/commit/4c35dce296)\
  2017-03-18 22:50:14 +0200
  * Clean up the test mentioned in [MDEV-12052](https://jira.mariadb.org/browse/MDEV-12052).
* [Revision #8971286a3c](https://github.com/MariaDB/server/commit/8971286a3c)\
  2017-03-16 14:03:17 +0100
  * compiler warning
* [Revision #2d0c579a86](https://github.com/MariaDB/server/commit/2d0c579a86)\
  2017-03-06 16:25:01 +0200
  * Wait for slave threads to start during startup
* [Revision #e7f55fde88](https://github.com/MariaDB/server/commit/e7f55fde88)\
  2017-03-06 16:02:50 +0200
  * Removed wrong assert
* [Revision #2c2bd8c155](https://github.com/MariaDB/server/commit/2c2bd8c155)\
  2017-03-15 11:46:54 +0100
  * [MDEV-12261](https://jira.mariadb.org/browse/MDEV-12261) build failure without P\_S
* [Revision #06f1f1aa6e](https://github.com/MariaDB/server/commit/06f1f1aa6e)\
  2017-03-14 00:24:06 +0200
  * Make ELOOP be considered a File Not Found error when it comes from handlerton
* [Revision #032678ad18](https://github.com/MariaDB/server/commit/032678ad18)\
  2017-03-10 18:33:38 +0200
  * [MDEV-12091](https://jira.mariadb.org/browse/MDEV-12091) Shutdown fails to wait for rollback of recovered transactions to finish
* [Revision #1d47bd61d5](https://github.com/MariaDB/server/commit/1d47bd61d5)\
  2017-03-09 16:52:57 +0200
  * Remove leftover merge conflict marker
* [Revision #1b2b209519](https://github.com/MariaDB/server/commit/1b2b209519)\
  2017-03-09 11:28:07 +0200
  * Use correct integer format with printf-like functions.
* [Revision #8805fe0d5c](https://github.com/MariaDB/server/commit/8805fe0d5c)\
  2017-03-09 11:27:24 +0200
  * Use %pure-parser instead of the deprecated %pure\_parser.
* [Revision #2158de8865](https://github.com/MariaDB/server/commit/2158de8865)\
  2017-03-09 11:26:36 +0200
  * Remove unused variables.
* [Revision #9fe92a9770](https://github.com/MariaDB/server/commit/9fe92a9770)\
  2017-03-08 11:13:34 -0500
  * bump the VERSION
* [Revision #e1e04c3d68](https://github.com/MariaDB/server/commit/e1e04c3d68)\
  2017-03-08 14:40:02 +0200
  * Correct a merge error.
* Merge [Revision #fc0a6dd57f](https://github.com/MariaDB/server/commit/fc0a6dd57f) 2017-03-08 12:21:13 +0200 - Merge branch '5.5' into 10.0
* [Revision #f65c9f825d](https://github.com/MariaDB/server/commit/f65c9f825d)\
  2017-03-07 15:52:17 +0200
  * mysql\_client\_test\_nonblock fails when compiled with clang
* [Revision #74fe0e03d5](https://github.com/MariaDB/server/commit/74fe0e03d5)\
  2017-03-08 11:46:34 +0200
  * Remove unused declarations.
* Merge [Revision #47396ddea9](https://github.com/MariaDB/server/commit/47396ddea9) 2017-03-08 11:40:43 +0200 - Merge 5.5 into 10.0
* [Revision #6860a4b556](https://github.com/MariaDB/server/commit/6860a4b556)\
  2017-03-08 10:31:06 +0200
  * [MDEV-12206](https://jira.mariadb.org/browse/MDEV-12206) Query\_cache::send\_result\_to\_client() may corrupt THD::query\_plan\_flags
* [Revision #9c47beb8bd](https://github.com/MariaDB/server/commit/9c47beb8bd)\
  2017-03-08 10:07:50 +0200
  * [MDEV-11027](https://jira.mariadb.org/browse/MDEV-11027) InnoDB log recovery is too noisy
* [Revision #1fd3cc8c1f](https://github.com/MariaDB/server/commit/1fd3cc8c1f)\
  2017-03-08 10:06:34 +0200
  * Fix a compiler warning.
* [Revision #17a1b194e2](https://github.com/MariaDB/server/commit/17a1b194e2)\
  2017-03-08 10:03:35 +0200
  * Fix some GCC 6.3.0 warnings in MyISAM and Maria.
* [Revision #30cac41c2f](https://github.com/MariaDB/server/commit/30cac41c2f)\
  2017-03-06 23:07:59 +0400
  * [MDEV-11084](https://jira.mariadb.org/browse/MDEV-11084) server\_audit does not work with mysql\_community 5.7.16.
* [Revision #43903745e5](https://github.com/MariaDB/server/commit/43903745e5)\
  2017-03-05 10:58:05 +0530
  * [MDEV-11078](https://jira.mariadb.org/browse/MDEV-11078): NULL NOT IN (non-empty subquery) should never return results
* [Revision #6b8173b6e9](https://github.com/MariaDB/server/commit/6b8173b6e9)\
  2017-03-03 11:47:31 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520): Retry posix\_fallocate() after EINTR.
* [Revision #75f6067e89](https://github.com/MariaDB/server/commit/75f6067e89)\
  2017-02-28 17:39:28 +0100
  * [MDEV-9635](https://jira.mariadb.org/browse/MDEV-9635): Server crashes in part\_of\_refkey or assertion \`!created && key\_to\_save < (int)s->keys' failed in TABLE::use\_index(int) or with join\_cache\_level>2

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
