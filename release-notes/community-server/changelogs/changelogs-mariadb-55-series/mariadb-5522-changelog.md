# MariaDB 5.5.22 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.askmonty.org/mariadb/5.5.22) |[Release Notes](../../old-releases/5.5/5.5.22.md) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 29 Mar 2012

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.22.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3357](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3357) \[merge]\
  Wed 2012-03-28 20:25:31 +0200
  * 5.3 merge
  * [Revision #2502.546.20](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.20)\
    Tue 2012-03-27 16:06:00 +0300
    * Added feature request from [Bug #956585](https://bugs.launchpad.net/bugs/956585) "Feature request - prevent truncating query in mytop"
    * Added feature request 'reading of my.cnf files' to mytop
    * Thanks to Jean Weisbuch for the patch/suggestion.
  * [Revision #2502.546.19](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.19)\
    Tue 2012-03-27 14:43:26 +0400
    * [Bug #965872](https://bugs.launchpad.net/bugs/965872): Server crashes in embedding\_sjm on a simple 1-table select with AND and OR
      * This is a regession introduced by fix for [Bug #951937](https://bugs.launchpad.net/bugs/951937)
      * The problem was that there were scenarios where check\_simple\_equality() would create an\
        Item\_equal object but would not call item\_equal->set\_context\_field() on it.
      * The fix was to add the missing calls.
  * [Revision #2502.546.18](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.18) \[merge]\
    Mon 2012-03-26 21:38:24 +0400
    * Merge
    * [Revision #2502.549.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.549.1)\
      Mon 2012-03-26 21:34:24 +0400
      * [Bug #951283](https://bugs.launchpad.net/bugs/951283): Wrong result (missing rows) with semijoin+firstmatch, IN/ANY subquery
        * The problem was with execution strategy for cases where FirstMatch's inner tables\
          were interleaved with outer-uncorrelated tables.
        * I was unable to find any cases where such join orders would be practically useful,\
          so fixed it by disabling them.
  * [Revision #2502.546.17](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.17)\
    Mon 2012-03-26 16:06:42 +0300
    * Bug fix for [MySQL Bug #61209](https://bugs.mysql.com/bug.php?id=61209) "auto\_increment\_offset != 1 + innodb\_autoinc\_lock\_mode=1 => bulk inserts fail"
    * Patch and test case by Patryk Pomykalski
  * [Revision #2502.546.16](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.16)\
    Mon 2012-03-26 15:05:50 +0300
    * Sorted some test results that can be different on different machines
  * [Revision #2502.546.15](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.15)\
    Mon 2012-03-26 13:29:45 +0300
    * Fixed [Bug #963603](https://bugs.launchpad.net/bugs/963603) "Assertion \`lock\_type != TL\_UNLOCK && (lock\_type == TL\_IGNORE || file->lock.type == TL\_UNLOCK)' failed in ha\_maria::store\_lock with DML, triggers, views"
  * [Revision #2502.546.14](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.14) \[merge]\
    Mon 2012-03-26 13:52:55 +0400
    * Merge
    * [Revision #2502.548.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.548.1)\
      Mon 2012-03-26 13:47:00 +0400
      * [Bug #951937](https://bugs.launchpad.net/bugs/951937): Wrong result (missing rows) with semijoin+materialization, IN subquery, InnoDB, TEMPTABLE view
        * Fix equality propagation to work with SJM nests and OR clauses (full descirption of problem and\
          solution in the comment in the patch)
        * (The second commit with post-review fixes)
  * [Revision #2502.546.13](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.13)\
    Mon 2012-03-26 11:46:01 +0300
    * Increased version number
  * [Revision #2502.546.12](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.12)\
    Sun 2012-03-25 18:31:35 +0400
    * [Bug #962667](https://bugs.launchpad.net/bugs/962667): Assertion \`0' failed in QUICK\_INDEX\_SORT\_SELECT::need\_sorted\_output()
    * The problem was that
      * we've picked a LooseScan that used full index scan (tab->type==JT\_ALL) on certain index.
      * there was also a quick select (tab->quick!=NULL), that used other indexes.
      * some old code assumes that (tab->type==JT\_ALL && tab->quick) -> means that the\
        quick select should be used, which is not true.
    * Fixed by discarding the quick select as soon as we know we're using LooseScan\
      without using the quick select.
* [Revision #3356](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3356)\
  Wed 2012-03-28 19:26:00 +0200
  * debug\_sync is now a service, available to dynamically loaded plugins.
  * new make target - abi\_update
* [Revision #3355](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3355) \[merge]\
  Wed 2012-03-28 01:04:46 +0200
  * mysql-5.5.22 merge
* [Revision #3354](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3354)\
  Tue 2012-03-27 16:16:44 +0200
  * [MDEV-201](https://jira.mariadb.org/browse/MDEV-201) - Assertion \`!thd->spcont' failed in net\_send\_error on server shutdown
  * bug in semisync plugin. It didn't check thd->killed before waiting on mysys->current\_cond,\
    and thus an attepmt to kill the thread (on shutdown) was lost
* [Revision #3353](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3353)\
  Mon 2012-03-26 14:39:52 +0200
  * move DBUG\_END() after my\_thread\_global\_end(), when all threads have already died.
* [Revision #3352](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3352)\
  Mon 2012-03-26 12:33:49 +0200
  * a couple of minor post-5.5-merge cleanups
* [Revision #3351](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3351) \[merge]\
  Sun 2012-03-25 19:36:06 +0200
  * merge
  * [Revision #3349.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3349.1.1)\
    Sun 2012-03-25 19:27:24 +0200
    * Small Windows specific performance fixes:
      * Use native memcmp() supplied with C runtime instead of hand-unrolled loop ptr\_compare\_N loop
        * Prior to fix ptr\_compare\_0() has 3.7% samples in OLTP-RO in-memory.
        * Fix brings this down to 1.8% (all memcmp samples)
      * Innodb : fix UT\_RELAX\_CPU to be defined as YieldProcessor, as was also originally intended\
        (but intention was lost in the #ifdef maze
    * This reduces number of ut\_delay() samples in profile from 1.5% to 0.5%
* [Revision #3350](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3350)\
  Sat 2012-03-24 21:51:10 +0100
  * fix a memory leak in dbug
* [Revision #3349](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3349) \[merge]\
  Sat 2012-03-24 18:25:00 +0100
  * Merge [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md) into latest [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md)
  * [Revision #3342.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3342.1.1) \[merge]\
    Sat 2012-03-24 18:21:22 +0100
    * Merge [mariadb 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series)->[mariadb 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series)
  * [Revision #2502.546.11](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.11)\
    Sat 2012-03-24 17:08:59 +0100
    * Improve filesort performance for small sorts: Don't write pointers to records that we will never use.
  * [Revision #2502.546.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.10)\
    Fri 2012-03-23 18:22:39 +0200
    * Speedup:
      * Don't call update\_virtual\_fields() if table->vfield is not set
      * Don't prealloc memory for in open\_tables() as this is very seldom used.
  * [Revision #2502.546.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.9)\
    Fri 2012-03-23 18:18:16 +0200
    * Fixes [Bug #941889](https://bugs.launchpad.net/bugs/941889) "JOIN constructors takes a long time in 5.3"
      * Remove all references of MAX\_TABLES from JOIN struct and make these dynamic
      * Updated Join\_plan\_state to allocate just as many elements as it's needed
  * [Revision #2502.546.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.8)\
    Fri 2012-03-23 18:11:29 +0200
    * Speedups:
      * Optimize away calls to hp\_rec\_hashnr() by cashing hash
      * Try to get more rows / block (to minimize overhead of HP\_PTRS) in HEAP tables.
  * [Revision #2502.546.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.7)\
    Thu 2012-03-22 19:56:17 -0700
    * Fixed [Bug #954900](https://bugs.launchpad.net/bugs/954900).
      * If the first component of a ref key happened to be a constant appeared\
        after constant row substitution then no store\_key element should be\
        created for such a component. Yet create\_ref\_for\_key() erroneously could\
        create such an element that caused construction of invalid ref keys and\
        wrong results for some joins.
  * [Revision #2502.546.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.6) \[merge]\
    Thu 2012-03-22 13:23:55 +0100
    * Automerge.
  * [Revision #2502.546.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.5) \[merge]\
    Wed 2012-03-21 19:15:29 +0100
    * merge
    * [Revision #2502.528.20](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.20) \[merge]\
      Wed 2012-03-21 18:30:34 +0100
      * merge
      * [Revision #2502.352.81](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.352.81)\
        Wed 2012-03-21 18:22:02 +0100
        * [Bug #933959](https://bugs.launchpad.net/bugs/933959) Assertion \`0' failed in net\_end\_statement(THD\*) on concurrent SELECT FROM I\_S.INNODB\_SYS\_INDEXES and ALTER TABLE
        * Workaround: report a generic error if an I\_S plugin failed silently.
      * [Revision #2502.352.80](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.352.80)\
        Thu 2012-03-15 15:06:06 +0100
        * Fix access to uninitialized variable in innodb error message in case WriteFile() fails.
      * [Revision #2502.352.79](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.352.79)\
        Wed 2012-03-14 21:16:24 +0100
        * restore my\_safe\_printf\_stderr for "crash-safe sigsegv handler"
          * use vsnprintf()
          * use write() on windows, not WriteFile or fwrite()
          * localtime\_r is still a problem
  * [Revision #2502.546.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.4)\
    Wed 2012-03-21 10:59:20 +0100
    * [MDEV-191](https://jira.mariadb.org/browse/MDEV-191) SHOW TABLES was unnecessary opening .frm files
    * mark the corresponding I\_S table as OPTIMIZE\_I\_S\_TABLE, to let the I\_S optimizer\
      figure out whether files need to be opened, and don't open the tables unless\
      I\_S optimizer says so.
  * [Revision #2502.546.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.3) \[merge]\
    Wed 2012-03-21 11:18:20 +0400
    * Merge [Bug #952372](https://bugs.launchpad.net/bugs/952372)
    * [Revision #2502.547.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.547.1)\
      Sun 2012-03-18 23:58:20 +0400
      * [Bug #952372](https://bugs.launchpad.net/bugs/952372): Server crashes on 2nd execution of PS in find\_field\_in\_tables with semijoin+materialization
        * The problem was that convert\_subq\_to\_jtbm() attached the semi-join\
          TABLE\_LIST object into the wrong list: they used to attach it to the\
          end of parent\_lex->leaf\_tables.head()->next\_local->...->next\_local.\
          This was apparently inccorect, as one can construct an example where\
          JTBM nest is attached to a table that is inside some mergeable VIEW, which\
          breaks (causes crash) for name resolution on the subsequent statement\
          re-execution.
        * Solution: Attach to the "right" list. The "wording" was copied from\
          st\_select\_lex::handle\_derived.
  * [Revision #2502.546.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.2)\
    Tue 2012-03-20 17:03:28 -0700
  * Fixed [Bug #954262](https://bugs.launchpad.net/bugs/954262).
  * This bug in the constructor SEL\_IMERGE::SEL\_IMERGE could\
    cause huge excessive memory requests.
  * [Revision #2502.546.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.546.1)\
    Mon 2012-03-19 01:04:55 +0400
    * [Bug #952583](https://bugs.launchpad.net/bugs/952583): Server crashes in Item\_field::fix\_after\_pullout on INSERT .. SELECT
      * Take into account that there may exist Item\_field objects with context==NULL.
* [Revision #3348](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3348)\
  Sat 2012-03-24 11:24:20 +0100
  * [MDEV-15](https://jira.mariadb.org/browse/MDEV-15) Log all sql errors.
    * modified for MySQL 5.5. Logger service moved to the\
      plugin/sql\_errlog directory to be properly used later.
* [Revision #3347](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3347)\
  Fri 2012-03-23 20:49:47 +0100
  * [MDEV-200](https://jira.mariadb.org/browse/MDEV-200) set session dbug resets the output to stderr.
  * it makes "`./mtr --debug`" unusable
  * revert the mysql fix for [MySQL Bug #46165](https://bugs.mysql.com/bug.php?id=46165).
  * implement shared FILE's with reference counting
* [Revision #3346](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3346)\
  Fri 2012-03-23 10:53:25 +0100
  * fixes bug(s): [MDEV-186](https://jira.mariadb.org/browse/MDEV-186) and [Bug #959701](https://bugs.launchpad.net/bugs/959701)
  * [MDEV-186](https://jira.mariadb.org/browse/MDEV-186) Client programs throw warnings about memory loss when executed with `--help` or alike
    * suppress these harmless but confusing warnings.
    * fix the program name (MY\_INIT) in mysqldump
* [Revision #3345](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3345)\
  Thu 2012-03-22 20:21:14 +0100
  * Fix Windows build
* [Revision #3344](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3344)\
  Thu 2012-03-22 15:44:06 +0100
  * precache results of system tests on Windows
* [Revision #3343](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3343)\
  Thu 2012-03-22 15:37:52 +0100
  * Fix CMake code to work with older cmake version, such as 2.6.2
* [Revision #3342](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3342) \[merge]\
  Thu 2012-03-22 13:26:40 +0100
  * Null merge from 5.3.
  * [Revision #2502.542.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.542.6)\
    Thu 2012-03-22 13:21:15 +0100
    * Backport some simple performance patches from 5.5.
* [Revision #3341](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3341)\
  Thu 2012-03-22 12:31:09 +0100
  * Do not use Valgrind client requests in a normal release build, they have a small but noticable performance impact.
* [Revision #3340](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3340)\
  Mon 2012-03-19 15:00:23 -0700
  * author: Davi Arnaut `<davi 'at' twitter (dot) com>`
  * Make Replication filter settings dynamic.
  * Make the slave options `--replicate-*` dynamic variables so that these\
    options can be changed dynamically while the server is running,\
    which enables users to modify replication filtering rules without\
    having to stop and restart the server.
  * This is accomplished by just requiring that the slave threads are\
    stopped when these options are set dynamically. Since filtering\
    rules are only used by the SQL slave thread, setting them while the\
    thread is not running avoids the need for locking.
* [Revision #3339](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3339) \[merge]\
  Wed 2012-03-21 15:51:13 +0100
  * merge
  * [Revision #3333.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3333.1.1)\
    Wed 2012-03-21 15:41:20 +0100
    * Fix race condition in rpl\_stop\_start\_slave. after kill connection, wait until it is gone in processlist
* [Revision #3338](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3338)\
  Wed 2012-03-21 09:55:48 +0100
  * A few simple performance fixes found with sysbench oltp.lua and Oprofile:
    * Avoid needless load/stores in my\_hash\_sort\_simple due to possible aliasing
    * Avoid expensive Join\_plan\_state constructor in choose\_subquery\_plan when no subquery
    * Avoid calling update\_virtual\_fields for every row when no virtual fields.
* [Revision #3337](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3337) \[merge]\
  Tue 2012-03-20 16:14:04 +0100
  * (no message)
  * [Revision #3326.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3326.1.2)\
    Thu 2012-03-15 10:12:32 +0100
    * more MY\_INIT(argv\[0]) in unittests
* [Revision #3336](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3336)\
  Tue 2012-03-20 16:04:50 +0200
  * Fixed [Bug #947474](https://bugs.launchpad.net/bugs/947474) "Assertion \`table->file->stats.records > 0 || error' failed in join\_read\_const\_table on concurrent SELECT and ALTER, constant Aria table"
  * Remove Aria state history for drop/rename
* [Revision #3335](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3335)\
  Tue 2012-03-20 15:23:56 +0200
  * Cleanups:
    * Don't use SAFEMALLOC on valgrind builds (slows things down)
    * Added back lost option from 5.3: debug-mutex-deadlock-detector
    * Flush pages before taking lock mutex (speeds up closing of Aria tables).
* [Revision #3334](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3334) \[merge]\
  Sat 2012-03-17 12:16:57 -0700
  * Merge
  * [Revision #3331.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3331.1.1) \[merge]\
    Sat 2012-03-17 01:26:58 -0700
    * Merge 5.3->5.5
    * [Revision #2502.542.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.542.5) \[merge]\
      Wed 2012-03-14 13:58:18 +0200
      * Merge 5.2->5.3
      * [Revision #2502.528.19](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.19)\
        Wed 2012-03-14 12:09:03 +0200
        * test suite for LP bug#694450
      * [Revision #2502.528.18](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.18) \[merge]\
        Mon 2012-03-12 12:15:55 +0100
        * merge
        * [Revision #2502.352.78](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.352.78)\
          Mon 2012-03-12 11:31:40 +0100
          * [Bug #952714](https://bugs.launchpad.net/bugs/952714): Fix formatting of the crash messages in signal/exception handler
      * [Revision #2502.528.17](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.17)\
        Mon 2012-03-12 12:14:04 +0100
        * [Bug #952607](https://bugs.launchpad.net/bugs/952607): Do not show MySQL services preinstalled by Dell in the upgrade wizard
      * [Revision #2502.528.16](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.16)\
        Fri 2012-03-09 15:37:16 -0800
        * Fixed LP bug #930814.
        * This bug was introduced into [mariadb 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md) in the December 2010 with\
          the patch that added a new engine property: the ability to support\
          virtual columns.
        * As a result of this bug the information from frm files for tables\
          that contained virtual columns did not appear in the information schema\
          tables.
      * [Revision #2502.528.15](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.15)\
        Fri 2012-03-09 14:28:02 +0200
        * Added test case for [Bug #905782](https://bugs.launchpad.net/bugs/905782) "Assertion `pageno < ((1ULL)` <<\` 40)' failed at ma\_pagecache.c:3438: pagecache\_read or table corruption on INSERT into a ucs2 table"
        * The orignal bug has been fixed earlier
      * [Revision #2502.528.14](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.14)\
        Fri 2012-03-09 14:06:17 +0200
        * Added ucs2 test moved from maria3.test. ([MDEV-167](https://jira.mariadb.org/browse/MDEV-167))
      * [Revision #2502.528.13](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.13)\
        Thu 2012-03-08 22:33:01 -0800
        * Fixed [Bug #884175](https://bugs.launchpad.net/bugs/884175).
        * If in the where clause of the a query some comparison conditions on the\
          field under a MIN/MAX aggregate function contained constants whose sizes\
          exceeded the size of the field then the query could return a wrong result\
          when the optimizer had chosen to apply the MIN/MAX optimization.
        * With such conditions the MIN/MAX optimization still could be applied, yet\
          it would require a more thorough analysis of the keys built to find\
          the value of MIN/MAX aggregate functions with index look-ups.
        * The current patch just prohibits using the MIN/MAX optimization in this\
          situation.
      * [Revision #2502.528.12](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.12) \[merge]\
        Tue 2012-03-06 01:48:38 +0100
        * merge
        * [Revision #2502.545.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.545.1)\
          Tue 2012-03-06 01:46:32 +0100
          * [Bug #947631](https://bugs.launchpad.net/bugs/947631): Uninstall wipes HeidiSQL settings, even if HeidiSQL is installed prior to MariaDB
          * Fixed detection of installed HeidiSQL in the machine, prevent installing own copy if HeidiSQL is already installed.
          * On deinstallation, do not remove settings if official HeidiSQL is detected.
      * [Revision #2502.528.11](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.11)\
        Thu 2012-03-01 09:27:42 +0200
        * Return original checksum value inside the test.
        * Move ucs2 test in separate file ([MDEV-167](https://jira.mariadb.org/browse/MDEV-167)).
    * [Revision #2502.542.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.542.4) \[merge]\
      Tue 2012-03-13 13:49:18 -0700
      * Merge.
      * [Revision #2502.544.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.544.1)\
        Tue 2012-03-13 13:34:20 -0700
        * Fixed [Bug #953649](https://bugs.launchpad.net/bugs/953649).
        * Do not call, directly or indirectly, SQL\_SELECT::test\_quick\_select()\
          for derived materialized tables / views when optimizing joins referring\
          to these tables / views to get cost estimates of materialization.
        * The current code does not create B-tree indexes for materialized\
          derived tables / views. So now it's not possible to get any estimates\
          for ranges conditions over the results of the materialization.
        * The function mysql\_derived\_create() must take into account the fact\
          that array of the KEY structures specifying the keys over a derived\
          table / view may be moved after the optimization phase if the\
          derived table / view is materialized.
    * [Revision #2502.542.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.542.3)\
      Tue 2012-03-13 16:38:43 +0200
      * Fixed [Bug #917689](https://bugs.launchpad.net/bugs/917689) "Archive table corruption crashing MariaDB signal 11"
      * Added 'from\_end' as extra parameter to Field::unpack() to detect wrong from data.
      * Change ha\_archive::unpack\_row() to detect wrong field lengths.
      * Replication code changed to detect wrong field information in events.
    * [Revision #2502.542.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.542.2) \[merge]\
      Mon 2012-03-12 18:21:14 +0400
      * Merge
      * [Revision #2502.543.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.543.2) \[merge]\
        Mon 2012-03-12 18:08:40 +0400
        * Merge
      * [Revision #2502.543.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.543.1)\
        Mon 2012-03-12 17:41:22 +0400
        * [Bug #952297](https://bugs.launchpad.net/bugs/952297): Server crashes on 2nd execution of PS in Field::is\_null with semijoin+materialization
        * The bug would show up
          * when using PS (so that we get re-execution)
          * the left\_expr of the subquery is a reference to viewname.column\_name, so that it crashes\
            when one tries to use it without having called fix\_fields for it.
          * when using SJ-Materialization, which makes use of sj\_subq\_pred->left\_expr expression
        * The fix is to have setup\_conds() fix sj\_subq\_pred->left\_expr for semi-join nests it finds.
    * [Revision #2502.542.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.542.1)\
      Mon 2012-03-12 18:20:30 +0400
      * Better comments
* [Revision #3333](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3333)\
  Fri 2012-03-16 20:52:17 +0100
  * Reduce size of windows MSI by approx. 50%
    * Mark test components, plugins etc with COMPONENT Test, to get them excluded from the MSI
    * Only include debug symbols for client and embedded libs and also\
      mysqld.exe and server plugins (so we can still can get a callstack in case of crash)
  * The rest (all \*.pdbs, test components, MTR) can be obtained from the big ZIP distribution, if required.
* [Revision #3332](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3332)\
  Fri 2012-03-16 17:47:31 +0100
  * Fix several buildot errors on Windows
    * do not attempt loading federatedx dynamically - does not work on Windows embedded
    * race condition in rpl\_start\_stop\_slave
    * fix exclusion rule to catch warning in partition test
* [Revision #3331](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3331)\
  Thu 2012-03-15 00:37:37 +0100
  * Fix compile error - linker does not find extern variables, in sql\_logger.c
  * The file uses external variables defined in another (C++) source file. Since\
    MSVC mangles variables and not only functions, either variables in question\
    should be extern "C", or sql\_logger should be made C++ for link to succeed.
  * Fixed by renaming sql\_logger.c to sql\_logger.cc
* [Revision #3330](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3330)\
  Wed 2012-03-14 19:47:15 +0100
  * another fix for `--innodb-trx*` name conflict
* [Revision #3329](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3329)\
  Wed 2012-03-14 16:37:49 +0400
  * [MDEV-15](https://jira.mariadb.org/browse/MDEV-15) Log SQL errors.
    * mysys/my\_logger.c was moved to sql/sql\_logger.c
    * Logger service was rewritten with file functions instead of stream, so it\
      can handle huge files.
* [Revision #3328](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3328)\
  Wed 2012-03-14 09:40:54 +0400
  * plugin.result fixed.
* [Revision #3327](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3327)\
  Wed 2012-03-14 00:55:56 +0400
  * [MDEV-15](https://jira.mariadb.org/browse/MDEV-15) Log all SQL errors.
    * Added the logger service that provides us with the rotating logs.
      * The plugin SQL\_ERROR\_LOG added. It logs the errors using the 'logger service'\
        for the rotating log files.
      * the example record from the log:`2012-03-09 15:07:29 root[root] @ localhost [] ERROR 1146: Table 'test.xyz' doesn't exist : select * from test.xyz`

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
