# MariaDB 10.0.24 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.24)[Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10024-release-notes)[Changelog](mariadb-10024-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 19 Feb 2016

For the highlights of this release, see the [release notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #a4b2714](https://github.com/MariaDB/server/commit/a4b2714)\
  2016-02-17 21:42:57 +0100
  * Merge branch 'bb-10.0-serg' into 10.0
* [Revision #3eb8b11](https://github.com/MariaDB/server/commit/3eb8b11)\
  2016-02-17 21:42:48 +0100
  * fix InnoDB on Windows
* [Revision #289fe37](https://github.com/MariaDB/server/commit/289fe37)\
  2016-02-15 18:05:05 +0100
  * [MDEV-9350](https://jira.mariadb.org/browse/MDEV-9350) Fix jemalloc detection for FreeBSD
* [Revision #74d86d1](https://github.com/MariaDB/server/commit/74d86d1)\
  2016-02-17 14:12:05 +0100
  * MYSQL\_ADD\_PLUGIN: fix DISABLED keyword to work
* [Revision #98be6ef](https://github.com/MariaDB/server/commit/98be6ef)\
  2016-02-17 13:50:03 +0100
  * mtr: read both suitedir/disabled.def and suitedir/t/disabled.def
* [Revision #dc92263](https://github.com/MariaDB/server/commit/dc92263)\
  2016-02-17 13:48:13 +0100
  * [MDEV-9308](https://jira.mariadb.org/browse/MDEV-9308) Fix build errors with recent gcc (isfinite)
* [Revision #09b5865](https://github.com/MariaDB/server/commit/09b5865)\
  2016-02-17 08:05:00 +0400
  * [MDEV-9511](https://jira.mariadb.org/browse/MDEV-9511) Valgrind warnings 'Invalid read' in Field\_newdate::cmp and Field\_newdate::val\_str
* [Revision #77b5484](https://github.com/MariaDB/server/commit/77b5484)\
  2016-02-16 19:35:58 +0100
  * Merge branch 'connect/10.0' into 10.0
* [Revision #b6bcd0f](https://github.com/MariaDB/server/commit/b6bcd0f)\
  2016-02-16 19:15:55 +0100
  * Merge branch 'merge-perfschema-5.6' into 10.0
* [Revision #7e22a1d](https://github.com/MariaDB/server/commit/7e22a1d)\
  2016-02-16 18:56:39 +0100
  * 5.6.29
* [Revision #17a792a](https://github.com/MariaDB/server/commit/17a792a)\
  2016-02-16 18:55:00 +0100
  * Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #c8fcaf8](https://github.com/MariaDB/server/commit/c8fcaf8)\
  2016-02-16 18:32:59 +0100
  * Merge branch 'merge-innodb-5.6' into 10.0
* [Revision #e8085d1](https://github.com/MariaDB/server/commit/e8085d1)\
  2016-02-16 12:49:59 +0400
  * [MDEV-9346](https://jira.mariadb.org/browse/MDEV-9346) - The federatedx and spider engine make mysqld crash when they are configured withtout username
* [Revision #9b73e88](https://github.com/MariaDB/server/commit/9b73e88)\
  2015-12-30 22:26:25 +0800
  * fix-[MDEV-9346](https://jira.mariadb.org/browse/MDEV-9346)
* [Revision #d520d35](https://github.com/MariaDB/server/commit/d520d35)\
  2016-02-16 12:53:24 +0100
  * Revert "[MDEV-8696](https://jira.mariadb.org/browse/MDEV-8696): Adding indexes on empty table is slow with large innodb\_sort\_buffer\_size."
* [Revision #31d2c02](https://github.com/MariaDB/server/commit/31d2c02)\
  2016-02-16 12:13:19 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #220e70f](https://github.com/MariaDB/server/commit/220e70f)\
  2016-02-16 12:07:18 +0100
  * 5.6.29
* [Revision #d76eba6](https://github.com/MariaDB/server/commit/d76eba6)\
  2016-02-16 12:06:16 +0100
  * 5.6.28-76.1
* [Revision #ab9b665](https://github.com/MariaDB/server/commit/ab9b665)\
  2016-02-16 10:49:13 +0200
  * [MDEV-9355](https://jira.mariadb.org/browse/MDEV-9355): parts.partition\_debug\_innodb fails in buildbot on p8-rhel6-bintar-debug
* [Revision #481e643](https://github.com/MariaDB/server/commit/481e643)\
  2016-02-15 23:41:59 +0100\
  \*
  * Fix to [MDEV-9542](https://jira.mariadb.org/browse/MDEV-9542) Connect was not handling NULLs in the answer from catalog functions and tables. It does now and when decimal is NULL defines DOUBLE without parameters.
* [Revision #271fed4](https://github.com/MariaDB/server/commit/271fed4)\
  2016-02-15 22:50:59 +0100
  * Merge branch '5.5' into 10.0
* [Revision #ff26d93](https://github.com/MariaDB/server/commit/ff26d93)\
  2016-02-15 18:23:52 +0100
  * bump the version
* [Revision #a70b896](https://github.com/MariaDB/server/commit/a70b896)\
  2016-02-15 18:38:15 +0200
  * [MDEV-9424](https://jira.mariadb.org/browse/MDEV-9424): Server crashes when slave works with partitioned tables copied from Windows to Linux
* [Revision #c0b6c27](https://github.com/MariaDB/server/commit/c0b6c27)\
  2016-02-15 14:43:42 +0200
  * [MDEV-9548](https://jira.mariadb.org/browse/MDEV-9548): Alter table (renaming and adding index) fails with "Incorrect key file for table" [MDEV-9469](https://jira.mariadb.org/browse/MDEV-9469): 'Incorrect key file' on ALTER TABLE
* [Revision #e1385f2](https://github.com/MariaDB/server/commit/e1385f2)\
  2016-02-15 12:59:47 +0100
  * fix buffer overrun
* [Revision #daa4a2c](https://github.com/MariaDB/server/commit/daa4a2c)\
  2016-02-12 18:12:16 +0100
  * [MDEV-9351](https://jira.mariadb.org/browse/MDEV-9351) Fix CPU detection for TokuDB on FreeBSD
* [Revision #5a0f2f5](https://github.com/MariaDB/server/commit/5a0f2f5)\
  2016-02-12 17:46:34 +0100
  * [MDEV-9149](https://jira.mariadb.org/browse/MDEV-9149) Ctrl-C in MySQL client does not interrupt query, but interrupts the session instead
* [Revision #9630eda](https://github.com/MariaDB/server/commit/9630eda)\
  2016-02-11 20:42:16 +0100
  * [MDEV-9390](https://jira.mariadb.org/browse/MDEV-9390) Function found\_rows() gives incorrect result where the previous SELECT contains ORDER BY clause
* [Revision #38b89a6](https://github.com/MariaDB/server/commit/38b89a6)\
  2016-02-11 12:25:23 +0100
  * [MDEV-9103](https://jira.mariadb.org/browse/MDEV-9103) Altering table comment does a full copy
* [Revision #3c6b771](https://github.com/MariaDB/server/commit/3c6b771)\
  2016-02-10 21:15:24 +0100
  * [MDEV-9045](https://jira.mariadb.org/browse/MDEV-9045) Inconsistent handling of "ALGORITHM=INPLACE" with PERSISTENT generated columns
* [Revision #48ea84f](https://github.com/MariaDB/server/commit/48ea84f)\
  2016-02-10 17:00:31 +0100
  * [MDEV-8427](https://jira.mariadb.org/browse/MDEV-8427) main.connect fails on ppc64el in 10.0 as of 1a8cf15d
* [Revision #9b9522a](https://github.com/MariaDB/server/commit/9b9522a)\
  2016-02-10 15:38:25 +0100
  * [MDEV-8133](https://jira.mariadb.org/browse/MDEV-8133) ALTER TABLE can perform the operation but escape the binary log
* [Revision #1fc6e29](https://github.com/MariaDB/server/commit/1fc6e29)\
  2016-01-13 21:06:29 +0100
  * XtraDB/InnoDB crash with autoinc, vcol and online alter
* [Revision #3889b19](https://github.com/MariaDB/server/commit/3889b19)\
  2016-02-14 22:19:27 +0100
  * more strict ipv6\_ok check in mtr
* [Revision #8f5030e](https://github.com/MariaDB/server/commit/8f5030e)\
  2016-02-14 22:17:38 +0100
  * fix my\_gethwaddr() for solaris
* [Revision #95740bc](https://github.com/MariaDB/server/commit/95740bc)\
  2016-02-14 22:16:50 +0100
  * dtrace in cmake
* [Revision #a5d9597](https://github.com/MariaDB/server/commit/a5d9597)\
  2016-02-14 22:15:16 +0100
  * better inline check
* [Revision #5f078cc](https://github.com/MariaDB/server/commit/5f078cc)\
  2016-02-14 20:57:48 +0100
  * compilation errors on sparc sun studio 10
* [Revision #2a47817](https://github.com/MariaDB/server/commit/2a47817)\
  2016-02-14 18:33:20 +0200
  * [MDEV-9225](https://jira.mariadb.org/browse/MDEV-9225) mysql\_upgrade segfault due to missing /etc/my.cnf.d
* [Revision #b7dc830](https://github.com/MariaDB/server/commit/b7dc830)\
  2016-02-14 18:31:06 +0200
  * Fix memory leak when failing to read config file
* [Revision #93e9d81](https://github.com/MariaDB/server/commit/93e9d81)\
  2016-02-12 12:04:11 +0400
  * Errorneous PSI declaration line fixed.
* [Revision #2c79f57](https://github.com/MariaDB/server/commit/2c79f57)\
  2016-02-12 03:47:25 +0200
  * [MDEV-9464](https://jira.mariadb.org/browse/MDEV-9464) perfschema.global\_read\_lock fails when executed after perfschema.dml\_setup\_instruments
* [Revision #5094a4a](https://github.com/MariaDB/server/commit/5094a4a)\
  2016-02-11 13:54:06 +0400
  * Adjusted main.contributors test result.
* [Revision #fbf132b](https://github.com/MariaDB/server/commit/fbf132b)\
  2016-02-11 11:24:45 +0400
  * Merge pull request #155 from iangilfillan/10.0
* [Revision #d859fff](https://github.com/MariaDB/server/commit/d859fff)\
  2016-02-11 11:15:14 +0400
  * Merge pull request #145 from ottok/ok-debpkg-10.0
* [Revision #a9a08b1](https://github.com/MariaDB/server/commit/a9a08b1)\
  2016-02-10 10:03:47 +0400
  * [MDEV-9371](https://jira.mariadb.org/browse/MDEV-9371) select insert('a',2,1,'b') doesn't return expected 'a'
* [Revision #3c5c04b](https://github.com/MariaDB/server/commit/3c5c04b)\
  2016-02-10 03:49:11 +0200
  * [MDEV-7122](https://jira.mariadb.org/browse/MDEV-7122): Assertion \`0' failed in subselect\_hash\_sj\_engine::init
* [Revision #6b614c6](https://github.com/MariaDB/server/commit/6b614c6)\
  2016-02-09 13:50:48 +0100
  * [MDEV-7765](https://jira.mariadb.org/browse/MDEV-7765): Crash (Assertion \`!table || (!table->write\_set || bitmap\_is\_set(table->write\_set, field\_index) || bitmap\_is\_set(table->vcol\_set, field\_index))' fails) on using function over not created table
* [Revision #775cccc](https://github.com/MariaDB/server/commit/775cccc)\
  2016-02-08 22:53:40 +0200
  * [MDEV-7122](https://jira.mariadb.org/browse/MDEV-7122): Assertion \`0' failed in subselect\_hash\_sj\_engine::init
* [Revision #01628ce](https://github.com/MariaDB/server/commit/01628ce)\
  2016-02-09 14:08:36 +0100
  * Merge branch 'bb-5.5-serg' into 5.5
* [Revision #afce541](https://github.com/MariaDB/server/commit/afce541)\
  2016-02-09 14:06:45 +0100
  * Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #5d478f5](https://github.com/MariaDB/server/commit/5d478f5)\
  2016-02-08 20:07:38 +0100
  * Bug#19817021
* [Revision #6703e5b](https://github.com/MariaDB/server/commit/6703e5b)\
  2016-02-08 20:07:09 +0100
  * Bug#20691429 ASSERTION \`CHILD\_L' FAILED IN STORAGE/MYISAMMRG/HA\_MYISAMMRG.CC:631
* [Revision #dece4bc](https://github.com/MariaDB/server/commit/dece4bc)\
  2016-02-09 11:28:44 +0100
  * cleanup: make assert more readable
* [Revision #63d3ccd](https://github.com/MariaDB/server/commit/63d3ccd)\
  2016-02-08 20:04:39 +0100
  * Bug#21205695 DROP TABLE MAY CAUSE SLAVES TO BREAK
* [Revision #f3444df](https://github.com/MariaDB/server/commit/f3444df)\
  2016-02-09 11:27:40 +0100
  * Merge branch 'mysql/5.5' into 5.5
* [Revision #ea0c3fc](https://github.com/MariaDB/server/commit/ea0c3fc)\
  2016-02-09 05:17:41 +0400
  * [MDEV-9438](https://jira.mariadb.org/browse/MDEV-9438) backport feedback-http-proxy to 5.5 and 10.0. The http-proxy option to the FEEDBACK plugin backported.
* [Revision #b17a435](https://github.com/MariaDB/server/commit/b17a435)\
  2016-02-09 02:31:47 +0300
  * [MDEV-6859](https://jira.mariadb.org/browse/MDEV-6859): scalar subqueries in a comparison produced unexpected result
* [Revision #3cfd36b](https://github.com/MariaDB/server/commit/3cfd36b)\
  2016-02-09 00:13:25 +0100
  * 5.5.47-37.7
* [Revision #d443d70](https://github.com/MariaDB/server/commit/d443d70)\
  2016-02-09 01:46:53 +0300
  * [MDEV-7823](https://jira.mariadb.org/browse/MDEV-7823): Server crashes in next\_depth\_first\_tab on nested IN clauses with SQ inside
* [Revision #eb752ac](https://github.com/MariaDB/server/commit/eb752ac)\
  2016-02-08 16:31:27 +0200
  * typo "Bangalore1" -> "Bangalore"
* [Revision #c4cb240](https://github.com/MariaDB/server/commit/c4cb240)\
  2016-02-06 22:41:58 +0100
  * [MDEV-9024](https://jira.mariadb.org/browse/MDEV-9024) Build fails with VS2015
* [Revision #1e361f2](https://github.com/MariaDB/server/commit/1e361f2)\
  2016-02-06 13:57:59 +0100
  * [MDEV-4664](https://jira.mariadb.org/browse/MDEV-4664) mysql\_upgrade crashes if root's password contains an apostrophe/single quotation mark
* [Revision #9e4e412](https://github.com/MariaDB/server/commit/9e4e412)\
  2016-02-06 13:56:37 +0100
  * unit test for dynstr\_append\_os\_quoted()
* [Revision #41021c0](https://github.com/MariaDB/server/commit/41021c0)\
  2016-02-03 17:15:22 +0100
  * [MDEV-9462](https://jira.mariadb.org/browse/MDEV-9462): Out of memory using explain on 2 empty tables
* [Revision #be19bba](https://github.com/MariaDB/server/commit/be19bba)\
  2016-02-06 12:58:06 +0200
  * Merge pull request #150 from grooverdan/10.0-my\_rnd\_cpp
* [Revision #ad94790](https://github.com/MariaDB/server/commit/ad94790)\
  2016-02-04 14:47:46 +0100
  * [MDEV-9453](https://jira.mariadb.org/browse/MDEV-9453) mysql\_upgrade.exe error when mysql is migrated to mariadb
* [Revision #0a76ad5](https://github.com/MariaDB/server/commit/0a76ad5)\
  2016-02-04 12:51:57 +0100
  * [MDEV-9175](https://jira.mariadb.org/browse/MDEV-9175) Query parser tansforms MICROSECOND into SECOND\_FRAC, which does not work
* [Revision #a90da6e](https://github.com/MariaDB/server/commit/a90da6e)\
  2016-02-05 14:04:24 +0100
  * [MDEV-9314](https://jira.mariadb.org/browse/MDEV-9314) fatal build error: viosslfactories.c:58:5: error: dereferencing pointer to incomplete type ‘DH {aka struct dh\_st}
* [Revision #db5f743](https://github.com/MariaDB/server/commit/db5f743)\
  2016-02-06 12:37:46 +0200
  * Merge pull request #148 from grooverdan/5.5-rpl\_reporting-cppcheck-va\_end
* [Revision #6ecf6d8](https://github.com/MariaDB/server/commit/6ecf6d8)\
  2016-02-05 17:46:01 +0100
  * [MDEV-7827](https://jira.mariadb.org/browse/MDEV-7827): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed in Field\_long::val\_str on EXPLAIN EXTENDED
* [Revision #9f3b53f](https://github.com/MariaDB/server/commit/9f3b53f)\
  2015-12-14 19:16:29 +0100
  * [MDEV-9093](https://jira.mariadb.org/browse/MDEV-9093) Persistent computed column is not updated when update query contains join
* [Revision #113b56e](https://github.com/MariaDB/server/commit/113b56e)\
  2016-02-04 16:03:14 +0200
  * Merge remote-tracking branch 'upstream/10.0' into 10.0
* [Revision #86b2621](https://github.com/MariaDB/server/commit/86b2621)\
  2016-02-04 16:00:11 +0200
  * [MDEV-6821](https://jira.mariadb.org/browse/MDEV-6821), [MDEV-6826](https://jira.mariadb.org/browse/MDEV-6826) - Update authors and contributors
* [Revision #33ac501](https://github.com/MariaDB/server/commit/33ac501)\
  2016-02-04 13:54:57 +0200
  * Use C++ linkage.
* [Revision #1d00d5c](https://github.com/MariaDB/server/commit/1d00d5c)\
  2016-02-03 16:51:23 +0200
  * Fix function visibility as it is used on row0mysql.c in Windows.
* [Revision #a3d843d](https://github.com/MariaDB/server/commit/a3d843d)\
  2016-02-03 15:52:26 +0200
  * Fix function visibility as it is used on row0mysql.c in Windows.
* [Revision #73d23f8](https://github.com/MariaDB/server/commit/73d23f8)\
  2016-02-03 14:34:06 +0200
  * [MDEV-9471](https://jira.mariadb.org/browse/MDEV-9471): Server crashes or returns an error while trying to alter partitioning on a table moved from Windows to Linux
* [Revision #f66d016](https://github.com/MariaDB/server/commit/f66d016)\
  2016-02-03 11:32:51 +0200
  * [MDEV-9471](https://jira.mariadb.org/browse/MDEV-9471): Server crashes or returns an error while trying to alter partitioning on a table moved from Windows to Linux
* [Revision #603c096](https://github.com/MariaDB/server/commit/603c096)\
  2016-02-03 00:43:00 +0100
  * [MDEV-9466](https://jira.mariadb.org/browse/MDEV-9466) : Exception handler on Windows does not output any text, if mysqld runs as service
* [Revision #5cf293f](https://github.com/MariaDB/server/commit/5cf293f)\
  2016-02-01 19:37:06 +0300
  * Merge branch '10.0' of github.com:MariaDB/server into 10.0
* [Revision #74f15e2](https://github.com/MariaDB/server/commit/74f15e2)\
  2016-02-01 19:36:22 +0300
  * [MDEV-9505](https://jira.mariadb.org/browse/MDEV-9505): Valgrind failure in SEL\_ARG::store\_min,find\_used\_partitions
* [Revision #955126e](https://github.com/MariaDB/server/commit/955126e)\
  2016-02-01 16:29:00 +0100
  * Merge [MDEV-9112](https://jira.mariadb.org/browse/MDEV-9112) into 10.0
* [Revision #0e84d54](https://github.com/MariaDB/server/commit/0e84d54)\
  2016-02-01 16:27:12 +0100
  * Merge [MDEV-9112](https://jira.mariadb.org/browse/MDEV-9112) into 5.5
* [Revision #8cf1f50](https://github.com/MariaDB/server/commit/8cf1f50)\
  2016-02-01 16:10:49 +0100
  * [MDEV-9112](https://jira.mariadb.org/browse/MDEV-9112): Non-blocking client API missing on non-x86 platforms
* [Revision #d0c5efc](https://github.com/MariaDB/server/commit/d0c5efc)\
  2016-01-29 23:53:44 +0200
  * If one compiled with too long MYSQL\_SERVER\_SUFFIX this caused a memory overrun that caused some test to fail.
* [Revision #a1ddf01](https://github.com/MariaDB/server/commit/a1ddf01)\
  2016-01-29 23:52:15 +0200
  * my\_decimal didn't compile properly with debug
* [Revision #a4ff37e](https://github.com/MariaDB/server/commit/a4ff37e)\
  2016-01-26 22:33:25 +0400
  * [MDEV-6421](https://jira.mariadb.org/browse/MDEV-6421) SQL\_ERROR\_LOG doesn't log comments in Events. Change parser so it saves all the query line to the ';' in the sp\_instr::m\_query.
* [Revision #0bfb5be](https://github.com/MariaDB/server/commit/0bfb5be)\
  2016-01-25 20:01:22 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #666b966](https://github.com/MariaDB/server/commit/666b966)\
  2016-01-25 19:03:33 +0100
  * update test results
* [Revision #62a5e56](https://github.com/MariaDB/server/commit/62a5e56)\
  2016-01-25 18:44:51 +0100\
  \*
  * Change SQL\_NTS to 0 when the string is NULL
* [Revision #1fa15f9](https://github.com/MariaDB/server/commit/1fa15f9)\
  2016-01-25 17:54:28 +0200
  * Updated README and CREDITS
* [Revision #1793646](https://github.com/MariaDB/server/commit/1793646)\
  2016-01-25 16:37:08 +0400
  * Merge branch '5.5' into 10.0
* [Revision #a7a4988](https://github.com/MariaDB/server/commit/a7a4988)\
  2016-01-19 16:53:13 +1100
  * mysys/my\_rnd.c - remove `#ifdef cplusplus`
* [Revision #3e5724f](https://github.com/MariaDB/server/commit/3e5724f)\
  2016-01-19 14:47:41 +1100
  * Add va\_end to make cppcheck happy
* [Revision #74b1af1](https://github.com/MariaDB/server/commit/74b1af1)\
  2016-01-15 12:50:23 +0100
  * Merge branch 'tmp' into tmp-10.0
* [Revision #06b2e32](https://github.com/MariaDB/server/commit/06b2e32)\
  2016-01-15 12:42:51 +0100
  * Fix error handling for GTID and domain-based parallel replication
* [Revision #9c9d10b](https://github.com/MariaDB/server/commit/9c9d10b)\
  2016-01-15 09:50:27 +0400
  * [MDEV-9106](https://jira.mariadb.org/browse/MDEV-9106) Audit plugin not working with MySQL 5.7. fixing Windows crash.
* [Revision #fe4823d](https://github.com/MariaDB/server/commit/fe4823d)\
  2016-01-13 18:02:44 +0400
  * [MDEV-9106](https://jira.mariadb.org/browse/MDEV-9106) Audit plugin doesnt run with MySQL 5.7. updata thread\_pool\_server\_audit test result.
* [Revision #cdc9aa5](https://github.com/MariaDB/server/commit/cdc9aa5)\
  2016-01-13 15:24:33 +0400
  * [MDEV-9106](https://jira.mariadb.org/browse/MDEV-9106) Audit Plugin doesn't run with MySQL 5.7. [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) built in debug gets unhappy with mutexes. Although everything is correct, some DBUG\_ASSERT can happen. So this patch keeps safe\_mutex silent.
* [Revision #c955253](https://github.com/MariaDB/server/commit/c955253)\
  2016-01-12 16:29:02 +0400
  * [MDEV-9106](https://jira.mariadb.org/browse/MDEV-9106) Audit plugin compiled with MariaDB can't install on MySQL 5.7. The audit API was seriously changed in MySQL 5.7. so we had to adapt the plugin's code to that.
* [Revision #2a9f84b](https://github.com/MariaDB/server/commit/2a9f84b)\
  2016-01-11 10:28:00 +0200
  * [MDEV-9354](https://jira.mariadb.org/browse/MDEV-9354): Debian: unmask the mysql.service on installation
* [Revision #7cd94c6](https://github.com/MariaDB/server/commit/7cd94c6)\
  2016-01-10 11:57:36 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #0891ae2](https://github.com/MariaDB/server/commit/0891ae2)\
  2016-01-09 20:52:17 +0100\
  \*
  * Fix [MDEV-9239](https://jira.mariadb.org/browse/MDEV-9239). Meanwhile, make all references to the database in XTAB Schema (was sometimes in XTAB Catalog)
* [Revision #3730d8a](https://github.com/MariaDB/server/commit/3730d8a)\
  2016-01-05 22:48:50 +0100
  * [MDEV-9366](https://jira.mariadb.org/browse/MDEV-9366) : do\_shutdown\_server fails to detect server shutdown on Windows. Fix test whether process is alive in mysqltest.
* [Revision #1236333](https://github.com/MariaDB/server/commit/1236333)\
  2015-12-24 21:46:38 +0100
  * Fix annoying repetitive tokudb build warning, if MariaDB is build on non-Linux x64 system
* [Revision #5f48b61](https://github.com/MariaDB/server/commit/5f48b61)\
  2016-01-07 14:45:40 +0100
  * [MDEV-9298](https://jira.mariadb.org/browse/MDEV-9298) : Build failure when linking libmysql.
* [Revision #8fcc0bf](https://github.com/MariaDB/server/commit/8fcc0bf)\
  2016-01-03 13:27:59 +0200
  * Fixed bug in semi\_sync replication tests.
* [Revision #661a6d8](https://github.com/MariaDB/server/commit/661a6d8)\
  2016-01-03 13:20:07 +0200
  * Cleanup of slave code:
* [Revision #4b4777a](https://github.com/MariaDB/server/commit/4b4777a)\
  2016-01-03 12:48:55 +0200
  * Backported fix for ccache Fixed compiler warnings Added --big-test to tokudb change\_column\_char & change\_column\_bin
* [Revision #ae7b39a](https://github.com/MariaDB/server/commit/ae7b39a)\
  2015-12-30 20:55:12 +0100
  * Merge branch '5.5' into 10.0
* [Revision #ff24820](https://github.com/MariaDB/server/commit/ff24820)\
  2015-12-30 19:39:31 +0100
  * Fix process handle leak in buildbot. GenerateConsoleCtrlEvent sent to non-existing process will add a process handle to this non-existing process to console host process conhost.exe
* [Revision #4d3bc26](https://github.com/MariaDB/server/commit/4d3bc26)\
  2015-12-29 18:41:37 +0400
  * Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #61d3621](https://github.com/MariaDB/server/commit/61d3621)\
  2015-12-29 18:40:41 +0400
  * Moving Field\_blob::store\_length() back from protected to public, as it's needed for Cassandra in 10.0.
* [Revision #7529870](https://github.com/MariaDB/server/commit/7529870)\
  2015-12-29 15:19:29 +0400
  * Merge branch '10.0' of github.com:MariaDB/server into 10.0
* [Revision #6d7362e](https://github.com/MariaDB/server/commit/6d7362e)\
  2015-12-29 15:18:55 +0400
  * Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #f31a891](https://github.com/MariaDB/server/commit/f31a891)\
  2015-11-18 15:51:20 +0400
  * [MDEV-9128](https://jira.mariadb.org/browse/MDEV-9128) - Compiling on IBM System Z fails
* [Revision #93b078c](https://github.com/MariaDB/server/commit/93b078c)\
  2015-12-27 15:40:34 +0400
  * [MDEV-9128](https://jira.mariadb.org/browse/MDEV-9128) - Compiling on IBM System Z fails
* [Revision #e1b9be5](https://github.com/MariaDB/server/commit/e1b9be5)\
  2015-12-29 14:17:31 +0400
  * [MDEV-9319](https://jira.mariadb.org/browse/MDEV-9319) ALTER from a bigger to a smaller blob type truncates too much data
* [Revision #e37372c](https://github.com/MariaDB/server/commit/e37372c)\
  2015-12-27 21:14:07 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #6883e5c](https://github.com/MariaDB/server/commit/6883e5c)\
  2015-12-27 19:45:51 +0100\
  \*
  * Fix [MDEV-9322](https://jira.mariadb.org/browse/MDEV-9322).
* [Revision #4fdf25a](https://github.com/MariaDB/server/commit/4fdf25a)\
  2015-12-21 16:37:59 +0100
  * after-merge: 10.0 part of [MDEV-9249](https://jira.mariadb.org/browse/MDEV-9249) (ERR\_remove\_state)
* [Revision #05dc86c](https://github.com/MariaDB/server/commit/05dc86c)\
  2015-12-21 16:36:10 +0100
  * Merge branch '5.5' into 10.0
* [Revision #e126baa](https://github.com/MariaDB/server/commit/e126baa)\
  2015-12-21 10:19:02 +0100
  * [MDEV-9249](https://jira.mariadb.org/browse/MDEV-9249) MariaDB un-buildable on linux64: fails @ "error: ‘ERR\_remove\_state’ was not declared in this scope" when linking against OpenSSL 1.0.2e
* [Revision #865548f](https://github.com/MariaDB/server/commit/865548f)\
  2015-12-18 09:50:39 +0100
  * [MDEV-9088](https://jira.mariadb.org/browse/MDEV-9088) Server crashes on shutdown after the second post of feedback report
* [Revision #591e74c](https://github.com/MariaDB/server/commit/591e74c)\
  2015-06-20 16:59:22 +0800
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #e386523](https://github.com/MariaDB/server/commit/e386523)\
  2015-12-19 13:53:43 +0200
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #f39b9e0](https://github.com/MariaDB/server/commit/f39b9e0)\
  2015-12-19 13:52:27 +0200
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #6414959](https://github.com/MariaDB/server/commit/6414959)\
  2015-12-19 13:31:44 +0200
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #f89c9fc](https://github.com/MariaDB/server/commit/f89c9fc)\
  2015-12-19 13:25:55 +0200
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #3b9423f](https://github.com/MariaDB/server/commit/3b9423f)\
  2015-03-12 04:49:31 +1100
  * [MDEV-7384](https://jira.mariadb.org/browse/MDEV-7384): Add --persistent option for mysqlcheck
* [Revision #5efb8f1](https://github.com/MariaDB/server/commit/5efb8f1)\
  2015-12-18 22:51:12 +0400
  * Filter out unix-socket from unrelated test cases
* [Revision #3402f7a](https://github.com/MariaDB/server/commit/3402f7a)\
  2015-12-18 16:31:05 +0400
  * Fixed auth\_socket static compilation
* [Revision #3f6159f](https://github.com/MariaDB/server/commit/3f6159f)\
  2015-12-14 23:47:05 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #11c339f](https://github.com/MariaDB/server/commit/11c339f)\
  2015-12-14 23:45:23 +0100\
  \*
  * Fix [MDEV-9279](https://jira.mariadb.org/browse/MDEV-9279). Replacing exit(1) in yy\_fatal\_error by a longjmp.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
