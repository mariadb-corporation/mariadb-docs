# MariaDB 5.5.57 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.57)[Release Notes](../../old-releases/5.5/5.5.57.md)[Changelog](mariadb-5557-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 19 Jul 2017

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.57.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

* Merge [Revision #59fca5806a](https://github.com/MariaDB/server/commit/59fca5806a) 2017-07-18 19:50:11 +0200 - Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #46977e0a01](https://github.com/MariaDB/server/commit/46977e0a01)\
  2017-07-18 19:47:01 +0200
  * 5.5.55-38.8
* [Revision #cba2ac6ef1](https://github.com/MariaDB/server/commit/cba2ac6ef1)\
  2016-12-22 13:06:44 +0100
  * 5.5.53-38.5
* [Revision #58aaae6f2a](https://github.com/MariaDB/server/commit/58aaae6f2a)\
  2017-07-18 16:42:40 +0200
  * ensure that filename in COM\_BINLOG\_DUMP isn't too long
* [Revision #172e3a1bc6](https://github.com/MariaDB/server/commit/172e3a1bc6)\
  2017-05-01 18:34:11 +1000
  * [MDEV-12646](https://jira.mariadb.org/browse/MDEV-12646): Apply fixes found by Coverity static analysis tool
* [Revision #f9dbfa58a5](https://github.com/MariaDB/server/commit/f9dbfa58a5)\
  2017-03-15 08:33:46 +1100
  * [MDEV-658](https://jira.mariadb.org/browse/MDEV-658): debian debug symbols require compat 9
* [Revision #7c9d00e0bb](https://github.com/MariaDB/server/commit/7c9d00e0bb)\
  2017-07-18 14:48:25 +0200
  * Bug #24595639: INCORRECT BEHAVIOR IN QUERY WITH UNION AND GROUP BY
* [Revision #9b3360ea44](https://github.com/MariaDB/server/commit/9b3360ea44)\
  2017-07-18 14:47:40 +0200
  * BUG#25250768: WRITING ON A READ\_ONLY=ON SERVER WITHOUT SUPER PRIVILEGE
* [Revision #f6bcdb9e3c](https://github.com/MariaDB/server/commit/f6bcdb9e3c)\
  2017-07-18 14:45:44 +0200
  * test case for loadxml and spaces
* Merge [Revision #9a5fe1f4ea](https://github.com/MariaDB/server/commit/9a5fe1f4ea) 2017-07-18 14:59:10 +0200 - Merge remote-tracking branch 'mysql/5.5' into 5.5
* [Revision #e7fd6ed387](https://github.com/MariaDB/server/commit/e7fd6ed387)\
  2017-07-17 22:34:07 +0200
  * [MDEV-11240](https://jira.mariadb.org/browse/MDEV-11240): Server crashes in check\_view\_single\_update or Assertion \`derived->table' failed in mysql\_derived\_merge\_for\_insert
* [Revision #7e44eabdad](https://github.com/MariaDB/server/commit/7e44eabdad)\
  2017-07-18 13:19:34 +0400
  * [MDEV-11205](https://jira.mariadb.org/browse/MDEV-11205) UDF\_ARGS "attribute\_lengths" incorrect value.
* [Revision #c9883b7591](https://github.com/MariaDB/server/commit/c9883b7591)\
  2017-07-02 14:53:23 +1000
  * ma\_check/mi\_check: maria\_repair\_parallel initialization for !quick
* [Revision #7d309b5f74](https://github.com/MariaDB/server/commit/7d309b5f74)\
  2017-07-18 01:38:13 +0300
  * Add storage\_engine/parts overlay for MyISAM
* [Revision #d023156782](https://github.com/MariaDB/server/commit/d023156782)\
  2015-10-30 10:10:43 +0400
  * [MDEV-8692](https://jira.mariadb.org/browse/MDEV-8692) prefschema test failures on ARM (on Debian build system)
* [Revision #6efee22541](https://github.com/MariaDB/server/commit/6efee22541)\
  2017-07-14 19:08:59 +0200
  * change flags as it was done in MyISAM
* [Revision #ec4e39558e](https://github.com/MariaDB/server/commit/ec4e39558e)\
  2017-07-02 17:02:03 +1000
  * ma\_recovery: unintentional order of operations
* [Revision #0375f2e273](https://github.com/MariaDB/server/commit/0375f2e273)\
  2017-07-14 15:30:27 +0200
  * [MDEV-12144](https://jira.mariadb.org/browse/MDEV-12144) Signal 6 crash corrupts ibd files
* [Revision #7338d3f221](https://github.com/MariaDB/server/commit/7338d3f221)\
  2017-07-14 13:37:37 +1000
  * client: mysql - fix type
* [Revision #27bc13b7a2](https://github.com/MariaDB/server/commit/27bc13b7a2)\
  2017-07-12 19:31:01 +0200
  * [MDEV-12136](https://jira.mariadb.org/browse/MDEV-12136) SELECT COUNT(DISTINCT) returns the wrong value when tmp\_table\_size is limited
* [Revision #e7f51e5d26](https://github.com/MariaDB/server/commit/e7f51e5d26)\
  2017-07-12 19:20:52 +0200
  * [MDEV-12136](https://jira.mariadb.org/browse/MDEV-12136) SELECT COUNT(DISTINCT) returns the wrong value when tmp\_table\_size is limited
* [Revision #181d9d2892](https://github.com/MariaDB/server/commit/181d9d2892)\
  2017-07-12 15:54:04 +0200
  * [MDEV-13180](https://jira.mariadb.org/browse/MDEV-13180) Unused left join causes server crash
* [Revision #05b678bc8c](https://github.com/MariaDB/server/commit/05b678bc8c)\
  2017-07-12 14:21:41 +0200
  * [MDEV-12489](https://jira.mariadb.org/browse/MDEV-12489) The select stmt may fail due to "having clause is ambiguous" unexpected
* [Revision #c83d6ff881](https://github.com/MariaDB/server/commit/c83d6ff881)\
  2017-07-12 13:55:04 +0200
  * compiler warning
* [Revision #d2e66a6f19](https://github.com/MariaDB/server/commit/d2e66a6f19)\
  2017-07-12 13:46:15 +0200
  * [MDEV-7828](https://jira.mariadb.org/browse/MDEV-7828) Assertion \`key\_read == 0' failed in TABLE::enable\_keyread with SELECT SQ and WHERE SQ
* [Revision #be55bbc2b2](https://github.com/MariaDB/server/commit/be55bbc2b2)\
  2017-07-12 12:49:29 +0200
  * [MDEV-7826](https://jira.mariadb.org/browse/MDEV-7826) Server crashes in Item\_subselect::enumerate\_field\_refs\_processor
* [Revision #c5975eaea1](https://github.com/MariaDB/server/commit/c5975eaea1)\
  2017-07-12 08:05:42 +0200
  * [MDEV-7339](https://jira.mariadb.org/browse/MDEV-7339) Server crashes in Item\_func\_trig\_cond::val\_int
* [Revision #f305a7ce4b](https://github.com/MariaDB/server/commit/f305a7ce4b)\
  2017-07-06 14:06:37 +0200
  * bugfix: long partition names
* [Revision #a7ed4644a6](https://github.com/MariaDB/server/commit/a7ed4644a6)\
  2017-07-03 13:35:32 +0200
  * [MDEV-10146](https://jira.mariadb.org/browse/MDEV-10146): Wrong result (or questionable result and behavior) with aggregate function in uncorrelated SELECT subquery
* [Revision #23ac2dd2a4](https://github.com/MariaDB/server/commit/23ac2dd2a4)\
  2017-07-04 13:28:47 +1000
  * sql\_class: incorrect assignment in Security\_context::destroy
* [Revision #89b81a9a24](https://github.com/MariaDB/server/commit/89b81a9a24)\
  2017-07-02 13:52:34 +1000
  * ma\_pagecache: release lock in pagecache\_read
* [Revision #2328860379](https://github.com/MariaDB/server/commit/2328860379)\
  2017-07-02 13:42:46 +1000
  * ma\_loghandler: translog\_set\_only\_in\_buffers failed to release lock
* [Revision #051f90a534](https://github.com/MariaDB/server/commit/051f90a534)\
  2017-07-02 13:37:14 +1000
  * ma\_loghandler: release file\_header\_lock on error
* [Revision #623c3f6731](https://github.com/MariaDB/server/commit/623c3f6731)\
  2017-07-02 11:26:02 +1000
  * thread\_group\_close: release mutex in all branches
* [Revision #cb870674d4](https://github.com/MariaDB/server/commit/cb870674d4)\
  2017-07-02 15:40:37 +1000
  * ha\_archive::info remove hidden assignment
* [Revision #9fc71eebb6](https://github.com/MariaDB/server/commit/9fc71eebb6)\
  2017-07-02 16:48:11 +1000
  * item\_timefunc: identical operands
* [Revision #4db6e1e4a5](https://github.com/MariaDB/server/commit/4db6e1e4a5)\
  2017-06-29 20:47:08 +0200
  * uninitialized variable
* [Revision #d5cd334504](https://github.com/MariaDB/server/commit/d5cd334504)\
  2017-06-27 14:00:10 +0200
  * [MDEV-13187](https://jira.mariadb.org/browse/MDEV-13187) incorrect backslash parsing in clients
* [Revision #39385ff7b2](https://github.com/MariaDB/server/commit/39385ff7b2)\
  2017-06-27 13:25:50 +0200
  * [MDEV-13187](https://jira.mariadb.org/browse/MDEV-13187) incorrect backslash parsing in clients
* [Revision #ded614d7db](https://github.com/MariaDB/server/commit/ded614d7db)\
  2017-06-14 13:44:31 +0200
  * [MDEV-12778](https://jira.mariadb.org/browse/MDEV-12778) mariadb-10.1 FTBFS on GNU/Hurd due to use of PATH\_MAX
* [Revision #48429359d6](https://github.com/MariaDB/server/commit/48429359d6)\
  2017-06-16 11:34:59 +0200
  * [MDEV-4646](https://jira.mariadb.org/browse/MDEV-4646) No mysqld-debug or debuginfo in MariaDB-Server RPM
* [Revision #e548e2184b](https://github.com/MariaDB/server/commit/e548e2184b)\
  2017-03-26 16:00:35 +1100
  * Use CPACK\_RPM\_FILE\_NAME="RPM-DEFAULT"
* [Revision #c7141fa75d](https://github.com/MariaDB/server/commit/c7141fa75d)\
  2017-06-15 14:41:59 +0200
  * [MDEV-13002](https://jira.mariadb.org/browse/MDEV-13002) mysqltest regex replace results in incorrect result
* [Revision #c661b4d0fb](https://github.com/MariaDB/server/commit/c661b4d0fb)\
  2017-06-14 00:48:34 +0200
  * [MDEV-13017](https://jira.mariadb.org/browse/MDEV-13017) LOCK TABLE fails with irrelevant error while working with tables affected by ANSI\_QUOTES
* [Revision #5cbbfe9f54](https://github.com/MariaDB/server/commit/5cbbfe9f54)\
  2017-06-14 00:33:11 +0200
  * cleanup: remove duplicate code
* [Revision #918e47030b](https://github.com/MariaDB/server/commit/918e47030b)\
  2017-06-14 11:30:32 +0200
  * [MDEV-13063](https://jira.mariadb.org/browse/MDEV-13063) Server crashes in intern\_plugin\_lock or assertion \`plugin\_ptr->ref\_count == 1' fails in plugin\_init
* [Revision #70b94c35d7](https://github.com/MariaDB/server/commit/70b94c35d7)\
  2017-06-14 11:27:36 +0200
  * cleanup: move common test into a function
* [Revision #b850fc66ca](https://github.com/MariaDB/server/commit/b850fc66ca)\
  2017-06-07 22:54:57 -0700
  * Fixed the bug [MDEV-12855](https://jira.mariadb.org/browse/MDEV-12855).
* [Revision #151f4e9b4a](https://github.com/MariaDB/server/commit/151f4e9b4a)\
  2017-06-07 16:29:55 -0700
  * Fixed the bug [MDEV-12963](https://jira.mariadb.org/browse/MDEV-12963).
* [Revision #c258ca2463](https://github.com/MariaDB/server/commit/c258ca2463)\
  2017-06-07 12:45:09 -0700
  * Fixed the bug [MDEV-12838](https://jira.mariadb.org/browse/MDEV-12838).
* [Revision #2cb94aa1b7](https://github.com/MariaDB/server/commit/2cb94aa1b7)\
  2017-05-29 13:07:23 +0300
  * [MDEV-11626](https://jira.mariadb.org/browse/MDEV-11626) innodb.innodb-change-buffer-recovery fails for xtradb
* [Revision #b8405c853f](https://github.com/MariaDB/server/commit/b8405c853f)\
  2017-05-22 07:09:49 +0200
  * [MDEV-11958](https://jira.mariadb.org/browse/MDEV-11958): LEFT JOIN with stored routine produces incorrect result
* [Revision #7d57ba6e28](https://github.com/MariaDB/server/commit/7d57ba6e28)\
  2017-05-19 13:02:45 +0530
  * [MDEV-11092](https://jira.mariadb.org/browse/MDEV-11092) :- Fix Previous commit of [MDEV-11092](https://jira.mariadb.org/browse/MDEV-11092)
* [Revision #4a846e018d](https://github.com/MariaDB/server/commit/4a846e018d)\
  2017-05-18 19:31:44 +0200
  * Make IF clear.
* [Revision #b5cdf01404](https://github.com/MariaDB/server/commit/b5cdf01404)\
  2017-05-18 17:13:37 +0530
  * [MDEV-11092](https://jira.mariadb.org/browse/MDEV-11092) Assertion \`!writer.checksum\_len || writer.remains == 0' failed
* [Revision #efb9f2617b](https://github.com/MariaDB/server/commit/efb9f2617b)\
  2017-05-17 16:16:54 -0700
  * Fixed the bug [MDEV-12812](https://jira.mariadb.org/browse/MDEV-12812).
* [Revision #7e97163102](https://github.com/MariaDB/server/commit/7e97163102)\
  2017-05-17 14:29:13 -0700
  * Fixed the bug [MDEV-12817](https://jira.mariadb.org/browse/MDEV-12817)/[MDEV-12820](https://jira.mariadb.org/browse/MDEV-12820).
* [Revision #934b831281](https://github.com/MariaDB/server/commit/934b831281)\
  2017-05-16 08:24:42 -0700
  * Fixed the bug [MDEV-7791](https://jira.mariadb.org/browse/MDEV-7791).
* [Revision #2e1428c0b5](https://github.com/MariaDB/server/commit/2e1428c0b5)\
  2017-05-15 13:33:59 +0200
  * [MDEV-12799](https://jira.mariadb.org/browse/MDEV-12799) Buffer overflow
* [Revision #e0352fb079](https://github.com/MariaDB/server/commit/e0352fb079)\
  2017-05-15 09:51:01 -0700
  * Fixed the bug [MDEV-7599](https://jira.mariadb.org/browse/MDEV-7599).
* [Revision #9495e018fb](https://github.com/MariaDB/server/commit/9495e018fb)\
  2017-05-12 11:09:27 +0530
  * [MDEV-11718](https://jira.mariadb.org/browse/MDEV-11718) Post-fix
* [Revision #6b97fe067d](https://github.com/MariaDB/server/commit/6b97fe067d)\
  2017-05-09 00:41:45 -0700
  * Fixed the bugs [MDEV-12670](https://jira.mariadb.org/browse/MDEV-12670) and [MDEV-12675](https://jira.mariadb.org/browse/MDEV-12675).
* [Revision #15f9931f6d](https://github.com/MariaDB/server/commit/15f9931f6d)\
  2017-05-04 22:45:32 -0700
  * Fixed the bug [MDEV-12673](https://jira.mariadb.org/browse/MDEV-12673).
* [Revision #14fca28ea4](https://github.com/MariaDB/server/commit/14fca28ea4)\
  2017-05-02 19:11:21 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
