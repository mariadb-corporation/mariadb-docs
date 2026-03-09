# MariaDB 10.0.34 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.34)[Release Notes](../../old-releases/10.0/10.0.34.md)[Changelog](mariadb-10034-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 30 Jan 2018

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.34.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #d01dbe66a8](https://github.com/MariaDB/server/commit/d01dbe66a8)\
  2018-01-27 20:37:09 +0200
  * List of unstable tests for 10.0.34 release
* [Revision #61e2f43e05](https://github.com/MariaDB/server/commit/61e2f43e05)\
  2018-01-25 19:48:36 +0200
  * Remove ut\_win\_init\_time from innodb
* [Revision #a0702dbcda](https://github.com/MariaDB/server/commit/a0702dbcda)\
  2018-01-23 11:24:53 +0100
  * [MDEV-11539](https://jira.mariadb.org/browse/MDEV-11539) test\_if\_reopen: Assertion \`strcmp(share->unique\_file\_name,filename) || share->last\_version' failed upon select from I\_S
* [Revision #1c10b256b3](https://github.com/MariaDB/server/commit/1c10b256b3)\
  2018-01-25 12:11:30 +0200
  * Port innodb\_print\_lock\_wait\_timeout\_info\_basic from Percona
* [Revision #f775ee6006](https://github.com/MariaDB/server/commit/f775ee6006)\
  2018-01-25 11:33:34 +0200
  * Fix innodb compilation failure on Windows
* [Revision #12c42bd2c7](https://github.com/MariaDB/server/commit/12c42bd2c7)\
  2018-01-24 20:21:58 +0200
  * Remove xtradb "fragmentation-statistics" patches
* Merge [Revision #a82bb5d316](https://github.com/MariaDB/server/commit/a82bb5d316) 2018-01-24 20:20:11 +0200 - Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #cd33250d2a](https://github.com/MariaDB/server/commit/cd33250d2a)\
  2018-01-23 18:04:34 +0200
  * 5.6.38-83.0
* Merge [Revision #3699a4b5c0](https://github.com/MariaDB/server/commit/3699a4b5c0) 2018-01-24 18:23:25 +0200 - Merge branch 'merge-innodb-5.6' into 10.0
* [Revision #3dfe148074](https://github.com/MariaDB/server/commit/3dfe148074)\
  2018-01-23 17:43:37 +0200
  * 5.6.39
* [Revision #d69d488b8c](https://github.com/MariaDB/server/commit/d69d488b8c)\
  2018-01-24 17:55:26 +0200
  * Remove innodb.test "keep away" comment
* [Revision #d81e41e773](https://github.com/MariaDB/server/commit/d81e41e773)\
  2018-01-24 17:54:25 +0200
  * Update Tokudb Test Results
* [Revision #fc3df561d4](https://github.com/MariaDB/server/commit/fc3df561d4)\
  2018-01-23 20:19:16 +0200
  * Make TokuDB run on 10.0
* Merge [Revision #c5f333adb6](https://github.com/MariaDB/server/commit/c5f333adb6) 2018-01-24 16:14:13 +0200 - Merge branch 'merge-tokudb-5.6' into 10.0
* [Revision #f6716cef7e](https://github.com/MariaDB/server/commit/f6716cef7e)\
  2018-01-23 19:20:10 +0200
  * 5.6.38-83.0
* [Revision #1e88e85503](https://github.com/MariaDB/server/commit/1e88e85503)\
  2018-01-24 16:12:52 +0200
  * Squashed commit of connect/10.0:
* [Revision #b20f821e07](https://github.com/MariaDB/server/commit/b20f821e07)\
  2018-01-24 15:18:36 +0200
  * Fix Innodb ASAN error on init
* Merge [Revision #d833bb65d5](https://github.com/MariaDB/server/commit/d833bb65d5) 2018-01-24 12:29:31 +0200 - Merge remote-tracking branch '5.5' into 10.0
* [Revision #76577e1e26](https://github.com/MariaDB/server/commit/76577e1e26)\
  2018-01-24 10:58:27 +0100
  * typo fix
* [Revision #e2da680c51](https://github.com/MariaDB/server/commit/e2da680c51)\
  2018-01-23 23:19:09 +0100
  * [MDEV-13187](https://jira.mariadb.org/browse/MDEV-13187) incorrect backslash parsing in clients
* [Revision #8637931f11](https://github.com/MariaDB/server/commit/8637931f11)\
  2018-01-23 19:29:12 +0200
  * Add ASAN instrumentation (and more strict Valgrind) to InnoDB
* [Revision #70a9b12de9](https://github.com/MariaDB/server/commit/70a9b12de9)\
  2018-01-23 18:08:55 +0200
  * Silence -Wimplicit-fallthrough
* [Revision #ba8d0fa700](https://github.com/MariaDB/server/commit/ba8d0fa700)\
  2018-01-15 14:50:35 +0100
  * [MDEV-14786](https://jira.mariadb.org/browse/MDEV-14786): Server crashes in Item\_cond::transform on 2nd execution of SP querying from a view
* [Revision #11408a69ad](https://github.com/MariaDB/server/commit/11408a69ad)\
  2018-01-21 23:44:31 +0100
  * Fix Item tree changes/rollback debug print
* [Revision #94da1cb4a6](https://github.com/MariaDB/server/commit/94da1cb4a6)\
  2018-01-23 15:47:54 +0530
  * [MDEV-14586](https://jira.mariadb.org/browse/MDEV-14586) Assertion \`0' failed in retrieve\_auto\_increment ...
* [Revision #cc3155415e](https://github.com/MariaDB/server/commit/cc3155415e)\
  2018-01-19 19:52:01 +1100
  * [MDEV-5510](https://jira.mariadb.org/browse/MDEV-5510): Replace MySQL -> MariaDB in init scripts
* [Revision #701c7e777f](https://github.com/MariaDB/server/commit/701c7e777f)\
  2018-01-23 11:56:52 +0100
  * Fix error message typo
* [Revision #9ee372736f](https://github.com/MariaDB/server/commit/9ee372736f)\
  2018-01-23 07:37:00 +1100
  * mysql\_install\_db: correct hosting/source/maillist information
* [Revision #c98906e4fe](https://github.com/MariaDB/server/commit/c98906e4fe)\
  2018-01-23 07:35:38 +1100
  * mysql\_install\_db: correct --skip-grant-tables help
* [Revision #3532a421f6](https://github.com/MariaDB/server/commit/3532a421f6)\
  2018-01-23 11:57:54 +0300
  * fix build for recent clang
* [Revision #a04b07eb34](https://github.com/MariaDB/server/commit/a04b07eb34)\
  2018-01-22 23:51:32 +0200
  * Fix TokuDB Not building
* [Revision #8539e4b1b6](https://github.com/MariaDB/server/commit/8539e4b1b6)\
  2018-01-22 13:39:59 +0100
  * improve ASAN instrumentation: clang
* [Revision #b20c3dc664](https://github.com/MariaDB/server/commit/b20c3dc664)\
  2018-01-21 21:18:57 +0200
  * [MDEV-14715](https://jira.mariadb.org/browse/MDEV-14715): Assertion \`!table || (!table->read\_set... failed in Field\_num::val\_decimal
* [Revision #6d826e3d7e](https://github.com/MariaDB/server/commit/6d826e3d7e)\
  2018-01-21 13:12:33 +0200
  * Remove commented out code post merge fix in 2011
* [Revision #03eb15933d](https://github.com/MariaDB/server/commit/03eb15933d)\
  2018-01-21 20:48:59 +0100
  * improve ASAN instrumentation: InnoDB/XtraDB
* [Revision #d9c460b84e](https://github.com/MariaDB/server/commit/d9c460b84e)\
  2018-01-21 15:08:33 +0100
  * Finally! Make './mtr --valgrind-mysqld --gdb' to work.
* [Revision #f2408e7e6a](https://github.com/MariaDB/server/commit/f2408e7e6a)\
  2018-01-20 17:59:37 +0100
  * Free memory in unit tests. Makes ASAN happier.
* [Revision #36eb0b7a55](https://github.com/MariaDB/server/commit/36eb0b7a55)\
  2018-01-21 12:50:49 +0100
  * improve ASAN instrumentation: table->record\[0]
* [Revision #fa331acefd](https://github.com/MariaDB/server/commit/fa331acefd)\
  2018-01-21 11:30:02 +0100
  * improve ASAN instrumentation: mtr
* [Revision #dc28b6d180](https://github.com/MariaDB/server/commit/dc28b6d180)\
  2018-01-21 12:53:17 +0100
  * improve ASAN instrumentation: MEM\_ROOT
* [Revision #a966d422ca](https://github.com/MariaDB/server/commit/a966d422ca)\
  2018-01-20 12:50:28 +0100
  * improve ASAN instrumentation: TRASH
* [Revision #22ae3843db](https://github.com/MariaDB/server/commit/22ae3843db)\
  2018-01-20 17:59:11 +0100
  * Correct TRASH() macro usage
* [Revision #204cb85aab](https://github.com/MariaDB/server/commit/204cb85aab)\
  2018-01-20 11:45:23 +0100
  * Fix compilation without dlopen
* [Revision #906ce0962d](https://github.com/MariaDB/server/commit/906ce0962d)\
  2018-01-22 11:18:10 +0200
  * [MDEV-7049](https://jira.mariadb.org/browse/MDEV-7049) MySQL#74585 - InnoDB: Failing assertion: \*mbmaxlen < 5 in file ha\_innodb.cc line 1904
* [Revision #6c60c809bb](https://github.com/MariaDB/server/commit/6c60c809bb)\
  2018-01-19 18:04:51 +0200
  * Add dummy defintion for Dl\_info in case we're missing dladdr
* [Revision #17f64b362a](https://github.com/MariaDB/server/commit/17f64b362a)\
  2018-01-19 11:01:32 -0500
  * bump the VERSION
* [Revision #26e5f9dda1](https://github.com/MariaDB/server/commit/26e5f9dda1)\
  2018-01-16 22:57:52 +0200
  * [MDEV-14229](https://jira.mariadb.org/browse/MDEV-14229): Stack trace is not resolved for shared objects
* [Revision #a7a4519a40](https://github.com/MariaDB/server/commit/a7a4519a40)\
  2018-01-19 13:29:31 +0530
  * [MDEV-14241](https://jira.mariadb.org/browse/MDEV-14241): Server crash in key\_copy / get\_matching\_chain\_by\_join\_key or valgrind warnings
* [Revision #4f96b401d9](https://github.com/MariaDB/server/commit/4f96b401d9)\
  2018-01-18 09:20:55 -0800
  * Fixed [MDEV-14960](https://jira.mariadb.org/browse/MDEV-14960) \[ERROR] mysqld got signal 11 with join\_buffer and join\_cache
* [Revision #e431d90065](https://github.com/MariaDB/server/commit/e431d90065)\
  2018-01-24 09:57:18 +0200
  * Update sponsors
* [Revision #d0acfa458e](https://github.com/MariaDB/server/commit/d0acfa458e)\
  2018-01-23 23:48:57 +0200
  * [MDEV-14245](https://jira.mariadb.org/browse/MDEV-14245) tokudb\_alter\_table.drop\_add\_pk\_part\_104 fails
* [Revision #d5d0c62459](https://github.com/MariaDB/server/commit/d5d0c62459)\
  2018-01-23 19:21:58 +0200
  * Fixed a few compiler warnings
* [Revision #b3c7cf81e3](https://github.com/MariaDB/server/commit/b3c7cf81e3)\
  2018-01-23 19:21:44 +0200
  * Fix for [MDEV-14141](https://jira.mariadb.org/browse/MDEV-14141) Crash in print\_keydup\_error()
* [Revision #a4663af05c](https://github.com/MariaDB/server/commit/a4663af05c)\
  2018-01-22 16:53:10 +0100
  * [MDEV-7533](https://jira.mariadb.org/browse/MDEV-7533): COLUMN\_JSON() doesn't escape control characters in string values
* [Revision #ea78c5744b](https://github.com/MariaDB/server/commit/ea78c5744b)\
  2018-01-22 20:10:57 +0100
  * [MDEV-13988](https://jira.mariadb.org/browse/MDEV-13988) connect.drop-open-error fails
* [Revision #431607237d](https://github.com/MariaDB/server/commit/431607237d)\
  2018-01-22 16:50:20 +0200
  * [MDEV-12173](https://jira.mariadb.org/browse/MDEV-12173) "Error: trying to do an operation on a dropped tablespace"
* [Revision #5e87f49a99](https://github.com/MariaDB/server/commit/5e87f49a99)\
  2018-01-18 09:29:49 +0200
  * Make row\_mysql\_table\_id\_reassign() static
* Merge [Revision #4c1479545d](https://github.com/MariaDB/server/commit/4c1479545d) 2018-01-11 10:16:38 +0200 - Merge 5.5 into 10.0
* [Revision #c903ba2f1e](https://github.com/MariaDB/server/commit/c903ba2f1e)\
  2018-01-08 14:24:04 +0200
  * [MDEV-13205](https://jira.mariadb.org/browse/MDEV-13205) InnoDB: Failing assertion: !dict\_index\_is\_online\_ddl(index) upon ALTER TABLE
* [Revision #4496fd71f4](https://github.com/MariaDB/server/commit/4496fd71f4)\
  2018-01-04 20:38:42 +0200
  * Fix a truncation warning introduced in [MDEV-12323](https://jira.mariadb.org/browse/MDEV-12323)
* Merge [Revision #8ac1982fcc](https://github.com/MariaDB/server/commit/8ac1982fcc) 2018-01-03 20:40:41 +0200 - Merge 5.5 into 10.0
* Merge [Revision #51e4650ed0](https://github.com/MariaDB/server/commit/51e4650ed0) 2018-01-02 21:52:46 +0200 - Merge 5.5 into 10.0
* [Revision #eef2bc5a5c](https://github.com/MariaDB/server/commit/eef2bc5a5c)\
  2017-12-28 17:13:42 +0200
  * Update mysqladmin man page
* [Revision #4b8cd4536a](https://github.com/MariaDB/server/commit/4b8cd4536a)\
  2017-12-22 14:03:25 +0400
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626) Merge InnoDB test cases from MySQL 5.7
* [Revision #24efee9100](https://github.com/MariaDB/server/commit/24efee9100)\
  2017-12-21 18:00:24 +0200
  * Follow up to [MDEV-12366](https://jira.mariadb.org/browse/MDEV-12366): FLUSH privileges can break hierarchy of roles
* [Revision #0202e47274](https://github.com/MariaDB/server/commit/0202e47274)\
  2017-12-21 17:19:13 +0200
  * [MDEV-12827](https://jira.mariadb.org/browse/MDEV-12827) Assertion failure when reporting duplicate key error in online table rebuild
* Merge [Revision #042f763268](https://github.com/MariaDB/server/commit/042f763268) 2017-12-20 12:51:57 +0200 - Merge remote-tracking branch '5.5' into 10.0
* [Revision #cb121a047b](https://github.com/MariaDB/server/commit/cb121a047b)\
  2017-12-20 13:49:27 +0400
  * An after-fix for [MDEV-14008](https://jira.mariadb.org/browse/MDEV-14008) Assertion failing: \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())
* [Revision #f7f5c710e4](https://github.com/MariaDB/server/commit/f7f5c710e4)\
  2017-12-20 09:21:08 +0200
  * Correct a function comment
* [Revision #be758322e2](https://github.com/MariaDB/server/commit/be758322e2)\
  2017-12-17 18:33:22 +0200
  * [MDEV-12366](https://jira.mariadb.org/browse/MDEV-12366): FLUSH PRIVILEGES can break hierarchy of roles
* [Revision #2fced9e7b6](https://github.com/MariaDB/server/commit/2fced9e7b6)\
  2017-12-16 11:56:16 +0200
  * [MDEV-13655](https://jira.mariadb.org/browse/MDEV-13655): Set role does not properly grant privileges.
* [Revision #40088bfc7e](https://github.com/MariaDB/server/commit/40088bfc7e)\
  2017-12-18 19:46:23 +0200
  * [MDEV-13407](https://jira.mariadb.org/browse/MDEV-13407) innodb.drop\_table\_background failed in buildbot with "Tablespace for table exists"
* [Revision #03e91ce324](https://github.com/MariaDB/server/commit/03e91ce324)\
  2017-12-15 16:38:46 +0100
  * [MDEV-14641](https://jira.mariadb.org/browse/MDEV-14641) Incompatible key or row definition between the MariaDB .frm file and the information in the storage engine
* [Revision #c1e5fef05d](https://github.com/MariaDB/server/commit/c1e5fef05d)\
  2017-12-18 11:25:38 +0400
  * [MDEV-14008](https://jira.mariadb.org/browse/MDEV-14008) Assertion failing: \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())
* [Revision #9d76b27498](https://github.com/MariaDB/server/commit/9d76b27498)\
  2017-12-13 22:30:13 +0200
  * Follow-up fix for [MDEV-12352](https://jira.mariadb.org/browse/MDEV-12352): Plug a memory leak
* [Revision #b1977a39de](https://github.com/MariaDB/server/commit/b1977a39de)\
  2017-12-13 18:56:22 +0200
  * [MDEV-12323](https://jira.mariadb.org/browse/MDEV-12323) Rollback progress log messages during crash recovery are intermixed with unrelated log messages
* [Revision #08d0ea1fcf](https://github.com/MariaDB/server/commit/08d0ea1fcf)\
  2017-12-13 18:53:46 +0200
  * Follow-up to [MDEV-11027](https://jira.mariadb.org/browse/MDEV-11027): Use recv\_sys\_t::report()
* [Revision #b46fa627ca](https://github.com/MariaDB/server/commit/b46fa627ca)\
  2017-12-13 18:02:09 +0200
  * [MDEV-12352](https://jira.mariadb.org/browse/MDEV-12352) InnoDB shutdown should not be blocked by a large transaction rollback
* [Revision #6559ba71a5](https://github.com/MariaDB/server/commit/6559ba71a5)\
  2017-12-13 16:18:08 +0200
  * [MDEV-13797](https://jira.mariadb.org/browse/MDEV-13797) InnoDB may hang if shutdown is initiated soon after startup while rolling back recovered incomplete transactions
* [Revision #622466644d](https://github.com/MariaDB/server/commit/622466644d)\
  2017-11-20 11:00:44 +0200
  * mysql\_uprade --help and man page fixes
* [Revision #d8ccc61f76](https://github.com/MariaDB/server/commit/d8ccc61f76)\
  2017-11-16 14:03:02 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #93326ef051](https://github.com/MariaDB/server/commit/93326ef051)\
  2017-11-16 13:21:07 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #923ea5dbf6](https://github.com/MariaDB/server/commit/923ea5dbf6)\
  2017-11-16 13:18:22 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #02e35ef5f2](https://github.com/MariaDB/server/commit/02e35ef5f2)\
  2017-11-15 15:52:03 +0400
  * [MDEV-12681](https://jira.mariadb.org/browse/MDEV-12681) Wrong VIEW results for CHAR(0xDF USING latin1)
* [Revision #ea1739f90d](https://github.com/MariaDB/server/commit/ea1739f90d)\
  2017-11-14 11:29:52 +0300
  * removed garbase struct member
* [Revision #2913f615f0](https://github.com/MariaDB/server/commit/2913f615f0)\
  2017-11-13 16:30:02 +0100
  * [MDEV-8949](https://jira.mariadb.org/browse/MDEV-8949): COLUMN\_CREATE unicode name breakage
* [Revision #c0e10f375a](https://github.com/MariaDB/server/commit/c0e10f375a)\
  2017-11-10 09:07:45 +0200
  * Fix a -Wimplicit-fallthrough warning
* [Revision #56394a78e3](https://github.com/MariaDB/server/commit/56394a78e3)\
  2017-11-03 12:33:01 +0100
  * [MDEV-12372](https://jira.mariadb.org/browse/MDEV-12372) mysqlbinlog --version output is the same on 10.x as on 5.5.x, and contains not only version
* [Revision #c97a7cdbd0](https://github.com/MariaDB/server/commit/c97a7cdbd0)\
  2017-11-09 20:51:11 +0100
  * remove redundant tests from mysql-test/include/\*.inc files
* [Revision #7ec6c6fa62](https://github.com/MariaDB/server/commit/7ec6c6fa62)\
  2017-10-22 21:29:31 +0200
  * typo
* Merge [Revision #3028357aa5](https://github.com/MariaDB/server/commit/3028357aa5) 2017-11-09 20:33:23 +0100 - Merge branch '5.5' into 10.0
* [Revision #c2c93fc6e4](https://github.com/MariaDB/server/commit/c2c93fc6e4)\
  2017-11-08 15:47:49 +0100
  * [MDEV-14164](https://jira.mariadb.org/browse/MDEV-14164): Unknown column error when adding aggregate to function in oracle style procedure FOR loop
* [Revision #ca695888e0](https://github.com/MariaDB/server/commit/ca695888e0)\
  2017-11-07 21:57:42 +0400
  * [MDEV-14116](https://jira.mariadb.org/browse/MDEV-14116) INET6\_NTOA output is set as null to varchar(39) variable
* [Revision #6a524fcfdd](https://github.com/MariaDB/server/commit/6a524fcfdd)\
  2017-11-06 14:55:34 +0200
  * [MDEV-14140](https://jira.mariadb.org/browse/MDEV-14140) IMPORT TABLESPACE must not go beyond FSP\_FREE\_LIMIT
* [Revision #bfde65c0ae](https://github.com/MariaDB/server/commit/bfde65c0ae)\
  2017-11-04 02:39:16 +0200
  * [MDEV-10651](https://jira.mariadb.org/browse/MDEV-10651), [MDEV-14196](https://jira.mariadb.org/browse/MDEV-14196) sys\_vars.innodb\_buffer\_pool\_\* tests fail
* [Revision #5e5adfa729](https://github.com/MariaDB/server/commit/5e5adfa729)\
  2017-11-01 18:40:09 +0200
  * [MDEV-14029](https://jira.mariadb.org/browse/MDEV-14029) Server does not remove #sql\*.frm files after crash during ALTER TABLE
* [Revision #0ed5c09b28](https://github.com/MariaDB/server/commit/0ed5c09b28)\
  2017-11-01 19:57:47 +0200
  * [MDEV-11864](https://jira.mariadb.org/browse/MDEV-11864) main.view test uses CHECK PARTITION but does not check for the partition plugin
* [Revision #1394ea6965](https://github.com/MariaDB/server/commit/1394ea6965)\
  2017-11-03 22:36:58 +0400
  * [MDEV-13921](https://jira.mariadb.org/browse/MDEV-13921) Audit log writes invalid SQL if single-line comments are present.
* [Revision #04daf30e9b](https://github.com/MariaDB/server/commit/04daf30e9b)\
  2017-11-03 17:05:41 +0400
  * [MDEV-13921](https://jira.mariadb.org/browse/MDEV-13921) Audit log writes invalid SQL if single-line comments are present.
* [Revision #c4c48e9740](https://github.com/MariaDB/server/commit/c4c48e9740)\
  2017-03-07 19:21:42 +0100
  * [MDEV-11965](https://jira.mariadb.org/browse/MDEV-11965) -Werror should not appear in released tarballs
* [Revision #d11001d11b](https://github.com/MariaDB/server/commit/d11001d11b)\
  2017-10-27 11:36:32 +0300
  * Backport [MDEV-13890](https://jira.mariadb.org/browse/MDEV-13890) from 10.2 (InnoDB/XtraDB shutdown failure)
* [Revision #2b332ab795](https://github.com/MariaDB/server/commit/2b332ab795)\
  2017-10-30 12:31:40 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
