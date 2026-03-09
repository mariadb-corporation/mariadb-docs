# MariaDB 10.1.25 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.25)[Release Notes](../../old-releases/10.1/10.1.25.md)[Changelog](mariadb-10125-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 4 Jul 2017

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.25.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

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
  * Fixed the bug [MDEV-12855](https://jira.mariadb.org/browse/MDEV-12855)
* [Revision #151f4e9b4a](https://github.com/MariaDB/server/commit/151f4e9b4a)\
  2017-06-07 16:29:55 -0700
  * Fixed the bug [MDEV-12963](https://jira.mariadb.org/browse/MDEV-12963)
* [Revision #c258ca2463](https://github.com/MariaDB/server/commit/c258ca2463)\
  2017-06-07 12:45:09 -0700
  * Fixed the bug [MDEV-12838](https://jira.mariadb.org/browse/MDEV-12838)
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
  * Cherrypick Percona's fix for leaking descriptors with new xbstream.
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
  * [MDEV-12193](https://jira.mariadb.org/browse/MDEV-12193) Discontinue support of insecure and unsupported OpenSSL versions (< 1.0.1)
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

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
