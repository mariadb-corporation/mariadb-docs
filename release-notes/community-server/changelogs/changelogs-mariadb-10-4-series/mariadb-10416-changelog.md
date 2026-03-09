# MariaDB 10.4.16 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.16](https://downloads.mariadb.org/mariadb/10.4.16/)[Release Notes](../../old-releases/10.4/10.4.16.md)[Changelog](mariadb-10416-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 3 Nov 2020

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.16.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.26](../changelogs-mariadb-10-3-series/mariadb-10326-changelog.md)
* [Revision #1f18e0c70e](https://github.com/MariaDB/server/commit/1f18e0c70e)\
  2020-11-02 01:29:52 +0200
  * List of unstable tests for 10.4.16 release
* Merge [Revision #80c951ce28](https://github.com/MariaDB/server/commit/80c951ce28) 2020-10-31 21:06:49 +0100 - Merge branch '10.3' into 10.4
* [Revision #1fddccf676](https://github.com/MariaDB/server/commit/1fddccf676)\
  2020-10-30 13:26:58 +0200
  * Update Connector/C
* [Revision #5b3be9e1c6](https://github.com/MariaDB/server/commit/5b3be9e1c6)\
  2020-10-30 13:18:41 +0200
  * Try to stabilize main.innodb\_ext\_key,off
* [Revision #cb253b8687](https://github.com/MariaDB/server/commit/cb253b8687)\
  2020-10-30 13:07:42 +0200
  * [MDEV-22387](https://jira.mariadb.org/browse/MDEV-22387): Static\_binary\_string::q\_append() invokes memcpy on NULL
* [Revision #199863d72b](https://github.com/MariaDB/server/commit/199863d72b)\
  2020-10-30 11:04:16 +0200
  * [MDEV-23991](https://jira.mariadb.org/browse/MDEV-23991) fixup: Initialize the memory
* [Revision #9936235985](https://github.com/MariaDB/server/commit/9936235985)\
  2020-10-30 08:54:05 +0200
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659): Update Galera disabled.def file
* [Revision #5485671474](https://github.com/MariaDB/server/commit/5485671474)\
  2020-10-30 08:52:10 +0200
  * Remove test that does not apply for 10.4.
* [Revision #eb38e7ef60](https://github.com/MariaDB/server/commit/eb38e7ef60)\
  2020-10-29 17:06:56 +0200
  * [MDEV-22879](https://jira.mariadb.org/browse/MDEV-22879) SIGSEGV (or hang) in free/my\_free
* [Revision #85613a3247](https://github.com/MariaDB/server/commit/85613a3247)\
  2020-10-29 16:27:04 +0200
  * After-merge fix: main,innodb\_ext\_key,off
* Merge [Revision #7b2bb67113](https://github.com/MariaDB/server/commit/7b2bb67113) 2020-10-29 13:38:38 +0200 - Merge 10.3 into 10.4
* [Revision #27b762e23d](https://github.com/MariaDB/server/commit/27b762e23d)\
  2020-10-29 12:14:19 +0300
  * [MDEV-22805](https://jira.mariadb.org/browse/MDEV-22805) SIGSEGV in check\_fields on UPDATE
* [Revision #e451145aa9](https://github.com/MariaDB/server/commit/e451145aa9)\
  2020-10-28 14:24:10 +0100
  * [MDEV-24040](https://jira.mariadb.org/browse/MDEV-24040) Named pipe permission issue
* [Revision #ec0e9d6f76](https://github.com/MariaDB/server/commit/ec0e9d6f76)\
  2020-10-25 11:17:27 +0200
  * [MDEV-22681](https://jira.mariadb.org/browse/MDEV-22681) EXECUTE IMMEDIATE crashes server if wsrep is on.
* [Revision #46c273892e](https://github.com/MariaDB/server/commit/46c273892e)\
  2020-10-08 13:15:18 +0200
  * [MDEV-23623](https://jira.mariadb.org/browse/MDEV-23623) - Fix assertion in MTR test galera\_sr.GCF-1051
* [Revision #97b10b7fdc](https://github.com/MariaDB/server/commit/97b10b7fdc)\
  2020-10-27 18:55:22 +0700
  * [MDEV-22805](https://jira.mariadb.org/browse/MDEV-22805): SIGSEGV in check\_fields on UPDATE
* [Revision #31cde275c2](https://github.com/MariaDB/server/commit/31cde275c2)\
  2020-10-20 20:10:40 +0300
  * [MDEV-23356](https://jira.mariadb.org/browse/MDEV-23356) InnoDB: Failing assertion: field->col->mtype == type, crash or ASAN failures in row\_sel\_convert\_mysql\_key\_to\_innobase, InnoDB indexes are inconsistent after INDEX changes
* [Revision #045671d473](https://github.com/MariaDB/server/commit/045671d473)\
  2020-10-24 17:58:19 +1100
  * [MDEV-23539](https://jira.mariadb.org/browse/MDEV-23539): aws key plugin - fails to build
* [Revision #c4f8ccc0f5](https://github.com/MariaDB/server/commit/c4f8ccc0f5)\
  2020-09-18 15:34:24 +0200
  * [MDEV-21954](https://jira.mariadb.org/browse/MDEV-21954) mysqld got signal 11 Fatal signal 6 while backtracing on parallel show global status
* [Revision #54c521ca33](https://github.com/MariaDB/server/commit/54c521ca33)\
  2020-10-22 16:49:57 +0300
  * [MDEV-23672](https://jira.mariadb.org/browse/MDEV-23672): incorrect v\_indexes access fix
* [Revision #9868253b32](https://github.com/MariaDB/server/commit/9868253b32)\
  2020-10-22 13:52:45 +0300
  * [MDEV-23576](https://jira.mariadb.org/browse/MDEV-23576): Disable galera\_3nodes.galera\_ipv6\_mysqldump
* [Revision #45e10d46d8](https://github.com/MariaDB/server/commit/45e10d46d8)\
  2020-10-22 13:50:06 +0300
  * After-merge fix to wsrep.variables
* Merge [Revision #46957a6a77](https://github.com/MariaDB/server/commit/46957a6a77) 2020-10-22 13:27:18 +0300 - Merge 10.3 into 10.4
* [Revision #1619ae8990](https://github.com/MariaDB/server/commit/1619ae8990)\
  2020-10-22 13:19:18 +0300
  * [MDEV-23672](https://jira.mariadb.org/browse/MDEV-23672): Partly revert an incorrect fix
* [Revision #77c00799e5](https://github.com/MariaDB/server/commit/77c00799e5)\
  2020-10-22 10:14:17 +0700
  * [MDEV-23935](https://jira.mariadb.org/browse/MDEV-23935): Fix warnings generated during compilation of plugin/auth\_pam/testing/pam\_mariadb\_mtr.c on MacOS
* [Revision #709ba7dcae](https://github.com/MariaDB/server/commit/709ba7dcae)\
  2020-10-21 23:34:36 +0300
  * [MDEV-20945](https://jira.mariadb.org/browse/MDEV-20945): BACKUP UNLOCK + FTWRL assertion failure
* [Revision #ac8d205795](https://github.com/MariaDB/server/commit/ac8d205795)\
  2020-04-16 00:44:20 +0900
  * [MDEV-20100](https://jira.mariadb.org/browse/MDEV-20100) [MariaDB 10.3.9](../../old-releases/10.3/10.3.9.md) Crash "\[ERROR] mysqld got signal 11 ;"
* [Revision #fdf87973cb](https://github.com/MariaDB/server/commit/fdf87973cb)\
  2020-10-15 09:24:01 +0200
  * [MDEV-23081](https://jira.mariadb.org/browse/MDEV-23081) Stray XA transactions at startup, with wsrep\_on=OFF
* [Revision #7eda556196](https://github.com/MariaDB/server/commit/7eda556196)\
  2020-10-20 10:57:57 +0300
  * [MDEV-23672](https://jira.mariadb.org/browse/MDEV-23672) Assertion \`v.v\_indexes.empty()' failed in dict\_table\_t::instant\_column
* [Revision #a6f956488c](https://github.com/MariaDB/server/commit/a6f956488c)\
  2020-10-10 08:28:53 +1100
  * [MDEV-22761](https://jira.mariadb.org/browse/MDEV-22761): innodb row\_search\_idx\_cond\_check handle CHECK\_ABORTED\_BY\_USER
* [Revision #c03885cd9c](https://github.com/MariaDB/server/commit/c03885cd9c)\
  2020-10-09 17:48:22 +0300
  * [MDEV-22761](https://jira.mariadb.org/browse/MDEV-22761): innodb row\_search\_idx\_cond\_check handle CHECK\_ABORTED\_BY\_USER
* [Revision #171da6b38b](https://github.com/MariaDB/server/commit/171da6b38b)\
  2020-09-30 10:22:58 +1000
  * [MDEV-22761](https://jira.mariadb.org/browse/MDEV-22761): innodb row\_search\_idx\_cond\_check handle CHECK\_ABORTED\_BY\_USER
* [Revision #5896a49820](https://github.com/MariaDB/server/commit/5896a49820)\
  2019-10-09 16:48:50 +1000
  * [MDEV-19130](https://jira.mariadb.org/browse/MDEV-19130) Assertion failed in handler::update\_auto\_increment
* Merge [Revision #c2ac0ce1f0](https://github.com/MariaDB/server/commit/c2ac0ce1f0) 2020-10-07 18:51:11 +0200 - Merge tag 'mariadb-10.4.15' into 10.4
* [Revision #232715f506](https://github.com/MariaDB/server/commit/232715f506)\
  2020-10-07 11:27:00 -0400
  * bump the VERSION
* [Revision #9e100f4b96](https://github.com/MariaDB/server/commit/9e100f4b96)\
  2020-10-07 11:14:20 +0200
  * Better German Error message.
* [Revision #fee807f6d8](https://github.com/MariaDB/server/commit/fee807f6d8)\
  2020-10-07 08:10:36 +0300
  * [MDEV-22148](https://jira.mariadb.org/browse/MDEV-22148) : Assertion \`state\_ == s\_exec || state\_ == s\_quitting' failed in optimized builds | SIGABRT in wsrep::client\_state::disable\_streaming
* [Revision #acb0c9e8fd](https://github.com/MariaDB/server/commit/acb0c9e8fd)\
  2020-08-28 16:05:38 +0200
  * [MDEV-23518](https://jira.mariadb.org/browse/MDEV-23518) Syntax error in ond SP results in misleading message on SHOW CREATE PROCEDURE
* [Revision #bd64c2e8cc](https://github.com/MariaDB/server/commit/bd64c2e8cc)\
  2020-10-01 13:51:31 +0300
  * Cleanup: Remove unnecessary trx\_i\_s\_cache\_t::last\_read\_mutex
* Merge [Revision #9ae608d24d](https://github.com/MariaDB/server/commit/9ae608d24d) 2020-10-01 13:41:36 +0300 - Merge 10.3 into 10.4
* [Revision #79e32e47a1](https://github.com/MariaDB/server/commit/79e32e47a1)\
  2020-09-26 10:07:28 -0700
  * [MDEV-23778](https://jira.mariadb.org/browse/MDEV-23778) Derived table handler looses data on conversion from HEAP to Aria
* Merge [Revision #ce845b7a2f](https://github.com/MariaDB/server/commit/ce845b7a2f) 2020-09-28 17:55:39 +0530 - Merge branch '10.3' into 10.4
* [Revision #7edfb72eff](https://github.com/MariaDB/server/commit/7edfb72eff)\
  2020-09-25 14:08:35 +0200
  * Fix MTR test wsrep.variables
* [Revision #e8b05ce503](https://github.com/MariaDB/server/commit/e8b05ce503)\
  2020-09-08 17:24:08 +0530
  * [MDEV-23675](https://jira.mariadb.org/browse/MDEV-23675) Assertion \`pos < table->n\_def' fails in dict\_table\_get\_nth\_col
* [Revision #6a1376252d](https://github.com/MariaDB/server/commit/6a1376252d)\
  2020-09-25 15:58:08 +0300
  * Reverted wrong patch for mysql\_upgrade
* [Revision #71a7b79bcb](https://github.com/MariaDB/server/commit/71a7b79bcb)\
  2020-09-25 13:38:48 +0300
  * Added asssert to init\_of\_queries() to make it more safe
* [Revision #bb2c958132](https://github.com/MariaDB/server/commit/bb2c958132)\
  2020-09-17 18:54:11 +0300
  * [MDEV-23296](https://jira.mariadb.org/browse/MDEV-23296) Assertion \`block->type == PAGECACHE\_EMPTY\_PAGE.. with aria\_max\_sort\_file\_size=0
* [Revision #92b5a8bb65](https://github.com/MariaDB/server/commit/92b5a8bb65)\
  2020-09-17 17:59:59 +0300
  * [MDEV-17665](https://jira.mariadb.org/browse/MDEV-17665) Assertion \`!share and other errors on concurrent Aria operations
* [Revision #8819b5eea5](https://github.com/MariaDB/server/commit/8819b5eea5)\
  2020-09-17 16:06:16 +0300
  * [MDEV-23318](https://jira.mariadb.org/browse/MDEV-23318) Assertion \`cache\_empty(keycache)' failed in prepare\_resize\_simple\_key\_cache
* [Revision #0b73ef0688](https://github.com/MariaDB/server/commit/0b73ef0688)\
  2020-09-16 18:29:11 +0300
  * [MDEV-21470](https://jira.mariadb.org/browse/MDEV-21470) ASAN heap-use-after-free in my\_hash\_sort\_bin
* [Revision #895e9950b2](https://github.com/MariaDB/server/commit/895e9950b2)\
  2020-09-15 16:13:37 +0300
  * Fix for timeout in rpl.rpl\_parallel\_retry
* [Revision #16ea692ed4](https://github.com/MariaDB/server/commit/16ea692ed4)\
  2020-09-07 10:38:12 +0300
  * [MDEV-23586](https://jira.mariadb.org/browse/MDEV-23586) mariadb-backup: GTID saved for replication in 10.4.14 is wrong
* [Revision #3cdbaa04bd](https://github.com/MariaDB/server/commit/3cdbaa04bd)\
  2020-09-14 21:22:32 +0300
  * Fixed BUILD script to make plugin-file\_key\_management DYNAMIC
* [Revision #920824c24e](https://github.com/MariaDB/server/commit/920824c24e)\
  2020-07-23 11:35:40 +0300
  * Backported setting of transcation.on=1 in THD::reset\_for\_reuse()
* [Revision #a50ce94458](https://github.com/MariaDB/server/commit/a50ce94458)\
  2020-09-02 20:38:25 +0200
  * [MDEV-23559](https://jira.mariadb.org/browse/MDEV-23559): Galera LeakSanitizer: detected memory leaks in galera.[GAL-419](https://github.com/codership/galera/issues/419)
* [Revision #8370a38dc0](https://github.com/MariaDB/server/commit/8370a38dc0)\
  2020-09-23 15:42:11 +0200
  * Window , MTR : fix lookup for mysql\_install\_db.exe
* [Revision #d7c82610c1](https://github.com/MariaDB/server/commit/d7c82610c1)\
  2020-09-23 09:29:05 +0300
  * Fix the WolfSSL build on FreeBSD
* Merge [Revision #61df98f964](https://github.com/MariaDB/server/commit/61df98f964) 2020-09-22 21:29:30 +0300 - Merge 10.3 into 10.4
* Merge [Revision #55e48b7722](https://github.com/MariaDB/server/commit/55e48b7722) 2020-09-22 15:12:59 +0300 - Merge 10.3 into 10.4
* [Revision #98f03e5a22](https://github.com/MariaDB/server/commit/98f03e5a22)\
  2020-09-21 12:14:49 +0300
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659) : Update Galera disabled.def file
* [Revision #98ac2d425e](https://github.com/MariaDB/server/commit/98ac2d425e)\
  2020-09-21 12:05:18 +0300
  * [MDEV-21170](https://jira.mariadb.org/browse/MDEV-21170) : Galera test failure on galera\_sr.GCF-1043\[A|B]
* Merge [Revision #952a028a52](https://github.com/MariaDB/server/commit/952a028a52) 2020-09-21 17:42:02 +0300 - Merge 10.3 into 10.4
* Merge [Revision #3a423088ac](https://github.com/MariaDB/server/commit/3a423088ac) 2020-09-21 12:29:00 +0300 - Merge 10.3 into 10.4
* [Revision #29847a3736](https://github.com/MariaDB/server/commit/29847a3736)\
  2020-09-18 07:32:36 +0300
  * [MDEV-23751](https://jira.mariadb.org/browse/MDEV-23751) : galera\_3nodes test failures on ipv6 sst tests
* [Revision #bfe612b738](https://github.com/MariaDB/server/commit/bfe612b738)\
  2020-09-17 18:05:53 +0200
  * [MDEV-23663](https://jira.mariadb.org/browse/MDEV-23663) - Add HAVE\_INTEL\_RDRAND flag for building WolfSSL, where appropiate
* [Revision #de76bebc57](https://github.com/MariaDB/server/commit/de76bebc57)\
  2020-09-14 18:21:48 +0300
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659) : Update Galera disabled.def file
* [Revision #b69e980a38](https://github.com/MariaDB/server/commit/b69e980a38)\
  2020-09-14 18:21:17 +0300
  * [MDEV-20581](https://jira.mariadb.org/browse/MDEV-20581) Fix MTR test wsrep.variables
* [Revision #7730b7bace](https://github.com/MariaDB/server/commit/7730b7bace)\
  2020-09-14 08:21:53 +0300
  * [MDEV-23617](https://jira.mariadb.org/browse/MDEV-23617) : galera\_sr.galera\_sr\_rollback\_retry MTR failed: 1213: Deadlock found when trying to get lock
* [Revision #af834c218a](https://github.com/MariaDB/server/commit/af834c218a)\
  2020-09-11 16:37:13 +0530
  * [MDEV-23199](https://jira.mariadb.org/browse/MDEV-23199) page\_compression flag is missing for full\_crc32 tablespace
* [Revision #8993e40dde](https://github.com/MariaDB/server/commit/8993e40dde)\
  2020-09-10 13:25:57 +0300
  * [MDEV-23709](https://jira.mariadb.org/browse/MDEV-23709) : Galera test failure on galera\_fk\_cascade\_delete\_debug
* [Revision #f19da4a05a](https://github.com/MariaDB/server/commit/f19da4a05a)\
  2020-09-07 14:23:05 +0530
  * [MDEV-23199](https://jira.mariadb.org/browse/MDEV-23199) page\_compression flag is missing for full\_crc32 tablespace
* [Revision #1bb3ad6dfc](https://github.com/MariaDB/server/commit/1bb3ad6dfc)\
  2020-08-27 17:30:03 +0200
  * [MDEV-23589](https://jira.mariadb.org/browse/MDEV-23589): Portability: use `uname -n` instead of `hostname`
* [Revision #cf9b3b25b4](https://github.com/MariaDB/server/commit/cf9b3b25b4)\
  2020-09-09 13:05:19 +0300
  * [MDEV-23608](https://jira.mariadb.org/browse/MDEV-23608) : galera\_sr.GCF-597 MTR failed: query 'ROLLBACK' succeeded - should have failed with errno 1213
* [Revision #44e7e1f0d3](https://github.com/MariaDB/server/commit/44e7e1f0d3)\
  2020-09-09 11:41:42 +0300
  * [MDEV-23611](https://jira.mariadb.org/browse/MDEV-23611) : galera\_sr.galera\_sr\_kill\_query MTR failed: 15 instead of 0 on "SELECT COUNT(\*) AS EXPECT\_0 FROM mysql.wsrep\_streaming\_log;"
* [Revision #90bea7c32c](https://github.com/MariaDB/server/commit/90bea7c32c)\
  2020-09-09 11:00:04 +0300
  * [MDEV-23613](https://jira.mariadb.org/browse/MDEV-23613) : galera\_sr.galera\_sr\_kill\_slave MTR failed: query 'LOCK TABLE t2 WRITE' failed: 1146: Table 'test.t2' doesn't exist
* Merge [Revision #66ae50a564](https://github.com/MariaDB/server/commit/66ae50a564) 2020-09-09 15:00:21 +0300 - Merge 10.3 into 10.4
* [Revision #9b68847127](https://github.com/MariaDB/server/commit/9b68847127)\
  2020-09-04 22:10:57 +0900
  * [MDEV-7098](https://jira.mariadb.org/browse/MDEV-7098) spider/bg.spider\_fixes failed in buildbot with safe\_mutex: Trying to unlock mutex conn->mta\_conn\_mutex that wasn't locked at storage/spider/spd\_db\_conn.cc, line 671
* Merge [Revision #7f8cd326c6](https://github.com/MariaDB/server/commit/7f8cd326c6) 2020-09-04 12:39:09 +0300 - Merge 10.3 into 10.4
* [Revision #b0c194cab4](https://github.com/MariaDB/server/commit/b0c194cab4)\
  2020-09-04 11:40:17 +0300
  * [MDEV-23633](https://jira.mariadb.org/browse/MDEV-23633) fixup: Add missing semicolon
* [Revision #24f510bba4](https://github.com/MariaDB/server/commit/24f510bba4)\
  2020-09-04 10:31:41 +0300
  * [MDEV-23633](https://jira.mariadb.org/browse/MDEV-23633) MY\_RELAX\_CPU performs unnecessary compare-and-swap on ARM
* Merge [Revision #1cda462f46](https://github.com/MariaDB/server/commit/1cda462f46) 2020-09-03 16:55:14 +0300 - Merge 10.3 into 10.4
* Merge [Revision #c9cf6b13f6](https://github.com/MariaDB/server/commit/c9cf6b13f6) 2020-09-03 15:53:38 +0300 - Merge 10.3 into 10.4
* [Revision #b795adcff7](https://github.com/MariaDB/server/commit/b795adcff7)\
  2020-09-03 15:37:04 +0300
  * Make rowid\_filter\_innodb test stable
* [Revision #0f080dd60a](https://github.com/MariaDB/server/commit/0f080dd60a)\
  2020-08-11 16:37:48 +0200
  * [MDEV-23094](https://jira.mariadb.org/browse/MDEV-23094): Multiple calls to a Stored Procedure from another Stored Procedure crashes server
* [Revision #571764c04f](https://github.com/MariaDB/server/commit/571764c04f)\
  2020-08-26 13:32:15 +0300
  * [MDEV-23584](https://jira.mariadb.org/browse/MDEV-23584) : Galera assertion failure "thd->transaction.stmt.is\_empty() at transaction.cc:69
* Merge [Revision #1e08e08ccb](https://github.com/MariaDB/server/commit/1e08e08ccb) 2020-08-26 11:30:20 +0300 - Merge 10.3 into 10.4
* [Revision #88e70f4cae](https://github.com/MariaDB/server/commit/88e70f4cae)\
  2020-08-24 16:50:53 +0300
  * [MDEV-23558](https://jira.mariadb.org/browse/MDEV-23558): Galera heap-buffer-overflow at wsrep\_schema.cc:1067
* [Revision #a16f4927db](https://github.com/MariaDB/server/commit/a16f4927db)\
  2020-08-24 14:09:40 +0300
  * [MDEV-22055](https://jira.mariadb.org/browse/MDEV-22055): Assertion \`active() == false' failed in wsrep::transaction::start\_transaction upon ROLLBACK AND CHAIN
* [Revision #2000d05c2e](https://github.com/MariaDB/server/commit/2000d05c2e)\
  2020-08-23 12:30:14 +0900
  * [MDEV-22246](https://jira.mariadb.org/browse/MDEV-22246) Result rows duplicated by spider engine
* [Revision #329301d2e6](https://github.com/MariaDB/server/commit/329301d2e6)\
  2020-08-24 22:55:39 +0400
  * [MDEV-23562](https://jira.mariadb.org/browse/MDEV-23562) Assertion \`time\_type == MYSQL\_TIMESTAMP\_DATETIME' failed upon SELECT from versioned table
* [Revision #056766c042](https://github.com/MariaDB/server/commit/056766c042)\
  2020-08-24 14:27:32 +0400
  * The patch for [MDEV-23551](https://jira.mariadb.org/browse/MDEV-23551) did not compile on some compilers. Fixing.
* [Revision #04ce29354b](https://github.com/MariaDB/server/commit/04ce29354b)\
  2020-08-24 09:17:47 +0400
  * [MDEV-23551](https://jira.mariadb.org/browse/MDEV-23551) Performance degratation in temporal literals in 10.4
* [Revision #2e5d86f49e](https://github.com/MariaDB/server/commit/2e5d86f49e)\
  2020-08-22 15:22:20 +0400
  * [MDEV-23537](https://jira.mariadb.org/browse/MDEV-23537) Comparison with temporal columns is slow in MariaDB
* [Revision #ae33ebe5b3](https://github.com/MariaDB/server/commit/ae33ebe5b3)\
  2020-08-21 19:41:51 +0400
  * [MDEV-23525](https://jira.mariadb.org/browse/MDEV-23525) Wrong result of MIN(time\_expr) and MAX(time\_expr) with GROUP BY
* Merge [Revision #aa6cb7ed03](https://github.com/MariaDB/server/commit/aa6cb7ed03) 2020-08-21 19:57:22 +0300 - Merge 10.3 into 10.4
* [Revision #688fb6301c](https://github.com/MariaDB/server/commit/688fb6301c)\
  2020-08-21 10:37:52 +0300
  * [MDEV-23526](https://jira.mariadb.org/browse/MDEV-23526) InnoDB leaks memory for some static objects
* Merge [Revision #2643249da5](https://github.com/MariaDB/server/commit/2643249da5) 2020-08-21 10:19:44 +0300 - Merge 10.3 into 10.4
* Merge [Revision #2fa9f8c53a](https://github.com/MariaDB/server/commit/2fa9f8c53a) 2020-08-20 11:01:47 +0300 - Merge 10.3 into 10.4
* [Revision #f8bf5b0f84](https://github.com/MariaDB/server/commit/f8bf5b0f84)\
  2020-08-18 11:03:12 +0200
  * [MDEV-23466](https://jira.mariadb.org/browse/MDEV-23466) SIGABRT on SELECT WSREP\_LAST\_SEEN\_GTID
* [Revision #fe3284b2cc](https://github.com/MariaDB/server/commit/fe3284b2cc)\
  2020-08-18 10:56:56 +0200
  * [MDEV-23092](https://jira.mariadb.org/browse/MDEV-23092) SIGABRT when setting invalid wsrep\_provider
* [Revision #09dd06f14a](https://github.com/MariaDB/server/commit/09dd06f14a)\
  2020-08-18 10:47:15 +0200
  * [MDEV-22443](https://jira.mariadb.org/browse/MDEV-22443) wsrep::runtime\_error on START TRANSACTION
* [Revision #8a6a084578](https://github.com/MariaDB/server/commit/8a6a084578)\
  2020-08-18 16:50:28 +0200
  * Re-record MTR tests galera\_3nodes.galera\_join\_with\_cc\_{A|B|C}
* [Revision #064bfbaf06](https://github.com/MariaDB/server/commit/064bfbaf06)\
  2020-08-18 15:14:12 +0300
  * [MDEV-23499](https://jira.mariadb.org/browse/MDEV-23499) Assertion c.same\_type(\*o) failed
* [Revision #5c8a1249dd](https://github.com/MariaDB/server/commit/5c8a1249dd)\
  2020-08-17 09:45:03 +0900
  * [MDEV-20827](https://jira.mariadb.org/browse/MDEV-20827) Wrong param parsing in spider\_direct\_sql() when param contain comma
* [Revision #010fd61a5f](https://github.com/MariaDB/server/commit/010fd61a5f)\
  2020-08-15 17:55:01 +0200
  * [MDEV-23489](https://jira.mariadb.org/browse/MDEV-23489) Windows zip files 10.4.14 have an embryonic data folder
* [Revision #303212d4b6](https://github.com/MariaDB/server/commit/303212d4b6)\
  2020-08-13 05:36:23 +0900
  * [MDEV-19794](https://jira.mariadb.org/browse/MDEV-19794) Spider crash with XA
* [Revision #7df4706619](https://github.com/MariaDB/server/commit/7df4706619)\
  2020-08-14 13:34:19 +0300
  * Fix Windows compiler error.
* [Revision #a7a9f44f8c](https://github.com/MariaDB/server/commit/a7a9f44f8c)\
  2020-08-10 11:44:42 +0300
  * [MDEV-22543](https://jira.mariadb.org/browse/MDEV-22543) : Galera SST donation fails, FLUSH TABLES WITH READ LOCK times out
* Merge [Revision #2f7b37b021](https://github.com/MariaDB/server/commit/2f7b37b021) 2020-08-13 18:48:41 +0300 - Merge 10.3 into 10.4, except [MDEV-22543](https://jira.mariadb.org/browse/MDEV-22543)
* [Revision #7f03b1d78f](https://github.com/MariaDB/server/commit/7f03b1d78f)\
  2020-08-11 16:23:10 +0300
  * Fix test galera\_ist\_progress in 10.4
* Merge [Revision #c86114f594](https://github.com/MariaDB/server/commit/c86114f594) 2020-08-11 10:53:28 +0300 - Merge 10.3 into 10.4
* [Revision #909d362fdb](https://github.com/MariaDB/server/commit/909d362fdb)\
  2020-08-11 10:38:49 +0300
  * After-merge fix of a result
* Merge [Revision #eae968f62d](https://github.com/MariaDB/server/commit/eae968f62d) 2020-08-10 21:08:46 +0300 - Merge 10.3 into 10.4
* Merge [Revision #101ddc5e27](https://github.com/MariaDB/server/commit/101ddc5e27) 2020-08-10 20:37:52 +0300 - Merge mariadb-10.4.14
* [Revision #2b9c53102c](https://github.com/MariaDB/server/commit/2b9c53102c)\
  2020-08-10 10:32:57 -0400
  * bump the VERSION
* [Revision #fe555b9c5f](https://github.com/MariaDB/server/commit/fe555b9c5f)\
  2020-08-08 09:44:31 +0400
  * [MDEV-23415](https://jira.mariadb.org/browse/MDEV-23415) Server crash or Assertion \`dec\_length <= str\_length' failed in Item\_func\_format::val\_str\_ascii
* [Revision #0041dacc1b](https://github.com/MariaDB/server/commit/0041dacc1b)\
  2020-08-05 08:56:12 +0400
  * [MDEV-23118](https://jira.mariadb.org/browse/MDEV-23118) FORMAT(d1,dec) where dec=0/38 and d1 is DECIMAL(38,38) gives incorrect results
* [Revision #14a5f73cda](https://github.com/MariaDB/server/commit/14a5f73cda)\
  2020-08-04 14:15:06 +0300
  * Add wait conditions for cluster size.
* [Revision #100f0c965c](https://github.com/MariaDB/server/commit/100f0c965c)\
  2020-08-04 08:31:03 +0400
  * [MDEV-23388](https://jira.mariadb.org/browse/MDEV-23388) Assertion \`args\[0]->decimals == 0' failed in Item\_func\_round::fix\_arg\_int
* [Revision #6a2ee9c8bb](https://github.com/MariaDB/server/commit/6a2ee9c8bb)\
  2020-08-03 13:56:10 +0400
  * [MDEV-23032](https://jira.mariadb.org/browse/MDEV-23032) FLOOR()/CEIL() incorrectly calculate the precision of a DECIMAL(M,D) column

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
