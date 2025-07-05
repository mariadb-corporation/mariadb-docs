# MariaDB 10.4.4 Changelog

The most recent release of [MariaDB 10.4](../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/release-notes-mariadb-10-4-series/mariadb-10-4-34-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.4)[Release Notes](../../old-releases/release-notes-mariadb-10-4-series/mariadb-1044-release-notes.md)[Changelog](mariadb-1044-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 8 Apr 2019

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-4-series/mariadb-1044-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #eb872ceb27](https://github.com/MariaDB/server/commit/eb872ceb27)\
  2019-04-06 12:33:51 +0300
  * Fixed wsrep replaying for stored procedures (#1256)
* [Revision #fe62ff6e1c](https://github.com/MariaDB/server/commit/fe62ff6e1c)\
  2019-04-06 12:25:29 +0300
  * [MDEV-18265](https://jira.mariadb.org/browse/MDEV-18265): Replace deprecated variable debug to debug\_dbug on Galera tests
* [Revision #8a194d99cf](https://github.com/MariaDB/server/commit/8a194d99cf)\
  2019-04-06 10:44:53 +0200
  * update test results
* [Revision #371d6ac1bd](https://github.com/MariaDB/server/commit/371d6ac1bd)\
  2019-04-06 11:38:18 +0400
  * [MDEV-19197](https://jira.mariadb.org/browse/MDEV-19197) Move ASSERT\_COLUMN\_MARKED\_FOR\_XXX as methods to Field
* [Revision #18bf0bf496](https://github.com/MariaDB/server/commit/18bf0bf496)\
  2019-04-05 23:14:05 -0700
  * [MDEV-18956](https://jira.mariadb.org/browse/MDEV-18956) Assertion \`sel->quick' failed in JOIN::make\_range\_rowid\_filters
* [Revision #a2e477ffd0](https://github.com/MariaDB/server/commit/a2e477ffd0)\
  2019-04-06 00:04:52 +0300
  * [MDEV-19186](https://jira.mariadb.org/browse/MDEV-19186): Assertion \`field->table == table' failed in create\_tmp\_table
* [Revision #694d1a50bd](https://github.com/MariaDB/server/commit/694d1a50bd)\
  2019-04-05 22:55:20 +0300
  * [MDEV-19185](https://jira.mariadb.org/browse/MDEV-19185): Pushdown constant function defined with subquery
* [Revision #c84dde148f](https://github.com/MariaDB/server/commit/c84dde148f)\
  2019-04-05 16:28:41 +0400
  * [MDEV-19184](https://jira.mariadb.org/browse/MDEV-19184) Crash in IS\_IPV6(\_ucs2 0x0031)
* Merge [Revision #02d9b048a2](https://github.com/MariaDB/server/commit/02d9b048a2) 2019-04-05 11:41:03 +0300 - Merge 10.3 into 10.4
* Merge [Revision #d5a2bc6a0f](https://github.com/MariaDB/server/commit/d5a2bc6a0f) 2019-04-04 19:41:12 +0300 - Merge 10.2 into 10.3
* Merge [Revision #b30fb701cc](https://github.com/MariaDB/server/commit/b30fb701cc) 2019-04-04 09:05:45 +0300 - Merge 10.1 into 10.2
* [Revision #71a2e6a3c6](https://github.com/MariaDB/server/commit/71a2e6a3c6)\
  2019-04-01 19:42:26 +0300
  * index\_merge\_innodb did sometimes give wrong results
* [Revision #6a9b216301](https://github.com/MariaDB/server/commit/6a9b216301)\
  2019-04-03 19:50:51 +0300
  * Fix clang -Wunused-private-field
* [Revision #f602385776](https://github.com/MariaDB/server/commit/f602385776)\
  2019-04-04 08:57:53 +0300
  * Do not pass table\_name\_t to printf-like functions
* [Revision #b718ec055d](https://github.com/MariaDB/server/commit/b718ec055d)\
  2019-04-03 21:41:19 +0300
  * [MDEV-18836](https://jira.mariadb.org/browse/MDEV-18836): Adjust a suppression
* [Revision #c676de1692](https://github.com/MariaDB/server/commit/c676de1692)\
  2019-04-03 21:00:13 +0300
  * Fix the non-debug build
* Merge [Revision #28636a92ed](https://github.com/MariaDB/server/commit/28636a92ed) 2019-04-03 19:57:29 +0300 - Merge 10.1 into 10.2
* [Revision #1f3bcff1f2](https://github.com/MariaDB/server/commit/1f3bcff1f2)\
  2019-04-03 19:46:34 +0300
  * Remove unused declarations
* [Revision #fa14784301](https://github.com/MariaDB/server/commit/fa14784301)\
  2019-04-03 19:21:54 +0300
  * Fix more -Wnonnull-compare
* [Revision #cad56fbaba](https://github.com/MariaDB/server/commit/cad56fbaba)\
  2019-04-03 16:10:20 +0300
  * [MDEV-18733](https://jira.mariadb.org/browse/MDEV-18733) MariaDB slow start after crash recovery
* [Revision #7984ea80de](https://github.com/MariaDB/server/commit/7984ea80de)\
  2019-04-03 17:10:54 +0300
  * Remove a useless CHECK TABLE printout for debug builds
* [Revision #a1ec7ac4f4](https://github.com/MariaDB/server/commit/a1ec7ac4f4)\
  2019-04-03 15:56:28 +0300
  * Clean up table\_name\_t
* [Revision #5da6944ea3](https://github.com/MariaDB/server/commit/5da6944ea3)\
  2019-04-04 20:00:41 +0200
  * update C/C
* [Revision #d2013e7328](https://github.com/MariaDB/server/commit/d2013e7328)\
  2019-04-04 16:36:26 -0700
  * [MDEV-18982](https://jira.mariadb.org/browse/MDEV-18982) Partition pruning with column list causes syntax error in 10.4
* [Revision #ae15f91f22](https://github.com/MariaDB/server/commit/ae15f91f22)\
  2019-03-23 15:28:22 +0300
  * [MDEV-18769](https://jira.mariadb.org/browse/MDEV-18769) Assertion \`fixed == 1' failed in Item\_cond\_or::val\_int
* [Revision #3a3d5ba235](https://github.com/MariaDB/server/commit/3a3d5ba235)\
  2019-03-14 17:28:20 +0300
  * [MDEV-13301](https://jira.mariadb.org/browse/MDEV-13301) Optimize DROP INDEX, ADD INDEX into RENAME INDEX
* [Revision #5d8ca98997](https://github.com/MariaDB/server/commit/5d8ca98997)\
  2019-01-30 00:00:06 +0400
  * Get rid of rea\_create\_table()
* [Revision #38e151d155](https://github.com/MariaDB/server/commit/38e151d155)\
  2019-02-05 18:41:33 +0400
  * Fix inplace ALTER TABLE to not register tmp table
* [Revision #914bb5387f](https://github.com/MariaDB/server/commit/914bb5387f)\
  2019-01-30 00:37:11 +0400
  * Removed redundant partitioning check
* [Revision #878f83151f](https://github.com/MariaDB/server/commit/878f83151f)\
  2019-01-29 23:36:44 +0400
  * Simplified dd\_recreate\_table()
* [Revision #1dac55cf0e](https://github.com/MariaDB/server/commit/1dac55cf0e)\
  2019-02-06 11:41:36 +0400
  * Removed redundant SE lock for tmp tables
* Merge [Revision #3638636f9b](https://github.com/MariaDB/server/commit/3638636f9b) 2019-04-03 14:11:08 +0300 - Merge 10.3 into 10.4
* [Revision #532fffb4cc](https://github.com/MariaDB/server/commit/532fffb4cc)\
  2019-04-03 14:07:18 +0300
  * Fix the non-debug build
* Merge [Revision #c8f8d5ceb7](https://github.com/MariaDB/server/commit/c8f8d5ceb7) 2019-04-03 11:42:11 +0300 - Merge 10.3 into 10.4
* Merge [Revision #c6b8b05be4](https://github.com/MariaDB/server/commit/c6b8b05be4) 2019-04-03 11:22:51 +0300 - Merge 10.2 into 10.3
* [Revision #03672a0573](https://github.com/MariaDB/server/commit/03672a0573)\
  2019-04-03 10:50:43 +0300
  * [MDEV-11487](https://jira.mariadb.org/browse/MDEV-11487): Remove dict\_table\_get\_n\_sys\_cols()
* Merge [Revision #dbc716675b](https://github.com/MariaDB/server/commit/dbc716675b) 2019-04-03 10:29:15 +0300 - Merge 10.1 into 10.2
* [Revision #c0fca2863b](https://github.com/MariaDB/server/commit/c0fca2863b)\
  2019-04-03 09:46:49 +0300
  * Fix -Wnonnull-compare
* [Revision #65d758aa89](https://github.com/MariaDB/server/commit/65d758aa89)\
  2019-03-30 12:52:23 +0100
  * [MDEV-18298](https://jira.mariadb.org/browse/MDEV-18298) Crashes server with segfault during role grants
* [Revision #409f69cd74](https://github.com/MariaDB/server/commit/409f69cd74)\
  2019-03-31 17:24:44 +0200
  * cmake: only search for libraries that are needed
* [Revision #7b527e6334](https://github.com/MariaDB/server/commit/7b527e6334)\
  2019-03-31 10:31:54 +0200
  * cmake: fix krb5 detection on SUSE
* [Revision #0b2042fdca](https://github.com/MariaDB/server/commit/0b2042fdca)\
  2019-03-29 22:06:24 +0100
  * speedup RPM builds
* [Revision #5f31f8cc87](https://github.com/MariaDB/server/commit/5f31f8cc87)\
  2019-04-03 10:56:04 +0300
  * Fix cmake -DWITH\_WSREP=OFF
* [Revision #ba7d33a898](https://github.com/MariaDB/server/commit/ba7d33a898)\
  2019-03-28 11:33:14 +0530
  * [MDEV-18820](https://jira.mariadb.org/browse/MDEV-18820) Assertion \`lock\_table\_has(trx, index->table, LOCK\_IX)' failed in lock\_rec\_insert\_check\_and\_lock upon INSERT into table with blob key
* [Revision #afca4a3a34](https://github.com/MariaDB/server/commit/afca4a3a34)\
  2019-04-03 09:23:29 +0300
  * [MDEV-19156](https://jira.mariadb.org/browse/MDEV-19156): Galera test failure on galerra\_sr\_cc\_master
* Merge [Revision #268d46b87d](https://github.com/MariaDB/server/commit/268d46b87d) 2019-04-03 09:20:44 +0300 - Merge 10.3 into 10.4
* Merge [Revision #977d7a7572](https://github.com/MariaDB/server/commit/977d7a7572) 2019-04-03 08:21:43 +0300 - Merge 10.2 into 10.3
* [Revision #e3f44d8d0e](https://github.com/MariaDB/server/commit/e3f44d8d0e)\
  2019-04-02 16:40:27 +0300
  * [MDEV-19085](https://jira.mariadb.org/browse/MDEV-19085): Remove a bogus debug assertion
* Merge [Revision #849734376a](https://github.com/MariaDB/server/commit/849734376a) 2019-04-03 08:21:00 +0300 - Merge bb-10.3-release into 10.3
* [Revision #f5176c2dfa](https://github.com/MariaDB/server/commit/f5176c2dfa)\
  2019-04-02 11:31:53 -0400
  * bump the VERSION
* [Revision #b896f60a73](https://github.com/MariaDB/server/commit/b896f60a73)\
  2019-04-03 09:19:12 +0300
  * Fix -Wformat and -Wnonnull-compare for WSREP
* [Revision #0dc442ac61](https://github.com/MariaDB/server/commit/0dc442ac61)\
  2019-04-03 00:29:24 +0530
  * [MDEV-18942](https://jira.mariadb.org/browse/MDEV-18942): Json\_writer::add\_bool: Conditional jump or move depends on uninitialised value upon fulltext search under optimizer trace
* [Revision #eac97ef44c](https://github.com/MariaDB/server/commit/eac97ef44c)\
  2019-03-27 20:48:28 +0530
  * [MDEV-18962](https://jira.mariadb.org/browse/MDEV-18962): ASAN heap-buffer-overflow in Single\_line\_formatting\_helper::on\_add\_str with optimizer trace
* [Revision #4d12a6458e](https://github.com/MariaDB/server/commit/4d12a6458e)\
  2019-04-01 20:29:45 +0400
  * [MDEV-19125](https://jira.mariadb.org/browse/MDEV-19125) Change Send\_field::type from enum\_field\_types to Type\_handler\*
* [Revision #e10f9e6c81](https://github.com/MariaDB/server/commit/e10f9e6c81)\
  2019-04-02 15:43:46 +0300
  * Adjust wsrep, galera, galera\_3nodes, galera\_sr and galera\_3nodes\_sr tests after commit b5615eff0d00cfb4c60b9d1bf67094da7c2258a6
* Merge [Revision #a10e29cc6d](https://github.com/MariaDB/server/commit/a10e29cc6d) 2019-04-02 13:55:04 +0300 - Merge 10.3 into 10.4
* Merge [Revision #44e64fd7e0](https://github.com/MariaDB/server/commit/44e64fd7e0) 2019-04-02 13:48:42 +0300 - Merge 10.2 into 10.3
* [Revision #5633f83ca4](https://github.com/MariaDB/server/commit/5633f83ca4)\
  2019-04-02 13:46:36 +0300
  * Fix integer type mismatch
* [Revision #8650848ec3](https://github.com/MariaDB/server/commit/8650848ec3)\
  2019-04-02 13:43:22 +0300
  * [MDEV-19128](https://jira.mariadb.org/browse/MDEV-19128) fil\_name\_parse() for MLOG\_FILE\_ is not portable
* [Revision #610ec192ec](https://github.com/MariaDB/server/commit/610ec192ec)\
  2019-03-22 21:08:34 +1000
  * [MDEV-17320](https://jira.mariadb.org/browse/MDEV-17320) add Feature\_application\_time\_periods status variable
* [Revision #5fc6ad95d4](https://github.com/MariaDB/server/commit/5fc6ad95d4)\
  2019-03-14 14:45:01 +1000
  * [MDEV-18921](https://jira.mariadb.org/browse/MDEV-18921) Server crashes in bitmap\_bits\_set or bitmap\_is\_set upon UPDATE IGNORE .. FOR PORTION with binary logging
* [Revision #7e3e2d060b](https://github.com/MariaDB/server/commit/7e3e2d060b)\
  2019-03-13 22:31:43 +1000
  * [MDEV-18859](https://jira.mariadb.org/browse/MDEV-18859) Server crashes in bitmap\_bits\_set / pack\_row / THD::binlog\_write\_row upon DELETE .. FOR PORTION with binary logging
* [Revision #04055060b6](https://github.com/MariaDB/server/commit/04055060b6)\
  2019-03-13 22:25:48 +1000
  * [MDEV-18852](https://jira.mariadb.org/browse/MDEV-18852) [MDEV-18853](https://jira.mariadb.org/browse/MDEV-18853) fix `period.delete`, `period.update` tests crashes with \`\`--ps-protocol\`
* [Revision #74c9872a9a](https://github.com/MariaDB/server/commit/74c9872a9a)\
  2017-04-28 11:22:30 +1000
  * [MDEV-10797](https://jira.mariadb.org/browse/MDEV-10797) RPM includes init script and a systemd unit
* [Revision #4975d25390](https://github.com/MariaDB/server/commit/4975d25390)\
  2019-03-22 01:55:35 +0100
  * don't run SysV scripts in scriptlets if systemd is used
* [Revision #4a7d7e79a2](https://github.com/MariaDB/server/commit/4a7d7e79a2)\
  2019-03-29 19:24:51 +0100
  * update test results
* [Revision #79fe17567a](https://github.com/MariaDB/server/commit/79fe17567a)\
  2019-03-29 20:38:53 +0100
  * gcc 8 warnings
* [Revision #f3adfcb523](https://github.com/MariaDB/server/commit/f3adfcb523)\
  2019-04-02 11:59:55 +0300
  * After-merge fix: Initialize all fields
* Merge [Revision #5c3ff5cb93](https://github.com/MariaDB/server/commit/5c3ff5cb93) 2019-04-02 11:04:54 +0300 - Merge 10.3 into 10.4
* Merge [Revision #7b42d892de](https://github.com/MariaDB/server/commit/7b42d892de) 2019-04-02 09:19:34 +0300 - Merge 10.2 into 10.3
* Merge [Revision #bce380f2a5](https://github.com/MariaDB/server/commit/bce380f2a5) 2019-04-02 09:14:15 +0300 - Merge 10.1 into 10.2
* [Revision #b88f378648](https://github.com/MariaDB/server/commit/b88f378648)\
  2019-04-02 08:48:54 +0300
  * Omit the definition of unused function yyset\_extra()
* [Revision #619d22dde5](https://github.com/MariaDB/server/commit/619d22dde5)\
  2019-04-01 13:03:18 +0300
  * Rebuild the InnoDB lexical analyzers with flex 2.6.4
* [Revision #23eeecd68f](https://github.com/MariaDB/server/commit/23eeecd68f)\
  2019-04-01 10:32:03 +0300
  * [MDEV-19111](https://jira.mariadb.org/browse/MDEV-19111) Unused field INFORMATION\_SCHEMA.INNODB\_TABLESPACES\_SCRUBBING.ROTATING\_OR\_FLUSHING
* [Revision #d59ad6972b](https://github.com/MariaDB/server/commit/d59ad6972b)\
  2019-04-01 18:13:11 +0300
  * [MDEV-19085](https://jira.mariadb.org/browse/MDEV-19085): Fix a typo that was caught by GCC 5.4
* Merge [Revision #8f01a17292](https://github.com/MariaDB/server/commit/8f01a17292) 2019-04-01 14:25:41 +0300 - Merge 10.2 into 10.3
* [Revision #f055da9b84](https://github.com/MariaDB/server/commit/f055da9b84)\
  2019-04-01 14:24:15 +0300
  * [MDEV-19085](https://jira.mariadb.org/browse/MDEV-19085) Assertion failures due to virtual columns after upgrading from 10.1
* [Revision #833071b857](https://github.com/MariaDB/server/commit/833071b857)\
  2019-04-01 12:58:51 +0300
  * Disable tests in rocksdb\_stress suite (which was enabled a few commits ago)
* Merge [Revision #0ffea01da5](https://github.com/MariaDB/server/commit/0ffea01da5) 2019-04-01 09:22:19 +0300 - Merge 10.2 into 10.3
* [Revision #fe1dfe3928](https://github.com/MariaDB/server/commit/fe1dfe3928)\
  2019-03-30 20:00:13 +0300
  * [MDEV-19089](https://jira.mariadb.org/browse/MDEV-19089), part #2: mark rocksdb.deadlock as "big test"
* [Revision #c2d9a346ff](https://github.com/MariaDB/server/commit/c2d9a346ff)\
  2019-03-30 19:50:55 +0300
  * [MDEV-19089](https://jira.mariadb.org/browse/MDEV-19089) part #1: adapt rocksdb\_stress suite for MariaDB
* [Revision #76934212eb](https://github.com/MariaDB/server/commit/76934212eb)\
  2018-09-23 12:19:24 +0300
  * remove unneeded code
* [Revision #b66164ab56](https://github.com/MariaDB/server/commit/b66164ab56)\
  2018-08-29 13:50:52 +0300
  * remove dead code
* [Revision #65bd38204b](https://github.com/MariaDB/server/commit/65bd38204b)\
  2019-03-29 12:06:34 +0200
  * Update 10.2 man pages
* [Revision #f9ab7b473a](https://github.com/MariaDB/server/commit/f9ab7b473a)\
  2019-04-01 17:58:32 +0300
  * [MDEV-18623](https://jira.mariadb.org/browse/MDEV-18623) Assertion after DROP FULLTEXT INDEX and removing NOT NULL
* [Revision #43c20542dd](https://github.com/MariaDB/server/commit/43c20542dd)\
  2019-04-01 16:11:41 +0300
  * [MDEV-19030](https://jira.mariadb.org/browse/MDEV-19030): Assertion failed in rec\_init\_offsets() after DROP COLUMN
* [Revision #517486963b](https://github.com/MariaDB/server/commit/517486963b)\
  2019-04-02 11:01:27 +0300
  * Adjust tests after commit b5615eff0d00cfb4c60b9d1bf67094da7c2258a6
* [Revision #ea5cda5269](https://github.com/MariaDB/server/commit/ea5cda5269)\
  2019-04-02 11:40:22 +0400
  * [MDEV-18402](https://jira.mariadb.org/browse/MDEV-18402) Assertion \`sec.sec() <= 59' failed in Item\_func\_maketime::get\_date
* [Revision #b9ea778f6c](https://github.com/MariaDB/server/commit/b9ea778f6c)\
  2019-04-02 11:06:07 +0400
  * [MDEV-18503](https://jira.mariadb.org/browse/MDEV-18503) Assertion \`native.length() == binlen' failed in Type\_handler\_timestamp\_common::make\_sort\_key
* [Revision #d8e936a2af](https://github.com/MariaDB/server/commit/d8e936a2af)\
  2019-04-02 10:14:39 +0400
  * Tests for [MDEV-18595](https://jira.mariadb.org/browse/MDEV-18595) Assertion \`0' failed in Item\_cache\_timestamp::val\_datetime\_packed / Predicant\_to\_list\_comparator::cmp\_arg
* [Revision #5201a1d080](https://github.com/MariaDB/server/commit/5201a1d080)\
  2019-04-02 09:56:31 +0400
  * [MDEV-18240](https://jira.mariadb.org/browse/MDEV-18240) Assertion \`0' failed in Item\_cache\_timestamp::val\_datetime\_packed
* [Revision #1b4bb3b5bb](https://github.com/MariaDB/server/commit/1b4bb3b5bb)\
  2019-04-02 09:13:16 +0400
  * [MDEV-19124](https://jira.mariadb.org/browse/MDEV-19124) Assertion \`0' failed in Item::val\_native
* [Revision #8840045021](https://github.com/MariaDB/server/commit/8840045021)\
  2019-04-01 19:42:26 +0300
  * index\_merge\_innodb did sometimes give wrong results
* [Revision #48810a0014](https://github.com/MariaDB/server/commit/48810a0014)\
  2019-03-25 16:00:45 +0200
  * [MDEV-19116](https://jira.mariadb.org/browse/MDEV-19116) Speed up rotation of binary logs
* [Revision #adb7016214](https://github.com/MariaDB/server/commit/adb7016214)\
  2019-03-25 15:57:00 +0200
  * [MDEV-19117](https://jira.mariadb.org/browse/MDEV-19117) Don't keep binary log index file locked during show binary logs
* [Revision #e3bffd579f](https://github.com/MariaDB/server/commit/e3bffd579f)\
  2019-03-26 17:36:20 +0200
  * Removed some warnings from -Wimplicit-fallthrough= with build scripts
* [Revision #b5615eff0d](https://github.com/MariaDB/server/commit/b5615eff0d)\
  2019-03-25 08:02:22 +0200
  * Write information about restart in .result
* [Revision #6fd7a4b601](https://github.com/MariaDB/server/commit/6fd7a4b601)\
  2019-03-22 07:02:40 +0200
  * Fixed uninitialized bug in Range\_rowid\_filter\_cost\_info
* [Revision #5b15f68e0f](https://github.com/MariaDB/server/commit/5b15f68e0f)\
  2019-03-31 13:44:43 +0300
  * Fixed valgrind warning: Wrong usage of c\_ptr()
* [Revision #48c6726b13](https://github.com/MariaDB/server/commit/48c6726b13)\
  2019-03-22 07:01:34 +0200
  * Updated valgrind.supp for OpenSLL 1.0.1l
* [Revision #10dd290b4b](https://github.com/MariaDB/server/commit/10dd290b4b)\
  2019-04-01 11:57:06 +0300
  * [MDEV-17380](https://jira.mariadb.org/browse/MDEV-17380) innodb\_flush\_neighbors=ON should be ignored on SSD
* [Revision #2d825e97df](https://github.com/MariaDB/server/commit/2d825e97df)\
  2019-04-01 10:09:24 +0400
  * Cleanup: removing unused type LEX\_TYPE and #include
* [Revision #17cbae6501](https://github.com/MariaDB/server/commit/17cbae6501)\
  2018-11-14 03:27:55 +1000
  * Fix error failed to compile regex
* [Revision #39f195052c](https://github.com/MariaDB/server/commit/39f195052c)\
  2019-03-28 17:22:04 +0100
  * [MDEV-19068](https://jira.mariadb.org/browse/MDEV-19068) - rename eventlog source to MariaDB.
* [Revision #8d27f1e4f4](https://github.com/MariaDB/server/commit/8d27f1e4f4)\
  2019-03-28 13:12:28 +0200
  * Update 10.4 man pages
* [Revision #27ae38e034](https://github.com/MariaDB/server/commit/27ae38e034)\
  2019-03-29 10:56:45 +0200
  * [MDEV-18590](https://jira.mariadb.org/browse/MDEV-18590): galera.versioning\_trx\_id: Test failure: mysqltest: Result content mismatch
* [Revision #780d77109b](https://github.com/MariaDB/server/commit/780d77109b)\
  2019-03-29 12:26:42 +0400
  * [MDEV-17969](https://jira.mariadb.org/browse/MDEV-17969) Assertion \`name' failed in THD::push\_warning\_truncated\_value\_for\_field
* [Revision #a5ac029f8a](https://github.com/MariaDB/server/commit/a5ac029f8a)\
  2019-03-28 10:28:52 +0400
  * [MDEV-19062](https://jira.mariadb.org/browse/MDEV-19062) Item\_sum\_variance: move recurrence\_m, recurrence\_s, count to a separate class
* [Revision #3e1f3d3e2f](https://github.com/MariaDB/server/commit/3e1f3d3e2f)\
  2019-03-27 17:28:23 +0400
  * A cleanup in Item\_sum: removing dead code
* [Revision #f78eb52fba](https://github.com/MariaDB/server/commit/f78eb52fba)\
  2019-03-27 14:33:04 +0100
  * Make test galera\_sr.GCF-1018 deterministic (#1245)
* Merge [Revision #0bc4260226](https://github.com/MariaDB/server/commit/0bc4260226) 2019-03-26 17:43:59 +0200 - Merge 10.3 into 10.4
* [Revision #7225bef727](https://github.com/MariaDB/server/commit/7225bef727)\
  2019-03-26 16:31:32 +0200
  * Fix crash recovery with small buffer pool
* Merge [Revision #8b480df63e](https://github.com/MariaDB/server/commit/8b480df63e) 2019-03-25 17:18:15 +0200 - Merge 10.3 into 10.4
* [Revision #c0ba036b77](https://github.com/MariaDB/server/commit/c0ba036b77)\
  2019-03-23 17:12:23 +0400
  * Fixed build failure
* [Revision #901e3ddf79](https://github.com/MariaDB/server/commit/901e3ddf79)\
  2019-03-22 14:54:24 +0530
  * [MDEV-18904](https://jira.mariadb.org/browse/MDEV-18904) Assertion \`m\_part\_spec.start\_part >= m\_part\_spec.end\_part' failed in ha\_partition::index\_read\_idx\_map
* [Revision #0c567648a4](https://github.com/MariaDB/server/commit/0c567648a4)\
  2019-03-22 13:30:22 +0530
  * Revert ([MDEV-18888](https://jira.mariadb.org/browse/MDEV-18888))2b06de8064660c5c, fix it in different way And add test case for [MDEV-18953](https://jira.mariadb.org/browse/MDEV-18953)
* [Revision #ef33e26f6e](https://github.com/MariaDB/server/commit/ef33e26f6e)\
  2019-03-23 09:47:29 +1200
  * Add Clion folder to gitignore (#928)
* Merge [Revision #ca80e14a88](https://github.com/MariaDB/server/commit/ca80e14a88) 2019-03-22 13:20:44 +0200 - Merge 10.3 into 10.4
* [Revision #c23d4700e6](https://github.com/MariaDB/server/commit/c23d4700e6)\
  2019-03-19 16:40:23 +0530
  * [MDEV-18901](https://jira.mariadb.org/browse/MDEV-18901) Wrong results after ADD UNIQUE INDEX(blob\_column)
* [Revision #625aa232a6](https://github.com/MariaDB/server/commit/625aa232a6)\
  2019-03-19 16:36:54 +0530
  * [MDEV-18967](https://jira.mariadb.org/browse/MDEV-18967) Load data in system version with long unique does not work
* [Revision #1dffa9d9c1](https://github.com/MariaDB/server/commit/1dffa9d9c1)\
  2019-03-21 12:05:04 +0200
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441): Rename buf\_pool\_t::io\_buf from buf\_pool->tmp\_arr
* [Revision #a9c230669e](https://github.com/MariaDB/server/commit/a9c230669e)\
  2019-03-21 11:26:12 +0200
  * Fix -Wmaybe-uninitialized (non-functional change)
* [Revision #2b00bdfd25](https://github.com/MariaDB/server/commit/2b00bdfd25)\
  2019-03-21 11:25:41 +0200
  * [MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026): Avoid uninitialized variable
* [Revision #b6a6aa5b5a](https://github.com/MariaDB/server/commit/b6a6aa5b5a)\
  2019-03-21 11:23:34 +0200
  * [MDEV-371](https://jira.mariadb.org/browse/MDEV-371): Enable a debug function only in debug builds
* Merge [Revision #7af0de9fa3](https://github.com/MariaDB/server/commit/7af0de9fa3) 2019-03-21 11:22:13 +0200 - Merge 10.3 into 10.4
* [Revision #8dffaaef72](https://github.com/MariaDB/server/commit/8dffaaef72)\
  2019-03-13 12:58:32 +0100
  * [MDEV-12836](https://jira.mariadb.org/browse/MDEV-12836) Avoid table rebuild when removing of auto\_increment settings
* [Revision #23a7693a68](https://github.com/MariaDB/server/commit/23a7693a68)\
  2019-03-13 12:42:42 +0100
  * [MDEV-18275](https://jira.mariadb.org/browse/MDEV-18275) Live upgrade from 5.5 does not work: InnoDB stat tables are used before creation
* Merge [Revision #96f8793a7a](https://github.com/MariaDB/server/commit/96f8793a7a) 2019-03-20 19:08:47 +0200 - Merge 10.3 into 10.4
* Merge [Revision #514b305dfb](https://github.com/MariaDB/server/commit/514b305dfb) 2019-03-20 10:26:49 +0200 - Merge 10.3 into 10.4
* [Revision #de51acd037](https://github.com/MariaDB/server/commit/de51acd037)\
  2019-02-27 13:52:37 +1100
  * [MDEV-18726](https://jira.mariadb.org/browse/MDEV-18726): innodb buffer pool size not consistent with large pages
* [Revision #6b6fa3cdb1](https://github.com/MariaDB/server/commit/6b6fa3cdb1)\
  2019-03-18 14:08:43 +0200
  * [MDEV-18644](https://jira.mariadb.org/browse/MDEV-18644): Support full\_crc32 for page\_compressed
* [Revision #2151aed44d](https://github.com/MariaDB/server/commit/2151aed44d)\
  2019-03-18 13:10:28 +0200
  * Follow-up fix to [MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026): FIL\_SPACE\_FLAGS trump fil\_space\_t::flags
* [Revision #9c7299365f](https://github.com/MariaDB/server/commit/9c7299365f)\
  2019-03-18 09:37:32 +0530
  * Temporary disable ctype\_utf8mb4\_innodb and myisam test untill [MDEV-18953](https://jira.mariadb.org/browse/MDEV-18953) is fixed
* [Revision #3943fe5630](https://github.com/MariaDB/server/commit/3943fe5630)\
  2019-03-12 15:01:41 +0530
  * [MDEV-18888](https://jira.mariadb.org/browse/MDEV-18888) Server crashes in Item\_field::register\_field\_in\_read\_map upon... MODIFY COLUMN
* [Revision #8995f33c0b](https://github.com/MariaDB/server/commit/8995f33c0b)\
  2019-03-16 12:34:08 +0530
  * [MDEV-18889](https://jira.mariadb.org/browse/MDEV-18889) Long unique on virtual fields crashes server
* [Revision #09b2d37a32](https://github.com/MariaDB/server/commit/09b2d37a32)\
  2019-03-15 18:06:30 +0200
  * [MDEV-18941](https://jira.mariadb.org/browse/MDEV-18941): Temporarily record wrong result after [MDEV-18922](https://jira.mariadb.org/browse/MDEV-18922)
* [Revision #3dd477db70](https://github.com/MariaDB/server/commit/3dd477db70)\
  2019-03-15 18:05:47 +0200
  * [MDEV-18640](https://jira.mariadb.org/browse/MDEV-18640): Correct a result
* [Revision #a23657671e](https://github.com/MariaDB/server/commit/a23657671e)\
  2019-03-15 15:22:32 +0100
  * [MDEV-18666](https://jira.mariadb.org/browse/MDEV-18666) Fix MTR test galera\_sr\_kill\_all\_norecovery (#1229)
* [Revision #2e34a031f8](https://github.com/MariaDB/server/commit/2e34a031f8)\
  2019-03-15 14:27:29 +0530
  * [MDEV-18809](https://jira.mariadb.org/browse/MDEV-18809) Server crash in fields\_in\_hash\_keyinfo or Assertion \`key\_info->key\_part->field->flags & (1<< 30)' failed in setup\_keyinfo\_hash
* [Revision #ecf07300a2](https://github.com/MariaDB/server/commit/ecf07300a2)\
  2019-03-15 11:29:38 +0100
  * [MDEV-18915](https://jira.mariadb.org/browse/MDEV-18915) Re-record MTR test galera.galera\_many\_rows (#1228)
* [Revision #d27aa35eee](https://github.com/MariaDB/server/commit/d27aa35eee)\
  2019-03-15 10:20:32 +0200
  * Disable mysql-wsrep#198
* [Revision #050280ce8b](https://github.com/MariaDB/server/commit/050280ce8b)\
  2019-03-15 12:06:40 +0530
  * [MDEV-18922](https://jira.mariadb.org/browse/MDEV-18922) Alter on long unique varchar column makes result null
* [Revision #1ef50a34ec](https://github.com/MariaDB/server/commit/1ef50a34ec)\
  2019-03-15 07:09:13 +0200
  * 10.4 wsrep group commit fixes (#1224)
* [Revision #b234f81037](https://github.com/MariaDB/server/commit/b234f81037)\
  2019-03-14 19:33:13 -0700
  * [MDEV-18640](https://jira.mariadb.org/browse/MDEV-18640) TABLE::prune\_range\_rowid\_filters: Conditional jump or move depends on uninitialized value
* [Revision #e3ebeebe3a](https://github.com/MariaDB/server/commit/e3ebeebe3a)\
  2019-03-14 18:48:22 +0200
  * [MDEV-18450](https://jira.mariadb.org/browse/MDEV-18450) followup: fixing rpl\_shutdown\_wait. The test appeared to leave warning due to expectable full exit of IO threads. Fixed to ignore warnings at the final START SLAVEs.
* [Revision #e012d26680](https://github.com/MariaDB/server/commit/e012d26680)\
  2019-03-14 15:47:04 +0200
  * row\_undo(): Do not return an undefined value
* [Revision #ebd0eab5a3](https://github.com/MariaDB/server/commit/ebd0eab5a3)\
  2019-03-14 12:06:17 +0200
  * Removing warning from Aria recovery
* [Revision #e121a078bf](https://github.com/MariaDB/server/commit/e121a078bf)\
  2019-03-14 17:20:32 +1100
  * travis: use galera-4 in 10.4 branch (#1226)
* [Revision #7b33a6a1ea](https://github.com/MariaDB/server/commit/7b33a6a1ea)\
  2019-03-13 09:31:35 +0400
  * [MDEV-18876](https://jira.mariadb.org/browse/MDEV-18876) Assertion \`is\_valid\_time\_slow()' failed in Time::valid\_MYSQL\_TIME\_to\_valid\_value
* [Revision #62bfb2fe49](https://github.com/MariaDB/server/commit/62bfb2fe49)\
  2019-03-04 14:48:11 +0530
  * [MDEV-18800](https://jira.mariadb.org/browse/MDEV-18800) Server crash in instant\_alter\_column\_possible or Assertion... \`!pk->has\_virtual()' failed in instant\_alter\_column\_possible upon adding key
* [Revision #ecf323620b](https://github.com/MariaDB/server/commit/ecf323620b)\
  2019-03-04 14:08:46 +0530
  * Add test cases for [MDEV-18792](https://jira.mariadb.org/browse/MDEV-18792) [MDEV-18793](https://jira.mariadb.org/browse/MDEV-18793) [MDEV-18795](https://jira.mariadb.org/browse/MDEV-18795) [MDEV-18798](https://jira.mariadb.org/browse/MDEV-18798) [MDEV-18801](https://jira.mariadb.org/browse/MDEV-18801)
* [Revision #560598c9b2](https://github.com/MariaDB/server/commit/560598c9b2)\
  2019-03-03 17:56:48 +0530
  * [MDEV-18799](https://jira.mariadb.org/browse/MDEV-18799) Long unique does not work after failed alter table
* [Revision #c3cfcd5b5e](https://github.com/MariaDB/server/commit/c3cfcd5b5e)\
  2019-03-13 14:26:16 +0530
  * [MDEV-18810](https://jira.mariadb.org/browse/MDEV-18810): Optimizer trace typo: cumulateed\_index\_scan\_cost
* [Revision #52560b8b2d](https://github.com/MariaDB/server/commit/52560b8b2d)\
  2019-03-13 13:48:42 +0530
  * [MDEV-18905](https://jira.mariadb.org/browse/MDEV-18905): Remove the warning "'optimizer-trace' is MySQL 5.6 / 5.7 compatible option"
* [Revision #f9f625fb43](https://github.com/MariaDB/server/commit/f9f625fb43)\
  2019-03-03 16:35:13 +0530
  * [MDEV-18790](https://jira.mariadb.org/browse/MDEV-18790) Server crash in fields\_in\_hash\_keyinfo after unsuccessful... attempt to drop BLOB with long index
* [Revision #3568427d11](https://github.com/MariaDB/server/commit/3568427d11)\
  2019-03-07 08:12:26 +0400
  * [MDEV-18450](https://jira.mariadb.org/browse/MDEV-18450) Slaves wait shutdown
* Merge [Revision #e450527938](https://github.com/MariaDB/server/commit/e450527938) 2019-03-12 16:14:31 +0200 - Merge 10.3 into 10.4
* [Revision #6d68a3464e](https://github.com/MariaDB/server/commit/6d68a3464e)\
  2019-03-11 17:10:20 +0100
  * [MDEV-18701](https://jira.mariadb.org/browse/MDEV-18701): Wrong result from query that uses INTERSECT after UNION ALL
* Merge [Revision #58f3ff7175](https://github.com/MariaDB/server/commit/58f3ff7175) 2019-03-11 18:01:48 +0200 - Merge 10.3 into 10.4
* [Revision #038ffd2ee4](https://github.com/MariaDB/server/commit/038ffd2ee4)\
  2019-03-11 15:33:58 +0100
  * Merge pull request #1222 from codership/10.4-clear-sr-bugfix
* [Revision #15ccd3902e](https://github.com/MariaDB/server/commit/15ccd3902e)\
  2019-03-08 17:22:30 +0200
  * [MDEV-18837](https://jira.mariadb.org/browse/MDEV-18837) Fixed stored procedure wsrep error handling and MW-388
* [Revision #88d89ee0ba](https://github.com/MariaDB/server/commit/88d89ee0ba)\
  2019-03-09 19:48:11 +0400
  * Less abort\_loop references
* Merge [Revision #5a796f1f41](https://github.com/MariaDB/server/commit/5a796f1f41) 2019-03-08 22:11:37 +0200 - Merge 10.3 into 10.4
* [Revision #9512d3659c](https://github.com/MariaDB/server/commit/9512d3659c)\
  2019-03-08 15:52:13 +0100
  * Test failure: mysqltest: Result length mismatch
* Merge [Revision #5c6fdf420e](https://github.com/MariaDB/server/commit/5c6fdf420e) 2019-03-08 15:22:41 +0100 - Merge branch '10.3' into 10.4
* [Revision #f06868e56b](https://github.com/MariaDB/server/commit/f06868e56b)\
  2019-03-08 12:13:53 +0200
  * Unbreak the Windows build after d3e3bb77c2173ab200efdc8188c4d0a52127d247
* Merge [Revision #c67b306e4f](https://github.com/MariaDB/server/commit/c67b306e4f) 2019-03-08 11:19:48 +0200 - Merge 10.3 into 10.4
* [Revision #91d7e7b244](https://github.com/MariaDB/server/commit/91d7e7b244)\
  2019-03-08 10:18:20 +0200
  * Add C\_MODE\_START to aria\_backup.h
* [Revision #ec66320b0c](https://github.com/MariaDB/server/commit/ec66320b0c)\
  2019-03-08 10:17:56 +0200
  * Replace setting QPLAN\_ADMIN directly with prepare\_logs\_for\_admin\_command()
* [Revision #d3e3bb77c2](https://github.com/MariaDB/server/commit/d3e3bb77c2)\
  2019-03-08 10:05:30 +0200
  * Print value of 'protocol' option in --help
* [Revision #5f34513c2a](https://github.com/MariaDB/server/commit/5f34513c2a)\
  2019-03-06 17:36:30 +0400
  * [MDEV-18813](https://jira.mariadb.org/browse/MDEV-18813) PROCEDURE and anonymous blocks silently ignore FETCH GROUP NEXT ROW
* [Revision #a71d185a9a](https://github.com/MariaDB/server/commit/a71d185a9a)\
  2019-03-05 12:07:43 +0400
  * [MDEV-18813](https://jira.mariadb.org/browse/MDEV-18813) PROCEDURE and anonymous blocks silently ignore FETCH GROUP NEXT ROW
* Merge [Revision #aa4b2c1509](https://github.com/MariaDB/server/commit/aa4b2c1509) 2019-03-07 08:02:33 +0200 - Merge 10.3 into 10.4
* [Revision #32badae31f](https://github.com/MariaDB/server/commit/32badae31f)\
  2019-02-25 17:08:02 +0100
  * Fix for galera\_3nodes.galera\_var\_dirty\_reads2
* [Revision #7b9981fbdf](https://github.com/MariaDB/server/commit/7b9981fbdf)\
  2019-03-05 23:42:04 -0800
  * [MDEV-18816](https://jira.mariadb.org/browse/MDEV-18816) Assertion \`sel->quick' failed in JOIN::make\_range\_rowid\_filters
* [Revision #a36ac52f93](https://github.com/MariaDB/server/commit/a36ac52f93)\
  2019-03-06 15:31:50 +0100
  * [MDEV-18339](https://jira.mariadb.org/browse/MDEV-18339): ASAN heap-buffer-overflow in Item\_exists\_subselect::is\_top\_level\_item
* [Revision #2b711d231a](https://github.com/MariaDB/server/commit/2b711d231a)\
  2019-03-02 00:41:33 +0400
  * Adieu slave\_list
* [Revision #68c765d313](https://github.com/MariaDB/server/commit/68c765d313)\
  2019-03-01 22:36:29 +0400
  * Cleanup remnants of rpl\_recovery\_rank
* Merge [Revision #2a791c53ad](https://github.com/MariaDB/server/commit/2a791c53ad) 2019-03-06 09:00:52 +0200 - Merge 10.3 into 10.4
* [Revision #b5c72a843a](https://github.com/MariaDB/server/commit/b5c72a843a)\
  2019-03-04 12:17:13 +0100
  * [MDEV-18358](https://jira.mariadb.org/browse/MDEV-18358): Server crash when using SET STATEMENT max\_statement\_time
* [Revision #1bcb66c597](https://github.com/MariaDB/server/commit/1bcb66c597)\
  2019-03-04 10:04:41 +0400
  * [MDEV-18806](https://jira.mariadb.org/browse/MDEV-18806) Synchronize ALTER TABLE EXCHANGE PARTITION and PURGE grammar in sql\_yacc.yy and sql\_yacc\_ora.yy
* [Revision #e3e06722f0](https://github.com/MariaDB/server/commit/e3e06722f0)\
  2019-02-26 18:12:49 +0200
  * Fixes to galera\_gtid\_2\_cluster, galear\_sr\_mysqldump\_sst
* [Revision #a8ff4f243d](https://github.com/MariaDB/server/commit/a8ff4f243d)\
  2019-02-21 21:57:52 +0200
  * [MDEV-18631](https://jira.mariadb.org/browse/MDEV-18631) Fix streaming replication with wsrep\_gtid\_mode=ON
* [Revision #fa52846bc7](https://github.com/MariaDB/server/commit/fa52846bc7)\
  2019-02-21 16:02:57 +0200
  * [MDEV-18631](https://jira.mariadb.org/browse/MDEV-18631) Added MTR test
* [Revision #47b7ca629f](https://github.com/MariaDB/server/commit/47b7ca629f)\
  2019-03-03 07:20:15 +0400
  * [MDEV-18796](https://jira.mariadb.org/browse/MDEV-18796) Synchronize PS grammar between sql\_yacc.yy and sql\_yacc\_ora.yy
* [Revision #3b47587f41](https://github.com/MariaDB/server/commit/3b47587f41)\
  2019-03-01 23:55:55 +0400
  * [MDEV-18789](https://jira.mariadb.org/browse/MDEV-18789) Port "[MDEV-7773](https://jira.mariadb.org/browse/MDEV-7773) Aggregate stored functions" to sql\_yacc\_ora.yy
* [Revision #01d7727b76](https://github.com/MariaDB/server/commit/01d7727b76)\
  2019-03-01 17:02:58 +0400
  * [MDEV-18779](https://jira.mariadb.org/browse/MDEV-18779) Port sp\_suid implementation from sql\_yacc\_ora.yy to sql\_yacc.yy
* [Revision #5a0874449a](https://github.com/MariaDB/server/commit/5a0874449a)\
  2019-02-28 14:44:38 -0800
  * [MDEV-18755](https://jira.mariadb.org/browse/MDEV-18755) Assertion \`inited==INDEX' failed in handler::ha\_index\_read\_map
* [Revision #b10340998f](https://github.com/MariaDB/server/commit/b10340998f)\
  2019-02-27 23:32:02 +0100
  * [MDEV-18748](https://jira.mariadb.org/browse/MDEV-18748) REPLACE doesn't work with unique blobs on MyISAM table
* [Revision #9fd3e810e8](https://github.com/MariaDB/server/commit/9fd3e810e8)\
  2019-02-27 15:43:57 -0500
  * [MDEV-18747](https://jira.mariadb.org/browse/MDEV-18747) InnoDB: Failing assertion: table->get\_ref\_count() == 0 upon dropping temporary table with unique blob
* [Revision #304f0084ef](https://github.com/MariaDB/server/commit/304f0084ef)\
  2019-02-27 12:34:26 -0500
  * [MDEV-18720](https://jira.mariadb.org/browse/MDEV-18720) Assertion \`inited==NONE' failed in ha\_index\_init upon update on versioned table with key on blob
* [Revision #f78c0f6f00](https://github.com/MariaDB/server/commit/f78c0f6f00)\
  2019-02-27 07:35:46 -0500
  * [MDEV-18722](https://jira.mariadb.org/browse/MDEV-18722) Assertion \`templ->mysql\_null\_bit\_mask' failed in row\_sel\_store\_mysql\_rec upon modifying indexed column into blob
* [Revision #3f53515425](https://github.com/MariaDB/server/commit/3f53515425)\
  2019-02-26 22:55:39 -0500
  * [MDEV-18713](https://jira.mariadb.org/browse/MDEV-18713) Assertion \`strcmp(share->unique\_file\_name,filename) || share->last\_version' failed in test\_if\_reopen upon REPLACE into table with key on blob
* [Revision #20c89f9f37](https://github.com/MariaDB/server/commit/20c89f9f37)\
  2019-02-27 03:36:37 +0100
  * [MDEV-18712](https://jira.mariadb.org/browse/MDEV-18712) InnoDB indexes are inconsistent with what defined in .frm for table after rebuilding table with index on blob
* [Revision #5adf11250a](https://github.com/MariaDB/server/commit/5adf11250a)\
  2019-02-27 02:38:46 +0100
  * [MDEV-18707](https://jira.mariadb.org/browse/MDEV-18707) Server crash in my\_hash\_sort\_bin, ASAN heap-use-after-free in Field::is\_null, server hang, corrupted double-linked list
* [Revision #0477e80522](https://github.com/MariaDB/server/commit/0477e80522)\
  2019-02-25 00:46:48 +0530
  * Long Index is only allowed for unique keys not normal index.
* [Revision #8084eeaa66](https://github.com/MariaDB/server/commit/8084eeaa66)\
  2019-02-27 10:45:34 -0500
  * cleanup: set HA\_PART\_KEY\_SEG properly
* [Revision #593e869742](https://github.com/MariaDB/server/commit/593e869742)\
  2019-02-22 19:38:43 +0100
  * cleanup: reserve one keypart for LONG\_UNIQUE\_HASH\_FIELD
* [Revision #387b690eab](https://github.com/MariaDB/server/commit/387b690eab)\
  2019-02-22 18:58:14 +0100
  * cleanup: cosmetic fixes
* [Revision #72ee180512](https://github.com/MariaDB/server/commit/72ee180512)\
  2019-02-22 18:30:04 +0100
  * cleanup: set HA\_PART\_KEY\_SEG for HA\_KEY\_ALG\_LONG\_HASH prefix keys
* [Revision #09d29dfc76](https://github.com/MariaDB/server/commit/09d29dfc76)\
  2019-02-28 07:17:47 +0400
  * [MDEV-18767](https://jira.mariadb.org/browse/MDEV-18767) Port "[MDEV-16294](https://jira.mariadb.org/browse/MDEV-16294): INSTALL PLUGIN IF NOT EXISTS / UNINSTALL PLUGIN IF EXISTS" to sql\_yacc\_ora.yy
* [Revision #9bd47835d0](https://github.com/MariaDB/server/commit/9bd47835d0)\
  2019-02-23 14:53:27 -0800
  * [MDEV-18679](https://jira.mariadb.org/browse/MDEV-18679) Server crashes in JOIN::optimize
* [Revision #bba4e7f287](https://github.com/MariaDB/server/commit/bba4e7f287)\
  2019-02-22 22:28:24 +0100
  * [MDEV-18694](https://jira.mariadb.org/browse/MDEV-18694) : Do not call close\_connection() on active connections in server shutdown code.
* [Revision #794c6dd215](https://github.com/MariaDB/server/commit/794c6dd215)\
  2019-02-26 23:03:55 +0400
  * Yet another Adieu LOCK\_thread\_count
* [Revision #f92b7b1a27](https://github.com/MariaDB/server/commit/f92b7b1a27)\
  2019-02-26 22:44:38 +0400
  * Adieu LOCK\_thread\_count, COND\_thread\_count
* [Revision #785092ee23](https://github.com/MariaDB/server/commit/785092ee23)\
  2019-02-26 20:39:05 +0200
  * LOCK\_thread\_count and COND\_thread\_count removed from wsrep modules (#1197)
* [Revision #bb970dda77](https://github.com/MariaDB/server/commit/bb970dda77)\
  2019-02-25 15:35:00 +0200
  * [MDEV-18719](https://jira.mariadb.org/browse/MDEV-18719) Assertion (c.prtype ^ o->prtype) & ... failed on ALTER TABLE
* [Revision #201bd21e23](https://github.com/MariaDB/server/commit/201bd21e23)\
  2019-02-25 08:44:37 -0500
  * bump the VERSION
* [Revision #b25ad1bc47](https://github.com/MariaDB/server/commit/b25ad1bc47)\
  2019-02-21 21:44:44 +0400
  * [MDEV-18408](https://jira.mariadb.org/browse/MDEV-18408) Assertion \`0' failed in Item::val\_native\_result / Timestamp\_or\_zero\_datetime\_native\_null::Timestamp\_or\_zero\_datetime\_native\_null upon mysqld\_list\_fields after crash recovery
* [Revision #1ab2e7573a](https://github.com/MariaDB/server/commit/1ab2e7573a)\
  2019-02-20 13:22:04 +0200
  * Fixed and recorded galera\_sr.galera\_sr\_rollback\_statement
* [Revision #24be84384c](https://github.com/MariaDB/server/commit/24be84384c)\
  2019-02-19 22:56:39 +0200
  * Simplified Wsrep\_client\_service::interrupted()
* [Revision #6edfeb82fd](https://github.com/MariaDB/server/commit/6edfeb82fd)\
  2019-02-19 14:08:29 +0200
  * Fixes to streaming replication BF aborts
* [Revision #31b65d3dd2](https://github.com/MariaDB/server/commit/31b65d3dd2)\
  2018-12-19 17:08:51 +1100
  * stop covering\_keys from being set to the same thing twice

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
