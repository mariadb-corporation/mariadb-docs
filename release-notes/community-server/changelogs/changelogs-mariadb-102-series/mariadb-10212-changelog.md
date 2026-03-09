# MariaDB 10.2.12 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.12)[Release Notes](../../old-releases/10.2/10.2.12.md)[Changelog](mariadb-10212-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 4 Jan 2018

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.12.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* Merge [Revision #d361401bc2](https://github.com/MariaDB/server/commit/d361401bc2) 2018-01-03 11:46:31 +0200 - Merge 10.1 into 10.2, with some [MDEV-14799](https://jira.mariadb.org/browse/MDEV-14799) fixups
* Merge [Revision #016caa3d20](https://github.com/MariaDB/server/commit/016caa3d20) 2018-01-02 21:57:22 +0200 - Merge 10.0 into 10.1
* Merge [Revision #51e4650ed0](https://github.com/MariaDB/server/commit/51e4650ed0) 2018-01-02 21:52:46 +0200 - Merge 5.5 into 10.0
* [Revision #20fab71b14](https://github.com/MariaDB/server/commit/20fab71b14)\
  2018-01-02 21:41:39 +0200
  * Follow-up to [MDEV-14799](https://jira.mariadb.org/browse/MDEV-14799): Remove bogus debug assertions
* [Revision #d384ead0f0](https://github.com/MariaDB/server/commit/d384ead0f0)\
  2018-01-02 19:11:10 +0200
  * [MDEV-14799](https://jira.mariadb.org/browse/MDEV-14799) After UPDATE of indexed columns, old values will not be purged from secondary indexes
* [Revision #1300627a5d](https://github.com/MariaDB/server/commit/1300627a5d)\
  2017-12-27 22:10:17 +0100
  * [MDEV-14309](https://jira.mariadb.org/browse/MDEV-14309) MTR tests require perl-Env which is not always in the default installation
* [Revision #462808f3b6](https://github.com/MariaDB/server/commit/462808f3b6)\
  2017-12-20 13:52:27 +0100
  * [MDEV-10657](https://jira.mariadb.org/browse/MDEV-10657): incorrect result returned with binary protocol (prepared statements)
* [Revision #eef2bc5a5c](https://github.com/MariaDB/server/commit/eef2bc5a5c)\
  2017-12-28 17:13:42 +0200
  * Update mysqladmin man page
* [Revision #7a9fee9853](https://github.com/MariaDB/server/commit/7a9fee9853)\
  2018-01-02 09:25:37 +0200
  * [MDEV-13568](https://jira.mariadb.org/browse/MDEV-13568) gcol.innodb\_virtual\_debug\_purge failed in buildbot with wrong result
* [Revision #6f28f78429](https://github.com/MariaDB/server/commit/6f28f78429)\
  2018-01-02 20:43:29 +0200
  * More output in galera.query\_cache.test
* [Revision #83a8b0e9d3](https://github.com/MariaDB/server/commit/83a8b0e9d3)\
  2018-01-02 20:42:42 +0200
  * Fixed compiler warning
* [Revision #22b4f469ca](https://github.com/MariaDB/server/commit/22b4f469ca)\
  2018-01-02 18:18:47 +0200
  * [MDEV-14813](https://jira.mariadb.org/browse/MDEV-14813) rpl.rpl\_ctype\_latin1 fails in buildbot on Mac with wrong result
* [Revision #b2115ce235](https://github.com/MariaDB/server/commit/b2115ce235)\
  2018-01-02 21:50:40 +0200
  * Rocksdb fails to build when the source and build directory are not the same. This is a follow up fix for [MDEV-12458](https://jira.mariadb.org/browse/MDEV-12458)
* [Revision #b32b22baba](https://github.com/MariaDB/server/commit/b32b22baba)\
  2018-01-01 19:38:58 +0200
  * Disable warnings in partion\_alter\_myisam
* [Revision #aed2050e40](https://github.com/MariaDB/server/commit/aed2050e40)\
  2018-01-01 15:01:20 +0200
  * Ignore generated file rdb\_source\_revision.h
* [Revision #7e882a60bf](https://github.com/MariaDB/server/commit/7e882a60bf)\
  2018-01-01 14:44:20 +0200
  * Ensure that table->vcol\_set is properly restored if used
* [Revision #08ff39dca2](https://github.com/MariaDB/server/commit/08ff39dca2)\
  2018-01-01 14:12:18 +0200
  * Write location of core when doing core dump
* [Revision #322c637c1c](https://github.com/MariaDB/server/commit/322c637c1c)\
  2018-01-01 14:10:22 +0200
  * Fixed compiler warnings about possible uninitialized variables
* [Revision #7703095d2e](https://github.com/MariaDB/server/commit/7703095d2e)\
  2017-12-31 16:18:39 +0200
  * [MDEV-12458](https://jira.mariadb.org/browse/MDEV-12458): Variable and log records to indicate RocksDB version are missing
* [Revision #a118c20c81](https://github.com/MariaDB/server/commit/a118c20c81)\
  2017-12-30 10:18:22 +0530
  * [MDEV-10844](https://jira.mariadb.org/browse/MDEV-10844): EXPLAIN FORMAT=JSON doesn't show order direction for filesort
* [Revision #8bcbcac053](https://github.com/MariaDB/server/commit/8bcbcac053)\
  2017-12-29 17:25:21 +0200
  * Updated list of unstable tests for 10.2.12
* [Revision #f5c479565d](https://github.com/MariaDB/server/commit/f5c479565d)\
  2017-12-26 14:38:45 +0400
  * [MDEV-11071](https://jira.mariadb.org/browse/MDEV-11071) - Assertion \`thd->transaction.stmt.is\_empty()' failed in Locked\_tables\_list::unlock\_locked\_tables
* [Revision #24774fba65](https://github.com/MariaDB/server/commit/24774fba65)\
  2017-12-29 09:33:30 +0200
  * Update galera\_gtid\_slave result file post merge
* [Revision #6c4cf79d94](https://github.com/MariaDB/server/commit/6c4cf79d94)\
  2017-12-28 19:29:40 +0200
  * [MDEV-13683](https://jira.mariadb.org/browse/MDEV-13683): crash in Item\_window\_func::update\_used\_tables
* [Revision #8e9d8ffd1a](https://github.com/MariaDB/server/commit/8e9d8ffd1a)\
  2017-12-28 19:49:58 +0200
  * Update main.innodb test result post-merge
* [Revision #1a9728d901](https://github.com/MariaDB/server/commit/1a9728d901)\
  2017-12-28 19:27:07 +0200
  * Update Connector/C
* Merge [Revision #9aeb5d01d6](https://github.com/MariaDB/server/commit/9aeb5d01d6) 2017-12-28 19:27:00 +0200 - Merge remote-tracking branch 'origin/10.1' into bb-10.2-vicentiu
* [Revision #7e4c185c77](https://github.com/MariaDB/server/commit/7e4c185c77)\
  2017-09-13 21:02:44 +0200
  * [MDEV-14272](https://jira.mariadb.org/browse/MDEV-14272) Mariadb crashes with signal 11 when using federatedx engine and galera
* Merge [Revision #d1c2cd30b7](https://github.com/MariaDB/server/commit/d1c2cd30b7) 2017-12-27 17:50:39 +0200 - Merge remote-tracking branch '10.0' into 10.1
* [Revision #4b8cd4536a](https://github.com/MariaDB/server/commit/4b8cd4536a)\
  2017-12-22 14:03:25 +0400
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626) Merge InnoDB test cases from MySQL 5.7
* [Revision #24efee9100](https://github.com/MariaDB/server/commit/24efee9100)\
  2017-12-21 18:00:24 +0200
  * Follow up to [MDEV-12366](https://jira.mariadb.org/browse/MDEV-12366): FLUSH privileges can break hierarchy of roles
* [Revision #5377242fff](https://github.com/MariaDB/server/commit/5377242fff)\
  2017-12-24 18:39:00 +0100
  * [MDEV-14026](https://jira.mariadb.org/browse/MDEV-14026) ALTER TABLE ... DELAY\_KEY\_WRITE=1 creates table copy for partitioned MyISAM table with DATA DIRECTORY/INDEX DIRECTORY options
* [Revision #6d8b1bd620](https://github.com/MariaDB/server/commit/6d8b1bd620)\
  2017-12-24 18:37:42 +0100
  * cleanup: ha\_partition::update\_create\_info
* [Revision #c881d82c93](https://github.com/MariaDB/server/commit/c881d82c93)\
  2017-12-24 17:21:50 +0100
  * cleanup: ha\_myisam::data\_file\_name and index\_file\_name
* [Revision #2fe6186124](https://github.com/MariaDB/server/commit/2fe6186124)\
  2017-12-25 05:09:49 +0530
  * [MDEV-10715](https://jira.mariadb.org/browse/MDEV-10715) Galera: Replicate MariaDB GTID to other nodes in the cluster
* [Revision #db3bdca7c2](https://github.com/MariaDB/server/commit/db3bdca7c2)\
  2017-12-22 16:45:20 -0500
  * bump the VERSION
* [Revision #14de2ad3cb](https://github.com/MariaDB/server/commit/14de2ad3cb)\
  2017-12-28 11:47:03 +0200
  * Removed curr\_bitmap\_pos++ from possible macro
* [Revision #bbb8c9d773](https://github.com/MariaDB/server/commit/bbb8c9d773)\
  2017-12-24 14:08:20 -0800
  * Fixed the bug [MDEV-14755](https://jira.mariadb.org/browse/MDEV-14755) Crash when executing prepared statement for a query that uses CTE
* [Revision #02b7dc7bec](https://github.com/MariaDB/server/commit/02b7dc7bec)\
  2017-12-27 12:30:05 +0400
  * [MDEV-14249](https://jira.mariadb.org/browse/MDEV-14249) Wrong character set info of Query\_log\_event and the query in Query\_log\_event constructed by different charsets cause error when slave apply the event.
* [Revision #c3bd0b0301](https://github.com/MariaDB/server/commit/c3bd0b0301)\
  2017-11-18 00:05:22 +0800
  * Appveyor: apply feedback from wlad, timeout=4
* [Revision #e8182df142](https://github.com/MariaDB/server/commit/e8182df142)\
  2017-07-20 10:32:25 +1000
  * [MDEV-12386](https://jira.mariadb.org/browse/MDEV-12386): Use AppVeyor for public Windows CI
* [Revision #76056559ac](https://github.com/MariaDB/server/commit/76056559ac)\
  2017-11-29 18:36:17 +0100
  * [MDEV-9869](https://jira.mariadb.org/browse/MDEV-9869) INSTALL SONAME 'ha\_connect'
* [Revision #9631d933fb](https://github.com/MariaDB/server/commit/9631d933fb)\
  2017-12-03 02:17:12 +0100
  * debian: don't be smart about skipping plugins
* [Revision #f0f3b6549a](https://github.com/MariaDB/server/commit/f0f3b6549a)\
  2017-12-25 08:10:48 +0400
  * [MDEV-13970](https://jira.mariadb.org/browse/MDEV-13970) crash in Item\_func\_json\_extract::read\_json.
* [Revision #6e7ca6b0b2](https://github.com/MariaDB/server/commit/6e7ca6b0b2)\
  2017-12-23 14:53:12 +0200
  * [MDEV-13719](https://jira.mariadb.org/browse/MDEV-13719) Assertion \`bit < (map)->n\_bits' failed in bitmap\_is\_set
* Merge [Revision #068b1d0eb8](https://github.com/MariaDB/server/commit/068b1d0eb8) 2017-12-23 13:32:54 +0300 - Merge branch '10.2' into bb-10.2-mariarocks
* Merge [Revision #985d2d393c](https://github.com/MariaDB/server/commit/985d2d393c) 2017-12-22 12:23:39 +0200 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #a76a2522ec](https://github.com/MariaDB/server/commit/a76a2522ec)\
  2017-12-22 08:22:10 +0400
  * [MDEV-14426](https://jira.mariadb.org/browse/MDEV-14426) Assertion in Diagnostics\_area::set\_error\_status when using a bad datetime with PS and SP
* [Revision #8c3a1b15e6](https://github.com/MariaDB/server/commit/8c3a1b15e6)\
  2017-12-22 13:22:59 +0300
  * Fix a typo in previous commit
* [Revision #5426f6e30f](https://github.com/MariaDB/server/commit/5426f6e30f)\
  2017-12-22 02:30:32 +0300
  * Better comments: explain why slave\_use\_idempotent\_for\_recovery is disabled
* [Revision #ab0a7e13b2](https://github.com/MariaDB/server/commit/ab0a7e13b2)\
  2017-12-22 02:21:27 +0300
  * More fixes in MyRocks' rocksdb\_rpl testsuite
* [Revision #aed781ef7f](https://github.com/MariaDB/server/commit/aed781ef7f)\
  2017-12-22 01:13:43 +0300
  * Cleanup in storage/rocksdb/mysql-test/rocksdb\_rpl/t/disabled.def
* Merge [Revision #9c28fd7a33](https://github.com/MariaDB/server/commit/9c28fd7a33) 2017-12-21 23:34:49 +0300 - Merge branch '10.2' into bb-10.2-mariarocks
* [Revision #207976d6b9](https://github.com/MariaDB/server/commit/207976d6b9)\
  2017-12-21 02:34:02 +0300
  * Better comments part #2
* [Revision #e27e7ec767](https://github.com/MariaDB/server/commit/e27e7ec767)\
  2017-12-21 02:02:25 +0300
  * Better comments part #1
* [Revision #85fad60dc7](https://github.com/MariaDB/server/commit/85fad60dc7)\
  2017-12-21 01:50:44 +0300
  * Disable back rocksdb.col\_opt\_zerofill due to [MDEV-14729](https://jira.mariadb.org/browse/MDEV-14729)
* [Revision #73fa7aeb20](https://github.com/MariaDB/server/commit/73fa7aeb20)\
  2017-12-20 19:49:56 +0300
  * [MDEV-14165](https://jira.mariadb.org/browse/MDEV-14165): not MyRocks -problem in ps-protocol, happens in upstream too
* [Revision #21eed925a0](https://github.com/MariaDB/server/commit/21eed925a0)\
  2017-12-20 19:37:07 +0300
  * Cleanup out of date comments (no real changes).
* [Revision #eb14042383](https://github.com/MariaDB/server/commit/eb14042383)\
  2017-12-20 16:52:02 +0100
  * [MDEV-14613](https://jira.mariadb.org/browse/MDEV-14613): Assertion \`fixed == 0' failed in Item\_func::fix\_fields
* Merge [Revision #8d70097c21](https://github.com/MariaDB/server/commit/8d70097c21) 2017-12-19 16:48:28 +0200 - Merge 10.1 to 10.2
* [Revision #079c359971](https://github.com/MariaDB/server/commit/079c359971)\
  2017-12-19 11:49:40 +0200
  * [MDEV-14629](https://jira.mariadb.org/browse/MDEV-14629): failing assertion when a user-defined variable is defined by the recursive CTE
* [Revision #06f0b23a78](https://github.com/MariaDB/server/commit/06f0b23a78)\
  2017-12-17 17:53:53 +0200
  * Fixed memory leak in my\_rocks
* [Revision #4bd63bd551](https://github.com/MariaDB/server/commit/4bd63bd551)\
  2017-12-16 17:45:55 +0300
  * [MDEV-14679](https://jira.mariadb.org/browse/MDEV-14679): RocksdB plugin fails to load with "Loading of unknown plugin ROCKSDB\_CFSTATS
* [Revision #7380376370](https://github.com/MariaDB/server/commit/7380376370)\
  2017-12-16 16:44:33 +0300
  * [MDEV-14293](https://jira.mariadb.org/browse/MDEV-14293): MyRocks lacks basic functionality
* [Revision #64b11e61b5](https://github.com/MariaDB/server/commit/64b11e61b5)\
  2017-12-15 17:59:33 +0300
  * [MDEV-14293](https://jira.mariadb.org/browse/MDEV-14293): MyRocks lacks basic functionality
* [Revision #a9a4089175](https://github.com/MariaDB/server/commit/a9a4089175)\
  2017-12-14 13:47:38 +0200
  * Plug a small memory leak in mariadb-backup --backup
* [Revision #8063804943](https://github.com/MariaDB/server/commit/8063804943)\
  2017-12-13 23:14:54 +0200
  * Re-remove the file kill\_and\_restart\_mysqld.inc
* Merge [Revision #ece9c54e10](https://github.com/MariaDB/server/commit/ece9c54e10) 2017-12-13 23:14:15 +0200 - Merge 10.1 into 10.2
* [Revision #58eb4e5db9](https://github.com/MariaDB/server/commit/58eb4e5db9)\
  2017-12-13 14:16:15 +0200
  * [MDEV-14422](https://jira.mariadb.org/browse/MDEV-14422) Assertion failure in trx\_purge\_run() on shutdown
* [Revision #0e69d0b094](https://github.com/MariaDB/server/commit/0e69d0b094)\
  2017-12-13 00:29:44 +0200
  * [MDEV-14607](https://jira.mariadb.org/browse/MDEV-14607) storage\_engine-rocksdb.type\_bit\_indexes fails after latest pushes
* [Revision #a3476a5de2](https://github.com/MariaDB/server/commit/a3476a5de2)\
  2017-12-12 20:00:28 +0200
  * Skip btr\_search\_latches\[] in SHOW ENGINE INNODB STATUS
* [Revision #86c69263a4](https://github.com/MariaDB/server/commit/86c69263a4)\
  2017-12-12 13:31:41 +0300
  * [MDEV-14389](https://jira.mariadb.org/browse/MDEV-14389): MyRocks and NOPAD collations
* [Revision #e12f77a7e3](https://github.com/MariaDB/server/commit/e12f77a7e3)\
  2017-12-12 01:33:03 +0300
  * [MDEV-14389](https://jira.mariadb.org/browse/MDEV-14389): MyRocks and NOPAD collations
* [Revision #13b9ec651a](https://github.com/MariaDB/server/commit/13b9ec651a)\
  2017-12-11 14:39:53 +0200
  * [MDEV-14589](https://jira.mariadb.org/browse/MDEV-14589) InnoDB should not lock a delete-marked record
* [Revision #434c9e6f0e](https://github.com/MariaDB/server/commit/434c9e6f0e)\
  2017-12-11 13:55:05 +0200
  * [MDEV-14614](https://jira.mariadb.org/browse/MDEV-14614) InnoDB: Failing assertion in dict\_stats\_rename\_table()
* [Revision #1e6ac94451](https://github.com/MariaDB/server/commit/1e6ac94451)\
  2017-12-11 12:37:19 +0200
  * Correct the comment of row\_vers\_impl\_x\_locked()
* [Revision #15219eb08a](https://github.com/MariaDB/server/commit/15219eb08a)\
  2017-12-11 12:41:45 +0200
  * [MDEV-14290](https://jira.mariadb.org/browse/MDEV-14290) Binlog rotate crashes when two commit\_checkpoint\_notify capable engines.
* [Revision #bdeb27a000](https://github.com/MariaDB/server/commit/bdeb27a000)\
  2017-12-10 19:22:48 +0300
  * [MDEV-14123](https://jira.mariadb.org/browse/MDEV-14123): .rocksdb folder may break workflow which re-create data directory
* [Revision #ddc1d6904a](https://github.com/MariaDB/server/commit/ddc1d6904a)\
  2017-12-08 16:41:51 +0300
  * [MDEV-14123](https://jira.mariadb.org/browse/MDEV-14123): .rocksdb folder may break workflow which re-create data directory
* [Revision #b8a0373ed2](https://github.com/MariaDB/server/commit/b8a0373ed2)\
  2017-12-08 16:13:03 +0300
  * [MDEV-14123](https://jira.mariadb.org/browse/MDEV-14123): ".rocksdb folder may break workflow", and other MDEVs
* [Revision #40eee1da17](https://github.com/MariaDB/server/commit/40eee1da17)\
  2017-12-11 10:06:32 +0200
  * [MDEV-14614](https://jira.mariadb.org/browse/MDEV-14614) InnoDB: Failing assertion: trx->error\_state == DB\_SUCCESS or lock wait timeout upon saving statistics
* [Revision #86beb08774](https://github.com/MariaDB/server/commit/86beb08774)\
  2017-12-11 09:31:28 +0200
  * Remove an unnecessary dependency on persistent statistics
* [Revision #0af52734a7](https://github.com/MariaDB/server/commit/0af52734a7)\
  2017-12-08 16:36:19 +0200
  * Remove the unused function row\_is\_magic\_monitor\_table()
* [Revision #51bc407403](https://github.com/MariaDB/server/commit/51bc407403)\
  2017-12-08 16:31:54 +0200
  * Remove dead code for "InnoDB table(space) monitor"
* [Revision #bf96310657](https://github.com/MariaDB/server/commit/bf96310657)\
  2017-12-08 13:10:41 +0000
  * Fix warnings
* [Revision #2662228d18](https://github.com/MariaDB/server/commit/2662228d18)\
  2017-12-08 13:33:11 +0200
  * Fix test failures.
* [Revision #0e5eef886a](https://github.com/MariaDB/server/commit/0e5eef886a)\
  2017-12-08 13:19:19 +0400
  * [MDEV-14350](https://jira.mariadb.org/browse/MDEV-14350) Index use with collation utf8mb4\_unicode\_nopad\_ci on LIKE pattern with wrong results
* [Revision #dfafe15abb](https://github.com/MariaDB/server/commit/dfafe15abb)\
  2017-12-08 09:53:11 +0200
  * [MDEV-14606](https://jira.mariadb.org/browse/MDEV-14606) Assertion failure on IMPORT TABLESPACE
* [Revision #578b26598a](https://github.com/MariaDB/server/commit/578b26598a)\
  2017-12-08 01:15:10 +0300
  * [MDEV-14607](https://jira.mariadb.org/browse/MDEV-14607): storage\_engine-rocksdb.type\_bit\_indexes fails after latest pushes
* [Revision #4d016e6ed2](https://github.com/MariaDB/server/commit/4d016e6ed2)\
  2017-12-07 12:59:32 +0200
  * Add Galera test cases that fail to disabled.
* [Revision #ba576c5b78](https://github.com/MariaDB/server/commit/ba576c5b78)\
  2017-12-07 12:43:26 +0200
  * [MDEV-14401](https://jira.mariadb.org/browse/MDEV-14401): Stored procedure that declares a handler that catches ER\_LOCK\_DEADLOCK error causes thd->is\_error() assertion
* [Revision #da3a3a68df](https://github.com/MariaDB/server/commit/da3a3a68df)\
  2017-12-07 12:26:29 +0200
  * [MDEV-12837](https://jira.mariadb.org/browse/MDEV-12837): WSREP: BF lock wait long
* [Revision #3eaca005ff](https://github.com/MariaDB/server/commit/3eaca005ff)\
  2017-12-05 17:05:05 +0200
  * Ensure that mysqladmin also works with [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) + more
* Merge [Revision #51c73a431f](https://github.com/MariaDB/server/commit/51c73a431f) 2017-12-07 08:17:50 +0200 - Merge 10.1 into 10.2
* [Revision #77fb7ccba4](https://github.com/MariaDB/server/commit/77fb7ccba4)\
  2017-12-04 16:26:14 +0200
  * Follow-up fix to [MDEV-13201](https://jira.mariadb.org/browse/MDEV-13201) Assertion `srv_undo_sources || ...` failed on shutdown during DDL operation
* [Revision #7dc6066dea](https://github.com/MariaDB/server/commit/7dc6066dea)\
  2017-12-01 16:51:24 +0200
  * [MDEV-14511](https://jira.mariadb.org/browse/MDEV-14511) Use fewer transactions for updating InnoDB persistent statistics
* [Revision #2c1e4d4d7a](https://github.com/MariaDB/server/commit/2c1e4d4d7a)\
  2017-12-05 16:33:38 +0300
  * [MDEV-14563](https://jira.mariadb.org/browse/MDEV-14563): Wrong query plan for query with no PK
* [Revision #a6254e5e7d](https://github.com/MariaDB/server/commit/a6254e5e7d)\
  2017-12-04 15:01:57 +0300
  * [MDEV-14563](https://jira.mariadb.org/browse/MDEV-14563): Wrong query plan for query with no PK
* [Revision #c3803914c5](https://github.com/MariaDB/server/commit/c3803914c5)\
  2017-12-02 17:26:37 +0000
  * [MDEV-14433](https://jira.mariadb.org/browse/MDEV-14433): RocksDB may show empty or incorrect output with rocksdb\_strict\_collation\_check=off
* Merge [Revision #f1f2b7742f](https://github.com/MariaDB/server/commit/f1f2b7742f) 2017-12-06 10:40:58 +0200 - [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626) Merge InnoDB test cases from MySQL 5.7 (part 4)
* [Revision #afe6aef5ff](https://github.com/MariaDB/server/commit/afe6aef5ff)\
  2017-12-06 10:37:08 +0200
  * Adjust the test innodb.virtual\_stats and rename to gcol.innodb\_virtual\_stats
* [Revision #b1cd5ca2af](https://github.com/MariaDB/server/commit/b1cd5ca2af)\
  2017-12-06 10:35:09 +0200
  * Import innodb.virtual\_stats from MySQL 5.7
* [Revision #e9bc0f75ef](https://github.com/MariaDB/server/commit/e9bc0f75ef)\
  2017-12-06 10:32:24 +0200
  * [MDEV-5834](https://jira.mariadb.org/browse/MDEV-5834) cleanup: Inline two tiny functions
* Merge [Revision #1d526f31fb](https://github.com/MariaDB/server/commit/1d526f31fb) 2017-12-05 14:23:57 +0200 - Merge 10.1 into 10.2
* [Revision #d1ab89037a](https://github.com/MariaDB/server/commit/d1ab89037a)\
  2017-12-05 12:50:35 +0200
  * [MDEV-13670](https://jira.mariadb.org/browse/MDEV-13670)/[MDEV-14550](https://jira.mariadb.org/browse/MDEV-14550) Error log flood : "InnoDB: page\_cleaner: 1000ms intended loop took N ms. The settings might not be optimal."
* [Revision #8be7548085](https://github.com/MariaDB/server/commit/8be7548085)\
  2017-12-04 13:43:02 +0200
  * Follow-up to [MDEV-12698](https://jira.mariadb.org/browse/MDEV-12698): Adjust some comments
* [Revision #bd8fd3b7c3](https://github.com/MariaDB/server/commit/bd8fd3b7c3)\
  2017-12-04 11:48:12 +0200
  * Remove references to UNIV\_SYNC\_DEBUG which was merged with UNIV\_DEBUG
* [Revision #d9188adae5](https://github.com/MariaDB/server/commit/d9188adae5)\
  2017-12-03 12:45:54 +0200
  * resolve\_stack\_dump updated to match latest stack trace format
* [Revision #40bf5c951b](https://github.com/MariaDB/server/commit/40bf5c951b)\
  2017-12-01 15:28:33 +0200
  * Fix a Bison warning about semantic type clash in default action
* [Revision #8d24bef640](https://github.com/MariaDB/server/commit/8d24bef640)\
  2017-12-01 15:02:04 +0200
  * [MDEV-14080](https://jira.mariadb.org/browse/MDEV-14080) InnoDB shutdown sometimes hangs
* [Revision #f59a1826f8](https://github.com/MariaDB/server/commit/f59a1826f8)\
  2017-11-29 22:56:23 +0000
  * [MDEV-14536](https://jira.mariadb.org/browse/MDEV-14536) : during backup, retry read of log blocks, if there is (possibly intermittent) checksum mismatch.
* Merge [Revision #3fe261bd2b](https://github.com/MariaDB/server/commit/3fe261bd2b) 2017-11-29 15:08:04 +0000 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #8cee2f136d](https://github.com/MariaDB/server/commit/8cee2f136d)\
  2017-11-23 18:42:28 +0200
  * [MDEV-13384](https://jira.mariadb.org/browse/MDEV-13384): "window" seems like a reserved column name but it's not listed as one
* [Revision #b65fd73bb1](https://github.com/MariaDB/server/commit/b65fd73bb1)\
  2017-11-28 15:59:36 -0500
  * bump the VERSION
* [Revision #23d2dae5f0](https://github.com/MariaDB/server/commit/23d2dae5f0)\
  2017-11-28 18:23:35 +0200
  * Fix some integer type mismatch warnings
* [Revision #e02b860861](https://github.com/MariaDB/server/commit/e02b860861)\
  2017-11-20 20:39:59 +0000
  * Windows, generic threadpool cleanups

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
