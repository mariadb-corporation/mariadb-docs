# MariaDB 10.3.37 Changelog

The most recent release of [MariaDB 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/changelogs/changelogs-mariadb-10-3-series) is:[**MariaDB 10.3.39**](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/changelogs/changelogs-mariadb-10-3-series/mariadb-10-3-39-changelog) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download 10.3.37](https://downloads.mariadb.org/mariadb/10.3.37/) [Release Notes](../../../mariadb-community-server-release-notes/changelogs/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/)[Changelog](mariadb-10-3-37-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 7 Nov 2022

For the highlights of this release, see the [release notes](../../../mariadb-community-server-release-notes/changelogs/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.44](../changelogs-mariadb-102-series/mariadb-10244-changelog.md)
* [Revision #3303748fd1](https://github.com/MariaDB/server/commit/3303748fd1)\
  2022-11-02 12:49:24 +0100
  * [MDEV-29926](https://jira.mariadb.org/browse/MDEV-29926): ASAN heap-use-after-free in Explain\_query::Explain\_query
* [Revision #278fbe61d8](https://github.com/MariaDB/server/commit/278fbe61d8)\
  2022-10-26 10:14:34 +0200
  * Add skipped changes to oracle mode parser.
* [Revision #fa5f26b422](https://github.com/MariaDB/server/commit/fa5f26b422)\
  2022-09-22 15:13:22 +0100
  * [MDEV-29578](https://jira.mariadb.org/browse/MDEV-29578) Fix CONNECT build warnings
* [Revision #055cb3fcd1](https://github.com/MariaDB/server/commit/055cb3fcd1)\
  2022-10-22 23:08:06 -0400
  * Rocksdb: Add initial OpenBSD support
* [Revision #77951dd710](https://github.com/MariaDB/server/commit/77951dd710)\
  2022-10-25 23:48:54 +0400
  * [MDEV-26161](https://jira.mariadb.org/browse/MDEV-26161) crash in Gis\_point::calculate\_haversine
* [Revision #e910dff81e](https://github.com/MariaDB/server/commit/e910dff81e)\
  2022-10-25 21:21:19 +0200
  * [MDEV-26161](https://jira.mariadb.org/browse/MDEV-26161) crash in Gis\_point::calculate\_haversine
* [Revision #72e79eaaf3](https://github.com/MariaDB/server/commit/72e79eaaf3)\
  2022-10-25 20:24:11 +0200
  * cleanup: put casts in a separate statement
* [Revision #1ff476b415](https://github.com/MariaDB/server/commit/1ff476b415)\
  2022-09-12 14:39:12 +0200
  * [MDEV-29490](https://jira.mariadb.org/browse/MDEV-29490) Renaming internally used client API to avoid name conflicts
* [Revision #32158be720](https://github.com/MariaDB/server/commit/32158be720)\
  2022-10-21 19:50:07 +0200
  * [MDEV-29811](https://jira.mariadb.org/browse/MDEV-29811) server advertises ssl even if it's unusable.
* [Revision #34ff5ca895](https://github.com/MariaDB/server/commit/34ff5ca895)\
  2022-10-24 15:52:29 +0200
  * [MDEV-28701](https://jira.mariadb.org/browse/MDEV-28701) Update 10.3 HELP tables
* [Revision #4fd6dd2d3b](https://github.com/MariaDB/server/commit/4fd6dd2d3b)\
  2022-10-12 15:59:46 +0200
  * [MDEV-29748](https://jira.mariadb.org/browse/MDEV-29748) ASAN errors or server crash in File\_parser::parse upon concurrent view operations
* [Revision #e00ea301ef](https://github.com/MariaDB/server/commit/e00ea301ef)\
  2022-10-21 13:47:17 +0200
  * [MDEV-16549](https://jira.mariadb.org/browse/MDEV-16549) Server crashes in Item\_field::fix\_fields on query with view and subquery, Assertion `context' failed, Assertion` field' failed
* [Revision #28d6f6a514](https://github.com/MariaDB/server/commit/28d6f6a514)\
  2022-10-24 13:58:14 +0400
  * [MDEV-14983](https://jira.mariadb.org/browse/MDEV-14983) Wrong error message with SET sql\_mode=sha2(ucs2\_value)
* [Revision #68fb05c360](https://github.com/MariaDB/server/commit/68fb05c360)\
  2022-10-22 17:11:04 +0200
  * [MDEV-29851](https://jira.mariadb.org/browse/MDEV-29851) Cached role privileges are not invalidated when needed
* [Revision #7a2f995649](https://github.com/MariaDB/server/commit/7a2f995649)\
  2022-10-22 17:06:50 +0200
  * cleanup: rename test file
* [Revision #741c14cbdd](https://github.com/MariaDB/server/commit/741c14cbdd)\
  2022-10-22 12:33:09 +0200
  * remove two acl\_cache->clear()
* [Revision #16d4431ab6](https://github.com/MariaDB/server/commit/16d4431ab6)\
  2022-10-22 11:45:38 +0200
  * CONNECT: compile with libxml2 2.10.x
* [Revision #0609b34555](https://github.com/MariaDB/server/commit/0609b34555)\
  2022-10-21 20:37:09 +0200
  * disable LTO in debian builds
* [Revision #3e377fd35b](https://github.com/MariaDB/server/commit/3e377fd35b)\
  2022-10-21 19:40:08 +0200
  * [MDEV-15795](https://jira.mariadb.org/browse/MDEV-15795) Stack exceeded if pthread\_attr\_setstacksize(\&thr\_attr,8196) succeeds
* [Revision #68391acef2](https://github.com/MariaDB/server/commit/68391acef2)\
  2022-10-22 10:22:56 +0200
  * fix for x86 and other 32-bit little engian arch
* [Revision #45755c4e1b](https://github.com/MariaDB/server/commit/45755c4e1b)\
  2022-09-13 00:41:43 +0000
  * Use OPENSSL\_free instead of free to avoid instance crash
* [Revision #e46217182f](https://github.com/MariaDB/server/commit/e46217182f)\
  2022-10-12 10:42:54 +1100
  * [MDEV-29678](https://jira.mariadb.org/browse/MDEV-29678) Valgrind/MSAN uninitialised value errors upon PS with ALTER under ONLY\_FULL\_GROUP\_BY
* [Revision #6bc2e93381](https://github.com/MariaDB/server/commit/6bc2e93381)\
  2022-10-21 12:04:00 +0300
  * [MDEV-23160](https://jira.mariadb.org/browse/MDEV-23160): SIGSEGV in Explain\_node::print\_explain\_for\_children on UNION SELECT
* [Revision #0c06320ae9](https://github.com/MariaDB/server/commit/0c06320ae9)\
  2022-10-21 14:26:06 +0200
  * [MDEV-29687](https://jira.mariadb.org/browse/MDEV-29687):ODBC tables do not quote identifier names correctly (#2295)
* [Revision #e1414fc7e3](https://github.com/MariaDB/server/commit/e1414fc7e3)\
  2022-10-20 08:29:56 +0530
  * [MDEV-29778](https://jira.mariadb.org/browse/MDEV-29778) Having Unique index interference with MATCH from a FULLTEXT
* [Revision #e11661a4a2](https://github.com/MariaDB/server/commit/e11661a4a2)\
  2022-09-21 11:29:07 +0800
  * [MDEV-25343](https://jira.mariadb.org/browse/MDEV-25343) Error log message not helpful when filekey is too long
* [Revision #9de37e07de](https://github.com/MariaDB/server/commit/9de37e07de)\
  2022-10-18 00:01:58 +0400
  * [MDEV-19569](https://jira.mariadb.org/browse/MDEV-19569) Assertion \`table\_list->table' failed in find\_field\_in\_table\_ref.
* [Revision #3a62ff7e89](https://github.com/MariaDB/server/commit/3a62ff7e89)\
  2022-10-19 19:25:48 +1100
  * Revert "[MDEV-25343](https://jira.mariadb.org/browse/MDEV-25343) add read secret size in file key plugin"
* [Revision #cee7175b79](https://github.com/MariaDB/server/commit/cee7175b79)\
  2022-09-21 11:29:07 +0800
  * [MDEV-25343](https://jira.mariadb.org/browse/MDEV-25343) add read secret size in file key plugin
* [Revision #64d85c369b](https://github.com/MariaDB/server/commit/64d85c369b)\
  2022-09-22 14:57:57 +0800
  * [MDEV-28720](https://jira.mariadb.org/browse/MDEV-28720) add log message if flush log failure
* [Revision #8c38939369](https://github.com/MariaDB/server/commit/8c38939369)\
  2022-09-16 11:20:41 +1000
  * [MDEV-29540](https://jira.mariadb.org/browse/MDEV-29540) Incorrect sequence values in INSERT SELECT
* [Revision #d6707ab11f](https://github.com/MariaDB/server/commit/d6707ab11f)\
  2022-10-18 10:29:15 +0300
  * [MDEV-29753](https://jira.mariadb.org/browse/MDEV-29753) fixup: Silence bogus GCC -Og -Wmaybe-uninitialized
* [Revision #64f822c142](https://github.com/MariaDB/server/commit/64f822c142)\
  2022-07-04 08:27:36 -0500
  * [MDEV-28455](https://jira.mariadb.org/browse/MDEV-28455): CREATE TEMPORARY TABLES privilege is insufficient for SHOW COLUMNS
* [Revision #bd9274faa4](https://github.com/MariaDB/server/commit/bd9274faa4)\
  2022-10-17 15:05:17 +0700
  * [MDEV-16128](https://jira.mariadb.org/browse/MDEV-16128): Server crash in Item\_func::print\_op on 2nd execution of PS
* [Revision #4b92fedc62](https://github.com/MariaDB/server/commit/4b92fedc62)\
  2022-10-15 23:50:09 +0200
  * new 3.1
* [Revision #b20f608d4f](https://github.com/MariaDB/server/commit/b20f608d4f)\
  2022-10-16 20:38:04 +0200
  * Update ODBC instructions for Connect SE and update ODBC result file (#2284)
* [Revision #5f25a91140](https://github.com/MariaDB/server/commit/5f25a91140)\
  2022-10-16 13:44:51 -0400
  * Cleanup the alloca.h header handling to further reduce hardcoded OS lists (#2289)
* [Revision #e0b4db5ba3](https://github.com/MariaDB/server/commit/e0b4db5ba3)\
  2022-10-11 12:56:01 +0200
  * [MDEV-29750](https://jira.mariadb.org/browse/MDEV-29750) triggers can modify history
* [Revision #78030b67b9](https://github.com/MariaDB/server/commit/78030b67b9)\
  2022-10-14 11:54:05 +0300
  * Do not use C++11 before [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/)
* [Revision #3d9b350a9c](https://github.com/MariaDB/server/commit/3d9b350a9c)\
  2022-10-14 11:00:34 +0300
  * Fix clang -Wunused-but-set-variable
* Merge [Revision #89e3815b39](https://github.com/MariaDB/server/commit/89e3815b39) 2022-10-14 08:29:11 +0200 - Merge branch 'bb-10.3-vp-[MDEV-27691](https://jira.mariadb.org/browse/MDEV-27691)' into 10.3
* [Revision #72ba96a48e](https://github.com/MariaDB/server/commit/72ba96a48e)\
  2022-06-09 10:32:51 +0700
  * [MDEV-27691](https://jira.mariadb.org/browse/MDEV-27691): make working view-protocol
* [Revision #1dd6255ffe](https://github.com/MariaDB/server/commit/1dd6255ffe)\
  2022-06-27 14:22:57 +0200
  * [MDEV-27691](https://jira.mariadb.org/browse/MDEV-27691): prequisite enable/disable service connection
* [Revision #1f5615360c](https://github.com/MariaDB/server/commit/1f5615360c)\
  2022-10-13 14:43:35 +0300
  * Silence clang 13 -Wunused-but-set-variable
* [Revision #128356b4b1](https://github.com/MariaDB/server/commit/128356b4b1)\
  2022-10-10 19:41:09 +0300
  * [MDEV-29753](https://jira.mariadb.org/browse/MDEV-29753) An error is wrongly reported during INSERT with vcol index
* [Revision #3cd2c1e8b6](https://github.com/MariaDB/server/commit/3cd2c1e8b6)\
  2022-08-17 18:46:04 +0300
  * [MDEV-29299](https://jira.mariadb.org/browse/MDEV-29299) SELECT from table with vcol index reports warning
* [Revision #4fec99a2ba](https://github.com/MariaDB/server/commit/4fec99a2ba)\
  2022-10-11 04:22:05 -0700
  * [MDEV-29102](https://jira.mariadb.org/browse/MDEV-29102) system\_time\_zone is incorrect on Windows when TZ is set
* [Revision #e8101a4d03](https://github.com/MariaDB/server/commit/e8101a4d03)\
  2022-10-11 13:56:47 +0300
  * [MDEV-19455](https://jira.mariadb.org/browse/MDEV-19455)/[MDEV-29342](https://jira.mariadb.org/browse/MDEV-29342) fixup: Avoid DEBUG\_DBUG=-d,...
* [Revision #7a28c82dcd](https://github.com/MariaDB/server/commit/7a28c82dcd)\
  2022-10-11 06:40:50 -0400
  * [MDEV-29183](https://jira.mariadb.org/browse/MDEV-29183): Clarify mysqlbinlog command description (#2245)
* [Revision #c49ebd2622](https://github.com/MariaDB/server/commit/c49ebd2622)\
  2022-10-11 10:15:09 +0200
  * [MDEV-21905](https://jira.mariadb.org/browse/MDEV-21905): Galera test galera\_var\_notify\_cmd causes hang
* [Revision #e05ab0cfc5](https://github.com/MariaDB/server/commit/e05ab0cfc5)\
  2022-10-10 09:36:43 +0300
  * Silence clang 13 -Wunused-but-set-variable for Bison
* [Revision #56b97ca03a](https://github.com/MariaDB/server/commit/56b97ca03a)\
  2022-10-10 09:12:55 +0300
  * [MDEV-29742](https://jira.mariadb.org/browse/MDEV-29742) heap number overflow
* [Revision #602124bb3b](https://github.com/MariaDB/server/commit/602124bb3b)\
  2022-08-08 15:03:52 +0200
  * Remove redudant defines USE\_MB and USE\_MB\_IDENT
* [Revision #d099bcadc3](https://github.com/MariaDB/server/commit/d099bcadc3)\
  2022-10-06 08:52:51 +0300
  * Test results updated.
* [Revision #09f7889b5c](https://github.com/MariaDB/server/commit/09f7889b5c)\
  2022-10-06 08:51:16 +0300
  * [MDEV-29706](https://jira.mariadb.org/browse/MDEV-29706) : SIGSEGV in wsrep\_TOI\_begin on non-Galera builds
* [Revision #074e358213](https://github.com/MariaDB/server/commit/074e358213)\
  2022-10-05 17:46:51 +0300
  * [MDEV-29697](https://jira.mariadb.org/browse/MDEV-29697) Assertion failure in Diagnostics\_area::set\_ok\_status upon CREATE OR REPLACE causing ER\_UPDATE\_TABLE\_USED
* [Revision #0779e2cb10](https://github.com/MariaDB/server/commit/0779e2cb10)\
  2022-10-05 17:46:51 +0300
  * [MDEV-28576](https://jira.mariadb.org/browse/MDEV-28576) RENAME COLUMN with NOCOPY algorithm leads to corrupt partitioned table
* [Revision #4eb8c35b36](https://github.com/MariaDB/server/commit/4eb8c35b36)\
  2022-10-05 17:46:50 +0300
  * [MDEV-28576](https://jira.mariadb.org/browse/MDEV-28576) Ability to manipulate List\<const char \*>
* [Revision #c0eda62aec](https://github.com/MariaDB/server/commit/c0eda62aec)\
  2022-08-31 17:49:38 +0300
  * [MDEV-27927](https://jira.mariadb.org/browse/MDEV-27927) row\_sel\_try\_search\_shortcut\_for\_mysql() does not latch a page, violating read view isolation
* [Revision #111cbdf3da](https://github.com/MariaDB/server/commit/111cbdf3da)\
  2022-10-05 15:18:58 +0300
  * [MDEV-29710](https://jira.mariadb.org/browse/MDEV-29710): Valgrind tests massively fail due to silently killing server on shutdown timeout
* [Revision #e0bcff10ef](https://github.com/MariaDB/server/commit/e0bcff10ef)\
  2022-10-05 15:18:44 +0300
  * [MDEV-29710](https://jira.mariadb.org/browse/MDEV-29710): Disable main.log\_slow under Valgrind
* [Revision #380e06f84b](https://github.com/MariaDB/server/commit/380e06f84b)\
  2022-10-05 15:16:03 +0300
  * [MDEV-29710](https://jira.mariadb.org/browse/MDEV-29710): Disable sys\_vars.innodb\_flush\_method\_func under Valgrind
* [Revision #c64e2d60a3](https://github.com/MariaDB/server/commit/c64e2d60a3)\
  2022-10-05 15:15:28 +0300
  * [MDEV-29710](https://jira.mariadb.org/browse/MDEV-29710): Disable innodb.table\_flags under Valgrind
* [Revision #1562b2c20b](https://github.com/MariaDB/server/commit/1562b2c20b)\
  2022-10-05 09:30:33 +0300
  * [MDEV-29666](https://jira.mariadb.org/browse/MDEV-29666) InnoDB fails to purge secondary index records when indexed virtual columns exist
* [Revision #19f0b96d53](https://github.com/MariaDB/server/commit/19f0b96d53)\
  2022-10-04 13:15:52 +0200
  * [MDEV-27682](https://jira.mariadb.org/browse/MDEV-27682): bundled wsrep\_notify.sh causes mariadbd to freeze during start
* [Revision #c0817dac99](https://github.com/MariaDB/server/commit/c0817dac99)\
  2022-09-30 19:38:59 +0300
  * [MDEV-29575](https://jira.mariadb.org/browse/MDEV-29575) Access to innodb\_trx, innodb\_locks and innodb\_lock\_waits along with detached XA's can cause SIGSEGV
* [Revision #dd8833bff0](https://github.com/MariaDB/server/commit/dd8833bff0)\
  2022-10-01 16:10:27 +0200
  * cleanup: suppress rocksdb compilation warning, fix a comment
* [Revision #fa6d7e4e98](https://github.com/MariaDB/server/commit/fa6d7e4e98)\
  2022-10-01 16:11:13 +0200
  * compilation error
* [Revision #f65ba9aeb7](https://github.com/MariaDB/server/commit/f65ba9aeb7)\
  2019-04-17 15:50:59 +0200
  * [MDEV-17124](https://jira.mariadb.org/browse/MDEV-17124): [mariadb 10.1.34](../../old-releases/10.1/10.1.34.md), views and prepared statements: ERROR 1615 (HY000): Prepared statement needs to be re-prepared
* [Revision #98e62e6317](https://github.com/MariaDB/server/commit/98e62e6317)\
  2018-11-13 09:12:55 +0100
  * Better declaration of the buffer size
* [Revision #1f51d6c0f6](https://github.com/MariaDB/server/commit/1f51d6c0f6)\
  2022-07-16 14:39:17 +0200
  * [MDEV-28548](https://jira.mariadb.org/browse/MDEV-28548): ER\_TABLEACCESS\_DENIED\_ERROR is missing information about DB
* [Revision #f9605eb209](https://github.com/MariaDB/server/commit/f9605eb209)\
  2022-09-29 00:58:09 +0200
  * fix sporadic failures on main.kill
* [Revision #28ae361857](https://github.com/MariaDB/server/commit/28ae361857)\
  2022-09-22 21:40:33 -0700
  * [MDEV-29361](https://jira.mariadb.org/browse/MDEV-29361) Infinite recursive calls when detecting CTE dependencies
* [Revision #9de9f105b5](https://github.com/MariaDB/server/commit/9de9f105b5)\
  2022-09-28 07:45:25 -0700
  * Use memory safe snprintf() in Connect Engine and elsewhere (#2210)
* [Revision #b2cfcf1d1f](https://github.com/MariaDB/server/commit/b2cfcf1d1f)\
  2022-08-19 11:24:51 +0400
  * [MDEV-21134](https://jira.mariadb.org/browse/MDEV-21134) Crash with partitioned table, PARTITION syntax, and index\_merge.
* [Revision #47e9678982](https://github.com/MariaDB/server/commit/47e9678982)\
  2022-07-04 15:23:01 +0200
  * [MDEV-29022](https://jira.mariadb.org/browse/MDEV-29022) add\_slave destroy child list and has dead code
* [Revision #2b89598fe0](https://github.com/MariaDB/server/commit/2b89598fe0)\
  2021-10-19 13:59:14 +0900
  * [MDEV-26852](https://jira.mariadb.org/browse/MDEV-26852) Spider: -Werror=maybe-uninitialized raises on spd\_sys\_table.cc and ha\_spider.cc
* [Revision #fa4e84b5d9](https://github.com/MariaDB/server/commit/fa4e84b5d9)\
  2022-09-23 14:13:55 +0200
  * cleanup: main.mysqldump test
* [Revision #88db4e3ea4](https://github.com/MariaDB/server/commit/88db4e3ea4)\
  2022-09-23 11:11:15 +0200
  * wsrep suite isn't run by default, wsrep\_info shouldn't either
* [Revision #4fd096df06](https://github.com/MariaDB/server/commit/4fd096df06)\
  2022-09-23 10:52:16 +0200
  * sporadic failures of main.bootstrap
* [Revision #59c9e2f202](https://github.com/MariaDB/server/commit/59c9e2f202)\
  2022-09-26 13:59:23 +0100
  * [MDEV-29579](https://jira.mariadb.org/browse/MDEV-29579) Fix CONNECT ASAN hits (#2277)
* [Revision #b3e06ce3fd](https://github.com/MariaDB/server/commit/b3e06ce3fd)\
  2022-09-26 08:53:43 +0200
  * [MDEV-28533](https://jira.mariadb.org/browse/MDEV-28533): CONNECT engine does not quote columns involved in WHERE clause (#2263)
* [Revision #66cd1c33f7](https://github.com/MariaDB/server/commit/66cd1c33f7)\
  2022-09-23 14:02:41 +0100
  * [MDEV-25767](https://jira.mariadb.org/browse/MDEV-25767) Fix CONNECT ODBC WHERE condition crash (#2243)
* [Revision #ce23802c0e](https://github.com/MariaDB/server/commit/ce23802c0e)\
  2022-09-22 11:18:00 +0300
  * [MDEV-29600](https://jira.mariadb.org/browse/MDEV-29600) Memory leak in row\_log\_table\_apply\_update()
* [Revision #2d5cfdc570](https://github.com/MariaDB/server/commit/2d5cfdc570)\
  2022-09-22 11:08:17 +0300
  * Cleanup: Remove redundant output from a test
* [Revision #f5e4e15403](https://github.com/MariaDB/server/commit/f5e4e15403)\
  2022-09-13 11:46:28 +0900
  * Backport fix for [MDEV-29352](https://jira.mariadb.org/browse/MDEV-29352) to 10.3-10.5
* [Revision #b9c1c07f83](https://github.com/MariaDB/server/commit/b9c1c07f83)\
  2022-08-31 10:22:29 +0200
  * [MDEV-29275](https://jira.mariadb.org/browse/MDEV-29275) Fix server/Docs typos
* [Revision #b6bf7cd192](https://github.com/MariaDB/server/commit/b6bf7cd192)\
  2022-09-16 08:36:11 -0600
  * [MDEV-28986](https://jira.mariadb.org/browse/MDEV-28986): rpl tests sometimes failing on freebsd builders
* [Revision #fc8a765532](https://github.com/MariaDB/server/commit/fc8a765532)\
  2022-09-15 12:06:55 +0200
  * [MDEV-29480](https://jira.mariadb.org/browse/MDEV-29480) spider group by handler wrong result on order by aggregate alias
* [Revision #5dcc56be4d](https://github.com/MariaDB/server/commit/5dcc56be4d)\
  2022-09-20 10:29:37 +0400
  * [MDEV-29561](https://jira.mariadb.org/browse/MDEV-29561) SHOW CREATE TABLE produces syntactically incorrect structure
* [Revision #65b4a2afb8](https://github.com/MariaDB/server/commit/65b4a2afb8)\
  2022-09-19 13:25:45 +0100
  * [MDEV-29426](https://jira.mariadb.org/browse/MDEV-29426) Fix memory leak in CONNECT JSON/BSON (#2255)
* [Revision #5e959bc363](https://github.com/MariaDB/server/commit/5e959bc363)\
  2022-09-19 13:30:52 +0300
  * Fix clang -Wunused-but-set-variable
* [Revision #3ab4b260e1](https://github.com/MariaDB/server/commit/3ab4b260e1)\
  2022-09-19 12:42:50 +0300
  * Merge innodb.cmake to CMakeLists.txt
* [Revision #73658eded3](https://github.com/MariaDB/server/commit/73658eded3)\
  2022-09-19 12:36:19 +0300
  * Cleanup: Remove HAVE\_IB\_LINUX\_FUTEX
* [Revision #4c8b65db08](https://github.com/MariaDB/server/commit/4c8b65db08)\
  2022-09-19 12:29:16 +0300
  * Cleanup: Remove INNODB\_COMPILER\_HINTS
* [Revision #c22dff21a5](https://github.com/MariaDB/server/commit/c22dff21a5)\
  2022-09-19 12:20:53 +0300
  * InnoDB cleanup: Replace UNIV\_LINUX, UNIV\_SOLARIS, UNIV\_AIX
* [Revision #bbf81b51f2](https://github.com/MariaDB/server/commit/bbf81b51f2)\
  2022-09-19 10:23:57 +0300
  * Correct typos in a function comment
* [Revision #32bab2ce05](https://github.com/MariaDB/server/commit/32bab2ce05)\
  2022-09-15 09:36:44 +0200
  * [MDEV-29543](https://jira.mariadb.org/browse/MDEV-29543) Windows: Unreadable dlerror() message on localized OS
* [Revision #beffef9f00](https://github.com/MariaDB/server/commit/beffef9f00)\
  2022-09-14 19:15:26 +0200
  * [MDEV-22647](https://jira.mariadb.org/browse/MDEV-22647) Assertion \`!check\_audit\_mask(mysql\_global\_audit\_mask, event\_class\_mask)'
* [Revision #b7928f7566](https://github.com/MariaDB/server/commit/b7928f7566)\
  2022-08-16 15:53:42 +0200
  * Add missing comment and remove unnecessary initialization
* [Revision #16b2bb909a](https://github.com/MariaDB/server/commit/16b2bb909a)\
  2022-09-12 10:44:12 +0300
  * [MDEV-29509](https://jira.mariadb.org/browse/MDEV-29509) execute granted indirectly (via roles) doesn't always work
* [Revision #5ad8cd93b7](https://github.com/MariaDB/server/commit/5ad8cd93b7)\
  2022-09-13 10:10:36 +0300
  * cleanup: indentation and whitespace fixes
* [Revision #7735ba7666](https://github.com/MariaDB/server/commit/7735ba7666)\
  2022-09-13 10:04:33 +0300
  * [MDEV-29458](https://jira.mariadb.org/browse/MDEV-29458): Role grant commands do not propagate all grants
* [Revision #145932a57b](https://github.com/MariaDB/server/commit/145932a57b)\
  2022-09-05 13:15:16 +0300
  * [MDEV-29465](https://jira.mariadb.org/browse/MDEV-29465): Inherited columns privs for roles wrongly set mysql.tables\_priv column
* [Revision #d7aefc0fab](https://github.com/MariaDB/server/commit/d7aefc0fab)\
  2022-09-07 15:10:16 +0530
  * [MDEV-29479](https://jira.mariadb.org/browse/MDEV-29479) I\_S.INNODB\_SYS\_TABLESPACES doesn't have temporary tablespace information
* [Revision #5af7149ff5](https://github.com/MariaDB/server/commit/5af7149ff5)\
  2022-09-13 10:32:38 +0200
  * mysql\_release: treat alma|rocky as centos|rhel
* [Revision #68ce0231ad](https://github.com/MariaDB/server/commit/68ce0231ad)\
  2022-09-13 15:46:40 +0300
  * [MDEV-23801](https://jira.mariadb.org/browse/MDEV-23801) Assertion failed in btr\_pcur\_store\_position()
* [Revision #4c14243373](https://github.com/MariaDB/server/commit/4c14243373)\
  2022-09-13 12:44:23 +0400
  * A cleanup for [MDEV-29446](https://jira.mariadb.org/browse/MDEV-29446) Change SHOW CREATE TABLE to display default collation
* [Revision #83175219c3](https://github.com/MariaDB/server/commit/83175219c3)\
  2022-09-12 23:57:20 +0200
  * [MDEV-29522](https://jira.mariadb.org/browse/MDEV-29522) RocksDB RPM doesn't get built on Rocky Linux and Alma
* [Revision #fc794fd8ff](https://github.com/MariaDB/server/commit/fc794fd8ff)\
  2022-09-13 08:58:34 +0300
  * [MDEV-29520](https://jira.mariadb.org/browse/MDEV-29520) heap-use-after-poison in row\_merge\_spatial\_rows()
* [Revision #f1544424de](https://github.com/MariaDB/server/commit/f1544424de)\
  2022-09-02 17:32:14 +0400
  * [MDEV-29446](https://jira.mariadb.org/browse/MDEV-29446) Change SHOW CREATE TABLE to display default collation
* [Revision #667df98c3e](https://github.com/MariaDB/server/commit/667df98c3e)\
  2022-09-12 09:27:46 +0300
  * [MDEV-29507](https://jira.mariadb.org/browse/MDEV-29507) InnoDB: Failing assertion: table->n\_rec\_locks == 0
* [Revision #43745b7e17](https://github.com/MariaDB/server/commit/43745b7e17)\
  2022-09-01 09:55:49 +0300
  * [MDEV-29433](https://jira.mariadb.org/browse/MDEV-29433) innodb.lock\_delete\_updated is unstable
* [Revision #04899d6d91](https://github.com/MariaDB/server/commit/04899d6d91)\
  2022-09-07 16:05:09 +0300
  * [MDEV-28605](https://jira.mariadb.org/browse/MDEV-28605): Change wrong plugin config installation location (#2160)
* [Revision #ac49b7a845](https://github.com/MariaDB/server/commit/ac49b7a845)\
  2022-08-29 22:54:25 +0530
  * [MDEV-29342](https://jira.mariadb.org/browse/MDEV-29342) Assertion failure in file que0que.cc line 728
* [Revision #f501f815bc](https://github.com/MariaDB/server/commit/f501f815bc)\
  2022-08-26 18:35:15 +0300
  * [MDEV-28827](https://jira.mariadb.org/browse/MDEV-28827) Minor unsafe statement warning message improvement
* [Revision #47812017c6](https://github.com/MariaDB/server/commit/47812017c6)\
  2022-05-10 14:25:35 -0600
  * [MDEV-28530](https://jira.mariadb.org/browse/MDEV-28530): Revoking privileges from a non-existing user on a master breaks replication on the slave in the presence of replication filters
* [Revision #e4cffc92c7](https://github.com/MariaDB/server/commit/e4cffc92c7)\
  2022-06-30 01:58:57 +0900
  * [MDEV-27172](https://jira.mariadb.org/browse/MDEV-27172) Prefix indices on Spider tables may lead to wrong query results
* [Revision #4f2dc716ee](https://github.com/MariaDB/server/commit/4f2dc716ee)\
  2022-08-31 15:58:52 +0300
  * [MDEV-13668](https://jira.mariadb.org/browse/MDEV-13668) fixup: Remove test work-arounds
* [Revision #c487eeed10](https://github.com/MariaDB/server/commit/c487eeed10)\
  2022-08-31 15:24:06 +1000
  * [MDEV-28592](https://jira.mariadb.org/browse/MDEV-28592) disks plugin (postfix - remove tabs)
* [Revision #129616c70a](https://github.com/MariaDB/server/commit/129616c70a)\
  2022-07-31 13:41:59 +1000
  * [MDEV-28592](https://jira.mariadb.org/browse/MDEV-28592) disks plugin - getmntinfo (BSD) & getmntent (AIX)
* [Revision #57739ae94a](https://github.com/MariaDB/server/commit/57739ae94a)\
  2022-08-30 12:03:58 +0300
  * [MDEV-13888](https://jira.mariadb.org/browse/MDEV-13888): innodb\_fts.innodb\_fts\_plugin failed
* [Revision #422f3204ef](https://github.com/MariaDB/server/commit/422f3204ef)\
  2022-08-30 12:02:56 +0300
  * [MDEV-29409](https://jira.mariadb.org/browse/MDEV-29409) Buffer overflow in my\_wc\_mb\_filename() on RENAME TABLE
* [Revision #b260903832](https://github.com/MariaDB/server/commit/b260903832)\
  2022-08-30 10:59:31 +0300
  * [MDEV-29258](https://jira.mariadb.org/browse/MDEV-29258) Failing assertion for name length on RENAME TABLE
* [Revision #0d1de5e1d1](https://github.com/MariaDB/server/commit/0d1de5e1d1)\
  2022-08-28 21:23:28 +0300
  * [MDEV-29403](https://jira.mariadb.org/browse/MDEV-29403) innodb.innodb\_sys\_semaphore\_waits fails with wrong errno 5014
* [Revision #94e3f02db7](https://github.com/MariaDB/server/commit/94e3f02db7)\
  2022-08-24 11:07:09 -0700
  * [MDEV-29350](https://jira.mariadb.org/browse/MDEV-29350) Crash when IN predicand is used in eliminated GROUP BY clause
* [Revision #d1a80c42ee](https://github.com/MariaDB/server/commit/d1a80c42ee)\
  2022-08-25 15:14:38 +0300
  * [MDEV-29384](https://jira.mariadb.org/browse/MDEV-29384) Hangs caused by innodb\_adaptive\_hash\_index=ON
* [Revision #2f6a728075](https://github.com/MariaDB/server/commit/2f6a728075)\
  2022-08-10 13:27:01 +0200
  * update a global\_suppressions() list
* [Revision #f2a53b6158](https://github.com/MariaDB/server/commit/f2a53b6158)\
  2022-08-24 15:00:47 +0300
  * btr\_search\_drop\_page\_hash\_index(): Remove a racey debug check
* [Revision #61f456e772](https://github.com/MariaDB/server/commit/61f456e772)\
  2022-08-24 12:27:15 +0530
  * [MDEV-29319](https://jira.mariadb.org/browse/MDEV-29319) Assertion failure size\_in\_header >= space.free\_limit in fsp\_get\_available\_space\_in\_free\_extents()
* [Revision #dd737d071e](https://github.com/MariaDB/server/commit/dd737d071e)\
  2022-08-17 18:09:06 +0530
  * [MDEV-29291](https://jira.mariadb.org/browse/MDEV-29291) Assertion \`!table->fts' failed in dict\_table\_can\_be\_evicted on SHUTDOWN
* [Revision #0b80573310](https://github.com/MariaDB/server/commit/0b80573310)\
  2022-08-22 18:36:30 +0530
  * [MDEV-29319](https://jira.mariadb.org/browse/MDEV-29319) Assertion failure size\_in\_header >= space.free\_limit in fsp\_get\_available\_space\_in\_free\_extents()
* [Revision #8963d64ee8](https://github.com/MariaDB/server/commit/8963d64ee8)\
  2022-04-26 19:51:42 -0600
  * [MDEV-28294](https://jira.mariadb.org/browse/MDEV-28294): set default role bypasses Replicate\_Wild\_Ignore\_Table: mysql.%
* [Revision #c7f8cfc9e7](https://github.com/MariaDB/server/commit/c7f8cfc9e7)\
  2022-08-16 15:31:49 +0530
  * [MDEV-27700](https://jira.mariadb.org/browse/MDEV-27700) ASAN: Heap\_use\_after\_free in btr\_search\_drop\_page\_hash\_index()
* [Revision #fd0cd4801a](https://github.com/MariaDB/server/commit/fd0cd4801a)\
  2022-08-22 12:32:47 +0300
  * [MDEV-13013](https://jira.mariadb.org/browse/MDEV-13013) fixup: Adjust a test
* [Revision #a1055ab35d](https://github.com/MariaDB/server/commit/a1055ab35d)\
  2022-08-19 09:18:24 +0300
  * [MDEV-29043](https://jira.mariadb.org/browse/MDEV-29043) mariadb-backup --compress hangs
* [Revision #32167225c7](https://github.com/MariaDB/server/commit/32167225c7)\
  2022-08-16 17:34:38 +0530
  * [MDEV-13013](https://jira.mariadb.org/browse/MDEV-13013) InnoDB unnecessarily extends data files
* [Revision #c208006080](https://github.com/MariaDB/server/commit/c208006080)\
  2022-07-28 21:24:57 +0900
  * [MDEV-29008](https://jira.mariadb.org/browse/MDEV-29008) Server crash or assertion \`field' failed in spider\_db\_open\_item\_ident / group by handler
* Merge [Revision #8c21dc52ee](https://github.com/MariaDB/server/commit/8c21dc52ee) 2022-08-15 10:11:23 +0200 - Merge branch '10.3' into bb-10.3-release
* [Revision #6d90d2ba7f](https://github.com/MariaDB/server/commit/6d90d2ba7f)\
  2022-08-14 21:45:05 -0400
  * bump the VERSION
* [Revision #d48428e99a](https://github.com/MariaDB/server/commit/d48428e99a)\
  2022-08-01 19:39:09 +0530
  * [MDEV-27151](https://jira.mariadb.org/browse/MDEV-27151): JSON\_VALUE() does not parse NULL properties properly
* [Revision #d7ba72ea9b](https://github.com/MariaDB/server/commit/d7ba72ea9b)\
  2022-08-06 22:18:11 -0400
  * Remove Darwin CMake file

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
