# MariaDB 10.5.3 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download](https://downloads.mariadb.org/mariadb/10.5.3)[Release Notes](../../old-releases/10.5/10.5.3.md)[Changelog](mariadb-1053-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 12 May 2020

**Do not use non-stable (non-GA) releases in production!**

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.3.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.13](../changelogs-mariadb-10-4-series/mariadb-10413-changelog.md)
* [Revision #173adeaff4](https://github.com/MariaDB/server/commit/173adeaff4)\
  2020-05-11 16:09:30 +0200
  * 10.5 becomes gamma/RC
* Merge [Revision #13038e4705](https://github.com/MariaDB/server/commit/13038e4705) 2020-05-09 20:43:36 +0200 - Merge branch '10.4' into 10.5
* [Revision #72c7b4eb4c](https://github.com/MariaDB/server/commit/72c7b4eb4c)\
  2020-05-08 18:31:34 +0300
  * [MDEV-16678](https://jira.mariadb.org/browse/MDEV-16678) fixup: Remove orphaned DBUG\_EXECUTE\_IF
* [Revision #4a5be2e94e](https://github.com/MariaDB/server/commit/4a5be2e94e)\
  2020-05-07 17:57:03 +0300
  * [MDEV-22495](https://jira.mariadb.org/browse/MDEV-22495) Assertion ...status != buf\_page\_t::FREED in ibuf\_read\_merge\_pages()
* [Revision #18a62eb76d](https://github.com/MariaDB/server/commit/18a62eb76d)\
  2020-05-07 17:15:34 +0300
  * [MDEV-21133](https://jira.mariadb.org/browse/MDEV-21133) follow-up: Use fil\_page\_get\_type()
* [Revision #ba573c4736](https://github.com/MariaDB/server/commit/ba573c4736)\
  2020-05-07 12:25:00 +0300
  * [MDEV-21133](https://jira.mariadb.org/browse/MDEV-21133) follow-up: More my\_assume\_aligned hints
* [Revision #0781c91d28](https://github.com/MariaDB/server/commit/0781c91d28)\
  2020-05-06 15:32:31 +0300
  * Fix test case failure on galera\_vote\_rejoin\_dml
* [Revision #91734431ba](https://github.com/MariaDB/server/commit/91734431ba)\
  2020-05-01 20:32:33 +0400
  * Move all thread cache specific code to a new class
* [Revision #8ad3c6154b](https://github.com/MariaDB/server/commit/8ad3c6154b)\
  2020-05-06 13:19:35 +0400
  * [MDEV-22130](https://jira.mariadb.org/browse/MDEV-22130) SHOW WARNINGS will SIGSEGV 10.5 optimized build after setting CHARACTER\_SET\_RESULTS to NULL and running any invalid SQL | Binary\_string::copy\_printable\_hhhh
* Merge [Revision #7bcaa541aa](https://github.com/MariaDB/server/commit/7bcaa541aa) 2020-05-05 21:16:22 +0300 - Merge 10.4 into 10.5
* [Revision #36b8ac2c0d](https://github.com/MariaDB/server/commit/36b8ac2c0d)\
  2020-05-05 13:24:58 +0300
  * remove double std::map lookup
* [Revision #937dfb74cb](https://github.com/MariaDB/server/commit/937dfb74cb)\
  2020-05-04 11:32:08 +0200
  * [MDEV-22424](https://jira.mariadb.org/browse/MDEV-22424) Server crashes in handler::check\_duplicate\_long\_entry\_key or Assertion \`inited == NONE || lookup\_handler != this' failed upon DELETE FOR PORTION on table with long unique key
* [Revision #18502f99eb](https://github.com/MariaDB/server/commit/18502f99eb)\
  2020-05-04 10:48:39 +0200
  * [MDEV-22185](https://jira.mariadb.org/browse/MDEV-22185) Failing assertion: node->pcur->rel\_pos == BTR\_PCUR\_ON or ER\_KEY\_NOT\_FOUND or Assertion \`inited==NONE' failed in handler::ha\_index\_init
* [Revision #67aaf51cf9](https://github.com/MariaDB/server/commit/67aaf51cf9)\
  2020-04-19 19:47:31 +0200
  * cleanup: ha\_external\_unlock() helper
* [Revision #f29287d280](https://github.com/MariaDB/server/commit/f29287d280)\
  2020-05-05 18:18:35 +0200
  * Update README
* [Revision #89ff4176c1](https://github.com/MariaDB/server/commit/89ff4176c1)\
  2020-04-30 20:06:26 +0300
  * [MDEV-22437](https://jira.mariadb.org/browse/MDEV-22437) make THR\_THD\* variable thread\_local
* [Revision #90aad47dd9](https://github.com/MariaDB/server/commit/90aad47dd9)\
  2020-05-05 22:41:10 +0900
  * [MDEV-20502](https://jira.mariadb.org/browse/MDEV-20502) Queries against spider tables return wrong values for columns following constant declarations.
* [Revision #af09ce55eb](https://github.com/MariaDB/server/commit/af09ce55eb)\
  2020-05-05 12:59:15 +0200
  * Fix for galera\_3nodes\_sr/suite.pm (#1526)
* [Revision #64488a6f2d](https://github.com/MariaDB/server/commit/64488a6f2d)\
  2020-05-05 07:06:37 +0300
  * Cleanup: Remove global functions or redundant parameters
* Merge [Revision #97261cbb7a](https://github.com/MariaDB/server/commit/97261cbb7a) 2020-05-04 22:07:18 +0300 - Merge 10.4 into 10.5
* Merge [Revision #4337a3b5f9](https://github.com/MariaDB/server/commit/4337a3b5f9) 2020-05-04 18:43:00 +0300 - Merge 10.4 into 10.5
* [Revision #d50f776930](https://github.com/MariaDB/server/commit/d50f776930)\
  2020-05-04 14:17:06 +0200
  * [MDEV-22454](https://jira.mariadb.org/browse/MDEV-22454)\
    Allow -DCMAKE\_INTERPROCEDURAL\_OPTIMIZATION=ON
* [Revision #f544a712c8](https://github.com/MariaDB/server/commit/f544a712c8)\
  2020-04-30 10:33:54 +0300
  * Cleanup: Reduce que\_thr\_t, que\_fork\_t, trx\_lock\_t size
* [Revision #77e1b0c397](https://github.com/MariaDB/server/commit/77e1b0c397)\
  2020-04-29 21:35:17 +0530
  * [MDEV-22317](https://jira.mariadb.org/browse/MDEV-22317): SIGSEGV in my\_free/delete\_dynamic in optimized builds (ARIA)
* [Revision #89aebdf964](https://github.com/MariaDB/server/commit/89aebdf964)\
  2020-04-29 21:03:45 +0300
  * [MDEV-22337](https://jira.mariadb.org/browse/MDEV-22337): Fix type mismatch
* [Revision #3e6722d88d](https://github.com/MariaDB/server/commit/3e6722d88d)\
  2020-04-29 16:00:17 +0300
  * Cleanup: More trx\_t member functions
* Merge [Revision #496d0372ef](https://github.com/MariaDB/server/commit/496d0372ef) 2020-04-29 15:40:51 +0300 - Merge 10.4 into 10.5
* [Revision #d4da131cff](https://github.com/MariaDB/server/commit/d4da131cff)\
  2020-04-29 11:40:14 +0400
  * [MDEV-22337](https://jira.mariadb.org/browse/MDEV-22337) Assertion \`Alloced\_length >= (str\_length + length + net\_le… …ngth\_size(length))' failed in Binary\_string::q\_net\_store\_data on long MULTIPOLYGON query with session\_track\_user\_variables=1 (optimized builds).
* [Revision #ffc5e00e9c](https://github.com/MariaDB/server/commit/ffc5e00e9c)\
  2020-04-29 10:35:49 +0400
  * [MDEV-21915](https://jira.mariadb.org/browse/MDEV-21915) Server crashes in copy\_fields,Item\_func\_group\_concat::add …
* [Revision #2e6b21be4a](https://github.com/MariaDB/server/commit/2e6b21be4a)\
  2020-04-28 14:47:53 +0530
  * [MDEV-22317](https://jira.mariadb.org/browse/MDEV-22317): SIGSEGV in my\_free/delete\_dynamic in optimized builds (ARIA)
* [Revision #5193c1b542](https://github.com/MariaDB/server/commit/5193c1b542)\
  2020-04-28 19:22:44 +0530
  * [MDEV-22369](https://jira.mariadb.org/browse/MDEV-22369) Assertion \`err == DB\_SUCCESS' failed. in btr\_block\_get\_func during crash recovery
* [Revision #25cb2b373c](https://github.com/MariaDB/server/commit/25cb2b373c)\
  2020-04-28 16:20:24 +0300
  * [MDEV-22128](https://jira.mariadb.org/browse/MDEV-22128) : Server with wsrep\_on crashes in do\_rename upon RENAME TABLE on a view
* [Revision #e545a60bf4](https://github.com/MariaDB/server/commit/e545a60bf4)\
  2020-04-28 16:08:18 +0400
  * [MDEV-22236](https://jira.mariadb.org/browse/MDEV-22236) JSON\_ARRAYAGG query leads to SIGSEGV in Charset::swap on optimized builds.
* [Revision #0cd2b4c249](https://github.com/MariaDB/server/commit/0cd2b4c249)\
  2020-04-07 12:22:57 +0300
  * [MDEV-22177](https://jira.mariadb.org/browse/MDEV-22177) more fsync() -> fdatasync() in InnoDB
* [Revision #9bd98f450c](https://github.com/MariaDB/server/commit/9bd98f450c)\
  2020-04-27 18:19:07 +0300
  * Compilation fix
* [Revision #73aa78ea9d](https://github.com/MariaDB/server/commit/73aa78ea9d)\
  2020-04-27 16:36:03 +0300
  * [MDEV-22155](https://jira.mariadb.org/browse/MDEV-22155) ALTER add default history partitions name clash on non-default partitions
* [Revision #e174fa9d79](https://github.com/MariaDB/server/commit/e174fa9d79)\
  2020-04-27 16:36:03 +0300
  * [MDEV-22207](https://jira.mariadb.org/browse/MDEV-22207) Drop default history partitions renders table inaccessible
* Merge [Revision #fbe2712705](https://github.com/MariaDB/server/commit/fbe2712705) 2020-04-25 21:57:52 +0300 - Merge 10.4 into 10.5
* [Revision #62903434eb](https://github.com/MariaDB/server/commit/62903434eb)\
  2020-04-24 22:22:01 +0300
  * fix s390x warning caused by gcc-5 bug
* [Revision #2b2dcf34f7](https://github.com/MariaDB/server/commit/2b2dcf34f7)\
  2020-04-23 18:31:32 +0300
  * fix buggy gcc warning on ARM
* [Revision #a4bccefb11](https://github.com/MariaDB/server/commit/a4bccefb11)\
  2020-04-23 20:48:32 +0200
  * [MDEV-20372](https://jira.mariadb.org/browse/MDEV-20372) - fix thread\_pool\_info
* [Revision #2655984ed4](https://github.com/MariaDB/server/commit/2655984ed4)\
  2020-04-21 23:49:51 +0300
  * Deb: Use mysql\[d].service symlinks as created by CMake
* [Revision #77bf7a9176](https://github.com/MariaDB/server/commit/77bf7a9176)\
  2020-04-21 09:02:25 +0300
  * Remove excess mysql-\* provides (the virtual-mysql-\* are enough)
* [Revision #7cbde2d0a2](https://github.com/MariaDB/server/commit/7cbde2d0a2)\
  2020-04-05 11:56:14 +0300
  * Deb: Misc small fixes and cleanups
* [Revision #13ec2ecc99](https://github.com/MariaDB/server/commit/13ec2ecc99)\
  2020-04-08 20:26:11 +0300
  * Deb: Rename mysqlreport to mariadb-report, fix regression in 9e1b3af4a
* [Revision #7fe2dddb0f](https://github.com/MariaDB/server/commit/7fe2dddb0f)\
  2020-04-05 13:13:54 +0300
  * Clean up logcheck.ignore.\* configs and unify MariaDB.org links with https
* [Revision #b8092a3c9d](https://github.com/MariaDB/server/commit/b8092a3c9d)\
  2020-04-13 14:26:34 +0300
  * Deb: Remove unmaintained AWS key plugin packaging
* [Revision #da64ec1ede](https://github.com/MariaDB/server/commit/da64ec1ede)\
  2020-04-13 09:33:02 +0300
  * [MDEV-19110](https://jira.mariadb.org/browse/MDEV-19110): Remove Cassandra from Debian packaging
* [Revision #9cc1c74ca3](https://github.com/MariaDB/server/commit/9cc1c74ca3)\
  2020-04-19 23:51:52 +0300
  * [MDEV-21944](https://jira.mariadb.org/browse/MDEV-21944): Remove TokuDB from Debian packaging
* [Revision #86f59e8615](https://github.com/MariaDB/server/commit/86f59e8615)\
  2020-04-10 19:31:18 +0300
  * Deb: Use 'eatmydata' when available to build faster with less disk I/O
* [Revision #03119c5890](https://github.com/MariaDB/server/commit/03119c5890)\
  2020-04-07 20:20:11 +0300
  * Deb: Add a customized salsa-ci.yml for easy extra testing
* [Revision #6f0b621caf](https://github.com/MariaDB/server/commit/6f0b621caf)\
  2020-04-05 12:33:42 +0300
  * Temporarily disable tests permanently failing on 10.5
* [Revision #e4d9ee00fb](https://github.com/MariaDB/server/commit/e4d9ee00fb)\
  2020-04-22 09:21:39 +0300
  * [MDEV-21807](https://jira.mariadb.org/browse/MDEV-21807) : galera.galera\_slave\_replay MTR failed: WSREP: Unknown parameter 'dbug
* [Revision #5951f4a174](https://github.com/MariaDB/server/commit/5951f4a174)\
  2020-04-21 21:14:54 +0300
  * [MDEV-22159](https://jira.mariadb.org/browse/MDEV-22159): Don't redirect as root to a tmp file not owned by root
* [Revision #1483ea911c](https://github.com/MariaDB/server/commit/1483ea911c)\
  2020-04-22 07:35:41 +0300
  * [MDEV-22181](https://jira.mariadb.org/browse/MDEV-22181) : galera.galera\_sst\_mysqldump\_with\_key MTR failed: INSERT failed: 1146: Table 'test.t1' doesn't exist
* [Revision #30c9833751](https://github.com/MariaDB/server/commit/30c9833751)\
  2020-04-22 12:36:11 +0300
  * [MDEV-22332](https://jira.mariadb.org/browse/MDEV-22332): Assertion mtr\_started == mtr.is\_active() failed
* [Revision #1b81e96593](https://github.com/MariaDB/server/commit/1b81e96593)\
  2020-04-22 04:44:28 +0900
  * [MDEV-21884](https://jira.mariadb.org/browse/MDEV-21884) MariaDB with Spider crashes on a query
* [Revision #7bd3c8a4b3](https://github.com/MariaDB/server/commit/7bd3c8a4b3)\
  2020-04-21 17:37:29 +0300
  * [MDEV-21941](https://jira.mariadb.org/browse/MDEV-21941): Fix GCC 10 -Wmaybe-uninitialized
* [Revision #2a691d5744](https://github.com/MariaDB/server/commit/2a691d5744)\
  2020-04-21 17:21:58 +0300
  * Fix main.partition\_debug\_innodb
* [Revision #4db43972e1](https://github.com/MariaDB/server/commit/4db43972e1)\
  2020-04-21 15:04:21 +0300
  * [MDEV-18115](https://jira.mariadb.org/browse/MDEV-18115): Remove fil\_type\_is\_data()
* [Revision #98003440c2](https://github.com/MariaDB/server/commit/98003440c2)\
  2020-04-20 11:00:39 +0300
  * Initialize error variable to 0 in alter\_table\_close
* [Revision #d2f5e82f00](https://github.com/MariaDB/server/commit/d2f5e82f00)\
  2020-04-20 09:58:25 +0300
  * Ship mariadb.service and mysql\[d].service symlinks
* [Revision #27d9986c1b](https://github.com/MariaDB/server/commit/27d9986c1b)\
  2020-04-17 17:41:49 +0300
  * Added more digits to JSON output of double
* [Revision #8d74d30dde](https://github.com/MariaDB/server/commit/8d74d30dde)\
  2020-04-15 17:47:30 +0300
  * Fixed compiler warning
* [Revision #f40ca33bbc](https://github.com/MariaDB/server/commit/f40ca33bbc)\
  2020-04-09 16:52:59 +0300
  * Make all #sql temporary table names uniform
* [Revision #eca5c2c67f](https://github.com/MariaDB/server/commit/eca5c2c67f)\
  2020-03-30 14:50:03 +0300
  * Added support for more functions when using partitioned S3 tables
* [Revision #78357796e8](https://github.com/MariaDB/server/commit/78357796e8)\
  2020-04-09 01:11:35 +0300
  * Added support for VISIBLE attribute for indexes in CREATE TABLE
* [Revision #91ffdc8380](https://github.com/MariaDB/server/commit/91ffdc8380)\
  2020-04-06 15:41:33 +0300
  * Don't try to open temporary tables if there are no temporary tables.
* [Revision #f9f33b85be](https://github.com/MariaDB/server/commit/f9f33b85be)\
  2020-03-30 20:12:02 +0300
  * Handle errors from external\_unlock & mysql\_unlock\_tables
* [Revision #7866b72304](https://github.com/MariaDB/server/commit/7866b72304)\
  2020-03-31 14:10:45 +0300
  * Updated client and server to use new binary names in --debug traces
* [Revision #e3130d22e1](https://github.com/MariaDB/server/commit/e3130d22e1)\
  2020-03-30 21:59:07 +0300
  * Fixed some assert crashes related to keyread.
* [Revision #8399af81be](https://github.com/MariaDB/server/commit/8399af81be)\
  2020-03-30 14:46:44 +0300
  * Bug#19784790: ASSERTION \`PART\_SHARE->PARTITIONS\_SHARE\_REFS->NUM\_PARTS >= M\_TOT\_PARTS' FAILED.
* [Revision #0126169e08](https://github.com/MariaDB/server/commit/0126169e08)\
  2020-03-30 14:44:54 +0300
  * Added error message to --die in mtr
* [Revision #478ec7750a](https://github.com/MariaDB/server/commit/478ec7750a)\
  2020-04-19 17:17:59 +0300
  * Cleanup whitespace
* [Revision #8c41a1df86](https://github.com/MariaDB/server/commit/8c41a1df86)\
  2020-04-07 20:05:56 +0300
  * [MDEV-21869](https://jira.mariadb.org/browse/MDEV-21869): Add temporary Lintian overrides
* [Revision #29c5d96da3](https://github.com/MariaDB/server/commit/29c5d96da3)\
  2020-04-07 20:29:16 +0300
  * [MDEV-21869](https://jira.mariadb.org/browse/MDEV-21869): Make Debian packaging Lintian clean
* [Revision #a4c5480525](https://github.com/MariaDB/server/commit/a4c5480525)\
  2020-04-08 20:18:37 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Sync correct Debian handling of auth\_pam\_tool
* [Revision #4e946b0f0c](https://github.com/MariaDB/server/commit/4e946b0f0c)\
  2020-04-07 12:10:03 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Sync mariadb-server maintainer scripts as much as possible
* [Revision #9ed7e967b3](https://github.com/MariaDB/server/commit/9ed7e967b3)\
  2020-04-07 20:17:54 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Sync breaks/replaces relationships and file locations
* [Revision #7a0eeaaf66](https://github.com/MariaDB/server/commit/7a0eeaaf66)\
  2020-04-05 13:05:56 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Sync deb build rules etc with downstream
* [Revision #bc11f392f8](https://github.com/MariaDB/server/commit/bc11f392f8)\
  2020-04-05 12:57:10 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Correctly place files in libmariadb-dev, libmariadbd-dev etc packages
* [Revision #5cdf245d7e](https://github.com/MariaDB/server/commit/5cdf245d7e)\
  2020-04-04 22:53:00 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Sync deb build dependencies and control file with downstream
* [Revision #6af0bd6907](https://github.com/MariaDB/server/commit/6af0bd6907)\
  2019-01-11 18:22:44 -0300
  * [MDEV-15526](https://jira.mariadb.org/browse/MDEV-15526) systemd unit files naming and installation
* [Revision #afde33fc6f](https://github.com/MariaDB/server/commit/afde33fc6f)\
  2020-04-17 20:41:33 +0300
  * Update plugins.pam\_\* tests to no longer provide --plugin-dir to mysqltest
* [Revision #181f17c3cd](https://github.com/MariaDB/server/commit/181f17c3cd)\
  2020-04-15 23:19:10 +0900
  * [MDEV-20502](https://jira.mariadb.org/browse/MDEV-20502) Queries against spider tables return wrong values for columns following constant declarations.
* [Revision #b4dd996dc1](https://github.com/MariaDB/server/commit/b4dd996dc1)\
  2020-04-17 01:49:46 +0900
  * [MDEV-21884](https://jira.mariadb.org/browse/MDEV-21884) MariaDB with Spider crashes on a query
* [Revision #e2a932c9ea](https://github.com/MariaDB/server/commit/e2a932c9ea)\
  2020-04-17 13:11:07 +0200
  * Post-fixes for [MDEV-18851](https://jira.mariadb.org/browse/MDEV-18851) for Windows
* [Revision #2f7d91bb6c](https://github.com/MariaDB/server/commit/2f7d91bb6c)\
  2020-04-14 18:43:03 +0300
  * [MDEV-22242](https://jira.mariadb.org/browse/MDEV-22242) B-trees can become extremely skewed
* [Revision #87a7968c23](https://github.com/MariaDB/server/commit/87a7968c23)\
  2020-04-05 18:21:29 +0300
  * [MDEV-22150](https://jira.mariadb.org/browse/MDEV-22150): Symlink and move test client plugins to client plugin path
* [Revision #8447edb747](https://github.com/MariaDB/server/commit/8447edb747)\
  2020-04-08 15:25:04 +0300
  * Specify a new client\_plugindir path, to be used during testing
* [Revision #609a9312dc](https://github.com/MariaDB/server/commit/609a9312dc)\
  2020-04-08 15:09:47 +0300
  * Update dialog to not provide plugin-dir path to mysqltest
* [Revision #4bc31a904f](https://github.com/MariaDB/server/commit/4bc31a904f)\
  2020-03-27 01:47:53 +0200
  * [MDEV-22053](https://jira.mariadb.org/browse/MDEV-22053): Pass INSTALL\_LAYOUT "DEB" correctly to CONC (libmariadb)
* [Revision #91e79dff54](https://github.com/MariaDB/server/commit/91e79dff54)\
  2020-04-12 22:11:22 +0200
  * cleanup: comments
* [Revision #fcd84da5f1](https://github.com/MariaDB/server/commit/fcd84da5f1)\
  2020-04-12 18:09:09 +0200
  * [MDEV-22218](https://jira.mariadb.org/browse/MDEV-22218) InnoDB: Failing assertion: node->pcur->rel\_pos == BTR\_PCUR\_ON upon LOAD DATA with NO\_BACKSLASH\_ESCAPES in SQL\_MODE and unique blob in table
* [Revision #8c0b988073](https://github.com/MariaDB/server/commit/8c0b988073)\
  2020-04-09 12:15:58 +0200
  * cleanup: remove unnecessary malloc
* [Revision #4bd8c63444](https://github.com/MariaDB/server/commit/4bd8c63444)\
  2020-04-08 18:46:08 +0200
  * cleanup: don't repeat common code
* [Revision #364e7a9ae6](https://github.com/MariaDB/server/commit/364e7a9ae6)\
  2020-04-10 19:53:33 +0200
  * remove debugging message
* [Revision #3ab21fd4e0](https://github.com/MariaDB/server/commit/3ab21fd4e0)\
  2020-04-10 18:59:55 +0200
  * Windows build - use InstallRequiredSystemLibraries for MSVC\_CRT\_TYPE=/MD CMake parameter
* [Revision #93efbc390d](https://github.com/MariaDB/server/commit/93efbc390d)\
  2020-04-10 14:09:18 +0200
  * [MDEV-22214](https://jira.mariadb.org/browse/MDEV-22214) mariadbd.exe calls function mysqld.exe, and crashes
* [Revision #38f7dbec19](https://github.com/MariaDB/server/commit/38f7dbec19)\
  2020-04-10 10:47:03 +0200
  * CMake - clang linker on Windows does not understand /release flag
* [Revision #11cebb4ae8](https://github.com/MariaDB/server/commit/11cebb4ae8)\
  2020-04-10 10:45:58 +0200
  * CMake : Do not add compile flags, such as -Wconversion with ADD\_DEFINITIONS
* [Revision #6bbc0eedc6](https://github.com/MariaDB/server/commit/6bbc0eedc6)\
  2020-04-08 18:31:18 +0530
  * [MDEV-22193](https://jira.mariadb.org/browse/MDEV-22193) Avoid un-necessary page initialization during recovery
* [Revision #ff66d38cf2](https://github.com/MariaDB/server/commit/ff66d38cf2)\
  2020-04-06 13:06:12 +0530
  * [MDEV-21946](https://jira.mariadb.org/browse/MDEV-21946): Server crash in store\_length upon GROUP BY WITH ROLLUP with geometry field
* [Revision #c7ab676192](https://github.com/MariaDB/server/commit/c7ab676192)\
  2020-04-08 18:09:28 +0300
  * [MDEV-22075](https://jira.mariadb.org/browse/MDEV-22075) : Server crashes in wsrep\_should\_replicate\_ddl\_iterate upon CREATE VIEW
* [Revision #6cf8f05fd9](https://github.com/MariaDB/server/commit/6cf8f05fd9)\
  2020-04-08 15:31:57 +0400
  * Fixed centos 6 build failure
* [Revision #97506bf7c3](https://github.com/MariaDB/server/commit/97506bf7c3)\
  2020-04-07 14:42:02 +1000
  * mysql-test: add large\_pages test
* [Revision #5f5bb63b2e](https://github.com/MariaDB/server/commit/5f5bb63b2e)\
  2020-04-07 13:20:24 +1000
  * Add Daniel Black to authors
* [Revision #a0d5894015](https://github.com/MariaDB/server/commit/a0d5894015)\
  2020-04-07 10:00:10 +1000
  * my\_pagepages: perror -> my\_error
* [Revision #a535d4d1a6](https://github.com/MariaDB/server/commit/a535d4d1a6)\
  2020-04-06 13:36:25 +1000
  * my\_largepage: fprintf -> my\_{printf\_,}error
* [Revision #11aaf5c8d2](https://github.com/MariaDB/server/commit/11aaf5c8d2)\
  2020-04-06 13:35:34 +1000
  * add EE\_BADMEMORY\_RELEASE
* [Revision #5e86b2eec8](https://github.com/MariaDB/server/commit/5e86b2eec8)\
  2020-04-06 12:07:34 +1000
  * my\_large\_malloc: style fix
* [Revision #2c00502014](https://github.com/MariaDB/server/commit/2c00502014)\
  2020-04-06 11:55:42 +1000
  * my\_largepage: reduce includes already in my\_global.h
* [Revision #96d4b228ea](https://github.com/MariaDB/server/commit/96d4b228ea)\
  2020-04-06 11:52:29 +1000
  * my\_large\_pages: simplify solaris constants
* [Revision #7b7a9161e2](https://github.com/MariaDB/server/commit/7b7a9161e2)\
  2020-04-06 11:05:42 +1000
  * my\_large\_pages: remove conventional memory(my\_malloc\_lock) fallback
* Merge [Revision #ccc06931c3](https://github.com/MariaDB/server/commit/ccc06931c3) 2020-04-08 10:36:41 +0300 - Merge 10.4 into 10.5
* [Revision #9075973dbf](https://github.com/MariaDB/server/commit/9075973dbf)\
  2020-04-08 06:09:42 +0000
  * [MDEV-17812](https://jira.mariadb.org/browse/MDEV-17812) Use MariaDB in error messages instead of MySQL
* [Revision #0eab87cef2](https://github.com/MariaDB/server/commit/0eab87cef2)\
  2020-04-07 17:20:38 +0300
  * [MDEV-22010](https://jira.mariadb.org/browse/MDEV-22010): Allow mariadbd in mtr suppressions
* [Revision #1738c0f1be](https://github.com/MariaDB/server/commit/1738c0f1be)\
  2020-04-07 16:43:46 +0300
  * [MDEV-22169](https://jira.mariadb.org/browse/MDEV-22169) Recovery fails after failing to insert into mlog\_init
* [Revision #d848fcad69](https://github.com/MariaDB/server/commit/d848fcad69)\
  2020-04-07 14:53:40 +1000
  * [MDEV-22010](https://jira.mariadb.org/browse/MDEV-22010): mtr, "mariadbd" exists in mysys error messages
* [Revision #dcc2eaebbd](https://github.com/MariaDB/server/commit/dcc2eaebbd)\
  2020-03-31 07:49:45 +1100
  * [MDEV-22010](https://jira.mariadb.org/browse/MDEV-22010): mtr search for mariadbd first
* [Revision #778a174e5e](https://github.com/MariaDB/server/commit/778a174e5e)\
  2020-04-06 10:47:11 +0300
  * Postfix for f46917238: use colon instead of comma
* [Revision #139117528a](https://github.com/MariaDB/server/commit/139117528a)\
  2020-04-06 06:26:46 +0300
  * [MDEV-22153](https://jira.mariadb.org/browse/MDEV-22153) ALTER add default history partitions makes table inaccessible
* [Revision #22811a1c60](https://github.com/MariaDB/server/commit/22811a1c60)\
  2020-04-05 17:32:06 +0400
  * Fixed build failure
* [Revision #113e227e26](https://github.com/MariaDB/server/commit/113e227e26)\
  2020-04-05 20:53:08 +1000
  * my\_largepage.c: cleanup
* [Revision #abb2332420](https://github.com/MariaDB/server/commit/abb2332420)\
  2020-04-05 16:39:23 +1000
  * travis: xcode11.3
* [Revision #9bf3a3a47a](https://github.com/MariaDB/server/commit/9bf3a3a47a)\
  2020-04-05 18:04:52 +1000
  * HAVE\_LARGE\_PAGES no longer global
* [Revision #71337a4452](https://github.com/MariaDB/server/commit/71337a4452)\
  2020-04-05 18:06:27 +1000
  * my\_large\_malloc/free fall back to my\_{malloc|free}\_lock
* [Revision #2a18e783ca](https://github.com/MariaDB/server/commit/2a18e783ca)\
  2020-04-05 16:34:12 +1000
  * my\_large\_page: more verbose errors on allocation fallback/failure
* [Revision #d5568e7591](https://github.com/MariaDB/server/commit/d5568e7591)\
  2020-04-05 12:33:45 +1000
  * my\_large\_malloc\_int consolidated into my\_large\_malloc
* [Revision #472d2d0492](https://github.com/MariaDB/server/commit/472d2d0492)\
  2020-04-05 11:34:41 +1000
  * my\_large\_free\_int merge into my\_large\_free
* [Revision #4ac7693678](https://github.com/MariaDB/server/commit/4ac7693678)\
  2020-04-04 20:44:07 +0300
  * Add author "Otto Kekäläinen" to SHOW AUTHORS
* [Revision #b541defea0](https://github.com/MariaDB/server/commit/b541defea0)\
  2020-04-03 14:05:40 +0300
  * Deb: Build depend on libcurl4-openssl-dev as primary option
* [Revision #6959c0922a](https://github.com/MariaDB/server/commit/6959c0922a)\
  2020-04-03 13:00:22 +0300
  * [MDEV-20298](https://jira.mariadb.org/browse/MDEV-20298) Make mariadb-client-10.5 perl dep backwards compatible
* [Revision #333e1d82fc](https://github.com/MariaDB/server/commit/333e1d82fc)\
  2020-03-27 01:31:35 +0200
  * Deb: Update control file Depends to include only variables that are set
* [Revision #2cedf3eca4](https://github.com/MariaDB/server/commit/2cedf3eca4)\
  2020-03-27 00:48:34 +0200
  * [MDEV-21303](https://jira.mariadb.org/browse/MDEV-21303): Fix man page packaging for new mariadb-\* named binaries
* [Revision #80abfa0eda](https://github.com/MariaDB/server/commit/80abfa0eda)\
  2020-03-16 10:39:43 +0200
  * Don't force to use all processors in autobake-deb.sh
* [Revision #1589cf1cb3](https://github.com/MariaDB/server/commit/1589cf1cb3)\
  2020-03-26 19:22:57 +0200
  * Deb: Remove TokuDB from Debian packages while keeping it easy to revert
* [Revision #91994b6be4](https://github.com/MariaDB/server/commit/91994b6be4)\
  2020-03-14 22:40:26 +0200
  * Deb: Extend control dependencies for MySQL 8.0 and clean up
* [Revision #400d7709ce](https://github.com/MariaDB/server/commit/400d7709ce)\
  2020-03-14 22:11:37 +0200
  * Deb: Clean away deprecated autobake modifications
* [Revision #f469172380](https://github.com/MariaDB/server/commit/f469172380)\
  2020-04-04 17:38:44 +0300
  * Do not print LSAN suppression statistics in the output
* [Revision #40c2cf335d](https://github.com/MariaDB/server/commit/40c2cf335d)\
  2020-04-04 15:52:31 +0400
  * [MDEV-22146](https://jira.mariadb.org/browse/MDEV-22146) - Server crashes in mysql\_ha\_flush\_tables upon ALTER SERVER
* [Revision #2e2138baa5](https://github.com/MariaDB/server/commit/2e2138baa5)\
  2020-04-04 00:42:09 +0400
  * Simplified away my\_get\_large\_page\_size()
* [Revision #30379b487f](https://github.com/MariaDB/server/commit/30379b487f)\
  2020-04-03 21:13:04 +0400
  * HAVE\_LARGE\_PAGE\_OPTION to HAVE\_LARGE\_PAGES
* [Revision #4338bb8a75](https://github.com/MariaDB/server/commit/4338bb8a75)\
  2020-04-03 20:53:53 +0400
  * Coding style fixes
* [Revision #e4a960780f](https://github.com/MariaDB/server/commit/e4a960780f)\
  2020-04-03 20:46:48 +0400
  * my\_next\_large\_page\_size() cleanup
* [Revision #fc6e8b4b1b](https://github.com/MariaDB/server/commit/fc6e8b4b1b)\
  2020-04-03 20:29:38 +0400
  * Cleanup HAVE\_MMAP\_ALIGNED: one cmake check less
* [Revision #40f4d8c671](https://github.com/MariaDB/server/commit/40f4d8c671)\
  2020-04-04 01:07:24 +0300
  * [MDEV-21941](https://jira.mariadb.org/browse/MDEV-21941) assertion cleanups
* [Revision #105b879d0f](https://github.com/MariaDB/server/commit/105b879d0f)\
  2020-04-04 00:53:37 +0300
  * [MDEV-21941](https://jira.mariadb.org/browse/MDEV-21941) RENAME doesn't work for system time or period fields
* [Revision #431a740815](https://github.com/MariaDB/server/commit/431a740815)\
  2020-04-04 00:53:36 +0300
  * [MDEV-21889](https://jira.mariadb.org/browse/MDEV-21889) IF EXISTS clause does not work for RENAME COLUMN and RENAME INDEX
* [Revision #6fb3e83d74](https://github.com/MariaDB/server/commit/6fb3e83d74)\
  2020-04-04 00:52:54 +0300
  * [MDEV-21889](https://jira.mariadb.org/browse/MDEV-21889) Typo fix: ER\_KEY\_DOES\_NOT\_EXISTS
* [Revision #d2c366c6fb](https://github.com/MariaDB/server/commit/d2c366c6fb)\
  2020-04-03 20:02:36 +0400
  * Fix CentOS 6 and quantal build failures
* [Revision #1078a630f7](https://github.com/MariaDB/server/commit/1078a630f7)\
  2020-04-03 17:47:56 +0300
  * [MDEV-22139](https://jira.mariadb.org/browse/MDEV-22139) fseg\_free\_page\_low() fails to write FREE\_PAGE record, breaking recovery
* [Revision #abb0a31ec8](https://github.com/MariaDB/server/commit/abb0a31ec8)\
  2020-03-27 14:45:42 +1100
  * output\_core\_info - freebsd rlimits in different proc entry
* [Revision #4197014ba0](https://github.com/MariaDB/server/commit/4197014ba0)\
  2019-12-21 23:51:49 +0400
  * Yet less TDC hash lookups
* [Revision #7a947614fb](https://github.com/MariaDB/server/commit/7a947614fb)\
  2019-12-17 16:25:15 +0400
  * Split tdc\_remove\_table()
* [Revision #06fae75859](https://github.com/MariaDB/server/commit/06fae75859)\
  2019-12-18 15:02:55 +0400
  * tc\_remove\_all\_unused\_tables() cleanup
* [Revision #14e1385691](https://github.com/MariaDB/server/commit/14e1385691)\
  2019-12-17 23:00:23 +0400
  * Proper locking for mysql.gtid\_slave\_pos truncation
* [Revision #bfdd30d3e9](https://github.com/MariaDB/server/commit/bfdd30d3e9)\
  2019-12-21 01:22:09 +0400
  * Fixed close\_cached\_connection\_tables() flushing
* [Revision #54c03cb4f0](https://github.com/MariaDB/server/commit/54c03cb4f0)\
  2019-12-20 20:33:29 +0400
  * Cleanup mysql\_inplace\_alter\_table()
* [Revision #02619ed73b](https://github.com/MariaDB/server/commit/02619ed73b)\
  2019-12-20 17:20:56 +0400
  * Cleanup close\_all\_tables\_for\_name()
* [Revision #e0743bd1a5](https://github.com/MariaDB/server/commit/e0743bd1a5)\
  2019-12-18 01:18:19 +0400
  * Let "FTWRL \<table\_list>" use extra(HA\_EXTRA\_FLUSH)
* [Revision #0870b75af7](https://github.com/MariaDB/server/commit/0870b75af7)\
  2020-04-02 19:34:34 +0300
  * [MDEV-22126](https://jira.mariadb.org/browse/MDEV-22126) Rename confusing constant mtr\_t::OPT
* [Revision #406ca20b49](https://github.com/MariaDB/server/commit/406ca20b49)\
  2020-04-02 19:06:03 +0300
  * [MDEV-22108](https://jira.mariadb.org/browse/MDEV-22108) Recovery fails with InnoDB: Malformed log record
* [Revision #e8351934b6](https://github.com/MariaDB/server/commit/e8351934b6)\
  2020-04-03 06:54:08 +1100
  * Merge pull request #1221 from grooverdan/10.4-[MDEV-18851](https://jira.mariadb.org/browse/MDEV-18851)-multiple-sized-large-page-support
* [Revision #3bb5c6b0c2](https://github.com/MariaDB/server/commit/3bb5c6b0c2)\
  2020-04-02 14:03:19 +0200
  * [MDEV-22113](https://jira.mariadb.org/browse/MDEV-22113) SIGSEGV, ASAN use-after-poison, Assertion \`next\_insert\_id == 0' in handler::ha\_external\_lock
* [Revision #a5686e14d9](https://github.com/MariaDB/server/commit/a5686e14d9)\
  2020-03-27 13:04:58 +1100
  * [MDEV-21303](https://jira.mariadb.org/browse/MDEV-21303) Use mariadbd as the library plugins link to on non-Linux
* [Revision #5f3501a6e5](https://github.com/MariaDB/server/commit/5f3501a6e5)\
  2020-04-02 10:54:31 +0000
  * [MDEV-22120](https://jira.mariadb.org/browse/MDEV-22120) Add author to SHOW AUTHORS
* [Revision #a135f0ab88](https://github.com/MariaDB/server/commit/a135f0ab88)\
  2020-03-28 17:05:11 +0200
  * Travis-CI: Update default distro from Ubuntu Xenial to Bionic
* [Revision #dda61ade11](https://github.com/MariaDB/server/commit/dda61ade11)\
  2020-03-27 23:08:16 +0200
  * Travis-CI: Slim down number of parallel jobs to speed up total run time
* [Revision #33ffcecc89](https://github.com/MariaDB/server/commit/33ffcecc89)\
  2020-04-02 09:39:43 +0300
  * [MDEV-22114](https://jira.mariadb.org/browse/MDEV-22114) Assertion failure on SET GLOBAL innodb\_buffer\_pool\_evict='uncompressed'
* [Revision #b212f1dac2](https://github.com/MariaDB/server/commit/b212f1dac2)\
  2020-04-01 17:56:50 +0300
  * [MDEV-22107](https://jira.mariadb.org/browse/MDEV-22107) Restore accidentally orphaned MTR\_MEMO\_MODIFY
* [Revision #587f3e0d9f](https://github.com/MariaDB/server/commit/587f3e0d9f)\
  2020-04-01 11:38:26 +0300
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Fix a warning in RelWithDebInfo build
* [Revision #51a9dd6793](https://github.com/MariaDB/server/commit/51a9dd6793)\
  2020-04-01 11:33:58 +0300
  * Fix GCC 9.3.0 -Wstrict-aliasing
* [Revision #abaeeffbf9](https://github.com/MariaDB/server/commit/abaeeffbf9)\
  2020-04-01 11:19:12 +0300
  * [MDEV-22103](https://jira.mariadb.org/browse/MDEV-22103) INNODB\_ENCRYPTION\_NUM\_KEY\_REQUESTS is missing from INFORMATION\_SCHEMA.GLOBAL\_STATUS
* [Revision #a1077ab287](https://github.com/MariaDB/server/commit/a1077ab287)\
  2020-04-01 10:40:53 +0300
  * [MDEV-22102](https://jira.mariadb.org/browse/MDEV-22102) Assertion w==OPT failed in trx\_undo\_header\_create()
* [Revision #244ff3e5a0](https://github.com/MariaDB/server/commit/244ff3e5a0)\
  2020-03-17 02:59:11 +1000
  * forbid REPLACE/ODKU on tables containing WITHOUT OVERLAPS
* [Revision #62e7ad2bbc](https://github.com/MariaDB/server/commit/62e7ad2bbc)\
  2020-03-29 20:30:59 +0200
  * cleanup: move initializations from query exec to prepare time
* [Revision #259fb1cbed](https://github.com/MariaDB/server/commit/259fb1cbed)\
  2019-11-26 19:22:04 +1000
  * [MDEV-16978](https://jira.mariadb.org/browse/MDEV-16978) Application-time periods: WITHOUT OVERLAPS
* [Revision #0515577d12](https://github.com/MariaDB/server/commit/0515577d12)\
  2020-03-05 19:19:57 +0100
  * cleanup: prepare "update\_handler" for WITHOUT OVERLAPS
* [Revision #045510cb92](https://github.com/MariaDB/server/commit/045510cb92)\
  2020-03-23 17:51:46 +1000
  * fix mroonga: change field's table as well as ptr for ad-hoc fixes ptr\_in\_record usage
* [Revision #db6f02bb98](https://github.com/MariaDB/server/commit/db6f02bb98)\
  2020-03-24 16:45:56 +1000
  * fix key\_copy to use from\_record argument data
* [Revision #7f9b3ea951](https://github.com/MariaDB/server/commit/7f9b3ea951)\
  2020-03-24 16:45:01 +1000
  * pass ptr into more Field methods
* [Revision #6334b57621](https://github.com/MariaDB/server/commit/6334b57621)\
  2020-03-12 14:14:55 +0100
  * cleanup: const
* [Revision #b9df4d2a35](https://github.com/MariaDB/server/commit/b9df4d2a35)\
  2019-11-19 18:52:41 +1000
  * Fix real keyread count for partitions
* [Revision #e6af62189e](https://github.com/MariaDB/server/commit/e6af62189e)\
  2020-01-10 23:17:38 +1000
  * unify "partitioning cannot do X" error messages
* [Revision #3bef848226](https://github.com/MariaDB/server/commit/3bef848226)\
  2019-11-27 00:05:19 +1000
  * cleanup: reduce code duplication in read\_extra2()
* [Revision #8ab693847e](https://github.com/MariaDB/server/commit/8ab693847e)\
  2020-03-21 20:21:58 +0100
  * cleanup: remove unused PLUGIN\_INIT\_SKIP\_DYNAMIC\_LOADING
* [Revision #64be8c2bf2](https://github.com/MariaDB/server/commit/64be8c2bf2)\
  2020-03-21 20:09:50 +0100
  * mysqld --help will now load mysqld.plugin table
* [Revision #dc3185c759](https://github.com/MariaDB/server/commit/dc3185c759)\
  2020-03-24 22:22:57 +0100
  * cleanup: pk\_is\_clustering\_key() -> is\_clustering\_key()
* [Revision #27bf97aa00](https://github.com/MariaDB/server/commit/27bf97aa00)\
  2020-03-24 22:13:49 +0100
  * cleanup: dead code, comments, avoid current\_thd
* [Revision #63f922dae1](https://github.com/MariaDB/server/commit/63f922dae1)\
  2020-03-31 14:42:07 +0300
  * [MDEV-22090](https://jira.mariadb.org/browse/MDEV-22090) Change buffer is not freed after dropping or rebuilding table
* [Revision #14c72bd3e0](https://github.com/MariaDB/server/commit/14c72bd3e0)\
  2020-03-31 14:37:11 +0300
  * [MDEV-19514](https://jira.mariadb.org/browse/MDEV-19514): Correct a few outdated comments
* [Revision #b2bc837ebe](https://github.com/MariaDB/server/commit/b2bc837ebe)\
  2020-03-31 08:48:00 +0300
  * Cassandra: Define ha\_cassandra::records\_in\_range()
* Merge [Revision #37c14690fc](https://github.com/MariaDB/server/commit/37c14690fc) 2020-03-30 18:52:17 +0300 - Merge 10.4 into 10.5
* [Revision #aae3f921ad](https://github.com/MariaDB/server/commit/aae3f921ad)\
  2020-03-30 18:45:09 +0300
  * Cleanup recv\_sys: Move things to members
* [Revision #a8b04c3ee0](https://github.com/MariaDB/server/commit/a8b04c3ee0)\
  2020-03-30 18:08:38 +0300
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Remove a trace of pre-[MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) crash-upgrade
* [Revision #6be56dd1c8](https://github.com/MariaDB/server/commit/6be56dd1c8)\
  2020-03-28 21:05:55 +0200
  * [MDEV-20377](https://jira.mariadb.org/browse/MDEV-20377): Enable MemorySanitizer user-poisoning
* [Revision #94d0bb4dbe](https://github.com/MariaDB/server/commit/94d0bb4dbe)\
  2020-03-28 21:33:18 +0200
  * [MDEV-20377](https://jira.mariadb.org/browse/MDEV-20377): Make WITH\_MSAN more usable
* [Revision #6ec6eda4e3](https://github.com/MariaDB/server/commit/6ec6eda4e3)\
  2020-03-28 21:17:26 +0200
  * Do not compare uninitialized data
* [Revision #3a1c897184](https://github.com/MariaDB/server/commit/3a1c897184)\
  2020-03-28 21:01:10 +0200
  * my\_net\_init(): Avoid reading uninitialized data in my\_net\_local\_init()
* [Revision #e129555462](https://github.com/MariaDB/server/commit/e129555462)\
  2020-03-28 01:46:53 +0100
  * [MDEV-20372](https://jira.mariadb.org/browse/MDEV-20372) thread\_pool\_info fails randomly in 10.5
* [Revision #f991c41670](https://github.com/MariaDB/server/commit/f991c41670)\
  2020-03-27 11:32:41 +0400
  * [MDEV-22057](https://jira.mariadb.org/browse/MDEV-22057) REPLICATION MASTER ADMIN is missing in root account after upgrade
* [Revision #d3bdc30c00](https://github.com/MariaDB/server/commit/d3bdc30c00)\
  2020-03-27 15:17:50 +0200
  * [MDEV-22060](https://jira.mariadb.org/browse/MDEV-22060) MSAN use-of-uninitialized-value in main.query\_cache\_innodb
* [Revision #0181384a3f](https://github.com/MariaDB/server/commit/0181384a3f)\
  2020-03-18 09:05:02 +0000
  * [MDEV-20329](https://jira.mariadb.org/browse/MDEV-20329) Fix S3 engine OpenSSL race
* [Revision #ff64152bc7](https://github.com/MariaDB/server/commit/ff64152bc7)\
  2020-03-27 12:30:10 +0200
  * Fixed failing tests in buildbot
* Merge [Revision #53aabda6b5](https://github.com/MariaDB/server/commit/53aabda6b5) 2020-03-27 09:39:15 +0200 - Merge 10.4 into 10.5
* [Revision #f614b6ea61](https://github.com/MariaDB/server/commit/f614b6ea61)\
  2020-03-27 08:59:20 +0200
  * [MDEV-21899](https://jira.mariadb.org/browse/MDEV-21899) INSERT into a secondary index with zero-data-length key is not crash-safe
* [Revision #eb483c5181](https://github.com/MariaDB/server/commit/eb483c5181)\
  2020-02-28 12:59:30 +0200
  * Updated optimizer costs in multi\_range\_read\_info\_const() and sql\_select.cc
* [Revision #b3ab3105fd](https://github.com/MariaDB/server/commit/b3ab3105fd)\
  2020-03-04 19:52:19 +0200
  * Removed double calls to records\_in\_range from distinct and group by
* [Revision #f36ca142f7](https://github.com/MariaDB/server/commit/f36ca142f7)\
  2020-02-27 19:12:27 +0200
  * Added page\_range to records\_in\_range() to improve range statistics
* [Revision #9b06199080](https://github.com/MariaDB/server/commit/9b06199080)\
  2020-03-22 16:11:10 +0200
  * Disabled partition\_innodb because it constaintly fails in buildbot
* [Revision #0fbab2525d](https://github.com/MariaDB/server/commit/0fbab2525d)\
  2020-03-26 12:02:29 -0400
  * bump the VERSION
* [Revision #2e0a40bdf0](https://github.com/MariaDB/server/commit/2e0a40bdf0)\
  2020-03-17 15:10:46 +1100
  * Deb: libcurl4 in bionic+/buster+
* [Revision #718f18599a](https://github.com/MariaDB/server/commit/718f18599a)\
  2020-03-26 16:05:25 +0200
  * [MDEV-21850](https://jira.mariadb.org/browse/MDEV-21850): ASAN use-after-poison in page\_cur\_insert\_rec\_low()
* [Revision #b8e7579194](https://github.com/MariaDB/server/commit/b8e7579194)\
  2020-03-26 09:29:33 +0400
  * [MDEV-22040](https://jira.mariadb.org/browse/MDEV-22040) versioning.truncate\_privilege : GRANT fails with "Access denied", for root user
* [Revision #6ef3dbb1ff](https://github.com/MariaDB/server/commit/6ef3dbb1ff)\
  2020-03-25 15:09:53 +0100
  * Fix unused variable warning in optimized build.
* [Revision #1b58ef7d3f](https://github.com/MariaDB/server/commit/1b58ef7d3f)\
  2020-03-25 15:09:14 +0100
  * Build cleanups.
* [Revision #bb8df68521](https://github.com/MariaDB/server/commit/bb8df68521)\
  2020-03-25 16:29:50 +0200
  * Disable building S3 for embedded server
* [Revision #80544a5878](https://github.com/MariaDB/server/commit/80544a5878)\
  2020-03-25 16:29:23 +0200
  * Fixed rpl.rpl\_mariadb\_slave\_capability.result file
* [Revision #12d59fabe2](https://github.com/MariaDB/server/commit/12d59fabe2)\
  2020-03-25 22:40:14 +0900
  * change from to for adding defaults-file in Spider tests
* [Revision #334ab8c6a7](https://github.com/MariaDB/server/commit/334ab8c6a7)\
  2020-03-25 11:59:33 +0100
  * Improve cmake performance on Windows

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
