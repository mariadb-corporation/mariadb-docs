# MariaDB 5.3.0 Changelog p6

[Download](https://downloads.askmonty.org/mariadb/5.3.0) |[Release Notes](../../old-releases/release-notes-mariadb-5-3-series/mariadb-530-release-notes.md) |**Changelog**\
(page:`[1](mariadb-530-changelog.md)[2](mariadb-530-changelog-p2.md)[3](mariadb-530-changelog-p3.md)[4](mariadb-530-changelog-p4.md)[5](mariadb-530-changelog-p5.md)6`\
) |[Overview of 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)

**Release date:** 26 July 2011

* [Revision #2832](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2832)\
  Mon 2010-10-25 23:48:43 +0300
  * Fixed [Bug #609121](https://bugs.launchpad.net/bugs/609121)
  * The bug was a result of missing logic to handle the case\
    when there are 'expensive' predicates that are not evaluated\
    during constant table optimization. Such is the case for\
    the IN predicate, which is considered expensive if it is\
    computed via materialization. In general this bug can be\
    triggered with any expensive predicate instead of IN.
  *   When FALSE constant predicates are not evaluated during constant\
      optimization, the execution path changes so that instead of\
      setting JOIN::zero\_result\_cause after make\_join\_select, and\
      exiting JOIN::exec via the call to return\_zero\_rows(), execution\
      ends in JOIN::exec in the branch:

      ```c
      if (join->tables == join->const_tables)
      {
      ...
      else if (join->send_row_on_empty_set())
       ...
       rc= join->result->send_data(*columns_list);
      }
      ```
* Unlike return\_zero\_rows(), this branch didn't evaluate the\
  having clause of the query.
* The patch adds a call to evaluate the HAVING clause of a query even\
  when all tables are constant, because even for an empty result set\
  some aggregate functions may produce a NULL value.
* [Revision #2831](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2831)\
  Mon 2010-10-18 16:23:05 +0400
  * Make innodb\_plugin testsuite not to use IndexConditionPushdown or DS-MRR\
    (Otherwise we get different EXPLAINs for xtradb and innodb plugin).
* [Revision #2830](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2830)\
  Mon 2010-10-18 12:55:26 +0400
  * No BUG#, a case brought from 5.2's innodb\_mysql\_lock.test
    * Fix a crash in nested semi-join subquery processing
* [Revision #2829](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2829)\
  Sun 2010-10-17 18:05:29 +0400
  * [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) -> 5.2 post-merge fixes:
    * When building multiple-equalities for HAVING, don't set JOIN::cond\_equal, set\
      join\_having\_equal instead. Setting JOIN::cond\_equal based on HAVING makes\
      equality propagation data self-inconsistent
* [Revision #2828](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2828) \[merge]\
  Thu 2010-10-14 16:01:40 -0700
  * Merge from mariadb-5.1 (through mariadb-5.2)
* [Revision #2827](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2827)\
  Thu 2010-10-14 11:45:46 -0700
  * Turned off the test case for [MySQL Bug #49322](https://bugs.mysql.com/bug.php?id=49322) when join\_cache\_level=6.\
    It should be turned on back when the tree for [MWL#128](https://askmonty.org/worklog/?tid=128) is merged\
    into the main 5.3 merge.
* [Revision #2826](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2826) \[merge]\
  Thu 2010-10-14 01:50:16 +0400
  * Merge-in Sanja's post-merge fix
  * [Revision #2823.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2823.1.1)\
    Wed 2010-10-13 14:29:38 +0300
    * version of mysqld changed.
* [Revision #2825](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2825)\
  Thu 2010-10-14 01:48:03 +0400
  * Merge [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) -> [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)
    * post-merge fixes
* [Revision #2824](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2824)\
  Wed 2010-10-13 16:26:58 +0400
  * More post-merge test result updates (2).
* [Revision #2823](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2823)\
  Tue 2010-10-12 23:11:08 +0300
  * More post-merge test result updates
* [Revision #2822](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2822)\
  Tue 2010-10-12 22:48:49 +0300
  * Post-merge test result fixes part#1 (checked)
* [Revision #2821](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2821)\
  Sun 2010-10-10 22:43:19 +0300
  * Remove garbage comments
* [Revision #2820](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2820)\
  Sun 2010-10-10 17:38:17 +0300
  * Post-merge fixes part 1
* [Revision #2819](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2819) \[merge]\
  Sun 2010-10-10 17:18:11 +0300
  * Merge 5.2->5.3
    * Re-commit Monty's merge, partially fixed by Igor and SergeyP,\
      but still broken
* [Revision #2818](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2818)\
  Tue 2010-09-14 16:43:41 +0300
  * Engine should not be mentioned in such test
* [Revision #2817](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2817)\
  Thu 2010-09-09 11:01:13 +0300
  * table\_elimination switchable only for debug build and has no influence on the result of the test so it is removed.
* [Revision #2816](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2816)\
  Wed 2010-09-08 09:26:17 +0300
  * (no message)
* [Revision #2815](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2815)\
  Mon 2010-09-06 15:34:24 +0300
  * Fixed [Bug #615760](https://bugs.launchpad.net/bugs/615760): Check on double cache assignment added into the transformation methods.
  * Cache parameters print added in EXPLAIN EXTENDED output.
* [Revision #2814](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2814)\
  Wed 2010-09-01 17:42:41 +0300
  * pbxt test suite fix (expression test added to EXPLAIN EXTENDED).
* [Revision #2813](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2813)\
  Tue 2010-08-31 16:16:10 +0300
  * [Bug #615752](https://bugs.launchpad.net/bugs/615752) fix. Expression cache added to EXPLAIN EXTENDED output.
* [Revision #2812](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2812)\
  Mon 2010-08-30 11:07:16 +0300
  * Fixed [Bug #608744](https://bugs.launchpad.net/bugs/608744)
    * The bug is a result of the following change by Monty:
      * Revision Id: monty@askmonty.org-20100716073301-gstby2062nqd42qv\
        Fri 2010-07-16 10:33:01 +0300
  * Where Monty changed the queues interface and implementation.\
    The fix adjusts the queue\_remove call to the new interface.
* [Revision #2811](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2811)\
  Mon 2010-08-09 21:03:48 +0400
  * Let xtradb set mrr\_length\_per\_rec stats.
* [Revision #2810](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2810)\
  Mon 2010-08-09 13:00:58 +0300
  * Fix for [Bug #611625](https://bugs.launchpad.net/bugs/611625): Removing NULL references from subquery parameter list added.
  * Incorrect limitation on number of parameters removed.
* [Revision #2809](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2809)\
  Thu 2010-08-05 17:23:48 +0300
  * The test files renamed to have uniform name.
* [Revision #2808](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2808)\
  Fri 2010-07-30 07:16:58 +0300
  * Fix for [Bug #609043](https://bugs.launchpad.net/bugs/609043)
    * Removed indirect reference in equalities for cache index lookup.
    * We should use a direct reference because some optimization of the\
      query may optimize out a condition predicate and if the outer reference\
      is the only element of the condition predicate the indirect reference\
      becomes NULL.
    * We can resolve correctly the indirect reference in\
      Expression\_cache\_tmptable::make\_equalities because it is called before\
      optimization of the cached subquery.
* [Revision #2807](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2807)\
  Thu 2010-07-29 14:13:48 +0300
  * Bugfix for [Bug #608834](https://bugs.launchpad.net/bugs/608834) ([Bug #608824](https://bugs.launchpad.net/bugs/608824), [Bug #609045](https://bugs.launchpad.net/bugs/609045), [Bug #609052](https://bugs.launchpad.net/bugs/609052)).
  * Added get\_tmp\_table\_item() to cache wrapper as it has all not simple Items (Item\_func, Item\_field, Item\_subquery).
* [Revision #2806](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2806)\
  Fri 2010-07-23 11:25:00 +0300
  * Removed dead code that was made obsolete by the introduction of\
    check\_join\_cache\_usage() by the change:
    * [Revision #2793](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2793)\
      Revision Id: igor@askmonty.org-20091221022615-kx5ieiu0okmiupuc\
      Sun 2009-12-20 18:26:15 -0800
      * Backport into MariaDB-5.2 the following:
      * [MWL#2771](https://askmonty.org/worklog/?tid=2771) "Block Nested Loop Join and Batched Key Access Join"
* [Revision #2805](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2805)\
  Fri 2010-07-16 14:02:15 +0300
  * Fixed a problem where the temp table of a materialized subquery\
    was not cleaned up between PS re-executions. The reason was two-fold:
    * a merge with mysql-6.0 missed select\_union::cleanup() that should\
      have cleaned up the temp table, and
    * the subclass of select\_union used by materialization didn't call\
      the base class cleanup() method.
* [Revision #2804](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2804) \[merge]\
  Fri 2010-07-16 13:07:11 +0400
  * Merge
  * [Revision #2802.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2802.1.1)\
    Fri 2010-07-16 12:58:24 +0400
    * Fix @@optimizer\_switch support
      * Let "mysqld `--`help `--`verbose" list all optimizer options
      * Make it possible to add new @@optimizer\_switch flags w/o causing .result\
        changes all over the testsuite:
        * Remove "select @@optimizer\_switch" from tests that do not need all switches
        * Move @@optimizer\_switch-specific tests to t/optimizer\_switch.test
* [Revision #2803](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2803) \[merge]\
  Fri 2010-07-16 11:02:05 +0300
  * Merge with new queue code.\
    Updated configure.in to have version 5.3
  * [Revision #2800.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2800.1.1)\
    Fri 2010-07-16 10:33:01 +0300
    * Improved speed of thr\_alarm from O(N) to O(1). thr\_alarm is used to handle timeouts and kill of connections.\
      Fixed compiler warnings.\
      queues.h and queues.c are now based on the UNIREG code and thus made BSD.
    * Fix code to use new queue() interface. This mostly affects how you access elements in the queue.\
      If USE\_NET\_CLEAR is not set, don't clear connection from unexpected characters. This should give a speed up when doing a lot of fast queries.\
      Fixed some code in ma\_ft\_boolean\_search.c that had not made it from myisam/ft\_boolean\_search.c
* [Revision #2802](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2802)\
  Thu 2010-07-15 18:07:01 +0400
  * Fix order\_by test failure: don't run EXPLAIN for a query that has multiple\
    range plans with identical costs.
* [Revision #2801](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2801)\
  Thu 2010-07-15 16:59:10 +0300
  * Fixed an error in the creation of REF access method for materialized\
    subquery execution, where the REF buffer format was mistaken to\
    be in record format instead of key format. The error was that the null\
    byte for all fields of the record was in the front of the buffer,\
    and not before each field data.
* [Revision #2800](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2800)<>\
  Sat 2010-07-10 13:37:30 +0300
  * Subquery cache ([MWL#66](https://askmonty.org/worklog/?tid=66)) added.
* [Revision #2799](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2799)\
  Tue 2010-07-06 19:16:24 +0400
  * Fix buildbot valgrind failure
    * Item\_in\_subselect::init\_left\_expr\_cache() should not try to\
      guess whether the left expression is accessed "over the grouping operation"\
      (i.e. the subselect is evaluated after the grouping while the left\_expr is\
      an Item\_ref that wraps an expression from before the grouping). Instead,\
      let new\_Cached\_item not to try accessing item->real\_item() when creating\
      left expr cache.
* [Revision #2798](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2798)\
  Thu 2010-07-01 22:13:19 -0700
  * Added missing calls of update\_virtual\_fields() in the
    * join cache module.
    * Without these calls SELECTs over tables with virtual columns\
      that used join cache could return wrong results. This could\
      be seen with the test case added into vcol\_misc.test
* [Revision #2797](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2797)\
  Sun 2010-06-27 09:52:14 +0400
  * Add sql/opt\_index\_cond\_pushdown.cc to CMakeLists.txt files
* [Revision #2796](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2796)\
  Sun 2010-06-27 01:00:34 +0400
  * Fix windows build: add sql/opt\_subselect.cc to CMakeLists.txt files
* [Revision #2795](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2795)\
  Sun 2010-06-27 00:55:40 +0400
  * Fix valgrind failure: when creating key image, don't try to copy out more than\
    field->pack\_length() bytes.
* [Revision #2794](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2794)\
  Sat 2010-06-26 23:55:33 +0400
  * Fix windows build: provide log2 function if the system doesn't have it.
* [Revision #2793](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2793)\
  Sat 2010-06-26 23:33:16 +0400
  * Post-merge fixes: update test results for vcol and pbxt test suites.
* [Revision #2792](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2792)\
  Sat 2010-06-26 23:11:45 +0400
  * Post-merge fixes: Update test results. The differences in QEPs are because\
    5.3 had
    * handler::index\_only\_read\_time(uint keynr, double records)
    * while 5.2 got:
    * handler::keyread\_read\_time(uint index, uint ranges, ha\_rows rows)
  * which causes floor()'ing of rows parameter, which makes all further costs different.
* [Revision #2791](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2791)\
  Sat 2010-06-26 23:05:09 +0400
  * Post-merge fixes:
    * fix a bug in LooseScan strategy execution code (exposed by changing costs/QEP)
    * Do set join\_tab->sorted=TRUE for JOIN\_TABs that use LooseScan (partitioning\
      handler cares about "sorted" parameter of h->index\_init() call)
* [Revision #2790](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2790) \[merge]\
  Sat 2010-06-26 14:05:41 +0400
  * [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) -> [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) merge
* [Revision #2789](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2789)\
  Mon 2010-06-14 15:17:54 +0400
  * More comments
* [Revision #2788](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2788)\
  Mon 2010-05-10 15:46:08 +0200
  * fix compilation errors for builds w/o maria engine.\
    tests still fail, the fix will come from 5.1 tree
* [Revision #2787](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2787)\
  Tue 2010-03-30 00:09:40 +0400
  * Fix buildbot compile failure on hardy-amd64-makedist:\
    invoke proper Item\_int constructor.
* [Revision #2786](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2786)\
  Mon 2010-03-29 18:04:35 +0400
  * [MWL#110](https://askmonty.org/worklog/?tid=110): Make EXPLAIN always show materialization separately
    * Add Item\_in\_subselect::get\_identifier() that returns subquery's id
    * Change select\_describe() to produce output in new format
    * Update test results (checked)
* [Revision #2785](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2785)\
  Tue 2010-03-23 17:57:50 +0300
  * Disable subselect\_notembedded.test due to [Bug #545137](https://bugs.launchpad.net/bugs/545137)
* [Revision #2784](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2784)\
  Sun 2010-03-21 23:06:04 +0300
  * Make test result stable (had different result orderings, on some platforms, both\
    of which satisfied the ORDER BY clause).
* [Revision #2783](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2783)\
  Sun 2010-03-21 22:50:33 +0300
  * Fix merge error in pbxt suite test results
* [Revision #2782](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2782)\
  Sat 2010-03-20 19:59:30 +0300
  * Fix union.test failure in buildbot: alternate fix for [MySQL Bug #49734](https://bugs.mysql.com/bug.php?id=49734)
* [Revision #2781](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2781) \[merge]\
  Sat 2010-03-20 15:08:44 +0300
  * Merge
  * [Revision #2779.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2779.1.1)\
    Tue 2010-03-16 00:41:30 +0200
    * [MWL#68](https://askmonty.org/worklog/?tid=68): Subquery optimization: Efficient NOT IN execution with NULLs
    * Fix for the PBXT copy of subselect.test.
* [Revision #2780](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2780) \[merge]\
  Sat 2010-03-20 15:01:47 +0300
  * Merge MariaDB-5.2 -> [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)
* [Revision #2779](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2779) \[merge]\
  Mon 2010-03-15 21:52:58 +0200
  * Merge in [MWL#68](https://askmonty.org/worklog/?tid=68): Subquery optimization: Efficient NOT IN execution with NULLs
  * [Revision #2761.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2761.1.6)\
    Thu 2010-03-11 23:43:31 +0200
    * [MWL#68](https://askmonty.org/worklog/?tid=68) Subquery optimization: Efficient NOT IN execution with NULLs
    * This patch does three things:
      * It adds the possibility to force the execution of top-level \[NOT] IN\
        subquery predicates via the IN=>EXISTS transformation. This is done by\
        setting both optimizer switches partial\_match\_rowid\_merge and\
        partial\_match\_table\_scan to "off".
      * It adjusts all test cases where the complete optimizer\_switch is\
        selected because now we have two more switches.
      * For those test cases where the plan changes because of the new available\
        strategies, we switch off both partial match strategies in order to\
        force the "old" IN=>EXISTS strategy. This is done because most of these\
        test cases specifically test bugs in this strategy.
  * [Revision #2761.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2761.1.5) \[merge]\
    Tue 2010-03-09 12:36:15 +0200
    * [MWL#68](https://askmonty.org/worklog/?tid=68) Subquery optimization: Efficient NOT IN execution with NULLs
    * Automerge with 5.3-subqueries
  * [Revision #2761.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2761.1.4)\
    Tue 2010-03-09 12:14:06 +0200
    * [MWL#68](https://askmonty.org/worklog/?tid=68) Subquery optimization: Efficient NOT IN execution with NULLs
      * Implemented a second partial matching strategy via table scan.\
        This strategy is a fallback when there is no memory for rowid merging.
      * Refactored the selection and creation of partial matching strategies,\
        so that the choice of strategy is encapsulated in a separate method\
        choose\_partial\_match\_strategy().
      * Refactored the representation of partial match strategies so that:
        * each strategy is represented by a polymorphic class, and
        * the base class for all partial match strategies contains common\
          execution code.
      * Added an estimate of the memory needed for the rowid merge strategy,\
        and the system variable "rowid\_merge\_buff\_size" to control the maximum\
        memory to be used by the rowid merge algorithm.
      * Added two optimizer\_switch system variables to control the choice of\
        partial match strategy:\
        "partial\_match\_rowid\_merge", "partial\_match\_table\_scan".
      * Fixed multiple problems with deallocation of resources by the partial\
        match strategies.
  * [Revision #2761.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2761.1.3)\
    Mon 2010-02-22 17:16:55 +0200
    * [MWL#68](https://askmonty.org/worklog/?tid=68) Subquery optimization: Efficient NOT IN execution with NULLs
    * This patch mainly adds sorting of all indexes for partial matching\
      according to their NULL selectivity. The patch also fixes a related bug\
      in subselect\_rowid\_merge\_engine::test\_null\_row() where the wrong matched\
      indexes were skipped.
    * In addition the patch:
      * adds few ::print() methods,
      * renames few variables that had similar names but different purpose.
  * [Revision #2761.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2761.1.2) \[merge]\
    Mon 2010-02-22 15:57:09 +0200
    * Automerge with 5.3-subqueries
  * [Revision #2761.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2761.1.1)\
    Fri 2010-02-19 23:55:57 +0200
    * [MWL#68](https://askmonty.org/worklog/?tid=68) Subquery optimization: Efficient NOT IN execution with NULLs
    * This patch implements correct NULL semantics for materialized subquery execution.
    * The implementation has the following properties and main limitations:
      * It passes all query result tests, but fails a number of EXPLAIN tests because of\
        changed plans.
      * The EXPLAIN output for partial matching is not decided yet.
      * It works only when all necessary indexes fit into main memory. Notice that these\
        are not the general B-tree/Hash indexes, but instead much more compact ones,\
        therefore this limitation may not be a problem in many practical cases.
      * It doesn't contain specialized tests.
      * In several places the implementation uses methods that are modified copies of\
        other similar methods. These cases need to be refactored to avoid code duplication.
      * Add a test if the predicate is top-level just before deciding on partial matching.\
        If it is top-level, use a more efficient exec method (index lookup).
      * Add sorting of indexes according to their selectivity. The code is almost there.
      * Needs more comments, and to sync existing ones with the implementation.
* [Revision #2778](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2778) \[merge]\
  Mon 2010-03-15 09:35:35 +0300
  * Merge
  * [Revision #2776.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2776.1.1)\
    Mon 2010-03-15 09:06:59 +0300
    * Update test results for the previous push
* [Revision #2777](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2777)\
  Mon 2010-03-15 09:32:54 +0300
  * Apply fix by Roy Lyseng:
    * [MySQL Bug #48623](https://bugs.mysql.com/bug.php?id=48623): Multiple subqueries are optimized incorrectly
    * The function setup\_semijoin\_dups\_elimination() has a major loop that\
      goes through every table in the JOIN object. Usually, there is a normal\
      "plus one" increment in the for loop that implements this, but each semijoin\
      nest is treated as one entity and there is another increment that skips past\
      the semijoin nest to the next table in the JOIN object. However, when\
      combining these two increments, the next joined table is skipped, and if that\
      happens to be the start of another semijoin nest, the correct processing\
      for that nest will not be carried out.
* [Revision #2776](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2776) \[merge]\
  Sun 2010-03-14 21:25:43 +0300
  * Merge
  * [Revision #2773.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2773.1.2)\
    Sun 2010-03-14 00:11:06 +0300
    * Apply fix by oystein.grovlen@sun.com 2010-03-12:
      * [MySQL Bug #48213](https://bugs.mysql.com/bug.php?id=48213) Materialized subselect crashes if using GEOMETRY type
      *
      * The problem occurred because during semi-join a materialized table\
        was created which contained a GEOMETRY column, which is a specialized\
        BLOB column. This caused an segmentation fault because such tables will\
        have extra columns, and the semi-join code was not prepared for that.
      *
      * The solution is to disable materialization when Blob/Geometry columns would\
        need to be materialized. Blob columns cannot be used for index look-up\
        anyway, so it does not makes sense to use materialization.
      *
      * This fix implies that it is detected earlier that subquery materialization\
        can not be used. The result of that is that in->exist optimization may\
        be performed for such queries. Hence, extended query plans for such\
        queries had to be updated.
  * [Revision #2773.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2773.1.1)\
    Sat 2010-03-13 23:04:52 +0300
    * [MySQL Bug #45174](https://bugs.mysql.com/bug.php?id=45174): XOR in subqueries produces differing results in 5.1 and 5.4
    * [MySQL Bug #50019](https://bugs.mysql.com/bug.php?id=50019): Wrong result for IN-subquery with materialization
      * Fix equality substitution in presense of semi-join materialization, lookup and scan variants\
        (started off from fix by Evgen Potemkin, then modified it to work in all cases)
* [Revision #2775](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2775)\
  Sun 2010-03-14 20:55:49 +0300
  * Fix support-files/build-tags to work with recent versions of bazaar.
* [Revision #2774](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2774)\
  Sun 2010-03-14 20:54:12 +0300
  * [MySQL Bug #43768](https://bugs.mysql.com/bug.php?id=43768): Prepared query with nested subqueries core dumps on second execution
  * Fix two problems:
    1. Let optimize\_semijoin\_nests() reset sj\_nest->sjmat\_info irrespectively\
       of value of optimizer\_flag. We need this in case somebody has turned optimization\
       off between reexecutions of the same statement.
    2. Do not pull out constant tables out of semi-join nests. The problem is that pullout\
       operation is not undoable, and if a table is constant because it is 1/0-row table it\
       may cease to be constant on the next execution. Note that tables that are constant\
       because of possible eq\_ref(const) access will still be pulled out as they are\
       considered functionally-dependent.
* [Revision #2773](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2773)\
  Sun 2010-03-07 18:41:45 +0300
  * [MySQL Bug #49129](https://bugs.mysql.com/bug.php?id=49129): Wrong result with IN-subquery with join\_cache\_level=6 and firstmatch=off
    * The problem was that DuplicateWeedout strategy setup code wasn't aware of the\
      fact that join buffering will be used and applied optimization that doesn't work\
      together with join buffering. Fixed by making DuplicateWeedout setup code to have\
      a pessimistic check about whether there is a chance that join buffering will be\
      used.
    * Make JOIN\_CACHE\_BKA::init() correctly process Copy\_field elements that denote saving\
      current rowids in the join buffer.
* [Revision #2772](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2772)\
  Sat 2010-03-06 11:14:55 -0800
  * Fixed [MySQL Bug #51092](https://bugs.mysql.com/bug.php?id=51092).
    * The function JOIN\_CACHE::read\_all\_record\_fields could return 0\
      for an incremental join cache in two cases:
      1. there were no more records in the associated join buffer
      2. there was no table fields stored in the join buffer.
    * As a result the function JOIN\_CACHE::get\_record() could\
      return prematurely and did not read all needed fields from\
      join buffers into the record buffer.
    * Now the function JOIN\_CACHE::read\_all\_record\_fields returns\
      -1 if there are no more records in the associated join buffer.
* [Revision #2771](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2771)\
  Fri 2010-03-05 10:54:48 -0800
  * Corrected Evgen's fix for [MySQL Bug #45191](https://bugs.mysql.com/bug.php?id=45191).\
    Made sure that join buffers could be used for inner tables of\
    any semi-join when the first match strategy is employed.
* [Revision #2770](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2770)\
  Thu 2010-02-25 08:09:10 +0000
  * Prepare for OJ+SJ handling: Make replace\_where\_subcondition() not to assume\
    it's working on the WHERE clause.
* [Revision #2769](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2769)\
  Wed 2010-02-24 12:33:42 +0100
  * [MySQL Bug #49198](https://bugs.mysql.com/bug.php?id=49198) Wrong result for second call of procedure with view in subselect.
  * Re-worked fix of Tor Didriksen:
    * The problem was that fix\_after\_pullout() after semijoin conversion\
      wasn't propagated from the view to the underlying table.
    * On subesequent executions of the prepared statement,\
      we would mark the underlying table as 'dependent' and the predicate\
      anlysis would lead to a different (and illegal) execution plan.
* [Revision #2768](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2768)\
  Tue 2010-02-23 11:22:02 +0200
  * Subquery backport: update pbxt suite test results (checked).
* [Revision #2767](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2767)\
  Sun 2010-02-21 09:53:12 +0200
  * Fix buildbot failure: take into account that there is no optimizer\_switch flag\
    for table elimination in debug builds.\
    (part 2)
* [Revision #2766](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2766)\
  Sun 2010-02-21 09:33:54 +0200
  * Fix buildbot failure: take into account that there is no optimizer\_switch flag\
    for table elimination in debug builds.
* [Revision #2765](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2765)\
  Sun 2010-02-21 08:32:23 +0200
  * Change Field\_enumerator to enumerate Item\_field-s not Field-s.\
    In Item\_ref::fix\_fields() do invoke mark\_as\_dependent() for outside\
    references in all cases (see email for more details)
* [Revision #2764](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2764)\
  Sun 2010-02-21 05:36:18 +0200
  * Better self-recursion protection in Item\_subselect::fix\_fields.\
    Don't go into branch that calls upper\_refs.empty() more than once per\
    PREPARE or EXECUTE
  * Avoid crashing when processing references to outside from subquery's HAVING\
    (will explain in more details in email)
* [Revision #2763](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2763)\
  Sat 2010-02-20 11:23:29 +0300
  * Fix Item\_subselect::update\_used\_tables() and fix\_after\_pullout() to work with\
    prepared statements: re-collect list of upper refs on every PS re-execution.
* [Revision #2762](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2762)\
  Thu 2010-02-18 01:54:59 +0300
  * Subquery backport: update test results (checked).
* [Revision #2761](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2761)\
  Thu 2010-02-18 00:59:41 +0300
  * Subquery optimizations backport: fix test failures, update test results.
* [Revision #2760](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2760)\
  Wed 2010-02-17 13:47:55 +0300
  * Subquery backport:
    * More test results updates (checked)
* [Revision #2759](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2759)\
  Wed 2010-02-17 13:05:27 +0300
  * Subquery optimizations backport:
    * Update test results
    * More comments
    * Add Item\_in\_optimizer::transform() which was lost in backport
* [Revision #2758](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2758)\
  Tue 2010-02-16 00:53:06 +0300
  * Subquery optimization backport:
    * Factor out subquery code into sql/opt\_subselect.{h,cc}
    * Stop using the term "confluent" (was used due to misreading the dictionary)
* [Revision #2757](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2757)\
  Fri 2010-02-12 21:10:41 +0300
  * Fix for previous cset
* [Revision #2756](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2756)\
  Fri 2010-02-12 02:59:58 +0300
  * [MySQL Bug #31480](https://bugs.mysql.com/bug.php?id=31480): Incorrect result for nested subquery when executed via semi join
    * Variant #3 of the fix. It also
      * Unifies code with table elimination's
      * is able to handle FROM-subquery pullout.
* [Revision #2755](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2755)\
  Fri 2010-02-12 01:31:18 +0300
  * Subquery optimizations: backport: enable disabled subquery code in BKA
* [Revision #2754](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2754)\
  Fri 2010-02-12 01:00:36 +0300
  * Subquery optimizations: backport
    * Fix valgrind failure: do initialize Item::is\_expensive\_cache.
* [Revision #2753](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2753)\
  Fri 2010-02-12 00:59:32 +0300
  * Subquery optimizations backport: Update test results (checked)
* [Revision #2752](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2752)\
  Fri 2010-02-12 00:58:23 +0300
  * Apply Jorgen Loland's fix: [MySQL Bug #45221](https://bugs.mysql.com/bug.php?id=45221): Query "SELECT pk FROM C WHERE pk IN (SELECT int\_key)" failing
    * XOR conditions are not optimized, and Item\_cond\_xor therefore\
      acts like type Func\_item even though it inherits from Item\_cond.\
      A subtle difference between Item\_func and Item\_cond is that\
      you can get the children Items from the former by calling\
      arguments(), and from the latter by calling argument\_list().\
      However, since Item\_cond\_xor inherits from Item\_cond,\
      arguments() did not return any Items.
    *
    * The fact that Item\_cond\_xor::arguments() did not return it's\
      children items lead to a problem for make\_cond\_for\_index();\
      the method accepted that XOR items on unindexed columns were\
      pushed using ICP. ICP evaluation of non-indexed columns\
      does not (and should not) work.
    *
    * The fix for this bug is to make Item\_cond\_xor return it's\
      children items when the arguments() method is used. This makes\
      Item\_cond\_xor behave more like Item\_func and in turn allows\
      make\_cond\_for\_index() to discover any conflicting children\
      Items.
    *
    * This is a temporary fix and should be removed when Item\_cond\_xor\
      is optimized.
* [Revision #2751](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2751)\
  Fri 2010-02-12 00:56:02 +0300
  * Subquery backport: Update test results (checked)
* [Revision #2750](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2750)\
  Fri 2010-02-12 00:54:56 +0300
  * Subquery optimization backport: Duplicate Elimination:\
    process temporary table overflow correctly.
* [Revision #2749](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2749)\
  Thu 2010-01-28 16:48:33 +0300
  * Subquery optimizations: non-semijoin materialization
    * Backport into Maria DB 5.3, part 1
* [Revision #2748](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2748)\
  Tue 2010-01-19 01:32:23 +0300
  * Subquery optimizations: Backport into 5.3:
    * Enable semi-join handling in the join cache code
* [Revision #2747](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2747)\
  Sun 2010-01-17 23:52:20 +0300
  * Subquery optimizations, backport to 5.3:
    * Fix valgrind failure
    * Test result fixes (not finished)
* [Revision #2746](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2746)\
  Sun 2010-01-17 18:01:59 +0300
  * Fix incorrect merge
* [Revision #2745](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2745) \[merge]\
  Sun 2010-01-17 17:55:08 +0300
  * Merge
  * [Revision #2743.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2743.1.1)\
    Fri 2010-01-01 10:36:55 +0200
    * Backport of subquery optimizations to 5.3
* [Revision #2744](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2744)\
  Sun 2010-01-17 17:51:10 +0300
  * Backport of subquery optimizations to 5.3.\
    There are still test failures because of:
    * Wrong query results in outer join + semi join
    * EXPLAIN output differences
* [Revision #2743](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2743)\
  Sun 2009-12-27 23:24:22 +0300
  * DS-MRR backport: fix buildbot valgrind failures:
    * Do call update\_used\_tables() for new conditions obtained when adding\
      outer join's triggered conditions. Correct values of used\_tables() are\
      now needed for condition pushdown.
    * Update test results
* [Revision #2742](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2742) \[merge]\
  Tue 2009-12-22 07:18:49 -0800
  * Merge
  * [Revision #2738.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2738.1.4)\
    Tue 2009-12-22 17:43:00 +0300
    * Make testcase work for both debug and release
    * Add opt\_range\_mrr.cc file into source repo
  * [Revision #2738.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2738.1.3) \[merge]\
    Tue 2009-12-22 15:49:15 +0300
    * Merge [MWL#67](https://askmonty.org/worklog/?tid=67): MRR Backport and BKA backport.
  * [Revision #2738.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2738.1.2)\
    Tue 2009-12-22 15:33:21 +0300
    * [MWL#67](https://askmonty.org/worklog/?tid=67): MRR backport
    * Make index condition pushdown be controlled by an @@optimizer\_switch flag,\
      not by @@engine\_condition\_pushdown
      * Make MRR buffer size be controlled by @@mrr\_buffer\_size, not\
        by @@read\_rnd\_buffer\_size
      * Move parts of code to separate files
      * Code cleanup
      * Add `--`sorted\_result to some SELECTs in tests.
* [Revision #2741](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2741)\
  Tue 2009-12-22 07:12:09 -0800
  * Added the include files needed for join\_cache.test.
* [Revision #2740](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2740) \[merge]\
  Mon 2009-12-21 10:34:47 -0800
  * Merge from 5.2-dsmrr
  * [Revision #2738.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2738.1.1)\
    Sat 2009-12-19 22:54:54 +0300
    * DS-MRR backport: Update test results (checked)
* [Revision #2739](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2739)\
  Sun 2009-12-20 18:26:15 -0800
  * Backport into MariaDB-5.2 the following:[WL#2771](https://askmonty.org/worklog/?tid=2771) "Block Nested Loop Join and Batched Key Access Join"
* [Revision #2738](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2738)\
  Wed 2009-12-16 12:28:51 +0300
  * DS-MRR backport:
    * Fix PBXT test results (PBXT doesn't support MRR or ICP, but we get result\
      diffs because we've also backported a fix that
      * prints out "Using where" when the table has part of WHERE that it has\
        got from LEFT JOIN's ON expression
      * Does a better job at removing equalities that are guaranteed to be true\
        by use of ref acccess.
* [Revision #2737](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2737)\
  Wed 2009-12-16 01:37:39 +0300
  * Add ds\_mrr.cc to CMakeLists.txt
* [Revision #2736](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2736)\
  Wed 2009-12-16 00:35:55 +0300
  * Fix compile failure
* [Revision #2735](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2735)\
  Tue 2009-12-15 20:23:55 +0300
  * Backport into MariaDB-5.2 the following:
    * [MWL#2474](https://askmonty.org/worklog/?tid=2474) "Multi Range Read: Change the default MRR implementation to implement new MRR interface"
    * [MWL#2475](https://askmonty.org/worklog/?tid=2475) "Batched range read functions for MyISAM/InnoDb"\
      "Index condition pushdown for MyISAM/InnoDB"
      * Adjust test results (checked)
      * Code cleanup.
* [Revision #2734](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2734)\
  Tue 2009-12-15 17:53:30 +0300
  * Backport into MariaDB-5.2 the following:
    * [MWL#2474](https://askmonty.org/worklog/?tid=2474) "Multi Range Read: Change the default MRR implementation to implement new MRR interface"
    * [MWL#2475](https://askmonty.org/worklog/?tid=2475) "Batched range read functions for MyISAM/InnoDb"\
      "Index condition pushdown for MyISAM/InnoDB"
    * Fix valgrind failures
* [Revision #2733](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2733)\
  Tue 2009-12-15 10:16:46 +0300
  * Backport into MariaDB-5.2 the following:
    * [MWL#2474](https://askmonty.org/worklog/?tid=2474) "Multi Range Read: Change the default MRR implementation to implement new MRR interface"
    * [MWL#2475](https://askmonty.org/worklog/?tid=2475) "Batched range read functions for MyISAM/InnoDb"\
      "Index condition pushdown for MyISAM/InnoDB"
    * Igor's fix from sp1r-igor@olga.mysql.com-20080330055902-07614:\
      There could be observed the following problems:
      1. EXPLAIN did not mention pushdown conditions from on expressions in the\
         'extra' column. As a result if a query had no where conditions pushed\
         down to a table, but had on conditions pushed to this table the 'extra'\
         column in the EXPLAIN for the table missed 'using where'.
      2. Conditions for ref access were not eliminated from on expressions\
         though such conditions were eliminated from the where condition.

[MariaDB 5.3.0](../../old-releases/release-notes-mariadb-5-3-series/mariadb-530-release-notes.md) Changelog — page:`[1](mariadb-530-changelog.md)[2](mariadb-530-changelog-p2.md)[3](mariadb-530-changelog-p3.md)[4](mariadb-530-changelog-p4.md)[5](mariadb-530-changelog-p5.md)6`

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
