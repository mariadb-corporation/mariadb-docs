# MariaDB 10.4.34 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.4/10.4.34.md)[Changelog](mariadb-10-4-34-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.4.34/)

**Release date:** 16 May 2024

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.34.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.39](../changelogs-mariadb-10-3-series/mariadb-10-3-39-changelog.md)
* [Revision #16394f1aa1](https://github.com/MariaDB/server/commit/16394f1aa1)\
  2024-05-06 16:14:11 +0200
  * update C/C 3.1
* [Revision #f378e76434](https://github.com/MariaDB/server/commit/f378e76434)\
  2024-04-30 14:16:08 +0530
  * [MDEV-33980](https://jira.mariadb.org/browse/MDEV-33980) mariadb-backup --backup is missing retry logic for undo tablespaces
* [Revision #a586b6dbc8](https://github.com/MariaDB/server/commit/a586b6dbc8)\
  2024-04-29 16:42:26 +0530
  * [MDEV-22855](https://jira.mariadb.org/browse/MDEV-22855) Assertion \`!field->prefix\_len || field->fixed\_len == field->prefix\_len' failed in btr\_node\_ptr\_max\_size
* [Revision #3f2a5b28c6](https://github.com/MariaDB/server/commit/3f2a5b28c6)\
  2024-04-29 16:42:46 +1000
  * [MDEV-34003](https://jira.mariadb.org/browse/MDEV-34003) Add testcase spider/bugfix.mdev\_34003
* [Revision #136358036d](https://github.com/MariaDB/server/commit/136358036d)\
  2024-04-27 18:40:58 +0200
  * [MDEV-18590](https://jira.mariadb.org/browse/MDEV-18590): galera.versioning\_trx\_id: Test failure: mysqltest: Result content mismatch
* [Revision #1532f12058](https://github.com/MariaDB/server/commit/1532f12058)\
  2024-04-12 15:40:11 +0300
  * [MDEV-33898](https://jira.mariadb.org/browse/MDEV-33898) : Galera test failure on galera.MW-369
* [Revision #288ea9e146](https://github.com/MariaDB/server/commit/288ea9e146)\
  2024-04-25 00:13:02 +0200
  * galera SST scripts: parsing CN in certificates
* Merge [Revision #ee59ca7ff1](https://github.com/MariaDB/server/commit/ee59ca7ff1) 2024-04-26 13:50:03 +0200 - Merge branch 'merge-zlib' (1.3.1) into 10.4
* [Revision #5aff13b65c](https://github.com/MariaDB/server/commit/5aff13b65c)\
  2024-04-26 13:18:51 +0200
  * zlib 1.3.1
* [Revision #45846bacb3](https://github.com/MariaDB/server/commit/45846bacb3)\
  2024-04-26 13:02:47 +0200
  * v5.7.0-stable
* [Revision #62287320d4](https://github.com/MariaDB/server/commit/62287320d4)\
  2024-04-23 11:37:11 +0200
  * [MDEV-33790](https://jira.mariadb.org/browse/MDEV-33790) Incorrect DEFAULT expression evaluated in UPDATE
* [Revision #77d5104fee](https://github.com/MariaDB/server/commit/77d5104fee)\
  2024-04-25 12:58:32 +0300
  * Remove a bogus workaround for old GCC
* [Revision #0c55d854fe](https://github.com/MariaDB/server/commit/0c55d854fe)\
  2024-04-24 13:13:57 +0530
  * [MDEV-33334](https://jira.mariadb.org/browse/MDEV-33334) mariadb-backup fails to preserve innodb\_encrypt\_tables
* [Revision #a2fee2da0b](https://github.com/MariaDB/server/commit/a2fee2da0b)\
  2024-04-18 15:41:30 +0300
  * [MDEV-33928](https://jira.mariadb.org/browse/MDEV-33928) : Assertion failure on wsrep\_thd\_is\_aborting
* [Revision #4aeba2590b](https://github.com/MariaDB/server/commit/4aeba2590b)\
  2024-04-12 09:15:53 +0300
  * [MDEV-33895](https://jira.mariadb.org/browse/MDEV-33895) : Galera test failure on galera\_sr.[MDEV-25718](https://jira.mariadb.org/browse/MDEV-25718)
* [Revision #50998a6c6f](https://github.com/MariaDB/server/commit/50998a6c6f)\
  2024-04-15 16:39:01 +0200
  * [MDEV-33861](https://jira.mariadb.org/browse/MDEV-33861) main.query\_cache fails with embedded after enabling WITH\_PROTECT\_STATEMENT\_MEMROOT
* [Revision #051a1fa0e9](https://github.com/MariaDB/server/commit/051a1fa0e9)\
  2024-03-27 11:15:25 +1100
  * [MDEV-33777](https://jira.mariadb.org/browse/MDEV-33777) Spider: Correct checks for show index column numbers
* [Revision #18b93d6eb0](https://github.com/MariaDB/server/commit/18b93d6eb0)\
  2024-03-20 17:20:39 +1100
  * [MDEV-28993](https://jira.mariadb.org/browse/MDEV-28993) Spider: Push down CASE statement
* [Revision #99dc0f030f](https://github.com/MariaDB/server/commit/99dc0f030f)\
  2024-03-20 17:23:49 +1100
  * [MDEV-28993](https://jira.mariadb.org/browse/MDEV-28993) spider: revert removal of ITEM\_FUNC\_CASE\_PARAMS\_ARE\_PUBLIC
* [Revision #d7fc975cfe](https://github.com/MariaDB/server/commit/d7fc975cfe)\
  2024-04-02 20:45:29 +0300
  * [MDEV-33802](https://jira.mariadb.org/browse/MDEV-33802) Weird read view after ROLLBACK of other transactions.
* [Revision #d824977598](https://github.com/MariaDB/server/commit/d824977598)\
  2024-04-10 09:47:44 +0300
  * [MDEV-33512](https://jira.mariadb.org/browse/MDEV-33512) Corrupted table after IMPORT TABLESPACE and restart
* [Revision #662bb176b4](https://github.com/MariaDB/server/commit/662bb176b4)\
  2024-03-13 13:11:15 +1100
  * [MDEV-33661](https://jira.mariadb.org/browse/MDEV-33661) MENT-1591 Keep spider in memory until exit in ASAN builds
* [Revision #a73c3f1077](https://github.com/MariaDB/server/commit/a73c3f1077)\
  2024-04-08 16:35:21 +1000
  * [MDEV-21007](https://jira.mariadb.org/browse/MDEV-21007) Do not assert auto\_increment\_value unless all parts open
* [Revision #f9e0ebeca4](https://github.com/MariaDB/server/commit/f9e0ebeca4)\
  2024-04-08 14:28:23 +1000
  * [MDEV-33742](https://jira.mariadb.org/browse/MDEV-33742) Do not create group by handler when all tables are constant
* [Revision #e865ef6a04](https://github.com/MariaDB/server/commit/e865ef6a04)\
  2024-03-25 14:06:27 +1100
  * [MDEV-33742](https://jira.mariadb.org/browse/MDEV-33742) Remove macro PARTITION\_HAS\_GET\_CHILD\_HANDLERS
* [Revision #860c1ca9ad](https://github.com/MariaDB/server/commit/860c1ca9ad)\
  2024-03-18 13:11:49 +1100
  * [MDEV-33679](https://jira.mariadb.org/browse/MDEV-33679) Spider group by handler: skip on multiple equalities
* [Revision #9c93d41ad7](https://github.com/MariaDB/server/commit/9c93d41ad7)\
  2024-03-20 14:03:52 +1100
  * [MDEV-33728](https://jira.mariadb.org/browse/MDEV-33728) spider: remove use of MYSQL\_VERSION\_ID and MARIADB\_BASE\_VERSION
* [Revision #44c88faeca](https://github.com/MariaDB/server/commit/44c88faeca)\
  2024-03-20 10:36:25 +1100
  * [MDEV-28992](https://jira.mariadb.org/browse/MDEV-28992) Spider group by handler: Push down TIMESTAMPDIFF function
* [Revision #11fe2ee0af](https://github.com/MariaDB/server/commit/11fe2ee0af)\
  2024-02-21 14:17:34 +1100
  * [MDEV-33493](https://jira.mariadb.org/browse/MDEV-33493) Spider: Make a symlink result file a normal file
* [Revision #504925c416](https://github.com/MariaDB/server/commit/504925c416)\
  2024-02-19 15:12:16 +1100
  * [MDEV-33434](https://jira.mariadb.org/browse/MDEV-33434) spider direct sql: Check length before memcpy
* [Revision #9b5d711ac3](https://github.com/MariaDB/server/commit/9b5d711ac3)\
  2024-04-05 16:09:56 +0530
  * [MDEV-20094](https://jira.mariadb.org/browse/MDEV-20094) InnoDB blob allocation allocates extra extents
* [Revision #8cc36fb743](https://github.com/MariaDB/server/commit/8cc36fb743)\
  2024-03-20 13:09:12 +0300
  * [MDEV-21102](https://jira.mariadb.org/browse/MDEV-21102): Server crashes in JOIN\_CACHE::write\_record\_data upon EXPLAIN with subqueries
* [Revision #a618ff2b1c](https://github.com/MariaDB/server/commit/a618ff2b1c)\
  2024-01-10 14:34:12 +0100
  * [MDEV-33216](https://jira.mariadb.org/browse/MDEV-33216) stack-use-after-return in Wsrep\_schema\_impl::open\_table()
* [Revision #c81139357a](https://github.com/MariaDB/server/commit/c81139357a)\
  2024-03-28 11:48:32 +0700
  * [MDEV-14959](https://jira.mariadb.org/browse/MDEV-14959): the follow-up patch to turn on the option -DWITH\_PROTECT\_STATEMENT\_MEMROOT by default
* [Revision #e6d12bb459](https://github.com/MariaDB/server/commit/e6d12bb459)\
  2024-03-13 13:11:07 +1100
  * [MDEV-33661](https://jira.mariadb.org/browse/MDEV-33661) MENT-1591 Fix spider/bugfix.mdev\_28856 because of [MDEV-29718](https://jira.mariadb.org/browse/MDEV-29718).
* [Revision #0b627377a9](https://github.com/MariaDB/server/commit/0b627377a9)\
  2024-03-13 13:10:47 +1100
  * [MDEV-33661](https://jira.mariadb.org/browse/MDEV-33661) MENT-1591 Documenting spider\_mon\_table\_cache and friends.
* [Revision #fa1ae367f1](https://github.com/MariaDB/server/commit/fa1ae367f1)\
  2024-03-27 01:23:42 +0100
  * galera: wsrep-lib submodule update
* [Revision #c71dc39529](https://github.com/MariaDB/server/commit/c71dc39529)\
  2022-11-24 14:47:18 +0100
  * [MDEV-26499](https://jira.mariadb.org/browse/MDEV-26499) Fix error "mysql\_shutdown failed" during MTR tests
* [Revision #db0b9ec37b](https://github.com/MariaDB/server/commit/db0b9ec37b)\
  2024-03-27 11:40:41 +1100
  * [MDEV-33584](https://jira.mariadb.org/browse/MDEV-33584) Use the default SQL\_MODE for spider init queries
* [Revision #9d34939c6e](https://github.com/MariaDB/server/commit/9d34939c6e)\
  2024-02-20 11:20:21 +1100
  * [MDEV-33494](https://jira.mariadb.org/browse/MDEV-33494) fix spider init with no\_zero\_date global sql mode
* [Revision #bf49e7cfc7](https://github.com/MariaDB/server/commit/bf49e7cfc7)\
  2024-03-26 15:29:33 +0530
  * [MDEV-33770](https://jira.mariadb.org/browse/MDEV-33770) Alter operation hangs when encryption thread works on the same tablespace
* [Revision #d695e2de54](https://github.com/MariaDB/server/commit/d695e2de54)\
  2024-03-26 13:10:16 +0100
  * [MDEV-33506](https://jira.mariadb.org/browse/MDEV-33506) Show original IP in the "aborted" message.
* [Revision #ed027d65f1](https://github.com/MariaDB/server/commit/ed027d65f1)\
  2024-03-22 14:04:46 +0300
  * [MDEV-33747](https://jira.mariadb.org/browse/MDEV-33747): Optimization of (SELECT) IN (SELECT ...) executes subquery at prepare stage
* [Revision #17573166c4](https://github.com/MariaDB/server/commit/17573166c4)\
  2024-03-26 10:47:50 +0200
  * [MDEV-22742](https://jira.mariadb.org/browse/MDEV-22742) fixup: Remove a suppression
* [Revision #9b7c2c6b00](https://github.com/MariaDB/server/commit/9b7c2c6b00)\
  2024-03-26 10:47:43 +0200
  * [MDEV-33220](https://jira.mariadb.org/browse/MDEV-33220) fixup: Remove some initialization
* [Revision #e0c8165487](https://github.com/MariaDB/server/commit/e0c8165487)\
  2024-03-21 14:03:19 +0100
  * [MDEV-33509](https://jira.mariadb.org/browse/MDEV-33509) Failed to apply write set with flags=(rollback|pa\_unsafe)
* [Revision #ef9cdacf51](https://github.com/MariaDB/server/commit/ef9cdacf51)\
  2024-03-21 17:17:53 +1100
  * [MDEV-33220](https://jira.mariadb.org/browse/MDEV-33220) Fix -wmaybe-uninitialized warnings for g++-13
* [Revision #2250b42f52](https://github.com/MariaDB/server/commit/2250b42f52)\
  2024-03-21 16:01:29 +0200
  * Fix heap-use-after-free in fts\_free()
* [Revision #5d85749953](https://github.com/MariaDB/server/commit/5d85749953)\
  2024-03-21 14:20:33 +0200
  * Cleanup: Remove unused DYN\_BLOCK\_FULL\_FLAG
* [Revision #59e7289b6c](https://github.com/MariaDB/server/commit/59e7289b6c)\
  2024-03-19 08:10:42 +0200
  * Fix g++-14 -Wmaybe-uninitialized
* [Revision #2a8c4ccf2e](https://github.com/MariaDB/server/commit/2a8c4ccf2e)\
  2024-03-19 08:09:31 +0200
  * Fix g++-14 -Wtemplate-id-cdtor
* [Revision #83a87da430](https://github.com/MariaDB/server/commit/83a87da430)\
  2024-03-19 08:08:18 +0200
  * Fix g++-14 -Wmaybe-uninitialized
* [Revision #2ba4248334](https://github.com/MariaDB/server/commit/2ba4248334)\
  2024-03-19 08:07:41 +0200
  * Fix g++-14 -Wcalloc-transposed-args
* [Revision #af85e2ba19](https://github.com/MariaDB/server/commit/af85e2ba19)\
  2024-03-18 22:07:32 +0100
  * MTR, Windows - remove --verbose-restart output on buildbot run
* [Revision #5abf0fea51](https://github.com/MariaDB/server/commit/5abf0fea51)\
  2024-01-26 14:37:26 +0100
  * mtr - synchronize output between different threads on Windows.
* [Revision #d912a6369c](https://github.com/MariaDB/server/commit/d912a6369c)\
  2024-03-14 18:59:47 +0530
  * [MDEV-31154](https://jira.mariadb.org/browse/MDEV-31154) Fatal InnoDB error or assertion \`!is\_v' failure upon multi-update with indexed virtual column [MDEV-33558](https://jira.mariadb.org/browse/MDEV-33558) Fatal error InnoDB: Clustered record field for column x not found
* [Revision #f5df4482e0](https://github.com/MariaDB/server/commit/f5df4482e0)\
  2024-03-15 13:32:22 +0530
  * [MDEV-33214](https://jira.mariadb.org/browse/MDEV-33214) Table is getting rebuild with ALTER TABLE ADD COLUMN
* [Revision #ef7abc881c](https://github.com/MariaDB/server/commit/ef7abc881c)\
  2024-03-14 22:48:12 +0100
  * [MDEV-10793](https://jira.mariadb.org/browse/MDEV-10793): [MDEV-33292](https://jira.mariadb.org/browse/MDEV-33292): main.kill\_processlist-6619 fails sporadically in buildbot
* [Revision #ae063e4ff5](https://github.com/MariaDB/server/commit/ae063e4ff5)\
  2024-03-01 11:21:50 +0200
  * Fixed random failure in main.kill\_processlist-6619
* [Revision #d7758debae](https://github.com/MariaDB/server/commit/d7758debae)\
  2024-03-13 20:07:04 +0700
  * [MDEV-33218](https://jira.mariadb.org/browse/MDEV-33218): Assertion \`active\_arena->is\_stmt\_prepare\_or\_first\_stmt\_execute() || active\_arena->state == Query\_arena::STMT\_SP\_QUERY\_ARGUMENTS' failed in st\_select\_lex::fix\_prepare\_information
* [Revision #0a6f46965a](https://github.com/MariaDB/server/commit/0a6f46965a)\
  2024-03-08 22:18:44 +0100
  * [MDEV-33475](https://jira.mariadb.org/browse/MDEV-33475): --gtid-ignore-duplicate can double-apply event in case of parallel replication retry
* [Revision #7bcacd767a](https://github.com/MariaDB/server/commit/7bcacd767a)\
  2024-03-13 12:21:53 +0100
  * [MDEV-21864](https://jira.mariadb.org/browse/MDEV-21864) Commands start-all-slaves and stop-all-slaves are not listed in mysqladmin help
* [Revision #ac20edd737](https://github.com/MariaDB/server/commit/ac20edd737)\
  2024-03-13 17:46:05 +0700
  * [MDEV-33549](https://jira.mariadb.org/browse/MDEV-33549): Incorrect handling of UPDATE in PS mode in case a table's colum declared as NOT NULL
* [Revision #428a673152](https://github.com/MariaDB/server/commit/428a673152)\
  2024-03-12 16:13:49 +0700
  * [MDEV-33549](https://jira.mariadb.org/browse/MDEV-33549): Incorrect handling of UPDATE in PS mode in case a table's colum declared as NOT NULL
* [Revision #0a9cec229a](https://github.com/MariaDB/server/commit/0a9cec229a)\
  2024-03-11 16:14:54 +0200
  * [MDEV-33642](https://jira.mariadb.org/browse/MDEV-33642): MemorySanitizer: SEGV on unknown address on shutdown
* [Revision #09ea2dc788](https://github.com/MariaDB/server/commit/09ea2dc788)\
  2024-03-11 09:53:04 +0200
  * [MDEV-33209](https://jira.mariadb.org/browse/MDEV-33209) Stack overflow in main.json\_debug\_nonembedded due to incorrect debug injection
* [Revision #015f69a779](https://github.com/MariaDB/server/commit/015f69a779)\
  2024-03-11 09:52:59 +0200
  * [MDEV-14448](https://jira.mariadb.org/browse/MDEV-14448) fixup: clang -Wunused-function
* [Revision #648d2da8f2](https://github.com/MariaDB/server/commit/648d2da8f2)\
  2024-03-07 15:24:43 +0100
  * [MDEV-33540](https://jira.mariadb.org/browse/MDEV-33540) Avoid writes to TRX\_SYS page during mariadb-backup operations
* [Revision #738da4918d](https://github.com/MariaDB/server/commit/738da4918d)\
  2024-03-05 21:32:30 +0530
  * [MDEV-32346](https://jira.mariadb.org/browse/MDEV-32346) Assertion failure sym\_node->table != NULL in pars\_retrieve\_table\_def on UPDATE
* [Revision #8532dd82f1](https://github.com/MariaDB/server/commit/8532dd82f1)\
  2024-03-05 18:31:56 +0530
  * [MDEV-13765](https://jira.mariadb.org/browse/MDEV-13765) encryption.encrypt\_and\_grep failed in buildbot with wrong result
* [Revision #b93252a303](https://github.com/MariaDB/server/commit/b93252a303)\
  2023-12-15 00:48:48 +0400
  * [MDEV-32454](https://jira.mariadb.org/browse/MDEV-32454) JSON test has problem in view protocol.
* [Revision #c9b0c006e0](https://github.com/MariaDB/server/commit/c9b0c006e0)\
  2024-02-19 18:17:36 +0100
  * galera: correction after wsrep-lib update
* [Revision #87abae4601](https://github.com/MariaDB/server/commit/87abae4601)\
  2024-02-27 09:48:14 +0100
  * galera: wsrep-lib submodule update
* [Revision #57cc8605eb](https://github.com/MariaDB/server/commit/57cc8605eb)\
  2024-02-26 12:40:14 +0530
  * [MDEV-19044](https://jira.mariadb.org/browse/MDEV-19044) Alter table corrupts while applying the modification log
* [Revision #1b37cb71f4](https://github.com/MariaDB/server/commit/1b37cb71f4)\
  2024-01-26 13:12:03 +0400
  * [MDEV-32975](https://jira.mariadb.org/browse/MDEV-32975) Default charset doesn't work with PHP MySQLi extension
* [Revision #a5998145ba](https://github.com/MariaDB/server/commit/a5998145ba)\
  2024-02-20 13:36:18 +0100
  * Record correct mutex (LOCK\_STATUS and acl\_cache) order for debugging.
* [Revision #8a505980c5](https://github.com/MariaDB/server/commit/8a505980c5)\
  2023-10-27 12:44:57 +0800
  * [MDEV-28430](https://jira.mariadb.org/browse/MDEV-28430): Fix memory barrier missing of lf\_alloc on Arm64
* [Revision #5707f1efda](https://github.com/MariaDB/server/commit/5707f1efda)\
  2024-02-15 10:41:23 +0100
  * [MDEV-33468](https://jira.mariadb.org/browse/MDEV-33468): Crash due to missing stack overrun check in two recursive functions
* [Revision #fdaa7a96ed](https://github.com/MariaDB/server/commit/fdaa7a96ed)\
  2024-02-12 12:00:58 +0100
  * [MDEV-33443](https://jira.mariadb.org/browse/MDEV-33443): Unsafe use of LOCK\_thd\_kill in my\_malloc\_size\_cb\_func()
* [Revision #c73c6aea63](https://github.com/MariaDB/server/commit/c73c6aea63)\
  2024-02-11 11:57:42 +0100
  * [MDEV-33426](https://jira.mariadb.org/browse/MDEV-33426): Aria temptables wrong thread-specific memory accounting in slave thread
* [Revision #ae709b64e2](https://github.com/MariaDB/server/commit/ae709b64e2)\
  2024-02-13 09:24:32 +0100
  * fix view protocol in [MDEV-29179](https://jira.mariadb.org/browse/MDEV-29179)
* [Revision #ca88eac835](https://github.com/MariaDB/server/commit/ca88eac835)\
  2024-02-01 14:51:26 +0200
  * [MDEV-30528](https://jira.mariadb.org/browse/MDEV-30528) CREATE FULLTEXT INDEX assertion failure WITH SYSTEM VERSIONING
* [Revision #c37216de64](https://github.com/MariaDB/server/commit/c37216de64)\
  2024-02-12 21:08:22 +1100
  * [MDEV-33441](https://jira.mariadb.org/browse/MDEV-33441) Do not deinit plugin variables when retry requested
* [Revision #a0f2ff8832](https://github.com/MariaDB/server/commit/a0f2ff8832)\
  2024-02-12 12:43:08 +0100
  * Return back wolfssl v5.6.6 and new CC changed by 6b2cd7869522a140329a27583f965b8662d7f5f5
* [Revision #36f51d9748](https://github.com/MariaDB/server/commit/36f51d9748)\
  2023-02-17 08:28:38 +1200
  * [MDEV-29179](https://jira.mariadb.org/browse/MDEV-29179) Condition pushdown from HAVING into WHERE is not shown in optimizer trace
* [Revision #d816a5ca32](https://github.com/MariaDB/server/commit/d816a5ca32)\
  2024-02-08 14:19:47 +0100
  * fix test
* [Revision #e48bd474a2](https://github.com/MariaDB/server/commit/e48bd474a2)\
  2024-02-08 12:17:02 +0700
  * [MDEV-15703](https://jira.mariadb.org/browse/MDEV-15703): Crash in EXECUTE IMMEDIATE 'CREATE OR REPLACE TABLE t1 (a INT DEFAULT ?)' USING DEFAULT
* [Revision #6b2cd78695](https://github.com/MariaDB/server/commit/6b2cd78695)\
  2024-02-08 12:12:57 +0700
  * [MDEV-15703](https://jira.mariadb.org/browse/MDEV-15703): Crash in EXECUTE IMMEDIATE 'CREATE OR REPLACE TABLE t1 (a INT DEFAULT ?)' USING DEFAULT, UBSAN runtime error: member call on null pointer of type 'struct TABLE\_LIST' in Item\_param::save\_in\_field
* [Revision #85db534731](https://github.com/MariaDB/server/commit/85db534731)\
  2024-02-07 12:26:59 +0200
  * [MDEV-33400](https://jira.mariadb.org/browse/MDEV-33400) Adaptive hash index corruption after DISCARD TABLESPACE
* [Revision #2310130488](https://github.com/MariaDB/server/commit/2310130488)\
  2024-02-06 12:15:02 -0500
  * bump the VERSION
* Merge [Revision #8adc759988](https://github.com/MariaDB/server/commit/8adc759988) 2024-02-06 15:58:12 +0100 - Merge branch '10.4' into mariadb-10.4.33
* [Revision #3812e1c958](https://github.com/MariaDB/server/commit/3812e1c958)\
  2024-02-04 11:58:31 -0800
  * Fix commit 179424db: No test file or result files should be executable
* [Revision #05314ed0d4](https://github.com/MariaDB/server/commit/05314ed0d4)\
  2024-01-31 23:50:41 -0800
  * [MDEV-31305](https://jira.mariadb.org/browse/MDEV-31305) Crash caused by query with aggregation over materialized derived
* [Revision #f4ee7c110c](https://github.com/MariaDB/server/commit/f4ee7c110c)\
  2023-11-30 12:52:53 +0300
  * [MDEV-22232](https://jira.mariadb.org/browse/MDEV-22232) Fix test after changing behavior of ALTER DROP FOREIGN KEY
* [Revision #b7d1f65b81](https://github.com/MariaDB/server/commit/b7d1f65b81)\
  2024-01-30 13:10:53 +0200
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266) fixup: Remove dead code
* [Revision #bc2849579b](https://github.com/MariaDB/server/commit/bc2849579b)\
  2024-01-30 13:10:46 +0200
  * [MDEV-33251](https://jira.mariadb.org/browse/MDEV-33251) Redundant check on prebuilt::n\_rows\_fetched overflow
* [Revision #57ffcd686f](https://github.com/MariaDB/server/commit/57ffcd686f)\
  2024-01-29 15:51:29 +0200
  * [MDEV-21472](https://jira.mariadb.org/browse/MDEV-21472): ALTER TABLE ... ANALYZE PARTITION ... with EITS reads and locks all rows
* [Revision #f8fa3c55c6](https://github.com/MariaDB/server/commit/f8fa3c55c6)\
  2024-01-04 16:46:47 +0200
  * [MDEV-33173](https://jira.mariadb.org/browse/MDEV-33173) : Galera test case galera\_sr\_kill\_slave\_before\_apply unstable
* [Revision #ddb27a29b1](https://github.com/MariaDB/server/commit/ddb27a29b1)\
  2024-01-04 15:27:15 +0200
  * [MDEV-33172](https://jira.mariadb.org/browse/MDEV-33172) : Galera test case galera\_mdl\_race unstable
* [Revision #5b4456b38a](https://github.com/MariaDB/server/commit/5b4456b38a)\
  2023-12-29 10:20:51 +0200
  * [MDEV-33036](https://jira.mariadb.org/browse/MDEV-33036) : Galera test case galera\_3nodes.galera\_ist\_gcache\_rollover has warning
* [Revision #49fa5f6b5f](https://github.com/MariaDB/server/commit/49fa5f6b5f)\
  2024-01-05 11:33:53 +0200
  * [MDEV-33138](https://jira.mariadb.org/browse/MDEV-33138) : Galera test case MW-336 unstable
* [Revision #736e429320](https://github.com/MariaDB/server/commit/736e429320)\
  2024-01-05 13:35:41 +0200
  * [MDEV-32635](https://jira.mariadb.org/browse/MDEV-32635): galera\_shutdown\_nonprim: mysql\_shutdown failed
* [Revision #e4f221a5f2](https://github.com/MariaDB/server/commit/e4f221a5f2)\
  2024-01-29 15:17:57 -0700
  * [MDEV-33327](https://jira.mariadb.org/browse/MDEV-33327): rpl\_seconds\_behind\_master\_spike Sensitive to IO Thread Stop Position
* [Revision #c768ac6208](https://github.com/MariaDB/server/commit/c768ac6208)\
  2023-09-04 12:22:51 +0300
  * [MDEV-25731](https://jira.mariadb.org/browse/MDEV-25731) : Assertion \`mode\_ == m\_local' failed in wsrep::client\_state::streaming\_params()
* [Revision #daaa16a47f](https://github.com/MariaDB/server/commit/daaa16a47f)\
  2023-11-01 11:07:16 +0200
  * [MDEV-25089](https://jira.mariadb.org/browse/MDEV-25089) : Assertion \`error.len > 0' failed in galera::ReplicatorSMM::handle\_apply\_error()
* [Revision #3228c08fa8](https://github.com/MariaDB/server/commit/3228c08fa8)\
  2023-12-07 08:23:29 +0200
  * [MDEV-22063](https://jira.mariadb.org/browse/MDEV-22063) : Assertion \`0' failed in wsrep::transaction::before\_rollback

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
