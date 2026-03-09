# MariaDB 10.5.18 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.18](https://downloads.mariadb.org/mariadb/10.5.18/)[Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10-5-18-release-notes)[Changelog](mariadb-10-5-18-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 7 Nov 2022

For the highlights of this release, see the [release notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.27](../changelogs-mariadb-10-4-series/mariadb-10-4-27-changelog.md)
* Merge [Revision #177d858e38](https://github.com/MariaDB/server/commit/177d858e38) 2022-11-02 13:14:54 +0100 - Merge branch '10.4' into 10.5
* [Revision #b4a58581fd](https://github.com/MariaDB/server/commit/b4a58581fd)\
  2022-10-26 17:18:19 +0200
  * columnstore 5.6.8-1
* Merge [Revision #4519b42e61](https://github.com/MariaDB/server/commit/4519b42e61) 2022-10-26 15:26:06 +0200 - Merge branch '10.4' into 10.5
* [Revision #f90d9c347f](https://github.com/MariaDB/server/commit/f90d9c347f)\
  2022-10-04 11:44:14 +0400
  * [MDEV-28822](https://jira.mariadb.org/browse/MDEV-28822) Table from older version requires table rebuild when adding column to table with multi-column index
* [Revision #42802ad66c](https://github.com/MariaDB/server/commit/42802ad66c)\
  2022-09-14 15:08:12 -0600
  * [MDEV-25616](https://jira.mariadb.org/browse/MDEV-25616) XA PREPARE event group is not binlogged when..
* [Revision #4b4c2b8cc0](https://github.com/MariaDB/server/commit/4b4c2b8cc0)\
  2022-10-25 11:43:59 +0300
  * Merge 10.4 into 10.5
* Merge [Revision #9a0b9e3360](https://github.com/MariaDB/server/commit/9a0b9e3360) 2022-10-25 11:26:37 +0300 - Merge 10.4 into 10.5
* [Revision #2f7a0072b6](https://github.com/MariaDB/server/commit/2f7a0072b6)\
  2022-10-24 16:05:32 +0200
  * [MDEV-28701](https://jira.mariadb.org/browse/MDEV-28701) Update 10.5 HELP tables
* [Revision #8128a46827](https://github.com/MariaDB/server/commit/8128a46827)\
  2022-06-29 17:03:56 +0300
  * [MDEV-28709](https://jira.mariadb.org/browse/MDEV-28709) unexpected X lock on Supremum in READ COMMITTED
* [Revision #ce2825a867](https://github.com/MariaDB/server/commit/ce2825a867)\
  2022-10-24 14:40:29 +0100
  * Fix Aria S3 building in FreeBSD (#2242)
* [Revision #dca4fc24a2](https://github.com/MariaDB/server/commit/dca4fc24a2)\
  2022-10-21 02:17:25 -0700
  * Deb: Use archive.mariadb.org for upgrade testing in Salsa-CI (#2294)
* [Revision #7afc6ee8bc](https://github.com/MariaDB/server/commit/7afc6ee8bc)\
  2022-09-23 18:28:12 +1000
  * [MDEV-29615](https://jira.mariadb.org/browse/MDEV-29615) mtr to use mariadb names
* [Revision #99e14aa592](https://github.com/MariaDB/server/commit/99e14aa592)\
  2021-05-10 18:36:13 +0300
  * [MDEV-25606](https://jira.mariadb.org/browse/MDEV-25606): Concurrent CREATE TRIGGER statements mix up in binlog and break replication
* [Revision #81ad6787cc](https://github.com/MariaDB/server/commit/81ad6787cc)\
  2022-10-18 19:44:07 +0300
  * [MDEV-29508](https://jira.mariadb.org/browse/MDEV-29508) perfschema.short\_option\_1 fails with MSAN - Error in accept
* [Revision #55227234cc](https://github.com/MariaDB/server/commit/55227234cc)\
  2022-10-19 19:52:16 +1100
  * [MDEV-26872](https://jira.mariadb.org/browse/MDEV-26872) perfschema.prepared\_statements non-deterministic test failure (#2290)
* Merge [Revision #6b8c43baac](https://github.com/MariaDB/server/commit/6b8c43baac) 2022-10-14 12:28:32 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #2a62e61511](https://github.com/MariaDB/server/commit/2a62e61511) 2022-10-14 12:25:11 +0200 - Merge branch 'bb-10.5-vp-[MDEV-27691](https://jira.mariadb.org/browse/MDEV-27691)' into 10.5
* [Revision #2abf499c76](https://github.com/MariaDB/server/commit/2abf499c76)\
  2022-09-16 17:55:42 +0700
  * [MDEV-27691](https://jira.mariadb.org/browse/MDEV-27691): make working view-protocol
* Merge [Revision #d444536e1d](https://github.com/MariaDB/server/commit/d444536e1d) 2022-09-26 10:24:59 +0700 - Merge branch 'bb-10.4-all-builders' into bb-10.5-all-builders
* Merge [Revision #66e44afd94](https://github.com/MariaDB/server/commit/66e44afd94) 2022-10-13 17:05:30 +0300 - Merge 10.4 into 10.5
* [Revision #5fffdbc8d5](https://github.com/MariaDB/server/commit/5fffdbc8d5)\
  2022-10-12 10:53:14 +0300
  * Fixes after 10.4 --> 10.5 merge
* Merge [Revision #977c385df3](https://github.com/MariaDB/server/commit/977c385df3) 2022-10-12 11:29:32 +0300 - Merge 10.4 into 10.5
* [Revision #fa0cada95b](https://github.com/MariaDB/server/commit/fa0cada95b)\
  2022-10-07 00:45:21 +0300
  * [MDEV-28576](https://jira.mariadb.org/browse/MDEV-28576) RENAME COLUMN with NOCOPY algorithm leads to corrupt partitioned table
* Merge [Revision #74fe1c44aa](https://github.com/MariaDB/server/commit/74fe1c44aa) 2022-10-07 00:42:55 +0300 - Merge 10.4 into 10.5
* [Revision #5e66b63d95](https://github.com/MariaDB/server/commit/5e66b63d95)\
  2022-10-06 12:33:05 +0300
  * [MDEV-29710](https://jira.mariadb.org/browse/MDEV-29710): Disable a timing-sensitive test on Valgrind
* [Revision #d766a799f4](https://github.com/MariaDB/server/commit/d766a799f4)\
  2022-10-06 11:58:28 +0300
  * [MDEV-29508](https://jira.mariadb.org/browse/MDEV-29508) work-around: Disable hanging test on Valgrind
* [Revision #8d6421aa48](https://github.com/MariaDB/server/commit/8d6421aa48)\
  2022-10-06 08:45:42 +0300
  * MemorySanitizer: Disable tests that time out
* [Revision #f54bc7deb7](https://github.com/MariaDB/server/commit/f54bc7deb7)\
  2022-10-06 08:42:26 +0300
  * [MDEV-29710](https://jira.mariadb.org/browse/MDEV-29710): Disable some slow tests on Valgrind
* Merge [Revision #de078e060e](https://github.com/MariaDB/server/commit/de078e060e) 2022-10-06 08:29:56 +0300 - Merge 10.4 into 10.5
* [Revision #2154a1fc35](https://github.com/MariaDB/server/commit/2154a1fc35)\
  2022-09-29 18:50:29 +0900
  * [MDEV-29484](https://jira.mariadb.org/browse/MDEV-29484) Assertion \`!trx\_free || !trx->locked\_connections' failed in spider\_free\_trx\_conn on LOCK TABLES
* [Revision #7865c8c9a2](https://github.com/MariaDB/server/commit/7865c8c9a2)\
  2022-09-26 13:29:10 +0530
  * Crash in INSERT...SELECT..RETURNING with subquery
* Merge [Revision #3a2116241b](https://github.com/MariaDB/server/commit/3a2116241b) 2022-10-02 14:38:13 +0200 - Merge branch '10.4' into 10.5
* [Revision #e29fb95614](https://github.com/MariaDB/server/commit/e29fb95614)\
  2022-09-30 08:25:00 +0300
  * Cleanup: Remove innobase\_destroy\_background\_thd()
* [Revision #6b685ea7b0](https://github.com/MariaDB/server/commit/6b685ea7b0)\
  2022-09-28 18:55:15 +0200
  * correctness assert
* [Revision #de130323b4](https://github.com/MariaDB/server/commit/de130323b4)\
  2022-09-28 14:27:55 +0200
  * [MDEV-29368](https://jira.mariadb.org/browse/MDEV-29368) Assertion \`trx->mysql\_thd == thd' failed in innobase\_kill\_query from process\_timers/timer\_handler and use-after-poison in innobase\_kill\_query
* [Revision #74ac683a7e](https://github.com/MariaDB/server/commit/74ac683a7e)\
  2022-09-28 14:43:30 +0200
  * cleanup: kill test
* [Revision #d7d3ad698a](https://github.com/MariaDB/server/commit/d7d3ad698a)\
  2022-09-28 13:00:38 +0200
  * debug\_sync: ignore "sort" kills and disconnects
* [Revision #620d520d68](https://github.com/MariaDB/server/commit/620d520d68)\
  2022-09-29 00:20:23 +1000
  * [MDEV-29614](https://jira.mariadb.org/browse/MDEV-29614) mariadb-upgrade calls mysql and mysql-check (#2279)
* [Revision #fe7c95ec78](https://github.com/MariaDB/server/commit/fe7c95ec78)\
  2022-09-26 13:45:53 +0300
  * Cleanup: Declare srv\_shutdown\_bg\_undo\_sources() static
* Merge [Revision #6286a05d80](https://github.com/MariaDB/server/commit/6286a05d80) 2022-09-26 13:34:38 +0300 - Merge 10.4 into 10.5
* Merge [Revision #0792aff161](https://github.com/MariaDB/server/commit/0792aff161) 2022-09-20 13:17:02 +0300 - Merge 10.4 into 10.5
* [Revision #fed0d85de7](https://github.com/MariaDB/server/commit/fed0d85de7)\
  2022-09-19 11:46:25 +0300
  * [MDEV-29559](https://jira.mariadb.org/browse/MDEV-29559) Recovery of INSERT\_HEAP\_DYNAMIC into secondary index fails
* Merge [Revision #3c8674edcc](https://github.com/MariaDB/server/commit/3c8674edcc) 2022-09-19 17:03:17 +1000 - Merge 10.4 into 10.5
* [Revision #01d78d31ca](https://github.com/MariaDB/server/commit/01d78d31ca)\
  2022-09-17 01:18:42 +0200
  * Update 10.5 HELP contents
* [Revision #23a8654cdb](https://github.com/MariaDB/server/commit/23a8654cdb)\
  2022-09-15 12:20:50 +0400
  * A cleanup for [MDEV-29446](https://jira.mariadb.org/browse/MDEV-29446) Change SHOW CREATE TABLE to display default collation
* [Revision #2fd4d25d8f](https://github.com/MariaDB/server/commit/2fd4d25d8f)\
  2022-09-15 07:44:35 +0400
  * A cleanup for [MDEV-29446](https://jira.mariadb.org/browse/MDEV-29446) Change SHOW CREATE TABLE to display default collation
* [Revision #35e18c240b](https://github.com/MariaDB/server/commit/35e18c240b)\
  2022-09-14 19:59:05 +0200
  * race condition in the test
* [Revision #b65ffe156a](https://github.com/MariaDB/server/commit/b65ffe156a)\
  2022-09-14 19:01:26 +0400
  * A cleanup for [MDEV-29446](https://jira.mariadb.org/browse/MDEV-29446) Change SHOW CREATE TABLE to display default collation
* Merge [Revision #fe844c16b6](https://github.com/MariaDB/server/commit/fe844c16b6) 2022-09-14 15:00:09 +0400 - Merge remote-tracking branch 'origin/10.4' into 10.5
* [Revision #fb70bb44d0](https://github.com/MariaDB/server/commit/fb70bb44d0)\
  2022-09-12 12:10:10 +0200
  * [MDEV-29513](https://jira.mariadb.org/browse/MDEV-29513) avoid useless os\_thread\_sleep() during srv\_purge\_shutdown()
* [Revision #bc12478a9a](https://github.com/MariaDB/server/commit/bc12478a9a)\
  2022-08-16 20:03:15 +0300
  * [MDEV-24660](https://jira.mariadb.org/browse/MDEV-24660) MYSQL\_BIN\_LOG::cleanup(): Assertion \`b->xid\_count == 0'
* [Revision #5563202089](https://github.com/MariaDB/server/commit/5563202089)\
  2022-08-30 00:26:20 +0300
  * [MDEV-29322](https://jira.mariadb.org/browse/MDEV-29322) ASAN heap-use-after-free in Query\_log\_event::do\_apply\_event
* Merge [Revision #80cf7a4c43](https://github.com/MariaDB/server/commit/80cf7a4c43) 2022-09-07 15:28:58 +0200 - Merge branch '10.4' into 10.5
* [Revision #dd092bc6eb](https://github.com/MariaDB/server/commit/dd092bc6eb)\
  2022-09-07 19:58:55 +1000
  * Deb: add kinetic to autobake (#2250)
* Merge [Revision #38d36b59f9](https://github.com/MariaDB/server/commit/38d36b59f9) 2022-09-07 08:26:21 +0300 - Merge 10.4 into 10.5
* [Revision #38dda1f026](https://github.com/MariaDB/server/commit/38dda1f026)\
  2022-09-06 15:11:24 +0300
  * [MDEV-29475](https://jira.mariadb.org/browse/MDEV-29475) trx\_undo\_rseg\_free() does not write redo log
* [Revision #c0470caf5a](https://github.com/MariaDB/server/commit/c0470caf5a)\
  2022-09-06 11:33:52 +0300
  * [MDEV-29471](https://jira.mariadb.org/browse/MDEV-29471) Buffer overflow in page\_cur\_insert\_rec\_low()
* Merge [Revision #ba987a46c9](https://github.com/MariaDB/server/commit/ba987a46c9) 2022-09-05 13:28:56 +0300 - Merge 10.4 into 10.5
* [Revision #244fdc435d](https://github.com/MariaDB/server/commit/244fdc435d)\
  2022-09-05 09:54:47 +0300
  * [MDEV-29438](https://jira.mariadb.org/browse/MDEV-29438) Recovery or backup of instant ALTER TABLE is incorrect
* [Revision #5cbc5dbbbe](https://github.com/MariaDB/server/commit/5cbc5dbbbe)\
  2022-08-31 13:00:16 +1000
  * [MDEV-29418](https://jira.mariadb.org/browse/MDEV-29418) linux uuid implementation returning non-hwaddr based suffix
* Merge [Revision #43037a5a48](https://github.com/MariaDB/server/commit/43037a5a48) 2022-08-31 11:06:14 +1000 - Merge branch 10.4 into 10.5
* Merge [Revision #29fa9bcee0](https://github.com/MariaDB/server/commit/29fa9bcee0) 2022-08-30 12:29:04 +0300 - Merge 10.4 into 10.5
* [Revision #0324bde846](https://github.com/MariaDB/server/commit/0324bde846)\
  2022-08-26 10:20:26 +1000
  * mariadb-backup: remove MySQL wording
* [Revision #79b58f1ca8](https://github.com/MariaDB/server/commit/79b58f1ca8)\
  2022-07-30 00:11:08 +1000
  * [MDEV-23607](https://jira.mariadb.org/browse/MDEV-23607) mariadb-backup - align required GRANTS to cmd options
* Merge [Revision #9929301ecd](https://github.com/MariaDB/server/commit/9929301ecd) 2022-08-25 15:31:19 +0300 - Merge 10.4 into 10.5
* [Revision #a3fd9e6b06](https://github.com/MariaDB/server/commit/a3fd9e6b06)\
  2022-08-24 10:09:27 +0200
  * [MDEV-29367](https://jira.mariadb.org/browse/MDEV-29367) Refactor tpool::cache
* Merge [Revision #720fa05e5b](https://github.com/MariaDB/server/commit/720fa05e5b) 2022-08-23 20:59:34 +0900 - Merge 10.4 into 10.5
* [Revision #55c648a738](https://github.com/MariaDB/server/commit/55c648a738)\
  2022-08-23 08:58:23 +0400
  * [MDEV-27099](https://jira.mariadb.org/browse/MDEV-27099) Subquery using the ALL keyword on INET6 columns produces a wrong result
* Merge [Revision #3b656ac8c1](https://github.com/MariaDB/server/commit/3b656ac8c1) 2022-08-22 19:49:56 +0300 - Merge 10.4 into 10.5
* Merge [Revision #1d90d6874d](https://github.com/MariaDB/server/commit/1d90d6874d) 2022-08-22 13:38:40 +0300 - Merge 10.4 into 10.5
* Merge [Revision #5fc172fd43](https://github.com/MariaDB/server/commit/5fc172fd43) 2022-08-15 10:37:33 +0200 - Merge branch '10.5' into bb-10.5-release
* [Revision #fd1e5f91d2](https://github.com/MariaDB/server/commit/fd1e5f91d2)\
  2022-08-14 22:53:37 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
