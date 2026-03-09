# MariaDB 10.3.0 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.0)[Release Notes](../../old-releases/10.3/10.3.0.md)[Changelog](mariadb-1030-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 16 Apr 2017

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.0.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #20ae591abd](https://github.com/MariaDB/server/commit/20ae591abd)\
  2017-04-13 21:39:05 +0200
  * Make feedback plugin ON by default, for pre-release
* [Revision #e2fc1f0ad4](https://github.com/MariaDB/server/commit/e2fc1f0ad4) 2017-04-13 07:12:50 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #45730fb11e](https://github.com/MariaDB/server/commit/45730fb11e)\
  2017-04-13 06:50:00 +0400
  * [MDEV-12238](https://jira.mariadb.org/browse/MDEV-12238) Add Type\_handler::Item\_func\_{plus|minus|mul|div|mod}\_fix\_length\_and\_dec()
* [Revision #949faa2ec2](https://github.com/MariaDB/server/commit/949faa2ec2) 2017-04-13 05:52:44 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #eecce3d7c8](https://github.com/MariaDB/server/commit/eecce3d7c8)\
  2017-04-10 19:11:01 +1000
  * Travis: Test more suites, latest OSX
* [Revision #c7319cf3d5](https://github.com/MariaDB/server/commit/c7319cf3d5)\
  2017-04-03 14:11:27 +0200
  * 10.2 man pages
* [Revision #8c9cd26c06](https://github.com/MariaDB/server/commit/8c9cd26c06)\
  2017-04-07 17:00:35 +0000
  * Rocksdb - disable tests that fail regularly on buildbot ([MDEV-12474](https://jira.mariadb.org/browse/MDEV-12474))
* [Revision #d9484a2f60](https://github.com/MariaDB/server/commit/d9484a2f60)\
  2017-04-04 14:47:58 +0200
  * [MDEV-12395](https://jira.mariadb.org/browse/MDEV-12395): DROP PARTITION does not work as expected when table has DEFAULT LIST partition
* [Revision #27f6b11a97](https://github.com/MariaDB/server/commit/27f6b11a97)\
  2017-04-04 11:00:25 +0200
  * [MDEV-12379](https://jira.mariadb.org/browse/MDEV-12379): Server crashes in TABLE\_LIST::is\_with\_table on SHOW CREATE VIEW
* [Revision #a33653eedb](https://github.com/MariaDB/server/commit/a33653eedb)\
  2017-04-07 15:09:28 +0000
  * [MDEV-12473](https://jira.mariadb.org/browse/MDEV-12473) - fix rocksdb linking error
* [Revision #85da56bf2d](https://github.com/MariaDB/server/commit/85da56bf2d)\
  2017-04-07 13:33:59 +0300
  * Remove the unused variable trx\_t::support\_xa.
* [Revision #84d9d286cf](https://github.com/MariaDB/server/commit/84d9d286cf)\
  2017-04-05 13:17:43 +0200
  * use log-error in mtr, don't let mysqld to write to stderr
* [Revision #cd79be82d1](https://github.com/MariaDB/server/commit/cd79be82d1)\
  2017-04-06 14:47:55 +0200
  * cleanup: unused method LOGGER::flush\_logs
* [Revision #06ee58a7dd](https://github.com/MariaDB/server/commit/06ee58a7dd)\
  2017-04-03 23:58:36 +0200
  * ASAN error in rpl.mysql-wsrep#110-2
* [Revision #30ed99cb82](https://github.com/MariaDB/server/commit/30ed99cb82)\
  2017-04-03 21:08:23 +0200
  * ASAN errors in many rpl tests
* [Revision #82196f0131](https://github.com/MariaDB/server/commit/82196f0131)\
  2017-04-03 17:18:37 +0200
  * [MDEV-11995](https://jira.mariadb.org/browse/MDEV-11995) ALTER TABLE proceeds despite reporting ER\_TOO\_LONG\_KEY error
* [Revision #30cbbfbf77](https://github.com/MariaDB/server/commit/30cbbfbf77)\
  2017-04-07 06:09:25 +0000
  * [MDEV-12452](https://jira.mariadb.org/browse/MDEV-12452) postfix - use C style cast, not reinterpret\_cast
* [Revision #73c57e2be7](https://github.com/MariaDB/server/commit/73c57e2be7)\
  2017-04-06 23:11:57 +0000
  * Fix building aws\_key\_management on Linux
* [Revision #b64910ce27](https://github.com/MariaDB/server/commit/b64910ce27)\
  2017-04-06 18:29:33 -0400
  * [MDEV-12452](https://jira.mariadb.org/browse/MDEV-12452) [MDEV-12453](https://jira.mariadb.org/browse/MDEV-12453) : Fix building rocksdb and aws\_key\_management on macOS
* [Revision #428a922cd0](https://github.com/MariaDB/server/commit/428a922cd0)\
  2017-04-06 12:08:14 -0700
  * Fixed the bug [MDEV-12440](https://jira.mariadb.org/browse/MDEV-12440).
* [Revision #1759e91986](https://github.com/MariaDB/server/commit/1759e91986)\
  2017-04-02 21:46:10 +1000
  * travis: osx - specify allowed\_failures accurately
* [Revision #08359bc570](https://github.com/MariaDB/server/commit/08359bc570)\
  2017-04-02 20:39:01 +1000
  * travis: OSX - 2 minute test case timeout
* [Revision #3bfb0b3bbd](https://github.com/MariaDB/server/commit/3bfb0b3bbd)\
  2017-04-02 20:20:32 +1000
  * Travis: Add OSX to tests (but allow failure)
* [Revision #46e2442f6f](https://github.com/MariaDB/server/commit/46e2442f6f)\
  2017-03-17 16:37:53 +1100
  * [MDEV-6262](https://jira.mariadb.org/browse/MDEV-6262): travis coverity support
* [Revision #fce645745b](https://github.com/MariaDB/server/commit/fce645745b)\
  2017-03-17 14:41:53 +1100
  * Travis: remove tokudb when building with clang
* [Revision #e130ee552a](https://github.com/MariaDB/server/commit/e130ee552a)\
  2017-03-17 13:33:21 +1100
  * Travis: remove Mroonga for clang
* [Revision #837fa86cf0](https://github.com/MariaDB/server/commit/837fa86cf0)\
  2017-03-17 13:09:00 +1100
  * Travis: add ccache for clang
* [Revision #cfd9a75c23](https://github.com/MariaDB/server/commit/cfd9a75c23)\
  2017-04-02 12:30:13 +1000
  * travis: disable main.mysqlhotcopy\_myisam in container builds
* [Revision #eb04ee5c9d](https://github.com/MariaDB/server/commit/eb04ee5c9d)\
  2017-03-17 12:50:21 +1100
  * Travis: llvm, additional packages and container
* [Revision #d235782fca](https://github.com/MariaDB/server/commit/d235782fca) 2017-04-06 09:51:35 +0000 - Merge branch '10.1' into 10.2
* [Revision #b666732182](https://github.com/MariaDB/server/commit/b666732182)\
  2017-04-06 09:50:27 +0000
  * Do not link client plugins to mysqld
* [Revision #1494147cf6](https://github.com/MariaDB/server/commit/1494147cf6) 2017-04-06 09:52:25 +0300 - Merge 10.1 into 10.2
* [Revision #25d69ea012](https://github.com/MariaDB/server/commit/25d69ea012)\
  2017-04-04 10:13:53 +0300
  * [MDEV-12198](https://jira.mariadb.org/browse/MDEV-12198) innodb\_defragment=1 crashes server on OPTIMIZE TABLE when FULLTEXT index exists
* [Revision #8d4871a953](https://github.com/MariaDB/server/commit/8d4871a953) 2017-04-06 08:53:59 +0300 - Merge 10.0 into 10.1
* [Revision #57a699b0a0](https://github.com/MariaDB/server/commit/57a699b0a0)\
  2016-06-17 16:51:11 +0200
  * [MDEV-8642](https://jira.mariadb.org/browse/MDEV-8642): WHERE Clause not applied on View - Empty result set returned
* [Revision #8e36216a06](https://github.com/MariaDB/server/commit/8e36216a06)\
  2017-04-05 14:46:35 +0300
  * Import two ALTER TABLE…ALGORITHM=INPLACE tests from MySQL 5.6.
* [Revision #f2dc04abea](https://github.com/MariaDB/server/commit/f2dc04abea)\
  2017-04-03 18:48:48 +0000
  * Compiling, Windows . Avoid unnecessary rebuilds with MSVC.
* [Revision #ff6f4d7db1](https://github.com/MariaDB/server/commit/ff6f4d7db1)\
  2017-04-03 15:18:46 +0000
  * Windows : Fix compiling with VS2013
* [Revision #cd494f4cef](https://github.com/MariaDB/server/commit/cd494f4cef)\
  2017-04-05 08:54:20 +0300
  * fix warning "ignoring return value" of fwrite.
* [Revision #64a37f6cab](https://github.com/MariaDB/server/commit/64a37f6cab) 2017-04-05 09:43:36 +0300 - Merge pull request #352 from grooverdan/10.1-xtradb-fil\_crypt\_rotate\_page
* [Revision #a7bb9e8fdb](https://github.com/MariaDB/server/commit/a7bb9e8fdb)\
  2017-04-05 16:29:08 +1000
  * xtradb: fil\_crypt\_rotate\_page, space\_id should be compared to TRX\_SYS\_SPACE not space
* [Revision #85239bdfeb](https://github.com/MariaDB/server/commit/85239bdfeb) 2017-04-05 08:40:47 +0300 - Merge pull request #350 from grooverdan/10.1-TRX\_SYS\_PAGE\_NO
* [Revision #9a218f4fb8](https://github.com/MariaDB/server/commit/9a218f4fb8)\
  2017-04-04 15:47:21 +1000
  * fil\_crypt\_rotate\_page - space\_id should be compared to TRX\_SYS\_SPACE not space
* [Revision #d528fd72f2](https://github.com/MariaDB/server/commit/d528fd72f2)\
  2017-04-05 14:43:24 -0400
  * bump the VERSION
* [Revision #8423294acf](https://github.com/MariaDB/server/commit/8423294acf)\
  2017-04-05 16:24:44 +0300
  * Make InnoDB doublewrite buffer creation more robust.
* [Revision #35e582c917](https://github.com/MariaDB/server/commit/35e582c917)\
  2017-04-05 16:00:35 +0300
  * Adjust tests for the removal of kill\_and\_restart\_mysqld.inc.
* [Revision #310ec63fd6](https://github.com/MariaDB/server/commit/310ec63fd6) 2017-04-12 22:09:55 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #012fbc15cf](https://github.com/MariaDB/server/commit/012fbc15cf)\
  2017-04-11 19:32:55 +0400
  * [MDEV-12478](https://jira.mariadb.org/browse/MDEV-12478) CONCAT function inside view casts values incorrectly with Oracle sql\_mode
* [Revision #5bf7046fa7](https://github.com/MariaDB/server/commit/5bf7046fa7)\
  2017-04-11 16:15:08 +0400
  * Adding the const quafilier to "sp\_name \*" parameters in a few routine.
* [Revision #597d1515da](https://github.com/MariaDB/server/commit/597d1515da) 2017-04-09 14:27:35 +0300 - Merge branch 'bb-10.2-ext' into 10.3
* [Revision #958e634d25](https://github.com/MariaDB/server/commit/958e634d25)\
  2017-04-09 14:23:49 +0300
  * Fixed failure in mtr --ps sql\_sequence.create sql\_sequence.read\_only
* [Revision #48319b0383](https://github.com/MariaDB/server/commit/48319b0383) 2017-04-08 07:45:30 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #099e87e090](https://github.com/MariaDB/server/commit/099e87e090)\
  2017-04-08 07:40:09 +0400
  * "mtr --embedded sysvars\_server\_embedded" failed. Recording new correct results.
* [Revision #311503f328](https://github.com/MariaDB/server/commit/311503f328)\
  2017-04-08 07:05:01 +0400
  * storage/rocksdb/rdb\_datadic.cc failed to compile on big endian machines (wrong usage of static\_assert)
* [Revision #3cb28fad7a](https://github.com/MariaDB/server/commit/3cb28fad7a)\
  2017-04-08 06:37:54 +0400
  * "mtr myisam\_views-big" failed with "Unknown VIEW" vs "Unknown table". Recording correct results.
* [Revision #329946cacf](https://github.com/MariaDB/server/commit/329946cacf) 2017-04-07 21:02:56 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #fa5be1d3e0](https://github.com/MariaDB/server/commit/fa5be1d3e0)\
  2017-04-07 21:01:11 +0400
  * Fixed that sql\_sequence.binlog failed sporadically.
* [Revision #3edfe79712](https://github.com/MariaDB/server/commit/3edfe79712) 2017-04-07 20:10:18 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #0177a9c74a](https://github.com/MariaDB/server/commit/0177a9c74a)\
  2017-04-07 10:08:20 +0300
  * Simple binary cache optimizations
* [Revision #1bcfa14e26](https://github.com/MariaDB/server/commit/1bcfa14e26)\
  2017-03-29 23:10:42 +0300
  * Simple cleanups
* [Revision #7c767a30a7](https://github.com/MariaDB/server/commit/7c767a30a7)\
  2017-03-27 18:58:16 +0300
  * [MDEV-10139](https://jira.mariadb.org/browse/MDEV-10139) Support for InnoDB SEQUENCE objects
* [Revision #470c3fd98d](https://github.com/MariaDB/server/commit/470c3fd98d)\
  2017-03-26 22:30:43 +0300
  * Change error message when using DROP VIEW on a non existing view from "Unknown table" to "Unknown view"
* [Revision #17a87d6063](https://github.com/MariaDB/server/commit/17a87d6063)\
  2017-03-25 23:36:56 +0200
  * [MDEV-10139](https://jira.mariadb.org/browse/MDEV-10139) Support for SEQUENCE objects
* [Revision #546e7aa96f](https://github.com/MariaDB/server/commit/546e7aa96f)\
  2017-04-07 10:19:10 +0300
  * [MDEV-8203](https://jira.mariadb.org/browse/MDEV-8203) Assert in Query\_log\_event::do\_apply\_event()
* [Revision #858d8f0c6e](https://github.com/MariaDB/server/commit/858d8f0c6e)\
  2017-04-07 13:51:07 +0300
  * Remove innodb\_support\_xa (deprecated in 5.7.10 and 10.2.)
* [Revision #dedb022047](https://github.com/MariaDB/server/commit/dedb022047) 2017-04-07 14:22:50 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #ed305c0fd5](https://github.com/MariaDB/server/commit/ed305c0fd5)\
  2017-04-07 13:40:27 +0400
  * [MDEV-12461](https://jira.mariadb.org/browse/MDEV-12461) TYPE OF and ROW TYPE OF anchored data types
* [Revision #a8a3ef7bf2](https://github.com/MariaDB/server/commit/a8a3ef7bf2) 2017-04-07 06:40:18 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #113a980ff1](https://github.com/MariaDB/server/commit/113a980ff1)\
  2017-04-06 17:05:42 +0400
  * [MDEV-12457](https://jira.mariadb.org/browse/MDEV-12457) Cursors with parameters
* [Revision #75d1962a24](https://github.com/MariaDB/server/commit/75d1962a24)\
  2017-04-06 20:58:12 +0400
  * Using the -t command line to bison instead of %name-prefix
* [Revision #191f262600](https://github.com/MariaDB/server/commit/191f262600)\
  2017-04-06 16:26:38 +0400
  * Fixing that "mtr --ps compat/oracle.sp-row" failed due to a wrong position of the DELIMITER command
* [Revision #b97a8b123f](https://github.com/MariaDB/server/commit/b97a8b123f)\
  2017-04-06 21:35:43 +0300
  * Fix remnant of RocksDB sed delete
* [Revision #0ecbaae816](https://github.com/MariaDB/server/commit/0ecbaae816)\
  2017-04-06 20:23:32 +0300
  * Fix debian install due to mariadb-client-core circular conflict
* [Revision #32a6621ac9](https://github.com/MariaDB/server/commit/32a6621ac9)\
  2017-04-06 13:49:14 +0300
  * Fix rocksdb plugin && make mariadb-client-10.3 replace mariadb-client-10.2
* [Revision #dadb76521d](https://github.com/MariaDB/server/commit/dadb76521d)\
  2017-04-06 20:58:12 +0400
  * Using the -t command line to bison instead of %name-prefix
* [Revision #06fede98a5](https://github.com/MariaDB/server/commit/06fede98a5)\
  2017-04-06 17:05:42 +0400
  * [MDEV-12457](https://jira.mariadb.org/browse/MDEV-12457) Cursors with parameters
* [Revision #c4963a3422](https://github.com/MariaDB/server/commit/c4963a3422)\
  2017-04-06 16:26:38 +0400
  * Fixing that "mtr --ps compat/oracle.sp-row" failed due to a wrong position of the DELIMITER command
* [Revision #ea751857db](https://github.com/MariaDB/server/commit/ea751857db) 2017-04-06 08:34:28 +0400 - Merge bb-10.2-compatibility into 10.3
* [Revision #e1cff0ac5d](https://github.com/MariaDB/server/commit/e1cff0ac5d)\
  2017-04-05 10:52:31 +0400
  * [MDEV-12441](https://jira.mariadb.org/browse/MDEV-12441) Variables declared after cursors with parameters lose values
* [Revision #d433277f53](https://github.com/MariaDB/server/commit/d433277f53)\
  2017-04-03 16:55:42 +0400
  * A cleanup for [MDEV-10914](https://jira.mariadb.org/browse/MDEV-10914) ROW data type for stored routine variables
* [Revision #cae6bf2b9c](https://github.com/MariaDB/server/commit/cae6bf2b9c)\
  2017-04-03 15:30:31 +0400
  * Cleanup for [MDEV-10581](https://jira.mariadb.org/browse/MDEV-10581) sql\_mode=ORACLE: Explicit cursor FOR LOOP
* [Revision #ce4b291b51](https://github.com/MariaDB/server/commit/ce4b291b51)\
  2017-04-03 14:34:32 +0400
  * A cleanup patch for [MDEV-12011](https://jira.mariadb.org/browse/MDEV-12011) sql\_mode=ORACLE: cursor%ROWTYPE in variable declarations
* [Revision #48a7ea6da3](https://github.com/MariaDB/server/commit/48a7ea6da3)\
  2017-03-31 21:20:32 +0400
  * Uninitialized Column\_definition::pack\_flag for ROW-type SP variables and their fields
* [Revision #281f8a42ee](https://github.com/MariaDB/server/commit/281f8a42ee)\
  2017-03-29 16:09:49 +0400
  * [MDEV-12089](https://jira.mariadb.org/browse/MDEV-12089) sql\_mode=ORACLE: Understand optional routine name after the END keyword
* [Revision #891c1e2dd0](https://github.com/MariaDB/server/commit/891c1e2dd0)\
  2017-03-23 17:48:44 +0400
  * An additional test for [MDEV-12347](https://jira.mariadb.org/browse/MDEV-12347) Valgrind reports invalid read errors in Item\_field\_row::element\_index\_by\_name
* [Revision #01457ec280](https://github.com/MariaDB/server/commit/01457ec280)\
  2017-03-23 17:21:10 +0400
  * [MDEV-12347](https://jira.mariadb.org/browse/MDEV-12347) Valgrind reports invalid read errors in Item\_field\_row::element\_index\_by\_name
* [Revision #ec19e48021](https://github.com/MariaDB/server/commit/ec19e48021)\
  2017-03-22 18:10:33 +0400
  * [MDEV-12314](https://jira.mariadb.org/browse/MDEV-12314) Implicit cursor FOR LOOP for cursors with parameters
* [Revision #e0451941cc](https://github.com/MariaDB/server/commit/e0451941cc)\
  2017-03-18 17:39:17 +0400
  * [MDEV-12291](https://jira.mariadb.org/browse/MDEV-12291) Allow ROW variables as SELECT INTO targets
* [Revision #9dfe7bf86d](https://github.com/MariaDB/server/commit/9dfe7bf86d)\
  2017-03-16 16:28:52 +0400
  * [MDEV-10598](https://jira.mariadb.org/browse/MDEV-10598) Variable declarations can go after cursor declarations
* [Revision #84c55a5668](https://github.com/MariaDB/server/commit/84c55a5668)\
  2017-03-10 14:11:07 +0400
  * [MDEV-10581](https://jira.mariadb.org/browse/MDEV-10581) sql\_mode=ORACLE: Explicit cursor FOR LOOP [MDEV-12098](https://jira.mariadb.org/browse/MDEV-12098) sql\_mode=ORACLE: Implicit cursor FOR loop
* [Revision #f429b5a834](https://github.com/MariaDB/server/commit/f429b5a834)\
  2017-03-08 23:20:39 +0400
  * [MDEV-12011](https://jira.mariadb.org/browse/MDEV-12011) sql\_mode=ORACLE: cursor%ROWTYPE in variable declarations
* [Revision #1b8a0c879d](https://github.com/MariaDB/server/commit/1b8a0c879d)\
  2017-03-03 15:02:08 +0400
  * [MDEV-12133](https://jira.mariadb.org/browse/MDEV-12133) sql\_mode=ORACLE: table%ROWTYPE in variable declarations
* [Revision #400de20279](https://github.com/MariaDB/server/commit/400de20279)\
  2017-03-08 22:32:01 +0400
  * [MDEV-12209](https://jira.mariadb.org/browse/MDEV-12209) sql\_mode=ORACLE: Syntax error in a OPEN cursor with parameters makes the server crash
* [Revision #7ca2f816a8](https://github.com/MariaDB/server/commit/7ca2f816a8)\
  2017-02-22 15:32:41 +0400
  * Part#2 for [MDEV-12107](https://jira.mariadb.org/browse/MDEV-12107) sql\_mode=ORACLE: Inside routines the CALL keywoard is optional
* [Revision #29e7cf01c3](https://github.com/MariaDB/server/commit/29e7cf01c3)\
  2017-02-22 14:13:53 +0400
  * [MDEV-12107](https://jira.mariadb.org/browse/MDEV-12107) sql\_mode=ORACLE: Inside routines the CALL keywoard is optional
* [Revision #839e0947ee](https://github.com/MariaDB/server/commit/839e0947ee)\
  2017-02-27 17:47:06 +0400
  * [MDEV-12143](https://jira.mariadb.org/browse/MDEV-12143) sql\_mode=ORACLE: make the CONCAT function ignore NULL arguments
* [Revision #915c5df865](https://github.com/MariaDB/server/commit/915c5df865)\
  2017-02-20 19:50:39 +0400
  * [MDEV-12088](https://jira.mariadb.org/browse/MDEV-12088) sql\_mode=ORACLE: Do not require BEGIN..END in multi-statement exception handlers in THEN clause
* [Revision #99df09ecab](https://github.com/MariaDB/server/commit/99df09ecab)\
  2017-02-20 19:30:58 +0400
  * [MDEV-12086](https://jira.mariadb.org/browse/MDEV-12086) sql\_mode=ORACLE: allow SELECT UNIQUE as a synonym for SELECT DISTINCT
* [Revision #af7f287b3b](https://github.com/MariaDB/server/commit/af7f287b3b)\
  2017-02-14 14:43:11 +0100
  * [MDEV-10697](https://jira.mariadb.org/browse/MDEV-10697) GOTO statement
* [Revision #d836f52be5](https://github.com/MariaDB/server/commit/d836f52be5)\
  2017-02-07 13:32:55 +0400
  * [MDEV-12007](https://jira.mariadb.org/browse/MDEV-12007) Allow ROW variables as a cursor FETCH target
* [Revision #72f43df623](https://github.com/MariaDB/server/commit/72f43df623)\
  2017-02-02 22:59:07 +0400
  * [MDEV-10914](https://jira.mariadb.org/browse/MDEV-10914) ROW data type for stored routine variables
* [Revision #ffbb2bbc09](https://github.com/MariaDB/server/commit/ffbb2bbc09)\
  2017-02-02 15:05:20 +0400
  * Removing redundant tests for "SET (global|local|session).varname"
* [Revision #81f32145fa](https://github.com/MariaDB/server/commit/81f32145fa)\
  2017-02-01 23:12:16 +0400
  * [MDEV-10655](https://jira.mariadb.org/browse/MDEV-10655) Anonymous blocks
* [Revision #08799831cc](https://github.com/MariaDB/server/commit/08799831cc)\
  2017-02-01 16:35:23 +0400
  * [MDEV-11880](https://jira.mariadb.org/browse/MDEV-11880) sql\_mode=ORACLE: Make the concatenation operator ignore NULL arguments
* [Revision #46255b0c0d](https://github.com/MariaDB/server/commit/46255b0c0d)\
  2016-12-22 10:04:54 +0400
  * Fixing that LEX::sp\_add\_for\_loop\_variable() did not initialize pack\_flag
* [Revision #46d076d67a](https://github.com/MariaDB/server/commit/46d076d67a)\
  2016-12-06 09:05:52 +0400
  * [MDEV-10577](https://jira.mariadb.org/browse/MDEV-10577) sql\_mode=ORACLE: %TYPE in variable declarations
* [Revision #cd1afe0aac](https://github.com/MariaDB/server/commit/cd1afe0aac)\
  2016-11-15 15:57:57 +0400
  * [MDEV-10588](https://jira.mariadb.org/browse/MDEV-10588) sql\_mode=ORACLE: TRUNCATE TABLE t1 \[ {DROP|REUSE} STORAGE ]
* [Revision #c0576ba5ec](https://github.com/MariaDB/server/commit/c0576ba5ec)\
  2016-11-15 15:20:30 +0400
  * [MDEV-11275](https://jira.mariadb.org/browse/MDEV-11275) sql\_mode=ORACLE: CAST(..AS VARCHAR(N))
* [Revision #f8a714c848](https://github.com/MariaDB/server/commit/f8a714c848)\
  2016-10-21 11:51:49 +0400
  * [MDEV-10597](https://jira.mariadb.org/browse/MDEV-10597) Cursors with parameters
* [Revision #4ed804aa4d](https://github.com/MariaDB/server/commit/4ed804aa4d)\
  2016-10-14 16:52:33 +0400
  * [MDEV-10587](https://jira.mariadb.org/browse/MDEV-10587) sql\_mode=ORACLE: User defined exceptions
* [Revision #4d3818d30d](https://github.com/MariaDB/server/commit/4d3818d30d)\
  2016-10-13 18:19:58 +0400
  * [MDEV-11037](https://jira.mariadb.org/browse/MDEV-11037) Diagnostics\_area refactoring for user defined exceptions
* [Revision #6010662cb3](https://github.com/MariaDB/server/commit/6010662cb3)\
  2016-10-12 18:16:38 +0400
  * [MDEV-11037](https://jira.mariadb.org/browse/MDEV-11037) Diagnostics\_area refactoring for user defined exceptions
* [Revision #ffca1e4830](https://github.com/MariaDB/server/commit/ffca1e4830)\
  2016-10-11 12:25:32 +0400
  * [MDEV-10578](https://jira.mariadb.org/browse/MDEV-10578) sql\_mode=ORACLE: SP control functions SQLCODE, SQLERRM
* [Revision #de6d40592c](https://github.com/MariaDB/server/commit/de6d40592c)\
  2016-10-11 11:48:08 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #f7043858ba](https://github.com/MariaDB/server/commit/f7043858ba)\
  2016-10-04 20:22:18 +0400
  * [MDEV-10866](https://jira.mariadb.org/browse/MDEV-10866) Extend PREPARE and EXECUTE IMMEDIATE to understand expressions [MDEV-10867](https://jira.mariadb.org/browse/MDEV-10867) PREPARE..EXECUTE is not consistent about non-ASCII characters
* [Revision #054d00a9a3](https://github.com/MariaDB/server/commit/054d00a9a3)\
  2016-10-03 10:33:22 +0400
  * A fix for [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs (Part 6: Assignment operator)
* [Revision #7fa1ad14dc](https://github.com/MariaDB/server/commit/7fa1ad14dc)\
  2016-09-27 13:22:38 +0400
  * [MDEV-10840](https://jira.mariadb.org/browse/MDEV-10840) sql\_mode=ORACLE: RAISE statement for predefined exceptions
* [Revision #76714a5c9a](https://github.com/MariaDB/server/commit/76714a5c9a)\
  2016-09-27 10:13:08 +0400
  * [MDEV-10582](https://jira.mariadb.org/browse/MDEV-10582) sql\_mode=ORACLE: explicit cursor attributes %ISOPEN, %ROWCOUNT, %FOUND, %NOTFOUND
* [Revision #4bb87996b9](https://github.com/MariaDB/server/commit/4bb87996b9)\
  2016-09-26 18:01:36 +0400
  * DEV-10583 sql\_mode=ORACLE: SQL%ROWCOUNT
* [Revision #a2a196c04c](https://github.com/MariaDB/server/commit/a2a196c04c)\
  2016-09-25 13:51:56 +0400
  * [MDEV-10709](https://jira.mariadb.org/browse/MDEV-10709) Expressions as parameters to Dynamic SQL
* [Revision #417c8c9daf](https://github.com/MariaDB/server/commit/417c8c9daf)\
  2016-09-22 15:18:53 +0400
  * [MDEV-10585](https://jira.mariadb.org/browse/MDEV-10585) EXECUTE IMMEDIATE statement
* [Revision #a699a5f967](https://github.com/MariaDB/server/commit/a699a5f967)\
  2016-09-22 13:31:20 +0400
  * [MDEV-10583](https://jira.mariadb.org/browse/MDEV-10583) sql\_mode=ORACLE: SQL%ROWCOUNT
* [Revision #ccb91eb3ce](https://github.com/MariaDB/server/commit/ccb91eb3ce)\
  2016-09-20 15:30:15 +0400
  * [MDEV-10839](https://jira.mariadb.org/browse/MDEV-10839) sql\_mode=ORACLE: Predefined exceptions: TOO\_MANY\_ROWS, NO\_DATA\_FOUND, DUP\_VAL\_ON\_INDEX
* [Revision #c2c45c55ce](https://github.com/MariaDB/server/commit/c2c45c55ce)\
  2016-09-20 06:23:15 +0400
  * [MDEV-10709](https://jira.mariadb.org/browse/MDEV-10709) Expressions as parameters to Dynamic SQL
* [Revision #c8822d71ef](https://github.com/MariaDB/server/commit/c8822d71ef)\
  2016-09-19 11:39:36 +0400
  * [MDEV-10342](https://jira.mariadb.org/browse/MDEV-10342) Providing compatibility for basic SQL built-in functions
* [Revision #02a72cf87c](https://github.com/MariaDB/server/commit/02a72cf87c)\
  2016-09-19 09:43:00 +0400
  * [MDEV-10596](https://jira.mariadb.org/browse/MDEV-10596) Allow VARCHAR and VARCHAR2 without length as a data type of routine parameters and in RETURN clause
* [Revision #ec527face3](https://github.com/MariaDB/server/commit/ec527face3)\
  2016-09-13 16:34:18 +0400
  * [MDEV-10801](https://jira.mariadb.org/browse/MDEV-10801) sql\_mode: dynamic SQL placeholders
* [Revision #f564ceb473](https://github.com/MariaDB/server/commit/f564ceb473)\
  2016-09-07 12:27:36 +0400
  * Fixed a crash in a EXIT/CONTINUE with an unknown identifier in the WHEN clause
* [Revision #cfb6345982](https://github.com/MariaDB/server/commit/cfb6345982)\
  2016-08-31 09:13:38 +0400
  * Fixed that 'FOR i IN 1..10' with no spaces around '..' returned a syntax error.
* [Revision #bf573e21c7](https://github.com/MariaDB/server/commit/bf573e21c7)\
  2016-08-31 08:03:34 +0400
  * [MDEV-10580](https://jira.mariadb.org/browse/MDEV-10580) sql\_mode=ORACLE: FOR loop statement
* [Revision #30bec863cf](https://github.com/MariaDB/server/commit/30bec863cf)\
  2016-09-17 08:24:05 +0400
  * [MDEV-10342](https://jira.mariadb.org/browse/MDEV-10342) Providing compatibility for basic SQL built-in functions
* [Revision #7e7ba7cb94](https://github.com/MariaDB/server/commit/7e7ba7cb94)\
  2016-08-25 15:07:42 +0400
  * Removing SHOW FUNCTION CODE from compat/oracle.sp, as this type of SHOW is only available in debug builds. A bug in b7af3e704dd7800638ef677e9d921ad3e467a9a6. All SHOW FUNCTION CODE queries should be in compat/oracle.sp-code.
* [Revision #5721ea6ab7](https://github.com/MariaDB/server/commit/5721ea6ab7)\
  2016-08-25 13:38:24 +0400
  * [MDEV-10579](https://jira.mariadb.org/browse/MDEV-10579) sql\_mode=ORACLE: Triggers: Understand :NEW.c1 and :OLD.c1 instead of NEW.c1 and OLD.c1
* [Revision #ca242117ce](https://github.com/MariaDB/server/commit/ca242117ce)\
  2016-08-24 15:23:04 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #442ea81ed3](https://github.com/MariaDB/server/commit/442ea81ed3)\
  2016-08-24 12:30:27 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #2ea63492f7](https://github.com/MariaDB/server/commit/2ea63492f7)\
  2016-08-24 08:32:05 +0400
  * [MDEV-10580](https://jira.mariadb.org/browse/MDEV-10580) sql\_mode=ORACLE: FOR loop statement
* [Revision #c570636ba2](https://github.com/MariaDB/server/commit/c570636ba2)\
  2016-08-24 07:39:04 +0400
  * [MDEV-10580](https://jira.mariadb.org/browse/MDEV-10580) sql\_mode=ORACLE: FOR loop statement
* [Revision #71a0a12e61](https://github.com/MariaDB/server/commit/71a0a12e61)\
  2016-08-23 11:57:47 +0400
  * Changing a LEX::sp\_variable\_declarations\_finalize() parameter from "const Lex\_field\_type\_st &" to "const Column\_definition &".
* [Revision #8ec4cf1f01](https://github.com/MariaDB/server/commit/8ec4cf1f01)\
  2016-08-22 13:24:15 +0400
  * Refactoring for [MDEV-10580](https://jira.mariadb.org/browse/MDEV-10580) sql\_mode=ORACLE: FOR loop statement
* [Revision #28f2859136](https://github.com/MariaDB/server/commit/28f2859136)\
  2016-08-22 07:05:18 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #4212039db7](https://github.com/MariaDB/server/commit/4212039db7)\
  2016-08-22 06:17:26 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #ed19ed6a4b](https://github.com/MariaDB/server/commit/ed19ed6a4b)\
  2016-08-19 13:01:35 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #6cd24d124f](https://github.com/MariaDB/server/commit/6cd24d124f)\
  2016-09-17 08:14:07 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #a83d0aee96](https://github.com/MariaDB/server/commit/a83d0aee96)\
  2016-08-17 12:08:20 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #8feb984211](https://github.com/MariaDB/server/commit/8feb984211)\
  2016-08-17 10:33:31 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #765d9d6429](https://github.com/MariaDB/server/commit/765d9d6429)\
  2016-08-16 19:20:52 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #f37a943f49](https://github.com/MariaDB/server/commit/f37a943f49)\
  2016-08-16 15:24:24 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #4b61495576](https://github.com/MariaDB/server/commit/4b61495576)\
  2016-08-16 10:24:12 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #d2b007d6bc](https://github.com/MariaDB/server/commit/d2b007d6bc)\
  2016-08-15 21:46:22 +0400
  * Optimization for [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #4940a91a5f](https://github.com/MariaDB/server/commit/4940a91a5f)\
  2016-08-15 17:04:55 +0400
  * A test clean-up for 7c78b27a33b749656cbc28091eac32bbbeee9e42
* [Revision #81ba971d03](https://github.com/MariaDB/server/commit/81ba971d03)\
  2016-08-15 16:25:27 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #0040b0f380](https://github.com/MariaDB/server/commit/0040b0f380)\
  2016-08-12 15:32:10 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #bd76d44564](https://github.com/MariaDB/server/commit/bd76d44564)\
  2016-08-12 14:41:13 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #f3a0df72f2](https://github.com/MariaDB/server/commit/f3a0df72f2)\
  2016-08-12 12:55:37 +0400
  * Reusing code: Adding LEX::make\_sp\_head() and LEX::make\_sp\_head\_no\_recursive()
* [Revision #dc292bc6eb](https://github.com/MariaDB/server/commit/dc292bc6eb)\
  2016-08-12 10:45:13 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #0c9c4b84b7](https://github.com/MariaDB/server/commit/0c9c4b84b7)\
  2016-08-11 15:47:17 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #8fdc1f0147](https://github.com/MariaDB/server/commit/8fdc1f0147)\
  2016-08-11 14:12:14 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #a44e90ae05](https://github.com/MariaDB/server/commit/a44e90ae05)\
  2016-08-10 15:39:07 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #e399949bfe](https://github.com/MariaDB/server/commit/e399949bfe)\
  2016-08-09 15:53:15 +0400
  * Adding Lex\_spblock\_st::init() and Lex\_spblock\_st::join().
* [Revision #365e0b3178](https://github.com/MariaDB/server/commit/365e0b3178)\
  2016-08-09 14:58:20 +0400
  * sql\_lex.yy / sql\_yacc\_ora.yy refactoring for [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411).
* [Revision #36b80caed1](https://github.com/MariaDB/server/commit/36b80caed1)\
  2016-08-09 12:08:11 +0400
  * Moving the code from \*.yy to new methods to LEX and sp\_context
* [Revision #0281757e82](https://github.com/MariaDB/server/commit/0281757e82)\
  2016-08-09 10:36:26 +0400
  * Fixing sp.result, forgotten in 78d68badd7f399f08bc1000f56b2a12bb8515718.
* [Revision #f71a1f736d](https://github.com/MariaDB/server/commit/f71a1f736d)\
  2016-08-08 18:06:49 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #892af78085](https://github.com/MariaDB/server/commit/892af78085)\
  2016-08-08 16:42:01 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs
* [Revision #7e10e38825](https://github.com/MariaDB/server/commit/7e10e38825)\
  2016-08-05 13:53:38 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs Part2: Different order of IN, OUT, INOUT keywords in CREATE PROCEDURE params
* [Revision #47a75ed7cb](https://github.com/MariaDB/server/commit/47a75ed7cb)\
  2016-08-05 09:58:36 +0400
  * [MDEV-10411](https://jira.mariadb.org/browse/MDEV-10411) Providing compatibility for basic PL/SQL constructs Changing label syntax from "label:" to "`<<label>>`".
* [Revision #4de26a8e0e](https://github.com/MariaDB/server/commit/4de26a8e0e)\
  2016-09-17 08:09:10 +0400
  * [MDEV-10343](https://jira.mariadb.org/browse/MDEV-10343) Providing compatibility for basic SQL data types Based on the patch by Dmitry Tolpeko.
* [Revision #decc550fa9](https://github.com/MariaDB/server/commit/decc550fa9)\
  2016-07-08 21:42:33 +0400
  * Making sp\_create\_assignment\_lex() and sp\_create\_assignment\_lex() non-static
* [Revision #c21fc0085b](https://github.com/MariaDB/server/commit/c21fc0085b)\
  2016-09-17 08:00:59 +0400
  * Moving the code from my\_parse\_error() to THD::parse\_error().
* [Revision #9f6aca198c](https://github.com/MariaDB/server/commit/9f6aca198c)\
  2016-09-17 07:56:56 +0400
  * Adding an alternative grammar file sql\_yacc\_ora.yy for sql\_mode=ORACLE
* [Revision #9764efe52c](https://github.com/MariaDB/server/commit/9764efe52c)\
  2017-04-05 22:13:37 +0000
  * Windows packaging cleanup- get rid of "Monty Program AB" in installation registry keys.
* [Revision #75b8fe4f18](https://github.com/MariaDB/server/commit/75b8fe4f18)\
  2017-04-05 15:58:24 +0300
  * Update debian packaging to work in 10.3
* [Revision #3d004de31d](https://github.com/MariaDB/server/commit/3d004de31d) 2017-04-05 14:47:06 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #e34acc838b](https://github.com/MariaDB/server/commit/e34acc838b) 2017-04-05 14:42:14 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #0d34dd7cfb](https://github.com/MariaDB/server/commit/0d34dd7cfb)\
  2017-04-04 12:19:42 +0300
  * [MDEV-11840](https://jira.mariadb.org/browse/MDEV-11840) InnoDB: "Cannot open \<ib\_buffer\_pool file>" should not be an error
* [Revision #d5c77fba20](https://github.com/MariaDB/server/commit/d5c77fba20) 2017-04-04 18:02:23 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #17309c4c12](https://github.com/MariaDB/server/commit/17309c4c12)\
  2017-04-04 17:59:48 +0400
  * [MDEV-12303](https://jira.mariadb.org/browse/MDEV-12303) Add Type\_handler::Item\_xxx\_fix\_length\_and\_dec() for CAST classes
* [Revision #b7fb644622](https://github.com/MariaDB/server/commit/b7fb644622) 2017-04-04 16:54:51 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #f1b0b04651](https://github.com/MariaDB/server/commit/f1b0b04651)\
  2017-04-04 16:54:02 +0400
  * [MDEV-12411](https://jira.mariadb.org/browse/MDEV-12411) Remove Lex::text\_string\_is\_7bit
* [Revision #15d98ddc2a](https://github.com/MariaDB/server/commit/15d98ddc2a) 2017-04-03 17:35:55 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #015868e7da](https://github.com/MariaDB/server/commit/015868e7da) 2017-04-03 17:22:10 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #f00a314f9a](https://github.com/MariaDB/server/commit/f00a314f9a) 2017-03-31 16:40:29 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #e191833d75](https://github.com/MariaDB/server/commit/e191833d75)\
  2017-03-31 14:26:43 +0400
  * [MDEV-12415](https://jira.mariadb.org/browse/MDEV-12415) Remove sp\_name::m\_qname
* [Revision #94d643ac22](https://github.com/MariaDB/server/commit/94d643ac22) 2017-03-29 21:02:18 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #0d8dc74d30](https://github.com/MariaDB/server/commit/0d8dc74d30) 2017-03-29 20:51:54 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #1694c0e8d8](https://github.com/MariaDB/server/commit/1694c0e8d8)\
  2017-03-29 18:15:28 +0400
  * [MDEV-12394](https://jira.mariadb.org/browse/MDEV-12394) Add function is\_native\_function\_with\_warn()
* [Revision #8af5dcb0d8](https://github.com/MariaDB/server/commit/8af5dcb0d8)\
  2017-03-29 17:33:27 +0400
  * [MDEV-12393](https://jira.mariadb.org/browse/MDEV-12393) Add function mysql\_create\_routine
* [Revision #2361f835ae](https://github.com/MariaDB/server/commit/2361f835ae)\
  2017-03-29 17:22:49 +0400
  * [MDEV-12392](https://jira.mariadb.org/browse/MDEV-12392) Duplicate code cleanup: add function normalize\_db\_name()
* [Revision #fb43180c4f](https://github.com/MariaDB/server/commit/fb43180c4f) 2017-03-29 07:24:05 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #ab96710bb7](https://github.com/MariaDB/server/commit/ab96710bb7) 2017-03-24 18:48:40 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #48c59f394b](https://github.com/MariaDB/server/commit/48c59f394b)\
  2017-03-24 17:52:55 +0400
  * [MDEV-12338](https://jira.mariadb.org/browse/MDEV-12338) Split Item\_type\_holder::get\_real\_type() into virtual Item::real\_type\_handler()
* [Revision #1b3bd00c6b](https://github.com/MariaDB/server/commit/1b3bd00c6b) 2017-03-24 16:14:30 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #a1e5201488](https://github.com/MariaDB/server/commit/a1e5201488)\
  2017-03-24 15:59:58 +0400
  * [MDEV-12357](https://jira.mariadb.org/browse/MDEV-12357) Invalid read of size 8 in Type\_aggregator::Type\_aggregator()
* [Revision #552072e4d1](https://github.com/MariaDB/server/commit/552072e4d1)\
  2017-03-19 23:39:42 +0400
  * [MDEV-12239](https://jira.mariadb.org/browse/MDEV-12239) Add Type\_handler::Item\_sum\_{sum|avg|variance}\_fix\_length\_and\_dec()
* [Revision #7d0c354f5c](https://github.com/MariaDB/server/commit/7d0c354f5c) 2017-03-18 14:20:06 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #af22a70df9](https://github.com/MariaDB/server/commit/af22a70df9)\
  2017-02-21 16:28:42 +0400
  * [MDEV-11418](https://jira.mariadb.org/browse/MDEV-11418) - AliSQL: \[Feature] Issue#1 KILL IDLE TRANSACTIONS
* [Revision #8026cd6202](https://github.com/MariaDB/server/commit/8026cd6202)\
  2017-02-07 13:27:42 +0400
  * [MDEV-11379](https://jira.mariadb.org/browse/MDEV-11379), [MDEV-11388](https://jira.mariadb.org/browse/MDEV-11388) - \[WAIT n|NOWAIT]
* [Revision #4c6ae99285](https://github.com/MariaDB/server/commit/4c6ae99285) 2017-03-16 11:21:06 +0100 - Merge branch 'bb-10.2-ext' into 10.3-merge-10.2-ext
* [Revision #b13ce223a8](https://github.com/MariaDB/server/commit/b13ce223a8)\
  2017-03-16 10:21:52 +0100
  * fix time replacement due to possible exponent in the output
* [Revision #05d3c3d3f7](https://github.com/MariaDB/server/commit/05d3c3d3f7)\
  2017-03-14 11:52:00 +0100
  * [MDEV-10141](https://jira.mariadb.org/browse/MDEV-10141): Add support for INTERSECT (and common parts for EXCEPT) [MDEV-10140](https://jira.mariadb.org/browse/MDEV-10140): Add support for EXCEPT
* [Revision #e43156e1a6](https://github.com/MariaDB/server/commit/e43156e1a6)\
  2017-03-13 17:20:22 +0400
  * Removing the duplicate copy of char\_to\_byte\_length\_safe().
* [Revision #a4a48a37c4](https://github.com/MariaDB/server/commit/a4a48a37c4)\
  2017-03-10 16:12:58 +0400
  * [MDEV-12199](https://jira.mariadb.org/browse/MDEV-12199) Split Item\_func\_{abs|neg|int\_val}::fix\_length\_and\_dec() into methods in Type\_handler
* [Revision #6a9e2e1979](https://github.com/MariaDB/server/commit/6a9e2e1979)\
  2017-03-15 14:30:27 +0100
  * fix 32bit redefine of char\_to\_byte\_length\_safe (#337)
* [Revision #7aa09a5ed2](https://github.com/MariaDB/server/commit/7aa09a5ed2)\
  2017-01-22 12:31:32 +0100
  * [MDEV-10141](https://jira.mariadb.org/browse/MDEV-10141): Add support for INTERSECT (and common parts for EXCEPT) [MDEV-10140](https://jira.mariadb.org/browse/MDEV-10140): Add support for EXCEPT
* [Revision #a4652c3b1a](https://github.com/MariaDB/server/commit/a4652c3b1a)\
  2017-01-29 18:52:32 +0100
  * Comment added.
* [Revision #f7740b6604](https://github.com/MariaDB/server/commit/f7740b6604)\
  2017-03-10 23:16:01 +0200
  * [MDEV-12096](https://jira.mariadb.org/browse/MDEV-12096): Fix ln syntax in debian/rules for libmariadb3 symlink creation
* [Revision #fa2a3480c4](https://github.com/MariaDB/server/commit/fa2a3480c4) 2017-03-09 00:02:13 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #ec8c38a82e](https://github.com/MariaDB/server/commit/ec8c38a82e) 2017-03-08 23:47:20 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #7b9029b17f](https://github.com/MariaDB/server/commit/7b9029b17f)\
  2017-03-01 11:41:13 +0200
  * Remove innodb\_use\_trim, innodb\_instrument\_semaphores.
* [Revision #7a9dc5ab3a](https://github.com/MariaDB/server/commit/7a9dc5ab3a) 2017-03-01 10:55:59 +0200 - Merge 10.2 into 10.3
* [Revision #b5d7fff687](https://github.com/MariaDB/server/commit/b5d7fff687) 2017-02-27 12:41:37 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #47b7ffb396](https://github.com/MariaDB/server/commit/47b7ffb396) 2017-02-27 10:07:59 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #8c3ae615ac](https://github.com/MariaDB/server/commit/8c3ae615ac) 2017-02-10 16:17:35 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #3f83801d82](https://github.com/MariaDB/server/commit/3f83801d82)\
  2017-02-07 21:07:28 +0400
  * [MDEV-12001](https://jira.mariadb.org/browse/MDEV-12001) Split Item\_func\_round::fix\_length\_and\_dec to virtual methods in Type\_handler
* [Revision #11e9b25e8e](https://github.com/MariaDB/server/commit/11e9b25e8e) 2017-02-06 10:19:19 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #d333e3ad9c](https://github.com/MariaDB/server/commit/d333e3ad9c) 2017-02-02 08:21:42 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #02a4bbb412](https://github.com/MariaDB/server/commit/02a4bbb412)\
  2017-02-01 15:36:22 +0400
  * [MDEV-11913](https://jira.mariadb.org/browse/MDEV-11913) Split sp\_get\_item\_value() into methods in Type\_handler
* [Revision #68235f2c2b](https://github.com/MariaDB/server/commit/68235f2c2b)\
  2017-02-01 08:00:50 +0400
  * [MDEV-11692](https://jira.mariadb.org/browse/MDEV-11692) Comparison data type aggregation for pluggable data types
* [Revision #095ea087b4](https://github.com/MariaDB/server/commit/095ea087b4) 2017-01-17 18:25:18 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #c846ebe9df](https://github.com/MariaDB/server/commit/c846ebe9df) 2017-01-13 17:26:32 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #59c58f6ec3](https://github.com/MariaDB/server/commit/59c58f6ec3)\
  2017-01-13 17:25:16 +0400
  * [MDEV-9522](https://jira.mariadb.org/browse/MDEV-9522) Split sql\_select.cc:can\_change\_cond\_ref\_to\_const into virtual methods in Type\_handler
* [Revision #306ce497a7](https://github.com/MariaDB/server/commit/306ce497a7)\
  2017-01-03 14:26:04 +0100
  * Fixed typo in comments
* [Revision #060d4861b9](https://github.com/MariaDB/server/commit/060d4861b9)\
  2016-12-30 21:13:34 +0400
  * Fixing minor problems in the patch for [MDEV-11478](https://jira.mariadb.org/browse/MDEV-11478) (shortint vs smallint)
* [Revision #8a5de517bc](https://github.com/MariaDB/server/commit/8a5de517bc)\
  2016-12-30 16:20:10 +0200
  * [MDEV-11687](https://jira.mariadb.org/browse/MDEV-11687) innodb\_use\_fallocate has no effect
* [Revision #f5148fa6e1](https://github.com/MariaDB/server/commit/f5148fa6e1) 2016-12-30 16:15:28 +0200 - Merge 10.2 into 10.3
* [Revision #86209c7304](https://github.com/MariaDB/server/commit/86209c7304) 2016-12-30 15:43:08 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #9b2bcf19f4](https://github.com/MariaDB/server/commit/9b2bcf19f4)\
  2016-12-30 15:39:33 +0400
  * [MDEV-11528](https://jira.mariadb.org/browse/MDEV-11528) Split Item\_func\_min\_max::val\_xxx() and Item\_func\_min\_max::get\_date() into methods in Type\_handler
* [Revision #b4ef7b25e4](https://github.com/MariaDB/server/commit/b4ef7b25e4) 2016-12-30 14:49:21 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #b6aa3d2add](https://github.com/MariaDB/server/commit/b6aa3d2add) 2016-12-30 13:55:47 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #c0fc4391f0](https://github.com/MariaDB/server/commit/c0fc4391f0) 2016-12-30 10:29:20 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #09615ca757](https://github.com/MariaDB/server/commit/09615ca757)\
  2016-12-29 14:13:58 +0400
  * An after-fix for [MDEV-11478](https://jira.mariadb.org/browse/MDEV-11478): fixing the error code
* [Revision #b3706c82aa](https://github.com/MariaDB/server/commit/b3706c82aa)\
  2016-12-29 12:38:45 +0400
  * An improvement for the [MDEV-11514](https://jira.mariadb.org/browse/MDEV-11514) patch: adding data type name into debug output
* [Revision #8aa044e674](https://github.com/MariaDB/server/commit/8aa044e674)\
  2016-12-29 11:53:14 +0400
  * [MDEV-11478](https://jira.mariadb.org/browse/MDEV-11478) Result data type aggregation for pluggable data types
* [Revision #f6138883b1](https://github.com/MariaDB/server/commit/f6138883b1)\
  2016-12-29 07:40:49 +0400
  * [MDEV-11672](https://jira.mariadb.org/browse/MDEV-11672) mysql\_list\_field() returns wrong default values for VIEW
* [Revision #7435dc4b3e](https://github.com/MariaDB/server/commit/7435dc4b3e) 2016-12-27 10:03:02 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #d8c695ead4](https://github.com/MariaDB/server/commit/d8c695ead4)\
  2016-12-27 09:32:54 +0400
  * [MDEV-11615](https://jira.mariadb.org/browse/MDEV-11615) Split Item\_hybrid\_func::fix\_attributes into virtual methods in Type\_handler
* [Revision #4e23bfa11c](https://github.com/MariaDB/server/commit/4e23bfa11c) 2016-12-27 07:07:36 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #99c2493cec](https://github.com/MariaDB/server/commit/99c2493cec)\
  2016-12-21 16:10:39 +0400
  * Changing version in bb-10.2-ext from 10.3 to 10.2.x
* [Revision #74891ed257](https://github.com/MariaDB/server/commit/74891ed257)\
  2016-12-17 23:35:12 +0400
  * [MDEV-11514](https://jira.mariadb.org/browse/MDEV-11514), [MDEV-11497](https://jira.mariadb.org/browse/MDEV-11497), [MDEV-11554](https://jira.mariadb.org/browse/MDEV-11554), [MDEV-11555](https://jira.mariadb.org/browse/MDEV-11555) - IN and CASE type aggregation problems
* [Revision #191c3f4973](https://github.com/MariaDB/server/commit/191c3f4973)\
  2016-12-17 22:53:48 +0400
  * Adding "DBUG" prefix into the debug messages in Item\_func\_in::fix\_length\_and\_dec()
* [Revision #c4de14fb44](https://github.com/MariaDB/server/commit/c4de14fb44) 2016-12-27 08:19:14 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* [Revision #ab774974d6](https://github.com/MariaDB/server/commit/ab774974d6) 2016-12-17 22:06:55 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* [Revision #7d0a8832d8](https://github.com/MariaDB/server/commit/7d0a8832d8)\
  2016-12-17 21:10:59 +0400
  * [MDEV-11558](https://jira.mariadb.org/browse/MDEV-11558) Split Item\_type\_holder::display\_length into virtual methods in Type\_handler
* [Revision #93bc72836e](https://github.com/MariaDB/server/commit/93bc72836e)\
  2016-12-10 22:25:17 +0400
  * [MDEV-11503](https://jira.mariadb.org/browse/MDEV-11503) Introduce Type\_handler::make\_in\_vector() and Item\_func\_in\_fix\_comparator\_compatible\_types()
* [Revision #8b930b8f68](https://github.com/MariaDB/server/commit/8b930b8f68)\
  2016-12-07 10:00:46 +0400
  * Addressing Sanja's comments about for the [MDEV-11485](https://jira.mariadb.org/browse/MDEV-11485) patch
* [Revision #cfda0a71a7](https://github.com/MariaDB/server/commit/cfda0a71a7)\
  2016-12-06 23:20:39 +0400
  * [MDEV-11485](https://jira.mariadb.org/browse/MDEV-11485) Split Item\_func\_between::val\_int() into virtual methods in Type\_handler
* [Revision #1c1d8fe9e4](https://github.com/MariaDB/server/commit/1c1d8fe9e4)\
  2016-12-05 18:40:04 +0400
  * Moving LEX::set\_last\_field\_type() to Column\_definition::set\_attributes()
* [Revision #6be678608f](https://github.com/MariaDB/server/commit/6be678608f)\
  2016-12-05 16:23:18 +0400
  * [MDEV-11330](https://jira.mariadb.org/browse/MDEV-11330) Split Item\_func\_hybrid\_field\_type::val\_xxx() into methods in Type\_handler
* [Revision #69f80e5ecf](https://github.com/MariaDB/server/commit/69f80e5ecf)\
  2016-12-01 11:57:01 +0400
  * [MDEV-11298](https://jira.mariadb.org/browse/MDEV-11298) Split Item\_func\_hex::val\_str\_ascii() into virtual methods in Type\_handler
* [Revision #9185f8d4a7](https://github.com/MariaDB/server/commit/9185f8d4a7)\
  2016-11-28 10:21:01 +0400
  * [MDEV-11365](https://jira.mariadb.org/browse/MDEV-11365) Split the data type and attribute related code in Item\_sum\_hybrid::fix\_fields into Type\_handler::Item\_sum\_hybrid\_fix\_length\_and\_dec()
* [Revision #749bbb3d7b](https://github.com/MariaDB/server/commit/749bbb3d7b)\
  2016-11-26 21:19:48 +0400
  * [MDEV-11357](https://jira.mariadb.org/browse/MDEV-11357) Split Item\_cache::get\_cache() into virtual methods in Type\_handler
* [Revision #352ff9cc96](https://github.com/MariaDB/server/commit/352ff9cc96)\
  2016-11-25 22:37:58 +0400
  * [MDEV-11347](https://jira.mariadb.org/browse/MDEV-11347) Move add\_create\_index\_prepare(), add\_key\_to\_list(), set\_trigger\_new\_row(), set\_local\_variable(), set\_system\_variable(), create\_item\_for\_sp\_var() as methods to LEX
* [Revision #2637828065](https://github.com/MariaDB/server/commit/2637828065)\
  2016-11-24 16:26:30 +0400
  * [MDEV-11344](https://jira.mariadb.org/browse/MDEV-11344) Split Arg\_comparator::set\_compare\_func() into virtual methods in Type\_handler
* [Revision #cb16d753b2](https://github.com/MariaDB/server/commit/cb16d753b2)\
  2016-11-25 07:40:10 +0400
  * [MDEV-11337](https://jira.mariadb.org/browse/MDEV-11337) Split Item::save\_in\_field() into virtual methods in Type\_handler
* [Revision #4b4efb0485](https://github.com/MariaDB/server/commit/4b4efb0485)\
  2016-11-24 21:57:14 +0400
  * [MDEV-11346](https://jira.mariadb.org/browse/MDEV-11346) Move functions case\_stmt\_xxx and add\_select\_to\_union\_list as methods to LEX
* [Revision #cba0092196](https://github.com/MariaDB/server/commit/cba0092196)\
  2016-11-21 17:23:10 +0400
  * [MDEV-11294](https://jira.mariadb.org/browse/MDEV-11294) Move definitions of Derivation, DTCollation, Type\_std\_attributes from field.h and item.h to sql\_type.h
* [Revision #01546ee403](https://github.com/MariaDB/server/commit/01546ee403)\
  2016-11-18 15:40:45 +0400
  * [MDEV-11245](https://jira.mariadb.org/browse/MDEV-11245) Move prepare\_create\_field and sp\_prepare\_create\_field() as methods to Column\_definition
* [Revision #8b4f181c60](https://github.com/MariaDB/server/commit/8b4f181c60)\
  2016-11-16 10:08:17 +0400
  * [MDEV-10811](https://jira.mariadb.org/browse/MDEV-10811) Change design from "Item is Type\_handler" to "Item has Type\_handler"
* [Revision #e5dfe04da0](https://github.com/MariaDB/server/commit/e5dfe04da0)\
  2016-11-02 18:04:35 +0400
  * [MDEV-11146](https://jira.mariadb.org/browse/MDEV-11146) SP variables of the SET data type erroneously allow values with comma
* [Revision #239287b22e](https://github.com/MariaDB/server/commit/239287b22e)\
  2016-11-02 09:20:47 +0400
  * Starting the 10.3 branch
* [Revision #77a5dab5a2](https://github.com/MariaDB/server/commit/77a5dab5a2)\
  2016-11-17 14:50:09 +0400
  * [MDEV-11212](https://jira.mariadb.org/browse/MDEV-11212) - Clean-up MariaDB atomic operations
* [Revision #c10e523d78](https://github.com/MariaDB/server/commit/c10e523d78)\
  2016-11-03 13:21:18 +0400
  * [MDEV-11212](https://jira.mariadb.org/browse/MDEV-11212) - Clean-up MariaDB atomic operations
* [Revision #81f280789b](https://github.com/MariaDB/server/commit/81f280789b)\
  2016-11-02 16:43:23 +0400
  * [MDEV-11212](https://jira.mariadb.org/browse/MDEV-11212) - Clean-up MariaDB atomic operations
* [Revision #c23399d3de](https://github.com/MariaDB/server/commit/c23399d3de)\
  2016-11-02 16:40:43 +0400
  * [MDEV-11212](https://jira.mariadb.org/browse/MDEV-11212) - Clean-up MariaDB atomic operations
* [Revision #8ff3b892ae](https://github.com/MariaDB/server/commit/8ff3b892ae)\
  2016-11-02 15:40:30 +0400
  * [MDEV-11212](https://jira.mariadb.org/browse/MDEV-11212) - Clean-up MariaDB atomic operations
* [Revision #bb9928160f](https://github.com/MariaDB/server/commit/bb9928160f)\
  2016-11-02 15:30:01 +0400
  * [MDEV-11212](https://jira.mariadb.org/browse/MDEV-11212) - Clean-up MariaDB atomic operations
* [Revision #8f9999b5fc](https://github.com/MariaDB/server/commit/8f9999b5fc)\
  2016-11-02 15:27:12 +0400
  * [MDEV-11212](https://jira.mariadb.org/browse/MDEV-11212) - Clean-up MariaDB atomic operations
* [Revision #1369e70b56](https://github.com/MariaDB/server/commit/1369e70b56)\
  2016-11-02 15:16:36 +0400
  * [MDEV-11212](https://jira.mariadb.org/browse/MDEV-11212) - Clean-up MariaDB atomic operations
* [Revision #beea3413e0](https://github.com/MariaDB/server/commit/beea3413e0)\
  2016-12-10 22:25:17 +0400
  * [MDEV-11503](https://jira.mariadb.org/browse/MDEV-11503) Introduce Type\_handler::make\_in\_vector() and Item\_func\_in\_fix\_comparator\_compatible\_types()
* [Revision #e315bb7d19](https://github.com/MariaDB/server/commit/e315bb7d19)\
  2016-12-07 10:00:46 +0400
  * Addressing Sanja's comments about for the [MDEV-11485](https://jira.mariadb.org/browse/MDEV-11485) patch
* [Revision #fd4e986b07](https://github.com/MariaDB/server/commit/fd4e986b07)\
  2016-12-06 23:20:39 +0400
  * [MDEV-11485](https://jira.mariadb.org/browse/MDEV-11485) Split Item\_func\_between::val\_int() into virtual methods in Type\_handler
* [Revision #466728c452](https://github.com/MariaDB/server/commit/466728c452)\
  2016-12-05 18:40:04 +0400
  * Moving LEX::set\_last\_field\_type() to Column\_definition::set\_attributes()
* [Revision #378c3cf99d](https://github.com/MariaDB/server/commit/378c3cf99d)\
  2016-12-05 16:23:18 +0400
  * [MDEV-11330](https://jira.mariadb.org/browse/MDEV-11330) Split Item\_func\_hybrid\_field\_type::val\_xxx() into methods in Type\_handler
* [Revision #98eaff34af](https://github.com/MariaDB/server/commit/98eaff34af)\
  2016-12-01 11:57:01 +0400
  * [MDEV-11298](https://jira.mariadb.org/browse/MDEV-11298) Split Item\_func\_hex::val\_str\_ascii() into virtual methods in Type\_handler
* [Revision #587d387a03](https://github.com/MariaDB/server/commit/587d387a03)\
  2016-11-28 10:21:01 +0400
  * [MDEV-11365](https://jira.mariadb.org/browse/MDEV-11365) Split the data type and attribute related code in Item\_sum\_hybrid::fix\_fields into Type\_handler::Item\_sum\_hybrid\_fix\_length\_and\_dec()
* [Revision #81f448ce4d](https://github.com/MariaDB/server/commit/81f448ce4d)\
  2016-11-26 21:19:48 +0400
  * [MDEV-11357](https://jira.mariadb.org/browse/MDEV-11357) Split Item\_cache::get\_cache() into virtual methods in Type\_handler
* [Revision #7ae95bd0e5](https://github.com/MariaDB/server/commit/7ae95bd0e5)\
  2016-11-25 22:37:58 +0400
  * [MDEV-11347](https://jira.mariadb.org/browse/MDEV-11347) Move add\_create\_index\_prepare(), add\_key\_to\_list(), set\_trigger\_new\_row(), set\_local\_variable(), set\_system\_variable(), create\_item\_for\_sp\_var() as methods to LEX
* [Revision #ebd8710b78](https://github.com/MariaDB/server/commit/ebd8710b78)\
  2016-11-24 16:26:30 +0400
  * [MDEV-11344](https://jira.mariadb.org/browse/MDEV-11344) Split Arg\_comparator::set\_compare\_func() into virtual methods in Type\_handler
* [Revision #25f52725da](https://github.com/MariaDB/server/commit/25f52725da)\
  2016-11-25 07:40:10 +0400
  * [MDEV-11337](https://jira.mariadb.org/browse/MDEV-11337) Split Item::save\_in\_field() into virtual methods in Type\_handler
* [Revision #8a1c0d46eb](https://github.com/MariaDB/server/commit/8a1c0d46eb)\
  2016-11-24 21:57:14 +0400
  * [MDEV-11346](https://jira.mariadb.org/browse/MDEV-11346) Move functions case\_stmt\_xxx and add\_select\_to\_union\_list as methods to LEX
* [Revision #fb3806fd34](https://github.com/MariaDB/server/commit/fb3806fd34)\
  2016-11-21 17:23:10 +0400
  * [MDEV-11294](https://jira.mariadb.org/browse/MDEV-11294) Move definitions of Derivation, DTCollation, Type\_std\_attributes from field.h and item.h to sql\_type.h
* [Revision #b9768dd17c](https://github.com/MariaDB/server/commit/b9768dd17c)\
  2016-11-18 15:40:45 +0400
  * [MDEV-11245](https://jira.mariadb.org/browse/MDEV-11245) Move prepare\_create\_field and sp\_prepare\_create\_field() as methods to Column\_definition
* [Revision #9ea06588f8](https://github.com/MariaDB/server/commit/9ea06588f8)\
  2016-11-16 10:08:17 +0400
  * [MDEV-10811](https://jira.mariadb.org/browse/MDEV-10811) Change design from "Item is Type\_handler" to "Item has Type\_handler"
* [Revision #3c4de09653](https://github.com/MariaDB/server/commit/3c4de09653)\
  2016-11-02 18:04:35 +0400
  * [MDEV-11146](https://jira.mariadb.org/browse/MDEV-11146) SP variables of the SET data type erroneously allow values with comma
* [Revision #e4ec85088f](https://github.com/MariaDB/server/commit/e4ec85088f)\
  2016-11-02 09:20:47 +0400
  * Starting the 10.3 branch

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
