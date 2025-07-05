# MariaDB 5.5.60 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.60)[Release Notes](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5560-release-notes.md)[Changelog](mariadb-5560-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 23 Apr 2018

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5560-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

* Merge [Revision #51c415d97d](https://github.com/MariaDB/server/commit/51c415d97d) 2018-04-20 01:04:43 +0200 - Merge branch 'merge/merge-xtradb-5.5' into 5.5
* [Revision #4fd1c7e453](https://github.com/MariaDB/server/commit/4fd1c7e453)\
  2018-04-20 01:01:56 +0200
  * 5.5.59-38.11
* [Revision #7828ba0df4](https://github.com/MariaDB/server/commit/7828ba0df4)\
  2018-04-19 22:39:24 +0200
  * Bug#25471090: MYSQL USE AFTER FREE
* [Revision #149c993b2c](https://github.com/MariaDB/server/commit/149c993b2c)\
  2018-04-19 22:36:46 +0200
  * BUG#27216817: INNODB: FAILING ASSERTION: PREBUILT->TABLE->N\_MYSQL\_HANDLES\_OPENED == 1
* [Revision #f1258e7cd2](https://github.com/MariaDB/server/commit/f1258e7cd2)\
  2018-04-19 22:32:27 +0200
  * BUG#26881798: SERVER EXITS WHEN PRIMARY KEY IN MYSQL.PROC IS DROPPED
* Merge [Revision #1a019d0801](https://github.com/MariaDB/server/commit/1a019d0801) 2018-04-19 22:27:02 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #5e61e1716e](https://github.com/MariaDB/server/commit/5e61e1716e)\
  2018-04-16 16:59:19 -0700
  * [MDEV-14515](https://jira.mariadb.org/browse/MDEV-14515) ifnull result depends on number of rows in joined table
* [Revision #88ac368fea](https://github.com/MariaDB/server/commit/88ac368fea)\
  2018-01-13 14:05:14 +1100
  * defaults-group-suffix in print\_defaults
* [Revision #3eb2a265ea](https://github.com/MariaDB/server/commit/3eb2a265ea)\
  2018-04-08 09:05:00 +0400
  * [MDEV-14185](https://jira.mariadb.org/browse/MDEV-14185) CREATE TEMPORARY TABLE AS SELECT causes error 1290 with read\_only and InnoDB.
* [Revision #d6f3a0064b](https://github.com/MariaDB/server/commit/d6f3a0064b)\
  2018-04-07 21:51:15 +0400
  * [MDEV-14185](https://jira.mariadb.org/browse/MDEV-14185) CREATE TEMPORARY TABLE AS SELECT causes error 1290 with read\_only and InnoDB.
* [Revision #6beb08c7b6](https://github.com/MariaDB/server/commit/6beb08c7b6)\
  2018-04-04 09:12:14 +0400
  * [MDEV-15624](https://jira.mariadb.org/browse/MDEV-15624) Changing the default character set to utf8mb4 changes query evaluation in a very surprising way
* [Revision #f5369faf5b](https://github.com/MariaDB/server/commit/f5369faf5b)\
  2018-03-29 15:25:08 +0200
  * don't disable SSL when connecting via libmysqld
* [Revision #df6197c8b9](https://github.com/MariaDB/server/commit/df6197c8b9)\
  2018-02-23 18:50:12 +0100
  * compiler warning
* [Revision #606e21867c](https://github.com/MariaDB/server/commit/606e21867c)\
  2018-04-03 16:28:52 +0400
  * [MDEV-15630](https://jira.mariadb.org/browse/MDEV-15630) uuid() function evaluates at wrong time in query
* [Revision #bdab8b74ff](https://github.com/MariaDB/server/commit/bdab8b74ff)\
  2018-03-24 03:31:18 +0530
  * [MDEV-11274](https://jira.mariadb.org/browse/MDEV-11274): Executing EXPLAIN of complex query over join limit causes server to crash
* [Revision #e8c2366bf8](https://github.com/MariaDB/server/commit/e8c2366bf8)\
  2018-03-27 09:40:10 +0400
  * [MDEV-15620](https://jira.mariadb.org/browse/MDEV-15620) Crash when using "SET @@NEW.a=expr" inside a trigger
* [Revision #ddc5c65333](https://github.com/MariaDB/server/commit/ddc5c65333)\
  2018-03-22 03:01:53 +0530
  * [MDEV-14779](https://jira.mariadb.org/browse/MDEV-14779): using left join causes incorrect results with materialization and derived tables
* [Revision #f3994b7432](https://github.com/MariaDB/server/commit/f3994b7432)\
  2018-03-21 12:13:37 +0100
  * [MDEV-15492](https://jira.mariadb.org/browse/MDEV-15492): Subquery crash similar to [MDEV-10050](https://jira.mariadb.org/browse/MDEV-10050)
* [Revision #2dd4e50d5f](https://github.com/MariaDB/server/commit/2dd4e50d5f)\
  2018-03-21 01:34:45 +0530
  * [MDEV-15555](https://jira.mariadb.org/browse/MDEV-15555): select from DUAL where false yielding wrong result when in a IN
* Merge [Revision #69bc3c1976](https://github.com/MariaDB/server/commit/69bc3c1976) 2018-03-20 18:18:57 +0200 - PR #666: [MDEV-15030](https://jira.mariadb.org/browse/MDEV-15030) Add ASAN instrumentation
* [Revision #5a8f8f89d6](https://github.com/MariaDB/server/commit/5a8f8f89d6)\
  2018-03-20 10:46:57 +0300
  * honor alignment rules and xtradb too
* [Revision #75c76dbb06](https://github.com/MariaDB/server/commit/75c76dbb06)\
  2018-03-19 16:18:53 +0300
  * [MDEV-15030](https://jira.mariadb.org/browse/MDEV-15030) Add ASAN instrumentation
* [Revision #0943b33de3](https://github.com/MariaDB/server/commit/0943b33de3)\
  2018-03-14 14:35:27 +0000
  * [MDEV-12190](https://jira.mariadb.org/browse/MDEV-12190) YASSL isn't able to negotiate TLS version correctly
* [Revision #926edd48e1](https://github.com/MariaDB/server/commit/926edd48e1)\
  2018-03-06 19:59:57 +0530
  * [MDEV-15235](https://jira.mariadb.org/browse/MDEV-15235): Assertion \`length > 0' failed in create\_ref\_for\_key
* [Revision #ac3fd5acac](https://github.com/MariaDB/server/commit/ac3fd5acac)\
  2018-02-03 22:01:30 +1100
  * debian: VCS is on github
* [Revision #7bd258c44c](https://github.com/MariaDB/server/commit/7bd258c44c)\
  2018-02-15 10:06:14 +0100
  * fix plugins.server\_audit test for --ps
* [Revision #03de234baf](https://github.com/MariaDB/server/commit/03de234baf)\
  2018-02-14 19:12:23 +0100
  * [MDEV-13982](https://jira.mariadb.org/browse/MDEV-13982) Server crashes in ha\_partition::engine\_name
* [Revision #2709380587](https://github.com/MariaDB/server/commit/2709380587)\
  2018-02-14 18:14:24 +0100
  * [MDEV-13748](https://jira.mariadb.org/browse/MDEV-13748) Assertion \`status\_var.local\_memory\_used == 0 || !debug\_assert\_on\_not\_freed\_memory' failed in virtual THD::THD after query with INTERSECT
* [Revision #c8afe7daac](https://github.com/MariaDB/server/commit/c8afe7daac)\
  2018-02-05 14:13:26 +0100
  * cleanup: remove a duplicated test case
* [Revision #7c6cf7fefe](https://github.com/MariaDB/server/commit/7c6cf7fefe)\
  2018-01-25 14:25:48 +0100
  * bug: ha\_heap was unilaterally increasing reclength
* [Revision #7a63ffab71](https://github.com/MariaDB/server/commit/7a63ffab71)\
  2018-01-29 18:56:08 +0200
  * Fix an out of scope bzero
* [Revision #5edd129fbf](https://github.com/MariaDB/server/commit/5edd129fbf)\
  2018-01-30 21:05:27 +0200
  * Fix ASAN failure in main.lock (and others)
* [Revision #ded07724ee](https://github.com/MariaDB/server/commit/ded07724ee)\
  2018-01-29 19:46:59 +0200
  * [MDEV-15014](https://jira.mariadb.org/browse/MDEV-15014) Assertion \`m\_cache\_lock\_status == LOCKED\_NO\_WAIT || m\_cache\_status == DISABLE\_REQUEST' failed in Query\_cache::free\_cache on startup
* [Revision #547ec8ce27](https://github.com/MariaDB/server/commit/547ec8ce27)\
  2018-01-29 16:25:26 +0200
  * Do not SET DEBUG\_DBUG=-d,... in tests
* [Revision #ee8755e3c5](https://github.com/MariaDB/server/commit/ee8755e3c5)\
  2018-01-24 14:42:52 +0100
  * [MDEV-15012](https://jira.mariadb.org/browse/MDEV-15012): ASAN: numerous test failures in PS
* [Revision #76577e1e26](https://github.com/MariaDB/server/commit/76577e1e26)\
  2018-01-24 10:58:27 +0100
  * typo fix
* [Revision #e2da680c51](https://github.com/MariaDB/server/commit/e2da680c51)\
  2018-01-23 23:19:09 +0100
  * [MDEV-13187](https://jira.mariadb.org/browse/MDEV-13187) incorrect backslash parsing in clients
* [Revision #8637931f11](https://github.com/MariaDB/server/commit/8637931f11)\
  2018-01-23 19:29:12 +0200
  * Add ASAN instrumentation (and more strict Valgrind) to InnoDB
* [Revision #70a9b12de9](https://github.com/MariaDB/server/commit/70a9b12de9)\
  2018-01-23 18:08:55 +0200
  * Silence -Wimplicit-fallthrough
* [Revision #ba8d0fa700](https://github.com/MariaDB/server/commit/ba8d0fa700)\
  2018-01-15 14:50:35 +0100
  * [MDEV-14786](https://jira.mariadb.org/browse/MDEV-14786): Server crashes in Item\_cond::transform on 2nd execution of SP querying from a view
* [Revision #11408a69ad](https://github.com/MariaDB/server/commit/11408a69ad)\
  2018-01-21 23:44:31 +0100
  * Fix Item tree changes/rollback debug print
* [Revision #94da1cb4a6](https://github.com/MariaDB/server/commit/94da1cb4a6)\
  2018-01-23 15:47:54 +0530
  * [MDEV-14586](https://jira.mariadb.org/browse/MDEV-14586) Assertion \`0' failed in retrieve\_auto\_increment ...
* [Revision #cc3155415e](https://github.com/MariaDB/server/commit/cc3155415e)\
  2018-01-19 19:52:01 +1100
  * [MDEV-5510](https://jira.mariadb.org/browse/MDEV-5510): Replace MySQL -> MariaDB in init scripts
* [Revision #701c7e777f](https://github.com/MariaDB/server/commit/701c7e777f)\
  2018-01-23 11:56:52 +0100
  * Fix error message typo
* [Revision #9ee372736f](https://github.com/MariaDB/server/commit/9ee372736f)\
  2018-01-23 07:37:00 +1100
  * mysql\_install\_db: correct hosting/source/maillist information
* [Revision #c98906e4fe](https://github.com/MariaDB/server/commit/c98906e4fe)\
  2018-01-23 07:35:38 +1100
  * mysql\_install\_db: correct --skip-grant-tables help
* [Revision #3532a421f6](https://github.com/MariaDB/server/commit/3532a421f6)\
  2018-01-23 11:57:54 +0300
  * fix build for recent clang
* [Revision #a04b07eb34](https://github.com/MariaDB/server/commit/a04b07eb34)\
  2018-01-22 23:51:32 +0200
  * Fix TokuDB Not building
* [Revision #8539e4b1b6](https://github.com/MariaDB/server/commit/8539e4b1b6)\
  2018-01-22 13:39:59 +0100
  * improve ASAN instrumentation: clang
* [Revision #b20c3dc664](https://github.com/MariaDB/server/commit/b20c3dc664)\
  2018-01-21 21:18:57 +0200
  * [MDEV-14715](https://jira.mariadb.org/browse/MDEV-14715): Assertion \`!table || (!table->read\_set... failed in Field\_num::val\_decimal
* [Revision #6d826e3d7e](https://github.com/MariaDB/server/commit/6d826e3d7e)\
  2018-01-21 13:12:33 +0200
  * Remove commented out code post merge fix in 2011
* [Revision #03eb15933d](https://github.com/MariaDB/server/commit/03eb15933d)\
  2018-01-21 20:48:59 +0100
  * improve ASAN instrumentation: InnoDB/XtraDB
* [Revision #d9c460b84e](https://github.com/MariaDB/server/commit/d9c460b84e)\
  2018-01-21 15:08:33 +0100
  * Finally! Make './mtr --valgrind-mysqld --gdb' to work.
* [Revision #f2408e7e6a](https://github.com/MariaDB/server/commit/f2408e7e6a)\
  2018-01-20 17:59:37 +0100
  * Free memory in unit tests. Makes ASAN happier.
* [Revision #36eb0b7a55](https://github.com/MariaDB/server/commit/36eb0b7a55)\
  2018-01-21 12:50:49 +0100
  * improve ASAN instrumentation: table->record\[0]
* [Revision #fa331acefd](https://github.com/MariaDB/server/commit/fa331acefd)\
  2018-01-21 11:30:02 +0100
  * improve ASAN instrumentation: mtr
* [Revision #dc28b6d180](https://github.com/MariaDB/server/commit/dc28b6d180)\
  2018-01-21 12:53:17 +0100
  * improve ASAN instrumentation: MEM\_ROOT
* [Revision #a966d422ca](https://github.com/MariaDB/server/commit/a966d422ca)\
  2018-01-20 12:50:28 +0100
  * improve ASAN instrumentation: TRASH
* [Revision #22ae3843db](https://github.com/MariaDB/server/commit/22ae3843db)\
  2018-01-20 17:59:11 +0100
  * Correct TRASH() macro usage
* [Revision #204cb85aab](https://github.com/MariaDB/server/commit/204cb85aab)\
  2018-01-20 11:45:23 +0100
  * Fix compilation without dlopen
* [Revision #906ce0962d](https://github.com/MariaDB/server/commit/906ce0962d)\
  2018-01-22 11:18:10 +0200
  * [MDEV-7049](https://jira.mariadb.org/browse/MDEV-7049) MySQL#74585 - InnoDB: Failing assertion: \*mbmaxlen < 5 in file ha\_innodb.cc line 1904
* [Revision #6c60c809bb](https://github.com/MariaDB/server/commit/6c60c809bb)\
  2018-01-19 18:04:51 +0200
  * Add dummy defintion for Dl\_info in case we're missing dladdr
* [Revision #17f64b362a](https://github.com/MariaDB/server/commit/17f64b362a)\
  2018-01-19 11:01:32 -0500
  * bump the VERSION
* [Revision #26e5f9dda1](https://github.com/MariaDB/server/commit/26e5f9dda1)\
  2018-01-16 22:57:52 +0200
  * [MDEV-14229](https://jira.mariadb.org/browse/MDEV-14229): Stack trace is not resolved for shared objects
* [Revision #a7a4519a40](https://github.com/MariaDB/server/commit/a7a4519a40)\
  2018-01-19 13:29:31 +0530
  * [MDEV-14241](https://jira.mariadb.org/browse/MDEV-14241): Server crash in key\_copy / get\_matching\_chain\_by\_join\_key or valgrind warnings
* [Revision #4f96b401d9](https://github.com/MariaDB/server/commit/4f96b401d9)\
  2018-01-18 09:20:55 -0800
  * Fixed [MDEV-14960](https://jira.mariadb.org/browse/MDEV-14960) \[ERROR] mysqld got signal 11 with join\_buffer and join\_cache

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
