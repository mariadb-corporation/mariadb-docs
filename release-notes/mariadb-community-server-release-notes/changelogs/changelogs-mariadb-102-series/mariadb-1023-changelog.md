# MariaDB 10.2.3 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/release-notes-mariadb-10-2-series/mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.3)[Release Notes](../../old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md)[Changelog](mariadb-1023-changelog.md)[Overview of 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md)

**Release date:** 24 Dec 2016

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.2) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #0c3791c](https://github.com/MariaDB/server/commit/0c3791c)\
  2016-12-22 14:02:27 +0400
  * [MDEV-11227](https://jira.mariadb.org/browse/MDEV-11227) - mysqlimport -l doesn't issue UNLOCK TABLES
* [Revision #9b10b41](https://github.com/MariaDB/server/commit/9b10b41)\
  2016-12-22 10:17:26 +0100
  * update libmariadb, and fix debian packaging for client libs
* [Revision #27f20d1](https://github.com/MariaDB/server/commit/27f20d1)\
  2016-12-21 13:21:38 +0400
  * Updated test results
* [Revision #8774a02](https://github.com/MariaDB/server/commit/8774a02)\
  2016-12-08 14:20:46 +0400
  * [MDEV-11227](https://jira.mariadb.org/browse/MDEV-11227) - mysqlimport -l doesn't issue UNLOCK TABLES
* [Revision #561b6d2](https://github.com/MariaDB/server/commit/561b6d2)\
  2016-12-20 22:46:29 +0200
  * Revert "Merge pull request #275 from grooverdan/10.2-[MDEV-11075](https://jira.mariadb.org/browse/MDEV-11075)-crc32-runtime-detect-getauxval"
* [Revision #229dd71](https://github.com/MariaDB/server/commit/229dd71)\
  2016-12-20 22:42:13 +0200
  * [MDEV-11585](https://jira.mariadb.org/browse/MDEV-11585) Hard-code the shared InnoDB temporary tablespace ID
* [Revision #9b27d3e](https://github.com/MariaDB/server/commit/9b27d3e)\
  2016-12-20 11:08:50 -0800
  * Fixed bug [MDEV-11608](https://jira.mariadb.org/browse/MDEV-11608).
* [Revision #95228dc](https://github.com/MariaDB/server/commit/95228dc)\
  2016-12-20 17:32:08 +0400
  * [MDEV-11570](https://jira.mariadb.org/browse/MDEV-11570) JSON\_MERGE returns incorrect result.
* [Revision #83dbb2d](https://github.com/MariaDB/server/commit/83dbb2d)\
  2016-12-20 12:07:33 +0200
  * [MDEV-11487](https://jira.mariadb.org/browse/MDEV-11487) Revert InnoDB internal temporary tables from [WL#7682](https://askmonty.org/worklog/?tid=7682)
* [Revision #1152b07](https://github.com/MariaDB/server/commit/1152b07)\
  2016-12-20 00:42:13 -0800
  * Corrected a test from func\_date\_add.test
* [Revision #5c69879](https://github.com/MariaDB/server/commit/5c69879)\
  2016-12-20 00:36:59 -0800
  * Fixed bug [MDEV-11593](https://jira.mariadb.org/browse/MDEV-11593).
* [Revision #2c734e7](https://github.com/MariaDB/server/commit/2c734e7)\
  2016-12-19 16:12:26 -0500
  * [MDEV-10993](https://jira.mariadb.org/browse/MDEV-10993): wsrep.mdev\_10186 result depends on location of
* [Revision #b800264](https://github.com/MariaDB/server/commit/b800264)\
  2016-12-19 16:11:27 -0500
  * [MDEV-11152](https://jira.mariadb.org/browse/MDEV-11152): wsrep\_replicate\_myisam: SELECT gets replicated
* [Revision #d51e7f9](https://github.com/MariaDB/server/commit/d51e7f9)\
  2016-12-19 15:55:55 -0500
  * [MDEV-10957](https://jira.mariadb.org/browse/MDEV-10957): Assertion failure when dropping a myisam table
* [Revision #9d8ec14](https://github.com/MariaDB/server/commit/9d8ec14)\
  2016-12-19 15:50:33 -0500
  * [MDEV-11082](https://jira.mariadb.org/browse/MDEV-11082): Fix mysql\_client\_test.c (by Elena)
* [Revision #da4babb](https://github.com/MariaDB/server/commit/da4babb)\
  2016-12-19 15:47:01 -0500
  * Fix failing galera tests.
* [Revision #a01bfc9](https://github.com/MariaDB/server/commit/a01bfc9)\
  2016-12-19 15:57:41 +0200
  * [MDEV-11602](https://jira.mariadb.org/browse/MDEV-11602) InnoDB leaks foreign key metadata on DDL operations
* [Revision #8375a2c](https://github.com/MariaDB/server/commit/8375a2c)\
  2016-12-16 16:36:54 +0200
  * [MDEV-11585](https://jira.mariadb.org/browse/MDEV-11585) Hard-code the shared InnoDB temporary tablespace ID at -1
* [Revision #c35b8c4](https://github.com/MariaDB/server/commit/c35b8c4)\
  2016-12-15 11:03:34 +1100
  * Travis: parallel\_jobs=3
* [Revision #ce55094](https://github.com/MariaDB/server/commit/ce55094)\
  2016-12-16 14:06:12 +0400
  * [MDEV-11572](https://jira.mariadb.org/browse/MDEV-11572) JSON\_DEPTH returns wrong results.
* [Revision #30c231b](https://github.com/MariaDB/server/commit/30c231b)\
  2016-12-16 13:51:35 +0400
  * [MDEV-11569](https://jira.mariadb.org/browse/MDEV-11569) JSON\_ARRAY\_INSERT produces an invalid result.
* [Revision #beded43](https://github.com/MariaDB/server/commit/beded43)\
  2016-12-16 12:43:44 +0400
  * MDEV-JSON\_CONTAINS\_PATH returns incorrect results and produces wrong warning.
* [Revision #e5377be](https://github.com/MariaDB/server/commit/e5377be)\
  2016-12-16 12:32:56 +0400
  * [MDEV-11562](https://jira.mariadb.org/browse/MDEV-11562) Assertion \`js->state == JST\_VALUE' failed in check\_contains(json\_engine\_t\*, json\_engine\_t\*).
* [Revision #8938031](https://github.com/MariaDB/server/commit/8938031)\
  2016-12-14 17:47:10 +0100
  * InnoDB: don't stop purge threads if there's work to do
* [Revision #8d77085](https://github.com/MariaDB/server/commit/8d77085)\
  2016-12-14 17:46:58 +0100
  * InnoDB purge thread and other bg threads
* [Revision #eabb0ae](https://github.com/MariaDB/server/commit/eabb0ae)\
  2016-12-14 17:47:24 +0100
  * sporadic crashes of innodb.innodb\_prefix\_index\_restart\_server
* [Revision #a8e0c6f](https://github.com/MariaDB/server/commit/a8e0c6f)\
  2016-12-15 09:59:40 +1100
  * Travis: add refs for future capability - when travis catches up
* [Revision #e14bdcb](https://github.com/MariaDB/server/commit/e14bdcb)\
  2016-08-24 13:29:09 +1000
  * travis: gcc-5 and gcc-6
* [Revision #9213ac8](https://github.com/MariaDB/server/commit/9213ac8)\
  2016-12-15 02:35:31 +0200
  * Follow-up for a411d7f4f6 - change in formatting of SHOW CREATE TABLE
* [Revision #a1833ac](https://github.com/MariaDB/server/commit/a1833ac)\
  2016-12-15 02:34:02 +0200
  * Follow-up for 180065ebb0 - removal of redundant parentheses
* [Revision #5cf6fd3](https://github.com/MariaDB/server/commit/5cf6fd3)\
  2016-12-14 12:11:02 -0800
  * Adjusted test results after merge.
* [Revision #441fa00](https://github.com/MariaDB/server/commit/441fa00)\
  2016-12-14 10:11:52 -0800
  * Fixed bug [MDEV-11488](https://jira.mariadb.org/browse/MDEV-11488).
* [Revision #e9ada86](https://github.com/MariaDB/server/commit/e9ada86)\
  2016-12-12 16:42:25 +1100
  * Travis: add lib{stemmer,xml2,pcre3}-dev
* [Revision #44e7995](https://github.com/MariaDB/server/commit/44e7995)\
  2016-12-13 12:55:18 +0100
  * buildbot issues
* [Revision #65b4d74](https://github.com/MariaDB/server/commit/65b4d74)\
  2016-12-13 11:52:23 +0200
  * Merge the test innodb.innodb\_misc1 into innodb.innodb.
* [Revision #d26b9f6](https://github.com/MariaDB/server/commit/d26b9f6)\
  2016-12-13 12:39:48 +0400
  * [MDEV-11470](https://jira.mariadb.org/browse/MDEV-11470) JSON\_KEYS accepts arguments in invalid format.
* [Revision #1b7a794](https://github.com/MariaDB/server/commit/1b7a794)\
  2016-12-12 22:33:27 +0100
  * [MDEV-11540](https://jira.mariadb.org/browse/MDEV-11540) Unexpected system threads in the process list
* [Revision #8541626](https://github.com/MariaDB/server/commit/8541626)\
  2016-12-12 18:35:30 +0100
  * [MDEV-11518](https://jira.mariadb.org/browse/MDEV-11518) Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed in Field\_long::val\_int()
* [Revision #c697ddc](https://github.com/MariaDB/server/commit/c697ddc)\
  2016-12-12 15:47:51 +0100
  * cleanup: remove unused handler table flag
* [Revision #b3e3356](https://github.com/MariaDB/server/commit/b3e3356)\
  2016-12-07 10:10:08 +0100
  * bugfix: reset MODE\_NO\_BACKSLASH\_ESCAPES during vcol parsing
* [Revision #a9a362d](https://github.com/MariaDB/server/commit/a9a362d)\
  2016-11-29 22:10:13 +0100
  * Aria: test for ER\_KEY\_BASED\_ON\_GENERATED\_VIRTUAL\_COLUMN
* [Revision #9d7c3cb](https://github.com/MariaDB/server/commit/9d7c3cb)\
  2016-04-01 22:45:32 +0200
  * CONNECT: simple vcol test
* [Revision #5d5e832](https://github.com/MariaDB/server/commit/5d5e832)\
  2016-11-28 12:46:49 +0100
  * weird compilation fix
* [Revision #8c876ad](https://github.com/MariaDB/server/commit/8c876ad)\
  2016-11-28 00:12:00 +0100
  * Item\_func\_like: print a not like b instead of !(a like b)
* [Revision #180065e](https://github.com/MariaDB/server/commit/180065e)\
  2016-11-27 19:50:10 +0100
  * Item::print(): remove redundant parentheses
* [Revision #1db438c](https://github.com/MariaDB/server/commit/1db438c)\
  2016-11-24 09:49:12 +0100
  * [MDEV-11066](https://jira.mariadb.org/browse/MDEV-11066) use MySQL terminology for "virtual columns"
* [Revision #6eaa5fd](https://github.com/MariaDB/server/commit/6eaa5fd)\
  2016-11-17 15:47:27 +0100
  * bugfix: InnoDB doesn't support ICP on vcols
* [Revision #44ca499](https://github.com/MariaDB/server/commit/44ca499)\
  2016-11-16 21:53:35 +0100
  * bugfix: partitioning and keyread on an indexed vcol
* [Revision #2a0f7a3](https://github.com/MariaDB/server/commit/2a0f7a3)\
  2016-11-08 17:24:42 +0100
  * bugfix: non-deterministic vcols in partitioning
* [Revision #d1f3763](https://github.com/MariaDB/server/commit/d1f3763)\
  2016-11-08 14:57:43 +0100
  * bugfix: non-deterministic vcols in indexes
* [Revision #6b0f4c2](https://github.com/MariaDB/server/commit/6b0f4c2)\
  2016-11-08 12:09:05 +0100
  * cleanup: unpack\_vcol\_info\_from\_frm
* [Revision #a72f1de](https://github.com/MariaDB/server/commit/a72f1de)\
  2016-11-07 23:18:03 +0100
  * rename Virtual\_column\_info::expr\_item
* [Revision #a411d7f](https://github.com/MariaDB/server/commit/a411d7f)\
  2016-11-07 17:17:40 +0100
  * store/show vcols as item->print()
* [Revision #8b3b6dc](https://github.com/MariaDB/server/commit/8b3b6dc)\
  2016-11-21 15:04:57 +0100
  * test how MDL blocks InnoDB purge
* [Revision #1cae1af](https://github.com/MariaDB/server/commit/1cae1af)\
  2016-11-07 22:35:02 +0100
  * [MDEV-5800](https://jira.mariadb.org/browse/MDEV-5800) InnoDB support for indexed vcols
* [Revision #7fca91f](https://github.com/MariaDB/server/commit/7fca91f)\
  2016-11-26 15:26:34 +0100
  * cleanup: InnoDB, dict\_create\_add\_foreign\_to\_dictionary()
* [Revision #528dd5f](https://github.com/MariaDB/server/commit/528dd5f)\
  2016-11-26 14:43:30 +0100
  * cleanup: InnoDB, remove index\_field\_t::col\_name
* [Revision #b66976a](https://github.com/MariaDB/server/commit/b66976a)\
  2016-11-26 14:10:53 +0100
  * cleanup: InnoDB, various minor issues
* [Revision #a6f05b9](https://github.com/MariaDB/server/commit/a6f05b9)\
  2016-11-26 13:38:46 +0100
  * cleanup: redundant casts in THD::dec\_thread\_count
* [Revision #0d6a773](https://github.com/MariaDB/server/commit/0d6a773)\
  2016-11-26 13:37:53 +0100
  * cleanup: unused handler::check\_if\_supported\_virtual\_columns()
* [Revision #2614a0a](https://github.com/MariaDB/server/commit/2614a0a)\
  2016-11-20 11:23:48 +0100
  * extend prelocking to FK-accessed tables
* [Revision #f136291](https://github.com/MariaDB/server/commit/f136291)\
  2016-11-10 16:10:41 +0100
  * cleanup: sp\_head::add\_used\_tables\_to\_table\_list()
* [Revision #a3614d3](https://github.com/MariaDB/server/commit/a3614d3)\
  2016-11-10 14:56:51 +0100
  * cleanup: FOREIGN\_KEY\_INFO
* [Revision #94462aa](https://github.com/MariaDB/server/commit/94462aa)\
  2016-11-19 16:23:33 +0100
  * bugfix: remove broken insert t values () optimization
* [Revision #56c1f8d](https://github.com/MariaDB/server/commit/56c1f8d)\
  2016-11-16 20:33:45 +0100
  * bugfix: table->get\_fields\_in\_item\_tree=true
* [Revision #f73bdb6](https://github.com/MariaDB/server/commit/f73bdb6)\
  2016-11-23 16:42:09 +0100
  * bugfix: UPDATE and virtual BLOBs
* [Revision #aebb103](https://github.com/MariaDB/server/commit/aebb103)\
  2016-11-23 12:54:59 +0100
  * bugfix: multi-UPDATE, vcols, const tables
* [Revision #0e401bf](https://github.com/MariaDB/server/commit/0e401bf)\
  2016-10-22 17:33:42 +0200
  * bugfix: move vcol calculations down into the handler
* [Revision #b8f51c0](https://github.com/MariaDB/server/commit/b8f51c0)\
  2016-11-16 19:26:55 +0100
  * bugfix: update-behind-insert
* [Revision #54ab7db](https://github.com/MariaDB/server/commit/54ab7db)\
  2016-11-16 14:04:49 +0100
  * cleanup: remove now-unused TABLE::merge\_keys
* [Revision #b38ff28](https://github.com/MariaDB/server/commit/b38ff28)\
  2016-11-16 14:04:37 +0100
  * bugfix: mark\_columns\_needed\_for\_update
* [Revision #d137b4d](https://github.com/MariaDB/server/commit/d137b4d)\
  2016-11-23 17:33:40 +0100
  * [MDEV-5800](https://jira.mariadb.org/browse/MDEV-5800) MyISAM support for indexed vcols
* [Revision #a418c99](https://github.com/MariaDB/server/commit/a418c99)\
  2016-11-07 16:48:50 +0100
  * gcol mysql-test suite from 5.7
* [Revision #4136968](https://github.com/MariaDB/server/commit/4136968)\
  2016-10-15 23:53:14 +0200
  * enable spatial indexes in innodb vcol tests
* [Revision #c2b2cb8](https://github.com/MariaDB/server/commit/c2b2cb8)\
  2016-11-24 16:07:19 +0100
  * TABLE::update\_virtual\_field to compute just one vcol
* [Revision #2cdcf14](https://github.com/MariaDB/server/commit/2cdcf14)\
  2016-03-11 13:46:46 +0100
  * make myisamchk -d ignore HA\_CREATE\_RELIES\_ON\_SQL\_LAYER
* [Revision #5d6aab8](https://github.com/MariaDB/server/commit/5d6aab8)\
  2016-03-11 13:40:31 +0100
  * cleanup: minor issues in MyISAM
* [Revision #961fc6a](https://github.com/MariaDB/server/commit/961fc6a)\
  2016-11-24 16:08:35 +0100
  * cleanup: T\_REP/T\_REP\_BY\_SORT/T\_REP\_PARALLEL in MyISAM
* [Revision #b634bd5](https://github.com/MariaDB/server/commit/b634bd5)\
  2016-11-24 14:55:01 +0100
  * cleanup: move all Item processors together
* [Revision #acfc3ba](https://github.com/MariaDB/server/commit/acfc3ba)\
  2016-11-11 13:31:34 +0100
  * cleanup: remove ONLY\_FOR\_MYSQL\_CLOSED\_SOURCE\_SCHEDULED
* [Revision #d4170f6](https://github.com/MariaDB/server/commit/d4170f6)\
  2016-11-16 19:03:51 +0100
  * cleanup: set\_field\_ptr()
* [Revision #65e53c8](https://github.com/MariaDB/server/commit/65e53c8)\
  2016-10-18 10:17:55 +0200
  * cleanup: Field\_blob::get\_ptr()
* [Revision #9a3ec79](https://github.com/MariaDB/server/commit/9a3ec79)\
  2016-11-07 21:47:48 +0100
  * cleanup: TABLE::update\_virtual\_fields
* [Revision #8b6c054](https://github.com/MariaDB/server/commit/8b6c054)\
  2016-11-21 16:16:52 +0100
  * bugfix: stored column depends on virtual depends on updated
* [Revision #1008949](https://github.com/MariaDB/server/commit/1008949)\
  2016-04-01 18:40:31 +0200
  * cleanup: update\_virtual\_fields()
* [Revision #a632df9](https://github.com/MariaDB/server/commit/a632df9)\
  2016-11-15 16:07:37 +0100
  * improve Item\_field::register\_field\_in\_read\_map()
* [Revision #7459f0c](https://github.com/MariaDB/server/commit/7459f0c)\
  2016-04-01 19:51:57 +0200
  * cleanup: don't update\_virtual\_fields from READ\_RECORD
* [Revision #163478d](https://github.com/MariaDB/server/commit/163478d)\
  2016-10-23 14:04:57 +0200
  * cleanup: InnoDB: is\_partition()
* [Revision #4aab058](https://github.com/MariaDB/server/commit/4aab058)\
  2016-10-11 16:10:47 +0200
  * cleanup: spatial indexes in MyISAM
* [Revision #b2c8d55](https://github.com/MariaDB/server/commit/b2c8d55)\
  2016-11-14 20:24:03 +0100
  * cleanup: unused open\_table\_from\_share() flags
* [Revision #db3f110](https://github.com/MariaDB/server/commit/db3f110)\
  2016-03-09 12:32:35 +0100
  * cleanup: remove unused Field::utype values
* [Revision #4210538](https://github.com/MariaDB/server/commit/4210538)\
  2016-01-13 17:43:54 +0100
  * cleanup: avoid Field::field\_index
* [Revision #03a0623](https://github.com/MariaDB/server/commit/03a0623)\
  2016-01-13 13:42:46 +0100
  * cleanup: rename a method
* [Revision #46ae210](https://github.com/MariaDB/server/commit/46ae210)\
  2016-11-26 13:04:36 +0100
  * cleanup: my\_strerror
* [Revision #590d473](https://github.com/MariaDB/server/commit/590d473)\
  2016-11-12 15:17:18 +0100
  * cleanup: my\_printf\_error(ER\_xxx, ER(ER\_xxx), ... )
* [Revision #605cf619](https://github.com/MariaDB/server/commit/605cf619)\
  2016-01-09 00:02:56 +0100
  * cleanup: extra\_rec\_buf\_length
* [Revision #98be2d8](https://github.com/MariaDB/server/commit/98be2d8)\
  2016-11-08 12:25:45 +0100
  * cleanup: old (harmless?) typo fixed
* [Revision #d2408e4](https://github.com/MariaDB/server/commit/d2408e4)\
  2016-04-01 18:42:15 +0200
  * cleanup: fix a comment
* [Revision #3a3017a](https://github.com/MariaDB/server/commit/3a3017a)\
  2016-11-15 19:00:00 +0100
  * cleanup: set\_thd\_proc\_info()
* [Revision #9bcfd27](https://github.com/MariaDB/server/commit/9bcfd27)\
  2015-11-28 18:25:05 +0100
  * cleanup: remove dead (half-merged) code from partition\_info.\*
* [Revision #5b716bc](https://github.com/MariaDB/server/commit/5b716bc)\
  2015-11-25 08:02:52 +0100
  * cleanup: reorder TABLE members
* [Revision #0ed291e](https://github.com/MariaDB/server/commit/0ed291e)\
  2016-11-28 11:27:47 +0100
  * cleanup: parser: s/USER/USER\_SYM/
* [Revision #0bef3bb](https://github.com/MariaDB/server/commit/0bef3bb)\
  2015-11-20 13:11:35 +0100
  * cleanup: remove Item::intro\_version
* [Revision #d440319](https://github.com/MariaDB/server/commit/d440319)\
  2016-11-23 20:12:28 +0100
  * cleanup: TABLE::init()
* [Revision #335082e](https://github.com/MariaDB/server/commit/335082e)\
  2016-11-03 12:39:04 +0100
  * cleanup: remove bad String=0 assignment
* [Revision #a721dca](https://github.com/MariaDB/server/commit/a721dca)\
  2016-11-27 19:30:20 +0100
  * cleanup: Item\_func\_opt\_neg::negate()
* [Revision #fd00440](https://github.com/MariaDB/server/commit/fd00440)\
  2016-11-04 11:16:13 +0100
  * don't convert WEEK(x) to WEEK(x, @@default\_week\_format)
* [Revision #867809f](https://github.com/MariaDB/server/commit/867809f)\
  2016-11-08 20:04:09 +0100
  * bugfix: compile InnoDB w/o P\_S
* [Revision #75925f8](https://github.com/MariaDB/server/commit/75925f8)\
  2016-11-06 22:25:39 +0100
  * bugfix: Item\_func\_spatial\_collection::print()
* [Revision #75fb321](https://github.com/MariaDB/server/commit/75fb321)\
  2016-11-06 21:21:00 +0100
  * bugfix: Item\_func\_dyncol\_add::print()
* [Revision #0980627](https://github.com/MariaDB/server/commit/0980627)\
  2016-11-04 16:54:58 +0100
  * bugfix: Item\_func\_weight\_string::print()
* [Revision #232dc91](https://github.com/MariaDB/server/commit/232dc91)\
  2016-11-03 22:40:19 +0100
  * bugfix: Item\_func\_like::print() was losing ESCAPE clause
* [Revision #660355c](https://github.com/MariaDB/server/commit/660355c)\
  2016-11-02 21:08:49 +0100
  * bugfix: Item\_func\_get\_system\_var::print()
* [Revision #96bb5f4](https://github.com/MariaDB/server/commit/96bb5f4)\
  2016-11-03 17:30:17 +0100
  * bugfix: returning on-the-stack buffer to the caller
* [Revision #a838b10](https://github.com/MariaDB/server/commit/a838b10)\
  2016-11-08 09:24:23 +0100
  * bugfix: delayed insert table was using other table's expr\_arena
* [Revision #0852cf5](https://github.com/MariaDB/server/commit/0852cf5)\
  2016-10-15 23:51:03 +0200
  * say MariaDB in InnoDB error messages, not MySQL
* [Revision #f7dcd8a](https://github.com/MariaDB/server/commit/f7dcd8a)\
  2016-10-23 00:13:11 +0200
  * shut up annoying InnoDB warning when --gdb
* [Revision #b8dfedd](https://github.com/MariaDB/server/commit/b8dfedd)\
  2016-10-18 16:46:53 +0200
  * the mysql-test combination is 'innodb' not 'xtradb'
* [Revision #e336fc0](https://github.com/MariaDB/server/commit/e336fc0)\
  2016-10-25 15:47:53 +0200
  * fix stack traces when linking with libbfd
* [Revision #855f0b9](https://github.com/MariaDB/server/commit/855f0b9)\
  2016-03-18 14:12:03 +0100
  * update RPM metadata (vendor and contact)
* Merge [Revision #edf4cc7](https://github.com/MariaDB/server/commit/edf4cc7) 2016-12-12 09:56:42 +0200 - Merge pull request #275 from grooverdan/10.2-[MDEV-11075](https://jira.mariadb.org/browse/MDEV-11075)-crc32-runtime-detect-getauxval
* [Revision #e76183f0](https://github.com/MariaDB/server/commit/e76183f0)\
  2016-12-12 15:35:08 +1100
  * [MDEV-11075](https://jira.mariadb.org/browse/MDEV-11075): Power - runtime detection of optimized instructions
* [Revision #9320d8a](https://github.com/MariaDB/server/commit/9320d8a)\
  2016-12-11 01:12:33 +0400
  * [MDEV-11453](https://jira.mariadb.org/browse/MDEV-11453) JSON\_CONTAINS returns incorrect values.
* [Revision #c868acd](https://github.com/MariaDB/server/commit/c868acd)\
  2016-12-05 21:04:30 +0200
  * [MDEV-11487](https://jira.mariadb.org/browse/MDEV-11487) Revert InnoDB internal temporary tables from [WL#7682](https://askmonty.org/worklog/?tid=7682)
* [Revision #b0266b6](https://github.com/MariaDB/server/commit/b0266b6)\
  2016-12-09 12:03:24 +0200
  * Use mtr\_memo\_contains\_flagged() instead of mtr\_memo\_contains().
* [Revision #63152a5](https://github.com/MariaDB/server/commit/63152a5)\
  2016-12-09 12:00:19 +0200
  * Port the test innodb.innodb\_misc1 from MySQL.
* [Revision #04aa31c](https://github.com/MariaDB/server/commit/04aa31c)\
  2016-12-09 12:26:32 +0400
  * [MDEV-11469](https://jira.mariadb.org/browse/MDEV-11469) JSON\_SEARCH returns incorrect results.
* Merge [Revision #0f7864a](https://github.com/MariaDB/server/commit/0f7864a) 2016-12-09 09:26:10 +0200 - Merge branch 'grooverdan-10.2-[MDEV-9872](https://jira.mariadb.org/browse/MDEV-9872)-crc32-generic-message' into 10.2
* [Revision #c6017b7](https://github.com/MariaDB/server/commit/c6017b7)\
  2016-12-09 09:12:32 +0200
  * Address my review comments in the contributed patch.
* Merge [Revision #64d29c6](https://github.com/MariaDB/server/commit/64d29c6) 2016-12-09 09:04:35 +0200 - Merge branch '10.2-[MDEV-9872](https://jira.mariadb.org/browse/MDEV-9872)-crc32-generic-message' of [mariadb-server](https://github.com/grooverdan/mariadb-server) into grooverdan-10.2-[MDEV-9872](https://jira.mariadb.org/browse/MDEV-9872)-crc32-generic-message
* [Revision #50617c4](https://github.com/MariaDB/server/commit/50617c4)\
  2016-12-09 15:29:42 +1100
  * [MDEV-11075](https://jira.mariadb.org/browse/MDEV-11075): allow software crc32c on Power8 (for BE)
* [Revision #410bf82](https://github.com/MariaDB/server/commit/410bf82)\
  2016-12-05 08:35:55 +1100
  * [MDEV-9872](https://jira.mariadb.org/browse/MDEV-9872): Valgrind supports CRC32B and CRC32Q since valgrind-3.6.1
* [Revision #6d12569](https://github.com/MariaDB/server/commit/6d12569)\
  2016-12-01 13:17:19 +1100
  * [MDEV-9872](https://jira.mariadb.org/browse/MDEV-9872): crc32 initialization (innodb/xtradb)
* [Revision #ba6af68](https://github.com/MariaDB/server/commit/ba6af68)\
  2016-12-01 12:35:59 +1100
  * [MDEV-9872](https://jira.mariadb.org/browse/MDEV-9872): Generic CRC32 message using ptr
* Merge [Revision #2b6498b](https://github.com/MariaDB/server/commit/2b6498b) 2016-12-09 08:20:27 +0200 - Merge pull request #274 from grooverdan/10.2-[MDEV-11075](https://jira.mariadb.org/browse/MDEV-11075)-innochecksum-bigendian-optimised
* [Revision #850ed6e](https://github.com/MariaDB/server/commit/850ed6e)\
  2016-12-09 14:58:23 +1100
  * [MDEV-11075](https://jira.mariadb.org/browse/MDEV-11075): changing to algorithm innodb from crc32
* [Revision #7ca1e2a](https://github.com/MariaDB/server/commit/7ca1e2a)\
  2016-12-08 14:34:54 +0200
  * [MDEV-11422](https://jira.mariadb.org/browse/MDEV-11422) rpl.rpl\_parallel\_optimistic\_nobinlog failed in buildbot with "InnoDB: Killing connection failed Deadlock"
* [Revision #6816c80](https://github.com/MariaDB/server/commit/6816c80)\
  2016-12-08 15:41:09 +0100
  * [MDEV-11435](https://jira.mariadb.org/browse/MDEV-11435) - fix integer divided by zero exception when calculating buffer pool size
* [Revision #7f6710e](https://github.com/MariaDB/server/commit/7f6710e)\
  2016-12-08 11:25:21 +0400
  * [MDEV-11489](https://jira.mariadb.org/browse/MDEV-11489) Assertion \`0' failed in json\_find\_path.
* Merge [Revision #9ea5de3](https://github.com/MariaDB/server/commit/9ea5de3) 2016-12-07 09:19:27 +0200 - Merge branch 'sensssz-10.2-vats' into 10.2
* Merge [Revision #7f504c7](https://github.com/MariaDB/server/commit/7f504c7) 2016-12-07 09:18:41 +0200 - Merge branch '10.2-vats' of [server](https://github.com/sensssz/server) into sensssz-10.2-vats
* [Revision #02c8852](https://github.com/MariaDB/server/commit/02c8852)\
  2016-12-01 13:50:00 -0500
  * Bug fix: consider lock wait mode first.
* [Revision #3371904](https://github.com/MariaDB/server/commit/3371904)\
  2016-12-06 01:39:06 +0400
  * [MDEV-11447](https://jira.mariadb.org/browse/MDEV-11447) JSON\_MERGE merges valid JSON objects incorrectly.
* [Revision #fba1eab](https://github.com/MariaDB/server/commit/fba1eab)\
  2016-12-06 01:35:40 +0400
  * [MDEV-11446](https://jira.mariadb.org/browse/MDEV-11446) JSON\_MERGE accepts arguments in invalid format.
* [Revision #3bae532](https://github.com/MariaDB/server/commit/3bae532)\
  2016-12-06 01:32:13 +0400
  * [MDEV-11433](https://jira.mariadb.org/browse/MDEV-11433) JSON\_MERGE returns a non-NULL result with a NULL argument.
* [Revision #486079d](https://github.com/MariaDB/server/commit/486079d)\
  2016-12-06 00:39:53 +0400
  * [MDEV-11440](https://jira.mariadb.org/browse/MDEV-11440) JSON has become a reserved word in MariaDB.
* [Revision #3743b4c](https://github.com/MariaDB/server/commit/3743b4c)\
  2016-12-06 00:34:25 +0400
  * [MDEV-11468](https://jira.mariadb.org/browse/MDEV-11468) JSON\_UNQUOTE returns incorrect results.
* Merge [Revision #0009f4a](https://github.com/MariaDB/server/commit/0009f4a) 2016-12-05 17:12:29 +0200 - Merge pull request #268 from grooverdan/10.2-[MDEV-10651](https://jira.mariadb.org/browse/MDEV-10651)-enable-test-sys\_vars.innodb\_buffer\_pool\_dump\_pct\_basic
* [Revision #6924593](https://github.com/MariaDB/server/commit/6924593)\
  2016-12-05 10:42:42 +1100
  * [MDEV-10651](https://jira.mariadb.org/browse/MDEV-10651): enable test sys\_vars.innodb\_buffer\_pool\_dump\_pct\_basic
* Merge [Revision #660521a](https://github.com/MariaDB/server/commit/660521a) 2016-12-05 17:01:28 +0200 - Merge pull request #263 from grooverdan/10.2-[MDEV-11451](https://jira.mariadb.org/browse/MDEV-11451)-isfinite
* [Revision #b11eb36](https://github.com/MariaDB/server/commit/b11eb36)\
  2016-12-01 17:14:47 +1100
  * [MDEV-11451](https://jira.mariadb.org/browse/MDEV-11451): isinf || isnan -> !isfinite
* [Revision #cc85ba8](https://github.com/MariaDB/server/commit/cc85ba8)\
  2016-12-05 15:25:59 +0200
  * [MDEV-11233](https://jira.mariadb.org/browse/MDEV-11233) CREATE FULLTEXT INDEX with a token longer than 127 bytes crashes server
* [Revision #1da0865](https://github.com/MariaDB/server/commit/1da0865)\
  2016-12-05 09:34:28 +0400
  * [MDEV-11467](https://jira.mariadb.org/browse/MDEV-11467) JSON\_EXTRACT returns incorrect results.
* [Revision #2b01461](https://github.com/MariaDB/server/commit/2b01461)\
  2016-12-05 08:59:55 +0400
  * [MDEV-11465](https://jira.mariadb.org/browse/MDEV-11465) JSON\_LENGTH returns incorrect length.
* [Revision #75a5181](https://github.com/MariaDB/server/commit/75a5181)\
  2016-12-05 08:52:37 +0400
  * [MDEV-11448](https://jira.mariadb.org/browse/MDEV-11448) Assertion \`\*p\_cur\_step < p->last\_step' failed in strings/json\_lib.c handle\_match.
* [Revision #fe6d0a0](https://github.com/MariaDB/server/commit/fe6d0a0)\
  2016-12-05 08:43:15 +0400
  * [MDEV-11471](https://jira.mariadb.org/browse/MDEV-11471) JSON\_ARRAY\_APPEND returns incorrect results.
* [Revision #abb80d2](https://github.com/MariaDB/server/commit/abb80d2)\
  2016-12-05 08:03:11 +0400
  * [MDEV-11472](https://jira.mariadb.org/browse/MDEV-11472) JSON\_ARRAY\_INSERT returns incorrect results.
* [Revision #df87dce](https://github.com/MariaDB/server/commit/df87dce)\
  2016-12-05 07:42:00 +0400
  * [MDEV-11473](https://jira.mariadb.org/browse/MDEV-11473) JSON\_REMOVE returns invalid results.
* [Revision #7e03c67](https://github.com/MariaDB/server/commit/7e03c67)\
  2016-12-05 07:17:54 +0400
  * [MDEV-11474](https://jira.mariadb.org/browse/MDEV-11474) JSON\_DEPTH returns incorrect results.
* [Revision #78dc7c3](https://github.com/MariaDB/server/commit/78dc7c3)\
  2016-12-05 01:01:09 +0400
  * [MDEV-11461](https://jira.mariadb.org/browse/MDEV-11461) JSON\_TYPE does not recognize integer/double types.
* [Revision #5454500](https://github.com/MariaDB/server/commit/5454500)\
  2016-12-05 00:15:08 +0400
  * [MDEV-11452](https://jira.mariadb.org/browse/MDEV-11452) JSON\_CONTAINS accepts wrong number of arguments.
* [Revision #c89c514](https://github.com/MariaDB/server/commit/c89c514)\
  2016-12-04 23:57:26 +0400
  * [MDEV-11445](https://jira.mariadb.org/browse/MDEV-11445) JSON\_MERGE requires at least two arguments in MySQL, but not in MariaDB.
* [Revision #12897a5](https://github.com/MariaDB/server/commit/12897a5)\
  2016-12-04 14:49:06 +0400
  * [MDEV-11437](https://jira.mariadb.org/browse/MDEV-11437) JSON\_QUOTE function does not quote and uses wrong character set.
* [Revision #b4cbaf0](https://github.com/MariaDB/server/commit/b4cbaf0)\
  2016-12-04 14:22:01 +0400
  * [MDEV-11436](https://jira.mariadb.org/browse/MDEV-11436) CREATE TABLE .. AS SELECT JSON\_OBJECT truncates data.
* [Revision #f391ab4](https://github.com/MariaDB/server/commit/f391ab4)\
  2016-12-04 13:57:46 +0400
  * [MDEV-11438](https://jira.mariadb.org/browse/MDEV-11438) Assertion \`null\_value' failed in Item::send(Protocol\*, String\*) upon casting NULL as JSON.
* [Revision #f105014](https://github.com/MariaDB/server/commit/f105014)\
  2016-12-03 12:41:19 +0400
  * [MDEV-11464](https://jira.mariadb.org/browse/MDEV-11464) Server crashes in mark\_object upon JSON\_VALID.
* [Revision #7fca133](https://github.com/MariaDB/server/commit/7fca133)\
  2016-12-03 12:36:10 +0400
  * [MDEV-11463](https://jira.mariadb.org/browse/MDEV-11463) Server crashes in mark\_array upon JSON\_VALID.
* [Revision #edc75c9](https://github.com/MariaDB/server/commit/edc75c9)\
  2016-12-03 12:11:06 +0400
  * [MDEV-11450](https://jira.mariadb.org/browse/MDEV-11450) Assertion \`!null\_value' failed invirtual bool Item::send on json\_search.
* [Revision #a8467e2](https://github.com/MariaDB/server/commit/a8467e2)\
  2016-12-03 11:45:24 +0400
  * [MDEV-11449](https://jira.mariadb.org/browse/MDEV-11449) Server crashes in Item\_func\_or\_sum::agg\_item\_collations.
* [Revision #eca1579](https://github.com/MariaDB/server/commit/eca1579)\
  2016-12-03 11:32:47 +0400
  * [MDEV-11444](https://jira.mariadb.org/browse/MDEV-11444) Server crashes in String::ptr / Item\_func\_json\_depth::val\_int.
* [Revision #4ad0813](https://github.com/MariaDB/server/commit/4ad0813)\
  2016-12-03 11:22:42 +0400
  * [MDEV-11143](https://jira.mariadb.org/browse/MDEV-11143) Server crashes in json\_string\_set\_cs.
* [Revision #e8c4195](https://github.com/MariaDB/server/commit/e8c4195)\
  2016-12-03 11:02:28 +0400
  * [MDEV-11442](https://jira.mariadb.org/browse/MDEV-11442) Server crashes in String::length / parse\_one\_or\_all /Item\_func\_json\_contains\_path::val\_int
* [Revision #b28626e](https://github.com/MariaDB/server/commit/b28626e)\
  2016-12-03 10:53:12 +0400
  * [MDEV-11441](https://jira.mariadb.org/browse/MDEV-11441) Server crashes in String::append /Item\_func\_json\_extract::val\_str.
* [Revision #1e2b46d](https://github.com/MariaDB/server/commit/1e2b46d)\
  2016-12-02 17:28:39 +0200
  * [MDEV-11168](https://jira.mariadb.org/browse/MDEV-11168): InnoDB: Failing assertion: !other\_lock || wsrep\_thd\_is\_BF(lock->trx->mysql\_thd, FALSE) || wsrep\_thd\_is\_BF(other\_lock->trx->mysql\_thd, FALSE)
* [Revision #33ed16c](https://github.com/MariaDB/server/commit/33ed16c)\
  2016-12-02 16:25:47 +0200
  * [MDEV-11236](https://jira.mariadb.org/browse/MDEV-11236) Failing assertion: state == TRX\_STATE\_NOT\_STARTED
* [Revision #cb78555](https://github.com/MariaDB/server/commit/cb78555)\
  2016-12-02 00:39:19 +0100
  * update test results
* Merge [Revision #6a10681](https://github.com/MariaDB/server/commit/6a10681) 2016-12-01 15:05:20 +0200 - Merge pull request #262 from grooverdan/10.2-[MDEV-9451](https://jira.mariadb.org/browse/MDEV-9451)-remove-innodb\_buffer\_pool\_populate
* [Revision #09b825b](https://github.com/MariaDB/server/commit/09b825b)\
  2016-12-01 09:17:00 +1100
  * [MDEV-9451](https://jira.mariadb.org/browse/MDEV-9451): Remove innodb\_buffer\_pool\_populate from xtradb
* [Revision #0b66d3f](https://github.com/MariaDB/server/commit/0b66d3f)\
  2016-12-01 12:56:23 +0200
  * [MDEV-11426](https://jira.mariadb.org/browse/MDEV-11426) Remove InnoDB INFORMATION\_SCHEMA.FILES implementation
* [Revision #943baa3](https://github.com/MariaDB/server/commit/943baa3)\
  2016-12-01 12:44:12 +0200
  * [MDEV-11168](https://jira.mariadb.org/browse/MDEV-11168): InnoDB: Failing assertion: !other\_lock || wsrep\_thd\_is\_BF(lock->trx->mysql\_thd, FALSE) || wsrep\_thd\_is\_BF(other\_lock->trx->mysql\_thd, FALSE)
* [Revision #2c9bb42](https://github.com/MariaDB/server/commit/2c9bb42)\
  2016-12-01 08:28:59 +0200
  * [MDEV-11432](https://jira.mariadb.org/browse/MDEV-11432) Change the informational redo log format tag to "[MariaDB 10.2.3](../../old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md)"
* [Revision #dc9f919](https://github.com/MariaDB/server/commit/dc9f919)\
  2016-12-01 06:42:59 +0200
  * [MDEV-11005](https://jira.mariadb.org/browse/MDEV-11005): Incorrect error message when using ONLINE alter table with GIS
* [Revision #3d0d290](https://github.com/MariaDB/server/commit/3d0d290)\
  2016-11-30 17:53:30 +0200
  * Remove tablespace code from InnoDB compilation as it is not used.
* [Revision #674e338](https://github.com/MariaDB/server/commit/674e338)\
  2016-11-29 20:54:18 -0800
  * Added the test case for bug [MDEV-10836](https://jira.mariadb.org/browse/MDEV-10836). The bug was fixed by the patch for [MDEV-10882](https://jira.mariadb.org/browse/MDEV-10882).
* [Revision #b2c63d2](https://github.com/MariaDB/server/commit/b2c63d2)\
  2016-11-29 15:54:20 -0800
  * Fixed bug [MDEV-10882](https://jira.mariadb.org/browse/MDEV-10882). The implementation of the virtual method build\_clone for the class Item\_cache was missing.
* [Revision #cc577f8](https://github.com/MariaDB/server/commit/cc577f8)\
  2016-11-29 16:25:22 +0400
  * [MDEV-11041](https://jira.mariadb.org/browse/MDEV-11041) Innodb\_gis/ tests taken from MySQL fail.
* [Revision #098dff1](https://github.com/MariaDB/server/commit/098dff1)\
  2016-11-26 17:23:24 +0100
  * [MDEV-11359](https://jira.mariadb.org/browse/MDEV-11359) Implement IGNORE for bulk operation
* [Revision #d9c03c4](https://github.com/MariaDB/server/commit/d9c03c4)\
  2016-11-27 20:40:35 +0100
  * Deb: Streamline package listing order to make comparisons downstream easier
* [Revision #ca3df8f](https://github.com/MariaDB/server/commit/ca3df8f)\
  2016-11-27 12:34:53 +0100
  * Deb: wrap-and-sort for easier comparison to downstream in future
* [Revision #f977709](https://github.com/MariaDB/server/commit/f977709)\
  2016-11-26 19:08:07 +0100
  * Deb: Make libmariadb3 to provide the libmysqlclient.so.XX links
* [Revision #1965f03](https://github.com/MariaDB/server/commit/1965f03)\
  2016-11-26 22:22:50 +0100
  * Deb: Rename libmariadbclient-dev to libmariadb-dev
* [Revision #2949282](https://github.com/MariaDB/server/commit/2949282)\
  2016-11-26 18:05:42 +0100
  * Deb: Fix libmariadbclient.so.18 link path to point to libmariadb.so.3
* [Revision #9bfde89](https://github.com/MariaDB/server/commit/9bfde89)\
  2016-11-27 18:21:18 +0400
  * [MDEV-11360](https://jira.mariadb.org/browse/MDEV-11360) Dynamic SQL: DEFAULT as a bind parameter
* [Revision #1d0f174](https://github.com/MariaDB/server/commit/1d0f174)\
  2016-11-26 21:22:49 -0800
  * Fixed bug [MDEV-11313](https://jira.mariadb.org/browse/MDEV-11313). The fix for bug 11072 was not complete though it also fixed the bug [MDEV-10800](https://jira.mariadb.org/browse/MDEV-10800). This patch resolves the problems of all three bugs.
* [Revision #b5b68b6](https://github.com/MariaDB/server/commit/b5b68b6)\
  2016-11-26 13:22:10 +0100
  * [MDEV-10126](https://jira.mariadb.org/browse/MDEV-10126): replace deprecated iproute dependency with iproute2
* [Revision #3a6e781](https://github.com/MariaDB/server/commit/3a6e781)\
  2016-11-26 00:46:12 +0100
  * [MDEV-9165](https://jira.mariadb.org/browse/MDEV-9165): Run chown much faster on the datadir during install/update
* Merge [Revision #618edd4](https://github.com/MariaDB/server/commit/618edd4) 2016-11-25 14:30:47 +0200 - Merge branch 'kevgs-10.2\_warnings' into 10.2
* Merge [Revision #cc3aba2](https://github.com/MariaDB/server/commit/cc3aba2) 2016-11-25 14:28:31 +0200 - Merge branch '10.2\_warnings' of [server](https://github.com/kevgs/server) into kevgs-10.2\_warnings
* [Revision #780db8e](https://github.com/MariaDB/server/commit/780db8e)\
  2016-11-24 17:36:02 +0300
  * fix build and some warnings
* [Revision #d247d64](https://github.com/MariaDB/server/commit/d247d64)\
  2016-11-25 06:28:02 +0200
  * [MDEV-11349](https://jira.mariadb.org/browse/MDEV-11349) (2/2) Fix some bogus-looking Valgrind warnings
* [Revision #cdaa1d7](https://github.com/MariaDB/server/commit/cdaa1d7)\
  2016-11-25 06:09:00 +0200
  * [MDEV-11349](https://jira.mariadb.org/browse/MDEV-11349) (1/2) Fix some clang 4.0 warnings
* [Revision #1a1749e](https://github.com/MariaDB/server/commit/1a1749e)\
  2016-11-24 18:18:00 +0400
  * [MDEV-11296](https://jira.mariadb.org/browse/MDEV-11296) - InnoDB stalls under OLTP RW on P8
* [Revision #fb7caad](https://github.com/MariaDB/server/commit/fb7caad)\
  2016-11-23 14:07:17 +0400
  * [MDEV-11296](https://jira.mariadb.org/browse/MDEV-11296) - InnoDB stalls under OLTP RW on P8
* [Revision #68a8537](https://github.com/MariaDB/server/commit/68a8537)\
  2016-11-23 11:34:50 +0400
  * [MDEV-11296](https://jira.mariadb.org/browse/MDEV-11296) - InnoDB stalls under OLTP RW on P8
* [Revision #8d010c4](https://github.com/MariaDB/server/commit/8d010c4)\
  2016-11-22 14:19:54 +0400
  * [MDEV-11296](https://jira.mariadb.org/browse/MDEV-11296) - InnoDB stalls under OLTP RW on P8
* [Revision #bb7e84b](https://github.com/MariaDB/server/commit/bb7e84b)\
  2016-11-22 14:04:43 +0400
  * [MDEV-11296](https://jira.mariadb.org/browse/MDEV-11296) - InnoDB stalls under OLTP RW on P8
* [Revision #e06e455](https://github.com/MariaDB/server/commit/e06e455)\
  2016-11-24 23:38:59 +0100
  * Deb: make server core package breaks/replaces earlier client packages
* [Revision #89236a8](https://github.com/MariaDB/server/commit/89236a8)\
  2016-11-25 00:10:15 +0100
  * Deb: skip invoke-rc.d mysql stop if no mysql process is running at all
* [Revision #e726ae6](https://github.com/MariaDB/server/commit/e726ae6)\
  2016-11-24 17:39:12 +0100
  * Made all capability bit constants to be ULL. All new MariaDB capabilities(in upper 32bits) were sent as 0 on 32bit Windows. They were reset because CLIENT\_SSL, CLIENT\_COMPRESS and CLIENT\_SSL\_VERIFY\_SERVER\_CERT were defined as UL Plus MARIADB\_CLIENT\_STMT\_BULK\_OPERATIONS was defined as 1UL << 34, and that is undefined operation.
* [Revision #f4d6f26](https://github.com/MariaDB/server/commit/f4d6f26)\
  2016-11-22 17:19:08 -0800
  * Fixed bug [MDEV-11315](https://jira.mariadb.org/browse/MDEV-11315). There were no implementations for the virtual functions exclusive\_dependence\_on\_table\_processor and exclusive\_dependence\_on\_table\_processor. As a result the procedure pushdown\_cond\_for\_derived erroneously detected some conditions with outer references as pushable into materialized view / derived table.
* [Revision #779d416](https://github.com/MariaDB/server/commit/779d416)\
  2016-11-16 20:39:08 +0100
  * [MDEV-10724](https://jira.mariadb.org/browse/MDEV-10724) Assertion \`vcol\_table == 0 || vcol\_table == table' failed in fill\_record(THD\*, TABLE\*, List&, List&, bool, bool)
* [Revision #4a27ab2](https://github.com/MariaDB/server/commit/4a27ab2)\
  2016-11-21 17:14:14 -0500
  * [MDEV-10792](https://jira.mariadb.org/browse/MDEV-10792): Assertion \`thd->mdl\_context.is\_lock\_owner ..
* [Revision #ebe0619](https://github.com/MariaDB/server/commit/ebe0619)\
  2016-11-21 16:20:10 -0500
  * [MDEV-10442](https://jira.mariadb.org/browse/MDEV-10442): "Address already in use" on restart
* [Revision #44ccb8f](https://github.com/MariaDB/server/commit/44ccb8f)\
  2016-11-08 08:35:57 -0500
  * [MDEV-10432](https://jira.mariadb.org/browse/MDEV-10432): Post-fix after merging PR#205
* [Revision #cf1b0c1](https://github.com/MariaDB/server/commit/cf1b0c1)\
  2016-07-24 22:13:02 +0200
  * Implement native/base process checks for FreeBSD
* [Revision #f16ead5](https://github.com/MariaDB/server/commit/f16ead5)\
  2016-07-24 22:01:14 +0200
  * POSIX-ify wsrep scripts
* [Revision #665045f](https://github.com/MariaDB/server/commit/665045f)\
  2016-11-21 10:33:06 -0800
  * Fixed bug [MDEV-11081](https://jira.mariadb.org/browse/MDEV-11081).
* [Revision #022aeda](https://github.com/MariaDB/server/commit/022aeda)\
  2016-09-10 20:42:20 +0200
  * Attempt to fix strange rpm dependency issue following prior patch
* [Revision #58532f3](https://github.com/MariaDB/server/commit/58532f3)\
  2016-11-21 02:32:48 +0300
  * Update the testcase for [MDEV-10330](https://jira.mariadb.org/browse/MDEV-10330)
* [Revision #f77bd5f](https://github.com/MariaDB/server/commit/f77bd5f)\
  2016-09-10 17:50:32 +0200
  * Fix use of `require` in mysql-test-run.
* [Revision #d49cffa](https://github.com/MariaDB/server/commit/d49cffa)\
  2016-11-12 23:01:37 +0200
  * Deb: provide the libmysqlclient shim packages that exist in Debian/Ubuntu
* [Revision #dcfe6cb](https://github.com/MariaDB/server/commit/dcfe6cb)\
  2016-11-13 01:10:41 +0200
  * Deb: make libmariadb3 to provide the libmariadbclient.so.18 link
* [Revision #2bcc16c](https://github.com/MariaDB/server/commit/2bcc16c)\
  2016-11-17 22:12:42 +0200
  * Deb: rename client library packages to reflect its contents
* [Revision #54bd67a](https://github.com/MariaDB/server/commit/54bd67a)\
  2016-11-12 22:20:19 +0200
  * Deb: provide the default-mysql-\* packages that exist in Debian/Ubuntu
* [Revision #df8ba7a](https://github.com/MariaDB/server/commit/df8ba7a)\
  2016-11-12 19:15:07 +0200
  * Deb: install GSSAPI and Cracklib config files
* [Revision #68535b5](https://github.com/MariaDB/server/commit/68535b5)\
  2016-11-12 22:38:39 +0200
  * Deb: correct comment about socket auth in Spider/Mroong maintainer scripts
* [Revision #039bab2](https://github.com/MariaDB/server/commit/039bab2)\
  2016-11-20 00:25:38 +0300
  * Undo the unfinished patch for [MDEV-8359](https://jira.mariadb.org/browse/MDEV-8359):
* Merge [Revision #e0fc6dc](https://github.com/MariaDB/server/commit/e0fc6dc) 2016-11-19 12:59:22 +0400 - Merge pull request #244 from hholzgra/hartmut-[MDEV-726](https://jira.mariadb.org/browse/MDEV-726)
* [Revision #86637b2](https://github.com/MariaDB/server/commit/86637b2)\
  2016-10-09 01:20:17 +0200
  * [MDEV-726](https://jira.mariadb.org/browse/MDEV-726) - added regression test case
* [Revision #3234faf](https://github.com/MariaDB/server/commit/3234faf)\
  2016-10-08 15:57:12 +0200
  * [MDEV-726](https://jira.mariadb.org/browse/MDEV-726) - CREATE and ALTER SERVER need to lowercase host name
* [Revision #4504986](https://github.com/MariaDB/server/commit/4504986)\
  2016-11-18 18:28:01 +0200
  * Deb: install libmysqld.so and libmysqld.so.19 in correct packages
* [Revision #a4dc956](https://github.com/MariaDB/server/commit/a4dc956)\
  2016-11-18 22:46:54 +0300
  * [MDEV-10330](https://jira.mariadb.org/browse/MDEV-10330): main.show\_explain\_ps fails sporadically in buildbot
* Merge [Revision #d66e111](https://github.com/MariaDB/server/commit/d66e111) 2016-11-18 22:33:25 +0300 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* [Revision #b162068](https://github.com/MariaDB/server/commit/b162068)\
  2016-11-18 18:27:01 +0100
  * Fixed embedded prepared statements.
* [Revision #84fd0bc](https://github.com/MariaDB/server/commit/84fd0bc)\
  2016-11-17 23:38:08 +0400
  * Update libmariadb
* [Revision #e1caf31](https://github.com/MariaDB/server/commit/e1caf31)\
  2016-11-17 17:36:06 +0400
  * Mark spider tests big
* [Revision #7072ca1f](https://github.com/MariaDB/server/commit/7072ca1f)\
  2016-11-04 10:20:34 +1100
  * [MDEV-5725](https://jira.mariadb.org/browse/MDEV-5725): mysqld embedded libraries into libmariadbd19 Deb package
* [Revision #2387c91](https://github.com/MariaDB/server/commit/2387c91)\
  2016-11-04 09:24:54 +1100
  * [MDEV-5725](https://jira.mariadb.org/browse/MDEV-5725): Don't install private mysql header files
* [Revision #691214a](https://github.com/MariaDB/server/commit/691214a)\
  2016-11-16 22:16:20 -0800
  * Fixed bug [MDEV-11103](https://jira.mariadb.org/browse/MDEV-11103). The class Item\_func\_nop\_all missed an implementation of the virtual method get\_copy. As a result if the condition that can be pushed into a materialized view / derived table contained an ANY subselect then the pushdown condition was built incorrectly.
* [Revision #ebe5a38](https://github.com/MariaDB/server/commit/ebe5a38)\
  2016-11-16 15:06:19 -0800
  * Correction for the patch for [MDEV-11102](https://jira.mariadb.org/browse/MDEV-11102).
* [Revision #1655160](https://github.com/MariaDB/server/commit/1655160)\
  2016-11-16 14:32:04 -0800
  * Fixed bug [MDEV-11102](https://jira.mariadb.org/browse/MDEV-11102). Do not push conditions from where into materialized inner tables of outer joins: this is not valid.
* Merge [Revision #dace5f9](https://github.com/MariaDB/server/commit/dace5f9) 2016-11-16 19:51:22 +0300 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* [Revision #ded4cd1](https://github.com/MariaDB/server/commit/ded4cd1)\
  2016-11-16 20:25:55 +0400
  * Added missing INNODB\_COMPRESSION\_DEFAULT
* [Revision #0838fd0](https://github.com/MariaDB/server/commit/0838fd0)\
  2016-11-16 12:07:12 +0200
  * [MDEV-11185](https://jira.mariadb.org/browse/MDEV-11185): innodb.innodb\_trx\_weight fails in buildbot
* [Revision #0d85124](https://github.com/MariaDB/server/commit/0d85124)\
  2016-11-16 12:47:46 +0400
  * func\_json.test failing on Windows fixed.
* [Revision #0b86981](https://github.com/MariaDB/server/commit/0b86981)\
  2016-11-15 09:24:39 -0800
  * Made the result output deterministic.
* [Revision #68e7d92](https://github.com/MariaDB/server/commit/68e7d92)\
  2016-11-14 23:23:36 -0800
  * Fixed bug [MDEV-11072](https://jira.mariadb.org/browse/MDEV-11072). In a general case the conditions with outer fields cannot be pushed into materialized views / derived tables. However if the outer field in the condition refers to a single row table then the condition may be pushable. In this case a special care should be taken for outer fields when pushing the condition into a materialized view / derived table.
* [Revision #ebe5ebb](https://github.com/MariaDB/server/commit/ebe5ebb)\
  2016-11-15 17:04:31 +0400
  * [MDEV-9143](https://jira.mariadb.org/browse/MDEV-9143) JSON\_xxx functions.
* [Revision #1122c1f](https://github.com/MariaDB/server/commit/1122c1f)\
  2016-11-15 14:56:29 +0400
  * InnoDB cleanups
* [Revision #8283d7f](https://github.com/MariaDB/server/commit/8283d7f)\
  2016-11-13 14:55:50 -0800
  * Added the test case from [MDEV-11259](https://jira.mariadb.org/browse/MDEV-11259).
* [Revision #92bcb90](https://github.com/MariaDB/server/commit/92bcb90)\
  2016-11-13 14:46:33 -0800
  * Fixed bug [MDEV-11278](https://jira.mariadb.org/browse/MDEV-11278). If a recursive CTE referred to a materialized view/derived table then the query that used this CTE returned a bogus error message.
* [Revision #f2219c8](https://github.com/MariaDB/server/commit/f2219c8)\
  2016-11-09 21:15:17 +0200
  * Deb: add gdb as a build dependency for stack traces on test suite failures
* [Revision #e820dec](https://github.com/MariaDB/server/commit/e820dec)\
  2016-11-08 22:18:19 +0200
  * Deb: List package contents as part of the build log
* [Revision #d50ca35](https://github.com/MariaDB/server/commit/d50ca35)\
  2016-11-08 22:15:33 +0200
  * Deb: clean up, strip legacy and simplify autobake-deb.sh
* [Revision #8c03823](https://github.com/MariaDB/server/commit/8c03823)\
  2016-11-10 09:42:49 +0200
  * [MDEV-11250](https://jira.mariadb.org/browse/MDEV-11250): mtflush threads stall on shutdown
* [Revision #ada3d75](https://github.com/MariaDB/server/commit/ada3d75)\
  2016-11-09 15:17:55 +0200
  * [MDEV-10692](https://jira.mariadb.org/browse/MDEV-10692): InnoDB: Failing assertion: lock->trx->lock.wait\_lock == lock
* [Revision #8e5f532](https://github.com/MariaDB/server/commit/8e5f532)\
  2016-11-09 13:32:43 +0200
  * [MDEV-10692](https://jira.mariadb.org/browse/MDEV-10692): InnoDB: Failing assertion: lock->trx->lock.wait\_lock == lock
* [Revision #0259b3c](https://github.com/MariaDB/server/commit/0259b3c)\
  2016-11-08 20:57:19 +0400
  * [MDEV-11255](https://jira.mariadb.org/browse/MDEV-11255) LDML: allow defining 2-level UCA collations
* [Revision #90c5b2f](https://github.com/MariaDB/server/commit/90c5b2f)\
  2016-10-08 14:20:06 +0200
  * [MDEV-10982](https://jira.mariadb.org/browse/MDEV-10982) - Show real version number in 'ready for connections' message
* [Revision #f8b4015](https://github.com/MariaDB/server/commit/f8b4015)\
  2016-09-29 11:50:13 +0200
  * init plugin psi keys before LOCK\_plugin
* [Revision #491f42d](https://github.com/MariaDB/server/commit/491f42d)\
  2016-11-01 17:37:20 -0400
  * Fix/disable some failing galera tests.
* [Revision #9b6bd3f](https://github.com/MariaDB/server/commit/9b6bd3f)\
  2016-10-26 12:06:54 -0400
  * [MDEV-11149](https://jira.mariadb.org/browse/MDEV-11149): wsrep\_replicate\_mysaim: DML fails when binlog checksum enabled
* [Revision #db95beb](https://github.com/MariaDB/server/commit/db95beb)\
  2016-10-03 11:30:12 +0100
  * [MDEV-9903](https://jira.mariadb.org/browse/MDEV-9903) - 10.2 : Check and run rsync daemon only in the needed IP See [235](https://github.com/MariaDB/server/pull/235) I submit this code under the BSD-new license.
* [Revision #d5e6d83](https://github.com/MariaDB/server/commit/d5e6d83)\
  2016-10-03 17:03:02 -0400
  * Update test results in galera, galera\_3nodes suites.
* [Revision #9ddbf2c](https://github.com/MariaDB/server/commit/9ddbf2c)\
  2016-10-03 12:02:46 -0400
  * [MDEV-10944](https://jira.mariadb.org/browse/MDEV-10944): GALERA log-slave-updates FAIL after upgrading from 10.1.17 to 10.1.18
* [Revision #9d89c18](https://github.com/MariaDB/server/commit/9d89c18)\
  2016-09-29 14:58:32 -0400
  * [MDEV-9312](https://jira.mariadb.org/browse/MDEV-9312): storage engine not enforced during galera cluster replication
* [Revision #7241258](https://github.com/MariaDB/server/commit/7241258)\
  2016-09-28 13:27:34 -0400
  * [MDEV-9416](https://jira.mariadb.org/browse/MDEV-9416): MariaDB galera got signal 11 when altering table add unique index
* [Revision #6bb6f30](https://github.com/MariaDB/server/commit/6bb6f30)\
  2016-09-28 13:26:13 -0400
  * [MDEV-9312](https://jira.mariadb.org/browse/MDEV-9312): storage engine not enforced during galera cluster replication
* [Revision #7c38a94](https://github.com/MariaDB/server/commit/7c38a94)\
  2016-09-28 13:23:31 -0400
  * [MDEV-10041](https://jira.mariadb.org/browse/MDEV-10041): Server crashes sporadically during bootstrap while running wsrep tests
* [Revision #458648e](https://github.com/MariaDB/server/commit/458648e)\
  2016-11-07 13:27:33 +0400
  * Fixed test suite name
* Merge [Revision #ea24480](https://github.com/MariaDB/server/commit/ea24480) 2016-11-07 10:25:49 +0200 - Merge pull request #255 from rasmushoj/[MDEV-9820](https://jira.mariadb.org/browse/MDEV-9820)
* [Revision #bba224d](https://github.com/MariaDB/server/commit/bba224d)\
  2016-10-27 23:24:44 +0300
  * Added server variable compression\_default, which if 1/ON sets compression on for all new InnoDB/XtraDB tables by default by setting PAGE\_COMPRESSED=1
* [Revision #f5719fc](https://github.com/MariaDB/server/commit/f5719fc)\
  2016-11-07 03:20:04 +0300
  * Temporarily disable innodb.innodb\_trx\_weight test due to [MDEV-11185](https://jira.mariadb.org/browse/MDEV-11185)
* [Revision #72c9de1](https://github.com/MariaDB/server/commit/72c9de1)\
  2016-11-07 01:52:07 +0300
  * [MDEV-10986](https://jira.mariadb.org/browse/MDEV-10986) sphinx.union-5539 and sphinx.sphinx fail in buildbot and outside
* Merge [Revision #2d25d09](https://github.com/MariaDB/server/commit/2d25d09) 2016-11-04 17:19:02 +0100 - Merge pull request #253 from grooverdan/10.2-[MDEV-11195](https://jira.mariadb.org/browse/MDEV-11195)-numa-build
* [Revision #58ac8dd](https://github.com/MariaDB/server/commit/58ac8dd)\
  2016-11-02 14:37:43 +1100
  * [MDEV-11195](https://jira.mariadb.org/browse/MDEV-11195): Simplify enablement of NUMA in innodb/xtradb
* [Revision #ab0e503](https://github.com/MariaDB/server/commit/ab0e503)\
  2016-11-01 11:01:48 +1100
  * [MDEV-11195](https://jira.mariadb.org/browse/MDEV-11195): Correct enablement of NUMA in innodb/xtradb
* [Revision #7afcc7d](https://github.com/MariaDB/server/commit/7afcc7d)\
  2016-11-03 17:32:17 +0100
  * Re-generate .rdiff file in attempt to fix a test failure.
* [Revision #99d07aa](https://github.com/MariaDB/server/commit/99d07aa)\
  2016-11-03 16:56:18 +0100
  * Fixed print format.
* [Revision #9151121](https://github.com/MariaDB/server/commit/9151121)\
  2016-11-03 19:01:09 +0400
  * Scalability bottleneck in ha\_innodb::general\_fetch
* Merge [Revision #b002509](https://github.com/MariaDB/server/commit/b002509) 2016-11-03 14:48:51 +0100 - [MDEV-11065](https://jira.mariadb.org/browse/MDEV-11065): Compressed binary log. Merge code into current 10.2.
* [Revision #56a041c](https://github.com/MariaDB/server/commit/56a041c)\
  2016-11-03 13:37:15 +0100
  * [MDEV-11065](https://jira.mariadb.org/browse/MDEV-11065): Compressed binary log. Fix BINLOG statement.
* [Revision #3c0ff61](https://github.com/MariaDB/server/commit/3c0ff61)\
  2016-11-03 12:03:52 +0100
  * [MDEV-11065](https://jira.mariadb.org/browse/MDEV-11065): Compressed binary log
* [Revision #0e380c3](https://github.com/MariaDB/server/commit/0e380c3)\
  2016-10-29 21:59:20 +0800
  * two fix: 1.Avoid overflowing buffers in case of corrupt events 2.Check the compressed algorithm.
* [Revision #c06bc66](https://github.com/MariaDB/server/commit/c06bc66)\
  2016-10-20 18:00:59 +0200
  * [MDEV-11065](https://jira.mariadb.org/browse/MDEV-11065): Compressed binary log
* [Revision #e1c5028](https://github.com/MariaDB/server/commit/e1c5028)\
  2016-10-14 18:55:37 +0800
  * test suite for compressed binlog event
* [Revision #d4b2c9b](https://github.com/MariaDB/server/commit/d4b2c9b)\
  2016-10-14 15:23:49 +0800
  * optimize the memory allocation for compressed binlog event
* [Revision #640051e](https://github.com/MariaDB/server/commit/640051e)\
  2016-10-08 12:07:26 +0800
  * Binlog compressed
* [Revision #d665e79](https://github.com/MariaDB/server/commit/d665e79)\
  2016-05-06 13:44:07 +0400
  * [MDEV-7660](https://jira.mariadb.org/browse/MDEV-7660) - [MySQL Worklog #6671](https://dev.mysql.com/worklog/task/?id=6671) "Improve scalability by not using thr\_lock.c locks for InnoDB tables"
* [Revision #e2d6912](https://github.com/MariaDB/server/commit/e2d6912)\
  2016-06-29 20:03:06 +0200
  * [MDEV-9114](https://jira.mariadb.org/browse/MDEV-9114): Bulk operations (Array binding)
* [Revision #c6713f6](https://github.com/MariaDB/server/commit/c6713f6)\
  2016-07-20 10:00:26 +0530
  * Bug#23631471 BUF\_BLOCK\_ALIGN() MAKES INCORRECT ASSUMPTIONS ABOUT CHUNK SIZE
* [Revision #ce10116](https://github.com/MariaDB/server/commit/ce10116)\
  2016-11-02 12:19:37 +0400
  * [MDEV-11175](https://jira.mariadb.org/browse/MDEV-11175) - \H option does not replace localhost with a host name
* Merge [Revision #23cb94f](https://github.com/MariaDB/server/commit/23cb94f) 2016-11-01 13:39:09 +0200 - Merge pull request #251 from ottok/ok-debpkg-10.2
* [Revision #c912d05](https://github.com/MariaDB/server/commit/c912d05)\
  2016-10-29 02:43:45 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Install systemd files (almost) the Debian way
* [Revision #7316b14](https://github.com/MariaDB/server/commit/7316b14)\
  2016-10-29 02:55:19 +0300
  * Deb: use deb-sys-maint user credentials to configure MariaDB plugins
* [Revision #02a6f61](https://github.com/MariaDB/server/commit/02a6f61)\
  2016-10-29 02:17:14 +0300
  * Deb: delete runnable files we don't want to have in the test data package
* [Revision #bfda961](https://github.com/MariaDB/server/commit/bfda961)\
  2016-10-29 01:30:50 +0300
  * Deb: omit source building step when running from autobake-deb.sh
* [Revision #0668e6b](https://github.com/MariaDB/server/commit/0668e6b)\
  2016-10-26 02:12:18 +0300
  * Travis-CI: skip building mariadb-test packages to speed up build
* [Revision #7f570be](https://github.com/MariaDB/server/commit/7f570be)\
  2016-10-21 13:52:36 +0300
  * Deb: fix commit 1369696 and change autobake strategy to Debian Sid first
* [Revision #affa6e3](https://github.com/MariaDB/server/commit/affa6e3)\
  2016-10-11 18:45:59 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Break/replace MySQL 5.7 packages to allow upgrade
* [Revision #8c32d95](https://github.com/MariaDB/server/commit/8c32d95)\
  2016-10-11 17:26:22 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Activate quilt patches again: test table expection needed
* [Revision #4b7004d](https://github.com/MariaDB/server/commit/4b7004d)\
  2016-10-10 13:50:38 +0300
  * Travis-CI: build less verbose, log must stay under 4MB limit
* [Revision #19cffe6](https://github.com/MariaDB/server/commit/19cffe6)\
  2016-10-10 11:28:26 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Revert commit af03ba84 partially for systemd
* [Revision #f63799d](https://github.com/MariaDB/server/commit/f63799d)\
  2016-10-10 05:59:28 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Clean up crufs (dirs files, duplicate entries etc)
* [Revision #235db2c](https://github.com/MariaDB/server/commit/235db2c)\
  2016-10-09 18:00:57 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): wrap-and-sort
* [Revision #b2dffcb](https://github.com/MariaDB/server/commit/b2dffcb)\
  2016-10-09 15:51:01 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Fix issues detected by Lintian
* [Revision #1877a8c](https://github.com/MariaDB/server/commit/1877a8c)\
  2016-10-09 16:48:17 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Remove CMakeLists.txt hack that mangled the server install file
* [Revision #d495bf4](https://github.com/MariaDB/server/commit/d495bf4)\
  2016-10-09 14:43:34 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Spliy Mroonga, Spider and TokuDB into their own packages
* [Revision #e58e7b5](https://github.com/MariaDB/server/commit/e58e7b5)\
  2016-10-09 14:42:17 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Rename plugin packages to match new Debian convention
* [Revision #0a1dbe8](https://github.com/MariaDB/server/commit/0a1dbe8)\
  2016-07-10 23:36:05 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Split mariadb-test-data out of mariadb-test
* [Revision #1494a96](https://github.com/MariaDB/server/commit/1494a96)\
  2016-10-07 17:03:08 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Make mariadb-test package versionless
* [Revision #73f1c65](https://github.com/MariaDB/server/commit/73f1c65)\
  2016-10-09 23:39:01 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Import most of downstream Debian packaging
* [Revision #a59655a](https://github.com/MariaDB/server/commit/a59655a)\
  2016-07-09 22:03:02 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Remove Debian policy breaking and empty RELEASE\_\* variables
* [Revision #148422e](https://github.com/MariaDB/server/commit/148422e)\
  2016-07-09 18:51:08 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Bump compat level and define native Debian format
* [Revision #be78eec](https://github.com/MariaDB/server/commit/be78eec)\
  2016-07-09 18:48:56 +0300
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284): Rename .files -> .install
* [Revision #71e11bc](https://github.com/MariaDB/server/commit/71e11bc)\
  2016-10-28 12:29:37 +0400
  * [MDEV-8791](https://jira.mariadb.org/browse/MDEV-8791) - AIX: Unresolved Symbols during linking
* [Revision #40ad946](https://github.com/MariaDB/server/commit/40ad946)\
  2016-10-31 07:35:02 +0100
  * [MDEV-11187](https://jira.mariadb.org/browse/MDEV-11187): Server does not compile on labrador
* Merge [Revision #951ca5d](https://github.com/MariaDB/server/commit/951ca5d) 2016-10-27 17:05:00 +0300 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* [Revision #39d2c7b](https://github.com/MariaDB/server/commit/39d2c7b)\
  2016-10-27 06:37:21 +0400
  * Removing LEX::interval\_list, as it's not used since parser cleanups made in 227510e039b4ec6bff3096a4b9b39847551dab1a. We now use lex->last\_field->interval\_list directly instead.
* [Revision #0c15d1a](https://github.com/MariaDB/server/commit/0c15d1a)\
  2016-10-25 12:21:07 +0300
  * Set new scheduling algorithm VATS for lock waits as a default.
* [Revision #201c1e0](https://github.com/MariaDB/server/commit/201c1e0)\
  2016-10-25 10:09:33 +0400
  * [MDEV-9143](https://jira.mariadb.org/browse/MDEV-9143) JSON\_xxx functions.
* Merge [Revision #b09b316](https://github.com/MariaDB/server/commit/b09b316) 2016-10-24 15:17:24 +0300 - Merge pull request #248 from sensssz/10.2-vats
* [Revision #f6da2b4](https://github.com/MariaDB/server/commit/f6da2b4)\
  2016-10-23 13:42:50 -0400
  * Undo changes to XtraDB.
* [Revision #0064d85](https://github.com/MariaDB/server/commit/0064d85)\
  2016-10-23 13:41:36 -0400
  * Remove duplicated comments.
* [Revision #a24e625](https://github.com/MariaDB/server/commit/a24e625)\
  2016-10-23 13:36:26 -0400
  * Change all space indentions to tab.
* [Revision #fd30d07](https://github.com/MariaDB/server/commit/fd30d07)\
  2016-10-23 13:17:30 -0400
  * Style fixes.
* [Revision #149581a](https://github.com/MariaDB/server/commit/149581a)\
  2016-10-22 15:01:37 -0400
  * Remove unnecessary changes. Apply changes to XtraDB.
* [Revision #04f241a](https://github.com/MariaDB/server/commit/04f241a)\
  2016-10-22 10:22:03 -0400
  * Add a NULL check for thd\_is\_replication\_slave\_thread
* [Revision #adaebd2](https://github.com/MariaDB/server/commit/adaebd2)\
  2016-10-22 10:19:41 -0400
  * A few bug fixes. Use thd\_is\_slave\_replication.
* [Revision #36841ac](https://github.com/MariaDB/server/commit/36841ac)\
  2016-10-19 10:10:22 -0400
  * Add INNODB\_LOCK\_SCHEDULE\_ALGORITHM to sysvars\_innodb.result
* [Revision #f62fd5ad](https://github.com/MariaDB/server/commit/f62fd5ad)\
  2016-10-19 01:46:57 -0400
  * Bug fix: remove redundant code from check\_deadlock\_result. Remove assert.
* Merge [Revision #0f93b53](https://github.com/MariaDB/server/commit/0f93b53) 2016-10-19 01:42:34 -0400 - Merge branch '10.2-vats' of [server](https://github.com/sensssz/server) into 10.2-vats
* [Revision #5661b5c](https://github.com/MariaDB/server/commit/5661b5c)\
  2016-10-19 01:37:52 -0400
  * Change VATS implementation.
* Merge [Revision #5c40954](https://github.com/MariaDB/server/commit/5c40954) 2016-10-18 10:29:02 -0400 - Merge branch '10.2-vats' of [server](https://github.com/sensssz/server) into 10.2-vats
* [Revision #88519c9](https://github.com/MariaDB/server/commit/88519c9)\
  2016-10-18 09:52:39 -0400
  * Disable VATS on slave servers during replication.
* [Revision #87abc87](https://github.com/MariaDB/server/commit/87abc87)\
  2016-10-17 21:56:05 -0400
  * Implement VATS in XtraDB and InnoDB.
* [Revision #a9bdea5](https://github.com/MariaDB/server/commit/a9bdea5)\
  2016-10-18 09:52:39 -0400
  * Disable VATS on slave servers during replication.
* [Revision #0b7c35c](https://github.com/MariaDB/server/commit/0b7c35c)\
  2016-10-17 21:56:05 -0400
  * Implement VATS in XtraDB and InnoDB.
* [Revision #0e60f89](https://github.com/MariaDB/server/commit/0e60f89)\
  2016-10-19 01:37:52 -0400
  * Change VATS implementation.
* [Revision #03b3425](https://github.com/MariaDB/server/commit/03b3425)\
  2016-10-18 09:52:39 -0400
  * Disable VATS on slave servers during replication.
* [Revision #c455898](https://github.com/MariaDB/server/commit/c455898)\
  2016-10-17 21:56:05 -0400
  * Implement VATS in XtraDB and InnoDB.
* Merge [Revision #a1f0a33](https://github.com/MariaDB/server/commit/a1f0a33) 2016-10-24 09:08:19 +0300 - Merge branch 'grooverdan-10.2-numa' into 10.2
* Merge [Revision #f35f61b](https://github.com/MariaDB/server/commit/f35f61b) 2016-10-24 09:07:49 +0300 - Merge branch '10.2-numa' of [mariadb-server](https://github.com/grooverdan/mariadb-server) into grooverdan-10.2-numa
* Merge [Revision #f05dfbe](https://github.com/MariaDB/server/commit/f05dfbe) 2016-09-23 09:24:22 +1000 - Merge 10.2
* [Revision #633e995](https://github.com/MariaDB/server/commit/633e995)\
  2016-09-23 09:09:46 +1000
  * [MDEV-10829](https://jira.mariadb.org/browse/MDEV-10829): libnuma-dev for travis
* [Revision #8e8e65e](https://github.com/MariaDB/server/commit/8e8e65e)\
  2016-09-19 12:07:20 +1000
  * [MDEV-10829](https://jira.mariadb.org/browse/MDEV-10829): innodb\_numa\_interleave=1, use numa numa\_get\_mems\_allowed
* [Revision #8b59eab](https://github.com/MariaDB/server/commit/8b59eab)\
  2016-09-23 08:58:57 +1000
  * [MDEV-10829](https://jira.mariadb.org/browse/MDEV-10829): add libnuma-dev to debian packaging
* [Revision #8103f6f](https://github.com/MariaDB/server/commit/8103f6f)\
  2016-09-20 10:05:10 +1000
  * [MDEV-10829](https://jira.mariadb.org/browse/MDEV-10829): Enable Innodb NUMA interleave
* [Revision #26e3117](https://github.com/MariaDB/server/commit/26e3117)\
  2016-09-20 09:51:22 +1000
  * [MDEV-10829](https://jira.mariadb.org/browse/MDEV-10829): Port Innodb NUMA interleave test cases from MySQL
* [Revision #1de147f](https://github.com/MariaDB/server/commit/1de147f)\
  2016-10-24 02:12:12 +0300
  * [MDEV-11120](https://jira.mariadb.org/browse/MDEV-11120) sys\_vars.sysvars\_server\_notembedded fails on 32-bit
* [Revision #6f7fca7](https://github.com/MariaDB/server/commit/6f7fca7)\
  2016-10-24 02:11:39 +0300
  * [MDEV-11019](https://jira.mariadb.org/browse/MDEV-11019) sys\_vars.sysvars\_server\_embedded fails in buildbot
* Merge [Revision #82b974a](https://github.com/MariaDB/server/commit/82b974a) 2016-10-21 17:37:30 +0200 - Merge [MDEV-11064](https://jira.mariadb.org/browse/MDEV-11064): "Restrict the speed of reading binlog from Master" into 10.2
* [Revision #9970e81](https://github.com/MariaDB/server/commit/9970e81)\
  2016-10-21 16:31:45 +0800
  * fix the ABI check
* [Revision #07f09df](https://github.com/MariaDB/server/commit/07f09df)\
  2016-10-21 16:02:51 +0800
  * fix the ABI and stop slave hang problem
* [Revision #0fa39ff](https://github.com/MariaDB/server/commit/0fa39ff)\
  2016-10-17 18:27:49 +0800
  * fix code style..
* [Revision #c334f4f](https://github.com/MariaDB/server/commit/c334f4f)\
  2016-10-17 18:04:15 +0800
  * fix the code style for read\_binlog\_speed\_limit
* [Revision #ef77847](https://github.com/MariaDB/server/commit/ef77847)\
  2016-10-11 15:21:20 +0800
  * fix common test suite
* [Revision #4378990](https://github.com/MariaDB/server/commit/4378990)\
  2016-09-19 17:23:23 +0800
  * Control the binlog read speed for compressed protocol
* [Revision #8eb0f5c](https://github.com/MariaDB/server/commit/8eb0f5c)\
  2016-09-19 11:40:31 +0800
  * Control the Maximum speed(KB/s) to read binlog from master
* [Revision #2702522](https://github.com/MariaDB/server/commit/2702522)\
  2016-10-19 14:10:03 +0400
  * [MDEV-9143](https://jira.mariadb.org/browse/MDEV-9143) JSON\_xxx functions.
* [Revision #8303ade](https://github.com/MariaDB/server/commit/8303ade)\
  2016-09-15 13:39:41 +0400
  * [MDEV-7148](https://jira.mariadb.org/browse/MDEV-7148) - Recurring: InnoDB: Failing assertion: !lock->recursive
* [Revision #2b47f8f](https://github.com/MariaDB/server/commit/2b47f8f)\
  2016-09-14 15:12:54 +0400
  * [MDEV-10813](https://jira.mariadb.org/browse/MDEV-10813) - Clean-up InnoDB atomics, memory barriers and mutexes
* [Revision #5608a73](https://github.com/MariaDB/server/commit/5608a73)\
  2016-09-14 15:56:06 +0400
  * [MDEV-10813](https://jira.mariadb.org/browse/MDEV-10813) - Clean-up InnoDB atomics, memory barriers and mutexes
* [Revision #f4d885c](https://github.com/MariaDB/server/commit/f4d885c)\
  2016-09-09 15:05:59 +0400
  * [MDEV-10813](https://jira.mariadb.org/browse/MDEV-10813) - Clean-up InnoDB atomics, memory barriers and mutexes
* [Revision #d055e28](https://github.com/MariaDB/server/commit/d055e28)\
  2016-09-13 23:35:20 +0400
  * [MDEV-10813](https://jira.mariadb.org/browse/MDEV-10813) - Clean-up InnoDB atomics, memory barriers and mutexes
* [Revision #cc49f00](https://github.com/MariaDB/server/commit/cc49f00)\
  2016-10-17 12:52:14 +0200
  * Move InnoDB/XtraDB to async deadlock kill for parallel replication.
* [Revision #4d3e366](https://github.com/MariaDB/server/commit/4d3e366)\
  2016-10-17 00:59:02 +0300
  * [MDEV-11061](https://jira.mariadb.org/browse/MDEV-11061) Valgrind builder produces warnings with OpenSSL
* Merge [Revision #e1ef99c](https://github.com/MariaDB/server/commit/e1ef99c) 2016-10-16 23:44:44 +0200 - [MDEV-7145](https://jira.mariadb.org/browse/MDEV-7145): Delayed replication
* [Revision #fb13616](https://github.com/MariaDB/server/commit/fb13616)\
  2016-10-14 21:29:35 +0200
  * [MDEV-7145](https://jira.mariadb.org/browse/MDEV-7145): Delayed replication.
* [Revision #3011060](https://github.com/MariaDB/server/commit/3011060)\
  2016-10-14 12:22:00 +0200
  * [MDEV-7145](https://jira.mariadb.org/browse/MDEV-7145): Delayed slave.
* [Revision #09136ec](https://github.com/MariaDB/server/commit/09136ec)\
  2016-10-14 11:33:45 +0200
  * [MDEV-7145](https://jira.mariadb.org/browse/MDEV-7145), Delayed slave.
* [Revision #8148807](https://github.com/MariaDB/server/commit/8148807)\
  2016-10-14 11:18:33 +0200
  * BUG#56442: Slave executes delayed statements when STOP SLAVE is issued
* [Revision #851c401](https://github.com/MariaDB/server/commit/851c401)\
  2016-09-23 11:31:57 +0200
  * [MDEV-7145](https://jira.mariadb.org/browse/MDEV-7145): Delayed replication, fix wsrep build failure.
* [Revision #b2bc6da](https://github.com/MariaDB/server/commit/b2bc6da)\
  2016-09-22 13:36:45 +0200
  * [MDEV-7145](https://jira.mariadb.org/browse/MDEV-7145): Delayed replication, cleanup some code
* [Revision #a9fb480](https://github.com/MariaDB/server/commit/a9fb480)\
  2016-09-22 12:23:32 +0200
  * [MDEV-7145](https://jira.mariadb.org/browse/MDEV-7145): Delayed replication, fixing test failures.
* [Revision #19abe79](https://github.com/MariaDB/server/commit/19abe79)\
  2016-09-22 08:26:45 +0200
  * [MDEV-7145](https://jira.mariadb.org/browse/MDEV-7145): Delayed replication, intermediate commit.
* [Revision #50f19ca](https://github.com/MariaDB/server/commit/50f19ca)\
  2016-09-20 15:30:57 +0200
  * Remove unnecessary global mutex in parallel replication.
* [Revision #057c560](https://github.com/MariaDB/server/commit/057c560)\
  2016-10-15 02:27:28 +0200
  * [MDEV-10943](https://jira.mariadb.org/browse/MDEV-10943) . Workaround linker error on Linux. Linux does not actually use bss\_start, put bss\_start into #ifndef linux section
* [Revision #b8b1b92](https://github.com/MariaDB/server/commit/b8b1b92)\
  2016-10-14 00:05:13 +0300
  * [MDEV-8359](https://jira.mariadb.org/browse/MDEV-8359): WHERE condition referring to inner table of left join can be sargable
* [Revision #9208b87](https://github.com/MariaDB/server/commit/9208b87)\
  2016-10-13 16:54:59 +0300
  * Follow-up for big error-message cleanup (trailing dots were removed)
* [Revision #5058ced](https://github.com/MariaDB/server/commit/5058ced)\
  2016-10-10 14:36:09 +0400
  * [MDEV-7769](https://jira.mariadb.org/browse/MDEV-7769) MY\_CHARSET\_INFO refactoring

## On branch 10.2

* [Revision #a6f032a](https://github.com/MariaDB/server/commit/a6f032a)\
  2016-10-09 13:46:09 +0300
  * Deb: use --mem to run mtr faster and keep Travis-CI well below 50 min
* [Revision #c416ed8](https://github.com/MariaDB/server/commit/c416ed8)\
  2016-10-09 13:42:36 +0300
  * Deb: build faster using ccache when available
* [Revision #0331df1](https://github.com/MariaDB/server/commit/0331df1)\
  2016-10-08 03:28:41 +0300
  * Travis-CI: clean away cruf in definition file and use correct syntax
* [Revision #553ca40](https://github.com/MariaDB/server/commit/553ca40)\
  2016-10-08 15:20:16 +0400
  * A post-fix for [MDEV-10866](https://jira.mariadb.org/browse/MDEV-10866) Extend PREPARE and EXECUTE IMMEDIATE to understand expressions
* [Revision #46dc7bd](https://github.com/MariaDB/server/commit/46dc7bd)\
  2016-10-08 13:06:15 +0400
  * [MDEV-10866](https://jira.mariadb.org/browse/MDEV-10866) Extend PREPARE and EXECUTE IMMEDIATE to understand expressions [MDEV-10867](https://jira.mariadb.org/browse/MDEV-10867) PREPARE..EXECUTE is not consistent about non-ASCII characters
* [Revision #e1a212e](https://github.com/MariaDB/server/commit/e1a212e)\
  2016-10-08 12:32:52 +0400
  * [MDEV-10585](https://jira.mariadb.org/browse/MDEV-10585) EXECUTE IMMEDIATE statement
* [Revision #4c45b82](https://github.com/MariaDB/server/commit/4c45b82)\
  2016-10-08 11:50:18 +0400
  * [MDEV-10709](https://jira.mariadb.org/browse/MDEV-10709) Expressions as parameters to Dynamic SQL
* [Revision #8ea2e14](https://github.com/MariaDB/server/commit/8ea2e14)\
  2016-10-08 09:57:35 +0400
  * [MDEV-10772](https://jira.mariadb.org/browse/MDEV-10772) Introduce Item\_param::CONVERSION\_INFO
* [Revision #62d1cfe](https://github.com/MariaDB/server/commit/62d1cfe)\
  2016-10-07 01:25:05 +0300
  * Deb: always build mariadb-cracklib-password-check, even on Travis-CI
* [Revision #1369696](https://github.com/MariaDB/server/commit/1369696)\
  2016-10-06 19:30:20 +0300
  * Deb: Re-factor conditional build dependency checking and injecting
* [Revision #44dd9a5](https://github.com/MariaDB/server/commit/44dd9a5)\
  2016-07-12 10:27:37 +0300
  * Deb: wrap-and-sort
* [Revision #0a97008](https://github.com/MariaDB/server/commit/0a97008)\
  2016-07-12 10:21:26 +0300
  * Deb: Fix various shortcomings in the control file
* [Revision #e2bf4d8](https://github.com/MariaDB/server/commit/e2bf4d8)\
  2016-07-10 20:31:53 +0300
  * Deb: Remove commented out patches that for sure are not used anymore
* [Revision #5549d62](https://github.com/MariaDB/server/commit/5549d62)\
  2016-07-11 20:21:44 +0300
  * Deb: Make alternative Debian builds easy with git-buildpackage config file
* [Revision #00fc86f](https://github.com/MariaDB/server/commit/00fc86f)\
  2016-10-06 12:31:23 +0200
  * Remove test for using bash characters in tls/ssl file and directory names. bash char substitution is not supported for other file options (e.g. read default file)
* [Revision #14b1c8c](https://github.com/MariaDB/server/commit/14b1c8c)\
  2016-10-05 01:09:52 +0300
  * After merge and bug fixes - Fixed compiler warnings - Removed have\_debug.inc from innochecksum\_3 - Fixed race condition in innodb\_buffer\_pool\_load - Fixed merge issue in innodb-bad-key-change.test - Fixed missing array allocation that could cause function\_defaults\_notembedded to fail - Fixed thread\_cache\_size\_func
* [Revision #af7490f](https://github.com/MariaDB/server/commit/af7490f)\
  2016-10-03 18:49:44 +0300
  * Remove end . from error messages to get them consistent Fixed a few failing tests
* [Revision #c1125c3](https://github.com/MariaDB/server/commit/c1125c3)\
  2016-10-02 18:42:39 +0300
  * Fixed compiler warnings and failing tests
* [Revision #7b96416](https://github.com/MariaDB/server/commit/7b96416)\
  2016-10-02 16:39:40 +0300
  * Use sql\_mode\_t for sql\_mode. This fixed several cases where we where using just ulong for sql\_mode
* [Revision #8be53a3](https://github.com/MariaDB/server/commit/8be53a3)\
  2016-10-02 15:35:08 +0300
  * [MDEV-6112](https://jira.mariadb.org/browse/MDEV-6112) multiple triggers per table
* [Revision #0bae195](https://github.com/MariaDB/server/commit/0bae195)\
  2016-10-04 16:25:12 +0200
  * simplify the ipv6 check
* [Revision #70dcb46](https://github.com/MariaDB/server/commit/70dcb46)\
  2016-08-25 10:21:06 +1000
  * [MDEV-9185](https://jira.mariadb.org/browse/MDEV-9185): fix ipv6 detection test in MTR
* [Revision #4f919be](https://github.com/MariaDB/server/commit/4f919be)\
  2016-10-03 19:54:23 +0300
  * Enable Geometry datatype for SPATIAL indexes and disable online index creation for SPATIAL indexes.
* [Revision #9e70d88](https://github.com/MariaDB/server/commit/9e70d88)\
  2016-10-03 19:29:46 +0300
  * Disable wl6560.
* [Revision #cb2c2f1](https://github.com/MariaDB/server/commit/cb2c2f1)\
  2016-10-03 19:19:00 +0300
  * Replace non-repeatable page-type-dump directory.
* [Revision #a0a4079](https://github.com/MariaDB/server/commit/a0a4079)\
  2016-10-03 10:05:15 +0300
  * Run only on debug to avoid test differences.
* [Revision #2e7baca](https://github.com/MariaDB/server/commit/2e7baca)\
  2016-10-03 08:22:52 +0300
  * Replace tablespace numbers to make repeatable.
* [Revision #3b314ec](https://github.com/MariaDB/server/commit/3b314ec)\
  2016-09-30 17:39:55 -0700
  * Fixed bug [MDEV-10933](https://jira.mariadb.org/browse/MDEV-10933). The bug was caused by a misplaced construct opt\_with\_clause for one of the variants of CREATE ... SELECT.
* [Revision #6681a49](https://github.com/MariaDB/server/commit/6681a49)\
  2016-09-30 13:13:18 -0700
  * Post-review addition to the fix for [MDEV-10868](https://jira.mariadb.org/browse/MDEV-10868).
* [Revision #061d282](https://github.com/MariaDB/server/commit/061d282)\
  2016-09-30 13:10:58 -0700
  * Fixed bug [MDEV-10923](https://jira.mariadb.org/browse/MDEV-10923). The code for st\_select\_lex::find\_table\_def\_in\_with\_clauses() did not take into account the fact that the specs for mergeable CTEs were cloned and were not processed by the function With\_element::check\_dependencies\_in\_spec().
* [Revision #903f34c](https://github.com/MariaDB/server/commit/903f34c)\
  2016-09-29 01:15:00 -0700
  * Fixed bug [MDEV-10868](https://jira.mariadb.org/browse/MDEV-10868). There was no implementation of the virtual method print() for the Item\_window\_func class. As a result for a view containing window function an invalid view definition could be written in the frm file. When a query that refers to this view was executed a syntax error was reported.
* [Revision #6aeaebd](https://github.com/MariaDB/server/commit/6aeaebd)\
  2016-09-27 19:08:36 -0700
  * Fixed the bug number in the comment of the test case for [MDEV-10899](https://jira.mariadb.org/browse/MDEV-10899).
* [Revision #e5019d3](https://github.com/MariaDB/server/commit/e5019d3)\
  2016-09-30 08:45:51 +0300
  * [MDEV-10908](https://jira.mariadb.org/browse/MDEV-10908): innodb\_zip.bug56680 fails in buildbot with InnoDB: Failing assertion: bpage->id.space() == page\_id.space()
* [Revision #737295c](https://github.com/MariaDB/server/commit/737295c)\
  2016-09-29 13:59:41 +0300
  * [MDEV-10727](https://jira.mariadb.org/browse/MDEV-10727): Merge 5.7 Innochecksum with 5.6
* [Revision #b3f7d52](https://github.com/MariaDB/server/commit/b3f7d52)\
  2016-09-29 13:25:45 +0000
  * [MDEV-10918](https://jira.mariadb.org/browse/MDEV-10918) Innodb/Linux - Fallback to simulated aio if io\_setup() fails, e.g due to insufficient resources
* [Revision #098f0ae](https://github.com/MariaDB/server/commit/098f0ae)\
  2016-09-27 09:51:32 -0400
  * bump the VERSION
* [Revision #b91bd82](https://github.com/MariaDB/server/commit/b91bd82)\
  2016-09-26 10:40:44 -0700
  * Fixed bug [MDEV-10889](https://jira.mariadb.org/browse/MDEV-10889) The bug was in the code of the recursive method With\_element::check\_unrestricted\_recursive. For recursive calls of this method sel->get\_with\_element()->owner != owner.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
