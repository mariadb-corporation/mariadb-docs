# MariaDB 5.3.1 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.3.1) |[Release Notes](../../old-releases/5.3/5.3.1.md) |**Changelog** |[Overview of 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md)

**Release date:** 10 Sep 2011

For the highlights of this release, see the [release notes](../../old-releases/5.3/5.3.1.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3182](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3182)\
  Thu 2011-09-08 23:24:47 +0400
  * [Bug #833600](https://bugs.launchpad.net/bugs/833600): Wrong result with view + outer join + uncorrelated subquery (non-semijoin)
    * The bug was caused by outer join being incorrectly converted into inner because of\
      invalid return values of Item\_direct\_view\_ref::not\_null\_tables().
    * Provided a correct Item\_direct\_view\_ref::not\_null\_tables() function.
* [Revision #3181](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3181) \[merge]\
  Thu 2011-09-08 21:38:10 +0400
  * Automerge.
    * [Revision #3173.1.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3173.1.9)\
      Thu 2011-09-08 19:48:14 +0400
      * [Bug #830993](https://bugs.launchpad.net/bugs/830993): Crash in end\_read\_record with derived table
        * Let join buffering code correctly take into account rowids needed\
          by DuplicateElimination when it is calculating minimum record sizes.
        * In JOIN\_CACHE::write\_record\_data, added asserts that prevent us from\
          writing beyond the end of the buffer.
* [Revision #3180](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3180) \[merge]\
  Thu 2011-09-08 09:21:31 -0700
  * Merge.
    * [Revision #3156.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3156.1.1)\
      Mon 2011-08-15 23:18:36 -0700
      * Fixed LP bug #824463.
      * When merging a view / derived table the function SELECT\_LEX::merge\_subquery\
        incorrectly updated the list SELECT\_LEX::leaf\_tables. Erroneously it\
        appended the leaf\_tables list of the merged object L and then removed the\
        reference to the merged object T from the SELECT\_LEX::leaf\_tables list.
      * A correct implementation should insert the list L into the\
        SELECT\_LEX::leaf\_tables list in place of the element of the list that\
        refers to T.
      * The bug could lead to wrong results or even crashes for queries with\
        nested outer joins over views / derived tables.
* [Revision #3179](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3179)\
  Wed 2011-09-07 20:39:47 +0200
  * [Bug #839387](https://bugs.launchpad.net/bugs/839387) Assertion \`(Item\_result) i != TIME\_RESULT' failed with CASE + datetime
    * remove incorrect DBUG\_ASSERT().
    * Fix incorrectly used cmp\_item::get\_comparator() in Item\_func\_case and Item\_equal
* [Revision #3178](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3178) \[merge]\
  Tue 2011-09-06 20:59:29 +0400
  * Merge
    * [Revision #3173.1.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3173.1.8)\
      Tue 2011-09-06 20:52:36 +0400
      * Fix typo bug
    * [Revision #3173.1.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3173.1.7)\
      Tue 2011-09-06 17:06:04 +0400
      * [Bug #823930](https://bugs.launchpad.net/bugs/823930): Wrong result with semijoin materialization and blob fields
        * Make subquery\_types\_allow\_materialization() detect a case where\
          create\_tmp\_table() would create a blob column which would make it\
          impossible to use materialization
        * Non-semi-join materialization worked because it detected that this case\
          and felt back to use IN->EXISTS. Semi-join Materialization cannot easily\
          fallback, so we have to detect this case early.
    * [Revision #3173.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3173.1.6)\
      Mon 2011-09-05 20:51:37 +0400
      * [Bug #834739](https://bugs.launchpad.net/bugs/834739): Wrong result with 3-way inner join, LooseScan,multipart keys
        * Don't use join buffering for tables that are within ranges that are\
          covered by LooseScan strategy.
    * [Revision #3173.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3173.1.5)\
      Mon 2011-09-05 19:28:22 +0400
      * [Bug #834758](https://bugs.launchpad.net/bugs/834758): Wrong result with innner join, LooseScan, two-column IN() predicate
        * get\_bound\_sj\_equalities() would produce incorrect bitmap when non-first\
          equality was bound, which resulted in invalid LooseScan plans.
    * [Revision #3173.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3173.1.4)\
      Sun 2011-09-04 16:35:37 +0400
      * [Bug #836532](https://bugs.launchpad.net/bugs/836532): Crash in Item\_equal\_fields\_iterator::get\_curr\_field with semijoin+materialization
        * Item\_in\_subselect::inject\_in\_to\_exists\_cond() should not call\
          ((Item\_cond\*)join->conds)->argument\_list()->concat(join->cond\_equal->current\_level)\
          as that makes two lists share their tail, and the cond\_equal list\
          will end up containing non-Item\_equal objects when substitute\_for\_best\_equal\_field()\
          walks through join->conds and replaces all Item\_equal objects with Item\_func\_eq objects.
        * So, instead of using List::concat(), manually copy entries from one list to another.
    * [Revision #3173.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3173.1.3)\
      Sat 2011-09-03 17:05:05 +0400
      * [Bug #834514](https://bugs.launchpad.net/bugs/834514): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(...' with aggregates
        * Make find\_all\_keys() not to rely on table->tmp\_set remaining constant during execution\
          quick\_index\_merge\_select->reset() may change it.
    * [Revision #3173.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3173.1.2)\
      Fri 2011-09-02 23:44:28 +0400
      * [Bug #836507](https://bugs.launchpad.net/bugs/836507): Crash in setup\_sj\_materialization\_part1() with semijoin+materialization
        * setup\_sj\_materialization() code failed to take into account that it can be that\
          the first \[in join order ordering] table inside semi-join-materialization nest\
          is also an inner table wrt an outer join (that is embedded in the semi-join).\
          This can happen when all of the tables that are inside the semi-join but not inside\
          the outer join are constant.
        * Made a trivial to not assume that table's embedding join nest is the semi-join\
          nest: instead, walk up the outer join nests until we reach the semi-join nest.
    * [Revision #3173.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3173.1.1)\
      Fri 2011-09-02 22:43:35 +0400
      * [Bug #836523](https://bugs.launchpad.net/bugs/836523): Crash in JOIN::get\_partial\_cost\_and\_fanout with semijoin+materialization
        * Make JOIN::get\_partial\_cost\_and\_fanout() be able to handle join plans with\
          semi-join-materialization nests.
* [Revision #3177](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3177) \[merge]\
  Tue 2011-09-06 08:38:35 -0700
  * Merge.
    * [Revision #3169.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3169.1.1)\
      Tue 2011-09-06 07:17:39 -0700
      * Fixed LP bug #838633.
      * For any query JOIN::optimize() should call the method\
        SELECT::save\_leaf\_tables after the last transformation\
        that utilizes the statement memory rather than the\
        execution memory.
* [Revision #3176](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3176) \[merge]\
  Mon 2011-09-05 10:14:48 +0300
  * Merge [Bug #780386](https://bugs.launchpad.net/bugs/780386) 5.2->5.3 (where other fix was present)
    * [Revision #2732.44.28](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.28)\
      Mon 2011-09-05 09:29:49 +0300
      * Fix of [Bug #780386](https://bugs.launchpad.net/bugs/780386).
        * ALL subquery should return TRUE if subquery rowa set is empty independently\
          of left part. The problem was that Item\_func\_(eq,ne,gt,ge,lt,le) do not\
          call execution of second argument if first is NULL no in this case subquery\
          will not be executed and when Item\_func\_not\_all calls any\_value() of the\
          subquery or aggregation function which report that there was rows. So for\
          NULL < ALL (SELECT...) result was FALSE instead of TRUE.
        * Fix is just swapping of arguments of Item\_func\_(eq,ne,gt,ge,lt,le) (with\
          changing the operation if it is needed) so that result will be the same\
          (for examole a < b is equal to b > a). This fix exploit the fact that\
          first argument will be executed in any case.
* [Revision #3175](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3175) \[merge]\
  Mon 2011-09-05 08:28:08 +0300
  * merge 5.2->5.3
    * [Revision #2732.44.27](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.27)\
      Mon 2011-09-05 08:15:46 +0300
      * Fix pbxt suite to keep the same opti9misation it was before.
* [Revision #3174](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3174)\
  Sat 2011-09-03 11:50:56 +0300
  * Fixed [Bug #828514](https://bugs.launchpad.net/bugs/828514) "Assertion \`! is\_set()' failed in Diagnostics\_area::set\_ok\_status with derived table + subquery + concurrent DML"
* [Revision #3173](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3173) \[merge]\
  Fri 2011-09-02 15:36:02 +0300
  * Merge of merge
    * [Revision #3171.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3171.1.1) \[merge]\
      Fri 2011-09-02 15:10:10 +0300
      * Merge 5.2->5.3
* [Revision #3172](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3172) \[merge]\
  Fri 2011-09-02 14:32:48 +0400
  * Merge
    * [Revision #3167.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3167.1.2)\
      Mon 2011-08-29 21:54:16 +0400
      * [Bug #836491](https://bugs.launchpad.net/bugs/836491): Crash in Item\_field::Item\_field from add\_ref\_to\_table\_cond() with semijoin+materialization
        * Let create\_tmp\_table set KEY\_PART\_INFO::fieldnr. It is needed in add\_ref\_to\_table\_cond(), and possibly other places.
    * [Revision #3167.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3167.1.1)\
      Mon 2011-08-29 19:57:41 +0400
      * [Bug #834534](https://bugs.launchpad.net/bugs/834534): Assertion \`0' failed in replace\_where\_subcondition with semijoin subquery in HAVING
        * The problem was that the code that made the check whether the subquery is an AND-part of the WHERE\
          clause didn't work correctly for nested subqueries. In particular, grand-child subquery in HAVING was\
          treated as if it was in the WHERE, which eventually caused an assert when replace\_where\_subcondition\
          looked for the subquery predicate in the WHERE and couldn't find it there.
        * The fix: Removed implementation of "thd\_marker approach". thd->thd\_marker was used to determine the\
          location of subquery predicate: setup\_conds() would set accordingly it when making\
          the `{where|on_expr}->fix_fields(...)`call\
          so that AND-parts of the WHERE/ON clauses can determine they are the AND-parts.\
          Item\_cond\_or::fix\_fields(), Item\_func::fix\_fields(), Item\_subselect::fix\_fields (this one was missed),\
          and all other items-that-contain-items had to reset thd->thd\_marker before calling fix\_fields() for\
          their children items, so that the children can see they are not AND-parts of WHERE/ON.\
          \* The "thd\_marker approach" required that a lot of code in different locations maintains correct value of\
          thd->thd\_marker, so it was replaced with:\
          \* The new approach with mark\_as\_condition\_AND\_part does not keep context in thd->thd\_marker. Instead,\
          setup\_conds() now calls `{where|on_expr}->mark_as_condition_AND_part()`
    * and implementations of that function make sure that:
      * parts of AND-expressions get the mark\_as\_condition\_AND\_part() call
      * Item\_in\_subselect objects record that they are AND-parts of WHERE/ON
* [Revision #3171](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3171)\
  Thu 2011-09-01 23:53:12 +0300
  * Fix for [Bug #834492](https://bugs.launchpad.net/bugs/834492)
  * Analysis:
    * In the test query semi-join merges the inner-most subquery\
      into the outer subquery, and the optimization of the merged\
      subquery finds some new index access methods. Later the\
      IN-EXISTS transformation is applied to the unmerged subquery.\
      Since the optimizer is instructed to not consider\
      materialization, it reoptimizes the plan in-place to take into\
      account the new IN-EXISTS conditions. Just before reoptimization\
      JOIN::choose\_subquery\_plan resets the query plan, which also\
      resets the access methods found during the semi-join merge.\
      Then reoptimization discovers there are no new access methods,\
      but it leaves the query plan in its reset state. Later semi-join\
      crashes because it assumes these access methods are present.
  * Solution:
    * When reoptimizing in-place, reset the query plan only after new\
      access methods were discovered. If no new access methods were\
      discovered, leave the current plan as it was.
* [Revision #3170](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3170)\
  Thu 2011-09-01 14:23:03 +0400
  * sec\_to\_time() in the integer context was losing the sign of the result
* [Revision #3169](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3169)\
  Mon 2011-08-29 18:16:18 +0300
  * Updated crash-me for 5.3
* [Revision #3168](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3168)\
  Mon 2011-08-29 18:14:14 +0300
  * Added MariaDB executable comment syntax: /\*M!`#` \*/
* [Revision #3167](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3167)\
  Sat 2011-08-27 00:40:29 +0300
  * Fix [Bug #827416](https://bugs.launchpad.net/bugs/827416)
  * Analysis:
    * Constant table optimization of the outer query finds that\
      the right side of the equality is a constant that can\
      be used for an eq\_ref access to fetch one row from t1,\
      and substitute t1 with a constant. Thus constant optimization\
      triggers evaluation of the subquery during the optimize\
      phase of the outer query.
    * The innermost subquery requires a plan with a temporary\
      table because with InnoDB tables the exact count of rows\
      is not known, and the empty tables cannot be optimzied\
      way. JOIN::exec for the innermost subquery substitutes\
      the subquery tables with a temporary table.
    * When EXPLAIN gets to print the tables in the innermost\
      subquery, EXPLAIN needs to print the name of each table\
      through the corresponding TABLE\_LIST object. However,\
      the temporary table created during execution doesn't\
      have a corresponding TABLE\_LIST, so we get a null\
      pointer exception.
  * Solution:
    * The solution is to forbid using expensive constant\
      expressions for eq\_ref access for contant table\
      optimization. Notice that eq\_ref with a subquery\
      providing the value is still possible during regular\
      execution.
* [Revision #3166](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3166) \[merge]\
  Tue 2011-08-23 15:51:47 +0300
  * Automatic merge.
    * [Revision #3164.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3164.1.2)\
      Tue 2011-08-23 15:39:15 +0300
      * Fixed [Bug #825018](https://bugs.launchpad.net/bugs/825018)
        * Analysis:
          * During the first execution of the query through the stored\
            procedure, the optimization phase calls\
            substitute\_for\_best\_equal\_field(), which calls\
            Item\_in\_optimizer::transform(). The latter replaces\
            Item\_in\_subselect::left\_expr with args\[0] via assignment.\
            In this test case args\[0] is an Item\_outer\_ref which is\
            created/deallocated for each re-execution. As a result,\
            during the second execution Item\_in\_subselect::left\_expr\
            pointed to freed memory, which resulted in a crash.
        * Solution:
          * The solution is to use change\_item\_tree(), so that the\
            origianal left expression is restored after each execution.
    * [Revision #3164.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3164.1.1)\
      Tue 2011-08-23 00:00:13 +0300
      * Fix [Bug #825095](https://bugs.launchpad.net/bugs/825095)
        * Analysis:
          * Partial matching is used even when there are no NULLs in\
            a materialized subquery, as long as the left NOT IN operand\
            may contain NULL values.
          * This case was not handled correctly in two different places.\
            First, the implementation of parital matching did not clear\
            the set of matching columns when the merge process advanced\
            to the next row.
          * Second, there is no need to perform partial matching at all\
            when the left operand has no NULLs.
        * Solution:
          * First fix subselect\_rowid\_merge\_engine::partial\_match() to\
            properly cleanup the bitmap of matching keys when advancing\
            to the next row.
          * Second, change subselect\_partial\_match\_engine::exec() so\
            that when the materialized subquery doesn't contain any\
            NULLs, and the left operand of \[NOT] IN doesn't contain\
            NULLs either, the method returns without doing any\
            unnecessary partial matching. The correct result in this\
            case is in Item::in\_value.
* [Revision #3165](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3165)\
  Mon 2011-08-22 13:38:32 +0200
  * [Bug #822760](https://bugs.launchpad.net/bugs/822760) Wrong result with view + invalid dates
* [Revision #3164](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3164)\
  Fri 2011-08-19 21:02:05 -0700
  * Fixed [Bug #826279](https://bugs.launchpad.net/bugs/826279).
    * When the WHERE/HAVING condition of a subquery has been transformed\
      by the optimizer the pointer stored the 'where'/'having' field\
      of the SELECT\_LEX structure used for the subquery must be updated\
      accordingly. Otherwise the pointer may refer to an invalid item.\
      This can lead to the reported assertion failure for some queries\
      with correlated subqueries
* [Revision #3163](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3163)\
  Wed 2011-08-17 14:10:32 +0300
  * Fix [Bug #813473](https://bugs.launchpad.net/bugs/813473)
    * The bug is a duplicate of MySQL's bug#11764086,\
      however MySQL's fix is incomplete for MariaDB, so\
      this fix is slightly different.
    * In addition, this patch renames\
      Item\_func\_not\_all::top\_level() to is\_top\_level\_item()\
      to make it in line with the analogous methods of\
      Item\_in\_optimizer, and Item\_subselect.
    * Analysis:
      * It is possible to determine whether a predicate is\
        NULL-rejecting only if it is a top-level one. However,\
        this was not taken into account for Item\_in\_optimizer.\
        As a result, a NOT IN predicate was erroneously\
        considered as NULL-rejecting, and the NULL-complemented\
        rows generated by the outer join were rejected before\
        being checked by the NOT IN predicate.
    * Solution:
      * Change Item\_in\_optimizer to be considered as\
        NULL-rejecting only if it a top-level predicate.
* [Revision #3162](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3162)\
  Wed 2011-08-17 12:32:15 +0400
  * field\_conv.cc: added comments\
    opt\_range.cc: modified print\_key() so that it doesn't do memory re-allocs when\
    printing multipart keys over varchar columns. When it did, key printout in\
    debug trace was interrupted with my\_malloc/free printouts.
* [Revision #3161](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3161) \[merge]\
  Wed 2011-08-17 12:02:02 +0400
  * Merge
    * [Revision #3155.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3155.1.2)\
      Wed 2011-08-17 11:57:01 +0400
      * [Bug #826935](https://bugs.launchpad.net/bugs/826935) Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed
        * add\_ref\_to\_table\_cond() should not just overwrite pre\_idx\_push\_select\_cond\
          with the contents tab->select\_cond.
        * pre\_idx\_push\_select\_cond exists precisely for the reason that it may contain\
          a condition that is a strict superset of what is in tab->select\_cond.
        * The fix is to inject generated equality into pre\_idx\_push\_select\_cond.
* [Revision #3160](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3160)\
  Tue 2011-08-16 22:48:35 -0700
  * Fixed [Bug #825035](https://bugs.launchpad.net/bugs/825035).
    * The value of maybe\_null flag should be saved for the second execution\
      of a prepared statement from SELECT that uses an outer join.
* [Revision #3159](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3159) \[merge]\
  Tue 2011-08-16 23:45:08 +0300
  * Merge fix for small\_blocksize.test
    * [Revision #3157.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3157.1.1) \[merge]\
      Tue 2011-08-16 19:02:15 +0300
      * Merge with 5.2
* [Revision #3158](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3158) \[merge]\
  Tue 2011-08-16 21:54:48 +0400
  * Merge
    * [Revision #3155.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3155.1.1)\
      Tue 2011-08-16 21:42:25 +0400
      * [Bug #818280](https://bugs.launchpad.net/bugs/818280): crash in do\_copy\_not\_null() in maria-5.3 with semijoin
        * Make simplify\_joins() set maybe\_null=FALSE for tables that were on the\
          inner sides of inner joins and then were moved to the inner sides of semi-joins.
* [Revision #3157](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3157) \[merge]\
  Tue 2011-08-16 15:51:40 +0300
  * Automatic merge with 5.2
    * [Revision #2732.44.20](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.20)\
      Tue 2011-08-16 13:28:20 +0300
      * Fixed build failure in embedded library regarding that decrease\_user\_connections() was not declared
    * [Revision #2732.44.19](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.19)\
      Tue 2011-08-16 13:06:07 +0300
      * If mysqld `--log-warnings=3` or higher, then print all check and repair warnings for MyISAM tables to the log.\
        This is useful when trying to find out why an automatic myisam repair failes.
    * [Revision #2732.44.18](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.18)\
      Tue 2011-08-16 12:32:06 +0300
      * Fixed bug that MAX\_USER\_CONNECTIONS was not working properly in all situations (which could cause aborted connects)\
        thd->user\_connect is now handled in thd->clenup() which will ensure that it works in all context (including slaves).\
        I added also some DBUG\_ASSERT() to ensure that things are working correctly.
    * [Revision #2732.44.17](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.17)\
      Mon 2011-08-15 23:53:55 +0300
      * Fixed recovery crash [Bug #814806](https://bugs.launchpad.net/bugs/814806) "Unclean shutdown corrupted Aria table blocking startup"
* [Revision #3156](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3156) \[merge]\
  Mon 2011-08-15 22:14:08 +0300
  * Automatic merge with 5.2
    * [Revision #2732.44.16](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.16) \[merge]\
      Mon 2011-08-15 20:42:29 +0300
      * Merge in bug fix from 5.1
    * [Revision #2732.44.15](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.15)\
      Mon 2011-08-15 20:40:13 +0300
      * Increase server version
    * [Revision #2732.44.14](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.14)\
      Mon 2011-08-15 16:39:53 +0300
      * Fixes bugs found by testcase for [Bug #815022](https://bugs.launchpad.net/bugs/815022) and [Bug #726374](https://bugs.launchpad.net/bugs/726374) "ma\_blockrec.c:3000: write\_block\_record: Assertion \`cur\_block\[1].page\_count == 0' failed with a multi-index Aria workload"
        * The issues were:
          * For some tables with a lot of not packed fields, we didn't allocate enough memory in head page which caused DBUG\_ASSERT's
          * Removed wrong DBUG\_ASSERT()
          * Fixed a problem with underflow() where it generates a key page where all keys didn't fit.
          * Max key length is now limited by block\_size/3 (was block\_size /2). This is required for underflow() to work with packed keys.
    * [Revision #2732.44.13](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.13) \[merge]\
      Fri 2011-08-12 15:51:05 +0300
      * Autmatic merge with 5.1
    * [Revision #2732.44.12](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.12)\
      Wed 2011-08-10 22:44:39 +0300
      * Fixed [Bug #814054](https://bugs.launchpad.net/bugs/814054) 'Assertion \`block->hash\_link == hash\_link && hash\_link->block == block' in ma\_pagecache.c:2275 with Aria'
        * Replaced old DBUG\_ASSERT with a new correct one + a comment.
    * [Revision #2732.44.11](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.11)\
      Wed 2011-08-10 13:08:19 +0300
      * Fixes [MySQL Bug #48972](https://bugs.mysql.com/bug.php?id=48972): mysqldump `--insert-ignore` leaves set unique\_checks=0.\
        This fixes a bug that when you use mysqldump `--no-create-info` to generate a dump that you want to merge with an existing table,\
        you can get an innodb table with duplicated unique keys.\
        Patch originally by Eric Bergen.
    * [Revision #2732.44.10](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.10)\
      Mon 2011-08-08 14:53:52 +0300
      * Optimize mutex usage.
* [Revision #3155](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3155)\
  Fri 2011-08-12 14:31:40 +0300
  * Fixed test results after the tests adding.
* [Revision #3154](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3154)\
  Fri 2011-08-12 13:54:41 +0300
  * Early check of subquery cache hit rate added to limit its performance impact in the worst case.
* [Revision #3153](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3153)\
  Fri 2011-08-12 11:39:29 +0300
  * [Bug #781508](https://bugs.launchpad.net/bugs/781508): Take relevant test cases from MySQL 5.6 feature preview trees
    * Identified all test cases in the MySQL file subquery.inc that are\
      not present in MariaDB. This patch adds the test cases that are:
      * not present in MySQL 5.5, and
      * already fixed in [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md)
    * The patch adds test cases for the following mysql-trunk bugs:
      * bug 12763207 - not a bug, mysql-trunk, added test case
      * [MySQL Bug #50257](https://bugs.mysql.com/bug.php?id=50257) - not a bug, mysql-trunk, added test case
      * bug 11765699 - not a bug, mysql-trunk, added test case
      * bug 12616253 - not a bug, mysql-trunk, added test case
    *   The comparison was based on the following version of\
        mysql-trunk:

        ```
        revno: 3350 [merge]
         committer: Marko Mäkelä <marko.makela@oracle.com>
         branch nick: mysql-trunk
         timestamp: Mon 2011-08-08 12:42:09 +0300
         message:
         Merge mysql-5.5 to mysql-trunk.
        ```
* [Revision #3152](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3152)\
  Fri 2011-08-12 11:23:50 +0300
  * Protect statistic variables of subquery cache.
* [Revision #3151](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3151)\
  Thu 2011-08-11 22:34:41 -0700
  * Added a test case for [Bug #823835](https://bugs.launchpad.net/bugs/823835) - a duplicate of [Bug #823189](https://bugs.launchpad.net/bugs/823189).
* [Revision #3150](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3150)\
  Thu 2011-08-11 20:24:32 -0700
  * Fixed [Bug #823189](https://bugs.launchpad.net/bugs/823189).
    * The method Item\_ref::not\_null\_tables() returned incorrect bitmap\
      for outer references to view columns. This could cause an invalid\
      conversion of an outer join into an inner join that could lead\
      to a wrong result set for a query with a correlated subquery over\
      an outer join whose where condition had an outer reference to a view.
* [Revision #3149](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3149)\
  Thu 2011-08-11 12:11:04 -0700
  * Fixed [Bug #823826](https://bugs.launchpad.net/bugs/823826).
    * The method Item\_func\_isnull::update\_used\_tables() erroneously did not\
      update cached values stored in the fields used\_tables\_cache and\
      const\_item\_cache of the Item\_func\_isnull objects. As a result the\
      Item\_func\_isnull::used\_tables() returned wrong bitmaps and, as a\
      consequence, push-down predicates could be attached to wrong tables.
* [Revision #3148](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3148)\
  Tue 2011-08-09 18:34:26 +0300
  * [Bug #781508](https://bugs.launchpad.net/bugs/781508): Take relevant test cases from MySQL 5.6 feature preview trees
    * Identified all test cases in the MySQL file subquery\_mat.inc that are\
      not present in MariaDB. In total found 8 test cases for the following\
      MySQL bugs:
      * [MySQL Bug #49630](https://bugs.mysql.com/bug.php?id=49630) - not a bug in MariaDB, added test case
      * [MySQL Bug #52538](https://bugs.mysql.com/bug.php?id=52538) - not a bug in MariaDB, added test case (checked with VG)
      * [MySQL Bug #53103](https://bugs.mysql.com/bug.php?id=53103) - not a bug in MariaDB, added test case
      * [MySQL Bug #54511](https://bugs.mysql.com/bug.php?id=54511) - not a bug in MariaDB, added test case
      * [MySQL Bug #56367](https://bugs.mysql.com/bug.php?id=56367) - not a bug in MariaDB, added test case
      * [MySQL Bug #59833](https://bugs.mysql.com/bug.php?id=59833) - not a bug in MariaDB, added test case
      * bug 11852644 - not a bug in MariaDB, added test case
      * bug 12668294 - not a bug in MariaDB, added test case
    * All of these MySQL bugs are not present in [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md).
    *   The comparison was based on the following version of\
        mysql-trunk:

        ```
        revno: 3350 [merge]
         committer: Marko Mäkelä <marko.makela@oracle.com>
         branch nick: mysql-trunk
         timestamp: Mon 2011-08-08 12:42:09 +0300
         message:
         Merge mysql-5.5 to mysql-trunk.
        ```
* [Revision #3147](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3147)\
  Tue 2011-08-09 10:28:57 +0300
  * Fix [Bug #817384](https://bugs.launchpad.net/bugs/817384)
    * This bug is a special case of [Bug #813447](https://bugs.launchpad.net/bugs/813447).
    * Analysis:
      * Constant optimization finds that the condition t2.a = 1\
        can be used to access the primary key of table 't2'. As\
        a result both outer table t1,t2 are considered as constant\
        when we reach the execution phase. At the same time, during\
        constant optimization, the IN predicate is not evaluated\
        because it is expensive.
      *   When execution of the outer query reaches do\_select(),\
          control flow enter the branch:

          ```
          if (join->table_count == join->const_tables)
           { ... }
          ```
  * This branch checks only the WHERE and HAVING clauses,\
    but doesn't check the ON clauses of the query. Since the\
    IN predicate was not evaluated during optimization, it is\
    not evaluated at all, thus execution doesn't detect that\
    the ON clause is FALSE.\\
  * Solution:
  * Similar to the patch for [Bug #813447](https://bugs.launchpad.net/bugs/813447), exclude system\
    tables from constant substitution based on unique key\
    lookups if there is an expensive ON condition on the\
    inner table.
* [Revision #3146](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3146)\
  Mon 2011-08-08 22:02:10 -0700
  * Fixed [Bug #819716](https://bugs.launchpad.net/bugs/819716).\
    Do not optimize derived table for the second time ever.
* [Revision #3145](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3145) \[merge]\
  Tue 2011-08-09 01:57:08 +0400
  * Merge fix for [Bug #822134](https://bugs.launchpad.net/bugs/822134)
    * [Revision #3138.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3138.1.3)\
      Tue 2011-08-09 01:37:06 +0400
      * [Bug #822134](https://bugs.launchpad.net/bugs/822134): Invalid plan and wrong result set for Q20 from DBT3 benchmark set
        * create\_ref\_for\_key() has the code that walks KEYUSE array and tries to use\
          maximum number of keyparts for ref (and eq\_ref and ref\_or\_null) access.\
          When one constructs ref access for table that is inside a SJ-Materialization\
          nest, it is not possible to use tables that are ouside the nest (because\
          materialization is performed before they have any "current value").\
          The bug was caused by this function not taking this into account.
* [Revision #3144](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3144) \[merge]\
  Mon 2011-08-08 23:12:34 +0400
  * Merge
    * [Revision #3141.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3141.1.1)\
      Mon 2011-08-08 22:37:53 +0400
      * Update test results for previous cset
* [Revision #3143](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3143)\
  Mon 2011-08-08 18:40:41 +0200
  * Fix long xtradb shutdown on Windows XP
    * The reason for the long shutdown is hanging in io threads. It appears\
      that just closing completion port on XP does not necessarily signal\
      thread waiting in GetIOCompletionStatus() (even if this works fine\
      on later Windows versions)
    * The fix is to wakeup background threads using PostQueuedCompletionStatus()\
      with a special 'key' parameter indicating shutdown.
* [Revision #3142](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3142)\
  Mon 2011-08-08 18:01:33 +0200
  * [Bug #882689](https://bugs.launchpad.net/bugs/882689) - crash during startup on XP.
    * The reason for the crash is Innodb assertion after trying to load condition variables function\
      dynamically and not finding them
    * The fix is to skip dynamic loading if srv\_use\_native\_conditions is FALSE. srv\_use\_native\_conditions\
      is derived from Windows version and would be FALSE on XP and TRUE on later Windows.
    * This is the same handling as in MySQL 5.. In Maria 5.3 srv\_use\_native\_conditions check was\
      presumably lost in the downporting.
* [Revision #3141](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3141) \[merge]\
  Fri 2011-08-05 22:07:06 +0400
  * Merge
    * [Revision #3138.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3138.1.2)\
      Fri 2011-08-05 22:01:49 +0400
      * Backport of:

```
revno: 2876.47.174
revision-id: jorgen.loland@oracle.com-20110519120355-qn7eprkad9jqwu5j
parent: mayank.prasad@oracle.com-20110518143645-bdxv4udzrmqsjmhq
committer: Jorgen Loland <jorgen.loland@oracle.com>
branch nick: mysql-trunk-11765831
timestamp: Thu 2011-05-19 14:03:55 +0200
message:
 BUG#11765831: 'RANGE ACCESS' MAY INCORRECTLY FILTER 
 AWAY QUALIFYING ROWS
.
 The problem was that the ranges created when OR'ing two 
 conditions could be incorrect. Without the bugfix, 
 "I <> 6 OR (I <> 8 AND J = 5)" would create these ranges:
.
 "NULL < I < 6",
 "6 <= I <= 6 AND 5 <= J <= 5",
 "6 < I < 8",
 "8 <= I <= 8 AND 5 <= J <= 5",
 "8 < I"
.
 While the correct ranges is
 "NULL < I < 6",
 "6 <= I <= 6 AND 5 <= J <= 5",
 "6 < I"
.
 The problem occurs when key_or() ORs
 (1) "NULL < I < 6, 6 <= I <= 6 AND 5 <= J <= 5, 6 < I" with 
 (2) "8 < I AND 5 <= J <= 5"
.
 The reason for the bug is that in key_or(), SEL_ARG *tmp is 
 used to point to the range in (1) above that is merged with 
 (2) while key1 points to the root of the red-black tree of 
 (1). When merging (1) and (2), tmp refers to the "6 < I" 
 part whereas the root is the "6 <= ... AND 5 <= J <= 5" part. 
.
 key_or() decides that the tmp range needs to be split into
 "6 < I < 8, 8 <= I <= 8, 8 < I", in which next_key_part of the 
 second range should be that of tmp. However, next_key_part is
 set to key1->next_key_part ("5 <= J <= 5") instead of 
 tmp->next_key_part (empty). Fixing this gives the correct but
 not optimal ranges:
 "NULL < I < 6",
 "6 <= I <= 6 AND 5 <= J <= 5",
 "6 < I < 8",
 "8 <= I <= 8",
 "8 < I"
.
 A second problem can be seen above: key_or() may create 
 adjacent ranges that could be replaced with a single range. 
 Fixes for this is also included in the patch so that the range
 above becomes correct AND optimal:
 "NULL < I < 6",
 "6 <= I <= 6 AND 5 <= J <= 5",
 "6 < I"
.
 Merging adjacent ranges like this gives a slightly lower cost 
 estimate for the range access.
```

* [Revision #3138.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3138.1.1)\
  Thu 2011-08-04 18:20:02 +0400
  *   Backport of:

      ```
      revno: 3363.3.16
      revision-id: jorgen.loland@oracle.com-20110506132631-5wickj6dvrh1dpj6
      parent: alexander.nozdrin@oracle.com-20110506132138-46459va9vcbd4nz0
      committer: Jorgen Loland <jorgen.loland@oracle.com>
      branch nick: mysql-trunk-11765831
      timestamp: Fri 2011-05-06 15:26:31 +0200
      message:
       BUG#11765831: 'RANGE ACCESS' MAY INCORRECTLY FILTER
       AWAY QUALIFYING ROWS
      .
       Preparation patch (does not include fix for the bug):
      .
       - Extensively document key_or()
       - Remove tab indentations from key_or()
       - Minor code changes like using existing utility functions
       in key_or()
      ```
* [Revision #3140](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3140)\
  Wed 2011-08-03 13:58:46 +0200
  * Limit query length in error log to 64K, to avoid output of full blobs
* [Revision #3139](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3139)\
  Wed 2011-08-03 13:42:53 +0200
  * Enhance crash reporting. Fix
    * [Bug #819711](https://bugs.launchpad.net/bugs/819711) : optimizer\_switch must be reported on segfault
    * [Bug #820169](https://bugs.launchpad.net/bugs/820169): Full query text must be reported on crash
* [Revision #3138](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3138) \[merge]\
  Mon 2011-08-01 11:05:30 +0200
  * Automerge 5.2->5.3
    * [Revision #2732.44.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.9)\
      Mon 2011-08-01 10:56:24 +0200
      * After-merge fix of result file (MARIA <-> Aria)
* [Revision #3137](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3137) \[merge]\
  Sun 2011-07-31 22:59:55 +0200
  * Automerge 5.2->5.3
* [Revision #3136](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3136)\
  Fri 2011-07-29 17:09:16 -0700
  * Fixed [Bug #817360](https://bugs.launchpad.net/bugs/817360).
    * This problem could be observed for queries with nested outer joins\
      for which the not\_exist optimization were applicable.\
      The problem was caused by the code of the patch for [MySQL Bug #49322](https://bugs.mysql.com/bug.php?id=49322)\
      that erroneously forced the return to the previous nested loop\
      level when the join algorithm successfully builds a partial record\
      for an embedded outer to which the not\_exist optimization could be\
      applied.
    * Actually the immediate return to the previous nested loops level\
      is correct only if this partial record is rejected by a predicate\
      pushed down to one of the inner tables of this outer join. Otherwise\
      attempts to find extensions of this record must be made.
* [Revision #3135](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3135)\
  Thu 2011-07-28 17:10:29 +0300
  * Subquery cache going on disk management fix: Do not go on disk if hit rate is not good.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
