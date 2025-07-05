# MariaDB 5.3.0 Changelog p5

[Download](https://downloads.askmonty.org/mariadb/5.3.0) |[Release Notes](../../old-releases/release-notes-mariadb-5-3-series/mariadb-530-release-notes.md) |**Changelog**\
(page:[1](mariadb-530-changelog.md)[2](mariadb-530-changelog-p2.md)[3](mariadb-530-changelog-p3.md)[4](mariadb-530-changelog-p4.md)5[6](mariadb-530-changelog-p6.md)\
) |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 26 July 2011

* [Revision #2880](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2880)\
  Sat 2011-01-15 23:39:51 -0800
  * Corrected test case for [Bug #698882](https://bugs.launchpad.net/bugs/698882) to make it platform independent
* [Revision #2879](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2879) \[merge]\
  Sat 2011-01-15 12:42:32 -0800
  * Merge
  * [Revision #2875.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2875.2.1)\
    Sat 2011-01-15 11:14:36 -0800
    * Fixed [Bug #698882](https://bugs.launchpad.net/bugs/698882).
    * Made sure that the optimal fields are used by TABLE\_REF objects\
      when building index access keys to joined tables.
    * Fixed a bug in the template function that sorts the elements of\
      a list using the bubble sort algorithm. The bug caused poor\
      performance of the function. Also added an optimization that\
      skips comparison with the most heavy elements that has been\
      already properly placed in the list.
    * Made the comparison of the fields belonging to the same Item\_equal\
      more granular: fields belonging to the same table are also ordered\
      according to some rules.
* [Revision #2878](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2878) \[merge]\
  Fri 2011-01-14 23:53:27 -0800
  * Merge
  * [Revision #2875.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2875.1.1)\
    Fri 2011-01-14 22:55:56 -0800
    * Ported the fix for [Bug #702310](https://bugs.launchpad.net/bugs/702310) / [MySQL Bug #59493](https://bugs.mysql.com/bug.php?id=59493).
    * An assertion failure was triggered for a 6-way join query that used two\
      join buffers.
    * The failure happened because every call of JOIN\_CACHE::join\_matching\_records\
      saved and restored status of all tables that were accessed before the table\
      join\_tab. It must do it only for those of them that follow the last table\
      using a join buffer.
* [Revision #2877](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2877) \[merge]\
  Fri 2011-01-14 13:07:50 +0300
  * Merge backported subquery bugfixes/testcases into [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)
  * [Revision #2869.2.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.5)\
    Fri 2011-01-14 00:47:03 +0300
    * Backport testcase for: [MySQL Bug #43360](https://bugs.mysql.com/bug.php?id=43360) - Server crash with a simple multi-table update
  * [Revision #2869.2.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.4)\
    Fri 2011-01-14 00:15:44 +0300
    * Testcase Backport: [MySQL Bug #48093](https://bugs.mysql.com/bug.php?id=48093): 6.0 Server not processing equivalent IN clauses properly
  * [Revision #2869.2.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.3)\
    Thu 2011-01-13 23:47:15 +0300
    * Backport testcase for:
      * mybug #45092: join buffer contains two blob columns one of which is used in the key employed to access the joined table
  * [Revision #2869.2.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.2)\
    Thu 2011-01-13 19:25:31 +0300
    * Backport of (see below) + temporary measures to make SJ-Materialization work with join buffering.\
      \*
      * Date: Mon, 01 Nov 2010 15:15:25 -0000<>
      * 3272 Roy Lyseng 2010-11-01
      * [MySQL Bug #52068](https://bugs.mysql.com/bug.php?id=52068): Optimizer generates invalid semijoin materialization plan
      *
      * When MaterializeScan semijoin strategy was used and there were one\
        or more outer dependent tables before the semijoin tables, the scan\
        over the materialized table was not properly reset for each row of\
        the prefix outer tables.
      *
      * Example: suppose we have a join order:
      *
      * ot1 SJ-Mat-Scan(it2 it3) ot4
      *
      * Notice that this is called a MaterializeScan, even though there is an\
        outer table ahead of the materialized tables. Usually a MaterializeScan\
        has the outer tables after the materialized table, but this is\
        a special (but legal) case with outer dependent tables both before and\
        after the materialized table.
      *
      * For each qualifying row from ot1, a new scan over the materialized\
        table must be set up. The code failed to do that, so all scans after\
        the first one returned zero rows from the materialized table.
  * [Revision #2869.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.2.1)\
    Sat 2010-12-25 16:23:16 +0300[MySQL Bug #46680](https://bugs.mysql.com/bug.php?id=46680): Assertion failed in file item\_subselect.cc, line 305 crashing on HAVING subquery
* Backport the testcase (the fix itself was included with the subquery optimizations backport)
* [Revision #2876](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2876)\
  Wed 2011-01-12 15:00:10 +0300
  * [Bug #665669](https://bugs.launchpad.net/bugs/665669): Result differences on query re-execution
    * Cause: handler::in\_range\_check\_pushed\_down was not reset when a\
      command would call handler->idx\_cond\_push() without later calling\
      handler->index\_end().
    * Fix: reset the variable in handler->reset(), too (like we do with other\
      Index Condition Pushdown members).
* [Revision #2875](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2875)\
  Wed 2011-01-05 15:03:30 -0800
  * Fixed [Bug #697557](https://bugs.launchpad.net/bugs/697557).\
    When stored in a key buffer any varchar field has a length prefix\
    that always takes 2 bytes.
* [Revision #2874](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2874)\
  Wed 2010-12-29 18:14:03 -0800
  * Corrected the test case for [Bug #695304](https://bugs.launchpad.net/bugs/695304)\
    Added a test case for [Bug #695442](https://bugs.launchpad.net/bugs/695442) - a duplicate of [Bug #694092](https://bugs.launchpad.net/bugs/694092)
* [Revision #2873](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2873) \[merge]\
  Wed 2010-12-29 13:45:38 -0800
  * Merge.
  * [Revision #2870.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2870.1.3)\
    Wed 2010-12-29 11:00:22 -0800
    * Fixed [Bug #695304](https://bugs.launchpad.net/bugs/695304)\
      The bug was the result of a bad merge maria-5.2-wl21 -> 5.3.
  * [Revision #2870.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2870.1.2) \[merge]\
    Tue 2010-12-28 12:25:33 -0800
    * Merge
  * [Revision #2870.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2870.1.1) \[merge]\
    Mon 2010-12-27 14:22:05 -0800
    * Merge
* [Revision #2872](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2872)\
  Sun 2010-12-26 16:31:03 -0800
  * Fixed [Bug #694443](https://bugs.launchpad.net/bugs/694443)\
    One of the hash functions employed by the BNLH join algorithm\
    calculates the value of hash index for key value utilizing\
    every byte of the key buffer. To make this calculation valid\
    one has to ensure that for any key value unused bytes of the\
    buffer are filled with a certain filler. We choose 0 as\
    a filler for these bytes.
  * Added an optional boolean parameter with\_zerofill to the function\
    key\_copy. If the value of the parameter is TRUE all unused bytes\
    of the key buffer is filled with 0.
* [Revision #2871](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2871) \[merge]\
  Sat 2010-12-25 18:54:14 -0800
  * Merge
  * [Revision #2869.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869.1.1)\
    Fri 2010-12-24 14:36:35 -0800
    * Fixed [Bug #694092](https://bugs.launchpad.net/bugs/694092)
    * In some cases the function make\_cond\_for\_index() was mistaken\
      when detecting index only pushdown conditions for a table:\
      a pushdown condition that was not index only could be marked\
      as such.
    * It happened because the procedure erroneously used the markers\
      for index only conditions that remained from the calls of\
      this function that extracted the index conditions for other\
      tables.
    * Fixed by erasing index only markers as soon as they are need\
      anymore.
* [Revision #2870](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2870) \[merge]\
  Fri 2010-12-24 16:24:20 -0800
  * Merge
  * [Revision #2867.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2867.1.1)\
    Wed 2010-12-22 00:37:35 -0800
    * Fixed [Bug #670380](https://bugs.launchpad.net/bugs/670380)\
      Lifted the limitation that hash join could not be used over\
      varchar fields with non-binary collation.
* [Revision #2869](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2869)\
  Wed 2010-12-22 02:26:35 +0300
  * Fix compile error on Windows: instead of round(X) use floor(X+0.5)
* [Revision #2868](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2868) \[merge]\
  Tue 2010-12-21 14:40:23 +0300
  * [MWL#121](https://askmonty.org/worklog/?tid=121)-125 DS-MRR improvements
    * Merge with 5.3-main
  * [Revision #2866.1.10](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2866.1.10)\
    Mon 2010-12-20 14:40:12 +0300
    * [Bug #670417](https://bugs.launchpad.net/bugs/670417): Diverging results in maria-5.3-mwl128-dsmrr-cpk with join buffer
      * Fixes for the second fix: take into account case where we don't need to save/restore the scan.
  * [Revision #2866.1.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2866.1.9)\
    Sun 2010-12-19 13:56:12 +0300
    * [Bug #670417](https://bugs.launchpad.net/bugs/670417): Diverging results in maria-5.3-mwl128-dsmrr-cpk with join buffer
      * Switch from "Disable identical key handling optimization when
      * IndexConditionPushdown is used" approach
      * To
      * an approach where we save/restore index tuple and so can use index condition pushdown.
  * [Revision #2866.1.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2866.1.8)\
    Fri 2010-12-17 14:58:08 +0300
    * Fix a compiler warning on sparc32
  * [Revision #2866.1.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2866.1.7)\
    Fri 2010-12-17 13:06:21 +0300
    * Small code cleanups
  * [Revision #2866.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2866.1.6)\
    Thu 2010-12-16 23:43:52 +0300
    * Better comments
  * [Revision #2866.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2866.1.5)\
    Thu 2010-12-16 23:37:26 +0300
    * [MWL#121](https://askmonty.org/worklog/?tid=121)-125 DS-MRR improvements
      * Address Monty's review feedback, portion 3
  * [Revision #2866.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2866.1.4)\
    Thu 2010-12-16 21:18:35 +0300
    * [MWL#121](https://askmonty.org/worklog/?tid=121)-125 DS-MRR improvements
      * Address Monty's review feedback, portion 2
  * [Revision #2866.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2866.1.3)\
    Wed 2010-12-15 10:45:08 +0300
    * Fix compiler warning
    * Better warnings
  * [Revision #2866.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2866.1.2)\
    Mon 2010-12-13 20:01:32 +0300
    * [MWL#121](https://askmonty.org/worklog/?tid=121)-125 DS-MRR improvements
      * Address review feedback: change return type of RANGE\_SEQ\_IF::next()
  * [Revision #2866.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2866.1.1) \[merge]\
    Mon 2010-12-13 13:42:40 +0300
    * Merge DS-MRR/CPK improvements into 5.3-main
* [Revision #2867](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2867)\
  Tue 2010-12-14 14:08:05 +0200
  * Fix [Bug #685411](https://bugs.launchpad.net/bugs/685411)
    * Analysis:
      * The assert failed because st\_select\_lex::print() was called for subqueries\
        as follows:
      * Item\_subselect::print() ->\
        subselect\_single\_select\_engine::print() -> st\_select\_lex::print()
      * It was Item\_subselect::fix\_fields() that set the thd by calling set\_thd(),\
        so when this print() was called before fix\_fields(), subselect\_engine::thd\
        was NULL.
    * Solution:
      * The patch makes all constructors of all subselect\_engine classes to take\
        a THD parameter. The default subselect\_single\_select\_engine engine is created\
        early during parse time, in the Item\_subselect::init call, so we pass the\
        correct THD object already at this point.
* [Revision #2866](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2866)\
  Sat 2010-12-11 12:50:39 -0800
  * Fixed compiler warnings.
* [Revision #2865](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2865) \[merge]\
  Fri 2010-12-10 23:23:34 -0800
  * Merge.
  * [Revision #2850.1.11](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2850.1.11)\
    Fri 2010-11-19 11:03:03 -0800
    * Got the declarations related to the class JOIN\_CACHE, its derivatives and\
      companions out of sql\_select.h into a separate file sql\_join\_cache.h.
  * [Revision #2850.1.10](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2850.1.10)\
    Fri 2010-11-19 07:38:02 -0800
    * Fixed [Bug #675922](https://bugs.launchpad.net/bugs/675922).
    * The bug happened when BKA join algorithm used an incremental buffer\
      and some of the fields over which access keys were constructed
      * were allocated in the previous join buffers
      * were non-nullable
      * belonged to inner tables of outer joins.
    * For such fields an offset to the field value in the record is saved\
      in the postfix of the record, and a zero offset indicates that the value\
      is null. Before the key using the field value is constructed the\
      value is read into the corresponding field of the record buffer and\
      the null bit is set for the field if the offset is 0. However if\
      the field is non-nullable the table->null\_row must be set to 1\
      for null values and to 0 for non-null values to ensure proper reading\
      of the value from the record buffer.
  * [Revision #2850.1.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2850.1.9)\
    Fri 2010-11-19 06:20:28 -0800
    * Fixed [Bug #660963](https://bugs.launchpad.net/bugs/660963).
    * The condition that was supposed to check whether a join table\
      is an inner table of a nested outer join or semi-join was not\
      quite correct in the code of the function check\_join\_cache\_usage.
    * That's why some queries with nested outer joins triggered\
      an assertion failure.
    * Encapsulated this condition in the new method called\
      JOIN\_TAB::is\_nested\_inner and provided a proper code for it.
    * Also corrected a bug in the code of check\_join\_cache\_usage()\
      that caused a downgrade of not first join buffers of the\
      level 5 and 7 to level 4 and 6 correspondingly.
  * [Revision #2850.1.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2850.1.8)\
    Mon 2010-11-15 21:07:32 -0800
    * Fixed [Bug #675516](https://bugs.launchpad.net/bugs/675516).
    * When pushing the condition for a table in the function\
      JOIN\_TAB::make\_scan\_filter the optimizer must not push\
      conditions from WHERE if the table is some inner table\
      of an outer join..
  * [Revision #2850.1.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2850.1.7)\
    Sun 2010-11-14 23:38:25 -0800
    * Fixed [Bug #675095](https://bugs.launchpad.net/bugs/675095).
    * The condition over outer tables extracted from the on expression\
      for a outer join must be ANDed to the condition pushed to the\
      first inner table of this outer join only.
    * Nested outer joins cannot use flat join buffers. So if join\_cache\_level\
      is set to 1 then any join algorithm employing join buffers cannot be used\
      for nested outer joins.
  * [Revision #2850.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2850.1.6)\
    Sat 2010-11-13 07:47:43 -0800
    * Fixed [Bug #674423](https://bugs.launchpad.net/bugs/674423).
    * The patch that introduced the new enumeration type Match\_flag\
      for the values of match flags in the records put into join buffers\
      missed the necessary modifications in JOIN\_CACHE::set\_match\_flag\_if\_none.
    * This could cause wrong results for outer joins with on expressions\
      only over outer tables.
  * [Revision #2850.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2850.1.5) \[merge]\
    Sat 2010-11-13 06:35:54 -0800
    * Merge
  * [Revision #2850.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2850.1.4)\
    Fri 2010-11-12 16:53:20 -0800
    * Corrected the fix for [Bug #672551](https://bugs.launchpad.net/bugs/672551).
  * [Revision #2850.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2850.1.3) \[merge]\
    Thu 2010-11-11 16:59:08 -0800
    * Merge
  * [Revision #2850.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2850.1.2) \[merge]\
    Thu 2010-11-11 16:38:55 -0800
    * Merge
  * [Revision #2850.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2850.1.1) \[merge]\
    Wed 2010-11-10 14:34:37 -0800
    * Merge
* [Revision #2864](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2864)\
  Wed 2010-12-08 16:16:32 +0200
  * Fixed test results for windows builds
  * Fixed compiler warning
* [Revision #2863](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2863) \[merge]\
  Tue 2010-12-07 00:15:27 +0100
  * merge [Bug #686184](https://bugs.launchpad.net/bugs/686184)
* [Revision #2862](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2862)\
  Mon 2010-12-06 20:44:17 +0300
  * Post-merge fixes: fix compile failure in buildbot
* [Revision #2861](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2861) \[
  * merge]\
    Mon 2010-12-06 13:40:52 +0100
  * merge
* [Revision #2860](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2860) \[merge]\
  Mon 2010-12-06 10:25:44 +0200
  * Merge with 5.1-release.
    * Fixed problem with oqgraph and 'make dist'
    * Note that after this merge we have a problem show in join\_outer where we examine too many rows in one specific case (related to [MySQL Bug #57024](https://bugs.mysql.com/bug.php?id=57024)).
    * This will be fixed when [MWL#128](https://askmonty.org/worklog/?tid=128) is merged into 5.3.
* [Revision #2859](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2859)\
  Tue 2010-11-30 01:27:14 +0200
  * Fixed some compiler warnings found when compiling for windows.
  * Changed rows\_read and rows\_sent status variables to be longlong (to avoid compiler warnings)
* [Revision #2858](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2858)\
  Mon 2010-11-29 23:58:18 +0100
  * Use three digits after the decimal point for better resolution and comparability of results.
* [Revision #2857](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2857)\
  Mon 2010-11-29 22:02:33 +0200
  * Fix logical expression according to operation priority (also MS visual studio compiler warnings).
* [Revision #2856](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2856) \[merge]\
  Mon 2010-11-29 13:50:56 +0200
  * Auto-merge fix for [Bug #611622](https://bugs.launchpad.net/bugs/611622)
  * [Revision #2853.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2853.1.1)\
    Thu 2010-11-25 11:43:23 +0200
    * Fix [Bug #611622](https://bugs.launchpad.net/bugs/611622)
    * Fix [MySQL Bug #52344](https://bugs.mysql.com/bug.php?id=52344) - Subquery materialization: Assertion if subquery in on-clause of outer join
    * Original fix and comments from Oysten, adjusted for the different\
      subquery optimization in MariaDB.
    * Problem: If tables of an outer join are constant tables,\
      the associated on-clause will be evaluated in the optimization\
      phase. If the on-clause contains a query that is to be\
      executed with subquery materialization, this will not work\
      since the infrastructure for such execution is not yet set up.
    * Solution: Do not evaluate on-clause in optimization phase if\
      is\_expensive() returns true for this clause. This is how the\
      problem is currently avoided for where-clauses. This works\
      because, Item\_in\_subselect::is\_expensive\_processor returns true\
      if query is to be executed with subquery materialization.
    * In addition, after [MWL#89](https://askmonty.org/worklog/?tid=89), in MariaDB if the IN-EXISTS strategy\
      is chosen, the in-to-exists predicates are insterted after\
      join\_read\_const\_table() is called, resulting in evaluation of\
      the subquery without the in-to-exists predicates.
* [Revision #2855](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2855)\
  Sun 2010-11-28 15:02:12 +0200
  * Disable warning that comes 'occasionable' depending on if HAVING is executed or not.
* [Revision #2854](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2854) \[merge]\
  Sun 2010-11-28 14:38:59 +0200
  * Automatic merge
  * [Revision #2851.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2851.1.4)\
    Sat 2010-11-27 17:29:52 +0200
    * Added TRASH() to table->record\[0] to find out if we access not initialzed data.
      * Changed Cached\_item\_field not copy data for fields with NULL value
      * In key\_copy() and key\_restore() don't copy data for fields with NULL value
    * Fixed code to avoid valgrind warnings
      * Use c\_ptr\_safe instead of c\_ptr()
    * Removed "QQ" from comments (QQ was ment to be used for internal comments that should be removed before pushing)\
      Fixed wrong alias used (from previous patch)
  * [Revision #2851.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2851.1.3) \[merge]\
    Sat 2010-11-27 17:23:48 +0200
    * Automatic merge with 5.3 (support of BIT keys in heap)
  * [Revision #2851.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2851.1.2)\
    Wed 2010-11-24 00:08:48 +0200
    * Code cleanup to get fewer reallocs() during execution.
      * Changed TABLE->alias to String to get fewer reallocs when alias are used.
      * Preallocate some buffers
      * Changed some String->c\_ptr() -> String->ptr() when \0 is not needed.
      * Fixed wrong usage of String->ptr() when we need a \0 terminated string.
      * Use my\_strtod() instead of my\_atof() to avoid having to add \0 to string.
      * c\_ptr() -> c\_ptr\_safe() to avoid warnings from valgrind.
      * zr
  * [Revision #2851.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2851.1.1) \[merge]\
    Tue 2010-11-16 19:52:44 +0200
    * Merge to get make String reallocation faster
* [Revision #2853](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2853)\
  Thu 2010-11-25 00:34:50 +0200
  * Fix [Bug #680058](https://bugs.launchpad.net/bugs/680058)
  * Analysis:
    * The send\_data method of the result sink class used to collect\
      data statistics about materialized subqueries incorrectly assumed\
      that duplicate rows are removed prior to calling send\_data. As\
      a result the collected statistics was wrong, which resulted in\
      an incorrect maximal number of keys in the Ordered\_key buffer.
  * Solution:
    * Try to insert each row into the materialized temp table before\
      collecting statistics, and if the insertion results in a duplicate\
      row, do not count the current row.
* [Revision #2852](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2852)\
  Tue 2010-11-23 12:35:37 +0200
  * Fix for [Bug #606013](https://bugs.launchpad.net/bugs/606013): Adding bit field support for heap tables.
* [Revision #2851](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2851) \[merge]\
  Thu 2010-11-11 14:35:26 +0200
  * Merge in [Bug #602574](https://bugs.launchpad.net/bugs/602574)
  * [Revision #2831.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2831.1.1)\
    Tue 2010-11-02 21:13:53 +0300
    * [Bug #602574](https://bugs.launchpad.net/bugs/602574): RQG: sql\_select.cc:5385: bool greedy\_search... : Assertion \`join->best\_read
    * Make optimize\_wo\_join\_buffering() handle cases where position->records\_read=0 (this\
      happens for outer joins that have constant tables inside them). The number of\
      0 is not correct (should be 1 because outer join will produce at least a NULL-complemented\
      record) but for now we just make it work with incorrect number.
* [Revision #2850](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2850) \[merge]\
  Tue 2010-11-09 19:40:02 -0800
  * Merge
  * [Revision #2844.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2844.1.1)\
    Mon 2010-11-08 20:36:32 -0800
    * Fixed [Bug #668644](https://bugs.launchpad.net/bugs/668644).
    * The pushdown condition for the sorted table in a query can be complemented\
      by the conditions from HAVING. This transformation is done in JOIN::exec\
      pretty late after the original pushdown condition have been saved in the\
      field pre\_idx\_push\_select\_cond for the sorted table. So this field must\
      be updated after the inclusion of the condition from HAVING.
* [Revision #2849](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2849)\
  Tue 2010-11-09 13:13:56 +0200
  * Fixed [Bug #615378](https://bugs.launchpad.net/bugs/615378) Incorrect processing of NULL result in Item\_cache fixed.
* [Revision #2848](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2848)\
  Tue 2010-11-09 09:52:22 +0200
  * Fix buildbot failure introduced by the previous push
* [Revision #2847](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2847)\
  Mon 2010-11-08 23:25:12 +0200
  * Fix buildbot failures caused by two previous pushes.
* [Revision #2846](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2846)\
  Mon 2010-11-08 20:51:31 +0300
  * Fix buildbot errors: rec\_per\_key\_part can be 0 if re-opening
* [Revision #2845](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2845)\
  Mon 2010-11-08 19:06:26 +0300
  * \[Patch from Monty] Fix stack-overrun crash in subselect\_notembedded.test
    * Make mi\_open() use less stack space
* [Revision #2844](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2844) \[merge]\
  Fri 2010-11-05 12:37:51 +0200
  * Automerge with 5.2
* [Revision #2843](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2843)\
  Fri 2010-11-05 11:54:42 +0200
  * Fixed usage of wrong variable in case of errors
* [Revision #2842](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2842) \[merge]\
  Tue 2010-11-02 16:08:02 -0700
  * Merge
  * [Revision #2838.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2838.1.2) \[merge]\
    Tue 2010-11-02 10:12:21 -0700
    * Merge
  * [Revision #2838.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2838.1.1)\
    Tue 2010-11-02 10:07:46 -0700
    * Fixed [Bug #669420](https://bugs.launchpad.net/bugs/669420).
    * This bug in the MRR code for Maria engine caused wrong results when\
      MRR was used to scan ranges for each record.
    * Added test cases for [Bug #669420](https://bugs.launchpad.net/bugs/669420) and [Bug #669423](https://bugs.launchpad.net/bugs/669423) (as a duplicate of [Bug #669420](https://bugs.launchpad.net/bugs/669420)).
* [Revision #2841](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2841)\
  Tue 2010-11-02 16:04:39 -0700
  * Removed empty lines.
* [Revision #2840](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2840) \[merge]\
  Tue 2010-11-02 10:48:55 +0100
  * merge
  * [Revision #2837.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2837.1.2)\
    Tue 2010-11-02 10:47:36 +0100
    * fix windows embedded
  * [Revision #2837.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2837.1.1) \[merge]\
    Tue 2010-11-02 10:12:29 +0100
    * merge w/ 5.2
* [Revision #2839](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2839)\
  Tue 2010-11-02 11:03:33 +0200
  * Fixed wrong queue\_replace(), which caused timeout failure in pbxt.flush\_read\_lock\_kill
  * Fixed compiler warnings.
* [Revision #2838](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2838)\
  Fri 2010-10-29 18:59:39 -0700
  * Fixed [Bug #665049](https://bugs.launchpad.net/bugs/665049).
  * The bug could cause wrong results for queries over Maria tables when\
    index condition pushdown was used.
* [Revision #2837](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2837) \[merge]\
  Thu 2010-10-28 19:04:23 +0200
  * 5.2 merge
* [Revision #2836](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2836)\
  Wed 2010-10-27 16:28:19 +0300
  * Fixed [Bug #613009](https://bugs.launchpad.net/bugs/613009)
  * The set of Ordered keys of a rowid merge engine is dense. Thus when\
    we decide not to create a key for a column that has only NULLs, this\
    column shouldn't be counted.
  * Notice that the caller has already precomputed the correct total\
    number of keys that should be created.
* [Revision #2835](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2835)\
  Wed 2010-10-27 12:35:15 +0300
  * Fixed [Bug #609121](https://bugs.launchpad.net/bugs/609121)
  * Post-review fix - avoid re-evaluation of the having clause\
    when it evaluates to true.
* [Revision #2834](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2834)\
  Wed 2010-10-27 06:03:59 +0300
  * Type of the variables fixed.
* [Revision #2833](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2833)\
  Tue 2010-10-26 14:55:42 +0300
  * Fixed [Bug #601156](https://bugs.launchpad.net/bugs/601156)
  * The cause for this bug is that [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) still processes derived tables\
    (subqueries in the FROM clause) by fully executing them during the parse\
    phase. This will be remedied by [MWL#106](https://askmonty.org/worklog/?tid=106) once merged into the main 5.3.
  * The assert statement is triggered when MATERIALIZATION is ON for EXPLAIN\
    EXTENDED for derived tables with an IN subquery as follows:
    * mysql\_parse calls JOIN::exec for the derived table as if it is regular\
      execution (not explain).
    * When materialization is ON, this call goes all the way to\
      subselect\_hash\_sj\_engine::exec, which creates a partial match engine\
      because of NULL presence.
    * In order to proceed with normal execution, the hash\_sj engine substitutes\
      itself with the created partial match engine.
    * After the parse phase it turns out that this execution was part of\
      EXPLAIN EXTENDED, which in turn calls\
      Item\_cond::print -> ... -> Item\_subselect::print,\
      which calls engine->print().\
      Since subselect\_hash\_sj\_engine::exec substituted the current\
      Item\_subselect engine with a partial match engine, eventually we call\
      its ::print() method. However the partial match engines are designed only\
      for execution, hence there is no implementation of this print() method.
  * The fix temporarily removes the assert, until this code is merged with[MWL#106](https://askmonty.org/worklog/?tid=106).

[MariaDB 5.3.0](../../old-releases/release-notes-mariadb-5-3-series/mariadb-530-release-notes.md) Changelog — page:[1](mariadb-530-changelog.md)[2](mariadb-530-changelog-p2.md)[3](mariadb-530-changelog-p3.md)[4](mariadb-530-changelog-p4.md)5[6](mariadb-530-changelog-p6.md)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
