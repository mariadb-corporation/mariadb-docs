# MariaDB 10.2.27 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.27/)[Release Notes](../../old-releases/10.2/10.2.27.md)[Changelog](mariadb-10227-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 11 Sep 2019

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.27.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* Includes all fixes from [MariaDB 10.1.41](../changelogs-mariadb-101-series/mariadb-10141-changelog.md)
* [Revision #f9f968557f](https://github.com/MariaDB/server/commit/f9f968557f)\
  2019-09-08 16:21:48 +0300
  * List of unstable tests for 10.2.27 release
* [Revision #8750df43ab](https://github.com/MariaDB/server/commit/8750df43ab)\
  2019-09-07 07:44:54 +0400
  * [MDEV-20517](https://jira.mariadb.org/browse/MDEV-20517) Assertion \`!is\_expensive()' failed in Item::value\_depends\_on\_sql\_mode\_const\_item
* [Revision #39e5b76ef1](https://github.com/MariaDB/server/commit/39e5b76ef1)\
  2019-09-06 14:42:46 +0200
  * use a shorter name for sources in debuginfo rpms
* [Revision #5a9e2b77d4](https://github.com/MariaDB/server/commit/5a9e2b77d4)\
  2019-09-06 14:36:12 +0200
  * [MDEV-18156](https://jira.mariadb.org/browse/MDEV-18156) Assertion `0' failed or` btr\_validate\_index(index, 0, false)' in row\_upd\_sec\_index\_entry or error code 126: Index is corrupted upon DELETE with PAD\_CHAR\_TO\_FULL\_LENGTH
* [Revision #2480f6b7ff](https://github.com/MariaDB/server/commit/2480f6b7ff)\
  2019-09-06 14:08:46 +0200
  * don't run RocksDB suites by default
* [Revision #292e2649d4](https://github.com/MariaDB/server/commit/292e2649d4)\
  2019-09-06 12:47:48 +0300
  * [MDEV-12121](https://jira.mariadb.org/browse/MDEV-12121): Avoid unused variable
* [Revision #16e9943d89](https://github.com/MariaDB/server/commit/16e9943d89)\
  2019-09-04 10:31:40 +0300
  * [MDEV-20421](https://jira.mariadb.org/browse/MDEV-20421): big\_innodb\_log reliably fails on buildbot Windows
* [Revision #41e351f608](https://github.com/MariaDB/server/commit/41e351f608)\
  2019-09-05 17:43:13 +0300
  * [MDEV-20490](https://jira.mariadb.org/browse/MDEV-20490): rocksdb.ttl\_primary\_read\_filtering fails in BB
* [Revision #f605ce08b5](https://github.com/MariaDB/server/commit/f605ce08b5)\
  2019-09-04 14:20:37 +0200
  * more tests for DEFAULT and DEFAULT(column) in INSERT
* [Revision #8dca4cf53f](https://github.com/MariaDB/server/commit/8dca4cf53f)\
  2019-09-04 14:02:01 +0200
  * [MDEV-20403](https://jira.mariadb.org/browse/MDEV-20403) Assertion `0' or Assertion` btr\_validate\_index(index, 0)' failed in row\_upd\_sec\_index\_entry or error code 126: Index is corrupted upon UPDATE with TIMESTAMP..ON UPDATE
* [Revision #53ec9047c9](https://github.com/MariaDB/server/commit/53ec9047c9)\
  2019-07-27 19:57:46 +0530
  * [MDEV-20137](https://jira.mariadb.org/browse/MDEV-20137) rpl.mdev\_17588 fails in buildbot with "Table doesn't exist"
* [Revision #01e455dbb8](https://github.com/MariaDB/server/commit/01e455dbb8)\
  2019-09-04 01:59:35 +0300
  * Fix of query cache bug in Aria
* [Revision #dae1b3b04c](https://github.com/MariaDB/server/commit/dae1b3b04c)\
  2019-09-03 13:04:05 +0300
  * [MDEV-15326](https://jira.mariadb.org/browse/MDEV-15326): Backport trx\_t::is\_referenced()
* [Revision #b07beff894](https://github.com/MariaDB/server/commit/b07beff894)\
  2019-09-03 12:31:37 +0300
  * [MDEV-15326](https://jira.mariadb.org/browse/MDEV-15326): InnoDB: Failing assertion: !other\_lock
* [Revision #7c79c12784](https://github.com/MariaDB/server/commit/7c79c12784)\
  2019-09-02 14:00:53 +0300
  * [MDEV-15326](https://jira.mariadb.org/browse/MDEV-15326) preparation: Remove trx\_sys\_t::n\_prepared\_trx
* [Revision #154bd0950f](https://github.com/MariaDB/server/commit/154bd0950f)\
  2019-09-03 11:23:57 +0300
  * [MDEV-15326](https://jira.mariadb.org/browse/MDEV-15326) preparation: Test slow shutdown after XA PREPARE
* [Revision #b2775ae855](https://github.com/MariaDB/server/commit/b2775ae855)\
  2019-09-02 12:31:29 +0300
  * MVCC::view\_close(): Correct comments
* [Revision #cbb85f0d21](https://github.com/MariaDB/server/commit/cbb85f0d21)\
  2019-09-04 08:36:52 +0300
  * Disable galera.galera\_var\_node\_address test case.
* [Revision #6ee7a9a438](https://github.com/MariaDB/server/commit/6ee7a9a438)\
  2019-09-03 11:41:35 +0200
  * C/C
* [Revision #c7c481f4d9](https://github.com/MariaDB/server/commit/c7c481f4d9)\
  2019-09-02 14:10:20 +0200
  * [MDEV-20403](https://jira.mariadb.org/browse/MDEV-20403) Assertion `0' or Assertion` btr\_validate\_index(index, 0)' failed in row\_upd\_sec\_index\_entry or error code 126: Index is corrupted upon UPDATE with TIMESTAMP..ON UPDATE
* [Revision #3789692d17](https://github.com/MariaDB/server/commit/3789692d17)\
  2019-09-02 14:14:57 +0200
  * don't compare unassigned columns
* [Revision #17ab02f4b0](https://github.com/MariaDB/server/commit/17ab02f4b0)\
  2019-09-02 10:53:46 +0200
  * cleanup: on update default now
* [Revision #ef00ac4c86](https://github.com/MariaDB/server/commit/ef00ac4c86)\
  2019-08-29 12:35:19 +0400
  * [MDEV-18156](https://jira.mariadb.org/browse/MDEV-18156) Assertion `0' failed or` btr\_validate\_index(index, 0, false)' in row\_upd\_sec\_index\_entry or error code 126: Index is corrupted upon DELETE with PAD\_CHAR\_TO\_FULL\_LENGTH
* [Revision #dc719597ee](https://github.com/MariaDB/server/commit/dc719597ee)\
  2019-08-26 15:28:32 +0400
  * [MDEV-18156](https://jira.mariadb.org/browse/MDEV-18156) Assertion `0' failed or` btr\_validate\_index(index, 0, false)' in row\_upd\_sec\_index\_entry or error code 126: Index is corrupted upon DELETE with PAD\_CHAR\_TO\_FULL\_LENGTH
* [Revision #0d66358220](https://github.com/MariaDB/server/commit/0d66358220)\
  2019-09-02 17:18:04 +0300
  * Disabled test in 32bit that uses too much memory or cpu
* [Revision #9cba6c5aa3](https://github.com/MariaDB/server/commit/9cba6c5aa3)\
  2019-08-30 16:06:54 +0300
  * Updated mtr files to support different compiled in options
* [Revision #b23b3a5fb6](https://github.com/MariaDB/server/commit/b23b3a5fb6)\
  2019-09-01 15:13:22 +0300
  * Fixed some compiler warnings
* [Revision #b0916141c7](https://github.com/MariaDB/server/commit/b0916141c7)\
  2019-08-30 18:04:15 +0300
  * embedded client now writes errors to stderr during init\_embedded\_server
* [Revision #d558981e2c](https://github.com/MariaDB/server/commit/d558981e2c)\
  2019-08-30 14:38:16 +0300
  * Remove test that where only applicable for MySQL
* [Revision #2d85714448](https://github.com/MariaDB/server/commit/2d85714448)\
  2019-08-30 16:07:26 +0300
  * Updated BUILD/SETUP from [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md)
* [Revision #d5a11a1f02](https://github.com/MariaDB/server/commit/d5a11a1f02)\
  2019-09-01 13:27:32 +0200
  * C/C
* Merge [Revision #14149d6c33](https://github.com/MariaDB/server/commit/14149d6c33) 2019-08-30 16:52:43 +0200 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #6c593cd358](https://github.com/MariaDB/server/commit/6c593cd358)\
  2019-08-22 23:34:42 +0200
  * Typo
* [Revision #c0f9042500](https://github.com/MariaDB/server/commit/c0f9042500)\
  2019-08-19 18:06:34 +0200
  * Some small changes. Modify tracing to use htrc to be compatible with old versions when this code is used to make an EOM module.
* [Revision #4d93c7f3b0](https://github.com/MariaDB/server/commit/4d93c7f3b0)\
  2019-08-17 16:58:58 +0200
  * In CONNECT version 1.6.10 NOSQL facility is enhanced by a new way to retrieve NOSQL data. In addition to files and Mongo collections, JSON as well as XML and CSV data can be retrieved from the net as answers from REST queries. Because it uses and external package (cpprestsdk) this is currently available only to MariaDB servers compiled from source.
* [Revision #d302cb3534](https://github.com/MariaDB/server/commit/d302cb3534)\
  2019-07-31 11:17:59 +0200
  * Typo
* [Revision #e4797a991f](https://github.com/MariaDB/server/commit/e4797a991f)\
  2019-07-30 22:45:04 +0200
  * In CONNECT version 1.6.10 NOSQL facility is enhanced by a new way to retrieve NOSQL data. In addition to files and Mongo collections, JSON as well as XML and CSV data can be retrieved from the net as answers from REST queries. Because it uses and external package (cpprestsdk) this is currently available only to MariaDB servers compiled from source.
* [Revision #1688a22612](https://github.com/MariaDB/server/commit/1688a22612)\
  2019-08-30 14:13:00 +0300
  * [MDEV-18384](https://jira.mariadb.org/browse/MDEV-18384): rocksdb.index\_merge\_rocksdb2 test fails
* [Revision #5e9b34191e](https://github.com/MariaDB/server/commit/5e9b34191e)\
  2019-08-29 08:21:54 +0300
  * Clean up innodb.innodb-read-view
* [Revision #2842ae03bc](https://github.com/MariaDB/server/commit/2842ae03bc)\
  2019-08-28 15:27:35 +0300
  * Remove a bogus comment
* Merge [Revision #5f35e103ee](https://github.com/MariaDB/server/commit/5f35e103ee) 2019-08-28 15:23:21 +0300 - Merge 10.1 into 10.2
* [Revision #4ba20e0a14](https://github.com/MariaDB/server/commit/4ba20e0a14)\
  2019-08-28 04:49:01 +0200
  * Improved handling of subdirectories in the xtrabackup-v2 SST scripts (similar to [MDEV-18863](https://jira.mariadb.org/browse/MDEV-18863)) for more predictable test results (related to xtrabackup-v2 SST)
* [Revision #d4866c7d0d](https://github.com/MariaDB/server/commit/d4866c7d0d)\
  2019-08-26 19:19:12 +0300
  * fix clang warnings
* [Revision #f608713739](https://github.com/MariaDB/server/commit/f608713739)\
  2019-08-27 08:30:26 +0300
  * Enable galera\_sst\_mysqldump\_with\_key test case.
* [Revision #29bbf4749e](https://github.com/MariaDB/server/commit/29bbf4749e)\
  2019-08-27 09:13:20 +0400
  * [MDEV-19699](https://jira.mariadb.org/browse/MDEV-19699) Server crashes in Item\_null\_result::field\_type upon SELECT with ROLLUP on constant table
* [Revision #de0f93fb0d](https://github.com/MariaDB/server/commit/de0f93fb0d)\
  2019-08-26 13:37:09 +0200
  * [MDEV-20420](https://jira.mariadb.org/browse/MDEV-20420): SST failed after [MDEV-18863](https://jira.mariadb.org/browse/MDEV-18863) in some test configurations
* [Revision #4a9fb9055e](https://github.com/MariaDB/server/commit/4a9fb9055e)\
  2019-08-26 14:03:51 +0530
  * [MDEV-20188](https://jira.mariadb.org/browse/MDEV-20188): binlog.binlog\_stm\_drop\_tmp\_tbl fails in buildbot with Unknown table on exec
* [Revision #b01a95f6fc](https://github.com/MariaDB/server/commit/b01a95f6fc)\
  2019-08-22 17:37:13 +0300
  * row\_undo\_mod\_remove\_clust\_low(): Remove duplicated code
* [Revision #5b29820d80](https://github.com/MariaDB/server/commit/5b29820d80)\
  2019-08-22 11:11:22 +0300
  * Fix -Wstringop-truncation
* [Revision #94e6a4fa6a](https://github.com/MariaDB/server/commit/94e6a4fa6a)\
  2019-08-21 11:12:39 +0200
  * Bash-specific operator replaced by a universal one
* [Revision #91fdb931fa](https://github.com/MariaDB/server/commit/91fdb931fa)\
  2019-08-12 18:30:19 +0200
  * ensure that pam plugin is present in release packages
* [Revision #62cc991bc8](https://github.com/MariaDB/server/commit/62cc991bc8)\
  2019-07-14 12:17:32 +0200
  * really make CPACK\_RPM\_DEBUGINFO\_PACKAGE configurable
* [Revision #9cd6e7ad73](https://github.com/MariaDB/server/commit/9cd6e7ad73)\
  2019-05-14 14:01:15 +0200
  * [MDEV-16932](https://jira.mariadb.org/browse/MDEV-16932): ASAN heap-use-after-free in my\_charlen\_utf8 / my\_well\_formed\_char\_length\_utf8 on 2nd execution of SP with ALTER trying to add bad CHECK
* [Revision #7aac83580a](https://github.com/MariaDB/server/commit/7aac83580a)\
  2019-08-27 15:57:32 +0300
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Add innodb.innodb-read-view
* [Revision #25af2a183b](https://github.com/MariaDB/server/commit/25af2a183b)\
  2019-08-27 15:48:46 +0300
  * [MDEV-15326](https://jira.mariadb.org/browse/MDEV-15326)/[MDEV-16136](https://jira.mariadb.org/browse/MDEV-16136) dead code removal
* [Revision #e7b71e0daa](https://github.com/MariaDB/server/commit/e7b71e0daa)\
  2019-08-27 13:05:04 +0530
  * [MDEV-19925](https://jira.mariadb.org/browse/MDEV-19925): Column ... cannot be converted from type 'varchar(20)' to type 'varchar(20)'
* [Revision #9bf424bc7b](https://github.com/MariaDB/server/commit/9bf424bc7b)\
  2019-08-26 10:37:34 +0000
  * [MDEV-20421](https://jira.mariadb.org/browse/MDEV-20421) : Disable the test until fixed
* [Revision #202243d59e](https://github.com/MariaDB/server/commit/202243d59e)\
  2019-08-26 10:58:27 +0000
  * MTR : improve detection of handles.exe on Windows.
* [Revision #9de2e60d74](https://github.com/MariaDB/server/commit/9de2e60d74)\
  2019-08-21 11:38:17 +0300
  * [MDEV-17187](https://jira.mariadb.org/browse/MDEV-17187) table doesn't exist in engine after ALTER of FOREIGN KEY
* [Revision #e279c0076d](https://github.com/MariaDB/server/commit/e279c0076d)\
  2019-08-20 12:52:57 +0300
  * [MDEV-17187](https://jira.mariadb.org/browse/MDEV-17187): Code cleanup
* [Revision #ddaebdd210](https://github.com/MariaDB/server/commit/ddaebdd210)\
  2019-08-20 14:55:49 +0300
  * dict\_table\_open\_on\_index\_id(): Remove a redundant parameter
* [Revision #1a3c77e524](https://github.com/MariaDB/server/commit/1a3c77e524)\
  2019-08-21 09:09:26 +0300
  * [MDEV-19968](https://jira.mariadb.org/browse/MDEV-19968): Galera test failure on galera\_load\_data
* [Revision #6c06defb5f](https://github.com/MariaDB/server/commit/6c06defb5f)\
  2019-08-19 14:17:38 +0200
  * [MDEV-15458](https://jira.mariadb.org/browse/MDEV-15458) Segfault in heap\_scan() upon UPDATE after ADD SYSTEM VERSIONING
* [Revision #1ad70bf2fe](https://github.com/MariaDB/server/commit/1ad70bf2fe)\
  2019-08-20 13:06:53 +0200
  * Revert "Fixes a problem with heap when scanning and insert rows at the same time"
* [Revision #4438ff07cd](https://github.com/MariaDB/server/commit/4438ff07cd)\
  2019-08-20 16:03:43 +0300
  * [MDEV-20389](https://jira.mariadb.org/browse/MDEV-20389): Refine the test case
* [Revision #2850b8d844](https://github.com/MariaDB/server/commit/2850b8d844)\
  2019-08-20 15:24:32 +0300
  * [MDEV-20389](https://jira.mariadb.org/browse/MDEV-20389) The test innodb.innodb\_bug84958 fails intermittently
* [Revision #6dd1d6cb90](https://github.com/MariaDB/server/commit/6dd1d6cb90)\
  2019-08-20 15:28:01 +0300
  * [MDEV-20379](https://jira.mariadb.org/browse/MDEV-20379) Mroonga has memory leak in ha\_mroonga::is\_foreign\_key\_field
* [Revision #262927a9e5](https://github.com/MariaDB/server/commit/262927a9e5)\
  2019-08-20 12:57:52 +0300
  * Fixes a problem with heap when scanning and insert rows at the same time
* [Revision #64c6f2bffc](https://github.com/MariaDB/server/commit/64c6f2bffc)\
  2019-08-20 09:50:35 +0300
  * After-merge fixes
* Merge [Revision #48c67038b9](https://github.com/MariaDB/server/commit/48c67038b9) 2019-08-20 09:15:28 +0300 - Merge 10.1 into 10.2
* [Revision #bc89b1c558](https://github.com/MariaDB/server/commit/bc89b1c558)\
  2019-08-20 07:47:11 +0300
  * [MDEV-18863](https://jira.mariadb.org/browse/MDEV-18863): Fix -Wsign-compare
* Merge [Revision #a02dd7e614](https://github.com/MariaDB/server/commit/a02dd7e614) 2019-08-20 07:31:44 +0300 - Merge 5.5 into 10.1
* [Revision #e746f451d5](https://github.com/MariaDB/server/commit/e746f451d5)\
  2019-08-15 17:27:49 -0700
  * [MDEV-20265](https://jira.mariadb.org/browse/MDEV-20265) Unknown column in field list
* [Revision #a7e2cd55ab](https://github.com/MariaDB/server/commit/a7e2cd55ab)\
  2019-08-19 22:42:56 +0400
  * [MDEV-19034](https://jira.mariadb.org/browse/MDEV-19034) ASAN unknown-crash in get\_date\_time\_separator with PAD\_CHAR\_TO\_FULL\_LENGTH
* [Revision #457dc9d64d](https://github.com/MariaDB/server/commit/457dc9d64d)\
  2019-07-30 13:45:13 +0200
  * [MDEV-18863](https://jira.mariadb.org/browse/MDEV-18863): Galera SST scripts can't read \[mysqldN] option groups
* Merge [Revision #f987de7122](https://github.com/MariaDB/server/commit/f987de7122) 2019-08-16 20:58:14 +0400 - Merge remote-tracking branch 'origin/5.5' into 10.1
* [Revision #ec1f195ecf](https://github.com/MariaDB/server/commit/ec1f195ecf)\
  2019-08-16 14:32:44 +0400
  * [MDEV-15955](https://jira.mariadb.org/browse/MDEV-15955) Assertion \`field\_types == 0 || field\_types\[field\_pos] == MYSQL\_TYPE\_LONGLONG' failed in Protocol\_text::store\_longlong
* [Revision #ecdacf7264](https://github.com/MariaDB/server/commit/ecdacf7264)\
  2019-08-16 14:36:23 +0300
  * [MDEV-19834](https://jira.mariadb.org/browse/MDEV-19834) Selectivity of an equality condition discounted twice
* [Revision #fa74088838](https://github.com/MariaDB/server/commit/fa74088838)\
  2019-08-15 07:46:41 +0300
  * [MDEV-18778](https://jira.mariadb.org/browse/MDEV-18778): mysql\_tzinfo\_to\_sql does not work correctly in MariaDB Galera
* [Revision #1c75ad6eed](https://github.com/MariaDB/server/commit/1c75ad6eed)\
  2019-08-15 12:57:21 +0300
  * [MDEV-19834](https://jira.mariadb.org/browse/MDEV-19834) Selectivity of an equality condition discounted twice
* [Revision #588e67956a](https://github.com/MariaDB/server/commit/588e67956a)\
  2019-08-13 19:29:59 +0300
  * Make sure histograms do not write uninitialized bytes to record
* [Revision #12e3ac04fe](https://github.com/MariaDB/server/commit/12e3ac04fe)\
  2019-07-30 17:16:25 +0200
  * [MDEV-20185](https://jira.mariadb.org/browse/MDEV-20185): Windows: Use of uninitialized value $bpath in string eq
* [Revision #ff6d3075d5](https://github.com/MariaDB/server/commit/ff6d3075d5)\
  2019-07-30 13:45:13 +0200
  * [MDEV-18863](https://jira.mariadb.org/browse/MDEV-18863): Galera SST scripts can't read \[mysqldN] option groups
* [Revision #68e6c2d768](https://github.com/MariaDB/server/commit/68e6c2d768)\
  2019-08-19 17:11:49 +0300
  * [MDEV-20377](https://jira.mariadb.org/browse/MDEV-20377): Introduce cmake -DWITH\_MSAN:BOOL=ON
* [Revision #e7fda5db07](https://github.com/MariaDB/server/commit/e7fda5db07)\
  2019-08-19 17:09:06 +0300
  * [MDEV-20377](https://jira.mariadb.org/browse/MDEV-20377): Fix uninitialized memory in mysqltest
* [Revision #dc91372de3](https://github.com/MariaDB/server/commit/dc91372de3)\
  2019-08-16 18:11:32 +0530
  * During ibd file creation, InnoDB flushes the page0 without crypt information. During recovery, InnoDB encounters encrypted page read before initialising the crypt data of the tablespace. So it leads t corruption of page and doesn't allow innodb to start.
* [Revision #fe6eac0cf7](https://github.com/MariaDB/server/commit/fe6eac0cf7)\
  2019-08-16 09:50:54 +0300
  * [MDEV-19200](https://jira.mariadb.org/browse/MDEV-19200): shutdown timeout on innodb.undo\_truncate\_recover
* [Revision #555af003e4](https://github.com/MariaDB/server/commit/555af003e4)\
  2019-08-16 09:54:33 +0300
  * [MDEV-8588](https://jira.mariadb.org/browse/MDEV-8588)/[MDEV-19740](https://jira.mariadb.org/browse/MDEV-19740): Restore a condition
* [Revision #112589cded](https://github.com/MariaDB/server/commit/112589cded)\
  2019-08-15 15:29:32 +0300
  * [MDEV-19740](https://jira.mariadb.org/browse/MDEV-19740): Remove a bogus condition
* [Revision #d07936aaba](https://github.com/MariaDB/server/commit/d07936aaba)\
  2019-08-15 15:29:03 +0300
  * [MDEV-19740](https://jira.mariadb.org/browse/MDEV-19740): Silence a bogus "may be uninitialized" warning
* [Revision #ec28f9532e](https://github.com/MariaDB/server/commit/ec28f9532e)\
  2019-08-15 15:06:27 +0300
  * [MDEV-19740](https://jira.mariadb.org/browse/MDEV-19740): Fix C++11 violations caught by GCC 9.2.1
* [Revision #0b20b9e911](https://github.com/MariaDB/server/commit/0b20b9e911)\
  2019-08-15 12:53:08 +0300
  * Disable galera.query\_cache as it still fails on bb and azure.
* [Revision #29e560cdf3](https://github.com/MariaDB/server/commit/29e560cdf3)\
  2019-08-14 22:53:16 +0530
  * [MDEV-20348](https://jira.mariadb.org/browse/MDEV-20348): DROP TABLE IF EXISTS killed on master but was replicated
* [Revision #2347ffd843](https://github.com/MariaDB/server/commit/2347ffd843)\
  2019-08-09 00:31:35 +0300
  * [MDEV-20301](https://jira.mariadb.org/browse/MDEV-20301) InnoDB's MVCC has O(N^2) behaviors
* [Revision #65296123d0](https://github.com/MariaDB/server/commit/65296123d0)\
  2019-08-13 16:37:21 +0300
  * [MDEV-12439](https://jira.mariadb.org/browse/MDEV-12439): MariaRocks produces numerous (spurious?) valgrind failures
* [Revision #c5b4697b24](https://github.com/MariaDB/server/commit/c5b4697b24)\
  2019-08-13 16:27:51 +0300
  * [MDEV-20315](https://jira.mariadb.org/browse/MDEV-20315): Backport to 10.2: Myrocks: Get the upstream's valgrind suppressions to work
* [Revision #a18d1cc777](https://github.com/MariaDB/server/commit/a18d1cc777)\
  2019-08-13 16:26:17 +0300
  * [MDEV-20315](https://jira.mariadb.org/browse/MDEV-20315): MyRocks tests produce valgrind failures (Backport to 10.2)
* Merge [Revision #ed4ccf34a6](https://github.com/MariaDB/server/commit/ed4ccf34a6) 2019-08-13 13:33:23 +0300 - Merge 10.1 into 10.2
* [Revision #c738aa240e](https://github.com/MariaDB/server/commit/c738aa240e)\
  2019-08-13 12:39:08 +0300
  * [MDEV-20138](https://jira.mariadb.org/browse/MDEV-20138) innodb.trx\_id\_future fails on big-endian
* [Revision #eff898f2a0](https://github.com/MariaDB/server/commit/eff898f2a0)\
  2019-08-13 12:30:36 +0300
  * [MDEV-20335](https://jira.mariadb.org/browse/MDEV-20335): Extra trans\_commit\_stmt after rollback caused by incorrect fix of [MDEV-14401](https://jira.mariadb.org/browse/MDEV-14401)
* [Revision #f13471c9fe](https://github.com/MariaDB/server/commit/f13471c9fe)\
  2019-08-13 13:14:23 +0300
  * [MDEV-20060](https://jira.mariadb.org/browse/MDEV-20060): Remove bogus unit from error message
* [Revision #f25e9aa4ba](https://github.com/MariaDB/server/commit/f25e9aa4ba)\
  2019-08-13 11:37:01 +0300
  * [MDEV-20310](https://jira.mariadb.org/browse/MDEV-20310): Make InnoDB crash tests Valgrind-friendly
* [Revision #5edc4ea4d9](https://github.com/MariaDB/server/commit/5edc4ea4d9)\
  2019-08-13 09:24:31 +0300
  * [MDEV-20324](https://jira.mariadb.org/browse/MDEV-20324): Galera threads are not registered to performance schema
* [Revision #3cee665a04](https://github.com/MariaDB/server/commit/3cee665a04)\
  2019-08-12 13:01:33 +0300
  * [MDEV-17847](https://jira.mariadb.org/browse/MDEV-17847) Galera test failure on MW-328\[A|B|C]
* [Revision #609ea2f37b](https://github.com/MariaDB/server/commit/609ea2f37b)\
  2019-08-12 18:50:54 +0300
  * [MDEV-17614](https://jira.mariadb.org/browse/MDEV-17614): After-merge fix
* Merge [Revision #be33124c9d](https://github.com/MariaDB/server/commit/be33124c9d) 2019-08-12 18:23:42 +0300 - Merge 10.1 into 10.2
* Merge [Revision #15c1ab52a9](https://github.com/MariaDB/server/commit/15c1ab52a9) 2019-08-12 14:46:28 +0300 - Merge 5.5 into 10.1
* [Revision #1217e4a0c0](https://github.com/MariaDB/server/commit/1217e4a0c0)\
  2019-08-12 14:12:32 +0300
  * Fix -Wimplicit-fallthrough
* [Revision #b2a387a3f1](https://github.com/MariaDB/server/commit/b2a387a3f1)\
  2019-08-12 14:05:26 +0300
  * Document TRASH\_FILL, TRASH\_ALLOC, TRASH\_FREE
* [Revision #cabf10b640](https://github.com/MariaDB/server/commit/cabf10b640)\
  2019-07-31 09:53:58 -0400
  * bump the VERSION
* [Revision #7a9e1fcd45](https://github.com/MariaDB/server/commit/7a9e1fcd45)\
  2019-08-12 14:45:28 +0300
  * [MDEV-17614](https://jira.mariadb.org/browse/MDEV-17614): Re-record a result
* [Revision #284c72eacf](https://github.com/MariaDB/server/commit/284c72eacf)\
  2019-07-17 15:56:29 +0530
  * [MDEV-17614](https://jira.mariadb.org/browse/MDEV-17614) INSERT on dup key update is replication unsafe
* [Revision #47f8a18fec](https://github.com/MariaDB/server/commit/47f8a18fec)\
  2019-08-07 12:35:04 +0530
  * [MDEV-20247](https://jira.mariadb.org/browse/MDEV-20247) Replication hangs with "preparing" and never starts
* [Revision #eef7540405](https://github.com/MariaDB/server/commit/eef7540405)\
  2019-08-05 14:34:13 +0530
  * [MDEV-18930](https://jira.mariadb.org/browse/MDEV-18930): Failed CREATE OR REPLACE TEMPORARY not written into binary log makes data on master and slave diverge
* [Revision #319cec959c](https://github.com/MariaDB/server/commit/319cec959c)\
  2019-08-01 15:24:48 +0300
  * [MDEV-17638](https://jira.mariadb.org/browse/MDEV-17638) Improve error message about corruption of encrypted page
* [Revision #f79212f96d](https://github.com/MariaDB/server/commit/f79212f96d)\
  2019-07-31 02:49:15 -0700
  * Fix extra space in mysql-test README
* [Revision #fe8181aca1](https://github.com/MariaDB/server/commit/fe8181aca1)\
  2019-08-12 15:40:57 +0300
  * Fixed issues found by valgrind
* [Revision #3b234104ae](https://github.com/MariaDB/server/commit/3b234104ae)\
  2019-08-10 01:46:50 +0300
  * [MDEV-16955](https://jira.mariadb.org/browse/MDEV-16955): rocksdb\_sys\_vars.rocksdb\_update\_cf\_options\_basic
* [Revision #6765cc6077](https://github.com/MariaDB/server/commit/6765cc6077)\
  2019-08-08 20:10:00 +0300
  * Fixed assertion Assertion \`!table->pos\_in\_locked\_tables' failed
* [Revision #dbac2039e8](https://github.com/MariaDB/server/commit/dbac2039e8)\
  2019-08-08 20:05:40 +0300
  * Fixed some errors & warnings found by clang
* [Revision #5fa2eb6f3d](https://github.com/MariaDB/server/commit/5fa2eb6f3d)\
  2019-08-08 20:03:21 +0300
  * Fixed connect\_debug.test to not depend on system error message
* [Revision #6168f41401](https://github.com/MariaDB/server/commit/6168f41401)\
  2019-08-08 20:02:40 +0300
  * Updated BUILD/compile-pentium64-asan-max
* [Revision #6dca5f6726](https://github.com/MariaDB/server/commit/6dca5f6726)\
  2019-08-08 22:55:35 +0300
  * revert accidental libmariadb change
* [Revision #d39d5dd2bc](https://github.com/MariaDB/server/commit/d39d5dd2bc)\
  2019-07-29 14:12:19 +0300
  * [MDEV-20060](https://jira.mariadb.org/browse/MDEV-20060): Failing assertion: srv\_log\_file\_size <= 512ULL << 30 while preparing backup
* [Revision #88abca55f9](https://github.com/MariaDB/server/commit/88abca55f9)\
  2019-08-06 12:56:16 +0300
  * fix build (-Werror + -Wignored-qualifiers)
* [Revision #a5a7ab1957](https://github.com/MariaDB/server/commit/a5a7ab1957)\
  2019-07-19 18:23:10 +0300
  * Cleanup: this is how to use span
* [Revision #da7d82b8ea](https://github.com/MariaDB/server/commit/da7d82b8ea)\
  2019-07-19 18:22:22 +0300
  * [MDEV-20103](https://jira.mariadb.org/browse/MDEV-20103) add a class similar to std::span
* [Revision #988ff90256](https://github.com/MariaDB/server/commit/988ff90256)\
  2019-08-04 23:37:47 +0300
  * [MDEV-20227](https://jira.mariadb.org/browse/MDEV-20227): rocksdb.rocksdb\_concurrent\_delete fails on windows
* [Revision #09a85692a6](https://github.com/MariaDB/server/commit/09a85692a6)\
  2019-08-03 23:15:44 +0300
  * Post-merge fixes for rocksdb.group\_min\_max test
* [Revision #05b35cf4c1](https://github.com/MariaDB/server/commit/05b35cf4c1)\
  2019-07-31 09:57:31 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
