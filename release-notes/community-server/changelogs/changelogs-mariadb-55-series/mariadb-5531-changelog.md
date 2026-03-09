# MariaDB 5.5.31 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.31) | [Release Notes](../../old-releases/5.5/5.5.31.md) | **Changelog** | \[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 23 May 2013

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.31.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3778](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3778)\
  Tue 2013-05-21 18:56:35 +0200
  * fix for compiled-in FederatedX
* [Revision #3777](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3777)\
  Tue 2013-05-21 13:03:37 +0200
  * [MDEV-388](https://jira.mariadb.org/browse/MDEV-388) Creating a federated table with a non-existing server returns a random error code (part 2)
* [Revision #3776](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3776) \[merge]\
  Tue 2013-05-21 09:43:34 +0200
  * 5.3 merge
  * [Revision #2502.567.103](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.103)\
    Tue 2013-05-21 09:42:10 +0200
    * fixes for buildbot
* [Revision #3775](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3775)\
  Mon 2013-05-20 23:58:44 +0200
  * [MDEV-388](https://jira.mariadb.org/browse/MDEV-388) Creating a federated table with a non-existing server returns a random error code
* [Revision #3774](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3774)\
  Mon 2013-05-20 13:41:03 +0200
  * increase MAX\_HA (number of simultaneously installed storage engines) to 64
* [Revision #3773](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3773) \[merge]\
  Mon 2013-05-20 12:36:30 +0200
  * 5.3 merge. change maria.distinct to use a function that doesn't require ssl-enabled builds
  * [Revision #2502.567.102](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.102) \[merge]\
    Mon 2013-05-20 11:13:07 +0200
    * 5.2 merge
    * [Revision #2502.566.49](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.49) \[merge]\
      Mon 2013-05-20 10:53:04 +0200
      * 5.1 merge
      * [Revision #2502.565.49](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.49)\
        Sat 2013-05-11 20:23:57 +0300
        * Fixed compiler failure on solaris
      * [Revision #2502.565.48](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.48)\
        Sat 2013-05-11 18:57:06 +0300
        * Fixed compiler warning
      * [Revision #2502.565.47](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.47)\
        Sat 2013-05-11 15:55:11 +0300
        * [MDEV-4280](https://jira.mariadb.org/browse/MDEV-4280): Assertion \`empty\_size == empty\_size\_on\_page' failure in ma\_blockrec.c or ER\_NOT\_KEYFILE on query with DISTINCT and GROUP BY This could happen when using Aria for internal temporary files (default case) and using DISTINCT. \_ma\_scan\_restore\_block\_record() didn't work correctly if there was rows inserted, updated or deleted on the handler between calls to \_ma\_scan\_remember\_block\_record() and \_ma\_scan\_restore\_block\_record(). The effect was that some DISTINCT queries that used remove\_dup\_with\_compare() could fail.
      * [Revision #2502.565.46](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.46)\
        Tue 2013-04-09 09:58:51 +0300
        * [MDEV-4326](https://jira.mariadb.org/browse/MDEV-4326) fix.
    * [Revision #2502.566.48](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.48)\
      Sun 2013-05-19 16:38:56 +0200
      * [MDEV-4544](https://jira.mariadb.org/browse/MDEV-4544) - update MSI to include HeidiSQL 8.0
    * [Revision #2502.566.47](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.47)\
      Sun 2013-05-19 16:22:33 +0200
      * Fix cpack error - safe\_process.pl does not exist anymore.
    * [Revision #2502.566.46](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.46)\
      Wed 2013-05-08 14:32:32 +0200
      * [MDEV-4462](https://jira.mariadb.org/browse/MDEV-4462) mysqld gets SIGFPE when mysql.user table is empty
  * [Revision #2502.567.101](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.101)\
    Fri 2013-05-03 16:07:13 +0300
    * [MDEV-4290](https://jira.mariadb.org/browse/MDEV-4290): Fix agregate function resolution in derived tables (no name resolution over a derived table border)
  * [Revision #2502.567.100](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.100) \[merge]\
    Sun 2013-05-05 05:32:55 +0400
    * Merge
* [Revision #3772](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3772)\
  Sun 2013-05-19 17:42:30 +0200
  * remove start menu shortcut to upgrade wizard
* [Revision #3771](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3771)\
  Sun 2013-05-19 17:41:22 +0200
  * [MDEV-4544](https://jira.mariadb.org/browse/MDEV-4544) : Update MSI installer to use latest HeidiSQL 8.0
* [Revision #3770](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3770)\
  Fri 2013-05-17 10:16:56 +0400
  * Bug#[MDEV-4518](https://jira.mariadb.org/browse/MDEV-4518) Server crashes in is\_white\_space when it's run with query cache, charset ucs2 and collation ucs2\_unicode\_ci
* [Revision #3769](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3769)\
  Wed 2013-05-15 16:28:12 +0300\
  \*
  * Solaris fixes: - Fixed that wait\_timeout\_func and wait\_timeout tests works on solaris - We have to compile without NO\_ALARM on Solaris as Solaris doesn't support timeouts on sockets with setsockopt(.. SO\_RCVTIMEO). - Fixed that compile-solaris-amd64-debug works (before that we got a wrong ELF class: ELFCLASS64 on linkage) - Fixed some compiler warnings - Fixed some failing tests
* [Revision #3768](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3768)\
  Wed 2013-05-15 02:36:37 +0500
  * [MDEV-4266](https://jira.mariadb.org/browse/MDEV-4266) Server upgrade via apt-get install does not work. Now empty 'highlevel' packages strictly depend on the same versions of files. These are mariadb-server, mariadb-client, mariadb-test
* [Revision #3767](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3767)\
  Wed 2013-05-15 02:33:29 +0500
  * [MDEV-4521](https://jira.mariadb.org/browse/MDEV-4521) MBRContains, MBRWithin no longer work with geometries of different type. get\_mm\_leaf function can store all sorts of spatial features in one type of field it receives from an Item\_field. So we just allow that by setting the type of this field to GEOMETRY.
* [Revision #3766](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3766)\
  Tue 2013-05-14 18:32:16 +0300
  * When one does 'REPAIR TABLE', update uuid() to the current system
* [Revision #3765](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3765)\
  Tue 2013-05-14 14:49:52 +0200
  * Fix test failure in plugins.unix\_socket when running tests as user root.
* [Revision #3764](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3764)\
  Mon 2013-05-13 16:11:39 +0200
  * [MDEV-4514](https://jira.mariadb.org/browse/MDEV-4514) After increasing user name length mysql.db is reported broken and event scheduler does not start
* [Revision #3763](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3763)\
  Mon 2013-05-13 15:49:48 +0200
  * [MDEV-4505](https://jira.mariadb.org/browse/MDEV-4505) Buffer overrun when processing --log-bin parameter without file name
* [Revision #3762](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3762)\
  Mon 2013-05-13 15:49:27 +0200
  * [MDEV-4199](https://jira.mariadb.org/browse/MDEV-4199) Installing postfix on CentOS 5.9 requires MariaDB-server
* [Revision #3761](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3761)\
  Mon 2013-05-13 15:46:58 +0200
  * fix test cases
* [Revision #3760](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3760)\
  Mon 2013-05-13 00:43:46 +0300
  * Fixed [MDEV-4291](https://jira.mariadb.org/browse/MDEV-4291): Assertion \`trid >= info->s->state.create\_trid' failure or data corruption (key points to record outside datafile) on INSERT into an Aria table.
* [Revision #3759](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3759)\
  Sun 2013-05-12 11:29:16 +0300
  * [MDEV-3999](https://jira.mariadb.org/browse/MDEV-3999): Valgrind errors 'invalid write' or assorted server crashes on concurrent flow with partitioned Aria tables [MDEV-3989](https://jira.mariadb.org/browse/MDEV-3989): Server crashes on import from MariaDB mysqldump export with partitioned Aria table.
* [Revision #3758](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3758)\
  Sat 2013-05-11 20:31:50 +0300
  * Fixed that SHOW PROCESSLIST and information\_schema.processlist uses the right length for user names. Fixed some failing tests
* [Revision #3757](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3757)\
  Sat 2013-05-11 12:20:21 +0300
  * [MDEV-4231](https://jira.mariadb.org/browse/MDEV-4231): Possible bug in function \_ma\_apply\_undo\_row\_insert() Added comment to clearify the code.
* [Revision #3756](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3756)\
  Thu 2013-05-09 23:25:57 +0200
  * Fix compile error
* [Revision #3755](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3755)\
  Thu 2013-05-09 22:21:07 +0200
  * Small mysql\_install\_db.exe fixes - Use lc-messages-dir instead of deprecated --language when running mysqld in bootstrap mode. - Add some verbosity to mysql\_install\_db.exe when it runs in course of MSI installation.
* [Revision #3754](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3754)\
  Wed 2013-05-08 20:37:17 +0200
  * [MDEV-4206](https://jira.mariadb.org/browse/MDEV-4206) : log all slow statements (do not use filters), if log\_slow\_filter is empty.
* [Revision #3753](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3753)\
  Wed 2013-05-08 13:36:17 +0400
  * The bug [MDEV-4489](https://jira.mariadb.org/browse/MDEV-4489) "Replication of big5, cp932, gbk, sjis strings makes wrong values on slave" has been fixed.
* [Revision #3752](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3752) \[merge]\
  Wed 2013-05-08 10:12:21 +0200
  * Merge with XtraDB as of Percona-Server-5.5.30-rel30.2
  * [Revision #0.12.62](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.62)\
    Wed 2013-05-08 09:52:54 +0200
    * Percona-Server-5.5.30-rel30.2.tar.gz
* [Revision #3751](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3751)\
  Tue 2013-05-07 18:28:36 +0200
  * centos5 gcc 4.1 asm bug
* [Revision #3750](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3750)\
  Tue 2013-05-07 18:26:22 +0200
  * Compilation warnings. openssl compilation problem.
* [Revision #3749](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3749) \[merge]\
  Tue 2013-05-07 13:05:09 +0200
  * mysql-5.5.31 merge
  * [Revision #3077.184.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.184.3) \[merge]\
    Thu 2013-01-10 10:11:53 +1100
    * Merge from mysql-5.1 to mysql-5.5.
    * [Revision #2661.844.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.2)\
      Thu 2013-01-10 10:01:50 +1100
      * Bug#13997024 SEGV IN SYNC\_ARRAY\_CELL\_PRINT PRINTING OUT LONG SEMAPHORE WAIT DATA
* [Revision #3748](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3748)\
  Mon 2013-05-06 16:51:41 +0300
  * If one declared several continue handler for the same condition on different level of stored procedures, all of them where executed. Now we only execute the innermost of them (the most relevant).
* [Revision #3747](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3747) \[merge]\
  Sun 2013-05-05 05:38:09 +0400
  * [MDEV-4482](https://jira.mariadb.org/browse/MDEV-4482) fix null-merged to 5.5
  * [Revision #3745.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3745.1.1) \[merge]\
    Sun 2013-05-05 05:29:33 +0400
    * Merge
    * [Revision #2502.577.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.577.1)\
      Sun 2013-05-05 05:27:02 +0400
      * [MDEV-4482](https://jira.mariadb.org/browse/MDEV-4482): main.windows test fails in buildbot with result mismatch - Rollback an earlier patch (was pushed into 5.3 instead of 5.5)
* [Revision #3746](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3746) \[merge]\
  Sat 2013-05-04 21:56:45 -0700
  * Merge 5.3->5.5
  * [Revision #2502.567.99](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.99)\
    Fri 2013-05-03 22:46:45 -0700
    * Fixed bug [MDEV-4336](https://jira.mariadb.org/browse/MDEV-4336). When iterating over a list of conditions using List\_iterator the function remove\_eq\_conds should skip all predicates that replace a condition from the list. Otherwise it can come to an infinite recursion.
  * [Revision #2502.567.98](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.98)\
    Fri 2013-05-03 18:45:20 -0700
    * Made consistent handling of the predicates of the form IS NULL in outer joins with that in inner joins. Previously such condition was transformed into the condition = 0 unless the field belonged to an inner table of an outer join. In this case the predicate was interpreted as for any other field. Now if the field in the predicate IS NULL belongs to an inner table of an outer join the predicate is transformed into the disjunction = 0 OR IS NULL. This is fully compatible with the semantics of such predicates in 5.5.
  * [Revision #2502.567.97](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.97)\
    Mon 2013-04-29 20:31:40 -0700
    * Fixed bug [MDEV-4274](https://jira.mariadb.org/browse/MDEV-4274). This bug was the result of incompleteness of the patch for bug [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177). When an OR condition is simplified to a single conjunct it is merged into the embedding AND condition. Multiple equalities are also merged, and any field item involved in those equality should acquire a pointer to a the multiple equality formed by this merge.
* [Revision #3745](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3745)\
  Sat 2013-05-04 20:42:43 +0400
  * [MDEV-4071](https://jira.mariadb.org/browse/MDEV-4071): Valgrind warnings 'Invalid read' in subselect\_engine::calc\_const\_tables with ... - Call tmp\_having->update\_used\_tables() _before_ we have call JOIN::cleanup(). Making the call after join::cleanup() is not allowed, because subquery predicate items walk parent join's JOIN\_TAB structures. Which can be invalidated by JOIN::cleanup().
* [Revision #3744](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3744)\
  Sat 2013-05-04 21:02:07 +0400
  * [MDEV-389](https://jira.mariadb.org/browse/MDEV-389): Wrong result (missing row) with semijoin, join\_cache\_level>4 ... - Added testcase
* [Revision #3743](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3743)\
  Sat 2013-05-04 13:05:24 +0400
  * Update testcase result
* [Revision #3742](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3742)\
  Sat 2013-05-04 01:08:20 +0400
  * [MDEV-4270](https://jira.mariadb.org/browse/MDEV-4270): crash in fix\_semijoin\_strategies\_for\_picked\_join\_order - Added testcase
* [Revision #3741](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3741)\
  Sat 2013-05-04 00:56:50 +0400
  * [MDEV-621](https://jira.mariadb.org/browse/MDEV-621): [Bug #693329](https://bugs.launchpad.net/bugs/693329) - Assertion \`!is\_interleave\_error' failed on low optimizer\_search\_depth - When restore\_prev\_nj\_state() is called for the table that is the last remaining child of a nested join, do not leave that nested join's bit in join->cur\_embedding\_map.
* [Revision #3740](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3740)\
  Fri 2013-05-03 00:10:43 +0400
  * [MDEV-4465](https://jira.mariadb.org/browse/MDEV-4465): Reproducible crash (mysqld got signal 11) in multi\_delete::initialize\_tables... - make multi\_delete::initialize\_tables() take into account that the JOIN structure may have semi-join nests (which are not fully initialized when this function is called, they have tab->table=NULL which caused the crash) - Also checked multi\_update::initialize\_tables(): it has a different logic and needed no fixing.
* [Revision #3739](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3739)\
  Tue 2013-04-30 00:29:47 +0200
  * [MDEV-4458](https://jira.mariadb.org/browse/MDEV-4458) - Windows installer does not launch upgrade wizard anymore, even if there are upgradable instances (i.e windows service of lower MariaDB/MySQL version)
* [Revision #3738](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3738)\
  Sun 2013-04-28 14:28:46 +0200
  * fix test on Windows
* [Revision #3737](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3737)\
  Sat 2013-04-27 23:28:48 -0700
  * Fixed bug [MDEV-4340](https://jira.mariadb.org/browse/MDEV-4340). The function make\_join\_statistics checks whether eq\_ref access uses only constant expressions, and, if this is the case the function performs constant row substitution. The code of this check must take into account hidden components of extended secondary keys.
* [Revision #3736](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3736)\
  Thu 2013-04-25 15:11:59 +0200
  * Fix build on Windows
* [Revision #3735](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3735)\
  Thu 2013-04-25 13:16:35 +0200
  * Fix unsigned/signed conversion bug in event type during mysql\_binlog\_send().
* [Revision #3734](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3734)\
  Mon 2013-04-22 16:22:39 +0200
  * [MDEV-4396](https://jira.mariadb.org/browse/MDEV-4396): Fix sporadic failure of test innodb.innodb\_bug14676111
* [Revision #3733](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3733)\
  Fri 2013-04-19 12:50:16 +0200
  * [MDEV-260](https://jira.mariadb.org/browse/MDEV-260) auditing table accesses
* [Revision #3732](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3732)\
  Fri 2013-04-19 12:08:55 +0200
  * [MDEV-4398](https://jira.mariadb.org/browse/MDEV-4398) - Change default for innodb\_use\_fallocate to FALSE, due to bugs in older Linux kernels (posix\_fallocate() does not always guarantee that file size is like one specified)
* [Revision #3731](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3731)\
  Thu 2013-04-18 22:17:29 +0200
  * [MDEV-4332](https://jira.mariadb.org/browse/MDEV-4332) Increase username length from 16 characters
* [Revision #3730](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3730)\
  Wed 2013-04-17 19:42:34 +0200
  * strmake\_buf(X,Y) helper, equivalent to strmake(X,Y,sizeof(X)-1) with a bit of lame protection against abuse.
* [Revision #3729](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3729)\
  Tue 2013-04-16 18:52:23 +0200
  * debug\_sync is only available in debug build.
* [Revision #3728](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3728)\
  Tue 2013-04-16 17:33:47 +0200
  * Fix race in test case.
* [Revision #3727](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3727)\
  Tue 2013-04-16 09:42:09 +0200
  * [MDEV-3882](https://jira.mariadb.org/browse/MDEV-3882): .deb versions lower than upstream repo, causing install failure
* [Revision #3726](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3726)\
  Sun 2013-04-14 16:48:16 +0200
  * compiler warnings
* [Revision #3725](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3725)\
  Sun 2013-04-14 10:00:42 +0200
  * add missing tests
* [Revision #3724](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3724)\
  Fri 2013-04-12 13:19:00 +0300
  * Increase default value of max\_binlog\_cache\_size and max\_binlog\_stmt\_cache\_size to ulonglong\_max. This fixes that by default LOAD DATA INFILE will not generate the error: "Multi-statement transaction required more than 'max\_binlog\_cache\_size' bytes of storage..."
* [Revision #3723](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3723)\
  Fri 2013-04-12 01:05:29 +0200
  * complier warnings. hide the redundant condition under #ifdef (because only there it makes any sense)
* [Revision #3722](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3722) \[merge]\
  Fri 2013-04-12 01:01:18 +0200
  * 5.3 merge
  * [Revision #2502.567.96](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.96) \[merge]\
    Thu 2013-04-11 19:35:39 +0200
    * 5.2 merge
    * [Revision #2502.566.45](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.45) \[merge]\
      Thu 2013-04-11 19:30:59 +0200
      * 5.1 merge
      * [Revision #2502.565.45](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.45)\
        Sat 2013-04-06 21:29:12 +0200
        * [MDEV-4244](https://jira.mariadb.org/browse/MDEV-4244) \[PATCH] Buffer overruns and use-after-free errors
      * [Revision #2502.565.44](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.44)\
        Thu 2013-04-04 11:35:10 +0200
        * [MDEV-4088](https://jira.mariadb.org/browse/MDEV-4088) Replication 10.0 -> 5.5 fails
  * [Revision #2502.567.95](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.95)\
    Sat 2013-04-06 15:51:08 +0200
    * [MDEV-4244](https://jira.mariadb.org/browse/MDEV-4244) \[PATCH] Buffer overruns and use-after-free errors
  * [Revision #2502.567.94](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.94)\
    Sat 2013-04-06 15:14:46 +0200
    * [MDEV-4316](https://jira.mariadb.org/browse/MDEV-4316) MariaDB server crash with signal 11
  * [Revision #2502.567.93](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.93)\
    Mon 2013-04-08 12:04:28 +0300
    * If a range tree has a branch that is an expensive constant, currently get\_mm\_tree skipped the evaluation of this constant and icorrectly proceeded. The correct behavior is to return a NULL subtree, according to the IF branch being fixed - when it evaluates the constant it returns a value, and doesn't continue further.
  * [Revision #2502.567.92](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.92)\
    Thu 2013-04-04 12:34:31 +0400
    * Update tests results, mysql-test/r/windows.result
* [Revision #3721](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3721)\
  Sun 2013-04-07 20:32:39 +0200
  * [MDEV-4356](https://jira.mariadb.org/browse/MDEV-4356) : MariaDB does not start if bind-address gets resolved to more than single IP address.
* [Revision #3720](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3720)\
  Sat 2013-04-06 00:36:10 +0200
  * [MDEV-4338](https://jira.mariadb.org/browse/MDEV-4338) - Support FusionIO/directFS atomic writes
* [Revision #3719](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3719)\
  Sat 2013-04-06 00:35:45 +0200
  * [MDEV-4338](https://jira.mariadb.org/browse/MDEV-4338) - Support FusionIO/directFS atomic writes
* [Revision #3718](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3718)\
  Thu 2013-04-04 11:37:23 +0200
  * compilation warnings
* [Revision #3717](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3717)\
  Thu 2013-04-04 11:37:13 +0200
  * fix have\_debug\_sync.inc to be more robust (debug\_sync value can have single quotes)
* [Revision #3716](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3716)\
  Thu 2013-04-04 11:05:04 +0200
  * [MDEV-4161](https://jira.mariadb.org/browse/MDEV-4161) Assertion \`status\_var.memory\_used == 0' fails in virtual THD::THD()
* [Revision #3715](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3715)\
  Thu 2013-03-28 20:04:14 +0100
  * [MDEV-4243](https://jira.mariadb.org/browse/MDEV-4243) Warnings/errors while compiling with clang
* [Revision #3714](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3714) \[merge]\
  Wed 2013-04-03 18:51:29 +0400
  * Merge 5.3 -> 5.5
  * [Revision #2502.567.91](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.91)\
    Mon 2013-04-01 18:03:14 +0400
    * [MDEV-4240](https://jira.mariadb.org/browse/MDEV-4240): [mariadb 5.3.12](../../old-releases/5.3/5.3.12.md) using more memory than MySQL 5.1 for an inefficient query - Let index\_merge allocate table handlers on quick select's MEM\_ROOT, not on statement's MEM\_ROOT. This is crucial for big "range checked for each record" queries, where index\_merge can be created and deleted many times during query exection. We should not make O(#rows) allocations on statement's MEM\_ROOT.
  * [Revision #2502.567.90](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.90)\
    Fri 2013-03-29 19:27:06 +0400
    * [MDEV-4335](https://jira.mariadb.org/browse/MDEV-4335): Unexpected results when selecting on information\_schema - When converting a subquery to a semi-join, propagate OPTION\_SCHEMA\_TABLE.
* [Revision #3713](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3713)\
  Fri 2013-03-29 17:53:21 +0200
  * Fix for [MDEV-4144](https://jira.mariadb.org/browse/MDEV-4144)
* [Revision #3712](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3712)\
  Fri 2013-03-29 14:56:09 +0100
  * [MDEV-4243](https://jira.mariadb.org/browse/MDEV-4243) : remove several clang warnings.
* [Revision #3711](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3711) \[merge]\
  Thu 2013-03-28 19:18:36 -0700
  * Merge 5.3->5.5.
  * [Revision #2502.567.89](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.89) \[merge]\
    Wed 2013-03-27 08:58:16 -0700
    * Merge.
    * [Revision #2502.576.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.576.1)\
      Fri 2013-03-22 21:33:06 -0700
      * Fixed bug [MDEV-4318](https://jira.mariadb.org/browse/MDEV-4318). In some cases, when using views the optimizer incorrectly determined possible join orders for queries with nested outer and inner joins. This could lead to invalid execution plans for such queries.
* [Revision #3710](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3710) \[merge]\
  Wed 2013-03-27 22:22:52 -0700
  * Merge
  * [Revision #3700.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3700.1.1)\
    Wed 2013-03-27 19:17:32 -0700
    * Fixed bug [MDEV-4311](https://jira.mariadb.org/browse/MDEV-4311) (bug #68749). This bug was introduced by the patch for [WL#3220](https://askmonty.org/worklog/?tid=3220). If the memory allocated for the tree to store unique elements to be counted is not big enough to include all of them then an external file is used to store the elements. The unique elements are guaranteed not to be nulls. So, when reading them from the file we don't have to care about the null flags of the read values. However, we should remove the flag at the very beginning of the process. If we don't do it and if the last value written into the record buffer for the field whose distinct values needs to be counted happens to be null, then all values read from the file are considered to be nulls and are not counted in. The fix does not remove a possible null flag for the read values. Rather it just counts the values in the same way it was done before WL #3220.
* [Revision #3709](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3709) \[merge]\
  Wed 2013-03-27 10:03:28 +0100
  * 5.3 merge
  * [Revision #2502.567.88](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.88) \[merge]\
    Tue 2013-03-26 19:09:47 +0100
    * 5.2 merge
    * [Revision #2502.566.44](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.44) \[merge]\
      Tue 2013-03-26 17:39:45 +0100
      * 5.1 merge
      * [Revision #2502.565.43](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.43)\
        Wed 2013-03-20 21:20:51 +0100
        * add 'plugins' suite - empty, but the line ./mtr --suite=main,plugins will work on all branches.
      * [Revision #2502.565.42](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.42)\
        Tue 2013-03-19 17:25:58 +0400
        * [MDEV-4295](https://jira.mariadb.org/browse/MDEV-4295) Server crashes in get\_point on a query with Area, AsBinary, MultiPoint. Need to check if the number of points is 0 for the polygon.
      * [Revision #2502.565.41](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.41)\
        Tue 2013-03-19 17:16:10 +0400
        * [MDEV-4296](https://jira.mariadb.org/browse/MDEV-4296) Assertion \`n\_linear\_rings > 0' fails in Gis\_polygon::centroid\_xy. Forgotten DBUG\_ASSERT should be replaced with the 'return error'.
      * [Revision #2502.565.40](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.40)\
        Mon 2013-03-18 15:07:52 +0200
        * [MDEV-4269](https://jira.mariadb.org/browse/MDEV-4269) fix. Item\_default\_value inherited form Item\_field so should create temporary table field similary.
      * [Revision #2502.565.39](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.39)\
        Mon 2013-03-18 17:58:00 +0400
        * [MDEV-4252](https://jira.mariadb.org/browse/MDEV-4252) geometry query crashes server. Additional fixes for possible overflows in length-related calculations in 'spatial' implementations. Checks added to the ::get\_data\_size() methods. max\_n\_points decreased to occupy less 2G size. An object of that size is practically inoperable anyway.
      * [Revision #2502.565.38](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.38)\
        Mon 2013-03-18 10:35:03 +0100
        * [MDEV-4289](https://jira.mariadb.org/browse/MDEV-4289) Assertion \`0' fails in make\_sortkey with GROUP\_CONCAT, MAKE\_SET, GROUP BY
      * [Revision #2502.565.37](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.37)\
        Sun 2013-03-10 23:08:05 +0400
        * [MDEV-4252](https://jira.mariadb.org/browse/MDEV-4252) geometry query crashes server. The bug was found by Alyssa Milburn. If the number of points of a geometry feature read from binary representation is greater than 0x10000000, then the (uint32) (num\_points \* 16) will cut the higher byte, which leads to various errors. Fixed by additional check if (num\_points > max\_n\_points).
  * [Revision #2502.567.87](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.87)\
    Tue 2013-03-26 21:47:06 +0400
    * GEOMETRYCOLLECTION EMPTY handling fixed. The get\_mbr() method shouldn't return the error, rather an invalid MBR in this case.
  * [Revision #2502.567.86](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.86)\
    Tue 2013-03-26 13:07:46 +0200
    * [MDEV-4292](https://jira.mariadb.org/browse/MDEV-4292) fix.
  * [Revision #2502.567.85](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.85)\
    Fri 2013-03-22 17:32:27 +0400
    * [MDEV-4310](https://jira.mariadb.org/browse/MDEV-4310) geometry function equals hangs forever. The Geometry::get\_mbr() function can return an error on a bad data. We have to check for that and act respectively.
  * [Revision #2502.567.84](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.84) \[merge]\
    Thu 2013-03-21 11:07:38 +0400
    * Merge
    * [Revision #2502.575.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.575.1)\
      Thu 2013-03-21 11:06:27 +0400
      * [MDEV-4277](https://jira.mariadb.org/browse/MDEV-4277): Crash inside mi\_killed\_in\_mariadb() with myisammrg - Set MI\_INFO::external\_ref for MyISAM tables that are parts of myisamMRG table.
  * [Revision #2502.567.83](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.83)\
    Wed 2013-03-20 16:13:00 +0100
    * [MDEV-4293](https://jira.mariadb.org/browse/MDEV-4293) Valgrind warnings (Conditional jump or move depends on uninitialised value) in remove\_eq\_conds on time functions with NULL argument
  * [Revision #2502.567.82](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.82)\
    Mon 2013-03-18 08:44:24 +0100
    * [MDEV-4283](https://jira.mariadb.org/browse/MDEV-4283) Assertion \`scale <= precision' fails in strings/decimal.c
  * [Revision #2502.567.81](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.81)\
    Sun 2013-03-17 17:44:15 +0100
    * [MDEV-4286](https://jira.mariadb.org/browse/MDEV-4286) Server crashes in Protocol\_text::store, stack smashing detected
  * [Revision #2502.567.80](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.80)\
    Sun 2013-03-17 07:41:22 +0100
    * [MDEV-4281](https://jira.mariadb.org/browse/MDEV-4281) Assertion \`maybe\_null && item->null\_value' fails in make\_sortkey on CASE with different return types, GROUP\_CONCAT, GROUP BY
* [Revision #3708](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3708)\
  Tue 2013-03-26 19:17:26 +0100
  * [MDEV-4307](https://jira.mariadb.org/browse/MDEV-4307) Support at least 48 utf8 characters in username in server and PAM
* [Revision #3707](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3707)\
  Tue 2013-03-26 17:57:36 +0100
  * fix @@external\_user variable
* [Revision #3706](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3706)\
  Mon 2013-03-25 16:38:00 +0100
  * fixes for windows
* [Revision #3705](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3705)\
  Wed 2013-03-20 20:56:14 +0100
  * [MDEV-249](https://jira.mariadb.org/browse/MDEV-249) QUERY CACHE INFORMATION
* [Revision #3704](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3704)\
  Tue 2013-03-19 15:25:58 +0100
  * extend check\_global\_access() to avoid my\_error when it's not needed (in INFORMATION\_SCHEMA).
* [Revision #3703](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3703)\
  Tue 2013-03-26 10:34:21 +0100
  * Fixes for Windows XP
* [Revision #3702](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3702)\
  Tue 2013-03-26 08:17:22 +0100
  * [MDEV-4330](https://jira.mariadb.org/browse/MDEV-4330) - get\_tty\_password() does not work if input redirection is used.
* [Revision #3701](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3701)\
  Mon 2013-03-25 16:45:24 +0200
  * Patch by Ian Good for [MDEV-4319](https://jira.mariadb.org/browse/MDEV-4319): mysqlbinlog output ambiguous escaping
* [Revision #3700](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3700)\
  Sun 2013-03-17 11:41:25 +0100
  * [MDEV-4284](https://jira.mariadb.org/browse/MDEV-4284) Assertion \`cmp\_items\[(uint)cmp\_type]' fails in sql/item\_cmpfunc.cc
* [Revision #3699](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3699)\
  Thu 2013-03-14 19:07:20 +0200
  * [MDEV-4272](https://jira.mariadb.org/browse/MDEV-4272) fix.
* [Revision #3698](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3698)\
  Thu 2013-03-14 18:39:22 +0200
  * OPTION is now a valid identifier (not a reserved word)
* [Revision #3697](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3697)\
  Thu 2013-03-14 16:52:20 +0400
  * [MDEV-4214](https://jira.mariadb.org/browse/MDEV-4214) : main.partition\_rename\_longfilename fails on eCryptFS Adding an include file which checks whether long names are supported
* [Revision #3696](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3696)\
  Wed 2013-03-13 22:33:52 +0100
  * [MDEV-4265](https://jira.mariadb.org/browse/MDEV-4265) 5.5 is slower than 5.3 because of many str\_to\_datetime calls
* [Revision #3695](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3695)\
  Mon 2013-03-11 21:00:08 +0100
  * fix innodb failures on solaris
* [Revision #3694](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3694)\
  Tue 2013-03-12 21:06:46 +0100
  * Fix clang warning (suggest parentheses)
* [Revision #3693](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3693)\
  Tue 2013-03-12 20:11:05 +0100
  * [MDEV-4267](https://jira.mariadb.org/browse/MDEV-4267) : do not copy sql\_yacc.cc and sql\_yacc.h from unpacked source tarball into build directory, if usable bison is installed on the build machine.
* [Revision #3692](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3692)\
  Tue 2013-03-12 20:09:49 +0100
  * [MDEV-4224](https://jira.mariadb.org/browse/MDEV-4224) : func\_math test fails, when clang 3.0 compiler is used.
* [Revision #3691](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3691)\
  Wed 2013-03-06 13:30:40 +0100
  * [MDEV-4249](https://jira.mariadb.org/browse/MDEV-4249) : when autodetecting default client charset on Windows, fallback to GetACP() whenever GetConsoleCP() returns 0 (i.e appkication does not have a console , which is the case for GUI apps, Windows services etc)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
