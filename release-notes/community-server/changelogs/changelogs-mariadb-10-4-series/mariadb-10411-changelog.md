# MariaDB 10.4.11 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.11/)[Release Notes](../../old-releases/10.4/10.4.11.md)[Changelog](mariadb-10411-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 11 Dec 2019

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.11.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.21](../changelogs-mariadb-10-3-series/mariadb-10321-changelog.md)
* [Revision #7c2c420b70](https://github.com/MariaDB/server/commit/7c2c420b70)\
  2019-12-10 15:43:56 +0200
  * List of unstable tests for 10.4.11 release
* Merge [Revision #a15234bf4b](https://github.com/MariaDB/server/commit/a15234bf4b) 2019-12-09 15:09:41 +0100 - Merge branch '10.3' into 10.4
* [Revision #9a62120089](https://github.com/MariaDB/server/commit/9a62120089)\
  2019-12-09 05:45:40 +0000
  * [MDEV-21229](https://jira.mariadb.org/browse/MDEV-21229) Update wsrep-lib to deal with libstdc++ vector assertion (#1423)
* [Revision #f5b76d8c40](https://github.com/MariaDB/server/commit/f5b76d8c40)\
  2019-12-06 04:32:56 +0900
  * fix compiler warnings
* [Revision #aab6cefe8d](https://github.com/MariaDB/server/commit/aab6cefe8d)\
  2019-12-04 08:21:14 +0100
  * [MDEV-20848](https://jira.mariadb.org/browse/MDEV-20848) Fixes for MTR test galera\_sr.GCF-1060 (#1421)
* Merge [Revision #0b8b11b0b1](https://github.com/MariaDB/server/commit/0b8b11b0b1) 2019-12-02 12:51:53 +0300 - Merge 10.3 into 10.4
* [Revision #1d46923a0f](https://github.com/MariaDB/server/commit/1d46923a0f)\
  2019-12-02 12:46:15 +0300
  * [MDEV-18929](https://jira.mariadb.org/browse/MDEV-18929) 2nd execution of SP does not detect ER\_VERS\_NOT\_VERSIONED (10.4)
* Merge [Revision #a3b63b8da3](https://github.com/MariaDB/server/commit/a3b63b8da3) 2019-11-29 23:27:26 +0900 - [MDEV-18973](https://jira.mariadb.org/browse/MDEV-18973) CLIENT\_FOUND\_ROWS wrong in spider
* [Revision #e066723a41](https://github.com/MariaDB/server/commit/e066723a41)\
  2019-11-29 08:22:13 +0900
  * [MDEV-18973](https://jira.mariadb.org/browse/MDEV-18973) CLIENT\_FOUND\_ROWS wrong in spider
* [Revision #7955e197d0](https://github.com/MariaDB/server/commit/7955e197d0)\
  2019-11-29 08:48:46 +0200
  * Cleanup: Remove a constant template parameter
* [Revision #a8bf39cc3e](https://github.com/MariaDB/server/commit/a8bf39cc3e)\
  2019-11-28 15:38:09 +0200
  * Disable failing Galera test cases.
* [Revision #ad5b7b157b](https://github.com/MariaDB/server/commit/ad5b7b157b)\
  2019-05-19 20:40:40 -0700
  * [MDEV-19510](https://jira.mariadb.org/browse/MDEV-19510) Issue with: sql/wsrep\_mysqld.cc : ip\_len
* [Revision #3826178da8](https://github.com/MariaDB/server/commit/3826178da8)\
  2019-11-28 19:53:00 +0200
  * Fix the Windows non-debug build
* [Revision #4beace3316](https://github.com/MariaDB/server/commit/4beace3316)\
  2019-11-28 16:22:53 +0200
  * [MDEV-21171](https://jira.mariadb.org/browse/MDEV-21171) InnoDB is unnecessarily resetting FIL\_PAGE\_TYPE for full\_crc32 files
* [Revision #576e85ad99](https://github.com/MariaDB/server/commit/576e85ad99)\
  2019-11-27 14:36:21 +0100
  * fix ssl\_crl test failures on newer OpenSSL
* [Revision #96c6b2b649](https://github.com/MariaDB/server/commit/96c6b2b649)\
  2019-11-27 15:49:09 +0100
  * [MDEV-19781](https://jira.mariadb.org/browse/MDEV-19781) fixups
* [Revision #ed355f59dd](https://github.com/MariaDB/server/commit/ed355f59dd)\
  2019-11-26 11:22:51 -0800
  * [MDEV-20407](https://jira.mariadb.org/browse/MDEV-20407) mysqld got signal 11; rowid filter
* [Revision #3eda03d0fe](https://github.com/MariaDB/server/commit/3eda03d0fe)\
  2019-11-26 17:35:21 +0200
  * [MDEV-21148](https://jira.mariadb.org/browse/MDEV-21148): Assertion index->n\_core\_fields + n\_add >= index->n\_fields
* [Revision #4d4b2867a2](https://github.com/MariaDB/server/commit/4d4b2867a2)\
  2019-11-25 17:40:47 -0800
  * [MDEV-20056](https://jira.mariadb.org/browse/MDEV-20056) Assertion \`!prebuilt->index->is\_primary()' failed in row\_search\_idx\_cond\_check
* [Revision #b6f7ec6a5b](https://github.com/MariaDB/server/commit/b6f7ec6a5b)\
  2019-11-17 10:39:47 +0200
  * [MDEV-19781](https://jira.mariadb.org/browse/MDEV-19781) Create MariaDB named commands on Windows
* [Revision #f9ceb0a67f](https://github.com/MariaDB/server/commit/f9ceb0a67f)\
  2019-11-25 15:22:21 +0200
  * [MDEV-20190](https://jira.mariadb.org/browse/MDEV-20190) Instant operation fails when add column and collation change on non-indexed column
* Merge [Revision #a34c34d9a8](https://github.com/MariaDB/server/commit/a34c34d9a8) 2019-11-25 16:03:45 +0300 - Merge 10.3 into 10.4
* [Revision #33f55789d3](https://github.com/MariaDB/server/commit/33f55789d3)\
  2019-11-25 16:01:43 +0300
  * [MDEV-18727](https://jira.mariadb.org/browse/MDEV-18727) improve DML operation of System Versioning (10.4)
* [Revision #4111a53079](https://github.com/MariaDB/server/commit/4111a53079)\
  2019-11-25 11:19:33 +0200
  * [MDEV-21096](https://jira.mariadb.org/browse/MDEV-21096) async slave crash with gtid\_log\_pos table access (#1413)
* [Revision #f95288211c](https://github.com/MariaDB/server/commit/f95288211c)\
  2019-11-22 19:11:58 -0800
  * [MDEV-19919](https://jira.mariadb.org/browse/MDEV-19919) Assertion \`!prebuilt->index->is\_primary()' failed in row\_search\_idx\_cond\_check
* [Revision #cb6d7c3ee3](https://github.com/MariaDB/server/commit/cb6d7c3ee3)\
  2019-11-04 16:17:59 -0500
  * [MDEV-20972](https://jira.mariadb.org/browse/MDEV-20972): `or` alterative operator breaking windows build
* [Revision #6cedb671e9](https://github.com/MariaDB/server/commit/6cedb671e9)\
  2019-11-20 14:12:53 +0800
  * [MDEV-21088](https://jira.mariadb.org/browse/MDEV-21088) Table cannot be loaded after instant ADD/DROP COLUMN
* Merge [Revision #1c92406337](https://github.com/MariaDB/server/commit/1c92406337) 2019-11-20 14:11:54 +0800 - Merge 10.3 into 10.4
* Merge [Revision #589a1235b6](https://github.com/MariaDB/server/commit/589a1235b6) 2019-11-19 01:32:50 +0200 - Merge 10.3 into 10.4
* [Revision #77a245fe56](https://github.com/MariaDB/server/commit/77a245fe56)\
  2019-11-17 20:04:11 +0200
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Remove an unused return value
* [Revision #009674dc52](https://github.com/MariaDB/server/commit/009674dc52)\
  2019-11-15 15:37:25 +0100
  * Fix a couple of clang-cl warnings
* [Revision #6df0bb7d38](https://github.com/MariaDB/server/commit/6df0bb7d38)\
  2019-11-13 21:12:48 +0100
  * [MDEV-21062](https://jira.mariadb.org/browse/MDEV-21062) Buildbot, Windows - sporadically missing lines from mtr's "exec"
* Merge [Revision #89ae01fd00](https://github.com/MariaDB/server/commit/89ae01fd00) 2019-11-14 13:23:36 +0200 - Merge 10.3 into 10.4
* Merge [Revision #746ee78535](https://github.com/MariaDB/server/commit/746ee78535) 2019-11-14 13:22:29 +0200 - [MDEV-20949](https://jira.mariadb.org/browse/MDEV-20949): Merge 10.3 into 10.4
* Merge [Revision #3bee95d769](https://github.com/MariaDB/server/commit/3bee95d769) 2019-11-14 13:20:57 +0200 - Merge 10.3 into 10.4
* [Revision #caa79081c3](https://github.com/MariaDB/server/commit/caa79081c3)\
  2019-10-14 12:08:28 +0530
  * [MDEV-20707](https://jira.mariadb.org/browse/MDEV-20707): Missing memory barrier in parallel replication error handler in wait\_for\_prior\_commit()
* [Revision #49019dde65](https://github.com/MariaDB/server/commit/49019dde65)\
  2019-11-13 18:35:04 +0200
  * [MDEV-17138](https://jira.mariadb.org/browse/MDEV-17138) follow-up: Optimize index page creation
* [Revision #2b7aa60b7e](https://github.com/MariaDB/server/commit/2b7aa60b7e)\
  2019-11-13 14:34:52 +0200
  * Use constexpr for constants on data pages
* [Revision #ae72205e31](https://github.com/MariaDB/server/commit/ae72205e31)\
  2019-11-12 18:15:26 +0700
  * cleanup: replace List\_iterator(\_fast) in handler0alter.cc
* [Revision #83a0eaec08](https://github.com/MariaDB/server/commit/83a0eaec08)\
  2019-11-13 00:32:27 +0900
  * [MDEV-18987](https://jira.mariadb.org/browse/MDEV-18987) bug in "load data local infile xxx replace into " (#1408)
* Merge [Revision #33cb10d4e9](https://github.com/MariaDB/server/commit/33cb10d4e9) 2019-11-12 16:55:44 +0200 - Merge 10.3 into 10.4
* [Revision #e5f99a0c0c](https://github.com/MariaDB/server/commit/e5f99a0c0c)\
  2019-10-30 13:55:52 +0300
  * [MDEV-20297](https://jira.mariadb.org/browse/MDEV-20297) Support C++11 range-based for loop for List
* [Revision #0308de94ee](https://github.com/MariaDB/server/commit/0308de94ee)\
  2019-11-11 15:09:23 +0200
  * [MDEV-17138](https://jira.mariadb.org/browse/MDEV-17138) follow-up: Optimize fseg\_create()
* Merge [Revision #3da895a736](https://github.com/MariaDB/server/commit/3da895a736) 2019-11-11 15:03:46 +0200 - Merge 10.3 into 10.4
* [Revision #74892bda3a](https://github.com/MariaDB/server/commit/74892bda3a)\
  2019-11-08 09:53:06 -0500
  * bump the VERSION
* [Revision #15b713cadc](https://github.com/MariaDB/server/commit/15b713cadc)\
  2019-11-08 13:36:20 +0200
  * [MDEV-17138](https://jira.mariadb.org/browse/MDEV-17138) follow-up: Use MLOG\_MEMSET in xdes\_init()
* [Revision #78d0d2cdc5](https://github.com/MariaDB/server/commit/78d0d2cdc5)\
  2019-11-08 09:41:06 +0200
  * Cleanup: Remove mach\_read\_ulint()
* [Revision #8a5eb4141b](https://github.com/MariaDB/server/commit/8a5eb4141b)\
  2019-11-08 08:59:59 +0200
  * [MDEV-17138](https://jira.mariadb.org/browse/MDEV-17138) follow-up: Use MLOG\_MEMSET for writing FIL\_NULL

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
