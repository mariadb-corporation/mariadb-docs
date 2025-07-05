# MariaDB 5.5.25 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.25) |[Release Notes](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5525-release-notes.md) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 22 Jun 2012

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5525-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3455](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3455)\
  Thu 2012-06-21 21:17:34 +0200
  * [MDEV-342](https://jira.mariadb.org/browse/MDEV-342): Do not mark old binlog file as cleanly closed during rotate until\
    the new file is fully synced to disk and binlog index. This fixes a window\
    where a crash would leave next server restart unable to detect that a crash\
    occured, causing recovery to fail.
* [Revision #3454](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3454)\
  Thu 2012-06-21 19:02:53 +0200
  * [MDEV-359](https://jira.mariadb.org/browse/MDEV-359): Fix another case where switch-off semisync could cause a race that ended with server crash.
  * This one was when the code releases and reaquires the lock with pthread\_cond\_wait() - and semisync is switched off meanwhile.
* [Revision #3453](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3453)\
  Thu 2012-06-21 17:39:21 +0200
  * Use the portable form of INSTALL PLUGIN in rpl\_mdev359.test
* [Revision #3452](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3452)\
  Thu 2012-06-21 14:00:19 +0200
  * fixing the order of includes in the rpl\_mdev359.test
* [Revision #3451](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3451)\
  Thu 2012-06-21 11:52:54 +0200
  * [MDEV-359](https://jira.mariadb.org/browse/MDEV-359): Server crash when SET GLOBAL rpl\_semi\_sync\_master\_enabled = OFF
  * The semisync code does a fast-but-unsafe check for enabled or not without lock,\
    followed by a slow-but-safe check under lock. However, if the slow check failed,\
    the code still referenced not valid data (in an assert() expression), causing a\
    crash.
  * Fixed by not running the incorrect assert when semisync is disabled.
* [Revision #3450](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3450)\
  Thu 2012-06-21 11:26:53 +0200
  * [MDEV-349](https://jira.mariadb.org/browse/MDEV-349) 5.5 xtradb innodb\_prefix\_index\_liftedlimit crash with valgrind
  * This is XtraDB bug [Bug #1015109](https://bugs.launchpad.net/bugs/1015109), introduced by innodb\_split\_buf\_pool\_mutex.patch
  * Comment the offending assertion, until the fixed XtraDB is available
* [Revision #3449](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3449)\
  Thu 2012-06-21 00:49:24 +0200
  * [MDEV-361](https://jira.mariadb.org/browse/MDEV-361) - Fix handle leak in os\_thread\_create (Windows)
* [Revision #3448](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3448)\
  Wed 2012-06-20 14:23:23 +0200
  * Fix memory leak introduced with merge of mysql 5.5.
  * MySQL introduced a class Deferred\_log\_events. This class keeps a pointer\
    last\_added. The code was keeping this pointer around even after the memory\
    pointed to was freed, and later comparing the bogus pointer against other\
    allocated memory. This is illegal, and can randomly produce false equal\
    comparisons depending on whatever the malloc() subsystem decides to return.
* [Revision #3447](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3447) \[merge]\
  Wed 2012-06-20 14:50:44 +0300
  * Automatic merge
  * [Revision #3445.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3445.1.1)\
    Wed 2012-06-20 14:37:37 +0300
    * Fixed [MDEV-348](https://jira.mariadb.org/browse/MDEV-348): 5.5 valgrind warinings on maria tests
* [Revision #3446](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3446) \[merge]\
  Wed 2012-06-20 15:01:28 +0400
  * Merge 5.3 -> 5.5
  * [Revision #2502.561.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.7)\
    Wed 2012-06-20 13:41:31 +0400
    * Post-merge fixes:
      * put back the result encoding in func\_in.result (messed up by kdiff3)
      * update .result for other tests (checked)
  * [Revision #2502.561.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.6) \[merge]\
    Mon 2012-06-18 22:38:11 +0400
    * Merge 5.2->5.3
    * [Revision #2502.562.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.562.7)\
      Tue 2012-06-12 10:06:26 -0700
      * Adjusted results in pbxt.negation\_elimination after the fix for lp bug 992380.
    * [Revision #2502.562.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.562.6) \[merge]\
      Tue 2012-06-12 00:09:20 -0700
      * Merge.
      * [Revision #2502.563.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.563.1)\
        Mon 2012-06-11 22:12:47 -0700
        * Fixed [Bug #1008293](https://bugs.launchpad.net/bugs/1008293).
        * One of the reported problems manifested itself in the scenario when one\
          thread tried to get statistics on a key cache while the second thread\
          had not finished initialization of the key cache structure yet.\
          The problem was resolved by forcing serialization of such operations\
          on key caches.
        * To serialize function calls to perform certain operations over a key cache\
          a new mutex associated with the key cache now is used. It is stored in the\
          field op\_lock of the KEY\_CACHE structure. It is locked when the operation\
          is performed. Some of the serialized key cache operations utilize calls\
          for other key cache operations. To avoid recursive locking of op\_lock\
          the new functions that perform the operations of key cache initialization,\
          destruction and re-partitioning with an additional parameter were introduced.\
          The parameter says whether the operation over op\_lock are to be performed or\
          are to be omitted. The old functions for the operations of key cache\
          initialization, destruction,and re-partitioning now just call the\
          corresponding new functions with the additional parameter set to true\
          requesting to use op\_lock while all other calls of these new function\
          have this parameter set to false.
        * Another problem reported in the bug entry concerned the operation of\
          assigning an index to a key cache. This operation can be called\
          while the key cache structures are not initialized yet. In this\
          case any call of flush\_key\_blocks() should return without any actions.
        * No test case is provided with this patch.
    * [Revision #2502.562.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.562.5) \[merge]\
      Sun 2012-06-10 14:04:21 +0400
      * Merge
    * [Revision #2502.562.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.562.4) \[merge]\
      Fri 2012-06-01 23:45:54 +0200
      * 5.1 merge
      * [Revision #2502.554.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.554.9)\
        Fri 2012-06-01 17:53:59 +0200
        * [MDEV-256](https://jira.mariadb.org/browse/MDEV-256) [Bug #995501](https://bugs.launchpad.net/bugs/995501) - mysqltest attempts to parse Perl code inside a block\
          with false condition, gets confused and throws wrong errors
    * [Revision #2502.562.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.562.3)\
      Fri 2012-05-25 10:29:53 +0300
      * Fix of [Bug #992380](https://bugs.launchpad.net/bugs/992380) + revise fix\_fields about missing with\_subselect collection
      * The problem is that some fix\_fields do not call Item\_func::fix\_fields and do not collect with subselect\_information.
    * [Revision #2502.562.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.562.2)\
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
    * [Revision #2502.562.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.562.1)\
      Tue 2012-05-22 08:48:10 +0300
      * Fix of [Bug #992380](https://bugs.launchpad.net/bugs/992380) + revise fix\_fields about missing with\_subselect collection
      * The problem is that some fix\_fields do not call Item\_func::fix\_fields and do not collect with subselect\_information.
* [Revision #3445](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3445) \[merge]\
  Tue 2012-06-19 15:06:45 +0300
  * Merged the fix for bug [Bug #944706](https://bugs.launchpad.net/bugs/944706), [MDEV-193](https://jira.mariadb.org/browse/MDEV-193)
  * [Revision #3434.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3434.2.1) \[merge]\
    Thu 2012-06-14 23:55:22 +0300
    * Merge the fix for [Bug #944706](https://bugs.launchpad.net/bugs/944706), [MDEV-193](https://jira.mariadb.org/browse/MDEV-193)
    * [Revision #3428.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3428.1.1) \[merge]\
      Wed 2012-06-06 22:26:40 +0300
      * Merge the fix for [Bug #944706](https://bugs.launchpad.net/bugs/944706), [MDEV-193](https://jira.mariadb.org/browse/MDEV-193)
      * [Revision #3402.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3402.1.5)\
        Fri 2012-06-01 14:10:15 +0300
        * Fixed bug [MDEV-288](https://jira.mariadb.org/browse/MDEV-288)
        * CHEAP SQ: Valgrind warnings "Memory lost" with IN and EXISTS nested subquery, materialization+semijoin
        * Analysis:
          * The memory leak was a result of the interaction of semi-join optimization\
            with early optimization of constant subqueries. The function:\
            setup\_jtbm\_semi\_joins() created a dummy temporary table "dummy\_table"\
            in order to make some JOIN\_TAB objects complete. Normally, such temporary\
            tables are freed inside JOIN\_TAB::cleanup.
          *
          * However, the inner-most subquery is pre-optimized, which allows the\
            optimization fo the MAX subquery to determine that its WHERE is TRUE,\
            and thus to compute the result of the MAX during optimization. This\
            ultimately allows the optimize phase of the outer query to find that\
            it WHERE clause is FALSE. Once JOIN::optimize finds that the result\
            set is empty, it sets zero\_result\_cause, and returns _before_ it ever\
            reached make\_join\_statistics(). As a result the query plan has no\
            JOIN\_TABs at all. Since the temporary table is supposed to be cleanup\
            via JOIN\_TAB::cleanup, this never happens because there is no JOIN\_TAB\
            for this table. Hence we get a memory leak.
          *
        * Solution:
          * Whenever there are no JOIN\_TABs, iterate over all table reference in\
            JOIN::join\_list, and free the ones that contain semi-join temporary\
            tables.
      * [Revision #3402.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3402.1.4)\
        Wed 2012-05-30 00:18:53 +0300
        * Patch for [MDEV-287](https://jira.mariadb.org/browse/MDEV-287): CHEAP SQ: A query with subquery in SELECT list, EXISTS, inner joins takes hundreds times longer
        * Analysis:
          * The fix for [Bug #944706](https://bugs.launchpad.net/bugs/944706) introduces early subquery optimization.\
            While a subquery is being optimized some of its predicates may be\
            removed. In the test case, the EXISTS subquery is constant, and is\
            evaluated to TRUE. As a result the whole OR is TRUE, and thus the\
            correlated condition "b = alias1.b" is optimized away. The subquery\
            becomes non-correlated.
          *
          * The subquery cache is designed to work only for correlated subqueries.\
            If constant subquery optimization is disallowed, then the constant\
            subquery is not evaluated, the subquery remains correlated, and its\
            execution is cached. As a result execution is fast.
          *
          * However, when the constant subquery was optimized away, it was neither\
            cached by the subquery cache, nor it was cached by the internal subquery\
            caching. The latter was due to the fact that the subquery still appeared\
            as correlated to the subselect\_XYZ\_engine::exec methods, and they\
            re-executed the subquery on each call to Item\_subselect::exec.
          *
        * Solution:
          * The solution is to update the correlated status of the subquery after it has\
            been optimized. This status consists of:
          *
            * st\_select\_lex::is\_correlated
            * Item\_subselect::is\_correlated
            * SELECT\_LEX::uncacheable
            * SELECT\_LEX\_UNIT::uncacheable
          *
          * The status is updated by st\_select\_lex::update\_correlated\_cache(), and its\
            caller st\_select\_lex::optimize\_unflattened\_subqueries. The solution relies\
            on the fact that the optimizer already called\
            st\_select\_lex::update\_used\_tables() for each subquery. This allows to\
            efficiently update the correlated status of each subquery without walking\
            the whole subquery tree.
          *
          * Notice that his patch is an improvement over MySQL 5.6 and older, where\
            subqueries are not pre-optimized, and the above analysis is not possible.
      * [Revision #3402.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3402.1.3)\
        Thu 2012-05-24 14:08:28 +0300
        * Test case for [Bug #1001117](https://bugs.launchpad.net/bugs/1001117), MySQL BUG#12330344
        * Analysis:
          * The problem in the original MySQL bug is that the range optimizer\
            performs its analysis in a separate MEM\_ROOT object that is freed\
            after the range optimzier is done. During range analysis get\_mm\_tree\
            calls Item\_func\_like::select\_optimize, which in turn evaluates its\
            right argument. In the test case the right argument is a subquery.
          *
          * In MySQL, subqueries are optimized lazyly, thus the call to val\_str\
            triggers optimization for the subquery. All objects needed by the\
            subquery plan end up in the temporary MEM\_ROOT used by the range\
            optimizer. When execution ends, the JOIN::cleanup process tries to\
            cleanup objects of the subquery plan, but all these objects are gone\
            with the temporary MEM\_ROOT. The solution for MySQL is to switch the\
            mem\_root.
          *
          * In MariaDB with the patch for bug [Bug #944706](https://bugs.launchpad.net/bugs/944706), all constant subqueries\
            that may be used by the optimization process are preoptimized. Therefore\
            Item\_func\_like::select\_optimize only triggers subquery execution, and\
            the above problem is not present.
          *
          * The patch however adds a test whether the evaluated right argument of\
            the LIKE predicate is expensive. This is consistent with our approach\
            not to evaluate expensive expressions during optimization.
      * [Revision #3402.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3402.1.2)\
        Fri 2012-05-18 14:52:01 +0300
        * Fixed bug [MDEV-277](https://jira.mariadb.org/browse/MDEV-277) as part of the fix for [Bug #944706](https://bugs.launchpad.net/bugs/944706)
        * The cause for this bug is that the method JOIN::get\_examined\_rows iterates over all\
          JOIN\_TABs of the join assuming they are just a sequence. In the query above, the\
          innermost subquery is merged into its parent query. When we call\
          JOIN::get\_examined\_rows for the second-level subquery, the iteration that\
          assumes sequential order of join tabs goes outside the join\_tab array and calls\
          the method JOIN\_TAB::get\_examined\_rows on uninitialized memory.
        * The fix is to iterate over JOIN\_TABs in a way that takes into account the nested\
          semi-join structure of JOIN\_TABs. In particular iterate as select\_describe.
      * [Revision #3402.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3402.1.1)\
        Thu 2012-05-17 13:46:05 +0300
        * Fix for bug [Bug #944706](https://bugs.launchpad.net/bugs/944706), task [MDEV-193](https://jira.mariadb.org/browse/MDEV-193)
        * The patch enables back constant subquery execution during\
          query optimization after it was disabled during the development\
          of [MWL#89](https://askmonty.org/worklog/?tid=89) (cost-based choice of IN-TO-EXISTS vs MATERIALIZATION).
        * The main idea is that constant subqueries are allowed to be executed\
          during optimization if their execution is not expensive.
        * The approach is as follows:
          * Constant subqueries are recursively optimized in the beginning of\
            JOIN::optimize of the outer query. This is done by the new method\
            JOIN::optimize\_constant\_subqueries(). This is done so that the cost\
            of executing these queries can be estimated.
          *
          * Optimization of the outer query proceeds normally. During this phase\
            the optimizer may request execution of non-expensive constant subqueries.\
            Each place where the optimizer may potentially execute an expensive\
            expression is guarded with the predicate Item::is\_expensive().
          *
          * The implementation of Item\_subselect::is\_expensive has been extended\
            to use the number of examined rows (estimated by the optimizer) as a\
            way to determine whether the subquery is expensive or not.
          *
          * The new system variable "expensive\_subquery\_limit" controls how many\
            examined rows are considered to be not expensive. The default is 100.
          *
        * In addition, multiple changes were needed to make this solution work\
          in the light of the changes made by [MWL#89](https://askmonty.org/worklog/?tid=89). These changes were needed\
          to fix various crashes and wrong results, and legacy bugs discovered\
          during development.
* [Revision #3444](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3444)\
  Mon 2012-06-18 17:29:05 -0400
  * fixed some urls that the previous update missed
* [Revision #3443](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3443)\
  Mon 2012-06-18 16:57:58 -0400
  * various documentation updates
* [Revision #3442](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3442) \[merge]\
  Mon 2012-06-18 16:50:16 +0400
  * 5.3->5.5 merge
  * [Revision #2502.561.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.5)\
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
  * [Revision #2502.561.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.4)\
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
      *
    * Solution:
      * In all implementations of Item\_subselect::no\_rows\_in\_result() check if the\
        subquery predicate is constant. If it is constant, do not set it to the\
        default value for implicit grouping, instead let it be evaluated.
  * [Revision #2502.561.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.3) \[merge]\
    Sun 2012-06-10 14:06:11 +0400
    * Merge
* [Revision #3441](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3441)\
  Mon 2012-06-18 14:26:36 +0200
  * [MDEV-346](https://jira.mariadb.org/browse/MDEV-346): 5.5 upgrade test fails on precise.
  * Attempt to make it easier to upgrade mysql->mariadb on Ubuntu precise.\
    It looks like we were missing conflicts: and replaces: on packages\
    mysql-server-5.5 and mysql-client-5.5.
* [Revision #3440](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3440)\
  Sun 2012-06-17 16:09:16 +0200
  * fix an overly agressive optimization in Item\_func\_conv\_charset
* [Revision #3439](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3439)\
  Sat 2012-06-16 14:58:00 +0200
  * fix innodb\_bug12902967 to pass when aio check on /dev/shm fails
* [Revision #3438](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3438) \[merge]\
  Sat 2012-06-16 09:03:07 +0200
  * merge
  * [Revision #3433.2.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3433.2.8)\
    Fri 2012-06-15 17:22:49 +0200
    * [MDEV-316](https://jira.mariadb.org/browse/MDEV-316) [Bug #1009085](https://bugs.launchpad.net/bugs/1009085) Assertion failed: warn\_item, file item\_cmpfunc.cc, line 3613
    * make sure that find\_date\_time\_item() is called before agg\_arg\_charsets\_for\_comparison().
    * optimize Item\_func\_conv\_charset to avoid conversion if no string result is needed
  * [Revision #3433.2.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3433.2.7) \[merge]\
    Fri 2012-06-15 14:54:23 +0200
    * merged with XtraDB 1.1.8-26.0
    * [Revision #0.12.53](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.53)\
      Fri 2012-06-15 10:23:33 +0200
      * XtraDB 1.1.8-20.1 from\
        Percona-Server 5.5.24-rel26.0
  * [Revision #3433.2.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3433.2.6)\
    Fri 2012-06-15 10:26:06 +0200
    * comments
  * [Revision #3433.2.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3433.2.5) \[merge]\
    Thu 2012-06-14 20:05:31 +0200
    * mysql-5.5 merge
  * [Revision #3433.2.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3433.2.4)\
    Fri 2012-06-08 14:50:50 +0200
    * apply mysql fix for bug#58421 to XtraDB
  * [Revision #3433.2.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3433.2.3)\
    Thu 2012-06-07 19:15:41 +0200
    * client's option is default-character-set, server's is character-set-server
  * [Revision #3433.2.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3433.2.2)\
    Wed 2012-06-06 16:41:13 +0200
    * fixes for bintar mtr failures:
      * look for plugins in the correct path.
      * skip `--plugin-load` if it has the empty soname part, not only if the whole argument is empty.
  * [Revision #3433.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3433.2.1)\
    Wed 2012-06-06 14:15:29 +0200
    * [MDEV-302](https://jira.mariadb.org/browse/MDEV-302) [Bug #988204](https://bugs.launchpad.net/bugs/988204) [MariaDB 5.5.23](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5523-release-notes.md) binaries don't use libaio
    * simplify debian/dist/\*/rules slightly.
    * move hard-coded config value to cmake files.
    * (the actual fix is -DBUILD\_CONFIG=mysql\_release)
* [Revision #3437](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3437) \[merge]\
  Fri 2012-06-15 18:32:04 +0200
  * merge
  * [Revision #3433.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3433.1.1)\
    Fri 2012-06-15 17:21:06 +0200
    * [MDEV-339](https://jira.mariadb.org/browse/MDEV-339), [Bug #1001340](https://bugs.launchpad.net/bugs/1001340) - system\_time\_zone is wrong on Windows
    * On localized Windows versions, Windows uses localized time zone names and contain non-ASCII characters. non-ASCII characters appear broken when displayed by clients
    * The fix is to declare system\_time\_zone variable to have UTF8 encoding and to convert tzname to UTF8.
* [Revision #3436](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3436) \[merge]\
  Fri 2012-06-15 13:39:07 +0300
  * Automatic merge
  * [Revision #3434.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3434.1.3)\
    Fri 2012-06-15 13:36:34 +0300
    * Removed one variable from the test output that was depending on timing.
  * [Revision #3434.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3434.1.2)\
    Fri 2012-06-15 13:08:10 +0300
    * Fix for: [Bug #1013432](https://bugs.launchpad.net/bugs/1013432) and MySQL#64800:
    * mysqldump with `--include-master-host-port` putting quotes around port number
    * Patch from Stewart Smith
  * [Revision #3434.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3434.1.1)\
    Fri 2012-06-15 12:52:58 +0300
    * Fixed [MDEV-306](https://jira.mariadb.org/browse/MDEV-306) / [Bug #1007967](https://bugs.launchpad.net/bugs/1007967) - Assertion \`table->file->stats.records > 0 || error' failed join\_read\_const\_table on concurrent SELECT and DROP/ADD INDEX
* [Revision #3435](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3435)\
  Fri 2012-06-15 00:01:20 -0700
  * Fixed [Bug #1002157](https://bugs.launchpad.net/bugs/1002157).
  * The class Item\_func missed an implementation of the virtual\
    function update\_null\_value.
  * Back-ported the fix for bug 62125 from mysql 5.6 code line.
  * The test case was also back-ported.
* [Revision #3434](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3434) \[merge]\
  Wed 2012-06-13 16:28:47 -0700
  * Merge.
  * [Revision #3426.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3426.1.1)\
    Fri 2012-06-08 22:15:49 -0700
    * Fixed [Bug #1010729](https://bugs.launchpad.net/bugs/1010729).
    * The bug prevented acceptance of UNION queries whose non-first select\
      clauses contained join expressions with degenerated single-table nests\
      as valid queries.
    * The bug was introduced into mysql-5.5 code line by the patch for\
      bug 33204.
* [Revision #3433](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3433) \[merge]\
  Wed 2012-06-13 11:37:51 +0200
  * merge
  * [Revision #2502.561.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.2)\
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
  * [Revision #2502.561.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.1)\
    Wed 2012-06-06 23:02:21 +0300
    * Fixed pbxt test case not run by default.
* [Revision #3432](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3432) \[merge]\
  Sun 2012-06-10 14:12:50 +0400
  * Merge BUG#1010351 from 5.2 to 5.5
  * [Revision #2502.546.80](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.80) \[merge]\
    Sun 2012-06-10 13:53:06 +0400
    * Merge BUG#1010351 from 5.1 to 5.2
    * [Revision #2502.528.48](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.48)\
      Sun 2012-06-10 13:50:21 +0400
      * [Bug #1010351](https://bugs.launchpad.net/bugs/1010351): New "via" keyword in 5.2+ can't be used as identifier anymore
      * Add the VIA\_SYM token into keyword\_sp list, which makes it allowed for\
        use as keyword and SP label.
* [Revision #3431](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3431)\
  Fri 2012-06-08 22:13:38 +0300
  * Moved init\_log() to be later to not write log entries when one uses `--example`
* [Revision #3430](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3430)\
  Fri 2012-06-08 22:12:44 +0300
  * Changed last\_insert\_id() to be unsigned.
  * Fixed [MDEV-331](https://jira.mariadb.org/browse/MDEV-331): last\_insert\_id() returns a signed number
* [Revision #3429](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3429)\
  Fri 2012-06-08 11:18:56 +0200
  * [MDEV-329](https://jira.mariadb.org/browse/MDEV-329): [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) does not use fdatasync().
  * The `--debug-no-sync` incorrectly defaulted to ON, disabling sync calls\
    by default which can loose data or cause corruption. Also, the code\
    used fsync() instead of the sometimes more efficient fdatasync().
* [Revision #3428](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3428) \[merge]\
  Wed 2012-06-06 16:19:48 +0300
  * Merge
  * [Revision #2502.546.79](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.79)\
    Tue 2012-06-05 17:25:10 +0300
    * Fixed [Bug #1000649](https://bugs.launchpad.net/bugs/1000649)
    * Analysis:
      * When the method JOIN::choose\_subquery\_plan() decided to apply\
        the IN-TO-EXISTS strategy, it set the unit and select\_lex\
        uncacheable flag to UNCACHEABLE\_DEPENDENT\_INJECTED unconditionally.
      *
      * As result, even if IN-TO-EXISTS injected non-correlated predicates,\
        the subquery was still treated as correlated.
      *
    * Solution:
      * Set the subquery as correlated only if the injected predicate(s) depend\
        on the outer query.
  * [Revision #2502.546.78](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.78)\
    Mon 2012-06-04 23:22:03 +0200
    * [MDEV-308](https://jira.mariadb.org/browse/MDEV-308) / [Bug #1008516](https://bugs.launchpad.net/bugs/1008516) - Failing assertion: templ->mysql\_col\_len == len
    * remove the offending assert.
    * take the test case from mysql Bug#58015
* [Revision #3427](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3427) \[merge]\
  Wed 2012-06-06 14:06:13 +0200
  * merge
  * [Revision #3425.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3425.1.2)\
    Mon 2012-06-04 17:39:28 +0200
    * [MDEV-136](https://jira.mariadb.org/browse/MDEV-136) Non-blocking "set read\_only"
    * backport dmitry.shulga@oracle.com-20120209125742-w7hdxv0103ymb8ko from mysql-trunk:
      * Patch for bug#11764747 (formerly known as 57612): SET GLOBAL READ\_ONLY=1 cannot\
        progress when a table is locked with LOCK TABLES.
      *
      * The reason for the bug was that mysql server makes a flush of all open tables\
        during handling of statement 'SET GLOBAL READ\_ONLY=1'. Therefore if some of\
        these tables were locked by "LOCK TABLE ... READ" from a different connection,\
        then execution of statement 'SET GLOBAL READ\_ONLY=1' would be waiting for\
        the lock for such table even if the table was locked in a compatible read mode.
      *
      * Flushing of all open tables before setting of read\_only system variable\
        is inherited from 5.1 implementation since this was the only possible approach\
        to ensure that there isn't any pending write operations on open tables.
      *
      * Start from version 5.5 and above such behaviour is guaranteed by the fact\
        that we acquire global\_read\_lock before setting read\_only flag. Since\
        acquiring of global\_read\_lock is successful only when there isn't any\
        active write operation then we can remove flushing of open tables from\
        processing of SET GLOBAL READ\_ONLY=1.
      *
      * This modification changes the server behavior so that read locks held\
        by other connections (LOCK TABLE ... READ) no longer will block attempts\
        to enable read\_only.
  * [Revision #3425.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3425.1.1) \[merge]\
    Mon 2012-06-04 17:26:11 +0200
    * merge with 5.3.
    * Take only test cases from [MDEV-136](https://jira.mariadb.org/browse/MDEV-136) Non-blocking "set read\_only"
    * [Revision #2502.546.77](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.77) \[merge]\
      Sat 2012-06-02 16:13:05 +0400
      * Merge
      * [Revision #2502.560.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.560.1)\
        Sat 2012-06-02 03:25:56 +0400
        * [Bug #1006164](https://bugs.launchpad.net/bugs/1006164): Multi-table DELETE that uses innodb + index\_merge/intersect may fail to delete rows
        * Set index columns to be read when using index\_merge, even if TABLE->no\_keyread is\
          set for the table (happens for multi-table UPDATEs)
    * [Revision #2502.546.76](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.76)\
      Fri 2012-06-01 14:56:47 +0200
      * [MDEV-304](https://jira.mariadb.org/browse/MDEV-304): Insufficient buffer allocation for Query\_log\_event
      * The constructor for Query\_log\_event allocated 2 bytes too few for\
        extra space needed by Query cache. (Not sure if this is reproducible\
        in practice, as there are often a couple of extra bytes allocated\
        for unused string zero terminators, but better safe than sorry).
    * [Revision #2502.546.75](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.75)\
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
        *
      * Solution:
        * The fix is to block subquery evaluation inside\
          Item\_func\_like::fix\_fields and Item\_func\_like::select\_optimize()\
          using the Item::is\_expensive() test.
    * [Revision #2502.546.74](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.74)\
      Tue 2012-05-29 09:59:25 +0500
      * [MDEV-294](https://jira.mariadb.org/browse/MDEV-294) SELECT WHERE ST\_CONTAINS doesn't return all the records where ST\_CONTAINS() is 1.\
        Optimizator fails using index with ST\_Within(g, constant\_poly).
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
    * [Revision #2502.546.73](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.73) \[merge]\
      Fri 2012-05-25 00:44:43 -0700
      * Merge.
      * [Revision #2502.559.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.559.1)\
        Fri 2012-05-25 00:07:26 -0700
        * Fixed a performance problem: calls of the function imerge\_list\_and\_tree\
          could lead an to exponential growth of the imerge lists.
    * [Revision #2502.546.72](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.72)\
      Fri 2012-05-25 01:20:40 +0400
      * [Bug #1002630](https://bugs.launchpad.net/bugs/1002630): Valgrind warnings 'Invalid read' in subselect\_engine::calc\_const\_tables with SELECT
      * In JOIN::exec(), make the having->update\_used\_tables() call before we've\
        made the JOIN::cleanup(full=true) call. The latter frees SJ-Materialization\
        structures, which correlated subquery predicate items attempt to walk afterwards.
    * [Revision #2502.546.71](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.71)\
      Wed 2012-05-23 21:05:53 +0400
      * Update test results after the latest push
    * [Revision #2502.546.70](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.70)\
      Wed 2012-05-23 11:55:14 +0400
      * [Bug #1000051](https://bugs.launchpad.net/bugs/1000051): Query with simple join and ORDER BY takes thousands times longer when run with ICP
      * Correct testcases.
    * [Revision #2502.546.69](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.69)\
      Wed 2012-05-23 11:46:40 +0400
      * [Bug #1000051](https://bugs.launchpad.net/bugs/1000051): Query with simple join and ORDER BY takes thousands times longer when run with ICP
      * Disable IndexConditionPushdown for reverse scans.
    * [Revision #2502.546.68](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.68)\
      Tue 2012-05-22 15:22:55 +0300
      * Fix [Bug #1002079](https://bugs.launchpad.net/bugs/1002079)
      * Analysis:
        * The optimizer detects an empty result through constant table optimization.\
          Then it calls return\_zero\_rows(), which in turns calls inderctly\
          Item\_maxmin\_subselect::no\_rows\_in\_result(). The latter method set "value=0",\
          however "value" is pointer to Item\_cache, and not just an integer value.
        *
        * All of the Item\_\[maxmin | singlerow]\_subselect::val\_XXX methods does:
        *
          * if (forced\_const)
            * return value->val\_real();
        *
        * which of course crashes when value is a NULL pointer.
        *
      * Solution:
        * When the optimizer discovers an empty result set, set\
          Item\_singlerow\_subselect::value to a FALSE constant Item instead of NULL.
    * [Revision #2502.546.67](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.67)\
      Mon 2012-05-21 19:37:46 +0500
      * [MDEV-136](https://jira.mariadb.org/browse/MDEV-136) Non-blocking "set read\_only".
      * Handle the 'set read\_only=1' in lighter way, than the FLUSH TABLES READ LOCK;\
        For the transactional engines we don't wait for operations on that tables to finish.
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
* [Revision #3426](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3426)\
  Mon 2012-06-04 18:06:00 +0300
  * Fix [Bug #1008487](https://bugs.launchpad.net/bugs/1008487)
  * Analysis:
    * The crash is a result of Item\_cache\_temporal::example not being set\
      (it is NULL). It turns out that the value of Item\_cache\_temporal\
      may be set directly by calling Item\_cache\_temporal::store\_packed\
      without ever setting the "example" of this Item\_cache. Therefore\
      the failing assertion is too narrow.
    *
  * Solution:
    * Remove the assert.
    *
    * In principle we could overwrite this method for Item\_cache\_temporal,\
      but it doesn't make sense just for this assert.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
