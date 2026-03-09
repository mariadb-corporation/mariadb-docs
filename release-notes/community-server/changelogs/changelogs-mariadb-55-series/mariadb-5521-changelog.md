# MariaDB 5.5.21 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.askmonty.org/mariadb/5.5.21) |[Release Notes](../../old-releases/5.5/5.5.21.md) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 16 Mar 2012

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.21.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3327](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3327)\
  Wed 2012-03-14 19:47:15 +0100
  * another fix for `--innodb-trx*` name conflict
* [Revision #3326](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3326)\
  Tue 2012-03-13 14:43:34 +0100
  * [MDEV-176](https://jira.mariadb.org/browse/MDEV-176) feedback plugin is linked dynamically in bintar
* [Revision #3325](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3325)\
  Tue 2012-03-13 13:34:24 +0100
  * alternative method of resolving addresses for safemalloc and crash handler.\
    don't link with libbfd, exec addr2line, if it's available at run time
* [Revision #3324](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3324)\
  Tue 2012-03-13 13:31:21 +0100
  * fix SphinxSE version as reported in I\_S.PLUGINS
* [Revision #3323](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3323)\
  Tue 2012-03-13 13:29:44 +0100
  * monty's cleanup of my\_thr\_init.c\
    and collateral changes
* [Revision #3322](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3322)\
  Tue 2012-03-13 13:28:08 +0100
  * broad suppression for dlsym "memory leak" - same as for dlclose
* [Revision #3321](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3321)\
  Tue 2012-03-13 13:27:14 +0100
  * disable EXTRA\_DEBUG in non-dbug builds
* [Revision #3320](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3320) \[merge]\
  Mon 2012-03-12 00:45:18 +0200
  * Merged the implementation of [MDEV-28](https://jira.mariadb.org/browse/MDEV-28) LIMIT ROWS EXAMINED into [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md).
  * [Revision #2502.513.75](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.75)\
    Sun 2012-03-11 14:39:20 +0200
    * Implementation of [MDEV-28](https://jira.mariadb.org/browse/MDEV-28) LIMIT ROWS EXAMINED
    * This task implements a new clause LIMIT ROWS EXAMINED as an extention to the ANSI LIMIT clause. This extension\
      allows to limit the number of rows and/or keys a query\
      would access (read and/or write) during query execution.
* [Revision #3319](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3319)\
  Fri 2012-03-09 09:20:45 +0100
  * fix uninitialized warning in mysql-test-run.pl\
    make the test to require sphinx 2.0.4 or later
* [Revision #3318](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3318) \[merge]\
  Fri 2012-03-09 08:06:59 +0100
  * merge with mysql-5.5.21
* [Revision #3317](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3317)\
  Thu 2012-03-08 13:06:28 +0100
  * remove .bzr-mysql directory - it's only used by proprietory bzr-mysql plugin
* [Revision #3316](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3316)\
  Wed 2012-03-07 17:38:47 +0200
  * Upgraded sphinx to version 2.0.4
  * Fixed memory leaks and compiler warnings in ha\_sphinx.cc
  * Added HA\_MUST\_USE\_TABLE\_CONDITION\_PUSHDOWN so that an engine can force index condition to be used
* [Revision #3315](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3315) \[merge]\
  Tue 2012-03-06 20:46:07 +0100
  * 5.3 merge
  * [Revision #2502.513.74](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.74) \[merge]\
    Mon 2012-03-05 22:33:46 -0800
    * Merge.
    * [Revision #2502.541.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.541.1)\
      Mon 2012-03-05 20:32:28 -0800
      * Fixed [Bug #946055](https://bugs.launchpad.net/bugs/946055).
      * The function create\_hj\_key\_for\_table() that builds the descriptor of\
        the hash join key to access a table of a materialized subquery must\
        ignore any equi-join predicate depending on the tables not belonging\
        to the subquery.
  * [Revision #2502.513.73](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.73) \[merge]\
    Mon 2012-03-05 22:00:24 +0200
    * Automatic merge
    * [Revision #2502.540.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.540.2)\
      Mon 2012-03-05 21:59:00 +0200
      * Ensure that we mark all processed tables as 'properly closed'.
      * This is needed as last log entry may be a DDL that is not processed and then a table may be left in 'not properly closed state' even if information is correct in it.
    * [Revision #2502.540.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.540.1)\
      Tue 2012-02-28 23:18:52 +0200
      * Fixed [Bug #925377](https://bugs.launchpad.net/bugs/925377) "Querying myisam table metadata while 'alter table..enable keys' is running may corrupt the table"
      * Fixed wrong mutex order bug in Aria when flush\_log\_for\_bitmap() was called when table is not yet marked for change.
  * [Revision #2502.513.72](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.72)\
    Mon 2012-03-05 15:48:12 +0200
    * Fix for [Bug #944504](https://bugs.launchpad.net/bugs/944504)
    * Problem is that subquery execution can't be called during prepare/optimize phase.
    * Also small fix for subquery test suite.
  * [Revision #2502.513.71](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.71)\
    Sun 2012-03-04 22:38:17 -0800
    * Fixed [Bug #944782](https://bugs.launchpad.net/bugs/944782).
    * This bug in the function JOIN::drop\_unused\_derived\_keys() could\
      leave the internal structures for a materialized derived table\
      in an inconsistent state. This led to a not quite correct EXPLAIN\
      output when no additional key had been created to access the table.\
      It also may lead to more serious consequences: so, the test case\
      added with this fix caused a crash in mariadb-5.5.20.
* [Revision #3314](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3314)\
  Mon 2012-03-05 21:55:25 +0100
  * compilation warning: unused variable
* [Revision #3313](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3313)\
  Mon 2012-03-05 21:48:06 +0100
  * [MDEV-20](https://jira.mariadb.org/browse/MDEV-20): INSTALL PLUGIN SONAME
* [Revision #3312](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3312)\
  Mon 2012-03-05 17:44:26 +0100
  * updates after writing [mysql-test Auxiliary Files](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/testing-tools/mariadb-test/mariadb-test-auxiliary-files)
* [Revision #3311](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3311)\
  Sat 2012-03-03 13:22:49 -0800
  * Supported extended keys ([MWL#247](https://askmonty.org/worklog/?tid=247)) for innodb\_plugin.
* [Revision #3310](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3310) \[merge]\
  Sat 2012-03-03 09:16:30 +0100
  * Merge
  * [Revision #3307.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3307.1.2) \[merge]\
    Fri 2012-03-02 22:52:03 -0800
    * Merge
  * [Revision #3307.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3307.1.1) \[merge]\
    Fri 2012-03-02 15:03:20 -0800
    * Merge [MWL#247](https://askmonty.org/worklog/?tid=247) from [mariadb 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series) -> [mariadb 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series).
    * [Revision #2502.539.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.539.6)\
      Tue 2012-02-28 13:03:10 -0800
      * Addressed all review feedbacks for [MWL#247](https://askmonty.org/worklog/?tid=247).
    * [Revision #2502.539.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.539.5) \[merge]\
      Mon 2012-02-27 21:23:12 -0800
      * Merge.
    * [Revision #2502.539.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.539.4) \[merge]\
      Wed 2012-02-22 13:04:58 -0800
      * Merge.
    * [Revision #2502.539.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.539.3)\
      Sun 2012-01-29 14:35:30 -0800
      * Fixed [Bug #923236](https://bugs.launchpad.net/bugs/923236).
      * When working on [MWL#247](https://askmonty.org/worklog/?tid=247) I forgot to adjust the function create\_hj\_key\_for\_table()\
        that created a key definition for hash join keys. The modified function must\
        set the values of the fields ext\_key\_parts, ext\_key\_flags, ext\_key\_part\_map\
        added to the key definition structure in [MWL#247](https://askmonty.org/worklog/?tid=247).
    * [Revision #2502.539.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.539.2)\
      Tue 2012-01-24 23:34:02 -0800
      * Fixed LP bug #921167.
      * The fields ext\_key\_flags and ext\_key\_part\_map must be initialized for any\
        key, even for a MyISAM key that never is considered by the optimizer as one\
        extended by hidden components.
    * [Revision #2502.539.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.539.1) \[merge]\
      Tue 2012-01-24 21:12:02 -0800
      * Merge.
      * [Revision #2502.538.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.538.6)\
        Wed 2012-01-18 19:38:03 -0800
        * Added a test case for [Bug #915291](https://bugs.launchpad.net/bugs/915291).
        * The bug was fixed by the patch for [Bug #914560](https://bugs.launchpad.net/bugs/914560).
      * [Revision #2502.538.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.538.5)\
        Tue 2012-01-17 03:26:49 -0800
        * Fixed [Bug #914560](https://bugs.launchpad.net/bugs/914560).
        * The patch for [MWL#247](https://askmonty.org/worklog/?tid=247) forgot to initialize the TABLE::ext\_key\_parts and\
          TABLE::ext\_key\_flags of the temporary tables by a query. This could cause\
          crashes for queries the execution of which needed creation of temporary\
          tables.
      * [Revision #2502.538.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.538.4)\
        Sun 2012-01-01 22:42:11 -0800
        * Fixed more compiler warnings.
      * [Revision #2502.538.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.538.3)\
        Sun 2012-01-01 21:41:57 -0800
        * Fixed compiler warnings.
      * [Revision #2502.538.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.538.2)\
        Sun 2012-01-01 20:47:36 -0800
        * Fixed calculation of rec\_per\_key elements for added components of the extended keys.
        * Slightly corrected the implementation of the function ha\_innobase::read\_time().
        * Changed the implementation of handler::keyread\_time to make the cost of single key\
          index only look-ups dependent on the key entry length.
        * Corrected the index of the last possible components of an extended key in the\
          function best\_access\_path().
      * [Revision #2502.538.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.538.1) \[merge]\
        Sat 2011-12-31 03:36:20 -0800
        * Merged [MWL#247](https://askmonty.org/worklog/?tid=247) into the latest 5.3.
        * [Revision #2502.537.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.537.1)\
          Sat 2011-12-31 02:25:57 -0800
          * Implementation of the [MWL#247](https://askmonty.org/worklog/?tid=247): Make the optimizer use extended keys.
          * The main patch.
* [Revision #3309](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3309)\
  Fri 2012-03-02 08:32:16 +0100
  * misc test/result fixes
* [Revision #3308](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3308) \[merge]\
  Fri 2012-03-02 07:45:06 +0100
  * Merge [MWL#234](https://askmonty.org/worklog/?tid=234): @@skip\_replication, into latest [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) for push
  * [Revision #3283.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3283.1.3)\
    Thu 2012-03-01 16:06:27 +0100
    * replicate\_events\_marked\_for\_skip does not exist in embedded.
  * [Revision #3283.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3283.1.2)\
    Thu 2012-03-01 13:12:49 +0100
    * Small cleanups:
      * use thd->in\_active\_multi\_stmt\_transaction() for\
        @@in\_transaction, not THD flag directly
      * use common error\_if\_in\_trans\_or\_substatement() function for\
        all 4 binlog variables that cannot be changed inside\
        statement or transaction.
  * [Revision #3283.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3283.1.1) \[merge]\
    Thu 2012-03-01 12:41:49 +0100
    * Merge [MWL#234](https://askmonty.org/worklog/?tid=234): @@skip\_replication feature to [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md).
    * [Revision #2502.536.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.536.4)\
      Tue 2011-08-16 11:51:02 +0200
      * [MWL#234](https://askmonty.org/worklog/?tid=234): Implement option to switch between master-side and client-side filtering of @@skip\_replication events.
    * [Revision #2502.536.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.536.3)\
      Mon 2011-08-15 10:05:14 +0200
      * [MWL#234](https://askmonty.org/worklog/?tid=234): Add MTR tests for SESSION/GLOBAL semantics of new system variables.
    * [Revision #2502.536.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.536.2)\
      Fri 2011-08-12 13:18:34 +0200
      * [MWL#234](https://askmonty.org/worklog/?tid=234): After-review fixes, including better names for the new system variables.
    * [Revision #2502.536.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.536.1)\
      Thu 2011-08-11 11:38:52 +0200
      * [MWL#234](https://askmonty.org/worklog/?tid=234): Support for marking binlog events to not be replicated, and for telling slaves not to replicate events with such mark
* [Revision #3307](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3307) \[merge]\
  Thu 2012-03-01 14:22:22 -0800
  * Merge 5.3->5.5.
  * [Revision #2502.513.70](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.70)\
    Wed 2012-02-29 23:28:16 -0800
    * Fixed [Bug #943543](https://bugs.launchpad.net/bugs/943543).
    * This bug appeared after the patch for bug 939009 that in the\
      function merge\_key\_fields forgot to reset a proper value for\
      the val field in the result of the merge operation of the key\
      field created for a regular key access and the key field\
      created to look for a NULL key.
    * Adjusted the results of the test case for bug 939009 that\
      actually were incorrect.
  * [Revision #2502.513.69](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.69)\
    Tue 2012-02-28 15:41:55 +0100
    * [Bug #938977](https://bugs.launchpad.net/bugs/938977) - Query performance with join/index super slow on [MariaDB 5.3.4](../../old-releases/5.3/5.3.4.md) RC
    * make sure that stored routines are evaluated (that is, de facto - cached) in convert\_const\_to\_int().
    * revert the fix for [Bug #806943](https://bugs.launchpad.net/bugs/806943) because it cannot be repeated anymore.
    * add few tests for convert\_const\_to\_int()
  * [Revision #2502.513.68](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.68) \[merge]\
    Tue 2012-02-28 15:04:31 +0100
    * merge
    * [Revision #2502.528.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.10) \[merge]\
      Tue 2012-02-28 13:50:30 +0200
      * Automatic merge
      * [Revision #2502.535.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.535.1)\
        Tue 2012-02-28 13:39:02 +0200
        * Fixed [Bug #905716](https://bugs.launchpad.net/bugs/905716) "Assertion \`page->size <= share->max\_index\_block\_size'"
        * The issue was that Aria allowed too long keys to be created (so that the internal buffer was not big enough to hold the whole key).
        * Key lengths is now limited to HA\_MAX\_KEY\_LENGTH (1000), as for MyISAM.
        * Fixed failure in "\_ma\_apply\_redo\_index: Assertion \`new\_page\_length == 0", as found by buildbot.
  * [Revision #2502.513.67](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.67) \[merge]\
    Sun 2012-02-26 03:13:33 -0800
    * Merge.
    * [Revision #2502.534.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.534.2) \[merge]\
      Sun 2012-02-26 02:42:45 -0800
      * Merge 5.2->5.3
      * [Revision #2502.528.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.9)\
        Sat 2012-02-25 17:10:07 -0800
        * Fixed [Bug #939866](https://bugs.launchpad.net/bugs/939866).
        * The field key\_cache\_mem\_size of the KEY\_CACHE structure must be\
          initialized in the function init\_key\_cache() and updated in the\
          function resize\_key\_cache().
      * [Revision #2502.528.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.8)\
        Sat 2012-02-25 09:03:06 +0200
        * Fix of [Bug #938518](https://bugs.launchpad.net/bugs/938518) (also [Bug #791761](https://bugs.launchpad.net/bugs/791761) and [Bug #806955](https://bugs.launchpad.net/bugs/806955))
        * Cause of the bug is uninitialized items before evaluation HAVING clasue in case of empty result.
    * [Revision #2502.534.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.534.1)\
      Sun 2012-02-26 00:19:07 -0800
      * Rolled back the patch for bug 791761.
      * A better fix for this bug will be pulled from mariadb-5.2.
  * [Revision #2502.513.66](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.66)\
    Sun 2012-02-26 11:44:52 +0400
    * Bump the version number.
  * [Revision #2502.513.65](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.65) \[merge]\
    Fri 2012-02-24 18:35:58 -0800
    * Merge.
    * [Revision #2502.533.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.533.1)\
      Fri 2012-02-24 16:50:22 -0800
      * Fixed [Bug #939009](https://bugs.launchpad.net/bugs/939009).
      * The result of materialization of the right part of an IN subquery predicate\
        is placed into a temporary table. Each row of the materialized table is\
        distinct. A unique key over all fields of the temporary table is defined and\
        created. It allows to perform key look-ups into the table.\
        The table created for a materialized subquery can be accessed by key as\
        any other table. The function best\_access-path search for the best access\
        to join a table to a given partial join. With some where conditions this\
        function considers a possibility of a ref\_or\_null access. If such access\
        employs the unique key on the temporary table then when estimating\
        the cost this access the function tries to use the array rec\_per\_key. Yet,\
        such array is not built for this unique key. This causes a crash of the server.
      * Rows returned by the subquery that contain nulls don't have to be placed\
        into temporary table, as they cannot be match any row produced by the\
        left part of the subquery predicate. So all fields of the temporary table\
        can be defined as non-nullable. In this case any ref\_or\_null access\
        to the temporary table does not make any sense and it does not make sense\
        to estimate such an access.
      * The fix makes sure that the temporary table for a materialized IN subquery\
        is defined with columns that are all non-nullable. The also ensures that\
        any row with nulls returned by the subquery is not placed into the\
        temporary table.
  * [Revision #2502.513.64](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.64)\
    Sat 2012-02-25 01:42:28 +0400
    * Update test results.
  * [Revision #2502.513.63](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.63)\
    Fri 2012-02-24 22:42:37 +0400
    * [Bug #938131](https://bugs.launchpad.net/bugs/938131): Subquery materialization is not used in `CREATE TABLE SELECT`
    * Enable subquery materialization for `CREATE TABLE ... SELECT`.
  * [Revision #2502.513.62](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.62) \[merge]\
    Fri 2012-02-24 20:07:12 +0400
    * Merge 5.2->5.3
    * [Revision #2502.528.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.7) \[merge]\
      Fri 2012-02-24 17:21:44 +0200
      * Automatic merge
      * [Revision #2502.352.77](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.352.77)\
        Fri 2012-02-24 17:01:47 +0200
        * Fix for [Bug #909635](https://bugs.launchpad.net/bugs/909635): MariaDB crashes on a select with long varchar and blob fields
        * Problem was a crash in internal temporary (Maria) files when row length exceeded 65535
    * [Revision #2502.528.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.528.6)\
      Wed 2012-02-22 00:10:39 -0800
      * Back-ported the fix and test cases for bugs #59487 and #43368 from\
        the mysql-5.6 code line.
  * [Revision #2502.513.61](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.513.61) \[merge]\
    Fri 2012-02-24 17:13:04 +0400
    * Merge fix for [Bug #934597](https://bugs.launchpad.net/bugs/934597)
    * [Revision #2502.532.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.532.1)\
      Fri 2012-02-24 17:09:13 +0400
      * [Bug #934597](https://bugs.launchpad.net/bugs/934597): Assertion \`! is\_set()' failed in Diagnostics\_area::set\_ok\_status(THD...
      * After the exec\_const\_cond->val\_int() call, check for error and return.
      * (if we don't do it, we will eventually hit an error when trying to set status OK in\
        the diagnostics area, which already has an error status).
* [Revision #3306](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3306)\
  Thu 2012-03-01 17:04:57 +0100
  * misc test/result fixes
* [Revision #3305](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3305)\
  Wed 2012-02-29 21:55:53 +0100
  * Make Tc\_log\_page\_size status variable use SHOW\_LONG\_NOFLUSH.
  * Otherwise XA crashes after FLUSH STATUS as log page size suddenly becomes 0.
* [Revision #3304](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3304)\
  Wed 2012-02-29 21:55:33 +0100
  * fixing pam plugin to compile again
* [Revision #3303](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3303)\
  Wed 2012-02-29 21:55:04 +0100
  * pbxt suite is now a main-pbxt overlay
* [Revision #3302](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3302)\
  Thu 2012-02-23 09:24:11 +0100
  * instead of having win/notwin tests that only differ in results,\
    use one test with two combinations (win/unix), where only one is enabled.
  * Apply this technique to `mysqld--help`.
* [Revision #3301](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3301)\
  Thu 2012-02-23 09:18:48 +0100
  * don't even try to run xtradb-only tests with innodb, use have\_xtradb.combinations.
* [Revision #3300](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3300)\
  Thu 2012-02-23 07:52:27 +0100
  * remove few .require files and one duplicate have\_\*inc file.
  * move variable tests from main to sys-vars
* [Revision #3299](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3299)\
  Thu 2012-02-23 07:50:43 +0100
  * HAVE\_STRNDUP check for pam plugin
* [Revision #3298](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3298)\
  Thu 2012-02-23 07:50:11 +0100
  * overlay support for mysql-test-run and mysqltest
  * mysql-test-run auto-disables all optional plugins.
* [Revision #3297](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3297)\
  Tue 2012-02-07 18:53:33 +0100
  * making more use of My::Suite object
* [Revision #3296](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3296)\
  Tue 2012-02-07 17:18:41 +0100
  * small cleanup
* [Revision #3295](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3295)\
  Tue 2012-02-07 16:22:36 +0100
  * allow suite.pm to skip combinations that originate from test/include files.
* [Revision #3294](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3294)\
  Mon 2012-02-06 23:16:21 +0100
  * mtr: support for rdiff files
* [Revision #3293](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3293)\
  Mon 2012-02-06 22:55:17 +0100
  * per-combination result files
* [Revision #3292](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3292)\
  Mon 2012-02-06 21:36:56 +0100
  * per-file combinations
* [Revision #3291](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3291)\
  Mon 2012-02-06 20:29:21 +0100
  * cleanup
* [Revision #3290](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3290)\
  Mon 2012-02-06 20:29:13 +0100
  * make %suites hash local to mtr\_cases.pm
* [Revision #3289](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3289)\
  Mon 2012-02-06 20:28:56 +0100
  * move `--secure-file-priv` from hardcoded to a template. remove redundant suite.opt
* [Revision #3288](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3288)\
  Mon 2012-02-06 18:42:18 +0100
  * remove few obscure, unused, or misused mtr features
* [Revision #3287](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3287)\
  Mon 2012-02-06 16:29:53 +0100
  * remove few hard-coded checks from mtr
* [Revision #3286](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3286)\
  Mon 2012-02-06 16:26:12 +0100
  * added plugin/auth\_pam/CMakeLists.txt
* [Revision #3285](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3285)\
  Thu 2012-03-01 16:24:59 +0100
  * fixes [Bug #922146](https://bugs.launchpad.net/bugs/922146) [MDEV-117](https://jira.mariadb.org/browse/MDEV-117)
  * [MDEV-117](https://jira.mariadb.org/browse/MDEV-117) Assertion: prebuilt->sql\_stat\_start || trx->conc\_state == 1 failed at row0sel.c:3933
  * DELETE IGNORE should not ignore deadlocks
* [Revision #3284](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3284)\
  Wed 2012-02-29 18:25:25 +0100
* fixes [Bug #942266](https://bugs.launchpad.net/bugs/942266)
  * Fix build error on Ubuntu 11.10, if systemtap is installed.
  * The error is due to conflict between min/max macros in my\_global.h\
    and system header < limits>, indirectly included via generated\
    probes\_mysql\_dtrace.h
  * Temporarily undefined min/max for the inclusion of the probes\_mysq\_dtrace.h
* [Revision #3283](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3283)\
  Tue 2012-02-28 18:53:05 +0100
  * Update copyright notices
* [Revision #3282](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3282) \[merge]\
  Tue 2012-02-28 13:16:17 +0100
  * merge threadpool
  * [Revision #3168.1.61](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.61)\
    Mon 2012-02-27 19:54:30 +0100
    * precache some more system checks on Windows
  * [Revision #3168.1.60](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.60)\
    Mon 2012-02-27 19:53:49 +0100
    * Remove libevent from sources - not needed now
  * [Revision #3168.1.59](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.59) \[merge]\
    Mon 2012-02-27 19:32:44 +0100
    * merge 5.5
    * [Revision #3281.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3281.1.1)\
      Mon 2012-02-27 19:20:18 +0100
      * because of the high cost associated with fake symdir resolution, disable symbolic-links on Windows by default. Real symlinks (Vista+) as well as NTFS junctions (prior to Vista) do not require this parameter
  * [Revision #3168.1.58](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.58)\
    Fri 2012-02-17 23:33:18 +0100
    * Simplify thd\_wait\_begin. given how seldom they are called, calling current\_thd one more time is not going to be anything performance relevant.
    * Also use thd\_wait\_begin/end for thr\_lock and sync callbacks.
  * [Revision #3168.1.57](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.57)\
    Fri 2012-02-17 23:27:15 +0100
    * Added copiright, some more comments
  * [Revision #3168.1.56](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.56)\
    Fri 2012-02-17 23:23:54 +0100
    * Store callback instance in the connection structure, to call CallbackMayRunLong on long\
      waits (currently binlog only)
    * Also add copyright notice.
  * [Revision #3168.1.55](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.55)\
    Fri 2012-02-17 03:34:33 +0100
    * fix windows embedded (default thread handling ==pool-of-threads does not work in embedded)
  * [Revision #3168.1.54](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.54)\
    Thu 2012-02-16 21:07:22 +0100
    * use poof-of-threads as default for thread\_handling on Windows
  * [Revision #3168.1.53](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.53)\
    Thu 2012-02-16 18:12:40 +0100
    * Only synchronous disk reads should use thd\_wait\_begin with THD\_WAIT\_DISKIO
  * [Revision #3168.1.52](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.52) \[merge]\
    Thu 2012-02-16 17:33:37 +0100
    * merge from 5.5
  * [Revision #3168.1.51](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.51)\
    Thu 2012-02-16 16:59:04 +0100
    * address second round review comments
  * [Revision #3168.1.50](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.50) \[
    * merge]\
      Wed 2012-02-08 11:18:55 +0100
    * merge
  * [Revision #3168.1.49](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.49)\
    Sat 2012-01-28 01:09:28 +0100
    * some more whitespace, remove pending\_thread\_start\_count. increment counters (thread\_group->count, thread\_group->active\_thread\_count) whenever mysql\_create\_thread returns success.
  * [Revision #3168.1.48](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.48)\
    Fri 2012-01-27 21:24:17 +0100
    * Fix test case - result file needs one-thread-per-connection
  * [Revision #3168.1.47](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.47)\
    Fri 2012-01-27 19:52:53 +0100
    * Threadpool : Rest of monty's review
  * [Revision #3168.1.46](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.46) \[
    * merge]\
      Fri 2012-01-27 00:40:12 +0100
    * merge
  * [Revision #3168.1.45](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.45)\
    Fri 2012-01-27 00:39:23 +0100
    * close callbacks prior to closing connection to avoid potential race when e.g timer callback and connection\_destroy run in parallel
  * [Revision #3168.1.44](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.44) \[
    * merge]\
      Thu 2012-01-26 20:09:25 +0100
    * merge
  * [Revision #3168.1.43](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.43)\
    Thu 2012-01-26 19:25:22 +0100
    * Disable perfschema/all\_instances for the threadpool (because of new mutexes and conditions)
  * [Revision #3168.1.42](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.42) \[
    * merge]\
      Thu 2012-01-26 17:35:01 +0100
    * merge
  * [Revision #3168.1.41](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.41)\
    Thu 2012-01-26 04:35:54 +0100
    * Further review points and simplify Windows implementation
  * [Revision #3168.1.40](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.40)\
    Wed 2012-01-25 03:59:09 +0100
    * add test thread\_pool\_min\_basic
  * [Revision #3168.1.39](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.39)\
    Tue 2012-01-24 19:18:22 +0100
    * further reduce diffs to 5.5, monty review
  * [Revision #3168.1.38](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.38)\
    Tue 2012-01-24 03:23:14 +0100
    * small cleanups
  * [Revision #3168.1.37](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.37)\
    Tue 2012-01-24 02:26:29 +0100
    * reduce diffs to the 5.5 version, remove random change in mysql-test-run.pl
  * [Revision #3168.1.36](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.36) \[
    * merge]\
      Tue 2012-01-24 01:59:03 +0100
    * merge
  * [Revision #3168.1.35](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.35)\
    Wed 2012-01-18 21:12:04 +0100
    * ensure that lock is held, whenever active thread counter changes.\
      It was not the case inside listener routine.
  * [Revision #3168.1.34](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.34)\
    Tue 2012-01-17 18:50:40 +0100
    * Threadpool : address some of the monty's review points\
      Also, print message when pool blocks.
  * [Revision #3168.1.33](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.33)\
    Mon 2012-01-16 02:18:24 +0100
    * Fix threadpool on BSD and Solaris
  * [Revision #3168.1.32](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.32)\
    Sun 2012-01-15 15:41:25 +0100
    * Get rid of idle thread counter atomic variable.
    * Instead, use function that loops over groups and\
      calculates idle threads for "show status".
  * [Revision #3168.1.31](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.31)\
    Sun 2012-01-15 11:17:45 +0100
    * Threadpool -address review comments
  * [Revision #3168.1.30](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.30)\
    Fri 2012-01-13 15:53:17 +0100
    * Simplify thread attach/detach. Use connection specific mysys\_var, rather than sharing worker thread's my\_thread\_var with THD.
  * [Revision #3168.1.29](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.29)\
    Thu 2012-01-12 13:40:09 +0100
    * fix kill test, again
  * [Revision #3168.1.28](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.28) \[merge]\
    Wed 2012-01-11 14:56:19 +0100
    * merge 5.5
  * [Revision #3168.1.27](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.27)\
    Tue 2012-01-10 16:58:30 +0100
    * [MDEV-82](https://jira.mariadb.org/browse/MDEV-82) : Fix place in thr\_lock.c where wait-end callback was called without corresponding wait-begin
  * [Revision #3168.1.26](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.26) \[merge]\
    Mon 2012-01-02 12:03:49 +0100
    * merge with 5.5
  * [Revision #3168.1.25](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.25)\
    Mon 2012-01-02 11:43:22 +0100
    * Fix crashes in windows-embedded
  * [Revision #3168.1.24](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.24)\
    Mon 2012-01-02 10:13:53 +0100
    * fix test
  * [Revision #3168.1.23](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.23)\
    Sat 2011-12-31 05:24:11 +0100
    * fixes [Bug #909774](https://bugs.launchpad.net/bugs/909774)
    * Allow for faster creation of threads in corner cases where pool would be overloaded with long non-yielding queries.
    * To allow it, change minimum of thread\_pool\_stall\_limit to be 10 milliseconds.
    * Also introduce a new parameter to oversubscribe a group . Number of threads running in parallel would be higher than it normally should, leading to thrashing, but it may improving preemptiveness, which is useful for the described corner case.
  * [Revision #3168.1.22](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.22)\
    Thu 2011-12-29 21:11:06 +0100
    * Make threadpool\_stall\_limit variable really dynamic
  * [Revision #3168.1.21](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.21)\
    Thu 2011-12-29 19:37:26 +0100
    * [Bug #909537](https://bugs.launchpad.net/bugs/909537): Ensure thd\_wait\_begin/thd\_wait\_end callbacks are called.
  * [Revision #3168.1.20](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.20)\
    Thu 2011-12-29 13:37:37 +0100
    * Fix valgrind errors with network timeouts.
  * [Revision #3168.1.19](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.19) \[
    * merge]\
      Thu 2011-12-29 12:54:40 +0100
    * merge
  * [Revision #3168.1.18](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.18)\
    Thu 2011-12-29 12:53:07 +0100
    * [Bug #909512](https://bugs.launchpad.net/bugs/909512): Fix crash on tp\_set\_threadpool\_size if threadpool is not used(thread\_handling != pool-of-threads)
  * [Revision #3168.1.17](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.17)\
    Thu 2011-12-29 12:17:30 +0100
    * Fix [Bug #909414](https://bugs.launchpad.net/bugs/909414): Valgrind warnings in threadpool code
  * [Revision #3168.1.16](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.16)\
    Thu 2011-12-29 01:59:05 +0100
    * bug: 9091416: destroy timer mutex when threadpool scheduler shuts down.
    * Fixes valgrind warning.
  * [Revision #3168.1.15](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.15)\
    Wed 2011-12-28 16:23:46 +0100
    * use performance-schema friendly mysql\_thread\_create() instead of pthread\_create()
  * [Revision #3168.1.14](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.14)\
    Wed 2011-12-28 03:51:12 +0100
    * fix result file
  * [Revision #3168.1.13](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.13)\
    Tue 2011-12-27 17:54:04 +0100
    * disable threadpool threads in sys\_var suite, when the suite runs with embedded server
  * [Revision #3168.1.12](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.12)\
    Tue 2011-12-27 16:10:34 +0100
    * fix test suite
  * [Revision #3168.1.11](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.11)\
    Tue 2011-12-27 12:20:06 +0100
    * fix embedded build and warning
  * [Revision #3168.1.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.10) \[
    * merge]\
      Mon 2011-12-26 16:57:28 +0100
    * merge
  * [Revision #3168.1.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.9)\
    Mon 2011-12-26 01:08:46 +0100
    * Fix build on old 32 bit Centos (kernel 2.6.18)
  * [Revision #3168.1.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.8)\
    Wed 2011-12-21 00:56:34 +0100
    * Fix threadpool related test failures
  * [Revision #3168.1.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.7)\
    Tue 2011-12-20 22:49:24 +0100
    * make sys\_vars suite pass
  * [Revision #3168.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.6)\
    Mon 2011-12-19 13:28:30 +0100
    * allow changing thread\_pool\_size without server restart
  * [Revision #3168.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.5)\
    Sun 2011-12-18 23:03:35 +0100
    * Fix pool\_of\_threads test case
  * [Revision #3168.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.4)\
    Sun 2011-12-18 20:40:38 +0100
    * Small adjustements to threadpool
  * [Revision #3168.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.3)\
    Wed 2011-12-14 23:16:50 +0100
    * On Unix, correct default threadpool\_idle\_timeout to be 60 sec
  * [Revision #3168.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.2)\
    Sat 2011-12-10 19:35:44 +0100
    * Fix Unix build
  * [Revision #3168.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3168.1.1)\
    Thu 2011-12-08 19:17:49 +0100
    * Initial threadpool implementation for [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md)
* [Revision #3281](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3281) \[merge]\
  Sun 2012-02-26 16:11:44 +0100
  * Merge [MWL#192](https://askmonty.org/worklog/?tid=192): non-blocking client library into MariaDB.
  * [Revision #3253.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3253.1.4)\
    Thu 2012-02-23 15:42:21 +0100
    * [MWL#192](https://askmonty.org/worklog/?tid=192) after-merge fixes.
      * Fix memory leak in one error case in mysqldump.
      * Fix that HAVE\_VALGRIND\_VALGRIND\_H is now HAVE\_VALGRIND in 5.5.
      * Fix that @have\_ssl should not be set in embedded (introduced when\
        removing #undef HAVE\_OPENSSL from my\_global.h).
  * [Revision #3253.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3253.1.3) \[merge]\
    Wed 2012-02-22 12:14:34 +0100
  * Merge latest [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) into [MWL#192](https://askmonty.org/worklog/?tid=192): Non-blocking client library.
  * [Revision #3253.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3253.1.2)\
    Wed 2012-02-22 11:44:53 +0100
  * Fix [MWL#192](https://askmonty.org/worklog/?tid=192) build error: Remove SSL special case for embedded server.
  * VIO has SSL in embedded server anyway, so we do not win anything by excluding it.
  * This was actually already done in this changeset:
    * revision-id: kostja@sun.com-20100413150445-8x23keoxdiufgq76
    * "... Also, he removed the (probable) bug of embedded server never using SSL-dependent functions..."
  * But was apparenly lost by a mis-merge of [WL#5030](https://askmonty.org/worklog/?tid=5030).
  * [Revision #3253.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3253.1.1) \[merge]\
    Tue 2012-02-21 22:15:44 +0100
    * Merge [MWL#192](https://askmonty.org/worklog/?tid=192): Non-blocking client library, into [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md).
    * [Revision #2502.531.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.531.5)\
      Mon 2012-01-30 13:45:58 +0100
      * [MWL#192](https://askmonty.org/worklog/?tid=192): Fix problem when we first enable MYSQL\_OPT\_NONBLOCK, then connect\
        in normal blocking style, then later do a non-blocking operation.
      * In this case, the vio->async\_context was not set up correctly, so that\
        non-blocking operation was not properly handled.
    * [Revision #2502.531.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.531.4)\
      Sun 2012-01-08 10:13:39 +0100
      * Fix non-ssl build.
    * [Revision #2502.531.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.531.3)\
      Sat 2012-01-07 23:20:08 +0100
      * fix typo.
    * [Revision #2502.531.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.531.2)\
      Fri 2012-01-06 12:43:18 +0100
      * [MWL#192](https://askmonty.org/worklog/?tid=192): non-blocking client API, after-review fixes.
      * Main change is that non-blocking operation is now an option that must be\
        explicitly enabled with mysql\_option(mysql, MYSQL\_OPT\_NONBLOCK, ...)\
        before any non-blocing operation can be used.
      * Also the CLIENT\_REMEMBER\_OPTIONS flag is now always enabled and thus\
        effectively ignored (it was not really useful anyway, and this simplifies\
        things when non-blocking mysql\_real\_connect() fails).
    * [Revision #2502.531.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/2502.531.1)\
      Tue 2011-09-20 12:49:25 +0200
      * [MWL#192](https://askmonty.org/worklog/?tid=192): Non-blocking client API for libmysqlclient.
      * All client functions that can block on I/O have alternate \_start() and\
        \_cont() versions that do not block but return control back to the\
        application, which can then issue I/O wait in its own fashion and later\
        call back into the library to continue the operation.
      * Works behind the scenes by spawning a co-routine/fiber to run the\
        blocking operation and suspend it while waiting for I/O. This\
        co-routine/fiber use is invisible to applications.
      * For i368/x86\_64 on GCC, uses very fast assembler co-routine support. On\
        Windows uses native Win32 Fibers. Falls back to POSIX ucontext on other\
        platforms. Assembler routines for more platforms are relatively easy to\
        add by extending mysys/my\_context.c, eg. similar to the Lua lcoco\
        library.
      * For testing, mysqltest and mysql\_client\_test are extended with the\
        option `--non-blocking-api`. This causes the programs to use the\
        non-blocking API for database access. mysql-test-run.pl has a similar\
        option `--non-blocking-api` that uses this, as well as additional\
        testcases.
      * An example program tests/async\_queries.c is included that uses the new\
        non-blocking API with libevent to show how, in a single-threaded\
        program, to issue many queries in parallel against a database.
* [Revision #3280](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3280)\
  Sat 2012-02-25 16:13:24 +0100
  * make the test result independent from sizeof(void\*)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
