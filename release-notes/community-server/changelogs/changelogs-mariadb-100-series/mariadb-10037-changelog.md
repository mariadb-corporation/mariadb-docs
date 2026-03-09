# MariaDB 10.0.37 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.37)[Release Notes](../../old-releases/10.0/10.0.37.md)[Changelog](mariadb-10037-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 1 Nov 2018

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.37.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #a737135ae3](https://github.com/MariaDB/server/commit/a737135ae3)\
  2018-10-30 18:15:58 +0200
  * List of unstable tests for 10.0.37 release
* [Revision #6ced789186](https://github.com/MariaDB/server/commit/6ced789186)\
  2018-10-30 13:29:19 +0200
  * [MDEV-12023](https://jira.mariadb.org/browse/MDEV-12023) Assertion failure sym\_node->table != NULL on startup
* [Revision #f4b8b6b9a3](https://github.com/MariaDB/server/commit/f4b8b6b9a3)\
  2018-10-29 21:44:38 +0100
  * [MDEV-15919](https://jira.mariadb.org/browse/MDEV-15919) lower\_case\_table\_names does not behave as expected
* [Revision #f30148a740](https://github.com/MariaDB/server/commit/f30148a740)\
  2018-10-29 14:51:29 +0100
  * CONNECT: bintar compilation failure on Mac OS X
* [Revision #cd0734d6bd](https://github.com/MariaDB/server/commit/cd0734d6bd)\
  2018-10-28 10:55:46 +0100
  * after-merge: enable tests
* [Revision #70e567f576](https://github.com/MariaDB/server/commit/70e567f576)\
  2018-05-07 22:43:43 +0200
  * Squashed commit of connect/10.0:
* [Revision #411a2540ee](https://github.com/MariaDB/server/commit/411a2540ee)\
  2018-10-28 10:09:58 +0100
  * CONNECT: don't mix bundled zlib and system libxml2
* Merge [Revision #3e2394a56b](https://github.com/MariaDB/server/commit/3e2394a56b) 2018-10-28 10:06:23 +0100 - Merge branch 'merge/merge-perfschema-5.6' into 10.0
* [Revision #a9a0d0c372](https://github.com/MariaDB/server/commit/a9a0d0c372)\
  2018-10-27 21:06:41 +0200
  * 5.6.42
* Merge [Revision #1bad8f9df3](https://github.com/MariaDB/server/commit/1bad8f9df3) 2018-10-28 10:04:36 +0100 - Merge branch 'merge/merge-xtradb-5.6' into 10.0
* [Revision #bbcb173436](https://github.com/MariaDB/server/commit/bbcb173436)\
  2018-10-27 20:53:19 +0200
  * 5.6.41-84.1
* Merge [Revision #87d852f102](https://github.com/MariaDB/server/commit/87d852f102) 2018-10-28 01:10:15 +0200 - Merge branch 'merge/merge-innodb-5.6' into 10.0
* [Revision #da34c7de5d](https://github.com/MariaDB/server/commit/da34c7de5d)\
  2018-10-27 21:05:16 +0200
  * 5.6.42
* Merge [Revision #37ab7e4596](https://github.com/MariaDB/server/commit/37ab7e4596) 2018-10-27 20:46:18 +0200 - Merge branch '5.5' into 10.0
* [Revision #30c3d6db32](https://github.com/MariaDB/server/commit/30c3d6db32)\
  2018-10-24 16:28:46 +0300
  * [MDEV-17533](https://jira.mariadb.org/browse/MDEV-17533) Merge new release of InnoDB 5.6.42 to 10.0
* [Revision #2549f98289](https://github.com/MariaDB/server/commit/2549f98289)\
  2018-10-24 16:01:18 +0300
  * [MDEV-17532](https://jira.mariadb.org/browse/MDEV-17532) Performance\_schema reports wrong directory for the temporary files of ALTER TABLE…ALGORITHM=INPLACE
* [Revision #5dd3b52f95](https://github.com/MariaDB/server/commit/5dd3b52f95)\
  2018-10-24 11:04:38 +0300
  * [MDEV-17531](https://jira.mariadb.org/browse/MDEV-17531) Crash in RENAME TABLE with FOREIGN KEY and FULLTEXT INDEX
* [Revision #642394197e](https://github.com/MariaDB/server/commit/642394197e)\
  2018-10-19 19:10:45 +0400
  * Remove unused code.
* [Revision #4ac85d6fd7](https://github.com/MariaDB/server/commit/4ac85d6fd7)\
  2018-10-18 22:48:28 +0400
  * [MDEV-14815](https://jira.mariadb.org/browse/MDEV-14815) - Server crash or AddressSanitizer errors or valgrind warnings in thr\_lock / has\_old\_lock upon FLUSH TABLES
* [Revision #8e716138ce](https://github.com/MariaDB/server/commit/8e716138ce)\
  2018-10-17 08:26:13 +0400
  * [MDEV-17257](https://jira.mariadb.org/browse/MDEV-17257) Server crashes in Item::field\_type\_for\_temporal\_comparison or in get\_datetime\_value on SELECT with YEAR field and IN
* [Revision #853dee854c](https://github.com/MariaDB/server/commit/853dee854c)\
  2018-10-03 12:22:03 +0300
  * [MDEV-17358](https://jira.mariadb.org/browse/MDEV-17358) my\_reverse\_bits() is incorrect due to UB
* [Revision #bebe24b03b](https://github.com/MariaDB/server/commit/bebe24b03b)\
  2017-12-26 14:38:45 +0400
  * [MDEV-11071](https://jira.mariadb.org/browse/MDEV-11071) - Assertion \`thd->transaction.stmt.is\_empty()' failed in Locked\_tables\_list::unlock\_locked\_tables
* [Revision #1dacd5f299](https://github.com/MariaDB/server/commit/1dacd5f299)\
  2018-10-16 13:02:50 +0530
  * [MDEV-12547](https://jira.mariadb.org/browse/MDEV-12547): InnoDB FULLTEXT index has too strict innodb\_ft\_result\_cache\_limit max limit
* [Revision #3c5f6aa21c](https://github.com/MariaDB/server/commit/3c5f6aa21c)\
  2018-10-14 10:30:23 -0700
  * [MDEV-17020](https://jira.mariadb.org/browse/MDEV-17020): Assertion \`length > 0' failed in ptr\_compare upon ORDER BY with bad conversion
* [Revision #34f8a4071e](https://github.com/MariaDB/server/commit/34f8a4071e)\
  2018-10-15 13:22:18 +0400
  * [MDEV-17064](https://jira.mariadb.org/browse/MDEV-17064) LIKE function has error behavior on the fields in which the collation is xxx\_unicode\_xx
* [Revision #ae3fe14c17](https://github.com/MariaDB/server/commit/ae3fe14c17)\
  2018-10-15 10:57:36 +0400
  * Test for [MDEV-13119](https://jira.mariadb.org/browse/MDEV-13119) and [MDEV-13120](https://jira.mariadb.org/browse/MDEV-13120)
* [Revision #cb4877a503](https://github.com/MariaDB/server/commit/cb4877a503)\
  2018-10-15 10:48:55 +0400
  * [MDEV-14322](https://jira.mariadb.org/browse/MDEV-14322) main.type\_datetime failed in buildbot, results mismatch
* [Revision #4d07e6c12d](https://github.com/MariaDB/server/commit/4d07e6c12d)\
  2018-10-13 18:47:16 +0300
  * Disabled storage engine tests using LOCK with MERGE engine
* [Revision #0f178e7cae](https://github.com/MariaDB/server/commit/0f178e7cae)\
  2018-10-12 13:51:37 +0300
  * Fix typo in 5936d43afb6ad5a75d9eed17eb39e8c00a08a684
* [Revision #b7918a6d38](https://github.com/MariaDB/server/commit/b7918a6d38)\
  2018-10-11 20:36:59 +0200
  * fix test suite after [MDEV-15438](https://jira.mariadb.org/browse/MDEV-15438)
* [Revision #5936d43afb](https://github.com/MariaDB/server/commit/5936d43afb)\
  2018-02-02 14:24:36 +1100
  * threadpool\_size can contribute to the wanted\_files
* [Revision #00ddc8bc7c](https://github.com/MariaDB/server/commit/00ddc8bc7c)\
  2018-10-09 18:06:22 +0100
  * [MDEV-17413](https://jira.mariadb.org/browse/MDEV-17413) Crash in my\_malloc\_size\_cb\_func() during shutdown with forceful connection close.
* [Revision #bd21904357](https://github.com/MariaDB/server/commit/bd21904357)\
  2018-10-07 10:19:19 -0700
  * [MDEV-17382](https://jira.mariadb.org/browse/MDEV-17382) Hash join algorithm should not be used to join materialized derived table / view by equality
* [Revision #a660a5ed42](https://github.com/MariaDB/server/commit/a660a5ed42)\
  2018-10-01 14:33:48 +0300
  * Correct a typo in a comment
* [Revision #1144acbcbd](https://github.com/MariaDB/server/commit/1144acbcbd)\
  2018-09-22 15:21:20 +0200
  * tokudb: create and destroy TOKUDB\_SHARE::\_open\_tables\_mutex dynamically
* [Revision #3a9276bad3](https://github.com/MariaDB/server/commit/3a9276bad3)\
  2018-09-22 15:19:40 +0200
  * sanitize tokudb locking macros
* Merge [Revision #a4131c51f5](https://github.com/MariaDB/server/commit/a4131c51f5) 2018-09-21 18:17:32 +0400 - Merge remote-tracking branch 'origin/5.5' into bb-10.0-bar
* Merge [Revision #acc97298e5](https://github.com/MariaDB/server/commit/acc97298e5) 2018-09-21 14:41:11 +0300 - Merge 5.5 into 10.0
* [Revision #d533f6d58b](https://github.com/MariaDB/server/commit/d533f6d58b)\
  2018-09-21 09:32:17 +0400
  * After-merge cleanup: adjust the test to work in 10.0
* Merge [Revision #80bcb05b24](https://github.com/MariaDB/server/commit/80bcb05b24) 2018-09-21 08:37:42 +0400 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #327b271721](https://github.com/MariaDB/server/commit/327b271721)\
  2018-09-07 14:50:10 +0400
  * [MDEV-14410](https://jira.mariadb.org/browse/MDEV-14410) - Assertion \`table->pos\_in\_locked\_tables == null || table->pos\_in\_locked\_tables->table == table' failed in mark\_used\_tables\_as\_free\_for\_reuse
* [Revision #b7944343dd](https://github.com/MariaDB/server/commit/b7944343dd)\
  2018-09-10 14:26:11 +0200
  * Update contributors
* [Revision #3a4242fd57](https://github.com/MariaDB/server/commit/3a4242fd57)\
  2018-09-06 20:41:28 +0200
  * TokuDB: Don't free P\_S instrumented mutexes after exit()
* Merge [Revision #d527bf5390](https://github.com/MariaDB/server/commit/d527bf5390) 2018-09-06 21:04:56 +0200 - Merge branch 'merge-tokudb-5.6' into 10.0
* [Revision #a816eac92a](https://github.com/MariaDB/server/commit/a816eac92a)\
  2018-09-03 14:22:54 +0200
  * 5.6.41-84.1
* [Revision #0ccba62db3](https://github.com/MariaDB/server/commit/0ccba62db3)\
  2018-09-05 19:47:37 +0200
  * [MDEV-16465](https://jira.mariadb.org/browse/MDEV-16465) Invalid (old?) table or database name or hang in ha\_innobase::delete\_table and log semaphore wait upon concurrent DDL with foreign keys
* [Revision #4cf75706b3](https://github.com/MariaDB/server/commit/4cf75706b3)\
  2018-09-05 17:14:20 +0400
  * [MDEV-16757](https://jira.mariadb.org/browse/MDEV-16757) Memory leak after adding manually min/max statistical data for blob column
* [Revision #09bc99fac9](https://github.com/MariaDB/server/commit/09bc99fac9)\
  2018-07-19 11:10:41 +0200
  * cleanup: remove extra/rpl\_tests/rpl\_foreign\_key.test
* [Revision #d831cefb43](https://github.com/MariaDB/server/commit/d831cefb43)\
  2018-07-19 01:18:14 +0200
  * [MDEV-16465](https://jira.mariadb.org/browse/MDEV-16465) Invalid (old?) table or database name or hang in ha\_innobase::delete\_table and log semaphore wait upon concurrent DDL with foreign keys
* [Revision #9180e8666b](https://github.com/MariaDB/server/commit/9180e8666b)\
  2018-07-19 01:03:14 +0200
  * [MDEV-16465](https://jira.mariadb.org/browse/MDEV-16465) Invalid (old?) table or database name or hang in ha\_innobase::delete\_table and log semaphore wait upon concurrent DDL with foreign keys
* [Revision #e81f101dac](https://github.com/MariaDB/server/commit/e81f101dac)\
  2018-07-17 17:12:05 +0200
  * create a reusable function that tells what FK actions can write
* [Revision #dd74332d2c](https://github.com/MariaDB/server/commit/dd74332d2c)\
  2018-07-18 19:04:51 +0200
  * [MDEV-12669](https://jira.mariadb.org/browse/MDEV-12669) Circular foreign keys cause a loop and OOM upon LOCK TABLE
* [Revision #710093ccb0](https://github.com/MariaDB/server/commit/710093ccb0)\
  2018-09-04 09:49:00 +0200
  * compilation failure
* [Revision #64a23c1c8a](https://github.com/MariaDB/server/commit/64a23c1c8a)\
  2018-07-17 16:56:40 +0200
  * extend prelocking to FK-accessed tables
* [Revision #3b365fa829](https://github.com/MariaDB/server/commit/3b365fa829)\
  2016-11-10 16:10:41 +0100
  * cleanup: sp\_head::add\_used\_tables\_to\_table\_list()
* [Revision #22bcfa011a](https://github.com/MariaDB/server/commit/22bcfa011a)\
  2018-07-17 14:35:04 +0200
  * cleanup: FOREIGN\_KEY\_INFO
* Merge [Revision #b9bc3c2463](https://github.com/MariaDB/server/commit/b9bc3c2463) 2018-09-03 10:57:02 +0200 - Merge branch '5.5' into 10.0
* [Revision #b3c320bb0b](https://github.com/MariaDB/server/commit/b3c320bb0b)\
  2018-08-29 04:39:42 +0530
  * [MDEV-16995](https://jira.mariadb.org/browse/MDEV-16995): ER\_CANT\_CREATE\_GEOMETRY\_OBJECT encountered for a query with optimizer\_use\_condition\_selectivity>=3
* [Revision #a9c09c95bd](https://github.com/MariaDB/server/commit/a9c09c95bd)\
  2018-08-28 21:59:11 +0530
  * [MDEV-15306](https://jira.mariadb.org/browse/MDEV-15306): Wrong/Unexpected result with the value optimizer\_use\_condition\_selectivity set to 4
* Merge [Revision #5fb251642e](https://github.com/MariaDB/server/commit/5fb251642e) 2018-08-27 12:22:27 +0300 - Commit the [MDEV-17023](https://jira.mariadb.org/browse/MDEV-17023) fix with the correct number
* [Revision #51fb163b6d](https://github.com/MariaDB/server/commit/51fb163b6d)\
  2018-08-25 18:23:34 +0300
  * Fix clang warning of mismatched new\[] and delete\[]
* [Revision #6b22cc4ae0](https://github.com/MariaDB/server/commit/6b22cc4ae0)\
  2018-06-30 21:23:21 +1000
  * connect engine: GetStringUTFChars takes pointer arg
* [Revision #4ba6327f95](https://github.com/MariaDB/server/commit/4ba6327f95)\
  2018-04-16 21:11:58 +0000
  * Fix typo in `--srcdir` option in echo message status of mysql\_install\_db
* [Revision #490e220ad2](https://github.com/MariaDB/server/commit/490e220ad2)\
  2018-08-24 21:03:22 +0300
  * [MDEV-17067](https://jira.mariadb.org/browse/MDEV-17067) Server crash in write\_block\_record
* [Revision #f195286a3e](https://github.com/MariaDB/server/commit/f195286a3e)\
  2018-08-24 18:08:56 +0300
  * [MDEV-17021](https://jira.mariadb.org/browse/MDEV-17021) Server crash or assertion \`length <= column->length' failure in write\_block\_record
* [Revision #0cafc13164](https://github.com/MariaDB/server/commit/0cafc13164)\
  2018-08-24 01:59:02 +0530
  * [MDEV-17073](https://jira.mariadb.org/browse/MDEV-17073): Crash during read\_histogram\_for\_table with optimizer\_use\_condition\_selectivity set to 4
* [Revision #69d7bfd970](https://github.com/MariaDB/server/commit/69d7bfd970)\
  2018-08-24 01:59:02 +0530
  * [MDEV-17023](https://jira.mariadb.org/browse/MDEV-17023): Crash during read\_histogram\_for\_table with optimizer\_use\_condition\_selectivity set to 4
* [Revision #7d8d37c31d](https://github.com/MariaDB/server/commit/7d8d37c31d)\
  2018-08-23 16:01:58 +0530
  * [MDEV-17039](https://jira.mariadb.org/browse/MDEV-17039): Query plan changes when we use GROUP BY optimization with optimizer\_use\_condition\_selectivity=4 and use\_stat\_tables= PREFERABLY
* Merge [Revision #bcc677bb72](https://github.com/MariaDB/server/commit/bcc677bb72) 2018-08-15 16:48:13 +0200 - Merge branch '5.5' into 10.0
* [Revision #b62ac16185](https://github.com/MariaDB/server/commit/b62ac16185)\
  2018-08-15 15:21:37 +0300
  * [MDEV-6439](https://jira.mariadb.org/browse/MDEV-6439): Server crashes in Explain\_union::print\_explain with explain in slow log, tis620 charset
* [Revision #9dfef6e29b](https://github.com/MariaDB/server/commit/9dfef6e29b)\
  2018-08-03 11:22:20 +0300
  * Fix -Wclass-memaccess warnings in InnoDB,XtraDB
* [Revision #b963cbaf4b](https://github.com/MariaDB/server/commit/b963cbaf4b)\
  2018-08-03 11:49:49 +0300
  * Follow-up fix to [MDEV-16865](https://jira.mariadb.org/browse/MDEV-16865): InnoDB fts\_query() ignores KILL
* [Revision #90b66c1699](https://github.com/MariaDB/server/commit/90b66c1699)\
  2018-08-01 12:09:33 -0400
  * bump the VERSION
* [Revision #a7f84f09bf](https://github.com/MariaDB/server/commit/a7f84f09bf)\
  2018-07-31 16:12:38 +0300
  * [MDEV-16865](https://jira.mariadb.org/browse/MDEV-16865) InnoDB fts\_query() ignores KILL
* [Revision #b3e95086e1](https://github.com/MariaDB/server/commit/b3e95086e1)\
  2018-07-31 14:29:05 +0300
  * Fix function pointer type mismatch

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
