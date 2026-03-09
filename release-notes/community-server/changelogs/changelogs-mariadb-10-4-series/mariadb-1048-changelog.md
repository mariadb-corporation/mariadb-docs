# MariaDB 10.4.8 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.8/)[Release Notes](../../old-releases/10.4/10.4.8.md)[Changelog](mariadb-1048-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 11 Sep 2019

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.8.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.18](../changelogs-mariadb-10-3-series/mariadb-10318-changelog.md)
* [Revision #4c2464b87d](https://github.com/MariaDB/server/commit/4c2464b87d)\
  2019-09-08 23:58:53 +0300
  * List of unstable tests for 10.4.8 release (updated)
* Merge [Revision #8885e7ba78](https://github.com/MariaDB/server/commit/8885e7ba78) 2019-09-06 20:12:11 +0200 - Merge branch '10.3' into 10.4
* [Revision #38e21c7000](https://github.com/MariaDB/server/commit/38e21c7000)\
  2019-09-06 17:31:02 +0200
  * various test failures post-merge
* Merge [Revision #244f0e6dd8](https://github.com/MariaDB/server/commit/244f0e6dd8) 2019-09-06 11:53:10 +0200 - Merge branch '10.3' into 10.4
* [Revision #18af13b88b](https://github.com/MariaDB/server/commit/18af13b88b)\
  2019-09-03 16:31:10 +0300
  * \[NFC] range-forify loops
* [Revision #7bccd2910f](https://github.com/MariaDB/server/commit/7bccd2910f)\
  2019-09-03 16:28:30 +0300
  * [MDEV-20479](https://jira.mariadb.org/browse/MDEV-20479) assertion failure in dict\_table\_get\_nth\_col() after INSTANT DROP COLUMN
* Merge [Revision #4f10d0918d](https://github.com/MariaDB/server/commit/4f10d0918d) 2019-09-02 14:57:05 +0200 - Merge branch '10.3' into 10.4
* [Revision #3ca68794c0](https://github.com/MariaDB/server/commit/3ca68794c0)\
  2019-08-06 00:11:05 +0200
  * [MDEV-20231](https://jira.mariadb.org/browse/MDEV-20231): [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) HELP Tables
* [Revision #de5f7348bd](https://github.com/MariaDB/server/commit/de5f7348bd)\
  2019-09-02 14:22:19 +0300
  * Make main.subselect\_sj2\* tests stable
* [Revision #b1e377997e](https://github.com/MariaDB/server/commit/b1e377997e)\
  2019-09-02 11:21:52 +0530
  * Fixed a typo
* [Revision #29b13d114e](https://github.com/MariaDB/server/commit/29b13d114e)\
  2019-09-02 00:06:31 +0530
  * Followup fix for [MDEV-20440](https://jira.mariadb.org/browse/MDEV-20440)
* Merge [Revision #db4a27ab73](https://github.com/MariaDB/server/commit/db4a27ab73) 2019-08-31 06:53:45 +0300 - Merge 10.3 into 10.4
* [Revision #d1ef02e959](https://github.com/MariaDB/server/commit/d1ef02e959)\
  2019-08-30 09:58:24 -0700
  * [MDEV-20265](https://jira.mariadb.org/browse/MDEV-20265) Unknown column in field list
* [Revision #9dae991a95](https://github.com/MariaDB/server/commit/9dae991a95)\
  2019-08-30 17:06:53 +0200
  * [MDEV-19200](https://jira.mariadb.org/browse/MDEV-19200) Do not print "Thread did not exit" message for system/background THDs
* [Revision #9487e0b259](https://github.com/MariaDB/server/commit/9487e0b259)\
  2019-08-30 08:42:24 +0300
  * [MDEV-19826](https://jira.mariadb.org/browse/MDEV-19826) 10.4 seems to crash with "pool-of-threads" (#1370)
* [Revision #d22f8c459f](https://github.com/MariaDB/server/commit/d22f8c459f)\
  2019-08-29 18:33:58 +0200
  * [MDEV-20432](https://jira.mariadb.org/browse/MDEV-20432) : add MYSQL\_PLUGIN\_IMPORT
* [Revision #5bb8945a3a](https://github.com/MariaDB/server/commit/5bb8945a3a)\
  2019-08-27 20:46:05 +0200
  * Fix compress\_qpress result file, broken in b5615eff0d00cfb4c60b9d1bf67094da7c2258a6
* [Revision #77e44282ff](https://github.com/MariaDB/server/commit/77e44282ff)\
  2019-08-26 20:59:51 +0530
  * [MDEV-19705](https://jira.mariadb.org/browse/MDEV-19705): Assertion \`tmp >= 0' failed in best\_access\_path
* [Revision #6afe013cde](https://github.com/MariaDB/server/commit/6afe013cde)\
  2019-08-02 17:57:49 +0200
  * always build wsrep libraries static
* [Revision #58bfe9da54](https://github.com/MariaDB/server/commit/58bfe9da54)\
  2019-08-26 16:28:29 +0200
  * cleanup: SECURITY\_HARDENED in CMakeLists.txt
* [Revision #eb8f7005bd](https://github.com/MariaDB/server/commit/eb8f7005bd)\
  2019-07-28 00:04:57 +0200
  * cleanup: remove few #ifdef's
* [Revision #4af932e899](https://github.com/MariaDB/server/commit/4af932e899)\
  2019-08-05 14:47:02 +0200
  * remove incorrect #ifdef
* [Revision #72c5a8d39b](https://github.com/MariaDB/server/commit/72c5a8d39b)\
  2019-08-26 23:42:06 +0400
  * [MDEV-20417](https://jira.mariadb.org/browse/MDEV-20417) Assertion \`\`(m\_ptr == null) == item->null\_value' failed in VDec::VDec(Item\*)\`
* [Revision #4a490d1a99](https://github.com/MariaDB/server/commit/4a490d1a99)\
  2019-08-25 11:03:19 +0300
  * [MDEV-6111](https://jira.mariadb.org/browse/MDEV-6111): Optimizer Trace: add tracing for semi-join optimizations
* [Revision #9fce942878](https://github.com/MariaDB/server/commit/9fce942878)\
  2019-08-24 20:47:24 +0300
  * [MDEV-19831](https://jira.mariadb.org/browse/MDEV-19831) find\_select\_handler() now tries its best to find a handlerton that is able to processes the whole query. For that it traverses tables from subqueries.
* Merge [Revision #efb8485d85](https://github.com/MariaDB/server/commit/efb8485d85) 2019-08-23 08:06:17 +0300 - Merge 10.3 into 10.4, except for [MDEV-20265](https://jira.mariadb.org/browse/MDEV-20265)
* [Revision #235cf969d2](https://github.com/MariaDB/server/commit/235cf969d2)\
  2019-08-22 14:17:04 +0400
  * [MDEV-20397](https://jira.mariadb.org/browse/MDEV-20397) Support TIMESTAMP, DATETIME, TIME in ROUND() and TRUNCATE()
* [Revision #7b4de10477](https://github.com/MariaDB/server/commit/7b4de10477)\
  2019-08-20 10:32:04 +0300
  * [MDEV-20378](https://jira.mariadb.org/browse/MDEV-20378): Galera uses uninitialized memory
* [Revision #c5bc0cedea](https://github.com/MariaDB/server/commit/c5bc0cedea)\
  2019-07-30 17:18:31 +0200
  * [MDEV-20185](https://jira.mariadb.org/browse/MDEV-20185): Windows: Use of uninitialized value $bpath in string eq
* [Revision #89fb295b1b](https://github.com/MariaDB/server/commit/89fb295b1b)\
  2019-07-30 13:45:13 +0200
  * [MDEV-18863](https://jira.mariadb.org/browse/MDEV-18863): Galera SST scripts can't read \[mysqldN] option groups
* [Revision #fcae2a6364](https://github.com/MariaDB/server/commit/fcae2a6364)\
  2019-08-19 16:29:36 +0300
  * [MDEV-20383](https://jira.mariadb.org/browse/MDEV-20383) Use of uninitialized value in Datafile::find\_space\_id() for ROW\_FORMAT=COMPRESSED
* [Revision #52e276247d](https://github.com/MariaDB/server/commit/52e276247d)\
  2019-08-19 15:11:14 +0400
  * [MDEV-19961](https://jira.mariadb.org/browse/MDEV-19961) MIN(timestamp\_column) returns a wrong result in a GROUP BY query
* [Revision #850bf33137](https://github.com/MariaDB/server/commit/850bf33137)\
  2019-08-19 11:54:26 +0300
  * [MDEV-20374](https://jira.mariadb.org/browse/MDEV-20374): innodb.innodb\_mysql fails sporadically in BB
* [Revision #4d5382504d](https://github.com/MariaDB/server/commit/4d5382504d)\
  2019-08-16 16:49:12 +0530
  * [MDEV-20349](https://jira.mariadb.org/browse/MDEV-20349): Assertion \`to\_len >= 8' failed in convert\_to\_printable
* Merge [Revision #c221bcdce7](https://github.com/MariaDB/server/commit/c221bcdce7) 2019-08-16 10:51:20 +0300 - Merge 10.3 into 10.4
* [Revision #3bbf008096](https://github.com/MariaDB/server/commit/3bbf008096)\
  2019-08-16 08:33:01 +0300
  * Remove file accidentally pushed.
* [Revision #e6b505fd3c](https://github.com/MariaDB/server/commit/e6b505fd3c)\
  2019-08-16 07:07:31 +0300
  * [MDEV-18778](https://jira.mariadb.org/browse/MDEV-18778): mysql\_tzinfo\_to\_sql does not work correctly in MariaDB Galera
* [Revision #136cf0400f](https://github.com/MariaDB/server/commit/136cf0400f)\
  2019-08-15 13:48:55 +0300
  * Fix result error.
* [Revision #5a2012d2b3](https://github.com/MariaDB/server/commit/5a2012d2b3)\
  2019-08-15 12:36:28 +0300
  * Fix test failure on galera-features#56
* [Revision #870acdf534](https://github.com/MariaDB/server/commit/870acdf534)\
  2019-08-15 09:00:01 +0300
  * After-merge fix: Re-record results
* Merge [Revision #1d15a28e52](https://github.com/MariaDB/server/commit/1d15a28e52) 2019-08-14 18:06:51 +0300 - Merge 10.3 into 10.4
* [Revision #c4feef50cf](https://github.com/MariaDB/server/commit/c4feef50cf)\
  2019-08-14 11:58:22 +0300
  * [MDEV-20138](https://jira.mariadb.org/browse/MDEV-20138) innodb.trx\_id\_future fails on 10.4+
* [Revision #7772c7cd94](https://github.com/MariaDB/server/commit/7772c7cd94)\
  2019-08-14 12:01:40 +0530
  * [MDEV-20340](https://jira.mariadb.org/browse/MDEV-20340) Encrypted temporary tables cannot be read with full\_crc32
* [Revision #dc8a20f3d0](https://github.com/MariaDB/server/commit/dc8a20f3d0)\
  2019-08-14 09:29:25 +0300
  * [MDEV-19781](https://jira.mariadb.org/browse/MDEV-19781): Adapt the test for full\_crc32
* [Revision #d7be886cb8](https://github.com/MariaDB/server/commit/d7be886cb8)\
  2019-08-14 10:11:30 +0300
  * Fix main.opt\_trace
* [Revision #c4fd167d5a](https://github.com/MariaDB/server/commit/c4fd167d5a)\
  2019-08-13 17:17:56 +0300
  * Fixed access to unitialized memory when using unique HASH key
* [Revision #2dbe472ed0](https://github.com/MariaDB/server/commit/2dbe472ed0)\
  2019-08-10 00:53:28 +0300
  * Optimizer trace: print cost and #rows of the join prefix
* Merge [Revision #95cdc1ca5f](https://github.com/MariaDB/server/commit/95cdc1ca5f) 2019-08-13 11:42:31 +0400 - Merge commit '43882e764d6867c6855b1ff057758a3f08b25c55' into 10.4
* [Revision #ae1d17f52d](https://github.com/MariaDB/server/commit/ae1d17f52d)\
  2019-08-12 18:29:16 +0300
  * [MDEV-20316](https://jira.mariadb.org/browse/MDEV-20316) InnoDB writes uninitialised tail of XID buffer
* [Revision #97bbac8ec6](https://github.com/MariaDB/server/commit/97bbac8ec6)\
  2019-08-12 19:35:59 +0300
  * Revert part of 05619f6989590727a470c23475fc987f52b56988
* [Revision #05619f6989](https://github.com/MariaDB/server/commit/05619f6989)\
  2019-08-12 10:42:12 +0300
  * Fixes based on warnings from gcc/clang and valgrind
* [Revision #13f36fffea](https://github.com/MariaDB/server/commit/13f36fffea)\
  2019-08-06 10:53:55 +0400
  * [MDEV-19301](https://jira.mariadb.org/browse/MDEV-19301) Assertion \`!is\_valid\_datetime() || fraction\_remainder(((item->decimals) < (6) ? (item->decimals) : (6))) == 0' failed in Datetime\_truncation\_not\_needed::Datetime\_truncation\_not\_needed
* [Revision #c99f9766b1](https://github.com/MariaDB/server/commit/c99f9766b1)\
  2019-08-05 14:41:17 +0400
  * [MDEV-19166](https://jira.mariadb.org/browse/MDEV-19166) Assertion \`!is\_zero\_datetime()' failed in Timestamp\_or\_zero\_datetime::tv
* [Revision #e244652831](https://github.com/MariaDB/server/commit/e244652831)\
  2019-08-03 01:02:32 +0400
  * [MDEV-20246](https://jira.mariadb.org/browse/MDEV-20246) Error compiling PAM plugin.
* [Revision #60a37783ae](https://github.com/MariaDB/server/commit/60a37783ae)\
  2019-08-01 12:26:36 +0530
  * [MDEV-20224](https://jira.mariadb.org/browse/MDEV-20224): main.derived crashes with ASAN with error use-after-poison
* [Revision #b428b09997](https://github.com/MariaDB/server/commit/b428b09997)\
  2019-08-01 08:59:53 +0900
  * [MDEV-20179](https://jira.mariadb.org/browse/MDEV-20179) Server hangs on shutdown during installation of Spider (#1369)
* [Revision #798080f4b3](https://github.com/MariaDB/server/commit/798080f4b3)\
  2019-07-31 10:00:26 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
