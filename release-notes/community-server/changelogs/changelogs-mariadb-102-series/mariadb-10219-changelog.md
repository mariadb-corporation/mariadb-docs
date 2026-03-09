# MariaDB 10.2.19 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.19/)[Release Notes](../../old-releases/10.2/10.2.19.md)[Changelog](mariadb-10219-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 13 Nov 2018

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.19.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #32bebfeefb](https://github.com/MariaDB/server/commit/32bebfeefb)\
  2018-11-12 18:19:31 +0200
  * Updated list of unstable tests for 10.2.19
* [Revision #59b87e75d0](https://github.com/MariaDB/server/commit/59b87e75d0)\
  2018-11-12 18:06:41 +0200
  * Fix a comment
* [Revision #85baa03c60](https://github.com/MariaDB/server/commit/85baa03c60)\
  2018-11-06 21:18:49 +0100
  * update results after [CONC-351](https://jira.mariadb.org/browse/CONC-351) fix
* [Revision #4f9c44ed39](https://github.com/MariaDB/server/commit/4f9c44ed39)\
  2018-05-19 12:44:15 +0000
  * adjust MTR code after C/C changed the location of plugin libraries
* [Revision #3f10cbf3e4](https://github.com/MariaDB/server/commit/3f10cbf3e4)\
  2018-05-19 15:13:53 +0000
  * pipe and shared memory protocol should be statically compiled into C/C
* [Revision #1bba3cc2e7](https://github.com/MariaDB/server/commit/1bba3cc2e7)\
  2018-11-06 11:37:15 +0100
  * C/C 3.0.7
* [Revision #4b773ca298](https://github.com/MariaDB/server/commit/4b773ca298)\
  2018-11-12 10:16:28 +0200
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) clean-up: Replace memset() with init()
* [Revision #b290ef8c76](https://github.com/MariaDB/server/commit/b290ef8c76)\
  2018-11-12 01:50:07 +0400
  * [MDEV-17454](https://jira.mariadb.org/browse/MDEV-17454) JSON\_VALID( '{"a":1]' ) evaluates to 1.
* [Revision #a12b8ac8e9](https://github.com/MariaDB/server/commit/a12b8ac8e9)\
  2018-11-09 19:53:40 +0530
  * [MDEV-12575](https://jira.mariadb.org/browse/MDEV-12575): Server crash in AGGR\_OP::put\_record or in JOIN\_CACHE::free or Invalid write in JOIN::make\_aggr\_tables\_info
* [Revision #5cfb043d29](https://github.com/MariaDB/server/commit/5cfb043d29)\
  2018-11-09 22:55:34 +0400
  * [MDEV-16174](https://jira.mariadb.org/browse/MDEV-16174) Assertion \`\`0'\` failed in Type\_handler\_string\_result::make\_sort\_key(uchar\*, Item\*, const SORT\_FIELD\_ATTR\*, Sort\_param\*)
* [Revision #67567f5c9a](https://github.com/MariaDB/server/commit/67567f5c9a)\
  2018-10-14 12:28:46 +0200
  * Implement the CHECK TABLE statement and accept REPAIR and ANALYZE
* [Revision #2d7d19a3cd](https://github.com/MariaDB/server/commit/2d7d19a3cd)\
  2018-11-08 22:54:03 -0800
  * [MDEV-17574](https://jira.mariadb.org/browse/MDEV-17574) SIGSEGV or Assertion \`\`producing\_item != null'\` in Item\_direct\_view\_ref::derived\_field\_transformer\_for\_where upon updating a view
* [Revision #3fbee66499](https://github.com/MariaDB/server/commit/3fbee66499)\
  2018-11-08 14:50:32 +0200
  * [MDEV-17645](https://jira.mariadb.org/browse/MDEV-17645) innodb.log\_file\_name\_debug does not clean up after itself
* [Revision #4142589207](https://github.com/MariaDB/server/commit/4142589207)\
  2018-11-07 12:07:32 -0800
  * [MDEV-17635](https://jira.mariadb.org/browse/MDEV-17635) Server hangs after the query with recursive CTE
* [Revision #c565622c6c](https://github.com/MariaDB/server/commit/c565622c6c)\
  2018-11-07 15:24:30 +0200
  * [MDEV-14528](https://jira.mariadb.org/browse/MDEV-14528) followup.
* [Revision #e82ebb8f06](https://github.com/MariaDB/server/commit/e82ebb8f06)\
  2018-11-07 13:08:00 +0200
  * [MDEV-14528](https://jira.mariadb.org/browse/MDEV-14528): Disable a failing test
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
* [Revision #bdfe2784d5](https://github.com/MariaDB/server/commit/bdfe2784d5)\
  2018-11-06 08:42:30 +0200
  * Unify a test with the 10.3 version
* [Revision #db55b39fb2](https://github.com/MariaDB/server/commit/db55b39fb2)\
  2018-11-05 16:47:14 +0200
  * Revert some InnoDB/XtraDB changes
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
  * [MDEV-17349](https://jira.mariadb.org/browse/MDEV-17349) Assertion \`\`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))'\` failed on concurrent SELECT and DELETE after RENAME from table with index on virtual column
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
* [Revision #ab1ce2204e](https://github.com/MariaDB/server/commit/ab1ce2204e)\
  2018-10-19 09:29:28 +0300
  * [MDEV-17466](https://jira.mariadb.org/browse/MDEV-17466): Remove the debug assertion
* [Revision #abbf169f52](https://github.com/MariaDB/server/commit/abbf169f52)\
  2018-10-19 09:28:21 +0300
  * Remove unused TIMETPF
* [Revision #64d26ec52a](https://github.com/MariaDB/server/commit/64d26ec52a)\
  2018-10-18 12:15:07 +0300
  * Fix the Windows build
* [Revision #56de291978](https://github.com/MariaDB/server/commit/56de291978)\
  2018-10-18 10:10:11 +0300
  * Fix a merge error in commit 28f08d3753eb10a1393a63e6c581d43aad9f93b9
* [Revision #853a0a4368](https://github.com/MariaDB/server/commit/853a0a4368)\
  2018-10-17 09:54:18 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Set innodb\_safe\_truncate=ON by default
* [Revision #dc3f55947e](https://github.com/MariaDB/server/commit/dc3f55947e)\
  2018-10-17 03:26:30 -0700
  * [MDEV-17107](https://jira.mariadb.org/browse/MDEV-17107) Assertion \`\`table\_list->table'\` failed in find\_field\_in\_table\_ref
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
* [Revision #81a5b6ccd5](https://github.com/MariaDB/server/commit/81a5b6ccd5)\
  2018-10-11 22:48:19 +0300
  * [MDEV-17433](https://jira.mariadb.org/browse/MDEV-17433) Allow InnoDB start up with empty ib\_logfile0 from mariadb-backup --prepare
* [Revision #b8944e8972](https://github.com/MariaDB/server/commit/b8944e8972)\
  2018-10-11 22:47:42 +0300
  * Fix a sign mismatch
* [Revision #6319c0b541](https://github.com/MariaDB/server/commit/6319c0b541)\
  2018-10-11 15:10:13 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Replace innodb\_unsafe\_truncate with innodb\_safe\_truncate
* [Revision #3448ceb02a](https://github.com/MariaDB/server/commit/3448ceb02a)\
  2018-10-10 19:19:29 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Implement innodb\_unsafe\_truncate=ON for compatibility
* [Revision #940f0c78a4](https://github.com/MariaDB/server/commit/940f0c78a4)\
  2018-10-10 14:10:29 +0300
  * [MDEV-11487](https://jira.mariadb.org/browse/MDEV-11487): Make row\_ins\_index\_entry\_set\_vals() static
* [Revision #8d116d1686](https://github.com/MariaDB/server/commit/8d116d1686)\
  2018-10-10 14:39:57 +0300
  * [MDEV-17181](https://jira.mariadb.org/browse/MDEV-17181): rocksdb.allow\_to\_start\_after\_corruption fails on current 10.2
* [Revision #00b6c7d8fc](https://github.com/MariaDB/server/commit/00b6c7d8fc)\
  2018-10-10 06:31:43 +0300
  * [MDEV-16946](https://jira.mariadb.org/browse/MDEV-16946) innodb.alter\_kill failed in buildbot with wrong result
* [Revision #8b371e4b13](https://github.com/MariaDB/server/commit/8b371e4b13)\
  2018-10-09 17:01:49 +0300
  * [MDEV-16577](https://jira.mariadb.org/browse/MDEV-16577): rocksdb.issue255 fails in buildbot
* [Revision #e9d9ca8c44](https://github.com/MariaDB/server/commit/e9d9ca8c44)\
  2018-10-08 21:40:18 +0530
  * [MDEV-16980](https://jira.mariadb.org/browse/MDEV-16980) Wrongly set tablename len while opening the table for purge thread
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
  2018-10-05 16:45:27 +0530
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
  * [MDEV-17215](https://jira.mariadb.org/browse/MDEV-17215) Assertion \`\`rw\_lock\_own(dict\_operation\_lock, RW\_LOCK\_S) || node->vcol\_info.is\_used()'\` failed
* [Revision #0f709912fb](https://github.com/MariaDB/server/commit/0f709912fb)\
  2018-09-27 17:57:27 +0300
  * [MDEV-17306](https://jira.mariadb.org/browse/MDEV-17306) rw\_lock\_x\_lock\_wait\_func() double increments rw\_x\_spin\_round\_count
* [Revision #f77071e0e8](https://github.com/MariaDB/server/commit/f77071e0e8)\
  2018-09-26 16:58:42 +0300
  * Remove unused code
* [Revision #fc34e4c067](https://github.com/MariaDB/server/commit/fc34e4c067)\
  2018-09-10 16:10:26 +0300
  * [MDEV-17161](https://jira.mariadb.org/browse/MDEV-17161) TRUNCATE TABLE fails after upgrade from 10.1
* [Revision #75f8e86f57](https://github.com/MariaDB/server/commit/75f8e86f57)\
  2018-09-10 14:59:58 +0300
  * [MDEV-17158](https://jira.mariadb.org/browse/MDEV-17158) TRUNCATE is not atomic after [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564)
* [Revision #99e36a7157](https://github.com/MariaDB/server/commit/99e36a7157)\
  2018-09-09 11:34:56 +0300
  * Follow-up to [MDEV-13407](https://jira.mariadb.org/browse/MDEV-13407): Remove fil\_wait\_crypt\_bg\_threads()
* [Revision #980d1bf1a9](https://github.com/MariaDB/server/commit/980d1bf1a9)\
  2018-09-07 17:24:31 +0300
  * [MDEV-14717](https://jira.mariadb.org/browse/MDEV-14717): Prevent crash-downgrade to earlier [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md)
* [Revision #73ed19e44f](https://github.com/MariaDB/server/commit/73ed19e44f)\
  2018-09-06 11:51:50 +0300
  * [MDEV-14585](https://jira.mariadb.org/browse/MDEV-14585) Automatically remove #sql- tables in InnoDB dictionary during recovery
* [Revision #8dcacd3b01](https://github.com/MariaDB/server/commit/8dcacd3b01)\
  2018-09-06 11:47:54 +0300
  * Follow-up to [MDEV-13407](https://jira.mariadb.org/browse/MDEV-13407) innodb.drop\_table\_background failed in buildbot with "Tablespace for table exists"
* [Revision #754727bb8a](https://github.com/MariaDB/server/commit/754727bb8a)\
  2018-09-06 11:40:27 +0300
  * [MDEV-14378](https://jira.mariadb.org/browse/MDEV-14378) In ALGORITHM=INPLACE, use a common name for the intermediate tables or partitions
* [Revision #cf2a4426a2](https://github.com/MariaDB/server/commit/cf2a4426a2)\
  2018-09-06 10:32:49 +0300
  * [MDEV-14717](https://jira.mariadb.org/browse/MDEV-14717) RENAME TABLE in InnoDB is not crash-safe
* [Revision #e67b1070bb](https://github.com/MariaDB/server/commit/e67b1070bb)\
  2018-08-28 22:41:17 +0300
  * [MDEV-17049](https://jira.mariadb.org/browse/MDEV-17049) Enable innodb\_undo tests on buildbot
* [Revision #055a3334ad](https://github.com/MariaDB/server/commit/055a3334ad)\
  2018-08-28 13:43:06 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) mariadb-backup does not work with TRUNCATE
* [Revision #d913f6611c](https://github.com/MariaDB/server/commit/d913f6611c)\
  2018-09-25 10:06:06 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
