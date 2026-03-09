# MariaDB 10.4.13 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.13/)[Release Notes](../../old-releases/10.4/10.4.13.md)[Changelog](mariadb-10413-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 12 May 2020

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.13.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.23](../changelogs-mariadb-10-3-series/mariadb-10323-changelog.md)
* [Revision #1b18cddaa2](https://github.com/MariaDB/server/commit/1b18cddaa2)\
  2020-05-09 22:20:04 +0300
  * List of unstable tests for 10.4.13 release
* Merge [Revision #f5844e7c4b](https://github.com/MariaDB/server/commit/f5844e7c4b) 2020-05-09 20:25:21 +0200 - Merge branch '10.3' into 10.4
* [Revision #5b0df7433d](https://github.com/MariaDB/server/commit/5b0df7433d)\
  2020-05-08 12:31:33 +0200
  * WolfSSL fixes
* [Revision #403dc759d0](https://github.com/MariaDB/server/commit/403dc759d0)\
  2020-05-05 18:10:53 +0200
  * Update WolfSSL
* [Revision #8d85715d50](https://github.com/MariaDB/server/commit/8d85715d50)\
  2020-05-06 15:37:19 +0300
  * [MDEV-21794](https://jira.mariadb.org/browse/MDEV-21794): Optimizer flag rowid\_filter leads to long query
* [Revision #0253ea7f22](https://github.com/MariaDB/server/commit/0253ea7f22)\
  2020-02-19 17:50:30 +0100
  * [MDEV-19650](https://jira.mariadb.org/browse/MDEV-19650): Privilege bug on [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/)
* Merge [Revision #2c3c851d2c](https://github.com/MariaDB/server/commit/2c3c851d2c) 2020-05-05 20:33:10 +0300 - Merge 10.3 into 10.4
* [Revision #474290540a](https://github.com/MariaDB/server/commit/474290540a)\
  2020-05-05 14:20:47 +0300
  * [MDEV-22465](https://jira.mariadb.org/browse/MDEV-22465): DROP indexed COLUMN is wrongly claimed to be ALGORITHM=INSTANT
* [Revision #69925c0d2e](https://github.com/MariaDB/server/commit/69925c0d2e)\
  2020-05-05 22:41:10 +0900
  * [MDEV-20502](https://jira.mariadb.org/browse/MDEV-20502) Queries against spider tables return wrong values for columns following constant declarations.
* [Revision #37a01aceca](https://github.com/MariaDB/server/commit/37a01aceca)\
  2020-05-05 09:48:03 +0300
  * [MDEV-21489](https://jira.mariadb.org/browse/MDEV-21489) : wsrep\_cluster\_conf\_id has wrong value
* [Revision #1ed98782e7](https://github.com/MariaDB/server/commit/1ed98782e7)\
  2020-05-04 22:06:31 +0300
  * [MDEV-22452](https://jira.mariadb.org/browse/MDEV-22452): Fix cmake -DWITH\_WSREP=OFF
* [Revision #50f3a38e89](https://github.com/MariaDB/server/commit/50f3a38e89)\
  2020-05-04 18:24:01 +0300
  * Add an end marker to a test
* [Revision #5e7e7153b4](https://github.com/MariaDB/server/commit/5e7e7153b4)\
  2020-05-04 18:19:13 +0300
  * [MDEV-22452](https://jira.mariadb.org/browse/MDEV-22452): Missing call to wsrep\_commit\_ordered in trx\_t::commit()
* [Revision #f5cff8980a](https://github.com/MariaDB/server/commit/f5cff8980a)\
  2020-05-04 17:21:46 +0200
  * [MDEV-22453](https://jira.mariadb.org/browse/MDEV-22453): Missing suite.pm for galera\_3nodes\_sr (#1522)
* [Revision #a1eb151327](https://github.com/MariaDB/server/commit/a1eb151327)\
  2020-05-04 19:11:02 +0530
  * [MDEV-22410](https://jira.mariadb.org/browse/MDEV-22410) Change the error when table schema mismatch happens
* [Revision #d002ec2c87](https://github.com/MariaDB/server/commit/d002ec2c87)\
  2020-05-04 11:06:40 +0300
  * [MDEV-21489](https://jira.mariadb.org/browse/MDEV-21489) : wsrep\_cluster\_conf\_id has wrong value
* [Revision #7f03a93348](https://github.com/MariaDB/server/commit/7f03a93348)\
  2020-04-29 20:22:18 +0530
  * [MDEV-22160](https://jira.mariadb.org/browse/MDEV-22160): SIGSEGV in st\_join\_table::save\_explain\_data on SELECT
* [Revision #7bc6735736](https://github.com/MariaDB/server/commit/7bc6735736)\
  2020-04-29 01:13:52 +0300
  * [MDEV-22401](https://jira.mariadb.org/browse/MDEV-22401): Optimizer trace: multi-component range is not printed correctly
* [Revision #5ba2aa1ddc](https://github.com/MariaDB/server/commit/5ba2aa1ddc)\
  2020-04-29 14:54:36 +0300
  * [MDEV-7962](https://jira.mariadb.org/browse/MDEV-7962): Remove one more wsrep\_on()
* [Revision #cfbbf5424b](https://github.com/MariaDB/server/commit/cfbbf5424b)\
  2020-04-29 11:50:03 +0300
  * [MDEV-7962](https://jira.mariadb.org/browse/MDEV-7962): Follow-up fix for 10.4
* Merge [Revision #0632b8034b](https://github.com/MariaDB/server/commit/0632b8034b) 2020-04-29 09:05:15 +0300 - Merge 10.3 into 10.4
* [Revision #503fd2115b](https://github.com/MariaDB/server/commit/503fd2115b)\
  2020-04-27 15:05:18 +0200
  * fix the test for windows
* Merge [Revision #b63446984c](https://github.com/MariaDB/server/commit/b63446984c) 2020-04-27 17:38:17 +0300 - Merge 10.3 into 10.4
* [Revision #6dab094fbd](https://github.com/MariaDB/server/commit/6dab094fbd)\
  2020-04-25 12:49:47 +0200
  * [MDEV-20257](https://jira.mariadb.org/browse/MDEV-20257) Server crashes in Grant\_table\_base::init\_read\_record upon crash-upgrade
* [Revision #a58b2b3b2b](https://github.com/MariaDB/server/commit/a58b2b3b2b)\
  2020-04-22 19:59:48 +0200
  * [MDEV-21928](https://jira.mariadb.org/browse/MDEV-21928) ALTER USER doesn't remove excess authentication plugins from mysql.global\_priv
* [Revision #2144dc1ff2](https://github.com/MariaDB/server/commit/2144dc1ff2)\
  2020-04-21 18:45:12 +0200
  * more verbose tests
* [Revision #b976b9bfc3](https://github.com/MariaDB/server/commit/b976b9bfc3)\
  2020-04-21 18:40:15 +0200
  * [MDEV-21244](https://jira.mariadb.org/browse/MDEV-21244) mysql\_upgrade creating empty global\_priv table
* [Revision #c2db9397c7](https://github.com/MariaDB/server/commit/c2db9397c7)\
  2020-04-21 18:07:11 +0200
  * [MDEV-18565](https://jira.mariadb.org/browse/MDEV-18565) Galera mtr-suite fails if galera library is not installed
* [Revision #81511b4776](https://github.com/MariaDB/server/commit/81511b4776)\
  2020-04-26 15:13:26 +0300
  * Fixed shutdown crash in Aria that affects debug binaries
* [Revision #a19782522b](https://github.com/MariaDB/server/commit/a19782522b)\
  2020-04-24 17:13:04 +0300
  * [MDEV-14735](https://jira.mariadb.org/browse/MDEV-14735): Fix -Wunused-const-variable
* [Revision #be42004d3d](https://github.com/MariaDB/server/commit/be42004d3d)\
  2020-04-24 17:12:11 +0300
  * Fixup d1c3342d07dbf56dc355b9e61efc3938807bcb3a for --embedded
* [Revision #edd38b50f6](https://github.com/MariaDB/server/commit/edd38b50f6)\
  2020-04-24 16:01:10 +0300
  * [MDEV-7962](https://jira.mariadb.org/browse/MDEV-7962) wsrep\_on() takes 0.14% in OLTP RO
* [Revision #2c39f69d34](https://github.com/MariaDB/server/commit/2c39f69d34)\
  2020-04-24 15:25:39 +0300
  * [MDEV-22203](https://jira.mariadb.org/browse/MDEV-22203): WSREP\_ON is unnecessarily expensive WITH\_WSREP=OFF
* [Revision #93475aff8d](https://github.com/MariaDB/server/commit/93475aff8d)\
  2020-04-21 13:46:05 +0300
  * [MDEV-22203](https://jira.mariadb.org/browse/MDEV-22203): WSREP\_ON is unnecessarily expensive to evaluate
* [Revision #9398c3dfa5](https://github.com/MariaDB/server/commit/9398c3dfa5)\
  2020-04-23 14:24:52 +0300
  * Fixed memory leak if Aria didn't start
* [Revision #d1c3342d07](https://github.com/MariaDB/server/commit/d1c3342d07)\
  2020-04-23 11:08:52 +0300
  * Fixed default\_storage\_engine.test
* Merge [Revision #88cf6f1c7f](https://github.com/MariaDB/server/commit/88cf6f1c7f) 2020-04-22 18:18:51 +0300 - Merge 10.3 into 10.4
* [Revision #498c5e2be1](https://github.com/MariaDB/server/commit/498c5e2be1)\
  2020-04-22 04:44:28 +0900
  * [MDEV-21884](https://jira.mariadb.org/browse/MDEV-21884) MariaDB with Spider crashes on a query
* [Revision #632b1deb67](https://github.com/MariaDB/server/commit/632b1deb67)\
  2020-04-18 08:06:13 +0300
  * [MDEV-21025](https://jira.mariadb.org/browse/MDEV-21025) Server crashes on START TRANSACTION after INSERT IGNORE (#1489)
* [Revision #68ceb4b460](https://github.com/MariaDB/server/commit/68ceb4b460)\
  2020-04-15 23:19:10 +0900
  * [MDEV-20502](https://jira.mariadb.org/browse/MDEV-20502) Queries against spider tables return wrong values for columns following constant declarations.
* [Revision #00db9c6b40](https://github.com/MariaDB/server/commit/00db9c6b40)\
  2020-04-17 01:49:46 +0900
  * [MDEV-21884](https://jira.mariadb.org/browse/MDEV-21884) MariaDB with Spider crashes on a query
* [Revision #c79051e587](https://github.com/MariaDB/server/commit/c79051e587)\
  2020-03-03 16:50:48 +0200
  * [MDEV-22271](https://jira.mariadb.org/browse/MDEV-22271) Excessive stack memory usage due to WSREP\_LOG
* Merge [Revision #af91266498](https://github.com/MariaDB/server/commit/af91266498) 2020-04-16 12:12:26 +0300 - Merge 10.3 into 10.4
* [Revision #5679a2b6b3](https://github.com/MariaDB/server/commit/5679a2b6b3)\
  2020-04-15 21:23:12 +0400
  * Shrink my\_atomic.h and my\_cpu.h scope
* [Revision #4bd9f82a8f](https://github.com/MariaDB/server/commit/4bd9f82a8f)\
  2020-04-15 20:38:25 +0400
  * slave\_open\_temp\_tables to Atomic\_counter
* [Revision #10cdf5230d](https://github.com/MariaDB/server/commit/10cdf5230d)\
  2020-04-15 19:11:49 +0400
  * my\_file\_opened to my\_atomic
* [Revision #5876ed9e5b](https://github.com/MariaDB/server/commit/5876ed9e5b)\
  2020-04-15 18:35:48 +0400
  * Relay\_log\_info::executed\_entries to Atomic\_counter
* [Revision #c1bdf62452](https://github.com/MariaDB/server/commit/c1bdf62452)\
  2020-02-27 01:53:46 +0200
  * [MDEV-18768](https://jira.mariadb.org/browse/MDEV-18768): Rename auth\_socket to unix\_socket on upgrades from MySQL
* [Revision #edc3899d97](https://github.com/MariaDB/server/commit/edc3899d97)\
  2020-03-31 18:43:10 +0200
  * [MDEV-22051](https://jira.mariadb.org/browse/MDEV-22051): Protocol::end\_statement(): Assertion \`0' failed on Galera node upon DDL attempt with conflicting lock
* [Revision #476966b3fb](https://github.com/MariaDB/server/commit/476966b3fb)\
  2020-04-08 09:58:08 +0300
  * [MDEV-21535](https://jira.mariadb.org/browse/MDEV-21535) Unnecessarily large ha\_innobase::records\_in\_range() scans
* [Revision #b6eabce139](https://github.com/MariaDB/server/commit/b6eabce139)\
  2020-03-16 13:07:52 +0200
  * Travis-CI: Shorten deb build log to keep it under 4 MB
* [Revision #28604c349b](https://github.com/MariaDB/server/commit/28604c349b)\
  2020-04-05 18:55:15 +0300
  * Travis-CI: Add missing build dependency dh-exec
* [Revision #aa7f2578fc](https://github.com/MariaDB/server/commit/aa7f2578fc)\
  2020-04-03 23:55:48 +0300
  * [MDEV-21471](https://jira.mariadb.org/browse/MDEV-21471) ER\_CRASHED\_ON\_USAGE upon UPDATE FOR PORTION on Aria table
* [Revision #198af54bb9](https://github.com/MariaDB/server/commit/198af54bb9)\
  2020-04-03 23:55:48 +0300
  * [MDEV-20494](https://jira.mariadb.org/browse/MDEV-20494) Fix wrongly ignored error status
* [Revision #76063c2a13](https://github.com/MariaDB/server/commit/76063c2a13)\
  2020-04-03 23:55:48 +0300
  * [MDEV-20494](https://jira.mariadb.org/browse/MDEV-20494) ER\_NOT\_FORM\_FILE or assertion upon adding partition to period table
* [Revision #a219006636](https://github.com/MariaDB/server/commit/a219006636)\
  2020-04-02 11:50:47 +0300
  * [MDEV-22014](https://jira.mariadb.org/browse/MDEV-22014): Rowid Filtering is not displayed well in the optimizer trace
* [Revision #bdcecfa22c](https://github.com/MariaDB/server/commit/bdcecfa22c)\
  2020-03-16 15:03:00 +0100
  * [MDEV-22021](https://jira.mariadb.org/browse/MDEV-22021): Galera database could get inconsistent with rollback to savepoint
* Merge [Revision #e2f1f88fa6](https://github.com/MariaDB/server/commit/e2f1f88fa6) 2020-03-30 14:50:23 +0300 - Merge 10.3 into 10.4
* [Revision #9eae063e79](https://github.com/MariaDB/server/commit/9eae063e79)\
  2020-03-27 02:24:49 +0400
  * num\_worker\_threads my\_atomic to Atomic\_counter
* [Revision #e91a3ea732](https://github.com/MariaDB/server/commit/e91a3ea732)\
  2020-03-27 02:13:41 +0400
  * shutdown\_group\_count my\_atomic to Atomic\_counter
* [Revision #ed8bf7c98f](https://github.com/MariaDB/server/commit/ed8bf7c98f)\
  2020-03-27 02:08:53 +0400
  * next\_timeout\_check my\_atomic to std::atomic
* [Revision #ba679ae52f](https://github.com/MariaDB/server/commit/ba679ae52f)\
  2020-03-26 19:19:41 +0400
  * Fix for rpl\_start\_stop\_slave failure
* [Revision #af4b2ae858](https://github.com/MariaDB/server/commit/af4b2ae858)\
  2020-03-26 15:01:44 +0300
  * [MDEV-21887](https://jira.mariadb.org/browse/MDEV-21887): federatedx crashes on SELECT ... INTO query in select\_handler code
* [Revision #1c8de231a3](https://github.com/MariaDB/server/commit/1c8de231a3)\
  2020-03-25 17:27:42 +0400
  * dequeued\_count my\_atomic to Atomic\_counter
* [Revision #98fc6b923f](https://github.com/MariaDB/server/commit/98fc6b923f)\
  2020-03-25 19:45:37 +0100
  * [MDEV-20388](https://jira.mariadb.org/browse/MDEV-20388) : disable inline assembly in WolfSSL if MSAN is on
* [Revision #3a1075b93e](https://github.com/MariaDB/server/commit/3a1075b93e)\
  2020-03-25 18:16:36 +0100
  * [MDEV-19519](https://jira.mariadb.org/browse/MDEV-19519) mysql\_install\_db.exe doesn't set password\_last\_changed for newly created password
* [Revision #497a4169df](https://github.com/MariaDB/server/commit/497a4169df)\
  2020-03-25 22:40:14 +0900
  * change from to for adding defaults-file in Spider tests
* [Revision #efc97eff31](https://github.com/MariaDB/server/commit/efc97eff31)\
  2020-03-24 09:35:19 +0200
  * Fix clang -Wsometimes-uninitialized
* [Revision #8b647d6960](https://github.com/MariaDB/server/commit/8b647d6960)\
  2020-03-24 09:27:09 +0200
  * [MDEV-22020](https://jira.mariadb.org/browse/MDEV-22020): Fix spider/bugfix.return\_found\_rows\_update
* [Revision #f7599f4799](https://github.com/MariaDB/server/commit/f7599f4799)\
  2020-03-23 13:13:20 +0530
  * [MDEV-21792](https://jira.mariadb.org/browse/MDEV-21792) Server aborts upon attempt to create foreign key on spatial field
* [Revision #81f700015e](https://github.com/MariaDB/server/commit/81f700015e)\
  2020-03-21 19:49:46 +0400
  * Cleanup my\_atomic.h includes
* [Revision #6acddd5367](https://github.com/MariaDB/server/commit/6acddd5367)\
  2020-03-21 19:46:49 +0400
  * global\_query\_id: my\_atomic to Atomic\_counter
* [Revision #62687801ff](https://github.com/MariaDB/server/commit/62687801ff)\
  2020-03-21 18:36:31 +0400
  * tc\_active\_instances: my\_atomic to std::atomic
* [Revision #3b3f931570](https://github.com/MariaDB/server/commit/3b3f931570)\
  2020-03-21 17:59:43 +0400
  * Discovery counters: my\_atomic to Atomic\_counter
* [Revision #a39d92ca57](https://github.com/MariaDB/server/commit/a39d92ca57)\
  2020-03-21 17:36:38 +0400
  * gtid\_pos\_table: my\_atomic to std::atomic
* [Revision #4d9977e5ff](https://github.com/MariaDB/server/commit/4d9977e5ff)\
  2020-03-21 15:52:24 +0400
  * default\_gtid\_pos\_table: my\_atomic to std::atomic
* [Revision #9394cc8914](https://github.com/MariaDB/server/commit/9394cc8914)\
  2020-03-21 08:17:28 +0100
  * [MDEV-21675](https://jira.mariadb.org/browse/MDEV-21675): Data inconsistency after multirow insert rollback (#1474)
* Merge [Revision #bd3c8f47cd](https://github.com/MariaDB/server/commit/bd3c8f47cd) 2020-03-20 22:06:55 +0200 - Merge 10.3 into 10.4
* [Revision #d529389358](https://github.com/MariaDB/server/commit/d529389358)\
  2020-03-20 15:38:37 +0200
  * [MDEV-21979](https://jira.mariadb.org/browse/MDEV-21979) Galera test sporadic failure on galera\_3nodes.galera\_pc\_weight (#1473)
* [Revision #ec5e48be4b](https://github.com/MariaDB/server/commit/ec5e48be4b)\
  2020-03-20 13:23:24 +0200
  * Test fixes for galera\_3nodes suite.
* [Revision #b6e3cfde26](https://github.com/MariaDB/server/commit/b6e3cfde26)\
  2020-03-19 12:39:26 +0200
  * Fix test case name and add debug sync include.
* Merge [Revision #1de104a4d6](https://github.com/MariaDB/server/commit/1de104a4d6) 2020-03-19 12:25:49 +0200 - Merge branch 'codership-10.4-[MDEV-19966](https://jira.mariadb.org/browse/MDEV-19966)' into 10.4
* Merge [Revision #91baaf450f](https://github.com/MariaDB/server/commit/91baaf450f) 2020-03-19 12:25:15 +0200 - Merge branch '10.4-[MDEV-19966](https://jira.mariadb.org/browse/MDEV-19966)' of [mariadb-server](https://github.com/codership/mariadb-server) into codership-10.4-[MDEV-19966](https://jira.mariadb.org/browse/MDEV-19966)
* [Revision #d87c16be79](https://github.com/MariaDB/server/commit/d87c16be79)\
  2020-02-24 17:04:43 +0100
  * [MDEV-20616](https://jira.mariadb.org/browse/MDEV-20616): MariaDB-Galera 10.4.8 | Transaction aborted | Sig 6 Shutdown
* Merge [Revision #6a63457639](https://github.com/MariaDB/server/commit/6a63457639) 2020-03-18 22:15:21 +0200 - Merge branch '10.3' into 10.4
* [Revision #dbde95d912](https://github.com/MariaDB/server/commit/dbde95d912)\
  2020-03-17 19:13:17 +0200
  * Updated aria\_pack to support transactional tables
* [Revision #517f659e6d](https://github.com/MariaDB/server/commit/517f659e6d)\
  2020-03-17 12:37:56 +0200
  * Fixed that caused failure in --ps binlog\_encryption.rpl\_gtid\_basic
* [Revision #a2d24def8c](https://github.com/MariaDB/server/commit/a2d24def8c)\
  2020-03-13 15:55:32 +0200
  * [MDEV-21932](https://jira.mariadb.org/browse/MDEV-21932) A fast plan with ROR index-merge is ignored when 'index\_merge\_sort\_union=off'
* [Revision #1242eb3d32](https://github.com/MariaDB/server/commit/1242eb3d32)\
  2020-03-13 15:28:42 +0200
  * Removed double records\_in\_range calls from multi\_range\_read\_info\_const
* [Revision #96b472c0ae](https://github.com/MariaDB/server/commit/96b472c0ae)\
  2020-03-17 00:56:49 +0100
  * [MDEV-18439](https://jira.mariadb.org/browse/MDEV-18439)\
    Windows builds should have core\_file=1 by default
* [Revision #097e2f9d0a](https://github.com/MariaDB/server/commit/097e2f9d0a)\
  2020-03-16 16:51:35 +0200
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188): Fix clang 10 -Wimplicit-int-float-conversion
* [Revision #b7f0644710](https://github.com/MariaDB/server/commit/b7f0644710)\
  2020-03-16 16:32:11 +0200
  * [MDEV-5313](https://jira.mariadb.org/browse/MDEV-5313): Fix GCC 10 -Wenum-conversion
* Merge [Revision #e5e95a287e](https://github.com/MariaDB/server/commit/e5e95a287e) 2020-03-16 16:24:36 +0200 - Merge 10.3 into 10.4
* [Revision #2b3f6ab417](https://github.com/MariaDB/server/commit/2b3f6ab417)\
  2020-03-13 18:15:57 +0100
  * [MDEV-21599](https://jira.mariadb.org/browse/MDEV-21599) plugins.server\_audit fails sporadically in buildbot
* Merge [Revision #b7362d5fbc](https://github.com/MariaDB/server/commit/b7362d5fbc) 2020-03-11 14:28:24 +0100 - Merge branch '10.3' into 10.4
* Merge [Revision #b8c0e49670](https://github.com/MariaDB/server/commit/b8c0e49670) 2020-03-11 13:27:10 +0100 - Merge commit '10.3' into 10.4
* [Revision #5c6c4b1395](https://github.com/MariaDB/server/commit/5c6c4b1395)\
  2020-03-09 14:53:35 +0200
  * Fixes for previous not-complete-push
* [Revision #c037cdadf4](https://github.com/MariaDB/server/commit/c037cdadf4)\
  2020-03-05 14:10:03 +0200
  * Added keyread\_time() to HEAP
* [Revision #a24d0926b9](https://github.com/MariaDB/server/commit/a24d0926b9)\
  2020-03-06 14:21:20 +0200
  * Second stage of optimizer\_trace optimizations
* [Revision #940fcbe73b](https://github.com/MariaDB/server/commit/940fcbe73b)\
  2020-03-06 10:33:11 +0200
  * Improved speed of optimizer trace
* [Revision #1ad8693a6f](https://github.com/MariaDB/server/commit/1ad8693a6f)\
  2020-02-28 15:44:56 +0000
  * [MDEV-21841](https://jira.mariadb.org/browse/MDEV-21841) CONV() function doesn't truncate its output to 21 when uses default charset.
* [Revision #e837a358b6](https://github.com/MariaDB/server/commit/e837a358b6)\
  2020-02-28 14:01:27 +0200
  * [MDEV-21693](https://jira.mariadb.org/browse/MDEV-21693): Fix clang -Winconsistent-missing-override
* [Revision #f56dd0a12d](https://github.com/MariaDB/server/commit/f56dd0a12d)\
  2020-02-28 14:29:05 +0530
  * [MDEV-21693](https://jira.mariadb.org/browse/MDEV-21693) ALGORITHM=INSTANT does not work for partitioned tables
* [Revision #a17a327f11](https://github.com/MariaDB/server/commit/a17a327f11)\
  2020-02-26 13:58:08 +0100
  * [MDEV-21684](https://jira.mariadb.org/browse/MDEV-21684): mysqld crash with signal 11 when renaming table+max\_statement\_time
* [Revision #e637355156](https://github.com/MariaDB/server/commit/e637355156)\
  2020-02-20 13:35:19 +0300
  * [MDEV-21610](https://jira.mariadb.org/browse/MDEV-21610) Different query results from 10.4.11 to 10.4.12
* [Revision #adcfea710f](https://github.com/MariaDB/server/commit/adcfea710f)\
  2020-02-19 14:57:47 +0300
  * Fix compile failure, compare\_key\_parts in handler shadowed by MyRocks
* [Revision #2fb881df1d](https://github.com/MariaDB/server/commit/2fb881df1d)\
  2020-02-18 22:49:42 -0800
  * [MDEV-21610](https://jira.mariadb.org/browse/MDEV-21610) Different query results from 10.4.11 to 10.4.12
* [Revision #df07e00a81](https://github.com/MariaDB/server/commit/df07e00a81)\
  2019-10-14 18:13:02 +0300
  * [MDEV-20726](https://jira.mariadb.org/browse/MDEV-20726) InnoDB: Assertion failure in file data0type.cc line 67
* [Revision #7ccc1710a0](https://github.com/MariaDB/server/commit/7ccc1710a0)\
  2019-10-14 16:20:16 +0300
  * cleanup: key parts comparison
* [Revision #5a42a114fd](https://github.com/MariaDB/server/commit/5a42a114fd)\
  2020-02-17 13:56:41 +0200
  * Add missing files.
* [Revision #1a73b995fc](https://github.com/MariaDB/server/commit/1a73b995fc)\
  2020-01-31 08:05:41 +0200
  * [MDEV-21601](https://jira.mariadb.org/browse/MDEV-21601) : Cleanup Galera disabled tests
* [Revision #4eb4d07856](https://github.com/MariaDB/server/commit/4eb4d07856)\
  2020-02-14 08:20:52 +0200
  * Fix Galera test galera\_as\_slave\_ctas.
* [Revision #9ab171edd6](https://github.com/MariaDB/server/commit/9ab171edd6)\
  2020-02-13 17:06:02 +0200
  * [MDEV-21420](https://jira.mariadb.org/browse/MDEV-21420) : Galera test failure on galera.mysql-wsrep#33
* [Revision #38414b2bd0](https://github.com/MariaDB/server/commit/38414b2bd0)\
  2020-02-13 14:13:12 +0200
  * [MDEV-21514](https://jira.mariadb.org/browse/MDEV-21514) : Galera test failure on galera.galera\_wan\_restart\_sst on Azure
* [Revision #2cff542892](https://github.com/MariaDB/server/commit/2cff542892)\
  2019-11-28 17:37:57 +0500
  * [MDEV-21140](https://jira.mariadb.org/browse/MDEV-21140) Make galera\_recovery.sh work with fs.protected\_regular = 1 (#1417)
* [Revision #ba3e9d0adb](https://github.com/MariaDB/server/commit/ba3e9d0adb)\
  2020-02-13 12:38:15 +0200
  * [MDEV-18180](https://jira.mariadb.org/browse/MDEV-18180) : Galera test failure on galera.galera\_concurrent\_ctas
* [Revision #7002948bc5](https://github.com/MariaDB/server/commit/7002948bc5)\
  2020-02-12 11:29:37 +0200
  * [MDEV-21517](https://jira.mariadb.org/browse/MDEV-21517) : Galera test galera\_sr.GCF-561 failure: Result length mismatch
* [Revision #a3f3d40b33](https://github.com/MariaDB/server/commit/a3f3d40b33)\
  2020-02-13 08:32:59 +0200
  * [MDEV-21421](https://jira.mariadb.org/browse/MDEV-21421) : Galera test sporadic failure on galera.galera\_as\_slave\_gtid\_myisam: Result length mismatch
* [Revision #5007633c10](https://github.com/MariaDB/server/commit/5007633c10)\
  2020-01-31 08:05:41 +0200
  * [MDEV-21601](https://jira.mariadb.org/browse/MDEV-21601) : Cleanup Galera disabled tests
* [Revision #9f71804110](https://github.com/MariaDB/server/commit/9f71804110)\
  2020-02-13 23:50:17 +0300
  * [MDEV-21628](https://jira.mariadb.org/browse/MDEV-21628): Index condition pushdown condition ... not used with BKA
* [Revision #8eb0384556](https://github.com/MariaDB/server/commit/8eb0384556)\
  2020-02-14 20:32:46 +1100
  * mysys: remove windac my\_security\_attr\_create (#1391)
* [Revision #c400a73d7a](https://github.com/MariaDB/server/commit/c400a73d7a)\
  2020-02-13 16:26:47 +0300
  * micro optimization: avoid std::string copy
* [Revision #1394216e3d](https://github.com/MariaDB/server/commit/1394216e3d)\
  2020-02-07 23:43:52 +0400
  * [MDEV-21669](https://jira.mariadb.org/browse/MDEV-21669) InnoDB: Table ... contains indexes inside InnoDB, which is different from the number of indexes defined in the MariaDB
* [Revision #c5e00fea10](https://github.com/MariaDB/server/commit/c5e00fea10)\
  2019-11-01 19:18:47 +0400
  * [MDEV-20867](https://jira.mariadb.org/browse/MDEV-20867) - Perform careful review of "Server crashes with BACKUP STAGE and FLUSH TABLE table\_name"
* Merge [Revision #646d1ec83a](https://github.com/MariaDB/server/commit/646d1ec83a) 2020-02-11 14:40:35 +0100 - Merge branch '10.3' into 10.4
* [Revision #c1eaa385ff](https://github.com/MariaDB/server/commit/c1eaa385ff)\
  2020-02-03 18:20:24 +0100
  * [MDEV-21616](https://jira.mariadb.org/browse/MDEV-21616): Server crash when using "SET STATEMENT max\_statement\_time=0 FOR desc xxx" lead to collapse
* [Revision #2acc6f2d95](https://github.com/MariaDB/server/commit/2acc6f2d95)\
  2020-02-05 11:12:10 +0200
  * [MDEV-21658](https://jira.mariadb.org/browse/MDEV-21658) Error on online ADD PRIMARY KEY after instant DROP/reorder
* [Revision #a56f78243e](https://github.com/MariaDB/server/commit/a56f78243e)\
  2020-02-04 16:31:52 +0200
  * [MDEV-21645](https://jira.mariadb.org/browse/MDEV-21645) SIGSEGV in innobase\_get\_computed\_value
* [Revision #46386661a2](https://github.com/MariaDB/server/commit/46386661a2)\
  2020-02-04 09:00:36 +0200
  * [MDEV-20625](https://jira.mariadb.org/browse/MDEV-20625) : MariaDB asserting when enabling wsrep\_on
* [Revision #93278ee8ad](https://github.com/MariaDB/server/commit/93278ee8ad)\
  2019-10-08 10:47:30 +0200
  * [MDEV-20625](https://jira.mariadb.org/browse/MDEV-20625): MariaDB asserting when enabling wsrep=on
* [Revision #574354a6b2](https://github.com/MariaDB/server/commit/574354a6b2)\
  2020-02-03 19:45:30 +0200
  * [MDEV-20625](https://jira.mariadb.org/browse/MDEV-20625) : MariaDB asserting when enabling wsrep\_on
* [Revision #eed6d215f1](https://github.com/MariaDB/server/commit/eed6d215f1)\
  2019-10-09 21:16:31 +0530
  * [MDEV-20001](https://jira.mariadb.org/browse/MDEV-20001) Potential dangerous regression: INSERT INTO >=100 rows fail for myisam table with HASH indexes
* [Revision #b615d275b8](https://github.com/MariaDB/server/commit/b615d275b8)\
  2020-02-02 15:13:29 +0300
  * [MDEV-17798](https://jira.mariadb.org/browse/MDEV-17798) System variable system\_versioning\_asof accepts wrong values (10.4)
* [Revision #5a6023cf6f](https://github.com/MariaDB/server/commit/5a6023cf6f)\
  2019-10-08 17:35:09 +0530
  * [MDEV-18791](https://jira.mariadb.org/browse/MDEV-18791) Wrong error upon creating Aria table with long index on BLOB
* [Revision #1b414c0313](https://github.com/MariaDB/server/commit/1b414c0313)\
  2020-02-01 15:06:12 +0200
  * [MDEV-21256](https://jira.mariadb.org/browse/MDEV-21256) after-merge fix: Use std::atomic
* [Revision #4b291588bb](https://github.com/MariaDB/server/commit/4b291588bb)\
  2020-02-01 14:53:41 +0200
  * [MDEV-19845](https://jira.mariadb.org/browse/MDEV-19845): Make my\_cpu.h self-contained
* [Revision #d87b725eeb](https://github.com/MariaDB/server/commit/d87b725eeb)\
  2020-01-31 09:54:43 +0200
  * [MDEV-17844](https://jira.mariadb.org/browse/MDEV-17844) recs\_off\_validate() fails in page\_zip\_write\_trx\_id\_and\_roll\_ptr()
* [Revision #88bcc7f21c](https://github.com/MariaDB/server/commit/88bcc7f21c)\
  2020-01-31 09:17:12 +0200
  * Fixup cd2c0e013ccb5f9b009743dfd7188585a539d9b5
* [Revision #a10a94b262](https://github.com/MariaDB/server/commit/a10a94b262)\
  2020-01-31 11:47:17 +0530
  * Empty commit
* [Revision #4d61f1247a](https://github.com/MariaDB/server/commit/4d61f1247a)\
  2020-01-29 16:41:04 +0200
  * Fixed compiler warnings from gcc 7.4.1
* [Revision #cd2c0e013c](https://github.com/MariaDB/server/commit/cd2c0e013c)\
  2020-01-29 17:31:08 +0200
  * Added error output wsrep\_print\_version
* Merge [Revision #bc89105496](https://github.com/MariaDB/server/commit/bc89105496) 2020-01-28 09:42:21 +0100 - Merge branch 'bb-10.4-release' into 10.4
* [Revision #1ef8d0b45d](https://github.com/MariaDB/server/commit/1ef8d0b45d)\
  2020-01-27 15:12:05 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
