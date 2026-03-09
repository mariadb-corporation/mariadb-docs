# MariaDB 10.1.3 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.3)[Release Notes](../../old-releases/10.1/10.1.3.md)[Changelog](mariadb-10-1-3-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 2 Mar 2015

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.3.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #702aee6](https://github.com/MariaDB/server/commit/702aee6)\
  2015-02-25 23:56:44 +0300
  * [MDEV-6323](https://jira.mariadb.org/browse/MDEV-6323): ‘explain\_node’ may be used uninitialized in this function
* [Revision #2330107](https://github.com/MariaDB/server/commit/2330107)\
  2015-02-25 13:26:57 +0200
  * [MDEV-7572](https://jira.mariadb.org/browse/MDEV-7572): InnoDB: Assertion failure in log\_init\_crypt\_key if file\_key\_management\_plugin is used
* [Revision #da181fe](https://github.com/MariaDB/server/commit/da181fe)\
  2015-02-24 16:26:18 +0100
  * disable feedback plugin again
* [Revision #b286291](https://github.com/MariaDB/server/commit/b286291)\
  2015-02-22 08:46:22 +0200
  * Try to stabilize test case. Problem was that test compares number of encryption/compression pages and that will happen if and only if dirty pages are written to the disk.
* [Revision #1cc7bef](https://github.com/MariaDB/server/commit/1cc7bef)\
  2015-02-21 21:45:16 +0200
  * [MDEV-7109](https://jira.mariadb.org/browse/MDEV-7109): Add support for INFORMATION\_SCHEMA.INNODB\_SEMAPHORE\_WAITS [MDEV-7399](https://jira.mariadb.org/browse/MDEV-7399): Add support for INFORMATION\_SCHEMA.INNODB\_MUTEXES [MDEV-7618](https://jira.mariadb.org/browse/MDEV-7618): Improve semaphore instrumentation
* [Revision #9152b83](https://github.com/MariaDB/server/commit/9152b83)\
  2015-02-19 17:42:18 +0200
  * Merged from 10.0-FusionIO:
* [Revision #bab1c68](https://github.com/MariaDB/server/commit/bab1c68)\
  2015-02-19 12:41:10 +0200
  * Push forgotten file change to fix compiler errors.
* [Revision #36c1982](https://github.com/MariaDB/server/commit/36c1982)\
  2015-02-18 15:23:37 +0200
  * [MDEV-7604](https://jira.mariadb.org/browse/MDEV-7604): wsrep plugin lists its plugin\_maturity as Unknown
* [Revision #4040bf1](https://github.com/MariaDB/server/commit/4040bf1)\
  2015-02-18 08:29:38 +0200
  * [MDEV-7593](https://jira.mariadb.org/browse/MDEV-7593): Default encryption key does not work correctly for page encrypted tables
* [Revision #11536f9](https://github.com/MariaDB/server/commit/11536f9)\
  2015-02-16 23:18:32 +0100
  * [MDEV-7305](https://jira.mariadb.org/browse/MDEV-7305) Difficulties building cracklib\_password\_check
* [Revision #87eb82d](https://github.com/MariaDB/server/commit/87eb82d)\
  2015-02-16 23:18:00 +0100
  * cleanup: remove old debian/ubuntu names from debian/\* files
* [Revision #a0e93bc](https://github.com/MariaDB/server/commit/a0e93bc)\
  2015-02-17 23:49:02 +0100
  * innodb/xtradb: update nonnull attributes to match the new semantics
* [Revision #4da7aa5](https://github.com/MariaDB/server/commit/4da7aa5)\
  2015-02-17 18:43:22 +0300
  * Add a testcase for EXPLAIN FORMAT=JSON for ROR-union index\_merge.
* [Revision #3e2849d](https://github.com/MariaDB/server/commit/3e2849d)\
  2015-02-13 00:50:30 +0100
  * update result files
* [Revision #db22761](https://github.com/MariaDB/server/commit/db22761)\
  2015-02-12 12:26:37 +0100
  * followup for "[MDEV-6248](https://jira.mariadb.org/browse/MDEV-6248) GUI-friendly cmake options to enable/disable plugins"
* [Revision #985ef1d](https://github.com/MariaDB/server/commit/985ef1d)\
  2015-02-12 22:33:30 +0100
  * Don't link plugins with libmysys.a or libmysys\_ssl.a
* [Revision #4c9d0b2](https://github.com/MariaDB/server/commit/4c9d0b2)\
  2015-02-13 15:04:23 +0100
  * yassl builds: don't hide mysys\_ssl symbols that cannot possibly collide with openssl
* [Revision #2043e3d](https://github.com/MariaDB/server/commit/2043e3d)\
  2015-02-12 17:10:59 +0400
  * Removing the Hybrid\_type\_traits framework. It's not used since 5.5.
* [Revision #0ed60af](https://github.com/MariaDB/server/commit/0ed60af)\
  2015-02-11 19:52:43 +0200
  * Fix test failure seen on p8-rhel7
* [Revision #d72dea1](https://github.com/MariaDB/server/commit/d72dea1)\
  2015-02-10 21:08:57 +0100
  * Revert "Fixing ConnectSE compilation warnings"
* [Revision #aa61e4c](https://github.com/MariaDB/server/commit/aa61e4c)\
  2015-02-10 16:47:42 +0400
  * Fixing ConnectSE compilation warnings (and failires in maintainer mode).
* [Revision #1c80165](https://github.com/MariaDB/server/commit/1c80165)\
  2015-02-04 17:09:43 +0100
  * [MDEV-7450](https://jira.mariadb.org/browse/MDEV-7450) key management plugins don't work with yassl
* [Revision #d78a53e](https://github.com/MariaDB/server/commit/d78a53e)\
  2015-01-09 15:59:55 +0100
  * update 32-bit rdiff files in sys\_vars suite
* [Revision #093b232](https://github.com/MariaDB/server/commit/093b232)\
  2015-01-12 19:24:24 +0200
  * Do not yet allow encrypted tables with compressed tables.
* [Revision #e2e8098](https://github.com/MariaDB/server/commit/e2e8098)\
  2015-01-09 12:30:59 +0200
  * Pass down the information should we encrypt the page at os0file.cc when page compression and google encryption is used.
* [Revision #e109a66](https://github.com/MariaDB/server/commit/e109a66)\
  2015-01-09 15:12:17 +0100
  * mtr check for openssl support for AES\_CTR
* [Revision #f3da18f](https://github.com/MariaDB/server/commit/f3da18f)\
  2015-01-08 00:25:05 +0100
  * cmake-time detection for EVP\_aes\_128\_ctr()
* [Revision #faad7e0](https://github.com/MariaDB/server/commit/faad7e0)\
  2015-01-07 15:24:09 +0200
  * Add test case for combination Google encryption and page compressed tables.
* [Revision #21430e4](https://github.com/MariaDB/server/commit/21430e4)\
  2015-01-02 22:53:54 +0100
  * encryption keys service
* [Revision #cf8bf0b](https://github.com/MariaDB/server/commit/cf8bf0b)\
  2015-01-05 13:36:14 +0100
  * encryption key management plugin api
* [Revision #c8997c3](https://github.com/MariaDB/server/commit/c8997c3)\
  2015-01-05 13:27:44 +0100
  * initialize plugins in the specific order by plugin type
* [Revision #9cdf494](https://github.com/MariaDB/server/commit/9cdf494)\
  2014-12-29 21:55:20 +0200
  * Fixed XtraDB implementation of encryption and page encryption.
* [Revision #d7d589d](https://github.com/MariaDB/server/commit/d7d589d)\
  2014-12-22 16:53:17 +0200
  * Push for testing of encryption
* [Revision #3a3ec74](https://github.com/MariaDB/server/commit/3a3ec74)\
  2014-12-22 02:02:38 +0200
  * cleanups done as part of adding encryption - Fixed compiler warnings - Added include/wait\_for\_binlog\_checkpoint.inc, as suggested by JonasO - Updated 'build-tags' to work with git (Patch by Serg)
* [Revision #01963e5](https://github.com/MariaDB/server/commit/01963e5)\
  2015-01-26 21:30:34 +0100
  * fix for cmake builds on windows
* [Revision #83c0866](https://github.com/MariaDB/server/commit/83c0866)\
  2015-01-09 14:00:00 +0100
  * new read-only server variable version\_ssl\_library
* [Revision #0d676fa](https://github.com/MariaDB/server/commit/0d676fa)\
  2015-02-04 17:07:47 +0100
  * minor cleanup: ssl.cmake
* [Revision #4280b25](https://github.com/MariaDB/server/commit/4280b25)\
  2015-01-07 12:13:21 +0100
  * \--getopt-prefix-matching command-line option
* [Revision #0ce8703](https://github.com/MariaDB/server/commit/0ce8703)\
  2015-01-05 13:35:55 +0100
  * password validation plugin API: renames
* [Revision #5e17ca5](https://github.com/MariaDB/server/commit/5e17ca5)\
  2015-01-05 16:54:00 +0100
  * don't mention bzr in "make distclean" warning message
* [Revision #df37215](https://github.com/MariaDB/server/commit/df37215)\
  2015-01-05 18:18:33 +0100
  * small cleanup of my\_default.c
* [Revision #c7d9f11](https://github.com/MariaDB/server/commit/c7d9f11)\
  2015-02-10 00:45:37 +0100
  * update test results for embedded
* [Revision #4c69a6f](https://github.com/MariaDB/server/commit/4c69a6f)\
  2015-02-09 17:16:55 +0200
  * [MDEV-6918](https://jira.mariadb.org/browse/MDEV-6918) Create a way to see a user's default role.
* [Revision #bceb0b0](https://github.com/MariaDB/server/commit/bceb0b0)\
  2015-02-08 20:44:46 +0100
  * [MDEV-7151](https://jira.mariadb.org/browse/MDEV-7151) ha\_archive.so missing from .deb
* [Revision #8672339](https://github.com/MariaDB/server/commit/8672339)\
  2015-02-06 10:02:02 +0100
  * [MDEV-6676](https://jira.mariadb.org/browse/MDEV-6676): Optimistic parallel replication
* [Revision #734c4c0](https://github.com/MariaDB/server/commit/734c4c0)\
  2015-02-06 08:31:38 +0100
  * Add error handling on realpath() call.
* [Revision #2deaa29](https://github.com/MariaDB/server/commit/2deaa29)\
  2015-02-04 13:57:09 +0100
  * [MDEV-7201](https://jira.mariadb.org/browse/MDEV-7201): parallel threads resizing - potential race condition to access freed memory
* [Revision #3b267eb](https://github.com/MariaDB/server/commit/3b267eb)\
  2015-02-06 20:18:40 +0100
  * after-merge fixes for test cases
* [Revision #324cd36](https://github.com/MariaDB/server/commit/324cd36)\
  2015-02-06 18:06:46 +0100
  * disable -Werror in the maintainer mode until we're ready for it
* [Revision #2a1470a](https://github.com/MariaDB/server/commit/2a1470a)\
  2015-02-06 16:16:38 +0100
  * wsrep: check options as early as possible
* [Revision #c877610](https://github.com/MariaDB/server/commit/c877610)\
  2015-02-06 16:15:17 +0100
  * wsrep: ha\_abort\_transaction() does NOT end the transaction
* [Revision #f9448bc](https://github.com/MariaDB/server/commit/f9448bc)\
  2015-02-05 19:18:09 +0100
  * small cleanups
* [Revision #32b0b64](https://github.com/MariaDB/server/commit/32b0b64)\
  2015-02-05 13:58:30 +0400
  * [MDEV-7177](https://jira.mariadb.org/browse/MDEV-7177) - Server hangs on shutdown after InnoDB error (main.plugin\_loaderr fails in buildbot)
* [Revision #451e9b7](https://github.com/MariaDB/server/commit/451e9b7)\
  2015-02-05 13:54:55 +0400
  * [MDEV-7499](https://jira.mariadb.org/browse/MDEV-7499) - System variables have broken default values on big endian
* [Revision #b08126a](https://github.com/MariaDB/server/commit/b08126a)\
  2015-02-05 08:52:17 +0200
  * [MDEV-7178](https://jira.mariadb.org/browse/MDEV-7178): wsrep\* tests fail in buildbot
* [Revision #ad433e1](https://github.com/MariaDB/server/commit/ad433e1)\
  2015-02-05 02:44:03 +0300
  * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests
* [Revision #41dc186](https://github.com/MariaDB/server/commit/41dc186)\
  2015-02-04 19:31:16 +0200
  * [MDEV-6633](https://jira.mariadb.org/browse/MDEV-6633): Remove magic dependencies for InnoDB compression methods
* [Revision #bfe703a](https://github.com/MariaDB/server/commit/bfe703a)\
  2015-02-03 18:19:56 +0100
  * don't let current\_thd to point to a destroyed THD
* [Revision #d0fb958](https://github.com/MariaDB/server/commit/d0fb958)\
  2015-02-03 09:31:13 +0100
  * Update test results after the last push. Again.
* [Revision #d8eba59](https://github.com/MariaDB/server/commit/d8eba59)\
  2015-02-03 00:47:39 +0200
  * Commit one file that I forgot in last commit
* [Revision #80ce0c1](https://github.com/MariaDB/server/commit/80ce0c1)\
  2015-02-01 13:43:19 +0100
  * cleanup: ha\_checktype()
* [Revision #06c1690](https://github.com/MariaDB/server/commit/06c1690)\
  2015-02-02 18:02:43 +0100
  * revert test changes from "cleaned up code for setting slave\_parallel\_mode"
* [Revision #51bdfb0](https://github.com/MariaDB/server/commit/51bdfb0)\
  2015-02-02 09:04:16 +0100
  * trivial cleanup: be explicit about extern variables
* [Revision #9efd020](https://github.com/MariaDB/server/commit/9efd020)\
  2015-02-02 09:03:40 +0100
  * fix the code to compile
* [Revision #cd9e69e](https://github.com/MariaDB/server/commit/cd9e69e)\
  2015-02-01 22:39:59 +0200
  * Cleaned up code for setting slave\_parallel\_mode Now this works the same way as all other multi source variables.
* [Revision #0ee879f](https://github.com/MariaDB/server/commit/0ee879f)\
  2015-02-01 15:24:22 +0200
  * Improve performance for calculating memory allocation Extend interface for 'show variables' with current scope
* [Revision #67b24a2](https://github.com/MariaDB/server/commit/67b24a2)\
  2015-01-29 15:36:25 +0200
  * Remove some allocations not needed for internal temporary tables.
* [Revision #e787012](https://github.com/MariaDB/server/commit/e787012)\
  2015-01-29 15:35:52 +0200
  * Ignore tokudb binaries
* [Revision #b2ceedc](https://github.com/MariaDB/server/commit/b2ceedc)\
  2015-01-31 16:35:50 +0100
  * main.ctype\_ucs2 --ps: Item\_func\_nullif should use m\_args0\_copy metadata
* [Revision #f122cca](https://github.com/MariaDB/server/commit/f122cca)\
  2015-01-31 16:01:20 +0100
  * main.null --ps: Item\_null doesn't need charset converter
* [Revision #6f12cfd](https://github.com/MariaDB/server/commit/6f12cfd)\
  2015-01-31 15:14:59 +0100
  * fix semisync plugin locking: rpl.rpl\_semi\_sync\_uninstall\_plugin failed
* [Revision #863cfb3](https://github.com/MariaDB/server/commit/863cfb3)\
  2015-01-31 15:04:37 +0100
  * small cleanup, remove a useless function
* [Revision #b050354](https://github.com/MariaDB/server/commit/b050354)\
  2015-01-31 12:54:07 +0100
  * compiler warnings
* [Revision #f299da8](https://github.com/MariaDB/server/commit/f299da8)\
  2015-01-30 21:12:26 +0100
  * rpl.rpl\_parallel: after-merge fix
* [Revision #dfc7e95](https://github.com/MariaDB/server/commit/dfc7e95)\
  2015-01-30 15:53:24 +0100
  * [MDEV-7531](https://jira.mariadb.org/browse/MDEV-7531) Update 10.0.15 to 10.0.16 -> Error 2003 (HY000) can't connect to MySql server.
* [Revision #edf34f3](https://github.com/MariaDB/server/commit/edf34f3)\
  2015-01-29 22:43:07 +0100
  * [MDEV-7024](https://jira.mariadb.org/browse/MDEV-7024): Assertion \`! is\_set()' failed in Diagnostics\_area::set\_eof\_status on executing ANALYZE SELECT via PS
* [Revision #5c30901](https://github.com/MariaDB/server/commit/5c30901)\
  2015-01-29 21:10:45 +0100
  * increase the version
* [Revision #5f63c9c](https://github.com/MariaDB/server/commit/5f63c9c)\
  2015-01-29 14:34:31 +0100
  * recreate expired certificates for SSL tests
* [Revision #51feb6f](https://github.com/MariaDB/server/commit/51feb6f)\
  2015-01-29 12:47:13 +0100
  * [MDEV-7023](https://jira.mariadb.org/browse/MDEV-7023): Error 2027: Malformed packet and assertion \`field\_types == 0 || field\_types\[field\_pos] == MYSQL\_TYPE\_INT24 || field\_types\[field\_pos] == MYSQL\_TYPE\_LONG' failure in Protocol\_text::store\_long
* [Revision #1e227b8](https://github.com/MariaDB/server/commit/1e227b8)\
  2015-01-29 12:12:29 +0100
  * clarify the comment and trivial cleanups
* [Revision #9033aa0](https://github.com/MariaDB/server/commit/9033aa0)\
  2015-01-28 11:49:55 +0100
  * [MDEV-6128](https://jira.mariadb.org/browse/MDEV-6128):\[PATCH] mysqlcheck wrongly escapes '.' in table names
* [Revision #0b049b4](https://github.com/MariaDB/server/commit/0b049b4)\
  2015-01-27 15:40:50 +0200
  * Fix test failure on innodb\_stats\_fetch\_nonexistent.
* [Revision #ea229eb](https://github.com/MariaDB/server/commit/ea229eb)\
  2015-01-26 22:48:02 -0500
  * Minor test modifications.
* [Revision #e6f35f1](https://github.com/MariaDB/server/commit/e6f35f1)\
  2015-01-26 11:58:16 -0500
  * Backported changes done in wsrep\_guess\_ip() from 10.1.
* [Revision #fb71449](https://github.com/MariaDB/server/commit/fb71449)\
  2015-01-25 16:16:25 +0100
  * [MDEV-5719](https://jira.mariadb.org/browse/MDEV-5719): Wrong result with GROUP BY and LEFT OUTER JOIN
* [Revision #53b9f75](https://github.com/MariaDB/server/commit/53b9f75)\
  2015-01-24 18:46:48 -0500
  * [MDEV-7374](https://jira.mariadb.org/browse/MDEV-7374) : Losing connection to MySQL while running ALTER TABLE
* [Revision #267fc6f](https://github.com/MariaDB/server/commit/267fc6f)\
  2015-01-24 09:37:58 +0100
  * Master\_info\_index assumed that file descriptor can never be 0
* [Revision #45ff0d6](https://github.com/MariaDB/server/commit/45ff0d6)\
  2015-01-29 15:14:09 +0200
  * Ignore some tokudb executables
* [Revision #b83f692](https://github.com/MariaDB/server/commit/b83f692)\
  2015-01-29 15:12:32 +0200
  * [MDEV-6668](https://jira.mariadb.org/browse/MDEV-6668): Server crashes in check\_view\_single\_update on concurrent DDL/DML flow with views and triggers
* [Revision #d1c4ff2](https://github.com/MariaDB/server/commit/d1c4ff2)\
  2015-01-23 14:17:38 +0100
  * win32-debug build failure
* [Revision #c287873](https://github.com/MariaDB/server/commit/c287873)\
  2015-01-23 13:56:46 +0100
  * [MDEV-7352](https://jira.mariadb.org/browse/MDEV-7352): main.kill\_processlist-6619 fails sporadically in buildbot
* [Revision #cb9c116](https://github.com/MariaDB/server/commit/cb9c116)\
  2015-01-23 09:13:21 +0100
  * update tokudb version after merge
* [Revision #0105bf3](https://github.com/MariaDB/server/commit/0105bf3)\
  2015-01-22 18:00:37 -0500
  * [MDEV-7476](https://jira.mariadb.org/browse/MDEV-7476): Allow SELECT to succeed even when node is not ready
* [Revision #c23c001](https://github.com/MariaDB/server/commit/c23c001)\
  2015-01-22 16:11:03 +0100
  * [MDEV-7491](https://jira.mariadb.org/browse/MDEV-7491): Occasional test failure in innodb.group\_commit\_crash\_no\_optimize\_thread
* [Revision #f2be9c0](https://github.com/MariaDB/server/commit/f2be9c0)\
  2015-01-22 08:58:13 +0100
  * after merge. innodb/xtradb to work on Windows
* [Revision #ff55d90](https://github.com/MariaDB/server/commit/ff55d90)\
  2015-01-21 14:02:26 +0100
  * after-merge fixes
* [Revision #e576772](https://github.com/MariaDB/server/commit/e576772)\
  2015-01-20 11:26:03 +0100\
  \*
  * Last revision was to add the JSON table type. This one adds a sort on the multiple table result to obtain the same result on Windows and Linux (because files can be retrieved in a different order) modified: storage/connect/mysql-test/connect/r/json.result storage/connect/mysql-test/connect/t/json.test
* [Revision #2d2e110](https://github.com/MariaDB/server/commit/2d2e110)\
  2015-01-19 18:55:25 +0100\
  \*
  * Adding the JSON table type added: storage/connect/json.cpp storage/connect/json.h storage/connect/mysql-test/connect/r/json.result storage/connect/mysql-test/connect/std\_data/biblio.jsn storage/connect/mysql-test/connect/std\_data/expense.jsn storage/connect/mysql-test/connect/std\_data/mulexp3.jsn storage/connect/mysql-test/connect/std\_data/mulexp4.jsn storage/connect/mysql-test/connect/std\_data/mulexp5.jsn storage/connect/mysql-test/connect/t/json.test storage/connect/tabjson.cpp storage/connect/tabjson.h modified: storage/connect/CMakeLists.txt storage/connect/engmsg.h storage/connect/filamtxt.h storage/connect/ha\_connect.cc storage/connect/msgid.h storage/connect/mycat.cc storage/connect/plgdbsem.h storage/connect/tabdos.cpp storage/connect/value.cpp storage/connect/value.h
* [Revision #8bc712e](https://github.com/MariaDB/server/commit/8bc712e)\
  2015-01-19 17:31:59 +0100
  * [MDEV-6671](https://jira.mariadb.org/browse/MDEV-6671) mysql\_server\_end breaks OpenSSL
* [Revision #3212aaa](https://github.com/MariaDB/server/commit/3212aaa)\
  2015-01-19 17:18:24 +0100
  * [MDEV-6220](https://jira.mariadb.org/browse/MDEV-6220) mysqldump will not backup database with --flush-logs parameter and log\_error my.cnf parameter defined
* [Revision #a18eb83](https://github.com/MariaDB/server/commit/a18eb83)\
  2015-01-19 16:41:37 +0100
  * [MDEV-7226](https://jira.mariadb.org/browse/MDEV-7226) sql-bench test-table-elimination does not execute
* [Revision #d854a25](https://github.com/MariaDB/server/commit/d854a25)\
  2015-01-19 16:30:32 +0100
  * remove incorrect asserts in innodb/xtradb. 0 is a valid file handle value.
* [Revision #595cf63](https://github.com/MariaDB/server/commit/595cf63)\
  2015-01-19 16:29:18 +0100
  * [MDEV-7475](https://jira.mariadb.org/browse/MDEV-7475) Wrong implementation of checking PLUGIN\_VAR\_SET condition
* [Revision #5d0d6cb](https://github.com/MariaDB/server/commit/5d0d6cb)\
  2015-01-19 16:28:58 +0100
  * [MDEV-7294](https://jira.mariadb.org/browse/MDEV-7294) MTR does not use /dev/shm with a out-of-source build
* [Revision #919443f](https://github.com/MariaDB/server/commit/919443f)\
  2015-01-19 16:11:48 +0100
  * [MDEV-5679](https://jira.mariadb.org/browse/MDEV-5679) MariaDB holds stdin open after startup as mysqld
* [Revision #510ca9b](https://github.com/MariaDB/server/commit/510ca9b)\
  2015-01-19 14:32:28 +0100
  * [MDEV-7402](https://jira.mariadb.org/browse/MDEV-7402) 'reset master' hangs, waits for signalled COND\_xid\_list
* [Revision #73ebabd](https://github.com/MariaDB/server/commit/73ebabd)\
  2015-01-19 14:19:14 +0100
  * [MDEV-7299](https://jira.mariadb.org/browse/MDEV-7299) Assertion \`m\_status == DA\_ERROR || m\_status == DA\_OK' fails on concurrent execution of DDL, queries from I\_S, and KILL QUERY
* [Revision #c75eec8](https://github.com/MariaDB/server/commit/c75eec8)\
  2015-01-19 14:19:05 +0100
  * rename st\_my\_thread\_var::opt\_info -> st\_my\_thread\_var::keycache\_link
* [Revision #e2a2768](https://github.com/MariaDB/server/commit/e2a2768)\
  2015-01-19 14:18:55 +0100
  * remove unused st\_my\_thread\_var::cmp\_length
* [Revision #47c844f](https://github.com/MariaDB/server/commit/47c844f)\
  2015-01-19 14:18:44 +0100
  * [MDEV-7219](https://jira.mariadb.org/browse/MDEV-7219) SQL\_CALC\_FOUND\_ROWS yields wrong result
* [Revision #ce0ed97](https://github.com/MariaDB/server/commit/ce0ed97)\
  2015-01-19 14:18:34 +0100
  * [MDEV-7186](https://jira.mariadb.org/browse/MDEV-7186) get\_lock() crashes on Windows, main.sp\_notembedded and main.trigger\_notembedded fail in buildbot
* [Revision #1f4ebbd](https://github.com/MariaDB/server/commit/1f4ebbd)\
  2015-01-19 14:07:51 +0100
  * [MDEV-7184](https://jira.mariadb.org/browse/MDEV-7184) main.key\_cache fails in buildbot on Windows 32bit
* [Revision #56c323c](https://github.com/MariaDB/server/commit/56c323c)\
  2015-01-19 14:07:41 +0100
  * [MDEV-6728](https://jira.mariadb.org/browse/MDEV-6728) KILL QUERY executed on an idle connection can interrupt the next query
* [Revision #b4cd8a8](https://github.com/MariaDB/server/commit/b4cd8a8)\
  2015-01-19 14:07:29 +0100
  * [MDEV-7224](https://jira.mariadb.org/browse/MDEV-7224) OQGraph compile error
* [Revision #f78078a](https://github.com/MariaDB/server/commit/f78078a)\
  2015-01-19 14:07:22 +0100
  * mtr+valgrind: fix jemalloc check to work correctly for bundler and system jemalloc
* [Revision #2877c5e](https://github.com/MariaDB/server/commit/2877c5e)\
  2015-01-19 12:39:17 +0200
  * [MDEV-7477](https://jira.mariadb.org/browse/MDEV-7477): Make innochecksum work on compressed tables
* [Revision #f6e1906](https://github.com/MariaDB/server/commit/f6e1906)\
  2015-01-18 18:16:36 -0500
  * [MDEV-7470](https://jira.mariadb.org/browse/MDEV-7470): MariaDB-Galera-server uses 'tar', but 'tar' is not in the dependency list
* [Revision #67da9e8](https://github.com/MariaDB/server/commit/67da9e8)\
  2015-01-19 00:15:29 +0100
  * 5.6.22-71.0
* [Revision #05c002d](https://github.com/MariaDB/server/commit/05c002d)\
  2015-01-19 00:12:51 +0100
  * 5.6.22
* [Revision #06ae6c6](https://github.com/MariaDB/server/commit/06ae6c6)\
  2015-01-19 00:11:05 +0100
  * 5.6.22
* [Revision #7cb4a1c](https://github.com/MariaDB/server/commit/7cb4a1c)\
  2015-01-18 20:38:07 +0200
  * Fixed [MDEV-7314](https://jira.mariadb.org/browse/MDEV-7314): Deadlock when doing insert-select with Aria
* [Revision #32be7df](https://github.com/MariaDB/server/commit/32be7df)\
  2015-01-18 13:39:59 +0200
  * Return to original stage after mysql\_lock\_tables Stage "Filling schema table" is now properly shown in 'show processlist'
* [Revision #c11a054](https://github.com/MariaDB/server/commit/c11a054)\
  2015-01-18 01:54:11 +0400
  * [MDEV-7152](https://jira.mariadb.org/browse/MDEV-7152) Wrong result set for WHERE a='oe' COLLATE utf8\_german2\_ci AND a='oe' - The code that tested if WHERE expr=value AND expr=const can be rewritten to: WHERE const=value AND expr=const was incomplete in case of STRING\_RESULT. - Moving the test into a new function, to reduce duplicate code.
* [Revision #09d54b3](https://github.com/MariaDB/server/commit/09d54b3)\
  2015-01-17 16:58:10 +0000
  * [MDEV-7362](https://jira.mariadb.org/browse/MDEV-7362): ANALYZE TABLES crash with table-independent-statistics gathering
* [Revision #6e6750a](https://github.com/MariaDB/server/commit/6e6750a)\
  2015-01-17 17:52:03 +0400
  * [MDEV-7366](https://jira.mariadb.org/browse/MDEV-7366) SELECT 'a' = BINARY 'A' returns 1 (utf8 charset, utf8\_unicode\_ci collation) Fixing a wrong assymetric code in Arg\_comparator::set\_cmp\_func(). It existed for a long time, but showed up in 10.0.14 after the fix for "[MDEV-6666](https://jira.mariadb.org/browse/MDEV-6666) Malformed result for CONCAT(utf8\_column, binary\_string)".
* [Revision #252be4c](https://github.com/MariaDB/server/commit/252be4c)\
  2015-01-17 16:10:45 +0400
  * A post-fix for: [MDEV-7254](https://jira.mariadb.org/browse/MDEV-7254) Assigned expression is evaluated twice when updating column TIMESTAMP NOT NULL The test type\_timestamp failed depending on the build machine time zone. Setting a fixed time zone for the test.
* [Revision #fb3f469](https://github.com/MariaDB/server/commit/fb3f469)\
  2015-01-17 12:19:06 +0100\
  \*
  * Fix two bugs concerning Discovery of CSV tables: Sep\_char default is now ',' like when discovery is not used If data\_charset is UTF8, column names retrieved from the header are no longer converted to UTF8 considering they already are ([MDEV-7421](https://jira.mariadb.org/browse/MDEV-7421)) modified: storage/connect/ha\_connect.cc
* [Revision #f5beda4](https://github.com/MariaDB/server/commit/f5beda4)\
  2015-01-17 11:54:41 +0100\
  \*
  * Fix two bugs concerning Discovery of CSV tables: Sep\_char default is now ',' like when discovery is not used If data\_charset is UTF8, column names retrieved from the header are no longer converted to UTF8 considering they already are. modified: storage/connect/ha\_connect.cc
* [Revision #887628a](https://github.com/MariaDB/server/commit/887628a)\
  2015-01-16 13:53:23 -0500
  * Test changes (backported from 10.1).
* [Revision #3f118a7](https://github.com/MariaDB/server/commit/3f118a7)\
  2015-01-16 18:13:02 +0100
  * [MDEV-6347](https://jira.mariadb.org/browse/MDEV-6347) Build RHEL7 packages
* [Revision #2fc0b22](https://github.com/MariaDB/server/commit/2fc0b22)\
  2015-01-16 17:54:00 +0100
  * restore an incorrectly merged line
* [Revision #6164157](https://github.com/MariaDB/server/commit/6164157)\
  2015-01-16 12:00:07 +0200
  * [MDEV-7254](https://jira.mariadb.org/browse/MDEV-7254): Assigned expression is evaluated twice when updating column TIMESTAMP NOT NULL
* [Revision #813af4c](https://github.com/MariaDB/server/commit/813af4c)\
  2015-01-16 11:26:03 +0200
  * Fix try for Buildbot test failure for tests innodb\_bug12400341 innodb-mdev7046 innodb\_stats\_fetch\_nonexistent
* [Revision #26a8a95](https://github.com/MariaDB/server/commit/26a8a95)\
  2015-01-15 20:15:50 +0400
  * [MDEV-7431](https://jira.mariadb.org/browse/MDEV-7431) main.log\_tables fails sporadically in buildbot
* [Revision #df2db86](https://github.com/MariaDB/server/commit/df2db86)\
  2015-01-15 15:55:09 +0100
  * [MDEV-7430](https://jira.mariadb.org/browse/MDEV-7430): rpl.rpl\_gtid\_crash still fails in buildbot
* [Revision #ab440b0](https://github.com/MariaDB/server/commit/ab440b0)\
  2015-01-15 14:59:20 +0100
  * update sysvars\_server\_embedded,32bit.rdiff
* [Revision #90f2ec5](https://github.com/MariaDB/server/commit/90f2ec5)\
  2015-01-15 14:57:50 +0100
  * bugfix: incorrect cast causing random memory write
* [Revision #b4daf8e](https://github.com/MariaDB/server/commit/b4daf8e)\
  2015-01-15 14:41:24 +0100
  * split an assert
* [Revision #de4cfab](https://github.com/MariaDB/server/commit/de4cfab)\
  2015-01-15 08:36:13 +0100
  * sort a non-deterministic test result
* [Revision #a1e3eaf](https://github.com/MariaDB/server/commit/a1e3eaf)\
  2015-01-13 11:00:40 +0100
  * fix a duplicate macro definition
* [Revision #919825a](https://github.com/MariaDB/server/commit/919825a)\
  2015-01-14 18:26:29 -0500
  * [MDEV-7368](https://jira.mariadb.org/browse/MDEV-7368) : SLES: Failed to start mysql.service: Unit mysql.service failed to load
* [Revision #fe0112e](https://github.com/MariaDB/server/commit/fe0112e)\
  2015-01-14 19:24:37 +0200
  * [MDEV-7424](https://jira.mariadb.org/browse/MDEV-7424): InnoDB: Assertion failure in thread 139901753345792 in file buf0mtflu.cc line 439
* [Revision #02099a3](https://github.com/MariaDB/server/commit/02099a3)\
  2015-01-14 18:19:05 +0100
  * [MDEV-7467](https://jira.mariadb.org/browse/MDEV-7467): sporadic failure in rpl.rpl\_gtid\_crash
* [Revision #ca6b86f](https://github.com/MariaDB/server/commit/ca6b86f)\
  2015-01-14 17:50:38 +0400
  * [MDEV-7448](https://jira.mariadb.org/browse/MDEV-7448) - mtr may leave stale mysqld
* [Revision #d9d9940](https://github.com/MariaDB/server/commit/d9d9940)\
  2015-01-14 18:24:23 -0500
  * [MDEV-7368](https://jira.mariadb.org/browse/MDEV-7368) : SLES: Failed to start mysql.service: Unit mysql.service failed to load
* [Revision #5900333](https://github.com/MariaDB/server/commit/5900333)\
  2015-01-14 12:10:13 +0100
  * [MDEV-7404](https://jira.mariadb.org/browse/MDEV-7404) REPAIR multiple tables crash in MDL\_ticket::has\_stronger\_or\_equal\_type
* [Revision #e53b41a](https://github.com/MariaDB/server/commit/e53b41a)\
  2015-01-13 19:28:03 +0100
  * cleanup
* [Revision #7f9f313](https://github.com/MariaDB/server/commit/7f9f313)\
  2015-01-13 19:27:28 +0100
  * [MDEV-7333](https://jira.mariadb.org/browse/MDEV-7333) "'show table status like 'table\_name'" on tokudb table lead to MariaDB crash
* [Revision #abf400e](https://github.com/MariaDB/server/commit/abf400e)\
  2015-01-13 13:12:05 -0500
  * [MDEV-6771](https://jira.mariadb.org/browse/MDEV-6771) : Incorrect Size for Transfer Reported to pv
* [Revision #70b4e6d](https://github.com/MariaDB/server/commit/70b4e6d)\
  2015-01-13 17:24:31 +0100\
  \*
  * Add ConnectTimout and QueryTimout options for ODBC tables. Should fix [MDEV-7415](https://jira.mariadb.org/browse/MDEV-7415). (To be specified in option\_list) modified: storage/connect/ha\_connect.cc storage/connect/odbccat.h storage/connect/odbconn.cpp storage/connect/odbconn.h storage/connect/tabodbc.cpp storage/connect/tabodbc.h
* [Revision #39556a7](https://github.com/MariaDB/server/commit/39556a7)\
  2015-01-13 16:48:11 +0200
  * [MDEV-7262](https://jira.mariadb.org/browse/MDEV-7262): innodb.innodb-mdev7046 fail on BuildBot
* [Revision #2de9427](https://github.com/MariaDB/server/commit/2de9427)\
  2015-01-13 14:18:23 +0100
  * [MDEV-7391](https://jira.mariadb.org/browse/MDEV-7391): rpl.rpl\_semi\_sync, rpl.rpl\_semi\_sync\_after\_sync\_row fail in buildbot
* [Revision #e695db0](https://github.com/MariaDB/server/commit/e695db0)\
  2015-01-12 17:03:45 +0100
  * [MDEV-7437](https://jira.mariadb.org/browse/MDEV-7437) remove suport for "atomics" with rwlocks
* [Revision #1f0ad6c](https://github.com/MariaDB/server/commit/1f0ad6c)\
  2015-01-13 11:50:33 +0400
  * [MDEV-7288](https://jira.mariadb.org/browse/MDEV-7288) USER/ROLE: CREATE OR REPLACE, CREATE IF NOT EXISTS, DROP IF EXISTS
* [Revision #a68ad5d](https://github.com/MariaDB/server/commit/a68ad5d)\
  2015-01-07 11:36:46 +0100
  * [MDEV-7325](https://jira.mariadb.org/browse/MDEV-7325) make lf\_hash\_delete(), lf\_hash\_search(), and lf\_hash\_iterator() never to return OOM
* [Revision #2a4a5d8](https://github.com/MariaDB/server/commit/2a4a5d8)\
  2015-01-12 13:30:30 +0400
  * [MDEV-7426](https://jira.mariadb.org/browse/MDEV-7426) - federated.federated\_server fails
* [Revision #517c5c9](https://github.com/MariaDB/server/commit/517c5c9)\
  2015-01-12 09:30:49 +0200
  * [MDEV-7262](https://jira.mariadb.org/browse/MDEV-7262): innodb.innodb-mdev7046 fail on BuildBot
* [Revision #2501a0e](https://github.com/MariaDB/server/commit/2501a0e)\
  2015-01-11 16:37:25 +0100
  * [MDEV-7364](https://jira.mariadb.org/browse/MDEV-7364) - mysqld --help --verbose prints random values for "debug"
* [Revision #3fcbd7c](https://github.com/MariaDB/server/commit/3fcbd7c)\
  2015-01-11 15:49:23 +0100
  * cleanup: remove unused THD::COND\_wsrep\_thd
* [Revision #2ab4968](https://github.com/MariaDB/server/commit/2ab4968)\
  2015-01-10 14:07:46 +0100
  * [MDEV-7410](https://jira.mariadb.org/browse/MDEV-7410) Temporary table name conflict between sessions
* [Revision #1182aeb](https://github.com/MariaDB/server/commit/1182aeb)\
  2015-01-09 21:52:16 -0500
  * [MDEV-7271](https://jira.mariadb.org/browse/MDEV-7271) : rpl.rpl\_domain\_id\_filter fails sporadically in buildbot
* [Revision #85c65f4](https://github.com/MariaDB/server/commit/85c65f4)\
  2015-01-09 23:36:50 +0100\
  \*
  * Fix [MDEV-7427](https://jira.mariadb.org/browse/MDEV-7427) by not reallocating the date format in ScanRecord on each inserted row. modified: storage/connect/ha\_connect.cc storage/connect/ha\_connect.h
* [Revision #6627895](https://github.com/MariaDB/server/commit/6627895)\
  2015-01-08 21:26:56 +0100
  * [MDEV-6731](https://jira.mariadb.org/browse/MDEV-6731) No ALGORITHM information in I\_S.VIEWS
* [Revision #b111d98](https://github.com/MariaDB/server/commit/b111d98)\
  2015-01-08 16:53:36 +0100
  * [MDEV-5533](https://jira.mariadb.org/browse/MDEV-5533) increase the default max thread pool size
* [Revision #dd80c22](https://github.com/MariaDB/server/commit/dd80c22)\
  2015-01-09 00:32:28 -0500
  * [MDEV-7123](https://jira.mariadb.org/browse/MDEV-7123) : [MariaDB 10.0.14](../../old-releases/10.0/10.0.14.md) Galera node shutdown with signal 11
* [Revision #8655136](https://github.com/MariaDB/server/commit/8655136)\
  2015-01-08 20:26:53 +0100
  * remove wsrep\_hton dependency from innodb/xtradb
* [Revision #4ce39dc](https://github.com/MariaDB/server/commit/4ce39dc)\
  2014-12-04 17:59:07 +0100
  * enable feedback plugin by default
* [Revision #54b26b4](https://github.com/MariaDB/server/commit/54b26b4)\
  2015-01-07 13:12:31 -0500
  * [MDEV-7129](https://jira.mariadb.org/browse/MDEV-7129) : Galera duplicate error on autoincrement field primary key
* [Revision #f27817c](https://github.com/MariaDB/server/commit/f27817c)\
  2015-01-07 14:45:39 +0100
  * [MDEV-7326](https://jira.mariadb.org/browse/MDEV-7326): Server deadlock in connection with parallel replication
* [Revision #0064952](https://github.com/MariaDB/server/commit/0064952)\
  2015-01-06 16:32:41 +0100
  * [MDEV-7189](https://jira.mariadb.org/browse/MDEV-7189): main.processlist fails sporadically in buildbot
* [Revision #4a32515](https://github.com/MariaDB/server/commit/4a32515)\
  2015-01-06 16:08:42 +0200
  * [MDEV-7403](https://jira.mariadb.org/browse/MDEV-7403): should not pass recv\_writer\_thread\_handle to CloseHandle()
* [Revision #d4bf645](https://github.com/MariaDB/server/commit/d4bf645)\
  2015-01-06 11:32:40 +0100\
  \*
  * Typo to eliminate some GCC warnings modified: storage/connect/odbconn.cpp storage/connect/plgdbsem.h
* [Revision #afd373c](https://github.com/MariaDB/server/commit/afd373c)\
  2015-01-06 10:18:04 +0100\
  \*
  * Set connection charset before calling mysql\_real\_connect for MYSQL tables. This should fix bug [MDEV-7343](https://jira.mariadb.org/browse/MDEV-7343). modified: storage/connect/ha\_connect.cc storage/connect/myconn.cpp storage/connect/myconn.h storage/connect/reldef.cpp storage/connect/reldef.h storage/connect/table.cpp storage/connect/tabmysql.cpp storage/connect/xtable.h
* [Revision #6e0a00e](https://github.com/MariaDB/server/commit/6e0a00e)\
  2015-01-06 09:52:09 +0100
  * [MDEV-7353](https://jira.mariadb.org/browse/MDEV-7353): rpl\_mdev6386 fails sporadically in buildbot
* [Revision #ed0ea64](https://github.com/MariaDB/server/commit/ed0ea64)\
  2015-01-05 17:06:50 -0500
  * [MDEV-7412](https://jira.mariadb.org/browse/MDEV-7412): Segfault during start with mysqldump SST
* [Revision #aee3ac4](https://github.com/MariaDB/server/commit/aee3ac4)\
  2015-01-02 10:02:04 -0500
  * [MDEV-7222](https://jira.mariadb.org/browse/MDEV-7222): Cluster Node Crash at CREATE DEFINER statement
* [Revision #455f77b](https://github.com/MariaDB/server/commit/455f77b)\
  2015-01-02 10:01:09 -0500
  * [MDEV-7222](https://jira.mariadb.org/browse/MDEV-7222): Cluster Node Crash at CREATE DEFINER statement
* [Revision #068416d](https://github.com/MariaDB/server/commit/068416d)\
  2015-01-02 09:50:51 -0500
  * DB-785 add a txn api to check if a txn is prepared
* [Revision #6f4f8c5](https://github.com/MariaDB/server/commit/6f4f8c5)\
  2014-12-31 20:58:54 -0500
  * [MDEV-7374](https://jira.mariadb.org/browse/MDEV-7374) : Losing connection to MySQL while running ALTER TABLE
* [Revision #61f73d4](https://github.com/MariaDB/server/commit/61f73d4)\
  2014-12-31 19:52:35 -0500
  * [MDEV-7397](https://jira.mariadb.org/browse/MDEV-7397): SIGSEGV on inserting into a key-less table
* [Revision #25aaa65](https://github.com/MariaDB/server/commit/25aaa65)\
  2014-12-31 19:46:48 -0500
  * [MDEV-6832](https://jira.mariadb.org/browse/MDEV-6832): ER\_LOCK\_WAIT\_TIMEOUT on SHOW STATUS
* [Revision #f0be022](https://github.com/MariaDB/server/commit/f0be022)\
  2014-12-30 17:10:54 +0200
  * [MDEV-5539](https://jira.mariadb.org/browse/MDEV-5539) Empty results in UNION with Sphinx engine The bug was fixed by Serg earlier by including Sphinx 2.2.6, but he forgot to update the test case.
* [Revision #dc92032](https://github.com/MariaDB/server/commit/dc92032)\
  2014-12-29 15:41:08 +0400
  * Fixed sysvars\_server\_embedded test result to reflect new values for query\_prealloc\_size, query\_alloc\_block\_size and log\_tc\_size.
* [Revision #6dbc48c](https://github.com/MariaDB/server/commit/6dbc48c)\
  2014-12-28 19:42:17 +0400
  * [MDEV-7324](https://jira.mariadb.org/browse/MDEV-7324) - Lock-free hash for table definition cache
* [Revision #8883c54](https://github.com/MariaDB/server/commit/8883c54)\
  2014-11-27 23:49:45 +0100
  * lf\_hash\_iterate() function
* [Revision #48430e4](https://github.com/MariaDB/server/commit/48430e4)\
  2014-11-27 20:51:23 +0100
  * lf\_hash changes, in lfind()
* [Revision #c0d4e8a](https://github.com/MariaDB/server/commit/c0d4e8a)\
  2014-12-28 13:54:41 +0200
  * [MDEV-7262](https://jira.mariadb.org/browse/MDEV-7262): innodb.innodb-mdev7046 fail on BuildBot
* [Revision #de09076](https://github.com/MariaDB/server/commit/de09076)\
  2014-12-28 13:44:30 +0200
  * [MDEV-7369](https://jira.mariadb.org/browse/MDEV-7369): MariaDB build fails when XTRADB\_STORAGE\_ENGINE enabled
* [Revision #5fafc3c](https://github.com/MariaDB/server/commit/5fafc3c)\
  2014-12-28 13:24:53 +0200
  * [MDEV-7369](https://jira.mariadb.org/browse/MDEV-7369): MariaDB build fails when XTRADB\_STORAGE\_ENGINE enabled
* [Revision #7860333](https://github.com/MariaDB/server/commit/7860333)\
  2014-12-27 03:23:49 +0000
  * Add fix for [MDEV-7369](https://jira.mariadb.org/browse/MDEV-7369)
* [Revision #f65901e](https://github.com/MariaDB/server/commit/f65901e)\
  2014-12-26 23:38:45 +0400
  * [MDEV-7273](https://jira.mariadb.org/browse/MDEV-7273) - 10.1 fails to start up during tc\_log initializations on PPC64
* [Revision #8c616cd](https://github.com/MariaDB/server/commit/8c616cd)\
  2014-12-26 19:44:38 +0400
  * [MDEV-7053](https://jira.mariadb.org/browse/MDEV-7053) - WSREP\_STATUS & WSREP\_MEMBERSHIP I\_S tables
* [Revision #db89dd3](https://github.com/MariaDB/server/commit/db89dd3)\
  2014-12-26 13:07:43 +0400
  * [MDEV-7364](https://jira.mariadb.org/browse/MDEV-7364) - mysqld --help --verbose prints random values for "debug"
* [Revision #ae09895](https://github.com/MariaDB/server/commit/ae09895)\
  2014-12-24 10:06:12 +0400
  * [MDEV-7277](https://jira.mariadb.org/browse/MDEV-7277) Server crashes on creating/opening tables on Windows debug build. The srid variable was used uninitialised when the field wasn't GIS. Only problem is that it makes the debugger unhappy. Still added the initialization.
* [Revision #03e0f1f](https://github.com/MariaDB/server/commit/03e0f1f)\
  2014-12-23 18:36:33 -0500
  * [MDEV-7053](https://jira.mariadb.org/browse/MDEV-7053) : WSREP\_STATUS & WSREP\_MEMBERSHIP I\_S tables
* [Revision #8051205](https://github.com/MariaDB/server/commit/8051205)\
  2014-12-23 21:21:23 +0400
  * Increased the version number
* [Revision #0b87de1](https://github.com/MariaDB/server/commit/0b87de1)\
  2014-12-23 13:38:00 +0100
  * [MDEV-162](https://jira.mariadb.org/browse/MDEV-162) Enhanced semisync replication
* [Revision #4d8b346](https://github.com/MariaDB/server/commit/4d8b346)\
  2014-12-19 12:36:23 +0100
  * [MDEV-7257](https://jira.mariadb.org/browse/MDEV-7257): Dump Thread Enhancements
* [Revision #3818bbb](https://github.com/MariaDB/server/commit/3818bbb)\
  2014-12-21 19:23:28 +0100
  * Adding mariadb-version on the view creation to view frm. ([MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916) followup)
* [Revision #96e505e](https://github.com/MariaDB/server/commit/96e505e)\
  2014-12-20 19:58:54 -0500
  * [MDEV-7319](https://jira.mariadb.org/browse/MDEV-7319) : Galera bootstrap (/etc/init.d/mysql bootstrap) returns code 0 on failure
* [Revision #260727a](https://github.com/MariaDB/server/commit/260727a)\
  2014-12-19 23:42:22 +0400
  * Fixed yet another compiler warning.
* [Revision #094640c](https://github.com/MariaDB/server/commit/094640c)\
  2014-12-19 23:17:59 +0400
  * Fixed a couple of compiler warnings.
* [Revision #bc21e7a](https://github.com/MariaDB/server/commit/bc21e7a)\
  2014-12-19 09:25:29 +0200
  * Fixed compiler warnings
* [Revision #b75090c](https://github.com/MariaDB/server/commit/b75090c)\
  2014-12-18 20:06:49 +0300
  * [MDEV-6830](https://jira.mariadb.org/browse/MDEV-6830): Server crashes in best\_access\_path after a sequence of SELECTs ...
* [Revision #826d7c6](https://github.com/MariaDB/server/commit/826d7c6)\
  2014-12-18 11:59:08 +0100
  * [MDEV-7342](https://jira.mariadb.org/browse/MDEV-7342): Test failure in perfschema.setup\_instruments\_defaults
* [Revision #724dbaa](https://github.com/MariaDB/server/commit/724dbaa)\
  2014-12-18 00:13:16 +0100
  * [MDEV-7150](https://jira.mariadb.org/browse/MDEV-7150) Wrong auto increment values on INSERT .. ON DUPLICATE KEY UPDATE when the inserted columns include NULL in an auto-increment column
* [Revision #a4ff2af](https://github.com/MariaDB/server/commit/a4ff2af)\
  2014-12-17 14:38:14 +0100
  * cleanup
* [Revision #ff5349b](https://github.com/MariaDB/server/commit/ff5349b)\
  2014-12-17 14:35:13 +0100
  * [MDEV-6985](https://jira.mariadb.org/browse/MDEV-6985): MariaDB crashes on stored procedure call
* [Revision #357cb12](https://github.com/MariaDB/server/commit/357cb12)\
  2014-12-16 15:33:13 +0400
  * DEV-7221 from\_days fails after null value
* [Revision #ea01fff](https://github.com/MariaDB/server/commit/ea01fff)\
  2014-12-16 15:31:25 +0400
  * Fixing test failures caused by the previous commits. Adding "--source include/have\_udf.inc" and a few "--replace" commands.
* [Revision #5257d71](https://github.com/MariaDB/server/commit/5257d71)\
  2014-12-15 17:13:47 +0200
  * [MDEV-6855](https://jira.mariadb.org/browse/MDEV-6855) Assertion \`cond\_type == Item::FUNC\_ITEM' failed in check\_group\_min\_max\_predicates with GROUP BY, aggregate in WHERE SQ, multi-part key
* [Revision #2dbd2693](https://github.com/MariaDB/server/commit/2dbd2693)\
  2014-12-15 17:41:15 +0400
  * [MDEV-7283](https://jira.mariadb.org/browse/MDEV-7283) UDF: CREATE OR REPLACE, CREATE IF NOT EXISTS, DROP IF EXISTS [MDEV-7282](https://jira.mariadb.org/browse/MDEV-7282) SP: CREATE OR REPLACE, CREATE IF NOT EXISTS
* [Revision #10ab3e6](https://github.com/MariaDB/server/commit/10ab3e6)\
  2014-12-15 14:49:23 +0200
  * [MDEV-4010](https://jira.mariadb.org/browse/MDEV-4010) Deadlock on concurrent INSERT .. SELECT into an Aria table with statement binary logging There was a bug in lock handling when mixing INSERT ... SELECT on the same table.
* [Revision #80ee57a](https://github.com/MariaDB/server/commit/80ee57a)\
  2014-12-15 13:01:11 +0200
  * [MDEV-6896](https://jira.mariadb.org/browse/MDEV-6896) kill user command cause MariaDB crash
* [Revision #4a32d9c](https://github.com/MariaDB/server/commit/4a32d9c)\
  2014-12-15 11:16:33 +0200
  * [MDEV-6871](https://jira.mariadb.org/browse/MDEV-6871) Multi-value insert on MyISAM table that makes slaves crash (when using --skip-external-locking=0) Problem was that repair() did lock and unlock tables, which leaved already locked tables in wrong state
* [Revision #8761f22](https://github.com/MariaDB/server/commit/8761f22)\
  2014-12-14 22:47:12 +0100\
  \*
  * Temporary fix for [MDEV-7304](https://jira.mariadb.org/browse/MDEV-7304). modified: storage/connect/rcmsg.c
* [Revision #3a37c01](https://github.com/MariaDB/server/commit/3a37c01)\
  2014-12-12 17:16:11 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Addendum, update company name in copyright notice
* [Revision #fc1a705](https://github.com/MariaDB/server/commit/fc1a705)\
  2014-12-12 17:13:13 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Addendum, update company name in copyright notice
* [Revision #743e2ae](https://github.com/MariaDB/server/commit/743e2ae)\
  2014-12-12 17:10:51 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Addendum, update company name in copyright notice
* [Revision #48ed8ab](https://github.com/MariaDB/server/commit/48ed8ab)\
  2014-12-12 10:58:38 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Update company name
* [Revision #756c6f7](https://github.com/MariaDB/server/commit/756c6f7)\
  2014-12-12 10:46:31 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Update company name
* [Revision #def5bd6](https://github.com/MariaDB/server/commit/def5bd6)\
  2014-12-12 10:40:27 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Update company name
* [Revision #4ba6ee1](https://github.com/MariaDB/server/commit/4ba6ee1)\
  2014-12-12 10:38:19 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Update company name
* [Revision #16fb296](https://github.com/MariaDB/server/commit/16fb296)\
  2014-12-12 14:03:20 +0100
  * Fix typo that breaks compilation on platforms without atomics.
* [Revision #263cf26](https://github.com/MariaDB/server/commit/263cf26)\
  2014-12-12 04:42:59 +0400
  * Increased the version number
* [Revision #0b936cd](https://github.com/MariaDB/server/commit/0b936cd)\
  2014-12-10 16:46:21 +0400
  * Using Schema\_specification\_st instead of HA\_CREATE\_INFO in a few places where the former is enough.
* [Revision #4f9f3d4](https://github.com/MariaDB/server/commit/4f9f3d4)\
  2014-12-10 06:24:56 -0500
  * empty revision
* [Revision #76c3981](https://github.com/MariaDB/server/commit/76c3981)\
  2014-12-10 12:12:09 +0200
  * Fix test case to allow success on create table (Windows).
* [Revision #822eb6c](https://github.com/MariaDB/server/commit/822eb6c)\
  2014-12-10 13:41:14 +0400
  * [MDEV-7285](https://jira.mariadb.org/browse/MDEV-7285) SERVER: CREATE OR REPLACE and CREATE IF NOT EXISTS
* [Revision #14cfb0a](https://github.com/MariaDB/server/commit/14cfb0a)\
  2014-12-10 12:00:25 +0400
  * [MDEV-6409](https://jira.mariadb.org/browse/MDEV-6409) CREATE VIEW replication problem if error occurs in mysql\_register\_view An additional debug test, made by Sriram Patil while working on "CREATE VIEW IF NOT EXISTS".
* [Revision #60277b8](https://github.com/MariaDB/server/commit/60277b8)\
  2014-12-10 11:32:52 +0400
  * [MDEV-7287](https://jira.mariadb.org/browse/MDEV-7287) VIEW: CREATE IF NOT EXISTS Forgot to do "git add" for a number of files in the previous commit.
* [Revision #acdc383](https://github.com/MariaDB/server/commit/acdc383)\
  2014-12-10 11:06:36 +0400
  * [MDEV-7287](https://jira.mariadb.org/browse/MDEV-7287) VIEW: CREATE IF NOT EXISTS
* [Revision #92a523e](https://github.com/MariaDB/server/commit/92a523e)\
  2014-12-10 10:40:35 +0400
  * [MDEV-7280](https://jira.mariadb.org/browse/MDEV-7280) DATABASE: CREATE OR REPLACE A clean-up: require CREATE+DROP privileges for "CREATE OR REPLACE DATABASE", instead of just CREATE privilege.
* [Revision #31c7458](https://github.com/MariaDB/server/commit/31c7458)\
  2014-12-10 08:19:19 +0400
  * [MDEV-7280](https://jira.mariadb.org/browse/MDEV-7280) DATABASE: CREATE OR REPLACE A test clean-up: The "SHOW DATABASES" queries now use "LIKE 'db%'", to display only the databases created during this test, thus exclude the system databases, as some of them can be optional (e.g. performance\_schema).
* [Revision #dd270e4](https://github.com/MariaDB/server/commit/dd270e4)\
  2014-12-10 08:13:08 +0400
  * [MDEV-7280](https://jira.mariadb.org/browse/MDEV-7280) DATABASE: CREATE OR REPLACE
* [Revision #41367e4](https://github.com/MariaDB/server/commit/41367e4)\
  2014-12-09 10:35:16 -0500
  * [MDEV-7204](https://jira.mariadb.org/browse/MDEV-7204): mariadb-galera-server el7 rpms packaging issue, no mariadb-server in provides [MDEV-7233](https://jira.mariadb.org/browse/MDEV-7233): Fix issue with missing dependency socat when installing MariaDB-galera-server on RedhatEL/OracleEL/(Others?) RPM based
* [Revision #e51e5e9](https://github.com/MariaDB/server/commit/e51e5e9)\
  2014-12-08 23:44:53 -0500
  * Merged patch for [Bug #1167368](https://bugs.launchpad.net/bugs/1167368) from maria-5.5-galera.
* [Revision #c6d3f80](https://github.com/MariaDB/server/commit/c6d3f80)\
  2014-12-08 10:56:08 +0400
  * [MDEV-7112](https://jira.mariadb.org/browse/MDEV-7112) Split HA\_CREATE\_INFO
* [Revision #b372720](https://github.com/MariaDB/server/commit/b372720)\
  2014-12-06 20:34:33 +0300
  * Update test results
* [Revision #eeef80d](https://github.com/MariaDB/server/commit/eeef80d)\
  2014-12-06 20:13:38 +0300
  * EXPLAIN FORMAT=JSON : Fix [MDEV-7266](https://jira.mariadb.org/browse/MDEV-7266), bug in pretty-printer
* [Revision #dc25932](https://github.com/MariaDB/server/commit/dc25932)\
  2014-12-06 19:27:42 +0300
  * EXPLAIN JSON: Print out the "expensive constant condition" attached to joins.
* [Revision #db21fdd](https://github.com/MariaDB/server/commit/db21fdd)\
  2014-12-05 16:09:48 +0100
  * [MDEV-6676](https://jira.mariadb.org/browse/MDEV-6676): Optimistic parallel replication
* [Revision #1e3f09f](https://github.com/MariaDB/server/commit/1e3f09f)\
  2014-12-06 04:02:30 +0300
  * [MDEV-7264](https://jira.mariadb.org/browse/MDEV-7264): Assertion \`0' failed in subselect\_engine::get\_identifier()
* [Revision #5ee1c25](https://github.com/MariaDB/server/commit/5ee1c25)\
  2014-12-06 03:11:03 +0300
  * EXPLAIN FORMAT=JSON: Full scan on NULL key (join case)
* [Revision #a80a797](https://github.com/MariaDB/server/commit/a80a797)\
  2014-12-06 02:23:37 +0300
  * EXPLAIN FORMAT=JSON: Support "range checked for each record"
* [Revision #9cac764](https://github.com/MariaDB/server/commit/9cac764)\
  2014-12-06 01:11:22 +0300
  * EXPLAIN FORMAT=JSON: Support range+MRR plans (when MRR is used but BKA is not)
* [Revision #f7fed26](https://github.com/MariaDB/server/commit/f7fed26)\
  2014-12-05 21:38:16 +0400
  * Storage engines tests: ALTER ONLINE works differently for MERGE in 10.0
* [Revision #8fb2c80](https://github.com/MariaDB/server/commit/8fb2c80)\
  2014-12-05 16:38:48 +0400
  * Fixed valgrind warnings in delete\_dynamic().
* [Revision #010724f](https://github.com/MariaDB/server/commit/010724f)\
  2014-12-05 14:23:24 +0400
  * Run engines tests for MyISAM and in-built InnoDB
* [Revision #5bba110](https://github.com/MariaDB/server/commit/5bba110)\
  2014-12-04 14:10:41 +0200
  * Add possibility to success on Windows.
* [Revision #c8f7f98](https://github.com/MariaDB/server/commit/c8f7f98)\
  2014-12-04 02:54:42 +0400
  * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests, part 6
* [Revision #f02f061](https://github.com/MariaDB/server/commit/f02f061)\
  2014-12-04 02:17:09 +0400
  * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests, part 5
* [Revision #d5f52fe](https://github.com/MariaDB/server/commit/d5f52fe)\
  2014-12-04 02:16:41 +0400
  * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests, part 4
* [Revision #27ac97e](https://github.com/MariaDB/server/commit/27ac97e)\
  2014-12-04 01:59:25 +0400
  * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests, part 3
* [Revision #aafdc4b](https://github.com/MariaDB/server/commit/aafdc4b)\
  2014-12-04 01:52:03 +0400
  * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests, part 2
* [Revision #cc06415](https://github.com/MariaDB/server/commit/cc06415)\
  2014-12-03 19:53:40 +0400
  * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests, part 1
* [Revision #6cd78ee](https://github.com/MariaDB/server/commit/6cd78ee)\
  2014-12-02 13:26:45 +0200
  * [MDEV-7242](https://jira.mariadb.org/browse/MDEV-7242): innodb.innodb-mdev7046 fails in various ways on buildbot
* [Revision #d79cce8](https://github.com/MariaDB/server/commit/d79cce8)\
  2014-12-03 15:49:31 +0100
  * [MDEV-4393](https://jira.mariadb.org/browse/MDEV-4393): show\_explain.test times out randomly
* [Revision #ed313e8](https://github.com/MariaDB/server/commit/ed313e8)\
  2014-12-01 14:58:29 +0400
  * [MDEV-7148](https://jira.mariadb.org/browse/MDEV-7148) - Recurring: InnoDB: Failing assertion: !lock->recursive
* [Revision #df20184](https://github.com/MariaDB/server/commit/df20184)\
  2014-12-03 13:38:39 +0200
  * [MDEV-7252](https://jira.mariadb.org/browse/MDEV-7252): Test failure on innodb.innodb\_bug12400341 at Windows
* [Revision #e544bcd](https://github.com/MariaDB/server/commit/e544bcd)\
  2014-12-02 12:19:29 +0200
  * [MDEV-7243](https://jira.mariadb.org/browse/MDEV-7243): innodb-change-buffer-recovery fails on windows
* [Revision #e0c71a9](https://github.com/MariaDB/server/commit/e0c71a9)\
  2014-12-02 01:31:49 +0400
  * [MDEV-7169](https://jira.mariadb.org/browse/MDEV-7169): innodb.innodb\_bug14147491 fails in buildbot on Windows
* [Revision #89a3628](https://github.com/MariaDB/server/commit/89a3628)\
  2014-11-25 12:04:32 +0200
  * Better comments part 2 with proof and simplified implementation. Thanks to Daniel Black.
* [Revision #e3ded84](https://github.com/MariaDB/server/commit/e3ded84)\
  2014-11-25 08:22:10 +0200
  * Fix typo.
* [Revision #c3b0894](https://github.com/MariaDB/server/commit/c3b0894)\
  2014-11-24 18:32:44 +0100\
  \*
  * Make the fix for getting day names of dates more general modified: storage/connect/ha\_connect.cc storage/connect/value.cpp
* [Revision #c89b8a3](https://github.com/MariaDB/server/commit/c89b8a3)\
  2014-11-24 18:26:44 +0100\
  \*
  * Enhance the implementation of ODBC tables when using scrollable cursor modified: storage/connect/odbconn.cpp storage/connect/odbconn.h storage/connect/tabodbc.cpp
* [Revision #6211708](https://github.com/MariaDB/server/commit/6211708)\
  2014-11-23 16:12:26 +0100\
  \*
  * Fix a bug causing the day always printed as Sunday for date columns with a date format specifying DDD or DDDD. modified: storage/connect/ha\_connect.cc storage/connect/value.cpp
* [Revision #b2db891](https://github.com/MariaDB/server/commit/b2db891)\
  2014-11-20 23:18:51 +0100\
  \*
  * Remove gcc warning (variable n is set and not used) modified: storage/connect/odbconn.cpp
* [Revision #d592f66](https://github.com/MariaDB/server/commit/d592f66)\
  2014-11-20 12:57:33 +0100\
  \*
  * Remove gcc warning on variable n set but not used modified: storage/connect/odbconn.cpp
* [Revision #c144cf3](https://github.com/MariaDB/server/commit/c144cf3)\
  2014-11-20 11:00:02 +0100\
  \*
  * Implement putting in memory the result set from an ODBC query. modified: storage/connect/odbconn.cpp storage/connect/odbconn.h storage/connect/tabodbc.cpp storage/connect/tabodbc.h
* [Revision #a4cdd20](https://github.com/MariaDB/server/commit/a4cdd20)\
  2014-11-19 13:33:37 -0500
  * [MDEV-7131](https://jira.mariadb.org/browse/MDEV-7131): \[PATCH] wsrep\_guess\_ip doesn't compile on OpenBSD
* [Revision #6f65d2d](https://github.com/MariaDB/server/commit/6f65d2d)\
  2014-11-17 11:56:03 -0500
  * [MDEV-6924](https://jira.mariadb.org/browse/MDEV-6924) : Server crashed on CREATE TABLE ... SELECT
* [Revision #0773c7f](https://github.com/MariaDB/server/commit/0773c7f)\
  2014-11-04 08:30:23 +0100
  * Added sles11 repo packages
* [Revision #7dd74fa](https://github.com/MariaDB/server/commit/7dd74fa)\
  2014-10-08 13:30:45 -0400
  * [MDEV-6481](https://jira.mariadb.org/browse/MDEV-6481): Yum Upgrade on CentOS 6.5 causes instant crash of MariaDB/Galera
* [Revision #b197066](https://github.com/MariaDB/server/commit/b197066)\
  2014-10-03 21:22:41 -0400
  * [MDEV-6807](https://jira.mariadb.org/browse/MDEV-6807): InnoDB: Assertion failure in file lock0lock.cc (lock != ctx->wait\_lock)
* [Revision #9a57de8](https://github.com/MariaDB/server/commit/9a57de8)\
  2014-09-30 18:06:15 -0400
  * bzr merge -r4123..4144 codership/5.6
* [Revision #023366e](https://github.com/MariaDB/server/commit/023366e)\
  2014-09-24 12:17:29 -0400
  * Moved wsrep\_slave\_threads to optional settings.
* [Revision #e207e5f](https://github.com/MariaDB/server/commit/e207e5f)\
  2014-09-23 14:33:27 -0400
  * Updated config files: - Removed QC restriction - Added bind-address Fixed file permissions for wsrep\_sst\_rsync.sh. Removed some unnecessary files.
* [Revision #4538665](https://github.com/MariaDB/server/commit/4538665)\
  2014-09-22 12:15:44 -0400
  * [MDEV-6740](https://jira.mariadb.org/browse/MDEV-6740) : Galera crash in rpl\_sql\_thread\_info/cached\_charset\_compare
* [Revision #c4356bf](https://github.com/MariaDB/server/commit/c4356bf)\
  2014-09-17 14:59:39 -0400
  * [MDEV-6447](https://jira.mariadb.org/browse/MDEV-6447): Galera: Enable QC
* [Revision #cf180e7](https://github.com/MariaDB/server/commit/cf180e7)\
  2014-09-17 09:54:04 -0400
  * Reverting version change to match the version of supporting packages available on buildbot.
* [Revision #69bc2d5](https://github.com/MariaDB/server/commit/69bc2d5)\
  2014-09-16 12:58:35 -0400
  * Updated mysqld--help test and result ([MDEV-6717](https://jira.mariadb.org/browse/MDEV-6717), [MDEV-6659](https://jira.mariadb.org/browse/MDEV-6659)).
* [Revision #ac2a2f3](https://github.com/MariaDB/server/commit/ac2a2f3)\
  2014-09-16 12:42:17 -0400
  * [MDEV-6659](https://jira.mariadb.org/browse/MDEV-6659): mysqld --help --verbose initializes wsrep
* [Revision #76d15af](https://github.com/MariaDB/server/commit/76d15af)\
  2014-09-09 19:19:12 -0400
  * Minor improvements in mtr and wsrep test files.
* [Revision #4ffccff](https://github.com/MariaDB/server/commit/4ffccff)\
  2014-09-09 13:43:01 -0400
  * [MDEV-6717](https://jira.mariadb.org/browse/MDEV-6717) : wsrep\_data\_home\_dir should default to @@datadir
* [Revision #f3e95ca](https://github.com/MariaDB/server/commit/f3e95ca)\
  2014-09-09 09:25:47 -0400
  * [MDEV-6699](https://jira.mariadb.org/browse/MDEV-6699) : wsrep\_node\_name not automatically set to hostname
* [Revision #47fcca0](https://github.com/MariaDB/server/commit/47fcca0)\
  2014-09-08 21:21:37 -0400
  * [MDEV-6667](https://jira.mariadb.org/browse/MDEV-6667) : Improved handling of wsrep-new-cluster option
* [Revision #c0483b0](https://github.com/MariaDB/server/commit/c0483b0)\
  2014-09-08 14:01:41 -0400
  * Bumping server version. (10.0.14-galera)
* [Revision #d7f3775](https://github.com/MariaDB/server/commit/d7f3775)\
  2014-09-03 18:25:49 +0300
  * [MDEV-6651](https://jira.mariadb.org/browse/MDEV-6651): MariaDB galera cluster crashes in file row0mysql.cc line 684 DELETE FROM ports WHERE ports.id = 'f37aa3fe-ab99-4d0f-a566-6cd3169d7516' where table ports have foreign keys.
* [Revision #f99f573](https://github.com/MariaDB/server/commit/f99f573)\
  2014-08-29 09:42:13 +0300
  * [MDEV-6656](https://jira.mariadb.org/browse/MDEV-6656): Test wsrep.variables hangs
* [Revision #4fb45aa](https://github.com/MariaDB/server/commit/4fb45aa)\
  2014-08-27 15:28:43 +0300
  * Fix compiler error when WITH\_WSREP is not used.
* [Revision #9d15afd](https://github.com/MariaDB/server/commit/9d15afd)\
  2014-08-26 16:23:56 -0400
  * Merged fix for [MDEV-6646](https://jira.mariadb.org/browse/MDEV-6646) from maria-5.5-galera.
* [Revision #9b506d4](https://github.com/MariaDB/server/commit/9b506d4)\
  2014-08-25 09:13:15 +0300
  * [MDEV-6602](https://jira.mariadb.org/browse/MDEV-6602): rpl.rpl\_mdev6020 fails sporadically with SIGABRT
* [Revision #de38fcf](https://github.com/MariaDB/server/commit/de38fcf)\
  2014-08-14 18:43:04 -0400
  * Fix for build failure in tokudb.
* [Revision #f523662](https://github.com/MariaDB/server/commit/f523662)\
  2014-08-14 18:19:01 -0400
  * Fix for some failing rpl tests.
* [Revision #0680eea](https://github.com/MariaDB/server/commit/0680eea)\
  2014-08-13 11:29:13 -0400
  * Test modifications
* [Revision #ef4cbd8](https://github.com/MariaDB/server/commit/ef4cbd8)\
  2014-08-12 18:26:45 -0400
  * Updated WSREP\_PATCH\_REVNO.
* [Revision #305c1ae](https://github.com/MariaDB/server/commit/305c1ae)\
  2014-08-12 16:39:10 -0400
  * Merge of innobase changes to xtradb. (r3871..3873).
* [Revision #8ec02bb](https://github.com/MariaDB/server/commit/8ec02bb)\
  2014-08-12 14:50:26 -0400
  * bzr merge -c4123 codership/5.6/ (minus [4122](https://bazaar.launchpad.net/~codership/codership-mysql/5.6/revision/4122))
* [Revision #857abf1](https://github.com/MariaDB/server/commit/857abf1)\
  2014-08-12 14:05:44 -0400
  * bzr merge -r4104..4120 codership/5.6/
* [Revision #38f048a](https://github.com/MariaDB/server/commit/38f048a)\
  2014-08-12 12:43:56 -0400
  * bzr merge -r4101..4103 codership/5.6/
* [Revision #e06e12f](https://github.com/MariaDB/server/commit/e06e12f)\
  2014-08-11 14:31:30 -0400
  * Added 'have\_innodb\_disallow\_writes.inc'.
* [Revision #f842099](https://github.com/MariaDB/server/commit/f842099)\
  2014-08-07 18:29:20 -0400
  * [MDEV-6490](https://jira.mariadb.org/browse/MDEV-6490): mysqldump unknown option --galera-sst-mode
* [Revision #746c755](https://github.com/MariaDB/server/commit/746c755)\
  2014-08-05 19:00:54 -0400
  * [MDEV-6495](https://jira.mariadb.org/browse/MDEV-6495): local merge from maria-5.5-galera.
* [Revision #30b5a4d](https://github.com/MariaDB/server/commit/30b5a4d)\
  2014-07-31 16:40:32 -0400
  * [MDEV-6492](https://jira.mariadb.org/browse/MDEV-6492): MariaDB Galera Cluster cant use rsync sst
* [Revision #05ff47c](https://github.com/MariaDB/server/commit/05ff47c)\
  2014-07-22 10:04:57 -0400
  * Local merge of patch for [MDEV-6377](https://jira.mariadb.org/browse/MDEV-6377) from maria-5.5-galera.
* [Revision #efdf79b](https://github.com/MariaDB/server/commit/efdf79b)\
  2014-07-22 09:43:42 -0400
  * Local merge of patch for [MDEV-4647](https://jira.mariadb.org/browse/MDEV-4647) from maria-5.5-galera.
* [Revision #e5cea60](https://github.com/MariaDB/server/commit/e5cea60)\
  2014-07-21 17:27:06 -0400
  * Local merge of patch for [MDEV-3896](https://jira.mariadb.org/browse/MDEV-3896) from maria-5.5-galera.
* [Revision #eaa0fe7](https://github.com/MariaDB/server/commit/eaa0fe7)\
  2014-07-15 01:01:49 -0400
  * [MDEV-4728](https://jira.mariadb.org/browse/MDEV-4728): local merge from maria-5.5-galera.
* [Revision #b77fc5a](https://github.com/MariaDB/server/commit/b77fc5a)\
  2014-07-12 18:21:29 -0400
  * Merge of patch for [MDEV-6399](https://jira.mariadb.org/browse/MDEV-6399).
* [Revision #b6a116c](https://github.com/MariaDB/server/commit/b6a116c)\
  2014-07-11 13:40:39 -0400
  * Merge of patch for [MDEV-5786](https://jira.mariadb.org/browse/MDEV-5786).
* [Revision #dc377fc](https://github.com/MariaDB/server/commit/dc377fc)\
  2014-07-09 11:07:23 -0400
  * Merge of patch for [MDEV-6411](https://jira.mariadb.org/browse/MDEV-6411) from maria-5.5-galera.
* [Revision #3d1ac12](https://github.com/MariaDB/server/commit/3d1ac12)\
  2014-07-04 11:59:09 +0300
  * Add test case for [1314854](https://bugs.launchpad.net/percona-xtradb-cluster/+bug/1314854)
* [Revision #84b3ec1](https://github.com/MariaDB/server/commit/84b3ec1)\
  2014-07-04 11:58:14 +0300
  * Merge -r4105..4106 from codership/5.6
* [Revision #006cb2a](https://github.com/MariaDB/server/commit/006cb2a)\
  2014-07-04 11:41:09 +0300
  * Merge -r4102..4103 codership/5.6/
* [Revision #fbf3974](https://github.com/MariaDB/server/commit/fbf3974)\
  2014-06-30 09:03:29 -0400
  * Bumping server version. (10.0.13-galera)
* [Revision #7ed27e1](https://github.com/MariaDB/server/commit/7ed27e1)\
  2014-06-26 12:11:12 -0400
  * Fix for some failing tests.
* [Revision #9e1075e](https://github.com/MariaDB/server/commit/9e1075e)\
  2014-06-25 11:22:01 -0400
  * Follow-up patch for [Bug #1312618](https://bugs.launchpad.net/bugs/1312618) to fix a segfault.
* [Revision #c039d96](https://github.com/MariaDB/server/commit/c039d96)\
  2014-06-25 00:45:12 -0400
  * Fixed a typo and updated mysqld--help test result.
* [Revision #9a0b80c](https://github.com/MariaDB/server/commit/9a0b80c)\
  2014-06-23 19:14:28 -0400
  * [MDEV-5747](https://jira.mariadb.org/browse/MDEV-5747): wsrep system variables not listed alphabetically
* [Revision #b9a4569](https://github.com/MariaDB/server/commit/b9a4569)\
  2014-06-23 10:18:52 -0400
  * Updated sys\_vars.all\_vars result file.
* [Revision #02034e4](https://github.com/MariaDB/server/commit/02034e4)\
  2014-06-19 21:55:19 -0400
  * Merging fix for [MDEV-6296](https://jira.mariadb.org/browse/MDEV-6296) from maria-5.5-galera.
* [Revision #97779a2](https://github.com/MariaDB/server/commit/97779a2)\
  2014-06-19 18:48:20 -0400
  * bzr merge -r4091..4101 codership/5.6/
* [Revision #0f5522c](https://github.com/MariaDB/server/commit/0f5522c)\
  2014-06-18 10:19:18 -0400
  * [MDEV-6316](https://jira.mariadb.org/browse/MDEV-6316): (post-fix) Using C-style comments in mysqldump.
* [Revision #1fbb705](https://github.com/MariaDB/server/commit/1fbb705)\
  2014-06-16 14:55:14 -0400
  * [MDEV-6316](https://jira.mariadb.org/browse/MDEV-6316): Fix mysqldump SST method to transfer binlog state to the joiner
* [Revision #20279b0](https://github.com/MariaDB/server/commit/20279b0)\
  2014-06-16 10:32:21 -0400
  * Bumping the revision number.
* [Revision #2357871](https://github.com/MariaDB/server/commit/2357871)\
  2014-06-09 16:13:30 -0400
  * Fix for a debian build failure (cherry-picked from 10.0:r4231).
* [Revision #cc66ae6](https://github.com/MariaDB/server/commit/cc66ae6)\
  2014-06-06 13:27:15 -0400
  * [MDEV-6317](https://jira.mariadb.org/browse/MDEV-6317): Fix rsync SST method to transfer binlog state to the joiner
* [Revision #68deb11](https://github.com/MariaDB/server/commit/68deb11)\
  2014-06-05 23:31:00 -0400
  * Modified mtr script to skip inclusion of 'galera' test suites if galera library is not specified or found.
* [Revision #97d8323](https://github.com/MariaDB/server/commit/97d8323)\
  2014-06-02 22:45:41 -0400
  * Fix for wsrep\_sst\_xtrabackup-v2.sh script.
* [Revision #6fc646e](https://github.com/MariaDB/server/commit/6fc646e)\
  2014-06-02 08:26:42 -0400
  * Fixed a typo in debian control file.
* [Revision #d939fad](https://github.com/MariaDB/server/commit/d939fad)\
  2014-05-29 21:02:17 -0400
  * Added rsync to galera server's rpm dependency list.
* [Revision #707f378](https://github.com/MariaDB/server/commit/707f378)\
  2014-05-29 15:39:29 -0400
  * Added rsync to galera server's debian dependency list.
* [Revision #7e85cfb](https://github.com/MariaDB/server/commit/7e85cfb)\
  2014-05-28 00:46:21 -0400
  * [MDEV-6266](https://jira.mariadb.org/browse/MDEV-6266): Changing password fails on galera cluster
* [Revision #8d37bd4](https://github.com/MariaDB/server/commit/8d37bd4)\
  2014-05-27 10:11:42 -0400
  * Fixing a typo s/connection\_tcpwrap\_errors/connection\_errors\_tcpwrap, causing build to fail when HAVE\_LIBWRAP is enabled.
* [Revision #ef7e173](https://github.com/MariaDB/server/commit/ef7e173)\
  2014-05-27 09:06:04 -0400
  * Removing rsync from the debian build dependency list.
* [Revision #bd5ca5e](https://github.com/MariaDB/server/commit/bd5ca5e)\
  2014-05-25 00:18:26 -0400
  * [MDEV-6211](https://jira.mariadb.org/browse/MDEV-6211): MariaDB-Galera-server uses 'socat', but 'socat' is not in the dependency list
* [Revision #ab49474](https://github.com/MariaDB/server/commit/ab49474)\
  2014-05-22 18:31:04 -0400
  * Merging changes from maria-5.5-galera and some test fixes.
* [Revision #0bf3ed1](https://github.com/MariaDB/server/commit/0bf3ed1)\
  2014-05-21 18:10:43 -0400
  * bzr merge -r4089..4091 codership/5.6
* [Revision #0b98d2f](https://github.com/MariaDB/server/commit/0b98d2f)\
  2014-05-21 17:07:17 -0400
  * bzr merge -r4065..4088 codership/5.6
* [Revision #0903e2b](https://github.com/MariaDB/server/commit/0903e2b)\
  2014-05-21 16:03:58 -0400
  * Fix for a segfault.
* [Revision #645d402](https://github.com/MariaDB/server/commit/645d402)\
  2014-05-21 15:16:15 -0400
  * Fix for a build failure.
* [Revision #81a85ad](https://github.com/MariaDB/server/commit/81a85ad)\
  2014-05-21 15:04:13 -0400
  * bzr merge -r3985..3991 codership/5.5
* [Revision #99df0fb](https://github.com/MariaDB/server/commit/99df0fb)\
  2014-05-21 14:32:57 -0400
  * bzr merge -r3968..3984 codership/5.5 (non-Innodb changes only).
* [Revision #8a6f4e1](https://github.com/MariaDB/server/commit/8a6f4e1)\
  2014-05-21 12:09:31 -0400
  * Updated wsrep.variables result.
* [Revision #8597170](https://github.com/MariaDB/server/commit/8597170)\
  2014-05-21 11:59:33 -0400
  * Added test for [MDEV-4953](https://jira.mariadb.org/browse/MDEV-4953).
* [Revision #2f90221](https://github.com/MariaDB/server/commit/2f90221)\
  2014-05-21 11:23:59 -0400
  * Fixed a segfault issue by initializing thd's system\_thread\_info in wsrep applier threads, introduced by [MDEV-6156](https://jira.mariadb.org/browse/MDEV-6156).
* [Revision #558995a](https://github.com/MariaDB/server/commit/558995a)\
  2014-05-12 12:14:27 -0400
  * [MDEV-5942](https://jira.mariadb.org/browse/MDEV-5942) (Issue 1), [MDEV-5903](https://jira.mariadb.org/browse/MDEV-5903)
* [Revision #bdeb847](https://github.com/MariaDB/server/commit/bdeb847)\
  2014-04-30 15:40:00 -0400
  * [MDEV-6192](https://jira.mariadb.org/browse/MDEV-6192) \[Warning] Failed to load slave replication state from table mysql.gtid\_slave\_pos: 1286: Unknown storage engine 'InnoDB'
* [Revision #43a9e65](https://github.com/MariaDB/server/commit/43a9e65)\
  2014-04-17 14:10:22 -0400
  * [MDEV-6132](https://jira.mariadb.org/browse/MDEV-6132): yum update for MGC-10.0 fails (10.0.7 -> 10.0.10)
* [Revision #b11be05](https://github.com/MariaDB/server/commit/b11be05)\
  2014-04-16 13:04:03 -0400
  * [MDEV-6079](https://jira.mariadb.org/browse/MDEV-6079): xtrabackup SST failing with maria-10.0-galera
* [Revision #eec6222](https://github.com/MariaDB/server/commit/eec6222)\
  2014-04-15 22:31:08 -0400
  * Adding wsrep\_sst\_xtrabackup-v2 to the list of files in mariadb-galera-server package.
* [Revision #df1ee18](https://github.com/MariaDB/server/commit/df1ee18)\
  2014-04-15 22:16:11 -0400
  * Fix for build failure.
* [Revision #9983873](https://github.com/MariaDB/server/commit/9983873)\
  2014-04-15 14:27:45 -0400
  * [MDEV-6098](https://jira.mariadb.org/browse/MDEV-6098) mysqldump sst fails on maria-10.0-galera
* [Revision #24ad467](https://github.com/MariaDB/server/commit/24ad467)\
  2014-04-11 13:20:13 -0400
  * [MDEV-6077](https://jira.mariadb.org/browse/MDEV-6077) : mysqldump sst fails on maria-10.0-galera
* [Revision #4a6f27a](https://github.com/MariaDB/server/commit/4a6f27a)\
  2014-04-10 23:27:08 -0400
  * Removing unnecessary extra copies of wsrep\_sst\_xxx scripts.
* [Revision #9d91160](https://github.com/MariaDB/server/commit/9d91160)\
  2014-04-09 12:25:47 -0400
  * Fixes for some test failures.
* [Revision #ba7f73f](https://github.com/MariaDB/server/commit/ba7f73f)\
  2014-04-02 22:35:12 -0400\
  \*
  * Merging fix for [Bug #1224775](https://bugs.launchpad.net/bugs/1224775) \* Removing duplicate code
* [Revision #f4defb0](https://github.com/MariaDB/server/commit/f4defb0)\
  2014-03-29 13:34:50 +0200
  * References: [Bug #1299430](https://bugs.launchpad.net/bugs/1299430) - initial support for tokudb replication in master-slave model
* [Revision #a500865](https://github.com/MariaDB/server/commit/a500865)\
  2014-03-27 16:22:57 -0400
  * Merged revision 3471, 3472 & 3473 from maria-5.5-galera.
* [Revision #43c6c2a](https://github.com/MariaDB/server/commit/43c6c2a)\
  2014-03-27 08:22:29 -0400
  * Merged r3468 from maria-5.5-galera.
* [Revision #7fd382f](https://github.com/MariaDB/server/commit/7fd382f)\
  2014-03-27 08:17:24 -0400
  * Merged r3466 from maria-5.5-galera.
* [Revision #8fb80a5](https://github.com/MariaDB/server/commit/8fb80a5)\
  2014-03-27 10:56:11 +0200
  * References [Bug #1280896](https://bugs.launchpad.net/bugs/1280896) - merged the fix from wsrep-5.6 skipping secondary index dupkey checks for applier
* [Revision #c5f7486](https://github.com/MariaDB/server/commit/c5f7486)\
  2014-03-26 14:13:12 -0400
  * bzr merge -r4062..4065 codership/5.6
* [Revision #71dafbf](https://github.com/MariaDB/server/commit/71dafbf)\
  2014-03-26 14:04:50 -0400
  * Merging InnoDB changes to xtradb (r3783..3808).
* [Revision #b5871a5](https://github.com/MariaDB/server/commit/b5871a5)\
  2014-03-26 11:12:38 -0400\
  \*
  * bzr merge -r4027..4061 codership/5.6 \* Merged Innodb changes to xtradb
* [Revision #7d892f6](https://github.com/MariaDB/server/commit/7d892f6)\
  2014-03-25 23:13:30 -0400
  * bzr merge -r4021..4026 codership-mysql/5.6.
* [Revision #0a6924a](https://github.com/MariaDB/server/commit/0a6924a)\
  2014-03-25 17:02:57 -0400
  * Updated WSREP\_PATCH\_REVNO.
* [Revision #899f980](https://github.com/MariaDB/server/commit/899f980)\
  2014-03-25 17:01:05 -0400
  * bzr merge -r3946..3968 codership/5.5
* [Revision #3088d52](https://github.com/MariaDB/server/commit/3088d52)\
  2014-03-25 14:42:15 -0400
  * bzr merge -r3933..3945 codership/5.5 (Non-InnoDB changes only).
* [Revision #3c0b3ba](https://github.com/MariaDB/server/commit/3c0b3ba)\
  2014-03-25 13:39:12 -0400
  * bzr merge -r3928..3932 codership/5.5
* [Revision #586fab7](https://github.com/MariaDB/server/commit/586fab7)\
  2014-03-24 16:40:24 -0400
  * Merging deb/rpm script changes from maria-5.5-galera.
* [Revision #7b57c5e](https://github.com/MariaDB/server/commit/7b57c5e)\
  2014-03-20 16:03:20 +0200
  * References: [MDEV-5908](https://jira.mariadb.org/browse/MDEV-5908) - moved releasing of wsrep THD mutex and thd->awake later, so that wsrep->abort\_pre\_commit() is guaranteed to run for a thread which is still in conflict state
* [Revision #8a99be6](https://github.com/MariaDB/server/commit/8a99be6)\
  2014-03-14 17:52:55 -0400
  * Modified debian scripts to make galera packages self-contained.
* [Revision #ff0f419](https://github.com/MariaDB/server/commit/ff0f419)\
  2014-03-13 11:56:37 -0400
  * Debian script fixes.
* [Revision #27c0952](https://github.com/MariaDB/server/commit/27c0952)\
  2014-03-04 22:10:28 -0500
  * [MDEV-5790](https://jira.mariadb.org/browse/MDEV-5790) : SHOW GLOBAL STATUS LIKE does not show the correct list of variables when using "\_"
* [Revision #87910f7](https://github.com/MariaDB/server/commit/87910f7)\
  2014-02-27 17:56:28 -0500
  * [MDEV-5759](https://jira.mariadb.org/browse/MDEV-5759) Init script contains syntax error
* [Revision #5de274c](https://github.com/MariaDB/server/commit/5de274c)\
  2014-02-19 13:59:10 -0500
  * Fixed install\_macros.cmake to set the correct destination for documentation.
* [Revision #e6a7a38](https://github.com/MariaDB/server/commit/e6a7a38)\
  2014-02-14 17:03:44 -0500\
  \*
  * mysqld\_safe could not start server as it failed trying to perform wsrep position recovery. Fixed by correcting the erroneous mysqld command by properly quoting it.
* [Revision #9564537](https://github.com/MariaDB/server/commit/9564537)\
  2014-02-13 09:33:04 -0500
  * Fixes in debian distribution files.
* [Revision #b0ad00d](https://github.com/MariaDB/server/commit/b0ad00d)\
  2014-02-11 15:03:42 +0200
  * [MDEV-5644](https://jira.mariadb.org/browse/MDEV-5644): Assertion failure during lock\_cancel\_waiting\_and\_release.
* [Revision #65f2f28](https://github.com/MariaDB/server/commit/65f2f28)\
  2014-02-10 09:22:24 -0500
  * [MDEV-5626](https://jira.mariadb.org/browse/MDEV-5626) : Cannot install InnoDB/XtraDB plugin (undefined symbol: wsrep\_md5\_update)
* [Revision #aaf3063](https://github.com/MariaDB/server/commit/aaf3063)\
  2014-02-07 09:14:43 -0500
  * Dummy empty revision (to trigger bb).
* [Revision #324544e](https://github.com/MariaDB/server/commit/324544e)\
  2014-02-03 17:14:38 -0500
  * Fix for main.commit test.
* [Revision #4d254ef](https://github.com/MariaDB/server/commit/4d254ef)\
  2014-01-30 20:27:01 -0500\
  \*
  * Fixed debian dist file names. \* Fixed failing test results. \* Updated tztime.cc ([Bug #1161432](https://bugs.launchpad.net/bugs/1161432)).
* [Revision #4a6be51](https://github.com/MariaDB/server/commit/4a6be51)\
  2014-01-30 12:45:38 -0500\
  \*
  * Merged revisions: 3431, 3435..3457, 3459, 3460 from maria-5.5-galera. \* Fixed Debian/Ubuntu dist files. \* Fixed some compiler warnings.
* [Revision #5b6a4f2](https://github.com/MariaDB/server/commit/5b6a4f2)\
  2014-01-29 08:54:17 +0200
  * Fixed issue on wsrep\_kill\_victim mutexing order error. Furthermore, fixed merge errors found on mysql-test suite testing.
* [Revision #86d4703](https://github.com/MariaDB/server/commit/86d4703)\
  2014-01-28 09:48:51 +0200
  * Fixed issue with extra status lines Wsrep\_local\_bf\_aborts at SHOW GLOBAL STATUS LIKE 'x'; where x != wsrep\_local\_bf\_aborts by changing it as SHOW\_SIMPLE\_FUNC from SHOW\_FUNC.
* [Revision #d0f77b8](https://github.com/MariaDB/server/commit/d0f77b8)\
  2014-01-20 12:17:31 +0200
  * Fixed issue with retrying autocommitted transactions. We might need to clean up the explain structure in this case.
* [Revision #caa1b78](https://github.com/MariaDB/server/commit/caa1b78)\
  2014-01-17 13:55:09 +0200
  * Fixed one compiler warning in wsrep\_applier.cc
* [Revision #a8dbf68](https://github.com/MariaDB/server/commit/a8dbf68)\
  2014-01-17 13:28:43 +0200
  * Added missing files
* [Revision #45f484b](https://github.com/MariaDB/server/commit/45f484b)\
  2013-11-27 22:20:32 +0200
  * fixes for wsrep-5.5 merges
* [Revision #447b19a](https://github.com/MariaDB/server/commit/447b19a)\
  2013-11-27 14:45:32 +0200
  * Ported all remaining storage/innobase changes from lp:codership-mysql/5.6, up tp revision #4021 This is same level as wsrep\_25.1 milestone Note: stotage/xtaradb is not upgraded yet
* [Revision #9642344](https://github.com/MariaDB/server/commit/9642344)\
  2013-11-27 01:10:29 +0200
  * diffed in fix in #3953 from lp:codership-mysql/5.6
* [Revision #ae8f0eb](https://github.com/MariaDB/server/commit/ae8f0eb)\
  2013-11-27 00:54:21 +0200
  * diffed in the fix from revision #3937 from lp:codership-mysql/5.6
* [Revision #9b16346](https://github.com/MariaDB/server/commit/9b16346)\
  2013-11-27 00:44:10 +0200
  * bzr merge -c 3921 lp:codership-mysql/5.6
* [Revision #b098b7a](https://github.com/MariaDB/server/commit/b098b7a)\
  2013-11-27 00:18:44 +0200
  * bzr merge -r3904..3928 lp:codership-mysql/5.5 This is now otherwise on level wsrep-25.9, but storage/innobase has not been fully merged wsrep-5.5 is not good source for that, so we probably have to cherry pick innodb changes from wsrep-5.6
* [Revision #6422d27](https://github.com/MariaDB/server/commit/6422d27)\
  2013-11-26 22:09:14 +0200
  * bzr merge -r3895..3903 lp:codership-mysql/5.5 This is just before 5.5.34 merge in wsrep-5.5 branch
* [Revision #4a11e84](https://github.com/MariaDB/server/commit/4a11e84)\
  2013-11-26 17:03:14 +0200
  * merge from lp:codership-mysql/5.5 rev #3895
* [Revision #a2594e9](https://github.com/MariaDB/server/commit/a2594e9)\
  2013-11-26 16:48:30 +0200
  * Merges from lp:codership-mysql/5.5 up to rev #3893, this changes to wsrep API #24
* [Revision #2b4183f](https://github.com/MariaDB/server/commit/2b4183f)\
  2013-11-06 00:29:37 +0200
  * bzr merge -r3890..3891 lp:codership-mysql/5.5
* [Revision #9129c8f](https://github.com/MariaDB/server/commit/9129c8f)\
  2013-11-06 00:02:22 +0200
  * bzr merge -r3889..3890 lp:codership-mysql/5.5
* [Revision #eec8297](https://github.com/MariaDB/server/commit/eec8297)\
  2013-10-15 12:03:57 +0300
  * Fixed performance schema instrumentation on galera and added correct mutexing when cancelling waiting trx on InnoDB
* [Revision #1a34a56](https://github.com/MariaDB/server/commit/1a34a56)\
  2013-10-14 11:54:27 +0300
  * Fix incorrect merge
* [Revision #8da8c60](https://github.com/MariaDB/server/commit/8da8c60)\
  2013-10-11 16:51:26 +0300
  * Fix temporary table search
* [Revision #37b3d94](https://github.com/MariaDB/server/commit/37b3d94)\
  2013-10-11 12:28:13 +0300
  * Merge fix for DDL handling
* [Revision #a0c8679](https://github.com/MariaDB/server/commit/a0c8679)\
  2013-10-07 20:18:58 +0300
  * Added correct mutexing on trx handling.
* [Revision #f222e7d](https://github.com/MariaDB/server/commit/f222e7d)\
  2013-10-07 11:35:19 +0300
  * Merge fixes, now at level 3430 in mariadb-galera-5.5
* [Revision #61bda9a](https://github.com/MariaDB/server/commit/61bda9a)\
  2013-10-07 09:43:19 +0300
  * Merged revisions 3425..3430 from mariadb-galera-5.5
* [Revision #255e20a](https://github.com/MariaDB/server/commit/255e20a)\
  2013-10-07 08:57:23 +0300
  * Merged revisions 3418..3424 from mariadb-galera-5.5
* [Revision #06a7eeb](https://github.com/MariaDB/server/commit/06a7eeb)\
  2013-10-07 00:18:26 +0300
  * Merged revisions 3411..3417 from mariadb-galera-5.5
* [Revision #337fdb8](https://github.com/MariaDB/server/commit/337fdb8)\
  2013-10-06 23:59:20 +0300
  * Merged revisions 3409..3411 from mariadb-galera-5.5
* [Revision #089f10f](https://github.com/MariaDB/server/commit/089f10f)\
  2013-10-06 23:54:18 +0300
  * Merged #3909 from mariadb-galera-5.5
* [Revision #bfbb0ff](https://github.com/MariaDB/server/commit/bfbb0ff)\
  2013-09-26 14:10:47 +0300
  * Fixed merge error on rollback to savepoint
* [Revision #745239f](https://github.com/MariaDB/server/commit/745239f)\
  2013-09-25 10:42:05 +0300
  * After merge fixes
* [Revision #9c85ced](https://github.com/MariaDB/server/commit/9c85ced)\
  2013-09-09 10:38:58 +0300
  * Merge fix.
* [Revision #0880db5](https://github.com/MariaDB/server/commit/0880db5)\
  2013-09-04 09:54:40 +0300
  * Fix merge error
* [Revision #6e8bfb0](https://github.com/MariaDB/server/commit/6e8bfb0)\
  2013-09-04 08:47:05 +0300
  * Fixed merge errors and XA prepare
* [Revision #81739d3](https://github.com/MariaDB/server/commit/81739d3)\
  2013-07-16 12:09:38 +0300
  * Initial fixes after mariadb 10 merge, basic replication works now
* [Revision #0a92168](https://github.com/MariaDB/server/commit/0a92168)\
  2013-07-13 13:01:13 +0300
  * Initial merge result with mariaDB 10: lp:maria

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
