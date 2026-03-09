# MariaDB 5.3.0 Changelog p4

[Download](https://downloads.askmonty.org/mariadb/5.3.0) |[Release Notes](../../old-releases/5.3/5.3.0.md) |**Changelog**\
(page:[1](mariadb-530-changelog.md)[2](mariadb-530-changelog-p2.md)[3](mariadb-530-changelog-p3.md) 4 [5](mariadb-530-changelog-p5.md)[6](mariadb-530-changelog-p6.md)\
) |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 26 July 2011

* [Revision #2945](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2945) \[merge]\
  Tue 2011-03-15 12:30:48 -0700
  * Merge.
  * [Revision #2928.3.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2928.3.1)\
    Thu 2011-03-03 18:24:41 -0800
    * Fixed [Bug #702322](https://bugs.launchpad.net/bugs/702322):\
      The bug was a result of the fix for [Bug #668644](https://bugs.launchpad.net/bugs/668644) that turned out to be\
      not quite correct. A problem appeared with HAVING conditions containing\
      more than one predicate. If a query with an ORDER BY clause uses\
      such HAVING condition and the required order can be obtained with\
      a range/index scan then the HAVING condition has to be pushed into\
      two different formulas (items). To be able to do it we have to create\
      a copy of the ANDOR structure of the pushed condition.
* [Revision #2944](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2944) \[merge]\
  Sun 2011-03-13 16:57:05 +0000
  * Merge in the fix for [Bug #730604](https://bugs.launchpad.net/bugs/730604), and a corrected fix for [Bug #719198](https://bugs.launchpad.net/bugs/719198),\
    after Monty's review.
  * [Revision #2933.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2933.2.1)\
    Sun 2011-03-13 15:03:26 +0000
    * Fix [Bug #719198](https://bugs.launchpad.net/bugs/719198), [Bug #730604](https://bugs.launchpad.net/bugs/730604)
    * Analysis ( [Bug #719198](https://bugs.launchpad.net/bugs/719198) ):
      * The assert failed because the execution code for\
        partial matching is designed with the assumption that\
        NULLs on the left side are detected as early as possible,\
        and a NULL result is returned before any lookups are\
        performed at all.
      * However, in the case of an Item\_cache object on the left\
        side, null was not detected properly, because detection\
        was done via Item::is\_null(), which is not implemented at\
        all for Item\_cache, and resolved to the default Item::is\_null()\
        which always returns FALSE.
    * Solution:
      * Imlpement Item::is\_null().
    * Analysis ( [Bug #730604](https://bugs.launchpad.net/bugs/730604) ):
      * The method Item\_field::is\_null() determines if an item is NULL from its\
        Item\_field::field object. However, for Item\_fields that represent internal\
        temporary tables, Item\_field::field represents the field of the original\
        table that was the source for the temporary table (in this case t1.f3).\
        Both in the committed test case, and in the original bug report the current\
        value of t1.f3 is not NULL. This results in an incorrect count of NULLs\
        for this column. As a consequence, all related Ordered\_key buffers are\
        allocated with incorrect sizes. Depending on the exact query and data,\
        these incorrect sizes result in various crashes or failed asserts.
    * Solution:
      * The correct value of the current field of the internal temp table is\
        in Item\_field::result\_field. This value is determined by\
        Item::is\_null\_result().
* [Revision #2943](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2943) \[merge]\
  Sun 2011-03-13 03:50:14 -0700
  * Merge
  * [Revision #2933.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2933.1.1)\
    Mon 2011-03-07 22:09:21 -0800
    * Fixed [Bug #729039](https://bugs.launchpad.net/bugs/729039):\
      If join condition is of the form \<t2.key>=\<t1.no\_key> then the server\
      performs no index look-ups when looking for matching rows of t2 for\
      the rows from t1 with t1.no\_key=NULL. It happens because the function\
      add\_not\_null\_conds() injects an additional condition of the form\
      IS NOT NULL(\<t1.no\_key>) into the WHERE condition.\
      However if the join condition was of the form \<t.key>=\<outer\_ref> no\
      additional null rejecting predicate was generated. This could lead\
      to extra records in the result set if the value of \<outer\_ref> happened\
      to be NULL.
    * The new code injects null rejecting predicates of the form\
      IS NOT NULL(\<outer\_ref>) and evaluates them before the first row\
      the subquery is constructed.
* [Revision #2942](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2942)\
  Sat 2011-03-12 16:18:02 +0000
  * Fix wrong use of compiler flag causing the build to fail in handlersocket.
* [Revision #2941](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2941) \[merge]\
  Sat 2011-03-12 05:14:10 -0800
  * Merge.
  * [Revision #2934.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2934.1.1)\
    Sat 2011-03-12 00:49:03 -0800
    * Fixed LP bugs [Bug #729067](https://bugs.launchpad.net/bugs/729067) / [Bug #730466](https://bugs.launchpad.net/bugs/730466):\
      Do not reset the value of the item\_equal field in the Item\_field object\
      once it has been set.
* [Revision #2940](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2940) \[
  * merge]\
    Fri 2011-03-11 16:08:26 +0100
  * merge
* [Revision #2939](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2939) \[
  * merge]\
    Fri 2011-03-11 15:47:15 +0100
  * merge
* [Revision #2938](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2938) \[merge]\
  Fri 2011-03-11 15:20:24 +0100
  * merge [MWL#55](https://askmonty.org/worklog/?tid=55)
* [Revision #2937](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2937)\
  Wed 2011-03-09 17:55:00 +0200
  * Added item.real\_type() for easy access to the underlaying types for Item\_ref and Item\_cache\_wrapper()\
    This allows us to simplify and speed up some tests and also remove get\_cached\_item()
* [Revision #2936](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2936) \[merge]\
  Wed 2011-03-09 15:47:59 +0200
  * Merge with 5.2
* [Revision #2935](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2935)\
  Wed 2011-03-09 00:51:22 +0200
  * Added define to get rid of compiler warnings on system without DLOPEN
* [Revision #2934](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2934)\
  Tue 2011-03-08 23:23:44 +0200
  * Fix [Bug #719198](https://bugs.launchpad.net/bugs/719198)
    * Analysis:
      * The assert failed because the execution code for\
        partial matching is designed with the assumption that\
        NULLs on the left side are detected as early as possible,\
        and a NULL result is returned before any lookups are\
        performed at all.
      * However, in the case of an Item\_cache object on the left\
        side, null was not detected properly, because detection\
        was done via Item::is\_null(), which is not implemented at\
        all for Item\_cache, and resolved to the default Item::is\_null()\
        which always returns FALSE.
    * Solution:
      * Use the property Item::null\_value instead of is\_null(), which\
        is properly updated for Item\_cache objects as well.
* [Revision #2933](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2933) \[merge]\
  Fri 2011-03-04 18:54:30 +0300
  * Merge in MRR interface fixes.
  * [Revision #2931.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2931.1.1)\
    Fri 2011-03-04 12:06:03 +0300
    * MRR interface: change range\_info's type from char\* to range\_id\_t typedef. The goals are:
      * cleaner code
      * ability to change from using pointers to offsets at some point
* [Revision #2932](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2932)\
  Fri 2011-03-04 12:14:46 +0300
  * Make testcase pass on systems with lower\_case\_table\_names=2.
    * Generally, we should use only small letters for table names\
      but here it's easier to fix with one `--`replace.
* [Revision #2931](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2931) \[merge]\
  Fri 2011-03-04 01:30:25 +0300
  * Merge fix for [Bug #693747](https://bugs.launchpad.net/bugs/693747)
  * [Revision #2928.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2928.2.1)\
    Wed 2011-03-02 23:08:13 +0300
    * [Bug #693747](https://bugs.launchpad.net/bugs/693747): Assertion multi\_range\_read.cc:908: int DsMrr\_impl::dsmrr\_init
      * Make DsMrr\_impl::dsmrr\_init() handle the case of
        1. 1st MRR scan using DS-MRR strategy (i.e. doing key sorting and rowid sorting)
        2. 2nd MRR scan getting a buffer that's too small to fit one key element\
           and one rowid element, and so falling back to default MRR implementation
      * In this case, dsmrr\_init() is invoked with {primary\_handler, secondary\_handler}\
        initialized for DS-MRR scan and have to reset them to be initialized for the\
        default MRR scan.
      * (attempt 2, with simplified testcase)
* [Revision #2930](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2930) \[merge]\
  Fri 2011-03-04 01:28:02 +0300
  * Merge [Bug #707925](https://bugs.launchpad.net/bugs/707925).
  * [Revision #2928.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2928.1.1)\
    Fri 2011-03-04 00:54:10 +0300
    * [Bug #707925](https://bugs.launchpad.net/bugs/707925): Wrong result with join\_cache\_level=6 optimizer\_use\_mrr = force (incremental, BKA join)
      * The problem was that Mrr\_ordered\_index\_reader's interrupt\_read() and resume\_read() would\
        save and restore 1) index tuple 2) the rowid (as bytes returned by handler->position()). Clustered\
        primary key columns were not saved/restored.
      * They are not explicitly present in the index tuple (i.e. table->key\_info\[secondary\_key].key\_parts\
        doesn't list them), but they are actually there, in particular\
        table->field\[clustered\_primary\_key\_member].part\_of\_key(secondary\_key) == 1. Index condition pushdown\
        code \[correctly] uses the latter as inidication that pushed index condition can refer to clustered PK\
        members.
      * The fix was to make interrupt\_read()/resume\_read() to save/restore clustered primary key members as well,\
        so that we get correct values for them when evaluating pushed index condition.
    * \[3rd attempt: remove the debugging aids, fix comments in testcase]
* [Revision #2929](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2929)\
  Thu 2011-03-03 23:48:31 +0200
  * Fix [Bug #718763](https://bugs.launchpad.net/bugs/718763)
    * Analysis:
      * The reason for the crash was that the inner subquery was executed\
        via a scan on a final temporary table applied after all other\
        operations. This final operation is implemented by changing the\
        contents of the JOIN object of the subquery to represent a table\
        scan over the temp table. At the same time query optimization of\
        the outer subquery required evaluation of the inner subquery, which\
        happened before the actual EXPLAIN. The evaluation left the JOIN\
        object of the inner subquery in the changed state, where it represented\
        a table scan over a temp table, and EXPLAIN crashed because the temp\
        table is not associated with any table reference (TABLE\_LIST object).\
        The reason the JOIN was not restored was because its saving/restoration\
        was controlled by the join->select\_lex->uncacheable flag, which was\
        not set in the case of materialization.
    * Solution:
      * In the methods Item\_in\_subselect::\[single | row]\_value\_transformer() set:\
        select\_lex->uncacheable|= UNCACHEABLE\_EXPLAIN;
      * In addition, for symmetry, change:\
        master\_unit->uncacheable|= UNCACHEABLE\_EXPLAIN;
      * instead of UNCACHEABLE\_DEPENDENT because if a subquery was not\
        dependent initially, the changed methods do not change this\
        fact. The subquery may later become correlated if it is transformed\
        to an EXISTS query, but it may stay uncorrelated if executed via\
        materialization.
* [Revision #2928](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2928) \[merge]\
  Tue 2011-03-01 10:22:22 +0300
  * Merge fix for [Bug #725275](https://bugs.launchpad.net/bugs/725275)
  * [Revision #2925.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2925.1.1)\
    Tue 2011-03-01 00:29:59 +0300
    * [Bug #724275](https://bugs.launchpad.net/bugs/724275): Crash in JOIN::optimize in maria-5.3
      * Make equality-substitution-for-ref-access code in JOIN::optimize() treat join\_tab->ref.key\_copy correctly\
        (in the way create\_ref\_for\_key() has filled it).
* [Revision #2927](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2927)\
  Mon 2011-02-28 17:27:41 -0800
  * Moved the test case for [Bug #725050](https://bugs.launchpad.net/bugs/725050) into a new test file.
* [Revision #2926](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2926)\
  Sun 2011-02-27 22:37:46 -0800
  * Fixed [Bug #725050](https://bugs.launchpad.net/bugs/725050):\
    The bug in the function print\_keyuse() caused crashes if\
    hash join could be used. It happened because the function\
    ignored the fact that KEYUSE structures could be created\
    for hash joins as well.
* [Revision #2925](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2925) \[merge]\
  Sun 2011-02-27 10:14:11 -0800
  * Merge.
  * [Revision #2907.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2907.1.1)\
    Sun 2011-02-27 09:35:14 -0800
    * Minor corrections.
* [Revision #2924](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2924) \[merge]\
  Sun 2011-02-27 00:21:45 -0800
  * Merge
  * [Revision #2900.2.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2900.2.2)\
    Thu 2011-02-24 10:36:32 -0800
    * Made a newly added EXPLAIN platform independent.
  * [Revision #2900.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2900.2.1)\
    Wed 2011-02-23 22:23:12 -0800
    * BNLH algorithm always used a full table scan over the joined table\
      even in the cases when there existed range/index-merge scans that\
      were cheaper than the full table scan.
    * This was a defect/bug of the implementation of mwl #128.\
      Now hash join can work not only with full table scan of the joined\
      table, but also with full index scan, range and index-merge scans.
    * Accordingly, in the cases when hash join is used the column 'type'\
      in the EXPLAINs can contain now 'hash\_ALL', 'hash\_index', 'hash\_range'\
      and 'hash\_index\_merge'. If hash join is coupled with a range/index\_merge\
      scan then the columns 'key' and 'key\_len' contain info not only on\
      the used hash index, but also on the indexes used for the scan.
* [Revision #2923](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2923)\
  Sat 2011-02-26 23:09:58 +0300
  * Fix buildbot failure in fix of [Bug #723822](https://bugs.launchpad.net/bugs/723822)
* [Revision #2922](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2922) \[merge]\
  Fri 2011-02-25 21:45:21 +0300
  * Merge of fix for [Bug #723822](https://bugs.launchpad.net/bugs/723822)
  * [Revision #2920.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2920.1.1)\
    Fri 2011-02-25 21:43:57 +0300
    * [Bug #723822](https://bugs.launchpad.net/bugs/723822): Crash in get\_constant\_key\_infix with EXISTS ( SELECT .. DISTINCT )
      * Make get\_constant\_key\_infix() take into account that there may be SEL\_TREEs with\
        type=SEL\_ARG::MAYBE\_KEY, which it cannot process, because they are not real ranges\
        but rather indications that we might have been able to construct a range if we had\
        values for some other tables' fields.\
        (check\_quick\_select() already has such check)
* [Revision #2921](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2921) \[merge]\
  Fri 2011-02-25 20:32:18 +0200
  * automatic merge
  * [Revision #2919.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2919.1.1)\
    Fri 2011-02-25 20:15:27 +0200
    * Fixed compiler warnings
* [Revision #2920](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2920)\
  Thu 2011-02-24 23:32:00 +0300
  * [Bug #724537](https://bugs.launchpad.net/bugs/724537): innodb\_mysql.test fails with `--`embedded-server
    * Don't access THD::killed directly from ha\_innodb.cc. This is forbidden because\
      THD has different membership (and so, different member offsets) in regular and embedded server.\
      Access must be done through thd\_killed() function.
    * if we're interrupted by the user while in XtraDB, return the proper code.
* [Revision #2919](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2919)\
  Wed 2011-02-23 14:46:16 +0200
  * Fixed build issues
    * Linking now with g++ instead of gcc with 'compile-dist' to solve problems with handlersocket/client
    * Fixed bug in heap tables when doing handler read next-prev over last row
* [Revision #2918](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2918)\
  Wed 2011-02-23 02:06:58 +0200
  * Fixed compiler warnings and some test failures found by buildbot
* [Revision #2917](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2917) \[merge]\
  Tue 2011-02-22 11:30:51 +0200
  * Merge with main
  * [Revision #2914.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2914.1.1) \[merge]\
    Tue 2011-02-22 11:15:47 +0200
    * Merge in new handler and handlersocket code into 5.3 main
* [Revision #2916](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2916)\
  Mon 2011-02-21 20:17:26 +0100
  * [Bug #53240](https://bugs.launchpad.net/bugs/53240) :Fixed dependency to prevent occasional situations\
    where bison runs in parallel with the same input and output files
* [Revision #2915](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2915)\
  Mon 2011-02-21 14:23:44 +0100
  * Fix remaining 5.2 buildbot problems:
    * Cherrypick [Bug #688404](https://bugs.launchpad.net/bugs/688404) (PBXT crashes in debug/x64)
    * Fix unixism (rm -rf) in the test suite\_timeout
    * Avoid plugin tests on Windows/embedded, plugins do not and will not work here
* [Revision #2914](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2914)\
  Sat 2011-02-19 15:21:50 +0100
  * add newline at the end of file
* [Revision #2913](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2913)\
  Sat 2011-02-19 15:16:31 +0100
  * Fix remaining windows (32 bit) warnings.
* [Revision #2912](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2912)\
  Sat 2011-02-19 13:43:01 +0100
  * Fixed high-impact Windows 64bit warnings (at least 4000 of them)
* [Revision #2911](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2911)\
  Sat 2011-02-19 02:42:08 +0100
  * Fixed DBUG\_PRINT formatting (compile error on Linux with -Werror)
* [Revision #2910](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2910)\
  Fri 2011-02-18 23:31:01 +0100
  * Fix numerous warnings introduced in the last pushes on Windows
* [Revision #2909](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2909)\
  Fri 2011-02-18 22:38:22 +0100
  * Linker error, missing extern "C" for mi\_killed.
  * Fix is to move extern "C" at the start of header file.
* [Revision #2908](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2908) \[merge]\
  Fri 2011-02-18 21:45:32 +0200
  * Merge with bugfix
  * [Revision #2900.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2900.1.1)\
    Fri 2011-02-18 17:43:59 +0200
    * Fix for [Bug #711565](https://bugs.launchpad.net/bugs/711565) "Index Condition Pushdown can make a thread hold MyISAM locks as well as be unKILLable for long time"
      * In Maria/MyISAM: Release/re-acquire locks to give queries that wait on them a chance to make progress
      * In Maria/MyISAM: Change from numeric constants to ICP\_RES values.
      * In Maria: Do check index condition in maria\_rprev() (was lost in the merge/backport?)
      * In Maria/MyISAM/XtraDB: Check if the query was killed, and return immediately if it was.
      * Added new storage engine error: HA\_ERR\_ABORTED\_BY\_USER, for handler to signal that it detected a kill of the query and aborted
      * Authors: Sergey Petrunia & Monty
* [Revision #2907](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2907)\
  Sat 2011-02-12 18:43:22 +0100
  * Workaround CMake bug [view.php?id=11240](https://www.vtk.org/Bug/view.php?id=11240)\
    Huge static libraries like libmysqld might not build if /MACHINE flag is missing\
    for librarian with the correct processor architecture.
  * Fix is to add /MACHINE flag for x64 builds
* [Revision #2906](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2906)\
  Sat 2011-02-12 17:44:01 +0100
  * Fix test suite - adjust result files
* [Revision #2905](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2905)\
  Sat 2011-02-12 17:17:19 +0100
  * Fix [MySQL Bug #60057](https://bugs.mysql.com/bug.php?id=60057) : sel\_arg\_range\_seq\_next loops in optimized compilation/VS2010
    * When [mariadb 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/changelogs/changelogs-mariadb-53-series) is compiler with VS2010, several tests would enter infinite loop in\
      sel\_arg\_range\_seq\_next(). The reason is compiler backend bug. This bug is not\
      present in either VS2008 or VS2010 SP1 RC.
    * Workaround is to compile this function without most aggresive optimization flag\
      (-Og ) using #pragma optimize ("g", {on|off}) for this version of MSVC compiler.
* [Revision #2904](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2904)\
  Sat 2011-02-12 15:43:24 +0100
  * Fix Aria engine build
    * add forgotten source file
* [Revision #2903](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2903) \[merge]\
  Fri 2011-02-11 13:27:35 +0300
  * Merge: [Bug #716293](https://bugs.launchpad.net/bugs/716293): "Range checked for each record" is not used if condition refers to outside of subquery
  * [Revision #2891.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2891.1.1)\
    Thu 2011-02-10 11:36:43 +0300
    * [Bug #716293](https://bugs.launchpad.net/bugs/716293): "Range checked for each record" is not used if condition refers to outside of subquery
      * Assume that outside subquery references are known when doing "Range-checked-for-each-record" check.
* [Revision #2902](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2902) \[merge]\
  Wed 2011-02-09 11:22:26 -0800
  * Merge
  * [Revision #2899.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2899.1.1)\
    Fri 2011-02-04 19:06:35 -0800
    * Introduced optimizer switch flag 'optimize\_join\_buffer\_size'.
    * When this flag is 'off' the size of the used join buffer\
      is taken directly from the system variable 'join\_buffer\_size'.
    * When this flag is 'on' then the size of the buffer depends\
      on the estimated number of rows in the partial join whose\
      records are to be stored in the buffer.
    * By default this flag is set 'on'.
* [Revision #2901](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2901)\
  Tue 2011-02-08 19:17:12 -0800
  * Backported test case for [Bug #36981](https://bugs.launchpad.net/bugs/36981).
* [Revision #2900](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2900) \[merge]\
  Mon 2011-02-07 15:19:03 -0800
  * Merge
  * [Revision #2897.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2897.1.1)\
    Sat 2011-02-05 20:57:03 -0800
    * Fixed [Bug #702403](https://bugs.launchpad.net/bugs/702403) that caused a crash on the tree for [MWL#128](https://askmonty.org/worklog/?tid=128)\
      with the test case added by this patch.
    * The bug cannot be reproduced with the same test case for the main\
      5.3 tree because the backported fix for [MySQL Bug #59696](https://bugs.mysql.com/bug.php?id=59696) masks the\
      problem that causes the crash in the mentioned test case. It's not\
      clear weather this fix masks this problem in all possible cases.
    * Anyway the patch for [Bug #698882](https://bugs.launchpad.net/bugs/698882) introduced some inconsistent data\
      structures that could contain indirect references to deleted object.
    * It happened when two Item\_equal objects were merged and the Item\_field\
      list of the second object was joined to such list of the first object.
    * This operation required adjustment of the backward pointers in\
      Item fields from the joined list. However the adjustment was missing\
      and this caused crashes in the tree for [MWL#128](https://askmonty.org/worklog/?tid=128).
    * Now the backward pointers are set only when Item\_equal items are\
      completely built and are not changed anymore.
* [Revision #2899](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2899)\
  Tue 2011-02-01 14:19:58 +0100
  * Fix compile errors:
    * declaration in the middle of the block in C file.
    * round() is only available in C99.
* [Revision #2898](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2898)\
  Mon 2011-01-31 19:33:32 -0800
  * Back-ported the patch for [MySQL Bug #59696](https://bugs.mysql.com/bug.php?id=59696) from mysql-5.6 code line.
  * The patch fixed the following optimizer defect: when performing\
    substitution for best equal fields into where conditions to be\
    able to do their evaluations as soon as possible the optimizer\
    skipped conditions over views. That could lead to suboptimal\
    execution of queries that used views.
  * Slightly changed the test case to demonstrate the performance\
    improvements if this fix.
* [Revision #2897](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2897) \[merge]\
  Fri 2011-01-28 18:54:30 -0800
  * Merge
  * [Revision #2893.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2893.1.2)\
    Mon 2011-01-24 14:54:50 -0800
    * Post-second-review fixes for the patch that added the code allowing to use\
      hash join over equi-join conditions without supporting indexes.
  * [Revision #2893.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2893.1.1) \[merge]\
    Sun 2011-01-23 10:39:53 -0800
  * Merge
* [Revision #2896](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2896)\
  Thu 2011-01-27 21:23:02 -0800
  * Fixed [Bug #707827](https://bugs.launchpad.net/bugs/707827).
    * This bug could manifest itself when hash join over a varchar column\
      with NULL values in some rows was used. It happened because the\
      function key\_buf\_cmp erroneously returned FALSE when one of the joined\
      key fields was null while the second was not.
    * Also fixed two other bugs in the functions key\_hashnr and key\_buf\_cmp\
      that could possibly lead to wrong results for some queries that\
      used hash join over several columns with nulls.
    * Also reverted the latest addition of the test case for [MySQL Bug #45092](https://bugs.mysql.com/bug.php?id=45092). It\
      had been already backported earlier.
* [Revision #2895](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2895)\
  Wed 2011-01-26 20:45:23 -0800
  * Fixed [Bug #707848](https://bugs.launchpad.net/bugs/707848).
    * This was another bug in the patch for [Bug #698882](https://bugs.launchpad.net/bugs/698882). The new\
      code from this patch did not ensured that substitutions\
      of fields for best equal fields were performed on all\
      AND-OR levels. As a result substitutions for best fields\
      in some predicates that had been used by the range optimizer\
      were not actually performed while range plans could employ\
      these substitutions. This could lead to inconsistent data\
      structures and ultimately to a crash.
* [Revision #2894](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2894)\
  Wed 2011-01-26 11:30:29 -0800
  * Fixed [Bug #707555](https://bugs.launchpad.net/bugs/707555).
    * The bug was in the code of the patch fixing [Bug #698882](https://bugs.launchpad.net/bugs/698882).
    * With improper casting the method store\_key\_field::change\_source\_field\
      was called for the elements of the array TABLE\_REF::key\_copy that\
      were either of a different type or not allocated at all. This caused\
      crashes in some queries.
* [Revision #2893](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2893)\
  Sat 2011-01-22 23:45:52 -0800
  * Fixed typo that caused printing 'range' instead of 'index\_merge' as the type\
    of sort\_intersect scans.
* [Revision #2892](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2892)\
  Fri 2011-01-21 09:56:55 +0200
  * Fix of reverting changes in depend\_on list.
* [Revision #2891](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2891)\
  Fri 2011-01-14 21:51:55 +0100
  * issue an informative error message for a common Aria problem when opening a table\
    (incorrect block size)
* [Revision #2890](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2890)\
  Fri 2011-01-14 21:02:51 +0100
  * compilation failures caused by adding new row format to Aria
* [Revision #2889](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2889)\
  Fri 2011-01-14 12:05:46 +0100
  * Optimize use of SEARCH\_SAVE\_BUFF in Aria\
    (less not-needed copies of key pages)
* [Revision #2888](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2888)\
  Fri 2011-01-14 12:03:41 +0100
  * use bulk insert and repair by sort for unique keys in\
    Aria and MyISAM in create\_internal\_tmp\_table\_from\_heap()
    * (safe, as duplicates are impossible).
    * This gives a HUGE speed boost!
* [Revision #2887](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2887)\
  Fri 2011-01-14 11:58:45 +0100
  * Added ha\_write\_tmp\_row() for slightly faster write\_row for internal temp tables.
  * This will also enable us in the future to collect statistics for\
    writes to internal tmp tables.
* [Revision #2886](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2886)\
  Fri 2011-01-14 11:54:39 +0100
  * Added support for NO\_RECORD record format (don't store any row data) for Aria.
  * This makes the keys smaller (no row pointer) and gives us proper errors if we\
    use the table wrongly.
* [Revision #2885](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2885)\
  Fri 2011-01-14 11:43:42 +0100
  * use normal unique (HA\_NOSAME) keys for expression cache\
    temptables, not "uniques", that are hash-based keys.
* [Revision #2884](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2884)\
  Fri 2011-01-14 11:37:23 +0100
  * Added to Aria better hash for packed numeric data for unique handling.
  * This was needed as the old code caused us to have LOTS of duplicate\
    hash values when used by optimizer.
* [Revision #2883](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2883)\
  Fri 2011-01-14 11:34:41 +0100
  * compare "Copying to tmp table" proc\_info as a pointer, not as a string
* [Revision #2882](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2882)\
  Fri 2011-01-14 11:31:09 +0100
  * Removed some old comments.
* [Revision #2881](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2881) \[merge]\
  Tue 2011-01-18 00:26:04 +0300
  * Merge 5.3-subquery-bugfixing -> 5.3
  * [Revision #2869.2.13](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.13)\
    Mon 2011-01-17 15:09:30 +0300
    * Enable testcase for [MySQL Bug #49129](https://bugs.mysql.com/bug.php?id=49129)
  * [Revision #2869.2.12](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.12)\
    Sat 2011-01-15 02:07:04 +0300
    * [MySQL Bug #46692](https://bugs.mysql.com/bug.php?id=46692) Crash occurring on queries with nested FROM subqueries using materialization
      * Backport testcases
      * We have a different fix because we've fixed part of the problem as part of fix for [Bug #602574](https://bugs.launchpad.net/bugs/602574).
  * [Revision #2869.2.11](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.11)\
    Fri 2011-01-14 20:40:16 +0300
    * Backport testcase: [MySQL Bug #45863](https://bugs.mysql.com/bug.php?id=45863) "Assertion failed: (fixed == 0), function fix\_fields(), file item.cc, line 4448"\
      (The fix was backported with subquery code backport)
  * [Revision #2869.2.10](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.10)\
    Fri 2011-01-14 17:30:27 +0300
    * Backport of:
      * 3150 Olav Sandstaa 2010-05-07
      * Test cases for the following "ICP for InnoDB" bugs:
      * [MySQL Bug #40992](https://bugs.mysql.com/bug.php?id=40992) InnoDB: Crash when engine\_condition\_pushdown is on
      * [MySQL Bug #35080](https://bugs.mysql.com/bug.php?id=35080) Innodb crash at mem\_block\_get\_len line 72
      * [MySQL Bug #41996](https://bugs.mysql.com/bug.php?id=41996) multi-table delete crashes server (InnoDB table)
      * [MySQL Bug #43448](https://bugs.mysql.com/bug.php?id=43448) Server crashes on multi table delete with Innodb
      * All these bugs are duplicates of either one or both of [MySQL Bug #43360](https://bugs.mysql.com/bug.php?id=43360) or [MySQL Bug #36981](https://bugs.mysql.com/bug.php?id=36981).
      * (backporting of olav@sun.com-20100226091930-qxvakxmcp6463t5w)
  * [Revision #2869.2.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.9)\
    Fri 2011-01-14 16:38:41 +0300
    * Test case backport for: [MySQL Bug #42580](https://bugs.mysql.com/bug.php?id=42580) - Innodb's ORDER BY ..LIMIT returns no rows for null-safe operator <=> NULL
  * [Revision #2869.2.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.8)\
    Fri 2011-01-14 14:13:11 +0300
    * Testcase backport: [MySQL Bug #43249](https://bugs.mysql.com/bug.php?id=43249)
  * [Revision #2869.2.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.7)\
    Fri 2011-01-14 13:51:30 +0300
    * Testcase backport: [MySQL Bug #46548](https://bugs.mysql.com/bug.php?id=46548) IN-subqueries return 0 rows with materialization=on
    * (the bug itself was fixed during the subquery code backport)
  * [Revision #2869.2.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.6)\
    Fri 2011-01-14 12:55:03 +0300
    * Backport of:
      * 3723 oystein.grovlen@sun.com 2009-11-23
      * [MySQL Bug #46548](https://bugs.mysql.com/bug.php?id=46548) (addendum)
      * Remove KEY::extra\_length. It is not in use.

[MariaDB 5.3.0](../../old-releases/5.3/5.3.0.md) Changelog — page:[1](mariadb-530-changelog.md)[2](mariadb-530-changelog-p2.md)[3](mariadb-530-changelog-p3.md) 4 [5](mariadb-530-changelog-p5.md)[6](mariadb-530-changelog-p6.md)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
