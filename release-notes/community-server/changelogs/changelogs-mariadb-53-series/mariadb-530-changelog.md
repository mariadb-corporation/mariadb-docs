# MariaDB 5.3.0 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.3.0) |[Release Notes](../../old-releases/5.3/5.3.0.md) |**Changelog**\
(page:`1 [2](mariadb-530-changelog-p2.md)[3](mariadb-530-changelog-p3.md)[4](mariadb-530-changelog-p4.md)[5](mariadb-530-changelog-p5.md)[6](mariadb-530-changelog-p6.md)`\
) |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 26 July 2011

* [Revision #3134](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3134)\
  Fri 2011-07-22 23:47:28 -0700
  * Removed settings of 'derived\_merge' to 'on' in ps tests.
* [Revision #3133](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3133)\
  Fri 2011-07-22 21:39:55 -0700
  * Fixed a crash with pbxt.subselect when 'derived\_merge' is set off in\
    the optimizer switch.
* [Revision #3132](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3132) \[merge]\
  Thu 2011-07-21 15:55:08 -0700
  * Merge.
    * [Revision #3121.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3121.1.1)\
      Thu 2011-07-21 14:23:08 -0700
      * Made the optimizer switches 'derived\_merge' and 'derived\_with\_keys'\
        off by default.
* [Revision #3131](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3131)\
  Thu 2011-07-21 23:37:40 +0300
  * Fix for [Bug #806071](https://bugs.launchpad.net/bugs/806071)
    * In case of two views with subqueries it is dificult to decide about order of injected ORDER BY clauses.
    * A simple solution is just prohibit ORDER BY injection if there is other order by.
* [Revision #3130](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3130)\
  Thu 2011-07-21 19:14:34 +0400
  * [Bug #803457](https://bugs.launchpad.net/bugs/803457): Wrong result with semijoin + view + outer join in maria-5.3-subqueries-mwl90
  * Correct handling of outer joins + DuplicateWeedout (docs pending)
* [Revision #3129](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3129) \[merge]\
  Thu 2011-07-21 15:50:25 +0300
  * Merge from 5.2
  * [Revision #2732.44.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.6) \[merge]\
    Thu 2011-07-21 15:21:22 +0300
    * Test fix merge.
    * [Revision #2643.143.28](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.28)\
      Thu 2011-07-21 15:14:16 +0300
      * Fixed PBXT test.
  * [Revision #2732.44.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.5) \[merge]\
    Thu 2011-07-21 13:15:09 +0300
    * Merge 5.1->5.2
    * [Revision #2643.143.27](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.27)\
      Thu 2011-07-21 12:29:00 +0300
      * Removed incorrect fix and its test suite (the test suit is duplicate).
      * Fixed explains of previous patch.
    * [Revision #2643.143.26](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.26)\
      Thu 2011-07-21 11:45:19 +0300
      * The function description added.
    * [Revision #2643.143.25](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.25)\
      Thu 2011-07-21 11:20:55 +0300
      * Fix of [Bug #777809](https://bugs.launchpad.net/bugs/777809)
      * There are 2 volatile condition constructions AND/OR constructions and fields(references) when first\
        good supported to be top elements of conditions because it is normal practice\
        (see copy\_andor\_structure for example) fields without any expression in the condition is really rare\
        and mostly useless case however it could lead to problems when optimiser changes/moves them unaware\
        of other variables referring to them. An easy solution of this problem is just to replace single field\
        in a condition with equivalent expression well supported by the server ( -> != 0).
  * [Revision #2732.44.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.4) \[merge]\
    Tue 2011-07-12 22:42:00 +0200
    * 5.1 merge
    * [Revision #2643.143.24](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.24)\
      Tue 2011-07-12 08:58:33 +0200
      * bugfix: create internal temporary tables in mysql\_tmpdir, not in datadir
    * [Revision #2643.143.23](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.23)\
      Sun 2011-07-10 13:38:15 +0200
      * Post-fix for [Bug #808233](https://bugs.launchpad.net/bugs/808233) : replace uint with "unsigned int" in mysql.h.pp, too
    * [Revision #2643.143.22](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.22) \[merge]\
      Sun 2011-07-10 12:33:08 +0200
      * merge
      * [Revision #2643.146.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.146.4) \[
        * merge]\
          Sun 2011-07-10 12:31:09 +0200
        * merge
      * [Revision #2643.146.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.146.3)\
        Sun 2011-07-10 12:27:42 +0200
        * [Bug #808233](https://bugs.launchpad.net/bugs/808233): Undefined uint in typelib.h
        * Fix is to replace uint in public header with unsigned int. uint is not guaranteed to be defined by system headers.
    * [Revision #2643.143.21](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.21)\
      Thu 2011-07-07 22:37:38 +0200
      * protocol safety fix:
      * before strlen(db) we need to be sure that db lies within packet boundaries
  * [Revision #2732.44.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.44.3)\
    Fri 2011-07-08 00:13:24 +0200
    * protocol safety fix:
    * before strlen(db) we need to be sure that
      * db lies within packet boundaries.
      * same for client\_plugin.
* [Revision #3128](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3128)\
  Thu 2011-07-21 00:43:37 -0700
  * Fixed [Bug #813447](https://bugs.launchpad.net/bugs/813447).
  * Do not make substitution of a single-row table if it is an inner\
    table of an outer join with on expression containing an expensive\
    subquery.
* [Revision #3127](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3127)\
  Wed 2011-07-20 21:55:55 -0700
  * Fixed [Bug #791761](https://bugs.launchpad.net/bugs/791761).
  * An aggregating query over an empty set of a join of two tables\
    with a rejecting HAVING clause erroneously could return a row.\
    It could happen in the cases when the optimizer made a conclusion\
    that the aggregating set was empty.\
    Wrong results were produced because the server missed initial\
    setting for aggregation functions in the mentioned cases.
* [Revision #3126](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3126) \[merge]\
  Wed 2011-07-20 16:49:36 -0700
  * Merge.
  * [Revision #3123.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3123.1.1)\
    Wed 2011-07-20 16:09:28 -0700
    * Fixed [Bug #702301](https://bugs.launchpad.net/bugs/702301).
  * The function matching\_cond should take into account that\
    there may be always false constant conjunctive conditions\
    that has not been evaluated yet,for example, conjunctive\
    conditions with non-correlated subqueries.
* [Revision #3125](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3125)\
  Wed 2011-07-20 16:02:26 -0700
  * Adjusted the results of the pbxt.subselect test after the push\
    of the patch for [Bug #780386](https://bugs.launchpad.net/bugs/780386).
* [Revision #3124](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3124)\
  Wed 2011-07-20 21:48:41 +0300
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
* [Revision #3123](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3123)\
  Wed 2011-07-20 11:56:28 +0400
  * Fix a compile error, and most likely a bug: jtb\_table\_no holds table number, not table->map.
* [Revision #3122](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3122) \[merge]\
  Wed 2011-07-20 11:21:30 +0400
  * Merge fix for [Bug #806524](https://bugs.launchpad.net/bugs/806524)
  * [Revision #3120.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3120.1.1)\
    Wed 2011-07-20 01:31:40 +0400
    * [Bug #806524](https://bugs.launchpad.net/bugs/806524): Assertion \`join->best\_read < 1.7976931348623157e+308 with table\_elimination=on and derived\_merge=on\
      reset\_nj\_counters() used to rely on the fact that join nests have\
      table->table==NULL. This ceased to be true wit new derived table\
      optimizations. Use test for table->nested\_join!=NULL instead.
* [Revision #3121](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3121)\
  Tue 2011-07-19 23:19:10 +0300
  * Fixed [Bug #800696](https://bugs.launchpad.net/bugs/800696).
  * The problem was that optimizer removes some outer references (it they are\
    constant for example) and the list of outer items built during prepare phase is\
    not actual during execution phase when we need it as the cache parameters.\
    First solution was use pointer on pointer on outer reference Item and\
    initialize temporary table on demand. This solved most problem except case\
    when optimiser also reduce Item which contains outer references ('OR' in\
    this bug test suite).
  * The solution is to build the list of outer reference items on execution\
    phase (after optimization) on demand (just before temporary table creation)\
    by walking Item tree and finding outer references among Item\_ident\
    (Item\_field/Item\_ref) and Item\_sum items.
  * Removed depends\_on list (because it is not neede any mnore for the cache, in the place where it was used it replaced with upper\_refs).
  * Added processor (collect\_outer\_ref\_processor) and get\_cache\_parameters() methods to collect outer references (or other expression parameters in future).
* [Revision #3120](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3120)\
  Tue 2011-07-19 22:22:40 +0400
  * [Bug #803303](https://bugs.launchpad.net/bugs/803303): Wrong result with semijoin=on, outer join in maria-5.3-subqueries-mwl90
  * Add testcase.
* [Revision #3119](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3119)\
  Tue 2011-07-19 13:48:16 +0400
  * Buildbot fixes: add `--sorted-result`
* [Revision #3118](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3118) \[merge]\
  Tue 2011-07-19 11:45:46 +0400
  * Merge
  * [Revision #3110.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3110.1.1) \[merge]\
    Fri 2011-07-15 03:37:16 +0400
    * Merge
    * [Revision #3108.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3108.1.1)\
      Fri 2011-07-15 02:58:34 +0400
      * [Bug #803457](https://bugs.launchpad.net/bugs/803457): Wrong result with semijoin + view + outer join in maria-5.3-subqueries-mwl90
        * (This is not a real fix for this bug, even though it makes it to no longer repeat)
        * Semi-join subquery predicates, i.e. ... WHERE outer\_expr IN (SELECT ...) may have null-rejecting properties,\
          may allow to convert outer joins into inner.
        * When convert\_subq\_to\_sj() injected IN-equality into parent's WHERE/ON clause, it didn't call\
          $new\_cond->top\_level\_item(), which would cause null-rejecting properties to be lost.
        * Fixed, now the mentioned outer-to-inner conversion will really take place.
* [Revision #3117](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3117) \[merge]\
  Mon 2011-07-18 23:21:48 -0700
  * Merge.
  * [Revision #3114.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3114.2.1)\
    Sun 2011-07-17 23:12:31 -0700
    * Fixed [Bug #793448](https://bugs.launchpad.net/bugs/793448).
    * This bug could lead to wrong result sets for a query over a\
      materialized derived table or view accessed by a multi-component\
      key.
    * It happened because the function get\_next\_field\_for\_derived\_key\
      was supposed to update its argument, and it did not do it.
* [Revision #3116](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3116) \[merge]\
  Mon 2011-07-18 20:40:50 -0700
  * Merge.
  * [Revision #3114.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3114.1.1)\
    Mon 2011-07-18 20:05:33 -0700
    * Fixed valgrind problems of the patch for bug 794901.
* [Revision #3115](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3115)\
  Mon 2011-07-18 23:45:38 +0300
  * Fix [Bug #782305](https://bugs.launchpad.net/bugs/782305)
  * Analysis:
    * Both the wrong result and the valgrind warning were a result\
      of incomplete cleanup of the MIN/MAX subquery rewrite. At the\
      first execution of the query, the non-aggregate subquery is\
      transformed into an aggregate MIN/MAX subquery. During the\
      fix\_fields phase of the MIN/MAX function, it sets the property\
      st\_select\_lex::with\_sum\_func to true.
    * The second execution of the query finds this flag to be ON.\
      When optimization reaches the same MIN/MAX subquery\
      transformation, it tests if the subquery is an aggregate or not.\
      Since select\_lex->with\_sum\_func == true from the previous\
      execution, the transformation executes the second branch that\
      handles aggregate subqueries. This substitutes the subquery\
      Item into a Item\_maxmin\_subselect. At the same time elsewhere\
      it is assumed that the subquery Item is of type\
      Item\_allany\_subselect. Ultimately this results in casting the\
      actual object to the wrong class, and calling the wrong\
      any\_value() method from empty\_underlying\_subquery().
  * Solution:
    * Cleanup the st\_select\_lex::with\_sum\_func property in the case\
      when the MIN/MAX transformation was performed for a non-aggregate\
      subquery, so that the transformation can be repeated.
* [Revision #3114](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3114) \[merge]\
  Sun 2011-07-17 00:52:07 -0700
  * Merge with the latest 5.3 code.
  * [Revision #3100.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3100.1.2)\
    Sat 2011-07-16 23:57:43 -0700
    * Fixed [Bug #794901](https://bugs.launchpad.net/bugs/794901).
    * Also:\
      \*
      1. simplified the code of the function mysql\_derived\_merge\_for\_insert.
      2.
         2. moved merge of views/dt for multi-update/delete to the prepare stage.
      3.
         3. the list of the references to the candidates for semi-join now is\
            allocated in the statement memory.
  * [Revision #3100.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3100.1.1) \[merge]\
    Mon 2011-07-11 14:00:44 -0700
    * Merge with the latest 5.3 code.
  * [Revision #3025.1.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3025.1.7)\
    Mon 2011-06-13 22:18:40 -0700
    * Fixed a typo in the patch for [Bug #794890](https://bugs.launchpad.net/bugs/794890).
  * [Revision #3025.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3025.1.6)\
    Mon 2011-06-13 19:03:03 -0700
    * Fixed [Bug #794890](https://bugs.launchpad.net/bugs/794890).
    * Changed the code that processing of multi-updates and multi-deletes\
      with multitable views at the prepare stage.
    * A proper solution would be: never to perform any transformations of views\
      before and at the prepare stage. Yet it would require re-engineering\
      of the code that checks privileges and updatability of views.\
      Ultimately this re-engineering has to be done to provide a clean solution\
      for INSERT/UPDATE/DELETE statements that use views.
    * Fixed a valgrind problem in the function TABLE::use\_index.
* [Revision #3113](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3113) \[merge]\
  Fri 2011-07-15 12:16:46 +0300
  * Merge of subquery cache off by default.
  * [Revision #3102.3.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3102.3.1)\
    Fri 2011-07-15 11:36:36 +0300
    * Make subquery cache off by default.
* [Revision #3112](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3112) \[merge]\
  Fri 2011-07-15 09:17:22 +0300
  * Automatic merge.
  * [Revision #3106.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3106.1.3)\
    Fri 2011-07-15 00:23:57 +0300
    * [MWL#68](https://askmonty.org/worklog/?tid=68) efficient partial matching
    * Added an initial set of feature-specific test cases
    * Handled the special case where the materialized subquery of an\
      IN predicates consists of only NULL values.
    * Fixed a bug where making Item\_in\_subselect a constant,\
      didn't respect its null\_value value.
  * [Revision #3106.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3106.1.2)\
    Thu 2011-07-14 12:53:00 +0300
    * Fix [Bug #777691](https://bugs.launchpad.net/bugs/777691)
    * Analysis:
      * For some of the re-executions of the correlated subquery the\
        where clause is false. In these cases the execution of the\
        subquery detects that it must generate a NULL row because of\
        implicit grouping. In this case the subquery execution reaches\
        the following code in do\_select():
      * while ((table= li++))\
        mark\_as\_null\_row(table->table);
      * This code marks all rows in the table as complete NULL rows.\
        In the example, when evaluating the field t2.f10 for the second\
        row, all bits of Field::null\_ptr\[0] are set by the previous call\
        to mark\_as\_null\_row(). Then the call to Field::is\_null()\
        returns true, resulting in a NULL for the MAX function.
      * Thus the lines above are not suitable for subquery re-execution\
        because mark\_as\_null\_row() changes the NULL bits of each table\
        field, and there is no logic to restore these fields.
    * Solution:
      * The call to mark\_as\_null\_row() was added by the fix for bug [Bug #613029](https://bugs.launchpad.net/bugs/613029). Therefore removing the fix for [Bug #613029](https://bugs.launchpad.net/bugs/613029) corrects\
        this wrong result. At the same time the test for [Bug #613029](https://bugs.launchpad.net/bugs/613029)\
        behaves correctly because the changes of [MWL#89](https://askmonty.org/worklog/?tid=89) result in a\
        different execution path where:
      * the constant subquery is evaluated via JOIN::exec\_const\_cond
      * detecting that it has an empty result triggers the branch
      * if (zero\_result\_cause)\
        return\_zero\_rows()
      * return\_zero\_rows() calls mark\_as\_null\_row().
  * [Revision #3106.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3106.1.1) \[merge]\
    Thu 2011-07-14 10:22:18 +0300
    * Automatic merge.
    * [Revision #3102.2.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3102.2.2)\
      Thu 2011-07-14 00:15:07 +0300
      * Fix [Bug #809266](https://bugs.launchpad.net/bugs/809266)
      * Analysis:
        * This is a bug in [MWL#68](https://askmonty.org/worklog/?tid=68), where it was incorrectly assumed\
          that if there is a match in the only non-null key, then\
          if there is a covering NULL row on all remaining NULL-able\
          columns there is a partial match. However, this is not the case,\
          because even if there is such a null-only sub-row, it is not\
          guaranteed to be part of the matched sub-row. The matched sub-row\
          and the NULL-only sub-row may be parts of different rows.
        * In fact there are two cases:
          * there is a complete row with only NULL values, and
          * all nullable columns contain only NULL values.
        * These two cases were incorrectly mixed up in the class member\
          subselect\_partial\_match\_engine::covering\_null\_row\_width.
      * Solution:
        * The solution is to:
        * split covering\_null\_row\_width into two members:\
          has\_covering\_null\_row, and has\_covering\_null\_columns, and
          * take into account each state during initialization and\
            execution.
    * [Revision #3102.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3102.2.1) \[merge]\
      Wed 2011-07-13 17:11:46 +0300
      * Merged the fix for [Bug #608744](https://bugs.launchpad.net/bugs/608744)
      * [Revision #3091.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3091.1.1)\
        Wed 2011-07-13 17:09:09 +0300
        * Fixed [Bug #809245](https://bugs.launchpad.net/bugs/809245)
        * In addition to the bug fix explained below, the patch performs\
          few renames, and adds some comments to avoid similar problems.
        * Analysis:
          * The failed assert was due to a bug in [MWL#68](https://askmonty.org/worklog/?tid=68), where it was\
            incorrectly assumed that the size of the bitmap\
            subselect\_rowid\_merge\_engine::null\_only\_columns should be\
            the same as the size of the array of Ordered\_keys.
          * The bitmap null\_only\_columns contains bits to mark columns\
            that contain only NULLs. Therefore the indexes of the bits\
            to be set in null\_only\_columns are different from the indexes\
            of the Ordered\_keys. If there is a NULL-only column that appears\
            in a table after the last partial match column with Ordered\_key,\
            this NULL-only column would require setting a bit with index\
            bigger than the size of the bitmap null\_only\_columns.
          * Accessing such a bit caused the failed assert.
        * Solution:
          * Upon analysis, it turns out that null\_only\_columns is not needed\
            at all, because we are looking for partial matches, and having\
            such columns guarantees that there is a partial match for any\
            corresponding outer value.
        * Therefore the patch removes subselect\_rowid\_merge\_engine::null\_only\_columns.
* [Revision #3111](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3111)\
  Thu 2011-07-14 22:24:59 -0700
  * Changed the default setting of the optimizer switch 'optimize\_join\_buffer\_size'.\
    Made it 'off' by default.
* [Revision #3110](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3110)\
  Fri 2011-07-15 03:34:00 +0400
  * Test result update forgotten in pre-previous cset.
* [Revision #3109](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3109)\
  Fri 2011-07-15 03:29:38 +0400
  * Valgrind fix for the previous cset:
  * {ha\_myisam,ha\_maria}::index\_read\_idx\_map should also initialize end\_range, because index condition\
    function will attempt to check it. We initialize it like index\_init() does.
* [Revision #3108](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3108) \[merge]\
  Thu 2011-07-14 20:06:46 +0400
  * Merge
    * [Revision #3102.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3102.1.1)\
      Thu 2011-07-14 01:53:05 +0400
      * Disable LooseScan and FirstMatch when outer joins are present.
* [Revision #3107](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3107)\
  Thu 2011-07-14 17:44:37 +0400
  * [Bug #778434](https://bugs.launchpad.net/bugs/778434) Wrong result with in\_to\_exists=on in maria-5.3-mwl89
  * Make {ha\_myisam,ha\_maria}::index\_read\_idx\_map check pushed index condition.
  * Address review feedback (added comments)
* [Revision #3106](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3106) \[merge]\
  Wed 2011-07-13 22:19:32 -0700
  * Merge.
  * [Revision #3104.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3104.1.1)\
    Wed 2011-07-13 21:06:28 -0700
    * Fixed [Bug #809179](https://bugs.launchpad.net/bugs/809179).
    * The attribute not\_null\_tables could be calculated incorrectly in the\
      function SELECT\_LEX::update\_used\_tables for queries over views\
      with row items in the WHERE clause. It happened because no\
      implementation of the virtual callback function eval\_not\_null\_tables\
      was provided for the class Item\_row.
    * Also slightly optimized the code calculating the value of the maybe\_null\
      flag for tables in the function SELECT\_LEX::update\_used\_tables.
* [Revision #3105](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3105)\
  Wed 2011-07-13 20:00:28 -0700
  * Corrected the patch for [Bug #809206](https://bugs.launchpad.net/bugs/809206) to fix valgrind failures.
* [Revision #3104](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3104) \[merge]\
  Wed 2011-07-13 12:14:35 -0700
  * Merge.
  * [Revision #3101.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3101.1.1)\
    Tue 2011-07-12 23:47:35 -0700
    * Fixed [Bug #809206](https://bugs.launchpad.net/bugs/809206).
    * The bitmap of used tables must be evaluated for the select list of every\
      materialized derived table / view and saved in a dedicated field.
    * This is also applied to materialized subqueries.
* [Revision #3103](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3103)\
  Wed 2011-07-13 11:05:33 -0700
  * Corrected the code of the recent patch that had changed the base\
    class for Item\_func\_xor. Added the implementation of the\
    subst\_argument\_checker virtual method that the objects of this\
    class used to use before the patch.
  * Reverted the previous result changes in sunselect\_sj and\
    subselect\_sj\_jcl6.
* [Revision #3102](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3102)\
  Wed 2011-07-13 16:49:52 +0400
  * Update test results for previous cset
* [Revision #3101](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3101) \[merge]\
  Tue 2011-07-12 13:02:19 +0400
  * Merge
  * [Revision #3095.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3095.1.2)\
    Mon 2011-07-11 23:48:35 +0400
    * Port of code for: (part of testcase is in mysql-test/t/subquery\*.test and will be ported separately)
      * [Bug #11766642](https://bugs.launchpad.net/bugs/11766642): crash in Item\_field::register\_field\_in\_read\_map\
        with view
      * (Former [MySQL Bug #59793](https://bugs.mysql.com/bug.php?id=59793))
      * Prior to the refactoring in this patch, Item\_cond\_xor behaved\
        partially as an Item\_cond and partially as an Item\_func. The\
        reasoning behind this was that XOR is currently not optimized\
        (thus should be Item\_func instead of Item\_cond), but it was\
        planned optimize it in the future (thus, made Item\_cond anyway\
        to ease optimization later).
      * Even though Item\_cond inherits from Item\_func, there are\
        differences between these two. One difference is that the\
        arguments are stored differently. Item\_cond stores them in a\
        list while Item\_func store them in an args\[].
      * [MySQL Bug #45221](https://bugs.mysql.com/bug.php?id=45221) was caused by Item\_cond\_xor storing arguments in\
        the list while users of the objects would look for them in\
        args\[]. The fix back then was to store the arguments in both\
        locations.
      * In this bug, Item\_cond\_xor initially gets two Item\_field\
        arguments. These are stored in the list inherited from\
        Item\_cond and in args\[] inherited from Item\_func. During\
        resolution, find\_field\_in\_view() replaces the Item\_fields\
        stored in the list with Item\_direct\_view\_refs, but args\[]\
        still points to the unresolved Item\_fields. This shows that\
        the fix for 45221 was incorrect.
      * The refactoring performed in this patch removes the confusion\
        by making the XOR item an Item\_func period. A neg\_transformer()\
        is also implemented for Item\_func\_xor to improve performance\
        when negating XOR expressions. An XOR is negated by negating\
        one of the operands.
  * [Revision #3095.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3095.1.1)\
    Mon 2011-07-11 17:13:16 +0400
    * Alternate version of MySQL's fix for [MySQL Bug #49453](https://bugs.mysql.com/bug.php?id=49453).
    * The cause of the crash is sj\_nest->sj\_subq\_pred->unit->first\_select()->item\_list\
      contains "stale" items for the second execution. By "stale" I mean that they have\
      item->fixed==FALSE, and they are Item\_field object instead of Item\_direct\_view\_ref.
    * The solution is to use sj\_nest->sj\_subq\_pred->unit->first\_select()->ref\_pointer\_array.\
      Surprisingly, that array contains items that are ok.
    * Oracle team has introduced and is using NESTED\_JOIN::sj\_inner\_exprs, but we go without that\
      and always copy the ref\_pointer\_array.
* [Revision #3100](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3100)\
  Mon 2011-07-11 10:56:48 -0700
  * Fixed [Bug #793386](https://bugs.launchpad.net/bugs/793386).\
    Auto-generated names for view field items must be allocated in\
    the statement memory, not in the execution memory of the statement.
* [Revision #3099](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3099)\
  Sun 2011-07-10 17:19:45 -0700
  * Fixed [Bug #806504](https://bugs.launchpad.net/bugs/806504).\
    Missing initialization of the bitmap not\_null\_tables\_cache to 0\
    in the function Item\_func::eval\_not\_null\_tables caused this bug.\
    This function is called indirectly from the function\
    SELECT\_LEX::update\_used\_tables after merging mergeable views and\
    derived tables into the main query. The leaf tables of resulting\
    query may change their bitmap numbers after this merge. That's why\
    the not\_null\_tables\_cache bitmaps must be updated. Due to the bug\
    mentioned above the result of the re-evaluation of the\
    not\_null\_tables\_cache turned out to be incorrect in some cases.\
    This could trigger an invalid conversion of outer joins into\
    inner joins leading to invalid query result sets.
  * Also removed an implicit conversion from int to bool in the function\
    SELECT\_LEX::update\_used\_tables.
* [Revision #3098](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3098) \[
  * merge]\
    Sun 2011-07-10 13:41:30 +0200
  * merge
* [Revision #3097](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3097) \[
  * merge]\
    Sun 2011-07-10 13:01:00 +0200
  * merge
* [Revision #3096](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3096)\
  Sat 2011-07-09 22:34:56 -0700
  * Fixed [Bug #806097](https://bugs.launchpad.net/bugs/806097).\
    The value of THD::used tables should be re-evaluated after merges\
    of views and derived tables into the main query.\
    Now it's done in the function SELECT\_LEX::update\_used\_tables.\
    The re-evaluation of the 'used\_table' bitmaps for the items\
    in HAVING, GROUP BY and ORDER BY clauses has been added as well.
* [Revision #3095](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3095)\
  Sat 2011-07-09 16:33:40 +0400
  * Semi-join fixes: make COST\_VECT objects survive add\_io(add\_io\_cnt=0, add\_avg\_cost=...) calls without\
    getting NaN in internal fields.
* [Revision #3094](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3094)\
  Sat 2011-07-09 13:47:41 +0400
  * \[No BUG#] Fixes for problems discovered when running mysql-trunk's subquery testsuite
* [Revision #3093](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3093) \[merge]\
  Sat 2011-07-09 11:20:15 +0400
  * Merge @@optimizer\_switch default settings changes into 5.3
  * [Revision #3089.2.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3089.2.4)\
    Fri 2011-07-08 22:01:02 +0400
    * Update test results for previous csets.
  * [Revision #3089.2.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3089.2.3)\
    Fri 2011-07-08 19:09:30 +0400
    * Make table\_elimination=on|off flag to be always present in @@optimizer\_switch.
  * [Revision #3089.2.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3089.2.2)\
    Fri 2011-07-08 18:49:53 +0400
    * Forgot to add these two files when setting semijoin=off by default:
* Scavenged subquery tests from testcases other than t/subselect\*.test and put them into single file
* [Revision #3089.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3089.2.1)\
  Fri 2011-07-08 18:46:47 +0400
  * Set the default to be mrr=off,mrr\_sort\_keys=off:
    * Set the default
    * Adjust the testcases so that 'new' tests are run with optimizations turned on.
    * Pull out relevant tests from "irrelevant" tests and run them with optimizations on.
    * Run range.test and innodb.test with both mrr=on and mrr=off
* [Revision #3092](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3092) \[merge]\
  Fri 2011-07-08 16:42:59 -0700
  * Merge.
  * [Revision #3090.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3090.1.1)\
    Fri 2011-07-08 16:39:28 -0700
    * Fixed [Bug #806510](https://bugs.launchpad.net/bugs/806510).\
      The bug was caused by an incorrect code of the function\
      Item\_direct\_view\_ref::replace\_equal\_field introduced in the\
      patch for bugs 717577, 724942. The function erroneously\
      returned the wrapped field instead of the Item\_direct\_view\_ref\
      object itself in the cases when no replacement happened.
    * The bug masked two other minor bugs that could result in not\
      quite correct output of the EXPLAIN command for some queries.\
      They were fixed in the patch as well.
* [Revision #3091](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3091) \[merge]\
  Fri 2011-07-08 10:56:46 +0300
  * Merge test cases for bugs that were fixed by [MWL#89](https://askmonty.org/worklog/?tid=89).
  * [Revision #3089.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3089.1.4)\
    Fri 2011-07-08 10:51:53 +0300
    * Test for [Bug #611382](https://bugs.launchpad.net/bugs/611382)
    * The bug itself has been fixed by [MWL#89](https://askmonty.org/worklog/?tid=89).
  * [Revision #3089.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3089.1.3)\
    Fri 2011-07-08 08:52:30 +0300
    * Test case for [Bug #611396](https://bugs.launchpad.net/bugs/611396)
    * The bug itself has been fixed by [MWL#89](https://askmonty.org/worklog/?tid=89).
  * [Revision #3089.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3089.1.2)\
    Thu 2011-07-07 17:22:28 +0300
    * Test for [Bug #612543](https://bugs.launchpad.net/bugs/612543)
    * The bug itself has been fixed by [MWL#89](https://askmonty.org/worklog/?tid=89).
  * [Revision #3089.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3089.1.1)\
    Thu 2011-07-07 17:07:13 +0300
    * Test case for [Bug #611690](https://bugs.launchpad.net/bugs/611690)
    * The bug itself has been fixed by [MWL#89](https://askmonty.org/worklog/?tid=89).
* [Revision #3090](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3090) \[merge]\
  Thu 2011-07-07 13:06:40 -0700
  * Merge.
  * [Revision #3088.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3088.1.1)\
    Thu 2011-07-07 13:04:48 -0700
    * Fixed [Bug #806477](https://bugs.launchpad.net/bugs/806477).\
      The offending query returns a wrong result set because the optimizer\
      erroneously eliminated the where condition evaluated it to TRUE.\
      The cause of this wrong transformation was that the flag maybe\_null\
      for an inner table of the outer join was not set to TRUE after the\
      table had replaced the wrapping view.\
      Now the function SELECT\_LEX::update\_used\_tables resets the value\
      of the maybe\_null flag for each leaf table of the query after all\
      merges of views have been done.
* [Revision #3089](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3089)\
  Thu 2011-07-07 16:28:26 +0300
  * Fix [Bug #806943](https://bugs.launchpad.net/bugs/806943)
    * Analysis:\
      This bug is yet another incarnation of the generic problem\
      where optimization of the outer query triggers evaluation\
      of a subquery, and this evaluation performs a destructive\
      change to the subquery plan. Specifically a temp table is\
      created for the DISTINCT operation that replaces the\
      original subquery table. Later, select\_describe() attempts\
      to print the table name, however, there is no corresponding\
      TABLE\_LIST object to the internal temp table, so we get a\
      crash. Execution works fine because it is not interested in\
      the corresponding TABLE\_LIST object (or its name).
    * Solution:\
      Similar to other such bugs, block the evaluation of expensive\
      Items in convert\_const\_to\_int().
* [Revision #3088](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3088) \[merge]\
  Wed 2011-07-06 17:26:01 -0700
  * Merge.
  * [Revision #3086.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3086.1.1)\
    Wed 2011-07-06 17:24:42 -0700
    * Fixed [Bug #806431](https://bugs.launchpad.net/bugs/806431).\
      The function generate\_derived\_keys\_for\_table incorrectly handled\
      the cases when a materialized view or derived table could be accessed\
      by different keys on the same fields if these keys depended on the\
      same tables.
* [Revision #3087](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3087)\
  Wed 2011-07-06 21:32:07 +0300
  * [Bug #802979](https://bugs.launchpad.net/bugs/802979)\
    Adjust PBXT test results.
* [Revision #3086](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3086) \[merge]\
  Wed 2011-07-06 17:27:38 +0300
  * Merge the fix for [Bug #802979](https://bugs.launchpad.net/bugs/802979)
  * [Revision #3070.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3070.1.1)\
    Mon 2011-07-04 14:51:16 +0300
    * Fix [Bug #802979](https://bugs.launchpad.net/bugs/802979)
    * Analysis:\
      This bug consists of two related problems that are\
      result of too early evaluation of single-row subqueries\
      during the optimization phase of the outer query.
      * Several optimizer code paths try to evaluate single-row\
        subqueries in order to produce a constant and use that\
        constant for further optimzation.
      * When the execution of the subquery peforms destructive\
        changes to the representation of the subquery, and these\
        changes are not anticipated by the subsequent optimization\
        phases of the outer query, we tipically get a crash or\
        failed assert.
      * Specifically, in this bug the inner-most suqbuery with\
        DISTINCT triggers a substitution of the original JOIN\
        object by a single-table JOIN object with a temp table\
        needed to perform the DISTINCT operation (created by\
        JOIN::make\_simple\_join).
      * This substitution breaks EXPLAIN because:\
        a) in the first example JOIN::cleanup no longer can\
        reach the original table of the innermost subquery, and\
        close all indexes, and\
        b) in this second test query, EXPLAIN attempts to print\
        the name of the internal temp table, and crashes because\
        the temp table has no name (NULL pointer instead).
    * Solution:
      * a) fully disable subquery evaluation during optimization\
        in all cases - both for constant propagation and range\
        optimization, and
      * b) change JOIN::join\_free() to perform cleanup irrespective\
        of EXPLAIN or not.
* [Revision #3085](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3085) \[merge]\
  Wed 2011-07-06 10:30:51 +0400
  * Merge fix for [Bug #611704](https://bugs.launchpad.net/bugs/611704)
  * [Revision #3082.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3082.1.1)\
    Wed 2011-07-06 10:21:31 +0400
    * [Bug #611704](https://bugs.launchpad.net/bugs/611704): Crash in replace\_where\_subcondition with nested subquery and semijoin=on
    * SELECT\_LEX::merge\_subquery should not set "(\*in\_subq)->emb\_on\_expr\_nest= derived" for subqueries that\
      are in the ON expressions of semi-joins.
* [Revision #3084](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3084)\
  Tue 2011-07-05 22:38:38 +0200
  * fix compile warnings
* [Revision #3083](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3083) \[merge]\
  Tue 2011-07-05 21:46:53 +0200
  * merge Windows performance patches into 5.3
  * [Revision #2732.40.14](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.14)\
    Sun 2011-06-26 01:07:39 +0200
    * set errno to EBADF, if file descriptor < 0 in my\_write()
  * [Revision #2732.40.13](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.13)\
    Sun 2011-06-19 17:19:22 +0200
    * Fix "make dist" : add my\_winfile.c and my\_winerr.c to EXTRA\_DIST list
  * [Revision #2732.40.12](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.12)\
    Sun 2011-06-19 00:51:41 +0200
    * add missing DBUG\_RETURN
  * [Revision #2732.40.11](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.11)\
    Sun 2011-06-19 00:29:49 +0200
    * fix compile error on \*nix
  * [Revision #2732.40.10](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.10)\
    Sat 2011-06-18 21:56:47 +0200
    * dummy change to trigger the buildbot
  * [Revision #2732.40.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.9)\
    Fri 2011-06-17 00:29:22 +0200
    * Point to the correct documentation on building in our KB.
  * [Revision #2732.40.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.8)\
    Thu 2011-06-16 14:51:50 +0200
    * Fix [MySQL Bug #21978](https://bugs.mysql.com/bug.php?id=21978) : 'flush\_time' value set for 1800 sec
    * This setting is obsolete now. It could makes sense in the past, situations open file handles\
      limit was low. It does not make sense anymore to flush all files every 1.5 hours now, after 2048\
      myisam file limit is removed as fix to [MySQL Bug #24509](https://bugs.mysql.com/bug.php?id=24509).
  * [Revision #2732.40.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.7)\
    Thu 2011-06-16 14:33:09 +0200
    * Accept innodb\_flush\_method values previously allowed on Unix only\
      map them to corresponding Windows CreateFile flags,\
      O\_DSYNC=>FILE\_FLAG\_WRITE\_THROUGH\
      ALL\_O\_DIRECT=>FILE\_FLAG\_NO\_BUFFERING
    * Ability to specify innodb\_flush\_method=O\_DSYNC fixes [MySQL Bug #31876](https://bugs.mysql.com/bug.php?id=31876)\
      (InnoDB commit performance slow on Windows XP), by removing an extra FlushFileBuffers()\
      call overhead.
  * [Revision #2732.40.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.6)\
    Mon 2011-06-13 02:38:16 +0200
    * fix warnings
  * [Revision #2732.40.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.5)\
    Sun 2011-06-12 16:44:41 +0200
    * fix mismerge
  * [Revision #2732.40.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.4) \[merge]\
    Sun 2011-06-12 16:26:43 +0200
    * merge
      * [Revision #2732.43.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.43.1)\
        Sun 2011-06-12 16:09:28 +0200
        * Backport fix for [MySQL Bug #56405](https://bugs.mysql.com/bug.php?id=56405) :\
          use native windows condition variables and rwlocks in mysys, if Windows supports it.
  * [Revision #2732.40.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.3) \[merge]\
    Sun 2011-06-12 16:24:00 +0200
    * merge
      * [Revision #2732.42.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.42.1)\
        Sun 2011-06-12 16:07:18 +0200
        * Fix XtraDB [Bug #714143](https://bugs.launchpad.net/bugs/714143) :\
          Windows native async io is disabled.
        * The patch uses completion ports for asynchronous IO notification ,\
          instead of formerly used notification via event . This also removes\
          the limit of 64 async IOs per background IO thread (this limit was\
          forced by using WaitForMultipleObjects in previous AIO implementation)
  * [Revision #2732.40.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.2) \[merge]\
    Sun 2011-06-12 16:11:05 +0200
    * merge
      * [Revision #2732.41.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.41.1) \[merge]\
        Sun 2011-06-12 15:54:49 +0200
        * Backport scalability improvements for innodb on Windows , [MySQL Bug #52102](https://bugs.mysql.com/bug.php?id=52102)\
          ()
      * [Revision #2732.36.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.36.4)\
        Sat 2011-06-04 20:06:01 +0200
        * improve Innodb locking primitives on Windows ([MySQL Bug #52102](https://bugs.mysql.com/bug.php?id=52102), and fix OS\_FILE\_LIMIT - on Windows it is about 16 millions
  * [Revision #2732.40.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.40.1) \[merge]\
    Sun 2011-06-12 16:10:38 +0200
    * merge
      * [Revision #2732.39.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.39.1)\
        Sun 2011-06-12 15:52:07 +0200
        * Backport Fix for [MySQL Bug #24509](https://bugs.mysql.com/bug.php?id=24509) - 2048 file descriptor limit on windows needs increasing.
        * The patch replaces the use of the POSIX I/O interfaces in mysys on Windows with\
          the Win32 API calls (CreateFile, WriteFile, etc). The Windows HANDLE for the open\
          file is stored in the my\_file\_info struct, along with a flag for append mode\
          (because the Windows API does not support opening files in append mode in all cases)\
          The default max open files has been increased to 16384 and can be increased further\
          by setting `--`max-open-files= during the server start.
        * Noteworthy benefit of this patch is that it removes limits from the table\_cache size -\
          allowing for more simultaneus users
* [Revision #3082](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3082) \[merge]\
  Tue 2011-07-05 21:48:50 +0400
  * Merge fix for [Bug #803365](https://bugs.launchpad.net/bugs/803365)
  * [Revision #3073.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3073.1.1)\
    Tue 2011-07-05 21:22:13 +0400
    * [Bug #803365](https://bugs.launchpad.net/bugs/803365): Crash in pull\_out\_semijoin\_tables with outer join + semijoin + derived tables in maria-5.3 with [WL#106](https://askmonty.org/worklog/?tid=106)
    * Don't perform table pullout out of semi-join nests that have nested outer joins.
* [Revision #3081](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3081)\
  Tue 2011-07-05 15:28:15 +0200
  * [MWL#163](https://askmonty.org/worklog/?tid=163) [Bug #798213](https://bugs.launchpad.net/bugs/798213): Remove the `--`innodb-release-locks-early feature.
  * The [Bug #798213](https://bugs.launchpad.net/bugs/798213) exposes a design flaw in `--`innodb-release-locks-early.\
    It does not work with InnoDB crash recovery, so it breaks transactional\
    integrety. So remove the feature.
* [Revision #3080](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3080)\
  Tue 2011-07-05 10:32:49 +0400
  * Update test results for the previous cset.
* [Revision #3079](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3079)\
  Tue 2011-07-05 01:44:15 +0400
  * Change the default @@optimizer\_switch setting from`semijoin=on,firstmatch=on,loosescan=on`\
    to`semijoin=off,firstmatch=off,loosescan=off`
  * Adjust the testcases:
    * Modify subselect\*.test and join\_cache.test so that all tests\
      use the same execution paths as before (i.e. optimizations that\
      are being tested are enabled)
    * Let all other test files run with the new default settings (i.e.\
      with new optimizations disabled)
    * Copy subquery testcases from these files into t/subselect\_extra.test\
      which will run them with new optimizations enabled.
* [Revision #3078](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3078) \[merge]\
  Mon 2011-07-04 11:02:35 -0700
  * Merge.
  * [Revision #3076.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3076.1.1)\
    Sun 2011-07-03 14:59:01 -0700
    * Fixed [Bug #804686](https://bugs.launchpad.net/bugs/804686).\
      The assert conditions in the functions Item\_direct\_ref\_to\_ident::transform\
      and Item\_direct\_ref\_to\_ident::compile could be not valid after constant\
      propagation when fields and field references may be substituted for constants.\
      Not only these invalid asserts have been removed, but the functions containing\
      them have been removed as well because now Item\_ref::transform and\
      Item\_ref::compile can be used instead of them.
* [Revision #3077](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3077) \[merge]\
  Mon 2011-07-04 17:27:46 +0300
  * Automatic merge
* [Revision #3076](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3076)\
  Sat 2011-07-02 17:37:59 +0300
  * Fixed compilation & test issues found by buildbot
* [Revision #3075](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3075)\
  Fri 2011-07-01 21:53:47 -0700
  * Fixed [Bug #804515](https://bugs.launchpad.net/bugs/804515).\
    If no index is used to access a materialized derived table or view\
    then the value of TABLE\_REF::key for this table must be (-1).
* [Revision #3074](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3074) \[merge]\
  Fri 2011-07-01 15:35:34 +0300
  * Automatic merge
  * [Revision #3066.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3066.1.5) \[merge]\
    Fri 2011-07-01 15:16:10 +0300\
    Merge with 5.2
  * [Revision #3066.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3066.1.4)\
    Fri 2011-07-01 15:08:30 +0300
    * Added progress reporting for alter table, LOAD DATA INFILE and for aria tables: check table, repair table, analyze table.
      * The client gets a progress report message that triggers a callback function if requested with mysql\_options(MYSQL\_PROGRESS\_CALLBACK, function)
      * Added Progress field last to 'show processlist'
      * Stage, Max\_stage and Progress field added to information\_schema.progresslist
      * The 'mysql' client by defaults enables progress reports when the output is a tty.
      * Added progress\_report\_time time variable to configure how often progress reports is sent to client
    * Added read only system variable 'in\_transaction' which is 1 if we have executed a BEGIN statement.
  * [Revision #3066.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3066.1.3)\
    Fri 2011-07-01 14:16:36 +0300
    * Updated result
  * [Revision #3066.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3066.1.2)\
    Fri 2011-07-01 10:20:11 +0200
    * Added read only system variable 'in\_transaction' which tells if there's\
      an active transaction.
    * fixed a bug - not clearing "in transaction" status on set @@autocommit=1
  * [Revision #3066.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3066.1.1)\
    Fri 2011-07-01 09:05:15 +0200
    * Removed check\_license() function
* [Revision #3073](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3073)\
  Fri 2011-07-01 13:22:23 +0400
  * Buildbot run fixes:
    * update suite/pbxt/r/status.result with changes that arise from addition of Handler\_tmp\_% status variables.
* [Revision #3072](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3072) \[merge]\
  Fri 2011-07-01 12:45:45 +0400
  * Merge first chunk of OJ+SJ fixes into 5.3
  * [Revision #3068.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3068.1.3)\
    Thu 2011-06-30 20:49:11 +0400
    * Fix buildbot failures:
      * JOIN::prepare would have set JOIN::table\_count to incorrect value (bad merge of MWL 106)
      * optimize\_keyuse() would use table-bit as table number\
        (the change in optimize\_keyuse is also the reason for query plan changes. Not\
        expected to have much effect because only handles cases of no index statistics)
      * st\_select\_lex::register\_dependency\_item() ignored the fact that some of the\
        selects on the dependency paths could have been merged to their parents (because they\
        were mergeable VIEWs)
      * Undo the incorrect fix in Item\_subselect::recalc\_used\_tables(): do not call\
        fix\_after\_pullout() for Item\_subselect::Ref\_to\_outside members.
  * [Revision #3068.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3068.1.2)\
    Wed 2011-06-29 15:07:28 +0400
    * [Bug #802965](https://bugs.launchpad.net/bugs/802965): Crash in do\_copy\_not\_null with semijoin=on in maria-5.3
      * The crash was because a NOT NULL table column inside the subquery was considered NULLable\
        because the code thought it was on the inner side of an outer join nest.
      * Fixed by making correct distinction between tables inside outer join nests and inside semi-join nests.
  * [Revision #3068.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3068.1.1) \[merge]\
    Wed 2011-06-29 11:52:26 +0400
    * Merge
      * [Revision #3062.3.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3062.3.4)\
        Tue 2011-06-28 18:25:02 +0400
        * Remove garbage comment
      * [Revision #3062.3.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3062.3.3)\
        Tue 2011-06-28 17:42:10 +0400
        * Followup to previous commit:
          * Update test results
          * Fix a problem with PS:
            * convert\_subq\_to\_sj() should not save where to prep\_where or on\_expr to prep\_on\_expr.
            * After an unmerged subquery predicate has been pulled, it should call fix\_after\_pullout() for\
              outer\_refs.
      * [Revision #3062.3.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3062.3.2)\
        Tue 2011-06-28 00:51:26 +0400
        * Test: enable semi-join processing for cases of semi-joins and outer joins, except for the case when the\
          subquery is in the ON clause.
      * [Revision #3062.3.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3062.3.1) \[merge]\
        Mon 2011-06-27 23:40:58 +0400
        * Merge semi-join+outer-join fixes into 5.3
* [Revision #3071](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3071)\
  Thu 2011-06-30 19:32:19 -0700
  * Fixed [Bug #803851](https://bugs.launchpad.net/bugs/803851).\
    The function generate\_derived\_keys\_for\_table should set the value of\
    the number of keys for the derived table to 0 before it starts\
    generating key definitions for the table. It's important as the\
    function can be called twice by the optimizer for a derived table\
    if the query contains a subquery to which the IN-EXIST transformation\
    is applicable.
  * Fixed a valgrind complain.
* [Revision #3070](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3070)\
  Wed 2011-06-29 20:07:24 -0700
  * Fixed [Bug #802845](https://bugs.launchpad.net/bugs/802845).\
    If the expression for a derived table contained a clause LIMIT 0\
    SELECT from such derived table incorrectly returned a non-empty set.
  * Fixed by ensuring JOIN::do\_send\_rows to be updated after the call\
    of st\_select\_lex\_unit::set\_limit that sets the value of\
    JOIN::unit->select\_limit\_cnt.

[MariaDB 5.3.0](../../old-releases/5.3/5.3.0.md) Changelog — page:`1 [2](mariadb-530-changelog-p2.md)[3](mariadb-530-changelog-p3.md)[4](mariadb-530-changelog-p4.md)[5](mariadb-530-changelog-p5.md)[6](mariadb-530-changelog-p6.md)`

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
