# MariaDB 10.1.36 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.36)[Release Notes](../../old-releases/10.1/10.1.36.md)[Changelog](mariadb-10136-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 7 Sep 2018

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.36.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #b1d72f1722](https://github.com/MariaDB/server/commit/b1d72f1722)\
  2018-09-07 16:49:39 +0300
  * Updated list of unstable tests for 10.1.36 release
* Merge [Revision #db947b7599](https://github.com/MariaDB/server/commit/db947b7599) 2018-09-07 15:25:27 +0200 - Merge branch '10.0-galera' into 10.1
* [Revision #5d90717cc9](https://github.com/MariaDB/server/commit/5d90717cc9)\
  2018-08-04 11:28:25 +0300
  * Add wsrep.cnf
* [Revision #ea0356e1ad](https://github.com/MariaDB/server/commit/ea0356e1ad)\
  2018-08-03 16:43:32 +0300
  * Add galera library dependency directly to test case.
* [Revision #9808e23a7a](https://github.com/MariaDB/server/commit/9808e23a7a)\
  2018-08-03 13:44:30 +0300
  * MariaDB adjustments.
* [Revision #3f0cd66a2b](https://github.com/MariaDB/server/commit/3f0cd66a2b)\
  2018-07-16 09:42:53 +0200
  * Also include InnoDB undo tablespaces in rsync sst
* [Revision #62e290923e](https://github.com/MariaDB/server/commit/62e290923e)\
  2018-07-16 09:41:37 +0200
  * Put one filter per line in wsrep\_sst\_rsync.sh
* [Revision #639bd1c71f](https://github.com/MariaDB/server/commit/639bd1c71f)\
  2018-07-06 11:53:43 +0200
  * galera#505 mtr test
* [Revision #1d414d9491](https://github.com/MariaDB/server/commit/1d414d9491)\
  2018-03-01 17:07:07 +0200
  * codership/galera#501 Check cluster weight in galera\_pc\_weight test
* [Revision #40f6bcb856](https://github.com/MariaDB/server/commit/40f6bcb856)\
  2018-08-02 20:35:44 +0300
  * Add missing WSREP(thd) condition and remove unnecessary DBUG\_RETURN.
* Merge [Revision #9b29bda0d6](https://github.com/MariaDB/server/commit/9b29bda0d6) 2018-08-02 13:13:21 +0300 - Merge remote-tracking branch 'origin/5.5-galera' into 10.0-galera
* [Revision #e88e26b424](https://github.com/MariaDB/server/commit/e88e26b424)\
  2018-05-23 14:13:11 +0200
  * Follow up to previous commit for codership/mysql-wsrep#332
* [Revision #4d2b552369](https://github.com/MariaDB/server/commit/4d2b552369)\
  2018-05-22 16:45:27 +0200
  * Fix FK constraint violation in applier, after ALTER TABLE ADD FK
* Merge [Revision #b286a9f823](https://github.com/MariaDB/server/commit/b286a9f823) 2018-08-01 10:58:38 +0300 - Merge tag 'mariadb-5.5.61' into 5.5-galera
* [Revision #33e39f0682](https://github.com/MariaDB/server/commit/33e39f0682)\
  2018-05-03 10:23:36 -0400
  * bump the VERSION
* Merge [Revision #c5a8583b31](https://github.com/MariaDB/server/commit/c5a8583b31) 2018-08-02 11:44:02 +0300 - Merge tag 'mariadb-10.0.36' into 10.0-galera
* [Revision #c863159c32](https://github.com/MariaDB/server/commit/c863159c32)\
  2018-07-24 14:54:50 +0300
  * [MDEV-16799](https://jira.mariadb.org/browse/MDEV-16799): Test wsrep.variables crash at sql\_class.cc:639 thd\_get\_ha\_data
* [Revision #f99fe68b4f](https://github.com/MariaDB/server/commit/f99fe68b4f)\
  2018-07-19 21:05:36 +0300
  * Fix compile error.
* [Revision #c09d54924a](https://github.com/MariaDB/server/commit/c09d54924a)\
  2018-07-19 15:13:31 +0300
  * [MDEV-10564](https://jira.mariadb.org/browse/MDEV-10564): Galera `wsrep_debug` patch logs MySQL user credentials
* Merge [Revision #71e0ba4ae6](https://github.com/MariaDB/server/commit/71e0ba4ae6) 2018-07-19 07:04:40 +0300 - Merge pull request #645 from grooverdan/10.0-wsrep\_sst\_common\_bashism
* [Revision #6aa22eaf62](https://github.com/MariaDB/server/commit/6aa22eaf62)\
  2018-03-07 14:36:40 +1100
  * wsrep\_sst\_common: fix per shellcheck
* [Revision #cf648afd5b](https://github.com/MariaDB/server/commit/cf648afd5b)\
  2018-06-14 15:12:13 +0200
  * fix galera sst tests
* Merge [Revision #f95d26b4d3](https://github.com/MariaDB/server/commit/f95d26b4d3) 2018-09-07 11:52:05 +0200 - Merge branch '10.1' into bb-10.1-release
* [Revision #285969e1c6](https://github.com/MariaDB/server/commit/285969e1c6)\
  2018-09-07 11:27:15 +0300
  * Fix result file for wsrep.variables, for some reason had too new galera library used.
* [Revision #62dbf4f18d](https://github.com/MariaDB/server/commit/62dbf4f18d)\
  2018-09-06 23:36:53 +0200
  * post merge
* Merge [Revision #31081593aa](https://github.com/MariaDB/server/commit/31081593aa) 2018-09-06 22:45:19 +0200 - Merge branch '11.0' into 10.1
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
* [Revision #43c393ff47](https://github.com/MariaDB/server/commit/43c393ff47)\
  2018-09-03 11:10:30 +0300
  * [MDEV-16682](https://jira.mariadb.org/browse/MDEV-16682) Assertion \`(buff\[7] & 7) == HEAD\_PAGE' failed
* [Revision #796d54df11](https://github.com/MariaDB/server/commit/796d54df11)\
  2018-08-30 15:18:35 +0200
  * [MDEV-16957](https://jira.mariadb.org/browse/MDEV-16957): Server crashes in Field\_iterator\_natural\_join::next upon 2nd execution of SP
* [Revision #42f09adab6](https://github.com/MariaDB/server/commit/42f09adab6)\
  2018-08-30 13:45:27 +0300
  * [MDEV-16682](https://jira.mariadb.org/browse/MDEV-16682) Assertion \`(buff\[7] & 7) == HEAD\_PAGE' failed
* Merge [Revision #e560f2f342](https://github.com/MariaDB/server/commit/e560f2f342) 2018-08-24 12:33:05 +0300 - Merge pull request #846 from shinnok/bb-5.5-mtr-shm
* [Revision #1b1b941385](https://github.com/MariaDB/server/commit/1b1b941385)\
  2018-08-16 16:39:50 +0300
  * [MDEV-17022](https://jira.mariadb.org/browse/MDEV-17022): check if mtr --mem location is writeable
* [Revision #064ba8cc9f](https://github.com/MariaDB/server/commit/064ba8cc9f)\
  2017-11-17 08:00:32 +0800
  * item\_cmp\_type: simplier for a faster codepath
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
* [Revision #b0026e33af](https://github.com/MariaDB/server/commit/b0026e33af)\
  2018-09-06 18:55:57 +0300
  * Disable failing galera test for now.
* [Revision #fba683c069](https://github.com/MariaDB/server/commit/fba683c069)\
  2018-08-27 12:03:02 +0300
  * [MDEV-17062](https://jira.mariadb.org/browse/MDEV-17062): Test failure on galera.MW-336 [MDEV-17058](https://jira.mariadb.org/browse/MDEV-17058): Test failure on wsrep.variables [MDEV-17060](https://jira.mariadb.org/browse/MDEV-17060): Test failure on galera.galera\_var\_slave\_threads
* Merge [Revision #653038ccad](https://github.com/MariaDB/server/commit/653038ccad) 2018-09-06 14:10:29 +0300 - Merge pull request #855 from tempesta-tech/sysprg/10.1-[MDEV-10756](https://jira.mariadb.org/browse/MDEV-10756)
* [Revision #c11fb374b5](https://github.com/MariaDB/server/commit/c11fb374b5)\
  2018-08-27 16:10:20 +0200
  * [MDEV-10756](https://jira.mariadb.org/browse/MDEV-10756): wsrep\_sst\_xtrabackup-v2 does not support innodb\_data\_home\_dir
* [Revision #6695fcead3](https://github.com/MariaDB/server/commit/6695fcead3)\
  2018-09-04 18:50:06 +0300
  * Galera test case cleanups.
* [Revision #b44b9f71bd](https://github.com/MariaDB/server/commit/b44b9f71bd)\
  2018-06-26 12:56:19 +0300
  * [MDEV-15436](https://jira.mariadb.org/browse/MDEV-15436): If log\_bin and log\_bin\_index is different SST with rsync fails.
* [Revision #4caf3e08a8](https://github.com/MariaDB/server/commit/4caf3e08a8)\
  2018-09-04 20:21:57 +0300
  * Add [MDEV-11080](https://jira.mariadb.org/browse/MDEV-11080), [MDEV-16709](https://jira.mariadb.org/browse/MDEV-16709) tests for the [MDEV-13333](https://jira.mariadb.org/browse/MDEV-13333) fix
* [Revision #a6246cab16](https://github.com/MariaDB/server/commit/a6246cab16)\
  2018-09-03 10:27:36 +0200
  * fix failures of innodb\_plugin tests in --embedded
* [Revision #c272754740](https://github.com/MariaDB/server/commit/c272754740)\
  2018-08-31 13:45:49 +0200
  * [MDEV-15792](https://jira.mariadb.org/browse/MDEV-15792) Fix mtr to be able to wait for >1 exited mysqld
* [Revision #1d98255f61](https://github.com/MariaDB/server/commit/1d98255f61)\
  2018-03-19 08:41:33 +0100
  * [MDEV-15792](https://jira.mariadb.org/browse/MDEV-15792) Fix mtr to be able to wait for >1 exited mysqld
* [Revision #82bb01588d](https://github.com/MariaDB/server/commit/82bb01588d)\
  2018-08-31 15:01:53 +0200
  * run binlog.binlog\_stm\_binlog test in non-debug builds
* [Revision #8bee7c16c8](https://github.com/MariaDB/server/commit/8bee7c16c8)\
  2018-08-31 01:22:51 +0200
  * compiler warnings (clang 4.0.1 on i386)
* [Revision #aec54fb938](https://github.com/MariaDB/server/commit/aec54fb938)\
  2018-08-31 00:56:10 +0200
  * [MDEV-9627](https://jira.mariadb.org/browse/MDEV-9627) clang builds fail on i386
* [Revision #64d4181f0c](https://github.com/MariaDB/server/commit/64d4181f0c)\
  2018-06-29 14:46:41 +0200
  * Fix TokuDB's check for -Wno-address-of-packed-member
* Merge [Revision #34e026f35a](https://github.com/MariaDB/server/commit/34e026f35a) 2018-09-03 08:37:22 +0300 - Merge pull request #859 from grooverdan/10.1-galera\_new\_cluster-unsed-vars
* [Revision #eda88e60fb](https://github.com/MariaDB/server/commit/eda88e60fb)\
  2018-09-03 09:53:05 +1000
  * galera\_new\_cluster.sh: unused variables
* [Revision #63ad6a9e1a](https://github.com/MariaDB/server/commit/63ad6a9e1a)\
  2018-09-02 09:24:33 +0400
  * [MDEV-15890](https://jira.mariadb.org/browse/MDEV-15890) Strange error message if you try to FLUSH TABLES after LOCK TABLES .
* [Revision #288212f489](https://github.com/MariaDB/server/commit/288212f489)\
  2018-08-31 15:30:44 +0300
  * Disable failing Galera tests.
* [Revision #f693170c75](https://github.com/MariaDB/server/commit/f693170c75)\
  2018-08-31 13:16:31 +0300
  * [MDEV-16647](https://jira.mariadb.org/browse/MDEV-16647) InnoDB fails to drop large temporary table on disconnect
* [Revision #3b5d3cd68e](https://github.com/MariaDB/server/commit/3b5d3cd68e)\
  2018-08-31 11:41:59 +0300
  * Revert [MDEV-9519](https://jira.mariadb.org/browse/MDEV-9519) due to regressions
* [Revision #c933970974](https://github.com/MariaDB/server/commit/c933970974)\
  2018-08-30 15:57:22 +0400
  * [MDEV-16665](https://jira.mariadb.org/browse/MDEV-16665) ed25519 describes itself as 1.0-alpha even though it's not alpha.
* [Revision #2ad51a0bd8](https://github.com/MariaDB/server/commit/2ad51a0bd8)\
  2018-08-30 14:51:15 +0400
  * [MDEV-17095](https://jira.mariadb.org/browse/MDEV-17095) pam\_user\_map module throws syntax error if group name contains backslash.
* [Revision #104089e182](https://github.com/MariaDB/server/commit/104089e182)\
  2018-08-29 19:30:03 +0300
  * [MDEV-15512](https://jira.mariadb.org/browse/MDEV-15512) - Fix sh parse error when \[sst] config value has spaces.
* [Revision #6c588c92a9](https://github.com/MariaDB/server/commit/6c588c92a9)\
  2018-08-09 13:22:30 +0200
  * [MDEV-14927](https://jira.mariadb.org/browse/MDEV-14927): Missing man pages
* Merge [Revision #f4454a35fc](https://github.com/MariaDB/server/commit/f4454a35fc) 2018-08-28 13:48:43 +0300 - Merge pull request #539 from grooverdan/10.1-wsrep\_sst\_rsync\_read\_MYSQL\_BASE\_VERSION\_config
* Merge [Revision #a0a9958098](https://github.com/MariaDB/server/commit/a0a9958098) 2018-02-04 22:20:52 +1100 - Merge branch '10.1' into 10.1-wsrep\_sst\_rsync\_read\_MYSQL\_BASE\_VERSION\_config
* [Revision #67f3fb1bc5](https://github.com/MariaDB/server/commit/67f3fb1bc5)\
  2018-01-02 14:26:48 +1100
  * galera\_recovery: misses reading default configuration groups
* [Revision #7dc5183317](https://github.com/MariaDB/server/commit/7dc5183317)\
  2018-01-02 13:40:05 +1100
  * wsrep\_sst\_rsync: read correct configuration sections
* [Revision #cded083a37](https://github.com/MariaDB/server/commit/cded083a37)\
  2018-08-27 22:00:14 +0300
  * [MDEV-15797](https://jira.mariadb.org/browse/MDEV-15797) Assertion \`thd->killed != 0' failed in ha\_maria::enable\_indexes
* Merge [Revision #b87b8c1344](https://github.com/MariaDB/server/commit/b87b8c1344) 2018-08-21 15:58:09 +0300 - Merge pull request #828 from tempesta-tech/sysprg/10.1-[MDEV-10754](https://jira.mariadb.org/browse/MDEV-10754)
* [Revision #4ff7f14fef](https://github.com/MariaDB/server/commit/4ff7f14fef)\
  2018-08-17 15:54:55 +0200
  * Fixes of the base patch for compatibility with the 10.1 branch
* [Revision #36832711c1](https://github.com/MariaDB/server/commit/36832711c1)\
  2018-08-13 10:40:47 +0200
  * Reverting changes made to support the mtr under the root
* [Revision #7e8ed15b95](https://github.com/MariaDB/server/commit/7e8ed15b95)\
  2018-08-09 02:24:12 +0000
  * Fixes after review and correction of the problems caused by the fact that during the SST innodb plugin is not yet initialized, as well as problems with running tests from the root user (not directly related to the [MDEV-10754](https://jira.mariadb.org/browse/MDEV-10754)).
* Merge [Revision #6d5b71e02a](https://github.com/MariaDB/server/commit/6d5b71e02a) 2018-08-08 15:47:57 +0200 - Merge branch '10.1' of [server](https://github.com/MariaDB/server) into sysprg/10.1-[MDEV-10754](https://jira.mariadb.org/browse/MDEV-10754)
* [Revision #46d5e1f2fd](https://github.com/MariaDB/server/commit/46d5e1f2fd)\
  2018-07-26 15:42:06 +0200
  * [MDEV-10754](https://jira.mariadb.org/browse/MDEV-10754) wsrep\_sst\_rsync does not support innodb\_data\_home\_dir
* [Revision #dc7c080369](https://github.com/MariaDB/server/commit/dc7c080369)\
  2018-08-21 12:01:44 +0300
  * [MDEV-17026](https://jira.mariadb.org/browse/MDEV-17026) Assertion srv\_undo\_sources || ... failed on slow shutdown
* [Revision #45dbd47026](https://github.com/MariaDB/server/commit/45dbd47026)\
  2018-08-21 11:56:50 +0300
  * [MDEV-17003](https://jira.mariadb.org/browse/MDEV-17003) service\_manager\_extend\_timeout() being called too often
* Merge [Revision #b4210f3640](https://github.com/MariaDB/server/commit/b4210f3640) 2018-08-21 10:07:26 +0200 - Merge branch '10.0' into 10.1
* Merge [Revision #bcc677bb72](https://github.com/MariaDB/server/commit/bcc677bb72) 2018-08-15 16:48:13 +0200 - Merge branch '5.5' into 10.0
* [Revision #1b797e9e63](https://github.com/MariaDB/server/commit/1b797e9e63)\
  2018-08-06 15:50:22 +0200
  * [MDEV-15475](https://jira.mariadb.org/browse/MDEV-15475): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed on EXPLAIN EXTENDED with constant table and view
* [Revision #074b672b5d](https://github.com/MariaDB/server/commit/074b672b5d)\
  2018-08-13 19:43:59 +0100
  * [MDEV-16963](https://jira.mariadb.org/browse/MDEV-16963) Tighten named pipe access control
* [Revision #3ff0801c73](https://github.com/MariaDB/server/commit/3ff0801c73)\
  2018-08-11 12:11:59 +0200
  * [MDEV-16810](https://jira.mariadb.org/browse/MDEV-16810) AddressSanitizer: stack-buffer-overflow in int10\_to\_str
* [Revision #ad577091ed](https://github.com/MariaDB/server/commit/ad577091ed)\
  2018-08-06 21:22:17 +0530
  * [MDEV-16904](https://jira.mariadb.org/browse/MDEV-16904) inline void swap(base\_list \&rhs) should swap list only when list is... not empty
* [Revision #ebaacf0747](https://github.com/MariaDB/server/commit/ebaacf0747)\
  2018-08-06 16:46:19 +0300
  * Update rules
* [Revision #68ebfb31f2](https://github.com/MariaDB/server/commit/68ebfb31f2)\
  2018-06-05 15:14:19 +0530
  * [MDEV-16166](https://jira.mariadb.org/browse/MDEV-16166) RBR breaks with HA\_ERR\_KEY\_NOT\_FOUND upon DELETE from table... with spatial index
* [Revision #33110db055](https://github.com/MariaDB/server/commit/33110db055)\
  2018-07-31 10:46:16 -0400
  * bump the VERSION
* [Revision #b62ac16185](https://github.com/MariaDB/server/commit/b62ac16185)\
  2018-08-15 15:21:37 +0300
  * [MDEV-6439](https://jira.mariadb.org/browse/MDEV-6439): Server crashes in Explain\_union::print\_explain with explain in slow log, tis620 charset
* [Revision #75dfd4acb9](https://github.com/MariaDB/server/commit/75dfd4acb9)\
  2018-07-26 15:04:11 +0200
  * This is patch for the [MDEV-9519](https://jira.mariadb.org/browse/MDEV-9519) issue:
* Merge [Revision #5960815630](https://github.com/MariaDB/server/commit/5960815630) 2018-08-15 10:35:54 +0300 - Merge pull request #844 from codership/10.1-[MDEV-15933](https://jira.mariadb.org/browse/MDEV-15933)
* [Revision #dfb19c06b8](https://github.com/MariaDB/server/commit/dfb19c06b8)\
  2018-08-14 10:34:51 +0200
  * [MDEV-15933](https://jira.mariadb.org/browse/MDEV-15933) Cannot resume Node SYNCED state when wsrep\_desync is done after FTWRL
* [Revision #68eb9b1a78](https://github.com/MariaDB/server/commit/68eb9b1a78)\
  2018-08-14 22:42:46 +0200
  * [MDEV-16220](https://jira.mariadb.org/browse/MDEV-16220) Do not pass UTF8 to mysql in command line parameters, on Windows
* [Revision #0496bbc120](https://github.com/MariaDB/server/commit/0496bbc120)\
  2018-08-09 15:05:40 -0300
  * [MDEV-15869](https://jira.mariadb.org/browse/MDEV-15869) mariadb-backup is lacking some dependencies declaration (#771)
* [Revision #757e3b88d2](https://github.com/MariaDB/server/commit/757e3b88d2)\
  2018-08-07 10:43:08 -0400
  * bump the VERSION
* [Revision #3b37edee1a](https://github.com/MariaDB/server/commit/3b37edee1a)\
  2018-08-06 15:45:44 +0300
  * [MDEV-13333](https://jira.mariadb.org/browse/MDEV-13333): Deadlock failure that does not occur elsewhere
* [Revision #998b1c0e75](https://github.com/MariaDB/server/commit/998b1c0e75)\
  2018-08-05 12:11:31 +0300
  * Fix galera test MW-44
* [Revision #9419908f38](https://github.com/MariaDB/server/commit/9419908f38)\
  2018-08-04 05:57:06 +0530
  * [MDEV-15433](https://jira.mariadb.org/browse/MDEV-15433): Optimizer does not use group by optimization with distinct
* Merge [Revision #b9f0112248](https://github.com/MariaDB/server/commit/b9f0112248) 2018-08-05 09:27:13 +0300 - Merge pull request #609 from benrubson/stunnel
* [Revision #1adc382c2f](https://github.com/MariaDB/server/commit/1adc382c2f)\
  2018-02-12 22:08:57 +0100
  * Use stunnel during rsync SST if available

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
