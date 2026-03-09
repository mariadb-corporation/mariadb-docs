# MariaDB 10.1.41 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.41/)[Release Notes](../../old-releases/10.1/10.1.41.md)[Changelog](mariadb-10141-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 31 Jul 2019

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.41.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 5.5.65](../changelogs-mariadb-55-series/mariadb-5565-changelog.md)
* [Revision #403e6615fd](https://github.com/MariaDB/server/commit/403e6615fd)\
  2019-07-26 18:17:55 +0300
  * List of unstable tests for 10.1.41 release (updated)
* Merge [Revision #2382cd14a8](https://github.com/MariaDB/server/commit/2382cd14a8) 2019-07-26 13:33:51 +0200 - Merge branch '5.5' into 10.1
* [Revision #f8a1a262e2](https://github.com/MariaDB/server/commit/f8a1a262e2)\
  2019-07-26 13:15:44 +0200
  * Move the test not suitable for embedded.
* Merge [Revision #4177181e16](https://github.com/MariaDB/server/commit/4177181e16) 2019-07-26 10:48:12 +0200 - Merge branch 'merge-tokudb-5.6' into 10.1
* [Revision #24a0d7c507](https://github.com/MariaDB/server/commit/24a0d7c507)\
  2019-07-26 08:48:46 +0200
  * 5.6.44-86.0
* Merge [Revision #25d216dcd5](https://github.com/MariaDB/server/commit/25d216dcd5) 2019-07-26 07:57:57 +0200 - Merge remote-tracking branch 'connect/10.1' into 10.1
* Merge [Revision #fe71854157](https://github.com/MariaDB/server/commit/fe71854157) 2019-03-26 17:13:42 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #6b1e133874](https://github.com/MariaDB/server/commit/6b1e133874)\
  2019-03-25 23:54:09 +0100
  * Fixed compiler warning in connect engine
* [Revision #48d2141ba5](https://github.com/MariaDB/server/commit/48d2141ba5)\
  2019-03-25 17:36:35 +0100
  * Fix [MDEV-15793](https://jira.mariadb.org/browse/MDEV-15793): Server crash in PlugCloseFile with sql\_mode='' Fixed by replacing sprinf by snprintf in ShowValue to avoid buffer overflow. It nows always use a buffer and returns int.
* Merge [Revision #6b0fc1ee0e](https://github.com/MariaDB/server/commit/6b0fc1ee0e) 2019-01-27 13:49:03 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #e0c147c2da](https://github.com/MariaDB/server/commit/e0c147c2da)\
  2019-01-27 12:22:44 +0100
  * Fix [MDEV-18192](https://jira.mariadb.org/browse/MDEV-18192): CONNECT Engine JDBC not able to issue simple UPDATE statement from trigger or stored procedure
* Merge [Revision #e3b3e225df](https://github.com/MariaDB/server/commit/e3b3e225df) 2019-01-04 10:43:32 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #261e9a8a53](https://github.com/MariaDB/server/commit/261e9a8a53)\
  2019-01-03 18:19:36 +0100
  * Fix a few bug mainly concerning discovery and call from OEM (and prepare new table types)
* Merge [Revision #faa1d149a7](https://github.com/MariaDB/server/commit/faa1d149a7) 2018-12-04 23:39:59 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #f25aab0ecf](https://github.com/MariaDB/server/commit/f25aab0ecf)\
  2018-12-04 23:37:58 +0100
  * Fix wrong version number
* Merge [Revision #d6c7189f05](https://github.com/MariaDB/server/commit/d6c7189f05) 2018-12-02 10:39:52 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #0fb92dddf9](https://github.com/MariaDB/server/commit/0fb92dddf9)\
  2018-12-01 23:45:58 +0100
  * Make PlugSubAlloc to be exportable Suppress unused parameter from PlugSubSet
* Merge [Revision #ddff78ab18](https://github.com/MariaDB/server/commit/ddff78ab18) 2018-10-11 22:49:27 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #5d6daa6f15](https://github.com/MariaDB/server/commit/5d6daa6f15)\
  2018-10-11 18:47:59 +0200
  * Implement the CHECK TABLE statement and accept REPAIR and ANALYZE
* Merge [Revision #cce151f010](https://github.com/MariaDB/server/commit/cce151f010) 2018-08-08 12:27:22 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #31dda7e9fd](https://github.com/MariaDB/server/commit/31dda7e9fd)\
  2018-08-08 12:16:56 +0200
  * Comment out failing Cyrillic test in xml2.test
* [Revision #040e7de6de](https://github.com/MariaDB/server/commit/040e7de6de)\
  2018-08-07 19:42:54 +0200
  * Fix [MDEV-16672](https://jira.mariadb.org/browse/MDEV-16672) Connect: Warnings with 10.0 filamtxt.cpp: DOSFAM::RenameTempFile: Change sprintf to snprintf. filamvct.cpp: VECFAM::RenameTempFile: Change sprintf to snprintf. javaconn.cpp: Add JAVAConn::GetUTFString function. Use it instead of env->GetStringUTFChars. Fix wrong identation. javaconn.h: Add GetUTFString declaration. jdbconn.cpp: Use GetUTFString function instead of env->GetStringUTFChars. jmgoconn.cpp: Use GetUTFString function instead of env->GetStringUTFChars. Fix wrong identation. jsonudf.cpp: change 139 to BMX line 4631. tabjmg.cpp: Add ReleaseStringUTF. Fix wrong identation. tabpivot.cpp: Fix wrong identation. tabutil.cpp: TDBPRX::GetSubTable: Change sprintf to snprintf.
* Merge [Revision #01536189ca](https://github.com/MariaDB/server/commit/01536189ca) 2018-06-28 19:28:44 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #3d9d447614](https://github.com/MariaDB/server/commit/3d9d447614)\
  2018-06-28 19:26:54 +0200
  * Fix [MDEV-16167](https://jira.mariadb.org/browse/MDEV-16167) Cannot insert unsigned values into a VEC table
* Merge [Revision #546773fb78](https://github.com/MariaDB/server/commit/546773fb78) 2018-05-07 22:41:34 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #762111ea3a](https://github.com/MariaDB/server/commit/762111ea3a)\
  2018-05-07 18:39:02 +0200
  * Fix [MDEV-15735](https://jira.mariadb.org/browse/MDEV-15735) CONNECT \[filamtxt.cpp:429]: Suspicious condition
* Merge [Revision #3bd6e68a42](https://github.com/MariaDB/server/commit/3bd6e68a42) 2018-03-27 23:17:24 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #494fb254e7](https://github.com/MariaDB/server/commit/494fb254e7)\
  2018-03-27 23:16:14 +0200
  * Fix [MDEV-15577](https://jira.mariadb.org/browse/MDEV-15577) CONNECT engine JDBC remote index prevents UPDATE Fixed in TDBJDBC::OpenDB because query can be null for updates
* Merge [Revision #a0f47c39b7](https://github.com/MariaDB/server/commit/a0f47c39b7) 2018-03-14 11:31:28 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #46defc4373](https://github.com/MariaDB/server/commit/46defc4373)\
  2018-03-14 01:00:59 +0100
  * Fix [MDEV-15429](https://jira.mariadb.org/browse/MDEV-15429) CONNECT engine JDBC handling Postgresql UUID type Also handle Postgresql sending type VARCHAR for TEXT column and setting length to b x7FFFFFF when the length is unknown.
* Merge [Revision #c195e05132](https://github.com/MariaDB/server/commit/c195e05132) 2018-02-26 11:58:50 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #ed5e84eddb](https://github.com/MariaDB/server/commit/ed5e84eddb)\
  2018-02-26 00:40:02 +0100
  * Remove warning on not used tabtyp variable in connect\_assisted\_discovery
* Merge [Revision #34e141180b](https://github.com/MariaDB/server/commit/34e141180b) 2018-02-16 15:43:33 +0100 - Commit merge of new MariaDB version
* [Revision #18e6a81bab](https://github.com/MariaDB/server/commit/18e6a81bab)\
  2018-02-16 15:16:11 +0100
  * Make Json\_Array\_Add to accept a non JSON item as 1st parameter This is a test that will extended to some other UDF functions.
* Merge [Revision #a88bdbdc63](https://github.com/MariaDB/server/commit/a88bdbdc63) 2018-02-14 11:32:58 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #46f3e320da](https://github.com/MariaDB/server/commit/46f3e320da)\
  2018-02-13 15:11:08 +0100
  * Fix a bug causing CONNECT to loop when expanding a JSON column when the expanded column value is null or void array. - Adding the FullArray option to JSON tables. - Skipping expanded JSON lines when the expanded column value is null.
* Merge [Revision #c6e13e3bc2](https://github.com/MariaDB/server/commit/c6e13e3bc2) 2018-02-02 18:14:55 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #d8436c9f24](https://github.com/MariaDB/server/commit/d8436c9f24)\
  2018-02-02 15:39:38 +0100
  * Remove warning on not used tabtyp variable in connect\_assisted\_discovery
* Merge [Revision #27fef1e62a](https://github.com/MariaDB/server/commit/27fef1e62a) 2018-02-01 01:19:58 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #942d727751](https://github.com/MariaDB/server/commit/942d727751)\
  2018-01-31 12:36:46 +0100
  * Use delayed load for the MongoDB C Drive on Windows
* Merge [Revision #dc303220e6](https://github.com/MariaDB/server/commit/dc303220e6) 2018-01-04 17:21:46 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #834559720c](https://github.com/MariaDB/server/commit/834559720c)\
  2018-01-04 13:49:31 +0100
  * Fix [MDEV-9844](https://jira.mariadb.org/browse/MDEV-9844), [MDEV-10179](https://jira.mariadb.org/browse/MDEV-10179), [MDEV-14214](https://jira.mariadb.org/browse/MDEV-14214) This is done by removing the tbl table type THREAD option that causes a multiple of sporadic bugs. This may be temporary depending on whether a real fix is found.
* Merge [Revision #3c6ba5b905](https://github.com/MariaDB/server/commit/3c6ba5b905) 2017-11-03 21:04:26 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #341a36021d](https://github.com/MariaDB/server/commit/341a36021d)\
  2017-11-03 15:24:48 +0100
  * Fix [MDEV-13925](https://jira.mariadb.org/browse/MDEV-13925): Actually this fixes SELECT queries when the WHERE clause have single quote.
* Merge [Revision #bcc39742b9](https://github.com/MariaDB/server/commit/bcc39742b9) 2017-10-17 19:42:05 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #b7f352b278](https://github.com/MariaDB/server/commit/b7f352b278)\
  2017-10-17 12:11:53 +0200
  * Update version number
* Merge [Revision #2c41314eab](https://github.com/MariaDB/server/commit/2c41314eab) 2017-10-11 12:19:40 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #5aec754011](https://github.com/MariaDB/server/commit/5aec754011)\
  2017-10-11 12:18:15 +0200
  * Fix [MDEV-13924](https://jira.mariadb.org/browse/MDEV-13924) modified: storage/connect/jdbconn.cpp
* Merge [Revision #57c14acac8](https://github.com/MariaDB/server/commit/57c14acac8) 2017-09-11 18:16:35 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #791e5fd488](https://github.com/MariaDB/server/commit/791e5fd488)\
  2017-09-11 16:30:45 +0200
  * Enable MONGO for the C driver. Modified: modified: storage/connect/CMakeLists.txt
* Merge [Revision #2b25447f1e](https://github.com/MariaDB/server/commit/2b25447f1e) 2017-09-05 22:41:06 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #0f4b540780](https://github.com/MariaDB/server/commit/0f4b540780)\
  2017-09-05 15:58:46 +0200
  * Update version number
* Merge [Revision #92c8864f7b](https://github.com/MariaDB/server/commit/92c8864f7b) 2017-09-02 19:06:45 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #c23b832556](https://github.com/MariaDB/server/commit/c23b832556)\
  2017-09-02 16:07:46 +0200
  * Fix MongoDB C Driver adding for CMAKE. Requires MongoDB C Driver version 1.7 now available
* Merge [Revision #6884f5628c](https://github.com/MariaDB/server/commit/6884f5628c) 2017-08-31 10:00:48 +0200 - Merge branch 'ob-10.1' into 10.1
* Merge [Revision #f6103105c0](https://github.com/MariaDB/server/commit/f6103105c0) 2017-08-31 01:26:45 +0200 - Merging from MariaDB repository
* Merge [Revision #b1b6b503b4](https://github.com/MariaDB/server/commit/b1b6b503b4) 2017-08-30 11:50:52 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #5c42d86aff](https://github.com/MariaDB/server/commit/5c42d86aff)\
  2017-08-29 18:20:01 +0200
  * New distribution enabling or disabling the MONGO table type
* Merge [Revision #af727451cc](https://github.com/MariaDB/server/commit/af727451cc) 2017-08-27 23:12:37 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #5b998bf953](https://github.com/MariaDB/server/commit/5b998bf953)\
  2017-08-27 17:23:27 +0200
  * Fix [MDEV-13621](https://jira.mariadb.org/browse/MDEV-13621) JDBC UPDATE containing single or double quote chars produces wrong result in ha\_connect::GetStringOption
* Merge [Revision #c499f33b10](https://github.com/MariaDB/server/commit/c499f33b10) 2017-08-20 13:14:55 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #5f83a9b751](https://github.com/MariaDB/server/commit/5f83a9b751)\
  2017-08-20 13:13:52 +0200
  * Fix [MDEV-12422](https://jira.mariadb.org/browse/MDEV-12422) by implementing a fake virtual "check" function.
* Merge [Revision #22a675b5d1](https://github.com/MariaDB/server/commit/22a675b5d1) 2017-08-18 12:46:57 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #b6afeacd33](https://github.com/MariaDB/server/commit/b6afeacd33)\
  2017-08-18 12:45:31 +0200
  * Fix failing test tbl\_thread on linux (and mask another fail until [MDEV-10179](https://jira.mariadb.org/browse/MDEV-10179) is fixed)
* Merge [Revision #5b6906cf5b](https://github.com/MariaDB/server/commit/5b6906cf5b) 2017-08-13 18:59:11 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #4d5844d9da](https://github.com/MariaDB/server/commit/4d5844d9da)\
  2017-08-13 16:11:09 +0200
  * Fix [MDEV-13503](https://jira.mariadb.org/browse/MDEV-13503) Modified: storage/connect/jdbconn.cpp
* Merge [Revision #b94cde2138](https://github.com/MariaDB/server/commit/b94cde2138) 2017-08-11 21:50:47 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #11ce35ea63](https://github.com/MariaDB/server/commit/11ce35ea63)\
  2017-08-11 19:06:33 +0200
  * Restore tabs. Modified: storage/connect/mysql-test/connect/r/xml2\_grant.result and storage/connect/mysql-test/connect/r/xml2\_mdev5261.result
* [Revision #3979f130db](https://github.com/MariaDB/server/commit/3979f130db)\
  2017-08-11 16:44:44 +0200
  * Fix failing tests. Modified: storage/connect/mysql-test/connect/r/xml2\_grant.result and storage/connect/mysql-test/connect/r/xml2\_mdev5261.result
* [Revision #0b9ea65dc1](https://github.com/MariaDB/server/commit/0b9ea65dc1)\
  2017-08-10 16:16:25 +0200
  * Make source from 10.2 source
* [Revision #9e5ca80afe](https://github.com/MariaDB/server/commit/9e5ca80afe)\
  2017-08-06 22:04:14 +0200
  * Fix Linux compile error by #define NODW. Modified: plgdbutl.cpp; typo Modified: odbconn.h
* [Revision #d66d149f0a](https://github.com/MariaDB/server/commit/d66d149f0a)\
  2017-08-06 21:33:52 +0200
  * Make source the same as branch 10.2
* [Revision #bae30c93da](https://github.com/MariaDB/server/commit/bae30c93da)\
  2017-06-10 10:42:38 +0200
  * Last 3 commits of 10.2
* [Revision #96f229460f](https://github.com/MariaDB/server/commit/96f229460f)\
  2017-06-08 18:17:17 +0200
  * Fix [MDEV-12973](https://jira.mariadb.org/browse/MDEV-12973): Blank columns querying SQL Server Added support of NCHAR, NVARCHAR an ROWID JDBC types.
* [Revision #b781d29083](https://github.com/MariaDB/server/commit/b781d29083)\
  2017-06-06 17:32:30 +0200
  * commit git 167, 168 and 169 msg
* Merge [Revision #a6114421a7](https://github.com/MariaDB/server/commit/a6114421a7) 2017-05-28 12:29:40 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #24f5bbac50](https://github.com/MariaDB/server/commit/24f5bbac50)\
  2017-05-28 12:28:12 +0200
  * Add CHECK TABLE to the list of accepted commands. This is to avoid an error to be reported when executing this command on a CONNECT table.
* [Revision #e720e50213](https://github.com/MariaDB/server/commit/e720e50213)\
  2017-05-23 22:59:44 +0200
  * Fix bug: Discovery of JSON table fails in DEBUG mode when NO MONGO support. (tdb->Uri is uninitialized)
* [Revision #37235293b0](https://github.com/MariaDB/server/commit/37235293b0)\
  2017-05-23 14:48:49 +0200
  * Fix gcc compiler warnings reported by Sergei
* Merge [Revision #630d70352c](https://github.com/MariaDB/server/commit/630d70352c) 2017-05-12 11:52:43 +0200 - Merge branch 'develop' into 10.1
* [Revision #8f66819611](https://github.com/MariaDB/server/commit/8f66819611)\
  2017-05-12 11:52:03 +0200
  * Fix column types wrongly set to TYPE\_STRING in JSONColumns when the column contains NULL values.
* Merge [Revision #b9dfbc154b](https://github.com/MariaDB/server/commit/b9dfbc154b) 2017-05-11 17:30:04 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #ea7081bfa2](https://github.com/MariaDB/server/commit/ea7081bfa2)\
  2017-05-11 17:23:02 +0200
  * Fix wrong value of JSON column When null and the column is NOT NULL the value was not reset.
* [Revision #2195f5dc02](https://github.com/MariaDB/server/commit/2195f5dc02)\
  2017-05-11 10:35:14 +0200
  * Fix converting bstr\_t string to set error message
* Merge [Revision #9c887014ef](https://github.com/MariaDB/server/commit/9c887014ef) 2017-05-08 16:51:23 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #9d6677b5ea](https://github.com/MariaDB/server/commit/9d6677b5ea)\
  2017-05-08 14:46:15 +0200
  * _Null\_terminated_ not recognized by gcc
* [Revision #40a56581b0](https://github.com/MariaDB/server/commit/40a56581b0)\
  2017-05-08 12:42:12 +0200
  * Fixing [MDEV-12149](https://jira.mariadb.org/browse/MDEV-12149): compile errors on Windows with /Zc:strictStrings Introduce typedef PCSZ and replace PSZ by it where it matters All done on CONNECT but compile still fails because of an included system file
* [Revision #e7d91cd783](https://github.com/MariaDB/server/commit/e7d91cd783)\
  2017-05-06 23:43:02 +0200
  * Prepare fixing [MDEV-12149](https://jira.mariadb.org/browse/MDEV-12149) compile errors on Windows with /Zc:strictStrings Introduce typedef PCSZ and replace PSZ by it where it matters
* [Revision #d75d61cd6f](https://github.com/MariaDB/server/commit/d75d61cd6f)\
  2017-05-05 23:56:16 +0200
  * Fix [MDEV-12603](https://jira.mariadb.org/browse/MDEV-12603) Insert replaces values in ZIP file
* [Revision #fd166e0377](https://github.com/MariaDB/server/commit/fd166e0377)\
  2017-05-04 18:49:00 +0200
  * Fix [MDEV-12653](https://jira.mariadb.org/browse/MDEV-12653) Cannot add index for ZIP CONNECT table
* Merge [Revision #3f444827d9](https://github.com/MariaDB/server/commit/3f444827d9) 2017-05-03 10:40:29 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #ce3c7cd972](https://github.com/MariaDB/server/commit/ce3c7cd972)\
  2017-05-03 10:39:32 +0200
  * Handle error return from SetPath
* [Revision #2d85b10060](https://github.com/MariaDB/server/commit/2d85b10060)\
  2017-05-03 09:10:26 +0200
  * Fix gcc compile error. modified: storage/connect/tabmul.cpp
* [Revision #cd337a3730](https://github.com/MariaDB/server/commit/cd337a3730)\
  2017-05-03 01:06:00 +0200
  * Fix [MDEV-12587](https://jira.mariadb.org/browse/MDEV-12587) MariaDB CONNECT DIR Type - Subfolder Option: SELECT Query Never Ends
* Merge [Revision #040ccce879](https://github.com/MariaDB/server/commit/040ccce879) 2017-04-29 23:35:13 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #2f9db4ef70](https://github.com/MariaDB/server/commit/2f9db4ef70)\
  2017-04-29 23:33:10 +0200
  * Fix [MDEV-12631](https://jira.mariadb.org/browse/MDEV-12631) valgrind warning for zipped tables
* Merge [Revision #e6da89bad7](https://github.com/MariaDB/server/commit/e6da89bad7) 2017-04-26 23:07:30 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #b6135bb51e](https://github.com/MariaDB/server/commit/b6135bb51e)\
  2017-04-26 18:38:32 +0200
  * Continue working on MONGO tables
* [Revision #36206acc2f](https://github.com/MariaDB/server/commit/36206acc2f)\
  2017-04-25 10:58:34 +0200
  * Work on new MONGO table type Handle discovery, insert, update and delete Add support for Pipeline
* [Revision #0149f9c2a1](https://github.com/MariaDB/server/commit/0149f9c2a1)\
  2017-04-17 10:44:51 +0200
  * Add MONGO table type new file: storage/connect/tabmgo.cpp new file: storage/connect/tabmgo.h
* [Revision #95af77b1f7](https://github.com/MariaDB/server/commit/95af77b1f7)\
  2017-04-14 12:58:47 +0200
  * Comment out in CMakeLists.txt
* [Revision #ff704368c0](https://github.com/MariaDB/server/commit/ff704368c0)\
  2017-04-13 23:52:39 +0200
  * Add mongoDB access to json tables. Finalize replacement of longjmp by throw.
* [Revision #9262ae65fc](https://github.com/MariaDB/server/commit/9262ae65fc)\
  2017-04-13 21:30:33 +0200
  * Add mongoDB access to json tables. Filalize replacement oflongjmp by throw.
* [Revision #2c16792995](https://github.com/MariaDB/server/commit/2c16792995)\
  2017-04-06 19:45:19 +0200
  * Fix bug. Date value was null when retrieved from a json expanded array.
* Merge [Revision #fcfcd99e64](https://github.com/MariaDB/server/commit/fcfcd99e64) 2017-04-06 00:44:53 +0200 - Commit resolved files
* [Revision #332c617690](https://github.com/MariaDB/server/commit/332c617690)\
  2017-04-05 10:22:58 +0200
  * Export TDBJSN class so it can be used by EOM tables
* Merge [Revision #ffa7790d91](https://github.com/MariaDB/server/commit/ffa7790d91) 2017-03-28 10:02:28 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #8bd1f06c5a](https://github.com/MariaDB/server/commit/8bd1f06c5a)\
  2017-03-27 15:51:39 +0200
  * Return to original version of jdbc.test
* [Revision #efe9982873](https://github.com/MariaDB/server/commit/efe9982873)\
  2017-03-27 15:40:07 +0200
  * Fix crash when a line is not ended by \n.
* Merge [Revision #0518081c6d](https://github.com/MariaDB/server/commit/0518081c6d) 2017-03-18 12:43:23 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #cf1ca74736](https://github.com/MariaDB/server/commit/cf1ca74736)\
  2017-03-18 12:42:46 +0100
  * Typo
* [Revision #d9b7433c98](https://github.com/MariaDB/server/commit/d9b7433c98)\
  2017-03-18 10:40:51 +0100
  * Fix [MDEV-12220](https://jira.mariadb.org/browse/MDEV-12220): add MODE\_READX to permissible index read
* [Revision #932a4401f0](https://github.com/MariaDB/server/commit/932a4401f0)\
  2017-03-17 19:00:30 +0100
  * Fix [MDEV-12220](https://jira.mariadb.org/browse/MDEV-12220): Crash when doing UPDATE or DELETE on an external table (ODBC, JDBC, MYSQL) with a WHERE clause on an indexed column. Also fix a bugs in TDBEXT::MakeCommand (use of uninitialised Quote) Add in this function the eventual Schema (database) prefixing.
* Merge [Revision #9e233c1ac0](https://github.com/MariaDB/server/commit/9e233c1ac0) 2017-03-11 17:14:30 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #e5f5457b6f](https://github.com/MariaDB/server/commit/e5f5457b6f)\
  2017-03-11 14:10:34 +0100
  * Also order the result of multiple=1 table, otherwise being different on Linux and Windows causing the test to fail.
* [Revision #2d573a6c5a](https://github.com/MariaDB/server/commit/2d573a6c5a)\
  2017-03-10 17:53:36 +0100
  * CONNECT Storage Engine: Support of ENUM and SET column types for MYSQL tables.
* [Revision #bf6cadf923](https://github.com/MariaDB/server/commit/bf6cadf923)\
  2017-03-10 00:28:26 +0100
  * CONNECT Storage Engine: The last commited changes have brought important additions to CONNECT. 1 - Replacement of setjmp/longjump's by try/catch/throw 2 - Support of multiple tables in subdirectories 3 - Support translating ENUM to VARCHAR for MYSQL tables. 4 - Tables based on ZIP files
* [Revision #cdc7a69ea2](https://github.com/MariaDB/server/commit/cdc7a69ea2)\
  2017-03-09 16:28:11 +0100
  * CONNECT DIR tables: fix retrieving file date values under Windows.
* [Revision #95667ae294](https://github.com/MariaDB/server/commit/95667ae294)\
  2017-03-08 23:30:24 +0100
  * Fix errors in function TDBSDR::FindInDir. Comment out PSYSTEMTIME stp not used in DIRCOL::ReadColumn causing a compile error won Linux?
* [Revision #fc8cf00429](https://github.com/MariaDB/server/commit/fc8cf00429)\
  2017-03-08 11:12:36 +0100
  * Implement sub-directory search for multiple tables. This is specifies by MULTIPLE=3 when creating the table.
* Merge [Revision #e1c271067e](https://github.com/MariaDB/server/commit/e1c271067e) 2017-03-06 15:08:37 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #c4471352db](https://github.com/MariaDB/server/commit/c4471352db)\
  2017-03-05 23:54:54 +0100
  * Fix [MDEV-12142](https://jira.mariadb.org/browse/MDEV-12142) crash when creating CSV table Was an unprepared longjmp (now throw) Also fix a wrong calculation of To\_Line sometimes causing a crash because of buffer overflow.
* [Revision #e52bf14714](https://github.com/MariaDB/server/commit/e52bf14714)\
  2017-03-05 19:43:17 +0100
  * Replace setjmp-longjmp's by try\_catch-throw
* Merge [Revision #5c8ef4953d](https://github.com/MariaDB/server/commit/5c8ef4953d) 2017-03-02 00:24:36 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #180fe61c1a](https://github.com/MariaDB/server/commit/180fe61c1a)\
  2017-03-01 12:17:25 +0100
  * Update version number and date
* Merge [Revision #a8dacd03c3](https://github.com/MariaDB/server/commit/a8dacd03c3) 2017-02-24 23:18:22 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #62cd105689](https://github.com/MariaDB/server/commit/62cd105689)\
  2017-02-24 23:15:28 +0100
  * Fix crashing when joining two JDBC tables.. Was in close (the virtual machine could have been detached.
* Merge [Revision #c4ae3fcc68](https://github.com/MariaDB/server/commit/c4ae3fcc68) 2017-02-16 12:05:46 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #403ef9918f](https://github.com/MariaDB/server/commit/403ef9918f)\
  2017-02-15 00:30:00 +0100
  * Fix gcc compile error on friend declaration. "friend TDBEXT" must specified as "friend class TDBEXT"
* [Revision #6aa144f8d6](https://github.com/MariaDB/server/commit/6aa144f8d6)\
  2017-02-14 21:15:26 +0100
  * Fix gcc compile error on strlwr.
* [Revision #41b4ef4348](https://github.com/MariaDB/server/commit/41b4ef4348)\
  2017-02-14 15:38:07 +0100
  * Add the tabext.cpp and tabext.h files in the source list.
* [Revision #5c2c68d454](https://github.com/MariaDB/server/commit/5c2c68d454)\
  2017-02-14 12:20:20 +0100
  * This is a major update concerning many source files.
* Merge [Revision #de4fcf1e33](https://github.com/MariaDB/server/commit/de4fcf1e33) 2017-01-17 19:24:48 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #9fa0d2fe98](https://github.com/MariaDB/server/commit/9fa0d2fe98)\
  2017-01-17 10:42:41 +0100
  * Replace bios.json CRLF by LF to avoid test failing on Linux.
* [Revision #286819aef2](https://github.com/MariaDB/server/commit/286819aef2)\
  2017-01-16 22:42:56 +0100
  * Fix gcc errors and warnings.
* [Revision #b1bd990e45](https://github.com/MariaDB/server/commit/b1bd990e45)\
  2017-01-16 18:57:35 +0100
  * Add #include \<fnmatch.h> #include \<dirent.h> to avoid compile error on Linux.
* [Revision #c7446daeb6](https://github.com/MariaDB/server/commit/c7446daeb6)\
  2017-01-16 18:03:09 +0100
  * Add #include \<fnmatch.h> #include \<stdlib.h> #include \<stdio.h> #include \<string.h> to avoid compile error on Linux.
* [Revision #0cb9369b37](https://github.com/MariaDB/server/commit/0cb9369b37)\
  2017-01-16 17:18:54 +0100
  * Add #include \<fnmatch.h> to avoid compile error on Linux.
* [Revision #707cd98592](https://github.com/MariaDB/server/commit/707cd98592)\
  2017-01-16 15:13:40 +0100
  * Fix info cardinality for catalog tables. Was returning 0, which caused an assert error when retreiving records.
* Merge [Revision #0b527dd36b](https://github.com/MariaDB/server/commit/0b527dd36b) 2016-12-25 12:19:11 +0100 - Merge branch 'ob-10.1' into 10.1
* Merge [Revision #df21d45fdd](https://github.com/MariaDB/server/commit/df21d45fdd) 2016-12-24 17:48:21 +0100 - Merge branch '10.1' of [server](https://github.com/MariaDB/server) into ob-10.1
* [Revision #00e0acd814](https://github.com/MariaDB/server/commit/00e0acd814)\
  2016-12-24 17:48:10 +0100
  * Changing version number in ha\_connect.cc
* Merge [Revision #970c90e8bd](https://github.com/MariaDB/server/commit/970c90e8bd) 2016-12-23 16:42:01 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #5c0c623577](https://github.com/MariaDB/server/commit/5c0c623577)\
  2016-12-23 14:23:46 +0100
  * Fix some XML table type bugs
* Merge [Revision #2b415eac08](https://github.com/MariaDB/server/commit/2b415eac08) 2016-12-14 14:40:26 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #b3d2ac3492](https://github.com/MariaDB/server/commit/b3d2ac3492)\
  2016-12-14 14:37:31 +0100
  * [MDEV-11295](https://jira.mariadb.org/browse/MDEV-11295): developing handling files contained in ZIP file. Fix bug using multiple zip files
* Merge [Revision #a411f0133c](https://github.com/MariaDB/server/commit/a411f0133c) 2016-12-14 11:16:52 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #8a3fc7c041](https://github.com/MariaDB/server/commit/8a3fc7c041)\
  2016-12-14 11:11:22 +0100
  * [MDEV-11295](https://jira.mariadb.org/browse/MDEV-11295): developing handling files contained in ZIP file. Enable using multiple zip files
* Merge [Revision #87261eeba9](https://github.com/MariaDB/server/commit/87261eeba9) 2016-12-12 10:35:30 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #0e06a8357b](https://github.com/MariaDB/server/commit/0e06a8357b)\
  2016-12-12 00:49:31 +0100
  * [MDEV-11295](https://jira.mariadb.org/browse/MDEV-11295): developing handling files contained in ZIP file. A first experimental and limited implementation. Add NOCRYPT preprocessor definition to avoid compiling error
* [Revision #9afa90090a](https://github.com/MariaDB/server/commit/9afa90090a)\
  2016-12-11 23:47:15 +0100
  * [MDEV-11295](https://jira.mariadb.org/browse/MDEV-11295): developing handling files contained in ZIP file. A first experimental and limited implementation.
* Merge [Revision #751abafb01](https://github.com/MariaDB/server/commit/751abafb01) 2016-12-02 22:46:46 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #c6a72d2c9c](https://github.com/MariaDB/server/commit/c6a72d2c9c)\
  2016-12-02 11:29:14 +0100
  * [MDEV-11366](https://jira.mariadb.org/browse/MDEV-11366) SIGBUS errors in Connect Storage Engine for ArmHF and MIPS. Fix includes launchpad fix plus more to cover writing BIN tables.
* Merge [Revision #f292666c5e](https://github.com/MariaDB/server/commit/f292666c5e) 2016-11-27 14:37:43 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #c82462c054](https://github.com/MariaDB/server/commit/c82462c054)\
  2016-11-27 14:35:01 +0100
  * Fix null pointer java error when connecting to jdbc:drill driver. By setting the context class loader.
* [Revision #c2f93a3354](https://github.com/MariaDB/server/commit/c2f93a3354)\
  2016-11-27 14:22:04 +0100
  * Fix null pointer java error when connecting to jdbc:drill driver. By setting the context class loader.
* Merge [Revision #9759d90ba0](https://github.com/MariaDB/server/commit/9759d90ba0) 2016-11-14 18:49:09 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #558245d540](https://github.com/MariaDB/server/commit/558245d540)\
  2016-11-14 15:22:22 +0100
  * [MDEV-11051](https://jira.mariadb.org/browse/MDEV-11051) place Java classes ApacheInterface and JdbcInterface into single jar file. Try to fix the INSTALL command.
* [Revision #163629f32b](https://github.com/MariaDB/server/commit/163629f32b)\
  2016-11-14 11:41:46 +0100
  * [MDEV-11067](https://jira.mariadb.org/browse/MDEV-11067) suggested to add configuration support to the Apache wrapper. Try to fix the INSTALL command.
* [Revision #0bec832fea](https://github.com/MariaDB/server/commit/0bec832fea)\
  2016-11-14 00:46:45 +0100
  * [MDEV-11067](https://jira.mariadb.org/browse/MDEV-11067) suggested to add configuration support to the Apache wrapper. Suppress / from the INSTALL command.
* [Revision #db926c385e](https://github.com/MariaDB/server/commit/db926c385e)\
  2016-11-13 23:41:58 +0100
  * [MDEV-11067](https://jira.mariadb.org/browse/MDEV-11067) suggested to add configuration support to the Apache wrapper. Directly install a precompiled JavaWrappers.jar file.
* [Revision #bc65996b82](https://github.com/MariaDB/server/commit/bc65996b82)\
  2016-11-13 18:39:35 +0100
  * Fix [MDEV-11267](https://jira.mariadb.org/browse/MDEV-11267). Insert NULL into JDBC table does not work. Fixed in JDBConn::SetParam and adding java function SetNullParm.
* Merge [Revision #6bd527fc96](https://github.com/MariaDB/server/commit/6bd527fc96) 2016-11-06 14:45:11 +0100 - Merge branch 'ob-10.1' into 10.1
* [Revision #cde0746135](https://github.com/MariaDB/server/commit/cde0746135)\
  2016-11-06 10:23:18 +0100
  * Fix [MDEV-11234](https://jira.mariadb.org/browse/MDEV-11234). Escape quoting character. Should be doubled. Now it is also possible to escape it by a backslash.
* Merge [Revision #c8edba368c](https://github.com/MariaDB/server/commit/c8edba368c) 2016-10-14 17:57:43 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #cb8e5ecbce](https://github.com/MariaDB/server/commit/cb8e5ecbce)\
  2016-10-14 17:32:21 +0200
  * Fix [MDEV-10950](https://jira.mariadb.org/browse/MDEV-10950). Null values not retrieved for numeric types. Now the null is tested using the result set getObject method.
* Merge [Revision #1548d7f3f3](https://github.com/MariaDB/server/commit/1548d7f3f3) 2016-10-05 18:02:57 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #e6c678c8a9](https://github.com/MariaDB/server/commit/e6c678c8a9)\
  2016-10-05 16:03:50 +0200
  * Fix [MDEV-10948](https://jira.mariadb.org/browse/MDEV-10948). Syntax error on quoted JDBC tables. Was because the quoting character was always '"' instead of being retrieve from the JDBC source.
* Merge [Revision #3d208649e0](https://github.com/MariaDB/server/commit/3d208649e0) 2016-09-16 22:00:51 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #98cc0913f0](https://github.com/MariaDB/server/commit/98cc0913f0)\
  2016-09-16 17:30:46 +0200
  * Woking on [MDEV-10525](https://jira.mariadb.org/browse/MDEV-10525). Lrecl mismatch on DBF files
* Merge [Revision #0799cf0804](https://github.com/MariaDB/server/commit/0799cf0804) 2016-09-05 13:04:55 +0200 - Fix merge conflict
* [Revision #a4623b5160](https://github.com/MariaDB/server/commit/a4623b5160)\
  2016-09-05 12:47:52 +0200
  * Fix [MDEV-10496](https://jira.mariadb.org/browse/MDEV-10496). Memory leak in discovery
* Merge [Revision #72f262ce6e](https://github.com/MariaDB/server/commit/72f262ce6e) 2016-09-05 12:49:39 +0200 - Merge branch '10.1' of [server](https://github.com/MariaDB/server) into 10.1
* [Revision #55fb72d869](https://github.com/MariaDB/server/commit/55fb72d869)\
  2016-08-10 17:57:58 +0200
  * JdbcInterface: change return type of ...Field function
* [Revision #e4b1846c60](https://github.com/MariaDB/server/commit/e4b1846c60)\
  2016-07-15 00:43:37 +0200
  * jdbc.test: change data file girls.txt CRLF to LF
* [Revision #543cba96c6](https://github.com/MariaDB/server/commit/543cba96c6)\
  2016-07-14 19:47:40 +0200
  * Disable JDBC tests that fail on Linux
* [Revision #72844d88f6](https://github.com/MariaDB/server/commit/72844d88f6)\
  2016-07-12 11:56:38 +0200
  * Adding DESTINATION to install\_jar in CMakeLists.txt
* [Revision #11a1332b87](https://github.com/MariaDB/server/commit/11a1332b87)\
  2016-07-11 19:14:19 +0200
  * Change CONNECT to connect-engine in CMakeLists.txt
* [Revision #11f0eb0f1d](https://github.com/MariaDB/server/commit/11f0eb0f1d)\
  2016-07-11 18:45:37 +0200
  * Add CONNECT\_WITH\_JDBC to CMakeLists.txt
* [Revision #8388ae6c00](https://github.com/MariaDB/server/commit/8388ae6c00)\
  2016-07-11 15:22:30 +0200
  * Try distributing the JdbcInterface.jar ${INSTALL\_PLUGIN\_DIR} --> ${INSTALL\_PLUGINDIR}
* [Revision #fca92ced73](https://github.com/MariaDB/server/commit/fca92ced73)\
  2016-07-09 12:15:30 +0200
  * remove jdrv.test
* [Revision #b6209dc519](https://github.com/MariaDB/server/commit/b6209dc519)\
  2016-07-09 12:08:31 +0200
  * JAVA DEBUG now depends on connect\_xtrace MySQL and MariaDB drivers use catalog for schema
* [Revision #fc905f15d1](https://github.com/MariaDB/server/commit/fc905f15d1)\
  2016-07-02 18:08:40 +0200
  * New version of java wrappers as the "wrappers" package
* [Revision #b0c90e8186](https://github.com/MariaDB/server/commit/b0c90e8186)\
  2016-06-30 11:28:24 +0200
  * New version of java wrappers as the "wrappers" package
* [Revision #92dbe32ddb](https://github.com/MariaDB/server/commit/92dbe32ddb)\
  2016-06-25 14:26:36 +0200
  * Define MAX\_CONNECT\_LEN as 1024 following MSDN recommendation
* [Revision #d50acf9f88](https://github.com/MariaDB/server/commit/d50acf9f88)\
  2016-06-22 19:52:40 +0200
  * Fix warning "invalid conversion from const char \* to char \*"
* Merge [Revision #584d213235](https://github.com/MariaDB/server/commit/584d213235) 2019-07-25 17:42:20 +0200 - Merge branch '5.5' into 10.1
* Merge [Revision #ae476868a5](https://github.com/MariaDB/server/commit/ae476868a5) 2019-07-25 13:27:11 +0200 - Merge branch '5.5' into 10.1
* [Revision #8d0dabc56b](https://github.com/MariaDB/server/commit/8d0dabc56b)\
  2019-07-25 14:23:47 +0530
  * [MDEV-20091](https://jira.mariadb.org/browse/MDEV-20091) DROP TEMPORARY table is logged despite no CREATE was logged
* [Revision #f6ea0389a4](https://github.com/MariaDB/server/commit/f6ea0389a4)\
  2019-07-25 10:30:28 +0300
  * Replace ut\_timer() with my\_interval\_timer()
* [Revision #e32f29b7f3](https://github.com/MariaDB/server/commit/e32f29b7f3)\
  2019-07-23 15:46:51 +0530
  * [MDEV-20091](https://jira.mariadb.org/browse/MDEV-20091) DROP TEMPORARY table is logged despite no CREATE was logged
* [Revision #0c7c61019d](https://github.com/MariaDB/server/commit/0c7c61019d)\
  2019-07-24 21:43:19 +0300
  * Remove the wrappers ut\_time(), ut\_difftime(), ib\_time\_t
* [Revision #c663a9414b](https://github.com/MariaDB/server/commit/c663a9414b)\
  2019-07-24 21:07:48 +0300
  * [MDEV-14154](https://jira.mariadb.org/browse/MDEV-14154): Failing assertion: slot->last\_run <= current\_time in fts0opt.cc
* [Revision #9e5df96751](https://github.com/MariaDB/server/commit/9e5df96751)\
  2019-07-24 20:50:59 +0300
  * Reduce the amount of time(NULL) calls for lock processing
* [Revision #2b5bc761d3](https://github.com/MariaDB/server/commit/2b5bc761d3)\
  2019-07-24 13:55:59 +0300
  * [MDEV-14154](https://jira.mariadb.org/browse/MDEV-14154): Document some time\_t fields better
* [Revision #10727b6953](https://github.com/MariaDB/server/commit/10727b6953)\
  2019-07-24 20:43:24 +0300
  * Always initialize trx\_t::start\_time\_micro
* [Revision #10ee1b95b8](https://github.com/MariaDB/server/commit/10ee1b95b8)\
  2019-07-24 20:02:07 +0300
  * Remove ut\_usectime(), ut\_gettimeofday()
* [Revision #e764d5bc01](https://github.com/MariaDB/server/commit/e764d5bc01)\
  2019-07-24 19:48:38 +0300
  * Correct the type of a parameter
* [Revision #ab6dd77408](https://github.com/MariaDB/server/commit/ab6dd77408)\
  2019-07-24 19:43:37 +0300
  * [MDEV-14154](https://jira.mariadb.org/browse/MDEV-14154): Remove ut\_time\_us()
* [Revision #86767f4ac1](https://github.com/MariaDB/server/commit/86767f4ac1)\
  2019-07-24 19:41:59 +0300
  * Remove unused ut\_get\_year\_month\_day()
* [Revision #c83663e574](https://github.com/MariaDB/server/commit/c83663e574)\
  2019-07-24 00:43:21 +0300
  * List of unstable tests for 10.1.41 release
* Merge [Revision #1f498f901b](https://github.com/MariaDB/server/commit/1f498f901b) 2019-07-23 15:47:22 +0300 - 5.6.44-86.0
* [Revision #c385d80abd](https://github.com/MariaDB/server/commit/c385d80abd)\
  2019-01-30 10:16:55 +0200
  * Fix PS-5388 (Enable hardware CRC32 under Valgrind)
* [Revision #d653db32f2](https://github.com/MariaDB/server/commit/d653db32f2)\
  2019-07-23 14:40:22 +0300
  * [MDEV-14154](https://jira.mariadb.org/browse/MDEV-14154): Make ut\_time\_ms(), ut\_time\_us() monotonic
* [Revision #61b5e244d6](https://github.com/MariaDB/server/commit/61b5e244d6)\
  2019-07-23 15:15:00 +0300
  * [MDEV-20127](https://jira.mariadb.org/browse/MDEV-20127) Merge new release of InnoDB 5.6.45 to 10.1
* [Revision #e6c1e588f0](https://github.com/MariaDB/server/commit/e6c1e588f0)\
  2019-07-23 14:51:48 +0300
  * gen\_lex\_hash: Omit deprecated register keywords
* [Revision #a5e268a293](https://github.com/MariaDB/server/commit/a5e268a293)\
  2019-07-22 14:55:46 +0300
  * [MDEV-20102](https://jira.mariadb.org/browse/MDEV-20102) Phantom InnoDB table remains after interrupted CREATE...SELECT
* [Revision #4aa97ba594](https://github.com/MariaDB/server/commit/4aa97ba594)\
  2019-07-19 09:48:17 +0300
  * Fix innodb-system-table-view for --embedded
* [Revision #864f0005f9](https://github.com/MariaDB/server/commit/864f0005f9)\
  2019-07-18 23:26:52 +0300
  * [MDEV-20094](https://jira.mariadb.org/browse/MDEV-20094): Disable innodb.check\_ibd\_filesize
* [Revision #a24e824cc4](https://github.com/MariaDB/server/commit/a24e824cc4)\
  2019-07-18 23:24:13 +0300
  * [MDEV-20097](https://jira.mariadb.org/browse/MDEV-20097): Also fix XtraDB
* [Revision #5b205458d9](https://github.com/MariaDB/server/commit/5b205458d9)\
  2019-07-18 22:28:11 +0300
  * [MDEV-20097](https://jira.mariadb.org/browse/MDEV-20097) potential use-after-free
* [Revision #f616e2b97f](https://github.com/MariaDB/server/commit/f616e2b97f)\
  2019-07-18 16:51:16 +0300
  * [MDEV-13625](https://jira.mariadb.org/browse/MDEV-13625): Add innodb.check\_ibd\_filesize
* [Revision #eb14806e6c](https://github.com/MariaDB/server/commit/eb14806e6c)\
  2019-07-18 15:01:13 +0300
  * [MDEV-13625](https://jira.mariadb.org/browse/MDEV-13625): Adapt the test innodb-system-table-view
* [Revision #5a22c45604](https://github.com/MariaDB/server/commit/5a22c45604)\
  2019-07-18 14:30:34 +0300
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Add the test innodb.trx\_id\_future
* [Revision #adbab0d4cd](https://github.com/MariaDB/server/commit/adbab0d4cd)\
  2019-06-26 12:07:17 +0300
  * [MDEV-13625](https://jira.mariadb.org/browse/MDEV-13625): Add the test innodb.innodb-wl5980-debug
* [Revision #10ebdb7f1d](https://github.com/MariaDB/server/commit/10ebdb7f1d)\
  2019-07-15 13:30:10 +0530
  * [MDEV-11154](https://jira.mariadb.org/browse/MDEV-11154): Write\_on\_release\_cache(log\_event.cc) function will not write "COMMIT", if use "mysqlbinlog ... | mysql ..."
* [Revision #aba2b41e9e](https://github.com/MariaDB/server/commit/aba2b41e9e)\
  2019-07-11 18:24:27 +0530
  * [MDEV-19978](https://jira.mariadb.org/browse/MDEV-19978) Page read from tablespace is corrupted
* [Revision #e52fea3fe9](https://github.com/MariaDB/server/commit/e52fea3fe9)\
  2019-07-11 02:55:04 -0700
  * Fix typo open\_table\_def()
* [Revision #d91dd2878a](https://github.com/MariaDB/server/commit/d91dd2878a)\
  2019-07-08 18:15:47 +0200
  * [MDEV-9409](https://jira.mariadb.org/browse/MDEV-9409) workaround
* [Revision #a43edf73f3](https://github.com/MariaDB/server/commit/a43edf73f3)\
  2019-07-08 12:08:00 +0200
  * restore RESTRICT\_SYMBOL\_EXPORTS(zlib)
* [Revision #5d04391f58](https://github.com/MariaDB/server/commit/5d04391f58)\
  2019-07-05 08:37:44 +0200
  * [MDEV-19726](https://jira.mariadb.org/browse/MDEV-19726) MariaDB server or backup RPM install assumes mysql user exists
* [Revision #bdc961acc7](https://github.com/MariaDB/server/commit/bdc961acc7)\
  2019-07-10 11:51:43 +0530
  * [MDEV-17588](https://jira.mariadb.org/browse/MDEV-17588) replicate-do filters cause errors when creating filtered-out tables on master with syntax unsupported on slave
* [Revision #fd08f95322](https://github.com/MariaDB/server/commit/fd08f95322)\
  2019-07-08 11:37:34 +0530
  * [MDEV-17963](https://jira.mariadb.org/browse/MDEV-17963): Assertion `field_pos < field_count' failed in Protocol_text::store, Assertion` field\_handlers == 0 || field\_pos < field\_count'
* [Revision #838bb9fad4](https://github.com/MariaDB/server/commit/838bb9fad4)\
  2019-07-08 17:04:18 +0300
  * fix Galera memory leak
* [Revision #02a0ebc613](https://github.com/MariaDB/server/commit/02a0ebc613)\
  2019-07-06 12:22:45 +0100
  * Make Win compiler happy about the SERVER\_AUDIT code.
* [Revision #d04961cdb3](https://github.com/MariaDB/server/commit/d04961cdb3)\
  2019-07-05 12:22:04 +0100
  * Make Win compiler happy.
* [Revision #be22d1ff39](https://github.com/MariaDB/server/commit/be22d1ff39)\
  2019-07-05 12:06:34 +0400
  * Adding tests for [MDEV-17857](https://jira.mariadb.org/browse/MDEV-17857) Assertion \`tmp != ((long long) 0x8000000000000000LL)' failed in TIME\_from\_longlong\_datetime\_packed upon SELECT with GROUP BY
* [Revision #11f13bff21](https://github.com/MariaDB/server/commit/11f13bff21)\
  2019-07-05 09:15:40 +0400
  * [MDEV-17857](https://jira.mariadb.org/browse/MDEV-17857) Assertion \`tmp != ((long long) 0x8000000000000000LL)' failed in TIME\_from\_longlong\_datetime\_packed upon SELECT with GROUP BY
* [Revision #bee24fe181](https://github.com/MariaDB/server/commit/bee24fe181)\
  2019-06-30 11:16:33 +0200
  * [MDEV-19726](https://jira.mariadb.org/browse/MDEV-19726) MariaDB server or backup RPM install assumes mysql user exists
* [Revision #1003c76eb4](https://github.com/MariaDB/server/commit/1003c76eb4)\
  2019-06-30 11:17:55 +0200
  * fix incorrect shell usage
* [Revision #971bef89ab](https://github.com/MariaDB/server/commit/971bef89ab)\
  2019-06-18 14:19:49 +0200
  * [MDEV-19481](https://jira.mariadb.org/browse/MDEV-19481) mariadb-10.3.15-linux-systemd-x86\_64/bin/mysqld: /lib64/libstdc++.so.6: version \`GLIBCXX\_3.4.20' and 'GLIBCXX\_3.4.21' not found
* [Revision #a099284b71](https://github.com/MariaDB/server/commit/a099284b71)\
  2019-07-03 16:41:01 +0400
  * [MDEV-19851](https://jira.mariadb.org/browse/MDEV-19851) server\_audit plugin should not allow server\_audit\_output\_type=SYSLOG on Windows.
* [Revision #bf37b9fce9](https://github.com/MariaDB/server/commit/bf37b9fce9)\
  2019-06-10 09:07:49 -0700
  * [MDEV-19636](https://jira.mariadb.org/browse/MDEV-19636) Usage message for plugin activation - add FORCE\_PLUS\_PERMANENT
* [Revision #b105427745](https://github.com/MariaDB/server/commit/b105427745)\
  2019-07-02 10:06:13 +0300
  * [MDEV-19660](https://jira.mariadb.org/browse/MDEV-19660): wsrep\_rec\_get\_foreign\_key() is dereferencing a stale pointer to a page that was previously latched
* [Revision #82bb108ea9](https://github.com/MariaDB/server/commit/82bb108ea9)\
  2019-07-01 13:15:20 +0300
  * Update test case
* [Revision #3816c411bf](https://github.com/MariaDB/server/commit/3816c411bf)\
  2019-06-18 13:24:57 +0800
  * repair\_symlink-5543 fails: ELOOP is 90
* [Revision #85f1022410](https://github.com/MariaDB/server/commit/85f1022410)\
  2019-06-29 01:03:56 +0530
  * Fix galera\_log\_bin
* [Revision #49ec78ab70](https://github.com/MariaDB/server/commit/49ec78ab70)\
  2019-06-28 21:50:56 +0530
  * [MDEV-19370](https://jira.mariadb.org/browse/MDEV-19370): rpl.kill\_race\_condition failed in buildbot with Wrong value for slave parameter
* [Revision #5c1f51835a](https://github.com/MariaDB/server/commit/5c1f51835a)\
  2019-06-28 17:46:43 +0300
  * [MDEV-19904](https://jira.mariadb.org/browse/MDEV-19904) poradic buildbot failures in rpl.rpl\_semi\_sync\_uninstall\_plugin
* [Revision #354b14e718](https://github.com/MariaDB/server/commit/354b14e718)\
  2019-06-27 12:43:51 +0530
  * Fix galera\_as\_slave\_gtid.test galera\_var\_gtid\_domain\_id galera.mdev\_10518.test
* [Revision #6bc782a233](https://github.com/MariaDB/server/commit/6bc782a233)\
  2019-06-27 11:15:00 +0530
  * Fix galera\_sync\_wait\_show.test
* [Revision #7f2cfa8f47](https://github.com/MariaDB/server/commit/7f2cfa8f47)\
  2019-06-12 15:58:44 +0530
  * [MDEV-8874](https://jira.mariadb.org/browse/MDEV-8874) Replication filters configured in my.cnf are ignored if slave reset and reconfigured
* [Revision #aa55d93cde](https://github.com/MariaDB/server/commit/aa55d93cde)\
  2019-06-26 14:49:23 +0530
  * Fix galera\_log\_output\_csv.test
* [Revision #d36c107a6b](https://github.com/MariaDB/server/commit/d36c107a6b)\
  2019-06-24 19:38:00 +0300
  * imporve clang build
* [Revision #d78145459f](https://github.com/MariaDB/server/commit/d78145459f)\
  2019-06-13 20:42:13 +0300
  * Fixed Aria recovery progress printing
* [Revision #793e5be770](https://github.com/MariaDB/server/commit/793e5be770)\
  2019-06-13 17:54:28 +0300
  * Give a readable error if aria\_log page numbers doesn't match
* [Revision #204434f2d0](https://github.com/MariaDB/server/commit/204434f2d0)\
  2019-06-13 20:31:41 +0300
  * Backport aria usage if LSN\_FMT from 10.3
* Merge [Revision #cf40393471](https://github.com/MariaDB/server/commit/cf40393471) 2019-06-20 12:26:01 +0300 - Merge 5.5 into 10.1
* [Revision #d1fa6ba845](https://github.com/MariaDB/server/commit/d1fa6ba845)\
  2019-06-08 17:36:52 +0200
  * [MDEV-18328](https://jira.mariadb.org/browse/MDEV-18328): Make DISKS plugin check some privilege to access information\_schema.DISKS table
* [Revision #65e0c9b91b](https://github.com/MariaDB/server/commit/65e0c9b91b)\
  2019-06-15 01:02:55 +0400
  * [MDEV-18661](https://jira.mariadb.org/browse/MDEV-18661) loading the audit plugin causes performance regression.
* Merge [Revision #5b65d61d93](https://github.com/MariaDB/server/commit/5b65d61d93) 2019-06-12 22:54:46 +0200 - Merge branch '5.5' into 10.1
* [Revision #56c60b2fc5](https://github.com/MariaDB/server/commit/56c60b2fc5)\
  2019-06-12 19:02:08 +0300
  * [MDEV-16111](https://jira.mariadb.org/browse/MDEV-16111) encryption.innodb\_lotoftables failed in buildbot with wrong result
* [Revision #efc3cb9322](https://github.com/MariaDB/server/commit/efc3cb9322)\
  2019-06-12 12:50:19 +0300
  * [MDEV-19563](https://jira.mariadb.org/browse/MDEV-19563) Removed references to deprecated option innodb\_locks\_unsafe\_for\_binlog
* [Revision #9d886de499](https://github.com/MariaDB/server/commit/9d886de499)\
  2019-06-12 13:09:41 +0400
  * [MDEV-16467](https://jira.mariadb.org/browse/MDEV-16467) - MariaDB crashes because of "long semaphore wait"after migrating from 10.1 to 10.3
* [Revision #b2f76bac03](https://github.com/MariaDB/server/commit/b2f76bac03)\
  2019-06-12 12:25:00 +0530
  * [MDEV-16866](https://jira.mariadb.org/browse/MDEV-16866) InnoDB fails to start upon crash recovery with "\[ERROR] InnoDB: Redo log crypto: failed to decrypt log block"
* [Revision #c5fe1b8fc1](https://github.com/MariaDB/server/commit/c5fe1b8fc1)\
  2019-06-12 12:17:13 +0530
  * [MDEV-16866](https://jira.mariadb.org/browse/MDEV-16866) InnoDB fails to start upon crash recovery with "\[ERROR] InnoDB: Redo log crypto: failed to decrypt log block"
* [Revision #e7695f95ae](https://github.com/MariaDB/server/commit/e7695f95ae)\
  2019-06-07 12:24:27 +0400
  * [MDEV-19360](https://jira.mariadb.org/browse/MDEV-19360) - Disable \_FORTIFY\_SOURCE for ASAN builds
* [Revision #c97c8c28b5](https://github.com/MariaDB/server/commit/c97c8c28b5)\
  2019-06-05 19:42:21 +0200
  * [MDEV-17103](https://jira.mariadb.org/browse/MDEV-17103) MY\_CHECK\_{C,CXX}\_COMPILER\_FLAG do not work on with localized gcc messages
* [Revision #b003b0c934](https://github.com/MariaDB/server/commit/b003b0c934)\
  2019-06-03 12:42:36 +0400
  * [MDEV-19675](https://jira.mariadb.org/browse/MDEV-19675) Wrong charset is chosen when opening a pre-4.1 table
* [Revision #5a19908b95](https://github.com/MariaDB/server/commit/5a19908b95)\
  2019-05-31 15:24:40 +0400
  * [MDEV-19653](https://jira.mariadb.org/browse/MDEV-19653) Add class Sql\_cmd\_create\_table
* [Revision #dd939d6f7e](https://github.com/MariaDB/server/commit/dd939d6f7e)\
  2019-05-30 19:34:08 +0400
  * [MDEV-15734](https://jira.mariadb.org/browse/MDEV-15734) - calculation inside sizeof() warning
* [Revision #78c1be8b6b](https://github.com/MariaDB/server/commit/78c1be8b6b)\
  2019-05-30 12:11:57 +0530
  * [MDEV-18913](https://jira.mariadb.org/browse/MDEV-18913): typo in error log
* [Revision #a47464d1c1](https://github.com/MariaDB/server/commit/a47464d1c1)\
  2019-05-29 17:35:29 +0530
  * [MDEV-11094](https://jira.mariadb.org/browse/MDEV-11094): Blackhole table updates on slave fail when row annotation is enabled
* [Revision #b347396181](https://github.com/MariaDB/server/commit/b347396181)\
  2019-05-28 14:20:39 +0530
  * [MDEV-11094](https://jira.mariadb.org/browse/MDEV-11094): Blackhole table updates on slave fail when row annotation is enabled
* [Revision #8358c6f03e](https://github.com/MariaDB/server/commit/8358c6f03e)\
  2019-05-28 15:24:32 +0300
  * [MDEV-19614](https://jira.mariadb.org/browse/MDEV-19614): Fix innodb\_plugin on Windows
* Merge [Revision #bf8fe324d2](https://github.com/MariaDB/server/commit/bf8fe324d2) 2019-05-28 11:25:45 +0300 - Merge 5.5 into 10.1
* [Revision #626f2a1c17](https://github.com/MariaDB/server/commit/626f2a1c17)\
  2019-05-28 10:50:17 +0300
  * [MDEV-19614](https://jira.mariadb.org/browse/MDEV-19614) SET GLOBAL innodb\_ deadlock due to LOCK\_global\_system\_variables
* [Revision #242a28c320](https://github.com/MariaDB/server/commit/242a28c320)\
  2019-05-28 08:07:45 +0300
  * [MDEV-6812](https://jira.mariadb.org/browse/MDEV-6812): Remove the wrapper my\_log2f()
* [Revision #661289f462](https://github.com/MariaDB/server/commit/661289f462)\
  2019-05-21 09:20:49 +0300
  * Mention the sample IPv4 address 10.0.0.1
* [Revision #aaf53ea0b6](https://github.com/MariaDB/server/commit/aaf53ea0b6)\
  2019-05-23 21:12:14 +0300
  * [MDEV-17948](https://jira.mariadb.org/browse/MDEV-17948) Assertion \`thd\_killed(thd) || !m\_active\_tranxs ..
* [Revision #e57bb1f76c](https://github.com/MariaDB/server/commit/e57bb1f76c)\
  2019-05-14 23:58:56 -0700
  * [MDEV-19258](https://jira.mariadb.org/browse/MDEV-19258) RIGHT JOIN hangs in MariaDB
* [Revision #aad4e5637d](https://github.com/MariaDB/server/commit/aad4e5637d)\
  2019-05-22 12:20:02 +0300
  * Stale files cause intermittent failure when ordering is unfortunate
* [Revision #6dbc2ab8b3](https://github.com/MariaDB/server/commit/6dbc2ab8b3)\
  2019-05-20 17:44:55 +0530
  * [MDEV-17752](https://jira.mariadb.org/browse/MDEV-17752): Plan changes from hash\_index\_merge to index\_merge with new optimizer defaults
* [Revision #aaa920dad3](https://github.com/MariaDB/server/commit/aaa920dad3)\
  2019-05-21 14:54:03 +0200
  * [MDEV-19537](https://jira.mariadb.org/browse/MDEV-19537): Document mysqlimport option ignore-foreign-keys
* [Revision #91efcc6392](https://github.com/MariaDB/server/commit/91efcc6392)\
  2019-05-17 19:17:19 +0300
  * Better comment from Monty for code in make\_join\_select
* [Revision #c84f390df2](https://github.com/MariaDB/server/commit/c84f390df2)\
  2019-05-14 10:50:49 +0300
  * [MDEV-16021](https://jira.mariadb.org/browse/MDEV-16021): galera mtr test galera\_evs\_suspect\_timeout crashed
* [Revision #61469b3a3b](https://github.com/MariaDB/server/commit/61469b3a3b)\
  2019-05-13 13:23:52 +0300
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Timeout in wait\_condition.inc for PROCESSLIST
* [Revision #579c1a8c20](https://github.com/MariaDB/server/commit/579c1a8c20)\
  2019-05-13 11:31:01 +0300
  * [MDEV-17061](https://jira.mariadb.org/browse/MDEV-17061): Test failure on galera.galera\_gcs\_fc\_limit
* [Revision #70a5fb49a7](https://github.com/MariaDB/server/commit/70a5fb49a7)\
  2019-05-16 13:49:47 +0530
  * Fixed the case when statistics were not getting read because we had the statistics tables in the FROM list of the select. The statistics for tables are not read in such cases, so we need to check this case separately.
* [Revision #6ab9d1627a](https://github.com/MariaDB/server/commit/6ab9d1627a)\
  2019-05-15 01:38:28 +0530
  * [MDEV-19407](https://jira.mariadb.org/browse/MDEV-19407): Assertion \`field->table->stats\_is\_read' failed in is\_eits\_usable
* [Revision #a941e58fb8](https://github.com/MariaDB/server/commit/a941e58fb8)\
  2019-05-13 12:30:35 +0300
  * [MDEV-788](https://jira.mariadb.org/browse/MDEV-788) mysqlimport should support the ability to disable foreign keys
* [Revision #47637a3dd1](https://github.com/MariaDB/server/commit/47637a3dd1)\
  2019-05-14 13:03:06 +0530
  * [MDEV-11095](https://jira.mariadb.org/browse/MDEV-11095): rpl.rpl\_row\_mysqlbinlog test fails if row annotation enabled
* [Revision #2647fd101d](https://github.com/MariaDB/server/commit/2647fd101d)\
  2019-05-13 17:16:42 +0300
  * [MDEV-19445](https://jira.mariadb.org/browse/MDEV-19445) heap-use-after-free related to innodb\_ft\_aux\_table
* [Revision #1c97e07f8f](https://github.com/MariaDB/server/commit/1c97e07f8f)\
  2019-05-13 17:07:13 +0300
  * fts\_optimize\_words(): Remove stray output
* [Revision #c7c54ce606](https://github.com/MariaDB/server/commit/c7c54ce606)\
  2019-05-13 11:32:20 +0300
  * fts\_doc\_ids\_free(): Define inline
* [Revision #7f7211073c](https://github.com/MariaDB/server/commit/7f7211073c)\
  2019-05-13 08:48:22 +0300
  * [MDEV-19441](https://jira.mariadb.org/browse/MDEV-19441) Typo in error message "InnoDB: FTS Doc ID must be large than"
* Merge [Revision #cb248f8806](https://github.com/MariaDB/server/commit/cb248f8806) 2019-05-11 22:19:05 +0300 - Merge branch '5.5' into 10.1
* [Revision #c0ac0b8860](https://github.com/MariaDB/server/commit/c0ac0b8860)\
  2019-05-11 19:25:02 +0300
  * Update FSF address
* Merge [Revision #f177f125d4](https://github.com/MariaDB/server/commit/f177f125d4) 2019-05-11 19:15:57 +0300 - Merge branch '5.5' into 10.1
* [Revision #3e8cab51cb](https://github.com/MariaDB/server/commit/3e8cab51cb)\
  2019-05-07 12:53:50 +0530
  * [MDEV-13893](https://jira.mariadb.org/browse/MDEV-13893) encryption.innodb-redo-badkey failed in buildbot with page cannot be decrypted
* [Revision #542f32649b](https://github.com/MariaDB/server/commit/542f32649b)\
  2019-05-09 10:41:10 +0300
  * [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220): race condition in fts\_get\_table\_name()
* [Revision #f3718a112a](https://github.com/MariaDB/server/commit/f3718a112a)\
  2019-05-09 09:31:30 +0300
  * [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220): Backport some code from [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md)
* [Revision #f92749ed36](https://github.com/MariaDB/server/commit/f92749ed36)\
  2019-05-08 12:18:52 +0300
  * [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220): heap-use-after-free in fts\_get\_table\_name\_prefix()
* [Revision #5b3f7c0c33](https://github.com/MariaDB/server/commit/5b3f7c0c33)\
  2019-05-09 14:08:49 +0300
  * [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220): Remove some redundant data structures
* [Revision #06442e3e9f](https://github.com/MariaDB/server/commit/06442e3e9f)\
  2019-05-06 22:30:35 +0300
  * [MDEV-19399](https://jira.mariadb.org/browse/MDEV-19399) do not call slow my\_timer\_init() several times
* [Revision #d0ee3b5500](https://github.com/MariaDB/server/commit/d0ee3b5500)\
  2019-05-09 16:55:08 +0200
  * [MDEV-19427](https://jira.mariadb.org/browse/MDEV-19427) mysql\_upgrade\_service throws exception upgrading from 10.0 to 10.3
* [Revision #410585ca63](https://github.com/MariaDB/server/commit/410585ca63)\
  2019-05-01 15:22:22 +0400
  * Removed dead code
* [Revision #d0b73fb8d3](https://github.com/MariaDB/server/commit/d0b73fb8d3)\
  2019-03-29 19:08:22 +0400
  * [MDEV-16060](https://jira.mariadb.org/browse/MDEV-16060) - InnoDB: Failing assertion: ut\_strcmp(index->name, key->name)
* [Revision #3e5526b0df](https://github.com/MariaDB/server/commit/3e5526b0df)\
  2019-05-08 09:54:26 -0400
  * bump the VERSION
* Merge [Revision #4ad720282d](https://github.com/MariaDB/server/commit/4ad720282d) 2019-05-08 16:46:38 +0300 - Null merge mariadb-10.1.40 into 10.1
* [Revision #7b93d71a4b](https://github.com/MariaDB/server/commit/7b93d71a4b)\
  2019-05-07 15:21:41 +0530
  * [MDEV-19387](https://jira.mariadb.org/browse/MDEV-19387) innodb\_ft\_result\_cache\_limit\_32 fails on s390x
* [Revision #db9622f1f5](https://github.com/MariaDB/server/commit/db9622f1f5)\
  2019-05-07 12:51:59 +0300
  * [MDEV-19405](https://jira.mariadb.org/browse/MDEV-19405): Galera test failure on galera\_parallel\_autoinc\_largetrx
* [Revision #0573744a83](https://github.com/MariaDB/server/commit/0573744a83)\
  2019-05-06 17:15:32 +0300
  * Revert "[MDEV-19399](https://jira.mariadb.org/browse/MDEV-19399) do not call slow my\_timer\_init() several times"
* [Revision #147c1239f1](https://github.com/MariaDB/server/commit/147c1239f1)\
  2019-05-06 12:12:10 +0200
  * [MDEV-17640](https://jira.mariadb.org/browse/MDEV-17640) UMASK\_DIR configuration for mysql\_install\_db is not applied to mysql database
* [Revision #c83f837053](https://github.com/MariaDB/server/commit/c83f837053)\
  2019-04-26 14:54:44 +0300
  * [MDEV-18214](https://jira.mariadb.org/browse/MDEV-18214) remove some duplicated MONITOR counters
* [Revision #8dc670a5e8](https://github.com/MariaDB/server/commit/8dc670a5e8)\
  2019-05-06 15:38:02 +0300
  * [MDEV-19399](https://jira.mariadb.org/browse/MDEV-19399) do not call slow my\_timer\_init() several times
* [Revision #15f065599e](https://github.com/MariaDB/server/commit/15f065599e)\
  2019-05-02 14:07:24 +0300
  * [MDEV-17883](https://jira.mariadb.org/browse/MDEV-17883): CREATE TABLE IF NOT EXISTS locking changes in 10.3.10
* Merge [Revision #b85aa20065](https://github.com/MariaDB/server/commit/b85aa20065) 2019-05-02 17:23:36 +0200 - Merge branch '5.5' into 10.1
* [Revision #8cda7ab6a2](https://github.com/MariaDB/server/commit/8cda7ab6a2)\
  2019-05-02 10:17:05 -0400
  * bump the VERSION
* [Revision #ca94ce2a58](https://github.com/MariaDB/server/commit/ca94ce2a58)\
  2019-05-01 01:44:45 +0530
  * [MDEV-19352](https://jira.mariadb.org/browse/MDEV-19352): Server crash in alloc\_histograms\_for\_table\_share upon query from information schema
* [Revision #57c37e6c3f](https://github.com/MariaDB/server/commit/57c37e6c3f)\
  2019-05-01 01:19:30 +0530
  * Adjusting sql\_command to align with higher version, this is an adjustment to the patch for [MDEV-17605](https://jira.mariadb.org/browse/MDEV-17605)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
