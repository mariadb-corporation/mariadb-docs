# MariaDB 10.3.22 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.22/)[Release Notes](../../old-releases/10.3/10.3.22.md)[Changelog](mariadb-10322-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 28 Jan 2020

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.22.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.31](../changelogs-mariadb-102-series/mariadb-10231-changelog.md)
* [Revision #0152704ae3](https://github.com/MariaDB/server/commit/0152704ae3)\
  2020-01-26 20:34:09 +0200
  * List of unstable tests for 10.3.22 release
* Merge [Revision #e10e922afd](https://github.com/MariaDB/server/commit/e10e922afd) 2020-01-25 16:09:34 +0100 - Merge branch '[MDEV-21383](https://jira.mariadb.org/browse/MDEV-21383)' into 10.3
* [Revision #7e8a58020b](https://github.com/MariaDB/server/commit/7e8a58020b)\
  2020-01-20 00:06:51 +0300
  * [MDEV-21383](https://jira.mariadb.org/browse/MDEV-21383): Possible range plan is not used under certain conditions
* Merge [Revision #ceda5f724f](https://github.com/MariaDB/server/commit/ceda5f724f) 2020-01-24 14:16:20 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #ade89fc898](https://github.com/MariaDB/server/commit/ade89fc898) 2020-01-21 09:11:14 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #bc43bf3e43](https://github.com/MariaDB/server/commit/bc43bf3e43) 2020-01-20 08:41:52 +0200 - Merge 10.2 into 10.3
* [Revision #9be5c19c34](https://github.com/MariaDB/server/commit/9be5c19c34)\
  2020-01-19 21:16:15 +0300
  * Fix another trivial merge error
* Merge [Revision #6373ec3ec7](https://github.com/MariaDB/server/commit/6373ec3ec7) 2020-01-18 16:56:16 +0200 - Merge 10.2 into 10.3
* Merge [Revision #e709eb9bf7](https://github.com/MariaDB/server/commit/e709eb9bf7) 2020-01-17 00:46:40 +0300 - Merge branch '10.2' into 10.3
* [Revision #d531b4ee3a](https://github.com/MariaDB/server/commit/d531b4ee3a)\
  2020-01-12 22:15:55 +0300
  * [MDEV-21341](https://jira.mariadb.org/browse/MDEV-21341): Fix UBSAN failures: Issue Six
* [Revision #9c3eca8514](https://github.com/MariaDB/server/commit/9c3eca8514)\
  2019-12-07 18:21:36 +0300
  * [MDEV-21243](https://jira.mariadb.org/browse/MDEV-21243): Join buffer: condition is checked in wrong place for range access
* [Revision #cba9ed1279](https://github.com/MariaDB/server/commit/cba9ed1279)\
  2020-01-08 00:51:04 +0700
  * fix compilation
* Merge [Revision #b365b6e7d8](https://github.com/MariaDB/server/commit/b365b6e7d8) 2020-01-08 13:44:06 +0530 - Merge branch '10.2' into 10.3
* Merge [Revision #eda719793a](https://github.com/MariaDB/server/commit/eda719793a) 2020-01-07 12:14:35 +0200 - Merge 10.2 into 10.3
* Merge [Revision #7753a29064](https://github.com/MariaDB/server/commit/7753a29064) 2020-01-03 13:44:16 +0100 - Merge branch '10.2' into 10.3
* [Revision #02e3006957](https://github.com/MariaDB/server/commit/02e3006957)\
  2019-12-30 10:08:18 +0200
  * [MDEV-21405](https://jira.mariadb.org/browse/MDEV-21405) Assertion failed on instant ADD COLUMN
* [Revision #4923604ee2](https://github.com/MariaDB/server/commit/4923604ee2)\
  2019-03-24 19:01:54 +1000
  * [MDEV-18865](https://jira.mariadb.org/browse/MDEV-18865) Assertion \`t->first->versioned\_by\_id()' failed in innodb\_prepare\_commit\_versioned
* [Revision #720e9bd5be](https://github.com/MariaDB/server/commit/720e9bd5be)\
  2019-03-22 16:26:42 +1000
  * [MDEV-18875](https://jira.mariadb.org/browse/MDEV-18875) Assertion \`\`thd->transaction.stmt.ha\_list == \_\_null || trans == \&thd->transaction.stmt'\` failed or bogus ER\_DUP\_ENTRY upon ALTER TABLE with versioning
* [Revision #808bc919eb](https://github.com/MariaDB/server/commit/808bc919eb)\
  2019-12-27 17:04:47 +0200
  * Re-record funcs\_1.is\_columns\_is\_embedded after a merge
* [Revision #1d9532cd8b](https://github.com/MariaDB/server/commit/1d9532cd8b)\
  2019-12-27 18:22:16 +0400
  * After-merge cleanup
* Merge [Revision #5ab70e7f68](https://github.com/MariaDB/server/commit/5ab70e7f68) 2019-12-27 13:05:06 +0200 - Merge 10.2 into 10.3
* [Revision #ee9a19fb05](https://github.com/MariaDB/server/commit/ee9a19fb05)\
  2019-12-25 12:23:24 +0400
  * [MDEV-21392](https://jira.mariadb.org/browse/MDEV-21392) Cleanup redundant overriding in Item\_sum\_num
* [Revision #b21dc11986](https://github.com/MariaDB/server/commit/b21dc11986)\
  2019-12-24 18:10:18 +0400
  * [MDEV-21389](https://jira.mariadb.org/browse/MDEV-21389) Derive Item\_func\_month from Item\_long\_func
* [Revision #59a088744d](https://github.com/MariaDB/server/commit/59a088744d)\
  2019-12-16 13:40:00 +0200
  * Remove unused mlog\_catenate\_ulint\_compressed()
* [Revision #cf0823f9b5](https://github.com/MariaDB/server/commit/cf0823f9b5)\
  2019-12-13 20:52:44 +0200
  * Update test result post merge
* Merge [Revision #193b5ed50b](https://github.com/MariaDB/server/commit/193b5ed50b) 2019-12-13 16:36:46 +0200 - Merge branch '10.2' into 10.3
* [Revision #a134f1ebb1](https://github.com/MariaDB/server/commit/a134f1ebb1)\
  2019-01-24 03:06:56 -0800
  * PR #1127 and PR #1150
* Merge [Revision #3466b47b0d](https://github.com/MariaDB/server/commit/3466b47b0d) 2019-12-13 10:08:57 +0200 - Merge 10.2 into 10.3
* Merge [Revision #0a20e5ab77](https://github.com/MariaDB/server/commit/0a20e5ab77) 2019-12-12 14:41:51 +0200 - Merge 10.2 into 10.3
* [Revision #e0f9540bcc](https://github.com/MariaDB/server/commit/e0f9540bcc)\
  2019-12-11 15:09:17 +0400
  * [MDEV-20667](https://jira.mariadb.org/browse/MDEV-20667) Server crash on pop\_cursor
* [Revision #ce47e66516](https://github.com/MariaDB/server/commit/ce47e66516)\
  2019-12-11 13:03:16 -0500
  * bump the VERSION
* [Revision #246e2ae12b](https://github.com/MariaDB/server/commit/246e2ae12b)\
  2019-12-04 20:04:45 +0530
  * [MDEV-20900](https://jira.mariadb.org/browse/MDEV-20900): IN predicate to IN subquery conversion causes performance regression

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
