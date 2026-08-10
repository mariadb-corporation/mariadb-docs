# MariaDB Galera Cluster 10.0.32 Changelog

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.32)[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10032-release-notes.md)[Changelog](mariadb-galera-cluster-10032-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 17 Aug 2017

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10032-release-notes.md).\
For changes made in MariaDB, see the [MariaDB 10.0.32 Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10032-changelog.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code
modified in that revision.

* [Revision #0a479f7860](https://github.com/MariaDB/server/commit/0a479f7860)\
  2017-08-16 13:10:01 +0300
  * More test failure fixes.
* [Revision #7ce37d9757](https://github.com/MariaDB/server/commit/7ce37d9757)\
  2017-08-16 10:14:19 +0300
  * Move galera\_ist\_progress and galera\_ist\_restart\_joiner tests under big\_test.
* [Revision #81fd8ff676](https://github.com/MariaDB/server/commit/81fd8ff676)\
  2017-08-16 07:49:19 +0300
  * Fix test failures.
* [Revision #5017c261d4](https://github.com/MariaDB/server/commit/5017c261d4)\
  2017-08-15 13:57:15 +0300
  * Fix test failure on test MW-86 and remove MW-360 test.
* [Revision #b5323054af](https://github.com/MariaDB/server/commit/b5323054af)\
  2017-05-24 14:55:13 +0300
  * MW-383 Bumped wsrep patch version
* [Revision #dd72d66c45](https://github.com/MariaDB/server/commit/dd72d66c45)\
  2017-04-24 18:39:38 +0300
  * MW-373 Wait for wsrep\_ready at startup when provider is loaded
* [Revision #224ae5770f](https://github.com/MariaDB/server/commit/224ae5770f)\
  2017-02-22 10:57:39 +0200
  * Refs: MW-363
    * enabling binlog file copying even for binlog files with basename "0"
    * mtr suite uses binlog files with names: 0.000001, 0.000002.. and so on
* [Revision #7ee47ef456](https://github.com/MariaDB/server/commit/7ee47ef456)\
  2017-05-10 15:59:52 +0300
  * MW-378 enabling build with WITH\_WSREP=OFF only one fix here, enables build of mysqld however, building embedded server fails in linking phase
* [Revision #318af3f3b8](https://github.com/MariaDB/server/commit/318af3f3b8)\
  2017-05-08 23:03:01 +0300
  * MW-369 FK fixes
* [Revision #f3c5928cff](https://github.com/MariaDB/server/commit/f3c5928cff)\
  2017-05-08 23:03:01 +0300
  * MW-369 FK fixes
* [Revision #d43a12bf2f](https://github.com/MariaDB/server/commit/d43a12bf2f)\
  2017-05-08 16:23:25 +0300
  * MW-369 Removing obsoleted tests
* [Revision #7a1a5e473e](https://github.com/MariaDB/server/commit/7a1a5e473e)\
  2017-04-15 02:20:36 +0300
  * Refs: MW-369
    * fixed sync point usage in MW-369.inc, which made it impossible to run this test with --repeat option
    * moved all MW-369\*.test tests into MW-369.test file, each as one separate test phase
    * added two more test phases, in MW-369.test file
    * tests MW-369A, MW-369B and MW-369C are obsolete after this commit
* [Revision #0d5c605b60](https://github.com/MariaDB/server/commit/0d5c605b60)\
  2017-04-10 13:09:20 +0300
  * MW-369 Fixed test MW-369D, recorded MW-369C, MW-369D
* [Revision #396770fb67](https://github.com/MariaDB/server/commit/396770fb67)\
  2017-04-07 00:18:30 +0300
  * Refs: MW-369
    * changed parent row key type to S(hared), when FK child table is being updated or deleted
* [Revision #7c07f456a1](https://github.com/MariaDB/server/commit/7c07f456a1)\
  2017-04-06 09:23:30 +0300
  * MW-369 MTR tests for foreign key conflicts
* [Revision #41fac0a54c](https://github.com/MariaDB/server/commit/41fac0a54c)\
  2017-04-05 12:08:06 +0300
  * Refs: MW-369
    * changed insert for a FK child table to take exclusive lock on FK parent table
* [Revision #cc3bee92b6](https://github.com/MariaDB/server/commit/cc3bee92b6)\
  2017-04-05 12:08:06 +0300
  * Refs: MW-369
    * changed insert for a FK child table to take exclusive lock on FK parent table
* [Revision #20c21152db](https://github.com/MariaDB/server/commit/20c21152db)\
  2017-04-05 10:51:42 +0300
  * Refs: MW-369
    * added MTR test, which causes a crash in slave applying, due to FK constraint violation
    * mtr test is not deterministic, but can surface the crash, at least in my laptop
* [Revision #7f66fcc3fc](https://github.com/MariaDB/server/commit/7f66fcc3fc)\
  2017-03-27 02:22:18 -0700
  * Galera MTR Tests: Fortify galera\_ist\_restart\_joiner.test - remove DDLs, fix sync point handling
* [Revision #ea197c0f7d](https://github.com/MariaDB/server/commit/ea197c0f7d)\
  2017-03-24 02:15:01 -0700
  * Galera MTR Tests: Stability fixes
* [Revision #a7f010a343](https://github.com/MariaDB/server/commit/a7f010a343)\
  2017-03-14 12:41:22 -0700
  * Galera MTR Tests: Test case for [GAL-501](https://github.com/codership/galera/issues/501) Improved URI parsing for IPv6 addresses
* [Revision #f81d9ef108](https://github.com/MariaDB/server/commit/f81d9ef108)\
  2017-03-13 22:45:42 +0100
  * MW-86 Removed unnecessary wsrep\_sync\_wait before processing SQLCOM\_REPLACE
* [Revision #df5b90e18b](https://github.com/MariaDB/server/commit/df5b90e18b)\
  2017-03-13 08:52:09 -0700
  * Galera MTR Tests: Extend test for MW-86 with additional SHOW commands (part #2)
* [Revision #fae7d85600](https://github.com/MariaDB/server/commit/fae7d85600)\
  2017-03-13 08:45:42 -0700
  * Galera MTR Tests: Extend test for MW-86 with additional SHOW commands
* [Revision #62cd7553d9](https://github.com/MariaDB/server/commit/62cd7553d9)\
  2017-03-13 15:35:04 +0100
  * MW-86 Additional wsrep\_sync\_wait coverage
* [Revision #e2ccbe1aea](https://github.com/MariaDB/server/commit/e2ccbe1aea)\
  2017-03-13 02:30:01 -0700
  * Galera MTR Tests: Tests for MW-360 DROP TABLE containing temporary tables results in binlog divergence
* [Revision #795713405b](https://github.com/MariaDB/server/commit/795713405b)\
  2017-03-10 09:25:24 +0200
  * Refs: MW-360
    * fix for regression with galera\_toi\_ddl\_nonconflicting test
* [Revision #3d4708554c](https://github.com/MariaDB/server/commit/3d4708554c)\
  2017-03-08 15:29:31 +0100
  * MW-86 MTR test: check that SHOW commands no longer obey wsrep\_sync\_wait = 1
* [Revision #f20b21a29a](https://github.com/MariaDB/server/commit/f20b21a29a)\
  2017-03-08 13:11:57 +0100
  * MW-86 Adjust MTR tests for changes to wsrep\_sync\_wait
* [Revision #7a219b6f23](https://github.com/MariaDB/server/commit/7a219b6f23)\
  2017-03-08 13:08:21 +0100
  * MW-86 Add separate wsrep\_sync\_wait bitmask value for SHOW commands
* [Revision #afbaa5c697](https://github.com/MariaDB/server/commit/afbaa5c697)\
  2017-03-07 23:47:22 -0800
  * Galera MTR Tests: Tests for MW-366 - improved support for IPv6
* [Revision #83664e21e4](https://github.com/MariaDB/server/commit/83664e21e4)\
  2017-03-03 20:28:27 +0000
  * MW-366 Improved support for IPv6 networks - made mysqld and SST scripts to recognize \[]-escaped IPv6 addresses - pulled in latest Percona and MariaDB updates to SST scripts - instruct netcat and socat in wsrep\_sst\_xtrabackup-v2 to listen on IPv6 socket via sockopt parameter in the \[sst] section of my.cnf
* [Revision #5108deded5](https://github.com/MariaDB/server/commit/5108deded5)\
  2017-03-08 01:35:05 -0800
  * Galera MTR Tests: Stability fixes
* [Revision #6da41e17d8](https://github.com/MariaDB/server/commit/6da41e17d8)\
  2017-03-02 17:53:16 +0100
  * MW-365 Do not load/dump innodb buffer pool with wsrep\_recover
* [Revision #3ef3c467ad](https://github.com/MariaDB/server/commit/3ef3c467ad)\
  2017-03-02 17:53:16 +0100
  * MW-365 Do not load/dump innodb buffer pool with wsrep\_recover
* [Revision #9064263703](https://github.com/MariaDB/server/commit/9064263703)\
  2017-03-03 03:51:07 -0800
  * Galera MTR Tests: Test for [GAL-491](https://github.com/codership/galera/issues/491): Progress output for IST
* [Revision #5fb1260365](https://github.com/MariaDB/server/commit/5fb1260365)\
  2017-03-01 11:27:33 +0200
  * Refs: MW-360, white space fix
* [Revision #ba3d26d3ab](https://github.com/MariaDB/server/commit/ba3d26d3ab)\
  2017-02-26 23:48:32 +0200
  * Refs: MW-360
    * fixes required in pull request review
* [Revision #0ddf32c840](https://github.com/MariaDB/server/commit/0ddf32c840)\
  2017-01-16 16:10:37 +0200
  * refs: MW-322
    * generating fake trx id for CTAS, requires trx\_sys mutex protection to be safe for concurrent CTAS processors
* [Revision #790a8274cd](https://github.com/MariaDB/server/commit/790a8274cd)\
  2017-02-22 23:10:36 +0200
  * Refs: MW-360
    * reverted WSREP\_TO\_ISOLATION macros back to original form
* [Revision #04c6b03c9b](https://github.com/MariaDB/server/commit/04c6b03c9b)\
  2017-02-20 23:29:25 +0200
  * Refs: MW-360
    * merged relevant parts of DROP TABLE query splitting from mysql-wsrep-features
* [Revision #a754387a09](https://github.com/MariaDB/server/commit/a754387a09)\
  2017-02-17 10:25:05 +0200
  * Refs: MW-360, fix for compiler warning
* [Revision #7ef2d5aa5b](https://github.com/MariaDB/server/commit/7ef2d5aa5b)\
  2017-02-16 23:19:10 +0200
  * Refs: MW-360
    * splitting DROP TABLE query in separate DROP commands for temporary and real tables
    * not replicating temporary table DROP command
    * using wsrep\_sidno GTID group only for innodb table drop command part all this follows more or less the logic of how mysql wants to split drop table list
* [Revision #364b15c090](https://github.com/MariaDB/server/commit/364b15c090)\
  2017-02-08 23:36:34 +0100
  * MW-336 Avoid slave threads leaking
* [Revision #7af44d7aa0](https://github.com/MariaDB/server/commit/7af44d7aa0)\
  2017-02-08 06:56:00 -0800
  * Galera MTR Tests: MW-359 Include include/have\_innodb.inc part of include/galera\_cluster.inc
* [Revision #77f5b188d3](https://github.com/MariaDB/server/commit/77f5b188d3)\
  2017-02-06 18:07:21 +0100
  * MW-357 Reset thd->wsrep\_apply\_toi regardless of applier exiting
* [Revision #391b1af0fb](https://github.com/MariaDB/server/commit/391b1af0fb)\
  2017-08-10 13:09:27 +0300
  * [MDEV-13471](https://jira.mariadb.org/browse/MDEV-13471): Test failure on innodb.log\_file\_size,4k
* Merge [Revision #56b03e308f](https://github.com/MariaDB/server/commit/56b03e308f) 2017-08-09 08:56:11 +0300 - Merge tag 'mariadb-10.0.32' into 10.0-galera
* [Revision #4f40f87c48](https://github.com/MariaDB/server/commit/4f40f87c48)\
  2017-06-02 11:33:35 -0400
  * bump the VERSION

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
