# MariaDB 10.1.19 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.19)[Release Notes](../../old-releases/10.1/10.1.19.md)[Changelog](mariadb-10119-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 7 Nov 2016

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.19.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #5fda340](https://github.com/MariaDB/server/commit/5fda340)\
  2016-11-04 14:04:24 +0300
  * Remove galera suites from default list for now, tests are unstable
* [Revision #1ddd1b5](https://github.com/MariaDB/server/commit/1ddd1b5)\
  2016-11-04 13:41:26 +0300
  * Add sphinx tests to the list, just in case they are run somewhere
* [Revision #ee0094d](https://github.com/MariaDB/server/commit/ee0094d)\
  2016-11-04 13:33:28 +0300
  * [MDEV-10985](https://jira.mariadb.org/browse/MDEV-10985), [MDEV-10986](https://jira.mariadb.org/browse/MDEV-10986) - sphinx tests have not been maintained
* [Revision #cbfb3f9](https://github.com/MariaDB/server/commit/cbfb3f9)\
  2016-11-03 19:30:02 -0400
  * Move disabled galera tests to galera/disabled.def
* [Revision #d34cd35](https://github.com/MariaDB/server/commit/d34cd35)\
  2016-11-03 22:07:31 +0400
  * Disabling tests mentioned in [MDEV-11229](https://jira.mariadb.org/browse/MDEV-11229) galera.MW-258 galera.galera\_as\_master fail in buildbot
* [Revision #f0d8a4d](https://github.com/MariaDB/server/commit/f0d8a4d)\
  2016-11-03 22:02:24 +0400
  * [MDEV-11219](https://jira.mariadb.org/browse/MDEV-11219) main.null fails in buldbot and outside with ps-protocol
* [Revision #82780a7](https://github.com/MariaDB/server/commit/82780a7)\
  2016-11-02 21:20:00 +0300
  * [MDEV-11130](https://jira.mariadb.org/browse/MDEV-11130) Update the list of unstable tests for 10.1
* [Revision #54d3dc0](https://github.com/MariaDB/server/commit/54d3dc0)\
  2016-11-01 17:27:53 -0400
  * Fix/disable some failing galera tests.
* [Revision #7a17020](https://github.com/MariaDB/server/commit/7a17020)\
  2016-10-26 13:19:00 -0400
  * [MDEV-11152](https://jira.mariadb.org/browse/MDEV-11152): wsrep\_replicate\_myisam: SELECT gets replicated using TO
* [Revision #07918b4](https://github.com/MariaDB/server/commit/07918b4)\
  2016-10-10 14:02:37 -0400
  * [MDEV-10993](https://jira.mariadb.org/browse/MDEV-10993): wsrep.mdev\_10186 result depends on location of galera library
* [Revision #3daf89c](https://github.com/MariaDB/server/commit/3daf89c)\
  2016-10-05 04:24:07 -0400
  * [MDEV-10957](https://jira.mariadb.org/browse/MDEV-10957): Assertion failure when dropping a myisam table with wsrep\_replicate\_myisam enabled
* [Revision #6dbfe7f](https://github.com/MariaDB/server/commit/6dbfe7f)\
  2016-10-03 12:02:46 -0400
  * [MDEV-10944](https://jira.mariadb.org/browse/MDEV-10944): GALERA log-slave-updates FAIL after upgrading from 10.1.17 to 10.1.18
* [Revision #fa4fa0a](https://github.com/MariaDB/server/commit/fa4fa0a)\
  2016-09-30 21:13:03 -0400
  * Make galera test suites default.
* [Revision #a52a68c](https://github.com/MariaDB/server/commit/a52a68c)\
  2016-07-13 16:17:08 -0400
  * fix the tokudb\_analyze\_in\_background\_basic test to run on mariadb. mariadb does additional value checking for boolean system variables
* [Revision #110a9f0](https://github.com/MariaDB/server/commit/110a9f0)\
  2016-07-13 15:15:35 -0400
  * add mtr support files for tokudb\_sys\_vars tests
* [Revision #c948559](https://github.com/MariaDB/server/commit/c948559)\
  2016-07-20 13:43:53 -0400
  * [MDEV-10408](https://jira.mariadb.org/browse/MDEV-10408) run the tokudb\_rpl.rpl\_rfr\_disable\_on\_expl\_pk\_absence test. Add control files. Fixup result file for mariadb
* [Revision #a98c85b](https://github.com/MariaDB/server/commit/a98c85b) 2016-11-02 13:44:07 +0100 - Merge branch '10.0-galera' into 10.1
* [Revision #7196691](https://github.com/MariaDB/server/commit/7196691)\
  2016-11-01 17:20:12 -0400
  * Fix/disable some failing galera tests.
* [Revision #5db2195](https://github.com/MariaDB/server/commit/5db2195) 2016-10-28 15:50:13 -0400 - Merge tag 'mariadb-10.0.28' into 10.0-galera
* [Revision #eca8c32](https://github.com/MariaDB/server/commit/eca8c32)\
  2016-10-27 19:07:55 +0200
  * Typo fixed.
* [Revision #a079565](https://github.com/MariaDB/server/commit/a079565)\
  2016-10-27 12:23:31 +0200
  * [MDEV-10846](https://jira.mariadb.org/browse/MDEV-10846) Running mysqldump backup twice returns error: Table 'mysql.proc' doesn't exist.
* [Revision #d451d77](https://github.com/MariaDB/server/commit/d451d77)\
  2016-10-26 10:59:38 -0700
  * Fixed bug [MDEV-9628](https://jira.mariadb.org/browse/MDEV-9628). In the function create\_key\_parts\_for\_pseudo\_indexes() the key part structures of pseudo-indexes created for BLOB fields were set incorrectly. Also the key parts for long fields must be 'truncated' up to the maximum length acceptable for key parts.
* [Revision #9d4a0dd](https://github.com/MariaDB/server/commit/9d4a0dd)\
  2016-10-24 10:15:11 -0700
  * Fixed bug [MDEV-11096](https://jira.mariadb.org/browse/MDEV-11096). 1. When min/max value is provided the null flag for it must be set to 0 in the bitmap Culumn\_statistics::column\_stat\_nulls. 2. When the calculation of the selectivity of the range condition over a column requires min and max values for the column then we have to check that these values are provided.
* [Revision #26b87c3](https://github.com/MariaDB/server/commit/26b87c3)\
  2016-10-27 00:04:26 +0400
  * [MDEV-10846](https://jira.mariadb.org/browse/MDEV-10846) Running mysqldump backup twice returns error: Table 'mysql.proc' doesn't exist.
* [Revision #22490a0](https://github.com/MariaDB/server/commit/22490a0)\
  2016-10-26 13:26:43 +0200
  * [MDEV-8345](https://jira.mariadb.org/browse/MDEV-8345) STOP SLAVE should not cause an ERROR to be logged to the error log
* [Revision #2593270](https://github.com/MariaDB/server/commit/2593270)\
  2016-10-26 12:30:18 +0200
  * backport include/search\_pattern\_in\_file.inc from 10.1
* [Revision #5569ac0](https://github.com/MariaDB/server/commit/5569ac0)\
  2016-10-25 15:08:15 +0300
  * [MDEV-11126](https://jira.mariadb.org/browse/MDEV-11126): Crash while altering persistent virtual column
* [Revision #59a7bc3](https://github.com/MariaDB/server/commit/59a7bc3)\
  2016-10-26 14:09:11 +0400
  * Removed duplicate open\_strategy assignments
* [Revision #a3c980b](https://github.com/MariaDB/server/commit/a3c980b)\
  2016-10-24 15:26:11 +0400
  * [MDEV-10824](https://jira.mariadb.org/browse/MDEV-10824) - Crash in CREATE OR REPLACE TABLE t1 AS SELECT spfunc()
* [Revision #9155cc7](https://github.com/MariaDB/server/commit/9155cc7)\
  2016-08-31 15:57:02 +1000
  * [MDEV-10292](https://jira.mariadb.org/browse/MDEV-10292): Tokudb - PerconaFT - compile error in recent gcc
* [Revision #ad5b88a](https://github.com/MariaDB/server/commit/ad5b88a)\
  2016-10-26 09:26:34 +0000
  * Fix build error in XtraDB on Windows.
* [Revision #bd4568a](https://github.com/MariaDB/server/commit/bd4568a) 2016-10-26 10:49:31 +0200 - Merge branch 'bb-10.0-serg' into 10.0
* [Revision #2cfccbe](https://github.com/MariaDB/server/commit/2cfccbe) 2016-10-25 21:59:06 +0200 - Merge branch 'connect/10.0' into 10.0
* [Revision #b7aee7d](https://github.com/MariaDB/server/commit/b7aee7d)\
  2016-10-14 18:29:33 +0200
  * Fix [MDEV-10950](https://jira.mariadb.org/browse/MDEV-10950). Null values not retrieved for numeric types. Now the null is tested using the result set getObject method.
* [Revision #9b20d60](https://github.com/MariaDB/server/commit/9b20d60)\
  2016-10-05 23:44:54 +0200
  * Fix [MDEV-10948](https://jira.mariadb.org/browse/MDEV-10948). Syntax error on quoted JDBC tables. Was because the quoting character was always '"' instead of being retrieve from the JDBC source.
* [Revision #7d596c9](https://github.com/MariaDB/server/commit/7d596c9)\
  2016-09-16 22:14:14 +0200
  * Working on [MDEV-10525](https://jira.mariadb.org/browse/MDEV-10525). Lrecl mismatch on DBF files
* [Revision #2140dcf](https://github.com/MariaDB/server/commit/2140dcf) 2016-09-05 13:19:28 +0200 - Merge branch '10.0' of [server](https://github.com/MariaDB/server) into ob-10.0
* [Revision #213765c](https://github.com/MariaDB/server/commit/213765c)\
  2016-09-05 13:18:04 +0200
  * Fix [MDEV-10496](https://jira.mariadb.org/browse/MDEV-10496). Memory leak in discovery
* [Revision #de9ea40](https://github.com/MariaDB/server/commit/de9ea40) 2016-10-25 21:58:59 +0200 - Merge branch 'merge/merge-tokudb-5.6' into 10.0
* [Revision #d9787aa](https://github.com/MariaDB/server/commit/d9787aa)\
  2016-10-25 17:03:23 +0200
  * 5.6.33-79.0
* [Revision #675f27b](https://github.com/MariaDB/server/commit/675f27b) 2016-10-25 18:28:31 +0200 - Merge branch 'merge/merge-xtradb-5.6' into 10.0
* [Revision #d7dc03a](https://github.com/MariaDB/server/commit/d7dc03a)\
  2016-10-25 17:01:37 +0200
  * 5.6.33-79.0
* [Revision #12c3e16](https://github.com/MariaDB/server/commit/12c3e16) 2016-10-25 16:41:43 +0200 - Merge branch '5.5' into 10.0
* [Revision #6e25727](https://github.com/MariaDB/server/commit/6e25727)\
  2016-10-17 11:43:47 -0400
  * bump the VERSION
* [Revision #df87be5](https://github.com/MariaDB/server/commit/df87be5)\
  2016-10-17 14:04:45 +0300
  * [MDEV-11069](https://jira.mariadb.org/browse/MDEV-11069) main.information\_schema test fails if hostname includes 'user'
* [Revision #eac8d95](https://github.com/MariaDB/server/commit/eac8d95)\
  2016-10-14 12:51:53 +0200
  * compilation warning after xtradb merge
* [Revision #5a43a31](https://github.com/MariaDB/server/commit/5a43a31)\
  2016-10-14 00:33:49 +0200
  * mysqldump: comments and identifiers with new lines
* [Revision #01b39b7](https://github.com/MariaDB/server/commit/01b39b7)\
  2016-10-13 20:58:08 +0200
  * mysqltest: don't eat new lines in `--exec`
* [Revision #383007c](https://github.com/MariaDB/server/commit/383007c)\
  2016-10-13 21:35:01 +0200
  * mysql cli: fix USE command quoting
* [Revision #e4957de](https://github.com/MariaDB/server/commit/e4957de) 2016-10-13 12:40:24 +0200 - Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #6010a27](https://github.com/MariaDB/server/commit/6010a27)\
  2016-10-13 12:23:16 +0200
  * 5.5.52-38.3
* [Revision #02be50a](https://github.com/MariaDB/server/commit/02be50a) 2016-10-13 11:18:30 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #82ab92b](https://github.com/MariaDB/server/commit/82ab92b)\
  2016-10-25 22:35:35 +0000
  * [MDEV-10951](https://jira.mariadb.org/browse/MDEV-10951) Field\_newdate::cmp access violation
* [Revision #ed3998a](https://github.com/MariaDB/server/commit/ed3998a)\
  2016-10-25 15:46:10 +0200
  * Revert "Add tokuftdump man page"
* [Revision #1daf746](https://github.com/MariaDB/server/commit/1daf746)\
  2016-10-25 16:34:22 +0300
  * Add tokuftdump man page
* [Revision #39dceaa](https://github.com/MariaDB/server/commit/39dceaa)\
  2016-10-09 12:09:44 +0200
  * [MDEV-10983](https://jira.mariadb.org/browse/MDEV-10983): TokuDB does not compile on OS X 10.12
* [Revision #ba11dd6](https://github.com/MariaDB/server/commit/ba11dd6)\
  2016-10-25 12:21:53 +0000
  * [MDEV-11127](https://jira.mariadb.org/browse/MDEV-11127) : Fix innochecksum to work with large files on Windows.
* [Revision #3321f1a](https://github.com/MariaDB/server/commit/3321f1a)\
  2016-06-21 13:35:59 +1000
  * [MDEV-5944](https://jira.mariadb.org/browse/MDEV-5944): Compile fix for OQGRAPH with LLVM
* [Revision #0c925aa](https://github.com/MariaDB/server/commit/0c925aa)\
  2016-10-23 18:47:44 +0300
  * [MDEV-11097](https://jira.mariadb.org/browse/MDEV-11097) - Update the list of unstable tests
* [Revision #fb38d26](https://github.com/MariaDB/server/commit/fb38d26)\
  2016-10-22 07:34:23 +0000
  * [MDEV-11104](https://jira.mariadb.org/browse/MDEV-11104) Fix client to correctly retrieve current user name on Windows
* [Revision #39b7aff](https://github.com/MariaDB/server/commit/39b7aff)\
  2016-10-21 23:02:56 +0200
  * Upstream MIPS 32bit-build-on-64bit patch from Debian Bug#838914
* [Revision #7eb4bd3](https://github.com/MariaDB/server/commit/7eb4bd3)\
  2016-10-21 22:43:46 +0200
  * Upstream patch from Debian Bug 838557
* [Revision #998f987](https://github.com/MariaDB/server/commit/998f987)\
  2016-10-21 22:37:51 +0200
  * Upstream MIPS test fixes from Debian Bug 838557.
* [Revision #4dfb6a3](https://github.com/MariaDB/server/commit/4dfb6a3)\
  2016-09-28 14:16:38 +0000
  * [MDEV-11083](https://jira.mariadb.org/browse/MDEV-11083) performance schema test fail with threadpool
* [Revision #4192c46](https://github.com/MariaDB/server/commit/4192c46)\
  2016-10-16 04:46:39 +0300
  * [MDEV-11061](https://jira.mariadb.org/browse/MDEV-11061) Valgrind builder produces endless warnings
* [Revision #8a49e00](https://github.com/MariaDB/server/commit/8a49e00)\
  2016-10-14 23:23:49 +0300
  * More unstable tests
* [Revision #f6d4f82](https://github.com/MariaDB/server/commit/f6d4f82)\
  2016-10-14 23:23:16 +0300
  * [MDEV-11061](https://jira.mariadb.org/browse/MDEV-11061) Valgrind builder produces endless warnings after switching to OpenSS
* [Revision #c18054d](https://github.com/MariaDB/server/commit/c18054d)\
  2016-11-02 08:20:15 +0400
  * [MDEV-10347](https://jira.mariadb.org/browse/MDEV-10347) mysqld got signal 11
* [Revision #554c60a](https://github.com/MariaDB/server/commit/554c60a)\
  2016-10-31 12:44:06 +0200
  * [MDEV-11182](https://jira.mariadb.org/browse/MDEV-11182): InnoDB: Assertion failure in file buf0buf.cc line 4730 (encryption.create\_or\_replace fails in buildbot and outside)
* [Revision #cb5685a](https://github.com/MariaDB/server/commit/cb5685a)\
  2016-10-31 08:49:36 +0200
  * [MDEV-11184](https://jira.mariadb.org/browse/MDEV-11184): innodb.innodb-wl5522-debug-zip fails in buildbot on Windows
* [Revision #9aa7315](https://github.com/MariaDB/server/commit/9aa7315)\
  2016-10-31 08:48:00 +0200
  * [MDEV-11183](https://jira.mariadb.org/browse/MDEV-11183): innodb.innodb-wl5522-debug fails in buildbot and outside
* [Revision #67e6cfd](https://github.com/MariaDB/server/commit/67e6cfd)\
  2016-10-30 09:16:02 +0200
  * Add suppression for new InnoDB error log error as this test intentionally produces this error.
* [Revision #58b5c40](https://github.com/MariaDB/server/commit/58b5c40)\
  2016-10-29 12:57:48 +0300
  * Remove accidentally added directory.
* [Revision #bb4b8c7](https://github.com/MariaDB/server/commit/bb4b8c7)\
  2016-10-28 13:59:35 +0300
  * [MDEV-9099](https://jira.mariadb.org/browse/MDEV-9099): Test encryption.innodb\_encryption\_discard\_import fails on buildbot
* [Revision #de0f77a](https://github.com/MariaDB/server/commit/de0f77a)\
  2016-10-28 09:27:03 +0300
  * [MDEV-11106](https://jira.mariadb.org/browse/MDEV-11106): Improve error messages when importing tablespaces
* [Revision #84ce681](https://github.com/MariaDB/server/commit/84ce681)\
  2016-10-27 15:01:15 +0300
  * [MDEV-10917](https://jira.mariadb.org/browse/MDEV-10917): Warning suggesting that innodb\_page\_size is experimental may be inaccurate
* [Revision #885577f](https://github.com/MariaDB/server/commit/885577f)\
  2016-10-27 14:51:10 +0300
  * [MDEV-11004](https://jira.mariadb.org/browse/MDEV-11004): Unable to start (Segfault or os error 2) when encryption key missing
* [Revision #bc32372](https://github.com/MariaDB/server/commit/bc32372)\
  2016-10-27 08:18:14 +0300
  * [MDEV-10977](https://jira.mariadb.org/browse/MDEV-10977): \[ERROR] InnoDB: Block in space\_id 0 in file ibdata1 encrypted. [MDEV-10394](https://jira.mariadb.org/browse/MDEV-10394): Innodb system table space corrupted
* [Revision #c1bbedb](https://github.com/MariaDB/server/commit/c1bbedb)\
  2016-10-28 20:37:18 +0200
  * AWS key Management plugin - add plugin variable for the region
* [Revision #ea0ae42](https://github.com/MariaDB/server/commit/ea0ae42) 2016-10-26 08:34:04 +0300 - Merge pull request #250 from sensssz/10.1-vats
* [Revision #7496176](https://github.com/MariaDB/server/commit/7496176)\
  2016-10-25 18:57:03 -0400
  * A few fixes for VATS in 10.1
* [Revision #4edd4ad](https://github.com/MariaDB/server/commit/4edd4ad)\
  2016-10-24 22:25:54 +0300
  * [MDEV-10970](https://jira.mariadb.org/browse/MDEV-10970): Crash while loading mysqldump backup when InnoDB encryption is enabled
* [Revision #021212b](https://github.com/MariaDB/server/commit/021212b) 2016-10-24 21:51:42 +0300 - Merge pull request #245 from sensssz/10.1-vats
* [Revision #183c028](https://github.com/MariaDB/server/commit/183c028)\
  2016-10-13 01:23:21 -0400
  * Move the lock after deadlock is resolved.
* [Revision #0a769b0](https://github.com/MariaDB/server/commit/0a769b0)\
  2016-10-12 21:54:31 -0400
  * Get thd by lock->trx->mysql\_thd.
* [Revision #5dc7ad8](https://github.com/MariaDB/server/commit/5dc7ad8)\
  2016-10-12 21:52:14 -0400
  * Reduce conflict during in-order replication.
* [Revision #55d2bff](https://github.com/MariaDB/server/commit/55d2bff)\
  2016-10-11 23:27:03 -0400
  * Bug fix: add \* and ; for innodb
* [Revision #288796f](https://github.com/MariaDB/server/commit/288796f)\
  2016-10-11 23:05:02 -0400
  * Bug fix: missing \* and ;
* [Revision #e93d44f](https://github.com/MariaDB/server/commit/e93d44f)\
  2016-10-11 23:02:26 -0400
  * Bug fix: add undeclared variables.
* [Revision #6100f59](https://github.com/MariaDB/server/commit/6100f59)\
  2016-10-11 20:52:35 -0400
  * Implement VATS both in InnoDB and XtraDB. Add configuration options for it in both of them.
* [Revision #1bfa37a](https://github.com/MariaDB/server/commit/1bfa37a)\
  2016-10-24 16:55:36 +0300
  * Add more information if encryption information is already stored for tablespace but page0 is not yet read.
* [Revision #ec5bd0d](https://github.com/MariaDB/server/commit/ec5bd0d)\
  2016-10-24 09:25:36 +0300
  * [MDEV-10969](https://jira.mariadb.org/browse/MDEV-10969): innochecksum dumps core for some .ibd files due to floating point exception
* [Revision #aea1967](https://github.com/MariaDB/server/commit/aea1967) 2016-10-24 09:05:10 +0300 - Merge pull request #249 from Cona19/10.1-remove-unnecessary-semicolon
* [Revision #9401e6b](https://github.com/MariaDB/server/commit/9401e6b)\
  2016-10-24 14:58:41 +0900
  * Remove unnecessary semicolons
* [Revision #ee1d08c](https://github.com/MariaDB/server/commit/ee1d08c)\
  2016-10-23 00:10:37 +0000
  * Revert "Prepare XtraDB to be used with xtrabackup."
* [Revision #de5646f](https://github.com/MariaDB/server/commit/de5646f)\
  2016-10-22 14:10:12 +0000
  * Prepare XtraDB to be used with xtrabackup.
* [Revision #8f5e3e2](https://github.com/MariaDB/server/commit/8f5e3e2)\
  2016-10-21 16:20:47 +0000
  * Fix escaping '' in a string constant.
* [Revision #2584897](https://github.com/MariaDB/server/commit/2584897)\
  2016-10-19 03:02:13 +0300
  * [MDEV-11082](https://jira.mariadb.org/browse/MDEV-11082) mysql\_client\_test: test\_ps\_query\_cache fails with group-concat-max-len=1M
* [Revision #fd1f507](https://github.com/MariaDB/server/commit/fd1f507)\
  2016-10-19 03:01:36 +0300
  * Additions to the list of unstable tests
* [Revision #c4776d3](https://github.com/MariaDB/server/commit/c4776d3) 2016-10-16 23:48:59 +0200 - Merge "remove unnecessary global mutex in parallel replication" into 10.1.
* [Revision #50f19ca](https://github.com/MariaDB/server/commit/50f19ca)\
  2016-09-20 15:30:57 +0200
  * Remove unnecessary global mutex in parallel replication.
* [Revision #ed4a6f1](https://github.com/MariaDB/server/commit/ed4a6f1)\
  2016-10-10 12:49:10 +0000
  * [MDEV-10823](https://jira.mariadb.org/browse/MDEV-10823) amend : Use opt\_log\_basename instead of hostname to test filesystem case sensitivity.
* [Revision #f35e918](https://github.com/MariaDB/server/commit/f35e918)\
  2016-09-30 12:11:09 -0400
  * bump the VERSION
* [Revision #d83fd5f](https://github.com/MariaDB/server/commit/d83fd5f)\
  2016-09-30 09:13:39 +0300
  * [MDEV-10685](https://jira.mariadb.org/browse/MDEV-10685): innodb.xa\_recovery failed in buildbot

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
