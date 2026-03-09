# MariaDB 10.3.8 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.8)[Release Notes](../../old-releases/10.3/10.3.8.md)[Changelog](mariadb-1038-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 2 Jul 2018

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.8.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #eaab98f702](https://github.com/MariaDB/server/commit/eaab98f702)\
  2018-07-02 09:30:10 +0200
  * after-merge fix
* [Revision #fc6fe26dc0](https://github.com/MariaDB/server/commit/fc6fe26dc0)\
  2018-07-01 16:33:42 +0200
  * update C/C
* [Revision #f3ac221ffd](https://github.com/MariaDB/server/commit/f3ac221ffd)\
  2018-07-01 16:06:11 +0200
  * Fix deb build failure on Xenial: disable -fPIE
* [Revision #872e9a8ceb](https://github.com/MariaDB/server/commit/872e9a8ceb)\
  2018-07-01 02:51:53 +0300
  * Updated list of unstable tests for 10.3.8 release
* Merge [Revision #36e59752e7](https://github.com/MariaDB/server/commit/36e59752e7) 2018-06-30 16:39:20 +0200 - Merge branch '10.2' into 10.3
* Merge [Revision #1dd3c8f8ba](https://github.com/MariaDB/server/commit/1dd3c8f8ba) 2018-06-28 22:21:50 +0200 - Merge branch '10.1' into 10.2
* [Revision #45cabf1017](https://github.com/MariaDB/server/commit/45cabf1017)\
  2018-06-28 16:17:21 +0200
  * [MDEV-16615](https://jira.mariadb.org/browse/MDEV-16615) ASAN SEGV in handler::print\_error or server crash after error upon CREATE TABLE
* [Revision #8ca18294d5](https://github.com/MariaDB/server/commit/8ca18294d5)\
  2018-03-18 21:01:41 +0200
  * [MDEV-14014](https://jira.mariadb.org/browse/MDEV-14014) Multi-Slave Replication Fail: bogus data in log event
* [Revision #16c14d7ba0](https://github.com/MariaDB/server/commit/16c14d7ba0)\
  2018-06-21 09:43:05 +0200
  * mark ed25519 stable
* Merge [Revision #44d1cada12](https://github.com/MariaDB/server/commit/44d1cada12) 2018-06-28 14:07:51 +0200 - Merge branch '10.0' into 10.1
* [Revision #3d4beee1a9](https://github.com/MariaDB/server/commit/3d4beee1a9)\
  2018-06-28 11:59:25 +0200
  * remove double-counting
* [Revision #bf4244d1a0](https://github.com/MariaDB/server/commit/bf4244d1a0)\
  2018-06-27 17:01:09 +0400
  * [MDEV-8540](https://jira.mariadb.org/browse/MDEV-8540) - Crash on server shutdown since 10.0.16
* [Revision #be5698265a](https://github.com/MariaDB/server/commit/be5698265a)\
  2018-06-27 12:37:21 +0300
  * [MDEV-15607](https://jira.mariadb.org/browse/MDEV-15607): mysqld crashed few after node is being joined with sst
* [Revision #04677f44c7](https://github.com/MariaDB/server/commit/04677f44c7)\
  2018-06-28 17:23:05 +0100
  * Innodb : do not use errno on Windows to print os\_file\_pwrite() error.
* [Revision #78a0646fe4](https://github.com/MariaDB/server/commit/78a0646fe4)\
  2018-06-28 09:05:01 +0200
  * make plugins.processlist more robust
* [Revision #00ccff48af](https://github.com/MariaDB/server/commit/00ccff48af)\
  2018-03-18 21:01:41 +0200
  * [MDEV-14014](https://jira.mariadb.org/browse/MDEV-14014) Multi-Slave Replication Fail: bogus data in log event
* [Revision #52a25d7b67](https://github.com/MariaDB/server/commit/52a25d7b67)\
  2018-06-28 12:36:32 +0200
  * [MDEV-16473](https://jira.mariadb.org/browse/MDEV-16473) WITH statement throws 'no database selected' error
* [Revision #090febbb2d](https://github.com/MariaDB/server/commit/090febbb2d)\
  2018-06-28 00:33:44 -0700
  * This is another attempt to fix [MDEV-16473](https://jira.mariadb.org/browse/MDEV-16473).
* [Revision #377cd52064](https://github.com/MariaDB/server/commit/377cd52064)\
  2018-06-27 11:38:09 +0300
  * Pretty-print table names in some error messages
* [Revision #6d377a523c](https://github.com/MariaDB/server/commit/6d377a523c)\
  2018-06-26 10:49:23 -0700
  * Correction for the patch to fix [MDEV-16473](https://jira.mariadb.org/browse/MDEV-16473).
* Merge [Revision #31c950cca8](https://github.com/MariaDB/server/commit/31c950cca8) 2018-06-26 18:16:49 +0300 - Merge 10.1 into 10.2
* Merge [Revision #c6392d52ee](https://github.com/MariaDB/server/commit/c6392d52ee) 2018-06-26 17:34:44 +0300 - Merge 10.0 into 10.1
* Merge [Revision #cc8772f33e](https://github.com/MariaDB/server/commit/cc8772f33e) 2018-06-26 17:02:46 +0300 - [MDEV-15953](https://jira.mariadb.org/browse/MDEV-15953) Alter InnoDB Partitioned Table ignores pre-existing DATA DIRECTORY attribute
* [Revision #ff8b3c8df8](https://github.com/MariaDB/server/commit/ff8b3c8df8)\
  2018-06-23 13:49:36 +0300
  * [MDEV-15953](https://jira.mariadb.org/browse/MDEV-15953) Alter InnoDB Partitioned Table Moves Files (which were originally not in the datadir) to the datadir
* [Revision #28e1f1453f](https://github.com/MariaDB/server/commit/28e1f1453f)\
  2018-06-19 18:14:47 +0300
  * [MDEV-15242](https://jira.mariadb.org/browse/MDEV-15242) Poor RBR update performance with partitioned tables
* [Revision #364a20fe0b](https://github.com/MariaDB/server/commit/364a20fe0b)\
  2018-06-23 19:36:26 -0700
  * [MDEV-16507](https://jira.mariadb.org/browse/MDEV-16507) SIGSEGV when use\_stat\_tables = preferably and optimizer\_use\_condition\_selectivity = 4
* [Revision #0e937f30f6](https://github.com/MariaDB/server/commit/0e937f30f6)\
  2018-06-26 11:04:57 -0400
  * bump the VERSION
* Merge [Revision #1b4ac075bf](https://github.com/MariaDB/server/commit/1b4ac075bf) 2018-06-26 15:12:58 +0300 - Merge 10.1 into 10.2
* [Revision #c4eb4bcef6](https://github.com/MariaDB/server/commit/c4eb4bcef6)\
  2018-06-26 11:34:51 +0300
  * [MDEV-16515](https://jira.mariadb.org/browse/MDEV-16515) InnoDB: Failing assertion: ++retries < 10000 in file dict0dict.cc
* [Revision #7d0d934ca6](https://github.com/MariaDB/server/commit/7d0d934ca6)\
  2018-06-25 19:19:10 -0700
  * [MDEV-16473](https://jira.mariadb.org/browse/MDEV-16473) WITH statement throws 'no database selected' error
* [Revision #31e52b1632](https://github.com/MariaDB/server/commit/31e52b1632)\
  2018-03-12 14:46:00 +0100
  * Optimize charset tracking a bit.
* [Revision #517d718201](https://github.com/MariaDB/server/commit/517d718201)\
  2018-03-09 14:39:40 +0100
  * [MDEV-15477](https://jira.mariadb.org/browse/MDEV-15477): SESSION\_SYSVARS\_TRACKER does not track last\_gtid
* [Revision #73de63e898](https://github.com/MariaDB/server/commit/73de63e898)\
  2018-03-09 14:27:13 +0100
  * Session tracking info support in mysqltest (port from mysql)
* [Revision #a8e1eef899](https://github.com/MariaDB/server/commit/a8e1eef899)\
  2018-03-09 14:26:10 +0100
  * Reset connection support in mysqltest (port from mysql)
* [Revision #7c0779da7c](https://github.com/MariaDB/server/commit/7c0779da7c)\
  2018-05-08 14:14:36 +0300
  * [MDEV-16102](https://jira.mariadb.org/browse/MDEV-16102) Wrong ER\_DUP\_ENTRY upon ADD UNIQUE KEY on versioned table
* [Revision #b5184c7efb](https://github.com/MariaDB/server/commit/b5184c7efb)\
  2018-04-26 09:37:59 +0300
  * [MDEV-15947](https://jira.mariadb.org/browse/MDEV-15947) ASAN heap-use-after-free in Item\_ident::print or in my\_strcasecmp\_utf8 or unexpected ER\_BAD\_FIELD\_ERROR upon call of stored procedure reading from versioned table
* [Revision #133cfe39f1](https://github.com/MariaDB/server/commit/133cfe39f1)\
  2018-04-19 22:23:14 +0300
  * [MDEV-15645](https://jira.mariadb.org/browse/MDEV-15645) Assertion \`table->insert\_values' failed in write\_record upon REPLACE into a view with underlying versioned table
* [Revision #7d42135959](https://github.com/MariaDB/server/commit/7d42135959)\
  2018-06-13 14:24:42 +0200
  * [MDEV-16485](https://jira.mariadb.org/browse/MDEV-16485) Insert rows unable to execute correctly on slave's System-Versioned Tables
* [Revision #65f7473cf9](https://github.com/MariaDB/server/commit/65f7473cf9)\
  2018-06-17 18:08:04 +0200
  * fix for ctags
* [Revision #724a5105cb](https://github.com/MariaDB/server/commit/724a5105cb)\
  2018-06-28 16:55:42 +0400
  * [MDEV-16584](https://jira.mariadb.org/browse/MDEV-16584) SP with a cursor inside a loop wastes THD memory aggressively
* [Revision #445339feac](https://github.com/MariaDB/server/commit/445339feac)\
  2018-06-27 23:56:40 +0200
  * compat/oracle.parser failed in --ps
* [Revision #56145be295](https://github.com/MariaDB/server/commit/56145be295)\
  2018-06-27 12:53:49 +0400
  * [MDEV-16584](https://jira.mariadb.org/browse/MDEV-16584) SP with a cursor inside a loop wastes THD memory aggressively
* [Revision #1d6bc0f01f](https://github.com/MariaDB/server/commit/1d6bc0f01f)\
  2018-06-26 17:53:11 +0400
  * Removing sp\_head::is\_stored\_procedure. This code was dead after [MDEV-15991](https://jira.mariadb.org/browse/MDEV-15991)
* [Revision #fe76e68e0e](https://github.com/MariaDB/server/commit/fe76e68e0e)\
  2018-06-26 14:10:58 +0530
  * [MDEV-16365](https://jira.mariadb.org/browse/MDEV-16365) Setting a column NOT NULL fails to return error for NULL values when there is no DEFAULT
* [Revision #f5b60857f4](https://github.com/MariaDB/server/commit/f5b60857f4)\
  2018-06-25 18:57:32 +0400
  * A cleanup for 84c55a5668db582aa92dd2ccf076fbb783894b12 (that implemented cursor FOR loops earlier):
* [Revision #1ba5b38bfa](https://github.com/MariaDB/server/commit/1ba5b38bfa)\
  2018-06-25 20:49:22 +0530
  * [MDEV-16365](https://jira.mariadb.org/browse/MDEV-16365) Setting a column NOT NULL fails to return error for NULL values when there is no DEFAULT
* [Revision #1ace3b3fad](https://github.com/MariaDB/server/commit/1ace3b3fad)\
  2018-06-25 14:50:36 +0200
  * Mark embedded library as deinited.
* [Revision #69b9ed063b](https://github.com/MariaDB/server/commit/69b9ed063b)\
  2018-06-25 18:16:29 +0530
  * [MDEV-16365](https://jira.mariadb.org/browse/MDEV-16365) Setting a column NOT NULL fails to return error for NULL values when there is no DEFAULT
* [Revision #46fc864b90](https://github.com/MariaDB/server/commit/46fc864b90)\
  2018-06-23 09:47:18 +0200
  * [MDEV-16478](https://jira.mariadb.org/browse/MDEV-16478): mysql\_real\_connect() from libmariadbd.so always crash
* [Revision #88aaf590ac](https://github.com/MariaDB/server/commit/88aaf590ac)\
  2018-06-25 14:52:38 +0530
  * [MDEV-16365](https://jira.mariadb.org/browse/MDEV-16365) Setting a column NOT NULL fails to return error for NULL values when there is no DEFAULT
* [Revision #1abd877e2d](https://github.com/MariaDB/server/commit/1abd877e2d)\
  2018-06-22 11:28:02 +0400
  * [MDEV-8049](https://jira.mariadb.org/browse/MDEV-8049) name\_const() is not consistent about its signess
* [Revision #bcc2100f9d](https://github.com/MariaDB/server/commit/bcc2100f9d)\
  2018-06-21 12:54:28 +0400
  * [MDEV-16471](https://jira.mariadb.org/browse/MDEV-16471) mysqldump throws "Variable 'sql\_mode' can't be set to the value of 'NULL' (1231)"
* [Revision #9dc81f7d38](https://github.com/MariaDB/server/commit/9dc81f7d38)\
  2018-06-09 16:06:39 +0300
  * [MDEV-16330](https://jira.mariadb.org/browse/MDEV-16330) Allow instant change of WITH SYSTEM VERSIONING column attribute
* [Revision #ff09512e07](https://github.com/MariaDB/server/commit/ff09512e07)\
  2018-06-20 19:36:37 +0400
  * [MDEV-16489](https://jira.mariadb.org/browse/MDEV-16489) when lead() returns null on a datetime field, the result is treated as the literal string '\[NULL]'
* [Revision #9c53cbdd88](https://github.com/MariaDB/server/commit/9c53cbdd88)\
  2018-06-20 13:29:11 +0400
  * [MDEV-15941](https://jira.mariadb.org/browse/MDEV-15941) Explicit cursor FOR loop does not close the cursor
* Merge [Revision #b534a7b89e](https://github.com/MariaDB/server/commit/b534a7b89e) 2018-06-20 08:29:07 +0200 - Merge branch '10.3' into bb-10.3-fix\_len\_dec
* [Revision #956b296248](https://github.com/MariaDB/server/commit/956b296248)\
  2018-06-14 15:48:57 -0700
  * [MDEV-16420](https://jira.mariadb.org/browse/MDEV-16420) View stop working after upgrade from 10.1.15 to 10.3.7
* [Revision #b27ec70935](https://github.com/MariaDB/server/commit/b27ec70935)\
  2018-06-18 15:29:50 -0700
  * [MDEV-16319](https://jira.mariadb.org/browse/MDEV-16319): Test for crash introduced by b4a2baffa8 fixed by 4968049799
* Merge [Revision #083279f783](https://github.com/MariaDB/server/commit/083279f783) 2018-06-19 14:51:50 +0200 - Merge commit '6b8802e8dd5467556a024d807a1df23940b00895' into bb-10.3-fix\_len\_dec
* Merge [Revision #0121d5a790](https://github.com/MariaDB/server/commit/0121d5a790) 2018-06-18 12:40:53 +0300 - Merge 10.2 into 10.3
* [Revision #63027a5763](https://github.com/MariaDB/server/commit/63027a5763)\
  2018-06-13 16:45:11 +0200
  * .gitignore
* [Revision #f2c418079d](https://github.com/MariaDB/server/commit/f2c418079d)\
  2018-06-15 17:13:31 +0300
  * Fix a typo in get\_best\_ror\_intersect
* [Revision #f61909e19e](https://github.com/MariaDB/server/commit/f61909e19e)\
  2018-06-15 06:33:34 +0400
  * [MDEV-10182](https://jira.mariadb.org/browse/MDEV-10182) Bad value when inserting COALESCE(CURRENT\_TIMESTAMP) into a DECIMAL column
* [Revision #4787913db0](https://github.com/MariaDB/server/commit/4787913db0)\
  2018-06-13 08:25:16 +0400
  * [MDEV-16464](https://jira.mariadb.org/browse/MDEV-16464) Oracle Comp.: Sql-Error on "SELECT name, comment FROM mysql.proc"
* [Revision #b52bb6eb82](https://github.com/MariaDB/server/commit/b52bb6eb82)\
  2018-06-12 12:49:42 +0300
  * [MDEV-16469](https://jira.mariadb.org/browse/MDEV-16469) SET GLOBAL innodb\_change\_buffering has no effect
* [Revision #4461b0f9b3](https://github.com/MariaDB/server/commit/4461b0f9b3)\
  2018-06-08 14:30:04 +0100
  * [MDEV-16424](https://jira.mariadb.org/browse/MDEV-16424) replace cmake/bison.cmake with cmake's builtin FindBison module
* Merge [Revision #62d21ddac1](https://github.com/MariaDB/server/commit/62d21ddac1) 2018-06-07 15:07:00 +0300 - Merge 10.2 into 10.3
* [Revision #88a263eabb](https://github.com/MariaDB/server/commit/88a263eabb)\
  2018-06-03 20:31:10 +1000
  * [MDEV-16318](https://jira.mariadb.org/browse/MDEV-16318): mysqld\_safe - partial revert on 64094e1
* [Revision #c10bed17dd](https://github.com/MariaDB/server/commit/c10bed17dd)\
  2018-05-29 14:31:53 +1000
  * mysqld\_safe: use sh not bash
* [Revision #106f0b5798](https://github.com/MariaDB/server/commit/106f0b5798)\
  2018-06-05 10:25:39 +0400
  * [MDEV-16385](https://jira.mariadb.org/browse/MDEV-16385) ROW SP variable is allowed in unexpected context
* Merge [Revision #b50685af82](https://github.com/MariaDB/server/commit/b50685af82) 2018-06-04 16:12:00 +0300 - Merge 10.2 into 10.3
* [Revision #cac4100186](https://github.com/MariaDB/server/commit/cac4100186)\
  2018-05-29 16:49:48 +0200
  * cmake: shut up repeated NUMA status messages
* [Revision #eb76698300](https://github.com/MariaDB/server/commit/eb76698300)\
  2018-06-02 22:27:59 +0200
  * client.c: set connect attributes as late as possible
* [Revision #748ef3ec91](https://github.com/MariaDB/server/commit/748ef3ec91)\
  2018-05-16 18:11:30 +0300
  * [MDEV-15991](https://jira.mariadb.org/browse/MDEV-15991) Server crashes in setup\_on\_expr upon calling SP or function executing DML on versioned tables
* [Revision #b1efff46cd](https://github.com/MariaDB/server/commit/b1efff46cd)\
  2018-02-26 19:41:04 +0300
  * Vers cleanups
* [Revision #486682b1da](https://github.com/MariaDB/server/commit/486682b1da)\
  2018-05-22 21:57:20 +0200
  * cleanup: vers tests, remove create\_table procedure
* [Revision #898a8c3c0c](https://github.com/MariaDB/server/commit/898a8c3c0c)\
  2018-06-01 22:24:20 +0300
  * Deb: Disable PIE in debian/rules on older Debian/Ubuntu releases
* [Revision #ee5124d714](https://github.com/MariaDB/server/commit/ee5124d714)\
  2018-06-01 18:06:01 +0800
  * Make MariaDB CRC32-lib platform independence (#780)
* [Revision #db677cc6ef](https://github.com/MariaDB/server/commit/db677cc6ef)\
  2018-05-31 22:52:56 +0300
  * Follow-up to [MDEV-14168](https://jira.mariadb.org/browse/MDEV-14168): Correct INNOBASE\_DEFAULTS
* [Revision #5a61fa9882](https://github.com/MariaDB/server/commit/5a61fa9882)\
  2018-05-30 21:37:51 +0000
  * [MDEV-16345](https://jira.mariadb.org/browse/MDEV-16345) : No upgrade wizard in 10.3 in Windows packages.
* [Revision #682e7b8ff4](https://github.com/MariaDB/server/commit/682e7b8ff4)\
  2018-05-30 14:35:34 +0300
  * [MDEV-16334](https://jira.mariadb.org/browse/MDEV-16334) Incorrect ALTER TABLE for changing column option
* [Revision #c0f9771058](https://github.com/MariaDB/server/commit/c0f9771058)\
  2018-05-30 10:02:43 +0300
  * After-merge fixes
* [Revision #00677b368b](https://github.com/MariaDB/server/commit/00677b368b)\
  2018-05-29 09:50:55 +0300
  * Deb: Import default.mk instead of only the subset buildflags.mk
* [Revision #26d50036d9](https://github.com/MariaDB/server/commit/26d50036d9)\
  2018-05-29 09:23:23 +0300
  * Deb: Fix FTBFS on non-Linux architectures that don't support systemd
* [Revision #dc0a76600b](https://github.com/MariaDB/server/commit/dc0a76600b)\
  2018-04-17 21:53:02 +0300
  * Deb: Don't disable PIE in debian/rules, it's enabled anyway
* [Revision #a2499a2d46](https://github.com/MariaDB/server/commit/a2499a2d46)\
  2018-04-17 21:54:30 +0300
  * Deb: Clean away legacy rules sections which no longer have a function
* Merge [Revision #a3539bbb2a](https://github.com/MariaDB/server/commit/a3539bbb2a) 2018-05-29 17:34:49 +0300 - Merge 10.2 into 10.3
* [Revision #c98e6d4b3d](https://github.com/MariaDB/server/commit/c98e6d4b3d)\
  2018-04-17 21:31:34 +0300
  * Deb: Remove dependencies on packages that are 'essential' anyway
* [Revision #44e7ec193e](https://github.com/MariaDB/server/commit/44e7ec193e)\
  2018-04-17 21:30:36 +0300
  * Deb: Extend new package descriptions to meet Lintian minimum criteria
* [Revision #d46ebfb5b6](https://github.com/MariaDB/server/commit/d46ebfb5b6)\
  2018-04-11 22:18:51 +0300
  * Deb: Mark binary package architectures correctly
* [Revision #0a2ef601e0](https://github.com/MariaDB/server/commit/0a2ef601e0)\
  2018-04-11 22:17:46 +0300
  * Deb: Skip building RocksDB, TokuDB and using jemalloc on certain archs
* [Revision #548ec3a088](https://github.com/MariaDB/server/commit/548ec3a088)\
  2018-04-11 09:14:58 +0300
  * Deb: Update documentation and fix spelling errors
* [Revision #c902d5a4de](https://github.com/MariaDB/server/commit/c902d5a4de)\
  2018-04-10 19:38:14 +0300
  * Apply debian/patches/61\_replace\_dash\_with\_bash\_mbug675185.dpatch
* [Revision #64094e12c0](https://github.com/MariaDB/server/commit/64094e12c0)\
  2018-04-10 19:31:18 +0300
  * Apply debian/patches/38\_scriptsmysqld\_safe.shsignals.dpatch
* [Revision #58721c3e38](https://github.com/MariaDB/server/commit/58721c3e38)\
  2018-05-26 16:57:18 +0300
  * [MDEV-16286](https://jira.mariadb.org/browse/MDEV-16286) Killed CREATE SEQUENCE leaves sequence in unusable state
* [Revision #b3a2761807](https://github.com/MariaDB/server/commit/b3a2761807)\
  2018-05-26 16:26:56 +0300
  * Remove warning when using ScopedStatementReplication
* [Revision #3e03b3dc15](https://github.com/MariaDB/server/commit/3e03b3dc15)\
  2018-05-26 14:27:23 +0300
  * Extended vcol.update with checking if statement worked
* [Revision #afbea676de](https://github.com/MariaDB/server/commit/afbea676de)\
  2018-05-26 14:25:37 +0300
  * Fixed wrong usage of variable in ha\_sphinx.cc
* [Revision #aeaac6ca76](https://github.com/MariaDB/server/commit/aeaac6ca76)\
  2018-05-25 22:57:49 +0400
  * moved include from my\_global.h
* [Revision #8f888ab1d8](https://github.com/MariaDB/server/commit/8f888ab1d8)\
  2018-05-25 22:33:18 +0400
  * Cleanup log2() portability checks
* [Revision #3e63fa6eb3](https://github.com/MariaDB/server/commit/3e63fa6eb3)\
  2018-05-25 22:25:45 +0400
  * Cleanup rint() portability checks
* [Revision #7ffd7fe962](https://github.com/MariaDB/server/commit/7ffd7fe962)\
  2018-05-25 22:16:04 +0400
  * Cleanup isnan() portability checks
* [Revision #bc469a0bdf](https://github.com/MariaDB/server/commit/bc469a0bdf)\
  2018-05-25 22:09:07 +0400
  * Cleanup isinf() portability checks
* [Revision #3bbc30c73b](https://github.com/MariaDB/server/commit/3bbc30c73b)\
  2018-05-22 20:19:13 +0300
  * [MDEV-13727](https://jira.mariadb.org/browse/MDEV-13727) top-level query timestamp reset at stored func/trigger internal statements
* [Revision #83ec8c88c6](https://github.com/MariaDB/server/commit/83ec8c88c6)\
  2018-05-25 14:27:34 +0300
  * Make a test independent of VERSION
* [Revision #c86ea54003](https://github.com/MariaDB/server/commit/c86ea54003)\
  2018-05-24 22:13:02 -0400
  * bump the VERSION
* Merge [Revision #6f01c42fd6](https://github.com/MariaDB/server/commit/6f01c42fd6) 2018-05-24 22:36:40 +0300 - Merge 10.2 into 10.3
* [Revision #96cee524fe](https://github.com/MariaDB/server/commit/96cee524fe)\
  2018-05-22 21:57:14 +0300
  * [MDEV-15578](https://jira.mariadb.org/browse/MDEV-15578): MyRocks: support zstandard compression where the distro allows it
* [Revision #dda808e662](https://github.com/MariaDB/server/commit/dda808e662)\
  2018-05-24 14:59:25 +0530
  * fix gcc row0trunc compilation error aarch64
* Merge [Revision #0267df39a2](https://github.com/MariaDB/server/commit/0267df39a2) 2018-05-24 16:15:15 +0200 - Merge branch '10.3' into bb-10.3-release
* Merge [Revision #6686dfcbbf](https://github.com/MariaDB/server/commit/6686dfcbbf) 2018-05-24 11:27:15 +0300 - Merge 10.2 into 10.3
* [Revision #a80e410438](https://github.com/MariaDB/server/commit/a80e410438)\
  2018-05-24 08:40:52 +0300
  * Correct comments
* [Revision #54999f4e75](https://github.com/MariaDB/server/commit/54999f4e75)\
  2018-05-23 18:52:55 +0400
  * Use std::isfinite in C++ code
* [Revision #031fa6d425](https://github.com/MariaDB/server/commit/031fa6d425)\
  2018-05-21 22:30:07 +0800
  * remove check for finite/isfinite
* [Revision #c13e3c37be](https://github.com/MariaDB/server/commit/c13e3c37be)\
  2018-05-22 22:32:14 +0300
  * cleanup TABLE\_LIST
* [Revision #611488e3d9](https://github.com/MariaDB/server/commit/611488e3d9)\
  2018-05-23 12:08:35 +0400
  * [MDEV-16244](https://jira.mariadb.org/browse/MDEV-16244) sql\_mode=ORACLE: Some keywords do not work in variable declarations
* [Revision #d6976a7e52](https://github.com/MariaDB/server/commit/d6976a7e52)\
  2018-05-22 16:38:02 +0300
  * [MDEV-16234](https://jira.mariadb.org/browse/MDEV-16234) CREATE TABLE .. SELECT LASTVAL breaks replication
* [Revision #14e5db6fad](https://github.com/MariaDB/server/commit/14e5db6fad)\
  2018-05-17 20:51:03 +0300
  * Print out retry count when using mysql-test-run --repeat

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
