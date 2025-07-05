# MariaDB 10.0.1 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.1) |[Release Notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-1001-release-notes.md) |**Changelog** |[Overview of 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)

**Release date:** 06 Feb 2013

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-1001-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #3501](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3501) \[merge]\
  Mon 2013-02-04 17:30:39 +0200
  * merge
  * [Revision #3427.1.68](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.68)\
    Mon 2013-02-04 17:25:10 +0200
    * [MDEV-3873](https://jira.mariadb.org/browse/MDEV-3873): post-merge fix.
  * [Revision #3427.1.67](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.67)\
    Mon 2013-02-04 11:47:57 +0100
    * missing cast added
* [Revision #3500](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3500)\
  Mon 2013-02-04 10:38:31 +0400
  * Skip cassandra\_qcache.test if there is no Cassandra cluster running.
* [Revision #3499](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3499) \[merge]\
  Mon 2013-02-04 10:15:52 +0400
  * Merge fix for [MDEV-3997](https://jira.mariadb.org/browse/MDEV-3997).
  * [Revision #3497.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3497.1.2)\
    Mon 2013-02-04 10:14:20 +0400
    * [MDEV-3997](https://jira.mariadb.org/browse/MDEV-3997): Querying a Cassandra table on a server with query cache enabled is likely to cause problems - Disable query cache for Cassandra tables.
  * [Revision #3497.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3497.1.1)\
    Mon 2013-02-04 09:22:29 +0400
    * Fix mysql-test/suite/plugins/suite.pm to correctly check if Cassandra cluster is running.
* [Revision #3498](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3498) \[merge]\
  Mon 2013-02-04 12:04:29 +0200
  * merge
  * [Revision #3427.1.66](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.66)\
    Mon 2013-02-04 11:31:05 +0200
    * [MDEV-4091](https://jira.mariadb.org/browse/MDEV-4091): Dynamic columns C functions should be included in libmysqlclient
  * [Revision #3427.1.65](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.65)\
    Thu 2013-01-31 11:29:58 +0100
    * [MDEV-4121](https://jira.mariadb.org/browse/MDEV-4121): binlog.binlog\_row\_binlog sporadic test failure
    * Add a wait for binlog checkpoint to avoid thread scheduling giving different binlog order at random.
* [Revision #3497](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3497)\
  Sat 2013-02-02 12:52:44 +0100
  * remove "invisible sysvars" oxymoron
* [Revision #3496](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3496)\
  Thu 2013-01-31 21:32:21 +0100
  * fix for a valgrind builds. my\_alloca() cannot have MY\_THREAD\_SPECIFIC, because can be used outside of the THD context.
* [Revision #3495](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3495)\
  Thu 2013-01-31 15:51:26 +0100
  * avoid mtr errors for `--plugin-add=EXAMPLE=$HA_EXAMPLE_SO` when no ha\_example.so is built
* [Revision #3494](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3494)\
  Thu 2013-01-31 13:19:53 +0100
  * skip cassandra.test unless cassandra is running
* [Revision #3493](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3493) \[merge]\
  Thu 2013-01-31 09:48:19 +0100
  * 10.0-base merge
  * [Revision #3427.1.64](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.64)\
    Wed 2013-01-30 22:33:25 +0100
    * don't disable the cassandra engine by default
  * [Revision #3427.1.63](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.63)\
    Wed 2013-01-30 15:11:36 +0100
    * [MDEV-3984](https://jira.mariadb.org/browse/MDEV-3984): Double free of Master\_info \* when CHANGE MASTER fails.
    * When CHANGE MASTER fails, it may or may not have already added the\
      Master\_info to the index. Implement logic that properly handles removal and\
      freeing in both cases.
  * [Revision #3427.1.62](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.62)\
    Tue 2013-01-29 19:14:43 +0100
    * move cassandra-related code from cmake/cpack\_rpm.cmake to storage/cassandra/CMakeLists.txt
  * [Revision #3427.1.61](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.61)\
    Tue 2013-01-29 17:42:51 +0100
    * buildbot fixes for storage/cassandra/CMakeLists.txt
  * [Revision #3427.1.60](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.60) \[merge]\
    Tue 2013-01-29 15:10:47 +0100
    * 5.5 merge
  * [Revision #3427.1.59](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.59)\
    Mon 2013-01-28 15:06:36 +0100
    * my\_alloca() when it's mapped to malloc() works most certainly MY\_THREAD\_SPECIFIC
  * [Revision #3427.1.58](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.58)\
    Thu 2013-01-24 17:52:25 +0100
    * fix ha\_cassandra to compile
  * [Revision #3427.1.57](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.57)\
    Thu 2013-01-24 17:24:21 +0100
    * workaround for incorrectly (?) generated code on gcc 4.2.4-1ubuntu4 with -fPIE (which is added automatically because of DEB\_BUILD\_HARDENING=1)
  * [Revision #3427.1.56](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.56)\
    Thu 2013-01-24 17:24:03 +0100
    * race conditions in show\_explain.test
  * [Revision #3427.1.55](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.55)\
    Wed 2013-01-23 19:17:13 +0100
    * main.partition\_myisam crashes in embedded. long error message with %M fails the assertion in my\_vsnprintf
  * [Revision #3427.1.54](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.54)\
    Wed 2013-01-23 16:24:04 +0100
    * fix the failing federated.federated\_innodb test: update all start\_bulk\_insert() methods to the new signature.
  * [Revision #3427.1.53](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.53)\
    Wed 2013-01-23 16:23:50 +0100
    * 32-bit fix: first cast the value to a signed type, then subtract
  * [Revision #3427.1.52](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.52)\
    Wed 2013-01-23 16:22:27 +0100
    * test suite fixes
  * [Revision #3427.1.51](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.51)\
    Wed 2013-01-23 16:20:39 +0100
    * cleanup: \* don't use 'myf flags', when 'my\_bool is\_thread\_specific' is meant \* call set\_malloc\_size\_cb() for embedded too \* warn in safemalloc if the memory is freed by a wrong thread
  * [Revision #3427.1.50](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.50)\
    Wed 2013-01-23 16:19:37 +0100
    * cleanup: \* remove unused mysql\_option \* don't allocate 5GB of memory in the mtr tests \* restore the behavior in dynamic\_column\_offset\_byte(), put the ifdef correctly \* prefer attribute((unused)) to #ifdef \* prefer UNINIT\_VAR to LINT\_INIT \* make most Warning\_info users blissfully unaware of the postponed initialization \* use my\_offsetof instead of offsetof where the compiler thinks the latter is incorrect
  * [Revision #3427.1.49](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.49)\
    Wed 2013-01-23 16:18:53 +0100
    * cleanup: remove unused init\_dynamic\_array and init\_dynamic\_array2 symbols, as only my\_init\_dynamic\_array and my\_init\_dynamic\_array2 are used everywhere. fix ha\_cassandra to compile.
  * [Revision #3427.1.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.48)\
    Wed 2013-01-23 16:18:09 +0100
    * cleanup: use MYF() for mysys flags
  * [Revision #3427.1.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.47)\
    Wed 2013-01-23 16:16:14 +0100
    * [MDEV-4011](https://jira.mariadb.org/browse/MDEV-4011) Added per thread memory counting and usage Base code and idea from a patch from by plinux at Taobao.
    * The idea is that we mark all memory that are thread specific with\
      MY\_THREAD\_SPECIFIC. Memory counting is done per thread in the\
      my\_malloc\_size\_cb\_func callback function from my\_malloc(). There are plenty of\
      new asserts to ensure that for a debug server the counting is correct.
    * Information\_schema.processlist gets two new columns: MEMORY\_USED and\
      EXAMINED\_ROWS.
      * The later is there mainly to show how query is progressing.
    * The following changes in interfaces was needed to get this to work:
      * init\_alloc\_root() amd init\_sql\_alloc() has extra option so that one can mark memory with MY\_THREAD\_SPECIFIC
      * One now have to use alloc\_root\_set\_min\_malloc() to set min memory to be allocated by alloc\_root()
      * my\_init\_dynamic\_array() has extra option so that one can mark memory with MY\_THREAD\_SPECIFIC
      * my\_net\_init() has extra option so that one can mark memory with MY\_THREAD\_SPECIFIC
      * Added flag for hash\_init() so that one can mark hash table to be thread specific.
      * Added flags to init\_tree() so that one can mark tree to be thread specific.
      * Removed with\_delete option to init\_tree(). Now one should instead use MY\_TREE\_WITH\_DELETE\_FLAG.
      * Added flag to Warning\_info::Warning\_info() if the structure should be fully initialized.
      * String elements can now be marked as thread specific.
      * Internal HEAP tables are now marking it's memory as MY\_THREAD\_SPECIFIC.
      * Changed type of myf from int to ulong, as this is always a set of bit flags.
    * Other things:
      * Removed calls to net\_end() and thd
      * cleanup() as these are now done in THD()
      * We now also show EXAMINED\_ROWS in SHOW PROCESSLIST
      * Added new variable 'memory\_used'
      * Fixed bug where kill\_threads\_for\_user() was using the wrong mem\_root to allocate memory.
      * Removed calls to the obsoleted function init\_dynamic\_array()
      * Use set\_current\_thd() instead of my\_pthread\_setspecific\_ptr(THR\_THD,...)
  * [Revision #3427.1.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.46)\
    Wed 2013-01-23 15:52:59 +0100
    * [MDEV-3931](https://jira.mariadb.org/browse/MDEV-3931) Cassandra SE packaging
    * Added autodetection for thrift library and includes Added Cassandra Storage Engine rpm
  * [Revision #3427.1.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.45)\
    Mon 2013-01-21 10:06:03 +0100
    * Fix uninitialised variable in binlog group commit (probably not reachable code).
    * Fix test failure when $vardir does not allow executing programs.
  * [Revision #3427.1.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.44)\
    Wed 2013-01-16 16:12:50 +0100
    * Fix missing #include
  * [Revision #3427.1.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.43) \[merge]\
    Wed 2013-01-16 16:55:37 +0400
    * [MDEV-3990](https://jira.mariadb.org/browse/MDEV-3990): engine tests went out of sync with current MariaDB code
    * [Revision #3427.12.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.12.1)\
      Sun 2013-01-13 17:01:34 +0400
      * [MDEV-3990](https://jira.mariadb.org/browse/MDEV-3990): engine tests went out of sync with current MariaDB code
      * Reasons:
        * alter\_tablespace.rdiff:
        * tc\_rename\_error.result:
          * from monty@askmonty.org-20120529213755-876ptdhhaj0t7l8r
          * (Added text for errno in error messages)
        * insert\_time.result:
          * from sergii@pisem.net-20120908101555-37w00eyfrd9noc06
          * ([MDEV-457](https://jira.mariadb.org/browse/MDEV-457) - Inconsistent data truncation)
        * misc.result:
          * from igor@askmonty.org-20130109033433-5awdv0w6vbpigltw
          * ([MDEV-3806](https://jira.mariadb.org/browse/MDEV-3806)/mwl248 - Engine independent statistics)
        * tbl\_opt\_row\_format.rdiff:
          * from monty@askmonty.org-20120706161018-y5teinbuqpchle2m
          * (Fixed wrong error codes)
        * vcol.rdiff:
          * sergii@pisem.net-20121217100039-ikj1820nrku7p6d5
          * (simplify the handler api)
  * [Revision #3427.1.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.42)\
    Mon 2013-01-14 13:36:28 +0200
    * Compiler warning fixed.
  * [Revision #3427.1.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.41) \[merge]\
    Sun 2013-01-13 02:11:22 -0800
    * Merged the fix for bug [MDEV-4019](https://jira.mariadb.org/browse/MDEV-4019).
    * [Revision #3413.22.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.14)\
      Sun 2013-01-13 00:40:38 -0800
      * Fixed bug [MDEV-4019](https://jira.mariadb.org/browse/MDEV-4019). The bug could cause a crash when several connections needed persistent statistics for the same table.
      * Also added a missing call of set\_statistics\_for\_table() in the code of the function mysql\_update.
  * [Revision #3427.1.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.40)\
    Fri 2013-01-11 14:12:59 +0200
    * Windows compiler warnings fix.
  * [Revision #3427.1.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.39)\
    Fri 2013-01-11 13:27:19 +0200
    * Fix windows compiler warnings.
  * [Revision #3427.1.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.38)\
    Thu 2013-01-10 19:47:07 +0200
    * fixed crossplatform double values representation.
  * [Revision #3427.1.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.37)\
    Thu 2013-01-10 17:10:58 +0400
    * [MDEV-3982](https://jira.mariadb.org/browse/MDEV-3982): show\_explain.test fails, times out or crashes Backport the fix from 10.0 tree
    *
      * The problem was that thd\_killed() may be called by innodb from an internal innodb thread. - Fixed by not processing APC requests when we're not in the thread that owns the APC target.
  * [Revision #3427.1.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.36)\
    Thu 2013-01-10 17:12:31 +0200
    * 32 bit systems warnings fixed.
  * [Revision #3427.1.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.35)\
    Thu 2013-01-10 13:47:47 +0200
    * append\_identifier() declaration fixed.
  * [Revision #3427.1.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.34)\
    Thu 2013-01-10 11:39:43 +0200
    * fix cassandra SE test to be working in case of not built cassandra.
  * [Revision #3427.1.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.33)\
    Thu 2013-01-10 01:01:15 +0200
    * Make cassandra not built by default
  * [Revision #3427.1.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.32) \[merge]\
    Thu 2013-01-10 00:58:36 +0200
    * Cassandra SE merge
    * [Revision #3427.11.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.11.6)\
      Thu 2013-01-10 00:07:44 +0200
      * Make cassandra module and do not load it by default.
    * [Revision #3427.11.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.11.5)\
      Wed 2013-01-09 22:32:21 +0200
      * fixed feature counter.
    * [Revision #3427.11.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.11.4)\
      Wed 2013-01-09 22:24:37 +0200
      * The library interface fixed.
    * [Revision #3427.11.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.11.3)\
      Wed 2013-01-09 08:10:48 +0200
      * [MDEV-4005](https://jira.mariadb.org/browse/MDEV-4005) fix.
      * Field matching fixed. DBUG\_ASSERT fixed.
    * [Revision #3427.11.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.11.2)\
      Mon 2012-12-24 08:36:22 +0400
      * Post-merge fixes: - update ha\_cassandra::start\_bulk\_insert() definition to match those in class handler.
    * [Revision #3427.11.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.11.1) \[merge]\
      Sun 2012-12-23 23:37:11 +0200
      * pre-merge
      * [Revision #3413.25.54](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.54)\
        Sun 2012-12-23 22:17:22 +0200
        * Post-post review fixes.
      * [Revision #3413.25.53](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.53)\
        Sun 2012-12-23 20:57:54 +0200
        * backport to 5.5 dyncol changes and names support
      * [Revision #3413.25.52](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.52)\
        Thu 2012-12-20 14:30:09 +0400
        * Cassandra Storage Engine: Address review feedback part #3 - Cleanup ha\_cassandra::store\_lock() - Remove dummy ha\_cassandra::delete\_table() - Add HA\_TABLE\_SCAN\_ON\_INDEX to table\_flags()
      * [Revision #3413.25.51](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.51)\
        Thu 2012-12-20 14:15:56 +0400
        * Cassandra Storage Engine: Address review feedback part 2 - Register counters directly in the array passed to maria\_declare\_plugin. As a consequence, FLUSH TABLES will reset the counters. - Update test results accordingly.
  * [Revision #3413.25.50](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.50)\
    Thu 2012-12-20 13:10:09 +0400
    * Cassandra Storage Engine: - Partially address review feedback. - Update cassandra.test result - make cassandra.test timezone-agnostic
  * [Revision #3413.25.49](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.49)\
    Sun 2012-09-30 07:58:01 +0300
    * Check of deleting whole dynamic columns.
  * [Revision #3413.25.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.48)\
    Sat 2012-09-29 16:01:24 +0300
    * Fix of [MDEV-565](https://jira.mariadb.org/browse/MDEV-565): Server crashes in ha\_cassandra::write\_row on inserting NULL into a dynamic column
    * Fixed incorrect initialization of variable which caused freeing memory by random address in case of error.
  * [Revision #3413.25.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.47)\
    Fri 2012-09-28 15:29:59 +0400
    * Include cassandra storage engine in tarballs
  * [Revision #3413.25.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.46)\
    Fri 2012-09-28 14:02:59 +0400
    * Fix compile: expect Thrift where it is at buildbot.
  * [Revision #3413.25.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.45)\
    Fri 2012-09-28 14:01:52 +0400
    * Fix compile warnings
  * [Revision #3413.25.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.44)\
    Fri 2012-09-28 15:30:49 +0300
    * Ending spaces removed.
  * [Revision #3413.25.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.43)\
    Fri 2012-09-28 15:27:16 +0300
    * [MDEV-506](https://jira.mariadb.org/browse/MDEV-506) Cassandra dynamic columns access
  * [Revision #3413.25.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.42)\
    Fri 2012-09-28 14:01:17 +0300
    * [MDEV-377](https://jira.mariadb.org/browse/MDEV-377) Name support for dynamic columns
    * [MDEV-127](https://jira.mariadb.org/browse/MDEV-127) Optimization of memory allocation
    * [MDEV-483](https://jira.mariadb.org/browse/MDEV-483) Make column\_check function which cheсks dynamic columns integrit JSON conversion function
  * [Revision #3413.25.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.41)\
    Thu 2012-09-27 16:08:28 +0400
    * Cassandra SE: lazy connections
      * Don't connect right away in ha\_cassandra::open. If we do this, it becomes impossible to do SHOW CREATE TABLE when the server is not present.
      * Note: CREATE TABLE still requires that connection is present, as it needs to check whether the specified DDL can be used with Cassandra. We could delay that check also, but then one would not be able to find out about errors in table DDL until they do a SELECT.
  * [Revision #3413.25.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.40)\
    Thu 2012-09-27 11:59:14 +0400
    * Cassandra SE
      * Support UPDATE statements
      * Follow what CQL does: don't show deleted rows (they show up as rows without any columns in reads)
  * [Revision #3413.25.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.39)\
    Wed 2012-09-26 19:02:12 +0400
    * Update testcases
    * Better error messages.
  * [Revision #3413.25.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.38)\
    Wed 2012-09-26 14:57:45 +0400
    * Cassandra SE:
      * Add a test for ALTER TABLE
  * [Revision #3413.25.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.37)\
    Wed 2012-09-26 14:13:03 +0400
    * Cassandra SE: Add capability to retry failed API calls
      * Add capability to retry calls that have failed with UnavailableException or \[Cassandra's] TimedOutException.
      * We don't retry for Thrift errors yet, although could easily do, now.
  * [Revision #3413.25.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.36)\
    Tue 2012-09-25 16:20:19 +0400
    * Cassandra SE: more datatypes support
      * Support mapping Cassandra's timestamp to INT64
      * Support mapping Cassadnra's decimal to VARBINARY.
  * [Revision #3413.25.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.35)\
    Mon 2012-09-24 20:58:26 +0400
    * Cassandra SE: varint datatype support:
      * allow only VARBINARY(n), all other types can get meaningless data after conversions
      * more comments
  * [Revision #3413.25.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.34)\
    Mon 2012-09-24 19:15:12 +0400
    * Cassandra SE
      * Add support for Cassandra's 'varint' datatype, mappable to VARBINARY.
  * [Revision #3413.25.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.33)\
    Sat 2012-09-22 23:30:29 +0400
    * Cassandra SE: make consistency settings user-settable.
  * [Revision #3413.25.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.32)\
    Thu 2012-09-20 14:22:36 +0400
    * Cassandra SE:
      * Added @@cassandra\_thrift\_host global variable.
  * [Revision #3413.25.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.31)\
    Sun 2012-09-16 12:22:21 +0400
    * Cassandra SE:
      * added option thrift\_port which allows to specify which port to connect to
      * not adding username/password - it turns out, there are no authentication schemes in stock cassandra distribution.
  * [Revision #3413.25.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.30)\
    Fri 2012-09-14 09:25:42 +0400
    * [MDEV-530](https://jira.mariadb.org/browse/MDEV-530): Cassandra SE: Locking is incorrect
      * Use more permissive locking.
  * [Revision #3413.25.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.29)\
    Fri 2012-09-14 09:03:25 +0400
    * Cassandra SE
      * Also provide handling for generic Thrift exceptions. These are not listed in the 'throws' clause of API definition but still can happen.
  * [Revision #3413.25.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.28)\
    Fri 2012-09-14 08:44:34 +0400
    * Cassandra SE
      * Catch all kinds of exceptions when calling Thrift code.
  * [Revision #3413.25.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.27)\
    Wed 2012-09-12 20:52:23 +0400
    * Cassandra SE: small optimization: StringCopyConverter::mariadb\_to\_cassandra doesn't need to make NULL-terminated strings.
  * [Revision #3413.25.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.26)\
    Wed 2012-09-12 07:36:23 +0400
    * Update test results after last cset
  * [Revision #3413.25.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.25)\
    Mon 2012-09-10 14:40:07 +0400
    * Cassandra SE: add support for reading counter type values
  * [Revision #3413.25.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.24)\
    Mon 2012-09-10 12:50:58 +0400
    * Cassandra SE
      * Make cassandra.test drop and re-crate the test keyspace.
  * [Revision #3413.25.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.23)\
    Fri 2012-09-07 15:32:43 +0400
    * Cassandra SE: added support for boolean type.
  * [Revision #3413.25.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.22)\
    Fri 2012-08-31 11:03:59 +0400
    * [MDEV-498](https://jira.mariadb.org/browse/MDEV-498): Cassandra: Inserting a timestamp does not work on a 32-bit system
      * Make an attempt at fixing.
  * [Revision #3413.25.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.21)\
    Fri 2012-08-31 10:49:36 +0400
    * Cassandra SE
      * add support for Cassandra's UUID datatype. We map it to CHAR(36).
  * [Revision #3413.25.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.20)\
    Wed 2012-08-29 20:27:11 +0400
    * Cassandra SE: fix batched insert to flush its buffers after insert operation.
  * [Revision #3413.25.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.19)\
    Wed 2012-08-29 11:14:04 +0400
    * Fix for the previous cset: Field::store\_TIME() accepts microseconds fraction, not millisecond.
  * [Revision #3413.25.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.18)\
    Wed 2012-08-29 11:05:46 +0400
    * Cassandra SE: Timestamp data type support.
  * [Revision #3413.25.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.17)\
    Wed 2012-08-29 10:05:21 +0400
    * Cassandra SE
      * Add mapping for INT datatype
      * Primary key column should now be named like CQL's primary key, or 'rowkey' if CF has key\_alias.
  * [Revision #3413.25.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.16)\
    Wed 2012-08-29 07:39:22 +0400
    * Cassandra storage engine: add @@rnd\_batch\_size variable.
  * [Revision #3413.25.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.15)\
    Tue 2012-08-28 20:22:45 +0400
    * [MDEV-494](https://jira.mariadb.org/browse/MDEV-494), part #1: phantom row for big full-scan selects
      * Full table scan internally uses LIMIT n, and re-starts the scan from the last seen rowkey value. rowkey ranges are inclusive, so we will see the same rowkey again. We should ignore it.
  * [Revision #3413.25.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.14)\
    Tue 2012-08-28 12:53:33 +0400
    * [MDEV-480](https://jira.mariadb.org/browse/MDEV-480): TRUNCATE TABLE on a Cassandra table does not remove rows
      * Remove HTON\_CAN\_RECREATE flag, re-create won't delete rows in cassandra.
  * [Revision #3413.25.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.13)\
    Mon 2012-08-27 08:44:58 +0400
    * Cassandra storage engine: BKA support
      * We use HA\_MRR\_NO\_ASSOC ("optimizer\_switch=join\_cache\_hashed") mode
      * Not able to use BKA's buffers yet.
      * There is a variable to control batch size
      * There are status counters.
      * Nedeed to make some fixes in BKA code (to be checked with Igor)
  * [Revision #3413.25.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.12)

```

Sun 2012-08-26 16:06:39 +0400

```

```
* Cassandra storage engine: bulk INSERT support

  * bulk inserts themselves
  * control variable and counters.
```

* [Revision #3413.25.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.11)

```

Thu 2012-08-23 21:16:01 +0400

```

```
* Enable mapping of CHAR(n)
* preparations for support of bulk INSERT.
```

* [Revision #3413.25.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.10)

```

Thu 2012-08-23 16:15:28 +0400

```

```
* # [MDEV-476](https://jira.mariadb.org/browse/MDEV-476): Cassandra: Server crashes in calculate_key_len on DELETE with ORDER BY


  * Fix typo in ha_cassandra::rnd_pos().
  * in ::index_read_map(), do not assume that pk column is part of table->read_set.
```

* [Revision #3413.25.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.9)

```

Tue 2012-08-21 18:38:27 +0400

```

```
* Make ha_cassandra work with filesort().
```

* [Revision #3413.25.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.8)

```

Mon 2012-08-20 12:08:29 +0400

```

```
* Read records in batches when doing full table scan.
```

* [Revision #3413.25.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.7)

```

Sun 2012-08-19 14:54:58 +0400

```

```
* position() and rnd_pos() implementations.
```

* [Revision #3413.25.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.6)

```

Sun 2012-08-19 13:21:23 +0400

```

```
* [MDEV-431](https://jira.mariadb.org/browse/MDEV-431): Cassandra storage engine

  * Partial support for DELETE ... WHERE.
```

* [Revision #3413.25.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.5)

```

Sun 2012-08-19 12:50:53 +0400

```

```
* [MDEV-431](https://jira.mariadb.org/browse/MDEV-431): Cassandra storage engine

  * Descriptive error messages
  * Unpack PK column on range scans
```

* [Revision #3413.25.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.4)

```

Sat 2012-08-18 21:29:31 +0400

```

```
* [MDEV-431](https://jira.mariadb.org/browse/MDEV-431): Cassandra storage engine

  * Support "DELETE FROM cassandra_table"
```

* [Revision #3413.25.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.3)

```

Sat 2012-08-18 21:21:50 +0400

```

```
* [MDEV-431](https://jira.mariadb.org/browse/MDEV-431): Cassandra storage engine

  * Got range reads to work (except for unpacking of the rowkey value)
```

* [Revision #3413.25.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.2)

```

Sat 2012-08-18 16:28:35 +0400

```

```
* [MDEV-431](https://jira.mariadb.org/browse/MDEV-431): Cassandra storage engine

  * Introduce type converters (so far rather trivial)
  * switch INSERT to using batch_mutate()
```

* [Revision #3413.25.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.25.1)

```

Fri 2012-08-17 21:13:20 +0400

```

```
* Initial commit for Cassandra storage engine.
```

```

* [Revision #3492](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492)\
  Fri 2013-01-11 16:33:51 +0100
  * make sure that our .deb packages provide mysql-\*-5.5 where appropriate
* [Revision #3491](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3491) \[merge]\
  Thu 2013-01-10 22:33:23 -0800
  * Merge 10.0-base -> 10.0.
  * Also fixed a bug in sql\_update.cc: the code of mysql\_update() lacked a call of set\_statistics\_for\_table().
  * [Revision #3427.1.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.31) \[merge]\
    Tue 2013-01-08 19:34:33 -0800
    * Merge 5.5-mwl248 -> 10.0-base
    * [Revision #3413.22.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.13) \[merge]\
      Tue 2013-01-08 15:04:14 -0800
      * Merge 5.5 -> mwl248
    * [Revision #3413.22.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.12)\
      Tue 2013-01-08 08:17:51 -0800
      * Fixed bug [MDEV-3979](https://jira.mariadb.org/browse/MDEV-3979). Made allocation of memory for statistical data in a table share to be thread safe. This memory is now allocated in a special MEM\_ROOT that is created for each table share.
  * [Revision #3427.1.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.30) \[merge]\
    Thu 2012-12-20 15:38:29 -0800
    * Merge mdev539->10.0-base.
    * [Revision #3427.10.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.10.1)\
      Thu 2012-12-20 10:58:40 -0800
      * The patch for the task [MDEV-539](https://jira.mariadb.org/browse/MDEV-539).
      * The patch lifts the limitation of the current implementation of ALTER TABLE that does not allow to build unique/primary indexes by sort for MyISAM and Aria engines.
  * [Revision #3427.1.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.29) \[merge]\
    Wed 2012-12-19 19:15:51 -0800
    * Merge mwl248->10.0-base.
    * [Revision #3427.9.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.9.1) \[merge]\
      Sun 2012-12-16 21:33:17 -0800
      * Merge maria-5.5-mwl248 -> 10.0-base.
      * [Revision #3413.22.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.11) \[merge]\
        Fri 2012-12-14 12:02:08 -0800
        * Merge 5.5 -> mwl248
      * [Revision #3413.22.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.10)\
        Thu 2012-12-13 23:05:12 -0800
        * Addressed all remaining issues from the review of the patch that introduced engine independent persistent statistics. In particular: - added an enumeration type for possible values of the system variable use\_stat\_tables - renamed KEY::real\_rec\_per\_key to KEY::actual\_rec\_per\_key - optimized the collection of statistical data for any primary key defined only on one column.
      * [Revision #3413.22.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.9)\
        Wed 2012-12-12 23:16:54 -0800
        * Fixed bug [MDEV-3891](https://jira.mariadb.org/browse/MDEV-3891). If a query referenced some system statistical tables, but not all of them, then executing an ANALYZE command simultaneously with this query could lead to a deadlock. The fix prohibited reading statistics from system statistical tables for such queries.
        * Removed the function unlock\_tables\_n\_open\_system\_tables\_for\_write() as not used anymore. Performed some minor refactoring of the code in sql\_statistics.cc.
      * [Revision #3413.22.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.8)\
        Sun 2012-12-09 21:33:08 -0800
        * Addressed the following issue from the review of the patch for engine-independent statistics. If a table was created for InnoDB then the execution of the ANALYZE command over this table blocked any INSERT/DELETE/UPDATE of the table.
      * [Revision #3413.22.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.7)\
        Sat 2012-12-08 15:38:15 -0800
        * Addressed the following issue from the review of the patch for engine-independent statistics. When the primary key was dropped or changed statistics on secondary indexes for the prefixes that included components of the primary key was not removed from the table mysql.index\_stats.
        * Also fixed: in the some cases when a column was changed statistics on the indexes that included this column was not removed from the table mysql.index\_stats.
        * Also disabled the test [MDEV-504](https://jira.mariadb.org/browse/MDEV-504) for `--ps-protocol`.
      * [Revision #3413.22.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.6)\
        Wed 2012-12-05 22:51:11 -0800
        * Addressed the following issues from the review of the patch: 1. The PERSISTENT FOR clause of the ANALYZE command overrides the setting of the system variable use\_stat\_tables: with this clause ANALYZE unconditionally collects persistent statistics. 2. ANALYZE collects persistent statistics only for tables of the USER category. So it never collects persistent statistics for system tables.
      * [Revision #3413.22.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.5)\
        Wed 2012-12-05 09:57:34 -0800
        * Adjusted results for a test. The adjustment was supposed to be done in the previous commit.
      * [Revision #3413.22.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.4)\
        Wed 2012-12-05 00:31:05 -0800
        * Changed the names of the system tables for statistical data: table\_stat -> table\_stats column\_stat -> column\_stats index\_stat -> index\_stats to be in line with the names of innodb statistical tables from mysql-5.6: innodb\_table\_stats and innodb\_index\_stats.
      * [Revision #3413.22.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.3) \[merge]\
        Tue 2012-12-04 19:04:25 -0800
        * Merge 5.5->mwl248
      * [Revision #3413.22.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.2)\
        Mon 2012-11-19 13:04:37 -0800
        * Fixed bug [MDEV-3866](https://jira.mariadb.org/browse/MDEV-3866). The invalid implementation of the method Field\_bit::cmp\_max could trigger a valgrind complain or could lead to incorrect statistical data when collecting engine-independent statistics on BIT fields.
      * [Revision #3413.22.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.22.1) \[merge]\
        Fri 2012-11-02 20:38:05 -0700
        * Merge 5.5 -> 5.5-mwl248.
        * [Revision #3334.1.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.39)\
          Wed 2012-09-12 15:33:03 -0700
          * Made the results from the stat\_tables\_rbr test to be not dependent on the debug mode.
        * [Revision #3334.1.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.38)\
          Tue 2012-09-11 22:36:04 -0700
          * Fixed bug [MDEV-518](https://jira.mariadb.org/browse/MDEV-518). If some statistical tables are corrupted the server should use the conventional statistical data.
        * [Revision #3334.1.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.37)\
          Mon 2012-09-10 22:22:57 -0700
          * Fixed bug [MDEV-485](https://jira.mariadb.org/browse/MDEV-485). RBR should be turned off when statistical tables are modified in the result of the execution of a DDL statement. Revised the fix for bug [MDEV-463](https://jira.mariadb.org/browse/MDEV-463). Ensured suppression of RBR for the modifications of the statistical tables triggered by the execution of any analyze operation.
        * [Revision #3334.1.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.36) \[merge]\
          Sat 2012-09-08 22:36:55 -0700
          * Merge 5.5 -> mwl248
        * [Revision #3334.1.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.35)\
          Sat 2012-09-08 20:33:03 -0700
          * Part 2 of the fix for bug [MDEV-504](https://jira.mariadb.org/browse/MDEV-504). Any Field object should use current\_thd instead of table->in\_use when THD is needed if table == NULL. This patch fixes the crash of test case from [MDEV-504](https://jira.mariadb.org/browse/MDEV-504).test.
        * [Revision #3334.1.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.34) \[merge]\
          Sat 2012-09-08 12:07:14 -0700
          * Merge.
          * [Revision #3334.3.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.3.1)\
            Mon 2012-09-03 22:01:52 +0400
            * Preliminary test case for [MDEV-504](https://jira.mariadb.org/browse/MDEV-504) in order to reproduce the problem
        * [Revision #3334.1.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.33)\
          Sat 2012-09-08 12:04:31 -0700
          * Fixed bug [MDEV-504](https://jira.mariadb.org/browse/MDEV-504). Opening system statistical tables and reading statistical data from them for a regular table should be done after opening and locking this regular table. No test case is provided with this patch.
        * [Revision #3334.1.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.32)\
          Sat 2012-09-01 23:51:47 -0700
          * Fixed bug [MDEV-503](https://jira.mariadb.org/browse/MDEV-503). If a table is already in the table cache but without data from persistent statistical tables then the function open\_and\_process\_table should not only allocate memory for this statistical data in the corresponding TABLE\_SHARE object, but also should copy the references to the data into certain fields of the TABLE data structure: for each key of the table KEY::read\_stats should be copied, and for each column of the table Field::read\_stats should be copied.
        * [Revision #3334.1.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.31) \[merge]\
          Wed 2012-08-29 18:50:38 -0700
          * Merge 5.5->5.5-mwl248.
        * [Revision #3334.1.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.30)\
          Mon 2012-08-27 14:19:25 -0700
          * Fixed bug [MDEV-487](https://jira.mariadb.org/browse/MDEV-487). The function collect\_statistics\_for\_table() when scanning a table did not take into account that the handler function ha\_rnd\_next could return the code HA\_ERR\_RECORD\_DELETE that should not be considered as an indication of an error. Also fixed a potential memory leak in this function.
        * [Revision #3334.1.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.29)\
          Thu 2012-08-23 11:22:26 -0700
          * Fixed bug [MDEV-473](https://jira.mariadb.org/browse/MDEV-473). With the new code of mysql-5.5 for metadata locking the function unlock\_tables\_n\_open\_system\_tables\_for\_write should not explicitly unlock tables for which external locks have been set and should not explicitly reset thd->lock to 0.
        * [Revision #3334.1.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.28)\
          Mon 2012-08-20 12:05:37 -0700
          * Fixed bug [MDEV-463](https://jira.mariadb.org/browse/MDEV-463). RBR should be turned off when an ANALYZE TABLE command is executed.
        * [Revision #3334.1.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.27)\
          Sat 2012-08-18 22:18:46 -0700
          * Fixed the following problem: the syntax of the ANALYZE command did not returned an error if the list of the specified index names contained the name 'primary'.
        * [Revision #3334.1.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.26)\
          Sat 2012-08-18 11:49:14 -0700
          * Made the process of collecting persistent statistics killable.
        * [Revision #3334.1.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.25)\
          Fri 2012-08-17 13:23:49 -0700
          * Fixed bug [MDEV-464](https://jira.mariadb.org/browse/MDEV-464). The value of system variable use\_stat\_tables was always reset to 0 ('never') by mistake at the launch of the server.
        * [Revision #3334.1.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.24) \[merge]\
          Tue 2012-08-14 12:42:14 -0700
          * Merge 5.5->5.5-mwl248
        * [Revision #3334.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.23) \[merge]\
          Mon 2012-07-30 23:08:05 -0700
          * Merge 5.5 -> 5.5-mwl248.
        * [Revision #3334.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.22)\
          Mon 2012-07-30 10:09:58 -0700
          * Fixed errors in the calls of the macros my\_atomic\_rwlock\_wrlock, my\_atomic\_rwlock\_wrunlock.
        * [Revision #3334.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.21)\
          Fri 2012-07-27 17:33:23 -0700
          * Moved the test cases for parallel execution from stat\_tables.test into a separate file stat\_tables\_par.test because the test cases could not be run with embedded server.
        * [Revision #3334.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.20)\
          Fri 2012-07-27 12:05:23 -0700
          * Added missing declaration of statistics\_lock. Replaced bzero with memset. Added missing `--source include/have_debug_sync.inc` into stat\_tables.test.
        * [Revision #3334.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.19)\
          Thu 2012-07-26 17:50:08 -0700
          * Performed re-factoring and re-structuring of the code for [MWL#248](https://askmonty.org/worklog/?tid=248):
            * Moved the definitions of the classes to store data from persistent statistical tables into statistics.h, leaving in other internal data structures only references to the corresponding objects.
            * Defined class Column\_statistics\_collected derived from the class Column\_statistics. This is a helper class to collect statistics on columns.
            * Moved references to read statistics to TABLE SHARE, leaving the reference to the collected statistics in TABLE.
            * Added a new clone method for the class Field allowing to clone fields attached to table shares. It was used to create fields for min/max values in the memory of the table share.
          * Also:
            * Added procedures to allocate memory for statistical data in the table share memory and in table memory.
          * Also:
            * Added a test case demonstrating how ANALYZE could work in parallel to collect statistics on different indexes of the same table.
            * Added a test two demonstrate how two connections working simultaneously could allocate memory for statistical data in the table share memory.
        * [Revision #3334.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.18)\
          Tue 2012-07-10 22:12:23 -0700
          * Made the output of the newly added test cases from statistics.test platform independent.
          * Adjusted results of funcs\_1.is\_columns\_mysql\_embedded.
        * [Revision #3334.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.17)\
          Tue 2012-07-10 16:34:39 -0700
          * Added procedures to delete records by keys from statistical tables. Now when a table is dropped the statistics on the table is removed from the statistical tables. If the table is altered in such a way that a column is dropped or the type of the column is changed then statistics on the column is removed from the table column\_stat. It also triggers removal of the statistics on the indexes who use this column as its component.
          * Added procedures that changes the names of the tables or columns in the statistical tables for. These procedures are used when tables/columns are renamed.
          * Also partly re-factored the code that introduced the persistent statistical tables.
          * Added test cases into statistics.test to cover the new code.
        * [Revision #3334.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.16) \[merge]\
          Tue 2012-06-26 11:37:48 -0700
          * Merge 5.5 -> 5.5-mwl248.
        * [Revision #3334.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.15)\
          Mon 2012-06-25 22:33:07 -0700
          * Changed the type of all double columns in the system statistical tables mysql.column\_stat, mysql.table\_stat for the type DECIMAL(12,4). When cached the values from these columns are multiplied by factor 10^5 and stored as ulong numbers now.
        * [Revision #3334.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.14)\
          Sat 2012-06-02 17:19:01 -0700
          * Removed the server option `--stat-tables`.
          * Renamed the system variable optimizer\_use\_stat\_tables to use\_stat\_tables.
          * This variable now has only 3 possible values: 'never', 'complementary', 'preferably'.
          * If the server has been launched with `--use-stat-tables='complementary'|'preferably'` then the statictics tables can be employed by the optimizer and by the ANALYZE command.
        * [Revision #3334.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.13)\
          Fri 2012-06-01 17:38:32 -0700
          * Fixed a buildbot failure with a testcase from statistics.test that analyzes only some columns from a table.
        * [Revision #3334.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.12) \[merge]\
          Fri 2012-06-01 13:42:39 -0700
          * Merge
        * [Revision #3334.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.11)\
          Fri 2012-06-01 11:23:53 -0700
          * An attempt to fix a buildbot failure with a test case from statistics.test that analyzes only some columns from a table.
        * [Revision #3334.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.10) \[merge]\
          Tue 2012-05-22 21:31:36 -0700
          * Merge.
          * [Revision #3334.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.2.1)\
            Tue 2012-05-22 20:55:07 -0700
            * Support of the extended syntax for ANALYZE.
        * [Revision #3334.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.9) \[merge]\
          Fri 2012-05-18 11:28:02 -0700
          * Merge.
        * [Revision #3334.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.8) \[merge]\
          Fri 2012-05-18 09:50:30 -0700
          * Merge.
        * [Revision #3334.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.7)\
          Thu 2012-05-17 16:54:26 -0700
          * Fixed the bug that caused displaying incorrect values in the column cardinality of the table information\_schema.statistics.
        * [Revision #3334.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.6)\
          Tue 2012-05-08 16:42:55 -0700
          * Inverted the option `--skip-stat-tables` for `--stat-tables`. Set it to 0 by default. Now only the tests that use persistent statistics tables require starting the server with `--stat-tables` set on.
        * [Revision #3334.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.5)\
          Sun 2012-05-06 22:42:14 -0700
          * Supported extended keys when collecting and using persistent statistics.
        * [Revision #3334.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.4)\
          Thu 2012-04-19 09:49:53 -0700
          * Fixed a problem for Q18 from DBT3/SF30 with innodb database instance: the server crashed when running the query with persistent statistics enabled.
          * The field KEY::read\_stat.avg\_frequency must be initialized to NULL for the keys of temporary tables.
        * [Revision #3334.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.3) \[merge]\
          Wed 2012-04-11 20:44:52 -0700
          * Merge 5.5 -> 5.5-mwl248.
        * [Revision #3334.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.2)\
          Wed 2012-04-11 17:14:06 -0700
          * The pilot implementation of [MWL#250](https://askmonty.org/worklog/?tid=250): Use the statistics from persistent statistical tables instead of the statistics provided by engine.
        * [Revision #3334.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3334.1.1) \[merge]\
          Mon 2012-03-19 01:35:32 -0700
          * Merge maria-5.3-mwl248 -> 5.5 = maria-5.5-mwl248.
          * [Revision #2502.574.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.574.8) \[merge]\
            Thu 2012-03-15 21:40:15 -0700
            * Merge
          * [Revision #2502.574.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.574.7) \[merge]\
            Fri 2012-03-09 19:04:59 -0800
            * Merged 5.3 changes into the mwl #248 tree.
          * [Revision #2502.574.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.574.6)\
            Mon 2012-01-09 21:14:34 -0800
            * [MWL#248](https://askmonty.org/worklog/?tid=248): added the option skip-stat-tables.
          * [Revision #2502.574.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.574.5)\
            Sat 2012-01-07 00:34:30 -0800
            * Made statistics.test platform independent.
          * [Revision #2502.574.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.574.4)\
            Thu 2012-01-05 22:45:08 -0800
            * Adjusted results for the test suite funcs\_1.
          * [Revision #2502.574.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.574.3)\
            Thu 2012-01-05 18:55:37 -0800
            * Fixed a compiler warning. Adjusted results for mysql\_upgrade.test
          * [Revision #2502.574.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.574.2)\
            Wed 2012-01-04 18:32:21 -0800
            * In statistics.test: Saved at the very beginning and restored at the very end the value of optimizer\_use\_stat\_tables.
          * [Revision #2502.574.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.574.1)\
            Wed 2012-01-04 17:51:53 -0800
            * The main patch for the [MWL#248](https://askmonty.org/worklog/?tid=248) back-ported from lp:igorb-seattle/mysql-server/mysql-azalea-wl4777.
* [Revision #3490](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3490) \[merge]\
  Tue 2012-12-18 22:13:14 +0100
  * Merge a couple more fixes from 10.0-base to 10.0
  * [Revision #3427.1.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.28)\
    Tue 2012-12-18 22:00:55 +0100
    * Previous change of have\_debug\_sync.inc broke non-debug builds. Implement it in a different way that works on both release and debug builds, and still uses `--skip` instead of `--require`.
  * [Revision #3427.1.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.27)\
    Tue 2012-12-18 11:56:00 +0100
    * [MDEV-3927](https://jira.mariadb.org/browse/MDEV-3927) Add variable "have yassl" have\_openssl variable was ON even when OpenSSL was not used (but YaSSL was). fix that, so that have\_openssl really corresponds to OpenSSL
    * rename not\_openssl.inc to not\_ssl.inc and fix the test accordingly.
* [Revision #3489](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3489)\
  Tue 2012-12-18 22:03:53 +0100
  * After-merge fixes for merge 10.0-base -> 10.0.
* [Revision #3488](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3488) \[merge]\
  Tue 2012-12-18 15:01:58 +0100
  * Merge [MariaDB 10.0](../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)-base to [MariaDB 10.0](../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
  * [Revision #3427.1.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.26)\
    Mon 2012-12-17 21:00:36 +0100
    * fix have\_debug\_sync.inc remove unused require files
  * [Revision #3427.1.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.25)\
    Mon 2012-12-17 20:47:23 +0100
    * [MDEV-438](https://jira.mariadb.org/browse/MDEV-438) Microseconds: Precision is ignored in CURRENT\_TIMESTAMP(N) when it is given as a default column value
    * For MySQL 5.6 compatibility, support precision specification in CURRENT\_TIMESTAMP in a default clause, when it's not less than the column's precision.
  * [Revision #3427.1.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.24)\
    Mon 2012-12-17 11:00:39 +0100
    * simplify the handler api - table\_type() is no longer abstract, not even virtual
  * [Revision #3427.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.23)\
    Mon 2012-12-17 10:56:26 +0100
    * remove HAVE\_EXPLICIT\_TEMPLATE\_INSTANTIATION
  * [Revision #3427.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.22)\
    Mon 2012-12-17 12:49:11 +0100
    * [MDEV-532](https://jira.mariadb.org/browse/MDEV-532): Fix some race conditions in test cases.
    * With [MDEV-532](https://jira.mariadb.org/browse/MDEV-532), the binlog\_checkpoint event is logged asynchronously from a binlog background thread. This causes some sporadic failures in some test cases whose output depends on order of events in binlog.
    * Fix using an include file that waits until the binlog checkpoint event has been logged before proceeding with the test case.
  * [Revision #3427.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.21) \[merge]\
    Sun 2012-12-16 16:49:19 -0800
    * Merge mariadb-5.5 -> 10.0-base.
  * [Revision #3427.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.20)\
    Fri 2012-12-14 15:38:07 +0100
    * [MDEV-532](https://jira.mariadb.org/browse/MDEV-532): Async InnoDB commit checkpoint.
    * Make the commit checkpoint inside InnoDB be asynchroneous. Implement a background thread in binlog to do the writing and flushing of binlog checkpoint events to disk.
  * [Revision #3427.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.19) \[merge]\
    Fri 2012-12-14 09:51:06 +0200
    * Automatic merge [MDEV-452](https://jira.mariadb.org/browse/MDEV-452) with the latest 10.0-base.
    * [Revision #3427.8.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.8.2)\
      Thu 2012-12-13 22:56:03 +0200
      * [MDEV-452](https://jira.mariadb.org/browse/MDEV-452) Add full support for auto-initialized/updated timestamp and datetime
      * Post-review changes according to Monty's review from 28/11/2012.
    * [Revision #3427.8.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.8.1) \[merge]\
      Thu 2012-10-18 15:57:12 +0300
      * Merge [MDEV-452](https://jira.mariadb.org/browse/MDEV-452) with the latest 10.0-base.
      * [Revision #3427.7.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.7.1)\
        Wed 2012-10-17 15:43:56 +0300
        * [MDEV-452](https://jira.mariadb.org/browse/MDEV-452) Add full support for auto-initialized/updated timestamp and datetime
        * Generalized support for auto-updated and/or auto-initialized timestamp and datetime columns. This patch is a reimplementation of MySQL's "[WL#5874](https://askmonty.org/worklog/?tid=5874): CURRENT\_TIMESTAMP as DEFAULT for DATETIME columns". In order to ease future merges, this implementation reused few function and variable names from MySQL's patch, however the implementation is quite different.
        * TODO: The only unresolved problem in this patch is the semantics of LOAD DATA for TIMESTAMP and DATETIME columns in the cases when there are missing or NULL columns. I couldn't fully comprehend the logic behind MySQL's behavior and its relationship with their own documentation, so I left the results to be more consistent with all other LOAD cases.
        * The problematic test cases can be seen by running the test file function\_defaults, and observing the test case differences. Those were left on purpose for discussion.
* [Revision #3487](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3487)\
  Sun 2012-12-16 21:45:45 +0100
  * small code cleanup taken from MySQL 5.6
* [Revision #3486](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3486)\
  Sun 2012-12-16 21:11:24 +0100
  * [MDEV-3816](https://jira.mariadb.org/browse/MDEV-3816) init-file stops getting executed if a long enough line is encountered; on a debug version, assertion \`! is\_set() || can\_overwrite\_status' fails backport improved bootstrap error handling from 5.6
  * Was:

```

revno: 3768.1.1\
committer: Christopher Powers [chris.powers@oracle.com](mailto:chris.powers@oracle.com)\
timestamp: Wed 2012-05-02 22:16:40 -0500\
message:\
Bug#11766342 INITIAL DB CREATION FAILS ON WINDOWS WITH AN ASSERT IN SQL\_ERROR.CC\
Improved bootstrap error handling:

* Detect and report file i/o errors
* Report query size errors with nearest query text

```

* [Revision #3485](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3485)\
  Sat 2012-12-15 21:55:04 +0100
  * [MDEV-3834](https://jira.mariadb.org/browse/MDEV-3834) Crossgrade from MySQL 5.6.7 to [MariaDB 10.0](../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) fails due to non-existing mysql.host table Treat the host table as optional, don't abort when it's missing
* [Revision #3484](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3484)\
  Sat 2012-12-15 21:54:18 +0100
  * [MDEV-3837](https://jira.mariadb.org/browse/MDEV-3837) Assertion \`table->read\_set == \&table->def\_read\_set' failed on updating a performance\_schema table This was failing not only for P\_S, but for any engine that had HA\_PRIMARY\_KEY\_REQUIRED\_FOR\_DELETE flag set (in the tree - only P\_S and federated). Because of this flag, read\_set and write\_set were (possibly) changed on update. But later the code modified these bitmaps and restored them to the default state, losing HA\_PRIMARY\_KEY\_REQUIRED\_FOR\_DELETE related changes.
* [Revision #3483](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3483)\
  Sat 2012-12-15 18:24:11 +0100
  * [MDEV-3860](https://jira.mariadb.org/browse/MDEV-3860) backport `--plugin-load-add` (and related mysql-test changes)

```

revno: 3383\
revision-id: georgi.kodinov@oracle.com-20110818083108-qa3h3ufqu4zne80a\
committer: Georgi Kodinov [Georgi.Kodinov@Oracle.com](mailto:Georgi.Kodinov@Oracle.com)\
timestamp: Thu 2011-08-18 11:31:08 +0300\
message:\
.\
Bug #11766001: 59026: ALLOW MULTIPLE --PLUGIN-LOAD OPTIONS\
.\
Implemented support for a new command line option :\
\--plugin-load-add=\
This option takes the same type of arguments that --plugin-load does\
and complements --plugin-load (that continues to operate as before) by\
appending its argument to the list specified by --plugin-load.\
So --plugin-load can be considered a composite option consisting of\
resetting the plugin load list and then calling --plugin-load-add to process\
the argument.\
Note that the order in which you specify --plugin-load and --plugin-load-add\
is important : "--plugin-load=x --plugin-load-add=y" will be equivalent to\
"--plugin-load=x,y" whereas "--plugin-load-add=y --plugin-load=x" will be\
equivalent to "plugin-load=x".\
.\
Incompatible change : the --help --verbose command will no longer print the\
\--plugin-load variable's values (as it doesn't have one). Otherwise both --plugin-load\
and --plugin-load-add are mentioned in it.

```

* [Revision #3482](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3482)\
  Wed 2012-12-12 19:54:04 +0200
  * New results of `--big` test ([MDEV-3862](https://jira.mariadb.org/browse/MDEV-3862) fix).
* [Revision #3481](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3481)\
  Tue 2012-11-20 15:11:22 +0200
  * [MDEV-3862](https://jira.mariadb.org/browse/MDEV-3862) Lift limitation for merging VIEWS with Subqueries in SELECT list.
* [Revision #3480](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3480) \[merge]\
  Tue 2012-11-20 14:22:51 +0100
  * Merge [MariaDB 10.0](../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)-base -> 10.0
  * [Revision #3427.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.18)\
    Tue 2012-11-20 14:20:26 +0100
    * [MDEV-3861](https://jira.mariadb.org/browse/MDEV-3861): Assertion in TC\_LOG\_MMAP.
    * Root cause was that number of entries in commit checkpoint buffer was bigger than total available entries in the mmap()'ed score file. This causes TC\_LOG\_MMAP to run out of entries before even the first checkpoint is started, which causes a hang.
    * Fixed by making sure we have fewer entries within one commit checkpoint than total available scorefile entries.
    * Another part of this bug was discovery of severel unrelated bugs in TC\_LOG\_MMAP dating back to 5.1. These were fixed in 5.1 and will be merged up (the problem this patch fixes exists only in 10.0).
* [Revision #3479](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3479)\
  Thu 2012-11-15 12:54:50 +0200
  * [MDEV-3858](https://jira.mariadb.org/browse/MDEV-3858) Change JOIN\_TAB::records\_read from ha\_rows to double
  * Currently JOIN\_TAB::records\_read is of type ha\_rows. This is an integer type, which prevents proper selectivity and rows estimates.
```

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
