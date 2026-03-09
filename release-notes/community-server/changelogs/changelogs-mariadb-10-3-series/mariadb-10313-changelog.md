# MariaDB 10.3.13 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://mariadb.com/downloads/?showall=1\&tab=mariadb_platform\&group=mariadb_server\&version=10.3.13)[Release Notes](../../old-releases/10.3/10.3.13.md)[Changelog](mariadb-10313-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.3.13/)

**Release date:** 21 Feb 2019

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.13.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #c8f9b3f915](https://github.com/MariaDB/server/commit/c8f9b3f915)\
  2019-02-20 08:44:08 +0100
  * remove aws-key management plugin
* [Revision #5296aa8b12](https://github.com/MariaDB/server/commit/5296aa8b12)\
  2019-02-20 12:25:57 +0100
  * [MDEV-18663](https://jira.mariadb.org/browse/MDEV-18663) Tests : use --core-file if mariadb-backup output is redirected to a file
* [Revision #1005376e58](https://github.com/MariaDB/server/commit/1005376e58)\
  2019-02-20 04:14:23 +0200
  * Updated list of unstable tests for 10.3.13 release
* [Revision #c65daf02f0](https://github.com/MariaDB/server/commit/c65daf02f0)\
  2019-02-19 19:11:40 +0100
  * make compatible parser in sync with main one
* Merge [Revision #00906719fe](https://github.com/MariaDB/server/commit/00906719fe) 2019-02-19 17:26:44 +0100 - Merge branch '10.2' into bb-10.3-merge
* Merge [Revision #91d506cf2d](https://github.com/MariaDB/server/commit/91d506cf2d) 2019-02-19 16:47:45 +0100 - Merge branch '10.1' into 10.2
* [Revision #431da59f1c](https://github.com/MariaDB/server/commit/431da59f1c)\
  2019-02-19 16:09:46 +0100
  * centos has symlinks /bin->usr/bin and /sbin -> usr/sbin, but even if this script called as /bin/mysql\_install\_db it is still standard install and scripts are in /usr/share/ (but not in the /share/)
  * fix of bindir path
* [Revision #2de0b57dd1](https://github.com/MariaDB/server/commit/2de0b57dd1)\
  2019-02-18 11:12:52 +0100
  * Don't build aws\_key\_management plugin by default
* Merge [Revision #055c09ad6b](https://github.com/MariaDB/server/commit/055c09ad6b) 2019-02-19 17:26:32 +0100 - Merge branch '10.3' into bb-10.3-merge
* Merge [Revision #fc124778ea](https://github.com/MariaDB/server/commit/fc124778ea) 2019-02-19 17:41:13 +0200 - Merge 10.2 into 10.3
* [Revision #88b6dc4db5](https://github.com/MariaDB/server/commit/88b6dc4db5)\
  2019-02-19 14:47:10 +0200
  * [MDEV-18639](https://jira.mariadb.org/browse/MDEV-18639) Assertion failure upon attempt to start with lower number of undo tablespaces
* Merge [Revision #af6fdc1307](https://github.com/MariaDB/server/commit/af6fdc1307) 2019-02-19 11:15:10 +0200 - Merge 10.1 into 10.2
* [Revision #346e460896](https://github.com/MariaDB/server/commit/346e460896)\
  2019-02-19 10:51:34 +0200
  * Fixed bug in macro \_ma\_mark\_page\_with\_transid()
* [Revision #ca76fc4a3a](https://github.com/MariaDB/server/commit/ca76fc4a3a)\
  2019-02-19 11:14:03 +0200
  * [MDEV-18611](https://jira.mariadb.org/browse/MDEV-18611): mariadb-backup silently ended during xtrabackup\_copy\_logfile()
* [Revision #d2fc9d09da](https://github.com/MariaDB/server/commit/d2fc9d09da)\
  2019-02-19 07:31:25 +0100
  * [MDEV-18204](https://jira.mariadb.org/browse/MDEV-18204) - fixup
* Merge [Revision #e3f6ea5080](https://github.com/MariaDB/server/commit/e3f6ea5080) 2019-02-18 22:21:02 +0200 - Merge 10.1 into 10.2
* [Revision #98e185ee37](https://github.com/MariaDB/server/commit/98e185ee37)\
  2019-02-18 21:42:58 +0200
  * [MDEV-18630](https://jira.mariadb.org/browse/MDEV-18630) Uninitialised value in FOREIGN KEY error message
* [Revision #3a42926c88](https://github.com/MariaDB/server/commit/3a42926c88)\
  2019-02-18 18:56:32 +0100
  * [MDEV-18204](https://jira.mariadb.org/browse/MDEV-18204) Fix rocksdb incremental backup
* [Revision #40b4f9c907](https://github.com/MariaDB/server/commit/40b4f9c907)\
  2019-02-14 11:54:34 +0100
  * [MDEV-18575](https://jira.mariadb.org/browse/MDEV-18575) remove innodb-encrypt-log parameter from mariadb-backup
* Merge [Revision #10cc8bbdbb](https://github.com/MariaDB/server/commit/10cc8bbdbb) 2019-02-13 09:26:37 +0200 - Merge pull request #1181 from grooverdan/10.2-submodule-update
* [Revision #43a7409bb8](https://github.com/MariaDB/server/commit/43a7409bb8)\
  2019-02-13 17:48:12 +1100
  * typo cmake/submodules.cmake
* [Revision #17c3f147f8](https://github.com/MariaDB/server/commit/17c3f147f8)\
  2019-02-13 09:03:12 +1100
  * cmake/submodules: notify user about gitconfig for automatic update
* [Revision #a4cd91c526](https://github.com/MariaDB/server/commit/a4cd91c526)\
  2018-11-20 15:19:32 +0300
  * [MDEV-18603](https://jira.mariadb.org/browse/MDEV-18603) Debug option to disable InnoDB monitor threads
* [Revision #df51dc28f5](https://github.com/MariaDB/server/commit/df51dc28f5)\
  2019-02-16 12:06:52 +0200
  * Fix tests for innodb\_checksum\_algorithm=strict\_crc32
* [Revision #e8b6c15010](https://github.com/MariaDB/server/commit/e8b6c15010)\
  2019-02-13 23:26:23 +0400
  * connect.xml.result fixed.
* [Revision #ce0678f6cb](https://github.com/MariaDB/server/commit/ce0678f6cb)\
  2018-05-22 07:49:44 +1000
  * hash (storage): hp\_hashnr is local
* [Revision #7fa67e391f](https://github.com/MariaDB/server/commit/7fa67e391f)\
  2018-05-21 15:16:36 +1000
  * heap: remove NEW\_HASH\_FUNCTION
* [Revision #438811b4b2](https://github.com/MariaDB/server/commit/438811b4b2)\
  2019-02-13 18:21:19 +0200
  * Fixed two bugs related to column level constraints
* [Revision #44898d28f0](https://github.com/MariaDB/server/commit/44898d28f0)\
  2019-02-06 08:28:48 +1100
  * my\_close: Don't retry on close
* [Revision #8a3a332bc0](https://github.com/MariaDB/server/commit/8a3a332bc0)\
  2019-02-13 17:40:03 +0400
  * Cleanup Item\_func\_sp::fix\_fields()
* [Revision #a3ccad0f21](https://github.com/MariaDB/server/commit/a3ccad0f21)\
  2019-02-12 15:38:01 +1100
  * Aggregate functions: only create list if args exist
* [Revision #75bb5e457c](https://github.com/MariaDB/server/commit/75bb5e457c)\
  2019-02-18 23:51:56 +0100
  * fix of windows compiler warnings
* [Revision #5b43dbb33e](https://github.com/MariaDB/server/commit/5b43dbb33e)\
  2019-02-18 09:51:08 +0100
  * rempve relaxed chack made by galera
* [Revision #221d462cc7](https://github.com/MariaDB/server/commit/221d462cc7)\
  2019-02-18 09:42:46 +0100
  * fix for windows
* [Revision #6ffbfb92ed](https://github.com/MariaDB/server/commit/6ffbfb92ed)\
  2019-02-14 12:53:49 +0100
  * Try to fix windows compiler warnings
* [Revision #56a8acd2e9](https://github.com/MariaDB/server/commit/56a8acd2e9)\
  2019-02-14 11:06:15 +0100
  * fix problem of last /
* [Revision #1b6b99be24](https://github.com/MariaDB/server/commit/1b6b99be24)\
  2019-02-12 16:17:47 +0100
  * tempesta fixes
* Merge [Revision #dcc838168f](https://github.com/MariaDB/server/commit/dcc838168f) 2019-02-12 12:05:10 +0100 - Merge branch '10.3' into bb-10.3-merge
* [Revision #4e7ee166a9](https://github.com/MariaDB/server/commit/4e7ee166a9)\
  2019-02-11 14:40:28 +0200
  * [MDEV-18295](https://jira.mariadb.org/browse/MDEV-18295) IMPORT TABLESPACE fails with instant-altered tables
* [Revision #4eae9eeccc](https://github.com/MariaDB/server/commit/4eae9eeccc)\
  2019-02-06 20:43:28 +0200
  * Backport BUILD scripts from 10.4
* [Revision #d0799a0479](https://github.com/MariaDB/server/commit/d0799a0479)\
  2019-02-06 20:42:15 +0200
  * Removed compiler warnings from tokudb
* [Revision #8bee13da81](https://github.com/MariaDB/server/commit/8bee13da81)\
  2019-02-06 20:41:38 +0200
  * Added generated wsrep\_xxx files to .gitignore
* [Revision #129b2dcef3](https://github.com/MariaDB/server/commit/129b2dcef3)\
  2019-02-06 16:12:12 +0200
  * Changed user\_variables and sql\_sequence to maturity state stable
* [Revision #e33daef446](https://github.com/MariaDB/server/commit/e33daef446)\
  2019-02-06 08:35:48 +1100
  * Don't retry on close
* Merge [Revision #b953d70d15](https://github.com/MariaDB/server/commit/b953d70d15) 2019-02-12 12:04:10 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #8a9cdc5f44](https://github.com/MariaDB/server/commit/8a9cdc5f44) 2019-02-12 09:54:12 +0200 - Merge 10.1 into 10.2
* [Revision #5b82751111](https://github.com/MariaDB/server/commit/5b82751111)\
  2019-02-06 16:44:36 +0100
  * [MDEV-18426](https://jira.mariadb.org/browse/MDEV-18426): Most of the mtr tests in the galera\_3nodes suite fail
* Merge [Revision #9e4f299404](https://github.com/MariaDB/server/commit/9e4f299404) 2019-02-11 11:42:18 +0200 - Merge 10.1 into 10.2
* [Revision #be25414828](https://github.com/MariaDB/server/commit/be25414828)\
  2019-02-11 11:36:00 +0200
  * [MDEV-18016](https://jira.mariadb.org/browse/MDEV-18016): Cover the no-rebuild case, and remove a bogus debug assertion
* [Revision #31d6e9c3c8](https://github.com/MariaDB/server/commit/31d6e9c3c8)\
  2019-02-12 10:48:19 +0100
  * Fix of error messages with big help of serg
* [Revision #fa57e11844](https://github.com/MariaDB/server/commit/fa57e11844)\
  2019-02-11 14:36:24 +0200
  * [MDEV-10963](https://jira.mariadb.org/browse/MDEV-10963) manual merge 10.1->10.3.
* [Revision #0cdcb5f083](https://github.com/MariaDB/server/commit/0cdcb5f083)\
  2019-02-11 12:38:43 +0200
  * Re-record some results
* [Revision #55bb279c6f](https://github.com/MariaDB/server/commit/55bb279c6f)\
  2019-02-11 12:34:46 +0200
  * Correctly resolve the conflict around commit\_cache\_norebuild()
* [Revision #69e552279c](https://github.com/MariaDB/server/commit/69e552279c)\
  2019-02-07 17:12:49 +0200
  * merge fixes: sql\_table.cc and partition\_info.cc (caused by ef4ccb6ce2fd3) done
* [Revision #1efc19904a](https://github.com/MariaDB/server/commit/1efc19904a)\
  2019-02-07 15:57:15 +0200
  * merge fixes: sql\_binlog.cc is done
* Merge [Revision #65c5ef9b49](https://github.com/MariaDB/server/commit/65c5ef9b49) 2019-02-07 13:59:31 +0100 - dirty merge
* [Revision #7293ce0ee8](https://github.com/MariaDB/server/commit/7293ce0ee8)\
  2019-02-04 17:52:39 +0300
  * [MDEV-18470](https://jira.mariadb.org/browse/MDEV-18470) improve alter\_varchar\_change.test
* Merge [Revision #ab2458c61f](https://github.com/MariaDB/server/commit/ab2458c61f) 2019-02-04 15:12:14 +0200 - Merge 10.2 into 10.3
* [Revision #e214aa1cd3](https://github.com/MariaDB/server/commit/e214aa1cd3)\
  2019-02-02 10:02:03 +0100
  * [MDEV-18281](https://jira.mariadb.org/browse/MDEV-18281) COM\_RESET\_CONNECTION changes the connection encoding
* Merge [Revision #14a58cea59](https://github.com/MariaDB/server/commit/14a58cea59) 2019-01-31 19:52:11 +0200 - Merge pull request #1147 from tempesta-tech/sysprg/[MDEV-18426](https://jira.mariadb.org/browse/MDEV-18426)
* [Revision #c9f0a4a9bf](https://github.com/MariaDB/server/commit/c9f0a4a9bf)\
  2019-01-30 15:16:36 +0100
  * [MDEV-18426](https://jira.mariadb.org/browse/MDEV-18426): Most of the mtr tests in the galera\_3nodes suite fail
* [Revision #4e599c74bb](https://github.com/MariaDB/server/commit/4e599c74bb)\
  2019-01-30 03:29:37 +0900
  * [MDEV-18313](https://jira.mariadb.org/browse/MDEV-18313) Supports 'wrapper mariadb' for connection information
* [Revision #470c1b8d56](https://github.com/MariaDB/server/commit/470c1b8d56)\
  2018-12-31 23:42:49 +0900
  * Fix an error at using spider\_direct\_sql with temporary table
* [Revision #ea347fcb28](https://github.com/MariaDB/server/commit/ea347fcb28)\
  2018-12-25 00:22:45 +0900
  * remove unnecessary drop database/table from slave\_trx\_isolation.test add simplified slave\_trx\_isolation.test
* [Revision #be556f817b](https://github.com/MariaDB/server/commit/be556f817b)\
  2018-12-24 23:40:33 +0900
  * remove unnecessary drop database/table from quick\_mode.test add simplified quick\_mode.test
* [Revision #6d80d35d91](https://github.com/MariaDB/server/commit/6d80d35d91)\
  2018-12-13 03:11:57 +0900
  * [MDEV-16787](https://jira.mariadb.org/browse/MDEV-16787) optimistic parallel replication fails on spider Add a system variable spider\_slave\_trx\_isolation. - spider\_slave\_trx\_isolation The transaction isolation level when Spider table is used by slave SQL thread. -1 : OFF 0 : READ UNCOMMITTED 1 : READ COMMITTED 2 : REPEATABLE READ 3 : SERIALIZABLE The default value is -1
* [Revision #bef6b197fc](https://github.com/MariaDB/server/commit/bef6b197fc)\
  2018-11-30 03:17:08 +0900
  * [MDEV-16520](https://jira.mariadb.org/browse/MDEV-16520) Out-Of-Memory running big aggregate query on Spider Engine
* [Revision #3cb7c5f27b](https://github.com/MariaDB/server/commit/3cb7c5f27b)\
  2018-11-20 05:43:49 +0900
  * [MDEV-16279](https://jira.mariadb.org/browse/MDEV-16279) Spider crashes on CHECKSUM TABLE with spider\_quick\_mode=3 The fields of the temporary table were not created in create\_tmp\_table function. Because item->const\_item() was true. But the temporary tables that is created by Spider are always used all columns. So Spider should call create\_tmp\_table function with TMP\_TABLE\_ALL\_COLUMNS flag.
* [Revision #6caf9ec425](https://github.com/MariaDB/server/commit/6caf9ec425)\
  2018-11-20 00:12:58 +0900
  * Update Spider to version 3.3.14. Add direct left outer join/right outer join/inner join feature
* [Revision #36be0a5aef](https://github.com/MariaDB/server/commit/36be0a5aef)\
  2019-01-28 17:58:14 +0200
  * [MDEV-18399](https://jira.mariadb.org/browse/MDEV-18399) Recognize the deprecated parameters innodb\_file\_format, innodb\_large\_prefix
* Merge [Revision #3b1b665fcb](https://github.com/MariaDB/server/commit/3b1b665fcb) 2019-01-25 20:33:47 +0100 - Merge branch '10.2' into 10.3
* [Revision #a4ab66c8f8](https://github.com/MariaDB/server/commit/a4ab66c8f8)\
  2019-01-09 23:10:16 +0100
  * Make the PYTHON\_SHEBANG value configurable
* [Revision #7334f9717d](https://github.com/MariaDB/server/commit/7334f9717d)\
  2019-01-09 15:05:02 +0100
  * Do not import commands library as it is not used
* [Revision #e99e6f29e9](https://github.com/MariaDB/server/commit/e99e6f29e9)\
  2019-01-05 11:49:35 +0100
  * cleanup: trg2bit() helper
* [Revision #0e1f7f5c4a](https://github.com/MariaDB/server/commit/0e1f7f5c4a)\
  2019-01-25 12:04:28 +0300
  * [MDEV-18057](https://jira.mariadb.org/browse/MDEV-18057) Assertion \`(node->state == 5) || (node->state == 6)' failed in row\_upd\_sec\_step upon DELETE after UPDATE failed due to FK violation
* Merge [Revision #9bd80ada6f](https://github.com/MariaDB/server/commit/9bd80ada6f) 2019-01-25 16:35:13 +0200 - Merge 10.2 into 10.3
* Merge [Revision #f2518f3da9](https://github.com/MariaDB/server/commit/f2518f3da9) 2019-01-25 14:38:44 +0200 - Merge pull request #1136 from tempesta-tech/sysprg/[MDEV-18379](https://jira.mariadb.org/browse/MDEV-18379)
* [Revision #a22dc6268b](https://github.com/MariaDB/server/commit/a22dc6268b)\
  2019-01-25 12:29:50 +0100
  * [MDEV-18379](https://jira.mariadb.org/browse/MDEV-18379): Unification of check for IPv6
* [Revision #45c47a04bd](https://github.com/MariaDB/server/commit/45c47a04bd)\
  2019-01-24 10:43:27 +0100
  * [MDEV-17401](https://jira.mariadb.org/browse/MDEV-17401): LOAD DATA from very big file into MyISAM table results in EOF error and corrupt index
* Merge [Revision #e9ba165bcb](https://github.com/MariaDB/server/commit/e9ba165bcb) 2019-01-25 08:03:48 +0200 - Merge pull request #1129 from GeoffMontee/10.3-geoff-[MDEV-18372](https://jira.mariadb.org/browse/MDEV-18372)
* [Revision #f4ca2445c3](https://github.com/MariaDB/server/commit/f4ca2445c3)\
  2019-01-24 17:18:26 -0500
  * [MDEV-18372](https://jira.mariadb.org/browse/MDEV-18372): Minor [MDEV-17973](https://jira.mariadb.org/browse/MDEV-17973)-related merge issue to 10.3
* Merge [Revision #947b6b849d](https://github.com/MariaDB/server/commit/947b6b849d) 2019-01-24 16:14:12 +0200 - Merge 10.2 into 10.3
* Merge [Revision #55be043c13](https://github.com/MariaDB/server/commit/55be043c13) 2019-01-23 12:07:36 +0200 - Merge pull request #1120 from tempesta-tech/sysprg/[MDEV-17835](https://jira.mariadb.org/browse/MDEV-17835) v2
* [Revision #0e89e90f42](https://github.com/MariaDB/server/commit/0e89e90f42)\
  2019-01-22 13:28:03 +0100
  * [MDEV-17835](https://jira.mariadb.org/browse/MDEV-17835): Remove wsrep-sst-method=xtrabackup
* [Revision #d4144c8e01](https://github.com/MariaDB/server/commit/d4144c8e01)\
  2019-01-21 09:32:06 +0200
  * [MDEV-17821](https://jira.mariadb.org/browse/MDEV-17821) Assertion !page\_rec\_is\_supremum(rec) failed in btr\_pcur\_store\_position
* [Revision #778192454e](https://github.com/MariaDB/server/commit/778192454e)\
  2019-01-18 14:22:33 +0200
  * [MDEV-17823](https://jira.mariadb.org/browse/MDEV-17823): Fix the non-debug build
* [Revision #4e75bfcb21](https://github.com/MariaDB/server/commit/4e75bfcb21)\
  2019-01-18 12:39:19 +0200
  * [MDEV-18152](https://jira.mariadb.org/browse/MDEV-18152) Assertion 'num\_fts\_index <= 1' failed
* Merge [Revision #a0d3ead83a](https://github.com/MariaDB/server/commit/a0d3ead83a) 2019-01-18 10:43:31 +0200 - Merge 10.2 into 10.3
* [Revision #5f60c7c3c2](https://github.com/MariaDB/server/commit/5f60c7c3c2)\
  2019-01-18 10:39:52 +0200
  * [MDEV-17823](https://jira.mariadb.org/browse/MDEV-17823) Assertion failed when accessing indexed instantly added column
* Merge [Revision #77cbaa96ad](https://github.com/MariaDB/server/commit/77cbaa96ad) 2019-01-17 12:33:31 +0200 - Merge 10.2 into 10.3
* [Revision #62a0224666](https://github.com/MariaDB/server/commit/62a0224666)\
  2019-01-09 09:26:17 +1100
  * safemalloc: put bad\_ptr error arguments in right order
* [Revision #848fd3f765](https://github.com/MariaDB/server/commit/848fd3f765)\
  2019-01-16 05:25:53 +0200
  * Add release result diff for galera\_ist\_innodb\_flush\_logs
* [Revision #8655592ae5](https://github.com/MariaDB/server/commit/8655592ae5)\
  2019-01-15 08:52:26 +0200
  * recv\_log\_recover\_10\_4(): Fix a trivial bug
* Merge [Revision #efb510462e](https://github.com/MariaDB/server/commit/efb510462e) 2019-01-14 14:55:50 +0200 - Merge 10.2 into 10.3
* [Revision #a75dbfd718](https://github.com/MariaDB/server/commit/a75dbfd718)\
  2019-01-14 14:37:34 +0200
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Remove fil\_space\_t::name\_hash
* [Revision #69290ce3eb](https://github.com/MariaDB/server/commit/69290ce3eb)\
  2019-01-14 09:24:39 +0200
  * [MDEV-18224](https://jira.mariadb.org/browse/MDEV-18224) MTR's internal check of the test case 'innodb.recovery\_shutdown' failed due to extra #sql-ib\*.ibd files
* [Revision #82490a97db](https://github.com/MariaDB/server/commit/82490a97db)\
  2019-01-10 16:08:26 +0400
  * [MDEV-18150](https://jira.mariadb.org/browse/MDEV-18150) Assertion \`decimals\_to\_set <= 38' failed in Item\_func\_round::fix\_length\_and\_dec\_decimal
* [Revision #2ffa11e33e](https://github.com/MariaDB/server/commit/2ffa11e33e)\
  2019-01-09 15:00:56 +0200
  * Appveyor configuration and addition of badge
* Merge [Revision #4bf47cb989](https://github.com/MariaDB/server/commit/4bf47cb989) 2019-01-09 10:17:51 +0000 - Merge pull request #559 from grooverdan/10.3-travis-systemversioning
* [Revision #5cf45fb272](https://github.com/MariaDB/server/commit/5cf45fb272)\
  2018-01-18 20:33:02 +1100
  * travis: add versioning to test suite
* Merge [Revision #13df03a04e](https://github.com/MariaDB/server/commit/13df03a04e) 2019-01-09 07:53:22 +0000 - Merge pull request #768 from grooverdan/10.3-travis-osx-zstd
* [Revision #2b39f43613](https://github.com/MariaDB/server/commit/2b39f43613)\
  2018-05-23 14:58:13 +1000
  * travis: add zstd for osx
* Merge [Revision #38f1c9df32](https://github.com/MariaDB/server/commit/38f1c9df32) 2019-01-08 17:37:44 +0200 - Merge 10.2 into 10.3
* [Revision #d27bea9e9a](https://github.com/MariaDB/server/commit/d27bea9e9a)\
  2019-01-07 07:31:25 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
