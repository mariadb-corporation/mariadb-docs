# MariaDB 10.3.9 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.9)[Release Notes](../../old-releases/10.3/10.3.9.md)[Changelog](mariadb-1039-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 15 Aug 2018

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.9.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #ca26f91bca](https://github.com/MariaDB/server/commit/ca26f91bca)\
  2018-08-14 03:35:06 +0300
  * Updated list of unstable tests for 10.3.9 release
* [Revision #fac3e575b2](https://github.com/MariaDB/server/commit/fac3e575b2)\
  2018-08-13 12:22:55 +0200
  * fix third-party tool packaging on Win
* [Revision #a928751c78](https://github.com/MariaDB/server/commit/a928751c78)\
  2018-08-13 12:14:56 +0200
  * fix bundled pcre unit tests
* [Revision #5e7496e2ea](https://github.com/MariaDB/server/commit/5e7496e2ea)\
  2018-08-12 14:52:37 +0200
  * fix C/C packaging on debian
* Merge [Revision #0aa9b03393](https://github.com/MariaDB/server/commit/0aa9b03393) 2018-08-12 11:47:16 +0200 - Merge branch '10.2' into 10.3
* [Revision #655cba619d](https://github.com/MariaDB/server/commit/655cba619d)\
  2018-08-10 15:03:21 +0200
  * Update C/C to v3.0.6
* [Revision #456517b88e](https://github.com/MariaDB/server/commit/456517b88e)\
  2018-07-05 17:37:07 +0200
  * compiler warnings
* [Revision #97b563b5db](https://github.com/MariaDB/server/commit/97b563b5db)\
  2018-07-05 14:23:23 +0200
  * less re-cmake messages
* [Revision #8ca2219065](https://github.com/MariaDB/server/commit/8ca2219065)\
  2018-07-04 19:50:14 +0200
  * cmake .git warning
* [Revision #675e7e7dcc](https://github.com/MariaDB/server/commit/675e7e7dcc)\
  2018-07-04 18:21:47 +0200
  * remove obsolete checks for -fno-implicit-templates
* [Revision #889d8a8f2b](https://github.com/MariaDB/server/commit/889d8a8f2b)\
  2018-07-10 17:45:49 +0200
  * [MDEV-16662](https://jira.mariadb.org/browse/MDEV-16662) CMake warnings: CMP0045
* [Revision #9c195176a1](https://github.com/MariaDB/server/commit/9c195176a1)\
  2018-07-10 17:44:38 +0200
  * [MDEV-16662](https://jira.mariadb.org/browse/MDEV-16662) CMake warnings: CMP0042
* [Revision #6b53f9d781](https://github.com/MariaDB/server/commit/6b53f9d781)\
  2018-07-06 04:03:58 +0200
  * [MDEV-16662](https://jira.mariadb.org/browse/MDEV-16662) CMake warnings: CMP0026
* [Revision #96b8909062](https://github.com/MariaDB/server/commit/96b8909062)\
  2018-07-06 04:03:43 +0200
  * [MDEV-16662](https://jira.mariadb.org/browse/MDEV-16662) CMake warnings: CMP0022
* [Revision #aa19eda7da](https://github.com/MariaDB/server/commit/aa19eda7da)\
  2018-07-06 04:00:49 +0200
  * [MDEV-16662](https://jira.mariadb.org/browse/MDEV-16662) CMake warnings: CMP0007
* [Revision #a39337415d](https://github.com/MariaDB/server/commit/a39337415d)\
  2018-06-29 11:01:55 +0200
  * [MDEV-14900](https://jira.mariadb.org/browse/MDEV-14900) Upstream 10.3 debian patches
* [Revision #08b91548db](https://github.com/MariaDB/server/commit/08b91548db)\
  2018-07-09 11:05:34 +0200
  * [MDEV-16495](https://jira.mariadb.org/browse/MDEV-16495) mariadb segfaults at start on FreeBSD
* [Revision #10d347dc6a](https://github.com/MariaDB/server/commit/10d347dc6a)\
  2018-08-08 12:06:01 +0300
  * Deb: Make libmariadb3 Breaks+Replaces libmariadbclient18 so upgrade pass
* [Revision #340c8a2a32](https://github.com/MariaDB/server/commit/340c8a2a32)\
  2018-08-09 12:11:47 +0300
  * Remove set-but-not-used log\_sys.log.state
* [Revision #482d4da0a7](https://github.com/MariaDB/server/commit/482d4da0a7)\
  2018-08-07 16:05:48 +0530
  * [MDEV-15127](https://jira.mariadb.org/browse/MDEV-15127) AddressSanitizer: stack-buffer-overflow in base\_list::push\_back ..
* [Revision #4cbadaeaea](https://github.com/MariaDB/server/commit/4cbadaeaea)\
  2018-08-07 11:55:51 +0400
  * [MDEV-16891](https://jira.mariadb.org/browse/MDEV-16891) EVENTs created with SQL\_MODE=ORACLE fail to execute
* [Revision #cb1945dd0d](https://github.com/MariaDB/server/commit/cb1945dd0d)\
  2018-08-05 17:11:15 +0300
  * [MDEV-16666](https://jira.mariadb.org/browse/MDEV-16666): Partially revert "Deb: Update documentation and fix spelling errors"
* [Revision #3570ea9189](https://github.com/MariaDB/server/commit/3570ea9189)\
  2018-08-05 00:36:59 +0100
  * remove warning on Windows
* [Revision #f4e2db5b43](https://github.com/MariaDB/server/commit/f4e2db5b43)\
  2018-08-05 00:33:12 +0100
  * [MDEV-16544](https://jira.mariadb.org/browse/MDEV-16544) - crash in ha\_sphinx::create()
* [Revision #d453374fc4](https://github.com/MariaDB/server/commit/d453374fc4)\
  2018-08-03 14:54:02 -0700
  * [MDEV-16801](https://jira.mariadb.org/browse/MDEV-16801) seg\_fault on a query
* [Revision #7749745b7d](https://github.com/MariaDB/server/commit/7749745b7d)\
  2018-08-03 22:39:57 +0200
  * Fix of type, to make windows compiler happy.
* [Revision #aab5c557cf](https://github.com/MariaDB/server/commit/aab5c557cf)\
  2018-08-03 17:39:38 +0300
  * [MDEV-16830](https://jira.mariadb.org/browse/MDEV-16830) Crash in ALTER TABLE DROP FOREIGN KEY
* Merge [Revision #05459706f2](https://github.com/MariaDB/server/commit/05459706f2) 2018-08-03 15:57:23 +0300 - Merge 10.2 into 10.3
* [Revision #8ae2a2dbe6](https://github.com/MariaDB/server/commit/8ae2a2dbe6)\
  2018-08-03 09:03:11 +0400
  * [MDEV-15363](https://jira.mariadb.org/browse/MDEV-15363) Wrong result for CAST(LAST\_DAY(TIME'00:00:00') AS TIME)
* [Revision #89b6ce026a](https://github.com/MariaDB/server/commit/89b6ce026a)\
  2018-07-31 15:47:54 +0300
  * Disabled rocksdb.autoinc\_debug as it fails very often
* [Revision #a89a6e4f77](https://github.com/MariaDB/server/commit/a89a6e4f77)\
  2018-08-02 11:27:22 +0000
  * Added -j option to dpkg-buildpackage to speed up build
* [Revision #1b87cd80a2](https://github.com/MariaDB/server/commit/1b87cd80a2)\
  2018-08-02 10:48:55 +0400
  * [MDEV-16878](https://jira.mariadb.org/browse/MDEV-16878) Functions ADDTIME and SUBTIME get wrongly removed from WHERE by the equal expression optimizer
* [Revision #0c745c743c](https://github.com/MariaDB/server/commit/0c745c743c)\
  2018-07-29 10:56:11 +0300
  * Don't give warnings from perror or resolveip with safemalloc
* [Revision #255328d393](https://github.com/MariaDB/server/commit/255328d393)\
  2018-07-26 22:52:53 +0300
  * [MDEV-16131](https://jira.mariadb.org/browse/MDEV-16131) Assertion failed in dict\_index\_t::instant\_field\_value()
* [Revision #a97c190d95](https://github.com/MariaDB/server/commit/a97c190d95)\
  2018-07-24 18:01:30 +0300
  * [MDEV-16812](https://jira.mariadb.org/browse/MDEV-16812) Semisync slave io thread segfaults at STOP-SLAVE handling
* Merge [Revision #93b6552182](https://github.com/MariaDB/server/commit/93b6552182) 2018-07-26 08:54:44 +0300 - Merge 10.2 into 10.3
* Merge [Revision #294a426088](https://github.com/MariaDB/server/commit/294a426088) 2018-07-24 18:44:49 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* [Revision #f74d2a9faa](https://github.com/MariaDB/server/commit/f74d2a9faa)\
  2018-07-24 13:19:31 +0400
  * [MDEV-16729](https://jira.mariadb.org/browse/MDEV-16729) VARCHAR COMPRESSED is created with a wrong length for multi-byte character sets
* [Revision #a86a02a844](https://github.com/MariaDB/server/commit/a86a02a844)\
  2018-07-20 18:21:32 -0700
  * [MDEV-15786](https://jira.mariadb.org/browse/MDEV-15786): ERROR 1062 (23000) at line 365: Duplicate entry 'spider' for key 'PRIMARY'
* Merge [Revision #f418661efa](https://github.com/MariaDB/server/commit/f418661efa) 2018-07-23 18:56:52 +0300 - Merge 10.2 into 10.3
* [Revision #b9865b289a](https://github.com/MariaDB/server/commit/b9865b289a)\
  2018-07-23 12:09:59 +0300
  * Follow-up to [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Remove latch\_t::m\_temp\_fsp
* [Revision #141a5b2484](https://github.com/MariaDB/server/commit/141a5b2484)\
  2018-07-14 20:05:46 +0300
  * rpl\_row\_001.test failed in internal check
* [Revision #813b739850](https://github.com/MariaDB/server/commit/813b739850)\
  2018-07-09 16:09:20 -0700
  * [MDEV-16246](https://jira.mariadb.org/browse/MDEV-16246): insert timestamp into spider table from mysqldump gets wrong time zone.
* Merge [Revision #bbf780efcd](https://github.com/MariaDB/server/commit/bbf780efcd) 2018-07-07 11:39:38 +0300 - Merge 10.2 into 10.3
* Merge [Revision #934d5f95d3](https://github.com/MariaDB/server/commit/934d5f95d3) 2018-07-06 18:17:24 +0300 - Merge 10.2 into 10.3
* Merge [Revision #b4c377f215](https://github.com/MariaDB/server/commit/b4c377f215) 2018-07-05 17:08:44 +0300 - Merge 10.2 into 10.3
* [Revision #1748a31ae8](https://github.com/MariaDB/server/commit/1748a31ae8)\
  2018-07-03 15:10:06 +0300
  * [MDEV-16675](https://jira.mariadb.org/browse/MDEV-16675) Unnecessary explicit lock acquisition during UPDATE or DELETE
* Merge [Revision #186a998b5b](https://github.com/MariaDB/server/commit/186a998b5b) 2018-07-03 10:25:38 +0300 - Merge 10.2 into 10.3
* Merge [Revision #c3289d27ee](https://github.com/MariaDB/server/commit/c3289d27ee) 2018-07-03 10:22:43 +0300 - Merge mariadb-10.3.8 into 10.3
* [Revision #358ae4b46d](https://github.com/MariaDB/server/commit/358ae4b46d)\
  2018-07-02 20:55:10 -0400
  * bump the VERSION
* [Revision #71144afa96](https://github.com/MariaDB/server/commit/71144afa96)\
  2018-07-02 12:17:15 +0300
  * Update result
* [Revision #e86d7108a2](https://github.com/MariaDB/server/commit/e86d7108a2)\
  2018-07-02 12:14:19 +0300
  * Shorten some add\_suppression
* [Revision #502f1a3c11](https://github.com/MariaDB/server/commit/502f1a3c11)\
  2018-07-02 11:53:25 +0300
  * [MDEV-16623](https://jira.mariadb.org/browse/MDEV-16623) ASAN: use-after-free in create\_index()
* [Revision #6e90c195ed](https://github.com/MariaDB/server/commit/6e90c195ed)\
  2018-07-02 12:45:02 +0530
  * [MDEV-16365](https://jira.mariadb.org/browse/MDEV-16365) Setting a column NOT NULL fails to return error for NULL values when there is no DEFAULT
* [Revision #46857a860c](https://github.com/MariaDB/server/commit/46857a860c)\
  2018-06-30 10:28:51 +0300
  * Update travis test status and position in README file
* [Revision #5ef4870bb3](https://github.com/MariaDB/server/commit/5ef4870bb3)\
  2018-06-29 15:11:38 +0300
  * Travis-CI: Ensure AWS key management plugin is not built nor packaged
* [Revision #d6b26a8924](https://github.com/MariaDB/server/commit/d6b26a8924)\
  2018-06-29 17:29:00 +0300
  * Travis-CI: Don't build nor package the embedded server to save disk space
* [Revision #dbdaafb014](https://github.com/MariaDB/server/commit/dbdaafb014)\
  2018-06-29 17:02:08 +0300
  * autobake-deb: Stop packaging plugins that are not built
* [Revision #ecb0e0ade4](https://github.com/MariaDB/server/commit/ecb0e0ade4)\
  2018-06-29 13:54:01 +0300
  * autobake-deb: disable storage engines using -DPLUGIN
* [Revision #4d637628d3](https://github.com/MariaDB/server/commit/4d637628d3)\
  2018-06-29 13:51:33 +0300
  * [MDEV-16213](https://jira.mariadb.org/browse/MDEV-16213): Travis whitespace fix and remove comment
* [Revision #7b6e867288](https://github.com/MariaDB/server/commit/7b6e867288)\
  2018-06-29 11:17:28 +0300
  * [MDEV-16213](https://jira.mariadb.org/browse/MDEV-16213): Further improvements to the Travis config
* [Revision #1d5220ae23](https://github.com/MariaDB/server/commit/1d5220ae23)\
  2018-06-05 08:38:17 +0300
  * [MDEV-16213](https://jira.mariadb.org/browse/MDEV-16213): Exclude more engines from autobake-deb.sh
* [Revision #5cdc70b8a1](https://github.com/MariaDB/server/commit/5cdc70b8a1)\
  2018-05-29 10:26:01 +0300
  * [MDEV-16213](https://jira.mariadb.org/browse/MDEV-16213): Improvements and adjustments to Travis config

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
