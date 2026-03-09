# MariaDB 5.1.66 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.1.66) | [Release Notes](../../old-releases/5.1/5.1.66.md) | **Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 29 Nov 2012

For the highlights of this release, see the [release notes](../../old-releases/5.1/5.1.66.md).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #3172](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3172)\
  Thu 2012-11-22 18:27:02 +0100
  * Feedback plugin now recognizes Windows 8 / Windows Server 2012.
* [Revision #3171](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3171)\
  Tue 2012-11-20 13:28:53 +0100
  * [MDEV-3861](https://jira.mariadb.org/browse/MDEV-3861): assertions in TC\_LOG\_MMAP.
* [Revision #3170](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3170)\
  Mon 2012-11-19 11:18:40 +0100
  * potential crash in the feedback plugin
* [Revision #3169](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3169)\
  Sat 2012-11-17 19:04:13 +0100
  * [MDEV-3850](https://jira.mariadb.org/browse/MDEV-3850) too early pthread\_mutex\_unlock in TC\_LOG\_MMAP::log\_xid
* [Revision #3168](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3168)\
  Mon 2012-11-12 19:56:51 +0100
  * followup fixes for MySQL Bug #13889741: HANDLE\_FATAL\_SIGNAL IN _DB\_ENTER_ | HANDLE\_FATAL\_SIGNAL IN STRNLEN
* [Revision #3167](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3167)\
  Sat 2012-11-10 20:36:18 +0100
  * [MDEV-3849](https://jira.mariadb.org/browse/MDEV-3849) - 1 bytes stack overwrite in normalize\_dirname().
* [Revision #3166](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3166)\
  Fri 2012-11-09 20:15:23 +0100
  * add a test case for MySQL Bug #13889741: HANDLE\_FATAL\_SIGNAL IN _DB\_ENTER_ | HANDLE\_FATAL\_SIGNAL IN STRNLEN
* [Revision #3165](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3165)\
  Wed 2012-11-07 17:48:02 +0200
  * Updated test results after the mysql 5.1 merge.
* [Revision #3164](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3164) \[merge]\
  Tue 2012-11-06 11:52:55 +0200
  * Merge MySQL 5.1.66 -> MariaDB 5.1.65
  * [Revision #2502.1195.40](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.40)\
    Tue 2012-09-11 12:47:32 +0200
    * Spec file change to work around cast ulonglong -> int.
  * [Revision #2502.1195.39](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.39)\
    Wed 2012-09-05 17:40:13 +0200
    * Bug#13734987 MEMORY LEAK WITH I\_S/SHOW AND VIEWS WITH SUBQUERY
  * [Revision #2502.1195.38](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.38)\
    Mon 2012-09-03 11:33:05 +0530
  * [Revision #2502.1195.37](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.37)\
    Fri 2012-08-31 15:42:00 +0530
    * Bug #13453036 ERROR CODE 1118: ROW SIZE TOO LARGE - EVEN THOUGH IT IS NOT.
  * [Revision #2502.1195.36](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.36)\
    Fri 2012-08-31 09:51:27 +0300
  * [Revision #2502.1195.35](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.35)\
    Thu 2012-08-30 21:53:41 +0300
    * Bug#14554000 CRASH IN PAGE\_REC\_GET\_NTH\_CONST(NTH=0) DURING COMPRESSED PAGE SPLIT
  * [Revision #2502.1195.34](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.34)\
    Thu 2012-08-30 21:49:24 +0300
    * Bug#14547952: DEBUG BUILD FAILS ASSERTION IN RECORDS\_IN\_RANGE()
  * [Revision #2502.1195.33](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.33)\
    Tue 2012-08-28 14:51:01 +0200
    * Bug#14547952: DEBUG BUILD FAILS ASSERTION IN RECORDS\_IN\_RANGE()
  * [Revision #2502.1195.32](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.32)\
    Tue 2012-08-21 10:47:17 +0300
    * Fix regression from Bug#12845774 OPTIMISTIC INSERT/UPDATE USES WRONG HEURISTICS FOR COMPRESSED PAGE SIZE
  * [Revision #2502.1195.31](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.31)\
    Mon 2012-08-20 12:39:36 +0200
    * Bug#13025132 - PARTITIONS USE TOO MUCH MEMORY
  * [Revision #2502.1195.30](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.30) \[merge]\
    Mon 2012-08-20 11:18:17 +0200
    * merge
    * [Revision #2502.1197.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1197.2)\
      Fri 2012-08-17 14:25:32 +0200
      * Bug#13025132 - PARTITIONS USE TOO MUCH MEMORY
    * [Revision #2502.1197.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1197.1)\
      Wed 2012-08-15 14:31:26 +0200
      * Bug#13025132 - PARTITIONS USE TOO MUCH MEMORY
  * [Revision #2502.1195.29](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.29)\
    Fri 2012-08-17 13:14:04 +0400
    * Backporting Bug 14100466 from 5.6.
  * [Revision #2502.1195.28](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.28)\
    Thu 2012-08-16 17:45:39 +0300
    * Bug#12595091 POSSIBLY INVALID ASSERTION IN BTR\_CUR\_PESSIMISTIC\_UPDATE()
  * [Revision #2502.1195.27](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.27)\
    Thu 2012-08-16 17:37:52 +0300
    * Bug#12845774 OPTIMISTIC INSERT/UPDATE USES WRONG HEURISTICS FOR COMPRESSED PAGE SIZE
  * [Revision #2502.1195.26](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.26)\
    Thu 2012-08-16 17:31:23 +0300
    * Bug#13523839 ASSERTION FAILURES ON COMPRESSED INNODB TABLES
  * [Revision #2502.1195.25](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.25)\
    Tue 2012-08-14 14:11:01 +0530
    * Bug#13596613:SHOW SLAVE STATUS GIVES WRONG OUTPUT WITH MASTER-MASTER AND USING SET USE
  * [Revision #2502.1195.24](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.24)\
    Sat 2012-08-11 15:43:04 +0530
    * Bug #13115401: -SSL-KEY VALUE IS NOT VALIDATED AND IT ALLOWS INSECURE CONNECTIONS IF SPE
  * [Revision #2502.1195.23](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.23)\
    Thu 2012-08-09 15:34:52 +0400
    * Bug #14409015 MEMORY LEAK WHEN REFERENCING OUTER FIELD IN HAVING When resolving outer fields, Item\_field::fix\_outer\_fields() creates new Item\_refs for each execution of a prepared statement, so these must be allocated in the runtime memroot. The memroot switching before resolving JOIN::having causes these to be allocated in the statement root, leaking memory for each PS execution.
  * [Revision #2502.1195.22](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.22) \[merge]\
    Thu 2012-08-09 10:48:25 +0300
    * Merge from mysql-5.1 to working copy.
    * [Revision #2502.1196.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1196.1) \[merge]\
      Thu 2012-08-09 08:50:43 +0200
      * Merge from mysql-5.1.65-release
  * [Revision #2502.1195.21](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.21)\
    Thu 2012-08-09 09:55:29 +0300
    * Bug#14399148 INNODB TABLES UNDER LOAD PRODUCE DUPLICATE COPIES OF ROWS IN QUERIES
  * [Revision #2502.1195.20](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.20)\
    Wed 2012-08-08 22:15:46 +0530
    * BUG#11757312: MYSQLBINLOG DOES NOT ACCEPT INPUT FROM STDIN WHEN STDIN IS A PIPE
  * [Revision #2502.1195.19](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.19)\
    Tue 2012-08-07 18:58:19 +0530
    * Bug#13928675 MYSQL CLIENT COPYRIGHT NOTICE MUST SHOW 2012 INSTEAD OF 2011
  * [Revision #2502.1195.18](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.18)\
    Tue 2012-08-07 16:23:53 +0530
    * Bug#14068244: INCOMPATIBILITY BETWEEN LIBMYSQLCLIENT/LIBMYSQLCLIENT\_R AND LIBCRYPTO
  * [Revision #2502.1195.17](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.17)\
    Sun 2012-08-05 16:29:28 +0530
    * Bug #14099846: EXPORT\_SET CRASHES DUE TO OVERALLOCATION OF MEMORY
  * [Revision #2502.1195.16](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.16)\
    Tue 2012-07-31 20:41:46 +0200
    * INSTALL-BINARY placeholder: change invalid URLs (request from Kristofer)
  * [Revision #2502.1195.15](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.15)\
    Fri 2012-07-27 09:13:10 +0200
    * Bug#14111180 HANDLE\_FATAL\_SIGNAL IN PTR\_COMPARE\_1 / QUEUE\_INSERT
  * [Revision #2502.1195.14](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.14)\
    Fri 2012-07-27 12:05:37 +0530
    * Bug #12876932 - INCORRECT SELECT RESULT ON FEDERATED TABLE
  * [Revision #2502.1195.13](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.13)\
    Thu 2012-07-26 23:44:43 +0530
    * BUG#13868860 - LIMIT '5' IS EXECUTED WITHOUT ERROR WHEN '5' IS PLACE HOLDER AND USE SERVER-SIDE
  * [Revision #2502.1195.12](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.12)\
    Thu 2012-07-26 23:23:04 +0530
    * Bug #12876932 - INCORRECT SELECT RESULT ON FEDERATED TABLE
  * [Revision #2502.1195.11](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.11)\
    Thu 2012-07-26 21:47:03 +0530
    * Bug#13741677 MYSQL\_SECURE\_INSTALLATION DOES NOT WORK + SAVES ROOT PASSWORD TO DISK!
  * [Revision #2502.1195.10](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.10)\
    Thu 2012-07-26 15:05:24 +0200
    * Backport of Bug#14171740 65562: STRING::SHRINK SHOULD BE A NO-OP WHEN ALLOCED=0
  * [Revision #2502.1195.9](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.9)\
    Thu 2012-07-26 15:09:22 +0530
    * Bug #12876932 - INCORRECT SELECT RESULT ON FEDERATED TABLE
  * [Revision #2502.1195.8](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.8)\
    Wed 2012-07-25 13:51:39 +0530
    * Bug #13113026 INFORMATION\_SCHEMA.INNODB\_BUFFER\_PAGE\_LRUFROM 5.6 BACKPORT
  * [Revision #2502.1195.7](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.7)\
    Tue 2012-07-24 09:27:00 +0400
    * Fixing wrong copyright. Index.xml was modified in 2005, while the copyright notice still mentioned 2003.
  * [Revision #2502.1195.6](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.6)\
    Thu 2012-07-19 15:55:41 +0200
    * Reverting broken configure/make stuff
  * [Revision #2502.1195.5](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.5)\
    Thu 2012-07-19 12:57:36 +0200
    * Bug #14035452 - MODULARIZE MYSQL\_CLIENT\_TEST Added new minimal client using same framework Added internal test using it Small changes to top level make/configure/cmake to have it built
  * [Revision #2502.1195.4](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.4)\
    Thu 2012-07-19 13:52:34 +0530
    * Bug #12615411 - server side help doesn't work as first statement
  * [Revision #2502.1195.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.3)\
    Wed 2012-07-18 14:36:08 +0530
    * Bug#11762052: 54599: BUG IN QUERY PLANNER ON QUERIES WITH "ORDER BY" AND "LIMIT BY" CLAUSE
  * [Revision #2502.1195.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.2)\
    Thu 2012-07-12 16:42:07 +0530
    * Bug #11765218 58157: INNODB LOCKS AN UNMATCHED ROW EVEN THOUGH USING RBR AND RC
  * [Revision #2502.1195.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1195.1)\
    Wed 2012-07-11 15:18:34 +0200
    * Raise version number after cloning 5.1.65
* [Revision #3163](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3163) \[merge]\
  Thu 2012-11-01 16:20:09 +0100
  * Merge XtraDB from Percona-Server 5.1.66-rel14.1 into [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md).
  * [Revision #0.6.48](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/0.6.48)\
    Thu 2012-11-01 15:16:42 +0100
    * Updated with changes from Percona Server 5.1.66-rel14.1 tarball.
* [Revision #3162](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3162)\
  Wed 2012-10-31 23:49:51 +0200
  * Fixed [MDEV-612](https://jira.mariadb.org/browse/MDEV-612), [Bug #1010759](https://bugs.launchpad.net/bugs/1010759) - Valgrind error ha\_maria::check\_if\_incompatible\_data on
* [Revision #3161](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3161)\
  Wed 2012-10-31 23:22:32 +0200
  * Fixed [MDEV-647](https://jira.mariadb.org/browse/MDEV-647),[Bug #986261](https://bugs.launchpad.net/bugs/986261) - Aria unit tests fail at ma\_test2
* [Revision #3160](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3160)\
  Thu 2012-09-27 12:25:45 +0200
  * Fix incorrect assembler in Taocrypt which causes crashes on i386 with certain GCC versions/options
* [Revision #3159](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3159)\
  Wed 2012-09-26 11:59:49 +0200
  * always force the language in mysql\_install\_db
* [Revision #3158](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3158)\
  Wed 2012-09-26 15:30:08 +0200
  * Fix some failures in 5.1 Buildbot:
* [Revision #3157](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3157)\
  Mon 2012-09-24 11:33:41 +0200
  * [MDEV-543](https://jira.mariadb.org/browse/MDEV-543) mysql\_install\_db doesn't work with blanks in either basedir or datadir path
* [Revision #3156](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3156)\
  Fri 2012-08-24 19:11:54 +0200
  * Fix compiler warning
* [Revision #3155](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3155)\
  Fri 2012-08-24 15:32:44 +0200
  * Fix compiler warnings
* [Revision #3154](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3154) \[merge]\
  Fri 2012-08-24 10:34:55 +0200
  * Merge with latest 5.1.
  * [Revision #3151.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3151.1.1)\
    Fri 2012-08-24 10:06:16 +0200
    * [MDEV-382](https://jira.mariadb.org/browse/MDEV-382): Incorrect quoting ([CVE-2012-4414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-4414) )
* [Revision #3153](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3153)\
  Wed 2012-08-22 16:10:31 +0200
  * merge with XtraDB as of Percona-Server-5.1.63-rel13.4
* [Revision #3152](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3152) \[merge]\
  Wed 2012-08-22 11:40:39 +0200
  * merge with MySQL 5.1.65
  * [Revision #2502.1137.219](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.219) \[merge]\
    Thu 2012-07-12 10:00:14 +0200
    * Merge unpushed changes from 5.1.64-release
    * [Revision #2502.1194.4](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1194.4)\
      Tue 2012-06-26 16:30:15 +0200
      * Solve a linkage problem with "libmysqld" on several Solaris platforms: a multiple definition of 'THD::clear\_error()' in (at least) libmysqld.a(lib\_sql.o) and libmysqld.a(libfederated\_a-ha\_federated.o).
    * [Revision #2502.1194.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1194.3)\
      Thu 2012-06-21 16:26:50 +0200
      * Fixing wrong comment syntax (discovered by Kent)
    * [Revision #2502.1194.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1194.2)\
      Wed 2012-06-20 13:10:13 +0200
      * Version for this release build is 5.1.64
    * [Revision #2502.1194.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1194.1) \[merge]\
      Wed 2012-06-20 13:06:32 +0200
      * Merge
  * [Revision #2502.1137.218](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.218)\
    Tue 2012-07-10 18:55:07 +0530
  * [Revision #2502.1137.217](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.217) \[merge]\
    Tue 2012-07-10 13:51:50 +0300
    * merge from 5.1 repo.
    * [Revision #2502.1193.6](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1193.6)\
      Tue 2012-07-10 11:57:24 +0200
      * mysql\_client\_fw.c was not included in make dist
  * [Revision #2502.1137.216](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.216) \[merge]\
    Tue 2012-07-10 13:00:03 +0300
    * merge from 5.1 repo.
    * [Revision #2502.1193.5](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1193.5)\
      Tue 2012-07-10 14:23:17 +0530
      * BUG#11762670:MY\_B\_WRITE RETURN VALUE IGNORED
  * [Revision #2502.1137.215](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.215) \[merge]\
    Tue 2012-07-10 12:48:23 +0300
    * merge from 5.1 repo.
    * [Revision #2502.1193.4](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1193.4)\
      Tue 2012-07-10 10:04:57 +0200
      * mysql\_client\_test did not build within limbysqld/examples
    * [Revision #2502.1193.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1193.3)\
      Mon 2012-07-09 16:36:50 +0200
      * Fixed compile error in mysql\_client\_test using gcc
    * [Revision #2502.1193.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1193.2)\
      Mon 2012-07-09 15:10:07 +0200
      * Refactor mysql\_client\_test.c into a framework part and a test part
    * [Revision #2502.1193.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1193.1)\
      Thu 2012-07-05 13:41:16 +0300
      * Bug #13889741: HANDLE\_FATAL\_SIGNAL IN _DB\_ENTER_ | HANDLE\_FATAL\_SIGNAL IN STRNLEN
  * [Revision #2502.1137.214](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.214)\
    Thu 2012-07-05 14:37:48 +0300
    * Bug#14275000
  * [Revision #2502.1137.213](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.213)\
    Tue 2012-07-03 18:00:21 +0530
    * BUG#11762667:MYSQLBINLOG IGNORES ERRORS WHILE WRITING OUTPUT
  * [Revision #2502.1137.212](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.212)\
    Fri 2012-06-29 18:24:43 +0400
    * minor update to make MSVS happy
  * [Revision #2502.1137.211](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.211)\
    Thu 2012-06-28 18:38:55 +0300
    * Bug #13708485: malformed resultset packet crashes client
  * [Revision #2502.1137.210](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.210)\
    Fri 2012-06-29 13:25:57 +0200
    * Bug#14238406 NEW COMPILATION WARNINGS WITH GCC 4.7 (-WERROR=NARROWING)
  * [Revision #2502.1137.209](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.209)\
    Fri 2012-06-29 12:55:45 +0400
    * Backport of the deprecation warning from [WL#6219](https://askmonty.org/worklog/?tid=6219): "Deprecate and remove YEAR(2) type"
  * [Revision #2502.1137.208](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.208) \[merge]\
    Thu 2012-06-28 14:34:49 +0200
    * Merge.
    * [Revision #2502.1192.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1192.1)\
      Mon 2012-06-18 09:20:12 +0200
      * Bug#13003736 CRASH IN ITEM\_REF::WALK WITH SUBQUERIES
  * [Revision #2502.1137.207](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.207)\
    Tue 2012-06-19 12:56:40 +0530
    * Bug#11753779: MAX\_CONNECT\_ERRORS WORKS ONLY WHEN 1ST INC\_HOST\_ERRORS() IS CALLED.
  * [Revision #2502.1137.206](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.206)\
    Fri 2012-06-15 13:31:27 +0200
    * Raise version number after cloning 5.1.64
  * [Revision #2502.1137.205](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.205)\
    Thu 2012-06-14 17:07:49 +0530
    * BUG #13946716: FEDERATED\_PLUGIN TEST CASE FAIL ON 64BIT ARCHITECTURES
  * [Revision #2502.1137.204](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.204)\
    Wed 2012-06-13 16:03:58 +0530
    * Bug#11753779: MAX\_CONNECT\_ERRORS WORKS ONLY WHEN 1ST INC\_HOST\_ERRORS() IS CALLED.
  * [Revision #2502.1137.203](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.203) \[merge]\
    Tue 2012-06-12 12:59:13 +0530
    * BUG#12400221 - 60926: BINARY LOG EVENTS LARGER THAN MAX\_ALLOWED\_PACKET
    * [Revision #2502.1191.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1191.1)\
      Mon 2012-05-21 12:57:39 +0530
      * BUG#12400221 - 60926: BINARY LOG EVENTS LARGER THAN MAX\_ALLOWED\_PACKET
  * [Revision #2502.1137.202](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.202)\
    Tue 2012-06-05 15:53:39 +0200
    * Bug#14051002 VALGRIND: CONDITIONAL JUMP OR MOVE IN RR\_CMP / MY\_QSORT
  * [Revision #2502.1137.201](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.201)\
    Fri 2012-06-01 14:12:57 +0530
    * Bug #13933132: \[ERROR] GOT ERROR -1 WHEN READING TABLE APPEARED WHEN KILLING
  * [Revision #2502.1137.200](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.200)\
    Thu 2012-05-31 22:28:18 +0530
  * [Revision #2502.1137.199](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.199)\
    Thu 2012-05-31 14:32:29 +0530
  * [Revision #2502.1137.198](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.198)\
    Wed 2012-05-30 14:00:29 +0530
  * [Revision #2502.1137.197](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.197)\
    Wed 2012-05-30 13:54:15 +0530
    * Fixing the build failure on Windows debug build.
  * [Revision #2502.1137.196](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.196)\
    Tue 2012-05-29 12:11:30 +0530
    * Bug#11762667: MYSQLBINLOG IGNORES ERRORS WHILE WRITING OUTPUT
  * [Revision #2502.1137.195](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.195)\
    Thu 2012-05-24 12:37:03 -0400
    * Bug #14100254 65389: MVCC IS BROKEN WITH IMPLICIT LOCK
  * [Revision #2502.1137.194](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.194)\
    Mon 2012-05-21 17:25:40 +0530
    * Bug #12752572 61579: REPLICATION FAILURE WHILE INNODB\_AUTOINC\_LOCK\_MODE=1 AND USING TRIGGER
  * [Revision #2502.1137.193](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.193)\
    Fri 2012-05-18 14:44:40 +0530
    * BUG#14005409 - 64624
  * [Revision #2502.1137.192](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.192)\
    Thu 2012-05-17 18:07:59 +0530
    * Bug#12636001 : deadlock from thd\_security\_context
  * [Revision #2502.1137.191](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.191)\
    Thu 2012-05-17 11:41:46 +0100
  * [Revision #2502.1137.190](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.190)\
    Thu 2012-05-17 10:15:54 +0530
  * [Revision #2502.1137.189](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.189)\
    Wed 2012-05-16 16:36:49 +0530
    * Bug #13943231: ALTER TABLE AFTER DISCARD MAY CRASH THE SERVER
  * [Revision #2502.1137.188](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.188)\
    Wed 2012-05-16 16:14:27 +0530
    * Bug #13955256: KEYCACHE CRASHES, CORRUPTIONS/HANGS WITH, FULLTEXT INDEX AND CONCURRENT DML.
  * [Revision #2502.1137.187](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.187)\
    Wed 2012-05-16 11:17:48 +0530
    * Bug #12752572 61579: REPLICATION FAILURE WHILE INNODB\_AUTOINC\_LOCK\_MODE=1 AND USING TRIGGER
  * [Revision #2502.1137.186](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.186)\
    Tue 2012-05-15 22:06:48 +0100
    * BUG#11754117 - 45670: INTVAR\_EVENTS FOR FILTERED-OUT QUERY\_LOG\_EVENTS ARE EXECUTED
  * [Revision #2502.1137.185](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.185)\
    Tue 2012-05-15 15:04:39 +0300
    * Bug#14025221 FOREIGN KEY REFERENCES FREED MEMORY AFTER DROP INDEX
  * [Revision #2502.1137.184](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.184)\
    Tue 2012-05-15 13:12:22 +0300
    * Bug #11761822: yassl rejects valid certificate which openssl accepts
  * [Revision #2502.1137.183](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.183)\
    Tue 2012-05-15 09:14:44 +0200
    * Added some extra optional path to test suites
  * [Revision #2502.1137.182](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.182)\
    Thu 2012-05-10 10:18:31 +0530
    * Bug #14007649 65111: INNODB SOMETIMES FAILS TO UPDATE ROWS INSERTED BY A CONCURRENT TRANSACTIO
  * [Revision #2502.1137.181](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.181) \[merge]\
    Tue 2012-05-08 07:19:14 +0200
    * Merge from mysql-5.1.63-release
  * [Revision #2502.1137.180](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.180)\
    Mon 2012-05-07 16:46:44 +0530
    * Bug #11754178 45740: MYSQLDUMP DOESN'T DUMP GENERAL\_LOG AND SLOW\_QUERY CAUSES RESTORE PROBLEM Problem Statement: ------------------ mysqldump is not having the dump stmts for general\_log and slow\_log tables. That is because of the fix for Bug#26121. Hence, after dropping the mysql database, and applying the dump by enabling the logging, "'general\_log' table not found" errors are logged into the server log file.
  * [Revision #2502.1137.179](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.179)\
    Fri 2012-04-27 19:38:13 +0900
    * Bug#11758510 (#50723): INNODB CHECK TABLE FATAL SEMAPHORE WAIT TIMEOUT POSSIBLY TOO SHORT FOR BI Fixed not to check timeout during the check table.
  * [Revision #2502.1137.178](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.178)\
    Thu 2012-04-26 08:17:14 -0700
    * InnoDB: Adjust error message when a dropped tablespace is accessed.
  * [Revision #2502.1137.177](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.177) \[merge]\
    Mon 2012-04-23 12:05:05 +0300
    * merge from 5.1 repo
    * [Revision #2502.1190.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1190.1)\
      Fri 2012-04-20 22:25:59 +0100
      * BUG#13979418: SHOW BINLOG EVENTS MAY CRASH THE SERVER
  * [Revision #2502.1137.176](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.176)\
    Mon 2012-04-23 11:51:19 +0300
    * BUG#11754117
  * [Revision #2502.1137.175](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.175)\
    Fri 2012-04-20 19:41:20 +0300
    * BUG#11754117 incorrect logging of INSERT into auto-increment BUG#11761686 insert\_id event is not filtered.
  * [Revision #2502.1137.174](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.174)\
    Thu 2012-04-19 14:57:34 +0530
    * BUG#12427262 : 60961: SHOW TABLES VERY SLOW WHEN NOT IN SYSTEM DISK CACHE
  * [Revision #2502.1137.173](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.173)\
    Wed 2012-04-18 14:13:13 +0200
    * new header file must be listed in Makefile.am
  * [Revision #2502.1137.172](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.172)\
    Wed 2012-04-18 13:14:05 +0200
    * Backport 5.5=>5.1 Patch for Bug#13805127: Stored program cache produces wrong result in same THD.
  * [Revision #2502.1137.171](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.171)\
    Wed 2012-04-18 10:08:01 +0100
    * [WL#6236](https://askmonty.org/worklog/?tid=6236): Allow SHOW MASTER LOGS and SHOW BINARY LOGS with REPLICATION CLIENT
  * [Revision #2502.1137.170](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.170)\
    Wed 2012-04-18 11:25:01 +0530
    * Bug#12713907:STRANGE OPTIMIZE & WRONG RESULT UNDER ORDER BY COUNT(\*) LIMIT.
  * [Revision #2502.1137.169](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.169)\
    Tue 2012-04-17 13:25:41 +0300
    * Raise version number after cloning 5.1.63
* [Revision #3151](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3151)\
  Fri 2012-06-01 17:53:59 +0200
  * [MDEV-256](https://jira.mariadb.org/browse/MDEV-256) [Bug #995501](https://bugs.launchpad.net/bugs/995501) - mysqltest attempts to parse Perl code inside a block with false condition, gets confused and throws wrong errors
* [Revision #3150](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3150)\
  Fri 2012-05-18 12:42:06 +0200
  * post-merge fixes
* [Revision #3149](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3149) \[merge]\
  Thu 2012-05-17 12:12:33 +0200
  * merge with mysql-5.1.63
  * [Revision #2502.1184.18](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.18) \[merge]\
    Tue 2012-04-10 14:21:57 +0300
    * merge mysql-5.1->mysql-5.1-security
    * [Revision #2502.1137.168](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.168)\
      Mon 2012-04-09 16:42:41 +0530
      * Bug #11766072 59107: MYSQLSLAP CRASHES IF STARTED WITH NO ARGUMENTS ON WINDOWS
    * [Revision #2502.1137.167](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.167)\
      Fri 2012-04-06 17:03:13 +0530
      * BUG#13738989 : 62136 : FAILED TO FETCH SELECT RESULT USING EMBEDDED MYSQLD
    * [Revision #2502.1137.166](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.166)\
      Wed 2012-03-28 12:05:31 +0530
      * Bug#11763507 - 56224: FUNCTION NAME IS CASE-SENSITIVE
    * [Revision #2502.1137.165](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.165) \[merge]\
      Wed 2012-03-28 13:35:44 +1100
      * Merge from mysql-5.0
      * [Revision #1810.3997.22](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/1810.3997.22)\
        Wed 2012-03-28 13:08:25 +1100
        * Bug# 13847885 - PURGING STALLS WHEN PURGE\_SYS->N\_PAGES\_HANDLED OVERFLOWS
  * [Revision #2502.1137.164](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.164)\
    Tue 2012-03-27 14:39:27 +0200
    * Backport of fix for Bug#12763207 - ASSERT IN SUBSELECT::SINGLE\_VALUE\_TRANSFORMER
  * [Revision #2502.1137.163](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.163)\
    Tue 2012-03-27 12:42:11 +0530
  * Bug#11763507 - 56224: FUNCTION NAME IS CASE-SENSITIVE
  * [Revision #2502.1184.17](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.17)\
    Fri 2012-04-06 12:04:07 +0300
    * Bug #13934049: 64884: LOGINS WITH INCORRECT PASSWORD ARE ALLOWED
  * [Revision #2502.1184.16](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.16)\
    Wed 2012-04-04 13:29:45 +0400
    * Bug#11766300 59387: FAILING ASSERTION: CURSOR->POS\_STATE == 1997660512 (BTR\_PCUR\_IS\_POSITIONE Bug#13639204 64111: CRASH ON SELECT SUBQUERY WITH NON UNIQUE INDEX The crash happened due to wrong calculation of key length during creation of reference for sort order index. The problem is that keyuse->used\_tables can have OUTER\_REF\_TABLE\_BIT enabled but used\_tables parameter(create\_ref\_for\_key() func) does not have it. So key parts which have OUTER\_REF\_TABLE\_BIT are ommited and it could lead to incorrect key length calculation(zero key length).
  * [Revision #2502.1184.15](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.15) \[merge]\
    Wed 2012-03-21 14:58:27 +0200
  * empty weave merge mysql-5.0-security->mysql-5.1-security
  * [Revision #1810.4003.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/1810.4003.3) \[merge]\
    Wed 2012-03-21 14:35:25 +0200
    * weave merge mysql-5.0->mysql-5.0-security
  * [Revision #2502.1184.14](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.14) \[merge]\
    Wed 2012-03-21 14:53:09 +0200
  * merge mysql-5.1->mysql-5.1-security
  * [Revision #2502.1137.162](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.162) \[merge]\
    Wed 2012-03-21 11:18:21 +0100
    * Upmerge an empty merge changeset (backmerge of 5.0.96 into main 5.0), solve a conflict in ".bzr-mysql/default.conf".
    * [Revision #1810.3997.21](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/1810.3997.21) \[merge]\
      Tue 2012-03-20 17:30:49 +0100
      * Merge from mysql-5.0.96-release
  * [Revision #2502.1137.161](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.161) \[merge]\
    Tue 2012-03-20 17:35:41 +0100
    * Merge from mysql-5.1.62-release
  * [Revision #2502.1137.160](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.160)\
    Fri 2012-03-16 12:06:29 +0530
    * Bug #11766634 59783: INNODB DATA GROWS UNEXPECTEDLY WHEN INSERTING, TRUNCATING, INSERTING THE
  * [Revision #2502.1137.159](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.159)\
    Thu 2012-03-15 13:30:17 -0400
    * Bug#13825266 RACE IN LOCK\_VALIDATE() WHEN ACCESSING PAGES DIRECTLY FROM BUFFER POOL
  * [Revision #2502.1137.158](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.158)\
    Thu 2012-03-15 12:38:40 -0400
    * Bug#13851171 STRING OVERFLOW IN INNODB CODE FOUND BY STATIC ANALYSIS
  * [Revision #2502.1137.157](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.157)\
    Thu 2012-03-15 11:53:30 -0400
    * Bug#13537504 VALGRIND: COND. JUMP/MOVE DEPENDS ON UNINITIALISED VALUES IN OS\_THREAD\_EQ
  * [Revision #2502.1137.156](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.156)\
    Mon 2012-03-12 23:23:40 +0000
    * BUG#12400313
  * [Revision #2502.1137.155](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.155) \[merge]\
    Mon 2012-03-12 23:16:44 +0000
    * Automerge merge with latest mysql-5.1.
    * [Revision #2502.1189.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1189.2)\
      Mon 2012-03-12 23:15:01 +0000
      * BUG#12400313
  * [Revision #2502.1137.154](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.154) \[merge]\
    Mon 2012-03-12 21:58:00 +0000
    * BUG#12400313
    * [Revision #2502.1189.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1189.1)\
      Mon 2012-03-12 12:28:27 +0000
      * BUG#12400313 RELAY\_LOG\_SPACE\_LIMIT IS NOT WORKING IN MANY CASES BUG#64503: mysql frequently ignores --relay-log-space-limit
  * [Revision #2502.1137.153](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.153)\
    Fri 2012-03-09 11:07:16 +0530
    * Bug #11766634 59783: InnoDB data grows unexpectedly when inserting, truncating, inserting the same set of rows. When a table is re-created with the same set of rows, the data file size must not grow.
  * [Revision #2502.1137.152](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.152)\
    Thu 2012-03-08 17:10:10 +0200
    * Fix a compiler warning about possibly uninitiaizlied variable.
* [Revision #2502.1184.13](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.13)\
  Mon 2012-03-12 08:56:56 +0100
  * Bug#13031606 VALUES() IN A SELECT STATEMENT CRASHES SERVER
* [Revision #2502.1184.12](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.12)\
  Sun 2012-03-11 16:05:42 +0400
  * Fixed test case for bug #13105873 "valgrind warning:possible crash in foreign key handling on subsequent create table if not exists".
* [Revision #2502.1184.11](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.11) \[merge]\
  Thu 2012-03-08 17:20:03 +0200
  * empty weave merge mysql-5.0-security->mysql-5.1-security
  * [Revision #1810.4003.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/1810.4003.2) \[merge]\
    Thu 2012-03-08 17:15:43 +0200
    * empty auto merge of mysql-5.0->mysql-5.0-security
* [Revision #2502.1184.10](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.10) \[merge]\
  Thu 2012-03-08 17:16:53 +0200
  * merge mysql-5.1->mysql-5.1-security
  * [Revision #2502.1137.151](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.151)\
    Thu 2012-03-08 14:56:22 +0200
    * Bug#13807811 BTR\_PCUR\_RESTORE\_POSITION() CAN SKIP A RECORD
  * [Revision #2502.1137.150](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.150)\
    Tue 2012-03-06 13:30:30 +0100
    * Bug#11761576 54082: HANDLE\_SEGFAULT MAKES USE OF UNSAFE FUNCTIONS
  * [Revision #2502.1137.149](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.149) \[merge]\
    Wed 2012-02-29 20:51:38 +0100
    * merge into mysql-5.1
    * [Revision #2502.1188.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1188.1)\
      Mon 2012-02-20 22:59:11 +0100
      * Bug#11761296: 53775: QUERY ON PARTITIONED TABLE RETURNS CACHED RESULT FROM PREVIOUS TRANSACTION
  * [Revision #2502.1137.148](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.148) \[merge]\
    Wed 2012-02-29 14:52:08 +0530
    * Bug#12601974 - STORED PROCEDURE SQL\_MODE=NO\_BACKSLASH\_ESCAPES IGNORED AND BREAKS REPLICATION
    * [Revision #2502.1187.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1187.1)\
      Wed 2012-02-29 12:23:15 +0530
      * Bug#12601974 - STORED PROCEDURE SQL\_MODE=NO\_BACKSLASH\_ESCAPES IGNORED AND BREAKS REPLICATION
  * [Revision #2502.1137.147](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.147)\
    Tue 2012-02-28 21:41:55 +0200
    * Fix a mistake in the Bug#12861864 fix.
  * [Revision #2502.1137.146](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.146)\
    Tue 2012-02-28 14:00:00 +0200
    * Bug#12861864 RACE CONDITION IN BTR\_GET\_SIZE() AND DROP INDEX/TABLE/DATABASE also filed as Bug#13146269, Bug#13713178
  * [Revision #2502.1137.145](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.145)\
    Mon 2012-02-27 23:19:14 +0200
    * Remove a bogus BLOB debug assertion that was added in Bug#13721257 fix.
  * [Revision #2502.1137.144](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.144)\
    Fri 2012-02-24 11:53:36 +0530
    * Bug#13012483:EXPLAIN EXTENDED, PREPARED STATEMENT, CRASH IN CHECK\_SIMPLE\_EQUALITY
  * [Revision #2502.1137.143](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.143)\
    Tue 2012-02-21 17:57:07 +0200
    * Fix Bug#13639142 64128: INNODB ERROR IN SERVER LOG OF INNODB\_BUG34300
  * [Revision #2502.1137.142](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.142) \[merge]\
    Tue 2012-02-21 14:14:52 +0200
    * merged and updated the version in mysql-5.1
    * [Revision #1810.3997.20](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/1810.3997.20)\
      Tue 2012-02-21 14:13:31 +0200
      * bumped up the version of the main tree to match the security tree
  * [Revision #2502.1137.141](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1137.141)\
    Sun 2012-02-19 03:18:49 +0000
    * BUG 13454045 - 63524: BUG #35396 "ABNORMAL/IMPOSSIBLE/LARGE QUERY\_TIME AND LOCK\_TIME" HAPPENS A
* [Revision #2502.1184.9](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.9)\
  Tue 2012-03-06 15:13:56 +0400
  * BUG#12537203 - CRASH WHEN SUBSELECTING GLOBAL VARIABLES IN GEOMETRY FUNCTION ARGUMENTS
* [Revision #2502.1184.8](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.8)\
  Mon 2012-03-05 22:15:23 +0400
  * BUG#12537203 - CRASH WHEN SUBSELECTING GLOBAL VARIABLES IN GEOMETRY FUNCTION ARGUMENTS
* [Revision #2502.1184.7](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.7)\
  Mon 2012-03-05 21:58:07 +0400
  * Fix for BUG#12414917 - ISCLOSED() CRASHES ON 64-BIT BUILDS
* [Revision #2502.1184.6](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.6)\
  Thu 2012-03-01 15:44:23 +0530
  * The innodb plugin module cannot use DEBUG\_SYNC\_C facility on Windows. Taking care of it.
* [Revision #2502.1184.5](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.5)\
  Thu 2012-03-01 11:05:51 +0530
  * Bug#13635833: MULTIPLE CRASHES IN FOREIGN KEY CODE WITH CONCURRENT DDL/DML
* [Revision #2502.1184.4](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.4) \[merge]\
  Wed 2012-02-22 16:18:12 +0100
  * auto-merge
  * [Revision #2502.1186.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1186.1) \[merge]\
    Sun 2012-02-19 08:57:11 +0000
    * BUG#13431369 - MAIN.VARIABLES-NOTEMBEDDED CRASHES THE SERVER SPORADICALLY ON WINDOWS
    * [Revision #2502.1185.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1185.1)\
      Fri 2012-02-17 19:02:17 +0000
      * BUG#13431369 - MAIN.VARIABLES-NOTEMBEDDED CRASHES THE SERVER SPORADICALLY ON WINDOWS
* [Revision #2502.1184.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.3)\
  Wed 2012-02-22 11:17:50 +0100
  * Bug#13519724 63793: CRASH IN DTCOLLATION::SET(DTCOLLATION \&SET)
* [Revision #2502.1184.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.2) \[merge]\
  Tue 2012-02-21 11:06:08 +0200
  * merge 5.0-security->5.1-security
  * [Revision #1810.4003.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/1810.4003.1)\
    Mon 2012-02-20 06:19:12 +0100
    * Raise version number after cloning 5.0.96
* [Revision #2502.1184.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2502.1184.1)\
  Mon 2012-02-20 17:03:24 +0100
  * Raise version number after cloning 5.1.62
* [Revision #3148](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3148)\
  Sat 2012-05-12 11:53:14 +0400
  * BUG#997747: Assertion \`join->best\_read < ((double)1.79..5e+308L)' failed in greedy\_search with LEFT JOINs and unique keys - Backport the fix for BUG#806524 from [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md)
* [Revision #3147](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3147)\
  Tue 2012-04-24 17:29:03 +0200
  * [Bug #986120](https://bugs.launchpad.net/bugs/986120) Problem installing mariadb 5 on solaris 10
* [Revision #3146](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3146)\
  Fri 2012-04-06 13:31:33 +0500
  * [MDEV-80](https://jira.mariadb.org/browse/MDEV-80) Memory engine table full at much less than max\_heap\_table\_size with btree index. RB-tree index in the MEMORY table fails if it grews over 4G. That happened because the old\_allocated variable in hp\_rb\_write\_key() had the uint type. Changed with the 'size\_t' type to be same as the 'rb\_tree.allocated'.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
