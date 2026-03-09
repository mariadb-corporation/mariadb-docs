# MariaDB 10.4.26 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.26](https://downloads.mariadb.org/mariadb/10.4.26/)[Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10426-release-notes)[Changelog](mariadb-10426-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 15 Aug 2022

For the highlights of this release, see the [release notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.36](../changelogs-mariadb-10-3-series/mariadb-10336-changelog.md)
* Merge [Revision #65e8506ca9](https://github.com/MariaDB/server/commit/65e8506ca9) 2022-08-10 12:21:08 +0200 - Merge branch '10.3' into bb-10.4-release
* Merge [Revision #6adfce9c8d](https://github.com/MariaDB/server/commit/6adfce9c8d) 2022-08-04 12:13:31 +0200 - Merge branch '10.3' into 10.4
* Merge [Revision #b4c572f48a](https://github.com/MariaDB/server/commit/b4c572f48a) 2022-08-04 10:46:04 +0200 - Merge branch '10.3' into 10.4
* [Revision #c6406643cd](https://github.com/MariaDB/server/commit/c6406643cd)\
  2022-08-04 10:01:24 +0200
  * Fix compile errors.
* Merge [Revision #e509065247](https://github.com/MariaDB/server/commit/e509065247) 2022-08-03 19:51:44 +0200 - Merge branch '10.3' into 10.4
* [Revision #8fd8a81a99](https://github.com/MariaDB/server/commit/8fd8a81a99)\
  2022-08-03 12:49:49 +0200
  * Fix Oracle parser.
* Merge [Revision #48e35b8cf6](https://github.com/MariaDB/server/commit/48e35b8cf6) 2022-08-02 14:15:39 +0200 - Merge branch '10.3' into 10.4
* [Revision #1ea5e402a8](https://github.com/MariaDB/server/commit/1ea5e402a8)\
  2022-08-01 11:13:50 +0300
  * [MDEV-28727](https://jira.mariadb.org/browse/MDEV-28727) ALTER TABLE ALGORITHM=NOCOPY does not work after upgrade
* [Revision #231feabd2b](https://github.com/MariaDB/server/commit/231feabd2b)\
  2022-08-01 11:13:50 +0300
  * [MDEV-21540](https://jira.mariadb.org/browse/MDEV-21540) Initialization of already inited long unique index on reorganize partition
* [Revision #f0107c90a0](https://github.com/MariaDB/server/commit/f0107c90a0)\
  2022-07-27 16:21:28 +0200
  * wolfssl v5.4.0-stable
* [Revision #4329720b79](https://github.com/MariaDB/server/commit/4329720b79)\
  2022-07-25 13:27:23 +0200
  * Fixes for WolfSSL 5.4.0
* Merge [Revision #e5c4f4e590](https://github.com/MariaDB/server/commit/e5c4f4e590) 2022-07-27 14:25:36 +0300 - Merge 10.3 into 10.4
* Merge [Revision #3bb36e9495](https://github.com/MariaDB/server/commit/3bb36e9495) 2022-07-27 11:02:57 +0200 - Merge branch '10.3' into 10.4
* [Revision #9a897335eb](https://github.com/MariaDB/server/commit/9a897335eb)\
  2022-07-26 16:45:10 +0300
  * [MDEV-26420](https://jira.mariadb.org/browse/MDEV-26420) Buffer overflow on instant ADD/DROP of generated column
* [Revision #8911823f65](https://github.com/MariaDB/server/commit/8911823f65)\
  2022-07-16 16:54:03 +0400
  * [MDEV-26546](https://jira.mariadb.org/browse/MDEV-26546) SIGSEGV's in spider\_db\_connect on SHOW TABLE and spider\_db… …\_mbase::connect (and SIGSEGV's in check\_vcol\_forward\_refs and inline\_mysql\_mutex\_lock)
* [Revision #65cc89ed9e](https://github.com/MariaDB/server/commit/65cc89ed9e)\
  2022-07-13 11:13:06 -0700
  * [MDEV-29088](https://jira.mariadb.org/browse/MDEV-29088) Server crash upon CREATE VIEW with unknown column in ON condition
* [Revision #f439cfdf93](https://github.com/MariaDB/server/commit/f439cfdf93)\
  2022-07-12 17:18:48 +0700
  * [MDEV-22001](https://jira.mariadb.org/browse/MDEV-22001): Server crashes in st\_select\_lex\_unit::exclude\_level upon execution of SP
* [Revision #9a0cbd31ce](https://github.com/MariaDB/server/commit/9a0cbd31ce)\
  2022-07-04 08:04:44 +0300
  * [MDEV-26294](https://jira.mariadb.org/browse/MDEV-26294) Duplicate entries in unique index not detected when changing collation
* Merge [Revision #392ee571c1](https://github.com/MariaDB/server/commit/392ee571c1) 2022-07-01 13:10:36 +0300 - Merge 10.3 into 10.4
* [Revision #99de8cc028](https://github.com/MariaDB/server/commit/99de8cc028)\
  2022-06-28 15:51:05 +0530
  * [MDEV-28919](https://jira.mariadb.org/browse/MDEV-28919) Assertion \`(((core\_null) + 7) >> 3) == oindex.n\_core\_null\_bytes || !not\_redundant()' failed
* [Revision #d89cac0884](https://github.com/MariaDB/server/commit/d89cac0884)\
  2022-06-18 02:19:41 +0300
  * [MDEV-28567](https://jira.mariadb.org/browse/MDEV-28567) MDL debug logging
* [Revision #dbd562787a](https://github.com/MariaDB/server/commit/dbd562787a)\
  2021-10-11 14:21:10 +0900
  * [MDEV-24343](https://jira.mariadb.org/browse/MDEV-24343) Spider Left join failed Unknown column 't0.ID' in 'on clause'
* Merge [Revision #b922ae5fc9](https://github.com/MariaDB/server/commit/b922ae5fc9) 2022-06-27 16:16:20 +0300 - Merge 10.3 into 10.4
* [Revision #dd7e9fb38a](https://github.com/MariaDB/server/commit/dd7e9fb38a)\
  2022-06-27 10:47:05 +0300
  * [MDEV-28854](https://jira.mariadb.org/browse/MDEV-28854) after-merge fix: Remove a test for [MDEV-26583](https://jira.mariadb.org/browse/MDEV-26583)
* Merge [Revision #01d757036f](https://github.com/MariaDB/server/commit/01d757036f) 2022-06-27 10:14:37 +0300 - Merge 10.3 into 10.4
* [Revision #af929146ed](https://github.com/MariaDB/server/commit/af929146ed)\
  2022-06-17 13:56:03 +0200
  * [MDEV-28583](https://jira.mariadb.org/browse/MDEV-28583) postfix: fixing .result files after automatic merge
* [Revision #01c0345d44](https://github.com/MariaDB/server/commit/01c0345d44)\
  2022-06-20 16:17:14 +0200
  * [MDEV-28819](https://jira.mariadb.org/browse/MDEV-28819) Statically compiled encryption plugins do not work in mariadb-backup
* [Revision #0565dfe490](https://github.com/MariaDB/server/commit/0565dfe490)\
  2022-06-17 19:38:40 +0300
  * [MDEV-17390](https://jira.mariadb.org/browse/MDEV-17390): re-neable rpl\_semi\_sync\_after\_sync test
* Merge [Revision #c89e3b70a7](https://github.com/MariaDB/server/commit/c89e3b70a7) 2022-06-09 11:53:46 +0300 - Merge 10.3 into 10.4
* [Revision #5efadf8d8c](https://github.com/MariaDB/server/commit/5efadf8d8c)\
  2022-06-04 10:16:15 +0400
  * [MDEV-28747](https://jira.mariadb.org/browse/MDEV-28747) Index condition pushdown may be configured incorrectly
* [Revision #09177eadc3](https://github.com/MariaDB/server/commit/09177eadc3)\
  2022-06-07 16:00:49 +0300
  * [MDEV-25257](https://jira.mariadb.org/browse/MDEV-25257) follow-up: full\_crc32 format is garbage-free
* Merge [Revision #ea1fbd0326](https://github.com/MariaDB/server/commit/ea1fbd0326) 2022-06-07 15:55:32 +0300 - Merge 10.3 into 10.4
* Merge [Revision #96f4b4a55b](https://github.com/MariaDB/server/commit/96f4b4a55b) 2022-06-02 16:34:17 +0300 - Merge 10.3 into 10.4
* [Revision #ebbd5ef6e2](https://github.com/MariaDB/server/commit/ebbd5ef6e2)\
  2022-05-10 11:15:32 +0200
  * [MDEV-27862](https://jira.mariadb.org/browse/MDEV-27862) Galera should replicate nextval()-related changes in sequences with INCREMENT <> 0, at least NOCACHE ones with engine=InnoDB
* [Revision #c8fabbed42](https://github.com/MariaDB/server/commit/c8fabbed42)\
  2022-05-30 11:11:48 +0300
  * [MDEV-20627](https://jira.mariadb.org/browse/MDEV-20627) : Galera 4 not able to report proper wsrep\_incoming\_addresses
* [Revision #99c8aed00d](https://github.com/MariaDB/server/commit/99c8aed00d)\
  2022-05-25 14:06:04 +0300
  * [MDEV-28601](https://jira.mariadb.org/browse/MDEV-28601) InnoDB history list length was reverted to 32 bits
* [Revision #c1d380aa88](https://github.com/MariaDB/server/commit/c1d380aa88)\
  2022-05-24 07:17:16 +0300
  * Update galera disabled.def file
* [Revision #0263944a7f](https://github.com/MariaDB/server/commit/0263944a7f)\
  2022-05-24 07:11:10 +0300
  * [MDEV-20888](https://jira.mariadb.org/browse/MDEV-20888) : Galera test failure on galera.galera\_pc\_ignore\_sb: 2013: Lost connection to MySQL server during query
* [Revision #665c01d1f2](https://github.com/MariaDB/server/commit/665c01d1f2)\
  2022-05-24 07:09:27 +0300
  * [MDEV-15794](https://jira.mariadb.org/browse/MDEV-15794) : Test failure on galera.galera\_var\_retry\_autocommit
* [Revision #82f45ef576](https://github.com/MariaDB/server/commit/82f45ef576)\
  2022-05-24 07:08:12 +0300
  * [MDEV-18179](https://jira.mariadb.org/browse/MDEV-18179) : Galera test failure on galera.galera\_kill\_largechanges [MDEV-18283](https://jira.mariadb.org/browse/MDEV-18283) : Galera test failure on galera.GCF-1081
* Merge [Revision #2f6a014fa2](https://github.com/MariaDB/server/commit/2f6a014fa2) 2022-05-23 08:07:03 +0300 - Merge 10.4 into 10.5
* Merge [Revision #cf75793d00](https://github.com/MariaDB/server/commit/cf75793d00) 2022-05-20 19:27:44 +0200 - Merge branch '10.4' into bb-10.4-release
* [Revision #8872ad44a7](https://github.com/MariaDB/server/commit/8872ad44a7)\
  2022-05-20 11:46:31 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
