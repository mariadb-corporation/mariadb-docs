# MariaDB 10.2.28 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

After an upgrade MariaDB Server can crash if InnoDB tables exist with a `FULLTEXT INDEX` and a `FOREIGN KEY` constraint attached to them. We got reports that the crash already will be encountered on startup, but a crash is also possible at a later stage. See [MDEV-20987](https://jira.mariadb.org/browse/MDEV-20987) for more details.**Do not download or use this release.**

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.2/10.2.28.md)[Changelog](mariadb-10228-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.2.28/)

**Release date:** 5 Nov 2019

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.28.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* Includes all fixes from [MariaDB 10.1.42](../changelogs-mariadb-101-series/mariadb-10142-changelog.md)
* [Revision #1552b254a0](https://github.com/MariaDB/server/commit/1552b254a0)\
  2019-10-31 20:42:08 +0200
  * List of unstable tests for 10.2.28 release
* Merge [Revision #259edb1f60](https://github.com/MariaDB/server/commit/259edb1f60) 2019-10-31 09:07:26 +0100 - Merge branch '10.1' into 10.2
* [Revision #2ba9a269df](https://github.com/MariaDB/server/commit/2ba9a269df)\
  2019-10-31 06:13:38 +0100
  * new CC 3.1 due to typo in it
* Merge [Revision #fd6dfb3b54](https://github.com/MariaDB/server/commit/fd6dfb3b54) 2019-10-30 23:38:05 +0100 - Merge branch 'github/10.1' into 10.2
* Merge [Revision #6680b04961](https://github.com/MariaDB/server/commit/6680b04961) 2019-10-30 21:56:35 +0100 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #a00b713130](https://github.com/MariaDB/server/commit/a00b713130)\
  2019-10-16 22:12:47 +0200
  * Fix wrong second parameter in snprintf
* [Revision #b56589eaf2](https://github.com/MariaDB/server/commit/b56589eaf2)\
  2019-10-16 17:40:49 +0200
  * Fix unhandled throws, add some trace + typo
* [Revision #425dc6d66f](https://github.com/MariaDB/server/commit/425dc6d66f)\
  2019-09-10 15:57:48 +0200
  * Remove some incorrect compile flags Just keep the /MDd flag but only for Windows Debug REST compile
* [Revision #baaf02a48b](https://github.com/MariaDB/server/commit/baaf02a48b)\
  2019-10-30 21:37:46 +0100
  * new CC 3.1
* Merge [Revision #36f67a7dff](https://github.com/MariaDB/server/commit/36f67a7dff) 2019-10-30 21:33:01 +0100 - Merge branch '10.1' into 10.2
* [Revision #cd1c10859d](https://github.com/MariaDB/server/commit/cd1c10859d)\
  2019-10-29 13:13:31 +0200
  * Fix test cases that use debug galera library.
* [Revision #36a9694378](https://github.com/MariaDB/server/commit/36a9694378)\
  2019-10-29 13:11:34 +0200
  * [MDEV-18562](https://jira.mariadb.org/browse/MDEV-18562) - InnoDB: WSREP: referenced FK check fail: Lock wait index
* [Revision #44b0c86971](https://github.com/MariaDB/server/commit/44b0c86971)\
  2019-10-30 06:42:51 +0200
  * Clean up ut\_strlcpy(), ut\_strlcpy\_rev()
* [Revision #814534745b](https://github.com/MariaDB/server/commit/814534745b)\
  2019-10-29 17:11:34 +0200
  * [MDEV-20917](https://jira.mariadb.org/browse/MDEV-20917) InnoDB is passing NULL to nonnull function parameters
* [Revision #2d82ae5ba3](https://github.com/MariaDB/server/commit/2d82ae5ba3)\
  2019-10-28 17:01:32 +0000
  * [MDEV-20825](https://jira.mariadb.org/browse/MDEV-20825) : Innodb does not start if GetDiskFreeSpace() fails.
* [Revision #c13519312b](https://github.com/MariaDB/server/commit/c13519312b)\
  2019-10-25 17:17:32 +0200
  * [MDEV-20799](https://jira.mariadb.org/browse/MDEV-20799) DROP Virtual Column crashes MariaDB
* [Revision #8bb6b9c634](https://github.com/MariaDB/server/commit/8bb6b9c634)\
  2019-09-18 14:00:32 +0200
  * gis2 test no longer exists after 3fe38574fbdd
* [Revision #c075c7a861](https://github.com/MariaDB/server/commit/c075c7a861)\
  2019-09-10 17:31:10 +0200
  * [MDEV-20549](https://jira.mariadb.org/browse/MDEV-20549) SQL SECURITY DEFINER does not work for INFORMATION\_SCHEMA tables
* [Revision #be780c0555](https://github.com/MariaDB/server/commit/be780c0555)\
  2019-09-10 19:15:32 +0200
  * fix CONNECT engine to issue the correct error message
* [Revision #42ada91542](https://github.com/MariaDB/server/commit/42ada91542)\
  2019-09-10 17:24:34 +0200
  * cleanup: RAII helper for swapping of thd->security\_ctx
* Merge [Revision #d752a97ebb](https://github.com/MariaDB/server/commit/d752a97ebb) 2019-10-25 17:33:39 +0300 - Merge 10.1 to 10.2
* Merge [Revision #19ceaf2928](https://github.com/MariaDB/server/commit/19ceaf2928) 2019-10-25 12:57:36 +0300 - Merge 10.1 into 10.2
* [Revision #7457181ba4](https://github.com/MariaDB/server/commit/7457181ba4)\
  2019-10-24 21:20:53 +0300
  * Clean up innodb.innodb\_stats\_persistent
* [Revision #2809842031](https://github.com/MariaDB/server/commit/2809842031)\
  2019-10-19 15:16:47 +0300
  * [MDEV-20864](https://jira.mariadb.org/browse/MDEV-20864) Introduce debug option innodb\_change\_buffer\_dump
* [Revision #fa929f7cdf](https://github.com/MariaDB/server/commit/fa929f7cdf)\
  2019-10-17 17:12:23 +0300
  * Simplify row\_undo\_ins\_remove\_sec\_low()
* Merge [Revision #b027830232](https://github.com/MariaDB/server/commit/b027830232) 2019-10-17 17:08:58 +0300 - [MDEV-20850](https://jira.mariadb.org/browse/MDEV-20850) Merge new release of InnoDB 5.7.28 to 10.2
* [Revision #fa32d28f2f](https://github.com/MariaDB/server/commit/fa32d28f2f)\
  2019-10-17 13:58:04 +0300
  * [MDEV-20852](https://jira.mariadb.org/browse/MDEV-20852) BtrBulk is unnecessarily holding dict\_index\_t::lock
* [Revision #3ce14a66ef](https://github.com/MariaDB/server/commit/3ce14a66ef)\
  2019-10-16 18:40:31 +0300
  * Fixed bug in lock tables + alter table with Aria tables.
* [Revision #7952f7720f](https://github.com/MariaDB/server/commit/7952f7720f)\
  2019-10-15 20:26:40 +0300
  * [MDEV-10748](https://jira.mariadb.org/browse/MDEV-10748) Server crashes in ha\_maria::implicit\_commit
* [Revision #4d14785546](https://github.com/MariaDB/server/commit/4d14785546)\
  2019-10-09 03:09:48 +0300
  * [MDEV-20778](https://jira.mariadb.org/browse/MDEV-20778) UBSAN: call to function free\_rpl\_filter() through pointer to incorrect function type
* [Revision #f989c0ce66](https://github.com/MariaDB/server/commit/f989c0ce66)\
  2019-10-14 17:26:21 +0300
  * [MDEV-20813](https://jira.mariadb.org/browse/MDEV-20813): Do not rotate keys for unallocated pages
* Merge [Revision #4f9f3f19cd](https://github.com/MariaDB/server/commit/4f9f3f19cd) 2019-10-14 16:53:57 +0300 - Merge 10.1 into 10.2
* [Revision #361e8284f3](https://github.com/MariaDB/server/commit/361e8284f3)\
  2019-10-12 15:28:55 +0300
  * [MDEV-20813](https://jira.mariadb.org/browse/MDEV-20813) Assertion failure in buf\_flush\_init\_for\_writing() for innodb\_immediate\_scrub\_data\_uncompressed=ON
* Merge [Revision #2227dec45e](https://github.com/MariaDB/server/commit/2227dec45e) 2019-10-12 06:10:41 +0300 - Merge 10.1 into 10.2
* [Revision #4ca0abe964](https://github.com/MariaDB/server/commit/4ca0abe964)\
  2019-10-07 12:34:08 +0200
  * [MDEV-20728](https://jira.mariadb.org/browse/MDEV-20728): /usr/sbin/mysqld: unknown variable 'defaults-group-suffix=mysqld1
* [Revision #38736928e7](https://github.com/MariaDB/server/commit/38736928e7)\
  2019-10-11 21:26:16 +0300
  * Fix -std=c++98 -Wzero-length-array
* [Revision #1e1b53ccfd](https://github.com/MariaDB/server/commit/1e1b53ccfd)\
  2019-10-11 21:24:48 +0300
  * After-merge fix: Correct an assertion
* Merge [Revision #966d97b5f9](https://github.com/MariaDB/server/commit/966d97b5f9) 2019-10-11 18:38:18 +0300 - Merge 10.1 into 10.2
* [Revision #1fd1ef25c2](https://github.com/MariaDB/server/commit/1fd1ef25c2)\
  2019-10-11 18:36:08 +0300
  * Fix CMAKE\_BUILD\_TYPE=Debug
* [Revision #350e46a8b5](https://github.com/MariaDB/server/commit/350e46a8b5)\
  2019-07-30 22:39:55 +1000
  * [MDEV-18546](https://jira.mariadb.org/browse/MDEV-18546) ASAN heap-use-after-free in innobase\_get\_computed\_value / row\_purge
* [Revision #b393e2cb0c](https://github.com/MariaDB/server/commit/b393e2cb0c)\
  2019-07-25 22:17:04 +1000
  * add innodb\_debug\_sync var to support DEBUG\_SYNC from purge threads
* [Revision #6d7a826953](https://github.com/MariaDB/server/commit/6d7a826953)\
  2019-10-10 20:29:30 +0300
  * [MDEV-20788](https://jira.mariadb.org/browse/MDEV-20788): Bogus assertion failure for PAGE\_FREE list
* [Revision #726b1998fc](https://github.com/MariaDB/server/commit/726b1998fc)\
  2019-10-10 10:25:32 +0300
  * Fixed feedback\_plugin\_load to work with staticly loaded plugin
* [Revision #6fde0073bf](https://github.com/MariaDB/server/commit/6fde0073bf)\
  2019-10-09 18:47:14 +0300
  * Rename log\_make\_checkpoint\_at() to log\_make\_checkpoint()
* [Revision #c65cb244b3](https://github.com/MariaDB/server/commit/c65cb244b3)\
  2019-10-03 18:12:08 +0530
  * [MDEV-19335](https://jira.mariadb.org/browse/MDEV-19335) Remove buf\_page\_t::encrypted
* Merge [Revision #24232ec12c](https://github.com/MariaDB/server/commit/24232ec12c) 2019-10-09 08:30:23 +0300 - Merge 10.1 into 10.2
* [Revision #ed0793e096](https://github.com/MariaDB/server/commit/ed0793e096)\
  2019-10-02 22:47:45 +0300
  * [MDEV-19783](https://jira.mariadb.org/browse/MDEV-19783): Add more REC\_INFO\_MIN\_REC\_FLAG checks
* [Revision #99dc40d6ac](https://github.com/MariaDB/server/commit/99dc40d6ac)\
  2019-09-30 20:58:50 +0300
  * [MDEV-19783](https://jira.mariadb.org/browse/MDEV-19783) Random crashes and corrupt data in INSTANT-added columns
* [Revision #d480d28f4f](https://github.com/MariaDB/server/commit/d480d28f4f)\
  2019-10-08 18:18:48 +0300
  * Add page\_has\_prev(), page\_has\_next(), page\_has\_siblings()
* [Revision #27664ef29d](https://github.com/MariaDB/server/commit/27664ef29d)\
  2019-09-26 15:05:55 +0530
  * [MDEV-20574](https://jira.mariadb.org/browse/MDEV-20574) Position of events reported by mysqlbinlog is wrong with encrypted binlogs, SHOW BINLOG EVENTS reports the correct one.
* [Revision #13535b2713](https://github.com/MariaDB/server/commit/13535b2713)\
  2019-09-30 09:08:17 +0200
  * Fix problem with warnings of new compilers.
* [Revision #5e65c67cfc](https://github.com/MariaDB/server/commit/5e65c67cfc)\
  2019-10-03 17:45:36 +0300
  * fix clang warning
* [Revision #edda2fd149](https://github.com/MariaDB/server/commit/edda2fd149)\
  2019-10-01 03:23:33 +0300
  * [MDEV-20703](https://jira.mariadb.org/browse/MDEV-20703): mariadb-backup creates binlog files in server binlog directory on --prepare --export step
* Merge [Revision #f203245e9e](https://github.com/MariaDB/server/commit/f203245e9e) 2019-10-01 06:10:19 +0400 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #576a5f091e](https://github.com/MariaDB/server/commit/576a5f091e)\
  2019-09-24 16:20:59 +0300
  * [MDEV-20647](https://jira.mariadb.org/browse/MDEV-20647) Fix and enable SphinxSE tests
* [Revision #46b785262b](https://github.com/MariaDB/server/commit/46b785262b)\
  2019-09-30 12:48:26 +0300
  * Fix -Wunused for CMAKE\_BUILD\_TYPE=RelWithDebInfo
* [Revision #bc70862e13](https://github.com/MariaDB/server/commit/bc70862e13)\
  2019-09-25 14:00:39 +0200
  * [MDEV-20614](https://jira.mariadb.org/browse/MDEV-20614): Syntax error, and option put in wrong place
* [Revision #c76873f23d](https://github.com/MariaDB/server/commit/c76873f23d)\
  2019-09-27 17:46:10 +0530
  * [MDEV-20688](https://jira.mariadb.org/browse/MDEV-20688) Recovery crashes after unnecessarily reading a corrupted page
* [Revision #d874cdeccc](https://github.com/MariaDB/server/commit/d874cdeccc)\
  2019-09-27 14:29:22 +0300
  * dict\_load\_table(): Remove constant parameter cached=true
* [Revision #718fcee0a3](https://github.com/MariaDB/server/commit/718fcee0a3)\
  2019-09-27 14:22:59 +0300
  * Reduce rw\_lock\_debug\_mutex contention
* [Revision #4ec0c346b8](https://github.com/MariaDB/server/commit/4ec0c346b8)\
  2019-09-27 13:58:01 +0300
  * Remove a useless large test, and add a debug assertion
* [Revision #ca9e0089d5](https://github.com/MariaDB/server/commit/ca9e0089d5)\
  2019-09-27 10:43:23 +0300
  * [MDEV-19740](https://jira.mariadb.org/browse/MDEV-19740): Fix GCC 9.2.1 -Wmaybe-uninitialized on AMD64
* [Revision #2d6719d7ee](https://github.com/MariaDB/server/commit/2d6719d7ee)\
  2019-09-26 12:48:55 +0300
  * [MDEV-19514](https://jira.mariadb.org/browse/MDEV-19514) preparation: Extend innodb.innodb-change-buffer-recovery
* [Revision #23d675453f](https://github.com/MariaDB/server/commit/23d675453f)\
  2019-09-26 12:44:04 +0300
  * [MDEV-20675](https://jira.mariadb.org/browse/MDEV-20675) Crash in SHOW ENGINE INNODB STATUS with innodb\_force\_recovery=5
* Merge [Revision #574ff87f2a](https://github.com/MariaDB/server/commit/574ff87f2a) 2019-09-26 12:36:01 +0300 - Merge 10.1 into 10.2
* [Revision #102bc7beb0](https://github.com/MariaDB/server/commit/102bc7beb0)\
  2019-09-24 19:24:32 +0400
  * Fixing tests according to [MDEV-20655](https://jira.mariadb.org/browse/MDEV-20655) maturity stable for user\_variables
* Merge [Revision #0a359d7627](https://github.com/MariaDB/server/commit/0a359d7627) 2019-09-24 19:19:25 +0400 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #fa9e012a34](https://github.com/MariaDB/server/commit/fa9e012a34)\
  2019-09-24 14:37:01 +0300
  * [MDEV-20655](https://jira.mariadb.org/browse/MDEV-20655) maturity stable for user\_variables
* [Revision #ef701bfd07](https://github.com/MariaDB/server/commit/ef701bfd07)\
  2019-09-24 13:29:23 +0300
  * Remove the unused function btr\_page\_get()
* [Revision #ab9f378b0b](https://github.com/MariaDB/server/commit/ab9f378b0b)\
  2019-09-23 13:47:52 +0530
  * Backporting 273d8eb12c40a6dcd05a8148bdfba3f1fd96e764 Proper fix for disabling warnings in read\_statistics\_for\_table()
* [Revision #2931fd2917](https://github.com/MariaDB/server/commit/2931fd2917)\
  2019-09-23 09:04:51 +0300
  * After-merge fix: Adjust a result
* [Revision #60cb5559a9](https://github.com/MariaDB/server/commit/60cb5559a9)\
  2019-09-23 08:29:39 +0300
  * [MDEV-17614](https://jira.mariadb.org/browse/MDEV-17614) post-fix: Remove dead dup\_chk\_only=true code.
* Merge [Revision #44c5144943](https://github.com/MariaDB/server/commit/44c5144943) 2019-09-23 08:26:08 +0300 - Merge 10.1 into 10.2
* [Revision #1ad79c8187](https://github.com/MariaDB/server/commit/1ad79c8187)\
  2019-06-18 06:58:41 -0700
  * [MDEV-19679](https://jira.mariadb.org/browse/MDEV-19679) - CREATE SERVER needs tweaks for compatibility with CONNECT engine
* [Revision #fd5cd073cc](https://github.com/MariaDB/server/commit/fd5cd073cc)\
  2019-05-08 06:40:37 -0700
  * MDEV 19205 Sphinx unable to connect using a host name
* [Revision #9611d7e08a](https://github.com/MariaDB/server/commit/9611d7e08a)\
  2018-01-03 11:27:20 +0100
  * Fix
* [Revision #75bcf1f9ad](https://github.com/MariaDB/server/commit/75bcf1f9ad)\
  2017-05-08 16:36:37 +1000
  * [MDEV-12646](https://jira.mariadb.org/browse/MDEV-12646): systemd service file changes from Fedora
* [Revision #4afe9d4b6d](https://github.com/MariaDB/server/commit/4afe9d4b6d)\
  2019-09-20 08:30:31 +0300
  * [MDEV-16222](https://jira.mariadb.org/browse/MDEV-16222): Move the test to gcol.innodb\_virtual\_debug\_purge
* [Revision #c0db3fe6da](https://github.com/MariaDB/server/commit/c0db3fe6da)\
  2019-05-27 13:52:27 +0200
  * [MDEV-18438](https://jira.mariadb.org/browse/MDEV-18438) Don't stream xtrabackup\_info of extra-lsndir
* [Revision #f94d9ab9f8](https://github.com/MariaDB/server/commit/f94d9ab9f8)\
  2019-09-18 20:19:03 +0530
  * [MDEV-20483](https://jira.mariadb.org/browse/MDEV-20483) Follow-up fix
* [Revision #b3a7c07eae](https://github.com/MariaDB/server/commit/b3a7c07eae)\
  2019-09-18 16:50:46 +0300
  * Enable galera.MW-286 test case.
* Merge [Revision #bb4214272a](https://github.com/MariaDB/server/commit/bb4214272a) 2019-09-18 16:24:48 +0300 - Merge 10.1 into 10.2
* [Revision #24859049c6](https://github.com/MariaDB/server/commit/24859049c6)\
  2019-09-18 16:04:43 +0300
  * [MDEV-20485](https://jira.mariadb.org/browse/MDEV-20485): Disable galera.galera\_var\_node\_address
* [Revision #a624b99f91](https://github.com/MariaDB/server/commit/a624b99f91)\
  2019-09-18 12:17:09 +0300
  * Remove an unused declaration
* [Revision #273d8eb12c](https://github.com/MariaDB/server/commit/273d8eb12c)\
  2019-09-18 01:59:29 +0530
  * [MDEV-20589](https://jira.mariadb.org/browse/MDEV-20589): Server still crashes in Field::set\_warning\_truncated\_wrong\_value
* [Revision #c471bfb34e](https://github.com/MariaDB/server/commit/c471bfb34e)\
  2019-09-18 01:44:36 +0530
  * Fixing a test to reset to original state
* [Revision #fb3e3a6a3d](https://github.com/MariaDB/server/commit/fb3e3a6a3d)\
  2019-09-17 19:54:15 +0530
  * [MDEV-20483](https://jira.mariadb.org/browse/MDEV-20483) trx\_lock\_t::table\_locks is not a subset of trx\_lock\_t::trx\_locks
* [Revision #2a98d0b5ca](https://github.com/MariaDB/server/commit/2a98d0b5ca)\
  2019-09-14 12:14:20 +0300
  * Fix #2 for galera.MW-336
* [Revision #23657a2101](https://github.com/MariaDB/server/commit/23657a2101)\
  2019-09-13 17:07:58 +0300
  * [MDEV-13893](https://jira.mariadb.org/browse/MDEV-13893)/[MDEV-12699](https://jira.mariadb.org/browse/MDEV-12699): Enable encryption.innodb-redo-badkey
* [Revision #3793da44cf](https://github.com/MariaDB/server/commit/3793da44cf)\
  2018-04-16 20:49:27 +0000
  * Enable the auto parameter of the flag `default-character-set`
* [Revision #3422c13ab7](https://github.com/MariaDB/server/commit/3422c13ab7)\
  2019-09-11 14:15:17 +0300
  * Try to fix galera.MW-336 test case.
* [Revision #40beeb1402](https://github.com/MariaDB/server/commit/40beeb1402)\
  2019-09-13 09:18:11 +0300
  * [MDEV-20561](https://jira.mariadb.org/browse/MDEV-20561) Galera node shutdown fails in non-Primary (#1386)
* [Revision #99ecb33389](https://github.com/MariaDB/server/commit/99ecb33389)\
  2019-09-12 15:15:33 +0200
  * [MDEV-20570](https://jira.mariadb.org/browse/MDEV-20570) : Packaging fails "The specified timestamp server either could not be reached"
* [Revision #be6beb73e9](https://github.com/MariaDB/server/commit/be6beb73e9)\
  2019-09-11 23:05:12 +0300
  * [MDEV-16560](https://jira.mariadb.org/browse/MDEV-16560): \[counter] rocksdb.ttl\_secondary\_read\_filtering fail in buildbot
* [Revision #c8dc866fde](https://github.com/MariaDB/server/commit/c8dc866fde)\
  2019-09-10 23:51:42 +0300
  * [MDEV-20371](https://jira.mariadb.org/browse/MDEV-20371): Invalid reads at plan refinement stage: join->positions...
* [Revision #863a951731](https://github.com/MariaDB/server/commit/863a951731)\
  2019-09-11 09:11:58 -0400
  * bump the VERSION
* [Revision #0f950e53f0](https://github.com/MariaDB/server/commit/0f950e53f0)\
  2019-09-11 15:08:32 +0300
  * [MDEV-20562](https://jira.mariadb.org/browse/MDEV-20562) btr\_cur\_open\_at\_rnd\_pos() fails to return error for corrupted page
* [Revision #df4dee4b84](https://github.com/MariaDB/server/commit/df4dee4b84)\
  2019-09-11 16:02:41 +0530
  * [MDEV-17939](https://jira.mariadb.org/browse/MDEV-17939) Assertion \`++loop\_count < 2' failed in trx\_undo\_report\_rename
* Merge [Revision #f7fe51f126](https://github.com/MariaDB/server/commit/f7fe51f126) 2019-09-11 08:48:00 +0300 - Merge 10.1 into 10.2
* [Revision #5ec4efb7b1](https://github.com/MariaDB/server/commit/5ec4efb7b1)\
  2019-09-11 04:44:24 +0400
  * Adding missing semicolons to sql\_yacc.yy (10.2)
* [Revision #acf0f2d592](https://github.com/MariaDB/server/commit/acf0f2d592)\
  2019-09-10 14:54:31 +0300
  * [MDEV-20143](https://jira.mariadb.org/browse/MDEV-20143) innodb.innodb-virtual-columns-debug failed in buildbot with wrong result
* [Revision #879c9ddce7](https://github.com/MariaDB/server/commit/879c9ddce7)\
  2019-09-09 19:57:25 +0200
  * [MDEV-20542](https://jira.mariadb.org/browse/MDEV-20542) Windows enable/d2OptimizeHugeFunctions
* [Revision #43a6e81ccb](https://github.com/MariaDB/server/commit/43a6e81ccb)\
  2019-09-09 18:18:52 +0300
  * [MDEV-19514](https://jira.mariadb.org/browse/MDEV-19514) preparation: Remove innodb\_change\_buffering\_debug=2
* [Revision #2336e0b394](https://github.com/MariaDB/server/commit/2336e0b394)\
  2019-09-09 13:48:36 +0200
  * [MDEV-20206](https://jira.mariadb.org/browse/MDEV-20206) : Crash inside timer\_callback()\[threadpool\_win.cc:419]
* [Revision #a895c68c58](https://github.com/MariaDB/server/commit/a895c68c58)\
  2019-09-09 12:08:47 +0200
  * On Windows, treat linker warnings as errors, if MYSQL\_MAINTAINER\_MODE is ERR
* [Revision #d251b76884](https://github.com/MariaDB/server/commit/d251b76884)\
  2019-09-09 12:07:47 +0200
  * Fix warning when compiling with OpenSSL.
* [Revision #7e7b6ec4d6](https://github.com/MariaDB/server/commit/7e7b6ec4d6)\
  2019-09-09 12:06:29 +0200
  * Fix connect RESTSDK support.
* [Revision #803bb5cdf8](https://github.com/MariaDB/server/commit/803bb5cdf8)\
  2019-09-09 10:51:10 +0200
  * Windows, cmake : Fix occasional link error when switching between debug to optimized compilation
* [Revision #0fd5b11eb0](https://github.com/MariaDB/server/commit/0fd5b11eb0)\
  2019-09-06 14:54:22 +0300
  * [MDEV-20511](https://jira.mariadb.org/browse/MDEV-20511): Galera replication of events is not consistent
* [Revision #efbfded563](https://github.com/MariaDB/server/commit/efbfded563)\
  2019-09-05 12:26:36 +0300
  * Move MW-328B to big test to avoid test timeout.
* [Revision #caa7bb62f6](https://github.com/MariaDB/server/commit/caa7bb62f6)\
  2019-09-04 09:21:07 +0300
  * [MDEV-20485](https://jira.mariadb.org/browse/MDEV-20485): Galera test failure on galera.galera\_var\_node\_address
* [Revision #b8b4b6594e](https://github.com/MariaDB/server/commit/b8b4b6594e)\
  2019-09-05 07:43:57 +0300
  * [MDEV-19926](https://jira.mariadb.org/browse/MDEV-19926): Galera SST tests fail
* [Revision #7591a24fa6](https://github.com/MariaDB/server/commit/7591a24fa6)\
  2019-09-09 13:06:33 +0300
  * [MDEV-20531](https://jira.mariadb.org/browse/MDEV-20531): innodb.temporary\_table\_optimisation fails

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
