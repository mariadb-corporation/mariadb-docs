# MariaDB 10.3.1 Changelog

[Download](https://downloads.mariadb.org/mariadb/10.3.1)[Release Notes](../../old-releases/10.3/10.3.1.md)[Changelog](mariadb-1031-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 29 Aug 2017

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.1.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #316cb33795](https://github.com/MariaDB/server/commit/316cb33795)\
  2017-08-26 22:01:03 +0000
  * In test\_proxy\_header(), use IP address 192.0.2.1 .
* [Revision #f93d5d927e](https://github.com/MariaDB/server/commit/f93d5d927e)\
  2017-08-26 15:26:39 +0200
  * after merge: remove innodb\_file\_format from merged tests
* [Revision #e20f1ec302](https://github.com/MariaDB/server/commit/e20f1ec302)\
  2017-08-26 12:38:31 +0200
  * mysql\_client\_test: don't use 192.168.0.1
* Merge [Revision #bb8e99fdc3](https://github.com/MariaDB/server/commit/bb8e99fdc3) 2017-08-26 00:34:43 +0200 - Merge branch 'bb-10.2-ext' into 10.3
* [Revision #c02d61bc11](https://github.com/MariaDB/server/commit/c02d61bc11)\
  2017-08-25 20:52:55 +0200
  * fix test result for windows
* [Revision #9bbc8a8924](https://github.com/MariaDB/server/commit/9bbc8a8924)\
  2017-08-25 20:45:00 +0200
  * update test results after 988a9daa945c
* [Revision #fd56727e99](https://github.com/MariaDB/server/commit/fd56727e99)\
  2017-08-25 14:23:24 +0200
  * [MDEV-13545](https://jira.mariadb.org/browse/MDEV-13545) sql\_sequence.gtid fails in buildbot
* [Revision #d0d626be4c](https://github.com/MariaDB/server/commit/d0d626be4c)\
  2017-08-17 17:04:31 +0200
  * [MDEV-13510](https://jira.mariadb.org/browse/MDEV-13510) main.delete\_use\_source fails in buildbot and outside with wrong plan
* Merge [Revision #27412877db](https://github.com/MariaDB/server/commit/27412877db) 2017-08-25 10:25:48 +0200 - Merge branch '10.2' into bb-10.2-ext
* [Revision #a544225d0a](https://github.com/MariaDB/server/commit/a544225d0a)\
  2017-08-24 12:51:05 +0530
  * Update README.md
* [Revision #e7bf8bca2f](https://github.com/MariaDB/server/commit/e7bf8bca2f)\
  2017-08-24 10:13:07 +0300
  * [MDEV-13534](https://jira.mariadb.org/browse/MDEV-13534) InnoDB STATS\_PERSISTENT fails to ignore garbage delete-mark flag on node pointer pages
* [Revision #ae0759ad45](https://github.com/MariaDB/server/commit/ae0759ad45)\
  2017-08-23 18:40:47 +0300
  * [MDEV-13602](https://jira.mariadb.org/browse/MDEV-13602): rocksdb.index\_merge\_rocksdb2 failed in buildbot
* [Revision #06b4b99f3e](https://github.com/MariaDB/server/commit/06b4b99f3e)\
  2017-08-23 14:40:23 +0300
  * The test failed once on Buildbot with the result difference:
* [Revision #81bd81fbe8](https://github.com/MariaDB/server/commit/81bd81fbe8)\
  2017-08-23 11:35:34 +0300
  * Adjust InnoDB debug assertions for Oracle Bug#25551311 aka Bug#23517560
* [Revision #36a971724e](https://github.com/MariaDB/server/commit/36a971724e)\
  2017-08-23 10:01:48 +0300
  * [MDEV-13167](https://jira.mariadb.org/browse/MDEV-13167) InnoDB key rotation is not skipping unused pages
* [Revision #e52dd13c2e](https://github.com/MariaDB/server/commit/e52dd13c2e)\
  2017-08-23 09:47:50 +0300
  * Code clean-up related to [MDEV-13167](https://jira.mariadb.org/browse/MDEV-13167)
* [Revision #59caf2c3c1](https://github.com/MariaDB/server/commit/59caf2c3c1)\
  2017-08-21 18:56:46 +0300
  * [MDEV-13485](https://jira.mariadb.org/browse/MDEV-13485) MTR tests fail massively with --innodb-sync-debug
* [Revision #1621d32eac](https://github.com/MariaDB/server/commit/1621d32eac)\
  2017-08-22 14:56:17 +0300
  * Remove the unused redo log record type MLOG\_INIT\_FILE\_PAGE
* [Revision #825b6a354a](https://github.com/MariaDB/server/commit/825b6a354a)\
  2017-08-23 08:05:50 +0300
  * [MDEV-13452](https://jira.mariadb.org/browse/MDEV-13452) Assertion \`!recv\_no\_log\_write' failed at startup
* [Revision #ef8e1a35cc](https://github.com/MariaDB/server/commit/ef8e1a35cc)\
  2017-08-21 16:12:09 +0300
  * Fix rocksdb.bulk\_load test
* [Revision #4f34ec26fa](https://github.com/MariaDB/server/commit/4f34ec26fa)\
  2017-08-21 15:26:21 +0300
  * [MDEV-13600](https://jira.mariadb.org/browse/MDEV-13600): Update test results for rocksdb.bulk\_load\_rev\_cf
* [Revision #86fc5ece26](https://github.com/MariaDB/server/commit/86fc5ece26)\
  2017-08-18 15:01:32 +0300
  * [MDEV-13559](https://jira.mariadb.org/browse/MDEV-13559) encryption.innodb-redo-badkey failed in buildbot
* [Revision #8a9e9d896e](https://github.com/MariaDB/server/commit/8a9e9d896e)\
  2017-08-18 14:42:53 +0300
  * [MDEV-13570](https://jira.mariadb.org/browse/MDEV-13570) Assertion failure !srv\_read\_only\_mode in --innodb-read-only shutdown when buf\_resize\_thread is active
* [Revision #8a3e2970ad](https://github.com/MariaDB/server/commit/8a3e2970ad)\
  2017-08-18 14:42:18 +0300
  * [MDEV-13575](https://jira.mariadb.org/browse/MDEV-13575) On failure, mariadb-backup --backup --safe-slave-backup may forget to START SLAVE SQL\_THREAD
* [Revision #72ac85cdda](https://github.com/MariaDB/server/commit/72ac85cdda)\
  2017-08-18 12:51:28 -0400
  * bump the VERSION
* [Revision #605b835220](https://github.com/MariaDB/server/commit/605b835220)\
  2017-08-18 10:07:11 +0300
  * [MDEV-13754](https://jira.mariadb.org/browse/MDEV-13754) Memory leak in mariadb-backup.incremental\_backup
* [Revision #74ce0cf148](https://github.com/MariaDB/server/commit/74ce0cf148)\
  2017-08-18 10:00:56 +0300
  * [MDEV-13574](https://jira.mariadb.org/browse/MDEV-13574) related mariadb-backup code cleanup (non-functional change)
* [Revision #e9e051d297](https://github.com/MariaDB/server/commit/e9e051d297)\
  2017-08-18 08:52:41 +0300
  * Follow-up fix to [MDEV-12988](https://jira.mariadb.org/browse/MDEV-12988) backup fails if innodb\_undo\_tablespaces>0
* [Revision #f269915381](https://github.com/MariaDB/server/commit/f269915381)\
  2017-08-18 02:51:30 +0300
  * Updated list of unstable tests for 10.2.8
* [Revision #bcd5622ebb](https://github.com/MariaDB/server/commit/bcd5622ebb)\
  2017-08-18 02:48:43 +0300
  * gcol.gcol\_rollback could fail with errors in server log
* [Revision #edf77043ba](https://github.com/MariaDB/server/commit/edf77043ba)\
  2017-08-17 15:07:44 +0000
  * [MDEV-12948](https://jira.mariadb.org/browse/MDEV-12948) : do not spam error log, if DeviceIoControl(IOCTL\_STORAGE\_QUERY\_PROPERTY) fails with ERROR\_INVALID\_FUNCTION
* [Revision #e6971011c3](https://github.com/MariaDB/server/commit/e6971011c3)\
  2017-08-17 15:38:41 +0300
  * [MDEV-12988](https://jira.mariadb.org/browse/MDEV-12988) backup fails if innodb\_undo\_tablespaces>0
* [Revision #f2033df6ac](https://github.com/MariaDB/server/commit/f2033df6ac)\
  2017-08-24 20:49:07 -0700
  * More thorough correction of the patch that complemented the patch for [MDEV-10855](https://jira.mariadb.org/browse/MDEV-10855)
* [Revision #0336655918](https://github.com/MariaDB/server/commit/0336655918)\
  2017-08-23 19:59:49 -0700
  * Corrected the patch that complemented the patch for [MDEV-10855](https://jira.mariadb.org/browse/MDEV-10855)
* [Revision #add44e684c](https://github.com/MariaDB/server/commit/add44e684c)\
  2017-08-25 11:28:44 +0200
  * compilation failure in oqgraph after 4aaa38d26ed9
* [Revision #578b2b05b8](https://github.com/MariaDB/server/commit/578b2b05b8)\
  2017-08-25 16:14:03 +0000
  * [MDEV-13641](https://jira.mariadb.org/browse/MDEV-13641) host errors are not reset after successful connection.
* [Revision #77c41fa725](https://github.com/MariaDB/server/commit/77c41fa725)\
  2017-08-23 13:34:52 +0200
  * small cleanup of rpl.rpl\_stop\_slave
* [Revision #f753480c72](https://github.com/MariaDB/server/commit/f753480c72)\
  2017-08-09 23:54:16 +0300
  * Fixed assert when running rpl.rpl\_parallel\_partition
* [Revision #e208100d44](https://github.com/MariaDB/server/commit/e208100d44)\
  2017-08-09 23:52:13 +0300
  * Have mysqltest first send SIGABRT, then SIGKILL
* [Revision #25c06f5282](https://github.com/MariaDB/server/commit/25c06f5282)\
  2017-06-18 14:00:28 +0300
  * Optimize LEX\_STRING comparisons
* [Revision #cc77f9882d](https://github.com/MariaDB/server/commit/cc77f9882d)\
  2017-06-18 12:28:40 +0300
  * Changed KEY names to use LEX\_CSTRING
* [Revision #874e4e473a](https://github.com/MariaDB/server/commit/874e4e473a)\
  2017-08-07 23:21:23 +0300
  * Better error message for mysql\_upgrade if upgrade file can't be updated.
* [Revision #b6c5657ef2](https://github.com/MariaDB/server/commit/b6c5657ef2)\
  2017-08-06 21:53:49 +0300
  * Reduce stack size
* [Revision #ffb17a6509](https://github.com/MariaDB/server/commit/ffb17a6509)\
  2017-08-04 13:13:32 +0300
  * Marked innodb\_virtual\_basic as 'big' to fix some timeouts in buildbot
* [Revision #8e722064f7](https://github.com/MariaDB/server/commit/8e722064f7)\
  2017-07-30 11:45:49 +0300
  * Remove dumping of some not needed core's when running test suite
* [Revision #94bbe8ad58](https://github.com/MariaDB/server/commit/94bbe8ad58)\
  2017-07-29 10:35:30 +0300
  * Affected rows for a SP now includes affected rows for all statements
* [Revision #4be15fe065](https://github.com/MariaDB/server/commit/4be15fe065)\
  2017-07-21 20:02:11 +0300
  * Added missing ; after WSREP\_TO\_ISOLATION\_BEGIN
* [Revision #21518ab2e4](https://github.com/MariaDB/server/commit/21518ab2e4)\
  2017-07-21 19:56:41 +0300
  * New option for slow logging (log\_slow\_disable\_statements)
* [Revision #536215e32f](https://github.com/MariaDB/server/commit/536215e32f)\
  2017-07-03 11:35:44 +0300
  * Added DBUG\_ASSERT\_AS\_PRINTF compile flag
* [Revision #52a1e4d613](https://github.com/MariaDB/server/commit/52a1e4d613)\
  2017-07-01 17:21:02 +0300
  * Fixed sequence.gtid
* [Revision #9e1cc831f2](https://github.com/MariaDB/server/commit/9e1cc831f2)\
  2017-06-20 18:30:00 +0300
  * Fixed some compiler warnings
* [Revision #f71bed08ca](https://github.com/MariaDB/server/commit/f71bed08ca)\
  2017-06-19 06:37:43 +0300
  * Safety fix: lock binlog\_end\_pos before calling signal\_update
* [Revision #458d5ed8aa](https://github.com/MariaDB/server/commit/458d5ed8aa)\
  2017-06-19 06:34:38 +0300
  * Lots of small cleanups
* [Revision #a70f7aad55](https://github.com/MariaDB/server/commit/a70f7aad55)\
  2017-06-19 06:25:10 +0300
  * Print thread\_id instead of pthread\_self to error log
* [Revision #af06683b73](https://github.com/MariaDB/server/commit/af06683b73)\
  2017-06-18 10:01:24 +0300
  * Optimize make\_lex\_string() to not call alloc\_root twice.
* [Revision #8bfda2f0af](https://github.com/MariaDB/server/commit/8bfda2f0af)\
  2017-06-18 09:58:13 +0300
  * Simplify test if we can use table in query cache
* [Revision #1ed605e490](https://github.com/MariaDB/server/commit/1ed605e490)\
  2017-06-18 08:43:55 +0300
  * Added sql\_alloc.h
* [Revision #828602356c](https://github.com/MariaDB/server/commit/828602356c)\
  2017-08-11 13:58:32 +0200
  * Don't include my\_global.h in "pure" plugins
* [Revision #a6e215f221](https://github.com/MariaDB/server/commit/a6e215f221)\
  2017-08-11 13:26:54 +0200
  * Fix compilation warnings in plugins
* [Revision #d5a6bae7c0](https://github.com/MariaDB/server/commit/d5a6bae7c0)\
  2017-08-21 16:57:08 +0200
  * Fix compilation errors
* [Revision #4aaa38d26e](https://github.com/MariaDB/server/commit/4aaa38d26e)\
  2017-06-18 06:42:16 +0300
  * Enusure that my\_global.h is included first
* [Revision #b0da8897b0](https://github.com/MariaDB/server/commit/b0da8897b0)\
  2017-06-18 06:25:01 +0300
  * Added copyright message to some files
* [Revision #b77bb43f60](https://github.com/MariaDB/server/commit/b77bb43f60)\
  2017-06-09 16:30:58 +0300
  * Use microsecond\_interval\_timer() instead of my\_time() in replicaiton
* [Revision #44676ed5b1](https://github.com/MariaDB/server/commit/44676ed5b1)\
  2017-06-09 10:04:00 +0300
  * Cleaned up output from thr\_print\_locks
* [Revision #4040a17ea2](https://github.com/MariaDB/server/commit/4040a17ea2)\
  2017-08-23 16:27:24 +0200
  * Compile mariadb-backup with its own copy of net\_serv.cc
* [Revision #7a5eb00322](https://github.com/MariaDB/server/commit/7a5eb00322)\
  2017-08-23 15:20:38 +0200
  * fix 64-bit tests too
* [Revision #4246fe802e](https://github.com/MariaDB/server/commit/4246fe802e)\
  2017-08-23 12:23:57 +0200
  * 32-bit fixes
* [Revision #aaddac5cd7](https://github.com/MariaDB/server/commit/aaddac5cd7)\
  2017-08-23 08:27:46 +0000
  * fix compile errors
* [Revision #58cd69fc80](https://github.com/MariaDB/server/commit/58cd69fc80)\
  2017-08-22 21:08:38 +0200
  * [MDEV-11159](https://jira.mariadb.org/browse/MDEV-11159) Server proxy protocol support
* Merge [Revision #d258a2bd1f](https://github.com/MariaDB/server/commit/d258a2bd1f) 2017-08-22 20:27:10 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #b0dbc707b8](https://github.com/MariaDB/server/commit/b0dbc707b8)\
  2017-08-22 20:25:59 +0400
  * [MDEV-13617](https://jira.mariadb.org/browse/MDEV-13617) tokudb\_parts tests failed in buildbot
* [Revision #a1e444e1cc](https://github.com/MariaDB/server/commit/a1e444e1cc)\
  2017-08-19 20:59:24 -0700
  * Corrected the function compare\_order\_elements() to make it platform independent.
* [Revision #d7b45e01b4](https://github.com/MariaDB/server/commit/d7b45e01b4)\
  2017-08-19 15:02:29 -0700
  * This patch complements the patch for [MDEV-10855](https://jira.mariadb.org/browse/MDEV-10855).
* [Revision #1b7a2e4ca2](https://github.com/MariaDB/server/commit/1b7a2e4ca2)\
  2017-08-17 17:04:31 +0200
  * [MDEV-13510](https://jira.mariadb.org/browse/MDEV-13510) main.delete\_use\_source fails in buildbot and outside with wrong plan
* Merge [Revision #935c6f502f](https://github.com/MariaDB/server/commit/935c6f502f) 2017-08-18 18:30:52 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #4305c3ca57](https://github.com/MariaDB/server/commit/4305c3ca57)\
  2017-08-18 18:29:33 +0400
  * [MDEV-13581](https://jira.mariadb.org/browse/MDEV-13581) ROW TYPE OF t1 and t1%ROWTYPE for routine parameters
* Merge [Revision #83ea51a28d](https://github.com/MariaDB/server/commit/83ea51a28d) 2017-08-17 09:45:05 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #a70809c0fc](https://github.com/MariaDB/server/commit/a70809c0fc)\
  2017-08-17 07:07:11 +0400
  * [MDEV-13555](https://jira.mariadb.org/browse/MDEV-13555) Assertion \`!item->null\_value' failed in Type\_handler::Item\_send\_str
* [Revision #ff3cf74974](https://github.com/MariaDB/server/commit/ff3cf74974)\
  2017-08-16 14:46:24 +0300
  * Silence a -Wimplicit-fallthrough warning
* [Revision #58c5145d60](https://github.com/MariaDB/server/commit/58c5145d60)\
  2017-08-15 08:28:38 -0700
  * Adjusted the result file for sys\_vars.sysvars\_server\_embedded.
* [Revision #92f9be495b](https://github.com/MariaDB/server/commit/92f9be495b)\
  2017-08-16 09:03:27 +0300
  * Work around [MDEV-13542](https://jira.mariadb.org/browse/MDEV-13542) Crashing on a corrupted page is unhelpful
* [Revision #f4b379d6ca](https://github.com/MariaDB/server/commit/f4b379d6ca)\
  2017-08-15 17:18:55 +0300
  * [MDEV-13536](https://jira.mariadb.org/browse/MDEV-13536) DB\_TRX\_ID is not actually being reset when the history is removed
* Merge [Revision #442ac9229b](https://github.com/MariaDB/server/commit/442ac9229b) 2017-08-15 17:54:46 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #3fd30508b2](https://github.com/MariaDB/server/commit/3fd30508b2)\
  2017-08-15 17:53:08 +0400
  * Recording more tests for [MDEV-13500](https://jira.mariadb.org/browse/MDEV-13500) sql\_mode=ORACLE: can't create a virtual column with function MOD
* Merge [Revision #6ac3d7511c](https://github.com/MariaDB/server/commit/6ac3d7511c) 2017-08-15 17:13:59 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #b5098f3dae](https://github.com/MariaDB/server/commit/b5098f3dae)\
  2017-08-15 16:41:58 +0400
  * [MDEV-13533](https://jira.mariadb.org/browse/MDEV-13533) Remove the THD parameter from sp\_head::init\_sp\_name()
* [Revision #3f7f0c6a29](https://github.com/MariaDB/server/commit/3f7f0c6a29)\
  2017-08-15 14:58:42 +0400
  * [MDEV-13531](https://jira.mariadb.org/browse/MDEV-13531) Add Database\_qualified\_name::copy()
* [Revision #4d50594dfc](https://github.com/MariaDB/server/commit/4d50594dfc)\
  2017-08-15 14:13:42 +0400
  * [MDEV-13529](https://jira.mariadb.org/browse/MDEV-13529) Add class Sql\_cmd\_call
* [Revision #966cc80299](https://github.com/MariaDB/server/commit/966cc80299)\
  2017-08-15 11:15:18 +0400
  * [MDEV-13528](https://jira.mariadb.org/browse/MDEV-13528) Add LEX::sp\_body\_finalize\_{procedure|function}
* Merge [Revision #1743883d55](https://github.com/MariaDB/server/commit/1743883d55) 2017-08-15 09:59:17 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #22c9663d85](https://github.com/MariaDB/server/commit/22c9663d85)\
  2017-08-15 09:55:09 +0400
  * [MDEV-13527](https://jira.mariadb.org/browse/MDEV-13527) Crash when EXPLAIN SELECT .. INTO row\_sp\_variable.field
* [Revision #6179a8efdc](https://github.com/MariaDB/server/commit/6179a8efdc)\
  2017-08-15 09:37:16 +0400
  * [MDEV-13526](https://jira.mariadb.org/browse/MDEV-13526) Add Type\_handler::Item\_val\_bool()
* Merge [Revision #6db1b0188c](https://github.com/MariaDB/server/commit/6db1b0188c) 2017-08-15 07:52:48 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #9822fb1f19](https://github.com/MariaDB/server/commit/9822fb1f19)\
  2017-08-15 07:49:18 +0400
  * Fixing test results for [MDEV-13500](https://jira.mariadb.org/browse/MDEV-13500) sql\_mode=ORACLE: can't create a virtual column with function MOD
* [Revision #596bdc2dbe](https://github.com/MariaDB/server/commit/596bdc2dbe)\
  2017-08-14 17:05:41 -0700
  * Changed the function my\_set\_bits() to return uint64 instead of uint32. Corrected an assertion in the constructor for the class Sys\_var\_flagset.
* [Revision #9d85323007](https://github.com/MariaDB/server/commit/9d85323007)\
  2017-08-14 11:12:17 +0400
  * [MDEV-13500](https://jira.mariadb.org/browse/MDEV-13500) sql\_mode=ORACLE: can't create a virtual column with function MOD
* [Revision #0f554dd0fd](https://github.com/MariaDB/server/commit/0f554dd0fd)\
  2017-08-13 09:44:44 -0700
  * Adjusted result files for tokudb tests.
* [Revision #61bbabb202](https://github.com/MariaDB/server/commit/61bbabb202)\
  2017-08-12 19:58:16 -0700
  * Implemented condition pushdown into derived tables / views with window functions ([MDEV-10855](https://jira.mariadb.org/browse/MDEV-10855)).
* [Revision #c9981fbee2](https://github.com/MariaDB/server/commit/c9981fbee2)\
  2017-05-31 09:49:17 +0200
  * [MDEV-13003](https://jira.mariadb.org/browse/MDEV-13003) - Oracle compatibility : Replace function
* Merge [Revision #1a9e13d622](https://github.com/MariaDB/server/commit/1a9e13d622) 2017-08-11 10:58:23 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #837aa57fb2](https://github.com/MariaDB/server/commit/837aa57fb2)\
  2017-08-11 10:21:51 +0400
  * Test result fixed.
* [Revision #2ebb1380d6](https://github.com/MariaDB/server/commit/2ebb1380d6)\
  2017-08-11 00:50:29 +0400
  * [MDEV-12604](https://jira.mariadb.org/browse/MDEV-12604) Comparison of JSON\_EXTRACT result differs with Mysql.
* [Revision #e223752472](https://github.com/MariaDB/server/commit/e223752472)\
  2017-08-10 21:40:19 -0700
  * Adjusted results after the patch for [MDEV-13369](https://jira.mariadb.org/browse/MDEV-13369).
* [Revision #bf75dcac89](https://github.com/MariaDB/server/commit/bf75dcac89)\
  2017-08-10 14:25:19 -0700
  * This is a modification of the first patch committed for [MDEV-13369](https://jira.mariadb.org/browse/MDEV-13369) developed to cover the case of [MDEV-13389](https://jira.mariadb.org/browse/MDEV-13389): "Optimization for equi-joins of derived tables with window functions".
* [Revision #b14e2b044b](https://github.com/MariaDB/server/commit/b14e2b044b)\
  2017-08-03 21:19:19 -0700
  * This first patch prepared for the task [MDEV-13369](https://jira.mariadb.org/browse/MDEV-13369): "Optimization for equi-joins of derived tables with GROUP BY" should be considered rather as a 'proof of concept'.
* [Revision #3e7b1bd64a](https://github.com/MariaDB/server/commit/3e7b1bd64a)\
  2017-08-14 19:56:52 +0300
  * [MDEV-13518](https://jira.mariadb.org/browse/MDEV-13518) funcs\_1.myisam\_views-big failed in buildbot
* [Revision #734671174e](https://github.com/MariaDB/server/commit/734671174e)\
  2017-08-14 19:56:08 +0300
  * [MDEV-13014](https://jira.mariadb.org/browse/MDEV-13014) Typos in ER\_WRONG\_INSERT\_INTO\_SEQUENCE
* [Revision #347d9456e4](https://github.com/MariaDB/server/commit/347d9456e4)\
  2017-08-11 12:47:54 +0300
  * [MDEV-13495](https://jira.mariadb.org/browse/MDEV-13495) Crash in rollback of a recovered INSERT transaction after upgrade
* [Revision #73297f532f](https://github.com/MariaDB/server/commit/73297f532f)\
  2017-08-10 12:31:26 +0300
  * [MDEV-13476](https://jira.mariadb.org/browse/MDEV-13476) TRX\_UNDO\_PAGE\_TYPE mismatch when writing undo log after upgrade
* [Revision #237f23d702](https://github.com/MariaDB/server/commit/237f23d702)\
  2017-08-10 11:46:08 +0300
  * [MDEV-13475](https://jira.mariadb.org/browse/MDEV-13475) InnoDB: Failing assertion: lsn == log\_sys->lsn || srv\_force\_recovery == SRV\_FORCE\_NO\_LOG\_REDO
* [Revision #63ad4fe5bb](https://github.com/MariaDB/server/commit/63ad4fe5bb)\
  2017-08-07 16:04:05 +0300
  * [MDEV-13430](https://jira.mariadb.org/browse/MDEV-13430) InnoDB upgrade from previous versions to 10.3 is not possible
* [Revision #efa4996bb7](https://github.com/MariaDB/server/commit/efa4996bb7)\
  2017-08-08 19:59:42 +0300
  * Remove stray XtraDB files
* [Revision #f5b0c47b58](https://github.com/MariaDB/server/commit/f5b0c47b58)\
  2017-08-08 00:05:20 +0300
  * Fix a -Wimplicit-fallthrough warning
* [Revision #c039cacf53](https://github.com/MariaDB/server/commit/c039cacf53)\
  2017-08-07 23:44:45 +0300
  * [MDEV-12288](https://jira.mariadb.org/browse/MDEV-12288) follow-up: Adjust PAGE\_MAX\_TRX\_ID in online ADD INDEX
* [Revision #932273a8a0](https://github.com/MariaDB/server/commit/932273a8a0)\
  2017-08-07 23:56:30 +0300
  * [MDEV-12288](https://jira.mariadb.org/browse/MDEV-12288) follow-up: Adjust a test for the purge of insert\_undo log
* Merge [Revision #620ba97cfc](https://github.com/MariaDB/server/commit/620ba97cfc) 2017-08-09 12:59:03 +0300 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #6685cdc250](https://github.com/MariaDB/server/commit/6685cdc250)\
  2017-08-09 12:36:06 +0300
  * Temporarily record wrong result for the [MDEV-12604](https://jira.mariadb.org/browse/MDEV-12604) JSON\_EXTRACT test
* Merge [Revision #0930d6698f](https://github.com/MariaDB/server/commit/0930d6698f) 2017-08-09 12:35:21 +0300 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #1f0a22acbd](https://github.com/MariaDB/server/commit/1f0a22acbd) 2017-08-08 09:47:00 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #4649fb37e3](https://github.com/MariaDB/server/commit/4649fb37e3)\
  2017-08-07 21:21:13 +0300
  * Get rid of valgrind warning for sql\_sequence tests.
* [Revision #213af08d99](https://github.com/MariaDB/server/commit/213af08d99)\
  2017-08-07 20:49:56 +0300
  * [MDEV-13393](https://jira.mariadb.org/browse/MDEV-13393) SEQUENCE related crash when running concurrent I\_S.TABLES and FLUSH queries
* [Revision #cf9e0bf3e6](https://github.com/MariaDB/server/commit/cf9e0bf3e6)\
  2017-08-07 20:43:44 +0300
  * Fixed compiler warning
* Merge [Revision #988a9daa94](https://github.com/MariaDB/server/commit/988a9daa94) 2017-08-07 21:35:34 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #0f1cadd9a5](https://github.com/MariaDB/server/commit/0f1cadd9a5)\
  2017-08-04 16:33:58 +0400
  * [MDEV-13450](https://jira.mariadb.org/browse/MDEV-13450) Cleanup SP code for packages
* [Revision #b3977ac23f](https://github.com/MariaDB/server/commit/b3977ac23f)\
  2017-08-04 15:15:55 +0400
  * An additional patch for [MDEV-13415](https://jira.mariadb.org/browse/MDEV-13415) Wrap the code in sp.cc into a class Sp\_handler
* [Revision #9b74b00c8e](https://github.com/MariaDB/server/commit/9b74b00c8e)\
  2017-08-04 14:41:05 +0400
  * Adding the "const" qualified to the LEX\_CSTRING parameter of a few check\_xxx() functions
* [Revision #f717fb8242](https://github.com/MariaDB/server/commit/f717fb8242)\
  2017-08-06 14:42:30 +0300
  * Make rocksdb.type\_varchar test stable
* Merge [Revision #1b0cf1b729](https://github.com/MariaDB/server/commit/1b0cf1b729) 2017-08-01 15:58:26 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* Merge [Revision #68bc777830](https://github.com/MariaDB/server/commit/68bc777830) 2017-08-01 15:37:01 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #9372f6e526](https://github.com/MariaDB/server/commit/9372f6e526)\
  2017-08-01 12:04:14 +0400
  * [MDEV-13419](https://jira.mariadb.org/browse/MDEV-13419) Cleanup for Sp\_handler::show\_create\_sp
* Merge [Revision #c431eafd62](https://github.com/MariaDB/server/commit/c431eafd62) 2017-07-31 23:00:59 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #c9218ff439](https://github.com/MariaDB/server/commit/c9218ff439)\
  2017-07-31 23:00:02 +0400
  * [MDEV-13415](https://jira.mariadb.org/browse/MDEV-13415) Wrap the code in sp.cc into a class Sp\_handler
* [Revision #4937474f86](https://github.com/MariaDB/server/commit/4937474f86)\
  2017-07-31 17:34:59 +0400
  * [MDEV-13414](https://jira.mariadb.org/browse/MDEV-13414) Fix the SP code to avoid excessive use of strlen
* Merge [Revision #716898755a](https://github.com/MariaDB/server/commit/716898755a) 2017-07-28 12:47:20 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* Merge [Revision #4fc1f2fb75](https://github.com/MariaDB/server/commit/4fc1f2fb75) 2017-07-22 22:48:45 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* Merge [Revision #23290e42e3](https://github.com/MariaDB/server/commit/23290e42e3) 2017-07-21 23:38:30 +0400 - Merge commit 'e2afdb1ee430cb9d030aeeedc85eb903cda5e5d1' into bb-10.2-ext
* Merge [Revision #e67b816451](https://github.com/MariaDB/server/commit/e67b816451) 2017-07-19 19:43:55 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* Merge [Revision #34668e10b2](https://github.com/MariaDB/server/commit/34668e10b2) 2017-07-19 14:45:54 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #d1af417eb8](https://github.com/MariaDB/server/commit/d1af417eb8)\
  2017-07-18 13:51:12 +0300
  * Postfix for [MDEV-12619](https://jira.mariadb.org/browse/MDEV-12619) - test results adjusted
* [Revision #442a6f61f5](https://github.com/MariaDB/server/commit/442a6f61f5)\
  2017-07-18 13:50:26 +0300
  * Postfix for 74891ed257c43 - test result adjusted
* Merge [Revision #29acdcd542](https://github.com/MariaDB/server/commit/29acdcd542) 2017-07-13 07:21:21 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* Merge [Revision #daec000450](https://github.com/MariaDB/server/commit/daec000450) 2017-07-12 22:54:49 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #0f348bcd96](https://github.com/MariaDB/server/commit/0f348bcd96)\
  2017-07-12 22:51:06 +0400
  * [MDEV-13302](https://jira.mariadb.org/browse/MDEV-13302) Avoid using LEX::spname during CREATE PROCEDURE and CREATE FUNCTION
* Merge [Revision #e33bda183e](https://github.com/MariaDB/server/commit/e33bda183e) 2017-07-12 12:00:11 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #7c3df72d0a](https://github.com/MariaDB/server/commit/7c3df72d0a)\
  2017-07-12 11:57:47 +0400
  * [MDEV-13298](https://jira.mariadb.org/browse/MDEV-13298) Change sp\_head::m\_chistics from a pointer to a structure
* [Revision #31b3511849](https://github.com/MariaDB/server/commit/31b3511849)\
  2017-07-11 16:16:11 +0400
  * Fixing a type-clash bison warning in keyword\_directly\_not\_assignable
* [Revision #59350ce076](https://github.com/MariaDB/server/commit/59350ce076)\
  2017-07-11 15:10:25 +0400
  * [MDEV-13292](https://jira.mariadb.org/browse/MDEV-13292) Move the code from sp\_head::init() to sp\_head::sp\_head()
* [Revision #42cb3dcb74](https://github.com/MariaDB/server/commit/42cb3dcb74)\
  2017-07-10 12:24:58 +0400
  * (partial) [MDEV-12518](https://jira.mariadb.org/browse/MDEV-12518) Unify sql\_yacc.yy and sql\_yacc\_ora.yy
* [Revision #77ace5dbd1](https://github.com/MariaDB/server/commit/77ace5dbd1)\
  2017-07-10 10:51:07 +0400
  * (partial) [MDEV-12518](https://jira.mariadb.org/browse/MDEV-12518) Unify sql\_yacc.yy and sql\_yacc\_ora.yy
* [Revision #f3ad96a3a6](https://github.com/MariaDB/server/commit/f3ad96a3a6)\
  2017-07-08 01:38:56 +0200
  * fix the bad merge
* [Revision #c65cce3698](https://github.com/MariaDB/server/commit/c65cce3698)\
  2017-07-07 19:55:31 +0200
  * [MDEV-12137](https://jira.mariadb.org/browse/MDEV-12137) DELETE statement with the same source and target
* [Revision #abf95afa2a](https://github.com/MariaDB/server/commit/abf95afa2a)\
  2017-07-07 17:50:09 +0200
  * [MDEV-12137](https://jira.mariadb.org/browse/MDEV-12137) DELETE statement with the same source and target
* [Revision #51a552ddf2](https://github.com/MariaDB/server/commit/51a552ddf2)\
  2017-07-09 06:10:17 +0000
  * Fix debian control file syntax.
* [Revision #2312556bba](https://github.com/MariaDB/server/commit/2312556bba)\
  2017-07-08 21:57:54 +0000
  * Attempt to fix mariadb-backup debian packaging in 10.3
* Merge [Revision #0496430ffa](https://github.com/MariaDB/server/commit/0496430ffa) 2017-07-07 21:27:26 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* Merge [Revision #30fee6150a](https://github.com/MariaDB/server/commit/30fee6150a) 2017-07-07 19:48:35 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #c1885d22df](https://github.com/MariaDB/server/commit/c1885d22df)\
  2017-07-07 17:00:07 +0400
  * [MDEV-13273](https://jira.mariadb.org/browse/MDEV-13273) Confusion between table alias and ROW type variable
* [Revision #3c09f148f3](https://github.com/MariaDB/server/commit/3c09f148f3)\
  2017-07-07 13:08:16 +0300
  * [MDEV-12288](https://jira.mariadb.org/browse/MDEV-12288) Reset DB\_TRX\_ID when the history is removed, to speed up MVCC
* [Revision #bae0844f65](https://github.com/MariaDB/server/commit/bae0844f65)\
  2017-07-07 00:55:01 +0300
  * Introduce a new InnoDB redo log format for [MariaDB 10.3.1](../../old-releases/10.3/10.3.1.md)
* Merge [Revision #57fea53615](https://github.com/MariaDB/server/commit/57fea53615) 2017-07-07 12:39:43 +0300 - Merge bb-10.2-ext into 10.3
* Merge [Revision #9e53a6bdfd](https://github.com/MariaDB/server/commit/9e53a6bdfd) 2017-07-07 12:00:27 +0300 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #8b2c7c9444](https://github.com/MariaDB/server/commit/8b2c7c9444) 2017-07-07 12:43:10 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #3f32743294](https://github.com/MariaDB/server/commit/3f32743294)\
  2017-07-06 10:59:45 +0300
  * [MDEV-13020](https://jira.mariadb.org/browse/MDEV-13020) Server crashes in Item\_func\_nextval::val\_int...
* [Revision #7fee164faf](https://github.com/MariaDB/server/commit/7fee164faf)\
  2017-03-19 13:10:12 +1100
  * Remove dated my-{size}.cnf files
* Merge [Revision #3b9273d203](https://github.com/MariaDB/server/commit/3b9273d203) 2017-07-05 17:43:32 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #58dd72f18c](https://github.com/MariaDB/server/commit/58dd72f18c)\
  2017-07-05 17:18:33 +0400
  * [MDEV-13245](https://jira.mariadb.org/browse/MDEV-13245) Add struct AUTHID
* Merge [Revision #5c0df0e4a8](https://github.com/MariaDB/server/commit/5c0df0e4a8) 2017-07-04 15:31:25 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #25ad623d64](https://github.com/MariaDB/server/commit/25ad623d64)\
  2017-07-04 14:14:30 +0400
  * [MDEV-13240](https://jira.mariadb.org/browse/MDEV-13240) Wrong warning with MAX(datetime\_field) OVER (...)
* [Revision #760127ac6f](https://github.com/MariaDB/server/commit/760127ac6f)\
  2017-07-03 14:56:33 +0400
  * Adding sf\_return\_type, improving sf\_tail readability.
* [Revision #306bc90ad7](https://github.com/MariaDB/server/commit/306bc90ad7)\
  2017-07-03 09:15:28 +0400
  * Adding "const" qualifier to Column\_definition::make\_field()
* [Revision #96d1cdecbe](https://github.com/MariaDB/server/commit/96d1cdecbe)\
  2017-07-01 14:37:12 +0400
  * [MDEV-13197](https://jira.mariadb.org/browse/MDEV-13197) Parser refactoring for CREATE VIEW,TRIGGER,SP,UDF,EVENT
* [Revision #505a11d9ac](https://github.com/MariaDB/server/commit/505a11d9ac)\
  2017-06-30 16:26:15 +0400
  * Adding the "const" qualifier to st\_sp\_chistics parameters in a few functions.
* [Revision #95979d2bae](https://github.com/MariaDB/server/commit/95979d2bae)\
  2017-06-29 12:24:47 +0400
  * Removing duplicate code in mysql\_execute\_command: Adding prepare\_db\_action().
* [Revision #a4d9fa99ea](https://github.com/MariaDB/server/commit/a4d9fa99ea)\
  2017-07-03 10:39:18 +0200
  * Fix compiler warning in embedded server
* [Revision #c36620ddc3](https://github.com/MariaDB/server/commit/c36620ddc3)\
  2017-07-03 10:36:09 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179) post-merge fixes.
* Merge [Revision #1d91910b94](https://github.com/MariaDB/server/commit/1d91910b94) 2017-07-03 09:33:41 +0200 - [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #95e09f0766](https://github.com/MariaDB/server/commit/95e09f0766)\
  2017-05-11 08:45:29 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #b19f055772](https://github.com/MariaDB/server/commit/b19f055772)\
  2017-05-11 08:03:27 +0200
  * TokuDB .result file update following earlier commit.
* [Revision #105ea511dc](https://github.com/MariaDB/server/commit/105ea511dc)\
  2017-05-10 16:54:28 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #01b86a0ad9](https://github.com/MariaDB/server/commit/01b86a0ad9)\
  2017-05-10 15:48:32 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #0db2cd7c76](https://github.com/MariaDB/server/commit/0db2cd7c76)\
  2017-05-10 09:56:31 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #8683052389](https://github.com/MariaDB/server/commit/8683052389)\
  2017-04-29 11:19:09 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #c174718aed](https://github.com/MariaDB/server/commit/c174718aed)\
  2017-04-25 19:08:45 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #86fa6f9b3d](https://github.com/MariaDB/server/commit/86fa6f9b3d)\
  2017-04-25 12:00:43 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #59bab556a0](https://github.com/MariaDB/server/commit/59bab556a0)\
  2017-04-25 10:01:33 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #89aad233de](https://github.com/MariaDB/server/commit/89aad233de)\
  2017-04-23 10:49:58 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #1af3165f98](https://github.com/MariaDB/server/commit/1af3165f98)\
  2017-04-23 10:47:22 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #4a8381ad34](https://github.com/MariaDB/server/commit/4a8381ad34)\
  2017-04-23 10:46:07 +0200
  * Fix test to wait for slave to fully stop.
* [Revision #df2f01c14a](https://github.com/MariaDB/server/commit/df2f01c14a)\
  2017-04-23 10:44:45 +0200
  * Add cleanup of mysql.gtid\_slave\_pos table.
* [Revision #1b54cb3b77](https://github.com/MariaDB/server/commit/1b54cb3b77)\
  2017-04-20 16:22:21 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #8953c7e484](https://github.com/MariaDB/server/commit/8953c7e484)\
  2017-04-20 16:19:01 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #00eebb2243](https://github.com/MariaDB/server/commit/00eebb2243)\
  2017-04-20 16:16:26 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #638d4e90e8](https://github.com/MariaDB/server/commit/638d4e90e8)\
  2017-04-20 16:14:37 +0200
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #094e4b264c](https://github.com/MariaDB/server/commit/094e4b264c)\
  2017-04-20 16:11:14 +0200
  * Clarify plugin\_ref lifetimes in function comments
* [Revision #da9decdccf](https://github.com/MariaDB/server/commit/da9decdccf)\
  2017-04-20 16:07:27 +0200
  * Use separate connection for START SLAVE in rpl\_deadlock.test
* [Revision #fdf2d40770](https://github.com/MariaDB/server/commit/fdf2d40770)\
  2017-03-24 12:07:07 +0100
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #3cc89b3e85](https://github.com/MariaDB/server/commit/3cc89b3e85)\
  2017-03-24 12:06:29 +0100
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #4eebf431b0](https://github.com/MariaDB/server/commit/4eebf431b0)\
  2017-03-24 11:51:23 +0100
  * Fix that MTR leaks restart: options to following test
* [Revision #8bc1632ea5](https://github.com/MariaDB/server/commit/8bc1632ea5)\
  2017-03-20 13:29:37 +0100
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #363d6a16ae](https://github.com/MariaDB/server/commit/363d6a16ae)\
  2017-03-20 11:55:24 +0100
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #6a84473c28](https://github.com/MariaDB/server/commit/6a84473c28)\
  2017-03-14 12:54:10 +0100
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #3501a5356e](https://github.com/MariaDB/server/commit/3501a5356e)\
  2017-03-09 15:30:19 +0100
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #c995ecbe98](https://github.com/MariaDB/server/commit/c995ecbe98)\
  2017-03-09 13:27:27 +0100
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #087cf02328](https://github.com/MariaDB/server/commit/087cf02328)\
  2017-03-09 12:16:15 +0100
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #141a1b09e6](https://github.com/MariaDB/server/commit/141a1b09e6)\
  2017-03-08 13:56:29 +0100
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table
* [Revision #d3837c69a2](https://github.com/MariaDB/server/commit/d3837c69a2)\
  2017-03-06 15:32:54 +0100
  * [MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179): Per-engine mysql.gtid\_slave\_pos table.
* Merge [Revision #176000a54c](https://github.com/MariaDB/server/commit/176000a54c) 2017-06-27 08:14:45 +0300 - Merge bb-10.2-ext into 10.3
* Merge [Revision #43c77bb937](https://github.com/MariaDB/server/commit/43c77bb937) 2017-06-27 08:13:59 +0300 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #ed61fddf24](https://github.com/MariaDB/server/commit/ed61fddf24) 2017-06-21 12:14:35 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #2a3fe45dd2](https://github.com/MariaDB/server/commit/2a3fe45dd2)\
  2017-06-21 13:44:16 +0300
  * Remove XtraDB
* [Revision #99e017d099](https://github.com/MariaDB/server/commit/99e017d099)\
  2017-06-20 09:39:13 +0300
  * Remove INFORMATION\_SCHEMA.INNODB\_TRX.trx\_adaptive\_hash\_latched
* [Revision #813e6e628f](https://github.com/MariaDB/server/commit/813e6e628f)\
  2017-06-20 09:35:58 +0300
  * Adjust sys\_vars.sysvars\_innodb for 32-bit builds
* Merge [Revision #1e3886ae80](https://github.com/MariaDB/server/commit/1e3886ae80) 2017-06-19 17:28:08 +0300 - Merge bb-10.2-ext into 10.3
* Merge [Revision #3a7201ea92](https://github.com/MariaDB/server/commit/3a7201ea92) 2017-06-19 16:56:13 +0300 - Merge 10.2 into bb-10.2-ext
* [Revision #578d8bfde5](https://github.com/MariaDB/server/commit/578d8bfde5)\
  2017-06-19 10:44:13 +0400
  * Additional tests for [MDEV-10309](https://jira.mariadb.org/browse/MDEV-10309) COALESCE(12345678900) makes a column of a wrong type and truncates the data
* Merge [Revision #43eec57fab](https://github.com/MariaDB/server/commit/43eec57fab) 2017-06-15 18:02:57 +0300 - Merge 10.2 into bb-10.2-ext; also, fix [MDEV-13015](https://jira.mariadb.org/browse/MDEV-13015) After restart, InnoDB wrongly thinks that a SEQUENCE is a TABLE
* Merge [Revision #765347384a](https://github.com/MariaDB/server/commit/765347384a) 2017-06-15 15:27:11 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #3b1921c714](https://github.com/MariaDB/server/commit/3b1921c714)\
  2017-06-08 08:25:53 +0300
  * Re-record failing SEQUENCE tests
* [Revision #8a65b49c43](https://github.com/MariaDB/server/commit/8a65b49c43)\
  2017-06-07 16:09:33 +0300
  * Update sql\_yacc\_ora.yy with latest changes of sql\_yacc.yy
* [Revision #3d428e017d](https://github.com/MariaDB/server/commit/3d428e017d)\
  2017-06-03 16:16:18 +0300
  * Cleanups (LINT\_INIT & --debug-mutex-deadlock-detector
* [Revision #36ae8846ca](https://github.com/MariaDB/server/commit/36ae8846ca)\
  2017-06-03 16:08:23 +0300
  * Fixed sequences based on comments from Peter Gulutzan and Andrii Nikitin
* [Revision #3356e42d01](https://github.com/MariaDB/server/commit/3356e42d01)\
  2017-06-02 13:52:47 +0300
  * Improved warning "xxx is not BASE TABLE/SEQUENCE"
* [Revision #0fe7d8a2a2](https://github.com/MariaDB/server/commit/0fe7d8a2a2)\
  2017-06-13 12:46:33 +0400
  * [MDEV-12292](https://jira.mariadb.org/browse/MDEV-12292) - port "Report timing with more precision" by @dveeden
* [Revision #1a873fb865](https://github.com/MariaDB/server/commit/1a873fb865)\
  2017-06-08 12:27:16 +0200
  * replace my\_timer\_microseconds with microsecond\_interval\_timer
* [Revision #eede812f05](https://github.com/MariaDB/server/commit/eede812f05)\
  2017-06-08 12:16:13 +0200
  * Fix whitespace in new code
* [Revision #6486bac29f](https://github.com/MariaDB/server/commit/6486bac29f)\
  2017-06-08 12:11:16 +0200
  * Callers of start\_timer should have ulonglong data type
* [Revision #ca2d9546c8](https://github.com/MariaDB/server/commit/ca2d9546c8)\
  2017-03-09 17:57:22 +0100
  * port "Report timing with more precision" by @dveeden
* [Revision #86b9417035](https://github.com/MariaDB/server/commit/86b9417035)\
  2017-05-09 13:37:08 +0200
  * 10.3 man pages
* [Revision #0c92794db3](https://github.com/MariaDB/server/commit/0c92794db3)\
  2017-06-01 13:03:55 +0300
  * Remove deprecated InnoDB file format parameters
* Merge [Revision #3d615e4b1a](https://github.com/MariaDB/server/commit/3d615e4b1a) 2017-06-01 11:02:32 +0300 - Merge branch 'bb-10.2-ext' into 10.3
* [Revision #959891662d](https://github.com/MariaDB/server/commit/959891662d)\
  2017-05-30 21:31:30 +0300
  * [MDEV-12930](https://jira.mariadb.org/browse/MDEV-12930) Testing SEQUENCE object
* [Revision #d5d8fa6e04](https://github.com/MariaDB/server/commit/d5d8fa6e04)\
  2017-05-30 12:55:58 +0300
  * Updated test case
* [Revision #267bd4cc7b](https://github.com/MariaDB/server/commit/267bd4cc7b)\
  2017-05-29 16:40:24 +0300
  * Add automatic updating of sub modules to BUILD scripts
* [Revision #7e5bd1500f](https://github.com/MariaDB/server/commit/7e5bd1500f)\
  2017-05-29 16:08:11 +0300
  * Add locks for sequence's to ensure that there is only one writer or many readers
* [Revision #d7e3120da8](https://github.com/MariaDB/server/commit/d7e3120da8)\
  2017-05-22 16:57:41 +0200
  * SP stack trace
* [Revision #8b68263a53](https://github.com/MariaDB/server/commit/8b68263a53)\
  2017-05-29 10:29:46 +0400
  * [MDEV-12803](https://jira.mariadb.org/browse/MDEV-12803) Improve function parameter data type control
* [Revision #0f0bced885](https://github.com/MariaDB/server/commit/0f0bced885)\
  2017-05-27 16:45:22 +0400
  * Adding tests for [MDEV-9410](https://jira.mariadb.org/browse/MDEV-9410) VIEW over a ROLLUP query reports too large columns
* [Revision #a9b79bf710](https://github.com/MariaDB/server/commit/a9b79bf710)\
  2017-05-27 16:39:20 +0400
  * Adding tests for [MDEV-12861](https://jira.mariadb.org/browse/MDEV-12861) FIRST\_VALUE() does not preserve the exact data type
* [Revision #241d5edcf9](https://github.com/MariaDB/server/commit/241d5edcf9)\
  2017-05-27 16:21:20 +0400
  * Adding tests for [MDEV-9408](https://jira.mariadb.org/browse/MDEV-9408) CREATE TABLE SELECT MAX(int\_column) creates different columns for table vs view
* [Revision #86b5be0e16](https://github.com/MariaDB/server/commit/86b5be0e16)\
  2017-05-27 16:13:58 +0400
  * Adding tests for [MDEV-9406](https://jira.mariadb.org/browse/MDEV-9406) CREATE TABLE..SELECT creates different columns for IFNULL() and equivalent COALESCE,CASE,IF
* [Revision #13c6b0d534](https://github.com/MariaDB/server/commit/13c6b0d534)\
  2017-05-27 16:03:18 +0400
  * [MDEV-10309](https://jira.mariadb.org/browse/MDEV-10309) COALESCE(12345678900) makes a column of a wrong type and truncates the data
* [Revision #9d834c76af](https://github.com/MariaDB/server/commit/9d834c76af)\
  2017-05-27 11:12:14 +0400
  * [MDEV-12932](https://jira.mariadb.org/browse/MDEV-12932) Remove enum Cast\_target and use Type\_handler to handle CAST
* [Revision #f462bfc1f7](https://github.com/MariaDB/server/commit/f462bfc1f7)\
  2017-05-27 07:05:16 +0400
  * A post-merge fix: loadxml failed on Windows (due to a wrong parameter to my\_error).
* Merge [Revision #9bc3225642](https://github.com/MariaDB/server/commit/9bc3225642) 2017-05-26 19:32:28 +0400 - Merge tag 'mariadb-10.2.6' into bb-10.2-ext
* [Revision #77b2f55f61](https://github.com/MariaDB/server/commit/77b2f55f61)\
  2017-05-26 09:42:11 +0300
  * Follow-up fixes for [MDEV-10139](https://jira.mariadb.org/browse/MDEV-10139) Support for InnoDB SEQUENCE objects
* [Revision #e1f81822c3](https://github.com/MariaDB/server/commit/e1f81822c3)\
  2017-05-25 17:19:35 +0400
  * A cleanup for [MDEV-11514](https://jira.mariadb.org/browse/MDEV-11514), [MDEV-11497](https://jira.mariadb.org/browse/MDEV-11497), [MDEV-11554](https://jira.mariadb.org/browse/MDEV-11554), [MDEV-11555](https://jira.mariadb.org/browse/MDEV-11555) - IN and CASE type aggregation problems
* [Revision #109bc47084](https://github.com/MariaDB/server/commit/109bc47084)\
  2017-05-25 15:15:39 +0400
  * Fixing a few data type related problems: [MDEV-12875](https://jira.mariadb.org/browse/MDEV-12875), [MDEV-12886](https://jira.mariadb.org/browse/MDEV-12886), [MDEV-12916](https://jira.mariadb.org/browse/MDEV-12916)
* [Revision #54e29712a3](https://github.com/MariaDB/server/commit/54e29712a3)\
  2017-05-25 14:12:18 +0400
  * Adding tests for [MDEV-12917](https://jira.mariadb.org/browse/MDEV-12917) Wrong data type for CREATE..SELECT year\_sp\_variable
* [Revision #a4789f52d8](https://github.com/MariaDB/server/commit/a4789f52d8)\
  2017-05-24 18:57:47 +0300
  * More tests for SEQUENCE's
* [Revision #8acf4d6f78](https://github.com/MariaDB/server/commit/8acf4d6f78)\
  2017-05-24 18:09:22 +0300
  * Follow-up fixes for [MDEV-10139](https://jira.mariadb.org/browse/MDEV-10139) Support for InnoDB SEQUENCE objects
* [Revision #9497a64679](https://github.com/MariaDB/server/commit/9497a64679)\
  2017-05-24 15:39:24 +0300
  * Fixed failing test sql\_sequence.replication
* [Revision #d60e5fe391](https://github.com/MariaDB/server/commit/d60e5fe391)\
  2017-05-24 15:10:04 +0300
  * Simple replication test for sequences
* [Revision #e5145a5ac3](https://github.com/MariaDB/server/commit/e5145a5ac3)\
  2017-05-24 15:43:09 +0400
  * [MDEV-12546](https://jira.mariadb.org/browse/MDEV-12546) Wrong metadata or data type for string user variables
* [Revision #90f06818b3](https://github.com/MariaDB/server/commit/90f06818b3)\
  2017-05-23 23:13:54 +0400
  * [MDEV-12876](https://jira.mariadb.org/browse/MDEV-12876) Wrong data type for CREATE..SELECT sp\_var
* [Revision #62b62319bf](https://github.com/MariaDB/server/commit/62b62319bf)\
  2017-05-23 23:11:31 +0400
  * A cleanup for the patch for [MDEV-12852](https://jira.mariadb.org/browse/MDEV-12852), [MDEV-12853](https://jira.mariadb.org/browse/MDEV-12853), [MDEV-12869](https://jira.mariadb.org/browse/MDEV-12869)
* [Revision #6a779a6d28](https://github.com/MariaDB/server/commit/6a779a6d28)\
  2017-05-23 17:18:31 +0300
  * Make SEQUENCE working with replication
* [Revision #d9304914be](https://github.com/MariaDB/server/commit/d9304914be)\
  2017-05-23 12:45:47 +0400
  * Fixing a few problems with data type and metadata for INT result functions ([MDEV-12852](https://jira.mariadb.org/browse/MDEV-12852), [MDEV-12853](https://jira.mariadb.org/browse/MDEV-12853), [MDEV-12869](https://jira.mariadb.org/browse/MDEV-12869))
* [Revision #9b79888df8](https://github.com/MariaDB/server/commit/9b79888df8)\
  2017-05-22 17:13:15 +0400
  * [MDEV-12866](https://jira.mariadb.org/browse/MDEV-12866) Out-of-range error with CREATE..SELECT..TO\_SECONDS(NOW())
* [Revision #c84bbeda7f](https://github.com/MariaDB/server/commit/c84bbeda7f)\
  2017-05-22 13:44:26 +0400
  * [MDEV-12858](https://jira.mariadb.org/browse/MDEV-12858) + MDEV+12859 + [MDEV-12862](https://jira.mariadb.org/browse/MDEV-12862) - a join patch fixing a few data type problems with CREATE..SELECT
* [Revision #feb15f4e45](https://github.com/MariaDB/server/commit/feb15f4e45)\
  2017-05-22 10:27:05 +0400
  * [MDEV-12860](https://jira.mariadb.org/browse/MDEV-12860) Out-of-range error on CREATE..SELECT with a view using MAX and EXTRACT(MINUTE\_MICROSECOND..)
* [Revision #8c479820da](https://github.com/MariaDB/server/commit/8c479820da)\
  2017-05-21 09:28:12 +0400
  * [MDEV-12856](https://jira.mariadb.org/browse/MDEV-12856) Wrong .. metadata for DIV + [MDEV-12857](https://jira.mariadb.org/browse/MDEV-12857)..errors on CREATE..SELECT..DIV
* [Revision #a8caa8e04a](https://github.com/MariaDB/server/commit/a8caa8e04a)\
  2017-05-20 16:29:11 +0400
  * [MDEV-12854](https://jira.mariadb.org/browse/MDEV-12854) Synchronize CREATE..SELECT data type and result set metadata data type for INT functions
* [Revision #d2fec340d2](https://github.com/MariaDB/server/commit/d2fec340d2)\
  2017-05-19 21:39:41 +0400
  * An after-fix for [MDEV-12849](https://jira.mariadb.org/browse/MDEV-12849) Out-of-range errors when casting hex-hybrid to SIGNED and UNSIGNED
* [Revision #ac4ce47b09](https://github.com/MariaDB/server/commit/ac4ce47b09)\
  2017-05-19 18:45:01 +0400
  * [MDEV-12849](https://jira.mariadb.org/browse/MDEV-12849) Out-of-range errors when casting hex-hybrid to SIGNED and UNSIGNED
* Merge [Revision #732cfabafd](https://github.com/MariaDB/server/commit/732cfabafd) 2017-05-18 14:23:14 +0400 - Merge branch 'halfspawn-bb-10.2-ext' into bb-10.2-ext
* [Revision #87d952746f](https://github.com/MariaDB/server/commit/87d952746f)\
  2017-05-18 11:43:24 +0200
  * [MDEV-12783](https://jira.mariadb.org/browse/MDEV-12783) : sql\_mode=ORACLE: Functions LENGTH() and LENGTHB()
* [Revision #5b034f1cf8](https://github.com/MariaDB/server/commit/5b034f1cf8)\
  2017-05-17 18:07:20 +0400
  * [MDEV-12833](https://jira.mariadb.org/browse/MDEV-12833) Split Column\_definition::create\_length\_to\_internal\_length() to virtual methods in Type\_handler
* [Revision #278c3ea756](https://github.com/MariaDB/server/commit/278c3ea756)\
  2017-05-17 14:02:25 +0400
  * [MDEV-12826](https://jira.mariadb.org/browse/MDEV-12826) Add Type\_handler::val\_int\_signed\_typecast() and Type\_handler::val\_int\_unsigned\_typecast()
* Merge [Revision #896c2c73a0](https://github.com/MariaDB/server/commit/896c2c73a0) 2017-05-17 12:59:07 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #fba7fbbc5c](https://github.com/MariaDB/server/commit/fba7fbbc5c)\
  2017-05-17 12:21:39 +0400
  * [MDEV-9397](https://jira.mariadb.org/browse/MDEV-9397) Split field.cc:calc\_pack\_length() into virtual methods in Type\_handler
* [Revision #f1b729d352](https://github.com/MariaDB/server/commit/f1b729d352)\
  2017-05-16 14:29:51 +0400
  * [MDEV-9188](https://jira.mariadb.org/browse/MDEV-9188) Split Column\_definition::check() into virtual methods in Type\_handler
* [Revision #705fc43eaa](https://github.com/MariaDB/server/commit/705fc43eaa)\
  2017-05-10 15:29:48 +0400
  * [MDEV-12775](https://jira.mariadb.org/browse/MDEV-12775) Reuse data type aggregation code for hybrid functions and UNION
* [Revision #7c44b8afb7](https://github.com/MariaDB/server/commit/7c44b8afb7)\
  2017-05-15 14:58:05 +0400
  * [MDEV-12798](https://jira.mariadb.org/browse/MDEV-12798) Item\_param does not preserve exact field type in EXECUTE IMMEDIATE 'CREATE TABLE AS SELECT ?' USING POINT(1,1)
* [Revision #38acc29ccb](https://github.com/MariaDB/server/commit/38acc29ccb)\
  2017-05-13 16:52:53 +0300
  * Fixed buildbot failures with --embedded-server
* [Revision #238eb41005](https://github.com/MariaDB/server/commit/238eb41005)\
  2017-05-11 19:39:49 +0400
  * [MDEV-12784](https://jira.mariadb.org/browse/MDEV-12784) Change Item\_func\_length::print() to display octet\_length() rather than length()
* [Revision #7beb8ff274](https://github.com/MariaDB/server/commit/7beb8ff274)\
  2017-05-11 07:27:11 +0400
  * A --ps cleanup for [MDEV-12658](https://jira.mariadb.org/browse/MDEV-12658) Make the third parameter to LPAD and RPAD optional
* [Revision #533506b4ed](https://github.com/MariaDB/server/commit/533506b4ed)\
  2017-05-10 18:14:08 +0400
  * [MDEV-12777](https://jira.mariadb.org/browse/MDEV-12777) Change Lex\_field\_type\_st::m\_type from enum\_field\_types to Type\_handler pointer
* [Revision #191638416b](https://github.com/MariaDB/server/commit/191638416b)\
  2017-05-10 11:02:02 +0400
  * [MDEV-12772](https://jira.mariadb.org/browse/MDEV-12772) Add Field::get\_typelib() and Item::get\_typelib()
* [Revision #0f642188cc](https://github.com/MariaDB/server/commit/0f642188cc)\
  2017-05-10 09:27:15 +0400
  * [MDEV-12771](https://jira.mariadb.org/browse/MDEV-12771) Remove Item\_func\_xxx::decimal\_precision() for case and abbreviations
* [Revision #cd32f84214](https://github.com/MariaDB/server/commit/cd32f84214)\
  2017-05-10 08:30:56 +0400
  * [MDEV-12770](https://jira.mariadb.org/browse/MDEV-12770) Add Type\_handler::decimal\_precision() + [MDEV-12769](https://jira.mariadb.org/browse/MDEV-12769)
* [Revision #18ad176809](https://github.com/MariaDB/server/commit/18ad176809)\
  2017-05-04 15:57:19 +0200
  * [MDEV-12685](https://jira.mariadb.org/browse/MDEV-12685) Oracle-compatible function CHR()
* [Revision #71fa413c16](https://github.com/MariaDB/server/commit/71fa413c16)\
  2017-05-08 02:44:55 +0300
  * [MDEV-10139](https://jira.mariadb.org/browse/MDEV-10139) Support for SEQUENCE objects
* [Revision #1e04ad284c](https://github.com/MariaDB/server/commit/1e04ad284c)\
  2017-05-07 18:26:10 +0300
  * Fixed compiler warnings and warnings from build.tags
* [Revision #276b0c8ef0](https://github.com/MariaDB/server/commit/276b0c8ef0)\
  2017-05-02 19:23:00 +0300
  * Fixed crash with SEQUENCE when using REPAIR
* [Revision #6378c95ee0](https://github.com/MariaDB/server/commit/6378c95ee0)\
  2017-05-17 00:34:48 +0300
  * Fix that end\_bulk\_insert() doesn't write to to-be-deleted files
* Merge [Revision #314350a722](https://github.com/MariaDB/server/commit/314350a722) 2017-05-07 23:51:18 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #c619fbeafe](https://github.com/MariaDB/server/commit/c619fbeafe)\
  2017-05-07 19:41:19 +0400
  * Adding MYSQL\_PLUGIN\_IMPORT to type\_handler\_xxx declarations (fixing compilation failure on Windows)
* [Revision #da63db1e3b](https://github.com/MariaDB/server/commit/da63db1e3b)\
  2017-05-07 19:29:23 +0400
  * [MDEV-12719](https://jira.mariadb.org/browse/MDEV-12719) Determine Item::result\_type() from Item::type\_handler()
* [Revision #02ada41744](https://github.com/MariaDB/server/commit/02ada41744)\
  2017-05-07 17:44:27 +0400
  * [MDEV-12721](https://jira.mariadb.org/browse/MDEV-12721) Wrong execution plan for WHERE (date\_field <=> timestamp\_expr AND TRUE)
* [Revision #4e9022b48b](https://github.com/MariaDB/server/commit/4e9022b48b)\
  2017-05-07 09:12:54 +0400
  * [MDEV-12718](https://jira.mariadb.org/browse/MDEV-12718) Determine Item::cmp\_type() from Item::type\_handler()
* [Revision #cc694792c9](https://github.com/MariaDB/server/commit/cc694792c9)\
  2017-05-07 01:02:37 +0400
  * [MDEV-12717](https://jira.mariadb.org/browse/MDEV-12717) Change Item\_equal to operate Type\_handler rather than Item\_result
* [Revision #aea54a11a6](https://github.com/MariaDB/server/commit/aea54a11a6)\
  2017-05-06 23:06:18 +0400
  * [MDEV-12716](https://jira.mariadb.org/browse/MDEV-12716) Change Value\_source::Context to operate Type\_handler rather than Item\_result
* [Revision #c898de84b7](https://github.com/MariaDB/server/commit/c898de84b7)\
  2017-05-06 20:44:05 +0400
  * [MDEV-12714](https://jira.mariadb.org/browse/MDEV-12714) Determine Item::field\_type() from Item::type\_handler()
* [Revision #46239f29c6](https://github.com/MariaDB/server/commit/46239f29c6)\
  2017-05-06 19:12:59 +0400
  * [MDEV-12713](https://jira.mariadb.org/browse/MDEV-12713) Define virtual type\_handler() for all Item classes
* [Revision #5a644e177f](https://github.com/MariaDB/server/commit/5a644e177f)\
  2017-05-06 15:05:59 +0400
  * Adding "const" qualifier to Item::cols(), and to the "Item \*cmp" parameter to Type\_handler::make\_const\_item\_for\_comparison()
* [Revision #9a360e97a2](https://github.com/MariaDB/server/commit/9a360e97a2)\
  2017-05-06 14:52:18 +0400
  * Cleanup: changing set\_handler\_by\_field\_type(field\_type()) to set\_handler(type\_handler()).
* [Revision #380ec90905](https://github.com/MariaDB/server/commit/380ec90905)\
  2017-05-06 13:34:16 +0400
  * [MDEV-12710](https://jira.mariadb.org/browse/MDEV-12710) Fix Item\_cache constructors to accept Type\_handler instead of enum\_field\_types
* [Revision #26fa7232cf](https://github.com/MariaDB/server/commit/26fa7232cf)\
  2017-05-06 00:04:15 +0400
  * [MDEV-12707](https://jira.mariadb.org/browse/MDEV-12707) Split resolve\_const\_item() into virtual methods in Type\_handler
* Merge [Revision #ac53b49b1b](https://github.com/MariaDB/server/commit/ac53b49b1b) 2017-05-05 16:12:54 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* Merge [Revision #39e3167193](https://github.com/MariaDB/server/commit/39e3167193) 2017-05-05 07:25:11 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #583b68e899](https://github.com/MariaDB/server/commit/583b68e899)\
  2017-05-05 07:23:16 +0400
  * [MDEV-12560](https://jira.mariadb.org/browse/MDEV-12560), [MDEV-12665](https://jira.mariadb.org/browse/MDEV-12665) - geometry type not preserved in hybrid functions and UNION
* [Revision #aacb4d57ca](https://github.com/MariaDB/server/commit/aacb4d57ca)\
  2017-05-05 07:00:18 +0400
  * [MDEV-12695](https://jira.mariadb.org/browse/MDEV-12695) Add Column\_definition::type\_handler()
* [Revision #1ff79562b8](https://github.com/MariaDB/server/commit/1ff79562b8)\
  2017-05-04 18:30:11 +0400
  * [MDEV-12692](https://jira.mariadb.org/browse/MDEV-12692) Split Item\_func\_between::fix\_length\_and\_dec
* Merge [Revision #4991eab483](https://github.com/MariaDB/server/commit/4991eab483) 2017-05-04 16:29:05 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #fe127562e2](https://github.com/MariaDB/server/commit/fe127562e2)\
  2017-05-04 16:05:21 +0400
  * [MDEV-12687](https://jira.mariadb.org/browse/MDEV-12687) Split Item::send() into virtual method in Type\_handler
* [Revision #ae5b31fe52](https://github.com/MariaDB/server/commit/ae5b31fe52)\
  2017-05-04 13:17:12 +0400
  * A cleanup for [MDEV-12619](https://jira.mariadb.org/browse/MDEV-12619) UNION creates excessive integer column types for integer literals
* [Revision #01b308c39c](https://github.com/MariaDB/server/commit/01b308c39c)\
  2017-05-04 11:38:55 +0400
  * [MDEV-12617](https://jira.mariadb.org/browse/MDEV-12617) CASE and CASE-alike hybrid functions do not preserve exact data types
* [Revision #78a891c87b](https://github.com/MariaDB/server/commit/78a891c87b)\
  2017-05-04 09:56:09 +0400
  * A partial patch for [MDEV-12518](https://jira.mariadb.org/browse/MDEV-12518) Unify sql\_yacc.yy and sql\_yacc\_ora.yy
* Merge [Revision #7a70641f10](https://github.com/MariaDB/server/commit/7a70641f10) 2017-05-04 06:58:28 +0400 - Merge branch 'halfspawn-bb-10.2-ext' into bb-10.2-ext
* [Revision #850d3bafca](https://github.com/MariaDB/server/commit/850d3bafca)\
  2017-05-03 17:39:45 +0200
  * [MDEV-12658](https://jira.mariadb.org/browse/MDEV-12658) Make the third parameter to LPAD and RPAD optional
* [Revision #736a1d29bc](https://github.com/MariaDB/server/commit/736a1d29bc)\
  2017-05-03 13:43:22 +0400
  * Adding Item\_func\_pad as a common parent for Item\_func\_lpad and Item\_func\_rpad
* [Revision #1bcbe6fc2b](https://github.com/MariaDB/server/commit/1bcbe6fc2b)\
  2017-05-02 19:19:23 +0300
  * Fixed build scripts to compile MyRocks as a plugin
* [Revision #8bc88a4940](https://github.com/MariaDB/server/commit/8bc88a4940)\
  2017-05-02 15:58:26 +0400
  * Fixing a warning: ‘class Type\_all\_attributes’ has ... non-virtual destructor
* Merge [Revision #280866d38d](https://github.com/MariaDB/server/commit/280866d38d) 2017-05-02 13:52:45 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #746f794c43](https://github.com/MariaDB/server/commit/746f794c43)\
  2017-05-02 13:51:35 +0400
  * [MDEV-12657](https://jira.mariadb.org/browse/MDEV-12657) A few tests fail in build-bot on Windows after changing Field::field\_name and Item::name to LEX\_CSTRING
* [Revision #07143a7393](https://github.com/MariaDB/server/commit/07143a7393)\
  2017-05-02 12:58:25 +0400
  * [MDEV-12659](https://jira.mariadb.org/browse/MDEV-12659) Add THD::make\_string\_literal()
* [Revision #85b73e2254](https://github.com/MariaDB/server/commit/85b73e2254)\
  2017-05-02 11:39:20 +0400
  * [MDEV-12656](https://jira.mariadb.org/browse/MDEV-12656) Crash in CREATE..SELECT..UNION with a ENUM column and NULL
* [Revision #50b70e765b](https://github.com/MariaDB/server/commit/50b70e765b)\
  2017-05-02 07:49:06 +0400
  * [MDEV-12655](https://jira.mariadb.org/browse/MDEV-12655) Move Item\_func::count\_xxx\_length() to Type\_std\_attributes
* [Revision #c67971a8a3](https://github.com/MariaDB/server/commit/c67971a8a3)\
  2017-04-30 22:50:37 +0400
  * [MDEV-12649](https://jira.mariadb.org/browse/MDEV-12649) Add Type\_handler::Item\_save\_in\_value
* [Revision #7a19c59c00](https://github.com/MariaDB/server/commit/7a19c59c00)\
  2017-04-29 21:34:57 +0400
  * [MDEV-9395](https://jira.mariadb.org/browse/MDEV-9395) Add Type\_handler::Item\_decimal\_scale() and Item\_divisor\_precision\_increment()
* [Revision #ea18b11235](https://github.com/MariaDB/server/commit/ea18b11235)\
  2017-04-28 16:27:55 +0400
  * [MDEV-12619](https://jira.mariadb.org/browse/MDEV-12619) UNION creates excessive integer column types for integer literals
* [Revision #a147eea62c](https://github.com/MariaDB/server/commit/a147eea62c)\
  2017-04-27 21:58:10 +0400
  * [MDEV-12607](https://jira.mariadb.org/browse/MDEV-12607) Hybrid functions create wrong VARBINARY length when mixing character and binary data
* [Revision #9346939545](https://github.com/MariaDB/server/commit/9346939545)\
  2017-04-27 15:40:16 +0400
  * [MDEV-12601](https://jira.mariadb.org/browse/MDEV-12601) Hybrid functions create a column of an impossible type DOUBLE(256,4)
* [Revision #cfb4d9f9dc](https://github.com/MariaDB/server/commit/cfb4d9f9dc)\
  2017-04-27 15:02:35 +0400
  * [MDEV-12592](https://jira.mariadb.org/browse/MDEV-12592) Illegal mix of collations with the HEX function
* [Revision #441349aa06](https://github.com/MariaDB/server/commit/441349aa06)\
  2017-04-27 14:37:27 +0400
  * [MDEV-12588](https://jira.mariadb.org/browse/MDEV-12588) Add Type\_handler::type\_handler\_for\_tmp\_table() and Type\_handler::type\_handler\_for\_union()
* [Revision #b445c1ebb5](https://github.com/MariaDB/server/commit/b445c1ebb5)\
  2017-04-26 10:52:18 +0400
  * Fixing compilation failure on Windows: moving references to type\_handler\_xxx from field.h to field.cc
* [Revision #852f2305b9](https://github.com/MariaDB/server/commit/852f2305b9)\
  2017-04-26 10:37:05 +0400
  * Fixing a typo: UINT32\_MAX -> UINT\_MAX32 (introduced by the patch for [MDEV-9217](https://jira.mariadb.org/browse/MDEV-9217))
* [Revision #61a771df00](https://github.com/MariaDB/server/commit/61a771df00)\
  2017-04-26 09:49:41 +0400
  * Moving a part of st\_select\_lex\_unit::prepare() into a new method prepare\_join()
* [Revision #2fd635409d](https://github.com/MariaDB/server/commit/2fd635409d)\
  2017-04-25 14:22:07 +0400
  * [MDEV-12426](https://jira.mariadb.org/browse/MDEV-12426) Add Field::type\_handler() + [MDEV-12432](https://jira.mariadb.org/browse/MDEV-12432)
* [Revision #57bcc70fdc](https://github.com/MariaDB/server/commit/57bcc70fdc)\
  2017-04-25 11:05:41 +0400
  * [MDEV-12582](https://jira.mariadb.org/browse/MDEV-12582) Wrong data type for CREATE..SELECT MAX(COALESCE(timestamp\_column))
* [Revision #6cc40856ee](https://github.com/MariaDB/server/commit/6cc40856ee)\
  2017-04-25 10:20:27 +0400
  * A safety patch for [MDEV-9217](https://jira.mariadb.org/browse/MDEV-9217) Split Item::tmp\_table\_field\_from\_field\_type() into virtual methods in Type\_handler
* [Revision #5f1544fef3](https://github.com/MariaDB/server/commit/5f1544fef3)\
  2017-04-24 16:08:28 +0400
  * A cleanup for [MDEV-9217](https://jira.mariadb.org/browse/MDEV-9217) Split Item::tmp\_table\_field\_from\_field\_type() into virtual methods in Type\_handler
* [Revision #791374354c](https://github.com/MariaDB/server/commit/791374354c)\
  2017-04-24 12:09:25 +0400
  * [MDEV-9217](https://jira.mariadb.org/browse/MDEV-9217) Split Item::tmp\_table\_field\_from\_field\_type() into virtual methods in Type\_handler
* [Revision #3cd7690a5e](https://github.com/MariaDB/server/commit/3cd7690a5e)\
  2017-04-24 10:57:31 +0400
  * [MDEV-12568](https://jira.mariadb.org/browse/MDEV-12568) Add Type\_handler::subquery\_type\_allows\_materialization()
* Merge [Revision #79ecd75afd](https://github.com/MariaDB/server/commit/79ecd75afd) 2017-04-24 09:54:12 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #5a759d31f7](https://github.com/MariaDB/server/commit/5a759d31f7)\
  2017-04-23 19:39:57 +0300
  * Changing field::field\_name and Item::name to LEX\_CSTRING
* [Revision #cba84469eb](https://github.com/MariaDB/server/commit/cba84469eb)\
  2017-04-23 13:56:50 +0300
  * Fixed compiler warnings and wrong test results
* [Revision #f82212946f](https://github.com/MariaDB/server/commit/f82212946f)\
  2017-04-23 12:57:26 +0400
  * Fixing a bug in the recent commit that added trigger names into error messages
* [Revision #658082551f](https://github.com/MariaDB/server/commit/658082551f)\
  2017-04-22 23:47:27 +0400
  * [MDEV-12506](https://jira.mariadb.org/browse/MDEV-12506) Split Item\_func\_min\_max::fix\_length\_and\_dec() into methods in Type\_handler + [MDEV-12497](https://jira.mariadb.org/browse/MDEV-12497) + [MDEV-12504](https://jira.mariadb.org/browse/MDEV-12504)
* [Revision #ba670edfa3](https://github.com/MariaDB/server/commit/ba670edfa3)\
  2017-04-22 21:59:00 +0400
  * [MDEV-12559](https://jira.mariadb.org/browse/MDEV-12559) Split Item::temporal\_precision() into virtual methods in Type\_handler
* [Revision #b781408601](https://github.com/MariaDB/server/commit/b781408601)\
  2017-04-22 16:49:26 +0400
  * [MDEV-9235](https://jira.mariadb.org/browse/MDEV-9235) Add Type\_handler::is\_param\_long\_data\_type()
* Merge [Revision #530396cef0](https://github.com/MariaDB/server/commit/530396cef0) 2017-04-22 23:49:47 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* Merge [Revision #ef6e03d38d](https://github.com/MariaDB/server/commit/ef6e03d38d) 2017-04-20 08:49:48 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #33b6a347e4](https://github.com/MariaDB/server/commit/33b6a347e4)\
  2017-04-20 08:30:23 +0400
  * [MDEV-12533](https://jira.mariadb.org/browse/MDEV-12533) sql\_mode=ORACLE: Add support for database qualified sequence names in NEXTVAL and CURRVAL
* [Revision #e112eb19c4](https://github.com/MariaDB/server/commit/e112eb19c4)\
  2017-04-20 08:26:34 +0400
  * Recording correct test results in funcs\_1.myisam\_trig\_0407, related to the recent "Trigger already exists" change.
* [Revision #e6c11717bf](https://github.com/MariaDB/server/commit/e6c11717bf)\
  2017-04-19 22:10:36 +0300
  * Fixed wrong prototype in ha\_cassandra.cc that broke linking
* [Revision #847eb24b17](https://github.com/MariaDB/server/commit/847eb24b17)\
  2017-04-19 22:09:43 +0300
  * Fixed some wrong/inconsistent error message
* [Revision #b478276b04](https://github.com/MariaDB/server/commit/b478276b04)\
  2017-04-19 13:16:34 +0300
  * Removed complex and wrong set\_name\_for\_rollback()
* Merge [Revision #7ba0cfc8ae](https://github.com/MariaDB/server/commit/7ba0cfc8ae) 2017-04-19 05:21:36 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #e2b03cd3b5](https://github.com/MariaDB/server/commit/e2b03cd3b5)\
  2017-04-19 05:20:19 +0400
  * [MDEV-12514](https://jira.mariadb.org/browse/MDEV-12514) Split Item\_temporal\_func::fix\_length\_and\_dec() + [MDEV-12515](https://jira.mariadb.org/browse/MDEV-12515)
* [Revision #634f918692](https://github.com/MariaDB/server/commit/634f918692)\
  2017-04-18 12:16:34 +0300
  * Add multiple parsing protection to include/mysqld\_error.h
* [Revision #a30c225e53](https://github.com/MariaDB/server/commit/a30c225e53)\
  2017-04-17 20:41:27 +0300
  * Avoid DBUG\_ASSERT in mysqlcheck when working with views
* [Revision #a05a610d60](https://github.com/MariaDB/server/commit/a05a610d60)\
  2017-04-16 22:40:39 +0300
  * Added "const" to new data for handler::update\_row()
* [Revision #d82ac8eaaf](https://github.com/MariaDB/server/commit/d82ac8eaaf)\
  2017-04-16 17:14:41 +0300
  * Change "static int" to enum in classes
* [Revision #00946f4331](https://github.com/MariaDB/server/commit/00946f4331)\
  2017-04-16 17:08:00 +0300
  * Simple cleanups
* [Revision #f2ccc595b6](https://github.com/MariaDB/server/commit/f2ccc595b6)\
  2017-04-15 15:51:57 +0400
  * Derive Item\_func\_makedate from Item\_datefunc rather than Item\_temporal\_func
* [Revision #64e63131f8](https://github.com/MariaDB/server/commit/64e63131f8)\
  2017-04-14 21:27:33 +0400
  * Moving implementation of Item\_hybrid\_func::fix\_attributes() from item\_cmpfunc.cc to item\_func.cc
* [Revision #f89a5c9a25](https://github.com/MariaDB/server/commit/f89a5c9a25)\
  2017-04-18 17:15:44 +0200
  * [MDEV-11825](https://jira.mariadb.org/browse/MDEV-11825): Make session variables TRACKING enabled by default
* [Revision #ebe47c3442](https://github.com/MariaDB/server/commit/ebe47c3442)\
  2017-04-16 15:40:04 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
