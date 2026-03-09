# MariaDB 5.3.3 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.3.3) |[Release Notes](../../old-releases/5.3/5.3.3.md) |**Changelog** |[Overview of 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md)

**Release date:** 21 Dec 2011

For the highlights of this release, see the [release notes](../../old-releases/5.3/5.3.3.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3367](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3367)\
  Tue 2011-12-20 12:13:47 +0400
  * Fix version number: it's 5.3.3
* [Revision #3366](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3366)\
  Tue 2011-12-20 09:57:42 +0400
  * Update mysql-test/suite/pbxt/r/subselect.result for the previous push
* [Revision #3365](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3365)\
  Mon 2011-12-19 23:05:44 +0200
  * Backport of [MySQL Worklog #5953](https://dev.mysql.com/worklog/task/?id=5953) from MySQL 5.6
  * The patch differs from the original MySQL patch as follows:
    * All test case differences have been reviewed one by one, and\
      care has been taken to restore the original plan so that each\
      test case executes the code path it was designed for.
    * A bug was found and fixed in [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md) in\
      Item\_allany\_subselect::cleanup().
    * ORDER BY is not removed because we are unsure of all effects,\
      and it would prevent enabling ORDER BY ... LIMIT subqueries.
    * ref\_pointer\_array.m\_size is not adjusted because we don't do\
      array bounds checking, and because it looks risky.
  * Original comment by Jorgen Loland:
    * [MySQL Worklog #5953](https://dev.mysql.com/worklog/task/?id=5953) - Optimize away useless subquery clauses
    * For IN/ALL/ANY/SOME/EXISTS subqueries, the following clauses are\
      meaningless:
      * ORDER BY (since we don't support LIMIT in these subqueries)
      * DISTINCT
      * GROUP BY if there is no HAVING clause and no aggregate\
        functions
    * This WL detects and optimizes away these useless parts of the\
      query during JOIN::prepare()
* [Revision #3364](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3364)\
  Mon 2011-12-19 22:24:10 +0400
  * [Bug #906385](https://bugs.launchpad.net/bugs/906385): EXPLAIN EXTENDED crashes in TABLE\_LIST::print with limited max\_join\_size
    * Take into account that subquery's optimization can fail because of @@max\_join\_size error.
* [Revision #3363](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3363)\
  Mon 2011-12-19 20:58:55 +0400
  * [Bug #904432](https://bugs.launchpad.net/bugs/904432): Wrong result with LEFT JOIN, constant table, semijoin=ON,materialization=ON
    * Correct handling for SJ-Materialization + outer joins (details in the comments in the code)
* [Revision #3362](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3362)\
  Mon 2011-12-19 18:07:19 +0400
  * Remove garbage comments
* [Revision #3361](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3361)\
  Mon 2011-12-19 10:11:21 +0200
  * Supression condition made wider to cover some other system cases.
* [Revision #3360](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3360)\
  Sun 2011-12-18 23:38:37 -0800
  * Fixed [Bug #904832](https://bugs.launchpad.net/bugs/904832).
  * Do not perform index condition pushdown for conditions containing subqueries\
    and stored functions.
* [Revision #3359](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3359)\
  Sun 2011-12-18 19:25:00 +0400
  * Bump version number: now it's 5.3.3 (5.3.2 has been released some time ago)
* [Revision #3358](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3358)\
  Fri 2011-12-16 08:05:14 -0800
  * Adjusted test cases of the suite funcs\_1.
* [Revision #3357](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3357)\
  Fri 2011-12-16 14:19:58 +0400
  * Update test results for previous push
* [Revision #3356](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3356)\
  Fri 2011-12-16 10:21:46 +0400
  * GIS issues fixed.
  * Failures on SUN Solaris. Buggy compiler there required some extra initialization\
    for variables. Then the 02 optimization leads to bugs when values set through the\
    pointer are not always taken into account. Finally, the (long long) / (long)\
    crashes there, the explicit typeconverstion added.\
    Failing innodb\_plunin.innodb\_gis.test fixed.
  * per-file comments:
    * mysql-test/suite/innodb\_plugin/t/innodb\_gis.test
      * GIS issues fixed.
    * sql/gcalc\_slicescan.cc
      * GIS issues fixed.
    * sql/gcalc\_tools.cc
      * GIS issues fixed.
* [Revision #3355](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3355) \[merge]\
  Thu 2011-12-15 15:55:00 -0800
  * Merge
  * [Revision #3353.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3353.1.1) \[merge]\
    Thu 2011-12-15 14:28:34 -0800
    * Merge.
    * [Revision #3349.2.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3349.2.2)\
      Thu 2011-12-15 14:26:59 -0800
      * Made join\_cache\_level == 2 by default.
    * [Revision #3349.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3349.2.1)\
      Thu 2011-12-15 00:21:15 -0800
      * Made the optimizer switch flags 'outer\_join\_with\_cache', 'semijoin\_with\_cache'\
        set to 'on' by default.
* [Revision #3354](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3354) \[merge]\
  Fri 2011-12-16 03:46:04 +0400
  * Merge
  * [Revision #3349.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3349.1.2)\
    Fri 2011-12-16 03:44:25 +0400
    * [Bug #901399](https://bugs.launchpad.net/bugs/901399): Wrong result (extra row) with semijoin=ON, materialization=OFF, optimizer\_prune\_level=0
    * Correctly handle plan refinement stage for LooseScan plans: run create\_ref\_for\_key() if LooseScan\
      plan includes a ref access, and if we don't have any fixed key components, switch to a full index scan.
* [Revision #3353](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3353)\
  Thu 2011-12-15 17:26:32 +0400
  * Fix unused variable 'thd' error.
* [Revision #3352](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3352) \[merge]\
  Thu 2011-12-15 16:47:39 +0400
  * Merge
  * [Revision #3349.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3349.1.1)\
    Thu 2011-12-15 02:49:19 +0400
    * Make MyISAM's version of create\_internal\_tmp\_table set\
      QPLAN\_TMP\_DISK, like Aria version does (otherwise slow query\
      log would show Tmp\_table\_on\_disk=No when it should have said Yes)
* [Revision #3351](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3351)\
  Thu 2011-12-15 16:43:28 +0400
  * Fix trivial merge error
* [Revision #3350](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3350) \[merge]\
  Wed 2011-12-14 20:38:38 +0200
  * Merge
  * [Revision #3345.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3345.1.2) \[merge]\
    Wed 2011-12-14 20:36:51 +0200
    * Merge with 5.2
    * [Revision #2732.46.39](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.39) \[merge]\
      Tue 2011-12-13 20:08:41 +0200
      * Merge with 5.1
      * Updated version number in configure
      * [Revision #2643.143.66](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.66)\
        Mon 2011-12-12 16:28:16 +0100
        * new "`./configure --disable-distribution`" option
        * [Revision #2643.143.65](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.65)\
          Mon 2011-12-12 13:37:18 +0100
          * Fix GCC build failure in PBXT in some cases/platforms.
          * [Revision #2643.143.64](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.64)\
            Sun 2011-12-11 22:58:01 +0200
            * Fixed valgrind problem: reference on deleted memory of temporary table name.\
              Removed previous patch of this problem.
    * [Revision #2732.46.38](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.38)\
      Tue 2011-12-13 19:57:19 +0200
      * Fixed [Bug #887051](https://bugs.launchpad.net/bugs/887051) ; Error in recovery with LOAD DATA + DELETE
  * [Revision #3345.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3345.1.1)\
    Tue 2011-12-13 20:07:23 +0200
    * Fixed failure with query\_cache.test for embedded server
* [Revision #3349](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3349) \[merge]\
  Wed 2011-12-14 04:56:54 +0400
  * Merge
  * [Revision #3338.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3338.1.1)\
    Wed 2011-12-14 04:39:29 +0400
    * [Bug #901506](https://bugs.launchpad.net/bugs/901506): Crash in TABLE\_LIST::print on EXPLAIN EXTENDED
      * Let JTBM optimization code handle the case where the subquery is\
        degenerate and doesn't have a join query plan. Regular materialization\
        would fall back to IN->EXISTS for such cases. Semi-Join materialization\
        does not have such option, instead we introduce and use "constant JTBM\
        join tabs".
* [Revision #3348](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3348) \[merge]\
  Tue 2011-12-13 14:28:53 -0800
  * Merge
  * [Revision #3346.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3346.1.1)\
    Tue 2011-12-13 14:20:47 -0800
    * Fixed [Bug #902356](https://bugs.launchpad.net/bugs/902356).
    * A memory overwrite in the function test\_if\_skip\_sort\_order()\
      could cause a crash for some queries with subqueries.
* [Revision #3347](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3347)\
  Wed 2011-12-14 02:15:15 +0400
  * [Bug #902632](https://bugs.launchpad.net/bugs/902632): Crash or invalid read at st\_join\_table::cleanup, st\_table::disable\_keyread
    * Do a "more thorough" cleanup of SJ-Materialization join tab in\
      JOIN\_TAB::cleanup. The bug was due to the fact that JOIN\_TAB::cleanup() may\
      be called multiple times for the same tab if the join has grouping.
* [Revision #3346](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3346)\
  Tue 2011-12-13 20:52:06 +0200
  * The variable query\_cache\_strip\_comments allowed in embedded server.
* [Revision #3345](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3345) \[merge]\
  Tue 2011-12-13 14:11:08 +0200
  * Automatic merge
  * [Revision #3343.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3343.1.1)\
    Tue 2011-12-13 14:00:20 +0200
    * Fixed valgrind error when storing db\_name\_length in query\_cache.
      * Changed storage to be 2 bytes instead of sizeof(size\_t) (simple optimization)
      * Fixed bug when using query\_cache\_strip\_comments and query that started with '('
      * Fixed DBUG\_PRINT() that used wrong (not initialized) variables.
* [Revision #3344](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3344) \[merge]\
  Mon 2011-12-12 13:00:33 +0100
  * 5.2->5.3 merge
  * [Revision #2732.46.37](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.37)\
    Mon 2011-12-12 12:36:46 +0200
  * Fixed [Bug #900375](https://bugs.launchpad.net/bugs/900375)
  * The range optimizer incorrectly chose a loose scan for group by\
    when there is a correlated WHERE condition. This range access\
    method cannot be executed for correlated conditions also with the\
    "range checked for each record" because generally the range access\
    method can change for each outer record. Loose scan destructively\
    changes the query plan and removes the GROUP operation, which will\
    result in wrong query plans if another range access is chosen\
    dynamically.
  * [Revision #2732.46.36](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.36)\
    Thu 2011-12-08 12:05:52 +0200
  * Fixed [Bug #888456](https://bugs.launchpad.net/bugs/888456)
  * Analysis:
    * The class member QUICK\_GROUP\_MIN\_MAX\_SELECT::seen\_first\_key\
      was not reset between subquery re-executions. Thus each\
      subsequent execution continued from the group that was\
      reached by the previous subquery execution. As a result\
      loose scan reached end of file much earlier, and returned\
      empty result where it shouldn't.
  * Solution:
    * Reset seen\_first\_key before each re-execution of the\
      loose scan.
  * [Revision #2732.46.35](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.35)\
    Sat 2011-12-03 22:44:33 +0100
    * updated the version in configure
  * [Revision #2732.46.34](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.34)\
    Fri 2011-12-02 16:27:13 +0100
    * PAM plugin with test
  * [Revision #2732.46.33](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.33)\
    Fri 2011-12-02 16:26:43 +0100
    1. add `--plugin-dir` and `--default-auth` to mysqltest.
    2. dialog plugin now always returns mysql->password if non-empty and the first question is of password type
    3. split get\_tty\_password into get\_tty\_password\_buff and strdup.
    4. dialog plugin now uses get\_tty\_password by default
    5. dialog.test
    6. moved small tests of individual plugins into a dedicated suite
  * [Revision #2732.46.32](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.32)\
    Sat 2011-12-03 10:53:00 +0100
    * update tests
* [Revision #3343](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3343)\
  Sun 2011-12-11 19:41:53 -0800
  * Fixed [Bug #901709](https://bugs.launchpad.net/bugs/901709)
  * The cause of the reported assertion failure was a division of a double value by 0.
* [Revision #3342](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3342) \[merge]\
  Sun 2011-12-11 14:38:14 -0800
  * Merge
  * [Revision #3339.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3339.1.1)\
    Sun 2011-12-11 12:56:06 -0800
    * Fixed [Bug #901478](https://bugs.launchpad.net/bugs/901478)
    * If the duplicate elimination strategy is used for a semi-join and potentially\
      one of the block-based join algorithms can be employed to join the inner\
      tables of the semi-join then sorting of the head (first non-constant) table\
      for a query with ORDER BY / GROUP BY cannot be used.
* [Revision #3341](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3341)\
  Sun 2011-12-11 12:42:43 -0800
  * Adjusted the results of pbxt.subselect after the latest merge 5.1->5.2->5.3.
* [Revision #3340](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3340) \[merge]\
  Sun 2011-12-11 19:28:05 +0200
  * Merge with 5.1 & fixes to IGNORE handling
  * [Revision #3327.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3327.1.3)\
    Sun 2011-12-11 18:39:33 +0200
    * Rewrite IGNORE handling:
      * Instead of supressing all errors, only suppress safe ones like:
        * ER\_DUP\_KEY, ER\_BAD\_NULL\_ERROR, ER\_SUBQUERY\_NO\_1\_ROW, ER\_ROW\_IS\_REFERENCED\_2
  * [Revision #3327.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3327.1.2) \[merge]\
    Sun 2011-12-11 11:34:44 +0200
    * Merge with 5.2.
    * no\_error handling for select (used by `INSERT ... SELECT`) still needs to\
      be fixed, but I will do that in a separate commit
    * [Revision #2732.46.31](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.31) \[merge]\
      Sat 2011-12-03 20:47:25 +0200
      * Merge with 5.1
      * [Revision #2643.143.63](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.63)\
        Sat 2011-12-03 20:29:15 +0200
        * Added suppressions
        * Fixed feedback\_plugin\_send to not generate a random number of lines.
      * [Revision #2643.143.62](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.62) \[merge]\
        Thu 2011-12-01 19:20:57 +0100
        * merge
        * [Revision #2643.150.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.150.2) \[
          * merge]\
            Thu 2011-12-01 19:18:45 +0100
          * merge
        * [Revision #2643.150.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.150.1)\
          Thu 2011-12-01 19:15:09 +0100
          * Fix main.merge testcase on Windows
    * [Revision #2732.46.30](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.30)\
      Sat 2011-12-03 20:44:54 +0200
      * Fixed buildbot warnings
    * [Revision #2732.46.29](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.29)\
      Fri 2011-12-02 18:10:54 +0200
      * Fixed some Aria limits to be more sane
    * [Revision #2732.46.28](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.28) \[merge]\
      Fri 2011-12-02 17:32:56 +0200
      * Merge
      * [Revision #2732.49.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.49.1)\
        Fri 2011-12-02 17:22:17 +0200
        * Fixed bug where automaticly zerofilled table was not part of recovery if crash happended before next checkpoint.
    * [Revision #2732.46.27](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.27)\
      Thu 2011-12-01 22:37:45 +0100
      * Fix intermittently failing variables-notembedded test case.
      * After sending packet that is too large, clienrt can get either an error packet with\
        ER\_NET\_PACKET\_TOO\_LARGE, or a socket error. Both cases are valid, since the\
        server does not ensure reply was fully read by client, before shutting down and closing\
        the socket.
    * [Revision #2732.46.26](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.26)\
      Thu 2011-12-01 20:21:11 +0200
      * Fixed compiler warning
    * [Revision #2732.46.25](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.25) \[merge]\
      Thu 2011-12-01 20:14:53 +0200
      * Merge with 5.1
      * [Revision #2643.143.61](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.61)\
        Thu 2011-12-01 20:11:41 +0200
        * Fixed that `--with-libedit --without-readline` works
        * Fixed buildbot failures (compiler warnings, failing tests)
    * [Revision #2732.46.24](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.24) \[merge]\
      Wed 2011-11-30 22:57:18 +0200
      * Merge with 5.1
      * [Revision #2643.143.60](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.60)\
        Wed 2011-11-30 20:57:09 +0200
        * Fixed compiler warning and errors
      * [Revision #2643.143.59](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.59)\
        Wed 2011-11-30 18:44:51 +0200
        * Fixed compiler warnings and other bugs found by buildbot.
      * [Revision #2643.143.58](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.58)\
        Wed 2011-11-30 11:37:28 +0100
        * test both federated and federatedX in the federated suite.
      * [Revision #2643.143.57](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.57)\
        Wed 2011-11-30 13:53:25 +0100
        * Cherrypick into XtraDB: Bug#13002783 PARTIALLY UNINITIALIZED CASCADE UPDATE VECTOR<>
        * We merged the test case for this into [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md), but the fix was not\
          yet part of XtraDB.
      * [Revision #2643.143.56](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.56)\
        Wed 2011-11-30 00:34:05 +0200
        * Fixed compiler warnings
    * [Revision #2732.46.23](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.23) \[merge]\
      Tue 2011-11-29 22:48:24 +0200
      * Merge with 5.1 + fixes for build failures in 5.2
      * [Revision #2643.143.55](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.55)\
        Tue 2011-11-29 15:32:25 +0200
        * Fixed that maria-recover works as expected.
          * "" is now used if no option is set
      * [Revision #2643.143.54](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.54)\
        Tue 2011-11-29 01:10:17 +0100
        * Fix Windows build, and a conversion truncation warning.
      * [Revision #2643.143.53](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.53)\
        Thu 2011-11-24 19:23:20 +0200
        * Fixed that one can use `--maria-recover=backup,force`
        * (Before we only allowed one option)
    * [Revision #2732.46.22](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.22)\
      Tue 2011-11-29 08:50:54 +0100
      * Fix testcases:
        1. main.merge fails with errno 13 in copy\_file().
        2. The reason for the error is that copy\_file tries to create a file with\
           the same name as recently deleted one, and there is still an open handle\
           for the deleted file.
        3. To fix, use my\_delete\_allow\_opened() for MTR's delete\_file. On Windows,\
           this renames file to unique name prior to deletion, and prevents EACCES\
           errors for files opened with FILE\_SHARE\_DELETE.
        4. innodb\_bug59641
        5. generates warnings, after server was killed and restarted in the test case.
        6. The warnings are about test\_suppression table (needs to be repaired, as it that was written just prior to the crash)
        7. Fixed by using FLUSH TABLES after populating warning suppression table.
    * [Revision #2732.46.21](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.21)\
      Tue 2011-11-29 02:00:24 +0100
      * merge, fix Windows warnings
    * [Revision #2732.46.20](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.20)\
      Mon 2011-11-28 15:08:12 +0100
      * after merge fixes
    * [Revision #2732.46.19](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.19) \[merge]\
      Thu 2011-11-24 22:48:35 +0200
      * Automatic merge
      * [Revision #2732.48.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.48.2)\
        Thu 2011-11-24 19:07:36 +0200
        * Added test case for [Bug #875797](https://bugs.launchpad.net/bugs/875797) Using 'innodb\_sys\_indexes' causes core dump
      * [Revision #2732.48.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.48.1) \[merge]\
        Thu 2011-11-24 18:48:58 +0200
        * Merge with [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)
        * [Revision #2643.143.52](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.52)\
          Thu 2011-11-24 16:04:19 +0200
          * Fixes for build failuers found by buildbot
        * [Revision #2643.143.51](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.51) \[merge]\
          Wed 2011-11-23 19:32:14 +0200
          * Merge with MySQL 5.1.60
        * [Revision #2643.143.50](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.50)\
          Wed 2011-11-23 10:25:27 +0200
          * Fixes of testcases after merge with MySQL 5.1.59
        * [Revision #2643.143.49](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.49) \[merge]\
          Mon 2011-11-21 19:19:37 +0200
          * Merge of XtraDB for 5.1.59
          * [Revision #2643.149.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.149.1) \[merge]\
            Mon 2011-11-21 14:21:13 +0100
            * Merge XtraDB from Percona-Server-5.1.59-13 into [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md).
            * [Revision #0.6.47](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/0.6.47)\
              Mon 2011-11-21 13:20:15 +0100
              * Updated with changes from Percona Server 5.1.56-13, from\
                lp`:`percona-server/5.1, tag Percona-Server-5.1.59-13.0.
              * Merged: revid:ignacio.nin@percona.com-20111016133841-fzpr5s89n13ft1s1
        * [Revision #2643.143.48](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.48) \[merge]\
          Mon 2011-11-21 19:17:56 +0200
          * Automatic merge
          * [Revision #2643.148.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.148.1) \[merge]\
            Mon 2011-11-21 19:13:14 +0200
            * Initial merge with MySQL 5.1 (XtraDB still needs to be merged)
            * Fixed up copyright messages.
    * [Revision #2732.46.18](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.18)\
      Tue 2011-11-22 21:55:11 +0100
      * fix dialog plugin to work on windows
    * [Revision #2732.46.17](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.17)\
      Tue 2011-11-15 13:14:54 +0200
      * Fix for [Bug #780425](https://bugs.launchpad.net/bugs/780425) sql\_buffer\_result=1 gives wrong result for GROUP BY with a +

## constant expression"

* [Revision #3327.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3327.1.1)\
  Sat 2011-12-03 23:06:16 +0200
  * Added handler and temporary table usage to mytop
  * Fixed prompt on reconnect in mysql client
* [Revision #3339](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3339)\
  Fri 2011-12-09 14:30:50 -0800
  * Fixed [Bug #901312](https://bugs.launchpad.net/bugs/901312)
  * The function setup\_sj\_materialization\_part1() forgot to set the value\
    of TABLE::map for any materialized IN subquery.
  * This could lead to wrong results for queries with subqueries that were\
    converted to queries with semijoins.
* [Revision #3338](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3338)\
  Thu 2011-12-08 16:29:45 +0400
  * [Bug #901655](https://bugs.launchpad.net/bugs/901655) ST\_BUFFER asserts with a coplicated shape.
  * Coinciding nodes can appear as a result of DOUBLE inaccuracy.
  * We should test that before we start the loop.
  * Also the spatial relations can be calculated faster if we check\
    MBR relations first. And we do have the shape's MBR-s now.
  * per-file comments:
    * sql/gcalc\_slicescan.cc
      * set\_extent() method added.
      * [Bug #901655](https://bugs.launchpad.net/bugs/901655) ST\_BUFFER asserts with a coplicated shape.
    * sql/gcalc\_slicescan.h
      * set\_extent() method declared.
      * [Bug #901655](https://bugs.launchpad.net/bugs/901655) ST\_BUFFER asserts with a coplicated shape.
    * sql/gcalc\_tools.cc
      * [Bug #901655](https://bugs.launchpad.net/bugs/901655) ST\_BUFFER asserts with a coplicated shape.
      * checks for equal nodes added.
    * sql/item\_geofunc.cc
      * [Bug #901655](https://bugs.launchpad.net/bugs/901655) ST\_BUFFER asserts with a coplicated shape.
      * MBR for the shapes calculated, and MBR checks added before we\
        start the heavy calculations.
    * sql/spatial.h
      * [Bug #901655](https://bugs.launchpad.net/bugs/901655) ST\_BUFFER asserts with a coplicated shape.
      * MBR::buffer() method implemented.
* [Revision #3337](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3337)\
  Thu 2011-12-08 04:22:38 +0400
  * Small semi-join optimization improvement:
    * if we're considering FirstMatch access with one inner table, and\
      @@optimizer\_switch has semijoin\_with\_cache flag, calculate costs\
      as if we used join cache (because we will be able to do so)
* [Revision #3336](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3336) \[merge]\
  Thu 2011-12-08 02:47:54 +0400
  * Merge fix for [Bug #868908](https://bugs.launchpad.net/bugs/868908)
  * [Revision #3322.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3322.1.3)\
    Wed 2011-12-07 23:15:57 +0400
    * Remove garbage assignments causing failures on Windows
  * [Revision #3322.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3322.1.2)\
    Wed 2011-12-07 19:21:51 +0400
    * [Bug #868908](https://bugs.launchpad.net/bugs/868908): Crash in check\_simple\_equality() with semijoin + materialization + prepared statement
      * Part2: safety and code cleanup
  * [Revision #3322.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3322.1.1)\
    Wed 2011-12-07 01:03:00 +0400
    * [Bug #868908](https://bugs.launchpad.net/bugs/868908): Crash in check\_simple\_equality() with semijoin + materialization + prepared statement
      * Part 1 of the fix: for semi-join merged subqueries, calling child\_join->optimize() until we're done with all\
        PS-lifetime optimizations in the parent.
* [Revision #3335](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3335)\
  Thu 2011-12-08 02:12:48 +0400
  * [Bug #901032](https://bugs.launchpad.net/bugs/901032): Wrong result for MIN/MAX on an indexed column with materialization and semijoin
    * opt\_sum\_query() should not assume that join tables from sj-materialization\
      have known numbers of rows.
* [Revision #3334](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3334)\
  Tue 2011-12-06 13:42:18 -0800
  * Fixed [Bug #900469](https://bugs.launchpad.net/bugs/900469).
  * The execution plan cannot use sorting on the first table from the\
    sequence of the joined tables if it plans to employ the block-based\
    hash join algorithm.
* [Revision #3333](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3333)\
  Tue 2011-12-06 02:46:42 -0800
  * Fixed [Bug #899509](https://bugs.launchpad.net/bugs/899509).
  * The optimizer must ignore any possible hash join key when looking for the\
    query execution plan with join\_cache\_level set to 0.
* [Revision #3332](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3332) \[merge]\
  Mon 2011-12-05 18:52:50 -0800
  * Merge
  * [Revision #3330.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3330.1.1) \[merge]\
    Mon 2011-12-05 18:51:56 -0800
    * Merge
    * [Revision #3328.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3328.1.1)\
      Mon 2011-12-05 09:50:24 -0800
      * Fixed [Bug #899777](https://bugs.launchpad.net/bugs/899777).
      * KEYUSE elements for a possible hash join key are not sorted by field\
        numbers of the second table T of the hash join operation. Besides\
        some of these KEYUSE elements cannot be used to build any key as their\
        key expressions depend on the tables that are planned to be accessed\
        after the table T.
      * The code before the patch did not take this into account and, as a result,\
        execition of a query the employing block-based hash join algorithm could\
        cause a crash or return a wrong result set.
* [Revision #3331](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3331)\
  Tue 2011-12-06 01:04:27 +0400
  * [Bug #899962](https://bugs.launchpad.net/bugs/899962): materialized subquery with join\_cache\_level=3
  * Make create\_tmp\_table() set KEY\_PART\_INFO attributes for the keys it creates.
  * This wasn't needed before but is needed now, when temp. tables that are\
    results of SJ-Materialization are being used for joins.
  * This particular bug depended on HA\_VAR\_LENGTH\_PART being set,\
    but also added code to set HA\_BLOB\_PART and HA\_NULL\_PART when appropriate.
* [Revision #3330](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3330)\
  Mon 2011-12-05 10:24:14 +0400
  * Update test result missed in the previous cset
* [Revision #3329](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3329)\
  Mon 2011-12-05 01:31:42 +0400
  * Make subquery Materialization, as well as semi-join Materialization be shown\
    in EXPLAIN as select\_type==MATERIALIZED.
  * Before, we had select\_type==SUBQUERY and it was difficult to tell materialized\
    subqueries from uncorrelated scalar-context subqueries.
* [Revision #3328](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3328)\
  Sun 2011-12-04 07:43:33 -0800
  * Fixed [Bug #899696](https://bugs.launchpad.net/bugs/899696).
  * If has been decided that the first match strategy is to be used to join table T\
    from a semi-join nest while no buffer can be employed to join this table\
    then no join buffer can be used to join any table in the join sequence between\
    the first one belonging to the semi-join nest and table T.
* [Revision #3327](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3327)\
  Fri 2011-12-02 00:36:55 +0200
  * Added new file (for netware)
  * Added some file to ignore
* [Revision #3326](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3326)\
  Fri 2011-12-02 00:34:59 +0200
  * Fixes for netware by Guenter Knauf
* [Revision #3325](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3325)\
  Fri 2011-12-02 00:24:58 +0200
  * Patch to get MariaDB to compile on CYGWIN; By Guenter Knauf
  * Increased number of locks in thr\_lock (used only when testing)
* [Revision #3324](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3324)\
  Wed 2011-11-30 10:22:53 -0800
  * Fixed [Bug #898073](https://bugs.launchpad.net/bugs/898073).
  * The tables from the same semi-join or outer join nest cannot use\
    join buffers if in the join sequence of the query execution plan\
    they are separated by a table that is planned to be joined without\
    usage of a join buffer.
* [Revision #3323](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3323) \[merge]\
  Wed 2011-11-30 08:28:40 +0200
  * Merge the fix of [Bug #825051](https://bugs.launchpad.net/bugs/825051)
  * [Revision #3321.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3321.1.1)\
    Tue 2011-11-29 23:06:39 +0200
    * Fixed [Bug #825051](https://bugs.launchpad.net/bugs/825051)
    * The cause of the wrong result was that Item\_ref\_null\_helper::get\_date()\
      didn't use a method of the \*\_result() family, and fetched the data\
      for the field from the current row instead of result\_field. Changed to\
      use the correct \*\_result() method, like to all other similar methods\
      of Item\_ref\_null\_helper.
* [Revision #3322](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3322)\
  Tue 2011-11-29 23:09:06 +0200
  * Added test suite for the [Bug #885162](https://bugs.launchpad.net/bugs/885162) (fixed by the patch for [Bug #859375](https://bugs.launchpad.net/bugs/859375) and [Bug #887458](https://bugs.launchpad.net/bugs/887458)).
* [Revision #3321](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3321)\
  Tue 2011-11-29 15:27:52 +0400
  * [Bug #857066](https://bugs.launchpad.net/bugs/857066) Wrong result with ST\_DISJOINT when using an index.
  * DISJOINT can't be properly optimized with the RTree keys in MyISAM also.
  * per-file comments:
    * storage/myisam/rt\_index.c
      * [Bug #857066](https://bugs.launchpad.net/bugs/857066) Wrong result with `ST_DISJOINT` when using an index.
      * don't optimize `DISJOINT` with the RTree keys.
* [Revision #3320](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3320)\
  Tue 2011-11-29 02:11:13 +0400
  * [Bug #857066](https://bugs.launchpad.net/bugs/857066) Wrong result with ST\_DISJOINT when using an index\
    the ST\_DISJOINT can't be properly optimized with the RTree key\
    at the moment.
  * per-file comments:
    * storage/maria/ma\_rt\_index.c
      * [Bug #857066](https://bugs.launchpad.net/bugs/857066) Wrong result with ST\_DISJOINT when using an index\
        disabled optimization for the DISJOINT case.
* [Revision #3319](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3319)\
  Mon 2011-11-28 15:24:07 +0200
  * Fix [Bug #833777](https://bugs.launchpad.net/bugs/833777), [Bug #894397](https://bugs.launchpad.net/bugs/894397)
  * Analysis:
    * [Bug #894397](https://bugs.launchpad.net/bugs/894397) was a consequence of a prior incorrect fix of [Bug #833777](https://bugs.launchpad.net/bugs/833777)\
      which didn't take into account that even when all tables are\
      constant there may be correlated conditions, and the where clause\
      is not equivalent to the constant conditions.
  * Solution:
    * When there are constant tables only, evaluate only the conditions\
      that reference outer fields, because the constant conditions are\
      already checked, and the where clause doesn't have other conditions\
      than constant ones, and outer referencing ones. The fix for [Bug #894397](https://bugs.launchpad.net/bugs/894397) also fixes [Bug #833777](https://bugs.launchpad.net/bugs/833777)
* [Revision #3318](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3318)\
  Mon 2011-11-28 12:42:14 +0200
  * Fixed [Bug #747278](https://bugs.launchpad.net/bugs/747278)
  * The problem was that when we have single row subquery with no rows\
    Item\_cache(es) which represent result row was not null and being\
    requested via element\_index() returned random value.
  * The fix is setting all Item\_cache(es) in NULL before executing the\
    query (reset() method) which guaranty NULL value of whole query\
    or its elements requested in any way if no rows was found.
  * set\_null() method was added to Item\_cache to guaranty correct NULL\
    value in case of reseting the cache.
* [Revision #3317](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3317)\
  Sat 2011-11-26 14:23:00 -0800
  * Set new default values for the optimizer switch flags 'derived\_merge'\
    and 'derived\_with\_keys'. Now they are set on by default.
* [Revision #3316](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3316) \[merge]\
  Sat 2011-11-26 12:27:52 +0400
  * Merge
  * [Revision #3314.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3314.1.5)\
    Fri 2011-11-25 23:54:36 +0400
    * Subquery code cleanups:
* Make functions that operate on SJ\_TMP\_TABLE be member functions
* Make Loose\_scan\_opt data members private
* [Revision #3314.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3314.1.4)\
  Fri 2011-11-25 21:45:58 +0400
  * Update test results
* [Revision #3314.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3314.1.3)\
  Fri 2011-11-25 15:48:56 +0400
  * Update test results
* [Revision #3314.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3314.1.2)\
  Fri 2011-11-25 14:57:27 +0400
  * Remove garbage comments
* [Revision #3314.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3314.1.1) \[merge]\
  Fri 2011-11-25 14:28:43 +0400
  * Merge
  * [Revision #3275.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3275.1.3)\
    Fri 2011-11-25 05:56:58 +0400
    * Semi-join optimizations code cleanup part 2:
      * Make EXPLAIN display "Start temporary" at the start of the fanout (it used to display\
        at the first table whose rowid gets into temp. table which is not that useful for\
        the user)
      * Updated test results (all checked)
  * [Revision #3275.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3275.1.2)\
    Wed 2011-11-23 04:25:52 +0400
    * Semi-join optimizations code cleanup:
      * Break down POSITION/advance\_sj\_state() into four classes\
        representing potential semi-join strategies.
      * Treat all strategies uniformly (before, DuplicateWeedout\
        was special as it was the catch-all strategy. Now, we're\
        still relying on it to be the catch-all, but are able to\
        function,e.g. with firstmatch=on,duplicate\_weedout=off.
      * Update test results (checked)
  * [Revision #3275.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3275.1.1)\
    Sat 2011-11-12 20:50:11 +0200
    * [Bug #887468](https://bugs.launchpad.net/bugs/887468): Second assertion \`keypart\_map' failed in maria\_rkey with semijoin
    * in advance\_sj\_state: Do not try to construct LooseScan strategy if we're\
      already behind the last LooseScan table.
* [Revision #3315](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3315)\
  Fri 2011-11-25 22:54:13 +0400
  * Remove garbage comment
* [Revision #3314](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3314)\
  Thu 2011-11-24 22:56:02 -0800
  * Currently innodb\_plugin does not support ICP. Part2.
* [Revision #3313](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3313)\
  Thu 2011-11-24 23:47:50 +0200
  * Added valgrind suppression for an error due to
  * [bugreport.cgi?bug=577135](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=577135)
* [Revision #3312](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3312)\
  Thu 2011-11-24 23:15:40 +0200
  * Fix [Bug #894326](https://bugs.launchpad.net/bugs/894326)
  * The patch also fixes an unrelated compiler warning.
  * Analysis:
    * The temporary table created during SJ-materialization\
      might be used for sorting for a group by operation. The\
      sort buffers for this internal temporary table were not\
      cleared by the execution code after each subquery\
      re-execution. This resulted in a memory leak detected\
      by valgrind.
  * Solution:
    * Cleanup the sort buffers for the semijon tables as well.
* [Revision #3311](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3311)\
  Thu 2011-11-24 12:19:37 -0800\
  Currently innodb\_plugin does not support ICP.
* [Revision #3310](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3310)\
  Thu 2011-11-24 15:12:10 +0200
  * Fix for [Bug #859375](https://bugs.launchpad.net/bugs/859375) and [Bug #887458](https://bugs.launchpad.net/bugs/887458).
  * Stop attempts to apply IN/ALL/ANY optimizations to so called "fake\_select"\
    (used for ordering and filtering results of union) in union subquery execution.
* [Revision #3309](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3309)\
  Thu 2011-11-24 16:26:13 +0400
  * fixes to make compilers happy.
  * per-file comments:
    * mysql-test/t/gis-precise.test
      * number-to-string conversion differs on Windows.
      * Have to tolerate this while GIS data is stored in doubles.
    * sql/spatial.cc
      * prev\_x initialization added.
* [Revision #3308](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3308)\
  Wed 2011-11-23 23:13:51 +0200
  * Fix [Bug #893486](https://bugs.launchpad.net/bugs/893486)
  * Analysis:
    * The bug is a result of an incomplete fix for [Bug #869036](https://bugs.launchpad.net/bugs/869036)
    * That fix didn't take into account that there may be a case\
      when ther are no NULLs in the materialized subquery, however\
      all columns without NULLs may not be grouped in the only\
      non-null index. This is the case when the left subquery expression\
      has nullable columns.
  * Solution:
    * The patch handles two missing sub-cases of the case when there are\
      no value (non-null matches) for any outer expression, and there are\
      both NULLs and non-NUll values in the outer reference.
      1. If the materialized subquery contains no NULLs there cannot be a\
         partial match, because there are no NULLs in those columns where\
         the outer reference has no NULLs.
      2. If the materialized subquery contains NULLs, but there exists a\
         column, such that its corresponding outer expression has no NULL,\
         and this column also has no NULL. Then there cannot be a partial\
         match either.
* [Revision #3307](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3307)\
  Tue 2011-11-22 17:57:33 +0400
  * Small fixes to make compilers happy.
* [Revision #3306](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3306)\
  Tue 2011-11-22 17:32:05 +0400
  * Windows has no 'nearbyint' in libraries.
  * So removed.
* [Revision #3305](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3305) \[merge]\
  Tue 2011-11-22 12:06:46 +0200
  * Merge default materialization=on.
  * [Revision #3300.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3300.2.1) \[merge]\
    Mon 2011-11-21 17:48:25 +0200
    * Merge enabling materialization=on by default.
    * [Revision #3290.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3290.1.1) \[merge]\
      Mon 2011-11-21 16:56:32 +0200
      * Merge enabling of materialization=on by default with main tree.
      * [Revision #3273.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3273.1.3)\
        Wed 2011-11-09 21:29:01 +0200
        * Fixed PBXT test cases.
      * [Revision #3273.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3273.1.2)\
        Wed 2011-11-09 16:46:08 +0200
        * Removed a comment that is not true any more.
        * Consistent use of the `SUBS_NOT_TRANSFORMED` constant for in\_strategy.
      * [Revision #3273.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3273.1.1)\
        Wed 2011-11-09 15:36:25 +0200
        * Enable subquery materialization=ON by default.
* [Revision #3304](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3304)\
  Mon 2011-11-21 22:16:01 +0200
  * Fix [Bug #833777](https://bugs.launchpad.net/bugs/833777)
  * Correct test file.
* [Revision #3303](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3303)\
  Mon 2011-11-21 22:01:47 +0200
  * Fix [Bug #833777](https://bugs.launchpad.net/bugs/833777)
  * Fix test to pass on 32-bit machines by reducing\
    the depth of subquery nestedness to less than 31\
    (sizeof(ulong)-1).
* [Revision #3302](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3302) \[merge]\
  Mon 2011-11-21 11:21:30 -0800
  * Merge.
  * [Revision #3300.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3300.1.1)\
    Mon 2011-11-21 09:06:35 -0800
    * Fixed [Bug #887496](https://bugs.launchpad.net/bugs/887496)
    * This bug in the function Loose\_scan\_opt::check\_ref\_access\_part1 could lead\
      to choosing an invalid execution plan employing a loose scan access to a\
      semi-join table even in the cases when such access could not be used at all.\
      This could result in wrong answers for some queries with IN subqueries.
* [Revision #3301](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3301)\
  Mon 2011-11-21 18:00:55 +0200
  * Fix [Bug #833777](https://bugs.launchpad.net/bugs/833777)
  * Analysis:
    * The optimizer distinguishes two kinds of 'constant' conditions:\
      expensive ones, and non-expensive ones. The non-expensive conditions\
      are evaluated inside make\_join\_select(), and if false, already the\
      optimizer detects empty query results.
    *   In order to avoid arbitrarily expensive optimization, the evaluation of\
        expensive constant conditions is delayed until execution. These conditions\
        are attached to JOIN::exec\_const\_cond and evaluated in the beginning of\
        JOIN::exec. The relevant execution logic is:

        ```c
        JOIN::exec()
         {
         if (! join->exec_const_cond->val_int())
         {
         produce an empty result;
         stop execution
         }
         continue execution
         execute the original WHERE clause (that contains exec_const_cond)
         ...
         }
        ```
* As a result, when an expensive constant condition is\
  TRUE, it is evaluated twice - once through\
  JOIN::exec\_const\_cond, and once through JOIN::cond.\
  When the expensive constant condition is a subquery,\
  predicate, the subquery is evaluated twice. If we have\
  many levels of subqueries, this logic results in a chain\
  of recursive subquery executions that walk a perfect\
  binary tree. The result is that for subquries with depth N,\
  JOIN::exec is executed O(2^N) times.
* Solution:
  * Notice that the second execution of the constant conditions\
    happens inside do\_select(), in the branch:\
    if (join->table\_count == join->const\_tables) { ... }\
    In this case exec\_const\_cond is equivalent to the whole WHERE\
    clause, therefore the WHERE clause has already been checked in\
    the beginnig of JOIN::exec, and has been found to be true.\
    The bug is addressed by not evaluating the WHERE clause if there\
    was exec\_const\_conds, and it was TRUE.
* [Revision #3300](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3300)\
  Mon 2011-11-21 07:00:14 -0800
  * Corrected the patch that made the optimizer switch for index condition pushdown\
    set to 'on' by default.
* [Revision #3299](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3299)\
  Mon 2011-11-21 05:16:16 -0800
  * Made the optimizer switch for index condition pushdown set to 'on' by default.
* [Revision #3298](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3298)\
  Sun 2011-11-20 04:53:07 -0800
  * Fixed [Bug #892725](https://bugs.launchpad.net/bugs/892725).
  * A non-first execution of a prepared statement missed a call of the\
    TABLE\_LIST::process\_index\_hints() method in the code of the function\
    setup\_tables().
  * At some scenarios this could lead to the choice of a quite inefficient\
    execution plan for the base query of the prepared statement.
* [Revision #3297](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3297)\
  Sun 2011-11-20 12:30:43 +0400
  * Fix for [Bug #809849](https://bugs.launchpad.net/bugs/809849) spatial operations must be KILL-able.
    * Checks for thd->killed state added to the long loops in geometry calculations.
  * per-file comments:
    * sql/gcalc\_slicescan.cc
      * Fix for [Bug #809849](https://bugs.launchpad.net/bugs/809849) spatial operations must be KILL-able.
      * checks for TERMINATED\_STATE added.
    * sql/gcalc\_slicescan.h
      * Fix for [Bug #809849](https://bugs.launchpad.net/bugs/809849) spatial operations must be KILL-able.
      * defines added to include checks for termination in the\
        library.
    * sql/gcalc\_tools.cc
      * Fix for [Bug #809849](https://bugs.launchpad.net/bugs/809849) spatial operations must be KILL-able.
      * checks for TERMINATED\_STATE added.
    * sql/gcalc\_tools.h
      * Fix for [Bug #809849](https://bugs.launchpad.net/bugs/809849) spatial operations must be KILL-able.
      * TERMINATED\_STATE pointers added.
    * sql/item\_geofunc.cc
      * Fix for [Bug #809849](https://bugs.launchpad.net/bugs/809849) spatial operations must be KILL-able.
    * sql/item\_geofunc.h
      * Fix for [Bug #809849](https://bugs.launchpad.net/bugs/809849) spatial operations must be KILL-able.
* [Revision #3296](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3296)\
  Fri 2011-11-18 13:32:21 -0800
  * Fixed [Bug #891995](https://bugs.launchpad.net/bugs/891995)
  * This bug in the function setup\_semijoin\_dups\_elimination() could\
    lead to invalid choice of the sequence of tables for which semi-join\
    duplicate elimination was applied.
* [Revision #3295](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3295)\
  Fri 2011-11-18 09:35:51 -0800
  * Fixed [Bug #891953](https://bugs.launchpad.net/bugs/891953)
  * Due to this bug the function SEL\_IMERGE::or\_sel\_tree\_with\_checks()\
    could build an inconsistent merge tree if one of the SEL\_TREEs in the\
    resulting index merge happened to contain a full key range.
  * This could trigger an assertion failure.
* [Revision #3294](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3294)\
  Fri 2011-11-18 18:15:06 +0400
  * unused variable removed.
* [Revision #3293](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3293)\
  Fri 2011-11-18 17:56:42 +0400
  * GCALC\_CHECK\_WITH\_FLOAT disabled.
  * That's not a good option for an onrdinary user.
* [Revision #3292](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3292)\
  Fri 2011-11-18 04:41:25 -0800
  * Fixed [Bug #800184](https://bugs.launchpad.net/bugs/800184)
  * The function key\_and() erroneously called SEL\_ARG::increment\_use\_count()\
    when SEL\_ARG::incr\_refs() should had been called. This could lead to\
    wrong values of use\_count for some SEL\_ARG trees.
* [Revision #3291](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3291) \[merge]\
  Thu 2011-11-17 08:00:22 -0800
  * Merge.
  * [Revision #3287.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3287.1.1)\
    Thu 2011-11-17 03:24:20 -0800
    * Corrected the fix for [Bug #891052](https://bugs.launchpad.net/bugs/891052)
* [Revision #3290](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3290)\
  Thu 2011-11-17 18:03:47 +0400
  * small fixes to make compiler happy.
* [Revision #3289](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3289)\
  Thu 2011-11-17 17:12:58 +0400
  * test results updated.
* [Revision #3288](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3288) \[merge]\
  Thu 2011-11-17 14:27:00 +0400
  * merging.
  * [Revision #2978.3.42](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.42) \[merge]\
    Sat 2011-11-12 19:56:29 +0400
    * merging.
  * [Revision #2978.3.41](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.41)\
    Sun 2011-10-16 21:16:53 +0500
    * code cleanup.
  * [Revision #2978.3.40](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.40)\
    Sun 2011-10-16 19:55:37 +0500
    * GIS code cleanup.
  * [Revision #2978.3.39](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.39)\
    Fri 2011-10-14 18:37:40 +0500
    * \#define added
  * [Revision #2978.3.38](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.38)\
    Fri 2011-10-14 17:57:07 +0500
    * repeating calcualtions eliminated.
  * [Revision #2978.3.37](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.37)\
    Fri 2011-10-14 16:10:55 +0500
    * GIS code.
    * Forward calculations introduced.
    * per-file comments:
      * sql/gcalc\_slicescan.cc
      * sql/gcalc\_slicescan.h
      * sql/gcalc\_tools.cc
      * sql/gcalc\_tools.h
      * sql/item\_geofunc.cc
  * [Revision #2978.3.36](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.36)\
    Thu 2011-10-06 17:41:28 +0500
    * Copyright notices fixed.
  * [Revision #2978.3.35](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.35)\
    Wed 2011-10-05 14:45:39 +0500
    * Valgrind warning fixed.
    * Coordinate size limitation removed.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * test result updated.
      * sql/gcalc\_slicescan.cc
        * Check coordinate extent to pick better precidion in the ::set\_double()
      * sql/gcalc\_slicescan.h
        * free\_list() can lead to valgrind warnig. Fixed
      * sql/gcalc\_tools.cc
        * free\_list() call changed.
  * [Revision #2978.3.34](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.34)\
    Tue 2011-10-04 15:29:39 +0500
    * GIS code cleanup.
    * GCALC\_xxx macros fixed for the GCALC\_DBUG\_OFF case.
    * per-file comments:
      * sql/gcalc\_slicescan.h
        * GIS code cleanup.
  * [Revision #2978.3.33](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.33)\
    Tue 2011-10-04 15:01:21 +0500
    * GIS library code cleanup.
    * GCALC\_DBUG\_OFF and related infrastructure defined so we can enable/disable debugging conveniently.
    * per-file comments:
      * sql/gcalc\_slicescan.cc
        * GIS library code cleanup.
      * sql/gcalc\_slicescan.h
        * GIS library code cleanup.
      * sql/gcalc\_tools.cc
        * GIS library code cleanup.
      * sql/gcalc\_tools.h
        * GIS library code cleanup.
  * [Revision #2978.3.32](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.32)\
    Fri 2011-09-23 17:00:36 +0500
    * [Bug #857087](https://bugs.launchpad.net/bugs/857087) Wrong result with ST\_INTERSECTS and LINESTRINGs
    * Line autointersection point was treated as if it doesn't belong to the line.
    * It's in some way logical, but seems to confuse people. Fixed.
    * per\_file\_comments:
      * mysql-test/r/gis-precise.result
        * [Bug #857087](https://bugs.launchpad.net/bugs/857087) Wrong result with ST\_INTERSECTS and LINESTRINGs
        * test result updated.
      * mysql-test/t/gis-precise.test
        * [Bug #857087](https://bugs.launchpad.net/bugs/857087) Wrong result with ST\_INTERSECTS and LINESTRINGs
        * test case added.
      * sql/gcalc\_tools.cc
        * [Bug #857087](https://bugs.launchpad.net/bugs/857087) Wrong result with ST\_INTERSECTS and LINESTRINGs
        * Point of line autointersection handled as it belongs to the line.
      * sql/gcalc\_tools.h
        * [Bug #857087](https://bugs.launchpad.net/bugs/857087) Wrong result with ST\_INTERSECTS and LINESTRINGs
        * Gcalc\_function::set\_i\_state() added
  * [Revision #2978.3.31](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.31)\
    Fri 2011-09-23 15:36:56 +0500
    * [Bug #857050](https://bugs.launchpad.net/bugs/857050) ST\_WITHIN returns wrong result with MULTIPOINT and POLYGON\
      actually only testcase added as the bug was fixed already.
    * modified:
      * mysql-test/r/gis-precise.result
        * [Bug #857050](https://bugs.launchpad.net/bugs/857050) ST\_WITHIN returns wrong result with MULTIPOINT and POLYGON
        * test result updated.
      * mysql-test/t/gis-precise.test
        * [Bug #857050](https://bugs.launchpad.net/bugs/857050) ST\_WITHIN returns wrong result with MULTIPOINT and POLYGON
        * test case added.
      * sql/gcalc\_tools.cc
        * superfluous variable removed.
  * [Revision #2978.3.30](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.30)\
    Fri 2011-09-23 15:25:48 +0500
    * fix for [Bug #857051](https://bugs.launchpad.net/bugs/857051) ST\_EQUALS returns TRUE on two nonidentical MULTIPOINTs
    * The 'single point' event was forgotten in the relation's calculation
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * fix for [Bug #857051](https://bugs.launchpad.net/bugs/857051) ST\_EQUALS returns TRUE on two nonidentical MULTIPOINTs
        * test result updated.
      * mysql-test/t/gis-precise.test
        * fix for [Bug #857051](https://bugs.launchpad.net/bugs/857051) ST\_EQUALS returns TRUE on two nonidentical MULTIPOINTs
        * test case added.
      * sql/gcalc\_tools.cc
        * fix for [Bug #857051](https://bugs.launchpad.net/bugs/857051) ST\_EQUALS returns TRUE on two nonidentical MULTIPOINTs
        * scev\_single\_point is properly handled.
  * [Revision #2978.3.29](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.29)\
    Fri 2011-09-23 15:05:36 +0500
    * fix for 857050 ST\_WITHIN returns wrong result with MULTIPOINT and POLYGON\
      return GEOMETRYCOLLECTION EMPTY, not NULL for the query
    * per-file comments:
      * mysql-test/r/gis.result
        * fix for 857050 ST\_WITHIN returns wrong result with MULTIPOINT and POLYGON\
          test result updated.
      * sql/spatial.cc
        * fix for 857050 ST\_WITHIN returns wrong result with MULTIPOINT and POLYGON\
          return of the Geometry::envelope() changed for the empty geometry.
  * [Revision #2978.3.28](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.28)\
    Thu 2011-09-22 18:53:36 +0500
    * fixed bugs
      * [Bug #855485](https://bugs.launchpad.net/bugs/855485) ST\_CROSSES returns different result than PostGIS for overlapping polygons
      * [Bug #855487](https://bugs.launchpad.net/bugs/855487) ST\_WITHIN returns wrong result for partially overlapping polygons
      * [Bug #855492](https://bugs.launchpad.net/bugs/855492) ST\_WITHIN returns TRUE on point on the edge of a polygon
      * [Bug #855497](https://bugs.launchpad.net/bugs/855497) ST\_ENVELOPE of GEOMETRYCOLLECTION EMPTY returns NULL and not GEOMETRYCOLLECTION EMPTY
      * [Bug #855503](https://bugs.launchpad.net/bugs/855503) ST\_EQUALS reports TRUE between a POLYGON and a MULTILINESTRING
      * [Bug #855505](https://bugs.launchpad.net/bugs/855505) ST\_TOUCHES reports TRUE for intersecting polygon and linestring
    * Changed the way weird functions like Crosses or Touches treated.
    * Added BORDER handling to the Gcalc\_function.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * GIS bugs fixed.
        * test result updated.
      * mysql-test/t/gis-precise.test
        * GIS bugs fixed.
        * test cases added.
      * sql/gcalc\_slicescan.h
        * GIS bugs fixed.
      * sql/gcalc\_tools.cc
        * GIS bugs fixed.
      * sql/gcalc\_tools.h
        * GIS bugs fixed.
      * sql/item\_create.cc
        * GIS bugs fixed.
      * sql/item\_geofunc.cc
        * GIS bugs fixed.
      * sql/item\_geofunc.h
        * GIS bugs fixed.
      * sql/spatial.cc
        * GIS bugs fixed.
  * [Revision #2978.3.27](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.27)\
    Wed 2011-09-21 13:26:21 +0500
    * [Bug #855336](https://bugs.launchpad.net/bugs/855336) ST\_LENGTH does not work on GEOMETRYCOLLECTIONs fixed.
    * per-file comments:
      * mysql-test/r/gis.result
        * [Bug #855336](https://bugs.launchpad.net/bugs/855336) ST\_LENGTH does not work on GEOMETRYCOLLECTIONs fixed.
        * test result updated.
      * mysql-test/t/gis.test
        * [Bug #855336](https://bugs.launchpad.net/bugs/855336) ST\_LENGTH does not work on GEOMETRYCOLLECTIONs fixed.
        * test case added.
      * sql/item\_geofunc.cc
        * [Bug #855336](https://bugs.launchpad.net/bugs/855336) ST\_LENGTH does not work on GEOMETRYCOLLECTIONs fixed.
        * geom\_length() call fixed.
      * sql/spatial.cc
        * [Bug #855336](https://bugs.launchpad.net/bugs/855336) ST\_LENGTH does not work on GEOMETRYCOLLECTIONs fixed.
        * Geometry\_collection::geom\_length implemented.
      * sql/spatial.h
        * [Bug #855336](https://bugs.launchpad.net/bugs/855336) ST\_LENGTH does not work on GEOMETRYCOLLECTIONs fixed.
        * Geometry\_collection::geom\_length declaration added.
  * [Revision #2978.3.26](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.26)\
    Wed 2011-09-21 12:50:03 +0500
    * fix for [Bug #848926](https://bugs.launchpad.net/bugs/848926) GIS functions return "GEOMETRYCOLLECTION()" instead of "GEOMETRYCOLLECTION EMPTY"
    * per-file comments:
      * mysql-test/r/gis.result
        * fix for [Bug #848926](https://bugs.launchpad.net/bugs/848926) GIS functions return "GEOMETRYCOLLECTION()" instead of "GEOMETRYCOLLECTION EMPTY"
        * test result updated.
      * mysql-test/t/gis.test
        * fix for [Bug #848926](https://bugs.launchpad.net/bugs/848926) GIS functions return "GEOMETRYCOLLECTION()" instead of "GEOMETRYCOLLECTION EMPTY"
        * test case added.
      * sql/gstream.cc
        * fix for [Bug #848926](https://bugs.launchpad.net/bugs/848926) GIS functions return "GEOMETRYCOLLECTION()" instead of "GEOMETRYCOLLECTION EMPTY"
        * lookup\_next\_word() implemented.
      * sql/gstream.h
        * fix for [Bug #848926](https://bugs.launchpad.net/bugs/848926) GIS functions return "GEOMETRYCOLLECTION()" instead of "GEOMETRYCOLLECTION EMPTY"
        * lookup\_next\_word() added.
      * sql/spatial.cc
        * fix for [Bug #848926](https://bugs.launchpad.net/bugs/848926) GIS functions return "GEOMETRYCOLLECTION()" instead of "GEOMETRYCOLLECTION EMPTY"
        * name changed for the empty geometry.
      * sql/spatial.h
        * fix for [Bug #848926](https://bugs.launchpad.net/bugs/848926) GIS functions return "GEOMETRYCOLLECTION()" instead of "GEOMETRYCOLLECTION EMPTY"
        * declarations modified.
  * [Revision #2978.3.25](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.25)\
    Wed 2011-09-21 09:29:37 +0500
    * bugs fixed
      * [Bug #855253](https://bugs.launchpad.net/bugs/855253) Compiler error: gcalc\_slicescan.cc:2036: error: suggest parentheses around comparison in operand of .|. in maria-5.3-gis
      * [Bug #850775](https://bugs.launchpad.net/bugs/850775) ST\_AREA does not work on GEOMETRYCOLLECTIONs in maria-5.3-gis
    * per-file comments:
      * mysql-test/r/gis.result
        * test result updated.
      * mysql-test/t/gis.test
        * test case added for 850775.
      * sql/gcalc\_slicescan.cc
        * compiler error fixed.
      * sql/spatial.cc
        * ST\_AREA implementation for GEOMETRY\_COLLECTION, POINT and LINESTRING.
      * sql/spatial.h
        * area() declarations added.
  * [Revision #2978.3.24](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.24)\
    Wed 2011-09-21 00:04:41 +0500
    * several bugs fixed here.
      * [Bug #849789](https://bugs.launchpad.net/bugs/849789) Second assertion \`m\_poly\_borders->next' failed in Gcalc\_operation\_reducer::count\_slice in maria-5.3-gis
      * [Bug #849791](https://bugs.launchpad.net/bugs/849791) Fourth assertion \`n > 0 && n < SINUSES\_CALCULATED\*2+1' in get\_n\_sincos
      * [Bug #849789](https://bugs.launchpad.net/bugs/849789) Second assertion \`m\_poly\_borders->next' failed in Gcalc\_operation\_reducer::count\_slice in maria-5.3-gis
      * [Bug #848901](https://bugs.launchpad.net/bugs/848901) Assertion \`fabs(cur\_isc->x-m\_cur\_intersection->x) + fabs(cur\_isc->y-m\_cur\_intersection->y) < 0.000000000001' failed in Gcalc\_scan\_iterator::intersection\_scan() in maria-5.3-gis
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * test result updated.
      * mysql-test/r/gis.result
        * test result updated.
      * sql/gcalc\_slicescan.cc
        * bugfixes.
      * sql/gcalc\_slicescan.h
        * bugfixes.
      * sql/gcalc\_tools.cc
        * bugfixes.
      * sql/gcalc\_tools.h
        * bugfixes.
      * sql/item\_geofunc.cc
        * bugfixes.
      * sql/spatial.cc
        * bugfixes.
  * [Revision #2978.3.23](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.23)\
    Tue 2011-09-13 18:26:16 +0500
    * Fix for [Bug #848939](https://bugs.launchpad.net/bugs/848939) Wrong result with `ST_INTERSECTION` between linestrings and a polygon in 5.3-gis
      * Coordinates were mistakenly reversed for MULTIPOINT.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * Fix for [Bug #848939](https://bugs.launchpad.net/bugs/848939) Wrong result with ST\_INTERSECTION between linestrings and a polygon in 5.3-gis
        * test result updated.
      * mysql-test/t/gis-precise.test
        * Fix for [Bug #848939](https://bugs.launchpad.net/bugs/848939) Wrong result with ST\_INTERSECTION between linestrings and a polygon in 5.3-gis
        * test case added.
      * sql/gcalc\_tools.cc
        * Fix for [Bug #848939](https://bugs.launchpad.net/bugs/848939) Wrong result with ST\_INTERSECTION between linestrings and a polygon in 5.3-gis
        * coordinates set in the proper order.
  * [Revision #2978.3.22](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.22)\
    Tue 2011-09-13 15:19:55 +0500
    * Fix for [Bug #848901](https://bugs.launchpad.net/bugs/848901) Assertion \`fabs(cur\_isc->x-m\_cur\_intersection->x) + fabs(cur\_isc->y-m\_cur\_intersection->y) < 0.000000000001' failed in Gcalc\_scan\_iterator::intersection\_scan() in maria-5.3-gis
    * That assertion's check was too tight. Released it a bit.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * Fix for [Bug #848901](https://bugs.launchpad.net/bugs/848901)
        * test result updated.
      * mysql-test/t/gis-precise.test
        * Fix for [Bug #848901](https://bugs.launchpad.net/bugs/848901)
        * test case added.
      * sql/gcalc\_slicescan.cc
        * Fix for [Bug #848901](https://bugs.launchpad.net/bugs/848901)
        * The DBUG\_ASSERT check is too tight here.
  * [Revision #2978.3.21](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.21)\
    Tue 2011-09-13 13:59:11 +0500
    * Fix for few similar bugs:
      * [Bug #841622](https://bugs.launchpad.net/bugs/841622) Assertion \`t->rp->type == Gcalc\_function::shape\_line' failed in Gcalc\_operation\_reducer::end\_line in maria-5.3-gi
      * [Bug #841625](https://bugs.launchpad.net/bugs/841625) Assertion \`m\_poly\_borders->next' failed in Gcalc\_operation\_reducer::count\_slice in maria-5.3-gis
      * [Bug #841638](https://bugs.launchpad.net/bugs/841638) Assertion \`!m\_prev || m\_prev->x != x || m\_prev->y != y' failed in Gcalc\_shape\_transporter::int\_add\_point in maria-5.3-gis
      * [Bug #841662](https://bugs.launchpad.net/bugs/841662) Third assertion \`n > 0 && n < SINUSES\_CALCULATED\*2+1' in get\_n\_sincos
      * [Bug #841745](https://bugs.launchpad.net/bugs/841745) Assertion \`!sp0->is\_bottom()' failed in Gcalc\_scan\_iterator::find\_intersections in maria-5.3-gis
    * They mostly was caused by inprecision of double arithmetic.
      * Fixed by changes in how to handle multiple intersections to keep their order right.
      * Also ST\_DISTANCE(GEOM, EMPTY\_GEOM) was defined as NULL.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * GIS bugfixes.
          * test result updated.
      * mysql-test/t/gis-precise.test
        * GIS bugfixes.
          * test cases added.
      * sql/gcalc\_slicescan.cc
        * GIS bugfixes.
          * If intersections are close, add order checks to cope with the\
            double calcualtions imprecision.
      * sql/gcalc\_slicescan.h
        * GIS bugfixes.
          * n\_row parameter added to intersection to check their order.
      * sql/item\_geofunc.cc
        * GIS bugfixes.
          * ST\_DISTANCE(GEOM, EMPTY\_GEOM) returns NULL.
  * [Revision #2978.3.20](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.20)\
    Mon 2011-09-05 09:49:46 +0500
    * [Bug #839327](https://bugs.launchpad.net/bugs/839327) Crash in Gcalc\_operation\_reducer::end\_couple with ST\_UNION and MULTIPOLYGONs in 5.3-gis.
    * When edges of a polygon coicide, it can form an pike, that is turned into a line after an operation.
    * In this case a former polygon point can be an end of a single line, and that case wasn't properly handled.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * [Bug #839327](https://bugs.launchpad.net/bugs/839327) Crash in Gcalc\_operation\_reducer::end\_couple with ST\_UNION and MULTIPOLYGONs in 5.3-gis.
          * test result updated.
      * mysql-test/t/gis-precise.test
        * [Bug #839327](https://bugs.launchpad.net/bugs/839327) Crash in Gcalc\_operation\_reducer::end\_couple with ST\_UNION and MULTIPOLYGONs in 5.3-gis.
          * test case added.
      * sql/gcalc\_tools.cc
        * [Bug #839327](https://bugs.launchpad.net/bugs/839327) Crash in Gcalc\_operation\_reducer::end\_couple with ST\_UNION and MULTIPOLYGONs in 5.3-gis.
          * in the scev\_two\_ends case check if we have single line ending on a polygon node.
  * [Revision #2978.3.19](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.19)\
    Mon 2011-09-05 09:13:58 +0500
    * [Bug #839318](https://bugs.launchpad.net/bugs/839318) Crash in Gcalc\_scan\_iterator::point::get\_shape with ST\_DISTANCE and MULTILINESTRING in maria-5.3-gis.
      * wrong variable was used as a result of inattentive copypaste.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * [Bug #839318](https://bugs.launchpad.net/bugs/839318) Crash in Gcalc\_scan\_iterator::point::get\_shape with ST\_DISTANCE and MULTILINESTRING in maria-5.3-gis.
        * test result updated.
      * mysql-test/t/gis-precise.test
        * [Bug #839318](https://bugs.launchpad.net/bugs/839318) Crash in Gcalc\_scan\_iterator::point::get\_shape with ST\_DISTANCE and MULTILINESTRING in maria-5.3-gis.
        * test case added.
      * sql/item\_geofunc.cc
        * [Bug #839318](https://bugs.launchpad.net/bugs/839318) Crash in Gcalc\_scan\_iterator::point::get\_shape with ST\_DISTANCE and MULTILINESTRING in maria-5.3-gis.
        * use 'ev' variable instead of the 'evpos'.
  * [Revision #2978.3.18](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.18)\
    Sun 2011-09-04 23:48:17 +0500
    * [Bug #839341](https://bugs.launchpad.net/bugs/839341) 100% CPU usage with ST\_UNION in maria-5.3-gis.
      * Line loops weren't recognized when collect results.
      * Fixed by checking if we got the same beginning point of the line.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * [Bug #839341](https://bugs.launchpad.net/bugs/839341) 100% CPU usage with ST\_UNION in maria-5.3-gis.
        * test result updated.
      * mysql-test/t/gis-precise.test
        * [Bug #839341](https://bugs.launchpad.net/bugs/839341) 100% CPU usage with ST\_UNION in maria-5.3-gis.
        * test case added.
      * sql/gcalc\_tools.cc
        * [Bug #839341](https://bugs.launchpad.net/bugs/839341) 100% CPU usage with ST\_UNION in maria-5.3-gis.
        * check if we get the beginning node of the linestring, then cut the loop.
  * [Revision #2978.3.17](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.17)\
    Sun 2011-09-04 19:11:04 +0500
    * [Bug #801466](https://bugs.launchpad.net/bugs/801466) ST\_INTERSECTION() returns invalid value on empty intersection in maria-5.3-gis.
      * We didn't implement an empty geometry. And returning NULL instead of it is not\
        quite correct. So here is the implementation of the empty value as GEOMETRYCOLLECTION().
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * [Bug #801466](https://bugs.launchpad.net/bugs/801466) ST\_INTERSECTION() returns invalid value on empty intersection in maria-5.3-gis.
          * test result updated.
      * mysql-test/r/gis.result
        * [Bug #801466](https://bugs.launchpad.net/bugs/801466) ST\_INTERSECTION() returns invalid value on empty intersection in maria-5.3-gis.
          * test result updated.
      * mysql-test/t/gis-precise.test
        * [Bug #801466](https://bugs.launchpad.net/bugs/801466) ST\_INTERSECTION() returns invalid value on empty intersection in maria-5.3-gis.
          * test case added.
      * mysql-test/t/gis.test
        * [Bug #801466](https://bugs.launchpad.net/bugs/801466) ST\_INTERSECTION() returns invalid value on empty intersection in maria-5.3-gis.
          * test case added.
      * sql/field.cc
        * [Bug #801466](https://bugs.launchpad.net/bugs/801466) ST\_INTERSECTION() returns invalid value on empty intersection in maria-5.3-gis.
          * store GEOMETRYCOLLECTION() properly.
      * sql/gcalc\_tools.cc
        * [Bug #801466](https://bugs.launchpad.net/bugs/801466) ST\_INTERSECTION() returns invalid value on empty intersection in maria-5.3-gis.
          * create the GEOMETRYCOLLECTION() for the empty result.
      * sql/gstream.h
        * [Bug #801466](https://bugs.launchpad.net/bugs/801466) ST\_INTERSECTION() returns invalid value on empty intersection in maria-5.3-gis.
          * next\_symbol() added.
      * sql/spatial.cc
        * [Bug #801466](https://bugs.launchpad.net/bugs/801466) ST\_INTERSECTION() returns invalid value on empty intersection in maria-5.3-gis.
          * code modified to handle 0 geometries in the GEOMETRYCOLLECTION properly.
  * [Revision #2978.3.16](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.16)\
    Fri 2011-09-02 09:38:17 +0500
    * [Bug #801560](https://bugs.launchpad.net/bugs/801560) and [Bug #802194](https://bugs.launchpad.net/bugs/802194)
      * tests added.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * [Bug #801560](https://bugs.launchpad.net/bugs/801560) and [Bug #802194](https://bugs.launchpad.net/bugs/802194)
          * test result updated.
      * mysql-test/t/gis-precise.test
        * [Bug #801560](https://bugs.launchpad.net/bugs/801560) and [Bug #802194](https://bugs.launchpad.net/bugs/802194)
          * test case added.
  * [Revision #2978.3.15](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.15)\
    Thu 2011-09-01 11:44:56 +0500
    * PostGIS-style 'same point' handling.
  * [Revision #2978.3.14](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.14)\
    Wed 2011-07-13 14:57:27 +0500
    * Fix for [Bug #804266](https://bugs.launchpad.net/bugs/804266) Memory corruption/valgrind warning/crash in move\_hole() with ST\_UNION.
    * Second smaller hole in the polygon got link to the bigger one as it's the\
      outer ring. Fixed by specifying the outer ring explicitly.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * Fix for [Bug #804266](https://bugs.launchpad.net/bugs/804266) Memory corruption/valgrind warning/crash in move\_hole() with ST\_UNION.
          * test result updated.
      * mysql-test/t/gis-precise.test
        * Fix for [Bug #804266](https://bugs.launchpad.net/bugs/804266) Memory corruption/valgrind warning/crash in move\_hole() with ST\_UNION.
          * test case added.
      * sql/gcalc\_tools.cc
        * Fix for [Bug #804266](https://bugs.launchpad.net/bugs/804266) Memory corruption/valgrind warning/crash in move\_hole() with ST\_UNION.
          * specify the outer ring explicitly in the get\_polygon\_result parameter.
      * sql/gcalc\_tools.h
        * Fix for [Bug #804266](https://bugs.launchpad.net/bugs/804266) Memory corruption/valgrind warning/crash in move\_hole() with ST\_UNION.
          * add the outer ring as a parameter to the get\_polygon\_result.
  * [Revision #2978.3.13](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.13)\
    Tue 2011-07-12 11:21:20 +0500
    * Fix for [Bug #801217](https://bugs.launchpad.net/bugs/801217) Assertion \`t1->result\_range' in Gcalc\_operation\_reducer::end\_couple.
      * We cannot cut a line from a polygon. So if the polygon fits the condition, and\
        the intersection of a line and the polygon doesn't, we just skip the line.
      * That rule wasn't applied if the line start was inside the polygon, which leaded\
        to the assertion.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * Fix for [Bug #801217](https://bugs.launchpad.net/bugs/801217) Assertion \`t1->result\_range' in Gcalc\_operation\_reducer::end\_couple.
          * test result updated.
      * mysql-test/t/gis-precise.test
        * Fix for [Bug #801217](https://bugs.launchpad.net/bugs/801217) Assertion \`t1->result\_range' in Gcalc\_operation\_reducer::end\_couple.
          * test case added.
      * sql/gcalc\_tools.cc
        * Fix for [Bug #801217](https://bugs.launchpad.net/bugs/801217) Assertion \`t1->result\_range' in Gcalc\_operation\_reducer::end\_couple.
          * Don't mark the line as a border if it's inside a polygon that fits the result condition.
  * [Revision #2978.3.12](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.12)\
    Fri 2011-07-08 15:38:15 +0500
    * Fix for [Bug #804259](https://bugs.launchpad.net/bugs/804259) Second assertion in Gis\_geometry\_collection::init\_from\_opresult.
      * A polygon has no right to have holes that are actually points.
      * So just skip them when we collect the result of an operation.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * Fix for [Bug #804259](https://bugs.launchpad.net/bugs/804259) Second assertion in Gis\_geometry\_collection::init\_from\_opresult.
          * test result updated.
      * mysql-test/t/gis-precise.test
        * Fix for [Bug #804259](https://bugs.launchpad.net/bugs/804259) Second assertion in Gis\_geometry\_collection::init\_from\_opresult.
          * test case added.
      * sql/gcalc\_tools.cc
        * Fix for [Bug #804259](https://bugs.launchpad.net/bugs/804259) Second assertion in Gis\_geometry\_collection::init\_from\_opresult.
          * Skip the point in the result if it's the hole inside a polygon.
  * [Revision #2978.3.11](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.11)\
    Thu 2011-07-07 21:30:51 +0500
    * Fix for [Bug #805860](https://bugs.launchpad.net/bugs/805860) Second assertion Assertion \`n > 0 && n < SINUSES\_CALCULATED\*2+1' in get\_n\_sincos.
      * Just typo-style mistake. Should be '||' instead of '&&'.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * Fix for [Bug #805860](https://bugs.launchpad.net/bugs/805860) Second assertion Assertion \`n > 0 && n < SINUSES\_CALCULATED\*2+1' in get\_n\_sincos.
          * test result updated.
      * mysql-test/t/gis-precise.test
        * Fix for [Bug #805860](https://bugs.launchpad.net/bugs/805860) Second assertion Assertion \`n > 0 && n < SINUSES\_CALCULATED\*2+1' in get\_n\_sincos.
          * test case added.
      * sql/item\_geofunc.cc
        * Fix for [Bug #805860](https://bugs.launchpad.net/bugs/805860) Second assertion Assertion \`n > 0 && n < SINUSES\_CALCULATED\*2+1' in get\_n\_sincos.
          * condition fixed.
  * [Revision #2978.3.10](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.10)\
    Thu 2011-07-07 16:59:45 +0500
    * Fix for [Bug #804324](https://bugs.launchpad.net/bugs/804324) Assertion 0 in Gcalc\_scan\_iterator::pop\_suitable\_intersection
      * There were actually two bugs. One was when the line that intersects itself\
        the intersection point treated as it doesn't belong to the line.
      * Second when edges partly coincide, wrong result produced when we try to find their\
        intersection.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * Fix for [Bug #804324](https://bugs.launchpad.net/bugs/804324) Assertion 0 in Gcalc\_scan\_iterator::pop\_suitable\_intersection
          * test result updated.
      * mysql-test/t/gis-precise.test
        * Fix for [Bug #804324](https://bugs.launchpad.net/bugs/804324) Assertion 0 in Gcalc\_scan\_iterator::pop\_suitable\_intersection
          * test case added.
      * sql/gcalc\_slicescan.cc
        * Fix for [Bug #804324](https://bugs.launchpad.net/bugs/804324) Assertion 0 in Gcalc\_scan\_iterator::pop\_suitable\_intersection
          * skip the intersection if it just line that intersects itself.
      * sql/gcalc\_tools.cc
        * Fix for [Bug #804324](https://bugs.launchpad.net/bugs/804324) Assertion 0 in Gcalc\_scan\_iterator::pop\_suitable\_intersection
          * if edges coincide, just pick the first coinciding poing as an intersection.
  * [Revision #2978.3.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.9)\
    Tue 2011-07-05 19:42:35 +0500
    * [Bug #804305](https://bugs.launchpad.net/bugs/804305) Crash in wkb\_get\_double with ST\_INTERSECTION.
    * That crash happened with the complicated topology of the result.
    * If we found a hole in a polygon whose outside border was already\
      found, we need to paste the hole right after it and respectively\
      shift polygons after it. Also we need to update poly\_position fields\
      in these polygons. That last thing wasn't properly done that led to the\
      crash.
    * To fix that we keep the list of the found polygons and update the\
      poly\_positions that are bigger or equal to where we placed the next hole.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * [Bug #804305](https://bugs.launchpad.net/bugs/804305) Crash in wkb\_get\_double with ST\_INTERSECTION.
          * test result updated.
      * mysql-test/t/gis-precise.test
        * [Bug #804305](https://bugs.launchpad.net/bugs/804305) Crash in wkb\_get\_double with ST\_INTERSECTION.
          * test result added.
      * sql/gcalc\_tools.cc
        * [Bug #804305](https://bugs.launchpad.net/bugs/804305) Crash in wkb\_get\_double with ST\_INTERSECTION.
          * keep the list of the found polygons and update their poly\_position fields respectively.
      * sql/gcalc\_tools.h
        * [Bug #804305](https://bugs.launchpad.net/bugs/804305) Crash in wkb\_get\_double with ST\_INTERSECTION.
          * Gcalc\_result\_receiver::move\_hole interface changed.
  * [Revision #2978.3.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.8)\
    Mon 2011-07-04 16:17:34 +0500
    * fix for [Bug #801212](https://bugs.launchpad.net/bugs/801212) Assertion with ST\_INTERSECTION on NULL values
      * The ::val\_str() method has to return NULL if it calculated\
        the null\_value, not just set the related flag.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * fix for [Bug #801212](https://bugs.launchpad.net/bugs/801212) Assertion with ST\_INTERSECTION on NULL values
          * test result updated.
      * mysql-test/t/gis-precise.test
        * fix for [Bug #801212](https://bugs.launchpad.net/bugs/801212) Assertion with ST\_INTERSECTION on NULL values
          * test case added.
      * sql/item\_geofunc.cc
        * fix for [Bug #801212](https://bugs.launchpad.net/bugs/801212) Assertion with ST\_INTERSECTION on NULL values
          * return NULL from the val\_str if we get the null\_value.
  * [Revision #2978.3.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.7)\
    Mon 2011-07-04 16:03:36 +0500
    * [Bug #801199](https://bugs.launchpad.net/bugs/801199) Infinite recursion in Gcalc\_function::count\_internal with ST\_BUFFER over MULTIPOINT
      * Collections were treated mistakenly, so the counter for the final UNION operation\
        received the wrong value.
      * As a fix we implement Item\_func\_buffer::Transporter::start\_collection() method,\
        where we set the proper operation and the operand counter.\
        start\_poly() and start\_line() were also modified to function correctly for the\
        polygon as a part of a collection.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * [Bug #801199](https://bugs.launchpad.net/bugs/801199) Infinite recursion in Gcalc\_function::count\_internal with ST\_BUFFER over MULTIPOINT
          * test result updated.
      * mysql-test/t/gis-precise.test
        * [Bug #801199](https://bugs.launchpad.net/bugs/801199) Infinite recursion in Gcalc\_function::count\_internal with ST\_BUFFER over MULTIPOINT
          * test case added.
      * sql/item\_geofunc.cc
        * [Bug #801199](https://bugs.launchpad.net/bugs/801199) Infinite recursion in Gcalc\_function::count\_internal with ST\_BUFFER over MULTIPOINT
          * start\_collection() implemented.
      * sql/item\_geofunc.h
        * [Bug #801199](https://bugs.launchpad.net/bugs/801199) Infinite recursion in Gcalc\_function::count\_internal with ST\_BUFFER over MULTIPOINT
          * Item\_func\_buffer::Transporter::start\_collection() defined.
  * [Revision #2978.3.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.6)\
    Thu 2011-06-30 19:24:52 +0500
    * fix for [Bug #201189](https://bugs.launchpad.net/bugs/201189) ST\_BUFFER asserts if radius = 0.
      * Internal caclucations can't handle zero distance properly.
      * As the ST\_BUFFER(geom, 0) is in fact NOOP, we'll just return the
        * 'geom' as the result here.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * fix for [Bug #201189](https://bugs.launchpad.net/bugs/201189) ST\_BUFFER asserts if radius = 0.
          * test result updated.
      * mysql-test/t/gis-precise.test
        * fix for [Bug #201189](https://bugs.launchpad.net/bugs/201189) ST\_BUFFER asserts if radius = 0.
          * test case added.
      * sql/item\_geofunc.cc
        * fix for [Bug #201189](https://bugs.launchpad.net/bugs/201189) ST\_BUFFER asserts if radius = 0.
          * return the first argument as the result of the ST\_BUFFER, if\
            the distance is 0 there.
  * [Revision #2978.3.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.5)\
    Thu 2011-06-30 18:18:27 +0500
    * fix for [Bug #801243](https://bugs.launchpad.net/bugs/801243) Assertion \`(0)' failed in Gis\_geometry\_collection::init\_from\_opresult on ST\_UNION
      * If the result contains a polygon with a hole, consequitive shapes weren't calculated\
        properly, as the hole appeared as shape in the result, but actually it's a single shape\
        with the surrounding polygon. It's more natural to use the size of the result as\
        a border instead of the number of resulting shapes.
    * per-file comments:
      * mysql-test/r/gis-precise.result
        * fix for [Bug #801243](https://bugs.launchpad.net/bugs/801243) Assertion \`(0)' failed in Gis\_geometry\_collection::init\_from\_opresult on ST\_UNION
        * test result updated.
      * mysql-test/t/gis-precise.test
        * fix for [Bug #801243](https://bugs.launchpad.net/bugs/801243) Assertion \`(0)' failed in Gis\_geometry\_collection::init\_from\_opresult on ST\_UNION
        * test case added.
      * sql/spatial.cc
        * fix for [Bug #801243](https://bugs.launchpad.net/bugs/801243) Assertion \`(0)' failed in Gis\_geometry\_collection::init\_from\_opresult on ST\_UNION
        * check the data lenght instead of number of shapes.
      * sql/spatial.h
        * fix for [Bug #801243](https://bugs.launchpad.net/bugs/801243) Assertion \`(0)' failed in Gis\_geometry\_collection::init\_from\_opresult on ST\_UNION
        * check the data lenght instead of number of shapes.
  * [Revision #2978.3.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.4) \[merge]\
    Mon 2011-06-20 00:21:41 +0500
    * gis-related tests fixes.
    * merging.
    * [Revision #2978.3.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.3)\
      Tue 2011-06-14 11:20:48 +0500
      * Precision spatial function tests added.
    * [Revision #2978.3.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.2)\
      Thu 2011-05-05 14:30:59 +0500
      * forgotten h-files added to the NOINST\_HEADERS
    * [Revision #2978.3.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978.3.1)\
      Wed 2011-05-04 23:20:17 +0500
      * Precise GIS functions added.
* [Revision #3287](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3287)\
  Thu 2011-11-17 01:00:46 -0800
  * Fixed [Bug #891052](https://bugs.launchpad.net/bugs/891052).
  * Some optimizer switches were missing in the help lists of mysqld.
* [Revision #3286](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3286)\
  Thu 2011-11-17 01:25:10 +0200
  * Fix [Bug #869036](https://bugs.launchpad.net/bugs/869036)
  * Apart from the fix, the patch also adds few more unrelated test\
    cases for partial matching, and fixes few typos.
  * Analysis:
    * This bug uncovered that partial matching via rowid intersection\
      didn't handle the case when:
      * the left IN argument has some NULLs,
      * there are no non-null value matches, and there is no non-null\
        column,
      * the subquery columns that are not covered with the NULLs in\
        the left IN argument contain at least one row, such that it\
        has NULL values in all columns where the left IN operand has\
        no NULLs.
    * In this case there is a partial match.
    * In addition the analysis of the related code uncovered incorrect\
      handling of few other related cases.
  * Solution:
    * The solution for the bug is to check if there exists a row with\
      NULLs in all columns other than the ones having NULL in the\
      let IN operand.
    * The check is implemented via checking whether the bitmaps that\
      store NULL information in class Ordered\_key have a non-empty\
      intersection for the relevant columns.
    * The intersection itself is implemented via the function\
      bitmap\_exists\_intersection() in my\_bitmap.c.
* [Revision #3285](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3285)\
  Wed 2011-11-16 06:11:25 -0800
  * Fixed [Bug #887479](https://bugs.launchpad.net/bugs/887479).
  * The function setup\_semijoin\_dups\_elimination erroneously assumed\
    that if join\_cache\_level is set to 3 or 4 then the type of the\
    access to a table cannot be JT\_REF or JT\_EQ\_REF. This could lead\
    to wrong query result sets.
* [Revision #3284](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3284) \[merge]\
  Tue 2011-11-15 14:35:36 -0800
  * Merge.
  * [Revision #3278.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3278.1.1)\
    Tue 2011-11-15 13:03:00 -0800
    * Fixed [Bug #889750](https://bugs.launchpad.net/bugs/889750).
    * If the optimizer switch 'semijoin\_with\_cache' is set to 'off' then\
      join cache cannot be used to join inner tables of a semijoin.
    * Also fixed a bug in the function check\_join\_cache\_usage() that led\
      to wrong output of the EXPLAIN commands for some test cases.
* [Revision #3283](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3283)\
  Mon 2011-11-14 19:24:36 +0200
  * Fix [Bug #889744](https://bugs.launchpad.net/bugs/889744)
  * [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) merges changes from MySQL 5.5 where all constant\
    expressions are wrapped into an Item\_cache. As a result, constant\
    single-row subqueries were also wrapped in an Item\_cache.\
    When analyzing the where clause for constant expressions that\
    can be evaluated during optimization, subqueries wrapped into\
    an Item\_cache did not appear as expensive, and were therefore\
    evaluated during optimization. Such evaluation is against the\
    current architecture of [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md) where subquries are executed\
    during the execute phase.
  * The patch adds the is\_expensive() predicate to Item\_cache.
  * This makes Item\_cache consistent with other wrapping Item\
    classes that need to look at the properties of the wrapped\
    object.
* [Revision #3282](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3282) \[merge]\
  Mon 2011-11-14 00:32:21 +0100
  * 5.2->5.3 merge
  * [Revision #2732.46.16](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.16) \[merge]\
    Sun 2011-11-13 18:41:45 +0100
    * 5.1->5.2 merge
    * [Revision #2643.143.47](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.47)\
      Sun 2011-11-13 13:28:35 +0100
      * don't make feedback\_plugin\_send.test as 'big'
      * don't assume that the http reply packet will arrive in all in one piece
* [Revision #3281](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3281)\
  Sun 2011-11-13 12:02:13 +0200
  * Fix for [Bug #824425](https://bugs.launchpad.net/bugs/824425): Prohibiting subqueries in rows for left part of IN/ALL/ANY
  * Fix for walk() method of subqueries: always call the method on the subquery.
* [Revision #3280](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3280) \[merge]\
  Sun 2011-11-13 09:10:45 +0100
  * 5.2->5.3 merge
  * [Revision #2732.46.15](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.15) \[merge]\
    Sun 2011-11-13 08:30:03 +0100
    * 5.1-5.2 merge
    * [Revision #2643.143.46](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.46)\
      Sat 2011-11-12 18:40:51 +0100
      * increase feedback plugin version
* [Revision #3279](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3279) \[merge]\
  Sat 2011-11-12 18:08:12 +0100
  * 5.2->5.3 merge
  * [Revision #2732.46.14](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.14) \[merge]\
    Sat 2011-11-12 16:47:14 +0100
    * 5.1 merge
    * [Revision #2643.143.45](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.45)\
      Sat 2011-11-12 16:41:00 +0100
      * feedback plugin:
        * fix for mem\_total on windows
        * report the time of the data snapshot
    * [Revision #2643.143.44](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.44)\
      Tue 2011-11-08 23:07:19 +0100
      * typos fixed
        * (thanks viva64.com)
  * [Revision #2732.46.13](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.13) \[merge]\
    Fri 2011-11-04 12:41:27 +0200
    * Merge of gcc 4.6 fixes
    * [Revision #2732.47.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.47.2)\
      Thu 2011-10-27 19:18:25 +0300
      * Fix gcc 4.6 warning after merge with 5.1
    * [Revision #2732.47.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.47.1) \[merge]\
      Thu 2011-10-27 17:51:30 +0300
      * 5.1->5.2 merge (gcc 4.6 warnings and apple hwaddress fixes).
      * [Revision #2643.143.43](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.43)\
        Thu 2011-10-27 15:22:52 +0300
        * Fix gcc 4.6 warnings about assigned but not used variables.
        * Fixed my\_gethwaddr.c to allow compilation on Mac OS X.
  * [Revision #2732.46.12](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.12)\
    Tue 2011-11-01 12:36:43 +0400
    * [Bug #884184](https://bugs.launchpad.net/bugs/884184): Wrong result with RIGHT JOIN + derived\_merge
      *   Make eliminate\_tables\_for\_list() take into account that it is not possible\
          to eliminate a table if it is used in the upper-side ON expressions. Example:

          ```
          xxx JOIN (t1 LEFT JOIN t2 ON cond ) ON func(t2.columns)
          ```
      * Here it would eliminate t2 which is not possible because of use of t2.columns.
* [Revision #3278](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3278) \[merge]\
  Sat 2011-11-12 03:57:46 -0800
  * Merge.
  * [Revision #3148.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3148.1.1)\
    Sat 2011-11-12 02:20:44 -0800
    * Fixed [Bug #823301](https://bugs.launchpad.net/bugs/823301)
    * A bug in the code of the function key\_or could lead to a situation\
      when performing of an OR operation for one index changes the result\
      the operation for another index. This bug is fixed with this patch.
    * Also corrected the specification and the code of the function\
      or\_sel\_tree\_with\_checks.
* [Revision #3277](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3277)\
  Sat 2011-11-12 12:03:27 +0200
  * Remove unused variable detected by GCC 4.6.1.
* [Revision #3276](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3276)\
  Sat 2011-11-12 11:29:12 +0200
  * Fix [MySQL Bug #12329653](https://bugs.mysql.com/bug.php?id=12329653)
    * In MariaDB, when running in ONLY\_FULL\_GROUP\_BY mode,\
      the server produced in incorrect error message that there\
      is an aggregate function without GROUP BY, for artificially\
      created MIN/MAX functions during subquery MIN/MAX optimization.
    * The fix introduces a way to distinguish between artifially\
      created MIN/MAX functions as a result of a rewrite, and normal\
      ones present in the query. The test for ONLY\_FULL\_GROUP\_BY violation\
      now tests in addition if a MIN/MAX function was part of a MIN/MAX\
      subquery rewrite.
    * In order to be able to distinguish these MIN/MAX functions, the\
      patch introduces an additional flag in Item\_in\_subselect::in\_strategy -\
      SUBS\_STRATEGY\_CHOSEN. This flag is set when the optimizer makes its\
      final choice of a subuqery strategy. In order to make the choice\
      consistent, access to Item\_in\_subselect::in\_strategy is provided\
      via new class methods.
  * Fix [MySQL Bug #12329653](https://bugs.mysql.com/bug.php?id=12329653)
    * In MariaDB, when running in ONLY\_FULL\_GROUP\_BY mode,\
      the server produced in incorrect error message that there\
      is an aggregate function without GROUP BY, for artificially\
      created MIN/MAX functions during subquery MIN/MAX optimization.
    * The fix introduces a way to distinguish between artifially\
      created MIN/MAX functions as a result of a rewrite, and normal\
      ones present in the query. The test for ONLY\_FULL\_GROUP\_BY violation\
      now tests in addition if a MIN/MAX function was part of a MIN/MAX\
      subquery rewrite.
    * In order to be able to distinguish these MIN/MAX functions, the\
      patch introduces an additional flag in Item\_in\_subselect::in\_strategy -\
      SUBS\_STRATEGY\_CHOSEN. This flag is set when the optimizer makes its\
      final choice of a subuqery strategy. In order to make the choice\
      consistent, access to Item\_in\_subselect::in\_strategy is provided\
      via new class methods.
* [Revision #3275](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3275)\
  Fri 2011-11-11 14:53:26 -0800
  * Fixed [Bug #879871](https://bugs.launchpad.net/bugs/879871)
  * The function add\_ref\_to\_table\_cond missed updating the value of\
    join\_tab->pre\_idx\_push\_select\_cond after having updated the value\
    of join\_tab->select->pre\_idx\_push\_select\_cond.
* [Revision #3274](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3274) \[merge]\
  Thu 2011-11-10 13:28:02 -0800
  * Merge of the maria-5.3-icp tree into the 5.3 tree
  * [Revision #3256.1.16](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.16) \[merge]\
    Tue 2011-11-08 08:04:48 -0800
    * Merge.
  * [Revision #3256.1.15](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.15)\
    Mon 2011-11-07 23:30:03 +0400
    * [Bug #887026](https://bugs.launchpad.net/bugs/887026): Wrong result with ICP, outer join, subquery in maria-5.3-icp
      * Do not push index condition if we're using a triggered ref access.
  * [Revision #3256.1.14](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.14) \[merge]\
    Sun 2011-11-06 13:44:59 -0800
    * Merge.
  * [Revision #3256.1.13](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.13)\
    Sun 2011-11-06 01:23:03 -0700
    * Fixed [Bug #886145](https://bugs.launchpad.net/bugs/886145)
    * The bug happened because in some cases the function JOIN::exec\
      did not save the value of TABLE::pre\_idx\_push\_select\_cond in\
      TABLE::select->pre\_idx\_push\_select\_cond for the sort table.
    * Noticed and fixed a bug in the function make\_cond\_remainder\
      that builds the remainder condition after extraction of an index\
      pushdown condition from the where condition. The code\
      erroneously assumed that the function make\_cond\_for\_table left\
      the value of ICP\_COND\_USES\_INDEX\_ONLY in sub-condition markers.
    * Adjusted many result files from the regression test suite\
      after this fix .
  * [Revision #3256.1.12](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.12)\
    Fri 2011-11-04 05:39:45 -0700
    * Fixed [Bug #885168](https://bugs.launchpad.net/bugs/885168)
    * The call of the virtual function cancel\_pushed\_idx\_cond in the code of\
      the function test\_if\_skip\_sort\_order was misplaced when backporting the\
      fix for [MySQL Bug #58816](https://bugs.mysql.com/bug.php?id=58816)
  * [Revision #3256.1.11](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.11) \[merge]\
    Wed 2011-11-02 01:22:11 -0700
    * Merge.
  * [Revision #3256.1.10](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.10)\
    Tue 2011-11-01 07:00:55 -0700
    * Backported the fix and the test case for [MySQL Bug #12822678](https://bugs.mysql.com/bug.php?id=12822678) from the mysql-5.6 code line.
    * Fixed a bug in select\_describe.
    * Adjusted results for affected test cases.
  * [Revision #3256.1.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.9)\
    Mon 2011-10-31 01:36:28 -0700
    * Fixed a compilation error.
  * [Revision #3256.1.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.8)\
    Mon 2011-10-31 01:13:12 -0700
    * Backported the test case for [MySQL Bug #59843](https://bugs.mysql.com/bug.php?id=59843) from the mysql-5.6 code line.
    * (Failed to reproduce the bug in mariadb-5.3).
  * [Revision #3256.1.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.7)\
    Sun 2011-10-30 06:17:07 -0700
    * Backported the fix and the test case for [MySQL Bug #59483](https://bugs.mysql.com/bug.php?id=59483) from the mysql-5.6 code line.
  * [Revision #3256.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.6)\
    Sun 2011-10-30 04:18:09 -0700
    * Backported the test case for [MySQL Bug #58838](https://bugs.mysql.com/bug.php?id=58838) from mysql-5.6 code line.
    * The bug was fixed by the patches for [Bug #668644](https://bugs.launchpad.net/bugs/668644) and [Bug #702322](https://bugs.launchpad.net/bugs/702322) that\
      were applied earlier to the mariadb-5.3 code.
  * [Revision #3256.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.5)\
    Sun 2011-10-30 03:34:26 -0700
    * Backported the test case for [MySQL Bug #59186](https://bugs.mysql.com/bug.php?id=59186) from mysql-5.6 code line.
    * The bug was fixed by the patch for [Bug #694092](https://bugs.launchpad.net/bugs/694092) that was\
      applied earlier to the mariadb-5.3 code.
  * [Revision #3256.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.4)\
    Sun 2011-10-30 02:37:10 -0700
    * Backported the test case for [MySQL Bug #58837](https://bugs.mysql.com/bug.php?id=58837) The fix was backported earlier.
  * [Revision #3256.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.3)\
    Sat 2011-10-29 15:36:24 -0700
    * Backported the fix and the test case for [MySQL Bug #58816](https://bugs.mysql.com/bug.php?id=58816) from mysql-5.6 code line.
  * [Revision #3256.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.2) \[merge]\
    Fri 2011-10-28 05:19:45 -0700
    * Merge.
  * [Revision #3256.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256.1.1) \[merge]\
    Fri 2011-10-28 04:07:11 -0700
    * Merge.
    * [Revision #3015.2.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3015.2.3)\
      Thu 2011-06-02 14:03:02 -0700
      * Applied the patch for [MySQL Bug #58837](https://bugs.mysql.com/bug.php?id=58837) (for the mysql-5.6 code line).
      * This patch fixed the crash in innodb\_bug59307.
    * [Revision #3015.2.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3015.2.2) \[merge]\
      Wed 2011-06-01 20:49:37 -0700
      * Merge.
      * [Revision #2954.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2954.1.6)\
        Wed 2011-06-01 17:41:50 -0700
        * Modified the code backported from mysql 5.6 to make it handle virtual\
          columns as well.
      * [Revision #2954.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2954.1.5)\
        Sun 2011-05-29 11:09:05 -0700
        * Backported the test case for [MySQL Bug #52605](https://bugs.mysql.com/bug.php?id=52605)
      * [Revision #2954.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2954.1.4)\
        Fri 2011-05-27 20:50:06 -0700
        * Backported the test case for [MySQL Bug #52660](https://bugs.mysql.com/bug.php?id=52660) from mysql code line.
        * Extended the test case to show how MariaDB applies ICP for\
          indexes with some components defined on the beginning of fields.
      * [Revision #2954.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2954.1.3)\
        Fri 2011-05-27 17:04:29 -0700
        * Backported the test case for [MySQL Bug #43618](https://bugs.mysql.com/bug.php?id=43618) from mysql code line.
      * [Revision #2954.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2954.1.2)\
        Fri 2011-05-27 15:20:19 -0700
        * Backported the test case for [MySQL Bug #43617](https://bugs.mysql.com/bug.php?id=43617) fixed by the patch for [MySQL Bug #42580](https://bugs.mysql.com/bug.php?id=42580)
        * Backported the test case for [MySQL Bug #49906](https://bugs.mysql.com/bug.php?id=49906) fixed by the patch for [Bug #625841](https://bugs.launchpad.net/bugs/625841)
        * Slightly optimized the code of the fix for [Bug #625841](https://bugs.launchpad.net/bugs/625841)
      * [Revision #2954.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2954.1.1)\
        Wed 2011-05-25 16:01:56 -0700
        * Downported InnoDB support of Index Condition Pushdown from MySQL-5.6 code line.
* [Revision #3273](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3273)\
  Mon 2011-11-07 16:39:02 +0400
  * Make subselect\_extra\_no\_semijoin.test run the tests with semijoin=off,
  * update test results
* [Revision #3272](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3272)\
  Fri 2011-11-04 12:04:12 +0200
  * Fixed that test doesn't abort if 'var' points to a deleted directory (common case when using `--mem`)
  * Better error message if `--log-bin` is used without `--log-bin-index`
* [Revision #3271](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3271)\
  Fri 2011-11-04 10:14:25 +0200
  * Fixed [Bug #884101](https://bugs.launchpad.net/bugs/884101) "Crash in check\_table\_is\_closed with concurrent workload"
* [Revision #3270](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3270)\
  Thu 2011-11-03 13:00:25 +0100
  * rename binlog\_dbug\_fsync\_sleep -> debug\_binlog\_fsync\_sleep
* [Revision #3269](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3269)\
  Thu 2011-11-03 12:59:48 +0100
  * cast.test: use exact double, to be independent from compiler optimizations
* [Revision #3268](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3268) \[merge]\
  Wed 2011-11-02 22:06:22 +0400
  * Merge
  * [Revision #3262.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3262.1.3)\
    Wed 2011-11-02 22:05:08 +0400
    * [Bug #878753](https://bugs.launchpad.net/bugs/878753): Assertion '0' failed in replace\_where\_subcondition with derived\_merge
      * Remove the assert in replace\_where\_subcondition (the patch has explanation why)
* [Revision #3267](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3267)\
  Wed 2011-11-02 20:01:50 +0400
  * Change the default @@optimizer\_switch settings:
    * More test result updates (the errors are the same, the difference is that\
      "at row X" became "at row Y" due to queries with semi-joins producing\
      select results in different order)
* [Revision #3266](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3266)\
  Wed 2011-11-02 19:52:11 +0400
  * Fix "unused variable addr" warning
* [Revision #3265](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3265) \[merge]\
  Wed 2011-11-02 19:37:26 +0400
  * Merge
  * [Revision #3262.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3262.1.2)\
    Wed 2011-11-02 19:36:08 +0400
    * Change the default @@optimizer\_switch settings:
      * More test result updates
* [Revision #3264](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3264) \[merge]\
  Wed 2011-11-02 13:51:47 +0400
  * Merge
  * [Revision #3262.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3262.1.1)\
    Wed 2011-11-02 13:48:41 +0400
    * Change the default @@optimizer\_switch settings:
      * semijoin=on
      * firstmatch=on
      * loosescan=on
* [Revision #3263](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3263) \[merge]\
  Wed 2011-11-02 10:05:07 +0200
  * Merge of [Bug #872775](https://bugs.launchpad.net/bugs/872775) fix
    * [Revision #3248.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3248.1.1)\
      Tue 2011-11-01 17:42:52 +0200
      * Fix of [Bug #872775](https://bugs.launchpad.net/bugs/872775)
      * The problem was that merged views has its own nest\_level numbering =>\
        when we compare nest levels we should take into considiration basis (i.e. 0 level),\
        if it is different then nest levels are not comparable.
* [Revision #3262](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3262)\
  Tue 2011-11-01 18:19:19 +0200
  * Fix [Bug #833702](https://bugs.launchpad.net/bugs/833702)
  * Analysis:
    * Equality propagation propagated the constant '7' into\
      args\[0] of the Item\_in\_optimizer that stands for the\
      "< ANY" predicate. At the same the min/max subquery\
      rewrite swapped the order of the left and right operands\
      of the "<" predicate, but used Item\_in\_subselect::left\_expr.
    * As a result, when the \<ANY predicate is executed early in the\
      execution phase as a contant condition, instead of a constant\
      right (swapped) argument of the < predicate, there was a field\
      (t3.a). This field had no data, since the whole predicate is\
      considered constant, and it is evaluated before any tables are\
      read. Having junk in the field row buffer produced wrong result
  * Solution:
    * Fix create\_swap to pick the correct Item\_in\_optimizer left\
      argument.
* [Revision #3261](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3261)\
  Tue 2011-11-01 13:22:09 +0200
  * Fix of typo.
* [Revision #3260](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3260)\
  Tue 2011-11-01 12:04:11 +0400
  * [Bug #884631](https://bugs.launchpad.net/bugs/884631): Table elimination works 5.3 release builds even if turned off
    * Make table elimination to actually switch itself on/off in release builds.
* [Revision #3259](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3259)\
  Mon 2011-10-31 15:07:43 +0400
  * [Bug #882994](https://bugs.launchpad.net/bugs/882994): Crash in QUICK\_RANGE\_SELECT::reset with derived\_with\_keys
    * The bug was caused by the following scenario:
      * a quick select is created with get\_quick\_select\_for\_ref. The quick\
        select refers to temporary (derived) table. It saves table->file, which\
        refers to a ha\_heap object.
      * When temp table is populated, ha\_heap reaches max. size and is converted\
        to a ha\_myisam. However, quick->file remains pointing to where ha\_heap\
        was.
      * Attempt to use the quick select causes crash.
        * Fixed by introducing QUICK\_SELECT\_I::replace\_handler(). Note that it will\
          not work for index\_merge quick selects. Which is fine, because these\
          quick selects are never created for derived tables.
* [Revision #3258](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3258)\
  Fri 2011-10-28 12:38:36 +0400
  * Let t/myisam\_icp.test run include/icp\_tests.inc with MRR/ICP turned ON (not OFF)
  * Fix the compile-time-default value of optimizer\_switch printed by mysqld `--help --defaults`
* [Revision #3257](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3257)\
  Fri 2011-10-28 11:23:30 +0400
  * Make innodb\_no\_mrricp.test to really run with MRR and ICP turned OFF.
* [Revision #3256](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3256)\
  Thu 2011-10-27 12:03:33 -0700
  * Moved the test case for [Bug #879939](https://bugs.launchpad.net/bugs/879939) to derived\_view.test where it belongs to.
* [Revision #3255](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3255) \[merge]\
  Thu 2011-10-27 09:14:45 -0700
  * Merge.
  * [Revision #3252.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3252.1.1)\
    Thu 2011-10-27 08:32:24 -0700
    * Fixed [Bug #874035](https://bugs.launchpad.net/bugs/874035)
    * The function Item\_direct\_view\_ref::fix\_fields erroneously did not correct\
      the value of the flag maybe\_null when the view for which the item was\
      being fixed happened to be an inner table of an outer join.
* [Revision #3254](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3254)\
  Thu 2011-10-27 13:54:28 +0400
  * [Bug #882472](https://bugs.launchpad.net/bugs/882472): subselect4.test fails in current 5.3
    * The problem was that the value of READ\_RECORD::file was not updated when the underlying table\
      was temporary and was converted from heap to myisam. Resolved by eliminating READ\_RECORD::file,\
      always use READ\_RECORD::table->file
* [Revision #3253](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3253)\
  Wed 2011-10-26 20:25:18 +0300
  * Fixed [Bug #879939](https://bugs.launchpad.net/bugs/879939) "assertion in ha\_maria::enable\_indexes with derived\_with\_keys=on"
  * Honor unique/not unique when creating keys for internal tempory tables.
  * Added new variables to be used to limit how keys are created for internal temporary tables.
* [Revision #3252](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3252)\
  Wed 2011-10-26 04:27:09 -0700
  * Fixed [Bug #881449](https://bugs.launchpad.net/bugs/881449)
  * The function SELECT\_LEX::update\_used\_tables first must clean up\
    all bitmaps to be recalculated for all tables that require it\
    and only after this walk through on conditions attached to the\
    tables to update these bitmaps.
* [Revision #3251](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3251) \[merge]\
  Wed 2011-10-26 10:58:40 +0400
  * Merge fix for [Bug #877288](https://bugs.launchpad.net/bugs/877288)
  * [Revision #3249.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3249.1.1)\
    Wed 2011-10-26 02:38:49 +0400
    * [Bug #877288](https://bugs.launchpad.net/bugs/877288): Wrong result with semijoin + materialization + multipart key
      * when create\_ref\_for\_key() is constructing a ref access for\
        a table that's inside a SJ-Materialization nest, it may not\
        use references to fields of tables that are unside the nest (because\
        these fields will not yet have values when ref access will be used)
      * The check was performed in the first of create\_ref\_for\_key's loops (the\
        one which counts how many key parts are usable) but not in the second\
        (the one which actually fills the TABLE\_REF structure).
* [Revision #3250](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3250)\
  Tue 2011-10-25 14:18:19 -0700
  * Fixed [Bug #881318](https://bugs.launchpad.net/bugs/881318).
  * If a materialized derived table / view is empty then for this table\
    the value of file->ref is 0. This was not taken into account by\
    the function JOIN\_CACHE::write\_record\_data. As a result a query\
    using an empty materialized derived tables as inner tables of outer\
    joins and IN subqueries in WHERE conditions could cause server crashes\
    when the optimizer employed join caches and duplicate elimination for\
    semi-joins.
* [Revision #3249](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3249)\
  Mon 2011-10-24 12:54:28 -0700
  * Fixed [Bug #880724](https://bugs.launchpad.net/bugs/880724)
  * Do not create KEYUSEs for a materialized view over a constant table.
* [Revision #3248](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3248)\
  Sun 2011-10-23 05:46:03 -0700
  * Fixed [Bug #879882](https://bugs.launchpad.net/bugs/879882)
  * This bug happened because the function Item\_cond::eval\_not\_null\_tables\
    erroneously did not initialize the value of not\_null\_tables\_cache.
* [Revision #3247](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3247)\
  Sat 2011-10-22 07:19:43 -0700
  * Fixed [Bug #878769](https://bugs.launchpad.net/bugs/878769)
  * The method DsMrr\_impl::dsmrr\_init erroneously tried to get a KEY descriptor\
    for key with number MAX\_KEY. This caused valgrind complains.
* [Revision #3246](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3246)\
  Sat 2011-10-22 00:14:27 -0700
  * Fixed [Bug #874378](https://bugs.launchpad.net/bugs/874378)
  * This bug happened for the queries over multi-table mergeable views\
    because the bitmap TABLE::read\_set of the underlying tables were not\
    updated after the views had been merged into the query.
  * Now this bitmaps are updated properly.
  * Also the bitmap TABLE::merge\_keys now is updated in prevention of\
    future bugs.
* [Revision #3245](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3245)\
  Thu 2011-10-20 08:02:31 -0700
  * Added a test case for [Bug #873263](https://bugs.launchpad.net/bugs/873263) fixed by the patch for [Bug #874006](https://bugs.launchpad.net/bugs/874006)
* [Revision #3244](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3244)\
  Thu 2011-10-20 04:59:20 -0700
  * Fixed [Bug #878199](https://bugs.launchpad.net/bugs/878199)
  * The function JOIN::drop\_unused\_derived\_keys could erroneously set\
    the value of REF::key to 0 for a joined materialized view/derived table\
    in the case when no REF access to the table was used by the query\
    execution plan. This could cause a crash of the server.
* [Revision #3243](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3243) \[merge]\
  Wed 2011-10-19 23:35:11 -0700
  * Merge.
  * [Revision #3240.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3240.1.1)\
    Wed 2011-10-19 23:28:37 -0700
    * Fixed [Bug #877316](https://bugs.launchpad.net/bugs/877316)
    * This bug happened due to incompleteness of the fix for [Bug #872735](https://bugs.launchpad.net/bugs/872735):\
      the occurrences of the fields in the conditions of correlated\
      subqueries were not taken into account when recalculating\
      covering keys bit maps.
* [Revision #3242](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3242) \[merge]\
  Wed 2011-10-19 21:01:42 +0200
  * merge 5.2
  * [Revision #2732.46.11](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.11) \[merge]\
    Wed 2011-10-19 20:53:16 +0200
    * merge from 5.1
    * [Revision #2643.143.42](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.42)\
      Wed 2011-10-19 20:51:01 +0200
      * Fix endless loop in my\_gethwaddr()
    * [Revision #2643.143.41](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.143.41)\
      Thu 2011-10-13 11:20:33 +0200
      * silence the "uninitialized" warning
  * [Revision #2732.46.10](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.46.10)\
    Sun 2011-10-16 21:55:53 +0300
    * Fixed wrong info message for mysqld `--general-log`
    * Fixed wrong parameter type for `--general-log`. Now one can enable it with `--general-log= 1 | true | on`
    * Fixed that bool parameters can also take 'on' and 'off' as parameters. This is in line with the values assigned to them in mysqld.
* [Revision #3241](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3241)\
  Tue 2011-10-18 22:50:17 +0300
  * Fix of building on Mac OS.
* [Revision #3240](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3240) \[merge]\
  Tue 2011-10-18 14:04:10 +0300
  * merge
  * [Revision #3233.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3233.2.1)\
    Tue 2011-10-18 13:44:12 +0300
    * Compiler warning about assigned but not used variables fixed.
* [Revision #3239](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3239)\
  Mon 2011-10-17 03:42:56 -0700
  * Fixed a compiler warning.
* [Revision #3238](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3238) \[merge]\
  Mon 2011-10-17 01:20:16 -0700
  * Merge.
  * [Revision #3235.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3235.1.1)\
    Sun 2011-10-16 13:23:57 -0700
    * Fixed [Bug #874006](https://bugs.launchpad.net/bugs/874006)
    * This bug manifested itself with queries containing non-correlated\
      IN subqueries over materialized views/derived tables.
    * The bug happened because the code of the function generate\_derived\_keys did\
      not take into account that the function could be called twice when the\
      optimizer was deciding whether in-exist transformation should be applied.
* [Revision #3237](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3237)\
  Sun 2011-10-16 22:46:11 +0300
  * Remove extra MariaDB- from binary tar.gz file name
  * Print server version name to .err file on crash
* [Revision #3236](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3236)\
  Fri 2011-10-14 17:51:16 +0200
  * In crash handler, output session value of the optimizer switch.
* [Revision #3235](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3235) \[merge]\
  Fri 2011-10-14 03:56:41 -0700
  * Merge.
  * [Revision #3233.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3233.1.1) \[merge]\
    Fri 2011-10-14 00:11:50 -0700
    * Merge.
    * [Revision #3232.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3232.1.1)\
      Thu 2011-10-13 22:39:00 -0700
      * Fixed [Bug #872735](https://bugs.launchpad.net/bugs/872735)
      * This bug happened because the maps of covering keys for mergeable derived\
        tables/views was not recalculated after the derived tables/vies had been\
        merged into the main query.
* [Revision #3234](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3234)\
  Fri 2011-10-14 12:41:20 +0200
  * update pbxt test results
* [Revision #3233](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3233)\
  Thu 2011-10-13 13:44:50 +0200
  * [Bug #817966](https://bugs.launchpad.net/bugs/817966) int\_column IN (string\_constant)
  * restore the status quo from before the microsecond patch
* [Revision #3232](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3232)\
  Thu 2011-10-13 11:23:59 +0200
  * typo.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
