# MariaDB 10.2.5 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.5)[Release Notes](../../old-releases/10.2/10.2.5.md)[Changelog](mariadb-1025-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 5 Apr 2017

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.5.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2) you can view more details of the revision and view diffs of the code modified in that revision.

* Merge [Revision #ebce682557](https://github.com/MariaDB/server/commit/ebce682557) 2017-04-04 22:00:03 +0300 - Merge ../10.2-mariarocks into 10.2
* [Revision #23b86a18e6](https://github.com/MariaDB/server/commit/23b86a18e6)\
  2017-04-04 17:46:56 +0300
  * MariaRocks: temporarily disable 32-bit Windows builds
* [Revision #15878ee41c](https://github.com/MariaDB/server/commit/15878ee41c)\
  2017-04-04 18:55:18 +0000
  * Windows, compiling : Remove \_DEBUG preprocessor constant, to fix debug build with older cmake.
* Merge [Revision #fb0b3640fe](https://github.com/MariaDB/server/commit/fb0b3640fe) 2017-04-04 17:12:06 +0300 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mariarocks
* [Revision #6d417a0bad](https://github.com/MariaDB/server/commit/6d417a0bad)\
  2017-04-04 08:50:01 +0000
  * Fix aws\_key\_management compilation after mismerge
* Merge [Revision #6e105d7535](https://github.com/MariaDB/server/commit/6e105d7535) 2017-04-04 07:59:25 +0300 - Merge 10.1 into 10.2
* [Revision #9505c96839](https://github.com/MariaDB/server/commit/9505c96839)\
  2017-04-03 19:36:54 +0300
  * [MDEV-12428](https://jira.mariadb.org/browse/MDEV-12428) SIGSEGV in buf\_page\_decrypt\_after\_read() during DDL
* [Revision #ac8218a0be](https://github.com/MariaDB/server/commit/ac8218a0be)\
  2017-03-31 17:40:42 +0200
  * fix Ninja builds for AWS SDK
* [Revision #31896aa6e2](https://github.com/MariaDB/server/commit/31896aa6e2)\
  2017-03-31 15:25:35 +0200
  * put all aws\_key\_management plugin files into plugin/aws\_key\_management
* [Revision #9de7386f6f](https://github.com/MariaDB/server/commit/9de7386f6f)\
  2017-03-31 16:01:37 +0000
  * AWS KMS plugin : Fix building in case AWS C++ SDK was preinstalled into non-standard compiler/linker path (e.g vcpkg on Windows).
* [Revision #00ab154d49](https://github.com/MariaDB/server/commit/00ab154d49)\
  2017-04-03 15:59:38 -0700
  * Fixed bug [MDEV-10454](https://jira.mariadb.org/browse/MDEV-10454).
* [Revision #c85ea1ab6d](https://github.com/MariaDB/server/commit/c85ea1ab6d)\
  2017-04-04 12:39:27 +0300
  * [MDEV-12439](https://jira.mariadb.org/browse/MDEV-12439): (Temporary) Don't run MariaRocks tests under valgrind
* [Revision #d1fc3cc469](https://github.com/MariaDB/server/commit/d1fc3cc469)\
  2017-04-04 12:36:14 +0300
  * MariaRocks: temporarily disable a few failing tests
* Merge [Revision #5e0ed6912f](https://github.com/MariaDB/server/commit/5e0ed6912f) 2017-04-03 13:48:05 +0300 - Merge 10.2 into bb-10.2-mariarocks
* [Revision #c07bb700c8](https://github.com/MariaDB/server/commit/c07bb700c8)\
  2017-03-29 08:08:50 +0300
  * [MDEV-11629](https://jira.mariadb.org/browse/MDEV-11629): Unknown table 'innodb\_cmp\_per\_index\_reset' in
* [Revision #238c6700dd](https://github.com/MariaDB/server/commit/238c6700dd)\
  2017-04-01 18:55:42 +0200
  * include C/C fix for binding of int values to string variables
* [Revision #190591968e](https://github.com/MariaDB/server/commit/190591968e)\
  2017-04-01 18:54:15 +0200
  * vcol.wrong\_arena fails in fulltest
* [Revision #e68f7402c5](https://github.com/MariaDB/server/commit/e68f7402c5)\
  2017-04-01 15:59:45 +0200
  * Avoid TARGET\_LINK\_LIBRARIES() for plugins
* [Revision #22d8bb2706](https://github.com/MariaDB/server/commit/22d8bb2706)\
  2017-04-01 15:58:29 +0200
  * [MDEV-12421](https://jira.mariadb.org/browse/MDEV-12421) Check constraint with query crashes server and renders DB unusable
* [Revision #6315426565](https://github.com/MariaDB/server/commit/6315426565)\
  2017-03-31 19:56:15 +0200
  * restore libmariadb state
* [Revision #124bae082b](https://github.com/MariaDB/server/commit/124bae082b)\
  2017-03-30 13:11:34 +0300
  * [MDEV-12289](https://jira.mariadb.org/browse/MDEV-12289) Keep 128 persistent rollback segments for compatibility and performance
* [Revision #0b9a13a8fc](https://github.com/MariaDB/server/commit/0b9a13a8fc)\
  2017-03-31 15:03:02 +0200
  * update C/C to fix main.mysql\_client\_test\_nonblock failures
* [Revision #6fbcf4134a](https://github.com/MariaDB/server/commit/6fbcf4134a)\
  2017-03-30 15:26:10 +0200
  * properly close the table in fill\_schema\_table\_from\_frm()
* [Revision #2f3d4bd566](https://github.com/MariaDB/server/commit/2f3d4bd566)\
  2017-03-31 15:18:28 +0400
  * [MDEV-12416](https://jira.mariadb.org/browse/MDEV-12416) OOM in create\_virtual\_tmp\_table() makes the server crash
* [Revision #5c66eb5c9f](https://github.com/MariaDB/server/commit/5c66eb5c9f)\
  2017-04-03 10:29:40 +0300
  * Disable compilation of storage/rocksdb/unittest/test\_properties\_collector
* [Revision #44bc2a0ef7](https://github.com/MariaDB/server/commit/44bc2a0ef7)\
  2017-04-02 23:38:28 +0300
  * Post-fixes for "Rename plugin rocksdb\_se to rocksdb"
* [Revision #e7e6e30cb7](https://github.com/MariaDB/server/commit/e7e6e30cb7)\
  2017-04-02 23:14:12 +0300
  * rocksdb\_sys\_vars should not be run if MyRocks is not compiled.
* Merge [Revision #12f7cbc65b](https://github.com/MariaDB/server/commit/12f7cbc65b) 2017-04-02 18:22:39 +0000 - Merge branch 'bb-10.2-mariarocks-wlad' of [server](https://github.com/mariadb/server) into bb-10.2-mariarocks-wlad
* Merge [Revision #9b7ef6f77a](https://github.com/MariaDB/server/commit/9b7ef6f77a) 2017-04-02 12:38:40 +0000 - Merge branch 'bb-10.2-mariarocks' into bb-10.2-mariarocks-wlad
* [Revision #96c48a0d89](https://github.com/MariaDB/server/commit/96c48a0d89)\
  2017-04-02 12:35:59 +0000
  * rocksdb - fix failing tests on Windows
* Merge [Revision #9501c7d06e](https://github.com/MariaDB/server/commit/9501c7d06e) 2017-04-01 16:05:08 +0000 - Merge branch 'bb-10.2-mariarocks' into bb-10.2-mariarocks-wlad
* [Revision #a194390eb8](https://github.com/MariaDB/server/commit/a194390eb8)\
  2017-03-30 13:11:34 +0000
  * Allow to specify C runtime library used for compilation. Default to static release (previously static debug was used in debug builds, but not is appears to be too slow)
* [Revision #ba85f519b9](https://github.com/MariaDB/server/commit/ba85f519b9)\
  2017-04-01 12:39:09 +0000
  * Fixes for innodb crash recovery tests from Serg
* [Revision #df92ba3459](https://github.com/MariaDB/server/commit/df92ba3459)\
  2017-04-01 11:51:24 +0000
  * MariaRocks : Fix looking up sst\_dump
* [Revision #980905c884](https://github.com/MariaDB/server/commit/980905c884)\
  2017-04-01 11:01:36 +0000
  * Fix result files
* Merge [Revision #e6a28b298d](https://github.com/MariaDB/server/commit/e6a28b298d) 2017-04-01 10:55:54 +0000 - Merge branch 'bb-10.2-mariarocks' into bb-10.2-mariarocks-wlad
* [Revision #58bff40d6c](https://github.com/MariaDB/server/commit/58bff40d6c)\
  2017-04-01 10:47:06 +0000
  * Enable MariaRocks test on Buildbot
* [Revision #62ba511314](https://github.com/MariaDB/server/commit/62ba511314)\
  2017-04-01 10:37:36 +0000
  * Fix the build on Windows.
* [Revision #45a9470ff3](https://github.com/MariaDB/server/commit/45a9470ff3)\
  2017-04-02 18:22:22 +0000
  * Rename plugin rocksdb\_se to rocksdb
* [Revision #85a1d9edbe](https://github.com/MariaDB/server/commit/85a1d9edbe)\
  2017-04-02 12:35:59 +0000
  * rocksdb - fix failing tests on Windows
* [Revision #0cca5bdf0b](https://github.com/MariaDB/server/commit/0cca5bdf0b)\
  2017-03-30 13:11:34 +0000
  * Allow to specify C runtime library used for compilation. Default to static release (previously static debug was used in debug builds, but not is appears to be too slow)
* [Revision #099ba3465e](https://github.com/MariaDB/server/commit/099ba3465e)\
  2017-04-01 12:39:09 +0000
  * Fixes for innodb crash recovery tests from Serg
* [Revision #3599b4989d](https://github.com/MariaDB/server/commit/3599b4989d)\
  2017-04-01 11:51:24 +0000
  * MariaRocks : Fix looking up sst\_dump
* [Revision #440addf635](https://github.com/MariaDB/server/commit/440addf635)\
  2017-04-01 10:47:06 +0000
  * Enable MariaRocks test on Buildbot
* [Revision #2be18d9b7f](https://github.com/MariaDB/server/commit/2be18d9b7f)\
  2017-04-01 10:37:36 +0000
  * Fix the build on Windows.
* [Revision #c35a5884b0](https://github.com/MariaDB/server/commit/c35a5884b0)\
  2017-04-02 14:51:59 +0300
  * Mark rocksdb.bulk\_load and rocksdb.add\_index\_inplace\_sstfilewriter as big
* [Revision #0aa056f642](https://github.com/MariaDB/server/commit/0aa056f642)\
  2017-04-02 13:12:19 +0300
  * Disable persistent\_cache.test due to upstream MyRocks issue #579.
* [Revision #20d9fbcf9a](https://github.com/MariaDB/server/commit/20d9fbcf9a)\
  2017-04-02 12:18:23 +0300
  * [MDEV-12424](https://jira.mariadb.org/browse/MDEV-12424): binlog\_encryption.encrypted\_\* tests fail with Can't locate autodie.pm error
* [Revision #74889de426](https://github.com/MariaDB/server/commit/74889de426)\
  2017-04-01 16:11:19 +0300
  * Apply a workaround for MyRocks upstream issue #569
* [Revision #92c24fda08](https://github.com/MariaDB/server/commit/92c24fda08)\
  2017-04-01 11:01:36 +0000
  * Fix result files
* [Revision #9cdc6bcfe4](https://github.com/MariaDB/server/commit/9cdc6bcfe4)\
  2017-04-01 12:56:45 +0300
  * Update test results after changes in search\_pattern\_in\_file.inc
* [Revision #321f5d9d70](https://github.com/MariaDB/server/commit/321f5d9d70)\
  2017-04-01 10:12:28 +0300
  * Fix debian architecture parsing
* [Revision #788382f77a](https://github.com/MariaDB/server/commit/788382f77a)\
  2017-04-01 06:32:20 +0300
  * Fix coompilation on windows
* [Revision #16a99c5ad9](https://github.com/MariaDB/server/commit/16a99c5ad9)\
  2017-03-31 16:28:27 +0200
  * MariaRocks tests: various cleanups
* [Revision #b2865a437f](https://github.com/MariaDB/server/commit/b2865a437f)\
  2017-03-14 15:36:30 +0100
  * search\_pattern\_in\_file.inc changes
* [Revision #d6d994bf42](https://github.com/MariaDB/server/commit/d6d994bf42)\
  2017-03-12 11:18:51 +0100
  * remove two redundant \*.inc files to restart a server
* [Revision #143e771dee](https://github.com/MariaDB/server/commit/143e771dee)\
  2017-03-13 10:18:15 +0100
  * ha\_start\_consistent\_snapshot() did not check for errors
* [Revision #6e899642fe](https://github.com/MariaDB/server/commit/6e899642fe)\
  2017-03-11 16:25:03 +0100
  * move rocksdb specific changes into rocksdb
* [Revision #9ce639af52](https://github.com/MariaDB/server/commit/9ce639af52)\
  2017-03-10 19:41:48 +0100
  * don't export all charsets to plugins
* [Revision #76a262cdf8](https://github.com/MariaDB/server/commit/76a262cdf8)\
  2017-03-10 19:41:35 +0100
  * remove my\_hash\_const\_element(), use Hash\_set in C++ code
* [Revision #63798a6ea8](https://github.com/MariaDB/server/commit/63798a6ea8)\
  2017-03-13 10:21:00 +0100
  * remove DB\_TYPE\_ROCKSDB
* [Revision #dd3b7ad10f](https://github.com/MariaDB/server/commit/dd3b7ad10f)\
  2017-03-31 14:06:28 +0000
  * MariaRocks : Run rocksdb suite on Windows
* [Revision #54a892e133](https://github.com/MariaDB/server/commit/54a892e133)\
  2017-03-31 01:32:59 +0300
  * Post-merge fixes
* Merge [Revision #5210c69e71](https://github.com/MariaDB/server/commit/5210c69e71) 2017-03-31 01:14:00 +0300 - Merge 10.2 into bb-10.2-mariarocks
* [Revision #a0c79bcf00](https://github.com/MariaDB/server/commit/a0c79bcf00)\
  2017-03-30 08:46:12 +0300
  * Rename InnoDB transaction undo logging predicates.
* [Revision #d1374c5b77](https://github.com/MariaDB/server/commit/d1374c5b77)\
  2017-03-30 14:34:45 +0300
  * [MDEV-12345](https://jira.mariadb.org/browse/MDEV-12345) post-merge fix.
* [Revision #72c6af8d1a](https://github.com/MariaDB/server/commit/72c6af8d1a)\
  2017-03-30 13:12:57 +0200
  * disable failing test, see [MDEV-11420](https://jira.mariadb.org/browse/MDEV-11420)
* Merge [Revision #da4d71d10d](https://github.com/MariaDB/server/commit/da4d71d10d) 2017-03-30 12:48:42 +0200 - Merge branch '10.1' into 10.2
* [Revision #a00517ac97](https://github.com/MariaDB/server/commit/a00517ac97)\
  2017-03-28 19:34:51 +0200
  * restore the correct linking of ed25519 plugin
* [Revision #9ab9a28b5d](https://github.com/MariaDB/server/commit/9ab9a28b5d)\
  2017-03-27 11:04:06 +0200
  * disable innodb snappy for release builds
* [Revision #c56b896c17](https://github.com/MariaDB/server/commit/c56b896c17)\
  2017-03-28 12:28:09 +0300
  * Fix test failure on debug\_key\_management test.
* Merge [Revision #ba298b1f02](https://github.com/MariaDB/server/commit/ba298b1f02) 2017-03-24 18:20:09 +0200 - Merge 10.0 into 10.1
* Merge [Revision #c51fc679f5](https://github.com/MariaDB/server/commit/c51fc679f5) 2017-03-24 18:19:15 +0200 - Merge 5.5 into 10.0
* [Revision #a821ef7605](https://github.com/MariaDB/server/commit/a821ef7605)\
  2017-03-24 18:01:56 +0200
  * [MDEV-11802](https://jira.mariadb.org/browse/MDEV-11802) innodb.innodb\_bug14676111 fails on buildbot
* [Revision #716188f1d4](https://github.com/MariaDB/server/commit/716188f1d4)\
  2017-03-24 10:02:31 +0100
  * Fix some warnings on Windows compilation - silence warnings in ed25519 reference implementation - fix signed/unsigned warning in popular header item\_func.h
* [Revision #d7c35a9992](https://github.com/MariaDB/server/commit/d7c35a9992)\
  2017-03-23 19:28:36 +0000
  * Fix compiler error
* [Revision #e5b67a46bc](https://github.com/MariaDB/server/commit/e5b67a46bc)\
  2017-03-23 11:48:56 +0000
  * [MDEV-12345](https://jira.mariadb.org/browse/MDEV-12345) Performance : replace calls to clock() inside trx\_start\_low() by THD::start\_utime
* Merge [Revision #09a2107b1b](https://github.com/MariaDB/server/commit/09a2107b1b) 2017-03-21 19:20:44 +0100 - Merge branch '10.0' into 10.1
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
* [Revision #bbf0c9d4c3](https://github.com/MariaDB/server/commit/bbf0c9d4c3)\
  2017-03-16 09:07:20 +0100
  * cleanup: pfs\_upgrade\* tests
* [Revision #386ef08704](https://github.com/MariaDB/server/commit/386ef08704)\
  2017-03-13 10:54:08 +0100
  * [MDEV-12233](https://jira.mariadb.org/browse/MDEV-12233) main.mysql\_upgrade\_noengine fails in buildbot on ppc64le
* [Revision #b1ec35b903](https://github.com/MariaDB/server/commit/b1ec35b903)\
  2017-03-16 17:30:13 +0200
  * Add assertions when key rotation list is used.
* [Revision #c333cae652](https://github.com/MariaDB/server/commit/c333cae652)\
  2017-03-16 13:35:36 +0200
  * [MDEV-11964](https://jira.mariadb.org/browse/MDEV-11964) Add more stub missing man pages
* [Revision #854359ffc5](https://github.com/MariaDB/server/commit/854359ffc5)\
  2017-03-14 20:44:25 +0000
  * Fix AWS KMS plugin's compile error
* [Revision #50eb40a2a8](https://github.com/MariaDB/server/commit/50eb40a2a8)\
  2017-03-14 12:56:01 +0200
  * [MDEV-11738](https://jira.mariadb.org/browse/MDEV-11738): Mariadb uses 100% of several of my 8 cpus doing nothing
* [Revision #a2f34809e5](https://github.com/MariaDB/server/commit/a2f34809e5)\
  2017-03-14 09:56:05 -0400
  * bump the VERSION
* [Revision #98be67266d](https://github.com/MariaDB/server/commit/98be67266d)\
  2017-03-13 23:13:24 +0000
  * Fix truncation of affected rows and insert id in select\_insert::send\_ok\_packet
* Merge [Revision #9dc10d5851](https://github.com/MariaDB/server/commit/9dc10d5851) 2017-03-13 19:17:34 +0200 - Merge 10.0 into 10.1
* [Revision #032678ad18](https://github.com/MariaDB/server/commit/032678ad18)\
  2017-03-10 18:33:38 +0200
  * [MDEV-12091](https://jira.mariadb.org/browse/MDEV-12091) Shutdown fails to wait for rollback of recovered transactions to finish
* [Revision #68be011cf2](https://github.com/MariaDB/server/commit/68be011cf2)\
  2017-03-11 20:59:52 +0200
  * Updated list of unstable tests for 10.1.22
* [Revision #2033844319](https://github.com/MariaDB/server/commit/2033844319)\
  2017-03-11 12:42:55 +0100
  * test failures in buildbot
* [Revision #f0ec34002a](https://github.com/MariaDB/server/commit/f0ec34002a)\
  2017-02-10 13:26:55 +0200
  * Correct FSF address
* [Revision #2a0ae1c90a](https://github.com/MariaDB/server/commit/2a0ae1c90a)\
  2017-03-07 19:21:42 +0100
  * [MDEV-11965](https://jira.mariadb.org/browse/MDEV-11965) -Werror should not appear in released tarballs
* [Revision #5d40ed864e](https://github.com/MariaDB/server/commit/5d40ed864e)\
  2017-03-07 19:17:37 +0100
  * [MDEV-11752](https://jira.mariadb.org/browse/MDEV-11752) Unsafe strmov - function definition in include/m\_string.h
* [Revision #e0a03ca30a](https://github.com/MariaDB/server/commit/e0a03ca30a)\
  2017-03-06 01:27:34 +0100
  * ed25519 plugin: simplify the api
* [Revision #7120118a5e](https://github.com/MariaDB/server/commit/7120118a5e)\
  2017-03-05 16:18:16 +0100
  * [MDEV-12160](https://jira.mariadb.org/browse/MDEV-12160) Modern alternative to the SHA1 authentication plugin
* [Revision #269ab56f8b](https://github.com/MariaDB/server/commit/269ab56f8b)\
  2017-03-06 22:42:00 +0100
  * small plugin API related fixes
* [Revision #227f63db3b](https://github.com/MariaDB/server/commit/227f63db3b)\
  2017-03-06 19:37:48 +0100
  * cleanup: sort various lists of services
* [Revision #0877eff401](https://github.com/MariaDB/server/commit/0877eff401)\
  2017-03-06 19:34:22 +0100
  * thd\_rnd service
* [Revision #6305533de2](https://github.com/MariaDB/server/commit/6305533de2)\
  2017-03-06 17:32:18 +0100
  * Auth Plugin API: add THD to MYSQL\_SERVER\_AUTH\_INFO
* [Revision #051851b9a6](https://github.com/MariaDB/server/commit/051851b9a6)\
  2017-03-06 17:05:03 +0100
  * base64 service
* [Revision #70a2efde03](https://github.com/MariaDB/server/commit/70a2efde03)\
  2017-03-06 15:31:25 +0100
  * remove old API for SHA2
* [Revision #d6a7aece08](https://github.com/MariaDB/server/commit/d6a7aece08)\
  2017-03-06 13:06:03 +0100
  * my\_sha2 service
* [Revision #bd1139ad27](https://github.com/MariaDB/server/commit/bd1139ad27)\
  2017-03-06 12:45:36 +0100
  * cleanup: generalize my\_sha1.cc
* [Revision #6cddd12ad6](https://github.com/MariaDB/server/commit/6cddd12ad6)\
  2017-03-05 15:50:32 +0100
  * make sql\_udf.cc to shorten dlerror() messages
* [Revision #2b1bbac5fa](https://github.com/MariaDB/server/commit/2b1bbac5fa)\
  2017-03-05 20:51:31 +0100
  * cleanup: remove a duplicate file
* [Revision #aa51b559ab](https://github.com/MariaDB/server/commit/aa51b559ab)\
  2017-03-06 15:07:46 +0100
  * typo fixed
* [Revision #0633d0e2ed](https://github.com/MariaDB/server/commit/0633d0e2ed)\
  2017-03-08 14:54:12 +0100
  * don't show 'performance\_schema\_%\_classes\_lost' variables in tests
* [Revision #3d06f0f72c](https://github.com/MariaDB/server/commit/3d06f0f72c)\
  2017-03-04 17:17:00 +0100
  * [MDEV-11942](https://jira.mariadb.org/browse/MDEV-11942) BLACKHOLE is no longer active in 10.1 by default, mysql\_upgrade not handling the situation
* [Revision #c372388e48](https://github.com/MariaDB/server/commit/c372388e48)\
  2017-02-07 22:56:28 +0100
  * make mysql\_upgrade try to install missing storage engine plugins ([MDEV-11942](https://jira.mariadb.org/browse/MDEV-11942))
* [Revision #8f1ca5e311](https://github.com/MariaDB/server/commit/8f1ca5e311)\
  2017-03-03 15:27:19 +0100
  * [MDEV-11943](https://jira.mariadb.org/browse/MDEV-11943) I\_S.TABLES inconsistencies with tables with unknown storage engine
* [Revision #48b1d17534](https://github.com/MariaDB/server/commit/48b1d17534)\
  2017-03-02 15:36:18 +0100
  * [MDEV-11943](https://jira.mariadb.org/browse/MDEV-11943) I\_S.TABLES inconsistencies with tables with unknown storage engine
* [Revision #25c32c89f1](https://github.com/MariaDB/server/commit/25c32c89f1)\
  2017-03-02 14:04:14 +0100
  * trivial cleanup
* [Revision #8eb66bc382](https://github.com/MariaDB/server/commit/8eb66bc382)\
  2017-03-02 20:59:29 +0100
  * cleanup: change dd\_frm\_type() to return the engine name, not legacy\_db\_type
* [Revision #1c8d2121ab](https://github.com/MariaDB/server/commit/1c8d2121ab)\
  2017-03-02 06:53:07 +0100
  * don't do vio\_description(NULL)
* [Revision #5fa04aae9e](https://github.com/MariaDB/server/commit/5fa04aae9e)\
  2017-03-01 23:52:35 +0100
  * [MDEV-11842](https://jira.mariadb.org/browse/MDEV-11842) Fail to insert on a table where a field has no default
* [Revision #b6a1d6538b](https://github.com/MariaDB/server/commit/b6a1d6538b)\
  2017-03-10 16:25:01 +0100
  * compiler warnings
* Merge [Revision #0094b6581d](https://github.com/MariaDB/server/commit/0094b6581d) 2017-03-10 15:16:13 +0200 - Merge 10.0 into 10.1
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
* [Revision #814d050760](https://github.com/MariaDB/server/commit/814d050760)\
  2017-03-10 14:07:22 +0200
  * [MDEV-12215](https://jira.mariadb.org/browse/MDEV-12215): main.repair\_symlink-5543 fails in buildbot
* [Revision #18de829618](https://github.com/MariaDB/server/commit/18de829618)\
  2017-03-09 13:18:40 +0200
  * [MDEV-11964](https://jira.mariadb.org/browse/MDEV-11964) Add missing stub manpages
* [Revision #07d89fa59c](https://github.com/MariaDB/server/commit/07d89fa59c)\
  2017-03-09 16:52:57 +0200
  * Remove leftover merge conflict marker
* [Revision #5aacb861f2](https://github.com/MariaDB/server/commit/5aacb861f2)\
  2017-03-09 14:45:52 +0200
  * WSREP: Use TRX\_ID\_FMT for trx\_id\_t in messages.
* [Revision #b28adb6a62](https://github.com/MariaDB/server/commit/b28adb6a62)\
  2017-03-09 15:09:44 +0200
  * Fix an error introduced in the previous commit.
* [Revision #498f4a825b](https://github.com/MariaDB/server/commit/498f4a825b)\
  2017-03-09 08:54:07 +0200
  * Fix InnoDB/XtraDB compilation warnings on 32-bit builds.
* Merge [Revision #ad0c218a44](https://github.com/MariaDB/server/commit/ad0c218a44) 2017-03-08 19:44:22 +0200 - Merge 10.0 into 10.1
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
* Merge [Revision #c4f3e64c23](https://github.com/MariaDB/server/commit/c4f3e64c23) 2017-03-06 21:50:42 +0200 - Merge branch 'bb-10.0-vicentiu' into 10.0
* [Revision #dc1c9e69d0](https://github.com/MariaDB/server/commit/dc1c9e69d0)\
  2017-03-06 19:25:22 +0200
  * Make tokudb report ENOENT when renaming table to nonexistant DB
* [Revision #3da916246f](https://github.com/MariaDB/server/commit/3da916246f)\
  2017-03-06 19:17:15 +0200
  * Revert "Add extra HA\_ERR message that Percona introduced within TokuDB 5.6.35-80"
* [Revision #9741017b1f](https://github.com/MariaDB/server/commit/9741017b1f)\
  2017-03-05 15:17:23 +0200
  * Disable 2 tokudb tests
* [Revision #7bf914e157](https://github.com/MariaDB/server/commit/7bf914e157)\
  2017-03-05 14:50:03 +0200
  * rpl\_extra\_col\_slave\_tokudb changes result set
* [Revision #97041acf7f](https://github.com/MariaDB/server/commit/97041acf7f)\
  2017-03-05 14:32:30 +0200
  * Fix tokudb.gap\_lock\_error test
* [Revision #4c3b732d9f](https://github.com/MariaDB/server/commit/4c3b732d9f)\
  2017-03-05 12:26:32 +0200
  * Updated list of unstable tests for 10.0.30 release
* Merge [Revision #1cac281ebe](https://github.com/MariaDB/server/commit/1cac281ebe) 2017-03-05 02:44:39 +0200 - Merge branch 'merge-pcre' into 10.0
* [Revision #dfd7749120](https://github.com/MariaDB/server/commit/dfd7749120)\
  2017-03-05 02:27:59 +0200
  * 8.40
* Merge [Revision #895b253963](https://github.com/MariaDB/server/commit/895b253963) 2017-03-05 02:22:40 +0200 - Merge remote-tracking branch 'connect/10.0' into 10.0
* [Revision #b2956b2ab4](https://github.com/MariaDB/server/commit/b2956b2ab4)\
  2017-03-02 12:12:53 +0100
  * Update version number and date modified: storage/connect/ha\_connect.cc
* [Revision #d75e5e6e26](https://github.com/MariaDB/server/commit/d75e5e6e26)\
  2017-02-24 23:21:20 +0100
  * Fix crashing when joining two JDBC tables.. Was in close (the virtual machine could have been detached. modified: storage/connect/jdbconn.cpp
* [Revision #6f34d8807c](https://github.com/MariaDB/server/commit/6f34d8807c)\
  2017-02-16 18:01:48 +0100
  * All changes made on 10.1
* [Revision #82913b0e90](https://github.com/MariaDB/server/commit/82913b0e90)\
  2017-01-17 19:39:49 +0100
  * Commit changes made for version 10.1
* [Revision #fa59ac5055](https://github.com/MariaDB/server/commit/fa59ac5055)\
  2017-03-05 02:01:49 +0200
  * Add extra HA\_ERR message that Percona introduced within TokuDB 5.6.35-80
* Merge [Revision #b7a3bce06e](https://github.com/MariaDB/server/commit/b7a3bce06e) 2017-03-05 02:01:21 +0200 - Merge branch 'merge-tokudb-5.6' into 10.0
* [Revision #d71df7e1db](https://github.com/MariaDB/server/commit/d71df7e1db)\
  2017-03-05 01:31:32 +0200
  * 5.6.35-80.0
* [Revision #5139c4b688](https://github.com/MariaDB/server/commit/5139c4b688)\
  2017-03-05 01:06:01 +0200
  * Update xtradb version to match the merged one
* [Revision #5d0c123007](https://github.com/MariaDB/server/commit/5d0c123007)\
  2017-03-05 01:00:21 +0200
  * Add missing sys\_var test for innodb\_stats\_include\_delete\_marked
* Merge [Revision #83da1a1e57](https://github.com/MariaDB/server/commit/83da1a1e57) 2017-03-05 00:59:57 +0200 - Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #8d69ce7b82](https://github.com/MariaDB/server/commit/8d69ce7b82)\
  2017-03-04 20:49:14 +0200
  * 5.6.35-80.0
* [Revision #f4806772d3](https://github.com/MariaDB/server/commit/f4806772d3)\
  2017-03-03 20:16:16 +0200
  * Add missing DBUG\_RETURN
* [Revision #606a4a4847](https://github.com/MariaDB/server/commit/606a4a4847)\
  2017-03-03 20:12:48 +0200
  * Post [MDEV-11902](https://jira.mariadb.org/browse/MDEV-11902) Fix test failures in maria and myisam storage engines
* Merge [Revision #1acfa942ed](https://github.com/MariaDB/server/commit/1acfa942ed) 2017-03-03 01:37:54 +0200 - Merge branch '5.5' into 10.0
* [Revision #5a0fff50f8](https://github.com/MariaDB/server/commit/5a0fff50f8)\
  2017-02-26 15:40:18 -0800
  * Fixed bug [MDEV-12099](https://jira.mariadb.org/browse/MDEV-12099).
* [Revision #199f88cb9c](https://github.com/MariaDB/server/commit/199f88cb9c)\
  2017-02-23 12:48:15 +0100
  * [MDEV-5999](https://jira.mariadb.org/browse/MDEV-5999) MySQL Bug#12766319 - 61865: RENAME USER DOES NOT WORK CORRECTLY - REQUIRES FLUSH PRIVILEGES
* [Revision #494a94158a](https://github.com/MariaDB/server/commit/494a94158a)\
  2017-02-23 12:41:13 +0100
  * Fix for bug#11759114 - '51401: GRANT TREATS NONEXISTENT FUNCTIONS/PRIVILEGES DIFFERENTLY'.
* [Revision #0a480f03c6](https://github.com/MariaDB/server/commit/0a480f03c6)\
  2017-02-23 10:37:02 +0100
  * delete the installation warning for CentOS4/RHEL4
* [Revision #2c354e7468](https://github.com/MariaDB/server/commit/2c354e7468)\
  2017-02-23 10:34:51 +0100
  * [MDEV-11789](https://jira.mariadb.org/browse/MDEV-11789) MariaDB fails to restart after 10.0.29-1.el7 update
* [Revision #713d513624](https://github.com/MariaDB/server/commit/713d513624)\
  2017-02-23 10:32:34 +0100
  * [MDEV-12074](https://jira.mariadb.org/browse/MDEV-12074) selinux build failure on Fedora 24
* [Revision #831b531895](https://github.com/MariaDB/server/commit/831b531895)\
  2017-02-22 15:22:22 +0100
  * [MDEV-10788](https://jira.mariadb.org/browse/MDEV-10788) Not able to compile source with -DBUILD\_CONFIG=mysql\_release -DCMAKE\_BUILD\_TYPE=Debug
* [Revision #44534487d4](https://github.com/MariaDB/server/commit/44534487d4)\
  2017-02-21 11:07:42 +0100
  * [MDEV-11505](https://jira.mariadb.org/browse/MDEV-11505) wrong databasename in mysqldump comment
* [Revision #d72dbb4122](https://github.com/MariaDB/server/commit/d72dbb4122)\
  2017-02-20 22:40:47 +0100
  * bugfix: remove my\_delete\_with\_symlink()
* [Revision #955f2f036d](https://github.com/MariaDB/server/commit/955f2f036d)\
  2017-02-20 19:53:12 +0100
  * race-condition safe implementation of test\_if\_data\_home\_dir()
* [Revision #93cb0246b8](https://github.com/MariaDB/server/commit/93cb0246b8)\
  2017-02-20 11:07:38 +0100
  * race-condition safe implementation of mi\_delete\_table/maria\_delete\_table
* [Revision #6d50324558](https://github.com/MariaDB/server/commit/6d50324558)\
  2017-02-20 22:41:17 +0100
  * support MY\_NOSYMLINKS in my\_delete()
* [Revision #f2d24ea68b](https://github.com/MariaDB/server/commit/f2d24ea68b)\
  2017-02-20 13:39:54 +0100
  * compilation failure
* [Revision #b6862c914f](https://github.com/MariaDB/server/commit/b6862c914f)\
  2017-02-18 15:18:35 +0100
  * cleanup: remove now-unused argument
* [Revision #b27fd90ad3](https://github.com/MariaDB/server/commit/b27fd90ad3)\
  2017-02-15 18:45:19 +0100
  * [MDEV-11902](https://jira.mariadb.org/browse/MDEV-11902) mi\_open race condition
* [Revision #d78d0d459d](https://github.com/MariaDB/server/commit/d78d0d459d)\
  2017-02-18 10:38:14 +0100
  * cleanup: NO\_OPEN\_3 was never defined
* [Revision #8722d4b8d2](https://github.com/MariaDB/server/commit/8722d4b8d2)\
  2017-02-18 10:20:15 +0100
  * cleanup: remove 16-year-old "TODO"
* [Revision #c826ac9d53](https://github.com/MariaDB/server/commit/c826ac9d53)\
  2017-02-18 10:10:34 +0100
  * cleanup: mysys\_test\_invalid\_symlink
* [Revision #24d8bc707a](https://github.com/MariaDB/server/commit/24d8bc707a)\
  2017-02-18 10:08:49 +0100
  * cleanup: my\_register\_filename()
* [Revision #3cba74e032](https://github.com/MariaDB/server/commit/3cba74e032)\
  2017-02-18 10:01:31 +0100
  * cleanup: fn\_format, remove dead code
* [Revision #924a81a548](https://github.com/MariaDB/server/commit/924a81a548)\
  2017-02-18 15:06:25 +0100
  * bugfix: DEBUG\_SYNC() invoked with no THD
* [Revision #8897b50dca](https://github.com/MariaDB/server/commit/8897b50dca)\
  2017-02-16 13:24:00 +0100
  * [MDEV-11525](https://jira.mariadb.org/browse/MDEV-11525) Assertion \`cp + len <= buff + buff\_size' failed in JOIN\_CACHE::write\_record\_data
* [Revision #eef2101489](https://github.com/MariaDB/server/commit/eef2101489)\
  2017-02-16 11:32:47 +0100
  * [MDEV-11933](https://jira.mariadb.org/browse/MDEV-11933) Wrong usage of linked list in mysql\_prune\_stmt\_list
* [Revision #ac78927aef](https://github.com/MariaDB/server/commit/ac78927aef)\
  2017-02-24 00:10:08 -0800
  * Fixed bug [MDEV-7992](https://jira.mariadb.org/browse/MDEV-7992).
* [Revision #bdb672fe96](https://github.com/MariaDB/server/commit/bdb672fe96)\
  2017-02-23 19:46:10 +0200
  * [MDEV-12120](https://jira.mariadb.org/browse/MDEV-12120) tokudb\_bugs.xa-N tests fail with timeout on valgrind
* [Revision #365c4e971a](https://github.com/MariaDB/server/commit/365c4e971a)\
  2017-02-22 10:03:33 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520)/[MDEV-5746](https://jira.mariadb.org/browse/MDEV-5746) post-fix: Do not posix\_fallocate() too much.
* [Revision #6de50b2c7f](https://github.com/MariaDB/server/commit/6de50b2c7f)\
  2017-02-22 09:17:30 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) post-fixes
* [Revision #32591b750f](https://github.com/MariaDB/server/commit/32591b750f)\
  2017-02-22 11:40:01 +0530
  * [MDEV-11718](https://jira.mariadb.org/browse/MDEV-11718) 5.5 rpl and federated tests massively fail in buildbot with valgrind
* [Revision #cf673adee2](https://github.com/MariaDB/server/commit/cf673adee2)\
  2017-02-22 01:36:16 +0400
  * [MDEV-10418](https://jira.mariadb.org/browse/MDEV-10418) Assertion \`m\_extra\_cache' failed in ha\_partition::late\_extra\_cache(uint).
* [Revision #978179a9d4](https://github.com/MariaDB/server/commit/978179a9d4)\
  2017-02-20 17:58:42 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) Extending an InnoDB data file unnecessarily allocates a large memory buffer on Windows
* [Revision #2bfe83adec](https://github.com/MariaDB/server/commit/2bfe83adec)\
  2017-02-20 17:16:59 +0200
  * Remove a bogus Valgrind "suppression".
* [Revision #5ddfcb05ca](https://github.com/MariaDB/server/commit/5ddfcb05ca)\
  2017-02-17 13:37:18 +0100
  * [MDEV-9455](https://jira.mariadb.org/browse/MDEV-9455): \[ERROR] mysqld got signal 11
* [Revision #1b7aae90fb](https://github.com/MariaDB/server/commit/1b7aae90fb)\
  2017-02-20 18:22:01 +0400
  * [MDEV-11904](https://jira.mariadb.org/browse/MDEV-11904) Make Audit Plugin working with MySQL 8.0.
* [Revision #6364adb199](https://github.com/MariaDB/server/commit/6364adb199)\
  2017-02-18 20:39:49 +0200
  * [MDEV-10621](https://jira.mariadb.org/browse/MDEV-10621) parts.partition\_float\_myisam failed with timeout in buildbot
* [Revision #f49375fddf](https://github.com/MariaDB/server/commit/f49375fddf)\
  2017-02-16 23:44:54 -0800
  * Fixed bug [MDEV-9028](https://jira.mariadb.org/browse/MDEV-9028).
* [Revision #b70cd26d73](https://github.com/MariaDB/server/commit/b70cd26d73)\
  2017-02-17 00:57:24 +0200
  * [MDEV-11668](https://jira.mariadb.org/browse/MDEV-11668) rpl.rpl\_heartbeat\_basic fails sporadically in buildbot
* [Revision #29d78dbb44](https://github.com/MariaDB/server/commit/29d78dbb44)\
  2017-02-12 23:19:48 +0600
  * minor typo in a description of mysql\_parse()
* [Revision #108b211ee2](https://github.com/MariaDB/server/commit/108b211ee2)\
  2017-02-16 12:02:31 +0200
  * Fix gcc 6.3.x compiler warnings.
* [Revision #2e8fa1c2b2](https://github.com/MariaDB/server/commit/2e8fa1c2b2)\
  2017-02-13 17:29:32 -0500
  * [MDEV-12058](https://jira.mariadb.org/browse/MDEV-12058): MariaDB Test Suite issue with test sys\_vars.secure\_file\_priv.test
* [Revision #60c932a3d0](https://github.com/MariaDB/server/commit/60c932a3d0)\
  2017-01-27 16:47:00 +0200
  * backported build-tags from 10.2 to ensure that 'make tags' works again with xemacs
* [Revision #5c9baf54e7](https://github.com/MariaDB/server/commit/5c9baf54e7)\
  2017-01-27 16:46:26 +0200
  * Fix for memory leak in applications, like QT,that calls my\_thread\_global\_init() + my\_thrad\_global\_end() repeatadily. This caused THR\_KEY\_mysys to be allocated multiple times.
* [Revision #46eef1ede2](https://github.com/MariaDB/server/commit/46eef1ede2)\
  2017-01-23 19:40:22 -0800
  * Fixed bug [MDEV-11859](https://jira.mariadb.org/browse/MDEV-11859).
* [Revision #f003cc8a35](https://github.com/MariaDB/server/commit/f003cc8a35)\
  2017-01-18 11:42:41 -0800
  * Fixed bug [MDEV-8603](https://jira.mariadb.org/browse/MDEV-8603).
* [Revision #bb4ef470c2](https://github.com/MariaDB/server/commit/bb4ef470c2)\
  2017-03-08 17:35:55 +0200
  * Minor wording fix in mysqladmin man page
* [Revision #19629ebf81](https://github.com/MariaDB/server/commit/19629ebf81)\
  2017-03-07 15:06:01 +0400
  * [MDEV-10646](https://jira.mariadb.org/browse/MDEV-10646) - System Unit File After network-online
* [Revision #fa137476ff](https://github.com/MariaDB/server/commit/fa137476ff)\
  2017-03-03 12:33:24 +0400
  * [MDEV-11941](https://jira.mariadb.org/browse/MDEV-11941) - Lintian complains about executable bits
* [Revision #aeff61ee58](https://github.com/MariaDB/server/commit/aeff61ee58)\
  2017-03-07 17:27:27 +0400
  * [MDEV-12064](https://jira.mariadb.org/browse/MDEV-12064) Bug#18411494 WRONG COMPARSION ON BIG DECIMAL VALUES.
* [Revision #ea31755760](https://github.com/MariaDB/server/commit/ea31755760)\
  2017-01-05 12:07:26 +0100
  * properly set paths in systemd unit files
* [Revision #dbd1d7ea8e](https://github.com/MariaDB/server/commit/dbd1d7ea8e)\
  2017-01-23 11:58:41 +0100
  * Updated innotop on debian/additions from 1.7.1 to 1.11.4
* [Revision #7be541f281](https://github.com/MariaDB/server/commit/7be541f281)\
  2017-02-26 16:49:47 +0100
  * spelling fixes
* [Revision #e823023e4b](https://github.com/MariaDB/server/commit/e823023e4b)\
  2015-04-21 08:32:31 +0200
  * Bug#18411494 WRONG COMPARSION ON BIG DECIMAL VALUES
* [Revision #68d632bc5a](https://github.com/MariaDB/server/commit/68d632bc5a)\
  2017-03-06 10:02:01 +0200
  * Replace some functions with macros.
* Merge [Revision #adc91387e3](https://github.com/MariaDB/server/commit/adc91387e3) 2017-03-03 13:27:12 +0200 - Merge 10.0 into 10.1
* [Revision #29c776cfd1](https://github.com/MariaDB/server/commit/29c776cfd1)\
  2017-03-03 12:03:33 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520): Retry posix\_fallocate() after EINTR.
* [Revision #d04d835f64](https://github.com/MariaDB/server/commit/d04d835f64)\
  2017-02-28 22:26:53 +1100
  * [MDEV-11610](https://jira.mariadb.org/browse/MDEV-11610): support-files/mysql-log-rotate.sh not binlog either
* [Revision #156cf86def](https://github.com/MariaDB/server/commit/156cf86def)\
  2017-02-28 21:47:44 +1100
  * [MDEV-11610](https://jira.mariadb.org/browse/MDEV-11610): Alter Debian log rotate to not rotate binary/relay logs
* [Revision #0af8b565f2](https://github.com/MariaDB/server/commit/0af8b565f2)\
  2017-02-28 21:39:34 +1100
  * [MDEV-11610](https://jira.mariadb.org/browse/MDEV-11610): mysqladmin flush-X-log options
* [Revision #33c1f20d8e](https://github.com/MariaDB/server/commit/33c1f20d8e)\
  2017-02-28 20:21:19 +1100
  * [MDEV-11610](https://jira.mariadb.org/browse/MDEV-11610): Add --local to mysqladmin
* [Revision #659047b820](https://github.com/MariaDB/server/commit/659047b820)\
  2017-01-23 08:34:59 +1100
  * [MDEV-11386](https://jira.mariadb.org/browse/MDEV-11386): Advance Toochain library cache workaround (temporary)
* [Revision #71f53bf72d](https://github.com/MariaDB/server/commit/71f53bf72d)\
  2017-03-02 12:35:31 +0400
  * [MDEV-11221](https://jira.mariadb.org/browse/MDEV-11221) - main.events\_restart failed in bb
* [Revision #c1c5b7a8d2](https://github.com/MariaDB/server/commit/c1c5b7a8d2)\
  2017-03-01 11:41:48 +0400
  * Fixed missing DBUG\_RETURN
* [Revision #e9ad4bdb42](https://github.com/MariaDB/server/commit/e9ad4bdb42)\
  2017-02-28 15:23:44 +0400
  * [MDEV-11221](https://jira.mariadb.org/browse/MDEV-11221) - main.events\_restart failed in bb
* [Revision #cc413ce9a3](https://github.com/MariaDB/server/commit/cc413ce9a3)\
  2017-02-23 20:45:07 +0100
  * [MDEV-11753](https://jira.mariadb.org/browse/MDEV-11753) Link failure on missing -L${LIBLZ4\_LIBRARY\_DIR}
* [Revision #370cf70136](https://github.com/MariaDB/server/commit/370cf70136)\
  2017-02-22 19:50:27 +0100
  * [MDEV-11757](https://jira.mariadb.org/browse/MDEV-11757) KEY\_BLOCK\_SIZE strangeness when UNCOMPRESSing COMPRESSed InnoDB tables
* [Revision #6a12c05347](https://github.com/MariaDB/server/commit/6a12c05347)\
  2017-02-10 22:39:22 +0200
  * Fixed wrong arguments to sql\_print\_error()
* [Revision #84ed5e1d5f](https://github.com/MariaDB/server/commit/84ed5e1d5f)\
  2017-02-10 22:35:04 +0200
  * Fixed hang doing FLUSH TABLES WITH READ LOCK and parallel replication
* [Revision #f3c65ce951](https://github.com/MariaDB/server/commit/f3c65ce951)\
  2017-02-10 20:30:37 +0200
  * Add protection to not access is\_open() without LOCK\_log mutex
* [Revision #b624b41abb](https://github.com/MariaDB/server/commit/b624b41abb)\
  2017-02-10 20:25:01 +0200
  * Don't allow one to kill START SLAVE while the slaves IO\_THREAD or SQL\_THREAD is starting.
* [Revision #d7a9aed43f](https://github.com/MariaDB/server/commit/d7a9aed43f)\
  2017-02-08 02:14:54 +0200
  * Fixed test failing as myisam table was deleted before oqgraph table.
* [Revision #4bad74e139](https://github.com/MariaDB/server/commit/4bad74e139)\
  2017-02-05 02:23:49 +0200
  * Added error checking for all calls to flush\_relay\_log\_info() and stmt\_done()
* [Revision #a2de378c00](https://github.com/MariaDB/server/commit/a2de378c00)\
  2017-01-30 16:13:49 +0200
  * Add protection for reinitialization of mutex in parallel replaction
* [Revision #c5e25c8b40](https://github.com/MariaDB/server/commit/c5e25c8b40)\
  2017-01-29 23:44:24 +0200
  * Added a separate lock for start/stop/reset slave. This solves some possible dead locks when one calls stop slave while slave is starting.
* [Revision #e65f667bb6](https://github.com/MariaDB/server/commit/e65f667bb6)\
  2017-01-29 22:10:56 +0200
  * [MDEV-9573](https://jira.mariadb.org/browse/MDEV-9573) 'Stop slave' hangs on replication slave
* [Revision #d5c54f3990](https://github.com/MariaDB/server/commit/d5c54f3990)\
  2017-01-29 18:18:19 +0200
  * Fixed compiler warnings
* [Revision #ce903428a8](https://github.com/MariaDB/server/commit/ce903428a8)\
  2017-02-23 11:27:52 +0200
  * Update MariaDB Foundation sponsors
* [Revision #d4baeca441](https://github.com/MariaDB/server/commit/d4baeca441)\
  2017-02-28 12:57:33 +0000
  * Windows : Fix server compile errors when compile with /Zc:strictStrings option
* [Revision #fc673a2c12](https://github.com/MariaDB/server/commit/fc673a2c12)\
  2017-02-28 09:54:12 +0200
  * [MDEV-12127](https://jira.mariadb.org/browse/MDEV-12127) InnoDB: Assertion failure loop\_count < 5 in file log0log.cc
* [Revision #b54566d73b](https://github.com/MariaDB/server/commit/b54566d73b)\
  2017-02-28 10:08:12 +1100
  * [MDEV-11619](https://jira.mariadb.org/browse/MDEV-11619): mtr --mem {no argument of a directory} (#320)
* [Revision #e5b877ce27](https://github.com/MariaDB/server/commit/e5b877ce27)\
  2017-02-23 21:50:55 +0100
  * [MDEV-11935](https://jira.mariadb.org/browse/MDEV-11935): Queries in stored procedures with and EXISTS(SELECT \* FROM VIEW) crashes and closes hte conneciton.
* [Revision #fdeeab01c0](https://github.com/MariaDB/server/commit/fdeeab01c0)\
  2017-02-26 23:01:23 +0400
  * [MDEV-6390](https://jira.mariadb.org/browse/MDEV-6390) CONVERT TO CHARACTER SET utf8 doesn't change DEFAULT CHARSET.
* [Revision #ae142c21a5](https://github.com/MariaDB/server/commit/ae142c21a5)\
  2017-02-23 14:24:34 +0200
  * [MDEV-12106](https://jira.mariadb.org/browse/MDEV-12106) Valgrind tests fail all over in buildbot on 10.0
* [Revision #bc28b305e5](https://github.com/MariaDB/server/commit/bc28b305e5)\
  2017-02-20 11:36:33 +1100
  * Remove warning: unused variable 'volatile\_var' \[-Wunused-variable]
* Merge [Revision #88b5eedef2](https://github.com/MariaDB/server/commit/88b5eedef2) 2017-03-02 08:29:52 +0200 - Merge pull request #312 from grooverdan/10.0-[MDEV-10515](https://jira.mariadb.org/browse/MDEV-10515)-stat\_tables\_par-test-fix
* [Revision #e2d6760d8a](https://github.com/MariaDB/server/commit/e2d6760d8a)\
  2017-02-16 16:42:25 +1100
  * [MDEV-10515](https://jira.mariadb.org/browse/MDEV-10515): Correct stat\_tables\_par test results
* [Revision #ad2e38153c](https://github.com/MariaDB/server/commit/ad2e38153c)\
  2017-03-01 10:07:54 +0000
  * AWS key management plugin: Fix search for system installed AWS SDK libs
* [Revision #7f7673033e](https://github.com/MariaDB/server/commit/7f7673033e)\
  2017-02-22 19:55:54 +0200
  * Remove an unused variable.
* [Revision #ec4cf111c0](https://github.com/MariaDB/server/commit/ec4cf111c0)\
  2017-02-22 17:17:00 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) after-merge fix for 10.1: Use sparse files.
* Merge [Revision #e1e920bf63](https://github.com/MariaDB/server/commit/e1e920bf63) 2017-02-22 15:53:05 +0200 - Merge 10.0 into 10.1
* [Revision #a0ce92ddc7](https://github.com/MariaDB/server/commit/a0ce92ddc7)\
  2017-02-22 12:32:17 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) post-fix
* [Revision #81695ab8b5](https://github.com/MariaDB/server/commit/81695ab8b5)\
  2017-02-21 16:52:41 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) Extending an InnoDB data file unnecessarily allocates a large memory buffer on Windows
* [Revision #6dc00f97b7](https://github.com/MariaDB/server/commit/6dc00f97b7)\
  2017-02-21 15:03:34 +0200
  * [MDEV-11774](https://jira.mariadb.org/browse/MDEV-11774) tokudb.locks-select-update-3 failed in buildbot with lock wait timeout
* Merge [Revision #3c47ed4849](https://github.com/MariaDB/server/commit/3c47ed4849) 2017-02-20 14:02:40 +0200 - Merge 10.0 into 10.1
* [Revision #13493078e9](https://github.com/MariaDB/server/commit/13493078e9)\
  2017-02-16 19:40:03 +0200
  * [MDEV-11802](https://jira.mariadb.org/browse/MDEV-11802) innodb.innodb\_bug14676111 fails
* [Revision #72994d6442](https://github.com/MariaDB/server/commit/72994d6442)\
  2017-02-17 10:36:50 +0200
  * Revert the [MDEV-4396](https://jira.mariadb.org/browse/MDEV-4396) tweak to innodb.innodb\_bug14676111.
* [Revision #343ba58562](https://github.com/MariaDB/server/commit/343ba58562)\
  2017-02-18 16:33:18 +0200
  * [MDEV-10631](https://jira.mariadb.org/browse/MDEV-10631) rpl.rpl\_mdev6386 failed in buildbot
* [Revision #72a822f2ec](https://github.com/MariaDB/server/commit/72a822f2ec)\
  2017-02-17 20:09:14 +0200
  * [MDEV-11766](https://jira.mariadb.org/browse/MDEV-11766) Tests failed in buildbot with semaphore waiting warnings
* [Revision #5e42c958a5](https://github.com/MariaDB/server/commit/5e42c958a5)\
  2017-02-20 10:43:42 +1100
  * [MDEV-11619](https://jira.mariadb.org/browse/MDEV-11619): mtr --mem and $MTR\_MEM support in sane and consistent manner (10.0) (#289)
* [Revision #01d5d6db4c](https://github.com/MariaDB/server/commit/01d5d6db4c)\
  2017-02-16 11:16:27 +0200
  * Fix GCC 6.3.0 warnings.
* [Revision #ba4d0a1b35](https://github.com/MariaDB/server/commit/ba4d0a1b35)\
  2017-02-17 12:47:09 +0400
  * There's no systemd socket activation support yet
* [Revision #32170cafad](https://github.com/MariaDB/server/commit/32170cafad)\
  2017-02-16 11:12:24 +0200
  * [MDEV-12075](https://jira.mariadb.org/browse/MDEV-12075) innodb\_use\_fallocate does not work in MariaDB Server 10.1.21
* [Revision #74a5638a1d](https://github.com/MariaDB/server/commit/74a5638a1d)\
  2017-02-13 18:40:24 -0500
  * [MDEV-11530](https://jira.mariadb.org/browse/MDEV-11530): wsrep\_info.plugin fails sporadically in buildbot
* [Revision #66822f164f](https://github.com/MariaDB/server/commit/66822f164f)\
  2017-02-11 01:14:06 +0200
  * Follow-up to [MDEV-10731](https://jira.mariadb.org/browse/MDEV-10731) - fix the broken test
* [Revision #de9963b786](https://github.com/MariaDB/server/commit/de9963b786)\
  2017-02-10 17:41:35 +0200
  * After reivew fixes.
* [Revision #41cd80fe06](https://github.com/MariaDB/server/commit/41cd80fe06)\
  2017-02-10 16:05:37 +0200
  * After review fixes.
* [Revision #c2b217e243](https://github.com/MariaDB/server/commit/c2b217e243)\
  2017-02-09 22:23:26 +0530
  * [MDEV-10731](https://jira.mariadb.org/browse/MDEV-10731): Wrong NULL match results in "Subquery returns more than 1 row" (error code 1242)
* [Revision #99b2de92c6](https://github.com/MariaDB/server/commit/99b2de92c6)\
  2017-02-09 09:36:10 +0200
  * Post-push fix for [MDEV-11623](https://jira.mariadb.org/browse/MDEV-11623): Remove an unused variable.
* Merge [Revision #ef065dbbc2](https://github.com/MariaDB/server/commit/ef065dbbc2) 2017-02-09 08:51:52 +0200 - Merge 10.0 into 10.1
* [Revision #6011fb6daa](https://github.com/MariaDB/server/commit/6011fb6daa)\
  2017-02-09 08:47:38 +0200
  * Post-push fix for [MDEV-11947](https://jira.mariadb.org/browse/MDEV-11947) InnoDB purge workers fail to shut down
* [Revision #0340067608](https://github.com/MariaDB/server/commit/0340067608)\
  2017-02-07 20:08:07 +0200
  * After review fixes for [MDEV-11759](https://jira.mariadb.org/browse/MDEV-11759).
* Merge [Revision #9017a05d87](https://github.com/MariaDB/server/commit/9017a05d87) 2017-02-08 17:30:25 +0200 - Merge 10.0 into 10.1
* [Revision #d831e4c22a](https://github.com/MariaDB/server/commit/d831e4c22a)\
  2017-02-08 15:42:15 +0200
  * [MDEV-12024](https://jira.mariadb.org/browse/MDEV-12024) InnoDB startup fails to wait for recv\_writer\_thread to finish
* [Revision #981534b1dd](https://github.com/MariaDB/server/commit/981534b1dd)\
  2017-02-08 11:40:09 +0200
  * Remove unnecessary have\_debug.inc, not\_valgrind.inc
* [Revision #cbdc389ec9](https://github.com/MariaDB/server/commit/cbdc389ec9)\
  2017-02-08 11:35:35 +0200
  * [MDEV-12022](https://jira.mariadb.org/browse/MDEV-12022) InnoDB wrongly ignores the end of an .ibd file
* [Revision #06a7923f4f](https://github.com/MariaDB/server/commit/06a7923f4f)\
  2017-02-08 10:06:18 +0200
  * Remove some more error log spam.
* [Revision #257eea3dac](https://github.com/MariaDB/server/commit/257eea3dac)\
  2017-02-07 16:09:24 +0200
  * Remove some error log spam by not effectively setting DEBUG\_DBUG='d'.
* Merge [Revision #2e67e66c3a](https://github.com/MariaDB/server/commit/2e67e66c3a) 2017-02-08 08:53:34 +0200 - Merge 10.0 into 10.1
* [Revision #f162704570](https://github.com/MariaDB/server/commit/f162704570)\
  2017-01-30 17:00:51 +0200
  * Rewrite the innodb.log\_file\_size test with DBUG\_EXECUTE\_IF.
* [Revision #20e8347447](https://github.com/MariaDB/server/commit/20e8347447)\
  2017-02-03 12:25:42 +0200
  * [MDEV-11985](https://jira.mariadb.org/browse/MDEV-11985) Make innodb\_read\_only shutdown more robust
* [Revision #9f0dbb3120](https://github.com/MariaDB/server/commit/9f0dbb3120)\
  2017-02-03 18:17:36 +0200
  * [MDEV-11947](https://jira.mariadb.org/browse/MDEV-11947) InnoDB purge workers fail to shut down
* [Revision #e174d923d9](https://github.com/MariaDB/server/commit/e174d923d9)\
  2017-02-03 19:33:09 +0200
  * innodb.innodb-get-fk: Actually test --innodb-read-only.
* [Revision #1d725c8176](https://github.com/MariaDB/server/commit/1d725c8176)\
  2017-02-01 02:16:01 +0200
  * Flush suppressions table to prevent corruption when server is killed
* [Revision #b3dac63f9b](https://github.com/MariaDB/server/commit/b3dac63f9b)\
  2017-02-01 02:14:37 +0200
  * Produce better diagnostics when backtrace attempt fails
* [Revision #923d7d0ad2](https://github.com/MariaDB/server/commit/923d7d0ad2)\
  2017-01-29 00:50:28 +0200
  * Set sys\_errno upon exec command
* [Revision #c46d140961](https://github.com/MariaDB/server/commit/c46d140961)\
  2017-01-29 21:00:02 +0200
  * [MDEV-11764](https://jira.mariadb.org/browse/MDEV-11764) perfschema.table\_name fails in buildbot
* [Revision #f7e03d4419](https://github.com/MariaDB/server/commit/f7e03d4419)\
  2017-01-30 18:35:26 -0500
  * [MDEV-4774](https://jira.mariadb.org/browse/MDEV-4774): Fix test case
* [Revision #6da2adfaa2](https://github.com/MariaDB/server/commit/6da2adfaa2)\
  2017-02-07 13:54:46 -0500
  * [MDEV-12005](https://jira.mariadb.org/browse/MDEV-12005): GET\_LOCK: Fractional part of timeout is ignored
* [Revision #5c7111cb7c](https://github.com/MariaDB/server/commit/5c7111cb7c)\
  2017-02-07 14:32:09 +0200
  * Add suppression for page corruption caused by error injection.
* [Revision #e53dfb24be](https://github.com/MariaDB/server/commit/e53dfb24be)\
  2017-02-06 10:55:23 +0200
  * [MDEV-11707](https://jira.mariadb.org/browse/MDEV-11707): Fix incorrect memset() for structures containing
* [Revision #ddf2fac733](https://github.com/MariaDB/server/commit/ddf2fac733)\
  2017-02-06 10:47:55 +0200
  * [MDEV-11759](https://jira.mariadb.org/browse/MDEV-11759): Encryption code in [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)/10.2 causes
* [Revision #9ec8500998](https://github.com/MariaDB/server/commit/9ec8500998)\
  2017-03-30 09:25:16 +0200
  * update libmariadb, enable C/C unit tests
* [Revision #8599f16b9d](https://github.com/MariaDB/server/commit/8599f16b9d)\
  2017-03-29 21:12:09 +0200
  * fix mysql-test unit suite to work for out-of-source builds
* [Revision #3c422e60bb](https://github.com/MariaDB/server/commit/3c422e60bb)\
  2017-03-28 16:56:18 -0700
  * [MDEV-11115](https://jira.mariadb.org/browse/MDEV-11115) CHECK constraints are not shown in I\_S.TABLE\_CONSTRAINTS
* [Revision #4ebdef2bcd](https://github.com/MariaDB/server/commit/4ebdef2bcd)\
  2017-03-28 15:08:50 -0700
  * Fixed bug [MDEV-12336](https://jira.mariadb.org/browse/MDEV-12336).
* [Revision #f381e73f7d](https://github.com/MariaDB/server/commit/f381e73f7d)\
  2017-03-28 14:48:54 -0700
  * Fixed bug [MDEV-11907](https://jira.mariadb.org/browse/MDEV-11907).
* [Revision #d9bab412e9](https://github.com/MariaDB/server/commit/d9bab412e9)\
  2017-03-29 13:37:18 +0200
  * update test results for embedded
* [Revision #c5520a37d6](https://github.com/MariaDB/server/commit/c5520a37d6)\
  2017-03-29 07:21:34 +0400
  * [MDEV-12390](https://jira.mariadb.org/browse/MDEV-12390) Wrong error line numbers reported with sql\_mode=IGNORE\_SPACE
* [Revision #3f7455c030](https://github.com/MariaDB/server/commit/3f7455c030)\
  2017-03-28 18:56:37 +0200
  * update a forgotten result file
* [Revision #3a3b3d8ba8](https://github.com/MariaDB/server/commit/3a3b3d8ba8)\
  2017-03-27 11:03:23 +0200
  * cleanup: innodb files in cmake/
* [Revision #92aafebd2a](https://github.com/MariaDB/server/commit/92aafebd2a)\
  2017-03-24 11:11:11 +0100
  * [MDEV-11605](https://jira.mariadb.org/browse/MDEV-11605) Assertion \`(longlong) thd->status\_var.local\_memory\_used >= 0 || !debug\_assert\_on\_not\_freed\_memory' failed in my\_malloc\_size\_cb\_func
* [Revision #f63007a371](https://github.com/MariaDB/server/commit/f63007a371)\
  2017-03-23 13:53:36 +0100
  * [MDEV-10354](https://jira.mariadb.org/browse/MDEV-10354) Assertion \`! is\_set()' failed in Diagnostics\_area::set\_ok\_status on CREATE TABLE with invalid default
* [Revision #7a1b0582d6](https://github.com/MariaDB/server/commit/7a1b0582d6)\
  2017-03-22 20:38:10 +0100
  * [MDEV-11114](https://jira.mariadb.org/browse/MDEV-11114) Cannot drop column referenced by CHECK constraint: Unknown column 'a' in 'virtual column function'
* [Revision #33ec445975](https://github.com/MariaDB/server/commit/33ec445975)\
  2017-03-22 18:44:01 +0100
  * [MDEV-10370](https://jira.mariadb.org/browse/MDEV-10370) Check constraints on virtual columns fails on INSERT when column not specified
* [Revision #1216244eb9](https://github.com/MariaDB/server/commit/1216244eb9)\
  2017-03-22 16:17:03 +0100
  * [MDEV-11703](https://jira.mariadb.org/browse/MDEV-11703) InnoDB background threads show up in the processlist
* [Revision #98a5ee9d75](https://github.com/MariaDB/server/commit/98a5ee9d75)\
  2017-03-22 15:07:28 +0100
  * [MDEV-12105](https://jira.mariadb.org/browse/MDEV-12105) MySQL 5.7 and [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) error codes are out of sync
* [Revision #bf40e8069c](https://github.com/MariaDB/server/commit/bf40e8069c)\
  2017-03-22 14:34:34 +0100
  * [MDEV-11059](https://jira.mariadb.org/browse/MDEV-11059) don't build the server with jemalloc
* [Revision #31a5d7212f](https://github.com/MariaDB/server/commit/31a5d7212f)\
  2017-03-22 11:52:49 +0100
  * [MDEV-12203](https://jira.mariadb.org/browse/MDEV-12203) build fails, multiple errors, in xtradb/handler
* [Revision #f4c39f7bc9](https://github.com/MariaDB/server/commit/f4c39f7bc9)\
  2017-02-26 08:36:23 +0100
  * cleanup: mysqltest
* [Revision #2b4c485fea](https://github.com/MariaDB/server/commit/2b4c485fea)\
  2017-02-24 17:07:12 +0100
  * [MDEV-11720](https://jira.mariadb.org/browse/MDEV-11720) main.signal\_demo3 fails in buildbot on labrador
* [Revision #da5c3e03f6](https://github.com/MariaDB/server/commit/da5c3e03f6)\
  2017-03-28 23:36:33 +0400
  * [MDEV-9255](https://jira.mariadb.org/browse/MDEV-9255) Add generation\_expression to information\_schema.columns.
* [Revision #93dd70ced8](https://github.com/MariaDB/server/commit/93dd70ced8)\
  2017-03-27 14:41:17 -0700
  * Fixed bug [MDEV-12375](https://jira.mariadb.org/browse/MDEV-12375). The function st\_select\_lex\_unit::exec\_recursive() incorrectly determined that a CTE mutually recursive with some others was stabilized in the case when the non-recursive part of the CTE returned an empty set. As a result the server fell into an infinite loop when executing a query using this CTE.
* Merge [Revision #046d442d4c](https://github.com/MariaDB/server/commit/046d442d4c) 2017-03-27 16:47:01 +0000 - Merge branch '10.2' of [server](https://github.com/mariadb/server) into 10.2
* [Revision #ad7da60ded](https://github.com/MariaDB/server/commit/ad7da60ded)\
  2017-03-26 22:59:33 -0700
  * Fixed bug [MDEV-12368](https://jira.mariadb.org/browse/MDEV-12368).
* [Revision #5a4537f092](https://github.com/MariaDB/server/commit/5a4537f092)\
  2017-03-24 22:04:19 -0700
  * Fixed bug [MDEV-12360](https://jira.mariadb.org/browse/MDEV-12360).
* [Revision #d3f82e3a67](https://github.com/MariaDB/server/commit/d3f82e3a67)\
  2017-03-27 16:20:06 +0000
  * Fix connect engine crashes in buildbot tests on Win64.
* [Revision #b56262f696](https://github.com/MariaDB/server/commit/b56262f696)\
  2017-03-26 23:03:25 +0000
  * [MDEV-12328](https://jira.mariadb.org/browse/MDEV-12328), attempt to fix windows packaging
* [Revision #23d72bf3aa](https://github.com/MariaDB/server/commit/23d72bf3aa)\
  2017-03-24 19:17:23 +0200
  * Close a file handle in a Perl snippet.
* [Revision #cd2fe26116](https://github.com/MariaDB/server/commit/cd2fe26116)\
  2017-03-24 18:24:46 +0200
  * [MDEV-11802](https://jira.mariadb.org/browse/MDEV-11802) innodb.innodb\_bug14676111 fails on buildbot
* Merge [Revision #ec307de388](https://github.com/MariaDB/server/commit/ec307de388) 2017-03-24 16:04:39 +0100 - Merge pull request #342 from rasmushoj/10.2
* [Revision #3c3bbbb704](https://github.com/MariaDB/server/commit/3c3bbbb704)\
  2017-03-24 16:54:59 +0200
  * [MDEV-12328](https://jira.mariadb.org/browse/MDEV-12328), added building of AWS for release builds
* [Revision #92f18bdede](https://github.com/MariaDB/server/commit/92f18bdede)\
  2017-03-22 01:48:22 +0400
  * [MDEV-11177](https://jira.mariadb.org/browse/MDEV-11177) mysqlbinlog exits silently without error when another instance connects to server.
* [Revision #1ca8637ae3](https://github.com/MariaDB/server/commit/1ca8637ae3)\
  2017-03-20 14:14:01 +0000
  * Windows : Fix several thousand of warnings with Visual C++ compiler
* [Revision #76f6c1e1ed](https://github.com/MariaDB/server/commit/76f6c1e1ed)\
  2017-03-20 15:18:06 +0400
  * [MDEV-12262](https://jira.mariadb.org/browse/MDEV-12262) Assertion \`!null\_value' failed in virtual bool Item::send on JSON\_REMOVE.
* [Revision #a06da5c848](https://github.com/MariaDB/server/commit/a06da5c848)\
  2017-03-18 21:37:36 +0200
  * [MDEV-12258](https://jira.mariadb.org/browse/MDEV-12258) InnoDB: Fix the bogus debug assertion introduced in [MDEV-12219](https://jira.mariadb.org/browse/MDEV-12219)
* [Revision #6c5cfbbf33](https://github.com/MariaDB/server/commit/6c5cfbbf33)\
  2017-03-17 19:18:53 +0000
  * Fix crash (race condition) in DBUG in connect2 test case.
* [Revision #a77ac6513e](https://github.com/MariaDB/server/commit/a77ac6513e)\
  2015-05-27 14:34:45 +0100
  * Bug#21153166: REMOVE UNUSED VARIABLES AND CONVERT GLOBAL SYMBOLS TO STATIC
* [Revision #97acc4a1c3](https://github.com/MariaDB/server/commit/97acc4a1c3)\
  2015-05-26 10:01:12 +0300
  * [MDEV-12270](https://jira.mariadb.org/browse/MDEV-12270) Port MySQL 8.0 Bug#21141390 REMOVE UNUSED FUNCTIONS AND CONVERT GLOBAL SYMBOLS TO STATIC
* [Revision #4e1116b2c6](https://github.com/MariaDB/server/commit/4e1116b2c6)\
  2016-04-22 10:50:45 +0200
  * [MDEV-12271](https://jira.mariadb.org/browse/MDEV-12271) Port MySQL 8.0 Bug#23150562 REMOVE UNIV\_MUST\_NOT\_INLINE AND UNIV\_NONINL
* [Revision #c63ca3d7f0](https://github.com/MariaDB/server/commit/c63ca3d7f0)\
  2017-03-17 09:00:31 +0000
  * Do not send MARIADB\_CLIENT\_STMT\_BULK\_OPERATIONS server capability, until the protocol changes for bulk are finalized.
* [Revision #66905f6dcb](https://github.com/MariaDB/server/commit/66905f6dcb)\
  2017-03-17 08:56:57 +0000
  * Fix several compile warnings on Windows
* [Revision #7668a79a88](https://github.com/MariaDB/server/commit/7668a79a88)\
  2016-03-29 13:20:32 +0300
  * [MDEV-12269](https://jira.mariadb.org/browse/MDEV-12269) Port Bug#22996442 INNODB: MAKE UNIV\_DEBUG DEPEND ON DBUG\_OFF
* [Revision #105f46ffb8](https://github.com/MariaDB/server/commit/105f46ffb8)\
  2017-03-15 15:56:17 +0200
  * [MDEV-12273](https://jira.mariadb.org/browse/MDEV-12273) Remove dict\_table\_t::does\_not\_fit\_in\_memory
* [Revision #aad15eae89](https://github.com/MariaDB/server/commit/aad15eae89)\
  2017-03-16 10:18:02 +0530
  * Test result for [MDEV-10766](https://jira.mariadb.org/browse/MDEV-10766) fixed
* [Revision #cd7e6d8b53](https://github.com/MariaDB/server/commit/cd7e6d8b53)\
  2017-03-15 21:26:39 +0530
  * [MDEV-11645](https://jira.mariadb.org/browse/MDEV-11645): archive.archive fails in buildbot with valgrind (Use of uninitialised value)
* [Revision #6ac754163c](https://github.com/MariaDB/server/commit/6ac754163c)\
  2017-03-15 20:15:31 +0530
  * [MDEV-10766](https://jira.mariadb.org/browse/MDEV-10766): Queries which start with WITH clause do not get inserted into query cache
* [Revision #122d0701f7](https://github.com/MariaDB/server/commit/122d0701f7)\
  2017-01-24 19:20:30 +0100
  * [MDEV-11761](https://jira.mariadb.org/browse/MDEV-11761): CLIENT\_DEPRECATE\_EOF : Client must identify a "stored procedure output resultset"
* [Revision #5dd4d663fa](https://github.com/MariaDB/server/commit/5dd4d663fa)\
  2017-03-15 15:51:44 +0400
  * Test result fixed.
* [Revision #b5285bd7e2](https://github.com/MariaDB/server/commit/b5285bd7e2)\
  2017-03-14 17:11:46 +0200
  * [MDEV-11873](https://jira.mariadb.org/browse/MDEV-11873) Unnecessary InnoDB warnings upon bootstrap
* [Revision #af6eee1fc5](https://github.com/MariaDB/server/commit/af6eee1fc5)\
  2017-03-14 17:31:14 +0400
  * [MDEV-11833](https://jira.mariadb.org/browse/MDEV-11833) JSON functions don't seem to respect max\_allowed\_packet.
* [Revision #d0e8b427a1](https://github.com/MariaDB/server/commit/d0e8b427a1)\
  2017-03-14 16:35:39 +0400
  * [MDEV-12078](https://jira.mariadb.org/browse/MDEV-12078) Using spatial index changes type from point to geometry
* [Revision #7c7c0696e7](https://github.com/MariaDB/server/commit/7c7c0696e7)\
  2017-03-14 15:25:02 +0400
  * [MDEV-11856](https://jira.mariadb.org/browse/MDEV-11856) json\_search doesn't search for values with double quotes character (").
* [Revision #a77c2ea78f](https://github.com/MariaDB/server/commit/a77c2ea78f)\
  2017-03-14 12:15:49 +0200
  * Post-fix [MDEV-12219](https://jira.mariadb.org/browse/MDEV-12219) Discard temporary undo logs at transaction commit
* [Revision #f0a2f4bbb9](https://github.com/MariaDB/server/commit/f0a2f4bbb9)\
  2017-03-13 20:14:28 +0000
  * Windows : Remove the option for creating anonymous account from the MSI in 10.2
* [Revision #b7ffe9b81e](https://github.com/MariaDB/server/commit/b7ffe9b81e)\
  2017-03-13 19:58:04 +0000
  * [MDEV-11903](https://jira.mariadb.org/browse/MDEV-11903) : correction - min innodb pagesize is 4K
* [Revision #a8715884a4](https://github.com/MariaDB/server/commit/a8715884a4)\
  2017-03-13 18:38:36 +0000
  * [MDEV-11903](https://jira.mariadb.org/browse/MDEV-11903) Windows : Support innodb page sizes in the installer/mysql\_install\_db.exe
* [Revision #bfef611a22](https://github.com/MariaDB/server/commit/bfef611a22)\
  2017-03-13 18:00:42 +0100
  * [MDEV-12244](https://jira.mariadb.org/browse/MDEV-12244): C API header file contains C++ comment for COM\_BINLOG\_DUMP\_GTID
* [Revision #13e5c9de80](https://github.com/MariaDB/server/commit/13e5c9de80)\
  2017-03-09 23:20:51 +0200
  * [MDEV-12219](https://jira.mariadb.org/browse/MDEV-12219) Discard temporary undo logs at transaction commit
* [Revision #056ec4ab24](https://github.com/MariaDB/server/commit/056ec4ab24)\
  2017-03-11 15:20:33 +0200
  * Fix some compilation warnings.
* [Revision #e5b155a4e5](https://github.com/MariaDB/server/commit/e5b155a4e5)\
  2017-03-10 16:01:02 +0200
  * [MDEV-12091](https://jira.mariadb.org/browse/MDEV-12091) Shutdown fails to wait for rollback of recovered transactions to finish
* [Revision #ff8bf6e933](https://github.com/MariaDB/server/commit/ff8bf6e933)\
  2017-03-10 13:32:26 +0200
  * Define a mtr\_t::start() wrapper inline.
* [Revision #c32dcae65a](https://github.com/MariaDB/server/commit/c32dcae65a)\
  2017-03-10 15:54:41 +0200
  * Adjust an outdated comment.
* [Revision #c0fb7b458b](https://github.com/MariaDB/server/commit/c0fb7b458b)\
  2017-03-08 19:05:44 +0100
  * [MDEV-10555](https://jira.mariadb.org/browse/MDEV-10555): Server crashes in mysql\_admin\_table upon killing ANALYZE
* [Revision #c29336f2b0](https://github.com/MariaDB/server/commit/c29336f2b0)\
  2017-03-26 18:13:29 +0300
  * Skip rocksdb on debian i386 and when gcc version is < 4.8
* [Revision #7ebb81be1d](https://github.com/MariaDB/server/commit/7ebb81be1d)\
  2017-03-26 17:30:26 +0300
  * Make mysql\_ldb and sst\_dump part of the rocksdb-engine component
* [Revision #a421f0b6b8](https://github.com/MariaDB/server/commit/a421f0b6b8)\
  2017-03-26 00:05:24 +0200
  * Add sst\_dump as binary in rocksdb package
* [Revision #97e5ed1637](https://github.com/MariaDB/server/commit/97e5ed1637)\
  2017-03-25 23:44:21 +0200
  * Add mysql\_ldb to debian rocksdb package
* [Revision #3ade211a72](https://github.com/MariaDB/server/commit/3ade211a72)\
  2017-03-25 23:28:05 +0200
  * Do not build ldb binary as mysql\_ldb does the same thing
* [Revision #86680e8b4f](https://github.com/MariaDB/server/commit/86680e8b4f)\
  2017-03-25 20:18:06 +0200
  * Skip rocksdb plugin if sources can not be fetched
* [Revision #4653b6e2a3](https://github.com/MariaDB/server/commit/4653b6e2a3)\
  2017-03-23 11:06:26 +0300
  * [MDEV-12279](https://jira.mariadb.org/browse/MDEV-12279): rocksdb.tbl\_opt\_data\_index\_dir fails, wrong error code
* [Revision #4967c78aa0](https://github.com/MariaDB/server/commit/4967c78aa0)\
  2017-03-21 19:41:28 +0000
  * make sure rocksdb-engine compoment is in MSI
* [Revision #69ba6b36e6](https://github.com/MariaDB/server/commit/69ba6b36e6)\
  2017-03-21 16:25:38 +0200
  * Add rocksdb as a plugin into debian packaging
* [Revision #21bbe10bb3](https://github.com/MariaDB/server/commit/21bbe10bb3)\
  2017-03-17 17:08:34 +0200
  * Revert "Revert "Make rocksdb build as a deb package too""
* [Revision #619623b862](https://github.com/MariaDB/server/commit/619623b862)\
  2017-03-17 14:44:05 +0300
  * MariaRocks: SET GLOBAL rocksdb\_strict\_collation\_exceptions=null crashes
* [Revision #131d858206](https://github.com/MariaDB/server/commit/131d858206)\
  2017-03-17 04:46:01 +0300
  * Temporarily disable rocksdb.blind\_delete\_without\_tx\_api test
* [Revision #dd743dae32](https://github.com/MariaDB/server/commit/dd743dae32)\
  2017-03-17 04:05:03 +0300
  * Update test results for rocksdb.misc
* [Revision #c707997e15](https://github.com/MariaDB/server/commit/c707997e15)\
  2017-03-17 01:21:11 +0300
  * MariaRocks: run rocksdb testsuite with --default-storage-engine=rocksdb
* [Revision #46a78868fe](https://github.com/MariaDB/server/commit/46a78868fe)\
  2017-03-17 00:05:48 +0300
  * MariaRocks: make rocksdb.rocksdb\_datadir test pass
* [Revision #23f9bb966b](https://github.com/MariaDB/server/commit/23f9bb966b)\
  2017-03-16 21:28:42 +0300
  * [MDEV-12285](https://jira.mariadb.org/browse/MDEV-12285): MariaRocks: "\[ERROR] mysqld: Deadlock ..." messages in server stderr
* [Revision #49de95679d](https://github.com/MariaDB/server/commit/49de95679d)\
  2017-03-16 09:49:34 +0200
  * Revert "Make rocksdb build as a deb package too"
* [Revision #17d7cc731e](https://github.com/MariaDB/server/commit/17d7cc731e)\
  2017-03-16 09:46:01 +0300
  * [MDEV-12277](https://jira.mariadb.org/browse/MDEV-12277): rocksdb.rocksdb fails with Sort Aborted error in server stderr
* [Revision #c5a20553c0](https://github.com/MariaDB/server/commit/c5a20553c0)\
  2017-03-16 01:12:01 +0300
  * More testsuite fixes
* [Revision #38919f68a1](https://github.com/MariaDB/server/commit/38919f68a1)\
  2017-03-15 23:19:24 +0200
  * Make rocksdb build as a deb package too
* [Revision #adb7470742](https://github.com/MariaDB/server/commit/adb7470742)\
  2017-03-15 23:44:16 +0300
  * Disable rocksdb.rpl\_row\_triggers, rocksdb.trx\_info\_rpl
* [Revision #6dc2d581d4](https://github.com/MariaDB/server/commit/6dc2d581d4)\
  2017-03-15 23:36:20 +0300
  * Make rocksdb.rocksdb\_range pass: MariaDB doesnt support ICP over reverse index scans atm
* [Revision #c010f06380](https://github.com/MariaDB/server/commit/c010f06380)\
  2017-03-15 23:19:33 +0300
  * MariaRocks: Run rocksdb testsuite with @@rocksdb\_flush\_log\_at\_trx\_commit=0
* [Revision #bf578ff920](https://github.com/MariaDB/server/commit/bf578ff920)\
  2017-03-15 16:02:37 +0000
  * Add missing source include/have\_rocksdb.inc
* [Revision #20c085a4b7](https://github.com/MariaDB/server/commit/20c085a4b7)\
  2017-03-14 12:23:36 +0300
  * MariaRocks: disable rocksdb.mysqldump2 also (needs --print-ordering-key)
* [Revision #1a3065b51a](https://github.com/MariaDB/server/commit/1a3065b51a)\
  2017-03-14 12:23:08 +0300
  * MariaRocks: make rocksdb.issue495 declare it uses partitioning
* [Revision #3eb8bc7408](https://github.com/MariaDB/server/commit/3eb8bc7408)\
  2017-03-14 01:01:11 +0200
  * Make rocksdb not be compiled on x86 architectures
* [Revision #57672a85e3](https://github.com/MariaDB/server/commit/57672a85e3)\
  2017-03-13 22:02:39 +0000
  * MariaRocks: make partition.test work on any platform
* [Revision #69387c68b5](https://github.com/MariaDB/server/commit/69387c68b5)\
  2017-03-13 10:34:38 +0300
  * MariaRocks: update results for innodb\_i\_s\_tables\_disabled
* [Revision #b4ea125252](https://github.com/MariaDB/server/commit/b4ea125252)\
  2017-03-13 10:34:19 +0300
  * MariaRocks: disable tests that are known to fail
* [Revision #17aa495b64](https://github.com/MariaDB/server/commit/17aa495b64)\
  2017-03-12 22:52:52 +0300
  * MariaRocks: attempt to get to compile on Windows
* [Revision #11789a4fbe](https://github.com/MariaDB/server/commit/11789a4fbe)\
  2017-03-12 17:39:45 +0300
  * MariaRocks: Only call pthread\_setname\_np on platforms that support it
* [Revision #a72abc8c30](https://github.com/MariaDB/server/commit/a72abc8c30)\
  2017-03-12 16:08:26 +0300
  * Fix compile on windows
* [Revision #ec01aa5d6b](https://github.com/MariaDB/server/commit/ec01aa5d6b)\
  2017-03-12 15:59:46 +0300
  * MariaRocks: fix compilation in Windows: don't use PRETTY\_FUNCTION where it is not available
* [Revision #d49bbf12a2](https://github.com/MariaDB/server/commit/d49bbf12a2)\
  2017-03-12 12:14:33 +0300
  * MariaRocks: post-merge fixes: trivial updates to a few test results
* Merge [Revision #5b30c7896e](https://github.com/MariaDB/server/commit/5b30c7896e) 2017-03-11 20:12:15 +0000 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mariarocks
* [Revision #eded6243bc](https://github.com/MariaDB/server/commit/eded6243bc)\
  2017-03-10 23:16:01 +0200
  * [MDEV-12096](https://jira.mariadb.org/browse/MDEV-12096): Fix ln syntax in debian/rules for libmariadb3 symlink creation
* [Revision #eb574697c0](https://github.com/MariaDB/server/commit/eb574697c0)\
  2017-03-10 22:44:52 +0100
  * fix test for windows 64
* [Revision #f2fe5cb282](https://github.com/MariaDB/server/commit/f2fe5cb282)\
  2017-03-10 19:06:33 +0000
  * Fix several compile warnings on Windows
* [Revision #7c512138a1](https://github.com/MariaDB/server/commit/7c512138a1)\
  2017-03-10 19:01:14 +0000
  * Revert MySQL commit that disables writing on Windows while flush is in progress
* [Revision #a20340cf85](https://github.com/MariaDB/server/commit/a20340cf85)\
  2017-03-09 22:06:22 +0200
  * Hard-code innodb\_page\_size as the undo log page size.
* [Revision #0ef91c8958](https://github.com/MariaDB/server/commit/0ef91c8958)\
  2017-03-09 22:01:08 +0200
  * Simplify InnoDB transaction system initialization.
* [Revision #1417839810](https://github.com/MariaDB/server/commit/1417839810)\
  2017-03-09 20:40:48 +0200
  * InnoDB purge\_sys cleanup.
* [Revision #9928dbe5f6](https://github.com/MariaDB/server/commit/9928dbe5f6)\
  2017-03-09 22:47:29 +0100
  * Add SRV\_ALL\_O\_DIRECT\_FSYNC to switch(srv\_flush\_method) in log0log.c.
* [Revision #a98009ab02](https://github.com/MariaDB/server/commit/a98009ab02)\
  2017-03-09 14:32:17 +0000
  * [MDEV-12201](https://jira.mariadb.org/browse/MDEV-12201) innodb\_flush\_method are not available on Windows
* [Revision #8e05953dad](https://github.com/MariaDB/server/commit/8e05953dad)\
  2017-03-08 16:12:17 +0100
  * [MDEV-11363](https://jira.mariadb.org/browse/MDEV-11363): Assertion \`!derived->first\_sel ect()->first\_inner\_unit() || derived->first\_select()->first\_inner\_unit()->first\_select()-> exclude\_from\_table\_unique\_test' failed in TABLE\_LIST::set\_check\_materialized()
* [Revision #70a0500d3c](https://github.com/MariaDB/server/commit/70a0500d3c)\
  2017-03-09 17:35:09 +0200
  * Remove some InnoDB purge definitions from trx0types.h.
* [Revision #7a30d86e9d](https://github.com/MariaDB/server/commit/7a30d86e9d)\
  2017-03-09 17:28:06 +0200
  * Simplify InnoDB startup.
* [Revision #15bdfeeba8](https://github.com/MariaDB/server/commit/15bdfeeba8)\
  2017-03-09 15:58:33 +0200
  * Remove trx\_sys\_t::pending\_purge\_rseg\_array.
* [Revision #24cbc8dae3](https://github.com/MariaDB/server/commit/24cbc8dae3)\
  2017-02-02 12:09:49 +0100
  * [MDEV-11966](https://jira.mariadb.org/browse/MDEV-11966): Impossible to execute prepared ANALYZE SELECT
* [Revision #5ff6694d70](https://github.com/MariaDB/server/commit/5ff6694d70)\
  2017-03-09 10:30:36 +0200
  * enum btr\_latch\_mode: Incorporate some flags.
* [Revision #e88f6f4761](https://github.com/MariaDB/server/commit/e88f6f4761)\
  2017-03-08 22:22:43 +0000
  * [MDEV-12125](https://jira.mariadb.org/browse/MDEV-12125) Use FIND\_PACKAGE(OpenSSL) to find openssl
* [Revision #29a980cf5c](https://github.com/MariaDB/server/commit/29a980cf5c)\
  2017-03-08 22:36:10 +0200
  * [MDEV-11688](https://jira.mariadb.org/browse/MDEV-11688) follow-up: More robust shutdown after aborted startup.
* [Revision #5da6bd7b95](https://github.com/MariaDB/server/commit/5da6bd7b95)\
  2017-03-07 17:16:49 +0200
  * [MDEV-11027](https://jira.mariadb.org/browse/MDEV-11027) InnoDB log recovery is too noisy
* [Revision #0b1abc2f0f](https://github.com/MariaDB/server/commit/0b1abc2f0f)\
  2017-03-08 12:11:49 +0100
  * [MDEV-10704](https://jira.mariadb.org/browse/MDEV-10704): Assertion \`field->field->table == table\_arg' failed in fill\_record(THD\*, TABLE\*, List&, List&, bool, bool)
* [Revision #8c3b98fe5a](https://github.com/MariaDB/server/commit/8c3b98fe5a)\
  2017-03-03 16:58:03 +1100
  * Whitespace correction to avoid compile warning
* [Revision #2d948ebd19](https://github.com/MariaDB/server/commit/2d948ebd19)\
  2017-03-07 21:12:59 -0800
  * Fixed bug [MDEV-12185](https://jira.mariadb.org/browse/MDEV-12185).
* [Revision #3b30031d03](https://github.com/MariaDB/server/commit/3b30031d03)\
  2017-03-07 21:22:25 +0000
  * [MDEV-12202](https://jira.mariadb.org/browse/MDEV-12202) Do not package embedded in MSI
* [Revision #2bca41265c](https://github.com/MariaDB/server/commit/2bca41265c)\
  2017-03-07 13:15:29 +0200
  * Remove MLOG\_COMP\_REC\_SEC\_DELETE\_MARK.
* [Revision #89d80c1b0b](https://github.com/MariaDB/server/commit/89d80c1b0b)\
  2017-03-01 08:27:39 +0200
  * Fix many -Wconversion warnings.
* [Revision #d2f5e62422](https://github.com/MariaDB/server/commit/d2f5e62422)\
  2017-01-23 15:38:56 +1100
  * travis: add gcc-4.8
* [Revision #f2c1e06a94](https://github.com/MariaDB/server/commit/f2c1e06a94)\
  2016-12-19 14:51:36 +1100
  * Travis: Revert to optional MYSQL\_{BUILD\_CC,BUILD\_CXX,COMPILER\_LAUNCHER}
* Merge [Revision #20007c89c8](https://github.com/MariaDB/server/commit/20007c89c8) 2017-03-07 18:02:07 +0400 - Merge branch 'grooverdan-10.2-[MDEV-120555](https://jira.mariadb.org/browse/MDEV-120555)-test\_binlog\_stm\_ctype\_ucs' into 10.2
* Merge [Revision #6ad42c6d5b](https://github.com/MariaDB/server/commit/6ad42c6d5b) 2017-03-07 18:01:46 +0400 - Merge branch '10.2-[MDEV-120555](https://jira.mariadb.org/browse/MDEV-120555)-test\_binlog\_stm\_ctype\_ucs' of [mariadb-server](https://github.com/grooverdan/mariadb-server) into grooverdan-10.2-[MDEV-120555](https://jira.mariadb.org/browse/MDEV-120555)-test\_binlog\_stm\_ctype\_ucs
* [Revision #265e3253f1](https://github.com/MariaDB/server/commit/265e3253f1)\
  2017-02-07 13:08:17 +1100
  * [MDEV-12055](https://jira.mariadb.org/browse/MDEV-12055): Correct binlog\_stm\_ctype\_ucs test
* [Revision #5b07334b32](https://github.com/MariaDB/server/commit/5b07334b32)\
  2017-03-06 11:53:51 +0200
  * Remove an unused declaration.
* [Revision #7331b83eed](https://github.com/MariaDB/server/commit/7331b83eed)\
  2017-03-06 10:07:04 +0200
  * [MDEV-9282](https://jira.mariadb.org/browse/MDEV-9282) follow-up: Remove an unused variable.
* [Revision #ff0530ef68](https://github.com/MariaDB/server/commit/ff0530ef68)\
  2017-03-03 17:08:06 +0200
  * [MDEV-12121](https://jira.mariadb.org/browse/MDEV-12121): Revert test adjustments for -DWITH\_INNODB\_AHI=OFF
* [Revision #27b9989d31](https://github.com/MariaDB/server/commit/27b9989d31)\
  2017-02-23 23:05:12 +0200
  * [MDEV-12121](https://jira.mariadb.org/browse/MDEV-12121) Introduce build option WITH\_INNODB\_AHI to disable innodb\_adaptive\_hash\_index
* [Revision #545f49dac3](https://github.com/MariaDB/server/commit/545f49dac3)\
  2017-03-03 14:43:45 +0200
  * [MDEV-12103](https://jira.mariadb.org/browse/MDEV-12103): Move a misplaced assertion.
* [Revision #ab8199f38e](https://github.com/MariaDB/server/commit/ab8199f38e)\
  2017-03-01 23:43:37 +0200
  * [MDEV-12103](https://jira.mariadb.org/browse/MDEV-12103) Reduce the time of looking for MLOG\_CHECKPOINT during crash recovery
* [Revision #e4a2e80a57](https://github.com/MariaDB/server/commit/e4a2e80a57)\
  2017-03-03 12:18:14 +0530
  * [MDEV-11229](https://jira.mariadb.org/browse/MDEV-11229): galera.MW-258 galera.galera\_as\_master fail in buildbot.
* [Revision #c23e0fe532](https://github.com/MariaDB/server/commit/c23e0fe532)\
  2017-03-01 13:39:08 +1100
  * whitespace - fix indenting after commit 7450cb7f6
* [Revision #6cf29ab0df](https://github.com/MariaDB/server/commit/6cf29ab0df)\
  2017-02-28 12:42:45 +0200
  * [MDEV-12146](https://jira.mariadb.org/browse/MDEV-12146) Deprecate and remove innodb\_instrument\_semaphores
* [Revision #c1bcb2055e](https://github.com/MariaDB/server/commit/c1bcb2055e)\
  2017-02-27 13:44:53 +0200
  * Remove the unused field tablespace\_version.
* [Revision #78153cf641](https://github.com/MariaDB/server/commit/78153cf641)\
  2017-02-24 12:51:55 +0200
  * [MDEV-11927](https://jira.mariadb.org/browse/MDEV-11927) InnoDB change buffer is not being merged to tables in the system tablespace
* [Revision #b513e37117](https://github.com/MariaDB/server/commit/b513e37117)\
  2017-02-24 10:20:44 +0200
  * Clean up some Galera tests.
* [Revision #51af19851a](https://github.com/MariaDB/server/commit/51af19851a)\
  2017-02-24 22:08:09 +0200
  * [MDEV-11454](https://jira.mariadb.org/browse/MDEV-11454) post-merge fix:
* Merge [Revision #342b48b7b1](https://github.com/MariaDB/server/commit/342b48b7b1) 2017-02-24 15:12:09 +0200 - Merge pull request #264 from grooverdan/10.2-[MDEV-11454](https://jira.mariadb.org/browse/MDEV-11454)-innodb\_buffer\_pool\_dump\_pct-entire-pool
* [Revision #473fb9295d](https://github.com/MariaDB/server/commit/473fb9295d)\
  2016-12-08 11:55:35 +1100
  * [MDEV-11454](https://jira.mariadb.org/browse/MDEV-11454): Improve test case innodb\_buffer\_pool\_dump\_pct
* [Revision #84379b05b2](https://github.com/MariaDB/server/commit/84379b05b2)\
  2016-12-05 17:22:13 +1100
  * [MDEV-11454](https://jira.mariadb.org/browse/MDEV-11454): Add test case innodb\_buffer\_pool\_dump\_pct
* [Revision #d04cb70cc3](https://github.com/MariaDB/server/commit/d04cb70cc3)\
  2016-12-05 17:21:31 +1100
  * Report any innodb\_buf\_pool\_dump\_pct restriction
* [Revision #050a05bdb7](https://github.com/MariaDB/server/commit/050a05bdb7)\
  2016-12-05 16:27:51 +1100
  * xtradb: new style ib\_logf logging rather than stderr
* [Revision #1e3f351e92](https://github.com/MariaDB/server/commit/1e3f351e92)\
  2016-10-06 07:47:49 +0200
  * [MDEV-11454](https://jira.mariadb.org/browse/MDEV-11454): Make innodb\_buffer\_pool\_dump\_pct refer to the entire buffer pool size
* [Revision #979e94d264](https://github.com/MariaDB/server/commit/979e94d264)\
  2017-02-16 14:11:33 +0100
  * followup for 96d097a7fa1
* [Revision #a13a636c74](https://github.com/MariaDB/server/commit/a13a636c74)\
  2017-02-17 10:32:21 +0200
  * [MDEV-11802](https://jira.mariadb.org/browse/MDEV-11802) innodb.innodb\_bug14676111 fails
* [Revision #cc4b2b185d](https://github.com/MariaDB/server/commit/cc4b2b185d)\
  2017-02-17 10:23:39 +0200
  * [MDEV-11802](https://jira.mariadb.org/browse/MDEV-11802) preparation: Clean up the purge tests.
* [Revision #d58b4bc6a6](https://github.com/MariaDB/server/commit/d58b4bc6a6)\
  2017-02-17 16:23:17 -0500
  * bump the VERSION
* Merge [Revision #5c1c2f67ec](https://github.com/MariaDB/server/commit/5c1c2f67ec) 2017-03-11 20:00:08 +0000 - Merge branch 'merge-myrocks' of github.com:MariaDB/mergetrees into bb-10.2-mariarocks
* [Revision #65d01da29c](https://github.com/MariaDB/server/commit/65d01da29c)\
  2017-03-11 07:17:42 +0300
  * Copy of commit ba00e640f658ad8d0a4dff09a497a51b8a4de935 Author: Herman Lee [herman@fb.com](mailto:herman@fb.com) Date: Wed Feb 22 06:30:06 2017 -0800
* [Revision #fd39f25ca7](https://github.com/MariaDB/server/commit/fd39f25ca7)\
  2017-03-10 14:05:17 +0300
  * MariaRocks: fix compilation on Oracle Linux Server 7.3.
* [Revision #e19f1dd61e](https://github.com/MariaDB/server/commit/e19f1dd61e)\
  2017-03-07 14:11:19 +0000
  * Fix build on Windows. Remove some GCC specific pragmas, use #ifdef GNUC in other places. Only use pthread\_setname\_np on Linux. Fix a mismerge
* [Revision #f9e63b7c59](https://github.com/MariaDB/server/commit/f9e63b7c59)\
  2017-03-07 11:38:26 +0300
  * MariaRocks port: PRETTY\_FUNCTION is a gcc extension. Use func when it is not available
* [Revision #48a5dd945b](https://github.com/MariaDB/server/commit/48a5dd945b)\
  2017-03-07 11:08:41 +0300
  * MariaRocks: fix compilation on kvm-rpm-centos7-amd64
* [Revision #e7948e34ee](https://github.com/MariaDB/server/commit/e7948e34ee)\
  2017-03-06 23:59:29 +0300
  * Fix the previous cset: use a proper disabled.def syntax
* [Revision #f080c93dcd](https://github.com/MariaDB/server/commit/f080c93dcd)\
  2017-03-06 14:50:14 +0300
  * MariaRocks: (Temporarily?) disable MTR tests that run RQG
* [Revision #ea5cc017e9](https://github.com/MariaDB/server/commit/ea5cc017e9)\
  2017-02-21 16:49:18 +0300
  * Test fixes in rocksdb\_sys\_vars test suite
* [Revision #e57ab94cce](https://github.com/MariaDB/server/commit/e57ab94cce)\
  2017-02-21 03:51:09 +0300
  * Update rocksdb submodule to match the rocksdb version used in upstream
* Merge [Revision #7d00f0981e](https://github.com/MariaDB/server/commit/7d00f0981e) 2017-02-20 13:01:32 +0000 - Merge between local changes bb-10.2-mariarocks and the merge from upstream
* [Revision #7facbc548d](https://github.com/MariaDB/server/commit/7facbc548d)\
  2017-02-19 18:51:26 +0300
  * MariaRocks: fix a few tests
* [Revision #de49fd842a](https://github.com/MariaDB/server/commit/de49fd842a)\
  2017-02-09 16:55:02 +0000
  * RocksDB : Add lookup / compiling with optional compression libraries.
* [Revision #241e8a15a2](https://github.com/MariaDB/server/commit/241e8a15a2)\
  2017-02-07 22:12:36 +0200
  * Ignore "invisible" files
* [Revision #e2f3739aa1](https://github.com/MariaDB/server/commit/e2f3739aa1)\
  2017-02-07 22:12:06 +0200
  * Ignore dynamically generated build\_version.cc file
* [Revision #f46176cbef](https://github.com/MariaDB/server/commit/f46176cbef)\
  2017-02-07 22:10:38 +0200
  * Make rocksdb build with clang
* [Revision #840f8eab71](https://github.com/MariaDB/server/commit/840f8eab71)\
  2017-02-07 22:06:59 +0200
  * Make mysql\_ldb work on clang
* [Revision #884fd9ac2b](https://github.com/MariaDB/server/commit/884fd9ac2b)\
  2017-02-07 20:40:55 +0200
  * Make RocksDB run git submodule init and update if rocksdb is not fetched
* [Revision #5875633c2a](https://github.com/MariaDB/server/commit/5875633c2a)\
  2017-02-01 21:27:13 +0000
  * [MDEV-11901](https://jira.mariadb.org/browse/MDEV-11901) : MariaRocks on Windows
* Merge [Revision #5e47d08eb6](https://github.com/MariaDB/server/commit/5e47d08eb6) 2017-02-19 16:29:01 +0000 - Merge 'merge-myrocks' into 'bb-10.2-mariarocks'
* [Revision #7468ccfadf](https://github.com/MariaDB/server/commit/7468ccfadf)\
  2017-02-06 17:39:08 +0000
  * Copy of
* [Revision #13c7839ba7](https://github.com/MariaDB/server/commit/13c7839ba7)\
  2017-01-24 21:51:57 +0300
  * MariaRocks port: Fix for the previous cset (MariaRocks port: put back the assert)
* [Revision #555b1b9f15](https://github.com/MariaDB/server/commit/555b1b9f15)\
  2017-01-24 09:27:15 +0200
  * Make rocksdb dynamic plugin
* [Revision #15d101ca8e](https://github.com/MariaDB/server/commit/15d101ca8e)\
  2017-01-23 21:31:36 +0200
  * Update gitignore to not show rocksdb generated binaries
* [Revision #024a5ec0ec](https://github.com/MariaDB/server/commit/024a5ec0ec)\
  2017-01-23 19:47:58 +0200
  * Add ut0counter.h instead of xtradb linked ut0counter.h
* [Revision #351043adda](https://github.com/MariaDB/server/commit/351043adda)\
  2017-01-21 23:31:52 +0300
  * MariaRocks port: put back the assert
* [Revision #1f0c28f36e](https://github.com/MariaDB/server/commit/1f0c28f36e)\
  2017-01-21 22:58:57 +0300
  * MariaRocks port: move include/atomic\_stat.h into storage/rocksdb
* [Revision #7fb3b348d7](https://github.com/MariaDB/server/commit/7fb3b348d7)\
  2017-01-21 22:58:04 +0300
  * MariaRocks port: Remove handler::init\_with\_fields
* [Revision #2d789dd9dd](https://github.com/MariaDB/server/commit/2d789dd9dd)\
  2017-01-11 22:29:34 +0300
  * MariaRocks: fix a few tests in rocksdb\_sys\_vars test suite
* [Revision #81ed973b1a](https://github.com/MariaDB/server/commit/81ed973b1a)\
  2017-01-11 22:13:52 +0300
  * MariaRocks port: fix the build: fetch git submodules earlier
* [Revision #1a8731952d](https://github.com/MariaDB/server/commit/1a8731952d)\
  2017-01-11 19:40:25 +0300
  * MariaRocks port: get rocksdb\_sys\_vars.rocksdb\_deadlock\_detect\_basic to work
* [Revision #80be676fc0](https://github.com/MariaDB/server/commit/80be676fc0)\
  2017-01-11 17:32:47 +0300
  * MariaRocks port
* [Revision #edfe980aa1](https://github.com/MariaDB/server/commit/edfe980aa1)\
  2017-01-11 13:14:52 +0300
  * MariaRocks port: fix rocksdb.rpl\_row\_stats test
* [Revision #f89e07785a](https://github.com/MariaDB/server/commit/f89e07785a)\
  2017-01-11 12:41:22 +0300
  * MariaRocks port: Get rocksdb.autoinc\_vars\_thread test to work
* [Revision #520d206365](https://github.com/MariaDB/server/commit/520d206365)\
  2017-01-08 18:29:14 +0000
  * MariaRocks port: get rocksdb.rocksdb\_icp\[\_rev] to work
* [Revision #93d3a39ba9](https://github.com/MariaDB/server/commit/93d3a39ba9)\
  2017-01-07 19:43:27 +0000
  * MariaRocks port: fix rocksdb.rocksdb\_row\_stats test
* [Revision #ebbe59fa33](https://github.com/MariaDB/server/commit/ebbe59fa33)\
  2017-01-07 16:00:35 +0000
  * MariaRocks port: fix rocksdb.bloomfilter3 test
* [Revision #69d5ee58c6](https://github.com/MariaDB/server/commit/69d5ee58c6)\
  2017-01-06 23:36:23 +0300
  * MariaRocks port: Temporarily disable tests related to Gap Lock detector ([MDEV-11735](https://jira.mariadb.org/browse/MDEV-11735))
* [Revision #e3df50c4b9](https://github.com/MariaDB/server/commit/e3df50c4b9)\
  2017-01-03 00:21:04 +0300
  * MariaRocks port: fix rocksdb.table\_stats
* Merge [Revision #31b2237c68](https://github.com/MariaDB/server/commit/31b2237c68) 2017-01-02 21:09:31 +0000 - Merge branch '10.2' of github.com:MariaDB/server into 10.2-mariarocks
* [Revision #a597e0e164](https://github.com/MariaDB/server/commit/a597e0e164)\
  2017-01-02 22:50:35 +0300
  * MariaRocks port: fix tests - rocksdb.tmpdir works (however @@rocksdb\_tmpdir has no effect yet!) - trx\_info\_rpl is only run in RBR mode - type\_char\_indexes\_collation now works = take into account that characters with the same weight can have any order after sorting (and they do in MariaDB) = MariaDB doesn't use index-only for extended keys that have partially- covered columns.
* [Revision #3ecd9e0bfc](https://github.com/MariaDB/server/commit/3ecd9e0bfc)\
  2017-01-02 00:15:45 +0000
  * Post-merge fixes for rocksdb.add\_index\_inplace\_crash
* [Revision #7c4ebec82d](https://github.com/MariaDB/server/commit/7c4ebec82d)\
  2017-01-02 00:06:26 +0000
  * MariaRocks: trivial post-merge test fixes
* Merge [Revision #302ec9ab26](https://github.com/MariaDB/server/commit/302ec9ab26) 2017-01-01 23:33:50 +0000 - Merge branch '10.2-mariarocks' of github.com:MariaDB/server into 10.2-mariarocks
* [Revision #3e7e559150](https://github.com/MariaDB/server/commit/3e7e559150)\
  2017-01-01 01:50:17 +0300
  * Fix the "fatal error: mysqld\_error.h: No such file or directory" compile error
* Merge [Revision #d8288b306c](https://github.com/MariaDB/server/commit/d8288b306c) 2017-01-01 23:33:18 +0000 - Merge remote-tracking branch 'mergetrees/merge-myrocks' into 10.2-mariarocks
* [Revision #cfb59f3196](https://github.com/MariaDB/server/commit/cfb59f3196)\
  2016-12-31 23:30:09 +0300
  * Copy of commit f6ed777697db4ad7aee1e98c53243dced2b5891c Author: Chenyu Yan [seayan@outlook.com](mailto:seayan@outlook.com) Date: Thu Dec 29 16:10:25 2016 -0800
* [Revision #ae0a490eb3](https://github.com/MariaDB/server/commit/ae0a490eb3)\
  2016-12-31 22:08:05 +0300
  * MariaRocks port: Remove ifdef in ha\_rocksdb::set\_skip\_unique\_check\_tables
* [Revision #d1af31b3c2](https://github.com/MariaDB/server/commit/d1af31b3c2)\
  2016-12-31 21:31:50 +0300
  * MariaRocks port: Make rocksdb\_sys\_vars suite pass
* [Revision #d379963d73](https://github.com/MariaDB/server/commit/d379963d73)\
  2016-12-30 02:18:56 +0300
  * MariaRocks port: remove target\_lsn parameter of rocksdb\_flush\_wal
* [Revision #9ca608028f](https://github.com/MariaDB/server/commit/9ca608028f)\
  2016-12-27 00:13:32 +0000
  * MariaRocks port: make rocksdb.rocksdb\_qcache test pass
* [Revision #4faa9da81c](https://github.com/MariaDB/server/commit/4faa9da81c)\
  2016-12-27 01:55:05 +0300
  * MariaRocks port: Make SQL layer allow errors in start\_consistent\_snapshot().
* [Revision #8f2d58b26b](https://github.com/MariaDB/server/commit/8f2d58b26b)\
  2016-12-26 22:31:46 +0300
  * MariaRocks port: run rocksdb.rpl\_row\_stats with binlog\_format=row only
* [Revision #122bc4b54c](https://github.com/MariaDB/server/commit/122bc4b54c)\
  2016-12-26 19:12:16 +0000
  * MariaRocks port: Remove ifdef MARIAROCKS\_NOT\_YET in rocksdb\_start\_tx\_and\_assign\_read\_view
* [Revision #9f7dc2bbf5](https://github.com/MariaDB/server/commit/9f7dc2bbf5)\
  2016-12-15 20:56:27 +0300
  * MariaRocks port: make rocksdb.rpl\_savepoint pass
* [Revision #24224839d8](https://github.com/MariaDB/server/commit/24224839d8)\
  2016-12-15 19:25:32 +0300
  * MariaRocks port: make rocksdb.rpl\_statement\_not\_found work
* [Revision #0d3d2a5747](https://github.com/MariaDB/server/commit/0d3d2a5747)\
  2016-12-15 16:11:22 +0300
  * MariaRocks port: mark rocksdb.rpl\_statement to be run only in statement mode.
* [Revision #73c702eae5](https://github.com/MariaDB/server/commit/73c702eae5)\
  2016-12-15 15:34:56 +0300
  * MariaRocks port: fix rocksdb.rpl\_row\_rocksdb test
* [Revision #8e2cfde953](https://github.com/MariaDB/server/commit/8e2cfde953)\
  2016-12-04 23:55:54 +0300
  * MariaRocks port: fix rocksdb.collation, rocksdb.collation\_exception
* [Revision #34b66fcc98](https://github.com/MariaDB/server/commit/34b66fcc98)\
  2016-12-04 14:27:10 +0000
  * MariaRocks port: get rocksdb.locking\_issues test to work
* [Revision #7b708ee3ed](https://github.com/MariaDB/server/commit/7b708ee3ed)\
  2016-12-04 09:28:51 +0000
  * [MDEV-11329](https://jira.mariadb.org/browse/MDEV-11329): MariaRocks: rocksdb.add\_index\_inplace fails
* [Revision #05a593dfc9](https://github.com/MariaDB/server/commit/05a593dfc9)\
  2016-12-04 08:28:34 +0000
  * MariaRocks: temporary disable read-free replication
* [Revision #81c05c5931](https://github.com/MariaDB/server/commit/81c05c5931)\
  2016-12-03 20:56:40 +0000
  * MariaRocks port: disable rocksdb.select\_for\_update\_skip\_locked\_nowait
* [Revision #9a49210ec3](https://github.com/MariaDB/server/commit/9a49210ec3)\
  2016-12-03 20:37:45 +0000
  * MariaRocks port: disable rocksdb.slwo\_query\_log test ([MDEV-11480](https://jira.mariadb.org/browse/MDEV-11480))
* [Revision #aecc95a15c](https://github.com/MariaDB/server/commit/aecc95a15c)\
  2016-12-03 18:29:36 +0000
  * MariaRocks port: fix rocksdb.autoinc\_vars
* [Revision #044ad5d3d9](https://github.com/MariaDB/server/commit/044ad5d3d9)\
  2016-12-03 18:17:21 +0000
  * MariaRocks port: make rocksdb.show\_table\_status test pass
* [Revision #4f90605a3d](https://github.com/MariaDB/server/commit/4f90605a3d)\
  2016-12-03 14:56:38 +0000
  * MariaRocks port: make datetime-aware tests work in any timezone
* [Revision #00e3869a66](https://github.com/MariaDB/server/commit/00e3869a66)\
  2016-12-03 14:00:23 +0000
  * MariaRocks port: get rocksdb.checksum\_table to work
* [Revision #8018bb737c](https://github.com/MariaDB/server/commit/8018bb737c)\
  2016-12-03 12:52:34 +0000
  * MariaRocks port: use correct MTR command separators
* [Revision #b504c56bff](https://github.com/MariaDB/server/commit/b504c56bff)\
  2016-12-03 12:46:05 +0000
  * MariaRocks: test result MariaDB-fication
* [Revision #e6afa256e7](https://github.com/MariaDB/server/commit/e6afa256e7)\
  2016-12-03 12:42:30 +0000
  * MariaRocks port: Make ha\_rocksdb::index\_flags() return HA\_CLUSTERED\_INDEX for PK
* [Revision #0d5257215a](https://github.com/MariaDB/server/commit/0d5257215a)\
  2016-12-03 06:21:31 +0000
  * MariaRocks port: update test results
* [Revision #ec58a1cca8](https://github.com/MariaDB/server/commit/ec58a1cca8)\
  2016-12-03 06:17:57 +0000
  * MariaRocks port: update test results
* [Revision #d903396c18](https://github.com/MariaDB/server/commit/d903396c18)\
  2016-12-02 21:08:08 +0000
  * [MDEV-11321](https://jira.mariadb.org/browse/MDEV-11321): MariaRocks: type\_binary\_indexes, type\_blob\_indexes fail
* [Revision #7f43f736ac](https://github.com/MariaDB/server/commit/7f43f736ac)\
  2016-12-02 20:53:08 +0000
  * [MDEV-11477](https://jira.mariadb.org/browse/MDEV-11477): MariaRocks: rocksdb.type\_varchar failure
* [Revision #097bd3049c](https://github.com/MariaDB/server/commit/097bd3049c)\
  2016-12-02 20:49:10 +0000
  * MariaRocks port: update test results
* [Revision #9c083cd355](https://github.com/MariaDB/server/commit/9c083cd355)\
  2016-12-02 17:25:51 +0000
  * MariaRocks port: update test result for rocksdb.rocksdb\_parts
* [Revision #59d76665ee](https://github.com/MariaDB/server/commit/59d76665ee)\
  2016-12-02 15:35:36 +0000
  * MariaRocks port: Return correct value of HA\_PRIMARY\_KEY\_IN\_READ\_INDEX flag
* [Revision #f2219fe94d](https://github.com/MariaDB/server/commit/f2219fe94d)\
  2016-12-02 13:59:31 +0000
  * [MDEV-11462](https://jira.mariadb.org/browse/MDEV-11462): MariaRocks: rocksdb.type\_float\_indexes fails
* [Revision #9668b705f9](https://github.com/MariaDB/server/commit/9668b705f9)\
  2016-12-02 13:52:12 +0000
  * [MDEV-11462](https://jira.mariadb.org/browse/MDEV-11462): MariaRocks: rocksdb.type\_float\_indexes fails
* [Revision #6fb94c3e43](https://github.com/MariaDB/server/commit/6fb94c3e43)\
  2016-11-21 10:33:09 +0000
  * [MDEV-11320](https://jira.mariadb.org/browse/MDEV-11320): MariaRocks: rocksdb.type\_text\_indexes fails
* [Revision #3876f461a8](https://github.com/MariaDB/server/commit/3876f461a8)\
  2016-11-20 20:54:36 +0000
  * MariaRocks port: [MDEV-11318](https://jira.mariadb.org/browse/MDEV-11318): rocksdb.rocksdb test fails
* [Revision #a4c1b5bba8](https://github.com/MariaDB/server/commit/a4c1b5bba8)\
  2016-11-18 23:18:56 +0000
  * MariaRocks port: make rocksdb.alter\_table work
* [Revision #c12a1bb9c2](https://github.com/MariaDB/server/commit/c12a1bb9c2)\
  2016-11-18 21:05:49 +0000
  * MariaRocks port: more testcase fixes
* [Revision #c82f573879](https://github.com/MariaDB/server/commit/c82f573879)\
  2016-11-02 13:35:49 -0400
  * Use https instead of ssh(git@) for rocksdb submodule.
* [Revision #e370d0a9ae](https://github.com/MariaDB/server/commit/e370d0a9ae)\
  2016-11-13 18:31:09 +0000
  * MariaRocks port: Make rocksdb.compression\_zstd test skip itself when ZSTD is not supported
* [Revision #75f00a3388](https://github.com/MariaDB/server/commit/75f00a3388)\
  2016-11-13 11:40:13 +0000
  * MariaRocks port: move --ignore-db-dirs back to suite.opt
* [Revision #826753942f](https://github.com/MariaDB/server/commit/826753942f)\
  2016-11-12 09:20:36 +0000
  * MariaRocks port: temporarily? update ER\_LOCK\_WAIT\_TIMEOUT error messages
* [Revision #a5f72fb3c2](https://github.com/MariaDB/server/commit/a5f72fb3c2)\
  2016-11-12 06:56:39 +0000
  * MariaRocks port: put MyRocks options into rocksdb/my.cnf
* [Revision #c4270952b7](https://github.com/MariaDB/server/commit/c4270952b7)\
  2016-11-12 06:09:13 +0000
  * MariaRocks port: fix rocksdb.rocksdb\_checksums to work for MariaDB in the mornings
* [Revision #0f1821db19](https://github.com/MariaDB/server/commit/0f1821db19)\
  2016-11-12 05:15:06 +0000
  * MariaRocks port: make rocksdb.rocksdb\_cf\_options test pass
* [Revision #183ab78bab](https://github.com/MariaDB/server/commit/183ab78bab)\
  2016-11-12 04:48:47 +0000
  * MariaRocks port: more test result updates, again
* [Revision #223c14e706](https://github.com/MariaDB/server/commit/223c14e706)\
  2016-11-10 22:50:01 +0000
  * MariaRocks port: more test result updates
* [Revision #792aaedb42](https://github.com/MariaDB/server/commit/792aaedb42)\
  2016-11-10 21:32:31 +0000
  * MariaRocks port: Use another way to handle --force-restart
* [Revision #8014a942b7](https://github.com/MariaDB/server/commit/8014a942b7)\
  2016-11-10 20:36:24 +0000
  * MariaRocks port: update results for rocksdb.col\_opt\_null test.
* [Revision #ce9aeb888e](https://github.com/MariaDB/server/commit/ce9aeb888e)\
  2016-11-07 02:49:49 +0300
  * MariaRocks port: Support --force-restart "pseudo-argument", part#2
* [Revision #600a2075b5](https://github.com/MariaDB/server/commit/600a2075b5)\
  2016-11-06 22:18:11 +0000
  * MariaRocks port: more of testcase Maria-fication
* [Revision #f246829e2f](https://github.com/MariaDB/server/commit/f246829e2f)\
  2016-11-07 01:05:55 +0300
  * MariaRocks port: Support --force-restart "pseudo-argument"
* [Revision #df407fca0b](https://github.com/MariaDB/server/commit/df407fca0b)\
  2016-11-05 23:19:09 +0000
  * MariaRocks port: fix a few more testcases
* [Revision #0ab7cb236e](https://github.com/MariaDB/server/commit/0ab7cb236e)\
  2016-11-05 22:29:02 +0000
  * MariaRocks port: More of testcase Maria-fication
* [Revision #a42b9003f4](https://github.com/MariaDB/server/commit/a42b9003f4)\
  2016-11-05 19:23:18 +0000
  * MariaRocks port: more of testcase Maria-fication
* [Revision #ece3ab3702](https://github.com/MariaDB/server/commit/ece3ab3702)\
  2016-11-05 17:20:33 +0000
  * MariaRocks port: add have\_rocksdb.opt which enables MyRocks' plugins
* [Revision #997c86c76c](https://github.com/MariaDB/server/commit/997c86c76c)\
  2016-10-30 21:07:16 +0000
  * MariaRocks port: fix rocksdb.handler\_basic test
* [Revision #4462e77afa](https://github.com/MariaDB/server/commit/4462e77afa)\
  2016-10-29 13:23:42 +0000
  * MariaRocks port: update result for rocksdb.type\_char\_indexes (see [MDEV-11172](https://jira.mariadb.org/browse/MDEV-11172))
* [Revision #15f2bcfa94](https://github.com/MariaDB/server/commit/15f2bcfa94)\
  2016-10-29 00:30:01 +0000
  * MariaRocks port: get rid of "invalid table name" in the error log
* [Revision #1d1211ab1a](https://github.com/MariaDB/server/commit/1d1211ab1a)\
  2016-10-29 00:23:58 +0000
  * MariaRocks port: trivial Maria-fication of test results
* [Revision #9826edb6b8](https://github.com/MariaDB/server/commit/9826edb6b8)\
  2016-10-27 00:32:59 +0300
  * MariaRocks port: fix a few test result differences, part#2.
* [Revision #f23a0093e1](https://github.com/MariaDB/server/commit/f23a0093e1)\
  2016-10-26 23:56:59 +0300
  * MariaRocks port: fix a few test result differences
* [Revision #e9ee999e77](https://github.com/MariaDB/server/commit/e9ee999e77)\
  2016-10-25 15:01:27 +0000
  * MariaRocks port: "get rid of Invalid (old?) table or database name" error
* [Revision #bc646ee881](https://github.com/MariaDB/server/commit/bc646ee881)\
  2016-10-24 20:55:26 +0000
  * MariaRocks: fix a bug in MariaDB: SHOW STATUS LIKE shows extra rows
* [Revision #1d1b10e93c](https://github.com/MariaDB/server/commit/1d1b10e93c)\
  2016-10-24 20:51:44 +0000
  * MariaRocks: rocksdb.rocksdb fails with a duplicate key error
* [Revision #3ac33f8cdb](https://github.com/MariaDB/server/commit/3ac33f8cdb)\
  2016-10-24 12:04:01 +0000
  * MariaRocks: fix a compilation problem
* [Revision #8d8858c10a](https://github.com/MariaDB/server/commit/8d8858c10a)\
  2016-10-24 10:38:18 +0000
  * MariaRocks: trying to get the MTR tests to work
* [Revision #015617879a](https://github.com/MariaDB/server/commit/015617879a)\
  2016-10-24 10:35:56 +0000
  * MariaRocks port: fix a typo in test\_if\_order\_by\_key()
* [Revision #680a206b13](https://github.com/MariaDB/server/commit/680a206b13)\
  2016-10-23 18:28:07 +0000
  * MariaRocks port: compile the needed files with -frtti
* [Revision #fd4e83eb32](https://github.com/MariaDB/server/commit/fd4e83eb32)\
  2016-10-21 21:27:23 +0000
  * MariaRocks port: update ha\_rocksdb::delete\_all\_rows() to match the definition in class handler
* [Revision #e22b271b39](https://github.com/MariaDB/server/commit/e22b271b39)\
  2016-10-21 21:11:47 +0000
  * MariaRocks port: compilation fixes
* [Revision #86d963eb08](https://github.com/MariaDB/server/commit/86d963eb08)\
  2016-10-21 20:05:40 +0000
  * MariaRocks port: provide timeout\_message()
* [Revision #8c5912e9ee](https://github.com/MariaDB/server/commit/8c5912e9ee)\
  2016-10-19 14:27:43 +0000
  * MariaRocks port: temporarily disable gap lock checking
* [Revision #fe0b57dfbe](https://github.com/MariaDB/server/commit/fe0b57dfbe)\
  2016-10-19 13:16:51 +0000
  * MariaRocks port: disable more code that synchronizes with the binlog
* [Revision #085fa3e4bc](https://github.com/MariaDB/server/commit/085fa3e4bc)\
  2016-10-19 12:15:59 +0000
  * MariaRocks port: rli\_slave is called rgi\_slave in MariaDB.
* [Revision #e951fd17e8](https://github.com/MariaDB/server/commit/e951fd17e8)\
  2016-10-19 12:00:22 +0000
  * MariaRocks port: make rocksdb\_flush\_wal() match handlerton::flush\_logs definition
* [Revision #960fbc38d6](https://github.com/MariaDB/server/commit/960fbc38d6)\
  2016-10-17 16:53:20 +0000
  * MariaRocks port: temporarily? disable "CONSISTENT INNODB|ROCKSDB SNAPSHOT" feature
* [Revision #0a132ae7a2](https://github.com/MariaDB/server/commit/0a132ae7a2)\
  2016-10-16 18:38:34 +0000
  * MariaRocks: disable more of my\_io\_perf\_t usage
* [Revision #fdf026a4ad](https://github.com/MariaDB/server/commit/fdf026a4ad)\
  2016-10-16 18:07:35 +0000
  * MariaRocks port: s/my\_core::thd\_killed/thd\_killed/
* [Revision #9b78cd3cac](https://github.com/MariaDB/server/commit/9b78cd3cac)\
  2016-10-16 18:02:28 +0000
  * MariaRocks port: MariaDB doesn't support SHOW ENGINE ROCKSDB TRANSACTION STATUS
* [Revision #c6dee75759](https://github.com/MariaDB/server/commit/c6dee75759)\
  2016-10-16 14:34:46 +0000
  * MariaRocks: MariaDB doesnt support ICP over backwards index scans yet
* [Revision #54295beee2](https://github.com/MariaDB/server/commit/54295beee2)\
  2016-10-16 14:28:22 +0000
  * MariaRocks port: compare\_key\_icp() is called compare\_key2() in MariaDB
* [Revision #8cde1d449a](https://github.com/MariaDB/server/commit/8cde1d449a)\
  2016-10-16 14:16:58 +0000
  * MariaRocks port: disable thd\_store\_lsn() call
* [Revision #1dead2d213](https://github.com/MariaDB/server/commit/1dead2d213)\
  2016-10-16 14:06:25 +0000
  * MariaRocks port: MariaDB has no "ASYNC\_COMMIT" feature
* [Revision #e43ce18597](https://github.com/MariaDB/server/commit/e43ce18597)\
  2016-10-16 12:45:53 +0000
  * MariaRocks port: use correct path in CMakeLists.txt
* [Revision #27adea907b](https://github.com/MariaDB/server/commit/27adea907b)\
  2016-10-16 12:30:51 +0000
  * MariaRocks port: temporarily disable rdb\_collation\_exceptions
* [Revision #7eef3de1ae](https://github.com/MariaDB/server/commit/7eef3de1ae)\
  2016-10-16 11:56:14 +0000
  * MariaRocks port: In MariaDB, there's no Field\_longlong::PACK\_LENGTH
* [Revision #b42248d2f2](https://github.com/MariaDB/server/commit/b42248d2f2)\
  2016-10-16 11:39:55 +0000
  * MyRocks port: make Field::char\_length() a const function
* [Revision #a7091b0679](https://github.com/MariaDB/server/commit/a7091b0679)\
  2016-10-16 11:17:19 +0000
  * Temporarily disable Read-Free replication in MariaRocks, part#2
* [Revision #d26283458c](https://github.com/MariaDB/server/commit/d26283458c)\
  2016-10-16 11:01:01 +0000
  * MariaRocks port: make key\_restore() parameter const
* [Revision #274e5be194](https://github.com/MariaDB/server/commit/274e5be194)\
  2016-10-16 11:00:07 +0000
  * MariaRocks: port my\_hash\_const\_element
* [Revision #f456532c62](https://github.com/MariaDB/server/commit/f456532c62)\
  2016-10-15 21:20:52 +0000
  * MariaRocks port: compile RocksDB with -frtti.
* [Revision #01a5216b9c](https://github.com/MariaDB/server/commit/01a5216b9c)\
  2016-10-15 20:58:15 +0000
  * MariaRocks port: temporarily? disable Per-table Extra Stats
* [Revision #746f35d6f3](https://github.com/MariaDB/server/commit/746f35d6f3)\
  2016-10-10 18:54:43 +0000
  * MariaRocks: Disable FlashCache support
* [Revision #0c5823ab9e](https://github.com/MariaDB/server/commit/0c5823ab9e)\
  2016-10-09 18:22:23 +0000
  * MariaRocks port: mysql\_bin\_log\_is\_open -> mysql\_bin\_log.is\_open
* [Revision #06b4962fc4](https://github.com/MariaDB/server/commit/06b4962fc4)\
  2016-10-09 18:11:00 +0000
  * MariaRocks port: db\_low\_byte\_first is gone in MariaDB
* [Revision #08f96d21fd](https://github.com/MariaDB/server/commit/08f96d21fd)\
  2016-10-09 18:01:39 +0000
  * MariaRocks: add DB\_TYPE\_ROCKSDB into legacy\_db\_type enum
* [Revision #2770e8004d](https://github.com/MariaDB/server/commit/2770e8004d)\
  2016-10-09 17:52:01 +0000
  * MariaRocks: remove ha\_statistic\_increment calls
* [Revision #3af9986289](https://github.com/MariaDB/server/commit/3af9986289)\
  2016-10-09 17:30:16 +0000
  * MariaRocks port: dir\_entry has number\_of\_files with one 'f' in MariaDB
* [Revision #a06faac248](https://github.com/MariaDB/server/commit/a06faac248)\
  2016-10-09 17:24:01 +0000
  * Temporarily disable the fix for WebScaleSQL Issue #108.
* [Revision #50f323683a](https://github.com/MariaDB/server/commit/50f323683a)\
  2016-10-09 17:20:11 +0000
  * Add a temporary stand-in for abort\_with\_stack\_traces() call
* [Revision #f4994c7872](https://github.com/MariaDB/server/commit/f4994c7872)\
  2016-10-09 17:03:31 +0000
  * [MDEV-10975](https://jira.mariadb.org/browse/MDEV-10975): Merging of @@rocksdb\_skip\_unique\_check: Part #1
* [Revision #d3cd64fda9](https://github.com/MariaDB/server/commit/d3cd64fda9)\
  2016-10-09 16:03:39 +0000
  * In MariaDB, KEY::actual\_key\_parts is named ext\_key\_parts
* [Revision #84dd64702a](https://github.com/MariaDB/server/commit/84dd64702a)\
  2016-10-09 16:02:13 +0000
  * Fix compilation failure in rdb\_perf\_context.h
* [Revision #20bd26e6df](https://github.com/MariaDB/server/commit/20bd26e6df)\
  2016-10-09 15:27:22 +0000
  * Backport from facebook/mysql-5.6:
* [Revision #4be8cae56a](https://github.com/MariaDB/server/commit/4be8cae56a)\
  2016-10-09 14:39:00 +0000
  * Temporarily disable Read-Free replication in MariaRocks
* [Revision #272c05df56](https://github.com/MariaDB/server/commit/272c05df56)\
  2016-10-09 13:02:48 +0000
  * Temporarily (?) disable read-free replication in MariaRocks
* [Revision #d4f6c77ccc](https://github.com/MariaDB/server/commit/d4f6c77ccc)\
  2016-10-09 12:59:40 +0000
  * Temporarily (?) disable table statistics updates
* [Revision #7c3affdcc0](https://github.com/MariaDB/server/commit/7c3affdcc0)\
  2016-10-09 12:36:58 +0000
  * Add #include \<my\_config.h> at the start of every .cc file
* [Revision #a482f2221d](https://github.com/MariaDB/server/commit/a482f2221d)\
  2016-10-07 08:25:10 +0000
  * Fix MariaRocks build (unfinished)
* [Revision #be33178833](https://github.com/MariaDB/server/commit/be33178833)\
  2016-10-06 17:46:44 +0000
  * Add rocksdb submodule
* Merge [Revision #c680acd6a3](https://github.com/MariaDB/server/commit/c680acd6a3) 2016-10-06 17:31:12 +0000 - Merge remote-tracking branch 'mergetrees/merge-myrocks' into bb-10.2-mariarocks
* [Revision #ebfc4e6ad0](https://github.com/MariaDB/server/commit/ebfc4e6ad0)\
  2016-10-06 17:24:09 +0000
  * Initial commit, copy of commit 86587affafe77ef555f7c3839839de44f0f203f3 Author: Tian Xia [tianx@fb.com](mailto:tianx@fb.com) Date: Tue Oct 4 10:01:52 2016 -0700

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
