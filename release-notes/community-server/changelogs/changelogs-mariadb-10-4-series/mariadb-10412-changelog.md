# MariaDB 10.4.12 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.12/)[Release Notes](../../old-releases/10.4/10.4.12.md)[Changelog](mariadb-10412-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 28 Jan 2020

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.12.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.22](../changelogs-mariadb-10-3-series/mariadb-10322-changelog.md)
* [Revision #ba6bfc402c](https://github.com/MariaDB/server/commit/ba6bfc402c)\
  2020-01-26 22:39:52 +0200
  * List of unstable tests for 10.4.12 release
* [Revision #ee33c4a694](https://github.com/MariaDB/server/commit/ee33c4a694)\
  2020-01-26 12:47:20 +0300
  * Post-merge fix
* Merge [Revision #70815ed5b9](https://github.com/MariaDB/server/commit/70815ed5b9) 2020-01-25 16:10:48 +0100 - Merge branch '10.3' into 10.4
* [Revision #fdb9b05cbb](https://github.com/MariaDB/server/commit/fdb9b05cbb)\
  2020-01-24 15:38:25 +0100
  * fix tests
* Merge [Revision #bfc24bb2ec](https://github.com/MariaDB/server/commit/bfc24bb2ec) 2020-01-24 14:50:23 +0100 - Merge branch '10.3' into 10.4
* [Revision #2833e90619](https://github.com/MariaDB/server/commit/2833e90619)\
  2020-01-24 14:34:07 +0100
  * fix perfschema.start\_server\_innodb test (related to [MDEV-17571](https://jira.mariadb.org/browse/MDEV-17571))
* [Revision #8a931e4d16](https://github.com/MariaDB/server/commit/8a931e4d16)\
  2020-01-22 11:58:50 +0200
  * [MDEV-17571](https://jira.mariadb.org/browse/MDEV-17571) : Make systemd timeout behavior more compatible with long Galera SSTs
* Merge [Revision #6918157e98](https://github.com/MariaDB/server/commit/6918157e98) 2020-01-21 23:15:02 +0100 - Merge branch '10.3' into 10.4
* [Revision #1084fa77ab](https://github.com/MariaDB/server/commit/1084fa77ab)\
  2020-01-21 18:47:56 +0200
  * [MDEV-21539](https://jira.mariadb.org/browse/MDEV-21539) Assertion ...prtype... failed in row\_log\_table\_apply\_convert\_mrec
* [Revision #5cd21ac202](https://github.com/MariaDB/server/commit/5cd21ac202)\
  2020-01-17 20:26:14 +0200
  * [MDEV-20821](https://jira.mariadb.org/browse/MDEV-20821) parallel slave server shutdown hang
* [Revision #7c0e4748ac](https://github.com/MariaDB/server/commit/7c0e4748ac)\
  2020-01-21 09:20:59 +0100
  * silence a warning in WolfSSL.
* [Revision #1ecd0e0732](https://github.com/MariaDB/server/commit/1ecd0e0732)\
  2020-01-20 22:35:54 +0100
  * compilation fixes for new wolfssl
* [Revision #3155a643df](https://github.com/MariaDB/server/commit/3155a643df)\
  2020-01-20 16:31:50 +0100
  * new wolfssl v4.3.0-stable
* [Revision #259185764b](https://github.com/MariaDB/server/commit/259185764b)\
  2020-01-20 16:08:18 +0200
  * [MDEV-17062](https://jira.mariadb.org/browse/MDEV-17062): Fix a typo in an error message
* [Revision #57ec527841](https://github.com/MariaDB/server/commit/57ec527841)\
  2020-01-16 13:18:44 +0200
  * [MDEV-17062](https://jira.mariadb.org/browse/MDEV-17062) : Test failure on galera.MW-336
* Merge [Revision #87a61355e8](https://github.com/MariaDB/server/commit/87a61355e8) 2020-01-20 15:49:48 +0200 - Merge 10.3 into 10.4
* [Revision #7ea413ac2d](https://github.com/MariaDB/server/commit/7ea413ac2d)\
  2020-01-19 20:03:25 -0800
  * [MDEV-21446](https://jira.mariadb.org/browse/MDEV-21446) Assertion \`!prebuilt->index->is\_primary()' failed in row\_search\_idx\_cond\_check with rowid\_filter upon concurrent access to table
* [Revision #74a0cde1c6](https://github.com/MariaDB/server/commit/74a0cde1c6)\
  2020-01-18 02:02:29 +0100
  * mysql\_install\_db always has to pass --user=$user to the mysqld
* [Revision #4de32015be](https://github.com/MariaDB/server/commit/4de32015be)\
  2020-01-18 13:26:03 -0800
  * [MDEV-21356](https://jira.mariadb.org/browse/MDEV-21356) ERROR 1032 Can't find record when running simple, single-table query
* [Revision #057fbfa356](https://github.com/MariaDB/server/commit/057fbfa356)\
  2020-01-18 09:38:01 +0200
  * Disable Galera tests failing on bb and Azure until they are fixed.
* [Revision #51a9571256](https://github.com/MariaDB/server/commit/51a9571256)\
  2020-01-15 22:40:56 +0100
  * [MDEV-20205](https://jira.mariadb.org/browse/MDEV-20205) mysql\_install\_db shouldn't execute chown
* [Revision #9d18b62467](https://github.com/MariaDB/server/commit/9d18b62467)\
  2020-01-15 18:08:02 +0100
  * rpm/deb and auth\_pam\_tool\_dir/auth\_pam\_tool
* [Revision #7e378a8d31](https://github.com/MariaDB/server/commit/7e378a8d31)\
  2020-01-17 11:58:03 +0200
  * Test requires debug build from galera library.
* [Revision #f0ca9bc669](https://github.com/MariaDB/server/commit/f0ca9bc669)\
  2019-12-30 15:11:01 -0500
  * [MDEV-20732](https://jira.mariadb.org/browse/MDEV-20732) Correctly set the length of the FORMAT() result for float data type as argument.
* [Revision #1c97cd339e](https://github.com/MariaDB/server/commit/1c97cd339e)\
  2020-01-03 11:15:00 -0800
  * [MDEV-21184](https://jira.mariadb.org/browse/MDEV-21184) Assertion \`used\_tables\_cache == 0' failed in Item\_func::fix\_fields with condition\_pushdown\_from\_having
* [Revision #6a8a4c19e2](https://github.com/MariaDB/server/commit/6a8a4c19e2)\
  2020-01-15 18:28:52 +0200
  * [MDEV-21485](https://jira.mariadb.org/browse/MDEV-21485) ASAN use-after-poison in dfield\_get\_len or Assertion \`pos < index->n\_def' failed
* [Revision #2d4b6571ec](https://github.com/MariaDB/server/commit/2d4b6571ec)\
  2020-01-14 06:33:02 +0100
  * Wsrep position not updated in InnoDB after certification failures (#1432)
* [Revision #983163209d](https://github.com/MariaDB/server/commit/983163209d)\
  2020-01-08 16:23:49 +0100
  * [MDEV-21444](https://jira.mariadb.org/browse/MDEV-21444) : Fix socket leak if AcceptEx() return WSAECONNRESET.
* Merge [Revision #4032fc1d68](https://github.com/MariaDB/server/commit/4032fc1d68) 2020-01-08 13:53:03 +0530 - Merge branch '10.3' into 10.4
* [Revision #d2697dfbc6](https://github.com/MariaDB/server/commit/d2697dfbc6)\
  2020-01-07 13:35:32 +0200
  * [MDEV-20839](https://jira.mariadb.org/browse/MDEV-20839) encryption.innodb-redo-badkey sporadically fails on buildbot with page dump
* [Revision #d3e52ff24d](https://github.com/MariaDB/server/commit/d3e52ff24d)\
  2020-01-07 13:25:36 +0200
  * [MDEV-21288](https://jira.mariadb.org/browse/MDEV-21288) innodb.full\_crc32\_import fails due to the use of optional compression algorithm
* Merge [Revision #d60dcabd0f](https://github.com/MariaDB/server/commit/d60dcabd0f) 2020-01-07 13:23:41 +0200 - Merge 10.3 into 10.4
* [Revision #8a6863002c](https://github.com/MariaDB/server/commit/8a6863002c)\
  2020-01-06 11:33:57 +0200
  * Fixed that mtr --extern works again
* Merge [Revision #9d036f840a](https://github.com/MariaDB/server/commit/9d036f840a) 2020-01-03 15:05:50 +0100 - Merge branch '10.3' into 10.4
* [Revision #2cff807d3f](https://github.com/MariaDB/server/commit/2cff807d3f)\
  2019-12-31 11:55:44 +0200
  * Add have\_debug to [MDEV-20793](https://jira.mariadb.org/browse/MDEV-20793) and add wait condition to galera\_parallel\_autoinc\_largetrx to stabilize it.
* [Revision #13b3d7f1f1](https://github.com/MariaDB/server/commit/13b3d7f1f1)\
  2019-12-27 17:43:28 +0200
  * [MDEV-20793](https://jira.mariadb.org/browse/MDEV-20793) Assertion failed after replay.
* [Revision #59d4f2a373](https://github.com/MariaDB/server/commit/59d4f2a373)\
  2019-12-30 18:59:02 +0200
  * Cleanup after [MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026)
* Merge [Revision #ffc0a08d05](https://github.com/MariaDB/server/commit/ffc0a08d05) 2019-12-30 10:27:59 +0200 - Merge 10.3 into 10.4
* [Revision #071feae319](https://github.com/MariaDB/server/commit/071feae319)\
  2019-12-27 15:52:12 +0100
  * [MDEV-20170](https://jira.mariadb.org/browse/MDEV-20170) main.tls\_version and main.tls\_version1 fail in buildbot on RHEL8
* [Revision #b86e0f25f8](https://github.com/MariaDB/server/commit/b86e0f25f8)\
  2019-12-27 20:44:34 +0200
  * Cleanup: Use more page\_id\_t in crash recovery
* Merge [Revision #4c25e75ce7](https://github.com/MariaDB/server/commit/4c25e75ce7) 2019-12-27 18:20:28 +0200 - Merge 10.3 into 10.4
* Merge [Revision #4c57ab34d4](https://github.com/MariaDB/server/commit/4c57ab34d4) 2019-12-25 13:33:28 +0400 - Merge remote-tracking branch 'origin/10.3' into 10.4
* [Revision #3fbd9f1522](https://github.com/MariaDB/server/commit/3fbd9f1522)\
  2019-12-23 16:06:25 +0200
  * [MDEV-20909](https://jira.mariadb.org/browse/MDEV-20909) : Galera test failure on galera.galera\_gcs\_fc\_limit: Server crash with signal 6
* [Revision #cc9c55b2e2](https://github.com/MariaDB/server/commit/cc9c55b2e2)\
  2019-12-23 12:43:15 +0200
  * [MDEV-21189](https://jira.mariadb.org/browse/MDEV-21189) : Dropping partition with 'wsrep\_OSU\_method=RSU' and 'SESSION sql\_log\_bin = 0' cases the galera node to hang
* [Revision #5e0c80c2a5](https://github.com/MariaDB/server/commit/5e0c80c2a5)\
  2019-12-20 15:55:55 +0400
  * An extra test with NULLIF() for [MDEV-13995](https://jira.mariadb.org/browse/MDEV-13995) MAX(timestamp) returns a wrong result near DST change
* [Revision #088de81d96](https://github.com/MariaDB/server/commit/088de81d96)\
  2019-12-18 08:22:07 +0200
  * [MDEV-21335](https://jira.mariadb.org/browse/MDEV-21335) : Galera test failure on suite wsrep
* [Revision #67e063eb94](https://github.com/MariaDB/server/commit/67e063eb94)\
  2019-12-16 05:50:15 +0000
  * Update wsrep-lib. (#1426)
* Merge [Revision #8fa759a576](https://github.com/MariaDB/server/commit/8fa759a576) 2019-12-13 17:30:37 +0200 - Merge 10.3 into 10.4
* [Revision #014e125830](https://github.com/MariaDB/server/commit/014e125830)\
  2019-12-12 00:38:28 +0700
  * optimize crash recovery
* [Revision #3304004a57](https://github.com/MariaDB/server/commit/3304004a57)\
  2019-12-12 11:49:57 +0100
  * [MDEV-21260](https://jira.mariadb.org/browse/MDEV-21260) Innodb/Wjndows do not report error when trying open volumes on UNC paths
* [Revision #71e47f34f8](https://github.com/MariaDB/server/commit/71e47f34f8)\
  2019-11-27 18:07:12 +0100
  * git ignore generated stuff
* [Revision #3b401a69f7](https://github.com/MariaDB/server/commit/3b401a69f7)\
  2019-12-11 13:05:46 -0500
  * bump the VERSION
* [Revision #72a5a4f1d5](https://github.com/MariaDB/server/commit/72a5a4f1d5)\
  2019-12-11 13:08:06 +0100
  * [MDEV-20780](https://jira.mariadb.org/browse/MDEV-20780) Fixes for failures on galera\_sr\_ddl\_master (#1425)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
