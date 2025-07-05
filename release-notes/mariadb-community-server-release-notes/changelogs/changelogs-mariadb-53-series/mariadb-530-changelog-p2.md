# MariaDB 5.3.0 Changelog p2

[Download](https://downloads.askmonty.org/mariadb/5.3.0) |[Release Notes](../../old-releases/release-notes-mariadb-5-3-series/mariadb-530-release-notes.md) |**Changelog**\
(page:[1](mariadb-530-changelog.md)2[3](mariadb-530-changelog-p3.md)[4](mariadb-530-changelog-p4.md)[5](mariadb-530-changelog-p5.md)[6](mariadb-530-changelog-p6.md)\
) |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 26 July 2011

* [Revision #3069](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3069)\
  Wed 2011-06-29 16:05:16 -0700
  * Fixed [Bug #803410](https://bugs.launchpad.net/bugs/803410).\
    Due to this bug in the function generate\_derived\_keys\_for\_table some\
    key definitions to access materialized derived tables or materialized\
    views were constructed with invalid info for their key parts.\
    This could make the server crash when it optimized queries using\
    materialized derived tables or materialized views.
* [Revision #3068](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3068) \[merge]\
  Tue 2011-06-28 19:56:30 -0700
  * Merge.
  * [Revision #3065.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3065.1.1)\
    Tue 2011-06-28 18:31:54 -0700
    * Fixed [Bug #802860](https://bugs.launchpad.net/bugs/802860).\
      This crashing bug could manifest itself at execution of join queries\
      over materialized derived tables with IN subquery predicates in the\
      where clause. If for such a query the optimizer chose to use duplicate\
      weed-out with duplicates in a materialized derived table and chose to\
      employ join cache the execution could cause a crash of the server.\
      It happened because the JOIN\_CACHE::init method assumed that the value\
      of TABLE::file::ref is set at the moment when the method was called\
      for the employed join cache. It's true for regular tables, but it's\
      not true for materialized derived tables that are filled now at the\
      first access to them, i.e. after the JOIN\_CACHE::init has done its job.
    * To fix this problem for any ROWID field of materialized derived table\
      the procedure that copies fields from record buffers into the employed\
      join buffer first checks whether the value of TABLE::file::ref has\
      been set for the table, and if it's not so the procedure sets this value.
* [Revision #3067](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3067)\
  Tue 2011-06-28 15:48:44 +0300
  * Fixed [Bug #800679](https://bugs.launchpad.net/bugs/800679)
    * Analysis:
      * The failed assert ensured that the choice of subquery strategy\
        is performed only for queries with at least one table. If there\
        is a LIMIT 0 clause all tables are removed, and the subquery is\
        neither optimized, nor executed during actual optimization. However,\
        if the query is EXPLAIN-ed, the EXPLAIN execution path doesn't remove\
        the query tables if there is a LIMIT 0 clause. As a result, the\
        subquery optimization code is called, which violates the ASSERT\
        condition.
    * Solution:
      * Transform the assert into a condition, and if the outer query\
        has no tables assume that there will be at most one subquery\
        execution.
      * There is potentially a better solution by reengineering the\
        EXPLAIN/optimize code, so that subquery optimization is not\
        done if not needed. Such a solution would be a lot bigger and\
        more complex than a bug fix.
* [Revision #3066](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3066)\
  Tue 2011-06-28 11:11:26 +0400
  * [MySQL Bug #751484](https://bugs.mysql.com/bug.php?id=751484): Valgrind warning / sporadic crash in evaluate\_join\_record sql\_select.cc:14099 with semijoin
    * Added testcase. The bug is most likely fixed by [MWL#90](https://askmonty.org/worklog/?tid=90) code.
* [Revision #3065](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3065) \[merge]\
  Mon 2011-06-27 23:36:20 -0700
  * Merge
  * [Revision #3062.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3062.2.1)\
    Mon 2011-06-27 23:07:46 -0700
    * Fixed [Bug #800535](https://bugs.launchpad.net/bugs/800535).\
      The function create\_view\_field in some cases incorrectly set the maybe\_null\
      flag for the returned items.
* [Revision #3064](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3064) \[merge]\
  Tue 2011-06-28 00:18:42 +0300
  * Automatic merge
  * [Revision #3062.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3062.1.1) \[merge]\
    Tue 2011-06-28 00:13:22 +0300
    * Automatic merge
      * [Revision #3061.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3061.1.4)\
        Mon 2011-06-27 19:30:05 +0300
        * Added mytop to distribution (with some small trivial changes to make it workg good also for MariaDB)
      * [Revision #3061.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3061.1.3)\
        Mon 2011-06-27 19:07:24 +0300
        * New status variables: Rows\_tmp\_read, Handler\_tmp\_update and Handler\_tmp\_write\
          Split status variable Rows\_read to Rows\_read and Rows\_tmp\_read so that one can see how much real data is read.\
          Same was done with Handler\_update and Handler\_write.\
          Fixed bug in MEMORY tables where some variables was counted twice.\
          Added new internal handler call 'ha\_close()' to have one place to gather statistics.\
          Fixed bug where thd->open\_options was set to wrong value when doing admin\_recreate\_table()
      * [Revision #3061.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3061.1.2)\
        Mon 2011-06-27 12:51:13 +0300
        * Updated version tag to beta
      * [Revision #3061.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3061.1.1) \[merge]\
        Mon 2011-06-27 12:48:53 +0300
        * Automatic merge
          * [Revision #3039.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3039.1.2)\
            Mon 2011-06-27 12:45:03 +0300
            * Added reading of client-server my.cnf tag
          * [Revision #3039.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3039.1.1)\
            Mon 2011-06-13 14:07:44 +0300
            * Added test case to show that we get a warning from CHECK TABLE if we force auto\_increment value to 0
* [Revision #3063](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3063)\
  Mon 2011-06-27 23:38:56 +0400
  * Added TODO comments
* [Revision #3062](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3062)\
  Sun 2011-06-26 21:55:32 -0700
  * Fixed [Bug #801536](https://bugs.launchpad.net/bugs/801536).\
    Ensured valid calculations of the estimates stored in JOIN\_TAB::used\_fieldlength.
* [Revision #3061](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3061)\
  Sat 2011-06-25 14:02:27 -0700
  * Fixed [Bug #802023](https://bugs.launchpad.net/bugs/802023).\
    Made mergeable views and mergeable derived tables transparent for\
    the MIN/MAX optimization.
* [Revision #3060](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3060)\
  Fri 2011-06-24 21:18:20 -0700
  * Added test cases for [Bug #798625](https://bugs.launchpad.net/bugs/798625) and [Bug #800085](https://bugs.launchpad.net/bugs/800085)\
    fixed by the patch for [Bug #798621](https://bugs.launchpad.net/bugs/798621).
* [Revision #3059](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3059)\
  Fri 2011-06-24 18:42:14 -0700
  * Fixed [Bug #799499](https://bugs.launchpad.net/bugs/799499).\
    The following were missing in the patch for mwl106:
    * KEY\_PART\_INFO::fieldnr were not set for generated keys to access\
      tmp tables storing the rows of materialized derived tables/views
    * TABLE\_SHARE::column\_bitmap\_size was not set for tmp tables storing\
      the rows of materialized derived tables/views.
    * These could cause crashes or memory overwrite.
* [Revision #3058](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3058)\
  Fri 2011-06-24 14:38:53 -0700
  * Fixed [Bug #798576](https://bugs.launchpad.net/bugs/798576).\
    If a view/derived table is non-mergeable then the definition of the tmp table\
    to store the rows for it is created at the prepare stage. In this case if the\
    view definition uses outer joins and a view column belongs to an inner table\
    of one of them then the column should be considered as nullable independently\
    on nullability of the underlying column. If the underlying column happens to be\
    defined as non-nullable then the function create\_tmp\_field\_from\_item rather\
    than the function create\_tmp\_field\_from\_field should be employed to create\
    the definition of the interesting column in the tmp table.
* [Revision #3057](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3057) \[merge]\
  Fri 2011-06-24 21:43:31 +0400
  * Merge 5.2 -> 5.3\
    (testcase for [Bug #798597](https://bugs.launchpad.net/bugs/798597) now crashes)
* [Revision #3056](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3056)\
  Thu 2011-06-23 22:12:22 -0700
  * Fixed a valgrind problem.\
    The function setup\_tables should handle table\_list elements for\
    semijoin materialized tables in a special way when executing\
    a prepared statement for the second time.
* [Revision #3055](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3055)\
  Thu 2011-06-23 14:48:45 -0700
  * Fixed [Bug #800518](https://bugs.launchpad.net/bugs/800518).\
    The function simple\_pred did not take into account that a multiple equality\
    could include ref items (more exactly items of the class Item\_direct\_view\_ref).\
    It caused crashes for queries over derived tables or views if the\
    min/max optimization could be applied to these queries.
* [Revision #3054](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3054) \[merge]\
  Tue 2011-06-21 18:17:28 -0700
  * Merge
  * [Revision #3052.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3052.1.1)\
    Tue 2011-06-21 18:00:58 -0700
    * Fixed [Bug #798621](https://bugs.launchpad.net/bugs/798621).
    * The patch for [Bug #717577](https://bugs.launchpad.net/bugs/717577) and [Bug #724942](https://bugs.launchpad.net/bugs/724942) has missed to make adjustments for the\
      call item\_equal->add\_const(const\_item, orig\_field\_item) in the function\
      check\_simple\_equality that builds multiple equality for a field and a constant.\
      As a result, when this field happens to be a view field and the corresponding\
      Item\_field object F is wrapped in an Item\_direct\_view\_ref object R the object\
      F is placed in the multiple equality instead of the object R.\
      A substitution of an equal item for F potentially can cause very serious\
      problems and in some cases can lead to crashes of the server.
* [Revision #3053](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3053)\
  Tue 2011-06-21 23:01:01 +0300
  * [MWL#89](https://askmonty.org/worklog/?tid=89)\
    Removed forgotten EXPLAIN EXTENDED from the test file.
* [Revision #3052](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3052) \[merge]\
  Tue 2011-06-21 16:00:41 +0300
  * [MWL#89](https://askmonty.org/worklog/?tid=89)\
    Automerged with 5.3.
  * [Revision #3015.3.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3015.3.1)\
    Tue 2011-06-21 15:50:07 +0300
    * [MWL#89](https://askmonty.org/worklog/?tid=89)
      * Added regression test with queries over the WORLD database.
      * Discovered and fixed several bugs in the related cost calculation\
        functionality both in the semijoin and non-semijon subquery code.
      * Added DBUG printing of the cost variables used to decide between\
        IN-EXISTS and MATERIALIZATION.
* [Revision #3051](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3051)\
  Fri 2011-06-17 23:00:26 +0200
  * [Bug #779758](https://bugs.launchpad.net/bugs/779758) - fix missing alpha/beta etc in MSI and ZIP package names.
* [Revision #3050](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3050) \[merge]\
  Fri 2011-06-17 17:45:41 +0400
  * Merge fix for [Bug #778406](https://bugs.launchpad.net/bugs/778406).
  * [Revision #3048.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3048.1.1)\
    Wed 2011-06-15 18:37:01 +0400
    * [Bug #778406](https://bugs.launchpad.net/bugs/778406): Crash in hp\_movelink with Aria engine and subqueries\
      -In do\_sj\_dups\_weedout(), set nulls\_ptr to point to NULL bytes (and not to length bytes) of the DuplicateWeedout column.
* [Revision #3049](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3049) \[merge]\
  Wed 2011-06-15 21:48:38 -0700
  * Merge of mwl #106 into 5.3.
  * [Revision #3025.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3025.1.5)\
    Thu 2011-06-09 12:43:28 -0700
    * Fixed [Bug #794909](https://bugs.launchpad.net/bugs/794909).
      * The function generate\_derived\_keys did not take into account the fact\
        that the last element in the array of keyuses could be just a barrier\
        element. In some cases it could lead to a crash of the server.
    * Also fixed a couple of other bugs in generate\_derived\_keys: the inner\
      loop in the body of if this function did not change the cycle variables\
      properly.
  * [Revision #3025.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3025.1.4)\
    Thu 2011-06-09 00:13:00 -0700
    * Fixed [Bug #794038](https://bugs.launchpad.net/bugs/794038).\
      INSERT/UPDATE/DELETE statement that used a temptable view v1 could lead to\
      a crash if v1 was defined as a select from a mergeable view v2 that selected\
      rows from a temptable view v3.
    * When INSERT/UPDATE/DELETE uses a view that is not updatable then field\
      translation for the view should be created before the prepare phase.
  * [Revision #3025.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3025.1.3)\
    Mon 2011-06-06 12:19:35 -0700
    * Fixed [Bug #793436](https://bugs.launchpad.net/bugs/793436)
      * When looking for the execution plan of a derived table to be materialized\
        JOIN::optimize finds out that all joined tables of the derived table\
        contain not more than one row then the derived table should be maretialized\
        at the optimization stage.
      * Added a test case for the bug.
      * Adjusted results in other test cases.
  * [Revision #3025.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3025.1.2)\
    Sun 2011-06-05 21:54:25 -0700
    * Added two new flags for the optimizer switch:
      * 'derived\_merge':
        * if the flag is off then all derived tables are materialized
        * if the flag is on then mergeable derived tables are merged
      * 'derived\_with\_keys':
        * if the flag is off then no keys are created for derived tables
        * if the flag is on then for any derived table a key to access\
          the derived table may be created.
      * Now by default both flags are on.\
        Later the default values for the flags will be off to comply with\
        the current behaviour of mysql-5.1.
      * Uncommented previously commented out test case from parts.partition\_repair\_myisam\
        after having added an explicit requirement to materialize the derived\
        table used in the test case.
  * [Revision #3025.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3025.1.1) \[merge]\
    Sat 2011-06-04 19:56:06 -0700
    * Merged the code of [MWL#106](https://askmonty.org/worklog/?tid=106) into the latest 5.3 with [MWL#90](https://askmonty.org/worklog/?tid=90) pushed.\
      Resolved all conflicts and failures.
* [Revision #3048](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3048)\
  Wed 2011-06-15 17:40:18 +0400
  * [Bug #761598](https://bugs.launchpad.net/bugs/761598): Update .result file
* [Revision #3047](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3047)\
  Wed 2011-06-15 16:02:32 +0400
  * [Bug #598247](https://bugs.launchpad.net/bugs/598247): partition.test produces valgrind errors in 5.3-based branches
    * Testcase
* [Revision #3046](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3046)\
  Wed 2011-06-15 15:32:24 +0400
  * [Bug #761598](https://bugs.launchpad.net/bugs/761598): InnoDB: Error: row\_search\_for\_mysql() is called without ha\_innobase::external\_lock() in maria-5.3
    * Testcase
* [Revision #3045](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3045)\
  Wed 2011-06-15 13:43:04 +0400
  * [Bug #751439](https://bugs.launchpad.net/bugs/751439) Assertion \`!table->file || table->file->inited == handler::NONE' failed with subquery
    * Add testcase
* [Revision #3044](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3044)\
  Tue 2011-06-14 18:45:14 +0200
  * fix for cast of negative numbers to datetime
* [Revision #3043](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3043)\
  Sun 2011-06-12 11:28:22 +0200
  * a couple of fixes for pbxt tests
* [Revision #3042](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3042)\
  Tue 2011-06-14 15:21:54 +0200
  * Another attempt at fixing the rare random failures of rpl\_corruption
  * The previous patch partially fixed things by waiting for the old dump thread\
    on the master to exit before injecting the DBUG error. This prevents the error\
    injection going to the wrong thread.
  * However, there is still the problem that the old dump thread may never exit,\
    causing the wait to time out. This happens if the dump thread manages to write\
    all events down the socket before the socket is closed by the slave. The\
    master dump thread only checks for slave gone when writing a new event, so if\
    no new events are generated, old dump threads can hang around forever on the\
    master after the slave disconnects.
  * Fix by explicitly killing the old dump thread if it is still around.
* [Revision #3041](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3041)\
  Mon 2011-06-13 12:41:19 +0400
  * Remove redundant code that is a result of a wrong merge.\
    (Changeset sp1r-igor@olga.mysql.com-20070526173301-38848 moved this loop from one place\
    to another, then the merge of sp1r-gshchepa/uchum@gleb.loc-20070527192244-26330 have\
    kept both copies).
* [Revision #3040](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3040)\
  Sun 2011-06-12 00:35:53 +0400
  * In make\_join\_select():
    * move attempt to evaluate join->exec\_const\_cond() out of the "Extract constant part of each ON expression" loop\
      (it got there by mistake when merging).
* [Revision #3039](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3039) \[merge]\
  Sat 2011-06-11 12:04:42 +0300
  * Merge with Sergei's tree to get in latest microsecond patches and also fixes to innodb\_plugin.
  * [Revision #3027.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3027.1.6)\
    Fri 2011-06-10 21:15:13 +0200
    * more buildbot fixes
  * [Revision #3027.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3027.1.5)\
    Fri 2011-06-10 15:42:55 +0200
    * various fixes for buildbot failures
  * [Revision #3027.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3027.1.4)\
    Fri 2011-06-10 10:14:20 +0200
    * change test\_if\_equality\_guarantees\_uniqueness()\
      from an ad hoc set of limitations\
      to a correct rule
  * [Revision #3027.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3027.1.3)\
    Thu 2011-06-09 18:06:29 +0200
    * small optimization in Field\_time\_hires.
    * Fix Field\_time\_hires::reset()
  * [Revision #3027.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3027.1.2)\
    Thu 2011-06-09 17:23:39 +0200
    * bugfixes:
      * microsecond(TIME)
      * alter table datetime<->datetime(6)
      * max(TIME), mix(TIME)
  * [Revision #3027.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3027.1.1) \[merge]\
    Tue 2011-06-07 18:13:02 +0200
    * merge with 5.1-micro
      * [Revision #2502.1147.48](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2502.1147.48)\
        Mon 2011-06-06 20:28:15 +0200
        * revert a suggested "optimization" that introduced a bug
        * compilation error in mysys/my\_getsystime.c fixed
        * some redundant code removed
        * sec\_to\_time, time\_to\_sec, from\_unixtime, unix\_timestamp, @@timestamp now\
          use decimal, not double for numbers with a fractional part.
        * purge\_master\_logs\_before\_date() fixed
        * many bugs in corner cases fixed
      * [Revision #2502.1147.47](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2502.1147.47)\
        Thu 2011-05-26 19:16:10 +0200
        * innodb compatibility fix
      * [Revision #2502.1147.46](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2502.1147.46)\
        Thu 2011-05-26 18:11:26 +0200
        * fix for double or decimal to datetime conversion
* [Revision #3038](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3038)\
  Sat 2011-06-11 11:41:46 +0300
  * Fixed build failures with maria3.test and widows build
* [Revision #3037](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3037) \[merge]\
  Sat 2011-06-11 11:09:17 +0300
  * Merge with main 5.3
  * [Revision #3034.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3034.1.1) \[merge]\
    Fri 2011-06-10 12:09:21 +0300
    * Merge with 5.2
* [Revision #3036](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3036)\
  Fri 2011-06-10 12:45:43 +0400
  * [Bug #727183](https://bugs.launchpad.net/bugs/727183): [WL#90](https://askmonty.org/worklog/?tid=90) does not trigger with non-comma joins
    * Add a testcase (the bug has already been fixed)
* [Revision #3035](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3035)\
  Fri 2011-06-10 12:36:06 +0400
  * \[No BUG#] end\_tab\_idx==-1 passed as parameter to JOIN::get\_partial\_cost\_and\_fanout()
    * Handle the case when the subquery's join is degenerate and so has zero tables.
* [Revision #3034](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3034)\
  Thu 2011-06-09 21:39:31 +0300
  * Removed depricated `--`maria-options from mysqld.
* [Revision #3033](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3033)\
  Thu 2011-06-09 13:35:01 +0300
  * Fixed compile failure when we don't use system zlib
  * Fixed crash when setting query\_cache\_type to 0.
* [Revision #3032](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3032)\
  Thu 2011-06-09 11:13:03 +0300
  * Fixed build failure on OpenSolaris
* [Revision #3031](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3031)\
  Tue 2011-06-07 14:19:49 +0300
  * Upgraded to latest handlersocket code. This fixed [Bug #766870](https://bugs.launchpad.net/bugs/766870) "Assertion \`next\_insert\_id == 0' failed with handlersocket"
* [Revision #3030](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3030)\
  Tue 2011-06-07 10:54:37 +0300
  * Fixed that mysqld `--`no-defaults `--`help `--`verbose doesn't give a lot of irrelevant error messages.
* [Revision #3029](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3029)\
  Tue 2011-06-07 10:29:08 +0300
  * Fixed strict alias problem by replacing = with memcpy()
* [Revision #3028](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3028)\
  Mon 2011-06-06 15:50:46 -0700
  * Fixed [Bug #784441](https://bugs.launchpad.net/bugs/784441).\
    The code that added semi-join transformations missed checking\
    the state of the fixed flag for the items built with the\
    and\_items function before calls of the fix\_fields method.\
    This could lead to an abort failure when the first argument\
    of and\_items() happened to be NULL.
* [Revision #3027](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3027) \[merge]\
  Mon 2011-06-06 19:37:33 +0300
  * Merge with 5.2 to get bug fixes for thr\_lock
* [Revision #3026](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3026)\
  Mon 2011-06-06 17:25:01 +0300
  * Fixed that SHOW COLUMNS for a virtual persistent column shows 'PERSISTENT' instead of 'VIRTUAL'\
    Strict mode now gives error if one tries to update a virtual column.
* [Revision #3025](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3025)\
  Fri 2011-06-03 21:45:24 +0400
  * Buildbot fixes:
    * make sp.test work both with and without query\_cache (attempt 2)
    * fix compile warning in make\_sort\_key(), as directed by SergeiG
* [Revision #3024](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3024)\
  Fri 2011-06-03 15:06:13 +0200
  * Fixed compiler warning in central header file mysql\_priv.h.
* [Revision #3023](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3023)\
  Fri 2011-06-03 13:42:02 +0400
  * More changes from optimizer\_use\_mrr to optimizer\_switch
* [Revision #3022](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3022)\
  Fri 2011-06-03 11:32:21 +0400
  * Buildbot fixes: don't use @@optimizer\_use\_mrr, it has been moved into @@optimizer\_switch
* [Revision #3021](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3021)\
  Fri 2011-06-03 10:49:50 +0400
  * Buildbot fixes: let mysql-test/t/sp.test set @@query\_cache\_size only if the server has query cache.
* [Revision #3020](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3020) \[merge]\
  Fri 2011-06-03 09:38:59 +0400
  * Merge
  * [Revision #3018.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3018.1.1)\
    Fri 2011-06-03 00:25:58 +0400
    * Change optimizer\_use\_mrr=auto|disable|force\
      to be optimizer\_switch flags mrr=on|off and mrr\_cost\_based=on|off.
* [Revision #3019](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3019) \[merge]\
  Thu 2011-06-02 17:33:08 -0700
  * Merge
  * [Revision #3015.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3015.2.1)\
    Tue 2011-05-31 09:39:35 -0700
    * Corrected the previous patch concerning elimination of SQL\_SELECT::original\_cond.
    * Corrected the code from the patch for [Bug #702322](https://bugs.launchpad.net/bugs/702322).
* [Revision #3018](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3018) \[merge]\
  Thu 2011-06-02 23:52:36 +0400
  * Merge fix for [Bug #787299](https://bugs.launchpad.net/bugs/787299).
  * [Revision #3015.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3015.1.1)\
    Thu 2011-06-02 23:48:33 +0400
    * [Bug #787299](https://bugs.launchpad.net/bugs/787299): Valgrind complains on a join query with two IN subqueries
      * Don't attempt to construct FirstMatch access method if we've\
        just figured three lines above that it can't be used (because join\
        prefix doesn't have the needed tables), and so have set\
        pos->first\_firstmatch\_table= MAX\_TABLES
      * Attempts to analyze join->positions\[MAX\_TABLES] caused valgrind warnings
* [Revision #3017](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3017)\
  Thu 2011-06-02 16:46:47 +0400
  * Change suite/rpl/t/rpl\_row\_basic\_11bugs.test to require query cache.
* [Revision #3016](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3016) \[merge]\
  Tue 2011-05-31 12:16:02 +0200
  * automerge
  * [Revision #2732.26.25](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.25)\
    Tue 2011-05-31 12:14:21 +0200
    * Attempt to fix rpl.rpl\_corruption failure seen in Buildbot on Windows.
    * There is a potential race when we stop the slave. It may take some time for\
      the master to detect that the slave connection is closed (eg. if scheduling\
      delays the TCP RSET packet or whatever). Since we inject only a single corrupt\
      binlog event, we may be unfortunate enough to inject it on the wrong\
      connection, to a slave io thread that's already stopped.
    * Fix by waiting for the old dump thread on the master to go away before\
      injecting the corrupt event.
* [Revision #3015](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3015)\
  Mon 2011-05-30 11:19:40 +0400
  * Remove compiler warning
  * Remove garbage comments
* [Revision #3014](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3014) \[merge]\
  Mon 2011-05-30 10:51:41 +0400
  * Merge 5.3-main -> [MWL#90](https://askmonty.org/worklog/?tid=90)
* [Revision #3013](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3013)\
  Sun 2011-05-29 20:48:14 -0700
  * Eliminated the member original\_cond from the class SQL\_SELECT\
    introduced at the latest merge 5.1->5.2->5.3.\
    It is basically not needed since if SQL\_SELECT::pre\_idx\_push\_select\_cond\
    is not NULL then SQL\_SELECT::original\_cond would point to the same condition\
    as SQL\_SELECT::pre\_idx\_push\_select\_cond. Otherwise SQL\_SELECT::original\_cond\
    would be equal to SQL\_SELECT::cond.
* [Revision #3012](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3012)\
  Sat 2011-05-28 22:07:56 -0700
  * Fixed the abort failure of a test case from vcol.vcol\_misc.\
    The fix blocks execution of any constant sub-expressions of\
    the defining expressions for virtual columns when context\
    analysis if these expressions is performed.
  * Fixed a compiler warning.
* [Revision #3011](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3011)\
  Sat 2011-05-28 19:28:39 +0200
  * Fix gcc warning.
* [Revision #3010](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3010)\
  Sat 2011-05-28 16:57:58 +0200
  * Fix compile errors and warnings and test errors introduced by microseconds push.
  * Also, change windows timespec definition to be Unix-ish - simplifies handling a lot.
* [Revision #3009](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3009) \[merge]\
  Sat 2011-05-28 06:00:22 +0300
  * Automatic merge
  * [Revision #3006.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3006.1.4) \[merge]\
    Sat 2011-05-28 05:58:16 +0300
    * automatic merge with 5.3
  * [Revision #3006.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3006.1.3) \[merge]\
    Sat 2011-05-28 05:17:24 +0300
    * automatic merge with 5.2
  * [Revision #3006.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3006.1.2) \[merge]\
    Sat 2011-05-28 05:11:32 +0300
    * Merge with 5.1-microseconds
      * A lot of small fixes and new test cases.
  * [Revision #3006.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3006.1.1)\
    Mon 2011-05-23 15:14:54 +0300
    * Fixed errors found in buildbot
* [Revision #3008](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3008) \[
  * merge]\
    Fri 2011-05-27 19:05:35 +0200
  * merge
* [Revision #3007](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3007) \[merge]\
  Mon 2011-05-23 11:54:26 +0300
  * [MWL#89](https://askmonty.org/worklog/?tid=89) automatic merge with 5.3
  * [Revision #2991.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2991.1.3)\
    Mon 2011-05-23 10:56:05 +0300
    * [MWL#89](https://askmonty.org/worklog/?tid=89): Address review feedback (by Sergey Petrunia)
  * [Revision #2991.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2991.1.2)\
    Wed 2011-05-18 01:23:22 +0300
    * [MWL#89](https://askmonty.org/worklog/?tid=89) Addressing Sergey's review comments - Part 1.
    * Address the 'trivial' part of Sergey's review of [MWL#89](https://askmonty.org/worklog/?tid=89).
  * [Revision #2991.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2991.1.1) \[merge]\
    Tue 2011-05-17 14:56:02 +0300
    * [MWL#89](https://askmonty.org/worklog/?tid=89) - automatic merge with 5.3
* [Revision #3006](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3006)\
  Sat 2011-05-21 22:23:14 +0200
  * Fix comp\_errr crash ( fprintf crashes wheb uninitialized string is passed)
* [Revision #3005](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3005)\
  Sat 2011-05-21 00:46:18 +0300
  * Changed MariaDB error numbers to start from 1900 to not conflict with MySQL error numbers
* [Revision #3004](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3004)\
  Fri 2011-05-20 19:52:24 +0400
  * Fix a comment (unmatched '{' and '}' screw up jumping in advanced editors)
* [Revision #3003](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3003)\
  Fri 2011-05-20 19:08:55 +0400
  * Stabilize a testcase after fix for [Bug #784723](https://bugs.launchpad.net/bugs/784723), part 2
* [Revision #3002](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3002)\
  Fri 2011-05-20 14:15:22 +0400
  * Stabilize a testcase after fix for [Bug #784723](https://bugs.launchpad.net/bugs/784723)
* [Revision #3001](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3001) \[merge]\
  Fri 2011-05-20 10:13:02 +0400
  * Merge fix for [Bug #784723](https://bugs.launchpad.net/bugs/784723)
  * [Revision #2982.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2982.1.2)\
    Fri 2011-05-20 01:05:06 +0400
    * [Bug #784723](https://bugs.launchpad.net/bugs/784723): Wrong result with semijoin + nested subqueries in maria-5.3
      * in advance\_sj\_state(), remember join->cur\_dups\_producing\_tables in\
        pos->prefix\_dups\_producing\_tables _before_ we modify it, so that\
        restore\_prev\_sj\_state() restores cur\_dups\_producing\_tables in all cases.
      * Updated test results in subselect\_sj2\[\_jcl6].result (the original EXPLAIN\
        was invalid there)

[MariaDB 5.3.0](../../old-releases/release-notes-mariadb-5-3-series/mariadb-530-release-notes.md) Changelog — page:[1](mariadb-530-changelog.md)2[3](mariadb-530-changelog-p3.md)[4](mariadb-530-changelog-p4.md)[5](mariadb-530-changelog-p5.md)[6](mariadb-530-changelog-p6.md)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
