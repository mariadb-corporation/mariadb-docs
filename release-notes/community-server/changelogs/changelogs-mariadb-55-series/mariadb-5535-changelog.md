# MariaDB 5.5.35 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.35) |[Release Notes](../../old-releases/5.5/5.5.35.md) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 29 Jan 2014

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.35.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4052](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4052) \[merge]\
  Tue 2014-01-28 10:58:18 +0100
  * 5.3 merge
  * [Revision #2502.567.190](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.190) \[merge]\
    Tue 2014-01-28 10:27:52 +0100
    * 5.2 merge
    * [Revision #2502.566.61](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.61) \[merge]\
      Tue 2014-01-28 10:23:11 +0100
      * 5.1 merge
      * [Revision #2502.565.64](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.64)\
        Tue 2014-01-28 10:21:47 +0100
        * fixed a client-side overflow in mysql cli
* [Revision #4051](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4051)\
  Tue 2014-01-28 11:12:43 +0400
  * [MDEV-5345](https://jira.mariadb.org/browse/MDEV-5345) - Deadlock between mysql\_change\_user(), SHOW VARIABLES and INSTALL PLUGIN
* [Revision #4050](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4050) \[merge]\
  Tue 2014-01-28 13:00:50 +0400
  * merge 5.3 -> 5.5
  * [Revision #2502.567.189](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.189)\
    Tue 2014-01-28 12:25:29 +0400
    * [MDEV-5506](https://jira.mariadb.org/browse/MDEV-5506) safe\_mutex: Trying to lock unitialized mutex at safemalloc.c on server shutdown after SELECT with CONVERT\_TZ
* [Revision #4049](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4049)\
  Mon 2014-01-27 20:50:32 +0100
  * [MDEV-5576](https://jira.mariadb.org/browse/MDEV-5576) ALTER TABLE progress report > 100%
* [Revision #4048](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4048)\
  Mon 2014-01-27 16:58:26 +0100
  * [MDEV-4787](https://jira.mariadb.org/browse/MDEV-4787) Missing dependency to "patch" for the Debian/Ubuntu "mariadb-test" package
* [Revision #4047](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4047)\
  Mon 2014-01-27 12:11:04 +0100
  * [MDEV-5405](https://jira.mariadb.org/browse/MDEV-5405) RQG induced crash in mi\_assign\_to\_key\_cache in safe mutex unlock
* [Revision #4046](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4046)\
  Mon 2014-01-27 12:10:53 +0100
  * mtr: check that tests clean up debug\_sync. fix tests that didn't.
* [Revision #4045](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4045)\
  Sun 2014-01-26 21:49:39 +0100
  * improve oqgraph boost check to filter out newer boost versions
* [Revision #4044](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4044)\
  Sun 2014-01-26 21:49:31 +0100
  * workaround test failures in buildbot: in some VMs readline thinks that the window size is zero. ignore it.
* [Revision #4043](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4043)\
  Sun 2014-01-26 21:49:19 +0100
  * [MDEV-5461](https://jira.mariadb.org/browse/MDEV-5461) Assertion \`length <= column->length' fails in write\_block\_record with functions in select list, GROUP BY, ORDER BY
* [Revision #4042](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4042)\
  Sun 2014-01-26 21:49:11 +0100
  * move innodb specific test from group\_by.test to group\_by\_innodb.test
* [Revision #4041](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4041)\
  Sun 2014-01-26 21:49:04 +0100
  * fix the test for [MDEV-5029](https://jira.mariadb.org/browse/MDEV-5029) to clean up after itself
* [Revision #4040](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4040)\
  Sun 2014-01-26 21:48:42 +0100
  * Fix for [MDEV-5168](https://jira.mariadb.org/browse/MDEV-5168): MariaDB returns warnings for INSERT IGNORE
* [Revision #4039](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4039)\
  Sun 2014-01-26 21:48:23 +0100
  * Fixed that setup\_natural\_join\_row\_types can safely be called twice
* [Revision #4038](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4038)\
  Sun 2014-01-26 21:47:31 +0100
  * Fixed bug that I accidently introduced in mysql\_tzinfo\_to\_sql Added test cases
* [Revision #4037](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4037)\
  Sun 2014-01-26 20:46:15 +0200
  * speed up tokudb tests by adding begin/commit around insert loops Marked very long running tests as big\_test
* [Revision #4036](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4036)\
  Sat 2014-01-25 15:41:08 +0200
  * Fixed [MDEV-4970](https://jira.mariadb.org/browse/MDEV-4970): Wrong result with Aria table populated with disabled keys
* [Revision #4035](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4035) \[merge]\
  Mon 2014-01-27 15:05:23 +0400
  * Merge 5.3 -> 5.5
  * [Revision #2502.567.188](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.188)\
    Mon 2014-01-27 13:15:40 +0400
    * [MDEV-5458](https://jira.mariadb.org/browse/MDEV-5458) RQG hits 'sql/tztime.cc:799: my\_time\_t sec\_since\_epoch(...): Assertion \`mon > 0 && mon < 13' failed.'
* [Revision #4034](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4034) \[merge]\
  Mon 2014-01-27 13:14:00 +0400
  * Merge 5.3 -> 5.5
  * [Revision #2502.567.187](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.187)\
    Sat 2014-01-25 00:26:40 +0400
    * \[Backport to 5.3] [MDEV-5337](https://jira.mariadb.org/browse/MDEV-5337): Wrong result in [mariadb 5.5.32](../../old-releases/5.5/5.5.32.md) with ORDER BY + LIMIT when index\_condition\_pushdown=on
    * in test\_if\_skip\_sort\_order(), correct the condition under which we have the code that restores the previously pushed index condition.
  * [Revision #2502.567.186](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.186)\
    Fri 2014-01-24 16:50:39 +0400
    * [MDEV-5504](https://jira.mariadb.org/browse/MDEV-5504) Server crashes in String::length on SELECT with MONTHNAME, GROUP BY, ROLLUP
  * [Revision #2502.567.185](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.185)\
    Thu 2014-01-23 21:26:04 +0400
    * [MDEV-5368](https://jira.mariadb.org/browse/MDEV-5368): Server crashes in Item\_in\_subselect::optimize on ...
    * convert\_subq\_to\_sj() must connect child select's tables into parent select's TABLE\_LIST::next\_local chain.
    * The problem was that it took child's leaf\_tables.head() which is different. This could cause certain tables (in this bug's case, child select's non-merged semi-join) not to be present in TABLE\_LIST::next\_local chain. Which would cause non-merged semi-join not to be initialized in setup\_tables(), which would lead to NULL pointer dereference.
* [Revision #4033](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4033) \[merge]\
  Sun 2014-01-26 16:41:15 +0200
  * merge 5.3->5.5
  * [Revision #2502.567.184](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.184) \[merge]\
    Thu 2014-01-23 12:05:10 +0200
    * merge of [MDEV-5356](https://jira.mariadb.org/browse/MDEV-5356) 5.1->5.3 (with more fixes and test suite).
    * [Revision #2502.565.63](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.63)\
      Thu 2014-01-23 11:11:01 +0200
      * [MDEV-5356](https://jira.mariadb.org/browse/MDEV-5356): Server crashes in Item\_equal::contains on 2nd execution of a PS THD::thd->activate\_stmt\_arena\_if\_needed() should be used to temporary activating statement arena instead of direct usage of THD::set\_n\_backup\_active\_arena() because possible such scenario:
        1. func1 saves current arena and activates copy1 of statement arena
        2. func2 saves copy1 of statement arena setup by func1 and activates copy2
        3. some changes made for copy 2
        4. func2 stores changed copy2 back to statenet arena and activates copy1
        5. func1 store unchanged copy1 back to statemnt arena (rewrite changed copy 2 so changes become lost) and activates arena which was before.
  * [Revision #2502.567.183](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.183) \[merge]\
    Tue 2014-01-21 09:56:12 +0100
    * 5.2 merge
    * [Revision #2502.566.60](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.60) \[merge]\
      Tue 2014-01-21 09:41:28 +0100
      * 5.1 merge
      * [Revision #2502.565.62](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.62)\
        Mon 2014-01-20 20:53:39 +0100
        * fix a warning
      * [Revision #2502.565.61](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.61)\
        Mon 2014-01-20 19:09:01 +0100
        * [MDEV-5543](https://jira.mariadb.org/browse/MDEV-5543) MyISAM repair unsafe usage of TMD files
      * [Revision #2502.565.60](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.60)\
        Fri 2013-12-20 12:35:47 +0200
        * make 5.1 compiling with modern gcc.
* [Revision #4032](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4032) \[merge]\
  Fri 2014-01-24 23:44:52 +0400
  * Merge
  * [Revision #4026.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4026.1.1)\
    Fri 2014-01-24 23:40:48 +0400
    * [MDEV-5337](https://jira.mariadb.org/browse/MDEV-5337): Wrong result in [mariadb 5.5.32](../../old-releases/5.5/5.5.32.md) with ORDER BY + LIMIT when index\_condition\_pushdown=on
    * in test\_if\_skip\_sort\_order(), correct the condition under which we have the code that restores the previously pushed index condition.
* [Revision #4031](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4031)\
  Fri 2014-01-24 19:44:13 +0200
  * Fixed Mageia Bug 12355: mariadb produces warning messages while loading timezone information
  * Warnings about wrong symlink messages or non-timezone files with '.tab' are now only given if run with `--verbose`
  * Added long option handling
  * Added `--help`, `--verbose` and `--version` options
* [Revision #4030](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4030)\
  Fri 2014-01-24 14:50:18 +0200
  * Fix for [MDEV-5531](https://jira.mariadb.org/browse/MDEV-5531): double call procedure in one session
  * hard shutdown the server Main fix was to not cache derivied tables as they may be temporary tables that are deleted before the next query. This was a bit tricky as Item\_field::fix\_fields depended on cached\_tables to be set to resolve some columns.
* [Revision #4029](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4029)\
  Fri 2014-01-24 14:30:19 +0200
  * Fixed failures in tokudb test cases
* [Revision #4028](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4028)\
  Fri 2014-01-24 06:07:22 +0400
  * [MDEV-5419](https://jira.mariadb.org/browse/MDEV-5419) no audit events for warnings converted to errors in the strict mode. small fix in the `--replace_regex` template.
* [Revision #4027](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4027)\
  Thu 2014-01-23 22:21:02 +0400
  * [MDEV-5419](https://jira.mariadb.org/browse/MDEV-5419) no audit events for warnings converted to errors in the strict mode. Plugins get error notifications only when my\_message\_sql() is called. But errors are launched with THD::raise\_condition() calls in other places. These are push\_warning(), implementations of SIGNAL and RESIGNAL commands. So it makes sence to notify plugins there in THD::raise\_condition().
* [Revision #4026](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4026) \[merge]\
  Thu 2014-01-23 21:12:37 +0400
  * Merge
  * [Revision #4013.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4013.1.1)\
    Thu 2014-01-23 15:41:51 +0400
    * [MDEV-5368](https://jira.mariadb.org/browse/MDEV-5368): Server crashes in Item\_in\_subselect::optimize on ...
    * convert\_subq\_to\_sj() must connect child select's tables into parent select's TABLE\_LIST::next\_local chain.
    * The problem was that it took child's leaf\_tables.head() which is different. This could cause certain tables (in this bug's case, child select's non-merged semi-join) not to be present in TABLE\_LIST::next\_local chain. Which would cause non-merged semi-join not to be initialized in setup\_tables(), which would lead to NULL pointer dereference.
* [Revision #4025](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4025)\
  Thu 2014-01-23 11:04:59 +0100
  * [MDEV-5406](https://jira.mariadb.org/browse/MDEV-5406) add index to an innodb table with a uniqueness violation crashes mysqld
* [Revision #4024](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4024)\
  Thu 2014-01-23 00:03:05 +0100
  * [MDEV-5421](https://jira.mariadb.org/browse/MDEV-5421) Assertion \`! is\_set()' fails on INSERT IGNORE when a table has no partition for a value
* [Revision #4023](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4023)\
  Thu 2014-01-23 00:02:52 +0100
  * [MDEV-5550](https://jira.mariadb.org/browse/MDEV-5550) Invalid cmake variable in mysql-test/CMakeLists.txt
* [Revision #4022](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4022)\
  Thu 2014-01-23 00:02:37 +0100
  * Change our INSTALL\_DEBUG\_SYMBOLS cmake function to be less picky and support MySQL CMakeLists.txt files
* [Revision #4021](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4021)\
  Thu 2014-01-23 00:02:22 +0100
  * update debian patches to match the current code state
* [Revision #4020](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4020)\
  Thu 2014-01-23 00:02:08 +0100
  * fix XtraDB to compile on Windows
* [Revision #4019](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4019)\
  Wed 2014-01-22 23:59:21 +0100
  * update test results, broken by [MDEV-5547](https://jira.mariadb.org/browse/MDEV-5547) fix
* [Revision #4018](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4018) \[merge]\
  Wed 2014-01-22 15:35:42 +0100
  * Percona-Server-5.5.35-rel33.0.tar.gz
  * [Revision #0.12.66](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.66)\
    Wed 2014-01-22 10:03:32 +0100
    * Percona-Server-5.5.35-rel33.0.tar.gz
* [Revision #4017](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4017) \[merge]\
  Wed 2014-01-22 15:29:36 +0100
  * MySQL-5.5.35 merge
* [Revision #4016](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4016)\
  Tue 2014-01-21 17:20:51 +0100
  * clarify plugin-load usage in tokudb.cnf file
* [Revision #4015](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4015)\
  Tue 2014-01-21 17:20:44 +0100
  * remove an unused error message
* [Revision #4014](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4014)\
  Wed 2014-01-22 15:16:57 +0200
  * Fix for [MDEV-5547](https://jira.mariadb.org/browse/MDEV-5547): Bad error message when moving very old .frm files to [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md). mysql\_upgrade `--help` now also prints out `--default` options and variable values. mysql\_upgrade now prints permission errors. mysql\_upgrade doesn't print some non essential info if `--silent` is used. Added handler error message about incompatible versions Fixed that mysqlbug and mysql\_install\_db have the executable flag set. Removed executable flag for some non executable files. Changed in mysql\_install\_db askmonty.org to mariadb.com. Ensured that all client executables prints `--default` options the same way. Allow REPAIR ... USE\_FRM for old .frm files if the are still compatible. Extended shown error for storage engine messages.
* [Revision #4013](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4013)\
  Tue 2014-01-21 17:27:36 +0400
  * [MDEV-4974](https://jira.mariadb.org/browse/MDEV-4974): memory leak in 5.5.32-MariaDB-1wheezy-log
  * When a JOIN has both "optimization tabs" (JOIN\_TABs used to read the base tables and do the join operation) and also has "execution tabs" (a JOIN\_TAB that is to produce result set that is sent to the client), do not forget to call JOIN\_TAB::cleanup() for the execution JOIN\_TAB.
* [Revision #4012](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4012) \[merge]\
  Wed 2014-01-15 16:07:50 +0200
  * Merge 5.3->5.5
  * [Revision #2502.567.182](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.182)\
    Mon 2014-01-13 21:30:42 +0200
    * [MDEV-5515](https://jira.mariadb.org/browse/MDEV-5515): 2nd execution of a prepared statement returns wrong results
  * [Revision #2502.567.181](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.181)\
    Wed 2013-12-18 15:59:51 +0200
    * [MDEV-5414](https://jira.mariadb.org/browse/MDEV-5414): RAND() in a subselect : different behavior in MariaDB and MySQL
* [Revision #4011](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4011)\
  Sun 2014-01-05 15:21:58 +0200
  * Don't writing entries to slave log about binlog\_checksum not existing on master if log\_warnings is <=1.
* [Revision #4010](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4010)\
  Thu 2014-01-02 15:51:02 +0200
  * Fixed [MDEV-5424](https://jira.mariadb.org/browse/MDEV-5424): SELECT using ORDER BY DESC and LIMIT produces unexpected results (InnoDB/XtraDB) This only happend when using an ORDER BY on a primary key part, where all other key parts where constant. Remove of duplicated expressions in ORDER BY (as the old code did this in some strange cases)
* [Revision #4009](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4009)\
  Mon 2013-12-30 20:30:29 +0400
  * [MDEV-5349](https://jira.mariadb.org/browse/MDEV-5349): Test main.subselect\_sj\_jcl6 fails sporadically due to insufficient ordering
  * Add `--sorted_result` to the query
* [Revision #4008](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4008)\
  Tue 2013-12-17 17:26:54 +0100
  * [MDEV-5396](https://jira.mariadb.org/browse/MDEV-5396) Assertion \`Handlerton: r==0 ' failed (errno=0) on EXPLAIN with TokuDB tables
* [Revision #4007](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4007)\
  Tue 2013-12-17 15:19:26 +0400
  * [MDEV-5453](https://jira.mariadb.org/browse/MDEV-5453) Assertion \`src' fails in my\_strnxfrm\_unicode on GROUP BY MID(..) WITH ROLLUP Fixed a wrong assertion.
* [Revision #4006](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4006)\
  Sun 2013-12-15 15:55:15 +0100
  * don't run tokudb tests for `--embedded` by default
* [Revision #4005](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4005)\
  Sun 2013-12-15 11:31:57 +0100
  * Fix tokudb.hotindex-insert-bigchar failure in buildbot. This test needs at least 320M for tokudb-max-lock-memory. Normally tokudb-max-lock-memory is auto-sized to be 1/16th of the available RAM size, and many our test VMs have 4G of RAM.
* [Revision #4004](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4004) \[merge]\
  Fri 2013-12-13 13:00:38 +0100
  * 5.3 merge
  * [Revision #2502.567.180](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.180)\
    Thu 2013-12-12 13:55:33 -0800
    * Fixed bug [MDEV-5410](https://jira.mariadb.org/browse/MDEV-5410). The fix for bug #27937 was incomplete: it did not handle correctly the queries containing UNION with global ORDER BY in subselects.
  * [Revision #2502.567.179](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.179)\
    Wed 2013-12-11 10:13:08 -0800
    * Another attempt to fix the memory leak of [MDEV-5400](https://jira.mariadb.org/browse/MDEV-5400).
  * [Revision #2502.567.178](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.178)\
    Sat 2013-12-07 07:51:02 -0800
    * Fixed bug [MDEV-5400](https://jira.mariadb.org/browse/MDEV-5400): a memory leak in save\_index() first seen in the test case for [MDEV-5382](https://jira.mariadb.org/browse/MDEV-5382).
  * [Revision #2502.567.177](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.177) \[merge]\
    Thu 2013-12-05 12:40:04 -0800
    * Merge
    * [Revision #2502.582.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.582.1)\
      Thu 2013-12-05 11:13:20 -0800
      * Fixed bug [MDEV-5382](https://jira.mariadb.org/browse/MDEV-5382) When marking used columns the function find\_field\_in\_table\_ref() erroneously called the walk method for the real item behind a view/derived table field with the second parameter set to TRUE. This erroneous code was introduced in 2006.
  * [Revision #2502.567.176](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.176)\
    Wed 2013-12-04 16:54:33 +0200
    * [MDEV-5353](https://jira.mariadb.org/browse/MDEV-5353): server crash on subselect if WHERE applied to some result field
  * [Revision #2502.567.175](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.175)\
    Tue 2013-12-03 15:08:43 +0400
    * [MDEV-5374](https://jira.mariadb.org/browse/MDEV-5374) main.func\_time fails with valgrind warning "Conditional jump or move depends on uninitialised" in Item\_time\_typecast::get\_date.
  * [Revision #2502.567.174](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.174) \[merge]\
    Mon 2013-12-02 12:32:43 +0100
    * 5.2 merge
    * [Revision #2502.566.59](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.59) \[merge]\
      Sun 2013-12-01 20:12:19 +0100
      * 5.1 merge
      * [Revision #2502.565.59](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.59)\
        Fri 2013-11-29 20:21:05 +0100
        * [MDEV-5266](https://jira.mariadb.org/browse/MDEV-5266) MySQL:57657 - Temporary MERGE table with temporary underlying is broken by ALTER
* [Revision #4003](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4003)\
  Thu 2013-12-12 18:14:14 +0100
  * my\_addr\_resolve: don't resolve unknown addresses to ??:0(??), but return an error instead
* [Revision #4002](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4002)\
  Thu 2013-12-12 18:14:08 +0100
  * backport from 10.0: "bugfix: MYSQL\_THDVAR\_STR plugins with PLUGIN\_VAR\_MEMALLOC didn't work
* [Revision #4001](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4001)\
  Thu 2013-12-12 14:58:44 +0100
  * fix tokudb tests that fail in `--ps-protocol`
* [Revision #4000](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4000)\
  Thu 2013-12-12 11:42:00 +0100
  * update tokudb version. mask tests that are broken there.
* [Revision #3999](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3999)\
  Wed 2013-12-11 17:42:33 +0100
  * [MDEV-5323](https://jira.mariadb.org/browse/MDEV-5323) Ctrl-C not working under Ubuntu
* [Revision #3998](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3998)\
  Fri 2013-12-06 15:29:25 +0100
  * install embedded\_priv.h in ${INSTALL\_INCLUDEDIR}/private
* [Revision #3997](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3997)\
  Wed 2013-11-27 21:58:47 +0100
  * install and package plugin suites.
* [Revision #3996](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3996)\
  Wed 2013-11-27 21:58:36 +0100
  * mysql-test: allow suite.pm add its suite to the default list. run tokudb suites by default. mark big and slow tests tokudb.change\_column\_all\_1000\_1 and tokudb.change\_column\_all\_1000\_10 test as `--big`
* [Revision #3995](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3995)\
  Wed 2013-11-20 12:18:46 +0100
  * [MDEV-5303](https://jira.mariadb.org/browse/MDEV-5303) rpm post-inst scriptlet creates mysql user with a valid shell
* [Revision #3994](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3994)\
  Wed 2013-11-20 11:50:27 +0100
  * set CMP0022 policy to avoid cmake warnings
* [Revision #3993](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3993)\
  Mon 2013-12-02 22:22:43 +0200
  * Fixed compiler errors and warnings
* [Revision #3992](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3992) \[merge]\
  Mon 2013-12-02 15:50:35 +0400
  * Merge 5.3->5.5 pending merges: Alexander Barkov 2013-12-02 [MDEV-4857](https://jira.mariadb.org/browse/MDEV-4857) Wrong result of HOUR('1 00:00:00')
  * [Revision #2502.567.173](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.173)\
    Mon 2013-12-02 15:09:34 +0400
    * [MDEV-4857](https://jira.mariadb.org/browse/MDEV-4857) Wrong result of HOUR('1 00:00:00')
* [Revision #3991](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3991) \[merge]\
  Mon 2013-12-02 15:17:21 +0400
  * Merge 5.3 -> 5.5 pending merges: Sergey Petrunya 2013-11-27 [MDEV-5344](https://jira.mariadb.org/browse/MDEV-5344): LEFT OUTER JOIN table data is lost...
  * [Revision #2502.567.172](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.172)\
    Wed 2013-11-27 17:43:16 +0400
    * [MDEV-5344](https://jira.mariadb.org/browse/MDEV-5344): LEFT OUTER JOIN table data is lost in ON DUPLICATE KEY UPDATE section
    * For INSERT ... SELECT ... ON DUPLICATE KEY UPDATE, table elimination should check which tables are referenced in the ON DUPLICATE KEY UPDATE clause.
* [Revision #3990](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3990) \[merge]\
  Thu 2013-11-28 20:02:51 +0400
  * Fixes for storage\_engine tests
  * [Revision #3985.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3985.1.1)\
    Thu 2013-11-28 19:54:07 +0400
    * A fix for MySQL#65146 introduced a new warning. Minor wording changes in skip messages.
* [Revision #3989](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3989)\
  Thu 2013-11-28 11:34:43 +0200
  * Add additional srv\_use\_fallocate guard for completing the IO with read.
* [Revision #3988](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3988)\
  Wed 2013-11-27 20:24:52 +0200
  * [MDEV-5355](https://jira.mariadb.org/browse/MDEV-5355): InnoDB assertion at shutdown if posix\_fallocate is used in ut\_a(node->n\_pending == 0 || node->space->stop\_new\_ops);
* [Revision #3987](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3987)\
  Mon 2013-11-25 21:38:01 +0400
  * [MDEV-5321](https://jira.mariadb.org/browse/MDEV-5321) Calling mysql\_library\_end accesses freed memory; dumps memory to display.
  * Don't call the vio\_end() in the clean\_up() in EMBEDDED mode.
  * Call vio\_end() before the end\_embedded\_server().
* [Revision #3986](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3986)\
  Mon 2013-11-25 13:01:57 -0500
  * Fix for a compiler warning.
* [Revision #3985](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3985) \[merge]\
  Sun 2013-11-24 22:10:36 -0800
  * Merge
  * [Revision #2502.567.171](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.171)\
    Sun 2013-11-24 20:45:16 -0800
    * Made sure that JOIN::cond\_equal is correctly set after the call of remove\_eq\_conds() in the function make\_join\_statistics().
* [Revision #3984](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3984) \[merge]\
  Fri 2013-11-22 18:38:13 -0800
  * Merge
  * [Revision #2502.567.170](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.170)\
    Fri 2013-11-22 13:13:03 -0800
    * Post-review changes of the patch for bug [MDEV-5103](https://jira.mariadb.org/browse/MDEV-5103).
* [Revision #3983](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3983)\
  Fri 2013-11-22 20:03:36 +0400
  * Increment the version number
* [Revision #3982](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3982)\
  Fri 2013-11-22 12:20:29 +0400
  * A clean-up for the previous commit (mtr mysql\_tzinfo\_to\_sql\_symlink)
* [Revision #3981](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3981)\
  Fri 2013-11-22 11:52:19 +0400
  * "mtr mysql\_tzinfo\_to\_sql\_symlink" failed in out-of-source builds with this error: mysql-test-run: ERROR: Could not find any of /mariadb-5.5.34/sql/mysql\_tzinfo\_to\_sql /mariadb-5.5.34/build/client/mysql\_tzinfo\_to\_sql Fixed the directory list to search mysql\_tzinfo\_to\_sql binary in.
* [Revision #3980](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3980) \[merge]\
  Thu 2013-11-21 21:40:43 -0800
  * Merge 5.3->5.5
  * [Revision #2502.567.169](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.169) \[merge]\
    Thu 2013-11-21 18:28:20 -0800
    * Merge
    * [Revision #2502.581.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.581.1)\
      Thu 2013-11-21 15:19:25 -0800
      * Another attempt to fix bug [MDEV-5103](https://jira.mariadb.org/browse/MDEV-5103). The earlier pushed fix for the bug was incomplete. It did not remove the main cause of the problem: the function remove\_eq\_conds() removed always true multiple equalities from any conjunct, but did not adjust the list of them stored in Item\_cond\_and::cond\_equal.current\_level.
* [Revision #3979](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3979)\
  Thu 2013-11-21 13:35:20 +0400
  * [MDEV-5059](https://jira.mariadb.org/browse/MDEV-5059): Wrong result (missing row) wih semijoin, join\_cache\_level > 2, LEFT JOIN, ORDER BY
  * Added testcase
* [Revision #3978](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3978) \[merge]\
  Thu 2013-11-21 11:21:53 +0400
  * Merge
  * [Revision #3963.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3963.1.2)\
    Thu 2013-11-21 11:19:01 +0400
    * [MDEV-5161](https://jira.mariadb.org/browse/MDEV-5161): Wrong result (missing rows) with semijoin, LEFT JOIN, ORDER BY, constant table
    * Don't pull out a table out of a semi-join if it is on the inner side of an outer join.
    * Make join->sort\_by\_table= get\_sort\_by\_table(...) call after const table detection is done. That way, the value of join->sort\_by\_table will match the actual execution. Which will allow the code in setup\_semijoin\_dups\_elimination() (search for "Make sure that possible sorting of rows from the head table is not to be employed." to see that "Using filesort" is going to be used together with Duplicate Elimination ( and change it to Using temporary + Using filesort)
  * [Revision #3963.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3963.1.1)\
    Mon 2013-11-18 12:26:25 +0400
    * [MDEV-5293](https://jira.mariadb.org/browse/MDEV-5293): outer join, join buffering, and order by
    * invalid query plan
    * make\_join\_readinfo() has the code that forces use of "Using temporary; Using filesort" when join buffering is in use. That code didn't handle all cases, in particular it didn't hande the case where ORDER BY originally has tables from multiple columns, but the optimizer eventually figures out that doing filesort() on one table will be sufficient. Adjusted the code to handle that case.
* [Revision #3977](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3977) \[merge]\
  Thu 2013-11-21 13:09:08 +0400
  * Merge 5.3->5.5
  * [Revision #2502.567.168](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.168)\
    Thu 2013-11-21 11:46:36 +0400
    * [MDEV-4859](https://jira.mariadb.org/browse/MDEV-4859) Wrong value and data type of "SELECT MAX(time\_column) + 1 FROM t1" Fixed.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
