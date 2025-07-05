# MariaDB 5.5.20 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.askmonty.org/mariadb/5.5.20) |[Release Notes](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5520-release-notes.md) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 26 Feb 2012

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5520-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3279](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3279) \[merge]\
  Fri 2012-02-24 14:37:00 +0100
  * 5.3 merge
* [Revision #3278](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3278)\
  Thu 2012-02-23 15:31:24 +0100
  * disable safemalloc for valgrind builds.
  * always try to use valgrind headers in debug builds.
  * define HAVE\_valgrind for `--with-valgrind`
  * fix valgrind check in my\_valgrind.h
* [Revision #3277](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3277) \[merge]\
  Wed 2012-02-22 12:21:54 +0400
  * Merge fix for [Bug #920132](https://bugs.launchpad.net/bugs/920132)
* [Revision #3276](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3276) \[merge]\
  Tue 2012-02-21 20:51:56 +0100
  * 5.3 merge
  * [Revision #2502.513.51](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.513.51)\
    Mon 2012-02-20 21:30:23 +0100
    * fix for\
      "relocation R\_X86\_64\_PC32 against \`handler\_index\_cond\_check' can not be used when making a shared object; recompile with -fPIC"
    * don't use visibility=hidden for external functions
  * [Revision #2502.513.50](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.513.50) \[merge]\
    Tue 2012-02-21 09:43:36 +0200
    * Automatic merge
    * [Revision #2502.527.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.527.4) \[merge]\
      Tue 2012-02-21 09:37:56 +0200
      * Automatic merge
      * [Revision #2502.528.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.4)\
        Tue 2012-02-21 09:35:46 +0200
        * Fixed wrong test case
    * [Revision #2502.527.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.527.3) \[merge]\
      Tue 2012-02-21 09:36:48 +0200
      * Automatic merge
      * [Revision #2502.528.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.3) \[merge]\
        Tue 2012-02-21 01:55:12 +0200
        * Merge with 5.1
        * [Revision #2502.352.75](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.352.75) \[merge]\
          Tue 2012-02-21 01:51:55 +0200
          * Automatic merge
          * [Revision #2502.529.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.529.1)\
            Tue 2012-02-21 01:44:50 +0200
            * More general handling of memory loss in dlclose (backported from 5.2)
            * Fixed supression in mysql-test-run so it also works on windows.
      * [Revision #2502.528.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.2) \[merge]\
        Tue 2012-02-21 01:49:14 +0200
        * Automatic merge
        * [Revision #2502.461.76](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.461.76)\
          Tue 2012-02-21 01:46:51 +0200
          * Added missing signal values to signal\_handler.cc
      * [Revision #2502.528.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.1) \[merge]\
        Mon 2012-02-20 18:46:22 +0100
        * merge
        * [Revision #2502.352.74](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.352.74)\
          Mon 2012-02-20 18:07:38 +0100
          * Fix compilation on Windows, and various Windows related mistakes introduced by\
            "safe exception patch".
          * Remove misleading comments suggesting about signal() Windows, the routine here\
            is part of a exception handler, and sig parameter is an exception code.
    * [Revision #2502.527.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.527.2) \[merge]\
      Tue 2012-02-21 01:58:50 +0200
      * Merge with [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md)
      * [Revision #2502.461.75](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.461.75) \[merge]\
        Mon 2012-02-20 17:58:00 +0200
        * Merge with 5.1
        * [Revision #2502.352.73](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.352.73)\
          Mon 2012-02-20 17:56:47 +0200
          * Fixed compiler warnings
      * [Revision #2502.461.74](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.461.74) \[merge]\
        Mon 2012-02-20 17:49:21 +0200
        * Merge with [MariaDB 5.1](../../old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) and MySQL 5.1.61
        * [Revision #2502.352.72](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.352.72) \[merge]\
          Mon 2012-02-20 16:23:18 +0200
          * Merge with MYSQL 5.1.61
          * Fixed README with link to source
          * Merged InnoDB change to XtraDB
        * [Revision #2502.352.71](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.352.71) \[
          * merge]\
            Sat 2012-02-11 16:42:46 +0100
          * merge
        * [Revision #2502.352.70](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.352.70)\
          Wed 2012-01-25 11:34:43 +0100
          * mtr runs only "big" tests, if `--big-test` is repeated twice
        * [Revision #2502.352.69](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.352.69)\
          Wed 2012-01-04 20:10:15 +0100
          * report innodb\_file\_per\_table, innodb\_flush\_log\_at\_trx\_commit, innodb\_flush\_method
      * [Revision #2502.461.73](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.461.73)\
        Mon 2012-02-20 14:03:44 +0200
        * Fixed [Bug #902654](https://bugs.launchpad.net/bugs/902654) "MariaDB consistently crashes in collect\_tables on Aria checkpoint execution"
        * This happend when you have more than 1024 open Aria tables during checkpoint.
      * [Revision #2502.461.72](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.461.72)\
        Thu 2012-02-16 16:06:49 -0800
        * Fixed [Bug #933117](https://bugs.launchpad.net/bugs/933117).
        * The bug was fixed with the code back-ported from the patch for [Bug #800184](https://bugs.launchpad.net/bugs/800184)
        * pushed into mariadb-5.3.
    * [Revision #2502.527.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.527.1)\
      Mon 2012-02-20 17:59:42 +0200
      * Fixed issue found by buildbot
  * [Revision #2502.513.49](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.513.49)\
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
  * [Revision #2502.513.48](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.513.48) \[merge]\
    Mon 2012-02-20 15:34:50 +0400
    * Merge
    * [Revision #2502.526.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.526.1)\
      Mon 2012-02-20 15:30:54 +0400
      * [Bug #933407](https://bugs.launchpad.net/bugs/933407): Valgrind warnings in mark\_as\_null\_row with materialization+semijoin, STRAIGHT\_JOIN, impossible WHERE
      * In return\_zero\_rows(), don't call mark\_as\_null\_row() for semi-join\
        materialized tables, because
        1. they may have been already freed, and
        2. there is no real need to call mark\_as\_null\_row() for them
  * [Revision #2502.513.47](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.513.47)\
    Sat 2012-02-18 19:11:57 -0800
    * Fixed [Bug #934348](https://bugs.launchpad.net/bugs/934348)
    * This bug is the result of an incomplete/inconsistent change introduced into\
      5.3 code when the cond\_equal parameter were added to the function optimize\_cond.
    * The change was made during a merge from 5.2 in October 2010.\
      The bug could affect only queries with HAVING.
  * [Revision #2502.513.46](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.513.46)\
    Sat 2012-02-18 16:06:38 -0800
    * Fixed [Bug #934342](https://bugs.launchpad.net/bugs/934342).
    * An outer join query with a semi-join subquery could return a wrong result\
      if the optimizer chose to materialize the subquery.
    * It happened because when substituting for the best field into a ref item\
      used to build access keys not all COND\_EQUAL objects that could be employed\
      at substitution were checked.
    * Also refined some code in the function check\_join\_cache\_usage to make it\
      safer.
  * [Revision #2502.513.45](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.513.45)\
    Fri 2012-02-17 13:27:41 +0100
    * Remove engine-specific (but identical) icp callbacks. create one reusable\
      common icp callback in the handler.cc.
    * It can also increment status counters, without making the engine\
      dependent on the exact THD layout (that is different in embedded).
  * [Revision #2502.513.44](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.513.44)\
    Thu 2012-02-16 20:13:28 -0800
    * Fixed LP bug #928352.
    * This bug led to wrong values of the use\_count fields in some SEL\_ARG\
      trees that triggered complains on the server side when executing the\
      test case for LP bug 800184 if a debug build of the server was used.
    * This was the result of the incomplete fix for bug 800184.
    * To complete it the following corrections had to be made:
      * the copy constructor for SEL\_TREE must call the new function incr\_refs\_all()\
        instead of the function incr\_refs(), because references to next key parts\
        from any SEL\_ARG tree belonging to the list of the first key part has to be\
        adjusted.
      * the method and\_sel\_tree of the class SEL\_IMERGE must use the copy constructor\
        of the SEL\_TREE class to make a copy of its second argument before it ANDs it\
        with any SEL\_TREE tree from the processed SEL\_IMERGE object.
  * [Revision #2502.513.43](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.513.43)\
    Thu 2012-02-16 20:15:57 +0400
    * Backport of:
      * timestamp: Thu 2011-12-01 15:12:10 +0100
      * Fix for Bug#13430436 PERFORMANCE DEGRADATION IN SYSBENCH ON INNODB DUE TO ICP
      * When running sysbench on InnoDB there is a performance degradation due\
        to index condition pushdown (ICP). Several of the queries in sysbench\
        have a WHERE condition that the optimizer uses for executing these\
        queries as range scans. The upper and lower limit of the range scan\
        will ensure that the WHERE condition is fulfilled. Still, the WHERE\
        condition is part of the queries' condition and if ICP is enabled the\
        condition will be pushed down to InnoDB as an index condition.
      * Due to the range scan's upper and lower limits ensure that the WHERE\
        condition is fulfilled, the pushed index condition will not filter out\
        any records. As a result the use of ICP for these queries results in a\
        performance overhead for sysbench. This overhead comes from using\
        resources for determining the part of the condition that can be pushed\
        down to InnoDB and overhead in InnoDB for executing the pushed index\
        condition.
      * With the default configuration for sysbench the range scans will use\
        the primary key. This is a clustered index in InnoDB. Using ICP on a\
        clustered index provides the lowest performance benefit since the\
        entire record is part of the clustered index and in InnoDB it has the\
        highest relative overhead for executing the pushed index condition.
      * The fix for removing the overhead ICP introduces when running sysbench\
        is to disable use of ICP when the index used by the query is a\
        clustered index.
      * When [WL#6061](https://askmonty.org/worklog/?tid=6061) is implemented this change should be re-evaluated.
  * [Revision #2502.513.42](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.513.42)\
    Thu 2012-02-16 18:56:10 +0400
    * Added comments
  * [Revision #2502.513.41](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.513.41)\
    Thu 2012-02-16 08:49:10 +0200
    * Counters for Index Condition Pushdown added ([MDEV-130](https://jira.mariadb.org/browse/MDEV-130)).
* [Revision #3275](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3275)\
  Fri 2012-02-17 12:19:38 +0100
  * fix the include guards and add missing gplv2 headers
* [Revision #3274](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3274)\
  Tue 2012-02-21 01:08:22 +0400
  * [Bug #919878](https://bugs.launchpad.net/bugs/919878): Assertion \`!eliminated\_tables...
    * In MySQL 5.5, print\_join() was re-worked to print "FROM dual" when all\
      tables are constant. This change didn't work together with table\
      elimination.
* [Revision #3273](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3273)\
  Mon 2012-02-20 22:25:44 +0100
  * Workaround buggy Linux dtrace - it fails on fedora if CC is set to 'ccache gcc'
* [Revision #3272](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3272) \[merge]\
  Wed 2012-02-15 19:11:16 +0100
  * merge
  * [Revision #3268.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3268.1.1) \[merge]\
    Wed 2012-02-15 18:08:08 +0100
    * 5.3.4 merge
* [Revision #3271](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3271)\
  Wed 2012-02-15 17:09:56 +0100
  * Fix wrong type causing build failure on windows.
* [Revision #3270](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3270)\
  Wed 2012-02-15 16:38:38 +0100
  * Fix wrong type causing build failure on windows.
* [Revision #3269](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3269) \[merge]\
  Wed 2012-02-15 15:37:38 +0100
  * Merge XtraDB from Percona-Server-5.5.20-24.1 into [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md).
  * [Revision #0.12.52](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.52)\
    Wed 2012-02-15 11:49:53 +0100
    * Updated with XtraDB from Percona Server 5.5.20-24.1
    * Files copied from Percona-Server-5.5.20-rel24.1.tar.gz source tarball.
* [Revision #3268](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3268) \[merge]\
  Tue 2012-02-14 16:06:41 +0100
  * Merge MySQL 5.5.20 into [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md).
* [Revision #3267](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3267)\
  Tue 2012-02-14 13:24:03 +0100
  * Fix wrong error code in the test case.
  * The replication slave sets first error 1913 and immediately after error

1595. Thus it is possible, but unlikely, to get 1913. The original test\
      seems to realise this, but uses an invalid error code - my guess is\
      that this was a temporary code used in a feature tree, which was then\
      forgotten to be fixed when merged to main. The removed "1923" is\
      something committed by mistake during tests.

* [Revision #3266](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3266)\
  Sat 2012-02-11 13:32:36 +0100
  * Fix _another_ race in test case rpl\_cant\_read\_event\_incident (seen in 5.5 Buildbot).
* [Revision #3265](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3265) \[merge]\
  Fri 2012-02-10 21:58:39 +0100
  * Merge fix for [Bug #910817](https://bugs.launchpad.net/bugs/910817): Race condition in kill\_threads\_for\_user().
* [Revision #3264](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3264)\
  Fri 2012-02-10 16:23:18 +0200
  * Fix set\_limit to be uniform with all calls.\
    Fix of set\_limit in case of an error (actually impossible case but better it will be right)
* [Revision #3263](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3263)\
  Thu 2012-02-09 13:10:47 +0100
  * Fix a number of problems in the test suite (no code bugs):
    * `mysql-test-run.pl --valgrind` complains when all tests succeed.
    * perfschema.all\_instances fail on non-linux, where ENABLE\_TEMP\_POOL\
      is not set and therefore BITMAP mutex is not used.
    * [MDEV-132](https://jira.mariadb.org/browse/MDEV-132): main.mysqldump fails because it depends on exact size of stdio\
      buffers.
    * [MDEV-99](https://jira.mariadb.org/browse/MDEV-99): rpl.rpl\_cant\_read\_event\_incident fails due to a race where the\
      slave manages to connect while the test case is in the middle of setting up\
      the master, causing the slave to replicate extra/wrong events.
    * [MDEV-133](https://jira.mariadb.org/browse/MDEV-133): rpl.rpl\_rotate\_purge\_deadlock fails because it issues a\
      DEBUG\_SYNC SIGNAL immediately followed by RESET; this means that sometimes\
      the intended receipient has no time to see the signal before it is cleared\
      by the RESET, causing wait to timeout.
* [Revision #3262](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3262)\
  Wed 2012-02-08 21:55:40 +0100
  * Fix memory leak when one +O debug on top of another.
* [Revision #3261](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3261)\
  Mon 2012-02-06 13:30:39 +0100
  * [MDEV-135](https://jira.mariadb.org/browse/MDEV-135): work-around a GCC bug seen on Debian 5 "lenny" 64-bit.
* [Revision #3260](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3260)\
  Fri 2012-02-03 21:15:08 +0100
  * Add SET\_TARGET\_PROPERTIES(ENABLE\_EXPORTS) for mysqltest so plugins.dialog\
    test passes.
* [Revision #3259](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3259) \[merge]\
  Fri 2012-02-03 17:02:02 +0100
  * merge
  * [Revision #3257.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3257.1.4)\
    Fri 2012-02-03 11:46:40 +0100
    * Various fixes for Solaris compiler.
    * Also, restrict symbol visibility in statically\
      built plugins, to minimize the chance for symbol\
      name clashes with dynamic plugins.
  * [Revision #3257.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3257.1.3)\
    Thu 2012-02-02 21:50:03 +0100
    * Cherry-picked fix for solaris compilation from 5.2
  * [Revision #3257.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3257.1.2)\
    Thu 2012-02-02 21:48:22 +0100
  * Fix portability problems
    * Solaris readline always needs curses
    * -rdynamic is not portable, replaced by SET\_TARGET\_PROPERTIES(...ENABLE\_EXPORTS)
  * [Revision #3257.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3257.1.1)\
    Thu 2012-02-02 21:12:49 +0100
    * [MDEV-100](https://jira.mariadb.org/browse/MDEV-100) : innodb\_plugin tests fail on Solaris.
    * The reason for the failure is that the loaded library has the same exported symbols\
      as the builtin one. So the plugin uses innodb functions e.g srv\_boot from mysqld\
      rather than plugin's own. This causes the crash.
    * On Unix systems with gcc4 later this error was so far worked around using GCC's\
      visibility attribute. However, in our case, we're using gcc3.
    * See related MySQL bug [bug.php?id=48524](https://bugs.mysql.com/bug.php?id=48524) and[bug.php?id=52263](https://bugs.mysql.com/bug.php?id=52263)
    * The fix is to restrict symbol visibility in the plugin using version script\
      (called map file on Solaris).
* [Revision #3258](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3258)\
  Fri 2012-02-03 10:31:39 +0100
  * make pam plugin to build in 5.5.\
    fix pam.tets for 5.5
* [Revision #3257](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3257)\
  Wed 2012-02-01 15:33:37 +0100
  * disable sys\_vars.innodb\_use\_sys\_malloc\_basic test for valgrind runs
* [Revision #3256](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3256)\
  Tue 2012-01-31 17:12:44 +0100
  * a couple of fixes for tests
* [Revision #3255](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3255)\
  Tue 2012-01-31 08:57:59 +0100
  * Fix .deb install failure when PBXT is not built-in.\
    Fix egrep syntax error in .deb preinst.
* [Revision #3254](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3254)\
  Mon 2012-01-30 17:12:22 +0200
  * remove building pbxt by default in any configuration (need explicit `./configure --with-pbxt-storage-engine` )
* [Revision #3253](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3253)\
  Sun 2012-01-29 11:33:00 +0100
  * Do not run PBXT tests by default. They have problems (valgrind failures,\
    huge space usage), and there is no upstream support anymore.
* [Revision #3252](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3252)\
  Sat 2012-01-28 21:22:14 +0100
  * Add INFO\_SRC and INFO\_BIN to .deb packaging to fix a test failure in\
    file\_contents.test. Also fix some old references to 5.3 in .deb packaging\
    found while debugging this.
* [Revision #3251](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3251)\
  Sat 2012-01-28 17:08:42 +0100
  * Fix debian patches for mysql-test-run wrt. deleted test account.
* [Revision #3250](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3250) \[merge]\
  Sat 2012-01-28 14:04:11 +0400
  * mergin.
  * [Revision #3248.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3248.1.1)\
    Sat 2012-01-28 11:05:47 +0100
    * Make perfschema.all\_instances work with OpenSSL, which has an extra rwlock\_instance.
* [Revision #3249](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3249)\
  Sat 2012-01-28 13:52:26 +0400
  * mdev57 5.5 main.file\_contents fails on debian5-i386-fulltest.
  * The line in the file\_contents.test removes all the '/lib' substrings from the\
    path, so file cannot be found if a path contains such a substring.\
    As i didn't find where it is needed, the line was just removed
  * per-file comments:
    * `mysql-test/t/file_contents.test`
  * mdev57 5.5 main.file\_contents fails on debian5-i386-fulltest.
    * no '/lib' substring cutting.
* [Revision #3248](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3248)\
  Fri 2012-01-27 15:13:38 +0100
  * Fix main.openssl\_1 failures for -DWITH\_SSL=system build.
  * In 5.5, ssl\_do() no longer calls report\_errors() in case of ssl error.\
    Since report\_errors() iterated over the list of errors, this means that we\
    now report the first error in the list, rather than the last. Adjust the`--replace_regex` line for OpenSSL build accordingly in the test case.
* [Revision #3247](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3247)\
  Fri 2012-01-27 12:14:41 +0100
  * Revert some earlier changes to my.cnf and mariadb.cnf.\
    I want to avoid that upgrades silently change important config parameters\
    that users have come to rely on. This could happen if users changed their\
    my.cnf themselves, and then an upgrade introduces mariadb.cnf which silently\
    overrides the settings in my.cnf. Avoid this by having mariadb.cnf mostly\
    empty for now, and in the future we can add just new mariadb-specific\
    options there that do not break existing installations.
* [Revision #3246](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3246)\
  Fri 2012-01-27 10:58:59 +0200
  * Fixed tests consumed big amount of disk space to be "BIG".
* [Revision #3245](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3245) \[merge]\
  Fri 2012-01-27 00:57:38 +0100
  * merge
  * [Revision #3243.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3243.1.1)\
    Fri 2012-01-27 00:37:10 +0100
    * fix result file
* [Revision #3244](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3244)\
  Thu 2012-01-26 20:07:25 +0100
  * fix embedded build
* [Revision #3243](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3243)\
  Thu 2012-01-26 17:10:30 +0100
  * yet another attempt to fix rpl\_corruption test
* [Revision #3242](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3242)\
  Thu 2012-01-26 16:55:40 +0100
  * Fix a few failing tests on win2008r2-vs2010-amd64-debug
* [Revision #3241](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3241)\
  Thu 2012-01-26 16:06:08 +0100
  * Xtradb recently started to access thd members directly ,e.g thd->stmt\_da (ha\_innodb.cc)\
    It needs recompilation for embedded server, as layout of THD is different in embedded.
* [Revision #3240](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3240)\
  Thu 2012-01-26 12:55:12 +0100
  * .deb packaging fixes: make mariadb-common a real package, which depends on\
    mysql-common and places mariadb-specific stuff in /etc/mysql/conf.d/mariadb.cnf.\
    This should allow to co-exist with default Debian mysql-common package and\
    help resolve dependencies when installing mariadb among multiple available\
    versions of MySQL from different repositories.
* [Revision #3239](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3239)\
  Thu 2012-01-26 13:38:42 +0100
  * Remove `--plugin-dir` option from mysql\_client\_test test case.\
    This gives the wrong path when testing installed server, and we\
    set the correct path in my.cnf anyway.
* [Revision #3238](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3238)\
  Wed 2012-01-25 21:23:14 +0100
  * Always define UT\_DBG\_ABORT in innodb/xtradb, also on Windows. This will avoid endless hangs inside ut\_dgb\_stop\_thread
* [Revision #3237](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3237)\
  Wed 2012-01-25 13:39:54 +0100
  * Add missing include and library files to libmariadbclient-dev package.
* [Revision #3236](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3236) \[merge]\
  Wed 2012-01-25 09:43:41 +0200
  * Automatic merge
  * [Revision #3234.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3234.1.1)\
    Tue 2012-01-24 18:07:35 +0200
    * Don't crash with: UPDATE performance\_schema.setup\_instruments SET ENABLED="NO";
    * Don't log updates to performance schema in replication log.
    * Ensure that we don't call ha\_update after ha\_index\_or\_rnd\_end() is called on slave.
* [Revision #3235](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3235)\
  Tue 2012-01-24 14:52:43 +0100
  * More 5.5 .deb packaging fixes
* [Revision #3234](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3234)\
  Tue 2012-01-24 12:27:44 +0100
  * More small 5.5 .deb packaging fixes found in Buildbot tests.
* [Revision #3233](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3233)\
  Tue 2012-01-24 10:47:57 +0100
  * Fix two .deb problems causing build/install failures in Buildbot.
* [Revision #3232](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3232)\
  Mon 2012-01-23 17:12:25 +0100
  * portability fixes for FreeBSD 8 and 9
* [Revision #3231](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3231)\
  Mon 2012-01-23 17:07:01 +0100
  * Fix typo in Ubuntu .deb packaging
* [Revision #3230](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3230)\
  Mon 2012-01-23 15:08:46 +0100
  * Buildbot VMs have cmake in /usr/local/, so we need to include that in the path.
* [Revision #3229](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3229)\
  Mon 2012-01-23 12:20:16 +0100
  * Initial draft for building .deb packages for [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md).
* [Revision #3228](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3228)\
  Fri 2012-01-20 22:32:31 +0100
  * Always compile my\_new.cc and safemalloc.c with mysys
    * Preprocessor macros USE\_MYSYS\_NEW and -DSAFEMALLOC are\
      used to conditionally compile safemalloc or overwritten new/delete.
    * Define dummy symbol in my\_new.cc in case -DUSE\_MYSYS\_NEW is not set.\
      This avoids compiler/linker warnings about an essentially empty file\
      being compiled.
* [Revision #3227](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3227)\
  Fri 2012-01-20 16:54:35 +0100
  * Fix embedded build on Windows.
* [Revision #3226](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3226)\
  Fri 2012-01-20 12:39:06 +0100
  * Remove debug output
* [Revision #3225](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3225)\
  Fri 2012-01-20 01:57:58 +0100
  * Fix rpl\_checksum test. Use basename of file in error messages, not the\
    ones prefixed with .\ or ./
    * Add my\_basename() to mysys.
    * Do not compile files that are not needed on Windows (my\_addr\_resolve, and\
      safemalloc related stuff it is not used)
    * Avoids linker warnings about compilation of essentially empty files.
* [Revision #3224](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3224)\
  Fri 2012-01-20 01:57:34 +0100
  * [MDEV-103](https://jira.mariadb.org/browse/MDEV-103): 'debug' is disabled in this build warnings causes tests to fail
  * The root cause is that after recent fixes around `--debug` variable ([Bug #909051](https://bugs.launchpad.net/bugs/909051))\
    the variable is now available in both release and debug builds, such that MTR\
    cannot tell a debug compiled server from optimized one.
  * To fix, assign a special default value 'disabled' for 'debug' variable in optimized build\
    and fix MTR to check for this special value to recognize optimized build.
* [Revision #3223](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3223)\
  Thu 2012-01-19 18:41:56 +0100
  * disable character\_sets\_dir\_basic - slashes vs backslashes problem is not possible to resolve
* [Revision #3222](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3222)\
  Thu 2012-01-19 17:44:22 +0100
  * fix broken result file
* [Revision #3221](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3221)\
  Thu 2012-01-19 17:31:07 +0100
  * Fix innodb\_bug60229 (get the innodb change into xtradb)
* [Revision #3220](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3220)\
  Thu 2012-01-19 14:12:16 +0100
  * update the test result
* [Revision #3219](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3219)\
  Wed 2012-01-18 22:09:20 +0100
  * fix the linking failure on windows
* [Revision #3218](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3218) \[merge]\
  Wed 2012-01-18 00:38:13 -0800
  * Merge
  * [Revision #3216.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3216.1.2)\
    Tue 2012-01-17 10:55:27 +0100
    * [MDEV-69](https://jira.mariadb.org/browse/MDEV-69) SET optimizer\_switch = REPLACE(...) causes ER\_WRONG\_VALUE\_FOR\_VAR
    * fixes bug(s): [Bug #912552](https://bugs.launchpad.net/bugs/912552) [MDEV-69](https://jira.mariadb.org/browse/MDEV-69)
    * find\_set() in typelib.c expected a zero-terminated string
  * [Revision #3216.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3216.1.1)\
    Tue 2012-01-17 09:11:20 +0100
    * fixes for non-debug builds (CMAKE\_BUILD\_TYPE=Release or RelWithDebInfo)
    * fixes bug(s): [Bug #907894](https://bugs.launchpad.net/bugs/907894)
* [Revision #3217](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3217)\
  Tue 2012-01-17 23:42:49 -0800
  * Fixed the failure of sp.test reported in the issue [MDEV-86](https://jira.mariadb.org/browse/MDEV-86).
* [Revision #3216](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3216) \[merge]\
  Mon 2012-01-16 21:13:05 +0100
  * merge
  * [Revision #3208.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3208.1.6)\
    Wed 2012-01-11 13:35:27 +0100
    * [MDEV-85](https://jira.mariadb.org/browse/MDEV-85): Remove shared plugin library if build swtiches from shared to static with
    * e.g
      * cmake . -DWITH\_XXXX\_STORAGE\_ENGINE=1
  * [Revision #3208.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3208.1.5)\
    Wed 2012-01-11 10:26:35 +0200
    * fix for 64bit windows
    * fix misleading test name
  * [Revision #3208.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3208.1.4)\
    Tue 2012-01-10 01:11:36 +0100
    * [MDEV-33](https://jira.mariadb.org/browse/MDEV-33) : removed unused files in win/
  * [Revision #3208.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3208.1.3)\
    Mon 2012-01-09 21:15:34 +0100
    * Force bundled readline/libedit build as static library.
    * Packagers may attempt to outsmart MariaDB/MySQL build system -DBUILD\_SHARED\_LIBS=1, we need to minimize the damage of such attempts.
  * [Revision #3208.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3208.1.2)\
    Mon 2012-01-09 21:12:09 +0100
    * [MDEV-63](https://jira.mariadb.org/browse/MDEV-63) - attempt to fix the warning exclusion
  * [Revision #3208.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3208.1.1)\
    Mon 2012-01-09 15:02:02 +0200
    * Fix sys\_vars test suite for 32bit systems. ([MDEV-53](https://jira.mariadb.org/browse/MDEV-53) & [MDEV-53](https://jira.mariadb.org/browse/MDEV-53))
* [Revision #3215](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3215)\
  Mon 2012-01-16 21:06:44 +0100
  * remove unused flag
* [Revision #3214](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3214)\
  Mon 2012-01-16 21:06:23 +0100
  * query cache sysvar fixes
* [Revision #3213](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3213)\
  Mon 2012-01-16 21:02:43 +0100
  * enable test cases for bugs fixed in xtradb.
  * disable test cases for bugs not fixed in xtradb.
* [Revision #3212](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3212)\
  Mon 2012-01-16 20:58:00 +0100
  * minor mtr fix
* [Revision #3211](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3211) \[merge]\
  Mon 2012-01-16 20:16:35 +0100
  * mysql-5.5 merge
* [Revision #3210](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3210)\
  Fri 2012-01-13 15:52:19 +0100
  * remove duplicate .opt with AUTH\_PLUGIN\_SO
* [Revision #3209](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3209) \[merge]\
  Fri 2012-01-13 15:50:02 +0100
  * 5.3 merge
  * [Revision #2502.1.881](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.1.881)\
    Fri 2012-01-13 13:54:55 +0100
    * multi-delete should ignore semi-join internal temp tables,\
      when looking for tables to delete from
  * [Revision #2502.1.880](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.1.880) \[merge]\
    Thu 2012-01-12 20:23:02 +0100
    * [Bug #893522](https://bugs.launchpad.net/bugs/893522) more problems found by PVS Studio
* [Revision #3208](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3208)\
  Sat 2012-01-07 20:01:55 +0100
  * [MDEV-76](https://jira.mariadb.org/browse/MDEV-76) 5.5 memory overrun on main.select\_jcl6.
  * geometry fields are blobs too.
* [Revision #3207](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3207)\
  Fri 2012-01-06 18:35:08 +0100
  * moved ha\_maria::implicit\_commit() calls around
* [Revision #3206](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3206)\
  Thu 2012-01-05 18:57:13 +0100
  * valgrind suppression for older glibc
* [Revision #3205](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3205)\
  Thu 2012-01-05 18:56:31 +0100
  * fixes for opensolaris compilation failures
* [Revision #3204](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3204)\
  Fri 2012-01-06 13:07:20 +0100
  * Fix some failing tests on Windows
    * ensure that mtr supressions table is flushed before doing controlled crash and restart
    * use DBUG\_SUICIDE() rather than abort() in partition tests - avoids a crash message/warning
    * disable perfschema all\_instances test on Windows- there are legitimate\
      reasons for output to be different on Unix (some different threads, some\
      different locks), the differences are expected to grow in the future, e.g\
      with threadpool.
* [Revision #3203](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3203)\
  Thu 2012-01-05 00:02:57 +0100
  * updated results for big tests
* [Revision #3202](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3202)\
  Tue 2012-01-03 00:17:36 +0100
  * Fix compile error
* [Revision #3201](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3201)\
  Mon 2012-01-02 21:56:16 +0100
  * Fix compile warnings
* [Revision #3200](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3200)\
  Mon 2012-01-02 21:31:17 +0100
  * Fix buildbot: update test results (2)
* [Revision #3199](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3199)\
  Mon 2012-01-02 21:20:35 +0100
  * Fix buildbot: update test results
* [Revision #3198](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3198)\
  Fri 2011-12-30 11:22:27 +0100
  * Fix failing tests in the main suite
* [Revision #3197](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3197)\
  Fri 2011-12-30 11:21:39 +0100
  * Fix oqgraph so it can be built on Window as well.
  * Note: to build with -fno-rtti as we currently build the server, boost version 1.45 or later is required.\
    (without -fno-rtti, 1.40 is enough)
* [Revision #3196](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3196)\
  Wed 2011-12-28 23:20:39 +0100
  * Correct search path for plugins, in out-of-source build
* [Revision #3195](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3195)\
  Wed 2011-12-28 22:47:27 +0100
  * Fix oqgraph build . Plugin does not need rtti, and does not load if rtti compile settings are different from server's
* [Revision #3194](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3194)\
  Tue 2011-12-27 20:54:29 +0100
  * Fix compile error
* [Revision #3193](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3193)\
  Tue 2011-12-27 20:59:05 +0200
  * Added ignore of generated file
* [Revision #3192](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3192)\
  Tue 2011-12-27 20:55:21 +0200
  * Fixed [Bug #909051](https://bugs.launchpad.net/bugs/909051) Options `--debug` and `--disable-debug` are known but ambiguous in RelWithDebInfo build
  * Fixed memory leak printing when doing `'mysqld --version'`, `'mysqld --debug --help'` and `'mysqld --debug --help --verbose'`
* [Revision #3191](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3191)\
  Tue 2011-12-27 17:44:14 +0100
  * Fix RQG in 5.5, make mtr MTR\_VERSION=1 functional.\
    Patch by elenst
* [Revision #3190](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3190)\
  Tue 2011-12-27 01:14:54 +0100
  * Fix [Bug #886378](https://bugs.launchpad.net/bugs/886378) : allow chain certificate files to work.
  * Contributed by Maarten Vanraes (AL13N)
  * Fix things so that chains of certificates work in the server and client\
    certificate files.
  * This only really works for OpenSSL-based builds, as yassl is unable to read\
    multiple certificates from a file. The patch below to yassl/src/ssl.cpp\
    doesn't fix that, but just arranges that the viosslfactories.c patch won't\
    have any ill effects in a yassl build.
* [Revision #3189](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3189)\
  Tue 2011-12-27 00:39:34 +0100
  * [Bug #886526](https://bugs.launchpad.net/bugs/886526): Add propoer shebang to scripts
* [Revision #3188](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3188)\
  Mon 2011-12-26 15:24:54 +0100
  * use ADD\_CONVENIENCE\_LIBRARY when building libservices, because\
    it is a static library that links with shared libraries, so strictly speaking it should\
    have -fPIC or equivalent flags. Also, it must always build as static no matter\
    whether BUILD\_SHARED\_LIBS is set.
* [Revision #3187](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3187)\
  Wed 2011-12-21 23:40:26 +0100
  * keycache sysvars used to pass incorrect offset into the parent constructor,\
    that caused the default value to be written into an arbitrary location inside\
    global\_system\_variables
* [Revision #3186](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3186)\
  Wed 2011-12-21 02:44:50 +0100
  * fix 64 bit Windows build
* [Revision #3185](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3185)\
  Fri 2011-12-16 14:13:27 +0100
  * Restore some fixes for slow xtradb shutdown that were lost in the 5.5 merge.
* [Revision #3184](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3184)\
  Thu 2011-12-15 22:08:42 +0100
  * remove WITH\_DEBUG from CMakeLists.txt
  * MYSQL\_MAINTAINER\_MODE and SAFEMALLOC take values ON/OFF/AUTO
  * (in all builds, in none, only in debug and platform dependent)
  * `./configure` prefers RelWithDebInfo unless the user overrides
* [Revision #3183](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3183)\
  Thu 2011-12-15 22:07:58 +0100
  * rename debug variable to debug\_dbug, to make test pass in release builds\
    (and to follow the naming conventons).\
    keep old debug variable, but mark it as deprecated.
* [Revision #3182](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3182)\
  Thu 2011-12-15 19:28:38 +0100
  * always use sql/sql\_string.\* files, never - client/sql\_string.\*
* [Revision #3181](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3181)\
  Thu 2011-12-15 16:00:07 +0100
  * Fix XtraDB build on windows (avoid #ifdef inside macro invocation).
* [Revision #3180](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3180) \[merge]\
  Thu 2011-12-15 10:35:11 +0100
  * Merge missing file from XtraDB
  * [Revision #0.12.51](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.51)\
    Thu 2011-12-15 10:34:39 +0100
    * Add file accidentally omitted in last commit
* [Revision #3179](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3179) \[merge]\
  Thu 2011-12-15 10:34:14 +0100
  * Merge XtraDB from Percona-server-5.5.17-rel22.1 into [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)
  * [Revision #0.12.50](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.50)\
    Wed 2011-12-14 14:58:22 +0100
    * Updated with XtraDB from Percona Server 5.5.17-rel22.1
    * Files copied from Percona-Server-5.5.17-rel22.1.tar.gz source tarball.
* [Revision #3178](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3178)\
  Wed 2011-12-14 12:02:03 +0100
  * After-merge fixes for 5.5 merge.
    * Fix typo causing too low timeout value for wait\_for\_slave\_param.inc.
    * Fix binlog checksums following 5.5 merge.
    * Make sure the rpl suite can run with `--mysqld=--binlog-checksum=CRC32`
    * Fix a number of problems in the code when checksums are enabled.
* [Revision #3177](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3177)\
  Wed 2011-12-14 10:59:24 +0100
  * fix new String:realloc\* variants always to zero-terminate the string
* [Revision #3176](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3176)\
  Wed 2011-12-14 10:59:11 +0100
  * new valgrind suppression for ld.so\
    give mysqld more time to start under valgrind
* [Revision #3175](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3175)\
  Wed 2011-12-14 10:53:32 +0100
  * new configure option: NOT\_FOR\_DISTRIBUTION\
    fix safemalloc to compile w/o libbfd.
* [Revision #3174](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3174)\
  Tue 2011-12-13 11:07:55 +0100
  * bugfix: cxxabi.h was not found
* [Revision #3173](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3173)\
  Mon 2011-12-12 23:58:40 +0100
  * after merge changes:
    * rename all debugging related command-line options\
      and variables to start from "debug-", and made them all\
      OFF by default.
    * replace "MySQL" with "MariaDB" in error messages
    * "Cast ... converted ... integer to it's ... complement"\
      is now a note, not a warning
    * @@query\_cache\_strip\_comments now has a session scope,\
      not global.
* [Revision #3172](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3172)\
  Mon 2011-12-12 22:58:24 +0100
  * move safemalloc out of dbug.\
    remeber a real backtrace for every allocation.\
    make safemalloc to tract C++ new/delete too.\
    collateral fixes to make the test suite pass.
* [Revision #3171](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3171)\
  Sun 2011-12-11 09:00:12 +0100
  * another backtrace resolver that prints source file name and line number
* [Revision #3170](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3170)\
  Fri 2011-12-02 19:49:05 +0100
  * win64 sysvar portability fixes
* [Revision #3169](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3169)\
  Thu 2011-12-08 18:08:48 +0100
  * Fix valgrind error after 5.5 merge (the 5.3 fix was accidentally lost in the merge).
* [Revision #3168](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3168)\
  Mon 2011-12-05 13:17:54 +0100
  * Fix crash due to wrong my\_error() call (5.5 after-merge fix).
* [Revision #3167](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3167)\
  Fri 2011-12-02 16:29:02 +0100
  * install my\_valgrind.h too
* [Revision #3166](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3166)\
  Fri 2011-12-02 15:35:05 +0100
  * Fixed crashes found by application verifier:
    * leaking mutex in lf\_hash\_destroy
    * pthread\_getspecific() before pthread\_key\_create() in my\_thread\_var\_dbug()\
      (called by static C++ object constructors called in sys\_vars)
    * perfschema destroys mutexes that were not created.
* [Revision #3165](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3165)\
  Fri 2011-12-02 14:38:05 +0100
  * fix failing test cases in 5.5 main suite
* [Revision #3164](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3164)\
  Fri 2011-12-02 14:35:26 +0100
  * Make it possible to compile without SAFEMALLOC in debug builds\
    Default to no SAFEMALLOC on Windows, because C runtime malloc\
    has this functionslity already
* [Revision #3163](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3163)\
  Wed 2011-11-30 00:26:32 +0100
  * Fix Aria unit tests on Windows.
  * Replace statements connected with bitwise OR with series of "if"s.
  * The later is guaranteed to execute in order, bitwise OR does not have\
    specific order for statement execution.
* [Revision #3162](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3162)\
  Wed 2011-11-30 00:23:50 +0100
  * fix signing and packaging
* [Revision #3161](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3161)\
  Mon 2011-11-28 23:15:12 +0100
  * small cleanup
* [Revision #3160](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3160)\
  Mon 2011-11-28 18:20:51 +0100
  * by default disable pbxt too
* [Revision #3159](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3159)\
  Mon 2011-11-28 17:48:19 +0100
  * consistency fixes for `mysqld --help`
* [Revision #3158](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3158)\
  Mon 2011-11-28 17:45:17 +0100
  * compilation failure on Solaris
* [Revision #3157](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3157) \[merge]\
  Mon 2011-11-28 13:50:00 +0100
  * merge
  * [Revision #3152.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3152.1.6) \[
    * merge]\
      Mon 2011-11-28 01:23:13 +0100
    * merge
  * [Revision #3152.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3152.1.5)\
    Sat 2011-11-26 23:08:46 +0100
    * Fix MariaDB wasnings on Windows (rmdir not defined unless direct.h is included)
  * [Revision #3152.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3152.1.4)\
    Sat 2011-11-26 23:07:53 +0100
    * Fix build and packaging on Windows:
      * build executables we have in 5.3 (mysql\_install\_db.exe, mysq\_upgrade\_service.exe, upgrade wizard), and MSI
      * add some missing headers to windows specific source files.\
        This needs to be done since 5.5 is using WIN32\_LEAN\_AND\_MEAN preprocessor constant thus windows.h\
        no more includes whiole Windows
      * do not deliver perl scripts (mysql\_install\_db.pl & friends) -they do not work, are not documented, and we\
        have native executables for this functionality. do not pack echo.exe, replace.exe into MSI, they\
        are not needed. Do not build resolveip on Windows, it is not used.
      * precache results of system checks in cmake/os/WindowsCache.cmake (like it is alreay done for majority of tests\
        to speed up cmake run with VS)
      * make feedback plugin DEFAULT on Windows (so MSI works if user enables plugin),\
        fix null pointer access in PSI\_register
* [Revision #3156](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3156) \[merge]\
  Sun 2011-11-27 17:50:50 +0100
  * merged
  * [Revision #3152.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3152.1.3)\
    Fri 2011-11-25 20:50:14 +0100
    * Avoid mysqld dependency on libaio.so by linking xtradb statically to libaio.
      * A variable XTRADB\_PREFER\_STATIC\_LIBAIO should be set to 1 (or TRUE\
        or ON) for static linking.
      * Even if mysqld can avoid dependency on shared libaio, shared libraries\
        libmysqld.so or ha\_innodb.so cannot link without it.
      * Given that the patch primarily addresses building tar.gz package, and\
        shared libraries mentioned above deemed less important than mysqld\
        executable, we accept shared lib dependency on libaio.so
  * [Revision #3152.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3152.1.2)\
    Wed 2011-11-23 19:29:39 +0100
    * fix linking on Windows (iphlpapi missing)
  * [Revision #3152.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3152.1.1)\
    Wed 2011-11-23 19:02:08 +0100
    * Fix package names, by removing a trailing "-MariaDB" ,as we already have leading "mariadb-".
    * Hardcode -MariaDB suffix for MYSQL\_SERVER\_VERSION in mysql\_version.h
* [Revision #3155](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3155)\
  Sun 2011-11-27 17:50:08 +0100
  * compilation fixes
* [Revision #3154](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3154) \[merge]\
  Sun 2011-11-27 17:46:20 +0100
  * 5.3->5.5 merge
* [Revision #3153](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3153)\
  Wed 2011-11-23 18:25:07 +0100
  * compiler warnings/errors
* [Revision #3152](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3152) \[merge]\
  Tue 2011-11-22 18:51:33 +0100
  * merged
  * [Revision #3142.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3142.1.5)\
    Tue 2011-11-22 18:05:34 +0100
    * Add support for signed sysvars.
    * Make max\_user\_connections signed, with min allowed value being -1.
  * [Revision #3142.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3142.1.4) \[merge]\
    Tue 2011-11-22 18:04:38 +0100
    * 5.3->5.5 merge
  * [Revision #3142.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3142.1.3)\
    Thu 2011-11-03 23:48:42 +0100
    * few cmake/compiler warnings
  * [Revision #3142.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3142.1.2) \[
    * merge]\
      Thu 2011-11-03 23:39:53 +0100
    * merge
  * [Revision #3142.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3142.1.1) \[merge]\
    Thu 2011-11-03 19:17:05 +0100
    * mysql-5.5.18 merge
* [Revision #3151](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3151)\
  Tue 2011-11-08 02:14:57 +0100
  * For libmysqld.so, apply patch to the MySQL Bug#39288 found here[102373](https://lists.mysql.com/commits/102373)
  * It is better than previous attempts to build the libmysqld,\
    as it also takes care of
    1. `-Wl`,`--no-undefined` for shared libraries and
    2. `CLEAN_DIRECT_OUTPUT` since there are now 2 libraries with\
       the same base output name
* [Revision #3150](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3150)\
  Mon 2011-11-07 22:20:44 +0100
  * add version to the libmysqld.so
* [Revision #3149](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3149)\
  Mon 2011-11-07 19:26:36 +0100
  * Fix unresolved symbols in libmysqld.so
* [Revision #3148](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3148)\
  Wed 2011-11-02 16:30:52 +0100
  * Build libmysqld.so also on non-windows.
* [Revision #3147](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3147)\
  Wed 2011-11-02 14:10:09 +0100
  * Revert wrong change.
* [Revision #3146](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3146)\
  Tue 2011-10-25 12:53:40 +0200
  * Some after-merge fixes for 5.5 merge.
* [Revision #3145](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3145)\
  Wed 2011-11-02 12:55:46 +0100
  * compilation warnings on Windows
* [Revision #3144](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3144)\
  Wed 2011-11-02 12:26:30 +0100
  * build on windows
* [Revision #3143](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3143)\
  Mon 2011-10-31 17:25:29 +0100
  * On linux we build with defined \_GNU\_SOURCE.
  * We must perform system tests with \_GNU\_SOURCE too!
* [Revision #3142](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3142)\
  Sat 2011-10-29 20:40:03 +0200
  * fix the build and compiler warnings (few of which were real bugs)\
    for "cmake ." builds
* [Revision #3141](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3141)\
  Fri 2011-10-28 20:30:42 +0200
  * fix embedded tests.\
    temporarily disable pbxt in embedded
* [Revision #3140](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3140)\
  Fri 2011-10-28 17:25:20 +0200
  * ignore troff failures - they are not fatal
* [Revision #3139](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3139)\
  Fri 2011-10-28 14:24:02 +0200
  * fixes for sys\_vars and pbxt suites
* [Revision #3138](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3138) \[merge]\
  Thu 2011-10-27 00:31:44 +0400
  * Merge: post-merge fixes
  * [Revision #3136.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3136.1.1)\
    Thu 2011-10-27 00:23:48 +0400
    * Post-merge fixes: Fix problems in table\_elim.test and enable it.
* [Revision #3137](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3137)\
  Wed 2011-10-26 15:24:07 +0300
  * Fixed that oqgraph and libmysqld/examples compiles on OpenSuse 11.4
* [Revision #3136](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3136)\
  Tue 2011-10-25 01:12:16 +0200
  * Fix debug build on Windows.
    * Checking for WITH\_DEBUG does not work, as described in CMake MySQL wiki[CMake#Debug-only\_options](https://forge.mysql.com/wiki/CMake#Debug-only_options)
    * Excluding directory completely for certain build types works for Makefiles only, but not for Visual Studio and not for Xcode.
* [Revision #3135](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3135)\
  Mon 2011-10-24 15:22:17 +0400
  * Post-merge fixes:
    * Fix derived\_view.test to work, and enable it
    * Let subselect\*.test do "DROP TABLE IF EXISTS" before they attempt to create the table.
* [Revision #3134](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3134)\
  Sat 2011-10-22 09:40:45 +0200
  * embedded tests
* [Revision #3133](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3133)\
  Sat 2011-10-22 01:07:39 +0200
  * Sergey Petrunya fixes for subselect\* tests,\
    and other misc test fixes
* [Revision #3132](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3132)\
  Fri 2011-10-21 23:07:13 +0200
  * fixes for windows
* [Revision #3131](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3131)\
  Wed 2011-10-19 23:01:15 +0200
  * post-merge changes to the mysql-test suite
* [Revision #3130](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3130)\
  Wed 2011-10-19 22:56:23 +0200
  * bugfix: query cache was using incorrect wait flag
* [Revision #3129](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3129)\
  Wed 2011-10-19 22:55:43 +0200
  * bugfix: progress reporting and sub-statements
  * (a stored function or TRIGGER, that runs LOAD DATA, which, itself,\
    invokes another trigger, that also does LOAD DATA, etc).
* [Revision #3128](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3128)\
  Wed 2011-10-19 22:52:43 +0200
  * don't forget to call ha\_index\_end before destroying the handler
* [Revision #3127](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3127)\
  Wed 2011-10-19 22:52:01 +0200
  * with introduction of progress reporting, max error number is 65534
* [Revision #3126](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3126)\
  Wed 2011-10-19 22:51:24 +0200
  * bugfix: delay\_key\_write=ALL cannot be turned off
* [Revision #3125](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3125)\
  Wed 2011-10-19 22:50:45 +0200
  * cleanups
* [Revision #3124](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3124)\
  Wed 2011-10-19 22:48:48 +0200
  * intptr should be unsigned
* [Revision #3123](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3123)\
  Wed 2011-10-19 22:48:23 +0200
  * cmake 2.6 compat
* [Revision #3122](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3122)\
  Wed 2011-10-19 21:53:14 +0200
  * safe\_mutex deadlock detector post-merge fixes
* [Revision #3121](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3121)\
  Wed 2011-10-19 21:51:08 +0200
  * Id column in EXPLAIN can be null.
* [Revision #3120](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3120) \[merge]\
  Wed 2011-10-19 21:45:18 +0200
  * merge with 5.3
* [Revision #3119](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3119) \[merge]\
  Mon 2011-07-18 23:04:24 +0200
  * merge with xtradb-5.5.15\
    fix test cases
  * [Revision #0.12.49](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.49)\
    Sun 2011-07-17 11:28:48 +0200
    * applied percona patches to InnoDB as of 5.5.15
  * [Revision #0.12.48](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.48)\
    Sat 2011-07-16 18:03:08 +0200
    * renames
  * [Revision #0.12.47](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.47)\
    Thu 2011-07-14 21:22:41 +0200
    * xtradb 5.5.13
* [Revision #3118](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3118)\
  Sat 2011-07-16 17:58:45 +0200
  * more pbxt suite fixes
* [Revision #3117](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3117)\
  Sat 2011-07-16 09:59:15 +0200
  * move ctest handling from mtr to a separate suite
* [Revision #3116](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3116)\
  Sat 2011-07-16 09:59:04 +0200
  * skipped tests: improve skip messages, move to a proper suite, disable as needed
* [Revision #3115](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3115)\
  Sat 2011-07-16 09:09:01 +0200
  * unit test fixes for ctest
* [Revision #3114](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3114)\
  Sat 2011-07-16 09:07:41 +0200
  * compilation fixes: without dbug, without ssl
* [Revision #3113](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3113)\
  Fri 2011-07-15 09:09:33 +0200
  * maria suite ok
* [Revision #3112](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3112)\
  Thu 2011-07-14 18:25:05 +0200
  * fixing pbxt and oqgraph suites
* [Revision #3111](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3111)\
  Thu 2011-07-14 18:24:01 +0200
  * less boilerplate code - move common operations to wrappers
* [Revision #3110](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3110)\
  Wed 2011-07-13 21:10:18 +0200
  * use PSI wrappers in aria and other non-MySQL code
* [Revision #3109](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3109)\
  Tue 2011-07-12 17:41:13 +0200
  * fix misplaced and non-working if() in the grammar\
    few small post-merge fixes
* [Revision #3108](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3108)\
  Tue 2011-07-12 14:34:47 +0200
  * move authentication\_windows\_client and mysql\_clear\_password clear client auth plugins\
    out of libmysql into separate dynamic plugins in the plugin/ directory.
  * move dialog and auth\_socket plugins out of the plugin directory with examples into\
    dedicated directories in plugin/
* [Revision #3107](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3107)\
  Tue 2011-07-12 13:12:07 +0200\
  \*
  * build dbug manual and unit tests
* document safemalloc
* [Revision #3106](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3106)\
  Mon 2011-07-11 20:33:39 +0200
  * sys\_vars changes and cleanups
* [Revision #3105](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3105)\
  Sun 2011-07-10 20:21:18 +0200
  * adding DBUG\_ENTER/DBUG\_RETURN tags that were useful when fixing memory leaks
* [Revision #3104](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3104)\
  Sun 2011-07-10 20:09:17 +0200
  * fix memory leaks and other problems found by safemalloc
* [Revision #3103](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3103)\
  Sun 2011-07-10 19:55:54 +0200
  * add safemalloc back
  * ... but differently
* [Revision #3102](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3102)\
  Sun 2011-07-10 19:50:29 +0200
  * small dbug cleanup
* [Revision #3101](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3101)\
  Sun 2011-07-10 19:49:28 +0200
  * remove remnants of safemalloc and\
    very old halloca() support
* [Revision #3100](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3100)\
  Sun 2011-07-10 19:47:24 +0200
  * only allocate extra-port (in tests) when needed\
    (otherwise 10 ports per worker will be not enough)
* [Revision #3099](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3099)\
  Sun 2011-07-10 17:53:06 +0200
  * update .bzrignore
* [Revision #3098](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3098)\
  Mon 2011-07-04 10:42:17 +0200
  * utf8\_croatian\_ci my\_like\_range tests
* [Revision #3097](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3097)\
  Sun 2011-07-03 20:07:41 +0200
  * remove unused autotools files
* [Revision #3096](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3096)\
  Sun 2011-07-03 20:00:14 +0200
  * Bug#25679
  * Ensure that we do not hold the LOCK\_open mutex while attempting\
    to establish FederatedX connection to guard against a trivial\
    Denial of Service scenario.
* [Revision #3095](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3095)\
  Sat 2011-07-02 22:12:12 +0200
  * post-merge fixes.\
    most tests pass.\
    5.3 merge is next
* [Revision #3094](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3094) \[merge]\
  Sat 2011-07-02 22:08:51 +0200
  * 5.5-merge
* [Revision #3093](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3093)\
  Mon 2011-04-25 17:22:25 +0200
  * lots of post-merge changes
* [Revision #3092](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3092)\
  Fri 2010-11-26 12:22:40 +0100
  * updated sys\_vars.cc (converting 5.3 mysqld.cc and set\_var.cc\
    changes appropriately)
* [Revision #3091](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3091) \[merge]\
  Thu 2010-11-25 18:17:28 +0100
  * merge.\
    checkpoint.\
    does not compile.
* [Revision #3090](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3090)\
  Fri 2010-11-05 12:11:29 +0100
  * test result updated to match \[incorrect] mysql result.
  * [MySQL Bug #58011](https://bugs.mysql.com/bug.php?id=58011)
* [Revision #3089](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3089) \[merge]\
  Fri 2010-11-05 10:59:51 +0100
  * mysql-5.1 -> mysql-5.5 merge

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
