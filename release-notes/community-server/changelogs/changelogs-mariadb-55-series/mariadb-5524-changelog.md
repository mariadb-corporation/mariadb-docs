# MariaDB 5.5.24 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.askmonty.org/mariadb/5.5.24) |[Release Notes](../../old-releases/5.5/5.5.24.md) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 31 May 2012

For the highlights of this release, see the[release notes](../../old-releases/5.5/5.5.24.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3425](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3425)\
  Wed 2012-05-30 20:20:54 +0200
  * MSI package: always install new component "Common" (currently consists of charset directory)
* [Revision #3424](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3424)\
  Wed 2012-05-30 19:11:59 +0200
  * don't use deprecated options in the installed config files
* [Revision #3423](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3423)\
  Tue 2012-05-29 21:38:51 +0200
  * RPM packages should not obsolete themselves.
  * Otherwise yum on fedora will not install them\
    (rpm will, yum on centos and rhel will).
* [Revision #3422](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3422)\
  Tue 2012-05-29 21:38:35 +0200
  * [MDEV-293](https://jira.mariadb.org/browse/MDEV-293) 5.5 RPMs for RHEL6/CentOS6
  * Build MariaDB-compat rpm by repackaging files from MariaDB-shared-5.3.\*.rpm
  * Or RHEL6/CentOS6 make all other MariaDB rpms depend on MariaDB-compat.
* [Revision #3421](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3421)\
  Sat 2012-05-26 13:04:23 +0200
  * Don't install debug plugins and don't populate unused "plugins.files" file.
* [Revision #3420](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3420)\
  Fri 2012-05-25 21:08:26 +0200
  * [MDEV-295](https://jira.mariadb.org/browse/MDEV-295) Do NOT start mysql when installing MariaDB rpms\
    but restart it on upgrade, if it was already running
* [Revision #3419](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3419)\
  Fri 2012-05-25 19:18:29 +0200
  * create a new MariaDB-common.rpm that contains files needed both by the client and the server.
  * use my.cnf includes to split one big my.cnf file in server and client parts.
  * remove "Provides: mysql-libs" (doesn't help on CentOS 6)
* [Revision #3418](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3418)\
  Wed 2012-05-23 18:06:06 +0200
  * fix test case
* [Revision #3417](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3417)\
  Tue 2012-05-22 11:04:32 +0200
  * Building RPMs with CPack
  * configure with cmake -DRPM=distro
* [Revision #3416](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3416)\
  Fri 2012-05-11 09:18:00 +0200
  * more portable fix for [Bug #942266](https://bugs.launchpad.net/bugs/942266) - 5.5 builds fail with systemtap-sdt-dev installed on Ubuntu
  * include early, before min/max macros are defined.
* [Revision #3415](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3415) \[merge]\
  Mon 2012-05-21 20:54:41 +0200
  * 5.3 merge
  * [Revision #2502.546.66](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.66) \[merge]\
    Sun 2012-05-20 14:57:29 +0200
    * 5.2 merge
    * [Revision #2502.528.47](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.47) \[merge]\
      Fri 2012-05-18 14:23:05 +0200
      * 5.1 merge
      * [Revision #2502.554.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.554.8)\
        Fri 2012-05-18 12:42:06 +0200
        * post-merge fixes
      * [Revision #2502.554.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.554.7) \[merge]\
        Thu 2012-05-17 12:12:33 +0200
        * merge with mysql-5.1.63
    * [Revision #2502.528.46](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.46)\
      Thu 2012-05-17 10:13:25 +0300
      * fix of [Bug #998321](https://bugs.launchpad.net/bugs/998321)
      * The problem is that we can't check null\_value field of non-basic constant without the item execution.:
  * [Revision #2502.546.65](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.65) \[merge]\
    Fri 2012-05-18 16:28:11 +0400
    * Merge
    * [Revision #2502.558.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.558.1)\
      Fri 2012-05-18 16:24:12 +0400
      * [Bug #1000269](https://bugs.launchpad.net/bugs/1000269): Wrong result (extra rows) with semijoin+materialization, IN subqueries, join\_cache\_level>0
      * make make\_cond\_after\_sjm() correctly handle OR clauses where one branch refers to the semi-join table\
        while the other branch refers to the non-semijoin table.
  * [Revision #2502.546.64](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.64)\
    Thu 2012-05-17 10:45:20 +0300
    * Test suite of fixed bug ([Bug #993459](https://bugs.launchpad.net/bugs/993459)).
  * [Revision #2502.546.63](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.63)\
    Tue 2012-05-15 08:31:07 +0300
    * Fix for [Bug #998516](https://bugs.launchpad.net/bugs/998516)
    * If we did nothing in resolving unique table conflict we should not retry (it leed to infinite loop).
    * Now we retry (recheck) unique table check only in case if we materialized a table.
  * [Revision #2502.546.62](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.62)\
    Sun 2012-05-13 13:15:17 +0400
    * [Bug #998236](https://bugs.launchpad.net/bugs/998236): Assertion failure or valgrind errors at best\_access\_path ...
    * Let fix\_semijoin\_strategies\_for\_picked\_join\_order() set\
      POSITION::prefix\_record\_count for POSITION records that it copies from\
      SJ\_MATERIALIZATION\_INFO::tables.
    * (These records do not have prefix\_record\_count set, because they are optimized\
      as joins-inside-semijoin-nests, without full advance\_sj\_state() processing).
  * [Revision #2502.546.61](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.61) \[merge]\
    Sat 2012-05-12 12:27:26 +0400
    * Merge 5.2->5.3
    * [Revision #2502.528.45](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.45) \[merge]\
      Sat 2012-05-12 12:12:35 +0400
      * Merge 5.2->5.3
      * [Revision #2502.554.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.554.6)\
        Sat 2012-05-12 11:53:14 +0400
        * [Bug #997747](https://bugs.launchpad.net/bugs/997747): Assertion \`join->best\_read < ((double)1.79..5e+308L)' failed\
          in greedy\_search with LEFT JOINs and unique keys
        * Backport the fix for [Bug #806524](https://bugs.launchpad.net/bugs/806524) from [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md)
  * [Revision #2502.546.60](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.60) \[merge]\
    Fri 2012-05-11 11:40:23 +0300
    * Merge 5.2->5.3
    * [Revision #2502.528.44](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.44)\
      Fri 2012-05-11 09:35:46 +0300
      * fix for [Bug #994392](https://bugs.launchpad.net/bugs/994392)
      * The not\_null\_tables() of Item\_func\_not\_all and Item\_in\_optimizer was inherited from\
        Item\_func by mistake. It made the optimizer think that subquery\
        predicates with ALL/ANY/IN were null-rejecting. This could trigger invalid\
        conversions of outer joins into inner joins.
    * [Revision #2502.528.43](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.43)\
      Thu 2012-05-10 09:00:21 +0300
      * Fixed typo
    * [Revision #2502.528.42](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.42)\
      Tue 2012-05-08 12:38:22 +0200
      * [MDEV-262](https://jira.mariadb.org/browse/MDEV-262) : log\_state occationally fails in buildbot.
      * The failures are missing entries in the slow query log. The reason for the failure are sleep() calls with short duration 10ms, which is less than the default system timer resolution for various WaitForXXXObject functions (15.6 ms) and thus can't work reliably.
      * The fix is to make sleeps tiny bit longer (20ms from 10ms) in the test.
    * [Revision #2502.528.41](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.41)\
      Tue 2012-05-08 00:26:41 +0200
      * fixes [Bug #994156](https://bugs.launchpad.net/bugs/994156)
      * [MDEV-261](https://jira.mariadb.org/browse/MDEV-261) : mysqtest crashes when assigning variable to result of select , like\
        let x = `SELECT <something>`
      * The fix is to detect the condition "no active connection", to report error and die.
      * Note, that the check for no active connection was already in place for ordinary commands,\
        and was missing only for assign-variable command.
    * [Revision #2502.528.40](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.40)\
      Mon 2012-05-07 13:26:34 +0300
      * Fix for [Bug #993726](https://bugs.launchpad.net/bugs/993726)
      * Optimization of aggregate functions detected constant under max() and evalueted it, but condition in the WHWRE clause (which is always FALSE) was not taken into account
    * [Revision #2502.528.39](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.39)\
      Mon 2012-05-07 11:02:58 +0300
      * Fix for [Bug #992405](https://bugs.launchpad.net/bugs/992405)
      * The patch backports two patches from mysql 5.6:
        * BUG#12640437: USING SQL\_BUFFER\_RESULT RESULTS IN A DIFFERENT QUERY OUTPUT
        * Bug#12578908: SELECT SQL\_BUFFER\_RESULT OUTPUTS TOO MANY ROWS WHEN GROUP IS OPTIMIZED AWAY
        * Original comment:
          * 3714 Jorgen Loland 2012-03-01
          * BUG#12640437 - USING SQL\_BUFFER\_RESULT RESULTS IN A DIFFERENT\
            QUERY OUTPUT
          * For all but simple grouped queries, temporary tables are used to\
            resolve grouping. In these cases, the list of grouping fields is\
            stored in the temporary table and grouping is resolved\
            there (e.g. by adding a unique constraint on the involved\
            fields). Because of this, grouping is already done when the rows\
            are read from the temporary table.
          *
          * In the case where a group clause may be optimized away, grouping\
            does not have to be resolved using a temporary table. However, if\
            a temporary table is explicitly requested (e.g. because the\
            SQL\_BUFFER\_RESULT hint is used, or the statement is\
            INSERT...SELECT), a temporary table is used anyway. In this case,\
            the temporary table is created with an empty group list (because\
            the group clause was optimized away) and it will therefore not\
            create groups. Since the temporary table does not take care of\
            grouping, JOIN::group shall not be set to false in\
            make\_simple\_join(). This was fixed in bug 12578908.
          *
          * However, there is an exception where make\_simple\_join() should\
            set JOIN::group to false even if the query uses a temporary table\
            that was explicitly requested but is not strictly needed. That\
            exception is if the loose index scan access method (explain\
            says "Using index for group-by") is used to read into the\
            temporary table. With loose index scan, grouping is resolved\
            by the access method. This is exactly what happens in this bug.
    * [Revision #2502.528.38](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.38)\
      Thu 2012-05-03 14:49:52 +0300
      * Fix [Bug #993745](https://bugs.launchpad.net/bugs/993745)
      * This is a backport of the fix for MySQL bug #13723054 in 5.6.
      * Original comment:
        * The crash is caused by arbitrary memory area owerwriting in case of\
          BLOB fields during attempt to copy BLOB field key image into record\
          buffer(record buffer is too small to get BLOB key part image).\
          note:
        *
        * QUICK\_GROUP\_MIN\_MAX\_SELECT can not work with BLOB fields\
          because it uses record buffer as temporary buffer for key values\
          however this case is filtered out by covering\_keys() check\
          in get\_best\_group\_min\_max() as BLOBs always require key length\
          modificator in the key declaration and if the key has a BLOB\
          then it can not be covered key.\
          The fix is to use 'max\_used\_key\_length' key length instead of 0.
        *
        * Analysis:
        * Spcifically the crash in this bug was a result of the call to key\_copy()\
          that copied the whole key, inlcuding the BLOB field which is not used\
          for index access. Copying the blob field overwrote memory as far as the\
          function parameter 'key\_info'. As a result the contents of key\_info was\
          all 0, which resulted in a crash when this key\_info was accessed few\
          lines below in key\_cmp().
  * [Revision #2502.546.59](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.59)\
    Tue 2012-05-08 20:58:41 +0300
    * Fix compiler warnings.
  * [Revision #2502.546.58](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.58)\
    Tue 2012-05-08 19:13:26 +0300
    * Addition to the fix to LP bug#994275.
    * It is problem of constant propagated to ref\* access method (the problem was hiden by using debug binaries for testing).
  * [Revision #2502.546.57](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.57)\
    Mon 2012-05-07 21:14:37 +0300
    * [Bug #994275](https://bugs.launchpad.net/bugs/994275) fix.
    * In 5.3 we substitute constants in ref access values it can't be null so we do not need add NOT NULL for early NULL filtering.
* [Revision #3414](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3414) \[merge]\
  Mon 2012-05-21 15:30:25 +0200
  * Merge with MySQL
* [Revision #3413](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3413) \[merge]\
  Fri 2012-05-18 16:45:59 +0300
  * Automatic merge
  * [Revision #3407.2.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3407.2.2)\
    Fri 2012-05-18 16:40:16 +0300
    * Fixed compile warnings
    * Fixed some mtr test problems
  * [Revision #3407.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3407.2.1)\
    Fri 2012-05-18 16:02:11 +0300
    * Fixed [Bug #997460](https://bugs.launchpad.net/bugs/997460) Truncate table on partitioned Aria table fails with ER\_ILLEGAL\_HA
    * Fix is done by doing an autocommit in truncate table inside Aria
* [Revision #3412](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3412)\
  Fri 2012-05-18 13:32:25 +0200
  * Fix test case to produce sorted output
* [Revision #3411](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3411)\
  Fri 2012-05-18 01:44:13 -0700
  * Asked for sorted result from a query.
* [Revision #3410](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3410)\
  Thu 2012-05-17 18:01:13 -0700
  * Changed a test case from join\_cache.test to make it platform independent
* [Revision #3409](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3409) \[merge]\
  Thu 2012-05-17 21:52:48 +0200
  * merge
  * [Revision #3407.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3407.1.1)\
    Thu 2012-05-17 21:50:50 +0200
    * Add -Wno-missing-field-initializers to silence bogus warnings from GCC in maintainer mode.
* [Revision #3408](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3408) \[merge]\
  Wed 2012-05-16 22:33:22 -0700
  * Merge.
  * [Revision #3403.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3403.1.1)\
    Wed 2012-05-16 20:39:03 -0700
  * Fixed [Bug #999251](https://bugs.launchpad.net/bugs/999251): Q13 from DBT3 uses table scan instead of covering index scan.
  * The optimizer chose a less efficient execution plan due to the following\
    defects of the code:
    1. the generic handler function handler::keyread\_time did not take into account\
       that in clustered primary keys record data is included into each index entry
    2. the function make\_join\_readinfo erroneously decided that index only scan\
       could not be used if join cache was empoyed.
  * Added no additional test case.
  * Adjusted some of the test results.
* [Revision #3407](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3407)\
  Thu 2012-05-17 01:47:28 +0300
  * More fixes for LOCK TABLE and REPAIR/FLUSH
  * Changed HA\_EXTRA\_NORMAL to HA\_EXTRA\_NOT\_USED (more clean)
* [Revision #3406](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3406)\
  Wed 2012-05-16 22:04:48 +0300
  * Fixed [Bug #990187](https://bugs.launchpad.net/bugs/990187) Assertion \`share->reopen == 1' failed at maria\_extra on ADD PARTITION
* [Revision #3405](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3405)\
  Wed 2012-05-16 18:46:02 +0300
  * Moved maria tests to suite/maria
* [Revision #3404](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3404)\
  Wed 2012-05-16 18:44:17 +0300
  * Fixed [Bug #973039](https://bugs.launchpad.net/bugs/973039) - Assertion \`share->in\_trans == 0' failed in maria\_close on DROP TABLE under LOCK
  * 5.5 was missing calls to ha\_extra(HA\_PREPARE\_FOR\_DROP | HA\_PREPARE\_FOR\_RENAME); Lost in merge 5.3 -> 5.5
* [Revision #3403](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3403)\
  Tue 2012-05-15 19:35:57 +0200
  * Added `--continue-on-error` to mysqltest and mysql-test-run
  * This will contune the test case even if there was an error\
    and makes it easier to run a test that contains many sub tests against one engine.
  * (originally by Monty)
* [Revision #3402](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3402)\
  Tue 2012-05-08 14:27:44 +0200
  * [MDEV-254](https://jira.mariadb.org/browse/MDEV-254): Server hang with FLUSH TABLES WITH READ LOCK AND DISABLE CHECKPOINT
  * The code to re-enable checkpointing after UNLOCK TABLES was lost in the 5.5\
    merge, so re-add it back in.
* [Revision #3401](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3401)\
  Mon 2012-05-07 12:47:29 +0200
  * [MDEV-257](https://jira.mariadb.org/browse/MDEV-257): wrong libmysqlclient.so symlink in package libmariadbclient-dev.
* [Revision #3400](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3400) \[merge]\
  Mon 2012-05-07 12:21:59 +0200
  * merge
  * [Revision #3398.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3398.1.1)\
    Sat 2012-05-05 16:00:22 +0200
    * allow handlersocket on FreeBSD, fix getaddrinfo problem
* [Revision #3399](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3399) \[merge]\
  Sat 2012-05-05 14:59:44 +0200
  * merge
  * [Revision #3391.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3391.1.2)\
    Sat 2012-05-05 08:27:17 +0200
    * [MDEV-207](https://jira.mariadb.org/browse/MDEV-207) Install headers required to build external storage plugins
    * 5.5 version. for cmake, not autotools.
  * [Revision #3391.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3391.1.1) \[merge]\
    Fri 2012-05-04 07:16:38 +0200
    * 5.3 merge
    * [Revision #2502.546.56](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.56)\
      Wed 2012-05-02 22:02:17 +0200
      * update the version number
    * [Revision #2502.546.55](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.55)\
      Thu 2012-05-03 13:14:40 +0500
      * Fix for failing gis-precise on Windows.
    * [Revision #2502.546.54](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.54) \[merge]\
      Wed 2012-05-02 22:02:06 +0200
      * 5.2 merge
      * [Revision #2502.528.37](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.37)\
        Wed 2012-05-02 22:00:31 +0200
        * update the result file
      * [Revision #2502.528.36](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.36)\
        Wed 2012-05-02 18:11:02 +0200
        * [MDEV-214](https://jira.mariadb.org/browse/MDEV-214) [Bug #967242](https://bugs.launchpad.net/bugs/967242) Wrong result with JOIN, AND in ON condition, multi-part key, GROUP BY, subquery and OR in WHERE
        * The problem was in the code (update\_const\_equal\_items()) which marked\
          index parts constant independently of the place where the equality was used.
        * In the test suite it marked t2\_1.c part constant despite the fact that\
          it connected by OR with other expression.
        * Solution is to mark constant only top equalities connected with AND.
      * [Revision #2502.528.35](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.35) \[merge]\
        Wed 2012-05-02 17:06:30 +0200
        * 5.1 merge
        * [Revision #2502.554.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.554.5)\
          Tue 2012-04-24 17:29:03 +0200
  * [Bug #986120](https://bugs.launchpad.net/bugs/986120) Problem installing mariadb 5 on solaris 10
  * remove a redundant line in Makefile.am
    * [Revision #2502.546.53](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.53)\
      Wed 2012-05-02 15:23:49 +0200
      * implement Item\_singlerow\_subselect::get\_date() to avoid\
        unnecessary date->string->date conversion
    * [Revision #2502.546.52](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.52)\
      Wed 2012-05-02 15:22:47 +0200
      * [MDEV-241](https://jira.mariadb.org/browse/MDEV-241) [Bug #992722](https://bugs.launchpad.net/bugs/992722) - Server crashes in get\_datetime\_value
      * Create an Item\_cache based on item's cmp\_type, not result\_type in\
        subselect\_engine.
      * Use result\_field in Item\_cache\_temporal::cache\_value(),\
        just like all other Item\_cache\*::cache\_value() do.
    * [Revision #2502.546.51](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.51) \[merge]\
      Wed 2012-05-02 17:04:28 +0200
      * merge
      * [Revision #2502.528.34](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.34)\
        Wed 2012-05-02 16:53:02 +0200
        * [Bug #993103](https://bugs.launchpad.net/bugs/993103): Wrong result with LAST\_DAY('0000-00-00 00:00:00')IS NULL in WHERE condition
        * Fix is to set maybe\_null flag for Item\_func\_last\_day.
      * [Revision #2502.528.33](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.33)\
        Wed 2012-04-25 15:30:19 +0200
        * [MDEV-233](https://jira.mariadb.org/browse/MDEV-233) - Support Wix3.6 for MSI
      * [Revision #2502.528.32](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.32)\
        Wed 2012-04-18 20:04:50 +0200
        * [Bug #982664](https://bugs.launchpad.net/bugs/982664) there are few broken clients that lie about their capabilities\
          (for example, one of them sets client capabilities by copying server capabilities)
        * We cannot fix them - let's tolerate them
    * [Revision #2502.546.50](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.50)\
      Sun 2012-04-29 18:08:11 +0500
      * [Bug #977021](https://bugs.launchpad.net/bugs/977021) ST\_BUFFER fails with the negative D.
      * Points and lines should disappear if we got negative D.
        * To make it work properly inside the GEOMETRYCOLLECTION,\
          we add the empty operation there.
        *
        * [Bug #986977](https://bugs.launchpad.net/bugs/986977) Assertion \`!cur\_p->event' failed in Gcalc\_scan\_iterator::arrange\_event(int, int).
        * The double->inernal coord conversion produced -0 (minus zero) on some data.
        * That minus-zero produces invalid comparison results when compared agains plus-zero.
        * So we fixed the gcalc\_set\_double() to avoid it.
        *
        * per-file comments:
          * mysql-test/r/gis-precise.result
            * result updated.
          * mysql-test/t/gis-precise.test
            * tests for [Bug #977021](https://bugs.launchpad.net/bugs/977021) and [Bug #986977](https://bugs.launchpad.net/bugs/986977) added.
          * sql/gcalc\_slicescan.cc
            * [Bug #986977](https://bugs.launchpad.net/bugs/986977). The gcalc\_set\_double fixed to not produce minus-zero.
          * sql/item\_geofunc.cc
            * [Bug #977021](https://bugs.launchpad.net/bugs/977021). Add the NOOP for the disappearing features.
    * [Revision #2502.546.49](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.49)\
      Thu 2012-04-26 19:21:37 +0200
      * [MDEV-216](https://jira.mariadb.org/browse/MDEV-216) [Bug #976104](https://bugs.launchpad.net/bugs/976104) - Assertion \`0' failed in my\_message\_sql on UPDATE IGNORE, or unknown error on release build
      * Don't send\_error at the end of mysql\_multi\_update() if select failed.
      * The error, if there was any, was already sent by mysql\_select
    * [Revision #2502.546.48](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.48)\
      Fri 2012-04-27 12:59:17 +0300
      * Fix [Bug #985667](https://bugs.launchpad.net/bugs/985667), [MDEV-229](https://jira.mariadb.org/browse/MDEV-229)
      * Analysis:
        * The reason for the wrong result is the interaction between constant\
          optimization (in this case 1-row table) and subquery optimization.
        * First the outer query is optimized, and 'make\_join\_statistics' finds that\
          table t2 has one row, reads that row, and marks the whole table as constant.\
          This also means that all fields of t2 are constant.
        *
        * Next, we optimize the subquery in the end of the outer 'make\_join\_statistics'.\
          The field 'f2' is considered constant, with value '3'. The subquery predicate\
          is rewritten as the constant TRUE.
        *
        * The outer query execution detects early that the whole query result is empty\
          and calls 'return\_zero\_rows'. Since the query is with implicit grouping, we\
          have to produce one row with special values for the aggregates (depending on\
          each aggregate function), and NULL values for all non-aggregate fields. This\
          function calls 'no\_rows\_in\_result' to set each aggregate function to the\
          default value when it aggregates over an empty result, and then calls\
          'send\_data', which in turn evaluates each Item in the SELECT list.
        *
        * When evaluation reaches the subquery predicate, it executes the subquery\
          with field 'f2' having a constant value '3', and the subquery produces the\
          incorrect result '7'.
      * Solution:
        * Implement Item::no\_rows\_in\_result for all subquery predicates. In order to\
          make this work, it is also needed to make all val\_\* methods of all subquery\
          predicates respect the Item\_subselect::forced\_const flag. Otherwise subqueries\
          are executed anyways, and override the default value set by no\_rows\_in\_result\
          with whatever result is produced from the subquery evaluation.
    * [Revision #2502.546.47](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.47) \[merge]\
      Mon 2012-04-23 20:37:44 +0200
      * merge
      * [Revision #2502.557.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.557.1)\
        Fri 2012-04-20 21:09:16 +0200
        * [Bug #983285](https://bugs.launchpad.net/bugs/983285) - incompatibility in frm in case of VIEWs with non-default ALGORITHM option.
        * As part of derived tables redesign, values for VIEW\_ALGORITHM\_MERGE and VIEW\_ALGORITHM\_TMPTABLE have changed from (former values 1 rsp 2 , new values 5 rsp 9).
        * This lead to the problem that views, created with version 5.2 or earlier would not work in all situations (e.g "SHOW CREATE VIEW"), or with mysqldump.
        * The fix is to restore backward compatibility for the from file, and convert algorithm={1,2} in the frm to {5,9} when reading .frm from disk, and store backward compatible values when writing from to disk.
        * Also allow processing correct processing for "invalid" .frms created with [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md)/5.5 GA releases (where algorithm stored in memory matched the one stored in frm).
    * [Revision #2502.546.46](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.46)\
      Mon 2012-04-23 09:45:27 +0200
      * [MDEV-207](https://jira.mariadb.org/browse/MDEV-207) Install headers required to build external storage plugins
      * install all private headers in mysql/private/
    * [Revision #2502.546.45](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.45)\
      Thu 2012-04-19 09:16:30 +0300
      * [Bug #978847](https://bugs.launchpad.net/bugs/978847) fixed.
      * Fixed incorrect type casting which made all fields (except very first) changes to materialized table incorrect.
      * Saved list of view/derived table used items after expanding '\*'.
    * [Revision #2502.546.44](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.44)\
      Thu 2012-04-19 05:37:16 +0400
      * [Bug #978479](https://bugs.launchpad.net/bugs/978479): Wrong result (extra rows) with derived\_with\_keys+loosescan+semijoin=ON, materialization=OFF
      * Part#2: Don't try to construct a LooseScan access on indexes that do not guarantee\
        index-ordered reads.
    * [Revision #2502.546.43](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.43)\
      Thu 2012-04-19 04:50:32 +0400
      * [Bug #978479](https://bugs.launchpad.net/bugs/978479): Wrong result (extra rows) with derived\_with\_keys+loosescan+semijoin=ON, materialization=OFF
      * Part#1: make EXPLAIN's plan match the one by actual execution:\
        Item\_subselect::used\_tables() should return the same value irrespectively\
        of whether we're running an EXPLAIN or a SELECT.
* [Revision #3398](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3398)\
  Sat 2012-05-05 02:36:10 +0200
  * [MDEV-255](https://jira.mariadb.org/browse/MDEV-255): Compile handlersocket plugin in 5.5
* [Revision #3397](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3397)\
  Fri 2012-05-04 17:22:40 +0200
  * FreeBSD : Extend CMAKE\_REQUIRED\_LIBRARIES with ${LIBEXECINFO} , for backtrace\_symbols & Co
* [Revision #3396](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3396)\
  Fri 2012-05-04 14:46:18 +0200
  * Resolve opt\_vardir in MTR with realpath. Server resolves some directory names, thus\
    mtr should do it as well, to avoid differences in test output.
  * This fixes sys\_vars.secure\_file\_priv on FreeBSD9.0 buildbot.
* [Revision #3395](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3395)\
  Fri 2012-05-04 14:02:35 +0200
  * Fix FreeBSD test errors. Also link with libexecinfo on FreeBSD for stacktrace functionality.
* [Revision #3394](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3394)\
  Fri 2012-05-04 03:51:30 +0200
  * support same version upgrade for MSI
* [Revision #3393](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3393)\
  Thu 2012-05-03 18:58:48 +0200
  * Fix (hopefully) a race condition in a test. Wait until killed connection\
    is gone.
* [Revision #3392](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3392) \[merge]\
  Thu 2012-05-03 16:00:41 +0300
  * automatic merge
  * [Revision #3363.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3363.1.1)\
    Wed 2012-04-04 00:16:38 +0300
    * Created suites for heap, archive and csv.
    * Moved test from main suite to the new suites.
    * Move tests from maria/t and maria/r to maria
* [Revision #3391](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3391)\
  Thu 2012-05-03 02:47:06 +0200
  * fixes [Bug #992983](https://bugs.launchpad.net/bugs/992983)
  * [MDEV-246](https://jira.mariadb.org/browse/MDEV-246) - Aborted\_clients incremented during ordinary connection close
  * The problem was increment of aborted\_threads variable due to thd->killed which was set when threadpool connection was terminated . The fix is not to set thd->killed anymore, there is no real reason for doing it..
  * Added a test that checks that status variable aborted\_clients does not grow for ordinary disconnects, and that successful KILL increments this variable.
* [Revision #3390](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3390)\
  Thu 2012-04-19 17:00:13 +0300
  * Dependency of tests from ulong size removed.
* [Revision #3389](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3389)\
  Sun 2012-04-29 17:18:38 +0500
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
* [Revision #3388](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3388)\
  Sat 2012-04-21 02:57:28 +0200
  * [MDEV-202](https://jira.mariadb.org/browse/MDEV-202) Overlays do not support nested test suites which exist in MTR
* [Revision #3387](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3387)\
  Thu 2012-04-19 04:02:28 +0200
  * [MDEV-220](https://jira.mariadb.org/browse/MDEV-220) MariaDB server 5.5 GA candidate has default storage engine MyISAM
* [Revision #3386](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3386)\
  Wed 2012-04-18 20:48:14 +0200
  * fixes [Bug #976225](https://bugs.launchpad.net/bugs/976225)
  * [MDEV-217](https://jira.mariadb.org/browse/MDEV-217) - Assertion \`thd->stmt\_arena != thd->progress.arena' failed in thd\_progress\_init on OPTIMIZE two tables when replaced by recreate
  * call thd\_progress\_end() in the copy\_data\_between\_tables(), to match its\
    thd\_progress\_init().
* [Revision #3385](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3385)\
  Wed 2012-04-18 04:00:08 +0200
  * [MDEV-224](https://jira.mariadb.org/browse/MDEV-224) plugin usage statistics in the feedback reports
* [Revision #3384](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3384)\
  Wed 2012-04-18 03:29:26 +0200
  * add a space between safemalloc error mesage and a stack trace
* [Revision #3383](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3383)\
  Wed 2012-04-18 03:29:13 +0200
  * fix information\_schema\_all\_engines test to pass both with ha\_xtradb.so and libxtradb.a
* [Revision #3382](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3382)\
  Tue 2012-04-17 20:30:19 +0200
  * update @@have\_innodb variable when innodb plugin is uninstalled
* [Revision #3381](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3381)\
  Tue 2012-04-17 20:29:43 +0200
  * better fix for string plugin variables pointing into argv\[]\
    for a plugin installed run-time
* [Revision #3380](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3380)\
  Tue 2012-04-17 20:28:21 +0200
  * bugfix: mysqld failed to start if a compiled-in plugin failed to initialize\
    (`--xxx=ON behaving as --xxx=FORCE`)
* [Revision #3379](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3379)\
  Tue 2012-04-17 20:25:03 +0200
  * typo fixed: space in the status variable name
* [Revision #3378](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3378)\
  Tue 2012-04-17 14:25:08 +0200
  * bug fix: I\_S plugins were not locked when used
* [Revision #3377](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3377) \[merge]\
  Tue 2012-04-17 01:03:10 +0200
  * merge
  * [Revision #2502.546.42](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.42) \[merge]\
    Mon 2012-04-16 23:35:38 +0200
    * merge
    * [Revision #2502.528.31](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.31) \[merge]\
      Mon 2012-04-16 23:32:50 +0200
      * merge
      * [Revision #2502.556.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.556.3)\
        Mon 2012-04-16 23:31:33 +0200
        * fix compiler warnings
      * [Revision #2502.556.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.556.2)\
        Mon 2012-04-16 23:31:02 +0200
        * backport a change from 5.5 to remove thread sleeps from Innodb assertions on Windows.
        * This can result in bad deadlocks (e.g loader lock), seen in latest crash reports.
  * [Revision #2502.546.41](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.41) \[merge]\
    Mon 2012-04-16 17:41:43 +0200
    * merge
    * [Revision #2502.528.30](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.528.30) \[merge]\
      Mon 2012-04-16 15:38:53 +0200
      * merge
      * [Revision #2502.556.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.556.1)\
        Mon 2012-04-16 15:28:33 +0200
        * fixes [Bug #983047](https://bugs.launchpad.net/bugs/983047)
        * [MDEV-221](https://jira.mariadb.org/browse/MDEV-221) - Properly escape command line when starting mysql\_install\_db\
          since password characters can contain quotes or spaces.
        * The proper quoting method for command line arguments used here was extracted from[everyone-quotes-arguments-the-wrong-way.aspx](https://blogs.msdn.com/b/twistylittlepassagesallalike/archive/2011/04/23/everyone-quotes-arguments-the-wrong-way.aspx)
        * Additionally, mysql\_install\_db.exe now passes root password to `"mysqld.exe --bootstrap"`\
          in hexadecimal form, to handle potential special chars inside password string literal.
  * [Revision #2502.546.40](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.546.40)\
    Sat 2012-04-07 17:27:00 -0700
    * Fixed [Bug #972943](https://bugs.launchpad.net/bugs/972943) properly.
    * The previous patch for the bug (that erroneously identified the bug as [Bug #972973](https://bugs.launchpad.net/bugs/972973) in its comment) was incorrect.
    * It turned out that the code that triggered the abort complain reported for\
      the bug was not needed at all.
* [Revision #3376](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3376)\
  Sun 2012-04-15 01:54:28 +0200
  * fix compile error on unixes
* [Revision #3375](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3375)\
  Sun 2012-04-15 01:41:03 +0200
  * exclude cmake generated files from mysql-test installation (applies only for in-source builds)
* [Revision #3374](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3374)\
  Sun 2012-04-15 01:40:00 +0200
  * fix application verifier crashes
* [Revision #3373](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3373)\
  Sun 2012-04-15 01:29:17 +0200
  * Use test/db.opt as dummy file in the package, instead of test/.empty
  * Also, do not package aria log files in the zip package- not required for the database to function,\
    also will avoid trouble with recovery, if someone accidentially (or on purpose) upgrades by unpacking the zip in the existing install directory.
* [Revision #3372](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3372)\
  Sun 2012-04-15 01:21:18 +0200
  * Add minimal clarication about 'root' user to the installer UI
* [Revision #3371](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3371)\
  Sun 2012-04-15 01:19:39 +0200
  * [MDEV-221](https://jira.mariadb.org/browse/MDEV-221) : Fix potential memory access past the end of input string in filename\_to\_tablename()
* [Revision #3370](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3370)\
  Fri 2012-04-13 19:44:22 +0200
  * Fixed some simple warnings on Windows.
* [Revision #3369](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3369)\
  Thu 2012-04-12 01:40:44 +0200
  * Threadpool - use EV\_ONESHOT with kevent, to prevent race condition when 2\
    threads are retrieving events at the same time.
* [Revision #3368](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3368)\
  Thu 2012-04-12 01:33:43 +0200
  * Fix build on OSX
    * Workaround linker bug that prevents linking aria test executables\
      using -fno-common on OSX
    * Skip system readline detection (OSX readline is incompatible one)
    * Make Xcode generator work

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
