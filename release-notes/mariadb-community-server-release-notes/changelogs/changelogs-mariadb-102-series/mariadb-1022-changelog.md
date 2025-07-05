# MariaDB 10.2.2 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/release-notes-mariadb-10-2-series/mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.2)[Release Notes](../../old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md)[Changelog](mariadb-1022-changelog.md)[Overview of 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md)

**Release date:** 27 Sep 2016

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.2) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #1f1990a](https://github.com/MariaDB/server/commit/1f1990a)\
  2016-09-25 17:28:49 -0700
  * Fixed bug [MDEV-10884](https://jira.mariadb.org/browse/MDEV-10884). If a materialized derived table / view is specified by a unit with SELECTs containing ORDER BY ... LIMIT then condition pushdown cannot be done for these SELECTs. If a materialized derived table / view is specified by a unit containing global ORDER BY ... LIMIT then condition pushdown cannot be done for this unit.
* [Revision #09cbb77](https://github.com/MariaDB/server/commit/09cbb77)\
  2016-09-26 02:39:25 +0300
  * Follow-up for [MDEV-10174](https://jira.mariadb.org/browse/MDEV-10174) - fix the result file for the embedded test
* [Revision #20d7f93](https://github.com/MariaDB/server/commit/20d7f93)\
  2016-09-25 00:21:14 -0700
  * Adjusted test results.
* [Revision #54efb08](https://github.com/MariaDB/server/commit/54efb08)\
  2016-09-24 21:04:54 -0700
  * Fixed bug [MDEV-10881](https://jira.mariadb.org/browse/MDEV-10881) The server missed to call check\_dependencies\_in\_with\_clauses() when processing PREPARE ... FROM CREATE ... SELECT / INSERT ... SELECT with WITH clause before SELECT.
* [Revision #61ab733](https://github.com/MariaDB/server/commit/61ab733)\
  2016-09-24 20:29:56 -0700
  * Fixed bug [MDEV-10883](https://jira.mariadb.org/browse/MDEV-10883). When a prepared statement uses a CTE definition with a column list renaming of columns of the CTE expression must be performed for every execution of the prepared statement.
* [Revision #018ac12](https://github.com/MariaDB/server/commit/018ac12)\
  2016-09-24 20:44:15 +0000
  * use latest Connector/C commit
* [Revision #c1b2828](https://github.com/MariaDB/server/commit/c1b2828)\
  2016-09-24 20:20:33 +0300
  * [MDEV-10174](https://jira.mariadb.org/browse/MDEV-10174): Make the fix for [MDEV-8989](https://jira.mariadb.org/browse/MDEV-8989) enabled by default in 10.2
* [Revision #de2175e](https://github.com/MariaDB/server/commit/de2175e)\
  2016-09-24 15:25:00 +0200
  * Window functions can have an empty over clause
* [Revision #45faae6](https://github.com/MariaDB/server/commit/45faae6)\
  2016-09-24 15:18:37 +0200
  * Typo fix
* [Revision #1c858dd](https://github.com/MariaDB/server/commit/1c858dd)\
  2016-09-23 17:15:01 +0200
  * Make win\_big test specify only if Sort\_merge\_passes have happened
* [Revision #8b95e7e](https://github.com/MariaDB/server/commit/8b95e7e)\
  2016-09-23 14:03:19 +0200
  * Make sure to call Rowid\_seq\_cursor::next to not face infinite recursion
* [Revision #0479639](https://github.com/MariaDB/server/commit/0479639)\
  2016-09-23 14:18:29 +0300
  * [MDEV-9736](https://jira.mariadb.org/browse/MDEV-9736): Window functions: multiple cursors to read filesort result
* [Revision #6e40157](https://github.com/MariaDB/server/commit/6e40157)\
  2016-09-22 22:18:45 +0200
  * Clean up nth\_value
* [Revision #53cf265](https://github.com/MariaDB/server/commit/53cf265)\
  2016-09-22 18:26:55 +0200
  * Implement LEAD and LAG and NTH\_VALUE functions
* [Revision #29b227c](https://github.com/MariaDB/server/commit/29b227c)\
  2016-09-22 18:22:34 +0200
  * Cleanup win testcase to always be deterministic
* [Revision #09a8c79](https://github.com/MariaDB/server/commit/09a8c79)\
  2016-09-22 18:17:45 +0200
  * Fix win\_std nondeterministic results
* [Revision #3dd3a5d](https://github.com/MariaDB/server/commit/3dd3a5d)\
  2016-09-22 14:21:18 +0200
  * [MDEV-9935](https://jira.mariadb.org/browse/MDEV-9935): Window functions: assertion failure with empty OVER () clause
* [Revision #e992464](https://github.com/MariaDB/server/commit/e992464)\
  2016-09-21 21:47:47 +0200
  * Update Frame\_positional\_cursor to also take an optional bound
* [Revision #88a8abb](https://github.com/MariaDB/server/commit/88a8abb)\
  2016-09-21 21:47:00 +0200
  * Add test results for win\_first\_last\_value
* [Revision #872c0b4](https://github.com/MariaDB/server/commit/872c0b4)\
  2016-09-21 16:45:36 +0200
  * Allow first/last value functions to have frame definitions
* [Revision #74fa106](https://github.com/MariaDB/server/commit/74fa106)\
  2016-09-20 22:20:25 +0200
  * Update features result to account for window functions counter
* [Revision #a2bafba](https://github.com/MariaDB/server/commit/a2bafba)\
  2016-09-20 22:12:48 +0200
  * Make first\_value and last\_value computation efficient
* [Revision #15b8a77](https://github.com/MariaDB/server/commit/15b8a77)\
  2016-09-20 22:17:33 +0200
  * Add results for first\_value and last\_value test case
* [Revision #9a5930b](https://github.com/MariaDB/server/commit/9a5930b)\
  2016-09-20 20:44:49 +0200
  * Implement first\_value and last\_value as window functions
* [Revision #e413c6e](https://github.com/MariaDB/server/commit/e413c6e)\
  2016-09-20 12:18:35 +0200
  * Add test case for STD function used as window function
* [Revision #00bf18e](https://github.com/MariaDB/server/commit/00bf18e)\
  2016-09-20 11:11:24 +0200
  * Move table record writing outside of loop
* [Revision #2e7a585](https://github.com/MariaDB/server/commit/2e7a585)\
  2016-09-19 20:49:04 +0200
  * Add test case for new window functions status var
* [Revision #62df311](https://github.com/MariaDB/server/commit/62df311)\
  2016-09-19 20:45:30 +0200
  * Add a counter for the number of select statements using window functions
* [Revision #5cb5687](https://github.com/MariaDB/server/commit/5cb5687)\
  2016-09-17 11:17:48 +0200
  * [MDEV-10669](https://jira.mariadb.org/browse/MDEV-10669): Crash in SELECT with window function used
* [Revision #2857ff3](https://github.com/MariaDB/server/commit/2857ff3)\
  2016-09-16 20:38:22 +0200
  * [MDEV-10815](https://jira.mariadb.org/browse/MDEV-10815): Window Function Expressions Wrong Results
* [Revision #1c72441](https://github.com/MariaDB/server/commit/1c72441)\
  2016-09-13 17:52:38 +0200
  * Frame bounds using FOLLOWING or PRECEDING can have 0 as cardinal value
* [Revision #954e465](https://github.com/MariaDB/server/commit/954e465)\
  2016-09-13 13:16:11 +0200
  * Fix compilation failure of TokuDB on BSD-like systems
* [Revision #a95e384](https://github.com/MariaDB/server/commit/a95e384)\
  2016-09-24 15:27:56 +0300
  * [MDEV-10174](https://jira.mariadb.org/browse/MDEV-10174): Make the fix for [MDEV-8989](https://jira.mariadb.org/browse/MDEV-8989) enabled by default in 10.2
* [Revision #457f3b9](https://github.com/MariaDB/server/commit/457f3b9)\
  2016-09-23 14:42:12 -0700
  * Added the test case for bug [MDEV-9941](https://jira.mariadb.org/browse/MDEV-9941) that was fixed some time ago.
* [Revision #4872ec6](https://github.com/MariaDB/server/commit/4872ec6)\
  2016-09-23 14:22:20 -0700
  * Fixed bug [MDEV-10874](https://jira.mariadb.org/browse/MDEV-10874). In some cases the method Window\_funcs\_sort::setup() did not build the sequence of sorting keys correctly.
* [Revision #78f5879](https://github.com/MariaDB/server/commit/78f5879)\
  2016-09-23 22:34:03 +0200
  * more adequate rpm settings
* [Revision #deafe7a](https://github.com/MariaDB/server/commit/deafe7a)\
  2016-09-23 16:01:28 +0200
  * RPM fixes for CentOS7 and Fedora
* [Revision #0f8a1a3](https://github.com/MariaDB/server/commit/0f8a1a3)\
  2016-09-23 14:19:07 +0400
  * [MDEV-10877](https://jira.mariadb.org/browse/MDEV-10877) xxx\_unicode\_nopad\_ci collations
* [Revision #6304c0b](https://github.com/MariaDB/server/commit/6304c0b)\
  2016-09-19 12:31:20 +0000
  * Windows : completion port based asynchronous IO.
* [Revision #c46304f](https://github.com/MariaDB/server/commit/c46304f)\
  2016-09-22 17:21:21 +0000
  * Fix valgrind error.
* [Revision #630035b](https://github.com/MariaDB/server/commit/630035b)\
  2016-09-22 17:13:05 +0000
  * Fix buildbot errors on Windows
* [Revision #f7a7c0c](https://github.com/MariaDB/server/commit/f7a7c0c)\
  2016-09-21 14:28:42 +0000
  * [MDEV-10297](https://jira.mariadb.org/browse/MDEV-10297) Add priorization to threadpool
* [Revision #f32a511](https://github.com/MariaDB/server/commit/f32a511) 2016-09-22 17:50:37 +0200 - Merge branch '10.2' into bb-10.2-connector-c-integ-subm
* [Revision #2726378](https://github.com/MariaDB/server/commit/2726378) 2016-09-22 07:59:13 -0700 - Merge branch 'bb-10.2-mdev9864' into 10.2
* [Revision #48b4e33](https://github.com/MariaDB/server/commit/48b4e33)\
  2016-09-22 01:45:05 -0700
  * Allowed to use WITH clauses before SELECT in CREATE ... SELECT and INSERT ... SELECT. Added test cases.
* [Revision #c82c375](https://github.com/MariaDB/server/commit/c82c375)\
  2016-09-21 13:28:22 +0200
  * compilation failure on power8
* [Revision #200430e](https://github.com/MariaDB/server/commit/200430e)\
  2016-09-22 07:38:28 +0300
  * [MDEV-10845](https://jira.mariadb.org/browse/MDEV-10845): Server crashes in sync\_array\_cell\_print with innodb-status-file
* [Revision #f7640e1](https://github.com/MariaDB/server/commit/f7640e1)\
  2016-09-22 13:32:00 +0200
  * use the latest C/C commit
* [Revision #d2cfae6](https://github.com/MariaDB/server/commit/d2cfae6)\
  2016-09-22 13:07:38 +0200
  * copy-paste error fixed
* [Revision #b309faf](https://github.com/MariaDB/server/commit/b309faf)\
  2016-09-21 17:38:04 +0200
  * buildbot failures
* [Revision #d876f4b](https://github.com/MariaDB/server/commit/d876f4b)\
  2016-09-21 13:20:24 +0200
  * disable session\_track\_schema for perfschema.socket\_summary\_by\_instance\_func
* [Revision #59d51f0](https://github.com/MariaDB/server/commit/59d51f0) 2016-09-21 12:54:56 +0200 - Merge branch '10.2' into bb-10.2-connector-c-integ-subm
* [Revision #4368efe](https://github.com/MariaDB/server/commit/4368efe)\
  2016-09-19 19:07:17 +0200
  * valgrind failures
* [Revision #e4f7078](https://github.com/MariaDB/server/commit/e4f7078)\
  2016-09-19 19:55:49 +0200
  * fix sporadic innodb.auto\_increment\_dup failures
* [Revision #398d33c](https://github.com/MariaDB/server/commit/398d33c)\
  2016-09-19 19:05:35 +0200
  * fix main.index\_intersect\_innodb failure on trusty-amd64
* [Revision #10aa393](https://github.com/MariaDB/server/commit/10aa393)\
  2016-09-20 19:56:05 -0700
  * Fixed bug [MDEV-10842](https://jira.mariadb.org/browse/MDEV-10842). In some cases the function compare\_order\_elements() erroneously returned CMP\_EQ for not equal elements.
* [Revision #3da077a](https://github.com/MariaDB/server/commit/3da077a) 2016-09-19 09:54:16 -0700 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* [Revision #f9bdc7c](https://github.com/MariaDB/server/commit/f9bdc7c) 2016-09-19 09:47:08 +0200 - Merge branch '10.2' into bb-10.2-jan
* [Revision #f7be8cf](https://github.com/MariaDB/server/commit/f7be8cf)\
  2016-09-16 17:51:48 +0200
  * update test results
* [Revision #4572dca](https://github.com/MariaDB/server/commit/4572dca)\
  2016-09-16 09:53:46 +0200
  * increase I\_S.FILES.FILE\_NANE column length
* [Revision #15b174a](https://github.com/MariaDB/server/commit/15b174a)\
  2016-09-15 15:22:12 +0200
  * debug-only test, use have\_debug.inc
* [Revision #882aea9](https://github.com/MariaDB/server/commit/882aea9)\
  2016-09-15 11:00:28 +0200
  * fix debian: no ha\_innodb.so for you, sorry
* [Revision #f5ef5531](https://github.com/MariaDB/server/commit/f5ef5531)\
  2016-09-15 09:42:52 +0300
  * Fixed mutex deadlock found with innodb.innodb-defrag-concurrent test. We should not take X-lock for index in the begining, setting tablespace as named space is enough.
* [Revision #c8b3244](https://github.com/MariaDB/server/commit/c8b3244)\
  2016-09-14 15:23:59 +0200
  * fix some quoting in error messages
* [Revision #ea3262d](https://github.com/MariaDB/server/commit/ea3262d)\
  2016-09-14 15:10:47 +0200
  * Fix innodb\_fts suite
* [Revision #4133d29](https://github.com/MariaDB/server/commit/4133d29)\
  2016-09-14 15:11:01 +0300
  * Fix crash on innodb\_fts.innobase\_drop\_fts\_index\_table
* [Revision #62ed880](https://github.com/MariaDB/server/commit/62ed880)\
  2016-09-14 13:53:32 +0300
  * Fix test failure on tc\_partition\_list\_directory because innodb-strict-mode by default is now ON, disabling it for this test because test uses INDEX DICECTORY that is not really supported by InnoDB.
* [Revision #a729656](https://github.com/MariaDB/server/commit/a729656)\
  2016-09-14 11:28:40 +0300
  * [MDEV-10548](https://jira.mariadb.org/browse/MDEV-10548): Some of the debug sync waits do not work with InnoDB 5.7 (branch bb-10.2-jan)
* [Revision #da168b3](https://github.com/MariaDB/server/commit/da168b3)\
  2016-09-14 08:27:22 +0300
  * [MDEV-10200](https://jira.mariadb.org/browse/MDEV-10200): IS tables are not found on 10.2 InnoDB 5.7 (branch bb-10.2-jan)
* [Revision #587cb66](https://github.com/MariaDB/server/commit/587cb66)\
  2016-09-13 23:48:03 +0000
  * Windows : Remove one more CloseHandle() used on a (non-handle) thread id
* [Revision #588b033](https://github.com/MariaDB/server/commit/588b033)\
  2016-09-13 21:55:21 +0000
  * Add error logging for aio error on Windows
* [Revision #7c6037c](https://github.com/MariaDB/server/commit/7c6037c)\
  2016-09-13 18:23:14 +0000
  * Windows : CloseHandle() returned by CreateThread(). Don't wait until os\_thread\_exit to close it. Remove code from innodb\_shutdown to close handles on Windows.
* [Revision #bc526a5](https://github.com/MariaDB/server/commit/bc526a5)\
  2016-09-13 17:21:24 +0000
  * avoid warnings about mtr.test\_suppressions not being closed before the crash
* [Revision #6ee37fa](https://github.com/MariaDB/server/commit/6ee37fa)\
  2016-09-13 08:55:10 +0300
  * Fix test failure.
* [Revision #4ce0b3b](https://github.com/MariaDB/server/commit/4ce0b3b)\
  2016-09-11 14:05:29 +0200
  * fix MYSQL\_FTPARSER\_BOOLEAN\_INFO initialization
* [Revision #dc900cc](https://github.com/MariaDB/server/commit/dc900cc)\
  2016-09-11 10:57:05 +0200
  * Remove a bunch of TODO's, fix perfschema.threads\_innodb test
* [Revision #d019af4](https://github.com/MariaDB/server/commit/d019af4)\
  2016-09-10 16:04:44 +0200
  * misc after-merge changes:
* [Revision #d8cbad0](https://github.com/MariaDB/server/commit/d8cbad0)\
  2016-09-09 16:45:05 +0300
  * More test case fixes.
* [Revision #d3708f7](https://github.com/MariaDB/server/commit/d3708f7)\
  2016-09-09 10:01:18 +0300
  * Fix bunch of test failures and solaris build missing include.
* [Revision #11ae60d](https://github.com/MariaDB/server/commit/11ae60d)\
  2016-09-08 18:09:47 +0200
  * [MDEV-10551](https://jira.mariadb.org/browse/MDEV-10551) Test innodb.defrag\_mdl-9155 hangs on InnoDB 5.7
* [Revision #fec844a](https://github.com/MariaDB/server/commit/fec844a)\
  2016-09-06 09:43:16 +0300
  * Merge InnoDB 5.7 from mysql-5.7.14.
* [Revision #2e814d4](https://github.com/MariaDB/server/commit/2e814d4)\
  2016-08-12 11:17:45 +0300
  * Merge InnoDB 5.7 from mysql-5.7.9.
* [Revision #697a9d0](https://github.com/MariaDB/server/commit/697a9d0)\
  2016-09-19 09:53:36 -0700
  * Fixed a failure with --valgrind for cte\_recursive.test.
* [Revision #f566a4f](https://github.com/MariaDB/server/commit/f566a4f)\
  2016-09-12 16:07:10 +0200
  * maria.encrypt-wrong-key - cleanup properly
* [Revision #85358dd](https://github.com/MariaDB/server/commit/85358dd)\
  2016-09-17 11:01:27 +0400
  * [MDEV-10296](https://jira.mariadb.org/browse/MDEV-10296) - Multi-instance table cache
* [Revision #cb575ab](https://github.com/MariaDB/server/commit/cb575ab)\
  2016-09-16 21:46:33 +0400
  * [MDEV-10296](https://jira.mariadb.org/browse/MDEV-10296) - Multi-instance table cache
* [Revision #0d88b97](https://github.com/MariaDB/server/commit/0d88b97)\
  2016-09-16 19:07:59 +0400
  * [MDEV-10296](https://jira.mariadb.org/browse/MDEV-10296) - Multi-instance table cache
* [Revision #a2b1c58](https://github.com/MariaDB/server/commit/a2b1c58)\
  2016-09-16 18:35:56 +0400
  * [MDEV-10296](https://jira.mariadb.org/browse/MDEV-10296) - Multi-instance table cache
* [Revision #8613633](https://github.com/MariaDB/server/commit/8613633)\
  2016-09-08 16:01:28 +0400
  * [MDEV-10296](https://jira.mariadb.org/browse/MDEV-10296) - Multi-instance table cache
* [Revision #7e9ac7b](https://github.com/MariaDB/server/commit/7e9ac7b)\
  2016-06-29 16:33:08 +0400
  * [MDEV-10296](https://jira.mariadb.org/browse/MDEV-10296) - Multi-instance table cache
* [Revision #6c1c27e](https://github.com/MariaDB/server/commit/6c1c27e)\
  2016-09-15 22:02:32 +0300
  * Don't increment 'Empty\_queries' for queries with errors.
* [Revision #7ca60dd](https://github.com/MariaDB/server/commit/7ca60dd)\
  2016-09-15 21:56:01 +0300
  * Test case for fix assertion/hang in read\_init\_file()
* [Revision #55eb6fa](https://github.com/MariaDB/server/commit/55eb6fa)\
  2016-09-14 11:44:41 -0700
  * Another attempt to fix bug [MDEV-10785](https://jira.mariadb.org/browse/MDEV-10785) + cleanup for the previous attempt.
* [Revision #c22d307](https://github.com/MariaDB/server/commit/c22d307)\
  2016-09-14 01:06:45 -0700
  * Fixed bug [MDEV-10785](https://jira.mariadb.org/browse/MDEV-10785). The condition pushed into WHERE/HAVING of a materialized view/derived table may differ for different executions of the same prepared statement. That's why the should be ANDed with the existing WHERE/HAVING conditions only after all permanent transformations of these conditions has been performed.
* [Revision #61d46e0](https://github.com/MariaDB/server/commit/61d46e0) 2016-09-13 12:10:53 -0700 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* [Revision #a0db19b](https://github.com/MariaDB/server/commit/a0db19b)\
  2016-09-13 20:28:58 +0400
  * [MDEV-10779](https://jira.mariadb.org/browse/MDEV-10779) Failing assertion lex->proc\_list.elements == 0 or syntax error on PROCEDURE ANALYSE in UNION
* [Revision #08ba474](https://github.com/MariaDB/server/commit/08ba474)\
  2016-09-13 11:58:35 -0700
  * Fixed bug [MDEV-10783](https://jira.mariadb.org/browse/MDEV-10783). Do not push conditions into materialized views/derived tables marked with the flag 'fill\_me'.
* [Revision #54b81ac](https://github.com/MariaDB/server/commit/54b81ac)\
  2016-09-12 18:50:47 +0200
  * Window functions fail with --ps-protocol
* [Revision #ec59220](https://github.com/MariaDB/server/commit/ec59220)\
  2016-09-12 13:53:55 +0200
  * post-merge fixes for ec47bea
* [Revision #025c4ec](https://github.com/MariaDB/server/commit/025c4ec)\
  2016-09-12 14:29:01 +0300
  * Fix sysvars\_server\_notembedded rdiff for 32-bit
* [Revision #fd5df6f](https://github.com/MariaDB/server/commit/fd5df6f) 2016-09-12 13:53:39 +0400 - Merge pull request #232 from 0xAX/no-need-to-zero-vio-net
* [Revision #077da07](https://github.com/MariaDB/server/commit/077da07)\
  2016-09-09 16:35:31 +0600
  * no need to set net->vio to zero in mysql\_real\_connect
* [Revision #76a0ed2](https://github.com/MariaDB/server/commit/76a0ed2)\
  2016-09-12 13:11:35 +0400
  * alter\_table.test bug fixed.
* [Revision #3630a00](https://github.com/MariaDB/server/commit/3630a00)\
  2016-09-12 00:07:02 -0700
  * Fixed bug [MDEV-10782](https://jira.mariadb.org/browse/MDEV-10782). This bug in the code of Item\_ref::build\_clone could cause corruption of items in where conditions. Also made sure that equality predicates extracted from multiple equality items to be pushed into materialized views were cloned.
* [Revision #9810d5e](https://github.com/MariaDB/server/commit/9810d5e)\
  2016-09-11 11:55:57 +0200
  * Helper function for debugging.
* [Revision #1168e2f](https://github.com/MariaDB/server/commit/1168e2f) 2016-09-09 13:25:45 -0700 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* [Revision #49b2502](https://github.com/MariaDB/server/commit/49b2502)\
  2016-09-09 18:09:59 +0200
  * Fix assertion/hang in read\_init\_file()
* [Revision #be2b833](https://github.com/MariaDB/server/commit/be2b833)\
  2016-09-09 18:53:01 +0300
  * It is now possible to remove values multiple times from window functions
* [Revision #a37f24b](https://github.com/MariaDB/server/commit/a37f24b)\
  2016-09-09 18:21:08 +0300
  * Add min/max test cases for window functions
* [Revision #14690c7](https://github.com/MariaDB/server/commit/14690c7)\
  2016-09-09 18:21:36 +0300
  * Enable almost all aggregate functions for window functions
* [Revision #dfd3be9](https://github.com/MariaDB/server/commit/dfd3be9)\
  2016-09-09 14:46:47 +0300
  * Make cursor implementation uniform
* [Revision #ffed20c](https://github.com/MariaDB/server/commit/ffed20c)\
  2016-09-07 22:36:47 +0300
  * Extend Frame\_cursor to report the current row it is pointing at
* [Revision #e174b13](https://github.com/MariaDB/server/commit/e174b13)\
  2016-09-07 22:32:48 +0300
  * Add a method to disable the automatic adding of values from cursors
* [Revision #3ba867b](https://github.com/MariaDB/server/commit/3ba867b)\
  2016-09-07 21:35:56 +0300
  * Convert Partition\_read\_cursor to inherit from Table\_read\_cursor
* [Revision #1adc3fa](https://github.com/MariaDB/server/commit/1adc3fa)\
  2016-09-04 05:51:10 +0300
  * [MDEV-10097](https://jira.mariadb.org/browse/MDEV-10097): Assertion \`count > 0' failed in Item\_sum\_sum::add\_helper(bool)
* [Revision #23e8b50](https://github.com/MariaDB/server/commit/23e8b50)\
  2016-09-01 18:10:15 +0300
  * [MDEV-10059](https://jira.mariadb.org/browse/MDEV-10059): Compute window functions with same sorting criteria simultaneously
* [Revision #19d24f0](https://github.com/MariaDB/server/commit/19d24f0)\
  2016-09-08 16:36:23 +0200
  * [MDEV-10763](https://jira.mariadb.org/browse/MDEV-10763): Wrong result - server does not return NULL values from default list partition after ALTER table
* [Revision #b22ed66](https://github.com/MariaDB/server/commit/b22ed66)\
  2016-09-08 19:43:09 +0200
  * [MDEV-10765](https://jira.mariadb.org/browse/MDEV-10765): Wrong result - query does not retrieve values from default partition on a table partitioned by list columns
* [Revision #2c52493](https://github.com/MariaDB/server/commit/2c52493)\
  2016-09-09 13:12:47 +0200
  * Fixed condition
* [Revision #ec47bea](https://github.com/MariaDB/server/commit/ec47bea) 2016-09-09 12:15:53 +0200 - Merge parallel replication async deadlock kill into 10.2.
* [Revision #7e0c9de](https://github.com/MariaDB/server/commit/7e0c9de)\
  2016-09-08 15:25:40 +0200
  * Parallel replication async deadlock kill
* [Revision #06b7fce](https://github.com/MariaDB/server/commit/06b7fce) 2016-09-09 08:33:08 +0200 - Merge branch '10.1' into 10.2
* [Revision #8494039](https://github.com/MariaDB/server/commit/8494039)\
  2016-09-06 16:34:25 +0200
  * fix the test to work
* [Revision #61fd38a](https://github.com/MariaDB/server/commit/61fd38a)\
  2016-09-05 17:11:14 +0200
  * update plugin maturities
* [Revision #362ad94](https://github.com/MariaDB/server/commit/362ad94)\
  2016-09-05 09:11:42 +0200
  * cleanup: don't copy-paste, don't current\_thd
* [Revision #747893a](https://github.com/MariaDB/server/commit/747893a)\
  2016-09-02 14:40:09 -0400
  * [MDEV-10545](https://jira.mariadb.org/browse/MDEV-10545): Update perfschema.nesting result
* [Revision #31697d0](https://github.com/MariaDB/server/commit/31697d0)\
  2016-09-02 12:21:40 -0400
  * [MDEV-10545](https://jira.mariadb.org/browse/MDEV-10545): Server crashed in my\_copy\_fix\_mb on querying I\_S and P\_S tables
* [Revision #a322651](https://github.com/MariaDB/server/commit/a322651)\
  2016-08-29 16:44:46 +0200
  * [MDEV-10017](https://jira.mariadb.org/browse/MDEV-10017): Get unexpected `Empty Set` for correlated subquery with aggregate functions
* [Revision #f6e47c0](https://github.com/MariaDB/server/commit/f6e47c0) 2016-08-31 11:51:12 +0400 - Merge pull request #224 from 0xAX/build-get-rid-from-die
* [Revision #080ac47](https://github.com/MariaDB/server/commit/080ac47)\
  2016-08-25 15:56:53 +0600
  * remove die() from BUILD/autorun.sh
* [Revision #64fe389](https://github.com/MariaDB/server/commit/64fe389)\
  2016-08-30 10:32:37 -0400
  * bump the VERSION
* [Revision #1f2ff25](https://github.com/MariaDB/server/commit/1f2ff25)\
  2016-09-08 22:41:50 +0200
  * Fixed embedded server.
* [Revision #5c7d829](https://github.com/MariaDB/server/commit/5c7d829)\
  2016-09-09 13:25:02 -0700
  * Another attempt to fix bug [MDEV-10736](https://jira.mariadb.org/browse/MDEV-10736).
* [Revision #effb65b](https://github.com/MariaDB/server/commit/effb65b)\
  2016-09-07 19:34:11 -0700
  * Adjusted test results.
* [Revision #a2b8bdf](https://github.com/MariaDB/server/commit/a2b8bdf) 2016-09-07 15:49:56 -0700 - Merge branch '10.2' into bb-10.2-mdev9864
* [Revision #4ec088f](https://github.com/MariaDB/server/commit/4ec088f)\
  2016-08-29 22:29:12 +0200
  * [MDEV-8348](https://jira.mariadb.org/browse/MDEV-8348): Add catchall to all table partitioning for list partitions
* [Revision #95b8dcb](https://github.com/MariaDB/server/commit/95b8dcb)\
  2016-09-07 17:09:29 +0300
  * [MDEV-10729](https://jira.mariadb.org/browse/MDEV-10729): Server crashes in st\_select\_lex::set\_explain\_type
* [Revision #a032fd5](https://github.com/MariaDB/server/commit/a032fd5)\
  2016-09-07 16:43:45 +0400
  * [MDEV-10758](https://jira.mariadb.org/browse/MDEV-10758) engines/funcs.db\_alter\_collate\_ascii and engines/funcs.db\_alter\_collate\_utf8 fail with wrong results
* [Revision #e305054](https://github.com/MariaDB/server/commit/e305054)\
  2016-09-07 12:22:41 +0300
  * [MDEV-10058](https://jira.mariadb.org/browse/MDEV-10058): Suspicious EXPLAIN output for a derived table + WITH + joined tabl
* [Revision #4c39f75](https://github.com/MariaDB/server/commit/4c39f75)\
  2016-09-07 11:35:06 +0300
  * [MDEV-10057](https://jira.mariadb.org/browse/MDEV-10057): Crash with EXPLAIN + WITH + constant query
* [Revision #06ba09d](https://github.com/MariaDB/server/commit/06ba09d) 2016-09-07 11:17:41 +0300 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* [Revision #dd283db](https://github.com/MariaDB/server/commit/dd283db)\
  2016-09-07 11:36:22 +0400
  * [MDEV-8909](https://jira.mariadb.org/browse/MDEV-8909) union parser cleanup
* [Revision #5e20c61](https://github.com/MariaDB/server/commit/5e20c61)\
  2016-09-07 08:13:17 +1000
  * [MDEV-10707](https://jira.mariadb.org/browse/MDEV-10707) Tokudb tokudb\_parts test suites failing (#229)
* [Revision #a6fb647](https://github.com/MariaDB/server/commit/a6fb647)\
  2016-07-29 18:21:08 +0200
  * [MDEV-10419](https://jira.mariadb.org/browse/MDEV-10419): crash in [mariadb 10.1.16](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10116-release-notes.md)-MariaDB-1trusty
* [Revision #82626d7](https://github.com/MariaDB/server/commit/82626d7)\
  2016-09-07 08:51:18 -0700
  * Adjusted test results.
* [Revision #5684f9d](https://github.com/MariaDB/server/commit/5684f9d) 2016-09-06 14:43:05 -0700 - Merge branch '10.2' into bb-10.2-mdev9864
* [Revision #d6f87e6](https://github.com/MariaDB/server/commit/d6f87e6)\
  2016-09-06 14:36:59 -0700
  * For some unclear reasons the test case for bug [MDEV-10736](https://jira.mariadb.org/browse/MDEV-10736) does not work in non-debug modes.
* [Revision #dc9b092](https://github.com/MariaDB/server/commit/dc9b092)\
  2016-09-06 11:20:50 -0700
  * More cleanup.
* [Revision #2c6d620](https://github.com/MariaDB/server/commit/2c6d620) 2016-09-06 10:57:14 -0700 - Merge branch '10.2' into bb-10.2-mdev9864
* [Revision #2d36e5a](https://github.com/MariaDB/server/commit/2d36e5a)\
  2016-09-06 10:05:36 -0700
  * Fixed bug [MDEV-10736](https://jira.mariadb.org/browse/MDEV-10736) that caused crashes. The bug manifested itself for recursive definitions that used anchors over tables with blobs.
* [Revision #2254400](https://github.com/MariaDB/server/commit/2254400)\
  2016-09-06 14:42:33 +0400
  * [MDEV-10421](https://jira.mariadb.org/browse/MDEV-10421) duplicate CHECK CONSTRAINTs.
* [Revision #00dfe27](https://github.com/MariaDB/server/commit/00dfe27)\
  2016-09-06 14:42:54 +0400
  * Recording information\_schema.result (forgotten in the patch for [MDEV-9711](https://jira.mariadb.org/browse/MDEV-9711))
* [Revision #ee19806](https://github.com/MariaDB/server/commit/ee19806)\
  2016-09-06 12:50:02 +0400
  * [MDEV-9711](https://jira.mariadb.org/browse/MDEV-9711) NO PAD collations
* [Revision #e4f6fd5](https://github.com/MariaDB/server/commit/e4f6fd5)\
  2016-09-06 12:37:11 +0400
  * [MDEV-10743](https://jira.mariadb.org/browse/MDEV-10743) LDML: a new syntax to reuse sort order from another 8bit simple collation
* [Revision #8ae6592](https://github.com/MariaDB/server/commit/8ae6592)\
  2016-09-05 23:07:31 -0700
  * Fixed bug [MDEV-10737](https://jira.mariadb.org/browse/MDEV-10737). This bug in st\_select\_lex\_node::move\_node could result in invalid select lists in recursive units that could cause falling into infinite loops when iterating over selects in such units.
* [Revision #2f83cc6](https://github.com/MariaDB/server/commit/2f83cc6)\
  2016-09-06 09:11:34 -0700
  * Removed redefinitions of some newly introduced constants.
* [Revision #9fc2358](https://github.com/MariaDB/server/commit/9fc2358) 2016-09-05 22:13:01 -0700 - Merge branch '10.2' into bb-10.2-mdev9864
* [Revision #aaedb63](https://github.com/MariaDB/server/commit/aaedb63)\
  2016-09-05 16:01:44 +0300
  * [MDEV-10741](https://jira.mariadb.org/browse/MDEV-10741) sys\_vars.sysvars\_server\_embedded 32-bit fails in buildbot
* [Revision #9e89e11](https://github.com/MariaDB/server/commit/9e89e11)\
  2016-09-05 10:03:10 +0400
  * [MDEV-10742](https://jira.mariadb.org/browse/MDEV-10742) LDML: make conf\_to\_src reuse common data between collations
* [Revision #de02bfd](https://github.com/MariaDB/server/commit/de02bfd)\
  2016-09-05 22:10:50 -0700
  * The code that pushed conditions into derived did not take into account that the list of equal items in an Item\_equal object may contain items with type() == REF\_ITEM.
* [Revision #7faff4d](https://github.com/MariaDB/server/commit/7faff4d) 2016-09-04 20:42:07 -0700 - Merge branch '10.2' into 10.2-mdev9197
* [Revision #1da21cd](https://github.com/MariaDB/server/commit/1da21cd)\
  2016-06-02 12:12:26 +0200
  * [MDEV-10035](https://jira.mariadb.org/browse/MDEV-10035): DBUG\_ASSERT on CREATE VIEW v1 AS SELECT \* FROM t1 FOR UPDATE
* [Revision #3dcca1b](https://github.com/MariaDB/server/commit/3dcca1b)\
  2016-09-03 14:25:04 +0400
  * A fix for 1ca595fbf7d186bbe9f2f9896869b316d6e9567a (LDML refactoring)
* [Revision #1ca595f](https://github.com/MariaDB/server/commit/1ca595f)\
  2016-09-03 09:05:56 +0400
  * LDML refactoring for "[MDEV-9711](https://jira.mariadb.org/browse/MDEV-9711) NO PAD collations"
* [Revision #3b40f78](https://github.com/MariaDB/server/commit/3b40f78)\
  2016-09-04 20:11:58 -0700
  * Fixed a flaw in the implementation of condition push-down for materialized views and derived tables: there were no push-down if the view was defined as union of selects without aggregation. Added test cases with such unions.
* [Revision #102fc62](https://github.com/MariaDB/server/commit/102fc62)\
  2016-09-01 23:44:42 -0700
  * Fixed a failure with cte\_recursive.test: Do not push conditions into recursive with tables.
* [Revision #4de75af](https://github.com/MariaDB/server/commit/4de75af)\
  2016-09-01 23:37:27 -0700
  * Fixed the previous merge to be able to build mysqld. Adjusted one result file.
* [Revision #17622bc](https://github.com/MariaDB/server/commit/17622bc) 2016-09-01 15:07:10 -0700 - Merge branch '10.2' into 10.2-mdev9197
* [Revision #addb38f](https://github.com/MariaDB/server/commit/addb38f)\
  2016-09-01 21:15:17 +0300
  * More DBUG\_PRINT's to make it easier to debug parallel replication
* [Revision #b6e4362](https://github.com/MariaDB/server/commit/b6e4362)\
  2016-09-01 21:11:47 +0300
  * Split rpl\_parallel into two tests to make it easier to know what goes wrong. rpl\_parallel\_conflicts now contains the tests that can cause row conflicts in replication.
* [Revision #e19ca69](https://github.com/MariaDB/server/commit/e19ca69)\
  2016-09-01 19:52:04 +0300
  * Update test results, mysql-test/r/mysqld--help,win.rdiff
* [Revision #dd31e5c](https://github.com/MariaDB/server/commit/dd31e5c)\
  2016-08-26 16:39:32 +0400
  * [MDEV-9593](https://jira.mariadb.org/browse/MDEV-9593) - Print the real version in the error log
* [Revision #3fb4f9b](https://github.com/MariaDB/server/commit/3fb4f9b) 2016-08-31 16:16:54 -0700 - Merge branch '10.2-mdev9197-cons' of github.com:shagalla/server into branch 10.2-mdev9197.
* [Revision #eb2c147](https://github.com/MariaDB/server/commit/eb2c147)\
  2016-05-01 22:29:47 +0300
  * The consolidated patch for [MDEV-9197](https://jira.mariadb.org/browse/MDEV-9197).
* [Revision #670760d](https://github.com/MariaDB/server/commit/670760d)\
  2016-08-31 10:51:31 -0700
  * Adjusted test results after the previous merge.
* [Revision #080f16a](https://github.com/MariaDB/server/commit/080f16a) 2016-08-31 10:49:36 -0700 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mdev9864
* [Revision #d8ad96e](https://github.com/MariaDB/server/commit/d8ad96e)\
  2016-08-31 20:50:19 +0300
  * Update sys\_vars.sysvars\_server\_embedded after recent pushes
* [Revision #f11e892](https://github.com/MariaDB/server/commit/f11e892) 2016-08-31 10:34:21 -0700 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mdev9864
* [Revision #1eb58ff](https://github.com/MariaDB/server/commit/1eb58ff)\
  2016-08-31 20:33:28 +0300
  * Update mysql-test/r/mysqld--help,win.rdiff
* [Revision #7b86fda](https://github.com/MariaDB/server/commit/7b86fda)\
  2016-08-28 09:44:49 +0200
  * Fixed length of codding of COM\_MULTI parts.
* [Revision #6dfa1d3](https://github.com/MariaDB/server/commit/6dfa1d3)\
  2016-08-09 15:49:30 +0200
  * [MDEV-8931](https://jira.mariadb.org/browse/MDEV-8931): (server part of) session state tracking
* [Revision #0ee3e64](https://github.com/MariaDB/server/commit/0ee3e64)\
  2016-05-30 21:22:50 +0200
  * [MDEV-8931](https://jira.mariadb.org/browse/MDEV-8931): (server part of) session state tracking
* [Revision #c8948b0](https://github.com/MariaDB/server/commit/c8948b0)\
  2016-04-15 20:47:45 +0200
  * [MDEV-8931](https://jira.mariadb.org/browse/MDEV-8931): (server part of) session state tracking
* [Revision #e7608a7](https://github.com/MariaDB/server/commit/e7608a7)\
  2016-04-15 20:40:25 +0200
  * [MDEV-8931](https://jira.mariadb.org/browse/MDEV-8931): (server part of) session state tracking
* [Revision #468a6ad](https://github.com/MariaDB/server/commit/468a6ad)\
  2016-08-31 11:48:51 +0400
  * Fixed package build failure README -> README.md
* [Revision #c650a73](https://github.com/MariaDB/server/commit/c650a73) 2016-08-31 09:43:57 +0400 - Merge pull request #222 from grooverdan/10.2-README-markdown
* [Revision #8cbc96b](https://github.com/MariaDB/server/commit/8cbc96b)\
  2016-08-24 15:00:59 +1000
  * Markdown README for a prettier github representation
* [Revision #2250e9e](https://github.com/MariaDB/server/commit/2250e9e) 2016-08-30 16:14:51 -0700 - Merge 10.2 into 10.2-mdev9864.
* [Revision #4ca7b22](https://github.com/MariaDB/server/commit/4ca7b22)\
  2016-08-30 09:16:50 +0300
  * Safety fix to previous patch
* [Revision #bbfb5d7](https://github.com/MariaDB/server/commit/bbfb5d7)\
  2016-08-29 20:33:25 +0300
  * Fixed failures for privilege\_table\_io and wsrep\_cluster\_address\_basic
* [Revision #1c91569](https://github.com/MariaDB/server/commit/1c91569)\
  2016-08-29 20:28:06 +0300
  * Set server\_id to 1 by default and disallow to set it to 0 This makes it easier to setup master as on only have to set --log-bin. Before this patch if one did set up the master with just --log-bin, slaves could not connect until server\_id was set on the master, which could be both confusing and hard to do.
* [Revision #e139d97](https://github.com/MariaDB/server/commit/e139d97)\
  2016-08-29 13:11:34 +0300
  * Fixed compiler warning and failing test suite because system dependency
* [Revision #96e95b5](https://github.com/MariaDB/server/commit/96e95b5)\
  2016-08-29 13:10:17 +0300
  * Better SHOW PROCESSLIST for replication - When waiting for events, start time is now counted from start of wait - Instead of having "Connect" as "Command" for all replication threads we now have: - Slave\_IO for Slave thread reading relay log - Slave\_SQL for slave executing SQL commands or distribution queries to Slave workers - Slave\_worker for slave threads executin SQL commands in parallel replication
* [Revision #eac7e57](https://github.com/MariaDB/server/commit/eac7e57)\
  2016-07-25 22:15:05 +0200
  * Feature\_check\_constraint status variable
* [Revision #7450cb7](https://github.com/MariaDB/server/commit/7450cb7)\
  2016-07-25 17:57:31 +0200
  * re-fix vcols on demand, not always for every SELECT
* [Revision #cd51c7f](https://github.com/MariaDB/server/commit/cd51c7f)\
  2016-07-24 15:12:54 +0200
  * move away from TIMESTAMP\_DNUN\_FIELD/TIMESTAMP\_DN\_FIELD code
* [Revision #12d2c4f](https://github.com/MariaDB/server/commit/12d2c4f)\
  2016-07-23 16:55:52 +0200
  * optimize constant default expressions
* [Revision #4070d55](https://github.com/MariaDB/server/commit/4070d55)\
  2016-07-24 14:54:52 +0200
  * fix: CHECK and DEFAULT after CREATE ... SELECT
* [Revision #3aff76f](https://github.com/MariaDB/server/commit/3aff76f)\
  2016-07-23 16:26:24 +0200
  * vcol flag rename VCOL\_UNKNOWN -> VCOL\_FIELD\_REF
* [Revision #159dc96](https://github.com/MariaDB/server/commit/159dc96)\
  2016-07-22 15:36:31 +0200
  * cleanup: redundant variable
* [Revision #3953743](https://github.com/MariaDB/server/commit/3953743)\
  2016-07-22 14:24:23 +0200
  * clarify the comment
* [Revision #6e5048e](https://github.com/MariaDB/server/commit/6e5048e)\
  2016-07-22 13:48:21 +0200
  * clarify the error message for frm size overflow
* [Revision #266563a](https://github.com/MariaDB/server/commit/266563a)\
  2016-07-22 13:44:58 +0200
  * fix: CREATE TABLE (col TIMESTAMP(6) DEFAULT NOW(2))
* [Revision #73a220a](https://github.com/MariaDB/server/commit/73a220a)\
  2016-07-25 14:34:37 +0200
  * session-state dependent functions in DEFAULT/CHECK/vcols
* [Revision #eb9bce5](https://github.com/MariaDB/server/commit/eb9bce5)\
  2016-07-19 22:10:54 +0200
  * split fix\_vcol\_expr()
* [Revision #ebf1e1d](https://github.com/MariaDB/server/commit/ebf1e1d)\
  2016-07-19 14:12:24 +0200
  * NULL pointer dereference
* [Revision #b48555e](https://github.com/MariaDB/server/commit/b48555e)\
  2016-07-21 17:46:41 +0200
  * fix: DEFAULT() in a view should be not updatable
* [Revision #2013a7f](https://github.com/MariaDB/server/commit/2013a7f)\
  2016-07-21 14:03:49 +0200
  * fix: CURRENT\_ROLE() inside SECURITY DEFINER views
* [Revision #6820bf9](https://github.com/MariaDB/server/commit/6820bf9)\
  2016-07-19 11:18:58 +0200
  * do not quote numbers in the DEFAULT clause in SHOW CREATE
* [Revision #c5c9128](https://github.com/MariaDB/server/commit/c5c9128)\
  2016-07-24 16:54:01 +0200
  * cleanup: use multi\_alloc\_root
* [Revision #1fd8b0a](https://github.com/MariaDB/server/commit/1fd8b0a) 2016-08-27 08:33:46 +0400 - Merge pull request #226 from 0xAX/profile-must-be-enabled
* [Revision #e7f5443](https://github.com/MariaDB/server/commit/e7f5443)\
  2016-08-26 16:49:46 +0600
  * Call profiling.restart() and profiling.reset() only if profiling is enabled
* [Revision #cb1e442](https://github.com/MariaDB/server/commit/cb1e442)\
  2016-08-30 11:13:25 -0700
  * Adjusted test results.
* [Revision #501fc1a](https://github.com/MariaDB/server/commit/501fc1a)\
  2016-08-29 22:58:01 -0700
  * Returned the test case that was removed by mistake.
* [Revision #9ac235a](https://github.com/MariaDB/server/commit/9ac235a)\
  2016-08-29 22:45:17 -0700
  * [MDEV-9864](https://jira.mariadb.org/browse/MDEV-9864): cleanup, re-factoring. Added comments. Added reaction for exceeding maximum number of elements in with clause. Added a test case to check this reaction. Added a test case where the specification of a recursive table uses two non-recursive with tables.
* [Revision #c8f85bf](https://github.com/MariaDB/server/commit/c8f85bf)\
  2016-08-26 16:09:22 -0700
  * [MDEV-9864](https://jira.mariadb.org/browse/MDEV-9864): cleanup, re-factoring. Added comments.
* [Revision #f33c352](https://github.com/MariaDB/server/commit/f33c352)\
  2016-08-11 14:39:26 -0700
  * Adjusted test result.
* [Revision #2f9555c](https://github.com/MariaDB/server/commit/2f9555c)\
  2016-08-10 15:51:40 -0700
  * Removed the parameter from st\_select\_lex\_unit::exec\_recursive. Moved checking whether the limit set for the number of iterations when executing a recursive query has been reached from st\_select\_lex\_unit::exec\_recursive to TABLE\_LIST::fill\_recursive. Changed the name of the system variable max\_recursion\_level for max\_recursive\_iterations. Adjusted test cases.
* [Revision #e20e28b](https://github.com/MariaDB/server/commit/e20e28b)\
  2016-08-10 01:13:09 +0300
  * Fix for the previous cset: make first\_explain\_order\_tab handle degenerate joins
* [Revision #a2f245e](https://github.com/MariaDB/server/commit/a2f245e)\
  2016-08-08 23:02:52 +0300
  * [MDEV-10372](https://jira.mariadb.org/browse/MDEV-10372): EXPLAIN fixes for recursive CTEs, including FORMAT=JSON
* [Revision #e1c92a6](https://github.com/MariaDB/server/commit/e1c92a6)\
  2016-08-05 14:12:01 -0700
  * Fixed a problem with unreferenced CTE: explain for the query containing WITH clause with an unreferenced CTE caused a crash. Added a test covered this case.
* [Revision #247632e](https://github.com/MariaDB/server/commit/247632e)\
  2016-07-29 01:10:00 -0700
  * Fixed bug [MDEV-10344](https://jira.mariadb.org/browse/MDEV-10344). The patch for bug [MDEV-9937](https://jira.mariadb.org/browse/MDEV-9937) actually did not fix the problem of name resolution for tables used in views referred in queries with WITH clauses. This fix corrects the patch.
* [Revision #f982d10](https://github.com/MariaDB/server/commit/f982d10)\
  2016-07-26 22:58:33 -0700
  * Fixed the following problem: Temporary tables created for recursive CTE were instantiated at the prepare phase. As a result these temporary tables missed indexes for look-ups and optimizer could not use them.
* [Revision #8c6a9aa](https://github.com/MariaDB/server/commit/8c6a9aa)\
  2016-06-30 15:13:12 -0700
  * Added a proper check for acceptable mutually recursive CTE.
* [Revision #22c37c1](https://github.com/MariaDB/server/commit/22c37c1)\
  2016-06-29 15:20:24 -0700
  * Adjusted test results.
* [Revision #9606525](https://github.com/MariaDB/server/commit/9606525)\
  2016-06-25 21:38:40 -0700
  * Simplified the code that fills recursive tables.
* [Revision #0eec187](https://github.com/MariaDB/server/commit/0eec187)\
  2016-06-07 15:01:34 -0700
  * A commit to force buildbot working.
* [Revision #096286c](https://github.com/MariaDB/server/commit/096286c)\
  2016-06-07 11:06:54 -0700
  * The method With\_element::reset\_for\_exec was not called in non-debug builds.
* [Revision #0a6e6d7](https://github.com/MariaDB/server/commit/0a6e6d7)\
  2016-06-06 10:01:16 -0700
  * Fixed numerous problems for mutually recursive CTE. Actually mutually recursive CTE were not functional. Now the code for mutually recursive CTE looks like functional, but still needs re-writing. Added many new test cases for mutually recursive CTE.
* [Revision #6c6c3af](https://github.com/MariaDB/server/commit/6c6c3af) 2016-05-25 00:34:13 +0300 - Merge branch '10.2' into 10.2-mdev9864
* [Revision #c7c2f8d](https://github.com/MariaDB/server/commit/c7c2f8d) 2016-05-25 00:29:13 +0300 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* [Revision #b4f1f42](https://github.com/MariaDB/server/commit/b4f1f42)\
  2016-05-24 21:29:52 +0300
  * Fixed the problem of wrong identification of WITH tables defined in WITH clauses without RECURSIVE. Added test cases to check the fix. Fixed the problem of wrong types of recursive tables when the type of anchor part does not coincide with the type of recursive part. Prevented usage of marerialization and subquery cache for subqueries with recursive references. Introduced system variables 'max\_recursion\_level'. Added a test case to test usage of this variable.
* [Revision #0f7fe2a](https://github.com/MariaDB/server/commit/0f7fe2a)\
  2016-05-19 23:17:19 +0300
  * Changes in test files
* [Revision #46a2e41](https://github.com/MariaDB/server/commit/46a2e41)\
  2016-05-19 22:07:53 +0300
  * Fixed many problems in the code of With\_element::check\_unrestricted\_recursive(). Added the check whether there are set functions in the specifications of recursive CTE. Added the check whether there are recursive references in subqueries. Introduced boolean system variable 'standards\_compliant\_cte'. By default it's set to 'on'. When it's set to 'off' non-standard compliant CTE can be executed.
* [Revision #3b47632](https://github.com/MariaDB/server/commit/3b47632)\
  2016-05-14 23:33:50 +0300
  * Fixed a bug that caused crashes for SHOW CREATE VIEW when was recursive. Added a test case to check the fix.
* [Revision #d9b332b](https://github.com/MariaDB/server/commit/d9b332b)\
  2016-05-12 23:23:12 +0300
  * Made prepared statement, explain and views working with recursuve CTE.
* [Revision #d0e973a](https://github.com/MariaDB/server/commit/d0e973a)\
  2016-05-10 22:32:02 +0300
  * Fixed merge problems to allow mysql-test suite 'main' to pass
* [Revision #f516b96](https://github.com/MariaDB/server/commit/f516b96)\
  2016-05-09 23:39:10 +0300
  * Main patch for [MDEV-9864](https://jira.mariadb.org/browse/MDEV-9864)
* [Revision #5703d26](https://github.com/MariaDB/server/commit/5703d26) 2016-05-09 21:54:22 +0300 - Merge branch '10.2' into 10.2-mdev9864
* [Revision #93845e1](https://github.com/MariaDB/server/commit/93845e1)\
  2016-05-08 21:19:51 +0300
  * Initial commit for [MDEV-9864](https://jira.mariadb.org/browse/MDEV-9864) containing only test files
* [Revision #be1d06c](https://github.com/MariaDB/server/commit/be1d06c)\
  2016-05-08 23:04:41 +0300
  * Merge branch '10.2' into 10.2-mdev9864
* [Revision #e09b1f2](https://github.com/MariaDB/server/commit/e09b1f2)\
  2016-05-08 21:50:13 +0300
  * Initial commit just to make a branch for [MDEV-9864](https://jira.mariadb.org/browse/MDEV-9864)
* [Revision #fb8bc59](https://github.com/MariaDB/server/commit/fb8bc59)\
  2016-09-16 07:27:23 +0200
  * mysqld\_safe: don't use "$DATADIR/my.cnf"
* [Revision #7fc36e6](https://github.com/MariaDB/server/commit/7fc36e6)\
  2016-09-17 12:38:47 +0200
  * set the default socket addr for C/C
* [Revision #992606f](https://github.com/MariaDB/server/commit/992606f)\
  2016-09-17 10:15:09 +0200
  * only put real _.so._ shared libraries in compat.rpm
* [Revision #a749246](https://github.com/MariaDB/server/commit/a749246)\
  2016-09-16 12:21:05 +0200
  * a couple of C/C bugs to fix failures in ps-protocol
* [Revision #b138414](https://github.com/MariaDB/server/commit/b138414)\
  2016-09-15 15:31:28 +0200
  * fix many rpl test failures
* [Revision #ddc481b](https://github.com/MariaDB/server/commit/ddc481b)\
  2016-09-15 09:22:04 +0200
  * tls fixes in c/c
* [Revision #9ee34f7](https://github.com/MariaDB/server/commit/9ee34f7)\
  2016-09-14 16:09:33 +0200
  * install client plugins into their old location
* [Revision #2ae5c55](https://github.com/MariaDB/server/commit/2ae5c55)\
  2016-09-13 14:29:04 +0200
  * debian builds
* [Revision #e5c36c7](https://github.com/MariaDB/server/commit/e5c36c7)\
  2016-09-12 23:00:40 +0200
  * fix mysql\_client\_test test
* [Revision #694fd4e](https://github.com/MariaDB/server/commit/694fd4e)\
  2016-09-12 19:15:01 +0200
  * restore support for symbol versioning in libmysqld
* [Revision #cacb57b](https://github.com/MariaDB/server/commit/cacb57b)\
  2016-09-12 18:16:51 +0200
  * pass openssl config to C/C
* [Revision #0aa6817](https://github.com/MariaDB/server/commit/0aa6817)\
  2016-09-07 19:16:43 +0200
  * name clash with gnutls on base64\_encode
* [Revision #5ea5a7f](https://github.com/MariaDB/server/commit/5ea5a7f)\
  2016-09-05 08:09:16 +0200
  * auto-clone C/C, if possible
* [Revision #79fa256](https://github.com/MariaDB/server/commit/79fa256)\
  2016-09-04 14:04:40 +0200
  * really add a submodule
* [Revision #ece01ef](https://github.com/MariaDB/server/commit/ece01ef)\
  2016-09-03 14:04:17 +0200
  * After-review changes
* [Revision #1206763](https://github.com/MariaDB/server/commit/1206763)\
  2016-09-03 11:31:44 +0200
  * Build 10.1 compat rpm
* [Revision #10e1ff8](https://github.com/MariaDB/server/commit/10e1ff8)\
  2016-09-04 13:42:01 +0200
  * better identify C/C unit tests in mysql-test
* [Revision #017195c](https://github.com/MariaDB/server/commit/017195c)\
  2016-09-04 13:41:45 +0200
  * fix RPM builds
* [Revision #85828b8](https://github.com/MariaDB/server/commit/85828b8)\
  2016-09-04 13:41:03 +0200
  * fix "make dist" to support submodules
* [Revision #ed0b84a](https://github.com/MariaDB/server/commit/ed0b84a)\
  2016-09-04 13:35:14 +0200
  * remove libmysql/
* [Revision #4ba198c](https://github.com/MariaDB/server/commit/4ba198c)\
  2016-09-04 13:33:59 +0200
  * compiler warning
* [Revision #365f199](https://github.com/MariaDB/server/commit/365f199)\
  2016-09-12 17:47:06 +0200
  * fix the plugin suite to pass
* [Revision #1fc49d3](https://github.com/MariaDB/server/commit/1fc49d3)\
  2016-09-04 13:26:30 +0200
  * Add C/C as a submodule in libmariadb/
* [Revision #ca02ad4](https://github.com/MariaDB/server/commit/ca02ad4)\
  2016-09-04 13:32:31 +0200
  * fix cmake MESSAGE\_ONCE macro for multi-line messages
* [Revision #6152784](https://github.com/MariaDB/server/commit/6152784)\
  2016-09-05 16:05:13 +0200
  * make CONNECT's finding Java and JNI less verbose
* [Revision #58f20b0](https://github.com/MariaDB/server/commit/58f20b0)\
  2016-09-04 13:23:03 +0200
  * Set cmake policy CMP0054 NEW
* [Revision #663835f](https://github.com/MariaDB/server/commit/663835f)\
  2016-09-03 11:23:51 +0200
  * .gitignore for rpm builds
* [Revision #34f3fd2](https://github.com/MariaDB/server/commit/34f3fd2)\
  2016-08-22 16:45:46 +0200
  * add libmysqlclient's dependencies to the output of mysql\_config
* [Revision #22ea51e](https://github.com/MariaDB/server/commit/22ea51e)\
  2016-08-21 12:01:57 +0000
  * Increase shared library version
* [Revision #56c4cfe](https://github.com/MariaDB/server/commit/56c4cfe)\
  2016-08-19 20:03:05 +0000
  * [MDEV-9293](https://jira.mariadb.org/browse/MDEV-9293) - Use MariaDB's Connector/C in server
* [Revision #31a8cf5](https://github.com/MariaDB/server/commit/31a8cf5)\
  2016-08-19 15:46:27 +0000
  * Revert "[MDEV-9293](https://jira.mariadb.org/browse/MDEV-9293) Connector/C integration"
* [Revision #7b89b9f](https://github.com/MariaDB/server/commit/7b89b9f)\
  2016-08-19 15:27:37 +0000
  * [MDEV-9293](https://jira.mariadb.org/browse/MDEV-9293) Connector/C integration
* [Revision #daff133](https://github.com/MariaDB/server/commit/daff133)\
  2016-08-18 12:47:20 +0400
  * [MDEV-9185](https://jira.mariadb.org/browse/MDEV-9185) - Integrate with Travis-CI for easier and more automatic QA
* [Revision #69052ed](https://github.com/MariaDB/server/commit/69052ed)\
  2016-08-08 17:29:22 -0400
  * [MDEV-10320](https://jira.mariadb.org/browse/MDEV-10320): NO-OP ALTER TABLE on temporary tables getting
* [Revision #df9b455](https://github.com/MariaDB/server/commit/df9b455)\
  2016-08-08 17:26:06 -0400
  * [MDEV-10216](https://jira.mariadb.org/browse/MDEV-10216): Assertion \`strcmp(share->unique\_file\_name,filename) ||
* [Revision #45ffbda](https://github.com/MariaDB/server/commit/45ffbda)\
  2016-08-05 14:36:07 +1000
  * [MDEV-9872](https://jira.mariadb.org/browse/MDEV-9872): used optimized crc32 for SQL CRC32 function
* [Revision #c82bc56](https://github.com/MariaDB/server/commit/c82bc56)\
  2016-08-05 14:16:35 +1000
  * crc32-vpmsum: Restore non volatile registers on zero length CRC
* [Revision #a2c826b](https://github.com/MariaDB/server/commit/a2c826b)\
  2016-03-15 18:02:51 +1100
  * [MDEV-9872](https://jira.mariadb.org/browse/MDEV-9872): New Power8 crc32(ieee) optimized functions
* [Revision #e7e313f](https://github.com/MariaDB/server/commit/e7e313f)\
  2016-03-15 18:03:20 +1100
  * test case for CRC32() SQL function
* [Revision #9c2215e](https://github.com/MariaDB/server/commit/9c2215e)\
  2016-07-05 16:37:42 +0400
  * [MDEV-9872](https://jira.mariadb.org/browse/MDEV-9872) - Add common optimized CRC32 function interface
* [Revision #86975e0](https://github.com/MariaDB/server/commit/86975e0)\
  2016-08-01 19:24:55 +0200
  * [MDEV-7901](https://jira.mariadb.org/browse/MDEV-7901): re-implement analyze table for low impact
* [Revision #ba4ed3e](https://github.com/MariaDB/server/commit/ba4ed3e)\
  2016-08-03 13:36:12 -0400
  * [MDEV-10492](https://jira.mariadb.org/browse/MDEV-10492): Assertion failure on shutdown when wsrep\_sst\_auth set in config
* [Revision #08683a7](https://github.com/MariaDB/server/commit/08683a7)\
  2016-07-30 14:42:49 -0400
  * Galera test fixes.
* [Revision #77a8ae0](https://github.com/MariaDB/server/commit/77a8ae0)\
  2016-07-30 14:40:47 -0400
  * Cleanup around wsrep system variables.
* [Revision #355bf4f](https://github.com/MariaDB/server/commit/355bf4f)\
  2016-07-30 14:36:41 -0400
  * Cleanup around wsrep mdl exception.
* [Revision #fb07658](https://github.com/MariaDB/server/commit/fb07658)\
  2016-07-25 13:07:50 +0200
  * [MDEV-10271](https://jira.mariadb.org/browse/MDEV-10271): Stopped SQL slave thread doesn't print a message to error log like IO thread does
* [Revision #840015f](https://github.com/MariaDB/server/commit/840015f)\
  2016-07-21 14:11:21 +0400
  * [MDEV-10238](https://jira.mariadb.org/browse/MDEV-10238) - tokudb\_bugs.db938 fails due to connection logging (also affects buildbot)
* [Revision #848d211](https://github.com/MariaDB/server/commit/848d211)\
  2016-06-29 16:29:06 +0200
  * [MDEV-10084](https://jira.mariadb.org/browse/MDEV-10084): SQL batch united response
* [Revision #05d07e3](https://github.com/MariaDB/server/commit/05d07e3)\
  2016-07-04 08:36:24 -0400
  * bump the VERSION
* [Revision #59ec397](https://github.com/MariaDB/server/commit/59ec397)\
  2016-07-03 19:12:20 +0400
  * Removing duplicate code in double-to-longlong conversion.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
