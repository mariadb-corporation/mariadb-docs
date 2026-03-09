# MariaDB 10.1.39 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.39)[Release Notes](../../old-releases/10.1/10.1.39.md)[Changelog](mariadb-10139-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 2 May 2019

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.39.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 5.5.64](../changelogs-mariadb-55-series/mariadb-5564-changelog.md)
* [Revision #e9da78ee92](https://github.com/MariaDB/server/commit/e9da78ee92)\
  2019-04-30 23:58:14 +0300
  * Updated list of unstable tests for 10.1.39 release
* [Revision #5b035c8456](https://github.com/MariaDB/server/commit/5b035c8456)\
  2019-04-30 11:35:52 +0200
  * [MDEV-14572](https://jira.mariadb.org/browse/MDEV-14572): Assertion \`! is\_set()' failed in Diagnostics\_area::set\_eof\_status upon EXPLAIN UPDATE in PS
* [Revision #a8793a2c02](https://github.com/MariaDB/server/commit/a8793a2c02)\
  2019-04-29 22:57:21 +0200
  * [MDEV-19243](https://jira.mariadb.org/browse/MDEV-19243) Fix timezone handling on Windows to report standard timezone names
* [Revision #ba9f8776c2](https://github.com/MariaDB/server/commit/ba9f8776c2)\
  2019-04-30 11:10:03 +0400
  * Tests for [MDEV-19359](https://jira.mariadb.org/browse/MDEV-19359) ASAN heap-use-after-free in copy\_if\_not\_alloced / make\_sortkey
* [Revision #5fb6444a37](https://github.com/MariaDB/server/commit/5fb6444a37)\
  2019-04-30 10:53:59 +0400
  * [MDEV-18738](https://jira.mariadb.org/browse/MDEV-18738) ASAN heap-use-after-free in copy\_if\_not\_alloced / copy\_fields
* [Revision #021c7216c0](https://github.com/MariaDB/server/commit/021c7216c0)\
  2019-04-29 10:36:57 +0400
  * Tests for [MDEV-11895](https://jira.mariadb.org/browse/MDEV-11895) NO\_ZERO\_DATE affects timestamp values without any warnings
* [Revision #e8778f1c7c](https://github.com/MariaDB/server/commit/e8778f1c7c)\
  2019-04-25 18:51:28 +0200
  * [MDEV-19265](https://jira.mariadb.org/browse/MDEV-19265) Server should throw warning if event is created and event\_scheduler = OFF
* [Revision #7590861779](https://github.com/MariaDB/server/commit/7590861779)\
  2019-04-24 22:13:12 +0100
  * [MDEV-19276](https://jira.mariadb.org/browse/MDEV-19276) during connect, write error log warning for ER\_DBACCESS\_DENIED\_ERROR, if log\_warnings > 1.
* [Revision #6c9a6bad4f](https://github.com/MariaDB/server/commit/6c9a6bad4f)\
  2019-04-24 10:52:06 +0100
  * [MDEV-19262](https://jira.mariadb.org/browse/MDEV-19262) Server error message is unclear if event is created and event\_scheduler = DISABLED
* [Revision #e116f11f0a](https://github.com/MariaDB/server/commit/e116f11f0a)\
  2019-04-24 11:15:08 +0200
  * [MDEV-18131](https://jira.mariadb.org/browse/MDEV-18131) MariaDB does not verify IP addresses from subject alternative names
* [Revision #eb9b03ab48](https://github.com/MariaDB/server/commit/eb9b03ab48)\
  2019-04-28 10:53:07 +0400
  * [MDEV-13335](https://jira.mariadb.org/browse/MDEV-13335) UTF8 escape wildcard LIKE match has different behavior in different collations
* [Revision #d3534d5b45](https://github.com/MariaDB/server/commit/d3534d5b45)\
  2019-04-27 21:31:04 -0700
  * [MDEV-19351](https://jira.mariadb.org/browse/MDEV-19351) statistics\_for\_command\_is\_needed: Conditional jump or move depends on uninitialised value
* [Revision #d88dfd8732](https://github.com/MariaDB/server/commit/d88dfd8732)\
  2019-04-27 19:38:39 +0200
  * [MDEV-19350](https://jira.mariadb.org/browse/MDEV-19350) Server crashes in delete\_tree\_element / ... / Item\_func\_group\_concat::repack\_tree
* [Revision #3fe38574fb](https://github.com/MariaDB/server/commit/3fe38574fb)\
  2019-04-27 04:49:04 +0200
  * gis2 fails in embedded
* [Revision #0d5aabd632](https://github.com/MariaDB/server/commit/0d5aabd632)\
  2019-04-25 18:18:26 +0530
  * [MDEV-19334](https://jira.mariadb.org/browse/MDEV-19334): bool is\_eits\_usable(Field\*): Assertion \`field->table->stats\_is\_read' failed.
* [Revision #f239fd5034](https://github.com/MariaDB/server/commit/f239fd5034)\
  2019-04-27 08:44:29 +0400
  * [MDEV-11015](https://jira.mariadb.org/browse/MDEV-11015) Assertion failed: precision > 0 in decimal\_bin\_size upon SELECT with DISTINCT, CAST and other functions
* [Revision #5fe0087a72](https://github.com/MariaDB/server/commit/5fe0087a72)\
  2019-04-26 19:52:34 +0200
  * CONNECT compilation failure
* Merge [Revision #f22ed2779f](https://github.com/MariaDB/server/commit/f22ed2779f) 2019-04-26 18:26:23 +0200 - Merge branch 'merge-tokudb-5.6' into 10.1
* [Revision #33d8a28367](https://github.com/MariaDB/server/commit/33d8a28367)\
  2019-04-26 17:02:15 +0200
  * 5.6.43-84.3
* [Revision #e049f92392](https://github.com/MariaDB/server/commit/e049f92392)\
  2019-01-27 15:16:15 +0100
  * Squashed commit of connect/10.0:
* Merge [Revision #52eb4f172c](https://github.com/MariaDB/server/commit/52eb4f172c) 2019-04-26 16:11:55 +0200 - Merge branch 'merge-pcre' into 10.1
* [Revision #879f7e85aa](https://github.com/MariaDB/server/commit/879f7e85aa)\
  2019-04-26 12:25:09 +0200
  * 8.43
* Merge [Revision #1389c94b3c](https://github.com/MariaDB/server/commit/1389c94b3c) 2019-04-26 16:41:59 +0300 - Merge 5.5 into 10.1
* Merge [Revision #2ce52790ff](https://github.com/MariaDB/server/commit/2ce52790ff) 2019-04-26 14:02:37 +0200 - Merge branch '5.5' into 10.1
* Merge [Revision #caa9023c9e](https://github.com/MariaDB/server/commit/caa9023c9e) 2019-04-25 14:15:54 +0300 - [MDEV-19331](https://jira.mariadb.org/browse/MDEV-19331) Merge new release of InnoDB 5.6.44 to 10.1
* [Revision #1cd31bc132](https://github.com/MariaDB/server/commit/1cd31bc132)\
  2019-04-25 14:04:44 +0300
  * Bug#28573894 ALTER PARTITIONED TABLE ADD AUTO\_INCREMENT DIFF RESULT DEPENDING ON ALGORITHM
* [Revision #9e7bcb05d4](https://github.com/MariaDB/server/commit/9e7bcb05d4)\
  2019-04-25 14:01:55 +0300
  * Clean up ib\_sequence::m\_max\_value
* [Revision #ac97ad4eab](https://github.com/MariaDB/server/commit/ac97ad4eab)\
  2019-04-25 13:16:44 +0300
  * Bug#19811005: Add a simple test case
* [Revision #3ae2198483](https://github.com/MariaDB/server/commit/3ae2198483)\
  2019-01-30 23:09:57 +0530
  * Bug #19811005 ALTER TABLE ADD INDEX DOES NOT UPDATE INDEX\_LENGTH IN I\_S TABLES
* [Revision #bb17094be4](https://github.com/MariaDB/server/commit/bb17094be4)\
  2019-04-25 09:50:01 +0400
  * [MDEV-18452](https://jira.mariadb.org/browse/MDEV-18452) ASAN unknown-crash in Field::set\_default upon SET bit\_column = DEFAULT
* Merge [Revision #ecea90871e](https://github.com/MariaDB/server/commit/ecea90871e) 2019-04-25 10:43:55 +0300 - 5.6.43-84.3
* [Revision #83d8c38dd7](https://github.com/MariaDB/server/commit/83d8c38dd7)\
  2018-11-01 10:33:22 +0100
  * PS-4989: Fixing innodb\_track\_changed\_pages debug validation
* [Revision #979cad2291](https://github.com/MariaDB/server/commit/979cad2291)\
  2017-06-21 16:07:54 +0200
  * [MDEV-9531](https://jira.mariadb.org/browse/MDEV-9531) GROUP\_CONCAT with ORDER BY inside takes a lot of memory while it's executed
* [Revision #e91fd8783a](https://github.com/MariaDB/server/commit/e91fd8783a)\
  2017-06-21 16:07:29 +0200
  * don't cast random items to Item\_result\_field\*
* [Revision #d3b2228fd8](https://github.com/MariaDB/server/commit/d3b2228fd8)\
  2019-04-20 12:13:42 +0200
  * cleanup: cosmetic fixes
* [Revision #6cc19078ba](https://github.com/MariaDB/server/commit/6cc19078ba)\
  2017-06-21 14:36:29 +0200
  * cleanup: make TREE copyable
* [Revision #bed1ede197](https://github.com/MariaDB/server/commit/bed1ede197)\
  2019-04-12 01:21:11 -0700
  * [MDEV-19015](https://jira.mariadb.org/browse/MDEV-19015): mysql\_plugin doesn't read all server option groups
* [Revision #9ca3571cb8](https://github.com/MariaDB/server/commit/9ca3571cb8)\
  2019-04-18 11:53:36 +0200
  * [MDEV-18686](https://jira.mariadb.org/browse/MDEV-18686) Add option to PAM authentication plugin to allow case insensitive username matching
* [Revision #ed866e9301](https://github.com/MariaDB/server/commit/ed866e9301)\
  2019-04-18 10:14:40 +0200
  * [MDEV-19182](https://jira.mariadb.org/browse/MDEV-19182) mysqldump not always handling SHOW CREATE TRIGGER failures correctly
* [Revision #3db6de33b2](https://github.com/MariaDB/server/commit/3db6de33b2)\
  2019-04-17 14:53:30 +0200
  * [MDEV-17640](https://jira.mariadb.org/browse/MDEV-17640) UMASK\_DIR configuration for mysql\_install\_db is not applied to mysql database
* [Revision #17088dd941](https://github.com/MariaDB/server/commit/17088dd941)\
  2019-04-17 13:42:32 +0200
  * [MDEV-19024](https://jira.mariadb.org/browse/MDEV-19024) sys\_vars.transaction\_prealloc\_size\_bug27322 fails in buildbot with wrong result
* [Revision #2f9cd06da4](https://github.com/MariaDB/server/commit/2f9cd06da4)\
  2019-04-17 13:20:48 +0200
  * [MDEV-18362](https://jira.mariadb.org/browse/MDEV-18362) EPOCH=1 needs to be set for Ubuntu 18.10 cosmic builds
* [Revision #3885099563](https://github.com/MariaDB/server/commit/3885099563)\
  2019-04-10 11:55:49 +0300
  * tests for AddGeometryColumn and DropGeometryColumn
* [Revision #2a6f00ed6a](https://github.com/MariaDB/server/commit/2a6f00ed6a)\
  2019-04-10 10:08:42 +0300
  * use the correct SQL SECURITY type for OpenGIS stored procedures
* [Revision #932e29d4ad](https://github.com/MariaDB/server/commit/932e29d4ad)\
  2019-03-22 01:55:35 +0100
  * don't run SysV scripts in scriptlets if systemd is used
* Merge [Revision #bfb0726fc2](https://github.com/MariaDB/server/commit/bfb0726fc2) 2019-04-24 12:03:11 +0300 - Merge 5.5 into 10.1
* [Revision #9dcfd6be94](https://github.com/MariaDB/server/commit/9dcfd6be94)\
  2019-04-23 09:11:42 +0400
  * [MDEV-9465](https://jira.mariadb.org/browse/MDEV-9465) The constructor StringBuffer(const char \*str, size\_t length, const CHARSET\_INFO \*cs) looks suspicious
* [Revision #279a907fd0](https://github.com/MariaDB/server/commit/279a907fd0)\
  2019-04-22 17:10:42 -0700
  * [MDEV-17605](https://jira.mariadb.org/browse/MDEV-17605) Statistics for InnoDB table is wrong if persistent statistics is used
* [Revision #a4f7d85932](https://github.com/MariaDB/server/commit/a4f7d85932)\
  2019-04-22 23:28:44 +0400
  * [MDEV-18920](https://jira.mariadb.org/browse/MDEV-18920) Prepared statements with st\_convexhull hang and eat 100% cpu.
* [Revision #6c5e4c9bc0](https://github.com/MariaDB/server/commit/6c5e4c9bc0)\
  2019-04-22 15:05:11 +0400
  * Fixing -Werror=format-overflow errors (found by gcc-8.3.1)
* [Revision #279b50b4eb](https://github.com/MariaDB/server/commit/279b50b4eb)\
  2019-04-22 14:01:58 +0400
  * [MDEV-14041](https://jira.mariadb.org/browse/MDEV-14041) Server crashes in String::length on queries with functions and ROLLUP
* [Revision #f4b2740018](https://github.com/MariaDB/server/commit/f4b2740018)\
  2019-04-19 21:04:44 +0400
  * [MDEV-17299](https://jira.mariadb.org/browse/MDEV-17299) Assertion \`maybe\_null' failed in make\_sortkey
* [Revision #056b6fe1d5](https://github.com/MariaDB/server/commit/056b6fe1d5)\
  2019-04-18 23:12:43 +0300
  * [MDEV-17297](https://jira.mariadb.org/browse/MDEV-17297): stats.records=0 for a table of Archive engine when it has rows, when we run ANALYZE command
* [Revision #0bb924e18c](https://github.com/MariaDB/server/commit/0bb924e18c)\
  2019-04-17 20:21:11 +0400
  * [MDEV-17830](https://jira.mariadb.org/browse/MDEV-17830) Server crashes in Item\_null\_result::field\_type upon SELECT with CHARSET(date) and ROLLUP
* [Revision #409dddf695](https://github.com/MariaDB/server/commit/409dddf695)\
  2019-04-11 13:05:01 +0530
  * [MDEV-18300](https://jira.mariadb.org/browse/MDEV-18300): ASAN error in Field\_blob::get\_key\_image upon UPDATE with subquery
* [Revision #812ac2bb85](https://github.com/MariaDB/server/commit/812ac2bb85)\
  2019-04-04 22:19:56 +0300
  * [MDEV-19172](https://jira.mariadb.org/browse/MDEV-19172) Reorder fields in PFS\_events and PFS\_events\_waits to speed up memcpy()
* Merge [Revision #3b9d6bf7e4](https://github.com/MariaDB/server/commit/3b9d6bf7e4) 2019-04-04 15:36:07 +0100 - Merge branch '5.5' into 10.1
* [Revision #37bf7b195c](https://github.com/MariaDB/server/commit/37bf7b195c)\
  2019-04-04 15:27:16 +0100
  * [MDEV-17610](https://jira.mariadb.org/browse/MDEV-17610) Unexpected connection abort after certain operations from within stored procedure
* [Revision #6e71dde8b8](https://github.com/MariaDB/server/commit/6e71dde8b8)\
  2019-04-04 15:33:20 +0200
  * [MDEV-19169](https://jira.mariadb.org/browse/MDEV-19169): Add --defaults-group-suffix option to mysql\_install\_db man page
* [Revision #71a2e6a3c6](https://github.com/MariaDB/server/commit/71a2e6a3c6)\
  2019-04-01 19:42:26 +0300
  * index\_merge\_innodb did sometimes give wrong results
* [Revision #6a9b216301](https://github.com/MariaDB/server/commit/6a9b216301)\
  2019-04-03 19:50:51 +0300
  * Fix clang -Wunused-private-field
* [Revision #1f3bcff1f2](https://github.com/MariaDB/server/commit/1f3bcff1f2)\
  2019-04-03 19:46:34 +0300
  * Remove unused declarations
* [Revision #fa14784301](https://github.com/MariaDB/server/commit/fa14784301)\
  2019-04-03 19:21:54 +0300
  * Fix more -Wnonnull-compare
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
* [Revision #b88f378648](https://github.com/MariaDB/server/commit/b88f378648)\
  2019-04-02 08:48:54 +0300
  * Omit the definition of unused function yyset\_extra()
* [Revision #619d22dde5](https://github.com/MariaDB/server/commit/619d22dde5)\
  2019-04-01 13:03:18 +0300
  * Rebuild the InnoDB lexical analyzers with flex 2.6.4
* [Revision #23eeecd68f](https://github.com/MariaDB/server/commit/23eeecd68f)\
  2019-04-01 10:32:03 +0300
  * [MDEV-19111](https://jira.mariadb.org/browse/MDEV-19111) Unused field INFORMATION\_SCHEMA.INNODB\_TABLESPACES\_SCRUBBING.ROTATING\_OR\_FLUSHING
* [Revision #d0116e10a5](https://github.com/MariaDB/server/commit/d0116e10a5)\
  2019-03-28 12:27:06 +0200
  * Revert [MDEV-18464](https://jira.mariadb.org/browse/MDEV-18464) and [MDEV-12009](https://jira.mariadb.org/browse/MDEV-12009)
* [Revision #81d71ee6b2](https://github.com/MariaDB/server/commit/81d71ee6b2)\
  2019-02-05 15:41:53 +0200
  * [MDEV-12009](https://jira.mariadb.org/browse/MDEV-12009): Allow to force kill user threads/query which are flagged as high priority by Galera
* [Revision #21b2fada7a](https://github.com/MariaDB/server/commit/21b2fada7a)\
  2019-03-27 09:28:49 +0200
  * [MDEV-18464](https://jira.mariadb.org/browse/MDEV-18464): Port kill\_one\_trx fixes from 10.4 to 10.1
* [Revision #deff3f7572](https://github.com/MariaDB/server/commit/deff3f7572)\
  2019-03-22 19:28:59 +0100
  * [MDEV-18466](https://jira.mariadb.org/browse/MDEV-18466) Unsafe to log updates on tables referenced by foreign keys with triggers in statement format
* [Revision #d8084116b5](https://github.com/MariaDB/server/commit/d8084116b5)\
  2019-03-16 19:44:40 +0100
  * [MDEV-7066](https://jira.mariadb.org/browse/MDEV-7066) No Source RPMs ... (and so no "yum-builddep MariaDB-server" either)
* [Revision #b12f14965d](https://github.com/MariaDB/server/commit/b12f14965d)\
  2019-03-16 19:37:44 +0100
  * [MDEV-7066](https://jira.mariadb.org/browse/MDEV-7066) No Source RPMs ... (and so no "yum-builddep MariaDB-server" either)
* [Revision #ecc2711328](https://github.com/MariaDB/server/commit/ecc2711328)\
  2019-03-16 19:33:07 +0100
  * [MDEV-7066](https://jira.mariadb.org/browse/MDEV-7066) No Source RPMs ... (and so no "yum-builddep MariaDB-server" either)
* [Revision #86e80f944f](https://github.com/MariaDB/server/commit/86e80f944f)\
  2019-03-16 19:30:51 +0100
  * cmake: don't do fake rpm Provides
* [Revision #39cea72e7b](https://github.com/MariaDB/server/commit/39cea72e7b)\
  2019-03-17 15:05:56 +0100
  * cmake: fix cpack\_source\_ignore\_files
* [Revision #6417297180](https://github.com/MariaDB/server/commit/6417297180)\
  2019-03-16 19:27:51 +0100
  * cmake: remove workarounds for cmake bugs #13248 and #12864
* [Revision #f97d879bf8](https://github.com/MariaDB/server/commit/f97d879bf8)\
  2019-03-16 19:24:49 +0100
  * cmake: re-enable -Werror in the maintainer mode
* Merge [Revision #1a4746e128](https://github.com/MariaDB/server/commit/1a4746e128) 2019-03-27 19:35:03 +0100 - Merge branch '5.5' into 10.1
* [Revision #9a8b8ea66b](https://github.com/MariaDB/server/commit/9a8b8ea66b)\
  2019-03-27 14:37:14 +0100
  * [MDEV-19060](https://jira.mariadb.org/browse/MDEV-19060) : mariadb-backup continues, despite failing to open a tablespace
* Merge [Revision #a6585d5ce9](https://github.com/MariaDB/server/commit/a6585d5ce9) 2019-03-27 11:56:08 +0200 - Merge 10.0 into 10.1
* [Revision #828cc2ba7c](https://github.com/MariaDB/server/commit/828cc2ba7c)\
  2019-03-27 11:34:53 +0200
  * [MDEV-18417](https://jira.mariadb.org/browse/MDEV-18417)/[MDEV-18656](https://jira.mariadb.org/browse/MDEV-18656)/[MDEV-18417](https://jira.mariadb.org/browse/MDEV-18417): Work around compiler ASAN bug
* Merge [Revision #1933cf98e8](https://github.com/MariaDB/server/commit/1933cf98e8) 2019-03-26 14:13:46 +0200 - Merge 5.5 into 10.0
* [Revision #762419a573](https://github.com/MariaDB/server/commit/762419a573)\
  2019-03-26 17:19:05 +0200
  * Fixup for [MDEV-18968](https://jira.mariadb.org/browse/MDEV-18968)
* [Revision #f2c1c9590c](https://github.com/MariaDB/server/commit/f2c1c9590c)\
  2019-03-26 14:57:33 +0200
  * Fix cmake -DENABLED\_PROFILING=OFF
* Merge [Revision #42fd537244](https://github.com/MariaDB/server/commit/42fd537244) 2019-03-26 13:51:40 +0200 - Merge 10.0 into 10.1
* [Revision #137812c88a](https://github.com/MariaDB/server/commit/137812c88a)\
  2018-11-28 15:25:53 +0100
  * Fix USE\_AFTER\_FREE (CWE-416)
* [Revision #9d2d80aace](https://github.com/MariaDB/server/commit/9d2d80aace)\
  2019-02-07 03:29:12 -0500
  * Update sql\_parse.cc
* [Revision #065ba53ccb](https://github.com/MariaDB/server/commit/065ba53ccb)\
  2019-03-26 13:51:15 +0200
  * [MDEV-12711](https://jira.mariadb.org/browse/MDEV-12711) mariadb-backup --backup is refused for multi-file system tablespace
* [Revision #6fbbb0853e](https://github.com/MariaDB/server/commit/6fbbb0853e)\
  2019-03-26 11:37:18 +0400
  * [MDEV-18968](https://jira.mariadb.org/browse/MDEV-18968) Both (WHERE 0.1) and (WHERE NOT 0.1) return empty set
* [Revision #ed643f4bb3](https://github.com/MariaDB/server/commit/ed643f4bb3)\
  2018-11-29 15:59:26 +0100
  * Fix resource leak
* [Revision #f704361cd6](https://github.com/MariaDB/server/commit/f704361cd6)\
  2019-03-22 15:48:49 +0400
  * Backporting slow log simulation logic details from 10.2 to 10.1
* [Revision #9c9bf9642e](https://github.com/MariaDB/server/commit/9c9bf9642e)\
  2018-12-04 14:45:27 +0100
  * Fix resource leak
* [Revision #89e390b7ce](https://github.com/MariaDB/server/commit/89e390b7ce)\
  2018-11-29 16:08:55 +0100
  * Fix resource leak
* [Revision #9ff713d33a](https://github.com/MariaDB/server/commit/9ff713d33a)\
  2018-11-29 15:28:03 +0100
  * Fix resource leak
* [Revision #8be02be08b](https://github.com/MariaDB/server/commit/8be02be08b)\
  2018-11-28 14:16:52 +0100
  * Fix USE\_AFTER\_FREE (CWE-672)
* Merge [Revision #8c493a910f](https://github.com/MariaDB/server/commit/8c493a910f) 2019-03-21 21:06:01 +0200 - Merge 10.0 into 10.1
* Merge [Revision #925b503058](https://github.com/MariaDB/server/commit/925b503058) 2019-03-21 10:34:00 +0200 - Merge 5.5 into 10.0
* [Revision #5d454181a8](https://github.com/MariaDB/server/commit/5d454181a8)\
  2019-03-21 10:29:59 +0200
  * [MDEV-6262](https://jira.mariadb.org/browse/MDEV-6262) follow-up: Ensure NUL termination on strncpy()
* [Revision #e9c494c843](https://github.com/MariaDB/server/commit/e9c494c843)\
  2019-03-21 08:48:44 +0400
  * Fixing a failure in tests for "[MDEV-18892](https://jira.mariadb.org/browse/MDEV-18892) Regression in slow log and admin statements"
* [Revision #ef81d2ea64](https://github.com/MariaDB/server/commit/ef81d2ea64)\
  2019-03-19 22:14:37 +0400
  * Fixing "mtr func\_math" failure in the test for [MDEV-17643](https://jira.mariadb.org/browse/MDEV-17643)
* [Revision #3b98c65c4e](https://github.com/MariaDB/server/commit/3b98c65c4e)\
  2019-03-18 15:33:59 +0400
  * [MDEV-18881](https://jira.mariadb.org/browse/MDEV-18881) Assertion \`0' failed in make\_sortkey upon SELECT with GROUP BY after LOAD DATA
* [Revision #6c08174e36](https://github.com/MariaDB/server/commit/6c08174e36)\
  2019-03-13 15:33:21 +0200
  * [MDEV-18908](https://jira.mariadb.org/browse/MDEV-18908): Remove galera and wsrep suites from default run suites in mtr
* [Revision #cd805a5f1c](https://github.com/MariaDB/server/commit/cd805a5f1c)\
  2019-03-15 11:39:52 +0100
  * Cleanup - remove unused variables and functions after [MDEV-18917](https://jira.mariadb.org/browse/MDEV-18917)
* [Revision #b6dc47a0f7](https://github.com/MariaDB/server/commit/b6dc47a0f7)\
  2019-03-15 14:11:30 +0400
  * [MDEV-17643](https://jira.mariadb.org/browse/MDEV-17643) Assertion \`nr >= 0.0' failed in Item\_sum\_std::val\_real()
* [Revision #34db9958e2](https://github.com/MariaDB/server/commit/34db9958e2)\
  2019-03-15 12:09:46 +0200
  * [MDEV-18936](https://jira.mariadb.org/browse/MDEV-18936) Purge thread fails to exit on shutdown
* [Revision #396cf60ac0](https://github.com/MariaDB/server/commit/396cf60ac0)\
  2019-03-14 16:59:27 +0100
  * [MDEV-18917](https://jira.mariadb.org/browse/MDEV-18917) Don't create xtrabackup\_binlog\_pos\_innodb with mariadb-backup
* [Revision #7ad355dde7](https://github.com/MariaDB/server/commit/7ad355dde7)\
  2019-03-15 09:44:53 +0200
  * [MDEV-18934](https://jira.mariadb.org/browse/MDEV-18934): Document missing mysqldumpslow sort options
* [Revision #78c2499282](https://github.com/MariaDB/server/commit/78c2499282)\
  2019-03-15 11:36:41 +0400
  * [MDEV-16958](https://jira.mariadb.org/browse/MDEV-16958) Assertion \`field\_length < 5' failed in Field\_year::val\_str or data corruption upon SELECT with UNION and aggregate functions
* [Revision #3d2d060b62](https://github.com/MariaDB/server/commit/3d2d060b62)\
  2019-03-12 16:27:19 +0100
  * fix gcc 8 compiler warnings
* [Revision #ddfa722a03](https://github.com/MariaDB/server/commit/ddfa722a03)\
  2019-03-14 14:40:33 +0400
  * [MDEV-18626](https://jira.mariadb.org/browse/MDEV-18626) ASAN stack-buffer-overflow in int10\_to\_str / make\_date\_time upon DATE\_FORMAT
* [Revision #49c49e630b](https://github.com/MariaDB/server/commit/49c49e630b)\
  2019-03-14 10:14:37 +0400
  * Tests for [MDEV-18667](https://jira.mariadb.org/browse/MDEV-18667) ASAN heap-use-after-free in make\_date\_time / Arg\_comparator::compare\_string / Item\_func\_nullif::compare
* [Revision #cb66cdc6f8](https://github.com/MariaDB/server/commit/cb66cdc6f8)\
  2019-03-14 10:05:38 +0400
  * [MDEV-14926](https://jira.mariadb.org/browse/MDEV-14926) AddressSanitizer: heap-use-after-free in make\_date\_time on weird combination of functions
* [Revision #d7a38eaf1a](https://github.com/MariaDB/server/commit/d7a38eaf1a)\
  2019-03-13 15:38:33 +0400
  * [MDEV-18907](https://jira.mariadb.org/browse/MDEV-18907) Slow log: RENAME TABLE is not "admin", while ALTER TABLE..RENAME is
* [Revision #691c306953](https://github.com/MariaDB/server/commit/691c306953)\
  2019-03-13 11:38:09 +0200
  * [MDEV-14033](https://jira.mariadb.org/browse/MDEV-14033): wsrep\_on=off + binlog = mixed on [MariaDB 10.2.9](../../old-releases/10.2/10.2.9.md)
* [Revision #90ce95de4b](https://github.com/MariaDB/server/commit/90ce95de4b)\
  2019-03-12 18:46:37 +0400
  * Tests for [MDEV-18892](https://jira.mariadb.org/browse/MDEV-18892) Regression in slow log and admin statements
* [Revision #3b2a568589](https://github.com/MariaDB/server/commit/3b2a568589)\
  2019-03-12 11:45:59 +0200
  * Test cleanups.
* [Revision #a62e9a83c0](https://github.com/MariaDB/server/commit/a62e9a83c0)\
  2019-03-10 23:59:50 +0100
  * [MDEV-15945](https://jira.mariadb.org/browse/MDEV-15945) --ps-protocol does not test some queries
* [Revision #22f1cf9292](https://github.com/MariaDB/server/commit/22f1cf9292)\
  2018-11-11 14:20:37 +0100
  * cleanup: misc
* [Revision #dda2e940fb](https://github.com/MariaDB/server/commit/dda2e940fb)\
  2019-03-11 16:45:38 +0100
  * pass the slow logging information in thd->query\_plan\_flags
* [Revision #bc8ae50e7c](https://github.com/MariaDB/server/commit/bc8ae50e7c)\
  2019-03-07 11:30:06 +0100
  * Fix of prepared CREATE VIEW with global ORDER/GROUP
* [Revision #83123412f0](https://github.com/MariaDB/server/commit/83123412f0)\
  2018-04-18 19:34:12 +0200
  * [MDEV-11975](https://jira.mariadb.org/browse/MDEV-11975): SQLCOM\_PREPARE of EXPLAIN & ANALYZE statement do not return correct metadata info
* [Revision #01c49e66b5](https://github.com/MariaDB/server/commit/01c49e66b5)\
  2017-02-02 12:09:49 +0100
  * [MDEV-11966](https://jira.mariadb.org/browse/MDEV-11966): Impossible to execute prepared ANALYZE SELECT
* [Revision #32de60bb2e](https://github.com/MariaDB/server/commit/32de60bb2e)\
  2019-03-12 12:55:38 +0200
  * [MDEV-18749](https://jira.mariadb.org/browse/MDEV-18749): Fix GCC -flifetime-dse
* Merge [Revision #ea52ecbc10](https://github.com/MariaDB/server/commit/ea52ecbc10) 2019-03-11 22:50:24 +0400 - Merge remote-tracking branch 'origin/10.0' into 10.1
* [Revision #149b754768](https://github.com/MariaDB/server/commit/149b754768)\
  2019-03-07 13:43:53 +0400
  * [MDEV-17595](https://jira.mariadb.org/browse/MDEV-17595) - ALTER TABLE ADD FOREIGN KEY crash
* [Revision #2a2ab121b0](https://github.com/MariaDB/server/commit/2a2ab121b0)\
  2019-01-29 14:45:51 +0300
  * [MDEV-17703](https://jira.mariadb.org/browse/MDEV-17703) Add WITH\_UBSAN switch to CMake similar to WITH\_ASAN
* [Revision #0415021840](https://github.com/MariaDB/server/commit/0415021840)\
  2019-03-11 08:49:06 +0200
  * Clean up mysql-test/suite/galera/disabled.def again
* [Revision #b31d025c97](https://github.com/MariaDB/server/commit/b31d025c97)\
  2019-03-08 10:13:14 +0200
  * Decrease the time required to run test by removing unnecessary sleeps.
* [Revision #9fb84a166a](https://github.com/MariaDB/server/commit/9fb84a166a)\
  2019-03-07 08:06:50 +0200
  * remove WSREP\_SST\_OPT\_SUFFIX\_VALUE, checking \[mysqld] is covered in the parse\_cnf --mysqld case also in wsrep\_sst\_xtrabackup-v2
* [Revision #a05ca1a99a](https://github.com/MariaDB/server/commit/a05ca1a99a)\
  2019-03-06 16:41:40 +0200
  * Galera 3 versions of the result files recorded.
* [Revision #e8541c7565](https://github.com/MariaDB/server/commit/e8541c7565)\
  2019-03-05 15:29:24 +1100
  * galera: test cases for non \[mysqld] section for configuration
* [Revision #85a18526bc](https://github.com/MariaDB/server/commit/85a18526bc)\
  2019-03-05 14:01:02 +1100
  * wsrep\_sst: remove WSREP\_SST\_OPT\_SUFFIX\_VALUE, checking \[mysqld] is covered in the parse\_cnf --mysqld case
* [Revision #0957d25781](https://github.com/MariaDB/server/commit/0957d25781)\
  2019-03-06 13:33:37 +0200
  * [MDEV-18830](https://jira.mariadb.org/browse/MDEV-18830): Port SST fixes from 10.4 to 10.1
* [Revision #6567636b09](https://github.com/MariaDB/server/commit/6567636b09)\
  2019-03-08 16:33:23 +0200
  * Disable regularly failing Galera tests
* [Revision #d038806dfe](https://github.com/MariaDB/server/commit/d038806dfe)\
  2019-03-08 16:00:08 +0530
  * [MDEV-18855](https://jira.mariadb.org/browse/MDEV-18855) mariadb-backup should fetch innodb\_compression\_level from running server
* [Revision #e3adf96aeb](https://github.com/MariaDB/server/commit/e3adf96aeb)\
  2019-03-07 15:35:55 +0200
  * [MDEV-13818](https://jira.mariadb.org/browse/MDEV-13818) CREATE INDEX leaks memory if running out of undo log space
* [Revision #1a5028f430](https://github.com/MariaDB/server/commit/1a5028f430)\
  2019-03-07 14:31:54 +0200
  * Fix the WITH\_ASAN clang build of dynamic plugins
* Merge [Revision #4c0f43f45a](https://github.com/MariaDB/server/commit/4c0f43f45a) 2019-03-07 12:27:42 +0200 - Merge 10.0 into 10.1
* Merge [Revision #0a0eed8016](https://github.com/MariaDB/server/commit/0a0eed8016) 2019-03-07 12:04:22 +0200 - Merge 5.5 into 10.0
* [Revision #84645366c4](https://github.com/MariaDB/server/commit/84645366c4)\
  2019-03-05 20:19:50 +0100
  * ASAN loves stack, give it some
* [Revision #5ce6fb59a0](https://github.com/MariaDB/server/commit/5ce6fb59a0)\
  2019-03-05 22:40:55 +0100
  * disable LeakSanitizer for unit.dbug test
* [Revision #26f0d72a3f](https://github.com/MariaDB/server/commit/26f0d72a3f)\
  2019-03-06 17:08:03 +0400
  * A cleanup for [MDEV-18333](https://jira.mariadb.org/browse/MDEV-18333) Slow\_queries count doesn't increase when slow\_query\_log is turned off
* [Revision #485dcb07d1](https://github.com/MariaDB/server/commit/485dcb07d1)\
  2019-03-06 14:46:58 +0200
  * [MDEV-18637](https://jira.mariadb.org/browse/MDEV-18637) Assertion \`cache' failed in fts\_init\_recover\_doc
* [Revision #4b5dc47f56](https://github.com/MariaDB/server/commit/4b5dc47f56)\
  2019-03-06 12:45:54 +0200
  * [MDEV-18659](https://jira.mariadb.org/browse/MDEV-18659): Revert a non-functional change
* [Revision #b761211685](https://github.com/MariaDB/server/commit/b761211685)\
  2019-03-06 11:22:27 +0200
  * [MDEV-18659](https://jira.mariadb.org/browse/MDEV-18659): Fix string truncation/overflow in InnoDB and XtraDB
* [Revision #b21930fb0f](https://github.com/MariaDB/server/commit/b21930fb0f)\
  2019-03-06 10:37:43 +0200
  * [MDEV-18749](https://jira.mariadb.org/browse/MDEV-18749): Uninitialized value upon ADD FULLTEXT INDEX
* [Revision #91e4f00389](https://github.com/MariaDB/server/commit/91e4f00389)\
  2019-03-04 15:16:27 +0200
  * [MDEV-18732](https://jira.mariadb.org/browse/MDEV-18732) InnoDB: ALTER IGNORE returns error for NULL
* [Revision #19df45a705](https://github.com/MariaDB/server/commit/19df45a705)\
  2019-02-27 13:14:31 +0400
  * [MDEV-18333](https://jira.mariadb.org/browse/MDEV-18333) Slow\_queries count doesn't increase when slow\_query\_log is turned off
* Merge [Revision #f2e1451740](https://github.com/MariaDB/server/commit/f2e1451740) 2019-03-01 15:52:06 +0100 - Merge branch '10.0' into 10.1
* [Revision #2d34713294](https://github.com/MariaDB/server/commit/2d34713294)\
  2019-02-28 23:40:49 +0100
  * Increase the version
* Merge [Revision #7b5c63856b](https://github.com/MariaDB/server/commit/7b5c63856b) 2019-02-28 21:50:00 +0100 - Merge branch '5.5' into 10.0
* [Revision #e39d6e0c53](https://github.com/MariaDB/server/commit/e39d6e0c53)\
  2019-02-28 23:11:15 +0200
  * [MDEV-18601](https://jira.mariadb.org/browse/MDEV-18601) Can't create table with ENCRYPTED=DEFAULT when innodb\_default\_encryption\_key\_id!=1
* [Revision #622e9e8a7a](https://github.com/MariaDB/server/commit/622e9e8a7a)\
  2019-02-27 13:15:03 +0200
  * [MDEV-18265](https://jira.mariadb.org/browse/MDEV-18265): Replace deprecated variable debug to debug\_dbug on Galera tests
* [Revision #5a87e3ee87](https://github.com/MariaDB/server/commit/5a87e3ee87)\
  2019-02-28 09:29:19 +0200
  * Revert offending part of [MDEV-9519](https://jira.mariadb.org/browse/MDEV-9519): Data corruption will happen on the Galera cluster size change
* [Revision #243f829c1c](https://github.com/MariaDB/server/commit/243f829c1c)\
  2019-02-15 10:58:59 +0100
  * [MDEV-9519](https://jira.mariadb.org/browse/MDEV-9519): Data corruption will happen on the Galera cluster size change
* [Revision #28cb041754](https://github.com/MariaDB/server/commit/28cb041754)\
  2019-02-20 14:56:02 +0300
  * [MDEV-18662](https://jira.mariadb.org/browse/MDEV-18662) ib\_wqueue\_t has a data race
* [Revision #b88a803459](https://github.com/MariaDB/server/commit/b88a803459)\
  2019-02-21 09:19:18 +0200
  * [MDEV-17428](https://jira.mariadb.org/browse/MDEV-17428): Update wsrep\_max\_ws\_rows and wsrep\_max\_ws\_size values in wsrep.cnf.sh
* [Revision #d9f7b6be5a](https://github.com/MariaDB/server/commit/d9f7b6be5a)\
  2019-02-20 22:35:21 +0100
  * [MDEV-17942](https://jira.mariadb.org/browse/MDEV-17942) fixup : protect rebuild\_check\_host() / rebuild\_role\_grants() with acl\_cache->lock mutex
* [Revision #39a2984dc0](https://github.com/MariaDB/server/commit/39a2984dc0)\
  2019-02-20 17:22:44 +0100
  * Revert "[MDEV-18575](https://jira.mariadb.org/browse/MDEV-18575) Cleanup : remove innodb-encrypt-log parameter from mariadb-backup"
* [Revision #a2f82b649d](https://github.com/MariaDB/server/commit/a2f82b649d)\
  2019-02-20 16:23:10 +0100
  * [MDEV-17942](https://jira.mariadb.org/browse/MDEV-17942) Assertion \`found' failed in remove\_ptr\_from\_dynarray after failed CREATE OR REPLACE
* Merge [Revision #43a6aa377e](https://github.com/MariaDB/server/commit/43a6aa377e) 2019-02-20 10:43:09 +0100 - Merge branch '10.1' of [server](https://github.com/mariadb/server) into 10.1
* [Revision #431da59f1c](https://github.com/MariaDB/server/commit/431da59f1c)\
  2019-02-19 16:09:46 +0100\
  \*
  1. centos has symlinks /bin->usr/bin and /sbin -> usr/sbin, but even if this script called as /bin/mysql\_install\_db it is still standard install and scripts are in /usr/share/ (but not in the /share/) 2. fix of bindir path
* [Revision #2de0b57dd1](https://github.com/MariaDB/server/commit/2de0b57dd1)\
  2019-02-18 11:12:52 +0100
  * Don't build aws\_key\_management plugin by default
* Merge [Revision #16bc94820e](https://github.com/MariaDB/server/commit/16bc94820e) 2019-02-19 16:09:04 +0100 - Merge branch '10.1' of [server](https://github.com/mariadb/server) into 10.1
* [Revision #346e460896](https://github.com/MariaDB/server/commit/346e460896)\
  2019-02-19 10:51:34 +0200
  * Fixed bug in macro \_ma\_mark\_page\_with\_transid()
* [Revision #98e185ee37](https://github.com/MariaDB/server/commit/98e185ee37)\
  2019-02-18 21:42:58 +0200
  * [MDEV-18630](https://jira.mariadb.org/browse/MDEV-18630) Uninitialised value in FOREIGN KEY error message
* [Revision #3262967008](https://github.com/MariaDB/server/commit/3262967008)\
  2019-02-14 11:11:16 +0100
  * [MDEV-18575](https://jira.mariadb.org/browse/MDEV-18575) Cleanup : remove innodb-encrypt-log parameter from mariadb-backup
* [Revision #5b82751111](https://github.com/MariaDB/server/commit/5b82751111)\
  2019-02-06 16:44:36 +0100
  * [MDEV-18426](https://jira.mariadb.org/browse/MDEV-18426): Most of the mtr tests in the galera\_3nodes suite fail
* [Revision #be25414828](https://github.com/MariaDB/server/commit/be25414828)\
  2019-02-11 11:36:00 +0200
  * [MDEV-18016](https://jira.mariadb.org/browse/MDEV-18016): Cover the no-rebuild case, and remove a bogus debug assertion
* [Revision #af3cbb51ce](https://github.com/MariaDB/server/commit/af3cbb51ce)\
  2019-02-06 10:30:33 -0500
  * bump the VERSION
* [Revision #5eb3e4d83c](https://github.com/MariaDB/server/commit/5eb3e4d83c)\
  2019-02-05 17:03:41 +0200
  * [MDEV-15798](https://jira.mariadb.org/browse/MDEV-15798) Mutex leak on accessing INFORMATION\_SCHEMA.INNODB\_MUTEXES

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
