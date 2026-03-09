# MariaDB 5.3.5 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.3.5) |[Release Notes](../../old-releases/5.3/5.3.5.md) |**Changelog** |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 29 Feb 2012

For the highlights of this release, see the [release notes](../../old-releases/5.3/5.3.5.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3450](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3450)\
  Tue 2012-02-28 15:41:55 +0100
  * [Bug #938977](https://bugs.launchpad.net/bugs/938977) - Query performance with join/index super slow on [MariaDB 5.3.4](../../old-releases/5.3/5.3.4.md) RC
  * make sure that stored routines are evaluated (that is, de facto - cached) in convert\_const\_to\_int().\
    revert the fix for [Bug #806943](https://bugs.launchpad.net/bugs/806943) because it cannot be repeated anymore.\
    add few tests for convert\_const\_to\_int()
* [Revision #3449](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3449) \[merge]\
  Tue 2012-02-28 15:04:31 +0100
  * merge
  * [Revision #2732.53.10](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.10) \[merge]\
    Tue 2012-02-28 13:50:30 +0200
    * Automatic merge
    * [Revision #2732.54.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.54.1)\
      Tue 2012-02-28 13:39:02 +0200
      * Fixed [Bug #905716](https://bugs.launchpad.net/bugs/905716) "Assertion \`page->size <= share->max\_index\_block\_size'"
      * The issue was that Aria allowed too long keys to be created (so that the internal buffer was not big enough to hold the whole key).
      * Key lengths is now limited to HA\_MAX\_KEY\_LENGTH (1000), as for MyISAM.
      * Fixed failure in "\_ma\_apply\_redo\_index: Assertion \`new\_page\_length == 0", as found by buildbot.
* [Revision #3448](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3448) \[merge]\
  Sun 2012-02-26 03:13:33 -0800
  * Merge.
  * [Revision #3446.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3446.1.2) \[merge]\
    Sun 2012-02-26 02:42:45 -0800
    * Merge 5.2->5.3
    * [Revision #2732.53.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.9)\
      Sat 2012-02-25 17:10:07 -0800
      * Fixed LP bug #939866.
      * The field key\_cache\_mem\_size of the KEY\_CACHE structure must be\
        initialized in the function init\_key\_cache() and updated in the\
        function resize\_key\_cache().
    * [Revision #2732.53.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.8)\
      Sat 2012-02-25 09:03:06 +0200
      * Fix of [Bug #938518](https://bugs.launchpad.net/bugs/938518) (also [Bug #791761](https://bugs.launchpad.net/bugs/791761) and [Bug #806955](https://bugs.launchpad.net/bugs/806955))
      * Cause of the bug is uninitialized items before evaluation `HAVING` clasue in case of empty result.
  * [Revision #3446.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3446.1.1)\
    Sun 2012-02-26 00:19:07 -0800
    * Rolled back the patch for bug 791761.
    * A better fix for this bug will be pulled from mariadb-5.2.
* [Revision #3447](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3447)\
  Sun 2012-02-26 11:44:52 +0400
  * Bump the version number.
* [Revision #3446](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3446) \[merge]\
  Fri 2012-02-24 18:35:58 -0800
  * Merge.
  * [Revision #3439.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3439.2.1)\
    Fri 2012-02-24 16:50:22 -0800
    * Fixed [Bug #939009](https://bugs.launchpad.net/bugs/939009).
    * The result of materialization of the right part of an IN subquery predicate\
      is placed into a temporary table. Each row of the materialized table is\
      distinct. A unique key over all fields of the temporary table is defined and\
      created. It allows to perform key look-ups into the table.\
      The table created for a materialized subquery can be accessed by key as\
      any other table. The function best\_access-path search for the best access\
      to join a table to a given partial join. With some where conditions this\
      function considers a possibility of a ref\_or\_null access. If such access\
      employs the unique key on the temporary table then when estimating\
      the cost this access the function tries to use the array rec\_per\_key. Yet,\
      such array is not built for this unique key. This causes a crash of the server.
    * Rows returned by the subquery that contain nulls don't have to be placed\
      into temporary table, as they cannot be match any row produced by the\
      left part of the subquery predicate. So all fields of the temporary table\
      can be defined as non-nullable. In this case any ref\_or\_null access\
      to the temporary table does not make any sense and it does not make sense\
      to estimate such an access.
    * The fix makes sure that the temporary table for a materialized IN subquery\
      is defined with columns that are all non-nullable. The also ensures that\
      any row with nulls returned by the subquery is not placed into the\
      temporary table.
* [Revision #3445](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3445)\
  Sat 2012-02-25 01:42:28 +0400
  * Update test results.
* [Revision #3444](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3444)\
  Fri 2012-02-24 22:42:37 +0400
  * [Bug #938131](https://bugs.launchpad.net/bugs/938131): Subquery materialization is not used in `CREATE TABLE SELECT`
  * Enable subquery materialization for `CREATE TABLE ... SELECT`.
* [Revision #3443](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3443) \[merge]\
  Fri 2012-02-24 20:07:12 +0400
  * Merge 5.2->5.3
  * [Revision #2732.53.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.7) \[merge]\
    Fri 2012-02-24 17:21:44 +0200
    * Automatic merge
    * [Revision #2643.143.77](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.77)\
      Fri 2012-02-24 17:01:47 +0200
      * Fix for [Bug #909635](https://bugs.launchpad.net/bugs/909635): MariaDB crashes on a select with long varchar and blob fields
      * Problem was a crash in internal temporary (Maria) files when row length exceeded 65535
  * [Revision #2732.53.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.6)\
    Wed 2012-02-22 00:10:39 -0800
    * Back-ported the fix and test cases for [MySQL Bug #59487](https://bugs.mysql.com/bug.php?id=59487) and [MySQL Bug #43368](https://bugs.mysql.com/bug.php?id=43368) from\
      the mysql-5.6 code line.
* [Revision #3442](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3442) \[merge]\
  Fri 2012-02-24 17:13:04 +0400
  * Merge fix for [Bug #934597](https://bugs.launchpad.net/bugs/934597)
  * [Revision #3439.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3439.1.1)\
    Fri 2012-02-24 17:09:13 +0400
    * [Bug #934597](https://bugs.launchpad.net/bugs/934597): Assertion \`! is\_set()' failed in Diagnostics\_area::set\_ok\_status(THD...
    * After the exec\_const\_cond->val\_int() call, check for error and return.\
      (if we don't do it, we will eventually hit an error when trying to set status OK in\
      the diagnostics area, which already has an error status).
* [Revision #3441](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3441)\
  Fri 2012-02-24 12:34:47 +0200
  * Removed const declarations to get rid of compiler warnings. The changes are similar to what is done in innobase in MySQL 5.5
* [Revision #3440](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3440) \[merge]\
  Thu 2012-02-23 17:00:10 +0200
  * Automatic merge
  * [Revision #3434.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3434.1.2)\
    Thu 2012-02-23 16:51:58 +0200
    * Fixes for make\_binary\_distribution and mysql\_config for OpenSuse 12.1
  * [Revision #3434.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3434.1.1)\
    Thu 2012-02-23 16:43:35 +0200
    * Fixed [Bug #933719](https://bugs.launchpad.net/bugs/933719), "Assertion open\_tables == 0 ... " in THD::restore\_backup\_open\_tables\_state.
    * This also fixes a (not likely) crashing bug when forcing a thread that was doing a table lock to re-open it's files, for example by creating a trigger.
* [Revision #3439](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3439)\
  Wed 2012-02-22 17:38:24 +0400
  * Don't run test for BUG#933412 with embedded server, as it requires concurrent query\
    execution which `mtr --embedded` does not support
* [Revision #3438](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3438)\
  Wed 2012-02-22 17:11:33 +0400
  * Sort counters by their names (otherwise, the order of SHOW STATUS output is sometimes sorted and sometimes not)
* [Revision #3437](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3437)\
  Wed 2012-02-22 16:48:29 +0400
  * Added back MRR counters. The new names are: `Handler_mrr_init`, `Handler_mrr_key_refills`, `Handler_mrr_rowid_refills`.
* [Revision #3436](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3436)\
  Wed 2012-02-22 10:38:28 +0200
  * Changed names of statistic variables and counting matches instaed of rejected rows.
* [Revision #3435](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3435)\
  Tue 2012-02-21 21:18:41 +0100
  * [Bug #923429](https://bugs.launchpad.net/bugs/923429) Crash in `decimal_cmp` on using `UNIX_TIMESTAMP` with a wrongly formatted timestamp
  * `UNIX_TIMESTAMP()` can be null, and returns null for invalid values
* [Revision #3434](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3434) \[merge]\
  Tue 2012-02-21 18:00:23 +0200
  * Merge with 5.2
  * [Revision #2732.53.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.5) \[merge]\
    Tue 2012-02-21 17:48:15 +0200
    * Automatic merge with 5.1
    * [Revision #2643.143.76](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.76)\
      Tue 2012-02-21 14:17:33 +0200
      * Fixed suppression expression.
* [Revision #3433](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3433)\
  Tue 2012-02-21 17:58:43 +0200
  * Fixed that 'make distcheck' works with automake 1.11.11
  * Fixed compiler warnings found by buildbot
* [Revision #3432](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3432)\
  Mon 2012-02-20 21:30:23 +0100
  * fix for\
    "relocation R\_X86\_64\_PC32 against \`handler\_index\_cond\_check' can not be used when making a shared object; recompile with -fPIC"\
    don't use visibility=hidden for external functions
* [Revision #3431](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3431) \[merge]\
  Tue 2012-02-21 09:43:36 +0200
  * Automatic merge
  * [Revision #3429.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3429.1.4) \[merge]\
    Tue 2012-02-21 09:37:56 +0200
    * Automatic merge
    * [Revision #2732.53.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.4)\
      Tue 2012-02-21 09:35:46 +0200
      * Fixed wrong test case
  * [Revision #3429.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3429.1.3) \[merge]\
    Tue 2012-02-21 09:36:48 +0200
    * Automatic merge
    * [Revision #2732.53.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.3) \[merge]\
      Tue 2012-02-21 01:55:12 +0200
      * Merge with 5.1
      * [Revision #2643.143.75](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.75) \[merge]\
        Tue 2012-02-21 01:51:55 +0200
        * Automatic merge
        * [Revision #2643.151.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.151.1)\
          Tue 2012-02-21 01:44:50 +0200
          * More general handling of memory loss in dlclose (backported from 5.2)
          * Fixed supression in mysql-test-run so it also works on windows.
    * [Revision #2732.53.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.2) \[merge]\
      Tue 2012-02-21 01:49:14 +0200
      * Automatic merge
      * [Revision #2732.46.76](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.76)\
        Tue 2012-02-21 01:46:51 +0200
        * Added missing signal values to signal\_handler.cc
    * [Revision #2732.53.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.1) \[merge]\
      Mon 2012-02-20 18:46:22 +0100
      * merge
      * [Revision #2643.143.74](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.74)\
        Mon 2012-02-20 18:07:38 +0100
        * Fix compilation on Windows, and various Windows related mistakes introduced by\
          "safe exception patch".
        * Remove misleading comments suggesting about signal() Windows, the routine here\
          is part of a exception handler, and sig parameter is an exception code.
  * [Revision #3429.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3429.1.2) \[merge]\
    Tue 2012-02-21 01:58:50 +0200
    * Merge with [MariaDB 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)
    * [Revision #2732.46.75](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.75) \[merge]\
      Mon 2012-02-20 17:58:00 +0200
      * Merge with 5.1
      * [Revision #2643.143.73](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.73)\
        Mon 2012-02-20 17:56:47 +0200
        * Fixed compiler warnings
    * [Revision #2732.46.74](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.74) \[merge]\
      Mon 2012-02-20 17:49:21 +0200
      * Merge with [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md) and MySQL 5.1.61
      * [Revision #2643.143.72](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.72) \[merge]\
        Mon 2012-02-20 16:23:18 +0200
        * Merge with MYSQL 5.1.61
        * Fixed README with link to source
        * Merged InnoDB change to XtraDB
      * [Revision #2643.143.71](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.71) \[
        * merge]\
          Sat 2012-02-11 16:42:46 +0100
        * merge
      * [Revision #2643.143.70](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.70)\
        Wed 2012-01-25 11:34:43 +0100
        * mtr runs only "big" tests, if `--big-test` is repeated twice
      * [Revision #2643.143.69](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.69)\
        Wed 2012-01-04 20:10:15 +0100
        * report innodb\_file\_per\_table, innodb\_flush\_log\_at\_trx\_commit, innodb\_flush\_method
        * [Revision #2732.46.73](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.73)\
          Mon 2012-02-20 14:03:44 +0200
          * Fixed [Bug #902654](https://bugs.launchpad.net/bugs/902654) "MariaDB consistently crashes in collect\_tables on Aria checkpoint execution"\
            This happend when you have more than 1024 open Aria tables during checkpoint.
        * [Revision #2732.46.72](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.72)\
          Thu 2012-02-16 16:06:49 -0800
          * Fixed [Bug #933117](https://bugs.launchpad.net/bugs/933117).
          * The bug was fixed with the code back-ported from the patch for LP bug 800184\
            pushed into mariadb-5.3.
  * [Revision #3429.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3429.1.1)\
    Mon 2012-02-20 17:59:42 +0200
    * Fixed issue found by buildbot
* [Revision #3430](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3430)\
  Mon 2012-02-20 20:38:05 +0400
  * [Bug #933412](https://bugs.launchpad.net/bugs/933412): Server crashes in \_mi\_put\_key\_in\_record on KILL QUERY with ICP, STRAIGHT\_JOIN
    * In mi\_rkey(), do correct handling of case where mi\_yield\_and\_check\_if\_killed()\
      detects that the thread was killed (all other similar functions in MyISAM/Aria have\
      slightly different code and do not have this problem).
    * Also fixed assignment in DBUG\_ASSERT
    * this is 2nd variant of the fix:
      * make .result file smaller
      * run KILLable statements in a separate connection, otherwise we could end up trying to\
        KILL the final "DROP TABLE" statement
* [Revision #3429](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3429) \[merge]\
  Mon 2012-02-20 15:34:50 +0400
  * Merge
  * [Revision #3419.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3419.1.1)\
    Mon 2012-02-20 15:30:54 +0400
    * [Bug #933407](https://bugs.launchpad.net/bugs/933407): Valgrind warnings in mark\_as\_null\_row with materialization+semijoin, STRAIGHT\_JOIN, impossible WHERE
      * In return\_zero\_rows(), don't call mark\_as\_null\_row() for semi-join\
        materialized tables, because 1) they may have been already freed, and\
        2\)there is no real need to call mark\_as\_null\_row() for them.
* [Revision #3428](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3428)\
  Sat 2012-02-18 19:11:57 -0800
  * Fixed [Bug #934348](https://bugs.launchpad.net/bugs/934348).
  * This bug is the result of an incomplete/inconsistent change introduced into\
    5.3 code when the cond\_equal parameter were added to the function optimize\_cond.
  * The change was made during a merge from 5.2 in October 2010.
  * The bug could affect only queries with HAVING.
* [Revision #3427](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3427)\
  Sat 2012-02-18 16:06:38 -0800
  * Fixed [Bug #934342](https://bugs.launchpad.net/bugs/934342).
  * An outer join query with a semi-join subquery could return a wrong result\
    if the optimizer chose to materialize the subquery.
  * It happened because when substituting for the best field into a ref item\
    used to build access keys not all `COND_EQUAL` objects that could be employed\
    at substitution were checked.
  * Also refined some code in the function check\_join\_cache\_usage to make it\
    safer.
* [Revision #3426](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3426)\
  Fri 2012-02-17 13:27:41 +0100
  * Remove engine-specific (but identical) icp callbacks. create one reusable\
    common icp callback in the handler.cc.
  * It can also increment status counters, without making the engine\
    dependent on the exact THD layout (that is different in embedded).
* [Revision #3425](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3425)\
  Thu 2012-02-16 20:13:28 -0800
  * Fixed [Bug #928352](https://bugs.launchpad.net/bugs/928352).
  * This bug led to wrong values of the use\_count fields in some SEL\_ARG\
    trees that triggered complains on the server side when executing the\
    test case for LP bug 800184 if a debug build of the server was used.
  * This was the result of the incomplete fix for [Bug #800184](https://bugs.launchpad.net/bugs/800184).
  * To complete it the following corrections had to be made:
    * the copy constructor for SEL\_TREE must call the new function incr\_refs\_all()\
      instead of the function incr\_refs(), because references to next key parts\
      from any SEL\_ARG tree belonging to the list of the first key part has to be\
      adjusted.
    * the method and\_sel\_tree of the class SEL\_IMERGE must use the copy constructor\
      of the SEL\_TREE class to make a copy of its second argument before it ANDs it\
      with any SEL\_TREE tree from the processed SEL\_IMERGE object.
* [Revision #3424](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3424)\
  Thu 2012-02-16 20:15:57 +0400
  * Backport of:

```
timestamp: Thu 2011-12-01 15:12:10 +0100
Fix for Bug#13430436 PERFORMANCE DEGRADATION IN SYSBENCH ON INNODB DUE TO ICP
.
When running sysbench on InnoDB there is a performance degradation due
to index condition pushdown (ICP). Several of the queries in sysbench
have a WHERE condition that the optimizer uses for executing these
queries as range scans. The upper and lower limit of the range scan
will ensure that the WHERE condition is fulfilled. Still, the WHERE
condition is part of the queries' condition and if ICP is enabled the
condition will be pushed down to InnoDB as an index condition. 
.
Due to the range scan's upper and lower limits ensure that the WHERE
condition is fulfilled, the pushed index condition will not filter out
any records. As a result the use of ICP for these queries results in a
performance overhead for sysbench. This overhead comes from using
resources for determining the part of the condition that can be pushed
down to InnoDB and overhead in InnoDB for executing the pushed index
condition.
.
With the default configuration for sysbench the range scans will use
the primary key. This is a clustered index in InnoDB. Using ICP on a
clustered index provides the lowest performance benefit since the
entire record is part of the clustered index and in InnoDB it has the
highest relative overhead for executing the pushed index condition.
.
The fix for removing the overhead ICP introduces when running sysbench
is to disable use of ICP when the index used by the query is a
clustered index.
.
When WL#6061 is implemented this change should be re-evaluated.
```

* [Revision #3423](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3423)\
  Thu 2012-02-16 18:56:10 +0400
  * Added comments
* [Revision #3422](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3422)\
  Thu 2012-02-16 08:49:10 +0200
  * Counters for Index Condition Pushdown added ([MDEV-130](https://jira.mariadb.org/browse/MDEV-130)).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
