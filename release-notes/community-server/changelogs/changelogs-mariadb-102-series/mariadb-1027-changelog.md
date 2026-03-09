# MariaDB 10.2.7 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.7)[Release Notes](../../old-releases/10.2/10.2.7.md)[Changelog](mariadb-1027-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 12 Jul 2017

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.7.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #5ff2db7f67](https://github.com/MariaDB/server/commit/5ff2db7f67)\
  2017-07-10 00:05:45 +0300
  * Follow-up for [MDEV-13089](https://jira.mariadb.org/browse/MDEV-13089) (identifier quoting in partitioning)
* [Revision #4df726e180](https://github.com/MariaDB/server/commit/4df726e180)\
  2017-07-10 00:05:06 +0300
  * storage\_engine subsuites should also be disabled for XtraDB
* [Revision #3af125e082](https://github.com/MariaDB/server/commit/3af125e082)\
  2017-07-09 20:42:29 +0300
  * Updated list of unstable tests for 10.2.7
* [Revision #93e32d725c](https://github.com/MariaDB/server/commit/93e32d725c)\
  2017-07-09 20:38:57 +0300
  * Follow-up for [MDEV-13089](https://jira.mariadb.org/browse/MDEV-13089) (identifier quoting in partitioning)
* [Revision #970719cb15](https://github.com/MariaDB/server/commit/970719cb15)\
  2017-07-09 20:36:19 +0300
  * [MDEV-12785](https://jira.mariadb.org/browse/MDEV-12785) MTR complains "Can't exec mariadb\_config"
* [Revision #51256b603a](https://github.com/MariaDB/server/commit/51256b603a)\
  2017-07-08 19:18:52 +0200
  * fixes for lower\_case\_table\_names=2
* Merge [Revision #c9801135c1](https://github.com/MariaDB/server/commit/c9801135c1) 2017-07-08 09:56:28 +0200 - Merge branch '10.1' into 10.2
* Merge [Revision #9e11e055ce](https://github.com/MariaDB/server/commit/9e11e055ce) 2017-07-07 11:30:03 +0200 - Merge branch '10.0' into 10.1
* [Revision #6b99859fff](https://github.com/MariaDB/server/commit/6b99859fff)\
  2017-07-06 23:26:18 +0200
  * after-merge fix for a7ed4644a6f
* Merge [Revision #89dc445a55](https://github.com/MariaDB/server/commit/89dc445a55) 2017-07-06 23:47:33 +0200 - Merge branch '5.5' into 10.0
* [Revision #f305a7ce4b](https://github.com/MariaDB/server/commit/f305a7ce4b)\
  2017-07-06 14:06:37 +0200
  * bugfix: long partition names
* [Revision #a7ed4644a6](https://github.com/MariaDB/server/commit/a7ed4644a6)\
  2017-07-03 13:35:32 +0200
  * [MDEV-10146](https://jira.mariadb.org/browse/MDEV-10146): Wrong result (or questionable result and behavior) with aggregate function in uncorrelated SELECT subquery
* [Revision #23ac2dd2a4](https://github.com/MariaDB/server/commit/23ac2dd2a4)\
  2017-07-04 13:28:47 +1000
  * sql\_class: incorrect assignment in Security\_context::destroy
* [Revision #89b81a9a24](https://github.com/MariaDB/server/commit/89b81a9a24)\
  2017-07-02 13:52:34 +1000
  * ma\_pagecache: release lock in pagecache\_read
* [Revision #2328860379](https://github.com/MariaDB/server/commit/2328860379)\
  2017-07-02 13:42:46 +1000
  * ma\_loghandler: translog\_set\_only\_in\_buffers failed to release lock
* [Revision #051f90a534](https://github.com/MariaDB/server/commit/051f90a534)\
  2017-07-02 13:37:14 +1000
  * ma\_loghandler: release file\_header\_lock on error
* [Revision #623c3f6731](https://github.com/MariaDB/server/commit/623c3f6731)\
  2017-07-02 11:26:02 +1000
  * thread\_group\_close: release mutex in all branches
* [Revision #cb870674d4](https://github.com/MariaDB/server/commit/cb870674d4)\
  2017-07-02 15:40:37 +1000
  * ha\_archive::info remove hidden assignment
* [Revision #9fc71eebb6](https://github.com/MariaDB/server/commit/9fc71eebb6)\
  2017-07-02 16:48:11 +1000
  * item\_timefunc: identical operands
* [Revision #4d21313549](https://github.com/MariaDB/server/commit/4d21313549)\
  2017-05-24 13:11:33 +0200
  * coverity medium warnings
* [Revision #946a07e8a8](https://github.com/MariaDB/server/commit/946a07e8a8)\
  2017-07-02 19:45:04 +0300
  * Fix for [MDEV-9670](https://jira.mariadb.org/browse/MDEV-9670) server\_id mysteriously set to 0
* [Revision #46d6f74c48](https://github.com/MariaDB/server/commit/46d6f74c48)\
  2017-07-02 14:59:06 +0300
  * Fix for [MDEV-13191](https://jira.mariadb.org/browse/MDEV-13191). Assert for !is\_set() when doing LOAD DATA
* [Revision #21689d1252](https://github.com/MariaDB/server/commit/21689d1252)\
  2017-06-30 15:58:27 -0700
  * Run spider mtr suites in 10.0 only on demand.
* [Revision #5789934fda](https://github.com/MariaDB/server/commit/5789934fda)\
  2017-07-05 19:26:48 +0200
  * compilation warning
* [Revision #42f657cd2f](https://github.com/MariaDB/server/commit/42f657cd2f)\
  2017-07-07 18:29:31 +0300
  * [MDEV-13267](https://jira.mariadb.org/browse/MDEV-13267) At startup with crash recovery: mtr\_t::commit\_checkpoint(lsn\_t, bool): Assertion \`!recv\_no\_log\_write' failed
* [Revision #f20693c231](https://github.com/MariaDB/server/commit/f20693c231)\
  2017-07-07 11:57:39 +0300
  * Remove a reference to a non-existent include directory
* [Revision #3b862aaa10](https://github.com/MariaDB/server/commit/3b862aaa10)\
  2017-07-07 10:19:02 +1000
  * travis: Debian build - minimise packages, enable ccache
* [Revision #c89c49427d](https://github.com/MariaDB/server/commit/c89c49427d)\
  2017-07-06 23:14:39 +0300
  * Reduce a test so that it fails less frequently on buildbot
* Merge [Revision #d902d43ce7](https://github.com/MariaDB/server/commit/d902d43ce7) 2017-07-06 20:28:08 +0300 - Merge 10.1 into 10.2
* [Revision #2b5c9bc2c8](https://github.com/MariaDB/server/commit/2b5c9bc2c8)\
  2017-07-06 14:18:53 +0300
  * [MDEV-13247](https://jira.mariadb.org/browse/MDEV-13247) innodb\_log\_compressed\_pages=OFF breaks crash recovery of ROW\_FORMAT=COMPRESSED tables
* [Revision #ec76945dac](https://github.com/MariaDB/server/commit/ec76945dac)\
  2017-07-06 00:45:43 +0300
  * [MDEV-13248](https://jira.mariadb.org/browse/MDEV-13248) binlog.binlog\_parallel\_replication\_marks\_row fails in buildbot
* [Revision #4693f01f57](https://github.com/MariaDB/server/commit/4693f01f57)\
  2017-07-05 18:27:03 +0300
  * Fix warning discovered by ASAN
* [Revision #99d52c45cb](https://github.com/MariaDB/server/commit/99d52c45cb)\
  2017-07-06 19:20:34 +0300
  * mariadb-backup: Copy all of the redo log correctly
* [Revision #d7b21a49c2](https://github.com/MariaDB/server/commit/d7b21a49c2)\
  2017-07-06 18:31:28 +0300
  * mariadb-backup: Remove unused parameters and fix some memory leaks
* [Revision #60e6170893](https://github.com/MariaDB/server/commit/60e6170893)\
  2017-07-06 14:15:32 +0000
  * mysqltest - increase size of the "die message".
* [Revision #6f1f911497](https://github.com/MariaDB/server/commit/6f1f911497)\
  2017-07-05 19:37:57 +0000
  * [MDEV-12445](https://jira.mariadb.org/browse/MDEV-12445) : Rocksdb does not shutdown worker threads and aborts in memleak check on server shutdown
* [Revision #53d6325db0](https://github.com/MariaDB/server/commit/53d6325db0)\
  2017-07-05 19:41:46 +0000
  * Fix assertion in rocksb.
* [Revision #4e08cdf52a](https://github.com/MariaDB/server/commit/4e08cdf52a)\
  2017-07-06 10:39:21 +0400
  * Fixed build failure on Windows
* [Revision #7e6a600d13](https://github.com/MariaDB/server/commit/7e6a600d13)\
  2017-06-30 23:15:22 +0200
  * Remove obsolete synonyms for access bits
* [Revision #0ff62ad808](https://github.com/MariaDB/server/commit/0ff62ad808)\
  2017-07-06 02:14:33 +0300
  * InnoDB: Remove a redundant condition and an outdated comment
* [Revision #72a2de92a1](https://github.com/MariaDB/server/commit/72a2de92a1)\
  2017-07-05 22:09:28 +0300
  * Avoid a hang when InnoDB startup is aborted during redo log apply
* Merge [Revision #f6633bf058](https://github.com/MariaDB/server/commit/f6633bf058) 2017-07-05 19:08:55 +0200 - Merge branch '10.1' into 10.2
* [Revision #e555540ab6](https://github.com/MariaDB/server/commit/e555540ab6)\
  2017-07-05 14:35:55 +0300
  * [MDEV-13105](https://jira.mariadb.org/browse/MDEV-13105) InnoDB fails to load a table with PAGE\_COMPRESSION\_LEVEL after upgrade from 10.1.20
* [Revision #8ae9c86f2a](https://github.com/MariaDB/server/commit/8ae9c86f2a)\
  2017-07-04 10:26:14 -0400
  * bump the VERSION
* [Revision #f8dadbdf24](https://github.com/MariaDB/server/commit/f8dadbdf24)\
  2017-06-04 11:47:30 +0300
  * Ensure that we have LOG\_log locked when relay\_log.close is called
* [Revision #228479a28c](https://github.com/MariaDB/server/commit/228479a28c)\
  2017-05-29 11:35:36 +0300
  * [MDEV-8075](https://jira.mariadb.org/browse/MDEV-8075): DROP TEMPORARY TABLE not marked as ddl, causing optimistic parallel replication to fail
* [Revision #da7604a294](https://github.com/MariaDB/server/commit/da7604a294)\
  2017-07-01 21:12:26 +0300
  * Latest additions to the list of unstable tests in 10.1.25
* [Revision #806d4e3127](https://github.com/MariaDB/server/commit/806d4e3127)\
  2017-06-30 16:17:29 -0700
  * Run spider mtr suites in 10.1 only on demand.
* Merge [Revision #d38b15de65](https://github.com/MariaDB/server/commit/d38b15de65) 2017-06-30 16:33:13 +0200 - Merge branch '10.0-galera' into 10.1
* [Revision #4f40f87c48](https://github.com/MariaDB/server/commit/4f40f87c48)\
  2017-06-02 11:33:35 -0400
  * bump the VERSION
* [Revision #3806a323ce](https://github.com/MariaDB/server/commit/3806a323ce)\
  2017-06-01 16:40:57 +0530
  * Fix galera\_var\_node\_address.test
* [Revision #aa0f7e9bd7](https://github.com/MariaDB/server/commit/aa0f7e9bd7)\
  2017-05-31 17:53:32 +0530
  * Fix galera\_defaults test and check\_galera\_version.inc script
* Merge [Revision #92209ac6f6](https://github.com/MariaDB/server/commit/92209ac6f6) 2017-05-30 15:28:52 +0530 - Merge tag 'mariadb-10.0.31' into 10.0-galera
* Merge [Revision #d3cc15eb82](https://github.com/MariaDB/server/commit/d3cc15eb82) 2017-06-30 13:28:39 +0200 - Merge branch '10.0' into 10.1
* Merge [Revision #92928bcdd9](https://github.com/MariaDB/server/commit/92928bcdd9) 2017-06-29 23:32:18 +0200 - Merge branch '5.5' into 10.0
* [Revision #4db6e1e4a5](https://github.com/MariaDB/server/commit/4db6e1e4a5)\
  2017-06-29 20:47:08 +0200
  * uninitialized variable
* [Revision #5c89f23b45](https://github.com/MariaDB/server/commit/5c89f23b45)\
  2017-06-29 21:27:05 +0300
  * Fix debug assert post [MDEV-10306](https://jira.mariadb.org/browse/MDEV-10306)
* Merge [Revision #a02ba9c1c9](https://github.com/MariaDB/server/commit/a02ba9c1c9) 2017-06-28 10:10:31 +0200 - Merge branch '5.5' into 10.0
* [Revision #d5cd334504](https://github.com/MariaDB/server/commit/d5cd334504)\
  2017-06-27 14:00:10 +0200
  * [MDEV-13187](https://jira.mariadb.org/browse/MDEV-13187) incorrect backslash parsing in clients
* [Revision #39385ff7b2](https://github.com/MariaDB/server/commit/39385ff7b2)\
  2017-06-27 13:25:50 +0200
  * [MDEV-13187](https://jira.mariadb.org/browse/MDEV-13187) incorrect backslash parsing in clients
* [Revision #b503b1c0ed](https://github.com/MariaDB/server/commit/b503b1c0ed)\
  2017-06-23 15:14:22 +0200
  * [MDEV-11646](https://jira.mariadb.org/browse/MDEV-11646) main.myisam, maria.maria, main.mix2\_myisam, main.myisampack, main.mrr\_icp\_extra fail in buildbot with valgrind (Syscall param pwrite64(buf) points to uninitialised byte(s))
* [Revision #a1e51e7f47](https://github.com/MariaDB/server/commit/a1e51e7f47)\
  2017-06-30 11:28:52 +0300
  * mariadb-backup: Test file cleanup
* [Revision #4fe89773d8](https://github.com/MariaDB/server/commit/4fe89773d8)\
  2017-06-22 12:21:54 +0300
  * mariadb-backup: Clean up xtrabackup options
* [Revision #273e0f663e](https://github.com/MariaDB/server/commit/273e0f663e)\
  2017-06-30 10:28:01 +0200
  * [MDEV-13179](https://jira.mariadb.org/browse/MDEV-13179) main.errors fails in buildbot and outside with wrong errno 1290
* Merge [Revision #330792f3c3](https://github.com/MariaDB/server/commit/330792f3c3) 2017-06-27 16:34:36 +0300 - Merge branch 'bb-10.1-vicentiu' into 10.1
* [Revision #32659db864](https://github.com/MariaDB/server/commit/32659db864)\
  2017-06-26 12:22:27 +0300
  * Fix merge error from 10.0
* Merge [Revision #2e335a471c](https://github.com/MariaDB/server/commit/2e335a471c) 2017-06-21 16:19:43 +0300 - Merge remote-tracking branch '10.0' into 10.1
* Merge [Revision #8baf9b0c46](https://github.com/MariaDB/server/commit/8baf9b0c46) 2017-06-20 12:31:17 +0300 - Merge remote-tracking branch '5.5' into 10.0
* [Revision #ded614d7db](https://github.com/MariaDB/server/commit/ded614d7db)\
  2017-06-14 13:44:31 +0200
  * [MDEV-12778](https://jira.mariadb.org/browse/MDEV-12778) mariadb-10.1 FTBFS on GNU/Hurd due to use of PATH\_MAX
* [Revision #48429359d6](https://github.com/MariaDB/server/commit/48429359d6)\
  2017-06-16 11:34:59 +0200
  * [MDEV-4646](https://jira.mariadb.org/browse/MDEV-4646) No mysqld-debug or debuginfo in MariaDB-Server RPM
* [Revision #e548e2184b](https://github.com/MariaDB/server/commit/e548e2184b)\
  2017-03-26 16:00:35 +1100
  * Use CPACK\_RPM\_FILE\_NAME="RPM-DEFAULT"
* [Revision #c7141fa75d](https://github.com/MariaDB/server/commit/c7141fa75d)\
  2017-06-15 14:41:59 +0200
  * [MDEV-13002](https://jira.mariadb.org/browse/MDEV-13002) mysqltest regex replace results in incorrect result
* [Revision #c661b4d0fb](https://github.com/MariaDB/server/commit/c661b4d0fb)\
  2017-06-14 00:48:34 +0200
  * [MDEV-13017](https://jira.mariadb.org/browse/MDEV-13017) LOCK TABLE fails with irrelevant error while working with tables affected by ANSI\_QUOTES
* [Revision #5cbbfe9f54](https://github.com/MariaDB/server/commit/5cbbfe9f54)\
  2017-06-14 00:33:11 +0200
  * cleanup: remove duplicate code
* [Revision #918e47030b](https://github.com/MariaDB/server/commit/918e47030b)\
  2017-06-14 11:30:32 +0200
  * [MDEV-13063](https://jira.mariadb.org/browse/MDEV-13063) Server crashes in intern\_plugin\_lock or assertion \`plugin\_ptr->ref\_count == 1' fails in plugin\_init
* [Revision #70b94c35d7](https://github.com/MariaDB/server/commit/70b94c35d7)\
  2017-06-14 11:27:36 +0200
  * cleanup: move common test into a function
* [Revision #b850fc66ca](https://github.com/MariaDB/server/commit/b850fc66ca)\
  2017-06-07 22:54:57 -0700
  * Fixed the bug [MDEV-12855](https://jira.mariadb.org/browse/MDEV-12855).
* [Revision #151f4e9b4a](https://github.com/MariaDB/server/commit/151f4e9b4a)\
  2017-06-07 16:29:55 -0700
  * Fixed the bug [MDEV-12963](https://jira.mariadb.org/browse/MDEV-12963).
* [Revision #c258ca2463](https://github.com/MariaDB/server/commit/c258ca2463)\
  2017-06-07 12:45:09 -0700
  * Fixed the bug [MDEV-12838](https://jira.mariadb.org/browse/MDEV-12838).
* [Revision #5e4f4ec821](https://github.com/MariaDB/server/commit/5e4f4ec821)\
  2017-06-19 15:59:19 +0300
  * [MDEV-12975](https://jira.mariadb.org/browse/MDEV-12975) InnoDB redo log minimum size check uses detected file size instead of requested innodb\_log\_file\_size
* [Revision #3a37afec29](https://github.com/MariaDB/server/commit/3a37afec29)\
  2017-06-19 12:45:32 +0400
  * [MDEV-10306](https://jira.mariadb.org/browse/MDEV-10306) Wrong results with combination of CONCAT, SUBSTR and CONVERT in subquery
* [Revision #f0ad93403f](https://github.com/MariaDB/server/commit/f0ad93403f)\
  2017-05-22 17:06:01 +0300
  * [MDEV-12666](https://jira.mariadb.org/browse/MDEV-12666): CURRENT\_ROLE() and DATABASE() does not work in a view
* [Revision #34da3be8a8](https://github.com/MariaDB/server/commit/34da3be8a8)\
  2017-05-22 13:38:26 +0300
  * [MDEV-10463](https://jira.mariadb.org/browse/MDEV-10463): Granted as a whole to roles, databases are not show in SHOW DATABASES
* [Revision #2579b252dd](https://github.com/MariaDB/server/commit/2579b252dd)\
  2017-06-15 12:35:53 +0200
  * Update MariaDB Foundation sponsors
* [Revision #3125ba8912](https://github.com/MariaDB/server/commit/3125ba8912)\
  2017-06-27 03:48:04 +0300
  * Updated list of unstable tests for 10.1.25 release
* [Revision #b76b69cd5f](https://github.com/MariaDB/server/commit/b76b69cd5f)\
  2017-06-20 14:55:30 +0200
  * [MDEV-10880](https://jira.mariadb.org/browse/MDEV-10880): Assertions `keypart_map' or` prebuilt->search\_tuple->n\_fields > 0' fail on DISTINCT and GROUP BY constant
* [Revision #f65d6a03f0](https://github.com/MariaDB/server/commit/f65d6a03f0)\
  2017-06-22 19:28:07 +0000
  * workaround for a test failure on windows (by serg)
* [Revision #9b7afd4188](https://github.com/MariaDB/server/commit/9b7afd4188)\
  2017-06-16 16:24:36 +0200
  * [MDEV-12819](https://jira.mariadb.org/browse/MDEV-12819) order by ordering expression changed to empty string when creatin view with union
* [Revision #ba9daddcd8](https://github.com/MariaDB/server/commit/ba9daddcd8)\
  2017-06-20 20:02:20 +0000
  * Cherrypick Perconas fix for leaking descriptors with new xbstream.
* [Revision #f1a6d24af3](https://github.com/MariaDB/server/commit/f1a6d24af3)\
  2017-06-21 23:29:19 +0200
  * [MDEV-11003](https://jira.mariadb.org/browse/MDEV-11003) ndb test suite still exists and does not work
* [Revision #3f240bff80](https://github.com/MariaDB/server/commit/3f240bff80)\
  2017-06-16 00:35:57 +0200
  * [MDEV-13097](https://jira.mariadb.org/browse/MDEV-13097) Online alter of a partitioned MyISAM table with auto\_increment
* [Revision #b6ce68f450](https://github.com/MariaDB/server/commit/b6ce68f450)\
  2017-06-15 20:16:18 +0200
  * [MDEV-13012](https://jira.mariadb.org/browse/MDEV-13012) Assertion \`share->error' failed in discover\_handlerton upon executing statement with max\_session\_mem\_used = 8192
* [Revision #d937916c06](https://github.com/MariaDB/server/commit/d937916c06)\
  2017-06-14 20:21:24 +0200
  * [MDEV-12193](https://jira.mariadb.org/browse/MDEV-12193) Discontinue support of unsecure and unsupported OpenSSL versions (< 1.0.1)
* [Revision #d4007f2e73](https://github.com/MariaDB/server/commit/d4007f2e73)\
  2017-05-04 17:18:45 +0200
  * disable getopt prefix matching in mtr bootstrap
* [Revision #e333d82964](https://github.com/MariaDB/server/commit/e333d82964)\
  2017-06-22 11:38:50 +0530
  * [MDEV-12398](https://jira.mariadb.org/browse/MDEV-12398) All cluster nodes stop due to a foreign key constraint failure
* [Revision #472c2d9b2f](https://github.com/MariaDB/server/commit/472c2d9b2f)\
  2017-06-19 18:23:55 +0000
  * [MDEV-13106](https://jira.mariadb.org/browse/MDEV-13106) : Fix check for empty directory in MSI installer
* [Revision #b9a326b6e1](https://github.com/MariaDB/server/commit/b9a326b6e1)\
  2017-06-19 17:00:09 +0000
  * [MDEV-12709](https://jira.mariadb.org/browse/MDEV-12709) : mariadb-backup - during backup phase read some innodb parameter using "show variables", rather than take the value from my.cnf.
* [Revision #fc5932a1b7](https://github.com/MariaDB/server/commit/fc5932a1b7)\
  2017-06-24 10:16:48 +0200
  * update libmariadb
* [Revision #1ea3c93fda](https://github.com/MariaDB/server/commit/1ea3c93fda)\
  2017-07-03 16:22:30 +0200
  * [MDEV-9144](https://jira.mariadb.org/browse/MDEV-9144) JSON data type
* [Revision #51d457f371](https://github.com/MariaDB/server/commit/51d457f371)\
  2017-07-03 11:47:39 +0200
  * compilation failures
* [Revision #291411c96c](https://github.com/MariaDB/server/commit/291411c96c)\
  2017-06-29 00:57:20 +0200
  * [MDEV-13132](https://jira.mariadb.org/browse/MDEV-13132) Information Schema does not show whether column default is expression or literal
* [Revision #0559f12972](https://github.com/MariaDB/server/commit/0559f12972)\
  2017-06-30 20:15:38 +0200
  * [MDEV-13209](https://jira.mariadb.org/browse/MDEV-13209) Cross-database operation with virtual columns fails
* [Revision #186075adf2](https://github.com/MariaDB/server/commit/186075adf2)\
  2017-06-30 16:31:46 +0200
  * [MDEV-12938](https://jira.mariadb.org/browse/MDEV-12938) Discrepancy between mysql\_config and mariadb\_config
* [Revision #d2d52305b4](https://github.com/MariaDB/server/commit/d2d52305b4)\
  2017-06-28 19:41:08 +0200
  * [MDEV-12755](https://jira.mariadb.org/browse/MDEV-12755) Replication tests fail in buildbot with ASAN
* [Revision #cf9c290563](https://github.com/MariaDB/server/commit/cf9c290563)\
  2017-06-28 18:55:33 +0200
  * [MDEV-12738](https://jira.mariadb.org/browse/MDEV-12738) main.default fails with valgrind in buildbot and outside
* [Revision #48c22a68b1](https://github.com/MariaDB/server/commit/48c22a68b1)\
  2017-06-28 16:06:07 +0200
  * [MDEV-13089](https://jira.mariadb.org/browse/MDEV-13089) identifier quoting in partitioning
* [Revision #e1093e2464](https://github.com/MariaDB/server/commit/e1093e2464)\
  2017-06-27 20:47:46 +0200
  * cleanup: part\_func\_string and subpart\_func\_string
* [Revision #785e2248bd](https://github.com/MariaDB/server/commit/785e2248bd)\
  2017-06-27 20:46:45 +0200
  * [MDEV-13089](https://jira.mariadb.org/browse/MDEV-13089) identifier quoting in partitioning
* [Revision #504eff0ca1](https://github.com/MariaDB/server/commit/504eff0ca1)\
  2017-06-28 12:50:18 +0200
  * cleanup: generate\_partition\_syntax()
* [Revision #03c52e964f](https://github.com/MariaDB/server/commit/03c52e964f)\
  2017-06-27 20:44:32 +0200
  * cleanup: move Virtual\_column\_info::print out of Virtual\_column\_info
* [Revision #2bf017c210](https://github.com/MariaDB/server/commit/2bf017c210)\
  2017-06-26 20:06:12 +0200
  * [MDEV-13060](https://jira.mariadb.org/browse/MDEV-13060) Server Audit Plugin Crashes with AWS KMS plugin
* [Revision #47687eef41](https://github.com/MariaDB/server/commit/47687eef41)\
  2017-06-26 16:26:35 +0200
  * [MDEV-12936](https://jira.mariadb.org/browse/MDEV-12936) upgrade to 10.2.6 failed upon tables with virtual columns
* [Revision #75f80004b1](https://github.com/MariaDB/server/commit/75f80004b1)\
  2017-06-25 20:55:58 +0200
  * [MDEV-12939](https://jira.mariadb.org/browse/MDEV-12939) A query crashes MariaDB in Item\_func\_regex::cleanup
* [Revision #7bea860709](https://github.com/MariaDB/server/commit/7bea860709)\
  2017-06-24 14:08:57 +0200
  * [MDEV-12923](https://jira.mariadb.org/browse/MDEV-12923) MyISAM allows CHECK constraint violation in ALTER TABLE
* [Revision #9edfc00697](https://github.com/MariaDB/server/commit/9edfc00697)\
  2017-06-23 18:15:07 +0200
  * [MDEV-11930](https://jira.mariadb.org/browse/MDEV-11930) Unexpected ER\_ERROR\_EVALUATING\_EXPRESSION warning upon dropping database with a bad table
* [Revision #93a95c0a76](https://github.com/MariaDB/server/commit/93a95c0a76)\
  2017-06-23 16:19:40 +0200
  * cleanup: check\_openssl\_compatibility()
* [Revision #a6bef22cda](https://github.com/MariaDB/server/commit/a6bef22cda)\
  2017-06-10 18:08:05 +0200
  * reduce grammar duplication
* [Revision #c917ba1d51](https://github.com/MariaDB/server/commit/c917ba1d51)\
  2017-06-09 14:23:45 +0200
  * fix the comparison in st\_select\_lex::setup\_ref\_array()
* [Revision #5c30fcfa2f](https://github.com/MariaDB/server/commit/5c30fcfa2f)\
  2017-05-31 18:13:00 +0200
  * cleanup: C++ comments
* [Revision #05873ffbf7](https://github.com/MariaDB/server/commit/05873ffbf7)\
  2017-05-15 08:16:34 +0200
  * [MDEV-12795](https://jira.mariadb.org/browse/MDEV-12795) Possibly orphan mysql-test/t/mysql\_plugin-master.opt
* [Revision #32e3b02234](https://github.com/MariaDB/server/commit/32e3b02234)\
  2017-05-11 19:50:33 +0200
  * [MDEV-11639](https://jira.mariadb.org/browse/MDEV-11639) Server crashes in update\_virtual\_field, gcol.innodb\_virtual\_basic fails in buildbot
* [Revision #95e6dd443a](https://github.com/MariaDB/server/commit/95e6dd443a)\
  2017-05-10 01:30:34 +0200
  * crashes when errors on early startup
* [Revision #0e6c6d61c2](https://github.com/MariaDB/server/commit/0e6c6d61c2)\
  2017-06-30 13:37:39 +0200
  * fix main.mdl failure in --embedded
* [Revision #e022c22ba8](https://github.com/MariaDB/server/commit/e022c22ba8)\
  2017-07-04 10:29:49 +0200
  * update sysvar\_server\_embedded.result on 32bit
* [Revision #10a98a4992](https://github.com/MariaDB/server/commit/10a98a4992)\
  2017-07-05 17:22:53 +0300
  * Adjust a test for Windows
* [Revision #4f93c732d5](https://github.com/MariaDB/server/commit/4f93c732d5)\
  2017-06-28 19:39:49 +0300
  * [MDEV-13189](https://jira.mariadb.org/browse/MDEV-13189): Window functions crash when using INTERVAL
* [Revision #e3d3147792](https://github.com/MariaDB/server/commit/e3d3147792)\
  2017-07-05 14:35:55 +0300
  * [MDEV-13105](https://jira.mariadb.org/browse/MDEV-13105) InnoDB fails to load a table with PAGE\_COMPRESSION\_LEVEL after upgrade from 10.1.20
* [Revision #f2931b1e3a](https://github.com/MariaDB/server/commit/f2931b1e3a)\
  2017-07-05 11:33:04 +0000
  * mariadb-backup : run tests on buildbot on Windows
* [Revision #c5a525bda2](https://github.com/MariaDB/server/commit/c5a525bda2)\
  2017-07-05 10:55:36 +0000
  * mariadb-backup : debian packaging
* [Revision #e417af2cb8](https://github.com/MariaDB/server/commit/e417af2cb8)\
  2017-07-05 12:45:15 +0300
  * [MDEV-13143](https://jira.mariadb.org/browse/MDEV-13143) Server crashes in srv\_init\_abort\_low() when started with inaccessible tmpdir
* [Revision #8c71c6aa8b](https://github.com/MariaDB/server/commit/8c71c6aa8b)\
  2017-06-30 10:49:37 +0300
  * [MDEV-12548](https://jira.mariadb.org/browse/MDEV-12548) Initial implementation of mariadb-backup for [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md)
* [Revision #dc722559cc](https://github.com/MariaDB/server/commit/dc722559cc)\
  2017-07-05 10:16:36 +0300
  * Correct a message
* [Revision #15c73c8b4a](https://github.com/MariaDB/server/commit/15c73c8b4a)\
  2017-07-05 10:08:48 +0300
  * Flush crash-unsafe tables before killing the server
* [Revision #6eb1ce048e](https://github.com/MariaDB/server/commit/6eb1ce048e)\
  2017-07-05 08:07:16 +0300
  * Adjust a test for tmp\_disk\_table\_size
* [Revision #41a6475b49](https://github.com/MariaDB/server/commit/41a6475b49)\
  2017-07-03 16:36:06 +0300
  * InnoDB: Use access() instead of open()
* Merge [Revision #06041ade9a](https://github.com/MariaDB/server/commit/06041ade9a) 2017-07-04 16:14:12 +0530 - Merge pull request #397 from MariaDB/bb-10.2-[MDEV-12067](https://jira.mariadb.org/browse/MDEV-12067)
* [Revision #007d3ed905](https://github.com/MariaDB/server/commit/007d3ed905)\
  2017-07-03 14:48:07 +0800
  * [MDEV-12067](https://jira.mariadb.org/browse/MDEV-12067) flashback does not correcly revert update/replace statements
* [Revision #ad2d722acd](https://github.com/MariaDB/server/commit/ad2d722acd)\
  2017-07-03 13:13:54 +0300
  * [MDEV-13228](https://jira.mariadb.org/browse/MDEV-13228): Add a comment that clarifies the constants
* [Revision #d438a448e6](https://github.com/MariaDB/server/commit/d438a448e6)\
  2017-07-03 12:13:01 +0300
  * [MDEV-13228](https://jira.mariadb.org/browse/MDEV-13228) Assertion \`n < rec\_offs\_n\_fields(offsets)' failed in rec\_get\_nth\_field\_offs upon crash recovery with compressed table
* [Revision #56ff6f1b0b](https://github.com/MariaDB/server/commit/56ff6f1b0b)\
  2017-07-03 11:47:54 +0300
  * InnoDB: Remove dead code for DATA\_POINT and DATA\_VAR\_POINT
* [Revision #cf2789bf0b](https://github.com/MariaDB/server/commit/cf2789bf0b)\
  2017-07-03 11:27:53 +0300
  * ha\_innobase::write\_row(): Test the cheaper condition first
* [Revision #92f1837a27](https://github.com/MariaDB/server/commit/92f1837a27)\
  2017-07-01 14:22:49 +0300
  * Fixed compilation warnings (while testing 32 bit builds)
* [Revision #cc8912f223](https://github.com/MariaDB/server/commit/cc8912f223)\
  2017-07-01 14:05:22 +0300
  * Fixed failing test on 32 bit systems
* [Revision #3833097463](https://github.com/MariaDB/server/commit/3833097463)\
  2017-07-01 14:02:29 +0300
  * Clean up BUILD script
* [Revision #2e9b55f763](https://github.com/MariaDB/server/commit/2e9b55f763)\
  2017-07-01 12:00:02 +0300
  * [MDEV-13226](https://jira.mariadb.org/browse/MDEV-13226) Server crashes when tmpdir runs out of space
* [Revision #c436338d9d](https://github.com/MariaDB/server/commit/c436338d9d)\
  2017-06-30 18:51:51 +0300
  * Assert that DB\_TRX\_ID must be set on delete-marked records
* [Revision #53235cbb1f](https://github.com/MariaDB/server/commit/53235cbb1f)\
  2017-06-30 14:58:05 -0700
  * Updated spider/bg and spider/handler mtr suites.
* [Revision #f99b83571a](https://github.com/MariaDB/server/commit/f99b83571a)\
  2017-06-30 18:06:21 +0300
  * Added submodule updates to BUILD scripts
* [Revision #a2d5bd96bf](https://github.com/MariaDB/server/commit/a2d5bd96bf)\
  2017-06-30 18:01:55 +0300
  * Fixed wrong results in show\_all\_plugins.test
* [Revision #b356eae8a9](https://github.com/MariaDB/server/commit/b356eae8a9)\
  2017-06-30 18:00:37 +0300
  * Don't create tags for .xz files
* [Revision #dd8474b1dc](https://github.com/MariaDB/server/commit/dd8474b1dc)\
  2017-06-30 17:56:58 +0300
  * Added tmp\_disk\_table\_size to limit size of Aria temp tables in tmpdir
* [Revision #9f484b63f1](https://github.com/MariaDB/server/commit/9f484b63f1)\
  2017-06-07 17:17:51 +0300
  * Clean up replication check in open\_temporary\_table()
* [Revision #e16425ba97](https://github.com/MariaDB/server/commit/e16425ba97)\
  2017-06-30 18:50:30 +0300
  * Fix a compiler warning
* [Revision #ebe4c65e1d](https://github.com/MariaDB/server/commit/ebe4c65e1d)\
  2017-06-30 18:43:48 +0300
  * Enable more variants of some innodb\_zip tests
* [Revision #f27e1a318c](https://github.com/MariaDB/server/commit/f27e1a318c)\
  2017-06-30 18:39:23 +0300
  * Remove duplicated tests
* [Revision #4877659006](https://github.com/MariaDB/server/commit/4877659006)\
  2017-06-30 15:19:26 +0000
  * [MDEV-12097](https://jira.mariadb.org/browse/MDEV-12097) : avoid too large memory allocation in innodb buffer pool on Windows
* [Revision #bf262bd957](https://github.com/MariaDB/server/commit/bf262bd957)\
  2017-05-24 14:39:27 +0300
  * [MDEV-11649](https://jira.mariadb.org/browse/MDEV-11649) Uninitialized field fts\_token->position in innodb\_fts.innodb\_fts\_plugin
* [Revision #dd75087993](https://github.com/MariaDB/server/commit/dd75087993)\
  2017-06-30 15:03:01 +0300
  * Fix a compilation warning
* [Revision #61847b9d80](https://github.com/MariaDB/server/commit/61847b9d80)\
  2017-06-30 09:31:19 +0300
  * Tablespace: Add iterator, const\_iterator, begin(), end()
* [Revision #5ad4645779](https://github.com/MariaDB/server/commit/5ad4645779)\
  2017-06-30 09:25:39 +0300
  * Adjust a test for the changed innodb\_log\_file\_size limits
* [Revision #9f0c1c0cf6](https://github.com/MariaDB/server/commit/9f0c1c0cf6)\
  2017-06-29 20:50:07 -0700
  * Fixed the bug [MDEV-13193](https://jira.mariadb.org/browse/MDEV-13193).
* [Revision #84e4e4506f](https://github.com/MariaDB/server/commit/84e4e4506f)\
  2017-06-05 22:47:20 +0300
  * Reduce the granularity of innodb\_log\_file\_size
* [Revision #e903d458bb](https://github.com/MariaDB/server/commit/e903d458bb)\
  2017-06-29 23:10:46 +0300
  * Clean up InnoDB shutdown
* [Revision #591edccc93](https://github.com/MariaDB/server/commit/591edccc93)\
  2017-06-29 23:03:39 +0300
  * Simplify access to the binlog offset in InnoDB
* [Revision #aea0e125d2](https://github.com/MariaDB/server/commit/aea0e125d2)\
  2017-06-29 23:01:47 +0300
  * trx\_sys\_read\_wsrep\_checkpoint(): Return whether a checkpoint is present
* [Revision #cd623508df](https://github.com/MariaDB/server/commit/cd623508df)\
  2017-06-29 19:16:07 +0300
  * buf\_read\_ibuf\_merge\_pages(): Discard all entries for a missing tablespace
* [Revision #68b5aeae4e](https://github.com/MariaDB/server/commit/68b5aeae4e)\
  2017-06-29 18:33:18 +0300
  * Minor cleanup of InnoDB I/O routines
* [Revision #859714e73d](https://github.com/MariaDB/server/commit/859714e73d)\
  2017-06-29 22:24:48 +0300
  * Simplify up InnoDB redo log system startup and shutdown
* [Revision #8143ef1b7c](https://github.com/MariaDB/server/commit/8143ef1b7c)\
  2017-06-29 11:33:39 +0300
  * trx\_validate\_state\_before\_free(): Add debug assertions
* [Revision #bb60a832ed](https://github.com/MariaDB/server/commit/bb60a832ed)\
  2017-06-29 11:31:01 +0300
  * Minor cleanup of InnoDB shutdown
* [Revision #de3201df3f](https://github.com/MariaDB/server/commit/de3201df3f)\
  2017-06-29 23:03:30 +0530
  * Fix [MDEV-12758](https://jira.mariadb.org/browse/MDEV-12758)
* [Revision #629c60973d](https://github.com/MariaDB/server/commit/629c60973d)\
  2017-06-29 18:30:39 +0530
  * [MDEV-12758](https://jira.mariadb.org/browse/MDEV-12758) wrep.pool\_of\_threads failed in buildbot with WSREP ...
* [Revision #7c997f4b2e](https://github.com/MariaDB/server/commit/7c997f4b2e)\
  2017-06-29 15:59:17 +1000
  * travis: force deb build not to use ccache
* [Revision #13221b1eb2](https://github.com/MariaDB/server/commit/13221b1eb2)\
  2017-06-28 22:39:21 -0700
  * Fixed a failure of the test case for the bug [MDEV-13107](https://jira.mariadb.org/browse/MDEV-13107) in --ps-protocol.
* [Revision #18a2b0a168](https://github.com/MariaDB/server/commit/18a2b0a168)\
  2017-06-29 14:48:00 +1000
  * travis: disable ccache on deb build - ENOSPC
* [Revision #9e0aa294aa](https://github.com/MariaDB/server/commit/9e0aa294aa)\
  2017-06-29 12:39:42 +1000
  * travis: [MDEV-13002](https://jira.mariadb.org/browse/MDEV-13002) fixed - don't allow failures in MYSQL\_TEST\_SUITES=plugins
* [Revision #9222d79b82](https://github.com/MariaDB/server/commit/9222d79b82)\
  2017-06-29 12:32:43 +1000
  * travis: packages for debian build - added fakeroot
* [Revision #e608023947](https://github.com/MariaDB/server/commit/e608023947)\
  2017-06-28 11:38:26 -0700
  * Fixed the bug [MDEV-13107](https://jira.mariadb.org/browse/MDEV-13107) and some similar unreported bugs.
* [Revision #31ba0fa48d](https://github.com/MariaDB/server/commit/31ba0fa48d)\
  2017-06-28 18:42:56 +0300
  * [MDEV-12851](https://jira.mariadb.org/browse/MDEV-12851): Case with window functions query crashes server
* [Revision #23edc7c88f](https://github.com/MariaDB/server/commit/23edc7c88f)\
  2017-06-27 12:26:38 +0300
  * [MDEV-13186](https://jira.mariadb.org/browse/MDEV-13186): main.win failure post [MDEV-12336](https://jira.mariadb.org/browse/MDEV-12336)
* [Revision #9003869390](https://github.com/MariaDB/server/commit/9003869390)\
  2017-06-18 19:48:57 +0300
  * Simplify IO\_CACHE by removing current\_pos and end\_pos as self-references
* [Revision #b3171607e3](https://github.com/MariaDB/server/commit/b3171607e3)\
  2017-06-28 11:58:43 +0300
  * Avoid InnoDB messages about recovery after creating redo logs
* [Revision #3e1d0ff574](https://github.com/MariaDB/server/commit/3e1d0ff574)\
  2017-06-27 20:53:14 +0300
  * Fix a merge error in commit 8f643e2063c9890a353149f39ef85b2cf3151fd0
* [Revision #29624ea304](https://github.com/MariaDB/server/commit/29624ea304)\
  2017-06-26 16:39:00 +0300
  * [MDEV-13176](https://jira.mariadb.org/browse/MDEV-13176) ALTER TABLE…CHANGE col col TIMESTAMP NOT NULL DEFAULT… fails
* [Revision #02655a91cf](https://github.com/MariaDB/server/commit/02655a91cf)\
  2017-06-26 12:16:04 -0700
  * Fixed the bug [MDEV-13166](https://jira.mariadb.org/browse/MDEV-13166).
* [Revision #6d0aed42c5](https://github.com/MariaDB/server/commit/6d0aed42c5)\
  2017-06-22 17:15:10 +0400
  * [MDEV-12070](https://jira.mariadb.org/browse/MDEV-12070) - Introduce thd\_query\_safe() from MySQL 5.7
* [Revision #dd710e7552](https://github.com/MariaDB/server/commit/dd710e7552)\
  2017-06-22 17:35:36 +0400
  * [MDEV-12882](https://jira.mariadb.org/browse/MDEV-12882) - Assertion failed in MDL\_context::upgrade\_shared\_lock
* [Revision #0d69d313a1](https://github.com/MariaDB/server/commit/0d69d313a1)\
  2017-06-23 22:54:42 +0300
  * Prevent interleaved error log output on InnoDB startup
* [Revision #0288fa619f](https://github.com/MariaDB/server/commit/0288fa619f)\
  2017-06-23 09:46:51 +0300
  * Do allow writes for innodb\_force\_recovery=2 or 3
* [Revision #9f3622191d](https://github.com/MariaDB/server/commit/9f3622191d)\
  2017-06-22 00:41:44 -0700
  * Fixed the bug [MDEV-12845](https://jira.mariadb.org/browse/MDEV-12845).
* [Revision #a8131e71f9](https://github.com/MariaDB/server/commit/a8131e71f9)\
  2017-06-22 21:08:32 +0300
  * [MDEV-12528](https://jira.mariadb.org/browse/MDEV-12528) Run the engine-agnostic test suite on MyRocks
* [Revision #bb857f02d5](https://github.com/MariaDB/server/commit/bb857f02d5)\
  2017-06-22 21:06:31 +0300
  * Test changes to improve stability of results
* [Revision #953de41307](https://github.com/MariaDB/server/commit/953de41307)\
  2017-06-22 13:40:10 +0300
  * trx\_sys\_read\_wsrep\_checkpoint(): Do not write
* [Revision #a133b05cd7](https://github.com/MariaDB/server/commit/a133b05cd7)\
  2017-06-21 12:22:02 +0300
  * Disable more threads on innodb\_force\_recovery=3 or more
* [Revision #064d1a480c](https://github.com/MariaDB/server/commit/064d1a480c)\
  2017-06-22 09:52:02 +0200
  * [MDEV-12579](https://jira.mariadb.org/browse/MDEV-12579): Incorrect arguments to mysqld\_stmt\_execute when using LOBs
* [Revision #557e1bd472](https://github.com/MariaDB/server/commit/557e1bd472)\
  2017-06-21 16:37:48 +0300
  * dict\_create\_or\_check\_sys\_tablespace(): Add some error handling
* [Revision #a71c870ebf](https://github.com/MariaDB/server/commit/a71c870ebf)\
  2017-06-20 15:32:02 +0300
  * InnoDB: Reset unknown TRX\_SYS page type to FIL\_PAGE\_TYPE\_TRX\_SYS
* [Revision #0cf993c24f](https://github.com/MariaDB/server/commit/0cf993c24f)\
  2017-06-21 21:07:20 +0300
  * [MDEV-11002](https://jira.mariadb.org/browse/MDEV-11002) large\_tests.rpl\_slave\_net\_timeout fails due to connection logging
* [Revision #0992be927e](https://github.com/MariaDB/server/commit/0992be927e)\
  2017-06-16 10:12:14 +0300
  * [MDEV-13068](https://jira.mariadb.org/browse/MDEV-13068) Crash in Item::split\_sum\_func2 with INSERT SELECT using window functions
* Merge [Revision #c73fa2d75f](https://github.com/MariaDB/server/commit/c73fa2d75f) 2017-06-19 16:46:34 +0300 - Merge 10.1 into 10.2
* [Revision #d1e182d603](https://github.com/MariaDB/server/commit/d1e182d603)\
  2017-06-19 15:59:19 +0300
  * [MDEV-12975](https://jira.mariadb.org/browse/MDEV-12975) InnoDB redo log minimum size check uses detected file size instead of requested innodb\_log\_file\_size
* [Revision #9a646c91dd](https://github.com/MariaDB/server/commit/9a646c91dd)\
  2017-05-29 14:24:18 +0300
  * mariadb-backup: Remove the --stats option
* [Revision #cede2b6f0f](https://github.com/MariaDB/server/commit/cede2b6f0f)\
  2017-05-26 12:13:48 +0300
  * mariadb-backup: Remove support for .xbcrypt files
* [Revision #7e22050e66](https://github.com/MariaDB/server/commit/7e22050e66)\
  2017-05-26 12:38:32 +0300
  * mariadb-backup: Remove the options --compact --rebuild-indexes --rebuild-threads
* [Revision #fa70d077f7](https://github.com/MariaDB/server/commit/fa70d077f7)\
  2017-05-26 12:51:11 +0300
  * mariadb-backup: Remove the options --to-archived-lsn --innodb-log-arch-dir
* [Revision #056bab0880](https://github.com/MariaDB/server/commit/056bab0880)\
  2017-06-16 15:47:46 +0400
  * [MDEV-12620](https://jira.mariadb.org/browse/MDEV-12620) - set lock\_wait\_timeout = 1;flush tables with read lock; lock not released after timeout
* [Revision #cf4a6abea1](https://github.com/MariaDB/server/commit/cf4a6abea1)\
  2017-06-15 14:43:22 -0700
  * Fixed the bug [MDEV-13064](https://jira.mariadb.org/browse/MDEV-13064).
* [Revision #f73507e685](https://github.com/MariaDB/server/commit/f73507e685)\
  2017-06-16 18:37:38 +0200
  * result fix
* [Revision #50faeda4d6](https://github.com/MariaDB/server/commit/50faeda4d6)\
  2017-06-16 12:21:46 +0300
  * Remove trx\_t::has\_search\_latch and simplify debug code
* [Revision #e5980bf1b1](https://github.com/MariaDB/server/commit/e5980bf1b1)\
  2017-06-16 11:05:09 +0300
  * Remove the unnecessary method handlerton::release\_temporary\_latches()
* [Revision #6b71b3e348](https://github.com/MariaDB/server/commit/6b71b3e348)\
  2017-06-15 17:42:49 +0300
  * Follow-up to [MDEV-12873](https://jira.mariadb.org/browse/MDEV-12873): Refactor SYS\_TABLES.TYPE validation
* Merge [Revision #615b1f4189](https://github.com/MariaDB/server/commit/615b1f4189) 2017-06-15 14:35:51 +0300 - Merge 10.1 into 10.2
* [Revision #58f87a41bd](https://github.com/MariaDB/server/commit/58f87a41bd)\
  2017-06-15 12:41:02 +0300
  * Remove some fields from dict\_table\_t
* [Revision #88b961816e](https://github.com/MariaDB/server/commit/88b961816e)\
  2017-06-15 12:40:24 +0300
  * Re-record a failing test, likely related to [MDEV-12610](https://jira.mariadb.org/browse/MDEV-12610)
* Merge [Revision #9ed325efc1](https://github.com/MariaDB/server/commit/9ed325efc1) 2017-06-13 18:29:40 +0300 - Merge 10.0 into 10.1, plus fixup for [MDEV-12873](https://jira.mariadb.org/browse/MDEV-12873)
* [Revision #1d5a306e38](https://github.com/MariaDB/server/commit/1d5a306e38)\
  2017-06-13 16:20:21 +0300
  * [MDEV-12873](https://jira.mariadb.org/browse/MDEV-12873) InnoDB SYS\_TABLES.TYPE incompatibility for PAGE\_COMPRESSION in [MariaDB 10.2.2](../../old-releases/10.2/10.2.2.md) to 10.2.6
* [Revision #74e4cf70d0](https://github.com/MariaDB/server/commit/74e4cf70d0)\
  2017-06-12 18:43:23 +0000
  * [MDEV-13059](https://jira.mariadb.org/browse/MDEV-13059) XtraDB hangs on Windows due to failing to release block->lock X-latch in innodb\_read\_only mode.
* [Revision #9f0ed6c67e](https://github.com/MariaDB/server/commit/9f0ed6c67e)\
  2017-06-13 17:21:15 +0300
  * [MDEV-13009](https://jira.mariadb.org/browse/MDEV-13009) 10.1.24 does not compile on architectures without 64-bit atomics
* [Revision #72378a2583](https://github.com/MariaDB/server/commit/72378a2583)\
  2017-06-14 14:08:49 +0300
  * [MDEV-12873](https://jira.mariadb.org/browse/MDEV-12873) InnoDB SYS\_TABLES.TYPE incompatibility for PAGE\_COMPRESSED=YES in [MariaDB 10.2.2](../../old-releases/10.2/10.2.2.md) to 10.2.6
* [Revision #227bfe4466](https://github.com/MariaDB/server/commit/227bfe4466)\
  2017-06-14 14:39:51 +0200
  * new connector version which correspond BULK command
* [Revision #91ae1258ee](https://github.com/MariaDB/server/commit/91ae1258ee)\
  2017-04-07 15:38:01 +0200
  * [MDEV-12471](https://jira.mariadb.org/browse/MDEV-12471): BULK Command
* [Revision #e813fe8622](https://github.com/MariaDB/server/commit/e813fe8622)\
  2017-06-13 23:04:01 +0300
  * [MDEV-13084](https://jira.mariadb.org/browse/MDEV-13084) [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) crashes on corrupted SYS\_TABLES.MIX\_LEN field
* [Revision #a4efeabc43](https://github.com/MariaDB/server/commit/a4efeabc43)\
  2017-06-12 19:09:04 +0300
  * [MDEV-13061](https://jira.mariadb.org/browse/MDEV-13061) innodb\_encrypt\_log recovery is spamming the error log
* [Revision #35248fed10](https://github.com/MariaDB/server/commit/35248fed10)\
  2017-06-08 15:43:06 +0300
  * 10.2 follow-up to [MDEV-13039](https://jira.mariadb.org/browse/MDEV-13039) innodb\_fast\_shutdown=0 crash due premature purge shutdown before fts\_optimize\_shutdown()
* Merge [Revision #a78476d342](https://github.com/MariaDB/server/commit/a78476d342) 2017-06-12 17:43:07 +0300 - Merge 10.1 into 10.2
* [Revision #3976ec1e83](https://github.com/MariaDB/server/commit/3976ec1e83)\
  2017-06-09 17:22:59 +0300
  * [MDEV-13043](https://jira.mariadb.org/browse/MDEV-13043) Skipped tests ignore warning suppressions
* [Revision #3005cebc96](https://github.com/MariaDB/server/commit/3005cebc96)\
  2017-06-12 17:10:56 +0300
  * Post-push fix for [MDEV-12610](https://jira.mariadb.org/browse/MDEV-12610) MariaDB start is slow
* [Revision #757339efd0](https://github.com/MariaDB/server/commit/757339efd0)\
  2017-06-12 17:09:44 +0300
  * Adjust a test result after merge
* Merge [Revision #fa57479fcd](https://github.com/MariaDB/server/commit/fa57479fcd) 2017-06-12 14:26:32 +0300 - Merge 10.0 into 10.1
* [Revision #75b35a3b68](https://github.com/MariaDB/server/commit/75b35a3b68)\
  2017-06-12 14:10:39 +0300
  * Partially disable a test affected by [MDEV-13059](https://jira.mariadb.org/browse/MDEV-13059)
* [Revision #4325041df6](https://github.com/MariaDB/server/commit/4325041df6)\
  2017-06-12 11:08:06 +0300
  * [MDEV-13057](https://jira.mariadb.org/browse/MDEV-13057) innodb\_read\_only=1 should avoid creating buf\_flush\_page\_cleaner\_thread
* [Revision #417434f12d](https://github.com/MariaDB/server/commit/417434f12d)\
  2017-06-08 15:43:06 +0300
  * [MDEV-13039](https://jira.mariadb.org/browse/MDEV-13039) innodb\_fast\_shutdown=0 may fail to purge all undo log
* [Revision #a9117c9008](https://github.com/MariaDB/server/commit/a9117c9008)\
  2017-06-09 13:44:04 +0300
  * Correct a merge error of [MDEV-11626](https://jira.mariadb.org/browse/MDEV-11626)
* [Revision #d03abc71a4](https://github.com/MariaDB/server/commit/d03abc71a4)\
  2017-06-08 10:34:10 +0300
  * [MDEV-12609](https://jira.mariadb.org/browse/MDEV-12609): Allow suppression of InnoDB log messages about reserving extents
* [Revision #58c56dd7f8](https://github.com/MariaDB/server/commit/58c56dd7f8)\
  2017-06-08 15:40:25 +0300
  * [MDEV-12610](https://jira.mariadb.org/browse/MDEV-12610): MariaDB start is slow
* [Revision #7a12894de1](https://github.com/MariaDB/server/commit/7a12894de1)\
  2017-06-10 16:39:39 -0700
  * Fixed the bug mdev12992.
* [Revision #b175c41cde](https://github.com/MariaDB/server/commit/b175c41cde)\
  2017-06-10 12:57:59 +0530
  * [MDEV-9544](https://jira.mariadb.org/browse/MDEV-9544) Fix test case for 10.2
* Merge [Revision #2d8fdfbde5](https://github.com/MariaDB/server/commit/2d8fdfbde5) 2017-06-08 12:45:08 +0300 - Merge 10.1 into 10.2
* [Revision #fbeb9489cd](https://github.com/MariaDB/server/commit/fbeb9489cd)\
  2017-06-06 14:59:42 +0300
  * Cleanup of [MDEV-12600](https://jira.mariadb.org/browse/MDEV-12600): crash during install\_db with innodb\_page\_size=32K and ibdata1=3M
* [Revision #68890fe7d4](https://github.com/MariaDB/server/commit/68890fe7d4)\
  2017-06-06 15:24:43 +0300
  * Revert part of [MDEV-12113](https://jira.mariadb.org/browse/MDEV-12113)
* Merge [Revision #18f62d94d6](https://github.com/MariaDB/server/commit/18f62d94d6) 2017-06-08 08:18:38 +0300 - Merge pull request #404 from grooverdan/10.1-[MDEV-13032](https://jira.mariadb.org/browse/MDEV-13032)-galera\_new\_cluster
* [Revision #d8515829ec](https://github.com/MariaDB/server/commit/d8515829ec)\
  2017-06-08 12:43:39 +1000
  * [MDEV-13032](https://jira.mariadb.org/browse/MDEV-13032): fix galera\_new\_cluster to be POSIX
* [Revision #6439238c53](https://github.com/MariaDB/server/commit/6439238c53)\
  2017-06-06 14:57:20 +0300
  * Correct a merge error
* Merge [Revision #30df297c2f](https://github.com/MariaDB/server/commit/30df297c2f) 2017-06-06 09:54:57 +0300 - Merge 10.0 into 10.1
* [Revision #d8d39721df](https://github.com/MariaDB/server/commit/d8d39721df)\
  2017-06-06 09:34:09 +0300
  * Follow-up to [MDEV-12042](https://jira.mariadb.org/browse/MDEV-12042) (test innodb\_page\_size variants)
* [Revision #151daaf480](https://github.com/MariaDB/server/commit/151daaf480)\
  2017-06-05 15:16:15 +0300
  * [MDEV-12994](https://jira.mariadb.org/browse/MDEV-12994) innodb\_fast\_shutdown=0 skips change buffer merge; fast shutdown does it
* [Revision #ab62b7538f](https://github.com/MariaDB/server/commit/ab62b7538f)\
  2017-06-02 01:46:25 +0300
  * [MDEV-12042](https://jira.mariadb.org/browse/MDEV-12042) Re-bootstrap the server if InnoDB options are incompatible
* Merge [Revision #c2ef0bb6ce](https://github.com/MariaDB/server/commit/c2ef0bb6ce) 2017-05-29 13:15:36 +0300 - Merge 5.5 into 10.0
* [Revision #2cb94aa1b7](https://github.com/MariaDB/server/commit/2cb94aa1b7)\
  2017-05-29 13:07:23 +0300
  * [MDEV-11626](https://jira.mariadb.org/browse/MDEV-11626) innodb.innodb-change-buffer-recovery fails for xtradb
* [Revision #b8405c853f](https://github.com/MariaDB/server/commit/b8405c853f)\
  2017-05-22 07:09:49 +0200
  * [MDEV-11958](https://jira.mariadb.org/browse/MDEV-11958): LEFT JOIN with stored routine produces incorrect result
* [Revision #da61107fc8](https://github.com/MariaDB/server/commit/da61107fc8)\
  2017-06-05 13:10:24 +0530
  * [MDEV-9544](https://jira.mariadb.org/browse/MDEV-9544) FLUSH \[RELAY] LOGS does not rotate logs for a named slave
* [Revision #112b21da37](https://github.com/MariaDB/server/commit/112b21da37)\
  2017-05-30 11:55:11 +0300
  * [MDEV-12600](https://jira.mariadb.org/browse/MDEV-12600): crash during install\_db with innodb\_page\_size=32K and ibdata1=3M;
* [Revision #6b6987154a](https://github.com/MariaDB/server/commit/6b6987154a)\
  2017-05-30 12:02:42 +0300
  * [MDEV-12114](https://jira.mariadb.org/browse/MDEV-12114): install\_db shows corruption for rest encryption and innodb\_checksum\_algorithm=strict\_none
* [Revision #1af8bf39ca](https://github.com/MariaDB/server/commit/1af8bf39ca)\
  2017-05-30 11:30:43 +0300
  * [MDEV-12113](https://jira.mariadb.org/browse/MDEV-12113): install\_db shows corruption for rest encryption with innodb\_data\_file\_path=ibdata1:3M;
* [Revision #473f4a65e1](https://github.com/MariaDB/server/commit/473f4a65e1)\
  2017-05-31 11:39:21 -0400
  * bump the VERSION
* [Revision #5e0038b376](https://github.com/MariaDB/server/commit/5e0038b376)\
  2017-05-29 20:57:34 +0200
  * cleanup: remove Regexp\_processor\_pcre::m\_subpatterns\_needed
* [Revision #2372bfaa7b](https://github.com/MariaDB/server/commit/2372bfaa7b)\
  2017-05-29 20:49:36 +0200
  * [MDEV-12942](https://jira.mariadb.org/browse/MDEV-12942) REGEXP\_INSTR returns 1 when using brackets
* [Revision #af4421e82d](https://github.com/MariaDB/server/commit/af4421e82d)\
  2017-05-29 00:27:14 -0700
  * Fixed the bug [MDEV-12931](https://jira.mariadb.org/browse/MDEV-12931).
* [Revision #e4d10e09cf](https://github.com/MariaDB/server/commit/e4d10e09cf)\
  2017-05-28 00:40:36 +0530
  * [MDEV-11196](https://jira.mariadb.org/browse/MDEV-11196): Error:Run-Time Check Failure #2 - Stack around the variable 'key\_buff' was corrupted, server crashes in opt\_sum\_query
* Merge [Revision #f42e08f951](https://github.com/MariaDB/server/commit/f42e08f951) 2017-05-26 19:21:19 +0200 - Merge branch '10.0-galera' into 10.1
* [Revision #0e3170e30d](https://github.com/MariaDB/server/commit/0e3170e30d)\
  2017-05-08 16:29:41 +0530
  * Fix galera tests part II(Fix previous commit)
* [Revision #10d7a2f8e0](https://github.com/MariaDB/server/commit/10d7a2f8e0)\
  2017-05-08 16:00:23 +0530
  * Fix galera test failures.
* [Revision #e4a52670f4](https://github.com/MariaDB/server/commit/e4a52670f4)\
  2017-04-05 08:54:20 +0300
  * fix warning "ignoring return value" of fwrite.
* [Revision #09b28b3d10](https://github.com/MariaDB/server/commit/09b28b3d10)\
  2017-04-05 14:35:41 +0300
  * Fix compiler warnings on gcc 6.x.
* Merge [Revision #4b1cf0bba6](https://github.com/MariaDB/server/commit/4b1cf0bba6) 2017-04-05 08:14:18 +0300 - Merge pull request #351 from grooverdan/10.0-galera-[MDEV-7560](https://jira.mariadb.org/browse/MDEV-7560)-check\_galera\_version
* [Revision #5dca5b8007](https://github.com/MariaDB/server/commit/5dca5b8007)\
  2017-03-30 15:02:30 +1100
  * [MDEV-7560](https://jira.mariadb.org/browse/MDEV-7560): check\_galera\_version to account for greater version than specified
* [Revision #d95dc57e75](https://github.com/MariaDB/server/commit/d95dc57e75)\
  2017-03-23 13:18:29 +0530
  * Fix galera.galera\_gcs\_fc\_limit
* [Revision #bb20f6d9e2](https://github.com/MariaDB/server/commit/bb20f6d9e2)\
  2017-03-23 10:26:55 +0530
  * [MDEV-12319](https://jira.mariadb.org/browse/MDEV-12319) Part 2
* [Revision #a136c36781](https://github.com/MariaDB/server/commit/a136c36781)\
  2017-03-22 10:19:06 -0400
  * bump the VERSION
* [Revision #4eb29ecfab](https://github.com/MariaDB/server/commit/4eb29ecfab)\
  2017-03-22 09:40:57 +0530
  * [MDEV-12319](https://jira.mariadb.org/browse/MDEV-12319) Test added to disabled.def
* [Revision #656d0f10e5](https://github.com/MariaDB/server/commit/656d0f10e5)\
  2017-03-21 14:23:45 +0530
  * Fix galera\_admin test
* [Revision #b22026ddfd](https://github.com/MariaDB/server/commit/b22026ddfd)\
  2017-03-21 10:00:02 +0200
  * Fix failure on galera\_toi\_drop\_database test.
* [Revision #0759c9baf5](https://github.com/MariaDB/server/commit/0759c9baf5)\
  2017-03-21 12:14:19 +0530
  * Fix mysqlhotcopy test failures
* [Revision #0b51dee0e3](https://github.com/MariaDB/server/commit/0b51dee0e3)\
  2017-03-20 18:52:18 +0530
  * Change VERSION no to 30
* Merge [Revision #9cf499724f](https://github.com/MariaDB/server/commit/9cf499724f) 2017-03-20 18:11:56 +0530 - Merge branch '10.0' into bb-10.0-galera
* [Revision #53c6195eed](https://github.com/MariaDB/server/commit/53c6195eed)\
  2017-03-20 10:17:13 +0200
  * Fixed test failure on galere\_wsrep\_log\_conflicts on XtraDB.
* Merge [Revision #f66395f7c0](https://github.com/MariaDB/server/commit/f66395f7c0) 2017-03-17 02:05:20 +0530 - Merge tag 'mariadb-10.0.30' into bb-sachin-10.0-galera-merge
* [Revision #c401773c8d](https://github.com/MariaDB/server/commit/c401773c8d)\
  2017-03-16 08:07:58 +0530
  * Fix test cases
* [Revision #5bb7653667](https://github.com/MariaDB/server/commit/5bb7653667)\
  2017-03-16 02:13:31 +0530
  * Fix wsrep\_affected\_rows.
* [Revision #1743d68868](https://github.com/MariaDB/server/commit/1743d68868)\
  2017-03-14 18:41:38 +0530
  * Fix Some failing tests
* [Revision #25070d2a2c](https://github.com/MariaDB/server/commit/25070d2a2c)\
  2017-01-25 09:58:07 +0200
  * Bump WSREP\_PATCH\_VERSION to 19
* [Revision #ad7b00fb90](https://github.com/MariaDB/server/commit/ad7b00fb90)\
  2017-03-14 16:17:28 +0530
  * Galera MTR Tests: do not run innodb.innodb\_stats\_del\_mark and some other tests with Galera, as it produces warnings
* [Revision #69b5bd7ae3](https://github.com/MariaDB/server/commit/69b5bd7ae3)\
  2016-12-16 02:30:09 -0800
  * Galera MTR Tests: Tests for MW-328 Fix unnecessary/silent BF aborts
* [Revision #dd2f023427](https://github.com/MariaDB/server/commit/dd2f023427)\
  2016-12-15 01:22:44 -0800
  * Galera MTR Tests: restore galera\_autoinc\_sst\_xtrabackup.test to use xtrabackup SST
* [Revision #5ac0d5fc24](https://github.com/MariaDB/server/commit/5ac0d5fc24)\
  2016-12-08 05:15:31 -0800
  * Galera MTR Tests: Stability fix for MW-329
* [Revision #17f716062d](https://github.com/MariaDB/server/commit/17f716062d)\
  2016-12-08 00:17:28 -0800
  * Galera MTR Tests: Test for MW-329 Fix incorrect affected rows count after replay
* [Revision #00f1ed6655](https://github.com/MariaDB/server/commit/00f1ed6655)\
  2017-03-14 14:42:52 +0530
  * Galera MTR Tests: fix variable output in galera\_as\_slave\_gtid\_replicate\_do\_db.result
* [Revision #f29c40d0a5](https://github.com/MariaDB/server/commit/f29c40d0a5)\
  2017-03-14 14:31:13 +0530
  * [GAL-480](https://github.com/codership/galera/issues/480) MTR test
* [Revision #6fabf12ba0](https://github.com/MariaDB/server/commit/6fabf12ba0)\
  2016-11-23 02:55:36 -0800
  * Galera MTR Test: Test for MW-28 : Assertion with --wsrep-log-conflicts
* [Revision #0e0ae0bb06](https://github.com/MariaDB/server/commit/0e0ae0bb06)\
  2017-03-14 13:13:22 +0530
  * MW-28, codership/mysql-wsrep#28 Fix sync\_thread\_levels debug assert
* [Revision #471dd11381](https://github.com/MariaDB/server/commit/471dd11381)\
  2016-11-21 10:38:20 +0200
  * refs: MW-319 \* silenced the WSREP\_ERROR, this fires for all replication filtered DDL, and is false positive
* [Revision #c49bfff992](https://github.com/MariaDB/server/commit/c49bfff992)\
  2017-03-14 11:21:16 +0530
  * Galera MTR tests: Make the mysqlhotcopy tests pass on Ubuntu 16.04
* [Revision #e29d7b1d0b](https://github.com/MariaDB/server/commit/e29d7b1d0b)\
  2016-11-08 15:19:37 +0200
  * Bump WSREP\_PATCH\_VERSION to 18
* [Revision #f78332c581](https://github.com/MariaDB/server/commit/f78332c581)\
  2016-11-05 09:15:14 -0700
  * Galera MTR Tests: stability fix for galera#414.test
* [Revision #64bb59fce9](https://github.com/MariaDB/server/commit/64bb59fce9)\
  2017-03-14 11:19:03 +0530
  * Galera MTR Tests: stability fixes
* [Revision #451bf7243a](https://github.com/MariaDB/server/commit/451bf7243a)\
  2016-11-04 01:33:54 -0700
  * Galera MTR Tests: Test for MW-313 Enforce wsrep\_max\_ws\_rows also when binlog is enabled
* [Revision #9dda6cb08d](https://github.com/MariaDB/server/commit/9dda6cb08d)\
  2016-11-03 16:04:22 +0100
  * MW-313 Enforce wsrep\_max\_ws\_rows also when binlog is enabled
* [Revision #395c420f0f](https://github.com/MariaDB/server/commit/395c420f0f)\
  2016-11-03 04:05:05 -0700
  * Galera MTR Tests: MW-305 , re-enable the test for ALTER USER
* [Revision #0a06347333](https://github.com/MariaDB/server/commit/0a06347333)\
  2016-11-03 00:49:20 -0700
  * Galera MTR Tests: Test for MW-309 - Fix wsrep\_max\_ws\_rows so that it does not affect SELECT queries
* [Revision #5d9c747193](https://github.com/MariaDB/server/commit/5d9c747193)\
  2016-11-02 07:04:34 -0700
  * Galera MTR tests: Update galera\_defaults.result for [GAL-360](https://github.com/codership/galera/issues/360)
* [Revision #16e683fdad](https://github.com/MariaDB/server/commit/16e683fdad)\
  2017-03-14 07:11:17 +0530
  * Galera MTR Tests: Tests for [GAL-419](https://github.com/codership/galera/issues/419) Respect safe\_to\_bootstrap flag also with gcomm:
* [Revision #108fd77486](https://github.com/MariaDB/server/commit/108fd77486)\
  2016-11-02 02:01:10 -0700
  * Galera MTR Tests: [GAL-405](https://github.com/codership/galera/issues/405) Initial implementation of GCache recovery on startup.
* [Revision #9be994ba69](https://github.com/MariaDB/server/commit/9be994ba69)\
  2017-03-13 05:30:02 +0530
  * MW-309 Fix wsrep\_max\_ws\_rows so that it does not affect queries
* [Revision #4573924f7d](https://github.com/MariaDB/server/commit/4573924f7d)\
  2017-03-12 23:00:20 +0530
  * Galera MTR Tests: MW-308 , MW-307, GCF-992
* [Revision #c2eaae268d](https://github.com/MariaDB/server/commit/c2eaae268d)\
  2016-10-11 03:37:42 -0700
  * Galera MTR Tests: GCF-981 - galera\_bf\_abort is non deterministic
* [Revision #0e105bc1f2](https://github.com/MariaDB/server/commit/0e105bc1f2)\
  2016-10-03 03:09:49 -0700
  * Galera MTR Tests: Test for GCF-942 - safe\_to\_bootstrap flag in grastate.dat
* [Revision #15298689cb](https://github.com/MariaDB/server/commit/15298689cb)\
  2016-09-14 14:33:59 +0300
  * Bump WSREP\_PATCH\_VERSION to 17
* [Revision #86ec6c221a](https://github.com/MariaDB/server/commit/86ec6c221a)\
  2017-03-12 13:56:29 +0530
  * MW-267: followup to the original pull request, removed unnecessary cast.
* [Revision #3045b60f0f](https://github.com/MariaDB/server/commit/3045b60f0f)\
  2016-08-20 13:42:11 +0200
  * [GAL-401](https://github.com/codership/galera/issues/401): MTR test for the fix.
* [Revision #8c35f105d2](https://github.com/MariaDB/server/commit/8c35f105d2)\
  2017-05-26 19:54:09 +0300
  * Latest additions to the list of unstable tests in 10.1.24
* [Revision #994a5f29f1](https://github.com/MariaDB/server/commit/994a5f29f1)\
  2017-05-26 19:53:29 +0300
  * On a build without performance schema the test failed
* [Revision #c4cbc7a880](https://github.com/MariaDB/server/commit/c4cbc7a880)\
  2017-06-08 14:29:04 +1000
  * travis: allowed\_failures MYSQL\_TEST\_SUITES=plugins ([MDEV-13002](https://jira.mariadb.org/browse/MDEV-13002))
* [Revision #798db3d710](https://github.com/MariaDB/server/commit/798db3d710)\
  2017-06-08 14:01:19 +1000
  * travis: allow\_failures os: osx
* [Revision #035f74c36c](https://github.com/MariaDB/server/commit/035f74c36c)\
  2017-06-08 13:41:50 +1000
  * travis: enable (main,archive).mysqlhotcopy\_\1 test
* [Revision #bb1f41423a](https://github.com/MariaDB/server/commit/bb1f41423a)\
  2017-06-02 16:04:50 +0300
  * InnoDB: Remove thread\_mutex
* [Revision #86927cc712](https://github.com/MariaDB/server/commit/86927cc712)\
  2017-05-26 14:04:19 +0300
  * Remove traces of multiple InnoDB redo logs
* [Revision #ed2976caf0](https://github.com/MariaDB/server/commit/ed2976caf0)\
  2017-06-05 13:13:42 +0300
  * Remove an orphan declaration lock\_rec\_enqueue\_waiting()
* [Revision #da9c30a7b0](https://github.com/MariaDB/server/commit/da9c30a7b0)\
  2017-05-31 14:42:55 +0300
  * Remove unused declarations
* [Revision #6e0e5eefbc](https://github.com/MariaDB/server/commit/6e0e5eefbc)\
  2017-06-06 11:50:42 +0300
  * Fix some printf format type mismatch
* [Revision #22fa9f22aa](https://github.com/MariaDB/server/commit/22fa9f22aa)\
  2017-06-06 14:52:06 +1000
  * travis: add uuid-dev as dependency
* [Revision #cc7e349012](https://github.com/MariaDB/server/commit/cc7e349012)\
  2017-06-03 02:48:47 +0300
  * [MDEV-12764](https://jira.mariadb.org/browse/MDEV-12764) main.log\_tables-big fails in buildbot due to connect\_log
* [Revision #36e020a5d6](https://github.com/MariaDB/server/commit/36e020a5d6)\
  2017-06-03 02:47:52 +0300
  * Adjust storage\_engine suite according to server changes in 10.2
* [Revision #aad8cefd2d](https://github.com/MariaDB/server/commit/aad8cefd2d)\
  2017-06-01 14:08:41 +0300
  * Enable innodb\_encryption-page-compression test.
* [Revision #22e5e64c0d](https://github.com/MariaDB/server/commit/22e5e64c0d)\
  2017-05-29 14:16:57 +0300
  * [MDEV-11623](https://jira.mariadb.org/browse/MDEV-11623) merge fix: Use the correct flags in an error message
* Merge [Revision #959195e195](https://github.com/MariaDB/server/commit/959195e195) 2017-05-29 08:46:26 +0300 - Merge pull request #399 from grooverdan/10.2-[MDEV-12924](https://jira.mariadb.org/browse/MDEV-12924)-readd-numa-innodb
* [Revision #b53f6b9768](https://github.com/MariaDB/server/commit/b53f6b9768)\
  2017-05-29 15:30:21 +1000
  * [MDEV-12924](https://jira.mariadb.org/browse/MDEV-12924): re-add numa to innodb
* [Revision #73deafbc17](https://github.com/MariaDB/server/commit/73deafbc17)\
  2017-05-18 15:45:05 +0300
  * Remove dict\_index\_t::is\_ngram
* [Revision #c0dec39da0](https://github.com/MariaDB/server/commit/c0dec39da0)\
  2017-05-24 15:20:35 +0300
  * fts\_is\_charset\_cjk(): Do not call strcmp()
* [Revision #e54d521b66](https://github.com/MariaDB/server/commit/e54d521b66)\
  2017-05-24 14:07:41 +0300
  * Remove some noise from ib::fatal() and ib::fatal\_or\_error()
* [Revision #2fd840011c](https://github.com/MariaDB/server/commit/2fd840011c)\
  2017-05-24 13:30:01 +0300
  * Remove ut\_allocator::m\_oom\_fatal
* [Revision #acea8b5bad](https://github.com/MariaDB/server/commit/acea8b5bad)\
  2017-05-24 11:03:13 +0300
  * Fix some integer type mismatch in innochecksum
* [Revision #3b68515bf2](https://github.com/MariaDB/server/commit/3b68515bf2)\
  2017-05-24 13:25:27 +0300
  * Actually enable UNIV\_DEBUG\_VALGRIND
* [Revision #e32dc40c50](https://github.com/MariaDB/server/commit/e32dc40c50)\
  2017-05-24 12:42:25 +0300
  * Remove an unused variable
* [Revision #4114d1d452](https://github.com/MariaDB/server/commit/4114d1d452)\
  2017-05-24 11:05:41 +0300
  * Fix WITH\_INNODB\_EXTRA\_DEBUG
* Merge [Revision #8c81f24d1b](https://github.com/MariaDB/server/commit/8c81f24d1b) 2017-05-26 22:44:16 +0300 - Merge 10.1 into 10.2
* [Revision #808f18c748](https://github.com/MariaDB/server/commit/808f18c748)\
  2017-05-26 19:13:21 +0300
  * [MDEV-12926](https://jira.mariadb.org/browse/MDEV-12926) encryption.innodb\_onlinealter\_encryption, encryption.innodb-bad-key-change failed in buildbot with valgrind
* [Revision #2f29fc3c1c](https://github.com/MariaDB/server/commit/2f29fc3c1c)\
  2017-05-23 12:17:43 +0300
  * 10.1 additions for [MDEV-12052](https://jira.mariadb.org/browse/MDEV-12052) Shutdown crash presumably due to master thread activity
* Merge [Revision #4abc2dd0c7](https://github.com/MariaDB/server/commit/4abc2dd0c7) 2017-05-26 15:11:23 +0300 - Merge 10.0 to 10.1
* [Revision #449a88e1c6](https://github.com/MariaDB/server/commit/449a88e1c6)\
  2017-05-23 12:17:43 +0300
  * [MDEV-12052](https://jira.mariadb.org/browse/MDEV-12052) Shutdown crash presumably due to master thread activity
* [Revision #fde86fc1ed](https://github.com/MariaDB/server/commit/fde86fc1ed)\
  2017-05-23 09:21:28 -0400
  * bump the VERSION
* [Revision #70630e3c92](https://github.com/MariaDB/server/commit/70630e3c92)\
  2017-05-19 15:55:35 +0000
  * Workaround dependency problems (constant rebuilds) in Visual Studio generator
* [Revision #6bc9949210](https://github.com/MariaDB/server/commit/6bc9949210)\
  2017-05-24 20:38:40 +0300
  * Updated list of unstable tests for 10.1.24 release
* [Revision #b430133bb9](https://github.com/MariaDB/server/commit/b430133bb9)\
  2017-05-23 15:35:32 +0200
  * [MDEV-12844](https://jira.mariadb.org/browse/MDEV-12844) numerous issues in MASTER\_GTID\_WAIT()
* [Revision #fc89f5fd40](https://github.com/MariaDB/server/commit/fc89f5fd40)\
  2017-05-20 19:14:06 +0200
  * [MDEV-11335](https://jira.mariadb.org/browse/MDEV-11335) Changing delay\_key\_write option for MyISAM table should not copy rows
* [Revision #c65dd3668b](https://github.com/MariaDB/server/commit/c65dd3668b)\
  2017-05-22 11:02:15 +0200
  * de-obfuscate sys\_vars.delay\_key\_write\_func test
* [Revision #ae76ff4524](https://github.com/MariaDB/server/commit/ae76ff4524)\
  2017-05-22 09:34:39 +0200
  * compiler warning on Win64
* [Revision #ad807aebde](https://github.com/MariaDB/server/commit/ad807aebde)\
  2017-05-21 18:10:33 +0200
  * [MDEV-12612](https://jira.mariadb.org/browse/MDEV-12612) mysqladmin --local flush... to use FLUSH LOCAL
* [Revision #7e0c8fc3fb](https://github.com/MariaDB/server/commit/7e0c8fc3fb)\
  2017-05-21 16:21:15 +0200
  * [MDEV-12389](https://jira.mariadb.org/browse/MDEV-12389) ADD CHECK leaves an orphaned .par file
* [Revision #152aec019d](https://github.com/MariaDB/server/commit/152aec019d)\
  2017-05-21 13:19:38 +0200
  * [MDEV-11650](https://jira.mariadb.org/browse/MDEV-11650) plugins.cracklib\_password\_check, plugins.two\_password\_validations fail in buildbot with valgrind (Conditional jump or move depends on uninitialised value)
* [Revision #fdc1fd6f49](https://github.com/MariaDB/server/commit/fdc1fd6f49)\
  2017-05-20 14:04:03 +0200
  * [MDEV-11311](https://jira.mariadb.org/browse/MDEV-11311) Create federated table does not work as expected.
* [Revision #54caaf6848](https://github.com/MariaDB/server/commit/54caaf6848)\
  2017-05-20 12:32:10 +0200
  * [MDEV-10940](https://jira.mariadb.org/browse/MDEV-10940) plugins.pam still fails in buildbot with valgrind
* [Revision #7e0f40b333](https://github.com/MariaDB/server/commit/7e0f40b333)\
  2017-05-23 18:37:55 +0300
  * [MDEV-12625](https://jira.mariadb.org/browse/MDEV-12625) total\_index\_blocks is uninitialized in ALTER TABLE…ALGORITHM=INPLACE of small tables
* [Revision #a1b6128ded](https://github.com/MariaDB/server/commit/a1b6128ded)\
  2017-05-22 18:27:44 +0000
  * [MDEV-11264](https://jira.mariadb.org/browse/MDEV-11264) Fix DeviceIoControl() usage in innodb.
* Merge [Revision #8f643e2063](https://github.com/MariaDB/server/commit/8f643e2063) 2017-05-23 11:09:47 +0300 - Merge 10.1 into 10.2
* Merge [Revision #b61700c221](https://github.com/MariaDB/server/commit/b61700c221) 2017-05-23 08:59:03 +0300 - Merge 10.0 into 10.1
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
* Merge [Revision #70df2bef7a](https://github.com/MariaDB/server/commit/70df2bef7a) 2017-05-22 13:49:37 +0000 - Merge branch 'bb-10.1-wlad' into 10.1
* [Revision #ee4eda40b9](https://github.com/MariaDB/server/commit/ee4eda40b9)\
  2017-05-21 22:19:06 +0000
  * [MDEV-12832](https://jira.mariadb.org/browse/MDEV-12832) : remove libarchive support from mariadb-backup, due to different packaging issues.
* [Revision #2c69c428a7](https://github.com/MariaDB/server/commit/2c69c428a7)\
  2017-05-22 13:33:37 +0300
  * Changing maturity to stable
* [Revision #90c52e5291](https://github.com/MariaDB/server/commit/90c52e5291)\
  2017-05-20 21:49:35 +0300
  * [MDEV-12615](https://jira.mariadb.org/browse/MDEV-12615): InnoDB page compression method snappy mostly does not compress pages
* [Revision #f880200974](https://github.com/MariaDB/server/commit/f880200974)\
  2017-05-20 17:47:07 +0300
  * After-merge fix: Correct the 32-bit XtraDB result diff.
* [Revision #fe291c687d](https://github.com/MariaDB/server/commit/fe291c687d)\
  2017-05-20 08:43:25 +0300
  * After-merge fix: Correct the XtraDB result diff.
* [Revision #45fe62b8d6](https://github.com/MariaDB/server/commit/45fe62b8d6)\
  2017-05-19 22:25:57 +0300
  * Clean up a test
* [Revision #a4d4a5fe82](https://github.com/MariaDB/server/commit/a4d4a5fe82)\
  2017-05-19 14:28:57 +0300
  * After-merge fix for [MDEV-11638](https://jira.mariadb.org/browse/MDEV-11638)
* Merge [Revision #65e1399e64](https://github.com/MariaDB/server/commit/65e1399e64) 2017-05-19 13:59:43 +0300 - Merge 10.0 into 10.1
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
* [Revision #3aecedb2f8](https://github.com/MariaDB/server/commit/3aecedb2f8)\
  2017-05-23 00:11:17 -0400
  * bump the VERSION
* Merge [Revision #70505dd45b](https://github.com/MariaDB/server/commit/70505dd45b) 2017-05-22 09:20:20 +0300 - Merge 10.1 into 10.2
* Merge [Revision #13a350ac29](https://github.com/MariaDB/server/commit/13a350ac29) 2017-05-19 08:53:58 +0300 - Merge 10.0 into 10.1
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
* [Revision #d0eb4ee96b](https://github.com/MariaDB/server/commit/d0eb4ee96b)\
  2017-05-17 19:56:51 +0000
  * Backport aws kms build fixes from 10.2
* [Revision #9dffa3072c](https://github.com/MariaDB/server/commit/9dffa3072c)\
  2017-05-16 17:24:21 +0000
  * [MDEV-12810](https://jira.mariadb.org/browse/MDEV-12810) - force static build of crc library
* [Revision #40c7778e05](https://github.com/MariaDB/server/commit/40c7778e05)\
  2017-05-16 17:11:25 +0000
  * [MDEV-12814](https://jira.mariadb.org/browse/MDEV-12814) mariadb-backup : don't try io throttling in copy-back
* [Revision #f302a3cf9d](https://github.com/MariaDB/server/commit/f302a3cf9d)\
  2017-04-28 10:07:03 +0300
  * [MDEV-12593](https://jira.mariadb.org/browse/MDEV-12593): InnoDB page compression should use lz4\_compress\_default if
* [Revision #febe88198e](https://github.com/MariaDB/server/commit/febe88198e)\
  2017-05-17 08:54:16 +0300
  * Make some variables const in fil\_iterate()
* [Revision #408ef65f84](https://github.com/MariaDB/server/commit/408ef65f84)\
  2017-05-16 17:45:22 +0300
  * Never pass NULL to innobase\_get\_stmt()
* [Revision #71cd205956](https://github.com/MariaDB/server/commit/71cd205956)\
  2017-05-16 20:08:47 +0300
  * Silence bogus GCC 7 warnings -Wimplicit-fallthrough
* [Revision #7edadde72e](https://github.com/MariaDB/server/commit/7edadde72e)\
  2017-05-18 15:20:57 +0300
  * Remove bogus attribute((nonnull))
* [Revision #9756440fb5](https://github.com/MariaDB/server/commit/9756440fb5)\
  2017-05-18 14:29:39 +0300
  * Fix a compilation warning introduced by [MDEV-11782](https://jira.mariadb.org/browse/MDEV-11782)
* [Revision #6f54d04eb9](https://github.com/MariaDB/server/commit/6f54d04eb9)\
  2017-05-18 14:13:07 +0300
  * Remove unnecessary conversions from integer to double
* [Revision #907cbadb6f](https://github.com/MariaDB/server/commit/907cbadb6f)\
  2017-05-18 14:11:17 +0300
  * Fix some -Wimplicit-fallthrough warnings in InnoDB
* [Revision #0bfa3dff8b](https://github.com/MariaDB/server/commit/0bfa3dff8b)\
  2017-05-16 12:07:26 +0300
  * [MDEV-12698](https://jira.mariadb.org/browse/MDEV-12698) innodb.innodb\_stats\_del\_mark test failure
* [Revision #5e9d651108](https://github.com/MariaDB/server/commit/5e9d651108)\
  2017-05-18 23:54:43 -0700
  * Fixed the bug [MDEV-12788](https://jira.mariadb.org/browse/MDEV-12788).
* [Revision #4807df6f20](https://github.com/MariaDB/server/commit/4807df6f20)\
  2017-05-18 16:58:02 +0300
  * [MDEV-12794](https://jira.mariadb.org/browse/MDEV-12794) innodb\_zip.recover failed in buildbot
* [Revision #fff61e31ec](https://github.com/MariaDB/server/commit/fff61e31ec)\
  2017-05-17 14:44:16 +0300
  * Fix a compiler warning
* [Revision #f7dab76aa2](https://github.com/MariaDB/server/commit/f7dab76aa2)\
  2017-05-17 00:00:27 +0300
  * [MDEV-12756](https://jira.mariadb.org/browse/MDEV-12756) rpl.rpl\_killed\_ddl fails in buildbot with 'Can't find record'

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
