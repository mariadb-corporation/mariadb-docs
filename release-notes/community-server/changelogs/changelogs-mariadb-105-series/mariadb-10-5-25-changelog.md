# MariaDB 10.5.25 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.25](https://downloads.mariadb.org/mariadb/10.5.25/)[Release Notes](../../old-releases/10.5/10.5.25.md)[Changelog](mariadb-10-5-25-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 16 May 2024

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.25.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.34](../changelogs-mariadb-10-4-series/mariadb-10-4-34-changelog.md)
* [Revision #29c185bd77](https://github.com/MariaDB/server/commit/29c185bd77)\
  2024-05-08 09:31:10 +0200
  * test needs to cleanup after itself
* [Revision #938b929372](https://github.com/MariaDB/server/commit/938b929372)\
  2024-05-08 18:29:45 +0200
  * don't wait indefinitely for signal handler in --bootstrap
* [Revision #360a7ff760](https://github.com/MariaDB/server/commit/360a7ff760)\
  2024-05-08 10:52:28 +0200
  * fix tests after 349ca2be7437
* [Revision #1c425a8d85](https://github.com/MariaDB/server/commit/1c425a8d85)\
  2024-05-08 10:31:28 +0200
  * [MDEV-33727](https://jira.mariadb.org/browse/MDEV-33727) update test results
* [Revision #6f003b5d07](https://github.com/MariaDB/server/commit/6f003b5d07)\
  2024-05-04 10:06:11 +0200
  * [MDEV-29955](https://jira.mariadb.org/browse/MDEV-29955) post-fix - add CMake policy CMP0074, so ZLIB\_ROOT is not ignored
* [Revision #22d4fbeb62](https://github.com/MariaDB/server/commit/22d4fbeb62)\
  2024-05-04 10:02:21 +0200
  * Define CMake policy list, like it is done in 10.6+
* [Revision #40b3525fcc](https://github.com/MariaDB/server/commit/40b3525fcc)\
  2024-05-07 14:10:35 +0300
  * [MDEV-28621](https://jira.mariadb.org/browse/MDEV-28621): group by optimization incorrectly removing subquery where subject buried in a function
* [Revision #ec6aa9ac42](https://github.com/MariaDB/server/commit/ec6aa9ac42)\
  2024-05-07 17:21:01 +0300
  * [MDEV-34055](https://jira.mariadb.org/browse/MDEV-34055) Assertion '...' failure or corruption errors upon REPAIR on Aria tables
* [Revision #4bc1860eb4](https://github.com/MariaDB/server/commit/4bc1860eb4)\
  2024-04-30 21:31:47 +0200
  * [MDEV-23878](https://jira.mariadb.org/browse/MDEV-23878) Wrong result with semi-join and splittable derived table
* [Revision #10a7599286](https://github.com/MariaDB/server/commit/10a7599286)\
  2024-04-30 14:00:43 +1000
  * [MDEV-34036](https://jira.mariadb.org/browse/MDEV-34036) Reset spider\_hton\_ptr in spider\_db\_done()
* [Revision #42c99ef0d4](https://github.com/MariaDB/server/commit/42c99ef0d4)\
  2024-05-07 09:38:29 +0200
  * [MDEV-19949](https://jira.mariadb.org/browse/MDEV-19949) `mariadb-backup --password` test
* [Revision #421eeb18b8](https://github.com/MariaDB/server/commit/421eeb18b8)\
  2024-05-07 09:39:02 +0200
  * Revert "[MDEV-19949](https://jira.mariadb.org/browse/MDEV-19949) mariadb-backup option of '--password' or '-p' without specifying password in commandline"
* [Revision #33e4fbf045](https://github.com/MariaDB/server/commit/33e4fbf045)\
  2024-04-12 15:40:11 +0300
  * [MDEV-33898](https://jira.mariadb.org/browse/MDEV-33898) : Galera test failure on galera.MW-369
* [Revision #bca366e4a1](https://github.com/MariaDB/server/commit/bca366e4a1)\
  2024-05-07 10:16:38 +1000
  * [MDEV-34098](https://jira.mariadb.org/browse/MDEV-34098) source start\_slave.inc in spider suites
* [Revision #89084c2ea4](https://github.com/MariaDB/server/commit/89084c2ea4)\
  2024-05-02 11:44:02 -0400
  * [MDEV-33078](https://jira.mariadb.org/browse/MDEV-33078) SysInfo.pm reports incorrect CPU count on macOS
* [Revision #7ed9d2ac00](https://github.com/MariaDB/server/commit/7ed9d2ac00)\
  2024-05-06 20:12:32 +0200
  * [MDEV-9179](https://jira.mariadb.org/browse/MDEV-9179) When binlog\_annotate\_row\_events on , event of binlog file is truncated
* Merge [Revision #7eeba92520](https://github.com/MariaDB/server/commit/7eeba92520) 2024-05-06 17:17:18 +0200 - Merge branch '10.4' into 10.5
* [Revision #13663cb5c4](https://github.com/MariaDB/server/commit/13663cb5c4)\
  2024-05-05 17:37:37 +0200
  * [MDEV-33727](https://jira.mariadb.org/browse/MDEV-33727) mariadb-dump trusts the server and does not validate the data
* [Revision #2025597c0b](https://github.com/MariaDB/server/commit/2025597c0b)\
  2024-05-05 09:44:10 +0200
  * [MDEV-21778](https://jira.mariadb.org/browse/MDEV-21778) Disable system commands in mysql/mariadb client
* [Revision #83aedeacc4](https://github.com/MariaDB/server/commit/83aedeacc4)\
  2024-05-05 10:29:41 +0200
  * cleanup: remove attribute((unused)) from mysql.cc
* [Revision #994a0de96b](https://github.com/MariaDB/server/commit/994a0de96b)\
  2024-05-05 09:28:25 +0200
  * cleanup: reorder mysql help output
* [Revision #98b157fdee](https://github.com/MariaDB/server/commit/98b157fdee)\
  2024-05-04 17:05:29 +0200
  * cleanup: unused OPT\_xxx and client\_priv.h
* [Revision #22b3ba9312](https://github.com/MariaDB/server/commit/22b3ba9312)\
  2024-04-27 15:15:37 +0200
  * [MDEV-25102](https://jira.mariadb.org/browse/MDEV-25102) UNIQUE USING HASH error after ALTER ... DISABLE KEYS
* [Revision #9b2bf09b95](https://github.com/MariaDB/server/commit/9b2bf09b95)\
  2024-05-06 19:49:11 +0530
  * [MDEV-33980](https://jira.mariadb.org/browse/MDEV-33980) mariadb-backup --backup is missing retry logic for undo tablespaces
* Merge [Revision #b88c20ce1b](https://github.com/MariaDB/server/commit/b88c20ce1b) 2024-05-06 13:55:42 +0200 - Merge branch 10.4 into 10.5
* [Revision #55754be20c](https://github.com/MariaDB/server/commit/55754be20c)\
  2024-05-06 13:34:39 +0300
  * [MDEV-33781](https://jira.mariadb.org/browse/MDEV-33781): rocksdb.locking\_issues\_case5\_rc fails windows ... : Disable it
* [Revision #f90fcefdb2](https://github.com/MariaDB/server/commit/f90fcefdb2)\
  2024-05-06 13:31:31 +0300
  * [MDEV-33866](https://jira.mariadb.org/browse/MDEV-33866): rocksdb.write\_sync fails on windows ... : Disable it
* [Revision #be60782103](https://github.com/MariaDB/server/commit/be60782103)\
  2024-05-06 13:06:14 +0300
  * [MDEV-33789](https://jira.mariadb.org/browse/MDEV-33789): rocksdb.bloomfilter2 failed on ... : Disable it.
* [Revision #52c45332a8](https://github.com/MariaDB/server/commit/52c45332a8)\
  2024-05-03 15:16:25 +0200
  * [MDEV-34071](https://jira.mariadb.org/browse/MDEV-34071): Failure during the galera\_3nodes\_sr.GCF-336 test
* [Revision #4045a87bcb](https://github.com/MariaDB/server/commit/4045a87bcb)\
  2024-04-28 10:39:37 +0200
  * test for Bug #16051817 GOT ERROR 124 FROM STORAGE ENGINE ON DELETE FROM A PARTITIONED TABLE
* [Revision #3d75cffa91](https://github.com/MariaDB/server/commit/3d75cffa91)\
  2024-04-28 10:38:32 +0200
  * bugfix: INFORMATION\_SCHEMA.STATISTICS doesn't show whether the index is disabled
* [Revision #179515a68c](https://github.com/MariaDB/server/commit/179515a68c)\
  2024-04-28 09:45:16 +0200
  * bugfix: dgcov.pl shows wrong line numbers
* [Revision #4f5dea43df](https://github.com/MariaDB/server/commit/4f5dea43df)\
  2024-04-26 16:27:29 +0200
  * cleanup
* [Revision #947eeaa6dc](https://github.com/MariaDB/server/commit/947eeaa6dc)\
  2024-05-02 09:55:59 +0200
  * [MDEV-29345](https://jira.mariadb.org/browse/MDEV-29345) update case insensitive (large) unique key with insensitive change of value - duplicate key
* [Revision #91fb8b7fd3](https://github.com/MariaDB/server/commit/91fb8b7fd3)\
  2024-04-29 22:41:07 +0200
  * [MDEV-19949](https://jira.mariadb.org/browse/MDEV-19949) mariadb-backup option of '--password' or '-p' without specifying password in commandline
* [Revision #cd0356a764](https://github.com/MariaDB/server/commit/cd0356a764)\
  2024-04-27 13:35:48 +0300
  * [MDEV-34077](https://jira.mariadb.org/browse/MDEV-34077) scripts/mariadb-install-db: Error in my\_thread\_global\_end(): 1 threads didn't exit
* [Revision #983e6ca097](https://github.com/MariaDB/server/commit/983e6ca097)\
  2024-05-04 21:02:53 +0200
  * bugfix: buffer overwrite in mariadb-backup
* [Revision #349ca2be74](https://github.com/MariaDB/server/commit/349ca2be74)\
  2024-04-29 15:59:13 +0200
  * mtr: remove innodb combinations
* [Revision #df6899b30b](https://github.com/MariaDB/server/commit/df6899b30b)\
  2024-05-03 16:21:41 +0200
  * bugfix: mysqld --safe-mode crashes
* [Revision #d74fee9e8c](https://github.com/MariaDB/server/commit/d74fee9e8c)\
  2024-05-05 17:02:09 +0200
  * [MDEV-19487](https://jira.mariadb.org/browse/MDEV-19487) fix for --view
* [Revision #03295f0c20](https://github.com/MariaDB/server/commit/03295f0c20)\
  2024-05-05 17:13:20 +0200
  * [MDEV-30727](https://jira.mariadb.org/browse/MDEV-30727) Check spider\_hton\_ptr in spider udfs
* [Revision #7a789e2027](https://github.com/MariaDB/server/commit/7a789e2027)\
  2024-04-25 12:47:23 +0200
  * sporadic failures of rpl.rpl\_parallel\_sbm
* [Revision #cea083af9f](https://github.com/MariaDB/server/commit/cea083af9f)\
  2024-04-24 22:08:52 +0200
  * cleanup: use THD\_STAGE\_INFO, not thd\_proc\_info
* [Revision #cb7c99674e](https://github.com/MariaDB/server/commit/cb7c99674e)\
  2024-05-05 16:54:50 +0200
  * sporadic failure of perfschema.func\_file\_io
* [Revision #72429cad7f](https://github.com/MariaDB/server/commit/72429cad7f)\
  2022-12-28 23:05:46 +0300
  * [MDEV-30046](https://jira.mariadb.org/browse/MDEV-30046) wrong row targeted with "insert ... on duplicate" and "replace"
* [Revision #7f161a5c58](https://github.com/MariaDB/server/commit/7f161a5c58)\
  2024-05-05 15:28:37 +0400
  * [MDEV-34088](https://jira.mariadb.org/browse/MDEV-34088) The TIMESTAMP value of '1970-01-01 00:00:00' can be indirectly inserted in strict mode
* [Revision #2c19877015](https://github.com/MariaDB/server/commit/2c19877015)\
  2024-05-04 23:41:55 +0400
  * [MDEV-34061](https://jira.mariadb.org/browse/MDEV-34061) unix\_timestamp(coalesce(timestamp\_column)) returns NULL on '1970-01-01 00:00:00.000001'
* [Revision #1cdf22374b](https://github.com/MariaDB/server/commit/1cdf22374b)\
  2024-05-04 22:34:14 +0400
  * [MDEV-34069](https://jira.mariadb.org/browse/MDEV-34069) Zero datetime reinterprets as '1970-01-01 00:00:00' on field\_datetime=field\_timestamp
* [Revision #88f49da8e0](https://github.com/MariaDB/server/commit/88f49da8e0)\
  2024-05-03 21:48:26 +0200
  * [MDEV-34063](https://jira.mariadb.org/browse/MDEV-34063) tpool - integer overflow in multiplication.
* [Revision #b18259ecf5](https://github.com/MariaDB/server/commit/b18259ecf5)\
  2024-05-03 13:24:06 +0200
  * Compiling - Fix MSVC compile warnings, on x86
* [Revision #029e2a5fd9](https://github.com/MariaDB/server/commit/029e2a5fd9)\
  2024-05-02 23:11:38 +0200
  * [MDEV-33876](https://jira.mariadb.org/browse/MDEV-33876) CMake, zlib - use names compatible with official FindZLIB.cmake
* [Revision #9ec7819c58](https://github.com/MariaDB/server/commit/9ec7819c58)\
  2024-05-03 15:55:20 +0300
  * [MDEV-33817](https://jira.mariadb.org/browse/MDEV-33817): AVX512BW and VPCLMULQDQ based CRC-32
* [Revision #611cd6b981](https://github.com/MariaDB/server/commit/611cd6b981)\
  2024-05-03 13:06:13 +0300
  * [MDEV-33817](https://jira.mariadb.org/browse/MDEV-33817) preparation: Restructuring and unit tests
* [Revision #b84d335d9d](https://github.com/MariaDB/server/commit/b84d335d9d)\
  2024-03-04 10:25:34 +1100
  * [MDEV-33538](https://jira.mariadb.org/browse/MDEV-33538) make auxiliary spider plugins init depend on actual spider
* [Revision #20f60fe70f](https://github.com/MariaDB/server/commit/20f60fe70f)\
  2024-05-02 21:41:13 +0200
  * postfix a09ebe5567694f13dd77876bf61ce3560dfed0e6 (PCRE-10.43)
* [Revision #e63ed4e004](https://github.com/MariaDB/server/commit/e63ed4e004)\
  2024-03-08 16:27:23 +1100
  * [MDEV-33631](https://jira.mariadb.org/browse/MDEV-33631) Ubuntu/Debian MYSQL\_SERVER\_SUFFIX is version+suffix on MariaDB packaged versions
* [Revision #bf77f9793d](https://github.com/MariaDB/server/commit/bf77f9793d)\
  2024-04-13 23:29:11 +0100
  * openssl: add a more specific DES support detection
* [Revision #f9575495ce](https://github.com/MariaDB/server/commit/f9575495ce)\
  2024-04-28 16:51:04 +0000
  * Fix typo
* [Revision #9e6858a426](https://github.com/MariaDB/server/commit/9e6858a426)\
  2024-03-16 00:28:48 +0530
  * [MDEV-22141](https://jira.mariadb.org/browse/MDEV-22141): JSON\_REMOVE returns NULL on valid arguments
* [Revision #5ca64e65d0](https://github.com/MariaDB/server/commit/5ca64e65d0)\
  2024-03-19 00:04:47 +0530
  * [MDEV-32287](https://jira.mariadb.org/browse/MDEV-32287): JSON\_EXTRACT not returning multiple values for same path
* [Revision #d7df63e1c9](https://github.com/MariaDB/server/commit/d7df63e1c9)\
  2024-03-19 01:30:13 +0530
  * [MDEV-19487](https://jira.mariadb.org/browse/MDEV-19487): JSON\_TYPE doesnt detect the type of String Values (returns NULL) and for Date/DateTime returns "INTEGER"
* [Revision #c6e3fe29d4](https://github.com/MariaDB/server/commit/c6e3fe29d4)\
  2024-04-27 08:54:38 +0400
  * [MDEV-30646](https://jira.mariadb.org/browse/MDEV-30646) View created via JSON\_ARRAYAGG returns incorrect json object
* [Revision #dc25d600ee](https://github.com/MariaDB/server/commit/dc25d600ee)\
  2024-04-24 16:54:00 +0400
  * [MDEV-21058](https://jira.mariadb.org/browse/MDEV-21058) CREATE TABLE with generated column and RLIKE results in sigabrt
* [Revision #267dd5a993](https://github.com/MariaDB/server/commit/267dd5a993)\
  2024-04-29 16:17:22 +1000
  * [MDEV-30727](https://jira.mariadb.org/browse/MDEV-30727) Check spider\_hton\_ptr in spider udfs
* [Revision #bda8d4fdf7](https://github.com/MariaDB/server/commit/bda8d4fdf7)\
  2024-04-26 18:34:27 +0200
  * require boost 1.53 for columnstore
* [Revision #a09ebe5567](https://github.com/MariaDB/server/commit/a09ebe5567)\
  2024-04-26 14:44:38 +0200
  * PCRE2-10.43
* [Revision #3141a68b7c](https://github.com/MariaDB/server/commit/3141a68b7c)\
  2024-04-26 11:57:25 +0400
  * [MDEV-33534](https://jira.mariadb.org/browse/MDEV-33534) UBSAN: Negation of -X cannot be represented in type 'long long int'; cast to an unsigned type to negate this value to itself in my\_double\_round from sql/item\_func.cc|
* [Revision #3d41747625](https://github.com/MariaDB/server/commit/3d41747625)\
  2024-03-20 12:46:39 -0700
  * [MDEV-33574](https://jira.mariadb.org/browse/MDEV-33574) Improve mysqlbinlog error message
* [Revision #b3e531a3cc](https://github.com/MariaDB/server/commit/b3e531a3cc)\
  2024-04-12 10:10:29 +0300
  * [MDEV-33896](https://jira.mariadb.org/browse/MDEV-33896) : Galera test failure on galera\_3nodes.[MDEV-29171](https://jira.mariadb.org/browse/MDEV-29171)
* [Revision #10d251e05a](https://github.com/MariaDB/server/commit/10d251e05a)\
  2024-04-25 15:52:38 +0300
  * [MDEV-26450](https://jira.mariadb.org/browse/MDEV-26450) fixup: Remove a bogus assertion
* [Revision #553a4d6271](https://github.com/MariaDB/server/commit/553a4d6271)\
  2024-04-23 21:02:08 +0200
  * [MDEV-33602](https://jira.mariadb.org/browse/MDEV-33602): Sporadic test failure in rpl.rpl\_gtid\_stop\_start
* [Revision #a1c1f5029e](https://github.com/MariaDB/server/commit/a1c1f5029e)\
  2024-04-25 11:05:03 +0300
  * [MDEV-33974](https://jira.mariadb.org/browse/MDEV-33974) Enable GNU libstdc++ debugging
* [Revision #7229384256](https://github.com/MariaDB/server/commit/7229384256)\
  2024-04-25 07:48:57 +0300
  * [MDEV-23974](https://jira.mariadb.org/browse/MDEV-23974) fixup: Cover all debug builds
* [Revision #7d5e08de6b](https://github.com/MariaDB/server/commit/7d5e08de6b)\
  2024-04-24 18:08:46 +0200
  * [MDEV-20157](https://jira.mariadb.org/browse/MDEV-20157) perfschema.stage\_mdl\_function failed in buildbot with wrong result
* [Revision #259394aed7](https://github.com/MariaDB/server/commit/259394aed7)\
  2024-04-23 15:11:52 +0200
  * disable mariadb-backup.incremental\_encrypted,64k on 32bit
* [Revision #e2f95ebbcb](https://github.com/MariaDB/server/commit/e2f95ebbcb)\
  2024-04-23 14:45:23 +0200
  * fix galera\_3nodes.galera\_gtid\_consistency to work with nc
* [Revision #55cb2c2916](https://github.com/MariaDB/server/commit/55cb2c2916)\
  2024-03-13 20:16:56 +0000
  * [MDEV-29955](https://jira.mariadb.org/browse/MDEV-29955): Set path for zlib library with pkg-config
* [Revision #e73181112f](https://github.com/MariaDB/server/commit/e73181112f)\
  2024-04-23 10:55:17 +0200
  * [MDEV-16944](https://jira.mariadb.org/browse/MDEV-16944) fix galera tests
* [Revision #e02077aa03](https://github.com/MariaDB/server/commit/e02077aa03)\
  2024-04-23 09:55:49 +0400
  * [MDEV-21076](https://jira.mariadb.org/browse/MDEV-21076) NOT NULL and UNIQUE constraints cause SUM() to yield an incorrect result
* [Revision #24abbb9bdb](https://github.com/MariaDB/server/commit/24abbb9bdb)\
  2024-04-22 20:22:03 +0400
  * [MDEV-21034](https://jira.mariadb.org/browse/MDEV-21034) GREATEST() and LEAST() malfunction for NULL
* [Revision #361b790392](https://github.com/MariaDB/server/commit/361b790392)\
  2024-03-03 08:18:55 +0100
  * Remove unnecessary whitespace in mysqldump
* [Revision #57f6a1ca98](https://github.com/MariaDB/server/commit/57f6a1ca98)\
  2024-04-16 12:39:54 +0200
  * [MDEV-19415](https://jira.mariadb.org/browse/MDEV-19415): use-after-free on charsets\_dir from slave connect
* [Revision #0c249ad718](https://github.com/MariaDB/server/commit/0c249ad718)\
  2024-04-16 10:08:31 +0200
  * [MDEV-30232](https://jira.mariadb.org/browse/MDEV-30232): rpl.rpl\_gtid\_crash fails sporadically in BB
* [Revision #4a2e03453a](https://github.com/MariaDB/server/commit/4a2e03453a)\
  2024-04-19 22:09:06 +0200
  * [MDEV-33952](https://jira.mariadb.org/browse/MDEV-33952) galera\_create\_table\_as\_select fails sporadically
* [Revision #7432a487b1](https://github.com/MariaDB/server/commit/7432a487b1)\
  2024-03-19 19:16:46 +0000
  * Update tests to be compatible with OpenSSL 3.2.0
* [Revision #4c34339426](https://github.com/MariaDB/server/commit/4c34339426)\
  2024-04-19 15:46:21 +0300
  * [MDEV-33946](https://jira.mariadb.org/browse/MDEV-33946): OPT\_PAGE\_CHECKSUM mismatch due to mtr\_t::memmove()
* [Revision #2e84560dc4](https://github.com/MariaDB/server/commit/2e84560dc4)\
  2024-04-18 09:32:33 +0200
  * [MDEV-16944](https://jira.mariadb.org/browse/MDEV-16944) postfix. Fix a typo
* [Revision #5928e04d5f](https://github.com/MariaDB/server/commit/5928e04d5f)\
  2024-04-16 12:25:48 +0530
  * [MDEV-32489](https://jira.mariadb.org/browse/MDEV-32489) Change buffer index fails to delete the records
* [Revision #0ad52e4d6a](https://github.com/MariaDB/server/commit/0ad52e4d6a)\
  2024-04-10 12:00:02 -0600
  * [MDEV-27512](https://jira.mariadb.org/browse/MDEV-27512): Assertion !thd->transaction\_rollback\_request failed in rows\_event\_stmt\_cleanup
* [Revision #061adae9a2](https://github.com/MariaDB/server/commit/061adae9a2)\
  2024-04-15 15:46:50 +0200
  * [MDEV-16944](https://jira.mariadb.org/browse/MDEV-16944) Fix file sharing issues on Windows in mysqltest
* [Revision #b48de9737b](https://github.com/MariaDB/server/commit/b48de9737b)\
  2024-04-17 16:07:15 +0200
  * Remove duplicate key "Language" from .clang-format
* [Revision #173847b76a](https://github.com/MariaDB/server/commit/173847b76a)\
  2024-04-17 15:56:45 +0200
  * Do not run maria\_recover\_encrypted with embedded.
* [Revision #e87a175b3a](https://github.com/MariaDB/server/commit/e87a175b3a)\
  2024-04-10 12:37:06 +0200
  * Fix LTO (aka interprocedural optimization) build with MSVC
* [Revision #040069f4ba](https://github.com/MariaDB/server/commit/040069f4ba)\
  2024-04-17 15:16:50 +0530
  * [MDEV-33431](https://jira.mariadb.org/browse/MDEV-33431) Latching order violation reported fil\_system.sys\_space.latch and ibuf\_pessimistic\_insert\_mutex
* [Revision #f6e9600f42](https://github.com/MariaDB/server/commit/f6e9600f42)\
  2024-04-17 10:48:24 +0200
  * [MDEV-33840](https://jira.mariadb.org/browse/MDEV-33840) tpool- switch to longer maintainence timer interval, if pool is idle
* [Revision #2ba79aba2b](https://github.com/MariaDB/server/commit/2ba79aba2b)\
  2024-04-17 09:58:34 +0200
  * Revert "[MDEV-33840](https://jira.mariadb.org/browse/MDEV-33840) tpool : switch off maintenance timer when not needed."
* Merge [Revision #3a3fe3005d](https://github.com/MariaDB/server/commit/3a3fe3005d) 2024-04-17 10:10:26 +0300 - Merge 10.4 into 10.5
* [Revision #9164c2b8bb](https://github.com/MariaDB/server/commit/9164c2b8bb)\
  2024-04-17 10:10:23 +0300
  * Tests: remove a duplicated check
* [Revision #41e7ceb0ac](https://github.com/MariaDB/server/commit/41e7ceb0ac)\
  2024-04-15 22:54:20 +0200
  * [MDEV-33889](https://jira.mariadb.org/browse/MDEV-33889) Read only server throws error when running a create temporary table as select statement
* Merge [Revision #9b18275623](https://github.com/MariaDB/server/commit/9b18275623) 2024-04-16 11:04:14 +0200 - Merge branch '10.4' into 10.5
* [Revision #ce104d4171](https://github.com/MariaDB/server/commit/ce104d4171)\
  2024-04-15 18:54:30 +0200
  * Fix windows build failure
* Merge [Revision #16aa4b5f59](https://github.com/MariaDB/server/commit/16aa4b5f59) 2024-04-15 17:46:24 +0200 - Merge from 10.4 to 10.5
* [Revision #10272f3709](https://github.com/MariaDB/server/commit/10272f3709)\
  2024-04-15 10:23:22 +0200
  * Distinguish "manager stopped" from "manager not started"
* [Revision #a032f14b34](https://github.com/MariaDB/server/commit/a032f14b34)\
  2024-04-15 09:04:11 +0300
  * [MDEV-33559](https://jira.mariadb.org/browse/MDEV-33559) matched\_rec::block should be allocated from the buffer pool
* [Revision #ea810b04cb](https://github.com/MariaDB/server/commit/ea810b04cb)\
  2024-03-06 15:59:30 +1100
  * [MDEV-30676](https://jira.mariadb.org/browse/MDEV-30676) rpl.parallel\_backup\* tests sometimes fail
* [Revision #8bc3241016](https://github.com/MariaDB/server/commit/8bc3241016)\
  2024-04-13 16:27:08 +0200
  * feedback plugin: abort sending the report on server shutdown
* [Revision #6a4ac4c72d](https://github.com/MariaDB/server/commit/6a4ac4c72d)\
  2024-04-13 14:36:15 +0200
  * Fixed random failure in main.kill\_processlist-6619 (take 3)
* [Revision #69b5fdf32a](https://github.com/MariaDB/server/commit/69b5fdf32a)\
  2024-04-11 16:19:13 +0200
  * galera/suite.pm: perl warning
* [Revision #79706fd386](https://github.com/MariaDB/server/commit/79706fd386)\
  2024-03-08 23:53:24 +0000
  * Minor improvements to options error handling
* [Revision #47d75cdd80](https://github.com/MariaDB/server/commit/47d75cdd80)\
  2024-02-25 02:03:44 +0000
  * [MDEV-33469](https://jira.mariadb.org/browse/MDEV-33469) Fix behavior on invalid arguments
* [Revision #dd639985c1](https://github.com/MariaDB/server/commit/dd639985c1)\
  2024-03-08 22:56:14 +0000
  * Simplify MTR for handling multiple invalid options
* [Revision #a6aecbb036](https://github.com/MariaDB/server/commit/a6aecbb036)\
  2024-04-11 09:48:07 -0600
  * [MDEV-10684](https://jira.mariadb.org/browse/MDEV-10684): rpl.rpl\_domain\_id\_filter\_restart fails in buildbot
* [Revision #04be12a8f5](https://github.com/MariaDB/server/commit/04be12a8f5)\
  2024-04-11 15:51:30 +0300
  * Fix g++-14 -Wtemplate-id-cdtor
* [Revision #f131c60938](https://github.com/MariaDB/server/commit/f131c60938)\
  2024-04-09 17:20:18 -0700
  * Link beginner instructions in README.md
* [Revision #8785b79763](https://github.com/MariaDB/server/commit/8785b79763)\
  2024-04-08 23:11:14 +0200
  * Update README.md
* [Revision #37fd497c7b](https://github.com/MariaDB/server/commit/37fd497c7b)\
  2024-04-10 17:58:36 +0400
  * [MDEV-32458](https://jira.mariadb.org/browse/MDEV-32458) ASAN unknown-crash in Inet6::ascii\_to\_fbt when casting character string to inet6
* [Revision #2d2172a5cf](https://github.com/MariaDB/server/commit/2d2172a5cf)\
  2024-04-10 19:34:15 +0200
  * sporadic failures of rpl.rpl\_semi\_sync\_master\_shutdown
* [Revision #0da1653f1b](https://github.com/MariaDB/server/commit/0da1653f1b)\
  2024-04-10 18:19:43 +0300
  * [MDEV-31779](https://jira.mariadb.org/browse/MDEV-31779) Server crash in Rows\_log\_event::update\_sequence upon replaying binary log
* [Revision #b697dce8ca](https://github.com/MariaDB/server/commit/b697dce8ca)\
  2024-04-10 11:12:47 +0400
  * [MDEV-29149](https://jira.mariadb.org/browse/MDEV-29149) Assertion \`!is\_valid\_datetime() || fraction\_remainder(((item->decimals) < (6) ? (item->decimals) : (6))) == 0' failed in Datetime\_truncation\_not\_needed::Datetime\_truncation\_not\_needed
* [Revision #0304dbc327](https://github.com/MariaDB/server/commit/0304dbc327)\
  2023-11-01 11:07:16 +0200
  * [MDEV-25089](https://jira.mariadb.org/browse/MDEV-25089) : Assertion \`error.len > 0' failed in galera::ReplicatorSMM::handle\_apply\_error()
* [Revision #9fb8881ef8](https://github.com/MariaDB/server/commit/9fb8881ef8)\
  2024-04-09 17:37:08 +0400
  * [MDEV-28366](https://jira.mariadb.org/browse/MDEV-28366) GLOBAL debug\_dbug setting affected by collation\_connection=utf16...
* [Revision #952ab9a596](https://github.com/MariaDB/server/commit/952ab9a596)\
  2024-04-08 13:04:59 -0600
  * [MDEV-30260](https://jira.mariadb.org/browse/MDEV-30260): Slave crashed:reload\_acl\_and\_cache during shutdown
* [Revision #4980fcb990](https://github.com/MariaDB/server/commit/4980fcb990)\
  2024-04-09 13:07:23 +0200
  * [MDEV-33867](https://jira.mariadb.org/browse/MDEV-33867) main.query\_cache\_debug fails with heap-use-after-free
* [Revision #d4936c8b26](https://github.com/MariaDB/server/commit/d4936c8b26)\
  2024-04-09 14:18:29 +0400
  * [MDEV-18898](https://jira.mariadb.org/browse/MDEV-18898) SELECT using wrong index when using operator IN with mixed types
* [Revision #7aa86eb1e1](https://github.com/MariaDB/server/commit/7aa86eb1e1)\
  2024-04-04 14:30:59 +0300
  * [MDEV-33828](https://jira.mariadb.org/browse/MDEV-33828) : Transactional commit not supported by involved engine(s)
* [Revision #3003a3dab0](https://github.com/MariaDB/server/commit/3003a3dab0)\
  2024-04-05 11:22:28 +0200
  * galera: wsrep-lib submodule update
* [Revision #6606abb6a4](https://github.com/MariaDB/server/commit/6606abb6a4)\
  2024-04-09 13:25:55 +0400
  * [MDEV-18319](https://jira.mariadb.org/browse/MDEV-18319) BIGINT UNSIGNED Performance issue
* [Revision #09bae92c16](https://github.com/MariaDB/server/commit/09bae92c16)\
  2024-04-08 16:34:38 +0200
  * [MDEV-33840](https://jira.mariadb.org/browse/MDEV-33840) tpool : switch off maintenance timer when not needed.
* [Revision #b7b58a2310](https://github.com/MariaDB/server/commit/b7b58a2310)\
  2024-04-08 16:24:46 +1000
  * [MDEV-33731](https://jira.mariadb.org/browse/MDEV-33731) Only iterate over m\_locked\_partitions in update\_next\_auto\_inc\_val()
* [Revision #7e3090a8a0](https://github.com/MariaDB/server/commit/7e3090a8a0)\
  2024-04-08 20:52:14 +0200
  * fix perfschema.misc when previous tests used lots of threads
* [Revision #50803bc456](https://github.com/MariaDB/server/commit/50803bc456)\
  2024-04-08 18:43:24 +0200
  * [MDEV-25614](https://jira.mariadb.org/browse/MDEV-25614) disable failing galera test
* [Revision #d32b6f69b3](https://github.com/MariaDB/server/commit/d32b6f69b3)\
  2024-04-08 17:22:06 +0200
  * update C/C
* [Revision #3c40f8bafb](https://github.com/MariaDB/server/commit/3c40f8bafb)\
  2024-04-05 18:08:53 +0530
  * [MDEV-31402](https://jira.mariadb.org/browse/MDEV-31402): SIGSEGV in json\_get\_path\_next | Item\_func\_json\_extract::read\_json
* [Revision #e1825e39ca](https://github.com/MariaDB/server/commit/e1825e39ca)\
  2024-04-07 22:29:51 +0200
  * increase performance-schema-max-thread-instances
* [Revision #54ad3b0e9e](https://github.com/MariaDB/server/commit/54ad3b0e9e)\
  2024-04-07 12:01:24 +0200
  * [MDEV-22949](https://jira.mariadb.org/browse/MDEV-22949) perfschema.memory\_aggregate\_no\_a\_no\_u fails sporadically in buildbot with wrong result
* [Revision #a7bf0a42d0](https://github.com/MariaDB/server/commit/a7bf0a42d0)\
  2024-04-06 23:05:57 +0200
  * sporadic failures of main.mdl\_sync
* [Revision #12d448fde9](https://github.com/MariaDB/server/commit/12d448fde9)\
  2024-04-06 00:31:08 +0200
  * mtr: increase more timeouts under debuggers
* [Revision #429fdb5bd6](https://github.com/MariaDB/server/commit/429fdb5bd6)\
  2024-04-05 15:47:03 +0200
  * [MDEV-29171](https://jira.mariadb.org/browse/MDEV-29171) disable failing galera test
* [Revision #96533bae54](https://github.com/MariaDB/server/commit/96533bae54)\
  2024-04-05 10:41:01 +0200
  * suppress a transient galera warning
* [Revision #b3e29da540](https://github.com/MariaDB/server/commit/b3e29da540)\
  2024-04-04 18:23:52 +0200
  * [MDEV-33290](https://jira.mariadb.org/browse/MDEV-33290): Disable ColumnStore based on boost version (post-postfix)
* [Revision #075dd73641](https://github.com/MariaDB/server/commit/075dd73641)\
  2024-03-28 13:10:12 +1100
  * [MDEV-33290](https://jira.mariadb.org/browse/MDEV-33290): Disable ColumnStore based on boost version (postfix)
* [Revision #cb41757f02](https://github.com/MariaDB/server/commit/cb41757f02)\
  2024-03-29 08:39:42 +0100
  * cleanup: perfschema.threads\_history
* [Revision #190280205b](https://github.com/MariaDB/server/commit/190280205b)\
  2024-03-28 21:31:24 +0100
  * perfschema is disabled until it's enabled
* [Revision #53af3d8c25](https://github.com/MariaDB/server/commit/53af3d8c25)\
  2024-02-29 16:51:17 +0200
  * Fixed memory leaks in embedded server and mysqltest
* [Revision #fc6711c636](https://github.com/MariaDB/server/commit/fc6711c636)\
  2024-03-27 22:30:29 +0100
  * mtr: increase timeouts under ASAN/UBSAN/MSAN
* [Revision #bd0e751549](https://github.com/MariaDB/server/commit/bd0e751549)\
  2024-03-27 20:45:36 +0100
  * rpl.rpl\_domain\_id\_filter\_master\_crash failed on msan builder
* [Revision #b067df3213](https://github.com/MariaDB/server/commit/b067df3213)\
  2024-03-28 16:09:15 +0100
  * innodb.innodb\_defrag\_stats wait for the correct value
* [Revision #a58a570c07](https://github.com/MariaDB/server/commit/a58a570c07)\
  2024-03-27 17:17:53 +0100
  * innodb.monitor test: wait for the correct value
* [Revision #faf686db9e](https://github.com/MariaDB/server/commit/faf686db9e)\
  2024-03-28 18:23:11 +0100
  * [MDEV-22955](https://jira.mariadb.org/browse/MDEV-22955) innodb.innodb-alter fails in buildbot with extra warning
* [Revision #2fcf2ec229](https://github.com/MariaDB/server/commit/2fcf2ec229)\
  2024-04-04 17:12:09 +0300
  * [MDEV-33749](https://jira.mariadb.org/browse/MDEV-33749) hyphen in table name can cause galera certification failures
* [Revision #4987b5e3b1](https://github.com/MariaDB/server/commit/4987b5e3b1)\
  2024-04-02 00:07:12 -0500
  * [MDEV-33803](https://jira.mariadb.org/browse/MDEV-33803) Error 4162 "Operator does not exists" is incorrectly-worded
* [Revision #29bb321f04](https://github.com/MariaDB/server/commit/29bb321f04)\
  2024-03-28 14:01:43 +0400
  * [MDEV-33788](https://jira.mariadb.org/browse/MDEV-33788) HEX(COLUMN\_CREATE(.. AS CHAR ...)) fails with --view-protocol
* [Revision #e1876e7f78](https://github.com/MariaDB/server/commit/e1876e7f78)\
  2024-03-27 20:44:05 +0700
  * [MDEV-33768](https://jira.mariadb.org/browse/MDEV-33768): Memory leak found in the test main.constraints run with --ps-protocol against a server built with the option -DWITH\_PROTECT\_STATEMENT\_MEMROOT
* [Revision #f44e41db38](https://github.com/MariaDB/server/commit/f44e41db38)\
  2024-03-27 22:55:15 +0700
  * [MDEV-33767](https://jira.mariadb.org/browse/MDEV-33767): Memory leaks found in some tests run with --ps-protocol against a server built with the option -DWITH\_PROTECT\_STATEMENT\_MEMROOT
* [Revision #9f1019ba3d](https://github.com/MariaDB/server/commit/9f1019ba3d)\
  2024-03-28 13:53:52 +1100
  * [MDEV-33044](https://jira.mariadb.org/browse/MDEV-33044) Loading time zones does not work with alter\_algorithm INPLACE (postfix)
* [Revision #7890388d91](https://github.com/MariaDB/server/commit/7890388d91)\
  2024-03-18 20:45:45 +0000
  * [MDEV-33044](https://jira.mariadb.org/browse/MDEV-33044) Loading time zones does not work with alter\_algorithm INPLACE
* [Revision #81f75ca83a](https://github.com/MariaDB/server/commit/81f75ca83a)\
  2024-03-27 15:21:49 +0100
  * Fixed random failure in main.kill\_processlist-6619
* [Revision #3226787bba](https://github.com/MariaDB/server/commit/3226787bba)\
  2024-03-27 15:14:31 +0100
  * Revert "Fixed random failure in main.kill\_processlist-6619"
* [Revision #58c7f63176](https://github.com/MariaDB/server/commit/58c7f63176)\
  2024-03-27 15:01:28 +0100
  * mysqltest: better error reporting when "shutdown" fails
* [Revision #721a6a5e6b](https://github.com/MariaDB/server/commit/721a6a5e6b)\
  2024-03-27 11:38:36 +0100
  * plugins.test\_sql\_service --valgrind
* [Revision #f50694c52b](https://github.com/MariaDB/server/commit/f50694c52b)\
  2024-03-27 09:53:56 +0100
  * remove pointless test
* [Revision #dc681953cf](https://github.com/MariaDB/server/commit/dc681953cf)\
  2024-03-27 09:51:28 +0100
  * events in perfschema tests: use ON COMPLETION NOT PRESERVE
* [Revision #49f2e9f700](https://github.com/MariaDB/server/commit/49f2e9f700)\
  2024-03-27 00:05:00 +0100
  * update bison version dependency
* [Revision #8bb8820df2](https://github.com/MariaDB/server/commit/8bb8820df2)\
  2024-03-26 20:59:42 +0100
  * [MDEV-22949](https://jira.mariadb.org/browse/MDEV-22949) perfschema.memory\_aggregate\_no\_a\_no\_u fails sporadically in buildbot with wrong result
* [Revision #89fd381be8](https://github.com/MariaDB/server/commit/89fd381be8)\
  2024-03-25 19:34:41 +0100
  * [MDEV-25252](https://jira.mariadb.org/browse/MDEV-25252) main.type\_float fails in new buildbot
* [Revision #353f904ea9](https://github.com/MariaDB/server/commit/353f904ea9)\
  2024-03-25 14:44:31 +0100
  * [MDEV-31379](https://jira.mariadb.org/browse/MDEV-31379) Undefined behavior in the reference Ed25519 implementation
* [Revision #c84d67a302](https://github.com/MariaDB/server/commit/c84d67a302)\
  2024-03-25 12:20:16 +0100
  * reenable main.mysqldump-system test
* [Revision #c77680768c](https://github.com/MariaDB/server/commit/c77680768c)\
  2024-03-27 14:20:12 +0100
  * [MDEV-33460](https://jira.mariadb.org/browse/MDEV-33460) use the correct sql\_mode and fix for --view
* [Revision #0fc123c595](https://github.com/MariaDB/server/commit/0fc123c595)\
  2024-03-27 15:22:58 +0400
  * [MDEV-33772](https://jira.mariadb.org/browse/MDEV-33772) Bad SEPARATOR value in GROUP\_CONCAT on character set conversion
* [Revision #58df20974b](https://github.com/MariaDB/server/commit/58df20974b)\
  2024-03-13 16:56:37 -0400
  * [MDEV-33460](https://jira.mariadb.org/browse/MDEV-33460) select '123' 'x'; unexpected result
* [Revision #76a27155b4](https://github.com/MariaDB/server/commit/76a27155b4)\
  2024-03-20 18:25:21 +1100
  * [MDEV-33301](https://jira.mariadb.org/browse/MDEV-33301) memlock with systemd still not working
* [Revision #ee2ed1a036](https://github.com/MariaDB/server/commit/ee2ed1a036)\
  2024-03-20 16:30:11 +1100
  * Revert "[MDEV-33636](https://jira.mariadb.org/browse/MDEV-33636): RPM caps is on mariadbd exe"
* [Revision #987a266d77](https://github.com/MariaDB/server/commit/987a266d77)\
  2024-03-25 12:13:57 +0100
  * galera: wsrep-lib submodule update
* [Revision #e9d334434d](https://github.com/MariaDB/server/commit/e9d334434d)\
  2024-02-15 09:40:50 +0200
  * [MDEV-32787](https://jira.mariadb.org/browse/MDEV-32787) : Assertion \`!wsrep\_has\_changes(thd) || (thd->lex->sql\_command == SQLCOM\_CREATE\_TABLE && !thd->is\_current\_stmt\_binlog\_format\_row()) || thd->wsrep\_cs().transaction().state() == wsrep::transaction::s\_aborted' failed in void wsrep\_commit\_empty(THD\*, bool)
* [Revision #70b907724e](https://github.com/MariaDB/server/commit/70b907724e)\
  2024-03-22 15:07:31 +0200
  * [MDEV-32364](https://jira.mariadb.org/browse/MDEV-32364) fixup: crash in ut\_dontdump()
* [Revision #f0590db5c5](https://github.com/MariaDB/server/commit/f0590db5c5)\
  2024-03-22 14:57:00 +0200
  * [MDEV-33591](https://jira.mariadb.org/browse/MDEV-33591) MONITOR\_INC\_VALUE\_CUMULATIVE is executed regardless of "if" condition
* [Revision #7d36919f4b](https://github.com/MariaDB/server/commit/7d36919f4b)\
  2024-02-22 20:57:00 +0100
  * [MDEV-33723](https://jira.mariadb.org/browse/MDEV-33723) Mroonga ignored WITHOUT\_DYNAMIC\_PLUGINS
* [Revision #a13e521bc5](https://github.com/MariaDB/server/commit/a13e521bc5)\
  2024-03-18 17:37:13 +1100
  * [MDEV-33636](https://jira.mariadb.org/browse/MDEV-33636): RPM caps is on mariadbd exe
* [Revision #4592af2e84](https://github.com/MariaDB/server/commit/4592af2e84)\
  2024-03-18 16:01:58 +0200
  * Work around missing MSAN instrumentation
* [Revision #09d991d01c](https://github.com/MariaDB/server/commit/09d991d01c)\
  2024-03-18 16:01:29 +0200
  * [MDEV-33478](https://jira.mariadb.org/browse/MDEV-33478): Tests massively fail with clang-18 -fsanitize=memory
* [Revision #fb774eb1eb](https://github.com/MariaDB/server/commit/fb774eb1eb)\
  2024-03-15 14:54:36 +0100
  * Fix occasional test failure of rpl.rpl\_parallel\_stop\_slave
* [Revision #7f498fbab8](https://github.com/MariaDB/server/commit/7f498fbab8)\
  2024-03-15 00:41:28 +0100
  * Fix "Assertion \`THR\_PFS\_initialized' failed" in main.bootstrap
* [Revision #51e3f1daf5](https://github.com/MariaDB/server/commit/51e3f1daf5)\
  2024-03-14 15:31:46 +0100
  * cmake: append to the array correctly
* [Revision #9d5a8bd663](https://github.com/MariaDB/server/commit/9d5a8bd663)\
  2024-03-13 16:05:42 +0300
  * [MDEV-33665](https://jira.mariadb.org/browse/MDEV-33665): MSAN failure due to uninitialized Item\_func::not\_null\_tables\_cache
* [Revision #49cf702ee5](https://github.com/MariaDB/server/commit/49cf702ee5)\
  2024-03-14 10:53:49 +0100
  * build failure with cmake < 3.10
* [Revision #7eb6d5aa21](https://github.com/MariaDB/server/commit/7eb6d5aa21)\
  2024-03-14 09:15:53 +0100
  * update s3.partition result after 57ffcd686ffa
* [Revision #967a148966](https://github.com/MariaDB/server/commit/967a148966)\
  2024-03-13 14:41:24 +0530
  * [MDEV-33635](https://jira.mariadb.org/browse/MDEV-33635) innodb.innodb-64k-crash - Found warnings/errors in server log file
* Merge [Revision #4cda50afbd](https://github.com/MariaDB/server/commit/4cda50afbd) 2024-03-13 15:13:48 +0100 - Merge branch '10.4' into 10.5
* [Revision #62a9a54a94](https://github.com/MariaDB/server/commit/62a9a54a94)\
  2024-02-01 13:23:26 +0100
  * [MDEV-33344](https://jira.mariadb.org/browse/MDEV-33344) REGEXP empty string inconsistent
* [Revision #7828aadd3a](https://github.com/MariaDB/server/commit/7828aadd3a)\
  2024-01-26 21:50:51 +0100
  * [MDEV-33318](https://jira.mariadb.org/browse/MDEV-33318) ORDER BY COLLATE improperly applied to non-character columns
* [Revision #67abdb9f33](https://github.com/MariaDB/server/commit/67abdb9f33)\
  2024-03-11 15:59:56 +0530
  * [MDEV-33593](https://jira.mariadb.org/browse/MDEV-33593) Auto increment deadlock error causes ASSERT in subsequent save point
* Merge [Revision #f703e72bd8](https://github.com/MariaDB/server/commit/f703e72bd8) 2024-03-11 10:08:20 +0200 - Merge 10.4 into 10.5
* [Revision #afe9632913](https://github.com/MariaDB/server/commit/afe9632913)\
  2024-03-05 12:07:48 +0530
  * [MDEV-33593](https://jira.mariadb.org/browse/MDEV-33593) Auto increment deadlock error causes ASSERT in subsequent save point
* [Revision #6e5333fc8c](https://github.com/MariaDB/server/commit/6e5333fc8c)\
  2024-03-04 18:50:12 +0530
  * [MDEV-32445](https://jira.mariadb.org/browse/MDEV-32445) InnoDB may corrupt its log before upgrading it on startup
* [Revision #1b568fb917](https://github.com/MariaDB/server/commit/1b568fb917)\
  2024-02-26 15:00:54 +1100
  * [MDEV-33539](https://jira.mariadb.org/browse/MDEV-33539) spider: remove some unused code in self reference checks
* [Revision #d37c51b805](https://github.com/MariaDB/server/commit/d37c51b805)\
  2024-02-20 11:20:21 +1100
  * [MDEV-33494](https://jira.mariadb.org/browse/MDEV-33494) fix spider init with no\_zero\_date global sql mode
* [Revision #8b3f470c0b](https://github.com/MariaDB/server/commit/8b3f470c0b)\
  2024-03-01 11:21:50 +0200
  * Fixed random failure in main.kill\_processlist-6619
* [Revision #32546877cd](https://github.com/MariaDB/server/commit/32546877cd)\
  2023-12-12 05:21:10 +0000
  * [MDEV-26923](https://jira.mariadb.org/browse/MDEV-26923) Check all invalid config options
* [Revision #969669767b](https://github.com/MariaDB/server/commit/969669767b)\
  2024-02-27 17:59:20 +0530
  * [MDEV-33011](https://jira.mariadb.org/browse/MDEV-33011) mariadb-backup --backup: FATAL ERROR: ... Can't open datafile cool\_down/t3
* [Revision #8778a83eee](https://github.com/MariaDB/server/commit/8778a83eee)\
  2024-02-22 22:58:52 -0800
  * [MDEV-31276](https://jira.mariadb.org/browse/MDEV-31276) Wrong warnings on 2-nd execution of PS for query with GROUP\_CONCAT
* [Revision #e63311c2cf](https://github.com/MariaDB/server/commit/e63311c2cf)\
  2024-02-21 11:41:50 +0400
  * [MDEV-33496](https://jira.mariadb.org/browse/MDEV-33496) Out of range error in AVG(YEAR(datetime)) due to a wrong data type
* [Revision #d57c44f626](https://github.com/MariaDB/server/commit/d57c44f626)\
  2024-02-20 22:05:00 -0800
  * [MDEV-31277](https://jira.mariadb.org/browse/MDEV-31277) Wrong result on 2-nd execution of PS to select from view using derived
* [Revision #0f0da95db0](https://github.com/MariaDB/server/commit/0f0da95db0)\
  2024-02-21 14:17:34 +1100
  * [MDEV-33493](https://jira.mariadb.org/browse/MDEV-33493) Spider: Make a symlink result file a normal file
* [Revision #b04c857596](https://github.com/MariaDB/server/commit/b04c857596)\
  2024-02-20 08:16:15 -0700
  * [MDEV-33500](https://jira.mariadb.org/browse/MDEV-33500): rpl.rpl\_parallel\_sbm can fail on slow machines, e.g. MSAN/Valgrind builders
* [Revision #1bbbb66e46](https://github.com/MariaDB/server/commit/1bbbb66e46)\
  2024-02-20 13:48:20 +0200
  * Disable error messages in mysql-install-db for not writable log directory
* [Revision #90bbeafb7a](https://github.com/MariaDB/server/commit/90bbeafb7a)\
  2024-02-20 13:20:12 +0200
  * Get rid of error when running mariadb-install-db with --log-bin
* [Revision #75c0f9512a](https://github.com/MariaDB/server/commit/75c0f9512a)\
  2023-11-21 19:43:52 -0600
  * fix markdown headings
* [Revision #c492c34f67](https://github.com/MariaDB/server/commit/c492c34f67)\
  2024-02-19 15:12:16 +1100
  * [MDEV-33434](https://jira.mariadb.org/browse/MDEV-33434) spider direct sql: Check length before memcpy
* [Revision #d510f80549](https://github.com/MariaDB/server/commit/d510f80549)\
  2024-02-10 00:30:47 +0100
  * [MDEV-33482](https://jira.mariadb.org/browse/MDEV-33482): Optimize WolfSSL for improved performance
* [Revision #8a1904d782](https://github.com/MariaDB/server/commit/8a1904d782)\
  2024-01-25 16:07:51 +1100
  * [MDEV-33301](https://jira.mariadb.org/browse/MDEV-33301) memlock with systemd still not working
* [Revision #0185ac64f3](https://github.com/MariaDB/server/commit/0185ac64f3)\
  2024-01-11 10:02:58 -0500
  * [MDEV-30975](https://jira.mariadb.org/browse/MDEV-30975) Wrong result with cross Join given join order
* [Revision #85517f609a](https://github.com/MariaDB/server/commit/85517f609a)\
  2024-02-11 00:05:24 +0400
  * [MDEV-33393](https://jira.mariadb.org/browse/MDEV-33393) audit plugin do not report user did the action..
* Merge [Revision #b770633e07](https://github.com/MariaDB/server/commit/b770633e07) 2024-02-13 14:25:21 +0200 - Merge 10.4 into 10.5
* [Revision #68d9deb69a](https://github.com/MariaDB/server/commit/68d9deb69a)\
  2024-02-13 14:10:44 +0200
  * [MDEV-33332](https://jira.mariadb.org/browse/MDEV-33332) SIGSEGV in buf\_read\_ahead\_linear() when bpage is in buf\_pool.watch
* [Revision #d86deee34b](https://github.com/MariaDB/server/commit/d86deee34b)\
  2024-02-13 14:10:39 +0200
  * Fix GCC 14 -Wcalloc-transposed-args
* [Revision #d64ade302e](https://github.com/MariaDB/server/commit/d64ade302e)\
  2023-10-07 21:17:09 -0700
  * Properly introduce wsrep\_sst\_backup script in project packaging
* [Revision #cae18632ae](https://github.com/MariaDB/server/commit/cae18632ae)\
  2024-01-07 10:19:54 +0100
  * [MDEV-33439](https://jira.mariadb.org/browse/MDEV-33439) Fix build with libxml2 2.12
* [Revision #3281b6b8a3](https://github.com/MariaDB/server/commit/3281b6b8a3)\
  2023-11-21 11:50:55 -0800
  * [MDEV-24507](https://jira.mariadb.org/browse/MDEV-24507): Server Crash using UDF in WHERE clause of VIEW
* [Revision #b909b525f4](https://github.com/MariaDB/server/commit/b909b525f4)\
  2023-12-20 23:29:57 -0500
  * Fix a case of `unused-but-set-variable`
* [Revision #44f5fa2db9](https://github.com/MariaDB/server/commit/44f5fa2db9)\
  2023-12-30 16:30:22 -0500
  * Fix timeout(1) usage in wsrep\_sst\_mariadb-backup on \*BSD
* [Revision #81f3e97bc8](https://github.com/MariaDB/server/commit/81f3e97bc8)\
  2024-02-12 17:01:45 +0200
  * [MDEV-33383](https://jira.mariadb.org/browse/MDEV-33383): Corrupted red-black tree due to incorrect comparison
* [Revision #92f87f2cf0](https://github.com/MariaDB/server/commit/92f87f2cf0)\
  2024-02-12 17:01:35 +0200
  * Cleanup: Remove changed\_pages\_bitmap
* [Revision #47122a6112](https://github.com/MariaDB/server/commit/47122a6112)\
  2024-02-12 17:01:17 +0200
  * [MDEV-33383](https://jira.mariadb.org/browse/MDEV-33383): Replace fts\_doc\_id\_cmp, ib\_vector\_sort
* [Revision #03d1346e7f](https://github.com/MariaDB/server/commit/03d1346e7f)\
  2024-01-09 13:47:02 -0700
  * [MDEV-29369](https://jira.mariadb.org/browse/MDEV-29369): rpl.rpl\_semi\_sync\_shutdown\_await\_ack fails regularly with Result content mismatch
* [Revision #ee89558312](https://github.com/MariaDB/server/commit/ee89558312)\
  2024-02-08 09:55:02 -0700
  * [MDEV-14357](https://jira.mariadb.org/browse/MDEV-14357): rpl.rpl\_domain\_id\_filter\_io\_crash failed in buildbot with wrong result
* Merge [Revision #8ec12e0d6d](https://github.com/MariaDB/server/commit/8ec12e0d6d) 2024-02-12 11:38:13 +0200 - Merge 10.4 into 10.5
* [Revision #c32e59ac55](https://github.com/MariaDB/server/commit/c32e59ac55)\
  2024-02-10 18:50:37 +0700
  * Fix clang++ errors on missing 'override' specifier
* [Revision #15623c7f29](https://github.com/MariaDB/server/commit/15623c7f29)\
  2024-01-18 16:18:08 +0700
  * [MDEV-30660](https://jira.mariadb.org/browse/MDEV-30660) Aggregation functions fail to leverage uniqueness property
* [Revision #0381921e26](https://github.com/MariaDB/server/commit/0381921e26)\
  2024-02-08 10:35:45 +0200
  * [MDEV-33277](https://jira.mariadb.org/browse/MDEV-33277) In-place upgrade causes invalid AUTO\_INCREMENT values
* [Revision #915d951431](https://github.com/MariaDB/server/commit/915d951431)\
  2023-07-18 13:37:30 +1000
  * [MDEV-4827](https://jira.mariadb.org/browse/MDEV-4827) mysqldump --dump-slave=2 --master-data=2 doesn't record both
* [Revision #f7adf1292c](https://github.com/MariaDB/server/commit/f7adf1292c)\
  2024-02-06 18:20:53 +1100
  * [MDEV-4827](https://jira.mariadb.org/browse/MDEV-4827): prelude - additional gtid/no-gtid tests for mysqldump
* [Revision #5e7047067e](https://github.com/MariaDB/server/commit/5e7047067e)\
  2024-02-06 15:50:10 +0530
  * [MDEV-33274](https://jira.mariadb.org/browse/MDEV-33274) The test encryption.innodb-redo-nokeys often fails
* [Revision #6e406bb654](https://github.com/MariaDB/server/commit/6e406bb654)\
  2023-12-06 12:03:27 -0800
  * Fix inconsistent definition of PERFORMANCE\_SCHEMA.REPLICATION\_APPLIER\_STATUS.COUNT\_TRANSACTIONS\_RETRIES column
* [Revision #68c0f6d8ea](https://github.com/MariaDB/server/commit/68c0f6d8ea)\
  2024-01-26 01:33:28 +0000
  * Fix ninja build for cracklib\_password\_check
* [Revision #fb9da7f751](https://github.com/MariaDB/server/commit/fb9da7f751)\
  2024-01-23 20:43:39 +0530
  * [MDEV-33023](https://jira.mariadb.org/browse/MDEV-33023) Crash in mariadb-backup --prepare --export after --prepare
* [Revision #f5373db898](https://github.com/MariaDB/server/commit/f5373db898)\
  2024-01-25 15:57:05 +0300
  * [MDEV-33004](https://jira.mariadb.org/browse/MDEV-33004) innodb.cursor-restore-locking test fails
* [Revision #c31b1ee26a](https://github.com/MariaDB/server/commit/c31b1ee26a)\
  2024-02-06 20:21:00 +0530
  * [MDEV-33341](https://jira.mariadb.org/browse/MDEV-33341) innodb.undo\_space\_dblwr test case fails with Unknown Storage Engine InnoDB
* [Revision #d40eaf2dab](https://github.com/MariaDB/server/commit/d40eaf2dab)\
  2024-01-29 16:29:36 +1100
  * [MDEV-33174](https://jira.mariadb.org/browse/MDEV-33174) Fixing nondeterministic self-referencing test result
* [Revision #e06b159f02](https://github.com/MariaDB/server/commit/e06b159f02)\
  2024-02-07 15:43:19 +1100
  * [MDEV-33397](https://jira.mariadb.org/browse/MDEV-33397): Innodb include OS error information when failing to write to iblogfileX
* Merge [Revision #8e7314992f](https://github.com/MariaDB/server/commit/8e7314992f) 2024-02-06 18:29:14 +0100 - Merge branch '10.5' into mariadb-10.5.24
* [Revision #ec7a80db72](https://github.com/MariaDB/server/commit/ec7a80db72)\
  2024-02-06 08:21:25 -0500
  * bump the VERSION
* [Revision #66bb229e91](https://github.com/MariaDB/server/commit/66bb229e91)\
  2024-02-01 12:32:02 +0530
  * [MDEV-18288](https://jira.mariadb.org/browse/MDEV-18288) Transportable Tablespaces leave AUTO\_INCREMENT in mismatched state, causing INSERT errors in newly imported tables when .cfg is not used.
* [Revision #6fadbf8ebf](https://github.com/MariaDB/server/commit/6fadbf8ebf)\
  2024-02-02 20:33:40 -0800
  * [MDEV-31361](https://jira.mariadb.org/browse/MDEV-31361) Wrong result on 2nd execution of PS for query with derived table
* [Revision #9d0b79c5f5](https://github.com/MariaDB/server/commit/9d0b79c5f5)\
  2024-02-02 12:00:46 +0300
  * Make innodb\_ext\_key test stable: use innodb\_stable\_estimates.inc
* [Revision #5972f5c23b](https://github.com/MariaDB/server/commit/5972f5c23b)\
  2024-01-26 16:54:35 +0300
  * [MDEV-33314](https://jira.mariadb.org/browse/MDEV-33314): Crash in calculate\_cond\_selectivity\_for\_table() with many columns
* [Revision #78662ddadd](https://github.com/MariaDB/server/commit/78662ddadd)\
  2024-02-02 10:28:30 +0400
  * [MDEV-32893](https://jira.mariadb.org/browse/MDEV-32893) mariadb-backup is not considering O/S user when --user option is omitted
* [Revision #83aff675ce](https://github.com/MariaDB/server/commit/83aff675ce)\
  2024-02-01 15:20:37 +0400
  * [MDEV-33355](https://jira.mariadb.org/browse/MDEV-33355) Add a Galera-2-node-to-MariaDB replication MTR test cloning the slave with mariadb-backup
* [Revision #8fbad58731](https://github.com/MariaDB/server/commit/8fbad58731)\
  2024-01-31 14:45:11 +0400
  * [MDEV-33342](https://jira.mariadb.org/browse/MDEV-33342) Add a replication MTR test cloning the slave with mariadb-backup
* [Revision #68c1fbfc17](https://github.com/MariaDB/server/commit/68c1fbfc17)\
  2023-12-20 02:46:09 +0100
  * [MDEV-25370](https://jira.mariadb.org/browse/MDEV-25370) Update for portion changes autoincrement key in bi-temp table
* [Revision #21f18bd9d7](https://github.com/MariaDB/server/commit/21f18bd9d7)\
  2024-01-31 14:58:15 +0530
  * [MDEV-33341](https://jira.mariadb.org/browse/MDEV-33341) innodb.undo\_space\_dblwr test case fails with Unknown Storage Engine InnoDB
* [Revision #6914b7804d](https://github.com/MariaDB/server/commit/6914b7804d)\
  2023-12-04 10:01:36 +0200
  * [MDEV-32935](https://jira.mariadb.org/browse/MDEV-32935): Remove unneeded CMAKE\_SYSTEM\_PROCESSOR parameter from Debian
* [Revision #354e97cd72](https://github.com/MariaDB/server/commit/354e97cd72)\
  2024-01-26 15:07:41 +0100
  * Fix mtr for builds without perfschema.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
