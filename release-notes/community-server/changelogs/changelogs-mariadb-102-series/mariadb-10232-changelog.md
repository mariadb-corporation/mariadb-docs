# MariaDB 10.2.32 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.32/)[Release Notes](../../old-releases/10.2/10.2.32.md)[Changelog](mariadb-10232-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 12 May 2020

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.32.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* Includes all fixes from [MariaDB 10.1.45](../changelogs-mariadb-101-series/mariadb-10145-changelog.md)
* Merge [Revision #985f63cce1](https://github.com/MariaDB/server/commit/985f63cce1) 2020-05-08 13:38:36 +0200 - Merge branch '10.1' into 10.2
* [Revision #e84c62d59b](https://github.com/MariaDB/server/commit/e84c62d59b)\
  2020-05-08 12:41:45 +0200
  * [MDEV-22504](https://jira.mariadb.org/browse/MDEV-22504): Session tracking return incorrectly long traking data
* [Revision #1d1fb13e59](https://github.com/MariaDB/server/commit/1d1fb13e59)\
  2020-05-07 16:14:54 +0200
  * update C/C
* [Revision #5666f333a7](https://github.com/MariaDB/server/commit/5666f333a7)\
  2020-05-05 18:54:35 +0300
  * List of unstable tests for 10.2.32 release
* [Revision #1cccd3c7cc](https://github.com/MariaDB/server/commit/1cccd3c7cc)\
  2020-05-04 22:01:26 +0300
  * [MDEV-7962](https://jira.mariadb.org/browse/MDEV-7962): Fix cmake WITH\_WSREP=OFF
* Merge [Revision #3f65ce5781](https://github.com/MariaDB/server/commit/3f65ce5781) 2020-05-04 19:00:21 +0300 - Merge 10.1 into 10.2
* [Revision #d467bb7e5e](https://github.com/MariaDB/server/commit/d467bb7e5e)\
  2020-05-04 18:57:55 +0300
  * [MDEV-7962](https://jira.mariadb.org/browse/MDEV-7962) post-push fixes
* [Revision #5a270e6acc](https://github.com/MariaDB/server/commit/5a270e6acc)\
  2020-05-04 18:49:48 +0300
  * Add missing have\_debug.inc
* [Revision #5008fc709b](https://github.com/MariaDB/server/commit/5008fc709b)\
  2020-05-04 10:00:07 +0200
  * New Connector C
* Merge [Revision #79c29296ce](https://github.com/MariaDB/server/commit/79c29296ce) 2020-05-02 09:47:02 +0200 - Merge 'connect/10.2' into 10.2
* [Revision #f5f9659b15](https://github.com/MariaDB/server/commit/f5f9659b15)\
  2020-03-11 14:52:20 +0100
  * Fix [60637429#60637429](https://stackoverflow.com/questions/60625778/import-complex-xml-from-multiple-files-in-mariadb/60637429#60637429) Import complex XML from multiple files in MariaDB Some row results are missing and replaced by the last file one. Thats because Nx and Sx column members are not reset when changing file.
* Merge [Revision #ca091e6372](https://github.com/MariaDB/server/commit/ca091e6372) 2020-05-02 08:44:17 +0200 - Merge branch '10.1' into 10.2
* [Revision #28325b0863](https://github.com/MariaDB/server/commit/28325b0863)\
  2020-04-27 21:22:43 +0300
  * add WITH\_DBUG\_TRACE CMake variable
* [Revision #7a546650fa](https://github.com/MariaDB/server/commit/7a546650fa)\
  2020-04-29 17:02:30 +0300
  * [MDEV-20916](https://jira.mariadb.org/browse/MDEV-20916): Galera test failure on galera.galera\_parallel\_autoinc\_largetrx: Result content mismatch
* [Revision #ba2061da52](https://github.com/MariaDB/server/commit/ba2061da52)\
  2020-04-28 10:46:51 +1000
  * [MDEV-21595](https://jira.mariadb.org/browse/MDEV-21595): innodb offset\_t rename to rec\_offs
* [Revision #c238e9b96a](https://github.com/MariaDB/server/commit/c238e9b96a)\
  2020-04-04 13:27:43 +1100
  * [MDEV-20685](https://jira.mariadb.org/browse/MDEV-20685): compile fixes for Solaris/OSX/AIX
* [Revision #4af4284b79](https://github.com/MariaDB/server/commit/4af4284b79)\
  2020-04-29 11:06:48 +0400
  * [MDEV-22337](https://jira.mariadb.org/browse/MDEV-22337) Assertion \`Alloced\_length >= (str\_length + length +...
* Merge [Revision #dd5c307cb0](https://github.com/MariaDB/server/commit/dd5c307cb0) 2020-04-28 19:40:32 +0300 - [MDEV-22394](https://jira.mariadb.org/browse/MDEV-22394) Merge new release of InnoDB 5.7.30 to 10.2
* [Revision #2644e52fdb](https://github.com/MariaDB/server/commit/2644e52fdb)\
  2020-04-28 08:42:45 +0300
  * [MDEV-22384](https://jira.mariadb.org/browse/MDEV-22384) Wrong estimate of affected BLOB columns in update of PRIMARY KEY
* Merge [Revision #547cb280b8](https://github.com/MariaDB/server/commit/547cb280b8) 2020-04-28 19:39:40 +0300 - Merge 10.1 into 10.2
* [Revision #5a1d931529](https://github.com/MariaDB/server/commit/5a1d931529)\
  2020-04-28 19:05:56 +0300
  * Speed up innodb\_gis.rtree\_split
* [Revision #fae70d6b1c](https://github.com/MariaDB/server/commit/fae70d6b1c)\
  2020-04-28 09:47:40 +0300
  * Cleanup: Declare rtr\_get\_father\_node() statically
* [Revision #fb7c1b9415](https://github.com/MariaDB/server/commit/fb7c1b9415)\
  2020-04-22 15:39:40 +0200
  * [MDEV-21331](https://jira.mariadb.org/browse/MDEV-21331) installation fails on a server with containers
* [Revision #01f8f33b43](https://github.com/MariaDB/server/commit/01f8f33b43)\
  2020-04-23 12:25:15 +0200
  * [MDEV-21913](https://jira.mariadb.org/browse/MDEV-21913) Add pam\_user\_map.so file to binary tarball package
* [Revision #d0150dc14e](https://github.com/MariaDB/server/commit/d0150dc14e)\
  2020-04-27 21:46:05 +0300
  * [MDEV-20230](https://jira.mariadb.org/browse/MDEV-20230): mariadb-backup --ftwrl-wait-timeout never times out on explicit lock
* [Revision #581df0df89](https://github.com/MariaDB/server/commit/581df0df89)\
  2020-04-27 15:32:02 +0300
  * [MDEV-7962](https://jira.mariadb.org/browse/MDEV-7962): Follow-up fix for 10.2
* Merge [Revision #c06845d6f0](https://github.com/MariaDB/server/commit/c06845d6f0) 2020-04-27 13:28:13 +0300 - Merge 10.1 into 10.2
* [Revision #2c5067b689](https://github.com/MariaDB/server/commit/2c5067b689)\
  2020-04-07 13:14:41 +0300
  * cleanup THR\_KEY\_mysys
* [Revision #da7564edcf](https://github.com/MariaDB/server/commit/da7564edcf)\
  2020-04-24 10:46:33 +0300
  * Cleanup: Make row\_upd\_store\_row() static
* [Revision #57ec41d6ea](https://github.com/MariaDB/server/commit/57ec41d6ea)\
  2020-04-24 10:42:08 +0300
  * Cleanup: Remove a constant parameter
* [Revision #9f19dbe0c3](https://github.com/MariaDB/server/commit/9f19dbe0c3)\
  2020-04-23 19:33:55 +0300
  * [MDEV-22358](https://jira.mariadb.org/browse/MDEV-22358) Assertion srv\_undo\_sources || ... in row\_prebuilt\_free()
* Merge [Revision #e52a36d37b](https://github.com/MariaDB/server/commit/e52a36d37b) 2020-04-22 13:50:53 +0300 - Merge 10.1 into 10.2
* [Revision #8760ba6521](https://github.com/MariaDB/server/commit/8760ba6521)\
  2020-04-22 09:21:39 +0300
  * [MDEV-21807](https://jira.mariadb.org/browse/MDEV-21807) : galera.galera\_slave\_replay MTR failed: WSREP: Unknown parameter 'dbug
* [Revision #efa3b3de35](https://github.com/MariaDB/server/commit/efa3b3de35)\
  2020-04-21 21:14:54 +0300
  * [MDEV-22159](https://jira.mariadb.org/browse/MDEV-22159): Don't redirect as root to a tmp file not owned by root
* [Revision #a6a8774d47](https://github.com/MariaDB/server/commit/a6a8774d47)\
  2020-04-22 07:35:41 +0300
  * [MDEV-22181](https://jira.mariadb.org/browse/MDEV-22181) : galera.galera\_sst\_mysqldump\_with\_key MTR failed: INSERT failed: 1146: Table 'test.t1' doesn't exist
* [Revision #0efe1971c6](https://github.com/MariaDB/server/commit/0efe1971c6)\
  2020-04-20 17:23:43 +0300
  * [MDEV-19347](https://jira.mariadb.org/browse/MDEV-19347): mariadb-backup does not honor ignore\_db\_dirs from server config.
* [Revision #36bddacf6b](https://github.com/MariaDB/server/commit/36bddacf6b)\
  2020-04-18 11:51:21 +0300
  * Fixed multi\_update\_debug.test
* [Revision #0bcb65d358](https://github.com/MariaDB/server/commit/0bcb65d358)\
  2020-04-17 19:21:03 +0300
  * Don't write warning about uninitialized mutex if there is a memory leak
* [Revision #749b988794](https://github.com/MariaDB/server/commit/749b988794)\
  2020-04-18 00:32:24 +0300
  * Fixed memory leaks in resolve\_stack\_dump
* [Revision #48eda61cd4](https://github.com/MariaDB/server/commit/48eda61cd4)\
  2020-04-18 00:22:52 +0300
  * Fixed memory leak with DEFAULT(f) on Geometry field
* [Revision #a6d32976ae](https://github.com/MariaDB/server/commit/a6d32976ae)\
  2020-04-17 18:55:48 +0300
  * Fixed memory leak with fulltext indexes
* [Revision #70bb61414b](https://github.com/MariaDB/server/commit/70bb61414b)\
  2020-04-17 19:06:39 +0300
  * Fixed compiler warning in mysqltest.cc
* Merge [Revision #9e43ca8e8c](https://github.com/MariaDB/server/commit/9e43ca8e8c) 2020-04-15 15:05:45 +0300 - Merge 10.1 into 10.2
* Merge [Revision #ccaec18b39](https://github.com/MariaDB/server/commit/ccaec18b39) 2020-04-14 16:13:35 +0300 - Merge 10.1 into 10.2
* [Revision #e40ed0e881](https://github.com/MariaDB/server/commit/e40ed0e881)\
  2020-04-12 18:07:40 +0200
  * fix incorrect merge
* [Revision #06219c2ad4](https://github.com/MariaDB/server/commit/06219c2ad4)\
  2020-04-10 15:55:16 +0400
  * [MDEV-21599](https://jira.mariadb.org/browse/MDEV-21599) - plugins.server\_audit fails sporadically in buildbot
* [Revision #d565895bbd](https://github.com/MariaDB/server/commit/d565895bbd)\
  2020-04-07 22:26:11 +0200
  * fix rocksdb compression detection
* [Revision #5836191c8f](https://github.com/MariaDB/server/commit/5836191c8f)\
  2020-04-03 00:43:09 +0300
  * [MDEV-21168](https://jira.mariadb.org/browse/MDEV-21168): Active XA transactions stop slave from working after backup was restored.
* [Revision #cd88a606f5](https://github.com/MariaDB/server/commit/cd88a606f5)\
  2020-03-27 11:53:23 +1100
  * Correct FreeBSD cpuset\_t type
* [Revision #05e4a87c8b](https://github.com/MariaDB/server/commit/05e4a87c8b)\
  2020-04-01 16:25:07 +0400
  * A better fix for edd7e7c
* [Revision #cb4da5da74](https://github.com/MariaDB/server/commit/cb4da5da74)\
  2020-03-16 16:53:10 +0100
  * [MDEV-20604](https://jira.mariadb.org/browse/MDEV-20604): Duplicate key value is silently truncated to 64 characters in print\_keydup\_error
* [Revision #a1846b7a64](https://github.com/MariaDB/server/commit/a1846b7a64)\
  2020-03-25 12:09:47 +0200
  * [MDEV-22035](https://jira.mariadb.org/browse/MDEV-22035) Memory leak in main.mysqltest
* Merge [Revision #bc862c4ebe](https://github.com/MariaDB/server/commit/bc862c4ebe) 2020-04-01 09:19:37 +0300 - Merge 10.1 into 10.2
* [Revision #b1742a5c95](https://github.com/MariaDB/server/commit/b1742a5c95)\
  2020-04-01 09:13:01 +0300
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Improve innodb.xa\_recovery\_debug
* [Revision #fb217449dc](https://github.com/MariaDB/server/commit/fb217449dc)\
  2020-03-31 15:10:54 +0300
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Import and adapt innodb.xa\_recovery\_debug
* [Revision #2d16452a31](https://github.com/MariaDB/server/commit/2d16452a31)\
  2020-03-26 09:45:03 +0100
  * [MDEV-22021](https://jira.mariadb.org/browse/MDEV-22021): Galera database could get inconsistent with rollback to savepoint
* [Revision #5001487632](https://github.com/MariaDB/server/commit/5001487632)\
  2020-03-29 00:41:57 +0300
  * [MDEV-22074](https://jira.mariadb.org/browse/MDEV-22074) UBSAN: applying zero offset to null pointer in hash.c
* [Revision #edd7e7c85d](https://github.com/MariaDB/server/commit/edd7e7c85d)\
  2020-03-28 19:11:24 +0300
  * [MDEV-22069](https://jira.mariadb.org/browse/MDEV-22069) UBSAN: runtime error: member access within null pointer of type 'MY\_DIR\_HANDLE' in mysys/my\_lib.c
* [Revision #b11ff3d495](https://github.com/MariaDB/server/commit/b11ff3d495)\
  2020-03-30 08:03:54 +0530
  * [MDEV-22019](https://jira.mariadb.org/browse/MDEV-22019): Sig 11 in next\_breadth\_first\_tab | max\_sort\_length setting + double GROUP BY leads to crash
* [Revision #0b00c1a22f](https://github.com/MariaDB/server/commit/0b00c1a22f)\
  2020-03-23 02:08:01 +0300
  * [MDEV-22005](https://jira.mariadb.org/browse/MDEV-22005) UBSAN: applying non-zero offset 2 to null pointer in my\_charpos\_mb()
* [Revision #5918b17004](https://github.com/MariaDB/server/commit/5918b17004)\
  2020-03-24 11:01:42 +0200
  * [MDEV-21473](https://jira.mariadb.org/browse/MDEV-21473) conflicts with async slave BF aborting (#1475)
* [Revision #a7cbce06d4](https://github.com/MariaDB/server/commit/a7cbce06d4)\
  2020-03-23 16:47:43 +0300
  * unoptimized -fsanitize=undefined build on clang requires more stack space
* [Revision #fb74de9728](https://github.com/MariaDB/server/commit/fb74de9728)\
  2020-03-23 02:36:15 +0300
  * [MDEV-22006](https://jira.mariadb.org/browse/MDEV-22006) runtime error: null pointer passed as argument 2, which is declared to never be null in JOIN::copy\_ref\_ptr\_array()
* [Revision #6697135c6d](https://github.com/MariaDB/server/commit/6697135c6d)\
  2020-03-23 16:37:44 +0530
  * [MDEV-21572](https://jira.mariadb.org/browse/MDEV-21572) buf\_page\_get\_gen() should apply buffered page initialized redo log during recovery
* [Revision #1e6be69380](https://github.com/MariaDB/server/commit/1e6be69380)\
  2020-03-23 01:38:11 +0300
  * [MDEV-19658](https://jira.mariadb.org/browse/MDEV-19658) UBSAN: runtime error: load of value 2779096485, which is not a valid value for type 'enum\_binlog\_format'
* [Revision #82b3f1a80f](https://github.com/MariaDB/server/commit/82b3f1a80f)\
  2020-03-19 00:29:44 +0100
  * [MDEV-21930](https://jira.mariadb.org/browse/MDEV-21930) RocksDB does not compile anymore, with Visual Studio
* [Revision #ad6e421bd2](https://github.com/MariaDB/server/commit/ad6e421bd2)\
  2020-03-19 18:55:57 +0100
  * [MDEV-21360](https://jira.mariadb.org/browse/MDEV-21360) restore debud\_dbug through a session variable instead of '-d,..'
* [Revision #7e168634e9](https://github.com/MariaDB/server/commit/7e168634e9)\
  2020-03-21 20:37:00 +0300
  * blind fix for Windows building
* [Revision #5e9e0b8e3b](https://github.com/MariaDB/server/commit/5e9e0b8e3b)\
  2020-03-21 17:57:04 +0300
  * [MDEV-21993](https://jira.mariadb.org/browse/MDEV-21993) asan failure in encryption.innochecksum
* [Revision #23993c0036](https://github.com/MariaDB/server/commit/23993c0036)\
  2020-03-21 17:06:00 +0300
  * [MDEV-21993](https://jira.mariadb.org/browse/MDEV-21993) asan failure in encryption.innochecksum
* [Revision #de9072ca19](https://github.com/MariaDB/server/commit/de9072ca19)\
  2020-03-21 12:51:24 +0200
  * Connect: Remove some unused variables
* [Revision #45973ec610](https://github.com/MariaDB/server/commit/45973ec610)\
  2020-03-19 18:33:19 +0300
  * InnoDB: reduce size of dtuple\_t
* [Revision #54b2da9535](https://github.com/MariaDB/server/commit/54b2da9535)\
  2020-03-18 18:22:38 +0300
  * correct comment in buf\_page\_is\_corrupted()
* [Revision #1f53335d37](https://github.com/MariaDB/server/commit/1f53335d37)\
  2020-03-18 15:19:45 +0300
  * st\_::span fixes
* [Revision #884d22f288](https://github.com/MariaDB/server/commit/884d22f288)\
  2020-03-18 14:57:01 +0300
  * remove fishy reinterpret\_cast from buf\_page\_is\_zeroes()
* [Revision #2bde065525](https://github.com/MariaDB/server/commit/2bde065525)\
  2020-03-19 21:52:52 -0700
  * [MDEV-17177](https://jira.mariadb.org/browse/MDEV-17177) Crash in Item\_func\_in::cleanup() for SELECT executed via prepared statement
* [Revision #9f7b8625e6](https://github.com/MariaDB/server/commit/9f7b8625e6)\
  2020-03-20 17:40:39 +0200
  * [MDEV-14431](https://jira.mariadb.org/browse/MDEV-14431): Fix ulong/ulonglong type mismatch
* [Revision #b034d708c8](https://github.com/MariaDB/server/commit/b034d708c8)\
  2020-03-20 16:34:15 +0200
  * [MDEV-21549](https://jira.mariadb.org/browse/MDEV-21549): Clean up the import/export tests
* [Revision #b8b3edff13](https://github.com/MariaDB/server/commit/b8b3edff13)\
  2020-03-20 13:14:05 +0200
  * [MDEV-21549](https://jira.mariadb.org/browse/MDEV-21549) IMPORT TABLESPACE fails to adjust all tablespace ID in root pages
* Merge [Revision #c9ec1cc751](https://github.com/MariaDB/server/commit/c9ec1cc751) 2020-03-20 15:37:08 +0200 - Merge 10.1 into 10.2
* [Revision #a66eebf57c](https://github.com/MariaDB/server/commit/a66eebf57c)\
  2020-03-19 07:52:35 +0200
  * [MDEV-21981](https://jira.mariadb.org/browse/MDEV-21981) Replace arithmetic + with bitwise OR when possible
* [Revision #6960e9ed24](https://github.com/MariaDB/server/commit/6960e9ed24)\
  2020-03-19 14:23:47 +0200
  * [MDEV-21983](https://jira.mariadb.org/browse/MDEV-21983): Crash on DROP/RENAME TABLE after DISCARD TABLESPACE
* [Revision #9fd692aeca](https://github.com/MariaDB/server/commit/9fd692aeca)\
  2020-03-19 12:57:22 +0200
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Clean up the buffer pool resizing tests from MySQL 5.7
* [Revision #bfb5e1c3f0](https://github.com/MariaDB/server/commit/bfb5e1c3f0)\
  2020-03-19 07:46:30 +0200
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Import and adjust buffer pool resizing tests from MySQL 5.7
* [Revision #e28b4b68d3](https://github.com/MariaDB/server/commit/e28b4b68d3)\
  2020-03-19 06:58:49 +0200
  * [MDEV-14057](https://jira.mariadb.org/browse/MDEV-14057): Fix some tests
* [Revision #a0ce62f804](https://github.com/MariaDB/server/commit/a0ce62f804)\
  2020-03-18 13:55:21 +0400
  * [MDEV-14057](https://jira.mariadb.org/browse/MDEV-14057) InnoDB GIS tests fail.
* [Revision #09e8707d90](https://github.com/MariaDB/server/commit/09e8707d90)\
  2020-03-18 14:55:22 +0530
  * [MDEV-21826](https://jira.mariadb.org/browse/MDEV-21826) Recovery failure : loop of Read redo log up to LSN
* [Revision #6ecbb211c0](https://github.com/MariaDB/server/commit/6ecbb211c0)\
  2020-03-18 09:33:26 +0100
  * new (fixed) version of CC.
* [Revision #ab0034a789](https://github.com/MariaDB/server/commit/ab0034a789)\
  2020-03-17 16:28:16 +0200
  * [MDEV-20370](https://jira.mariadb.org/browse/MDEV-20370) Crash after OPTIMIZE TABLE on TEMPORARY TABLE
* [Revision #e61b99073f](https://github.com/MariaDB/server/commit/e61b99073f)\
  2020-03-17 19:22:20 +0530
  * [MDEV-14808](https://jira.mariadb.org/browse/MDEV-14808) innodb\_fts.sync fails in buildbot with wrong result
* [Revision #e64a3df4dc](https://github.com/MariaDB/server/commit/e64a3df4dc)\
  2020-03-17 13:11:46 +0400
  * [MDEV-21959](https://jira.mariadb.org/browse/MDEV-21959) GIS error message doesn't show the wrong value, just the type.
* [Revision #89698cef72](https://github.com/MariaDB/server/commit/89698cef72)\
  2020-03-17 10:32:42 +0200
  * [MDEV-10570](https://jira.mariadb.org/browse/MDEV-10570): Fix -Wmaybe-uninitialized
* [Revision #b1d7ba472e](https://github.com/MariaDB/server/commit/b1d7ba472e)\
  2020-03-11 22:00:14 +0100
  * innodb: fix typo in function description
* [Revision #ed21202a14](https://github.com/MariaDB/server/commit/ed21202a14)\
  2020-03-13 12:09:19 +0200
  * Fix GCC 10.0 -Wstringop-overflow
* [Revision #d9d3c222ca](https://github.com/MariaDB/server/commit/d9d3c222ca)\
  2020-03-12 17:47:54 +0530
  * [MDEV-10047](https://jira.mariadb.org/browse/MDEV-10047): table-based master info repository
* [Revision #9f858f38c0](https://github.com/MariaDB/server/commit/9f858f38c0)\
  2020-03-13 08:37:22 +0200
  * Fix clang 10 warnings
* [Revision #2e8b0c56a0](https://github.com/MariaDB/server/commit/2e8b0c56a0)\
  2020-03-13 08:07:02 +0200
  * [MDEV-21933](https://jira.mariadb.org/browse/MDEV-21933) INFORMATION\_SCHEMA.INNODB\_SYS\_TABLESPACES accesses SYS\_DATAFILES
* [Revision #47382a2f8c](https://github.com/MariaDB/server/commit/47382a2f8c)\
  2020-03-13 07:53:41 +0200
  * Fix GCC 10 -Wclass-memaccess
* [Revision #a8566f727f](https://github.com/MariaDB/server/commit/a8566f727f)\
  2020-03-13 07:39:14 +0200
  * Fix GCC 10 -Wstringop-truncation
* [Revision #2c8fa28f40](https://github.com/MariaDB/server/commit/2c8fa28f40)\
  2020-03-13 07:21:40 +0200
  * Update libmariadb
* Merge [Revision #32904dc5fa](https://github.com/MariaDB/server/commit/32904dc5fa) 2020-03-13 07:20:36 +0200 - Merge 10.1 into 10.2
* [Revision #5257bcfc7a](https://github.com/MariaDB/server/commit/5257bcfc7a)\
  2020-03-12 14:47:38 +0300
  * InnoDB: improve error message for checksum mismatch
* [Revision #069bad5e6b](https://github.com/MariaDB/server/commit/069bad5e6b)\
  2020-03-11 12:10:49 +0200
  * Add galera debug sync to galera\_slave\_replay test.
* [Revision #02343c4a54](https://github.com/MariaDB/server/commit/02343c4a54)\
  2020-03-10 15:46:29 +0200
  * [MDEV-19740](https://jira.mariadb.org/browse/MDEV-19740): Correct a type mismatch WITH\_INNODB\_EXTRA\_DEBUG
* [Revision #2b8b85bd0a](https://github.com/MariaDB/server/commit/2b8b85bd0a)\
  2020-03-10 15:14:53 +0300
  * fix use-after-free
* [Revision #69e4c74e07](https://github.com/MariaDB/server/commit/69e4c74e07)\
  2020-03-10 13:31:20 +0200
  * Make main.mysql\_client\_test non-great again
* Merge [Revision #8cd6cee876](https://github.com/MariaDB/server/commit/8cd6cee876) 2020-03-10 13:29:10 +0200 - Merge 10.1 into 10.2
* [Revision #7a52b6fd25](https://github.com/MariaDB/server/commit/7a52b6fd25)\
  2020-03-09 12:04:02 +0200
  * Minor cleanup of main.partition\_innodb
* [Revision #2bf4e574ad](https://github.com/MariaDB/server/commit/2bf4e574ad)\
  2020-03-09 09:00:14 +0200
  * [MDEV-21758](https://jira.mariadb.org/browse/MDEV-21758) : Events switched randomly to SLAVESIDE\_DISABLED
* [Revision #d7f74150e5](https://github.com/MariaDB/server/commit/d7f74150e5)\
  2020-03-07 19:21:40 +0200
  * Check for CPU\_COUNT macro within my\_getncpus
* [Revision #6610532170](https://github.com/MariaDB/server/commit/6610532170)\
  2020-03-07 14:46:40 +0200
  * Update install layout to account for multi-arch setup
* Merge [Revision #75d286c2cc](https://github.com/MariaDB/server/commit/75d286c2cc) 2020-03-06 15:42:45 +0100 - Merge branch '10.1' into 10.2
* [Revision #91aae18cc4](https://github.com/MariaDB/server/commit/91aae18cc4)\
  2020-03-06 13:46:19 +0200
  * Enable galera.galera\_ist\_mariadb-backup and galera.mysql-wsrep#33.
* [Revision #c5c1027c6e](https://github.com/MariaDB/server/commit/c5c1027c6e)\
  2020-02-26 13:46:27 +0200
  * [MDEV-19208](https://jira.mariadb.org/browse/MDEV-19208) mariadb.pc: install into libdir
* Merge [Revision #da10c6f448](https://github.com/MariaDB/server/commit/da10c6f448) 2020-03-05 10:52:43 +0200 - Merge branch '10.1' into 10.2
* [Revision #f0d2542a37](https://github.com/MariaDB/server/commit/f0d2542a37)\
  2020-03-02 16:35:57 +0100
  * [MDEV-21857](https://jira.mariadb.org/browse/MDEV-21857) - Fix sporadic failure of mdev375
* [Revision #8382f10691](https://github.com/MariaDB/server/commit/8382f10691)\
  2020-02-26 13:01:18 +0700
  * MENT-606 Error while setting value 'aes\_ctr' to 'file-key-management-encryption-algorithm'
* [Revision #42b29d4133](https://github.com/MariaDB/server/commit/42b29d4133)\
  2020-02-25 17:59:49 +0700
  * MENT-645 Undefined symbols for architecture x86\_64: \_pam\_syslog
* [Revision #4618c974e4](https://github.com/MariaDB/server/commit/4618c974e4)\
  2020-02-23 10:29:42 +0200
  * [MDEV-21723](https://jira.mariadb.org/browse/MDEV-21723) Async slave thread BF abort and replaying fixes (#1448)
* [Revision #3ce49a0a52](https://github.com/MariaDB/server/commit/3ce49a0a52)\
  2020-02-20 14:04:09 +0530
  * [MDEV-21563](https://jira.mariadb.org/browse/MDEV-21563) FTS thread aborts during shutdown
* [Revision #0d1dd2e79d](https://github.com/MariaDB/server/commit/0d1dd2e79d)\
  2020-02-20 09:25:05 +0100
  * Clean wrong cherry-pick from previous commit
* [Revision #fb01cc3766](https://github.com/MariaDB/server/commit/fb01cc3766)\
  2018-11-09 14:38:22 +1100
  * my\_getncpus based on threads available
* [Revision #959fc0c0cc](https://github.com/MariaDB/server/commit/959fc0c0cc)\
  2020-02-17 14:01:16 +0200
  * [MDEV-21591](https://jira.mariadb.org/browse/MDEV-21591) : galera.galera\_rsu\_add\_pk MTR failed: Result content mismatch
* [Revision #93dc3e2652](https://github.com/MariaDB/server/commit/93dc3e2652)\
  2020-02-13 13:33:41 +0200
  * [MDEV-21488](https://jira.mariadb.org/browse/MDEV-21488) : Galera test sporadic failure on galera.galera\_var\_notify\_cmd
* [Revision #ed10a8cd97](https://github.com/MariaDB/server/commit/ed10a8cd97)\
  2020-02-13 12:51:50 +0200
  * [MDEV-21515](https://jira.mariadb.org/browse/MDEV-21515) : Galera test sporadic failure on galera.galera\_wsrep\_new\_cluster: Result content mismatch
* [Revision #6c1e0c0493](https://github.com/MariaDB/server/commit/6c1e0c0493)\
  2020-02-13 10:30:40 +0200
  * [MDEV-21421](https://jira.mariadb.org/browse/MDEV-21421) : Galera test sporadic failure on galera.galera\_as\_slave\_gtid\_myisam: Result length mismatch
* [Revision #a6b92690e6](https://github.com/MariaDB/server/commit/a6b92690e6)\
  2020-02-12 10:32:30 +0200
  * [MDEV-21556](https://jira.mariadb.org/browse/MDEV-21556) : galera.lp1376747-4 MTR failed: Result length mismatch
* [Revision #f6663bfbd3](https://github.com/MariaDB/server/commit/f6663bfbd3)\
  2020-02-11 00:19:37 +0400
  * [MDEV-17941](https://jira.mariadb.org/browse/MDEV-17941) ALTER USER IF EXISTS does not work, although documentation says it should.
* [Revision #235d7c6f54](https://github.com/MariaDB/server/commit/235d7c6f54)\
  2020-02-06 12:14:40 +0100
  * Ignore /lib64 for rpm
* Merge [Revision #594282a534](https://github.com/MariaDB/server/commit/594282a534) 2020-02-10 14:31:39 +0100 - Merge branch '10.1' into 10.2
* [Revision #b08579aa28](https://github.com/MariaDB/server/commit/b08579aa28)\
  2020-01-30 21:11:24 +0100
  * [MDEV-16308](https://jira.mariadb.org/browse/MDEV-16308) : protocol messed up sporadically
* [Revision #6fc72ce169](https://github.com/MariaDB/server/commit/6fc72ce169)\
  2020-02-07 14:18:17 +0200
  * [MDEV-21667](https://jira.mariadb.org/browse/MDEV-21667) : Galera test failure on MW-336
* [Revision #0ea8894e52](https://github.com/MariaDB/server/commit/0ea8894e52)\
  2020-01-31 08:05:41 +0200
  * [MDEV-21601](https://jira.mariadb.org/browse/MDEV-21601) : Cleanup Galera disabled tests
* [Revision #785a9ac93a](https://github.com/MariaDB/server/commit/785a9ac93a)\
  2020-02-07 10:42:57 +0100
  * added warning to ignore
* [Revision #82c3b42a6e](https://github.com/MariaDB/server/commit/82c3b42a6e)\
  2020-02-06 20:03:04 +0100
  * Windows test fix
* [Revision #3be751d5b9](https://github.com/MariaDB/server/commit/3be751d5b9)\
  2020-02-07 16:01:31 +0530
  * [MDEV-21608](https://jira.mariadb.org/browse/MDEV-21608) Assertion \`n\_ext == dtuple\_get\_n\_ext(dtuple)' failed during updation of PK
* [Revision #ebbc572b82](https://github.com/MariaDB/server/commit/ebbc572b82)\
  2020-02-06 10:50:04 +0200
  * [MDEV-12121](https://jira.mariadb.org/browse/MDEV-12121): Clean up WITH\_INNODB\_AHI=OFF
* [Revision #236aed3f5f](https://github.com/MariaDB/server/commit/236aed3f5f)\
  2020-02-03 19:23:38 +0100
  * [MDEV-21656](https://jira.mariadb.org/browse/MDEV-21656): Wrong directory for pam\_user\_map.so JIRA:[MDEV-17292](https://jira.mariadb.org/browse/MDEV-17292)
* [Revision #a241d41195](https://github.com/MariaDB/server/commit/a241d41195)\
  2019-07-10 13:40:54 +0200
  * [MDEV-18027](https://jira.mariadb.org/browse/MDEV-18027): Running out of file descriptors and eventual crash
* [Revision #a9d1324867](https://github.com/MariaDB/server/commit/a9d1324867)\
  2020-02-03 12:10:59 +0200
  * Cleanup: Remove mem\_block\_t::magic\_n and mem\_block\_validate()
* [Revision #37b9734c06](https://github.com/MariaDB/server/commit/37b9734c06)\
  2020-02-03 10:02:58 +0200
  * [MDEV-21636](https://jira.mariadb.org/browse/MDEV-21636) information\_schema.innodb\_mutexes.name column is not populated
* [Revision #bd36a4ca12](https://github.com/MariaDB/server/commit/bd36a4ca12)\
  2020-01-30 13:11:06 +0800
  * introduce HASH\_REPLACE() for hash\_table\_t
* [Revision #256994ef74](https://github.com/MariaDB/server/commit/256994ef74)\
  2020-01-31 11:33:07 +0200
  * [MDEV-21586](https://jira.mariadb.org/browse/MDEV-21586): Fix a warning for converting my\_bool to bool
* Merge [Revision #2daf3b14fe](https://github.com/MariaDB/server/commit/2daf3b14fe) 2020-01-31 10:53:56 +0200 - Merge 10.1 into 10.2
* [Revision #f37a56de3c](https://github.com/MariaDB/server/commit/f37a56de3c)\
  2020-01-30 18:42:51 +0100
  * [MDEV-21586](https://jira.mariadb.org/browse/MDEV-21586) Server does not start if lc\_messages setting was not english.
* [Revision #07e34cddb6](https://github.com/MariaDB/server/commit/07e34cddb6)\
  2020-01-28 13:52:47 +0200
  * [MDEV-14330](https://jira.mariadb.org/browse/MDEV-14330): move tokudb manpages to right packages
* [Revision #a134ec3736](https://github.com/MariaDB/server/commit/a134ec3736)\
  2020-01-28 18:00:19 +0530
  * [MDEV-21550](https://jira.mariadb.org/browse/MDEV-21550) Assertion \`!table->fts->in\_queue' failed in fts\_optimize\_remove\_table
* [Revision #afc16a6faa](https://github.com/MariaDB/server/commit/afc16a6faa)\
  2020-01-27 15:08:36 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
