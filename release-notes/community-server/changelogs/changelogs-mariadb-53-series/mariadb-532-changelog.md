# MariaDB 5.3.2 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.3.2) |[Release Notes](../../old-releases/5.3/5.3.2.md) |**Changelog** |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 14 Oct 2011

For the highlights of this release, see the [release notes](../../old-releases/5.3/5.3.2.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3231](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3231)\
  Thu 2011-10-13 00:15:51 +0400
  * Remove garbage comment
* [Revision #3230](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3230)\
  Wed 2011-10-12 21:40:56 +0400
  * [Bug #872702](https://bugs.launchpad.net/bugs/872702): Crash in add\_ref\_to\_table\_cond() when grouping by a PK
  * Testcase
* [Revision #3229](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3229)\
  Wed 2011-10-12 21:38:40 +0400
  * Code cleanup: move variable into branch that uses it
* [Revision #3228](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3228)\
  Wed 2011-10-12 14:01:01 +0200
  * fix a compilation failure for perl Net::HandlerSocket module
* [Revision #3227](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3227) \[merge]\
  Wed 2011-10-12 12:45:35 +0200
  * merge
  * [Revision #3225.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3225.1.1) \[merge]\
    Wed 2011-10-12 12:30:55 +0200
    * merge
    * [Revision #2732.46.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.9)\
      Wed 2011-10-12 12:07:14 +0200
      * Add option to enable feedback plugin to the MSI installer.
* [Revision #3226](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3226)\
  Wed 2011-10-12 14:23:42 +0400
  * Fix compile error: ‘cond\_copy’ may be used uninitialized in this function.
* [Revision #3225](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3225)\
  Wed 2011-10-12 13:19:37 +0400
  * [Bug #869001](https://bugs.launchpad.net/bugs/869001): Wrong result with semijoin + materialization + firstmatch + multipart key
  * Make advance\_sj\_state() not to attempt building duplicate removal strategies\
    when we're doing optimization of an SJM-nest.
* [Revision #3224](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3224)\
  Wed 2011-10-12 02:04:03 +0400
  * Update subselect\_sj{,2}\_mat.result with changes that were lost when\
    they were deleted and re-created.
* [Revision #3223](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3223)\
  Tue 2011-10-11 23:38:26 +0200
  * Restore files accidentally deleted in previous merge.
* [Revision #3222](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3222) \[merge]\
  Tue 2011-10-11 23:52:23 +0400
  * Merge: fix subselect\_sj2\*.test: add missing DROP TABLE statement
    * [Revision #3219.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3219.1.1)\
      Tue 2011-10-11 23:48:50 +0400
      * Fix testcases from the previous push: add missing DROP TABLE statement
* [Revision #3221](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3221)\
  Tue 2011-10-11 21:43:43 +0200
  * when freeing a possibly NULL pointer under safemalloc - use MY\_ALLOW\_ZERO\_PTR
* [Revision #3220](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3220) \[merge]\
  Tue 2011-10-11 20:20:19 +0200
  * merge
  * [Revision #3218.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3218.1.2) \[merge]\
    Tue 2011-10-11 20:18:46 +0200
    * merge
    * [Revision #3218.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3218.1.1) \[merge]\
      Tue 2011-10-11 20:17:44 +0200
      * merge
      * [Revision #2732.46.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.8) \[merge]\
        Tue 2011-10-11 20:16:11 +0200
        * merge
        * [Revision #2643.143.40](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.40)\
          Tue 2011-10-11 20:13:57 +0200
          * remove unconditional SAFEMALLOC/SAFEMUTEX from debug flags
* [Revision #3219](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3219) \[merge]\
  Tue 2011-10-11 21:57:57 +0400
  * Merge fix for BUG#869012
  * [Revision #3216.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3216.1.1)\
    Tue 2011-10-11 21:34:00 +0400
    * [Bug #869012](https://bugs.launchpad.net/bugs/869012): Wrong result with semijoin + materialization + AND in WHERE
    * in make\_join\_select(), use the correct condition to check whether the\
      current table is a SJM nest (the previous condition used to be correct\
      before, but then sj-materialization temp table creation was moved to happen\
      before make\_join\_select was called)
* [Revision #3218](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3218) \[merge]\
  Tue 2011-10-11 12:55:42 +0200
  * merge
  * [Revision #2732.46.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.7) \[merge]\
    Mon 2011-10-10 19:34:37 +0200
    * merge
    * [Revision #2643.143.39](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.39)\
      Mon 2011-10-10 17:59:26 +0200
      * add a missing definition
      * [Revision #2732.46.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.6)\
        Sat 2011-10-08 19:00:00 +0200
        * fix feedback plugin for 5.2
      * [Revision #2732.46.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.5) \[merge]\
        Fri 2011-10-07 00:18:30 +0200
        * merge with 5.1
        * [Revision #2643.143.38](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.38)\
          Thu 2011-10-06 23:40:19 +0200
          * sort results in tests to make them stable
        * [Revision #2643.143.37](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.37)\
          Thu 2011-10-06 23:39:44 +0200
          * disable feedback plugin by default. Now on windows too.
        * [Revision #2643.143.36](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.36) \[merge]\
          Thu 2011-10-06 21:42:43 +0200
          * merge the feedback tree
          * [Revision #2643.147.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.147.8)\
            Thu 2011-10-06 20:55:38 +0200
            * Implement uname() on Windows.
            * Also, fix code to get physical memory size.
          * [Revision #2643.147.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.147.7) \[merge]\
            Thu 2011-10-06 18:48:16 +0200
            * merge with feedback-plugin
            * and disable feedback plugin by default, if it's compiled in.
            * [Revision #0.13.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/0.13.4)\
              Thu 2011-10-06 18:24:00 +0200
              * add #define WITH\_FEEDBACK\_PLUGIN
          * [Revision #2643.147.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.147.6)\
            Wed 2011-10-05 20:16:42 +0200
            * fix fulltext\_plugin.test on windows
          * [Revision #2643.147.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.147.5)\
            Tue 2011-10-04 16:51:39 +0200
            * tests for feedback plugin,
            * bugfix: garbage in PLUGIN\_VAR\_STR variables when INSTALL'ing a plugin
          * [Revision #2643.147.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.147.4) \[merge]\
            Tue 2011-10-04 16:03:10 +0200
            * merge feedback plugin
            * [Revision #0.13.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/0.13.3)\
              Tue 2011-10-04 15:48:39 +0200
              * fix for static plugins in mariadb.
              * send "startup" message 5 minutes after startup, not immediately
            * [Revision #0.13.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/0.13.2)\
              Mon 2011-10-03 08:43:01 +0200
              * don't use https url by default, if ssl is not available
            * [Revision #0.13.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/0.13.1)\
              Sat 2011-10-01 21:23:01 +0200
              * initial checkin
          * [Revision #2643.147.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.147.3)\
            Tue 2011-10-04 15:41:52 +0200
            * support for plugins on windows
          * [Revision #2643.147.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.147.2)\
            Tue 2011-10-04 15:07:55 +0200
            * my\_gethwaddr() on Solaris and Windows
          * [Revision #2643.147.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.147.1)\
            Tue 2011-10-04 15:01:26 +0200
            * remove redundant declarations
      * [Revision #2732.46.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.4)\
        Thu 2011-10-06 16:56:59 +0300
        * Fixed that when using a trigger mysql.proc is now accessed
        * Cleanup: Changed procedure type from a int/char to an enum for easier to manage and debug code.
* [Revision #3217](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3217)\
  Tue 2011-10-11 02:36:08 -0700
  * Fixed [Bug #870046](https://bugs.launchpad.net/bugs/870046).
  * This bug is a consequence of the fix in the function add\_ref\_to\_table\_cond\
    for [Bug #826935](https://bugs.launchpad.net/bugs/826935) that turned out to be not quite correct: it tried to AND\
    the same generated condition with two different other conditions.
  * This patch creates a copy of the generated condition if the condition needs\
    to be ANDed with two different items.
* [Revision #3216](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3216) \[merge]\
  Mon 2011-10-10 23:34:32 +0300
  * Merge
  * [Revision #3210.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3210.2.1)\
    Wed 2011-10-05 18:18:00 +0300
    * Making subquery cache on by default.
* [Revision #3215](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3215)\
  Mon 2011-10-10 15:38:11 +0200
  * remove unnecessary define
* [Revision #3214](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3214)\
  Thu 2011-09-29 20:12:57 +0200
  * make sure that cast(... as date) returns a valid date, as specified by the caller.
  * make Item::send() request a date according to the current SQL mode limitations.
* [Revision #3213](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3213) \[merge]\
  Thu 2011-10-06 01:21:15 +0400
  * Merge fix for BUG#860580
  * [Revision #3210.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3210.1.1)\
    Thu 2011-10-06 01:11:08 +0400
    * [Bug #860580](https://bugs.launchpad.net/bugs/860580): Sporadic crash / valgrind warning in register\_field\_in\_read\_map() with semijoin
    * The problem:
      * in an uncorrelated subquery, JOIN execution code may make\
        irreversible cleanups after it has been executed (because the subquery\
        won't be executed again). In particular, JTBM nests and their injected\
        IN-equalities will be invalidated (the materialized table will be dropped\
        and TABLE structure freed).
    * Solution:
      * don't walk into Item\_subselect if represents an uncorrelated\
        subselect that has already been executed. The idea is that the subselect\
        will not be executed again (calling Item\_subselect\_xxx::val\_int() will fetch\
        the cached value), so it should not matter what is inside the subselect.
* [Revision #3212](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3212) \[merge]\
  Wed 2011-10-05 16:56:17 +0300
  * Automatic merge with 5.2
  * [Revision #2732.46.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.3) \[merge]\
    Wed 2011-10-05 16:53:35 +0300
    * Automatic merge with 5.1
    * [Revision #2643.143.35](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.35)\
      Wed 2011-10-05 16:37:05 +0300
      * Fix for issue found in buildbot where mysqld.\*.err files was missing
      * Added suppression message for valgrind failure found on OpenSuSE 11.1
* [Revision #3211](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3211) \[merge]\
  Wed 2011-10-05 16:15:30 +0300
  * Automatic merge
  * [Revision #2732.46.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.2)\
    Wed 2011-10-05 15:59:49 +0300
    * Fixed [Bug #859051](https://bugs.launchpad.net/bugs/859051) "Periodic aria checkpoints prevent power management"
    * Now the aria\_log\_control\_file and log file is not touched if aria files are not written to.
    * [Revision #2732.46.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.1) \[
      * merge]\
        Fri 2011-09-16 18:30:46 +0200
      * merge
* [Revision #3210](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3210)\
  Tue 2011-10-04 23:57:46 +0300
  * Fix [Bug #856152](https://bugs.launchpad.net/bugs/856152)
  * Analysis:
    * The cause of the bug was that the method\
      subselect\_rowid\_merge\_engine::partial\_match()\
      was not designed for re-execution within the\
      same query. Specifically, it didn't cleanup\
      the bitmap of matching keys after completion.
    * The test query requires double execution of\
      the IN predicate because it first checks the\
      predicate as a constant condition. The second\
      execution during regular execution used the bitmap\
      of matching keys produced by the first execution\
      instead of starting with a clean one.
  * Solution:
    * Cleanup the bitmap of matching keys at the end of\
      the partial matching procedure.
* [Revision #3209](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3209)\
  Tue 2011-10-04 12:00:55 -0700
  * Made the result test of a test case platform independent
  * (correction for the previous patch).
* [Revision #3208](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3208)\
  Tue 2011-10-04 08:45:01 -0700
  * Made the result test of a test case platform independent.
* [Revision #3207](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3207)\
  Mon 2011-10-03 21:36:18 -0700
  * Fixed a bad merge.
  * Changed a test case to make its result set platform independent.
* [Revision #3206](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3206) \[merge]\
  Mon 2011-10-03 15:50:42 -0700
  * Merge.
  * [Revision #3190.2.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3190.2.2)\
    Fri 2011-09-30 21:53:59 -0700
    * The previous correction of the cost estimate to access a joined table\
      in the function best\_access\_path revealed another bug: currently\
      table scans on NULL keys used for NOT IN subqueries cannot work\
      together with employment of join caches for inner tables of these\
      subqueries. Otherwise the result can be wrong as it could be seen\
      with the result of the test case constructed for bug #37894\
      in the file subselect3\_jcl6.result.
  * [Revision #3190.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3190.2.1)\
    Fri 2011-09-30 18:55:02 -0700
    * Fixed a cost estimation bug introduced into in the function best\_access\_path\
      of the 5.3 code line after a merge with 5.2 on 2010-10-28\
      in order not to allow the cost to access a joined table to be equal\
      to 0 ever.
    * Expanded data sets for many test cases to get the same execution plans\
      as before.
* [Revision #3205](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3205) \[merge]\
  Tue 2011-10-04 02:24:04 +0400
  * Merge
  * [Revision #3203.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3203.1.1)\
    Tue 2011-10-04 02:20:06 +0400
    * Fix buildbot failure in previous fix ([Bug #861147](https://bugs.launchpad.net/bugs/861147)):
    * convert\_subq\_to\_jtbm() should always restore the used arena.
* [Revision #3204](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3204)\
  Mon 2011-10-03 22:48:15 +0300
  * Fix [Bug #858038](https://bugs.launchpad.net/bugs/858038)
  * Analysis:
    * The cause of the bug was the changed meaning of\
      subselect\_partial\_match\_engine::has\_covering\_null\_row.\
      Previously it meant that there is row with NULLs in\
      all nullable fields of the materialized subquery table.\
      Later it was changed to mean a row with NULLs in all\
      fields of this table.
    * At the same time there was a shortcut in\
      subselect\_rowid\_merge\_engine::partial\_match() that\
      detected a special case where:
      * there is no match in any of the columns with NULLs, and
      * there is no NULL-only row that covers all columns with\
        NULLs.
    * With the change in the meaning of has\_covering\_null\_row,\
      the condition that detected this special case was incomplete.
    * This resulted in an incorrect FALSE, when the result was a\
      partial match.
  * Solution:
    * Expand the condition that detected the special case with the\
      correct test for the existence of a row with NULL values in\
      all columns that contain NULLs (a kind of parially covering\
      NULL-row).
* [Revision #3203](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3203) \[merge]\
  Sat 2011-10-01 00:56:42 +0400
  * Merge
  * [Revision #3199.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3199.1.3)\
    Sat 2011-10-01 00:55:57 +0400
    * [Bug #861147](https://bugs.launchpad.net/bugs/861147): Assertion \`fixed == 1' failed in Item\_func\_eq::val\_int() with semijoin + materialization
    * convert\_subq\_to\_jtbm() didn't check that subuqery optimization was successful. If it wasn't (in this\
      example because of @@max\_join\_size violation), it would proceed further and eventually crash when\
      trying to execute the un-optimized subquery.
* [Revision #3202](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3202) \[merge]\
  Sat 2011-10-01 00:20:01 +0400
  * Merge
  * [Revision #3199.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3199.1.2)\
    Sat 2011-10-01 00:10:03 +0400
    * [Bug #860553](https://bugs.launchpad.net/bugs/860553): Crash in create\_ref\_for\_key with semijoin + materialization
      * The problem was that JOIN::save/restore\_query\_plan() did not save/restore parts of\
        the query plan that are located inside SJ\_MATERIALIZATION\_INFO structures. This could\
        cause parts of one plan to be used with another, which led get\_best\_combination() to\
        constructing non-sensical join plans (and crash).\
        Fixed by saving/restoring SJM parts of the query plans.
      * check\_and\_do\_in\_subquery\_rewrites() will not set SUBS\_MATERIALIZATION flag when it\
        records that the subquery predicate is to be converted into semi-join.\
        If convert\_join\_subqueries\_to\_semijoins() later decides not to convert to semi-join,\
        let it set SUBS\_MATERIALIZATION flag, if appropriate.
* [Revision #3201](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3201) \[merge]\
  Thu 2011-09-29 17:07:43 +0400
  * Merge
  * [Revision #3199.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3199.1.1)\
    Thu 2011-09-29 17:03:12 +0400
    * [Bug #860535](https://bugs.launchpad.net/bugs/860535): Assertion \`keypart\_map' failed in mi\_rkey with semijoin
      * are\_tables\_local() failed to recognize the fact that OUTER\_REF\_TABLE\_BIT is ok\
        for SJ-Materialization. This caused zero-length ref access to be constructed, which\
        led to an assert.
* [Revision #3200](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3200)\
  Thu 2011-09-29 12:58:20 +0200
  * Fix test suite:
    * on Windows, kill can and almost always will return client error 2013 ("Lost connection...") on the killed connection,
    * On the server side, if connection is "sleeping" KILL will close the socket, thus socket error on client is expected.
* [Revision #3199](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3199)\
  Wed 2011-09-28 17:20:43 +0300
  * Fix [Bug #858148](https://bugs.launchpad.net/bugs/858148).
  * Analysis:
    * The crash is a result of the same cause as all similar\
      bugs ([Bug #827416](https://bugs.launchpad.net/bugs/827416), [Bug #718763](https://bugs.launchpad.net/bugs/718763), [Bug #778413](https://bugs.launchpad.net/bugs/778413), [Bug #806943](https://bugs.launchpad.net/bugs/806943),[Bug #611690](https://bugs.launchpad.net/bugs/611690)). The general pattern is that some optimization\
      requires the evaluation of some condition (e.g. the WHERE\
      clause), and this condition contains a subquery, such that\
      the subquery itself requires a temporary table for its\
      execution. During the subquery execution the original\
      tables in the FROM clause are replaced by the temporary\
      table needed for the final GROUP or ORDER operation. All\
      this happens during optimization of the outer query. Later\
      when EXPLAIN is run for the subquery, explain attempts to\
      print the name of the tables in the FROM clause, but it\
      finds there a temporary table without a corresponding\
      TABLE\_LIST object. The attempt to print the name of a\
      NULL table list results in a crash.
  * Solution:
    * This patch extends the fix to bug [Bug #702301](https://bugs.launchpad.net/bugs/702301), and dissalows\
      constant substitution of aggregate functions if the filter\
      condition used to check MIN/MAX keys is an expensive condition.
* [Revision #3198](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3198) \[merge]\
  Wed 2011-09-28 13:01:47 +0400
  * Merge
  * [Revision #3196.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3196.1.1)\
    Wed 2011-09-28 12:58:01 +0400
    * [Bug #860300](https://bugs.launchpad.net/bugs/860300): Second crash with get\_fanout\_with\_deps() with semijoin + materialization
      * Make get\_post\_group\_estimate() take into account semi-join materialization nests.
* [Revision #3197](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3197)\
  Tue 2011-09-27 17:40:04 +0300
  * Fixed test case that changed when max\_user\_connections was made signed.\
    Threat ER\_CONNECTION\_KILLED same as ER\_SERVER\_SHUTDOWN in replication (to get rid of a possible warning in error log)
* [Revision #3196](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3196) \[merge]\
  Mon 2011-09-26 23:54:00 +0300
  * Automatic merge
  * [Revision #3191.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3191.1.3)\
    Mon 2011-09-26 20:26:47 +0300
    * Allow one to block an account by using GRANT max\_user\_connections = -1
    * One can set @@global.max\_user\_connections to -1 to block anyone, except SUPER user, to login.
    * If max\_user\_connection is 0, one can't change it without a restart (needed to get user connections counting to work correctly)
  * [Revision #3191.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3191.1.2)\
    Fri 2011-09-23 13:55:01 +0300
    * Fixed issue with slow query logging where examined rows where wrong
    * Reset 'examined\_rows\_count' in union to not count same rows twice
  * [Revision #3191.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3191.1.1)\
    Fri 2011-09-23 01:13:38 +0300
    * Added new options to KILL. New syntax is KILL \[HARD|SOFT] \[CONNECTION|QUERY] \[ID | USER user\_name]
      * If USER is given, all threads for that user is signaled
      * If SOFT is used then the KILL will not be sent to the handler. This can be used to not interrupt critical things in the handler like 'REPAIR'.
    * Internally added more kill signals. This gives us more information of why a query/connection was killed.
      * KILL\_SERVER is used when server is going down. In this case the users gets ER\_SHUTDOWN as the reason connection was killed.
      * Changed signals to number in correct order, which makes it easier to test how the signal should affect the code.
      * New error message ER\_CONNECTION\_KILLED if connection was killed by 'KILL CONNECTION'. Before we got error ER\_SHUTDOWN.
    * Changed names of not used parameters KILL\_QUERY & KILL\_CONNCTION to mysql\_kill() to not conflict with defines in the server
* [Revision #3195](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3195) \[merge]\
  Mon 2011-09-26 14:15:04 +0400
  * Merge
  * [Revision #3192.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3192.1.1)\
    Mon 2011-09-26 13:56:09 +0400
    * [Bug #858732](https://bugs.launchpad.net/bugs/858732): Wrong result with semijoin + loosescan + comma join
      * Fix wrong loop bounds in setup\_semijoin\_dups\_elimination()
* [Revision #3194](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3194)\
  Sat 2011-09-24 14:45:49 +0200
  * portability fix: use SOCKET\_SIZE\_TYPE in the handlersocket plugin
* [Revision #3193](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3193)\
  Fri 2011-09-23 12:00:52 +0200
  * fix typo: binlog\_annotate\_rows\_events -> binlog\_annotate\_row\_events
* [Revision #3192](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3192) \[merge]\
  Fri 2011-09-23 01:30:44 +0400
  * Merge
  * [Revision #3190.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3190.1.1)\
    Fri 2011-09-23 01:25:08 +0400
    * [Bug #849776](https://bugs.launchpad.net/bugs/849776): Wrong result with semijoin + "Impossible where"
      * Provide fix\_after\_pullout() function for Item\_in\_optimizer and other Item\_XXX classes (basically, all of them\
        that have eval\_not\_null\_tables, which means they have special rules for calculating not\_null\_tables\_cache value)
* [Revision #3191](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3191)\
  Thu 2011-09-22 11:04:00 +0200
  * portability fix: avoid anonymous structs and unions in C
* [Revision #3190](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3190)\
  Thu 2011-09-22 01:55:17 +0400
  * Fix after previous cset: update test results
* [Revision #3189](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3189) \[merge]\
  Tue 2011-09-20 20:43:57 +0400
  * Merge
  * [Revision #3184.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3184.1.2)\
    Tue 2011-09-20 20:40:07 +0400
    * [Bug #849763](https://bugs.launchpad.net/bugs/849763): Wrong result with second execution of prepared statement with semijoin + view
      * The problem was that Item\_direct\_view\_ref and its embedded Item\_field were getting incorrect\
        value of item->used\_tables() after fix\_fields() in the second and subsequent EXECUTE.
      * Made relevant fixes in Item\_field::fix\_fields() and find\_field\_in\_tables(), so that the\
        Item\_field gets the correct attributes.
* [Revision #3188](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3188) \[merge]\
  Sat 2011-09-17 23:58:36 +0400
  * Merge
  * [Revision #3184.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3184.1.1)\
    Sat 2011-09-17 23:53:50 +0400
    * LPBUG`849717: Crash in Item_func::fix_fields on second execution of a prepared statement with semijoin`
      * If convert\_join\_subqueries\_to\_semijoins() decides to wrap Item\_in\_subselect in Item\_in\_optimizer,\
        it should do so in prep\_on\_expr/prep\_where, too, as long as they are present.
      * There seems to be two possibilities of how we arrive in this function:
        * prep\_on\_expr/prep\_where==NULL, and will be set later by simplify\_joins()
        * prep\_on\_expr/prep\_where!=NULL, and it is a copy\_and\_or\_structure()-made copy of on\_expr/where.\
          the latter can happen for some (but not all!) nested joins. This bug was that we didn't handle this case.
* [Revision #3187](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3187) \[merge]\
  Fri 2011-09-16 18:26:20 +0200
  * merge
  * [Revision #2732.44.36](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.36)\
    Fri 2011-09-16 18:15:04 +0200
    * Fix path lookup for singtool
  * [Revision #2732.44.35](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.35)\
    Fri 2011-09-16 18:14:19 +0200
    * Fix compile warning
* [Revision #3186](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3186) \[merge]\
  Thu 2011-09-15 17:25:37 +0300
  * Merge with 5.2
  * [Revision #2732.44.34](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.34)\
    Thu 2011-09-15 16:56:06 +0300
    * Fixed race condition that could cause diff to fail.
    * (Code taken from 5.5)
  * [Revision #2732.44.33](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.33)\
    Thu 2011-09-15 10:36:17 +0300
    * Fixed test to be repeatable
  * [Revision #2732.44.32](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.32)\
    Wed 2011-09-14 12:48:08 +0300
    * Reset variable to not access it uninitialized
  * [Revision #2732.44.31](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.31)\
    Tue 2011-09-13 18:46:47 +0300
    * Increased version number
    * Give proper error to client on shutdown.
* [Revision #3185](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3185)\
  branch nick: maria-5.3\
  Thu 2011-09-15 16:36:43 +0300
  * Removed duplicate test
* [Revision #3184](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3184) \[merge]\
  Wed 2011-09-14 12:43:29 +0400
  * Merge
  * [Revision #3182.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3182.1.1)\
    Tue 2011-09-13 23:45:02 +0400
    * [Bug #730133](https://bugs.launchpad.net/bugs/730133): Wrong result with jkl = 7, BKA, ICP in maria-5.3 + compound index
    * Mrr\_ordered\_index\_reader::interrupt\_read() and resume\_read() should\
      save/restore not just index lookup tuple, but entire index tuple.
    * Key parts that are not used for index lookup can be still used in\
      pushed index condition. Failure to save/restore will cause the index\
      condition to be evaluated over the wrong values.
* [Revision #3183](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3183) \[merge]\
  branch nick: maria-5.3\
  Sat 2011-09-10 18:01:27 +0300
  * Merge with 5.2
  * [Revision #2732.44.30](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.30) \[merge]\
    Sat 2011-09-10 09:37:55 +0300
    * Automatic merge
    * [Revision #2732.45.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.45.2)\
      Fri 2011-09-09 19:44:07 +0300
      * Fixed that automatic killing of delayed insert thread (in flush, alter table etc) will not abort auto-repair of MyISAM table.
      * Give more information when finding an error in a MyISAM table.
      * When killing system thread, use KILL\_SYSTEM\_THREAD instead of KILL\_CONNECTION to make it easier to ignore the signal in sensitive context (like auto-repair)
      * Added new kill level: KILL\_SERVER that will in the future to be used to signal killed by shutdown.
      * Add more warnings about killed connections when warning level > 3
    * [Revision #2732.45.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.45.1)\
      Fri 2011-09-02 12:41:20 +0300
      * Fixed [Bug #814238](https://bugs.launchpad.net/bugs/814238) "safe\_mutex issues must be assertions in debug binary"
      * Added `--debug-assert-on-error` variable which, if set, will cause safe\_mutex to assert if it founds an error.
  * [Revision #2732.44.29](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.29)\
    Thu 2011-09-08 16:57:46 +0300
    * [Bug #813418](https://bugs.launchpad.net/bugs/813418) fix.
    * The problem was that optimization code did not take into account later\
      feature when instad of NOT before BETWEEN it has negated flag into the\
      Item\_func\_between inherited from Item\_func\_neg\_opt. So optimizer tried\
      process NOT BETWEEN as BETWEEN.
    * The patch just switches off the optimisation for NOT BETWEEN as it was before when NOT function was really used.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
