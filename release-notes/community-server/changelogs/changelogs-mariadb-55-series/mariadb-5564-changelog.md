# MariaDB 5.5.64 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://mariadb.com/downloads/?showall=1\&tab=mariadbtx\&group=mariadb_server\&version=5.5.64)[Release Notes](../../old-releases/5.5/5.5.64.md)[Changelog](mariadb-5564-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 29 Apr 2019

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.64.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

* [Revision #926446880f](https://github.com/MariaDB/server/commit/926446880f)\
  2019-04-26 15:29:40 +0300
  * [MDEV-15772](https://jira.mariadb.org/browse/MDEV-15772): Clean up the test
* [Revision #757daa4174](https://github.com/MariaDB/server/commit/757daa4174)\
  2019-04-26 08:55:37 +0200
  * fix the test for embedded
* [Revision #da0e00e710](https://github.com/MariaDB/server/commit/da0e00e710)\
  2019-04-25 18:15:12 +0200
  * Bug#28986737: RENAMING AND REPLACING MYSQL.USER TABLE CAN LEAD TO A SERVER CRASH
* [Revision #33fe3b58cc](https://github.com/MariaDB/server/commit/33fe3b58cc)\
  2019-04-25 18:03:16 +0200
  * test case for a previous commit
* [Revision #ae1b8b9bf5](https://github.com/MariaDB/server/commit/ae1b8b9bf5)\
  2019-04-25 18:01:49 +0200
  * Problem ------- MySQL abnormally exits on KILL command.
* [Revision #2be3ab9776](https://github.com/MariaDB/server/commit/2be3ab9776)\
  2019-04-19 12:48:47 +0200
  * [MDEV-15907](https://jira.mariadb.org/browse/MDEV-15907) ASAN heap-use-after-free in strnmov / .. / fill\_effective\_table\_privileges on concurrent GRANT and CREATE VIEW
* [Revision #e52a4ab693](https://github.com/MariaDB/server/commit/e52a4ab693)\
  2019-04-01 11:54:29 +0300
  * [MDEV-15907](https://jira.mariadb.org/browse/MDEV-15907) ASAN heap-use-after-free
* [Revision #5d510fdbf0](https://github.com/MariaDB/server/commit/5d510fdbf0)\
  2019-04-05 12:54:09 +0200
  * [MDEV-18507](https://jira.mariadb.org/browse/MDEV-18507) can't update temporary table when joined with table with triggers on read-only
* [Revision #5057d46375](https://github.com/MariaDB/server/commit/5057d46375)\
  2019-04-04 22:41:58 +0200
  * bugfix: multi-update checked privileges on views incorrectly
* [Revision #822071ca5b](https://github.com/MariaDB/server/commit/822071ca5b)\
  2019-04-05 13:02:51 +0200
  * [MDEV-18241](https://jira.mariadb.org/browse/MDEV-18241) Downgrade from 10.4 to 10.3 crashes
* [Revision #66099b8f2d](https://github.com/MariaDB/server/commit/66099b8f2d)\
  2019-04-03 17:21:10 +0200
  * cleanup
* [Revision #81a8d8be76](https://github.com/MariaDB/server/commit/81a8d8be76)\
  2019-04-03 10:57:45 +0200
  * [MDEV-18923](https://jira.mariadb.org/browse/MDEV-18923) Assertion \`!lex\_string\_cmp(system\_charset\_info, fk\_info->referenced\_table, \&table->s->table\_name)' failed in fk\_truncate\_illegal\_if\_parent
* [Revision #d5da8ae04d](https://github.com/MariaDB/server/commit/d5da8ae04d)\
  2019-04-24 12:31:24 +0530
  * [MDEV-15772](https://jira.mariadb.org/browse/MDEV-15772) Potential list overrun during XA recovery
* [Revision #cb8d888c42](https://github.com/MariaDB/server/commit/cb8d888c42)\
  2019-04-24 11:40:52 +0530
  * [MDEV-17260](https://jira.mariadb.org/browse/MDEV-17260): Memory leaks in mysqlbinlog
* [Revision #e5aa8ea525](https://github.com/MariaDB/server/commit/e5aa8ea525)\
  2019-04-23 17:56:43 +0300
  * [MDEV-18139](https://jira.mariadb.org/browse/MDEV-18139) ALTER IGNORE ... ADD FOREIGN KEY causes bogus error
* [Revision #38b6dc5a3d](https://github.com/MariaDB/server/commit/38b6dc5a3d)\
  2019-04-23 17:25:07 +0300
  * Fix the linking of async\_example
* [Revision #370886a9e2](https://github.com/MariaDB/server/commit/370886a9e2)\
  2019-04-04 13:10:13 +0100
  * [MDEV-17610](https://jira.mariadb.org/browse/MDEV-17610) Unexpected connection abort after certain operations from within stored procedure
* [Revision #f2d549d8db](https://github.com/MariaDB/server/commit/f2d549d8db)\
  2019-03-27 12:34:03 +0530
  * [MDEV-14784](https://jira.mariadb.org/browse/MDEV-14784): Slave crashes in show\_status\_array upon running a trigger with select from I\_S
* [Revision #e890711279](https://github.com/MariaDB/server/commit/e890711279)\
  2019-03-26 00:42:57 +0400
  * Fixed ps-protocol thread\_pool\_server\_audit failure
* [Revision #cfe0fe1ad1](https://github.com/MariaDB/server/commit/cfe0fe1ad1)\
  2019-01-26 19:12:17 +0100
  * Fix tests in 2020
* [Revision #c61e8a6597](https://github.com/MariaDB/server/commit/c61e8a6597)\
  2019-03-24 13:24:28 -0400
  * Fix for [MDEV-17449](https://jira.mariadb.org/browse/MDEV-17449), typo in error message (#1146)
* [Revision #d8b7e76c37](https://github.com/MariaDB/server/commit/d8b7e76c37)\
  2019-02-07 01:23:28 -0500
  * Fix for [MDEV-18276](https://jira.mariadb.org/browse/MDEV-18276), typo in error message + all other occurrences of refering
* [Revision #778c525ff8](https://github.com/MariaDB/server/commit/778c525ff8)\
  2019-03-20 15:04:24 +0530
  * [MDEV-17119](https://jira.mariadb.org/browse/MDEV-17119) replicate\_rewrite\_db does not work for single chardatabase name
* [Revision #f00e25b4c4](https://github.com/MariaDB/server/commit/f00e25b4c4)\
  2019-02-10 15:48:12 -0500
  * Fix for [MDEV-15538](https://jira.mariadb.org/browse/MDEV-15538), '-N' Produce html output wrong
* [Revision #0dd12b4f2a](https://github.com/MariaDB/server/commit/0dd12b4f2a)\
  2019-03-14 17:41:35 -0700
  * [MDEV-18896](https://jira.mariadb.org/browse/MDEV-18896) Crash in convert\_join\_subqueries\_to\_semijoins
* [Revision #8024f8c6b8](https://github.com/MariaDB/server/commit/8024f8c6b8)\
  2019-03-07 11:57:14 +0200
  * [MDEV-18272](https://jira.mariadb.org/browse/MDEV-18272) InnoDB fails to rollback after exceeding FOREIGN KEY recursion depth
* [Revision #cb11b3fbe9](https://github.com/MariaDB/server/commit/cb11b3fbe9)\
  2019-02-27 15:53:25 +0100
  * [MDEV-17055](https://jira.mariadb.org/browse/MDEV-17055): Server crashes in find\_order\_in\_list upon 2nd (3rd) execution of SP with UPDATE
* [Revision #0ad598a00b](https://github.com/MariaDB/server/commit/0ad598a00b)\
  2019-02-28 18:13:28 +0400
  * A cleanup in derived table handling: removing duplicate code from st\_select\_lex::handle\_derived()
* [Revision #c9b9d9f515](https://github.com/MariaDB/server/commit/c9b9d9f515)\
  2019-02-07 16:46:39 +0100
  * [MDEV-18506](https://jira.mariadb.org/browse/MDEV-18506) MSI can't be built if MFC package is not installed with Visual Studio
* [Revision #9034e5e18e](https://github.com/MariaDB/server/commit/9034e5e18e)\
  2019-01-30 10:12:21 -0500
  * bump the VERSION
* [Revision #6092093cb9](https://github.com/MariaDB/server/commit/6092093cb9)\
  2019-01-30 19:35:40 +0530
  * [MDEV-15950](https://jira.mariadb.org/browse/MDEV-15950): LOAD DATA INTO compex\_view crashed
* [Revision #08c05b5f34](https://github.com/MariaDB/server/commit/08c05b5f34)\
  2019-01-29 14:18:35 +0200
  * [MDEV-15744](https://jira.mariadb.org/browse/MDEV-15744): Assertion \`derived->table' failed in mysql\_derived\_merge\_for\_insert
* [Revision #eff71f39dd](https://github.com/MariaDB/server/commit/eff71f39dd)\
  2019-01-28 11:51:12 +0100
  * disable an old test

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
