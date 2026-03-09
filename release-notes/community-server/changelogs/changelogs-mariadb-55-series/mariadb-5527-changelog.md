# MariaDB 5.5.27 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.27) |[Release Notes](../../old-releases/5.5/5.5.27.md) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 07 Sep 2012

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.27.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3527](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3527)\
  Thu 2012-09-06 10:08:09 +0200
  * [MDEV-510](https://jira.mariadb.org/browse/MDEV-510) assert triggered by `./mtr --ps-protocol rpl_mdev382`
  * The DELETE for emplicitly emptied MEMORY tables should be written directly to binlog.
* [Revision #3526](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3526) \[merge]\
  Thu 2012-09-06 00:14:33 +0300
  * merge 5.3->5.5
  * [Revision #2502.567.18](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.18)\
    Wed 2012-09-05 23:23:58 +0300
    * [MDEV-486](https://jira.mariadb.org/browse/MDEV-486) [Bug #1010116](https://bugs.launchpad.net/bugs/1010116) fix.
    * Link view/derived table fields to a real table to check turning the table record to null row.
    * Item\_direct\_view\_ref wrapper now checks if table is turned to null row.
  * [Revision #2502.567.17](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.17)\
    Fri 2012-08-31 19:50:45 +0500
    * [Bug #1043845](https://bugs.launchpad.net/bugs/1043845) st\_distance() results are incorrect depending on variable order.
    * Autointersections of an object were treated as nodes, so the wrong result.
    * per-file comments:
      * mysql-test/r/gis.result
        * [Bug #1043845](https://bugs.launchpad.net/bugs/1043845) st\_distance() results are incorrect depending on variable order.
        * test result updated.
      * mysql-test/t/gis.test
        * [Bug #1043845](https://bugs.launchpad.net/bugs/1043845) st\_distance() results are incorrect depending on variable order.
        * test case added.
      * sql/item.cc
        * small fix to make compilers happy.
      * sql/item\_geofunc.cc
        * [Bug #1043845](https://bugs.launchpad.net/bugs/1043845) st\_distance() results are incorrect depending on variable order.
        * Skip intersection points when calculate distance.
* [Revision #3525](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3525)\
  Wed 2012-09-05 13:15:05 +0200
  * sys\_vars.expensive\_subquery\_limit\_basic
* [Revision #3524](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3524) \[merge]\
  Wed 2012-09-05 13:14:37 +0200
  * XtraDB from Percona-Server-5.5.27-rel28.1
  * [Revision #0.12.55](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.55)\
    Wed 2012-09-05 10:44:23 +0200
    * Percona-Server-5.5.27-rel28.1
* [Revision #3523](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3523)\
  Tue 2012-09-04 19:11:06 +0200
  * [MDEV-481](https://jira.mariadb.org/browse/MDEV-481) Assertion \`pins->pin\[i] == 0' failed in \_lf\_pinbox\_put\_pins on concurrent OPTIMIZE TABLE and DML with Aria tables
  * A bug in the lock-free hash implementation!
  * when lsearch() has not found the key, the caller needs to unpin all the three pins,\
    because lsearch() was using all the three.
* [Revision #3522](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3522)\
  Tue 2012-09-04 12:12:28 +0200
  1. fix an old typo. A purgatory must be cleaned on every LF\_PURGATORY\_SIZE freeing,\
     not every time.
  2. Increase purgatory size.
* [Revision #3521](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3521)\
  Sun 2012-09-02 19:09:17 +0200
  * don't run mdev375.test for embedded server
* [Revision #3520](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3520)\
  Sat 2012-09-01 00:23:30 +0200
  * remove the forgotten commented out piece of the old merge
* [Revision #3519](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3519)\
  Fri 2012-08-31 16:48:02 +0200
  * fix the test to work with `--lower-case-table-names=1`
* [Revision #3518](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3518) \[merge]\
  Fri 2012-08-31 14:15:52 +0200
  * 5.3 merge
  * [Revision #2502.567.16](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.16)\
    Fri 2012-08-31 12:01:52 +0200
    * compilation warning
  * [Revision #2502.567.15](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.15)\
    Thu 2012-08-30 10:53:49 +0200
    * [MDEV-381](https://jira.mariadb.org/browse/MDEV-381): fdatasync() does not correctly flush growing binlog file.
    * When we append data to the binlog file, we use fdatasync() to ensure\
      the data gets to disk so that crash recovery can work.
    * Unfortunately there seems to be a bug in ext3/ext4 on linux, so that\
      fdatasync() does not correctly sync all data when the size of a file\
      is increased. This causes crash recovery to not work correctly (it\
      loses transactions from the binlog).
    * As a work-around, use fsync() for the binlog, not fdatasync(). Since\
      we are increasing the file size, (correct) fdatasync() will most\
      likely not be faster than fsync() on any file system, and fsync()\
      does work correctly on ext3/ext4. This avoids the need to try to\
      detect if we are running on buggy ext3/ext4.
  * [Revision #2502.567.14](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.14)\
    Thu 2012-08-30 09:05:27 +0200
    * [MDEV-437](https://jira.mariadb.org/browse/MDEV-437) Microseconds: In time functions precision is calculated modulo 256
    * store the precision in uint, not uint8
  * [Revision #2502.567.13](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.13)\
    Wed 2012-08-29 18:36:57 +0200
    * [MDEV-438](https://jira.mariadb.org/browse/MDEV-438) Microseconds: Precision is ignored in CURRENT\_TIMESTAMP(N) when it is given as a default column value
    * The syntax for specifying precision in the DEFAULT clause is unintentional and unsupported.
    * Don't allow it anymore.
  * [Revision #2502.567.12](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.12)\
    Wed 2012-08-29 17:55:59 +0200
    * [MDEV-454](https://jira.mariadb.org/browse/MDEV-454) Addition of a time interval reduces the resulting value
      1. Field\_newdate::get\_date should refuse to return a date with zeros when\
         TIME\_NO\_ZERO\_IN\_DATE is set, not when TIME\_FUZZY\_DATE is unset
      2. Item\_func\_to\_days and Item\_date\_add\_interval can only work with valid dates,\
         no zeros allowed.
  * [Revision #2502.567.11](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.11)\
    Wed 2012-08-29 10:59:51 +0200
    * [MDEV-456](https://jira.mariadb.org/browse/MDEV-456) An out-of-range datetime value (with a 5-digit year) can be created and cause troubles
    * fix Item\_func\_add\_time::get\_date() to generate valid dates.
    * Move the validity check inside get\_date\_from\_daynr()\
      instead of relying on callers
    * (5 that had it, and 2 that did not, but should've)
  * [Revision #2502.567.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.10)\
    Wed 2012-08-29 11:35:42 +0300
    * [MDEV-492](https://jira.mariadb.org/browse/MDEV-492): fixed incorrect error check.
  * [Revision #2502.567.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.9)\
    Tue 2012-08-28 13:51:01 +0400
    * Fix bugs in BatchedKeyAccess that show up when working with a\
      storage engine in HA\_MRR\_NO\_ASSOCIATION mode.
    * (there is no testcase because we don't ship any such engines currently)
* [Revision #3517](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3517)\
  Fri 2012-08-31 13:03:41 +0200
  * [MDEV-414](https://jira.mariadb.org/browse/MDEV-414) Depending on indexes or execution plans, a warning on incorrect or out of range values in WHERE condition is sometimes produced and sometimes not
  * use the same method that disables warnings in all relevant places, remove redundant function
* [Revision #3516](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3516)\
  Thu 2012-08-30 11:47:01 +0200
  * [MDEV-395](https://jira.mariadb.org/browse/MDEV-395) PR\_SET\_DUMPABLE set in unreachable code
* [Revision #3515](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3515)\
  Wed 2012-08-29 15:19:17 +0200
  * [MDEV-448](https://jira.mariadb.org/browse/MDEV-448) Memory loss warnings in mysqldump when more than one schema is dumped
* [Revision #3514](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3514)\
  Tue 2012-08-28 19:39:49 +0300
  * Split ER\_NO\_SUCH\_TABLE into ER\_NO\_SUCH\_TABLE and ER\_NO\_SUCH\_TABLE\_IN\_ENGINE to be able to distingus if a .frm file is missing or if the table is missing in the engine.
* [Revision #3513](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3513)\
  Tue 2012-08-28 16:03:22 +0400
  * Update test results (checked)
* [Revision #3512](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3512)\
  Tue 2012-08-28 15:40:38 +0400
  * [MDEV-405](https://jira.mariadb.org/browse/MDEV-405): Server crashes in test\_if\_skip\_sort\_order on EXPLAIN with GROUP BY and HAVING in EXISTS subquery
  * Testcase
* [Revision #3511](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3511) \[merge]\
  Tue 2012-08-28 15:20:37 +0400
  * Merge
  * [Revision #3501.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3501.1.1)\
    Tue 2012-08-28 15:15:05 +0400
    * [MDEV-430](https://jira.mariadb.org/browse/MDEV-430): Server crashes in select\_describe on EXPLAIN with materialization+semijoin, etc
    * Don't do early cleanup of uncorrelated subqueries if we're running an EXPLAIN.
* [Revision #3510](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3510)\
  Tue 2012-08-28 15:07:50 +0500
  * [MDEV-471](https://jira.mariadb.org/browse/MDEV-471) update help tables.
    * the fill\_help\_table-5.5.sql file was copied into mariadb.
    * per-file comments:
      * scripts/fill\_help\_tables.sql
* [Revision #3509](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3509) \[merge]\
  Mon 2012-08-27 18:13:17 +0200
  * 5.3 merge
  * [Revision #2502.567.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.8)\
    Fri 2012-08-24 23:43:18 +0200
    * [MDEV-336](https://jira.mariadb.org/browse/MDEV-336) oqgraph 5.5 crashes in buildbot
    * force -fno-strict-aliasing for oqgraph
  * [Revision #2502.567.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.7)\
    Sat 2012-08-25 09:15:57 +0300
    * fix for [MDEV-367](https://jira.mariadb.org/browse/MDEV-367)
    * The problem was that was\_null and null\_value variables was reset in each reexecution of IN subquery, but engine rerun only for non-constant subqueries.
    * Fixed checking constant in Item\_equal sort.
    * Fix constant reporting in Item\_subselect.
  * [Revision #2502.567.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.6) \[merge]\
    Fri 2012-08-24 19:13:34 +0200
    * Merge from 5.2
    * [Revision #2502.566.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.5) \[merge]\
      Fri 2012-08-24 19:12:47 +0200
      * Merge from 5.1
      * [Revision #2502.565.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.5)\
        Fri 2012-08-24 19:11:54 +0200
        * Fix compiler warning
  * [Revision #2502.567.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.5) \[merge]\
    Fri 2012-08-24 15:39:34 +0200
    * Merge from 5.2.
    * [Revision #2502.566.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.4) \[merge]\
      Fri 2012-08-24 15:37:39 +0200
      * Merge from 5.1.
      * [Revision #2502.565.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.4)\
        Fri 2012-08-24 15:32:44 +0200
        * Fix compiler warnings
      * [Revision #2502.565.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.3) \[merge]\
        Fri 2012-08-24 10:34:55 +0200
        * Merge with latest 5.1.
    * [Revision #2502.566.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.3)\
      Fri 2012-08-24 15:30:05 +0200
      * [MDEV-484](https://jira.mariadb.org/browse/MDEV-484) : allow compilation/packaging on Windows with newly released VS2012
    * [Revision #2502.566.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.2) \[merge]\
      Fri 2012-08-24 12:57:19 +0200
      * Merge into latest 5.2.
  * [Revision #2502.567.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.4) \[merge]\
    Fri 2012-08-24 14:26:23 +0200
    * Merge into latest 5.3
  * [Revision #2502.567.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.3)\
    Thu 2012-08-23 13:52:36 +0200
    * remove mysql-5.1 assert that is already absent in mysql-5.5
  * [Revision #2502.567.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.2)\
    Wed 2012-08-22 18:40:27 +0200
    * [MDEV-472](https://jira.mariadb.org/browse/MDEV-472) `mysql-test-run --valgrind main.ps_2myisam` gives warning about not initialized memory
    * Item::get\_date() should return 1 unless the value is a valid date.
  * [Revision #2502.567.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.1) \[merge]\
    Wed 2012-08-22 16:45:25 +0200
    * 5.2 merge.
    * two tests still fail:
      * main.innodb\_icp and main.range\_vs\_index\_merge\_innodb
      * call records\_in\_range() with both range ends being open\
        (which triggers an assert)
    * [Revision #2502.566.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.1) \[merge]\
      Wed 2012-08-22 16:13:54 +0200
      * 5.1 merge
      * increase xtradb verson from 13.0 to 13.01
      * [Revision #2502.565.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.2)\
        Wed 2012-08-22 16:10:31 +0200
        * merge with XtraDB as of Percona-Server-5.1.63-rel13.4
      * [Revision #2502.565.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.1) \[merge]\
        Wed 2012-08-22 11:40:39 +0200
        * merge with MySQL 5.1.65
* [Revision #3508](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3508) \[merge]\
  Fri 2012-08-24 15:29:01 +0200
  * Merge from 5.3
  * [Revision #2502.561.19](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.19) \[merge]\
    Fri 2012-08-24 14:02:32 +0200
    * merge from 5.2
    * [Revision #2502.562.11](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.562.11) \[merge]\
      Fri 2012-08-24 12:32:46 +0200
      * Merge from 5.1.
      * [Revision #2502.554.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.554.10)\
        Fri 2012-08-24 10:06:16 +0200
        * [MDEV-382](https://jira.mariadb.org/browse/MDEV-382): Incorrect quoting ([CVE-2012-4414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-4414))
        * Various places in the server replication code was incorrectly quoting\
          strings, which could lead to incorrect SQL on the slave/mysqlbinlog.
* [Revision #3507](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3507) \[merge]\
  Fri 2012-08-24 13:57:39 +0200
  * Merge from 5.3
  * [Revision #2502.561.18](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.18) \[merge]\
    Fri 2012-08-24 13:51:16 +0200
    * Merge from 5.2
    * [Revision #2502.562.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.562.10)\
      Thu 2012-06-21 18:47:13 +0300
      * Fix for [Bug #1001505](https://bugs.launchpad.net/bugs/1001505) and [Bug #1001510](https://bugs.launchpad.net/bugs/1001510)
      * We set correct cmp\_context during preparation to avoid changing it later by Item\_field::equal\_fields\_propagator.\
        (see mysql bugs #57135 #57692 during merging)
  * [Revision #2502.561.17](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.17)\
    Tue 2012-08-21 22:24:34 +0400
    * Better comments
  * [Revision #2502.561.16](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.16)\
    Tue 2012-08-14 14:25:56 -0700
    * Corrected the pactch for [MDEV-449](https://jira.mariadb.org/browse/MDEV-449) to fix valgrind failures.
  * [Revision #2502.561.15](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.15)\
    Mon 2012-08-13 21:13:14 -0700
    * Fixed bug [MDEV-449](https://jira.mariadb.org/browse/MDEV-449).
    * The bug could caused a crash when the server executed a query with\
      ORDER by and sort\_buffer\_size was set to a small enough number.
    * It happened because the small sort buffer did not allow to allocate\
      all merge buffers in it.
    * Made sure that the allocated sort buffer would be big enough\
      to contain all possible merge buffers.
* [Revision #3506](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3506)\
  Thu 2012-08-23 15:36:38 +0200
  * [MDEV-439](https://jira.mariadb.org/browse/MDEV-439) cmake -DWITHOUT\_SERVER does not work
  * fix mysys/waiting\_threads.c to compile w/o performance schema\
    include clients. scripts and manpages in -DWITHOUT\_SERVER
* [Revision #3505](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3505)\
  Thu 2012-08-23 15:32:03 +0200
  * [MDEV-469](https://jira.mariadb.org/browse/MDEV-469) Debian/Ubuntu build dependencies for source package mariadb-5.5 does not includes "cmake"
  * only add cmake as a build dependency for distributions, where cmake is recent enough
* [Revision #3504](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3504)\
  Thu 2012-08-23 15:30:43 +0200
  * remove duplicate code from the factorial dbug example
* [Revision #3503](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3503)\
  Wed 2012-08-22 23:33:45 +0200
  * [MDEV-469](https://jira.mariadb.org/browse/MDEV-469) Debian/Ubuntu build dependencies for source package mariadb-5.5 does not includes "cmake"
* [Revision #3502](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3502)\
  Wed 2012-08-22 18:03:31 +0300
  * More DBUG\_ENTER, to make it easier to find out where free\_root(thd->mem\_root) is called
* [Revision #3501](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3501) \[merge]\
  Wed 2012-08-22 09:56:20 +0200
  * merge XtraDB 1.1.8-27.0 from Percona-Server-5.5.25a-rel27.1
  * [Revision #0.12.54](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.54)\
    Wed 2012-08-22 08:42:24 +0200
    * XtraDB 1.1.8-27.0 from Percona-Server-5.5.25a-rel27.1
* [Revision #3500](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3500)\
  Tue 2012-08-21 15:24:43 +0300
  * Fix bug [MDEV-447](https://jira.mariadb.org/browse/MDEV-447): Wrong output from the EXPLAIN command of the test case for [Bug #714999](https://bugs.launchpad.net/bugs/714999)
  * The fix backports from [MWL#182](https://askmonty.org/worklog/?tid=182): Explain running statements the logic that\
    saves the original JOIN\_TAB array of a query plan after optimization. This\
    array is later used during EXPLAIN to iterate over the original JOIN plan\
    nodes in the cases when this plan could be changed by early subquery\
    execution during the optimization phase of the outer query.
* [Revision #3499](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3499)\
  Tue 2012-08-21 08:46:32 +0300
  * Fix for [Bug #1039277](https://bugs.launchpad.net/bugs/1039277) "Crash in sql\_cache.cc".
  * The crash happend when combining query cache, prepared statements and using a read only cursor.
* [Revision #3498](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3498)\
  Mon 2012-08-20 22:54:15 +0300
  * Ensure we don't assert with debug binaries if SHOW INNODB STATUS returns with an error.
* [Revision #3497](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3497)\
  Fri 2012-08-17 14:35:28 +0200
  * Fix incorrect regexp in warning suppression pattern
* [Revision #3496](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3496)\
  Fri 2012-08-17 10:01:19 +0300
  * Fixed compiler warnings
  * Fixed error in test that caused following tests to fail
* [Revision #3495](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3495)\
  Wed 2012-08-15 14:37:55 +0300
  * Fixed [MDEV-366](https://jira.mariadb.org/browse/MDEV-366): Assertion \`share->reopen == 1' failed in maria\_extra on DROP TABLE which is locked twice
* [Revision #3494](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3494)\
  Wed 2012-08-15 13:33:37 +0300
  * Fixed [MDEV-365](https://jira.mariadb.org/browse/MDEV-365) "Got assertion when doing alter table on a partition"
* [Revision #3493](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3493) \[merge]\
  Wed 2012-08-15 12:07:21 +0300
  * automatic merge
  * [Revision #3489.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3489.1.3)\
    Wed 2012-08-15 09:34:18 +0300
    * Fixed compiler warnings
    * [Revision #3489.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3489.1.2)\
      Tue 2012-08-14 19:59:28 +0300
      * Fixed compiler errors
      * Updated test to also work on 32 bit
    * [Revision #3489.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3489.1.1) \[merge]\
      Mon 2012-08-13 23:45:16 +0300
      * Automatic merge
      * [Revision #3484.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3484.1.3)\
        Mon 2012-08-13 22:23:28 +0300
        * Fixed compiler warnings (A few of these was bugs)
      * [Revision #3484.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3484.1.2)\
        Wed 2012-08-08 18:04:57 +0300
        * Better test case for [MDEV-436](https://jira.mariadb.org/browse/MDEV-436)
      * [Revision #3484.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3484.1.1)\
        Tue 2012-08-07 01:58:05 +0300
        * Use less memory when growing HEAP tables. See [MDEV-436](https://jira.mariadb.org/browse/MDEV-436)
* [Revision #3492](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3492)\
  Tue 2012-08-14 12:40:40 +0200
  * [MDEV-450](https://jira.mariadb.org/browse/MDEV-450): Deadlock between starting a slave and reading system variables
  * Starting the SQL thread might deadlock with reading the values of the\
    replication filtering options.
  * The deadlock is due to a lock order violation when the variables are\
    read or set. For example, reading replicate\_ignore\_table first\
    acquires LOCK\_global\_system\_variables in sys\_var::value\_ptr and later\
    acquires LOCK\_active\_mi in Sys\_var\_rpl\_filter::global\_value\_ptr. This\
    violates the order established when starting a SQL thread, where\
    LOCK\_active\_mi is acquired before start\_slave, and ends up creating a\
    thread (handle\_slave\_sql) that allocates a THD handle whose\
    constructor acquires LOCK\_global\_system\_variables in THD::init.
  * The solution is to unlock LOCK\_global\_system\_variables before the\
    replication filtering options are set or read. This way the lock\
    order is preserved and the data being read/set is still protected\
    given that it acquires LOCK\_active\_mi.
* [Revision #3491](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3491)\
  Mon 2012-08-13 11:14:43 +0200
  * [MDEV-364](https://jira.mariadb.org/browse/MDEV-364) Server crashes in add\_identifier on concurrent ALTER TABLE and SHOW ENGINE INNODB STATUS
  * fix add\_identifier() to distinguish between temporary tables (#sql- prefix) and temporary partitions (#TMP

## suffix).

* change add\_identifier() to use the same name variant constants as sql\_partition.cc does.
* [Revision #3490](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3490)\
  Mon 2012-08-13 09:21:47 +0200
  * [MDEV-286](https://jira.mariadb.org/browse/MDEV-286) mytop is not installed in 5.5
  * include mytop in bintars, rpms, and debs.
  * install mysqlbug.1 too.
* [Revision #3489](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3489)\
  Sat 2012-08-11 10:31:10 +0200
  * [MDEV-336](https://jira.mariadb.org/browse/MDEV-336) oqgraph 5.5 crashes in buildbot
  * compile oqgraph with -fno-strict-aliasing
* [Revision #3488](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3488)\
  Fri 2012-08-10 13:48:31 +0200
  * compiler warnings
* [Revision #3487](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3487)\
  Thu 2012-08-09 18:25:47 +0200
  * fix val\_str\_ascii to return a string in the ascii-compatible charset.
  * two items didn't do that properly, one was exploitable, the other was not, but fixed anyway.
* [Revision #3486](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3486) \[merge]\
  Thu 2012-08-09 17:22:00 +0200
  * merge with MySQL 5.5.27
  * manually checked every change, reverted incorrect or stupid changes.
  * [Revision #3077.149.180](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.149.180)\
    Wed 2012-08-08 12:32:34 +0200
    * undo the fix for MySQL Bug#12998841
* [Revision #3485](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3485)\
  Wed 2012-08-08 12:08:54 +0200
  * [MDEV-392](https://jira.mariadb.org/browse/MDEV-392) MTR: skip-combinations option is declared in help, but is ignored
  * remove unused mtr option
* [Revision #3484](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3484)\
  Mon 2012-08-06 16:33:11 +0300
  * Fixed compiler warnings
* [Revision #3483](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3483)\
  Wed 2012-08-01 19:57:36 +0200
  * [MDEV-399](https://jira.mariadb.org/browse/MDEV-399) Combinations defined in the base suite cannot be skipped by overlay
  * When appliying parent combinations to the overlay,\
    filter them through the %skip\_combinations using the overlayed filename
* [Revision #3482](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3482)\
  Thu 2012-08-02 23:17:27 +0200
  * fix oqgraph on MSVC
* [Revision #3481](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3481)\
  Thu 2012-08-02 04:48:33 +0400
  * [MDEV-369](https://jira.mariadb.org/browse/MDEV-369): Mismatches in MySQL engines test suite
  * Post-merge fixes for mismatches that only affect 5.5 (but not 5.3)
* [Revision #3480](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3480) \[merge]\
  Thu 2012-08-02 04:22:43 +0400
  * Merge 5.3->5.5
  * [Revision #2502.561.14](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.14) \[merge]\
    Thu 2012-08-02 00:58:13 +0400
    * [MDEV-369](https://jira.mariadb.org/browse/MDEV-369) (Mismatches in MySQL engines test suite)
    * Following reasons caused mismatches:
      * different handling of invalid values;
      * different CAST results with fractional seconds;
      * microseconds support in MariaDB;
      * different algorithm of comparing temporal values;
      * differences in error and warning texts and codes;
      * different approach to truncating datetime values to time;
      * additional collations;
      * different record order for queries without ORDER BY;
      * [MySQL Bug #66034](https://bugs.mysql.com/bug.php?id=66034).
    * More details in [MDEV-369](https://jira.mariadb.org/browse/MDEV-369) comments.
    * [Revision #2502.564.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.564.2)\
      Mon 2012-07-30 04:16:49 +0400
      * [MDEV-369](https://jira.mariadb.org/browse/MDEV-369) (Mismatches in MySQL engines test suite)
    * [Revision #2502.564.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.564.1)\
      Thu 2012-07-26 23:31:08 +0400
      * Result files were wrong due to [MySQL Bug #66034](https://bugs.mysql.com/bug.php?id=66034)
* [Revision #3479](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3479)\
  Tue 2012-07-31 22:39:33 +0200
  * [MDEV-336](https://jira.mariadb.org/browse/MDEV-336) oqgraph 5.5 crashes in buildbot
  * make CMakeLists.txt to detect if the installed boost can be compiled with the\
    installed compile and specified set of compiler options.
  * Background: even sufficiently new Boost cannot be compiled with the sufficiently old gcc\
    in the presence of -fno-rtti
* [Revision #3478](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3478)\
  Tue 2012-07-31 19:29:07 +0200
  * [MDEV-419](https://jira.mariadb.org/browse/MDEV-419) ensure that all HAVE\_XXX constants can be set by cmake
  * add missing checks to configure.cmake
  * remove dead code and unused HAVE\_xxx constants from the sources
* [Revision #3477](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3477)\
  Tue 2012-07-31 18:32:46 +0200
  * [MDEV-375](https://jira.mariadb.org/browse/MDEV-375) Server crashes in THD::print\_aborted\_warning with log\_warnings > 3
  * Don't use ER(xxx) in THD::close\_connection(), when current\_thd is already reset to NULL.
  * Prefer ER\_THD() or ER\_DEFAULT() instead.
* [Revision #3476](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3476)\
  Tue 2012-07-31 16:21:53 +0500
  * [MDEV-340](https://jira.mariadb.org/browse/MDEV-340) Save replication comments for DROP TABLE.
  * mysql\_rm\_table\_no\_locks() function was modified.
  * When we construct log record for the DROP TABLE, now we\
    look if there's a comment before the first table name and\
    add it to the record if so.
  * per-file comments:
    * sql/sql\_table.cc
      * [MDEV-340](https://jira.mariadb.org/browse/MDEV-340) Save replication comments for DROP TABLE.
        * comment\_length() function implemented to find comments in the query,
        * call it in mysql\_rm\_table\_no\_locks() and use the result to form log record.
    * mysql-test/suite/binlog/r/binlog\_drop\_if\_exists.result
      * [MDEV-340](https://jira.mariadb.org/browse/MDEV-340) Save replication comments for DROP TABLE.
        * test result updated.
    * mysql-test/suite/binlog/t/binlog\_drop\_if\_exists.test
      * [MDEV-340](https://jira.mariadb.org/browse/MDEV-340) Save replication comments for DROP TABLE.
        * test case added.
* [Revision #3475](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3475)\
  Tue 2012-07-31 11:31:26 +0200
  * [MDEV-418](https://jira.mariadb.org/browse/MDEV-418) Feedback plugin statisics problem
  * Add the check for sys/utsname.h to configure.cmake
* [Revision #3474](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3474)\
  Mon 2012-07-30 20:13:23 +0200
  * [MDEV-417](https://jira.mariadb.org/browse/MDEV-417) - fix typo that prevented use of atomic instructions on Windows
  * use correct macro for Microsoft compiler. It is \_MSC\_VER , not \_MSV\_VER
* [Revision #3473](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3473)\
  Wed 2012-07-25 20:41:48 +0400
  * [MDEV-410](https://jira.mariadb.org/browse/MDEV-410): EXPLAIN shows type=range, while SHOW EXPLAIN and userstat show full table scan is used
  * Make Item\_subselect::fix\_fields() ignore UNCACHEABLE\_EXPLAIN flag when deciding whether\
    the subquery item should be marked as constant.
* [Revision #3472](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3472)\
  Tue 2012-07-24 17:50:06 +0300
  * Awoiding registering partiton engine underlying tables whan it has no sens.
* [Revision #3471](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3471)\
  Mon 2012-07-23 23:54:57 +0200
  * [MDEV-409](https://jira.mariadb.org/browse/MDEV-409) : /etc/my.cnf config file overwritten during RPM installation
  * Fix : use attribute %config(noreplace) for /etc/my.cnf , instead of (automatically generated) %config
* [Revision #3470](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3470) \[merge]\
  Thu 2012-07-19 13:24:24 +0200
  * merged in [MDEV-11](https://jira.mariadb.org/browse/MDEV-11) "Generic storage engine test suite"
  * see [MDEV-11](https://jira.mariadb.org/browse/MDEV-11)
  * [Revision #3466.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3466.1.4) \[merge]\
    Thu 2012-07-19 13:21:53 +0200
    * merged with maria/5.5
  * [Revision #3466.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3466.1.3)\
    Mon 2012-07-16 06:17:56 +0400
  * [MDEV-11](https://jira.mariadb.org/browse/MDEV-11): Generic storage engine test suite
  * [Revision #3466.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3466.1.2)\
    Mon 2012-07-16 06:14:53 +0400
    * Allow multiple error codes inside a variable in `--error` command
  * [Revision #3466.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3466.1.1)\
    Mon 2012-07-16 06:12:11 +0400
    * Export sys\_errno and errno to variables
* [Revision #3469](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3469) \[merge]\
  Wed 2012-07-18 22:40:15 +0400
  * Merge 5.3->5.5
  * [Revision #2502.561.13](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.13)\
    Wed 2012-07-18 15:03:05 +0400
    * [MDEV-398](https://jira.mariadb.org/browse/MDEV-398): Sergv related to spacial queries
    * index\_merge/intersection is unable to work on GIS indexes, because:
      1. index scans have no Rowid-Ordered-Retrieval property
      2. When one does an index-only read over a GIS index, they do not\
         get the index tuple, because index only contains bounding box of the geometry.\
         This is why key\_copy() call crashed.
    * This patch fixes #1, which makes the problem go away. Theoretically, it would\
      be nice to check #2, too, but SE API semantics is not sufficiently precise to do it.
* [Revision #3468](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3468) \[merge]\
  Wed 2012-07-18 22:36:20 +0400
  * Merge [Bug #1007622](https://bugs.launchpad.net/bugs/1007622) from 5.3 to 5.5
  * [Revision #2502.561.12](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.12)\
    Tue 2012-06-26 21:43:34 +0300
    * Fix for [Bug #1007622](https://bugs.launchpad.net/bugs/1007622)
    * TABLE\_LIST::check\_single\_table made aware about fact that now if table attached to a merged view it can be (unopened) temporary table\
      (in 5.2 it was always leaf table or non (in case of several tables)).
* [Revision #3467](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3467)\
  Mon 2012-07-16 10:48:03 +0300
  * fix to satisfy compiler.
* [Revision #3466](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3466)\
  Fri 2012-07-13 22:17:32 +0300
  * fixed [MySQL Bug #53775](https://bugs.mysql.com/bug.php?id=53775):
  * Now partition engine adds underlying tables to the QC and ask underlying tables engine permittion to cache the query and return result of the query.
  * Incorrect QC cleanup in case of table registration failure fixe.
  * Unified interface for myisammrg & partitioned engnes for QC.
* [Revision #3465](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3465)\
  Thu 2012-07-12 15:32:35 +0200
  * [MDEV-393](https://jira.mariadb.org/browse/MDEV-393). Remove `--loose-pbxt=OFF/loose-skip-pbxt` from bootstrapper calls to avoid "unknown parameter" warning
* [Revision #3464](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3464)\
  Wed 2012-07-11 16:19:05 +0200
  * [Bug #1023404](https://bugs.launchpad.net/bugs/1023404) problems with savepoints and tokudb with 5.5
  * fix incorrect merge
* [Revision #3463](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3463)\
  Tue 2012-07-10 09:02:12 +0300
  * Fixed [MDEV-385](https://jira.mariadb.org/browse/MDEV-385): mysqltest running with continue-on-error crashes on a non-SQL command producing an error
* [Revision #3462](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3462) \[merge]\
  Thu 2012-07-05 14:39:01 +0400
  * Merge fix for [MDEV-376](https://jira.mariadb.org/browse/MDEV-376)
  * [Revision #3457.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3457.1.1)\
    Wed 2012-07-04 14:34:45 +0400
    * [MDEV-376](https://jira.mariadb.org/browse/MDEV-376): Wrong result (missing rows) with index\_merge+index\_merge\_intersection, join
    * Let QUICK\_RANGE\_SELECT::init\_ror\_merged\_scan() call quick->reset() only\
      after we've set the column read bitmaps.
* [Revision #3461](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3461)\
  Thu 2012-07-05 09:29:34 +0200
  * The variable "table\_cache" is deprecated, use the new name "table\_open\_cache" instead.
  * Thanks to Ivoz for pointing this out.
* [Revision #3460](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3460)\
  Wed 2012-06-27 17:13:12 +0300
  * Don't abort InnoDB/XtraDB if one can't allocate resources for AIO
  * Better error messages
  * This fixes that one again can run the test systems with many threads without having to increase fs.aio-max-nr.
* [Revision #3459](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3459)\
  Mon 2012-06-25 18:17:24 +0200
  * fix compile error, when building with oqgraph
* [Revision #3458](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3458) \[merge]\
  Sun 2012-06-24 09:10:11 -0700
  * Merge 5.3->5.5.
  * [Revision #2502.561.11](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.11) \[merge]\
    Sat 2012-06-23 15:00:05 -0700
    * Merge 5.2->5.3
    * [Revision #2502.562.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.562.9)\
      Sat 2012-06-23 12:19:07 -0700
      * Fixed bug [MDEV-360](https://jira.mariadb.org/browse/MDEV-360).
      * The bug was the result of the incomplete fix for bug lp bug 1008293.
    * [Revision #2502.562.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.562.8)\
      Mon 2012-06-18 22:32:17 -0700
      * Fixed bug [MDEV-354](https://jira.mariadb.org/browse/MDEV-354).
      * Virtual columns of ENUM and SET data types were not supported properly\
        in the original patch that introduced virtual columns into [MariaDB 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md).
      * The problem was that for any virtual column the patch used the\
        interval\_id field of the definition of the column in the frm file as\
        a reference to the virtual column expression.
      * The fix stores the optional interval\_id of the virtual column in the\
        extended header of the virtual column expression.
  * [Revision #2502.561.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.10)\
    Fri 2012-06-22 14:14:22 +0400
    * Added comment about QUICK\_RANGE\_SELECT::free\_cond being unused.
  * [Revision #2502.561.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.9)\
    Thu 2012-06-21 14:33:36 +0400
    * Update test results (checked)
  * [Revision #2502.561.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.561.8)\
    Wed 2012-06-20 22:30:24 +0400
    * Update test results.
* [Revision #3457](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3457)\
  Sat 2012-06-23 20:12:54 +0400
  * Add back testcase for [Bug #817966](https://bugs.launchpad.net/bugs/817966) (was lost in the merge)
* [Revision #3456](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3456)\
  Fri 2012-06-22 10:42:55 +0200
  * [MDEV-342](https://jira.mariadb.org/browse/MDEV-342): fix two race conditions in the test case that could occasionally cause spurious failures.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
