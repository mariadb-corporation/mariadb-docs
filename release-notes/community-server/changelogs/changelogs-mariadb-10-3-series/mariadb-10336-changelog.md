# MariaDB 10.3.36 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download 10.3.36](https://downloads.mariadb.org/mariadb/10.3.36/)[Release Notes](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10336-release-notes/)[Changelog](mariadb-10336-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 15 Aug 2022

For the highlights of this release, see the [release notes](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.44](../changelogs-mariadb-102-series/mariadb-10244-changelog.md)
* [Revision #faddcf3c39](https://github.com/MariaDB/server/commit/faddcf3c39)\
  2022-08-10 10:40:37 +0200
  * Do not check symbol returned (or not and so there is some garbadge) by mb\_wc() if mb\_wc() failed
* [Revision #122742897b](https://github.com/MariaDB/server/commit/122742897b)\
  2022-06-23 12:59:31 +0200
  * my\_safe\_process: try to kill the process softly first
* [Revision #9ecdf860ce](https://github.com/MariaDB/server/commit/9ecdf860ce)\
  2022-08-10 08:59:28 +0200
  * missing '
* [Revision #82c07fcabf](https://github.com/MariaDB/server/commit/82c07fcabf)\
  2022-08-09 14:24:53 +0200
  * [MDEV-23149](https://jira.mariadb.org/browse/MDEV-23149) Server crashes in my\_convert / ErrConvString::ptr / Item\_char\_typecast::check\_truncation\_with\_warn
* [Revision #47d0df6ef0](https://github.com/MariaDB/server/commit/47d0df6ef0)\
  2022-08-05 21:47:02 +0200
  * take into account C/C specific CR\_ERR\_NET\_WRITE error
* [Revision #9d4ed44cac](https://github.com/MariaDB/server/commit/9d4ed44cac)\
  2022-08-04 21:24:26 +0200
  * remove invalid options from warning messages
* [Revision #50a2a8bb43](https://github.com/MariaDB/server/commit/50a2a8bb43)\
  2022-08-02 18:29:58 -0500
  * Update docs INSTALL BINARY to mention mariadb tar file instead
* [Revision #f2830af16c](https://github.com/MariaDB/server/commit/f2830af16c)\
  2022-08-07 17:07:39 -0500
  * Fix typos in the codebase.
* [Revision #195833f1b6](https://github.com/MariaDB/server/commit/195833f1b6)\
  2022-07-28 15:29:53 +0800
  * refactor: remove redundant assignments
* [Revision #c0fe31c5dd](https://github.com/MariaDB/server/commit/c0fe31c5dd)\
  2022-08-08 14:00:21 +0200
  * fix of [MDEV-12325](https://jira.mariadb.org/browse/MDEV-12325) patch: symetric changes in sql\_yacc\_ora
* [Revision #4a53253cf9](https://github.com/MariaDB/server/commit/4a53253cf9)\
  2022-08-06 15:06:22 +0300
  * Fixed that sp-no-valgrind.test is disabled on valgrind builds (not runs)
* [Revision #a5a9fcdfe4](https://github.com/MariaDB/server/commit/a5a9fcdfe4)\
  2022-08-05 17:57:27 +0300
  * [MDEV-12325](https://jira.mariadb.org/browse/MDEV-12325) Unexpected data type and truncation when using CTE
* [Revision #43c7f6a0f3](https://github.com/MariaDB/server/commit/43c7f6a0f3)\
  2022-08-04 19:41:09 +1000
  * [MDEV-18702](https://jira.mariadb.org/browse/MDEV-18702): mysqldump: add variable 'max-statement-time' (mtr fix)
* [Revision #992b510b2f](https://github.com/MariaDB/server/commit/992b510b2f)\
  2022-08-04 10:01:24 +0200
  * Fix compile errors.
* [Revision #37a3d4467e](https://github.com/MariaDB/server/commit/37a3d4467e)\
  2022-08-03 17:55:45 +0300
  * [MDEV-23809](https://jira.mariadb.org/browse/MDEV-23809): Server crash in JOIN\_CACHE::free ...: part #2
* [Revision #2cd98c95de](https://github.com/MariaDB/server/commit/2cd98c95de)\
  2022-08-03 16:07:16 +0300
  * [MDEV-23809](https://jira.mariadb.org/browse/MDEV-23809): Server crash in JOIN\_CACHE::free or ...
* [Revision #f9ec9b6abb](https://github.com/MariaDB/server/commit/f9ec9b6abb)\
  2022-07-20 14:14:43 +0530
  * [MDEV-27282](https://jira.mariadb.org/browse/MDEV-27282) InnoDB: Failing assertion: !query->intersection
* [Revision #c2300d06f7](https://github.com/MariaDB/server/commit/c2300d06f7)\
  2022-08-01 20:52:10 -0700
  * [MDEV-28617](https://jira.mariadb.org/browse/MDEV-28617) Crash with INSERT...SELECT using derived table in GROUP BY clause
* [Revision #07a670b884](https://github.com/MariaDB/server/commit/07a670b884)\
  2022-08-02 11:42:20 +0200
  * [MDEV-23097](https://jira.mariadb.org/browse/MDEV-23097) heap-use-after-free in mysqlimport
* [Revision #92b0a367aa](https://github.com/MariaDB/server/commit/92b0a367aa)\
  2022-07-30 13:29:17 +1000
  * [MDEV-26447](https://jira.mariadb.org/browse/MDEV-26447): mysqldump to use temporary view instead of tables.
* [Revision #53c4e4d054](https://github.com/MariaDB/server/commit/53c4e4d054)\
  2022-07-29 16:07:42 +1000
  * [MDEV-18702](https://jira.mariadb.org/browse/MDEV-18702) mysqldump: add variable 'max-statement-time'
* Merge [Revision #5ac528a91f](https://github.com/MariaDB/server/commit/5ac528a91f) 2022-08-02 10:23:53 +0200 - Merge remote-tracking branch 'connect/10.3' into 10.3
* [Revision #e3163524ea](https://github.com/MariaDB/server/commit/e3163524ea)\
  2020-05-18 23:52:33 +0200\
  \*
  * Fix [MDEV-22571](https://jira.mariadb.org/browse/MDEV-22571) and [MDEV-22572](https://jira.mariadb.org/browse/MDEV-22572). Allow multiple ZIP table and enable using special column in them. modified: storage/connect/tabzip.cpp modified: storage/connect/tabzip.h
* [Revision #674197e2ff](https://github.com/MariaDB/server/commit/674197e2ff)\
  2020-03-14 18:08:15 +0100
  * Disable set warnings as errors for Windows
* [Revision #45b9fa4a8a](https://github.com/MariaDB/server/commit/45b9fa4a8a)\
  2020-03-12 23:25:18 +0100
  * Fix compile error in tabcmg.cpp
* [Revision #4a8b55330c](https://github.com/MariaDB/server/commit/4a8b55330c)\
  2020-03-12 19:36:54 +0100
  * Resolved ha\_connect.cc and CMakeLists.txt
* Merge [Revision #d26b4eb4c0](https://github.com/MariaDB/server/commit/d26b4eb4c0) 2020-03-12 19:16:36 +0100 - Pull new version from origin
* [Revision #4ba36cfa0c](https://github.com/MariaDB/server/commit/4ba36cfa0c)\
  2020-03-12 19:06:03 +0100\
  \*
  * Fix [60637429#60637429](https://stackoverflow.com/questions/60625778/import-complex-xml-from-multiple-files-in-mariadb/60637429#60637429) Import complex XML from multiple files in MariaDB Some row results are missing and replaced by the last file one. Thats because Nx and Sx column members are not reset when changing file. modified: storage/connect/tabxml.cpp modified: storage/connect/tabxml.h
* Merge [Revision #ce49812ec5](https://github.com/MariaDB/server/commit/ce49812ec5) 2019-11-24 18:19:33 +0100 - Commit conflict resolving after pulling from origin 10.3
* [Revision #afc21ab6d8](https://github.com/MariaDB/server/commit/afc21ab6d8)\
  2019-11-23 16:11:46 +0100
  * Commit some changes before pulling from origin CMakeLists.txt connect.cc
* [Revision #672cc34cf5](https://github.com/MariaDB/server/commit/672cc34cf5)\
  2019-08-22 23:24:27 +0200
  * Fix change in xml2 test result
* [Revision #7628fd3c6e](https://github.com/MariaDB/server/commit/7628fd3c6e)\
  2019-08-22 16:16:23 +0200
  * Include all changes made on 10.2
* [Revision #06b3715f26](https://github.com/MariaDB/server/commit/06b3715f26)\
  2019-06-28 11:53:58 +0200
  * Record some failing test results (dir,xml,xml2)
* [Revision #ec4795add6](https://github.com/MariaDB/server/commit/ec4795add6)\
  2019-06-27 17:54:28 +0200
  * In CONNECT version 1.6.10 NOSQL facility is enhanced by a new way to retrieve NOSQL data. In addition to files and Mongo collections, JSON as well as XML and CSV data can be retrieved from the net as answers from REST queries. Because it uses and external package (cpprestsdk) this is currently available only to MariaDB servers compiled from source.
* [Revision #66197aa0d5](https://github.com/MariaDB/server/commit/66197aa0d5)\
  2019-03-04 12:26:47 +0100
  * Typo
* [Revision #0a43be3929](https://github.com/MariaDB/server/commit/0a43be3929)\
  2019-03-04 12:18:35 +0100\
  \*
  * Fix [MDEV-18292](https://jira.mariadb.org/browse/MDEV-18292): CONNECT Engine JDBC not able to issue simple UPDATE statement from trigger or stored procedure Was not fixed when the same table was called several times with different modes. Fixed by checking if a new statement is compatible in the start\_stmt function. It nows do the same checks than external\_lock. modified: storage/connect/ha\_connect.cc modified: storage/connect/ha\_connect.h
* [Revision #990f8e8146](https://github.com/MariaDB/server/commit/990f8e8146)\
  2019-02-03 12:34:30 +0100\
  \*
  * Fix [MDEV-13136](https://jira.mariadb.org/browse/MDEV-13136): enhance CREATE SERVER MyServerName FOREIGN DATA WRAPPER to work with CONNECT engine modified: storage/connect/tabjdbc.cpp
* [Revision #0f388dd4d0](https://github.com/MariaDB/server/commit/0f388dd4d0)\
  2019-01-27 15:10:03 +0100\
  \*
  * Enable CONNECT tables to have triggers Update version number modified: storage/connect/ha\_connect.cc
* [Revision #27fec12fae](https://github.com/MariaDB/server/commit/27fec12fae)\
  2019-01-26 18:11:45 +0100\
  \*
  * Make user and password defined in CREATE TABLE have precedence on the ones specified in a Federated Server. modified: storage/connect/tabjdbc.cpp
* [Revision #a4834755ec](https://github.com/MariaDB/server/commit/a4834755ec)\
  2019-01-24 23:49:57 +0100\
  \*
  * Fix [MDEV-18192](https://jira.mariadb.org/browse/MDEV-18192): CONNECT Engine JDBC not able to issue simple UPDATE statement from trigger or stored procedure modified: storage/connect/tabext.cpp modified: storage/connect/tabext.h modified: storage/connect/tabjdbc.cpp
* [Revision #547ce1b22a](https://github.com/MariaDB/server/commit/547ce1b22a)\
  2019-01-02 10:44:03 +0100\
  \*
  * Fix a few bug mainly concerning discovery and call from OEM (and prepare new table types)
* [Revision #c2482c76dc](https://github.com/MariaDB/server/commit/c2482c76dc)\
  2018-12-05 19:01:37 +0100
  * Modified because different result on Windows and Linux
* [Revision #60525ad348](https://github.com/MariaDB/server/commit/60525ad348)\
  2018-12-05 16:36:25 +0100
  * Modified to avoid make index error (AVG\_ROW\_LENGTH=5)
* [Revision #4a572631aa](https://github.com/MariaDB/server/commit/4a572631aa)\
  2018-12-04 23:26:47 +0100\
  \*
  * Make PlugSubAlloc to be exportable Suppress unused parameter from PlugSubSet modified: storage/connect/global.h modified: storage/connect/plugutil.cpp modified: storage/connect/jsonudf.cpp modified: storage/connect/tabjson.cpp modified: storage/connect/user\_connect.cc
* [Revision #28000d8141](https://github.com/MariaDB/server/commit/28000d8141)\
  2018-10-14 19:39:21 +0200
  * Restore mysql\_exec.result
* [Revision #ad09ea0df0](https://github.com/MariaDB/server/commit/ad09ea0df0)\
  2018-10-14 17:56:02 +0200\
  \*
  * Implement the CHECK TABLE statement and accept REPAIR and ANALYZE modified: storage/connect/connect.cc modified: storage/connect/ha\_connect.cc modified: storage/connect/ha\_connect.h modified: storage/connect/tabjdbc.cpp modified: storage/connect/tabmysql.cpp modified: storage/connect/tabodbc.cpp
* [Revision #15194de2c2](https://github.com/MariaDB/server/commit/15194de2c2)\
  2018-08-08 12:10:30 +0200\
  \*
  * Fix [MDEV-16672](https://jira.mariadb.org/browse/MDEV-16672) Connect: Warnings with 10.0 filamtxt.cpp: DOSFAM::RenameTempFile: Change sprintf to snprintf. filamvct.cpp: VECFAM::RenameTempFile: Change sprintf to snprintf. javaconn.cpp: Add JAVAConn::GetUTFString function. Use it instead of env->GetStringUTFChars. Fix wrong identation. javaconn.h: Add GetUTFString declaration. jdbconn.cpp: Use GetUTFString function instead of env->GetStringUTFChars. jmgoconn.cpp: Use GetUTFString function instead of env->GetStringUTFChars. Fix wrong identation. jsonudf.cpp: change 139 to BMX line 4631. tabjmg.cpp: Add ReleaseStringUTF. Fix wrong identation. tabpivot.cpp: Fix wrong identation. tabutil.cpp: TDBPRX::GetSubTable: Change sprintf to snprintf. modified: storage/connect/filamtxt.cpp modified: storage/connect/filamvct.cpp modified: storage/connect/javaconn.cpp modified: storage/connect/javaconn.h modified: storage/connect/jdbconn.cpp modified: storage/connect/jmgoconn.cpp modified: storage/connect/jsonudf.cpp modified: storage/connect/tabjmg.cpp modified: storage/connect/tabpivot.cpp modified: storage/connect/tabutil.cpp
* [Revision #c0fd3be272](https://github.com/MariaDB/server/commit/c0fd3be272)\
  2018-06-28 23:33:02 +0200\
  \*
  * Fix [MDEV-16167](https://jira.mariadb.org/browse/MDEV-16167) Cannot insert unsigned values into a VEC table modified: storage/connect/filamvct.cpp modified: storage/connect/tabvct.cpp
* [Revision #fa7bbe5a73](https://github.com/MariaDB/server/commit/fa7bbe5a73)\
  2018-05-07 00:56:45 +0200\
  \*
  * Fix [MDEV-15735](https://jira.mariadb.org/browse/MDEV-15735) CONNECT \[filamtxt.cpp:429]: Suspicious condition modified: storage/connect/filamtxt.cpp
* [Revision #182a6383cd](https://github.com/MariaDB/server/commit/182a6383cd)\
  2022-08-01 22:00:05 +1000
  * [MDEV-16605](https://jira.mariadb.org/browse/MDEV-16605) Always include buf\_madvise\_do\_dump in binaries
* [Revision #7fb1f919d0](https://github.com/MariaDB/server/commit/7fb1f919d0)\
  2022-07-19 13:26:19 +0200
  * [MDEV-28758](https://jira.mariadb.org/browse/MDEV-28758): mariadb-backup copies binary logs to backup directory
* [Revision #5b4154373a](https://github.com/MariaDB/server/commit/5b4154373a)\
  2022-06-28 09:42:45 +0200
  * only copy buffer pool dump in SST galera mode
* [Revision #5197519f4f](https://github.com/MariaDB/server/commit/5197519f4f)\
  2022-06-28 09:16:31 +0200
  * revert mariadb-backup part of [MDEV-27524](https://jira.mariadb.org/browse/MDEV-27524), fix the test
* [Revision #6a3fbfdb2d](https://github.com/MariaDB/server/commit/6a3fbfdb2d)\
  2022-08-01 15:15:06 +0300
  * [MDEV-14804](https://jira.mariadb.org/browse/MDEV-14804) innodb.update\_time occasionally fails
* [Revision #40c2460d8c](https://github.com/MariaDB/server/commit/40c2460d8c)\
  2022-08-01 11:11:26 +0200
  * in INFORMATION\_SCHEMA.ALL\_PLUGINS match installed plugins better
* [Revision #8ea529ecba](https://github.com/MariaDB/server/commit/8ea529ecba)\
  2022-07-29 21:57:06 +0200
  * [MDEV-29131](https://jira.mariadb.org/browse/MDEV-29131) Assertion \`status == 0' failed when renaming user after deleting table roles\_mapping
* [Revision #6c7e3e5c13](https://github.com/MariaDB/server/commit/6c7e3e5c13)\
  2022-07-29 10:24:45 +0200
  * bugfix: RAND is VCOL\_SESSION\_FUNC
* [Revision #25219920f5](https://github.com/MariaDB/server/commit/25219920f5)\
  2022-07-29 15:41:43 +0530
  * [MDEV-28762](https://jira.mariadb.org/browse/MDEV-28762): recursive call of some json functions without stack control
* [Revision #f9315b3321](https://github.com/MariaDB/server/commit/f9315b3321)\
  2022-07-29 07:40:00 +0200
  * CC 3.1 update
* [Revision #cbcc0101ee](https://github.com/MariaDB/server/commit/cbcc0101ee)\
  2022-07-28 16:17:03 +0200
  * [MDEV-29188](https://jira.mariadb.org/browse/MDEV-29188) Crash in JSON\_EXTRACT
* [Revision #4b77d38c26](https://github.com/MariaDB/server/commit/4b77d38c26)\
  2022-07-28 08:51:19 +0300
  * Fix GCC -Og -Wmaybe-uninitialized
* [Revision #15a2ff1231](https://github.com/MariaDB/server/commit/15a2ff1231)\
  2021-10-20 11:37:14 +0200
  * [MDEV-26647](https://jira.mariadb.org/browse/MDEV-26647) (simple\_password\_check) Include password validation plugin information in the error message if the SQL statement is not satisfied password policy
* [Revision #cc6bba008d](https://github.com/MariaDB/server/commit/cc6bba008d)\
  2021-10-20 10:21:00 +0200
  * [MDEV-26647](https://jira.mariadb.org/browse/MDEV-26647) (plugin name) Include password validation plugin information in the error message if the SQL statement is not satisfied password policy
* [Revision #0ee1082bd2](https://github.com/MariaDB/server/commit/0ee1082bd2)\
  2022-07-27 14:15:14 +0300
  * [MDEV-28495](https://jira.mariadb.org/browse/MDEV-28495) InnoDB corruption due to lack of file locking
* [Revision #bd935a4106](https://github.com/MariaDB/server/commit/bd935a4106)\
  2022-07-21 15:20:53 -0700
  * [MDEV-29139](https://jira.mariadb.org/browse/MDEV-29139) Crash when using ANY predicand with redundant subquery in GROUP BY clause
* [Revision #e8eb6d9c93](https://github.com/MariaDB/server/commit/e8eb6d9c93)\
  2022-07-26 16:21:15 +0200
  * zlib: remove redundant and generated files
* [Revision #bc4098582b](https://github.com/MariaDB/server/commit/bc4098582b)\
  2022-07-18 13:38:27 +0200
  * [MDEV-29074](https://jira.mariadb.org/browse/MDEV-29074) GET\_BIT variables crash in SET STATEMENT
* [Revision #0ee5cf837e](https://github.com/MariaDB/server/commit/0ee5cf837e)\
  2022-07-12 09:48:59 +0200
  * disks plugin: check for build prerequisites properly
* [Revision #15a68fc255](https://github.com/MariaDB/server/commit/15a68fc255)\
  2022-07-20 16:05:33 +0530
  * [MDEV-29058](https://jira.mariadb.org/browse/MDEV-29058) Assertion \`index->type == 32' failed in dict\_index\_build\_internal\_fts
* [Revision #f076dc2f66](https://github.com/MariaDB/server/commit/f076dc2f66)\
  2022-07-05 18:21:21 +0530
  * [MDEV-20797](https://jira.mariadb.org/browse/MDEV-20797) FULLTEXT search with apostrophe, and mandatory words
* [Revision #a8a27f1edf](https://github.com/MariaDB/server/commit/a8a27f1edf)\
  2022-07-26 11:03:53 +0300
  * Correct a bogus comment.
* [Revision #3bf10012e0](https://github.com/MariaDB/server/commit/3bf10012e0)\
  2022-07-26 11:00:11 +0300
  * [MDEV-28762](https://jira.mariadb.org/browse/MDEV-28762): Fixup for clang
* [Revision #19af1890b5](https://github.com/MariaDB/server/commit/19af1890b5)\
  2022-07-19 19:06:55 +0000
  * Use memory safe snprintf() in Connect Engine
* [Revision #95eb5e5a12](https://github.com/MariaDB/server/commit/95eb5e5a12)\
  2022-07-26 08:18:36 +0300
  * Fix clang -Wunused-but-set-variable in unit tests
* [Revision #5d0f75349f](https://github.com/MariaDB/server/commit/5d0f75349f)\
  2022-07-26 08:08:48 +0300
  * [MDEV-28980](https://jira.mariadb.org/browse/MDEV-28980): Disable the test for --embedded
* [Revision #555c12a541](https://github.com/MariaDB/server/commit/555c12a541)\
  2019-12-17 15:23:55 +0530
  * [MDEV-21087](https://jira.mariadb.org/browse/MDEV-21087)/[MDEV-21433](https://jira.mariadb.org/browse/MDEV-21433): ER\_SLAVE\_INCIDENT arrives at slave without failure specifics
* [Revision #46ff660883](https://github.com/MariaDB/server/commit/46ff660883)\
  2022-07-25 14:34:44 +0530
  * This commit is a fixup for [MDEV-28762](https://jira.mariadb.org/browse/MDEV-28762)
* [Revision #f1c8749f46](https://github.com/MariaDB/server/commit/f1c8749f46)\
  2022-07-25 15:58:16 +0300
  * Fix DBUG\_ENTER/return mismatch
* [Revision #8aa37c264f](https://github.com/MariaDB/server/commit/8aa37c264f)\
  2022-07-25 10:28:45 +0300
  * [MDEV-28980](https://jira.mariadb.org/browse/MDEV-28980) InnoDB: Failing assertion: len <= MAX\_TABLE\_NAME\_LEN
* [Revision #e55c3dc33f](https://github.com/MariaDB/server/commit/e55c3dc33f)\
  2022-07-25 00:31:33 -0400
  * Fix building Connect storage engine ioapi code on OpenBSD / NetBSD / DragonFly
* [Revision #95989e8211](https://github.com/MariaDB/server/commit/95989e8211)\
  2022-07-23 19:56:08 +0530
  * [MDEV-28762](https://jira.mariadb.org/browse/MDEV-28762): recursive call of some json functions without stack control
* Merge [Revision #4bc34ef36f](https://github.com/MariaDB/server/commit/4bc34ef36f) 2022-07-22 21:08:55 +0200 - Merge branch 'merge-zlib' into 10.3
* [Revision #8b6739e4e3](https://github.com/MariaDB/server/commit/8b6739e4e3)\
  2022-07-22 08:32:45 +0200
  * 1.2.12
* [Revision #3fb50da076](https://github.com/MariaDB/server/commit/3fb50da076)\
  2022-07-21 15:27:25 +0200
  * 1.2.11
* [Revision #7b0e68b8a2](https://github.com/MariaDB/server/commit/7b0e68b8a2)\
  2022-07-22 17:43:40 +0800
  * fix DBUG\_ENTER awake\_no\_mutex
* [Revision #dbe39f14fe](https://github.com/MariaDB/server/commit/dbe39f14fe)\
  2022-06-21 14:58:34 +0530
  * [MDEV-28762](https://jira.mariadb.org/browse/MDEV-28762): recursive call of some json functions without stack control
* [Revision #1848804840](https://github.com/MariaDB/server/commit/1848804840)\
  2022-07-18 23:16:18 +0300
  * [MDEV-29023](https://jira.mariadb.org/browse/MDEV-29023) MTR hangs after multiple failures
* [Revision #7ca5c7d8f9](https://github.com/MariaDB/server/commit/7ca5c7d8f9)\
  2022-07-18 23:16:18 +0300
  * [MDEV-29023](https://jira.mariadb.org/browse/MDEV-29023) waitpid() cleanup
* [Revision #1d307ed48a](https://github.com/MariaDB/server/commit/1d307ed48a)\
  2022-07-18 23:16:18 +0300
  * [MDEV-29025](https://jira.mariadb.org/browse/MDEV-29025) MTR doesn't print stack trace for bootstrap crashes
* [Revision #1bdcffb028](https://github.com/MariaDB/server/commit/1bdcffb028)\
  2022-07-18 23:16:17 +0300
  * [MDEV-29025](https://jira.mariadb.org/browse/MDEV-29025) Refactoring: moved out core\_wanted() out of mysql-test-run.pl
* [Revision #e9be5428a2](https://github.com/MariaDB/server/commit/e9be5428a2)\
  2022-07-18 23:16:17 +0300
  * [MDEV-28931](https://jira.mariadb.org/browse/MDEV-28931) MTR prints detailed stack trace unconditionally
* [Revision #220fb6797b](https://github.com/MariaDB/server/commit/220fb6797b)\
  2022-07-18 23:16:17 +0300
  * [MDEV-28931](https://jira.mariadb.org/browse/MDEV-28931) Debugger.pm readability fix
* [Revision #ce7820eb83](https://github.com/MariaDB/server/commit/ce7820eb83)\
  2022-07-18 23:16:17 +0300
  * [MDEV-28931](https://jira.mariadb.org/browse/MDEV-28931) --verbose option is too verbose
* [Revision #83f7d25c44](https://github.com/MariaDB/server/commit/83f7d25c44)\
  2022-07-18 23:16:17 +0300
  * [MDEV-28931](https://jira.mariadb.org/browse/MDEV-28931) Cleanup: try GDB to print core first
* [Revision #990ddaba1e](https://github.com/MariaDB/server/commit/990ddaba1e)\
  2022-07-18 14:09:29 +0200
  * Windows - reduce irrelevant CMake system checks
* [Revision #b3f0acf510](https://github.com/MariaDB/server/commit/b3f0acf510)\
  2022-07-17 15:14:52 +0200
  * [MDEV-27686](https://jira.mariadb.org/browse/MDEV-27686) Moving libexecinfo out of FreeBSD / OpenBSD specific CMake code
* [Revision #92a3280998](https://github.com/MariaDB/server/commit/92a3280998)\
  2022-07-12 09:25:08 +0200
  * table\_count was present twice in one class of LEX.
* [Revision #49e14000ee](https://github.com/MariaDB/server/commit/49e14000ee)\
  2022-06-18 20:54:39 +0700
  * [MDEV-26427](https://jira.mariadb.org/browse/MDEV-26427) MariaDB Server SEGV on INSERT .. SELECT
* [Revision #02e85aeafd](https://github.com/MariaDB/server/commit/02e85aeafd)\
  2022-07-05 07:12:49 -0600
  * [MDEV-28487](https://jira.mariadb.org/browse/MDEV-28487): sequences not respect value of binlog\_row\_image with select nextval(seq\_gen)
* [Revision #96be3fe841](https://github.com/MariaDB/server/commit/96be3fe841)\
  2022-07-11 12:32:52 +0200
  * [MDEV-21445](https://jira.mariadb.org/browse/MDEV-21445) update test results
* [Revision #b817afaa1c](https://github.com/MariaDB/server/commit/b817afaa1c)\
  2022-07-11 21:00:18 +0300
  * [MDEV-28689](https://jira.mariadb.org/browse/MDEV-28689), [MDEV-28690](https://jira.mariadb.org/browse/MDEV-28690): Remove ctrl\_mutex
* [Revision #4f62dfe676](https://github.com/MariaDB/server/commit/4f62dfe676)\
  2022-07-11 15:00:34 +0200
  * Revert "[MDEV-28689](https://jira.mariadb.org/browse/MDEV-28689), [MDEV-28690](https://jira.mariadb.org/browse/MDEV-28690): Incorrect error handling for ctrl\_mutex"
* [Revision #7598ef4b26](https://github.com/MariaDB/server/commit/7598ef4b26)\
  2022-07-10 19:28:06 +0200
  * [MDEV-28197](https://jira.mariadb.org/browse/MDEV-28197) Linux mariadb-client build does not accept Unicode characters
* [Revision #0e9a255ec8](https://github.com/MariaDB/server/commit/0e9a255ec8)\
  2022-07-07 22:15:42 +0300
  * [MDEV-28871](https://jira.mariadb.org/browse/MDEV-28871): Assert ... failed in JOIN::dbug\_verify\_sj\_inner\_tables...
* [Revision #66c06735a2](https://github.com/MariaDB/server/commit/66c06735a2)\
  2022-07-07 15:14:14 +0200
  * [MDEV-28746](https://jira.mariadb.org/browse/MDEV-28746) Wrong error code ER\_BAD\_DB\_ERROR for long filenames
* [Revision #d6e80c21d6](https://github.com/MariaDB/server/commit/d6e80c21d6)\
  2022-07-06 16:36:36 +0400
  * [MDEV-25492](https://jira.mariadb.org/browse/MDEV-25492) BETWEEN clause returns incorrect results on quoted 64-bit ints
* [Revision #57f5c319af](https://github.com/MariaDB/server/commit/57f5c319af)\
  2022-07-06 15:42:21 +0400
  * [MDEV-21445](https://jira.mariadb.org/browse/MDEV-21445) Strange/inconsistent behavior of IN condition when mixing numbers and strings
* [Revision #bdc1134dea](https://github.com/MariaDB/server/commit/bdc1134dea)\
  2022-07-06 10:28:06 +0400
  * [MDEV-29041](https://jira.mariadb.org/browse/MDEV-29041) Redundant truncation warning on CAST(string\_column AS DECIMAL)
* [Revision #6313702278](https://github.com/MariaDB/server/commit/6313702278)\
  2022-07-04 20:00:25 +0200
  * [MDEV-26568](https://jira.mariadb.org/browse/MDEV-26568) RPM logic prohibiting server major upgrade no longer works as expected
* [Revision #2f3f1cd05b](https://github.com/MariaDB/server/commit/2f3f1cd05b)\
  2021-10-13 22:45:26 +0900
  * [MDEV-26544](https://jira.mariadb.org/browse/MDEV-26544) Assertion \`part\_share->auto\_inc\_initialized' failed in ha\_partition::get\_auto\_increment on INSERT
* [Revision #4bc7c03b5f](https://github.com/MariaDB/server/commit/4bc7c03b5f)\
  2022-07-04 16:49:45 +0900
  * [MDEV-29011](https://jira.mariadb.org/browse/MDEV-29011) Server crash in spider\_db\_open\_item\_cond with XOR operator
* [Revision #8c8bd4bebf](https://github.com/MariaDB/server/commit/8c8bd4bebf)\
  2022-07-04 19:24:58 +0200
  * Fix typo in appveyor.yml
* [Revision #990cde800a](https://github.com/MariaDB/server/commit/990cde800a)\
  2022-07-01 14:00:57 +0530
  * [MDEV-28912](https://jira.mariadb.org/browse/MDEV-28912) NON-UNIQUE FTS\_DOC\_ID index mistaken as FTS\_DOC\_ID\_INDEX
* [Revision #7c35ad16e3](https://github.com/MariaDB/server/commit/7c35ad16e3)\
  2022-07-01 13:02:43 +0300
  * [MDEV-28389](https://jira.mariadb.org/browse/MDEV-28389) fixup: Fix pre-GCC 10 -Wconversion
* [Revision #045771c050](https://github.com/MariaDB/server/commit/045771c050)\
  2022-07-01 09:48:36 +0300
  * Fix most clang-15 -Wunused-but-set-variable
* [Revision #6dc1bc3a58](https://github.com/MariaDB/server/commit/6dc1bc3a58)\
  2022-07-01 09:34:31 +0300
  * Fix clang-15 -Wdeprecated-non-prototype
* [Revision #e34f878139](https://github.com/MariaDB/server/commit/e34f878139)\
  2022-06-07 18:24:02 +0530
  * [MDEV-28706](https://jira.mariadb.org/browse/MDEV-28706) Redundant InnoDB table fails during alter
* [Revision #efdbb3cf31](https://github.com/MariaDB/server/commit/efdbb3cf31)\
  2022-06-28 11:38:27 +0400
  * A cleanup for [MDEV-25243](https://jira.mariadb.org/browse/MDEV-25243) ASAN heap-use-after-free in Item\_func\_sp::execute\_impl upon concurrent view DDL and I\_S query with view and function
* [Revision #5375f0b495](https://github.com/MariaDB/server/commit/5375f0b495)\
  2022-06-22 00:56:16 +0900
  * [MDEV-21310](https://jira.mariadb.org/browse/MDEV-21310) AUTO\_INCREMENT column throws range error on INSERT in partitioned table | Assertion \`part\_share->auto\_inc\_initialized || !can\_use\_for\_auto\_inc\_init()' failed.
* [Revision #f339ef3f97](https://github.com/MariaDB/server/commit/f339ef3f97)\
  2022-06-27 16:00:34 +0300
  * [MDEV-26577](https://jira.mariadb.org/browse/MDEV-26577) InnoDB: Failing assertion: dict\_tf2\_is\_valid(flags, flags2) during ADD COLUMN
* [Revision #a75ad73545](https://github.com/MariaDB/server/commit/a75ad73545)\
  2022-06-27 14:50:00 +0300
  * [MDEV-28389](https://jira.mariadb.org/browse/MDEV-28389) fixup: Fix compiler warnings
* [Revision #c86b1389de](https://github.com/MariaDB/server/commit/c86b1389de)\
  2022-06-27 09:49:49 +0300
  * [MDEV-28389](https://jira.mariadb.org/browse/MDEV-28389): Simplify the InnoDB corrupted page output
* [Revision #2c1aaa6664](https://github.com/MariaDB/server/commit/2c1aaa6664)\
  2022-06-27 14:58:18 +0900
  * [MDEV-28854](https://jira.mariadb.org/browse/MDEV-28854) Disallow INSERT DELAYED on Spider table
* [Revision #5feb60ce18](https://github.com/MariaDB/server/commit/5feb60ce18)\
  2022-06-23 14:48:29 +0200
  * [MDEV-22590](https://jira.mariadb.org/browse/MDEV-22590) SIGSEGV in flush\_all\_key\_blocks when changing key\_buffer\_size / ASAN: heap-use-after-free in flush\_all\_key\_blocks
* [Revision #3e09c6199d](https://github.com/MariaDB/server/commit/3e09c6199d)\
  2022-06-21 13:29:45 +0200
  * [MDEV-26562](https://jira.mariadb.org/browse/MDEV-26562): galera-sst-mariadb-backup is failing due to missing xtrabackup\_checkpoints
* [Revision #d4539426bc](https://github.com/MariaDB/server/commit/d4539426bc)\
  2022-06-18 17:42:29 +0300
  * [MDEV-28884](https://jira.mariadb.org/browse/MDEV-28884): include kernel information in crashing signal handler
* [Revision #f299351e1c](https://github.com/MariaDB/server/commit/f299351e1c)\
  2022-06-18 15:10:34 +0200
  * remove invalid test
* [Revision #be99d0ddb6](https://github.com/MariaDB/server/commit/be99d0ddb6)\
  2022-06-17 08:40:51 +0300
  * Fix intermittent failures of innodb.stats\_persistent
* [Revision #c4f65d8fed](https://github.com/MariaDB/server/commit/c4f65d8fed)\
  2022-06-16 13:28:24 +0900
  * [MDEV-21027](https://jira.mariadb.org/browse/MDEV-21027) Assertion \`part\_share->auto\_inc\_initialized || !can\_use\_for\_auto\_inc\_init()' failed in ha\_partition::set\_auto\_increment\_if\_higher
* [Revision #f31e935c3e](https://github.com/MariaDB/server/commit/f31e935c3e)\
  2022-06-15 14:53:51 +0200
  * mtr: fix a race condition
* [Revision #2e7e89d6c9](https://github.com/MariaDB/server/commit/2e7e89d6c9)\
  2022-06-08 15:20:36 +0200
  * cleanup: move the check out of the loop
* [Revision #124326d810](https://github.com/MariaDB/server/commit/124326d810)\
  2022-06-08 15:36:28 +0200
  * [MDEV-28656](https://jira.mariadb.org/browse/MDEV-28656): Inability to roll upgrade without stopping the Galera cluster
* [Revision #c168e16782](https://github.com/MariaDB/server/commit/c168e16782)\
  2022-05-23 10:39:31 +0300
  * [MDEV-28628](https://jira.mariadb.org/browse/MDEV-28628): Change current Debian package revision scheme
* [Revision #e077ce2a68](https://github.com/MariaDB/server/commit/e077ce2a68)\
  2021-10-29 19:04:53 +0900
  * [MDEV-26127](https://jira.mariadb.org/browse/MDEV-26127) Assertion \`err != DB\_DUPLICATE\_KEY' failed or InnoDB: Failing assertion: id != 0 on ALTER ... REBUILD PARTITION
* [Revision #b59bc629c8](https://github.com/MariaDB/server/commit/b59bc629c8)\
  2022-02-08 08:57:24 +1100
  * [MDEV-27766](https://jira.mariadb.org/browse/MDEV-27766): connect engine; INSERT ignore option, was ignored
* [Revision #ace2e0301e](https://github.com/MariaDB/server/commit/ace2e0301e)\
  2022-06-09 10:43:44 +0300
  * [MDEV-28666](https://jira.mariadb.org/browse/MDEV-28666): Add correct 'Breaks' to make sure upgrade from 10.2 succeeds
* [Revision #98293130c3](https://github.com/MariaDB/server/commit/98293130c3)\
  2022-06-09 10:57:28 +0300
  * [MDEV-28779](https://jira.mariadb.org/browse/MDEV-28779): ALTER TABLE IMPORT TABLESPACE corrupts an encrypted table
* [Revision #2cd1edfc21](https://github.com/MariaDB/server/commit/2cd1edfc21)\
  2022-06-09 13:20:37 +1000
  * [MDEV-25577](https://jira.mariadb.org/browse/MDEV-25577) mariadb-tzinfo-to-sql generates superfluous warnings
* [Revision #9c207c88c1](https://github.com/MariaDB/server/commit/9c207c88c1)\
  2022-06-03 15:08:46 +0800
  * mysql.server.sh fix for non-Red Hat platforms
* [Revision #44ab6cba76](https://github.com/MariaDB/server/commit/44ab6cba76)\
  2022-06-08 14:23:21 +0300
  * Cleanup: Remove unused error code DB\_FORCED\_ABORT
* [Revision #960f0344a2](https://github.com/MariaDB/server/commit/960f0344a2)\
  2022-06-07 22:33:37 +0900
  * [MDEV-25273](https://jira.mariadb.org/browse/MDEV-25273): fix typo (s/strucures/structures/)
* [Revision #37ea077873](https://github.com/MariaDB/server/commit/37ea077873)\
  2022-06-07 15:49:41 +0200
  * main.help: flush help tables after modifying them
* [Revision #7c4efab903](https://github.com/MariaDB/server/commit/7c4efab903)\`\
  2022-05-19 13:58:31 +0200
  * typo fixed: [space](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/space) -> [:](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/space)
* [Revision #19c721631e](https://github.com/MariaDB/server/commit/19c721631e)\
  2022-06-06 22:21:22 +0300
  * [MDEV-28749](https://jira.mariadb.org/browse/MDEV-28749): restore\_prev\_nj\_state() doesn't update cur\_sj\_inner\_tables correctly
* [Revision #392e744aec](https://github.com/MariaDB/server/commit/392e744aec)\
  2022-05-04 17:30:21 +0300
  * Fixed crashing when using DBUG\_PUSH\_EMPTY
* [Revision #099b9202a5](https://github.com/MariaDB/server/commit/099b9202a5)\
  2022-06-03 10:47:34 +0300
  * [MDEV-27697](https://jira.mariadb.org/browse/MDEV-27697) fixup: Exclude debug code from non-debug builds
* [Revision #91d5fffa07](https://github.com/MariaDB/server/commit/91d5fffa07)\
  2022-06-01 11:20:47 +0300
  * [MDEV-28719](https://jira.mariadb.org/browse/MDEV-28719): compress\_write() leaks data\_mutex on error
* [Revision #fde99e006d](https://github.com/MariaDB/server/commit/fde99e006d)\
  2022-06-01 11:13:15 +0300
  * [MDEV-28716](https://jira.mariadb.org/browse/MDEV-28716): Portability: unlink() can return EPERM instead of EISDIR
* [Revision #9d10b7107c](https://github.com/MariaDB/server/commit/9d10b7107c)\
  2022-05-30 13:07:21 +0300
  * Fixed bug in ma\_loghandler.cc that could cause an assert
* [Revision #131c318b16](https://github.com/MariaDB/server/commit/131c318b16)\
  2022-05-30 13:04:14 +0300
  * Remove compiler warning about unused variables
* [Revision #863c3eda87](https://github.com/MariaDB/server/commit/863c3eda87)\
  2022-05-30 15:49:45 +0300
  * [MDEV-28689](https://jira.mariadb.org/browse/MDEV-28689), [MDEV-28690](https://jira.mariadb.org/browse/MDEV-28690): Incorrect error handling for ctrl\_mutex
* [Revision #f7137a619f](https://github.com/MariaDB/server/commit/f7137a619f)\
  2022-05-30 19:28:44 +0900
  * [MDEV-28599](https://jira.mariadb.org/browse/MDEV-28599) EXCHANGE PARTITION on view causes ER\_CHECK\_NO\_SUCH\_TABLE instead of ER\_WRONG\_OBJECT
* [Revision #c4e87cb22c](https://github.com/MariaDB/server/commit/c4e87cb22c)\
  2022-02-03 17:39:29 +1100
  * [MDEV-9020](https://jira.mariadb.org/browse/MDEV-9020): Connect issues ALTER TABLE DISABLE KEYS when inserting data
* [Revision #31e30329a3](https://github.com/MariaDB/server/commit/31e30329a3)\
  2022-05-03 17:25:48 +0000
  * Add option --enable-cleartext-plugin to the MariaDB client
* [Revision #f85d488ad2](https://github.com/MariaDB/server/commit/f85d488ad2)\
  2022-05-24 20:02:54 +0800
  * remove obsolete fix\_session\_vcol\_expr{,\_for\_read} function declarations
* [Revision #7fe474fe7e](https://github.com/MariaDB/server/commit/7fe474fe7e)\
  2022-05-12 17:10:58 +0530
  * [MDEV-25257](https://jira.mariadb.org/browse/MDEV-25257) SEGV in fts\_get\_next\_doc\_id upon some INSERT
* [Revision #7d3d3838c1](https://github.com/MariaDB/server/commit/7d3d3838c1)\
  2022-05-23 13:11:14 +0200
  * [MDEV-28583](https://jira.mariadb.org/browse/MDEV-28583): post-merge fixes
* Merge [Revision #7d5d9ead2b](https://github.com/MariaDB/server/commit/7d5d9ead2b) 2022-05-20 17:48:18 +0200 - Merge branch '10.3' into bb-10.3-release
* [Revision #68f0a5d008](https://github.com/MariaDB/server/commit/68f0a5d008)\
  2022-05-20 11:14:30 -0400
  * bump the VERSION
* [Revision #40d9dbb28f](https://github.com/MariaDB/server/commit/40d9dbb28f)\
  2022-05-13 18:10:11 +0400
  * [MDEV-28246](https://jira.mariadb.org/browse/MDEV-28246) Optimizer uses all partitions after upgrade to 10.3
* [Revision #8881c0100e](https://github.com/MariaDB/server/commit/8881c0100e)\
  2022-05-18 23:38:56 +0900
  * [MDEV-14642](https://jira.mariadb.org/browse/MDEV-14642) Assertion 'table->s->db\_create\_options == part\_table->s->db\_create\_options' failed in compare\_table\_with\_partition

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
