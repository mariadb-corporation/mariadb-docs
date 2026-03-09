# MariaDB 10.5.13 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.13](https://mariadb.org/download/?tab=mariadb\&release=10.5.13\&product=mariadb)[Release Notes](../../old-releases/10.5/10.5.13.md)[Changelog](mariadb-10513-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 8 Nov 2021

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.13.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.22](../changelogs-mariadb-10-4-series/mariadb-10422-changelog.md)
* Merge [Revision #8635be6a29](https://github.com/MariaDB/server/commit/8635be6a29) 2021-11-05 20:33:57 +0100 - Merge branch '10.4' into 10.5
* [Revision #8d7196cdf1](https://github.com/MariaDB/server/commit/8d7196cdf1)\
  2021-11-05 00:02:34 +0100
  * change pcre2 download url
* Merge [Revision #bc82c622c4](https://github.com/MariaDB/server/commit/bc82c622c4) 2021-11-03 14:07:38 +0100 - Merge branch '10.4' into 10.5
* Merge [Revision #e26b30d1bb](https://github.com/MariaDB/server/commit/e26b30d1bb) 2021-11-02 15:35:31 +0100 - Merge branch '10.4' into 10.5
* [Revision #7846c56fbe](https://github.com/MariaDB/server/commit/7846c56fbe)\
  2021-11-01 13:07:55 +0200
  * [MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) Server hang due to Galera lock conflict resolution
* Merge [Revision #cb5b3230d8](https://github.com/MariaDB/server/commit/cb5b3230d8) 2021-10-30 10:41:42 +0200 - Merge branch '10.4' into 10.5
* [Revision #ef2dbb8dbc](https://github.com/MariaDB/server/commit/ef2dbb8dbc)\
  2021-10-21 14:49:51 +0300
  * [MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) Server hang due to Galera lock conflict resolution
* [Revision #d5bc05798f](https://github.com/MariaDB/server/commit/d5bc05798f)\
  2021-10-28 11:25:15 +0300
  * [MDEV-25114](https://jira.mariadb.org/browse/MDEV-25114): Crash: WSREP: invalid state ROLLED\_BACK (FATAL)
* [Revision #1974df01d5](https://github.com/MariaDB/server/commit/1974df01d5)\
  2021-10-29 12:19:34 +0200
  * columnstore-5.6.3-2
* Merge [Revision #1c1396f09c](https://github.com/MariaDB/server/commit/1c1396f09c) 2021-10-29 10:21:52 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #a8ded39557](https://github.com/MariaDB/server/commit/a8ded39557) 2021-10-28 08:48:36 +0300 - Merge 10.4 into 10.5
* Merge [Revision #f7bd369973](https://github.com/MariaDB/server/commit/f7bd369973) 2021-10-27 13:29:16 +0300 - Merge 10.4 into 10.5
* Merge [Revision #44f9736e0b](https://github.com/MariaDB/server/commit/44f9736e0b) 2021-10-27 09:48:22 +0300 - Merge 10.4 into 10.5
* [Revision #49098bfd49](https://github.com/MariaDB/server/commit/49098bfd49)\
  2021-10-07 20:58:18 +0400
  * [MDEV-26732](https://jira.mariadb.org/browse/MDEV-26732) Assertion \`0' failed in Item::val\_native
* [Revision #395a033237](https://github.com/MariaDB/server/commit/395a033237)\
  2021-06-21 14:02:17 +0200
  * [MDEV-22552](https://jira.mariadb.org/browse/MDEV-22552): mytop packaging
* [Revision #2011fcf87d](https://github.com/MariaDB/server/commit/2011fcf87d)\
  2020-05-31 14:40:22 +0200
  * [MDEV-22552](https://jira.mariadb.org/browse/MDEV-22552): mytop packaging
* Merge [Revision #f1ba07a044](https://github.com/MariaDB/server/commit/f1ba07a044) 2021-10-21 18:09:17 +0300 - Merge 10.4 into 10.5
* [Revision #a0fda162eb](https://github.com/MariaDB/server/commit/a0fda162eb)\
  2021-10-21 15:31:21 +0300
  * Fix GCC 11.2.0 -m32 (IA-32) warnings
* Merge [Revision #5f8561a6bc](https://github.com/MariaDB/server/commit/5f8561a6bc) 2021-10-21 15:26:25 +0300 - Merge 10.4 into 10.5
* [Revision #3c2ab896b9](https://github.com/MariaDB/server/commit/3c2ab896b9)\
  2021-10-18 18:51:04 +0300
  * [MDEV-19129](https://jira.mariadb.org/browse/MDEV-19129): Xcode compatibility update: update libmariadb submodule
* [Revision #e7208bd934](https://github.com/MariaDB/server/commit/e7208bd934)\
  2021-09-21 20:22:56 +0900
  * [MDEV-26158](https://jira.mariadb.org/browse/MDEV-26158) SIGSEGV in spider\_free\_mem from ha\_spider::open on INSERT
* [Revision #edde9084c2](https://github.com/MariaDB/server/commit/edde9084c2)\
  2021-09-24 23:58:06 +0900
  * [MDEV-26582](https://jira.mariadb.org/browse/MDEV-26582) SIGSEGV in spider\_db\_bulk\_insert and spider\_db\_connect and spider\_db\_before\_query, and hang in "End of update loop" / "Reset for next command" query states
* [Revision #18eab4a832](https://github.com/MariaDB/server/commit/18eab4a832)\
  2021-10-18 12:49:10 +0300
  * [MDEV-26682](https://jira.mariadb.org/browse/MDEV-26682) Replication timeouts with XA PREPARE
* [Revision #9068020efe](https://github.com/MariaDB/server/commit/9068020efe)\
  2021-09-21 18:32:37 +0900
  * [MDEV-26539](https://jira.mariadb.org/browse/MDEV-26539) SIGSEGV in spider\_check\_and\_set\_trx\_isolation and I\_P\_List\_iterator from THD::drop\_temporary\_table (10.5.3 opt only) on ALTER
* [Revision #052dda61bb](https://github.com/MariaDB/server/commit/052dda61bb)\
  2021-10-17 12:36:12 +0300
  * Made optional Json\_writer\_object / Json\_writer\_array consistency check
* [Revision #cf8e78a401](https://github.com/MariaDB/server/commit/cf8e78a401)\
  2021-10-16 02:35:16 +0300
  * Implemented Json\_writer\_array & Json\_writer\_object subitems name presence control
* [Revision #df38304342](https://github.com/MariaDB/server/commit/df38304342)\
  2021-10-14 08:37:23 +0400
  * [MDEV-26742](https://jira.mariadb.org/browse/MDEV-26742) Assertion \`field->type\_handler() == this' failed in FixedBinTypeBundle\<NATIVE\_LEN, MAX\_CHAR\_LEN>::Type\_handler\_fbt::stored\_field\_cmp\_to\_item
* [Revision #bd1573b0f3](https://github.com/MariaDB/server/commit/bd1573b0f3)\
  2021-10-06 11:31:08 +0300
  * Xcode compatibility update: pcre, mysql-test-run.pl
* [Revision #d2b4d3ada0](https://github.com/MariaDB/server/commit/d2b4d3ada0)\
  2021-10-13 17:57:31 +0300
  * [MDEV-26707](https://jira.mariadb.org/browse/MDEV-26707): SR transaction rolls back locally, but not in cluster
* [Revision #f1acd9f14b](https://github.com/MariaDB/server/commit/f1acd9f14b)\
  2021-10-13 15:16:23 +0300
  * [MDEV-26819](https://jira.mariadb.org/browse/MDEV-26819) SET GLOBAL innodb\_max\_dirty\_pages\_pct=0 occasionally fails to trigger writes
* [Revision #ddf95e834d](https://github.com/MariaDB/server/commit/ddf95e834d)\
  2021-10-13 14:44:28 +0300
  * [MDEV-26707](https://jira.mariadb.org/browse/MDEV-26707): SR transaction rolls back locally, but not in cluster
* [Revision #ae098b49dd](https://github.com/MariaDB/server/commit/ae098b49dd)\
  2021-10-13 13:35:49 +0300
  * [MDEV-24062](https://jira.mariadb.org/browse/MDEV-24062): : Galera test failure on galera\_var\_replicate\_myisam\_on
* [Revision #aae72f821a](https://github.com/MariaDB/server/commit/aae72f821a)\
  2021-10-13 12:49:52 +0300
  * [MDEV-24062](https://jira.mariadb.org/browse/MDEV-24062): Re-disable the test after merge
* Merge [Revision #99bb3fb656](https://github.com/MariaDB/server/commit/99bb3fb656) 2021-10-13 12:33:56 +0300 - Merge 10.4 into 10.5
* [Revision #cda072bb4b](https://github.com/MariaDB/server/commit/cda072bb4b)\
  2020-12-30 10:08:23 +0200
  * Deb: Sync build and runtime dependencies from downstream to upstream
* [Revision #9bb6520622](https://github.com/MariaDB/server/commit/9bb6520622)\
  2020-12-21 20:42:52 +0200
  * Deb: Correctly install test\_sql\_service.so
* Merge [Revision #4eb7217ec3](https://github.com/MariaDB/server/commit/4eb7217ec3) 2021-10-06 09:45:12 +0300 - Merge 10.4 into 10.5
* [Revision #48f1b6946e](https://github.com/MariaDB/server/commit/48f1b6946e)\
  2021-10-06 07:09:24 +0300
  * Update libmariadb
* [Revision #1146b5cb58](https://github.com/MariaDB/server/commit/1146b5cb58)\
  2021-10-05 16:49:30 +0300
  * [MDEV-26761](https://jira.mariadb.org/browse/MDEV-26761): main.mysql\_client\_test fails with MemorySanitizer
* [Revision #df94aa344b](https://github.com/MariaDB/server/commit/df94aa344b)\
  2021-10-05 07:13:14 +0300
  * [MDEV-26445](https://jira.mariadb.org/browse/MDEV-26445) followup: Try to work around GCC 4.8.5 ICE on ARMv8
* Merge [Revision #ead38354e6](https://github.com/MariaDB/server/commit/ead38354e6) 2021-10-04 19:32:13 +0300 - Merge 10.4 into 10.5
* [Revision #f3bd278063](https://github.com/MariaDB/server/commit/f3bd278063)\
  2021-10-04 19:28:43 +0300
  * [MDEV-22083](https://jira.mariadb.org/browse/MDEV-22083)/[MDEV-26758](https://jira.mariadb.org/browse/MDEV-26758): Fix uninitialized memory in mysql\_client\_test
* [Revision #32839c4df2](https://github.com/MariaDB/server/commit/32839c4df2)\
  2021-10-04 22:31:05 +1100
  * [MDEV-19867](https://jira.mariadb.org/browse/MDEV-19867): postfix - syntax spelling ALTER TABLE
* [Revision #98a7fa0ce7](https://github.com/MariaDB/server/commit/98a7fa0ce7)\
  2021-10-02 11:14:14 +0300
  * [MDEV-26720](https://jira.mariadb.org/browse/MDEV-26720): optimize rw\_lock for IA-32, AMD64
* [Revision #be803f037f](https://github.com/MariaDB/server/commit/be803f037f)\
  2021-09-30 10:01:10 +0300
  * [MDEV-25215](https://jira.mariadb.org/browse/MDEV-25215) Excessive logging "InnoDB: Cannot close file"
* Merge [Revision #064cb58efe](https://github.com/MariaDB/server/commit/064cb58efe) 2021-09-30 09:04:43 +0300 - Merge 10.4 into 10.5
* [Revision #e5a9dcfda2](https://github.com/MariaDB/server/commit/e5a9dcfda2)\
  2021-09-28 22:25:47 +0200
  * [MDEV-23306](https://jira.mariadb.org/browse/MDEV-23306) Fix build dependency
* [Revision #690c472591](https://github.com/MariaDB/server/commit/690c472591)\
  2021-09-27 15:09:50 +0300
  * [MDEV-21613](https://jira.mariadb.org/browse/MDEV-21613) : galera\_sr.GCF-1018B MTR failed: Failed to open table mysql.wsrep\_streaming\_log for writing
* Merge [Revision #83c4523f03](https://github.com/MariaDB/server/commit/83c4523f03) 2021-09-24 17:32:50 +0300 - Merge 10.4 into 10.5
* Merge [Revision #88f38661b7](https://github.com/MariaDB/server/commit/88f38661b7) 2021-09-24 12:14:35 +0300 - Merge 10.4 into 10.5
* Merge [Revision #7e2b42324c](https://github.com/MariaDB/server/commit/7e2b42324c) 2021-09-24 08:42:23 +0300 - Merge 10.4 into 10.5
* [Revision #f5794e1dc6](https://github.com/MariaDB/server/commit/f5794e1dc6)\
  2021-09-24 08:24:03 +0300
  * [MDEV-26445](https://jira.mariadb.org/browse/MDEV-26445) innodb\_undo\_log\_truncate is unnecessarily slow
* [Revision #f5fddae3cb](https://github.com/MariaDB/server/commit/f5fddae3cb)\
  2021-09-24 08:22:19 +0300
  * [MDEV-26450](https://jira.mariadb.org/browse/MDEV-26450): Corruption due to innodb\_undo\_log\_truncate
* [Revision #15efb7ed48](https://github.com/MariaDB/server/commit/15efb7ed48)\
  2021-09-22 16:40:47 +0300
  * [MDEV-26626](https://jira.mariadb.org/browse/MDEV-26626) fixup: Do not advance checkpoint during startup
* [Revision #7d360060cb](https://github.com/MariaDB/server/commit/7d360060cb)\
  2021-09-21 22:40:47 +0700
  * [MDEV-24629](https://jira.mariadb.org/browse/MDEV-24629) mariadb-connector-c-config conflicts with MariaDB's MariaDB-common-10.5.8-1.fc32.x86\_64.rpm
* [Revision #edabb12509](https://github.com/MariaDB/server/commit/edabb12509)\
  2021-09-13 17:43:23 +0200
  * [MDEV-21286](https://jira.mariadb.org/browse/MDEV-21286): bison warnings on ubuntu 20.04 on deprecated directive in sql\_yacc.yy
* [Revision #de2b5795f4](https://github.com/MariaDB/server/commit/de2b5795f4)\
  2021-09-20 14:23:58 +0200
  * Remove mention of Freenode
* [Revision #b4074069b2](https://github.com/MariaDB/server/commit/b4074069b2)\
  2021-09-21 19:14:07 +0200
  * [MDEV-26657](https://jira.mariadb.org/browse/MDEV-26657) : Initialize some fields in create\_background\_thd()
* Merge [Revision #699de65d5e](https://github.com/MariaDB/server/commit/699de65d5e) 2021-09-17 19:57:13 +0300 - Merge 10.4 into 10.5
* [Revision #c430aa72ab](https://github.com/MariaDB/server/commit/c430aa72ab)\
  2021-09-16 20:10:42 +0300
  * [MDEV-26626](https://jira.mariadb.org/browse/MDEV-26626) InnoDB fails to advance the log checkpoint
* [Revision #65cce297be](https://github.com/MariaDB/server/commit/65cce297be)\
  2021-09-16 14:06:29 +0300
  * Updated rocksdb test result
* [Revision #0d47945b58](https://github.com/MariaDB/server/commit/0d47945b58)\
  2021-09-15 21:21:03 +0300
  * Fixed bug in aria\_chk that overwrote sort\_buffer\_length
* Merge [Revision #b4f24c745a](https://github.com/MariaDB/server/commit/b4f24c745a) 2021-09-15 20:23:07 +0300 - Merge branch '10.4' into 10.5
* [Revision #f03fee06b0](https://github.com/MariaDB/server/commit/f03fee06b0)\
  2021-09-15 19:18:11 +0300
  * Improve error messages from Aria
* [Revision #6be0ddae5e](https://github.com/MariaDB/server/commit/6be0ddae5e)\
  2021-09-15 19:16:37 +0300
  * Fixed compiler warnings in CONNECT
* [Revision #07abcb5045](https://github.com/MariaDB/server/commit/07abcb5045)\
  2021-09-05 20:22:45 -0700
  * Deb: Fix Gitlab-CI/Salsa-CI builds failures
* [Revision #1a6c130c4f](https://github.com/MariaDB/server/commit/1a6c130c4f)\
  2021-09-12 15:23:34 +0200
  * perfschema: use correct type for left shifts
* Merge [Revision #42e9506ce9](https://github.com/MariaDB/server/commit/42e9506ce9) 2021-09-11 17:19:36 +0200 - Merge branch '10.4' into 10.5
* [Revision #e42da92265](https://github.com/MariaDB/server/commit/e42da92265)\
  2021-09-11 16:48:33 +0200
  * Use mariadb- named targets for minbuild
* [Revision #cef656b11c](https://github.com/MariaDB/server/commit/cef656b11c)\
  2021-09-11 16:47:30 +0200
  * Fix Windows warnings and tests for -DPLUGIN\_PERFSCHEMA=NO
* Merge [Revision #c3341f8440](https://github.com/MariaDB/server/commit/c3341f8440) 2021-09-11 16:40:08 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #c7a721ee33](https://github.com/MariaDB/server/commit/c7a721ee33) 2021-09-11 16:22:55 +0200 - Merge branch '10.3' into 10.4
* [Revision #40b743f99e](https://github.com/MariaDB/server/commit/40b743f99e)\
  2021-09-11 11:49:36 +0200
  * remove redundant select in the perfschema.show\_aggregate test
* [Revision #b42158be53](https://github.com/MariaDB/server/commit/b42158be53)\
  2021-08-25 18:55:56 +0200
  * remove unused result file
* Merge [Revision #2d0847818d](https://github.com/MariaDB/server/commit/2d0847818d) 2021-09-11 11:49:12 +0300 - Merge 10.4 into 10.5
* [Revision #f99cc0d2fc](https://github.com/MariaDB/server/commit/f99cc0d2fc)\
  2021-09-11 11:45:17 +0300
  * Merge fixup 7c33ecb6651fb80f46bf9f3d8fee2e2f2b70995d
* [Revision #e813549942](https://github.com/MariaDB/server/commit/e813549942)\
  2021-09-11 00:13:15 +0200
  * Backport "Fix generation of bison output for out-of-source builds."to 10.5
* [Revision #8fe927e6de](https://github.com/MariaDB/server/commit/8fe927e6de)\
  2021-09-10 10:50:58 +0300
  * Expand performance\_schema tables definitions with column comments
* [Revision #cc71dc0b61](https://github.com/MariaDB/server/commit/cc71dc0b61)\
  2021-05-02 15:43:04 -0500
  * [MDEV-25325](https://jira.mariadb.org/browse/MDEV-25325) built-in documentation for performance\_schema tables
* Merge [Revision #7c33ecb665](https://github.com/MariaDB/server/commit/7c33ecb665) 2021-09-10 17:16:18 +0300 - Merge remote-tracking branch 'upstream/10.4' into 10.5
* [Revision #6e3bd663d0](https://github.com/MariaDB/server/commit/6e3bd663d0)\
  2021-09-09 09:05:26 +0300
  * [MDEV-25776](https://jira.mariadb.org/browse/MDEV-25776) Race conditions in buf\_pool.page\_hash around buf\_pool.watch
* [Revision #eb2f2c1e5f](https://github.com/MariaDB/server/commit/eb2f2c1e5f)\
  2021-09-07 08:55:08 +0300
  * [MDEV-26547](https://jira.mariadb.org/browse/MDEV-26547) fixup: Wait for read completion
* [Revision #b729c1a1ec](https://github.com/MariaDB/server/commit/b729c1a1ec)\
  2021-09-06 19:07:24 +0200
  * Fix a false positive GCC5 warning.
* [Revision #84c578c795](https://github.com/MariaDB/server/commit/84c578c795)\
  2021-09-06 10:14:24 +0300
  * [MDEV-26547](https://jira.mariadb.org/browse/MDEV-26547) Restoring InnoDB buffer pool dump is single-threaded for no reason
* [Revision #7d351f1aa0](https://github.com/MariaDB/server/commit/7d351f1aa0)\
  2021-09-06 10:14:17 +0300
  * [MDEV-26533](https://jira.mariadb.org/browse/MDEV-26533) fixup: GCC -Wformat
* [Revision #1fda0544b9](https://github.com/MariaDB/server/commit/1fda0544b9)\
  2021-08-11 10:27:20 +0000
  * [MDEV-25684](https://jira.mariadb.org/browse/MDEV-25684) Crash in THD::find\_temporary\_table while calling spider\_direct\_sql UDF without temporary table created
* [Revision #a1b0f23586](https://github.com/MariaDB/server/commit/a1b0f23586)\
  2021-09-04 17:38:47 +0200
  * [MDEV-26533](https://jira.mariadb.org/browse/MDEV-26533) [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) crashes with key\_buffer\_size > 4Gb on Windows x64
* [Revision #e38a05e20a](https://github.com/MariaDB/server/commit/e38a05e20a)\
  2021-09-02 19:41:54 +0200
  * Fix create\_background\_thd()
* [Revision #10f08aff15](https://github.com/MariaDB/server/commit/10f08aff15)\
  2021-09-01 13:32:57 +0300
  * Added support for CHECK TABLE for S3 tables
* [Revision #49ae199604](https://github.com/MariaDB/server/commit/49ae199604)\
  2021-08-31 18:02:38 +0300
  * Added support for ANALYZE TABLE to S3 tables
* [Revision #6bdc03ebcc](https://github.com/MariaDB/server/commit/6bdc03ebcc)\
  2021-08-31 15:34:28 +0300
  * Added options s3\_port and s3\_use\_http to aria\_s3\_copy
* [Revision #1fcd8db776](https://github.com/MariaDB/server/commit/1fcd8db776)\
  2021-08-31 12:02:31 +0200
  * [MDEV-26511](https://jira.mariadb.org/browse/MDEV-26511) - Do not change purge thread count during bootstrap
* Merge [Revision #e62120cec7](https://github.com/MariaDB/server/commit/e62120cec7) 2021-08-31 10:04:56 +0300 - Merge 10.4 into 10.5
* [Revision #1a69e1588b](https://github.com/MariaDB/server/commit/1a69e1588b)\
  2021-08-30 23:41:50 +0200
  * [MDEV-26511](https://jira.mariadb.org/browse/MDEV-26511) Only allocate Innodb background purge thd, when it is safe.
* [Revision #4b6ef03dcd](https://github.com/MariaDB/server/commit/4b6ef03dcd)\
  2021-08-27 12:54:42 +0700
  * [MDEV-26438](https://jira.mariadb.org/browse/MDEV-26438) cmake < 3.6.0 produced RPMs with invalid names
* Merge [Revision #87ff4ba7c8](https://github.com/MariaDB/server/commit/87ff4ba7c8) 2021-08-26 08:46:57 +0300 - Merge 10.4 into 10.5
* [Revision #bd3eb52851](https://github.com/MariaDB/server/commit/bd3eb52851)\
  2021-08-25 17:41:43 +1000
  * [MDEV-26474](https://jira.mariadb.org/browse/MDEV-26474): Fix mysql\_setpermission hostname logic
* Merge [Revision #1b2acc5b9d](https://github.com/MariaDB/server/commit/1b2acc5b9d) 2021-08-25 07:53:23 +0300 - Merge 10.4 into 10.5
* Merge [Revision #2c9f2a4c8c](https://github.com/MariaDB/server/commit/2c9f2a4c8c) 2021-08-23 11:10:59 +0300 - Merge 10.4 into 10.5
* [Revision #a6621867e9](https://github.com/MariaDB/server/commit/a6621867e9)\
  2021-08-20 10:36:38 +1000
  * deb: columnstore not 32bit (fix stretch)
* [Revision #69b75cb3db](https://github.com/MariaDB/server/commit/69b75cb3db)\
  2021-08-19 17:54:13 +0200
  * [MDEV-26440](https://jira.mariadb.org/browse/MDEV-26440) Missing connection id value in I\_S.thread\_pool\_queues
* [Revision #4009e9b253](https://github.com/MariaDB/server/commit/4009e9b253)\
  2021-08-19 17:49:39 +0200
  * [MDEV-19313](https://jira.mariadb.org/browse/MDEV-19313) post-fix
* [Revision #c9d57c006a](https://github.com/MariaDB/server/commit/c9d57c006a)\
  2021-08-19 19:47:38 +0700
  * [MDEV-26380](https://jira.mariadb.org/browse/MDEV-26380) auth\_pam\_tool has incorrect permissions on CentOS 7
* [Revision #17980e35fa](https://github.com/MariaDB/server/commit/17980e35fa)\
  2021-08-19 12:05:02 +0300
  * [MDEV-26439](https://jira.mariadb.org/browse/MDEV-26439) Typo in Foreign Key error message
* Merge [Revision #06079a4c2c](https://github.com/MariaDB/server/commit/06079a4c2c) 2021-08-19 11:52:35 +0300 - Merge 10.4 into 10.5
* [Revision #a2a0ac7c4c](https://github.com/MariaDB/server/commit/a2a0ac7c4c)\
  2021-08-18 19:26:01 +0300
  * [MDEV-26206](https://jira.mariadb.org/browse/MDEV-26206) gap lock is not set if implicit lock exists
* [Revision #7d2d9f04b9](https://github.com/MariaDB/server/commit/7d2d9f04b9)\
  2021-08-19 11:29:32 +0300
  * [MDEV-20931](https://jira.mariadb.org/browse/MDEV-20931) fixup
* Merge [Revision #4a25957274](https://github.com/MariaDB/server/commit/4a25957274) 2021-08-18 18:22:35 +0300 - Merge 10.4 into 10.5
* [Revision #da171182b7](https://github.com/MariaDB/server/commit/da171182b7)\
  2021-08-18 10:13:02 +0200
  * [MDEV-26223](https://jira.mariadb.org/browse/MDEV-26223) Galera cluster node consider old server\_id value even after modification of server\_id \[wsrep\_gtid\_mode=ON]
* [Revision #cce33787c3](https://github.com/MariaDB/server/commit/cce33787c3)\
  2021-08-17 12:01:10 +0300
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) fixup: Add missing 'static'
* [Revision #255313048c](https://github.com/MariaDB/server/commit/255313048c)\
  2021-08-16 17:02:15 +0530
  * [MDEV-26273](https://jira.mariadb.org/browse/MDEV-26273) InnoDB FTS DDL fails when innodb\_force\_recovery is set to 2
* [Revision #3d16e0e16c](https://github.com/MariaDB/server/commit/3d16e0e16c)\
  2021-08-16 15:40:55 +1000
  * deb: columnstore not 32bit (fix)
* [Revision #0268b87122](https://github.com/MariaDB/server/commit/0268b87122)\
  2021-08-11 11:28:08 +1000
  * deb: columnstore not 32bit
* [Revision #30d33d85cb](https://github.com/MariaDB/server/commit/30d33d85cb)\
  2021-08-11 11:14:45 +1000
  * deb: s390x no WolfSSL workaround as upstream fixed in 4.6.0
* [Revision #070183cfc0](https://github.com/MariaDB/server/commit/070183cfc0)\
  2021-08-12 18:32:01 +0200
  * [MDEV-26325](https://jira.mariadb.org/browse/MDEV-26325) Shutdown hangs whenever named pipes were used for connections.
* [Revision #10db7fcfa6](https://github.com/MariaDB/server/commit/10db7fcfa6)\
  2021-08-10 23:22:04 +0400
  * MENT-977 log priv host / priv user.
* [Revision #20a9f0b511](https://github.com/MariaDB/server/commit/20a9f0b511)\
  2021-08-05 10:18:19 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
