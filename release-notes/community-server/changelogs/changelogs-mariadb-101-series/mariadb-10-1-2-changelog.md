# MariaDB 10.1.2 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.2)[Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes)[Changelog](mariadb-10-1-2-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 7 Dec 2014

For the highlights of this release, see the [release notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #7856437](https://github.com/MariaDB/server/commit/7856437)\
  2014-08-29 14:07:43 +0300
  * my\_alloc.c - Changed 0x%lx -> %p
  * array.c: - Static (preallocated) buffer can now be anywhere
  * my\_sys.h - Define MY\_INIT\_BUFFER\_USED
  * sql\_delete.cc & sql\_lex.cc - Use memroot when allocating classes (avoids call to current\_thd)
  * sql\_explain.h: - Use preallocated buffers
  * sql\_explain.cc: - Use preallocated buffers and memroot
  * sql\_select.cc: - Use multi\_alloc\_root() instead of many alloc\_root() - Update calls to Explain
* [Revision #3392278](https://github.com/MariaDB/server/commit/3392278)\
  2014-12-04 17:44:46 +0400
  * [MDEV-7004](https://jira.mariadb.org/browse/MDEV-7004) - Merge scalability fixes from 10.0-power
* [Revision #eaa8c15](https://github.com/MariaDB/server/commit/eaa8c15)\
  2014-12-04 17:42:32 +0400
  * [MDEV-7004](https://jira.mariadb.org/browse/MDEV-7004) - Merge scalability fixes from 10.0-power
* [Revision #070a6e7](https://github.com/MariaDB/server/commit/070a6e7)\
  2014-08-29 14:09:51 +0300
  * Changed default values of query\_prealloc\_size and query\_alloc\_block\_size so that a simple query with one join would not have to call my\_malloc.
  * Allow lower limites for query\_prealloc\_size for testing.
  * Fixed wrong initialization of trans\_alloc\_block\_size
* [Revision #9127784](https://github.com/MariaDB/server/commit/9127784)\
  2014-12-04 17:35:55 +0400
  * Cherry pick dynamic array changes from commit:
* [Revision #9748087](https://github.com/MariaDB/server/commit/9748087)\
  2014-12-02 15:03:35 +0400
  * [MDEV-7004](https://jira.mariadb.org/browse/MDEV-7004) - Merge scalability fixes from 10.0-power
* [Revision #9e9f1da](https://github.com/MariaDB/server/commit/9e9f1da)\
  2014-12-02 14:59:01 +0400
  * [MDEV-7004](https://jira.mariadb.org/browse/MDEV-7004) - Merge scalability fixes from 10.0-power
* [Revision #b4ec230](https://github.com/MariaDB/server/commit/b4ec230)\
  2014-12-02 14:54:30 +0400
  * [MDEV-7004](https://jira.mariadb.org/browse/MDEV-7004) - Merge scalability fixes from 10.0-power
* [Revision #9bc5cec](https://github.com/MariaDB/server/commit/9bc5cec)\
  2014-12-02 14:50:18 +0400
  * [MDEV-7004](https://jira.mariadb.org/browse/MDEV-7004) - Merge scalability fixes from 10.0-power
* [Revision #faf169d](https://github.com/MariaDB/server/commit/faf169d)\
  2014-12-02 14:02:48 +0400
  * [MDEV-6906](https://jira.mariadb.org/browse/MDEV-6906) - Relaxed memory order for counters
* [Revision #732d2da](https://github.com/MariaDB/server/commit/732d2da)\
  2014-12-04 20:19:15 +0100
  * fix for 32-bit
* [Revision #6ea9036](https://github.com/MariaDB/server/commit/6ea9036)\
  2014-12-04 20:17:26 +0100
  * fix out-of-source builds
* [Revision #e1913ba](https://github.com/MariaDB/server/commit/e1913ba)\
  2014-12-04 15:58:25 +0100
  * fix set\_statement test for windows
* [Revision #7a47416](https://github.com/MariaDB/server/commit/7a47416)\
  2014-12-04 14:31:31 +0100
  * compilation failure on windows
* [Revision #c4cb15e](https://github.com/MariaDB/server/commit/c4cb15e)\
  2014-12-03 14:07:43 +0400
  * [MDEV-60](https://jira.mariadb.org/browse/MDEV-60) Support for Spatial Reference systems for the GIS data. The GEOMETRY field metadata is stored in the FRM file. SRID for a spatial column now can be stored, it was added to the CREATE TABLE syntax, so the AddGeometryData() stored procedure is now possible. Script adding the required Add/DropGeometryColumn sp-s added.
* [Revision #c4655cf](https://github.com/MariaDB/server/commit/c4655cf)\
  2014-11-14 13:46:21 +0100
  * cleanup: comments referring to non-extistent Item classes
* [Revision #65f0a8d](https://github.com/MariaDB/server/commit/65f0a8d)\
  2014-11-08 18:47:05 +0100
  * cleanup: sort and reorder %union elements in sql\_yacc.yy
* [Revision #227510e](https://github.com/MariaDB/server/commit/227510e)\
  2014-11-08 17:37:19 +0100
  * parser cleanup: don't store field properties in LEX, use Create\_field directly
* [Revision #d1522af](https://github.com/MariaDB/server/commit/d1522af)\
  2014-12-04 13:06:57 +0100
  * update 32-bit rdiff's
* [Revision #0fe39b6](https://github.com/MariaDB/server/commit/0fe39b6)\
  2014-12-04 12:40:19 +0200
  * [MDEV-7262](https://jira.mariadb.org/browse/MDEV-7262): innodb.innodb-mdev7046 and innodb-page\_compression\* fail on BuildBot
* [Revision #8360e1a](https://github.com/MariaDB/server/commit/8360e1a)\
  2014-12-03 23:51:47 +0100
  * [MDEV-6712](https://jira.mariadb.org/browse/MDEV-6712) THD specifics for plugins
* [Revision #0c7d773](https://github.com/MariaDB/server/commit/0c7d773)\
  2014-11-25 22:22:55 +0100
  * test for two password validation plugins
* [Revision #78cb6e3](https://github.com/MariaDB/server/commit/78cb6e3)\
  2014-11-25 21:48:13 +0100
  * cracklib\_password\_check plugin
* [Revision #7516a3c](https://github.com/MariaDB/server/commit/7516a3c)\
  2014-11-25 18:47:44 +0100
  * strict\_password\_validation
* [Revision #b814046](https://github.com/MariaDB/server/commit/b814046)\
  2014-11-25 10:07:59 +0100
  * validate SET PASSWORD
* [Revision #dccd85e](https://github.com/MariaDB/server/commit/dccd85e)\
  2014-11-24 21:02:57 +0100
  * cleanup: s/(OLD\_)?PASSWORD/&\_SYM/g
* [Revision #8934794](https://github.com/MariaDB/server/commit/8934794)\
  2014-11-25 18:53:40 +0100
  * password validation function in sql\_acl.cc
* [Revision #c98b2b3](https://github.com/MariaDB/server/commit/c98b2b3)\
  2014-11-25 21:58:14 +0100
  * password validation plugin type and a simple plugin
* [Revision #b5357f0](https://github.com/MariaDB/server/commit/b5357f0)\
  2014-11-25 19:05:49 +0100
  * GRANT: calculate pasword hash in sql\_acl.cc
* [Revision #7bd9eb1](https://github.com/MariaDB/server/commit/7bd9eb1)\
  2014-11-24 16:55:56 +0100
  * parser: store the password hash in LEX\_USER::auth, not in ::password
* [Revision #91ad0cd](https://github.com/MariaDB/server/commit/91ad0cd)\
  2014-11-24 16:53:51 +0100
  * sql\_acl.cc: better recognize the context to tell the role from a user
* [Revision #bc603c6](https://github.com/MariaDB/server/commit/bc603c6)\
  2014-11-24 15:10:51 +0100
  * bugfix: IDENTIFIED BY clause was lost in some GRANT variants
* [Revision #61820bc](https://github.com/MariaDB/server/commit/61820bc)\
  2014-11-24 14:07:42 +0100
  * cleanup: sql\_acl.cc
* [Revision #f5722f5](https://github.com/MariaDB/server/commit/f5722f5)\
  2014-11-23 20:30:56 +0100
  * cleanup: normalize LEX\_USER to get rid of different representation of the same thing
* [Revision #c1204da](https://github.com/MariaDB/server/commit/c1204da)\
  2014-11-23 19:36:08 +0100
  * cleanup: bool\_variable= -1; -> bool\_variable= true;
* [Revision #7f856f0](https://github.com/MariaDB/server/commit/7f856f0)\
  2014-11-21 17:53:16 +0100
  * remove unsupported service file
* [Revision #4027e3b](https://github.com/MariaDB/server/commit/4027e3b)\
  2014-11-21 14:45:25 +0100
  * don't load plugin of unsupported types
* [Revision #77e3cb7](https://github.com/MariaDB/server/commit/77e3cb7)\
  2014-10-23 21:01:52 +0200
  * cleanup: sql\_plugin.cc
* [Revision #bdb222b](https://github.com/MariaDB/server/commit/bdb222b)\
  2014-12-03 14:25:01 +0100
  * update 32-bit rdiff's
* [Revision #23fa0a3](https://github.com/MariaDB/server/commit/23fa0a3)\
  2014-11-29 19:49:42 +0100
  * fix a comment
* [Revision #fc40f81](https://github.com/MariaDB/server/commit/fc40f81)\
  2014-11-29 00:53:09 +0100
  * a case of uninitialized variable
* [Revision #e4f9739](https://github.com/MariaDB/server/commit/e4f9739)\
  2014-11-29 00:52:48 +0100
  * [MDEV-6999](https://jira.mariadb.org/browse/MDEV-6999) Remove or deprecate unused variables
* [Revision #6a2fbdf](https://github.com/MariaDB/server/commit/6a2fbdf)\
  2014-11-29 00:29:40 +0100
  * [MDEV-6979](https://jira.mariadb.org/browse/MDEV-6979) simplify trigger rules for RBR triggers
* [Revision #1bd1c29](https://github.com/MariaDB/server/commit/1bd1c29)\
  2014-11-28 22:39:22 +0100
  * [MDEV-6895](https://jira.mariadb.org/browse/MDEV-6895) switch to dynamic libjemalloc.so
* [Revision #0438f12](https://github.com/MariaDB/server/commit/0438f12)\
  2014-11-27 09:45:10 +0100
  * [MDEV-6980](https://jira.mariadb.org/browse/MDEV-6980) OUT parameters in PREPARE
* [Revision #717a264](https://github.com/MariaDB/server/commit/717a264)\
  2014-11-26 20:49:24 +0100
  * [MDEV-6894](https://jira.mariadb.org/browse/MDEV-6894) Enable SEQUENCE engine by default
* [Revision #69d700a](https://github.com/MariaDB/server/commit/69d700a)\
  2014-11-26 20:34:40 +0100
  * [MDEV-5871](https://jira.mariadb.org/browse/MDEV-5871) support assisted discovery in oqgraph v3
* [Revision #2ef0312](https://github.com/MariaDB/server/commit/2ef0312)\
  2014-11-26 20:33:50 +0100
  * oqgraph cleanup: remove casts
* [Revision #2ae7541](https://github.com/MariaDB/server/commit/2ae7541)\
  2014-11-19 09:13:38 +0100
  * cleanup: s/const CHARSET\_INFO/CHARSET\_INFO/
* [Revision #0d30423](https://github.com/MariaDB/server/commit/0d30423)\
  2014-11-19 08:55:06 +0100
  * cleanup: reuse MY\_CHECK\_AND\_SET\_COMPILER\_FLAG in sphinx/CMakeLists.txt
* [Revision #d2a78de](https://github.com/MariaDB/server/commit/d2a78de)\
  2014-11-18 11:36:15 +0100
  * cleanup: ptr\_cmp
* [Revision #20c3b2f](https://github.com/MariaDB/server/commit/20c3b2f)\
  2014-11-16 13:15:35 +0100
  * [MDEV-6311](https://jira.mariadb.org/browse/MDEV-6311) Add errors on CREATE SERVER
* [Revision #97a913e](https://github.com/MariaDB/server/commit/97a913e)\
  2014-11-16 13:12:58 +0100
  * cleanup: freshen up CREATE SERVER code
* [Revision #a50ddeb](https://github.com/MariaDB/server/commit/a50ddeb)\
  2014-12-03 22:30:48 -0500
  * [MDEV-6593](https://jira.mariadb.org/browse/MDEV-6593) : domain\_id based replication filters
* [Revision #7bf4f9f](https://github.com/MariaDB/server/commit/7bf4f9f)\
  2014-12-03 21:33:34 +0100
  * followup for [MDEV-6996](https://jira.mariadb.org/browse/MDEV-6996), update tests and results
* [Revision #24a6b41](https://github.com/MariaDB/server/commit/24a6b41)\
  2014-12-03 13:45:21 +0200
  * Move page initialization to better place.
* [Revision #316d8c7](https://github.com/MariaDB/server/commit/316d8c7)\
  2014-12-03 11:58:33 +0100
  * compiler warning
* [Revision #ec4137c](https://github.com/MariaDB/server/commit/ec4137c)\
  2014-12-03 11:37:26 +0100
  * Merge branch '10.1' into bb-10.1-merge
* [Revision #1caee39](https://github.com/MariaDB/server/commit/1caee39)\
  2014-12-02 22:25:53 +0100
  * disable mroonga temporarily: see [MDEV-7246](https://jira.mariadb.org/browse/MDEV-7246)
* [Revision #853077a](https://github.com/MariaDB/server/commit/853077a)\
  2014-12-02 22:25:16 +0100
  * Merge branch '10.0' into bb-10.1-merge
* [Revision #bf3b4a2](https://github.com/MariaDB/server/commit/bf3b4a2)\
  2014-12-01 16:43:09 +0100
  * fix mysqld\_safe to work
* [Revision #dbbe831](https://github.com/MariaDB/server/commit/dbbe831)\
  2014-12-01 15:25:07 +0100
  * don't skip wsrep position recovery silently
* [Revision #aa4ad1c](https://github.com/MariaDB/server/commit/aa4ad1c)\
  2014-12-01 13:43:17 +0100
  * update result files
* [Revision #bb070f9](https://github.com/MariaDB/server/commit/bb070f9)\
  2014-12-01 10:31:31 +0100
  * [MDEV-7188](https://jira.mariadb.org/browse/MDEV-7188) main.signal\_demo3 and sys\_vars.max\_sp\_recursion\_depth\_func fail in biuldbot on labrador with Thread stack overrun
* [Revision #2b40a38](https://github.com/MariaDB/server/commit/2b40a38)\
  2014-11-30 21:13:41 -0500
  * [MDEV-4412](https://jira.mariadb.org/browse/MDEV-4412) : SLOW QUERY LOG - add affected rows (UPDATE / DELETE) in slow query log
* [Revision #b16b072](https://github.com/MariaDB/server/commit/b16b072)\
  2014-11-30 09:26:32 +0100
  * Make test results stable.
* [Revision #2e728c7](https://github.com/MariaDB/server/commit/2e728c7)\
  2014-11-30 08:32:36 +0100
  * rdiff not needed anymore
* [Revision #3e792e6](https://github.com/MariaDB/server/commit/3e792e6)\
  2014-11-30 01:05:34 -0500
  * [MDEV-4018](https://jira.mariadb.org/browse/MDEV-4018) : Feature Request: microseconds in GET\_LOCK()
* [Revision #5298e21](https://github.com/MariaDB/server/commit/5298e21)\
  2014-11-30 00:12:45 -0500
  * [MDEV-6961](https://jira.mariadb.org/browse/MDEV-6961): mysqld should terminate when started with --wsrep-recover
* [Revision #f7708d6](https://github.com/MariaDB/server/commit/f7708d6)\
  2014-11-29 22:29:03 +0100
  * fixes for --embedded
* [Revision #d0d6284](https://github.com/MariaDB/server/commit/d0d6284)\
  2014-11-28 00:29:37 +0400
  * [MDEV-4045](https://jira.mariadb.org/browse/MDEV-4045) Missing OGC Spatial functions.
* [Revision #7b55b67](https://github.com/MariaDB/server/commit/7b55b67)\
  2014-11-27 20:11:14 +0200
  * [MDEV-7228](https://jira.mariadb.org/browse/MDEV-7228): innodb.innodb-page\_compression\_tables, innodb.innodb-page\_compression\_zip, innodb.innodb\_stats\_create\_on\_corrupted fail with embedded server
* [Revision #55e99b2](https://github.com/MariaDB/server/commit/55e99b2)\
  2014-11-26 13:28:46 +0400
  * [MDEV-7162](https://jira.mariadb.org/browse/MDEV-7162) main.mysqld--help fails in buildbot on Windows:
* [Revision #98a78c4](https://github.com/MariaDB/server/commit/98a78c4)\
  2014-11-25 09:11:48 +0200
  * [MDEV-7181](https://jira.mariadb.org/browse/MDEV-7181): innodb.innodb\_defrag\_concurrent fails in buildbot
* [Revision #afe6d88](https://github.com/MariaDB/server/commit/afe6d88)\
  2014-11-24 21:29:12 +0200
  * [MDEV-7167](https://jira.mariadb.org/browse/MDEV-7167): innodb.innodb\_bug12902967 fails in buildbot on Windows
* [Revision #96b031b](https://github.com/MariaDB/server/commit/96b031b)\
  2014-11-24 20:27:43 +0200
  * [MDEV-7169](https://jira.mariadb.org/browse/MDEV-7169): innodb.innodb\_bug14147491 fails in buildbot on Windows
* [Revision #8ba3585](https://github.com/MariaDB/server/commit/8ba3585)\
  2014-11-24 19:42:39 +0200
  * [MDEV-7168](https://jira.mariadb.org/browse/MDEV-7168): Tests innodb.innodb\_stats\_create\_table innodb.innodb\_stats\_drop\_locked fail and innodb.innodb\_stats\_fetch\_nonexistent fails in buildbot on Windows
* [Revision #1ac12df](https://github.com/MariaDB/server/commit/1ac12df)\
  2014-11-24 15:20:23 +0200
  * [MDEV-7164](https://jira.mariadb.org/browse/MDEV-7164): innodb.innodb-alter-table-disk-full fails in buildbot on Windows
* [Revision #c0a00a2](https://github.com/MariaDB/server/commit/c0a00a2)\
  2014-11-24 12:25:56 +0400
  * [MDEV-7171](https://jira.mariadb.org/browse/MDEV-7171) funcs\_1.is\_tables\_is and main.information\_schema-big fail in buildbot. test results updated with the new GIS-related IS tables.
* [Revision #1a05bb4](https://github.com/MariaDB/server/commit/1a05bb4)\
  2014-11-24 10:01:49 +0200
  * [MDEV-7166](https://jira.mariadb.org/browse/MDEV-7166): innodb.innodb-page\_compression\_zip fails in buildbot
* [Revision #deffb95](https://github.com/MariaDB/server/commit/deffb95)\
  2014-11-23 09:55:57 -0500
  * [MDEV-7161](https://jira.mariadb.org/browse/MDEV-7161): Build failure in buildbot on work-amd64-valgrind
* [Revision #369c026](https://github.com/MariaDB/server/commit/369c026)\
  2014-11-22 14:33:51 -0500
  * [MDEV-7053](https://jira.mariadb.org/browse/MDEV-7053): WSREP\_STATUS & WSREP\_MEMBERSHIP I\_S tables
* [Revision #cbc318f](https://github.com/MariaDB/server/commit/cbc318f)\
  2014-11-20 21:29:11 +0400
  * Removing some duplicate code: deriving Item\_func\_opt\_neg from Item\_bool\_func.
* [Revision #52b3d95](https://github.com/MariaDB/server/commit/52b3d95)\
  2014-11-20 12:56:47 +0400
  * Deriving Item\_bool\_func from Item\_bool\_func2.
* [Revision #969f491](https://github.com/MariaDB/server/commit/969f491)\
  2014-11-20 11:59:00 +0400
  * [MDEV-7005](https://jira.mariadb.org/browse/MDEV-7005) NULLIF does not work as documented [MDEV-7146](https://jira.mariadb.org/browse/MDEV-7146) NULLIF returns unexpected result with a YEAR field
* [Revision #9f4abde](https://github.com/MariaDB/server/commit/9f4abde)\
  2014-11-19 21:34:51 +0400
  * Sharing similar code between Item\_func\_ifnull and Item\_func\_if
* [Revision #b432c7b](https://github.com/MariaDB/server/commit/b432c7b)\
  2014-11-19 14:58:48 +0200
  * [MDEV-7133](https://jira.mariadb.org/browse/MDEV-7133): InnoDB: Assertion failure in dict\_tf\_is\_valid
* [Revision #7bf391c](https://github.com/MariaDB/server/commit/7bf391c)\
  2014-11-17 09:55:55 +0200
  * [MDEV-7108](https://jira.mariadb.org/browse/MDEV-7108): Make long semaphore wait timeout configurable
* [Revision #ea83226](https://github.com/MariaDB/server/commit/ea83226)\
  2014-11-12 15:37:52 +0200
  * [MDEV-7088](https://jira.mariadb.org/browse/MDEV-7088): Query stats for compression based on TRIM size
* [Revision #1827d9e](https://github.com/MariaDB/server/commit/1827d9e)\
  2014-10-24 10:13:08 +0200
  * [MDEV-5231](https://jira.mariadb.org/browse/MDEV-5231): Per query variables from Percona Server (rewritten)
* [Revision #a03dd94](https://github.com/MariaDB/server/commit/a03dd94)\
  2014-11-06 13:17:11 +0200
  * [MDEV-6936](https://jira.mariadb.org/browse/MDEV-6936): Buffer pool list scan optimization
* [Revision #84de277](https://github.com/MariaDB/server/commit/84de277)\
  2014-11-05 09:18:47 +0200
  * Fix error message output if posix\_fallocate (trim) is not successfull.
* [Revision #8b1b62d](https://github.com/MariaDB/server/commit/8b1b62d)\
  2014-11-04 15:41:39 +0200
  * Fix compiler failure on Windows.
* [Revision #8e27845](https://github.com/MariaDB/server/commit/8e27845)\
  2014-11-04 15:02:49 +0400
  * A follow up fix for [MDEV-5528](https://jira.mariadb.org/browse/MDEV-5528) (forgot to do "git add" for two files in the previous commit for [MDEV-5528](https://jira.mariadb.org/browse/MDEV-5528))
* [Revision #251fa7f](https://github.com/MariaDB/server/commit/251fa7f)\
  2014-11-04 12:26:48 +0200
  * Fix error on trim operation alligment. Furthermore, make sure that we do not return simulated out of file space on read operation, that would cause crash.
* [Revision #43f185e](https://github.com/MariaDB/server/commit/43f185e)\
  2014-11-03 21:45:06 +0400
  * [MDEV-5528](https://jira.mariadb.org/browse/MDEV-5528) Command line variable to choose MariaDB-5.3 vs MySQL-5.6 temporal data formats
* [Revision #a245543](https://github.com/MariaDB/server/commit/a245543)\
  2014-11-03 19:05:16 +0400
  * [MDEV-6649](https://jira.mariadb.org/browse/MDEV-6649) Different warnings for TIME and TIME(N) when @@old\_mode=zero\_date\_time\_cast Merging from 10.0 (pre-requisite for [MDEV-5528](https://jira.mariadb.org/browse/MDEV-5528))
* [Revision #cb37c55](https://github.com/MariaDB/server/commit/cb37c55)\
  2014-11-03 11:18:52 +0200
  * [MDEV-6929](https://jira.mariadb.org/browse/MDEV-6929): Port Facebook Prefix Index Queries Optimization
* [Revision #3c2c036](https://github.com/MariaDB/server/commit/3c2c036)\
  2014-10-29 22:31:19 -0400
  * [MDEV-6939](https://jira.mariadb.org/browse/MDEV-6939) : Dots in file names of configuration files
* [Revision #822dc6f](https://github.com/MariaDB/server/commit/822dc6f)\
  2014-10-29 22:28:14 -0400
  * mysys/mf\_fn\_ext.c: typos & indents
* [Revision #2bf3e41](https://github.com/MariaDB/server/commit/2bf3e41)\
  2014-10-29 13:49:12 +0200
  * [MDEV-6932](https://jira.mariadb.org/browse/MDEV-6932): Enable Lazy Flushing
* [Revision #58888e2](https://github.com/MariaDB/server/commit/58888e2)\
  2014-10-29 10:42:27 +0200
  * [MDEV-6935](https://jira.mariadb.org/browse/MDEV-6935): Change the default value for innodb\_log\_compressed\_pages to false
* [Revision #2d2d11f](https://github.com/MariaDB/server/commit/2d2d11f)\
  2014-10-29 08:39:48 +0200
  * [MDEV-6968](https://jira.mariadb.org/browse/MDEV-6968): CREATE TABLE crashes with InnoDB plugin
* [Revision #b96697d](https://github.com/MariaDB/server/commit/b96697d)\
  2014-10-28 14:49:31 +0400
  * [MDEV-6648](https://jira.mariadb.org/browse/MDEV-6648): InnoDB: Add support for 4K sector size if supported
* [Revision #e48fbd2](https://github.com/MariaDB/server/commit/e48fbd2)\
  2014-10-28 14:49:31 +0400
  * Increase the version number
* [Revision #5ff6f6f](https://github.com/MariaDB/server/commit/5ff6f6f)\
  2014-10-27 21:19:12 -0400
  * Added SST scripts to the server package.
* [Revision #9646f94](https://github.com/MariaDB/server/commit/9646f94)\
  2014-10-27 16:34:53 +0200
  * [MDEV-6759](https://jira.mariadb.org/browse/MDEV-6759): innodb valgrind failures
* [Revision #0a16fe4](https://github.com/MariaDB/server/commit/0a16fe4)\
  2014-10-24 17:12:03 +0500
  * GIS-related test results updated.
* [Revision #cc656e4](https://github.com/MariaDB/server/commit/cc656e4)\
  2014-10-22 16:14:25 +0300
  * Enhance row-merge sort progress logging.
* [Revision #c3db445](https://github.com/MariaDB/server/commit/c3db445)\
  2014-09-02 11:31:26 +0500
  * [MDEV-12](https://jira.mariadb.org/browse/MDEV-12) OpenGIS: create required tables: GeometryColumns, related views. GEOMETRY\_COLUMNS and SPATIAL\_REF\_SYS tables added to the INFORMATION\_SCHEMA.
* [Revision #c1f5f61](https://github.com/MariaDB/server/commit/c1f5f61)\
  2014-10-20 15:53:07 +0300
  * Make sure that information schema knows also page compressed page type and that we decompress fist page if it is page compressed before really accessing it.
* [Revision #d249199](https://github.com/MariaDB/server/commit/d249199)\
  2014-10-19 09:50:50 -0700
  * Correction for the fix of the bug [MDEV-6874](https://jira.mariadb.org/browse/MDEV-6874).
* [Revision #ec89abf](https://github.com/MariaDB/server/commit/ec89abf)\
  2014-10-17 14:06:54 -0700
  * Merge branch '10.1' of ../10.1-mdev334 into 10.1
* [Revision #aa0fd5c](https://github.com/MariaDB/server/commit/aa0fd5c)\
  2014-10-17 23:24:00 +0400
  * [MDEV-6388](https://jira.mariadb.org/browse/MDEV-6388): ANALYZE $stmt output in the slow query log
* [Revision #47ced65](https://github.com/MariaDB/server/commit/47ced65)\
  2014-10-17 22:47:06 +0400
  * [MDEV-6388](https://jira.mariadb.org/browse/MDEV-6388): ANALYZE $stmt output in the slow query log
* [Revision #d3bdc14](https://github.com/MariaDB/server/commit/d3bdc14)\
  2014-10-17 14:21:40 +0400
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #d44dd54](https://github.com/MariaDB/server/commit/d44dd54)\
  2014-10-17 14:18:10 +0400
  * [MDEV-6400](https://jira.mariadb.org/browse/MDEV-6400): "ANALYZE SELECT ... INTO @var" doesn't set @var

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
