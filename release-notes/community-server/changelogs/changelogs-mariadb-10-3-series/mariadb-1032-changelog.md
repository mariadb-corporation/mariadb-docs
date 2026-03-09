# MariaDB 10.3.2 Changelog

[Download](https://downloads.mariadb.org/mariadb/10.3.2)[Release Notes](../../old-releases/10.3/10.3.2.md)[Changelog](mariadb-1032-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 9 Oct 2017

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.2.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #2d2f857fb3](https://github.com/MariaDB/server/commit/2d2f857fb3)\
  2017-10-05 22:10:38 +0200
  * fixes for --embedded
* [Revision #e59d080ffa](https://github.com/MariaDB/server/commit/e59d080ffa)\
  2017-10-06 12:46:12 +0300
  * fix a data race in debug build (#456)
* [Revision #a4948dafcd](https://github.com/MariaDB/server/commit/a4948dafcd)\
  2017-10-06 07:00:05 +0300
  * [MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369) Instant ADD COLUMN for InnoDB
* [Revision #3a418242df](https://github.com/MariaDB/server/commit/3a418242df)\
  2017-10-06 00:27:40 +0300
  * fix TSAN build with Clang
* Merge [Revision #a1a4e8eec1](https://github.com/MariaDB/server/commit/a1a4e8eec1) 2017-10-05 11:48:28 +0200 - Merge branch 'bb-10.2-ext' into 10.3
* Merge [Revision #3e39771551](https://github.com/MariaDB/server/commit/3e39771551) 2017-10-04 19:50:04 +0200 - Merge branch '10.2' into bb-10.2-ext
* Merge [Revision #08c493c62a](https://github.com/MariaDB/server/commit/08c493c62a) 2017-10-04 18:36:58 +0200 - Merge branch '10.1' into 10.2
* [Revision #bcda03b4fa](https://github.com/MariaDB/server/commit/bcda03b4fa)\
  2017-10-02 13:30:48 +0530
  * [MDEV-13950](https://jira.mariadb.org/browse/MDEV-13950) mysqld\_safe could not start Galera node after upgrade ...
* [Revision #8898c1614d](https://github.com/MariaDB/server/commit/8898c1614d)\
  2017-10-04 18:32:45 +0200
  * cleanup: remove test include file, clarify the comment
* [Revision #a62ebf2590](https://github.com/MariaDB/server/commit/a62ebf2590)\
  2017-09-29 10:51:00 +0200
  * cppcheck harmless warnings
* [Revision #ebda6e958f](https://github.com/MariaDB/server/commit/ebda6e958f)\
  2017-09-28 20:28:01 +0200
  * enable MongoDB support in CONNECT
* [Revision #9584c6753e](https://github.com/MariaDB/server/commit/9584c6753e)\
  2017-10-04 10:28:20 +0200
  * [MDEV-12874](https://jira.mariadb.org/browse/MDEV-12874) UPDATE statements with the same source and target
* [Revision #ac57a30bd9](https://github.com/MariaDB/server/commit/ac57a30bd9)\
  2017-09-27 11:07:19 +0200
  * [MDEV-13675](https://jira.mariadb.org/browse/MDEV-13675) filsort\_priority\_queue
* [Revision #93fb586572](https://github.com/MariaDB/server/commit/93fb586572)\
  2017-10-04 11:59:54 +0000
  * Fix a truncations warning
* Merge [Revision #2c1067166d](https://github.com/MariaDB/server/commit/2c1067166d) 2017-10-04 08:24:06 +0300 - Merge bb-10.2-ext into 10.3
* Merge [Revision #61b2618d3a](https://github.com/MariaDB/server/commit/61b2618d3a) 2017-10-04 08:10:03 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #6ca35c1428](https://github.com/MariaDB/server/commit/6ca35c1428)\
  2017-10-04 08:07:41 +0300
  * Replace a non-ASCII character in a comment
* [Revision #8d413c32dc](https://github.com/MariaDB/server/commit/8d413c32dc)\
  2017-10-03 19:43:43 +0000
  * Fix several truncation and formatting warnings.
* [Revision #4732767981](https://github.com/MariaDB/server/commit/4732767981)\
  2017-10-03 19:42:16 +0000
  * Fix Windows warnings : fix server\_audit not to use my\_win\_open and Co functions.
* [Revision #35a4591e12](https://github.com/MariaDB/server/commit/35a4591e12)\
  2017-10-03 19:38:28 +0000
  * Update C/C
* [Revision #b716231238](https://github.com/MariaDB/server/commit/b716231238)\
  2017-10-03 20:14:18 +0300
  * [MDEV-13901](https://jira.mariadb.org/browse/MDEV-13901) Assertion \`!space->stop\_new\_ops' failed in TRUNCATE TABLE with many indexes
* [Revision #ac2db256d9](https://github.com/MariaDB/server/commit/ac2db256d9)\
  2017-10-03 21:07:27 +0200
  * [MDEV-12874](https://jira.mariadb.org/browse/MDEV-12874) UPDATE statements with the same source and target
* [Revision #1a74d12da6](https://github.com/MariaDB/server/commit/1a74d12da6)\
  2017-09-26 11:52:31 +0200
  * [MDEV-12874](https://jira.mariadb.org/browse/MDEV-12874) UPDATE statements with the same source and target
* [Revision #26ff92f7ac](https://github.com/MariaDB/server/commit/26ff92f7ac)\
  2017-09-26 10:28:00 +0200
  * [MDEV-13911](https://jira.mariadb.org/browse/MDEV-13911) Support ORDER BY and LIMIT in multi-table update
* [Revision #b6a5be9eaa](https://github.com/MariaDB/server/commit/b6a5be9eaa)\
  2017-09-26 11:05:27 +0200
  * cleanup: split multi\_update test in two
* Merge [Revision #1641879387](https://github.com/MariaDB/server/commit/1641879387) 2017-10-03 17:02:18 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #ebc2f0dad3](https://github.com/MariaDB/server/commit/ebc2f0dad3)\
  2017-10-03 16:05:24 +0300
  * Avoid using HA\_POS\_ERROR constant when passing around values of type double.
* Merge [Revision #325e071c11](https://github.com/MariaDB/server/commit/325e071c11) 2017-10-03 15:52:27 +0300 - Merge pull request #457 from smtalk/10.2
* [Revision #36ef89c999](https://github.com/MariaDB/server/commit/36ef89c999)\
  2017-10-01 15:45:51 +0200
  * wrep\_sst\_common: Setting "-c ''" for my\_print\_defaults just takes no values from config at all. $MY\_PRINT\_DEFAULTS is already set at the top of the script to have --defaults-file and --defaults-extra-file. If WSREP\_SST\_OPT\_CONF if set to "--defaults-file=/etc/my.cnf --defaults-extra-file=/etc/my.extra.cnf", then "my\_print\_defaults -c "" --defaults-file=/etc/my.cnf" succeeds, but if WSREP\_SST\_OPT\_CONF is empty - no default values are taken at all. wsrep\_sst\_xtrabackup-v2: innobackupex does not support --defaults-extra-file, so ${WSREP\_SST\_OPT\_CONF} cannot be used as an argument, it has been changed to ${WSREP\_SST\_OPT\_DEFAULT}. Removed --defaults-file= from INNOMOVE line, because WSREP\_SST\_OPT\_CONF already includes it (INNOBACKUP was fine, INNOMOVE - not).
* [Revision #770231f355](https://github.com/MariaDB/server/commit/770231f355)\
  2017-10-03 11:37:38 +0300
  * Remove dict\_disable\_redo\_if\_temporary()
* [Revision #64bfad6307](https://github.com/MariaDB/server/commit/64bfad6307)\
  2017-10-03 13:27:52 +0400
  * Fixing Item\_func\_hybrid\_field\_type::date\_op(,uint) to date\_op(,ulonglong)
* [Revision #c3a44c2701](https://github.com/MariaDB/server/commit/c3a44c2701)\
  2017-10-03 08:17:14 +0000
  * Fix compiler error on Win64 - do not truncate pointer in DBUG
* [Revision #fcf631eafb](https://github.com/MariaDB/server/commit/fcf631eafb)\
  2017-10-03 07:54:22 +0400
  * A cleanup for [MDEV-10914](https://jira.mariadb.org/browse/MDEV-10914) ROW data type for stored routine variables
* Merge [Revision #8ae8cd6348](https://github.com/MariaDB/server/commit/8ae8cd6348) 2017-10-02 22:35:13 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #387bdf07ae](https://github.com/MariaDB/server/commit/387bdf07ae)\
  2017-10-02 10:10:02 +0300
  * Remove MYSQL\_REPLACE\_TRX\_IN\_THD
* [Revision #cc3057fde7](https://github.com/MariaDB/server/commit/cc3057fde7)\
  2017-10-02 11:43:30 +0300
  * Remove dict\_table\_t::big\_rows
* [Revision #d6f857ddbc](https://github.com/MariaDB/server/commit/d6f857ddbc)\
  2017-10-02 11:27:53 +0300
  * Remove a constant parameter commit=false
* Merge [Revision #3c4cff3357](https://github.com/MariaDB/server/commit/3c4cff3357) 2017-10-02 11:12:19 +0300 - Merge 10.1 into 10.2
* Merge [Revision #ac0b5a2e79](https://github.com/MariaDB/server/commit/ac0b5a2e79) 2017-10-02 10:45:55 +0300 - Merge 10.0 into 10.1
* Merge [Revision #de4a00d4f7](https://github.com/MariaDB/server/commit/de4a00d4f7) 2017-10-02 10:42:55 +0300 - Merge 5.5 into 10.0
* [Revision #028d253dd7](https://github.com/MariaDB/server/commit/028d253dd7)\
  2017-10-02 10:22:42 +0300
  * [MDEV-13980](https://jira.mariadb.org/browse/MDEV-13980) InnoDB fails to discard record lock when discarding an index page
* [Revision #a47d16907d](https://github.com/MariaDB/server/commit/a47d16907d)\
  2017-09-19 13:08:24 +0400
  * [MDEV-13137](https://jira.mariadb.org/browse/MDEV-13137) MySQL 5.6.23 Crashes when SET GLOBAL server\_audit\_logging=OFF;
* [Revision #b8488e5cf5](https://github.com/MariaDB/server/commit/b8488e5cf5)\
  2017-09-29 14:12:38 +0300
  * [MDEV-13932](https://jira.mariadb.org/browse/MDEV-13932): fil0pagecompress.cc fails to compile with lzo 2.10
* [Revision #4d01dd79a1](https://github.com/MariaDB/server/commit/4d01dd79a1)\
  2017-09-28 12:38:51 +0300
  * [MDEV-12634](https://jira.mariadb.org/browse/MDEV-12634): Uninitialised ROW\_MERGE\_RESERVE\_SIZE bytes written to temporary file
* [Revision #4aeec7275f](https://github.com/MariaDB/server/commit/4aeec7275f)\
  2017-09-27 18:27:39 -0400
  * bump the VERSION
* [Revision #f0e9bebd27](https://github.com/MariaDB/server/commit/f0e9bebd27)\
  2017-09-26 16:43:54 +0200
  * [MDEV-13897](https://jira.mariadb.org/browse/MDEV-13897) SELECT @a := MAX(col) FROM t requires full index scan
* [Revision #5b01b88e2b](https://github.com/MariaDB/server/commit/5b01b88e2b)\
  2017-09-26 20:16:06 +0200
  * update test results on 32-bit
* [Revision #f7628ca3c2](https://github.com/MariaDB/server/commit/f7628ca3c2)\
  2017-09-27 10:22:00 +0200
  * cleanup: remove useless "inline" keywords
* [Revision #7dc1815d5c](https://github.com/MariaDB/server/commit/7dc1815d5c)\
  2017-09-26 18:36:19 +0200
  * cleanup: reduce code duplication
* [Revision #0627929f62](https://github.com/MariaDB/server/commit/0627929f62)\
  2017-09-27 10:06:44 +0530
  * [MDEV-13787](https://jira.mariadb.org/browse/MDEV-13787) Crash in persistent stats wsrep\_on (thd=0x0)
* [Revision #e3dee83768](https://github.com/MariaDB/server/commit/e3dee83768)\
  2017-09-25 13:41:20 -0400
  * bump the VERSION
* [Revision #76953c0e45](https://github.com/MariaDB/server/commit/76953c0e45)\
  2017-10-02 10:03:47 +0300
  * Remove remaining InnoDB references to the TABLESPACE keyword
* [Revision #157d130a87](https://github.com/MariaDB/server/commit/157d130a87)\
  2017-09-29 20:14:03 +0000
  * Fix some conversion warnings.
* [Revision #298c56cd6a](https://github.com/MariaDB/server/commit/298c56cd6a)\
  2017-09-29 18:15:57 +0000
  * Fix "ib::fatal::fatal': destructor never returns, potential memory leak" warning
* [Revision #a3835fad0c](https://github.com/MariaDB/server/commit/a3835fad0c)\
  2017-09-29 18:15:20 +0000
  * Correct definition of ATTRIBUTE\_NORETURN on Windows.
* [Revision #96b9c61787](https://github.com/MariaDB/server/commit/96b9c61787)\
  2017-09-29 17:29:21 +0000
  * [MDEV-13941](https://jira.mariadb.org/browse/MDEV-13941) Fix high NTFS fragmentation on 10.2
* [Revision #24d9664ad0](https://github.com/MariaDB/server/commit/24d9664ad0)\
  2017-09-29 16:44:53 +0000
  * In table cache code, fix casts from longlong to long for 'version' variables.
* [Revision #8e8a7f85a9](https://github.com/MariaDB/server/commit/8e8a7f85a9)\
  2017-09-29 17:12:14 +0000
  * Fix DBUG\_PRINT formatting in query cache.
* [Revision #7cd4a66de6](https://github.com/MariaDB/server/commit/7cd4a66de6)\
  2017-09-29 16:19:28 +0300
  * Remove unused parameters and dead code
* [Revision #358ab5d6b1](https://github.com/MariaDB/server/commit/358ab5d6b1)\
  2017-09-29 15:42:25 +0300
  * Remove remaining references to InnoDB native partitioning
* [Revision #ccf21c9962](https://github.com/MariaDB/server/commit/ccf21c9962)\
  2017-09-28 12:21:16 +0000
  * fix some conversion warnings
* [Revision #7354dc6773](https://github.com/MariaDB/server/commit/7354dc6773)\
  2017-09-28 10:38:02 +0000
  * [MDEV-13384](https://jira.mariadb.org/browse/MDEV-13384) - misc Windows warnings fixed
* [Revision #509928718d](https://github.com/MariaDB/server/commit/509928718d)\
  2017-09-28 10:36:00 +0000
  * [MDEV-13384](https://jira.mariadb.org/browse/MDEV-13384) Fix Windows warnings. thd\_alloc functions now use size\_t parameters
* [Revision #eba44874ca](https://github.com/MariaDB/server/commit/eba44874ca)\
  2017-09-19 17:45:17 +0000
  * [MDEV-13844](https://jira.mariadb.org/browse/MDEV-13844) : Fix Windows warnings. Fix DBUG\_PRINT.
* [Revision #6857cb57fe](https://github.com/MariaDB/server/commit/6857cb57fe)\
  2017-10-01 00:30:58 +0400
  * [MDEV-13967](https://jira.mariadb.org/browse/MDEV-13967) Parameter data type control for Item\_long\_func
* [Revision #aa582dedcb](https://github.com/MariaDB/server/commit/aa582dedcb)\
  2017-09-30 11:17:19 +0400
  * [MDEV-13966](https://jira.mariadb.org/browse/MDEV-13966) Parameter data type control for Item\_temporal\_func
* [Revision #ca38b93e35](https://github.com/MariaDB/server/commit/ca38b93e35)\
  2017-09-29 22:44:07 +0400
  * [MDEV-13965](https://jira.mariadb.org/browse/MDEV-13965) Parameter data type control for Item\_longlong\_func
* [Revision #dc41bc14e0](https://github.com/MariaDB/server/commit/dc41bc14e0)\
  2017-09-29 20:14:55 +0400
  * [MDEV-13964](https://jira.mariadb.org/browse/MDEV-13964) Parameter data type control for Item\_real\_func
* [Revision #2cf3e2ea2f](https://github.com/MariaDB/server/commit/2cf3e2ea2f)\
  2017-09-27 10:25:18 +0200
  * Compressed columns tests (replication and partition)
* Merge [Revision #67eb1252ac](https://github.com/MariaDB/server/commit/67eb1252ac) 2017-09-28 18:56:15 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* Merge [Revision #7131a0a803](https://github.com/MariaDB/server/commit/7131a0a803) 2017-09-28 18:42:14 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #de7c2e5e54](https://github.com/MariaDB/server/commit/de7c2e5e54)\
  2017-09-28 15:12:00 +0300
  * Avoid implicit conversion from unsigned to signed
* [Revision #5a0cd753be](https://github.com/MariaDB/server/commit/5a0cd753be)\
  2017-09-28 11:59:28 +0300
  * Added missing test if table is transactional or not in Aria
* [Revision #8d006b9b12](https://github.com/MariaDB/server/commit/8d006b9b12)\
  2017-09-27 18:25:32 -0400
  * bump the VERSION
* [Revision #06f7a7620f](https://github.com/MariaDB/server/commit/06f7a7620f)\
  2017-09-26 21:51:10 +0300
  * Fixed compiler warning
* [Revision #2fdbe15032](https://github.com/MariaDB/server/commit/2fdbe15032)\
  2017-09-27 22:19:26 +0300
  * Correct test output after variable comment change
* [Revision #c6e8d66e59](https://github.com/MariaDB/server/commit/c6e8d66e59)\
  2017-09-27 17:55:48 +0000
  * Fix buildbot error on windows.
* [Revision #fd2c5d19d0](https://github.com/MariaDB/server/commit/fd2c5d19d0)\
  2017-09-26 15:35:34 +0300
  * fix a data race
* [Revision #a02b81daea](https://github.com/MariaDB/server/commit/a02b81daea)\
  2017-09-26 00:12:36 +0300
  * Moved autosetting of host\_cache\_size and back\_log to proper place
* [Revision #139441d0a0](https://github.com/MariaDB/server/commit/139441d0a0)\
  2017-09-28 17:48:33 +0400
  * A cleanup for [MDEV-13919](https://jira.mariadb.org/browse/MDEV-13919) sql\_mode=ORACLE: Derive length of VARCHAR SP param...
* [Revision #596baeb1bf](https://github.com/MariaDB/server/commit/596baeb1bf)\
  2017-09-28 17:26:23 +0400
  * A cleanup for [MDEV-10577](https://jira.mariadb.org/browse/MDEV-10577) and [MDEV-13919](https://jira.mariadb.org/browse/MDEV-13919): moving a few sp\_rcontext methods
* [Revision #3a6d94428f](https://github.com/MariaDB/server/commit/3a6d94428f)\
  2017-09-28 17:00:42 +0400
  * Fixing a warning introduced by [MDEV-13919](https://jira.mariadb.org/browse/MDEV-13919) ("true" instread of "return true")
* [Revision #c9a01420cf](https://github.com/MariaDB/server/commit/c9a01420cf)\
  2017-09-28 11:05:27 +0400
  * Additional tests for [MDEV-13919](https://jira.mariadb.org/browse/MDEV-13919) sql\_mode=ORACLE: Derive length of VARCHAR...
* [Revision #f44d5de689](https://github.com/MariaDB/server/commit/f44d5de689)\
  2017-09-27 16:49:40 +0200
  * [MDEV-13919](https://jira.mariadb.org/browse/MDEV-13919) sql\_mode=ORACLE: Derive length of VARCHAR SP parameters with no length from actual parameters
* [Revision #d387bc89ed](https://github.com/MariaDB/server/commit/d387bc89ed)\
  2017-09-26 08:03:08 +0400
  * [MDEV-13907](https://jira.mariadb.org/browse/MDEV-13907) compoind.test fails in build-bot for bb-10.2-ext
* Merge [Revision #4a32e2395e](https://github.com/MariaDB/server/commit/4a32e2395e) 2017-09-25 22:05:56 +0300 - Merge bb-10.2-ext into 10.3
* Merge [Revision #86c3ba65aa](https://github.com/MariaDB/server/commit/86c3ba65aa) 2017-09-25 21:45:44 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #742263df4f](https://github.com/MariaDB/server/commit/742263df4f)\
  2017-09-25 17:24:52 +0300
  * [MDEV-13256](https://jira.mariadb.org/browse/MDEV-13256) innodb.truncate\_debug fails in buildbot
* Merge [Revision #7dcb8816a1](https://github.com/MariaDB/server/commit/7dcb8816a1) 2017-09-25 13:46:54 +0300 - Merge 10.1 into 10.2
* Merge [Revision #84be33abe0](https://github.com/MariaDB/server/commit/84be33abe0) 2017-09-25 09:37:26 +0300 - Merge 10.0 into 10.1
* [Revision #19d21b9366](https://github.com/MariaDB/server/commit/19d21b9366)\
  2017-09-25 09:29:27 +0300
  * Cherry-pick the [MDEV-13898](https://jira.mariadb.org/browse/MDEV-13898) test changes from 10.2 to 10.0
* [Revision #78b63425a3](https://github.com/MariaDB/server/commit/78b63425a3)\
  2017-09-24 10:11:16 +0300
  * [MDEV-13899](https://jira.mariadb.org/browse/MDEV-13899) IMPORT TABLESPACE may corrupt ROW\_FORMAT=REDUNDANT tables
* [Revision #7128fefa4c](https://github.com/MariaDB/server/commit/7128fefa4c)\
  2017-09-23 23:23:05 +0200
  * Fix compile with -DWITHOUT\_DYNAMIC\_PLUGINS on Unix
* [Revision #f91eb71e1c](https://github.com/MariaDB/server/commit/f91eb71e1c)\
  2017-09-24 23:37:57 +0530
  * [MDEV-8840](https://jira.mariadb.org/browse/MDEV-8840): ANALYZE FORMAT=JSON produces wrong data with BKA
* [Revision #ea2162b6aa](https://github.com/MariaDB/server/commit/ea2162b6aa)\
  2017-09-24 23:33:44 +0530
  * [MDEV-11846](https://jira.mariadb.org/browse/MDEV-11846): ERROR 1114 (HY000) table full when performing GROUP BY
* [Revision #d8fe5fa131](https://github.com/MariaDB/server/commit/d8fe5fa131)\
  2017-09-22 17:54:23 +0300
  * Updated list of unstable tests for 10.1.27 release
* [Revision #a753caf135](https://github.com/MariaDB/server/commit/a753caf135)\
  2017-09-22 13:40:04 +0200
  * update rdiff after merge
* Merge [Revision #e0ebe3d083](https://github.com/MariaDB/server/commit/e0ebe3d083) 2017-09-22 10:31:49 +0300 - Merge 10.0 into 10.1
* [Revision #f6cb4f0a19](https://github.com/MariaDB/server/commit/f6cb4f0a19)\
  2017-09-22 10:28:14 +0300
  * [MDEV-13814](https://jira.mariadb.org/browse/MDEV-13814) Extra logging when innodb\_log\_archive=ON
* [Revision #8acb2b7b28](https://github.com/MariaDB/server/commit/8acb2b7b28)\
  2017-09-22 23:20:28 -0400
  * README.md - Secure (HTTPS) Links
* [Revision #80b9ce3593](https://github.com/MariaDB/server/commit/80b9ce3593)\
  2017-09-22 20:22:55 +0200
  * [MDEV-11553](https://jira.mariadb.org/browse/MDEV-11553) Can't restore a PERSISTENT column that uses DATE\_FORMAT()
* Merge [Revision #1320ad5b92](https://github.com/MariaDB/server/commit/1320ad5b92) 2017-09-23 20:22:30 +0200 - Merge branch '10.2' into bb-10.2-ext
* [Revision #88adfd0cea](https://github.com/MariaDB/server/commit/88adfd0cea)\
  2017-09-22 20:12:15 +0200
  * compiler warning
* [Revision #b75ca7e086](https://github.com/MariaDB/server/commit/b75ca7e086)\
  2017-09-23 11:40:12 +0200
  * cleanup: remove a duplicate check for GIT\_EXECUTABLE
* [Revision #d1d3aff985](https://github.com/MariaDB/server/commit/d1d3aff985)\
  2017-09-22 20:24:32 +0200
  * ignore generated file
* [Revision #840f1310cb](https://github.com/MariaDB/server/commit/840f1310cb)\
  2017-09-23 15:48:47 +0400
  * Fixing a few -Wconversion warnings
* [Revision #b773270c39](https://github.com/MariaDB/server/commit/b773270c39)\
  2017-09-23 12:04:15 +0300
  * Clarify a comment
* [Revision #e62b57e4d0](https://github.com/MariaDB/server/commit/e62b57e4d0)\
  2017-09-23 20:34:53 +0300
  * Relax a too strict debug assertion
* Merge [Revision #41da3ca9cc](https://github.com/MariaDB/server/commit/41da3ca9cc) 2017-09-23 09:37:18 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #b652430f00](https://github.com/MariaDB/server/commit/b652430f00)\
  2017-09-22 23:59:28 +0200
  * Fix tests
* [Revision #884bd1d61b](https://github.com/MariaDB/server/commit/884bd1d61b)\
  2017-09-23 00:55:28 +0400
  * [MDEV-13863](https://jira.mariadb.org/browse/MDEV-13863) sql\_mode=ORACLE: DECODE does not treat two NULLs as equivalent
* [Revision #c39a744616](https://github.com/MariaDB/server/commit/c39a744616)\
  2017-09-22 12:45:34 +0400
  * [MDEV-13864](https://jira.mariadb.org/browse/MDEV-13864) (final) Change Item\_func\_case to store the predicant in args\[0]
* [Revision #e12390a3bd](https://github.com/MariaDB/server/commit/e12390a3bd)\
  2017-09-22 10:48:34 +0400
  * [MDEV-13864](https://jira.mariadb.org/browse/MDEV-13864) (partial) Change Item\_func\_case to store the predicant in args\[0]
* [Revision #c027717adb](https://github.com/MariaDB/server/commit/c027717adb)\
  2017-09-21 09:14:01 +0000
  * [MDEV-12583](https://jira.mariadb.org/browse/MDEV-12583) post-fix
* [Revision #0f3735842f](https://github.com/MariaDB/server/commit/0f3735842f)\
  2017-09-20 23:58:26 +0000
  * [MDEV-12583](https://jira.mariadb.org/browse/MDEV-12583) : Bake the git hash into the binaries.
* [Revision #4e1e5a3266](https://github.com/MariaDB/server/commit/4e1e5a3266)\
  2017-09-21 17:01:24 +0400
  * [MDEV-13857](https://jira.mariadb.org/browse/MDEV-13857) - Use the 10.2 libmariadb in 10.3
* [Revision #5a8a3c3fe3](https://github.com/MariaDB/server/commit/5a8a3c3fe3)\
  2017-09-21 17:19:35 +0400
  * [MDEV-13855](https://jira.mariadb.org/browse/MDEV-13855) - Rename idle\_readwrite\_transaction\_timeout to idle\_write\_transaction\_timeout
* [Revision #d4b2dfa967](https://github.com/MariaDB/server/commit/d4b2dfa967)\
  2017-09-21 14:55:22 +0300
  * Replace dict\_table\_get\_n\_sys\_cols(table) with DATA\_N\_SYS\_COLS
* Merge [Revision #e3d44f5d62](https://github.com/MariaDB/server/commit/e3d44f5d62) 2017-09-21 08:12:19 +0300 - Merge bb-10.2-ext into 10.3
* Merge [Revision #f70865bc9e](https://github.com/MariaDB/server/commit/f70865bc9e) 2017-09-21 08:10:43 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #c7cc3d04da](https://github.com/MariaDB/server/commit/c7cc3d04da)\
  2017-09-21 08:10:38 +0300
  * After-merge fix: Adjust one more result
* Merge [Revision #916cd7846b](https://github.com/MariaDB/server/commit/916cd7846b) 2017-09-21 07:58:25 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #72a8024217](https://github.com/MariaDB/server/commit/72a8024217)\
  2017-09-21 07:58:08 +0300
  * After-merge fix: Adjust some results.
* [Revision #625951cb28](https://github.com/MariaDB/server/commit/625951cb28)\
  2017-09-20 20:47:18 +0300
  * After-merge fix: Adjust some results.
* Merge [Revision #fc3b1a7d2f](https://github.com/MariaDB/server/commit/fc3b1a7d2f) 2017-09-20 17:47:49 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #d176be8aea](https://github.com/MariaDB/server/commit/d176be8aea)\
  2017-09-20 15:07:06 +0300
  * remove dead code (#450)
* [Revision #7e4a3c29e1](https://github.com/MariaDB/server/commit/7e4a3c29e1)\
  2017-09-19 00:06:29 +0300
  * remove dead code
* Merge [Revision #e17a282da9](https://github.com/MariaDB/server/commit/e17a282da9) 2017-09-18 11:38:07 +0300 - Merge bb-10.2-ext into 10.3
* Merge [Revision #4cfef2a5a4](https://github.com/MariaDB/server/commit/4cfef2a5a4) 2017-09-18 11:35:47 +0300 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #fe949504f0](https://github.com/MariaDB/server/commit/fe949504f0) 2017-09-17 14:03:51 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #3060f9afd6](https://github.com/MariaDB/server/commit/3060f9afd6)\
  2017-09-15 15:53:41 +0300
  * [MDEV-13813](https://jira.mariadb.org/browse/MDEV-13813) Assertion \`size % 512U == 0' failed in log\_crypt upon upgrade from 10.2
* [Revision #8d64da8570](https://github.com/MariaDB/server/commit/8d64da8570)\
  2017-09-15 14:08:29 +0300
  * add TSAN option to cmake (#444)
* [Revision #c8cba4af55](https://github.com/MariaDB/server/commit/c8cba4af55)\
  2017-09-12 15:49:23 +0300
  * remove unneeded allocation
* Merge [Revision #46cf221815](https://github.com/MariaDB/server/commit/46cf221815) 2017-09-14 13:58:00 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #ca906fb273](https://github.com/MariaDB/server/commit/ca906fb273)\
  2017-09-14 13:57:14 +0400
  * [MDEV-13686](https://jira.mariadb.org/browse/MDEV-13686) EXCEPTION reserved keyword in SQL\_MODE=oracle but not in Oracle itself
* Merge [Revision #348eaf4252](https://github.com/MariaDB/server/commit/348eaf4252) 2017-09-14 09:12:47 +0300 - Merge bb-10.2-ext into 10.3
* Merge [Revision #2bd6ccae72](https://github.com/MariaDB/server/commit/2bd6ccae72) 2017-09-14 09:00:10 +0300 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #c97e504a5f](https://github.com/MariaDB/server/commit/c97e504a5f) 2017-09-14 08:09:44 +0300 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #178540b904](https://github.com/MariaDB/server/commit/178540b904) 2017-09-13 12:12:05 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #3a9ee22ba9](https://github.com/MariaDB/server/commit/3a9ee22ba9)\
  2017-09-10 10:08:52 -0700
  * Fixed the bug [MDEV-13734](https://jira.mariadb.org/browse/MDEV-13734).
* [Revision #61074d0426](https://github.com/MariaDB/server/commit/61074d0426)\
  2017-09-09 20:35:05 -0700
  * Fixed the bug [MDEV-13710](https://jira.mariadb.org/browse/MDEV-13710).
* [Revision #5e4aa1a2f8](https://github.com/MariaDB/server/commit/5e4aa1a2f8)\
  2017-09-08 11:26:35 -0700
  * Fixed the bug [MDEV-13709](https://jira.mariadb.org/browse/MDEV-13709).
* Merge [Revision #474f51711b](https://github.com/MariaDB/server/commit/474f51711b) 2017-09-08 15:59:06 +0300 - Merge bb-10.2-ext into 10.3
* Merge [Revision #fb14761d66](https://github.com/MariaDB/server/commit/fb14761d66) 2017-09-08 15:44:34 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #e022dde39c](https://github.com/MariaDB/server/commit/e022dde39c)\
  2017-09-07 15:43:45 +0300
  * Cleanups and fixes
* [Revision #4cb1a4fe7d](https://github.com/MariaDB/server/commit/4cb1a4fe7d)\
  2017-09-05 16:27:51 +0300
  * Give asserts if update\_stats() fails.
* [Revision #0eef1735b6](https://github.com/MariaDB/server/commit/0eef1735b6)\
  2017-09-05 16:26:29 +0300
  * Make debug multi thread safe
* [Revision #07977c13e7](https://github.com/MariaDB/server/commit/07977c13e7)\
  2017-09-05 16:24:29 +0300
  * Fixed monitor.test to handle statistics >= 10
* [Revision #ef2ecf0370](https://github.com/MariaDB/server/commit/ef2ecf0370)\
  2017-09-04 19:13:53 +0300
  * [MDEV-13732](https://jira.mariadb.org/browse/MDEV-13732) User with SELECT privilege can ALTER sequence
* [Revision #c3399d799f](https://github.com/MariaDB/server/commit/c3399d799f)\
  2017-09-08 13:12:01 +0300
  * Add some const qualifiers
* Merge [Revision #ae02407ce3](https://github.com/MariaDB/server/commit/ae02407ce3) 2017-09-07 12:30:56 +0300 - Merge bb-10.2-ext into 10.3
* Merge [Revision #a82ed92a6a](https://github.com/MariaDB/server/commit/a82ed92a6a) 2017-09-07 12:23:58 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #8c0d873b76](https://github.com/MariaDB/server/commit/8c0d873b76)\
  2017-09-06 18:16:43 +0300
  * [MDEV-13724](https://jira.mariadb.org/browse/MDEV-13724) ALTER TABLE…ALGORITHM=INPLACE is modifying the source table
* [Revision #fe47aee3bd](https://github.com/MariaDB/server/commit/fe47aee3bd)\
  2017-09-04 13:13:59 +0300
  * Inline definition of mem\_heap\_dup(), mem\_heap\_strdup(), mem\_heap\_strdupl()
* [Revision #83f9422f05](https://github.com/MariaDB/server/commit/83f9422f05)\
  2017-09-02 02:16:12 +0200
  * update sysvars\_server\_notembedded,32bit.rdiff
* [Revision #a0c0d5ea2f](https://github.com/MariaDB/server/commit/a0c0d5ea2f)\
  2017-09-01 19:42:33 +0000
  * Fix compile warnings.
* Merge [Revision #9691f58bef](https://github.com/MariaDB/server/commit/9691f58bef) 2017-09-01 22:16:12 +0300 - Merge bb-10.2-ext into 10.3
* Merge [Revision #9f580bbc0e](https://github.com/MariaDB/server/commit/9f580bbc0e) 2017-09-01 22:15:12 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #0015cbb755](https://github.com/MariaDB/server/commit/0015cbb755)\
  2017-08-29 13:16:47 +0200
  * [MDEV-13656](https://jira.mariadb.org/browse/MDEV-13656) 10.3 does not build on CentOS 5 x86
* [Revision #016c35a7f2](https://github.com/MariaDB/server/commit/016c35a7f2)\
  2017-09-01 18:33:46 +0300
  * [MDEV-13690](https://jira.mariadb.org/browse/MDEV-13690): Remove unnecessary innodb\_use\_mtflush, innodb\_mtflush\_threads parameters and related code
* [Revision #9ff7129f16](https://github.com/MariaDB/server/commit/9ff7129f16)\
  2017-09-01 16:07:37 +0200
  * Fix of a warning of gcc 7.0
* [Revision #a8ec55e4e8](https://github.com/MariaDB/server/commit/a8ec55e4e8)\
  2017-09-01 16:20:40 +0300
  * [MDEV-13359](https://jira.mariadb.org/browse/MDEV-13359) Enable ALTER TABLE...ALGORITHM=INPLACE for compressed columns
* [Revision #8a8cca2865](https://github.com/MariaDB/server/commit/8a8cca2865)\
  2017-09-01 12:45:33 +0300
  * Fix a buffer overflow in INFORMATION\_SCHEMA.GLOBAL\_VARIABLES, caused by [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179)
* Merge [Revision #4e1fa7f63d](https://github.com/MariaDB/server/commit/4e1fa7f63d) 2017-09-01 11:33:45 +0300 - Merge bb-10.2-ext into 10.3
* [Revision #2f3968d98f](https://github.com/MariaDB/server/commit/2f3968d98f)\
  2017-09-01 11:29:11 +0300
  * After-merge fixes for Galera test results
* Merge [Revision #05cc028f56](https://github.com/MariaDB/server/commit/05cc028f56) 2017-09-01 11:24:36 +0300 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #6749d39a95](https://github.com/MariaDB/server/commit/6749d39a95) 2017-09-01 08:47:55 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #ff81faf670](https://github.com/MariaDB/server/commit/ff81faf670)\
  2017-08-31 18:03:50 +0300
  * [MDEV-13654](https://jira.mariadb.org/browse/MDEV-13654) Various crashes due to DB\_TRX\_ID mismatch in table-rebuilding ALTER TABLE…LOCK=NONE
* [Revision #fdc4779235](https://github.com/MariaDB/server/commit/fdc4779235)\
  2017-04-24 17:54:18 +0400
  * [MDEV-11371](https://jira.mariadb.org/browse/MDEV-11371) - column compression
* [Revision #dd4e9cdded](https://github.com/MariaDB/server/commit/dd4e9cdded)\
  2017-07-27 11:44:20 +0400
  * Get rid of Field::do\_save\_field\_metadata()
* [Revision #41d89b7da1](https://github.com/MariaDB/server/commit/41d89b7da1)\
  2017-08-25 12:56:42 +0300
  * Added HITS column to QUERY\_CACHE\_INFO table
* [Revision #cf3a74eb60](https://github.com/MariaDB/server/commit/cf3a74eb60)\
  2017-08-25 12:43:28 +0300
  * Counting hits for queries in query cache.
* [Revision #5dd8e1bf2d](https://github.com/MariaDB/server/commit/5dd8e1bf2d)\
  2017-08-25 14:36:13 +0300
  * simplify READ\_RECORD usage NFC
* [Revision #e1051590b6](https://github.com/MariaDB/server/commit/e1051590b6)\
  2017-08-29 12:30:30 -0400
  * bump the VERSION
* [Revision #62139dc2e2](https://github.com/MariaDB/server/commit/62139dc2e2)\
  2017-08-28 17:11:33 +0200
  * [MDEV-13656](https://jira.mariadb.org/browse/MDEV-13656) 10.3 does not build on CentOS 5 x86
* [Revision #1a503b2786](https://github.com/MariaDB/server/commit/1a503b2786)\
  2017-08-28 15:33:03 +0200
  * don't flush dbug buffers for every assert
* [Revision #c10fadb9d9](https://github.com/MariaDB/server/commit/c10fadb9d9)\
  2017-08-28 13:40:45 +0300
  * [MDEV-13603](https://jira.mariadb.org/browse/MDEV-13603) Sporadic failure in innodb.dml\_purge

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
