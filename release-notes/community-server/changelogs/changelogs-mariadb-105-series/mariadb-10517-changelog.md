# MariaDB 10.5.17 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.17](https://downloads.mariadb.org/mariadb/10.5.17/)[Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10-5-17-release-notes)[Changelog](mariadb-10517-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 15 Aug 2022

For the highlights of this release, see the [release notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.26](../changelogs-mariadb-10-4-series/mariadb-10426-changelog.md)
* Merge [Revision #1ac0bce36e](https://github.com/MariaDB/server/commit/1ac0bce36e) 2022-08-10 12:24:31 +0200 - Merge branch '10.4' into 10.5
* [Revision #3b071bad19](https://github.com/MariaDB/server/commit/3b071bad19)\
  2022-08-04 12:51:32 +0300
  * [MDEV-29242](https://jira.mariadb.org/browse/MDEV-29242): Assertion \`computed\_weight == weight' failed SEL\_ARG::verify\_weight
* Merge [Revision #ea12dafe65](https://github.com/MariaDB/server/commit/ea12dafe65) 2022-08-04 12:16:35 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #1e71ea806b](https://github.com/MariaDB/server/commit/1e71ea806b) 2022-08-04 08:30:03 +0200 - Merge branch '10.4' into 10.5
* [Revision #cd51854d7a](https://github.com/MariaDB/server/commit/cd51854d7a)\
  2022-08-03 13:31:48 +0200
  * RHEL9 disables SHA1 signatures in openssl
* [Revision #d7649968d9](https://github.com/MariaDB/server/commit/d7649968d9)\
  2022-08-03 00:11:34 +0200
  * [MDEV-29220](https://jira.mariadb.org/browse/MDEV-29220) Missing RHEL-9-specific logic in cpack\_rpm.cmake
* Merge [Revision #af143474d8](https://github.com/MariaDB/server/commit/af143474d8) 2022-08-03 07:12:27 +0200 - Merge branch '10.4' into 10.5
* [Revision #7b500f04fb](https://github.com/MariaDB/server/commit/7b500f04fb)\
  2022-07-23 16:38:03 +0200
  * [MDEV-29078](https://jira.mariadb.org/browse/MDEV-29078) For old binary logs explicit\_defaults\_for\_timestamp presumed to be OFF, server value ignored
* [Revision #56c7d14217](https://github.com/MariaDB/server/commit/56c7d14217)\
  2022-07-29 15:39:57 +0200
  * [MDEV-29075](https://jira.mariadb.org/browse/MDEV-29075) Changing explicit\_defaults\_for\_timestamp within stored procedure works inconsistently
* [Revision #b174ec169d](https://github.com/MariaDB/server/commit/b174ec169d)\
  2022-07-04 16:47:14 +0200
  * [MDEV-29225](https://jira.mariadb.org/browse/MDEV-29225) make explicit\_defaults\_for\_timestamps SESSION variable
* [Revision #4e3728f038](https://github.com/MariaDB/server/commit/4e3728f038)\
  2022-07-02 12:22:10 +0200
  * [MDEV-29225](https://jira.mariadb.org/browse/MDEV-29225) make explicit\_defaults\_for\_timestamps SESSION variable
* [Revision #086eb8e23c](https://github.com/MariaDB/server/commit/086eb8e23c)\
  2022-07-02 12:20:49 +0200
  * my\_getopt --help for "bit" options
* [Revision #28d44abd99](https://github.com/MariaDB/server/commit/28d44abd99)\
  2022-01-20 15:48:08 +0100
  * [MDEV-27540](https://jira.mariadb.org/browse/MDEV-27540) Different OpenSSL versions mix up in build depending on cmake options
* Merge [Revision #b043e1098e](https://github.com/MariaDB/server/commit/b043e1098e) 2022-08-02 09:34:15 +0200 - Merge branch 'merge-perfschema-5.7' into 10.5
* [Revision #61d08f7427](https://github.com/MariaDB/server/commit/61d08f7427)\
  2022-07-29 14:48:01 +0200
  * mysql-5.7.39
* [Revision #4d0c53a327](https://github.com/MariaDB/server/commit/4d0c53a327)\
  2022-08-01 23:59:57 +0200
  * [MDEV-28701](https://jira.mariadb.org/browse/MDEV-28701) Update Server HELP
* [Revision #90ba999e80](https://github.com/MariaDB/server/commit/90ba999e80)\
  2022-07-27 17:37:03 +0300
  * [MDEV-25020](https://jira.mariadb.org/browse/MDEV-25020): Range optimizer regression for key IN (const, ....)
* Merge [Revision #098c0f2634](https://github.com/MariaDB/server/commit/098c0f2634) 2022-07-27 17:17:24 +0300 - Merge 10.4 into 10.5
* [Revision #5bf4dee369](https://github.com/MariaDB/server/commit/5bf4dee369)\
  2022-07-24 20:43:45 +0300
  * [MDEV-28948](https://jira.mariadb.org/browse/MDEV-28948) FLUSH BINARY LOGS waits/hangs on mysql\_mutex\_unlock(\&LOCK\_index)
* [Revision #8494758e8e](https://github.com/MariaDB/server/commit/8494758e8e)\
  2022-07-08 11:38:45 +0200
  * [MDEV-26433](https://jira.mariadb.org/browse/MDEV-26433) assertion: table->get\_ref\_count() == 0 in dict0dict.cc line 1915
* [Revision #fc456bc97e](https://github.com/MariaDB/server/commit/fc456bc97e)\
  2022-07-09 12:28:48 +1000
  * [MDEV-27593](https://jira.mariadb.org/browse/MDEV-27593) InnoDB handle AIO errors - more detailed assertion
* [Revision #781948a19b](https://github.com/MariaDB/server/commit/781948a19b)\
  2022-07-08 18:37:12 +0200
  * [MDEV-22954](https://jira.mariadb.org/browse/MDEV-22954) fix sporadic failure of main.mdl
* [Revision #0fca5068a8](https://github.com/MariaDB/server/commit/0fca5068a8)\
  2022-07-04 20:20:20 +0200
  * [MDEV-28234](https://jira.mariadb.org/browse/MDEV-28234) Change maturity of plugins for July 2022 Releases
* [Revision #9d5718c9b9](https://github.com/MariaDB/server/commit/9d5718c9b9)\
  2022-05-23 14:38:56 +0200
  * [MDEV-28648](https://jira.mariadb.org/browse/MDEV-28648) main.ssl\_timeout fails with OpenSSL 3.0.3
* [Revision #ef65566981](https://github.com/MariaDB/server/commit/ef65566981)\
  2022-02-08 16:39:10 +0100
  * [MDEV-27778](https://jira.mariadb.org/browse/MDEV-27778) md5 in FIPS crashes with OpenSSL 3.0.0
* [Revision #1dc09ce0fd](https://github.com/MariaDB/server/commit/1dc09ce0fd)\
  2022-02-04 14:52:03 +0100
  * Revert "don't build with OpenSSL 3.0, it doesn't work before [MDEV-25785](https://jira.mariadb.org/browse/MDEV-25785)"
* [Revision #8a9c1e9ccf](https://github.com/MariaDB/server/commit/8a9c1e9ccf)\
  2021-11-08 18:48:19 +0100
  * [MDEV-25785](https://jira.mariadb.org/browse/MDEV-25785) Add support for OpenSSL 3.0
* Merge [Revision #33f0270ebb](https://github.com/MariaDB/server/commit/33f0270ebb) 2022-07-04 10:19:28 +0300 - Merge 10.4 into 10.5
* [Revision #b546913ba2](https://github.com/MariaDB/server/commit/b546913ba2)\
  2022-07-01 14:42:13 +0300
  * Valgrind: Disable tests that would often time out
* Merge [Revision #f09687094c](https://github.com/MariaDB/server/commit/f09687094c) 2022-07-01 14:42:02 +0300 - Merge 10.4 into 10.5
* [Revision #a1267724cb](https://github.com/MariaDB/server/commit/a1267724cb)\
  2022-06-30 14:28:16 +0300
  * [MDEV-26293](https://jira.mariadb.org/browse/MDEV-26293) InnoDB: Failing assertion: space->is\_ready\_to\_close() ...
* [Revision #afe607dffa](https://github.com/MariaDB/server/commit/afe607dffa)\
  2022-06-30 13:00:58 +0300
  * MSAN: Disable some slow tests
* [Revision #a26700cca5](https://github.com/MariaDB/server/commit/a26700cca5)\
  2022-06-16 20:25:02 +0900
  * [MDEV-28352](https://jira.mariadb.org/browse/MDEV-28352) Spider: heap-use-after-free in ha\_spider::lock\_tables(), heap freed by spider\_commit()
* Merge [Revision #773f1dad94](https://github.com/MariaDB/server/commit/773f1dad94) 2022-06-27 16:17:02 +0300 - Merge 10.4 into 10.5
* Merge [Revision #ea847cbeaf](https://github.com/MariaDB/server/commit/ea847cbeaf) 2022-06-27 10:51:20 +0300 - Merge 10.4 into 10.5
* [Revision #03174cabd7](https://github.com/MariaDB/server/commit/03174cabd7)\
  2022-06-27 10:49:15 +0300
  * Fix GCC -Og -Wmaybe-uninitialized
* [Revision #35f2cdcb99](https://github.com/MariaDB/server/commit/35f2cdcb99)\
  2022-06-23 05:53:55 +0200
  * [MDEV-28920](https://jira.mariadb.org/browse/MDEV-28920) Rescheduling of innodb\_stats\_func() missing
* [Revision #674842bee0](https://github.com/MariaDB/server/commit/674842bee0)\
  2022-06-15 23:49:09 +0300
  * [MDEV-28858](https://jira.mariadb.org/browse/MDEV-28858) Wrong result with table elimination combined with not\_null\_range\_scan
* [Revision #27309fc6b0](https://github.com/MariaDB/server/commit/27309fc6b0)\
  2022-06-14 11:31:11 +0300
  * [MDEV-28832](https://jira.mariadb.org/browse/MDEV-28832) infinite loop in mariadb-backup if log LOG\_HEADER\_FORMAT field is 0
* [Revision #4849d94fe6](https://github.com/MariaDB/server/commit/4849d94fe6)\
  2022-06-14 09:14:24 +0300
  * [MDEV-28828](https://jira.mariadb.org/browse/MDEV-28828) SIGSEGV in buf\_flush\_LRU\_list\_batch
* [Revision #06e9ce798c](https://github.com/MariaDB/server/commit/06e9ce798c)\
  2021-10-29 19:04:53 +0900
  * [MDEV-26127](https://jira.mariadb.org/browse/MDEV-26127) Assertion \`err != DB\_DUPLICATE\_KEY' failed or InnoDB: Failing assertion: id != 0 on ALTER ... REBUILD PARTITION
* [Revision #d4760d8c01](https://github.com/MariaDB/server/commit/d4760d8c01)\
  2022-05-23 10:00:13 +0300
  * [MDEV-28642](https://jira.mariadb.org/browse/MDEV-28642): Suspend obvious false-positive Lintian warnings
* Merge [Revision #a9d0bb12e6](https://github.com/MariaDB/server/commit/a9d0bb12e6) 2022-06-09 12:22:55 +0300 - Merge 10.4 into 10.5
* [Revision #4145618103](https://github.com/MariaDB/server/commit/4145618103)\
  2022-05-27 15:04:31 +0000
  * [MDEV-22023](https://jira.mariadb.org/browse/MDEV-22023) Update man page NAME section to say MariaDB instead of MySQL
* [Revision #e8b0894dc8](https://github.com/MariaDB/server/commit/e8b0894dc8)\
  2022-04-05 15:47:09 +1000
  * [MDEV-28243](https://jira.mariadb.org/browse/MDEV-28243): AIX missing my\_gethwaddr implementation
* [Revision #4834a0d1fa](https://github.com/MariaDB/server/commit/4834a0d1fa)\
  2022-06-06 14:58:34 +0300
  * Fixed bug in Aria read cache when doing check/repair
* [Revision #54e501cf04](https://github.com/MariaDB/server/commit/54e501cf04)\
  2022-06-06 14:53:09 +0300
  * [MDEV-28757](https://jira.mariadb.org/browse/MDEV-28757) S3 tables can hang in SELECT
* [Revision #6d99fdce18](https://github.com/MariaDB/server/commit/6d99fdce18)\
  2022-06-03 19:58:17 +0400
  * [MDEV-28491](https://jira.mariadb.org/browse/MDEV-28491) Uuid. "UPDATE/DELETE" not working "WHERE id IN (SELECT id FROM ..)"
* [Revision #22f935d6da](https://github.com/MariaDB/server/commit/22f935d6da)\
  2022-06-02 17:33:03 +0300
  * [MDEV-28731](https://jira.mariadb.org/browse/MDEV-28731) Race condition on log checkpoint
* [Revision #5909e0ec31](https://github.com/MariaDB/server/commit/5909e0ec31)\
  2022-06-02 17:22:16 +0300
  * Cleanup: btr\_store\_big\_rec\_extern\_fields() does not really modify pcur
* [Revision #5294695ebd](https://github.com/MariaDB/server/commit/5294695ebd)\
  2022-06-02 17:18:00 +0300
  * Clean up mtr\_t
* Merge [Revision #4b3c3e526e](https://github.com/MariaDB/server/commit/4b3c3e526e) 2022-06-02 16:51:13 +0300 - Merge 10.4 into 10.5
* [Revision #e7de50a821](https://github.com/MariaDB/server/commit/e7de50a821)\
  2022-05-30 17:32:41 +0300
  * Bug fixes for S3
* [Revision #2840d7750d](https://github.com/MariaDB/server/commit/2840d7750d)\
  2022-05-24 17:51:20 +0200
  * fix not\_valgrind.inc not to error out in embedded
* [Revision #8b19f521f1](https://github.com/MariaDB/server/commit/8b19f521f1)\
  2022-05-24 17:27:18 +0200
  * move alter\_table combinations to a separate test file
* [Revision #96329d6321](https://github.com/MariaDB/server/commit/96329d6321)\
  2022-05-29 12:10:37 +0300
  * Fixed that CHECK TABLE on an S3 table doesn't try to write to files
* Merge [Revision #ea40c75c27](https://github.com/MariaDB/server/commit/ea40c75c27) 2022-05-25 14:24:51 +0300 - Merge 10.4 into 10.5
* [Revision #a0e4853eff](https://github.com/MariaDB/server/commit/a0e4853eff)\
  2022-05-25 13:15:56 +0300
  * [MDEV-28668](https://jira.mariadb.org/browse/MDEV-28668) Recovery or backup of INSERT may be incorrect
* [Revision #915afddba2](https://github.com/MariaDB/server/commit/915afddba2)\
  2022-05-24 15:11:34 +0300
  * main.alter\_table\_lock could fail with query "'LOCK TABLE t1 WRITE' failed"
* [Revision #ddb1f7c4e4](https://github.com/MariaDB/server/commit/ddb1f7c4e4)\
  2022-05-24 15:08:03 +0300
  * Remove warning when using connect have\_libxml2.inc
* [Revision #847ca89d6d](https://github.com/MariaDB/server/commit/847ca89d6d)\
  2022-05-19 02:32:18 +0300
  * Added check for libxml2 for connect.misc
* [Revision #734f10f601](https://github.com/MariaDB/server/commit/734f10f601)\
  2022-05-22 19:03:54 +0300
  * Fix that spider test doesn't crash if my\_gethwaddr() fails
* [Revision #cc4384badf](https://github.com/MariaDB/server/commit/cc4384badf)\
  2022-05-24 07:37:08 +0300
  * Update galera\_sr disabled.def file
* [Revision #d3d50570de](https://github.com/MariaDB/server/commit/d3d50570de)\
  2022-05-11 11:45:57 +0300
  * [MDEV-28376](https://jira.mariadb.org/browse/MDEV-28376): Make sure available Perl MariaDB DBI driver is chosen
* [Revision #af869493b4](https://github.com/MariaDB/server/commit/af869493b4)\
  2022-05-09 21:08:33 -0700
  * [MDEV-27892](https://jira.mariadb.org/browse/MDEV-27892) Improve an error message for foreign server exists
* [Revision #3dd3dccb8e](https://github.com/MariaDB/server/commit/3dd3dccb8e)\
  2022-05-10 00:04:10 +0000
  * [MDEV-22023](https://jira.mariadb.org/browse/MDEV-22023) Update man pages titles to say MariaDB instead of MySQL
* Merge [Revision #a0f0687f6c](https://github.com/MariaDB/server/commit/a0f0687f6c) 2022-05-23 08:07:56 +0300 - Merge 10.4 into 10.5
* Merge [Revision #f73bb92848](https://github.com/MariaDB/server/commit/f73bb92848) 2022-05-20 19:30:08 +0200 - Merge branch '10.5' into bb-10.5-release
* [Revision #ebc140a78e](https://github.com/MariaDB/server/commit/ebc140a78e)\
  2022-05-20 12:05:54 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
