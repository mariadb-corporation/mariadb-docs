# MariaDB 10.0.8 Changelog

[Download](https://downloads.mariadb.org/mariadb/10.0.8) |[Release Notes](../../old-releases/10.0/10.0.8.md) |**Changelog** |[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 10 Feb 2014

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.8.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3994](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3994)\
  Thu 2014-02-06 21:58:38 +0100
  * skip performance\_schema also in spider/bg suite (as it was done for spider suite)
* [Revision #3993](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3993)\
  Thu 2014-02-06 21:26:00 +0100
  * update failing test to match recently updated result file
* [Revision #3992](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3992) \[merge]\
  Thu 2014-02-06 16:38:40 +0100
  * merge with 10.0-monty
  * [Revision #3978.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3978.1.4)\
    Thu 2014-02-06 16:14:09 +0200
    * Fixed errors and warnings found by buildbot
  * [Revision #3978.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3978.1.3)\
    Wed 2014-02-05 21:36:16 +0200
    * [MDEV-5602](https://jira.mariadb.org/browse/MDEV-5602): CREATE OR REPLACE obtains stricter locks than the connection had before
  * [Revision #3978.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3978.1.2)\
    Wed 2014-02-05 19:25:18 +0200
    * Marked some very slow tokudb test with `--big_test`
  * [Revision #3978.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3978.1.1) \[merge]\
    Wed 2014-02-05 19:23:11 +0200
    * Automatic merge
    * [Revision #3961.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3961.1.7)\
      Wed 2014-02-05 19:01:59 +0200
      * Replication changes for CREATE OR REPLACE TABLE
      * CREATE TABLE is by default executed on the slave as CREATE OR REPLACE
      * DROP TABLE is by default executed on the slave as DROP TABLE IF NOT EXISTS
    * [Revision #3961.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3961.1.6)\
      Fri 2014-01-31 12:06:28 +0200
      * Fixes for CREATE\_OR\_REPLACE
        * [MDEV-5587](https://jira.mariadb.org/browse/MDEV-5587) Server crashes in Locked\_tables\_list::restore\_lock on CREATE OR REPLACE .. SELECT under LOCK
        * [MDEV-5586](https://jira.mariadb.org/browse/MDEV-5586) Assertion \`\`share->tdc.all\_tables.is\_empty() || remove\_type != TDC\_RT\_REMOVE\_ALL'\` fails in tdc\_remove\_table
        * [MDEV-5588](https://jira.mariadb.org/browse/MDEV-5588) Strange error on CREATE OR REPLACE table over an existing view
    * [Revision #3961.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3961.1.5)\
      Wed 2014-01-29 15:41:10 +0200
      * Fixed compiler warnings Made stopping of slave more robust Fixed tokudb test cases that gave different results between runs Speed up some slow tokudb tests by adding begin ... commit
    * [Revision #3961.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3961.1.4)\
      Wed 2014-01-29 15:37:17 +0200
      * Implementation of [MDEV-5491](https://jira.mariadb.org/browse/MDEV-5491): CREATE OR REPLACE TABLE
    * [Revision #3961.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3961.1.3)\
      Thu 2014-01-09 22:01:12 +0200
      * Cleanups:
        * Updated help for mysql-test-run
        * Added OQGraph to all cmake error output regarding OQGraph to make it easier to spot problems
        * Suppressed warning messages from OQGraph
        * Added test for version\_malloc\_library variable
    * [Revision #3961.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3961.1.2)\
      Thu 2014-01-02 11:19:19 +0200
      * Fixes to get valgrind to work with jemalloc
        * Added MALLOC\_LIBRARY variable to hold name of malloc library
        * Back ported valgrind related fixes from jemalloc 3.4.1 to the included jemalloc 3.3.1
        * Renamed bitmap\_init() and bitmap\_free() to my\_bitmap\_init() and my\_bitmap\_free() to avoid clash with jemalloc 3.4.1
        * Use option `--soname-synonyms=somalloc=NON` to valgrind when using jemalloc
        * Show version related variables in `mysqld --help` Added SHOW\_VALUE\_IN\_HELP marker
    * [Revision #3961.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3961.1.1)\
      Fri 2013-12-27 13:00:14 +0200
      * Increased back\_log to 150, but not more than max\_connections.
        * This was done to get better performance when doing a lot of connections. Ensure that thread\_cache\_size is not larger than max\_connections (trivial optimizations). Fixed that the `--host_cache_size=#` startup option works
* [Revision #3991](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3991)\
  Thu 2014-02-06 16:28:05 +0100
  * fix tests for solaris - different errno numbers and/or different errno messages
* [Revision #3990](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3990)\
  Thu 2014-02-06 16:27:55 +0100
  * fix tests to cleanup after themselves
* [Revision #3989](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3989)\
  Thu 2014-02-06 16:27:44 +0100
  * another TLS valgrind suppression
* [Revision #3988](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3988)\
  Thu 2014-02-06 16:27:23 +0100
  * fix the fix and update test results for [MDEV-4439](https://jira.mariadb.org/browse/MDEV-4439)
* [Revision #3987](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3987)\
  Thu 2014-02-06 16:27:05 +0100
  * [MDEV-4439](https://jira.mariadb.org/browse/MDEV-4439) ALTER TABLE .. \[ADD|DROP] FOREIGN KEY IF \[NOT] EXISTS does not work if constraint name is not used. Patches for server and the Innodb engine. Server is fixed so it does nothing if no indexes left to alter. Innodb parser is fixed so it looks for the IF \[NOT] EXISTS option in a string. Another change is that it uses the index name for the internal dictionary. Prior to that it only used the CONSTRAINT name for it.
* [Revision #3986](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3986)\
  Thu 2014-02-06 16:25:40 +0100
  * [MDEV-5499](https://jira.mariadb.org/browse/MDEV-5499) install\_spider.sql tries to create tables with DEFAULT clause for TEXT columns
* [Revision #3985](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3985)\
  Thu 2014-02-06 16:25:18 +0100
  * mtr: allow nested plugin suites to be defaults too
* [Revision #3984](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984) \[merge]\
  Thu 2014-02-06 14:21:50 +0400
  * Merge 10.0-connect -> 10.0
  * [Revision #3966.2.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3966.2.3) \[merge]\
    Wed 2014-02-05 13:36:17 +0400
    * Merge 10.0->10.0-connect
  * [Revision #3966.2.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3966.2.2)\
    Mon 2014-02-03 23:07:49 +0100
    * Fix a few GCC errors an warnings
  * [Revision #3966.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3966.2.1)\
    Mon 2014-02-03 16:14:13 +0100
    * This is a major update of CONNECT that goes from version 1.1 to 1.2
      * Implement a first support of the ALTER TABLE command. This fixes [MDEV-5440](https://jira.mariadb.org/browse/MDEV-5440) but does much more than only that. See the details of how ALTER is supported in the new documentation and also in [MDEV-5440](https://jira.mariadb.org/browse/MDEV-5440) comment. This is done principally by implementing for CONNECT the virtual function check\_if\_supported\_inplace\_alter.
* [Revision #3983](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3983)\
  Wed 2014-02-05 18:18:51 +0100
  * revert bugfix for [MDEV-5295](https://jira.mariadb.org/browse/MDEV-5295) deb upgrade 5.5 to 10.0.6 does not work it didn't help, instead it only broke upgrades even more
* [Revision #3982](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3982)\
  Wed 2014-02-05 17:27:41 +0100
  * more solaris fixes. xtradb and spider.
* [Revision #3981](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3981)\
  Wed 2014-02-05 17:27:32 +0100
  * fix the test to be independent from the stack size
* [Revision #3980](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3980)\
  Wed 2014-02-05 20:53:54 +0200
  * Fix of rpl\_parallel.test cleanup.
* [Revision #3979](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3979) \[merge]\
  Wed 2014-02-05 20:35:11 +0200
  * merge 10.0-base ->10.0
  * [Revision #3427.35.235](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.235) \[merge]\
    Wed 2014-02-05 16:20:37 +0200
    * merge 5.5->10.0-base
    * [Revision #3413.21.511](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.511)\
      Wed 2014-02-05 14:25:37 +0400
      * unix\_socket fails in some build environments when $USER variable appears to be unset, or when it contains 'root' even though the user does not have real root permissions
    * [Revision #3413.21.510](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.510)\
      Sat 2014-02-01 02:41:12 +0400
      * Increment the version number
    * [Revision #3413.21.509](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.509) \[merge]\
      Wed 2014-01-29 00:19:53 +0200
      * merge of [MDEV-5369](https://jira.mariadb.org/browse/MDEV-5369) (5.3->5.5)
      * [Revision #2502.567.191](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.191)\
        Tue 2014-01-28 23:23:14 +0200
        * [MDEV-5369](https://jira.mariadb.org/browse/MDEV-5369): Wrong result (0 instead of NULL) on 2nd execution of PS with LEFT JOIN, TEMPTABLE view
  * [Revision #3427.35.234](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.234)\
    Mon 2014-02-03 08:54:12 +0400
    * Upgrading the bundled PCRE to 8.34
* [Revision #3978](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3978)\
  Wed 2014-02-05 16:41:29 +0400
  * From MySQL 5.6.13 change log: Unlike MyISAM, InnoDB does not support boolean full-text searches on nonindexed columns, but this restriction was not enforced, resulting in queries that returned incorrect results. (Bug #16434374)
* [Revision #3977](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3977)\
  Wed 2014-02-05 16:39:21 +0400
  * Intentional change in logging
* [Revision #3976](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3976)\
  Wed 2014-02-05 03:51:18 +0400
  * Spider tests failed in buildbot due to the lack of memory. Turned off Performance Schema for Spider test suite
* [Revision #3975](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3975)\
  Wed 2014-02-05 03:17:39 +0400
  * [MDEV-5591](https://jira.mariadb.org/browse/MDEV-5591) Cannot build the package under Debian Wheezy
* [Revision #3974](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3974)\
  Tue 2014-02-04 19:30:29 +0100
  * harmless typo fixed
* [Revision #3973](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3973)\
  Tue 2014-02-04 19:29:58 +0100
  * ha\_xtradb.so fix for solaris, gcc 3.4.3
* [Revision #3972](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3972)\
  Tue 2014-02-04 19:08:50 +0100
  * don't link with libmysys twice (it's implied here)
* [Revision #3971](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3971)\
  Tue 2014-02-04 19:07:15 +0100
  * update result file
* [Revision #3970](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3970) \[merge]\
  Tue 2014-02-04 10:49:44 +0100
  * merge
  * [Revision #3965.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.23)\
    Mon 2014-02-03 22:28:35 +0100
    * test fixes
  * [Revision #3965.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.22)\
    Mon 2014-02-03 15:27:03 +0100
    * WEIGHT\_STRING fix: correct Item\_func\_weight\_string::eq() method
  * [Revision #3965.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.21)\
    Mon 2014-02-03 15:26:58 +0100
    * mysql 5.6 partitioning bugfix: doubly-reported error
  * [Revision #3965.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.20) \[merge]\
    Mon 2014-02-03 15:22:39 +0100
    * 10.0-base merge
    * [Revision #3427.35.233](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.233)\
      Sat 2014-02-01 00:54:28 +0100
      * make sequence and sql\_discovery suites default too
    * [Revision #3427.35.232](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.232) \[merge]\
      Sat 2014-02-01 00:54:03 +0100
      * 5.5 merge
      * [Revision #3413.21.508](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.508) \[merge]\
        Tue 2014-01-28 10:58:18 +0100
        * 5.3 merge
        * [Revision #2502.567.190](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.190) \[merge]\
          Tue 2014-01-28 10:27:52 +0100
          * 5.2 merge
          * [Revision #2502.566.61](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.61) \[merge]\
            Tue 2014-01-28 10:23:11 +0100
            * 5.1 merge
            * [Revision #2502.565.64](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.64)\
              Tue 2014-01-28 10:21:47 +0100
              * fixed a client-side overflow in mysql cli
      * [Revision #3413.21.507](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.507)\
        Tue 2014-01-28 11:12:43 +0400
        * [MDEV-5345](https://jira.mariadb.org/browse/MDEV-5345) - Deadlock between mysql\_change\_user(), SHOW VARIABLES and INSTALL PLUGIN
      * [Revision #3413.21.506](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.506) \[merge]\
        Tue 2014-01-28 13:00:50 +0400
        * merge 5.3 -> 5.5
        * [Revision #2502.567.189](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.189)\
          Tue 2014-01-28 12:25:29 +0400
          * [MDEV-5506](https://jira.mariadb.org/browse/MDEV-5506) safe\_mutex: Trying to lock unitialized mutex at safemalloc.c on server shutdown after SELECT with CONVERT\_TZ
      * [Revision #3413.21.505](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.505)\
        Mon 2014-01-27 20:50:32 +0100
        * [MDEV-5576](https://jira.mariadb.org/browse/MDEV-5576) ALTER TABLE progress report > 100%
      * [Revision #3413.21.504](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.504)\
        Mon 2014-01-27 16:58:26 +0100
        * [MDEV-4787](https://jira.mariadb.org/browse/MDEV-4787) Missing dependency to "patch" for the Debian/Ubuntu "mariadb-test" package
      * [Revision #3413.21.503](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.503)\
        Mon 2014-01-27 12:11:04 +0100
        * [MDEV-5405](https://jira.mariadb.org/browse/MDEV-5405) RQG induced crash in mi\_assign\_to\_key\_cache in safe mutex unlock
      * [Revision #3413.21.502](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.502)\
        Mon 2014-01-27 12:10:53 +0100
        * mtr: check that tests clean up debug\_sync. fix tests that didn't.
      * [Revision #3413.21.501](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.501)\
        Sun 2014-01-26 21:49:39 +0100
        * improve oqgraph boost check to filter out newer boost versions
      * [Revision #3413.21.500](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.500)\
        Sun 2014-01-26 21:49:31 +0100
        * workaround test failures in buildbot: in some VMs readline thinks that the window size is zero. ignore it.
      * [Revision #3413.21.499](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.499)\
        Sun 2014-01-26 21:49:19 +0100
        * [MDEV-5461](https://jira.mariadb.org/browse/MDEV-5461) Assertion \`\`length <= column->length'\` fails in write\_block\_record with functions in select list, GROUP BY, ORDER BY
      * [Revision #3413.21.498](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.498)\
        Sun 2014-01-26 21:49:11 +0100
        * move innodb specific test from group\_by.test to group\_by\_innodb.test
      * [Revision #3413.21.497](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.497)\
        Sun 2014-01-26 21:49:04 +0100
        * fix the test for [MDEV-5029](https://jira.mariadb.org/browse/MDEV-5029) to clean up after itself
      * [Revision #3413.21.496](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.496)\
        Sun 2014-01-26 21:48:42 +0100
        * Fix for [MDEV-5168](https://jira.mariadb.org/browse/MDEV-5168): MariaDB returns warnings for INSERT IGNORE
      * [Revision #3413.21.495](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.495)\
        Sun 2014-01-26 21:48:23 +0100
        * Fixed that setup\_natural\_join\_row\_types can safely be called twice
      * [Revision #3413.21.494](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.494)\
        Sun 2014-01-26 21:47:31 +0100
        * Fixed bug that I accidently introduced in mysql\_tzinfo\_to\_sql Added test cases
      * [Revision #3413.21.493](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.493)\
        Sun 2014-01-26 20:46:15 +0200
        * speed up tokudb tests by adding begin/commit around insert loops Marked very long running tests as big\_test
      * [Revision #3413.21.492](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.492)\
        Sat 2014-01-25 15:41:08 +0200
        * Fixed [MDEV-4970](https://jira.mariadb.org/browse/MDEV-4970): Wrong result with Aria table populated with disabled keys
      * [Revision #3413.21.491](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.491) \[merge]\
        Mon 2014-01-27 15:05:23 +0400
        * Merge 5.3 -> 5.5
        * [Revision #2502.567.188](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.188)\
          Mon 2014-01-27 13:15:40 +0400
          * [MDEV-5458](https://jira.mariadb.org/browse/MDEV-5458) RQG hits 'sql/tztime.cc:799: my\_time\_t sec\_since\_epoch(...): Assertion \`mon > 0 && mon < 13' failed.'
      * [Revision #3413.21.490](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.490) \[merge]\
        Mon 2014-01-27 13:14:00 +0400
        * Merge 5.3 -> 5.5
        * [Revision #2502.567.187](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.187)\
          Sat 2014-01-25 00:26:40 +0400
          * \[Backport to 5.3] [MDEV-5337](https://jira.mariadb.org/browse/MDEV-5337): Wrong result in [mariadb 5.5.32](../../old-releases/5.5/5.5.32.md) with ORDER BY + LIMIT when index\_condition\_pushdown=on
          * in test\_if\_skip\_sort\_order(), correct the condition under which we have the code that restores the previously pushed index condition.
        * [Revision #2502.567.186](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.186)\
          Fri 2014-01-24 16:50:39 +0400
          * [MDEV-5504](https://jira.mariadb.org/browse/MDEV-5504) Server crashes in String::length on SELECT with MONTHNAME, GROUP BY, ROLLUP
        * [Revision #2502.567.185](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.185)\
          Thu 2014-01-23 21:26:04 +0400
          * [MDEV-5368](https://jira.mariadb.org/browse/MDEV-5368): Server crashes in Item\_in\_subselect::optimize on ...
          * convert\_subq\_to\_sj() must connect child select's tables into parent select's TABLE\_LIST::next\_local chain.
          * The problem was that it took child's leaf\_tables.head() which is different. This could cause certain tables (in this bug's case, child select's non-merged semi-join) not to be present in TABLE\_LIST::next\_local chain. Which would cause non-merged semi-join not to be initialized in setup\_tables(), which would lead to NULL pointer dereference.
      * [Revision #3413.21.489](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.489) \[merge]\
        Sun 2014-01-26 16:41:15 +0200
        * merge 5.3->5.5
        * [Revision #2502.567.184](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.184) \[merge]\
          Thu 2014-01-23 12:05:10 +0200
          * merge of [MDEV-5356](https://jira.mariadb.org/browse/MDEV-5356) 5.1->5.3 (with more fixes and test suite).
          * [Revision #2502.565.63](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.63)\
            Thu 2014-01-23 11:11:01 +0200
            * [MDEV-5356](https://jira.mariadb.org/browse/MDEV-5356): Server crashes in Item\_equal::contains on 2nd execution of a PS THD::thd->activate\_stmt\_arena\_if\_needed() should be used to temporary activating statement arena instead of direct usage of THD::set\_n\_backup\_active\_arena() because possible such scenario:
              1. func1 saves current arena and activates copy1 of statement arena
              2. func2 saves copy1 of statement arena setup by func1 and activates copy2
              3. some changes made for copy 2
              4. func2 stores changed copy2 back to statenet arena and activates copy1
              5. func1 store unchanged copy1 back to statemnt arena (rewrite changed copy 2 so changes become lost) and activates arena which was before.
        * [Revision #2502.567.183](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.183) \[merge]\
          Tue 2014-01-21 09:56:12 +0100
          * 5.2 merge
          * [Revision #2502.566.60](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.60) \[merge]\
            Tue 2014-01-21 09:41:28 +0100
            * 5.1 merge
            * [Revision #2502.565.62](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.62)\
              Mon 2014-01-20 20:53:39 +0100
              * fix a warning
            * [Revision #2502.565.61](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.61)\
              Mon 2014-01-20 19:09:01 +0100
              * [MDEV-5543](https://jira.mariadb.org/browse/MDEV-5543) MyISAM repair unsafe usage of TMD files
            * [Revision #2502.565.60](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.60)\
              Fri 2013-12-20 12:35:47 +0200
              * make 5.1 compiling with modern gcc.
      * [Revision #3413.21.488](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.488) \[merge]\
        Fri 2014-01-24 23:44:52 +0400
        * Merge
        * [Revision #3413.60.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.60.1)\
          Fri 2014-01-24 23:40:48 +0400
          * [MDEV-5337](https://jira.mariadb.org/browse/MDEV-5337): Wrong result in [mariadb 5.5.32](../../old-releases/5.5/5.5.32.md) with ORDER BY + LIMIT when index\_condition\_pushdown=on
          * in test\_if\_skip\_sort\_order(), correct the condition under which we have the code that restores the previously pushed index condition.
      * [Revision #3413.21.487](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.487)\
        Fri 2014-01-24 19:44:13 +0200
        * Fixed Mageia Bug 12355: mariadb produces warning messages while loading timezone information
          * Warnings about wrong symlink messages or non-timezone files with '.tab' are now only given if run with `--verbose`
          * Added long option handling
          * Added `--help`, `--verbose` and `--version` options
      * [Revision #3413.21.486](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.486)\
        Fri 2014-01-24 14:50:18 +0200
        * Fix for [MDEV-5531](https://jira.mariadb.org/browse/MDEV-5531): double call procedure in one session
          * hard shutdown the server Main fix was to not cache derivied tables as they may be temporary tables that are deleted before the next query. This was a bit tricky as Item\_field::fix\_fields depended on cached\_tables to be set to resolve some columns.
      * [Revision #3413.21.485](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.485)\
        Fri 2014-01-24 14:30:19 +0200
        * Fixed failures in tokudb test cases
      * [Revision #3413.21.484](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.484)\
        Fri 2014-01-24 06:07:22 +0400
        * [MDEV-5419](https://jira.mariadb.org/browse/MDEV-5419) no audit events for warnings converted to errors in the strict mode. small fix in the `--replace_regex` template.
      * [Revision #3413.21.483](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.483)\
        Thu 2014-01-23 22:21:02 +0400
        * [MDEV-5419](https://jira.mariadb.org/browse/MDEV-5419) no audit events for warnings converted to errors in the strict mode. Plugins get error notifications only when my\_message\_sql() is called. But errors are launched with THD::raise\_condition() calls in other places. These are push\_warning(), implementations of SIGNAL and RESIGNAL commands. So it makes sence to notify plugins there in THD::raise\_condition().
      * [Revision #3413.21.482](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.482) \[merge]\
        Thu 2014-01-23 21:12:37 +0400
        * Merge
        * [Revision #3413.59.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.59.1)\
          Thu 2014-01-23 15:41:51 +0400
          * [MDEV-5368](https://jira.mariadb.org/browse/MDEV-5368): Server crashes in Item\_in\_subselect::optimize on ...
          * convert\_subq\_to\_sj() must connect child select's tables into parent select's TABLE\_LIST::next\_local chain.
          * The problem was that it took child's leaf\_tables.head() which is different. This could cause certain tables (in this bug's case, child select's non-merged semi-join) not to be present in TABLE\_LIST::next\_local chain. Which would cause non-merged semi-join not to be initialized in setup\_tables(), which would lead to NULL pointer dereference.
      * [Revision #3413.21.481](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.481)\
        Thu 2014-01-23 11:04:59 +0100
        * [MDEV-5406](https://jira.mariadb.org/browse/MDEV-5406) add index to an innodb table with a uniqueness violation crashes mysqld
      * [Revision #3413.21.480](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.480)\
        Thu 2014-01-23 00:03:05 +0100
        * [MDEV-5421](https://jira.mariadb.org/browse/MDEV-5421) Assertion \`\`! is\_set()'\` fails on INSERT IGNORE when a table has no partition for a value
      * [Revision #3413.21.479](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.479)\
        Thu 2014-01-23 00:02:52 +0100
        * [MDEV-5550](https://jira.mariadb.org/browse/MDEV-5550) Invalid cmake variable in mysql-test/CMakeLists.txt
      * [Revision #3413.21.478](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.478)\
        Thu 2014-01-23 00:02:37 +0100
        * Change our INSTALL\_DEBUG\_SYMBOLS cmake function to be less picky and support MySQL CMakeLists.txt files
      * [Revision #3413.21.477](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.477)\
        Thu 2014-01-23 00:02:22 +0100
        * update debian patches to match the current code state
      * [Revision #3413.21.476](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.476)\
        Thu 2014-01-23 00:02:08 +0100
        * fix XtraDB to compile on Windows
      * [Revision #3413.21.475](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.475)\
        Wed 2014-01-22 23:59:21 +0100
        * update test results, broken by [MDEV-5547](https://jira.mariadb.org/browse/MDEV-5547) fix
      * [Revision #3413.21.474](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.474) \[merge]\
        Wed 2014-01-22 15:35:42 +0100
        * Percona-Server-5.5.35-rel33.0.tar.gz
        * [Revision #0.48.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.48.1)\
          Wed 2014-01-22 10:03:32 +0100
          * Percona-Server-5.5.35-rel33.0.tar.gz
      * [Revision #3413.21.473](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.473) \[merge]\
        Wed 2014-01-22 15:29:36 +0100
        * MySQL-5.5.35 merge
      * [Revision #3413.21.472](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.472)\
        Tue 2014-01-21 17:20:51 +0100
        * clarify plugin-load usage in tokudb.cnf file
      * [Revision #3413.21.471](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.471)\
        Tue 2014-01-21 17:20:44 +0100
        * remove an unused error message
      * [Revision #3413.21.470](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.470)\
        Wed 2014-01-22 15:16:57 +0200
        * Fix for [MDEV-5547](https://jira.mariadb.org/browse/MDEV-5547): Bad error message when moving very old .frm files to [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md). mysql\_upgrade `--help` now also prints out `--default` options and variable values. mysql\_upgrade now prints permission errors. mysql\_upgrade doesn't print some non essential info if `--silent` is used. Added handler error message about incompatible versions Fixed that mysqlbug and mysql\_install\_db have the executable flag set. Removed executable flag for some non executable files. Changed in mysql\_install\_db askmonty.org to mariadb.com. Ensured that all client executables prints `--default` options the same way. Allow REPAIR ... USE\_FRM for old .frm files if the are still compatible. Extended shown error for storage engine messages.
      * [Revision #3413.21.469](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.469)\
        Tue 2014-01-21 17:27:36 +0400
        * [MDEV-4974](https://jira.mariadb.org/browse/MDEV-4974): memory leak in 5.5.32-MariaDB-1wheezy-log
          * When a JOIN has both "optimization tabs" (JOIN\_TABs used to read the base tables and do the join operation) and also has "execution tabs" (a JOIN\_TAB that is to produce result set that is sent to the client), do not forget to call JOIN\_TAB::cleanup() for the execution JOIN\_TAB.
      * [Revision #3413.21.468](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.468) \[merge]\
        Wed 2014-01-15 16:07:50 +0200
        * Merge 5.3->5.5
        * [Revision #2502.567.182](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.182)\
          Mon 2014-01-13 21:30:42 +0200
          * [MDEV-5515](https://jira.mariadb.org/browse/MDEV-5515): 2nd execution of a prepared statement returns wrong results
        * [Revision #2502.567.181](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.181)\
          Wed 2013-12-18 15:59:51 +0200
          * [MDEV-5414](https://jira.mariadb.org/browse/MDEV-5414): RAND() in a subselect : different behavior in MariaDB and MySQL
      * [Revision #3413.21.467](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.467)\
        Sun 2014-01-05 15:21:58 +0200
        * Don't writing entries to slave log about binlog\_checksum not existing on master if log\_warnings is <=1.
      * [Revision #3413.21.466](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.466)\
        Thu 2014-01-02 15:51:02 +0200
        * Fixed [MDEV-5424](https://jira.mariadb.org/browse/MDEV-5424): SELECT using ORDER BY DESC and LIMIT produces unexpected results (InnoDB/XtraDB) This only happend when using an ORDER BY on a primary key part, where all other key parts where constant. Remove of duplicated expressions in ORDER BY (as the old code did this in some strange cases)
      * [Revision #3413.21.465](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.465)\
        Mon 2013-12-30 20:30:29 +0400
        * [MDEV-5349](https://jira.mariadb.org/browse/MDEV-5349): Test main.subselect\_sj\_jcl6 fails sporadically due to insufficient ordering
          * Add `--sorted_result` to the query
      * [Revision #3413.21.464](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.464)\
        Tue 2013-12-17 17:26:54 +0100
        * [MDEV-5396](https://jira.mariadb.org/browse/MDEV-5396) Assertion \`\`Handlerton: r==0 '\` failed (errno=0) on EXPLAIN with TokuDB tables
    * [Revision #3427.35.231](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.231)\
      Fri 2014-01-31 13:52:29 +0400
      * Adding a new command into CMakeLists.txt: SET(CMAKE\_INCLUDE\_DIRECTORIES\_PROJECT\_BEFORE ON) to find header files from the bundled libraries (jemalloc, yassl, readline, pcre, etc) before the ones installed in the system.
    * [Revision #3427.35.230](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.230) \[merge]\
      Tue 2014-01-07 11:57:03 +0100
      * Merge into 10.0-base: [MDEV-5363](https://jira.mariadb.org/browse/MDEV-5363), make parallel replication waits killable.
      * [Revision #3427.41.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.41.9)\
        Mon 2014-01-06 16:05:52 +0100
        * [MDEV-5363](https://jira.mariadb.org/browse/MDEV-5363): Make parallel replication waits killable
      * [Revision #3427.41.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.41.8)\
        Fri 2014-01-03 12:20:53 +0100
        * [MDEV-5363](https://jira.mariadb.org/browse/MDEV-5363): Make parallel replication waits killable
      * [Revision #3427.41.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.41.7)\
        Wed 2013-12-18 16:26:22 +0100
        * [MDEV-5363](https://jira.mariadb.org/browse/MDEV-5363): Make parallel replication waits killable
      * [Revision #3427.41.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.41.6)\
        Tue 2013-12-17 13:24:51 +0100
        * [MDEV-5363](https://jira.mariadb.org/browse/MDEV-5363): Make parallel replication waits killable
      * [Revision #3427.41.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.41.5)\
        Tue 2013-12-17 10:50:34 +0100
        * [MDEV-5363](https://jira.mariadb.org/browse/MDEV-5363): Make parallel replication waits killable
      * [Revision #3427.41.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.41.4)\
        Mon 2013-12-16 13:48:32 +0100
        * [MDEV-5363](https://jira.mariadb.org/browse/MDEV-5363): Make parallel replication waits killable
      * [Revision #3427.41.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.41.3)\
        Fri 2013-12-13 14:26:51 +0100
        * [MDEV-5363](https://jira.mariadb.org/browse/MDEV-5363): Make parallel replication waits killable
      * [Revision #3427.41.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.41.2)\
        Fri 2013-12-06 13:28:23 +0100
        * [MDEV-5363](https://jira.mariadb.org/browse/MDEV-5363): Make parallel replication waits killable
      * [Revision #3427.41.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.41.1)\
        Thu 2013-12-05 14:36:09 +0100
        * [MDEV-5363](https://jira.mariadb.org/browse/MDEV-5363): Make parallel replication waits killable
  * [Revision #3965.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.19)\
    Sun 2014-02-02 10:09:05 +0100
    * fixes:
      * roles.grant\_proxy-5526 test for `--embedded`
      * gcc warning in Connect
  * [Revision #3965.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.18)\
    Sun 2014-02-02 10:06:29 +0100
    * [MySQL Worklog #5522](https://dev.mysql.com/worklog/task/?id=5522) - InnoDB transportable tablespaces. Cleanups:
      * remove unused HA\_EXTRA\_EXPORT (can be added later if needed, e.g. for Aria)
      * clarify the meaning of HA\_CAN\_EXPORT
      * make all engines that support EXPORT to announce it
      * reduce code duplication
  * [Revision #3965.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.17)\
    Sun 2014-02-02 10:00:36 +0100
    * Merge the server part of [MySQL Worklog #5522](https://dev.mysql.com/worklog/task/?id=5522) - InnoDB transportable tablespaces. Syntax. Server support. Test cases.
    * InnoDB bugfixes:
      * don't mess around with system sprintf's, always use my\_error() for errors.
      * don't use InnoDB internal error codes where OS error codes are expected.
      * don't say "file not found", when it was.
  * [Revision #3965.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.16) \[merge]\
    Sat 2014-02-01 14:08:34 +0100
    * upgrade sphinx to 2.1.5
    * [Revision #0.47.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.47.2)\
      Sat 2014-02-01 10:56:56 +0100
      * sphinxse 2.1.5-release
  * [Revision #3965.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.15) \[merge]\
    Sat 2014-02-01 10:53:41 +0100
    * null-merge with the new sphinxse-merge bzr tree
    * [Revision #0.47.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.47.1)\
      Sat 2014-02-01 10:40:58 +0100
      * sphinxse 0.9.9
  * [Revision #3965.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.14)\
    Sat 2014-02-01 09:34:07 +0100
    * [MDEV-5549](https://jira.mariadb.org/browse/MDEV-5549) Wrong row counter in found\_rows() result
  * [Revision #3965.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.13)\
    Sat 2014-02-01 09:33:26 +0100
    * [MDEV-5574](https://jira.mariadb.org/browse/MDEV-5574) Set AUTO\_INCREMENT below max value of column.
    * Update InnoDB to 5.6.14
    * Apply MySQL-5.6 hack for MySQL Bug#16434374
    * Move Aria-only HA\_RTREE\_INDEX from my\_base.h to maria\_def.h (breaks an assert in InnoDB)
    * Fix InnoDB memory leak
  * [Revision #3965.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.12)\
    Sat 2014-02-01 09:32:59 +0100
    * [MDEV-5544](https://jira.mariadb.org/browse/MDEV-5544) Custom errors (generated from storage engine) not getting returned by mariadb
  * [Revision #3965.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.11)\
    Wed 2014-01-29 16:10:53 +0100
    * [MDEV-5295](https://jira.mariadb.org/browse/MDEV-5295) deb upgrade 5.5 to 10.0.6 does not work
  * [Revision #3965.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.10)\
    Wed 2014-01-29 11:00:06 +0100
    * [MDEV-5525](https://jira.mariadb.org/browse/MDEV-5525) Assertion \`\`status == 0'\` fails on creating user after granting it role admin option
  * [Revision #3965.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.9)\
    Wed 2014-01-29 00:05:24 +0100
    * [MDEV-5526](https://jira.mariadb.org/browse/MDEV-5526) Assertion \`\`proxied\_user->host.length'\` fails on GRANT PROXY ON
  * [Revision #3965.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.8)\
    Tue 2014-01-28 21:11:56 +0100
    * [MDEV-5523](https://jira.mariadb.org/browse/MDEV-5523) Server crashes on DROP USER
  * [Revision #3965.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.7)\
    Tue 2014-01-28 21:02:17 +0100
    * [MDEV-5521](https://jira.mariadb.org/browse/MDEV-5521) SET ROLE as prepared statement crashes the server
  * [Revision #3965.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.6)\
    Tue 2014-01-28 21:01:21 +0100
    * [MDEV-5520](https://jira.mariadb.org/browse/MDEV-5520) Connection lost on wrong CREATE ROLE
  * [Revision #3965.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.5)\
    Tue 2014-01-28 19:44:19 +0100
    * [MDEV-5493](https://jira.mariadb.org/browse/MDEV-5493) ha\_sphinx.so is not included into Ubuntu deb packages (included into Debian)
  * [Revision #3965.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.4)\
    Sat 2014-01-25 14:52:20 +0100
    * add all csv extensions to the ha\_tina\_exts\[] array
  * [Revision #3965.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.3)\
    Wed 2013-12-25 21:21:47 +0100
    * minor cleanup
  * [Revision #3965.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.2)\
    Wed 2013-12-18 15:39:09 +0200
    * Fix for: [MDEV-5221](https://jira.mariadb.org/browse/MDEV-5221): User auto-creation does not work upon GRANT
  * [Revision #3965.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965.1.1)\
    Wed 2013-12-25 10:13:15 +0100
    * mtr: print a detailed warning on a uninit assignment in the \[ENV] group spider suites: #varname is a valid syntax for a variable name, don't use it for comments
* [Revision #3969](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3969) \[merge]\
  Tue 2014-02-04 13:34:11 +0400
  * Merge
  * [Revision #3966.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3966.1.1)\
    Tue 2014-02-04 13:27:10 +0400
    * [MDEV-5606](https://jira.mariadb.org/browse/MDEV-5606): range optimizer: "x < y" is sargable, while "y > x" is not Port to mariadb-1.0 the following fix from mysql-5.6:
* [Revision #3968](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3968)\
  Tue 2014-02-04 12:05:00 +0400
  * Removing "#include \<sys/timeb.h>" from my\_global.h, which has been removed earlier, but somehow got into the sources again.
* [Revision #3967](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3967)\
  Mon 2014-02-03 23:29:22 +0400
  * [MDEV-5450](https://jira.mariadb.org/browse/MDEV-5450) Assertion \`\`cached\_field\_ type == MYSQL\_TYPE\_STRING || ltime.time\_type == MYSQL\_TIMESTAMP\_NONE || mysql\_type\_to\_time\_type(cached\_field\_type) == ltime.time\_type'\` fails with IF, ISNULL, ADDDATE
* [Revision #3966](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3966) \[merge]\
  Mon 2014-02-03 09:13:03 +0400
  * Merg 10.0-connect -> 10.0
  * [Revision #3913.1.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.27) \[merge]\
    Fri 2014-01-31 14:21:15 +0400
    * merge 10.0 -> 10.0-connect
  * [Revision #3913.1.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.26)\
    Tue 2013-12-31 13:08:29 +0100
    * Fix bug [MDEV-5486](https://jira.mariadb.org/browse/MDEV-5486) (fail to create or drop a table dbn.tbn when no default database)
  * [Revision #3913.1.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.25)\
    Sat 2013-12-28 16:56:51 +0100
    * Fix variables used uninitialized
  * [Revision #3913.1.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.24)\
    Sat 2013-12-28 15:46:49 +0100
    * Add the DECIMAL data type (TYPE\_DECIM) Change the variable name of the DOUBLE type from TYPE\_FLOAT to TYPE\_DOUBLE Change some names to reflect ODBC version 3. This affects some variable names, function names and catalog table column names. Qualifier -> Catalog Owner (Creator) -> Schema Length -> Precision Prec -> Scale
  * [Revision #3913.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.23)\
    Wed 2013-12-25 18:24:37 +0400
    * Adding tests for TABLE\_TYPE=ODBC with Oracle.
* [Revision #3965](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3965) \[merge]\
  Tue 2014-01-21 14:07:00 +0400
  * Merge
  * [Revision #3962.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.1.1)\
    Tue 2014-01-21 14:02:56 +0400
    * [MDEV-5426](https://jira.mariadb.org/browse/MDEV-5426): Assertion \`\`toku\_ft\_needed\_unlocked(src\_h)'\` failed (errno=11) ...
      * the problem was caused by EXPLAIN INSERT SELECT. For that statement, the code would call select\_insert::prepare2(), which would call handler->ha\_start\_bulk\_insert(). The corresponding handler->end\_bulk\_insert() call is made from select\_insert::send\_eof or select\_insert::abort\_result\_set which are never called for EXPLAIN INSERT SELECT.
      * Fixed by re-using approach of mysql-5.6: don't call ha\_start\_bulk\_insert() if we are in EXPLAIN.
* [Revision #3964](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3964)\
  Mon 2014-01-20 16:36:57 +0400
  * [MDEV-4816](https://jira.mariadb.org/browse/MDEV-4816): rpl.rpl\_trunc\_temp fails in 10.0-serg Undo the previous band-aid fix in psergey@askmonty.org-20130802141209-4dqfvx2db8acxwbl. Kristian has made a proper fix, which uses a different approach.
* [Revision #3963](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3963)\
  Tue 2014-01-14 19:00:38 +0100
  * Fix for [MDEV-4117](https://jira.mariadb.org/browse/MDEV-4117) @@global.relay\_log\_purge not per-master, conflicts between different masters in multisource replication
* [Revision #3962](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962)\
  Sat 2013-12-28 20:36:57 +0400
  * Increment the version number

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
