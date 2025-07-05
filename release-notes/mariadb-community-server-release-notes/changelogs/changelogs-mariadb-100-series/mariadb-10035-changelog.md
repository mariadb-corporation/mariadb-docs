# MariaDB 10.0.35 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.35)[Release Notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10035-release-notes.md)[Changelog](mariadb-10035-changelog.md)[Overview of 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)

**Release date:** 3 May 2018

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10035-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Merge [Revision #42fac32413](https://github.com/MariaDB/server/commit/42fac32413) 2018-05-01 11:47:43 +0200 - Merge branch '5.5' into 10.0
* [Revision #fab383aac0](https://github.com/MariaDB/server/commit/fab383aac0)\
  2018-04-30 23:06:09 +0200
  * Use after free in authentication
* [Revision #a52c46e069](https://github.com/MariaDB/server/commit/a52c46e069)\
  2018-04-30 13:50:59 +0200
  * Bug#25471090: MYSQL USE AFTER FREE
* Merge [Revision #c4499a0391](https://github.com/MariaDB/server/commit/c4499a0391) 2018-04-29 00:38:10 +0200 - Merge branch '5.5' into 10.0
* [Revision #5cfe52314e](https://github.com/MariaDB/server/commit/5cfe52314e)\
  2018-04-27 11:21:55 +0200
  * Bug#25471090: MYSQL USE AFTER FREE
* [Revision #eb057dce20](https://github.com/MariaDB/server/commit/eb057dce20)\
  2018-04-24 15:51:49 -0700
  * [MDEV-15035](https://jira.mariadb.org/browse/MDEV-15035) Wrong results when calling a stored procedure multiple times with different arguments.
* [Revision #adaa891ae7](https://github.com/MariaDB/server/commit/adaa891ae7)\
  2018-04-12 14:55:43 +0200
  * [MDEV-13699](https://jira.mariadb.org/browse/MDEV-13699): Assertion \`!new\_field->field\_name.str || strlen(new\_field->field\_name.str) == new\_field->field\_name.length' failed in create\_tmp\_table on 2nd execution of PS with semijoin
* [Revision #d6dbe8e207](https://github.com/MariaDB/server/commit/d6dbe8e207)\
  2018-04-26 22:42:42 +0300
  * List of unstable tests for 10.0.35 release
* Merge [Revision #48636f0972](https://github.com/MariaDB/server/commit/48636f0972) 2018-04-26 14:16:31 +0200 - Merge branch 'merge-pcre' into 10.0
* [Revision #cf242aded5](https://github.com/MariaDB/server/commit/cf242aded5)\
  2018-04-24 19:08:50 +0200
  * 8.42
* [Revision #5ae2656b69](https://github.com/MariaDB/server/commit/5ae2656b69)\
  2018-04-24 20:28:31 +0200
  * Squashed commit of connect/10.0:
* Merge [Revision #1bd33ca82b](https://github.com/MariaDB/server/commit/1bd33ca82b) 2018-04-26 14:14:51 +0200 - Merge branch 'merge-tokudb-5.6' into 10.0
* [Revision #3cd4da3257](https://github.com/MariaDB/server/commit/3cd4da3257)\
  2018-04-24 16:25:16 +0200
  * 5.6.39-83.1
* Merge [Revision #c74848ba14](https://github.com/MariaDB/server/commit/c74848ba14) 2018-04-26 14:13:58 +0200 - Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #6b84fdb2f3](https://github.com/MariaDB/server/commit/6b84fdb2f3)\
  2018-04-24 16:17:43 +0200
  * 5.6.39-83.1
* Merge [Revision #584137879f](https://github.com/MariaDB/server/commit/584137879f) 2018-04-26 14:11:39 +0200 - Merge branch 'merge-perfschema-5.6' into 10.0
* [Revision #7fcd9660a2](https://github.com/MariaDB/server/commit/7fcd9660a2)\
  2018-04-21 17:40:17 +0200
  * 5.6.40 (no changes)
* [Revision #06f02fe250](https://github.com/MariaDB/server/commit/06f02fe250)\
  2018-01-23 17:58:06 +0200
  * 5.6.39 (no changes)
* Merge [Revision #15ec8c2f28](https://github.com/MariaDB/server/commit/15ec8c2f28) 2018-04-26 14:11:09 +0200 - Merge branch 'merge-innodb-5.6' into 10.0
* [Revision #5883c6905b](https://github.com/MariaDB/server/commit/5883c6905b)\
  2018-04-21 17:37:24 +0200
  * 5.6.40
* [Revision #619afb151b](https://github.com/MariaDB/server/commit/619afb151b)\
  2018-04-25 13:20:44 +0200
  * [MDEV-15456](https://jira.mariadb.org/browse/MDEV-15456) Server crashes upon adding or dropping a partition in ALTER under LOCK TABLE after ER\_SAME\_NAME\_PARTITION
* [Revision #03da1253af](https://github.com/MariaDB/server/commit/03da1253af)\
  2018-04-26 14:22:09 +0300
  * Fix compilation error when compiling with valgrind
* [Revision #e86c0a5f2a](https://github.com/MariaDB/server/commit/e86c0a5f2a)\
  2018-04-26 14:21:36 +0300
  * Increase number of max table\_open\_cache instances
* [Revision #c7bb337248](https://github.com/MariaDB/server/commit/c7bb337248)\
  2018-04-23 16:19:50 +0300
  * [MDEV-15723](https://jira.mariadb.org/browse/MDEV-15723) Crash in INFORMATION\_SCHEMA.INNODB\_SYS\_TABLES when accessing corrupted record
* [Revision #fcaf619400](https://github.com/MariaDB/server/commit/fcaf619400)\
  2018-04-21 12:11:04 +0300
  * Remove the "register" keyword
* [Revision #88b1905eda](https://github.com/MariaDB/server/commit/88b1905eda)\
  2018-04-20 22:05:19 +0300
  * Fix -Wimplicit-fallthrough
* [Revision #01b2e773ef](https://github.com/MariaDB/server/commit/01b2e773ef)\
  2018-04-20 10:35:22 +0300
  * [MDEV-15937](https://jira.mariadb.org/browse/MDEV-15937) Assertion failure 'key->flags & 1' on ALTER TABLE
* [Revision #f2433b8dd3](https://github.com/MariaDB/server/commit/f2433b8dd3)\
  2018-04-21 13:13:19 +0200
  * [MDEV-10824](https://jira.mariadb.org/browse/MDEV-10824) - Crash in CREATE OR REPLACE TABLE t1 AS SELECT spfunc()
* [Revision #9fffa9374c](https://github.com/MariaDB/server/commit/9fffa9374c)\
  2018-04-20 20:58:46 +0200
  * mysqltest: use do\_stmt\_close() not mysql\_stmt\_close()
* Merge [Revision #587568b72a](https://github.com/MariaDB/server/commit/587568b72a) 2018-04-20 13:16:03 +0200 - Merge branch '5.5' into 10.0
* [Revision #bcb36ee21e](https://github.com/MariaDB/server/commit/bcb36ee21e)\
  2018-04-20 10:10:33 +0200
  * [MDEV-15456](https://jira.mariadb.org/browse/MDEV-15456) Server crashes upon adding or dropping a partition in ALTER under LOCK TABLE after ER\_SAME\_NAME\_PARTITION
* [Revision #86718fda4e](https://github.com/MariaDB/server/commit/86718fda4e)\
  2018-04-20 09:40:29 +0200
  * compiler warning
* [Revision #4f5dd1d40e](https://github.com/MariaDB/server/commit/4f5dd1d40e)\
  2018-04-17 00:44:46 +0200
  * ASAN error in main.statistics\_index\_crash-7362
* [Revision #226ec99a3e](https://github.com/MariaDB/server/commit/226ec99a3e)\
  2018-04-11 14:22:10 +0400
  * [MDEV-15510](https://jira.mariadb.org/browse/MDEV-15510) - storage/oqgraph: Quench warnings with Boost 1.66
* [Revision #400a8eb60f](https://github.com/MariaDB/server/commit/400a8eb60f)\
  2018-04-06 13:33:08 +0400
  * [MDEV-15291](https://jira.mariadb.org/browse/MDEV-15291) - OQGraph fails to build on FreeBSD
* [Revision #8901155780](https://github.com/MariaDB/server/commit/8901155780)\
  2018-04-04 23:35:47 +0200
  * Update contributors
* Merge [Revision #6a72b9096a](https://github.com/MariaDB/server/commit/6a72b9096a) 2018-04-03 18:08:30 +0300 - Merge branch '5.5' into 10.0
* [Revision #8ffbb825e6](https://github.com/MariaDB/server/commit/8ffbb825e6)\
  2018-03-27 07:55:56 +1100
  * increase upper value of max\_prepared\_stmt\_count to UINT32\_MAX
* [Revision #10f6b7001b](https://github.com/MariaDB/server/commit/10f6b7001b)\
  2018-04-02 13:14:30 +0300
  * [MDEV-9744](https://jira.mariadb.org/browse/MDEV-9744): session optimizer\_use\_condition\_selectivity=5 causing SQL Error (1918): Encountered illegal value '' when converting to DECIMAL
* [Revision #6aff5fa27a](https://github.com/MariaDB/server/commit/6aff5fa27a)\
  2018-03-26 10:33:58 +0400
  * [MDEV-15619](https://jira.mariadb.org/browse/MDEV-15619) using CONVERT() inside AES\_ENCRYPT() in an UPDATE corrupts data
* Merge [Revision #a2e47f8c41](https://github.com/MariaDB/server/commit/a2e47f8c41) 2018-03-23 11:44:29 +0100 - Merge branch '5.5' into 10.0
* Merge [Revision #0492100059](https://github.com/MariaDB/server/commit/0492100059) 2018-03-20 18:36:03 +0200 - Merge 5.5 into 10.0
* [Revision #e3dd9a95e5](https://github.com/MariaDB/server/commit/e3dd9a95e5)\
  2018-03-16 18:57:21 +0530
  * [MDEV-6736](https://jira.mariadb.org/browse/MDEV-6736): Valgrind warnings 'Invalid read' in subselect\_engine::calc\_const\_tables with SQ in WHERE and HAVING, ORDER BY, materialization+semijoin
* Merge [Revision #3d5dff6cae](https://github.com/MariaDB/server/commit/3d5dff6cae) 2018-03-14 12:10:31 +0200 - Merge branch '5.5' into 10.0
* [Revision #48c11d407b](https://github.com/MariaDB/server/commit/48c11d407b)\
  2018-03-13 12:42:41 +0400
  * [MDEV-13202](https://jira.mariadb.org/browse/MDEV-13202) Assertion \`ltime->neg == 0' failed in date\_to\_datetime
* [Revision #4a35e76f64](https://github.com/MariaDB/server/commit/4a35e76f64)\
  2018-03-12 13:06:21 +0200
  * [MDEV-14773](https://jira.mariadb.org/browse/MDEV-14773) DROP TABLE hangs for InnoDB table with FULLTEXT index
* [Revision #4a5c237c76](https://github.com/MariaDB/server/commit/4a5c237c76)\
  2018-03-09 22:26:27 +0200
  * [MDEV-14648](https://jira.mariadb.org/browse/MDEV-14648) Restore fix for MySQL BUG#39053 - UNINSTALL PLUGIN does not allow the storage engine to cleanup open connections
* Merge [Revision #b728641e86](https://github.com/MariaDB/server/commit/b728641e86) 2018-02-22 09:22:03 +0100 - Merge branch '5.5' into 10.0
* [Revision #88d1c1c551](https://github.com/MariaDB/server/commit/88d1c1c551)\
  2018-02-12 15:12:49 +0100
  * [MDEV-15288](https://jira.mariadb.org/browse/MDEV-15288) Configure errors when building without INNOBASE
* [Revision #c051eaba46](https://github.com/MariaDB/server/commit/c051eaba46)\
  2018-02-13 13:01:14 +0200
  * [MDEV-14988](https://jira.mariadb.org/browse/MDEV-14988) innodb\_read\_only tries to modify files if transactions were recovered in COMMITTED state
* [Revision #b0a92333c0](https://github.com/MariaDB/server/commit/b0a92333c0)\
  2018-02-09 19:47:00 +0400
  * [MDEV-15262](https://jira.mariadb.org/browse/MDEV-15262) Wrong results for SELECT..WHERE non\_indexed\_datetime\_column=indexed\_time\_column
* [Revision #6f0b316fbe](https://github.com/MariaDB/server/commit/6f0b316fbe)\
  2018-02-08 21:12:11 +0200
  * Update wrong xtradb version
* [Revision #9216a4f69f](https://github.com/MariaDB/server/commit/9216a4f69f)\
  2018-02-08 13:26:44 +0200
  * Make the test innodb.recovery\_shutdown more robust
* [Revision #5421e3aee7](https://github.com/MariaDB/server/commit/5421e3aee7)\
  2018-02-08 12:51:19 +0200
  * [MDEV-15249](https://jira.mariadb.org/browse/MDEV-15249) Crash in MVCC read after IMPORT TABLESPACE
* [Revision #b6455479e5](https://github.com/MariaDB/server/commit/b6455479e5)\
  2018-02-07 18:14:45 +0100
  * [MDEV-15230](https://jira.mariadb.org/browse/MDEV-15230): column\_json breaks cyrillic in 10.1.31
* [Revision #cb5374801e](https://github.com/MariaDB/server/commit/cb5374801e)\
  2018-02-05 09:23:36 +0200
  * [MDEV-15202](https://jira.mariadb.org/browse/MDEV-15202) innodb.log\_file\_size failed in buildbot
* Merge [Revision #0765caa073](https://github.com/MariaDB/server/commit/0765caa073) 2018-02-02 18:14:35 +0100 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #96cb428b35](https://github.com/MariaDB/server/commit/96cb428b35)\
  2018-01-29 09:44:17 +0100
  * [MDEV-14862](https://jira.mariadb.org/browse/MDEV-14862): Server crashes in Bitmap<64u>::merge / add\_key\_field
* [Revision #d6638586c6](https://github.com/MariaDB/server/commit/d6638586c6)\
  2018-01-31 20:22:31 +0100
  * don't crash debug builds on "packets out of order"
* [Revision #f4414d4c4e](https://github.com/MariaDB/server/commit/f4414d4c4e)\
  2018-01-30 10:54:28 -0500
  * bump the VERSION
* [Revision #6b4a4a85a7](https://github.com/MariaDB/server/commit/6b4a4a85a7)\
  2018-01-30 11:28:21 +0400
  * [MDEV-14696](https://jira.mariadb.org/browse/MDEV-14696) Server crashes in prep\_alter\_part\_table on 2nd execution of PS.
* [Revision #c4a908cb56](https://github.com/MariaDB/server/commit/c4a908cb56)\
  2018-01-30 11:35:27 +0400
  * [MDEV-13790](https://jira.mariadb.org/browse/MDEV-13790) UNHEX() of a somewhat complicated CONCAT() returns NULL
* [Revision #dae4fb0acb](https://github.com/MariaDB/server/commit/dae4fb0acb)\
  2018-01-30 11:07:35 +0400
  * [MDEV-15118](https://jira.mariadb.org/browse/MDEV-15118) ExtractValue(xml,something\_complex) does not work
* [Revision #b76881a23c](https://github.com/MariaDB/server/commit/b76881a23c)\
  2018-01-29 16:39:54 +0200
  * Do not SET DEBUG\_DBUG=-d,... in tests
* Merge [Revision #a5fcced7d1](https://github.com/MariaDB/server/commit/a5fcced7d1) 2018-01-29 16:32:59 +0200 - Merge 5.5 into 10.0
* [Revision #706ed8552d](https://github.com/MariaDB/server/commit/706ed8552d)\
  2018-01-29 11:01:02 +0200
  * Revert "[MDEV-6928](https://jira.mariadb.org/browse/MDEV-6928): Add trx pointer to struct mtr\_t"

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
