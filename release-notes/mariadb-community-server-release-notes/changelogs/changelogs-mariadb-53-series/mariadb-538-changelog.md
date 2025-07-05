# MariaDB 5.3.8 Changelog

[Download](https://downloads.mariadb.org/mariadb/5.3.8) |[Release Notes](../../old-releases/release-notes-mariadb-5-3-series/mariadb-538-release-notes.md) |**Changelog** |[Overview of 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)

**Release date:** 28 Aug 2012

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-5-3-series/mariadb-538-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3564](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3564)\
  Fri 2012-08-24 23:43:18 +0200
  * [MDEV-336](https://jira.mariadb.org/browse/MDEV-336) oqgraph 5.5 crashes in buildbot
  * force -fno-strict-aliasing for oqgraph
* [Revision #3563](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3563)\
  Sat 2012-08-25 09:15:57 +0300
  * fix for [MDEV-367](https://jira.mariadb.org/browse/MDEV-367)
  * The problem was that was\_null and null\_value variables was reset in each reexecution of IN subquery, but engine rerun only for non-constant subqueries.
  * Fixed checking constant in Item\_equal sort.
  * Fix constant reporting in Item\_subselect.
* [Revision #3562](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3562) \[merge]\
  Fri 2012-08-24 19:13:34 +0200
  * Merge from 5.2
  * [Revision #2732.57.15](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.15) \[merge]\
    Fri 2012-08-24 19:12:47 +0200
    * Merge from 5.1
    * [Revision #2643.153.14](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.14)\
      Fri 2012-08-24 19:11:54 +0200
      * Fix compiler warning
* [Revision #3561](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3561) \[merge]\
  Fri 2012-08-24 15:39:34 +0200
  * Merge from 5.2.
  * [Revision #2732.57.14](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.14) \[merge]\
    Fri 2012-08-24 15:37:39 +0200
    * Merge from 5.1.
    * [Revision #2643.153.13](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.13)\
      Fri 2012-08-24 15:32:44 +0200
      * Fix compiler warnings
    * [Revision #2643.153.12](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.12) \[merge]\
      Fri 2012-08-24 10:34:55 +0200
      * Merge with latest 5.1.
  * [Revision #2732.57.13](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.13)\
    Fri 2012-08-24 15:30:05 +0200
    * [MDEV-484](https://jira.mariadb.org/browse/MDEV-484) : allow compilation/packaging on Windows with newly released VS2012
  * [Revision #2732.57.12](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.12) \[merge]\
    Fri 2012-08-24 12:57:19 +0200
    * Merge into latest 5.2.
* [Revision #3560](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3560) \[merge]\
  Fri 2012-08-24 14:26:23 +0200
  * Merge into latest 5.3
  * [Revision #3556.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3556.1.2) \[merge]\
    Fri 2012-08-24 14:02:32 +0200
    * merge from 5.2
    * [Revision #2732.59.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.59.1) \[merge]\
      Fri 2012-08-24 12:32:46 +0200
      * Merge from 5.1.
      * [Revision #2643.154.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.154.1)\
        Fri 2012-08-24 10:06:16 +0200
        * [MDEV-382](https://jira.mariadb.org/browse/MDEV-382): Incorrect quoting ([CVE-2012-4414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-4414))
        * Various places in the server replication code was incorrectly quoting\
          strings, which could lead to incorrect SQL on the slave/mysqlbinlog.
  * [Revision #3556.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3556.1.1) \[merge]\
    Fri 2012-08-24 13:51:16 +0200
    * Merge from 5.2
* [Revision #3559](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3559)\
  Thu 2012-08-23 13:52:36 +0200
  * remove mysql-5.1 assert that is already absent in mysql-5.5
* [Revision #3558](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3558)\
  Wed 2012-08-22 18:40:27 +0200
  * [MDEV-472](https://jira.mariadb.org/browse/MDEV-472) `mysql-test-run --valgrind main.ps_2myisam` gives warning about not initialized memory
  * `Item::get_date()` should return 1 unless the value is a valid date.
* [Revision #3557](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3557) \[merge]\
  Wed 2012-08-22 16:45:25 +0200
  * 5.2 merge.
  * two tests still fail:
    * main.innodb\_icp and main.range\_vs\_index\_merge\_innodb
    * call records\_in\_range() with both range ends being open\
      (which triggers an assert)
  * [Revision #2732.57.11](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.11) \[merge]\
    Wed 2012-08-22 16:13:54 +0200
    * 5.1 merge
    * increase xtradb verson from 13.0 to 13.01
    * [Revision #2643.153.11](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.11)\
      Wed 2012-08-22 16:10:31 +0200
      * merge with XtraDB as of Percona-Server-5.1.63-rel13.4
    * [Revision #2643.153.10](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.10) \[merge]\
      Wed 2012-08-22 11:40:39 +0200
      * merge with MySQL 5.1.65
  * [Revision #2732.57.10](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.10)\
    Thu 2012-06-21 18:47:13 +0300
    * Fix for [Bug #1001505](https://bugs.launchpad.net/bugs/1001505) and [Bug #1001510](https://bugs.launchpad.net/bugs/1001510)
    * We set correct cmp\_context during preparation to avoid changing it later by Item\_field::equal\_fields\_propagator.\
      (see mysql bugs #57135 #57692 during merging)
* [Revision #3556](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3556)\
  Tue 2012-08-21 22:24:34 +0400
  * Better comments
* [Revision #3555](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3555)\
  Tue 2012-08-14 14:25:56 -0700
  * Corrected the pactch for [MDEV-449](https://jira.mariadb.org/browse/MDEV-449) to fix valgrind failures.
* [Revision #3554](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3554)\
  Mon 2012-08-13 21:13:14 -0700
  * Fixed bug [MDEV-449](https://jira.mariadb.org/browse/MDEV-449).
  * The bug could caused a crash when the server executed a query with\
    ORDER by and sort\_buffer\_size was set to a small enough number.
  * It happened because the small sort buffer did not allow to allocate\
    all merge buffers in it.
  * Made sure that the allocated sort buffer would be big enough\
    to contain all possible merge buffers.
* [Revision #3553](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3553) \[merge]\
  Thu 2012-08-02 00:58:13 +0400
  * [MDEV-369](https://jira.mariadb.org/browse/MDEV-369) (Mismatches in MySQL engines test suite)
  * Following reasons caused mismatches:
    * different handling of invalid values;
    * different CAST results with fractional seconds;
    * microseconds support in MariaDB;
    * different algorithm of comparing temporal values;
    * differences in error and warning texts and codes;
    * different approach to truncating datetime values to time;
    * additional collations;
    * different record order for queries without ORDER BY;
    * [MySQL Bug #66034](https://bugs.mysql.com/bug.php?id=66034).
  * More details in [MDEV-369](https://jira.mariadb.org/browse/MDEV-369) comments.
  * [Revision #3552.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3552.1.2)\
    Mon 2012-07-30 04:16:49 +0400
    * [MDEV-369](https://jira.mariadb.org/browse/MDEV-369) (Mismatches in MySQL engines test suite)
  * [Revision #3552.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3552.1.1)\
    Thu 2012-07-26 23:31:08 +0400
    * Result files were wrong due to MySQL bug#66034
* [Revision #3552](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3552)\
  Wed 2012-07-18 15:03:05 +0400
  * [MDEV-398](https://jira.mariadb.org/browse/MDEV-398): Sergv related to spacial queries
  * index\_merge/intersection is unable to work on GIS indexes, because:
    1. index scans have no Rowid-Ordered-Retrieval property
    2. When one does an index-only read over a GIS index, they do not\
       get the index tuple, because index only contains bounding box of the geometry.\
       This is why key\_copy() call crashed.
  * This patch fixes #1, which makes the problem go away. Theoretically, it would\
    be nice to check #2, too, but SE API semantics is not sufficiently precise to do it.
* [Revision #3551](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3551)\
  Tue 2012-06-26 21:43:34 +0300
  * Fix for [Bug #1007622](https://bugs.launchpad.net/bugs/1007622)
  * TABLE\_LIST::check\_single\_table made aware about fact that now if table attached to a merged view it can be (unopened) temporary table\
    (in 5.2 it was always leaf table or non (in case of several tables)).
* [Revision #3550](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3550) \[merge]\
  Sat 2012-06-23 15:00:05 -0700
  * Merge 5.2->5.3
  * [Revision #2732.57.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.9)\
    Sat 2012-06-23 12:19:07 -0700
    * Fixed bug [MDEV-360](https://jira.mariadb.org/browse/MDEV-360).
    * The bug was the result of the incomplete fix for bug lp bug 1008293.
  * [Revision #2732.57.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.8)\
    Mon 2012-06-18 22:32:17 -0700
    * Fixed bug [MDEV-354](https://jira.mariadb.org/browse/MDEV-354).
    * Virtual columns of ENUM and SET data types were not supported properly\
      in the original patch that introduced virtual columns into [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md).
    * The problem was that for any virtual column the patch used the\
      interval\_id field of the definition of the column in the frm file as\
      a reference to the virtual column expression.
    * The fix stores the optional interval\_id of the virtual column in the\
      extended header of the virtual column expression.
* [Revision #3549](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3549)\
  Fri 2012-06-22 14:14:22 +0400
  * Added comment about QUICK\_RANGE\_SELECT::free\_cond being unused.
* [Revision #3548](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3548)\
  Thu 2012-06-21 14:33:36 +0400
  * Update test results (checked)
* [Revision #3547](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3547)\
  Wed 2012-06-20 22:30:24 +0400
  * Update test results.
* [Revision #3546](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3546)\
  Wed 2012-06-20 13:41:31 +0400
  * Post-merge fixes:
    * put back the result encoding in func\_in.result (messed up by kdiff3)
    * update .result for other tests (checked)
* [Revision #3545](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3545) \[merge]\
  Mon 2012-06-18 22:38:11 +0400
  * Merge 5.2->5.3
  * [Revision #2732.57.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.7)\
    Tue 2012-06-12 10:06:26 -0700
    * Adjusted results in pbxt.negation\_elimination after the fix for lp bug 992380.
  * [Revision #2732.57.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.6) \[merge]\
    Tue 2012-06-12 00:09:20 -0700
    * Merge.
    * [Revision #2732.58.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.58.1)\
      Mon 2012-06-11 22:12:47 -0700
      * Fixed [Bug #1008293](https://bugs.launchpad.net/bugs/1008293).
        * One of the reported problems manifested itself in the scenario when one\
          thread tried to get statistics on a key cache while the second thread\
          had not finished initialization of the key cache structure yet.\
          The problem was resolved by forcing serialization of such operations\
          on key caches.
        *
        * To serialize function calls to perform certain operations over a key cache\
          a new mutex associated with the key cache now is used. It is stored in the\
          field op\_lock of the KEY\_CACHE structure. It is locked when the operation\
          is performed. Some of the serialized key cache operations utilize calls\
          for other key cache operations. To avoid recursive locking of op\_lock\
          the new functions that perform the operations of key cache initialization,\
          destruction and re-partitioning with an additional parameter were introduced.
        *
        * The parameter says whether the operation over op\_lock are to be performed or\
          are to be omitted. The old functions for the operations of key cache\
          initialization, destruction,and re-partitioning now just call the\
          corresponding new functions with the additional parameter set to true\
          requesting to use op\_lock while all other calls of these new function\
          have this parameter set to false.
        *
        * Another problem reported in the bug entry concerned the operation of\
          assigning an index to a key cache. This operation can be called\
          while the key cache structures are not initialized yet. In this\
          case any call of flush\_key\_blocks() should return without any actions.
        *
        * No test case is provided with this patch.
  * [Revision #2732.57.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.5) \[merge]\
    Sun 2012-06-10 14:04:21 +0400
    * Merge
  * [Revision #2732.57.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.4) \[merge]\
    Fri 2012-06-01 23:45:54 +0200
    * 5.1 merge
  * [Revision #2643.153.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.9)\
    Fri 2012-06-01 17:53:59 +0200
    * [MDEV-256](https://jira.mariadb.org/browse/MDEV-256) [Bug #995501](https://bugs.launchpad.net/bugs/995501) - mysqltest attempts to parse Perl code inside a block\
      with false condition, gets confused and throws wrong errors
  * [Revision #2732.57.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.3)\
    Fri 2012-05-25 10:29:53 +0300
    * Fix of [Bug #992380](https://bugs.launchpad.net/bugs/992380) + revise fix\_fields about missing with\_subselect collection
    * The problem is that some fix\_fields do not call Item\_func::fix\_fields and do not collect with subselect\_information.
  * [Revision #2732.57.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.2)\
    Wed 2012-05-23 18:18:08 +0300
    * Fix [Bug #1001506](https://bugs.launchpad.net/bugs/1001506)
    * This is a backport of the (unchaged) fix for MySQL bug #11764372, 57197.
    * Analysis:
      * When the outer query finishes its main execution and computes GROUP BY,\
        it needs to construct a new temporary table (and a corresponding JOIN) to\
        execute the last DISTINCT operation. At this point JOIN::exec calls\
        JOIN::join\_free, which calls JOIN::cleanup -> TMP\_TABLE\_PARAM::cleanup\
        for both the outer and the inner JOINs. The call to the inner\
        TMP\_TABLE\_PARAM::cleanup sets copy\_field = NULL, but not copy\_field\_end.
      *
      * The final execution phase that computes the DISTINCT invokes:\
        evaluate\_join\_record -> end\_write -> copy\_funcs\
        The last function copies the results of all functions into the temp table.\
        copy\_funcs walks over all functions in join->tmp\_table\_param.items\_to\_copy.\
        In this case items\_to\_copy contains both assignments to user variables.\
        The process of copying user variables invokes Item\_func\_set\_user\_var::check\
        which in turn re-evaluates the arguments of the user variable assignment.\
        This in turn triggers re-evaluation of the subquery, and ultimately\
        copy\_field.
      *
      * However, the previous call to TMP\_TABLE\_PARAM::cleanup for the subquery\
        already set copy\_field to NULL but not its copy\_field\_end. This results\
        in a null pointer access, and a crash.
      *
    * Fix:
      * Set copy\_field\_end and save\_copy\_field\_end to null when deleting\
        copy fields in TMP\_TABLE\_PARAM::cleanup().
  * [Revision #2732.57.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.1)\
    Tue 2012-05-22 08:48:10 +0300
    * Fix of [Bug #992380](https://bugs.launchpad.net/bugs/992380) + revise fix\_fields about missing with\_subselect collection
    * The problem is that some fix\_fields do not call Item\_func::fix\_fields and do not collect with subselect\_information.
* [Revision #3544](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3544)\
  Fri 2012-06-15 11:33:24 +0300
  * Fix [Bug #1008686](https://bugs.launchpad.net/bugs/1008686)
  * Analysis:
    * The fix for bug [Bug #985667](https://bugs.launchpad.net/bugs/985667) implements the method Item\_subselect::no\_rows\_in\_result()\
      for all main kinds of subqueries. The purpose of this method is to be called from\
      return\_zero\_rows() and set Items to some default value in the case when a query\
      returns no rows. Aggregates and subqueries require special treatment in this case.
    *
    * Every implementation of Item\_subselect::no\_rows\_in\_result() called\
      Item\_subselect::make\_const() to set the subquery predicate to its default value\
      irrespective of where the predicate was located in the query. Once the predicate\
      was set to a constant it was never executed.
    *
    * At the same time, the JOIN object of the fake select for UNIONs (the one used for\
      the final result of the UNION), was set after all subqueries in the union were\
      executed. Since we set the subquery as constant, it was never executed, and the\
      corresponding JOIN was never created.
    *
    * In order to decide whether the result of NOT IN is NULL or FALSE, Item\_in\_optimizer\
      needs to check if the subquery result was empty or not. This is where we got the\
      crash, because subselect\_union\_engine::no\_rows() checks for\
      unit->fake\_select\_lex->join->send\_records, and the join object was NULL.
    *
  * Solution:
    * If a subquery is in the HAVING clause it must be evaluated in order to know its\
      result, so that we can properly filter the result records. Once subqueries in the\
      HAVING clause are executed even in the case of no result rows, this specific\
      crash will be solved, because the UNION will be executed, and its JOIN will be\
      constructed. Therefore the fix for this crash is to narrow the fix for [Bug #985667](https://bugs.launchpad.net/bugs/985667),\
      and to apply Item\_subselect::no\_rows\_in\_result() only when the subquery predicate\
      is in the SELECT clause.
* [Revision #3543](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3543)\
  Thu 2012-06-14 17:03:09 +0300
  * Fix [Bug #1008773](https://bugs.launchpad.net/bugs/1008773)
  * Analysis:
    * Queries with implicit grouping (there is aggregate, but no group by)\
      follow some non-obvious semantics in the case of empty result set.\
      Aggregate functions produce some special "natural" value depending on\
      the function. For instance MIN/MAX return NULL, COUNT returns 0.
    *
    * The complexity comes from non-aggregate expressions in the select list.\
      If the non-aggregate expression is a constant, it can be computed, so\
      we should return its value, however if the expression is non-constant,\
      and depends on columns from the empty result set, then the only meaningful\
      value is NULL.
    *
    * The cause of the wrong result was that for subqueries the optimizer didn't\
      make a difference between constant and non-constant ones in the case of\
      empty result for implicit grouping.
  * Solution:
    * In all implementations of Item\_subselect::no\_rows\_in\_result() check if the\
      subquery predicate is constant. If it is constant, do not set it to the\
      default value for implicit grouping, instead let it be evaluated.
* [Revision #3542](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3542) \[merge]\
  Sun 2012-06-10 14:06:11 +0400
  * Merge
  * [Revision #3539.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3539.1.1) \[merge]\
    Sun 2012-06-10 13:53:06 +0400
    * Merge [Bug #1010351](https://bugs.launchpad.net/bugs/1010351) from 5.1 to 5.2
    * [Revision #2732.53.48](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.48)\
      Sun 2012-06-10 13:50:21 +0400
      * [Bug #1010351](https://bugs.launchpad.net/bugs/1010351): New "via" keyword in 5.2+ can't be used as identifier anymore
      * Add the VIA\_SYM token into keyword\_sp list, which makes it allowed for\
        use as keyword and SP label.
* [Revision #3541](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3541)\
  Fri 2012-06-08 19:15:01 +0200
  * [Bug #1008334](https://bugs.launchpad.net/bugs/1008334) : Speedup specific datetime queries that got slower with introduction of microseconds in 5.3
    * Item::get\_seconds() now skips decimal arithmetic, if decimals is 0. This significantly speeds up from\_unixtime() if no fractional part is passed.
    * replace sprintfs used to format temporal values by hand-coded formatting
  * Query1 (original query in the bug report)
    * BENCHMARK(10000000,DATE\_SUB(FROM\_UNIXTIME(RAND() \* 2147483648), INTERVAL (FLOOR(1 + RAND() \* 365)) DAY))
  * Query2 (Variation of query1 that does not use fractional part in FROM\_UNIXTIME parameter)
    * BENCHMARK(10000000,DATE\_SUB(FROM\_UNIXTIME(FLOOR(RAND() \* 2147483648)), INTERVAL (FLOOR(1 + RAND() \* 365)) DAY))
  * Prior to the patch, the runtimes were (32 bit compilation/AMD machine)
    * Query1: 41.53 sec
    * Query2: 23.90 sec
  * With the patch, the runtimes are
    * Query1: 32.32 sec (speed up due to removing sprintf)
    * Query2: 12.06 sec (speed up due to skipping decimal arithmetic)
* [Revision #3540](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3540)\
  Wed 2012-06-06 23:02:21 +0300
  * Fixed pbxt test case not run by default.
* [Revision #3539](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3539)\
  Tue 2012-06-05 17:25:10 +0300
  * Fixed [Bug #1000649](https://bugs.launchpad.net/bugs/1000649)
  * Analysis:
    * When the method JOIN::choose\_subquery\_plan() decided to apply\
      the IN-TO-EXISTS strategy, it set the unit and select\_lex\
      uncacheable flag to UNCACHEABLE\_DEPENDENT\_INJECTED unconditionally.
    *
    * As result, even if IN-TO-EXISTS injected non-correlated predicates,\
      the subquery was still treated as correlated.
  * Solution:
    * Set the subquery as correlated only if the injected predicate(s) depend\
      on the outer query.
* [Revision #3538](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3538)\
  Mon 2012-06-04 23:22:03 +0200
  * [MDEV-308](https://jira.mariadb.org/browse/MDEV-308) [Bug #1008516](https://bugs.launchpad.net/bugs/1008516) - Failing assertion: templ->mysql\_col\_len == len
  * remove the offending assert.
  * take the test case from [MySQL Bug #58015](https://bugs.mysql.com/bug.php?id=58015)
* [Revision #3537](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3537) \[merge]\
  Sat 2012-06-02 16:13:05 +0400
  * Merge
  * [Revision #3532.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3532.1.1)\
    Sat 2012-06-02 03:25:56 +0400
    * [Bug #1006164](https://bugs.launchpad.net/bugs/1006164): Multi-table DELETE that uses innodb + index\_merge/intersect may fail to delete rows
    * Set index columns to be read when using index\_merge, even if TABLE->no\_keyread is\
      set for the table (happens for multi-table UPDATEs)
* [Revision #3536](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3536)\
  Fri 2012-06-01 14:56:47 +0200
  * [MDEV-304](https://jira.mariadb.org/browse/MDEV-304): Insufficient buffer allocation for Query\_log\_event
  * The constructor for Query\_log\_event allocated 2 bytes too few for\
    extra space needed by Query cache. (Not sure if this is reproducible\
    in practice, as there are often a couple of extra bytes allocated\
    for unused string zero terminators, but better safe than sorry).
* [Revision #3535](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3535)\
  Wed 2012-05-30 19:10:18 +0300
  * Fix for [Bug #1006231](https://bugs.launchpad.net/bugs/1006231)
  * Analysis:
    * When a subquery that needs a temp table is executed during\
      the prepare or optimize phase of the outer query, at the end\
      of the subquery execution all the JOIN\_TABs of the subquery\
      are replaced by a new JOIN\_TAB that selects from the temp table.\
      However that temp table has no corresponding TABLE\_LIST.\
      Once EXPLAIN execution reaches its last phase, it tries to print\
      the names of the subquery tables through its TABLE\_LISTs, but in\
      the case of this bug there is no such TABLE\_LIST (it is NULL),\
      hence a crash.
  * Solution:
    * The fix is to block subquery evaluation inside\
      Item\_func\_like::fix\_fields and Item\_func\_like::select\_optimize()\
      using the Item::is\_expensive() test.
* [Revision #3534](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3534)\
  Tue 2012-05-29 09:59:25 +0500
  * [MDEV-294](https://jira.mariadb.org/browse/MDEV-294) SELECT WHERE ST\_CONTAINS doesn't return all the records where ST\_CONTAINS() is 1.
  * Optimizator fails using index with ST\_Within(g, constant\_poly).
  * per-file comments:
    * mysql-test/r/gis-rt-precise.result
      * test result fixed.
    * mysql-test/r/gis-rtree.result
      * test result fixed.
    * mysql-test/suite/maria/r/maria-gis-rtree-dynamic.result
      * test result fixed.
    * mysql-test/suite/maria/r/maria-gis-rtree-trans.result
      * test result fixed.
    * mysql-test/suite/maria/r/maria-gis-rtree.result
      * test result fixed.
    * storage/maria/ma\_rt\_index.c
      * Use MBR\_INTERSECT mode when optimizing the select WITH ST\_Within.
    * storage/myisam/rt\_index.c
      * Use MBR\_INTERSECT mode when optimizing the select WITH ST\_Within.
* [Revision #3533](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3533) \[merge]\
  Fri 2012-05-25 00:44:43 -0700
  * Merge.
  * [Revision #3531.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3531.1.1)\
    Fri 2012-05-25 00:07:26 -0700
    * Fixed a performance problem: calls of the function imerge\_list\_and\_tree\
      could lead an to exponential growth of the imerge lists.
* [Revision #3532](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3532)\
  Fri 2012-05-25 01:20:40 +0400
  * [Bug #1002630](https://bugs.launchpad.net/bugs/1002630): Valgrind warnings 'Invalid read' in subselect\_engine::calc\_const\_tables with SELECT
    * In JOIN::exec(), make the having->update\_used\_tables() call before we've\
      made the JOIN::cleanup(full=true) call. The latter frees SJ-Materialization\
      structures, which correlated subquery predicate items attempt to walk afterwards.
* [Revision #3531](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3531)\
  Wed 2012-05-23 21:05:53 +0400
  * Update test results after the latest push
* [Revision #3530](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3530)\
  Wed 2012-05-23 11:55:14 +0400
  * [Bug #1000051](https://bugs.launchpad.net/bugs/1000051): Query with simple join and ORDER BY takes thousands times longer when run with ICP
    * Correct testcases.
* [Revision #3529](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3529)\
  Wed 2012-05-23 11:46:40 +0400
  * [Bug #1000051](https://bugs.launchpad.net/bugs/1000051): Query with simple join and ORDER BY takes thousands times longer when run with ICP
    * Disable IndexConditionPushdown for reverse scans.
* [Revision #3528](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3528)\
  Tue 2012-05-22 15:22:55 +0300
  * Fix [Bug #1002079](https://bugs.launchpad.net/bugs/1002079)
  * Analysis:
    * The optimizer detects an empty result through constant table optimization.\
      Then it calls return\_zero\_rows(), which in turns calls inderctly\
      Item\_maxmin\_subselect::no\_rows\_in\_result(). The latter method set "value=0",\
      however "value" is pointer to Item\_cache, and not just an integer value.
    *   All of the Item\_\[maxmin | singlerow]\_subselect::val\_XXX methods does:

        ```
        if (forced_const)
        return value->val_real();
        ```
    * which of course crashes when value is a NULL pointer.
* Solution:
  * When the optimizer discovers an empty result set, set\
    Item\_singlerow\_subselect::value to a FALSE constant Item instead of NULL.
* [Revision #3527](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3527)\
  Mon 2012-05-21 19:37:46 +0500
  * [MDEV-136](https://jira.mariadb.org/browse/MDEV-136) Non-blocking "set read\_only".
  * Handle the 'set read\_only=1' in lighter way, than the FLUSH TABLES READ LOCK;
  * For the transactional engines we don't wait for operations on that tables to finish.
  * per-file comments:
    * mysql-test/r/read\_only\_innodb.result
      * [MDEV-136](https://jira.mariadb.org/browse/MDEV-136) Non-blocking "set read\_only".
        * test result updated.
    * mysql-test/t/read\_only\_innodb.test
      * [MDEV-136](https://jira.mariadb.org/browse/MDEV-136) Non-blocking "set read\_only".
        * test case added.
    * sql/mysql\_priv.h
      * [MDEV-136](https://jira.mariadb.org/browse/MDEV-136) Non-blocking "set read\_only".
        * The close\_cached\_tables\_set\_readonly() declared.
    * sql/set\_var.cc
      * [MDEV-136](https://jira.mariadb.org/browse/MDEV-136) Non-blocking "set read\_only".
        * Call close\_cached\_tables\_set\_readonly() for the read\_only::set\_var.
    * sql/sql\_base.cc
      * [MDEV-136](https://jira.mariadb.org/browse/MDEV-136) Non-blocking "set read\_only".
        * Parameters added to the close\_cached\_tables implementation,\
          close\_cached\_tables\_set\_readonly declared.
        * Prevent blocking on the transactional tables if the\
          set\_readonly\_mode is on.
* [Revision #3526](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3526) \[merge]\
  Sun 2012-05-20 14:57:29 +0200
  * 5.2 merge
  * [Revision #2732.53.47](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.47) \[merge]\
    Fri 2012-05-18 14:23:05 +0200
    * 5.1 merge
    * [Revision #2643.153.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.8)\
      Fri 2012-05-18 12:42:06 +0200
      * post-merge fixes
    * [Revision #2643.153.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.7) \[merge]\
      Thu 2012-05-17 12:12:33 +0200
      * merge with mysql-5.1.63
  * [Revision #2732.53.46](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.46)\
    Thu 2012-05-17 10:13:25 +0300
    * fix of [Bug #998321](https://bugs.launchpad.net/bugs/998321)
    * The problem is that we can't check null\_value field of non-basic constant without the item execution.:
* [Revision #3525](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3525) \[merge]\
  Fri 2012-05-18 16:28:11 +0400
  * Merge
  * [Revision #3522.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3522.1.1)\
    Fri 2012-05-18 16:24:12 +0400
    * [Bug #1000269](https://bugs.launchpad.net/bugs/1000269): Wrong result (extra rows) with semijoin+materialization, IN subqueries, join\_cache\_level>0
      * make make\_cond\_after\_sjm() correctly handle OR clauses where one branch refers to the semi-join table\
        while the other branch refers to the non-semijoin table.
* [Revision #3524](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3524)\
  Thu 2012-05-17 10:45:20 +0300
  * Test suite of fixed bug ([Bug #993459](https://bugs.launchpad.net/bugs/993459)).
* [Revision #3523](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3523)\
  Tue 2012-05-15 08:31:07 +0300
  * Fix for [Bug #998516](https://bugs.launchpad.net/bugs/998516)
  * If we did nothing in resolving unique table conflict we should not retry (it leed to infinite loop).
  * Now we retry (recheck) unique table check only in case if we materialized a table.
* [Revision #3522](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3522)\
  Sun 2012-05-13 13:15:17 +0400
  * [Bug #998236](https://bugs.launchpad.net/bugs/998236): Assertion failure or valgrind errors at best\_access\_path ...
  * Let fix\_semijoin\_strategies\_for\_picked\_join\_order() set\
    POSITION::prefix\_record\_count for POSITION records that it copies from\
    SJ\_MATERIALIZATION\_INFO::tables.
  * (These records do not have prefix\_record\_count set, because they are optimized\
    as joins-inside-semijoin-nests, without full advance\_sj\_state() processing).
* [Revision #3521](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3521) \[merge]\
  Sat 2012-05-12 12:27:26 +0400
  * Merge 5.2->5.3
  * [Revision #2732.53.45](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.45) \[merge]\
    Sat 2012-05-12 12:12:35 +0400
    * Merge 5.2->5.3
    * [Revision #2643.153.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.6)\
      Sat 2012-05-12 11:53:14 +0400
      * [Bug #997747](https://bugs.launchpad.net/bugs/997747): Assertion \`join->best\_read < ((double)1.79..5e+308L)' failed\
        in greedy\_search with LEFT JOINs and unique keys
      * Backport the fix for [Bug #806524](https://bugs.launchpad.net/bugs/806524) from [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)
* [Revision #3520](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3520) \[merge]\
  Fri 2012-05-11 11:40:23 +0300
  * Merge 5.2->5.3
  * [Revision #2732.53.44](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.44)\
    Fri 2012-05-11 09:35:46 +0300
    * fix for [Bug #994392](https://bugs.launchpad.net/bugs/994392)
    * The not\_null\_tables() of Item\_func\_not\_all and Item\_in\_optimizer was inherited from\
      Item\_func by mistake. It made the optimizer think that subquery\
      predicates with ALL/ANY/IN were null-rejecting. This could trigger invalid\
      conversions of outer joins into inner joins.
  * [Revision #2732.53.43](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.43)\
    Thu 2012-05-10 09:00:21 +0300
    * Fixed typo
  * [Revision #2732.53.42](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.42)\
    Tue 2012-05-08 12:38:22 +0200
    * [MDEV-262](https://jira.mariadb.org/browse/MDEV-262) : log\_state occationally fails in buildbot.
    * The failures are missing entries in the slow query log. The reason for\
      the failure are sleep() calls with short duration 10ms, which is less\
      than the default system timer resolution for various WaitForXXXObject\
      functions (15.6 ms) and thus can't work reliably.
    * The fix is to make sleeps tiny bit longer (20ms from 10ms) in the test.
  *   [Revision #2732.53.41](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.41)\
      Tue 2012-05-08 00:26:41 +0200

      * fixes [Bug #994156](https://bugs.launchpad.net/bugs/994156)
      * [MDEV-261](https://jira.mariadb.org/browse/MDEV-261) : mysqtest crashes when assigning variable to result of select , like

      ```
      let x = `SELECT <something>`
      ```

      * The fix is to detect the condition "no active connection", to report error and die.
      * Note, that the check for no active connection was already in place for ordinary commands,\
        and was missing only for assign-variable command.
* [Revision #2732.53.40](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.40)\
  Mon 2012-05-07 13:26:34 +0300
  * Fix for [Bug #993726](https://bugs.launchpad.net/bugs/993726)
  * Optimization of aggregate functions detected constant under max() and\
    evalueted it, but condition in the WHWRE clause (which is always FALSE) was\
    not taken into account
* [Revision #2732.53.39](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.39)\
  Mon 2012-05-07 11:02:58 +0300
  * Fix for bug [Bug #992405](https://bugs.launchpad.net/bugs/992405)
  *   The patch backports two patches from mysql 5.6:

      * BUG#12640437: USING SQL\_BUFFER\_RESULT RESULTS IN A DIFFERENT QUERY OUTPUT
      * Bug#12578908: SELECT SQL\_BUFFER\_RESULT OUTPUTS TOO MANY ROWS WHEN GROUP IS OPTIMIZED AWAY

      ```
      Original comment:
      -----------------
      3714 Jorgen Loland	2012-03-01
       BUG#12640437 - USING SQL_BUFFER_RESULT RESULTS IN A DIFFERENT 
       QUERY OUTPUT
       .
       For all but simple grouped queries, temporary tables are used to
       resolve grouping. In these cases, the list of grouping fields is
       stored in the temporary table and grouping is resolved
       there (e.g. by adding a unique constraint on the involved
       fields). Because of this, grouping is already done when the rows
       are read from the temporary table.
       .
       In the case where a group clause may be optimized away, grouping
       does not have to be resolved using a temporary table. However, if
       a temporary table is explicitly requested (e.g. because the
       SQL_BUFFER_RESULT hint is used, or the statement is
       INSERT...SELECT), a temporary table is used anyway. In this case,
       the temporary table is created with an empty group list (because
       the group clause was optimized away) and it will therefore not
       create groups. Since the temporary table does not take care of
       grouping, JOIN::group shall not be set to false in 
       make_simple_join(). This was fixed in bug 12578908. 
       .
       However, there is an exception where make_simple_join() should
       set JOIN::group to false even if the query uses a temporary table
       that was explicitly requested but is not strictly needed. That
       exception is if the loose index scan access method (explain
       says "Using index for group-by") is used to read into the 
       temporary table. With loose index scan, grouping is resolved 
       by the access method. This is exactly what happens in this bug.
      ```
* [Revision #2732.53.38](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.38)\
  Thu 2012-05-03 14:49:52 +0300
  * Fix [Bug #993745](https://bugs.launchpad.net/bugs/993745)
  * This is a backport of the fix for MySQL bug #13723054 in 5.6.
  *   Original comment:

      ```
      The crash is caused by arbitrary memory area owerwriting in case of
      BLOB fields during attempt to copy BLOB field key image into record
      buffer(record buffer is too small to get BLOB key part image).
      note:
      QUICK_GROUP_MIN_MAX_SELECT can not work with BLOB fields
      because it uses record buffer as temporary buffer for key values
      however this case is filtered out by covering_keys() check
      in get_best_group_min_max() as BLOBs always require key length
      modificator in the key declaration and if the key has a BLOB
      then it can not be covered key.
      The fix is to use 'max_used_key_length' key length instead of 0.
      ```
* Analysis:
  * Spcifically the crash in this bug was a result of the call to key\_copy()\
    that copied the whole key, inlcuding the BLOB field which is not used\
    for index access. Copying the blob field overwrote memory as far as the\
    function parameter 'key\_info'. As a result the contents of key\_info was\
    all 0, which resulted in a crash when this key\_info was accessed few\
    lines below in key\_cmp().
* [Revision #3519](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3519)\
  Tue 2012-05-08 20:58:41 +0300
  * Fix compiler warnings.
* [Revision #3518](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3518)\
  Tue 2012-05-08 19:13:26 +0300
  * Addition to the fix to [Bug #994275](https://bugs.launchpad.net/bugs/994275).
  * It is problem of constant propagated to ref\* access method (the problem was hiden by using debug binaries for testing).
* [Revision #3517](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3517)\
  Mon 2012-05-07 21:14:37 +0300
  * [Bug #994275](https://bugs.launchpad.net/bugs/994275) fix.
  * In 5.3 we substitute constants in ref access values it can't be null so we do not need add NOT NULL for early NULL filtering.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
