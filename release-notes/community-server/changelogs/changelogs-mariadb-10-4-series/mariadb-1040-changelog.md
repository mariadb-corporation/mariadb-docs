# MariaDB 10.4.0 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.0/)[Release Notes](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/)[Changelog](mariadb-1040-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 9 Nov 2018

For the highlights of this release, see the [release notes](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Merge [Revision #c761b43451](https://github.com/MariaDB/server/commit/c761b43451) 2018-11-08 09:50:56 +0200 - Merge 10.3 into 10.4
* [Revision #bac2ec3a5b](https://github.com/MariaDB/server/commit/bac2ec3a5b)\
  2018-11-08 09:44:29 +0200
  * After-merge fixes to the Oracle compatibility parser
* Merge [Revision #2767cb76d4](https://github.com/MariaDB/server/commit/2767cb76d4) 2018-11-08 09:39:37 +0200 - Merge 10.2 into 10.3
* [Revision #4142589207](https://github.com/MariaDB/server/commit/4142589207)\
  2018-11-07 12:07:32 -0800
  * [MDEV-17635](https://jira.mariadb.org/browse/MDEV-17635) Server hangs after the query with recursive CTE
* [Revision #c565622c6c](https://github.com/MariaDB/server/commit/c565622c6c)\
  2018-11-07 15:24:30 +0200
  * [MDEV-14528](https://jira.mariadb.org/browse/MDEV-14528) followup.
* [Revision #a91109846c](https://github.com/MariaDB/server/commit/a91109846c)\
  2018-11-07 20:21:12 +0200
  * Merge an .inc file to .test
* [Revision #6567a94c71](https://github.com/MariaDB/server/commit/6567a94c71)\
  2018-11-07 17:42:41 +0200
  * [MDEV-13134](https://jira.mariadb.org/browse/MDEV-13134): Merge tests to innodb.alter\_algorithm
* Merge [Revision #862af4d255](https://github.com/MariaDB/server/commit/862af4d255) 2018-11-07 13:11:04 +0200 - Merge 10.2 into 10.3
* [Revision #e82ebb8f06](https://github.com/MariaDB/server/commit/e82ebb8f06)\
  2018-11-07 13:08:00 +0200
  * [MDEV-14528](https://jira.mariadb.org/browse/MDEV-14528): Disable a failing test
* Merge [Revision #89f948c766](https://github.com/MariaDB/server/commit/89f948c766) 2018-11-07 08:17:47 +0200 - Merge 10.1 into 10.2
* Merge [Revision #59c82dde09](https://github.com/MariaDB/server/commit/59c82dde09) 2018-11-07 08:08:45 +0200 - Merge 10.0 into 10.1
* Merge [Revision #5f29fdecc0](https://github.com/MariaDB/server/commit/5f29fdecc0) 2018-11-07 08:02:18 +0200 - Merge 5.5 into 10.0
* [Revision #b68d8a05d3](https://github.com/MariaDB/server/commit/b68d8a05d3)\
  2018-10-12 09:07:05 +0200
  * [MDEV-17401](https://jira.mariadb.org/browse/MDEV-17401): LOAD DATA from very big file into MyISAM table results in EOF error and corrupt index
* [Revision #b7eca63620](https://github.com/MariaDB/server/commit/b7eca63620)\
  2018-11-01 18:47:53 +0100
  * fix the test to clean after itself
* [Revision #c32f7ed235](https://github.com/MariaDB/server/commit/c32f7ed235)\
  2018-10-31 18:18:48 +0100
  * [MDEV-17377](https://jira.mariadb.org/browse/MDEV-17377) invalid gap in auto-increment values after LOAD DATA
* [Revision #9ff9d2303d](https://github.com/MariaDB/server/commit/9ff9d2303d)\
  2018-10-28 22:50:49 +0900
  * test framework manual is moved
* [Revision #9c026273a9](https://github.com/MariaDB/server/commit/9c026273a9)\
  2018-11-06 10:58:02 +0000
  * Add implementation in .h and delete unneccessery printing
* [Revision #ef40018535](https://github.com/MariaDB/server/commit/ef40018535)\
  2018-10-10 18:25:53 +0300
  * [MDEV-17230](https://jira.mariadb.org/browse/MDEV-17230): encryption\_key\_id from alter is ignored by encryption threads
* [Revision #04789ec801](https://github.com/MariaDB/server/commit/04789ec801)\
  2018-11-06 09:29:41 +0100
  * [MDEV-14781](https://jira.mariadb.org/browse/MDEV-14781) - threadpool slowdown with slow ssl handshake.
* [Revision #54b8856b87](https://github.com/MariaDB/server/commit/54b8856b87)\
  2017-11-11 22:32:39 +0200
  * [MDEV-14528](https://jira.mariadb.org/browse/MDEV-14528) Track master timestamp in case rolling back to serial replication
* [Revision #7dfcb87107](https://github.com/MariaDB/server/commit/7dfcb87107)\
  2018-11-06 17:23:39 +0300
  * Disable rocksdb.com\_rpc\_tx test
* [Revision #54b2e1c1be](https://github.com/MariaDB/server/commit/54b2e1c1be)\
  2018-07-05 17:49:44 +0200
  * [MDEV-16697](https://jira.mariadb.org/browse/MDEV-16697): Fix difference between 32bit/windows and 64bit systems in allowed select nest level
* [Revision #89a87e8e42](https://github.com/MariaDB/server/commit/89a87e8e42)\
  2018-10-20 14:05:33 +0200
  * [MDEV-14429](https://jira.mariadb.org/browse/MDEV-14429) sql\_safe\_updates in my.cnf not work
* [Revision #564a63b5a3](https://github.com/MariaDB/server/commit/564a63b5a3)\
  2018-10-15 12:06:00 +0200
  * [MDEV-14429](https://jira.mariadb.org/browse/MDEV-14429) sql\_safe\_updates in my.cnf not work
* [Revision #4990b0e1ee](https://github.com/MariaDB/server/commit/4990b0e1ee)\
  2018-10-19 12:51:57 +0200
  * [MDEV-17496](https://jira.mariadb.org/browse/MDEV-17496) aws plugin is no longer built for debian/ubuntu
* [Revision #9bf8568c04](https://github.com/MariaDB/server/commit/9bf8568c04)\
  2018-10-09 18:10:48 +0200
  * fix an old typo
* [Revision #07e4853c23](https://github.com/MariaDB/server/commit/07e4853c23)\
  2018-11-07 19:00:14 +0400
  * [MDEV-17563](https://jira.mariadb.org/browse/MDEV-17563) Different results using table or view when comparing values of time type [MDEV-17625](https://jira.mariadb.org/browse/MDEV-17625) Different warnings when comparing a garbage to DATETIME vs TIME
* [Revision #a5e2a14ef3](https://github.com/MariaDB/server/commit/a5e2a14ef3)\
  2018-11-07 14:42:36 +0400
  * [MDEV-17634](https://jira.mariadb.org/browse/MDEV-17634) Regression: TIME(0)=TIME('z') returns NULL vs 1
* [Revision #41e68e8e5b](https://github.com/MariaDB/server/commit/41e68e8e5b)\
  2018-11-06 09:40:07 -0800
  * [MDEV-16357](https://jira.mariadb.org/browse/MDEV-16357) LIMIT and ORDER BY clause is ignored on a query with UNION when using brackets
* Merge [Revision #074c684099](https://github.com/MariaDB/server/commit/074c684099) 2018-11-06 16:24:16 +0200 - Merge 10.3 into 10.4
* Merge [Revision #df563e0c03](https://github.com/MariaDB/server/commit/df563e0c03) 2018-11-06 09:40:39 +0200 - Merge 10.2 into 10.3
* [Revision #bdfe2784d5](https://github.com/MariaDB/server/commit/bdfe2784d5)\
  2018-11-06 08:42:30 +0200
  * Unify a test with the 10.3 version
* Merge [Revision #32062cc61c](https://github.com/MariaDB/server/commit/32062cc61c) 2018-11-06 08:41:48 +0200 - Merge 10.1 into 10.2
* Merge [Revision #bae21bfb5d](https://github.com/MariaDB/server/commit/bae21bfb5d) 2018-11-05 17:08:21 +0200 - Merge 10.0 into 10.1
* [Revision #db55b39fb2](https://github.com/MariaDB/server/commit/db55b39fb2)\
  2018-11-05 16:47:14 +0200
  * Revert some InnoDB/XtraDB changes
* Merge [Revision #d63e198061](https://github.com/MariaDB/server/commit/d63e198061) 2018-11-05 12:15:17 +0200 - Merge 10.0 into 10.1
* [Revision #03977e8273](https://github.com/MariaDB/server/commit/03977e8273)\
  2018-10-25 21:36:24 +0300
  * [MDEV-13671](https://jira.mariadb.org/browse/MDEV-13671) InnoDB should use case-insensitive column name comparisons like the rest of the server
* [Revision #f0cb21ea2e](https://github.com/MariaDB/server/commit/f0cb21ea2e)\
  2018-11-02 12:42:01 +0200
  * Remove dead code is\_thd\_killed()
* [Revision #9eb8a46790](https://github.com/MariaDB/server/commit/9eb8a46790)\
  2018-11-01 11:09:32 -0400
  * bump the VERSION
* [Revision #38b3e52c3c](https://github.com/MariaDB/server/commit/38b3e52c3c)\
  2018-10-31 23:30:34 +0530
  * [MDEV-16695](https://jira.mariadb.org/browse/MDEV-16695): Estimate for rows of derived tables is very high when we are using index\_merge union
* [Revision #c4c738e1ef](https://github.com/MariaDB/server/commit/c4c738e1ef)\
  2018-11-01 09:27:59 +0200
  * Revert commit b2f39a5f567d006000aad8b431267298cf81b569 wrong branch.
* [Revision #b2f39a5f56](https://github.com/MariaDB/server/commit/b2f39a5f56)\
  2018-11-01 09:15:41 +0200
  * Add missing wsrep.cnf.sh
* [Revision #75ceb6ff13](https://github.com/MariaDB/server/commit/75ceb6ff13)\
  2018-10-31 14:25:26 +0400
  * [MDEV-17298](https://jira.mariadb.org/browse/MDEV-17298) ASAN unknown-crash / READ of size 1 in my\_strntoul\_8bit upon INSERT .. SELECT
* [Revision #6472c5c015](https://github.com/MariaDB/server/commit/6472c5c015)\
  2018-11-03 14:24:15 +0400
  * [MDEV-15890](https://jira.mariadb.org/browse/MDEV-15890) Strange error message if you try to FLUSH TABLES after LOCK TABLES .
* [Revision #1a89356382](https://github.com/MariaDB/server/commit/1a89356382)\
  2018-11-02 12:27:38 -0400
  * bump the VERSION
* [Revision #dafbd50e8a](https://github.com/MariaDB/server/commit/dafbd50e8a)\
  2018-11-01 16:06:03 +0200
  * [MDEV-17133](https://jira.mariadb.org/browse/MDEV-17133) follow-up patch to fix mf\_iocache-t unittest which did not always correctly simulated io-cache::end\_of\_file. The error was caused by implicit cast to unsigned of an intemediate term in a formula.
* [Revision #af9649c722](https://github.com/MariaDB/server/commit/af9649c722)\
  2018-11-03 21:17:17 +0100
  * [MDEV-17349](https://jira.mariadb.org/browse/MDEV-17349) Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed on concurrent SELECT and DELETE after RENAME from table with index on virtual column
* [Revision #8a346f31b9](https://github.com/MariaDB/server/commit/8a346f31b9)\
  2018-11-02 14:17:19 +0200
  * [MDEV-17073](https://jira.mariadb.org/browse/MDEV-17073) INSERT…ON DUPLICATE KEY UPDATE became more deadlock-prone
* [Revision #cfa047069e](https://github.com/MariaDB/server/commit/cfa047069e)\
  2018-11-02 14:17:11 +0200
  * Remove an unused declaration
* [Revision #1c6b982e02](https://github.com/MariaDB/server/commit/1c6b982e02)\
  2018-11-01 08:55:16 +0200
  * [MDEV-12779](https://jira.mariadb.org/browse/MDEV-12779) Oracle/DB2 Compatibility Implicit Ordering for ROW\_NUMBER OVER
* [Revision #dd6e74c62a](https://github.com/MariaDB/server/commit/dd6e74c62a)\
  2018-10-31 22:20:51 +0100
  * [MDEV-16774](https://jira.mariadb.org/browse/MDEV-16774) SET PASSWORD and ALTER USER with slightly different results
* [Revision #abcd09c95a](https://github.com/MariaDB/server/commit/abcd09c95a)\
  2018-11-01 10:48:56 +0200
  * mtr\_t::start(): Remove unused parameters
* [Revision #d355be8877](https://github.com/MariaDB/server/commit/d355be8877)\
  2018-11-01 10:40:14 +0200
  * Remove dead code in dict\_build\_table\_def\_step()
* [Revision #f8268f3cce](https://github.com/MariaDB/server/commit/f8268f3cce)\
  2018-10-31 17:19:25 +0100
  * [MDEV-17195](https://jira.mariadb.org/browse/MDEV-17195) Speedup lock-ddl-per-table, if there is a large number of tables
* [Revision #dc91ea5bb7](https://github.com/MariaDB/server/commit/dc91ea5bb7)\
  2018-10-30 13:29:19 +0200
  * [MDEV-12023](https://jira.mariadb.org/browse/MDEV-12023) Assertion failure sym\_node->table != NULL on startup
* [Revision #3859273d04](https://github.com/MariaDB/server/commit/3859273d04)\
  2018-02-10 18:28:23 +1100
  * [MDEV-14267](https://jira.mariadb.org/browse/MDEV-14267): correct FSF address
* [Revision #f8604ed9ff](https://github.com/MariaDB/server/commit/f8604ed9ff)\
  2018-10-29 13:49:44 +0300
  * [MDEV-17414](https://jira.mariadb.org/browse/MDEV-17414): MyROCKS order desc limit 1 fails : Backport to 10.2
* Merge [Revision #a6ffeeeaa9](https://github.com/MariaDB/server/commit/a6ffeeeaa9) 2018-10-29 12:05:50 +0200 - [MDEV-17491](https://jira.mariadb.org/browse/MDEV-17491) micro optimize page\_id\_t #892
* [Revision #b3009059d0](https://github.com/MariaDB/server/commit/b3009059d0)\
  2018-10-29 11:26:23 +0200
  * Minor cleanup
* [Revision #14be814380](https://github.com/MariaDB/server/commit/14be814380)\
  2018-10-18 18:23:12 +0300
  * [MDEV-17491](https://jira.mariadb.org/browse/MDEV-17491) micro optimize page\_id\_t
* [Revision #76318d55aa](https://github.com/MariaDB/server/commit/76318d55aa)\
  2018-10-24 09:03:47 +0200
  * [MDEV-17525](https://jira.mariadb.org/browse/MDEV-17525): Window functions not working in ONLY\_FULL\_GROUP\_BY mode
* [Revision #2abf2648a6](https://github.com/MariaDB/server/commit/2abf2648a6)\
  2018-10-25 17:09:54 +0300
  * [MDEV-17536](https://jira.mariadb.org/browse/MDEV-17536) Merge new release of InnoDB 5.7.24 to 10.2
* [Revision #31366c6c93](https://github.com/MariaDB/server/commit/31366c6c93)\
  2018-10-25 17:06:18 +0300
  * [MDEV-17548](https://jira.mariadb.org/browse/MDEV-17548) Incorrect access to off-page column for indexed virtual column
* [Revision #e548d92b23](https://github.com/MariaDB/server/commit/e548d92b23)\
  2018-10-25 16:11:52 +0300
  * [MDEV-17546](https://jira.mariadb.org/browse/MDEV-17546) SPATIAL INDEX should not be allowed for FOREIGN KEY
* [Revision #8c9c583aff](https://github.com/MariaDB/server/commit/8c9c583aff)\
  2018-10-25 15:31:13 +0300
  * Remove a deprecation warning
* [Revision #7e9728a913](https://github.com/MariaDB/server/commit/7e9728a913)\
  2018-10-25 15:04:37 +0300
  * [MDEV-17545](https://jira.mariadb.org/browse/MDEV-17545) Predicate lock for SPATIAL INDEX should lock non-matching record
* [Revision #a21e01a53d](https://github.com/MariaDB/server/commit/a21e01a53d)\
  2018-10-25 09:08:44 +0300
  * [MDEV-17541](https://jira.mariadb.org/browse/MDEV-17541) KILL QUERY during lock wait in FOREIGN KEY check causes hang
* [Revision #e058a251c1](https://github.com/MariaDB/server/commit/e058a251c1)\
  2018-11-01 11:35:28 +0300
  * [MDEV-17518](https://jira.mariadb.org/browse/MDEV-17518): Range optimization doesn't use ON expressions from nested outer joins
* [Revision #f0cf85fd15](https://github.com/MariaDB/server/commit/f0cf85fd15)\
  2018-10-23 14:12:59 +0200
  * [MDEV-17518](https://jira.mariadb.org/browse/MDEV-17518): Range optimization doesn't use ON expressions from nested outer joins
* [Revision #14b62b1578](https://github.com/MariaDB/server/commit/14b62b1578)\
  2018-10-23 13:17:14 +0200
  * [MDEV-17518](https://jira.mariadb.org/browse/MDEV-17518): Range optimization doesn't use ON expressions from nested outer joins
* [Revision #3b6d903852](https://github.com/MariaDB/server/commit/3b6d903852)\
  2018-10-23 11:23:34 +0200
  * [MDEV-17493](https://jira.mariadb.org/browse/MDEV-17493): Partition pruning doesn't work for nested outer joins
* [Revision #03680a9b4f](https://github.com/MariaDB/server/commit/03680a9b4f)\
  2018-10-22 15:14:43 +0200
  * [MDEV-17518](https://jira.mariadb.org/browse/MDEV-17518): Range optimization doesn't use ON expressions from nested outer joins
* [Revision #a33c0e3f34](https://github.com/MariaDB/server/commit/a33c0e3f34)\
  2018-11-01 17:30:11 +0200
  * Minor clean-up for [MDEV-17038](https://jira.mariadb.org/browse/MDEV-17038)
* [Revision #4acfc6ecd9](https://github.com/MariaDB/server/commit/4acfc6ecd9)\
  2018-09-27 23:34:24 +0300
  * [MDEV-17038](https://jira.mariadb.org/browse/MDEV-17038) ALTER TABLE CHANGE COLUMN c1 c1 bigint NOT NULL - generates error if table uses SYSTEM VERSIONING
* [Revision #d30124e844](https://github.com/MariaDB/server/commit/d30124e844)\
  2018-10-29 16:12:52 +0200
  * [MDEV-17503](https://jira.mariadb.org/browse/MDEV-17503) CREATE SEQUENCE failed with innodb\_force\_primary\_key =1
* [Revision #6a6cc8a653](https://github.com/MariaDB/server/commit/6a6cc8a653)\
  2018-10-29 15:48:49 +0200
  * Remove not used table\_flag HA\_NO\_VARCHAR
* [Revision #cfd81de6d4](https://github.com/MariaDB/server/commit/cfd81de6d4)\
  2018-10-29 13:43:52 +0300
  * [MDEV-17414](https://jira.mariadb.org/browse/MDEV-17414): MyROCKS order desc limit 1 fails
* [Revision #3e47b41a16](https://github.com/MariaDB/server/commit/3e47b41a16)\
  2018-10-25 12:07:23 +0400
  * [MDEV-17542](https://jira.mariadb.org/browse/MDEV-17542) 10.3: gcc-8.0 produces lots of -Wclass-memaccess warnings in Table\_scope\_and\_contents\_source\_st
* [Revision #554ce5a0cc](https://github.com/MariaDB/server/commit/554ce5a0cc)\
  2018-10-20 12:56:28 +0100
  * Attempt to fix build by a workaround for a bug in Windows8.1 SDK
* [Revision #5b63a660dd](https://github.com/MariaDB/server/commit/5b63a660dd)\
  2018-10-20 09:58:34 +0300
  * [MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369)/[MDEV-12288](https://jira.mariadb.org/browse/MDEV-12288): Reset DB\_TRX\_ID on the metadata record
* [Revision #d6889f2b58](https://github.com/MariaDB/server/commit/d6889f2b58)\
  2018-10-19 21:56:15 +0100
  * [MDEV-17504](https://jira.mariadb.org/browse/MDEV-17504) : add diagnostics if creation of directories fail in mysql\_install\_db.exe
* [Revision #563efeceec](https://github.com/MariaDB/server/commit/563efeceec)\
  2018-11-04 07:13:07 +0400
  * [MDEV-17607](https://jira.mariadb.org/browse/MDEV-17607) DATE(COALESCE(year\_column)) returns a wrong result
* [Revision #2feac61e18](https://github.com/MariaDB/server/commit/2feac61e18)\
  2018-11-01 16:57:58 +0400
  * A cleanup for: [MDEV-16884](https://jira.mariadb.org/browse/MDEV-16884) Remove tests for field\_type() in Item\_cache\_temporal
* [Revision #c0d75a6d26](https://github.com/MariaDB/server/commit/c0d75a6d26)\
  2018-10-28 11:07:18 +0100
  * spider.show\_system\_tables: make the result stable
* [Revision #6087e21d91](https://github.com/MariaDB/server/commit/6087e21d91)\
  2018-10-18 19:33:41 +0200
  * compilation failure on Windows
* [Revision #7c40996cc8](https://github.com/MariaDB/server/commit/7c40996cc8)\
  2018-10-17 12:48:13 +0200
  * [MDEV-12321](https://jira.mariadb.org/browse/MDEV-12321) authentication plugin: SET PASSWORD support
* [Revision #14e181a434](https://github.com/MariaDB/server/commit/14e181a434)\
  2018-10-15 01:39:03 +0200
  * misc cleanups
* [Revision #76151f3cbc](https://github.com/MariaDB/server/commit/76151f3cbc)\
  2018-10-14 13:52:52 +0200
  * Use mysql.user.authentication\_string for password
* [Revision #0e388d43a7](https://github.com/MariaDB/server/commit/0e388d43a7)\
  2018-10-27 11:53:05 +0200
  * cleanup: add 'const' to password validation API
* [Revision #1cc03e1f19](https://github.com/MariaDB/server/commit/1cc03e1f19)\
  2018-10-13 18:32:05 +0200
  * cleanup: sql\_acl.cc remove fix\_plugin\_ptr()
* [Revision #dd78430548](https://github.com/MariaDB/server/commit/dd78430548)\
  2018-10-13 11:30:39 +0200
  * cleanup: sql\_acl.cc remove username=NULL
* [Revision #3476854013](https://github.com/MariaDB/server/commit/3476854013)\
  2018-10-12 18:48:15 +0200
  * cleanup: sql\_acl.cc password->LEX\_CSTRING
* [Revision #ca7401afdf](https://github.com/MariaDB/server/commit/ca7401afdf)\
  2018-10-12 19:24:28 +0200
  * cleanup: safe\_lexcstrdup\_root()
* [Revision #dfbba3d202](https://github.com/MariaDB/server/commit/dfbba3d202)\
  2018-10-14 18:05:40 +0200
  * cleanup: get rid of a SQL warning in a test
* [Revision #92bde77826](https://github.com/MariaDB/server/commit/92bde77826)\
  2018-01-14 13:34:10 +1100
  * my\_print\_defaults: remove --config-file/extra-file
* [Revision #9aac2bf86e](https://github.com/MariaDB/server/commit/9aac2bf86e)\
  2018-08-23 21:41:22 +0200
  * [MDEV-16294](https://jira.mariadb.org/browse/MDEV-16294) post-merge cleanups
* [Revision #65180225b8](https://github.com/MariaDB/server/commit/65180225b8)\
  2018-07-09 08:10:09 +1000
  * [MDEV-16294](https://jira.mariadb.org/browse/MDEV-16294): remove INSTALL SONAME IF EXISTS option
* [Revision #6513b838d3](https://github.com/MariaDB/server/commit/6513b838d3)\
  2018-07-04 19:27:20 +1000
  * [MDEV-16294](https://jira.mariadb.org/browse/MDEV-16294): postfix - INSTALL PLUGIN IF NOT EXISTS
* [Revision #bb85d92d6f](https://github.com/MariaDB/server/commit/bb85d92d6f)\
  2018-05-18 12:59:32 +1000
  * [MDEV-16294](https://jira.mariadb.org/browse/MDEV-16294): INSTALL PLUGIN IF NOT EXISTS / UNINSTALL PLUGIN IF EXISTS
* [Revision #4272eec050](https://github.com/MariaDB/server/commit/4272eec050)\
  2018-10-24 15:12:38 +0400
  * [MDEV-17534](https://jira.mariadb.org/browse/MDEV-17534) Implement fast path for ASCII range in strnxfrm\_onelevel\_internal()
* [Revision #88cfde26e8](https://github.com/MariaDB/server/commit/88cfde26e8)\
  2018-10-21 21:28:11 +0400
  * A cleanup for [MDEV-17511](https://jira.mariadb.org/browse/MDEV-17511). Re-enabling ctype\_ldml.test.
* [Revision #2e0bad8fc7](https://github.com/MariaDB/server/commit/2e0bad8fc7)\
  2018-10-21 05:14:02 +0400
  * Disabling test ctype\_ldml temporary: [MDEV-17511](https://jira.mariadb.org/browse/MDEV-17511) revealed a wrong test fragment
* [Revision #3fe2b86627](https://github.com/MariaDB/server/commit/3fe2b86627)\
  2018-10-21 05:02:38 +0400
  * [MDEV-17511](https://jira.mariadb.org/browse/MDEV-17511) Improve performance for ORDER BY with a CHAR(N) CHARACTER SET utf8\_unicode\_ci
* [Revision #f6a2020514](https://github.com/MariaDB/server/commit/f6a2020514)\
  2018-10-20 19:51:14 +0400
  * [MDEV-17477](https://jira.mariadb.org/browse/MDEV-17477) Wrong result for TIME('-2001-01-01 10:20:30') and numerous other str-to-time conversion problems [MDEV-17478](https://jira.mariadb.org/browse/MDEV-17478) Wrong result for TIME('+100:20:30')
* [Revision #0e5a4ac253](https://github.com/MariaDB/server/commit/0e5a4ac253)\
  2018-10-19 16:49:54 +0300
  * [MDEV-15662](https://jira.mariadb.org/browse/MDEV-15662) Instant DROP COLUMN or changing the order of columns
* [Revision #a8efe7ab1f](https://github.com/MariaDB/server/commit/a8efe7ab1f)\
  2018-10-19 14:20:31 +0400
  * [MDEV-17502](https://jira.mariadb.org/browse/MDEV-17502) [MDEV-17474](https://jira.mariadb.org/browse/MDEV-17474) Change Unicode xxx\_general\_ci and xxx\_bin collation implementation to "inline" style
* Merge [Revision #1bb9041176](https://github.com/MariaDB/server/commit/1bb9041176) 2018-10-19 10:15:53 +0300 - Merge 10.3 into 10.4
* Merge [Revision #1595ff8a2c](https://github.com/MariaDB/server/commit/1595ff8a2c) 2018-10-19 09:32:52 +0300 - Merge 10.2 into 10.3
* [Revision #ab1ce2204e](https://github.com/MariaDB/server/commit/ab1ce2204e)\
  2018-10-19 09:29:28 +0300
  * [MDEV-17466](https://jira.mariadb.org/browse/MDEV-17466): Remove the debug assertion
* [Revision #abbf169f52](https://github.com/MariaDB/server/commit/abbf169f52)\
  2018-10-19 09:28:21 +0300
  * Remove unused TIMETPF
* [Revision #67f06cadc3](https://github.com/MariaDB/server/commit/67f06cadc3)\
  2018-10-09 10:20:49 +0200
  * [MDEV-17359](https://jira.mariadb.org/browse/MDEV-17359) Concatenation operator || in like expression
* Merge [Revision #9b14e37717](https://github.com/MariaDB/server/commit/9b14e37717) 2018-10-18 12:22:48 +0300 - Merge 10.3 into 10.4
* Merge [Revision #981a81090f](https://github.com/MariaDB/server/commit/981a81090f) 2018-10-18 12:15:31 +0300 - Merge 10.2 into 10.3
* [Revision #64d26ec52a](https://github.com/MariaDB/server/commit/64d26ec52a)\
  2018-10-18 12:15:07 +0300
  * Fix the Windows build
* Merge [Revision #22eb146454](https://github.com/MariaDB/server/commit/22eb146454) 2018-10-18 11:27:28 +0300 - Merge 10.2 into 10.3
* [Revision #56de291978](https://github.com/MariaDB/server/commit/56de291978)\
  2018-10-18 10:10:11 +0300
  * Fix a merge error in commit 28f08d3753eb10a1393a63e6c581d43aad9f93b9
* [Revision #3eaae09669](https://github.com/MariaDB/server/commit/3eaae09669)\
  2018-10-18 11:27:19 +0300
  * Extend the use of innodb\_default\_row\_format.combinations
* Merge [Revision #f454189c60](https://github.com/MariaDB/server/commit/f454189c60) 2018-10-17 19:05:59 +0300 - Merge 10.2 into 10.3
* [Revision #853a0a4368](https://github.com/MariaDB/server/commit/853a0a4368)\
  2018-10-17 09:54:18 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Set innodb\_safe\_truncate=ON by default
* [Revision #dc3f55947e](https://github.com/MariaDB/server/commit/dc3f55947e)\
  2018-10-17 03:26:30 -0700
  * [MDEV-17107](https://jira.mariadb.org/browse/MDEV-17107) Assertion \`table\_list->table' failed in find\_field\_in\_table\_ref
* [Revision #2308b9afec](https://github.com/MariaDB/server/commit/2308b9afec)\
  2018-10-03 21:45:05 +0300
  * [MDEV-17098](https://jira.mariadb.org/browse/MDEV-17098) DATE -> DATETIME replication conversion not working, even in ALL\_NON\_LOSSY mode
* [Revision #2d4075e1d9](https://github.com/MariaDB/server/commit/2d4075e1d9)\
  2018-10-16 10:42:30 +0300
  * [MDEV-17466](https://jira.mariadb.org/browse/MDEV-17466) Virtual column value not available during purge
* [Revision #af6077b535](https://github.com/MariaDB/server/commit/af6077b535)\
  2018-10-14 10:44:00 -0700
  * [MDEV-16990](https://jira.mariadb.org/browse/MDEV-16990):server crashes in base\_list\_iterator::next
* [Revision #b715a0fe45](https://github.com/MariaDB/server/commit/b715a0fe45)\
  2018-10-13 19:14:31 +0300
  * Disabled storage\_engine test for RocksDB due to unstable execution plan
* [Revision #6d29c8527b](https://github.com/MariaDB/server/commit/6d29c8527b)\
  2018-10-12 11:44:19 -0700
  * [MDEV-17354](https://jira.mariadb.org/browse/MDEV-17354) Server crashes in add\_key\_field / .. / Item\_func\_null\_predicate::add\_key\_fields upon INSERT .. SELECT
* [Revision #d3745c385e](https://github.com/MariaDB/server/commit/d3745c385e)\
  2018-10-18 10:17:34 +0400
  * Fixing "mtr --ps func\_time" failures in the tests added for [MDEV-17351](https://jira.mariadb.org/browse/MDEV-17351)
* [Revision #475c6ec551](https://github.com/MariaDB/server/commit/475c6ec551)\
  2018-10-16 19:10:57 +0400
  * [MDEV-17474](https://jira.mariadb.org/browse/MDEV-17474) Change Unicode collation implementation from "handler" to "inline" style (part#2)
* Merge [Revision #d88c136b9f](https://github.com/MariaDB/server/commit/d88c136b9f) 2018-10-17 19:11:42 +0300 - Merge 10.3 into 10.4
* [Revision #2fa4ed031c](https://github.com/MariaDB/server/commit/2fa4ed031c)\
  2018-10-17 18:55:46 +0300
  * [MDEV-17483](https://jira.mariadb.org/browse/MDEV-17483) Insert on delete-marked record can wrongly inherit old values for instantly added column
* [Revision #c2c1550f57](https://github.com/MariaDB/server/commit/c2c1550f57)\
  2018-10-17 04:37:25 -0700
  * [MDEV-17419](https://jira.mariadb.org/browse/MDEV-17419) Subquery with group by returns wrong results
* [Revision #97a37edc97](https://github.com/MariaDB/server/commit/97a37edc97)\
  2018-10-15 09:35:19 -0700
  * [MDEV-17137](https://jira.mariadb.org/browse/MDEV-17137): Syntax errors with VIEW using MEDIAN
* [Revision #103b1df510](https://github.com/MariaDB/server/commit/103b1df510)\
  2018-10-14 15:20:25 -0700
  * [MDEV-17222](https://jira.mariadb.org/browse/MDEV-17222) Reproducible server crash in String\_list::append\_str or in Field\_iterator\_table::create\_item
* Merge [Revision #74387028a0](https://github.com/MariaDB/server/commit/74387028a0) 2018-10-13 23:48:43 +0200 - Merge branch 'gtid\_table\_garbage\_rows' into 10.3
* Merge [Revision #00164ea4b1](https://github.com/MariaDB/server/commit/00164ea4b1) 2018-10-13 19:50:53 +0200 - Merge branch 'gtid\_table\_garbage\_rows\_10.3' into 10.3
* Merge [Revision #3eb2c46644](https://github.com/MariaDB/server/commit/3eb2c46644) 2018-10-07 23:40:32 +0200 - Merge branch 'gtid\_table\_garbage\_rows' into gtid\_table\_garbage\_rows\_10.3
* [Revision #2fd770641e](https://github.com/MariaDB/server/commit/2fd770641e)\
  2018-10-12 20:07:08 +0200
  * Revert the last change to replication test
* [Revision #00c40efcd6](https://github.com/MariaDB/server/commit/00c40efcd6)\
  2018-10-12 16:43:45 +0100
  * Fix portability issues with rpl test suite.
* [Revision #6120ae4aca](https://github.com/MariaDB/server/commit/6120ae4aca)\
  2018-10-12 06:15:21 +0400
  * Adjusting old tests and adding new tests for "[MDEV-8765](https://jira.mariadb.org/browse/MDEV-8765): mysqldump -use utf8mb4 by default"
* [Revision #ce643ddac7](https://github.com/MariaDB/server/commit/ce643ddac7)\
  2018-01-14 15:00:36 +1100
  * [MDEV-8765](https://jira.mariadb.org/browse/MDEV-8765): mysqldump -use utf8mb4 by default
* Merge [Revision #7e869a2767](https://github.com/MariaDB/server/commit/7e869a2767) 2018-10-11 23:09:10 +0300 - Merge 10.2 into 10.3
* [Revision #81a5b6ccd5](https://github.com/MariaDB/server/commit/81a5b6ccd5)\
  2018-10-11 22:48:19 +0300
  * [MDEV-17433](https://jira.mariadb.org/browse/MDEV-17433) Allow InnoDB start up with empty ib\_logfile0 from mariadb-backup --prepare
* [Revision #b8944e8972](https://github.com/MariaDB/server/commit/b8944e8972)\
  2018-10-11 22:47:42 +0300
  * Fix a sign mismatch
* [Revision #6319c0b541](https://github.com/MariaDB/server/commit/6319c0b541)\
  2018-10-11 15:10:13 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Replace innodb\_unsafe\_truncate with innodb\_safe\_truncate
* [Revision #4de0d920be](https://github.com/MariaDB/server/commit/4de0d920be)\
  2018-10-11 13:39:53 +0400
  * [MDEV-17411](https://jira.mariadb.org/browse/MDEV-17411) Wrong WHERE optimization with simple CASE and searched CASE
* Merge [Revision #30629e196d](https://github.com/MariaDB/server/commit/30629e196d) 2018-10-11 08:33:59 +0300 - [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Null-merge 10.2 into 10.3
* [Revision #3448ceb02a](https://github.com/MariaDB/server/commit/3448ceb02a)\
  2018-10-10 19:19:29 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Implement innodb\_unsafe\_truncate=ON for compatibility
* Merge [Revision #ae9d82c9f8](https://github.com/MariaDB/server/commit/ae9d82c9f8) 2018-10-11 08:22:08 +0300 - Merge 10.2 into 10.3
* Merge [Revision #07815d9555](https://github.com/MariaDB/server/commit/07815d9555) 2018-10-11 08:16:08 +0300 - Merge 10.1 into 10.2
* [Revision #940f0c78a4](https://github.com/MariaDB/server/commit/940f0c78a4)\
  2018-10-10 14:10:29 +0300
  * [MDEV-11487](https://jira.mariadb.org/browse/MDEV-11487): Make row\_ins\_index\_entry\_set\_vals() static
* [Revision #8d116d1686](https://github.com/MariaDB/server/commit/8d116d1686)\
  2018-10-10 14:39:57 +0300
  * [MDEV-17181](https://jira.mariadb.org/browse/MDEV-17181): rocksdb.allow\_to\_start\_after\_corruption fails on current 10.2
* [Revision #13e217b8c1](https://github.com/MariaDB/server/commit/13e217b8c1)\
  2018-10-17 01:27:25 -0700
  * [MDEV-17027](https://jira.mariadb.org/browse/MDEV-17027) server crashes in Bitmap<64u>::merge
* [Revision #6eae037c4c](https://github.com/MariaDB/server/commit/6eae037c4c)\
  2018-10-16 19:10:57 +0400
  * [MDEV-17474](https://jira.mariadb.org/browse/MDEV-17474) Change Unicode collation implementation from "handler" to "inline" style
* [Revision #fee24b1281](https://github.com/MariaDB/server/commit/fee24b1281)\
  2018-10-15 09:32:52 +0300
  * [MDEV-17313](https://jira.mariadb.org/browse/MDEV-17313) Data race in ib\_counter\_t
* [Revision #f7179c4432](https://github.com/MariaDB/server/commit/f7179c4432)\
  2018-10-15 21:30:27 +0400
  * [MDEV-17460](https://jira.mariadb.org/browse/MDEV-17460) Move the code from Item\_extract::val\_int() to a new class Extract\_source
* [Revision #1c5fd80a04](https://github.com/MariaDB/server/commit/1c5fd80a04)\
  2018-10-16 06:59:30 +0400
  * Fixing a test failure on 32bit platforms in the new [MDEV-17434](https://jira.mariadb.org/browse/MDEV-17434) code
* [Revision #22e75434e7](https://github.com/MariaDB/server/commit/22e75434e7)\
  2018-10-15 17:46:25 +0400
  * [MDEV-17434](https://jira.mariadb.org/browse/MDEV-17434) EXTRACT(DAY FROM negative\_time) returns wrong result
* [Revision #a53b99bf13](https://github.com/MariaDB/server/commit/a53b99bf13)\
  2018-10-14 17:28:55 +0400
  * [MDEV-17417](https://jira.mariadb.org/browse/MDEV-17417) TIME(99991231235959) returns 838:59:59 instead of 23:59:58
* [Revision #be31c18e4a](https://github.com/MariaDB/server/commit/be31c18e4a)\
  2018-10-11 22:55:52 +0300
  * ib\_counter\_t code simplified without functional changes
* [Revision #f9547748a6](https://github.com/MariaDB/server/commit/f9547748a6)\
  2018-10-11 13:06:37 +0300
  * [MDEV-17313](https://jira.mariadb.org/browse/MDEV-17313) Data race in ib\_counter\_t
* [Revision #f545e3cfa9](https://github.com/MariaDB/server/commit/f545e3cfa9)\
  2018-10-10 12:44:10 +0300
  * [MDEV-15562](https://jira.mariadb.org/browse/MDEV-15562): Remove dict\_table\_t::rollback\_instant(unsigned n)
* [Revision #f58a0b3afc](https://github.com/MariaDB/server/commit/f58a0b3afc)\
  2018-10-10 12:06:19 +0300
  * [MDEV-15562](https://jira.mariadb.org/browse/MDEV-15562): Simplify FOREIGN KEY error handling on DDL
* [Revision #cd08173490](https://github.com/MariaDB/server/commit/cd08173490)\
  2018-10-10 11:53:23 +0300
  * [MDEV-15562](https://jira.mariadb.org/browse/MDEV-15562): Add dict\_index\_t::first\_user\_field()
* Merge [Revision #2a955c7a83](https://github.com/MariaDB/server/commit/2a955c7a83) 2018-10-10 10:36:51 +0300 - Merge 10.3 into 10.4
* Merge [Revision #61b32df931](https://github.com/MariaDB/server/commit/61b32df931) 2018-10-10 06:45:19 +0300 - Merge 10.2 into 10.3
* [Revision #00b6c7d8fc](https://github.com/MariaDB/server/commit/00b6c7d8fc)\
  2018-10-10 06:31:43 +0300
  * [MDEV-16946](https://jira.mariadb.org/browse/MDEV-16946) innodb.alter\_kill failed in buildbot with wrong result
* [Revision #8b371e4b13](https://github.com/MariaDB/server/commit/8b371e4b13)\
  2018-10-09 17:01:49 +0300
  * [MDEV-16577](https://jira.mariadb.org/browse/MDEV-16577): rocksdb.issue255 fails in buildbot
* [Revision #e9d9ca8c44](https://github.com/MariaDB/server/commit/e9d9ca8c44)\
  2018-10-08 21:40:18 +0530
  * [MDEV-16980](https://jira.mariadb.org/browse/MDEV-16980) Wrongly set tablename len while opening the table for purge thread
* [Revision #2610c26a53](https://github.com/MariaDB/server/commit/2610c26a53)\
  2018-10-10 06:14:14 +0300
  * [MDEV-16273](https://jira.mariadb.org/browse/MDEV-16273) innodb.alter\_kill fails Unknown storage engine 'InnoDB'
* Merge [Revision #43ee6915fa](https://github.com/MariaDB/server/commit/43ee6915fa) 2018-10-09 09:11:30 +0300 - Merge 10.2 into 10.3
* [Revision #1ebe841fb8](https://github.com/MariaDB/server/commit/1ebe841fb8)\
  2018-10-07 10:19:19 -0700
  * [MDEV-17382](https://jira.mariadb.org/browse/MDEV-17382) Hash join algorithm should not be used to join materialized derived table / view by equality
* [Revision #1ff22b2062](https://github.com/MariaDB/server/commit/1ff22b2062)\
  2018-10-06 13:40:42 +0300
  * [MDEV-17289](https://jira.mariadb.org/browse/MDEV-17289): Skip the test for non-debug server
* [Revision #acca321af3](https://github.com/MariaDB/server/commit/acca321af3)\
  2018-10-04 16:06:05 +0100
  * CMake, Windows - reduce amount of noisy, irrelevant MESSAGE()s
* [Revision #8c2360dee8](https://github.com/MariaDB/server/commit/8c2360dee8)\
  2018-10-04 15:40:26 +0100
  * [MDEV-17373](https://jira.mariadb.org/browse/MDEV-17373) Windows: application verifier stop "Attempt to use an unknown SOCKET"
* [Revision #7fefd53f94](https://github.com/MariaDB/server/commit/7fefd53f94)\
  2018-10-04 14:24:14 +0100
  * [MDEV-14581](https://jira.mariadb.org/browse/MDEV-14581) Server does not clear diagnostics between sessions
* [Revision #33fadbfefc](https://github.com/MariaDB/server/commit/33fadbfefc)\
  2018-10-05 17:36:31 +0300
  * [MDEV-17289](https://jira.mariadb.org/browse/MDEV-17289): Add a test case
* [Revision #1e06daea7c](https://github.com/MariaDB/server/commit/1e06daea7c)\
  2018-09-20 06:14:03 +0300
  * Remove not used variable
* [Revision #6c97e85673](https://github.com/MariaDB/server/commit/6c97e85673)\
  2018-09-20 06:13:43 +0300
  * Remove valgrind warnings from Item\_str\_concat
* [Revision #29703e4f87](https://github.com/MariaDB/server/commit/29703e4f87)\
  2018-10-04 16:08:25 +0300
  * Fix a Galera result
* [Revision #6f2389b22d](https://github.com/MariaDB/server/commit/6f2389b22d)\
  2018-10-05 16:45:27 +0530\
  \*
  * Added flush table at the beginning of crash\_recovery test case.
* [Revision #2af67150cf](https://github.com/MariaDB/server/commit/2af67150cf)\
  2018-10-05 16:44:51 +0530
  * [MDEV-17289](https://jira.mariadb.org/browse/MDEV-17289) Multi-pass recovery fails to apply some redo log records
* [Revision #753117fed0](https://github.com/MariaDB/server/commit/753117fed0)\
  2018-10-03 16:49:19 +0100
  * AWS KMS plugin : more detailed message when API calls fail.
* [Revision #f67e050430](https://github.com/MariaDB/server/commit/f67e050430)\
  2018-10-03 14:29:16 +0100
  * Update libmariadb
* [Revision #b4e841648c](https://github.com/MariaDB/server/commit/b4e841648c)\
  2018-10-01 13:23:33 +0530
  * [MDEV-17215](https://jira.mariadb.org/browse/MDEV-17215) Assertion \`rw\_lock\_own(dict\_operation\_lock, RW\_LOCK\_S) || node->vcol\_info.is\_used()' failed
* [Revision #0f709912fb](https://github.com/MariaDB/server/commit/0f709912fb)\
  2018-09-27 17:57:27 +0300
  * [MDEV-17306](https://jira.mariadb.org/browse/MDEV-17306) rw\_lock\_x\_lock\_wait\_func() double increments rw\_x\_spin\_round\_count
* [Revision #f77071e0e8](https://github.com/MariaDB/server/commit/f77071e0e8)\
  2018-09-26 16:58:42 +0300
  * Remove unused code
* Merge [Revision #304857764b](https://github.com/MariaDB/server/commit/304857764b) 2018-09-25 17:29:43 +0300 - [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) mariadb-backup does not work with TRUNCATE
* [Revision #d913f6611c](https://github.com/MariaDB/server/commit/d913f6611c)\
  2018-09-25 10:06:06 -0400
  * bump the VERSION
* [Revision #7d4beb7286](https://github.com/MariaDB/server/commit/7d4beb7286)\
  2018-10-08 21:06:42 +0530
  * [MDEV-16980](https://jira.mariadb.org/browse/MDEV-16980) Wrongly set tablename len while opening the table for purge thread
* [Revision #8595361768](https://github.com/MariaDB/server/commit/8595361768)\
  2018-10-08 06:55:48 -0700
  * [MDEV-17381](https://jira.mariadb.org/browse/MDEV-17381) Wrong query result with LATERAL DERIVED optimization and join\_cache\_level=6
* [Revision #e2535dcc04](https://github.com/MariaDB/server/commit/e2535dcc04)\
  2018-10-08 06:19:27 -0700
  * [MDEV-17382](https://jira.mariadb.org/browse/MDEV-17382) Hash join algorithm should not be used to join materialized derived table / view by equality
* [Revision #fbee31418c](https://github.com/MariaDB/server/commit/fbee31418c)\
  2018-10-04 11:26:42 -0400
  * bump the VERSION
* [Revision #d7b293be87](https://github.com/MariaDB/server/commit/d7b293be87)\
  2018-10-04 18:38:01 +0400
  * [MDEV-17374](https://jira.mariadb.org/browse/MDEV-17374) Shift/reduce conflicts because of SOUNDS\_SYM, ESCAPE\_SYM, USER\_SYM not given precedence
* [Revision #5646c43159](https://github.com/MariaDB/server/commit/5646c43159)\
  2018-10-09 12:02:35 +0400
  * [MDEV-17216](https://jira.mariadb.org/browse/MDEV-17216) Assertion \`!dt->fraction\_remainder(decimals())' failed in Field\_temporal\_with\_date::store\_TIME\_with\_warning
* [Revision #f4cdf90d73](https://github.com/MariaDB/server/commit/f4cdf90d73)\
  2018-10-08 22:48:58 +0100
  * [MDEV-17279](https://jira.mariadb.org/browse/MDEV-17279) Windows : link C runtime dynamically
* [Revision #c57bbb2596](https://github.com/MariaDB/server/commit/c57bbb2596)\
  2018-10-09 05:20:05 +0400
  * [MDEV-17400](https://jira.mariadb.org/browse/MDEV-17400) The result of TIME('42949672965959-01') depends on architecture
* [Revision #f3761539b3](https://github.com/MariaDB/server/commit/f3761539b3)\
  2018-10-08 17:27:51 +0400
  * Disabling func\_time temporarily. New tests fail on machines with sizeof(long)==4
* [Revision #b639fe2be1](https://github.com/MariaDB/server/commit/b639fe2be1)\
  2018-10-08 13:38:01 +0400
  * [MDEV-17351](https://jira.mariadb.org/browse/MDEV-17351) Wrong results for GREATEST,TIMESTAMP,ADDTIME with an out-of-range TIME-alike argument
* [Revision #d03581bf3c](https://github.com/MariaDB/server/commit/d03581bf3c)\
  2018-10-07 12:16:59 -0700
  * [MDEV-17360](https://jira.mariadb.org/browse/MDEV-17360) Server crashes in optimize\_keyuse
* Merge [Revision #52f326cfb7](https://github.com/MariaDB/server/commit/52f326cfb7) 2018-10-05 10:33:50 +0100 - Merge branch 'bb-10.4-wlad' into 10.4
* [Revision #98473a8399](https://github.com/MariaDB/server/commit/98473a8399)\
  2018-10-05 09:36:02 +0100
  * Small refactoring in vio. - remove function prototype for shared memory (no more used), and VIO members that are unused - Do not call DisconnectNamedPipe on pipe handle. CloseHandle() is enough.
* [Revision #8f329e8d37](https://github.com/MariaDB/server/commit/8f329e8d37)\
  2018-09-25 16:06:32 +0100
  * [MDEV-10384](https://jira.mariadb.org/browse/MDEV-10384) Windows : Refactor threading in mysqld startup.
* Merge [Revision #444c380ceb](https://github.com/MariaDB/server/commit/444c380ceb) 2018-10-05 08:09:49 +0300 - Merge 10.3 into 10.4
* [Revision #941ca92a2c](https://github.com/MariaDB/server/commit/941ca92a2c)\
  2018-10-04 16:12:04 +0300
  * [MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369): Perform validation at IMPORT TABLESPACE
* [Revision #2badefb066](https://github.com/MariaDB/server/commit/2badefb066)\
  2018-10-04 16:08:25 +0300
  * Fix a Galera result
* [Revision #ae4f464fd6](https://github.com/MariaDB/server/commit/ae4f464fd6)\
  2018-10-03 11:16:40 +0300
  * [MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369): Implement accurate checks for the metadata record
* [Revision #c134f565c4](https://github.com/MariaDB/server/commit/c134f565c4)\
  2018-10-03 09:15:01 +0300
  * [MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369): Implement stricter checks for the metadata record
* Merge [Revision #15c7225a08](https://github.com/MariaDB/server/commit/15c7225a08) 2018-10-02 15:12:13 +0300 - Merge pull request #847 from tempesta-tech/tt-10.3-[MDEV-16211](https://jira.mariadb.org/browse/MDEV-16211)
* [Revision #44016ec0ca](https://github.com/MariaDB/server/commit/44016ec0ca)\
  2018-08-04 10:52:12 +0300
  * [MDEV-16211](https://jira.mariadb.org/browse/MDEV-16211) Contents of transaction\_registry not replicated by Galera
* [Revision #0c724a0c7d](https://github.com/MariaDB/server/commit/0c724a0c7d)\
  2018-10-02 13:46:20 +0300
  * Updated list of unstable tests for 10.3.10 release
* [Revision #55dd077656](https://github.com/MariaDB/server/commit/55dd077656)\
  2018-10-01 15:05:19 +0400
  * [MDEV-17331](https://jira.mariadb.org/browse/MDEV-17331) Reuse Temporal\_hybrid in xxx\_to\_date\_with\_warn()
* [Revision #e5aebc1408](https://github.com/MariaDB/server/commit/e5aebc1408)\
  2018-10-01 12:34:03 +0400
  * A cleanup for [MDEV-17317](https://jira.mariadb.org/browse/MDEV-17317) Add THD\* parameter into Item::get\_date() and stricter data type control to "fuzzydate"
* [Revision #f79bab3ae6](https://github.com/MariaDB/server/commit/f79bab3ae6)\
  2018-09-30 17:24:19 +0400
  * [MDEV-17318](https://jira.mariadb.org/browse/MDEV-17318) CAST(LEAST(zero\_date,non\_zero\_date) AS numeric\_data\_type) returns a wrong result
* [Revision #23740441d8](https://github.com/MariaDB/server/commit/23740441d8)\
  2018-09-29 21:20:24 +0400
  * [MDEV-17325](https://jira.mariadb.org/browse/MDEV-17325) NULL-ability problems with LEAST() in combination with NO\_ZERO\_DATE and NO\_ZERO\_IN\_DATE
* [Revision #ad8e02ac45](https://github.com/MariaDB/server/commit/ad8e02ac45)\
  2018-09-28 14:01:17 +0400
  * [MDEV-17317](https://jira.mariadb.org/browse/MDEV-17317) Add THD\* parameter into Item::get\_date() and stricter data type control to "fuzzydate"
* [Revision #492998c0d8](https://github.com/MariaDB/server/commit/492998c0d8)\
  2018-09-27 16:38:14 +0400
  * [MDEV-15406](https://jira.mariadb.org/browse/MDEV-15406) NO\_ZERO\_IN\_DATE erroneously affects how CAST(AS DATE) warns about fractional digit truncation
* [Revision #786940d7e0](https://github.com/MariaDB/server/commit/786940d7e0)\
  2018-09-26 20:14:47 +0400
  * [MDEV-17219](https://jira.mariadb.org/browse/MDEV-17219) Assertion \`!t->fraction\_remainder(decimals())' failed in Field\_time::store\_TIME\_with\_warning
* [Revision #25ad38abe5](https://github.com/MariaDB/server/commit/25ad38abe5)\
  2018-09-25 10:07:45 +0400
  * [MDEV-17288](https://jira.mariadb.org/browse/MDEV-17288) Replace Item\_func::get\_arg0\_date() to Date/Datetime methods
* [Revision #50003a9508](https://github.com/MariaDB/server/commit/50003a9508)\
  2018-09-22 18:33:07 +0400
  * [MDEV-17274](https://jira.mariadb.org/browse/MDEV-17274) Split Field\_temporal\_with\_date::store\*() for Field\_date\_common and Field\_datetime
* Merge [Revision #81ba90b59e](https://github.com/MariaDB/server/commit/81ba90b59e) 2018-09-21 13:16:38 +0300 - Merge 10.3 into 10.4
* Merge [Revision #45eaed0c4c](https://github.com/MariaDB/server/commit/45eaed0c4c) 2018-09-19 17:38:00 +0300 - Merge 10.3 into 10.4
* Merge [Revision #4a246fecbd](https://github.com/MariaDB/server/commit/4a246fecbd) 2018-09-19 08:21:03 +0300 - Merge 10.3 into 10.4
* [Revision #c9a5804e14](https://github.com/MariaDB/server/commit/c9a5804e14)\
  2018-09-17 18:39:16 -0700
  * [MDEV-17144](https://jira.mariadb.org/browse/MDEV-17144): Sample of spider\_direct\_sql cause crash
* [Revision #9e1a39aae4](https://github.com/MariaDB/server/commit/9e1a39aae4)\
  2018-09-17 12:56:03 +0400
  * Cleanup: Removing unused double\_to\_datetime().
* [Revision #4437b5bffb](https://github.com/MariaDB/server/commit/4437b5bffb)\
  2018-09-16 19:24:08 +0400
  * Fixing Windows compilation failure in [MDEV-17203](https://jira.mariadb.org/browse/MDEV-17203) (C4291 no matching operator delete found)
* [Revision #d93399746d](https://github.com/MariaDB/server/commit/d93399746d)\
  2018-09-16 12:40:57 +0400
  * [MDEV-17203](https://jira.mariadb.org/browse/MDEV-17203) Move fractional second truncation from Item\_xxx\_typecast::get\_date() to Time and Datetime constructors
* Merge [Revision #171fbbb968](https://github.com/MariaDB/server/commit/171fbbb968) 2018-09-14 15:23:34 +0300 - Merge 10.3 into 10.4
* [Revision #30d225698f](https://github.com/MariaDB/server/commit/30d225698f)\
  2018-09-13 16:07:02 -0700
  * [MDEV-16912](https://jira.mariadb.org/browse/MDEV-16912): Spider Order By column\[datatime] limit 5 returns 3 rows
* [Revision #61e8d21c77](https://github.com/MariaDB/server/commit/61e8d21c77)\
  2018-09-12 21:53:02 +0400
  * [MDEV-17182](https://jira.mariadb.org/browse/MDEV-17182) Move fractional second truncation outside of Field\_xxx::store\_TIME\_with\_warn()
* [Revision #2fe51a6fdd](https://github.com/MariaDB/server/commit/2fe51a6fdd)\
  2018-09-12 09:06:27 +0400
  * [MDEV-17175](https://jira.mariadb.org/browse/MDEV-17175) Change Time/Datetime constructors to return warnings in MYSQL\_TIME\_STATUS
* [Revision #5567a8c936](https://github.com/MariaDB/server/commit/5567a8c936)\
  2018-09-11 15:47:50 +0300
  * [MDEV-17138](https://jira.mariadb.org/browse/MDEV-17138) Reduce redo log volume for undo tablespace initialization
* [Revision #09af00cbde](https://github.com/MariaDB/server/commit/09af00cbde)\
  2018-09-10 18:01:54 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Remove old crash-upgrade logic in 10.4
* Merge [Revision #67fa97dc2c](https://github.com/MariaDB/server/commit/67fa97dc2c) 2018-09-11 21:31:47 +0300 - Merge 10.3 into 10.4
* Merge [Revision #1bf3e8ab43](https://github.com/MariaDB/server/commit/1bf3e8ab43) 2018-09-11 21:31:03 +0300 - Merge 10.3 into 10.4
* [Revision #f5bebaf1d6](https://github.com/MariaDB/server/commit/f5bebaf1d6)\
  2018-08-30 10:59:24 +0300
  * README.md: Break off long line
* [Revision #b1addcd9d4](https://github.com/MariaDB/server/commit/b1addcd9d4)\
  2018-08-30 11:01:51 +0300
  * README.md: Update Travis CI badge to active branch
* [Revision #a0dfefb0f8](https://github.com/MariaDB/server/commit/a0dfefb0f8)\
  2018-09-09 12:37:04 +0400
  * Fixed c++11 narrowing error
* [Revision #d9613b750c](https://github.com/MariaDB/server/commit/d9613b750c)\
  2018-05-29 21:46:31 +0400
  * Enable C++11
* [Revision #96572b7aa1](https://github.com/MariaDB/server/commit/96572b7aa1)\
  2018-08-30 11:30:28 -0700
  * EV-16992 Assertion \`table\_ref->table || table\_ref->view' failed in Field\_iterator\_table\_ref::set\_field\_iterator
* [Revision #f6694b6244](https://github.com/MariaDB/server/commit/f6694b6244)\
  2018-08-29 17:36:16 -0700
  * [MDEV-16889](https://jira.mariadb.org/browse/MDEV-16889): Spider Crash mysqld got exception 0xc0000005
* Merge [Revision #6ccd7d2df8](https://github.com/MariaDB/server/commit/6ccd7d2df8) 2018-08-28 05:54:16 -0700 - [MDEV-16250](https://jira.mariadb.org/browse/MDEV-16250): Spider system tables are MyISAM and needs repair after a crash
* [Revision #73fac2a5ff](https://github.com/MariaDB/server/commit/73fac2a5ff)\
  2018-08-27 13:27:18 -0700
  * [MDEV-16250](https://jira.mariadb.org/browse/MDEV-16250): Spider system tables are MyISAM and needs repair after a crash
* [Revision #8cc53aded9](https://github.com/MariaDB/server/commit/8cc53aded9)\
  2018-08-28 09:42:22 +0300
  * [MDEV-17068](https://jira.mariadb.org/browse/MDEV-17068) mysql system table is marked as crashed and should be repaired after the server crashes or is killed
* [Revision #f451fd8c06](https://github.com/MariaDB/server/commit/f451fd8c06)\
  2018-08-28 09:40:30 +0300
  * Updated company name in Aria plugin definition
* [Revision #2ccae65cff](https://github.com/MariaDB/server/commit/2ccae65cff)\
  2018-08-24 17:00:32 +0530
  * Fixed ASAN failure for the test main.func\_misc
* [Revision #5abc79dd7a](https://github.com/MariaDB/server/commit/5abc79dd7a)\
  2018-08-20 18:51:14 +0300
  * Fixed result for mysql\_protocols.result
* [Revision #38ecd541e8](https://github.com/MariaDB/server/commit/38ecd541e8)\
  2018-08-20 17:50:34 +0300
  * [MDEV-16986](https://jira.mariadb.org/browse/MDEV-16986) Unitialized mutex, SIGSEGV and assorted assertion failures in Aria code
* [Revision #ee98e95e25](https://github.com/MariaDB/server/commit/ee98e95e25)\
  2018-08-20 13:06:33 +0100
  * [MDEV-16536](https://jira.mariadb.org/browse/MDEV-16536) Remove shared memory transport
* [Revision #4299b82ad8](https://github.com/MariaDB/server/commit/4299b82ad8)\
  2018-08-18 23:22:22 +0400
  * [MDEV-17015](https://jira.mariadb.org/browse/MDEV-17015) Assertion \`m\_year <= 9999' failed in Year::Year upon bad argument to MAKEDATE
* [Revision #bf1c53e9be](https://github.com/MariaDB/server/commit/bf1c53e9be)\
  2018-08-18 01:14:49 +0530
  * Fixed ASAN failure for the test main.func\_misc. For Item name\_const , we should never do typecast it to Item\_field because we always expect it to be a constant value. So instead of checking the type() its better to introduce a function in the Item class get\_item\_field, which would return the item\_field object for the item which have type of FIELD\_ITEM
* [Revision #3faed09d6d](https://github.com/MariaDB/server/commit/3faed09d6d)\
  2018-08-16 17:30:02 +0300
  * [MDEV-16986](https://jira.mariadb.org/browse/MDEV-16986) Unitialized mutex, SIGSEGV and assorted assertion failures in Aria code
* [Revision #ead9a34a3e](https://github.com/MariaDB/server/commit/ead9a34a3e)\
  2018-08-16 18:12:13 +0100
  * [MDEV-15851](https://jira.mariadb.org/browse/MDEV-15851) Stop creating mysql.host table
* Merge [Revision #734db318ac](https://github.com/MariaDB/server/commit/734db318ac) 2018-08-16 10:08:30 +0300 - Merge 10.3 into 10.4
* [Revision #b151cc2b0b](https://github.com/MariaDB/server/commit/b151cc2b0b)\
  2018-08-16 09:57:53 +0300
  * Fix a test result
* [Revision #2ef3d37a59](https://github.com/MariaDB/server/commit/2ef3d37a59)\
  2018-08-15 19:14:20 +0400
  * [MDEV-16971](https://jira.mariadb.org/browse/MDEV-16971) Assertion \`is\_valid\_value\_slow()' failed in Time::adjust\_time\_range\_or\_invalidate
* [Revision #d87c53cb04](https://github.com/MariaDB/server/commit/d87c53cb04)\
  2018-08-15 18:18:41 +0400
  * [MDEV-16984](https://jira.mariadb.org/browse/MDEV-16984) Assertion \`dec' failed in Dec\_ptr::cmp
* [Revision #d6d63f4844](https://github.com/MariaDB/server/commit/d6d63f4844)\
  2018-08-02 17:59:11 +0300
  * [MDEV-16421](https://jira.mariadb.org/browse/MDEV-16421) Make system tables crash safe
* [Revision #0e0f1092b8](https://github.com/MariaDB/server/commit/0e0f1092b8)\
  2018-08-12 19:46:45 +0300
  * Fixed some source comments and help texts
* [Revision #5e1bbf66f1](https://github.com/MariaDB/server/commit/5e1bbf66f1)\
  2018-08-09 09:28:36 +0300
  * Remove warning from perfschema.bad\_option\_

## tests

* [Revision #cf7b48ffc9](https://github.com/MariaDB/server/commit/cf7b48ffc9)\
  2018-07-30 19:05:34 +0300
  * Updated wrong result files
* [Revision #e39eb18233](https://github.com/MariaDB/server/commit/e39eb18233)\
  2018-08-09 00:04:09 -0700
  * [MDEV-16398](https://jira.mariadb.org/browse/MDEV-16398): Spider Creates Query With Non-Existent Function
* [Revision #f6d4f624eb](https://github.com/MariaDB/server/commit/f6d4f624eb)\
  2018-08-13 16:04:37 +0300
  * [MDEV-12041](https://jira.mariadb.org/browse/MDEV-12041): innodb\_encrypt\_log key rotation
* [Revision #befc09f002](https://github.com/MariaDB/server/commit/befc09f002)\
  2018-08-12 12:08:11 +0530
  * [MDEV-16722](https://jira.mariadb.org/browse/MDEV-16722): Assertion \`type() != NULL\_ITEM' failed
* [Revision #b05ee14d95](https://github.com/MariaDB/server/commit/b05ee14d95)\
  2018-08-12 00:56:07 +0100
  * [MDEV-16277](https://jira.mariadb.org/browse/MDEV-16277) - fix tcp\_nodelay test.
* [Revision #077e590bbc](https://github.com/MariaDB/server/commit/077e590bbc)\
  2018-08-12 00:13:19 +0100
  * [MDEV-16277](https://jira.mariadb.org/browse/MDEV-16277) : Adjust MTR test results.
* [Revision #fdf4a5b7bc](https://github.com/MariaDB/server/commit/fdf4a5b7bc)\
  2018-08-11 22:54:14 +0100
  * [MDEV-16277](https://jira.mariadb.org/browse/MDEV-16277) tcp\_nodelay session variable to enable / disable Nagle algorithm
* [Revision #7a022d7061](https://github.com/MariaDB/server/commit/7a022d7061)\
  2018-08-11 19:12:13 +0400
  * A cleanup for [MDEV-16939](https://jira.mariadb.org/browse/MDEV-16939): avoid timeval initialization related problems in the future (compilation failures on Windows)
* [Revision #73a5dd8c54](https://github.com/MariaDB/server/commit/73a5dd8c54)\
  2018-08-11 15:32:55 +0100
  * Fix warning C4838 : conversion from 'type\_1' to 'type\_2' requires a narrowing conversion.
* [Revision #9811802a07](https://github.com/MariaDB/server/commit/9811802a07)\
  2018-08-11 14:43:45 +0400
  * [MDEV-16939](https://jira.mariadb.org/browse/MDEV-16939) Move TIMESTAMP truncation code to Field\_timestamp::store\_TIME\_with\_warn
* [Revision #2085f14a8d](https://github.com/MariaDB/server/commit/2085f14a8d)\
  2018-08-11 06:47:48 +0400
  * [MDEV-16938](https://jira.mariadb.org/browse/MDEV-16938) Move Item::get\_time\_with\_conversion() to Time
* [Revision #2966c1e422](https://github.com/MariaDB/server/commit/2966c1e422)\
  2018-08-11 06:24:36 +0400
  * Fixing size\_t to uint conversion failure on Windows
* [Revision #597dcbda3f](https://github.com/MariaDB/server/commit/597dcbda3f)\
  2018-08-10 19:20:14 +0400
  * Fixing a "safe" bug in [MDEV-16928](https://jira.mariadb.org/browse/MDEV-16928) (revealed by the Windows compiler)
* [Revision #c45050d253](https://github.com/MariaDB/server/commit/c45050d253)\
  2018-08-10 14:25:58 +0400
  * [MDEV-16935](https://jira.mariadb.org/browse/MDEV-16935) Change the parameter of Field\_xxx::store\_TIME\_with\_dec() to const Datetime\* and const Time\*
* [Revision #522cd3c7aa](https://github.com/MariaDB/server/commit/522cd3c7aa)\
  2018-08-10 06:22:13 +0400
  * Fixing compilation failure on Windows (cannot compare "bool" and "my\_bool" directly, cast needed)
* [Revision #d2bba4ce25](https://github.com/MariaDB/server/commit/d2bba4ce25)\
  2018-08-09 18:50:33 +0400
  * [MDEV-16928](https://jira.mariadb.org/browse/MDEV-16928) Move MYSQL\_TIME initialization from Field\_xxx::store\_time\_dec() to new constructors Time() and Datetime()
* [Revision #ffdae1a960](https://github.com/MariaDB/server/commit/ffdae1a960)\
  2018-08-09 11:08:11 +0400
  * [MDEV-16926](https://jira.mariadb.org/browse/MDEV-16926) CAST(COALESCE(year\_field)) returns wrong value
* [Revision #3f01c4fbd4](https://github.com/MariaDB/server/commit/3f01c4fbd4)\
  2018-08-09 09:26:57 +0300
  * Updated compress\_qpress.result
* [Revision #8524bb6872](https://github.com/MariaDB/server/commit/8524bb6872)\
  2018-08-09 06:31:05 +0400
  * [MDEV-14032](https://jira.mariadb.org/browse/MDEV-14032) SEC\_TO\_TIME executes side effect two times
* [Revision #a12e6c5ba4](https://github.com/MariaDB/server/commit/a12e6c5ba4)\
  2018-08-06 22:48:14 +0300
  * Deb: Don't define libzstd1 or other libraries as install dependencies manually
* [Revision #5d59a7b6a7](https://github.com/MariaDB/server/commit/5d59a7b6a7)\
  2018-08-07 16:15:27 +0300
  * Fixed compile error on windows
* [Revision #385ee993d9](https://github.com/MariaDB/server/commit/385ee993d9)\
  2018-08-07 16:26:35 +0400
  * A cleanup for [MDEV-16852](https://jira.mariadb.org/browse/MDEV-16852)
* [Revision #9da706fac3](https://github.com/MariaDB/server/commit/9da706fac3)\
  2018-08-07 11:04:56 +0300
  * Fixed compiler warning about MongoEnabled() in Connect
* [Revision #cb7b5fbf1c](https://github.com/MariaDB/server/commit/cb7b5fbf1c)\
  2018-08-07 10:48:42 +0400
  * [MDEV-16910](https://jira.mariadb.org/browse/MDEV-16910) Add class VDec
* [Revision #01e4426a63](https://github.com/MariaDB/server/commit/01e4426a63)\
  2018-08-05 01:23:44 -0500
  * Deb: Organize package order in control file to be more logical
* [Revision #cb6e888384](https://github.com/MariaDB/server/commit/cb6e888384)\
  2018-08-05 01:15:43 -0500
  * Deb: Fix brittle line numbers with simple paragraph detection
* [Revision #26c7b4f3fa](https://github.com/MariaDB/server/commit/26c7b4f3fa)\
  2018-08-05 00:07:35 -0500
  * Deb: Open new changelog entry for 10.4
* [Revision #aa6c1a6d19](https://github.com/MariaDB/server/commit/aa6c1a6d19)\
  2018-08-05 00:06:06 -0500
  * Deb: Mass replace 10.3 with 10.4 inside files
* [Revision #3173d73b71](https://github.com/MariaDB/server/commit/3173d73b71)\
  2018-08-04 23:58:54 -0500
  * Deb: Update the control file for 10.4 package names
* [Revision #788314ddf8](https://github.com/MariaDB/server/commit/788314ddf8)\
  2018-08-04 23:43:07 -0500
  * Deb: Rename all 10.3 files into 10.4 as this is a 10.4 branch now
* [Revision #0f9efd54ce](https://github.com/MariaDB/server/commit/0f9efd54ce)\
  2018-08-03 23:27:24 -0700
  * [MDEV-16359](https://jira.mariadb.org/browse/MDEV-16359) wrong result (extra rows) on the query with UNION and brackets
* [Revision #980aa3e71d](https://github.com/MariaDB/server/commit/980aa3e71d)\
  2018-08-03 07:55:50 +0400
  * [MDEV-16888](https://jira.mariadb.org/browse/MDEV-16888) Add virtual Type\_handler::cond\_notnull\_field\_isnull\_to\_field\_eq\_zero()
* [Revision #8ecc75373f](https://github.com/MariaDB/server/commit/8ecc75373f)\
  2018-08-02 17:49:28 +0400
  * [MDEV-16884](https://jira.mariadb.org/browse/MDEV-16884) Remove tests for field\_type() in Item\_cache\_temporal
* [Revision #c7115428ed](https://github.com/MariaDB/server/commit/c7115428ed)\
  2018-08-02 15:36:13 +0400
  * [MDEV-16881](https://jira.mariadb.org/browse/MDEV-16881) Remove Item::get\_temporal\_with\_sql\_mode() and val\_xxx\_from\_date()
* [Revision #41acca8bfa](https://github.com/MariaDB/server/commit/41acca8bfa)\
  2018-08-02 11:28:59 +0000
  * Added -j option to dpkg-buildpackage to speed up build
* [Revision #54fc47960d](https://github.com/MariaDB/server/commit/54fc47960d)\
  2018-08-01 16:14:41 +0400
  * [MDEV-16874](https://jira.mariadb.org/browse/MDEV-16874) Implement class Item\_handled\_func
* [Revision #af46c25760](https://github.com/MariaDB/server/commit/af46c25760)\
  2018-08-01 14:42:47 +0300
  * [MDEV-16727](https://jira.mariadb.org/browse/MDEV-16727): Server crashes in Item\_equal\_iterator\<List\_iterator\_fast, Item>::get\_curr\_field()
* [Revision #b1ae4e7e15](https://github.com/MariaDB/server/commit/b1ae4e7e15)\
  2018-07-31 16:58:02 +0400
  * [MDEV-16864](https://jira.mariadb.org/browse/MDEV-16864) Implement class Item\_func\_timestamp
* [Revision #2bbee0e1ec](https://github.com/MariaDB/server/commit/2bbee0e1ec)\
  2018-07-31 10:09:53 +0400
  * [MDEV-16861](https://jira.mariadb.org/browse/MDEV-16861) Split Item::update\_null\_value() into a new virtual method in Type\_handler
* [Revision #28ff7e89c6](https://github.com/MariaDB/server/commit/28ff7e89c6)\
  2018-07-30 20:40:48 +0400
  * [MDEV-16852](https://jira.mariadb.org/browse/MDEV-16852) Get rid of Item\_temporal\_hybrid\_func::fix\_temporal\_type()
* [Revision #aee3d162d2](https://github.com/MariaDB/server/commit/aee3d162d2)\
  2018-07-29 14:40:58 +0200
  * [MDEV-16730](https://jira.mariadb.org/browse/MDEV-16730): Server crashes in Bitmap<64u>::merge
* [Revision #2a3d3e052f](https://github.com/MariaDB/server/commit/2a3d3e052f)\
  2018-07-13 21:14:18 +0200
  * [MDEV-16721](https://jira.mariadb.org/browse/MDEV-16721): Assertion \`ctx.compare\_type\_handler()->cmp\_type() != STRING\_RESULT' failed
* [Revision #998c97e865](https://github.com/MariaDB/server/commit/998c97e865)\
  2018-07-25 13:08:01 +0400
  * [MDEV-16823](https://jira.mariadb.org/browse/MDEV-16823) Add Type\_handler::Column\_definition\_reuse\_fix\_attributes()
* Merge [Revision #9c0f5a252b](https://github.com/MariaDB/server/commit/9c0f5a252b) 2018-07-25 08:25:57 +0400 - Merge remote-tracking branch 'origin/10.3' into 10.4
* [Revision #d6594847cf](https://github.com/MariaDB/server/commit/d6594847cf)\
  2018-07-24 15:57:13 -0700
  * [MDEV-16246](https://jira.mariadb.org/browse/MDEV-16246): insert timestamp into spider table from mysqldump gets wrong time zone.
* [Revision #a78d1aaaa3](https://github.com/MariaDB/server/commit/a78d1aaaa3)\
  2018-07-24 12:00:17 +0400
  * [MDEV-16806](https://jira.mariadb.org/browse/MDEV-16806) Add Type\_handler::create\_literal\_item()
* [Revision #fee4632387](https://github.com/MariaDB/server/commit/fee4632387)\
  2018-07-20 11:07:19 +0400
  * [MDEV-15758](https://jira.mariadb.org/browse/MDEV-15758) Split Item\_bool\_func::get\_mm\_leaf() into virtual methods in Field and Type\_handler
* [Revision #6bfeace10b](https://github.com/MariaDB/server/commit/6bfeace10b)\
  2018-07-19 17:09:24 +0400
  * [MDEV-15759](https://jira.mariadb.org/browse/MDEV-15759) Expect "Impossible WHERE" for indexed\_int\_column=out\_of\_range\_int\_constant
* [Revision #25410d448d](https://github.com/MariaDB/server/commit/25410d448d)\
  2018-07-14 23:06:49 +0400
  * [MDEV-15473](https://jira.mariadb.org/browse/MDEV-15473) Isolate/sandbox PAM modules, so that they can't crash the server.
* [Revision #7fda6161bc](https://github.com/MariaDB/server/commit/7fda6161bc)\
  2018-07-14 19:49:59 +0300
  * Update version to 10.4.0
* [Revision #a9ca819897](https://github.com/MariaDB/server/commit/a9ca819897)\
  2018-07-12 18:12:20 +0300
  * Call alloc() instead of realloc()
* [Revision #5180eda342](https://github.com/MariaDB/server/commit/5180eda342)\
  2018-07-10 17:19:02 +0400
  * Adding forgotten "include/have\_debug.inc" into type\_temporal\_mysql56\_debug.test
* [Revision #29da7a1a9a](https://github.com/MariaDB/server/commit/29da7a1a9a)\
  2018-07-09 18:50:06 +0400
  * [MDEV-16542](https://jira.mariadb.org/browse/MDEV-16542) Fix ALTER TABLE FORCE to upgrade temporal types
* [Revision #aa01f51bde](https://github.com/MariaDB/server/commit/aa01f51bde)\
  2018-07-06 16:26:19 +0200
  * Fix of feedback plugin.
* [Revision #0e531581e0](https://github.com/MariaDB/server/commit/0e531581e0)\
  2018-07-06 10:33:00 +0200
  * A fix moved from sql\_yacc.yy to sql\_yacc\_ora.yy.
* [Revision #6fae04ea7d](https://github.com/MariaDB/server/commit/6fae04ea7d)\
  2018-07-06 09:03:13 +0200
  * Fixed compile warning of windows.
* [Revision #f9849766b3](https://github.com/MariaDB/server/commit/f9849766b3)\
  2018-07-06 09:02:40 +0200
  * Added new warnings for windows specific test.
* [Revision #1f8328fed0](https://github.com/MariaDB/server/commit/1f8328fed0)\
  2018-07-05 17:58:11 +0200
  * fix typo noticed by windows compiler
* [Revision #7e704a2308](https://github.com/MariaDB/server/commit/7e704a2308)\
  2018-07-05 14:19:54 +0200
  * Fixed 32bit version SELECT nesting depth.
* [Revision #9183f66f05](https://github.com/MariaDB/server/commit/9183f66f05)\
  2018-07-04 23:15:25 +0400
  * [MDEV-15473](https://jira.mariadb.org/browse/MDEV-15473) Isolate/sandbox PAM modules, so that they can't crash the server
* [Revision #725c3df53e](https://github.com/MariaDB/server/commit/725c3df53e)\
  2018-07-04 21:52:01 +0400
  * [MDEV-15471](https://jira.mariadb.org/browse/MDEV-15471) Isolate/sandbox PAM modules, so that they can't crash the server
* [Revision #de745ecf29](https://github.com/MariaDB/server/commit/de745ecf29)\
  2018-05-22 19:08:39 +0200
  * [MDEV-11953](https://jira.mariadb.org/browse/MDEV-11953): support of brackets in UNION/EXCEPT/INTERSECT operations
* [Revision #1b981b9edb](https://github.com/MariaDB/server/commit/1b981b9edb)\
  2018-07-03 14:54:40 +0200
  * Removed duplicate copy of the test
* [Revision #efba0b1df5](https://github.com/MariaDB/server/commit/efba0b1df5)\
  2018-07-03 15:49:34 +0400
  * [MDEV-15473](https://jira.mariadb.org/browse/MDEV-15473) Isolate/sandbox PAM modules, so that they can't crash the server.
* Merge [Revision #e61568ee93](https://github.com/MariaDB/server/commit/e61568ee93) 2018-07-03 14:02:05 +0400 - Merge remote-tracking branch 'origin/10.3' into 10.4
* [Revision #4b0cedf82d](https://github.com/MariaDB/server/commit/4b0cedf82d)\
  2018-06-27 16:07:21 +0400
  * [MDEV-16454](https://jira.mariadb.org/browse/MDEV-16454) Bad results for IN with ROW
* [Revision #e213b20e07](https://github.com/MariaDB/server/commit/e213b20e07)\
  2018-06-27 14:48:03 +0400
  * [MDEV-16592](https://jira.mariadb.org/browse/MDEV-16592) Change Item::with\_sum\_func from a member to a virtual method
* [Revision #d60fdb5814](https://github.com/MariaDB/server/commit/d60fdb5814)\
  2018-06-09 13:38:22 +0400
  * [MDEV-16451](https://jira.mariadb.org/browse/MDEV-16451) Split Item\_equal::add\_const() into a virtual method in type\_handler() [MDEV-16452](https://jira.mariadb.org/browse/MDEV-16452) Split TIME and DATETIME handling in Item\_func\_between, in\_temporal, cmp\_item\_internal
* [Revision #9043dd7a2d](https://github.com/MariaDB/server/commit/9043dd7a2d)\
  2018-06-08 12:36:42 +0400
  * [MDEV-11361](https://jira.mariadb.org/browse/MDEV-11361) Equal condition propagation does not work for DECIMAL and temporal dynamic SQL parameters [MDEV-16426](https://jira.mariadb.org/browse/MDEV-16426) Optimizer erroneously treats equal constants of different formats as same A cleanup for [MDEV-14630](https://jira.mariadb.org/browse/MDEV-14630): fixing a crash in Item\_decimal::eq().
* [Revision #054412598b](https://github.com/MariaDB/server/commit/054412598b)\
  2018-06-06 14:59:36 +0400
  * [MDEV-16414](https://jira.mariadb.org/browse/MDEV-16414) Add type\_handler\_xpath\_nodeset and remove XPATH\_NODESET
* [Revision #c20cd68e60](https://github.com/MariaDB/server/commit/c20cd68e60)\
  2018-06-06 14:09:06 +0400
  * [MDEV-14630](https://jira.mariadb.org/browse/MDEV-14630) Replace {STRING|INT|REAL|DECIMAL|DATE}\_ITEM to CONST\_ITEM
* [Revision #395212446a](https://github.com/MariaDB/server/commit/395212446a)\
  2018-06-05 22:26:24 +0400
  * [MDEV-16408](https://jira.mariadb.org/browse/MDEV-16408) Remove tests for Item::type() in Item\_basic\_value::eq()
* [Revision #f4dfc609cf](https://github.com/MariaDB/server/commit/f4dfc609cf)\
  2018-06-05 11:56:19 +0400
  * [MDEV-16388](https://jira.mariadb.org/browse/MDEV-16388) Replace member Item::fixed to virtual method is\_fixed()
* Merge [Revision #ab297744b7](https://github.com/MariaDB/server/commit/ab297744b7) 2018-06-05 10:50:08 +0400 - Merge remote-tracking branch 'origin/10.3' into 10.4
* [Revision #8760acdda8](https://github.com/MariaDB/server/commit/8760acdda8)\
  2018-06-03 02:39:53 +0200
  * cleanup: ASSERT\_COLUMN\_MARKED\_FOR\_WRITE\_OR\_COMPUTED
* [Revision #45dee3fc83](https://github.com/MariaDB/server/commit/45dee3fc83)\
  2018-06-01 16:59:21 +0200
  * cleanup: remove TABLE::vcol\_set
* [Revision #ac9cc63892](https://github.com/MariaDB/server/commit/ac9cc63892)\
  2018-06-02 16:33:27 +0200
  * cleanup: copy\_data\_between\_tables()
* [Revision #a0db3d714f](https://github.com/MariaDB/server/commit/a0db3d714f)\
  2018-05-31 18:37:52 +0200
  * bugfix: Item\_field::register\_field\_in\_read\_map
* [Revision #3edac3f18d](https://github.com/MariaDB/server/commit/3edac3f18d)\
  2018-05-21 09:51:45 +1000
  * [MDEV-15584](https://jira.mariadb.org/browse/MDEV-15584) Linux use O\_TMPFILE
* [Revision #ced6638773](https://github.com/MariaDB/server/commit/ced6638773)\
  2018-05-30 17:23:51 +0200
  * mysys: ME\_ERROR\_LOG\_ONLY flag
* [Revision #c9061d1102](https://github.com/MariaDB/server/commit/c9061d1102)\
  2018-05-29 23:54:25 +0200
  * mysys: rename ME\_xxx flags to match plugin api
* [Revision #37659ef43b](https://github.com/MariaDB/server/commit/37659ef43b)\
  2018-05-29 23:00:51 +0200
  * mysys: remove dead ME\_xxx flags
* [Revision #9988a423d2](https://github.com/MariaDB/server/commit/9988a423d2)\
  2018-06-04 09:04:03 +0400
  * [MDEV-16379](https://jira.mariadb.org/browse/MDEV-16379) Move Item\_basic\_const::used\_table\_map to Item\_cache
* [Revision #c3a4dcd0f0](https://github.com/MariaDB/server/commit/c3a4dcd0f0)\
  2018-06-03 21:28:50 +0200
  * after merge fixes
* Merge [Revision #cab1d63826](https://github.com/MariaDB/server/commit/cab1d63826) 2018-06-03 10:34:41 -0700 - Merge branch '10.3' into 10.4
* [Revision #ffe83e8e7b](https://github.com/MariaDB/server/commit/ffe83e8e7b)\
  2018-05-31 18:52:32 +0400
  * [MDEV-16351](https://jira.mariadb.org/browse/MDEV-16351) JSON\_OBJECT() treats hybrid functions with boolean arguments as numbers
* [Revision #3ceb4a54a1](https://github.com/MariaDB/server/commit/3ceb4a54a1)\
  2018-05-30 15:22:58 +0400
  * [MDEV-16325](https://jira.mariadb.org/browse/MDEV-16325) CREATE..SELECT..UNION creates a wrong field type for old varchar
* [Revision #d4da8e7c02](https://github.com/MariaDB/server/commit/d4da8e7c02)\
  2018-05-29 16:16:33 +0400
  * [MDEV-16320](https://jira.mariadb.org/browse/MDEV-16320) Replace INT\_ITEM references in sql\_select.cc
* [Revision #840d46b04f](https://github.com/MariaDB/server/commit/840d46b04f)\
  2018-05-29 13:28:48 +0400
  * [MDEV-16316](https://jira.mariadb.org/browse/MDEV-16316) Replace INT\_ITEM references in the code behind ORDER, LIMIT, PROCEDURE clause
* [Revision #637af78383](https://github.com/MariaDB/server/commit/637af78383)\
  2018-05-28 16:57:59 +0400
  * [MDEV-16309](https://jira.mariadb.org/browse/MDEV-16309) Split ::create\_tmp\_field() into virtual methods in Item
* [Revision #13f7ac2269](https://github.com/MariaDB/server/commit/13f7ac2269)\
  2018-05-28 09:36:18 +0300
  * [MDEV-15705](https://jira.mariadb.org/browse/MDEV-15705) Remove global status counter Innodb\_pages0\_read
* [Revision #f584557406](https://github.com/MariaDB/server/commit/f584557406)\
  2018-05-24 14:47:04 +0400
  * [MDEV-9216](https://jira.mariadb.org/browse/MDEV-9216) Split field.cc:make\_field() into virtual methods in Type\_handler
* [Revision #dc5802255d](https://github.com/MariaDB/server/commit/dc5802255d)\
  2018-05-24 09:31:36 +0400
  * [MDEV-16280](https://jira.mariadb.org/browse/MDEV-16280) Add class Bit\_addr
* [Revision #d3ff133390](https://github.com/MariaDB/server/commit/d3ff133390)\
  2018-05-15 23:45:59 +0200
  * [MDEV-12387](https://jira.mariadb.org/browse/MDEV-12387) Push conditions into materialized subqueries
* [Revision #569e3ad1ea](https://github.com/MariaDB/server/commit/569e3ad1ea)\
  2018-05-11 14:20:22 +0400
  * [MDEV-15655](https://jira.mariadb.org/browse/MDEV-15655): Add Linux abstract socket support
* [Revision #08098366d2](https://github.com/MariaDB/server/commit/08098366d2)\
  2018-03-25 13:42:48 +1100
  * [MDEV-15655](https://jira.mariadb.org/browse/MDEV-15655): Add Linux abstract socket support
* [Revision #eaaf004cc1](https://github.com/MariaDB/server/commit/eaaf004cc1)\
  2018-05-07 13:14:49 +0200
  * Update server.cnf section to mariadb-10.4

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
