# MariaDB 10.5.26 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.26](https://downloads.mariadb.org/mariadb/10.5.26/)[Release Notes](../../old-releases/10.5/10.5.26.md)[Changelog](mariadb-10-5-26-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 8 Aug 2024

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.26.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.34](../changelogs-mariadb-10-4-series/mariadb-10-4-34-changelog.md)
* [Revision #7a5b8bf0f5](https://github.com/MariaDB/server/commit/7a5b8bf0f5)\
  2024-08-03 08:47:17 +0200
  * lost in editinig line added
* [Revision #001608de7e](https://github.com/MariaDB/server/commit/001608de7e)\
  2024-07-31 14:14:18 -0600
  * [MDEV-15393](https://jira.mariadb.org/browse/MDEV-15393): Fix rpl\_mysqldump\_gtid\_slave\_pos
* [Revision #533e6d5d13](https://github.com/MariaDB/server/commit/533e6d5d13)\
  2024-07-30 23:59:00 +0530
  * [MDEV-34670](https://jira.mariadb.org/browse/MDEV-34670) IMPORT TABLESPACE unnecessary traverses tablespace list
* [Revision #fdda8171b2](https://github.com/MariaDB/server/commit/fdda8171b2)\
  2024-07-30 17:49:09 +0300
  * [MDEV-34580](https://jira.mariadb.org/browse/MDEV-34580): Assertion \`(key\_part->key\_part\_flag & 4) == 0' failed key\_hashnr
* [Revision #c038b3c05e](https://github.com/MariaDB/server/commit/c038b3c05e)\
  2024-07-30 12:05:38 +0530
  * [MDEV-34181](https://jira.mariadb.org/browse/MDEV-34181) Instant table aborts after discard tablespace
* [Revision #48b256a7e2](https://github.com/MariaDB/server/commit/48b256a7e2)\
  2024-07-02 12:27:41 +1100
  * [MDEV-34506](https://jira.mariadb.org/browse/MDEV-34506) 2nd execution name resolution problem with pushdown into unions
* [Revision #7e5c9ccda5](https://github.com/MariaDB/server/commit/7e5c9ccda5)\
  2024-07-29 15:04:16 +0300
  * [MDEV-34502](https://jira.mariadb.org/browse/MDEV-34502) fixup: Do not cripple MSAN
* [Revision #232d7a5e2d](https://github.com/MariaDB/server/commit/232d7a5e2d)\
  2024-07-29 10:58:09 +0300
  * [MDEV-34565](https://jira.mariadb.org/browse/MDEV-34565): SIGILL due to OS not supporting AVX512
* [Revision #0939bfc093](https://github.com/MariaDB/server/commit/0939bfc093)\
  2024-07-27 12:52:51 +1000
  * [MDEV-19052](https://jira.mariadb.org/browse/MDEV-19052) main.win postfix --view-protocol compat
* [Revision #7788593547](https://github.com/MariaDB/server/commit/7788593547)\
  2024-06-14 14:05:48 +1000
  * [MDEV-19052](https://jira.mariadb.org/browse/MDEV-19052) Range-type window frame supports only numeric datatype
* [Revision #26f31bdd52](https://github.com/MariaDB/server/commit/26f31bdd52)\
  2024-07-24 16:41:29 +0200
  * The test should be not for AddressSanitizer used becouse stack check tests and this check switched off
* [Revision #c91aeb3771](https://github.com/MariaDB/server/commit/c91aeb3771)\
  2024-07-23 15:34:23 +0700
  * [MDEV-34634](https://jira.mariadb.org/browse/MDEV-34634) Types mismatch when cloning items causes debug assertion
* [Revision #b8f92ade57](https://github.com/MariaDB/server/commit/b8f92ade57)\
  2024-07-15 17:50:37 +0300
  * [MDEV-15393](https://jira.mariadb.org/browse/MDEV-15393) gtid\_slave\_pos duplicate key errors after mysqldump restore
* [Revision #b8b6cab2d7](https://github.com/MariaDB/server/commit/b8b6cab2d7)\
  2024-07-19 13:07:17 +0200
  * Fix view protocol
* [Revision #9dafde575f](https://github.com/MariaDB/server/commit/9dafde575f)\
  2024-07-18 08:15:43 +0400
  * Additional tests for [MDEV-28345](https://jira.mariadb.org/browse/MDEV-28345) ASAN: use-after-poison or unknown-crash in my\_strtod\_int from charset\_info\_st::strntod or test\_if\_number
* [Revision #a061ae1079](https://github.com/MariaDB/server/commit/a061ae1079)\
  2024-07-17 12:56:45 -0600
  * [MDEV-33921](https://jira.mariadb.org/browse/MDEV-33921): Fix rpl\_xa\_empty\_transaction.test
* [Revision #36b867ad50](https://github.com/MariaDB/server/commit/36b867ad50)\
  2024-07-09 15:11:18 +0200
  * [MDEV-34353](https://jira.mariadb.org/browse/MDEV-34353) Revert "don't wait indefinitely for signal handler in --bootstrap"
* [Revision #8d813f080b](https://github.com/MariaDB/server/commit/8d813f080b)\
  2024-07-06 13:36:35 +0200
  * [MDEV-34539](https://jira.mariadb.org/browse/MDEV-34539) Invalid "use" and "Schema" in slow query log file with multi-line schema
* [Revision #f12634f5a4](https://github.com/MariaDB/server/commit/f12634f5a4)\
  2024-07-04 14:10:37 +0200
  * [MDEV-34530](https://jira.mariadb.org/browse/MDEV-34530) dead code in the thr\_rwlock.c
* [Revision #7ba12d42de](https://github.com/MariaDB/server/commit/7ba12d42de)\
  2024-06-21 17:10:49 +0200
  * [MDEV-34434](https://jira.mariadb.org/browse/MDEV-34434) Hide password passed on commandline from xtrabackup\_info
* [Revision #d20518168a](https://github.com/MariaDB/server/commit/d20518168a)\
  2024-06-17 15:54:30 +0200
  * also protect the /\*!999999 sandbox comment
* [Revision #d60f5c11ea](https://github.com/MariaDB/server/commit/d60f5c11ea)\
  2024-06-14 17:32:52 +0200
  * [MDEV-34318](https://jira.mariadb.org/browse/MDEV-34318) mariadb-dump SQL syntax error with MAX\_STATEMENT\_TIME against Percona MySQL server
* [Revision #dea5746de2](https://github.com/MariaDB/server/commit/dea5746de2)\
  2024-06-16 18:04:27 +0200
  * [MDEV-32155](https://jira.mariadb.org/browse/MDEV-32155) MariaDB Server crashes with ill-formed partitions
* [Revision #8ac30517af](https://github.com/MariaDB/server/commit/8ac30517af)\
  2024-06-14 17:23:55 +0200
  * [MDEV-34384](https://jira.mariadb.org/browse/MDEV-34384) restorecon call in RPM POSTIN script has hardcoded datadir path
* [Revision #1f28350b59](https://github.com/MariaDB/server/commit/1f28350b59)\
  2024-07-09 23:44:44 +0530
  * [MDEV-32456](https://jira.mariadb.org/browse/MDEV-32456): incorrect result of gis function in view protocol
* [Revision #4a89f79b6a](https://github.com/MariaDB/server/commit/4a89f79b6a)\
  2024-06-21 17:17:47 +0000
  * Refactor import \* with only required imports
* [Revision #008bddaa6c](https://github.com/MariaDB/server/commit/008bddaa6c)\
  2024-06-03 19:43:21 +0000
  * GitLab CI Upgrade CentOS 8 to CentOS 9 build
* [Revision #e7c2e25ba8](https://github.com/MariaDB/server/commit/e7c2e25ba8)\
  2024-07-17 13:08:55 +0200
  * new CC version
* [Revision #7478fabcff](https://github.com/MariaDB/server/commit/7478fabcff)\
  2024-07-17 09:02:58 +0200
  * new PCRE2-10.44
* [Revision #b777b749ad](https://github.com/MariaDB/server/commit/b777b749ad)\
  2024-07-17 08:39:43 +0400
  * [MDEV-28345](https://jira.mariadb.org/browse/MDEV-28345) ASAN: use-after-poison or unknown-crash in my\_strtod\_int from charset\_info\_st::strntod or test\_if\_number
* [Revision #383d53edbc](https://github.com/MariaDB/server/commit/383d53edbc)\
  2024-06-04 17:38:14 +0900
  * [MDEV-21166](https://jira.mariadb.org/browse/MDEV-21166) Add Mroonga initialized check to Mroonga UDFs
* [Revision #49dff5a4b6](https://github.com/MariaDB/server/commit/49dff5a4b6)\
  2024-03-07 19:09:39 -0500
  * [MDEV-34604](https://jira.mariadb.org/browse/MDEV-34604) mytop - fix specifying filters in .mytop
* [Revision #03a350378a](https://github.com/MariaDB/server/commit/03a350378a)\
  2024-07-17 08:54:28 +0800
  * [MDEV-30408](https://jira.mariadb.org/browse/MDEV-30408) Reset explicit\_limit in exists2in
* [Revision #8416fd323c](https://github.com/MariaDB/server/commit/8416fd323c)\
  2024-07-08 16:14:44 +0800
  * [MDEV-32627](https://jira.mariadb.org/browse/MDEV-32627) \[fixup] Spider: Fix conn key length
* [Revision #20d99f3f86](https://github.com/MariaDB/server/commit/20d99f3f86)\
  2024-06-04 14:51:25 +1000
  * [MDEV-32627](https://jira.mariadb.org/browse/MDEV-32627) Distinguish between absence of a keyword and empty value for the keyword
* [Revision #6f3baec4f5](https://github.com/MariaDB/server/commit/6f3baec4f5)\
  2024-06-11 16:30:00 +1000
  * [MDEV-32627](https://jira.mariadb.org/browse/MDEV-32627) Spider: add tests for connection param overriding
* [Revision #62dfd0c09d](https://github.com/MariaDB/server/commit/62dfd0c09d)\
  2024-06-14 09:51:44 +0300
  * [MDEV-33837](https://jira.mariadb.org/browse/MDEV-33837): Workaround chown warnings
* [Revision #972879f413](https://github.com/MariaDB/server/commit/972879f413)\
  2024-04-01 14:03:46 +0700
  * [MDEV-33010](https://jira.mariadb.org/browse/MDEV-33010) Crash when pushing condition with CHARSET()/COERCIBILITY() into derived table
* [Revision #384ec03e48](https://github.com/MariaDB/server/commit/384ec03e48)\
  2024-06-21 19:27:22 +0800
  * [MDEV-34421](https://jira.mariadb.org/browse/MDEV-34421) Check the SQL command when resolving storage engine
* [Revision #132270d3de](https://github.com/MariaDB/server/commit/132270d3de)\
  2024-07-11 11:16:46 +0800
  * [MDEV-34541](https://jira.mariadb.org/browse/MDEV-34541) Clean up spider self reference check
* [Revision #0bb9862888](https://github.com/MariaDB/server/commit/0bb9862888)\
  2024-07-05 16:32:54 +0800
  * [MDEV-29962](https://jira.mariadb.org/browse/MDEV-29962) Spider: creates connections if needed before lock\_tables()
* [Revision #696c2497fc](https://github.com/MariaDB/server/commit/696c2497fc)\
  2024-07-08 16:22:50 +0800
  * [MDEV-27902](https://jira.mariadb.org/browse/MDEV-27902) Spider check trx and get conn in rnd\_next()
* [Revision #85a36958e3](https://github.com/MariaDB/server/commit/85a36958e3)\
  2024-07-08 16:07:53 +0800
  * [MDEV-27902](https://jira.mariadb.org/browse/MDEV-27902) Some Spider code documentation regarding first\_link\_idx and remote HANDLER commands
* [Revision #14c4050992](https://github.com/MariaDB/server/commit/14c4050992)\
  2024-07-11 13:48:48 +0800
  * [MDEV-32492](https://jira.mariadb.org/browse/MDEV-32492) Delete and remove trx\_ha on spider share mismatch
* [Revision #653050ac84](https://github.com/MariaDB/server/commit/653050ac84)\
  2024-07-01 17:41:23 +0800
  * [MDEV-32492](https://jira.mariadb.org/browse/MDEV-32492) [MDEV-29676](https://jira.mariadb.org/browse/MDEV-29676) Spider: some code documentation and cleanup
* [Revision #26192a4665](https://github.com/MariaDB/server/commit/26192a4665)\
  2024-07-16 09:30:20 +0200
  * [MDEV-33265](https://jira.mariadb.org/browse/MDEV-33265) mariadb-secure-installation fails with --defaults-group-suffix
* [Revision #3a38a7a4ac](https://github.com/MariaDB/server/commit/3a38a7a4ac)\
  2024-07-15 19:11:39 +0200
  * New wolfssl v5.7.2-stable
* [Revision #cf1c381bb8](https://github.com/MariaDB/server/commit/cf1c381bb8)\
  2024-07-05 14:26:13 +1000
  * [MDEV-34099](https://jira.mariadb.org/browse/MDEV-34099): AddressSanitizer running out of memory regardless of stack\_thread size
* [Revision #405613ebb5](https://github.com/MariaDB/server/commit/405613ebb5)\
  2024-07-03 15:42:21 +0700
  * [MDEV-34490](https://jira.mariadb.org/browse/MDEV-34490) get\_copy() and build\_clone() may return an instance of an ancestor class instead of a copy/clone
* [Revision #46d95ae265](https://github.com/MariaDB/server/commit/46d95ae265)\
  2024-07-15 14:44:59 +0530
  * [MDEV-34474](https://jira.mariadb.org/browse/MDEV-34474) InnoDB: Failing assertion: stat\_n\_leaf\_pages > 0 in ha\_innobase::estimate\_rows\_upper\_bound
* [Revision #3b956f8329](https://github.com/MariaDB/server/commit/3b956f8329)\
  2024-07-03 10:22:13 +0800
  * [MDEV-34449](https://jira.mariadb.org/browse/MDEV-34449) Default ha\_spider::bulk\_size to 0.
* [Revision #3c508d4c71](https://github.com/MariaDB/server/commit/3c508d4c71)\
  2024-07-12 21:37:48 +0200
  * [MDEV-34581](https://jira.mariadb.org/browse/MDEV-34581): Fix flashback mode man pages
* [Revision #00d2c7f7f4](https://github.com/MariaDB/server/commit/00d2c7f7f4)\
  2024-07-10 19:34:53 +0530
  * [MDEV-34542](https://jira.mariadb.org/browse/MDEV-34542) Assertion \`lock\_trx\_has\_sys\_table\_locks(trx) == null' failed in void row\_mysql\_unfreeze\_data\_dictionary(trx\_t\*)
* [Revision #3662f8ca89](https://github.com/MariaDB/server/commit/3662f8ca89)\
  2024-07-12 12:45:11 +0530
  * [MDEV-34543](https://jira.mariadb.org/browse/MDEV-34543) Shutdown hangs while freeing the asynchronous i/o slots
* [Revision #e8bcc4e455](https://github.com/MariaDB/server/commit/e8bcc4e455)\
  2024-07-11 17:35:13 +1000
  * [MDEV-34568](https://jira.mariadb.org/browse/MDEV-34568) rpl.rpl\_mdev12179 - correct for Windows
* [Revision #aae3233c4f](https://github.com/MariaDB/server/commit/aae3233c4f)\
  2024-05-04 19:50:55 +0700
  * [MDEV-34041](https://jira.mariadb.org/browse/MDEV-34041) Display additional information for materialized subqueries in EXPLAIN/ANALYZE FORMAT=JSON
* [Revision #a5e4c34991](https://github.com/MariaDB/server/commit/a5e4c34991)\
  2024-07-09 17:37:04 +0200
  * [MDEV-32608](https://jira.mariadb.org/browse/MDEV-32608): Expression with constant subquery causes a crash in pushdown from HAVING
* [Revision #eaf7c0cbea](https://github.com/MariaDB/server/commit/eaf7c0cbea)\
  2024-07-11 16:51:39 +1000
  * mtr: remove not\_valgrind\_build
* [Revision #ea9869504d](https://github.com/MariaDB/server/commit/ea9869504d)\
  2024-06-20 12:21:48 -0600
  * [MDEV-33921](https://jira.mariadb.org/browse/MDEV-33921): Replication breaks when filtering two-phase XA transactions
* [Revision #9fdc0e5440](https://github.com/MariaDB/server/commit/9fdc0e5440)\
  2024-07-10 14:14:35 +0200
  * [MDEV-34546](https://jira.mariadb.org/browse/MDEV-34546) Windows - no error log entries after startup in XAMPP
* [Revision #60125a77b7](https://github.com/MariaDB/server/commit/60125a77b7)\
  2024-07-10 11:43:03 +0530
  * [MDEV-34474](https://jira.mariadb.org/browse/MDEV-34474) InnoDB: Failing assertion: stat\_n\_leaf\_pages > 0 in ha\_innobase::estimate\_rows\_upper\_bound
* [Revision #d0a2d4e755](https://github.com/MariaDB/server/commit/d0a2d4e755)\
  2024-07-04 02:43:32 +0200
  * galera mtr tests: correction of inaccuracies in warnings suppressions
* [Revision #f942927141](https://github.com/MariaDB/server/commit/f942927141)\
  2024-07-03 19:04:24 +0200
  * [MDEV-21538](https://jira.mariadb.org/browse/MDEV-21538): galera\_desync\_overlapped test result content mismatch
* [Revision #8d61a94b8b](https://github.com/MariaDB/server/commit/8d61a94b8b)\
  2024-06-27 15:10:25 +0300
  * [MDEV-34477](https://jira.mariadb.org/browse/MDEV-34477) galera.galera\_gcache\_recover\_manytrx sporadic failures
* [Revision #b7718a1c1c](https://github.com/MariaDB/server/commit/b7718a1c1c)\
  2023-12-06 18:31:23 +0300
  * [MDEV-32738](https://jira.mariadb.org/browse/MDEV-32738): Don't roll back high-prio txn waiting on a lock in InnoDB
* [Revision #744580d5a7](https://github.com/MariaDB/server/commit/744580d5a7)\
  2024-06-10 04:08:42 -0600
  * [MDEV-32892](https://jira.mariadb.org/browse/MDEV-32892): IO Thread Reports False Error When Stopped During Connecting to Primary
* [Revision #d1e5fa8917](https://github.com/MariaDB/server/commit/d1e5fa8917)\
  2024-06-11 13:49:08 +0400
  * [MDEV-34305](https://jira.mariadb.org/browse/MDEV-34305) Redundant truncation errors/warnings with optimizer\_trace enabled
* [Revision #df35072c8d](https://github.com/MariaDB/server/commit/df35072c8d)\
  2024-05-11 00:37:05 +0000
  * Refactor GitLab cppcheck and update SAST ignorelists
* [Revision #215fab68db](https://github.com/MariaDB/server/commit/215fab68db)\
  2024-05-13 22:19:38 +0000
  * Perform simple fixes for cppcheck findings
* [Revision #72ceae7314](https://github.com/MariaDB/server/commit/72ceae7314)\
  2024-07-08 10:23:52 +0300
  * [MDEV-34510](https://jira.mariadb.org/browse/MDEV-34510): UBSAN: overflow on adding an unsigned offset
* [Revision #33964984ad](https://github.com/MariaDB/server/commit/33964984ad)\
  2024-07-07 12:06:19 +0300
  * [MDEV-34522](https://jira.mariadb.org/browse/MDEV-34522) Index for (specific) Aria table is created as corrupted
* [Revision #cbc1898e82](https://github.com/MariaDB/server/commit/cbc1898e82)\
  2021-06-09 11:03:03 -0600
  * [MDEV-25607](https://jira.mariadb.org/browse/MDEV-25607): Auto-generated DELETE from HEAP table can break replication
* [Revision #834c013b64](https://github.com/MariaDB/server/commit/834c013b64)\
  2024-07-05 15:26:05 +0530
  * [MDEV-34519](https://jira.mariadb.org/browse/MDEV-34519) innodb\_log\_checkpoint\_now crashes when innodb\_read\_only is enabled
* [Revision #9e8546e2bd](https://github.com/MariaDB/server/commit/9e8546e2bd)\
  2023-03-11 00:27:42 +0000
  * Fix a stack overflow in pinbox allocator
* [Revision #6cb896a639](https://github.com/MariaDB/server/commit/6cb896a639)\
  2024-06-18 19:40:05 +0200
  * [MDEV-29363](https://jira.mariadb.org/browse/MDEV-29363): Constant subquery causing a crash in pushdown optimization
* [Revision #a4ef05d0d5](https://github.com/MariaDB/server/commit/a4ef05d0d5)\
  2024-07-03 12:01:28 +0200
  * Fix compiler errors
* [Revision #25c6e3e4b7](https://github.com/MariaDB/server/commit/25c6e3e4b7)\
  2024-07-01 14:09:04 +1000
  * [MDEV-34502](https://jira.mariadb.org/browse/MDEV-34502) InnoDB debug mode build - asserts with Valgrind
* [Revision #2739b5f5f8](https://github.com/MariaDB/server/commit/2739b5f5f8)\
  2024-06-29 10:41:04 +0300
  * [MDEV-34494](https://jira.mariadb.org/browse/MDEV-34494) Add server\_uid global variable and add it to error log at startup
* [Revision #d8c9c5ead6](https://github.com/MariaDB/server/commit/d8c9c5ead6)\
  2024-06-28 18:41:05 +0300
  * [MDEV-34491](https://jira.mariadb.org/browse/MDEV-34491) Setting log\_slow\_admin="" at startup should be converted to log\_slow\_admin=ALL
* [Revision #090cecd5e8](https://github.com/MariaDB/server/commit/090cecd5e8)\
  2023-08-30 12:22:07 +0700
  * [MDEV-31933](https://jira.mariadb.org/browse/MDEV-31933): Make working view-protocol + ps-protocol (running two protocols together)
* [Revision #d046b13e7b](https://github.com/MariaDB/server/commit/d046b13e7b)\
  2024-06-25 09:27:11 +0400
  * [MDEV-20548](https://jira.mariadb.org/browse/MDEV-20548) Unexpected error on CREATE..SELECT HEX(num)
* [Revision #e7b76f87c4](https://github.com/MariaDB/server/commit/e7b76f87c4)\
  2024-06-21 18:21:32 +1000
  * [MDEV-34437](https://jira.mariadb.org/browse/MDEV-34437) restrict port and extra-port to tcp valid values
* [Revision #54b7a879e9](https://github.com/MariaDB/server/commit/54b7a879e9)\
  2024-06-29 09:48:38 +1000
  * [MDEV-34313](https://jira.mariadb.org/browse/MDEV-34313) WITHOUT\_SERVER/WSREP postfix
* [Revision #9e74a7f4f3](https://github.com/MariaDB/server/commit/9e74a7f4f3)\
  2024-04-22 17:53:06 +0700
  * Removing [MDEV-27871](https://jira.mariadb.org/browse/MDEV-27871) from tastcases because it is not a bug
* [Revision #55db59f16d](https://github.com/MariaDB/server/commit/55db59f16d)\
  2023-12-06 19:48:53 +0000
  * \[[MDEV-28162](https://jira.mariadb.org/browse/MDEV-28162)] Replace PFS\_atomic with std::atomic
* [Revision #d5bad49011](https://github.com/MariaDB/server/commit/d5bad49011)\
  2024-06-07 16:56:17 +1000
  * [MDEV-34313](https://jira.mariadb.org/browse/MDEV-34313): compile WITHOUT\_SERVER and WSREP=ON
* [Revision #53a4867837](https://github.com/MariaDB/server/commit/53a4867837)\
  2024-06-06 15:53:16 +1000
  * [MDEV-34313](https://jira.mariadb.org/browse/MDEV-34313): compiler mariadb-binlog WITHOUT\_SERVER
* [Revision #ad0ee8cdb9](https://github.com/MariaDB/server/commit/ad0ee8cdb9)\
  2024-06-25 14:22:25 +0800
  * [MDEV-33746](https://jira.mariadb.org/browse/MDEV-33746) \[fixup] Add suggested overrides in oqgraph
* [Revision #01289dac41](https://github.com/MariaDB/server/commit/01289dac41)\
  2024-06-11 16:40:53 +1000
  * [MDEV-34361](https://jira.mariadb.org/browse/MDEV-34361) Split my.cnf in the spider suite.
* [Revision #aebd2397cc](https://github.com/MariaDB/server/commit/aebd2397cc)\
  2024-06-17 14:08:20 +0800
  * [MDEV-34404](https://jira.mariadb.org/browse/MDEV-34404) Use safe\_str in spider udfs to avoid passing NULL str
* [Revision #8b169949d6](https://github.com/MariaDB/server/commit/8b169949d6)\
  2024-06-24 21:51:19 +0700
  * [MDEV-24411](https://jira.mariadb.org/browse/MDEV-24411): Trigger doesn't work correctly with bulk insert
* [Revision #d513a4ce74](https://github.com/MariaDB/server/commit/d513a4ce74)\
  2024-04-30 10:39:20 +1100
  * [MDEV-19520](https://jira.mariadb.org/browse/MDEV-19520) Extend condition normalization to include 'NOT a'
* [Revision #d9dd673fee](https://github.com/MariaDB/server/commit/d9dd673fee)\
  2024-06-24 12:08:13 +0300
  * [MDEV-12008](https://jira.mariadb.org/browse/MDEV-12008) fixup: Do not add a new error code
* [Revision #acc077ffa1](https://github.com/MariaDB/server/commit/acc077ffa1)\
  2024-06-24 10:39:13 +0300
  * [MDEV-34443](https://jira.mariadb.org/browse/MDEV-34443) ha\_innobase::info\_low() does not distinguish HA\_STATUS\_VARIABLE\_EXTRA
* [Revision #3d2e54ff8c](https://github.com/MariaDB/server/commit/3d2e54ff8c)\
  2024-06-11 10:28:10 +0200
  * [MDEV-20053](https://jira.mariadb.org/browse/MDEV-20053): update systemd unit
* [Revision #105473233d](https://github.com/MariaDB/server/commit/105473233d)\
  2024-06-11 10:19:55 +0200
  * [MDEV-20053](https://jira.mariadb.org/browse/MDEV-20053): set @sbindir@ for scripts
* [Revision #9e800eda86](https://github.com/MariaDB/server/commit/9e800eda86)\
  2024-03-19 08:50:19 +1200
  * [MDEV-32583](https://jira.mariadb.org/browse/MDEV-32583) UUID() should be treated as stochastic for the purposes of forcing query materialization
* [Revision #5979dcf95b](https://github.com/MariaDB/server/commit/5979dcf95b)\
  2024-06-21 12:38:19 +0530
  * [MDEV-34435](https://jira.mariadb.org/browse/MDEV-34435) Increase code coverage for debug\_dbug test case during startup
* [Revision #db0c28eff8](https://github.com/MariaDB/server/commit/db0c28eff8)\
  2024-06-12 09:46:26 -0400
  * [MDEV-33746](https://jira.mariadb.org/browse/MDEV-33746) Supply missing override markings
* [Revision #ab448d4b34](https://github.com/MariaDB/server/commit/ab448d4b34)\
  2024-06-20 17:54:57 +0530
  * [MDEV-34389](https://jira.mariadb.org/browse/MDEV-34389) Avoid log overwrite in early recovery
* [Revision #6cecf61a59](https://github.com/MariaDB/server/commit/6cecf61a59)\
  2024-06-18 13:03:56 +0400
  * [MDEV-34417](https://jira.mariadb.org/browse/MDEV-34417) Wrong result set with utf8mb4\_danish\_ci and BNLH join
* [Revision #2f0e7f665c](https://github.com/MariaDB/server/commit/2f0e7f665c)\
  2024-06-14 15:31:39 +0200
  * galera: syncing SST scripts code with the following versions
* [Revision #1001dae186](https://github.com/MariaDB/server/commit/1001dae186)\
  2024-05-29 08:59:44 +0300
  * [MDEV-12008](https://jira.mariadb.org/browse/MDEV-12008) : Change error code for Galera unkillable threads
* [Revision #cfa6143453](https://github.com/MariaDB/server/commit/cfa6143453)\
  2024-06-19 10:01:30 +0400
  * [MDEV-27966](https://jira.mariadb.org/browse/MDEV-27966) Assertion `fixed()' failed and Assertion` fixed == 1' failed, both in Item\_func\_concat::val\_str on SELECT after INSERT with collation utf32\_bin on utf8\_bin table
* [Revision #6cab2f75fe](https://github.com/MariaDB/server/commit/6cab2f75fe)\
  2024-06-18 06:52:16 -0600
  * [MDEV-23857](https://jira.mariadb.org/browse/MDEV-23857): replication master password length
* [Revision #0e25cc51a9](https://github.com/MariaDB/server/commit/0e25cc51a9)\
  2024-06-18 06:12:57 -0600
  * [MDEV-34397](https://jira.mariadb.org/browse/MDEV-34397): "delete si" rather than "my\_free(si)" in THD::register\_slave()
* [Revision #10fbd1ce51](https://github.com/MariaDB/server/commit/10fbd1ce51)\
  2024-06-04 22:58:25 +0000
  * [MDEV-34168](https://jira.mariadb.org/browse/MDEV-34168): Extend perror utility to print link to KB page
* [Revision #2eda310b15](https://github.com/MariaDB/server/commit/2eda310b15)\
  2024-06-14 16:56:10 +0300
  * Restore test coverage for [MDEV-18956](https://jira.mariadb.org/browse/MDEV-18956)
* [Revision #0903276eae](https://github.com/MariaDB/server/commit/0903276eae)\
  2024-06-14 13:41:03 +0300
  * [MDEV-30651](https://jira.mariadb.org/browse/MDEV-30651): Assertion \`sel->quick' in make\_range\_rowid\_filters, followup
* [Revision #a2066b2400](https://github.com/MariaDB/server/commit/a2066b2400)\
  2024-06-11 16:16:11 +0300
  * [MDEV-30651](https://jira.mariadb.org/browse/MDEV-30651): Assertion \`sel->quick' in make\_range\_rowid\_filters
* [Revision #b47bd3f8bf](https://github.com/MariaDB/server/commit/b47bd3f8bf)\
  2024-06-14 12:46:56 +0300
  * [MDEV-33875](https://jira.mariadb.org/browse/MDEV-33875): ORDER BY DESC causes ROWID Filter slowdown
* [Revision #956bcf8f49](https://github.com/MariaDB/server/commit/956bcf8f49)\
  2024-06-15 16:55:08 +0300
  * Change mysqldump to use DO instead of 'SELECT' for storing sequences.
* [Revision #fef32fd9ad](https://github.com/MariaDB/server/commit/fef32fd9ad)\
  2024-06-15 14:26:07 +0300
  * [MDEV-34406](https://jira.mariadb.org/browse/MDEV-34406) Enhance mariadb\_upgrade to print failing query in case of error
* [Revision #4b4c371fe7](https://github.com/MariaDB/server/commit/4b4c371fe7)\
  2024-06-14 13:21:19 +0300
  * [MDEV-34297](https://jira.mariadb.org/browse/MDEV-34297) fixup: -Wconversion on 32-bit
* [Revision #3271588bb7](https://github.com/MariaDB/server/commit/3271588bb7)\
  2024-06-14 12:46:02 +0530
  * [MDEV-34381](https://jira.mariadb.org/browse/MDEV-34381) During innodb\_undo\_truncate=ON recovery, InnoDB may fail to shrink undo\* files
* [Revision #dd13243b0d](https://github.com/MariaDB/server/commit/dd13243b0d)\
  2024-06-13 19:42:18 +0300
  * [MDEV-33161](https://jira.mariadb.org/browse/MDEV-33161) fixup: CMAKE\_CXX\_FLAGS=-DEXTRA\_DEBUG
* [Revision #d3a7e46bb4](https://github.com/MariaDB/server/commit/d3a7e46bb4)\
  2024-06-11 08:21:28 -0600
  * [MDEV-34365](https://jira.mariadb.org/browse/MDEV-34365): UBSAN runtime error: call to function io\_callback(tpool::aiocb\*)
* [Revision #f2eda61579](https://github.com/MariaDB/server/commit/f2eda61579)\
  2024-06-10 21:56:22 +0200
  * [MDEV-33616](https://jira.mariadb.org/browse/MDEV-33616) workaround libmariadb bug : mysql\_errno = 0 on failed connection
* [Revision #d524cb5b3d](https://github.com/MariaDB/server/commit/d524cb5b3d)\
  2024-06-04 14:07:12 +1000
  * [MDEV-34002](https://jira.mariadb.org/browse/MDEV-34002) Initialise fields in spider\_db\_handler
* [Revision #40dd5b8676](https://github.com/MariaDB/server/commit/40dd5b8676)\
  2024-06-10 20:38:49 +0200
  * fix the test for --view
* [Revision #90d376e017](https://github.com/MariaDB/server/commit/90d376e017)\
  2024-05-13 10:36:11 -0400
  * [MDEV-34129](https://jira.mariadb.org/browse/MDEV-34129) mariadb-install-db appears to hang on macOS
* [Revision #3b80d23d02](https://github.com/MariaDB/server/commit/3b80d23d02)\
  2024-06-02 13:17:51 +0400
  * mtr --skip-not-found did not skip suites
* [Revision #a2bd936c52](https://github.com/MariaDB/server/commit/a2bd936c52)\
  2024-06-10 12:35:33 +0300
  * [MDEV-33161](https://jira.mariadb.org/browse/MDEV-33161) Function pointer signature mismatch in LF\_HASH
* [Revision #246c0b3a35](https://github.com/MariaDB/server/commit/246c0b3a35)\
  2024-06-10 12:17:01 +0400
  * [MDEV-34227](https://jira.mariadb.org/browse/MDEV-34227) On startup: UBSAN: runtime error: applying non-zero offset in JOIN::make\_aggr\_tables\_info in sql/sql\_select.cc
* [Revision #21f56583bf](https://github.com/MariaDB/server/commit/21f56583bf)\
  2024-06-10 09:31:14 +0400
  * [MDEV-32376](https://jira.mariadb.org/browse/MDEV-32376) SHOW CREATE DATABASE statement crashes the server when db name contains some unicode characters, ASAN stack-buffer-overflow
* [Revision #bf0aa99aeb](https://github.com/MariaDB/server/commit/bf0aa99aeb)\
  2024-06-06 11:46:27 -0600
  * [MDEV-34237](https://jira.mariadb.org/browse/MDEV-34237): On Startup: UBSAN: runtime error: call to function MDL\_lock::lf\_hash\_initializer lf\_hash\_insert through pointer to incorrect function type 'void (\*)(st\_lf\_hash \*, void \*, const void \*)'
* [Revision #0d85c905c4](https://github.com/MariaDB/server/commit/0d85c905c4)\
  2024-06-07 14:53:11 +0200
  * [MDEV-34269](https://jira.mariadb.org/browse/MDEV-34269): post-fix code simplification
* [Revision #0172887980](https://github.com/MariaDB/server/commit/0172887980)\
  2024-06-06 10:35:56 +0300
  * [MDEV-34269](https://jira.mariadb.org/browse/MDEV-34269) : 10.11.8 cluster becomes inconsistent when using composite primary key and partitioning
* [Revision #e255837eaf](https://github.com/MariaDB/server/commit/e255837eaf)\
  2024-05-30 09:16:42 +0300
  * [MDEV-34266](https://jira.mariadb.org/browse/MDEV-34266) safe\_strcpy() includes an unnecessary conditional branch
* [Revision #4b4dbb23ea](https://github.com/MariaDB/server/commit/4b4dbb23ea)\
  2024-06-07 20:24:39 +0530
  * [MDEV-34169](https://jira.mariadb.org/browse/MDEV-34169) Don't allow innodb\_open\_files to be lesser than number of non-user tablespace.
* [Revision #77c4c0f256](https://github.com/MariaDB/server/commit/77c4c0f256)\
  2024-06-07 12:13:21 +0200
  * [MDEV-34203](https://jira.mariadb.org/browse/MDEV-34203) Sandbox mode - is not compatible with --binary-mode
* [Revision #d9d0e8fd60](https://github.com/MariaDB/server/commit/d9d0e8fd60)\
  2024-06-07 13:51:46 +0300
  * [MDEV-34321](https://jira.mariadb.org/browse/MDEV-34321): call to crc32c\_3way through pointer to incorrect function type
* [Revision #b7a75fbb8a](https://github.com/MariaDB/server/commit/b7a75fbb8a)\
  2024-06-07 13:11:17 +0530
  * [MDEV-34169](https://jira.mariadb.org/browse/MDEV-34169) Don't allow innodb\_open\_files to be lesser than number of non-user tablespace.
* [Revision #238798d978](https://github.com/MariaDB/server/commit/238798d978)\
  2024-06-06 20:24:06 +0200
  * [MDEV-32158](https://jira.mariadb.org/browse/MDEV-32158): wsrep\_sst\_mariadb-backup use /tmp dir during SST rather then user defined tmpdir
* [Revision #654f6ecec4](https://github.com/MariaDB/server/commit/654f6ecec4)\
  2024-06-06 19:37:31 +0200
  * galera: wsrep-lib submodule update
* [Revision #c2d9762011](https://github.com/MariaDB/server/commit/c2d9762011)\
  2024-06-06 19:26:50 +0200
  * mtr: сhange the default setting for the port group size parameter
* [Revision #c1dc03974b](https://github.com/MariaDB/server/commit/c1dc03974b)\
  2024-03-28 11:24:27 +0100
  * [MDEV-33523](https://jira.mariadb.org/browse/MDEV-33523) Spurious deadlock error when wsrep\_on=OFF
* [Revision #d328705a12](https://github.com/MariaDB/server/commit/d328705a12)\
  2024-05-21 15:34:13 +0300
  * [MDEV-34170](https://jira.mariadb.org/browse/MDEV-34170) : table gtid\_slave\_pos entries never been deleted with wsrep\_gtid\_mode = 0
* [Revision #a02773f7c0](https://github.com/MariaDB/server/commit/a02773f7c0)\
  2024-06-06 19:09:13 +0530
  * [MDEV-34057](https://jira.mariadb.org/browse/MDEV-34057) Inconsistent FTS state in concurrent scenarios
* [Revision #0406b2a4ed](https://github.com/MariaDB/server/commit/0406b2a4ed)\
  2024-05-15 17:06:20 +0530
  * [MDEV-34143](https://jira.mariadb.org/browse/MDEV-34143): Server crashes when executing JSON\_EXTRACT after setting non-default collation\_connection
* [Revision #ce9efb4e02](https://github.com/MariaDB/server/commit/ce9efb4e02)\
  2024-06-05 16:34:50 +0200
  * [MDEV-34296](https://jira.mariadb.org/browse/MDEV-34296) tpool - declare thread\_local\_waiter "static thread\_local"
* [Revision #7d86751de5](https://github.com/MariaDB/server/commit/7d86751de5)\
  2024-06-01 00:04:45 +0200
  * mtr: run check-testcase client process under debugger
* [Revision #db9c2d225e](https://github.com/MariaDB/server/commit/db9c2d225e)\
  2024-06-05 13:14:20 +0200
  * fix typo
* [Revision #bfd3f45e8e](https://github.com/MariaDB/server/commit/bfd3f45e8e)\
  2024-06-05 12:26:46 +0200
  * Appveyor - better filtering for branches to match buildbot
* [Revision #b242b44f0a](https://github.com/MariaDB/server/commit/b242b44f0a)\
  2024-06-05 12:13:33 +0200
  * Appveyor build - skip irrelevant commits
* [Revision #40abd973ab](https://github.com/MariaDB/server/commit/40abd973ab)\
  2024-06-05 11:54:34 +0200
  * [MDEV-34236](https://jira.mariadb.org/browse/MDEV-34236) Mroonga build with ASAN/UBSAN with GCC 12+ extremely slow.
* [Revision #38cbef8b3f](https://github.com/MariaDB/server/commit/38cbef8b3f)\
  2024-06-05 10:22:27 +0300
  * [MDEV-22935](https://jira.mariadb.org/browse/MDEV-22935) Erroneous Aria Index / Optimizer behaviour
* [Revision #c6d36c3e7c](https://github.com/MariaDB/server/commit/c6d36c3e7c)\
  2024-06-05 09:25:20 +0300
  * [MDEV-34297](https://jira.mariadb.org/browse/MDEV-34297) get\_rnd\_value() of ib\_counter\_t is unnecessarily complex
* [Revision #ecf4a26107](https://github.com/MariaDB/server/commit/ecf4a26107)\
  2024-05-29 13:59:46 +1000
  * Fix Indonesian month name.
* [Revision #4d38267fc7](https://github.com/MariaDB/server/commit/4d38267fc7)\
  2024-06-01 01:11:40 -0700
  * [MDEV-29307](https://jira.mariadb.org/browse/MDEV-29307) Wrong result when joining two derived tables over the same view
* [Revision #042a0d85ad](https://github.com/MariaDB/server/commit/042a0d85ad)\
  2024-05-09 10:28:55 +1000
  * [MDEV-27186](https://jira.mariadb.org/browse/MDEV-27186) spider/partition: Report error on info() failure
* [Revision #e9f4b87e53](https://github.com/MariaDB/server/commit/e9f4b87e53)\
  2024-04-16 10:44:00 +0300
  * [MDEV-33919](https://jira.mariadb.org/browse/MDEV-33919): Remove less standard format directive an-trap
* [Revision #5e12d49205](https://github.com/MariaDB/server/commit/5e12d49205)\
  2024-06-04 15:06:37 +0400
  * [MDEV-34295](https://jira.mariadb.org/browse/MDEV-34295) CAST(char\_col AS DOUBLE) prints redundant spaces in a warning
* [Revision #581712b989](https://github.com/MariaDB/server/commit/581712b989)\
  2024-05-10 10:01:15 +1000
  * [MDEV-33490](https://jira.mariadb.org/browse/MDEV-33490) MENT-1504 Fix some english strings in spider.
* [Revision #c21aa486a8](https://github.com/MariaDB/server/commit/c21aa486a8)\
  2024-05-14 04:52:53 +0200
  * [MDEV-32633](https://jira.mariadb.org/browse/MDEV-32633): additional post-merge changes for 10.5+
* [Revision #a4838721a2](https://github.com/MariaDB/server/commit/a4838721a2)\
  2024-03-27 13:39:59 +0300
  * [MDEV-32633](https://jira.mariadb.org/browse/MDEV-32633): Fix Galera cluster <-> native replication interaction
* [Revision #0cc9b49751](https://github.com/MariaDB/server/commit/0cc9b49751)\
  2024-03-25 14:40:55 +0100
  * [MDEV-32633](https://jira.mariadb.org/browse/MDEV-32633): Fix Galera cluster <-> native replication interaction
* [Revision #a6b7203d65](https://github.com/MariaDB/server/commit/a6b7203d65)\
  2024-05-07 16:42:13 +0300
  * [MDEV-33952](https://jira.mariadb.org/browse/MDEV-33952): Fix flaky galera\_create\_table\_as\_select test with debug sync
* [Revision #25476ba1ae](https://github.com/MariaDB/server/commit/25476ba1ae)\
  2024-05-09 11:08:14 +1000
  * [MDEV-29027](https://jira.mariadb.org/browse/MDEV-29027) ASAN errors in spider\_db\_free\_result after partition DDL
* [Revision #6d0c9872d9](https://github.com/MariaDB/server/commit/6d0c9872d9)\
  2022-05-27 08:55:42 +0900
  * [MDEV-28522](https://jira.mariadb.org/browse/MDEV-28522) Delete constant SPIDER\_SQL\_TYPE\_\*\_HS
* [Revision #6c30220780](https://github.com/MariaDB/server/commit/6c30220780)\
  2024-04-30 14:51:37 +1000
  * [MDEV-26858](https://jira.mariadb.org/browse/MDEV-26858) Spider: Remove dead code related to HandlerSocket
* [Revision #0c440abd5e](https://github.com/MariaDB/server/commit/0c440abd5e)\
  2024-05-30 14:23:45 +0300
  * [MDEV-31340](https://jira.mariadb.org/browse/MDEV-31340) fixup: Add end-of-test marker
* [Revision #c71275b69e](https://github.com/MariaDB/server/commit/c71275b69e)\
  2024-05-30 14:22:00 +0300
  * Fix ./mtr --repeat=2 main.func\_str
* [Revision #b0b463a894](https://github.com/MariaDB/server/commit/b0b463a894)\
  2024-05-29 12:36:58 -0400
  * [MDEV-33616](https://jira.mariadb.org/browse/MDEV-33616) Fix memleak in pfs\_noop
* [Revision #1929a698a3](https://github.com/MariaDB/server/commit/1929a698a3)\
  2024-05-29 10:27:58 +0100
  * Update README for branch choice
* [Revision #83a04be84a](https://github.com/MariaDB/server/commit/83a04be84a)\
  2024-05-23 21:35:18 +0000
  * Fix Various Typos
* [Revision #4a158ec167](https://github.com/MariaDB/server/commit/4a158ec167)\
  2024-05-27 12:46:51 +0400
  * [MDEV-34226](https://jira.mariadb.org/browse/MDEV-34226) On startup: UBSAN: applying zero offset to null pointer in my\_copy\_fix\_mb from strings/ctype-mb.c and other locations
* [Revision #7925326183](https://github.com/MariaDB/server/commit/7925326183)\
  2024-05-23 16:42:15 +0400
  * [MDEV-30931](https://jira.mariadb.org/browse/MDEV-30931) UBSAN: negation of -X cannot be represented in type 'long long int'; cast to an unsigned type to negate this value to itself in get\_interval\_value on SELECT
* [Revision #44b23bb184](https://github.com/MariaDB/server/commit/44b23bb184)\
  2024-05-24 13:17:27 +0530
  * [MDEV-34222](https://jira.mariadb.org/browse/MDEV-34222) Alter operation on redundant table aborts the server
* [Revision #0ffa340a49](https://github.com/MariaDB/server/commit/0ffa340a49)\
  2024-05-24 10:51:32 +0530
  * [MDEV-34221](https://jira.mariadb.org/browse/MDEV-34221) Errors about checksum mismatch on crash recovery are confusing
* [Revision #736449d30f](https://github.com/MariaDB/server/commit/736449d30f)\
  2024-05-21 16:03:13 +0200
  * [MDEV-34205](https://jira.mariadb.org/browse/MDEV-34205): ASAN stack buffer overflow in strxnmov() in frm\_file\_exists
* [Revision #7c4c082349](https://github.com/MariaDB/server/commit/7c4c082349)\
  2024-05-23 14:18:34 +0400
  * [MDEV-28387](https://jira.mariadb.org/browse/MDEV-28387) UBSAN: runtime error: negation of -9223372036854775808 cannot be represented in type 'long long int'; cast to an unsigned type to negate this value to itself in my\_strtoll10 on SELECT
* [Revision #c4020b541c](https://github.com/MariaDB/server/commit/c4020b541c)\
  2024-05-20 09:44:47 +1000
  * [MDEV-24610](https://jira.mariadb.org/browse/MDEV-24610) MEMORY SE: check overflow in info calls with HA\_STATUS\_AUTO
* [Revision #266495b93e](https://github.com/MariaDB/server/commit/266495b93e)\
  2024-05-21 16:45:07 +0300
  * [MDEV-33817](https://jira.mariadb.org/browse/MDEV-33817) fixup: Disable for macOS
* [Revision #310fd6ff69](https://github.com/MariaDB/server/commit/310fd6ff69)\
  2024-05-21 08:53:40 +0400
  * Backporting bugs fixes fixed by [MDEV-31340](https://jira.mariadb.org/browse/MDEV-31340) from 11.5
* [Revision #b2944adb76](https://github.com/MariaDB/server/commit/b2944adb76)\
  2024-05-15 17:30:52 +0530
  * [MDEV-34166](https://jira.mariadb.org/browse/MDEV-34166) Server could hang with BP < 80M under stress
* [Revision #0907df3d89](https://github.com/MariaDB/server/commit/0907df3d89)\
  2024-05-21 09:52:35 +0300
  * [MDEV-34204](https://jira.mariadb.org/browse/MDEV-34204) Assertion \`!\*detailed\_error' failed on shutdown after XA PREPARE
* [Revision #698dae54ef](https://github.com/MariaDB/server/commit/698dae54ef)\
  2024-05-01 14:25:39 +1000
  * [MDEV-31475](https://jira.mariadb.org/browse/MDEV-31475) Spider: only reset wide\_handler when owning it
* [Revision #86adee3806](https://github.com/MariaDB/server/commit/86adee3806)\
  2024-05-01 14:22:46 +1000
  * [MDEV-31475](https://jira.mariadb.org/browse/MDEV-31475) remove unnecessary assignment to spider share init\_error
* [Revision #ac2e02e961](https://github.com/MariaDB/server/commit/ac2e02e961)\
  2024-05-20 18:18:41 +0530
  * [MDEV-34175](https://jira.mariadb.org/browse/MDEV-34175) mtr\_t::log\_close() warning should change the shutdown condition
* [Revision #28073a979f](https://github.com/MariaDB/server/commit/28073a979f)\
  2024-05-20 13:29:59 +0400
  * [MDEV-34187](https://jira.mariadb.org/browse/MDEV-34187) On startup: UBSAN: runtime error: applying zero offset to null pointer in skip\_trailing\_space and my\_hash\_sort\_utf8mb3\_general1400\_nopad\_as\_ci
* [Revision #dc38d8ea80](https://github.com/MariaDB/server/commit/dc38d8ea80)\
  2023-07-25 20:13:33 +0000
  * Minimize unsafe C functions with safe\_strcpy()
* [Revision #4911ec1a5b](https://github.com/MariaDB/server/commit/4911ec1a5b)\
  2024-05-15 09:50:11 -0400
  * mtr on FreeBSD detects core count for --parallel=auto
* [Revision #32ee6670a5](https://github.com/MariaDB/server/commit/32ee6670a5)\
  2024-05-15 10:52:16 -0400
  * bump the VERSION
* [Revision #7e65512ecc](https://github.com/MariaDB/server/commit/7e65512ecc)\
  2024-05-14 13:31:53 +0200
  * cleanup: compile with -fno-operator-names in maintainer mode
* [Revision #fd76746234](https://github.com/MariaDB/server/commit/fd76746234)\
  2024-05-07 13:49:17 +1000
  * [MDEV-28105](https://jira.mariadb.org/browse/MDEV-28105) Return error in ha\_spider::write\_row() if info(HA\_STATUS\_AUTO) fails
* [Revision #a6ae1c2dfb](https://github.com/MariaDB/server/commit/a6ae1c2dfb)\
  2024-05-13 09:15:14 +1000
  * [MDEV-32487](https://jira.mariadb.org/browse/MDEV-32487) Check plugin is ready when resolving storage engine
* [Revision #1e5b0ff977](https://github.com/MariaDB/server/commit/1e5b0ff977)\
  2024-05-12 10:13:15 +0200
  * mtr: don't store galera sst logs in /tmp/
* [Revision #9ea1f67214](https://github.com/MariaDB/server/commit/9ea1f67214)\
  2024-05-12 08:04:06 +0300
  * [MDEV-33817](https://jira.mariadb.org/browse/MDEV-33817): Proper intrinsics for vextracti32x4
* [Revision #d7d8c2c287](https://github.com/MariaDB/server/commit/d7d8c2c287)\
  2024-05-10 11:17:46 +1000
  * [MDEV-31566](https://jira.mariadb.org/browse/MDEV-31566): Fix buffer overrun of column\_json function (postfix)
* [Revision #867747204a](https://github.com/MariaDB/server/commit/867747204a)\
  2024-05-07 13:52:15 +0800
  * [MDEV-31566](https://jira.mariadb.org/browse/MDEV-31566) Fix buffer overrun of column\_json function
* [Revision #034ababa50](https://github.com/MariaDB/server/commit/034ababa50)\
  2024-05-03 11:41:58 +1000
  * [MDEV-34053](https://jira.mariadb.org/browse/MDEV-34053) mariadbbackup privilege REPLICA MONITOR issue

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
