# MariaDB 10.1.42 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

After an upgrade MariaDB Server can crash if InnoDB tables exist with a `FULLTEXT INDEX` and a `FOREIGN KEY` constraint attached to them. We got reports that the crash already will be encountered on startup, but a crash is also possible at a later stage. See [MDEV-20987](https://jira.mariadb.org/browse/MDEV-20987) for more details.**Do not download or use this release.**

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.1/10.1.42.md)[Changelog](mariadb-10142-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.1.42/)

**Release date:** 5 Nov 2019

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.42.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 5.5.66](../changelogs-mariadb-55-series/mariadb-5566-changelog.md)
* [Revision #d925aec1c1](https://github.com/MariaDB/server/commit/d925aec1c1)\
  2019-10-31 18:07:19 +0200
  * List of unstable tests for 10.1.42 release
* [Revision #1bb857089f](https://github.com/MariaDB/server/commit/1bb857089f)\
  2019-10-31 07:44:18 +0200
  * [MDEV-20927](https://jira.mariadb.org/browse/MDEV-20927): Remove duplicated code
* [Revision #313855766f](https://github.com/MariaDB/server/commit/313855766f)\
  2019-10-30 19:42:16 +0100
  * cleanup
* [Revision #5392b4a32c](https://github.com/MariaDB/server/commit/5392b4a32c)\
  2019-10-30 19:31:26 +0100
  * [MDEV-20354](https://jira.mariadb.org/browse/MDEV-20354) All but last insert ignored in InnoDB tables when table locked
* Merge [Revision #c8ba98206f](https://github.com/MariaDB/server/commit/c8ba98206f) 2019-10-30 20:01:51 +0100 - Merge branch '10.1' into bb-10.1-release
* [Revision #8fce180765](https://github.com/MariaDB/server/commit/8fce180765)\
  2019-10-30 09:50:52 +0100
  * [MDEV-19432](https://jira.mariadb.org/browse/MDEV-19432) Systemd service does not get re-enabled after upgrade
* Merge [Revision #d671f506b0](https://github.com/MariaDB/server/commit/d671f506b0) 2019-10-30 14:47:35 +0100 - Merge branch '5.5' into 10.1
* Merge [Revision #708d46158b](https://github.com/MariaDB/server/commit/708d46158b) 2019-10-30 13:55:35 +0100 - Merge remote-tracking branch 'connect/10.1' into 10.1
* Merge [Revision #ea084a41c8](https://github.com/MariaDB/server/commit/ea084a41c8) 2019-08-24 22:57:14 +0200 - Merge branch 'ob-10.1' into 10.1
* [Revision #0043593b9d](https://github.com/MariaDB/server/commit/0043593b9d)\
  2019-08-24 17:32:38 +0200
  * Fix xml(2)\_mult.test result mismatch
* [Revision #dd30ba4c1b](https://github.com/MariaDB/server/commit/dd30ba4c1b)\
  2019-08-24 16:14:24 +0200
  * In CONNECT version 1.6.10 NOSQL facility is enhanced by a new way to retrieve NOSQL data. In addition to files and Mongo collections, JSON as well as XML and CSV data can be retrieved from the net as answers from REST queries. Because it uses and external package (cpprestsdk) this is currently available only to MariaDB servers compiled from source.
* Merge [Revision #b58c38a3a9](https://github.com/MariaDB/server/commit/b58c38a3a9) 2019-10-30 13:49:25 +0100 - Merge branch 'merge-tokudb-5.6' into 10.1
* [Revision #a3553a1387](https://github.com/MariaDB/server/commit/a3553a1387)\
  2019-10-30 11:15:05 +0100
  * 5.6.45-86.1
* [Revision #d03a59c6ff](https://github.com/MariaDB/server/commit/d03a59c6ff)\
  2019-10-30 11:56:05 +0200
  * XtraDB 5.6.45-86.1
* [Revision #d1e6b0bcff](https://github.com/MariaDB/server/commit/d1e6b0bcff)\
  2019-10-30 12:36:57 +0200
  * [MDEV-20927](https://jira.mariadb.org/browse/MDEV-20927) Duplicate key with auto increment
* [Revision #b8eff8bce4](https://github.com/MariaDB/server/commit/b8eff8bce4)\
  2019-10-30 13:23:15 +0300
  * avoid accessing TLS
* [Revision #a7e3008ab3](https://github.com/MariaDB/server/commit/a7e3008ab3)\
  2019-10-30 12:53:25 +0300
  * [MDEV-20926](https://jira.mariadb.org/browse/MDEV-20926) UBSAN: load of value 165, which is not a valid value for type bool
* [Revision #bc8a9ab5f3](https://github.com/MariaDB/server/commit/bc8a9ab5f3)\
  2019-10-29 23:02:03 +0300
  * remove unused struct members
* Merge [Revision #9ed4d06706](https://github.com/MariaDB/server/commit/9ed4d06706) 2019-10-29 22:10:43 +0300 - Merge 5.5 into 10.1
* [Revision #2cc360bdf2](https://github.com/MariaDB/server/commit/2cc360bdf2)\
  2019-10-28 16:03:00 +0200
  * Remove bogus advice
* [Revision #a41d429765](https://github.com/MariaDB/server/commit/a41d429765)\
  2019-10-22 12:05:42 +0530
  * [MDEV-20621](https://jira.mariadb.org/browse/MDEV-20621) FULLTEXT INDEX activity causes InnoDB hang
* [Revision #bd22650bbc](https://github.com/MariaDB/server/commit/bd22650bbc)\
  2019-10-23 17:00:12 +0530
  * [MDEV-19073](https://jira.mariadb.org/browse/MDEV-19073) FTS row mismatch after crash recovery
* Merge [Revision #790a74d22b](https://github.com/MariaDB/server/commit/790a74d22b) 2019-10-21 19:00:42 +0200 - Merge branch 'github/5.5' into 10.1
* [Revision #ae702d7643](https://github.com/MariaDB/server/commit/ae702d7643)\
  2019-10-14 16:38:28 +0300
  * [MDEV-20813](https://jira.mariadb.org/browse/MDEV-20813): Remove the buf\_flush\_init\_for\_writing() assertion
* [Revision #2920377aa0](https://github.com/MariaDB/server/commit/2920377aa0)\
  2019-10-14 12:56:43 +0300
  * [MDEV-19740](https://jira.mariadb.org/browse/MDEV-19740): Fix C++11 violations caught by GCC 9.2.1
* [Revision #2ae02c295a](https://github.com/MariaDB/server/commit/2ae02c295a)\
  2019-10-07 12:34:08 +0200
  * [MDEV-20728](https://jira.mariadb.org/browse/MDEV-20728): /usr/sbin/mysqld: unknown variable 'defaults-group-suffix=mysqld1
* [Revision #c0c003beb4](https://github.com/MariaDB/server/commit/c0c003beb4)\
  2019-10-11 15:32:04 +0300
  * [MDEV-20805](https://jira.mariadb.org/browse/MDEV-20805) follow-up: Catch writes of bogus pages
* Merge [Revision #cbfd6882f4](https://github.com/MariaDB/server/commit/cbfd6882f4) 2019-10-11 15:19:55 +0300 - Merge 5.5 into 10.1
* [Revision #5ef1224434](https://github.com/MariaDB/server/commit/5ef1224434)\
  2019-10-11 12:29:12 +0300
  * [MDEV-20804](https://jira.mariadb.org/browse/MDEV-20804) Speed up main.index\_merge\_innodb
* Merge [Revision #d95f96ad1b](https://github.com/MariaDB/server/commit/d95f96ad1b) 2019-10-08 12:43:37 +0300 - Merge 5.5 into 10.1
* [Revision #adefaeffcc](https://github.com/MariaDB/server/commit/adefaeffcc)\
  2019-10-02 16:04:52 +0400
  * [MDEV-19536](https://jira.mariadb.org/browse/MDEV-19536) - Server crash or ASAN heap-use-after-free in is\_temporary\_table / read\_statistics\_for\_tables\_if\_needed
* [Revision #e43791d4dc](https://github.com/MariaDB/server/commit/e43791d4dc)\
  2019-10-02 15:23:59 +0400
  * Cleanup EITS
* Merge [Revision #4bcf524482](https://github.com/MariaDB/server/commit/4bcf524482) 2019-10-01 06:07:56 +0400 - Merge remote-tracking branch 'origin/5.5' into 10.1
* [Revision #9b80f9300d](https://github.com/MariaDB/server/commit/9b80f9300d)\
  2019-09-30 13:22:37 +0530
  * [MDEV-20645](https://jira.mariadb.org/browse/MDEV-20645): Replication consistency is broken as workers miss the error notification from an earlier failed group.
* [Revision #677cc64428](https://github.com/MariaDB/server/commit/677cc64428)\
  2019-09-27 13:20:00 +0200
  * chkconfig in RPM server scriptlets
* [Revision #144217339d](https://github.com/MariaDB/server/commit/144217339d)\
  2019-09-25 14:00:39 +0200
  * [MDEV-20614](https://jira.mariadb.org/browse/MDEV-20614): Syntax error, and option put in wrong place
* [Revision #516f7c111b](https://github.com/MariaDB/server/commit/516f7c111b)\
  2019-09-25 11:29:21 +0300
  * Speed up main.sum\_distinct-big
* Merge [Revision #5f118b26c8](https://github.com/MariaDB/server/commit/5f118b26c8) 2019-09-24 11:16:36 +0400 - Merge remote-tracking branch 'origin/5.5' into 10.1
* [Revision #896974fc3d](https://github.com/MariaDB/server/commit/896974fc3d)\
  2019-09-21 12:14:05 +0530
  * [MDEV-18094](https://jira.mariadb.org/browse/MDEV-18094): Query with order by limit picking index scan over filesort
* [Revision #7a4019a1c7](https://github.com/MariaDB/server/commit/7a4019a1c7)\
  2019-03-01 10:00:27 +0100
  * [MDEV-19207](https://jira.mariadb.org/browse/MDEV-19207) systemd service: add instance name in description
* [Revision #6a7d51b1cb](https://github.com/MariaDB/server/commit/6a7d51b1cb)\
  2019-09-21 01:04:07 +0300
  * [MDEV-19211](https://jira.mariadb.org/browse/MDEV-19211) Fix mysqld\_safe --dry-run
* [Revision #13c2fd36c1](https://github.com/MariaDB/server/commit/13c2fd36c1)\
  2019-06-02 12:05:53 +0300
  * Deb: Implement proper version detection in maintainer scripts
* [Revision #8a79fa0e4d](https://github.com/MariaDB/server/commit/8a79fa0e4d)\
  2019-09-18 13:22:08 +0530
  * [MDEV-19529](https://jira.mariadb.org/browse/MDEV-19529) InnoDB hang on DROP FULLTEXT INDEX
* [Revision #708f1e3419](https://github.com/MariaDB/server/commit/708f1e3419)\
  2019-09-17 20:47:58 +0530
  * [MDEV-19647](https://jira.mariadb.org/browse/MDEV-19647) Server hangs after dropping full text indexes and restart
* [Revision #ae2b88ff3f](https://github.com/MariaDB/server/commit/ae2b88ff3f)\
  2019-09-13 21:10:52 -0700
  * Adjusted test results after the change of a test case
* [Revision #0954bcb663](https://github.com/MariaDB/server/commit/0954bcb663)\
  2019-09-13 15:09:28 -0700
  * Post fix after the patch for [MDEV-20576](https://jira.mariadb.org/browse/MDEV-20576).
* [Revision #deb9121fdf](https://github.com/MariaDB/server/commit/deb9121fdf)\
  2019-09-12 23:00:49 -0700
  * [MDEV-20576](https://jira.mariadb.org/browse/MDEV-20576) A new assertion added to check validity of calculated selectivity values fails
* Merge [Revision #d6f0e60a67](https://github.com/MariaDB/server/commit/d6f0e60a67) 2019-09-11 08:06:53 +0300 - Merge 5.5 into 10.1
* [Revision #031c695b8c](https://github.com/MariaDB/server/commit/031c695b8c)\
  2019-09-09 15:39:12 +0400
  * [MDEV-16594](https://jira.mariadb.org/browse/MDEV-16594) ALTER DATA DIRECTORY in PARTITIONS of InnoDB storage does nothing silently
* [Revision #0e38cd37c7](https://github.com/MariaDB/server/commit/0e38cd37c7)\
  2019-07-27 19:57:46 +0530
  * [MDEV-20137](https://jira.mariadb.org/browse/MDEV-20137) rpl.mdev\_17588 fails in buildbot with "Table doesn't exist"
* [Revision #fe4eacde39](https://github.com/MariaDB/server/commit/fe4eacde39)\
  2019-09-03 16:02:46 +0400
  * [MDEV-17683](https://jira.mariadb.org/browse/MDEV-17683) sys\_vars.delayed\_insert\_limit\_func fails in buildbot with wrong result.
* [Revision #edb6e2b951](https://github.com/MariaDB/server/commit/edb6e2b951)\
  2019-09-03 11:23:12 +0200
  * [MDEV-17610](https://jira.mariadb.org/browse/MDEV-17610) - fix result, for the case when test runs with userstat=on
* [Revision #4ba20e0a14](https://github.com/MariaDB/server/commit/4ba20e0a14)\
  2019-08-28 04:49:01 +0200
  * Improved handling of subdirectories in the xtrabackup-v2 SST scripts (similar to [MDEV-18863](https://jira.mariadb.org/browse/MDEV-18863)) for more predictable test results (related to xtrabackup-v2 SST)
* [Revision #d4866c7d0d](https://github.com/MariaDB/server/commit/d4866c7d0d)\
  2019-08-26 19:19:12 +0300
  * fix clang warnings
* [Revision #f608713739](https://github.com/MariaDB/server/commit/f608713739)\
  2019-08-27 08:30:26 +0300
  * Enable galera\_sst\_mysqldump\_with\_key test case.
* [Revision #29bbf4749e](https://github.com/MariaDB/server/commit/29bbf4749e)\
  2019-08-27 09:13:20 +0400
  * [MDEV-19699](https://jira.mariadb.org/browse/MDEV-19699) Server crashes in Item\_null\_result::field\_type upon SELECT with ROLLUP on constant table
* [Revision #de0f93fb0d](https://github.com/MariaDB/server/commit/de0f93fb0d)\
  2019-08-26 13:37:09 +0200
  * [MDEV-20420](https://jira.mariadb.org/browse/MDEV-20420): SST failed after [MDEV-18863](https://jira.mariadb.org/browse/MDEV-18863) in some test configurations
* [Revision #4a9fb9055e](https://github.com/MariaDB/server/commit/4a9fb9055e)\
  2019-08-26 14:03:51 +0530
  * [MDEV-20188](https://jira.mariadb.org/browse/MDEV-20188): binlog.binlog\_stm\_drop\_tmp\_tbl fails in buildbot with Unknown table on exec
* [Revision #b01a95f6fc](https://github.com/MariaDB/server/commit/b01a95f6fc)\
  2019-08-22 17:37:13 +0300
  * row\_undo\_mod\_remove\_clust\_low(): Remove duplicated code
* [Revision #5b29820d80](https://github.com/MariaDB/server/commit/5b29820d80)\
  2019-08-22 11:11:22 +0300
  * Fix -Wstringop-truncation
* [Revision #94e6a4fa6a](https://github.com/MariaDB/server/commit/94e6a4fa6a)\
  2019-08-21 11:12:39 +0200
  * Bash-specific operator replaced by a universal one
* [Revision #91fdb931fa](https://github.com/MariaDB/server/commit/91fdb931fa)\
  2019-08-12 18:30:19 +0200
  * ensure that pam plugin is present in release packages
* [Revision #62cc991bc8](https://github.com/MariaDB/server/commit/62cc991bc8)\
  2019-07-14 12:17:32 +0200
  * really make CPACK\_RPM\_DEBUGINFO\_PACKAGE configurable
* [Revision #bc89b1c558](https://github.com/MariaDB/server/commit/bc89b1c558)\
  2019-08-20 07:47:11 +0300
  * [MDEV-18863](https://jira.mariadb.org/browse/MDEV-18863): Fix -Wsign-compare
* Merge [Revision #a02dd7e614](https://github.com/MariaDB/server/commit/a02dd7e614) 2019-08-20 07:31:44 +0300 - Merge 5.5 into 10.1
* [Revision #a7e2cd55ab](https://github.com/MariaDB/server/commit/a7e2cd55ab)\
  2019-08-19 22:42:56 +0400
  * [MDEV-19034](https://jira.mariadb.org/browse/MDEV-19034) ASAN unknown-crash in get\_date\_time\_separator with PAD\_CHAR\_TO\_FULL\_LENGTH
* [Revision #457dc9d64d](https://github.com/MariaDB/server/commit/457dc9d64d)\
  2019-07-30 13:45:13 +0200
  * [MDEV-18863](https://jira.mariadb.org/browse/MDEV-18863): Galera SST scripts can't read \[mysqldN] option groups
* Merge [Revision #f987de7122](https://github.com/MariaDB/server/commit/f987de7122) 2019-08-16 20:58:14 +0400 - Merge remote-tracking branch 'origin/5.5' into 10.1
* [Revision #ecdacf7264](https://github.com/MariaDB/server/commit/ecdacf7264)\
  2019-08-16 14:36:23 +0300
  * [MDEV-19834](https://jira.mariadb.org/browse/MDEV-19834) Selectivity of an equality condition discounted twice
* [Revision #fa74088838](https://github.com/MariaDB/server/commit/fa74088838)\
  2019-08-15 07:46:41 +0300
  * [MDEV-18778](https://jira.mariadb.org/browse/MDEV-18778): mysql\_tzinfo\_to\_sql does not work correctly in MariaDB Galera
* [Revision #1c75ad6eed](https://github.com/MariaDB/server/commit/1c75ad6eed)\
  2019-08-15 12:57:21 +0300
  * [MDEV-19834](https://jira.mariadb.org/browse/MDEV-19834) Selectivity of an equality condition discounted twice
* [Revision #588e67956a](https://github.com/MariaDB/server/commit/588e67956a)\
  2019-08-13 19:29:59 +0300
  * Make sure histograms do not write uninitialized bytes to record
* [Revision #c738aa240e](https://github.com/MariaDB/server/commit/c738aa240e)\
  2019-08-13 12:39:08 +0300
  * [MDEV-20138](https://jira.mariadb.org/browse/MDEV-20138) innodb.trx\_id\_future fails on big-endian
* [Revision #eff898f2a0](https://github.com/MariaDB/server/commit/eff898f2a0)\
  2019-08-13 12:30:36 +0300
  * [MDEV-20335](https://jira.mariadb.org/browse/MDEV-20335): Extra trans\_commit\_stmt after rollback caused by incorrect fix of [MDEV-14401](https://jira.mariadb.org/browse/MDEV-14401)
* Merge [Revision #15c1ab52a9](https://github.com/MariaDB/server/commit/15c1ab52a9) 2019-08-12 14:46:28 +0300 - Merge 5.5 into 10.1
* [Revision #7a9e1fcd45](https://github.com/MariaDB/server/commit/7a9e1fcd45)\
  2019-08-12 14:45:28 +0300
  * [MDEV-17614](https://jira.mariadb.org/browse/MDEV-17614): Re-record a result
* [Revision #284c72eacf](https://github.com/MariaDB/server/commit/284c72eacf)\
  2019-07-17 15:56:29 +0530
  * [MDEV-17614](https://jira.mariadb.org/browse/MDEV-17614) INSERT on dup key update is replication unsafe
* [Revision #47f8a18fec](https://github.com/MariaDB/server/commit/47f8a18fec)\
  2019-08-07 12:35:04 +0530
  * [MDEV-20247](https://jira.mariadb.org/browse/MDEV-20247) Replication hangs with "preparing" and never starts
* [Revision #eef7540405](https://github.com/MariaDB/server/commit/eef7540405)\
  2019-08-05 14:34:13 +0530
  * [MDEV-18930](https://jira.mariadb.org/browse/MDEV-18930): Failed CREATE OR REPLACE TEMPORARY not written into binary log makes data on master and slave diverge
* [Revision #319cec959c](https://github.com/MariaDB/server/commit/319cec959c)\
  2019-08-01 15:24:48 +0300
  * [MDEV-17638](https://jira.mariadb.org/browse/MDEV-17638) Improve error message about corruption of encrypted page
* [Revision #0bb8f33b55](https://github.com/MariaDB/server/commit/0bb8f33b55)\
  2019-07-31 09:55:57 -0400
  * bump the VERSION
* [Revision #f79212f96d](https://github.com/MariaDB/server/commit/f79212f96d)\
  2019-07-31 02:49:15 -0700
  * Fix extra space in mysql-test README

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
