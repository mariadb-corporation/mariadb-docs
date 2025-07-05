# MariaDB 5.3.4 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.3.4) |[Release Notes](../../old-releases/release-notes-mariadb-5-3-series/mariadb-534-release-notes.md) |**Changelog** |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 15 Feb 2012

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-5-3-series/mariadb-534-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3421](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3421)\
  Tue 2012-02-14 16:52:56 +0200
  * Fix for [Bug #910123](https://bugs.launchpad.net/bugs/910123) [MariaDB 5.3.3](../../old-releases/release-notes-mariadb-5-3-series/mariadb-533-release-notes.md) causes 1093 error on Drupal
  * Problem was that now we can merge derived table (subquery in the FROM clause).
  * Fix: in case of detected conflict and presence of derived table "over" the table which cased the conflict - try materialization strategy.
* [Revision #3420](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3420)\
  Tue 2012-02-14 16:04:06 +0400
  * [MDEV-59](https://jira.mariadb.org/browse/MDEV-59) Review and push crashsafe GIS keys.
  * tests for RTree keys recovery.
* [Revision #3419](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3419) \[merge]\
  Tue 2012-02-14 14:13:10 +0400
  * Merge fix for [Bug #928048](https://bugs.launchpad.net/bugs/928048)
  * [Revision #3411.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3411.2.1)\
    Tue 2012-02-14 13:58:57 +0400
    * [Bug #928048](https://bugs.launchpad.net/bugs/928048): Query containing IN subquery with OR in the where clause returns a wrong result
    * Make equality propagation work correctly when done inside the OR branches
* [Revision #3418](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3418)\
  Mon 2012-02-13 23:46:57 -0800
  * Fixed [Bug #925985](https://bugs.launchpad.net/bugs/925985).
  * If the flag 'optimize\_join\_buffer\_size' is set to 'off' and the value\
    of the system variable 'join\_buffer\_size' is greater than the value of\
    the system variable 'join\_buffer\_space\_limit' than no join cache can\
    be employed to join tables of the executed query.
  * A bug in the function JOIN\_CACHE::alloc\_buffer allowed to use join\
    buffer even in this case while another bug in the function\
    revise\_cache\_usage could cause a crash of the server in this case if the\
    chosen execution plan for the query contained outer join or semi-join\
    operation.
* [Revision #3417](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3417)\
  Mon 2012-02-13 17:14:10 +0100
  * When we fail during slave thread initialisation, keep mi->run\_lock\
    locked until we have finished clean up.
  * Previously, the code released the lock without marking that the thread\
    was running. This allowed a new slave thread to start while the old one\
    was still in the middle of cleaning up, causing assertions and probably\
    general mayhem.
* [Revision #3416](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3416) \[merge]\
  Sun 2012-02-12 23:03:36 +0100
  * merge
  * [Revision #2732.46.71](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.71)\
    Sun 2012-02-12 23:02:56 +0100
    * Use newly released HeidiSQL 7.0 in the MSI installer
    * [Revision #2732.46.70](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.70) \[
      * merge]\
        Sat 2012-02-11 15:05:07 +0100
      * merge
* [Revision #3415](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3415) \[merge]\
  Sat 2012-02-11 15:00:15 +0100
  * merge
  * [Revision #2732.52.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.52.1) \[merge]\
    Sat 2012-02-11 14:57:44 +0100
    * Fix for [MDEV-140](https://jira.mariadb.org/browse/MDEV-140), [Bug #930145](https://bugs.launchpad.net/bugs/930145) - broken SSL connectivity for some connectors
    * [Revision #2643.150.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.150.3)\
      Sat 2012-02-11 03:25:49 +0100
      * fixes bug(s): [Bug #930145](https://bugs.launchpad.net/bugs/930145)
      * A recent change in the server protocol code broke SSL connection for some\
        client libraries.
      * Protocol documentation\
        ([MySQL\_Internals\_ClientServer\_Protocol](https://forge.mysql.com/wiki/MySQL_Internals_ClientServer_Protocol)) says\
        that initial packet sent by client if client wants SSL, consists of client\
        capability flags only (4 bytes or 2 bytes edependent on protocol\
        versionl).
      * Some clients happen to send more in the initial SSL packet (C client,\
        Python connector), while others (Java, .NET) follow the docs and send only\
        client capability flags.
      * A change that broke Java client was a newly introduced check that frst\
        client packet has 32 or more bytes. This is generally wrong, if client\
        capability flags contains CLIENT\_SSL.
      * Also, fixed the code such that read max client packet size and charset in\
        the first packet prior to SSL handshake. With SSL, clients do not have to\
        send this info, they can only send client flags.
      * This is now fixed such that max packet size and charset are not read prior\
        to SSL handshake, in case of SSL they are read from the "complete" client\
        authentication packet after SSL initialization.
* [Revision #3414](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3414) \[merge]\
  Fri 2012-02-10 22:09:57 +0100
  * Merge fix for [Bug #910817](https://bugs.launchpad.net/bugs/910817): Race condition in kill\_threads\_for\_user().
  * [Revision #3412.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3412.1.1) \[merge]\
    Fri 2012-02-10 21:20:32 +0100
    * Merge fix for [Bug #910817](https://bugs.launchpad.net/bugs/910817): Race condition in kill\_threads\_for\_user().
    * [Revision #3381.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3381.2.1)\
      Fri 2012-02-10 21:19:12 +0100
      * [Bug #910817](https://bugs.launchpad.net/bugs/910817): Race condition in kill\_threads\_for\_user()
      * The code was accessing a pointer in a mem\_root that might be freed by\
        another concurrent thread. Fix by moving the access to be done while the\
        LOCK\_thd\_data is held, preventing the memory from being freed too early.
* [Revision #3413](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3413) \[merge]\
  Fri 2012-02-10 22:56:34 +0200
  * Automatic merge
  * [Revision #3411.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3411.1.1)\
    Fri 2012-02-10 22:53:46 +0200
    * Fixed that prepared statements are properly igored (if possible) by query cache.
* [Revision #3412](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3412)\
  Thu 2012-02-09 23:35:26 +0200
  * Test case for [Bug #905353](https://bugs.launchpad.net/bugs/905353)
  * The bug itself is fixed by the patch for [Bug #908269](https://bugs.launchpad.net/bugs/908269)
* [Revision #3411](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3411)\
  Fri 2012-02-03 12:49:17 -0800
  * Made mrr related counters temporarily invisible until we agree upon their names.
* [Revision #3410](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3410)\
  Fri 2012-02-03 16:56:12 +0200
  * Fixed typos in Query Cache.
* [Revision #3409](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3409) \[merge]\
  Fri 2012-02-03 13:32:29 +0200
  * Merge with 5.2
  * [Revision #2732.46.69](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.69)\
    Fri 2012-02-03 12:24:55 +0200
    * Fixed DELETE issues of view over view over table.
    * [Revision #2732.46.68](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.68)\
      Fri 2012-02-03 10:31:30 +0200
      * Added 5.2 test result delimiter
      * [Revision #2732.46.67](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.67)\
        Fri 2012-02-03 10:28:23 +0200
        * Fix check of view updatability in case of underlying view changes its\
          updatability.
        * For single table update/insert added deep check of single tables\
          (single\_table\_updatable()). For multi-table view insert added additional\
          check of target table (check\_view\_single\_update).
        * Multi-update was correct.
        * Test suite for all cases added.
* [Revision #3408](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3408)\
  Fri 2012-02-03 13:01:05 +0200
  * Moving [Bug #794005](https://bugs.launchpad.net/bugs/794005) to 5.3 + fixing INSERT of multi-table view.
* [Revision #3407](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3407)\
  Fri 2012-02-03 00:46:34 -0800
  * Back-ported the fix for bug #12831587 from mysql-5.6 code line.
  * The comment for the fix commit says:
    * Due to the changes required by ICP we first copy a row from the InnoDB\
      format to the MySQL row buffer and then copy it to the pre-fetch queue.\
      This was done for the non-ICP code path too. This change removes the double\
      copy for the latter.
* [Revision #3406](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3406)\
  Thu 2012-02-02 22:22:27 -0800
  * Applied the patch from mysql-5.6 code line that fixed\
    a significant performance drop for high concurrency bechmarks (bug #11765850
* [MySQL Bug #58854](https://bugs.mysql.com/bug.php?id=58854)).
* Here's the comment of the patch commit:
  * The bug is that the InnoDB pre-fetch cache was not being used in\
    row\_search\_for\_mysql(). Secondly the changeset that planted the bug also\
    introduced some inefficient code. It would read an extra row, convert it to\
    MySQL row format (for ICP==off), copy the row to the pre-fetch cache row\
    buffer, then check for cache overflow and dequeue the row that was pushed\
    if there was a possibility of a cache overflow.
* [Revision #3405](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3405) \[merge]\
  Wed 2012-02-01 17:48:45 -0800
  * Merge.
  * [Revision #3403.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3403.1.1) \[merge]\
    Wed 2012-02-01 15:48:02 -0800
    * Merge 5.2->5.3 in preparation for the release of mariadb-5.3.4-rc.
    * [Revision #2732.46.66](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.66)\
      Mon 2012-01-23 11:43:28 +0100
      * fixes bug(s): [MDEV-106](https://jira.mariadb.org/browse/MDEV-106)
      * [MDEV-106](https://jira.mariadb.org/browse/MDEV-106) my\_gethwaddr() does not compile on Solaris 11
    * [Revision #2732.46.65](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.65)\
      Fri 2012-01-20 23:54:43 -0800
      * Fixed [Bug #919427](https://bugs.launchpad.net/bugs/919427).
      * The function subselect\_uniquesubquery\_engine::copy\_ref\_key has to take\
        into account that when EXPLAIN is processed the array of store\_key object\
        created for any TABLE\_REF may contain elements for constant items. These\
        items should be ignored by thefunction.
    * [Revision #2732.46.64](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.64)\
      Thu 2012-01-12 20:13:41 +0100
      * [Bug #901693](https://bugs.launchpad.net/bugs/901693) dialog.c:perform\_dialog treats every password prompt as first
    * [Revision #2732.46.63](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.63)\
      Thu 2012-01-12 20:13:22 +0100
      * [Bug #893522](https://bugs.launchpad.net/bugs/893522) more problems found by PVS Studio
    * [Revision #2732.46.62](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.62)\
      Thu 2012-01-12 20:12:46 +0100
      * openpam compatibility
    * [Revision #2732.46.61](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.61)\
      Thu 2012-01-12 20:12:14 +0100
      * fixes for get\_password():
        1. on windows: don't hang when there's no console, that is, \_getch() returns -1.
        2. on windows: \_getch() returns an int, not char.\
           to distinguish between (char)255 and (int)-1
        3. everywhere. isspace(pos\[-1]) == ' ' never worked,\
           isspace() returns a boolean, not a char. the never-worked loop was\
           removed to preserve the existing behavior.
    * [Revision #2732.46.60](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.60)\
      Fri 2011-12-30 13:57:03 +0100
      * plugin renamed socket\_peercred -> unix\_socket.
      * test added.
    * [Revision #2732.46.59](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.59)\
      Thu 2011-12-29 22:52:13 +0100
      * on windows: don't link all plugins with mysqld, only do it for storage engines.
    * [Revision #2732.46.58](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.58)\
      Sat 2012-01-14 00:02:02 -0800
      * Back-ported the test case for bug #12616253 from mariadb-5.3 that\
        was actually a duplicate of [Bug #888456](https://bugs.launchpad.net/bugs/888456) fixed in mariadb-5.2.
    * [Revision #2732.46.57](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.57)\
      Fri 2012-01-13 19:00:50 -0800
      * Back-ported the fix and the test case for [MySQL Bug #50257](https://bugs.mysql.com/bug.php?id=50257) from mariadb-5.3 code line.
      * Adjusted results for a few test cases.
    * [Revision #2732.46.56](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.56)\
      Fri 2012-01-13 12:23:19 -0800
      * Back-ported the test cases for bug #12763207 from mysql-5.6 code line into 5.2
      * Completed the fix for this bug.
      * Note: in 5.3 the affected 'if' statement in Item\_in\_subselect::single\_value\_transformer()\
        starting with the condition (thd->variables.sql\_mode & MODE\_ONLY\_FULL\_GROUP\_BY)\
        should be removed altogether. The change from table.cc is not needed either.
      * This is because in 5.3
        * min/max transformation for subqueries are done at the optimization phase
        * evaluation of the expensive subqueries is done at the execution phase.
      * Added an `EXPLAIN EXTENDED` to the test case for bug #12329653.
    * [Revision #2732.46.55](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.55)\
      Tue 2012-01-10 19:26:47 +0100
      * [MDEV-50](https://jira.mariadb.org/browse/MDEV-50) : Fix default compilation comment
    * [Revision #2732.46.54](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.54)\
      Tue 2012-01-10 19:23:00 +0100
      * Fix [MDEV-49](https://jira.mariadb.org/browse/MDEV-49) : version\_compile\_machine server variable is 'unknown' for x64 builds
    * [Revision #2732.46.53](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.53)\
      Sun 2012-01-08 20:29:05 +0200
      * Fixed compiler and test failures found by buildbot
    * [Revision #2732.46.52](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.52) \[merge]\
      Sat 2012-01-07 14:59:03 +0200
      * Merge
      * [Revision #2732.51.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.51.1)\
        Sat 2012-01-07 10:23:46 +0200
        * Fixed wrong merge
    * [Revision #2732.46.51](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.51)\
      Thu 2012-01-05 11:06:52 +0200
      * Fix of [Bug #793589](https://bugs.launchpad.net/bugs/793589) Wrong result with double ORDER BY\
        Problem was in caching 'eq\_ref' dependency between calls of remove\_const() for ORDER BY and GROUP BY lists.
    * [Revision #2732.46.50](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.50) \[merge]\
      Wed 2012-01-04 17:22:06 +0200
      * Merge with 5.1
      * [Revision #2643.143.68](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.68)\
        Thu 2011-12-29 21:55:17 -0800
      * Fixed [Bug #848652](https://bugs.launchpad.net/bugs/848652).
      * The cause of this bug was the same as for [Bug #902356](https://bugs.launchpad.net/bugs/902356) fixed for 5.3.
      * [Revision #2643.143.67](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.67)\
        Wed 2011-12-21 13:23:15 +0200
        * Fixes [Bug #907049](https://bugs.launchpad.net/bugs/907049) "Server started with skip-aria crashes on an attempt to connect to it"
    * [Revision #2732.46.49](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.49)\
      Mon 2012-01-02 23:52:31 +0100
      * Fix embedded/windows tests- move COND\_manager and LOCK\_manager to sql\_manager.cc, to prevent race condition that results into accessing already destroyed critical section
    * [Revision #2732.46.48](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.48)\
      Thu 2011-12-29 15:09:20 -0800
      * Fixed [Bug #806057](https://bugs.launchpad.net/bugs/806057).
      * A table expression with a natural join or a USING clause is transformed\
        into an equivalent expression with equi-join ON conditions. If a reference\
        to a virtual column happened to occur only in these generated equi-join\
        conditions then it was not erroneously marked in the TABLE::vcol\_set\
        bitmap. This could lead to wrong results for queries containing natural\
        join expressions or USING clauses.
    * [Revision #2732.46.47](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.47)\
      Wed 2011-12-28 18:47:01 -0800
      * Fixed [Bug #777654](https://bugs.launchpad.net/bugs/777654).
      * The method Item\_sum\_num::fix\_fields() calculated the value of\
        the flag Item\_sum\_num::maybe\_null in some cases incorrectly.
    * [Revision #2732.46.46](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.46)\
      Tue 2011-12-27 19:13:53 -0800
      * Fixed [Bug #879860](https://bugs.launchpad.net/bugs/879860).
      * The MIN/MAX optimization cannot be applied to a subquery if its WHERE clause\
        contains a conjunctive condition depending on an outer reference.
    * [Revision #2732.46.45](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.45)\
      Tue 2011-12-27 13:19:13 -0800
      * Fixed [Bug #904345](https://bugs.launchpad.net/bugs/904345).
      * The MIN/MAX optimizer code from the function opt\_sum\_query erroneously\
        did not take into account conjunctive conditions that did not depend on\
        any table, yet were not identified as constant items. These could be\
        items containing rand() or PS/SP parameters. These items are supposed\
        to be evaluated at the execution phase. That's why if such conditions\
        can be extracted from the WHERE condition the MIN/MAX optimization is\
        not applied as currently it is always done at the optimization phase.
      * (In 5.3 expensive subqueries are also evaluated only at the execution\
        phase. So, if a constant condition with such subquery can be extracted\
        from the WHERE clause the MIN/MAX optimization should not be applied\
        in 5.3.)
      * IF an IN/ALL/SOME predicate with a constant left part is transformed\
        into an EXISTS subquery the resulting subquery should not be considered\
        uncacheable if the right part of the predicate is not uncacheable.
      * Backported the function dbug\_print\_item() from 5.3. The function is used\
        only for debugging.
    * [Revision #2732.46.44](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.44) \[merge]\
      Fri 2011-12-23 15:02:57 +0100
      * merge
      * [Revision #2732.50.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.50.1)\
        Thu 2011-12-22 15:50:33 +0100
      * [Bug #906638](https://bugs.launchpad.net/bugs/906638) : Fixes to build oqgraph with boost 1.48
      * dijkstra\_shortest\_paths() needs a Graph as first parameter, in case of reverse\_graph we now need to use\
        its m\_g member
      * use `boost::tuples::tie()` on all places where `<<code.>tie()<</code>>` was used . Reason -\
        fix the build with Visual Studio 10 SP1 (which includes std:tr1:tie, thus creating ambiguity)
    * [Revision #2732.46.43](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.43)\
      Thu 2011-12-22 11:07:04 +0100
      * compilation warning - unused variable
    * [Revision #2732.46.42](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.42)\
      Wed 2011-12-21 12:45:53 +0200
      * Supression condition made wider to cover some other system cases.
    * [Revision #2732.46.41](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.41)\
      Tue 2011-12-20 01:56:41 -0800
      * Fixed [Bug #794005](https://bugs.launchpad.net/bugs/794005)
      * The function st\_table::mark\_virtual\_columns\_for\_write() did not take into\
        account the fact that for any table the value of st\_table::vfield is 0\
        when there are no virtual columns in the table definition.
    * [Revision #2732.46.40](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.40)\
      Mon 2011-12-19 14:55:30 -0800
      * Fixed [Bug #906322](https://bugs.launchpad.net/bugs/906322)
      * If the sorted table belongs to a dependent subquery then the function\
        create\_sort\_index() should not clear TABLE:: select and TABLE::select for\
        this table after the sort of the table has been performed, because these\
        members are needed for the second execution of the subquery.
* [Revision #3404](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3404)\
  Wed 2012-02-01 17:09:49 +0200
  * fix for [Bug #921878](https://bugs.launchpad.net/bugs/921878)
  * Problem was in try to check/use Item\_direct\_ref of derived view when we have to use real Item\_field under it.
* [Revision #3403](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3403)\
  Tue 2012-01-31 21:12:26 +0100
  * sort status variables alphabetically in mysqld.cc
* [Revision #3402](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3402)\
  Mon 2012-01-30 20:34:47 +0400
  * [Bug #923246](https://bugs.launchpad.net/bugs/923246): Loosescan reports different result than other semijoin methods
  * If LooseScan is used with quick select, require that quick select produces\
    data in key order (this disables use of MRR, which can return data in arbitrary order).
* [Revision #3401](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3401) \[merge]\
  Mon 2012-01-30 17:38:14 +0400
  * Merge fix for [Bug #922254](https://bugs.launchpad.net/bugs/922254)
    * [Revision #3397.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3397.1.1)\
      Fri 2012-01-27 17:35:26 +0400
      * [Bug #922254](https://bugs.launchpad.net/bugs/922254): Assertion \`0' failed at item\_cmpfunc.cc:5899: Item\* Item\_equal::get\_first(JOIN\_TAB\*, Item\*)
      * Fixed Item\* Item\_equal::get\_first(JOIN\_TAB \*context, Item \*field\_item) to work correctly in the case where:
        * context!= NO\_PARTICULAR\_TAB, it points to a table within SJ-Materialization nest
        * field\_item points to an item\_equal that has a constant Item\_field but does not have any fields\
          from tables that are within semi-join nests.
* [Revision #3400](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3400)\
  Sat 2012-01-28 01:12:45 -0800
  * Fixed [Bug #922971](https://bugs.launchpad.net/bugs/922971)
  * Applied the fix for bug #12546542 from the mysql-5.6 code line:
  * JOIN\_CACHE::join\_records forgot to reset JOIN\_TAB::first\_unmatched\
    in some cases.
* [Revision #3399](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3399) \[merge]\
  Fri 2012-01-27 19:23:08 -0800
  * Merge.
  * [Revision #3393.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3393.1.1)\
    Fri 2012-01-27 19:01:26 -0800
    * Back-ported test cases for [MySQL Bug #59919](https://bugs.mysql.com/bug.php?id=59919) of mysql-5.6 code line. The bug could\
      not be reproduced in the latest release of mariadb-5.3 as it was fixed\
      by Sergey Petrunia when working on the problems concerning outer joins within\
      in subqueries converted to semi-joins.
* [Revision #3398](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3398)\
  Fri 2012-01-27 17:51:40 +0400
  * Make testcase stable by adding `--sorted_result` for SHOW STATUS commands.
* [Revision #3397](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3397)\
  Thu 2012-01-26 14:20:34 +0400
  * Fix compile failure when built without query cache:\
    define `QUERY_CACHE_DB_LENGTH_SIZE 0`, just like it is done\
    with `QUERY_CACHE_FLAGS_SIZE`.
* [Revision #3396](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3396)\
  Thu 2012-01-26 12:22:02 +0400
  * Sort counters by name (will this make them show in the same order on all platforms?)
* [Revision #3395](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3395)\
  Wed 2012-01-25 22:05:20 +0400
  * [Bug #920713](https://bugs.launchpad.net/bugs/920713): Wrong result (missing rows) with firstmatch+BNL, IN subquery, ...
    * Disable use of join cache when we're using FirstMatch strategy, and the join\
      order is such that subquery's inner tables are interleaved with outer. Join\
      buffering code is incapable of handling such join orders.
    * The testcase requires use of @@debug\_optimizer\_prefer\_join\_prefix to hit the bug,\
      but I'm pushing it anyway (including the mention of the variable in .test file),\
      so that it can be found and enabled when/if we get something comparable in the\
      main tree.
* [Revision #3394](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3394) \[merge]\
  Wed 2012-01-25 18:36:57 +0400
  * Merge
  * [Revision #3390.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3390.1.3)\
    Wed 2012-01-25 18:33:57 +0400
    * [Bug #920255](https://bugs.launchpad.net/bugs/920255): Wrong result (extra rows) with loosescan and IN subquery
    * The problem was that LooseScan execution code assumed that tab->key holds\
      the index used for looseScan. This is only true when range or full index\
      scan are used. In case of ref access, the index is in tab->ref.key (and\
      tab->index==0 which explains how LooseScan passed tests with ref access: they\
      used one index)
    * Fixed by setting/using loosescan\_key, which always the correct index#.
  * [Revision #3390.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3390.1.2)\
    Wed 2012-01-25 18:27:34 +0400
    * Update handler status variables after the last commit.
  * [Revision #3390.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3390.1.1)\
    Mon 2012-01-23 23:35:52 +0400
    * Add MRR counters: Handler\_mrr\_init, Handler\_mrr\_extra\_rowid\_sorts,\
      Handler\_mrr\_extra\_key\_sorts.
* [Revision #3393](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3393)\
  Mon 2012-01-23 15:14:13 +0200
  * Fixed creating limit for exists subquery.
* [Revision #3392](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3392)\
  Sun 2012-01-22 12:54:30 -0800
  * Back-ported test cases for [MySQL Bug #54437](https://bugs.mysql.com/bug.php?id=54437), [MySQL Bug #55955](https://bugs.mysql.com/bug.php?id=55955), [MySQL Bug #52329](https://bugs.mysql.com/bug.php?id=52329), [MySQL Bug #57623](https://bugs.mysql.com/bug.php?id=57623) from subquery\_sj\
    of mysql-5.6 code line. The bugs could not be reproduced in the latest release\
    of mariadb-5.3 as they were fixed either when the code of subquery optimization\
    was back-ported from mysql-6.0 or later when some other bugs were fixed.
* [Revision #3391](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3391)\
  Sat 2012-01-21 20:58:23 -0800
  * Back-ported test cases for [MySQL Bug #53060](https://bugs.mysql.com/bug.php?id=53060), [MySQL Bug #53305](https://bugs.mysql.com/bug.php?id=53305), [MySQL Bug #50358](https://bugs.mysql.com/bug.php?id=50358), [MySQL Bug #49453](https://bugs.mysql.com/bug.php?id=49453) from subquery\_sj\
    of mysql-5.6 code line. The bugs could not be reproduced in the latest release\
    of mariadb-5.3 as they were fixed either when the code of subquery optimization\
    was back-ported from mysql-6.0 or later when some other bugs were fixed.
* [Revision #3390](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3390)\
  Fri 2012-01-20 02:11:53 +0400
  * [Bug #912513](https://bugs.launchpad.net/bugs/912513): Wrong result (missing rows) with join\_cache\_hashed+materialization+semijoin=on
  * equality substitution code was geared towards processing WHERE/ON clauses.\
    that is, it assumed that it was doing substitions on the code that
    * wasn't attached to any particular join\_tab yet
    * was going to be fed to make\_join\_select() which would take the condition\
      apart and attach various parts of it to tables inside/outside semi-joins.
  * However, somebody added equality substition for ref access. That is, if\
    we have a ref access on TBL.key=expr, they would do equality substition in\
    'expr'. This possibility wasn't accounted for.
  * Fixed equality substition code by adding a mode that does equality\
    substition under assumption that the processed expression will be\
    attached to a certain particular table TBL.
* [Revision #3389](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3389)\
  Thu 2012-01-19 23:44:43 +0400
  * [Bug #912538](https://bugs.launchpad.net/bugs/912538): Wrong result (missing rows) with semijoin=on, firstmatch=on, ...
    * setup\_semijoin\_dups\_elimination() would incorrectly set join\_tab->do\_firstmatch\
      when the join order had outer tables interleaved with inner.
* [Revision #3388](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3388)\
  Thu 2012-01-19 13:46:59 +0100
  * Fix compiler warning on Windows.
* [Revision #3387](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3387) \[merge]\
  Wed 2012-01-18 15:28:13 -0800
  * Merge
    * [Revision #3384.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3384.1.1) \[merge]\
      Wed 2012-01-18 14:19:28 -0800
      * Merge
      * [Revision #3381.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3381.1.1)\
        Wed 2012-01-18 03:31:20 -0800
        * Fixed [Bug #917990](https://bugs.launchpad.net/bugs/917990).
        * If the expression for a derived table of a query contained a LIMIT\
          clause the estimate of the number of rows in this derived table\
          returned by the EXPLAIN command could be badly off since the\
          optimizer ignored the limit number from the LIMIT clause when\
          getting the estimate.
        * The call of the method SELECT\_LEX\_UNIT->set\_limit added in the code\
          of mysql\_derived\_optimize() will be needed also in maria-5.5 where\
          parameters in the LIMIT clause are supported.
* [Revision #3386](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3386)\
  Wed 2012-01-18 14:52:56 +0100
  * multi-delete should ignore semi-join internal temp tables, when looking for tables to delete from
* [Revision #3385](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3385) \[merge]\
  Wed 2012-01-18 14:52:38 +0100
  * [Bug #893522](https://bugs.launchpad.net/bugs/893522) more problems found by PVS Studio
  * [Revision #3280.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3280.1.1) \[merge]\
    Mon 2011-11-14 00:21:22 +0100
    * 5.2->5.3 merge
* [Revision #3384](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3384)\
  Wed 2012-01-18 12:53:50 +0200
  * Adjust test results after Monty's push of the new\
    handler counter Handler\_read\_rnd\_deleted.
* [Revision #3383](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3383)\
  Tue 2012-01-17 15:16:00 +0200
  * Removed unused code merged from 5.2. In 5.3 we fix this problem by checking if we put max/min group function\
    without GROUP BY artificially in case of MODE\_ONLY\_FULL\_GROUP\_BY sql mode.
* [Revision #3382](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3382)\
  Fri 2012-01-13 14:35:49 +0200
  * Added Handler\_read\_rnd\_deleted, number of deleted rows found with ha\_read\_rnd\_first.
* [Revision #3381](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3381)\
  Wed 2012-01-11 10:35:16 +0200
  * Fix the comment.
* [Revision #3380](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3380)\
  Tue 2012-01-10 23:26:00 +0200
  * Fix for [Bug #908269](https://bugs.launchpad.net/bugs/908269) Wrong result with subquery in select list, EXISTS, constant MyISAM/Aria table.
  * Problem: When building the condition for JOIN::outer\_ref\_cond the optimizer forgot to take into account\
    that this condition could depend on constant tables as well.
* [Revision #3379](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3379) \[merge]\
  Tue 2012-01-10 18:20:56 +0400
  * Merge fix for [Bug #912510](https://bugs.launchpad.net/bugs/912510)
  * [Revision #3376.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3376.1.1)\
    Sun 2012-01-08 14:43:14 +0400
    * [Bug #912510](https://bugs.launchpad.net/bugs/912510): Crash in do\_copy\_not\_null with semijoin=ON, firstmatch=ON, aggregate ...
      * Create/use do\_copy\_nullable\_row\_to\_notnull() function for ref access, which is used\
        when copying from not-NULL field in table that can be NULL-complemented to not-NULL field.
* [Revision #3378](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3378)\
  Mon 2012-01-09 13:49:47 +0200
  * Fixed that `--sorted-result` in mysql-test-run also works for exec
* [Revision #3377](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3377)\
  Sun 2012-01-08 21:14:07 +0100
  * [MDEV-77](https://jira.mariadb.org/browse/MDEV-77) - possible deadlock in XtraDB async io subsystem on Windows.
  * Split IO threads into ones that handle only read completion and ones that\
    handle only write completion, as it was originally done, but got lost with\
    "completion port" patch. The reason we need to have dedicated read and\
    dedicated write threads is that read completion routine can block waiting\
    for write io to complete, and in rare cases where all io threads are\
    handling async reads, it can deadlock.
* [Revision #3376](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3376)\
  Mon 2012-01-02 20:06:36 -0800
  * Fixed [Bug #910083](https://bugs.launchpad.net/bugs/910083)
  * The patch for [Bug #685411](https://bugs.launchpad.net/bugs/685411) erroneously removed a call of engine->set\_thd()\
    from Item\_subselect::fix\_fields().
* [Revision #3375](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3375)\
  Fri 2011-12-30 22:19:05 +0100
  * Make test results stable.
* [Revision #3374](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3374)\
  Fri 2011-12-30 20:22:52 +0100
  * Update version in configure.in (was forgotten in 5.3.3 release).
* [Revision #3373](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3373)\
  Fri 2011-12-30 11:34:29 +0100
  * Continuation of the efforts in previous cset.
* [Revision #3372](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3372)\
  Thu 2011-12-29 22:29:02 +0100
  * Make test results stable (they weren't, because filesort() used to read\
    from a heap temptable, which uses pointers to records (that is, byte\*\
    pointers) as rowids.
  * This meant that for rows with the same sort key value, the order was\
    determined by memory layout.
* [Revision #3371](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3371)\
  Wed 2011-12-28 12:12:48 +0400
  * Update test results.
* [Revision #3370](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3370) \[merge]\
  Wed 2011-12-28 03:37:34 +0400
  * Merge
  * [Revision #3364.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3364.1.1)\
    Tue 2011-12-20 00:55:32 +0400
    * [Bug #906357](https://bugs.launchpad.net/bugs/906357): Incorrect result with outer join and full text match
      * The problem was that const-table-reading code would try to evaluate MATCH()\
        before init\_ftfuncs() was called.
      * Fixed by making MATCH function "expensive" so that nobody tries to evaluate it\
        at optimization phase.
* [Revision #3369](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3369)\
  Sun 2011-12-25 18:03:03 -0800
  * Changed a test case from join\_cache.test to make it platform independent.
* [Revision #3368](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3368)\
  Sat 2011-12-24 08:55:10 -0800
  * Back-ported the patch of the mysql-5.6 code line that\
    fixed several defects in the greedy optimization:
    1. The greedy optimizer calculated the 'compare-cost' (CPU-cost)\
       for iterating over the partial plan result at each level in\
       the query plan as 'record\_count / (double) TIME\_FOR\_COMPARE'

This cost was only used locally for 'best' calculation at each\
level, and _not_ accumulated into the total cost for the query plan.

This fix added the 'CPU-cost' of processing 'current\_record\_count'\
records at each level to 'current\_read\_time' _before_ it is used as\
'accumulated cost' argument to recursive\
best\_extension\_by\_limited\_search() calls. This ensured that the\
cost of a huge join-fanout early in the QEP was correctly\
reflected in the cost of the final QEP.

To get identical cost for a 'best' optimized query and a\
straight\_join with the same join order, the same change was also\
applied to optimize\_straight\_join() and get\_partial\_join\_cost()\
1\. Furthermore to get equal cost for 'best' optimized query and a\
straight\_join the new code substrcated the same '0.001' in\
optimize\_straight\_join() as it had been already done in\
best\_extension\_by\_limited\_search()\
1\. When best\_extension\_by\_limited\_search() aggregated the 'best' plan a\
plan was 'best' by the check :

'if ((search\_depth == 1) || (current\_read\_time < join->best\_read))'

The term '(search\_depth == 1' incorrectly caused a new best plan to be\
collected whenever the specified 'search\_depth' was reached - even if\
this partial query plan was more expensive than what we had already\
found.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
