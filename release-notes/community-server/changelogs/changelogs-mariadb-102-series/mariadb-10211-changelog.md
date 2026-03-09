# MariaDB 10.2.11 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.11)[Release Notes](../../old-releases/10.2/10.2.11.md)[Changelog](mariadb-10211-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 28 Nov 2017

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.11.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #77872e4519](https://github.com/MariaDB/server/commit/77872e4519)\
  2017-11-27 12:04:51 +0200
  * Additions to the list of unstable tests for 10.2.11
* [Revision #414d3a3e17](https://github.com/MariaDB/server/commit/414d3a3e17)\
  2017-11-24 17:33:53 +0000
  * Fix warning.
* [Revision #4cc20c88df](https://github.com/MariaDB/server/commit/4cc20c88df)\
  2017-11-24 14:57:44 +0400
  * Fixed build failure with PFS disabled
* Merge [Revision #9cefffdab1](https://github.com/MariaDB/server/commit/9cefffdab1) 2017-11-24 17:30:26 +0000 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #40756c9151](https://github.com/MariaDB/server/commit/40756c9151)\
  2017-11-24 16:55:20 +0000
  * Fix Windows build with -DPLUGIN\_PERFSCHEMA=NO
* Merge [Revision #f1cc6e3874](https://github.com/MariaDB/server/commit/f1cc6e3874) 2017-11-24 17:17:16 +0200 - Merge 10.1 into 10.2
* [Revision #316f0d8fe3](https://github.com/MariaDB/server/commit/316f0d8fe3)\
  2017-11-23 21:01:00 +0000
  * [MDEV-14447](https://jira.mariadb.org/browse/MDEV-14447) mariadb-backup incremental incorrectly extends system tablespace for multi-file innodb\_data\_file\_path.
* [Revision #12840f97cd](https://github.com/MariaDB/server/commit/12840f97cd)\
  2017-11-21 16:20:08 -0500
  * Fix typo, and disable own dtrace proibes on Solaris, really.
* [Revision #83eb14ff65](https://github.com/MariaDB/server/commit/83eb14ff65)\
  2017-11-21 21:30:45 +0100
  * Fix compile error.
* [Revision #b6d72ed44d](https://github.com/MariaDB/server/commit/b6d72ed44d)\
  2017-11-21 21:14:06 +0100
  * [MDEV-14283](https://jira.mariadb.org/browse/MDEV-14283) : Fix Solaris 10 build. - introduce system check for posix\_memalign (not available on Solaris 10) - Disable dtrace probes, to fix weird link errors in mariadb-backup
* [Revision #7c4f859384](https://github.com/MariaDB/server/commit/7c4f859384)\
  2017-11-21 17:19:32 +0000
  * [MDEV-14283](https://jira.mariadb.org/browse/MDEV-14283) : Fix compilation of mariadb-backup for gcc3.x
* [Revision #6979d20426](https://github.com/MariaDB/server/commit/6979d20426)\
  2017-11-24 17:10:29 +0200
  * [MDEV-14499](https://jira.mariadb.org/browse/MDEV-14499) mariadb-backup 10.2 fails to back up a multi-file InnoDB system tablespace
* [Revision #59150361c3](https://github.com/MariaDB/server/commit/59150361c3)\
  2017-11-24 14:39:38 +0100
  * Update C/C to fix unit tests with clang
* [Revision #c5fffb33a4](https://github.com/MariaDB/server/commit/c5fffb33a4)\
  2017-11-24 00:24:37 +0000
  * [MDEV-14483](https://jira.mariadb.org/browse/MDEV-14483) Export \_mysl\_client\_plugin\_declaration from auth\_gssapi\_client.so
* [Revision #e6d6b0c08c](https://github.com/MariaDB/server/commit/e6d6b0c08c)\
  2017-11-24 01:38:38 +0200
  * Updated list of unstable tests for 10.2.11
* [Revision #c666ca7b1b](https://github.com/MariaDB/server/commit/c666ca7b1b)\
  2017-11-23 22:10:31 +0200
  * [MDEV-12012](https://jira.mariadb.org/browse/MDEV-12012). Post-push attempt to catch failure in rpl\_gtid\_delete\_domain failing on P8. The test is made more verbose.
* Merge [Revision #e2dd4e3206](https://github.com/MariaDB/server/commit/e2dd4e3206) 2017-11-23 08:56:06 +0200 - [MDEV-4697](https://jira.mariadb.org/browse/MDEV-4697) UPDATE\_TIME field for InnoDB
* [Revision #187a5bbf28](https://github.com/MariaDB/server/commit/187a5bbf28)\
  2017-11-23 08:54:33 +0200
  * Adjust the tests for MariaDB, and optimize them
* [Revision #f8bc799a89](https://github.com/MariaDB/server/commit/f8bc799a89)\
  2017-11-23 07:47:19 +0200
  * Import [WL#6658](https://askmonty.org/worklog/?tid=6658) update\_time tests from MySQL 5.7
* Merge [Revision #0055e1a57f](https://github.com/MariaDB/server/commit/0055e1a57f) 2017-11-22 17:38:30 +0100 - Merge branch 'connect/10.2' into 10.2
* [Revision #b6563d773a](https://github.com/MariaDB/server/commit/b6563d773a)\
  2017-11-03 11:29:02 +0100\
  \*
  * Fix [MDEV-13860](https://jira.mariadb.org/browse/MDEV-13860) CONNECT engine does not build with JDBC without ODBC. By including Sergei's patch in connect\_assisted\_discovery. modified: storage/connect/ha\_connect.cc
* [Revision #332d9f7b02](https://github.com/MariaDB/server/commit/332d9f7b02)\
  2017-10-31 18:53:15 +0100\
  \*
  * Change inihandl from c to c++. Because it now includes global.h that contains a bool function definition that make compile to fail on Linux. modified: storage/connect/CMakeLists.txt removed: storage/connect/inihandl.c added: storage/connect/inihandl.cpp
* [Revision #646ecb8970](https://github.com/MariaDB/server/commit/646ecb8970)\
  2017-10-31 17:51:25 +0100
  * Change inihandl from c to cpp (to accept bool)
* [Revision #3db76c99cc](https://github.com/MariaDB/server/commit/3db76c99cc)\
  2017-10-31 14:44:50 +0100\
  \*
  * Fix [MDEV-13925](https://jira.mariadb.org/browse/MDEV-13925): Actually this fixes SELECT queries when the WHERE clause have single quote. modified: storage/connect/ha\_connect.cc
* [Revision #37dd3cf424](https://github.com/MariaDB/server/commit/37dd3cf424)\
  2017-08-15 14:30:27 +0300
  * [MDEV-13550](https://jira.mariadb.org/browse/MDEV-13550) Copy ctor instread of memcpy() in partition\_info::get\_clone() (#436)
* [Revision #3422ceb10c](https://github.com/MariaDB/server/commit/3422ceb10c)\
  2017-11-15 21:39:30 +0800
  * remove dead code
* [Revision #f86413ecc1](https://github.com/MariaDB/server/commit/f86413ecc1)\
  2017-11-13 21:25:30 +0000
  * Fix the build on OpenBSD (#488)
* [Revision #14c2a9a52e](https://github.com/MariaDB/server/commit/14c2a9a52e)\
  2017-11-15 09:46:28 +0800
  * don't `git submodule update` from rocksdb/CMakeLists.txt (#492)
* [Revision #8c422bf48d](https://github.com/MariaDB/server/commit/8c422bf48d)\
  2017-11-14 07:22:25 +0800
  * [MDEV-14256](https://jira.mariadb.org/browse/MDEV-14256) [MariaDB 10.2.10](../../old-releases/10.2/10.2.10.md) can't SST with xtrabackup-v2
* [Revision #a963cb95db](https://github.com/MariaDB/server/commit/a963cb95db)\
  2017-11-10 18:55:57 +0100
  * [MDEV-14268](https://jira.mariadb.org/browse/MDEV-14268) Executable C source code files?
* [Revision #5dd505b709](https://github.com/MariaDB/server/commit/5dd505b709)\
  2017-11-20 15:03:44 +0100
  * [MDEV-14428](https://jira.mariadb.org/browse/MDEV-14428) main.cte\_nonrecursive failed in --embedded
* Merge [Revision #7f1900705b](https://github.com/MariaDB/server/commit/7f1900705b) 2017-11-21 19:47:46 +0100 - Merge branch '10.1' into 10.2
* [Revision #b54aeeb080](https://github.com/MariaDB/server/commit/b54aeeb080)\
  2017-11-19 14:05:07 +0100
  * never add new error messages to old GA releases!
* [Revision #685db2c112](https://github.com/MariaDB/server/commit/685db2c112)\
  2017-11-16 10:02:29 +0800
  * Fix the build on OpenBSD (#488)
* [Revision #4666f01534](https://github.com/MariaDB/server/commit/4666f01534)\
  2017-11-14 11:12:13 +0800
  * mroonga after-merge test fixes
* [Revision #d7349e204b](https://github.com/MariaDB/server/commit/d7349e204b)\
  2017-11-16 13:21:07 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #eeec64d75e](https://github.com/MariaDB/server/commit/eeec64d75e)\
  2017-11-16 13:18:22 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #c7e38076f3](https://github.com/MariaDB/server/commit/c7e38076f3)\
  2017-10-16 19:32:02 +0300
  * [MDEV-9510](https://jira.mariadb.org/browse/MDEV-9510) Segmentation fault in binlog thread causes crash
* [Revision #aae4932775](https://github.com/MariaDB/server/commit/aae4932775)\
  2017-09-29 21:56:59 +0300
  * [MDEV-12012](https://jira.mariadb.org/browse/MDEV-12012)/[MDEV-11969](https://jira.mariadb.org/browse/MDEV-11969) Can't remove GTIDs for a stale GTID Domain ID
* [Revision #7e1326cfcf](https://github.com/MariaDB/server/commit/7e1326cfcf)\
  2017-11-14 17:23:17 -0500
  * bump the VERSION
* [Revision #0f43279cc4](https://github.com/MariaDB/server/commit/0f43279cc4)\
  2017-11-06 14:35:58 +0100
  * [MDEV-13936](https://jira.mariadb.org/browse/MDEV-13936): Server crashes in Time\_and\_counter\_tracker::incr\_loops
* [Revision #375caf99c4](https://github.com/MariaDB/server/commit/375caf99c4)\
  2017-11-21 18:53:00 +0200
  * Adjust an imported test
* [Revision #9405fdeb9e](https://github.com/MariaDB/server/commit/9405fdeb9e)\
  2017-11-21 17:52:17 +0200
  * [MDEV-13201](https://jira.mariadb.org/browse/MDEV-13201) Assertion `srv_undo_sources || ...` failed on shutdown during DDL operation
* Merge [Revision #18cdc254b7](https://github.com/MariaDB/server/commit/18cdc254b7) 2017-11-20 16:06:17 +0200 - [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626) Merge InnoDB test cases from MySQL 5.7 (part 3)
* [Revision #f233c9778e](https://github.com/MariaDB/server/commit/f233c9778e)\
  2017-11-20 13:24:43 +0200
  * Adjust the MySQL 5.7 tests for [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md)
* [Revision #55a94ef1cf](https://github.com/MariaDB/server/commit/55a94ef1cf)\
  2017-11-20 12:22:28 +0200
  * Import [WL#7277](https://askmonty.org/worklog/?tid=7277) bulk insert creation tests from MySQL 5.7
* [Revision #ce64a65f27](https://github.com/MariaDB/server/commit/ce64a65f27)\
  2017-11-20 09:49:21 +0200
  * [MDEV-14310](https://jira.mariadb.org/browse/MDEV-14310) Possible corruption by table-rebuilding or index-creating ALTER TABLE…ALGORITHM=INPLACE
* [Revision #a20c1217a5](https://github.com/MariaDB/server/commit/a20c1217a5)\
  2017-11-18 18:29:50 +0400
  * [MDEV-14435](https://jira.mariadb.org/browse/MDEV-14435) Different UNSIGNED flag of out user variable for YEAR parameter for direct vs prepared CALL
* [Revision #4c2c5ec94e](https://github.com/MariaDB/server/commit/4c2c5ec94e)\
  2017-11-18 00:19:46 +0400
  * [MDEV-14434](https://jira.mariadb.org/browse/MDEV-14434) Wrong result for CHARSET(CONCAT(?,const))
* [Revision #0d1e805aeb](https://github.com/MariaDB/server/commit/0d1e805aeb)\
  2017-11-16 22:11:08 +0000
  * Fix rocksdb tests on Windows
* [Revision #689168be12](https://github.com/MariaDB/server/commit/689168be12)\
  2017-11-16 18:57:18 +0000
  * [MDEV-13852](https://jira.mariadb.org/browse/MDEV-13852) - redefine WinWriteableFile such as IsSyncThreadSafe() is set to true, as it should.
* [Revision #842dce378a](https://github.com/MariaDB/server/commit/842dce378a)\
  2017-11-16 19:59:27 +0400
  * [MDEV-14402](https://jira.mariadb.org/browse/MDEV-14402) JSON\_VALUE doesn't escape quote.
* [Revision #0c4d11e819](https://github.com/MariaDB/server/commit/0c4d11e819)\
  2017-11-16 11:05:24 +0200
  * [MDEV-13206](https://jira.mariadb.org/browse/MDEV-13206): INSERT ON DUPLICATE KEY UPDATE foreign key fail
* [Revision #2401d14e6b](https://github.com/MariaDB/server/commit/2401d14e6b)\
  2017-10-25 17:41:23 +0800
  * Support CRC32 SSE2 implementation under Windows
* [Revision #88cc6db0a4](https://github.com/MariaDB/server/commit/88cc6db0a4)\
  2017-11-15 13:25:55 +0100
  * [MDEV-13453](https://jira.mariadb.org/browse/MDEV-13453): Executing a query via CTE requires more permissions than the query itself
* [Revision #5e7435c4b0](https://github.com/MariaDB/server/commit/5e7435c4b0)\
  2017-11-15 08:53:02 +0200
  * Correct a merge error (remove a bogus #ifdef)
* [Revision #3afc9629fd](https://github.com/MariaDB/server/commit/3afc9629fd)\
  2017-11-14 12:22:30 -0800
  * Fixed bug [MDEV-13453](https://jira.mariadb.org/browse/MDEV-13453) Executing a query via CTE requires more permissions than the query itself
* [Revision #24184938ad](https://github.com/MariaDB/server/commit/24184938ad)\
  2017-11-14 13:36:50 +0400
  * [MDEV-11881](https://jira.mariadb.org/browse/MDEV-11881) Empty coordinates must be rejected in GeoJSON objects.
* [Revision #5632652804](https://github.com/MariaDB/server/commit/5632652804)\
  2017-11-13 14:59:43 +0000
  * update C/C
* [Revision #f48d56c459](https://github.com/MariaDB/server/commit/f48d56c459)\
  2017-11-09 16:25:16 +0000
  * [MDEV-14192](https://jira.mariadb.org/browse/MDEV-14192) Apply marko's patch
* [Revision #b2dd5232d4](https://github.com/MariaDB/server/commit/b2dd5232d4)\
  2017-11-13 04:32:56 +0200
  * InnoDB: Remove ut\_vsnprintf() and the use of my\_vsnprintf(); use vsnprintf()
* [Revision #c19ef508b8](https://github.com/MariaDB/server/commit/c19ef508b8)\
  2017-11-11 23:07:24 +0200
  * InnoDB: Remove ut\_snprintf() and the use of my\_snprintf(); use snprintf()
* [Revision #17bd6ed29a](https://github.com/MariaDB/server/commit/17bd6ed29a)\
  2017-11-11 22:48:19 +0200
  * Remove STATUS\_VERBOSE (there is no visible output)
* [Revision #1e2d4f677e](https://github.com/MariaDB/server/commit/1e2d4f677e)\
  2017-11-11 13:54:56 +0400
  * [MDEV-13971](https://jira.mariadb.org/browse/MDEV-13971) crash in skip\_num\_constant.
* [Revision #dcbf2823c7](https://github.com/MariaDB/server/commit/dcbf2823c7)\
  2017-11-10 13:58:00 -0800
  * Fixed [MDEV-13994](https://jira.mariadb.org/browse/MDEV-13994) Bad join results with orderby\_uses\_equalities=on.
* [Revision #589b0b3655](https://github.com/MariaDB/server/commit/589b0b3655)\
  2017-11-10 16:06:44 +0200
  * Allow innodb\_open\_files to be exceeded
* [Revision #fa00fedaac](https://github.com/MariaDB/server/commit/fa00fedaac)\
  2017-11-10 15:56:03 +0200
  * [MDEV-14100](https://jira.mariadb.org/browse/MDEV-14100) Assertion \`!is\_user\_rec || leaf || ...
* [Revision #9618c04e3f](https://github.com/MariaDB/server/commit/9618c04e3f)\
  2017-11-10 15:57:27 +0200
  * Follow-up fix of [MDEV-13795](https://jira.mariadb.org/browse/MDEV-13795)/[MDEV-14332](https://jira.mariadb.org/browse/MDEV-14332)
* [Revision #5d142f9958](https://github.com/MariaDB/server/commit/5d142f9958)\
  2017-11-09 23:01:44 +0200
  * [MDEV-13795](https://jira.mariadb.org/browse/MDEV-13795)/[MDEV-14332](https://jira.mariadb.org/browse/MDEV-14332) Corruption during online table-rebuilding ALTER when VIRTUAL columns exist
* [Revision #e2376e8137](https://github.com/MariaDB/server/commit/e2376e8137)\
  2017-11-09 19:45:28 +0300
  * [MDEV-14334](https://jira.mariadb.org/browse/MDEV-14334): Update test results for rocksdb.bulk\_load\_rev\_data
* [Revision #d40c23570f](https://github.com/MariaDB/server/commit/d40c23570f)\
  2017-11-09 14:57:40 +0200
  * Cleanup up after failed alter table in add\_index\_inplace\_crash
* Merge [Revision #761cf49265](https://github.com/MariaDB/server/commit/761cf49265) 2017-11-09 14:45:39 +0200 - Merge 10.1 into 10.2
* Merge [Revision #62333983e4](https://github.com/MariaDB/server/commit/62333983e4) 2017-11-09 15:41:26 +0400 - Merge remote-tracking branch 'origin/10.1' into 10.2
* Merge [Revision #7c85a8d936](https://github.com/MariaDB/server/commit/7c85a8d936) 2017-11-08 13:12:11 +0200 - Merge 10.1 into 10.2
* [Revision #e6ab6c4252](https://github.com/MariaDB/server/commit/e6ab6c4252)\
  2017-11-08 15:00:26 +0400
  * [MDEV-14320](https://jira.mariadb.org/browse/MDEV-14320) main.subselect failed in buildbot, results mismatch
* Merge [Revision #843e4508c0](https://github.com/MariaDB/server/commit/843e4508c0) 2017-11-07 23:02:39 +0200 - Merge 10.1 into 10.2
* [Revision #a4feb04ace](https://github.com/MariaDB/server/commit/a4feb04ace)\
  2017-11-07 15:34:04 +0200
  * [MDEV-14310](https://jira.mariadb.org/browse/MDEV-14310) ALTER TABLE…ADD INDEX may corrupt the InnoDB system tablespace
* [Revision #d04c4b3905](https://github.com/MariaDB/server/commit/d04c4b3905)\
  2017-11-07 10:57:36 +0200
  * [MDEV-14304](https://jira.mariadb.org/browse/MDEV-14304) Unnecessary conditions in buf\_page\_get\_gen()
* [Revision #fff7fc500b](https://github.com/MariaDB/server/commit/fff7fc500b)\
  2017-11-07 15:03:58 +0400
  * [MDEV-10817](https://jira.mariadb.org/browse/MDEV-10817) CAST(MAX(DATE'2001-01-01') AS TIME) returns a wrong result
* [Revision #8128ae48ef](https://github.com/MariaDB/server/commit/8128ae48ef)\
  2017-11-06 12:18:36 -0800
  * Test case for [MDEV-13753](https://jira.mariadb.org/browse/MDEV-13753) CTE is not visible during view creation
* [Revision #343bcb152f](https://github.com/MariaDB/server/commit/343bcb152f)\
  2017-11-05 22:52:41 -0800
  * Fixed [MDEV-14237](https://jira.mariadb.org/browse/MDEV-14237) Server crash on query with regexp\_substr
* [Revision #e0cd6f4b07](https://github.com/MariaDB/server/commit/e0cd6f4b07)\
  2017-11-05 18:45:12 -0800
  * Fixed bugs: [MDEV-13780](https://jira.mariadb.org/browse/MDEV-13780) CTE not found, [MDEV-14184](https://jira.mariadb.org/browse/MDEV-14184) recursive CTE not found
* Merge [Revision #8f2e8cf0cb](https://github.com/MariaDB/server/commit/8f2e8cf0cb) 2017-11-04 12:38:17 +0300 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mariarocks
* [Revision #beac522b55](https://github.com/MariaDB/server/commit/beac522b55)\
  2017-11-02 15:56:18 -0700
  * Fixed [MDEV-14093](https://jira.mariadb.org/browse/MDEV-14093) Wrong result upon JOIN with INDEX with no rows in joined table + GROUP BY + GROUP\_CONCAT + HAVING + ORDER BY \[by field from HAVING] + 1 row expected
* [Revision #b0cfb16867](https://github.com/MariaDB/server/commit/b0cfb16867)\
  2017-11-02 17:48:50 +0000
  * Fix a warning.
* [Revision #19733efa7b](https://github.com/MariaDB/server/commit/19733efa7b)\
  2017-11-02 16:18:41 +0200
  * [MDEV-14244](https://jira.mariadb.org/browse/MDEV-14244) [MariaDB 10.2.10](../../old-releases/10.2/10.2.10.md) fails to run on Debian Stretch with ext3 and O\_DIRECT
* [Revision #0f4e005541](https://github.com/MariaDB/server/commit/0f4e005541)\
  2017-11-02 15:40:27 +0200
  * Fixed compiler warning and warning from valgrind
* [Revision #6b7918d524](https://github.com/MariaDB/server/commit/6b7918d524)\
  2017-11-01 12:21:46 +0200
  * Fixed that --malloc-lib works properly
* Merge [Revision #6692b5f74a](https://github.com/MariaDB/server/commit/6692b5f74a) 2017-11-01 09:55:00 +0200 - Merge 10.1 into 10.2
* [Revision #c3b641ee20](https://github.com/MariaDB/server/commit/c3b641ee20)\
  2017-10-31 19:56:44 -0400
  * bump the VERSION
* [Revision #80d61515ac](https://github.com/MariaDB/server/commit/80d61515ac)\
  2017-11-02 19:11:01 +0300
  * Make rocksdb.read\_only\_tx pass and enable it
* [Revision #bd20fb87ec](https://github.com/MariaDB/server/commit/bd20fb87ec)\
  2017-10-31 13:44:25 +0200
  * Write error message ebfore aborting if not all memory is released
* [Revision #157f2b2551](https://github.com/MariaDB/server/commit/157f2b2551)\
  2017-10-31 13:42:57 +0200
  * Updated help message for long\_query\_time
* [Revision #b258080129](https://github.com/MariaDB/server/commit/b258080129)\
  2017-10-31 12:54:10 +0200
  * Disable known-failing tests
* [Revision #a0743734c4](https://github.com/MariaDB/server/commit/a0743734c4)\
  2017-10-30 09:45:38 +1100
  * travis: osx - xcode 8.3 -> 9.1
* [Revision #52c3afd4ca](https://github.com/MariaDB/server/commit/52c3afd4ca)\
  2017-10-30 18:57:44 +0200
  * Fix a type mismatch introduced by the merge commit e0a1c745ec3ed1ec6c0375a2a624697c29f480a6
* [Revision #b5689c6c87](https://github.com/MariaDB/server/commit/b5689c6c87)\
  2017-10-30 14:59:43 +0400
  * Compiler warnings fixed.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
