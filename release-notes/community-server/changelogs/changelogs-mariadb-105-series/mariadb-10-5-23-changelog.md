# MariaDB 10.5.23 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.23](https://downloads.mariadb.org/mariadb/10.5.23/)[Release Notes](../../old-releases/10.5/10.5.23.md)[Changelog](mariadb-10-5-23-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 13 Nov 2023

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.23.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.32](../changelogs-mariadb-10-4-series/mariadb-10-4-32-changelog.md)
* Merge [Revision #6cfd2ba397](https://github.com/MariaDB/server/commit/6cfd2ba397) 2023-11-08 12:59:00 +0100 - Merge branch '10.4' into 10.5
* [Revision #a44869d842](https://github.com/MariaDB/server/commit/a44869d842)\
  2023-11-07 10:55:55 +0530
  * [MDEV-31851](https://jira.mariadb.org/browse/MDEV-31851) Doublewrite recovery fixup
* [Revision #b5e43a1d35](https://github.com/MariaDB/server/commit/b5e43a1d35)\
  2023-10-23 16:13:16 +0300
  * [MDEV-32552](https://jira.mariadb.org/browse/MDEV-32552) Write-ahead logging is broken for freed pages
* [Revision #85751ed81d](https://github.com/MariaDB/server/commit/85751ed81d)\
  2023-10-19 15:39:44 +0530
  * [MDEV-31851](https://jira.mariadb.org/browse/MDEV-31851) After crash recovery, undo tablespace fails to open
* [Revision #dbba1bb1c3](https://github.com/MariaDB/server/commit/dbba1bb1c3)\
  2023-10-19 13:11:20 +0530
  * [MDEV-31851](https://jira.mariadb.org/browse/MDEV-31851) After crash recovery, undo tablespace fails to open
* [Revision #2d6dc65de5](https://github.com/MariaDB/server/commit/2d6dc65de5)\
  2023-10-19 08:24:37 +0300
  * [MDEV-32144](https://jira.mariadb.org/browse/MDEV-32144) fixup
* [Revision #cfd1788182](https://github.com/MariaDB/server/commit/cfd1788182)\
  2023-10-18 16:51:04 +0300
  * [MDEV-32511](https://jira.mariadb.org/browse/MDEV-32511): Race condition between checkpoint and page write
* [Revision #3da5d047b8](https://github.com/MariaDB/server/commit/3da5d047b8)\
  2023-10-17 18:37:45 +0530
  * [MDEV-31851](https://jira.mariadb.org/browse/MDEV-31851) After crash recovery, undo tablespace fails to open
* [Revision #ea0b1ccd41](https://github.com/MariaDB/server/commit/ea0b1ccd41)\
  2023-10-07 10:49:36 +0200
  * Revert "[MDEV-29091](https://jira.mariadb.org/browse/MDEV-29091): Correct event\_name in PFS for wait caused by FOR UPDATE"
* [Revision #c378efeeb9](https://github.com/MariaDB/server/commit/c378efeeb9)\
  2023-10-13 13:33:36 +0200
  * make perfschema.show\_aggregate test more reliable
* [Revision #e3e66a575b](https://github.com/MariaDB/server/commit/e3e66a575b)\
  2023-10-07 10:28:05 +0200
  * make perfschema.show\_aggregate test more debuggable
* [Revision #fbd11d5f29](https://github.com/MariaDB/server/commit/fbd11d5f29)\
  2023-10-13 09:12:01 +1100
  * [MDEV-18200](https://jira.mariadb.org/browse/MDEV-18200) mariadb-backup full backup failed with InnoDB: Failing assertion: success
* [Revision #c79ca7c7ad](https://github.com/MariaDB/server/commit/c79ca7c7ad)\
  2023-09-19 11:33:51 +1000
  * [MDEV-18200](https://jira.mariadb.org/browse/MDEV-18200) mariadb-backup full backup failed with InnoDB: Failing assertion: success
* [Revision #f9d471e2d5](https://github.com/MariaDB/server/commit/f9d471e2d5)\
  2023-10-12 09:48:54 +0300
  * Cleanup: Remove innobase\_init\_vc\_templ()
* [Revision #b04af64882](https://github.com/MariaDB/server/commit/b04af64882)\
  2023-10-08 22:36:16 +0300
  * Fixed that log\_slow.test works with view\_protocol
* [Revision #1dd6d9a0bf](https://github.com/MariaDB/server/commit/1dd6d9a0bf)\
  2023-10-08 20:17:52 +0300
  * Fixed compiler warnings in connect/odbconn.cpp
* [Revision #9d19b65269](https://github.com/MariaDB/server/commit/9d19b65269)\
  2023-10-08 18:04:15 +0300
  * [MDEV-22243](https://jira.mariadb.org/browse/MDEV-22243) type\_test.type\_test\_double fails with 'NUMERIC\_SCALE NULL'
* [Revision #185591c1c0](https://github.com/MariaDB/server/commit/185591c1c0)\
  2023-10-08 18:00:51 +0300
  * [MDEV-31349](https://jira.mariadb.org/browse/MDEV-31349) test maria.maria-purge failed on 'aria\_log.00000002 not found'
* [Revision #424a7a2620](https://github.com/MariaDB/server/commit/424a7a2620)\
  2023-10-06 18:18:37 +0300
  * Fixed randomly failing test main.order\_by\_optimizer\_innodb
* [Revision #6e9b421f77](https://github.com/MariaDB/server/commit/6e9b421f77)\
  2023-10-06 14:16:01 +0300
  * [MDEV-32364](https://jira.mariadb.org/browse/MDEV-32364) Server crashes when starting server with high innodb\_log\_buffer\_size
* [Revision #0e0a19b9f6](https://github.com/MariaDB/server/commit/0e0a19b9f6)\
  2023-10-06 12:58:52 +0300
  * [MDEV-32361](https://jira.mariadb.org/browse/MDEV-32361) mariadb-backup --move-back leaves out ib\_logfile0
* Merge [Revision #6b343de8ef](https://github.com/MariaDB/server/commit/6b343de8ef) 2023-09-25 13:06:57 +1000 - Merge branch '10.4' into 10.5
* [Revision #95730372bd](https://github.com/MariaDB/server/commit/95730372bd)\
  2023-09-20 21:15:42 +0300
  * [MDEV-30165](https://jira.mariadb.org/browse/MDEV-30165) X-lock on supremum for prepared transaction for RR
* [Revision #8513f8f1c9](https://github.com/MariaDB/server/commit/8513f8f1c9)\
  2023-09-20 08:31:28 +0300
  * Give a reason for disabling a test
* [Revision #2ed54611c7](https://github.com/MariaDB/server/commit/2ed54611c7)\
  2023-09-19 22:23:59 +0300
  * Disabled gcol.innodb\_virtual\_fk
* [Revision #5c9d8315cc](https://github.com/MariaDB/server/commit/5c9d8315cc)\
  2023-09-19 15:57:47 +0300
  * Fixed random failuring test main.innodb\_ext\_key
* [Revision #8a3a88a758](https://github.com/MariaDB/server/commit/8a3a88a758)\
  2023-09-19 15:01:28 +0300
  * Fixed compiler failure in lib\_sql.cc
* [Revision #821d691a20](https://github.com/MariaDB/server/commit/821d691a20)\
  2023-09-19 14:16:11 +0300
  * Correction of receent PR in mroonga for 10.5
* [Revision #d58f43f8b4](https://github.com/MariaDB/server/commit/d58f43f8b4)\
  2023-09-19 18:02:56 +0300
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174) fixup: Remove unused ut\_bit\_set\_nth()
* Merge [Revision #6c05edfdcd](https://github.com/MariaDB/server/commit/6c05edfdcd) 2023-09-19 10:20:09 +0300 - Merge 10.4 into 10.5
* [Revision #7bef86ea74](https://github.com/MariaDB/server/commit/7bef86ea74)\
  2023-08-11 11:55:27 +0700
  * [MDEV-31460](https://jira.mariadb.org/browse/MDEV-31460): main.order\_by\_pack\_big fails with view-protocol
* Merge [Revision #cf81626307](https://github.com/MariaDB/server/commit/cf81626307) 2023-09-15 15:21:48 +1000 - Merge branch '10.4' into 10.5
* [Revision #68a002071b](https://github.com/MariaDB/server/commit/68a002071b)\
  2023-09-14 16:12:10 +1000
  * [MDEV-29502](https://jira.mariadb.org/browse/MDEV-29502) Fix some issues with spider direct aggregate
* Merge [Revision #e95e9a221f](https://github.com/MariaDB/server/commit/e95e9a221f) 2023-09-15 12:04:44 +1000 - Merge branch '10.4' into 10.5
* [Revision #81e60f1a0a](https://github.com/MariaDB/server/commit/81e60f1a0a)\
  2023-09-14 15:17:27 +0300
  * [MDEV-32163](https://jira.mariadb.org/browse/MDEV-32163) Crash recovery fails after DROP TABLE in system tablespace
* Merge [Revision #cb1965bd9d](https://github.com/MariaDB/server/commit/cb1965bd9d) 2023-09-14 16:30:11 +1000 - Merge branch '10.4' into 10.5
* [Revision #7de0c7b569](https://github.com/MariaDB/server/commit/7de0c7b569)\
  2023-08-24 10:42:17 -0600
  * [MDEV-31038](https://jira.mariadb.org/browse/MDEV-31038): rpl.rpl\_xa\_prepare\_gtid\_fail clean up
* [Revision #9e9cefde2a](https://github.com/MariaDB/server/commit/9e9cefde2a)\
  2023-09-13 12:10:43 +0200
  * post-merge fix
* [Revision #d20a4da23d](https://github.com/MariaDB/server/commit/d20a4da23d)\
  2023-09-12 15:16:31 +0300
  * [MDEV-32150](https://jira.mariadb.org/browse/MDEV-32150) InnoDB reports corruption on 32-bit platforms with ibd files sizes > 4GB
* [Revision #a3cbc44b24](https://github.com/MariaDB/server/commit/a3cbc44b24)\
  2023-09-12 02:37:30 +0200
  * [MDEV-31833](https://jira.mariadb.org/browse/MDEV-31833) replication breaks when using optimistic replication and replica is a galera node
* [Revision #ef569c324d](https://github.com/MariaDB/server/commit/ef569c324d)\
  2023-09-11 12:32:44 +0300
  * [MDEV-21679](https://jira.mariadb.org/browse/MDEV-21679) fixup for s390x
* [Revision #384eb570a6](https://github.com/MariaDB/server/commit/384eb570a6)\
  2023-09-11 11:48:15 +0300
  * [MDEV-32144](https://jira.mariadb.org/browse/MDEV-32144) Debug assertion failure w == MAYBE\_NOP in mtr\_t::memcpy()
* Merge [Revision #f8f7d9de2c](https://github.com/MariaDB/server/commit/f8f7d9de2c) 2023-09-11 11:29:31 +0300 - Merge 10.4 into 10.5
* [Revision #b08474435f](https://github.com/MariaDB/server/commit/b08474435f)\
  2023-09-04 20:47:38 +0300
  * Fix compression tests for s390x
* Merge [Revision #68a925b325](https://github.com/MariaDB/server/commit/68a925b325) 2023-09-05 12:41:49 +0700 - Merge branch '10.4' into 10.5
* Merge [Revision #59952b2625](https://github.com/MariaDB/server/commit/59952b2625) 2023-09-04 09:40:26 +0300 - Merge 10.4 into 10.5
* [Revision #2db5f1b298](https://github.com/MariaDB/server/commit/2db5f1b298)\
  2023-08-31 12:14:49 +0300
  * [MDEV-32049](https://jira.mariadb.org/browse/MDEV-32049) Deadlock due to log\_free\_check() in trx\_purge\_truncate\_history()
* [Revision #3c86765efe](https://github.com/MariaDB/server/commit/3c86765efe)\
  2023-08-31 12:08:40 +0300
  * [MDEV-23974](https://jira.mariadb.org/browse/MDEV-23974) fixup: Use standard quotes in have\_innodb.inc
* [Revision #53499cd1ea](https://github.com/MariaDB/server/commit/53499cd1ea)\
  2023-08-29 11:51:01 +0400
  * [MDEV-31303](https://jira.mariadb.org/browse/MDEV-31303) Key not used when IN clause has both signed and usigned values
* [Revision #e938d7c18f](https://github.com/MariaDB/server/commit/e938d7c18f)\
  2023-08-28 19:02:23 +0530
  * [MDEV-32028](https://jira.mariadb.org/browse/MDEV-32028) InnoDB scrubbing doesn't write zero while freeing the extent
* Merge [Revision #aeb8eae5c8](https://github.com/MariaDB/server/commit/aeb8eae5c8) 2023-08-24 10:12:13 +0300 - Merge 10.4 into 10.5
* Merge [Revision #0d88365bd8](https://github.com/MariaDB/server/commit/0d88365bd8) 2023-08-23 17:16:47 +1000 - Merge 10.4 into 10.5
* Merge [Revision #f9cc29824b](https://github.com/MariaDB/server/commit/f9cc29824b) 2023-08-22 09:01:34 +0300 - Merge 10.4 into 10.5
* [Revision #be5fd3ec35](https://github.com/MariaDB/server/commit/be5fd3ec35)\
  2023-08-21 13:28:12 +0300
  * Remove a stale comment
* Merge [Revision #5895a3622b](https://github.com/MariaDB/server/commit/5895a3622b) 2023-08-17 10:33:36 +0300 - Merge 10.4 into 10.5
* Merge [Revision #7c9837ce74](https://github.com/MariaDB/server/commit/7c9837ce74) 2023-08-15 17:32:21 +0200 - Merge 10.4 into 10.5
* Merge [Revision #599c4d9a40](https://github.com/MariaDB/server/commit/599c4d9a40) 2023-08-15 11:10:27 +0300 - Merge 10.4 into 10.5
* Merge [Revision #2e78465d04](https://github.com/MariaDB/server/commit/2e78465d04) 2023-08-15 11:03:47 +0300 - Merge mariadb-10.5.22 into 10.5
* [Revision #d84df2b878](https://github.com/MariaDB/server/commit/d84df2b878)\
  2023-08-14 13:46:16 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
