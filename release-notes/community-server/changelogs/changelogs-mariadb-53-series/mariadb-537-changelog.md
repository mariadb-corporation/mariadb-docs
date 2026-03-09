# MariaDB 5.3.7 Changelog

[Download](https://downloads.mariadb.org/mariadb/5.3.7) |[Release Notes](../../old-releases/5.3/5.3.7.md) |**Changelog** |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 4 May 2012

For the highlights of this release, see the [release notes](../../old-releases/5.3/5.3.7.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3516](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3516)\
  Wed 2012-05-02 22:02:17 +0200
  * update the version number
* [Revision #3515](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3515)\
  Thu 2012-05-03 13:14:40 +0500
  * Fix for failing gis-precise on Windows.
* [Revision #3514](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3514) \[merge]\
  Wed 2012-05-02 22:02:06 +0200
  * 5.2 merge
  * [Revision #2732.53.37](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.37)\
    Wed 2012-05-02 22:00:31 +0200
    * update the result file
  * [Revision #2732.53.36](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.36)\
    Wed 2012-05-02 18:11:02 +0200
    * [MDEV-214](https://jira.mariadb.org/browse/MDEV-214) [Bug #967242](https://bugs.launchpad.net/bugs/967242) Wrong result with JOIN, AND in ON condition, multi-part key, GROUP BY, subquery and OR in WHERE
    * The problem was in the code (update\_const\_equal\_items()) which marked\
      index parts constant independently of the place where the equality was used.\
      In the test suite it marked t2\_1.c part constant despite the fact that\
      it connected by OR with other expression.
    * Solution is to mark constant only top equalities connected with AND.
  * [Revision #2732.53.35](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.35) \[merge]\
    Wed 2012-05-02 17:06:30 +0200
    * 5.1 merge
    * [Revision #2643.153.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.5)\
      Tue 2012-04-24 17:29:03 +0200
      * [Bug #986120](https://bugs.launchpad.net/bugs/986120) Problem installing mariadb 5 on solaris 10
      * remove a redundant line in Makefile.am
* [Revision #3513](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3513)\
  Wed 2012-05-02 15:23:49 +0200
  * implement Item\_singlerow\_subselect::get\_date() to avoid\
    unnecessary date->string->date conversion
* [Revision #3512](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3512)\
  Wed 2012-05-02 15:22:47 +0200
  * [MDEV-241](https://jira.mariadb.org/browse/MDEV-241) [Bug #992722](https://bugs.launchpad.net/bugs/992722) - Server crashes in get\_datetime\_value
  * Create an Item\_cache based on item's cmp\_type, not result\_type in\
    subselect\_engine.
  * Use result\_field in Item\_cache\_temporal::cache\_value(),\
    just like all other Item\_cache\*::cache\_value() do.
* [Revision #3511](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3511) \[merge]\
  Wed 2012-05-02 17:04:28 +0200
  * merge
  * [Revision #2732.53.34](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.34)\
    Wed 2012-05-02 16:53:02 +0200
    * [Bug #993103](https://bugs.launchpad.net/bugs/993103): Wrong result with LAST\_DAY('0000-00-00 00:00:00') IS NULL in WHERE condition
    * Fix is to set maybe\_null flag for Item\_func\_last\_day.
  * [Revision #2732.53.33](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.33)\
    Wed 2012-04-25 15:30:19 +0200
    * MDEV233 - Support Wix3.6 for MSI
  * [Revision #2732.53.32](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.32)\
    Wed 2012-04-18 20:04:50 +0200
    * [Bug #982664](https://bugs.launchpad.net/bugs/982664) there are few broken clients that lie about their capabilities\
      (for example, one of them sets client capabilities by copying server capabilities)
    * We cannot fix them - let's tolerate them
* [Revision #3510](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3510)\
  Sun 2012-04-29 18:08:11 +0500
  * [Bug #977021](https://bugs.launchpad.net/bugs/977021) ST\_BUFFER fails with the negative D.
    * Points and lines should disappear if we got negative D.
    * To make it work properly inside the GEOMETRYCOLLECTION,\
      we add the empty operation there.
  * [Bug #986977](https://bugs.launchpad.net/bugs/986977) Assertion \`!cur\_p->event' failed in Gcalc\_scan\_iterator::arrange\_event(int, int).
    * The double->inernal coord conversion produced -0 (minus zero) on some data.
    * That minus-zero produces invalid comparison results when compared agains plus-zero.
    * So we fixed the gcalc\_set\_double() to avoid it.
  * per-file comments:
    * mysql-test/r/gis-precise.result
      * result updated.
    * mysql-test/t/gis-precise.test
      * tests for [Bug #977021](https://bugs.launchpad.net/bugs/977021) and [Bug #986977](https://bugs.launchpad.net/bugs/986977) added.
    * sql/gcalc\_slicescan.cc
      * [Bug #986977](https://bugs.launchpad.net/bugs/986977). The gcalc\_set\_double fixed to not produce minus-zero.
    * sql/item\_geofunc.cc
      * [Bug #977021](https://bugs.launchpad.net/bugs/977021). Add the NOOP for the disappearing features.
* [Revision #3509](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3509)\
  Thu 2012-04-26 19:21:37 +0200
  * [MDEV-216](https://jira.mariadb.org/browse/MDEV-216) [Bug #976104](https://bugs.launchpad.net/bugs/976104) - Assertion \`0' failed in my\_message\_sql on UPDATE IGNORE, or unknown error on release build
  * Don't send\_error at the end of mysql\_multi\_update() if select failed.
  * The error, if there was any, was already sent by mysql\_select
* [Revision #3508](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3508)\
  Fri 2012-04-27 12:59:17 +0300
  * Fix [Bug #985667](https://bugs.launchpad.net/bugs/985667), [MDEV-229](https://jira.mariadb.org/browse/MDEV-229)
  * Analysis:
    * The reason for the wrong result is the interaction between constant\
      optimization (in this case 1-row table) and subquery optimization.
      * First the outer query is optimized, and 'make\_join\_statistics' finds that\
        table t2 has one row, reads that row, and marks the whole table as constant.\
        This also means that all fields of t2 are constant.
      * Next, we optimize the subquery in the end of the outer 'make\_join\_statistics'.\
        The field 'f2' is considered constant, with value '3'. The subquery predicate\
        is rewritten as the constant TRUE.
      * The outer query execution detects early that the whole query result is empty\
        and calls 'return\_zero\_rows'. Since the query is with implicit grouping, we\
        have to produce one row with special values for the aggregates (depending on\
        each aggregate function), and NULL values for all non-aggregate fields. This\
        function calls 'no\_rows\_in\_result' to set each aggregate function to the\
        default value when it aggregates over an empty result, and then calls\
        'send\_data', which in turn evaluates each Item in the SELECT list.
      * When evaluation reaches the subquery predicate, it executes the subquery\
        with field 'f2' having a constant value '3', and the subquery produces the\
        incorrect result '7'.
  * Solution:
    * Implement Item::no\_rows\_in\_result for all subquery predicates. In order to\
      make this work, it is also needed to make all val\_\* methods of all subquery\
      predicates respect the Item\_subselect::forced\_const flag. Otherwise subqueries\
      are executed anyways, and override the default value set by no\_rows\_in\_result\
      with whatever result is produced from the subquery evaluation.
* [Revision #3507](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3507) \[merge]\
  Mon 2012-04-23 20:37:44 +0200
  * merge
  * [Revision #3505.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3505.1.1)\
    Fri 2012-04-20 21:09:16 +0200
    * [Bug #983285](https://bugs.launchpad.net/bugs/983285) - incompatibility in frm in case of VIEWs with non-default ALGORITHM option.
    * As part of derived tables redesign, values for VIEW\_ALGORITHM\_MERGE and VIEW\_ALGORITHM\_TMPTABLE have changed from (former values 1 rsp 2 , new values 5 rsp 9).
    * This lead to the problem that views, created with version 5.2 or earlier would not work in all situations (e.g "SHOW CREATE VIEW"), or with mysqldump.
    * The fix is to restore backward compatibility for the from file, and convert algorithm={1,2} in the frm to {5,9} when reading .frm from disk, and store backward compatible values when writing from to disk.
    * Also allow processing correct processing for "invalid" .frms created with [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md)/5.5 GA releases (where algorithm stored in memory matched the one stored in frm).
* [Revision #3506](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3506)\
  Mon 2012-04-23 09:45:27 +0200
  * [MDEV-207](https://jira.mariadb.org/browse/MDEV-207) Install headers required to build external storage plugins
  * install all private headers in mysql/private/
* [Revision #3505](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3505)\
  Thu 2012-04-19 09:16:30 +0300
  * [Bug #978847](https://bugs.launchpad.net/bugs/978847) fixed.
  * Fixed incorrect type casting which made all fields (except very first) changes to materialized table incorrect.
  * Saved list of view/derived table used items after expanding '\*'.
* [Revision #3504](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3504)\
  Thu 2012-04-19 05:37:16 +0400
  * [Bug #978479](https://bugs.launchpad.net/bugs/978479): Wrong result (extra rows) with derived\_with\_keys+loosescan+semijoin=ON, materialization=OFF
  * Part#2: Don't try to construct a LooseScan access on indexes that do not guarantee\
    index-ordered reads.
* [Revision #3503](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3503)\
  Thu 2012-04-19 04:50:32 +0400
  * BUG#978479: Wrong result (extra rows) with derived\_with\_keys+loosescan+semijoin=ON, materialization=OFF
  * Part#1: make EXPLAIN's plan match the one by actual execution:
  * Item\_subselect::used\_tables() should return the same value irrespectively\
    of whether we're running an EXPLAIN or a SELECT.
* [Revision #3502](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3502) \[merge]\
  Mon 2012-04-16 23:35:38 +0200
  * merge
  * [Revision #2732.53.31](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.31) \[merge]\
    Mon 2012-04-16 23:32:50 +0200
    * merge
    * [Revision #2732.56.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.56.3)\
      Mon 2012-04-16 23:31:33 +0200
      * fix compiler warnings
    * [Revision #2732.56.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.56.2)\
      Mon 2012-04-16 23:31:02 +0200
      * backport a change from 5.5 to remove thread sleeps from Innodb assertions on Windows.
      * This can result in bad deadlocks (e.g loader lock), seen in latest crash reports.
* [Revision #3501](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3501) \[merge]\
  Mon 2012-04-16 17:41:43 +0200
  * merge
  * [Revision #2732.53.30](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.53.30) \[merge]\
    Mon 2012-04-16 15:38:53 +0200
    * merge
    * [Revision #2732.56.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.56.1)\
      Mon 2012-04-16 15:28:33 +0200
      * fixes [Bug #983047](https://bugs.launchpad.net/bugs/983047)
      * [MDEV-221](https://jira.mariadb.org/browse/MDEV-221) - Properly escape command line when starting mysql\_install\_db\
        since password characters can contain quotes or spaces.
      * The proper quoting method for command line arguments used here was extracted from [everyone-quotes-arguments-the-wrong-way.aspx](https://blogs.msdn.com/b/twistylittlepassagesallalike/archive/2011/04/23/everyone-quotes-arguments-the-wrong-way.aspx)
      * Additionally, mysql\_install\_db.exe now passes root password to "`mysqld.exe --bootstrap`"
      * in hexadecimal form, to handle potential special chars inside password string literal.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
