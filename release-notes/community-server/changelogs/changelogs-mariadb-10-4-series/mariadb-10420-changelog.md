# MariaDB 10.4.20 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.20](https://downloads.mariadb.org/mariadb/10.4.20/)[Release Notes](../../old-releases/10.4/10.4.20.md)[Changelog](mariadb-10420-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 23 Jun 2021

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.20.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.30](../changelogs-mariadb-10-3-series/mariadb-10330-changelog.md)
* Merge [Revision #c7ee039d36](https://github.com/MariaDB/server/commit/c7ee039d36) 2021-06-09 14:28:57 +0300 - Merge 10.3 to 10.4
* [Revision #b8d38c5e39](https://github.com/MariaDB/server/commit/b8d38c5e39)\
  2021-06-08 15:03:50 +0300
  * dict\_index\_build\_internal\_clust(): Catch [MDEV-20131](https://jira.mariadb.org/browse/MDEV-20131) on CREATE TABLE
* Merge [Revision #72b2489621](https://github.com/MariaDB/server/commit/72b2489621) 2021-06-08 15:02:40 +0300 - Merge 10.3 into 10.4
* [Revision #bb28bffc3e](https://github.com/MariaDB/server/commit/bb28bffc3e)\
  2021-06-07 19:51:57 -0700
  * Ported the test case for [MDEV-25682](https://jira.mariadb.org/browse/MDEV-25682) from 10.2
* [Revision #ddddfc33c7](https://github.com/MariaDB/server/commit/ddddfc33c7)\
  2021-06-04 14:57:11 +0200
  * Fix mtr tests with file\_key\_managment extension for Windows
* Merge [Revision #bab4348c6c](https://github.com/MariaDB/server/commit/bab4348c6c) 2021-06-04 09:42:18 +0300 - Merge 10.3 into 10.4
* [Revision #385f4316c3](https://github.com/MariaDB/server/commit/385f4316c3)\
  2021-06-03 20:43:04 -0700
  * Corrected the test case of [MDEV-25714](https://jira.mariadb.org/browse/MDEV-25714) in order to have the same EXPLAIN output as in 10.3
* [Revision #0b797130c6](https://github.com/MariaDB/server/commit/0b797130c6)\
  2021-05-26 23:41:59 -0700
  * [MDEV-25714](https://jira.mariadb.org/browse/MDEV-25714) Join using derived with aggregation returns incorrect results
* [Revision #fa0bbff032](https://github.com/MariaDB/server/commit/fa0bbff032)\
  2021-06-02 14:05:12 +0300
  * Fixed that compile-pentium64-valgrind-max works
* Merge [Revision #d3d2c96567](https://github.com/MariaDB/server/commit/d3d2c96567) 2021-06-02 08:29:47 +0300 - Merge 10.3 into 10.4
* Merge [Revision #77d8da57d7](https://github.com/MariaDB/server/commit/77d8da57d7) 2021-06-01 09:14:59 +0300 - Merge 10.3 into 10.4
* [Revision #26f9ff0a60](https://github.com/MariaDB/server/commit/26f9ff0a60)\
  2021-05-26 11:11:27 +0300
  * Remove unnecessary test case
* [Revision #88ce7cf744](https://github.com/MariaDB/server/commit/88ce7cf744)\
  2021-05-26 09:06:32 +0300
  * [MDEV-25769](https://jira.mariadb.org/browse/MDEV-25769) : Galera test failure on galera\_sr.GCF-627
* [Revision #e212415690](https://github.com/MariaDB/server/commit/e212415690)\
  2021-05-24 18:58:57 +0300
  * [MDEV-25551](https://jira.mariadb.org/browse/MDEV-25551) applying crash with tables without PK
* Merge [Revision #1dea7f7977](https://github.com/MariaDB/server/commit/1dea7f7977) 2021-05-25 15:38:57 +0300 - Merge 10.3 into 10.4
* [Revision #04de651725](https://github.com/MariaDB/server/commit/04de651725)\
  2021-05-25 00:43:03 -0700
  * [MDEV-23886](https://jira.mariadb.org/browse/MDEV-23886) Reusing CTE inside a function fails with table doesn't exist
* [Revision #67083ca4f3](https://github.com/MariaDB/server/commit/67083ca4f3)\
  2021-05-22 01:17:46 +0200
  * [MDEV-25719](https://jira.mariadb.org/browse/MDEV-25719) post-merge correction: wsrep\_debug=ON -> wsrep\_debug=1
* [Revision #8e280f3007](https://github.com/MariaDB/server/commit/8e280f3007)\
  2021-05-21 03:38:04 +0200
  * [MDEV-25719](https://jira.mariadb.org/browse/MDEV-25719): stunnel uses "verifyChain" without subject checks
* [Revision #5667baad5d](https://github.com/MariaDB/server/commit/5667baad5d)\
  2021-05-20 09:56:53 +0200
  * [MDEV-25562](https://jira.mariadb.org/browse/MDEV-25562) Assertion \`pause\_seqno\_.is\_undefined() == false' failed in void wsrep::server\_state::resume()
* [Revision #08b6fd9395](https://github.com/MariaDB/server/commit/08b6fd9395)\
  2021-05-18 12:13:18 +0300
  * [MDEV-25710](https://jira.mariadb.org/browse/MDEV-25710): Dead code os\_file\_opendir() in the server
* Merge [Revision #4240704abc](https://github.com/MariaDB/server/commit/4240704abc) 2021-05-18 08:59:12 +0300 - Merge 10.3 into 10.4
* [Revision #e861e057ad](https://github.com/MariaDB/server/commit/e861e057ad)\
  2021-05-17 19:51:49 +0200
  * [MDEV-25693](https://jira.mariadb.org/browse/MDEV-25693): SST failed due to incorrect connection address
* [Revision #cf4dd3cc81](https://github.com/MariaDB/server/commit/cf4dd3cc81)\
  2021-05-17 18:59:26 +0200
  * wsrep\_sst\_common.sh: file mode changed back to 664
* [Revision #f9f8e33f29](https://github.com/MariaDB/server/commit/f9f8e33f29)\
  2021-05-14 12:51:36 +0200
  * [MDEV-25669](https://jira.mariadb.org/browse/MDEV-25669): SST scripts should check all server groups in config files
* [Revision #16898e7f11](https://github.com/MariaDB/server/commit/16898e7f11)\
  2021-05-13 12:23:11 +0200
  * Added missing connection lines to some tests
* [Revision #9aac079a84](https://github.com/MariaDB/server/commit/9aac079a84)\
  2021-05-11 10:04:52 +0200
  * [MDEV-23580](https://jira.mariadb.org/browse/MDEV-23580) addendum: normal operation in configurations where stunnel is not available
* [Revision #27ae7f2a26](https://github.com/MariaDB/server/commit/27ae7f2a26)\
  2021-05-10 04:27:16 +0200
  * [MDEV-23580](https://jira.mariadb.org/browse/MDEV-23580): WSREP\_SST: \[ERROR] rsync daemon port has been taken
* [Revision #b2bb747f8c](https://github.com/MariaDB/server/commit/b2bb747f8c)\
  2021-05-10 11:11:21 -0400
  * bump the VERSION
* Merge [Revision #8c73fab7f7](https://github.com/MariaDB/server/commit/8c73fab7f7) 2021-05-10 09:52:01 +0300 - Merge 10.3 into 10.4
* Merge [Revision #583b72ad0d](https://github.com/MariaDB/server/commit/583b72ad0d) 2021-05-07 11:50:24 +0200 - Merge branch 'bb-10.4-release' into 10.4
* [Revision #473e85e931](https://github.com/MariaDB/server/commit/473e85e931)\
  2021-05-04 08:44:56 +0300
  * [MDEV-25591](https://jira.mariadb.org/browse/MDEV-25591) : Test case cleanups

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
