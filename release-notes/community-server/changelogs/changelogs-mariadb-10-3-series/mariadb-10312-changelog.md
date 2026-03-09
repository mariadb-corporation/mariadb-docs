# MariaDB 10.3.12 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.12/)[Release Notes](../../old-releases/10.3/10.3.12.md)[Changelog](mariadb-10312-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 7 Jan 2019

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.12.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #faf206a848](https://github.com/MariaDB/server/commit/faf206a848)\
  2019-01-04 17:25:19 +0200
  * Updated list of unstable tests for 10.3.12 release
* [Revision #968f1b5db6](https://github.com/MariaDB/server/commit/968f1b5db6)\
  2019-01-04 17:24:54 +0200
  * Fix the location of test files
* [Revision #c902a033b9](https://github.com/MariaDB/server/commit/c902a033b9)\
  2019-01-04 08:49:01 +0100
  * Disable a test that is failing very often.
* Merge [Revision #dd43c85c48](https://github.com/MariaDB/server/commit/dd43c85c48) 2019-01-04 02:06:41 +0200 - Merge 10.2 into 10.3
* [Revision #23e4446adc](https://github.com/MariaDB/server/commit/23e4446adc)\
  2019-01-03 22:14:55 +0200
  * Fix a merge error in the parent commit
* Merge [Revision #94e22efb79](https://github.com/MariaDB/server/commit/94e22efb79) 2019-01-03 17:26:50 +0200 - Merge 10.2 into 10.3
* Merge [Revision #b7392d142a](https://github.com/MariaDB/server/commit/b7392d142a) 2019-01-03 16:58:05 +0200 - Merge 10.1 into 10.2
* [Revision #7158edcba3](https://github.com/MariaDB/server/commit/7158edcba3)\
  2019-01-03 16:24:22 +0200
  * [MDEV-18129](https://jira.mariadb.org/browse/MDEV-18129) Backup fails for encrypted tables: mariadb-backup: Database page corruption detected at page 1
* [Revision #8cbb0bfaf7](https://github.com/MariaDB/server/commit/8cbb0bfaf7)\
  2018-12-31 00:25:27 +0100
  * "fix" sequence.temporary test
* Merge [Revision #6bb11efa4a](https://github.com/MariaDB/server/commit/6bb11efa4a) 2019-01-03 13:09:41 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #842402e4df](https://github.com/MariaDB/server/commit/842402e4df) 2019-01-03 09:57:02 +0100 - Merge branch '10.1' into 10.2
* Merge [Revision #3ba3f81ae0](https://github.com/MariaDB/server/commit/3ba3f81ae0) 2019-01-03 09:56:24 +0100 - Merge branch '10.0' into 10.1
* Merge [Revision #b87eb04f77](https://github.com/MariaDB/server/commit/b87eb04f77) 2019-01-03 00:20:53 +0100 - Merge branch '5.5' into 10.0
* [Revision #2450fd67ed](https://github.com/MariaDB/server/commit/2450fd67ed)\
  2019-01-02 12:03:15 +0100
  * fix the test for 2019
* [Revision #884caeafba](https://github.com/MariaDB/server/commit/884caeafba)\
  2019-01-02 19:32:05 +0100
  * fix RHEL8 "ambiguous python shebang" build failures
* [Revision #32150d2513](https://github.com/MariaDB/server/commit/32150d2513)\
  2019-01-02 19:28:48 +0100
  * compilation warning on Windows
* [Revision #2f368bb967](https://github.com/MariaDB/server/commit/2f368bb967)\
  2019-01-02 19:33:52 +0100
  * fix RHEL8 "ambiguous python shebang" build failures
* [Revision #cf8a564686](https://github.com/MariaDB/server/commit/cf8a564686)\
  2019-01-02 19:29:58 +0100
  * compilation warning on windows
* [Revision #1f9f72b13e](https://github.com/MariaDB/server/commit/1f9f72b13e)\
  2019-01-02 16:34:15 +0100
  * fix debian builds for cosmic
* [Revision #099186d09e](https://github.com/MariaDB/server/commit/099186d09e)\
  2019-01-02 13:42:11 -0500
  * bump the VERSION
* [Revision #ab4bc84420](https://github.com/MariaDB/server/commit/ab4bc84420)\
  2018-12-27 18:19:41 +0200
  * Follow-up to [MDEV-14585](https://jira.mariadb.org/browse/MDEV-14585): Remove dict\_temp\_file\_num
* [Revision #e2939795b1](https://github.com/MariaDB/server/commit/e2939795b1)\
  2018-12-26 16:55:54 +0000
  * travis: Fix ccache not used on macOS targets
* [Revision #d89d12e3b7](https://github.com/MariaDB/server/commit/d89d12e3b7)\
  2018-12-26 12:10:50 +0400
  * [MDEV-17759](https://jira.mariadb.org/browse/MDEV-17759) Assertion \`precision > 0' failed in decimal\_bin\_size upon CREATE TABLE .. SELECT
* [Revision #812bb1303c](https://github.com/MariaDB/server/commit/812bb1303c)\
  2018-12-24 09:53:17 +0100
  * (still) Packaging is broken for debian-based systems
* Merge [Revision #97181d84f9](https://github.com/MariaDB/server/commit/97181d84f9) 2018-12-23 06:06:51 +0200 - Merge pull request #1051 from tempesta-tech/sysprg/[MDEV-18064](https://jira.mariadb.org/browse/MDEV-18064)
* [Revision #1a4248ad6c](https://github.com/MariaDB/server/commit/1a4248ad6c)\
  2018-12-23 00:53:14 +0100
  * [MDEV-18064](https://jira.mariadb.org/browse/MDEV-18064): Packaging is broken for debian-based systems
* [Revision #779151db80](https://github.com/MariaDB/server/commit/779151db80)\
  2018-11-22 16:26:03 +0200
  * autobake-deb: fixes for AWS SDK build eligibility checks.
* [Revision #2999492c32](https://github.com/MariaDB/server/commit/2999492c32)\
  2018-12-20 11:22:13 +0100
  * [MDEV-16036](https://jira.mariadb.org/browse/MDEV-16036): Debug assertion failed in resignal on create temporary table
* Merge [Revision #b26736cdb1](https://github.com/MariaDB/server/commit/b26736cdb1) 2018-12-18 14:05:23 +0200 - Merge pull request #1029 from tempesta-tech/sysprg/[MDEV-17835](https://jira.mariadb.org/browse/MDEV-17835)
* [Revision #cadb6ac770](https://github.com/MariaDB/server/commit/cadb6ac770)\
  2018-12-06 14:36:57 +0100
  * DEV-17835: Remove wsrep-sst-method=xtrabackup
* Merge [Revision #75e7e0b90f](https://github.com/MariaDB/server/commit/75e7e0b90f) 2018-12-18 11:51:44 +0200 - Merge 10.2 into 10.3
* Merge [Revision #af9731071d](https://github.com/MariaDB/server/commit/af9731071d) 2018-12-18 09:44:49 +0200 - Merge pull request #1031 from tempesta-tech/sysprg/[MDEV-17786](https://jira.mariadb.org/browse/MDEV-17786)
* [Revision #dcef75df9f](https://github.com/MariaDB/server/commit/dcef75df9f)\
  2018-12-12 13:49:45 +0100
  * DEV-17786: Add mariadb-backup test case for galera\_sst\_xtrabackup-v2\_data\_dir
* Merge [Revision #45531949ae](https://github.com/MariaDB/server/commit/45531949ae) 2018-12-18 09:15:41 +0200 - Merge 10.2 into 10.3
* Merge [Revision #36b7f8f4b0](https://github.com/MariaDB/server/commit/36b7f8f4b0) 2018-12-17 18:37:56 +0200 - Merge pull request #1030 from tempesta-tech/sysprg/[MDEV-17848](https://jira.mariadb.org/browse/MDEV-17848)
* [Revision #d48ac8b414](https://github.com/MariaDB/server/commit/d48ac8b414)\
  2018-12-12 13:44:58 +0100
  * [MDEV-17848](https://jira.mariadb.org/browse/MDEV-17848): Galera test failure on galera\_sst\_xtrabackup-v2\[\_data\_dir]
* Merge [Revision #5fefcb0a21](https://github.com/MariaDB/server/commit/5fefcb0a21) 2018-12-14 16:13:35 +0200 - Merge 10.2 into 10.3
* Merge [Revision #cfe8386296](https://github.com/MariaDB/server/commit/cfe8386296) 2018-12-14 13:58:45 +0200 - Merge 10.2 into 10.3
* Merge [Revision #f6e16bdc62](https://github.com/MariaDB/server/commit/f6e16bdc62) 2018-12-13 21:58:35 +0200 - Merge 10.2 into 10.3
* Merge [Revision #839cf16bb2](https://github.com/MariaDB/server/commit/839cf16bb2) 2018-12-12 13:46:06 +0200 - Merge 10.2 into 10.3
* [Revision #dce2cc1c6a](https://github.com/MariaDB/server/commit/dce2cc1c6a)\
  2018-12-12 11:35:21 +0100
  * fix handler test failures on s390x
* [Revision #56d3a0e73b](https://github.com/MariaDB/server/commit/56d3a0e73b)\
  2018-12-07 00:33:51 +0100
  * [MDEV-17967](https://jira.mariadb.org/browse/MDEV-17967) Add a solution of the 8 queens problem to the regression test for CTE
* [Revision #ac31ff6275](https://github.com/MariaDB/server/commit/ac31ff6275)\
  2018-12-10 23:31:54 +0100
  * [MDEV-15760](https://jira.mariadb.org/browse/MDEV-15760) - don't build mariadb-backup with -DPLUGIN\_INNOBASE=DYNAMIC
* [Revision #8aef7f2bb9](https://github.com/MariaDB/server/commit/8aef7f2bb9)\
  2018-12-10 00:34:41 +0530
  * [MDEV-17778](https://jira.mariadb.org/browse/MDEV-17778): Alter table leads to a truncation warning with ANALYZE command
* [Revision #a72516348b](https://github.com/MariaDB/server/commit/a72516348b)\
  2018-12-10 13:02:04 +0200
  * [MDEV-17938](https://jira.mariadb.org/browse/MDEV-17938): ALTER TABLE error handling accesses freed memory
* Merge [Revision #1d18665e0b](https://github.com/MariaDB/server/commit/1d18665e0b) 2018-12-10 12:28:31 +0200 - Merge 10.2 into 10.3
* [Revision #705fd4e943](https://github.com/MariaDB/server/commit/705fd4e943)\
  2018-12-08 22:53:47 +0100
  * Fix another random failure in rpl.rpl\_gtid\_crash
* [Revision #2fd0acd30f](https://github.com/MariaDB/server/commit/2fd0acd30f)\
  2018-12-07 23:58:42 +0200
  * Fix the 64-bit Windows build
* [Revision #a02cac47f6](https://github.com/MariaDB/server/commit/a02cac47f6)\
  2018-12-07 17:20:31 +0100
  * Fix an occational test failure in rpl.rpl\_gtid\_crash
* Merge [Revision #21069c528e](https://github.com/MariaDB/server/commit/21069c528e) 2018-12-07 15:39:34 +0200 - Merge 10.2 into 10.3
* Merge [Revision #b6f203984b](https://github.com/MariaDB/server/commit/b6f203984b) 2018-12-04 13:18:14 +0200 - Merge 10.2 into 10.3
* [Revision #95f3c142a4](https://github.com/MariaDB/server/commit/95f3c142a4)\
  2018-11-30 15:48:33 +0200
  * [MDEV-17881](https://jira.mariadb.org/browse/MDEV-17881): Fix a debug assertion
* [Revision #e46a3aa42e](https://github.com/MariaDB/server/commit/e46a3aa42e)\
  2018-11-30 12:40:03 +0200
  * [MDEV-17881](https://jira.mariadb.org/browse/MDEV-17881) Assertion failure in cmp\_dtuple\_rec\_with\_match\_bytes after instant ADD COLUMN
* Merge [Revision #0abd2766b1](https://github.com/MariaDB/server/commit/0abd2766b1) 2018-11-30 09:23:23 +0200 - Merge 10.2 into 10.3
* Merge [Revision #35184902db](https://github.com/MariaDB/server/commit/35184902db) 2018-11-28 15:23:23 +0200 - Merge 10.2 into 10.3
* Merge [Revision #babb000a36](https://github.com/MariaDB/server/commit/babb000a36) 2018-11-28 01:02:46 +0200 - Merge 10.2 into 10.3
* [Revision #4b88d5ee51](https://github.com/MariaDB/server/commit/4b88d5ee51)\
  2018-11-27 15:26:18 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* Merge [Revision #36359157cf](https://github.com/MariaDB/server/commit/36359157cf) 2018-11-26 16:44:11 +0200 - Merge 10.2 into 10.3
* Merge [Revision #1afed20774](https://github.com/MariaDB/server/commit/1afed20774) 2018-11-26 14:05:15 +0200 - Merge 10.2 into 10.3
* [Revision #06972b2fbc](https://github.com/MariaDB/server/commit/06972b2fbc)\
  2018-11-23 10:28:07 +1100
  * travis: xcode10.1
* [Revision #06e5f28f9f](https://github.com/MariaDB/server/commit/06e5f28f9f)\
  2018-11-22 17:07:35 +0200
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Remove a level of pointer indirection
* [Revision #0c69f2e1ee](https://github.com/MariaDB/server/commit/0c69f2e1ee)\
  2018-11-21 16:55:57 +0200
  * Fixed compiler warnings
* [Revision #d07a6e33dd](https://github.com/MariaDB/server/commit/d07a6e33dd)\
  2018-11-20 17:31:07 +0100
  * Check that default() do not see invisible field.
* [Revision #02b70702d9](https://github.com/MariaDB/server/commit/02b70702d9)\
  2018-11-20 09:04:11 -0500
  * bump the VERSION
* Merge [Revision #4210e7bf6f](https://github.com/MariaDB/server/commit/4210e7bf6f) 2018-11-20 15:08:41 +0200 - Merge 10.2 into 10.3
* Merge [Revision #92996c9aa9](https://github.com/MariaDB/server/commit/92996c9aa9) 2018-11-20 15:08:30 +0200 - Merge bb-10.3-release into 10.3
* Merge [Revision #fd58bb71e2](https://github.com/MariaDB/server/commit/fd58bb71e2) 2018-11-19 18:45:53 +0200 - Merge 10.2 into 10.3
* [Revision #37d6d3b661](https://github.com/MariaDB/server/commit/37d6d3b661)\
  2018-11-16 16:54:33 +0200
  * Max transid was not stored directly after Aria recovery
* [Revision #a93ac8d95f](https://github.com/MariaDB/server/commit/a93ac8d95f)\
  2018-11-13 13:10:32 +0100
  * [MDEV-16448](https://jira.mariadb.org/browse/MDEV-16448) mysql\_upgrade\_service remove my.ini variables that are no more valid [MDEV-16447](https://jira.mariadb.org/browse/MDEV-16447) incorporate Innodb slow shutdown into mysql\_upgrade\_service.exe
* [Revision #efc235d84d](https://github.com/MariaDB/server/commit/efc235d84d)\
  2018-11-12 17:11:14 +0100
  * Fix test result.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
