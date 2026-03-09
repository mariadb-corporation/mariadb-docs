# MariaDB 10.1.6 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.6)[Release Notes](../../old-releases/10.1/10.1.6.md)[Changelog](mariadb-10-1-6-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 27 Jul 2015

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.6.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #d517886](https://github.com/MariaDB/server/commit/d517886)\
  2015-07-23 15:48:26 +0200
  * Merge branch 'bb-10.1-serg' into 10.1
* [Revision #26f249f](https://github.com/MariaDB/server/commit/26f249f)\
  2015-07-23 10:55:24 +0200
  * compilation failures on Windows
* [Revision #0ae8bae](https://github.com/MariaDB/server/commit/0ae8bae)\
  2015-07-22 18:46:36 +0200
  * fix for 32-bit tests
* [Revision #53623d9](https://github.com/MariaDB/server/commit/53623d9)\
  2015-07-22 08:42:52 +0300
  * [MDEV-8522](https://jira.mariadb.org/browse/MDEV-8522): InnoDB: Assertion failure in file fil0fil.cc line 475
* [Revision #62b5a56](https://github.com/MariaDB/server/commit/62b5a56)\
  2015-07-21 12:51:14 +0300
  * [MDEV-8501](https://jira.mariadb.org/browse/MDEV-8501): encryption.create\_or\_replace fails in buildbot on P8 builders
* [Revision #3ff9634](https://github.com/MariaDB/server/commit/3ff9634)\
  2015-07-20 20:28:32 +0200
  * [MDEV-8508](https://jira.mariadb.org/browse/MDEV-8508) mroonga fails embedded tests in 10.1
* [Revision #3d4c69d](https://github.com/MariaDB/server/commit/3d4c69d)\
  2015-07-20 19:47:46 +0200
  * compiler warning
* [Revision #82c6b25](https://github.com/MariaDB/server/commit/82c6b25)\
  2015-07-20 19:07:59 +0200
  * Merge [10.1](https://github.com/Kentoku/MariaDB/tree/10.1) into 10.1
* [Revision #e35fd20](https://github.com/MariaDB/server/commit/e35fd20)\
  2015-07-20 18:14:31 +0200
  * Null-merge branch 'github/10.0-galera' into 10.1
* [Revision #6d3bd65](https://github.com/MariaDB/server/commit/6d3bd65)\
  2015-07-19 21:33:12 -0400
  * [MDEV-8492](https://jira.mariadb.org/browse/MDEV-8492): Windows builds fail on current 10.1
* [Revision #c57edf3](https://github.com/MariaDB/server/commit/c57edf3)\
  2015-07-20 00:28:22 +0300
  * [MDEV-8500](https://jira.mariadb.org/browse/MDEV-8500) sys\_vars.sysvars\_innodb '32bit,xtradb' fails
* [Revision #7046788](https://github.com/MariaDB/server/commit/7046788)\
  2015-07-19 10:31:24 +0200
  * Fix build failures.
* [Revision #13dbb6f](https://github.com/MariaDB/server/commit/13dbb6f)\
  2015-07-19 09:30:36 +0200
  * Merge [MDEV-8496](https://jira.mariadb.org/browse/MDEV-8496) into 10.1
* [Revision #44c4b23](https://github.com/MariaDB/server/commit/44c4b23)\
  2015-07-19 09:28:22 +0200
  * [MDEV-8496](https://jira.mariadb.org/browse/MDEV-8496): gtid\_ignore\_duplicates treats gtid\_seq\_no as 32-bit
* [Revision #d258f5f](https://github.com/MariaDB/server/commit/d258f5f)\
  2015-07-17 19:20:50 +0300
  * [MDEV-8495](https://jira.mariadb.org/browse/MDEV-8495) encryption.innodb\_first\_page fails sporadically in buildbot
* [Revision #0ad00c6](https://github.com/MariaDB/server/commit/0ad00c6)\
  2015-07-16 10:26:01 +0300
  * Fix for MySQL bug #77448 Inconsistent handling of RAND() in WHERE and HAVING
* [Revision #872a953](https://github.com/MariaDB/server/commit/872a953)\
  2015-07-15 16:27:14 +0300
  * [MDEV-8469](https://jira.mariadb.org/browse/MDEV-8469) Add RESET MASTER TO x to allow specification of binlog file nr
* [Revision #df0498f](https://github.com/MariaDB/server/commit/df0498f)\
  2015-07-14 21:38:17 -0400
  * Update sys\_vars.sys\_vars\_wsrep result.
* [Revision #ee9bdcf](https://github.com/MariaDB/server/commit/ee9bdcf)\
  2015-07-14 17:33:22 -0400
  * Binlog SE doesn't implement abort\_transaction(), so skip warning.
* [Revision #e204116](https://github.com/MariaDB/server/commit/e204116)\
  2015-07-14 17:21:35 -0400
  * Check supress\_my\_ok before sending Ok packet (logic lost during merge).
* [Revision #0e2ce3b](https://github.com/MariaDB/server/commit/0e2ce3b)\
  2015-07-14 17:16:28 -0400
  * Allow binlog row image column marking even for wsrep binlog emulation.
* [Revision #dd4d81d](https://github.com/MariaDB/server/commit/dd4d81d)\
  2015-07-14 16:58:38 -0400
  * Update read\_pos after reading from the cache.
* [Revision #dced514](https://github.com/MariaDB/server/commit/dced514)\
  2015-07-14 16:05:29 -0400
  * Merge branch '10.0-galera' into 10.1
* [Revision #75931fe](https://github.com/MariaDB/server/commit/75931fe)\
  2015-07-14 12:00:05 +0400
  * [MDEV-8362](https://jira.mariadb.org/browse/MDEV-8362) dash '-' is not recognized in charset armscii8 on select where query
* [Revision #657f8a8](https://github.com/MariaDB/server/commit/657f8a8)\
  2015-07-13 13:16:14 +0400
  * [MDEV-8456](https://jira.mariadb.org/browse/MDEV-8456) Dead code in Item\_cond::fix\_fields() and Item\_func\_between::fix\_fields()
* [Revision #6771b81](https://github.com/MariaDB/server/commit/6771b81)\
  2015-07-10 19:06:42 -0400
  * [MDEV-8383](https://jira.mariadb.org/browse/MDEV-8383) : "GRANT role TO user" does not replicate
* [Revision #f195f93](https://github.com/MariaDB/server/commit/f195f93)\
  2015-07-10 12:49:05 +0300
  * Cleanups, fixed warnings from valgrind, fixed failing tests (because on changes in WSREP initialization)
* [Revision #2488143](https://github.com/MariaDB/server/commit/2488143)\
  2015-07-10 09:18:17 +0300
  * Fixed bug found by bar where we didn't properely check length of last argument for BETWEEN This should not have caused any notable errors in most cases.
* [Revision #9bb8b74](https://github.com/MariaDB/server/commit/9bb8b74)\
  2015-07-09 14:47:32 +0300
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #a6c8014](https://github.com/MariaDB/server/commit/a6c8014)\
  2015-07-09 13:09:36 +0300
  * Speed and code space optimziation: - Cache variables.lc\_messages->errmsgs->errmsgs in variables.errmsgs
* [Revision #7780370](https://github.com/MariaDB/server/commit/7780370)\
  2015-07-08 19:20:07 +0400
  * [MDEV-8336](https://jira.mariadb.org/browse/MDEV-8336) The meaning of NO\_ZERO\_DATE is not clear for DATETIME. In some cases NO\_ZERO\_DATE did not allow datetime values with zero date part and non-zero time part (e.g. '0000-00-00 10:20:30.123456'). Allowing values of this kind in all known pieces of the code.
* [Revision #8154ef4](https://github.com/MariaDB/server/commit/8154ef4)\
  2015-07-07 22:26:44 -0400
  * [MDEV-7067](https://jira.mariadb.org/browse/MDEV-7067): Server outputs Galera (WSREP) information, even if Galera is disabled
* [Revision #b08c420](https://github.com/MariaDB/server/commit/b08c420)\
  2015-07-07 15:59:21 +0400
  * Removing unused String declaration in Create\_field::Create\_field
* [Revision #e4f8cea](https://github.com/MariaDB/server/commit/e4f8cea)\
  2015-07-07 09:15:58 +0400
  * [MDEV-8419](https://jira.mariadb.org/browse/MDEV-8419) utf32: compare broken bytes as "greater than any non-broken character"
* [Revision #7332af4](https://github.com/MariaDB/server/commit/7332af4)\
  2015-07-06 20:24:14 +0300\
  \*
  * Renaming variables so that they don't shadow others (After this patch one can compile with -Wshadow and get much fewer warnings) - Changed ER(ER\_...) to ER\_THD(thd, ER\_...) when thd was known or if there was many calls to current\_thd in the same function. - Changed ER(ER\_..) to ER\_THD\_OR\_DEFAULT(current\_thd, ER...) in some places where current\_thd is not necessary defined. - Removing calls to current\_thd when we have access to thd
* [Revision #a5f4412](https://github.com/MariaDB/server/commit/a5f4412)\
  2015-07-06 11:40:56 -0400
  * Fix embedded result to reflect increased system variable's max value length.
* [Revision #3a606ba](https://github.com/MariaDB/server/commit/3a606ba)\
  2015-07-06 18:59:33 +0400
  * Fixing a bug in [MDEV-8418](https://jira.mariadb.org/browse/MDEV-8418) (utf16, utf16le) and [MDEV-8417](https://jira.mariadb.org/browse/MDEV-8417) (utf8mb4). Fixing non-BMP characters to have the same weight, as it was before [MDEV-8418](https://jira.mariadb.org/browse/MDEV-8418) and [MDEV-8417](https://jira.mariadb.org/browse/MDEV-8417).
* [Revision #b2e324a](https://github.com/MariaDB/server/commit/b2e324a)\
  2015-07-06 15:50:56 +0400
  * [MDEV-8416](https://jira.mariadb.org/browse/MDEV-8416) ucs2: compare broken bytes as "greater than any non-broken character" [MDEV-8418](https://jira.mariadb.org/browse/MDEV-8418) utf16: compare broken bytes as "greater than any non-broken character"
* [Revision #35d8ac3](https://github.com/MariaDB/server/commit/35d8ac3)\
  2015-07-06 10:47:39 +0400
  * [MDEV-8417](https://jira.mariadb.org/browse/MDEV-8417) utf8mb4: compare broken bytes as "greater than any non-broken character"
* [Revision #8d4d185](https://github.com/MariaDB/server/commit/8d4d185)\
  2015-07-05 12:40:16 +0300
  * Simple optimization and removal of compiler warnings
* [Revision #86377d0](https://github.com/MariaDB/server/commit/86377d0)\
  2015-07-05 12:39:46 +0300
  * Fixes done while working on [MDEV-4119](https://jira.mariadb.org/browse/MDEV-4119):
* [Revision #7ab7f53](https://github.com/MariaDB/server/commit/7ab7f53)\
  2015-07-03 19:08:18 +0400
  * Fixing a typo in the previous commit.
* [Revision #fff30e2](https://github.com/MariaDB/server/commit/fff30e2)\
  2015-07-03 18:40:04 +0400
  * Adding UTF8 related macros to reduce duplicate code.
* [Revision #aeb8d71](https://github.com/MariaDB/server/commit/aeb8d71)\
  2015-07-03 17:30:15 +0400
  * Removing unused code in ctype-utf8.c
* [Revision #9ad8ff6](https://github.com/MariaDB/server/commit/9ad8ff6)\
  2015-07-03 17:24:16 +0400
  * [MDEV-8415](https://jira.mariadb.org/browse/MDEV-8415) utf8: compare broken bytes as "greater than any non-broken character"
* [Revision #95d07ee](https://github.com/MariaDB/server/commit/95d07ee)\
  2015-07-03 10:33:17 +0400
  * [MDEV-8215](https://jira.mariadb.org/browse/MDEV-8215) Asian MB3 charsets: compare broken bytes as "greater than any non-broken character"
* [Revision #302bf7c](https://github.com/MariaDB/server/commit/302bf7c)\
  2015-07-02 13:33:08 +0300
  * Tabular ANALYZE must get its data from execution tracker
* [Revision #28a8ba0](https://github.com/MariaDB/server/commit/28a8ba0)\
  2015-07-02 12:00:25 +0300
  * Fix test failure seen on P7/P8 innodb-encrypt-tables update/validate function used incorrect type.
* [Revision #64424f9](https://github.com/MariaDB/server/commit/64424f9)\
  2015-07-02 10:24:02 +0300
  * Update test results
* [Revision #f0ce848](https://github.com/MariaDB/server/commit/f0ce848)\
  2015-07-01 22:52:59 -0400
  * Adjust result files to reflect increased system variable's max value length.
* [Revision #06913d0](https://github.com/MariaDB/server/commit/06913d0)\
  2015-07-02 04:12:21 +0900
  * Update Mroonga to the latest version on 2015-07-02T04:12:21+0900
* [Revision #0319304](https://github.com/MariaDB/server/commit/0319304)\
  2015-07-01 20:11:43 +0300
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #9d2aa2b](https://github.com/MariaDB/server/commit/9d2aa2b)\
  2015-07-01 20:03:29 +0300
  * [MDEV-7811](https://jira.mariadb.org/browse/MDEV-7811): EXPLAIN/ANALYZE FORMAT=JSON should show subquery cache
* [Revision #447416d](https://github.com/MariaDB/server/commit/447416d)\
  2015-07-01 16:23:22 +0300
  * [MDEV-8406](https://jira.mariadb.org/browse/MDEV-8406): Test failure on encryption.innodb-page\_encryption\_log\_encryption in P7/P8
* [Revision #93198fe](https://github.com/MariaDB/server/commit/93198fe)\
  2015-07-01 16:22:41 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Update test results to accound for binlog\_row\_image variable.
* [Revision #f35386d](https://github.com/MariaDB/server/commit/f35386d)\
  2015-07-01 15:37:52 +0400
  * Checking in range\_mrr\_icp.result forgotten in the previous patch.
* [Revision #92627e7](https://github.com/MariaDB/server/commit/92627e7)\
  2015-07-01 10:20:16 +0300
  * Add show warnings to test to find out the reason for create failure.
* [Revision #c6aee27](https://github.com/MariaDB/server/commit/c6aee27)\
  2015-03-25 18:27:10 +0100
  * [MDEV-7811](https://jira.mariadb.org/browse/MDEV-7811): EXPLAIN/ANALYZE FORMAT=JSON should show subquery cache
* [Revision #498a264](https://github.com/MariaDB/server/commit/498a264)\
  2015-06-30 19:51:09 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Update test results to accound for binlog\_row\_image variable.
* [Revision #84cefe2](https://github.com/MariaDB/server/commit/84cefe2)\
  2015-06-30 09:16:09 +0300
  * [MDEV-8396](https://jira.mariadb.org/browse/MDEV-8396): InnoDB: Assertion failure in file fil0crypt.cc line 2052
* [Revision #d1307bd](https://github.com/MariaDB/server/commit/d1307bd)\
  2015-06-30 08:34:31 +0300
  * [MDEV-8395](https://jira.mariadb.org/browse/MDEV-8395): InnoDB: Assertion failure in file fil0pagecompress.cc line 539 (SIGFPE)
* [Revision #1a3321b](https://github.com/MariaDB/server/commit/1a3321b)\
  2015-06-30 14:42:46 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Added basic tests for binlog\_row\_image using minimal and noblob values
* [Revision #4d856e3](https://github.com/MariaDB/server/commit/4d856e3)\
  2015-06-30 14:30:38 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Added tests for binlog\_row\_image using noblobs switch
* [Revision #d817267](https://github.com/MariaDB/server/commit/d817267)\
  2015-05-29 17:19:53 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Change replication event loop to account for empty events
* [Revision #5095507](https://github.com/MariaDB/server/commit/5095507)\
  2015-04-14 15:05:14 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Fixed Assertion Error, when receiving an empty event
* [Revision #ca27672](https://github.com/MariaDB/server/commit/ca27672)\
  2015-04-06 17:25:52 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Fixed Update\_rows\_log\_event to correctly apply update log events
* [Revision #8a1b7c9](https://github.com/MariaDB/server/commit/8a1b7c9)\
  2015-04-02 23:14:49 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Removed unnecesary bitmap in binlog\_write\_row
* [Revision #8bd5301](https://github.com/MariaDB/server/commit/8bd5301)\
  2015-04-02 23:03:30 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Add binlog writing according to columns
* [Revision #edff3f3](https://github.com/MariaDB/server/commit/edff3f3)\
  2015-04-02 20:46:21 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Update Update, Delete and Write row log event
* [Revision #724d5ae](https://github.com/MariaDB/server/commit/724d5ae)\
  2015-04-02 20:25:22 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Update binlog\_prepare\_pending\_rows\_events to use comparison function
* [Revision #a7d181a](https://github.com/MariaDB/server/commit/a7d181a)\
  2015-04-02 19:31:51 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Added a bitmap compare function for binlog\_row\_image
* [Revision #c096cae](https://github.com/MariaDB/server/commit/c096cae)\
  2015-04-02 19:22:41 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Removed unneded code from rpl\_injector
* [Revision #e53ad95](https://github.com/MariaDB/server/commit/e53ad95)\
  2015-04-02 19:09:40 +0300
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Added mark\_columns\_per\_bitmap\_row\_image
* [Revision #b9d1d34](https://github.com/MariaDB/server/commit/b9d1d34)\
  2015-03-21 20:44:53 +0200
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Added test suite for binlog\_row\_image sys var
* [Revision #3ed519f](https://github.com/MariaDB/server/commit/3ed519f)\
  2015-03-21 20:43:24 +0200
  * \[[MDEV-6877](https://jira.mariadb.org/browse/MDEV-6877)] Added binlog\_row\_image system variable
* [Revision #768620e](https://github.com/MariaDB/server/commit/768620e)\
  2015-06-30 12:56:31 +0400
  * [MDEV-8189](https://jira.mariadb.org/browse/MDEV-8189) field<>const and const<>field are not symmetric
* [Revision #1b2f912](https://github.com/MariaDB/server/commit/1b2f912)\
  2015-06-29 17:28:50 -0400
  * Increase field value max length to 2048 to avoid truncation of wsrep\_provider\_options' value. Also increase the max value length for SYSTEM\_VARIABLES schema table.
* [Revision #7923c0c](https://github.com/MariaDB/server/commit/7923c0c)\
  2015-06-29 20:03:57 +0300
  * Fix test failure where the environment was not fully restored.
* [Revision #79af0b3](https://github.com/MariaDB/server/commit/79af0b3)\
  2015-06-29 14:10:37 +0300
  * [MDEV-8393](https://jira.mariadb.org/browse/MDEV-8393): InnoDB: Assertion failure in file fil0crypt.cc line 2109
* [Revision #4fac626](https://github.com/MariaDB/server/commit/4fac626)\
  2015-06-29 12:48:42 +0300
  * [MDEV-8390](https://jira.mariadb.org/browse/MDEV-8390): innodb.innodb-flush-changed-page-bitmaps crashes
* [Revision #08fa60e](https://github.com/MariaDB/server/commit/08fa60e)\
  2015-06-29 12:06:00 +0400
  * [MDEV-8382](https://jira.mariadb.org/browse/MDEV-8382) - Processlist returns random numbers in Time column
* [Revision #a0f5f40](https://github.com/MariaDB/server/commit/a0f5f40)\
  2015-06-25 14:21:16 +0400
  * [MDEV-8339](https://jira.mariadb.org/browse/MDEV-8339) - Server crash during table cache eviction
* [Revision #0865e3d](https://github.com/MariaDB/server/commit/0865e3d)\
  2015-06-24 14:58:17 +0400
  * [MDEV-7792](https://jira.mariadb.org/browse/MDEV-7792) - SQL Parsing Error - UNION AND ORDER BY WITH JOIN
* [Revision #ad9b326](https://github.com/MariaDB/server/commit/ad9b326)\
  2015-06-29 08:49:58 +0300
  * [MDEV-8391](https://jira.mariadb.org/browse/MDEV-8391): encryption.innodb-page\_encryption\_compression fails
* [Revision #7567b9f](https://github.com/MariaDB/server/commit/7567b9f)\
  2015-06-28 18:51:40 +0200
  * update tests to pass
* [Revision #4d4f2ed](https://github.com/MariaDB/server/commit/4d4f2ed)\
  2015-06-28 18:23:15 +0400
  * Moving Item\_bool\_func::add\_key\_fields\_optimize\_op() to Item\_bool\_func2. It's now needed outside of Item\_bool\_func2 any more.
* [Revision #e04f6e7](https://github.com/MariaDB/server/commit/e04f6e7)\
  2015-06-28 15:23:33 +0200
  * Merge branch 'bb-10.1-serg' into 10.1
* [Revision #ee0237f](https://github.com/MariaDB/server/commit/ee0237f)\
  2015-06-28 14:29:51 +0400
  * [MDEV-8330](https://jira.mariadb.org/browse/MDEV-8330) Get rid of Item\_func::select\_optimize() and Item\_func::optimize\_type
* [Revision #26162c7](https://github.com/MariaDB/server/commit/26162c7)\
  2015-06-28 09:03:13 +0200
  * rename `{sys_vars,sql_plugin_services}.h -> *.ic`
* [Revision #55b96d2](https://github.com/MariaDB/server/commit/55b96d2)\
  2015-06-28 08:51:53 +0200
  * bump the VERSION to 10.1.6 and related changes
* [Revision #d1a1156](https://github.com/MariaDB/server/commit/d1a1156)\
  2015-06-27 20:38:05 +0200
  * cleanup: safer versions of PSI no-op macros
* [Revision #6589926](https://github.com/MariaDB/server/commit/6589926)\
  2015-06-27 20:35:26 +0200
  * Merge tag 'mariadb-10.0.20' into 10.1
* [Revision #fe7e334](https://github.com/MariaDB/server/commit/fe7e334)\
  2015-06-26 23:11:26 +0200
  * cleanup: remove unused function argument
* [Revision #c583360](https://github.com/MariaDB/server/commit/c583360)\
  2015-06-26 23:06:06 +0200
  * unittest: encrypted temporary IO\_CACHE
* [Revision #31eed47](https://github.com/MariaDB/server/commit/31eed47)\
  2015-06-25 13:05:46 +0200
  * cleanup: use WRITE\_CACHE for view frm files
* [Revision #1ce71c8](https://github.com/MariaDB/server/commit/1ce71c8)\
  2015-06-19 20:58:26 +0200
  * [MDEV-7832](https://jira.mariadb.org/browse/MDEV-7832) Add status variables to track CREATE TEMPORARY TABLE and DROP TEMPORARY TABLE
* [Revision #e24caa7](https://github.com/MariaDB/server/commit/e24caa7)\
  2015-06-19 20:57:39 +0200
  * small cleanup
* [Revision #c47acc2](https://github.com/MariaDB/server/commit/c47acc2)\
  2015-06-19 20:47:09 +0200
  * remove unused function and array
* [Revision #794a895](https://github.com/MariaDB/server/commit/794a895)\
  2015-06-19 19:46:12 +0200
  * simplify CREATE TEMPORARY TABLE parser rule
* [Revision #bfabaf6](https://github.com/MariaDB/server/commit/bfabaf6)\
  2015-06-22 17:17:03 +0200
  * Deinitialize plugins in the reverse plugin\_type\_initialization\_order
* [Revision #ff7a1ff](https://github.com/MariaDB/server/commit/ff7a1ff)\
  2015-06-21 06:34:58 +0200
  * fix printf format string
* [Revision #8036ad0](https://github.com/MariaDB/server/commit/8036ad0)\
  2015-06-21 06:33:45 +0200
  * misc encryption tests fixes
* [Revision #627c6e8](https://github.com/MariaDB/server/commit/627c6e8)\
  2015-06-19 18:10:47 +0200
  * [MDEV-8298](https://jira.mariadb.org/browse/MDEV-8298) sys\_vars.all\_vars fails in -DWITH\_WSREP=OFF build
* [Revision #e7620ce](https://github.com/MariaDB/server/commit/e7620ce)\
  2015-06-19 18:05:10 +0200
  * [MDEV-8281](https://jira.mariadb.org/browse/MDEV-8281) aes\_decrypt crashes in block\_crypt()
* [Revision #e20be69](https://github.com/MariaDB/server/commit/e20be69)\
  2015-06-27 09:40:42 +0200
  * update test results and 32-bit rdiffs
* [Revision #55d8ee5](https://github.com/MariaDB/server/commit/55d8ee5)\
  2015-06-26 22:49:49 +0400
  * [MDEV-8239](https://jira.mariadb.org/browse/MDEV-8239) Reverse spatial operations OP(const, field) do not get optimized Moving Item\_func\_spatial\_rel from Item\_bool\_func to Item\_bool\_func2. to make OP(const,field) use indexes.
  * MBR functions supported OP(const,field) optimization in 10.0, but were inintentionally broken in an earlier 10.1 change that introduced a common parent for Item\_func\_spatial\_mbr\_rel and Item\_func\_spatial\_precise\_rel.
  * Precise functions never supported optimization for OP(const,field). Now both MBR and precise functions support OP(const,field) optimization.
* [Revision #cb5f32e](https://github.com/MariaDB/server/commit/cb5f32e)\
  2015-06-26 20:00:24 +0400
  * Moving Item\_func\_xor out of Item\_bool\_func2, as it does not need any of the optimizer related functionality.
* [Revision #40e5ace](https://github.com/MariaDB/server/commit/40e5ace)\
  2015-06-26 17:46:34 +0400
  * Removing Item\_int\_func::sargable. Adding virtual implementations of count\_sargable\_conds() instead for Item\_func\_in, Item\_func\_null\_predicate, Item\_bool\_func2. There other Item\_int\_func descendants that used to set "sargable" to true (Item\_func\_between, Item\_equal) already have their own implementation of count\_sargable\_conds(). There is no sense to have two parallel coding models for the same thing.
* [Revision #4364118](https://github.com/MariaDB/server/commit/4364118)\
  2015-06-26 15:42:49 +0400
  * Moving ST\_RELATE() implementation out of Item\_func\_precise\_spatial\_rel, adding a separte class Item\_func\_spatial\_relate for ST\_RELATE(). This is a preparatory patch for: [MDEV-8239](https://jira.mariadb.org/browse/MDEV-8239) Reverse spatial operations OP(const, field) do not get optimized
* [Revision #4f828a1](https://github.com/MariaDB/server/commit/4f828a1)\
  2015-06-26 13:40:28 +0400
  * [MDEV-8214](https://jira.mariadb.org/browse/MDEV-8214) Asian MB2 charsets: compare broken bytes as "greater than any non-broken character"
* [Revision #d535728](https://github.com/MariaDB/server/commit/d535728)\
  2015-06-26 11:42:09 +0300
  * [MDEV-8219](https://jira.mariadb.org/browse/MDEV-8219): enforce\_storage\_engine cannot be set globally
* [Revision #a4b0063](https://github.com/MariaDB/server/commit/a4b0063)\
  2015-06-26 10:58:51 +0400
  * [MDEV-8256](https://jira.mariadb.org/browse/MDEV-8256) A part of a ROW comparison is erroneously optimized away Item\_func\_eq's created during conversion of a ROW equality to a conjunction of scalar equalities did not set cmp\_context for its arguments properly, so some of these created Item\_func\_eq could be later erroneously eliminated.
* [Revision #4a7afdd](https://github.com/MariaDB/server/commit/4a7afdd)\
  2015-06-26 10:18:34 +0400
  * [MDEV-8373](https://jira.mariadb.org/browse/MDEV-8373) Zero date can be inserted in strict no-zero mode through CREATE TABLE AS SELECT timestamp\_field
* [Revision #115904c](https://github.com/MariaDB/server/commit/115904c)\
  2015-06-26 10:16:51 +0400
  * [MDEV-7824](https://jira.mariadb.org/browse/MDEV-7824) \[Bug #68041] Zero date can be inserted in strict no-zero mode through a default value
* [Revision #874df50](https://github.com/MariaDB/server/commit/874df50)\
  2015-06-26 08:33:14 +0300
  * Fix failing test case.
* [Revision #9111ab7](https://github.com/MariaDB/server/commit/9111ab7)\
  2015-06-25 13:16:27 +0500
  * GIS-related tests started to fail as some related functions don't return NULL-s anymore, and actually they're not BOOLEAN. Fixed.
* [Revision #42bc08b](https://github.com/MariaDB/server/commit/42bc08b)\
  2015-06-25 12:51:32 +0400
  * [MDEV-8229](https://jira.mariadb.org/browse/MDEV-8229) GROUP\_MIN\_MAX is erroneously applied for BETWEEN in some cases
* [Revision #1f4a89b](https://github.com/MariaDB/server/commit/1f4a89b)\
  2015-06-24 23:38:04 -0400
  * Do print SST log messages.
* [Revision #5659608](https://github.com/MariaDB/server/commit/5659608)\
  2015-06-24 17:18:12 +0200
  * Merge [MDEV-8354](https://jira.mariadb.org/browse/MDEV-8354) into 10.1
* [Revision #d43df4a](https://github.com/MariaDB/server/commit/d43df4a)\
  2015-06-23 15:06:23 +0500
  * These functions can never return NULL.
* [Revision #b7ff2f1](https://github.com/MariaDB/server/commit/b7ff2f1)\
  2015-06-23 14:36:24 +0300
  * [MDEV-7472](https://jira.mariadb.org/browse/MDEV-7472): Implementation of user statements for handling the xtradb changed page bitmaps
* [Revision #d3b7eb7](https://github.com/MariaDB/server/commit/d3b7eb7)\
  2015-06-23 11:57:05 +0500
  * [MDEV-7528](https://jira.mariadb.org/browse/MDEV-7528) GIS: Functions return NULL instead of specified -1 for NULL arguments. The behaviour required by the standard seems too weird to expect.
* [Revision #3e4126e](https://github.com/MariaDB/server/commit/3e4126e)\
  2015-06-23 11:30:39 +0500
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #9b57b21](https://github.com/MariaDB/server/commit/9b57b21)\
  2015-05-21 13:08:46 +0400
  * [MDEV-8199](https://jira.mariadb.org/browse/MDEV-8199) - first\_breadth\_first\_tab() takes 0.07% in OLTP RO
* [Revision #45f41b5](https://github.com/MariaDB/server/commit/45f41b5)\
  2015-05-21 12:30:41 +0400
  * [MDEV-8199](https://jira.mariadb.org/browse/MDEV-8199) - first\_breadth\_first\_tab() takes 0.07% in OLTP RO
* [Revision #84568c2](https://github.com/MariaDB/server/commit/84568c2)\
  2015-05-20 12:04:32 +0400
  * [MDEV-8030](https://jira.mariadb.org/browse/MDEV-8030) - Apc\_target::disable() locks mutex twice
* [Revision #fb3e312](https://github.com/MariaDB/server/commit/fb3e312)\
  2015-06-22 23:33:35 +0500
  * [MDEV-7925](https://jira.mariadb.org/browse/MDEV-7925) Inconsistent behavior of ST\_Touches with a POINT as one of arguments. Some cases of the feature's borders were treated incorrectly.
* [Revision #0357791](https://github.com/MariaDB/server/commit/0357791)\
  2015-06-22 08:44:46 +0300
  * [MDEV-8280](https://jira.mariadb.org/browse/MDEV-8280): crash in 'show global status' with --skip-grant-tables
* [Revision #cbb8b2d](https://github.com/MariaDB/server/commit/cbb8b2d)\
  2015-06-20 05:01:16 +0300
  * More testcases.
* [Revision #ebe2bd7](https://github.com/MariaDB/server/commit/ebe2bd7)\
  2015-06-20 04:20:18 +0300
  * [MDEV-7836](https://jira.mariadb.org/browse/MDEV-7836): ANALYZE FORMAT=JSON should provide info about GROUP BY
* [Revision #f33173d](https://github.com/MariaDB/server/commit/f33173d)\
  2015-06-19 21:31:16 +0300
  * [MDEV-8282](https://jira.mariadb.org/browse/MDEV-8282): crash in filesort() with simple ordered delete
* [Revision #12d9fe1](https://github.com/MariaDB/server/commit/12d9fe1)\
  2015-06-17 13:09:22 +0400
  * [MDEV-7956](https://jira.mariadb.org/browse/MDEV-7956) - handler::rebind\_psi() takes 0.07% in OLTP RO
* [Revision #8f603bc](https://github.com/MariaDB/server/commit/8f603bc)\
  2015-06-17 18:55:38 +0400
  * [MDEV-7952](https://jira.mariadb.org/browse/MDEV-7952) - clock\_gettime() takes 0.24% in OLTP RO
* [Revision #2bc6e29](https://github.com/MariaDB/server/commit/2bc6e29)\
  2015-06-19 15:04:58 +0400
  * [MDEV-7943](https://jira.mariadb.org/browse/MDEV-7943) - pthread\_getspecific() takes 0.76% in OLTP RO
* [Revision #360176f](https://github.com/MariaDB/server/commit/360176f)\
  2015-06-18 18:01:56 +0400
  * [MDEV-7943](https://jira.mariadb.org/browse/MDEV-7943) - pthread\_getspecific() takes 0.76% in OLTP RO
* [Revision #b85e5ef](https://github.com/MariaDB/server/commit/b85e5ef)\
  2015-04-28 15:20:48 +0400
  * [MDEV-7943](https://jira.mariadb.org/browse/MDEV-7943) - pthread\_getspecific() takes 0.76% in OLTP RO
* [Revision #2b253ed](https://github.com/MariaDB/server/commit/2b253ed)\
  2015-06-17 12:37:19 +0400
  * [MDEV-8324](https://jira.mariadb.org/browse/MDEV-8324) - MariaDB fails to build with performance schema disabled
* [Revision #366cda4](https://github.com/MariaDB/server/commit/366cda4)\
  2015-06-18 23:27:44 +0400
  * Adding "const" qualifier into a few methods in Field.
* [Revision #091f677](https://github.com/MariaDB/server/commit/091f677)\
  2015-06-18 22:16:44 +0400
  * Removing duplicate code: Adding a protected method Field\_temporal\_with\_date::validate\_for\_get\_date() and reusing it in a few places.
* [Revision #f5ddffd](https://github.com/MariaDB/server/commit/f5ddffd)\
  2015-06-18 19:58:57 +0300
  * [MDEV-8156](https://jira.mariadb.org/browse/MDEV-8156): Assertion failure in file log0crypt.cc line 220 on server restart
* [Revision #6050ab6](https://github.com/MariaDB/server/commit/6050ab6)\
  2015-06-18 09:59:09 -0400
  * [MDEV-6829](https://jira.mariadb.org/browse/MDEV-6829) : SELinux/AppArmor policies for Galera server
* [Revision #e2a59eb](https://github.com/MariaDB/server/commit/e2a59eb)\
  2015-06-18 14:52:17 +0300
  * Make dbug\_print\_item() print conditions in siccint form
* [Revision #caf4291](https://github.com/MariaDB/server/commit/caf4291)\
  2015-06-18 14:51:50 +0300
  * Remove garbage comment
* [Revision #eb2c170](https://github.com/MariaDB/server/commit/eb2c170)\
  2015-06-18 08:38:33 +0300
  * [MDEV-8303](https://jira.mariadb.org/browse/MDEV-8303); Dumping buffer pool noisy in the logs.
* [Revision #b94eaff](https://github.com/MariaDB/server/commit/b94eaff)\
  2015-06-17 09:12:26 +0300
  * [MDEV-8310](https://jira.mariadb.org/browse/MDEV-8310): Encryption bogus message still in 10.1.5
* [Revision #6a92fa4](https://github.com/MariaDB/server/commit/6a92fa4)\
  2015-06-15 08:28:04 +0200
  * Merge branch 'mdev8294' into 10.1
* [Revision #b1b0db2](https://github.com/MariaDB/server/commit/b1b0db2)\
  2015-06-10 12:42:18 +0200
  * Merge [MDEV-8294](https://jira.mariadb.org/browse/MDEV-8294) into 10.1
* [Revision #f965cae](https://github.com/MariaDB/server/commit/f965cae)\
  2015-06-05 11:43:05 -0400
  * [MDEV-7110](https://jira.mariadb.org/browse/MDEV-7110) : Add missing MySQL variable log\_bin\_basename and log\_bin\_index
* [Revision #c94789c](https://github.com/MariaDB/server/commit/c94789c)\
  2015-06-09 15:35:25 +0400
  * Adding a test for: [MDEV-8167](https://jira.mariadb.org/browse/MDEV-8167) XOR returns bad results for an indexed column The bug itself was earlier fixed by one of the earlier changes.
* [Revision #b092871](https://github.com/MariaDB/server/commit/b092871)\
  2015-06-09 15:02:53 +0400
  * Adding a test for "[MDEV-6973](https://jira.mariadb.org/browse/MDEV-6973) XOR aggregates argument collations". The bug itself was earlier fixed by this patch:
* [Revision #70b82ef](https://github.com/MariaDB/server/commit/70b82ef)\
  2015-06-08 19:36:35 +0300
  * [MDEV-8273](https://jira.mariadb.org/browse/MDEV-8273): InnoDB: Assertion failure in file fil0pagecompress.cc line 532
* [Revision #4a6a61c](https://github.com/MariaDB/server/commit/4a6a61c)\
  2015-06-08 08:09:33 +0300
  * [MDEV-8268](https://jira.mariadb.org/browse/MDEV-8268): InnoDB: Assertion failure in file buf0buf.cc line 5842 failing assertion ut\_a(free\_slot != NULL);
* [Revision #d7f3d88](https://github.com/MariaDB/server/commit/d7f3d88)\
  2015-06-05 08:41:10 +0300
  * [MDEV-8272](https://jira.mariadb.org/browse/MDEV-8272): Encryption performance: Reduce the number of unused memcpy's
* [Revision #f744b2a](https://github.com/MariaDB/server/commit/f744b2a)\
  2015-06-09 12:08:46 +0400
  * [MDEV-8283](https://jira.mariadb.org/browse/MDEV-8283) crash in get\_mm\_leaf with xor on binary col
* [Revision #93fc04f](https://github.com/MariaDB/server/commit/93fc04f)\
  2015-06-06 00:32:27 +0300
  * [MDEV-6995](https://jira.mariadb.org/browse/MDEV-6995): EXPLAIN JSON and ORDER BY, GROUP BY, etc
* [Revision #f7002c0](https://github.com/MariaDB/server/commit/f7002c0)\
  2015-06-03 13:10:18 +0300
  * [MDEV-8250](https://jira.mariadb.org/browse/MDEV-8250): InnoDB: Page compressed tables are not compressed and compressed+encrypted tables cause crash

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
