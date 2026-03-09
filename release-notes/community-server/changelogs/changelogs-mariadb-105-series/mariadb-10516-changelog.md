# MariaDB 10.5.16 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.16](https://mariadb.org/download/?tab=mariadb\&release=10.5.16\&product=mariadb)[Release Notes](../../old-releases/10.5/10.5.16.md)[Changelog](mariadb-10516-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 20 May 2022

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.16.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.25](../changelogs-mariadb-10-4-series/mariadb-10425-changelog.md)
* Merge [Revision #7970ac7fe8](https://github.com/MariaDB/server/commit/7970ac7fe8) 2022-05-18 01:47:48 +0200 - Merge branch '10.4' into 10.5
* [Revision #b03ab1270d](https://github.com/MariaDB/server/commit/b03ab1270d)\
  2022-05-15 23:28:06 +0400
  * [MDEV-28490](https://jira.mariadb.org/browse/MDEV-28490) Strange result truncation with group\_concat\_max\_len=1GB
* [Revision #3fabdc3ca8](https://github.com/MariaDB/server/commit/3fabdc3ca8)\
  2022-05-06 10:49:35 +0300
  * [MDEV-28473](https://jira.mariadb.org/browse/MDEV-28473) field\_ref\_zero is not initialized in xtrabackup\_prepare\_func()
* [Revision #09ee95e33e](https://github.com/MariaDB/server/commit/09ee95e33e)\
  2022-05-11 13:24:39 +1000
  * [MDEV-28534](https://jira.mariadb.org/browse/MDEV-28534): clang-12 compile warnings
* [Revision #fe3d07cab8](https://github.com/MariaDB/server/commit/fe3d07cab8)\
  2022-05-10 11:46:05 +0200
  * fix plugins.multiauth for AIX
* Merge [Revision #ef781162ff](https://github.com/MariaDB/server/commit/ef781162ff) 2022-05-09 22:04:06 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #e9af6b2a4d](https://github.com/MariaDB/server/commit/e9af6b2a4d) 2022-05-08 09:31:00 +0200 - Merge branch 'merge-perfschema-5.7' into 10.5
* [Revision #bee3e96da3](https://github.com/MariaDB/server/commit/bee3e96da3)\
  2022-05-05 10:11:03 +0200
  * 5.7.38
* [Revision #16e276721a](https://github.com/MariaDB/server/commit/16e276721a)\
  2022-05-06 17:40:55 +0300
  * [MDEV-28478](https://jira.mariadb.org/browse/MDEV-28478) fixup: Declare a constexpr member function const
* [Revision #fd9e733aaa](https://github.com/MariaDB/server/commit/fd9e733aaa)\
  2022-05-06 10:39:12 +0300
  * [MDEV-28478](https://jira.mariadb.org/browse/MDEV-28478) fixup: Remove a conflict marker
* [Revision #26d46234e8](https://github.com/MariaDB/server/commit/26d46234e8)\
  2022-05-06 10:12:31 +0300
  * [MDEV-28478](https://jira.mariadb.org/browse/MDEV-28478): INSERT into SPATIAL INDEX in TEMPORARY table writes log
* [Revision #1421d1f296](https://github.com/MariaDB/server/commit/1421d1f296)\
  2022-04-29 20:40:50 +0200
  * columnstore-5.6.5-2
* [Revision #821808c45d](https://github.com/MariaDB/server/commit/821808c45d)\
  2022-04-28 11:23:12 +0400
  * A clean-up for "[MDEV-19772](https://jira.mariadb.org/browse/MDEV-19772) Add helper classes for ST\_FIELD\_INFO"
* [Revision #34b002d0dc](https://github.com/MariaDB/server/commit/34b002d0dc)\
  2022-04-26 11:09:16 +0200
  * New PCRE2 (10.40)
* [Revision #1a66e3f861](https://github.com/MariaDB/server/commit/1a66e3f861)\
  2022-04-25 14:36:00 +0300
  * Skip main.sp-no-valgrind WITH\_MSAN due to result diff
* [Revision #cba13079da](https://github.com/MariaDB/server/commit/cba13079da)\
  2022-04-25 10:42:57 +0300
  * Remove redundant innodb-page\_compression\_ tests
* [Revision #35095c458b](https://github.com/MariaDB/server/commit/35095c458b)\
  2022-04-25 10:19:12 +0300
  * Clean up the page\_compressed tests
* [Revision #4faef6e240](https://github.com/MariaDB/server/commit/4faef6e240)\
  2022-04-25 09:40:40 +0300
  * Cleanup: Remove IF\_VALGRIND
* [Revision #232af0c7bf](https://github.com/MariaDB/server/commit/232af0c7bf)\
  2022-04-25 09:36:30 +0300
  * Do not disable --symbolic-links on Valgrind (or MSAN)
* [Revision #c009ce7dd0](https://github.com/MariaDB/server/commit/c009ce7dd0)\
  2022-04-22 12:48:40 +0300
  * [MDEV-27094](https://jira.mariadb.org/browse/MDEV-27094) Debug builds include useless InnoDB "disabled" options
* Merge [Revision #620c55e708](https://github.com/MariaDB/server/commit/620c55e708) 2022-04-21 15:33:50 +0300 - Merge 10.4 into 10.5
* [Revision #fdec842fd7](https://github.com/MariaDB/server/commit/fdec842fd7)\
  2022-04-21 14:09:23 +0300
  * [MDEV-28371](https://jira.mariadb.org/browse/MDEV-28371) Assertion fold == id.fold() failed in buf\_flush\_check\_neighbor()
* Merge [Revision #580cbd18b3](https://github.com/MariaDB/server/commit/580cbd18b3) 2022-04-21 14:48:13 +1000 - Merge branch 10.4 into 10.5
* [Revision #a9adfc0f68](https://github.com/MariaDB/server/commit/a9adfc0f68)\
  2022-04-15 20:28:33 +0300
  * [MDEV-9948](https://jira.mariadb.org/browse/MDEV-9948) Failing assertion: new\_state->key\_version != ENCRYPTION\_KEY\_VERSION\_INVALID in fil0crypt.cc
* [Revision #4abb023ba5](https://github.com/MariaDB/server/commit/4abb023ba5)\
  2022-04-15 18:53:51 +0900
  * Spider: disable spider/bugfix.mdev\_27239
* [Revision #e41500e4f2](https://github.com/MariaDB/server/commit/e41500e4f2)\
  2022-04-12 13:57:16 +0400
  * [MDEV-26128](https://jira.mariadb.org/browse/MDEV-26128) type\_set and type\_enum are broken
* [Revision #f61f58e759](https://github.com/MariaDB/server/commit/f61f58e759)\
  2022-04-08 12:48:27 +0530
  * [MDEV-26578](https://jira.mariadb.org/browse/MDEV-26578) ERROR: AddressSanitizer: heap-use-after-free around dict\_table\_t::is\_temporary\_name
* [Revision #bf70532e3d](https://github.com/MariaDB/server/commit/bf70532e3d)\
  2022-04-10 14:36:47 +0400
  * 10.5 tests for [MDEV-26507](https://jira.mariadb.org/browse/MDEV-26507) Assertion \`tmp != ((long long) 0x8000000000000000LL)' failed in TIME\_from\_longlong\_datetime\_packed
* [Revision #cfdb621243](https://github.com/MariaDB/server/commit/cfdb621243)\
  2022-04-08 14:17:36 +0200
  * [MDEV-28255](https://jira.mariadb.org/browse/MDEV-28255) "Error" instead of NULL in P\_S.THREADS\_CONNECTION\_TYPE for background threads
* [Revision #d8463b64b3](https://github.com/MariaDB/server/commit/d8463b64b3)\
  2022-01-21 01:59:25 +0900
  * [MDEV-27239](https://jira.mariadb.org/browse/MDEV-27239) Spider: Assertion \`thd->transaction->stmt.ha\_list == null || trans == \&thd->transaction->stmt' failed in ha\_commit\_trans on BEGIN WORK after FTWRL
* Merge [Revision #6645b1d2c7](https://github.com/MariaDB/server/commit/6645b1d2c7) 2022-04-07 10:36:58 +0300 - Merge 10.4 into 10.5
* [Revision #dea4e178fe](https://github.com/MariaDB/server/commit/dea4e178fe)\
  2022-04-07 14:55:52 +1000
  * deb: make --output-sync=target
* [Revision #8990ffe62a](https://github.com/MariaDB/server/commit/8990ffe62a)\
  2022-03-25 17:25:11 +1100
  * [MDEV-28153](https://jira.mariadb.org/browse/MDEV-28153): Debian autobake to generate control
* [Revision #4ee00a29e3](https://github.com/MariaDB/server/commit/4ee00a29e3)\
  2022-04-07 10:50:04 +1000
  * [MDEV-28250](https://jira.mariadb.org/browse/MDEV-28250) aix test case failure innodb\_zip.innochecksum\_3,4k,crc32,innodb
* [Revision #e84e134a91](https://github.com/MariaDB/server/commit/e84e134a91)\
  2022-04-07 09:30:26 +1000
  * main.thread\_pool\_info - no threadpool on aix
* [Revision #fd6a464ae5](https://github.com/MariaDB/server/commit/fd6a464ae5)\
  2022-04-06 11:51:36 +0300
  * [MDEV-13005](https://jira.mariadb.org/browse/MDEV-13005) after-merge fixup
* Merge [Revision #5d8dcfd86c](https://github.com/MariaDB/server/commit/5d8dcfd86c) 2022-04-06 10:30:49 +0300 - [MDEV-25975](https://jira.mariadb.org/browse/MDEV-25975): Merge 10.4 into 10.5
* Merge [Revision #cacb61b6be](https://github.com/MariaDB/server/commit/cacb61b6be) 2022-04-06 10:06:39 +0300 - Merge 10.4 into 10.5
* [Revision #aed87f1e0a](https://github.com/MariaDB/server/commit/aed87f1e0a)\
  2022-03-31 10:14:12 +0200
  * Change MDBF mirror URL
* [Revision #6a3545dd1e](https://github.com/MariaDB/server/commit/6a3545dd1e)\
  2022-04-01 15:58:31 +0300
  * [MDEV-26322](https://jira.mariadb.org/browse/MDEV-26322) Last binlog file and position are "empty" in mariadb-backup --prepare output
* [Revision #7f5a3cd253](https://github.com/MariaDB/server/commit/7f5a3cd253)\
  2022-04-04 17:13:33 +1000
  * [MDEV-28231](https://jira.mariadb.org/browse/MDEV-28231): innodb: format string warning on aix UINT64PFx (ib\_id\_t)
* [Revision #7d7bdd4aaa](https://github.com/MariaDB/server/commit/7d7bdd4aaa)\
  2022-03-29 19:42:10 +0300
  * [MDEV-28185](https://jira.mariadb.org/browse/MDEV-28185) InnoDB generates redundant log checkpoints
* [Revision #d875c50bf4](https://github.com/MariaDB/server/commit/d875c50bf4)\
  2022-03-29 19:41:38 +0300
  * [MDEV-17841](https://jira.mariadb.org/browse/MDEV-17841) fixup: GCC -Wmaybe-uninitialized
* [Revision #42609c240d](https://github.com/MariaDB/server/commit/42609c240d)\
  2022-03-29 14:56:44 +0300
  * Cleanup: Replace log\_sys.n\_pending\_checkpoint\_writes with a Boolean
* [Revision #b7016bd379](https://github.com/MariaDB/server/commit/b7016bd379)\
  2022-03-29 14:53:51 +0300
  * [MDEV-26626](https://jira.mariadb.org/browse/MDEV-26626) fixup: SIGFPE during startup
* [Revision #c14f60a72f](https://github.com/MariaDB/server/commit/c14f60a72f)\
  2022-03-29 12:59:38 +0300
  * Fix g++-12 -O2 -Wstringop-overflow
* Merge [Revision #d62b0368ca](https://github.com/MariaDB/server/commit/d62b0368ca) 2022-03-29 12:59:18 +0300 - Merge 10.4 into 10.5
* [Revision #9d6d122123](https://github.com/MariaDB/server/commit/9d6d122123)\
  2022-03-24 00:43:04 -0700
  * Deb: Fix Salsa-CI autopkgtest failure
* [Revision #dcb2968f90](https://github.com/MariaDB/server/commit/dcb2968f90)\
  2022-03-14 20:46:40 +0300
  * [MDEV-27557](https://jira.mariadb.org/browse/MDEV-27557) InnoDB unnecessarily commits mtr during secondary index search to preserve clustered index latching order
* [Revision #157a838b19](https://github.com/MariaDB/server/commit/157a838b19)\
  2022-03-18 11:42:20 +1100
  * [MDEV-28153](https://jira.mariadb.org/browse/MDEV-28153): Debian autobake- use absolute dependencies rather than a buildtime detection
* [Revision #b101f19d29](https://github.com/MariaDB/server/commit/b101f19d29)\
  2022-03-24 13:43:58 +0200
  * [MDEV-23974](https://jira.mariadb.org/browse/MDEV-23974) fixup: rpl.rpl\_gtid\_stop\_start fails
* [Revision #d2c019b200](https://github.com/MariaDB/server/commit/d2c019b200)\
  2022-03-23 13:06:13 +0100
  * [MDEV-28107](https://jira.mariadb.org/browse/MDEV-28107) S3 doesn't build if CURL is in non-default location
* [Revision #2ca3861b55](https://github.com/MariaDB/server/commit/2ca3861b55)\
  2022-03-23 12:40:43 +0100
  * [MDEV-28106](https://jira.mariadb.org/browse/MDEV-28106) S3 tries to include thread.h while compiling on Windows
* [Revision #75b7cd680b](https://github.com/MariaDB/server/commit/75b7cd680b)\
  2022-03-23 16:42:43 +0200
  * [MDEV-23974](https://jira.mariadb.org/browse/MDEV-23974) Tests fail due to \[Warning] InnoDB: Trying to delete tablespace
* [Revision #44231dc6d5](https://github.com/MariaDB/server/commit/44231dc6d5)\
  2022-03-23 16:41:58 +0200
  * Cleanup: have\_sanitizer='ASAN,UBSAN'
* [Revision #9595ea8992](https://github.com/MariaDB/server/commit/9595ea8992)\
  2022-03-02 20:05:50 -0800
  * Deb: Sync Salsa-CI from Debian [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) repository
* [Revision #06e3bc4390](https://github.com/MariaDB/server/commit/06e3bc4390)\
  2022-03-17 10:33:06 +0200
  * [MDEV-17841](https://jira.mariadb.org/browse/MDEV-17841) fixup: GCC -Wmaybe-uninitialized
* Merge [Revision #b73d852779](https://github.com/MariaDB/server/commit/b73d852779) 2022-03-16 17:51:49 +1100 - Merge 10.4 to 10.5
* [Revision #73fee39ea6](https://github.com/MariaDB/server/commit/73fee39ea6)\
  2022-03-15 14:44:22 +0200
  * [MDEV-27985](https://jira.mariadb.org/browse/MDEV-27985) buf\_flush\_freed\_pages() causes InnoDB to hang
* [Revision #00896db1c5](https://github.com/MariaDB/server/commit/00896db1c5)\
  2022-03-15 10:37:13 +0200
  * [MDEV-25214](https://jira.mariadb.org/browse/MDEV-25214) Crash in fil\_space\_t::try\_to\_close
* Merge [Revision #e1246775a9](https://github.com/MariaDB/server/commit/e1246775a9) 2022-03-15 08:32:28 +0200 - Merge 10.4 into 10.5
* [Revision #258c34f17c](https://github.com/MariaDB/server/commit/258c34f17c)\
  2022-03-14 10:42:50 +0200
  * [MDEV-28050](https://jira.mariadb.org/browse/MDEV-28050): clang -Wtypedef-redefinition when PLUGIN\_S3=NO
* [Revision #c2146ce774](https://github.com/MariaDB/server/commit/c2146ce774)\
  2022-03-14 10:37:39 +0200
  * [MDEV-24841](https://jira.mariadb.org/browse/MDEV-24841): More workarounds
* [Revision #59359fb44a](https://github.com/MariaDB/server/commit/59359fb44a)\
  2022-03-14 09:28:55 +0200
  * [MDEV-24841](https://jira.mariadb.org/browse/MDEV-24841) Build error with MSAN use-of-uninitialized-value in comp\_err
* [Revision #d78173828e](https://github.com/MariaDB/server/commit/d78173828e)\
  2022-03-10 18:15:25 +1100
  * [MDEV-27900](https://jira.mariadb.org/browse/MDEV-27900): aio handle partial reads/writes
* Merge [Revision #4cfb6eddcd](https://github.com/MariaDB/server/commit/4cfb6eddcd) 2022-03-11 14:36:28 +0200 - Merge 10.4 into 10.5
* [Revision #97d82808b8](https://github.com/MariaDB/server/commit/97d82808b8)\
  2022-03-11 13:29:41 +0200
  * Fix clang -Wtypedef-redefinition
* Merge [Revision #9047a908fe](https://github.com/MariaDB/server/commit/9047a908fe) 2022-03-11 13:03:33 +0200 - Merge 10.4 into 10.5
* [Revision #5503c40460](https://github.com/MariaDB/server/commit/5503c40460)\
  2022-03-11 09:46:50 +0200
  * Stabilize innodb.redo\_log\_during\_checkpoint
* Merge [Revision #81523baac6](https://github.com/MariaDB/server/commit/81523baac6) 2022-03-11 09:36:03 +0200 - Merge 10.4 into 10.5
* Merge [Revision #0b92c7b0e0](https://github.com/MariaDB/server/commit/0b92c7b0e0) 2022-03-07 17:16:11 +0300 - Merge 10.4 into 10.5
* Merge [Revision #2dce3bad9c](https://github.com/MariaDB/server/commit/2dce3bad9c) 2022-03-07 09:26:50 +0200 - Merge 10.4 into 10.5
* [Revision #e8e755ea6c](https://github.com/MariaDB/server/commit/e8e755ea6c)\
  2022-02-21 19:32:09 +0530
  * [MDEV-26230](https://jira.mariadb.org/browse/MDEV-26230): mysql\_upgrade fails to load type\_mysql\_json due to insufficient maturity level
* [Revision #a1965b80e1](https://github.com/MariaDB/server/commit/a1965b80e1)\
  2022-03-01 17:19:58 +0300
  * Make testcase for [MDEV-26585](https://jira.mariadb.org/browse/MDEV-26585) stable.
* [Revision #a710016d57](https://github.com/MariaDB/server/commit/a710016d57)\
  2022-03-01 09:13:25 +0200
  * [MDEV-27967](https://jira.mariadb.org/browse/MDEV-27967) Assertion !buf\_pool.any\_io\_pending() failed
* [Revision #9af4c7c6d7](https://github.com/MariaDB/server/commit/9af4c7c6d7)\
  2022-03-01 09:12:15 +0200
  * [MDEV-27964](https://jira.mariadb.org/browse/MDEV-27964): A better work-around
* [Revision #72437cbc12](https://github.com/MariaDB/server/commit/72437cbc12)\
  2022-02-28 20:08:11 +0200
  * Fixed sporadic error in main.backup\_locks
* [Revision #bc020058d3](https://github.com/MariaDB/server/commit/bc020058d3)\
  2022-02-28 18:31:59 +0200
  * [MDEV-27964](https://jira.mariadb.org/browse/MDEV-27964): Work around SIGSEGV in WITH\_MSAN builds
* [Revision #08d39bdf22](https://github.com/MariaDB/server/commit/08d39bdf22)\
  2022-02-28 18:16:47 +0200
  * Merge fixup: -Wconversion
* [Revision #13076bd314](https://github.com/MariaDB/server/commit/13076bd314)\
  2022-02-28 14:05:50 +0200
  * Avoid some failures WITH\_MSAN
* Merge [Revision #cc1d906211](https://github.com/MariaDB/server/commit/cc1d906211) 2022-02-28 13:17:09 +0200 - Merge 10.4 into 10.5
* Merge [Revision #b791b942e1](https://github.com/MariaDB/server/commit/b791b942e1) 2022-02-25 13:27:41 +0200 - Merge 10.4 into 10.5
* Merge [Revision #f42d6234bd](https://github.com/MariaDB/server/commit/f42d6234bd) 2022-02-25 11:47:27 +0200 - Merge 10.4 into 10.5 ([MDEV-27913](https://jira.mariadb.org/browse/MDEV-27913))
* [Revision #97ed3dd6df](https://github.com/MariaDB/server/commit/97ed3dd6df)\
  2022-02-11 18:35:00 +0800
  * Remove unused header from crc32c.cc
* [Revision #863c1a0206](https://github.com/MariaDB/server/commit/863c1a0206)\
  2022-02-24 14:59:04 +1100
  * [MDEV-27932](https://jira.mariadb.org/browse/MDEV-27932): perfschema.dml\_file\_instances mtr failure
* [Revision #b91a123d8c](https://github.com/MariaDB/server/commit/b91a123d8c)\
  2022-02-23 15:48:08 +0200
  * Extend have\_sanitizer with ASAN+UBSAN and MSAN
* Merge [Revision #23368b76be](https://github.com/MariaDB/server/commit/23368b76be) 2022-02-23 15:31:36 +0200 - Merge 10.4 into 10.5
* Merge [Revision #a112a80b47](https://github.com/MariaDB/server/commit/a112a80b47) 2022-02-22 10:35:16 +0300 - Merge 10.4 into 10.5
* [Revision #b69191bbb2](https://github.com/MariaDB/server/commit/b69191bbb2)\
  2022-02-18 16:31:54 +0200
  * [MDEV-26645](https://jira.mariadb.org/browse/MDEV-26645): Fix UB in Item\_func\_plus and Item\_func\_minus
* Merge [Revision #cac995ec6f](https://github.com/MariaDB/server/commit/cac995ec6f) 2022-02-17 11:58:25 +0200 - Merge 10.4 into 10.5
* [Revision #5948d7602e](https://github.com/MariaDB/server/commit/5948d7602e)\
  2022-02-15 10:04:05 +0300
  * [MDEV-20605](https://jira.mariadb.org/browse/MDEV-20605) Awaken transaction can miss inserted by other transaction records due to wrong persistent cursor restoration
* [Revision #20e9e804c1](https://github.com/MariaDB/server/commit/20e9e804c1)\
  2021-11-30 18:22:39 +0300
  * [MDEV-20605](https://jira.mariadb.org/browse/MDEV-20605) Awaken transaction can miss inserted by other transaction records due to wrong persistent cursor restoration
* Merge [Revision #52b32c60c2](https://github.com/MariaDB/server/commit/52b32c60c2) 2022-02-14 08:59:33 +0200 - Merge 10.4 into 10.5
* Merge [Revision #6405ed63e1](https://github.com/MariaDB/server/commit/6405ed63e1) 2022-02-14 08:59:13 +0200 - Merge mariadb-10.5.15 into 10.5
* [Revision #1557204b05](https://github.com/MariaDB/server/commit/1557204b05)\
  2022-02-12 14:25:37 -0500
  * bump the VERSION
* [Revision #91d9e9bd80](https://github.com/MariaDB/server/commit/91d9e9bd80)\
  2022-02-11 14:27:57 +0100
  * [MDEV-27813](https://jira.mariadb.org/browse/MDEV-27813) Windows, compiling : RelWithDebInfo should use /Ob2
* [Revision #7c6ec0a53b](https://github.com/MariaDB/server/commit/7c6ec0a53b)\
  2022-02-08 00:18:27 +0000
  * [MDEV-27804](https://jira.mariadb.org/browse/MDEV-27804) Fails to build - perf schema - thread id of type uintptr\_t requires header

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
