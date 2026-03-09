# MariaDB 10.2.26 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.26/)[Release Notes](../../old-releases/10.2/10.2.26.md)[Changelog](mariadb-10226-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 31 Jul 2019

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.26.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* Includes all fixes from [MariaDB 10.1.41](../changelogs-mariadb-101-series/mariadb-10141-changelog.md)
* [Revision #d6886b95d0](https://github.com/MariaDB/server/commit/d6886b95d0)\
  2019-07-27 00:19:28 +0300
  * List of unstable tests for 10.2.26 release (updated)
* Merge [Revision #32c6f40a63](https://github.com/MariaDB/server/commit/32c6f40a63) 2019-07-26 13:39:17 +0200 - Merge branch '10.1' into 10.2
* Merge [Revision #cf8c2a3c3b](https://github.com/MariaDB/server/commit/cf8c2a3c3b) 2019-07-26 07:03:39 +0200 - Merge branch '10.1' into 10.2
* [Revision #fc77a66c7e](https://github.com/MariaDB/server/commit/fc77a66c7e)\
  2019-07-25 18:08:50 +0300
  * Disable a failing test
* [Revision #57421419ce](https://github.com/MariaDB/server/commit/57421419ce)\
  2019-07-25 17:35:38 +0300
  * RocksDB: Do not test bogus parameter slave\_gtid\_info
* [Revision #a7e9395f9d](https://github.com/MariaDB/server/commit/a7e9395f9d)\
  2019-07-25 13:34:36 +0300
  * fts\_sync\_table(), fts\_sync() dead code removal
* [Revision #7de38492fc](https://github.com/MariaDB/server/commit/7de38492fc)\
  2019-07-25 13:33:25 +0300
  * After-merge fix: cmake -DPLUGIN\_PERFSCHEMA=NO
* Merge [Revision #a3455c6085](https://github.com/MariaDB/server/commit/a3455c6085) 2019-07-25 12:40:54 +0300 - [MDEV-20133](https://jira.mariadb.org/browse/MDEV-20133) Merge new release of InnoDB 5.7.27 to 10.2
* [Revision #60069a9829](https://github.com/MariaDB/server/commit/60069a9829)\
  2019-04-27 05:54:37 +0530
  * Bug #29127203 VIRTUAL GENERATED COLUMN INDEX DATA INCONSISTENCY
* Merge [Revision #b6ac67389d](https://github.com/MariaDB/server/commit/b6ac67389d) 2019-07-25 12:08:50 +0300 - Merge 10.1 into 10.2
* [Revision #ee555f8fc5](https://github.com/MariaDB/server/commit/ee555f8fc5)\
  2019-07-24 03:23:01 -0700
  * [MDEV-19948](https://jira.mariadb.org/browse/MDEV-19948) `SHOW GRANTS` return privileges individually update in 10.2
* [Revision #8fb39b2c35](https://github.com/MariaDB/server/commit/8fb39b2c35)\
  2019-07-24 16:34:14 +0530
  * [MDEV-19870](https://jira.mariadb.org/browse/MDEV-19870) gcol.innodb\_virtual\_debug\_purge doesn't fail if row\_vers\_old\_has\_index\_entry gives wrong result
* [Revision #c22305f050](https://github.com/MariaDB/server/commit/c22305f050)\
  2019-07-24 12:52:35 +0300
  * List of unstable tests for 10.2.26 release
* [Revision #97055e6b11](https://github.com/MariaDB/server/commit/97055e6b11)\
  2019-07-23 17:13:00 +0300
  * [MDEV-14154](https://jira.mariadb.org/browse/MDEV-14154): Remove ut\_time\_us()
* Merge [Revision #058c385e03](https://github.com/MariaDB/server/commit/058c385e03) 2019-07-23 16:34:04 +0300 - Merge 10.1 into 10.2
* [Revision #3bcda8ad5f](https://github.com/MariaDB/server/commit/3bcda8ad5f)\
  2019-07-22 17:33:08 +0300
  * [MDEV-17005](https://jira.mariadb.org/browse/MDEV-17005): Re-enable existing tests for non-debug server
* Merge [Revision #60c790d6f4](https://github.com/MariaDB/server/commit/60c790d6f4) 2019-07-22 15:28:05 +0300 - Merge 10.1 into 10.2
* [Revision #12614af1fe](https://github.com/MariaDB/server/commit/12614af1fe)\
  2019-07-15 20:30:45 +1000
  * [MDEV-17005](https://jira.mariadb.org/browse/MDEV-17005) ASAN heap-use-after-free in innobase\_get\_computed\_value
* [Revision #b0b5485251](https://github.com/MariaDB/server/commit/b0b5485251)\
  2019-07-16 00:38:53 +1000
  * [MDEV-17005](https://jira.mariadb.org/browse/MDEV-17005) add debug logs and set up deterministic test
* [Revision #f27a00435b](https://github.com/MariaDB/server/commit/f27a00435b)\
  2019-07-22 12:16:39 +0200
  * The test for the wsrep\_info plugin needs the same flexible wsrep version checking as the tests for Galera (continuation of [MDEV-18565](https://jira.mariadb.org/browse/MDEV-18565) task)
* [Revision #6e98f6810c](https://github.com/MariaDB/server/commit/6e98f6810c)\
  2019-07-21 13:12:18 +0200
  * fix libsepol version detection for SUSE
* [Revision #e2bbb6f5e9](https://github.com/MariaDB/server/commit/e2bbb6f5e9)\
  2019-07-12 16:44:39 +0200
  * switch to CC 3.1
* [Revision #731ef75175](https://github.com/MariaDB/server/commit/731ef75175)\
  2019-07-19 21:24:28 +0300
  * [MDEV-20107](https://jira.mariadb.org/browse/MDEV-20107): rocksdb.check\_ignore\_unknown\_options fails on OS X again
* [Revision #8ec4aa4b6b](https://github.com/MariaDB/server/commit/8ec4aa4b6b)\
  2019-07-19 18:20:17 +0300
  * [MDEV-20107](https://jira.mariadb.org/browse/MDEV-20107): rocksdb.check\_ignore\_unknown\_options fails on OS X again
* [Revision #53a3594b90](https://github.com/MariaDB/server/commit/53a3594b90)\
  2019-07-19 13:25:46 +0300
  * [MDEV-19471](https://jira.mariadb.org/browse/MDEV-19471) Add ASAN-poisoned redzones for mem\_heap\_t
* Merge [Revision #d9dcb8ba02](https://github.com/MariaDB/server/commit/d9dcb8ba02) 2019-07-19 11:45:55 +0300 - Merge 10.1 into 10.2
* [Revision #059968dc5d](https://github.com/MariaDB/server/commit/059968dc5d)\
  2019-07-19 11:42:34 +0300
  * Remove a conditionally unused declaration
* [Revision #9c29d06862](https://github.com/MariaDB/server/commit/9c29d06862)\
  2019-07-19 11:42:08 +0300
  * [MDEV-20097](https://jira.mariadb.org/browse/MDEV-20097) potential use-after-free
* Merge [Revision #6a55aeb2af](https://github.com/MariaDB/server/commit/6a55aeb2af) 2019-07-18 23:38:48 +0300 - Merge 10.1 into 10.2
* Merge [Revision #e55cc2d8cc](https://github.com/MariaDB/server/commit/e55cc2d8cc) 2019-07-18 17:55:21 +0300 - Merge 10.1 into 10.2
* [Revision #c0eb3a4d92](https://github.com/MariaDB/server/commit/c0eb3a4d92)\
  2019-07-18 14:56:39 +0200
  * Fixed dependency checking in some Galera tests
* Merge [Revision #6962855185](https://github.com/MariaDB/server/commit/6962855185) 2019-07-18 13:10:09 +0300 - Merge 10.1 into 10.2
* [Revision #26b594e411](https://github.com/MariaDB/server/commit/26b594e411)\
  2019-07-18 11:37:01 +0200
  * Set the garbd\_exe variable to empty string to avoid warning about an uninitialized variable when wsrep\_provider is not initialized correctly, set to 'none' or when wsrep is switched off
* [Revision #4e02e502f6](https://github.com/MariaDB/server/commit/4e02e502f6)\
  2019-07-16 11:33:11 +0200
  * [MDEV-18565](https://jira.mariadb.org/browse/MDEV-18565): Galera mtr-suite fails if galera library is not installed
* [Revision #52f6aa1c54](https://github.com/MariaDB/server/commit/52f6aa1c54)\
  2019-07-16 18:42:19 +0300
  * Disable rocksdb\_rpl.rpl\_gtid\_crash\_safe\_optimized
* [Revision #a2dc3b9461](https://github.com/MariaDB/server/commit/a2dc3b9461)\
  2019-07-16 17:16:59 +0300
  * Disable rocksdb\_rpl.optimize\_myrocks\_replace\_into
* [Revision #e9a1918376](https://github.com/MariaDB/server/commit/e9a1918376)\
  2019-07-16 16:50:05 +0300
  * Disable rocksdb.rpl\_row\_not\_found
* [Revision #612f4908d2](https://github.com/MariaDB/server/commit/612f4908d2)\
  2019-07-16 12:23:52 +0300
  * rocksdb.unique\_check: attempt to remove race condtitions from the test
* [Revision #143fede177](https://github.com/MariaDB/server/commit/143fede177)\
  2019-07-16 11:10:59 +0300
  * Disable rocksdb.force\_shutdown, rocksdb.shutdown is fine
* [Revision #537893b072](https://github.com/MariaDB/server/commit/537893b072)\
  2019-07-16 11:07:46 +0300
  * Fix rocksdb.tbl\_opt\_data\_index\_dir on a mac
* [Revision #d2f094d9e6](https://github.com/MariaDB/server/commit/d2f094d9e6)\
  2019-07-15 22:50:18 +0300
  * Disable rocksdb.shutdown test
* [Revision #1da844124d](https://github.com/MariaDB/server/commit/1da844124d)\
  2019-07-15 12:25:36 +0300
  * Fix rocksdb.tbl\_opt\_data\_index\_dir on a mac
* [Revision #ec49976e38](https://github.com/MariaDB/server/commit/ec49976e38)\
  2019-07-11 07:13:58 +0300
  * [MDEV-19746](https://jira.mariadb.org/browse/MDEV-19746): Galera test failures because of wsrep\_slave\_threads identification
* [Revision #b3bd51c992](https://github.com/MariaDB/server/commit/b3bd51c992)\
  2019-07-15 00:50:46 +0300
  * Fix rocksdb.autoinc\_vars\_thread test
* [Revision #9ccbe8d581](https://github.com/MariaDB/server/commit/9ccbe8d581)\
  2019-07-14 11:25:24 +0300
  * Fix intermittent test failure in rocksdb.rocksdb\_cf\_per\_partition
* [Revision #fbbc2354c8](https://github.com/MariaDB/server/commit/fbbc2354c8)\
  2019-07-12 21:41:01 +0300
  * [MDEV-14455](https://jira.mariadb.org/browse/MDEV-14455): rocksdb.2pc\_group\_commit failed in buildbot
* [Revision #64900e3d7c](https://github.com/MariaDB/server/commit/64900e3d7c)\
  2019-07-10 12:37:48 +0530
  * [MDEV-15641](https://jira.mariadb.org/browse/MDEV-15641) InnoDB crash while committing table-rebuilding ALTER TABLE
* [Revision #578e822985](https://github.com/MariaDB/server/commit/578e822985)\
  2019-06-26 11:46:59 +0200
  * bugfix: RPM installation complains about policy files, mariadb.service is not installed
* [Revision #ab3a6ca670](https://github.com/MariaDB/server/commit/ab3a6ca670)\
  2019-07-07 15:07:13 +0200
  * cleanup: CPACK\_RPM\_\* package description
* [Revision #e47a143fc0](https://github.com/MariaDB/server/commit/e47a143fc0)\
  2019-06-26 16:20:12 +0200
  * package ed25519 in debs
* [Revision #01d3e39288](https://github.com/MariaDB/server/commit/01d3e39288)\
  2019-07-10 09:43:49 +0300
  * Galera test fixes.
* [Revision #46c9268b0a](https://github.com/MariaDB/server/commit/46c9268b0a)\
  2019-07-09 22:24:50 +0300
  * post-merge fixes
* [Revision #4f1e4aa2ca](https://github.com/MariaDB/server/commit/4f1e4aa2ca)\
  2019-07-09 22:16:43 +0300
  * fix clang warnings
* Merge [Revision #26c389b7b7](https://github.com/MariaDB/server/commit/26c389b7b7) 2019-07-09 13:22:22 +0300 - Merge 10.1 into 10.2
* [Revision #b9557418cc](https://github.com/MariaDB/server/commit/b9557418cc)\
  2019-07-09 08:32:13 +0300
  * Galera test adjustments.
* [Revision #1153950ad0](https://github.com/MariaDB/server/commit/1153950ad0)\
  2019-07-08 21:12:22 +0300
  * Fix test blocking for [MDEV-16222](https://jira.mariadb.org/browse/MDEV-16222) on 10.2
* [Revision #53dd0e4f75](https://github.com/MariaDB/server/commit/53dd0e4f75)\
  2019-06-25 10:53:33 +0300
  * [MDEV-16222](https://jira.mariadb.org/browse/MDEV-16222) Assertion \`0' failed in row\_purge\_remove\_sec\_if\_poss\_leaf on table with virtual columns and indexes
* [Revision #0fe212a880](https://github.com/MariaDB/server/commit/0fe212a880)\
  2019-06-17 11:44:53 +0300
  * [MDEV-19785](https://jira.mariadb.org/browse/MDEV-19785) Storage CONNECT compilation error: unknown type name 'UNZFAM'
* [Revision #9abdf11ed1](https://github.com/MariaDB/server/commit/9abdf11ed1)\
  2019-07-07 18:03:52 +0300
  * Update RocksDB the revision that fixes the compile error on power8
* [Revision #5ebef42238](https://github.com/MariaDB/server/commit/5ebef42238)\
  2019-06-26 16:10:00 +0300
  * [MDEV-19292](https://jira.mariadb.org/browse/MDEV-19292) "Row size too large" error when creating table with lots columns when row format is DYNAMIC or COMPRESSED
* [Revision #044d0ffcf3](https://github.com/MariaDB/server/commit/044d0ffcf3)\
  2019-07-05 10:25:16 +0300
  * Disable MW-329 (badly written test case).
* [Revision #d3c21484be](https://github.com/MariaDB/server/commit/d3c21484be)\
  2019-07-03 19:04:38 +0200
  * [MDEV-19942](https://jira.mariadb.org/browse/MDEV-19942) Default installation of mariadb-server doesn't allow clients to use client plugins
* [Revision #7d56bddfcf](https://github.com/MariaDB/server/commit/7d56bddfcf)\
  2019-07-05 06:51:29 +0300
  * Galera test fixes
* [Revision #fee61edd44](https://github.com/MariaDB/server/commit/fee61edd44)\
  2019-07-03 15:52:38 +0300
  * [MDEV-19939](https://jira.mariadb.org/browse/MDEV-19939): Galera test failure on galera\_toi\_ddl\_fk\_insert
* [Revision #24aa723a28](https://github.com/MariaDB/server/commit/24aa723a28)\
  2019-07-03 15:15:58 +0300
  * Update Galera failing test list and record correct results for passing ones.
* [Revision #c17b0b734c](https://github.com/MariaDB/server/commit/c17b0b734c)\
  2019-07-04 00:53:07 +0300
  * [MDEV-19936](https://jira.mariadb.org/browse/MDEV-19936): MyRocks: compile fails on Windows
* [Revision #69e1d65cce](https://github.com/MariaDB/server/commit/69e1d65cce)\
  2019-07-03 15:15:58 +0300
  * Update Galera failing test list.
* [Revision #24403da91a](https://github.com/MariaDB/server/commit/24403da91a)\
  2019-07-03 14:42:04 +0300
  * Remove unused const TABLE\_HASH\_SIZE
* [Revision #666730ee52](https://github.com/MariaDB/server/commit/666730ee52)\
  2019-07-03 14:32:24 +0300
  * Fix gcc-8 warning in rocksdb
* [Revision #a946b36601](https://github.com/MariaDB/server/commit/a946b36601)\
  2019-07-02 22:25:48 +0300
  * Fix the compilation after the parent commit
* [Revision #c1cb5c17be](https://github.com/MariaDB/server/commit/c1cb5c17be)\
  2019-07-02 21:38:34 +0300
  * [MDEV-19869](https://jira.mariadb.org/browse/MDEV-19869): Correct the logic, and avoid type mismatch
* [Revision #0c6514eece](https://github.com/MariaDB/server/commit/0c6514eece)\
  2019-07-02 21:33:54 +0300
  * [MDEV-19781](https://jira.mariadb.org/browse/MDEV-19781): Skip the test for embedded server
* [Revision #7f1e1309bb](https://github.com/MariaDB/server/commit/7f1e1309bb)\
  2019-07-02 15:20:13 +0300
  * [MDEV-12626](https://jira.mariadb.org/browse/MDEV-12626): Import innodb\_buffer\_pool\_dump\_pct adjusted for [MDEV-11454](https://jira.mariadb.org/browse/MDEV-11454)
* [Revision #6bb922e58e](https://github.com/MariaDB/server/commit/6bb922e58e)\
  2019-07-02 15:17:09 +0300
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Import and adjust innodb.blob-crash
* [Revision #41f6e68878](https://github.com/MariaDB/server/commit/41f6e68878)\
  2019-07-01 21:58:20 +0530
  * [MDEV-19781](https://jira.mariadb.org/browse/MDEV-19781) Add page id matching check in innochecksum tool
* [Revision #40c1f4bd4c](https://github.com/MariaDB/server/commit/40c1f4bd4c)\
  2019-07-01 20:21:26 +0530
  * [MDEV-19781](https://jira.mariadb.org/browse/MDEV-19781) Add page id matching check in innochecksum tool
* [Revision #dca9792a24](https://github.com/MariaDB/server/commit/dca9792a24)\
  2019-07-01 18:50:44 +0530
  * [MDEV-17228](https://jira.mariadb.org/browse/MDEV-17228) Encrypted temporary tables are not encrypted
* [Revision #5a136d84f3](https://github.com/MariaDB/server/commit/5a136d84f3)\
  2019-07-01 13:27:12 +0300
  * [MDEV-19766](https://jira.mariadb.org/browse/MDEV-19766): Disable page dump output in debug builds
* [Revision #85d0a1955f](https://github.com/MariaDB/server/commit/85d0a1955f)\
  2019-07-01 15:21:17 +0530
  * [MDEV-19914](https://jira.mariadb.org/browse/MDEV-19914) Server startup fails while dropping garbage encrypted tablespace if innodb\_encryption\_threads > 0
* [Revision #ed6da51f3e](https://github.com/MariaDB/server/commit/ed6da51f3e)\
  2019-07-01 13:44:59 +0530
  * [MDEV-19869](https://jira.mariadb.org/browse/MDEV-19869) Port innodb\_fts.fulltext2 from mysql to mariadb.
* [Revision #723a4b1d78](https://github.com/MariaDB/server/commit/723a4b1d78)\
  2019-06-27 16:23:03 +0530
  * [MDEV-17228](https://jira.mariadb.org/browse/MDEV-17228) Encrypted temporary tables are not encrypted
* [Revision #e4a0dbfb4a](https://github.com/MariaDB/server/commit/e4a0dbfb4a)\
  2019-06-28 18:49:43 +0530
  * [MDEV-19781](https://jira.mariadb.org/browse/MDEV-19781) Add page id matching check in innochecksum tool
* [Revision #f7a4a8719b](https://github.com/MariaDB/server/commit/f7a4a8719b)\
  2019-06-27 20:57:01 +0300
  * [MDEV-14996](https://jira.mariadb.org/browse/MDEV-14996) kill during FLUSH TABLES FOR EXPORT causes assert
* [Revision #51c3a5c840](https://github.com/MariaDB/server/commit/51c3a5c840)\
  2019-06-27 16:50:39 +0200
  * [MDEV-19893](https://jira.mariadb.org/browse/MDEV-19893) Do not send error packets with seqno= 0
* [Revision #dc11aab9b3](https://github.com/MariaDB/server/commit/dc11aab9b3)\
  2019-06-27 15:17:26 +0200
  * [MDEV-19889](https://jira.mariadb.org/browse/MDEV-19889) In CMakeLists.txt, use ${CMAKE\_CPACK\_COMMAND},rather than just cpack
* [Revision #92feac53a6](https://github.com/MariaDB/server/commit/92feac53a6)\
  2019-06-27 15:39:04 +0300
  * [MDEV-19886](https://jira.mariadb.org/browse/MDEV-19886) InnoDB returns misleading ER\_NO\_SUCH\_TABLE\_IN\_ENGINE
* [Revision #6d2b236568](https://github.com/MariaDB/server/commit/6d2b236568)\
  2019-06-20 23:37:28 +0300
  * [MDEV-19865](https://jira.mariadb.org/browse/MDEV-19865): AddressSanitizer error in open\_or\_create\_log\_file() in mariadb-backup
* [Revision #7a2958f456](https://github.com/MariaDB/server/commit/7a2958f456)\
  2019-06-25 15:59:57 +0300
  * [MDEV-17576](https://jira.mariadb.org/browse/MDEV-17576) Assertion in maria\_extra upon ALTER on table with triggers and locks
* [Revision #41e02d149e](https://github.com/MariaDB/server/commit/41e02d149e)\
  2019-06-25 15:55:20 +0300
  * Remove the stray test innodb\_zip.16k
* [Revision #a12fb5d0eb](https://github.com/MariaDB/server/commit/a12fb5d0eb)\
  2019-06-24 17:07:20 +0300
  * Replace innodb\_zip.16k with innodb\_zip.page\_size
* [Revision #6ffaed615a](https://github.com/MariaDB/server/commit/6ffaed615a)\
  2019-06-24 14:31:49 +0300
  * Remove the unused function maria\_clone
* Merge [Revision #ddeeb42e0b](https://github.com/MariaDB/server/commit/ddeeb42e0b) 2019-06-23 19:07:20 +0300 - Merge 10.1 into 10.2
* Merge [Revision #75833ef9c5](https://github.com/MariaDB/server/commit/75833ef9c5) 2019-06-21 14:20:03 +0300 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* [Revision #8d24f4e35d](https://github.com/MariaDB/server/commit/8d24f4e35d)\
  2019-06-21 12:02:40 +0200
  * [MDEV-19821](https://jira.mariadb.org/browse/MDEV-19821) "perl;" snippet must run the same perl executable that runs mtr.
* Merge [Revision #821b866b55](https://github.com/MariaDB/server/commit/821b866b55) 2019-06-21 12:56:26 +0300 - Merge branch 'bb-10.2-myrocks-merge' into 10.2
* [Revision #7345c0de26](https://github.com/MariaDB/server/commit/7345c0de26)\
  2019-06-20 21:34:15 +0300
  * Fix tests: some build hosts have ramdisk in /run/shm instead of /dev/shm
* [Revision #622ecfc7c6](https://github.com/MariaDB/server/commit/622ecfc7c6)\
  2019-06-20 19:35:36 +0300
  * Update test results
* [Revision #a2e9e3fbd4](https://github.com/MariaDB/server/commit/a2e9e3fbd4)\
  2019-06-20 15:29:17 +0300
  * MyRocks: dont show read-Free replication variables
* [Revision #7f845c6653](https://github.com/MariaDB/server/commit/7f845c6653)\
  2019-06-16 23:21:12 +0300
  * Fix typo
* [Revision #a0251c7d75](https://github.com/MariaDB/server/commit/a0251c7d75)\
  2019-06-16 21:44:02 +0300
  * Post-merge build fixes
* [Revision #15087b41a5](https://github.com/MariaDB/server/commit/15087b41a5)\
  2019-06-16 21:07:23 +0300
  * More Post-merge fixes
* [Revision #27e05d92be](https://github.com/MariaDB/server/commit/27e05d92be)\
  2019-06-16 20:41:53 +0300
  * Post-merge fixes cont'd
* [Revision #6152ecea21](https://github.com/MariaDB/server/commit/6152ecea21)\
  2019-06-16 20:28:01 +0300
  * Post-merge fixes: fix rocksdb.tbl\_opt\_data\_index\_dir
* [Revision #c399405885](https://github.com/MariaDB/server/commit/c399405885)\
  2019-06-16 17:42:45 +0300
  * Post-merge fixes: rocksdb.bloomfilter3, use\_direct\_io\_for\_flush\_and\_compaction
* [Revision #23b967d639](https://github.com/MariaDB/server/commit/23b967d639)\
  2019-06-16 15:29:04 +0300
  * Post-merge fixes: fix linking on Windows
* [Revision #ba2f20cc33](https://github.com/MariaDB/server/commit/ba2f20cc33)\
  2019-06-16 12:53:13 +0300
  * Post-merge fix: fix compilation on Windows
* [Revision #934c8f7f47](https://github.com/MariaDB/server/commit/934c8f7f47)\
  2019-06-16 12:47:23 +0300
  * Trivial test result update after fix for [MDEV-19771](https://jira.mariadb.org/browse/MDEV-19771)
* [Revision #9c75b3d283](https://github.com/MariaDB/server/commit/9c75b3d283)\
  2019-06-16 12:44:04 +0300
  * Post-merge fixes
* [Revision #e9e5e7fc92](https://github.com/MariaDB/server/commit/e9e5e7fc92)\
  2019-06-16 00:36:04 +0300
  * Post-merge fix: MariaDB doesn't have I\_S.PROCESSLIST.SRV\_ID
* Merge [Revision #9ab0d7b4e9](https://github.com/MariaDB/server/commit/9ab0d7b4e9) 2019-06-16 00:28:33 +0300 - Merge from MyRocks upstream:
* [Revision #5173e396ff](https://github.com/MariaDB/server/commit/5173e396ff)\
  2019-06-15 21:29:46 +0300
  * Copy of commit dcd9379eb5707bc7514a2ff4d9127790356505cb Author: Manuel Ung [mung@fb.com](mailto:mung@fb.com) Date: Fri Jun 14 10:38:17 2019 -0700
* [Revision #91be2212c6](https://github.com/MariaDB/server/commit/91be2212c6)\
  2019-06-15 19:55:57 +0300
  * [MDEV-17045](https://jira.mariadb.org/browse/MDEV-17045): MyRocks tables cannot be updated when binlog\_format=MIXED.
* [Revision #c631bd7f10](https://github.com/MariaDB/server/commit/c631bd7f10)\
  2019-06-19 11:22:36 +0300
  * Disable galera.MW-388.
* [Revision #8acbf9c1f9](https://github.com/MariaDB/server/commit/8acbf9c1f9)\
  2019-06-19 00:35:44 +0300
  * [MDEV-19595](https://jira.mariadb.org/browse/MDEV-19595) fixed
* [Revision #b23c82fef3](https://github.com/MariaDB/server/commit/b23c82fef3)\
  2019-06-18 14:32:24 +0300
  * [MDEV-18078](https://jira.mariadb.org/browse/MDEV-18078) Assertion \`trnman\_has\_locked\_tables(trn) > 0' failed
* [Revision #71eea0c3fb](https://github.com/MariaDB/server/commit/71eea0c3fb)\
  2019-06-17 19:01:15 +0100
  * Fix debug assert to match its intention.
* [Revision #5804bb4ef0](https://github.com/MariaDB/server/commit/5804bb4ef0)\
  2019-06-17 09:56:00 +0100
  * [MDEV-19750](https://jira.mariadb.org/browse/MDEV-19750) mysql command wrong encoding
* [Revision #81f60e8ade](https://github.com/MariaDB/server/commit/81f60e8ade)\
  2019-06-17 18:04:22 +0100
  * Portability fix.
* [Revision #c8b5fa4afc](https://github.com/MariaDB/server/commit/c8b5fa4afc)\
  2019-06-17 17:50:08 +0300
  * [MDEV-19055](https://jira.mariadb.org/browse/MDEV-19055) Failures with temporary tables and Aria
* [Revision #2b660fb4c2](https://github.com/MariaDB/server/commit/2b660fb4c2)\
  2019-06-16 15:55:09 +0300
  * mtr\_t::is\_block\_dirtied(): Define inline
* [Revision #a94638f155](https://github.com/MariaDB/server/commit/a94638f155)\
  2019-06-16 15:54:14 +0300
  * Clarify the purpose of MTR\_LOG\_NONE
* [Revision #e9795d0208](https://github.com/MariaDB/server/commit/e9795d0208)\
  2019-06-16 15:38:05 +0300
  * Add mtr\_buf\_t::for\_each\_block\_in\_reverse() const
* [Revision #93c84cc8f2](https://github.com/MariaDB/server/commit/93c84cc8f2)\
  2019-06-15 19:55:57 +0300
  * [MDEV-17045](https://jira.mariadb.org/browse/MDEV-17045): MyRocks tables cannot be updated when binlog\_format=MIXED.
* [Revision #2b0eb352b3](https://github.com/MariaDB/server/commit/2b0eb352b3)\
  2019-06-16 12:12:00 +0300
  * Trivial test result update after fix for [MDEV-19771](https://jira.mariadb.org/browse/MDEV-19771)
* [Revision #9dd72bbfb0](https://github.com/MariaDB/server/commit/9dd72bbfb0)\
  2019-06-15 16:54:02 -0400
  * bump the VERSION
* [Revision #c02d6164fb](https://github.com/MariaDB/server/commit/c02d6164fb)\
  2019-06-15 14:46:25 +0300
  * [MDEV-19771](https://jira.mariadb.org/browse/MDEV-19771) REPLACE on table with virtual\_field can cause crash

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
