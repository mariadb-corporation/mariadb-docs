# MariaDB Galera 5.5.25 Changelog

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.25) |[Release Notes](../mariadb-galera-55-release-notes/mariadb-galera-5525-release-notes.md) |**Changelog** |[Overview of Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 4 Sep 2012

For the highlights of this release, see the [release notes](../mariadb-galera-55-release-notes/mariadb-galera-5525-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3344](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3344)\
  Thu 2012-08-30 12:22:37 +0300
  * Merged in change sets 3772-3779 from lp:codership-mysql/5.5
* [Revision #3343](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3343) \[merge]\
  Thu 2012-08-09 01:47:21 +0300
  * References [Bug #1034621](https://bugs.launchpad.net/bugs/1034621) - Merge up to mysql-5.5.25 level
  * merged codership-mysql/5.5 revisions: bzr diff -r3759..3767
  * merged codership-mysql/5.5 revisions: bzr diff -r3768..3771
  * [Revision #3334.1.150](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.150)\
    Mon 2012-08-06 16:33:11 +0300
    * Fixed compiler warnings
  * [Revision #3334.1.149](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.149)\
    Wed 2012-08-01 19:57:36 +0200
    * [MDEV-399](https://jira.mariadb.org/browse/MDEV-399) Combinations defined in the base suite cannot be skipped by overlay
    * When appliying parent combinations to the overlay,\
      filter them through the %skip\_combinations using the overlayed filename
  * [Revision #3334.1.148](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.148)\
    Thu 2012-08-02 23:17:27 +0200
    * fix oqgraph on MSVC
  * [Revision #3334.1.147](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.147)\
    Thu 2012-08-02 04:48:33 +0400
    * [MDEV-369](https://jira.mariadb.org/browse/MDEV-369): Mismatches in MySQL engines test suite
    * Post-merge fixes for mismatches that only affect 5.5 (but not 5.3)
  * [Revision #3334.1.146](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.146) \[merge]\
    Thu 2012-08-02 04:22:43 +0400
    * Merge 5.3->5.5
    * [Revision #2502.561.14](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.561.14) \[merge]\
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
      * [Revision #2502.564.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.564.2)\
        Mon 2012-07-30 04:16:49 +0400
        * [MDEV-369](https://jira.mariadb.org/browse/MDEV-369) (Mismatches in MySQL engines test suite)
      * [Revision #2502.564.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.564.1)\
        Thu 2012-07-26 23:31:08 +0400
        * Result files were wrong due to MySQL bug#66034
  * [Revision #3334.1.145](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.145)\
    Tue 2012-07-31 22:39:33 +0200
    * [MDEV-336](https://jira.mariadb.org/browse/MDEV-336) oqgraph 5.5 crashes in buildbot
    * make CMakeLists.txt to detect if the installed boost can be compiled with the\
      installed compile and specified set of compiler options.
    * Background: even sufficiently new Boost cannot be compiled with the sufficiently old gcc\
      in the presence of -fno-rtti
  * [Revision #3334.1.144](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.144)\
    Tue 2012-07-31 19:29:07 +0200
    * [MDEV-419](https://jira.mariadb.org/browse/MDEV-419) ensure that all HAVE\_XXX constants can be set by cmake
    * add missing checks to configure.cmake
    * remove dead code and unused HAVE\_xxx constants from the sources
  * [Revision #3334.1.143](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.143)\
    Tue 2012-07-31 18:32:46 +0200
    * [MDEV-375](https://jira.mariadb.org/browse/MDEV-375) Server crashes in THD::print\_aborted\_warning with log\_warnings > 3
    * Don't use ER(xxx) in THD::close\_connection(), when current\_thd is already reset to NULL.
    * Prefer ER\_THD() or ER\_DEFAULT() instead.
  * [Revision #3334.1.142](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.142)\
    Tue 2012-07-31 16:21:53 +0500
    * [MDEV-340](https://jira.mariadb.org/browse/MDEV-340) Save replication comments for DROP TABLE.
    * mysql\_rm\_table\_no\_locks() function was modified.
    * When we construct log record for the DROP TABLE, now we\
      look if there's a comment before the first table name and\
      add it to the record if so.
    * per-file comments:
      * sql/sql\_table.cc
        * [MDEV-340](https://jira.mariadb.org/browse/MDEV-340) Save replication comments for DROP TABLE.
          * comment\_length() function implemented to find comments in the query,\
            call it in mysql\_rm\_table\_no\_locks() and use the result to form log record.
      * mysql-test/suite/binlog/r/binlog\_drop\_if\_exists.result
        * [MDEV-340](https://jira.mariadb.org/browse/MDEV-340) Save replication comments for DROP TABLE.
          * test result updated.
      * mysql-test/suite/binlog/t/binlog\_drop\_if\_exists.test
        * [MDEV-340](https://jira.mariadb.org/browse/MDEV-340) Save replication comments for DROP TABLE.
          * test case added.
  * [Revision #3334.1.141](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.141)\
    Tue 2012-07-31 11:31:26 +0200
    * [MDEV-418](https://jira.mariadb.org/browse/MDEV-418) Feedback plugin statisics problem
    * Add the check for sys/utsname.h to configure.cmake
  * [Revision #3334.1.140](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.140)\
    Mon 2012-07-30 20:13:23 +0200
    * [MDEV-417](https://jira.mariadb.org/browse/MDEV-417) - fix typo that prevented use of atomic instructions on Windows
    * use correct macro for Microsoft compiler. It is \_MSC\_VER , not \_MSV\_VER
  * [Revision #3334.1.139](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.139)\
    Wed 2012-07-25 20:41:48 +0400
    * [MDEV-410](https://jira.mariadb.org/browse/MDEV-410): EXPLAIN shows type=range, while SHOW EXPLAIN and userstat show full table scan is used
    * Make Item\_subselect::fix\_fields() ignore UNCACHEABLE\_EXPLAIN flag when deciding whether\
      the subquery item should be marked as constant.
  * [Revision #3334.1.138](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.138)\
    Tue 2012-07-24 17:50:06 +0300
    * Awoiding registering partiton engine underlying tables whan it has no sens.
  * [Revision #3334.1.137](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.137)\
    Mon 2012-07-23 23:54:57 +0200
    * [MDEV-409](https://jira.mariadb.org/browse/MDEV-409) : /etc/my.cnf config file overwritten during RPM installation
    * Fix : use attribute %config(noreplace) for /etc/my.cnf , instead of (automatically generated) %config
  * [Revision #3334.1.136](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.136) \[merge]\
    Thu 2012-07-19 13:24:24 +0200
    * merged in [MDEV-11](https://jira.mariadb.org/browse/MDEV-11) "Generic storage engine test suite"
    * [Revision #3334.22.4](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.22.4) \[merge]\
      Thu 2012-07-19 13:21:53 +0200
      * merged with maria/5.5
    * [Revision #3334.22.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.22.3)\
      Mon 2012-07-16 06:17:56 +0400
      * [MDEV-11](https://jira.mariadb.org/browse/MDEV-11): Generic storage engine test suite
    * [Revision #3334.22.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.22.2)\
      Mon 2012-07-16 06:14:53 +0400
      * Allow multiple error codes inside a variable in `--error` command
      * [Revision #3334.22.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.22.1)\
        Mon 2012-07-16 06:12:11 +0400
        * Export sys\_errno and errno to variables
  * [Revision #3334.1.135](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.135) \[merge]\
    Wed 2012-07-18 22:40:15 +0400
    * Merge 5.3->5.5
    * [Revision #2502.561.13](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.561.13)\
      Wed 2012-07-18 15:03:05 +0400
      * [MDEV-398](https://jira.mariadb.org/browse/MDEV-398): Sergv related to spacial queries
      * index\_merge/intersection is unable to work on GIS indexes, because:
        1. index scans have no Rowid-Ordered-Retrieval property
        2. When one does an index-only read over a GIS index, they do not\
           get the index tuple, because index only contains bounding box of the geometry.\
           This is why key\_copy() call crashed.
      * This patch fixes #1, which makes the problem go away. Theoretically, it would\
        be nice to check #2, too, but SE API semantics is not sufficiently precise to do it.
  * [Revision #3334.1.134](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.134) \[merge]\
    Wed 2012-07-18 22:36:20 +0400
    * Merge bug#1007622 from 5.3 to 5.5
    * [Revision #2502.561.12](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.561.12)\
      Tue 2012-06-26 21:43:34 +0300
      * Fix for [Bug #1007622](https://bugs.launchpad.net/bugs/1007622)
      * TABLE\_LIST::check\_single\_table made aware about fact that now if table attached to a merged view it can be (unopened) temporary table\
        (in 5.2 it was always leaf table or non (in case of several tables)).
  * [Revision #3334.1.133](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.133)\
    Mon 2012-07-16 10:48:03 +0300
    * fix to satisfy compiler.
  * [Revision #3334.1.132](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.132)\
    Fri 2012-07-13 22:17:32 +0300
    * fixed [MySQL Bug #53775](https://bugs.mysql.com/bug.php?id=53775):
    * Now partition engine adds underlying tables to the QC and ask underlying tables engine permittion to cache the query and return result of the query.
    * Incorrect QC cleanup in case of table registration failure fixe.
    * Unified interface for myisammrg & partitioned engnes for QC.
  * [Revision #3334.1.131](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.131)\
    Thu 2012-07-12 15:32:35 +0200
    * [MDEV-393](https://jira.mariadb.org/browse/MDEV-393). Remove `--loose-pbxt=OFF/loose-skip-pbxt` from bootstrapper calls to avoid "unknown parameter" warning
  * [Revision #3334.1.130](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.130)\
    Wed 2012-07-11 16:19:05 +0200
    * [Bug #1023404](https://bugs.launchpad.net/bugs/1023404) problems with savepoints and tokudb with 5.5
    * fix incorrect merge
  * [Revision #3334.1.129](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.129)\
    Tue 2012-07-10 09:02:12 +0300
    * Fixed [MDEV-385](https://jira.mariadb.org/browse/MDEV-385): mysqltest running with continue-on-error crashes on a non-SQL command producing an error
  * [Revision #3334.1.128](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.128) \[merge]\
    Thu 2012-07-05 14:39:01 +0400
    * Merge fix for [MDEV-376](https://jira.mariadb.org/browse/MDEV-376)
    * [Revision #3334.21.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.21.1)\
      Wed 2012-07-04 14:34:45 +0400
      * [MDEV-376](https://jira.mariadb.org/browse/MDEV-376): Wrong result (missing rows) with index\_merge+index\_merge\_intersection, join
      * Let QUICK\_RANGE\_SELECT::init\_ror\_merged\_scan() call quick->reset() only\
        after we've set the column read bitmaps.
  * [Revision #3334.1.127](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.127)\
    Thu 2012-07-05 09:29:34 +0200
    * The variable "table\_cache" is deprecated, use the new name "table\_open\_cache" instead.
    * Thanks to Ivoz for pointing this out.
  * [Revision #3334.1.126](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.126)\
    Wed 2012-06-27 17:13:12 +0300
    * Don't abort InnoDB/XtraDB if one can't allocate resources for AIO
    * Better error messages
    * This fixes that one again can run the test systems with many threads without having to increase fs.aio-max-nr.
  * [Revision #3334.1.125](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.125)\
    Mon 2012-06-25 18:17:24 +0200
    * fix compile error, when building with oqgraph
  * [Revision #3334.1.124](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.124) \[merge]\
    Sun 2012-06-24 09:10:11 -0700
    * Merge 5.3->5.5.
    * [Revision #2502.561.11](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.561.11) \[merge]\
      Sat 2012-06-23 15:00:05 -0700
      * Merge 5.2->5.3
      * [Revision #2502.562.9](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.562.9)\
        Sat 2012-06-23 12:19:07 -0700
        * Fixed bug [MDEV-360](https://jira.mariadb.org/browse/MDEV-360).\
          The bug was the result of the incomplete fix for bug lp bug 1008293.
      * [Revision #2502.562.8](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.562.8)\
        Mon 2012-06-18 22:32:17 -0700
        * Fixed bug [MDEV-354](https://jira.mariadb.org/browse/MDEV-354).
        * Virtual columns of ENUM and SET data types were not supported properly\
          in the original patch that introduced virtual columns into [MariaDB 5.2](../../5.2/changes-improvements-in-mariadb-5-2.md).
        * The problem was that for any virtual column the patch used the\
          interval\_id field of the definition of the column in the frm file as\
          a reference to the virtual column expression.
        * The fix stores the optional interval\_id of the virtual column in the\
          extended header of the virtual column expression.
    * [Revision #2502.561.10](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.561.10)\
      Fri 2012-06-22 14:14:22 +0400
      * Added comment about QUICK\_RANGE\_SELECT::free\_cond being unused.
    * [Revision #2502.561.9](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.561.9)\
      Thu 2012-06-21 14:33:36 +0400
      * Update test results (checked)
    * [Revision #2502.561.8](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.561.8)\
      Wed 2012-06-20 22:30:24 +0400
      * Update test results.
  * [Revision #3334.1.123](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.123)\
    Sat 2012-06-23 20:12:54 +0400
    * Add back testcase for [Bug #817966](https://bugs.launchpad.net/bugs/817966) (was lost in the merge)
  * [Revision #3334.1.122](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.122)\
    Fri 2012-06-22 10:42:55 +0200
    * [MDEV-342](https://jira.mariadb.org/browse/MDEV-342): fix two race conditions in the test case that could occasionally cause spurious failures.
  * [Revision #3334.1.121](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.121)\
    Thu 2012-06-21 21:17:34 +0200
    * [MDEV-342](https://jira.mariadb.org/browse/MDEV-342): Do not mark old binlog file as cleanly closed during rotate until\
      the new file is fully synced to disk and binlog index. This fixes a window\
      where a crash would leave next server restart unable to detect that a crash\
      occured, causing recovery to fail.
  * [Revision #3334.1.120](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.120)\
    Thu 2012-06-21 19:02:53 +0200
    * [MDEV-359](https://jira.mariadb.org/browse/MDEV-359): Fix another case where switch-off semisync could cause a race that ended with server crash.
    * This one was when the code releases and reaquires the lock with pthread\_cond\_wait() - and semisync is switched off meanwhile.
  * [Revision #3334.1.119](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.119)\
    Thu 2012-06-21 17:39:21 +0200
    * Use the portable form of INSTALL PLUGIN in rpl\_mdev359.test
  * [Revision #3334.1.118](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.118)\
    Thu 2012-06-21 14:00:19 +0200
    * fixing the order of includes in the rpl\_mdev359.test
  * [Revision #3334.1.117](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.117)\
    Thu 2012-06-21 11:52:54 +0200
    * [MDEV-359](https://jira.mariadb.org/browse/MDEV-359): Server crash when SET GLOBAL rpl\_semi\_sync\_master\_enabled = OFF
    * The semisync code does a fast-but-unsafe check for enabled or not without lock,\
      followed by a slow-but-safe check under lock. However, if the slow check failed,\
      the code still referenced not valid data (in an assert() expression), causing a\
      crash.
    * Fixed by not running the incorrect assert when semisync is disabled.
  * [Revision #3334.1.116](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.116)\
    Thu 2012-06-21 11:26:53 +0200
    * [MDEV-349](https://jira.mariadb.org/browse/MDEV-349) 5.5 xtradb innodb\_prefix\_index\_liftedlimit crash with valgrind
    * This is XtraDB [Bug #1015109](https://bugs.launchpad.net/bugs/1015109), introduced by innodb\_split\_buf\_pool\_mutex.patch
    * Comment the offending assertion, until the fixed XtraDB is available
* [Revision #3342](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3342)\
  Mon 2012-07-23 11:15:59 +0300
  * New version of mysqld\_multi. Building Galera tree fully first time in buildbot
* [Revision #3341](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3341)\
  Wed 2012-06-13 00:23:32 +0300
  * References [Bug #1011983](https://bugs.launchpad.net/bugs/1011983)
  * Merged from codership-mysql/5.5 revision 3758
* [Revision #3340](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3340) \[merge]\
  Tue 2012-06-12 16:34:18 +0300
  * references [Bug #1011983](https://bugs.launchpad.net/bugs/1011983)
  * Merged latest MariaDB development in: bzr merge lp:maria/5.5
    * \=>
    * Text conflict in CMakeLists.txt
    * Text conflict in sql/handler.h
    * Text conflict in support-files/CMakeLists.txt
    * 3 conflicts
* [Revision #3339](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3339)\
  Tue 2012-06-12 10:55:11 +0300
  * References [Bug #1011983](https://bugs.launchpad.net/bugs/1011983)
  * Merged from codership-mysql/5.5 changes revisions 3743-3756
* [Revision #3338](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3338)\
  Thu 2012-04-26 20:18:30 +0300
  * Merged changes from lp:codership-mysql up to rev 3743
    * -r3725..3737
    * -r3738..3740
    * -r3741..3743
* [Revision #3337](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3337) \[merge]\
  Thu 2012-04-26 13:59:35 +0300
  * Merge with [mariaDB 5.5.23](../../5.5/5.5.23.md): bzr merge lp:maria/5.5
* [Revision #3336](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3336)\
  Thu 2012-04-26 13:09:06 +0300
  * Added wsrep specific files
* [Revision #3335](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3335)\
  Fri 2012-04-13 01:33:24 +0300
  * Initial push of codership-wsrep API implementation for MariaDB.
  * Merge of:
    * lp:maria/5.5, #3334: [3334](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3334)
    * lp:codership-mysql/5.5, #3725: [3725](https://bazaar.launchpad.net/~codership/codership-mysql/wsrep-5.5/revision/3725)

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
