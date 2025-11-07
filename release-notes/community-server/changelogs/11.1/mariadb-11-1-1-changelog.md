# MariaDB 11.1.1 Changelog

The most recent release of [MariaDB 11.1](../../old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111.md) is:[**MariaDB 11.1.6**](../../old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.1.6/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.1.6/)

[Download 11.1.1](https://downloads.mariadb.org/mariadb/11.1.1/)[Release Notes](../../old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-1-release-notes.md)[Changelog](mariadb-11-1-1-changelog.md)[Overview of 11.1](../../old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.1.1/)

**Release date:** 6 Jun 2023

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-1-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Changes from [11.1.0](../../old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes.md) are also included in this changelog
* Includes all fixes from [MariaDB 11.0.2](../11.0/mariadb-11-0-2-changelog.md)
* [Revision #51b93a096e](https://github.com/MariaDB/server/commit/51b93a096e)\
  2023-05-25 11:42:25 +0200
  * columnstore warnings with gcc 12.x and 13.x
* [Revision #19856db637](https://github.com/MariaDB/server/commit/19856db637)\
  2023-05-27 00:58:36 +0200
  * disable lto in srpm builds
* [Revision #2f2047be35](https://github.com/MariaDB/server/commit/2f2047be35)\
  2023-05-05 16:53:49 +0200
  * [MDEV-25080](https://jira.mariadb.org/browse/MDEV-25080) Switch to new version of ColumnStore
* [Revision #dd5d641c9e](https://github.com/MariaDB/server/commit/dd5d641c9e)\
  2023-04-13 18:19:37 +0200
  * enable ColumnStore only on selected DEB distributions
* [Revision #5590e9132e](https://github.com/MariaDB/server/commit/5590e9132e)\
  2023-04-13 18:18:57 +0200
  * autobake-deb: move columnstore code down
* [Revision #d5e3d37ec2](https://github.com/MariaDB/server/commit/d5e3d37ec2)\
  2022-11-14 20:46:42 +0100
  * more C API methods in the service\_sql
* [Revision #47e29a2ff4](https://github.com/MariaDB/server/commit/47e29a2ff4)\
  2023-02-09 14:09:31 +0700
  * [MDEV-25080](https://jira.mariadb.org/browse/MDEV-25080) Fix incorrect view names in printed queries
* [Revision #b5507c738f](https://github.com/MariaDB/server/commit/b5507c738f)\
  2023-02-04 14:12:54 +0700
  * [MDEV-25080](https://jira.mariadb.org/browse/MDEV-25080) Fix crash for CREATE TABLE from pushed union
* [Revision #3118132228](https://github.com/MariaDB/server/commit/3118132228)\
  2022-08-20 22:23:45 +0700
  * [MDEV-25080](https://jira.mariadb.org/browse/MDEV-25080) Allow pushdown of UNIONs to foreign engines
* Merge [Revision #cbabb95915](https://github.com/MariaDB/server/commit/cbabb95915) 2023-06-05 20:13:06 +0200 - Merge branch '11.0' into 11.1
* [Revision #17127fd91b](https://github.com/MariaDB/server/commit/17127fd91b)\
  2023-05-31 09:04:33 +1000
  * Update README.md
* [Revision #092dba6340](https://github.com/MariaDB/server/commit/092dba6340)\
  2023-05-29 19:03:53 -0300
  * Update README to point to the Security Policy in GitHub
* [Revision #e37a7197c7](https://github.com/MariaDB/server/commit/e37a7197c7)\
  2023-05-29 18:45:49 -0300
  * Create SECURITY.md
* [Revision #4e5b771e98](https://github.com/MariaDB/server/commit/4e5b771e98)\
  2023-05-02 16:34:07 +0530
  * [MDEV-30677](https://jira.mariadb.org/browse/MDEV-30677): Incorrect result for "SELECT JSON\_SCHEMA\_VALID('{}', NULL)" Analysis: null\_value is not set if any one of the arguments is NULL. So it returns 1. Fix: when either argument is NULL, set null\_value to true, so that null can be returned
* [Revision #97675570ca](https://github.com/MariaDB/server/commit/97675570ca)\
  2023-04-25 13:54:05 +0530
  * [MDEV-30689](https://jira.mariadb.org/browse/MDEV-30689): JSON\_SCHEMA\_VALID for type=array return 1 for any string that starts with '\['
* [Revision #3ef111610b](https://github.com/MariaDB/server/commit/3ef111610b)\
  2023-03-09 10:39:29 -0800
  * \[[MDEV-29827](https://jira.mariadb.org/browse/MDEV-29827)] Clear error when --event-scheduler=ON is combined with --skip-grant-tables
* [Revision #7321c71aa1](https://github.com/MariaDB/server/commit/7321c71aa1)\
  2023-04-17 17:51:34 +0530
  * [MDEV-31032](https://jira.mariadb.org/browse/MDEV-31032): UBSAN|downcast of address X which does not point to an object of type 'Item\_string' in sql/json\_schema.cc
* [Revision #4b67ff3b25](https://github.com/MariaDB/server/commit/4b67ff3b25)\
  2023-03-03 13:50:46 +0530
  * [MDEV-30705](https://jira.mariadb.org/browse/MDEV-30705): JSON\_SCHEMA\_VALID: schema with multipleOf for big value always return 1
* [Revision #2c4c7c8b02](https://github.com/MariaDB/server/commit/2c4c7c8b02)\
  2023-03-02 17:19:36 +0530
  * [MDEV-30704](https://jira.mariadb.org/browse/MDEV-30704): JSON\_SCHEMA\_VALID: multipleOf must be greater than zero
* [Revision #dffd1679ba](https://github.com/MariaDB/server/commit/dffd1679ba)\
  2023-03-02 19:09:45 +0530
  * [MDEV-30703](https://jira.mariadb.org/browse/MDEV-30703): JSON\_SCHEMA\_VALID : Enum array must have at least one value
* [Revision #d555f38af8](https://github.com/MariaDB/server/commit/d555f38af8)\
  2023-03-02 17:50:19 +0530
  * [MDEV-30690](https://jira.mariadb.org/browse/MDEV-30690): Server crashed on function JSON\_SCHEMA\_VALID with incorrect input json schema
* [Revision #1c25b5c026](https://github.com/MariaDB/server/commit/1c25b5c026)\
  2023-04-04 14:39:41 +0530
  * [MDEV-30977](https://jira.mariadb.org/browse/MDEV-30977): Additional key values are not validating properly when using unevaluatedProperties with properties declared in subschemas
* [Revision #ee41fa38fc](https://github.com/MariaDB/server/commit/ee41fa38fc)\
  2023-04-04 13:35:02 +0530
  * [MDEV-30995](https://jira.mariadb.org/browse/MDEV-30995): JSON\_SCHEMA\_VALID is not validating case sensitive when using regex
* [Revision #8939e21dc5](https://github.com/MariaDB/server/commit/8939e21dc5)\
  2023-03-06 18:00:04 +0530
  * [MDEV-30795](https://jira.mariadb.org/browse/MDEV-30795): JSON\_SCHEMA\_VALID bugs mentioned in comment
* [Revision #358b8495f5](https://github.com/MariaDB/server/commit/358b8495f5)\
  2022-10-28 13:03:13 +0530
  * [MDEV-27128](https://jira.mariadb.org/browse/MDEV-27128): Implement JSON Schema Validation FUNCTION
* [Revision #af0e0ad18d](https://github.com/MariaDB/server/commit/af0e0ad18d)\
  2023-04-11 11:18:42 +0700
  * [MDEV-30946](https://jira.mariadb.org/browse/MDEV-30946) Index usage for DATE(datetime\_column) = const does not work for DELETE and UPDATE
* [Revision #9f9a53be40](https://github.com/MariaDB/server/commit/9f9a53be40)\
  2023-03-24 21:01:09 +0700
  * [MDEV-30901](https://jira.mariadb.org/browse/MDEV-30901) Index usage for DATE(datetime\_column) = const does not work for engine Memory
* [Revision #f0b665f880](https://github.com/MariaDB/server/commit/f0b665f880)\
  2023-02-17 19:21:30 +0700
  * [MDEV-8320](https://jira.mariadb.org/browse/MDEV-8320) Allow index usage for DATE(col) <=> const and YEAR <=> const
* [Revision #54c11273e3](https://github.com/MariaDB/server/commit/54c11273e3)\
  2023-04-13 23:10:52 +1000
  * [MDEV-28363](https://jira.mariadb.org/browse/MDEV-28363) remove #ifdef SPIDER\_use\_LEX\_CSTRING\_for\_Field\_blob\_constructor
* [Revision #d20a96f9c1](https://github.com/MariaDB/server/commit/d20a96f9c1)\
  2023-03-12 13:55:30 +0800
  * [MDEV-21921](https://jira.mariadb.org/browse/MDEV-21921) Make transaction\_isolation and transaction\_read\_only into system variables
* [Revision #4472a7b4ff](https://github.com/MariaDB/server/commit/4472a7b4ff)\
  2023-04-11 17:23:55 +1000
  * [MDEV-30205](https://jira.mariadb.org/browse/MDEV-30205): /usr/share/mysql-test -> mariadb-test (fix)
* [Revision #320a4b52c9](https://github.com/MariaDB/server/commit/320a4b52c9)\
  2022-12-12 14:20:08 +1100
  * [MDEV-30205](https://jira.mariadb.org/browse/MDEV-30205) Move /usr/share/mysql to /usr/share/mariadb
* Merge [Revision #2b61ff8f22](https://github.com/MariaDB/server/commit/2b61ff8f22) 2023-03-29 17:23:21 +0300 - Merge 11.0 into 11.1
* [Revision #7bd225e129](https://github.com/MariaDB/server/commit/7bd225e129)\
  2023-03-24 10:38:20 +1100
  * [MDEV-30920](https://jira.mariadb.org/browse/MDEV-30920) Remove need\_lock and table from spider\_close\_sys\_table()
* [Revision #5a1f7522a5](https://github.com/MariaDB/server/commit/5a1f7522a5)\
  2023-03-27 13:43:18 +0300
  * Fix ColumnStore again
* Merge [Revision #f6c5e917e0](https://github.com/MariaDB/server/commit/f6c5e917e0) 2023-03-27 12:53:57 +0300 - Merge 11.0 into 11.1
* [Revision #e371b1e264](https://github.com/MariaDB/server/commit/e371b1e264)\
  2023-03-24 15:12:08 +0200
  * [MDEV-28883](https://jira.mariadb.org/browse/MDEV-28883) fixup: clang -Winconsistent-missing-override
* Merge [Revision #9aa098c46b](https://github.com/MariaDB/server/commit/9aa098c46b) 2023-03-23 12:38:46 +0200 - Merge 11.0 into 11.1
* [Revision #22392b36ee](https://github.com/MariaDB/server/commit/22392b36ee)\
  2022-05-27 08:55:42 +0900
  * [MDEV-28522](https://jira.mariadb.org/browse/MDEV-28522) Delete constant SPIDER\_SQL\_TYPE\_\*\_HS
* Merge [Revision #bdcb2ae509](https://github.com/MariaDB/server/commit/bdcb2ae509) 2023-03-20 10:39:40 +0200 - Merge 11.0 into 11.1
* Merge [Revision #6e58d5ab6a](https://github.com/MariaDB/server/commit/6e58d5ab6a) 2023-03-17 15:04:38 +0200 - Merge 11.0 into 11.1
* [Revision #fc18f9c9ec](https://github.com/MariaDB/server/commit/fc18f9c9ec)\
  2023-03-15 18:29:05 -0700
  * Adjusted test results after rebase of [MDEV-7487](https://jira.mariadb.org/browse/MDEV-7487) related commits against 11.1
* [Revision #1e0a72a18b](https://github.com/MariaDB/server/commit/1e0a72a18b)\
  2022-09-19 12:26:59 +0700
  * [MDEV-29390](https://jira.mariadb.org/browse/MDEV-29390): Improve coverage for UPDATE and DELETE statements in MTR test suites
* [Revision #9a3fd1df01](https://github.com/MariaDB/server/commit/9a3fd1df01)\
  2023-03-09 21:48:58 -0800
  * Adjusted test results after rebase against 11.0.1
* [Revision #c912fd3b29](https://github.com/MariaDB/server/commit/c912fd3b29)\
  2023-02-09 20:45:04 -0800
  * Fixes of [MDEV-30538](https://jira.mariadb.org/browse/MDEV-30538) and [MDEV-30586](https://jira.mariadb.org/browse/MDEV-30586) for 10.4 adjusted for 11.0.
* [Revision #554278e24d](https://github.com/MariaDB/server/commit/554278e24d)\
  2023-01-09 22:39:39 -0800
  * [MDEV-7487](https://jira.mariadb.org/browse/MDEV-7487) Semi-join optimization for single-table update/delete statements
* [Revision #e2e3524d72](https://github.com/MariaDB/server/commit/e2e3524d72)\
  2022-09-16 22:36:22 -0700
  * Another fix after the latest rebase of commits for [MDEV-28883](https://jira.mariadb.org/browse/MDEV-28883)
* [Revision #c22f7e8e0a](https://github.com/MariaDB/server/commit/c22f7e8e0a)\
  2022-09-13 17:16:31 -0700
  * [MDEV-29428](https://jira.mariadb.org/browse/MDEV-29428) Incorrect result for delete with "order by" clause
* [Revision #ee495b2235](https://github.com/MariaDB/server/commit/ee495b2235)\
  2022-09-13 16:14:10 -0700
  * Fix after the latest rebase of commits for [MDEV-28883](https://jira.mariadb.org/browse/MDEV-28883)
* [Revision #11701780e0](https://github.com/MariaDB/server/commit/11701780e0)\
  2022-08-18 20:40:04 -0700
  * Applied the changes introduced in the commit
* [Revision #24f75b7f25](https://github.com/MariaDB/server/commit/24f75b7f25)\
  2022-07-28 17:52:47 -0700
  * [MDEV-29189](https://jira.mariadb.org/browse/MDEV-29189) Crash of the second execution of SF using DELETE/UPDATE
* [Revision #9f79652625](https://github.com/MariaDB/server/commit/9f79652625)\
  2022-07-26 21:24:01 -0700
  * Assertion failure with UPDATE of view using MERGE table
* [Revision #88ca62dc68](https://github.com/MariaDB/server/commit/88ca62dc68)\
  2022-07-11 16:57:37 -0700
  * [MDEV-28965](https://jira.mariadb.org/browse/MDEV-28965) Assertion failure when preparing UPDATE with derived table in WHERE
* [Revision #3a9358a410](https://github.com/MariaDB/server/commit/3a9358a410)\
  2022-06-18 16:28:48 -0700
  * [MDEV-28883](https://jira.mariadb.org/browse/MDEV-28883) Re-design the upper level of handling UPDATE and DELETE statements
* [Revision #7ca89af6f8](https://github.com/MariaDB/server/commit/7ca89af6f8)\
  2023-03-11 10:45:35 +0200
  * [MDEV-30545](https://jira.mariadb.org/browse/MDEV-30545) Remove innodb\_defragment and related parameters
* [Revision #b314f7b642](https://github.com/MariaDB/server/commit/b314f7b642)\
  2023-02-03 07:42:59 +0400
  * [MDEV-18931](https://jira.mariadb.org/browse/MDEV-18931) Rename mariadb-backup's xtrabackup\_\* files to mariadb\_backup\_\*
* [Revision #4ae97333f0](https://github.com/MariaDB/server/commit/4ae97333f0)\
  2023-03-08 19:50:40 +0100
  * 11.1 branch

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
