# MariaDB 10.3.18 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.18/)[Release Notes](../../old-releases/10.3/10.3.18.md)[Changelog](mariadb-10318-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 11 Sep 2019

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.18.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.27](../changelogs-mariadb-102-series/mariadb-10227-changelog.md)
* [Revision #604f80e77c](https://github.com/MariaDB/server/commit/604f80e77c)\
  2019-09-08 19:49:40 +0300
  * List of unstable tests for 10.3.18 release
* Merge [Revision #f80e02e043](https://github.com/MariaDB/server/commit/f80e02e043) 2019-09-06 16:57:54 +0200 - Merge branch '10.2' into 10.3
* [Revision #2842c36985](https://github.com/MariaDB/server/commit/2842c36985)\
  2019-09-05 16:37:32 +0300
  * [MDEV-20425](https://jira.mariadb.org/browse/MDEV-20425): Enable a test for debug builds
* [Revision #67e2252ba1](https://github.com/MariaDB/server/commit/67e2252ba1)\
  2019-09-05 12:00:15 +0300
  * Simplify trx\_state\_eq()
* [Revision #2c9e75ccfe](https://github.com/MariaDB/server/commit/2c9e75ccfe)\
  2019-09-05 15:57:39 +0300
  * [MDEV-15326](https://jira.mariadb.org/browse/MDEV-15326) after-merge fixes
* Merge [Revision #537f8594a6](https://github.com/MariaDB/server/commit/537f8594a6) 2019-09-04 17:52:04 +0300 - Merge 10.2 into 10.3
* [Revision #647d5b2430](https://github.com/MariaDB/server/commit/647d5b2430)\
  2019-09-03 15:28:32 +0200
  * [MDEV-20079](https://jira.mariadb.org/browse/MDEV-20079) When setting back the system time while mysqld is running, NOW() and UNIX\_TIMESTAMP() results get stuck
* [Revision #08b01ace8a](https://github.com/MariaDB/server/commit/08b01ace8a)\
  2019-09-01 15:28:11 +0200
  * [MDEV-16871](https://jira.mariadb.org/browse/MDEV-16871) in\_predicate\_conversion\_threshold cannot be set in my.cnf
* Merge [Revision #7e08ac0b41](https://github.com/MariaDB/server/commit/7e08ac0b41) 2019-09-04 09:55:59 +0400 - Merge 10.2 (up to commit ef00ac4c86daf3294c46a45358da636763fb0049) into 10.3
* Merge [Revision #a071e0e029](https://github.com/MariaDB/server/commit/a071e0e029) 2019-09-02 14:06:56 +0300 - Merge branch '10.2' into 10.3
* Merge [Revision #b0ff5a6a73](https://github.com/MariaDB/server/commit/b0ff5a6a73) 2019-09-02 09:01:54 +0200 - Merge branch '10.2' into 10.3
* [Revision #597b070f82](https://github.com/MariaDB/server/commit/597b070f82)\
  2019-09-01 17:56:47 +0300
  * Compilation fix
* [Revision #1bbc593eae](https://github.com/MariaDB/server/commit/1bbc593eae)\
  2019-09-01 15:42:23 +0300
  * Fixed compiler warning that broke builds
* [Revision #6a490ca0fb](https://github.com/MariaDB/server/commit/6a490ca0fb)\
  2019-08-28 19:51:23 +0300
  * [MDEV-18501](https://jira.mariadb.org/browse/MDEV-18501) Partition pruning doesn't work for historical queries (fix)
* [Revision #c3f35ea55a](https://github.com/MariaDB/server/commit/c3f35ea55a)\
  2019-08-28 11:57:16 +0300
  * [MDEV-18501](https://jira.mariadb.org/browse/MDEV-18501) Partition pruning doesn't work for historical queries (refactoring)
* [Revision #a3e49c0d36](https://github.com/MariaDB/server/commit/a3e49c0d36)\
  2019-08-27 23:01:12 +0300
  * [MDEV-18501](https://jira.mariadb.org/browse/MDEV-18501) Partition pruning doesn't work for historical queries (cleanup)
* [Revision #396da1a705](https://github.com/MariaDB/server/commit/396da1a705)\
  2019-08-30 14:49:21 +0300
  * Enable some RocksDB tests that are enabled on 10.2
* Merge [Revision #a5472b0367](https://github.com/MariaDB/server/commit/a5472b0367) 2019-08-30 14:39:03 +0300 - Merge 10.2 into 10.3
* [Revision #17336f6d30](https://github.com/MariaDB/server/commit/17336f6d30)\
  2019-08-30 14:37:50 +0300
  * [MDEV-20066](https://jira.mariadb.org/browse/MDEV-20066) Wrong value on instantly added column after DELETE and UPDATE
* [Revision #f42a23178e](https://github.com/MariaDB/server/commit/f42a23178e)\
  2019-08-30 12:51:37 +0300
  * [MDEV-20425](https://jira.mariadb.org/browse/MDEV-20425): Fix -Wimplicit-fallthrough
* [Revision #a379f151b1](https://github.com/MariaDB/server/commit/a379f151b1)\
  2019-08-29 16:07:15 +0300
  * [MDEV-20109](https://jira.mariadb.org/browse/MDEV-20109): Optimizer ignores distinct key created for materialized...
* [Revision #ef76f81c98](https://github.com/MariaDB/server/commit/ef76f81c98)\
  2019-08-29 15:37:49 +0300
  * [MDEV-20109](https://jira.mariadb.org/browse/MDEV-20109): Optimizer ignores distinct key created for materialized...
* [Revision #d58437d195](https://github.com/MariaDB/server/commit/d58437d195)\
  2019-08-29 18:25:24 +0300
  * [MDEV-20149](https://jira.mariadb.org/browse/MDEV-20149) innodb.innodb-system-table-view fails with wrong result
* [Revision #d4246e25e5](https://github.com/MariaDB/server/commit/d4246e25e5)\
  2019-08-29 18:22:41 +0300
  * After-merge fix
* [Revision #e50b2bdbcf](https://github.com/MariaDB/server/commit/e50b2bdbcf)\
  2019-08-29 13:10:40 +0300
  * [MDEV-20425](https://jira.mariadb.org/browse/MDEV-20425) Implement Boolean debug build option debug\_assert
* Merge [Revision #1a3c365953](https://github.com/MariaDB/server/commit/1a3c365953) 2019-08-29 08:41:53 +0300 - Merge 10.2 into 10.3
* Merge [Revision #e41eb044f1](https://github.com/MariaDB/server/commit/e41eb044f1) 2019-08-28 10:18:41 +0300 - Merge 10.2 into 10.3
* [Revision #947b0b5722](https://github.com/MariaDB/server/commit/947b0b5722)\
  2019-08-23 17:43:55 +0300
  * Implement innodb\_evict\_tables\_on\_commit\_debug
* [Revision #b96e4424fb](https://github.com/MariaDB/server/commit/b96e4424fb)\
  2019-08-21 16:06:29 +0300
  * [MDEV-17613](https://jira.mariadb.org/browse/MDEV-17613) MIN/MAX Optimization (Select tables optimized away) does not work
* Merge [Revision #32ec5fb979](https://github.com/MariaDB/server/commit/32ec5fb979) 2019-08-21 15:23:45 +0300 - Merge 10.2 into 10.3
* [Revision #e8de75db88](https://github.com/MariaDB/server/commit/e8de75db88)\
  2019-08-21 11:37:40 +0300
  * [MDEV-19740](https://jira.mariadb.org/browse/MDEV-19740) Debug build of 10.3.15 FTBFS
* [Revision #888f685226](https://github.com/MariaDB/server/commit/888f685226)\
  2019-07-31 03:28:38 -0700
  * [MDEV-20210](https://jira.mariadb.org/browse/MDEV-20210) If you have an INVISIBLE VIRTUAL column, SHOW CREATE TABLE doesn't list it as INVISIBLE
* [Revision #c93f96e2ec](https://github.com/MariaDB/server/commit/c93f96e2ec)\
  2019-07-30 17:18:31 +0200
  * [MDEV-20185](https://jira.mariadb.org/browse/MDEV-20185): Windows: Use of uninitialized value $bpath in string eq
* [Revision #137d8ed3fe](https://github.com/MariaDB/server/commit/137d8ed3fe)\
  2019-07-30 13:45:13 +0200
  * [MDEV-18863](https://jira.mariadb.org/browse/MDEV-18863): Galera SST scripts can't read \[mysqldN] option groups
* [Revision #938925211a](https://github.com/MariaDB/server/commit/938925211a)\
  2019-08-19 19:49:45 +0300
  * [MDEV-19254](https://jira.mariadb.org/browse/MDEV-19254) Server crashes in maria\_status with partitioned table
* [Revision #6dd3f24090](https://github.com/MariaDB/server/commit/6dd3f24090)\
  2019-08-18 23:18:44 +0300
  * [MDEV-19740](https://jira.mariadb.org/browse/MDEV-19740) Debug build of 10.3.15 FTBFS
* [Revision #44150a770f](https://github.com/MariaDB/server/commit/44150a770f)\
  2019-08-18 13:18:09 +0300
  * Updated result for rocksdb tests after merge
* [Revision #6626b10a7a](https://github.com/MariaDB/server/commit/6626b10a7a)\
  2019-08-17 00:40:38 +0900
  * fix for a compiler warning (#1372)
* [Revision #1639873671](https://github.com/MariaDB/server/commit/1639873671)\
  2019-08-15 22:32:59 +0300
  * [MDEV-18154](https://jira.mariadb.org/browse/MDEV-18154) Deadlock and assertion upon no-op ALTER under LOCK TABLES
* Merge [Revision #395e1dcd17](https://github.com/MariaDB/server/commit/395e1dcd17) 2019-08-16 10:02:18 +0300 - Merge 10.2 into 10.3
* [Revision #130d9490c8](https://github.com/MariaDB/server/commit/130d9490c8)\
  2019-08-16 08:29:41 +0300
  * Silence GCC 9.2.1 -Warray-bounds
* Merge [Revision #d50fe4021e](https://github.com/MariaDB/server/commit/d50fe4021e) 2019-08-15 15:59:32 +0300 - Merge 10.2 into 10.3
* Merge [Revision #828191b6a0](https://github.com/MariaDB/server/commit/828191b6a0) 2019-08-15 14:09:53 +0530 - [MDEV-20348](https://jira.mariadb.org/browse/MDEV-20348): DROP TABLE IF EXISTS killed on master but was replicated
* [Revision #ae34d85beb](https://github.com/MariaDB/server/commit/ae34d85beb)\
  2019-08-12 15:16:33 +0300
  * [MDEV-20311](https://jira.mariadb.org/browse/MDEV-20311) row\_ins\_step accesses unitialized memory
* [Revision #841294cfaa](https://github.com/MariaDB/server/commit/841294cfaa)\
  2019-08-15 10:32:42 +0400
  * [MDEV-20351](https://jira.mariadb.org/browse/MDEV-20351) Window function BIT\_OR() OVER (..) return a wrong data type
* Merge [Revision #c23a5e0e5e](https://github.com/MariaDB/server/commit/c23a5e0e5e) 2019-08-14 19:16:08 +0300 - Merge 10.2 into 10.3
* [Revision #a20f6f9853](https://github.com/MariaDB/server/commit/a20f6f9853)\
  2019-08-14 15:52:08 +0300
  * [MDEV-20336](https://jira.mariadb.org/browse/MDEV-20336) Assertion bitmap\_is\_set(read\_partitions) upon SELECT FOR UPDATE from versioned table
* [Revision #39db116562](https://github.com/MariaDB/server/commit/39db116562)\
  2019-08-13 14:31:34 +0300
  * [MDEV-18862](https://jira.mariadb.org/browse/MDEV-18862) Unfortunate error message upon attempt to drop system versioning
* Merge [Revision #65d48b4a7b](https://github.com/MariaDB/server/commit/65d48b4a7b) 2019-08-13 19:28:51 +0300 - Merge 10.2 to 10.3
* [Revision #eedd6179c1](https://github.com/MariaDB/server/commit/eedd6179c1)\
  2019-08-13 14:54:24 +0300
  * [MDEV-20138](https://jira.mariadb.org/browse/MDEV-20138) innodb.trx\_id\_future fails on 10.3+
* [Revision #20c78a6d3e](https://github.com/MariaDB/server/commit/20c78a6d3e)\
  2019-08-13 13:54:59 +0400
  * Fixing `[MDEV-20303](https://jira.mariadb.org/browse/MDEV-20303) SPACE(-1) returns a wrong data type` compilation problem in Windows
* [Revision #98b24da038](https://github.com/MariaDB/server/commit/98b24da038)\
  2018-11-03 18:00:22 +0300
  * [MDEV-17609](https://jira.mariadb.org/browse/MDEV-17609) mysql client sets wrong application name for Readline library
* [Revision #22914ec793](https://github.com/MariaDB/server/commit/22914ec793)\
  2019-02-05 00:57:31 +0300
  * [MDEV-18154](https://jira.mariadb.org/browse/MDEV-18154) Deadlock and assertion upon no-op ALTER under LOCK TABLES
* [Revision #0b74c8832d](https://github.com/MariaDB/server/commit/0b74c8832d)\
  2019-04-11 10:04:34 +0300
  * [MDEV-19127](https://jira.mariadb.org/browse/MDEV-19127) Assertion \`row\_start\_field' failed in vers\_prepare\_keys upon ALTER TABLE
* [Revision #638e78853f](https://github.com/MariaDB/server/commit/638e78853f)\
  2019-03-20 20:45:54 +0300
  * [MDEV-18862](https://jira.mariadb.org/browse/MDEV-18862) Unfortunate error message upon attempt to drop system versioning
* [Revision #5851e668d7](https://github.com/MariaDB/server/commit/5851e668d7)\
  2019-05-27 15:03:15 +0300
  * [MDEV-19304](https://jira.mariadb.org/browse/MDEV-19304) Segfault in ALTER TABLE after UPDATE for SIMULTANEOUS\_ASSIGNMENT
* [Revision #98758b52b3](https://github.com/MariaDB/server/commit/98758b52b3)\
  2019-07-16 19:40:38 +0300
  * [MDEV-20068](https://jira.mariadb.org/browse/MDEV-20068) History partition rotation is not done under LOCK TABLES
* [Revision #cdbac54df0](https://github.com/MariaDB/server/commit/cdbac54df0)\
  2018-12-26 13:24:45 +0300
  * [MDEV-17613](https://jira.mariadb.org/browse/MDEV-17613) MIN/MAX Optimization (Select tables optimized away) does not work
* [Revision #43882e764d](https://github.com/MariaDB/server/commit/43882e764d)\
  2019-08-09 14:18:13 +0400
  * [MDEV-20303](https://jira.mariadb.org/browse/MDEV-20303) SPACE(-1) returns a wrong data type
* [Revision #2dac123515](https://github.com/MariaDB/server/commit/2dac123515)\
  2019-08-09 09:00:17 +0400
  * A cleanup for `[MDEV-20273](https://jira.mariadb.org/browse/MDEV-20273) Add class Item_sum_min_max` - removing duplicate code
* [Revision #c3d67c17c1](https://github.com/MariaDB/server/commit/c3d67c17c1)\
  2019-08-08 17:08:56 +0400
  * [MDEV-20292](https://jira.mariadb.org/browse/MDEV-20292) REPEAT(x,-1) returns a wrong data type
* [Revision #e555df648c](https://github.com/MariaDB/server/commit/e555df648c)\
  2019-08-08 13:47:50 +0400
  * [MDEV-20285](https://jira.mariadb.org/browse/MDEV-20285) Wrong result on INSERT..SELECT when converting from SIGNED to UNSIGNED
* [Revision #7fc86a73d8](https://github.com/MariaDB/server/commit/7fc86a73d8)\
  2019-08-07 22:44:54 +0400
  * [MDEV-20272](https://jira.mariadb.org/browse/MDEV-20272) PERCENTILE\_DISC() crashes on a temporal type input
* [Revision #d70dac2079](https://github.com/MariaDB/server/commit/d70dac2079)\
  2019-08-07 21:01:22 +0400
  * [MDEV-20278](https://jira.mariadb.org/browse/MDEV-20278) PERCENTILE\_DISC() returns a wrong data type
* [Revision #e978efd96b](https://github.com/MariaDB/server/commit/e978efd96b)\
  2019-08-07 14:13:44 +0400
  * [MDEV-20273](https://jira.mariadb.org/browse/MDEV-20273) Add class Item\_sum\_min\_max
* [Revision #a8def12e8a](https://github.com/MariaDB/server/commit/a8def12e8a)\
  2019-08-06 18:02:03 +0400
  * [MDEV-20263](https://jira.mariadb.org/browse/MDEV-20263) sql\_mode=ORACLE: BLOB(65535) should not translate to LONGBLOB
* [Revision #f36c0189b1](https://github.com/MariaDB/server/commit/f36c0189b1)\
  2019-08-06 14:37:08 +0300
  * [MDEV-17544](https://jira.mariadb.org/browse/MDEV-17544): No warning when trying to name a primary key constraint
* [Revision #4c4e379ba9](https://github.com/MariaDB/server/commit/4c4e379ba9)\
  2019-08-05 16:03:33 +0400
  * [MDEV-20101](https://jira.mariadb.org/browse/MDEV-20101) Assertion failure on select @@global.'m2'.replicate\_ignore\_table;
* [Revision #6b48bdf269](https://github.com/MariaDB/server/commit/6b48bdf269)\
  2019-08-05 15:25:31 +0400
  * [MDEV-18456](https://jira.mariadb.org/browse/MDEV-18456) Assertion \`item->maybe\_null' failed in Type\_handler\_temporal\_result::make\_sort\_key
* [Revision #e1e142e7fc](https://github.com/MariaDB/server/commit/e1e142e7fc)\
  2019-07-31 09:58:59 -0400
  * bump the VERSION
* [Revision #fde7eb9ab2](https://github.com/MariaDB/server/commit/fde7eb9ab2)\
  2019-07-31 02:51:20 -0700
  * Fix README
* [Revision #c6efbc543d](https://github.com/MariaDB/server/commit/c6efbc543d)\
  2019-07-30 21:57:48 +0400
  * [MDEV-17544](https://jira.mariadb.org/browse/MDEV-17544) No warning when trying to name a primary key constraint.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
