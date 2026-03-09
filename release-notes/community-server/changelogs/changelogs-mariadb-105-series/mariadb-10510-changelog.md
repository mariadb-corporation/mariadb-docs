# MariaDB 10.5.10 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.10](https://downloads.mariadb.org/mariadb/10.5.10/)[Release Notes](../../old-releases/10.5/10.5.10.md)[Changelog](mariadb-10510-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 7 May 2021

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.10.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.19](../changelogs-mariadb-10-4-series/mariadb-10419-changelog.md)
* Merge [Revision #3f55c56951](https://github.com/MariaDB/server/commit/3f55c56951) 2021-05-05 23:17:20 +0300 - Merge branch bb-10.4-release into bb-10.5-release
* [Revision #ca1dc0789b](https://github.com/MariaDB/server/commit/ca1dc0789b)\
  2021-05-04 21:18:06 +0300
  * Follow-up for Deb: Stop depending on empty transitional package dh-systemd
* Merge [Revision #c6846757ac](https://github.com/MariaDB/server/commit/c6846757ac) 2021-05-03 14:34:48 +0300 - Merge 10.4 into 10.5
* [Revision #a61e556141](https://github.com/MariaDB/server/commit/a61e556141)\
  2021-05-02 09:06:27 +0200
  * new column store 5.5.2-2
* [Revision #29b0453653](https://github.com/MariaDB/server/commit/29b0453653)\
  2021-05-01 16:40:55 +0300
  * Updated wsrep.variables after wsrep lib update
* [Revision #25fa2a6831](https://github.com/MariaDB/server/commit/25fa2a6831)\
  2021-04-30 15:37:00 +0300
  * [MDEV-25507](https://jira.mariadb.org/browse/MDEV-25507) CHECK on encrypted Aria table complains about "Wrong LSN"
* [Revision #42cdc37ff9](https://github.com/MariaDB/server/commit/42cdc37ff9)\
  2021-04-19 22:54:45 +0900
  * [MDEV-22265](https://jira.mariadb.org/browse/MDEV-22265) Connect string character limit too small for full 64 character InnoDB table-name limit when using ad-hoc Spider server definitions.
* [Revision #e8b9d8d38c](https://github.com/MariaDB/server/commit/e8b9d8d38c)\
  2021-04-29 13:13:04 +0200
  * [MDEV-25530](https://jira.mariadb.org/browse/MDEV-25530) Error 1451 on slave: Cannot delete or update a parent row: a foreign key constraint fails
* [Revision #65e73b56d2](https://github.com/MariaDB/server/commit/65e73b56d2)\
  2021-04-28 18:50:13 +0200
  * [MDEV-24382](https://jira.mariadb.org/browse/MDEV-24382) Assertion in tdc\_remove\_table
* [Revision #3f4b7ed95a](https://github.com/MariaDB/server/commit/3f4b7ed95a)\
  2021-03-29 13:14:02 +0800
  * [MDEV-25093](https://jira.mariadb.org/browse/MDEV-25093): Adaptive flushing fails to kick in even if innodb\_adaptive\_flushing\_lwm is hit. (possible regression)
* Merge [Revision #559efad44e](https://github.com/MariaDB/server/commit/559efad44e) 2021-04-27 09:10:47 +0300 - Merge 10.4 into 10.5
* [Revision #dd07cfcecd](https://github.com/MariaDB/server/commit/dd07cfcecd)\
  2021-04-26 15:30:19 +0300
  * [MDEV-15756](https://jira.mariadb.org/browse/MDEV-15756): Remove some garbage output
* Merge [Revision #4725792bf3](https://github.com/MariaDB/server/commit/4725792bf3) 2021-04-25 12:04:45 +0300 - Merge 10.4 into 10.5
* [Revision #b8fad8c6bf](https://github.com/MariaDB/server/commit/b8fad8c6bf)\
  2021-04-21 12:51:39 +0200
  * [MDEV-25030](https://jira.mariadb.org/browse/MDEV-25030) Upgrade to 10.5.9 breaks root's ability to grant
* [Revision #a40f29ab19](https://github.com/MariaDB/server/commit/a40f29ab19)\
  2021-04-20 16:53:56 +0200
  * MYSQL\_MAINTAINER\_MODE fixes
* [Revision #1636db5443](https://github.com/MariaDB/server/commit/1636db5443)\
  2021-04-22 14:57:23 +0300
  * Revert "[MDEV-24589](https://jira.mariadb.org/browse/MDEV-24589) DROP TABLE is not crash-safe"
* [Revision #21973d0d8e](https://github.com/MariaDB/server/commit/21973d0d8e)\
  2021-04-02 00:33:13 +0100
  * [MDEV-22953](https://jira.mariadb.org/browse/MDEV-22953) main.flush\_read\_lock failed in buildbot with XAER\_NOTA: Unknown XID
* Merge [Revision #df33b719ca](https://github.com/MariaDB/server/commit/df33b719ca) 2021-04-22 08:25:40 +0300 - Merge 10.4 into 10.5
* [Revision #cbbca7edf6](https://github.com/MariaDB/server/commit/cbbca7edf6)\
  2021-04-22 08:13:57 +0300
  * [MDEV-25483](https://jira.mariadb.org/browse/MDEV-25483): Shutdown crash during innodb.innodb\_buffer\_pool\_resize\_temporary
* [Revision #9abc6fd73f](https://github.com/MariaDB/server/commit/9abc6fd73f)\
  2021-04-21 12:44:23 +0300
  * Cleanup: constexpr PFS\_table\_context::m\_word\_size
* [Revision #b59d07624c](https://github.com/MariaDB/server/commit/b59d07624c)\
  2021-04-21 12:34:54 +0300
  * WITH\_UBSAN: shift is too large for 32-bit int
* Merge [Revision #d104fe6f73](https://github.com/MariaDB/server/commit/d104fe6f73) 2021-04-21 10:27:13 +0300 - Merge 10.4 into 10.5
* Merge [Revision #80ed136e6d](https://github.com/MariaDB/server/commit/80ed136e6d) 2021-04-21 09:01:01 +0300 - Merge 10.4 into 10.5
* [Revision #675c22c065](https://github.com/MariaDB/server/commit/675c22c065)\
  2020-06-05 16:18:02 +0300
  * [MDEV-22757](https://jira.mariadb.org/browse/MDEV-22757) Assertion !binlog || exist\_hton\_without\_prepare' failed in MYSQL\_BIN\_LOG::unlog\_xa\_prepare
* [Revision #0620ccf3ea](https://github.com/MariaDB/server/commit/0620ccf3ea)\
  2021-04-19 14:31:57 +0300
  * Fixed failing test spider/bugfix.mdev\_22246
* [Revision #fce3e4ee8f](https://github.com/MariaDB/server/commit/fce3e4ee8f)\
  2021-04-16 18:21:52 +1000
  * Revert "Deb: Use build flag to enforce default charset as utf8mb4"
* [Revision #3f8df01194](https://github.com/MariaDB/server/commit/3f8df01194)\
  2021-04-15 11:40:43 +0300
  * [MDEV-25425](https://jira.mariadb.org/browse/MDEV-25425) Useless message "If the mysqld execution user is authorized page cleaner thread priority can be changed."
* [Revision #de746304c9](https://github.com/MariaDB/server/commit/de746304c9)\
  2020-12-20 20:52:51 +0200
  * Fix riscv64 build failure by linking correctly with pthread
* [Revision #f26e3259a1](https://github.com/MariaDB/server/commit/f26e3259a1)\
  2020-12-20 23:48:20 +0200
  * Deb: Use build flag to enforce default charset as utf8mb4
* [Revision #1715fef107](https://github.com/MariaDB/server/commit/1715fef107)\
  2021-04-14 10:17:16 +0200
  * Fix cross-compile to consider CMAKE\_CROSSCOMPILING\_EMULATOR
* [Revision #d1f2001ee6](https://github.com/MariaDB/server/commit/d1f2001ee6)\
  2021-04-14 15:23:00 +0300
  * fixup 6c3e860cbf36831c118f6ea183acbbeb3c889bed
* Merge [Revision #8d472f2b78](https://github.com/MariaDB/server/commit/8d472f2b78) 2021-04-14 12:48:48 +0300 - Merge 10.4 into 10.5
* [Revision #9a3cbc0541](https://github.com/MariaDB/server/commit/9a3cbc0541)\
  2021-04-13 20:23:46 +0100
  * mysqld: print status display subset of memory usage.
* Merge [Revision #6c3e860cbf](https://github.com/MariaDB/server/commit/6c3e860cbf) 2021-04-14 11:35:39 +0300 - Merge 10.4 into 10.5
* [Revision #9ff737b25e](https://github.com/MariaDB/server/commit/9ff737b25e)\
  2021-04-13 04:51:11 +0200
  * [MDEV-25307](https://jira.mariadb.org/browse/MDEV-25307): The value of the auto-increment variables changes during the test
* [Revision #58f184a4cb](https://github.com/MariaDB/server/commit/58f184a4cb)\
  2021-04-13 16:15:15 +0300
  * [MDEV-24745](https://jira.mariadb.org/browse/MDEV-24745) Generic CRC-32C computation wrongly uses SSE4.2 instructions
* [Revision #18a8290126](https://github.com/MariaDB/server/commit/18a8290126)\
  2021-03-09 21:30:30 +0100
  * [MDEV-23015](https://jira.mariadb.org/browse/MDEV-23015): mariadb-setpermission seems incompatible with DBI:MariaDB
* [Revision #9636b7cf55](https://github.com/MariaDB/server/commit/9636b7cf55)\
  2021-04-12 20:42:41 +0400
  * [MDEV-25393](https://jira.mariadb.org/browse/MDEV-25393) Fix mysql-test/lib/mtr\_cases.pm to search tests in submodules
* [Revision #0ba845a8c7](https://github.com/MariaDB/server/commit/0ba845a8c7)\
  2021-04-08 09:24:03 +0300
  * [MDEV-17913](https://jira.mariadb.org/browse/MDEV-17913) fixup: Correct a DBUG\_PRINT format string
* Merge [Revision #b4f09aa268](https://github.com/MariaDB/server/commit/b4f09aa268) 2021-04-08 08:15:11 +0300 - Merge 10.4 into 10.5
* Merge [Revision #2a7810759d](https://github.com/MariaDB/server/commit/2a7810759d) 2021-04-08 08:08:53 +0300 - [MDEV-22775](https://jira.mariadb.org/browse/MDEV-22775): Merge 10.4 into 10.5
* Merge [Revision #7b48da4d7e](https://github.com/MariaDB/server/commit/7b48da4d7e) 2021-04-08 07:47:49 +0300 - Merge 10.4 into 10.5
* [Revision #81258f1432](https://github.com/MariaDB/server/commit/81258f1432)\
  2021-04-02 22:00:36 +0300
  * [MDEV-17913](https://jira.mariadb.org/browse/MDEV-17913) Encrypted transactional Aria tables remain corrupt after crash recovery, automatic repairment does not work
* [Revision #7f75acc05c](https://github.com/MariaDB/server/commit/7f75acc05c)\
  2021-04-01 09:36:37 +0300
  * [MDEV-25313](https://jira.mariadb.org/browse/MDEV-25313): Assertion pending==log\_requests.start... failed
* [Revision #147a317e81](https://github.com/MariaDB/server/commit/147a317e81)\
  2021-03-31 14:11:56 +0300
  * [MDEV-25072](https://jira.mariadb.org/browse/MDEV-25072): Livelock due to innodb\_change\_buffering\_debug
* Merge [Revision #5eae8c2742](https://github.com/MariaDB/server/commit/5eae8c2742) 2021-03-31 11:05:21 +0300 - Merge 10.4 into 10.5
* [Revision #bf310b4cfb](https://github.com/MariaDB/server/commit/bf310b4cfb)\
  2021-03-30 16:17:10 +0300
  * [MDEV-25305](https://jira.mariadb.org/browse/MDEV-25305): MyRocks: Killing server during RESET MASTER can lose last transactions
* [Revision #5b678d9ea4](https://github.com/MariaDB/server/commit/5b678d9ea4)\
  2021-03-28 23:45:04 +0300
  * [MDEV-25251](https://jira.mariadb.org/browse/MDEV-25251): main.derived\_split\_innodb fails on ICC release binary
* [Revision #76d2846a71](https://github.com/MariaDB/server/commit/76d2846a71)\
  2021-03-30 15:57:14 +0800
  * [MDEV-24630](https://jira.mariadb.org/browse/MDEV-24630): MY\_RELAX\_CPU assembly instruction upgrade/research for memory barrier on ARM
* [Revision #8c2e3259c1](https://github.com/MariaDB/server/commit/8c2e3259c1)\
  2021-03-30 09:58:24 +0300
  * [MDEV-24302](https://jira.mariadb.org/browse/MDEV-24302) follow-up: RESET MASTER hangs
* [Revision #0df74a0197](https://github.com/MariaDB/server/commit/0df74a0197)\
  2021-03-11 22:04:22 +0200
  * Deb: Fix failing Salsa-CI by syncing fixes from downstream to upstream
* [Revision #5a4daa9099](https://github.com/MariaDB/server/commit/5a4daa9099)\
  2020-12-27 01:45:40 +0200
  * Deb: Add Breaks/Replaces
* [Revision #ab3777a3bf](https://github.com/MariaDB/server/commit/ab3777a3bf)\
  2020-12-26 20:35:52 +0200
  * Revert "[MDEV-23342](https://jira.mariadb.org/browse/MDEV-23342) MariaDB cannot be installed over MySQL 5.7.30 on Bionic anymore"
* [Revision #e8b7fceb82](https://github.com/MariaDB/server/commit/e8b7fceb82)\
  2021-03-29 15:16:23 +0300
  * [MDEV-24302](https://jira.mariadb.org/browse/MDEV-24302): RESET MASTER hangs
* [Revision #8e2d69f7b8](https://github.com/MariaDB/server/commit/8e2d69f7b8)\
  2021-03-28 18:43:14 +0300
  * Fixed access to undefined memory
* Merge [Revision #80459bcbd4](https://github.com/MariaDB/server/commit/80459bcbd4) 2021-03-27 17:37:42 +0200 - Merge 10.4 into 10.5
* [Revision #2e67b9f665](https://github.com/MariaDB/server/commit/2e67b9f665)\
  2021-03-26 09:58:52 +0200
  * [MDEV-25265](https://jira.mariadb.org/browse/MDEV-25265): ALTER TABLE...IMPORT TABLESPACE fails after DROP INDEX
* [Revision #bcb9ca4105](https://github.com/MariaDB/server/commit/bcb9ca4105)\
  2021-03-23 18:16:20 +1100
  * MEM\_CHECK\_DEFINED: replace HAVE\_valgrind
* [Revision #e731a28394](https://github.com/MariaDB/server/commit/e731a28394)\
  2021-03-23 16:20:15 +0200
  * [MDEV-24589](https://jira.mariadb.org/browse/MDEV-24589) DROP TABLE is not crash-safe
* [Revision #8b11550356](https://github.com/MariaDB/server/commit/8b11550356)\
  2021-03-23 14:58:04 +0200
  * fixup cebf9ee2040195a61fbed32d06cc2e335e9f8dfd
* [Revision #8f23aab068](https://github.com/MariaDB/server/commit/8f23aab068)\
  2021-03-23 14:47:04 +0200
  * [MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528) fixup: Remove dict\_table\_open\_on\_index\_id()
* [Revision #df931d888f](https://github.com/MariaDB/server/commit/df931d888f)\
  2021-03-23 12:37:55 +0700
  * fixed typo in postinst script
* [Revision #d902b53cfe](https://github.com/MariaDB/server/commit/d902b53cfe)\
  2021-03-22 17:53:39 +0200
  * Fixed wrong usage strlen(), should be sizeof()
* [Revision #cebf9ee204](https://github.com/MariaDB/server/commit/cebf9ee204)\
  2020-12-20 21:07:38 +0200
  * Fix various spelling errors still found in code
* [Revision #e7ddf46632](https://github.com/MariaDB/server/commit/e7ddf46632)\
  2021-03-20 13:47:05 +0200
  * [MDEV-25211](https://jira.mariadb.org/browse/MDEV-25211) Remove useless counter Innodb\_buffered\_aio\_submitted
* Merge [Revision #8570a6a093](https://github.com/MariaDB/server/commit/8570a6a093) 2021-03-20 13:34:38 +0200 - Merge 10.4 into 10.5
* [Revision #1bacab8ab9](https://github.com/MariaDB/server/commit/1bacab8ab9)\
  2021-03-19 09:31:27 +0000
  * mariadb-backup little FreeBSD update support.
* [Revision #8bdffb3750](https://github.com/MariaDB/server/commit/8bdffb3750)\
  2021-03-19 15:44:07 +0100
  * fix for tests from engines/funcs
* [Revision #233c09138f](https://github.com/MariaDB/server/commit/233c09138f)\
  2021-03-19 13:10:12 +0200
  * Disable crashing Galera tests: [MDEV-18534](https://jira.mariadb.org/browse/MDEV-18534), [MDEV-24485](https://jira.mariadb.org/browse/MDEV-24485)
* Merge [Revision #be881ec457](https://github.com/MariaDB/server/commit/be881ec457) 2021-03-19 13:06:31 +0200 - Merge 10.4 into 10.5
* Merge [Revision #190a8312f5](https://github.com/MariaDB/server/commit/190a8312f5) 2021-03-18 15:07:01 +0200 - Merge 10.4 into 10.5
* [Revision #5dbea46cfd](https://github.com/MariaDB/server/commit/5dbea46cfd)\
  2021-03-16 15:37:14 +1100
  * crc32c: Fix AIX compulation - ALIGN defined
* [Revision #60d1461a28](https://github.com/MariaDB/server/commit/60d1461a28)\
  2021-02-26 16:22:24 +0100
  * CRC32 on AIX
* [Revision #9c7bd4f283](https://github.com/MariaDB/server/commit/9c7bd4f283)\
  2021-03-17 16:51:56 +0300
  * [MDEV-25069](https://jira.mariadb.org/browse/MDEV-25069): Assertion \`root->weight >= ...' failed in SEL\_ARG::tree\_delete #2
* [Revision #7e3806ce24](https://github.com/MariaDB/server/commit/7e3806ce24)\
  2020-12-21 20:42:26 +0200
  * Deb: Sync updates to debconf templates and translations from downstream
* [Revision #bac931303d](https://github.com/MariaDB/server/commit/bac931303d)\
  2020-12-20 23:00:00 +0200
  * Deb: Add Finnish and Vietnamese debconf translations
* [Revision #dfa6fba959](https://github.com/MariaDB/server/commit/dfa6fba959)\
  2021-03-17 10:35:04 +0100
  * Skip tests that dump thread\_stack, for ASAN
* [Revision #825c0e2abe](https://github.com/MariaDB/server/commit/825c0e2abe)\
  2021-03-16 12:03:41 +0100
  * [MDEV-24601](https://jira.mariadb.org/browse/MDEV-24601): INFORMATION\_SCHEMA doesn't differentiate between column and table-level CHECK constraints
* [Revision #8cbada87f0](https://github.com/MariaDB/server/commit/8cbada87f0)\
  2021-03-15 16:11:23 +0300
  * [MDEV-24184](https://jira.mariadb.org/browse/MDEV-24184) InnoDB RENAME TABLE recovery failure if names are reused
* [Revision #031b3dfc22](https://github.com/MariaDB/server/commit/031b3dfc22)\
  2021-03-12 08:43:37 +0100
  * [MDEV-25123](https://jira.mariadb.org/browse/MDEV-25123) support MSVC ASAN
* [Revision #4c2b6be38e](https://github.com/MariaDB/server/commit/4c2b6be38e)\
  2021-03-11 21:43:43 +0200
  * One more try: Fix -Wconversion on GCC 4 to 9
* [Revision #abe25c31a6](https://github.com/MariaDB/server/commit/abe25c31a6)\
  2021-03-11 21:02:15 +0200
  * After-merge fix: -Wconversion in GCC 4 to 9
* Merge [Revision #a4b7232b2c](https://github.com/MariaDB/server/commit/a4b7232b2c) 2021-03-11 20:09:34 +0200 - Merge 10.4 into 10.5
* [Revision #a8650b64ed](https://github.com/MariaDB/server/commit/a8650b64ed)\
  2021-03-10 19:33:09 +0200
  * [MDEV-25110](https://jira.mariadb.org/browse/MDEV-25110) \[FATAL] InnoDB: Trying to write ... outside the bounds
* [Revision #549a70d7f0](https://github.com/MariaDB/server/commit/549a70d7f0)\
  2021-03-09 18:03:31 +0200
  * [MDEV-25031](https://jira.mariadb.org/browse/MDEV-25031) Not applying INSERT\_\*\_REDUNDANT due to corruption on page
* [Revision #a6cd4612a9](https://github.com/MariaDB/server/commit/a6cd4612a9)\
  2021-03-10 16:02:55 +0000
  * connect storage, little compile issues fix proposal.
* [Revision #f11b60879b](https://github.com/MariaDB/server/commit/f11b60879b)\
  2021-02-23 16:21:30 +0800
  * [MDEV-24949](https://jira.mariadb.org/browse/MDEV-24949): Enabling idle flushing (possible regression from [MDEV-23855](https://jira.mariadb.org/browse/MDEV-23855))
* [Revision #1799caa3a1](https://github.com/MariaDB/server/commit/1799caa3a1)\
  2021-03-10 17:27:01 +0200
  * [MDEV-24422](https://jira.mariadb.org/browse/MDEV-24422) Server crashes in ha\_connect::GetRealType upon ALTER TABLE
* [Revision #322129dfb4](https://github.com/MariaDB/server/commit/322129dfb4)\
  2021-03-10 10:31:22 +0200
  * Skip mysql\_json\_mysql\_upgrade if plugin is not built
* [Revision #bba6c38630](https://github.com/MariaDB/server/commit/bba6c38630)\
  2021-03-09 11:27:47 +0200
  * Deb: Sync downstream changes upstream
* [Revision #baddbaa0e3](https://github.com/MariaDB/server/commit/baddbaa0e3)\
  2021-03-09 11:44:29 +0100
  * fixup 449871458b49f224b27b26858784ef5408353f1b
* [Revision #449871458b](https://github.com/MariaDB/server/commit/449871458b)\
  2021-03-08 18:00:55 +0100
  * Fix Windows clang build with newest cmake
* [Revision #d2ddf82a0e](https://github.com/MariaDB/server/commit/d2ddf82a0e)\
  2021-03-08 11:39:09 +0200
  * After-merge fix: GCC -Wconversion
* Merge [Revision #a5d3c1c819](https://github.com/MariaDB/server/commit/a5d3c1c819) 2021-03-08 10:16:20 +0200 - Merge 10.4 into 10.5
* [Revision #f6cb9e6e2d](https://github.com/MariaDB/server/commit/f6cb9e6e2d)\
  2021-03-05 12:59:07 +0200
  * Cleanup: add override qualifiers to item.h
* [Revision #e5e0e519f4](https://github.com/MariaDB/server/commit/e5e0e519f4)\
  2021-03-05 12:55:46 +0200
  * [MDEV-24600](https://jira.mariadb.org/browse/MDEV-24600) fixup: Remove unused trx\_register\_for\_2pc()
* Merge [Revision #10d544aa7b](https://github.com/MariaDB/server/commit/10d544aa7b) 2021-03-05 12:54:43 +0200 - Merge 10.4 into 10.5
* [Revision #aa4f76bed7](https://github.com/MariaDB/server/commit/aa4f76bed7)\
  2021-03-01 23:07:12 +0530
  * [MDEV-25018](https://jira.mariadb.org/browse/MDEV-25018) \[FATAL] InnoDB: Unable to read page (of a dropped tablespace)
* [Revision #4b166ca901](https://github.com/MariaDB/server/commit/4b166ca901)\
  2021-02-25 20:51:30 +0530
  * [MDEV-24863](https://jira.mariadb.org/browse/MDEV-24863) AHI entries mismatch with the index while reloading the evicted tables.
* [Revision #01b44c054d](https://github.com/MariaDB/server/commit/01b44c054d)\
  2021-03-02 11:51:22 +0200
  * [MDEV-25026](https://jira.mariadb.org/browse/MDEV-25026) Various code paths are accessing freed pages
* [Revision #1f1f61a9de](https://github.com/MariaDB/server/commit/1f1f61a9de)\
  2021-03-01 16:53:09 +0100
  * [MDEV-24858](https://jira.mariadb.org/browse/MDEV-24858) SIGABRT in DbugExit from my\_malloc in Query\_cache::init\_cache Regression
* [Revision #6976bb94b4](https://github.com/MariaDB/server/commit/6976bb94b4)\
  2021-02-20 15:13:12 +0000
  * [MDEV-24858](https://jira.mariadb.org/browse/MDEV-24858) SIGABRT in DbugExit from my\_malloc in Query\_cache::init\_cache Regression
* [Revision #8d714db622](https://github.com/MariaDB/server/commit/8d714db622)\
  2021-02-26 19:02:26 +0530
  * [MDEV-24997](https://jira.mariadb.org/browse/MDEV-24997) Assertion mtr->is\_named\_space(page\_id.space()) in ibuf0ibuf.cc:624
* Merge [Revision #1696e4df3f](https://github.com/MariaDB/server/commit/1696e4df3f) 2021-02-26 13:25:04 +1100 - Merge remote-tracking branch 10.4 into 10.5
* Merge [Revision #86d60fc9e7](https://github.com/MariaDB/server/commit/86d60fc9e7) 2021-02-25 20:05:35 +1100 - Merge remote-tracking branch 'origin/10.4' into 10.5
* [Revision #e0ba68ba34](https://github.com/MariaDB/server/commit/e0ba68ba34)\
  2021-02-15 12:31:31 +1100
  * [MDEV-23510](https://jira.mariadb.org/browse/MDEV-23510): arm64 lf\_hash alignment of pointers
* [Revision #cea03285ec](https://github.com/MariaDB/server/commit/cea03285ec)\
  2021-02-24 13:30:35 +0200
  * [MDEV-24967](https://jira.mariadb.org/browse/MDEV-24967) : Signal 11 on ha\_innodb.cc::bg\_wsrep\_kill\_trx line 18611
* [Revision #f83e2ecc50](https://github.com/MariaDB/server/commit/f83e2ecc50)\
  2021-02-23 23:38:57 +0300
  * [MDEV-24953](https://jira.mariadb.org/browse/MDEV-24953): 10.5.9 crashes with large IN() list
* Merge [Revision #f159061510](https://github.com/MariaDB/server/commit/f159061510) 2021-02-24 08:54:44 +0200 - Merge 10.4 into 10.5
* Merge [Revision #f33e57a9e6](https://github.com/MariaDB/server/commit/f33e57a9e6) 2021-02-23 13:01:27 +0100 - Merge branch '10.4' into 10.5
* Merge [Revision #1a0526e2f2](https://github.com/MariaDB/server/commit/1a0526e2f2) 2021-02-23 09:27:02 +0100 - Merge branch 'bb-10.5-release' into 10.5
* [Revision #85bec9d691](https://github.com/MariaDB/server/commit/85bec9d691)\
  2021-02-22 09:40:30 -0500
  * bump the VERSION
* Merge [Revision #16388f393c](https://github.com/MariaDB/server/commit/16388f393c) 2021-02-17 16:19:49 +0200 - Merge mariadb-10.5.9
* [Revision #d82386b6b9](https://github.com/MariaDB/server/commit/d82386b6b9)\
  2021-02-17 16:18:55 +0200
  * [MDEV-24848](https://jira.mariadb.org/browse/MDEV-24848) Assertion rlen\<llen failed when applying MEMSET
* [Revision #fc5e03f093](https://github.com/MariaDB/server/commit/fc5e03f093)\
  2021-02-15 20:21:12 +0200
  * Ignore reporting in thd\_progress\_report() if we cannot lock LOCK\_thd\_data
* [Revision #8eaf4bc5ec](https://github.com/MariaDB/server/commit/8eaf4bc5ec)\
  2021-02-15 13:57:35 +0300
  * Comment on assertion in row\_rename\_table\_for\_mysql()
* [Revision #34c654024c](https://github.com/MariaDB/server/commit/34c654024c)\
  2021-02-15 01:33:06 +0200
  * [MDEV-24855](https://jira.mariadb.org/browse/MDEV-24855) ER\_CRASHED\_ON\_USAGE or Assertion \`length <= column->length'
* [Revision #b3df194e31](https://github.com/MariaDB/server/commit/b3df194e31)\
  2021-02-12 20:40:25 +0200
  * [MDEV-24833](https://jira.mariadb.org/browse/MDEV-24833) : Signal 11 on wsrep\_can\_run\_in\_toi at wsrep\_mysqld.cc:1994
* [Revision #7fb528d722](https://github.com/MariaDB/server/commit/7fb528d722)\
  2021-02-05 14:48:40 +0200
  * Deb: Remove build depencency libreadline-gplv2-dev no longer available
* [Revision #2405752855](https://github.com/MariaDB/server/commit/2405752855)\
  2021-02-10 12:14:56 +0200
  * Salsa-CI: Install readline from Buster as it was removed from Sid
* [Revision #c7edbe5bb1](https://github.com/MariaDB/server/commit/c7edbe5bb1)\
  2021-02-11 12:45:24 +1100
  * [MDEV-24366](https://jira.mariadb.org/browse/MDEV-24366): s3 test postfix - use default for S3\_BUCKET

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
